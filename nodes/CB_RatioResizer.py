import torch
import torch.nn.functional as F

class CB_RatioResizer:
    COMMON_RATIOS = {
        "16:9": 16/9,
        "4:3": 4/3,
        "3:4": 3/4,
        "1:1": 1,
        "2:1": 2,
        "3:2": 3/2,
        "21:9": 21/9,
        "9:16": 9/16,
        "1:2": 0.5,
    }
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "target_size": ("INT", {"default": 1920, "min": 1280, "max": 4096, "step": 1})
            }
        }

    RETURN_TYPES = ("IMAGE", "INT", "INT", "IMAGE")
    RETURN_NAMES = ("corrected_image", "final_width", "final_height", "pad_mask")
    FUNCTION = "resize_and_pad"
    CATEGORY = "image/resize"

    def resize_and_pad(self, image, target_size):
        C, orig_height, orig_width = image.shape
        measured_ratio = orig_width / orig_height

        best_ratio_name, best_ratio = min(self.COMMON_RATIOS.items(), key=lambda x: abs(x[1] - measured_ratio))

        if orig_width > target_size or orig_height > target_size:
            scale = target_size / max(orig_width, orig_height)
            new_width = int(round(orig_width * scale))
            new_height = int(round(orig_height * scale))
            image_scaled = F.interpolate(image.unsqueeze(0), size=(new_height, new_width),
                                         mode='bilinear', align_corners=False).squeeze(0)
        else:
            new_width = orig_width
            new_height = orig_height
            image_scaled = image

        if best_ratio >= 1:
            canvas_width = target_size
            canvas_height = int(round(target_size / best_ratio))
        else:
            canvas_height = target_size
            canvas_width = int(round(target_size * best_ratio))

        if new_width > canvas_width or new_height > canvas_height:
            raise ValueError("Scaled image exceeds the calculated canvas size.")

        canvas = torch.full((C, canvas_height, canvas_width), 1.0, dtype=image.dtype, device=image.device)
        mask = torch.ones((1, canvas_height, canvas_width), dtype=image.dtype, device=image.device)

        offset_x = (canvas_width - new_width) // 2
        offset_y = (canvas_height - new_height) // 2
        canvas[:, offset_y:offset_y+new_height, offset_x:offset_x+new_width] = image_scaled
        mask[:, offset_y:offset_y+new_height, offset_x:offset_x+new_width] = 0

        return (canvas, canvas_width, canvas_height, mask)

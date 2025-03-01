import torch
import torch.nn.functional as F
from PIL import Image, ImageDraw

class CB_AdvancedResizer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "target_size": ("INT", {"default": 1024, "min": 1, "max": 8192, "step": 1}),
                "common_ratios": (
                    [
                        "1:1", "4:3", "3:2", "16:9", "21:9",
                        "3:4", "2:3", "9:16", "9:21", "Custom"
                    ],
                    {"default": "16:9"}
                ),
                "custom_ratio_width": ("INT", {"default": 16, "min": 1, "max": 4096, "step": 1, "cond_visible": False}),
                "custom_ratio_height": ("INT", {"default": 9, "min": 1, "max": 4096, "step": 1, "cond_visible": False}),
            },
            "optional": {
                "force_resize": (["true", "false"], {"default": "false"}),
            }

        }

    RETURN_TYPES = ("IMAGE", "INT", "INT", "MASK")
    RETURN_NAMES = ("resized_image", "final_width", "final_height", "padding_mask")
    FUNCTION = "resize_and_pad"
    CATEGORY = "image/resize"

    def resize_and_pad(self, image, target_size, common_ratios, custom_ratio_width=16, custom_ratio_height=9, force_resize="false"):
        orig_height, orig_width = image.shape[1], image.shape[2]
        orig_ratio = orig_width / orig_height

        if common_ratios == "Custom":
            target_ratio = custom_ratio_width / custom_ratio_height
        else:
            target_w, target_h = map(int, common_ratios.split(':'))
            target_ratio = target_w / target_h

        if force_resize == "true" or orig_width > target_size or orig_height > target_size:
            if orig_ratio > target_ratio:
                new_width = target_size
                new_height = int(target_size / orig_ratio)
            else:
                new_height = target_size
                new_width = int(target_size * orig_ratio)
            image = F.interpolate(image, size=(new_height, new_width), mode='bilinear', align_corners=False)
            resized_width, resized_height = new_width, new_height

        else:
            resized_width, resized_height = orig_width, orig_height
            new_width, new_height = orig_width, orig_height

        if resized_width / resized_height > target_ratio:
            final_width = resized_width
            final_height = int(resized_width / target_ratio)
            pad_top = (final_height - resized_height) // 2
            pad_bottom = final_height - resized_height - pad_top
            pad_left = 0
            pad_right = 0
        else:
            final_height = resized_height
            final_width = int(resized_height * target_ratio)
            pad_left = (final_width - resized_width) // 2
            pad_right = final_width - resized_width - pad_left
            pad_top = 0
            pad_bottom = 0

        padded_image = F.pad(image, (pad_left, pad_right, pad_top, pad_bottom), "constant", value=1.0)

        mask = torch.zeros((1, final_height, final_width), dtype=torch.float32, device=image.device)
        mask[:, pad_top:final_height - pad_bottom, pad_left:final_width - pad_right] = 1.0

        return (padded_image, final_width, final_height, mask)
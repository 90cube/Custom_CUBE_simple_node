from __future__ import annotations

from typing import List


class _BasePromptNode:
    CATEGORY = "utils/PromptEngineering"
    NONE_OPTION = "None"

    @classmethod
    def _normalize(cls, value: str | None) -> str:
        if value is None:
            return ""
        cleaned = value.strip()
        if not cleaned or cleaned.lower() == cls.NONE_OPTION.lower():
            return ""
        return cleaned

    @classmethod
    def _with_connector(cls, value: str | None, connector: str) -> str:
        normalized = cls._normalize(value)
        if not normalized:
            return ""
        connector_clean = connector.strip()
        return f"{normalized} {connector_clean}" if connector_clean else normalized

    @classmethod
    def _join_prompt(cls, *values: str) -> str:
        return ", ".join([clean for clean in (cls._normalize(value) for value in values) if clean])


class CB_HeadPromptNode(_BasePromptNode):
    """Build a headwear prompt from selectable options and free text."""

    wear_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "hat",
        "helmet",
        "band",
        "headband",
        "bandana",
        "beret",
        "beanie",
        "bonnet",
        "boater hat",
        "bow",
        "bowler hat",
        "bucket hat",
        "cap",
        "cowboy hat",
        "crown",
        "circlet",
        "diadem",
        "fedora",
        "flat cap",
        "flower crown",
        "garland",
        "goggles",
        "helmet with visor",
        "hijab",
        "hood",
        "hooded cloak",
        "horns",
        "maid headband",
        "mask",
        "nurse cap",
        "pirate hat",
        "ribbon",
        "sailor hat",
        "scarf headwrap",
        "sombrero",
        "sun hat",
        "tiara",
        "top hat",
        "turban",
        "veil",
        "visor",
        "witch hat",
        "wolf ears",
        "cat ears",
        "bunny ears",
        "fox ears",
        "elf ears",
        "hairclip",
        "hair ornament",
        "hair flowers",
        "headphones",
        "earmuffs",
    ]
    color_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "red",
        "blue",
        "yellow",
        "green",
        "black",
        "white",
        "gold",
        "silver",
        "orange",
        "purple",
        "pink",
        "brown",
        "gray",
        "charcoal",
        "ivory",
        "cream",
        "beige",
        "tan",
        "peach",
        "maroon",
        "burgundy",
        "navy",
        "teal",
        "turquoise",
        "cyan",
        "mint",
        "lime",
        "olive",
        "amber",
        "magenta",
        "lavender",
        "lilac",
        "rose",
        "copper",
        "bronze",
        "platinum",
    ]
    above_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "angel ring",
        "halo",
        "glowing halo",
        "floating crown",
        "floating stars",
        "shooting stars",
        "star",
        "sparkles",
        "butterflies",
        "flower petals",
        "floating feathers",
        "fireflies",
        "lanterns",
        "bubbles",
        "balloons",
        "clouds",
        "rainbow",
        "aurora",
        "crescent moon",
        "full moon",
        "sun",
        "moon",
        "comet",
        "meteor shower",
        "paper talismans",
        "prayer slips",
        "floating runes",
        "glowing sigils",
    ]
    behind_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "tails",
        "fox tails",
        "nine tails",
        "wolf tail",
        "cat tail",
        "bunny tail",
        "dragon tail",
        "wings",
        "angel wings",
        "fairy wings",
        "butterfly wings",
        "feathered wings",
        "demon wings",
        "dragon wings",
        "mecha wings",
        "ribbon trails",
        "flowing ribbons",
        "streamers",
        "collars",
        "cape",
        "hooded cape",
        "cloak",
        "backpack",
        "quiver",
        "sheath",
        "katana on back",
        "guitar on back",
        "floating swords",
        "floating daggers",
        "floating crystals",
        "aura",
        "light rays",
        "holy light",
        "dark aura",
        "flames",
        "blue flames",
        "smoke wisps",
        "petals",
        "leaves",
        "water splash",
        "glowing circuit",
        "geometric halo",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "wear": (cls.wear_options, {"default": cls.wear_options[0]}),
                "color": (cls.color_options, {"default": cls.color_options[0]}),
                "above": (cls.above_options, {"default": cls.above_options[0]}),
                "behind": (cls.behind_options, {"default": cls.behind_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, wear: str, color: str, above: str, behind: str, manual_input: str):
        return (self._join_prompt(manual_input, wear, color, above, behind),)


class CB_StylePromptNode(_BasePromptNode):
    """Build a style-focused prompt with era, medium, genre, and mood picks."""

    era_options: List[str] = [
        "ancient", "classical", "medieval", "renaissance", "baroque", "rococo", "victorian",
        "edwardian", "industrial", "art nouveau", "art deco", "mid-century modern", "retro",
        "1960s", "1970s", "1980s", "1990s", "y2k", "modern", "contemporary", "postmodern",
        "dieselpunk", "steampunk", "clockpunk", "atompunk", "solarpunk", "cyberpunk",
        "biopunk", "nanopunk", "retrofuturism", "fantasy medieval", "high fantasy",
        "dark fantasy", "grimdark", "mythic", "oriental fantasy", "wuxia", "xianxia",
        "samurai era", "viking", "arabesque", "byzantine", "aztec", "mayan", "egyptian",
        "greco-roman", "celtic", "tribal", "sci-fi", "space opera", "utopian", "dystopian",
    ]

    medium_options: List[str] = [
        "oil painting", "watercolor", "gouache", "ink wash", "pencil sketch", "charcoal sketch",
        "pastel", "marker", "digital painting", "vector art", "flat color", "cel shading",
        "manga", "anime", "comic book", "graphic novel", "cartoon", "storybook", "concept art",
        "matte painting", "matte illustration", "photorealistic", "hyperrealistic",
        "cinematic render", "3d render", "octane render", "unreal engine", "blender render",
        "low poly", "pixel art", "voxel art", "line art", "woodcut", "engraving", "etching",
        "stained glass", "mosaic", "ukiyo-e", "ink outlines", "neon glow", "spray paint",
        "graffiti", "collage", "paper cut", "silkscreen", "mixed media",
    ]

    genre_options: List[str] = [
        "portrait", "character sheet", "environment", "fashion illustration", "editorial",
        "street style", "runway", "fantasy adventure", "sci-fi adventure", "space marine",
        "mecha", "kaiju", "post-apocalyptic", "urban fantasy", "mythology", "surreal",
        "dreamlike", "noir", "gothic", "romantic", "pastoral", "heroic", "epic",
        "slice of life", "magical girl", "superhero", "villain", "military", "cyborg",
        "android", "mech pilot", "wizard", "witch", "alchemist", "assassin", "rogue",
        "paladin", "knight", "cleric", "archer", "ranger", "bard", "druid", "beastmaster",
        "stealth", "sports", "dance", "idol", "idol concert", "battle", "duel",
    ]

    mood_options: List[str] = [
        "bright", "cheerful", "playful", "whimsical", "romantic", "mysterious", "dramatic",
        "moody", "melancholic", "ethereal", "serene", "tranquil", "dreamy", "surreal glow",
        "gritty", "dark", "gothic", "grim", "ominous", "epic lighting", "cinematic",
        "high contrast", "low key", "high key", "soft light", "rim light", "volumetric light",
        "sunset lighting", "golden hour", "blue hour", "moonlit", "neon", "rainy",
        "foggy", "stormy", "snowy", "dusty", "desert heat haze",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "era": (cls.era_options, {"default": cls.era_options[0]}),
                "medium": (cls.medium_options, {"default": cls.medium_options[0]}),
                "genre": (cls.genre_options, {"default": cls.genre_options[0]}),
                "mood": (cls.mood_options, {"default": cls.mood_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, era: str, medium: str, genre: str, mood: str, manual_input: str):
        return (self._join_prompt(manual_input, era, medium, genre, mood),)


class CB_FullBodyPromptNode(_BasePromptNode):
    """Assemble a full-body framing and pose prompt."""

    framing_options: List[str] = [
        "full body shot", "long shot", "standing center frame", "wide shot", "group shot",
        "dynamic angle", "three-quarter view", "profile view", "rear view", "360 turntable",
        "establishing shot", "hero pose", "power pose", "leaping", "mid-air", "running",
        "sprinting", "walking", "kneeling", "sitting", "floating", "flying", "combat stance",
        "spellcasting", "summoning circle", "parkour", "jump kick", "landing pose",
    ]

    perspective_options: List[str] = [
        "eye level", "low angle", "worm's-eye view", "high angle", "bird's-eye view",
        "dutch angle", "tilted frame", "wide-angle lens", "fisheye lens", "telephoto lens",
        "close distance", "medium distance", "far distance", "cinematic framing",
    ]

    motion_options: List[str] = [
        "motion blur", "speed lines", "afterimage", "dynamic smear", "freeze frame",
        "bullet time", "time stop", "slow motion", "action lines", "dust kick", "debris burst",
        "water splash", "energy trail", "aura burst", "wind swirl",
    ]

    focus_options: List[str] = [
        "sharp focus", "bokeh background", "shallow depth of field", "deep focus",
        "subject spotlight", "rim-lit silhouette", "backlit", "soft vignette", "glow outline",
        "HDR", "high contrast", "film grain", "cinematic color grade",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "framing": (cls.framing_options, {"default": cls.framing_options[0]}),
                "perspective": (cls.perspective_options, {"default": cls.perspective_options[0]}),
                "motion": (cls.motion_options, {"default": cls.motion_options[0]}),
                "focus": (cls.focus_options, {"default": cls.focus_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, framing: str, perspective: str, motion: str, focus: str, manual_input: str):
        return (self._join_prompt(manual_input, framing, perspective, motion, focus),)


class CB_UpperBodyPromptNode(_BasePromptNode):
    """Craft an upper-body portrait prompt."""

    pose_options: List[str] = [
        "bust shot", "half body", "torso up", "waist up", "arms crossed", "hands on hips",
        "hands clasped", "leaning forward", "leaning back", "arms behind back", "one hand raised",
        "peace sign", "pointing", "hand on cheek", "chin resting on hand", "phone holding",
        "book holding", "coffee cup", "microphone", "musical instrument",
    ]

    angle_options: List[str] = [
        "front view", "three-quarter view", "side view", "over-the-shoulder", "looking back",
        "tilted head", "upward gaze", "downward gaze", "close-up", "intimate portrait",
    ]

    clothing_options: List[str] = [
        "casual jacket", "hoodie", "cardigan", "kimono", "hakama", "cheongsam", "hanbok top",
        "school uniform", "sailor uniform", "military coat", "leather jacket", "denim jacket",
        "vest", "corset", "bustier", "turtleneck", "button-up shirt", "sweater", "poncho",
        "capelet", "shrug", "armor breastplate", "mage robe", "cleric robes", "witch cloak",
    ]

    accessory_options: List[str] = [
        "brooch", "necklace", "choker", "amulet", "pendant", "dog tags", "tie", "bow tie",
        "ascot", "scarf", "shawl", "bandolier", "sash", "pauldrons", "shoulder guard",
        "armlet", "bracers", "arm warmers", "fingerless gloves", "gauntlets", "armored vambrace",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pose": (cls.pose_options, {"default": cls.pose_options[0]}),
                "angle": (cls.angle_options, {"default": cls.angle_options[0]}),
                "clothing": (cls.clothing_options, {"default": cls.clothing_options[0]}),
                "accessory": (cls.accessory_options, {"default": cls.accessory_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, pose: str, angle: str, clothing: str, accessory: str, manual_input: str):
        return (self._join_prompt(manual_input, pose, angle, clothing, accessory),)


class CB_LowerBodyPromptNode(_BasePromptNode):
    """Define lower-body clothing and stance prompts."""

    legwear_options: List[str] = [
        "jeans", "ripped jeans", "slacks", "dress pants", "cargo pants", "track pants",
        "yoga pants", "leggings", "shorts", "denim shorts", "bike shorts", "hotpants",
        "bermuda shorts", "skirt", "pleated skirt", "pencil skirt", "mini skirt", "maxi skirt",
        "sarong", "hakama pants", "hanbok bottoms", "cheongsam split", "kilt",
        "armor greaves", "chainmail skirt", "tabard", "loincloth", "battle skirt",
    ]

    stance_options: List[str] = [
        "standing straight", "contrapposto", "one leg raised", "crossed legs", "kneeling",
        "crouching", "sitting on ledge", "perched", "tiptoes", "mid-step", "dancing pose",
        "karate stance", "martial arts ready", "archer stance", "lunge", "high kick",
    ]

    detail_options: List[str] = [
        "belt", "utility belt", "holster", "garter belt", "suspenders", "leg strap", "thigh strap",
        "lace trim", "fishnet stockings", "striped stockings", "patterned tights", "armored tassets",
        "cuisses", "faulds", "battle skirt plates", "runed straps", "glowing runes", "tech panels",
        "jet thrusters", "floating cloth", "layered fabric", "frills", "ribbons", "chains",
    ]

    footwear_anchor_options: List[str] = [
        "ground contact", "floating pose", "hovering", "splashing water", "dust cloud",
        "grass field", "stone pavement", "metal deck", "wooden floor", "snow ground",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "legwear": (cls.legwear_options, {"default": cls.legwear_options[0]}),
                "stance": (cls.stance_options, {"default": cls.stance_options[0]}),
                "detail": (cls.detail_options, {"default": cls.detail_options[0]}),
                "anchor": (cls.footwear_anchor_options, {"default": cls.footwear_anchor_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, legwear: str, stance: str, detail: str, anchor: str, manual_input: str):
        return (self._join_prompt(manual_input, legwear, stance, detail, anchor),)


class CB_LegPromptNode(_BasePromptNode):
    """Describe leg coverage, pose, and embellishments with optional attachment phrasing."""

    legwear_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "bare legs",
        "jeans",
        "ripped jeans",
        "slacks",
        "dress pants",
        "cargo pants",
        "track pants",
        "yoga pants",
        "leggings",
        "shorts",
        "denim shorts",
        "bike shorts",
        "hotpants",
        "bermuda shorts",
        "skirt",
        "pleated skirt",
        "pencil skirt",
        "mini skirt",
        "maxi skirt",
        "sarong",
        "hakama pants",
        "hanbok bottoms",
        "cheongsam split",
        "kilt",
        "armor greaves",
        "chainmail skirt",
        "tabard",
        "loincloth",
        "battle skirt",
        "layered battle skirts",
        "runed leggings",
        "tech leggings",
    ]

    pose_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "standing straight",
        "contrapposto",
        "one leg raised",
        "crossed legs",
        "kneeling",
        "crouching",
        "sitting on ledge",
        "perched",
        "tiptoes",
        "mid-step",
        "dancing pose",
        "karate stance",
        "martial arts ready",
        "archer stance",
        "lunge",
        "high kick",
        "heroic stance",
    ]

    detail_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "belt",
        "utility belt",
        "holster",
        "garter belt",
        "suspenders",
        "leg strap",
        "thigh strap",
        "lace trim",
        "fishnet stockings",
        "striped stockings",
        "patterned tights",
        "armored tassets",
        "cuisses",
        "faulds",
        "battle skirt plates",
        "runed straps",
        "glowing runes",
        "tech panels",
        "jet thrusters",
        "floating cloth",
        "layered fabric",
        "frills",
        "ribbons",
        "chains",
    ]

    anchor_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "ground contact",
        "floating pose",
        "hovering",
        "splashing water",
        "dust cloud",
        "grass field",
        "stone pavement",
        "metal deck",
        "wooden floor",
        "snow ground",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "legwear": (cls.legwear_options, {"default": cls.legwear_options[0]}),
                "pose": (cls.pose_options, {"default": cls.pose_options[0]}),
                "detail": (cls.detail_options, {"default": cls.detail_options[0]}),
                "anchor": (cls.anchor_options, {"default": cls.anchor_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, legwear: str, pose: str, detail: str, anchor: str, manual_input: str):
        legwear_part = self._with_connector(legwear, "on legs")
        return (self._join_prompt(manual_input, legwear_part, pose, detail, anchor),)


class CB_ArmPromptNode(_BasePromptNode):
    """Describe arm coverings, gear, and poses with optional attachment phrasing."""

    armwear_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "bare arms",
        "short sleeves",
        "rolled sleeves",
        "long sleeves",
        "detached sleeves",
        "arm warmers",
        "fingerless arm warmers",
        "armored sleeves",
        "plate vambraces",
        "chainmail sleeves",
        "mage sleeves",
        "padded sleeves",
        "fur-trim sleeves",
        "kimono sleeves",
        "hakama sleeves",
        "tech sleeves",
        "mechanical arms",
        "cybernetic arms",
        "bandaged arms",
        "tattooed arms",
    ]

    pose_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "arms crossed",
        "arms behind back",
        "one arm raised",
        "both arms raised",
        "arms outstretched",
        "blocking pose",
        "spellcasting pose",
        "aiming bow",
        "guarding pose",
        "muscular flex",
        "delicate gesture",
    ]

    accessory_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "pauldrons",
        "shoulder guard",
        "armlet",
        "bracers",
        "fingerless gloves",
        "gauntlets",
        "armored vambrace",
        "ribbon wraps",
        "tech armbands",
        "glowing runes",
        "floating bangles",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "armwear": (cls.armwear_options, {"default": cls.armwear_options[0]}),
                "pose": (cls.pose_options, {"default": cls.pose_options[0]}),
                "accessory": (cls.accessory_options, {"default": cls.accessory_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, armwear: str, pose: str, accessory: str, manual_input: str):
        armwear_part = self._with_connector(armwear, "on arms")
        return (self._join_prompt(manual_input, armwear_part, pose, accessory),)


class CB_HandPromptNode(_BasePromptNode):
    """Describe hand coverage and items with automatic linking language."""

    glove_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "bare hands",
        "lace gloves",
        "fingerless gloves",
        "leather gloves",
        "gauntlet gloves",
        "mage gloves",
        "mechanical gloves",
        "clawed gloves",
        "padded gloves",
        "armored gauntlets",
        "chain gloves",
        "opera gloves",
        "fur gloves",
    ]

    held_item_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "sword",
        "dagger",
        "staff",
        "wand",
        "orb",
        "book",
        "lantern",
        "scroll",
        "shield",
        "flag",
        "gun",
        "bow",
        "microphone",
        "instrument",
        "hammer",
        "tool",
        "teacup",
        "flower bouquet",
        "spell circle",
    ]

    gesture_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "peace sign",
        "pointing",
        "hand on cheek",
        "chin resting on hand",
        "open palm",
        "closed fist",
        "reaching out",
        "delicate grasp",
        "spellcasting gesture",
        "martial arts guard",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "gloves": (cls.glove_options, {"default": cls.glove_options[0]}),
                "held_item": (cls.held_item_options, {"default": cls.held_item_options[0]}),
                "gesture": (cls.gesture_options, {"default": cls.gesture_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, gloves: str, held_item: str, gesture: str, manual_input: str):
        gloves_part = self._with_connector(gloves, "on hands")
        held_part = self._with_connector(held_item, "in hand")
        return (self._join_prompt(manual_input, gloves_part, held_part, gesture),)


class CB_FootPromptNode(_BasePromptNode):
    """Select footwear with an automatic "on foot" connector for active choices."""

    footwear_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "barefoot",
        "sneakers",
        "running shoes",
        "basketball shoes",
        "high-top sneakers",
        "skate shoes",
        "loafers",
        "oxfords",
        "derby shoes",
        "dress shoes",
        "brogues",
        "monk strap shoes",
        "combat boots",
        "military boots",
        "ankle boots",
        "chelsea boots",
        "cowboy boots",
        "riding boots",
        "thigh-high boots",
        "knee-high boots",
        "platform boots",
        "lace-up boots",
        "mary janes",
        "ballerina flats",
        "sandals",
        "gladiator sandals",
        "flip-flops",
        "clogs",
        "geta",
        "zori",
        "okobo",
        "wooden sandals",
        "armor sabatons",
        "mecha boots",
    ]

    sole_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "flat sole",
        "chunky sole",
        "platform sole",
        "high heels",
        "stiletto heels",
        "block heels",
        "wedge heels",
        "transparent heels",
        "glowing soles",
        "roller shoes",
        "cleats",
        "spiked soles",
        "hover soles",
        "maglev soles",
    ]

    decoration_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "buckles",
        "laces",
        "ribbons",
        "bows",
        "studs",
        "chains",
        "straps",
        "zippers",
        "fur trim",
        "shearling",
        "embroidery",
        "paint splatter",
        "neon trim",
        "LED lights",
        "rune etchings",
        "glowing patterns",
        "winged heels",
        "jet boosters",
        "steam vents",
    ]

    weathering_options: List[str] = [
        _BasePromptNode.NONE_OPTION,
        "brand new",
        "worn",
        "scuffed",
        "dusty",
        "muddy",
        "battle damage",
        "weathered leather",
        "polished",
        "mirror shine",
        "matte finish",
        "wet",
        "snow dusted",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "footwear": (cls.footwear_options, {"default": cls.footwear_options[0]}),
                "sole": (cls.sole_options, {"default": cls.sole_options[0]}),
                "decoration": (cls.decoration_options, {"default": cls.decoration_options[0]}),
                "weathering": (cls.weathering_options, {"default": cls.weathering_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, footwear: str, sole: str, decoration: str, weathering: str, manual_input: str):
        footwear_part = self._with_connector(footwear, "on foot")
        return (self._join_prompt(manual_input, footwear_part, sole, decoration, weathering),)


class CB_FacePromptNode(_BasePromptNode):
    """Generate facial detail prompts."""

    expression_options: List[str] = [
        "neutral expression", "gentle smile", "big smile", "laughing", "serious", "stoic",
        "focused", "determined", "angry", "pouting", "sad", "teary-eyed", "crying",
        "surprised", "shocked", "embarrassed", "blushing", "winking", "sleepy", "yawning",
        "smirking", "mischievous", "sly", "flustered", "dreamy gaze", "confident grin",
    ]

    eye_options: List[str] = [
        "large eyes", "narrow eyes", "almond eyes", "round eyes", "heterochromia", "glowing eyes",
        "mechanical eyes", "cyber eyes", "cat eyes", "dragon eyes", "fox eyes", "reptile eyes",
        "pupil-less", "star pupils", "heart pupils", "cross pupils", "ringed iris", "multicolor iris",
        "eyeliner", "bold eyeliner", "smokey eyes", "eyeshadow", "sparkling eyes", "tear mole",
    ]

    hair_options: List[str] = [
        "short hair", "bob cut", "long hair", "twintails", "ponytail", "side ponytail",
        "braids", "single braid", "french braid", "crown braid", "bun", "twin buns", "curly hair",
        "wavy hair", "straight hair", "messy hair", "spiky hair", "afro", "dreadlocks",
        "side shave", "undercut", "mohawk", "bangs", "side bangs", "ahoge", "antenna hair",
        "ombre hair", "gradient hair", "highlighted hair", "streaked hair", "glowing hair",
    ]

    adornment_options: List[str] = [
        "freckles", "beauty mark", "scar", "face paint", "warpaint", "tribal paint",
        "tattoos", "cyber tattoos", "glowing tattoos", "runic markings", "stickers",
        "bandages", "eyepatch", "monocle", "glasses", "sunglasses", "visor", "mask",
        "respirator", "rebreather", "ear cuffs", "ear piercings", "lip piercing", "nose ring",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "expression": (cls.expression_options, {"default": cls.expression_options[0]}),
                "eyes": (cls.eye_options, {"default": cls.eye_options[0]}),
                "hair": (cls.hair_options, {"default": cls.hair_options[0]}),
                "adornment": (cls.adornment_options, {"default": cls.adornment_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, expression: str, eyes: str, hair: str, adornment: str, manual_input: str):
        return (self._join_prompt(manual_input, expression, eyes, hair, adornment),)


class CB_SubItemPromptNode(_BasePromptNode):
    """Combine secondary equipment and props outside normal fashion."""

    cloak_options: List[str] = [
        "tattered cape", "hooded cloak", "travel cloak", "feathered cape", "fur mantle", "wolf pelt",
        "dragon scale cape", "phoenix feather cloak", "shadow cloak", "mist cloak",
        "glowing rune cloak", "transparent veil cloak", "royal mantle", "ceremonial cape",
    ]

    weapon_options: List[str] = [
        "longsword", "greatsword", "rapier", "katana", "tachi", "nodachi", "spear", "halberd",
        "glaive", "lance", "trident", "warhammer", "mace", "flail", "morning star", "battle axe",
        "double axe", "scythe", "dagger", "twin daggers", "throwing knives", "chakram", "bow",
        "longbow", "recurve bow", "crossbow", "gunblade", "revolver", "pistol", "rifle",
        "shotgun", "energy rifle", "railgun", "laser pistol", "magic staff", "wizard staff",
        "scepter", "orb staff", "spellbook", "grimoire", "summoning tome", "wand",
    ]

    gadget_options: List[str] = [
        "grappling hook", "smoke bomb", "flash bomb", "utility drones", "shoulder drone",
        "floating drone", "hologram projector", "wrist computer", "holo gauntlet", "wrist blades",
        "energy shield", "portable shield", "magical talisman", "soul gem", "mana crystal",
        "artifact amulet", "ancient relic", "arcane focus", "pocket watch", "compass", "lantern",
    ]

    ornament_options: List[str] = [
        "runed charm", "beads", "totem", "talisman", "dragon fang", "demon horn", "angel feather",
        "phoenix feather", "mystic bell", "floating rings", "levitating crystals", "geometric halo",
        "scroll case", "banner", "standard", "heraldic flag", "music instrument prop",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "cloak": (cls.cloak_options, {"default": cls.cloak_options[0]}),
                "weapon": (cls.weapon_options, {"default": cls.weapon_options[0]}),
                "gadget": (cls.gadget_options, {"default": cls.gadget_options[0]}),
                "ornament": (cls.ornament_options, {"default": cls.ornament_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(self, cloak: str, weapon: str, gadget: str, ornament: str, manual_input: str):
        return (self._join_prompt(manual_input, cloak, weapon, gadget, ornament),)


class CB_FantasyArmorPromptNode(_BasePromptNode):
    """Create armored outfit prompts with theme and material choices."""

    armor_type_options: List[str] = [
        "light leather armor", "studded leather", "scale mail", "chainmail", "brigandine",
        "plate armor", "full plate", "samurai armor", "oni armor", "templar armor",
        "paladin armor", "dragon armor", "phoenix armor", "angelic armor", "demonic armor",
        "gothic armor", "runic armor", "crystal armor", "bone armor", "living armor",
        "biotech armor", "nanotech suit", "powered exosuit", "mecha frame", "stealth suit",
    ]

    motif_options: List[str] = [
        "dragon motif", "phoenix motif", "griffin motif", "wolf motif", "lion motif",
        "serpent motif", "skull motif", "floral engravings", "celtic knots", "aztec patterns",
        "mayan glyphs", "runic engravings", "glowing runes", "angelic filigree", "demonic spikes",
        "winged pauldrons", "crowned helm", "horned helm", "crest helm", "mask helm",
    ]

    material_options: List[str] = [
        "polished steel", "blued steel", "blackened steel", "mithril", "adamantite", "orichalcum",
        "obsidian", "crystal", "prismatic crystal", "enchanted wood", "dragonbone", "ivory",
        "bronze", "brass", "copper", "gold", "rose gold", "silver", "platinum", "meteorite metal",
        "aether alloy", "mana-infused metal", "void metal", "liquid metal", "glass armor",
    ]

    embellishment_options: List[str] = [
        "fur trim", "feather trim", "silk lining", "cloak clasp", "banner sash", "tabard",
        "surcoat", "heraldry", "etched plates", "riveted plates", "spiked armor", "plated skirt",
        "chain skirt", "tasset plates", "cuirass engravings", "pauldron wings", "glowing seams",
        "arcane circuits", "floating shards", "energy shield emitters", "halo crest", "tailored fit",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "armor_type": (cls.armor_type_options, {"default": cls.armor_type_options[0]}),
                "motif": (cls.motif_options, {"default": cls.motif_options[0]}),
                "material": (cls.material_options, {"default": cls.material_options[0]}),
                "embellishment": (cls.embellishment_options, {"default": cls.embellishment_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"

    def build_prompt(
        self,
        armor_type: str,
        motif: str,
        material: str,
        embellishment: str,
        manual_input: str,
    ):
        return (self._join_prompt(manual_input, armor_type, motif, material, embellishment),)

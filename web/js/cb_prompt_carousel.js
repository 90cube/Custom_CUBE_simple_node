import { app } from "../../scripts/app.js";

const CB_SETTING_ID = "cbPromptCarouselEnabled";
const CB_SETTING_GUARD = "__cbPromptCarouselSettingRegistered";
const CB_SETTING_DEFAULT = true;
const NONE_LABEL = "None";
const PREVIEW_WIDGET_NAME = "__cb_prompt_preview";

const NODE_OPTION_MAP = {
    CB_HeadPromptNode: {
        wear: [
            "None",
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
        ],
        color: [
            "None",
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
        ],
        above: [
            "None",
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
        ],
        behind: [
            "None",
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
        ],
    },
    CB_StylePromptNode: {
        era: [
            "ancient",
            "classical",
            "medieval",
            "renaissance",
            "baroque",
            "rococo",
            "victorian",
            "edwardian",
            "industrial",
            "art nouveau",
            "art deco",
            "mid-century modern",
            "retro",
            "1960s",
            "1970s",
            "1980s",
            "1990s",
            "y2k",
            "modern",
            "contemporary",
            "postmodern",
            "dieselpunk",
            "steampunk",
            "clockpunk",
            "atompunk",
            "solarpunk",
            "cyberpunk",
            "biopunk",
            "nanopunk",
            "retrofuturism",
            "fantasy medieval",
            "high fantasy",
            "dark fantasy",
            "grimdark",
            "mythic",
            "oriental fantasy",
            "wuxia",
            "xianxia",
            "samurai era",
            "viking",
            "arabesque",
            "byzantine",
            "aztec",
            "mayan",
            "egyptian",
            "greco-roman",
            "celtic",
            "tribal",
            "sci-fi",
            "space opera",
            "utopian",
            "dystopian",
        ],
        medium: [
            "oil painting",
            "watercolor",
            "gouache",
            "ink wash",
            "pencil sketch",
            "charcoal sketch",
            "pastel",
            "marker",
            "digital painting",
            "vector art",
            "flat color",
            "cel shading",
            "manga",
            "anime",
            "comic book",
            "graphic novel",
            "cartoon",
            "storybook",
            "concept art",
            "matte painting",
            "matte illustration",
            "photorealistic",
            "hyperrealistic",
            "cinematic render",
            "3d render",
            "octane render",
            "unreal engine",
            "blender render",
            "low poly",
            "pixel art",
            "voxel art",
            "line art",
            "woodcut",
            "engraving",
            "etching",
            "stained glass",
            "mosaic",
            "ukiyo-e",
            "ink outlines",
            "neon glow",
            "spray paint",
            "graffiti",
            "collage",
            "paper cut",
            "silkscreen",
            "mixed media",
        ],
        genre: [
            "portrait",
            "character sheet",
            "environment",
            "fashion illustration",
            "editorial",
            "street style",
            "runway",
            "fantasy adventure",
            "sci-fi adventure",
            "space marine",
            "mecha",
            "kaiju",
            "post-apocalyptic",
            "urban fantasy",
            "mythology",
            "surreal",
            "dreamlike",
            "noir",
            "gothic",
            "romantic",
            "pastoral",
            "heroic",
            "epic",
            "slice of life",
            "magical girl",
            "superhero",
            "villain",
            "military",
            "cyborg",
            "android",
            "mech pilot",
            "wizard",
            "witch",
            "alchemist",
            "assassin",
            "rogue",
            "paladin",
            "knight",
            "cleric",
            "archer",
            "ranger",
            "bard",
            "druid",
            "beastmaster",
            "stealth",
            "sports",
            "dance",
            "idol",
            "idol concert",
            "battle",
            "duel",
        ],
        mood: [
            "bright",
            "cheerful",
            "playful",
            "whimsical",
            "romantic",
            "mysterious",
            "dramatic",
            "moody",
            "melancholic",
            "ethereal",
            "serene",
            "tranquil",
            "dreamy",
            "surreal glow",
            "gritty",
            "dark",
            "gothic",
            "grim",
            "ominous",
            "epic lighting",
            "cinematic",
            "high contrast",
            "low key",
            "high key",
            "soft light",
            "rim light",
            "volumetric light",
            "sunset lighting",
            "golden hour",
            "blue hour",
            "moonlit",
            "neon",
            "rainy",
            "foggy",
            "stormy",
            "snowy",
            "dusty",
            "desert heat haze",
        ],
    },
    CB_FullBodyPromptNode: {
        framing: [
            "full body shot",
            "long shot",
            "standing center frame",
            "wide shot",
            "group shot",
            "dynamic angle",
            "three-quarter view",
            "profile view",
            "rear view",
            "360 turntable",
            "establishing shot",
            "hero pose",
            "power pose",
            "leaping",
            "mid-air",
            "running",
            "sprinting",
            "walking",
            "kneeling",
            "sitting",
            "floating",
            "flying",
            "combat stance",
            "spellcasting",
            "summoning circle",
            "parkour",
            "jump kick",
            "landing pose",
        ],
        perspective: [
            "eye level",
            "low angle",
            "worm's-eye view",
            "high angle",
            "bird's-eye view",
            "dutch angle",
            "tilted frame",
            "wide-angle lens",
            "fisheye lens",
            "telephoto lens",
            "close distance",
            "medium distance",
            "far distance",
            "cinematic framing",
        ],
        motion: [
            "motion blur",
            "speed lines",
            "afterimage",
            "dynamic smear",
            "freeze frame",
            "bullet time",
            "time stop",
            "slow motion",
            "action lines",
            "dust kick",
            "debris burst",
            "water splash",
            "energy trail",
            "aura burst",
            "wind swirl",
        ],
        focus: [
            "sharp focus",
            "bokeh background",
            "shallow depth of field",
            "deep focus",
            "subject spotlight",
            "rim-lit silhouette",
            "backlit",
            "soft vignette",
            "glow outline",
            "HDR",
            "high contrast",
            "film grain",
            "cinematic color grade",
        ],
    },
    CB_UpperBodyPromptNode: {
        pose: [
            "bust shot",
            "half body",
            "torso up",
            "waist up",
            "arms crossed",
            "hands on hips",
            "hands clasped",
            "leaning forward",
            "leaning back",
            "arms behind back",
            "one hand raised",
            "peace sign",
            "pointing",
            "hand on cheek",
            "chin resting on hand",
            "phone holding",
            "book holding",
            "coffee cup",
            "microphone",
            "musical instrument",
        ],
        angle: [
            "front view",
            "three-quarter view",
            "side view",
            "over-the-shoulder",
            "looking back",
            "tilted head",
            "upward gaze",
            "downward gaze",
            "close-up",
            "intimate portrait",
        ],
        clothing: [
            "casual jacket",
            "hoodie",
            "cardigan",
            "kimono",
            "hakama",
            "cheongsam",
            "hanbok top",
            "school uniform",
            "sailor uniform",
            "military coat",
            "leather jacket",
            "denim jacket",
            "vest",
            "corset",
            "bustier",
            "turtleneck",
            "button-up shirt",
            "sweater",
            "poncho",
            "capelet",
            "shrug",
            "armor breastplate",
            "mage robe",
            "cleric robes",
            "witch cloak",
        ],
        accessory: [
            "brooch",
            "necklace",
            "choker",
            "amulet",
            "pendant",
            "dog tags",
            "tie",
            "bow tie",
            "ascot",
            "scarf",
            "shawl",
            "bandolier",
            "sash",
            "pauldrons",
            "shoulder guard",
            "armlet",
            "bracers",
            "arm warmers",
            "fingerless gloves",
            "gauntlets",
            "armored vambrace",
        ],
    },
    CB_LowerBodyPromptNode: {
        legwear: [
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
        ],
        stance: [
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
        ],
        detail: [
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
        ],
        anchor: [
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
        ],
    },
    CB_LegPromptNode: {
        legwear: [
            "None",
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
        ],
        pose: [
            "None",
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
        ],
        detail: [
            "None",
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
        ],
        anchor: [
            "None",
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
        ],
    },
    CB_ArmPromptNode: {
        armwear: [
            "None",
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
        ],
        pose: [
            "None",
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
        ],
        accessory: [
            "None",
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
        ],
    },
    CB_HandPromptNode: {
        gloves: [
            "None",
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
        ],
        held_item: [
            "None",
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
        ],
        gesture: [
            "None",
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
        ],
    },
    CB_FootPromptNode: {
        footwear: [
            "None",
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
        ],
        sole: [
            "None",
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
        ],
        decoration: [
            "None",
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
        ],
        weathering: [
            "None",
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
        ],
    },
    CB_FacePromptNode: {
        expression: [
            "neutral expression",
            "gentle smile",
            "big smile",
            "laughing",
            "serious",
            "stoic",
            "focused",
            "determined",
            "angry",
            "pouting",
            "sad",
            "teary-eyed",
            "crying",
            "surprised",
            "shocked",
            "embarrassed",
            "blushing",
            "winking",
            "sleepy",
            "yawning",
            "smirking",
            "mischievous",
            "sly",
            "flustered",
            "dreamy gaze",
            "confident grin",
        ],
        eyes: [
            "large eyes",
            "narrow eyes",
            "almond eyes",
            "round eyes",
            "heterochromia",
            "glowing eyes",
            "mechanical eyes",
            "cyber eyes",
            "cat eyes",
            "dragon eyes",
            "fox eyes",
            "reptile eyes",
            "pupil-less",
            "star pupils",
            "heart pupils",
            "cross pupils",
            "ringed iris",
            "multicolor iris",
            "eyeliner",
            "bold eyeliner",
            "smokey eyes",
            "eyeshadow",
            "sparkling eyes",
            "tear mole",
        ],
        hair: [
            "short hair",
            "bob cut",
            "long hair",
            "twintails",
            "ponytail",
            "side ponytail",
            "braids",
            "single braid",
            "french braid",
            "crown braid",
            "bun",
            "twin buns",
            "curly hair",
            "wavy hair",
            "straight hair",
            "messy hair",
            "spiky hair",
            "afro",
            "dreadlocks",
            "side shave",
            "undercut",
            "mohawk",
            "bangs",
            "side bangs",
            "ahoge",
            "antenna hair",
            "ombre hair",
            "gradient hair",
            "highlighted hair",
            "streaked hair",
            "glowing hair",
        ],
        adornment: [
            "freckles",
            "beauty mark",
            "scar",
            "face paint",
            "warpaint",
            "tribal paint",
            "tattoos",
            "cyber tattoos",
            "glowing tattoos",
            "runic markings",
            "stickers",
            "bandages",
            "eyepatch",
            "monocle",
            "glasses",
            "sunglasses",
            "visor",
            "mask",
            "respirator",
            "rebreather",
            "ear cuffs",
            "ear piercings",
            "lip piercing",
            "nose ring",
        ],
    },
    CB_SubItemPromptNode: {
        cloak: [
            "tattered cape",
            "hooded cloak",
            "travel cloak",
            "feathered cape",
            "fur mantle",
            "wolf pelt",
            "dragon scale cape",
            "phoenix feather cloak",
            "shadow cloak",
            "mist cloak",
            "glowing rune cloak",
            "transparent veil cloak",
            "royal mantle",
            "ceremonial cape",
        ],
        weapon: [
            "longsword",
            "greatsword",
            "rapier",
            "katana",
            "tachi",
            "nodachi",
            "spear",
            "halberd",
            "glaive",
            "lance",
            "trident",
            "warhammer",
            "mace",
            "flail",
            "morning star",
            "battle axe",
            "double axe",
            "scythe",
            "dagger",
            "twin daggers",
            "throwing knives",
            "chakram",
            "bow",
            "longbow",
            "recurve bow",
            "crossbow",
            "gunblade",
            "revolver",
            "pistol",
            "rifle",
            "shotgun",
            "energy rifle",
            "railgun",
            "laser pistol",
            "magic staff",
            "wizard staff",
            "scepter",
            "orb staff",
            "spellbook",
            "grimoire",
            "summoning tome",
            "wand",
        ],
        gadget: [
            "grappling hook",
            "smoke bomb",
            "flash bomb",
            "utility drones",
            "shoulder drone",
            "floating drone",
            "hologram projector",
            "wrist computer",
            "holo gauntlet",
            "wrist blades",
            "energy shield",
            "portable shield",
            "magical talisman",
            "soul gem",
            "mana crystal",
            "artifact amulet",
            "ancient relic",
            "arcane focus",
            "pocket watch",
            "compass",
            "lantern",
        ],
        ornament: [
            "runed charm",
            "beads",
            "totem",
            "talisman",
            "dragon fang",
            "demon horn",
            "angel feather",
            "phoenix feather",
            "mystic bell",
            "floating rings",
            "levitating crystals",
            "geometric halo",
            "scroll case",
            "banner",
            "standard",
            "heraldic flag",
            "music instrument prop",
        ],
    },
    CB_FantasyArmorPromptNode: {
        armor_type: [
            "light leather armor",
            "studded leather",
            "scale mail",
            "chainmail",
            "brigandine",
            "plate armor",
            "full plate",
            "samurai armor",
            "oni armor",
            "templar armor",
            "paladin armor",
            "dragon armor",
            "phoenix armor",
            "angelic armor",
            "demonic armor",
            "gothic armor",
            "runic armor",
            "crystal armor",
            "bone armor",
            "living armor",
            "biotech armor",
            "nanotech suit",
            "powered exosuit",
            "mecha frame",
            "stealth suit",
        ],
        motif: [
            "dragon motif",
            "phoenix motif",
            "griffin motif",
            "wolf motif",
            "lion motif",
            "serpent motif",
            "skull motif",
            "floral engravings",
            "celtic knots",
            "aztec patterns",
            "mayan glyphs",
            "runic engravings",
            "glowing runes",
            "angelic filigree",
            "demonic spikes",
            "winged pauldrons",
            "crowned helm",
            "horned helm",
            "crest helm",
            "mask helm",
        ],
        material: [
            "polished steel",
            "blued steel",
            "blackened steel",
            "mithril",
            "adamantite",
            "orichalcum",
            "obsidian",
            "crystal",
            "prismatic crystal",
            "enchanted wood",
            "dragonbone",
            "ivory",
            "bronze",
            "brass",
            "copper",
            "gold",
            "rose gold",
            "silver",
            "platinum",
            "meteorite metal",
            "aether alloy",
            "mana-infused metal",
            "void metal",
            "liquid metal",
            "glass armor",
        ],
        embellishment: [
            "fur trim",
            "feather trim",
            "silk lining",
            "cloak clasp",
            "banner sash",
            "tabard",
            "surcoat",
            "heraldry",
            "etched plates",
            "riveted plates",
            "spiked armor",
            "plated skirt",
            "chain skirt",
            "tasset plates",
            "cuirass engravings",
            "pauldron wings",
            "glowing seams",
            "arcane circuits",
            "floating shards",
            "energy shield emitters",
            "halo crest",
            "tailored fit",
        ],
    },

};

const CONNECTOR_MAP = {
    CB_LegPromptNode: { legwear: "on legs" },
    CB_ArmPromptNode: { armwear: "on arms" },
    CB_HandPromptNode: { gloves: "on hands", held_item: "in hand" },
    CB_FootPromptNode: { footwear: "on foot" },
};

function isCarouselEnabled() {
    const stored = localStorage.getItem(CB_SETTING_ID);
    return stored === null ? CB_SETTING_DEFAULT : stored === "true";
}

function setCarouselEnabled(value) {
    localStorage.setItem(CB_SETTING_ID, value ? "true" : "false");
}

function registerCarouselSetting() {
    if (window[CB_SETTING_GUARD]) return;
    const settings = app?.ui?.settings;
    const enabled = isCarouselEnabled();
    setCarouselEnabled(enabled);
    if (settings?.addSetting) {
        settings.addSetting({
            id: CB_SETTING_ID,
            name: "Enable CB Prompt Carousel UI",
            type: "boolean",
            defaultValue: enabled,
            tooltip: "Toggle custom carousel widgets for CB prompt nodes.",
            onChange: (value) => setCarouselEnabled(Boolean(value)),
        });
        window[CB_SETTING_GUARD] = true;
    }
}

function clampIndex(index, length) {
    return (index + length) % length;
}

function normalizeValue(value) {
    if (value === undefined || value === null) return "";
    const cleaned = String(value).trim();
    if (!cleaned || cleaned.toLowerCase() === NONE_LABEL.toLowerCase()) return "";
    return cleaned;
}

function joinPrompt(parts) {
    return parts.filter(Boolean).join(", ");
}

function withConnector(value, connector) {
    const normalized = normalizeValue(value);
    if (!normalized) return "";
    const cleanedConnector = (connector || "").trim();
    return cleanedConnector ? `${normalized} ${cleanedConnector}` : normalized;
}

function composePrompt(node, optionMap) {
    if (!optionMap) return "";
    const widgetMap = Object.fromEntries((node.widgets || []).map((w) => [w.name, w]));
    const connectors = CONNECTOR_MAP[node.comfyClass] || {};
    const parts = [];

    const manual = normalizeValue(widgetMap.manual_input?.value ?? "");
    if (manual) parts.push(manual);

    Object.keys(optionMap).forEach((name) => {
        const widgetVal = widgetMap[name]?.value ?? "";
        const connected = connectors[name]
            ? withConnector(widgetVal, connectors[name])
            : normalizeValue(widgetVal);
        if (connected) parts.push(connected);
    });

    return joinPrompt(parts);
}

function ensureWidgetValues(node) {
    if (!node.widgets_values) {
        node.widgets_values = (node.widgets || []).map((w) => w.value);
    }
}

function setWidgetValue(node, widget, value) {
    widget.value = value;
    ensureWidgetValues(node);
    const widgetIndex = node.widgets.indexOf(widget);
    if (widgetIndex !== -1) {
        node.widgets_values[widgetIndex] = value;
    }
}

function getWidgetByName(node, name) {
    return (node.widgets || []).find((w) => w.name === name);
}

function wrapLines(ctx, text, maxWidth) {
    const words = (text || "").split(/\s+/);
    const lines = [];
    let current = "";
    words.forEach((word) => {
        const candidate = current ? `${current} ${word}` : word;
        if (current && ctx.measureText(candidate).width > maxWidth) {
            lines.push(current);
            current = word;
        } else {
            current = candidate;
        }
    });
    if (current) lines.push(current);
    return lines.length ? lines : [""];
}

function ensurePreviewWidget(node) {
    let widget = getWidgetByName(node, PREVIEW_WIDGET_NAME);
    if (widget) return widget;

    widget = {
        name: PREVIEW_WIDGET_NAME,
        type: "cb-prompt-preview",
        value: "",
        last_height: 70,
        serializeValue: () => widget.value,
        computeSize: () => [node.size[0], widget.last_height || 70],
    };

    widget.draw = function (ctx, node, width, y) {
        const padding = 8;
        const labelHeight = 16;
        const textHeight = 16;
        ctx.save();
        ctx.textBaseline = "top";
        ctx.textAlign = "left";

        const bgHeight = widget.last_height || 70;
        ctx.fillStyle = "#1b1b1b";
        ctx.fillRect(0, y, width, bgHeight);
        ctx.strokeStyle = "#444";
        ctx.strokeRect(0, y, width, bgHeight);

        ctx.fillStyle = "#9ac7ff";
        ctx.font = "bold 14px sans-serif";
        ctx.fillText("Prompt Preview", padding, y + padding);

        const text = widget.value || "(No prompt selected)";
        ctx.font = "13px sans-serif";
        const lines = wrapLines(ctx, text, width - padding * 2);
        const contentStart = y + padding + labelHeight;
        lines.forEach((line, idx) => {
            ctx.fillStyle = "#ddd";
            ctx.fillText(line, padding, contentStart + idx * textHeight);
        });

        const requiredHeight = padding + labelHeight + lines.length * textHeight + padding;
        widget.last_height = Math.max(requiredHeight, 56);
        ctx.restore();
    };

    if (!node.widgets) node.widgets = [];
    node.widgets.push(widget);
    ensureWidgetValues(node);
    return widget;
}

function refreshPromptPreview(node) {
    const optionMap = NODE_OPTION_MAP[node.comfyClass];
    if (!optionMap) return;
    const preview = ensurePreviewWidget(node);
    const prompt = composePrompt(node, optionMap);
    const estimatedLines = Math.max(1, Math.ceil((prompt || "(No prompt selected)").length / 48));
    preview.last_height = Math.max(56, 32 + estimatedLines * 16);
    setWidgetValue(node, preview, prompt);
    node.setDirtyCanvas(true, true);
}

function wrapWidgetCallback(widget, node) {
    if (!widget || widget.__cbPreviewWrapped) return;
    const original = widget.callback;
    widget.callback = function (...args) {
        const result = original ? original.apply(this, args) : undefined;
        setWidgetValue(node, widget, widget.value);
        refreshPromptPreview(node);
        return result;
    };
    widget.__cbPreviewWrapped = true;
}

function bindPreviewCallbacks(node, optionMap) {
    const names = ["manual_input", ...Object.keys(optionMap || {})];
    names.forEach((name) => wrapWidgetCallback(getWidgetByName(node, name), node));
}

function updateWidgetValue(node, widget, value) {
    setWidgetValue(node, widget, value);
    refreshPromptPreview(node);
    node.setDirtyCanvas(true, true);
}

function applyCarousel(widget, node, label) {
    widget.type = "cb-prompt-carousel";
    widget.label = label;
    widget.serializeValue = () => widget.value;
    widget.computeSize = () => [node.size[0], 32];
    widget.last_y = 0;
    widget.last_width = node.size[0];
    widget.last_height = 32;

    widget.draw = function (ctx, node, widgetWidth, y) {
        const height = 28;
        this.last_y = y;
        this.last_width = widgetWidth;
        this.last_height = height;
        const padding = 6;
        const buttonWidth = 20;

        ctx.save();
        ctx.fillStyle = "#333";
        ctx.font = "16px sans-serif";

        ctx.fillStyle = "#ddd";
        ctx.textAlign = "left";
        ctx.fillText(label, padding, y + height / 2 + 5);

        const leftX = widgetWidth - (buttonWidth * 2 + padding * 2 + 60);
        const rightX = widgetWidth - (buttonWidth + padding);
        const centerY = y + height / 2;

        ctx.fillStyle = "#555";
        ctx.fillRect(leftX, y + 6, buttonWidth, height - 12);
        ctx.fillRect(rightX, y + 6, buttonWidth, height - 12);

        ctx.fillStyle = "#fff";
        ctx.textAlign = "center";
        ctx.fillText("<", leftX + buttonWidth / 2, centerY + 5);
        ctx.fillText(">", rightX + buttonWidth / 2, centerY + 5);

        ctx.textAlign = "left";
        const valueX = leftX + buttonWidth + padding;
        ctx.fillStyle = "#ddd";
        ctx.fillText(widget.value, valueX, centerY + 5);

        ctx.restore();
    };

    widget.mouse = function (event, pos) {
        if (event.type !== LiteGraph.pointerevents_down) return;
        const [x, y] = pos;
        const height = this.last_height;
        const padding = 6;
        const buttonWidth = 20;
        const leftX = this.last_width - (buttonWidth * 2 + padding * 2 + 60);
        const rightX = this.last_width - (buttonWidth + padding);

        if (y < this.last_y || y > this.last_y + height) return;

        const options = widget.options ?? [];
        if (!options.length) return;
        const currentIndex = options.indexOf(widget.value);
        if (x >= leftX && x <= leftX + buttonWidth) {
            const next = clampIndex(currentIndex - 1, options.length);
            updateWidgetValue(node, widget, options[next]);
            return true;
        }
        if (x >= rightX && x <= rightX + buttonWidth) {
            const next = clampIndex(currentIndex + 1, options.length);
            updateWidgetValue(node, widget, options[next]);
            return true;
        }
    };
}

function setupCarouselWidgets(node, optionMap) {
    const widgets = node.widgets || [];
    const knownValues = node.widgets_values || [];

    Object.entries(optionMap).forEach(([name, options]) => {
        const widget = widgets.find((w) => w.name === name);
        if (!widget) return;
        if (widget.value === undefined || !options.includes(widget.value)) {
            const savedIndex = widgets.indexOf(widget);
            const savedValue = knownValues[savedIndex];
            widget.value = options.includes(savedValue) ? savedValue : options[0];
        }
        widget.options = options;
        applyCarousel(widget, node, name.charAt(0).toUpperCase() + name.slice(1));
    });
}

app.registerExtension({
    name: "custom.cb.additional_prompts.carousel",
    nodeCreated(node) {
        registerCarouselSetting();
        const optionMap = NODE_OPTION_MAP[node.comfyClass];
        if (!optionMap) return;

        ensureWidgetValues(node);
        ensurePreviewWidget(node);
        bindPreviewCallbacks(node, optionMap);

        if (isCarouselEnabled()) {
            setupCarouselWidgets(node, optionMap);
        }

        refreshPromptPreview(node);
    },
});


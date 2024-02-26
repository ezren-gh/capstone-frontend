import sys

from pathlib import Path  
from urllib.parse import urljoin

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# API URL
API_URL = "http://35.82.152.47/"

# MODELS API CONFIG
GLIPV2_URL = urljoin(API_URL, '/detection/base')
DESCO_GLIP_URL = urljoin(API_URL, '/detection/glip')
DESCO_FIBER_URL = urljoin(API_URL, '/detection/fiber')

# MODELS ENUM
GLIPV2 = 0
DESCO_GLIP = 1
DESCO_FIBER = 2

# IMAGES CONFIG
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'default_image.webp'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'default_image.webp'

EXAMPLE_IMAGE_2 = IMAGES_DIR / 'ex_2.jpg'
EXAMPLE_IMAGE_3 = IMAGES_DIR / 'ex_1.jpg'
EXAMPLE_IMAGE_4 = IMAGES_DIR / 'ex_3.jpg'

# EXAMPLE VALUES
EXAMPLE_CONFIG = {
    "GLIPv2": {
        "Example 1": {
            "image_path": EXAMPLE_IMAGE_2,
            "text": "airplane flying above a military truck"
        },
        "Example 2": {
            "image_path": EXAMPLE_IMAGE_2,
            "text": "airplane . truck . person . booth . light pole ."
        },
        "Example 3": {
            "image_path": EXAMPLE_IMAGE_3,
            "text": "boy doing a flip on a skateboard"
        },
        "Example 4": {
            "image_path": EXAMPLE_IMAGE_4,
            "text": "man . frisbee . child . statue ."
        },
    },
    "DesCo-GLIP": {
        "Example 1": {
            "image_path": EXAMPLE_IMAGE_2,
            "text": "airplane flying above a military truck",
            "ground_tokens": "airplane"
        },
        "Example 2": {
            "image_path": EXAMPLE_IMAGE_3,
            "text": "boy doing a flip on a skateboard",
            "ground_tokens": "skateboard"
        },
        "Example 3": {
            "image_path": EXAMPLE_IMAGE_4,
            "text": "man throwing a frisbee in front of a child",
            "ground_tokens": "frisbee"
        },
        "Example 4": {
            "image_path": EXAMPLE_IMAGE_4,
            "text": "man throwing a frisbee next to a statue in front of a child",
            "ground_tokens": "man;frisbee;child;statue"
        }
    },
    "DesCo-FIBER" : {
        "Example 1": {
            "image_path": EXAMPLE_IMAGE_2,
            "text": "airplane flying above a military truck",
            "ground_tokens": "airplane"
        },
        "Example 2": {
            "image_path": EXAMPLE_IMAGE_3,
            "text": "boy doing a flip on a skateboard",
            "ground_tokens": "skateboard"
        },
        "Example 3": {
            "image_path": EXAMPLE_IMAGE_4,
            "text": "man throwing a frisbee in front of a child",
            "ground_tokens": "frisbee"
        },
        "Example 4": {
            "image_path": EXAMPLE_IMAGE_4,
            "text": "man throwing a frisbee next to a statue in front of a child",
            "ground_tokens": "man;frisbee;child;statue"
        }
    }
}

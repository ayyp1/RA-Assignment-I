import os

# Path configurations
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data/3702_left_knee.nii.gz")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

# Segmentation parameters
SEGMENTATION = {
    "femur_tibia": {
        "lower_hu": 390,
        "upper_hu": 5000,
        "closing_iterations": 2
    },
    "tibia": {
        "lower_hu": 420,
        "upper_hu": 5000,
        "closing_iterations": 3
    }
}

# Expansion parameters
EXPANSION_MM = 2
MAX_EXPANSION_MM = 4

# Randomization
RANDOM_SEEDS = [42, 123]
import os
from config import *
from segmentation.femur_tibia import segment_femur_tibia
from segmentation.tibia import segment_tibia
from processing.expansion import expand_mask
from processing.randomization import randomize_mask
from analysis.landmarks import detect_landmarks, save_landmarks
from utils.io import load_nifti, save_nifti

def main():
    # Create output directory
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Task 1.1 - Femur & Tibia segmentation
    femur_tibia_path = os.path.join(RESULTS_DIR, "femur_tibia.nii.gz")
    segment_femur_tibia(DATA_PATH, femur_tibia_path, SEGMENTATION["femur_tibia"])

    # Task 1.4 - Tibia-specific segmentation
    tibia_path = os.path.join(RESULTS_DIR, "tibia.nii.gz")
    segment_tibia(DATA_PATH, tibia_path, SEGMENTATION["tibia"])

    # Task 1.2 - Mask expansions
    expanded_paths = []
    for mm in [2, 4]:
        path = os.path.join(RESULTS_DIR, f"tibia_{mm}mm.nii.gz")
        expand_mask(tibia_path, path, mm)
        expanded_paths.append(path)

    # Task 1.3 - Randomized masks
    randomized_paths = []
    for i, seed in enumerate(RANDOM_SEEDS):
        path = os.path.join(RESULTS_DIR, f"tibia_rand{i+1}.nii.gz")
        randomize_mask(tibia_path, expanded_paths[0], path, EXPANSION_MM, seed)
        randomized_paths.append(path)

    # Task 1.4 - Landmark detection
    all_masks = {
        "Original": tibia_path,
        "2mm_expanded": expanded_paths[0],
        "4mm_expanded": expanded_paths[1],
        "Randomized1": randomized_paths[0],
        "Randomized2": randomized_paths[1]
    }
    
    landmarks = {name: detect_landmarks(path) for name, path in all_masks.items()}
    save_landmarks(landmarks, os.path.join(RESULTS_DIR, "landmarks.txt"))

if __name__ == "__main__":
    main()
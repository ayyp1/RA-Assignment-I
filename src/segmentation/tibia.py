import numpy as np
from scipy.ndimage import label, binary_closing, binary_fill_holes, generate_binary_structure
from ..utils.io import load_nifti, save_nifti

def segment_tibia(input_path: str, output_path: str, config: dict):
    """Tibia-specific segmentation with spatial prioritization"""
    data, affine, _ = load_nifti(input_path)
    
    # Thresholding
    bone_mask = np.logical_and(
        data >= config["lower_hu"],
        data <= config["upper_hu"]
    )
    
    # Aggressive 2D Closing
    struct_2d = generate_binary_structure(2, 1)
    closed_mask = np.zeros_like(bone_mask)
    for z in range(bone_mask.shape[2]):
        closed_mask[:, :, z] = binary_closing(
            bone_mask[:, :, z],
            structure=struct_2d,
            iterations=config["closing_iterations"]
        )
    
    # 3D Component analysis with spatial features
    labeled_mask, _ = label(closed_mask)
    component_sizes = np.bincount(labeled_mask.ravel())
    component_sizes[0] = 0
    
    candidates = []
    for label_id in range(1, len(component_sizes)):
        if component_sizes[label_id] > 0:
            z_coords = np.where(labeled_mask == label_id)[2]
            candidates.append({
                "label": label_id,
                "size": component_sizes[label_id],
                "max_z": np.max(z_coords)
            })
    
    # Select tibia (largest component in lower slices)
    candidates.sort(key=lambda x: (-x["size"], -x["max_z"]))
    tibia_label = candidates[0]["label"]
    
    # Post-processing
    struct_3d = generate_binary_structure(3, 2)
    tibia_mask = labeled_mask == tibia_label
    tibia_mask = binary_closing(tibia_mask, struct_3d, iterations=2)
    tibia_mask = binary_fill_holes(tibia_mask)
    
    save_nifti(tibia_mask.astype(np.uint8), affine, output_path)
import numpy as np
from scipy.ndimage import label, binary_closing, binary_fill_holes, generate_binary_structure
from ..utils.io import load_nifti, save_nifti

def segment_femur_tibia(input_path: str, output_path: str, config: dict):
    """Segment both bones using thresholding and morphological operations"""
    data, affine, _ = load_nifti(input_path)
    
    # Thresholding
    bone_mask = np.logical_and(
        data >= config["lower_hu"],
        data <= config["upper_hu"]
    )
    
    # 2D Closing per slice
    struct_2d = generate_binary_structure(2, 1)
    closed_mask = np.zeros_like(bone_mask)
    for z in range(bone_mask.shape[2]):
        closed_mask[:, :, z] = binary_closing(
            bone_mask[:, :, z],
            structure=struct_2d,
            iterations=config["closing_iterations"]
        )
    
    # 3D Component analysis
    labeled_mask, _ = label(closed_mask)
    component_sizes = np.bincount(labeled_mask.ravel())
    component_sizes[0] = 0  # Ignore background
    
    # Select top 2 components
    top_labels = np.argsort(component_sizes)[-2:]
    
    # Post-processing
    struct_3d = generate_binary_structure(3, 2)
    final_mask = np.zeros_like(closed_mask, dtype=np.uint8)
    
    for idx, label_id in enumerate(top_labels, 1):
        mask = labeled_mask == label_id
        closed = binary_closing(mask, struct_3d, iterations=3)
        filled = binary_fill_holes(closed)
        
        # Keep largest component
        labeled, num_features = label(filled)
        if num_features > 1:
            largest = np.argmax(np.bincount(labeled.ravel())[1:]) + 1
            filled = labeled == largest
        
        final_mask[filled] = idx
    
    save_nifti(final_mask, affine, output_path)
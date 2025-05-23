import numpy as np
from scipy.ndimage import distance_transform_edt
from ..utils.io import load_nifti, save_nifti

def randomize_mask(original_path: str, expanded_path: str, output_path: str, max_mm: float, seed: int = None):
    """Generate randomized contour between original and expanded"""
    orig_data, affine, zooms = load_nifti(original_path)
    exp_data, _, _ = load_nifti(expanded_path)
    
    np.random.seed(seed)
    r = np.random.uniform(0, max_mm)
    
    # Calculate valid expansion region
    distance = distance_transform_edt(exp_data & ~orig_data, sampling=zooms)
    randomized = orig_data | ((distance > 0) & (distance <= r))
    
    save_nifti(randomized.astype(np.uint8), affine, output_path)
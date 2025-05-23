import numpy as np
from scipy.ndimage import distance_transform_edt
from ..utils.io import load_nifti, save_nifti

def expand_mask(input_path: str, output_path: str, expansion_mm: float):
    """Physically accurate mask expansion"""
    data, affine, zooms = load_nifti(input_path)
    
    # Calculate distance transform
    distance = distance_transform_edt(~data.astype(bool), sampling=zooms)
    expanded = data | (distance <= expansion_mm)
    
    save_nifti(expanded.astype(np.uint8), affine, output_path)
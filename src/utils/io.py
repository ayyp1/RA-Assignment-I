import nibabel as nib
import numpy as np
import os

def load_nifti(path: str):
    """Load NIfTI file with validation"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File {path} not found")
    img = nib.load(path)
    return img.get_fdata(), img.affine, img.header.get_zooms()[:3]

def save_nifti(data: np.ndarray, affine: np.ndarray, path: str):
    """Save NIfTI file with directory creation"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img = nib.Nifti1Image(data.astype(np.uint8), affine)
    nib.save(img, path)
import nibabel as nib
import numpy as np

def detect_landmarks(mask_path: str):
    """Find medial/lateral lowest points in world coordinates"""
    img = nib.load(mask_path)
    data = img.get_fdata()
    affine = img.affine
    
    # Find most inferior slice
    z_coords = np.where(data)[2]
    if len(z_coords) == 0:
        return (None, None)
    lowest_z = np.min(z_coords)
    
    # Find extremes in axial plane
    y, x = np.where(data[:, :, lowest_z])
    if len(x) == 0:
        return (None, None)
    
    # Convert voxel to world coordinates
    medial_voxel = [x.min(), y[np.argmin(x)], lowest_z]
    lateral_voxel = [x.max(), y[np.argmax(x)], lowest_z]
    
    medial_world = nib.affines.apply_affine(affine, medial_voxel).round(2)
    lateral_world = nib.affines.apply_affine(affine, lateral_voxel).round(2)
    
    return medial_world, lateral_world

def save_landmarks(landmarks: dict, output_path: str):
    """Save coordinates to text file"""
    with open(output_path, 'w') as f:
        for name, (medial, lateral) in landmarks.items():
            f.write(f"## {name} ##\n")
            f.write(f"Medial: [{medial[0]:.2f}, {medial[1]:.2f}, {medial[2]:.2f}]\n")
            f.write(f"Lateral: [{lateral[0]:.2f}, {lateral[1]:.2f}, {lateral[2]:.2f}]\n\n")
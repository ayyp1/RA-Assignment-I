``` bash
RA-Assignment-I/
├── data/                               # Input datasets for all tasks
├── results/                            # Output files generated from tasks
│   ├── femur_tibia_segmentation.nii.gz # Task 1.1: Femur and tibia segmentation
│   ├── expanded_2mm.nii.gz            # Task 1.2: Expanded segmentation (2mm margin)
│   ├── randomized_mask.nii.gz         # Task 1.3: Randomized mask output
│   ├── landmark_coordinates.txt       # Task 1.4: Landmark coordinates
│   ├── tibia_2mm.nii.gz              # Task 1.4: Tibia segmentation (2mm resolution)
│   ├── tibia_4mm.nii.gz              # Task 1.4: Tibia segmentation (4mm resolution)
│   ├── tibia_rand1.nii.gz            # Task 1.4: Tibia with random transform 1
│   ├── tibia_rand2.nii.gz            # Task 1.4: Tibia with random transform 2
│   ├── tibia_segmentation.nii.gz      # Task 1.4: Final tibia segmentation
├── src/                               # Source code for all tasks
├── config.py                          # Configuration file for task parameters
├── Documentation.pdf                  # Methodology and results documentation
├── requirements.txt                   # Python package dependencies
└── README.md                          # Repository overview and instructions
```

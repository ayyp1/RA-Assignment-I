RA-Assignment-I/
├── data/                           # Directory containing input data for the tasks
├── results/                        # Directory containing output files for all tasks
│   ├── femur_tibia_segmentation.nii.gz  # Task 1.1: Segmentation result for femur and tibia
│   ├── expanded_2mm.nii.gz             # Task 1.2: Expanded segmentation with 2mm margin
│   ├── randomized_mask.nii.gz          # Task 1.3: Randomized mask output
│   ├── landmark_coordinates.txt        # Task 1.4: Text file with landmark coordinates
│   ├── tibia_2mm.nii.gz               # Task 1.4: Tibia segmentation at 2mm resolution
│   ├── tibia_4mm.nii.gz               # Task 1.4: Tibia segmentation at 4mm resolution
│   ├── tibia_rand1.nii.gz             # Task 1.4: Tibia segmentation with random transform 1
│   ├── tibia_rand2.nii.gz             # Task 1.4: Tibia segmentation with random transform 2
│   ├── tibia_segmentation.nii.gz       # Task 1.4: Final tibia segmentation output
├── src/                           # Directory containing source code for all tasks
├── config.py                      # Configuration file for task parameters and settings
├── Documentation.pdf              # Detailed documentation of the methodology and results
├── requirements.txt               # List of required Python packages and dependencies
└── README.md                      # Overview of the repository, instructions, and usage

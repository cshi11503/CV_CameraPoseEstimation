# CV_CameraPoseEstimation
Final Project for Computer Vision

# Camera Pose Estimation under View Sparsity

EN.601.661 Computer Vision — Course Project

## Objective

Compare four camera pose estimation methods under
increasing image sparsity:

- COLMAP
- OpenMVG
- VGGT
- DUSt3R

## Dataset

Microsoft 7-Scenes

Initial experiment:
- Scene: chess
- Sequence: seq-01
- Images per run: 20
- Strides: 1, 2, 5, 10, 20

## Project Organization

- `configs/`: Shared experiment parameters
- `data/`: Local datasets (not committed)
- `methods/`: Independent method implementations
- `shared/`: Sampling and evaluation utilities
- `outputs/`: Generated camera poses
- `results/`: Evaluation tables and runtimes

## Required Pose Output

Filename:
`<method>_chess_seq01_s<stride>_n20.txt`

Each row:
`frame_index tx ty tz qx qy qz qw`

Requirements:
- Original dataset frame indices
- Camera-to-world transformations
- Quaternion order: x, y, z, w
- One row per successfully registered frame
- No fabricated poses for failed registrations

## Evaluation

- Sim(3) alignment
- Translation error (cm)
- Rotation error (degrees)
- Pose recovery rate
- Pose success rate (5 cm and 5 degrees)
- Runtime (seconds)

## Collaboration

Each method has its own feature branch.
Submit changes to main using pull requests.

## Status

Project infrastructure under development.
Method implementations and evaluation scripts are pending.

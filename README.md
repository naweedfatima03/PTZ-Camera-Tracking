# PTZ Camera Tracking
This repository provides a compact implementation of camera intrinsics, extrinsics, and pixel-to-pixel projection between two camera views. The mathematical model in the accompanying report and the proof-of-concept notebook demonstrate how camera rotation can be used to track and re-centre a pixel, similar to PTZ camera behaviour.

---

## Overview

The project introduces the foundational ideas behind camera modelling: how intrinsic and extrinsic parameters define the mapping between real-world coordinates and their corresponding pixel locations, and how those mappings change when a camera moves. The Python scripts provide simple helper functions that illustrate these concepts in code, while the notebook implements a functional demonstration of the overall projection approach.

---

## Methodology

The core idea presented in the report is to take a pixel in one image, estimate the 3D ray it lies on using the camera’s intrinsic and extrinsic parameters, rotate this ray according to the new camera orientation, and then project the transformed ray back onto the image plane of the second view. This creates a direct mapping from a pixel in Image 1 to its corresponding location in Image 2, allowing the camera to effectively “track” or re-centre the point through pan/tilt adjustments.

---

## Notebook Demo
You can view the full proof-of-concept notebook here:  
➡️ **[Camera_simulations.ipynb](Camera_simulations.ipynb)**  

---

## Key Components

The project covers:

* the structure and role of **intrinsic parameters**, which describe how a camera converts real-world rays into pixel coordinates
* the definition of **extrinsic parameters**, which describe where the camera is in space and how it is oriented
* the process of **projecting between 3D and 2D**, including estimating a 3D point from a pixel and reprojecting it into another view
* a **pixel-to-pixel transformation workflow**, which applies camera motion to determine where a point from one image would appear in another
* a **proof-of-concept demonstration** that visually explores this behaviour using simulated camera movements

---

## Acknowledgements

This work was developed with guidance and support from the **Computer Vision & Graphics Lab (CVGL) at LUMS**.

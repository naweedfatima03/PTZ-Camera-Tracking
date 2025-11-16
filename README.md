# Camera Projection & PTZ Transformation Toolkit

This repository provides a simple, modular implementation of camera intrinsics, extrinsics, and pixel-to-pixel projection between two camera views. The work is supported by a mathematical model (in the PDF) and a proof-of-concept notebook that demonstrates camera tracking through PTZ-style rotation.

---

## Overview

The Python scripts introduce the **core components of a camera model**—intrinsic parameters, extrinsic parameters, and how these combine to map points from the real world into image coordinates.

The accompanying mathematical report presents a **method for mapping a pixel from Image 1 to Image 2** by lifting it into 3D space between the two views. This allows simulation of **camera rotation to re-centre or track a pixel**, similar to how PTZ cameras operate.

The notebook provides a **proof of concept (POC)** implementation of this idea, showing how the proposed method behaves numerically and visually.

---

## Key Components

### **intrinsic.py**

Defines the intrinsic camera matrix (focal length, pixel scaling, principal point).
Used for converting between metric rays and pixel coordinates.

### **extrinsic.py**

Implements rotation and translation functions and constructs the extrinsic matrix.
Represents the camera’s position and orientation in the world.

### **projection.py**

Applies intrinsic and extrinsic matrices to:

* estimate a 3D point from pixel coordinates
* project world points into an image
* map a pixel from image 1 → image 2 given two camera poses

This script captures the core projection workflow described in the report.

### **Camera_simulations.ipynb**

A proof-of-concept notebook demonstrating:

* the image1 → world → image2 mapping pipeline
* camera rotation for pixel re-centering
* visualisation of projection behaviour under pan/tilt changes

### **PTZ_Camera_Transformations.pdf**

Contains the full mathematical model underlying the pixel transformation method used in the code.

---

## Acknowledgements

This work was developed with guidance and support from the **Computer Vision & Graphics Lab (CVGL) at LUMS**. 

---

If you'd like this even more concise or want a GitHub-formatted version with badges and visuals, I can prepare that too.

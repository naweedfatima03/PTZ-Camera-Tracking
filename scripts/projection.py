# Using the following camera model:
#                                       x' = K_in * K_ex * X
# X: 3D world coordinates of the form [x, y, z, 1] (4x1)
# K_ex: extrinsic parameters of the camera using 3D rotation and translation (3x4)
# K_in: intrinsic parameters of the camera using focal length, resolution and principal point offset (3x3)
# x': estimated 2D pixel coordinates of the form [hx, hy, h] (3x1)

# Estimate the real world coordinates from the first image's pixel coordinates:
#                                    X = (K_ex_1)^-1 * (K_in)^-1 * x

# Using this estimate project the first image's pixel coordinates to the second image's pixel coordinates:
#                              x_2 = K_in * K_ex_2 * (K_ex_2)^-1 * (K_in)^-1 * x_1

from intrinsic import inMat
from extrinsic import exMat
import numpy as np

def project_point(x_pixel_1, K_ex_1_params, K_ex_2_params):
    """
    Projects a pixel coordinate from image 1 into image 2 using the camera model.

    Parameters:
        x_pixel_1: (3x1) pixel coordinates from image 1 → [hx, hy, h]
        K_ex_1_params: (theta_x, theta_y, theta_z, tx, ty, tz) for image 1
        K_ex_2_params: (theta_x, theta_y, theta_z, tx, ty, tz) for image 2

    Returns:
        x_pixel_2: (3x1) projected pixel coordinates in image 2
    """

    # ---- Build intrinsic matrix ----
    K_in = inMat()

    # ---- Build extrinsic matrices ----
    K_ex_1 = exMat(*K_ex_1_params)
    K_ex_2 = exMat(*K_ex_2_params)

    # Convert extrinsics to 3x4 (drop last row)
    K_ex_1 = K_ex_1[:3, :]
    K_ex_2 = K_ex_2[:3, :]

    # ---- Step 1: Compute world point from image 1 ----
    # X = (K_ex_1)^-1 * (K_in)^-1 * x1
    X_world = np.linalg.inv(K_ex_1) @ np.linalg.inv(K_in) @ x_pixel_1

    # ---- Step 2: Project world point into image 2 ----
    # x2 = K_in * K_ex_2 * X_world
    x_pixel_2 = K_in @ (K_ex_2 @ X_world)

    # Normalize homogeneous coordinates
    if x_pixel_2[2] != 0:
        x_pixel_2 = x_pixel_2 / x_pixel_2[2]

    return x_pixel_2

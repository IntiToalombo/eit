
# EITAC: Electrical Impedance Tomography Analysis Code
# Description: This code is an implementation of Electrical Impedance Tomography Analysis Code (EITAC) for medical diagnosis. 
# The code calculates the voltages in each branch of the circuit and reconstructs the image of the breast for healthy and tumor cases. 
# The code also compares the errors between the healthy and tumor cases to help in medical diagnosis. 
# The code uses the conductance matrix and the inverse of the matrix to calculate the voltages in each branch. 
# The code also uses the calculated voltages to create the Z matrix and reconstruct the image of the breast. 
# The code also compares the errors between the healthy and tumor cases to help in medical diagnosis. 
# The code uses the matplotlib library to plot the reconstructed images of the breast for healthy and tumor cases and the error image for medical diagnosis. 
# The code uses the numpy library to perform matrix operations and calculations.
# Author: Leonardo Acho, UPC, Barcelona, Spain
# Date: March 2025

import numpy as np
import matplotlib.pyplot as plt

vs = 5  # supply voltage
s0 = vs / 2 # Unknown point

# Conductance matrix
A = np.array([
    [4,-1,0,0,0,0,-1,-1,0,0,0,0,0,0],
    [-1,4,-1,0,0,0,0,0,-1,0,0,0,0,0],
    [0,-1,4,-1,0,0,0,0,0,-1,0,0,0,0],
    [0,0,-1,4,-1,0,0,0,0,0,-1,0,0,0],
    [0,0,0,-1,4,-1,0,0,0,0,0,-1,0,0],
    [0,0,0,0,-1,4,-1,0,0,0,0,0,-1,0],
    [-1,0,0,0,0,-1,4,0,0,0,0,0,0,-1],
    [-1,0,0,0,0,0,0,4,-1,0,0,0,0,-1],
    [0,-1,0,0,0,0,0,-1,4,-1,0,0,0,0],
    [0,0,-1,0,0,0,0,0,-1,4,-1,0,0,0],
    [0,0,0,-1,0,0,0,0,0,-1,4,-1,0,0],
    [0,0,0,0,-1,0,0,0,0,0,-1,4,-1,0],
    [0,0,0,0,0,-1,0,0,0,0,0,-1,4,-1],
    [0,0,0,0,0,0,-1,-1,0,0,0,0,-1,4]
])

# Inverse of matrix A
Ainv = np.linalg.inv(A)

# Currents in each branch
currents = {
    "Healthy Case": [1.26417, 0.163937, 0.203791, 0.218233, 0.152962, 1.49323],
    "Tumor in Breast Case": [1.26488, 0.164981, 0.205508, 0.220371, 0.154173, 1.48631]
}

def calculate_voltages(case):
    # Create matrix b (column vector)
    b = np.array([[vs] + currents[case] + [s0] * 7]).T
    # Calculate voltages 
    return np.matmul(Ainv, b)

def create_Z_matrix(x):
    return np.array([[x[0][0], x[7][0], s0],
                     [x[1][0], x[8][0], s0],
                     [x[2][0], x[9][0], s0],
                     [x[3][0], x[10][0], s0],
                     [x[4][0], x[11][0], s0],
                     [x[5][0], x[12][0], s0],
                     [x[6][0], x[13][0], s0]])

def plot_reconstructed_image(Z, title):
    rlist = np.arange(0, 4, 1)
    thetalist = np.radians(np.array([0, 51, 102, 153, 204, 255, 300, 360]))
    rmesh, thetamesh = np.meshgrid(rlist, thetalist)
    Z = np.tile(Z, (1, 1)) # Repeat Z to match the dimensions of rmesh and thetamesh 
    fig, ax = plt.subplots(dpi=120, subplot_kw=dict(projection='polar'))
    pc = ax.pcolormesh(thetamesh, rmesh, Z, shading='flat')
    plt.title(title)
    ax.set_yticklabels([])
    fig.colorbar(pc)
    plt.show()

def compare_errors(x1, x2):
    return np.abs(x1 - x2)

# Healthy Case
x1 = calculate_voltages("Healthy Case")
Z1 = create_Z_matrix(x1)
plot_reconstructed_image(Z1, "Healthy Case")

# Tumor in Breast Case
x2 = calculate_voltages("Tumor in Breast Case")
Z2 = create_Z_matrix(x2)
plot_reconstructed_image(Z2, "Tumor in Breast Case")


# Error Comparison (Medical Diagnosis)
errors = compare_errors(x1, x2)
Z3 = create_Z_matrix(errors)
plot_reconstructed_image(Z3, "Image for Medical Diagnosis")

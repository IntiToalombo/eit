# Electrical Impedance Tomography Analysis Code (EITAC)

## Description
This project implements the Electrical Impedance Tomography Analysis Code (EITAC) for medical diagnosis. The code calculates the voltages in each branch of a circuit and reconstructs images of the breast for healthy and tumor cases. It also compares the errors between the healthy and tumor cases to assist in medical diagnosis.

## Features
- Calculation of voltages in each branch of the circuit using a conductance matrix and its inverse.
- Reconstruction of images for healthy and tumor cases.
- Comparison of errors between healthy and tumor cases for medical diagnosis.
- Visualization of reconstructed images using polar plots.

## Requirements
- Python 3.x
- NumPy
- Matplotlib
## Usage
1. Run the [eitac.py](https://github.com/IntiToalombo/eit/blob/main/eit_breast_image_reconstruction/eitac.py) script:
    ```sh
    python eitac.py
    ```
2. The script will display three polar plots:
    - Healthy Case
    - Tumor in Breast Case
    - Image for Medical Diagnosis (Error Comparison)

## Author
Leonardo Acho, UPC, Barcelona, Spain

## Date
March 2025

## License
This project is licensed under the MIT License.

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

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/eitac.git
    ```
2. Navigate to the project directory:
    ```sh
    cd eitac
    ```
3. Install the required Python packages:
    ```sh
    pip install numpy matplotlib
    ```

## Usage
1. Run the [eitac.py](http://_vscodecontentref_/0) script:
    ```sh
    python eitac.py
    ```
2. The script will display three polar plots:
    - Healthy Case
    - Tumor in Breast Case
    - Image for Medical Diagnosis (Error Comparison)

## Code Explanation
### Conductance Matrix
The conductance matrix [A](http://_vscodecontentref_/1) represents the conductances in the circuit. The inverse of this matrix [Ainv](http://_vscodecontentref_/2) is used to calculate the voltages in each branch.

### Currents
The currents in each branch for healthy and tumor cases are defined in the [currents](http://_vscodecontentref_/3) dictionary.

### Functions
- [calculate_voltages(case)](http://_vscodecontentref_/4): Calculates the voltages for the given case (healthy or tumor).
- [create_Z_matrix(x)](http://_vscodecontentref_/5): Creates the [Z](http://_vscodecontentref_/6) matrix for plotting based on the calculated voltages.
- [plot_reconstructed_image(Z, title)](http://_vscodecontentref_/7): Plots the reconstructed image using polar coordinates.
- [compare_errors(x1, x2)](http://_vscodecontentref_/8): Compares the errors between the healthy and tumor cases.

### Main Script
The main script calculates the voltages for healthy and tumor cases, creates the [Z](http://_vscodecontentref_/9) matrices, and plots the reconstructed images. It also compares the errors between the healthy and tumor cases and plots the error image for medical diagnosis.

## Author
Leonardo Acho, UPC, Barcelona, Spain

## Date
March 2025

## License
This project is licensed under the MIT License.

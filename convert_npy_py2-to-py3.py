'''
Convert numpy python2 .npy to python3

Take two arguments as input : input_filename output_filename

Verifies that the arrays are unchanged.

This allows to avoid the following UserWarning:
    UserWarning: Reading `.npy` or `.npz` file required additional header parsing as it was created on Python 2.
    Save the file again to speed up loading and avoid this warning.

Written by Stéphane Gagné, Université Laval, QC, Canada
'''

import numpy as np
import sys

def convert_npy(file_in, file_out):
    orig = np.load(file_in)
    np.save(file_out, orig)
    print("Saved file as : ", file_out)
    new = np.load(file_out)
    print("New array is equal original array : ", np.array_equal(orig, new))

file_in = sys.argv[1]
file_out = sys.argv[2]
convert_npy(file_in, file_out)

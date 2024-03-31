# My miscellaneous utilities

## Convert npy from python2 to python3
Convert numpy python2 .npy to python3
Take two arguments as input : input_filename output_filename
Verifies that the arrays are unchanged.

This allows to avoid the following UserWarning:
    UserWarning: Reading `.npy` or `.npz` file required additional header parsing as it was created on Python 2.
    Save the file again to speed up loading and avoid this warning.

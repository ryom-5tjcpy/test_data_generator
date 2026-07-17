import numpy as np
from scipy.io import FortranFile

def main():
    file_name = "data/4096/keta2/s2_64.float"
    with FortranFile(file_name, 'r') as f:
        # Read the data
        data = f.read_reals(dtype='float32')

    print(np.shape(data))
    print(data)

if __name__ == "__main__":
    main()

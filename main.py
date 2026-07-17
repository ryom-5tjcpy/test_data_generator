import glob
import numpy as np
import pandas as pd
from scipy.io import FortranFile

def main():
    i = np.tile(np.arange(1, 65), 64 * 64)
    j = np.repeat(np.tile(np.arange(1, 65), 64), 64)
    k = np.repeat(np.arange(1, 65), 64 * 64)

    data = np.vstack([i, j, k])

    df = pd.DataFrame(data.T, columns=['i', 'j', 'k'])
    
    file_pattern = "data/4096/keta2/*.float"
    file_list = glob.glob(file_pattern)

    for file_name in file_list:
        with FortranFile(file_name, 'r') as f:
            col_name = file_name.removeprefix("data/4096/keta2/")
            col_name = col_name.removesuffix("_64.float")
            df[col_name] = f.read_reals(dtype='float32')

    df.to_csv("test.csv", index=False)

if __name__ == "__main__":
    main()

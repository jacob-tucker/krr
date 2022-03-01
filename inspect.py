import h5py
# import pandas as pd
# from pandas import HDFStore
filename = "sample/TRAAAAW128F429D538.h5"
filename_2 = "sample/TRAAAMQ128F1460CD3.h5"
# hdf = HDFStore(filename_2)
# print(hdf.info())
# print(hdf.keys())
# print(1)




## H5PY Code ##
with h5py.File(filename, "r") as f:
    print(f"Keys: {f.keys()}")
    a_group_key = list(f.keys())[0]

    data = list(f[a_group_key])
    print(data)


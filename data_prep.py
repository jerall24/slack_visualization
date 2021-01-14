import pandas as pd
import glob
import os

path = os.path.abspath(os.path.dirname(__file__))
list_of_files = glob.glob(path + '/data_files/*.csv') # * means all if need specific format then *.csv
# print(list_of_files)
# for file in list_of_files:
#     print(file, os.path.getctime(file))
latest_file = max(list_of_files, key=os.path.getctime)
# print(latest_file)

data = pd.read_csv(latest_file)

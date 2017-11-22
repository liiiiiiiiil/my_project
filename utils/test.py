import csv

import pandas as pd

a=pd.read_csv('./output.csv')
print a.columns


# for video_file,labels in csv.reader(open("./output.csv")):
    # print video_file

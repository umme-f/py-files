import os
import glob
import pandas as pd

os.chdir('C:\\Users\\Ariake\\Desktop\\all csv\\fin-net')

ext= 'csv'
allfile= [i for i in glob.glob('*.{}'.format(ext))]

combine= pd.concat([pd.read_csv(f, encoding_errors='ignore') for f in allfile])
combine.to_csv('fl-combine.csv', index=False)

# type_column= pd.read_csv("mem-combine.csv")

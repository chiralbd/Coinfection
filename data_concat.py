import os
import pandas as pd
import glob

# Change directory
os.chdir("../data")

# extensions and all files
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# combining datasets
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

# export to csv
combined_csv.to_csv( "MHC-I.csv", index=False, encoding='utf-8-sig')

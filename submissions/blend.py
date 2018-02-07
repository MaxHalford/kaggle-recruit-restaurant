import glob
import os

import pandas as pd


sub_files = list(set(glob.glob('*.csv')) - set(['blend.csv']))

blend = pd.read_csv(os.path.abspath(sub_files[0]))[['id', 'visitors']]

for sub_file in sub_files[1:]:
    blend['visitors'] += pd.read_csv(sub_file)['visitors']

blend['visitors'] /= len(sub_files)

blend.to_csv('blend.csv', index=False)

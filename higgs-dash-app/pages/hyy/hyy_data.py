'''
Decaimiento HYY
extraído de ATLAS Open Data
'''
from utils.hyy_functions import *

# Data Sample A
# Constan
lumi = 0.5 #fb-1
fraction = 0.8
tuple_path = "https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/GamGam/Data/" # web address
samples_list = ['data_A']

start = time.time() # time at start of whole processing
data = get_data_from_files(samples_list, tuple_path) # process all files
elapsed = time.time() - start # time after whole processing
print("Time taken: "+str(round(elapsed,1))+"s") # print total time taken to process every file



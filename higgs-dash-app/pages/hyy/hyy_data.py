'''
Decaimiento HYY
extraído de ATLAS Open Data
'''
from utils.hyy_functions import *
from utils.constants import TIMEOUT
from app import cache
import pandas as pd

# Data Sample A
# Constants
lumi = 0.5 #fb-1
fraction = 0.8
tuple_path = "https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/GamGam/Data/" # web address
samples_list = ['data_A']
 
@cache.memoize(timeout=TIMEOUT)
def hyy_dataframe():
    return pd.read_csv('/Users/lvtrujillot/Github/notebooks-collection-opendata-dashapp/higgs-dash-app/assets/test-samplea.csv')

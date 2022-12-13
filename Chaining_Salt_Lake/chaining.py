'''
This script converts the building functionality data 
to a capital shock table for CGE model.
'''

import pandas as pd
import os

# import the standardized building functionality table provided by the civil engineering team
bldg_fun = pd.read_csv(('standard_format.csv'), index_col=False)

# import the standardized building-to-sector table
bldg_sector = pd.read_csv(('buildings_to_sectors_SLC.csv'), index_col=False)
bldg_sector['sector'] = bldg_sector['sector'].str.upper()

# merge the building functionality table with the building-to-sector table
shock = bldg_sector.merge(bldg_fun, how='right', on='guid', indicator=True)
shock = shock.drop(['guid', '_merge'], axis=1).rename(columns={'building_functionality': 'shock'})

shock.groupby(['sector']).mean().to_csv('sector_shocks.csv')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



wind_dir  = np.random.rand(100)*360
wind_speed = np.random.rand(100)*70
a = np.array([wind_dir, wind_speed])
a.shape

df = pd.DataFrame(a.T, columns=['wind_dir', 'wind_speed'])

bearing_plot(df, dirn='wind_dir', dir_info='Wind from the North', loc_0 = 'N', loc_90='E');

windrose(df, dirn='wind_dir', speed='wind_speed', loc_0 = 'N', loc_90='E')
windrose_cbar();
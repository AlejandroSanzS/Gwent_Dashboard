import re
import os
import numpy as np
import pandas as pd
from math import pi
from bokeh.models import sources
from bokeh.colors import named
from bokeh.transform import factor_cmap,linear_cmap
#from bokeh.palettes import Turbo256 as pallete
from bokeh.palettes import Inferno256,Category20,Viridis256, Turbo256
from bokeh.plotting import figure, output_file, show,output_notebook
from bokeh.io import output_file, show,curdoc
from bokeh.models import CheckboxButtonGroup,Panel, Tabs, Div, Slider, TextInput,TextAreaInput,ColumnDataSource, HoverTool,Select
from bokeh.layouts import column, row
from bokeh.models.widgets import Tabs
from bokeh.palettes import Spectral4,Spectral6,Spectral5
##############################################################################################################
#### LOADING AND DATA TREATMENT ######



#os.chdir(r'C:/Users/alexs/Desktop/Alejandro/Universidad/Proyectos/Gwent_Dashboard/data')
#print(os.getcwd())
directory = os.getcwd()
print('The directory is', directory)
os.chdir(directory+r'\data')
#os.chdir(directory + r'\data')
dataframe_art = pd.read_excel(r'df_processed.xlsx', sheet_name='dataframe_art')
print(dataframe_art)
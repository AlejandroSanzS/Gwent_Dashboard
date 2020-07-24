import re
import os
import numpy as np
import pandas as pd
from math import pi
from bokeh.models import sources
from bokeh.colors import named
from bokeh.transform import factor_cmap,linear_cmap
from bokeh.palettes import Turbo256 as pallete
from bokeh.palettes import Inferno256,Category20,Viridis256
from bokeh.plotting import figure, output_file, show,output_notebook
from bokeh.io import output_file, show,curdoc
from bokeh.models import CheckboxButtonGroup,Panel, Tabs, Div, Slider, TextInput,TextAreaInput,ColumnDataSource, HoverTool,Select
from bokeh.layouts import column, row
from bokeh.models.widgets import Tabs
from bokeh.palettes import Spectral4,Spectral6,Spectral5
#### LOADING AND DATA TREATMENT ######
os.chdir(r'c:\\Users\\alexs\\Desktop\\Alejandro\\Universidad\\Master_Ciencia_de_datos\\Gwent-TFM\\bokeh_gwent\\data')
df_gwent = pd.read_excel('df_gwent.xlsx')

df_gwent = df_gwent[['ID','Name_x','Available','Power', 'Armor','Provision','ArtistName' ,'Placement', 'Rarity', 'PrimaryCategory_0',
       'PrimaryCategory_1', 'PrimaryCategory_2', 'Categories_0',
       'Categories_1', 'Categories_2','FactionId','SecondaryFactionId', 'Tier', 'Type_y','fluff', 'Tooltip', 'hab0',
       'hab1', 'hab2', 'hab3', 'hab4', 'hab5', 'hab6', 'hab7']]


df_gwent = df_gwent.drop(['PrimaryCategory_1', 'PrimaryCategory_2', 'Categories_2'], axis = 1)
df_gwent = df_gwent.rename(columns = {'Name_x': 'Name','PrimaryCategory_0':'Category_0', 'Categories_0':'Category_1','Categories_1':'Category_2','SecondaryFactionId':'FactionId2','Type_y': 'Type','fluff':'Fluff'})

df_gwent_leaders = df_gwent[df_gwent['Type'] == 'Leader'][['ID','Name','Available','Provision'	,'ArtistName','Rarity','FactionId','Type','Fluff','Tooltip']]
df_gwent_leaders = df_gwent_leaders.astype({'ID':'int','Provision':'int'})

df_gwent_factionInfo = df_gwent[df_gwent.ID.apply(lambda x: len(str(x))==5)]
df_gwent_factionInfo = df_gwent_factionInfo[['ID','Fluff']]



df_gwent =df_gwent[df_gwent.ID.apply(lambda x: len(str(x))==8)] # para quedarme unicamente aquelals cuyo ID sea el asociado a una carta
df_gwent = df_gwent.astype({'ID':'int','Power':'int','Armor':'int','Provision':'int'})
df_gwent['Num'] = 1 
df_cahir = pd.DataFrame({'ID':[162104],'Category_3':['Knigth']})
df_gwent = df_gwent.merge(df_cahir, on = 'ID',how= 'outer')
df_gwent = df_gwent[['ID','Name','Available' ,'Power','Armor','Provision' ,'ArtistName','Placement' ,'Rarity','Category_0','Category_1','Category_2','Category_3','FactionId' ,'FactionId2','Tier','Type' ,'Fluff','Tooltip','hab0','hab1','hab2','hab3','hab4','hab5','hab6','hab7','Num']]
df_gwent = df_gwent[df_gwent['Type']!='Leader']

##############################################################################################################

def seleccion(self,columna,seleccionado):
    data = self[self[columna].isin([seleccionado])]
    return data

def counts(self,atributo):
    
    if atributo =='Abilites':
        data = self.copy()
        lista_habilidades = ['hab0' ,'hab1','hab2','hab3','hab4','hab5', 'hab6', 'hab7' ]
        dataframe_cuentas = []
        for value in lista_habilidades:
            cuentas = pd.DataFrame(data.groupby(value).size()).reset_index().rename(columns = {value:'Abilites',0:'Cuenta'}).fillna(0)
            dataframe_cuentas.append(cuentas)

        union = dataframe_cuentas[0].merge(dataframe_cuentas[1], how = 'outer',on = 'Abilites')
        union = union.merge(dataframe_cuentas[2], how = 'outer',on = 'Abilites')
        union = union.merge(dataframe_cuentas[3], how = 'outer',on = 'Abilites')
        union = union.merge(dataframe_cuentas[4], how = 'outer',on = 'Abilites')
        union = union.merge(dataframe_cuentas[5], how = 'outer',on = 'Abilites')
        union = union.merge(dataframe_cuentas[6], how = 'outer',on = 'Abilites')
        union = union.merge(dataframe_cuentas[7], how = 'outer',on = 'Abilites')
        union =union.fillna(0)
        union['Cuenta'] = union.sum(axis =1)
        union = union[['Abilites','Cuenta']].sort_values(by = ['Cuenta'],ascending = False)
        return union

    elif atributo =='Categories':
        data = self.copy()
        lista_habilidades = ['Category_0','Category_1','Category_2','Category_3']
        dataframe_cuentas = []
        for value in lista_habilidades:
            cuentas = pd.DataFrame(data.groupby(value).size()).reset_index().rename(columns = {value:'Category',0:'Cuenta'}).fillna(0)
            dataframe_cuentas.append(cuentas)

        union = dataframe_cuentas[0].merge(dataframe_cuentas[1], how = 'outer',on = 'Category')
        union = union.merge(dataframe_cuentas[2], how = 'outer',on = 'Category')
        
        union =union.fillna(0)
        union['Cuenta'] = union.sum(axis =1)
        union = union[['Category','Cuenta']].sort_values(by = ['Cuenta'],ascending = False)
        return union


    elif atributo =='Faction':
        data = self.copy()
        faction_list_order = ['Neutral',  
                      'Monsters',
                      'Nilfgaard' ,
                      'Northern Realms',
                      'Scoiatael',
                      'Skellige',
                      'Syndicate']
        lista_habilidades = ['FactionId','FactionId2']
        dataframe_cuentas = []
        for value in lista_habilidades:
            cuentas = pd.DataFrame(data.groupby(value).size()).reset_index().rename(columns = {value:'Faction',0:'Cuenta'}).fillna(0)
            dataframe_cuentas.append(cuentas)

        union = dataframe_cuentas[0].merge(dataframe_cuentas[1], how = 'outer',on = 'Faction')
        union =union.fillna(0)
        union['Cuenta'] = union.sum(axis =1)
        union = union[['Faction','Cuenta']]
        union = union[:-1]
        union['Faction'] = pd.Categorical(union['Faction'], faction_list_order)
        
        return union


    elif atributo =='Artist':
        data = self.copy()
        lista_habilidades = ['ArtistName']
        dataframe_cuentas = []

        for value in lista_habilidades:
            cuentas = pd.DataFrame(data.groupby(value).size()).reset_index().rename(columns = {value:'Artista',0:'Cuenta'}).fillna(0)
            dataframe_cuentas.append(cuentas)
        union = dataframe_cuentas[0]
        union =union.fillna(0)
        union['Cuenta'] = union.sum(axis =1)
        union = union[['Artista','Cuenta']]
        union = union.sort_values(by = ['Cuenta'],ascending = False).reset_index(drop=True)
        return union

    elif atributo =='Type':
        data = self.copy()
        lista_habilidades = ['Type']
        dataframe_cuentas = []
        for value in lista_habilidades:
            cuentas = pd.DataFrame(data.groupby(value).size()).reset_index().rename(columns = {value:'Tipo',0:'Cuenta'}).fillna(0)
            dataframe_cuentas.append(cuentas)

        union = dataframe_cuentas[0]


        union =union.fillna(0)
        union['Cuenta'] = union.sum(axis =1)
        union = union[['Tipo','Cuenta']]
        order_list = ['Unit','Spell','Artifact','Stratagem']
        union['Tipo'] = pd.Categorical(union['Tipo'], order_list)
        union = union.sort_values('Tipo')
        return union
    elif atributo =='Power':
        data = self.copy()
        lista_habilidades = ['Power']
        dataframe_cuentas = []
  
        for value in lista_habilidades:
            cuentas = pd.DataFrame(data.groupby(value).size())
            cuentas = cuentas.reset_index().rename(columns = {value:'Valores_poder',0:'Cuenta'})
            dataframe_cuentas.append(cuentas)
        union = dataframe_cuentas[0]
        union =union.fillna(0)
        union['Power'] = union.sum(axis =1)
        union = union[['Valores_poder','Cuenta']]
        union = union.sort_values(by = ['Valores_poder'],ascending = True).reset_index(drop=True)
        return union


    elif atributo =='Armor':
        data = self.copy()
        lista_habilidades = ['Armor']
        dataframe_cuentas = []

        for value in lista_habilidades:
            cuentas = pd.DataFrame(data.groupby(value).size())
            cuentas = cuentas.reset_index().rename(columns = {value:'Valores_armor',0:'Cuenta'})
            dataframe_cuentas.append(cuentas)
        union = dataframe_cuentas[0]
        union =union.fillna(0)
        union['Armor'] = union.sum(axis =1)
        union = union[['Valores_armor','Cuenta']]
        union = union.sort_values(by = ['Valores_armor'],ascending = True).reset_index(drop=True)
        return union


    elif atributo =='Provision':
        data = self.copy()
        lista_habilidades = ['Provision']
        dataframe_cuentas = []
        for value in lista_habilidades:
            cuentas = pd.DataFrame(data.groupby(value).size())
            cuentas = cuentas.reset_index().rename(columns = {value:'Valores_prov',0:'Cuenta'})
            dataframe_cuentas.append(cuentas)
        union = dataframe_cuentas[0]
        union =union.fillna(0)
        union['Provision'] = union.sum(axis =1)
        union = union[['Valores_prov','Cuenta']]
        union = union.sort_values(by = ['Valores_prov'],ascending = True).reset_index(drop=True)
        return union


dataframe_art = counts(df_gwent,'Artist')
dataframe_tipo = counts(df_gwent,'Type')
dataframe_faction = counts(df_gwent,'Faction')
dataframe_faction = dataframe_faction[:-1]

dataframe_cetegorias = counts(df_gwent,'Categories')[1:][:-1].reset_index(drop=True)
dataframe_abilities = counts(df_gwent,'Abilites').reset_index(drop=True)


faction_list_order = ['Neutral',  
                'Monsters',
                'Nilfgaard' ,
                'Northern Realms',
                'Scoiatael',
                'Skellige',
                'Syndicate']


a=counts(seleccion(df_gwent,'FactionId','Neutral'),'Type').rename(columns = {'Cuenta':'Neutral'})
a = a.rename(columns = {'Cuenta':'Cuenta '+'Neutral'})
b=counts(seleccion(df_gwent,'FactionId','Monsters'),'Type').rename(columns = {'Cuenta':'Monsters'})
c=counts(seleccion(df_gwent,'FactionId','Nilfgaard'),'Type').rename(columns = {'Cuenta':'Nilfgaard'})
d=counts(seleccion(df_gwent,'FactionId','Northern Realms'),'Type').rename(columns = {'Cuenta':'Northern Realms'})
e=counts(seleccion(df_gwent,'FactionId','Scoiatael'),'Type').rename(columns = {'Cuenta':'Scoiatael'})
f=counts(seleccion(df_gwent,'FactionId','Skellige'),'Type').rename(columns = {'Cuenta':'Skellige'})
g=counts(seleccion(df_gwent,'FactionId','Syndicate'),'Type').rename(columns = {'Cuenta':'Syndicate'})
facciones_cuentras = a.merge(b, on='Tipo')
facciones_cuentras = facciones_cuentras.merge(c, on='Tipo')
facciones_cuentras = facciones_cuentras.merge(d, on='Tipo')
facciones_cuentras = facciones_cuentras.merge(e, on='Tipo')
facciones_cuentras = facciones_cuentras.merge(f, on='Tipo')
facciones_cuentras = facciones_cuentras.merge(g, on='Tipo')


a=counts(seleccion(df_gwent,'FactionId','Neutral'),'Power').rename(columns = {'Cuenta':'Neutral'})
b=counts(seleccion(df_gwent,'FactionId','Monsters'),'Power').rename(columns = {'Cuenta':'Monsters'})
c=counts(seleccion(df_gwent,'FactionId','Nilfgaard'),'Power').rename(columns = {'Cuenta':'Nilfgaard'})
d=counts(seleccion(df_gwent,'FactionId','Northern Realms'),'Power').rename(columns = {'Cuenta':'Northern Realms'})
e=counts(seleccion(df_gwent,'FactionId','Scoiatael'),'Power').rename(columns = {'Cuenta':'Scoiatael'})
f=counts(seleccion(df_gwent,'FactionId','Skellige'),'Power').rename(columns = {'Cuenta':'Skellige'})
g=counts(seleccion(df_gwent,'FactionId','Syndicate'),'Power').rename(columns = {'Cuenta':'Syndicate'})
facciones_cp = a.merge(b, on='Valores_poder',how = 'outer')
facciones_cp = facciones_cp.merge(c, on='Valores_poder',how = 'outer')
facciones_cp = facciones_cp.merge(d, on='Valores_poder',how = 'outer')
facciones_cp = facciones_cp.merge(e, on='Valores_poder',how = 'outer')
facciones_cp = facciones_cp.merge(f, on='Valores_poder',how = 'outer')
facciones_cp = facciones_cp.merge(g, on='Valores_poder',how = 'outer')
facciones_cp=facciones_cp.fillna(0).sort_values(['Valores_poder'])


a=counts(seleccion(df_gwent,'FactionId','Neutral'),'Armor').rename(columns = {'Cuenta':'Neutral'})
b=counts(seleccion(df_gwent,'FactionId','Monsters'),'Armor').rename(columns = {'Cuenta':'Monsters'})
c=counts(seleccion(df_gwent,'FactionId','Nilfgaard'),'Armor').rename(columns = {'Cuenta':'Nilfgaard'})
d=counts(seleccion(df_gwent,'FactionId','Northern Realms'),'Armor').rename(columns = {'Cuenta':'Northern Realms'})
e=counts(seleccion(df_gwent,'FactionId','Scoiatael'),'Armor').rename(columns = {'Cuenta':'Scoiatael'})
f=counts(seleccion(df_gwent,'FactionId','Skellige'),'Armor').rename(columns = {'Cuenta':'Skellige'})
g=counts(seleccion(df_gwent,'FactionId','Syndicate'),'Armor').rename(columns = {'Cuenta':'Syndicate'})
facciones_ca = a.merge(b, on='Valores_armor',how = 'outer')
facciones_ca = facciones_ca.merge(c, on='Valores_armor',how = 'outer')
facciones_ca = facciones_ca.merge(d, on='Valores_armor',how = 'outer')
facciones_ca = facciones_ca.merge(e, on='Valores_armor',how = 'outer')
facciones_ca = facciones_ca.merge(f, on='Valores_armor',how = 'outer')
facciones_ca = facciones_ca.merge(g, on='Valores_armor',how = 'outer')
facciones_ca=facciones_ca.fillna(0).sort_values(['Valores_armor'])
facciones_ca = facciones_ca[facciones_ca['Valores_armor']!= 0]

a=counts(seleccion(df_gwent,'FactionId','Neutral'),'Provision').rename(columns = {'Cuenta':'Neutral'})
b=counts(seleccion(df_gwent,'FactionId','Monsters'),'Provision').rename(columns = {'Cuenta':'Monsters'})
c=counts(seleccion(df_gwent,'FactionId','Nilfgaard'),'Provision').rename(columns = {'Cuenta':'Nilfgaard'})
d=counts(seleccion(df_gwent,'FactionId','Northern Realms'),'Provision').rename(columns = {'Cuenta':'Northern Realms'})
e=counts(seleccion(df_gwent,'FactionId','Scoiatael'),'Provision').rename(columns = {'Cuenta':'Scoiatael'})
f=counts(seleccion(df_gwent,'FactionId','Skellige'),'Provision').rename(columns = {'Cuenta':'Skellige'})
g=counts(seleccion(df_gwent,'FactionId','Syndicate'),'Provision').rename(columns = {'Cuenta':'Syndicate'})
facciones_cprov = a.merge(b, on='Valores_prov',how = 'outer')
facciones_cprov = facciones_cprov.merge(c, on='Valores_prov',how = 'outer')
facciones_cprov = facciones_cprov.merge(d, on='Valores_prov',how = 'outer')
facciones_cprov = facciones_cprov.merge(e, on='Valores_prov',how = 'outer')
facciones_cprov = facciones_cprov.merge(f, on='Valores_prov',how = 'outer')

facciones_cprov = facciones_cprov.merge(g, on='Valores_prov',how = 'outer')
facciones_cprov=facciones_cprov.fillna(0).sort_values(['Valores_prov'])


os.chdir(r'C:/Users/alexs/Desktop/Alejandro/Universidad/Master_Ciencia_de_datos/Gwent-TFM/bokeh_gwent/data')
writer = pd.ExcelWriter('df_processed.xlsx', engine='xlsxwriter')
dataframe_art.to_excel(writer, sheet_name='dataframe_art')
dataframe_tipo.to_excel(writer, sheet_name='dataframe_tipo')
dataframe_faction.to_excel(writer, sheet_name='dataframe_faction')
dataframe_cetegorias.to_excel(writer, sheet_name='dataframe_cetegorias')
dataframe_abilities.to_excel(writer, sheet_name='dataframe_abilities')
facciones_cuentras.to_excel(writer, sheet_name='facciones_cuentras')
facciones_cp.to_excel(writer, sheet_name='facciones_cp')
facciones_ca.to_excel(writer, sheet_name='facciones_ca')
facciones_cprov.to_excel(writer, sheet_name='facciones_cprov')

writer.save() #ACTIVAR SI QUEREMOS GUARDAR

os.chdir(r'C:/Users/alexs/Desktop/Alejandro/Universidad/Master_Ciencia_de_datos/Gwent-TFM/bokeh_gwent/data')
writer = pd.ExcelWriter('df_gwent_clean.xlsx', engine='xlsxwriter')
df_gwent.to_excel(writer, sheet_name='df_gwent')
writer.save() #ACTIVAR SI QUEREMOS GUARDAR
##############################################
# For the data of the Abilities - Categories

faction_list_order = ['Neutral',  'Monsters','Nilfgaard' ,'Northern Realms','Scoiatael','Skellige','Syndicate']
tipo=['Unit', 'Spell', 'Artifact', 'Stratagem']

category = []
text = []
ability = []

for values_faction in faction_list_order:
    for values_type in tipo:
   
        category.append(counts(seleccion(seleccion(df_gwent,'FactionId',values_faction),'Type',values_type),'Categories')[1:])
        text.append(values_faction + '_' + values_type)
        ability.append(counts(seleccion(seleccion(df_gwent,'FactionId',values_faction),'Type',values_type),'Abilites'))
        
os.chdir(r'C:/Users/alexs/Desktop/Alejandro/Universidad/Master_Ciencia_de_datos/Gwent-TFM/bokeh_gwent/data')
writer = pd.ExcelWriter('categories.xlsx', engine='xlsxwriter')
for values in range(0,len(text)):
    texto = text[values]
    category[values].to_excel(writer, sheet_name=str(texto))

writer.save() #ACTIVAR SI QUEREMOS GUARDAR
writer = pd.ExcelWriter('abilities.xlsx', engine='xlsxwriter')
for values in range(0,len(text)):
    texto = text[values]
    ability[values].to_excel(writer, sheet_name=str(texto))

writer.save() #ACTIVAR SI QUEREMOS GUARDAR







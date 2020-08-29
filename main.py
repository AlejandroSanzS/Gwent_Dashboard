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
#os.chdir(directory)
os.chdir(directory+r'\Gwent_Dashboard\data')
#os.chdir(r'/data')
#os.chdir(directory+r'\data')
dataframe_art = pd.read_excel('df_processed.xlsx', sheet_name='dataframe_art')
dataframe_tipo= pd.read_excel('df_processed.xlsx', sheet_name='dataframe_tipo')
dataframe_faction= pd.read_excel('df_processed.xlsx', sheet_name='dataframe_faction')
dataframe_cetegorias= pd.read_excel('df_processed.xlsx', sheet_name='dataframe_cetegorias')
dataframe_abilities= pd.read_excel('df_processed.xlsx', sheet_name='dataframe_abilities')
facciones_cuentras= pd.read_excel('df_processed.xlsx', sheet_name='facciones_cuentras')
facciones_cp= pd.read_excel('df_processed.xlsx', sheet_name='facciones_cp')
facciones_ca= pd.read_excel('df_processed.xlsx', sheet_name='facciones_ca')
facciones_cprov= pd.read_excel('df_processed.xlsx', sheet_name='facciones_cprov')


# For the Introduction TAB

div = Div(text="""Hello there, glad you find this tool to know a little bit more about the cards of Gwent: The Witcher Card Game""",
width=200, height=100)

###################################################
def fig_scoiatel():
    p1 = figure(x_range=(0,1), y_range=(0,1),plot_width=250, plot_height=300,title="Scoiatel Faction")
    p1.axis.visible = False
    p1.toolbar.logo = None
    p1.toolbar_location = None
    p1.image_url(url=['http://localhost:5006/Gwent_Dashboard/static/Scoiatel.png'], x=0, y=1, w=1, h=1)
    
    return p1


def fig_neutral():
    p12 = figure(x_range=(0,1), y_range=(0,1),plot_width=250, plot_height=300,title="Neutral Faction")
    p12.axis.visible = False
    p12.toolbar.logo = None
    p12.toolbar_location = None
    p12.image_url(url=['http://localhost:5006/Gwent_Dashboard/static/Neutral.png'], x=0, y=1, w=1, h=1)

    
    return p12

def fig_Monsters():
    p13 = figure(x_range=(0,1), y_range=(0,1),plot_width=250, plot_height=300,title="Monsters Faction")
    p13.axis.visible = False
    p13.toolbar.logo = None
    p13.toolbar_location = None
    p13.image_url(url=['http://localhost:5006/Gwent_Dashboard/static/Monsters.png'], x=0, y=1, w=1, h=1)
    
    return p13
def fig_Nilfgaard():
    p14 = figure(x_range=(0,1), y_range=(0,1),plot_width=250, plot_height=300,title="Nilfgaard Faction")
    p14.axis.visible = False
    p14.toolbar.logo = None
    p14.toolbar_location = None
    p14.image_url(url=['http://localhost:5006/Gwent_Dashboard/static/Nilfgaard.png'], x=0, y=1, w=1, h=1)
    
    return p14
def fig_NR():
    p15 = figure(x_range=(0,1), y_range=(0,1),plot_width=250, plot_height=300,title="Northern Realms Faction")
    p15.axis.visible = False
    p15.toolbar.logo = None
    p15.toolbar_location = None
    p15.image_url(url=['http://localhost:5006/Gwent_Dashboard/static/NR.png'], x=0, y=1, w=1, h=1)
    
    return p15
def fig_Skellige():
    p16 = figure(x_range=(0,1), y_range=(0,1),plot_width=250, plot_height=300,title="Skellige Faction")
    p16.axis.visible = False
    p16.toolbar.logo = None
    p16.toolbar_location = None
    p16.image_url(url=['http://localhost:5006/Gwent_Dashboard/static/Skellige.png'], x=0, y=1, w=1, h=1)
    
    return p16
def fig_Syndicate():
    p17 = figure(x_range=(0,1), y_range=(0,1),plot_width=250, plot_height=300,title="Syndicate Faction")
    p17.axis.visible = False
    p17.toolbar.logo = None
    p17.toolbar_location = None
    p17.image_url(url=['http://localhost:5006/Gwent_Dashboard/static/Syndicate.png'], x=0, y=1, w=1, h=1)
    
    return p17
###################################################
div_Scoiatel = Div(text="Rebels who fight for the rights of non-humans. They'll stop at nothing to achieve their goal, turning the Continent's forests into fields of battle... And cemeteries.",width=200, height=100, margin = (25,0,0,0))
div_Neutral = Div(text="Not all on the Continent choose to follow kings, queens, dukes, and emperors. That isn't to say, however, that they cannot be persuaded by a purse heavy with coin. Everyone has their price, after all.",width=200, height=100, margin = (25,0,0,0))
div_Monsters = Div(text='Legions of hideous monsters, from alghoul to zeugl. All tremble before them, Nordling and Nilfgaardian alike.',width=200, height=100, margin = (25,0,0,0))
div_NR = Div(text="Kingdoms, duchies, marches... The territories of the North are numerous and varied. Yet, they've no time to fight each other, for the might of the Nilfgaardian Empire deserves one's full attention.",width=200, height=100, margin = (25,0,0,0))
div_Syndicate = Div(text='No crime is too hideous for these ruthless cutthroats, who will do anything for the coin.',width=200, height=100, margin = (25,0,0,0))
div_Nilfgaard = Div(text='The powerful Nilfgaardian Empire will not stop until their black and gold banners wave over the entire Continent. If recent years are any indication, they may succeed sooner rather than later.',width=200, height=100, margin = (25,0,0,0))
div_Skellige = Div(text='Fierce warriors who fear neither death nor cold. Yet, they are not without great weaknesses... Mead, song, and a tumbles in the hay.',width=200, height=100, margin = (25,0,0,0))

####################################################################
Howto=Div(text='<p style="font-size:20px"><b>How to play:</b></p>')
TextoHowTo= Div(text="Gwent is a competitive card game based on the lore of the universe of the witcher.<br/>\
     The main goal of the game consist on winning your adversary by having the maximum points on the board by the end of each round and each game has a maximum of 3 rounds,\
     so its necessary to win two rounds in order to win the march.At the beginning of the match each player draws 10 random cards from the deck with is the maximum number of cards a player can have in its hand.\
          At the end of each round 3 cards are drawn if a player has 10 cards the drawn card goes directly to the graveyard.<br/><br/>\
              There is also the ability to redraw some cards that the player does not want to have in its hand, this ability is called a mulligan.\
                  The first round there is 3 mulligans and on the second and third round there is a maximum of 2 mulligans.<br/>When a round starts each player has the possibility\
                       of playing a card on the board and depending of the abilities of each card make additional interactions to affect the game in order to give  advantage in order to win the round.\
                            A round ends when both players have played all orf their cards or both players had passed the turn. The player with the maximum amount of points, win the round.\
                                For this reasons is important to think a strategy based on the cards drawn.<br/><br/>",width=1700, height=100)
Cards_attributes=Div(text='<p style="font-size:20px"><b>Card attributes:</b></p>')
Text_cards = Div(text='<ul>\
  <li>Power : Value of the card in the board</li>\
  <li>Armor: Defensive attribute that protects from direct damage</li>\
  <li>Provision: The cost of having the card in the deck</li>\
  <li>Category: It does not affect gameplay directly is a way to categorice the different types of cards in the factions</li>\
  <li>Abilties: The different effects that  a card can bring into the game.</li>\
</ul>')

Deck_build = Div(text='<p style="font-size:20px"><b>Deck building</b></p>')
Text_decks = Div(text='To play the game is essential to build a deck.</b>\
There are 4 types of cards:\
<ul>\
  <li>Units: The most common type of card, usually have a power value,that is used to count the points each player has.</li>\
  <li>Artifacts: Card with special effects, has no power value.</li>\
  <li>Spells: Cards with special effect that usually synergies with units, does not has power value</li>\
  <li>Stratagem: Another type special card with a limit of 1 per deck.</li>\
</ul></b>The first thing to consider is that there are 6 factions each with its unique cards and abilities.</b>\
 Each deck must contain a Leader from one of the factions available, that plays like and additional card hand has special effects.\
      The balancing system in the game is based on an attribute called provisions.\
           The maximum provision of a deck must be 150 provision from  the cards selected in the deck plus the provisions of the leader.\
                Also there must be a minimum of 13 Units in the deck and a minimum of 25 cards per deck.\
                     Each deck can contain units from its faction and also a faction without leaders called neutral,\
                          that can be used in adition to the main faction of the deck.')

faction_description = Div(text='<p style="font-size:20px"><b>Faction Description:</b></p>')
#####################################################################

tab1 = Panel(child=column(Howto,TextoHowTo,Cards_attributes,Text_cards,Deck_build,Text_decks,faction_description,column(row(fig_neutral(),div_Neutral,fig_Monsters(),div_Monsters,fig_NR(),div_NR,fig_scoiatel(),div_Scoiatel),
row(fig_Syndicate(),div_Syndicate,fig_Nilfgaard(),div_Nilfgaard,fig_Skellige(),div_Skellige))), title="Introduction")

# For the Artista TAB

# Numero de cartas por facciones

# Data selection 


def figura_cartas():

    dataframe_arte = dataframe_art.copy()
    dataframe = dataframe_arte[dataframe_arte['Cuenta']<=Slider.value]
    artistas =list(dataframe['Artista'])
    counts =list(dataframe['Cuenta'])
    source = ColumnDataSource(data=dict(artistas=artistas, counts=counts),)

    TOOLTIPS = [
        ("Tipo", "@artistas"),
        ("Cuenta", "@counts"),
    ]
    color_map = factor_cmap(field_name='artistas',palette=Turbo256, factors=artistas)
    p = figure(plot_width=1880, plot_height=800, title="Number of cards per artist",x_range= artistas,toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)

    p.vbar(x ='artistas', top ='counts',width=1,source=source,color =color_map)

    p.xaxis.axis_label_text_font_size = '15pt'
    p.yaxis.axis_label_text_font_size = '15pt'
    p.xaxis.major_label_orientation = "vertical"
    return p

def update_artistas(attr, old, new):
    layout.children[0] = figura_cartas()
    

Slider = Slider(title="Number of cards", value=124, start=1.0, end=124.0, step=1)
Slider.on_change('value', update_artistas)
controls = column(Slider, width=200)
layout =  row(figura_cartas())
tab2= Panel(child=column(controls,layout), title="Artistas")

# Para las Cartas TAB

dataframe_faction = dataframe_faction
faccion =list(dataframe_faction['Faction'])
counts =list(dataframe_faction['Cuenta'])
source = ColumnDataSource(data=dict(faccion=faccion, counts=counts),)


TOOLTIPS = [
    ("Faction", "@faccion"),
    ("Counts", "@counts"),
]
color_map2 = factor_cmap(field_name='faccion',palette=Spectral6, factors=faccion)
p2 = figure(plot_width=940, plot_height=400, title="Number of cards by Faction",x_range= faccion,toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)
p2.vbar(x ='faccion', top ='counts',width=0.9,source=source,color =color_map2)
p2.yaxis.axis_label = 'Counts'
p2.xaxis.major_label_text_font_size = "15pt"

# Tipos de carta por faccion

dataframe_tipo = dataframe_tipo
tipo =list(dataframe_tipo['Tipo'])
counts =list(dataframe_tipo['Cuenta'])
source = ColumnDataSource(data=dict(tipo=tipo, counts=counts),)
TOOLTIPS = [
    ("Type", "@tipo"),
    ("Counts", "@counts"),
]
color_map2_2 = factor_cmap(field_name='tipo',palette=Spectral6, factors=tipo)
p2_2 = figure(plot_width=940, plot_height=400, title="Types of cards",x_range= tipo,toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)

p2_2.vbar(x ='tipo', top ='counts',width=0.9,source=source,color =color_map2_2)
p2_2.yaxis.axis_label = 'Counts'
p2_2.xaxis.major_label_text_font_size = "15pt"

dataframe_cetegorias = dataframe_cetegorias
cate =list(dataframe_cetegorias['Category'])
counts =list(dataframe_cetegorias['Cuenta'])
source = ColumnDataSource(data=dict(cate=cate, counts=counts),)

TOOLTIPS = [
    ("Category", "@cate"),
    ("Counts", "@counts"),
]

color_map2_22 = factor_cmap(field_name='cate',palette=Inferno256[100:200], factors=cate)
p2_22 = figure(plot_width=940, plot_height=400, title="Number of cards by Category",x_range= cate,toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)

p2_22.vbar(x ='cate', top ='counts',width=0.9,source=source ,color =color_map2_22)
p2_22.yaxis.axis_label = 'Counts'
p2_22.xaxis.major_label_orientation = "vertical"

dataframe_abilities = dataframe_abilities
habil =list(dataframe_abilities['Abilites'])
counts =list(dataframe_abilities['Cuenta'])
source = ColumnDataSource(data=dict(habil=habil, counts=counts),)
TOOLTIPS = [
    ("Abilities", "@habil"),
    ("Counts", "@counts"),
]

color_map2_221 = factor_cmap(field_name='habil',palette=Inferno256[100:200], factors=habil)
p2_221 = figure(plot_width=940, plot_height=400, title="Number of Abilities",x_range= habil,toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)
p2_221.vbar(x ='habil', top ='counts',width=0.9,source=source,color =color_map2_221)
p2_221.yaxis.axis_label = 'Counts'
p2_221.xaxis.major_label_orientation = "vertical"

tab3= Panel(child=column(row(p2,p2_2),row(p2_22,p2_221)), title="Cards")

# Para las Facciones  TAB

opciones = ['Neutral',  
            'Monsters',
            'Nilfgaard' ,
            'Northern Realms',
            'Scoiatael',
            'Skellige',
            'Syndicate']


def figura2():

    dataframe1 = facciones_cuentras
    tipo =list(dataframe1['Tipo'])
    counts =list(dataframe1[y.value].values)
    source = ColumnDataSource(data=dict(tipo=tipo, counts=counts),)

    TOOLTIPS = [
        ("Type", "@tipo"),
        ("Counts", "@counts"),
    ]
    color_map41 = factor_cmap(field_name='tipo',palette=Spectral5, factors=tipo)
    p41 = figure(plot_width=940, plot_height=400, title="Number of cards by type and faction",x_range= tipo,toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)
    p41.vbar(x ='tipo', top ='counts',width=1,source=source,color =color_map41)
    p41.xaxis.axis_label = 'Type'
    p41.yaxis.axis_label = 'Counts'
    p41.xaxis.major_label_text_font_size = "15pt"


    dataframe2 = facciones_cp
    val_power =list(dataframe2['Valores_poder'])
    counts =dataframe2[y.value].values
    source = ColumnDataSource(data=dict(val_power=val_power, counts=counts),)

    TOOLTIPS = [
        ("Power", "@val_power"),
        ("Counts", "@counts"),
    ]
    color_map42 = linear_cmap (field_name='val_power',palette=Category20[20],low = 0, high=20)
    p42 = figure(plot_width=940, plot_height=400, title="Distrubution of cards by Power",toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)
    p42.vbar(x ='val_power', top ='counts',width=1,source=source,color =color_map42)
    p42.xaxis.axis_label = 'Power'
    p42.yaxis.axis_label = 'Counts'
    

    ########################################################################

    dataframe3 = facciones_ca
    Valores_armor =list(dataframe3['Valores_armor'])
    counts =dataframe3[y.value].values
    source = ColumnDataSource(data=dict(Valores_armor=Valores_armor, counts=counts),)

    TOOLTIPS = [
        ("Armor", "@Valores_armor"),
        ("Counts", "@counts"),
    ]
    color_map43 = linear_cmap (field_name='Valores_armor',palette=Category20[20],low = 0, high=20)
    p43 = figure(plot_width=940, plot_height=400, title="Distribution of cards by Armor",toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)
    p43.vbar(x ='Valores_armor', top ='counts',width=1,source=source,color =color_map43)
    p43.xaxis.axis_label = 'Armor'
    p43.yaxis.axis_label = 'Counts'



    dataframe4 = facciones_cprov
    Valores_prov =list(dataframe4['Valores_prov'])
    counts =dataframe4[y.value].values
    source = ColumnDataSource(data=dict(Valores_prov=Valores_prov, counts=counts),)

    TOOLTIPS = [
        ("Provisions", "@Valores_prov"),
        ("Counts", "@counts"),
    ]
    color_map44 = linear_cmap (field_name='Valores_prov',palette=Category20[20],low = 0, high=20)
    p44 = figure(plot_width=940, plot_height=400, title="Distribution of cards by Provision",toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)
    p44.vbar(x ='Valores_prov', top ='counts',width=1,source=source,color =color_map44)
    p44.xaxis.axis_label = 'Provisions'
    p44.yaxis.axis_label = 'Counts'

    return p41,p42,p43,p44

def update2(attr, old, new):
    layout41.children[0] = figura2()[0]
    layout42.children[0] = figura2()[1]
    layout43.children[0] = figura2()[2]
    layout44.children[0] = figura2()[3]
y = Select(title='Faction', value='Neutral', options=opciones)
y.on_change('value', update2)

controls2 = column(y, width=200)

layout_control = column(controls2)
layout41 = row(figura2()[0])
layout42 = row(figura2()[1])
layout43= row(figura2()[2])
layout44= row(figura2()[3])

tab5= Panel(child=column(layout_control,row(layout41,layout44),row(layout42,layout43)), title="Faction")

#################################################################################################################

# PARA CREAR EL TAB DE LA TABLA DE DATOS Y LA DESCARGA
from bokeh.models import (Button, ColumnDataSource, CustomJS, DataTable,
                          NumberFormatter, RangeSlider, TableColumn,)


df_gwent = pd.read_excel('df_gwent_clean.xlsx')
df_gwent = df_gwent.drop(['Unnamed: 0'], axis = 1)
df_gwent_leaders = pd.read_excel('df_gwent_leaders.xlsx')
df_gwent_leaders = df_gwent_leaders.drop(['Unnamed: 0'], axis = 1)
Columns1 = [TableColumn(field=Ci, title=Ci) for Ci in df_gwent.columns] # bokeh columns
data_table1 = DataTable(columns=Columns1, source=ColumnDataSource(df_gwent),width=800,height= 800,fit_columns=False) # bokeh table
button1 = Button(label="Download", button_type="success")


Columns2 = [TableColumn(field=Ci, title=Ci) for Ci in df_gwent_leaders.columns] # bokeh columns
data_table2 = DataTable(columns=Columns2, source=ColumnDataSource(df_gwent_leaders),width=800,height= 800,fit_columns=False) # bokeh table
button2 = Button(label="Download", button_type="success")
javaScript="""
function table_to_csv(source) {
    const columns = Object.keys(source.data)
    const nrows = source.get_length()
    const lines = [columns.join(',')]

    for (let i = 0; i < nrows; i++) {
        let row = [];
        for (let j = 0; j < columns.length; j++) {
            const column = columns[j]
            row.push(source.data[column][i].toString())
        }
        lines.push(row.join(','))
    }
    return lines.join('\\n').concat('\\n')
}


const filename = 'data_result.csv'
filetext = table_to_csv(source)
const blob = new Blob([filetext], { type: 'text/csv;charset=utf-8;' })

//addresses IE
if (navigator.msSaveBlob) {
    navigator.msSaveBlob(blob, filename)
} else {
    const link = document.createElement('a')
    link.href = URL.createObjectURL(blob)
    link.download = filename
    link.target = '_blank'
    link.style.visibility = 'hidden'
    link.dispatchEvent(new MouseEvent('click'))
}
"""

button1.callback = CustomJS(args=dict(source=ColumnDataSource(df_gwent)),code=javaScript)
button2.callback = CustomJS(args=dict(source=ColumnDataSource(df_gwent_leaders)),code=javaScript)
div_cards = Div(text='<p style="font-size:20px"><b>CARDS</b></p>',width=200, height=50)
div_leaders = Div(text='<p style="font-size:20px"><b>LEADERS</b></p>',width=200, height=50)
tab6 = Panel(child=row(column(div_cards,data_table1,button1),column(div_leaders,data_table2,button2)),title='Dataframe')

#PARA EL TAB DE LAS LOOTBOXES

div_keg = Div(text="""This data was obtained from opening 75 Kegs""",
width=200, height=100)

#os.chdir(r'C:/Users/alexs/Desktop/Alejandro/Universidad/Proyectos/Gwent_Dashboard/data')
df_kegs = pd.read_excel('kegs.xlsx',sheet_name = 'BASE').fillna(0)
df_kegs = df_kegs.drop('KEG',axis =1).astype({'RARE':'int64','EPIC':'int64','LEGENDARY':'int64'})

df_lbprov = pd.DataFrame((df_kegs.sum()/375)*100).reset_index(drop= False).rename(columns={'index':'Rarity',0:'Probability'}).round(1)
Columns3 = [TableColumn(field=Ci, title=Ci) for Ci in df_kegs.columns] # bokeh columns
data_table3 = DataTable(columns=Columns3, source=ColumnDataSource(df_kegs),width=350,height= 400,fit_columns=True) # bokeh table
button3 = Button(label="Download", button_type="success")
Columns4 = [TableColumn(field=Ci, title=Ci) for Ci in df_lbprov.columns] # bokeh columns
data_table4 = DataTable(columns=Columns4, source=ColumnDataSource(df_lbprov),width=200,height= 400,fit_columns=True) # bokeh table
button4 = Button(label="Download", button_type="success")
button3.callback = CustomJS(args=dict(source=ColumnDataSource(df_kegs)),code=javaScript)
button4.callback = CustomJS(args=dict(source=ColumnDataSource(df_lbprov)),code=javaScript)
tab7 = Panel(child=column(div_keg,row(column(data_table3,button3),column(data_table4,button4))),title='Dataframes Lootboxes')

##########################################################################

faction_list_order = ['Neutral',  'Monsters','Nilfgaard' ,'Northern Realms','Scoiatael','Skellige','Syndicate']
tipo=['Unit', 'Spell', 'Artifact', 'Stratagem']

def update2_x(attr, old, new):
    layout41_x.children[0] = figura2_x()
    layout41_y.children[0] = figura2_y()

    

y_x = Select(title='Faction', value='Neutral', options=faction_list_order)
y_x.on_change('value', update2_x)
y2_x = Select(title='Type', value='Unit', options=tipo)
y2_x.on_change('value', update2_x)


def figura2_x():
    #os.chdir(r'C:/Users/alexs/Desktop/Alejandro/Universidad/Proyectos/Gwent_Dashboard/data')
    data_x = pd.read_excel( 'categories.xlsx', sheet_name=str(y_x.value + '_' + y2_x.value))
    dataframe1 = data_x
    cate =list(dataframe1['Category'])
    counts =list(dataframe1['Cuenta'])
    source = ColumnDataSource(data=dict(cate=cate, counts=counts),)

    TOOLTIPS = [
        ("Category", "@cate"),
        ("Counts", "@counts"),
    ]
    color_map41_x = factor_cmap(field_name='cate',palette=Category20[20], factors=cate)
    p41_x = figure(plot_width=940, plot_height=600, title="Number of cards by Category",x_range= cate,toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)
    p41_x.vbar(x ='cate', top ='counts',width=0.9,source=source,color =color_map41_x)
    p41_x.xaxis.axis_label_text_font_size = '15pt'
    p41_x.yaxis.axis_label_text_font_size = '15pt'
    p41_x.xaxis.major_label_orientation = pi/4
    p41_x.xaxis.major_label_text_font_size = "15pt"
    ########################################################################
    return p41_x


def figura2_y():
 
    
    data_y = pd.read_excel( 'abilities.xlsx', sheet_name=str(y_x.value +'_' + y2_x.value))
    dataframe1 = data_y
    Abi =list(dataframe1['Abilites'])
    counts =list(dataframe1['Cuenta'])
    source = ColumnDataSource(data=dict(Abi=Abi, counts=counts),)

    TOOLTIPS = [
        ("Ability", "@Abi"),
        ("Counts", "@counts"),
    ]
    color_map41_y = factor_cmap(field_name='Abi',palette=Viridis256[100:200], factors=Abi)
    p41_y = figure(plot_width=940, plot_height=600, title="Number of cards by Ability",x_range= Abi,toolbar_location='above', tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips=TOOLTIPS)
    p41_y.vbar(x ='Abi', top ='counts',width=0.9,source=source,color =color_map41_y)
    p41_y.xaxis.axis_label_text_font_size = '15pt'
    p41_y.yaxis.axis_label_text_font_size = '15pt'
    p41_y.xaxis.major_label_orientation = pi/4
    p41_y.xaxis.major_label_text_font_size = "12pt"

    ########################################################################
    return p41_y

controls2_x = column(y_x, width=200)
controls3_x = column(y2_x, width=200)

layout_control_x = row(controls2_x,controls3_x)
layout41_x = row(figura2_x())
layout41_y = row(figura2_y())

#####################################################################################################
# EXPLICACION DE LAS HABILIDADES
#os.chdir(r'C:/Users/alexs/Desktop/Alejandro/Universidad/Proyectos/Gwent_Dashboard/data')
keywords = pd.read_excel('keywords.xlsx')
habilidades = list(keywords.Ability)


def update_habilidad(attr, old, new):
    layout_habil.children[0]= texto()

def texto():
    #os.chdir(r'C:/Users/alexs/Desktop/Alejandro/Universidad/Proyectos/Gwent_Dashboard/data')
    keywords = pd.read_excel('keywords.xlsx')
    habilidades = list(keywords.Ability)
    texto = keywords[keywords['Ability']==sel_habilidad.value]['Description']
    indice = keywords[keywords['Ability']==sel_habilidad.value]['Description'].index[0]
    texto=texto[indice]
    habilidad=Div(text=texto, margin = (25,0,0,0))
    return habilidad


sel_habilidad = Select(title='Abilities', value='Ambush', options=habilidades)
sel_habilidad.on_change('value', update_habilidad)
layout_habil = row(texto())
coltrol_habilidad = column(sel_habilidad, width=200)
tab8= Panel(child=column(layout_control_x ,row(layout41_x,layout41_y),row(coltrol_habilidad,layout_habil)), title="Abilities - Categories")

#####################################################################################################
# PARA EL TAB LEADERS
  
faction_leaders = ['Monsters','Nilfgaard' ,'Northern Realms','Scoiatael','Skellige','Syndicate']

def text(self):
    div = Div(text=self,width=300, height=100)
    return div
def fig(self):
    p1 = figure(x_range=(0,1), y_range=(0,1),plot_width=150, plot_height=100)
    p1.axis.visible = False
    p1.toolbar.logo = None
    p1.toolbar_location = None
    p1.image_url(url=[self], x=0, y=1, w=1, h=1)

    return p1
todos =[]

for valor_faccion in faction_leaders:
    data = df_gwent_leaders[df_gwent_leaders['FactionId']==valor_faccion]
    data =data[data['Available']!='Tutorial set']
    IDS = data['ID'].to_list()
    tooltip=[]
    url=[]
    results=[]
    results2=[]
    layout_text = []
    layout_fig = []
    for values in IDS:
        tooltip=[]
        url=[]
        tooltip=df_gwent_leaders[df_gwent_leaders['ID']==values]['Tooltip'].tolist()[0]
        url= str('http://localhost:5006/Gwent_Dashboard/static/Skills_leaders/'+valor_faccion+'/'+str(values)+'.png')
        results = [tooltip]
        results2 =[url]
        layout_text.append(results)
        layout_fig.append(results2)


    display=[]
    rows=[]
    for i in range(0,7):
        #print(i)
        display = row(fig(layout_fig[i][0]),text(layout_text[i][0]))
        rows.append(display)
    todos.append(rows)

layout_leaders_monsters = column(row(todos[0][0],todos[0][1],todos[0][2],todos[0][3]),row(todos[0][4],todos[0][5],todos[0][6]))
layout_leaders_nilfgaard = column(row(todos[1][0],todos[1][1],todos[1][2],todos[1][3]),row(todos[1][4],todos[1][5],todos[1][6]))
layout_leaders_NR = column(row(todos[2][0],todos[2][1],todos[2][2],todos[2][3]),row(todos[2][4],todos[2][5],todos[2][6]))
layout_leaders_scoiatel = column(row(todos[3][0],todos[3][1],todos[3][2],todos[3][3]),row(todos[3][4],todos[3][5],todos[3][6]))
layout_leaders_skellige = column(row(todos[4][0],todos[4][1],todos[4][2],todos[4][3]),row(todos[4][4],todos[4][5],todos[4][6]))
layout_leaders_syndicate = column(row(todos[5][0],todos[5][1],todos[5][2],todos[5][3]),row(todos[5][4],todos[5][5],todos[5][6]))


#tab9 = Panel(child=column(controls2_x,row(rows[0])), title="Leaders")
Mon=Div(text='<p style="font-size:20px"><b>Monsters</b></p>')
Nilf=Div(text='<p style="font-size:20px"><b>Nilfgaard</b></p>')
NR=Div(text='<p style="font-size:20px"><b>Northen Realms</b></p>')
Sco=Div(text='<p style="font-size:20px"><b>Scoiatel</b></p>')
Ske=Div(text='<p style="font-size:20px"><b>Skellige</b></p>')
Sy=Div(text='<p style="font-size:20px"><b>Syndicate</b></p>')
#tab9 = Panel(child=column(layout_leaders_monsters),layout_leaders_nilfgaard,layout_leaders_NR,layout_leaders_scoiatel,layout_leaders_skellige,layout_leaders_syndicate), title="Leaders")
tab9 = Panel(child = column(column(Mon,layout_leaders_monsters),column(Nilf,layout_leaders_nilfgaard),column(NR,layout_leaders_NR),column(Sco,layout_leaders_scoiatel),column(Ske,layout_leaders_skellige),column(Sy,layout_leaders_syndicate)) , title="Leaders")
#,column(NR,layout_leaders_NR),column(Sco,layout_leaders_scoiatel),column(Ske,layout_leaders_skellige),column(Sy,layout_leaders_syndicate
#####################################################################################################
tabs = Tabs(tabs=[tab1,tab9, tab2,tab3,tab5,tab8,tab6,tab7])
curdoc().add_root(row(tabs, width=800,))
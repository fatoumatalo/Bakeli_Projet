#----------Import library
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import plotly as iplot
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.offline as pyo
import seaborn as sns
#-------------Import_csv_fichier
data =pd.read_csv('marketing_campaign.csv')
data
#--------data_statut
data_statut = data.groupby('Education').size().to_frame(name='count')
data_statut 
#---visualisation data_statut
 

fig = px.bar(data_statut, x='count', y=data_statut.index, 
             title='Nombre de clients par niveau d\'éducation',
             labels={'count': 'Nombre de clients', 'Education': 'Niveau d\'éducation'},
             color_discrete_sequence=px.colors.qualitative.Pastel1)
fig.update_traces(marker_color=['#7f7f7f', '#dc3912', '#ff9900', '#008080', '#ffd400', '#000080', '#808000', '#008000', '#ffa500'])
fig.show()
#-------------data_statut_matrimonial
data_statut = data.groupby('Marital_Status').size().to_frame(name='count')
data_statut 
#---visualistion

import plotly.express as px

vis_data_statut = data_statut.groupby('Marital_Status')['count'].sum()

fig = px.pie(vis_data_statut, values='count', names=vis_data_statut.index, title='Distribution of people by marital status')
fig.show()
#---------------------------client plus frequent

print(data['Recency'].min())

#----------------------------promotion avec plus grand achat aprés réduction 
data_promotion_favorite = data[data['NumDealsPurchases'] == data['NumDealsPurchases'].max()]
data_promotion_favorite
#---------------------------data_produit
data_produit = data[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']]
data_produit
#----------------------------data_place
Place = data[['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth']]
Place
#--------------------visualisation_place
fig = px.bar(Place.mean(), title='Nombre d’achats par place')
fig.update_yaxes(title='Nombre moyen d’achats')

fig.update_traces(marker_color=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3'])
for i, value in enumerate(Place.mean()):
    fig.add_annotation(x=i, y=value, text=f'{value:.2%}', showarrow=False)

fig.show()
#-----------------------------data_promotion
Promotion = data[['NumDealsPurchases', 'AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']]
Promotion
#----------------------------promotion sans réduction
import plotly.express as px

fig = px.histogram(Promotion, x="AcceptedCmp1", color="Response", barmode="group")
fig.show()

fig = px.histogram(Promotion, x="AcceptedCmp2", color="Response", barmode="group")
fig.show()

fig = px.histogram(Promotion, x="AcceptedCmp3", color="Response", barmode="group")
fig.show()

fig = px.histogram(Promotion, x="AcceptedCmp4", color="Response", barmode="group")
fig.show()

fig = px.histogram(Promotion, x="AcceptedCmp5", color="Response", barmode="group")
fig.show()
fig = px.histogram
#----------------------------promotion_max
Promotion_max =  Promotion[Promotion.NumDealsPurchases == Promotion.NumDealsPurchases.max()]
Promotion_max 
#----------------------------visualisation de pormotion_max
fig = px.bar(Promotion_max.mean(), title='Promotion')
fig.update_yaxes(title='Valeurs moyennes des promotions')
fig.update_layout(showlegend=False)
fig.update_traces(marker_color=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f0e', '#2ca02c', '#d62728'])
fig.show()
#---------------------------data_Age
data["Age"] = 2024 - data["Year_Birth"]
data
#--------------------------nombre-Age-inferieur_40ans

data_age = data[data['Age'] < 40]
nombre_client_moins_40 = data_age.shape[0]
print(f"Nombre de clients qui ont moins de 40 ans : {nombre_client_moins_40}")
#--------------------------nombre-Age-superieur_40ans
nombre_client_plus_40 = data.shape[0] - nombre_client_moins_40
print(f"Nombre de clients qui ont plus de 40 ans : {nombre_client_plus_40}")
#-------------------------data_Age_ID

new_data = data[["Age", "ID"]]
new_data
#--------------------------Visualisation-data-ID-Age
#-----------------Age < 45
import plotly.express as px 
df = new_data[new_data['Age'] < 45]
fig = px.bar(df, x='Age', y='ID')
fig.show()
import plotly.express as px

#------------Age > 45
fig = px.bar(new_data[new_data['Age'] > 45], x='Age', y='ID',
             title='Number of Customers by Age Group (Over 40)')

# Show the bar chart
fig.show()

#Librairies générales
import numpy as np
import pandas as pd
#Librairie stat
#import seaborn as sns


print("-------------- Fichier images_observations.csv --------------")
img_obs = pd.read_csv('images_observations.csv', sep = '\t')
print(img_obs.head(5))
print(img_obs.tail(5))

print("-------------- Fichier location_descriptions.csv --------------")
loca_desc = pd.read_csv('location_descriptions.csv', sep = '\t')
print(loca_desc.head(5))
print(loca_desc.tail(5))

print("-------------- Fichier locations.csv --------------")
locas = pd.read_csv('locations.csv', sep = '\t')
print(locas.head(5))
print(locas.tail(5))

print("-------------- Fichier name_classifications.csv  --------------")
name_class = pd.read_csv('name_classifications.csv', sep = '\t', header=0)
print(name_class.head(5))
print(name_class.tail(5))

print("-------------- Fichier name_descriptions.csv  --------------")
name_desc = pd.read_csv('name_descriptions.csv', sep = '\t', header=0)
print(name_desc.head(5))
print(name_desc.tail(5))

print("-------------- Fichier names.csv  --------------")
names = pd.read_csv('names.csv', sep = '\t', header=0)
print(names.head(5))
print(names.tail(5))


import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")
'''Questão B Organize a base de dados em ordem alfabética por nome''' 
aux = titanic.sort_values("Name")
print(aux.head(50))
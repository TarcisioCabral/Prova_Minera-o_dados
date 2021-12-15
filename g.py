import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")
""" Questão G Apresente o número de sobreviventes por classe"""
titanic1=titanic.loc[titanic["Survived"] == 1]

aux_titanic = titanic1.groupby(['Survived', 'Pclass']).count()
print(aux_titanic)
#print(titanic.head(10))
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")

""" Questão H Apresente o número de mortos por sexo"""
titanic1=titanic.loc[titanic["Survived"] == 0]

aux_titanic = titanic1.groupby(['Survived', 'Sex']).count()
print(aux_titanic)

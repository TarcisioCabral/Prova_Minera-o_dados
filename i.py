import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")

""" Questão I Monte um gráfico(formato a sua escolha) que mostre o número de sobreviventes por classe"""
titanic1=titanic.loc[titanic["Survived"] == 1]
aux_titanic= titanic1.groupby(['Pclass'])['Survived'].count()
 
aux_titanic.plot(kind = 'bar', color = 'orange')
plt.title("Sobreviventes por Classe")
plt.ylabel('Survived')
plt.xlabel('Pclass')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv("titanic.csv")

'''Questão C Crie uma nova série(no mesmo dataframe) com o nome "Sobrevivente",
 o conteúdo deve ser "Sim" caso a coluna Survived for 1 e "Não" caso a coluna Survived for 0''' 
titanic['Survived'] = titanic['Survived'].replace([0],'não')
titanic['Survived'] = titanic['Survived'].replace([1],'sim')
print(titanic.head(10))
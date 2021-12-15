import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")
""" Questão E Renomeie as colunas restantes para sua tradução em português"""

titanic = titanic.rename(columns = {'PassengerId': 'IdPassageiro', 'Survived': 'Sobrevivnetes', 'Pclass':'PClasse', 'Name':'Nome','Sex':'Sexo', 'Age':'Idade', 'Fare':'Tarifa', 'Cabin':'Cabine', 'Embarked':'Embarcou'}, inplace = False)
print(titanic.head(10))
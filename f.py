import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")
""" Questão F Altere os valores da coluna Sexo para: 
male = "masculino"(minúsculas) e female = "FEMININO"(maiúsculas)"""
aux_titanic = titanic.drop(["SibSp", "Parch", "Ticket" ], axis=1)
aux_titanic['Sex'] = aux_titanic['Sex'].replace(["male"],"masculino")
aux_titanic['Sex'] = aux_titanic['Sex'].replace(["female"],"FEMININO")
print(aux_titanic.head(2))
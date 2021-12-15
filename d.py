import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv("titanic.csv")

""" Questão D Remova as colunas "SibSp", "Parch" e "Ticket"""
aux_titanic = titanic.drop(["SibSp", "Parch", "Ticket" ], axis=1)
print(aux_titanic.head(10))

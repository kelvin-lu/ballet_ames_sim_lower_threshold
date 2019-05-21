from ballet import Feature
import sklearn.impute
import sklearn.preprocessing

input = ["Bsmt Qual"]

transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]

name = "Imputed basement height type"

feature = Feature(input=input, transformer=transformer, name=name)

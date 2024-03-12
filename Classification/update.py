import os


for i in os.listdir('F:\\GIt Repo\\machine learning\\Classification'):
    if "iris" in i:
        os.rename(i,'digits')
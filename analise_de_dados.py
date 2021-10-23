import pandas as pd

data1 = pd.read_csv('data/Athletes.csv')
data2 = pd.read_csv('data/Coaches.csv')
data3 = pd.read_csv('data/EntriesGender.csv')
data4 = pd.read_csv('data/Medals.csv')
data5 = pd.read_csv('data/Teams.csv')

def main():
    print(data1.head(3))

main()
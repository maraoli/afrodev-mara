import pandas as pd

def missing(text):
    data = pd.read_csv(f'data/puro/{text}.csv')
    data.info()

missing("Athletes")
missing("Coaches")
missing("EntriesGender")
missing("Medals")
missing("Teams")





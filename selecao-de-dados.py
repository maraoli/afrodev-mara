import pandas as pd

data_athletes = pd.read_csv('data/Athletes.csv')
data_coaches = pd.read_csv('data/Coaches.csv')
data_entries_gender = pd.read_csv('data/EntriesGender.csv')
data_medals = pd.read_csv('data/Medals.csv')
data_teams = pd.read_csv('data/Teams.csv')

def selecao_de_dados():
    # 0 - Total de atletas participantes.
    #11085
    total_de_atletas = data_athletes['Name'].count()

    # 1 - Total de participantes homens.
    #5884
    total_de_homens = data_entries_gender['Male'].sum()

    # 2 - Total de participantes mulheres.
    # 5432
    total_de_mulheres = data_entries_gender['Female'].sum()

    # 3 - Total de participantes por esporte.
    discipline = data_entries_gender['Discipline']
    total = data_entries_gender.iloc[:,[1,2]].sum(axis=1)
    total_por_esporte = pd.concat([discipline, total], axis=1)
    total_por_esporte.columns = ['Discipline', 'Total Athletes']


    # 4 - Total de medalhas por país.
    pais = data_medals['Team/NOC']
    total = data_medals.iloc[:, 2:5].sum(axis=1)
    total_medalhas_por_pais = pd.concat([pais, total], axis=1)
    total_medalhas_por_pais.columns = ['Team/NOC', 'Total Medals']
    print(total_medalhas_por_pais.head(3))

    # 5 - Ranking por medalhas totais.
    # 6 - País com mais medalhas de ouro.
    # 7 - País com mais medalhas de prata.
    # 8 - País com mais medalhas de bronze.
    # 9 - País com menos medalhas de ouro.
    # 10 - País com menos medalhas de prata.
    # 11 - País com menos medalhas de bronze.
    # 12 - Lista com esportes participantes.
    # 13 - Lista de esportes com mais homens que mulheres.
    # 14 - Lista de esportes com mais mulheres que homens.
    # 15 - Quantidade de treinadores por país.
    # 16 - País com a maior quantidade de treinadores
    # 17 - Quantidade de treinadores por esporte.
    # 18 - Quanto times por esporte cada país tem.

selecao_de_dados()
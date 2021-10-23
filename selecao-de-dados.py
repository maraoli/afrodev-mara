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

    # 5 - Ranking por medalhas totais.
    ranking_de_medalhas = total_medalhas_por_pais.sort_values(by="Total Medals", ascending=False)
    ranking_de_medalhas.index = range(ranking_de_medalhas.shape[0])

    # 6 - País com mais medalhas de ouro.
    selecao = data_medals['Gold'] == data_medals['Gold'].max()
    pais_com_mais_medalhas_de_ouro = data_medals[selecao]['Team/NOC']

    # 7 - País com mais medalhas de prata.
    selecao = data_medals['Silver'] == data_medals['Silver'].max()
    pais_com_mais_medalhas_de_prata = data_medals[selecao]['Team/NOC']

    # 8 - País com mais medalhas de bronze.
    selecao = data_medals['Bronze'] == data_medals['Bronze'].max()
    pais_com_mais_medalhas_de_bronze = data_medals[selecao]['Team/NOC']

    # 9 - País com menos medalhas de ouro.
    selecao = data_medals['Gold'] == data_medals['Gold'].min()
    pais_com_menos_medalhas_de_ouro = data_medals[selecao]['Team/NOC']

    # 10 - País com menos medalhas de prata.
    selecao = data_medals['Silver'] == data_medals['Silver'].min()
    pais_com_menos_medalhas_de_prata = data_medals[selecao]['Team/NOC']

    # 11 - País com menos medalhas de bronze.
    selecao = data_medals['Bronze'] == data_medals['Bronze'].min()
    pais_com_menos_medalhas_de_bronze = data_medals[selecao]['Team/NOC']

    # 12 - Lista com esportes participantes.
    esportes_participantes = data_entries_gender['Discipline']

    # 13 - Lista de esportes com mais homens que mulheres.
    selecao = (data_entries_gender['Male'] > data_entries_gender['Female'])
    mais_homens_que_mulheres = data_entries_gender[selecao]['Discipline']
    mais_homens_que_mulheres.index = range(mais_homens_que_mulheres.shape[0])

    # 14 - Lista de esportes com mais mulheres que homens.
    selecao = (data_entries_gender['Female'] > data_entries_gender['Male'])
    mais_mulheres_que_homens = data_entries_gender[selecao]['Discipline']
    mais_mulheres_que_homens.index = range(mais_mulheres_que_homens.shape[0])

    # 15 - Quantidade de treinadores por país.
    agrupamento = data_coaches.groupby('NOC')
    qtd_de_treinador_por_pais = pd.DataFrame(agrupamento['Name'].count())
    qtd_de_treinador_por_pais.columns = ['Total Coaches']

    # 16 - País com a maior quantidade de treinadores
    lista = [qtd_de_treinador_por_pais.index, qtd_de_treinador_por_pais['Total Coaches']]
    data = pd.DataFrame(lista).T
    data.columns = ['NOC', 'Total Coaches']
    selecao = data['Total Coaches'] == data['Total Coaches'].max()
    maior_qtd_de_treinadores = data[selecao]

    # 17 - Quantidade de treinadores por esporte.
    agrupamento = data_coaches.groupby('Discipline')
    qtd_de_treinador_por_esporte = pd.DataFrame(agrupamento['Name'].count())

    # 18 - Quanto times por esporte cada país tem.
    agrupamento =  data_teams.groupby(by=['Discipline','NOC'], dropna=False)
    qtd_de_times_por_esporte_cada_pais = agrupamento['Name'].count()
    qtd_de_times_por_esporte_cada_pais = pd.DataFrame(qtd_de_times_por_esporte_cada_pais)
    qtd_de_times_por_esporte_cada_pais.columns = ['Total Names']
    print(qtd_de_times_por_esporte_cada_pais)

selecao_de_dados()
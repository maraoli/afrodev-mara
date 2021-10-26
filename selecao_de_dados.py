import pandas as pd

data_athletes = pd.read_csv('data/puro/Athletes.csv')
data_coaches = pd.read_csv('data/puro/Coaches.csv')
data_entries_gender = pd.read_csv('data/puro/EntriesGender.csv')
data_medals = pd.read_csv('data/puro/Medals.csv')
data_teams = pd.read_csv('data/puro/Teams.csv')

def selecao_de_dados():

    resposta = []

    # 0 - Total de atletas participantes.
    data_athletes['Name'].drop_duplicates()
    total_de_atletas = data_athletes['Name'].count()
    resposta.append(f"Existem {total_de_atletas} atletas participantes.")

    # 1 - Total de participantes homens.
    total_de_homens = data_entries_gender['Male'].sum()
    resposta.append(f"Existem {total_de_homens} homens participantes.")

    # 2 - Total de participantes mulheres.
    total_de_mulheres = data_entries_gender['Female'].sum()
    resposta.append(f"Existem {total_de_mulheres} mulheres participantes.")

    # 3 - Total de participantes por esporte.
    discipline = data_entries_gender['Discipline']
    total = data_entries_gender.iloc[:,[1,2]].sum(axis=1)
    total_por_esporte = pd.concat([discipline, total], axis=1)
    total_por_esporte.columns = ['Discipline', 'Total Athletes']
    resposta.append(total_por_esporte)

    # 4 - Total de medalhas por país.
    pais = data_medals['Team/NOC']
    total = data_medals.iloc[:, 2:5].sum(axis=1)
    total_medalhas_por_pais = pd.concat([pais, total], axis=1)
    total_medalhas_por_pais.columns = ['Team/NOC', 'Total Medals']
    resposta.append(total_medalhas_por_pais)

    # 5 - Ranking por medalhas totais.
    ranking_de_medalhas = total_medalhas_por_pais.sort_values(by="Total Medals", ascending=False)
    ranking_de_medalhas.index = range(ranking_de_medalhas.shape[0])
    ranking_de_medalhas.columns.name = 'Hanking'
    resposta.append(ranking_de_medalhas)

    # 6 - País com mais medalhas de ouro.
    selecao = data_medals['Gold'] == data_medals['Gold'].max()
    pais_com_mais_medalhas_de_ouro = data_medals[selecao]
    resposta.append(f"O país com mais medalhas de ouro é o "
                    f"{pais_com_mais_medalhas_de_ouro['Team/NOC'][0]} com "
                    f"{pais_com_mais_medalhas_de_ouro['Gold'][0]} medalhas de ouro.")

    # 7 - País com mais medalhas de prata.
    selecao = data_medals['Silver'] == data_medals['Silver'].max()
    pais_com_mais_medalhas_de_prata = data_medals[selecao]
    resposta.append(f"O país com mais medalhas de prata é o "
                    f"{pais_com_mais_medalhas_de_prata['Team/NOC'][0]} com "
                    f"{pais_com_mais_medalhas_de_prata['Silver'][0]} medalhas de prata.")

    # 8 - País com mais medalhas de bronze.
    selecao = data_medals['Bronze'] == data_medals['Bronze'].max()
    pais_com_mais_medalhas_de_bronze = data_medals[selecao]
    resposta.append(f"O país com mais medalhas de bronze é o "
                    f"{pais_com_mais_medalhas_de_bronze['Team/NOC'][0]} com "
                    f"{pais_com_mais_medalhas_de_bronze['Silver'][0]} medalhas de bronze.")

    # 9 - País com menos medalhas de ouro.
    selecao = data_medals['Gold'] == data_medals['Gold'].min()
    pais_com_menos_medalhas_de_ouro = data_medals[selecao]
    pais_com_menos_medalhas_de_ouro.index = range(pais_com_menos_medalhas_de_ouro.shape[0])
    resposta.append(pais_com_menos_medalhas_de_ouro[['Team/NOC','Gold']])

    # 10 - País com menos medalhas de prata.
    selecao = data_medals['Silver'] == data_medals['Silver'].min()
    pais_com_menos_medalhas_de_prata = data_medals[selecao]
    pais_com_menos_medalhas_de_prata.index = range(pais_com_menos_medalhas_de_prata.shape[0])
    resposta.append(pais_com_menos_medalhas_de_prata[['Team/NOC', 'Silver']])

    # 11 - País com menos medalhas de bronze.
    selecao = data_medals['Bronze'] == data_medals['Bronze'].min()
    pais_com_menos_medalhas_de_bronze = data_medals[selecao]
    pais_com_menos_medalhas_de_bronze.index = range(pais_com_menos_medalhas_de_bronze.shape[0])
    resposta.append(pais_com_menos_medalhas_de_bronze[['Team/NOC', 'Bronze']])

    # 12 - Lista com esportes participantes.
    esportes_participantes = data_entries_gender['Discipline']
    resposta.append(esportes_participantes)

    # 13 - Lista de esportes com mais homens que mulheres.
    selecao = (data_entries_gender['Male'] > data_entries_gender['Female'])
    mais_homens_que_mulheres = data_entries_gender[selecao]
    mais_homens_que_mulheres.index = range(mais_homens_que_mulheres.shape[0])
    resposta.append(mais_homens_que_mulheres)

    # 14 - Lista de esportes com mais mulheres que homens.
    selecao = (data_entries_gender['Female'] > data_entries_gender['Male'])
    mais_mulheres_que_homens = data_entries_gender[selecao]
    mais_mulheres_que_homens.index = range(mais_mulheres_que_homens.shape[0])
    resposta.append(mais_mulheres_que_homens)

    # 15 - Quantidade de treinadores por país.
    agrupamento = data_coaches.groupby('NOC')
    qtd_de_treinador_por_pais = pd.DataFrame(agrupamento['Name'].count())
    qtd_de_treinador_por_pais.columns = ['Total Coaches']
    resposta.append(qtd_de_treinador_por_pais)

    # 16 - País com a maior quantidade de treinadores
    lista = [qtd_de_treinador_por_pais.index, qtd_de_treinador_por_pais['Total Coaches']]
    data = pd.DataFrame(lista).T
    data.columns = ['NOC', 'Total Coaches']
    selecao = data['Total Coaches'] == data['Total Coaches'].max()
    maior_qtd_de_treinadores = data[selecao]
    resposta.append(maior_qtd_de_treinadores)

    # 17 - Quantidade de treinadores por esporte.
    agrupamento = data_coaches.groupby('Discipline')
    qtd_de_treinador_por_esporte = pd.DataFrame(agrupamento['Name'].count())
    qtd_de_treinador_por_esporte.columns = ['Total Coaches']
    resposta.append(qtd_de_treinador_por_esporte)

    # 18 - Quantos times por esporte cada país tem.
    agrupamento = data_teams.groupby(by=['Discipline','NOC'])
    qtd_de_times_por_esporte_cada_pais = agrupamento['Name'].count()
    qtd_de_times_por_esporte_cada_pais = pd.DataFrame(qtd_de_times_por_esporte_cada_pais)
    qtd_de_times_por_esporte_cada_pais.columns = ['Total Names']
    resposta.append(qtd_de_times_por_esporte_cada_pais)

    # 19 -Mostre os paises que obtiveram 5 ou mais medalhas de ouro.
    selecione = data_medals['Gold'] >= 5
    mais_que_5_ouros = data_medals[selecione]
    resposta.append(mais_que_5_ouros[['Team/NOC', 'Gold']])

    # 20 -Mostre a porcentagem de paises que obtiveram menos que  5 medalhas de ouro.
    selecione = data_medals['Gold'] < 5
    total = data_medals['Gold'].count()
    menos_que_5 = data_medals[selecione]['Gold'].count()
    porcentagem_menos_5_outros = (menos_que_5 * 100) / total
    porcentagem_menos_5_outros = porcentagem_menos_5_outros.round(2)
    resposta.append(f"{porcentagem_menos_5_outros}% dos países obtiveram menos que 5 medalhas de ouro.")

    # 21 -Mostre o esporte com o maior número de mulheres.
    selecione = data_entries_gender['Female'] == data_entries_gender['Female'].max()
    data = data_entries_gender[selecione]
    esporte_mais_mulheres = str(data.iloc[0,0])
    total_mulheres = int(data['Female'])
    resposta.append(f"Existem {total_mulheres} mulheres no esporte {esporte_mais_mulheres}.")


    # 22 -Mostre o esporte com o maior número de homens.
    selecione = data_entries_gender['Female'] == data_entries_gender['Female'].max()
    data = data_entries_gender[selecione]
    esporte_mais_homens = str(data.iloc[0,0])
    total_homens = int(data['Male'])
    resposta.append(f"Existem {total_homens} homens no esporte {esporte_mais_homens}.")

    return resposta

selecao_de_dados()
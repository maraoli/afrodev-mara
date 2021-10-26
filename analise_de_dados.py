import pandas as pd
import matplotlib.pyplot as plt

data_athletes = pd.read_csv('data/puro/Athletes.csv')
data_coaches = pd.read_csv('data/puro/Coaches.csv')
data_entries_gender = pd.read_csv('data/puro/EntriesGender.csv')
data_medals = pd.read_csv('data/puro/Medals.csv')
data_teams = pd.read_csv('data/puro/Teams.csv')

def boxplot(data, var):
    plt.figure(figsize=(7, 7,))
    data.boxplot([var], color='green')
    plt.show()

def histograma(data, var):
    plt.figure(figsize=(7, 7,))
    data.hist([var], color='green')
    plt.show()

# ANALIZANDO O NUMERO DE MULHERES E HOMENS

#boxplot(data_entries_gender, 'Female')
#boxplot(data_entries_gender, 'Male')

#histograma(data_entries_gender, 'Female')

print()

grande_numero = data_entries_gender['Female'] > 800
print(f" Esporte com mais de 800 mulheres: \n {data_entries_gender[grande_numero][['Discipline','Female']]} \n")

grande_numero = data_entries_gender['Male'] > 1000
print(f" Esporte com mais de 1000 homens: \n {data_entries_gender[grande_numero][['Discipline','Male']]} \n")

# ANALIZANDO O NUMERO DE MEDALHAS

#boxplot(data_medals, 'Gold')
#boxplot(data_medals, 'Silver')
#boxplot(data_medals, 'Bronze')

grande_numero = data_medals['Gold'] > 10
print(f" Países com mais de 10 ouros: \n {data_medals[grande_numero][['Team/NOC', 'Gold']]}  \n")

grande_numero = data_medals['Silver'] > 10
print(f" Países com mais de 10 pratas: \n {data_medals[grande_numero][['Team/NOC', 'Silver']]}  \n")

# ANALISANDO CONCENTRAÇÃO DE MEDALHAS DE OURO

#histograma(data_medals, 'Gold')

selecione = data_medals['Gold'] < 5
total = data_medals['Gold'].count()
menos_que_5 = data_medals[selecione]['Gold'].count()
porcentagem = (menos_que_5 *100) / total
print(f"Total de países: {total}/ Países com menos de 5 ouros: {menos_que_5} Porcentagem:{porcentagem.round(2)}%")

# ANALISANDO CONCENTRAÇÃO DE MEDALHAS DE PRATA

#histograma(data_medals, 'Silver')

selecione = data_medals['Silver'] < 5
total = data_medals['Silver'].count()
menos_que_5 = data_medals[selecione]['Silver'].count()
porcentagem = (menos_que_5 *100) / total
print(f"Total de países: {total}/ Países com menos de 5 pratas: {menos_que_5} Porcentagem:{porcentagem.round(2)}%")

# ANALISANDO CONCENTRAÇÃO DE MEDALHAS DE BRONZE

#histograma(data_medals, 'Bronze')

selecione = data_medals['Bronze'] < 5
total = data_medals['Bronze'].count()
menos_que_5 = data_medals[selecione]['Bronze'].count()
porcentagem = (menos_que_5 *100) / total
print(f"Total de paises: {total}/ Países com menos de 5 bronzes: {menos_que_5} Porcentagem:{porcentagem.round(2)}%")

print()
# ANALIZANDO A BASE DE ATLETAS

# ANALIZANDO OS PAÍSES

data = data_athletes.groupby('NOC')
data = pd.DataFrame(data.count())
lista = [data.index, data['Discipline']]
data = pd.DataFrame(lista).T
data.columns = ['NOC', 'Discipline']
print(f"Paises agrupados: \n {data}")

# conversão de tipo
data['Discipline'] = pd.to_numeric(data['Discipline'])

#boxplot(data, 'Discipline')
#histograma(data, 'Discipline')

selecione = data['Discipline'] > 100
mais_que_100 = data[selecione]
mais_que_100.index = range(mais_que_100.shape[0])
mais_que_100 = mais_que_100.rename(columns={'Discipline': 'Total de atletas'})
print(f" Mais que 100 atletas: \n {mais_que_100} \n")

mais_que_100 = mais_que_100.count()
total = data.count()
porcentagem = (mais_que_100 *100) / total
print(f" Porcentagem de paises com mais de 100 atletas : {porcentagem[0].round(2)}% \n")

# ANALIZANDO AS DISCIPLINE

data = data_athletes.groupby('Discipline')
data = pd.DataFrame(data['Discipline'].count())
data = data.rename(columns={'Discipline': 'Total de atletas'})
print(f"Total de atletas por esporte \n {data} \n")

#boxplot(data, 'Total de atletas')

selecione = data['Total de atletas'] > 500
data =data[selecione]
print(f"Esportes com mais de 500 atletas: \n {data}")
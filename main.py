import pandas as pd

data1 = pd.read_csv('data/Athletes.csv')
data2 = pd.read_csv('data/Coaches.csv')
data3 = pd.read_csv('data/EntriesGender.csv')
data4 = pd.read_csv('data/Medals.csv')
data5 = pd.read_csv('data/Teams.csv')

perguntas = [
	["Total de atletas participantes.", 100]
,	["Total de participantes homens."]
,	["Total de participantes mulheres."]
,	["Total de participantes por esporte."]
,	["Total de medalhas por país."]
,	["Ranking por medalhas totais."]
,	["País com mais medalhas de ouro."]
,	["País com mais medalhas de prata."]
,	["País com mais medalhas de bronze."]
,	["País com menos medalhas de ouro."]
,	["País com menos medalhas de prata."]
,	["País com menos medalhas de bronze."]
,	["Lista com esportes participantes."]
,	["Lista de esportes com mais homens que mulheres."]
,	["Lista de esportes com mais mulheres que homens."]
,	["Quantidade de treinadores por país."]
,	["País com a maior quantidade de treinadores"]
,	["Quantidade de treinadores por esporte."]
,	["Quanto times por esporte cada país tem."]
]

def obter_int():
    valor = None

    while type(valor) != int:
        try:
            valor = int(valor)
        except:
            valor = input("Insira um número: \n")

    return valor

if __name__ == '__main__':
    print("Bem vindo ao sistema Consulta Atletas \n")

    print("Aqui você poderá obter diversas informações sobre atletas, times,  medalhas e muito mais.")
    print("Abaixo será presentado uma lista de opções para selecionar, pressione \"enter\" para prosseguir")
    print("e em seguida digite o número da pergunta desejada que iremos lhe mostrar a resposta. \n")
    print("Caso deseje encerrar o sistema digite ...  \n")

    input("Pressione \"enter\" para prosseguir \n")

    for i in range(len(perguntas)):
        print(perguntas.index(perguntas[i]), "-", perguntas[i][0])

    perg_numero = obter_int()

    if(perguntas[perg_numero][1]):
        print(f"A resposta para a pergunta: \"{perguntas[perg_numero][0]}\" é {perguntas[perg_numero][1]}")

    #print(data5.head(3))
    #print(perguntas.index(perguntas[2]),perguntas[2])
    #var = input("Digite um número: ")
    #print(var)

    #lista2[0].append(0)
    #print(lista2[0][2])



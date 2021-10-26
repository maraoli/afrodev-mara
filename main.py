from selecao_de_dados import selecao_de_dados

perguntas = [
	["Total de atletas participantes."]
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
,	["Quantos times por esporte cada país tem."]
,	["Mostre os paises que obtiveram 5 ou mais medalhas de ouro."]
,	["Mostre a porcentagem de paises que obtiveram menos que 5 medalhas de ouro."]
,	["Mostre o esporte com o maior número de mulheres."]
,	["Mostre o esporte com o maior número de homens."]
]

def obter_int(texto):
    valor = None

    while type(valor) != int:
        try:
            valor = int(valor)
        except:
            valor = input(f"{texto} \n")

    return valor

def saudacao():
    print("Bem vindo ao Sistema Olimpíco \n")

    print("Aqui você poderá obter diversas informações sobre atletas, times,  medalhas e muito mais.")
    print("Abaixo será presentado uma lista de opções para selecionar, pressione \"1\" para prosseguir")
    print("e em seguida digite o número da pergunta desejada que iremos lhe mostrar a resposta. \n")

    obter_int("Pressione \"1\" para prosseguir \n")

def salvar_respostas():
    respostas = selecao_de_dados()

    for i in range(len(respostas)):
        perguntas[i].append(respostas[i])

if __name__ == '__main__':

    saudacao()

    salvar_respostas()

    stop = None

    while stop != 2 :

        for i in range(len(perguntas)):
            print(perguntas.index(perguntas[i]), "-", perguntas[i][0])

        perg_numero = obter_int("Digite um número")

        print(f"A resposta para a pergunta: \"{perguntas[perg_numero][0]}\" é: \n")
        print(perguntas[perg_numero][1])

        stop = obter_int("\n Pressione \"1\" para continuar e \"2\" para terminar a execução deste programa.\n")






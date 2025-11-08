"""Lista de notas dos estudantes, primeiro foi criado variaveis para receber
cada notado  aluno, após receber cada nota individual foi criado uma nova
 variavel para receber as 4 notas"""

nota1 = float(input("Digite sua primeira nota. ex:7.5 "))
nota2 = float(input("Digite sua segunda nota. ex:7.5 "))
nota3 = float(input("Digite sua terceira nota. ex:7.5 "))
nota4 = float(input("Digite sua quarta nota. ex:7.5 "))
notas = [nota1, nota2, nota3, nota4]
# Função regular para calcular a média


def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media
# Função "sum" soma todos os valores presentes dentro da variavel notas
# Variavel total recebe o valor total das notas somadas
# Função len para quantificar os itens da variavel notas
# A média foi calculada recebendo o valor total e dividindo pelo numero de notas
# Return para retornar o valor da operação total/len(notas), e armazenar em media

# Função lambda para arredondar a média para duas casas decimais


def arredondar_media(media): return round(media, 2)

# Calcular a média


media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Verificando se os estudantes foram aprovados

situacao = "aprovado" if media_arredondada >= 7 else "reprovado"


# Resultados

print("suas notas são: ", notas)

print("sua media é: ", media_arredondada)

print("Você foi ", situacao)

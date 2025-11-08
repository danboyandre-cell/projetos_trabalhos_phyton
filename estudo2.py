
import matplotlib.pyplot as plt


class Livro:
    def __init__(self, titulo: str, autor: str, genero: str, qunatidade_disponivel: int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.qunatidade_disponivel = qunatidade_disponivel

    def __str__(self):
        return f"{self.titulo} por {self.autor}, genero {self.genero} quantidade disponivel {self.qunatidade_disponivel}"


# Criar uma lista de livros
biblioteca = []


# Função para adicionar um livro à biblioteca
def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o genero do livro: ")
    qunatidade_disponivel = int(input("Digite a quantidade disponivel: "))

    novo_livro = Livro(titulo, autor, genero, qunatidade_disponivel)
    biblioteca.append(novo_livro)
    print(f"'{titulo}' foi adicionado à biblioteca.\n")


# Função para listar todos os livros na biblioteca
def listar_livros():
    print("\n📚 Lista de livros na biblioteca:")
    if not biblioteca:
        print("Nenhum livro cadastrado ainda.")
    else:
        for livro in biblioteca:
            print(livro)


def buscar_livro():
    busca_titulo = input("Digite o título para busca: ").lower()
    encontrados = [
        livro for livro in biblioteca if busca_titulo in livro.titulo.lower()]
    if encontrados:
        print("\n🔎 Livros encontrados:")
        for livro in encontrados:
            print(livro)
    else:
        print("Nenhum livro encontrado.")


def grafico_livros_por_genero():
    if not biblioteca:
        print("Nenhum livro cadastrado ainda para gerar gráfico.")
        return

    # Pegar todos os gêneros
    generos = [livro.genero for livro in biblioteca]

    # Remover duplicatas e ordenar
    generos = list(set(generos))
    generos.sort()

    # Contagem de livros por gênero
    contagem_por_genero = [
        sum(1 for livro in biblioteca if livro.genero == genero) for genero in generos]

    # Criar gráfico de linha
    plt.plot(generos, contagem_por_genero, marker='o', linestyle='-')
    plt.xlabel('Gênero')
    plt.ylabel('Número de Livros')
    plt.title('Distribuição de Livros na Biblioteca por Gênero')

    # Adicionar rótulos nos pontos
    for i, valor in enumerate(contagem_por_genero):
        plt.text(generos[i], valor, str(valor), ha='center', va='bottom')

    plt.grid(True)
    plt.show()


# Programa principal
while True:
    print("\n=== MENU ===")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro pelo titulo")
    print("4 - Grafico de livro por genero")
    print("5 - sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        buscar_livro()
    elif opcao == "4":
        grafico_livros_por_genero()
    elif opcao == "5":
        print("Saindo do programa. Até mais! 👋")
        break
    else:
        print("Opção inválida, tente novamente.")

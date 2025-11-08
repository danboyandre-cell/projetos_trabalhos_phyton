import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================
# Conectar ao banco
# ============================
conexao = sqlite3.connect("dados_vendas.db")
cursor = conexao.cursor()

# Criar tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')
conexao.commit()

# ============================
# Funções
# ============================

# CREATE


def inserir_venda(data, produto, categoria, valor):
    cursor.execute('''
        INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda)
        VALUES (?, ?, ?, ?)
    ''', (data, produto, categoria, valor))
    conexao.commit()
    print("✅ Venda inserida com sucesso!")

# READ


def listar_vendas():
    df = pd.read_sql_query("SELECT * FROM vendas1", conexao)
    print(df)

# UPDATE


def atualizar_venda(id_venda, novo_produto=None, novo_valor=None):
    if novo_produto:
        cursor.execute(
            "UPDATE vendas1 SET produto = ? WHERE id_venda = ?", (novo_produto, id_venda))
    if novo_valor is not None:
        cursor.execute(
            "UPDATE vendas1 SET valor_venda = ? WHERE id_venda = ?", (novo_valor, id_venda))
    conexao.commit()
    print("✏️ Venda atualizada com sucesso!")

# DELETE


def deletar_venda(id_venda):
    cursor.execute("DELETE FROM vendas1 WHERE id_venda = ?", (id_venda,))
    conexao.commit()
    print("🗑️ Venda deletada com sucesso!")


# ============================
# Menu interativo
# ============================
while True:
    print("\n=== MENU VENDAS ===")
    print("1 - Inserir nova venda")
    print("2 - Listar vendas")
    print("3 - Atualizar venda")
    print("4 - Deletar venda")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        data = input("Digite a data da venda (Dia/mês/Ano ex: 02/12/2001): ")
        produto = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria: ")
        valor = float(input("Digite o valor da venda: "))
        inserir_venda(data, produto, categoria, valor)

    elif opcao == "2":
        listar_vendas()

    elif opcao == "3":
        listar_vendas()
        id_venda = int(input("Digite o ID da venda que deseja atualizar: "))
        novo_produto = input(
            "Digite o novo nome do produto (ou deixe vazio para não alterar): ")
        novo_valor = input(
            "Digite o novo valor (ou deixe vazio para não alterar): ")

        atualizar_venda(
            id_venda,
            novo_produto if novo_produto else None,
            float(novo_valor) if novo_valor else None
        )

    elif opcao == "4":
        listar_vendas()
        id_venda = int(input("Digite o ID da venda que deseja deletar: "))
        deletar_venda(id_venda)

    elif opcao == "5":
        print("👋 Saindo do sistema...")
        break

    else:
        print("❌ Opção inválida, tente novamente!")

df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

print(df_vendas.head())
print(df_vendas.describe())
print(df_vendas.info())
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
df_vendas['mes'] = df_vendas['data_venda'].dt.month
print("Faturamento total:", df_vendas['valor_venda'].sum())
print(df_vendas.groupby('categoria')['valor_venda'].sum())
print(df_vendas.groupby('produto')[
      'valor_venda'].sum().sort_values(ascending=False))
plt.figure(figsize=(6, 4))
sns.barplot(data=df_vendas, x='categoria', y='valor_venda', estimator=sum)
plt.title("Faturamento por Categoria")
plt.show()

# Evolução mensal
plt.figure(figsize=(8, 5))
df_vendas.groupby('mes')['valor_venda'].sum().plot(kind='line', marker='o')
plt.title("Faturamento Mensal")
plt.xlabel("Mês")
plt.ylabel("Total de Vendas")
plt.show()

import json

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class PilhaDeLivros:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self):
        if not self.vazia():
            return self.livros.pop()

    def livro_do_topo(self):
        if not self.vazia():
            return self.livros[-1]

    def total_de_livros(self):
        return len(self.livros)

def carregar_dados():
    try:
        with open("biblioteca.json", "r") as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        return {}

def salvar_dados(dados):
    with open("biblioteca.json", "a") as arquivo:
        json.dump(dados, arquivo, indent=4)

def main():
    pilhas = carregar_dados()

    while True:
        print("\nOpções:")
        print("1. Adicionar livro a uma pilha específica")
        print("2. Remover e retornar o livro do topo de uma pilha específica")
        print("3. Ver o livro do topo de uma pilha específica")
        print("4. Mostrar o total de livros em uma pilha")
        print("5. Criar uma nova pilha para um novo gênero")
        print("6. Listar todos os gêneros disponíveis")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            genero = input("Digite o gênero da pilha: ")
            if genero not in pilhas:
                print(f"O gênero '{genero}' não existe. Crie uma nova pilha para ele.")
            else:
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                livro = Livro(titulo, autor)
                pilhas[genero].adicionar_livro(livro)
                print(f"'{titulo}' adicionado à pilha de '{genero}'.")
                salvar_dados(pilhas)

        elif opcao == "2":
            genero = input("Digite o gênero da pilha: ")
            if genero in pilhas:
                livro_removido = pilhas[genero].remover_livro()
                if livro_removido:
                    print(f"Livro removido do topo da pilha de '{genero}':")
                    print(f"Título: {livro_removido.titulo}")
                    print(f"Autor: {livro_removido.autor}")
                    salvar_dados(pilhas)
                else:
                    print(f"A pilha de '{genero}' está vazia.")
            else:
                print(f"A pilha de '{genero}' não existe.")

        elif opcao == "3":
            genero = input("Digite o gênero da pilha: ")
            if genero in pilhas:
                livro_do_topo = pilhas[genero].livro_do_topo()
                if livro_do_topo:
                    print(f"Livro no topo da pilha de '{genero}':")
                    print(f"Título: {livro_do_topo.titulo}")
                    print(f"Autor: {livro_do_topo.autor}")
                else:
                    print(f"A pilha de '{genero}' está vazia.")
            else:
                print(f"A pilha de '{genero}' não existe.")

        elif opcao == "4":
            genero = input("Digite o gênero da pilha: ")
            if genero in pilhas:
                total = pilhas[genero].total_de_livros()
                print(f"Total de livros na pilha de '{genero}': {total}")
            else:
                print(f"A pilha de '{genero}' não existe.")

        elif opcao == "5":
            genero = input("Digite o nome do novo gênero: ")
            pilhas[genero] = PilhaDeLivros()
            print(f"Pilha de '{genero}' criada com sucesso.")
            salvar_dados(pilhas)

        elif opcao == "6":
            print("Gêneros disponíveis:")
            for genero in pilhas:
                print(genero)

        elif opcao == "7":
            salvar_dados(pilhas)
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

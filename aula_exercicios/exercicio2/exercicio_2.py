import os

class Exercicio2:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = os.path.join('aula_exercicios', 'exercicio2', nome_arquivo)
        
    def nome_string(self) -> None:
        """
            1. Faça um script que verifique se um nome é uma string válida.
        """
        try:
            name = input("Digite seu nome: ")
            if not name.isalpha():
                raise ValueError("Nome deve conter apenas letras.")
            print("Nome válido.")
        except ValueError as ve:
            print(f"String não é válida: {ve}")

    def divisao_exception(self) -> None:
        """
            2. Leia dois números e faça a divisão, capturando exceções para divisão por zero ou valores não numéricos.
        """
        try:
            num_1 = int(input("Digite o primeiro número: "))
            num_2 = int(input("Digite o segundo número: "))
            valor_divisao = num_1 / num_2
            print(f"Resultado da divisão: {valor_divisao}")
        except ValueError:
            print("Valor não é numérico.")
        except ZeroDivisionError:
            print("Divisão por zero não é permitida.")

    def fatorial(self) -> None:
        """
            3. Calcula o fatorial de um número não negativo.
        """
        numero_positivo = int(input("Digite um numero positivo: "))
        if numero_positivo < 0:
            raise ValueError("Número negativo nao possui fatorial.")
        resultado = 1
        for i in range(2, numero_positivo + 1):
            resultado *= i
            print(f"{i-1} fatorial = {resultado}")

    def fatorial_lista(self) -> None:
        """
            4. Calcula o fatorial para uma lista de números inteiros.
        """
        numeros = []
        print("Digite 'parar' quando quiser parar de digitar números")

        while True:
            entrada = input("Digite um número inteiro: ")

            if entrada.lower() == "parar":
                break

            try:
                item = int(entrada)
                if item < 0:
                    raise ValueError("Número negativo não é permitido.")
                numeros.append(item)
            except ValueError as e:
                print(f"Entrada inválida: {e}")
                continue

        for num in numeros:
            resultado = 1
            if num > 1:
                for i in range(2, num + 1):
                    resultado *= i
            print(f"Fatorial de {num} = {resultado}")

    def confirmar_file(self) -> None:
        """
            5. Tendo um arquivo de texto, conte quantas palavras e linhas tem; verifica se está no diretório.
        """
        caminho = os.path.join('aula_exercicios', 'exercicio2', 'numero_palavras.txt')
        try:
            with open(caminho, 'r') as file:
                linhas = file.readlines()

            num_linhas = len(linhas)
            num_palavras = sum(len(linha.split()) for linha in linhas)

            print(f"O arquivo 'numero_palavras.txt'' tem {num_linhas} linhas e {num_palavras} palavras.")

        except FileNotFoundError:
            print(f"arquivo 'numero_palavras.txt'' não encontrado... criando o arquivo")
            open(caminho, 'w').close()

    def salvar_nome_em_arquivo(self) -> None:
        """
            6. Leia um nome completo, mude as iniciais para maiúscula e salve em um arquivo; verifica se nome e arquivo são válidos.
        """
        nome_input = input("Digite seu nome completo: ")
        caminho = os.path.join('aula_exercicios', 'exercicio2', 'mudar_iniciais.txt')
        if not all(c.isalpha() or c.isspace() for c in nome_input) or len(nome_input.strip()) == 0:
            raise ValueError("Nome inválido, use apenas letras.")

        nome_input = nome_input.title()

        try:
            with open(caminho, 'a') as arquivo:
                arquivo.write(nome_input + '\n')
            print(f"Nome '{nome_input}' salvo no arquivo 'mudar_iniciais.txt'.")
        except FileNotFoundError:
            print(f"arquivo 'mudar_iniciais.txt' não encontrado... criando o arquivo")
            open(caminho, 'w').close()

def main():
    exercicio_2 = Exercicio2('dados.txt')
    while True:
        print("\nSelecione uma ação:")
        print("[1] - Verificar nome válido")
        print("[2] - Executar divisão com exceções")
        print("[3] - Calcular fatoriais de uma lista de números")
        print("[4] - Calcular fatoriais de uma lista de números")
        print("[5] - Confirmar arquivo e contar palavras e linhas")
        print("[6] - Salvar nome completo formatado em arquivo")
        print("[0] - Sair")

        escolha = int(input("Digite sua escolha: "))
        match escolha:
            case 1:
                exercicio_2.nome_string()
            case 2:
                exercicio_2.divisao_exception()
            case 3:
                exercicio_2.fatorial()
            case 4:
                exercicio_2.fatorial_lista()
            case 5:
                exercicio_2.confirmar_file()
            case 6:
                exercicio_2.salvar_nome_em_arquivo()
            case 7:
                print("Programa finalizado!")
                break
            case _:
                print("Opcao invalida")

if __name__ == '__main__':
    if not os.path.exists(os.path.join('aula_exercicios', 'exercicio2')):
        os.makedirs(os.path.join('aula_exercicios', 'exercicio2'))
    main()
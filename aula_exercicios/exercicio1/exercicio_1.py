from datetime import datetime
import os


class Exercicio1():
    def __init__(self, nome_arquivo):
        self.nome_arquivo = os.path.join('aula_exercicios', 'exercicio1', nome_arquivo)

    def tabuada_nove(self):
        """
            1. Elabore um programa em Python que insere a tabuada de multiplicação de 9 em um arquivo txt.
        """
        lines = []
        caminho = os.path.join('aula_exercicios', 'exercicio1', 'tabuada_nove.txt')
        for num in range(1, 11):
            resultado = num * 9
            lines.append(f"{num} X 9 = {resultado}")

        data = "\n".join(lines)

        with open(caminho, 'w') as file:
            file.write(data)
        
        with open(caminho, 'r') as file:
                print(file.read())
        

    def dados_pessoa(self):
        """
            2. Faça um programa que leia os dados de uma pessoa (Nome, RG, CPF, ano de nascimento e armazene em 
            um arquivo txt, calculando a idade da pessoa.
        """
        caminho = os.path.join('aula_exercicios', 'exercicio1', 'dados_pessoa.txt')

        nome = str(input("Nome: "))
        rg = int(input("RG: "))
        cpf = int(input("CPF: "))
        ano_nascimento = int(input("Ano de nascimento: "))

        ano_atual = datetime.now().year
        idade = ano_atual - ano_nascimento
        
        dados = (
            f"Nome: {nome}\n"
            f"RG: {rg}\n"
            f"CPF: {cpf}\n"
            f"Ano de Nascimento: {ano_nascimento}\n"
            f"Idade: {idade} anos\n"
        )

        with open(caminho, 'w') as file:
            file.write(dados)
            print('\n')

        with open(caminho, 'r') as file:
                print(file.read())

    def ler_arquivo(self) -> list:
        """
            3. Faça um programa que leia um arquivo txt e insere cada linha em uma lista.
        """
        lines = []
        caminho = os.path.join('aula_exercicios', 'exercicio1', 'ler_arquivo.txt')
        with open(caminho, "r") as file:
            lines = [line.strip() for line in file.readlines()]

        print("Arquivos transcritos com sucesso!")
        return lines
    
    def medir_notas(self):
        """
            4. Elabore um programa em Python que leia o nome e duas notas de um aluno do teclado, 
            calcule a média e armazene em um arquivo txt o nome, a média 
            final e se o mesmo foi Aprovado (média >=6) ou Reprovado (média < 6).
        """
        nome = str(input("Nome do aluno: "))
        caminho = os.path.join('aula_exercicios', 'exercicio1', 'resultado_aluno.txt')

        notas = []
        for i in range(0, 2):
            while True:
                nota = float(input(f"Nota {i}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota deve estar entre 0 e 10.")


        media = sum(notas) / 2
        status = "Aprovado" if media >= 6 else "Reprovado"

        dados = (
            f"Nome: {nome}\n"
            f"Média: {media:.2f}\n"
            f"Status: {status}\n"
        )
        with open(caminho, 'w') as file:
            file.write(dados)
            print('\n')

        with open(caminho, 'r') as file:
                print(file.read())

    def mini_calculadora(self):
        """
            5. Faça um algoritmo em Python que leia dois números inteiros do teclado, faça uma mini calculadora 
            (soma, subtração, multiplicação e divisão) e armazene todos os resultados em um arquivo txt.
        """
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        caminho = os.path.join('aula_exercicios', 'exercicio1', 'resultados_calculadora.txt')

        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2
        divisao = "Indefinida (divisão por zero)" if num2 == 0 else num1 / num2

        dados = (
            f"Números: {num1} e {num2}\n"
            f"Soma: {soma}\n"
            f"Subtração: {subtracao}\n"
            f"Multiplicação: {multiplicacao}\n"
            f"Divisão: {divisao}\n"
        )
        with open(caminho, 'w') as file:
            file.write(dados)
            print('\n')

        with open(caminho, 'r') as file:
                print(file.read())

    def dna_inverso(self):
        """
            6. Elabore um programa em Python que leia uma cadeia de DNA e gera a cadeia inversa. 
            Faça a leitura da cadeia utilizando arquivo txt. Exemplo: Entrada: AATCTGCAC Saída: CACGTCTAA
        """
        caminho_input = os.path.join('aula_exercicios', 'exercicio1', 'dna.txt')
        caminho_output = os.path.join('aula_exercicios', 'exercicio1', 'dna_invertido.txt')
        with open(caminho_input, "r") as file:
            dna = file.read().strip().upper()

        dna_invertido = dna[::-1]
        with open(caminho_output, "w") as file:
            file.write(dna_invertido)
        
        with open(caminho_output, 'r') as file:
            print(f"Cadeia invertida salva em 'dna_invertido'\n")
            print(file.read())
    
    def contar_palavras(self) -> int:
        """
            7. Faça um programa que leia um texto de um arquivo txt e conte quantas palavras tem nesse arquivo, 
            sem considerar os espaços.
        """
        caminho = os.path.join('aula_exercicios', 'exercicio1', 'contar_palavras.txt')
        with open(caminho, "r") as file:
            texto = file.read()
            palavras = texto.split()
            quantidade = len(palavras)

        with open(caminho, 'r') as file:
            print(file.read())
            print(f"\nO arquivo 'contar_palavras' contém {quantidade} palavras.")

    def substituir_espacos(self):
        """
            8. Faça um programa que Python que lê um texto de um arquivo txt e substitua todos os espaços por underline (_).
        """
        input_file =  os.path.join('aula_exercicios', 'exercicio1', 'espaco_normal.txt')
        output_file =  os.path.join('aula_exercicios', 'exercicio1', 'espaco_substituido.txt')
        with open(input_file, "r") as file:
            texto = file.read()
        
        texto_modificado = texto.replace(" ", "_")
        with open(output_file, "w") as file:
            file.write(texto_modificado)

        with open(output_file, 'r') as file:
            print(file.read())

    def inserir_frase(self) -> list:
        """
            9. Elabore um script em Python que leia um arquivo contendo frases e insira cada palavra da frase lida em uma lista, sem que haja palavras repetidas. 
            Exemplo: A frase lida de um arquivo: “futebol tequila bola futebol torcida bola goleiro”, deve ir para a lista [“futebol”, “tequila”, “bola”, “torcida”, “goleiro”]
        """
        unique_words = []
        caminho = os.path.join('aula_exercicios', 'exercicio1', 'inserir_frase.txt')

        with open(caminho, "r") as file:
            for line in file:
                words = line.strip().split()

                for word in words:
                    if word not in unique_words:
                        unique_words.append(word)

        print(f"\nLista de palavras únicas: {unique_words}")
        print(f"\nTotal de palavras únicas: {len(unique_words)}")

def main():
    exercicio_1 = Exercicio1('dados.txt')
    while True:
        print("\nSelecione uma ação:")
        print("[1] - Inserir tabuada de 9")
        print("[2] - Salvar dados pessoais")
        print("[3] - ler arquivos em lista")
        print("[4] - Calcular media de notas")
        print("[5] - Mini clculadora")
        print("[6] - Criar um DNA invertido")
        print("[7] - Contador de palavras")
        print("[8] - Substituir espaco de arquivo")
        print("[9] - Inserir palavra de frase")
        print("[0] - Sair")

        escolha = int(input("Digite sua escolha: "))
        match escolha:
            case 1:
                exercicio_1.tabuada_nove()
            case 2:
                exercicio_1.dados_pessoa()
            case 3:
                exercicio_1.ler_arquivo()
            case 4:
                exercicio_1.medir_notas()
            case 5:
                exercicio_1.mini_calculadora()
            case 6:
                exercicio_1.dna_inverso()
            case 7:
                exercicio_1.contar_palavras()
            case 8:
                exercicio_1.substituir_espacos()
            case 9:
                exercicio_1.inserir_frase()
            case 7:
                print("Programa finalizado!")
                break
            case _:
                print("Opcao invalida")

if __name__ == '__main__':
    if not os.path.exists(os.path.join('aula_exercicios', 'exercicio1')):
        os.makedirs(os.path.join('aula_exercicios', 'exercicio1'))
    main()
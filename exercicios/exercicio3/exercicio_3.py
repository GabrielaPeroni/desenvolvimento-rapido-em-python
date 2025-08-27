import os
import string

class Exercicio3:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = os.path.join('exercicios', 'exercicio3', nome_arquivo)

    def ler_ou_criar_arquivo(self):
        """
            1) (Ler ou criar arquivo) Abra “notas.txt” em modo leitura. Se não existir, capture FileNotFoundError
            e crie o arquivo com o texto “Arquivo criado.”, depois leia e imprima o conteúdo.
        """
        try:
            with open(self.nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
                print("conteúdo do arquivo:\n", conteudo)
        except FileNotFoundError:
            with open(self.nome_arquivo, 'w') as arquivo:
                print("arquivo não encontrado... criando o arquivo")
                arquivo.write("Arquivo criado.")

            with open(self.nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
                print("conteúdo do novo arquivo:\n", conteudo)

    def contar_linhas_nao_vazias(self):
        """
            2) (Contar linhas não vazias) Leia um arquivo “frases.txt” e exiba quantas linhas não estão vazias
            (desconsidere espaços). Trate PermissionError imprimindo uma mensagem amigável.
        """
        caminho = os.path.join('exercicios', 'exercicio3', 'frases.txt')
        try:
            with open(caminho, 'r') as arquivo:
                linhas = arquivo.readlines()
                linhas_nao_vazias = [linha for linha in linhas if linha.strip()]
                print(f"número de linhas não vazias: {len(linhas_nao_vazias)}")
        except FileNotFoundError:
            with open(caminho, 'w') as arquivo:
                print("arquivo não encontrado... criando o arquivo")
                arquivo.write("Arquivo criado.")
        except PermissionError:
            print("acesso negado para 'frases.txt'")

    def normalizar_espacos_e_pontos(self):
        """
            3) (Normalizar espaços e pontos) Leia “comentarios.txt”, remova espaços duplos e troque
            reticências “...” por um único “.”. Salve em “comentarios.txt”. Use try/except para lidar
            com UnicodeDecodeError (tente utf-8 e, se falhar, latin-1).
        """
        caminho = os.path.join('exercicios', 'exercicio3', 'comentarios.txt')
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                print("conteúdo do arquivo:\n", conteudo)
        except UnicodeDecodeError:
            with open(caminho, 'r', encoding='latin-1') as arquivo:
                conteudo = arquivo.read()
                print("conteúdo do arquivo (latin-1):\n", conteudo)
        except FileNotFoundError:
            with open(caminho, 'w') as arquivo:
                print("arquivo não encontrado... criando o arquivo")
                arquivo.write("Arquivo criado.")
            return

        conteudo = conteudo.replace('  ', ' ').replace('...', '.')
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
            print("arquivo 'comentarios.txt' atualizado com sucesso")

    def separar_nome_e_time(self):
        """
            4) (Nome e time separados por vírgula) De “jogadores_times.txt”, para cada linha com vírgula,
            separe na primeira vírgula e monte um dicionário {nome: time}. Ignore linhas inválidas (sem
            vírgula) e registre-as em “linhas_invalidas.log”. Use try/except no split e na escrita do log.
        """
        caminho = os.path.join('exercicios', 'exercicio3', 'jogadores_times.txt')
        jogadores_times = {}
        try:
            with open(caminho, 'r') as arquivo:
                linhas_invalidas = []
                for linha in arquivo:
                    try:
                        nome, time = linha.strip().split(',', 1)
                        jogadores_times[nome.strip()] = time.strip()
                    except ValueError:
                        linhas_invalidas.append(linha.strip())

            log_path = os.path.join('exercicios', 'exercicio3', 'linhas_invalidas.log')
            with open(log_path, 'w') as log:
                print("linhas inválidas salvas em 'linhas_invalidas.log'")
                for linha in linhas_invalidas:
                    log.write(linha + '\n')

            print(f"Jogadores e times: {jogadores_times}")
        except FileNotFoundError:
            with open(caminho, 'w') as arquivo:
                print("arquivo não encontrado... criando o arquivo")
                arquivo.write("Arquivo criado.")

    def dados_ordenados(self):
        """
            5) (Dados ordenados) Dado os arquivos “lista_a.txt” e “lista_b.txt” (um item por linha), gere um
            arquivo novo “lista_uniq.txt” com itens únicos ordenados. Se algum arquivo não puder ser lido,
            avise no terminal e prossiga com o que der. Dica: Use set() + sorted(); capture FileNotFoundError
            separadamente.
        """
        itens = set()
        arquivos = ['lista_a.txt', 'lista_b.txt']
        caminhos = [os.path.join('exercicios', 'exercicio3', nome) for nome in arquivos]

        for caminho in caminhos:
            try:
                with open(caminho, 'r') as arquivo:
                    itens.update(line.strip() for line in arquivo if line.strip())
            except FileNotFoundError:
                print(f"arquivo '{caminho}' não encontrado... criando o arquivo")
                open(caminho, 'w').close()

        uniq_path = os.path.join('exercicios', 'exercicio3', 'lista_uniq.txt')
        itens_ordenados = sorted(itens)
        with open(uniq_path, 'w', encoding='utf-8') as arquivo:
            print("arquivo 'lista_uniq.txt' criado com sucesso")
            for item in itens_ordenados:
                arquivo.write(item + '\n')

    def palavras_unicas(self):
        """
            6) (Palavras únicas) Leia “texto.txt”, transforme em minúsculas, remova pontuação básica e mostre a
            quantidade de palavras distintas. Trate FileNotFoundError e mostre 'arquivo texto.txt não
            encontrado'.
        """
        caminho = os.path.join('exercicios', 'exercicio3', 'texto.txt')
        try:
            with open(caminho, 'r') as arquivo:
                conteudo = arquivo.read().lower()
            conteudo = conteudo.translate(str.maketrans('', '', string.punctuation))
            palavras = set(conteudo.split())
            print(f"número de palavras distintas: {len(palavras)}")
        except FileNotFoundError:
            with open(caminho, 'w') as arquivo:
                print("arquivo não encontrado... criando o arquivo")
                arquivo.write("Arquivo criado.")

    def mesclar_listas_sem_duplicatas(self):
        """
            7) (Mesclar listas sem duplicatas) Leia “lista_a.txt” e “lista_b.txt” (um item por linha), junte tudo,
            remova duplicatas e salve em “lista_unica.txt” em ordem alfabética. Se um dos arquivos faltar,
            processe apenas o que existir e avise no terminal.
        """
        itens = set()
        arquivos = ['lista_a.txt', 'lista_b.txt']
        caminhos = [os.path.join('exercicios', 'exercicio3', nome) for nome in arquivos]

        for caminho in caminhos:
            if os.path.exists(caminho):
                with open(caminho, 'r') as arquivo:
                    itens.update(line.strip() for line in arquivo if line.strip())
            else:
                print(f"arquivo '{caminho}' não encontrado...")

        unica_path = os.path.join('exercicios', 'exercicio3', 'lista_unica.txt')
        itens_ordenados = sorted(itens)
        with open(unica_path, 'w', encoding='utf-8') as arquivo:
            print("arquivo 'lista_unica.txt' criado com sucesso")
            for item in itens_ordenados:
                arquivo.write(item + '\n')


def main():
    exercicio_3 = Exercicio3('notas.txt')
    while True:
        print("\nSelecione um exercício:")
        print("[1] - ler ou criar arquivo")
        print("[2] - contar linhas não vazias")
        print("[3] - normalizar espaços e pontos")
        print("[4] - separar nome e time")
        print("[5] - dados ordenados")
        print("[6] - palavras únicas")
        print("[7] - mesclar listas sem duplicatas")
        print("[0] - sair")

        escolha = input("Digite sua escolha: ").strip()
        match escolha:
            case '1':
                exercicio_3.ler_ou_criar_arquivo()
            case '2':
                exercicio_3.contar_linhas_nao_vazias()
            case '3':
                exercicio_3.normalizar_espacos_e_pontos()
            case '4':
                exercicio_3.separar_nome_e_time()
            case '5':
                exercicio_3.dados_ordenados()
            case '6':
                exercicio_3.palavras_unicas()
            case '7':
                exercicio_3.mesclar_listas_sem_duplicatas()
            case '0':
                print("programa finalizado!")
                break
            case _:
                print("opção inválida")


if __name__ == '__main__':
    if not os.path.exists(os.path.join('exercicios', 'exercicio3')):
        os.makedirs(os.path.join('exercicios', 'exercicio3'))
    main()
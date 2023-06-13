import os
import sys
from alguma_lexer import AlgumaLexerAnalyzer

""" Main function do nosso analisador léxico e sintático
    Recebe a pasta de entrada e a pasta de saída como argumentos. Se a pasta de saída
    não existir, ela é criada.

    Para cada arquivo na pasta de entrada, o analisador léxico é chamado e o arquivo
    de saída é gerado na pasta de saída com o mesmo nome do arquivo de entrada.

    Caso o arquivo de saída já exista, ele é sobrescrito.

    Exemplo de uso:
    ```
    $ python3 main.py input output
    ```
    Onde input é a pasta de entrada e output é a pasta de saída.

    O analisador léxico tem sua lógica implementado em lexical_compiler/alguma_lexer.py

"""

def main(args):
    # Verifica se os argumentos foram passados corretamente
    if len(args) != 2:
        print("Usage: python3 main.py input_folder output_folder")
        sys.exit(1)

    # Verifica se a pasta de entrada existe
    if not os.path.isdir(args[0]):
        print("Input folder does not exist")
        sys.exit(1)
    
    # Verifica se a pasta de saída existe, se não existir, cria
    if not os.path.isdir(args[1]):
        os.mkdir(args[1])

    # Instancia o analisador léxico
    alguma_lexer = AlgumaLexerAnalyzer()

    # Pega todos os arquivos da pasta de entrada
    files_to_analyze = os.listdir(args[0])

    # Para cada arquivo, chama o analisador léxico

    for file in files_to_analyze:
        print(f"Analyzing {file}")
        alguma_lexer.analyse_file(f"{args[0]}/{file}", f"{args[1]}/{file}")

if __name__ == '__main__':
    # main(["input", "output"])
    main(sys.argv[1:])
import os
import sys
from alguma_lexer import AlgumaLexerAnalyzer

""" Main function do nosso analisador léxico e sintático
    Recebe o arquivo de entrada e o arquivo de saída como argumentos. Se a pasta destino,
    onde o arquivo de saída será escrito não existir, ela é criada, assim como o arquivo.

    Caso o arquivo de saída já exista, ele é sobrescrito.

    Exemplo de uso:
    ```
    $ python3 main.py input/arquivo_teste1.txt output/arquivo_teste1.txt
    ```

    Onde input/arquivo_teste1.txt é o arquivo de entrada e output/arquivoteste1.txt é o arquivo
    de saída.

    O analisador léxico tem sua lógica implementado em lexical_compiler/alguma_lexer.py
"""

def main(args):
    # Verifica se os argumentos foram passados corretamente
    if len(args) != 2:
        print("Usage: python3 main.py input/file.txt output/file.txt")
        sys.exit(1)

    # Verifica se o arquivo de entrada existe
    if not os.path.isfile(args[0]):
        print(args[0])
        print("Input file does not exist")
        sys.exit(1)
    
    # Verifica se a pasta destino existe, se não existir, cria
    if not os.path.isdir(os.path.dirname(args[1])):
        os.makedirs(os.path.dirname(args[1]))

    # Instancia o analisador léxico
    alguma_lexer = AlgumaLexerAnalyzer()

    # Para cada arquivo, chama o analisador léxico
    alguma_lexer.analyse_file(args[0], args[1])

if __name__ == '__main__':
    # main(["input", "output"])
    main(sys.argv[1:])
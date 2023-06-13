from antlr4 import *
from lexer.grammarLinguagemLALexer import grammarLinguagemLALexer
from lexer.grammarLinguagemLAParser import grammarLinguagemLAParser
from lexer.grammarLinguagemLAListener import grammarLinguagemLAListener
from error_handling import LexerErrorHandler
from error_handling import ParserErrorHandler

"""
    Classe responsável por analisar o arquivo de entrada e gerar o arquivo de saída
    com os tokens encontrados.

    O método error_handling é chamado quando um erro léxico é encontrado. Ele recebe
    o token que causou o erro e escreve no arquivo de saída a mensagem de erro
    correspondente.

    O método analyse_file recebe o arquivo de entrada e o arquivo de saída e chama
    o analisador léxico para cada token do arquivo de entrada. Quando o token EOF
    é encontrado, o loop é encerrado.

    Exemplo de uso:
    ```
    lexer = AlgumaLexerAnalyzer()
    lexer.analyse_file("input_file.txt", "output_file.txt")
    ```

    O analisador léxico tem sua lógica implementado em dist/AlgumaLexer.py, criada pelo
    ANTLR, utilizando a gramática definida em AlgumaLexer.g4.

    O arquivo AlgumaLexer.py é gerado automaticamente pelo ANTLR, não deve ser alterado.
    
"""


class AlgumaLexerAnalyzer():

    # Função para mudar os error handlers do lexer e parser
    # criados no arquivo error_handling.py
    def change_error_handlers(self):
        self.la_lexer.removeErrorListeners()
        self.la_lexer.addErrorListener(LexerErrorHandler())

        self.parser.removeErrorListeners()
        self.parser.addErrorListener(ParserErrorHandler())

    def analyse_file(self, input_file, output_file):
        self.input_stream = FileStream(input_file, encoding='utf-8')
        self.output_stream = open(output_file, 'w')
        self.la_lexer = grammarLinguagemLALexer(self.input_stream)

        # Aqui definimos o Parser do nosso compilador
        tokens = CommonTokenStream(self.la_lexer)
        self.parser = grammarLinguagemLAParser(tokens)

        self.change_error_handlers()

        try:
            self.parser.programa()
        except Exception as e:
            # Se alguma exceção for gerada no nosso código, ela será capturada aqui
            # e a mensagem de erro será escrita no arquivo de saída
            self.output_stream.write(str(e))
            self.output_stream.write("\nFim da compilacao\n")

        self.output_stream.close()
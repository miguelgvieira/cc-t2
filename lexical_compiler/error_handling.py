from antlr4.error.ErrorListener import ErrorListener

"""
    De acordo com a documentação, criar uma classe que herda de ErrorListener
    e sobrescrever o método syntaxError é a forma recomendada de tratar erros
    léxicos e sintáticos no ANTLR.
"""

class LexerErrorHandler(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Parser da mensagem de erro para pegarmos a informação do símbolo que representa o erro
        error_symbol = str(e).split("(")[1][1]

        if error_symbol == '"':
            raise Exception(f'Linha {line}: cadeia literal nao fechada')
        elif error_symbol == '{':
            raise Exception(f'Linha {line}: comentario nao fechado')
        else:
            raise Exception(f'Linha {line}: {error_symbol} - simbolo nao identificado')

class ParserErrorHandler(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Pegamos o valor do símbolo que causou o erro
        symbol = offendingSymbol.text
        if symbol == '<EOF>':
            symbol = 'EOF'

        raise Exception(f'Linha {line}: erro sintatico proximo a {symbol}')
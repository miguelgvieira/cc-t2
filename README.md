# cc-t1

Repositório com o trabalho 2 de construção de compiladores.

# Aluno

- Miguel Gonçalves Vieira, RA: 609790

# Instalação

Recomenda-se utilizar um ambiente virtual para instalar os pacotes necessários, para não interferir com outros projetos. Foi utilizado o Python 3.11.3 para desenvolvimento.

```
python3 -m venv {virtual-env-name}
source {virtual-env-name}/bin/activate
```

Para instalar os pacotes necessários para rodar o programa, execute o comando:

```
pip3 install -r requirements.txt
````

# Rodando

Para executar o programa, basta executar o arquivo `lexical_compiler/main.py`
passando como argumento o arquivo de entrada e o arquivo de saída. Se o arquivo de saída e a pasta não existirem, serão criados automaticamente

Exemplo:
```
python3 lexical_compiler/main.py input_folder/input_file.txt output_folder/input_file.txt
```

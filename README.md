# cc-t1

Repositório com o trabalho 2 de construção de compiladores.

# Aluno

- Miguel Gonçalves Vieira, RA: 609790

# Instalação

Recomenda-se utilizar um ambiente virtual para instalar os pacotes necessários, para não interferir com outros projetos.

```
python3 -m venv {virtual-env-name}
source {virtual-env-name}/bin/activate
```

Para instalar os pacotes necessários para rodar o programa, execute o comando:

```
pip3 install -r requirements.txt
````

Para o desenvolvimento foi utilizado Python 3.11.3.

# Rodando

Para executar o programa, basta executar o arquivo `lexical_compiler/main.py`
passando como argumento a pasta com os arquivos de entrada, e a pasta para serem escriots os arquivos de saída.

Exemplo:
```
python3 lexical_compiler/main.py input_folder output_folder
```

Note que a pasta com os arquivos de entrada deve existir, mas a pasta de saída não precisa, ela será criada automaticamente caso não exista.

O programa irá ler todos os arquivos da pasta de entrada, e para cada arquivo, irá gerar um arquivo de saída com o mesmo nome na pasta de saída.

Exemplo:
```
input_folder/
    file1.txt
    file2.txt
    file3.txt
output_folder/
    file1.txt
    file2.txt
    file3.txt
```
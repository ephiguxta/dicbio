#!/usr/bin/python3

import re

from os import listdir
from os import path

# Pega todas as páginas que estão em TXTs separados e atribui a
# uma lista.
pages_dir_path = '../Compendio_Botanica_Vol2/Capítulo_1/'
pages = listdir(pages_dir_path)

for i in pages:

    # Evita os diretórios
    if not path.isfile(pages_dir_path + i):
        continue

    with open(pages_dir_path + i, 'r') as f:
        text = f.read()

        # TODO:
        #       Não deixe de verificar manualmente as inserções para
        #       corrigir possíveis bugs.

        # Caso comum da finalização de uma sentença, com as letras
        # geralmente minúsculas seguida por um ponto, que logo após o
        # ponto se inicia outra sentença com a primeira letra maiúscula
        text = re.sub(r'(([A-Z]|)[a-z]+\.) ([A-Z](|[a-z]+))',
                      r'\1</s> \3',
                      text)

        # Procura pelo caso anterior, pois a outra sentença que se inicia
        # precisa de um marcador <s>
        text = re.sub(r'(\.<\/s>) ([A-Z](|[a-z]+))',
                      r'\1 <s>\2',
                      text)

        # Aqui não damos match com '&l.' e inserimos a tag </s> quando for
        # final de linha.
        text = re.sub(r'(([A-Z]|)(?<!&)[a-z]+\.)(\s)',
                      r'\1</s>\3',
                      text)

        # Quando há uma sentença ou palavra dentro de um parêntese e termina
        # com um ponto, insere </s>.
        text = re.sub(r' (\((([A-Z]|)[a-z]+( |))+\)\.)(\s)',
                      r' \1</s>\5',
                      text)

        # Quando ocorre '(l).', padrão quando o texto está referenciando
        # as notas de rodapé.
        text = re.sub(r'(([A-Z]|)[a-z]+ )(\([a-z]\)\.)(\s)',
                      r'\1\2\3</s>\4',
                      text)

        # Se houver na linha anterior a tag </s> e se existir um novo
        # início de parágrafo na linha atual, insere <s>.
        text = re.sub(r'(([A-Z]|)[a-z]+\.</s>\n)([A-Z][a-z]+)',
                      r'\1<s>\3',
                      text)

        # Há algumas páginas que possuem notas de rodapé, as notas geralmente
        # começam com '(l)' sendo 'l' == [a-z]
        text = re.sub(r'\n(\([a-z]\) )',
                      r'\n<s>\1',
                      text)

        treated_text = pages_dir_path + i[0:1] + '_tratado.txt'

        with open(treated_text, 'w+') as new_file:
            print(text, file = new_file)

#!/usr/bin/python3

from re import findall
from re import sub

from os import listdir
from os import path
from os import makedirs

# Pega todas as páginas que estão em TXTs separados e atribui a
# uma lista.
pages_dir_path = '../Compendio_Brotero_Vol2/Capítulo_1/'
pages = listdir(pages_dir_path)

output_dir = 'words_in_order'

for i in pages:
    with open(pages_dir_path + i, 'r') as file:
        entire_page = file.read()

        # Iterando de A a Z para ordenar as palavras
        for i in range(ord('a'), ord('z')):

            # "Religando" as palavras que são separadas por hífen quando
            # estão no final de uma linha e sua continuação fica na linha
            # abaixo.
            words = sub(r'([a-z]+)\-\s([a-z]+)(,| )',
                        r'\1\2\3\n',
                        entire_page)

            # Esse regex exige que a palavra seja no mínimo da seguinte forma:
            #
            # [Ll][a-z] _ _
            # (Sendo 'L' a letra em maiúscula e 'l' minúscula)
            #
            # A palavra deve conter no mínimo 4 letras.
            # Também deve conter um espaço, quebra de linha ou vírgula
            # após a palavra
            #
            words = findall(r"\b[%s%s][a-z]{3,}(?=\s)" % (chr(i - 32), chr(i)),
                            words)

            if str(words) != '[]':
                # Caso o diretório onde ficarão os arquivos [a-z].txt
                # não exista, crie um.
                words_dir = pages_dir_path + output_dir
                if not path.exists(words_dir):
                    makedirs(words_dir)

                # Criando o caminho para o arquivo que será armazenado as
                # palavras com a mesma letra inicial.
                newfile = words_dir + '/' + chr(i) + '.txt'

                # TODO:
                #   Evitar repetição de palavras.
                with open(newfile, 'a') as letter_text:
                    print(*words, sep='\n', file = letter_text)

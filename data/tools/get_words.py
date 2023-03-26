#!/usr/bin/python3

# TODO:
#   Essa versão se trata de um esboço que utiliza a ideia de script, algo
#   sequencial sem modularização, assim que for alcançado a funcionalidade
#   básica do programa, modularize alguns trechos.

import re

filename = '../compendio1brotero.xml'

output_dir = 'words_in_order'

# TODO:
# como esse script vai servir para mais de um livro,
# pense em outra forma de atribuir o nome ao diretório gerado.
actual_book = 'compendio_de_botanica'

try:
    with open(filename, 'r') as f:
        entire_book = f.read()

        # Iterando de A a Z para ordenar as palavras
        for i in range(ord('a'), ord('z')):
            # Esse regex exige que a palavra seja no mínimo da seguinte forma:
            #   [A-Za-z] _ _ _
            # A palavra deve conter no mínimo 4 letras.
            # Também deve conter um espaço ou quebra de linha após a palavra
            #
            # TODO:
            #   Verifique se a ideia tornar a regex Case-Insensitive é
            #   realmente algo plausível.
            words = re.findall(r"\b%s[a-z]{3,}(?=\s)" % chr(i), entire_book,
                               re.IGNORECASE)

            try:
                # Criando o caminho para o arquivo que será armazenado as
                # palavras com a mesma letra inicial.
                newfile = output_dir + '/' + chr(i) + '.txt'

                with open(newfile, 'w') as letter_text:
                    print(*words, sep='\n', file = letter_text)

            except OSError:
                print("Erro!")

except OSError:
    print("Erro!")

#!/usr/bin/python3

import re

# TODO:
#       Faça um loop para iterar em todas as folhas, textos que são
#       gerados pelo OCR.
filename = 'page.txt'

try:
    with open(filename, 'r') as f:
        text = f.read()

        # TODO:
        #       Não deixe de verificar manualmente as inserções para
        #       corrigir possíveis bugs.

        # Caso comum da finalização de uma sentença, com as letras
        # geralmente minúsculas seguida por um ponto, que logo após o
        # ponto se inicia outra sentença com a primeira letra maiúscula
        text = re.sub(r'(([A-Z]|)[a-z]+\.)\s([A-Z]+)', r'\1</s> \3', text)

        # Procura pelo caso anterior, pois a outra sentença que se inicia
        # precisa de um marcador <s>
        text = re.sub(r'(\.<\/s>\s)(([A-Z]|)[a-z]+)', r'\1 <s>\2', text)

        # Agora procuramos pelos casos mais óbvios, em que o ponto é o
        # último caractere da linha.
        text = re.sub(r'([A-Za-z]\.)$', r'\1</s>', text)


        print(text)

except OSError:
    print("Erro!")

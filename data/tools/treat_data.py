#!/usr/bin/python

import re

from os import listdir

PATHDIR = "../Compendio_Brotero_Vol2/Capítulo_1/"

def get_files(pathdir):
    """
    Montar uma lista com os arquivos transcritos do livro
    """

    files = listdir(pathdir)

    # Procura por arquivos que não são os arquivos de
    # transcrição do livro.
    for i in files:
        if re.search(r'[0-9]+.txt', i) is None:
            files.remove(i)

    return files

def treat_spaces(page_text):
    """
    Remove espaços mal inseridos no final de linha,
    entre parênteses, espaços a mais e etc.
    """


    # Removendo os espaços a mais á direita...
    page_text = re.sub(r'([A-Za-z]+)[ ]+\)',
                       r'\1)',
                       page_text)
    # E á esquerda.
    page_text = re.sub(r'\([ ]+([A-Za-z]+)',
                       r'(\1',
                       page_text)

    # TODO:
    # Os caracteres null, "æ", "ª", "º" e "œ" são problemáticos.
    # Como o regex pode pegá-los?
    #
    # Entre duas palavras ou letras não pode
    # haver mais de um caractere de espaçamento
    page_text = re.sub(r'([a-zõ])[ ]+([A-Za-z])',
                       r'\1 \2',
                       page_text)

    return page_text

def main():
    files = get_files(PATHDIR)

    for file in files:
        target_file = PATHDIR + file

        with open(target_file, 'r') as f:
            entire_text = f.read()
            text = treat_spaces(entire_text)

        with open(target_file, 'w') as new_file:
            print(text, file = new_file)

if __name__ == "__main__":
    main()

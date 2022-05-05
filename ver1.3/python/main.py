import streamlit as st
import requests as req
import re
from fuzzywuzzy import process
from pyngrok import ngrok



from funcoes.api_passaport import *
from funcoes.api_nome import *
from funcoes.validar_passaporte import *
from funcoes.validar_nome import *
from funcoes.regez import *
from funcoes.link import *
from funcoes.split import *
from funcoes.test import *


def main():
    print(teste())
    # input_passaporte = st.text_input('Passaporte')
    # input_nome = st.text_input('Nome Completo')
    input_passaporte = 'BRA999999999'
    input_nome = 'JoAO CARLOS'

    country = split_country(input_passaporte)
    input_passporte = split_passport(input_passaporte)

    print(country)
    print(input_passporte)

    lista_passaporte = api_passaport()
    lista_nome = api_nome()

    lista_passaporte= regexlist(lista_passaporte)
    # print(lista_passaporte)
    # print(lista_nome)


    # input_passaporte = re.sub('\D', '', input_passaporte)
    #st.button("Verificar")
    if True:
        valid_passa(input_passaporte,lista_passaporte)
        valid_nome(input_nome,lista_passaporte)




if __name__ == '__main__':
    main()
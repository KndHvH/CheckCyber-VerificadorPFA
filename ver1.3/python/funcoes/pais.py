def separacao_pais(input_passaporte):
    pais = re.findall("\D", input_passaporte)
    lista = []
    for i in pais:
      lista.append(i)
    return pais
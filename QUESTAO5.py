'''
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

'''
#declaração da string que será invertida
string = "FILOMENA"

#conversão da string para uma lista de caracteres
caracteres = list(string)

#armazena o tamanho da string
tamanho = len(caracteres)

#percorre a metade da string e inverte as posições dos caracteres
for i in range(tamanho // 2):

    caracteres[i], caracteres[tamanho - 1 - i] = caracteres[tamanho - 1 - i], caracteres[i]

#converte a lista de caracteres de volta para uma string
string_invertida = ''.join(caracteres)

#imprime a string invertida
print("String original:", string)
print("String invertida:", string_invertida)
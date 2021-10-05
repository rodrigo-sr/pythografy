import string
import random

letras = string.ascii_letters + string.digits + string.punctuation

# ao invés de criar uma unica lista, foi criada duas listas contendo
# os mesmo caracteres para facilitar a leiitura do código
normal = [le for le in letras]
cript = [lc for lc in letras]

#cria um dicionário criptografado utilizando a base da cifra de césar
def cript_dict(semente):
    random.seed(semente)
    inicio = random.choice(cript)
    indice_selecionado = normal.index(inicio)
    tradutor = dict()
    cont = 0
    for crip in range(len(cript)):
        if indice_selecionado + crip < len(cript):
            tradutor[normal[crip]] = cript[indice_selecionado+crip]
        else:
            tradutor[normal[crip]] = cript[cont]
            cont += 1
    return tradutor

#gerador de senhas
def gera_senha():
    senha = ''
    while len(senha) < 6:
        senha += random.choice(letras)
    
    return senha

def mascara_senha(passw = gera_senha()):
    seeds_list = [random.randint(1,1000) for i in range(len(passw))]
    list_passw = [let for let in passw]
    masked = ''
    for mascara in range(len(passw)):
        dicionario_de_mascara = cript_dict(seeds_list[mascara])
        masked += dicionario_de_mascara[list_passw[mascara]] + '-' +str(seeds_list[mascara]) + '-'
    
    print(seeds_list)
    print(passw)
    print(masked)

mascara_senha()





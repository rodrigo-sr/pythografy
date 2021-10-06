import string
import random
import json

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

#realiza a criptografia da senha
def mascara_senha(passw = gera_senha()):
    seeds_list = [random.randint(1,1000) for i in range(len(passw))]
    list_passw = [let for let in passw]
    masked = ''
    for mascara in range(len(passw)):
        dicionario_de_mascara = cript_dict(seeds_list[mascara])
        masked += dicionario_de_mascara[list_passw[mascara]]
    
    return seeds_list, masked, passw

#faz a descriptografia da senha
def get_pass(seed_list, password):
    descriptografado = ''
    for i in range(len(seed_list)):
        dicionario = cript_dict(seed_list[i])
        desmasc = {x:y for y,x in dicionario.items()}
        descriptografado += desmasc[password[i]]
    return descriptografado


#bloco para iniciar o armazenamento de usuários, e suas respectivas senhas

#adiciona um usuario na base
def add_user(dicionario, usuario):
    dicionario[f'{usuario}'] = f'{usuario}.json'

#atualiza o arquivo de usuarios
def atualizar_usuarios(dicionario_user):
    with open('usuarios.json','w') as atualizar:
        json.dump(dicionario_user, atualizar, indent= 4)


with open('usuarios.json', 'r') as usuarios:
    users = json.load(usuarios)

def add_senha_user(usuario):
    seeds, mascarado, senha = mascara_senha()
    conta = input("Digite a conta/site que deverá ser gerada a senha: ")
    with open(f'usuarios/{usuario}.json', 'r') as ler:
        senha_user = json.load(ler)
    senha_user[f'{conta}'] = (seeds,mascarado,senha)
    with open(f'usuarios/{usuario}.json', 'w') as escrever:
        json.dump(senha_user, escrever, indent= 4)


#funçao para iniciar o processo de verificação da existencia de um usuário
def pergunta_usuario():
    usuario = input("Digite seu nome de usuário: ").lower()

    if usuario in users.keys():
        print('estou aqui')
    else:
        add_user(users, usuario)
        users[f'{usuario}'] = f'{usuario}.json'
        with open(f'usuarios/{usuario}.json', 'a') as arqu:
            pass
        atualizar_usuarios(users)


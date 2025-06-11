from modelo_personagem import Personagem

def validar_categoria(categoria):
        opcoes_categoria = ['CAVALEIRO', 'MAGO', 'ATIRADOR', 'BANDIDO', 'MONSTRO']
        if categoria.upper() in opcoes_categoria:
            return True
        else:
            return False
        

def validar_nome(nome,limite=30):
    if nome.replace(" ", "").isalpha() and len(nome) <= limite:
            return True
    else:
        return False


def validar_idade(idade,minimo = 0):
    try:
        idade_int = int(idade)
        if minimo <= idade_int:
            return True
        else:
             return False
    except ValueError:
         return False
    

def validar_grupo(grupo):
    opcoes_grupo = ['Clã', 'Guilda', 'Facção', 'Bando', 'Aliança', 'Independente']
    if grupo in opcoes_grupo:
        return True
    else:
        return False

def validar_nome_grupo(nome_grupo, limite=25):
    if nome_grupo.replace(" ", "").isalpha() and len(nome_grupo) <= limite:
        return True
    else:
        return False

def validar_raca(raca):
    opcoes_raca = ['Humano', 'Elfo', 'Anão', 'Orc', 'Monstro']
    if raca in opcoes_raca:
        return True
    else:
        return False




     
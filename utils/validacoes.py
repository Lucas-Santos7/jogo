from ..models.modelo_personagem import Personagem

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

def validar_aparencia(cabelo, cor_cabelo, cor_olho, cor_pele, deficiencia, acessorio, formato_rosto, peso, altura, vestimenta):
    opcoes_cabelo = ['Curto', 'Longo', 'Careca', 'Trançado', 'Cacheado', 'Liso']
    opcoes_cor_cabelo = ['Preto', 'Castanho', 'Loiro', 'Ruivo', 'Branco', 'Colorido']
    opcoes_cor_olho = ['Castanho', 'Azul', 'Verde', 'Preto', 'Cinza', 'Vermelho']
    opcoes_cor_pele = ['Clara', 'Morena', 'Negra', 'Parda', 'Verde', 'Azul']
    opcoes_deficiencia = [
        'Nenhuma',
        'Amputado do braço',
        'Amputado da perna',
        'Amputado de ambos os braços',
        'Amputado de ambas as pernas'
    ]
    opcoes_acessorio = ['Nenhum', 'Óculos', 'Chapéu', 'Brinco', 'Máscara']
    opcoes_formato_rosto = ['Oval', 'Redondo', 'Quadrado', 'Triangular']
    opcoes_vestimenta = ['Armadura', 'Roupas comuns', 'Túnica', 'Traje de gala']

    if cabelo not in opcoes_cabelo:
        return False
    if cor_cabelo not in opcoes_cor_cabelo:
        return False
    if cor_olho not in opcoes_cor_olho:
        return False
    if cor_pele not in opcoes_cor_pele:
        return False
    if deficiencia not in opcoes_deficiencia:
        return False
    if acessorio not in opcoes_acessorio:
        return False
    if formato_rosto not in opcoes_formato_rosto:
        return False
    if not (1 <= peso <= 500):  # Peso em kg
        return False
    if not (0.1 <= altura <= 5.0):  # Altura em metros
        return False
    if vestimenta not in opcoes_vestimenta:
        return False

    return True


def validar_historia(passado, familia, amor, presente, min_len=10, max_len=1000):
    campos = [passado, familia, amor, presente]
    for campo in campos:
        if not isinstance(campo, str):
            return False
        if not (min_len <= len(campo.strip()) <= max_len):
            return False
    return True

     
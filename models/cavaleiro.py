from modelo_personagem import Personagem


def escolha_personagem(self, categoria):
    pass

def identidade(self,nome,idade,grupo,raca):
        pass

def aparencia(self,cabelo,cor_cabelo,cor_olho,cor_pele,deficiencia,acessorio,formato_rosto,peso,altura,vestimenta):
        pass

def historia(self,passado,familia,amor,presente):
        pass

def skills(self, espada, escudo, lanca, porrete):
    opcoes_espada = ['Curta', 'Longa', 'Bastarda']
    opcoes_escudo = ['Madeira', 'Ferro', 'Torre']
    opcoes_lanca = ['Curta', 'Longa']
    opcoes_porrete = ['Leve', 'Pesado']

    if espada not in opcoes_espada:
        return False
    if escudo not in opcoes_escudo:
        return False
    if lanca not in opcoes_lanca:
        return False
    if porrete not in opcoes_porrete:
        return False
    return True

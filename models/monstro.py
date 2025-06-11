from modelo_personagem import Personagem


def escolha_personagem(self, categoria):
    pass

def identidade(self,nome,idade,grupo,raca):
        pass

def aparencia(self,cabelo,cor_cabelo,cor_olho,cor_pele,deficiencia,acessorio,formato_rosto,peso,altura,vestimenta):
        pass

def historia(self,passado,familia,amor,presente):
        pass

def skills(self, arma_geral, elmo_capacete_geral, armadura):
    opcoes_arma_geral = ['Garras', 'Presas', 'Cauda', 'Chifres', 'Fogo', 'Ácido']
    opcoes_elmo_capacete_geral = ['Nenhum', 'Ósseo', 'Couro', 'Metálico']
    opcoes_armadura = ['Escamas', 'Pele grossa', 'Carapaça', 'Nenhuma']

    if arma_geral not in opcoes_arma_geral:
        return False
    if elmo_capacete_geral not in opcoes_elmo_capacete_geral:
        return False
    if armadura not in opcoes_armadura:
        return False
    return True
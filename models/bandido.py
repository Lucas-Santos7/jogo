from modelo_personagem import Personagem


def escolha_personagem(self, categoria):
    pass

def identidade(self,nome,idade,grupo,raca):
        pass

def aparencia(self,cabelo,cor_cabelo,cor_olho,cor_pele,deficiencia,acessorio,formato_rosto,peso,altura,vestimenta):
        pass

def historia(self,passado,familia,amor,presente):
        pass


def skills(self, arma_branca, utilitarios):
    opcoes_arma_branca = ['Adaga', 'Faca', 'Espada curta', 'Porrete']
    opcoes_utilitarios = ['Corda', 'Chave mestra', 'Fumaça', 'Poção', 'Moeda falsa']

    if arma_branca not in opcoes_arma_branca:
        return False
    if utilitarios not in opcoes_utilitarios:
        return False
    return True
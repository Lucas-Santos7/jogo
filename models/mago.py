from modelo_personagem import Personagem


def escolha_personagem(self, categoria):
    pass

def identidade(self,nome,idade,grupo,raca):
        pass

def aparencia(self,cabelo,cor_cabelo,cor_olho,cor_pele,deficiencia,acessorio,formato_rosto,peso,altura,vestimenta):
        pass

def historia(self,passado,familia,amor,presente):
        pass

def skills(self, utilitarios, magias, arma_branca, escudinho):
    opcoes_utilitarios = ['Poção', 'Pergaminho', 'Cristal', 'Livro']
    opcoes_magias = ['Fogo', 'Gelo', 'Raio', 'Cura', 'Ilusão']
    opcoes_arma_branca = ['Adaga', 'Cajado', 'Espada curta']
    opcoes_escudinho = ['Mágico', 'Madeira', 'Nenhum']

    if utilitarios not in opcoes_utilitarios:
        return False
    if magias not in opcoes_magias:
        return False
    if arma_branca not in opcoes_arma_branca:
        return False
    if escudinho not in opcoes_escudinho:
        return False
    return True
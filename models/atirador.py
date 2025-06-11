from modelo_personagem import Personagem


def escolha_personagem(self, categoria):
    pass

def identidade(self,nome,idade,grupo,raca):
        pass

def aparencia(self,cabelo,cor_cabelo,cor_olho,cor_pele,deficiencia,acessorio,formato_rosto,peso,altura,vestimenta):
        pass

def historia(self,passado,familia,amor,presente):
        pass

def skills(self, arma, mira, utilitarios):
    opcoes_arma = ['Arco', 'Besta', 'Arma de fogo', 'Estilingue']
    opcoes_mira = ['Óptica', 'Laser', 'Ferro', 'Nenhuma']
    opcoes_utilitarios = ['Flecha explosiva', 'Flecha venenosa', 'Granada', 'Corda', 'Binóculo']

    if arma not in opcoes_arma:
        return False
    if mira not in opcoes_mira:
        return False
    if utilitarios not in opcoes_utilitarios:
        return False
    return True
    
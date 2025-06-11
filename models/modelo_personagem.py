
from abc import ABC, abstractmethod
class Personagem(ABC):
    def escolha_personagem(self,categoria):
        pass
    
    def identidade(self,nome,idade,grupo,raca):
        pass

    def aparencia(self,cabelo,cor_cabelo,cor_olho,cor_pele,deficiencia,acessorio,formato_rosto,peso,altura,vestimenta):
        pass

    def historia(self,passado,familia,amigos,amor,presente):
        pass

    @abstractmethod
    def skills(self):
        pass

    @abstractmethod
    def ataque(self):
        pass

    @abstractmethod
    def defesa(self):
        pass

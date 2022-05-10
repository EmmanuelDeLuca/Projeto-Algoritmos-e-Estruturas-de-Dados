class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
    def __repr__(self) -> str:
        return(f'{self.esquerda and self.esquerda.chave} <- {self.chave} -> {self.direita and self.direita.chave}')

    def insere(raiz, nodo):
        if raiz is None:
            raiz = nodo
        elif raiz.chave < nodo.chave:
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                insere(raiz.direita, nodo)
        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                insere(raiz.esquerda, nodo)
    def busca(raiz, chave):
        if raiz is None:
            return None
        if raiz.chave == chave:
            return raiz
        if raiz.chave < chave:
            return busca(raiz.direita, chave)
        return busca(raiz.esquerda, chave)

#Arvores binaria de busca
# Notação: se y.chave <= x.chave -> A esquerda. se y.chave >= x.chave -> A direita
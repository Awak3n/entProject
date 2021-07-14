class Tipo():
    def __init__(self, e, n, t, j):
        self.e = e
        self.n = n
        self.t = t
        self.j = j
        self.tipo = f'{getLetra(e,0)}{getLetra(n,1)}{getLetra(t,2)}{getLetra(j,3)}'
        self.porcentagem = 0.00


def perguntaInt(pergunta):
    pergunta = pergunta.__add__(" ")
    param = input(pergunta)
    while type(param) is not int:
        try:
            param = int(param)
            if param > 100 or param < 0:
                raise
        except:
            print("\nPRECISA SER UM VALOR ENTRE 0 E 100!")
            param = input(pergunta)
    return param

def getLetra(valor, posicao):
    if posicao == 0:
        return "E" if valor else "I"
    if posicao == 1:
        return "N" if valor else "S"
    if posicao == 2:
        return "T" if valor else "F"
    if posicao == 3:
        return "J" if valor else "P"

def getCarac(valor, a, b):
    return a if valor > 49 else b

def getPorc(valor, caracter):
    return (valor*0.01 if caracter else (100 - valor)*0.01)

tipos = [
    Tipo(False,False,False,False),
    Tipo(False,False,False,True),
    Tipo(False,False,True,False),
    Tipo(False,False,True,True),
    Tipo(False,True,False,False),
    Tipo(False,True,False,True),
    Tipo(False,True,True,False),
    Tipo(False,True,True,True),
    Tipo(True,False,False,False),
    Tipo(True,False,False,True),
    Tipo(True,False,True,False),
    Tipo(True,False,True,True),
    Tipo(True,True,False,False),
    Tipo(True,True,False,True),
    Tipo(True,True,True,False),
    Tipo(True,True,True,True),
]

def calculaTipos(ei,ns,tf,jp):
    global tipos
    for tipo in tipos:
        tipo.porcentagem = getPorc(ei,tipo.e) * getPorc(ns,tipo.n) * getPorc(tf,tipo.t) * getPorc(jp,tipo.j) * 100

if __name__ == '__main__':
    print('Bem-vindo ao ENTProject!')
    ei = perguntaInt('\nQuantos % extrovertido (E) você é?')
    ns = perguntaInt('\nQuantos % intuitivo (N) você é?')
    tf = perguntaInt('\nQuantos % lógico (T) você é?')
    jp = perguntaInt('\nQuantos % julgador (J) você é?')
    print(f'\nTu é um {getCarac(ei,"E","I")}{getCarac(ns,"N","S")}{getCarac(tf,"T","F")}{getCarac(jp,"J","P")} com as seguintes porcentagens:')
    calculaTipos(ei,ns,tf,jp)
    for tipo in tipos:
        print(f'{tipo.tipo}: {round(tipo.porcentagem, 2)}%')


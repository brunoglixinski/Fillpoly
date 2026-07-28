import numpy as np

# Define um ponto recebendo suas coordenadas x e y.
class ponto:
    def __init__ (self, x, y):
        self.x = float(x)
        self.y = float(y)

# Definição das arestas
class aresta:

    # Construtor da aresta a partir de dois pontos
    def __init__ (self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        # Chama a função para calcular os parâmetros da aresta
        self.defAresta()
    
    # Define os parâmetros da aresta necessários para o código
    def defAresta(self):
        # Se a aresta for horizontal:
        if self.p1.y == self.p2.y:
            self.horizontal = True
            self.ymin = self.p1.y
            self.ymax = self.p2.y
            self.xatual = self.p1.x
            self.m = 0.0

        # Caso não seja, trata qual é o y mínimo entre os dois
        else:
            self.horizontal = False
            if self.p1.y < self.p2.y:
                self.ymin = self.p1.y
                self.ymax = self.p2.y
                self.xatual = self.p1.x
                self.m = (self.p2.x - self.p1.x) / (self.p2.y - self.p1.y)
            elif self.p2.y < self.p1.y:
                self.ymin = self.p2.y
                self.ymax = self.p1.y
                self.xatual = self.p2.x
                self.m = (self.p2.x - self.p1.x) / (self.p2.y - self.p1.y)

    # Aqui define o avanço do x
    def avancaScanline(self):
        self.xatual += self.m

# Função pra criação da tabela de arestas
def criaTabAresta(vertices):

    # Cria dicionário vazio
    ta = {}

    for i in range(len(vertices)):

        # Instancia um objeto aresta em uma variável temporária 'a'
        a = aresta(vertices[i], vertices[(i + 1) % len(vertices)])

        # Verifica se não é horizontal, caso sim, ignora
        if a.horizontal == True:
            continue
        else:

            # A chave do dicionário vai ser o ymin da aresta
            chave = int(a.ymin)

            # Verifica a existência desse ymin no dicionário, se não tiver, cria essa chave
            if not chave in ta:
                ta[chave] = []


            # Coloca a aresta no dicionário com a chave sendo o ymin
            ta[chave].append(a)

    # Ordena as arestas de cada chave ymin pelo menor 'xatual'
    for ymin in ta:
        ta[ymin].sort(key=lambda item: item.xatual)
        
    return ta  # Retorna o dicionário

def preenchePoligono (ta):
    comeco = int(min(ta.keys()))
    final = int(max(a.ymax for lista in ta.values() for a in lista))

    aet = []

    for y in range(comeco, final):
        # Adiciona as arestas que "nascem" na scanline y
        if y in ta:
            aet.extend(ta[y])

        # Remove as arestas que já chegaram ao fim (ymax <= y)
        aet = [a for a in aet if a.ymax > y]

        # Ordena a AET pelo menor xatual
        aet.sort(key=lambda a: a.xatual)

        for i in range(0, len(aet), 2):
            # Pega os dois pontos da aresta
            a1 = aet[i]
            a2 = aet[i + 1]

            # Preenche o polígono entre os dois pontos
            x1 = int(a1.xatual)
            x2 = int(a2.xatual)

            for x in range(x1, x2):
                yield (x, y)
                
        # Atualiza o xatual de todas as arestas vivas para a linha y + 1
        for a in aet:
            a.avancaScanline()
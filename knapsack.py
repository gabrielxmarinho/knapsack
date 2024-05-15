#Problema da Mochila
#Variáveis Reais
filename = "knapsack.txt"
f = open(filename, 'r')
conteudo = f.read().split("\n")
n = int(conteudo[0])
c = conteudo[1].split(" ") # coeficientes da Função Objetivo
w = conteudo[2].split(" ") # coeficientes da Condição
M = conteudo[3].split(" ") # Limites superiores
m = conteudo[4].split(" ") # Limites inferiores
W= float(conteudo[5])

def Knapsack(n,c,w,M,m,W):
    #Disponibilidade do Peso a ser balanceado
    Disponivel = W
    X=[]
    #Inicio as variáveis com seu valor mínimo
    for i in range(0,n):
        X.append(float(m[i]))
    rendimentos = []
    #Calculando os Rendimentos
    for i in range(0,n):
        rendimentos.append(int(c[i])/int(w[i]))
    rendimentosOrdenados = sorted(rendimentos,reverse=True)
    indice = None
    # "indice" foi criada pois os rendimentos de 2 variáveis distintas pode ser o mesmo valor
    for rendimento in rendimentosOrdenados:
        for j in range(0,n):
            if rendimentos[j] == rendimento and j != indice:
                qtdMaiorRendimento = Disponivel / float(w[j])
                if qtdMaiorRendimento > float(M[j]):
                    qtdMaiorRendimento = float(M[j])
                Disponivel = Disponivel - float(w[j]) * qtdMaiorRendimento
                X[j] = qtdMaiorRendimento
                indice = j
                break
    return X

#Main
print(Knapsack(n,c,w,M,m,W))
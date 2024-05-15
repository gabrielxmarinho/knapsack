import knapsack
import math
#Branch And Bound
#Variáveis Inteiras
filename = "knapsack.txt"
f = open(filename, 'r')
conteudo = f.read().split("\n")
n = int(conteudo[0])
c = conteudo[1].split(" ") # coeficientes da Função Objetivo
w = conteudo[2].split(" ") # coeficientes da Condição
M = conteudo[3].split(" ") # Limites superiores
m = conteudo[4].split(" ") # Limites inferiores
W = float(conteudo[5])

def branchAndBoundKnapsack(n,c,w,M,m,W,X):
    if all(int(x) == float(x) for x in X):
        return X
    else:
        rendimentos = []
        #Rendimentos na Ordem
        for i in range(0, n):
            rendimentos.append(float(c[i]) / float(w[i]))
        #Rendimentos Ordenandos de Forma Decrescente
        rendimentosOrdenados = sorted(rendimentos, reverse=True)
        Disponivel = W
        for i in range(0,n):
            for j in range(0,n):
                if rendimentos[j]==rendimentosOrdenados[i] and int(X[j])!=float(X[j]):
                    Xpiso = X.copy()
                    Xpiso[j] = math.floor(X[j])
                    Xteto = X.copy()
                    Xteto[j] = math.ceil(X[j])
                    DisponivelPiso = W
                    #Fazendo para o piso:
                    for k in range(0,n):
                        DisponivelPiso = DisponivelPiso - float(w[k])*Xpiso[k]
                    DisponivelTeto = W
                    #Fazendo para o teto:
                    for k in range(0, n):
                        DisponivelTeto = DisponivelTeto - float(w[k]) * Xteto[k]
                    if Xteto[j]>float(M[j]):
                        X=Xpiso
                    else:
                        X=Xteto
                    break
                elif rendimentos[j]==rendimentosOrdenados[i]:
                    break
        
            # Dá para melhorar?
            while(Disponivel - float(w[j])*X[j]>0 and X[j]<float(M[j])):
                X[j]+=1
            #Corrigindo caso passe do limite
            if Disponivel - float(w[j])*X[j]<0 or X[j]>float(M[j]):
                X[j]=X[j] - 1
                X[j] = int(X[j])
            Disponivel = Disponivel - float(w[j])*X[j]

        return X
#Main
print(branchAndBoundKnapsack(n,c,w,M,m,W,knapsack.Knapsack(n,c,w,M,m,W)))
class Perceptron:

    def __init__(self):
        pass

    def __init__(self, entradas_p, alpha_p, theta_p):
        self.conjunto_treinamento = entradas_p
        self.alpha = alpha_p
        self.theta = theta_p

    def passo_zero(self):
        self.pesos = []
        for i in range(len(self.conjunto_treinamento[0][0])):
            self.pesos.append(0)

    def passo_n(self):
        self.passo_zero()
        epoca = 0
        while (True):
            for ct in self.conjunto_treinamento:
                entrada = list(ct[0])
                saida = ct[1]
                saida_y = 0
                # print(entrada, saida, saida_y)
                for j in range(len(self.pesos)):
                    saida_y += entrada[j] * self.pesos[j]
                saida_y = self.f_saida(saida_y, self.theta)
                # print(saida_y)
                p_old = list(self.pesos)
                if(saida_y != saida):
                    for i in range(len(self.pesos)):
                        self.pesos[i] = self.pesos[i] + entrada[i] * self.alpha * saida
            epoca += 1
            if (p_old == self.pesos and epoca != 1):
                break
        return self.pesos

    def f_saida(self, saida_y, theta):
        if (saida_y > theta):
            return 1
        elif (saida_y > -theta and saida_y < theta):
            return 0
        elif (saida_y < -theta):
            return -1
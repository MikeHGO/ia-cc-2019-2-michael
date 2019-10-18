class Hebb:

    def __init__(self):
        pass

    def __init__(self, entradas_p):
        self.conjunto_treinamento = entradas_p

    def passo_zero(self):
        self.pesos = []
        for i in range(len(self.conjunto_treinamento[0][0])):
            self.pesos.append(0)

    def passo_n(self):
        self.passo_zero()
        for ct in self.conjunto_treinamento:
            entrada = list(ct[0])
            saida = ct[1]
            for i in range(len(self.pesos)):
                self.pesos[i] = self.pesos[i] + entrada[i] * saida
        return self.pesos
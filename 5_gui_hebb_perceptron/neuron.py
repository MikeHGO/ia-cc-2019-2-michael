class Neuron:
    def __init__(self):
        pass

    def p_saida(self, t_entradas, theta):
        saida_y = 0.0
        for j in range(len(self.lista_pesos)):
            saida_y += t_entradas[j] * self.lista_pesos[j]
        if (saida_y > theta):
            return 1
        elif (saida_y > -theta and saida_y < theta):
            return 0
        elif (saida_y < -theta):
            return -1

    def h_saida(self, t_entradas):
        saida_y = 0.0
        for j in range(len(self.lista_pesos)):
            saida_y += t_entradas[j] * self.lista_pesos[j]
        if (saida_y > 0):
            return 1
        elif (saida_y < 0):
            return -1

# net somatorio xi wi
#hebb if theta > 0 = 1 elif theta < 0 -1
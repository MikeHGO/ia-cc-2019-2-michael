class Neuron:
    def __init__(self):
        pass

    def p_saida(self, t_entradas, theta):
        saida_y = sum(t_entradas) + sum(self.lista_pesos)
        if (saida_y > theta):
            return 1
        elif (saida_y > -theta and saida_y < theta):
            return 0
        elif (saida_y < -theta):
            return -1

    def h_saida(self, t_entradas):
        saida_y = sum(t_entradas) + sum(self.lista_pesos)
        if (saida_y > 0):
            return 1
        elif (saida_y < 0):
            return -1

# net somatorio xi wi
#hebb if theta > 0 = 1 elif theta < 0 -1
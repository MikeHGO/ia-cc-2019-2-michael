class Neutron:
    def __init__(self):
        pass

    def __init__(self, pesos):
        self.lista_pesos = pesos


    def net(self, entradas):
        return sum(entradas) + sum(self.lista_pesos)




# net somatorio xi wi
#hebb if theta > 0 = 1 elif theta < 0 -1
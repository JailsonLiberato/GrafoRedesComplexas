from constants import Constants


class Main:
    """Classe principal da execução do problema"""

    def __init__(self):
        self.__array_rede_small_world = []
        self.__array_rede_erdos = []
        self.__array_rede_barabasi_albert = []

    def execute(self):
        for n in Constants.N_ARRAY:
            for p in Constants.P_ARRAY:
                self.__array_rede_small_world.append(self.__executeSmallWorld(n, p))
                self.__array_rede_erdos.append(self.__executeErdos(n, p))
                self.__array_rede_barabasi_albert(self.__executeBarabasiAlbert(n, p))
        self.__gerar_arquivo()
        self.__plot_graficos()

    def __execute_small_world(self, n, p):
        pass

    def __execute_erdos(self, n, p):
        pass

    def __execute_barabasi_albert(self, n, p):
        pass

    def __gerar_arquivo(self):
        pass

    def __plot_graficos(self):
        pass


main = Main()
main.execute()

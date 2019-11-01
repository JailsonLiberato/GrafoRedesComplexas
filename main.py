from constants import Constants
import networkx as nx
import numpy as np


class Main:
    """Classe principal da execução do problema"""

    def __init__(self):
        self.__array_rede_small_world = []
        self.__array_rede_erdos = []
        self.__array_rede_barabasi_albert = []
        self.__seed = 42

    def execute(self):
        counter = 1
        for n in Constants.N_ARRAY:
            for p in Constants.P_ARRAY:
                print("### ", counter, "###")
                self.__array_rede_small_world.append(self.__execute_small_world(n, p))
                self.__array_rede_erdos.append(self.__execute_erdos(n, p))
                self.__array_rede_barabasi_albert.append(self.__execute_barabasi_albert(n, p))
                counter = counter + 1
                print("\n")
        self.__gerar_arquivo()
        self.__plot_graficos()

    def __execute_small_world(self, n, p):
        print("\n[Small World]")
        k = 2 # Cada nó está conectado aos k vizinhos mais próximos na topologia em anel.
        ws = nx.watts_strogatz_graph(n, k, p, self.__seed)
        degree_sequence = list(ws.degree())
        self.__calculate_properties(degree_sequence)

    def __execute_erdos(self, n, p):
        print("\n[Erdos]")
        er = nx.erdos_renyi_graph(n, p)
        degree_sequence = list(er.degree())
        self.__calculate_properties(degree_sequence)

    @staticmethod
    def __calculate_properties(degree_sequence):
        avg_degree = np.mean(np.array(degree_sequence)[:, 1])
        med_degree = np.median(np.array(degree_sequence)[:, 1])
        max_degree = max(np.array(degree_sequence)[:, 1])
        min_degree = np.min(np.array(degree_sequence)[:, 1])
        print("Média: ", avg_degree)
        print("Mediana", med_degree)
        print("Máxima", max_degree)
        print("Mínima", min_degree)

    def __execute_barabasi_albert(self, n, p):
        m = 3 # Número de arestas a serem anexadas de um novo nó aos nós existentes
        print("\n[Barabasi Albert]")
        q = (1 - p) - 0.000000000001
        ba = nx.extended_barabasi_albert_graph(n, m, p, q, seed=self.__seed)
        degree_sequence = list(ba.degree())
        self.__calculate_properties(degree_sequence)

    def __gerar_arquivo(self):
        pass

    def __plot_graficos(self):
        pass


main = Main()
main.execute()

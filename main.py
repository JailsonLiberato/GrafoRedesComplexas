from constants import Constants
import networkx as nx
import numpy as np
from rede import Rede
from type_network import TypeNetwork
from plot_chart import PlotChart


class Main:
    """Classe principal da execução do problema"""

    def __init__(self):
        self.__array_rede_small_world = []
        self.__array_rede_erdos = []
        self.__array_rede_barabasi_albert = []
        self.__seed = 42
        #self.__carregar_dados()
        self.__load_file()
        self.__plt_charts = PlotChart()

    def __carregar_dados(self):
        """Carrega os dados """
        for n in Constants.N_ARRAY:
            for p in Constants.P_ARRAY:
                self.__array_rede_small_world.append(self.__execute_small_world(n, p))
                self.__array_rede_erdos.append(self.__execute_erdos(n, p))
                self.__array_rede_barabasi_albert.append(self.__execute_barabasi_albert(n, p))
        self.__gerar_arquivo()

    def execute(self):
        self.__plt_charts.generate_table_dataframe(self.__array_rede_small_world)
        self.__plt_charts.generate_table_dataframe(self.__array_rede_erdos)
        self.__plt_charts.generate_table_dataframe(self.__array_rede_barabasi_albert)
       # self.__plt_charts.generate_bar_chart(self.__array_rede_small_world, self.__array_rede_erdos, self.__array_rede_barabasi_albert)
        print("\n\n\n\t### Fim da aplicação...")

    def __execute_small_world(self, n, p):
        """Executa a função Small World."""
        k = 2  # Cada nó está conectado aos k vizinhos mais próximos na topologia em anel.
        ws = nx.watts_strogatz_graph(n, k, p, self.__seed)
        degree_sequence = list(ws.degree())
        return self.__calculate_properties(degree_sequence, TypeNetwork.SMALL_WORLDS)

    def __execute_erdos(self, n, p):
        """Executa a função Erdos."""
        er = nx.erdos_renyi_graph(n, p)
        degree_sequence = list(er.degree())
        return self.__calculate_properties(degree_sequence, TypeNetwork.ERDOS)

    def __execute_barabasi_albert(self, n, p):
        """Executa a função Barabasi Albert."""
        m = 3  # Número de arestas a serem anexadas de um novo nó aos nós existentes
        q = (1 - p) - 0.000000000001
        ba = nx.extended_barabasi_albert_graph(n, m, p, q, seed=self.__seed)
        degree_sequence = list(ba.degree())
        return self.__calculate_properties(degree_sequence, TypeNetwork.ALBERT_BARABASI)

    def __calculate_properties(self, degree_sequence, type_network: TypeNetwork):
        """Calcula as propriedades."""
        avg_degree = np.mean(np.array(degree_sequence)[:, 1])
        med_degree = np.median(np.array(degree_sequence)[:, 1])
        max_degree = max(np.array(degree_sequence)[:, 1])
        min_degree = np.min(np.array(degree_sequence)[:, 1])
        rede = Rede(type_network, avg_degree, med_degree, max_degree, min_degree)
        return rede

    def __gerar_arquivo(self):
        """"Gera o arquivo de dados."""
        try:
            file = open("arquivo", "w")
            self.__gerar_arquivo_tipo(file, TypeNetwork.SMALL_WORLDS)
            self.__gerar_arquivo_tipo(file, TypeNetwork.ERDOS)
            self.__gerar_arquivo_tipo(file, TypeNetwork.ALBERT_BARABASI)
            file.close()
        except FileNotFoundError:
            print("Erro ao criar o arquivo.")

    def __gerar_arquivo_tipo(self, file, type_network):
        """Gera o arquivo com os dados por tipo de rede."""
        file.write(type_network.value)
        file.write("#")
        array = []
        if type_network == TypeNetwork.SMALL_WORLDS:
            array = self.__array_rede_small_world
        elif type_network == TypeNetwork.ERDOS:
            array = self.__array_rede_erdos
        else:
            array = self.__array_rede_barabasi_albert

        for sw in array:
            file.write(str(sw.media))
            file.write("_")
            file.write(str(sw.mediana))
            file.write("_")
            file.write(str(sw.maxima))
            file.write("_")
            file.write(str(sw.minima))
            file.write("|")
        file.write("\n")

    def __load_file(self):
        """Carrega o arquivo de dados e seta os valores."""
        try:
            file = open("arquivo", "r")
            array = file.readlines()
            if not self.__array_rede_small_world or not self.__array_rede_erdos or not self.__array_rede_barabasi_albert:
                for function_array in array:
                    type_network = function_array.split("#")[0]
                    if TypeNetwork.SMALL_WORLDS.value == type_network:
                        self.__set_values(function_array, type_network, self.__array_rede_small_world)
                    elif TypeNetwork.ERDOS.value == type_network:
                        self.__set_values(function_array, type_network, self.__array_rede_erdos)
                    else:
                        self.__set_values(function_array, type_network, self.__array_rede_barabasi_albert)
                file.close()
        except FileNotFoundError:
            print("Arquivo não existente.")

    def __set_values(self, function_array, type_network, array):
        """Seta os valores nos arrays de acordo com a rede."""
        for element in function_array.split("#")[1].split("|"):
            if element != '\n':
                rede = Rede(type_network,
                             float(element.split("_")[0]),
                             float(element.split("_")[1]),
                             float(element.split("_")[2]),
                             float(element.split("_")[3]))
                array.append(rede)


main = Main()
main.execute()

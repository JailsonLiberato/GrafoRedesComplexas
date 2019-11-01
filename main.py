from constants import Constants
import networkx as nx
import numpy as np
from rede import Rede
from type_network import TypeNetwork
import matplotlib.pyplot as plt

class Main:
    """Classe principal da execução do problema"""

    def __init__(self):
        self.__array_rede_small_world = []
        self.__array_rede_erdos = []
        self.__array_rede_barabasi_albert = []
        self.__seed = 42

    #def execute(self):
     #   self.__plot_graficos()

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
        #self.__load_file()
        self.__plot_graficos()
        print("\n\n\n\t### Fim da aplicação...")

    def __execute_small_world(self, n, p):
        k = 2  # Cada nó está conectado aos k vizinhos mais próximos na topologia em anel.
        ws = nx.watts_strogatz_graph(n, k, p, self.__seed)
        degree_sequence = list(ws.degree())
        return self.__calculate_properties(degree_sequence, TypeNetwork.SMALL_WORLDS)

    def __execute_erdos(self, n, p):
        er = nx.erdos_renyi_graph(n, p)
        degree_sequence = list(er.degree())
        return self.__calculate_properties(degree_sequence, TypeNetwork.ERDOS)

    def __execute_barabasi_albert(self, n, p):
        m = 3  # Número de arestas a serem anexadas de um novo nó aos nós existentes
        q = (1 - p) - 0.000000000001
        ba = nx.extended_barabasi_albert_graph(n, m, p, q, seed=self.__seed)
        degree_sequence = list(ba.degree())
        return self.__calculate_properties(degree_sequence, TypeNetwork.ALBERT_BARABASI)

    def __calculate_properties(self, degree_sequence, type_network: TypeNetwork):
        avg_degree = np.mean(np.array(degree_sequence)[:, 1])
        med_degree = np.median(np.array(degree_sequence)[:, 1])
        max_degree = max(np.array(degree_sequence)[:, 1])
        min_degree = np.min(np.array(degree_sequence)[:, 1])
        rede = Rede(type_network, avg_degree, med_degree, max_degree, min_degree)
        return rede

    def __gerar_arquivo(self):
        try:
            file = open("arquivo", "w")
            self.__gerar_arquivo_tipo(file, TypeNetwork.SMALL_WORLDS)
            self.__gerar_arquivo_tipo(file, TypeNetwork.ERDOS)
            self.__gerar_arquivo_tipo(file, TypeNetwork.ALBERT_BARABASI)
            file.close()
        except FileNotFoundError:
            print("Erro ao criar o arquivo.")

    def __gerar_arquivo_tipo(self, file, type_network):
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
        try:
            file = open("arquivo", "r")
            array = file.readlines()
            if not self.__array_rede_small_world or not self.__array_rede_erdos or not self.__array_rede_barabasi_albert:
                for function_array in array:
                    type_network
                    if TypeNetwork.SMALL_WORLDS.value == function_array.split("#")[0]:
                        type_network = TypeNetwork.SMALL_WORLDS
                        for element in function_array.split("#")[1].split("|"):
                            rede = Rede(type_network,
                                        element.split("_")[0],
                                        element.split("_")[1],
                                        element.split("_")[2],
                                        element.split("_")[3])
                            self.__array_rede_small_world.append(rede)
                    elif TypeNetwork.ERDOS.value == function_array.split("#")[0]:
                        type_network = TypeNetwork.ERDOS
                        for element in function_array.split("#")[1].split("|"):
                            rede = Rede(type_network,
                                        element.split("_")[0],
                                        element.split("_")[1],
                                        element.split("_")[2],
                                        element.split("_")[3])
                            self.__array_rede_erdos.append(rede)
                    else:
                        type_network = TypeNetwork.ALBERT_BARABASI
                        for element in function_array.split("#")[1].split("|"):
                            rede = Rede(type_network,
                                        element.split("_")[0],
                                        element.split("_")[1],
                                        element.split("_")[2],
                                        element.split("_")[3])
                            self.__array_rede_barabasi_albert.append(rede)
                file.close()
        except FileNotFoundError:
            print("Arquivo não existente.")

    def __plot_graficos(self):

        medias = []
        medianas = []
        maximos = []
        minimos = []

        media = []
        mediana = []
        maxima = []
        minima = []
        for med in self.__array_rede_small_world:
            media.append(med.media)
            mediana.append(med.mediana)
            maxima.append(med.maxima)
            minima.append(med.minima)
        medias.append(np.average(media))
        medianas.append(np.median(mediana))
        maximos.append(np.amax(maxima))
        minimos.append(np.amin(minima))

        media = []
        mediana = []
        maxima = []
        minima = []
        for med in self.__array_rede_small_world:
            media.append(med.media)
            mediana.append(med.mediana)
            maxima.append(med.maxima)
            minima.append(med.minima)
        medias.append( np.average( media ) )
        medianas.append( np.median( mediana ) )
        maximos.append( np.max( maxima ) )
        minimos.append( np.min( minima ) )

        media = []
        mediana = []
        maxima = []
        minima = []
        for med in self.__array_rede_small_world:
            media.append(med.media)
            mediana.append(med.mediana)
            maxima.append(med.maxima)
            minima.append(med.minima)
        medias.append( np.average( media ) )
        medianas.append( np.median( mediana ) )
        maximos.append( np.max( maxima ) )
        minimos.append( np.min( minima ) )


        bar_width = 0.25

        r1 = np.arange(len(medias))
        r2 = [x + bar_width for x in r1]
        r3 = [x + bar_width for x in r2]
        r4 = [x + bar_width for x in r3]


        plt.figure(figsize=(10, 5))
        plt.bar(r1, medias, color='#6A5ACD', width=bar_width, label='Média')
        plt.bar(r2, medianas, color='#FFF000', width=bar_width, label='Mediana')
        plt.bar(r3, maximos, color='#6495ED', width=bar_width, label='Máximo')
        plt.bar(r4, minimos, color='#00BFFF', width=bar_width, label='Mínimo')
        plt.ylabel("Valores")
        plt.xlabel("Funções")
        plt.xticks([r + bar_width for r in range(len(medias))], ['SMALL WORLDS', 'ERDOS', 'ALBERT BARABASI'])
        plt.title("Ciência de Redes")
        plt.legend()
        plt.show()


main = Main()
main.execute()

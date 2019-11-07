import matplotlib.pyplot as plt
import numpy as np
from rede import Rede
import pandas as pd
from pandas.plotting import table
from constants import Constants


class PlotChart:
    """Classe de geração de gráficos de análise das redes."""

    def generate_bar_chart(self, small_world_array, erdos_array, albert_barabasi_array):
        for x in range(len(Constants.N_ARRAY)):
            array_rede1 = np.zeros((4, len(Constants.P_ARRAY)))
            array_rede2 = np.zeros((4, len(Constants.P_ARRAY)))
            array_rede3 = np.zeros((4, len(Constants.P_ARRAY)))
            for y in range(len(Constants.P_ARRAY)):
                rede1 = small_world_array[(x*y) + y]
                rede2 = erdos_array[(x*y) + y]
                rede3 = albert_barabasi_array[(x*y) + y]
                array_rede1[0][y] = rede1.media
                array_rede2[0][y] = rede2.media
                array_rede3[0][y] = rede3.media
                array_rede1[1][y] = rede1.mediana
                array_rede2[1][y] = rede2.mediana
                array_rede3[1][y] = rede3.mediana
                array_rede1[2][y] = rede1.maxima
                array_rede2[2][y] = rede2.maxima
                array_rede3[2][y] = rede3.maxima
                array_rede1[3][y] = rede1.minima
                array_rede2[3][y] = rede2.minima
                array_rede3[3][y] = rede3.minima
            self.__configure_bar_chart(array_rede1, array_rede2, array_rede3, str(Constants.N_ARRAY[x]))

    def __configure_bar_chart(self, small_world_array, erdos_array, albert_barabasi_array, n_name):
        bar_width = 0.25

        for i in range(4):
            # set height of bar
            bars1 = small_world_array[i].tolist()
            bars2 = erdos_array[i].tolist()
            bars3 = albert_barabasi_array[i].tolist()
            
            # Set position of bar on X axis
            r1 = np.arange(len(bars1))
            r2 = [x + bar_width for x in r1]
            r3 = [x + bar_width for x in r2]
            # Make the plot
            plt.figure(figsize=(18.0, 12.0))
            title = self.__get_title_metric(i) + " " + n_name
            ax = plt.subplot(111, frame_on=False)  # no visible frame
            ax.set_title(title, fontdict={'fontsize': 15, 'fontweight': 'medium'})
            plt.bar(r1, bars1, color='r', width=bar_width, edgecolor='white', label='SmallWorlds')
            plt.bar(r2, bars2, color='b', width=bar_width, edgecolor='white', label='Erdos')
            plt.bar(r3, bars3, color='g', width=bar_width, edgecolor='white', label='Barabasi')
            
            # Add xticks on the middle of the group bars
            plt.xlabel('Probabilidades', fontweight='bold')
            plt.xticks([r + bar_width for r in range(len(bars1))], Constants.P_ARRAY)
            plt.legend()
            plt.savefig('charts/' + title + '.png')
            plt.close()

    @staticmethod
    def __get_title_metric(index_metric):
        if index_metric == 0:
            return "Media"
        elif index_metric == 1:
            return "Mediana"
        elif index_metric == 2:
            return "Maxima"
        else:
            return "Minima"

    @staticmethod
    def generate_table_dataframe(array: Rede):
        """Gera a tabela o resumo dos dados."""
        medias = []
        medianas = []
        maxs = []
        mins = []
        size = len(array)
        for rede in array:
            medias.append(rede.media)
            medianas.append(rede.mediana)
            maxs.append(rede.maxima)
            mins.append(rede.minima)
        title = array[0].type
        medias = np.array(medias).reshape(1, size).T
        medianas = np.array(medianas).reshape(1, size).T
        maxs = np.array(maxs).reshape(1, size).T
        mins = np.array(mins).reshape(1, size).T
        data = np.concatenate((medias, medianas, maxs, mins), axis=1)
        df = pd.DataFrame(data, columns=['Média', 'Mediana', 'Max', 'Min'])
        df.to_csv(r'table/table_summary' + " " + title + ".csv")

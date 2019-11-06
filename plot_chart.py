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
            array_rede1 = [][]
            array_rede2 = [][]
            array_rede3 = [][]
            for y in range(len(Constants.P_ARRAY)):
                rede1 = small_world_array[(x*y) + y]
                rede2 = erdos_array[(x*y) + y]
                rede3 = albert_barabasi_array[(x*y) + y]
                array_rede1.append(rede1.media, axis=0)
                array_rede2.append(rede2.media, axis=0)
                array_rede3.append(rede3.media, axis=0)
                array_rede1.append(rede1.mediana, axis=1)
                array_rede2.append(rede2.mediana, axis=1)
                array_rede3.append(rede3.mediana, axis=1)
                array_rede1.append(rede1.maxima, axis=2)
                array_rede2.append(rede2.maxima, axis=2)
                array_rede3.append(rede3.maxima, axis=2)
                array_rede1.append(rede1.minima, axis=3)
                array_rede2.append(rede2.minima, axis=3)
                array_rede3.append(rede3.minima, axis=3)
            self.__configure_bar_chart(array_rede1, array_rede2, array_rede3, str(Constants.N_ARRAY[x]))
    

    def __configure_bar_chart(self, small_world_array, erdos_array, albert_barabasi_array, n_name):
        barWidth = 0.25

        for i in range(4):
            # set height of bar
            bars1 = small_world_array[i]
            bars2 = erdos_array[i]
            bars3 = albert_barabasi_array[i]
            
            # Set position of bar on X axis
            r1 = np.arange(len(bars1))
            r2 = [x + barWidth for x in r1]
            r3 = [x + barWidth for x in r2]
            
            # Make the plot
            plt.bar(r1, bars1, color='r', width=barWidth, edgecolor='white', label='SmallWorlds')
            plt.bar(r2, bars2, color='b', width=barWidth, edgecolor='white', label='Erdos')
            plt.bar(r3, bars3, color='g', width=barWidth, edgecolor='white', label='Barabasi')
            
            # Add xticks on the middle of the group bars
            plt.xlabel('Probabilidades', fontweight='bold')
            plt.xticks([r + barWidth for r in range(len(bars1))], Constants.P_ARRAY)
            plt.ylim(0, 5)
            ax = plt.subplot(111, frame_on=False)  # no visible frame
            title = self.__get_title_metric(i) + n_name
            ax.set_title(title, fontdict={'fontsize': 15, 'fontweight': 'medium'})
            plt.legend()


            plt.savefig(title + '.png')
            plt.close()

    def __get_title_metric(index_metric):
        if(index_metric == 0):
            return "Media"
        elif(index_metric == 1):
            return "Mediana"
        elif(index_metric == 2):
            return "Maxima"
        else:
            return "Minima"


    def generate_table_dataframe(self, array: Rede):
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
        ax = plt.subplot(111, frame_on=False)  # no visible frame
        ax.set_title(title, fontdict={'fontsize': 15, 'fontweight': 'medium'})
        ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        ax.xaxis.set_visible(False)  # hide the x axis
        ax.yaxis.set_visible(False)  # hide the y axis
        plt.savefig('table summary' + title + '.png')
        plt.close()

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
            array_rede1 = []
            array_rede2 = []
            array_rede3 = []
            for y in range(len(Constants.P_ARRAY)):
                rede1 = small_world_array[(x*y) + y]
                rede2 = erdos_array[(x*y) + y]
                rede3 = albert_barabasi_array[(x*y) + y]
                array_rede1.append(rede1.media)
                array_rede2.append(rede2.media)
                array_rede3.append(rede3.media)
            self.__configure_bar_chart(array_rede1, array_rede2, array_rede3, str(Constants.N_ARRAY[x]))
    
    def __autolabel(self, rects, ax):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    def __configure_bar_chart(self, small_world_array, erdos_array, albert_barabasi_array, n_name):
        # set width of bar
        barWidth = 0.25
        
        # set height of bar
        bars1 = small_world_array
        bars2 = erdos_array
        bars3 = albert_barabasi_array
        
        # Set position of bar on X axis
        r1 = np.arange(len(bars1))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]
        
        # Make the plot
        plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='SmallWorlds')
        plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='Erdos')
        plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='Barabasi')
        
        # Add xticks on the middle of the group bars
        plt.xlabel('Probability', fontweight='bold')
        plt.xticks([r + barWidth for r in range(len(Constants.P_ARRAY))], Constants.P_ARRAY)
        
        # Create legend & Show graphic
        plt.legend()


        plt.savefig(n_name + '.png')
        plt.close()

    def generate_line_chart(self, array1, array2, array3):
        for x in range(len(Constants.N_ARRAY)):
            array_rede1 = []
            array_rede2 = []
            array_rede3 = []
            for y in range(len(Constants.P_ARRAY)):
                rede1 = array1[(x*y) + y]
                rede2 = array2[(x*y) + y]
                rede3 = array3[(x*y) + y]
                array_rede1.append(rede1.media)
                array_rede2.append(rede2.media)
                array_rede3.append(rede3.media)
            plt.plot(array_rede1, Constants.P_ARRAY)
            plt.plot(array_rede2, Constants.P_ARRAY)
            plt.plot(array_rede3, Constants.P_ARRAY)
            plt.legend(['Small Worlds', 'Erdos', 'Albert Barabasi'], loc='upper left')
            plt.savefig(str(x + 1) + '.png')
            plt.close()

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

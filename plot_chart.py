import matplotlib.pyplot as plt
import numpy as np
from rede import Rede
import pandas as pd
from pandas.plotting import table
from constants import Constants


class PlotChart:
    """Classe de geração de gráficos de análise das redes."""

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
            plt.plot(array_rede1)
            plt.plot(array_rede2)
            plt.plot(array_rede3)
            plt.legend(['Small Worlds', 'Erdos', 'Albert Barabasi'], loc='upper left')
            plt.savefig(str(x + 1) + '.png')
            plt.close()

    def generate_table_dataframe(self, array: Rede):
        """Gera a tabela o resumo dos dados."""
        medias = []
        medianas = []
        maxs = []
        mins = []
        size: int = len(array)
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

import matplotlib.pyplot as plt
import numpy as np
from rede import Rede
import pandas as pd
from pandas.table.plotting import table


class PlotChart:
    """Classe de geração de gráficos de análise das redes."""

    def generate_bar_chart(self):
        pass

    def generate_table_dataframe(self, array:Rede):
        medias = []
        medianas = []
        maxs = []
        mins = []
        for rede in array:
            medias.append(rede.media)
            medianas.append(rede.mediana)
            maxs.append(rede.max)
            mins.append(rede.min)
        data = [medias, medianas, maxs, mins] 
        df = pd.DataFrame(data, columns = ['Média', 'Mediana', 'Max','Min'])
        ax = plt.subplot(111, frame_on=False) # no visible frame
        ax.xaxis.set_visible(False)  # hide the x axis
        ax.yaxis.set_visible(False)  # hide the y axis

        table(ax, df)  # where df is your data frame

        plt.savefig('mytable.png') 
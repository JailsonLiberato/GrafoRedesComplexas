import matplotlib.pyplot as plt
import numpy as np
from rede import Rede


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
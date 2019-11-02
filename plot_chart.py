import matplotlib.pyplot as plt


class PlotChart:
    """Classe de geração de gráficos de análise das redes."""

    def generate_bar_chart(self):
        """Plota os gráficos de acordos com os dados."""
        medias = []
        medianas = []
        maximos = []
        minimos = []

        media = []
        mediana = []
        maxima = []
        minima = []
        for med in self.__array_rede_small_world:
            media.append( med.media )
            mediana.append( med.mediana )
            maxima.append( med.maxima )
            minima.append( med.minima )
        medias.append( np.average( media ) )
        medianas.append( np.median( mediana ) )
        maximos.append( np.amax( maxima ) )
        minimos.append( np.amin( minima ) )

        media = []
        mediana = []
        maxima = []
        minima = []
        for med in self.__array_rede_small_world:
            media.append( med.media )
            mediana.append( med.mediana )
            maxima.append( med.maxima )
            minima.append( med.minima )
        medias.append( np.average( media ) )
        medianas.append( np.median( mediana ) )
        maximos.append( np.max( maxima ) )
        minimos.append( np.min( minima ) )

        media = []
        mediana = []
        maxima = []
        minima = []
        for med in self.__array_rede_small_world:
            media.append( med.media )
            mediana.append( med.mediana )
            maxima.append( med.maxima )
            minima.append( med.minima )
        medias.append( np.average( media ) )
        medianas.append( np.median( mediana ) )
        maximos.append( np.max( maxima ) )
        minimos.append( np.min( minima ) )

        bar_width = 0.25

        r1 = np.arange( len( medias ) )
        r2 = [x + bar_width for x in r1]
        r3 = [x + bar_width for x in r2]
        r4 = [x + bar_width for x in r3]

        plt.figure( figsize=(10, 5) )
        plt.bar( r1, medias, color='#6A5ACD', width=bar_width, label='Média' )
        plt.bar( r2, medianas, color='#FFF000', width=bar_width, label='Mediana' )
        plt.bar( r3, maximos, color='#6495ED', width=bar_width, label='Máximo' )
        plt.bar( r4, minimos, color='#00BFFF', width=bar_width, label='Mínimo' )
        plt.ylabel( "Valores" )
        plt.xlabel( "Funções" )
        plt.xticks( [r + bar_width for r in range( len( medias ) )], ['SMALL WORLDS', 'ERDOS', 'ALBERT BARABASI'] )
        plt.title( "Ciência de Redes" )
        plt.legend()
        plt.show()
class Rede:

    def __init__(self, type, avg_degree, med_degree, max_degree, min_degree):
        self.__type = type
        self.__avg_degree = avg_degree
        self.__med_degree = med_degree
        self.__max_degree = max_degree
        self.__min_degree= min_degree

    @property
    def type(self):
        return self.__type

    @property
    def media(self):
        return self.__avg_degree

    @property
    def mediana(self):
        return self.__med_degree

    @property
    def maxima(self):
        return self.__max_degree

    @property
    def minima (self):
        return self.__min_degree

    def __str__(self):
        return "[Type]: ", self.__type, " [Média]: ", self.__avg_degree, " [Mediana]: ", self.__med_degree, \
               " [Máxima]: ", self.__max_degree, " [Mínima]: ", self.__min_degree, "."


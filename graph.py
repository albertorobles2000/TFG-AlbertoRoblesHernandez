import numpy as np
import functions as func

"""
Clase para manejar grafos en formato de lista de enñaces
"""
class Graph:
    """
    Constructor de un grafo
    """
    def __init__(self, data, covid_hashtags):
        self.graph = {}
        self.companias = []
        self.hashtags = []
        for row in data:
            for hashtag in row['hashtags']:
                #Si el hashtag esta relacionado con el covid
                hashtag_key = covid_hashtags.get_key_hashtag(hashtag)
                if(hashtag_key is not None):
                    #Aniadimos la compania al diccionario
                    if(row['company'] not in self.graph):
                        self.companias.append(row['company'])
                        self.graph[row['company']] = {}
                    #Incrementamos en uno el hashtag correspondiente 
                    #de la compania
                    if(hashtag_key in self.graph[row['company']]):
                        self.graph[row['company']][hashtag_key] += 1
                    else:
                        self.hashtags.append(hashtag_key)
                        self.graph[row['company']][hashtag_key] = 1
        self.hashtags = list(set(self.hashtags))
            
    """
    Metodo para generar ficheros en formato lista de enlaces
    """
    def generate_files(self,file):
        num_companias = 0
        #Generamos el fichero para la lista de nodos
        nodes_file = file + '_nodes.csv'
        with open(nodes_file, 'w', encoding='utf-8') as f:
            f.write('Id;label;type\n')
            num_companias = len(self.companias)
            for index,node in enumerate(self.companias):
                f.write(str(index)+';'+node+';'+str(1)+'\n')
            for index,node in enumerate(self.hashtags):
                f.write(str(index+num_companias)+';'+node+';'+str(2)+'\n')

        #Generamos el fichero para la lista de enlaces
        graph_file = file + '_graph.csv'
        with open(graph_file, 'w', encoding='utf-8') as f:
            f.write('Source;Target;Weight\n')
            for index_compania, compania in enumerate(self.companias):
                diccionario_hashtags = self.graph[compania]
                for key_hashtags in diccionario_hashtags:
                    index_hashtag = self.hashtags.index(key_hashtags)+num_companias
                    peso = diccionario_hashtags[key_hashtags]
                    f.write(str(index_compania)+';'+str(index_hashtag)+';'+str(peso)+'\n')


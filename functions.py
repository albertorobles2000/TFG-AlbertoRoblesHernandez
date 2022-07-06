import json
import numpy as np
import get_data_twitter as tw
import get_data_instagram as inst
import constantes as const
from graph import Graph

"""
Esta funcion divide los hashtags en oleadas, sin importar si
los hashtags estan relacionados o no con el Coronavirus
"""
def split_data_in_waves(waves):
    for country in const._PAISES:
        for social_network in const._REDES_SOCIALES:
            raw_data = read_json_file('./data/raw/'+social_network+'_'+country)
            print('Refining '+country+' '+social_network)
            for index,wave in enumerate(waves[country]):
                data = []
                for publication in raw_data:
                    if publication['date']>wave['start']\
                    and publication['date']<wave['end']\
                    and len(publication['hashtags'])>0:
                        data.append(publication)
                write_json_file('./data/refined/'+social_network+'_'+country+'_'+str(index+1)+'.json',data)


"""
Funcion que extrae los datos de Twitter e Instagram, de 
ciertas compañias de italia y españa
y almacena la extraccion en los ficheros correspondientes
"""
def scarp(file_path,social_media,companies,last_date):
    #Limpiamos los ficheros social_media, de Italia como de España
    open(file_path+"_italy", 'w').close()
    open(file_path+"_spain", 'w').close()
    #Extraemos los datos para cada una de las compañías
    for company in companies:
        file_name = None
        if(company['country']=='spain'):
            file_name = file_path + "_spain"
        else:
            file_name = file_path + "_italy"
        
        with open(file_name, 'a', encoding='utf-8') as file:
            data = None
            if(social_media == 'twitter' and company['twitter']!=""):
                data = tw.get_data(company['twitter'],last_date)
            elif(social_media == 'instagram' and company['instagram']!=""):
                data = inst.get_data(company['instagram'],last_date)
            if(data is not None):    
                for row in data:
                    row['company'] = company['company']
                    file.write(json.dumps(row)+'\n')

"""
Funcion que genera todos los grafos de los distintos paises, redes 
sociales y oleadas, y los almacena en los correspondientes ficheros.
"""
def convert_json_2_graph(covid_hashtags):
    #Generamos grafos por red social, pais, y oleada
    for country in const._PAISES:
        for social_network in const._REDES_SOCIALES:
            print('Creating graph for '+country+' '+social_network)
            for index in range(const._NUMERO_DE_OLEADAS):
                json_data = read_json_file('./data/refined/'+social_network+'_'+country+'_'+str(index+1)+'.json')
                print('Creating graph for '+country+' '+social_network+' wave '+ str(index+1))
                grafo = Graph(json_data,covid_hashtags)
                grafo.generate_files('./data/refined/'+social_network+'_'+country+'_'+str(index+1))

    #Generamos grafo por pais y ola
    for index in range(const._NUMERO_DE_OLEADAS):
        print('Creating graph for wave '+str(index+1))
        json_data = []
        for country in const._PAISES:
            for social_network in const._REDES_SOCIALES:
                json_data.extend(read_json_file('./data/refined/'+social_network+'_'+country+'_'+str(index+1)+'.json'))
        grafo = Graph(json_data,covid_hashtags)
        grafo.generate_files('./data/refined/wave_'+str(index+1))
    
    #Generamos grafo generico
    json_data = []
    print('Creating generic Graph')
    for index in range(const._NUMERO_DE_OLEADAS):
        for country in const._PAISES:
            for social_network in const._REDES_SOCIALES:
                json_data.extend(read_json_file('./data/refined/'+social_network+'_'+country+'_'+str(index+1)+'.json'))
    grafo = Graph(json_data,covid_hashtags)
    grafo.generate_files('./data/refined/pandemia')

"""
Funcion que devuelve lee el fichero json "file",
y lo devuele como una lista de diccionarios
"""
def read_json_file(file):
    data = []
    with open(file, 'r', encoding='utf-8') as file:
        for row in file:
            data.append(json.loads(row))
    return data

"""
Funcion que escribe una lista de diccionarios en formato
json, en el fichero "file"
"""
def write_json_file(file,data):
    with open(file, 'w', encoding='utf-8') as f:
        for row in data:
            f.write(json.dumps(row)+'\n')


def get_sort_vectors(dates, values):
    sort_dates = []
    sort_values = []
    indices = np.argsort(dates)
    for i in indices:
        sort_dates.append(dates[i])
        sort_values.append(values[i])
    return sort_dates, sort_values
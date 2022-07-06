
import graficos as graphics
import functions as func
from hashtags import Hashtags


def main(scrap,refine,create_graph):
    #Cargamos las compañias y hashtags que vamos a utilizar
    companies = func.read_json_file("./resources/companies.dat")
    covid_hashtags = Hashtags('./resources/covid_hashtags.dat') 
    waves = func.read_json_file("./resources/waves.dat")

    if(scrap):#Extraemos todos los datos de las redes sociales
        #Leemos las fechas de las oleadas
        start_date = waves[0]['spain'][0]['start']
        func.scarp('./data/raw/twitter','twitter',companies,start_date)
        func.scarp('./data/raw/instagram','instagram',companies,start_date)
    
    if(refine):#Separamos los datos en funcion de las oleadas  
        func.split_data_in_waves(waves[0])
        
    if(create_graph):#Creamos los grafos en un formato que Gephi soporta
        func.convert_json_2_graph(covid_hashtags)

    #Dibujamos las graficas de frecuencias
    graphics.draw_global_frequencies(covid_hashtags)
    graphics.draw_global_covid_frequencies(covid_hashtags)
    

if __name__ == '__main__':
    main(False,True,True)
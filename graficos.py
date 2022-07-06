import functions as func
from matplotlib import pyplot as plt
import constantes as const
import datetime
import numpy as np

def smooth(vector,n):
    new_vector = []
    for i in range(len(vector)):
        iter = n
        if(len(vector)-(i+n)<0):
            iter = len(vector)-i
        valor = 0
        for j in range(i,i+iter):
            valor += vector[j]
        new_vector.append(valor/iter)
    return new_vector    

def complete_vector(first_day,last_day,some_dates,values):
    date = first_day
    dates = []
    new_vector = []
    while(date < last_day):
        dates.append(date)
        indx = -1
        try:
            indx = some_dates.index(date)
        except ValueError:
            pass   
        if(indx==-1):
            new_vector.append(0)
        else:
            new_vector.append(values[indx])
        date += datetime.timedelta(days=1)
    return dates,new_vector


def get_all_covid_frequencies(covid_hashtags):
    data = {}
    for country in const._PAISES:
        for social_network in const._REDES_SOCIALES:
            print('Creating global analisis for '+country+' '+social_network)
            json_data = []
            for index in range(const._NUMERO_DE_OLEADAS):
                json_data.extend(func.read_json_file('./data/refined/'+social_network+'_'+country+'_'+str(index+1)+'.json'))
            dates = []
            for row in json_data:
                for hashtag in row['hashtags']:
                    if covid_hashtags.get_key_hashtag(hashtag) is not None: 
                        dates.append(datetime.datetime.strptime(row['date'][:10],'%Y-%m-%d'))
            unique_dates = list(set(dates))
            unique_dates.sort()
            values = [int(dates.count(date)) for date in unique_dates]

            data[country+"_"+social_network] = [unique_dates,values]

    return data


def draw_global_frequencies(covid_hashtags):
    data = get_all_covid_frequencies(covid_hashtags)
    first_day = datetime.datetime(2020,1,1)
    last_day = datetime.datetime(2022,4,18)
    spain_tw_x,spain_tw_y = complete_vector(first_day,last_day,data['spain_twitter'][0],data['spain_twitter'][1])
    spain_tw_y = smooth(spain_tw_y,7)
    spain_inst_x,spain_inst_y = complete_vector(first_day,last_day,data['spain_instagram'][0],data['spain_instagram'][1])
    spain_inst_y = smooth(spain_inst_y,7)
    italy_tw_x,italy_tw_y = complete_vector(first_day,last_day,data['italy_twitter'][0],data['italy_twitter'][1])
    italy_tw_y = smooth(italy_tw_y,7)
    italy_inst_x,italy_inst_y = complete_vector(first_day,last_day,data['italy_instagram'][0],data['italy_instagram'][1])
    italy_inst_y = smooth(italy_inst_y,7)

    # plot
    plt.plot(spain_tw_x,spain_tw_y,label='Twitter España')
    plt.plot(spain_inst_x,spain_inst_y,label='Instagram España')
    plt.plot(italy_tw_x,italy_tw_y,label='Twitter Italia')
    plt.plot(italy_inst_x,italy_inst_y,label='Instagram Italia')
    plt.gcf().autofmt_xdate()
    plt.xlabel('Tiempo')
    plt.ylabel('Número medio de hashtags diarios')
    plt.grid('on')
    plt.legend(loc='best')
    plt.show()







def get_hashtags_covid_frequencies(covid_hashtags, country):
    json_data = []
    for social_network in const._REDES_SOCIALES:
        for index in range(const._NUMERO_DE_OLEADAS):
            json_data.extend(func.read_json_file('./data/refined/'+social_network+'_'+country+'_'+str(index+1)+'.json'))
    
    dates = []
    values = []
    for row in json_data:
        for hashtag in row['hashtags']:
            key_hashtag = covid_hashtags.get_key_hashtag(hashtag)
            if(key_hashtag is not None):
                dates.append(datetime.datetime.strptime(row['date'][:10],'%Y-%m-%d'))
                values.append(key_hashtag)
        
    result = []         
    unique_values = list(set(values))
    for hashtag in unique_values:
        diccionario = {}
        diccionario['hashtag'] = hashtag
        valores = []
        fechas = []
        for i in range(len(values)):
            if(values[i]==hashtag):
                valores.append(1)
                fechas.append(dates[i])

        unique_dates = list(set(fechas))
        unique_values = []
        for date in unique_dates:
            unique_values.append(0)
            for index, target in enumerate(fechas):
                if(date == target):
                    unique_values[-1]+=valores[index]

        diccionario['dates'],diccionario['values'] = func.get_sort_vectors(unique_dates,unique_values)
        result.append(diccionario)

    return result

    


def draw_global_covid_frequencies(covid_hashtags):
    
    first_day = datetime.datetime(2020,1,1)
    last_day = datetime.datetime(2022,4,18)

    for country in ['spain','italy']:
        data = get_hashtags_covid_frequencies(covid_hashtags,country)
        data = sorted(data, key=lambda x: sum(x['values']), reverse=True)
        for row in data:
                x,y = complete_vector(first_day,last_day,row['dates'],row['values'])
                y = smooth(y,10)
                plt.plot(x,y,label=row['hashtag'])
        plt.gcf().autofmt_xdate()
        plt.xlabel('Tiempo')
        plt.ylabel('Número medio de hashtags diarios')
        plt.title(country)
        plt.grid('on')
        plt.legend(loc='best')
        plt.show()
        plt.close()
    # plot
    
    
    #plt.axvline(x_spain[100], 0, 0.7, label='pyplot vertical line')
    # beautify the x-labels
    
    
    









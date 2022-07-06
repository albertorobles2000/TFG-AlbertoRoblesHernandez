import twint 

"""
Funcion que extrae todos los hashtags de Twitter, dado el id de un usuario, hasta una fecha limite.

La funcion devuelve una lista de diccionarios con la fecha y hashtags de un tweet.
"""
def get_data(user_id,since_date=None):
    #Configuramos la extraccion
    c = twint.Config()
    c.Username = user_id
    c.Store_csv = False
    c.Hide_output = True
    c.Pandas = True
    if(since_date):
        c.Since = since_date
    #Lanzamos la descarga de datos
    twint.run.Search(c)
    #Procesamos el retorno de la funcion
    df = twint.storage.panda.Tweets_df
    listas = df[['date','hashtags']].values.tolist()
    data = []
    for row in listas:
        data.append({
        'date':row[0],
        'hashtags':row[1]
        })
    return data



import instaloader
import credentials
import datetime


"""
Funcion que extrae todos los hashtags de instagarm, 
dado el id de un usuario, hasta una fecha limite.

La funcion devuelve una lista de diccionarios con la fecha y hashtags de un tweet.
"""
def get_data(user_id,since_date=None):
    #Inicializamos Instaloader
    L = instaloader.Instaloader(download_pictures=False, download_videos=False
        , download_video_thumbnails=False)
    L.login(user=credentials.instagram_user,passwd=credentials.instagram_pass)
    #Extraemos los datos
    posts = instaloader.Profile.from_username(L.context, user_id).get_posts()
    #Filtramos y preparamos el retorno de la funcion
    since = datetime.datetime(int(since_date[:4]),int(since_date[5:7]),int(since_date[8:]))
    data = []
    for post in posts:
        if(since<=post.date):
            dic = {
                'date':str(post.date),
                'hashtags':post.caption_hashtags
            }
            data.append(dic)
        else:
            break
    return data


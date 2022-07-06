# Que hace el script
>
>El script ejecuta un pipeline que generará redes bipartitas en un formato
>soportado por Gephi, en ``data/refined``, donde las redes bipartitas
>estaran compuestas por las compañías mas sostenibles durente la pandemia
>de la Covid-19, y los hashtags que estas han publicado sobre el Coronavirus.
>También generará 3 graficas de frecuencia de publicación, general, por las
>compañías españolas y por las compañías italianas.
>
# Como ejecutar el script
>Clonamos el repositorio y accedemos a la raiz del mismo
>    
>``git clone https://github.com/albertorobles2000/TFG-AlbertoRoblesHernandez.git``  
>``cd TFG-AlbertoRoblesHernandez``
>
>Para construir la aplicación lo primero que debe hacer es crear un entorno virtual de python
>Para instalar virtualenv:
>    
>``pip install virtualenv``
>
>Para generar un entorno virtaul
>    
>``virtualenv .venv``
>
>Una vez creado el entorno virtual debemos activarlo
>
>Windows:
>
>``.\.venv\Scripts\activate.bat``
>
>Ubuntu:
>
>``source .venv/bin/activate``
>
>Una vez tenemos el entorno activado vamos a instalar en este todos los módulos necesarios
>
>``pip install -r requirements.txt``
>
>Ya tenemos configurado todo lo necesario para ejecutar el scrip, mediante el comando
>
>``python ./main.py``
>
>El script se encargará de refinar los datos en bruto, de todas las oleadas y redes sociales, de España e Italia, de forma que Gephi acepte dichos ficheros. Además, generará tres gráficas de frecuencia, una global, y otras dos, con los hashtags publicados en España e Italia.

# Configuración por defecto ejecutar el script

>El código ha sido entregado con los datos en bruto, extraídos de las redes sociales. 
>El script se encargará de refinarlos y pasar por todas las fases del procesado
>hasta generar los ficheros que soporta Gephi.
>
>Si deseamos ejecutar también la extracción de datos, debemos:  
>Poner en el fichero credenciales.py, un usuario y contraseña válidos de Instagram, ya que son necesarios para que instaloader realice la extracción de datos.
>A continuación, debemos modificar el archivo main.py, y llamar a la función main, con el argumento scrap a 'True'.

# Código

>El código consta de los diguientes ficheros:
>- **main.py**. Se encarga de llamar de forma ordenada a las distintas funciones que necesitamos para el refinamiento de los datos, así como carga en memoria, los hashtags relacionados con el covid, las distintas oleadas, y las compañías que vamos a estudiar.
>
>- **get_data_instagram.py**. Hace uso del módulo Instaloader, para extraer los datos que necesitemos de cada compañía de Instagram.
>
>- **get_data_twitter.py**. Hace uso del módulo Twint, para extraer los datos que necesitemos de cada compañía de Twitter.
>
>- **functions.py**. Contiene distintas funciones que utilizamos, algunas de ellas son:
>
>   - **split_data_in_waves**. Divide las publicaciones en oleadas
>
>   - **scarp**. Hace uso de get_data_instagram.py y get_data_twitter.py para extraer y agrupar la información correspondiente.
>
>   - **convert_json_2_graph**. Dado un vector de publicaciones, genera un grafo y lo almacena en un fichero
>
>- **graph.py**. Implementa la clase Graph, la cual, aísla el tratamiento de los grafos, en su última etapa, y los almacena en ficheros.
>
>- **hashtag.py**. Implementa la clase Hashtag, la cual nos ayuda a trabajar de forma eficiente con los grupos de hashtags.
>
>- **graficos.py**. Se encarga de generar las gráficas de frecuencias.
>
>- **constantes.py**. Agrupa algunas constantes globales
>
>- **credenciales.py**. Contiene las credenciales de acceso a Instagram.
>
>- **resources/companies.dat**. Agrupa todas las compañías que vamos a estudiar, y sus usuarios en Twitter e Instagram.
>
>- **resources/covid_hashtags.dat**. Agrupa los grupos de hashtags que vamos a estudiar.
>
>- **resources/waves.dat**. Contiene las distintas oleadas con su fecha de inicio y fin, tanto en España como en Italia.

import urllib.request

#Clase que se encarga con obtener el codigo fuente de un sitio web
class Html_import:

    def __init__(self): #Metodo init que inicializa la variable "url" que es la que usaremos para obtener la pagina web
        self.url = " " 
        
    def obtener_html(self): #Metodo que obtiene el codigo fuente en html de la pagina solitada
        self.webUrl = urllib.request.urlopen(self.url)
        self.data = self.webUrl.read()
    
    def imprimir_html(self): #Metodo que imprime el codigo fuente de la pagina solicitada
        print(self.data)

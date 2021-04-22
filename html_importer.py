import urllib.request

class Html_import:

    def __init__(self):
        self.url = " "
        
    def obtener_html(self):
        self.webUrl = urllib.request.urlopen(self.url)
        self.data = self.webUrl.read()
    
    def imprimir_html(self):
        print(self.data)

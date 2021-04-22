import urllib.request
from html_importer import Html_import

print("Ingrese la direccioon de Url")
print("Ejemplo: https://www.google.com")

importar = Html_import()

importar.url = input()

importar.obtener_html()
importar.imprimir_html()
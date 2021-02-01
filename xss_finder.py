import requests
from colorama import (init, Fore, Back,)
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", help="Especificar URL")
parser.add_argument("-p", help="Especificar posible parametro vulnerable")
parser.add_argument("-f", help="Especificar archivo con payloads ")
args = parser.parse_args()
url = args.u
uri = args.p
file2 = args.f

init()
good = Fore.GREEN+""+Back.BLACK+"[+]"+Fore.RESET+Back.RESET
bad = Fore.RED+""+Back.BLACK+"[-]"+Fore.RESET+Back.RESET
fondo = Back.LIGHTRED_EX
fondo1 = Back.LIGHTBLUE_EX
nofondo = Back.RESET

if file2 ==False or url ==False:
    print(f"{good} {fondo}Intentando otro metodo de desbloqueo {nofondo}")
else:
    archivo = open(file2,"r")

def start():
    try:
        x = 0
        print(f"{good} {fondo1}{Fore.WHITE}Iniciando{nofondo}")
        for line in archivo:
            payload = {f"{uri}":f"{line}"}
            request = requests.get(url,params=payload)
            if request.status_code == 200 and line in requests.get(url,params=payload).text:
                print(f"{good} {fondo1} {Fore.WHITE}200 XSS FOUND: {request.url} {nofondo}")
            if request.status_code == 302:
                print(f"{bad} {fondo1}{Fore.WHITE}302 Found {request.url} {nofondo}")
            if request.status_code == 304:
                print(f"{bad} {fondo1}{Fore.WHITE}304 Not Modified {request.url} {nofondo}")    
            if request.status_code == 403:
                print(f"{bad} {fondo1}{Fore.WHITE}403 Forbidden {request.url} {nofondo}")   
            if request.status_code == 404:
                print(f"{bad} {fondo1}{Fore.WHITE}404 Not Found {request.url} {nofondo}")
            if request.status_code == 409:
                print(f"{bad} {fondo1}{Fore.WHITE}409 Conflict {request.url} {nofondo}")
            if request.status_code == 500:
                print(f"{bad} {fondo1}{Fore.WHITE}500 Internal Server Error {request.url} {nofondo}")
            else:
                print(f"{bad} {fondo1}{Fore.WHITE}Al parecer el parametro no existe u ocurrió otro error {nofondo}")
            x = x + 1
    except KeyboardInterrupt:
        print(f"{good} {fondo}Proceso interrumpido {nofondo}")
    except requests.exceptions.MissingSchema:
        print(f"{bad} {fondo}URL invalida {nofondo}")
    except requests.exceptions.ConnectionError:
        print(f"{bad} {fondo}No se pudo conectar al host.{nofondo}")

def credit():
    logo = Fore.RED + """

__   __ _____ _____                 
\ \ / // ____/ ____|                
 \ V /| (___| (___                  
  > <  \___ \\___  \   """ + Back.LIGHTBLUE_EX + Fore.LIGHTGREEN_EX+f"""Cyber Phantom{nofondo}{Fore.RED}               
 / . \ ____) |___) |  _           _ 
/_/ \_\_____/_____/  (_)         (_)
                      ______ ______ 
                     |______|______|
                                         
    
    """
    print(logo)
if __name__ == "__main__":
    credit()
    start()
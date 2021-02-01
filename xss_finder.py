import requests
from colorama import (init, Fore, Back,)
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Especificar URL")
parser.add_argument("-p", "--parametro", help="Especificar posible parametro vulnerable")
parser.add_argument("-f", "--file", help="Especificar archivo con payloads ")
args = parser.parse_args()
url = args.url
uri = args.parametro
file2 = args.file

init()
good = Fore.GREEN+""+Back.BLACK+"[+]"+Fore.RESET+Back.RESET
bad = Fore.RED+""+Back.BLACK+"[-]"+Fore.RESET+Back.RESET
fondo = Back.LIGHTRED_EX
fondo1 = Back.LIGHTBLUE_EX
nofondo = Back.RESET

def start():
    if file2 ==None or url ==None or uri ==None:
        print(f"{good} {fondo}Llena los parametros. {nofondo}")
        parser.print_help()
    else:
        print(f"{good} {fondo1}{Fore.WHITE}Iniciando{nofondo}")
        try:
            x = 0
            if os.path.exists(file2):
                archivo = open(file2,"r")
            else:
                print(f"{bad} {fondo1}{Fore.WHITE}El archivo no existe. {nofondo}")
            for line in archivo:
                payload = {f"{uri}":f"{line}"}
                request = requests.get(url,params=payload)
                if request.status_code == 200 and line in requests.get(url,params=payload).text:
                    print(f"{good} {fondo1} {Fore.WHITE}200 XSS FOUND: {request.url} {nofondo}")
                elif request.status_code == 302:
                    print(f"{bad} {fondo1}{Fore.WHITE}302 Found {request.url} {nofondo}")
                elif request.status_code == 304:
                    print(f"{bad} {fondo1}{Fore.WHITE}304 Not Modified {request.url} {nofondo}")    
                elif request.status_code == 403:
                    print(f"{bad} {fondo1}{Fore.WHITE}403 Forbidden {request.url} {nofondo}")   
                elif request.status_code == 404:
                    print(f"{bad} {fondo1}{Fore.WHITE}404 Not Found {request.url} {nofondo}")
                elif request.status_code == 409:
                    print(f"{bad} {fondo1}{Fore.WHITE}409 Conflict {request.url} {nofondo}")
                elif request.status_code == 500:
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
        except FileNotFoundError:
            print(f"{bad} {fondo1}{Fore.WHITE}El archivo no existe. {nofondo}")
        except UnboundLocalError:
            parser.print_help()

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
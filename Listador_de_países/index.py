import pandas as pd 
import sys

def frm_principal():
	print("listando todos os paises que existem...")
	listar_paises()
	sair_do_programna()
	
def listar_paises():
	abrir_lista_de_paises = pd.read_csv("paises.csv")
	print(abrir_lista_de_paises)

def sair_do_programna():
	press_key = input("Pressione qualquer tecla...")
	
	sys.exit()

frm_principal()
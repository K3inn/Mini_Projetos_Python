
import voz

def principal():
	print("Digite uma frase em inglês")
	dados_digitado_pelo_usuario = input("$ ")
	voz.falar(dados_digitado_pelo_usuario)
	principal()

principal()

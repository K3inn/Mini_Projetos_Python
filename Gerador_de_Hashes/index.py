try:
	import hashlib
except:
	print("Erro")


valor = "Ola mundo"

def gerar_hash(valor):
	sha224_hash = hashlib.sha224()
	sha1_hash = hashlib.sha1()
	sha256_hash = hashlib.sha256()
	md5_hash = hashlib.md5()
	sha384_hash = hashlib.sha384()
	sha512_hash = hashlib.sha512()

	md5_hash.update(valor)
	sha256_hash.update(valor)
	sha1_hash.update(valor)
	sha224_hash.update(valor)
	sha384_hash.update(valor)
	sha512_hash.update(valor)

	print("Valor = Ola mundo\n")
	print("Valor em md5:\n"+md5_hash.hexdigest())
	print("\nValor em sha256:\n"+sha256_hash.hexdigest())
	print("\nValor em sha1:\n"+sha1_hash.hexdigest())
	print("\nValor em sha224:\n"+sha224_hash.hexdigest())
	print("\nValor em sha384:\n"+sha384_hash.hexdigest())
	print("\nValor em sha512:\n"+sha512_hash.hexdigest())

gerar_hash(valor)
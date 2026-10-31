class Animal:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def emitir_som(self):
		pass


class Cachorro(Animal):
	def emitir_som(self):
		print(f"{self.nome}: Au au!")


class Gato(Animal):
	def emitir_som(self):
		print(f"{self.nome}: Miau!")


class Vaca(Animal):
	def emitir_som(self):
		print(f"{self.nome}: Muuu!")


animais = [Cachorro("Rex", 3), Gato("Mimi", 2), Vaca("Mimosa", 5)]

for animal in animais:
	animal.emitir_som()

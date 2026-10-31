from abc import ABC, abstractmethod


class Animal(ABC):
	def __init__(self, nome):
		self.nome = nome


class Andador(ABC):
	@abstractmethod
	def andar(self):
		pass


class Voador(ABC):
	@abstractmethod
	def voar(self):
		pass


class Nadador(ABC):
	@abstractmethod
	def nadar(self):
		pass


class Cachorro(Animal, Andador, Nadador):
	def andar(self):
		print(f"{self.nome} está andando.")

	def nadar(self):
		print(f"{self.nome} está nadando.")


class Peixe(Animal, Nadador):
	def nadar(self):
		print(f"{self.nome} está nadando.")


class Aguia(Animal, Andador, Voador):
	def andar(self):
		print(f"{self.nome} está andando.")

	def voar(self):
		print(f"{self.nome} está voando.")

animais = [Cachorro("Rex"), Peixe("Nemo"), Aguia("Harpia")]

for animal in animais:
	if isinstance(animal, Andador):
		animal.andar()
	if isinstance(animal, Voador):
		animal.voar()
	if isinstance(animal, Nadador):
		animal.nadar()

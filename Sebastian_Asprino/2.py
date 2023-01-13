class Node:
    
	def __init__(self, data):
		## dato en el nodo
		self.data = data

		## siguiente espacio en memoria
		self.next = None

class LinkedList:

	def __init__(self):
		## inicia el puntero en vacio
		self.PTR = None

	def insertar(self, new_node):
		## verifica si el puntero esta vacia
		if self.PTR:
			## obtener ultimo nodo
			last_node = self.PTR
			while last_node.next != None:
				last_node = last_node.next

			## asignar el nuevo nodo al puntero del ultimo
			last_node.next = new_node

		else:
			## el puntero esta vacio
			## asignar nodo al puntero
			self.PTR = new_node

	def consola(self):

		## lee la lista para mostrarla en pantalla
		while self.PTR != None:
			print(self.PTR.data, end='->')

			## se cambia al sgt nodo
			self.PTR = self.PTR.next
        ## no hay mas nodos 
		print('Null')

def main():
	## sin rodeos profesor no se como sumar polinomios :C
	lista1= LinkedList()
	lista2=LinkedList()
	print("de cuando es su polinomio")
	tamaño_polinomio = input()
	while tamaño_polinomio == i:
		lista2.insertar(Node())
		i += 1

	while tamaño_polinomio == i:
		lista2.insertar(Node())
		i += 1





if __name__ == '__main__':
	main()



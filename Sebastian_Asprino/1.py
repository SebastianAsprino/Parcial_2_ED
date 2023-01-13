class Node:
    ## crear nodo
	def __init__(self, data):
		## dato en el nodo
		self.data = data

		## siguiente espacio en memoria
		self.next = None
class LinkedList:
    
    def __init__(self):
        self.PTR = None
    

    def vacio(self):
        ## revisa si la lista circular esta vacia
        return self.PTR is None

    
    def agregar_PTR(self, data):
        ## agregar un nodo antes de primero y este siendo ahora el primero
        nodo = Node(data)
        if self.vacio():
            self.PTR = nodo
            nodo.next = self.PTR
        else:
            nodito = self.PTR
            while nodito.next is not self.PTR:
                nodito = nodito.next
            nodito.next = nodo
            nodo.next   = self.PTR
            self.PTR    = nodo

    def agregar_ULT(self, data):
        ## agregar nodo al final "ULT" y luego este ser el ultimo "ULT"
        nodo = Node(data)
        if self.vacio():
            self.PTR = nodo
            nodo.next = self.PTR
        else:
            nodito = self.PTR
            while nodito.next is not self.PTR:
                nodito = nodito.next
            nodito.next = nodo
            nodo.next = self.PTR

    def pantalla(self):
        ## recorrer la lista circular
        if self.vacio():
            return
        nodito = self.PTR
        print(nodito.data)
        while nodito.next != self.PTR:
            nodito = nodito.next
            print(nodito.data, end='->')



def ordenar_lista(lista):
    ## ordena cada lista 1 y lista 2 cuando se le llama
    if lista.data > lista.next :
        aux = lista.data
        lista.data = lista.next
        lista.next = aux
        return ordenar_lista(lista.next)

def lista (lis1,lis2):
## agrega los datos de lista 3
    lista3 = LinkedList()
    if lis1.data == lis2.data:
        return lista(lis1.next,lis2.next)
    if lis1.data != lis2.data:
        dato = lis1.data 
        lista3.agregar_ULT(dato)
    if lis2.data != lis1.data:
        dato = lis2.data 
        lista3.agregar_ULT(dato)
    return lista3

def ordenar_lista1(lista):
    ## ordena de forma decesendente la lista 3
    if lista.data < lista.next :
        aux = lista.data
        lista.data = lista.next
        lista.next = aux
        return ordenar_lista(lista.next)



def main():

	lista1 = LinkedList()
	lista2 = LinkedList()
    ## lista enlazada 1
	lista1.agregar_ULT(3)
	lista1.agregar_ULT(1)
	lista1.agregar_ULT(2)
    ## lista enlazada 2
	lista2.agregar_ULT(3)
	lista2.agregar_ULT(2)
	lista2.agregar_ULT(1)
    ## ordena la lista 1
	ordenar_lista(lista1)
    ## ordena la lista 2
	ordenar_lista(lista2)
	lista3 = lista(lista1,lista2)
	ordenar_lista1(lista3)
	lista1.pantalla()
	lista2.pantalla()
	lista3.pantalla()



if __name__ == '__main__':
	main()


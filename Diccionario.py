
"""
2.7

No está bien pensada la resolución del ejercicio,
está muy limitado a la eliminación de caracteres y agregar nuevos
para eliminar nos deja sin el principio open close

Su método zplit no cumple con el single-responsability como se menciona en
el pdf.
"""
class Diccionario:
    def __init__(self, y):
        self.y = y  # inicializar cadena

    def zplit(self, deli=" "):
        listafinal = []  # lista vacía
        x1 = 0  # inicio subcadena
        x3 = 0  # fin subcadena

        # mientras no termine
        """
        split()
        """
        while x3 < len(self.y):
            # encontró delimitador
            if self.y[x3: x3 + len(deli)] == deli:
                listafinal.append(self.y[x1:x3])  # añadir palabra
                x1 = x3 + len(deli)  # mover inicio
                x3 += len(deli)  # mover fin
            else:
                x3 += 1  # mover fin
        listafinal.append(self.y[x1:])  # añadir última palabra

        """
        Está muy limitada la cantidad de caracteres que debemos quitar,
        podría ser cualquier texto con muchos caracteres diferentes.
        Y la forma de eliminarlos tampoco es la más eficiente.
        Van a escribir cada caracter existente?
        """
        lnv = '""!?.”:'  # caracteres a quitar
        lfinal1 = []  # lista final 1

        # eliminar caracteres

        for i in listafinal:
            elemnt = ''.join(x for x in i if x not in lnv)
            lfinal1.append(elemnt)  # añadir palabra

        # todo a minúsculas
        """
        Se puede como primer paso convertir la cadena a minúsculas y
        dejamos evitamos una complejidad O(n)
        """
        lfinal2 = [i.lower() for i in lfinal1]
        return lfinal2

    def reps(self, lista):
        """
        En las instrucciones de la tarea se especifica que no se debe usar
        set(), se tenía que implementar su propio algoritmo para eliminar
        los repetidos de una lista
        """
        return list(set(lista))  # eliminar repetidos

class OrdenableIterativoAbstractClass:
    def intercambiar(self, elementos, i, j):
        elementos[i], elementos[j] = elementos[j], elementos[i]  # intercambiar elementos

class BubbleSort(OrdenableIterativoAbstractClass):
    def ordenar(self, elementos):
        # recorrer lista
        for i in range(len(elementos)):
            # comparar elementos
            for j in range(len(elementos)-1):
                # si es mayor
                if elementos[j] > elementos[j+1]:
                    # intercambiar
                    self.intercambiar(elementos, j, j+1)


x = Diccionario("Two blondes were going to Disneyland when they came to a fork in the road. The sign read: ”Disneyland LEFT.” So they went home.")
lista = x.zplit(" ")  # dividir por espacio
y = x.reps(lista)  # eliminar repetidos

"""
Esto debería llamarse dentro de la clase, lo ideal al crear su método
de eliminar repetidos es primero tener la lista ordenada.
"""
bubble = BubbleSort()  # instancia bubblesort
bubble.ordenar(y)  # ordenar lista

print(y)
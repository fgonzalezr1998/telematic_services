#! /usr/bin/env python

class ClientsList():
    def __init__(self):
        self.list_ = []
        self.out_of_range_ex_ = "pop index out of range"

    def add_element(self, str):
        '''
        add element whose name is "str" to the list
        '''

        self.list_.append(str)

    def insert_list(self, list):
        '''
        insert "list" append self.list_
        '''

        self.list_ = self.list_ + list

    def delete_element(self, index):
        '''
        delete element given by index but index starts in 1, not 0
        index: int
        '''
        if(not self.elem_ok_(index)):
            print("Element doesn't exist")
            return
        self.list_.pop(index - 1)

    def go_first_by_index(self, index):
        '''
        one element of list, go to the firt position
        '''
        if(not self.elem_ok_(index - 1)):
            print("Element doesn't exist")
            return

        elem = self.list_.pop(index - 1)
        self.list_.insert(0, elem)

    def go_first_by_name(self, name):
        '''
        element whose name be "name" go first of queue
        '''
        try:
            pos = self.list_.index(name)
            self.go_first_by_index(pos + 1)
            print name, " pasa de la posicion ", pos + 1, " a la 1"
        except ValueError:
            print("Element doesn't exist")


    def change_of_queue(self, clients_list):
        '''
        move people of self.list_ to "list"
        clients_list: ClientsList
        '''
        #COMO PUEDO HACER ESTE METODO MEJOR??
        list_aux = []
        l = len(self.list_)
        for i in range(1, l, 2):
            list_aux.append(self.list_[i])

        clients_list.insert_list(list_aux) #move elements to "list"

        #delete elements of self.list_
        if(self.is_even_(l)):
            init = l - 1
        else:
            init = l - 2

        for i in range(init, 0, -2):
            self.list_.pop(i)

    def reverse(self):
        '''
        reverse self.list_
        '''
        self.list_.reverse()

    def get_list(self):
        return self.list_

    def print_list(self):
        '''
        print full list
        '''
        print(self.list_)

    #*****PRIVATE METHODS******

    def is_even_(self, n):
        return n % 2 == 0

    def elem_ok_(self, index):
        '''
        returns if one element of list exists
        '''
        return index < len(self.list_) and index >= 0

    def delete_all_(self):
        '''
        delete all elements of self.list_
        '''
        self.list_ = []

def add_elems(n, l):
    for i in n:
        l.add_element(i)

def show_report(l):
    for i in l:
        print "Caja con ", len(i.get_list()), "clientes: ", ", ".join(i.get_list())

if __name__ == "__main__":
    #creo las cajas 1 y 2
    caja_1 = ClientsList()
    caja_2 = ClientsList()

    #Anado elementos a las dos cajas
    names = ['Luis', 'Maria', 'Pepe', 'Javier', 'Laura', 'Lorena', 'Sigismundo']
    add_elems(names, caja_1)
    names = ['Alsacia', 'Paco', 'Carolina', 'Fernando']
    add_elems(names, caja_2)

    #Imprimo el contenido de las cajas
    print "caja 1: ",
    caja_1.print_list()
    print "caja 2: ",
    caja_2.print_list()

    #El cliente que ocupa la posicion 6 de la caja_1 abandola la fila
    caja_1.delete_element(6)
    print "caja 1: ",
    caja_1.print_list()

    #El ultimo cliente de la caja 1,lleva poca compra y le dejan ponerse el primero
    caja_1.go_first_by_index(len(caja_1.get_list()))
    print "caja 1: ",
    caja_1.print_list()

    #Se abre la caja 3
    caja_3 = ClientsList()

    #Los clientes de la caja 2 se pasan en orden a la caja 3
    caja_2.change_of_queue(caja_3)

    print "caja 2: ",
    caja_2.print_list()
    print "caja 3: ",
    caja_3.print_list()

    #Se invierte el orden de los clientes de la caja 1
    caja_1.reverse()
    print "caja 1: ",
    caja_1.print_list()

    #Anadimos un cliente llamado Ernesto en la caja 1
    caja_1.add_element('Ernesto')
    #Ernesto ira a la primera posicion
    caja_1.go_first_by_name('Ernesto')

    print "caja 1: ",
    caja_1.print_list()

    #Creamos una lista de cajas
    list = [caja_1, caja_2, caja_3]

    #Mostrar informe de cajas
    show_report(list)

    #Crear lista de strings
    for i in range(0, len(list)):
        list[i] = "; ".join(list[i].get_list())

    print list

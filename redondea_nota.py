#! /usr/bin/env python

class Redondea():
    def __init__(self):

        self.mode_types = ['normal', 'laxo', 'estricto']

    def redondea_nota(self, nota, modo):

        if(not self.mode_ok_(modo)):
            print("Modo Incorrecto")
            return

        if(modo == self.mode_types[0]):
            return nota
        elif(modo == self.mode_types[1]):
            return round(nota)
        else:
            return int(nota)

    def mode_ok_(self, modo):
        return modo in self.mode_types


if __name__ == "__main__":

    redondea = Redondea();

    print(redondea.redondea_nota(4.99, 'laxo'))
    print(redondea.redondea_nota(4.99, 'normal'))
    print(redondea.redondea_nota(4.99, 'estricto'))

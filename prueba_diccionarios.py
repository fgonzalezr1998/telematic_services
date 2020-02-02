#! /usr/bin/env python

class MyDict():

    def __init__(self, map = {}):
        self.map_table_ = map

    def add_element(self, key, value):

        self.map_table_[key] = value

    def delete_value_by_list(self, l):
        '''
        l: list of values we have to delete
        '''

        for i in l:
            for k, v in self.map_table_.items():
                if(isinstance(v, list)):

                    if i in v:
                        v.remove(i)

                else:
                    if(i == v):
                        del self.map_table_[k]

    def delete_by_key(self, key):
        '''
        key: key or keys list whose element we want to delete
        '''
        if(isinstance(key, list)):
            for i in key:
                self.delete_key_(i)
        else:
            self.delete_key_(key)

    def add_value_2_keys(self, keys_list, value):

        '''
        keys_list: list of keys
        value: value to add to dictionary

        '''

        for i in keys_list:

            for k, v in self.map_table_.items():

                if(k == i):
                    if(isinstance(v, list)):
                        v.append(value)

                    else:
                        l = [v, value]

                        self.map_table_[k] = l

    def get_dic(self):

        return self.map_table_

    def print_dic(self):
        sorted_list = sorted(self.map_table_.items())
        for i in sorted_list:
            if(isinstance(i[1], list)):
                print str(i[0]) + ": " + ", ".join(i[1])
            else:
                print str(i[0]) + ": " + str(i[1])

    def delete_key_(self, key):
        try:
            del self.map_table_[key]
        except KeyError:
            pass

if __name__ == "__main__":

    #creo la lista
    dic = MyDict({'valencia': ['unacosa', 'otracosa'], 'Francia': 'cerveza', 'Espana': ['vino', 'Tortilla de patata', 'Jamon']}) #Defino el objeto dic de la clase MyDict

    print(dic.get_dic())

    #anado un elemento
    dic.add_element('Inglaterra', 'Fish & Chips')

    print(dic.get_dic())

    #borro todos los elementos incluidos en la lista 'alcoholicas'
    alcoholicas = ['cerveza', 'vino', 'sidra']

    dic.delete_value_by_list(alcoholicas)

    print(dic.get_dic())

    #Anado el valor 'paella' a cualquiera de las claves incluidas en la lista 'comunidad_valenciana'
    comunidad_valenciana = ['valencia', 'alicante', 'castellon']

    dic.add_value_2_keys(comunidad_valenciana, 'paella')
    print(dic.get_dic())

    #borro los elementos cuyas claves se encuentran en la lista 'comunidad_valenciana'
    dic.delete_by_key(comunidad_valenciana)
    print(dic.get_dic())
    print("-------------")

    dic.print_dic()

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

    def get_dic(self):

        return self.map_table_

if __name__ == "__main__":

    dic = MyDict({'Francia': 'cerveza', 'Espana': ['vino', 'Paella', 'Tortilla de patata', 'Jamon']}) #Defino el objeto dic de la clase MyDict

    print(dic.get_dic())

    dic.add_element('Inglaterra', 'Fish & Chips')

    print(dic.get_dic())

    alcoholicas = ['cerveza', 'vino', 'sidra']

    dic.delete_value_by_list(alcoholicas)

    print(dic.get_dic())

#! /usr/bin/env python

class Ordenar():

    def __init__(self, list):

        self.list_ = list

    def ordenar(self):

        if(not self.list_ok_()):
            raise SystemExit


        self.sort_by_len_()
        list_sorted_by_sum = self.sort_by_sum_()

    def get_list(self):
        return self.list_

    def sort_by_len_(self):

        #l = self.list_
        self.list_.sort(key = lambda s: len(s))


    def sort_by_sum_(self):

        l = []
        list_sum = self.list_sum_()
        list_sum_sorted = sorted(list_sum)

        list_of_index = []
        used_pos = []
        for i in list_sum_sorted:
            pos = 0
            for j in list_sum:
                if(i == j and not (pos in used_pos)):
                    used_pos.append(pos)
                    break
                pos = pos + 1

            list_of_index.append(pos)

        l = []
        for i in list_of_index:
            l.append(self.list_[i])

        self.list_ = l
        return list_sum_sorted

    def list_ok_(self):
        return self.elems_are_lists_() and self.all_numbers_()

    def elems_are_lists_(self):
        for i in self.list_:
            if(not isinstance(i, list)):
                return False

        return True

    def all_numbers_(self):
        for i in self.list_:
            for j in i:
                if(type(j) != int):
                    return False
        return True

    def list_sum_(self):

        l = []
        for i in self.list_:
            sum = 0
            for j in i:
                sum = sum + j
            l.append(sum)
        return l

if __name__ == "__main__":

    l = [[1], [81], [1, 2, 1], [1, 1, 1, 1], [1, 3], [23, 32]]

    ord = Ordenar(l)
    ord.ordenar()
    print(ord.get_list())

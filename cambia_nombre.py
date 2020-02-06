#! /usr/bin/env python

# -*- coding: utf-8 -*-

import os
import sys
import threading

#Consts:
MinArgs = 1

class FolderChanger():
    def __init__(self, folders_list):

        self.folders_list_ = folders_list
        self.threads_list_ = []

        self.lock = threading.Lock()

        self.build_threads_()

    #PUBLIC METHODS

    def change_names(self):
        #start all threards
        for i in self.threads_list_:
            i.start()

        #wait for all threads
        for i in self.threads_list_:
            i.join()

    #PRIVATE METHODS

    def build_threads_(self):

        for i in self.folders_list_:
            th = threading.Thread(target=self.change_names_, args=(i,))
            self.threads_list_.append(th)

    def change_names_(self, path):

        self.lock.acquire()
        list_dir = os.listdir(path)
        self.lock.release()

        for i in list_dir:
            p = path + "/" + i #Complete the path

            #replace spaces:
            name = i.replace(" ", "_")
            #lower chars:
            name = name.lower()
            #replace strange characters
            name = self.replace_strange_chars_(name, ".")
            p_new = path + "/" + name
            #Only rename if file name changed
            if(name != i):
                self.lock.acquire()
                os.rename(p, p_new)
                self.lock.release()

    def thereis_spaces_(self, file_name):

        return file_name.find(" ") != -1

    def replace_strange_chars_(self, file_name, char2replace):
        n = file_name
        for i in file_name:
            if(self.is_strange_char_(i) and i != '_' and i != '.'):
                n = n.replace(i, char2replace)

        return n

    def is_strange_char_(self, c):
        pos = ord(c) #position in ascii table of character 'i'
        return (pos < ord('A') or pos > ord('z')) and
                        (pos < ord('0') or pos > ord('9'))


def folders_ok(folders_list):
    for i in folders_list:
        if(not os.path.isdir(i)):
            return False
    return True

def args_ok():
    if(len(sys.argv) == MinArgs):
        return True

    return folders_ok(sys.argv[1:])


if __name__ == "__main__":

    if(not args_ok()):
        sys.exit("Usage Error\n")

    #Create one thread for each folder
    fc = FolderChanger(sys.argv[1:])

    fc.change_names()

#! /usr/bin/env python

# -*- coding: utf-8 -*-

import os
import sys
import threading
import optparse

#Consts:
MinArgs = 1

class FolderChanger():
    def __init__(self, options, folders_list):

        self.opts_ = options
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

        if(self.opts_.recursive):
            print("Ejecuto recursivo")
            self.change_names_recursive(path)
        else:
            print("Ejecuto No rcursivo")
            self.change_names_no_recursive(path)

    def change_names_recursive(self, path):

        self.lock.acquire()
        list_dir = os.listdir(path)
        self.lock.release()

        for (root,dirs,files) in os.walk(list_dir, topdown=true):
            for i in list_dir:
                self.replace(path, i)

    def change_names_no_recursive(self, path):

        self.lock.acquire()
        list_dir = os.listdir(path)
        self.lock.release()

        for i in list_dir:
            self.replace(path, i)

    def replace(self, path, elem_name):
        '''
        param elem_name: name of file or folder to rename
        '''

        p = path + "/" + elem_name #Complete the path
        name = elem_name
        if(self.opts_received()):
            #replace spaces:
            if(self.opts_.spaces):
                name = name.replace(" ", "_")

            #lower chars:
            if(self.opts_.case):
                name = name.lower()

            #replace strange characters
            if(self.opts_.weird):
                name = self.replace_strange_chars_(name, ".")
        else:
            name = elem_name.replace(" ", "_")
            name = name.lower()
            name = self.replace_strange_chars_(name, ".")

        #Only rename if file name changed
        if(name != elem_name):
            p_new = path + "/" + name
            self.lock.acquire()
            os.rename(p, p_new)
            self.lock.release()


    def opts_received(self):
        finish = False
        for i in self.opts_.__dict__:
            if(self.opts_.__dict__[i] != None):
                finish = True
                break
        return finish

    def thereis_spaces_(self, file_name):

        return file_name.find(" ") != -1

    def replace_strange_chars_(self, file_name, char2replace):
        n = file_name
        for i in file_name:
            if(self.is_strange_char_(i) and i != '_' and i != '.'):
                n = n.replace(i, char2replace)

        return n

    def is_strange_char_(self, c):
        pos = ord(c) #position in ascii table of character 'c'
        return (pos < ord('A') or pos > ord('z')) and \
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

def add_parser_options(parser):

    options_list = ["-r", "--recursive", "-s", "--spaces",
                    "-c", "--case", "-n", "--enne", "-t", "--accent", "-w", "--weird"]
    for i in range(0, len(options_list), 2):
        parser.add_option(options_list[i], options_list[i + 1], action="store_true")

if __name__ == "__main__":

    parser = optparse.OptionParser("Usage: %prog [options] folder [folder1, folder2,...foldern]")

    add_parser_options(parser)
    (options, args) = parser.parse_args()

    #Create one thread for each folder
    if(len(args) == 0):
        args = ['.']

    fc = FolderChanger(options, args)

    fc.change_names()

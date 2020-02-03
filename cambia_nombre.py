#! /usr/bin/env python

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
        '''
        recursive algorithm
        '''
        self.lock.acquire()
        list_dir = os.listdir(path)
        print(list_dir)
        print("\n--------------------\n")
        self.lock.release()

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

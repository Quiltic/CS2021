import os, time, math, numpy

def Quickgit(words = None):
    comit = "git commit"
    if words != None:
        comit += " -m " + words
    os.system("git add .")
    time.sleep(1)
    os.system(comit)
    time.sleep(1)
    os.system("git push")

__author__ = "Josh Zack"
__email__ = "zackjm@mail.uc.edu"

if __name__ == "__main__":
    #Quickgit()
    Quickgit("Added_new_lab")
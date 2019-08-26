import os, time, math, numpy

def Quickgit(words = None):
    comit = "git commit"
    if words != None:
        comit += "-m " + words
    os.system("git add .")
    time.sleep(1)
    os.system(comit)
    time.sleep(1)
    os.system("git push")

if __name__ == "__main__":
    Quickgit()
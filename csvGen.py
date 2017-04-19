import os
import random
import confOpc
nb_tags = 0
freq = 1000

if __name__ == '__main__':
    for i in xrange(nb_tags, nb_tags + 110, 10):
        confopc = confOpc.confOpc(i, "loadAll", freq, "load", "172.23.6.15")
        confopc.printLoads()

import os
import random
import confOpc
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Opc-Ua configurator')
    parser.add_argument('--nb_tags', help='number of tags in the conf to create. Default is 100', type=int, action='store', default=100)
    parser.add_argument('--ip', help='IP adress of the server. Default is 127.0.0.1', type=str, action='store', default='127.0.0.1')
    parser.add_argument('--freq', help='Frequency at which the datapoints should be sent. default is 1000', type=int, action='store', default=1000)
    parser.add_argument('--agg', help='Option to decide to if the generator puts AGG nodes in one subscription, or 0 for une subscription par node', type=int, action='store', default=5)
    
    args = parser.parse_args()
    
    confopc = confOpc.confOpc(args.nb_tags, "loadAll", args.freq, "load", args.ip, args.agg)
    confopc.printLoads()

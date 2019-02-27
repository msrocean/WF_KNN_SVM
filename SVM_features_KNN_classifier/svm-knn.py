#!/usr/bin/python
# <Mohammad Saidur Rahman><mr6564@rit.edu>
# This code was modifed from the original code
# from features extraction code of the cummulative attack to make input file 
# consistent with the different data sets from different defences mechanisms

import os
import numpy
import itertools
import sys

dir = "/home/mr6564/Desktop/WF/experiment/svm-knn/batch/"
from natsort import natsorted
outdir = "/home/mr6564/Desktop/WF/experiment/svm-knn/batch/"


#for class_number in range(100):
filelist = os.listdir(dir)
filelist.sort()
for file_name in filelist:  # class label -= classnumber
    if True:

        try:
            parts = file_name.split('-')
            class_number = int(parts[0])
            instance = int(parts[1])
            #file_name = str(class_number)
            content = open(os.path.join(dir, file_name), "r")
            features = []
            total = []
            cum = []
            pos = []
            neg = []
            inSize = 0
            outSize = 0
            inCount = 0
            outCount = 0
            for line in content:
                parts = line.split("\t")
                timestamp = float(parts[0])
                # packetsize = int(parts[1][:-1]) # check this
                packetsize = int(parts[1])

                #Mohsen: I inverse the packet sizes to be compatible with our definition of incoming and outgoing
                packetsize = -1 * packetsize
                if packetsize > 0:
                    packetsize = +1.0
                else:
                    packetsize = -1.0

                # incoming packets
                if packetsize > 0:
                    inSize += packetsize
                    inCount += 1
                    # cumulated packetsizes
                    if len(cum) == 0:
                        cum.append(packetsize)
                        total.append(packetsize)
                        pos.append(packetsize)
                        neg.append(0)
                    else:
                        cum.append(cum[-1] + packetsize)
                        total.append(total[-1] + abs(packetsize))
                        pos.append(pos[-1] + packetsize)
                        neg.append(neg[-1] + 0)

                if packetsize < 0:
                    outSize += abs(packetsize)
                    outCount += 1
                    if len(cum) == 0:
                        cum.append(packetsize)
                        total.append(abs(packetsize))
                        pos.append(0)
                        neg.append(abs(packetsize))
                    else:

                        cum.append(cum[-1] + packetsize)
                        total.append(total[-1] + abs(packetsize))
                        pos.append(pos[-1] + 0)
                        neg.append(neg[-1] + abs(packetsize))

            # features append 0 for background and 1 for fore ground
                # add feature
            # features.append('1')
            features.append(class_number)
            features.append(inCount)
            features.append(outCount)
            features.append(outSize)
            features.append(inSize)


            # cumulative in one
            temp = []
            temp.append(inCount)
            temp.append(outCount)
            temp.append(outSize)
            temp.append(inSize)


            cumFeatures = numpy.interp(numpy.linspace(total[0], total[-1], 101), total, cum)
            temp.extend(cumFeatures)

            fout = open("/home/mr6564/Desktop/WF/experiment/svm-knn/batch/" + file_name + "f", "w")
            for x in temp:
                fout.write(repr(x) + " ")
            fout.close()
        except: pass
f = open("fdetails", "w")
f.write(str(len(temp)))
print (len(temp))
f.close()

        


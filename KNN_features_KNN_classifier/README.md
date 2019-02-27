Step 01: give the 'batch' folder location to fextractor.py file

Step 02: run python fextractor.py

it will give the number of features.


Step 03: Feed the number of features in flearner.cpp file

Step 04: compile flearner.cpp and run it.

[See the knnresults.txt  for help]



fextractor.py:
Generates feature files from packet sequence files. Packet sequence files are located in batch/ where each line is a time (float),
then, then a positive or negative number (postive: outgoing packet length or cell, negative: incoming packet length or cell).
Feature files are lists of features as defined by fextractor.py.


flearner.cpp:
Learns distance weights and measures accuracy based on the distance weights.

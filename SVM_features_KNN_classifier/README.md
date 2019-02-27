Step 01: give the 'batch' folder location to svm-knn.py file

Step 02: run python svm-knn.py

it will give the number of features.


Step 03: Feed the number of features in flearner.cpp file



Step 04: compile flearner.cpp and run it.

[see the svmknnresult.txt  file for help]



fextractor.py:
Generates feature files from packet sequence files. Packet sequence files are located in batch/ where each line is a time (float),
then \t, then a positive or negative number (postive: outgoing packet length or cell, negative: incoming packet length or cell).
Feature files are lists of features as defined by fextractor.py.


flearner.cpp:
Learns distance weights and measures accuracy based on the distance weights.

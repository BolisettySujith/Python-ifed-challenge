import time
import pandas as pd
import numpy as np

Files = {'SubFile':'subset_elemets.txt','allFile':'all_elements.txt'}

#Opening files using keys of the dictionary 
#Reading the opened files and and splits every word  
sub_file= open(Files.get('SubFile',0)).read().split('\n')
all_file = open(Files.get('allFile',0)).read().split('\n')

#calling time.time() function
start = time.time()

verified_elements=[]

#Finding the same element which is present in both the files
#If a same element is present then appending thet element to empty list
for element in sub_file and all_file:
    verified_elements.append(element)
    print(len(verified_elements))#printing length of the element wich is appended into list

#Measuring how much time taken for both files in seconds 
print('Duration: {} seconds'.format(time.time() - start))
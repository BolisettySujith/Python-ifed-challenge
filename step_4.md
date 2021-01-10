# Time taken for searching same element of string in two files

## steps involved
### step1
> imported the modules(time) required to do the task 
### step 2
>created a dictionary which are having the values as the file names
### step 3
declared a variable for storing the function done below 
> used open() function to open the file 

>used read() function to read the file

> used split() function to split the every word into a single string

### step 4
Calling the time.time() and storing to *start* variable
>The return value is how many seconds have passed between the Unix epoch and the moment time.time() was called.

> created an empty list'verified_elements=[]'

### step 5
> using for loop, looping to both the files and searching for the same element common in both files

>appending the common element to the empty list and printing its length using len() function.

### step 6

printing the time taken to work on the both files ny subtracting present time - start time by using *time.time() - start*

## conclusion
So by this the time taken for searching same element of string in two files caliculated

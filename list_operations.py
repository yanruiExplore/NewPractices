"""
The list_operations module provides functions that works on list

"""


def sum(list_input):
    '''
    Implementation for a sum function to add the numbers in a list and if the number appears as a string type, it will be converted to 
    either an int or a float type and be added as well. 
    If all elements are strings, it will concatenate all the strings.
    '''
    try:
        #check if all elements are strings
        testing = "".join(list_input)  #if it doesn't return an error, return the concatenation of the strings
        y = list_input[0]
        for i in list_input[1:]:
            y = y + i
        return y
    except:
        y = 0
        for i in list_input:
            if isinstance(i, int) == True:
                y = y + i
            elif isinstance(i, float) == True:
                y = y + i

            elif '.' in i:  
                try:
                    y = y + float(i)

                except ValueError:
                    continue
            
            else:
                try:
                    y = y + int(i)
                
                except ValueError:
                    continue

        return y

    

def product_numbers(list_numbers):
    '''
    Implementation of product function to compute product of numbers in a list. Elements that are of string type but can be convereted
    to either an int or float will be converted and included in the product of numbers.
    '''
    new_list = []

    for i in list_numbers:
        if isinstance(i, int) == True or isinstance(i, float) == True:
            new_list.append(i)
        elif '.' in i:  
            try:
                new_list.append(float(i))

            except ValueError:
                continue
            
        else:
            try:
                new_list.append(int(i))
                
            except ValueError:
                continue
    
    if len(new_list) == 0:
        return 0

    elif len(new_list) == 1:
        return new_list[0]

    else:
        y = new_list[0]
        for i in new_list[1:]:
            y = y * i
        
        return y


def factorial(number):
    '''
    A factorial function to compute the factorial of a number
    '''
    y = range(1, number + 1)

    return (product_numbers(y))


    

def filter_digits(list_inputs):
    #Implementation for a function that will filter the digits in a list
    new_list = []

    for i in list_inputs:
        if isinstance(i, int) == True:
            new_list.append(i)
        
        elif isinstance(i, float) == True:
            new_list.append(i)

        elif isinstance(int(i), int) == True:
            new_list.append(int(i))

        elif isinstance(float(i), float) == True:
            new_list.append(float(i))
        
        else:
            continue
    
    return new_list




def reverse_list(list_input):
    '''
    A reverse function to reverse a list
    '''
    length = len(list_input)
    y = []
    for i in range(length):
        y.append(list_input[length - 1])
        length = length - 1
    
    return y
    #using list slicing
    # x[::-1]




def max(a,b):
    if a > b:
        return a
    else:
        return b

def min(a,b):
    if a < b:
        return a
    else:
        return b









def find_max(list1):
    '''
    The find_max function will return the maximum of a given list. If there are strings and int/float elements, it will return the
    value of the int/float that is the highest.
    '''
    list_input = list1[:]  #explicit copy of the input list

    for i in range(len(list_input)-1):

        

        a = list_input[0]
        b = list_input[1]
        try:
            #scenario where comparison is between int and/or float
            if min(a, b) == a:
                list_input.remove(a)
            else:
                list_input.remove(b)
                
        
        except TypeError:
            #print('type error')
            #scenario where one of the compared number is a string and the other is either an int or float
            #this will test whether a or b is the string element
            if isinstance(a, int) == True or isinstance(a, float) == True:  

                if '.' in b:
                    #print('. in b')
                    #this will see if the string b can be converted to a float and proceed with the comparison
                    try:
                        if min(a, float(b)) == float(a):
                            list_input.remove(a)
                            
                        else:
                            list_input.remove(b)
                            
                    except ValueError:
                            list_input.remove(b)
                            
                else:
                    #this will see if the string b can be converted to an int and proceed with the comparison
                    try:
                        if min(a, int(b)) == int(a):
                            list_input.remove(a)
                            
                        else:
                            list_input.remove(b)
                            
                    except ValueError:
                            list_input.remove(b)
                            
            else:
                if '.' in a:
                    #print('. in a')
                    #this will see if the string a can be converted to a float and proceed with the comparison
                    try:
                        if min(float(a), b) == float(a):
                            list_input.remove(a)
                            
                        else:
                            list_input.remove(b)
                            
                    except ValueError:
                            #print('value error')
                            list_input.remove(a)
                            print(list_input)
                else:
                    #this will see if the string b can be converted to an int and proceed with the comparison
                    try:
                        if min(int(a), b) == int(a):
                            list_input.remove(a)
                            
                        else:
                            list_input.remove(b)
                            
                    except ValueError:
                            list_input.remove(a)
                            

    return list_input[0]

    #alternative implementation
    '''
    if max(a,b) == a:
        list_input.remove(b)
    else:
        list_input.remove(a)
    '''









def find_min(list1):
    '''
    The find_min function will return the minimum of a given list. If there are string numbers and int/float elements, it will return the
    value of the int/float that is the lowest.
    '''

    list_input = list(list1)

    for i in range(len(list_input)-1):

        a = list_input[0]
        b = list_input[1]
        try:
            #scenario where comparison is between int and/or float
            if max(a, b) == a:
                list_input.remove(a)
            else:
                list_input.remove(b)
        
        except TypeError:
            #scenario where one of the compared element is a string and the other is either an int or float
            #this will test whether a or b is the string element
            if isinstance(a, int) == True or isinstance(a, float) == True:  

                if '.' in b:
                    #this will see if the string b can be converted to a float and proceed with the comparison
                    try:
                        if max(a, float(b)) == a:
                            list_input.remove(a)
                        else:
                            list_input.remove(b)
                    except ValueError:
                            list_input.remove(b)
                else:
                    #this will see if the string b can be converted to an int and proceed with the comparison
                    try:
                        if max(a, int(b)) == a:
                            list_input.remove(a)
                        else:
                            list_input.remove(b)
                    except ValueError:
                            list_input.remove(b)
            else:
                if '.' in a:
                    #this will see if the string a can be converted to a float and proceed with the comparison
                    try:
                        if max(float(a), b) == a:
                            list_input.remove(a)
                        else:
                            list_input.remove(b)
                    except ValueError:
                            list_input.remove(a)
                else:
                    #this will see if the string b can be converted to an int and proceed with the comparison
                    try:
                        if max(int(a), b) == a:
                            list_input.remove(a)
                        else:
                            list_input.remove(b)
                    except ValueError:
                            list_input.remove(a)

    return list_input[0]

    #alternative implementation
    '''
    if min(a, b) == a:
        list_input.remove(d)
    else:
        list_input.remove(c)
    '''











# How can we implement cumulative_sum to work for string elements in a list?

def cumulative_sum(list_input):
    '''
    A cumulative_sum function that will compute the cumulative sum of the any numbers in a list and generate a list of the results
    Numbers can be of int, float or string type
    '''
    y = []
    z = 0
    for i in range(len(list_input)):
        if isinstance(list_input[i], int) == True or isinstance(list_input[i], float) == True:
            z = z + list_input[i]
        else:
            if '.' in list_input[i]:
                try:
                    z = z + float(list_input[i])
                except ValueError:
                    continue
            else:
                try:
                    z = z + int(list_input[i])
                except ValueError:
                    continue    

        y.append(z)
    
    if len(y) == 0:
        return print('There are no elements that is either an int/float or can be converted to an int/float')
    else:
        return y













def cumulative_product(list_input):
    '''
    A cumulative product function that will compute the cumulative product of the any numbers in a list and add them to a new list
    Numbers can be of int, float or string type
    '''
    y = []
    z = 0
    for i in range(len(list_input)):
        if isinstance(list_input[i], int) == True or isinstance(list_input[i], float) == True:
            #print('True')
            z = z + list_input[i]
            #y.append(z)

            break
        else:
            if '.' in list_input[i]:
                try:
                    z = z + float(list_input[i])
                    #y.append(z)
                    #print('float')
                    break
                except ValueError:
                    continue
            else:
                try:
                    z = z + int(list_input[i])
                    #print('integer')
                    #y.append(z)
                    break
                except ValueError:
                    continue    
    
    #print(z)    
    y.append(z)
    #print(len(y))
    if len(y) == 0:
        return print('There are no elements that is either an int/float or can be converted to an int/float')
    
    for i in range(1, len(list_input)):
        if isinstance(list_input[i], int) == True or isinstance(list_input[i], float) == True:
            z = z*list_input[i]
        else:
            if '.' in list_input[i]:
                try:
                    z = z*float(list_input[i])
                except ValueError:
                    continue
            else:
                try:
                    z = z*int(list_input[i])
                except ValueError:
                    continue    
        y.append(z)

    
    return y











def unique(list_input):
    '''
    A unique function to find all the unique elements in a list and present them in a list
    '''
    y = []
    for i in list_input:
        if i in y:
            continue
        else:
            y.append(i)
    
    y.sort()

    return y

    #alternative implementation
    '''
    return list(set(list_input)).sort()
    '''




def find_dups(list_input):
    '''
    A find_dups function to find the duplicate elements in a list
    '''
    unique = []
    duplicate = []
    for i in list_input:
        if i in unique:
            duplicate.append(i)
        else:
            unique.append(i)
    
    duplicate_filtered = list(set(duplicate)).sort()

    return duplicate_filtered





def group(user_list, size):
    '''
    A group(list,size) function that take a list and splits into smaller lists of given size
    '''
    list_input = list(user_list)
    final_list = []
    Number_of_steps = (len(list_input) // size) + (len(list_input) % size)

    #print(Number_of_steps)   # debugging purposes

    for i in range(Number_of_steps):
        if len(list_input) < size:
            break
        new_list = []
        for i in range(size):
            #print('list length is now: ', len(list_input))
            #debugging purposes
    #       print(i)
    #       print(list_input[i]) #debugging purposes
            new_list.append(list_input[i])
        for i in range(size):
            list_input.remove(list_input[0])
     #      print(list_input)
        final_list.append(new_list)
    
    if len(list_input) != 0:
        final_list.append(list_input)

    return final_list





def lensort(a):
    '''
    A function lensort to sort a list of strings based on length
    '''
    b = list(a).sort(key = lambda x: len(x))

    return b









def unique_key(list1, f):
    '''
    The unique function with an optional key function as argument and use the return value of the key function to check for uniqueness
    '''
    master_list = []
    for element in list1:
        #create a key value pair for the element and the key function result when applied to that element
        #add each of the key value pair to the master list
        internal_list = []
        internal_list.append(element)
        internal_list.append(f(element))
        master_list.append(internal_list)
    
    #stage 2
    #For each of the internal list value, assign them to list2 and apply unique function to it to create a unique list of the values
    list2 = []
    for count in range(len(master_list)):
        list2.append(master_list[count][1])
    
    print(list2)

    unique_list2 = unique(list2)
    return unique_list2   #This should be the answer
    #unique_list2 = set(list2)
    #The element checked using the in operator is faster in sets compared to lists
'''
Stage 3 not necessary

    #stage 3
    final_list1 = []
    for count in range(len(master_list)):
        if master_list[count][1] in unique_list2:
            final_list1.append(master_list[count][0])
    
    final_list2 = unique(final_list1)
    #final_list2 = set(final_list1)

    return final_list2
'''






def extsort(list1):
    '''
    A function extsort to sort a list of files based on extension
    '''

    main_list = []
    for element in list1:
        main_list.append(element.split('.')) 
        #element.split('.') will result in a list with 2 elements, first one will be the file name
        # the second one will be the extension

    main_list.sort(key= lambda x : x[1])

    new_list = []

    for element in main_list:
        new_list.append('.'.join(element))


    return new_list







def zip(list1, list2):
    '''
    Implementation of the zip function using list comprehension
    '''

    return [(x,y) for x in list1 for y in list2 if list1.index(x) == list2.index(y)]



def map(f, list_input):
    '''
    Implementation for function map that applies a function to each element of a list, using list comprehension
    '''

    return [f(x) for x in list_input]



def filter(f, a):
    '''
    Implementation for filter(f, a) that returns items of the list a for which f(item) returns true
    '''

    return [x for x in a if f(x) == True]




def enumerate(input_list):
    '''
    A function enumerate that takes a list and returns a list of tuples containing (index, item) for each item in the list
    '''

    list_length = len(input_list)
    new_list = []
    for i in range(list_length):
        new_tuple = (i, input_list[i])
        new_list.append(new_tuple)
    
    new_list.sort()

    return new_list


def enumerate2(input_list):
    '''
    Alternative implementation using list comprehension.
    '''

    index_length = len(input_list)

    return [(x, y) for x in range(index_length) for y in input_list]  #does not work as it gave all possible combinations of x and y





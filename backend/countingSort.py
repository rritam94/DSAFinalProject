import sys






def str_sort(lst, str_i, maxL):
    if maxL == str_i or len(lst) == 1: # Base case: O(1)
        return lst
    subList = [[] for _ in range(28)]  # for each letter and a space


    for i in range(len(lst)):  # O(len(lst))
        if str_i >= len(lst[i]): #if index out of range
            subList[27].append(lst[i]) #treat it as a space
        else:
            if lst[i][str_i] == ',':  # char a comma, append to 27th spot
                subList[26].append(lst[i])
            elif lst[i][str_i] == ' ':  # char a space, append to 28th spot
                subList[27].append(lst[i])
            elif 'a' <= lst[i][str_i] <= 'z':  # Only process lowercase letters
                subList[ord(lst[i][str_i]) - 97].append(lst[i])
            else:
                print("UH OH, idk that character" + lst[i][str_i])

    result = []
    for i in range(len(subList)): #O(28)
        if subList[i]:  #if not empty
            result.extend(str_sort(subList[i], str_i + 1, maxL)) # Recursive: O(len(subList) in worst case

    return result


def countingSort_tup(data, tup_i): #overload for list of tupples
    #tup_i is the index of the tupple to sort

# 1st section - confirms data is a list and each data type is the same
    if not isinstance(data, list):  # O(1) - Checking the type of an object is constant time
        raise TypeError("Argument must be a list.")

    if not data:  # O(1) - Checking if a list is empty is constant time
        raise ValueError("List must not be empty.")

    first_type = type(data[0][tup_i])  # O(1)
    # first_type = <class 'int'> or <class 'str'>

    for i in range(len(data)):
        if first_type != type(data[i][tup_i]):
        # O(len(data)) - Iterates over the list and checks the type of tup_i element
            raise TypeError("All elements in the list must be of the same type.")
# end of 1st section

#2nd section - map values to be sorted to their tupple
    subData = []
    myDict = {}
    for i in range(len(data)):  # O(len(data))
        subData.append(data[i][tup_i])  # O(1) per iteration
        myDict[data[i][tup_i]] = data[i]  # O(1) per iteration (assuming average-case dictionary insert) O(n) worst case
#end 2nd section

#3rd section - sort the data
    subData = countingSort(subData)
#end 3rd section

#4th section - create the result
    result = []
    for i in range(len(subData)): #O(len(subData)) = O(len(data))
        result.append(myDict[subData[i]]) # O(1) per iteration (assuming average-case dictionary lookup) O(n) worst case
    return result







def countingSort(data):
# 1st section - confirms data is a list and each data type is the same
    if not isinstance(data, list):  # O(1) - Checking the type of an object is constant time
        raise TypeError("Argument must be a list.")

    if not data:  # O(1) - Checking if a list is empty is constant time
        raise ValueError("List must not be empty.")

    first_type = type(data[0])  # O(1)
    # first_type = <class 'int'> or <class 'str'>

    if not all(isinstance(item, first_type) for item in data):
        # O(len(data)) - Iterates over the list and checks the type of each element
        raise TypeError("All elements in the list must be of the same type.")
# end of 1st section

# 2nd section - sort the list for ints
    if first_type == int:
        #iterate over data to find max and min
        max = 0
        min = sys.maxsize
        for i in range(len(data)):  # O(len(data))
            if data[i] > max: max = data[i]
            if data[i] < min: min = data[i]

        myList = [0] * (max - min + 1) #O(1) creates a list of 0s for the data set
        for i in range(len(data)):  # O(len(data))
            myList[data[i] - min] += 1
        j = 0
        i = 0
        while i < len(data):  #O(len(data))
            while myList[i + j] == 0: j += 1  #O(the amount of zeros in a row)
            repeated = myList[i + j]
            for k in range(repeated): #O(myList[i+j]) which is equal to the number of repeated elements
                data[i + k] = i + j + min
            i += repeated
            j -= repeated - 1
#end 2nd section
    #the worst case time complexity is O(max - min) because that is the size of myList


#3rd section - try strings
    elif first_type == str:
        myList = [[] for _ in range(28)]   #for each letter and a space
        maxL = 0 #max str length
        for i in range(len(data)): #O(len(data))
            data[i] = data[i].lower()
            if len(data[i]) > maxL: maxL = len(data[i])

            #sort strings by first charecter
            if data[i][0] == ',': #first char a comma, append to 27th spot
                myList[26].append(data[i])
            elif data[i][0] == ' ':  # first char a space, append to 28th spot
                myList[27].append(data[i])
            else:
                myList[ord(data[i][0]) - 97].append(data[i])

        result = []
        for i in range(len(myList)): #O(28)
            if myList[i]:
                result.extend(str_sort(myList[i], 1, maxL)) #total O(n * maxL) where n is the number of ellements
        data = result
#end 3rd section #total O(n * maxL) where n is the number of ellements

    return data
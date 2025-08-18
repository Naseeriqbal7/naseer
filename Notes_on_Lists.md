# WORKING WITH LISTS
> A list contains a collection of items.

##### The syntax for creating a list
```
my_list = [item1, item2, item3, ...]
```
##### Referring items in a list
- To refer to the items in a list, we use an index, where 0 refers the first item, 1 refers the second item, and 2 refer the third item, and so on.
- We can also use negative values for an index, where -1 refers to the last item, -2 refers to the second last item, and so on.

```
my_list[index]
```

#### List Methods
> Use list methods to add and remove the items in a list.

1. append(item)
    - Adds an item to the end of the list.

2. insert(index, item)
    - Inserts an item at the specified index.

3. remove(item)
    - Removes the first occurrence of the specified item.

4. index(item)
    - Returns the index of the first occurrence of the specified item.

5. pop([index])
    - Removes and returns the item at the specified index. If no index is specified, it removes and returns the last item.

- Built-in function to the length of a list:
    len(list)
    - Returns the number of items in the list.

- The 'in' keyword: for membership
    item in list
    - Returns True if the item is in the list, False otherwise.

- Looping through each item of a list:
```
    for item in list:
        statements
```  

##### Immutable objects
- Objects that don't change:
    str, int, bool, float, tuple, etc.
    
##### Mutable objects
- Objects that can change:
    list, dict, set, etc.

#### List of lists
- A list of ists is a list in which the items are other lists.
- To access the item in the list of lists, we use two indexes.
- A list of lists is also called as two-dimensional list (matrix), we can think of the data as columns and rows.


#### More list skills
1. count(item)
    - Returns the number of occurrences of the specified item.

2. reverse()
    - Reverses the order of the items in the list.

3. sort([key=function][, reverse=True/False])
    - Sorts the items in the list in ascending order in its place.
    - The optional key argument specifies a function to be called on each item before sorting.

- A built-in function: sorted(list[, key=function])
    - Returns a new list consisting of the sorted items of the original list.
    - The optional key arguments specifies the function to be called on each item before sorting.


- Two built-in functions
    1. min(list)
        - Returns the minimum value in the list.
    2. max(list)
        - Returns the maximum value in the list.


- Two functions from random module:
    1. choice(list)
        - Returns a random item from the list.
    2. shuffle(list)
        - Randomly shuffles the items in the list.

#### Copying lists
- The assignment operator makes a shallow copy of a list, so both list variables refer to the same list.
- In contrast, the deepcopy() function of the copy module makes a deep copy of the list variables refer to the two different lists.

Syntax:
```
import copy
new_list = copy.deepcopy(list)
```
- The deep copy of the list is a separate list with no relation to the original.


#### Slicing the list
- We can slice a list to get a subset of the original list.
- Syntax:
    my_list[start:end:step]
    By default, start is 0, and step is 1.
    By default, end is exclusive, if we don't specify end then the last item is inclusive.


#### Concatenating a list
- We concatenate lists by using the + operator or the += operator


#### List comprehension
- We can generate items in a list using a for loop inside the list.
new_list = [expression for item in list]
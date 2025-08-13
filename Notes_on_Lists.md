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

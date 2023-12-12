# Insertion Sort
## O(n^2)
Iterating number to the left until its in its sorted position.
- [22, 27, 16, 2, 18, 6], start
- [_**22, 27**_, 16, 2, 18, 6], no change between 22-27 they are already sorted
- [_**16, 22, 27**_, 2, 18, 6], moving 16 to the left until the first 3 elements are sorted
- [_**2, 16, 22, 27**_, 18, 6], moving 2 to the left until the first 4 elements are sorted 
- [_**2, 16, 18, 22, 27**_, 6], moving 18 to the left until the first 5 elements are sorted
- [_**2, 6, 16, 18, 22, 27**_], moving 6 to the left until the first 6 elements are sorted
- _**18**_ in the sorted list might be considered as average case.

# Selection Sort
## O(n^2)
Changing the smallest number in the list with the first element. Then repeating this with the next elements.
- [7, 3, 5, 8, 2, 9, 4, 15, 6], start
- [**2**, 3, 5, 8, **7**, 9, 4, 15, 6]
- [2, 3, 5, 8, 7, 9, 4, 15, 6], no change
- [2, 3, _**4**_, 8, 7 ,9, _**5**_, 15, 6]
- [2, 3, 4, _**5**_, 7, 9, _**8**_, 15, 6]
- [2, 3, 4, 5, _**6**_, 9, 8, 15, _**7**_]
- [2, 3, 4, 5, 6, _**7**_, 8, 15, **9**]
- [2, 3, 4, 5 ,6, 7, 8, 15, 9], no change
- [2, 3, 4, 5, 6, 7, 8, _**9**_, _**15**_]

# Merge Sort
## O(nlogn)
Splitting the list into two parts and repeating this process until each part has one or two elements.
- [16, 21, 11, 8, 12, 22]
- [16, 21, 11] - [8, 12, 22]
- [16] [21, 11] - [8] [12, 22]
- [_**11, 16, 21**_] - [**_8, 12, 22_**]
- [_**8, 11, 12, 16, 21, 22**_]

# Binary Search Tree
Assuming root is somewhere in the middle of the sorted list. Then inserting new values to the left(smaller than parent) or the right(greater than parent) of the root, then repeating this process. (searching, deleting also works same) (Depending on the distrubition of the values.)
- [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
* Assuming 5 is the root,
* 1 on the left of the **_5_** and 7 on the right of the **_5_**,
* 0 on the left of the **_1_** and 2 on the right of the **_1_**,
* 3 on the right of the **_2_**,
* 4 on the right of the **_3_**,
* 6 on the left of the **_7_** and 8 on the right of the **_7_**,
* 9 on the right of the **_8_**.
```               
            5
          /   \       
        1       7
       / \     / \
      0   2   6   8
           \       \
            3       9
             \
              4
```
Solutions may be different, and it will also affect its time complexity. More balanced tree means, more efficient Binary Search.

```               
            7
          /   \       
        5       8
       / \       \
      1   6       9
     / \
    0   3
       / \
      2   4

```

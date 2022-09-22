# Manage_Inventory


*Problem*


Ash is tasked with maintaining an inventory list of all the items in a lab. The inventory list contains entries of all the items present in the lab along with its quantity. On daily basis items can be borrowed from the lab or new items can be added to the Lab. Hence Ash usually performs 2 operations on the inventory list:  Adding items to the list Deleting items from the list Ash usually does this manually and would prefer to use a program to maintain the inventory list. Your task is to write a program that will help Ash.  Consider there are NN items in the lab initially. Therefore create a list LL that will contain all the names of items (item\_nameitem_name) along with its quantity (item\_quantityitem_quantity).  Also, make provision for adding/deleting items to/from the list. The item name and its quantity along with the operation (ADD / DELETE) will be specified. You must take care of the following conditions while performing any of the operations on the list.


*Condition for Adding*

Format: ADD $item_name$ $quantity$
    If the item\_nameitem_name of the item to be added does not exist in the list, then add item_name and its quantity to the List LL and print ADDED Item $item_name$
    If the item\_nameitem_name of the item to be added exists in the list, then simply update the quantity of the item and print UPDATED Item $item_name$


*Condition for Deleting*

Format: DELETE $item_name$ $quantity$
    If the item\_nameitem_name of the item to be deleted does not exist in the list, then print Item $item_name$ does not exist
    If the item\_nameitem_name of the item to be deleted exists in the list, then check if its quantity in the list LL is less than the quantityquantity specified in             the DELETE operation.
    If it is less then, print Item $item_name$ could not be DELETED
    Else update the quantity by subtracting the specified amount and print DELETED Item $item_name$

*Input Format*

    First line will contain TT, number of testcases. Then the testcases follow.
    Each testcase contains the following:
    NN, the number of items in the lab initially.
    Followed by list of items in the next NN lines. Every line will specify the item\_nameitem_name and item\_quantityitem_quantity separated by space.
          MM, the number of operations to be performed.
    Followed by sequence of operations on every new line. The operation format is: operation_name item\_nameitem_name quantityquantity separated by space.


*Output Format*

    For each testcase, the output should be as follows:

    Sequence of the print statements for every operation performed on individual lines.
    Finally print the sum of quantities of all items in the list LL, formatted as:


Total Items in Inventory:

*Constraints*
      1 \leq T \leq 251≤T≤25
      1 \leq N \leq 1001≤N≤100
      1 \leq M \leq 1001≤M≤100

  Operations will be either ADD or DELETE in capitals
      1 \leq1≤ quantities of each item \leq 100≤100

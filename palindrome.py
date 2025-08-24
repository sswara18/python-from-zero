list1 = [1,2,1]
list2 = [1,2,3]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("Palindrome")
else:
    print("Not a Palindrome")
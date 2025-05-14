'''
Task: 01.
'''

Dict = {'Mike': 89, 'John': 95, 'Bob': 92}
Name = input("Enter the Student's Name:")
if Name in Dict:
    print(Name, "got", Dict[Name], "marks.")
else:
    print(Name, "is not found in the dictionary named Dict.")
    

'''
Task: 02.
'''
List = list(range(1,11))
print(List)
List_f_5 = List[0:5]
print("First five elements from the list are:", List_f_5)
List_f_5_Rev = list(reversed(List_f_5))
print("The reverse order of the first five elements from the list are:", List_f_5_Rev)

#################################################################################################
###########
#################################################################################################

'''
Task: 01.
'''

Dict = {'Mike': 89, 'John': 95, 'Bob': 92}                                                                # Creates Dictionary.
Name = input("Enter the Student's Name:")                                                                 # Allows to provide a name.
if Name in Dict:                                                                                          # Checks provided name is in the dictionary or not.
    print(Name, "got", Dict[Name], "marks.")                                                              # Prints marks if the name is in the dictionary.
else:
    print(Name, "is not found in the dictionary named Dict.")                                             # Prints this message if the name is not in the dictionary.
    

'''
Task: 02.
'''
List = list(range(1,11))                                                                                  # Creates list.
print(List)
List_f_5 = List[0:5]                                                                                      # Extracts the first five elements from the list.
print("First five elements from the list are:", List_f_5)
List_f_5_Rev = list(reversed(List_f_5))                                                                   # Reverse the list.
print("The reverse order of the first five elements from the list are:", List_f_5_Rev)

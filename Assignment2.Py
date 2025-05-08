'''## Task: 01'''

n = int(input("Enter the number: "))
if (n % 2 == 0):
    print("The", n, "is an even number.")
else:
    print("The", n, "is an odd number.")

'''## Task: 02'''

s = 0
for i in range(1,51):
    s = s+i
print('The sum of the numbers from 1 to 50 is', s, '.')



###############################################################################

############## Readme.md content.

###############################################################################

'''## Task: 01'''

n = int(input("Enter the number: "))          'Enter the number to be check.'
if (n % 2 == 0):                               ' Checks the remainder equals to zero or not after dividing by 2.'
    print("The", n, "is an even number.")
else:
    print("The", n, "is an odd number.")

'''## Task: 02'''

s = 0                                                        'Setting the initial sum equals to zero.'
for i in range(1,51):                                          'Range function do not include the upper value in the loop.'
    s = s+i                                                    'Adds the sequential numbers in the sum.'
print('The sum of the numbers from 1 to 50 is', s, '.')

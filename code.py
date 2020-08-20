#Print out all of the numbers in the following array that are divisible by 3:

y = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

#The expected output for the above input is:
  # 3/ num == 0

x = [num for num in y if num % 3 == 0]

print(x)
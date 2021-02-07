"""
    Learning to convert some JAVA code into Python code
    I will be using my JavaReview01 part 01 code.
"""
print("\nInteger values in the Array\n")

nums = [39, 46, 10, 37, 33, 4, 30, 26, 14, 19, 29, 6, 43, 8, 35, 50, 13, 25,
        17, 48, 28, 3, 41, 34, 36, 38, 49, 16, 45, 2, 40, 15, 24, 7, 5, 9, 20, 1, 42,
        44, 21, 47, 12, 22, 18, 31, 11, 32, 27, 23]
nums_set = set(nums)

while True:
    userInput = int(input("Guess an Integer value between 1 and 50: "))

    if userInput in nums_set:
        print("Yes,", userInput, "is in the array list")
        print("The position value for the array index is: ", nums.index(userInput))
        break
    else: input("Nope, Hit Enter and Try again")






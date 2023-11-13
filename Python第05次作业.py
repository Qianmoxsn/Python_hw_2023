'''
Description:

Give a range of integers and find the first ten Palindrome Numbers (回文数字) in this range.

If there are less than 10 outputs, output all the Palindrome Numbers in this range.
'''

if __name__ == "__main__":
    # answer here
    a, b = map(int, input("Please input the range of integers split with , :").split(","))
    print("Find Palindrome Numbers between " + str(a) + "~" + str(b) + "\n")
    count = 0
    for i in range(a, b + 1):
        if str(i) == str(i)[::-1]:
            print(i)
            count += 1
            if count == 10:
                break
    if count == 0:
        print("No Palindrome Numbers in this range!\n")
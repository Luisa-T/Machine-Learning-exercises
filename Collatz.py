# first week exercise

n = int(input("enter a positive integer"))

# keep looping until we reach 1
#Note: ths assumes that the Collatx conjecture is true
while n != 1:
    # print the current value of n
    print(n)
    # check if n is even
    if n % 2 == 0:
        # if n is even, divide it by two
        n = n // 2
    else:
        # if n is odd, multiply be three and add 1
        n = ( 3 * n) + 1
# Finally, print 1
print(n)
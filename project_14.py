
# Longest Collatz sequence

def collatz(n):

    count = 1
    while n != 1:
        #print n,
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        count += 1
    #print n
    #print count
    return count

def find_longest():
    max_index = 0
    max_length = 0
    for i in range(1, 1000000):
        length = collatz(i)
        if length > max_length:
            max_index = i
            max_length = length
    
    print("\nThe longest collatz sequence starts at {} and it is {} numbers in length.\n".format(max_index, max_length))
    
if __name__ == '__main__':

    find_longest()
    #collatz(13)
    print(collatz(837799))

# text = input().split()
file = open('files/rosalind_fib.txt')
text = file.read().split()

# main code starts here #
fib = [1, 1]

for i in range(int(text[0]) - 2):
    fib.append(fib[i+1] + fib[i] * int(text[1]))

print(fib[int(text[0])-1])
# main code ends here #

file.close()

'''
Alternative solution:

def fib(n, k):
    previous1, previous2 = 1, 1
    for i in range(2, n):
        previous1, previous2 = previous2, previous1 * k + previous2
    return previous2
'''
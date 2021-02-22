file = open('files/rosalind_hamm.txt')
text = file.readlines()

# main code starts here #
num = 0

for i in range(len(text[0].rstrip())):
    if text[0][i] != text[1][i]:
        num += 1

print(num)
# main code ends here #

file.close()

'''
Alternative solution:

s1 = 'GAGCCTACTAACGGGAT'
s2 = 'CATCGTAATGACGGCCT'
print(sum([a != b for a, b in zip(s1, s2)]))
'''

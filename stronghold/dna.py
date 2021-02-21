# text = input()
file = open('files/rosalind_dna.txt')
text = file.read()

# main code starts here #
print(text.count('A'), text.count('C'), text.count('G'), text.count('T'))
# main code ends here #

file.close()

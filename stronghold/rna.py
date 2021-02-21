# text = input()
file = open('files/rosalind_rna.txt')
text = file.read()

# main code starts here #
print(text.replace('T', 'U'))
# main code ends here #

file.close()

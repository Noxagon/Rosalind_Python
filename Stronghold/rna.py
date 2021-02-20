# text = input()
file = open('Files/rosalind_rna.txt')
text = file.read()

# main code starts here #
print(text.replace('T', 'U'))
# main code ends here #

file.close()
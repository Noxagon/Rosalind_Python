# text = input()
file = open('Files/rosalind_rna.txt')
text = file.read()
text = text.replace("\n", "")

# main code starts here #
final = ""
dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

for s in text:
    final += s.replace(s, dict[s])

print(final[::-1])
# main code ends here #

file.close()
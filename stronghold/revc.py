# text = input()
file = open('files/rosalind_revc.txt')
text = file.read().replace("\n", "")

# main code starts here #
final = ""
match = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

for s in text:
    final += s.replace(s, match[s])

print(final[::-1])
# main code ends here #

file.close()

'''
Alternative solution:

st = "AAAACCCGGT"
st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print st
'''
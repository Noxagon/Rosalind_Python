file = open('files/rosalind_subs.txt')
text = file.readlines()

# main code starts here #
s = text[0].replace("\n", "")
t = text[1].replace("\n", "")

output = ""

for i in range(len(s)):
    if s[i:i+len(t)] == t:
        output += str(i+1)+" "

print(output)
# main code ends here #

file.close()

'''
Alternative solution:

s1,s2 = open('rosalind_subs.txt').read().split('\r\n')

for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print i+1,
        
===== OR =====

dnaSeq = "GATATATGCATATACTT"
subSeq = "ATAT"

r = 0
while r != -1 :
        r = dnaSeq.find(subSeq,r+1)
        print r+1
'''
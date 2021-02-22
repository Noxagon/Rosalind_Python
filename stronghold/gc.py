file = open('files/rosalind_gc.txt')
text = file.readlines()

# main code starts here #
id = {}
lines = []
name, max_name, line, dna = "", "", "", ""
gc, max_gc = 0, 0

for line in text:
    newline = line.replace("\n", "")

    if newline.find("Rosalind") == 1:
        name = newline.replace(">", "")
        dna = ""
        lines.clear()
    else:
        lines.append(line)
        dna = "".join(lines).replace("\n", "")

    id.update({name: dna})

for i in id:
    gc = (id[i].count('G') + id[i].count('C')) / len(id[i]) * 100
    if gc > max_gc:
        max_name, max_gc = i, gc

print(max_name)
print(max_gc)
# main code ends here #

file.close()

'''
Alternative solution:

f = open('rosalind_gc.txt', 'r')

max_gc_name, max_gc_content = '', 0

buf = f.readline().rstrip()
while buf:
    seq_name, seq = buf[1:], ''
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content

print('%s\n%.6f%%' % (max_gc_name, max_gc_content * 100))
f.close()
'''

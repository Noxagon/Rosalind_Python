file = open('files/rosalind_cons.txt')

collection = {}
dna_row, dna_col, profile = [], [], []
data = []

buf = file.readline().rstrip()
while buf:
    seq_name, seq_string = buf[1:], ''
    buf = file.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq_string = seq_string + buf
        buf = file.readline().rstrip()

    data.append(seq_string)
    collection.update({seq_name: seq_string})

# print(data)

for i in range(len(data[0])):
    for j in data:
        dna_col.append(j[i])
    dna_row.append(dna_col)
    dna_col = []

# print(dna_row)

for dna in dna_row:
    profile.append([dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')])

# print(profile)

cons_num = 0
cons_type = 0
consensus = []

for k in profile:
    for l in range(len(k)):
        if k[l] > cons_num:
            cons_num = k[l]
            cons_type = l
    cons_num = 0
    if cons_type == 0:
        consensus.append('A')
    elif cons_type == 1:
        consensus.append('C')
    elif cons_type == 2:
        consensus.append('G')
    elif cons_type == 3:
        consensus.append('T')

print("".join(consensus))

output_row = []
output_col = []

for i in range(len(profile[0])):
    for j in range(len(profile)):
        output_col.append(profile[j][i])
    output_row.append(output_col)
    output_col = []

# print(output_row)
for i in range(len(output_row)):
    if i == 0:
        print("A: " + "".join(str(output_row[i]).replace("[", "").replace("]", "").replace(",", "")))
    if i == 1:
        print("C: " + "".join(str(output_row[i]).replace("[", "").replace("]", "").replace(",", "")))
    if i == 2:
        print("G: " + "".join(str(output_row[i]).replace("[", "").replace("]", "").replace(",", "")))
    if i == 3:
        print("T: " + "".join(str(output_row[i]).replace("[", "").replace("]", "").replace(",", "")))

file.close()

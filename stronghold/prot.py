# text = input()
prot_file = open('files/rosalind_prot.txt')
text = prot_file.read().replace("\n", "")

table_file = open('files/rna_codon_table.txt')
lines = table_file.readlines()

# main code starts here #
table = {}
output = ""

for i in range(len(lines)):
    table.update(dict(map(lambda x: x.split('='), lines[i].replace("\n", "").split(';'))))

for j in range(0, len(text), 3):
    if table[text[j:j + 3]] == "Stop":
        break
    output += table[text[j:j + 3]]

print(output)
# main code ends here #

prot_file.close()
table_file.close()

'''
Alternative solution:

string = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

coded = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
decoded = ''

traL =  string.split()
traDict = dict(zip(traL[0::2], traL[1::2]))
# memo => array[startingIndex::stepIndex]

for i in range(0, len(coded)-3, 3):
    decoded += traDict[coded[i:i+3]]

print decoded
'''
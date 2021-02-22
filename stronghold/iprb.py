# text = input().split()
file = open('files/rosalind_iprb.txt')
text = file.read().split()

# main code starts here #
k, m, n = (int(val) for val in text)
total = 4 * (k + m + n) * (k + m + n - 1)
recessive = 4 * n * (n - 1) + m * (m - 1) + 4 * (m * n)
prob = (total - recessive) / total
# Simplified version = 1 - (n*(n-1) + 0.25*m*(m-1) + m*n) / ((k+m+n) * ((k+m+n)-1))
print(prob)
# main code ends here #

file.close()

'''
Alternative solution:
def firstLaw(k,m,n):
   N = float(k+m+n)
   return(1 - 1/N/(N-1)*(n*(n-1) + n*m + m*(m-1)/4.))

Draft (Ignore):
(xx)(xx) = (n^2 - n)(4)(4/4)    100%
(Xx)(xx) = 2(m)(n)(4)(2/4)       50%
(Xx)(Xx) = (m^2 - m)(4)(1/4)     25%
'''


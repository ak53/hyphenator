#Name-Amandeep Kaur

""" Inserts hyphens into a non-empty even-length input string as follows:
The hyphen splits the first and second halves. 
"""

s = input('Enter an even-length string: ')
n = len(s)
#print ('n is',n)
if n%2 == 0:                           # Line A
    if n ==0:
        print('-')
    else:
        # s has even length
        m = n//2
        #print ('even case. m is',m)
        first = s[0:m]                     # Line B
        #print ('even case. first is',first)
        second = s[m:]                     # Line C
        #print ('even case. second is',second)
        h = first + ' - ' + second
        # final output
        print (h)

elif n%2!=0:
    # s is of odd length.
    m=(n//2)+1
    first=s[:m]
    second=s[m:]
    print(first+' - '+second)

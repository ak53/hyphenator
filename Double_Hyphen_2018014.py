#Name-Amandeep KAur

""" Inserts hyphens into a non-empty odd-length input string as follows:
A hyphen is inserted on either side of the middle character.

Example: "abcde" becomes "ab-c-de"

"""

s = input('Enter an odd-length string: ')

n = len(s)
if n%2==0:
	print('Invalid Input')
else:
	if n==1:
		print('String length',n)
	else:
		m = int(n/2)
		#print('m is',m)

		first = s[0:m]
		#print('first is',first )


		middle = s[m]
		#print('middle is',middle)

		second = s[m+1:]
		#print('second is',second)

		h = first+'-'+middle+'-'+second

		# final output
		print (h)

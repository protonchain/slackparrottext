import numpy as np
import pandas as pd

def parrot(text, numspaces=1, partype=':60fpsparrot:', letters):
    matrix = np.zeros((5,5*len(text)))
    for i,letter in enumerate(text):
        letter = letter.upper()
        mat = letters[:,:,ord(letter)-ord('A')]
        matrix[:,i*5:(i*5)+5] = mat
    
    for i in range(5):
        st = ''
        for j in range(5 * len(text)):
            if(j % 5 == 0 and j != 0):
                st += ':blank:'* numspaces
                
            if(matrix[i,j] == 0):
                st += ':blank:'
            else:
                st += partype
        print(st)
        
if __name__ == '__main__':

	colnames = []
	for i in range(26):
		for j in range(5):
			colnames.append('{}{}'.format(chr(ord('A') + i), j+1))
		
	df = pd.read_csv('letters.csv', names=colnames)

	letters = np.zeros((5,5,26))
	for i in range(26):
		for j in range(5):
			letters[:,j,i] = df['{}{}'.format(chr(ord('A') + i), j+1)].values
			
	parrot('same', partype=':wave1:', numspaces=1, letters=letters)
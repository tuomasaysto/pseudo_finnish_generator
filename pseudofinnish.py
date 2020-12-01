'''A script that generates a desired number of pseudo Finnish words with
specific number of syllables. Works by combining Finnish syllables randomly.
Call with a function pse_fin(a,b) where a is the number of syllables in 
the words, and b the number of words. Returns a list.'''

from random import randrange

# Open dict.txt as list
f = open('dict.txt', encoding='utf-8' )
f = f.read()
f = f.split(', ')

# Create a list of words created via rand_syls. b = number of words needed
def pse_fin(a, b):
    wordlist = []
    i = 0
    while i < b:
   
        # Create a random word out of random syllables, where a = number of syllables
        syl_list = []
        def rand_syls (a):
            i = 0
            while i < a:
                   tavu = (f[randrange(1700)])
                   syl_list.append(tavu)
                   i += 1
            word = ''.join([str(elem) for elem in syl_list]) 
            return word
        
        c = rand_syls(a)        
        wordlist.append(c)
        i += 1
    
    return wordlist
    

# Example        
print(pse_fin(3, 10))


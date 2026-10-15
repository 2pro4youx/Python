"""Find the length of a string"""
#a=input("Enter a String: ")
#print(len(a))

"""Count vowels in a string"""
#v=['a','e','i','o','u']
#a=input("Enter charachters: ")
#c=0
#for i in a:
    #if i in v:
        #c+=1
#print("Vowels Detected: ",c)

"""Count consonants in a string"""
#v=['a','e','i','o','u']
#a=input("Enter charachters: ")
#c=0
#for i in a:
    #if i == " ":
        #c+=0
    #elif i not in v:
        #c+=1
#print("Consonants Detected: ",c)

"""Count digits in a string"""
#v=['1','2','3','4','5','6','7','8','9','0']
#a=input("Enter charachters: ")
#c=0
#for i in a:
    #if i in v:
        #c+=1
#print("Digits Detected: ",c)
##or
#a=input("Enter charachters: ")
#c=0
#for i in a:
    #try:
        #int(i)
        #c+=1
    #except:
        #pass
#print("Digits Detected: ", c)

"""Count special characters in a string"""
#a=input("Enter charachters: ")
#c=0
#for i in a:
    #if i in v:
        #c+=1
#print("Consonants Detected: ",c)

"""Convert string to uppercase"""
#a=input("Enter String: ").upper()
#print(a)

"""Convert string to lowercase"""
#a=input("Enter String: ").lower()
#print(a)

"""Reverse a String"""
#a=input("Enter String: ").lower()
#print(a[::-1])

"""Check whether a string is palindrome or not"""
#a=input("Enter String: ").lower()
#ra=a[::-1]
#if a==ra:
    #print("String is palindrome")
#else:
    #print("String is not palindrome")
    
"""Count total words in a string"""
#a=input("Enter a sentence: ")
#ra=a.split()
#print("Number of words: ", len(ra))

"""🚩Find frequency of each character in a string"""
#a = input("Enter a string: ")
#f = {}
#for i in a:
    #if i in f:
        #i.lower()
        #f[i] += 1
    #else:
        #i.lower()
        #f[i] = 1
#print("Character frequencies:")
#for i, c in f.items():
    #print(f"'{i}': {c}")
    
"""Find first non-repeating charachter"""
#a = input("Enter a string: ")
#f = {}
#for i in a:
    #if i in f:
        #i.lower()
        #f[i] += 1
    #else:
        #i.lower()
        #f[i] = 1
#found=False
#for i in a:
    #if f[i]==1:
        #found=True
        #print(f"{i} is the first non-repeating charachter")
        #break
#if not found:
    #print("Every charachter is repeating")
    
"""Find first repeating charachter"""
#a = input("Enter a string: ")
#f = {}
#for i in a:
    #if i in f:
        #i.lower()
        #f[i] += 1
    #else:
        #i.lower()
        #f[i] = 1
#found=False
#for i in a:
    #if f[i]==2:
        #found=True
        #print(f"{i} is the first repeating charachter")
        #break
#if not found:
    #print("None of the charachters repeat")
    
"""Remove duplicate characters from a string"""
#a = input("Enter a string: ")
#r=""
#for i in a:
    #if i not in r:
        #r+=i
#print(f"String after removing the duplicates is: {r}")

"""Replace spaces with hyphens"""
#a = input("Enter a string: ")
#print(a.replace(' ','-'))

"""Remove all spaces from a string"""
#a = input("Enter a string: ")
#print(a.replace(' ',''))

"""Find ASCII value of each charachter"""
#a = input("Enter a string: ")
#char = []
#for i in a:
    #if i not in char:
        #char.append(i)
        #v=ord(i)
        #print(f"'{i}' : {v}")
        
"""Compare two strings without using librabries"""
#a=input("Enter a string a: ")
#b=input("Enter a string b: ")
#la=len(a)
#lb=len(b)
#if la!=lb:
    #print("Strings are not equal")
#else:
    #equal=True
    #for i in range(la):
        #if a[i]!=b[i]:
            #equal=False
            #break
    #if equal:
        #print("Strings are equal")
    #else:
        #print("Strings are not eqal")
        
"""Concatenate two strings without using library function"""
#a=input("Enter a string a: ")
#b=input("Enter a string b: ")
#c=""
#for i in a:
    #c+=i
#c+=" "
#for i in b:
    #c+=i
#print ("Concatenated Strings: ",c)

"""Copy one string into another"""
#a = input("Enter a string to copy: ")
#b= ""  # Start with an empty target string
#for i in a:
    #b += i
#print("Original String:", a)
#print("Copied String:", b)

"""Search a charachter in a string"""
#a=input("Enter a string: ")
#b=input("Enter a character to search in the string: ")
#index=0
#found = False
#for i in a:
    #if i==b:
        #print(f"The charachter {b} exists in '{a}' at the position {index}")
        #found = True
        #break
    #index+=1
#if not found:
    #print(f"The charachter {b} does not exist in '{a}'")
    
"""Search a word in a sentence"""
#a1=input("Enter a Sentence: ")
#a=a1.split()
#b=input("Enter a word to search in the string: ")
#index=0
#found = False
#for i in a:
    #if i==b:
        #print(f"The word '{b}' exists in '{a1}' at the position {index}")
        #found = True
        #break
    #index+=1
#if not found:
    #print(f"The word '{b}' does not exist in '{a1}'")
    
"""Count occurrence of a substring"""
#a = input("Enter a string: ")
#b = input("Enter a substring: ")
#la=len(a)
#lb=len(b)
#if lb>la:
    #print("Substring cannot occur in the string due to its length")
#else:
    #count=0
    #for i in range(la):
        #text=a[i:i+lb]
        #if text==b:
            #count+=1
#print(f"The substring '{b}' appears in string '{a}', {count} time(s)")

"""🚩Find longest word in a sentence"""
#a=input("Enter a Sentence: ")
#s=a+" "
#c_word=""
#l_word=""
#cl=0
#for i in s:
    #if i!=" ":
        #c_word+=i
    #else:
        #cl=len(c_word)
        #ll=len(l_word)
        #if cl>ll:
            #l_word=c_word
        #c_word=""
#print("Longest Word:", l_word)

"""Find shortest word in a sentence"""
#a=input("Enter a Sentence: ")
#s=a+" "
#c_word=""
#s_word="pneumonoultramicroscopicsilicovolcanoconiosis"
#cl=0
#for i in s:
    #if i!=" ":
        #c_word+=i
    #else:
        #cl=len(c_word)
        #sl=len(s_word)
        #if cl<sl:
            #s_word=c_word
        #c_word=""
#print("Shortest Word:", s_word)

"""Sort charachters of a string alphabetically"""
#a=input("Enter a string: ")
#b=[]
#for i in a:
    #b.append(i)
#l=len(b)
#for i in range(l):
    #for j in range (l-i-1): #i is for optimization purposes
        #if b[j] > b[j + 1]:
            #b[j], b[j+1]=b[j+1], b[j]
#r=""
#for i in b:
    #r+=i
#print("Sorted characters are: ",r)
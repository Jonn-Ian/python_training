str = ["act","pots","tops","cat","stop","hat"]
anagrams = {}

for word in str: 
    key = "".join(sorted(word))
    
    for keys in word:

        if key in word:
            anagrams = key
            print([anagrams])

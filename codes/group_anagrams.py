str = ["act","pots","tops","cat","stop","hat"]
anagrams = {}

for word in str: 
    key = "".join(sorted(word))

    if key in str:
        anagrams = key
        print(anagrams)
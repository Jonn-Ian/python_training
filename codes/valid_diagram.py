s = "racecar"
t = "carrace"

#separating the characters to words by using tuple
tuple_s = tuple(s)
tuple_t = tuple(t)

#turn them into a list to be prepared to be arranged 
list_s = list(tuple_s)
lists_t = list(tuple_t)

#arrange the letters alphabetically
list_s.sort()
lists_t.sort()

#create a loop that equal to the length to the letters
#that has been sorted
for i in range(len(list_s) -1):
    #compare the both arranged list to each other by index
    if list_s[i] == lists_t[i]:
        print(True) #if the same, output True
        break
    else:
        print(False)
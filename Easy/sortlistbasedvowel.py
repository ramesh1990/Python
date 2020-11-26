
def is_vowel(ch):
    ch = ch.upper()
    if(ch in "AEIOU"):
        return 1
    else:
        return 0

def count_vow(word):
    count = 0
    for ch in word:
        count += is_vowel(ch)
    return count

def sortList(lst):
    result = []
    for word in lst:
        result.append((count_vow(word), word))
    result.sort()
    t = []
    for i in result:
        t.append(i[1])
    return t

print (" Sort a list based on the count of vowel : ",sortList(['Ramesh',"Balaji","Priyanka","Akhil"]))
def remove_duplicates(s):
    # this will store the final result without duplicates
    res = ""
    # go through each character in the string
    for ch in s:
        if ch not in res:     # add character only if not already present
            res += ch
    return res       # return the cleaned string

s = input("Enter string: ")
print(remove_duplicates(s))

'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    # if the length of the word is less than 2 set to 0
    if len(word) < 2:

        return 0
    # if the letters are equal to th then +1 and slice them off else keep slicing
    elif word[:2] == "th":
        
         return count_th(word[2:]) + 1
    else:
        
        return count_th(word[1:])
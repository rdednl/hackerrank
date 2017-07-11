from collections import Counter

"""
#not fast enough

def ransom_note(magazine, ransom):
    for _ in ransom:
        if _ not in magazine:
            return False
        else:
            magazine.remove(_)
    return True
"""

def ransom_note(magazine, ransom):
    return (Counter(ransom)-Counter(magazine)) == {}

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
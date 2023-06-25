# Finding Anagram Pairs


def anagram(n=None):
    if n is None:
        n = input('Enter your words as space seperated : ').split(' ')
    t = []
    while len(n) != 0:
        for j in n:
            if n[0] == j:
                pass
            elif sorted(n[0]) == sorted(j):
                t.append((n[0], j))
        n.remove(n[0])
    print(t)

anagram()

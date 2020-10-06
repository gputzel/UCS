def to_set(n):
    """Helper function for turning numbers into sets"""
    l=[]
    place=1
    while n > 0:
        bit = n % 2
        if bit:
            l.append(place)
        place += 1
        n = (n - bit)//2
    return frozenset(l)

def from_set(s):
    """Helper function for turning sets into numbers"""
    return sum([2**(i-1) for i in list(s)])

def to_integer_list(n):
    return [i-1 for i in to_set(n)]

class Family:
    n = 0 #Integer representation of the family of sets
    def __init__(self,n=0):
        self.n = n
    def to_integer_list(self):
        n = self.n
        return [i-1 for i in to_set(n)]
    def __str__(self):
        s = {to_set(i-1) for i in to_set(self.n)}
        return '{' + ','.join([str(set(ss)) if len(ss) > 0 else '{}' for ss in s]) + '}'
    def __repr__(self):
        return "Family(n=" + str(self.n) + ")"
    def is_union_closed(self):
        n = self.n
        l = to_integer_list(n)
        s = set(l)
        for i in range(len(l)):
            for j in range(i,len(l)):
                s1 = l[i]
                s2 = l[j]
                if not (s1 | s2) in s:
                    return False
        return True

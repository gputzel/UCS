from fractions import Fraction

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

def from_family(f):
    return sum([2**from_set(s) for s in f])

class Family:
    n = 0 #Integer representation of the family of sets
    def __init__(self,x):
        if type(x)==int:
            self.n = x
        else:
            if type(x) == set:
                self.n = from_family(x)
            else:
                raise TypeError('Family can not be constructed from type ' + str(type(x)))
    def to_integer_list(self):
        n = self.n
        return [i-1 for i in to_set(n)]
    def __str__(self):
        s = {to_set(i-1) for i in to_set(self.n)}
        return '{' + ','.join([str(set(ss)) if len(ss) > 0 else '{}' for ss in s]) + '}'
    def __repr__(self):
        return 'Family(' + str({to_set(i) for i in to_integer_list(self.n)}) + ')'
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
    def __add__(self,x):
        if type(x)==int:
            return Family({to_set(i) for i in to_integer_list(self.n)} | {to_set(x)})
        elif type(x) == frozenset:
            return Family({to_set(i) for i in to_integer_list(self.n)} | {x})
        else:
            raise TypeError('Family can not be constructed from type ' + str(type(x)))
    def prevalences(self):
        u = set()
        fam = {to_set(i) for i in to_integer_list(self.n)}
        l=len(fam)
        for s in fam:
            u = u | set(s)
        d = {i:0 for i in u}
        for s in fam:
            for i in s:
                d[i] += 1
        #return {i:round(d[i]/l,3) for i in d.keys()}
        print(d[i],',',l)
        return {i:Fraction(d[i],l) for i in d.keys()}

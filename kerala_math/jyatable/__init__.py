
def to_mst(f: float):
    """
    Convert float input to minutes/seconds/thirds/fourths
    """
    _r = f * 60 * 60 * 60 * 60
    minutes, _r = divmod(_r, 60*60*60*60)
    seconds, _r = divmod(_r, 60*60*60)
    thirds, _r  = divmod(_r, 60*60)
    fourths, _r = divmod(_r, 60)
    return int(minutes), int(seconds), int(thirds), int(fourths)

def to_float(m, s, t=0, f=0):
    return m + s/60 + t/3600 + f/216000


# Class that implements Minutes, seconds, thirds, fourths
class MST(object):
    def __init__(self, minutes, seconds=None, thirds=0, fourths=0):
        if seconds is not None:
            self.mst = (minutes, seconds, thirds, fourths)
        else:
            self.mst = to_mst(minutes)

    def __add__(self, other):
        a = to_mst(float(self) + float(other))
        return MST(*a)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        a = to_mst(float(self) - float(other))
        return MST(*a)

    def __rsub__(self, other):
        a = to_mst(float(other) - float(self))
        return MST(*a)

    def __truediv__(self, other):
        a = to_mst(float(self) / float(other))
        return MST(*a)
    
    def __mul__(self, other):
        a = to_mst(float(self) * float(other))
        return MST(*a)

    def __rmul__(self, other):
        return self.__mul__(other);
       
    def __float__(self):
        return to_float(*self.mst)

    def __str__(self):
        return ",".join([str(x) for x in self.mst])

    def __repr__(self):
        return str(self)

    

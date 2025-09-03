

def pintu():
    def kumar():
        s = 'hello'
    s = 'pintu'

s = 'kumsr'
pintu()
print(s)
print(type(pintu))
print(pintu.__code__.co_varnames)
print(globals()['pintu'])
print(locals())

import dis

def fun():
    s += 'GFG'

dis.dis(fun)

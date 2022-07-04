values = [2,3,4,5,6,7,8,9,10]

def powers(val,po):
    return val ** po

def non_concurrent_powers(po):
    for val in values:
        res = powers(val,po)
        print('%s to the power of %s is %s' % (val,po,res), '\n')

def concruent_powers(po):

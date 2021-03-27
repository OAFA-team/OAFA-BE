def positive_int(integer_string, strict=False, cutoff=None):
    '''Cast a string to a strictly positive integer.'''
    ret = int(integer_string)
    if ret < 0 or (ret == 0 and strict):
        raise ValueError()
    if cutoff:
        return min(ret, cutoff)
    return ret

#!/usr/bin/env python
# Port of my php base62 numbering thingy.

def base62(num):
    BASE62_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = []
    while( num > 61 ):
        result.append( BASE62_CHARS[ (num % 62) ] )
        num = num // 62

    result.append( BASE62_CHARS[ (num % 62) ] )

    result = "".join(result)
    return result[::-1]

if __name__=="__main__":
    # test/easy use
    import sys
    print base62(int(sys.argv[1]))

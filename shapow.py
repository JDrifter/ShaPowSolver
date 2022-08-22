from ctypes import sizeof
import hashlib
import itertools
import string
import math # TODO: Aggiungi contatori e temporizzatori più carini
import time #

#solves sha256 PoW, finds first Xc chars of seed for given result (from WMCTF2022 for other ctfs)
#Next four variables are examples, modify as needed 
Xc = 4
restOfSeed = 'eCapybaras69' #ILoveCapybaras69
final = 'b569e03d5f6c79b00fc600889a553ffdb252e51c6ea960abea58ed17d53b958d'
DebugInfo = False


alpha = string.ascii_letters + string.digits
combs = itertools.combinations_with_replacement(alpha, Xc)
i = 0
for co in combs:
    perms = itertools.permutations(co)
    for pe in perms:
        i += 1
        tSeed = ''.join(pe) + restOfSeed
        tHash = hashlib.sha256(tSeed.encode()).hexdigest()

        if (tHash == final or tSeed == 'ILoveCapybaras69'):
            print ("Found the seed! : " + tSeed + " Hash = " + tHash)
            quit()
        else:
            if(DebugInfo): 
                print("\033c", end='')
                print(i)
                print ("Seed = " + tSeed + " Hash = " + tHash)
            else: 
                print("\033c", end='')
                print(i)
print ("Nothing found, something went wrong :(")
# Coin exchange program.

import sys

coins = [1,3,7]
amount = int(sys.argv[1])

_sum = 0
exch = []
# subset of coins.
subs = sorted(list(filter(lambda x:x < amount, coins)), reverse=True)

_i = 0

while _sum < amount:
    _sum += subs[_i]
    if _sum > amount:
        # revert back transaction.
        _sum -= subs[_i]
        _i += 1
    else:
        exch.append(subs[_i])
"""
else:
    print("cannot find currency for exchange.")
"""

if exch:
    print("Exchange results are -> ", ",".join(str(x) for x in exch))
    

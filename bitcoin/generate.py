#! /usr/bin/env python
from pycoin.key import Key, BIP32Node

import os
private_key = os.getenv('PK', os.urandom(32).encode('hex'))

print '===private_key==='
print private_key
the_key = Key(secret_exponent=int(private_key, 16))

master_key = BIP32Node.BIP32Node.from_master_secret(bytes(the_key.wif().encode('ascii')), 'BTC')

the_address = master_key.address()
print '===withdraw address==='
print the_address

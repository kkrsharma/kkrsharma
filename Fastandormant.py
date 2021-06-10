# -*- coding: utf-8 -*-
"""
@author: iceland
"""

import bit
import time
import hashlib
from bitcoinlib.encoding import addr_bech32_to_pubkeyhash, change_base

################ Used Functions #############################
def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()  # 6% faster than bit.crypto

def bech32_to_hash160(address):
    return change_base(addr_bech32_to_pubkeyhash(address), 256, 16)

################# Initialization Phase #########################
print("\n-----------------------Starting------------------------------------\
      \nThis program can check 5 Types of Address.\
      \n[Legacy Compressed BTC, Legacy UnCompressed BTC, Segwit BTC, Bech32 BTC and Legacy LTC]")

with open('sample.txt') as f:
        btc_list = f.read().rstrip('\n').split('\n')
print('\nLoaded ' + str(len(btc_list)) +' address from file')

################ Preparation Phase #############################
legacy_btc_list = [x for x in btc_list if x[0] == '1']  # BTC Legacy Address
segwit_btc_list = [x for x in btc_list if x[0] == '3']  # BTC Segwit Address
bech32_btc_list = [x for x in btc_list if x[0] == 'b' and len(x) < 45]      # BTC bech32. ignore multisig address.

Legacy_ltc_list = [x for x in btc_list if x[0] in {'L','M'} and len(x) < 35]  # LTC Legacy Address

print(str(len(legacy_btc_list))+' Legacy BTC, '
      +str(len(segwit_btc_list))+ ' Segwit BTC, '
      +str(len(bech32_btc_list))+' bech32 BTC, '
      +str(len(Legacy_ltc_list))+' Legacy LTC address found in the file')

print('\nIgnored : '+str(len(btc_list)-len(legacy_btc_list)-len(segwit_btc_list)-len(bech32_btc_list)
    -len(Legacy_ltc_list)) +' Address. (Improper format or multisig address with more than 1 key.)\n')

print('Convert dormant address of all coins to Hash160 for faster lookup')
print('-------------------------------------------------------------------')
h160_list = [bit.base58.b58decode_check(address)[1:].hex() for address in legacy_btc_list]
h160_list.extend([bit.base58.b58decode_check(address)[1:].hex() for address in segwit_btc_list])
h160_list.extend([bech32_to_hash160(address) for address in bech32_btc_list])
h160_list.extend([bit.base58.b58decode_check(address)[1:].hex() for address in Legacy_ltc_list])
h160_list = set(h160_list)

################ Computation Phase #############################

st = time.time()
k = 1

while True:
    priv = bit.Key()
    cpub = priv.public_key
    upub = priv._pk.public_key.format(compressed=False)
    crmd = HASH160(cpub)
    urmd = HASH160(upub)
    segwit_rmd = HASH160(b'\x00\x14' + crmd)
    
    if crmd.hex() in h160_list or urmd.hex() in h160_list or segwit_rmd.hex() in h160_list:
        print("Matching Key ==== Found!!!\n PrivateKey: " + priv.to_wif())

        f=open(u"winner.txt","a")
        f.write('\nPrivateKey (hex): ' + priv.to_hex())
        f.write('\nPrivateKey (wif): ' + priv.to_wif())
        f.write('\n==================================')
        f.close()
        break
    else:
        if (k % 50000) == 0:
            print("Searching for match...")
            print(" PrivateKey: " + priv.to_hex() + "\n BTC Address: " + priv.address)
            print ('  {:0.2f} Address/s    :: Total Address Searched: {}'.format(3*k/(time.time() - st), 3*k), end='\r')
    k += 1


        

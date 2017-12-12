# -*- coding: utf-8 -*-
import json
from pycoin.tx.Tx import Spendable
from pycoin.serialize import h2b, b2h, h2b_rev
from pycoin.tx.tx_utils import create_signed_tx
from pycoin.convention import btc_to_satoshi, satoshi_to_btc
from pycoin.tx.pay_to import build_p2sh_lookup
from pycoin.services.agent import request, urlencode, urlopen
from pycoin.key import Key, BIP32Node

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--netcode", type=str, required=True, help='netcode: BTC/LTC/XTN/...')
parser.add_argument("--target", type=str, required=True, help='to address')
args = parser.parse_args()

to_address = args.target
private_key = 'YOUR PRIVATE KEY'
the_key = Key(secret_exponent=int(private_key, 16))
master_key = BIP32Node.BIP32Node.from_master_secret(bytes(the_key.wif().encode('ascii')), args.netcode)
from_address = master_key.address()


# that's work for insight
# TODO: 设计通用utxo
def get_speendable(address):
    URL = "%s%saddr/%s/utxo" % ('https://test-insight.bitpay.com', '/api/', from_address)
    utxos = json.loads(urlopen(URL).read().decode("utf8"))

    utxo = utxos[0]

    return Spendable(utxo['amount'], h2b(utxo.get("scriptPubKey")), h2b_rev(utxo.get("txid")), utxo.get("vout"))

amount, script_hex = get_spendable(from_address)

spendable = Spendable(amount, script_hex)
##################
# TODO: 设计amount计算
tx = create_signed_tx([spendable], [(to_address, btc_to_satoshi("0.00005")), (btc_withdraw_address, btc_to_satoshi("0.0015"))], fee=btc_to_satoshi("0.00005"),
                         wifs=[master_key.wif()],
                         netcode=args.netcode)

tx_as_hex = tx.as_hex()
print tx_as_hex
# TODO 节点选取
# url = "https://test-insight.bitpay.com/api/tx/send"
# data = urlencode(dict(rawtx=tx_as_hex)).encode("utf8")

# AGENT = 'pycoin/%s' % version
#req = request.Request(url, data=data)
#r = request.urlopen(req).read()
#print r

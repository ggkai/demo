import subprocess
import os.path

def command(*args, stdout=subprocess.PIPE):
    return subprocess.Popen(args, stdout=None, encoding="UTF8")

PORT = "8432" # 比特币节点RPC默认端口 8332，这里我们刻意避开了此端口

BASE = "/Users/guokai/Library/Application Support/Bitcoin"
DATA_AREA = os.path.join(BASE, "regtest") # regtest 是bitcoin默认的手动挖块选项，用于开发环境
os.makedirs(DATA_AREA, exist_ok=True)

CONFIG = os.path.join(DATA_AREA, "regtest.conf")
with open(CONFIG, "w+") as conf:
    conf.write("""
server=1
rpcbind=0.0.0.0
rpcuser=bitcoin
rpcpassword=bitcoin
rpcport=8432
txindex=1
""".strip())


command("bitcoind", "-regtest", '-datadir={}'.format(DATA_AREA), '-conf={}'.format(CONFIG))

command('bitcoin-cli','-regtest','-getinfo')



'''



command('bitcoin-li','-regtest','getbalance')

command('bitcoin-cli','-regtest','generate','15')

command('bitcoin-li','-regtest','getbalance')

command('bitcoin-cli','-regtest','generate','86')

command('bitcoin-li','-regtest','getbalance')


#构造交易
def cli(*args):
    cmd = ["bitcoin-cli", "-regtest", "-rpcport=8432", "-rpcuser=bitcoin", "-rpcpassword=bitcoin"]
    cmd += list(args)
    process = command(*cmd)
    process.wait()
    return process.stdout.read().strip()
addr = cli("getnewaddress")
print(addr)



txid = cli("sendtoaddress", addr, "10.00")
print(txid)

tx = cli("getrawtransaction", txid, "1")
print(tx)


import json

result = json.loads(cli("listunspent"))
utxo = result[-6]
print(utxo)

addr0 = cli("getnewaddress")
print(addr0)


vin = json.dumps([{"txid":utxo["txid"], "vout":utxo["vout"]}])
vout = json.dumps({addr0:49.9999})
print(vin)
print(vout)

rawtx = cli("createrawtransaction", vin, vout)
print(rawtx)


tx = cli("decoderawtransaction", rawtx)
print(tx)

signed = json.loads(cli("signrawtransaction", rawtx))
print(signed)


#广播
new_txid = cli("sendrawtransaction", signed["hex"])
print(new_txid)


result = cli("generate", "1")
print(result)



#离线签名



#多重签名



'''
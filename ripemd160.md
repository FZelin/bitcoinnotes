ripemd160 python code




```python

def hash160(data):
     ripemd160 = hashlib.new('ripemd160')
     ripemd160.update(sha256(data)).digest()
     return ripemd160.hexdigest()

```

处理data之前需要对原数据进行byte转换

scriptSig :        15686176652066756e2073746179696e6720706f6f72

scriptPubKey:      15686176652066756e2073746179696e6720706f6f7287



```python

data = bytes.fromhex('15686176652066756e2073746179696e6720706f6f7287')

```



如何获取p2sh address
以原始script为例

origin script : 

     data = 176567616d6965727020676e697473657265746e69206e41a820a966e2ccbbcd3814c8f913abcb1c4d487d63f23d93667c186b00a5a9181fd7b5887693010287

1.对原始代码进行 sha256 处理

     sha256(data) = baa4236c5fc29284e6602278919985ea0e8b248caffca6218fe38546ab6da8da

2.对获取的sha256进行 ripemd160 处理得到 importdata

     importdata = ripemd10(sha256(data)) = fdf552e53cf30ec311f96fd009458e03bb88906c
     
3.将得到的数据 importdata 插入到 OP_HASH160  OP_EQUAL 之间 得到 scriptPubKey （[OPCode](https://github.com/bitcoin/bitcoin/blob/master/src/script/script.h "OPCODE")）

     OP_HASH160 = 0xa9
     OP_EQUAL   = 0x87
     importdata = fdf552e53cf30ec311f96fd009458e03bb88906c //在添加进数据前需要对其长度进行标识，并放置在最前面
     scriptPubKey = a9                14                fdf552e53cf30ec311f96fd009458e03bb88906c      87
                    ^                 ^                 ^                                             ^ 
                    OP_HASH160    len(importdata)     importdata                                     OP_EQUAL

     scriptPubKey = a914fdf552e53cf30ec311f96fd009458e03bb88906c87


5.将p2sh版本前缀加入到 第二步 数据的 最前面得到 可以在 [P2SH version byte](https://en.bitcoin.it/wiki/List_of_address_prefixes "version byte") 查看相关

     Script hash (P2SH address MainNet) = 0x05
     Script hash (P2SH address TestNet/RegTest) = 0xc4
     //测试网和主网的编号不一样
     c4fdf552e53cf30ec311f96fd009458e03bb88906c

6.对第5步结果进行 checksum 处理

  Calculate the checksum = sha256(sha256(version byte || scripthash ))

     what is checksum?  //就是对数据进行两次sha256处理

     sha256(sha256(c4fdf552e53cf30ec311f96fd009458e03bb88906c)) = 012b9493e2da4e101ddff81c8f74724d239dfe9a0e338fdde11284af989b4fb2

7.将第6步中前 4个 bytes 取出来，参与地址的计算

     012b9493e2da4e101ddff81c8f74724d239dfe9a0e338fdde11284af989b4fb2
     
     012b9493

8.将第5步的结果和第7步结果进行组合，用base58进行编码得到最终的地址

  Base58-encode(version byte || scripthash || first 4 bytes of checksum)

     c4fdf552e53cf30ec311f96fd009458e03bb88906c 012b9493
     base58encode(c4fdf552e53cf30ec311f96fd009458e03bb88906c012b9493)
     = 2NGQ2qDNtgH9Z86gnq9qxRnJcQbYenWusD4

     
   

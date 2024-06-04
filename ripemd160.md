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

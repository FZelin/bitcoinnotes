ripemd160 python code

```python

def hash160(data):
     ripemd160 = hashlib.new('ripemd160')
     ripemd160.update(sha256(data)).digest()
     return ripemd160.hexdigest()

```
s

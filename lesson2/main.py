from coincurve import PrivateKey, PublicKey

#1 fing the public point of a privkey
def find_public_point(priv_int):
  return PrivateKey.from_int(priv_int).public_key.point()

# Compressed Key
def find_compressed_key(priv_int):
  return PrivateKey.from_int(priv_int).public_key.format().hex()

# Uncompressed Key
def find_uncompressed_key(priv_int):
  point = find_pubkey_point(priv_int)
  x_int = point[0]
  y_int = point[1]
  return (bytes([0x04]) + x_int.to_bytes(32, 'big') + y_int.to_bytes(32, 'big')).hex()

#
def point_to_compressed(point):
  x, y = point   
  parity_byte = 0x02 if y % 2 == 0 else 0x03
  return (bytes([parity_byte]) + x.to_bytes(32, 'big')).hex()

#
def compressd_to_point(compressed_key):
  

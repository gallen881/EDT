import os
from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad


class Encrypt:
    def des_cbc(plain: bytes, key: bytes, iv) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_CBC, iv=iv)

        cipher = des.encrypt(pad(plain, DES.block_size))

        des = DES.new(key=key, mode=DES.MODE_CBC, iv=iv)
        assert plain == unpad(des.decrypt(cipher), DES.block_size)

        return cipher


    def des_cfb(plain: bytes, key: bytes, iv) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_CFB, iv=iv)

        cipher = des.encrypt(plain)

        des = DES.new(key=key, mode=DES.MODE_CFB, iv=iv)
        assert plain == des.decrypt(cipher)

        return cipher

class Decrypt:
    def des_cbc(cipher: bytes, key: bytes, iv) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_CBC, iv=iv)

        plain = unpad(des.decrypt(cipher), DES.block_size)

        des = DES.new(key=key, mode=DES.MODE_CBC, iv=iv)
        assert cipher == des.encrypt(pad(plain, DES.block_size))

        return plain


    def des_cfb(cipher: bytes, key: bytes, iv) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_CFB, iv=iv)

        plain = des.decrypt(cipher)

        des = DES.new(key=key, mode=DES.MODE_CFB, iv=iv)
        assert cipher == des.encrypt(plain)

        return plain
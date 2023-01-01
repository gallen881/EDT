import os
from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad


class Encrypt:
    # DES CBC
    def des_cbc(plain: bytes, key: bytes, iv) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_CBC, iv=iv)

        cipher = des.encrypt(pad(plain, DES.block_size))

        des = DES.new(key=key, mode=DES.MODE_CBC, iv=iv)
        assert plain == unpad(des.decrypt(cipher), DES.block_size)

        return cipher


    # DES CFB
    def des_cfb(plain: bytes, key: bytes, iv) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_CFB, iv=iv)

        cipher = des.encrypt(plain)

        des = DES.new(key=key, mode=DES.MODE_CFB, iv=iv)
        assert plain == des.decrypt(cipher)

        return cipher


    # DES CTR
    def des_ctr(plain: bytes, key: bytes, iv) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_CTR, nonce=iv)

        cipher = des.encrypt(plain)

        des = DES.new(key=key, mode=DES.MODE_CTR, nonce=iv)
        assert plain == des.decrypt(cipher)

        return cipher


    #DES EAX
    def des_eax(plain: bytes, key: bytes, iv) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_EAX, nonce=iv)

        cipher = des.encrypt(plain)

        des = DES.new(key=key, mode=DES.MODE_EAX, nonce=iv)
        assert plain == des.decrypt(cipher)

        return cipher


    #DES ECB
    def des_ecb(plain: bytes, key: bytes) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_ECB)

        cipher = des.encrypt(pad(plain, DES.block_size))

        des = DES.new(key=key, mode=DES.MODE_ECB)
        assert plain == unpad(des.decrypt(cipher), DES.block_size)

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


    # DES CTR
    def des_ctr(cipher: bytes, key: bytes, iv) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_CTR, nonce=iv)

        plain = des.decrypt(cipher)

        des = DES.new(key=key, mode=DES.MODE_CTR, nonce=iv)
        assert cipher == des.encrypt(plain)

        return plain


    # DES EAX
    def des_eax(cipher: bytes, key: bytes, iv) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_EAX, nonce=iv)

        plain = des.decrypt(cipher)

        des = DES.new(key=key, mode=DES.MODE_EAX, nonce=iv)
        assert cipher == des.encrypt(plain)

        return plain


    # DES ECB
    def des_ecb(cipher: bytes, key: bytes,) -> bytes:
        des = DES.new(key=key, mode=DES.MODE_ECB)

        plain = unpad(des.decrypt(cipher), DES.block_size)

        des = DES.new(key=key, mode=DES.MODE_ECB)
        assert cipher == des.encrypt(pad(plain, DES.block_size))

        return plain
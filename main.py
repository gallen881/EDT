VERSION = '1.0.1'


print(' EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE          DDDDDDDDDDDDDDDDDDDDDD                    TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDDDDDDDDDDDDDDDDDDD                  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDDDDDDDDDDDDDDDDDDDDD                TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE         DDDDDDDD             DDDDDDDD              TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
print('EEEEEEEEE                                  DDDDDDDD               DDDDDDDD                         TTTTTTTTT             ')
print('EEEEEEEE                                   DDDDDDDD                 DDDDDDDD                       TTTTTTTTT             ')
print('EEEEEEEEE                                  DDDDDDDD                  DDDDDDDD                      TTTTTTTTT             ')
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE         DDDDDDDD                   DDDDDDDD                     TTTTTTTTT             ')
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDD                   DDDDDDDD                     TTTTTTTTT             ')
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDD                   DDDDDDDD                     TTTTTTTTT             ')
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE         DDDDDDDD                   DDDDDDDD                     TTTTTTTTT             ')
print('EEEEEEEEE                                  DDDDDDDD                  DDDDDDDD                      TTTTTTTTT             ')
print('EEEEEEEE                                   DDDDDDDD                 DDDDDDDD                       TTTTTTTTT             ')
print('EEEEEEEEE                                  DDDDDDDD               DDDDDDDD                         TTTTTTTTT             ')
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE         DDDDDDDD             DDDDDDDD                           TTTTTTTTT             ')
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDDDDDDDDDDDDDDDDDDDDD                             TTTTTTTTT             ')
print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDDDDDDDDDDDDDDDDDDD                               TTTTTTTTT             ')
print(' EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE          DDDDDDDDDDDDDDDDDDDDDD                                 TTTTTTTTT             ')
print(f'Encrypt & Decrypt Tool    v{VERSION}')


##################################################################################################################################


def print_mode(l, da=None):
    if l == 'l1':
        print('\n\n')
        print('(1): Encrypt')
        print('(2): Decrypt')
        print('(3): Help')
        print('(4): Info')
        print('(5): Exit')
    elif l == 'l2':
        print('\n')
        print('(1): DES')
        print('(2): 3DES')
        print('(3): AES')
        print('(4): ChaCha20')
        print('(5): Salsa20')
        print('(6): Blowfish')
        print('(7): Help')
        print('(8): Info')
        print('(9): Exit')
    elif l == 'l3':
        print('\n')
        print('(1): CBC')
        print('(2): CFB')
        print('(3): CTR')
        print('(4): EAX')
        print('(5): ECB')
        print('(6): OFB')
        if da == 'd':
            print('(7): Help')
            print('(8): Info')
            print('(9): Exit')
        elif da == 'a':
            print('(7): CCM')
            print('(8): GCM')
            print('(9): OCB')
            print('(10): SIV')
            print('(11): Help')
            print('(12): Info')
            print('(13): Exit')


loop = True


def info():
    print('Python 3.9.12')
    print('Author: 和泉かやと')
    print('Date: 2023/01/02')
    print(f'Version: {VERSION}')
    print('https://github.com/GallenWang/EDT')
    print('Thanks for using this tool. If it is helpful to you, please give me the star!')


def get_payload(iv: bool):
    if iv:
        path = input('file path?:')
        key = input('key?:')
        iv = input('iv/nonce?:')
        return [path, key, iv]
    else:
        path = input('file path?:')
        key = input('key?:')
        return [path, key]

import os

def check_path(path):
    if not os.path.exists(path):
        print('Wrong path')
        return False
    return True


def check_des_key(key):
    if len(key) != 8:
        print(f'Incorrect DES key length ({len(key)} bytes)')
        print('Should be 8 bytes')
        return False
    return True


def check_payload_cbc_cfb_ofb(para):
    a = check_path(para[0])
    b = check_des_key(para[1])
    c = True
    if len(para[2]) != 8:
        print(f'Incorrect DES iv length ({len(para[2])} bytes)')
        print('Should be 8 bytes')
        c = False
    if a and b and c:
        global loop
        loop = False

def check_payload_ctr(para):
    a = check_path(para[0])
    b = check_des_key(para[1])
    c = True
    if len(para[2]) >= 8:
        print(f'Incorrect DES iv length ({len(para[2])} bytes)')
        print('Should be smaller 8 bytes')
        c = False
    if a and b and c:
        global loop
        loop = False

def check_payload_eax_ecb(para):
    if check_path(para[0]) and check_des_key(para[1]):
        global loop
        loop = False


from Cryptodome.Util.Padding import pad, unpad

def encrypt(plain: bytes, enc: list, padding=None) -> bytes:
    '''
    `enc`: [enc, enc]
    `padding`: [bool, block_size]
    '''
    if padding == None:
        cipher = enc[0].encrypt(plain)
        assert plain == enc[1].decrypt(cipher)
    else:
        cipher = enc[0].encrypt(pad(plain, padding))
        assert plain == unpad(enc[1].decrypt(cipher), padding)

    return cipher

def decrypt(cipher: bytes, enc: list, padding=None) -> bytes:
    '''
    `enc`: [enc, enc]
    `padding`: [bool, block_size]
    '''
    if padding == None:
        plain = enc[0].decrypt(cipher)
        assert cipher == enc[1].encrypt(plain)
    else:
        plain = unpad(enc[0].decrypt(cipher), padding)
        assert cipher == enc[1].encrypt(pad(plain, padding))

    return plain

def rw(payload: list, enc: list, padding=None, de=None):
    with open(payload[0], 'rb') as file:
        if de == 'enc':
            result = encrypt(file.read(), enc, padding=padding)
            payload[0] += '.enc'
        elif de == 'dec':
            result = decrypt(file.read(), enc, padding=padding)
            if payload[0][-4:] == '.enc':
                payload[0] = payload[0][:-3]

    with open(payload[0], 'wb') as file:
        file.write(result)

    print('Done!')

from Cryptodome.Cipher import DES
from Cryptodome.Cipher import DES3


while True:

    print_mode('l1')
    mode = input('?:')

    if mode == '1':
        print_mode('l2')
        mode = input('?:')

        if mode == '1':
            print_mode('l3', 'd')
            mode = input('?:')

            if mode == '1':
                mode = '0'
                # enc des cbc
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_CBC, iv=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_CBC, iv=payload[2].encode())], padding=DES.block_size, de='enc')


            elif mode == '2':
                mode = '0'
                # enc des cfb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_CFB, iv=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_CFB, iv=payload[2].encode())], de='enc')

            elif mode == '3':
                mode = '0'
                # enc des ctr
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_ctr(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_CTR, nonce=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_CTR, nonce=payload[2].encode())], de='enc')

            elif mode == '4':
                mode = '0'
                # enc des eax
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_eax_ecb(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_EAX, nonce=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_EAX, nonce=payload[2].encode())], de='enc')


            elif mode == '5':
                mode = '0'
                # enc des ecb
                while loop:
                    payload = get_payload(iv=False)
                    check_payload_eax_ecb(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_ECB, iv=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_ECB)], padding=DES.block_size, de='enc')


            elif mode == '6':
                mode = '0'
                # enc des ofb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_OFB, iv=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_OFB, iv=payload[2].encode())], de='enc')


            elif mode == '9':
                break

                



    if mode == '2':
        print_mode('l2')
        mode = input('?:')

        if mode == '1':
            print_mode('l3')
            mode = input('?:')

            if mode == '1':
                mode = '0'
                # dec des cbc
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_CBC, iv=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_CBC, iv=payload[2].encode())], padding=DES.block_size, de='dec')
            
            if mode == '2':
                mode = '0'
                # dec des cfb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_CFB, iv=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_CFB, iv=payload[2].encode())], de='dec')


            elif mode == '3':
                mode = '0'
                # enc des ctr
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_ctr(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_CTR, nonce=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_CTR, nonce=payload[2].encode())], de='dec')

            elif mode == '4':
                mode = '0'
                # enc des eax
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_eax_ecb(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_EAX, nonce=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_EAX, nonce=payload[2].encode())], de='dec')

            elif mode == '5':
                mode = '0'
                # enc des ecb
                while loop:
                    payload = get_payload(iv=False)
                    check_payload_eax_ecb(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_ECB, iv=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_ECB)], padding=DES.block_size, de='dec')


            elif mode == '6':
                mode = '0'
                # enc des ofb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_cbc_cfb_ofb(payload)
                rw(payload, [DES.new(key=payload[1].encode(), mode=DES.MODE_OFB, iv=payload[2].encode()), DES.new(key=payload[1].encode(), mode=DES.MODE_OFB, iv=payload[2].encode())], de='dec')




            elif mode == '9':
                break

    elif mode == '4' or 'info' or 'version':
        info()

    elif mode == '5' or 'exit' or 'leave':
        os._exit(0)

    loop = True
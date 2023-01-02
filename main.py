VERSION = '1.2.1'


print('+——————————————————————————————————————————————————————————————+')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE         DDDDDDDDDDDDDDDDDDDDDD                    TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT  |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDDDDDDDDDDDDDDDDDDD                  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT  |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDDDDDDDDDDDDDDDDDDDDD                TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT  |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDD             DDDDDDDD              TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT  |')
print('| EEEEEEEEE                                  DDDDDDDD               DDDDDDDD                         TTTTTTTTT               |')
print('| EEEEEEEEE                                  DDDDDDDD                 DDDDDDDD                       TTTTTTTTT               |')
print('| EEEEEEEEE                                  DDDDDDDD                  DDDDDDDD                      TTTTTTTTT               |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDD                   DDDDDDDD                     TTTTTTTTT               |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDD                   DDDDDDDD                     TTTTTTTTT               |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDD                   DDDDDDDD                     TTTTTTTTT               |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDD                   DDDDDDDD                     TTTTTTTTT               |')
print('| EEEEEEEEE                                  DDDDDDDD                  DDDDDDDD                      TTTTTTTTT               |')
print('| EEEEEEEEE                                  DDDDDDDD                 DDDDDDDD                       TTTTTTTTT               |')
print('| EEEEEEEEE                                  DDDDDDDD               DDDDDDDD                         TTTTTTTTT               |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDD             DDDDDDDD                           TTTTTTTTT               |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDDDDDDDDDDDDDDDDDDDDD                             TTTTTTTTT               |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE        DDDDDDDDDDDDDDDDDDDDDDDDD                               TTTTTTTTT               |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE         DDDDDDDDDDDDDDDDDDDDDD                                 TTTTTTTTT               |')
print('+——————————————————————————————————————————————————————————————+')
print(f'Encrypt & Decrypt Tool    v{VERSION}')
import time
time.sleep(1.7)



##################################################################################################################################



import os
import colorama
from Cryptodome.Cipher import DES
from Cryptodome.Cipher import DES3
from Cryptodome.Cipher import Salsa20


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
    print('\n')
    print('Python 3.9.12')
    print('Author: 和泉かやと')
    print('Date: 2023/01/02')
    print(f'Version: {VERSION}')
    print('https://github.com/GallenWang/EDT')
    print('Thanks for using this tool. If it is helpful to you, please give me the star!')


def get_payload(iv: bool):
    if iv:
        path = input('file path?:')
        key = input('key?:').encode()
        iv = input('iv/nonce?:').encode()
        return [path, key, iv]
    else:
        path = input('file path?:')
        key = input('key?:').encode()
        return [path, key]


def check_path(path: str):
    if not os.path.exists(path):
        print(colorama.Fore.RED, 'Wrong path', colorama.Fore.RESET)
        return False
    return True


def check_des_key(key: bytes):
    if len(key) != DES.key_size:
        print(f'{colorama.Fore.RED}Incorrect DES key length ({len(key)} bytes)')
        print(f'Should be {DES.key_size} bytes', colorama.Fore.RESET)
        return False
    return True

def check_3des_key(key: bytes):
    if len(key) not in  DES3.key_size:
        print(f'{colorama.Fore.RED}Incorrect DES key length ({len(key)} bytes)')
        print(f'Should be {DES3.key_size[0]} or {DES3.key_size[1]} bytes{colorama.Fore.RESET}')
        return False
    return True


def check_payload_cbc_cfb_ofb(payload, d3):
    a = check_path(payload[0])
    if d3 == 'd':
        b = check_des_key(payload[1])
    elif d3 == 'ddd':
        b = check_3des_key(payload[1])
    c = True
    if len(payload[2]) != 8:
        print(f'{colorama.Fore.RED}Incorrect DES iv length ({len(payload[2])} bytes)')
        print('Should be 8 bytes', colorama.Fore.RESET)
        c = False
    if a and b and c:
        global loop
        loop = False

def check_payload_ctr(payload, d3):
    a = check_path(payload[0])
    if d3 == 'd':
        b = check_des_key(payload[1])
    elif d3 == 'ddd':
        b = check_3des_key(payload[1])
    c = True
    if len(payload[2]) >= 8:
        print(f'{colorama.Fore.RED}Incorrect DES iv length ({len(payload[2])} bytes)')
        print('Should be smaller 8 bytes', colorama.Fore.RESET)
        c = False
    if a and b and c:
        global loop
        loop = False

def check_payload_eax_ecb(payload, d3):
    a = check_path(payload[0])
    if d3 == 'd':
        b = check_des_key(payload[1])
    elif d3 == 'ddd':
        b = check_3des_key(payload[1])
    if a and b:
        global loop
        loop = False

def check_payload_salsa20(payload):
    a = check_path(payload[0])
    b = len(payload[1]) in Salsa20.key_size
    c = len(payload[2]) == 8
    if a and b and c:
        global loop
        loop = False
    else:
        if not b:
            print(f'{colorama.Fore.RED}Incorrect Salsa20 key length ({len(payload[1])} bytes)')
            print(f'Should be {Salsa20.key_size[0]} or {Salsa20.key_size[1]} bytes{colorama.Fore.RESET}')
        if not c:
            print(f'{colorama.Fore.RED}Incorrect Salsa20 iv length ({len(payload[2])} bytes)')
            print('Should be 8 bytes', colorama.Fore.RESET)    


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

def rw(path: str, enc: list, padding=None, de=None):
    with open(path, 'rb') as file:
        if de == 'enc':
            result = encrypt(file.read(), enc, padding=padding)
            path += '.enc'
        elif de == 'dec':
            result = decrypt(file.read(), enc, padding=padding)
            if path[-4:] == '.enc':
                path = path[:-3]

    with open(path, 'wb') as file:
        file.write(result)

    global loop
    loop = True
    print('\n', colorama.Fore.GREEN, 'Done!', colorama.Fore.RESET)



##################################################################################################################################



try:
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
                        check_payload_cbc_cfb_ofb(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CBC, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CBC, iv=payload[2])], padding=DES.block_size, de='enc')


                elif mode == '2':
                    mode = '0'
                    # enc des cfb
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_cbc_cfb_ofb(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CFB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CFB, iv=payload[2])], de='enc')

                elif mode == '3':
                    mode = '0'
                    # enc des ctr
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_ctr(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CTR, nonce=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CTR, nonce=payload[2])], de='enc')

                elif mode == '4':
                    mode = '0'
                    # enc des eax
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_eax_ecb(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_EAX, nonce=payload[2]), DES.new(key=payload[1], mode=DES.MODE_EAX, nonce=payload[2])], de='enc')


                elif mode == '5':
                    mode = '0'
                    # enc des ecb
                    while loop:
                        payload = get_payload(iv=False)
                        check_payload_eax_ecb(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_ECB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_ECB)], padding=DES.block_size, de='enc')


                elif mode == '6':
                    mode = '0'
                    # enc des ofb
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_cbc_cfb_ofb(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_OFB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_OFB, iv=payload[2])], de='enc')


                elif mode == '9':
                    break

            elif mode == '2':
                print_mode('l3', 'd')
                mode = input('?:')

                if mode == '1':
                    mode = '0'
                    # enc 3des cbc
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_cbc_cfb_ofb(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CBC, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CBC, iv=payload[2])], padding=DES3.block_size, de='enc')


                elif mode == '2':
                    mode = '0'
                    # enc 3des cfb
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_cbc_cfb_ofb(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CFB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CFB, iv=payload[2])], de='enc')

                elif mode == '3':
                    mode = '0'
                    # enc 3des ctr
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_ctr(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CTR, nonce=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CTR, nonce=payload[2])], de='enc')

                elif mode == '4':
                    mode = '0'
                    # enc 3des eax
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_eax_ecb(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_EAX, nonce=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_EAX, nonce=payload[2])], de='enc')


                elif mode == '5':
                    mode = '0'
                    # enc 3des ecb
                    while loop:
                        payload = get_payload(iv=False)
                        check_payload_eax_ecb(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_ECB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_ECB)], padding=DES3.block_size, de='enc')


                elif mode == '6':
                    mode = '0'
                    # enc 3des ofb
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_cbc_cfb_ofb(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_OFB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_OFB, iv=payload[2])], de='enc')

            elif mode == '5':
                mode = '0'
                # salsa20
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_salsa20(payload)
                rw(payload[0], [Salsa20.new(key=payload[1], nonce=payload[2]), Salsa20.new(key=payload[1], nonce=payload[2])], de='enc')


        elif mode == '2':
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
                        check_payload_cbc_cfb_ofb(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CBC, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CBC, iv=payload[2])], padding=DES.block_size, de='dec')
                
                if mode == '2':
                    mode = '0'
                    # dec des cfb
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_cbc_cfb_ofb(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CFB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CFB, iv=payload[2])], de='dec')


                elif mode == '3':
                    mode = '0'
                    # dec des ctr
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_ctr(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CTR, nonce=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CTR, nonce=payload[2])], de='dec')

                elif mode == '4':
                    mode = '0'
                    # dec des eax
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_eax_ecb(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_EAX, nonce=payload[2]), DES.new(key=payload[1], mode=DES.MODE_EAX, nonce=payload[2])], de='dec')

                elif mode == '5':
                    mode = '0'
                    # dec des ecb
                    while loop:
                        payload = get_payload(iv=False)
                        check_payload_eax_ecb(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_ECB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_ECB)], padding=DES.block_size, de='dec')


                elif mode == '6':
                    mode = '0'
                    # dec des ofb
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_cbc_cfb_ofb(payload, 'd')
                    rw(payload[0], [DES.new(key=payload[1], mode=DES.MODE_OFB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_OFB, iv=payload[2])], de='dec')


            elif mode == '2':
                print_mode('l3')
                mode = input('?:')

                if mode == '1':
                    mode = '0'
                    # dec 3des cbc
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_cbc_cfb_ofb(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CBC, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CBC, iv=payload[2])], padding=DES3.block_size, de='dec')
                
                if mode == '2':
                    mode = '0'
                    # dec 3des cfb
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_cbc_cfb_ofb(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CFB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CFB, iv=payload[2])], de='dec')


                elif mode == '3':
                    mode = '0'
                    # dec 3des ctr
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_ctr(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CTR, nonce=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CTR, nonce=payload[2])], de='dec')

                elif mode == '4':
                    mode = '0'
                    # dec 3des eax
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_eax_ecb(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_EAX, nonce=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_EAX, nonce=payload[2])], de='dec')

                elif mode == '5':
                    mode = '0'
                    # dec 3des ecb
                    while loop:
                        payload = get_payload(iv=False)
                        check_payload_eax_ecb(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_ECB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_ECB)], padding=DES3.block_size, de='dec')


                elif mode == '6':
                    mode = '0'
                    # dec 3des ofb
                    while loop:
                        payload = get_payload(iv=True)
                        check_payload_cbc_cfb_ofb(payload, 'ddd')
                    rw(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_OFB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_OFB, iv=payload[2])], de='dec')




                elif mode == '9':
                    break


            elif mode == '5':
                mode = '0'
                # salsa20
                while loop:
                    payload = get_payload(iv=True)
                    check_payload_salsa20(payload)
                rw(payload[0], [Salsa20.new(key=payload[1], nonce=payload[2]), Salsa20.new(key=payload[1], nonce=payload[2])], de='dec')


        elif mode == '4' or mode == 'info' or mode == 'version':
            print(mode)
            info()

        elif mode == '5' or mode == 'exit' or mode == 'leave':
            os._exit(0) 

        
    

except Exception as e:
    print(colorama.Fore.RED, e, colorama.Fore.RESET)
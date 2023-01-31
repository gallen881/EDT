VERSION = '1.5.0'


print('+----------------------------------------------------------------------------------------------------------------+')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE      DDDDDDDDDDDDDDDDDDDDDD            TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDDDDDDDDDDDDDDDDDDD          TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDDDDDDDDDDDDDDDDDDDDD        TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD             DDDDDDDD      TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT |')
print('| EEEEEEEEE                               DDDDDDDD               DDDDDDDD                 TTTTTTTTT              |')
print('| EEEEEEEEE                               DDDDDDDD                 DDDDDDDD               TTTTTTTTT              |')
print('| EEEEEEEEE                               DDDDDDDD                  DDDDDDDD              TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD                   DDDDDDDD             TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD                   DDDDDDDD             TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD                   DDDDDDDD             TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD                   DDDDDDDD             TTTTTTTTT              |')
print('| EEEEEEEEE                               DDDDDDDD                  DDDDDDDD              TTTTTTTTT              |')
print('| EEEEEEEEE                               DDDDDDDD                 DDDDDDDD               TTTTTTTTT              |')
print('| EEEEEEEEE                               DDDDDDDD               DDDDDDDD                 TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDD             DDDDDDDD                   TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDDDDDDDDDDDDDDDDDDDDD                     TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE     DDDDDDDDDDDDDDDDDDDDDDDDD                       TTTTTTTTT              |')
print('| EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE      DDDDDDDDDDDDDDDDDDDDDD                         TTTTTTTTT              |')
print('+----------------------------------------------------------------------------------------------------------------+')
print(f'Encrypt & Decrypt Tool    v{VERSION}')
import time
time.sleep(0.9)



##################################################################################################################################



import os
from Cryptodome.Cipher import DES
from Cryptodome.Cipher import DES3
from Cryptodome.Cipher import AES
from Cryptodome.Cipher import ChaCha20
from Cryptodome.Cipher import Salsa20


def print_selection(l, da=None):
    if l == 'l1':
        print('\n\n')
        print('[1]: Encrypt')
        print('[2]: Decrypt')
        print('[3]: Help')
        print('[4]: Info')
        print('[5]: Exit')
    elif l == 'l2':
        print('\n')
        print('[1]: DES')
        print('[2]: 3DES')
        print('[3]: AES')
        print('[4]: ChaCha20')
        print('[5]: Salsa20')
        print('[6]: Blowfish (not working)')
        print('[7]: Help')
        print('[8]: Info')
        print('[9]: Exit')
    elif l == 'l3':
        print('\n')
        print('[1]: CBC')
        print('[2]: CFB')
        print('[3]: CTR')
        print('[4]: EAX')
        print('[5]: ECB')
        print('[6]: OFB')
        if da == 'd':
            print('[7]: Help')
            print('[8]: Info')
            print('[9]: Exit')
        elif da == 'a':
            print('[7]: CCM')
            print('[8]: GCM')
            print('[9]: OCB')
            print('[10]: Help')
            print('[11]: Info')
            print('[12]: Exit')


loop = True


def info():
    print('\n')
    print('Python 3.9.12')
    print('Author: 和泉かやと')
    print('Date: 2023/01/02')
    print(f'Version: {VERSION}')
    print('https://github.com/GallenWang/EDT')
    print('Thanks for using this tool. If it is helpful to you, please give me the star!')

def help():
    print('''
1. Select mode
    e.g. [1]: Encrypt
         [2]: Decrypt
         [3]: Help
         [4]: Info
         [5]: Exit

         For showing this message, you should type "3".

2. Enter path
    If the file not found, return "Wrong path".

3. Enter key
    If the key is illegal, raise error.

4. Enter iv/nonce
    Some mode does not require iv/nonce.
    If the iv/nonce is illegal, raise error.

5. This tools is not a malware, if your antivirus blocks this tool, you should stop your antivirus.

6. Go to https://github.com/GallenWang/EDT for update and more informations.''')


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


def check_path(path: str) -> bool:
    if not os.path.exists(path):
        print('Wrong path')
        return False
    return True


def check_des_key(key: bytes) -> bool:
    if len(key) != DES.key_size:
        print(f'Incorrect DES key length ({len(key)} bytes)')
        print(f'Should be {DES.key_size} bytes')
        return False
    return True

def check_3des_key(key: bytes) -> bool:
    if len(key) not in  DES3.key_size:
        print(f'Incorrect DES key length ({len(key)} bytes)')
        print('Should be', end=' ')
        count = 0
        for i in DES3.key_size:
            if count == len(DES3.key_size) - 2:
                print(i, end=' or ')
            elif count == len(DES3.key_size) - 1:
                print(i, end=' Bytes\n')
            else:
                print(i, end=', ')
            count += 1
        return False
    return True

def check_aes_key(key: bytes) -> bool:
    if len(key) not in AES.key_size:
        print(f'Incorrect AES key length ({len(key)} bytes)')
        print('Should be', end=' ')
        count = 0
        for i in AES.key_size:
            if count == len(AES.key_size) - 2:
                print(i, end=' or ')
            elif count == len(AES.key_size) - 1:
                print(i, end=' bytes\n')
            else:
                print(i, end=', ')
            count += 1
        return False
    return True

def check_chacha20_key(key: bytes) -> bool:
    if len(key) != ChaCha20.key_size:
        print(f'Incorrect ChaCha20 key length ({len(key)} bytes)')
        print(f'Should be {ChaCha20.key_size} bytes')
        return False
    return True

def check_chacha20_iv(iv: bytes) -> bool:
    if len(iv) in [8, 12, 24]:
        print(f'Incorrect ChaCha20 iv length ({len(payload[2])} bytes)')
        print('Should be 8, 12 or 24 bytes')
        return False
    return True

def check_salsa20_key(key: bytes) -> bool:
    if len(key) in Salsa20.key_size:
        print(f'Incorrect Salsa20 key length ({len(key)} bytes)')
        print(f'Should be {Salsa20.key_size[0]} or {Salsa20.key_size[1]} bytes')
        return False
    return True

def check_salsa20_iv(iv: bytes) -> bool:
    if len(iv) == 8:
        print(f'Incorrect Salsa20 iv length ({len(payload[2])} bytes)')
        print('Should be 8 bytes')
        return False
    return True


def check_payload(payload, mode: list):
    a = check_path(payload[0])
    if mode[0] in ['des', '3des']:
        if mode[0] == 'des':
            b = check_des_key(payload[1])
        elif mode[0] == '3des':
            b = check_3des_key(payload[1])
        c = True
        if mode[1] in ['cbc', 'cfb', 'ofb']:
            if len(payload[2]) != 8:
                print(f'Incorrect DES/3DES iv length ({len(payload[2])} bytes)')
                print('Should be 8 bytes')
                c = False
        elif mode[1] == 'ctr':
            if len(payload[2]) >= 8:
                print(f'Incorrect DES/3DES iv length ({len(payload[2])} bytes)')
                print('Should be smaller 8 than bytes')
                c = False
        elif mode[1] in ['eax', 'ecb']:
            pass

    elif mode[0] == 'aes':
        b = check_aes_key(payload[1])
        c = True
        if mode[1] in ['cbc', 'cfb', 'ofb']:
            if len(payload[2]) != 16:
                print(f'Incorrect AES iv length ({len(payload[2])} bytes)')
                print('Should be 16 bytes')
                c = False
        elif mode[1] in ['ctr', 'ocb']:
            if len(payload[2]) >= 16:
                print(f'Incorrect AES iv length ({len(payload[2])} bytes)')
                print('Should be smaller than 16 bytes')
                c = False
        elif mode[1] == 'ccm':
            if len(payload[2]) < 7 or len(payload[2]) > 13:
                print(f'Incorrect AES iv length ({len(payload[2])} bytes)')
                print('Should be 7~13 bytes')
                c = False
        elif mode[1] in ['eax', 'ecb', 'gcm']:
            pass

    elif mode[0] == 'chacha20':
        b = check_chacha20_key(payload[1])
        c = check_chacha20_iv(payload[2])

    elif mode[0] == 'salsa20':
        b = check_salsa20_key(payload[1])
        c = check_salsa20_iv(payload[2])

    elif mode[0] == 'blowfish':
        pass

    if a and b and c:
        global loop
        loop = False



from Cryptodome.Util.Padding import pad, unpad

class EncDec:
    def __init__(self, path: str, enc: list, padding=None):
        self.path = path
        self.enc = enc
        self.padding = padding


    def loop_control(self):
        global loop
        loop = True
        print('\nDone!')


    def encrypt(self) -> bytes:
        '''
        `enc`: [enc, enc]
        `padding`: [bool, block_size]
        '''
        with open(self.path, 'rb') as file:
            self.plain = file.read()

        if self.padding == None:
            self.cipher = self.enc[0].encrypt(self.plain)
            assert self.plain == self.enc[1].decrypt(self.cipher)
        else:
            self.cipher = self.enc[0].encrypt(pad(self.plain, self.padding))
            assert self.plain == unpad(self.enc[1].decrypt(self.cipher), self.padding)

        with open(f'{self.path}.enc', 'wb') as file:
            file.write(self.cipher)

        self.loop_control()

        return self.cipher

    def decrypt(self) -> bytes:
        '''
        `enc`: [enc, enc]
        `padding`: [bool, block_size]
        '''
        with open(self.path, 'rb') as file:
            self.cipher = file.read()

        if self.padding == None:
            self.plain = self.enc[0].decrypt(self.cipher)
            assert self.cipher == self.enc[1].encrypt(self.plain)

        else:
            self.plain = unpad(self.enc[0].decrypt(self.cipher), self.padding)
            assert self.cipher == self.enc[1].encrypt(pad(self.plain, self.padding))

        if self.path.endswith('.enc'):
            self.path = self.path[:-3]
        with open(self.path, 'wb') as file:
            file.write(self.plain)
        
        self.loop_control()

        return self.plain



##################################################################################################################################



while True:
    try:
        print_selection('l1')
        selection = input('?:')

        if selection == '1':
            enc_or_dec = 'enc'
        elif selection == '2':
            enc_or_dec = 'dec'
        elif selection in ['3', 'help']:
            help()
            continue
        elif selection == '4' or selection == 'info' or selection == 'version':
            print(selection)
            info()
            continue
        elif selection == '5' or selection == 'exit' or selection == 'leave':
            os._exit(0)

        print_selection('l2')
        selection = input('?:')

        if selection == '1':
            print_selection('l3', 'd')
            selection = input('?:')

            if selection == '1':
                selection = '0'
                # des cbc
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['des', 'cbc'])
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CBC, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CBC, iv=payload[2])], padding=DES.block_size)

                    

            elif selection == '2':
                selection = '0'
                # des cfb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['des', 'cfb'])
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CFB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CFB, iv=payload[2])])


            elif selection == '3':
                selection = '0'
                # des ctr
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['des', 'ctr'])
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_CTR, nonce=payload[2]), DES.new(key=payload[1], mode=DES.MODE_CTR, nonce=payload[2])])


            elif selection == '4':
                selection = '0'
                # des eax
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['des', 'eax'])
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_EAX, nonce=payload[2]), DES.new(key=payload[1], mode=DES.MODE_EAX, nonce=payload[2])])


            elif selection == '5':
                selection = '0'
                # des ecb
                while loop:
                    payload = get_payload(iv=False)
                    check_payload(payload, ['des', 'ecb'])
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_ECB), DES.new(key=payload[1], mode=DES.MODE_ECB)], padding=DES.block_size)


            elif selection == '6':
                selection = '0'
                # des ofb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['des', 'ofb'])
                file = EncDec(payload[0], [DES.new(key=payload[1], mode=DES.MODE_OFB, iv=payload[2]), DES.new(key=payload[1], mode=DES.MODE_OFB, iv=payload[2])])


            elif selection in ['7', 'help']:
                help()
                enc_or_dec = None

            elif selection in ['8', 'info', 'version']:
                info()
                enc_or_dec = None

            elif selection in ['9', 'exit', 'leave']:
                enc_or_dec = None
                break

        elif selection == '2':
            print_selection('l3', 'd')
            selection = input('?:')

            if selection == '1':
                selection = '0'
                # 3des cbc
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['3des', 'cbc'])
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CBC, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CBC, iv=payload[2])], padding=DES3.block_size)


            elif selection == '2':
                selection = '0'
                # 3des cfb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['3des', 'cfb'])
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CFB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CFB, iv=payload[2])])


            elif selection == '3':
                selection = '0'
                # 3des ctr
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['3des', 'ctr'])
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_CTR, nonce=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_CTR, nonce=payload[2])])


            elif selection == '4':
                selection = '0'
                # 3des eax
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['3des', 'eax'])
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_EAX, nonce=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_EAX, nonce=payload[2])])


            elif selection == '5':
                selection = '0'
                # 3des ecb
                while loop:
                    payload = get_payload(iv=False)
                    check_payload(payload, ['3des', 'ecb'])
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_ECB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_ECB)], padding=DES3.block_size)


            elif selection == '6':
                selection = '0'
                # 3des ofb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['3des', 'ofb'])
                file = EncDec(payload[0], [DES3.new(key=payload[1], mode=DES3.MODE_OFB, iv=payload[2]), DES3.new(key=payload[1], mode=DES3.MODE_OFB, iv=payload[2])])


            elif selection in ['7', 'help']:
                help()
                enc_or_dec = None

            elif selection in ['8', 'info', 'version']:
                info()
                enc_or_dec = None

            elif selection in ['9', 'exit', 'leave']:
                enc_or_dec = None
                break

        if selection == '3':
            print_selection('l3', 'a')
            selection = input('?:')

            if selection == '1':
                selection = '0'
                # aes cbc
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['aes', 'cbc'])
                file = EncDec(payload[0], [AES.new(key=payload[1], mode=AES.MODE_CBC, iv=payload[2]), AES.new(key=payload[1], mode=AES.MODE_CBC, iv=payload[2])], padding=AES.block_size)

                    

            elif selection == '2':
                selection = '0'
                # aes cfb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['aes', 'cfb'])
                file = EncDec(payload[0], [AES.new(key=payload[1], mode=AES.MODE_CFB, iv=payload[2]), AES.new(key=payload[1], mode=AES.MODE_CFB, iv=payload[2])])


            elif selection == '3':
                selection = '0'
                # aes ctr
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['aes', 'ctr'])
                file = EncDec(payload[0], [AES.new(key=payload[1], mode=AES.MODE_CTR, nonce=payload[2]), AES.new(key=payload[1], mode=AES.MODE_CTR, nonce=payload[2])])


            elif selection == '4':
                selection = '0'
                # aes eax
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['aes', 'eax'])
                file = EncDec(payload[0], [AES.new(key=payload[1], mode=AES.MODE_EAX, nonce=payload[2]), AES.new(key=payload[1], mode=AES.MODE_EAX, nonce=payload[2])])


            elif selection == '5':
                selection = '0'
                # aes ecb
                while loop:
                    payload = get_payload(iv=False)
                    check_payload(payload, ['aes', 'ecb'])
                file = EncDec(payload[0], [AES.new(key=payload[1], mode=AES.MODE_ECB, iv=payload[2]), AES.new(key=payload[1], mode=AES.MODE_ECB)], padding=AES.block_size)


            elif selection == '6':
                selection = '0'
                # aes ofb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['aes', 'ofb'])
                file = EncDec(payload[0], [AES.new(key=payload[1], mode=AES.MODE_OFB, iv=payload[2]), AES.new(key=payload[1], mode=AES.MODE_OFB, iv=payload[2])])


            elif selection == '7':
                selection = '0'
                # aes ccm
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['aes', 'ccm'])
                file = EncDec(payload[0], [AES.new(key=payload[1], mode=AES.MODE_CCM, nonce=payload[2]), AES.new(key=payload[1], mode=AES.MODE_CCM, nonce=payload[2])])


            elif selection == '8':
                selection = '0'
                # aes gcm
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['aes', 'gcm'])
                file = EncDec(payload[0], [AES.new(key=payload[1], mode=AES.MODE_GCM, nonce=payload[2]), AES.new(key=payload[1], mode=AES.MODE_GCM, nonce=payload[2])])


            elif selection == '9':
                selection = '0'
                # aes ocb
                while loop:
                    payload = get_payload(iv=True)
                    check_payload(payload, ['aes', 'ocb'])
                file = EncDec(payload[0], [AES.new(key=payload[1], mode=AES.MODE_OCB, nonce=payload[2]), AES.new(key=payload[1], mode=AES.MODE_OCB, nonce=payload[2])], padding=AES.block_size)


            elif selection in ['10', 'help']:
                help()
                enc_or_dec = None

            elif selection in ['11', 'info', 'version']:
                info()
                enc_or_dec = None

            elif selection in ['12', 'exit', 'leave']:
                enc_or_dec = None
                break

        elif selection == '4':
            selection = '0'
            # chacha20
            while loop:
                payload = get_payload(iv=True)
                check_payload(payload, ['chacha20', None])
            file = EncDec(payload[0], [ChaCha20.new(key=payload[1], nonce=payload[2]), ChaCha20.new(key=payload[1], nonce=payload[2])])


        elif selection == '5':
            selection = '0'
            # salsa20
            while loop:
                payload = get_payload(iv=True)
                check_payload(payload, ['salsa20', None])
            file = EncDec(payload[0], [Salsa20.new(key=payload[1], nonce=payload[2]), Salsa20.new(key=payload[1], nonce=payload[2])])


        elif selection in ['7', 'help']:
            help()
            enc_or_dec = None

        elif selection in ['8', 'info', 'version']:
            info()
            enc_or_dec = None
        elif selection in ['9', 'exit', 'leave']:
            enc_or_dec = None
            break


        if enc_or_dec == 'enc':
            file.encrypt()
        elif enc_or_dec == 'dec':
            file.decrypt()

    except Exception as e:
        print(e)
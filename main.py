VERSION = '1.0.0'


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



def get_parameter(iv: bool):
    if iv:
        path = input('file path?:')
        key = input('key?:')
        iv = input('iv?:')
        return [path, key, iv]
    else:
        path = input('file path?:')
        key = input('key?:')
        return [path, key]


import EDT


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
                while True:
                    data = get_parameter(iv=True)
                    if len(data[1]) != 8:
                        print(f'Incorrect DES key length ({len(data[1])} bytes)')
                        print('Should be 8 bytes')
                    elif len(data[2]) != 8:
                        print(f'Incorrect DES iv length ({len(data[2])} bytes)')
                        print('Should be 8 bytes')
                    else:
                        break
                with open(data[0], 'rb') as file:
                    file = file.read()
                cipher = EDT.Encrypt.des_cbc(file, data[1].encode(), data[2].encode())
                with open(f'{data[0]}.enc', 'wb') as file:
                    file.write(cipher)

            elif mode == '2':
                mode = '0'
                # enc des cfb
                while True:
                    data = get_parameter(iv=True)
                    if len(data[1]) != 8:
                        print(f'Incorrect DES key length ({len(data[1])} bytes)')
                        print('Should be 8 bytes')
                    elif len(data[2]) != 8:
                        print(f'Incorrect DES iv length ({len(data[2])} bytes)')
                        print('Should be 8 bytes')
                    else:
                        break
                with open(data[0], 'rb') as file:
                    file = file.read()
                cipher = EDT.Encrypt.des_cfb(file, data[1].encode(), data[2].encode())
                with open(f'{data[0]}.enc', 'wb') as file:
                    file.write(cipher) 

                



    if mode == '2':
        print_mode('l2')
        mode = input('?:')

        if mode == '1':
            print_mode('l3')
            mode = input('?:')

            if mode == '1':
                mode = '0'
                # dec des cbc
                while True:
                    data = get_parameter(iv=True)
                    if len(data[1]) != 8:
                        print(f'Incorrect DES key length ({len(data[1])} bytes)')
                        print('Should be 8 bytes')
                    elif len(data[2]) != 8:
                        print(f'Incorrect DES iv length ({len(data[2])} bytes)')
                        print('Should be 8 bytes')
                    else:
                        break
                with open(data[0], 'rb') as file:
                    file = file.read()
                plain = EDT.Decrypt.des_cbc(file, data[1].encode(), data[2].encode())
                if data[0][-4:] == '.enc':
                    data[0] = data[0][:-3]
                with open(f'{data[0]}', 'wb') as file:
                    file.write(plain)
            
            if mode == '2':
                mode = '0'
                # dec des cfb
                while True:
                    data = get_parameter(iv=True)
                    if len(data[1]) != 8:
                        print(f'Incorrect DES key length ({len(data[1])} bytes)')
                        print('Should be 8 bytes')
                    elif len(data[2]) != 8:
                        print(f'Incorrect DES iv length ({len(data[2])} bytes)')
                        print('Should be 8 bytes')
                    else:
                        break
                with open(data[0], 'rb') as file:
                    file = file.read()
                plain = EDT.Decrypt.des_cfb(file, data[1].encode(), data[2].encode())
                if data[0][-4:] == '.enc':
                    data[0] = data[0][:-3]
                with open(f'{data[0]}', 'wb') as file:
                    file.write(plain)




    print('Done!')
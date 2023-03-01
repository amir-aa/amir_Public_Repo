def sbox_lookup(bits):
    sbox = [
        # S-box decimal
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ]
    row = int(bits[0] + bits[5], 2)
    col = int(bits[1:5], 2)
    return sbox[row][col]

def sbox_lookup_bin(bits):
    sbox = [
        # S-box 01
        ['1110', '0100', '1101', '0001', '0010', '1111', '1011', '1000',
         '0011', '1010', '0110', '1100', '0101', '1001', '0000', '0111'],
        ['0000', '1111', '0111', '0100', '1110', '0010', '1101', '0001',
         '1010', '0110', '1100', '1011', '1001', '0101', '0011', '1000'],
        ['0100', '0001', '1110', '1000', '1101', '0110', '0010', '1011',
         '1111', '1100', '1001', '0111', '0011', '1010', '0101', '0000'],
        ['1111', '1100', '1000', '0010', '0100', '1001', '0001', '0111',
         '0101', '1011', '0011', '1110', '1010', '0000', '0110', '1101'],
    ]
    print(bits)
    row = int(bits[0] + bits[5], 2)
    col = int(bits[1:5], 2)
    return str(sbox[row][col])# for decimal result =>int(sbox[row][col],2)

def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] >> shift) & 0x1
def Zero_Padding(bitsarray:list):
    if len(bitsarray)%6==0:
        return bitsarray # return it self if it is divisible by 6
    while not len(bitsarray)%6==0:
        bitsarray.append(0)
        print('ZeroAdded')
    return bitsarray
def Convert_to_bits(bytearray:bytes):
    bitslist=[access_bit(data,i) for i in range(len(data)*8)]
    return Zero_Padding(bitslist)
def Convert_to_bytes(bitsarray:list[int]):
    bitslist2=[int(i) for i in list(''.join(result))]

    byteslist = [sum([byte[b] << b for b in range(0,8)])
                for byte in zip(*(iter(bitslist2),) * 8)
            ]
    return bytes(byteslist)

def sbox(bitsarray:list):
    i=0
    result=[]
    while i < len(bitsarray)//6:
        startindex=6*i
        endindex=6*(i+1)
        
        inp=''.join(map(str, bitsarray[startindex:endindex]))
        result.append(sbox_lookup_bin(inp))
        i+=1
    return result

data=b'HeyThis is My Program!'


result=sbox(Convert_to_bits(data))
print(result)
print(Convert_to_bytes(result))
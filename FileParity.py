def calculate_even_parity_from_file(file_path):
 
    result = []
    with open(file_path, 'rb') as file:
        while True:
            byte = file.read(1)
            if not byte:
                break
            byte_value = int.from_bytes(byte, byteorder='big')
            parity = 0
            for i in range(8):
                if (byte_value >> i) & 1:
                    parity += 1
            if parity % 2 == 0:
                result.append((byte_value, 'Even'))
            else:
                result.append((byte_value, 'Odd'))
    return result


file_path = 'path_to_your_file'  
parity_results = calculate_even_parity_from_file(file_path)
for byte, parity in parity_results:
    print(f"Byte {byte}: Parity - {parity}")

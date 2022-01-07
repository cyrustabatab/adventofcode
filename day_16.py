import math

INPUT_FILE = "input_16.txt"

def day_16(input_file=INPUT_FILE):
    
    
    hex_to_binary = {}
    for i in range(0,16):
        bits = bin(i)
        hex_code =hex(i)
        index = bits.index('b')
        hex_index = hex_code.index('x')
        bits = bits[index +1:].zfill(4)
        hex_code =hex_code[hex_index +1:].upper()
        hex_to_binary[hex_code] = bits
    

    with open(input_file,'r') as f:
        hexadecimal_string = f.read().strip()

    binary_string = [] 
    for character in hexadecimal_string:
        binary = hex_to_binary[character]
        binary_string.append(binary)

    
    binary_string = ''.join(binary_string)


    i = 0

    version_numbers = 0
    while i < len(binary_string):

        version_number = binary_string[i:i+3]
        version_numbers += int(version_number,2)
        i += 3
        packet_type = int(binary_string[i:i+3],2)
        i += 3

        if packet_type == 4:
            i += 1
            length = 11
            while binary_string[i] == '1':
                i += 5
                length += 5

            i += 5 
            
            added_zero_bits = math.ceil(length / 4) * 4 - length
            i += added_zero_bits
        elif packet_type == 0:
            length = int(binary_string[i:i+15],2)

            i += (15 + length)
        elif packet_type == 1:
            number_subpackets = int(binary_string[i:i+11],2)
            i += 11 * (number_subpackets + 1)

            
    return version_numbers


            

















if __name__ == "__main__":


    print(day_16())

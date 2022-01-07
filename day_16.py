


def day_16():
    
    
    hex_to_binary = {}
    for i in range(0,16):
        bits = bin(i)
        hex_code =hex(i)
        index = bits.index('b')
        hex_index = hex_code.index('x')
        bits = bits[index +1:].zfill(4)
        hex_code =hex_code[hex_index +1:].upper()
        hex_to_binary[hex_code] = bits

    
    print(hex_to_binary)




if __name__ == "__main__":


    day_16()

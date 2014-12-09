#Matthew Wadkin
#18/09/14
#This program will change a number from decimal to hexidecimal

program = 1
while program == 1:

    DecimalValue = -1
    while DecimalValue > 4095 or DecimalValue < 0:
        DecimalValue = int(input("Enter an integer between 0 and 4095: "))
        
    BinaryString = ""
    while DecimalValue > 0:
        BinaryString = str(DecimalValue % 2) + BinaryString
        DecimalValue = DecimalValue // 2
        
    no_of_bits = len(BinaryString)

    no_of_bits = no_of_bits - 12
    while no_of_bits < 0:
        BinaryString = "0" + BinaryString
        no_of_bits = no_of_bits + 1

    bit12 = int(BinaryString[0])
    bit11 = int(BinaryString[1])
    bit10 = int(BinaryString[2])
    bit9 = int(BinaryString[3])
    bit8 = int(BinaryString[4])
    bit7 = int(BinaryString[5])
    bit6 = int(BinaryString[6])
    bit5 = int(BinaryString[7])
    bit4 = int(BinaryString[8])
    bit3 = int(BinaryString[9])
    bit2 = int(BinaryString[10])
    bit1 = int(BinaryString[11])

    ph8_2 = bit12 * 8
    ph4_2 = bit11 * 4
    ph2_2 = bit10 * 2
    ph1_2 = bit9 * 1

    ph8_1 = bit8 * 8
    ph4_1 = bit7 * 4
    ph2_1 = bit6 * 2
    ph1_1 = bit5 * 1

    ph8 = bit4 * 8
    ph4 = bit3 * 4
    ph2 = bit2 * 2
    ph1 = bit1 * 1

    hex2 = ph8_2 + ph4_2 + ph2_2 + ph1_2
    hex1 = ph8_1 + ph4_1 + ph2_1 + ph1_1
    hex0 = ph8 + ph4 + ph2 + ph1

    hex_num = [hex2,hex1,hex0]
    hex_number = ""
    for hexes in hex_num:
        
        if hexes == 10:
            hex_number = hex_number + "A"
        elif hexes == 11:
            hex_number = hex_number + "B"
        elif hexes == 12:
            hex_number = hex_number + "C"
        elif hexes == 13:
            hex_number = hex_number + "D"
        elif hexes == 14:
            hex_number = hex_number + "E"
        elif hexes == 15:
            hex_number = hex_number + "F"
        else:
            hex_number == hex_number + hex_number
    

    print("Your number in hexidecimal is {0}".format(hex_number))


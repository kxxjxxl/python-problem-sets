def HexaToDecimal(hexdec):
    length = len(hexdec)
    power_base = 1
    dec = 0
    for i in range(length - 1, -1, -1):
        # converting it to ASCII value for 1-9
        if hexdec[i] >= '0' and hexdec[i] <= '9':
            dec += (ord(hexdec[i]) - 48) * power_base #subtracting 48 from ASCII value to converting it to int 1-9
            # incrementing base by power
            power_base = power_base * 16
        # converting it to ASCII value for A-F
        elif hexdec[i] >= 'A' and hexdec[i] <= 'F':
            dec += (ord(hexdec[i]) - 55) * power_base #Subtracting 55 from ASCII value to converting it to int 10-15
            power_base = power_base * 16
    return dec


def main():
    hex_num = str(input("Please enter the Hexadecimal Value: "))
    print("Decimal Conversion is: ", HexaToDecimal(hex_num))


main()




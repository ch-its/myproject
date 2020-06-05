def dB(n):  
    return bin(n).replace("0b", "") 
print(dB(2000000000000))
print(dB(1999999999999))
print(dB(2000000000000)^dB(1999999999999))
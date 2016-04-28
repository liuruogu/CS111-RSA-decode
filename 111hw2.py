__author__ = 'liu'
import math

#calculate
def calcululate_decode(ds):
    cal = ds
    for i in range(14):
        ds*=cal
        ds%=115
    # print(ds)
    rule(ds)
# Decryption
def decrypton():

    for i in range(len(encode)):
        # print(encode[i])
        ds = encode[i]
        calcululate_decode(ds)

# Decryption rule
def rule(num):
    Dstring = ''
    if num == 2:
        Dstring = Dstring + ''
    elif num == 3:
        Dstring = Dstring + ','
    elif num == 4:
        Dstring = Dstring + '.'
    elif num == 5:
        Dstring = Dstring + ';'
    elif num == 6:
        Dstring = Dstring + '\''
    elif num<33 and num >6:
        Dstring = Dstring + chr(58+num)
    else:
        print('*error*')
    print(Dstring)

encode= [
     39,      40,     102,      40,      82,      40,
    108,     113,      96,      40,      61,      65,
      8,      40,     100,       8,      96,      99,
     66,       8,      82,      40,      74,      40,
     96,      82,      66,     100,     100,       8,
     74,      18,      82,      96,      40,      68,
     82,      40,      39,     113,      96,      40,
     61,      65,       8,      61,       3,       8,
     18,      65,      65,      66,      39,      66,
    100,     100,     113,      24,       6,       8,
     65,      66,      39,      66,     100,     100,
     40,      96,      40,      66,     100,      64,
    ]

def main():
    decrypton()

if __name__ == "__main__":
    main()
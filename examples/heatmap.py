# coverage heatmap example (no pep8 here to save vertical space :)

def not_called():  # (1x)
    return  # should be red (0x)

def called_once():
    print('called')  # should be white (1x)

def called_twice(a):
    print('toc')  # should be very transparent green (2x)
    if a:  # should be yellow (partial covered branch)
        d = a
    b = 1 + d  # Would crash if `a == 0` (`d` not defined). Branch coverage
               # can alert you about this (see the yellow line 11).
    return b

called_once()  # should be white (1x)

for i in range(2):  # 3x
    called_twice(i + 1)  # 2x
for _ in range(10):  # 11x
    pass  # 10x
for _ in range(100):
    pass
for _ in range(1000):
    pass
for _ in range(10000):  # should be very green
    pass

count = 0  # 1x
for i1 in range(2):  # 3x
    for i2 in range(2):  # 6x
        for i3 in range(2):
            print('8x')
            for i4 in range(2):
                for i5 in range(2):
                    for i6 in range(2):
                        for i7 in range(2):
                            for i8 in range(2):
                                for i9 in range(2):
                                    for i10 in range(2):
                                        for i11 in range(2):
                                            for i12 in range(2):
                                                for i13 in range(2):
                                                    for i14 in range(2):
                                                        for i15 in range(2):
                                                            for i16 in range(2):
                                                                count += 1  # 2^16x = 65536 hits

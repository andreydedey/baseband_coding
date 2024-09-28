def manchester_differential(bits):
    result = []
    previous = 0
    for bit in bits:
        if bit == '1':
            result.extend([previous, 1 - previous])
        else:
            previous = 1 - previous
            result.extend([previous, 1 - previous])
    return result

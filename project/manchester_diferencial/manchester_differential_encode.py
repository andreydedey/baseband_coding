def manchester_differential(bits):
    result = []
    previous = 0

    for bit in bits:
        if bit == '1':
            result.extend([previous, 1 - previous])
            previous = 1 - previous
        else:
            result.extend([1 - previous, previous])
    return result

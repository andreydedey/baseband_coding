def nrzi(bits):
    result = []
    previous = 0
    for bit in bits:
        if bit == '1':
            previous = 1 - previous
        result.append(previous)
    return result

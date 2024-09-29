def manchester_differential(bits):
    result = []
    previous = 1  # Começamos com o nível alto

    for bit in bits:
        if bit == '1':
            result.extend([previous, 1 - previous])
            previous = 1 - previous
        else:
            result.extend([1 - previous, previous])
    return result

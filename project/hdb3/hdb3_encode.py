def hdb3(bits):
    # Implementação simplificada de HDB3 (bipolar encoding com violação após 4 zeros consecutivos)
    result = []
    polarity = 1
    zero_count = 0
    for bit in bits:
        if bit == '0':
            zero_count += 1
            if zero_count == 4:
                # Violação
                result[-3] = -polarity  # Bipolar violation
                result.append(polarity)
                polarity *= -1
                zero_count = 0
            else:
                result.append(0)
        else:
            zero_count = 0
            polarity *= -1
            result.append(polarity)
    return result

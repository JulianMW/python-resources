def int2binary(input_str, output_base):
    """
    if x < 0:
        sign = -1
    elif x == 0:
        return digits_list[0]
    else:
        sign = 1
        
    x *= sign
    output_digits = []
    """
    
    while x:
        digits.append(digs[int(x % 2)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

return int(''.join(digits))

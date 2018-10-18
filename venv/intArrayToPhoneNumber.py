def create_phone_number(n):
    result = ''.join(map(str, n))
    return "(" + result[0:3] + ") " + result[3:6] + "-" + result[6:10]

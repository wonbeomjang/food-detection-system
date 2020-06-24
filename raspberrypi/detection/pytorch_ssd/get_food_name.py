def getfood_name(input_list):
    if not len(input_list):
        return []
    out = []
    for name in input_list:
        if name == 'apple':
            name = '사과'
        elif name == 'beer':
            name = '맥주'
        elif name == 'egg':
            name = '계란'
        elif name == 'mandarin':
            name = '귤'
        elif name == 'milk':
            name = '우유'
        elif name == 'soju':
            name = '소주'
        out.append({'name':name})
    return out

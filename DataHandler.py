

def SplitStr(str, preSeparator, subSeparator):
    return str.split(preSeparator)[1].split(subSeparator)[0]

def SplitStrAsFloat(str, preSeparator, subSeparator):
    return float(str.split(preSeparator)[1].split(subSeparator)[0])


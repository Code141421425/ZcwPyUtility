

def SplitStr(str, preSeparator, subSeparator=None):
    """
    DO: 返回字符串截取的部分
    """
    # if subSeparator:
    #     result = 
    # else:
    #     result = str.split(preSeparator)[1]
    
    return str.split(preSeparator)[1].split(subSeparator)[0]

def SplitStrAsFloat(str, preSeparator, subSeparator):
    return float(SplitStr(str, preSeparator, subSeparator))


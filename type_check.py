def only_ints(param1, param2):
    print (param1, "and", param2)
    if isinstance(param1, bool) or isinstance(param2, bool):
        print("caught true or false value")
        return False
    else:
        param1Value = isinstance(param1, int)
        param2Value = isinstance(param2, int)
        print(param1Value, "and", param2Value)
    if param1Value == param2Value:
        return True
    else:
        return False
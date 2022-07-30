# -*- coding: utf-8 --

def validate_pin(x):
    z = len(x)

    if x.isdigit():
        if z == 4 or z == 6:
            return True
        else:
            return False
    else:
        return False
    


#!/usr/bin/python3
"""
UTF-8 validation module.
"""


def validUTF8(data):
    """
    Check if the given data is valid UTF-8 encoded.

    Parameters:
    data (bytes or str): The data to check.

    Returns:
    bool: True if the data is valid UTF-8 encoded, False otherwise.
    """
    if not isinstance(data, bytes):
        i = 0
        while i < len(data):
            if (data[i] & 0b10000000) == 0b00000000:
                i += 1
            elif (data[i] & 0b11100000) == 0b11000000:
                if (data[i+1] & 0b11000000) == 0b10000000:
                    i += 2
                else:
                    return False
            elif (data[i] & 0b11110000) == 0b11100000:
                if (data[i+1] & 0b11000000) == 0b10000000 and \
                   (data[i+2] & 0b11000000) == 0b10000000:
                    i += 3
                else:
                    return False
            elif (data[i] & 0b11111000) == 0b11110000:
                if (data[i+1] & 0b11000000) == 0b10000000 and \
                   (data[i+2] & 0b11000000) == 0b10000000 and \
                   (data[i+3] & 0b11000000) == 0b10000000:
                    i += 4
                else:
                    return False
            else:
                return False
        return True
    else:
        try:
            data.encode('utf-8').decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False

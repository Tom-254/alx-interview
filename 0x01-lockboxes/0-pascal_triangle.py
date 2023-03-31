#!/usr/bin/python3
""" Unlock boxes """


def canUnlockAll(boxes):
    """
    Check if box can be unlocked
    """
    if len(boxes) is 0 or type(boxes) is not list:
        return False
    locked = {box: True for box in range(1, len(boxes))}
    locked.update({0: False})
    keys = boxes[0]
    unlock(boxes, locked, keys)

    if True in locked.values():
        return False
    return True


def unlock(boxes, locked, keys):
    """
        Recursively unlock the boxes locked
    """
    for key in keys:
        try:
            if locked[key]:
                locked[key] = False
                unlock(boxes, locked, boxes[key])
        except KeyError:
            pass

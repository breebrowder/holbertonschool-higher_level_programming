#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = []
    flip = 0
    for i in range(list_length):
        try:
            num = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            flip = 1

        except TypeError:
            print("wrong type")
            flip = 1

        except IndexError:
            print("out of range")
            flip = 1

        finally:
            if flip:
                flip = 0
                length.append(0)
            else:
                length.append(num)
    return length

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for index in range(list_length):
        item = 0
        try:
            item = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            result.append(item)
    return result

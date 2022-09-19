#!/usr/bin/python3


def list_division(my_list1, my_list2, n):

    divisions = []

    for i in range(n):

        div = 0

        try:
            div = my_list1[i] / my_list2[i]

        except ZeroDivisionError:
            print("division by 0")

        except IndexError:
            print("out of range")

        except (TypeError, ValueError):
            print("wrong type")

        finally:
            divisions.append(div)

    return divisions

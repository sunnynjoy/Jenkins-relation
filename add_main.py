from add import Add


class AddMain:

    add = Add()
    value = add.add_2_numbers(1, 2)
    print(" The addition of 2 numbers is ", value)

    # 3 values
    value = add.add_3_numbers(9, 2, 1)
    print(" The addition of 3 numbers is ", value)

    # 2 values subtract
    value = add.subtract_2_numbers(9, 2)
    print(" The subtraction of 2 numbers is ", value)
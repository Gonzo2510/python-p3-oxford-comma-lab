def oxford_comma(items):
    if len(items) == 1:
        my_str = ''.join(items)
    elif len(items) == 2:
        my_str = ' and '.join(items)
    elif len(items) >= 3:
        my_str = ''
        count = 0

        while count < len(items):
            if count == (len(items) - 2):
                my_str += items[count] +', and '+ items[count + 1]
            elif count < len(items) - 1:
                my_str += items[count] +', '
            count += 1

    print(my_str)
    return my_str


oxford_comma(["Jacob", 'Isabel', 'Aaron', 'Joe'])




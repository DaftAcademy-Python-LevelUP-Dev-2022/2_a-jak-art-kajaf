from ast import arg


def greeter(func):
    def inner(*args):
        r = func(*args)
        return (f'Aloha ' + r.title())
    return inner


def sums_of_str_elements_are_equal(func):
    def inner(*args):
        def count_sum(number):
            sum_of_digits = 0
            if str(number)[0] == "-":
                for digits in str(number)[1:]:
                    sum_of_digits -= int(digits)
            else:
                for digits in str(number):
                    sum_of_digits += int(digits)
            return sum_of_digits
        list_numbers = func(*args).split()    
        first = count_sum(list_numbers[0])
        second = count_sum(list_numbers[1])
        if first == second:
            return str(first) + ' == ' + str(second)
        else:
            return str(first) + ' != ' + str(second)
    return inner



def format_output(*required_keys):
    def decorator(func):
        def wrapper(*args):
            dict = func(*args)
            new_dict = {}
            for key in required_keys:
                tmp_list = []
                for x in key.split("__"):
                    if x in dict.keys():
                        if dict[x] == '':
                            tmp_list.append('Empty value')
                        else:
                            tmp_list.append(dict[x])
                    else:
                        raise ValueError
                    new_dict[key] = ' '.join(tmp_list)
            return new_dict
        return wrapper
    return decorator


def add_method_to_instance(klass):
    pass

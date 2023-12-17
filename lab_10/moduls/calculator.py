def make_calc(operator, initial=0):

    result = initial


    def calc(num):

        nonlocal result

        if operator == "+":

            result += num

        elif operator == "-":

            result -= num

        elif operator == "*":

            result *= num

        elif operator == "/":

            result /= num

        return result


    return calc

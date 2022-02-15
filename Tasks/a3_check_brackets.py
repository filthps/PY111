def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    open_brackets = "({["
    close_brackets = ")}]"
    b = {t[0]: t[1] for t in zip(open_brackets, close_brackets)}

    def get_reversed_bracket(bracket: str):
        if bracket in b:
            return b[bracket]
    arr_1 = []
    for i in brackets_row:
        if i in close_brackets:
            try:
                index = arr_1.index(i)
            except ValueError:  # Встретили закрывающую скобку, перед которой не было открывающей
                return False
            del arr_1[index]
        else:
            v = get_reversed_bracket(i)
            if v is not None:
                arr_1.append(v)
    if len(arr_1) > 0:
        return False
    return True


if __name__ == "__main__":
    print(check_brackets("{}()"))

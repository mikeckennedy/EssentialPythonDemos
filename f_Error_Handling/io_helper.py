def count_chars(filename):
    return len(open(filename, 'r').read())


def is_comment(shortline):
    if not shortline:
        return False

    return shortline.startswith('#')


def is_blank(shortline):
    return not shortline


def count_lines(filename):
    #fin = open(filename, 'r')
    with open(filename, 'r') as fin:
        real_lines = []
        for line in fin:
            shortline = line.strip()
            if is_comment(shortline) or is_blank(shortline):
                continue

            real_lines.append(shortline)

        #fin.close()
        return len(real_lines)

    # try:
    #
    #     real_lines = []
    #     for line in fin:
    #         shortline = line.strip()
    #         if is_comment(shortline) or is_blank(shortline):
    #             continue
    #
    #         real_lines.append(shortline)
    #
    # finally:
    #
    #     fin.close()
    #
    # return len(real_lines)

















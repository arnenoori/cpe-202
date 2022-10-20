def isBalanced (string):
    if isinstance(string, basestring) is False:
        return True

    STRUCTURE_OPN = 1
    STRUCTURE_CLS = 2

    structures      = {
        '(': (')', STRUCTURE_OPN),
        ')': ('(', STRUCTURE_CLS),
        '[': (']', STRUCTURE_OPN),
        ']': ('[', STRUCTURE_CLS),
        '{': ('}', STRUCTURE_OPN),
        '}': ('{', STRUCTURE_CLS),
    }
    structure_stack = []
    string_length   = len(string)

    for i in range(string_length):
        if string[i] in structures:
            structure = string[i]

            if structures[structure][1] is STRUCTURE_OPN:
                structure_stack.append(structure)
            elif structures[structure][1] is STRUCTURE_CLS:
                if len(structure_stack) is not 0:
                    if structure_stack.pop() != structures[structure][0]:
                        return False
                else:
                    return False

    return (len(structure_stack) is 0)
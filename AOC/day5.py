def is_gonna_react(a, b):
    low_up = a.isupper() and b.islower()
    up_low = a.islower() and b.isupper()
    same_sign = a.lower() == b.lower()

    return (low_up or up_low) and same_sign


def react(input):
    new_polymer = ['p']
    old_polymer = list(reversed(input))

    while old_polymer:
        current_unit = old_polymer.pop()

        if is_gonna_react(current_unit, new_polymer[-1]):
            new_polymer.pop()
        else:
            new_polymer.append(current_unit)

    return new_polymer


def remove_unit(unit, polymer):
    new_polymer = []

    for i in range(len(polymer)):
        if polymer[i] != unit.upper() and polymer[i] != unit.lower():
            new_polymer.append(polymer[i])

    return new_polymer


if __name__ == '__main__':

    input = open('inputs/input5.txt').read()

    new_polymer = react(input)
    print('Part One: Polymer after reaction has {} units'.format(len(new_polymer) - 2))

    alphabet = []
    for letter in range(97, 123):
        alphabet.append(chr(letter))

    data = {}
    for letter in alphabet:
        new_polymer = remove_unit(letter, input)
        new_polymer = react(new_polymer)
        data[letter] = len(new_polymer)

    max_value = min(data.values()) - 2
    max_arg = min(data, key=data.get)

    print('Part Two: The shortest polymer is {} units long, after the removal of letter: {}'.format(max_value, max_arg))

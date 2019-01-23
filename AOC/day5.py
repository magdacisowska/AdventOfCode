
def react(input):
    old_polymer = input
    new_polymer = []
    counter = 0

    while len(old_polymer) != len(new_polymer):
        if counter == 0:
            old_polymer = input
            new_polymer = []
        else:
            old_polymer = new_polymer
            new_polymer = []

        i = 0
        while i < len(old_polymer) - 1:

            one_case = old_polymer[i].isupper() and old_polymer[i + 1].islower()
            second_case = old_polymer[i].islower() and old_polymer[i + 1].isupper()

            if (one_case or second_case) and old_polymer[i].lower() == old_polymer[i + 1].lower():
                i += 2
            else:
                new_polymer.append(old_polymer[i])
                if i == len(old_polymer) - 2:
                    new_polymer.append(old_polymer[i + 1])
                i += 1
        counter = 1

    return new_polymer


def remove_unit(unit, polymer):

    new_polymer = []

    for i in range(len(polymer)):
        if polymer[i] != unit.upper() and polymer[i] != unit.lower():
            new_polymer.append(polymer[i])

    return new_polymer


if __name__ == '__main__':

    input = open('inputs/input5.txt').read()

    # reduced_polymer = react(input)
    # print('Part One: Polymer after reaction has {} units'.format(len(reduced_polymer)))

    data = {}

    alphabet = []
    for letter in range(97, 123):
        alphabet.append(chr(letter))

    for letter in alphabet:
        reduced = remove_unit(letter, input)
        reduced = react(reduced)
        data[letter] = len(reduced)
        print(letter, len(reduced))

    max_arg = min(data, key=data.get)
    max_value = min(data.values())

    print('Part Two: The shortest polymer is {} units long, after the removal of letter: {}'.format(max_value, max_arg))

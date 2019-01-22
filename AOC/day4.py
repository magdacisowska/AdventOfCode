import datetime
import collections


def organize(inputs):
    '''
    :param inputs: raw data, read line by line from file
    :return: dictionary organized by date, where key = date, value = comment
    '''
    register = {}

    for line in inputs:

        comment = []

        rubbish, tail = line.split('[')
        year, month, tail = tail.split('-')

        # distinguish shorter or longer message
        if '#' in line:
            day, full_hour, info_0, info_1, info_2, info_3 = tail.split(' ')
            comment[0:4] = info_0, info_1, info_2, info_3
        else:
            day, full_hour, info_0, info_1 = tail.split(' ')
            comment[0:2] = info_0, info_1

        hour, tail = full_hour.split(':')
        minute, rubbish = tail.split(']')

        date = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute))

        register[date] = comment

        register = collections.OrderedDict(sorted(register.items()))

    return register


def get_sleep_records(register):
    '''
    :param register: register (dictionary) ordered beforehand by date
    :return: full register (dictionary) of overall time of sleep of all guards.
     key = guard_id, value = total minutes of sleep
    '''
    records = {}

    for date, comment in register.items():
        if '#' in comment[1]:
            guard_id = int(comment[1][1:])
        elif 'asleep' in comment[1]:
            nap_start = date
        elif 'up' in comment[1]:
            nap_end = date
            nap_time = nap_end - nap_start
            records[guard_id] = records.get(guard_id, datetime.timedelta(minutes=0)) + nap_time

    for id, record in records.items():
        print('Guard {} slept for {}'.format(id, record))

    return records


def which_minute(victim_id, register):
    '''
    Given the ID of the most sleeping guard, crates a dictionary where key = hour, value = sleep attempts
    :param victim_id: ID of the laziest guard
    :param register: register (dictionary) ordered beforehand by date
    :return: dictionary
    '''

    minute_register = {}
    is_victim = False

    # iterate through all register, considering only the victim's sleep attempts
    for date, comment in register.items():

        # consider only concrete hour and minute, not the whole date
        time_of_day = datetime.timedelta(hours=date.hour, minutes=date.minute)

        if '#' in comment[1] and comment[1][1:] == str(victim_id):
            is_victim = True
        elif '#' in comment[1] and comment[1][1:] != str(victim_id):
            is_victim = False

        if 'asleep' in comment[1] and is_victim:
            minute_register[time_of_day] = minute_register.get(time_of_day, 0) + 1
            nap_start = date
        elif 'up' in comment[1] and is_victim:
            nap_end = date
            nap_time = nap_end - nap_start

            # having start- and end-time of each nap of the victim,
            # give each minute between start and stop the value of +1
            for i in range(1, int(nap_time.total_seconds()/60)):
                minute_register[time_of_day - datetime.timedelta(minutes=i)] = \
                    minute_register.get(time_of_day - datetime.timedelta(minutes=i), 0) + 1

    return minute_register


if __name__ == '__main__':
    inputs = open('inputs/input4.txt').read().splitlines()

    register = organize(inputs)
    records = get_sleep_records(register)

    max_value = max(records.values())
    max_arg = max(records, key=records.get)

    print('The longest nap time had guard #{}, making it a total of {}.'.format(max_arg, max_value))

    victim_register = which_minute(max_arg, register)
    max_value = max(victim_register.values())
    max_arg = max(victim_register, key=victim_register.get)

    print('The least guarded hour is {}, with {} sleep cases.'.format(max_arg, max_value))

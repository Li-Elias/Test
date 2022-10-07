import sys

START_TIME = 540
WORK_TIME = 480
REST_TIME = 960

all_orders = []
available_orders = []


with open(sys.argv[1], 'r') as fileobj:
    for row in fileobj:
        if row != '\n':
            all_orders.append(row.rstrip('\n').split())


def checkorders(current_time):
    count = 0
    for order in all_orders:
        if int(order[0]) <= current_time:
            available_orders.append(all_orders.pop(count))
        count += 1


def currentorder(key):
    if key == '1':
        return (available_orders.pop(0))

    elif key == '2':
        count = 0
        order = available_orders[0]
        for i, available_order in enumerate(available_orders):
            if int(available_order[1]) < int(order[1]):
                count = i
                order = available_order
        return (available_orders.pop(count))


def processorder(current_time, remaining_work_time, process_time):
    process_time -= remaining_work_time
    current_time += remaining_work_time

    while process_time != 0:
        if process_time - WORK_TIME > 0:
            process_time -= WORK_TIME
            current_time += WORK_TIME
        else:
            remaining_work_time = WORK_TIME - process_time
            current_time += process_time
            process_time = 0
            break
        current_time += REST_TIME

    return (current_time, remaining_work_time)


def main():
    order_length = len(all_orders)
    current_time = START_TIME
    waiting_time = 0

    while all_orders:
        remaining_work_time = WORK_TIME

        while remaining_work_time >= 0:
            checkorders(current_time)

            if available_orders:
                current_order = currentorder(sys.argv[2])
                waiting_time += (current_time - int(current_order[0]))
                current_time, remaining_work_time = processorder(
                    current_time, remaining_work_time, int(current_order[1]))

            remaining_work_time -= 1
            current_time += 1
        current_time += REST_TIME

    print(
        f'Maximale Wartezeit: {waiting_time}\nDurchschnittliche Wartezeit: {waiting_time/order_length}')


if __name__ == '__main__':
    main()

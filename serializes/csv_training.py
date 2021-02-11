import csv


def csv_write(users_list):
    try:
        with open('./data.csv', 'w') as fd:
            writer = csv.writer(fd)
            for user_tuple in users_list:
                writer.writerow(user_tuple)


    except (IOError, Exception) as e:
        print(f'Exception write CSV format {e.args}')


def csv_read():
    users = []

    try:
        with open('./data.csv', 'r') as fd:
            reader = csv.reader(fd)
            for row in reader:
                if row:
                    users.append(row)

    except (IOError, Exception) as e:
        print(f'Exception read CSV format {e.args}')

    return users


def main():
    users = [
        ('Anna', 'Much', 45633),
        ('Tom', 'Buch', 63012)
    ]
    csv_write(users)
    return_users = csv_read()
    print(return_users)


if __name__ == '__main__':
    main()

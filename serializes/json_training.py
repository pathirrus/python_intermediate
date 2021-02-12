import json


def json_write(warrior_list):
    try:
        with open("warriors.json", 'w') as out_file:
            json.dump(warrior_list, out_file, indent=2)

    except (IOError, Exception) as e:
        print(f'Exception write JSON format {e.args}')


def json_read():
    try:
        with open('./warriors.json', 'r') as fd:
            data = json.load(fd)
        return data

    except (IOError, Exception) as e:
        print(f'Exception read CSV format {e.args}')

def main():
    warrior_list = [
        {
            'Name': "Ragnar",
            'Weapon': '2 axes',
            'Victims': "Over 300"
        },
        {
            'Name': "Hehmund",
            'Weapon': 'Long sword',
            'Victims': "About 150"
        }
    ]
    json_write(warrior_list)
    return_users = json_read()
    print(return_users)


if __name__ == '__main__':
    main()


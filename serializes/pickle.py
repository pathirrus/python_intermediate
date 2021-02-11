import pickle


def pickle_write(items: list):
    print('Pickle_write start')
    try:
        with open('./data.pickle', 'wb') as fd:
            pickle.dump(items, fd)
            print(pickle.dumps(items))

    except (IOError, Exception) as e:
        print(f'Exception write pickle format {e.args}')
    print('Pickle_write finish')


def pickle_read():
    print('Pickle_read start')
    string_list = []
    try:
        with open('./data.pickle', 'rb') as fd:
            string_list = pickle.load(fd)
    except(IOError, Exception) as err:
        print(f'Exception pickle format {err.args}')
    print('Pickle_read start')
    return string_list

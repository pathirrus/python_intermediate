class OpenFileManager:
    def __init__(self, path: str = "", mode = 'a'):
        self.__source = path
        self.__mode = mode
        self.__fd = None

    @property
    def source(self):
        return self.__source

    def get_source(self):               #
        return self.__source            #robi to samo co powyżej

    @source.setter
    def source(self, path):
        self.__source = path

    def set_source(self, path):         #robi to samo co seter powyzej
        self.__source = path            #

    def __enter__(self):
        print("Opening file")
        self.__fd = open(self.__source, self.__mode)
        return  self.__fd

    def __exit__(self, *args):
        print("Closing filee")
        self.__fd.close()


def exercises_2():
    manager = OpenFileManager()
    manager_source = manager.source  # getter
    print(manager_source)
    manager.source = "./plik_test.txt"  # setter
    manager_source = manager.source  # getter
    print(manager_source)

    try:
        with manager as fd:
            print("Zapis")
            fd.write("Byle jaki tekst")
    except IOError as e:
        print(f"We have a problem, more info {e.args}")


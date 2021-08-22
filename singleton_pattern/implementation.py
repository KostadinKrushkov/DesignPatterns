class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        # else:  # If you want to run the __init__ method of a singleton when you call it
        #     cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class FileProxySingleton(metaclass=SingletonMeta):
    default_filename = 'testing.txt'

    def write_to_file(self, data, filename=default_filename):
        with open(filename, 'w') as f:
            f.write(data)
        print('Data saved')

    def append_to_file(self, data, filename=default_filename):
        with open(filename, 'a') as f:
            f.write(data)
        print('Data added')

    def read_from_file(self, filename=default_filename):
        with open(filename, 'r') as f:
            read_data = f.read()

        return read_data


if __name__ == '__main__':
    file_proxy = FileProxySingleton()
    second_file_proxy = FileProxySingleton()

    print(type(file_proxy) == type(second_file_proxy))  # True since both of them get the same instance

    file_proxy.write_to_file('Test writing some data\n')
    second_file_proxy.append_to_file('Test writing some other data\n')

    print(file_proxy.read_from_file())

class FileManager():
    def __init__(self, filename, mode, encoding):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


def is_increase(line1, line2):
    int1 = int(line1)
    int2 = int(line2)
    if int2 > int1:
        return 1
    else:
        return 0


def main():
    with FileManager('./data/input.txt', mode="r", encoding='utf-8') as f1:
        lines = f1.readlines()
        counter = 0
        for i in range(1, len(lines)):
            counter += is_increase(lines[i-1], lines[i])
    print(counter)


if __name__ == "__main__":
    main()
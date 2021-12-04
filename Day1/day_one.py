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


def count_inc(filename):
    with FileManager(filename, mode="r", encoding='utf-8') as f1:
        lines = f1.readlines()
        counter = 0
        for i in range(1, len(lines)):
            counter += is_increase(lines[i-1], lines[i])
    return counter


def create_windows(input_filename, windows_filename):
    with FileManager(input_filename, mode="r", encoding='utf-8') as f1:
        lines = f1.readlines()
        with FileManager(windows_filename, mode="w", encoding='utf-8') as fout:
            for i in range(2, len(lines)):
                win = int(lines[i-2]) + int(lines[i-1]) + int(lines[i])
                fout.write(f'{win}\n')


def main():
    input_file = './data/input.txt'
    windows_file = './data/win.txt'
    ans_p1 = count_inc(input_file)
    create_windows(input_file, windows_file)
    counter = count_inc(windows_file)
    print(f'Part 1: {ans_p1}\nPart 2: {counter}\n')


if __name__ == "__main__":
    main()
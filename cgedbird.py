def get_file_lines(filename):
    in_file = open(filename, 'r')
    lines = in_file.readlines()
    in_file.close()
    return lines

print(get_file_lines("poem.txt"))
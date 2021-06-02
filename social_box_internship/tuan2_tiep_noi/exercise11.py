def user_id_list(file_name=""):
    f = open(file_name, 'r')
    str_line = f.readline()
    while len(str_line) > 0:
        yield str_line.strip('\n')
        str_line = f.readline()
    f.close()

result = user_id_list('user_id_facebook.txt')
for x in result:
    print(x)

import os
path = os.getcwd()
file = os.listdir(path)
files_txt = [i for i in file if i.endswith('.txt')]


def file_collector(files):
    files_dict = {}
    files_list = []
    for name in files_txt:
        with open(name) as file_name:
            files_dict = {'name' : name, 'text' : file_name.readlines()}
        count = int(len(files_dict['text']))
        files_dict['count'] = count
        # print(files_dict)
        files_list.append(files_dict)
        # print(files_list)
        sorted_list = sorted(files_list, key=lambda x: x['count'])



    return sorted_list



# print(file_collector(files_txt))

def writing_file():
    for file in file_collector(files_txt):
        with open(file['name']) as f:
            name = file['name']
            count = str(file['count'])
            text = f.readline()
        with open('result.txt', 'a') as result_file:
            result_file.write(name)
            result_file.write('\n' + count)
            result_file.write('\n' + text)
            result_file.write('\n')
writing_file()















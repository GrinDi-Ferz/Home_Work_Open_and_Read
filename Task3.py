list_files = ['1.txt', '2.txt', '3.txt']

def sorted_files_by_size(file_names):
    file_size = {}
    for name in file_names:
        with open(name, 'r', encoding='utf-8') as f:
            file_size[name] = len(f.readlines())
    return sorted(file_size.items(), key=lambda item: item[1])


def united_text_files(list_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('')
    for file in list_files:
        with open(file[0], 'r', encoding='utf-8') as f:
            file_data = f.readlines()
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(file[0]+'\n')
            f.write(str(file[1])+'\n')
            f.writelines(file_data)
            f.write('\n')

united_text_files(sorted_files_by_size(list_files), 'new_text.txt')

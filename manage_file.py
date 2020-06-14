
# -*- coding: utf-8 -*-


def write_file(word_list):
    print('write file')
    try:
        _file = open('file.txt', 'w')
        _file.writelines(';'.join(word_list))
        _file.close()
    except Exception as exc:
        print(u'Catch Exception write_file')
        print(exc)


def read_file():
    print('read file')
    try:
        _file = open('file.txt', 'r')
        _file_line = _file.readline()
        _file.close()
        return _file_line.split(';')
    except Exception as exc:
        print(u'Catch Exception read_file')
        print(exc)
        return ['']

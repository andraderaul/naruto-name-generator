# -*- coding: utf-8 -*-
import requests
import bs4
from manage_file import write_file

alphabet = ['A', 'B', 'C', 'D', 'E',  'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8']


def _clear_name(a_name):
    a_name = a_name.lower()
    a_name = a_name.replace("-", " ")
    a_name = a_name.replace("0", "zero")
    a_name = a_name.replace("1", "one")
    a_name = a_name.replace("2", "two")
    a_name = a_name.replace("3", "three")
    a_name = a_name.replace("4", "four")
    a_name = a_name.replace("5", "five")
    a_name = a_name.replace("6", "six")
    a_name = a_name.replace("7", "seven")
    a_name = a_name.replace("8", "eight")
    a_name = a_name.replace("9", "nine")
    return a_name


def _get_name(tag_a, substring='name="'):
    tag_a_split_name = tag_a.split(substring)[1]
    a_name = tag_a_split_name.split('"')[0] + '.'
    return _clear_name(a_name)


def _filter(all_tag_a):
    substring = 'name="'
    return [_get_name(str(tag_a)) for tag_a in all_tag_a if(substring in str(tag_a))]


def _get_all_characters_names_async(url):
    print('url:', url)
    res = requests.get(url)
    res.encoding = 'utf-8'
    try:
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features="html.parser")
        all_tag_a = soup.find_all("a")
        characters_names = _filter(all_tag_a)
        print('characters:', characters_names)
        return characters_names
    except Exception as exc:
        print(u'Catch Exception!!!')
        print(exc)
        return []


def get_all_names():
    print('scrapping')
    all_characters_names = []
    for letter in alphabet:
        characters_names = _get_all_characters_names_async(
            'http://www.leafninja.com/biographies-'+letter+'.php')
        all_characters_names = [*all_characters_names, *characters_names]

    for number in numbers:
        characters_names = _get_all_characters_names_async(
            'http://www.leafninja.com/miscbio-'+number+'.php')
        all_characters_names = [*all_characters_names, *characters_names]

    characters_names = _get_all_characters_names_async(
        'http://www.leafninja.com/other.php')
    all_characters_names = [*all_characters_names, *characters_names]

    all_characters_names = list(set(all_characters_names))
    print('all characters name len:', len(all_characters_names))
    # write_file(all_characters_names)
    return all_characters_names

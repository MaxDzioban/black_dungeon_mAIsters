"""Very important module which contains functions: dict_reader_tuple, dict_reader_dict\
 and dict_invert which are used to work with pronunciation dictionary"""
def dict_reader_tuple(file_dict: str) -> tuple[str, int, list[str]]:
    """This function reads file and returns tuple with 3 elements
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w+', delete=False, encoding='utf-8') as tmpfile:
    ...     _ = tmpfile.write('NACHOS 2 N AE1 CH OW0 Z')
    >>> dict_reader_tuple(tmpfile.name)
    (('NACHOS', 2, ['N', 'AE1', 'CH', 'OW0', 'Z']),)
    """
    with open(file_dict, mode='r+', encoding='UTF-8') as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    res = []
    for i in content:
        i_s = i.split(' ', 2)
        i_s[1] = int(i_s[1])
        i_s[2] = i_s[2].split()
        res.append(tuple(i_s))
    return tuple(res)

def dict_reader_dict(file_dict: str) -> dict[str: set]:
    """This function reads file_dict and returns dictionary. The keys in this dictionary \
should be words, and the values should be a set of tuples of sound syllables
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w+', delete=False, encoding='utf-8') as tmpfile:
    ...     _ = tmpfile.write('NACHOS 1 N AA1 CH OW0 Z\\nNACHOS 2 N AE1 CH OW0 Z')
    >>> dict_reader_dict(tmpfile.name)
    {'NACHOS': {('N', 'AA1', 'CH', 'OW0', 'Z'), ('N', 'AE1', 'CH', 'OW0', 'Z')}}
    """
    dict_ = {}
    with open(file_dict, mode="r+", encoding="UTF-8") as file:
        content = file.readlines()
    content = [x.strip().split(' ', 2) for x in content]
    set_ = set()
    for el_ in content:
        if el_[0] not in dict_:
            set_ = set()
            set_.add(tuple(el_[2].split()))
        else:
            set_.add(tuple(el_[2].split()))
        dict_[el_[0]] = set_
    return dict_

def dict_invert(dct: dict) -> dict:
    """this function represents a dictionary of pronunciations in the form of a dictionary, \
the keys of which entries will be the number of utterances (Keys in the dictionary must be \
sorted), and the values will be sets of tuples, where the tuple represents a word that has \
the number of utterances equal to the key.
    >>> dict_invert({'WATER':{('W','A','T','E','R')}})
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    """
    dic_to_ret = {}
    set_ = set()
    if isinstance(dct, tuple):
        lst_to_app = []
        for i in dct:
            lst_to_app.append(i[0::2])
        dct = dict(lst_to_app)
    for key, val in list(dct.items()):
        val_t = tuple(val)
        if len(val) not in dic_to_ret:
            set_ = set()
            for i in val_t:
                set_.add(tuple((key, i)))
        else:
            for i in val_t:
                set_.add(tuple((key, i)))
        dic_to_ret[len(val)] = set_
    return dic_to_ret

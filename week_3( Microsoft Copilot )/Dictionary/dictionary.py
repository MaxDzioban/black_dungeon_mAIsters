def dict_reader_tuple(file_dict: str) -> tuple[str, int, list[str]]:
    """
    This function reads a file and returns a tuple with 3 elements.
    """
    with open(file_dict, mode='r', encoding='UTF-8') as file:
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
    """
    This function reads a file and returns a dictionary.
    The keys in this dictionary should be words, and the values should be a set of tuples of sound syllables.
    """
    dict_ = {}
    with open(file_dict, mode="r", encoding="UTF-8") as file:
        content = file.readlines()
    content = [x.strip().split(' ', 2) for x in content]
    for el_ in content:
        dict_.setdefault(el_[0], set()).add(tuple(el_[2].split()))
    return dict_

def dict_invert(dct: dict) -> dict:
    """
    This function represents a dictionary of pronunciations in the form of a dictionary,
    the keys of which entries will be the number of utterances (Keys in the dictionary must be sorted),
    and the values will be sets of tuples, where the tuple represents a word that has the number of utterances equal to the key.
    """
    dic_to_ret = {}
    for key, val in dct.items():
        for v in val:
            dic_to_ret.setdefault(len(v), set()).add((key, v))
    return dic_to_ret

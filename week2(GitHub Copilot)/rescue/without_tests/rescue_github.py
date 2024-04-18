def rescue_people(smarties: dict, limit_iq: int) -> tuple:
    output_lst = []
    limit = limit_iq
    smarties = dict(sorted(smarties.items(), key=lambda item: (-item[1], item[0])))

    for _ in range(len(smarties)):
        trans_lst = []
        for key, value in smarties.items():
            if limit - value >= 0:
                trans_lst.append(key)
                limit -= value
        for key in trans_lst:
            del smarties[key]
        output_lst.append(trans_lst)
        if not smarties:
            break

    return len(output_lst), output_lst
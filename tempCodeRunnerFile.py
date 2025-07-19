    temp_list = list()
        while len(temp_list) <= quantity-1:
            _random = randrange(min,max)
            if  _random not in temp_list:
                temp_list.append(_random)
        temp_list.sort()
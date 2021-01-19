import time


def _time_list():
    start_time = time.time()

    _num = 1000000
    _list = []
    _index = 1
    _value = 10

    for i in range(_num):
        _list.append(i)

    _result = _list[:_index] + [_value] + _list[_index:]
    print(_result)

    execution_time = (time.time() - start_time)
    return execution_time


def _time_loop():
    start_time = time.time()

    _num = 1000000
    _list = []
    _index = 1
    _value = 10

    for i in range(_num):
        _list.append(i)

    _list.append(_list[_num - 1])
    for i in range((_num - 1), _index, -1):
        _list[i] = _list[i - 1]
    _list[_index] = _value
    print(_list)

    execution_time = (time.time() - start_time)
    return execution_time


result = _time_list() - _time_loop()
print(result)

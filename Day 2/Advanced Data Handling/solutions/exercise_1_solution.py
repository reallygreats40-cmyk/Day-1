def load_all_records_baseline(data_list):
    results = []
    for item in data_list:
        if item > 0:
            results.append(item * 10)
    return results  # everything materialised before returning

def stream_records_lazy(data_list):
    # yield makes this a generator: nothing runs until iterated
    for item in data_list:
        if item > 0:
            yield item * 10  # one value produced at a time

raw_data = [5, -2, 12, 0, 8, -1]
print(load_all_records_baseline(raw_data))

lazy_gen = stream_records_lazy(raw_data)
print(hasattr(lazy_gen, "__next__"))  # True: it's an iterator
print(list(lazy_gen))  # consuming it runs the generator body

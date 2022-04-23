def make_flat_list(list):
    for item in list:
        if isinstance(item, list):
            for x in make_flat_list(item):
                yield x
        else:
            yield item

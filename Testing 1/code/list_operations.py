ls = []
def create_list():
    return ls

def add_to_list(item):
    create_list().append(item)
    return create_list()


def get_item(i):
    return create_list()[i]


def delete_item(i):
    del create_list()[i]

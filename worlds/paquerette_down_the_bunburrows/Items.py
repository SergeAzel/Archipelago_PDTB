from .RawItems import raw_list_of_tools

last_item_id = 0

fluffle = "Fluffle"


def toTuple(itemNames):
    global last_item_id
    items = []
    for itemName in itemNames:
        last_item_id += 1
        items.append((itemName, last_item_id))
    return items


list_of_tools = toTuple(raw_list_of_tools)
list_of_garbage = toTuple([fluffle])

list_of_items = list_of_tools + list_of_garbage

item_name_to_id = {item[0]: item[1] for item in list_of_items}
item_id_to_name = {item[1]: item[0] for item in list_of_items}

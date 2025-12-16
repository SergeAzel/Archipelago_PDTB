from .RawItems import raw_list_of_tools

last_item_id = 0

# Fluffle
fluffle = "Fluffle"
golden_fluffle = "Golden Fluffle"

# Traps
surface_teleport_trap = "Surface Teleport Trap"
elevator_trap = "Elevator Trap"

def toTuple(itemNames):
    global last_item_id
    items = []
    for itemName in itemNames:
        last_item_id += 1
        items.append((itemName, last_item_id))
    return items


list_of_tools = toTuple(raw_list_of_tools)
list_of_garbage = toTuple([fluffle, golden_fluffle])
list_of_traps = toTuple([surface_teleport_trap, elevator_trap])

list_of_items = list_of_tools + list_of_garbage + list_of_traps

item_name_to_id = {item[0]: item[1] for item in list_of_items}
item_id_to_name = {item[1]: item[0] for item in list_of_items}

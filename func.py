def move_unit(map, kaktus, direction):
    map.delete_object(kaktus.get_coords())
    kaktus.move(direction)
    map.enter_object(kaktus.get_coords(), '\U0001F335')

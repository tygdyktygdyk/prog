def move_unit(map, kaktus, direction):
    map.delete_object(kaktus.x, kaktus.y)
    kaktus.move(direction)
    map.enter_object(kaktus.x, kaktus.y, '\U0001F335')

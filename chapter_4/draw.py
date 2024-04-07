# drawing a ruler 

def draw_line(tick_length, tick_label=''):
    """ drawing one line wit given tick length followed by label"""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
        print(line)
    

def draw_interval(center_length):
    """ draw tick interval basd upon a central tick"""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    """ draw english ruler"""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


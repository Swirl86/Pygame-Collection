from constants import *

def get_light_color(rgb_color):
    for color_name, color_value in COLORS.items():
        if color_value == rgb_color:
            return LIGHT_COLORS[color_name]
    return WHITE
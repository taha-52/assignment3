import math

def degrees_to_radians(degrees):

    radians = degrees * (math.pi / 180)
    return radians

degree_value = 45 
radian_value = degrees_to_radians(degree_value)
print(f"{degree_value} degrees is equal to {radian_value} radians.")

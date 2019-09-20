""" the utility functions

Author: Henry Zhang
Date:August 31, 2019
"""

# module
import math

# parameters


# classes


# functions
def get_box_corners(x, y, orientation, l, w):
  ''' return corner points of an oriented box '''
  
  l_2 = l / 2
  w_2 = w / 2
  yaw_cos = math.cos(orientation)
  yaw_sin = math.sin(orientation)

  front_left_x = x + l_2 * yaw_cos - w_2 * yaw_sin
  front_left_y = y + l_2 * yaw_sin + w_2 * yaw_cos
  front_right_x = x + l_2 * yaw_cos + w_2 * yaw_sin
  front_right_y = y + l_2 * yaw_sin - w_2 * yaw_cos
  back_left_x = x - l_2 * yaw_cos - w_2 * yaw_sin
  back_left_y = y - l_2 * yaw_sin + w_2 * yaw_cos
  back_right_x = x - l_2 * yaw_cos + w_2 * yaw_sin
  back_right_y = y - l_2 * yaw_sin - w_2 * yaw_cos
  front_mid_x = x + l_2 / 2 * yaw_cos
  front_mid_y = y + l_2 / 2 * yaw_sin

  return (front_left_x, front_left_y), (front_right_x, front_right_y), \
         (back_left_x, back_left_y), (back_right_x, back_right_y), (front_mid_x, front_mid_y)

def get_box_outline(x, y, orientation, l, w):
  corners = get_box_corners(x, y, orientation, l, w)

  outline = []
  outline.append( ( (corners[0][0], corners[1][0]), (corners[0][1], corners[1][1]) ) )
  outline.append( ( (corners[1][0], corners[3][0]), (corners[1][1], corners[3][1]) ) )
  outline.append( ( (corners[3][0], corners[2][0]), (corners[3][1], corners[2][1]) ) )
  outline.append( ( (corners[2][0], corners[0][0]), (corners[2][1], corners[0][1]) ) )
  outline.append( ( (x, corners[4][0]), (y, corners[4][1]) ) )
  return outline

def align_angle(a1, a2):
  ''' align a2 to [a1 - pi, a1 + pi] '''
  while a2 - a1 > math.pi:
    a2 -= math.pi * 2
  while a1 - a2 > math.pi:
    a2 += math.pi * 2
  return a2

def is_angle_match(a1, a2):
  ''' return True if a1 is within (a2 - pi/4, a2 + pi/4) '''
  a2 = align_angle(a1, a2)
  if a2 - math.pi / 4 < a1 < a2 + math.pi / 4:
    return True
  else:
    return False


# main
def main():
  pass

if __name__ == "__main__":
  main()
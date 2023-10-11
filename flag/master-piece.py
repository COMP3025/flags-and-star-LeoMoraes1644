import sys
import math
import pygame
from pygame.locals import QUIT

# apanhei muito para fazer KKKK imagina fazer aquele dragão ... acho que não dava né KKKKKKK

SCREEN_SIZE = (400, 300)
RED_COLOR = (255, 0, 0)

DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
pygame.init()


def calculate_polygon_points(center_position, size, sides):
  angle_increment = math.radians(360 / sides)
  points = []
  for i in range(sides):
    x = int(center_position[0] + size * math.cos(i * angle_increment))
    y = int(center_position[1] + size * math.sin(i * angle_increment))
    points.append((x, y))
  return points


def rotate_point(point, angle, center):
  x_shifted, y_shifted = point[0] - center[0], point[1] - center[1]
  x_rot = x_shifted * math.cos(angle) - y_shifted * math.sin(angle)
  y_rot = x_shifted * math.sin(angle) + y_shifted * math.cos(angle)
  return int(x_rot + center[0]), int(y_rot + center[1])


def draw_star(screen,
              center_position,
              size,
              angle_degrees,
              overall_rotation_degrees=0):
  angle_radians = math.radians(angle_degrees)
  overall_rotation_radians = math.radians(overall_rotation_degrees)

  pentagon_points = calculate_polygon_points(center_position, size, 5)
  rotated_points = [
      rotate_point(point, angle_radians, center_position)
      for point in pentagon_points
  ]

  rotated_points = [
      rotate_point(point, overall_rotation_radians, center_position)
      for point in rotated_points
  ]

  pygame.draw.polygon(screen, RED_COLOR, [
      rotated_points[0], rotated_points[3], rotated_points[1],
      rotated_points[4], rotated_points[2], rotated_points[0]
  ])


def calculate_polygon_points(center_position, size, sides):
  angle_increment = math.radians(360 / sides)
  points = []
  for i in range(sides):
    x = int(center_position[0] + size * math.cos(i * angle_increment))
    y = int(center_position[1] + size * math.sin(i * angle_increment))
    points.append((x, y))
  return points


def rotate_point(point, angle, center):
  x_shifted, y_shifted = point[0] - center[0], point[1] - center[1]
  x_rot = x_shifted * math.cos(angle) - y_shifted * math.sin(angle)
  y_rot = x_shifted * math.sin(angle) + y_shifted * math.cos(angle)
  return int(x_rot + center[0]), int(y_rot + center[1])


def draw_rotating_pentagon(screen, center_position, size, rotation_degrees):
  rotation_radians = math.radians(rotation_degrees)
  pentagon_points = calculate_polygon_points(center_position, size, 5)
  rotated_points = [
      rotate_point(point, rotation_radians, center_position)
      for point in pentagon_points
  ]
  pygame.draw.polygon(screen, RED_COLOR, rotated_points)


def draw_half_circle(surface, color, center, radius, orientation):
  points = [center]

  if orientation == 'left':
    for i in range(0, 180):
      angle = math.radians(i)
      if orientation == 'left':
        angle += math.pi
      x = center[0] + math.sin(angle) * radius
      y = center[1] + math.cos(angle) * radius
      points.append((x, y))
  elif orientation == 'right':
    for i in range(0, 180):
      angle = math.radians(i)
      x = center[0] + math.sin(angle) * radius
      y = center[1] - math.cos(angle) * radius
      points.append((x, y))
  pygame.draw.polygon(surface, color, points)


while True:
  pygame.draw.rect(DISPLAYSURF, (0, 100, 0), (10, 20, 150, 200))
  pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (160, 20, 150, 200))
  pygame.draw.circle(DISPLAYSURF, (255, 0, 0), (160, 120), 65, 100)
  pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (177, 120), 52, 100)
  draw_half_circle(DISPLAYSURF, (0, 100, 0), (160, 110), 40, 'left')
  draw_half_circle(DISPLAYSURF, (0, 100, 0), (160, 120), 44, 'left')
  draw_half_circle(DISPLAYSURF, (0, 100, 0), (160, 130), 40, 'left')
  pygame.draw.ellipse(DISPLAYSURF, (255, 1, 0), (400, 250, 40, 80), 100)
  draw_star(DISPLAYSURF, (188, 120), 30, -17, overall_rotation_degrees=22)
  draw_rotating_pentagon(DISPLAYSURF, (188, 120), 15, 22)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()

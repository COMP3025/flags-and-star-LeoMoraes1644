import sys
import math
import pygame
from pygame.locals import QUIT

SCREEN_SIZE = (400, 300)
YELLOW_COLOR = (255, 255, 0)

pygame.init()
display_surface = pygame.display.set_mode(SCREEN_SIZE)


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


def draw_star(screen, center_position, size, angle_degrees):
  angle_radians = math.radians(angle_degrees)
  pentagon_points = calculate_polygon_points(center_position, size, 5)
  rotated_points = [
      rotate_point(point, angle_radians, center_position)
      for point in pentagon_points
  ]

  pygame.draw.polygon(screen, YELLOW_COLOR, [
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
  pygame.draw.polygon(screen, YELLOW_COLOR, rotated_points)


while True:
  draw_star(display_surface, (53, 55), 60, -17)
  draw_rotating_pentagon(display_surface, (53, 55), 24, 22)
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()

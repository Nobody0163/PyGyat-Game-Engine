import pygame
from enum import Flag

class GUIAlignmentType(Flag):
	COORDS = 1
	LEFT = 2
	TOP = 4
	RIGHT = 8
	BOTTOM = 16
	CENTER_X = 32
	CENTER_Y = 64

def verify_text_alignment_type(x: GUIAlignmentType):
	if x & GUIAlignmentType.COORDS:
		if x & (GUIAlignmentType.LEFT | GUIAlignmentType.TOP | GUIAlignmentType.RIGHT | GUIAlignmentType.BOTTOM):
			raise ValueError("Cannot have TextAlignmentType LEFT, TOP, RIGHT or BOTTOM when using COORDS")

	if x & GUIAlignmentType.LEFT and x & GUIAlignmentType.RIGHT:
		raise ValueError("Cannot have TextAlignmentType LEFT and RIGHT")

	if x & GUIAlignmentType.TOP and x & GUIAlignmentType.BOTTOM:
		raise ValueError("Cannot have TextAlignmentType TOP and BOTTOM")

	if x & GUIAlignmentType.CENTER_Y and x & (GUIAlignmentType.TOP | GUIAlignmentType.BOTTOM):
		raise ValueError("Cannot have TextAlignmentType CENTER_Y and TOP or BOTTOM")

	if x & GUIAlignmentType.CENTER_X and x & (GUIAlignmentType.LEFT | GUIAlignmentType.RIGHT):
		raise ValueError("Cannot have TextAlignmentType CENTER_X and LEFT or RIGHT")

class GUIAlignment:
	x: float
	y: float
	al_type: GUIAlignmentType

	def __init__(self, x: float, y: float, al_type: GUIAlignmentType):
		self.x = x
		self.y = y
		self.al_type = al_type

	def get_coords(self, dst: pygame.Surface, src: pygame.Surface):
		x = 0
		y = 0

		if self.al_type & GUIAlignmentType.CENTER_X:
			x = dst.get_width() / 2 - src.get_width() / 2

		if self.al_type & GUIAlignmentType.CENTER_Y:
			y = dst.get_height() / 2 - src.get_height() / 2

		if self.al_type & GUIAlignmentType.RIGHT:
			x = dst.get_width() - src.get_width()

		if self.al_type & GUIAlignmentType.BOTTOM:
			y = dst.get_height() - src.get_height()

		x += self.x
		y += self.y

		return (x, y)

__font_cache: dict[tuple[str, int], pygame.font.Font] = {}
def draw_text(dst: pygame.Surface, text: str, alignment: GUIAlignment, font_name: str, size: int, color: pygame.Color = (255, 255, 255)):
	verify_text_alignment_type(alignment.al_type)

	if (font_name, size) in __font_cache:
		font = __font_cache[(font_name, size)]
	else:
		font = pygame.font.Font(font_name, size)
		__font_cache[(font_name, size)] = font

	rendered = font.render(text, True, color)

	dst.blit(rendered, alignment.get_coords(dst, rendered))

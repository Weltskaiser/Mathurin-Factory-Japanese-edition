import os
import csv
import sys
import json
import pygame
import pygame.freetype
import random as rd

EVERYTHING = "== Everything =="

if len(sys.argv) != 5:
	sys.exit("Error: excepted three arguments: python3 cards.py path_to_csv level_delimiters path_to_score path_to_font_ttf")

csv_path = sys.argv[1]
level_delimiters = sys.argv[2]
score_path = sys.argv[3]
font_path = sys.argv[4]

def char_index(first_char, level_chars):
	i = 0
	while first_char != level_chars[i]:
		i += 1
		if i == len(level_chars):
			sys.exit("Unknown level indicator: {0}".format(first_char))
	return i

words = {}
# Setup dictionaries
level_count = 0
level_dicts = []
with open(csv_path, "r") as csv_file:
	rows = csv.reader(csv_file)
	next(rows)
	level_chars = []
	for char in level_delimiters:
		level_chars.append(char)
	level_count = len(level_chars)
	level_dicts = [{} for i in range(level_count)]
	last_level_list = []
	score_level_dicts = [{} for i in range(level_count)]
	last_level_score = 0
	level_names = ["" for i in range(level_count)]
	level = 0
	for row in rows:
		if row == []:
			continue
		elif len(row) == 1:
			indicator = row[0]
			level = char_index(indicator[0], level_chars)
			if level_names[level] != "":
				level_dicts[-1][level_names[-1]] = last_level_list.copy()
				score_level_dicts[-1][level_names[-1]] = last_level_score
				last_level_list = []
				level_names[-1] = ""
				if level < level_count - 1:
					l = level
					while l >= 0:
						level_dicts[l][level_names[l]] = level_dicts[l + 1].copy()
						level_dicts[l + 1] = {}
						if len(score_level_dicts[l + 1]) > 1:
							score_level_dicts[l + 1][EVERYTHING] = last_level_score
						score_level_dicts[l][level_names[l]] = score_level_dicts[l + 1].copy()
						score_level_dicts[l + 1] = {}
						level_names[l + 1] = ""
						l -= 1
			level_names[level] = indicator[3:]
			continue
		else:
			last_level_list.append(row)
	score_level_dicts[0][EVERYTHING] = last_level_score
# print(level_dicts)
# print(score_level_dicts)
score_dict = score_level_dicts[0].copy()

# Select words form dictionaries
level = 0
level_dict = level_dicts[0]
level_names = []
while level < level_count:
	print()
	print("Available categories:")
	key_i = 0
	keys = list(level_dict.keys())
	while key_i < len(keys):
		print("{0} - {1}".format(key_i, keys[key_i]))
		key_i += 1
	res = input("-> Select a category (press Enter for everything): ")
	if res == "":
		level_names.append(EVERYTHING)
		break
	res = eval(res)
	level_dict = level_dict[keys[res]]
	level_names.append(keys[res])
	level += 1

# print("dict", level_dict)
words = []
if level == level_count:
	words = level_dict.copy()
else:
	level_dicts = [level_dict]
	# print(level, level_count)
	while level < level_count - 1:
		level_plus_dicts = []
		for level_dict in level_dicts:
			keys = list(level_dict.keys())
			for key in keys:
				level_plus_dicts.append(level_dict[key])
		level_dicts = level_plus_dicts.copy()
		level += 1
		# print()
		# print(level, level_dicts)

	for last_level_dict in level_dicts:
		keys = list(last_level_dict.keys())
		for key in keys:
			for word in last_level_dict[key]:
				words.append(word)

# print(words)
# print(len(words))

# Prepare score
if os.path.isfile(score_path):
	with open(score_path, "r") as score_file:
		score_dict = json.loads(score_file.read())


pygame.init()
info = pygame.display.Info()
screen_size = (info.current_w, info.current_h)
# screen_size = (300, 900)
screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
# screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

pygame.freetype.init()
font_size = 100
delta = 2
font = pygame.font.Font(font_path, font_size)

kana_surface = font.render("Kana", False, (255, 255, 255))
kanji_surface = font.render("Kanji", False, (255, 255, 0))
english_surface = font.render("English", False, (0, 255, 255))
romaji_surface = font.render("Romaji", False, (255, 0, 255))
evaluation_surface = font.render("GLHF", False, (255, 255, 255))
word_count_surface = font.render("1/9001", False, (0, 0, 255))
score_surface = font.render("10/10", False, (0, 255, 0))
previous_score_surface = font.render("10/10", False, (255, 255, 0))
luck_surface = font.render("Congrats", False, (255, 128, 0))

kana_display = True
kanji_display = True
english_display = True
romaji_display = True
evaluation_display = False
word_count_display = False
score_display = False
previous_score_display = False

evaluation_mode = False
evaluation_word_index = -1
word_score = 0
evaluation_score = 0
enter_pressed = False
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LCTRL]:
			running = False
		if score_display == False:
			if keys[pygame.K_BACKSPACE]:
				kana_display = True if (kana_display == False) else False
			if keys[pygame.K_LSHIFT]:
				kanji_display = True if (kanji_display == False) else False
			if keys[pygame.K_RSHIFT]:
				english_display = True if (english_display == False) else False
			if keys[pygame.K_RIGHT]:
				romaji_display = True if (romaji_display == False) else False
			if keys[pygame.K_DOWN]:
				english_display = True if (english_display == False) else False
				romaji_display = True if (romaji_display == False) else False
			if keys[pygame.K_LEFT]:
				kana_display = True if (kana_display == False) else False
				english_display = True if (english_display == False) else False
				romaji_display = True if (romaji_display == False) else False
			if keys[pygame.K_RETURN]:
				if evaluation_mode == True and evaluation_word_index + 1 < len(words):
					kana_display = False
					english_display = False
					romaji_display = False
				if enter_pressed == False and (evaluation_display == True or evaluation_word_index == -1):
					enter_pressed = True
					if evaluation_mode == False:
						index = rd.randint(0, len(words)-1)
						word = words[index]
						# print(word)
					else:
						evaluation_display = False
						previous_score_display = False
						evaluation_score += word_score
						word_score = 0
						evaluation_word_index += 1
						word_count_string = "{0}/{1}".format(min(evaluation_word_index + 1, len(words)), len(words))
						word_count_surface = font.render(word_count_string, False, (0, 0, 255))
						if evaluation_word_index < len(words):
							word = words[evaluation_word_index]
						else: # Evaluation finished
							score_display = True
							previous_score_display = True
							evaluation_display = False
							score = round(100 * evaluation_score / len(words), 2)
							score_string = "{0}/{1} = {2}".format(evaluation_score, len(words), score)
							score_surface = font.render(score_string, False, (0, 255, 0))
							kana_surface = font.render("Finished!", False, (255, 255, 255))
							kanji_surface = font.render("Your score:", False, (255, 255, 0))
							score_dict_copy = score_dict
							for name in level_names[:-1]:
								score_dict = score_dict[name]
							# print(score_dict[level_names[-1]])
							score_string = str(score_dict[level_names[-1]])
							if score_dict[level_names[-1]] < score:
								score_dict[level_names[-1]] = score
								romaji_surface = font.render("== Congratulations! ==", False, (255, 128, 0))
							else:
								romaji_surface = font.render("Good luck improving!", False, (255, 128, 0))
							score_dict = score_dict_copy
							english_surface = font.render("Your previous score:", False, (0, 255, 255))
							previous_score_surface = font.render(score_string, False, (255, 255, 0))
					if evaluation_word_index < len(words):
						kana_surface = font.render(word[0], False, (255, 255, 255))
						kanji_surface = font.render(word[1], False, (255, 255, 0))
						english_surface = font.render(word[2], False, (0, 255, 255))
						romaji_surface = font.render(word[3], False, (255, 0, 255))
						if evaluation_mode:
							if word[1] == "":
								kana_display = True
			else:
				enter_pressed = False
			if evaluation_mode == False:
				if keys[pygame.K_KP4]:
					kana_surface = font.render("Evaluation", False, (255, 255, 255))
					kanji_surface = font.render("starts", False, (255, 255, 0))
					score_dict_copy = score_dict
					for name in level_names[:-1]:
						score_dict = score_dict[name]
					score_string = str(score_dict[level_names[-1]])
					score_dict = score_dict_copy
					english_surface = font.render("Score to beat:", False, (0, 255, 255))
					previous_score_surface = font.render(score_string, False, (255, 255, 0))
					romaji_surface = font.render("", False, (255, 0, 255))
					evaluation_mode = True
					word_count_display = True
					previous_score_display = True
					rd.shuffle(words)
			else:
				if evaluation_word_index > -1 and evaluation_word_index < len(words):
					if keys[pygame.K_KP5]:
						evaluation_surface = font.render("GLHF", False, (255, 0, 0))
						evaluation_display = True
						word_score = 0
					if keys[pygame.K_KP6]:
						evaluation_surface = font.render("OK", False, (0, 255, 0))
						evaluation_display = True
						word_score = 1

	screen.fill(pygame.Color(33, 33, 33))

	if kana_display:
		screen.blit(kana_surface, (font_size/delta, 0))
	if kanji_display:
		screen.blit(kanji_surface, (font_size/delta, screen_size[1]/4))
	if english_display:
		screen.blit(english_surface, (font_size/delta, screen_size[1]/2))
	if romaji_display:
		screen.blit(romaji_surface, (font_size/delta, screen_size[1]*3/4))
	if evaluation_display:
		screen.blit(evaluation_surface, (screen_size[0] - 4*font_size, screen_size[1]/4))
	if word_count_display:
		screen.blit(word_count_surface, (screen_size[0] - 4*font_size, 0))
	if score_display:
		screen.blit(score_surface, (screen_size[0]/2, screen_size[1]/4))
	if previous_score_display:
		screen.blit(previous_score_surface, (screen_size[0] - 4*font_size, screen_size[1]/2))

	pygame.display.flip()
	clock.tick(60) # limits FPS to 60

with open(score_path, "w") as score_file:
	score_json = json.dumps(score_dict)
	score_file.write(score_json)

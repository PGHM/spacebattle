import pygame as pg

pg.mixer.init()
laser_beam_sound = pg.mixer.Sound("assets/sound_effects/laser_beam.wav")

def play_laser_beam_sound():
    laser_beam_sound.play()
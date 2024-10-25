import pygame

from constants import SOUNDS_DIR

class SoundHandler:
    def __init__(self):
        self.sound_on = False
        self.assets_loaded = False
        self.load_music_assets()

    def load_music_assets(self):
        """Load music and sound assets from the specified directory."""
        try:
            # Load and prepare background music using pygame.mixer.music
            pygame.mixer.music.load(SOUNDS_DIR + "/sound_background_music.mp3")
            pygame.mixer.music.set_volume(0.05)
            pygame.mixer.music.play(-1)  # Start playing background music in a loop
            pygame.mixer.music.pause()

            # Load sound effects using pygame.mixer.Sound
            self.game_over_sound = pygame.mixer.Sound(SOUNDS_DIR + "/sound_game_over.wav")
            self.clear_sound = pygame.mixer.Sound(SOUNDS_DIR + "/sound_clear.wav")
            self.rotate_sound = pygame.mixer.Sound(SOUNDS_DIR + "/sound_rotate.wav")
            self.drop_sound = pygame.mixer.Sound(SOUNDS_DIR + "/sound_drop.wav")
            self.hard_drop_sound = pygame.mixer.Sound(SOUNDS_DIR + "/sound_hard_drop.wav") # TODO catch fast drop long press to play this sound

            # Set volumes for sound effects
            self.game_over_sound.set_volume(0.5)
            self.clear_sound.set_volume(0.2)
            self.rotate_sound.set_volume(0.1)
            self.drop_sound.set_volume(0.2)
            self.hard_drop_sound.set_volume(0.2)

            self.assets_loaded = True
            self.toggle_sound()
        except Exception as e:
            print("Error loading sound assets:", e)
            self.assets_loaded = False
            self.sound_on = False

    def toggle_sound(self):
        """Toggle the sound on or off."""
        if not self.assets_loaded:
            return
        self.sound_on = not self.sound_on
        if self.sound_on:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

    def play_game_over_sound(self):
        """Play the game over sound."""
        if self.assets_loaded and self.sound_on:
            pygame.mixer.music.stop()
            self.game_over_sound.play()

    def play_clear_sound(self):
        """Play the clear sound effect."""
        if self.assets_loaded and self.sound_on:
            self.clear_sound.play()

    def play_rotate_sound(self):
        """Play the rotation sound effect for the Tetrimino."""
        if self.assets_loaded and self.sound_on:
            self.rotate_sound.play()

    def play_drop_sound(self):
        """Play the sound effect for dropping the Tetrimino."""
        if self.assets_loaded and self.sound_on:
            self.drop_sound.play()

    def play_hard_drop_sound(self):
        """Play the sound effect for fast dropping the Tetrimino."""
        if self.assets_loaded and self.sound_on:
            self.hard_drop_sound.play()

import random
import pygame
from constants import *
from card import Card

class MemoryGame:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.reset_game()

    def reset_game(self):
        self.cards = self.create_cards()
        self.first_card = None
        self.second_card = None
        self.waiting = False
        self.flip_timer = 0
        self.flip_duration = 1000

    def create_cards(self):
        """Create unique pairs of cards and shuffle them."""
        total_cards = self.grid_size[0] * self.grid_size[1]

        num_unique_icons = total_cards // 2
        selected_icons = random.sample(ICONS, num_unique_icons)  # Ensure unique selection

        paired_icons = selected_icons * 2  # Duplicate icons for pairs
        random.shuffle(paired_icons)  # Shuffle the card order

        return [Card(icon) for icon in paired_icons] # Create pairs of cards

    def draw(self, screen):
        """Draw all cards on the screen."""
        for i, card in enumerate(self.cards):
            x = (i % self.grid_size[0]) * (CARD_SIZE + PADDING) + PADDING
            y = (i // self.grid_size[0]) * (CARD_SIZE + PADDING) + PADDING
            card.draw(screen, x, y)

            if card.is_matched:
                border_color = GREEN  # Green for matched cards
            elif card.is_flipped:
                border_color = RED # Red for flipped but unmatched cards
            else:
                border_color = BLACK  # Default to black for unflipped cards

            card.draw(screen, x, y, border_color)

    def flip_card(self, index):
        """Flip a card and check for matches."""
        if 0 <= index < len(self.cards):
            card = self.cards[index]
            # Allow flipping only if no waiting state and no matches
            if not card.is_flipped and not card.is_matched and not self.waiting:
                card.is_flipped = True
                if self.first_card is None:
                    self.first_card = card
                elif self.second_card is None:
                    self.second_card = card
                    self.check_for_match()

    def check_for_match(self):
        """Check if the two selected cards match."""
        if self.first_card.icon == self.second_card.icon:
            self.first_card.is_matched = True
            self.second_card.is_matched = True
            # Reset selections after a successful match
            self.first_card = None
            self.second_card = None
        else:
            # Cards do not match, start the flip timer
            self.waiting = True
            self.flip_timer = pygame.time.get_ticks()  # Start the timer

    def update(self):
        """Update the game state to manage card visibility after a match check."""
        if self.waiting:
            # Check if the time since the second card was flipped exceeds the duration
            if pygame.time.get_ticks() - self.flip_timer >= self.flip_duration:
                # If both cards are not matched, flip them back
                if self.first_card and self.second_card:
                    if not self.first_card.is_matched and not self.second_card.is_matched:
                        self.first_card.is_flipped = False
                        self.second_card.is_flipped = False
                # Reset the first and second card references
                self.first_card = None
                self.second_card = None
                self.waiting = False  # Reset waiting state after handling

        if self.check_for_win():
            self.reset_game()
            return True  # Return True to indicate the game is won
        return False

    def check_for_win(self):
        """Check if all pairs have been matched."""
        return all(card.is_matched for card in self.cards)

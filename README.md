# Pygame-Collection

A collection of example games I've developed in the process of learning PyGame.

---
### Pong

A classic two-player Pong game developed using PyGame. The objective is to score points by getting the ball past your opponent's paddle while defending your own side.

<details>
<summary>Gameplay Mechanics</summary>

- **Controls**:
  - **Player Paddle**: Use the **Up** and **Down** arrow keys to move the paddle vertically.
  - **Opponent Paddle**: Controlled by a simple AI that tracks the ball's vertical position.

- **Scoring**:
  - Players score a point when the opponent fails to return the ball.
  - The game keeps track of each player's score, and the first player to reach a predefined score (11 points) wins the game.

- **Game Timer**:
  - A timer counts down from a set duration, and if time runs out, the player with the highest score is declared the winner.

- **Visuals**:
  - The game features a minimalist design with a black background and contrasting colors for the paddles and ball.
  - A scoreboard displays the current scores and a timer.


#### Features

- **Smooth Paddle Movement**: The paddles move seamlessly within the boundaries of the game window.
- **Collision Detection**: The ball bounces off the paddles and walls, creating dynamic gameplay.
- **Restart Functionality**: Players can restart the game by clicking on a "Click to Restart" button displayed at the end of the game.

#### How to Play

Run the game by executing the main script:
   ```bash
   python main.py
  ```
</details>

---

### Memory Game

Memory Game is a classic card-matching game where the player flips over cards to find pairs of identical cards. It challenges short-term memory and concentration, requiring the player to remember previously revealed cards to match all pairs in as few moves as possible.

<details>
<summary>Gameplay Mechanics</summary>

- **Controls**:
  - **Mouse**: Click on a card to flip it. Match two identical cards to lock them in the face-up position.

#### Features

- **Grid Size Selection**: Players can choose from different grid sizes, such as 2x2, 3x2, or larger.
- **Dynamic Game Board**: The number of cards and their placement adjust based on the selected grid size.
- **Flip Function**: Click on a card to flip it and reveal its content.
- **Matching Logic**: If two flipped cards are identical, they remain face up otherwise, they flip back.
- **Scoring**: The player can see their current score or number of moves after the game ends.
- **Timer**: The player has access to a timer that tracks the duration it takes to complete the game.
- **Responsive Layout**: The size of the game board and card placement are adjusted to ensure the game looks good even with small grids (like 2x2).

#### How to Play

- At the start of the game, choose a grid size (e.g., 2x2, 3x2, 4x4).
- Click on two cards to flip them over.
- If the cards match, they stay face up; if not, they flip back after a short delay.
- Continue until all pairs of cards are matched!

Run the game by executing the main script:
   ```bash
   python main.py
  ```
</details>

---


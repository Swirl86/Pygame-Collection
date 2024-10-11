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

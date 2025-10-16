# RP_Manzella_Vairo_Mayi_25

## Purple Player Game

A Python game built with Pygame featuring a purple player that must avoid enemies and collect items.

### Features

- **Welcome Screen**: Press SPACE to start the game
- **Player Control**: Move using arrow keys or WASD
- **Obstacles/Enemies**: Red enemies that move automatically across the screen
- **Collisions**: Lose lives when touching enemies, gain points when collecting items
- **Score System**: Collect yellow items for points
- **Increasing Difficulty**: Game becomes harder as you progress through levels
- **End Game Screen**: Shows final score and options to play again or exit
- **Purple Player**: Player is represented by a purple circle

### Installation

1. Install Python 3.7 or higher
2. Install pygame:
   ```bash
   pip install -r requirements.txt
   ```

### How to Play

1. Run the game:
   ```bash
   python game.py
   ```

2. **Controls**:
   - Use arrow keys or WASD to move the purple player
   - Avoid red enemies (they will take away lives)
   - Collect yellow items for points
   - Survive as long as possible!

3. **Game Mechanics**:
   - You start with 3 lives
   - Each enemy collision reduces lives by 1
   - Each item collected gives 10 points
   - Game speed increases with each level
   - New enemies spawn faster as you progress

### Game Screens

- **Welcome Screen**: Shows instructions and waits for SPACE to start
- **Game Screen**: Shows current score, lives, and level
- **Game Over Screen**: Shows final score and options to restart or exit

### Branches

- **Game**: Contains the game implementation
- **ROS**: Reserved for ROS-related code

### Contact

Repository shared with: sacarras@ing.uc3m.es

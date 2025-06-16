# Python Game

## Features

### 1. Pygame Initialization
- The game initializes the Pygame library to manage game functionalities.

### 2. Screen Setup
- The game window is set up with specific dimensions defined in the settings.

### 3. Resource Loading
- Sprites and images are loaded from the assets folder, including the main character sprite sheet and heart image for the health bar.

### 4. Health Bar
- A health bar is displayed on the screen, showing the player's current health using heart images.

### 5. Room Management
- The game features different rooms, each with its own layout and walls. The `Room` class handles the drawing and caching of room surfaces.

### 6. Player Movement
- The player can move around the screen, and their position is updated based on keyboard input.

### 7. Collision Detection
- The player collides with walls, and the game checks for these collisions to prevent the player from moving through walls.

### 8. Door Traversal
- The game checks if the player is at the edge of the screen to move them to a new room.

### 9. Game Loop
- The main game loop handles events, updates the game state, and redraws the screen.

### 10. Caching
- Room surfaces are cached to improve performance when drawing rooms.

### 11. Placeholder Images
- Placeholder images are used for certain game elements, such as the magic feather.

### 12. Font Rendering
- The game uses a specific font to render text on the screen.

### 13. Event Handling
- The game handles various events, including quitting the game and key presses for player actions.

### 14. Smooth Scaling
- Sprites are smoothly scaled to fit the tile size defined in the settings.

### 15. Surface Management
- The game uses Pygame surfaces to manage and draw different game elements.

### 16. Class-level Cache
- The `Room` class uses a class-level cache to store and reuse room surfaces.

### 17. Map Drawing
- The current room is drawn onto a static map surface, which is then blitted onto the screen.

### 18. Player Spawning
- The player is spawned and their position is updated based on the game state.

## How to Run
1. Ensure you have Python, Pygame and Pygbag installed.
2. Run `pygbag --git --template pygbag/static/login.tmpl main.py` to launch the game on URL `http://localhost:8000`

import pygame
import random
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Player settings
PLAYER_SIZE = 20
PLAYER_SPEED = 5

# Enemy settings
ENEMY_SIZE = 15
ENEMY_SPEED = 3

# Item settings
ITEM_SIZE = 10

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = PLAYER_SIZE
        self.speed = PLAYER_SPEED
        
    def move(self, dx, dy):
        # Keep player within screen bounds
        self.x = max(self.size, min(SCREEN_WIDTH - self.size, self.x + dx * self.speed))
        self.y = max(self.size, min(SCREEN_HEIGHT - self.size, self.y + dy * self.speed))
        
    def draw(self, screen):
        pygame.draw.circle(screen, PURPLE, (int(self.x), int(self.y)), self.size)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = ENEMY_SIZE
        self.speed = ENEMY_SPEED
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        
    def move(self, game_speed_multiplier):
        self.x += self.dx * self.speed * game_speed_multiplier
        self.y += self.dy * self.speed * game_speed_multiplier
        
        # Bounce off edges
        if self.x <= self.size or self.x >= SCREEN_WIDTH - self.size:
            self.dx *= -1
        if self.y <= self.size or self.y >= SCREEN_HEIGHT - self.size:
            self.dy *= -1
            
        # Keep within bounds
        self.x = max(self.size, min(SCREEN_WIDTH - self.size, self.x))
        self.y = max(self.size, min(SCREEN_HEIGHT - self.size, self.y))
        
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (int(self.x - self.size), int(self.y - self.size), self.size * 2, self.size * 2))

class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = ITEM_SIZE
        
    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), self.size)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Purple Player Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
        # Game state
        self.state = "welcome"  # welcome, playing, game_over
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_speed_multiplier = 1.0
        
        # Game objects
        self.player = None
        self.enemies = []
        self.items = []
        
        # Timing
        self.enemy_spawn_timer = 0
        self.item_spawn_timer = 0
        self.level_timer = 0
        
    def reset_game(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_speed_multiplier = 1.0
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.enemies = []
        self.items = []
        self.enemy_spawn_timer = 0
        self.item_spawn_timer = 0
        self.level_timer = 0
        
    def spawn_enemy(self):
        # Spawn enemies from edges
        side = random.randint(0, 3)
        if side == 0:  # Top
            x = random.randint(0, SCREEN_WIDTH)
            y = -ENEMY_SIZE
        elif side == 1:  # Right
            x = SCREEN_WIDTH + ENEMY_SIZE
            y = random.randint(0, SCREEN_HEIGHT)
        elif side == 2:  # Bottom
            x = random.randint(0, SCREEN_WIDTH)
            y = SCREEN_HEIGHT + ENEMY_SIZE
        else:  # Left
            x = -ENEMY_SIZE
            y = random.randint(0, SCREEN_HEIGHT)
            
        self.enemies.append(Enemy(x, y))
        
    def spawn_item(self):
        x = random.randint(ITEM_SIZE, SCREEN_WIDTH - ITEM_SIZE)
        y = random.randint(ITEM_SIZE, SCREEN_HEIGHT - ITEM_SIZE)
        self.items.append(Item(x, y))
        
    def check_collisions(self):
        # Check enemy collisions
        for enemy in self.enemies[:]:
            distance = math.sqrt((self.player.x - enemy.x)**2 + (self.player.y - enemy.y)**2)
            if distance < self.player.size + enemy.size:
                self.lives -= 1
                self.enemies.remove(enemy)
                if self.lives <= 0:
                    self.state = "game_over"
                    
        # Check item collisions
        for item in self.items[:]:
            distance = math.sqrt((self.player.x - item.x)**2 + (self.player.y - item.y)**2)
            if distance < self.player.size + item.size:
                self.score += 10
                self.items.remove(item)
                
    def update_level(self):
        # Increase difficulty every 30 seconds
        self.level_timer += 1
        if self.level_timer >= FPS * 30:  # 30 seconds
            self.level += 1
            self.game_speed_multiplier += 0.2
            self.level_timer = 0
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.KEYDOWN:
                if self.state == "welcome":
                    if event.key == pygame.K_SPACE:
                        self.state = "playing"
                        self.reset_game()
                        
                elif self.state == "game_over":
                    if event.key == pygame.K_SPACE:
                        self.state = "welcome"
                    elif event.key == pygame.K_ESCAPE:
                        return False
                        
        return True
        
    def update(self):
        if self.state != "playing":
            return
            
        # Handle player movement
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1
            
        self.player.move(dx, dy)
        
        # Update enemies
        for enemy in self.enemies:
            enemy.move(self.game_speed_multiplier)
            
        # Spawn enemies
        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer >= FPS * (2 - self.level * 0.1):  # Faster spawning with level
            self.spawn_enemy()
            self.enemy_spawn_timer = 0
            
        # Spawn items
        self.item_spawn_timer += 1
        if self.item_spawn_timer >= FPS * 3:  # Every 3 seconds
            self.spawn_item()
            self.item_spawn_timer = 0
            
        # Check collisions
        self.check_collisions()
        
        # Update level
        self.update_level()
        
    def draw_welcome_screen(self):
        self.screen.fill(BLACK)
        title = self.big_font.render("PURPLE PLAYER GAME", True, WHITE)
        subtitle = self.font.render("Press SPACE to start", True, WHITE)
        instructions = [
            "Use ARROW KEYS or WASD to move",
            "Avoid RED enemies",
            "Collect YELLOW items for points",
            "Survive as long as possible!",
            "",
            "Press SPACE to begin"
        ]
        
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
        self.screen.blit(title, title_rect)
        
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
        self.screen.blit(subtitle, subtitle_rect)
        
        for i, instruction in enumerate(instructions):
            text = self.font.render(instruction, True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + i * 30))
            self.screen.blit(text, text_rect)
            
    def draw_game_screen(self):
        self.screen.fill(BLACK)
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(self.screen)
            
        # Draw items
        for item in self.items:
            item.draw(self.screen)
            
        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))
        self.screen.blit(level_text, (10, 90))
        
    def draw_game_over_screen(self):
        self.screen.fill(BLACK)
        
        game_over_text = self.big_font.render("GAME OVER", True, RED)
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        level_text = self.font.render(f"Level Reached: {self.level}", True, WHITE)
        restart_text = self.font.render("Press SPACE to play again", True, WHITE)
        exit_text = self.font.render("Press ESC to exit", True, WHITE)
        
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 10))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))
        exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))
        
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(level_text, level_rect)
        self.screen.blit(restart_text, restart_rect)
        self.screen.blit(exit_text, exit_rect)
        
    def draw(self):
        if self.state == "welcome":
            self.draw_welcome_screen()
        elif self.state == "playing":
            self.draw_game_screen()
        elif self.state == "game_over":
            self.draw_game_over_screen()
            
        pygame.display.flip()
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

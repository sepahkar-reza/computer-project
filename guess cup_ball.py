import pygame
import random
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Find the Ball - Interactive Multi-round Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Cup dimensions
CUP_WIDTH = 80
CUP_HEIGHT = 120
BALL_RADIUS = 20

# Original cup positions
original_positions = [
    (100, 200),
    (260, 200),
    (420, 200)
]
cups = [pygame.Rect(x, y, CUP_WIDTH, CUP_HEIGHT) for x, y in original_positions]

# Font
font = pygame.font.SysFont(None, 36)

# Function to draw cups and optionally ball
def draw_cups(show_ball=False):
    screen.fill(WHITE)
    for i, cup in enumerate(cups):
        pygame.draw.rect(screen, GRAY, cup)
        pygame.draw.rect(screen, BLACK, cup, 3)
        if show_ball and i == ball_index:
            pygame.draw.circle(screen, RED, (cup.centerx, cup.top + 30), BALL_RADIUS)
    pygame.display.update()

# Smooth curved animation between two cups
def animate_curve(cup_a, cup_b, steps=30, amplitude=30):
    start_a = cup_a.topleft
    start_b = cup_b.topleft
    end_a = start_b
    end_b = start_a

    for step in range(1, steps + 1):
        t = step / steps
        offset = math.sin(math.pi * t) * amplitude
        cup_a.topleft = (int(start_a[0] + (end_a[0] - start_a[0]) * t),
                         int(start_a[1] + (end_a[1] - start_a[1]) * t - offset))
        cup_b.topleft = (int(start_b[0] + (end_b[0] - start_b[0]) * t),
                         int(start_b[1] + (end_b[1] - start_b[1]) * t + offset))
        draw_cups(show_ball=False)
        pygame.time.delay(20)

# Shuffle cups multiple times
def shuffle_cups(times=15):
    for _ in range(times):
        a, b = random.sample([0, 1, 2], 2)
        animate_curve(cups[a], cups[b], steps=random.randint(25, 35), amplitude=random.randint(20, 50))
        cups[a], cups[b] = cups[b], cups[a]

# Function to ask player if they want to continue
def ask_continue(score):
    screen.fill(WHITE)
    msg = font.render(f"Current Score: {score}", True, BLUE)
    screen.blit(msg, (SCREEN_WIDTH//2 - msg.get_width()//2, 120))
    cont_msg = font.render("Click YES to continue, NO to quit", True, BLACK)
    screen.blit(cont_msg, (SCREEN_WIDTH//2 - cont_msg.get_width()//2, 180))

    # Draw YES/NO buttons
    yes_button = pygame.Rect(150, 250, 120, 50)
    no_button = pygame.Rect(330, 250, 120, 50)
    pygame.draw.rect(screen, GREEN, yes_button)
    pygame.draw.rect(screen, RED, no_button)
    yes_text = font.render("YES", True, BLACK)
    no_text = font.render("NO", True, BLACK)
    screen.blit(yes_text, (yes_button.centerx - yes_text.get_width()//2, yes_button.centery - yes_text.get_height()//2))
    screen.blit(no_text, (no_button.centerx - no_text.get_width()//2, no_button.centery - no_text.get_height()//2))
    pygame.display.update()

    waiting = True
    choice = False
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if yes_button.collidepoint(mouse_pos):
                    waiting = False
                    choice = True
                elif no_button.collidepoint(mouse_pos):
                    waiting = False
                    choice = False
    return choice

# Main game function
def main():
    global ball_index
    score = 0
    high_score = 0
    round_num = 0

    play = True
    while play:
        round_num += 1
        ball_index = random.randint(0, 2)

        # Show ball briefly
        draw_cups(show_ball=True)
        pygame.time.delay(1000)

        # Shuffle cups
        draw_cups(show_ball=False)
        shuffle_cups(times=15)

        # Wait for player choice
        selected = False
        while not selected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for i, cup in enumerate(cups):
                        if cup.collidepoint(mouse_pos):
                            selected = True
                            if i == ball_index:
                                message = "You found the ball! :)"
                                color = GREEN
                                score += 1
                            else:
                                message = "Wrong cup! :("
                                color = RED
                            draw_cups(show_ball=True)
                            text = font.render(message, True, color)
                            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, 50))
                            score_text = font.render(f"Score: {score}", True, BLUE)
                            screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 100))
                            pygame.display.update()
            pygame.time.Clock().tick(30)

        # Update high score
        if score > high_score:
            high_score = score

        # Pause before asking
        pygame.time.delay(1000)
        play = ask_continue(score)

    # Game over screen
    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, BLACK)
    final_score_text = font.render(f"Final Score: {score}", True, BLUE)
    high_score_text = font.render(f"High Score: {high_score}", True, GREEN)
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 120))
    screen.blit(final_score_text, (SCREEN_WIDTH//2 - final_score_text.get_width()//2, 170))
    screen.blit(high_score_text, (SCREEN_WIDTH//2 - high_score_text.get_width()//2, 220))
    pygame.display.update()
    pygame.time.delay(4000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
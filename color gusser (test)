import pygame
import random
import platform
import ctypes
import time
import numpy as np

# Configuration for easy tuning
config = {
    "ball_speed": 5,          # Ball speed (pixels per frame)
    "bot_speed": 17,          # Bot paddle speed
    "bot_reaction_delay": 4,  # Frames between bot reaction updates
}

# Function to bring pygame window to front on Windows
def bring_window_to_front():
    try:
        user32 = ctypes.WinDLL('user32')
        hwnd = pygame.display.get_wm_info()['window']

        SWP_NOSIZE = 0x0001
        SWP_NOMOVE = 0x0002
        HWND_TOPMOST = -1
        HWND_NOTOPMOST = -2

        # Set window topmost to force front
        user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)
        time.sleep(0.05)  # brief pause for OS
        # Remove topmost so window behaves normally
        user32.SetWindowPos(hwnd, HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)

        # Bring window to foreground
        user32.SetForegroundWindow(hwnd)
    except Exception as e:
        print("Could not bring window to front:", e)

# Fixed function to create stereo beep sound
def create_beep_sound(frequency=440, duration_ms=150, volume=0.5):
    sample_rate = 44100
    n_samples = int(sample_rate * duration_ms / 1000)
    t = np.linspace(0, duration_ms / 1000, n_samples, False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # sine wave

    # Convert to 16-bit signed integers
    audio = np.int16(wave * 32767 * volume)

    # Make stereo by duplicating audio to two channels
    stereo_audio = np.column_stack((audio, audio))

    sound = pygame.sndarray.make_sound(stereo_audio)
    return sound

def play_pong():
    pygame.init()
    pygame.mixer.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PONG")

    if platform.system() == "Windows":
        bring_window_to_front()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    paddle_width, paddle_height = 10, 100
    player1 = pygame.Rect(10, HEIGHT // 2 - 50, paddle_width, paddle_height)
    bot = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 50, paddle_width, paddle_height)

    ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

    # Use config values for speeds
    ball_speed = config["ball_speed"]
    ball_speed_x = ball_speed
    ball_speed_y = ball_speed

    bot_speed = config["bot_speed"]
    bot_reaction_delay = config["bot_reaction_delay"]
    bot_reaction_counter = 0

    score1 = 0
    score2 = 0
    winning_score = 5
    font = pygame.font.Font(None, 50)
    end_font = pygame.font.Font(None, 70)

    paddle_hit_sound = create_beep_sound(frequency=600, duration_ms=100, volume=0.3)
    wall_bounce_sound = create_beep_sound(frequency=400, duration_ms=80, volume=0.3)
    score_sound = create_beep_sound(frequency=800, duration_ms=200, volume=0.4)

    clock = pygame.time.Clock()
    running = True
    game_over = False
    winner_text = ""

    ball_collided = False  # Fix for repeated paddle collision sounds

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and player1.top > 0:
                player1.y -= 6
            if keys[pygame.K_s] and player1.bottom < HEIGHT:
                player1.y += 6

            bot_reaction_counter += 1
            if bot_reaction_counter >= bot_reaction_delay:
                if ball.centery > bot.centery + 7 and bot.bottom < HEIGHT:
                    bot.y += bot_speed
                elif ball.centery < bot.centery - 7 and bot.top > 0:
                    bot.y -= bot_speed
                bot_reaction_counter = 0

            ball.x += ball_speed_x
            ball.y += ball_speed_y

            if ball.top <= 0 or ball.bottom >= HEIGHT:
                ball_speed_y *= -1
                wall_bounce_sound.play()

            if ball.colliderect(player1) or ball.colliderect(bot):
                if not ball_collided:
                    ball_speed_x *= -1
                    paddle_hit_sound.play()
                    ball_collided = True
            else:
                ball_collided = False

            if ball.left <= 0:
                score2 += 1
                score_sound.play()
                ball.center = (WIDTH // 2, HEIGHT // 2)
                ball_speed_x *= -1
            if ball.right >= WIDTH:
                score1 += 1
                score_sound.play()
                ball.center = (WIDTH // 2, HEIGHT // 2)
                ball_speed_x *= -1

            if score1 >= winning_score:
                game_over = True
                winner_text = "🎉 You Win!"
            elif score2 >= winning_score:
                game_over = True
                winner_text = "🤖 Bot Wins!"

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player1)
        pygame.draw.rect(screen, WHITE, bot)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        text1 = font.render(str(score1), True, WHITE)
        text2 = font.render(str(score2), True, WHITE)
        screen.blit(text1, (WIDTH // 4, 20))
        screen.blit(text2, (WIDTH * 3 // 4, 20))

        if game_over:
            winner_surface = end_font.render(winner_text, True, WHITE)
            screen.blit(winner_surface, (WIDTH // 2 - winner_surface.get_width() // 2, HEIGHT // 2 - 50))
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def letters_in_common(a, b):
    return len(set(a) & set(b))

def color_guessing_game():
    colors = [
        'red', 'blue', 'green', 'yellow', 'purple', 'orange',
        'pink', 'brown', 'black', 'white', 'gray', 'cyan',
        'magenta', 'lime', 'teal', 'navy', 'maroon', 'olive',
        'gold', 'silver'
    ]

    total_guesses = 0
    correct_guesses = 0

    print("Welcome to the Color Guessing Game!")
    print("Type the name of the color I am thinking of.")
    print("Type 'quit' or 'exit' anytime to leave the game.")

    while True:
        chosen_color = random.choice(colors)
        # Start guessing loop until correct
        while True:
            guess = input(f"Guess the color ({', '.join(colors)}): ").strip().lower()

            if guess in ["quit", "exit"]:
                print(f"\nThanks for playing! You got {correct_guesses} correct out of {total_guesses} guesses!")
                print("Goodbye!")
                return

            if guess == "1972":
                print("Launching PONG...")
                play_pong()
                print("Back to Color Guessing Game!")
                continue  # ask for guess again without changing chosen color

            if guess not in colors:
                print("Invalid color. Please try again.")
                continue

            total_guesses += 1

            if guess == chosen_color:
                correct_guesses += 1
                print("Correct! 🎉")
                break  # exit guess loop, pick a new color
            else:
                print("Wrong!")
                hint = ""
                if guess[0] == chosen_color[0]:
                    hint = f"Hint: Your guess and the color start with the same letter '{guess[0]}'."
                else:
                    common_letters = letters_in_common(guess, chosen_color)
                    length_diff = len(chosen_color) - len(guess)
                    length_hint = ""
                    if length_diff > 0:
                        length_hint = f" The color is {length_diff} letter{'s' if length_diff > 1 else ''} longer than your guess."
                    elif length_diff < 0:
                        length_hint = f" The color is {abs(length_diff)} letter{'s' if abs(length_diff) > 1 else ''} shorter than your guess."

                    hint = f"Hint: Your guess and the color share {common_letters} letter{'s' if common_letters != 1 else ''}.{length_hint}"

                print(hint)

if __name__ == "__main__":
    color_guessing_game()


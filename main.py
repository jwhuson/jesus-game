import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Prayers to Jesus!!!!!")

# Load the background image and scale it to fit the screen
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the Jesus image
jesus_image = pygame.image.load("jesus-praying-in-the-garden.png").convert_alpha()
jesus_rect = jesus_image.get_rect()
jesus_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)

# Create the prayer text object
prayer_text = ""
font = pygame.font.Font(None, 32)  # Reduced the font size to 32 to make the text smaller
prayer_text_surface = font.render(prayer_text, True, (255, 0, 0))  # Changed the text color to bright red
prayer_text_rect = prayer_text_surface.get_rect()

# Create the text input box
text_input_box = pygame.Rect(SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 50, 400, 50)
active = False

# Create the message surface
message_surface = font.render("Type your prayer and press enter to begin.", True, (255, 255, 255))
message_rect = message_surface.get_rect()
message_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10)

# Create the message surface for the space bar instruction
spacebar_message_surface = None

# Set up the clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the mouse is clicked inside the text input box, set active to True
            if text_input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
        elif event.type == pygame.KEYDOWN:
            if active:
                # If a key is pressed while the text input box is active, add the key to the prayer text
                if event.key == pygame.K_RETURN:
                    # If the return key is pressed, deactivate the text input box, hide the "Type your prayer and press enter to begin." message, and display the message instructing the player to rapidly press the space bar
                    active = False
                    message_surface = None
                    spacebar_message_surface = font.render("Rapidly press the space bar to send your prayer to heaven!", True, (255, 255, 255))
                    spacebar_message_rect = spacebar_message_surface.get_rect()
                    spacebar_message_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
                elif event.key == pygame.K_BACKSPACE:
                    # If the backspace key is pressed, delete the last character from the prayer text
                    prayer_text = prayer_text[:-1]
                else:
                    # If any other key is pressed, add it to the prayer text
                    prayer_text += event.unicode
            elif spacebar_message_surface:
                # If the spacebar message surface is active, check if the space bar is being pressed
                if event.key == pygame.K_SPACE:
                    # If the space bar is being pressed, move the Jesus image up
                    jesus_rect.y -= 10
                    # If the Jesus image is at the top of the screen, stop moving it up
                    if jesus_rect.y <= 0:
                        spacebar_message_surface = None

    # Update the prayer text surface
    prayer_text_surface = font.render(prayer_text, True, (255, 0, 0))  # Changed the text color to bright red

    # Update the prayer text position to be inside the text input box
    prayer_text_rect.midleft = (text_input_box.x + 5, text_input_box.centery)

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the Jesus image
    screen.blit(jesus_image, jesus_rect)

    # Draw the prayer text
    screen.blit(prayer_text_surface, prayer_text_rect)

    # Draw the text input box
    pygame.draw.rect(screen, (255, 255, 255), text_input_box, 2)

    # If the text input box is active, draw the cursor
    if active:
        pygame.draw.line(screen, (255, 255, 255), (text_input_box.x + 5, text_input_box.y + 5), (text_input_box.x + 5, text_input_box.y + text_input_box.height - 5), 2)

    # Draw the message surface
    if message_surface:
        screen.blit(message_surface, message_rect)

    # Draw the spacebar message surface
    if spacebar_message_surface:
        screen.blit(spacebar_message_surface, spacebar_message_rect)

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()


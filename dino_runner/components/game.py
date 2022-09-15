import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.running = False
        self.score = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def generate_text(self, message, position_text, size_text):
        self.message = message
        self.position_text = position_text
        self.size_text = size_text
        font = pygame.font.Font(FONT_STYLE, self.size_text)
        text = font.render(self.message, True, (0, 0, 0))
        text_rec = text.get_rect()
        text_rec.center = (self.position_text)
        self.screen.blit(text, text_rec)

    def draw_score(self):
        self.generate_text(f'Score: {self.score}', (SCREEN_WIDTH - 100, 50), 25)

    def update_score(self):
        self.score += 1

        if self.score % 100 == 0 and self.game_speed < 700:
            self.game_speed += 5

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.half_screen_height = SCREEN_HEIGHT // 2
        self.half_screen_width = SCREEN_WIDTH // 2
        self.screen.fill((255, 255, 255))
        if self.death_count == 0:
            self.generate_text('Press any key to start', (self.half_screen_width, self.half_screen_height), 30)
        else:
            self.generate_text('GAME OVER', (self.half_screen_width, self.half_screen_height), 40)
            self.generate_text('Press any key to Restart', (self.half_screen_width, self.half_screen_height + 50), 30)
            self.generate_text(f'Last score: {self.score}', (SCREEN_WIDTH - 150, 50), 25)
            self.generate_text(f'Deaths: {self.death_count}', (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100), 25)
        self.screen.blit(ICON, (self.half_screen_width - 20, self.half_screen_height - 250))
        pygame.display.update()
        self.handle_events_on_menu()
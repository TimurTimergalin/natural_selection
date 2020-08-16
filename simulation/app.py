import pygame


class App:
    """
    Methods:
        set_variables
        create_sprite_groups
        main_loop
        run

    set_variables:
        Args: None
        Returns: None

        Set constant variables to use it in the simulation

    create_sprite_groups:
        Args: None
        Returns: None

        Create pygame.sprite.Group instances to use it in the simulation

    main_loop:
        Args:
            screen
        Returns: None

        The main loop of the simulation, that displays onto the screen

    run:
        Args:
            x
            y
        Returns: None

        Create screen X*Y and safely run the main loop
    """
    def __init__(self):
        self.set_variables()
        self.create_sprite_groups()

    def set_variables(self):
        """
        set_variables:
        Args: None
        Returns: None

        Set constant variables to use it in the simulation
        """
        self.fps = 60

    def create_sprite_groups(self):
        """
        create_sprite_groups:
        Args: None
        Returns: None

        Create pygame.sprite.Group instances to use it in the simulation
        """
        self.all_sprites = pygame.sprite.Group()
        self.creatures = pygame.sprite.Group()

    def main_loop(self, screen):
        """
        main_loop:
        Args:
            screen
        Returns: None

        The main loop of the simulation, that displays onto the screen
        """
        run = True
        clock = pygame.time.Clock()
        while run:  # Game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            screen.fill((0, 0, 0))
            pygame.display.flip()
            clock.tick(self.fps)

    def run(self, x, y):
        """
        run:
        Args:
            x
            y
        Returns: None

        Create screen X*Y and safely run the main loop
        """
        pygame.init()
        screen: pygame.Surface = pygame.display.set_mode((x, y))
        try:
            self.main_loop(screen)
        finally:
            pygame.quit()

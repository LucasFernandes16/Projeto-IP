def get_collectible(size):
    
    class Collectible(Object):
    
        ANIMATION_DELAY = 3
        def __init__(self, x, y, size, fruit):
        super().__init__(x, y, size, size, name=None)
        self.collecible = load_sprite_sheets("Fruits", fruit, 32, 32, True)
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = 
        self.mask = pygame.mask.from_surface(self.image)


        def draw(self, win):
            win.blit(self.image, (self.rect.x, self.rect.y))

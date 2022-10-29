import sys
import pygame
class AlienInvasion:
    '*** Каласс для управления ресурсами и поведением игры.***'
    def __init__(self):
        '*** Инициирует игру и создает ресурсы.***'
        pygame.init()
        self.screen = pygame.display.set_mode({1200,800})
        pygame.display.set_mode('Alien Invasion')

    def run_game(self):
        '*** Запуск основнога цыкла игры.***'
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

        pygame.display.flip()

if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()
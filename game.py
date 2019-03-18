import time
import pygame
from coin import Coin
from table import Table

table_radius = 100
coin_radius = 25
table = Table((0, 0), table_radius)
width = 500
height = 500
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("COINS")
window.fill((255, 255, 255))
pygame.display.update()
font = pygame.font.SysFont("monospace", 15)
set_of_coins = set()
set_of_coins.add(Coin(table.center, coin_radius))
for coin in set_of_coins:
    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 0, 0), (width // 2 + table.center[0], height // 2 - table.center[1]),
                       table_radius, 1)
    pygame.draw.circle(window, (255, 0, 0), (width // 2 + coin.center[0], height // 2 - coin.center[1]),
                       coin_radius, 1)
    text1 = font.render("YOUR TURN TO PLAY", 1, (0, 0, 0))
window.blit(text1, (width // 2 - 110, 20))
pygame.display.update()
end_of_game = False
while not end_of_game:
    pygame.time.delay(50)
    pos = (0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_of_game = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(window, (255, 255, 255), (width // 2 - 110, 20, 250, 20))
            text1 = font.render("COMPUTERS TURN TO PLAY", 1, (0, 0, 0))
            window.blit(text1, (width // 2 - 110, 20))
            pygame.display.update()
            pos = pygame.mouse.get_pos()
            x = pos[0] - width // 2
            y = height // 2 - pos[1]
            print(x, y)
            legal_move = True
            users_coin = Coin((x, y), coin_radius)
            pygame.draw.circle(window, (255, 0, 0), (width // 2 + users_coin.center[0], height // 2 - users_coin.center[1]),
                               coin_radius, 1)
            pygame.display.update()
            if not table.surrounds(users_coin):
                legal_move = False
            for c in set_of_coins:
                if users_coin.intersect(c):
                    legal_move = False
                    break
            if legal_move:
                computers_x = table.center[0] - (x - table.center[0])
                computers_y = table.center[1] - (y - table.center[1])
                computers_coin = Coin((computers_x, computers_y), coin_radius)
                print("User: (", x, ", ", y, ")")
                time.sleep(2)
                print("Computer: (", computers_x, ", ", computers_y, ")")
                set_of_coins.add(users_coin)
                set_of_coins.add(computers_coin)
                pygame.draw.rect(window, (255, 255, 255), (width // 2 - 110, 20, 250, 20))
                text1 = font.render("YOUR TURN TO PLAY", 1, (0, 0, 0))
                window.blit(text1, (width // 2 - 110, 20))
                pygame.draw.circle(window, (255, 0, 0),
                                   (width // 2 + computers_coin.center[0], height // 2 - computers_coin.center[1]),
                                   coin_radius, 1)
                pygame.display.update()
            else:
                pygame.draw.rect(window, (255, 255, 255), (width // 2 - 110, 20, 250, 20))
                text1 = font.render("GAME OVER, COMPUTER WINS", 1, (0, 0, 0))
                window.blit(text1, (width // 2 - 110, 20))
                pygame.display.update()
                end_of_game = True
                time.sleep(5)
print("End of game")
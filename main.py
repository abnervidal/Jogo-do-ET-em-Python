import pygame
pygame.init()

largura = 0
altura = 700
velocidade = 10


tela = pygame.display.set_mode((1200,700))
pygame.display.set_caption('A fuga do ET')

tela_aberta=True


mat = [[1,2,3],[4,5,6],[7,8,9]]

mapa01 = [
'. . . . . . . . . . . . . . . . . . . . . . . .'
'. . . . . . . . . . . . . . . . . . . . . . . .'
'. . . . . . . . . . . . . . . . . . . . . . . .'
'. . . . . . . . . . . . . . . . . . . . . . . .'
'. . . . . . . . . . . . . . . . . . . . . . . .'
'. . . . . . . . . . . . . . . . . . . . . . . .'
'. . . . . . . . . . . . . . . . . . . . . . . .'
'. . . . . . . . . . . . . . . . . . . . . . . .'
'. . . . . X X X X . . . . . . . . . . . . . . .'
'. . . . . . . . . . X X X X . . . . . . . . . .'
'. . . . . . . . . . . . . . . X X X X . . . . .'
'. . . . . . . . . . . . . . . . . . . . X X X X'
'. . . . . . . . . . . . . . . . . . . . . . . .'
'X X X X X X X X X X X X X X X X X X X X X X X X'
]

def draw_window(current_map):
	for y in range(len(current_map)):
		for x in range(len(current_map[y])):

while tela_aberta:
	pygame.time.delay(50)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			tela_aberta=False

	comandos = pygame.key.get_pressed()
	if comandos[pygame.K_UP]:
		altura-= velocidade
	if comandos[pygame.K_DOWN]:
		altura+= velocidade
	if comandos[pygame.K_RIGHT]:
		largura+= velocidade
	if comandos[pygame.K_LEFT]:
		largura-= velocidade

	tela.fill((0,0,0))
	pygame.draw.circle(tela, (0,245,0), (largura,altura),10)
	pygame.display.update()		
			
pygame.quit()
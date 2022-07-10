import pygame
import random

pygame.init()

largura = 1200
altura = 600
tela_aberta = True
atirar_nave = False
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('A fuga do ET')

#carregar imagem de fundo
imagem = pygame.image.load('fundo.jpg').convert_alpha()
imagem = pygame.transform.scale(imagem,(largura,altura))

alien = pygame.image.load('nave.png').convert_alpha()
alien = pygame.transform.scale(alien, (100,100))

aviao = pygame.image.load('aviao.png').convert_alpha()
aviao = pygame.transform.scale(aviao, (140,90))


lazer = pygame.image.load('tiro.png').convert_alpha()
lazer = pygame.transform.scale(lazer, (75,38))

missil = pygame.image.load('foguete.png').convert_alpha()
missil = pygame.transform.scale(missil, (60,40))

alien_x = 0
alien_y = 0


aviao_x = 1200
aviao_y = 300

vel_missil = 0
missil_x = 1250
missil_y = 320

vel_lazer = 0
lazer_x = 0
lazer_y = 37

pontos = 0
vida = 3

fonte = pygame.font.SysFont('rainyhearts.ttf', 25)

alien_rect = alien.get_rect()
aviao_rect = aviao.get_rect()
lazer_rect = lazer.get_rect()
missil_rect = missil.get_rect()

def respawn_aviao():
	altura = 1350 
	largura = random.randint(1, 480)
	
	return[altura, largura]
def respawn_lazer():
	atirar_nave = False
	respawn_lazer_x = alien_x
	respawn_lazer_y = alien_y + 37
	vel_lazer = 0
	return[respawn_lazer_x,respawn_lazer_y, atirar_nave, vel_lazer]
def colisao():
	global pontos
	if alien_rect.colliderect(aviao_rect) or aviao_rect.x == 80:
		pontos -= 0
		return True
	elif lazer_rect.colliderect(aviao_rect):
		pontos += 5
		return True
	else:
		return False
def colisao_missil():
	global vida
	if alien_rect.colliderect(aviao_rect) or aviao_rect.x == 80:
		vida -= 1
		return True
	elif missil_rect.colliderect(alien_rect):
		vida -= 1
		return True
	else:
		return False 

while tela_aberta:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			tela_aberta = False	 

	tela.blit(imagem, (0,0))

	repit_x = largura % imagem.get_rect().width
	tela.blit(imagem, (repit_x - imagem.get_rect().width, 0))
	if repit_x < 1200:
		tela.blit(imagem, (repit_x, 0))
	#movimento
	largura -= 1
	aviao_x -= 2.5
	missil_x -= 2.5
	

	
	tela.blit(lazer,(lazer_x, lazer_y))
	tela.blit(alien,(alien_x, alien_y))
	tela.blit(missil,(missil_x, missil_y))
	tela.blit(aviao,(aviao_x, aviao_y))
	
	
	lazer_x += vel_lazer
	missil_x -= vel_missil

	alien_rect.x = alien_x
	alien_rect.y = alien_y

	aviao_rect.x = aviao_x
	aviao_rect.y = aviao_y

	lazer_rect.x = lazer_x
	lazer_rect.y = lazer_y

	missil_rect.x = missil_x
	missil_rect.y = missil_y

	comando = pygame.key.get_pressed()
	if comando[pygame.K_UP] and alien_y > 0:
		alien_y -= 2
		if not atirar_nave:
			lazer_y -= 2
	if comando[pygame.K_DOWN] and alien_y < 480:
		alien_y += 2
		if not atirar_nave:
			lazer_y += 2
	if comando[pygame.K_SPACE]:
		atirar_nave = True
		vel_lazer = 6

	if vida == 0:
		tela_aberta = False
	if colisao_missil():
		missil_x = 100000
		missil_y = 100000
	if aviao_x == 80 or colisao():
		aviao_x = respawn_aviao()[0]
		aviao_y = respawn_aviao()[1]
		missil_x = aviao_x + 50
		missil_y = aviao_y + 20
	if aviao_x == 800:
		vel_missil = 4
	if lazer_x == 1200 or colisao():
		lazer_x, lazer_y, atirar_nave,vel_lazer = respawn_lazer()

	#Carregar Fonte
	score = fonte.render(f'PONTOS: {int(pontos)}',True,(0,0,0))
	life = fonte.render(f'VIDAS: {int(vida)}', True, (0,0,0))
	tela.blit(life, (1050,550))
	tela.blit(score, (50,550))
	print(pontos)
	print(vida)
	pygame.display.update()


	#classes e adicionar outros arquivos!
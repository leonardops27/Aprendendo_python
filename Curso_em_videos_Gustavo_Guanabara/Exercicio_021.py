
print('''
Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
''')
import pygame
pygame.init()
comando = 0
while comando != 4:
    print('''
    [1] Voltar  [2] Tocar   [3] Avançar
                [5] Parar
        ''')
    comando = int(input('Opção: '))
    if comando == 1:
        pygame.mixer.music.rewind()
    elif comando == 2:
        pygame.mixer.music.load('gigi-bla.mp3')
        volume = pygame.mixer.music.set_volume(5)
        tocar = pygame.mixer.music.play()
        stand_bye = pygame.event.wait()
        comando = int(input('Opção: '))
        if comando == 5:
            break
    elif comando == 3:
        print('Descobrir')
    elif comando == 5:
        pygame.mixer.music.stop()
    else:
        break

print('''
Bom, fiz tocar como pedido, estou fazendo modificações e procurando novos aprendizados. Continuo aos poucos aqui.
''')

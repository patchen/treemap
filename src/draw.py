'''
Draw functions
'''
import pygame


def find_dir(mouseX, mouseY, list_data):
    '''(int, int, list) -> tuple
    Return a string of the file and size of the file given its current
    mouse coordinate, and a list of data containing the coordinate of
    all directories'''

    for node in list_data:
        if mouseX <= node.x2 and mouseX >= node.x1 and mouseY <= node.y2 \
                                                    and mouseY >= node.y1:
            return node.path, node.size
    return "", 0


def blit_mousedir(screen, blit_size, mouseX, mouseY, list_data):
    '''(surface, int, int, list) -> None
    Blit the directory the mouse is hovering over, onto the bottom left corner
    of the screen and the size onto the bottom right '''

    pygame.draw.rect(screen, (0, 0, 0), (0, 500, 1024, 525))
    font = pygame.font.Font(None, 16)
    text_surface = font.render('Current Directory:' + find_dir(mouseX, \
                                mouseY, list_data)[0], 1, (255, 255, 255))
    text_size = font.render('Size: ' + str(find_dir(mouseX, mouseY, \
                                list_data)[1]) + ' Bytes', 1, (255, 255, 255))
    text_pos = (0, blit_size[1] - font.get_linesize())
    text_pos2 = (900, blit_size[1] - font.get_linesize() * 2)
    screen.blit(text_surface, text_pos)
    screen.blit(text_size, text_pos2)

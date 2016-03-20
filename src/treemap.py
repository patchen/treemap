from media import *
import os
import os.path
from file_node import *
from random import randint
import pygame
from tiling import tile
from draw import blit_mousedir


def random_color():
    '''(None)-> Tuple
    Return a random color as a Tuple'''

    return (randint(1, 254), randint(1, 254), \
             randint(1, 254))


def get_size(d):
    '''(Node) -> float
    Return the size of d, a file or directory.'''

    if os.path.isdir(d):
        size = 0
        for filename in os.listdir(d):
            subitem = os.path.join(d, filename)
            size += get_size(subitem)
    else:
        size = os.path.getsize(d)
    return size


def build_tree(d, area=0):
    '''(Directory, float) -> Node
    Return the node that is the root of the tree of files and directories
    starting from d, a directory.'''

    if area == 0:
        root = DirectoryNode(get_size(d), (255, 255, 255), 1024 * 500, str(d))
    else:
        root = DirectoryNode(get_size(d), random_color(), area, str(d))
    for filename in os.listdir(d):
        subitem = os.path.join(d, filename)
        if os.path.isdir(subitem):
            try:
                root.children.append(build_tree(subitem, \
                            float(get_size(subitem)) / root.size * root.area))
            except ZeroDivisionError:
                root.children.append(build_tree(subitem))
        else:
            try:
                root.children.append(FileNode(get_size(subitem), \
                                    random_color(), float(get_size(subitem)) /
                                    root.size * root.area, str(subitem)))
            except ZeroDivisionError:
                root.children.append(FileNode(get_size(subitem), \
                                        random_color(), 0, str(subitem)))
    return root


if __name__ == "__main__":
    # Build Tree
    while True:
        d = choose_folder()
        if os.path.isdir(d):
            break
    root = build_tree(d)

    # Initialize pygame
    pygame.init()
    screen_size = (1024, 525)
    screen = pygame.display.set_mode(screen_size)
    blit_size = (1024, 525)
    blitscreen = pygame.display.set_mode(screen_size)
    screen.fill((0, 0, 0))
    data = tile(screen, root, 1024, 500)
    data = data[:-1]
    running = True

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            blit_mousedir(blitscreen, blit_size, mouseX, mouseY, data)
        pygame.display.flip()

'''
Tiling Functions
'''
from file_node import DirectoryNode
import pygame


def tile(screen, root, w, h):
    '''(Surface, Node, float, float) -> list
    Call to recursive tile'''

    l = []
    _tile(screen, root, (0, 0), (w, h), l)
    return l


def _tile(screen, root, start, end, l):
    '''(surface, node, tuple, tuple, list) -> None
    The recursive tiling algorithm'''
    children = root.children
    if not children:
        pygame.draw.rect(screen, root.colour, (start[0], start[1],\
                                    end[0] - start[0], end[1] - start[1]))
        root.x1, root.y1, root.x2, root.y2 = start[0], start[1], end[0], end[1]
        l.append(root)
    else:
        if children[0].size == 0:
            if children[1:]:
                root.children = root.children[1:]
                _tile(screen, root, start, end, l)
        elif end[0] - start[0] > end[1] - start[1]:
            width = children[0].area / (end[1] - start[1])
            if isinstance(children[0], DirectoryNode):
                _tile(screen, children[0], start, (start[0] + width,\
                                                    end[1]), l)
                pygame.draw.rect(screen, (255, 255, 255), (start[0], start[1],\
                                    width, end[1] - start[1]), 5)
            else:
                pygame.draw.rect(screen, children[0].colour, (start[0], \
                                        start[1], width, end[1] - start[1]))
                children[0].x1, children[0].y1, children[0].x2, children[0].y2\
                            = start[0], start[1], start[0] + width, end[1]
                l.append(children[0])
            if children[1:]:
                root.children = root.children[1:]
                _tile(screen, root, (start[0] + width, start[1], l), end, l)
        else:
            height = children[0].area / (end[0] - start[0])
            if isinstance(children[0], DirectoryNode):
                _tile(screen, children[0], start, (end[0], start[1] +\
                                                    height), l)
                pygame.draw.rect(screen, (255, 255, 255), (start[0], start[1],\
                                    end[0] - start[0], height), 5)
            else:
                pygame.draw.rect(screen, children[0].colour, \
                            (start[0], start[1], end[0] - start[0], height))
                children[0].x1, children[0].y1, children[0].x2, children[0].y2\
                            = start[0], start[1], end[0], start[1] + height
                l.append(children[0])
            if children[1:]:
                root.children = root.children[1:]
                _tile(screen, root, (start[0], start[1] + height), end, l)

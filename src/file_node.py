class FileNode(object):
    '''A node representing a file.'''

    def __init__(self, size, colour, area, path):
        '''(FileNode, int, tuple, float, string) -> None
        Constructor'''

        self.size = size
        self.colour = colour
        self.area = area
        self.path = path


class DirectoryNode(FileNode):
    '''A FileNode representing a directory.'''

    def __init__(self, size, colour, area, path):
        '''(DirectoryNode, int, tuple, float, string) -> None
        Constructor'''

        FileNode.__init__(self, size, colour, area, path)
        self.children = []

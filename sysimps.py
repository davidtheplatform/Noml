try:
    import termios
    import sys, tty
    
    def rgetch(read=1):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(read)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
    
    def getch(read=1):
        chars = []
        for _ in range(read):
            firstChar = rgetch()
            if firstChar == '\x1b':
                chars.append({"[A": "up", "[B": "down", "[C": "right", "[D": "left"}[getch() + getch()])
            else:
                chars.append(firstChar)
        return chars[0] if len(chars) == 1 else chars
except ImportError:
    from msvcrt import getch as rgetch
    
    def getch(read=1):
        chars = []
        for _ in range(read):
            firstChar = rgetch()
            if firstChar == b'\xe0':
                chars.append({"H": "up", "P": "down", "M": "right", "K": "left"}[getch()])
            else:
                chars.append(firstChar)
        return chars[0] if len(chars) == 1 else chars
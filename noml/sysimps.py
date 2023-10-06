try:
    import termios
    import sys, tty
    
    def rgetch(read=1):
        """
        Reads a character from the standard input without echoing it to the screen.

        :param read: (int) The number of characters to read. Default is 1.
        :return: (str) The character read from the standard input.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(read)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
    
    def getch(read=1):
        """
        Returns a character or a list of characters read from the input. By default, it reads a single character.
        
        :param read: An optional integer specifying the number of characters to read. Defaults to 1.
        :type read: int
        
        :return: Returns a character if only one character is read, otherwise returns a list of characters.
        :rtype: str or list[str]
        """
        chars = []
        for i in range(read):
            firstChar = rgetch()
            if firstChar == '\x1b':
                chars.append({"[A": "up", "[B": "down", "[C": "right", "[D": "left"}[getch() + getch()])
            else:
                chars.append(firstChar)
        return chars[0] if len(chars) == 1 else chars

except ImportError:
    from msvcrt import getch as rgetch
    
    def getch(read=1):
        """
        Retrieves the next character or characters from the input stream.

        :param read: (optional) The number of characters to read. Defaults to 1.
        :type read: int
        :return: The retrieved character(s) from the input stream.
        :rtype: str or list
        """
        chars = []
        for i in range(read):
            firstChar = rgetch()
            if firstChar == b'\xe0':
                chars.append({"H": "up", "P": "down", "M": "right", "K": "left"}[getch()])
            else:
                chars.append(firstChar)
        return chars[0] if len(chars) == 1 else chars
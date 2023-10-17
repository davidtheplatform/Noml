from os import listdir
from os.path import exists, abspath, isfile, isdir, join, relpath
import sys
if getattr(sys, 'frozen', False):
    from noml.sysimps import getch
    from noml.commands import clear, echo, tput
else:
    from sysimps import getch
    from commands import clear, ehco, tput

class Global:
    windows = []


class WindowsManager:
    def __init__(self):
        self.windows = []

    def append(self, window):
        """
        Append a window to the list of windows.

        Args:
            window: The window object to append.

        Return:
            None
        """
        self.windows.append(window)

    def pop(self):
        """
        Remove and return the last window in the list of windows.
        """
        self.windows.pop()

    def remove(self, window):
        """
        Remove a window from the list of windows.

        Parameters:
            window (object): The window object to be removed.

        Returns:
            None
        """
        self.windows.remove(window)


# Create an instance of the WindowsManager class
windows_manager = WindowsManager()


def word_at_idx(input_string, index):
    words = input_string.split()
    current_index = 0
    for word in words:
        word_start = current_index
        word_end = current_index + len(word)
        if word_start <= index < word_end:
            return word
        current_index = word_end + 1
    return None


def windows():
    windows_manager.append("Windows Manager")
    while True:
        clear()
        for idx, window in enumerate(Global.windows):
            print(f"{idx+1}. {window}")

        char = getch()

        if char == "q":
            windows_manager.pop()
            return


def filestructure_render(directory, current, indentation=0, doabspath=True):
    print(f"{' ' * indentation + ('|---- ' if indentation > 0 else '')}{abspath(directory) if doabspath else directory} ----|")

    for item in listdir(directory):
        item_path = join(directory, item)
        if isfile(item_path):
            if current and item_path == current:
                print(
                    f"{' ' * (indentation+2)}|---- [{abspath(item_path) if doabspath else item_path}]")
            else:
                print(
                    f"{' ' * (indentation+2)}|---- {abspath(item_path) if doabspath else item_path}")
        elif isdir(item_path):
            filestructure_render(
                item_path, current, indentation=indentation+2, doabspath=doabspath)


def filestructure(directory, current=None):
    windows_manager.append("Filesystem Window")
    doabspath = True
    current = abspath(current) if current else None
    while True:
        clear()
        filestructure_render(abspath(directory), current, doabspath=doabspath)

        char = getch()
        if char == "q":
            windows_manager.pop()
            return
        elif char == "a":
            doabspath = not doabspath
        elif char == "j":
            target = input("Target: ")
            current = abspath(target)
            directory = "/".join(abspath(target).split("/")[:-1])
        elif char == "o":
            editor(current)


def editor(filename):
    windows_manager.append(f"Editor Window ({filename})")
    lines = open(filename, "r").readlines()
    for idx, line in enumerate(lines):
        lines[idx] = [char for char in line.replace("\n", "")]
    pointer = [0, 0]
    linenumbers = False
    visualeditor = False

    while True:
        clear()
        print(f"--- {filename} ---")
        for idx, line in enumerate(lines):
            print((f"{str(idx+1)}. " if linenumbers else "") + "".join([("\033[33m" + ("_" if char == " " else ("____" if char == "\t" else char)) + "\033[0m") if (
                pointer[0] == idx and pointer[1] == char_idx) else ("    " if char == "\t" else char) for char_idx, char in enumerate(line)]))
        print("------")

        if not visualeditor:
            inp = input(">")

            cmdname = inp.split(" ")[0]
            try:
                cmdargs = inp.split(" ")[1:]
            except:
                cmdargs = []

            if cmdname in ("q", "quit"):
                windows_manager.pop()
                return
            elif cmdname in ("qn", "quitnoml"):
                tput("cnorm")
                echo("")
                clear()
                exit()
            elif cmdname in ("m", "move"):
                pointer[1] += int(cmdargs[0])
            elif cmdname in ("mw", "moveword"):
                current_line = "".join([x for x in lines[pointer[0]]])
                words = current_line.split()
                word_idx = words.index(word_at_idx(current_line, pointer[1]))
                pointer[1] = current_line.index(
                    words[word_idx + int(cmdargs[0])])
            elif cmdname in ("ml", "moveline"):
                pointer[0] += int(cmdargs[0])
            elif cmdname in ("r", "replace"):
                lines[pointer[0]][pointer[1]] = cmdargs[0]
            elif cmdname in ("rw", "replaceword"):
                current_line = "".join([x for x in lines[pointer[0]]])
                words = current_line.split()
                word_idx = words.index(word_at_idx(current_line, pointer[1]))
                words[word_idx] = cmdargs[0]
                current_line = " ".join([x for x in words])
                lines[pointer[0]] = [char for char in current_line]
            elif cmdname in ("rl", "replaceline"):
                lines[pointer[0]] = [char for char in cmdargs[0]]
            elif cmdname in ("f", "find"):
                current_line = "".join([x for x in lines[pointer[0]]])
                pointer[1] = current_line.index(cmdargs[0])
            elif cmdname in ("o", "open", "j", "jump"):
                clear()
                editor(cmdargs[0])
            elif cmdname in ("s", "save"):
                with open(filename, "w") as wf:
                    content = ""
                    for line in lines:
                        for char in line:
                            content += char
                        content += "\n"
                    wf.write(content)
            elif cmdname in ("ln", "linenumbers"):
                linenumbers = not linenumbers
            elif cmdname in ("v", "visualeditor"):
                visualeditor = not visualeditor
            elif cmdname in ("fs", "filestructure"):
                filestructure("./", filename)
            elif cmdname in ("w", "windows"):
                windows()
            else:
                pass
        else:
            inp = getch()
            current_line = lines[pointer[0]]

            if inp == "`":
                visualeditor = not visualeditor
            elif inp == "\r":
                line = lines[pointer[0]][pointer[1]:]
                del lines[pointer[0]][pointer[1]:]
                lines.insert(pointer[0]+1, [char for char in line])
                pointer[0] += 1
                pointer[1] = 0
            elif inp == "\x7f":
                if not pointer[1] == 0:
                    del current_line[pointer[1]]
                    pointer[1] -= 1
            elif inp == "right":
                pointer[1] += 1
            elif inp == "left":
                pointer[1] -= 1
            elif inp == "up":
                pointer[0] -= 1
                if len(lines[pointer[0]]) < len(lines[pointer[0]+1]):
                    pointer[1] = len(lines[pointer[0]])-1
            elif inp == "down":
                pointer[0] += 1
                if len(lines[pointer[0]]) < len(lines[pointer[0]-1]):
                    pointer[1] = len(lines[pointer[0]])-1
            else:
                current_line.insert(pointer[1]+1, inp)
                pointer[1] += 1


def run():
    windows_manager.append("Starting Window")
    window = ""
    file = ""

    while True:
        clear()
        print("------")
        print("NOML is a text editor that is meant to come with absolutely no configuration or advanced features at all.")
        print("This allows for maximum customization, this text editor is designed for users that want their experience to be as personal as possible.")
        if window == "file":
            clear()
            editor(file)
            window = ""
            continue
        else:
            print("------")
        inp = input(">")

        cmdname = inp.split(" ")[0]
        try:
            cmdargs = inp.split(" ")[1:]
        except:
            cmdargs = []

        try:
            if cmdname in ("q", "quit", "qn", "quitnoml"):
                windows_manager.pop()
                return
            elif cmdname in ("o", "open"):
                window = "file"
                if exists(cmdargs[0]):
                    file = cmdargs[0]
                else:
                    raise FileNotFoundError
            elif cmdname in ("n", "new"):
                try:
                    file = cmdargs[0]
                except:
                    file = "untitled"
                with open(file, "w") as opened_file:
                    opened_file.write(" ")
                window = "file"
            elif cmdname in ("fs", "filestructure"):
                filestructure("./")
            elif cmdname in ("w", "windows"):
                windows()
            else:
                pass
        except Exception as e:
            print(e)
            window = ""
            file = ""
            print("\033[0;31mERROR\033[0m")
            getch()

import os
import os.path
import sysimps

class Global:
	windows = []

def word_at_idx(input_string, index):
    words = input_string.split()
    current_index = 0
    for word in words:
        if current_index <= index < current_index + len(word):
            return word
        current_index += len(word) + 1
    return None

def windows():
    Global.windows.append("Windows Manager")
    while True:
        os.system("clear")
        print("\n".join(f"{idx+1}. {window}" for idx, window in enumerate(Global.windows)))

        char = getch()

        if char == "q":
            Global.windows.pop()
            return

def filestructure_render(directory, current, indentation=0, doos.path.abspath=True):
    print(f"{' ' * indentation + ('|---- ' if indentation > 0 else '')}{os.path.abspath(directory) if doabspath else directory} ----|")

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            if current and item_path == current:
                print(f"{' ' * (indentation+2)}|---- [{os.path.abspath(item_path) if doabspath else item_path}]")
            else:
                print(f"{' ' * (indentation+2)}|---- {os.path.abspath(item_path) if doabspath else item_path}")
        elif os.path.isdir(item_path):
            filestructure_render(item_path, current, indentation=indentation+2, doabspath=doabspath)


def filestructure(directory, current=None):
	Global.windows.append("Filesystem Window")
	doabspath = True
	current = os.path.abspath(current)
	while True:
		os.system("clear")
		filestructure_render(os.path.abspath(directory), current, doabspath=doabspath)

		char = sysimps.getch()
		if char == "q":
			Global.windows.pop()
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
	Global.windows.append(f"Editor Window ({filename})")
	lines = open(filename, "r").readlines()
	for idx, line in enumerate(lines):
		lines[idx] = [char for char in line.replace("\n", "")]
	pointer = [0, 0]
	linenumbers = False
	visualeditor = False

	while True:
		system("clear")
		print(f"--- {filename} ---")
		for idx, line in enumerate(lines):
			print((f"{str(idx+1)}. " if linenumbers else "") + "".join([("\033[33m" + ("_" if char == " " else ("____" if char == "\t" else char)) + "\033[0m") if (pointer[0] == idx and pointer[1] == char_idx) else ("    " if char == "\t" else char) for char_idx, char in enumerate(line)]))
		print("------")

		if not visualeditor:
			inp = input(">")

			cmdname = inp.split(" ")[0]
			try:
				cmdargs = inp.split(" ")[1:]
			except:
				cmdargs = []

			if cmdname in ("q", "quit"):
				Global.windows.pop()
				return
			elif cmdname in ("qn", "quitnoml"):
				system("tput cnorm")
				system('echo -n -e "\033]0;\007"')
				system("clear")
				exit()
			elif cmdname in ("m", "move"):
				pointer[1] += int(cmdargs[0])
			elif cmdname in ("mw", "moveword"):
				current_line = "".join([x for x in lines[pointer[0]]])
				words = current_line.split()
				word_idx = words.index(word_at_idx(current_line, pointer[1]))
				pointer[1] = current_line.index(words[word_idx + int(cmdargs[0])])
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
				system("clear")
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
	Global.windows.append("Starting Window")
	window = ""
	file = ""

	while True:
		system("clear")
		print("------")
		print("NOML is a text editor that is meant to come with absolutely no configuration or advanced features at all.")
		print("This allows for maximum customization, this text editor is designed for users that want their experience to be as personal as possible.")
		if window == "file":
			system("clear")
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
				Global.windows.pop()
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
				system(f"echo ' ' > {file}")
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

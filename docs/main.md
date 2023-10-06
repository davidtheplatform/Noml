Noml Documentation
------------------
Welcome to Noml's documentation! This will cover what you can do with Noml, by default you will be brought to a home screen where you can type commands. So first we are going to cover which commands you can use.

# Commmands
-----------
Format: short <args> <optargs?> (long) (mode) - desc

q (quit) - This command will quit the current window.
qn (quitnoml) - This command will quit Noml.
o/j <path> (open/jump) (all/editor) - This command will open the file at the provided path.
n <path?> (new) - This command will create a file at the provided path, if no path is provided it will create a file in the current directory with the name "untitled".
fs (filestructure) - This command will open [filestructure mode](#filestructure)
w (windows) - This command will open [windows manager](#windows)
m <amount> (move) (editor) - This command will move the cursor the specified amount of characters horizontally, use negative numbers for moving back.
mw <amount> (moveword) (editor) - This command will move the cursor the specified amount of words horizontally.
ml <amount> (moveline) (editor) - This command will move the cursor the specified amount of lines vertically.
r <char> (replace) (editor) - This command will replace the character under the cursor with the specified character.
rw <word> (replaceword) (editor) - This command will replace the current word with the specified word.
rl <line> (replaceline) (editor) - This command will replace the current line with the specified line.
f <text> (find) (editor) - This command will find the first occurence of the provided text in the current line.
s (save) (editor) - This command will save the current file.
ln (linenumbers) (editor) - This will toggle line numbers.
v (visualeditor) (editor) - This will open [visual editor mode](#visual-editor)

# Editor
--------
The editor interface will first show the filename then the content of the file. The cursor is represented by the yellow and can be moved, it will be used in commands.
If the cursor is on a space, it will show as "_". If the cursor is on a tab, it will show as "____".
Below that is the commands interface, here editor-specific commands can also be done.

# Visual Editor
---------------
The visual editor can be entered by using the "v" command in the editor, the visual editor is a visual interface for people who don't want to use commands.
You can use arrow keys to move the cursor.
You can type characters like in any other text editor and you can use backslash to erase characters.
Pressing enter will create a new line, if you were in the middle of the previous line the content from the middle to the end will be moved to the new line.
You can type "`" to exit the visual editor. The "`" was picked because it is the least used character on the QWERTY keyboard.

# Filestructure
---------------
The filestructure can be entered using the "fs" command, the filestructure will allow you to move around your filesystem and open files.
If you run with a file opened, your current file will be shown.
You can toggle absolute paths off and on by pressing "a".
You can jump to files by pressing "j" and typing in your target.
You can open your current file by pressing "o".
You can exit by pressing "q".

# Windows
---------
In Noml, when you open a new mode such as main, editor or filestructure. You are creating a new window.
Each window has an associated mode and metadata about it such as for an editor window it will have the path and buffer as the metadata.
You can quit a window to go back to the previous window and you can keep quiting to exit Noml.
Though that can be annoying so you can quit Noml itself from any window.
The Windows Manager can be accesed by typing "w" and will show you all of your windows and metadata associated with them.

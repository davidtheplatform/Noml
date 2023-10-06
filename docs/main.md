# Noml Documentation

Welcome to Noml's documentation! This will cover what you can do with Noml. By default you will be brought to a home screen where you can type commands.

## Commmands

These commands are usable from every mode.

- `q` (quit): Quit the current window.
- `qn` (quitnoml): Quit Noml.
- `o <path>` (open): Open the file at the provided path.
- `n <path?>` (new): Create a file at the provided path. If no path is provided, create a file in the current directory with the name "untitled".

## Editor

The editor interface will first show the filename then the content of the file. The cursor is yellow and can be moved.

If the cursor is on a space, it will show as `_`. If the cursor is on a tab, it will show as `____`.

Below that is the commands interface, here editor-specific commands can also be done.

### Commands

- `j <path>` (open): Open the file at the provided path.
- `m <amount>` (move): Move the cursor the specified amount of characters horizontally. Negative numbers will move backwards.
- `mw <amount>` (moveword): Move the cursor the specified amount of words horizontally.
- `ml <amount>` (moveline): Move the cursor the specified amount of lines vertically.
- `r <char>` (replace): Replace the character under the cursor with the specified character.
- `rw <word>` (replaceword): Replace the current word with the specified word.
- `rl <line>` (replaceline): Replace the current line with the specified line.
- `f <text>` (find): Find the first occurence of the provided text in the current line.
- `s` (save): Save the current file.
- `ln` (linenumbers): Toggle line numbers.

## Visual Editor

The visual editor can be entered by using the `v` command in the editor, the visual editor is a visual interface for people who don't want to use commands.

You can use arrow keys to move the cursor.

You can type characters like in any other text editor and you can use backslash to erase characters.

Pressing enter will create a new line, if you were in the middle of the previous line the content from the middle to the end will be moved to the new line.

### Commands

- `` ` ``: Exit the visual editor. The `` ` `` was picked because it is the least used character on the QWERTY keyboard.

## Filestructure

The filestructure can be entered using the `fs` command, the filestructure will allow you to move around your filesystem and open files.

If you run with a file opened, your current file will be shown.

### Commands

- `a`: Toggle absolute paths.
- `j`: Jump to files by typing in your target.
- `o`: Open your current file.
- `q`: Exit.

## Windows

The Windows Manager can be accessed by typing `w` and will show you all of your windows and metadata associated with them.

In Noml, when you open a new mode, such as main, editor or filestructure you are creating a new window.

Each window has an associated mode and metadata about it - (i.e. the metadata for the editor would be the path and the buffer).

You can quit a window to go back to the previous window and you can keep quiting to exit Noml. However, you can also quit Noml itself from any window, as doing this for every window can be annoying.

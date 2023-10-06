# NOML - Simple Text Editor Documentation

NOML is a simple text editor designed for users who prefer minimalism and maximum customization in their text editing experience. It comes with no advanced features or configurations, allowing users to focus on their personal preferences. This markdown documentation provides an overview of NOML's functionality and usage.

## Table of Contents
- [Getting Started](#getting-started)
- [Windows Management](#windows-management)
- [File Operations](#file-operations)
- [Text Editing](#text-editing)
- [Installation](#installation)

## Getting Started

To start using NOML, run the script containing the provided code. The editor operates in a text-based terminal environment, providing a straightforward interface for editing and managing files.

## Windows Management

NOML features a simple window management system that allows you to switch between different functionalities within the editor.

### `windows()`
- Access: Press "w" while in the main menu.
- Description: Displays a list of open windows, allowing you to switch between them.
- Usage: 
  - Press "q" to exit the window manager and return to the main menu.

## File Operations

NOML enables you to perform basic file-related operations, including opening and creating files, as well as exploring the file structure.

### Opening a File
- Command: `o <file_path>`
- Description: Opens an existing file for editing.
- Usage: 
  - Replace `<file_path>` with the path to the file you want to open.
  - If the file exists, it will be loaded into the editor.

### Creating a New File
- Command: `n [file_name]`
- Description: Creates a new file with the specified name (or "untitled" if no name is provided).
- Usage: 
  - Optionally, provide a `file_name` to create a file with a custom name.
  - A blank file will be created for editing.

### File Structure Exploration
- Command: `fs`
- Description: Opens a file structure explorer to navigate and view directory contents.
- Usage: 
  - Use the arrow keys to navigate directories.
  - Press "o" to open a file for editing within the file structure explorer.

## Text Editing

NOML provides a minimalistic text editing environment for making changes to files.

### Key Commands
- Command: Various key commands for text editing are available while in the editor. Some key commands include:
  - `q` or `quit`: Exit the editor and return to the main menu.
  - `m [num]` or `move [num]`: Move the cursor horizontally by the specified number of characters.
  - `mw [num]` or `moveword [num]`: Move the cursor to the left or right by the specified number of words.
  - `ml [num]` or `moveline [num]`: Move the cursor vertically by the specified number of lines.
  - `r [char]` or `replace [char]`: Replace the character at the cursor position with the specified character.
  - `rw [word]` or `replaceword [word]`: Replace the word at the cursor position with the specified word.
  - `rl [line]` or `replaceline [line]`: Replace the entire line at the cursor position with the specified line.
  - `f [char]` or `find [char]`: Search for the specified character within the current line.
  - `o [file]` or `open [file]`: Open another file for editing within the editor.
  - `s` or `save`: Save changes made to the current file.
  - `ln` or `linenumbers`: Toggle line numbers display on/off.
  - `v` or `visualeditor`: Toggle the visual editor mode.
  - `fs` or `filestructure`: Open the file structure explorer from within the editor.

### Visual Editor Mode
- Description: Allows for cursor movement and text editing using arrow keys and other simple keystrokes.
- Usage: 
  - Enter the visual editor mode by pressing the backtick key (\`) while in the editor.
  - Use arrow keys to navigate and edit text.
  - Press Enter to create a new line.
  - Press Backspace to delete characters.
  - Press the backtick key (\`) again to exit visual editor mode.

Please note that NOML is designed to be a minimalistic text editor, and its functionality is limited to basic text editing and file operations. Enjoy the simplicity and customize it to suit your preferences.

## Installation

To clone the GitHub repository for `Noml_Plus` by `UniqueName12345`, add it to the `PYTHONPATH`, and create an alias, follow these steps for both Windows and Linux. Before you begin, make sure you have Git installed on your system.

**DO NOT USE INSTALLER.BAT OR INSTALLER.SH**

### Cloning the GitHub Repository:

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to clone the `Noml_Plus` repository. You can use the `cd` command to change directories. For example, to clone it in your home directory, you can use:

   ```shell
   cd ~  # On Linux
   cd %USERPROFILE%  # On Windows
   ```

3. Clone the GitHub repository using the following command:

   ```shell
   git clone https://github.com/UniqueName12345/Noml_Plus.git
   ```

   This command will create a directory named `Noml_Plus` containing the repository's files.

### Adding to PYTHONPATH (Linux):

1. Open your terminal.

2. Edit your shell profile file. Depending on your shell (e.g., Bash, Zsh), you'll need to edit a specific file like `~/.bashrc`, `~/.zshrc`, or `~/.profile`. Use a text editor like `nano`, `vim`, or `gedit`. For example:

   ```shell
   nano ~/.bashrc
   ```

3. Add the following line to the end of the file, replacing `/path/to/Noml_Plus` with the actual path to your `Noml_Plus` directory:

   ```shell
   export PYTHONPATH=$PYTHONPATH:/path/to/Noml_Plus
   ```

4. Save the file and exit the text editor.

5. To apply the changes immediately, run:

   ```shell
   source ~/.bashrc
   ```

### Adding to PYTHONPATH (Windows):

1. Open the Start Menu and search for "Environment Variables" and select "Edit the system environment variables."

2. In the System Properties window, click the "Environment Variables" button.

3. Under "User variables" or "System variables" (depending on whether you want to set the PYTHONPATH for your user or the entire system), locate the "Path" variable and click "Edit."

4. In the "Edit Environment Variable" window, click "New," and add the path to the `Noml_Plus` directory. For example, if `Noml_Plus` is in your user's Documents folder, you would add something like:

   ```
   C:\Users\<YourUsername>\Documents\Noml_Plus
   ```

5. Click "OK" to save the changes.

### Creating an Alias (Linux):

1. Open your terminal.

2. Edit your shell profile file (`~/.bashrc`, `~/.zshrc`, or `~/.profile`) again:

   ```shell
   nano ~/.bashrc
   ```

3. Add an alias to the end of the file. For example, to create an alias named `nomlplus`:

   ```shell
   alias nomlplus="python3 /path/to/Noml_Plus/noml_plus.py"
   ```

   Replace `/path/to/Noml_Plus` with the actual path to your `Noml_Plus` directory.

4. Save the file and exit the text editor.

5. To apply the changes immediately, run:

   ```shell
   source ~/.bashrc
   ```

Now, you should be able to use the `nomlplus` alias to run the `noml_plus.py` script from anywhere in your terminal.

### Creating a Shortcut (Windows):

1. Locate the `noml_plus.py` script inside the `Noml_Plus` directory.

2. Right-click on the `noml_plus.py` file and select "Create shortcut."

3. Drag the newly created shortcut to your desktop or a convenient location.

4. To run the script, simply double-click on the shortcut.

You now have a shortcut to execute `noml_plus.py` on Windows.

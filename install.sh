#!/bin/bash

# Function to clone the Noml GitHub repository
install_noml() {
    echo "Cloning Noml from GitHub..."
    git clone https://github.com/GenericProgrammer1234/Noml "$1" > /dev/null 2>&1
    echo "Noml installed successfully!"
}

# Function to add the Noml path to PYTHONPATH
add_to_pythonpath() {
    echo "Adding Noml path to PYTHONPATH..."
    export PYTHONPATH=\$PYTHONPATH:$1
    echo "export PYTHONPATH=\$PYTHONPATH:$1" >> "$HOME/.bashrc"
    [ -f "$HOME/.zshrc" ] && echo "export PYTHONPATH=\$PYTHONPATH:$1" >> "$HOME/.zshrc"
    echo "PYTHONPATH updated successfully!"
}

# Function to alias "noml" to the app.py file
alias_noml() {
    echo "Alias 'noml' to the Noml app.py file..."
    alias noml='python3 $1/app.py'
    echo "alias noml='python3 $1/app.py'" >> "$HOME/.bashrc"
    [ -f "$HOME/.zshrc" ] && echo "alias noml='python3 $1/app.py'" >> "$HOME/.zshrc"
    echo "Alias 'noml' added successfully!"
}

# Main installation process
echo "Welcome to the Noml installer!"

# Ask for installation directory
read -p "Enter the installation directory for Noml: " install_dir

# Create the installation directory if it doesn't exist
mkdir -p "$install_dir"

# Install Noml
install_noml "$install_dir"

# Add Noml path to PYTHONPATH
add_to_pythonpath "$install_dir/Noml"

# Alias "noml" to app.py
alias_noml "$install_dir/Noml"

echo "Installation has finished!"
echo "You can now run 'noml' to start the text editor."
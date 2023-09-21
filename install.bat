@echo off
setlocal enabledelayedexpansion

rem Function to clone the Noml GitHub repository
:install_noml
echo Cloning Noml from GitHub...
git clone https://github.com/GenericProgrammer1234/Noml "%1" >nul 2>&1
echo Noml installed successfully!
goto :EOF

rem Function to add the Noml path to PYTHONPATH
:add_to_pythonpath
echo Adding Noml path to PYTHONPATH...
echo setx PYTHONPATH "%%PYTHONPATH%%;%1" >temp.bat
call temp.bat >nul 2>&1
del temp.bat
echo PYTHONPATH updated successfully!
goto :EOF

rem Function to alias "noml" to the app.py file
:alias_noml
echo Alias 'noml' to the Noml app.py file...
echo doskey noml=python "%1\app.py" $* >> "%USERPROFILE%\Documents\noml_alias.bat"
echo Alias 'noml' added successfully!
goto :EOF

echo Welcome to the Noml installer!

rem Ask for installation directory
set /p "install_dir=Enter the installation directory for Noml: "

rem Create the installation directory if it doesn't exist
mkdir "%install_dir%" 2>nul

rem Install Noml
call :install_noml "%install_dir%\Noml"

rem Add Noml path to PYTHONPATH
call :add_to_pythonpath "%install_dir%\Noml"

rem Alias "noml" to app.py
call :alias_noml "%install_dir%\Noml"

echo Installation has finished!
echo You can now run 'noml' to start the text editor.
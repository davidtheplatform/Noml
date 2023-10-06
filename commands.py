from os import name, system


def tput(arg):
    """
    Pass something to tput.

    Args:
        arg (string): The argument to be passed to tput.

    Returns:
        None
    """

    if name != "nt":
        system(f"tput {arg}")


def echo(to_echo):
    """
    Echo something out.

    Args:
        to_echo (string): What should be echoed.
    """

    if name == "nt":
        system(f"echo \033]0;{to_echo}\007")
    else:
        system(f'echo -n -e "\033]0;{to_echo}\007"')


def clear():
    """
    Clear the screen.
    """

    if name == "nt":
        system("cls")
    else:
        system("clear")

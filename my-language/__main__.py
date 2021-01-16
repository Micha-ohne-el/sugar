import sys

from typing import Optional

from commands import commands, command
from error import error
from quality_of_life import *


def handle_commandline(*args: str):
    if len(args) == 0:
        args = ("help",)

    output = None

    if args[0] in commands:
        command = commands[args[0]]
        try:
            output = command["function"](*args[1:])
        except Warning:
            pass
        except TypeError:
            error(f"Command '{args[0]}' recieved invalid arguments: {args[1:]}")
            print(usage(args[0]), end="")
            return
        except Exception as e:
            error(f"Command '{args[0]}' raised an unexpected error:")
            raise e
        finally:
            if type(output) is str:
                print(output, end="")
    else:
        error(f"Could not find command '{args[0]}'.")


@command
def usage(cmd: str = "") -> Optional[str]:
    """
    Returns dynamically generated usage information on any given command.
    For generation, the function signature of the command is used.
    Required parameters are wrapped in <angle brackets>.
    Optional parameters are wrapped in [square brackets].
    If command is omitted, the usage for the program as a whole is returned.
    """
    if cmd == "":
        usage = f"Usage: {sys.argv[0]} [command] [arguments...]\n"
        return usage
    if not cmd in commands:
        return error(f"Could not find command '{cmd}'.")

    usage = f"Usage: {sys.argv[0]} {cmd}"

    for param in commands[cmd]["parameters"]:
        if param["required"]:
            usage += f" <{param['name']}>"
        else:
            usage += f" [{param['name']}]"
    return usage + "\n"

@command
def help(topic: str = "general") -> Optional[str]:
    """
    Returns the appropriate help message for the given topic or command.
    If topic is a command, its usage is returned as well.
    Help messages should match the glob ./help/*.txt, where * is the topic.
    Help message files should always include a newline at their end.
    If topic is omitted, the default file used is ./help/general.txt.
    """

    output = ""
    if topic in commands: # If topic is a command, print its usage too
        output += usage(topic) + "\n"
    path = ROOT / "help" / (topic + ".txt")
    if path.exists():
        with open(path) as f:
            output += f.read()
    if output == "":
        return error(f"Could not find usage or help for '{topic}'.")
    return output.strip("\n") + "\n" # Ensure one newline at the end.


if __name__ == "__main__":
    handle_commandline(*sys.argv[1:])

import inspect


commands = {}

def command(function):
    """
    Decorator to automatically turn a method into a command.
    """
    commands[function.__name__] = {
        "function": function,
        "parameters": tuple(
            {"name": p.name, "required": p.default is inspect.Parameter.empty}
            for p in inspect.signature(function).parameters.values()
        )
    }
    return function

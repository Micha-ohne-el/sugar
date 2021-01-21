import sys
def error(*values, sep=" ", end="\n", flush=False):
    """
    Prints all values to stderr instead of stdout.
    """
    print(*values, sep=sep, end=end, flush=flush, file=sys.stderr)

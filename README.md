# Sugar
A sweet little programming language.

## Introduction
I got bitten by the language bug over a year ago,
and ever since I've had these ideas floating around in my head.
This project is the manifestation of these ideas,
put together into a language that is hopefully nice to use
and that hopefully brings some neat ideas to the table.

## Running the program
* Navigate to the project root (`cd ~/Documents/sugar` for example).
* Run `pip install -r requirements.txt` to install all dependencies in one go.
* Run `python sugar [args...]`.  
  See the docs for a proper explanation on the commandline arguments.

I'm developing this on Linux, but since it's written in Python,
it should work just as well on Windows and MacOS.
If not, open an Issue or text me or whatever and I'll take care of it,
there is no reason this can't be cross-platform.

## Contributing
Right now this project is in its babyshoes,
so I doubt that I would accept any big PRs.
That being said, any ideas and minor contributions are very much appreciated!

You can just submit an Issue or a Pull Request on GitHub if you want to do that,
I'll reply as soon as possible!

## Project structure
Many subdirectories have their own `README.md` files that better explains them.

* `sugar/` – Project root.
  * `docs/` – HTML documentation for use on GitHub Pages.
    This is in contrast with `sugar/help/` which contains shorter plain-text
    help messages that appear on the commandline.
  * `examples/` – Example projects that showcase the syntax.
  * `ideas/` – Some rough drafts for ideas I have in my head.
    This is mainly just so I don't forget them,
    they are not at all guaranteed to get implemented.
  * `sugar/` – Root of the _program_ `sugar` (compiler, help texts, etc.).
    This is where the real programming happens.
    * `grammars/` – Grammar definitions for the entire language.
      This is what controls the syntax of Sugar.
      * `*.jsonc` – Left over files from when I was using JSON to define this.
        The code is still implemented but will probably removed soon,
        along with these files.
    * `help/` – Help texts that are built into the program (`sugar help`).
      This is in contrast to `../docs/` which contains HTML documentation.
      The docs are more thorough but not included in the program.
      * `general.txt` – The help file used when no topic is given
        (`sugar help` instead of `sugar help compile` for example).
      * `*.txt` – All other help files.
        These are dynamically read by the `help` command.
  * `tests/` – For the time being these are source files to test the parser.
    Eventually this will house proper unit tests.
  * `REMARKS.md` – Reasoning for certain design decisions,
    more thorough comments that would ruin the flow of source code,
    or other comments on things.
  * `requirements.txt` – Requirements file for PIP:
    `pip install -r requirements.txt`.
    These will not be required when this program gets released,
    they are just required for building and developing Sugar.


## :)
If you are the creator of _Sugar_
(the other programming language with this same name that may or may not exist)
and you are not okay with me calling this project that,
please get in touch with me. Thanks.

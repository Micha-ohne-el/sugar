# Sugar
A programming language. I haven't decided on more details yet...

## Project structure
Unimportant things are omitted (such as `.vscode/`).
* `sugar/` – Project root.
  * `docs/` – HTML documentation for use on GitHub Pages.
    This is in contrast with `sugar/help/` which contains shorter plain-text
    help messages that appear on the commandline.
  * `examples/` – Example projects that showcase the syntax.
  * `ideas/` – Some rough drafts for ideas I have in my head.
    This is mainly just so I don't forget them,
    they are not at all guaranteed to get implemented.
  * `sugar/` – Root of the _program_ `sugar` (compiler, help texts, etc.).
    * `grammars/` – Grammar definitions for the entire language.
      This is what controls the syntax of Sugar.
    * `help/` – Help texts that are built into the program (`sugar help`).
      This is in contrast to `../docs/` which contains HTML docs.
      The docs are more thorough but not included in the program.
  * `tests/` – For the time being these are source files to test the parser.
    Eventually this will house proper unit tests.
  * `REMARKS.md` – Reasoning for certain design decisions,
    more thorough comments that would ruin the flow of source code,
    or other comments on things.
  * `requirements.txt` – Requirements file for PIP:
    `pip install -r requirements.txt`.
    These will not be required when this program gets released,
    they are just required for building and developing Sugar.

## Running the program
* Navigate to the project root (`cd ~/Documents/sugar` for example).
* Run `python sugar [args...]`.  
  See the docs for a proper explanation on the commandline arguments.

## Contributing
Right now this project is in its babyshoes,
so doubt that I would accept any big PRs.
That being said, any ideas and contributions are very much appreciated!

You can just submit an Issue or a Pull Request on GitHub if you want to do that.


## :)
If you are the creator of _Sugar_
(the other programming language with this same name that may or may not exist)
and you are not okay with me calling this project that,
please get in touch with me. Thanks.

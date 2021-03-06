import json
import yaml
from typing import Iterable
from pathlib import Path

from quality_of_life import *

def load_grammars_json(files: Iterable = None) -> dict:
    if not files:
        p = ROOT / "grammars"
        files = (open(f) for f in p.rglob("*.json?"))

    syntaxes = {Path(f.name).stem: json.load(f) for f in files}

    return syntaxes

def load_grammars_yaml(files: Iterable = None) -> dict:
    if not files:
        p = ROOT / "grammars"
        files = (open(f) for f in p.rglob("*.yaml"))

    syntaxes = {Path(f.name).stem: yaml.full_load(f) for f in files}

    return syntaxes

load_grammars = load_grammars_yaml

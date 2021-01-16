import re
from typing import Any

class Parser:
    def __init__(self, *, operators, types):
        self.operators = operators
        self.types = types

        self._flattened_types = []

        print(repr(operators))
        print(repr(types))

    def parse(self, source: str):
        self.source = source

        self.index = 0 # index into self.source

        for group in self.operators:
            for sentence in group:
                id = re.sub(r"\s+", "_", sentence["name"].lower()).strip("_")
                for element in sentence["syntax"]:
                    for condition in element:
                        if condition[0] == "word":
                            print(id, self._peekAny(condition[1]))

    def _consume_syntax(self, syntax) -> bool:
        for element in syntax:
            for condition in element:
                if condition[0] == "word":
                    if self._peekAny(condition[1]):
                        self.index += len(condition[1])
                    else:
                        return False
        return True

    def _peekAny(self, *matches: str) -> bool:
        for match in matches:
            if self.source[self.index:self.index+len(match)] == match:
                return True
        return False

    def _peek(self, length: int) -> str:
        return self.source[self.index:self.index+length]

    def _existing_type_name(self, name: Any) -> bool:
        if not self._flattened_types:
            self._flattened_types = self._flatten_types(self.types)
        return name in (type["name"] for type in self._flattened_types)

    def _existing_type_id(self, id: Any) -> bool:
        if not self._flattened_types:
            self._flattened_types = self._flatten_types(self.types)
        return id in (type["id"] for type in self._flattened_types)







    @classmethod
    def _valid_syntax(cls, syntax: Any) -> bool:
        if syntax is not list:
            return False

        for element in syntax:
            if element is not list:
                return False

            for condition in element:
                return cls._valid_condition(condition)

        return False # syntax or element have len=0.

    @classmethod
    def _valid_condition(cls, condition: Any) -> bool:
        if condition is not list:
            return False
        if len(condition) < 1:
            return False
        if condition[0] == "word":
            if len(condition) != 2:
                return False
        elif condition[0] == "type":
            if len(condition) != 2:
                return False
            if not cls._valid_type_id(condition[1]):
                return False
        else:
            return False

        return True

    @classmethod
    def _valid_type_id(cls, id: Any) -> bool:
        return type(id) is str and len(id) == 3

    @classmethod
    def _flatten_types(cls, types: list) -> list[dict[str, str]]:
        result = []
        for type in types:
            result.append({"id": type["id"], "name": type["name"]})
            if "subtypes" in type:
                result.extend(cls._flatten_types(type["subtypes"]))
        return result

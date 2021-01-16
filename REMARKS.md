# Remarks

## TypeScript representation of grammar types
Python typing sucks, so here are the type definitions for the parser
written in TypeScript.
In the Python source files these are left untyped as of now,
because I had too much trouble trying to poperly type them.
### Operators
```typescript
type OperatorsGrammar = Group[];
type Group = Sentence[];
type Sentence = {
  /* id: string, */ // id is inferred from name.
  name: string,
  syntax: Syntax
};
type Syntax = Element[];
type Element = Condition[];
type Condition = {
  type?: str,
  word?: str
}
```
### Types
```typescript
type TypesGrammar = Type[];
type Type = {
  id: string,
  name: string,
  subtypes?: Type[]
};
```

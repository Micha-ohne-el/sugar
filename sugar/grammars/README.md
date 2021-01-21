# `sugar/sugar/grammars/`
This directory contains grammar definitions,
which are the files that control the syntax of Sugar.

The `*.jsonc` files in here are likely to be removed in the future
and should thus be ignored.

## Operators
#### `operators.yaml`
Operators are the built-in way of handling data.
They come in two varieties: _normal_ and _meta_ operators.

_Normal operators_ only know about values, never about anything else.
They never have side-effects.  
For example, Addition is a normal operator,
it does not matter whether either of its operands is literal, constant, etc.  
`1 + 1` and `x + y` are  not just equivalent but _identical_ when `x == y == 1`.

_Meta operators_ can, however, have side-effects,
and they can access more about their operands than just the value.  
For example, Assignment is a meta operator,
it checks to see that its first operand can be assigned to
and has the side-effect of actually assigning a value to a name.  
`x := y` and `1 := 1` are very different (the latter being invalid),
but a normal operator would see no difference.

### A TypeScript representation of the syntax of `operators.yaml`
```typescript
type OperatorsGrammar = Group[];
type Group = Operator[];
interface Operator {
  /* id: string; */   // id is inferred from name.
  name: string;       // Operator name, such as "Addition".
  syntax: NormalElement[] | MetaElement[];
}
interface NormalElement {
  type?: string;      // type of value, such as "str" or "int".
  word?: string;      // some literal text, such as "+" or "delete".
  min?: number;       // minimum amount this element must appear; default = 1.
  max?: number;       // maximum amount this element can appear; default = 1.
}
interface MetaElement extends NormalElement {
  literal?: boolean;  // whether the operand is literal.
  constant?: boolean; // whether the operand is constant.
  declared?: boolean; // whether the operand is an already declared name.
}
```

## Types
#### `types.yaml`
Types are the way to insure values and names are compatible with one another.
They follow a strict hierarchy layed out in this file.

Type IDs are always three lowercase letters,
which are equal to the first three letters of the type's full name,
except where ambiguous (Compound `com` and Command `com` for example.)

### A TypeScript representation of the syntax of `types.yaml`
```typescript
type TypesGrammar = Type[];
interface Type {
  id: string;         // Three-letter name used in Sugar code.
  name: string;       // Full name.
  subtypes?: Type[];
}
```

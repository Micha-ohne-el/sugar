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

## Types
#### `types.yaml`
Types are the way to insure values and names are compatible with one another.
They follow a strict hierarchy layed out in this file.

Type IDs are always three lowercase letters,
which are equal to the first three letters of the type's full name,
except where ambiguous (Compound `com` and Command `com` for example.)

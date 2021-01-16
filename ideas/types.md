## Type Hierarchy
- `any`: Anything
  - `sta`: Status (like boolean but with infinite values, not just two)
    - `pos`: Positive
    - `neg`: Negative
    - `neu`: Neutral
  - `num`: Number
    - `int`: Integer
    - `rat`: Rational (two integers that form a ratio)
  - `str`: String
    - `ast`: ASCII String (ASCII; 1 byte/character)
    - `wst`: Wide String (UTF-32; 4 bytes/character)
    - `ust`: Unicode String (UTF-8; 1 to 4 bytes/character)
  - `cpd`: Compound (types that are made up of fields)  
    (not sure on these at all yet)
    - `arr`: Array
    - `pol`: Pool
    - `col`: Collection
    - `tab`: Table
    - `vec`: Vector
    - `seq`: Sequence
    - `rec`: Record
  - `cod`: Code
    - `fun`: Function (no side-effects)
    - `cmd`: Command (side-effects)
- `not`: Nothing (Null)

## Compounds
| Type  | Accessible | Iterable | Ordered | Key unique | Key type | Val unique | Val type |
| ----- | ---------- | -------- | ------- | ---------- | -------- | ---------- | -------- |
| `arr` | Yes        | Yes      | Yes     | Yes        | `int`    | No         | `any`    |
| `pol` | No         | No       | —       | —          | —        | Yes        | `any`    |
| `col` | Yes        | Yes      | Yes     | Yes        | `int`    | Yes        | `any`    |
| `tab` | Yes        | Yes      | Yes     | Yes        | `any`    | No         | `any`    |
| `vec` | Yes        | No?      | Yes     | Yes        | `str`    | No         | `num`    |
| `seq` | No         | Yes      | Yes     | Yes        | `int`    | No         | `any`    |

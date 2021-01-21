So I had two different, incompatible ideas here.

First, a more wordy approach:
```
define name as "James"
define speak as [str sentence] => {
  ...
}
```
This approach looks like one for a functional language for some reason.

I'm not using `def` since all type IDs are three letters and I want to reserve that status for those.

The other idea I had was this:
```
name := "James"
speak := [str sentence] => {
  ...
}
```
This is much shorter and even more flexible:
```
`This is a variable-value assignment`
a := 123

`This is a constant-value assignment`
b ::= 123
b := 456 `invalid, already assigned`
b ::= 456 `invalid, already assigned`

`This is a variable-reference assignment`
x := 123
c :== x `123`
x := 456
c == 456 `true`
c := 123 `valid`

`This is a constant-reference assignment`
y := 123
d ::== y `123`
y := 456
d == 456 `true`
d := 123 `invalid, already assigned`
d ::== 123 `invalid, already assigned`
```
(Note that the way comments are handled here is not final)

I like this way of handling constants and references very much,
so this is what I defined in the grammars as of now.

.EQ
delim $$
.EN
.TL
Lecture 7
.SH
Operations on functions 2
.LP
* Restriction:
$f: A -> B$ and  $C \[sb] A$, then 

${f | sub C}$ is the function

${f | sub C}:  C -> B;~x -> f(x)$

* Composition:
$f: A -> B~~and~~g: B -> C$

$g \[u00B0] f: A -> C;~x -> g(f(x))$

* Quotient of two functions

$f: D -> R~~and~~g: D -> R\[rs] \[lC] 0 \[rC]$

${f over g}: D -> R;~x -> {f(x) over g(x)}$

.UL "Remark:"
.LP
$f \[u00B0] g != g \[u00B0]~~in~general$

.UL "Examples"
.LP
$h: R\[rs] \[lC] 0 \[rC] -> R\[rs] \[lC] 0 \[rC];~ x -> {1 over x}$

let $D = \[lC] x \[mo] R~|~x > 0 \[rC]$

$h | sub D$ has a graph which is part of that of $f$

$f: R -> R;~ x -> sin(x)~~and~~g: R -> R;~ x -> {x sup 2} + 1$

${f over g}(x) = {f(x) over g(x)} = {sin(x) over {{x sup 2} + 1}}$

We can also write $f.(h \[u00B0] )~~for~~f over g$

.EQ
(f.(h\[u00B0] g))(x) = f(x).(h\[u00B0] g)(x)
.EN
.EQ
= f(x).h(g(x))
.EN
.EQ
= f(x).{1 over g(x)} = {f(x) over g(x)}
.EN
.EQ
so~f.(h\[u00B0]g)={f over g}~~if~0~is~not~in~the~range~of~g
.EN

.SH
Intervals
.LP
These are subsets $I \[sb] R$ such that:

if $a\[mo]I, b\[mo]I, c \[mo]R$ between  $a$ and $b$

then $c \[mo]I$.

.UL "Examples"
.LP
* $\[lC] x \[mo] R~|~x > 0~~and~~x < 2 \[rC]$

* $\[lC] x \[mo] R~|~x >= -1~~and~~x <= 1 \[rC]$

* $\[lC] x \[mo] R~|~x > 0 \[rC]$

* $\[lC] x \[mo] {x sup 2} > 1 \[rC]~~not~an~interval$

.LP
Above can be expressed as the union of the 2 intervals 

$x < -1$ and $x > 1$

For $a \[mo] R$ and $b \[mo] R$ and $a < b$:
.EQ
(a, b) = \[lC]x \[mo] R~|~x > a~~and~~x < b\[rC]~~open~interval
.EN

.EQ
[a, b] = \[lC]x \[mo] R~|~x >= a~~and~~x <= b\[rC]~~closed~interval
.EN

.EQ
[a, b) = \[lC]x \[mo] R~|~x >= a~~and~~x < b\[rC]~~half~open
.EN

.EQ
(a, b] = \[lC]x \[mo] R~|~x > a~~and~~x <= b\[rC]~~half~open
.EN

When $a = b:~~[a, a] = \[lC] a \[rC]~~contains~a~single~point.$

.EQ
(-\[if], a) = \[lC]x \[mo] R~|~x < a\[rC]
.EN

.EQ
(-\[if], a] = \[lC]x \[mo] R~|~x <= a\[rC]
.EN

.EQ
(a, \[if]) = \[lC]x \[mo] R~|~x > a\[rC]
.EN

.EQ
[a, \[if]) = \[lC]x \[mo] R~|~x >= a\[rC]
.EN

.EQ
[-\[if], \[if]) = R
.EN

.UL "Remark:"
.LP
$\[if]~~and~~-\[if]$ are not real numbers so they are 
.UL "never"
included in any interval (or any other subset of $R$).

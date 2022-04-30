.EQ
delim $$
.EN
.TL
Lecture 6
.NH
Interpolating polynomials
.LP
Sometimes we want to find a function that takes some
prescribed values at certain given points. Polynomials help us
to find such a function, which has no sharp corners.
.SH
Theorem
.LP
For $n \[mo] N$, let ${x sub 1}$, ${x sub 2}$, ... , ${x sub
n}$ be distinct real numbers and ${y sub 1}$, ... , ${y sub
n}$ any real numbers.
.LP
.LP
Then there is a unique polynomial $p(n)$ of degree $<= n - 1$
such that $p({x sub i}) = {y sub i}$ for all $i \[mo]
\[lC]1$, ... , $ n\[rC]$
.LP
.LP
.BI Remark:
If the ${x sub i}$'s are not distinct, e.g. ${x sub 1} = {x
sub 2}$, then there may not be any function with $f({x sub
1}) = {y sub 1}$ and $f({x sub 2}) = {y sub 2}$, because we
may have ${y sub 1} != {y sub 2}$. (if. "vertical line test")
.LP
.LP
.SH
.UL "Examples"
.LP
$n = 1$: Given ${x sub 1} \[mo] R$ and ${y sub 1} \[mo] R$ we
can find a contrast function $p(x)$ with $p({x sub 1}) = {y
sub 1}$,

.QS
namely $p(x) = {y sub 1}$ for all $x \[mo] R$
.QE

$n = 2$: Given ${x sub 1}$, ${x sub 2}$, ${y sub 1}$, ${y sub 2} \[mo] R$ with ${x sub 1} != {x sub 2}$ we can find a linear function $p(x)$ with $p({x sub 1}) = {y sub 1}$ and $p({x sub 2}) = {y sub 2}$, Writing
.EQ
p(x) = m.x + b
.EN
.PP
we find
.ce
$m = {{y sub 2} - {y sub 1}} over {{x sub 2} - {x sub 1}}$ and $ b = {{y sub 1}.{x sub 2} - {y sub 2}.{x sub 1}} over {{x sub 2} - {x sub 1}}$
.ce

.LP
$n = 2,$

$\[parenlefttp]{y sub 2} = 0$: The formula simplifies to 
.br
$\[parenleftbt]{y sub 1} = 1$
.ce
$p(x) = {x - {x sub 2}} over {{x sub 1} - {x sub 2}}$
.ce

.PP
with $p({x sub 1}) = 1$ and $p({x sub 2})$


.LP
$n >= 2$: ${y sub 1} = 1$, ${y sub 2} = {y sub 3} = ... = {y sub n} = 0:$ Taking products of the previous case we can take 

.EQ
p(x) = {x - {x sub 2}} over {{x sub 1} - {x sub 2}}\[u00B7]{x - {x sub 3}} over {{x sub 1} - {x sub 3}} ... {x - {x sub n}} over {{x sub 1} - {x sub n}}
.EN

Here each factor is a linear function. There are $n - 1$
factors, so $p(x)$ has degree $= n - 1$.
.br
each factor has value $1$ at $x sub 1$, so $p({x sub 1}) = 1$,
.br
For $x sub i$ with $i >= 2$ there is a factor with value $0$, so $p({x sub i}) = 0$ if $i >= 2$.


The polynomial in the last example is called a Lagrange basis
polynomial.
.br
Given $n$ distinct numbers $x sub 1$, ... , $x
sub n$ 
.br
there are $n$ such Lagrange basis polynomials, which
vanish at all $x sub i$'s except for one, where their value
is $1$.


.SH
Proof of theorem on interpolating polynomials:
.LP

.B Uniqueness:
Suppose that $p(x)$ and $q(x)$ are polynomials of degree $<= n - 1$ with
.br
$p({x sub i}) = y sub i$ and $q({x sub i}) = y sub i$ for all
$i \[mo] \[lC]1, ... , n\[rC]$. Then $p - q$ is a polynomial
of degree $<= n - 1$ with $(p - q)(x sub {i}) = p(x sub{i}) -
q({x sub i}) = 0$ for all $i \[mo] \[lC]1, ... , n\[rC]$ so
$p - q$ has $n$ roots. This can only happen when $(p - q)(x)
= 0$ for all $x \[mo] R$, i.e. $p(x) = q(x)$, so $p$ and $q$
are the same function.


.B Existence:
First consider the Lagrange basis polynomials ${p sub 1}(x)$, ..., ${p sub n}(x)$ with
.EQ
{p sub 1}(x) = {x - {x sub 2}} over {{x sub 1} - {x sub 2}}\[u00B7]{x - {x sub 3}} over {{x sub 1} - {x sub 3}} ... {x - {x sub n}} over {{x sub 1} - {x sub n}} ~~~~~~~ {p sub 1}({x sub 1}) = 1,~p({x sub 2})= ... =~ p({x sub n}) = 0
.EN
.EQ
{p sub 2}(x) = {x - {x sub 1}} over {{x sub 2} - {x sub 1}}\[u00B7]{x - {x sub 3}} over {{x sub 2} - {x sub 3}} ... {x - {x sub n}} over {{x sub 2} - {x sub n}} ~~~~~~~ {p sub 2}({x sub 2}) = 1,~p({x sub 1})= p({x sub 3}) = ... = p({x sub n}) = 0
.EN
.EQ
{p sub n}(x) = {x - {x sub 1}} over {{x sub n} - {x sub 1}}\[u00B7]{x - {x sub 2}} over {{x sub n} - {x sub 2}} ... {x - {x sub {n - 1}}} over {{x sub n} - {x sub {n - 1}}} ~~~~~~~ {p sub n}({x sub n}) = 1,~p({x sub 1}) = ... = p(x sub {n - 1}) = 0
.EN

We can take $p(x) = {y sub 1}.{p sub 1}(x)~+~{y sub 2}.{p sub 2}(x)~+ ... +~{y sub n}.{p sub n}(x)$, which has degree $<= 1$
.br
and $p({x sub i}) = {y sub i}~for~all~i\[mo]\[lC]1,~...,~n\[rC]$.


.SH
.UL Example
.LP
Find the formulas for the unique quadratic polynomial through $(1, -3)$, $(2, 2)$ and $(3, -1)$.

.BI Solution:
We find first find the Langrange basis polynomials for the points $1$, $2$, $3$:
.EQ
{p sub 1}(x) = {{x - 2} over {1 - 2}}.{{x - 3} over {1 - 3}} = {1 over 2}({x sup 2}) - 2{1 over 2}x + 3,
.EN
.EQ
{p sub 2}(x) = {{x - 1} over {2 - 1}}.{{x - 3} over {2 - 3}} = -(x - 1)(x - 3) = -{x sup 2} + 4x - 3,
.EN
.EQ
{p sub 3}(x) = {{x - 1} over {3 - 1}}.{{x - 2} over {3 - 2}} = {1 over 2}(x - 1) = {1 over 2}{x sup 2} - 1{1 over 2}x + 1,
.EN
.LP
We have
.LP
$p(x) = -3.{p sub 1}(x) + 2.{p sub 2}(x) - 1.{p sub 3}(x)$

.QS
$= -3.({1 over 2}{x sup 2} - 2{1 over 2}x + 3) + 2(-{x sup 2} + 4x - 3) - ({1 over 2}{x sup 2} - 1{1 over 2}(x) + 1)$

$= -1{1 over 2}{x sup 2} + 7{1 over 2}x - 9 - 2{x sup 2} + 8x - 6 -{1 over 2}{x sup 2} + 1{1 over 2}x - 1$

$= -4{x sup 2} + 17x - 16$
.QE
.LP
Check
.QS
$p(1) = -4 + 17 - 16 = -3$

$p(2) = -4.4 + 17.2 - 16 = -16 + 34 - 16 = 2$

$p(3) = -4.9 + 17.3 - 16 = -36 + 51 - 16 = -1$
.QE
.LP
($p(x)$ has a maximum at $2{1 over 8}$, where $p(2{1 over 8}) = 2{1 over 16}$ the roots of $p$ are at $2{1 over 8} - {sqrt 33} over {8}$ and  $2{1 over 8} + {sqrt 33} over {8}$)

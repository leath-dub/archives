.TL
Lecture 4
.AU
Ko Sanders
.AI
DCU
.NH
Operations on Functions 1
.EQ
delim $$
.EN
.LP
There are many ways to combine functions into new ones. Here are
three of them:

Let D be any set, $f:D -> R$ and $g:D -> R$ functions with the same
domain $D$ and $c \[mo] R$, We define the functions $f + g$, $f.g$
and $c.f$ as follows:

.PP
The sum  $f + g:D -> R$  is given by  $(f + g)(x) = f(x) + g(x)$,
.PP
The sum  $f.g:D -> R$  is given by  $(f.g)(x) = f(x).g(x)$,
.PP
The sum  $c.g:D -> R$  is given by  $(c.g)(x) = c.g(x)$,

.LP
.BI Remark:
For any $x \[mo] D$, the right-hand side is a sum or
product of real numbers, but $f$ and $g$ are not numbers, so $f +
g$, $f.g$ and $c.f$ are operations on functions that we defined in
terms of their function values at every $x \[mo] D$.

.SH
.UL "Examples"
.PP
For $f(x) = x - 3$ and $g(x) = 2x sup 2 + 1$ ( with domain $R$) and
$c = -1 over 2$:

.PP
$(f + g)(x) = f(x) + g(x) = x - 3 + 2x sup 2 + 1 = 2x sup 2 + x - 2$
.PP
$(f.g)(x) = f(x).g(x) = (x - 3).(2x sup 2 + 1) = 2x sup 3 - 6x sup 2 + x - 3$
.PP
$({-1 over 2}.f)(x) = {-1 over 2}.f(x) = {-1 over 2}.(x - 3) = {-1 over 2}.x + 1.{1 over 2}$

We have seen that all linear functions are determined by their
slope $m$ and intecept $b$. We can now write this as follows.

.SH
.UL Example
.PP
Consider the identity function   $id: R -> R: x -> x$
.PP
and the constant function        $1 sub c: R -> R: x -> 1$
.LP
For any $m \[mo] R$ and $b \[mo] R$:
.PP
$(m.id + b.{1 sub c})(x) = (m.id)(x) + (b.{1 sub c})(x)$
.QS 
.PP 
                  $= m.id(x)   + b.{1 sub c}(x)$
.PP
                  $= m.x       +   b.1 sub c$
.QE
.LP
so the linear function with slope $m$ and intercept $b$ can be
written as:
.EQ
m.id + b.1 sub c
.EN
.LP
(In practice this is rarely the most convenient name for this function.)

For any function $f:D -> R$ we often write $f sup 2$ intead of
$f.f$, $f sup 3$ instead of $f.f.f$, etc.

.NH
Polynomials
.LP
A polynomial is a function $f:R -> R$ whose formula is of the form
.PP
.EQ
f(x) = {a sub n}.{x sup n} + {a sub {n - 1}}.{x sup {n - 1}} +
... +  {a sub 2}.{x sup 2} + {a sub 1}.x + {a sub 0}
.EN
.LP
for some $n \[mo] N$ (or $n = 0$) and real coefficients $a sub n$, $a sub {n - 1}$, ..., $a sub 2$, $a sub 1$, $a sub 0$.

.SH
.UL Examples
.LP
.B *
$f(x) = 7{x sup 3} - 2{x sup 2} - 4x + 11$
.LP
.B *
$g(x) = 3 - pi{x sup 38}$
.LP
.B *
$h(x) = {sqrt 2}{x sup 2} + {1 over 2}{x sup 4} - 1$   are
polynomials
.LP
Every linear function $f(x) = m.x + b$ is a polynomial with
$n = 1$, ${a sub 1} = m$ and ${a sub 0} = b$
.LP
Every quadratic function $f(x) = a{x sup 2} + bx + c$ is a
polynomial with $n = 2$, ${a sub 2} = a$, ${a sub 1} = b$ and
${a sub 0} = c$
.LP
Every monomial $f(x) = a.{x sup n}$ is a polynomial with ${a
sub n} = a$ and ${a sub {n - 1}} = ... = {a sub 2} = {a sub
1} = {a sub 0} = 0$, so only one term is left
.LP
.LP
The 
.B degree
of a polynomial is the largest numbers $n \[mo] N$  $\[cu]$
$\[lC]\[u00B0]\[rC]$ with ${a sub n} != 0$
.LP
.LP
A polynomial of degree 0 is a constant function 
.LP
A polynomial of degree 1 is a linear function with slope $m != 0$
.LP
A polynomial of degree 2 is a quadratic function
.LP
A polynomial of degree 3 is a cubic function
.LP
A polynomial of degree 4 is a quartic function
.LP
.LP
.SH
.UL Example
.PP
Using $id(x) = x$ and ${1 sub c}(x) = x$ we can build any polynomial
.EQ
f(x) = {a sub n}.{x sup n} + ... + {a sub 1}.x + {a sub 0}
.EN
.PP
by setting 
.EQ
f = {a sub n}.{id sup n} + ... + {a sub 1}.id + {a sub 0}.{1
sub c}
.EN
.PP
in terms of operations on functions. E.g. we have 
.EQ
{id sup 2}(x) = (id.id)(x) = id(x).id(x) = x.x = x sup 2
.EN
.EQ
{id sup 3}(x) = (id.{id sup 2})(x) = id(x).{id sup 2}(x) =
x.{x sup 2} = x sup 3
.EN
.PP
etc, with the general formula
.EQ
{id sup 2}(x) = x sup n
.EN
.PP
for all $x \[mo] R$, (you can prove this by mathematical induction )

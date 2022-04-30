.EQ
delim $$
.EN
.TL
Roots of polynomials
.AU
Ko Sanders
.AI
DCU
.LP
.NH
Generel Notes
.LP
.I "* see lecture notes 4 for definition of degree"

For a generel polynomial $f(x)$ it can be hard to solve $f(x)
= 0$, i.e. to find its roots. This gets harder if the degree
of $f$ increases:

If $f(x)$ has degree $<= 2$ we can find all real roots. There
are formulae for these roots in terms of the coefficients of
the polynomial.

If $f(x)$ has degree $3$ or $4$ there are also formulae for
the roots, but they are rather complicated and we won't use
them.

If $f(x)$ has degree $>= 5$ there is no general formula for
its roots. In fact, there is a proof that such a formula
cannot exist.

.UL Example
Find the roots of $f(x) = {x sup 7} - 9{x sup 3}$


Solution: We notice that $f(x) = {x sup 3}.({x sup 4} - 9) = {x sup 3}.({x sup 2} - 3).({x sup 2} + 3)$


For any $x \[mo] R$ we have

.QS
$f(x) = 0$ if and only if $({x sup 3} = 0$ or ${x sup 2} - 3 = 0$ or ${x sup 2} + 3 = 0)$
.QE

${x sup 3} = 0$ has only one solution: $x = 0$, (if $x > 0$, then ${x sup 3} > 0$ and if $x < 0$, then ${x sup 3} < 0$)
${x sup 2} - 3 = 0$ has two solutions: $x = - sqrt 3$ or $x = + sqrt 3$,
${x sup 2} + 3 = 0$ has no solutions in $R$.

Therefore, the roots of $f(x)$ are $0$, $- sqrt 3$ and $sqrt 3$.


To find the roots of general polynomials we can try some of these strategies:

.QS
1) Have a lucky guess to find a root.

2) Use information about one are several roots to help find
more roots.

3) Approximate a root by using a clever algorithm (e.g. the
Newton-Raphson method), which can be programmed into a
computer. 
.QE

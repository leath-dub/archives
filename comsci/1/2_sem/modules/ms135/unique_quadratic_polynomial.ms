.EQ
delim $$
.EN
.TL
Unique formula for quadratic polynomial
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

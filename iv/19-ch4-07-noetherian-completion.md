<!-- original page 182 -->

## §7. Application to relations between a Noetherian local ring and its completion. Excellent rings

The present section is devoted above all to the exposition of certain properties of Noetherian rings, generally stable
under passage to an algebra of finite type or under localization, which are true for the rings one encounters most often
(algebras of finite type over $Z$, or over a field, or over a complete Noetherian local ring), without being so for all
Noetherian rings. A first series of properties, tied to the theory of dimension and especially to the chain condition,
forms the subject of nos. 1 and 2; all the properties envisaged are true for the quotients of regular Noetherian rings,
and their proofs in this case are for the most part easy and well known [30]; for these rings the developments of §§1
and 2 are accordingly of no interest.

This is no longer so for the properties studied in nos. 3, 4 and 5 (which do not depend on nos. 1 and 2); their proofs,
even in the case of the localizations of algebras of finite type over a field or over $Z$ (where they are due for the
most part to Zariski and Nagata), are most often delicate; classical examples are for instance the equivalences $A$
normal $\Leftrightarrow \hat{A}$ normal, and $A$ reduced $\Leftrightarrow \hat{A}$ reduced. We develop a systematic
method for formulating and proving such properties, by means of the properties of the *fibres* of the canonical morphism
$\operatorname{Spec}(\hat{A}) \to \operatorname{Spec}(A)$ and using the notions and results expounded in §6; the success
of this method rests in the last analysis on the excellent properties of *complete local rings* and of those deduced
from them by localization or passage to an algebra of finite type. In this regard, Nagata's theorem `(6.12.7)` saying
that, for such a ring, the singular locus in $\operatorname{Spec}(A)$ is closed plays a crucial role; the same is so
(concerning the permanence properties) of the regularity criterion `(0, 22.3.4)`, which is more technical in nature.

Finally, in nos. 6 and 7, we apply the results obtained to the study of the finiteness of the integral closure of
Noetherian integral rings.

The reader will note that the most delicate results of §7 will be of only slight use in the rest of Chapter IV, and even
in the later chapters.

<!-- original page 183 -->

### 7.1. Formal equidimensionality and formally catenary rings

**Definition (7.1.1).**

<!-- label: IV.7.1.1 -->

*We say that a Noetherian local ring $A$ is **formally equidimensional** if its completion `Â` is equidimensional
`(0, 16.1.4)`.*

**Proposition (7.1.2).**

<!-- label: IV.7.1.2 -->

*Let $A$ be a Noetherian local ring and $p_{i}$ $(1 \leq i \leq n)$ its minimal prime ideals. In order that $A$ be
formally equidimensional, it is necessary and sufficient that the $A/p_{i}$ be so and that $A$ be equidimensional (in
other words, that the $A/p_{i}$ have the same dimension).*

Indeed, this results from the fact that for every prime ideal $p'$ of `Â`, $p' \cap A$ contains one of the $p_{i}$,
hence $p'$ contains one of the $p_{i} \hat{A}$, and $\hat{A}/p_{i} \hat{A} = (A/p_{i}) \otimes_{A} \hat{A}$ is the
completion of the local ring $A/p_{i}$ $(0_{I}, 7.3.3)$, hence has the same dimension. Every maximal chain of prime
ideals of `Â` therefore identifies canonically with a maximal chain of prime ideals of one of the $\hat{A}/p_{i}
\hat{A}$, and conversely, whence the conclusion at once.

**Proposition (7.1.3).**

<!-- label: IV.7.1.3 -->

*Let $A$, $A'$ be two Noetherian local rings, $\mathfrak{m}$ the maximal ideal of $A$, $\phi : A \to A'$ a local
homomorphism; suppose that $A'$ is a flat $A$-module, and that $A'$ is equidimensional and catenary. Then:*

*(i) $A$ is equidimensional and catenary.*

*(ii) Suppose further that $\mathfrak{m}A'$ is an ideal of definition of $A'$. Then, if $\mathfrak{a}$ is an ideal of
$A$, in order that $A'/\mathfrak{a}A'$ be equidimensional, it is necessary and sufficient that $A/\mathfrak{a}$ be so.
In particular, for every prime ideal $p$ of $A$, $A'/pA'$ is equidimensional.*

Let us first prove the second assertion of (ii). Set $X = \operatorname{Spec}(A)$, $X' = \operatorname{Spec}(A')$, $Y =
V(p) = \operatorname{Spec}(A/p)$, $Y' = V(pA') = \operatorname{Spec}(A'/pA')$; if $f : X' \to X$ is the morphism
corresponding to $\phi$, $Y'$ is also the closed sub-prescheme $f^{-1}(Y)$ of $X'$. Since $\mathfrak{m}A'$ is an ideal
of definition of $A'$, one has

$$ (7.1.3.1) \dim(X) = \dim(X') $$

by virtue of `(6.1.3)`; similarly $\mathfrak{m}A'/pA'$ is an ideal of definition of $A'/pA'$ and $Y'$ is flat over $Y$
`(2.1.4)`, hence `(6.1.3)`

$$ (7.1.3.2) \dim(Y) = \dim(Y'). $$

Let $y$ be the generic point of $Y$, $Y'_{i}$ $(1 \leq i \leq r)$ the irreducible components of $Y'$, $y'_{i}$ the
generic point of $Y'_{i}$ $(1 \leq i \leq r)$; one has $f(y'_{i}) = y$ for every $i$ `(2.3.4)`. On the other hand,
$y'_{i}$ is a maximal point of the fibre $f^{-1}(y)$ $(0_{I}, 2.1.8)$, hence $\mathcal{O}_{X', y'_{i}}
\otimes_{\mathcal{O}_{X, y}} \mathit{k}(y) = \mathcal{O}_{X', y'_{i}}/\mathfrak{m}_{y} \mathcal{O}_{X', y'_{i}}$ is of
dimension `0`, in other words $\mathfrak{m}_{y} \mathcal{O}_{X', y'_{i}}$ is an ideal of definition of $\mathcal{O}_{X',
y'_{i}}$; one can again apply `(6.1.3)`, which gives

```text
(7.1.3.3)                          dim(𝒪_{X', y'_i}) = dim(𝒪_{X, y})
```

that is to say `(5.1.2)`

```text
(7.1.3.4)                       codim(Y'_i, X') = codim(Y, X)
```

for every $i$. Since $A'$ is equidimensional and catenary, one has, by virtue of `(0, 14.3.5)`

```text
(7.1.3.5)                       dim(X') = dim(Y'_i) + codim(Y'_i, X')
```

<!-- original page 184 -->

for every $i$; by virtue of `(7.1.3.1)`, `(7.1.3.2)` and `(7.1.3.4)` and of the inequality $\dim(Y'_{i}) \leq \dim(Y')$,
one deduces

```text
(7.1.3.6)                          dim(X) ≤ dim(Y) + codim(Y, X)
```

hence the two sides of this inequality are equal by `(0, 14.2.2.2)`; moreover this equality entails

```text
(7.1.3.7)                          dim(Y'_i) = dim(Y') = dim(Y)
```

for every $i$, which proves the second assertion of (ii).

Let us now prove the first assertion of (ii). Let $p_{j}$ $(1 \leq j \leq n)$ be the prime ideals of $A$ minimal among
those that contain $\mathfrak{a}$, and let $p'_{jh}$ be the prime ideals of $A'$ minimal among those containing $p_{j}
A'$ $(1 \leq h \leq m_{j})$; one then knows `(2.3.4)` that the $p'_{jh}$ `(1 ≤ j ≤ n, 1 ≤ h ≤ m_j` for every `j)` are
also the prime ideals of $A'$ minimal among those containing $\mathfrak{a}A'$. From what was seen above, for every $j$,
the dimensions of the rings $A'/p'_{jh}$ $(1 \leq h \leq m_{j})$ are all equal, and so equal to $\dim(A'/p_{j} A')$,
itself equal to $\dim(A/p_{j})$ by `(7.1.3.2)`. To say that $A'/\mathfrak{a}A'$ is equidimensional means then that the
dimensions of the $A/p_{j}$ are all equal, that is to say that $A/\mathfrak{a}$ is equidimensional.

Finally let us prove (i). Let $r'$ be a prime ideal of $A'$ minimal among those containing $\mathfrak{m}A'$, and set
$A'' = A'_{r'}$; since `A''` is a flat $A'$-module, it is also a flat $A$-module; moreover `A''` is equidimensional and
catenary `(0, 16.1.4)`, and $\mathfrak{m}A''$ is an ideal of definition of `A''`. We may therefore reduce to the case
where $\mathfrak{m}A'$ is an ideal of definition of $A'$. If now $p$ and $q \subset p$ are two prime ideals of $A$, one
can apply (ii) to $A/q$ and to $A'/qA'$, which is equidimensional and flat over $A/q$; if $Z = \operatorname{Spec}(A/q)$
and $Y = \operatorname{Spec}(A/p)$, one has therefore `dim(Z) = dim(Y) + codim(Y, Z)`; moreover one can apply
`(7.1.3.6)`, which shows that `codim(Y, X) = dim X - dim Y`; since $X$ is equicodimensional, these relations show that
it is biequidimensional by virtue of `(0, 14.3.3)`.

**Corollary (7.1.4).**

<!-- label: IV.7.1.4 -->

*Let $A$ be a Noetherian local ring that is formally equidimensional. Then:*

*(i) $A$ is equidimensional and catenary (in other words, biequidimensional).*

*(ii) Let $\mathfrak{a}$ be an ideal of $A$; in order that $A/\mathfrak{a}$ be equidimensional, it is necessary and
sufficient that $A/\mathfrak{a}$ be formally equidimensional. In particular, for every prime ideal $p$ of $A$, $A/p$ is
formally equidimensional.*

If $\mathfrak{m}$ is the maximal ideal of $A$, $\mathfrak{m}\hat{A}$ is an ideal of definition of `Â`. By hypothesis `Â`
is equidimensional, and one knows on the other hand that it is catenary `(5.6.4)`; it then suffices to apply `(7.1.3)`
to $A' = \hat{A}$.

**Corollary (7.1.5).**

<!-- label: IV.7.1.5 -->

*Let $A$ be a Noetherian local ring such that there exists a finitely generated $A$-module $M$ which is a Cohen-Macaulay
$A$-module and for which $Supp(M) = \operatorname{Spec}(A)$ (which will be the case for instance if $A$ is a
Cohen-Macaulay ring). Then $A$ is formally equidimensional, hence `(7.1.4)` in order that a quotient ring $B$ of $A$ be
formally equidimensional, it is necessary and sufficient that it be equidimensional.*

<!-- original page 185 -->

Indeed, $\hat{M} = M \otimes_{A} \hat{A}$ is a Cohen-Macaulay `Â`-module `(0, 16.5.2)` with support equal to
$\operatorname{Spec}(\hat{A})$; consequently `(0, 16.5.4)`, `Â` is equidimensional.

**Remark (7.1.6).**

<!-- label: IV.7.1.6 -->

*One has seen `(6.3.8)` that under the hypotheses of `(7.1.5)`, for every quotient ring $B$ of $A$, the fibres of the
canonical morphism $\operatorname{Spec}(\hat{B}) \to \operatorname{Spec}(B)$ are Cohen-Macaulay preschemes; consequently
(`(6.4.3)` and `(5.7.5)`), in order that $B$ have no embedded associated prime ideals, it is necessary and sufficient
that the same be so of $\hat{B}$.*

**Lemma (7.1.7).**

<!-- label: IV.7.1.7 -->

*Let $A$ be a Noetherian local ring, $p_{i}$ $(1 \leq i \leq r)$ its minimal prime ideals. Suppose that each of the
rings $A/p_{i}$ is formally equidimensional. Then, for every prime ideal $q$ of $A$ and every $i$ such that $p_{i}
\subset q$, the ring $A_{q}/p_{i} A_{q}$ is formally equidimensional.*

Since $A_{q}/p_{i} A_{q}$ is the local ring of $A/p_{i}$ at the prime ideal $q/p_{i}$, we may reduce to the case where
$A$ is integral and formally equidimensional. Set $A' = \hat{A}$, and let $q'$ be one of the prime ideals of $A'$
minimal among those containing `qA'`; if one sets $B = A_{q}$, $B' = A'_{q'}$ is a flat $B$-module $(0_{I}, 6.3.2)$. Set
$C = \hat{B}$, $C' = \hat{B}'$; since $B'$ is a flat $B$-module, one knows that $C'$ is a flat $C$-module (Bourbaki,
*Alg. comm.*, chap. III, §5, n° 4, prop. 4). Since $A'$ is catenary `(5.6.4)` and equidimensional by hypothesis, the
same is so of $B' = A'_{q'}$ `(0, 16.1.4)`; moreover, since $A'$ is isomorphic to a quotient of a regular ring by virtue
of Cohen's theorem `(0, 19.8.8)`, the same is so of $B'$ `(0, 17.3.9)`; one concludes therefore from `(7.1.5)` that $C'$
is equidimensional. On the other hand, $C'$ is catenary `(5.6.4)`, hence $C$ is equidimensional by virtue of
`(7.1.3, (i))`.

**Theorem (7.1.8).**

<!-- label: IV.7.1.8 -->

*Let $A$ be a Noetherian local ring. The following conditions are equivalent:*

*a) Every integral quotient ring of $A$ is formally equidimensional.*

*b) The quotient rings of $A$ by its minimal prime ideals are formally equidimensional.*

*c) Every local ring $B$ which is an $A$-algebra essentially of finite type `(1.3.8)` and is equidimensional, is
formally equidimensional.*

It is trivial that c) implies a) and that a) implies b). On the other hand, since every prime ideal of $A$ contains a
minimal prime ideal of $A$, b) entails a) by virtue of `(7.1.4, (ii))`. It remains to see that a) implies c).

It suffices to prove that the quotients of $B$ by its minimal prime ideals are formally equidimensional `(7.1.2)`; since
every quotient ring of $B$ is again an $A$-algebra essentially of finite type `(1.3.9)`, one may first suppose $B$
integral. If $q$ is the inverse image in $A$ of the maximal ideal of $B$, one knows that $B$ is also an $A_{q}$-algebra
essentially of finite type `(1.3.10)`, and it results from a) and `(7.1.7)` that every integral quotient ring of $A_{q}$
is formally equidimensional; one may therefore suppose that the homomorphism $A \to B$ is a local homomorphism. The
kernel $r$ of this homomorphism is then a prime ideal of $A$, and by virtue of a), every integral quotient ring of $A/r$
is formally equidimensional; since $B$ is an $(A/r)$-algebra essentially of finite type, one sees that one may also
suppose

<!-- original page 186 -->

that $A$ is integral and is a subring of $B$. One knows `(1.3.11)` that $B$ is a quotient of a local ring of the form
$C_{p}$, where $C = A[T_{1}, \cdots, T_{n}]$ is a polynomial algebra and $p$ a prime ideal of $C$ lying over the maximal
ideal $\mathfrak{m}$ of $A$. By virtue of `(7.1.7)`, it suffices to prove that $C_{p}$ is formally equidimensional; in
other words, one may reduce to the case where $B = C_{p}$.

Set $A' = \hat{A}$, and $C' = A'[T_{1}, \cdots, T_{n}] = C \otimes_{A} A'$; there is a unique prime ideal $p'$ of $C'$
lying over the maximal ideal $\mathfrak{m}A'$ of $A'$, hence lying over $p$; set $B' = C'_{p'}$; the homomorphism $B \to
B'$ is local and makes $B'$ a flat $B$-module. One knows then that $\hat{B}'$ is a flat $\hat{B}$-module (Bourbaki,
*Alg. comm.*, chap. III, §5, n° 4, prop. 4); since $\hat{B}'$ is catenary `(5.6.4)`, it will suffice to prove that
$\hat{B}'$ is equidimensional to deduce that $\hat{B}$ is so as well `(7.1.3, (i))`, which will finish the proof.

Now, $A'$ is a quotient of a regular ring by Cohen's theorem `(0, 19.8.8)`, hence the same is so of $B'$ `(0, 17.3.9)`;
by virtue of `(7.1.5)`, to show that $B'$ is formally equidimensional, it suffices to prove that $B'$ is
*equidimensional*; and for this, it suffices to show that $C'$ is equidimensional, since $C'$ is a quotient of a regular
ring, hence catenary `(5.6.4)`. Now the minimal prime ideals of $C'$ are the ideals `q'C'`, where $q'$ runs through the
minimal prime ideals of $A'$ `(5.5.3)`, and one has $C'/q'C' = (A'/q')[T_{1}, \cdots, T_{n}]$. Since $A'$ is
equidimensional by hypothesis (since $A$ is integral), the same is so of $C'$ by `(5.5.4)`. Q.E.D.

**Definition (7.1.9).**

<!-- label: IV.7.1.9 -->

*When the equivalent conditions of `(7.1.8)` are satisfied, one says that $A$ is a **formally catenary** ring.*

For a Noetherian local ring, it therefore amounts to the same to say that it is formally equidimensional or that it is
formally catenary and equidimensional, by virtue of `(7.1.2)`.

**Proposition (7.1.10).**

<!-- label: IV.7.1.10 -->

*Every local ring $A$ which is a quotient of a Cohen-Macaulay local ring is formally catenary.*

This results at once from `(7.1.8)` and from `(7.1.5)` applied to the integral quotient rings of $A$.

**Proposition (7.1.11).**

<!-- label: IV.7.1.11 -->

*(i) A formally catenary Noetherian local ring is universally catenary.*

*(ii) If $A$ is a formally catenary Noetherian local ring, every local ring $B$ which is an $A$-algebra essentially of
finite type is formally catenary.*

Assertion (ii) results at once from condition c) of `(7.1.8)` and from the fact that if a local ring $C$ is a
$B$-algebra essentially of finite type, $C$ is also an $A$-algebra essentially of finite type `(1.3.9)`. To prove (i),
note first that by virtue of condition b) of `(7.1.8)`, a formally catenary Noetherian local ring $A$ is catenary, since
the quotients of $A$ by its minimal prime ideals are so `(7.1.4)`. If now $E$ is an $A$-algebra of finite type, it
results from the foregoing and from (ii) that every local ring of $E$ at a prime ideal is catenary, hence that $E$ is
catenary. Hence $A$ is universally catenary.

<!-- original page 187 -->

**Remarks (7.1.12).**

<!-- label: IV.7.1.12 -->

*(i) It is not known whether, conversely, a universally catenary Noetherian local ring is always formally catenary.*

*(ii) A Noetherian local ring $A$ of dimension `1` is necessarily equidimensional, its maximal ideal not being able to
be minimal (for in this case $A$ would be of dimension `0`). Since $\dim(\hat{A}) = 1$, this shows that $A$ is even
formally equidimensional, and a fortiori formally catenary (hence universally catenary). On the other hand, the local
ring of dimension `2` defined in `(5.6.11)`, which is catenary but not universally catenary, is a fortiori not formally
catenary.*

**Corollary (7.1.13).**

<!-- label: IV.7.1.13 -->

*Let $Y$ be a locally Noetherian irreducible prescheme of dimension `1`, $X$ an irreducible prescheme, $f : X \to Y$ a
dominant morphism of finite type, $\xi$, $\eta$ the generic points of $X$ and $Y$ respectively. Then, for every $y \in
f(X)$, the dimensions of the irreducible components of $f^{-1}(y)$ are all equal to $deg.tr_{\mathit{k}(\eta)}
\mathit{k}(\xi)$.*

By hypothesis, $f^{-1}(\eta)$ is irreducible with generic point $\xi$ and of dimension $deg.tr_{\mathit{k}(\eta)}
\mathit{k}(\xi)$ `(5.2.1)`. Since $Y$ is irreducible and of dimension `1`, one has $\dim(\mathcal{O}_{y}) = 1$ for every
$y \neq \eta$, and $\mathcal{O}_{y}$ is universally catenary by virtue of `(7.1.12, (ii))`. If $y \in f(X)$ and if $z$
is a generic point of an irreducible component $Z$ of $f^{-1}(y)$, one has therefore, by `(5.6.5)`

```text
                       dim(Z) = 1 + dim(f⁻¹(η)) - dim(𝒪_{X, z}).
```

But one has $\dim(\mathcal{O}_{X, z}) \leq \dim(\mathcal{O}_{y})$ `(0, 16.3.9)`, and on the other hand, since $z$ is not
the generic point of $X$, $\dim(\mathcal{O}_{X, z}) > 0$; hence $\dim(\mathcal{O}_{X, z}) = 1$ and $\dim(Z) =
\dim(f^{-1}(\eta))$.

### 7.2. Strictly formally catenary rings

**Notations (7.2.1).**

<!-- label: IV.7.2.1 -->

*For a Noetherian integral ring $A$, we shall denote by $A^{(1)}$ the intersection of the local rings $A_{p}$, where $p$
runs through the set of prime ideals of $A$ of height `1` `(5.10.17)`. If $A$ is an integral Noetherian local ring, we
shall denote by $A^{(\omega)}$ the intersection of the $A_{p}$ where this time $p$ runs through the set of all prime
ideals of $A$ distinct from the maximal ideal.*

*We shall say that a Noetherian local ring $A$ is **strictly equidimensional** if, for every prime ideal $p \in Ass(A)$,
one has $\dim(A/p) = \dim(A)$; it amounts to the same to say that $A$ is equidimensional and without embedded associated
prime ideals.*

**Example (7.2.1.1).**

<!-- label: IV.7.2.1.1 -->

*Let $A$ be a Noetherian local ring of dimension `1`. Then the following conditions are equivalent:*

*a) $A$ is without embedded associated prime ideals.*

*a') `Â` is without embedded associated prime ideals.*

*b) $A$ is strictly equidimensional.*

*b') `Â` is strictly equidimensional.*

*c) $A$ is a Cohen-Macaulay ring.*

Indeed, a) means that the maximal ideal $\mathfrak{m}$ of $A$ is not associated to $A$, hence the prime ideals
associated to $A$ are the minimal ideals of $A$, all distinct from $\mathfrak{m}$, and

<!-- original page 188 -->

for such an ideal $p$, one necessarily has $\dim(A/p) = 1$; hence a) implies b). Conversely, b) implies that every prime
ideal $p \in Ass(A)$ is distinct from $\mathfrak{m}$, hence minimal, and consequently b) implies a). One already knows
that a) and c) are equivalent for a local ring of dimension `1` `(5.7.8)`. Since it amounts to the same to say that $A$
is a Cohen-Macaulay ring or that `Â` is a Cohen-Macaulay ring `(0, 16.5.2)`, and since one has $\dim(\hat{A}) = 1$, one
finally sees that a') and b') are equivalent to c).

**Proposition (7.2.2).**

<!-- label: IV.7.2.2 -->

*Let $A$ be an integral Noetherian local ring; set $A' = \hat{A}$, $X = \operatorname{Spec}(A)$,
$X' = \operatorname{Spec}(A')$ and denote by $f : X' \to X$ the canonical morphism. Let $a$ be the closed point of $X$,
$j : X - {a} \to X$ the canonical injection. Let $\mathcal{F}$ be a coherent $\mathcal{O}_{X}$-Module,
$\mathcal{F}' = f*(\mathcal{F}) = \mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'}$; then the following conditions
are equivalent:*

*a) The $\mathcal{O}_{X}$-Module $j_{*}(\mathcal{F} | X - {a})$ is coherent.*

*b) For every $x' \in Ass(\mathcal{F}')$, one has $\dim(\overline{x'}) \geq 2$.*

Let $a'$ be the closed point of $X'$, which is the unique point of the fibre $f^{-1}(a)$, and let $j' : X' - {a'} \to
X'$ be the canonical injection. Since the morphism $f$ is faithfully flat and quasi-compact, it is equivalent to say
that $j_{*}(\mathcal{F} | X - {a})$ is coherent or that $j'_{*}(\mathcal{F}' | X' - {a'})$ is coherent `(5.9.5)`. On the
other hand, since $A'$ is isomorphic to the quotient of a regular local ring by Cohen's theorem `(0, 19.8.8)`, it
results from `(5.11.4)` that condition b) of the statement is equivalent to the fact that $j'_{*}(\mathcal{F}' | X' -
{a'})$ is coherent. Whence the proposition.

Instead of applying `(5.11.4)` using Cohen's theorem, which (by `(5.11.2)`) implicitly appeals to the cohomological
results of chap. III, one may also use the fact that $A'$ is universally catenary `(5.6.4)` and universally Japanese by
virtue of `(7.6.5)` (the proof of this last result not using `(7.2.2)`).

**Proposition (7.2.3).**

<!-- label: IV.7.2.3 -->

*Let $A$ be an integral Noetherian local ring. With the notations of `(7.2.2)`, the following conditions are
equivalent:*

*a) $A^{(1)}$ is a finite $A$-algebra.*

*b) For every closed part $T$ of $X$ of codimension $\geq 2$, if one denotes by $i : X - T \to X$ the canonical
injection, $i_{*}(\mathcal{O}_{X - T})$ is a coherent $\mathcal{O}_{X}$-Module.*

*c) For every $x' \in Ass(\mathcal{O}_{X'})$ and every closed part $T$ of $X$ of codimension $\geq 2$, one has
$codim(f^{-1}(T) \cap \overline{x'}, \overline{x'}) \geq 2$.*

Set $Z = Z^{(2)}(X)$ `(5.10.13)` and $Z' = f^{-1}(Z)$, which are parts stable under specialization; conditions a) and b)
are equivalent respectively to the following properties: $a_{1}$) $\mathcal{H}^{0}_{X/Z}(\mathcal{O}_{X})$ is coherent;
$b_{1}$) $\mathcal{H}^{0}_{X/T}(\mathcal{O}_{X})$ is coherent for every closed part $T$ of $X$ of codimension $\geq 2$.
Taking `(5.9.5)` into account, these two latter properties are respectively equivalent to: $a'_{1}$)
$\mathcal{H}^{0}_{X'/Z'}(\mathcal{O}_{X'})$ is coherent; $b'_{1}$) putting $T' = f^{-1}(T)$,
$\mathcal{H}^{0}_{X'/T'}(\mathcal{O}_{X'})$ is coherent for every closed part $T$ of $X$ of codimension $\geq 2$. Now,
every point of $Ass(\mathcal{O}_{X'})$ projects in $X$ to the generic point of $X$ since $f$ is a flat morphism
`(3.3.2)`; since by definition this point does not belong to $Z$, one sees that $Ass(\mathcal{O}_{X'})$ does not meet
$Z'$; the equivalence of $a'_{1}$) and $b'_{1}$) therefore results from `(5.11.5)`, since $A'$ is isomorphic to a
quotient of a regular ring by virtue of Cohen's theorem `(0, 19.8.8)` (or also

<!-- original page 189 -->

because $A'$ is universally Japanese `(7.6.5)`). For this reason, conditions $b'_{1}$) and c) are also equivalent by
virtue of `(5.11.4)`.

**Proposition (7.2.4).**

<!-- label: IV.7.2.4 -->

*Let $A$ be a Noetherian local ring and set $X = \operatorname{Spec}(A)$. The following conditions are equivalent:*

*a) For every integral quotient ring $B$ of $A$, the ring $B^{(1)}$ is a finite $B$-algebra.*

*b) For every coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ and every part $Z$, stable under specialization, such that
for every $x \in Ass(\mathcal{F}) \cap (X - Z)$ one has $codim(\overline{x} \cap Z, \overline{x}) \geq 2$, the
$\mathcal{O}_{X}$-Module $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is coherent.*

*c) For every closed part $T$ of $X$ and every coherent $\mathcal{O}_{U}$-Module $\mathcal{G}$ (where $U = X - T$) such
that, for every $x \in Ass(\mathcal{G})$, one has $codim(\overline{x} \cap T, \overline{x}) \geq 2$,
$i_{*}(\mathcal{G})$ (where $i : U \to X$ is the canonical injection) is a coherent $\mathcal{O}_{X}$-Module.*

*d) For every integral quotient ring $B$ of $A$ and every ideal $\mathfrak{J}$ of height $\geq 2$ in $B$, the ring
$\bigcap_{p \not\supseteq \mathfrak{J}} B_{p}$ is a finite $B$-algebra.*

*e) For every integral quotient ring $B$ of $A$ and every local ring $C = B_{q}$ at a prime ideal $q$ of $B$, such that
$\dim(C) \geq 2$, the ring $C^{(\omega)}$ is a finite $C$-algebra (or, what comes to the same, if $Y =
\operatorname{Spec}(C)$ and if $U$ is the complement in $Y$ of the closed point of $C$ and $j : U \to Y$ the canonical
injection, $j_{*}(\mathcal{O}_{U})$ is a coherent $\mathcal{O}_{Y}$-Module).*

*f) For every integral quotient ring $B$ of $A$, every local ring $C = B_{q}$ at a prime ideal $q$ of $B$ such that
$\dim(C) \geq 2$, and for every ideal $r \in Ass(\hat{C})$, one has $\dim(\hat{C}/r) \geq 2$.*

One already knows `(5.11.6)` that a) and b) are equivalent, as are c) and d), and that a) entails d). The equivalence of
a) and d) in the present case results from `(7.2.3)` applied to an integral quotient ring $B$ of $A$, condition d) being
an equivalent formulation of condition `(7.2.3, b))` by virtue of `(5.9.3.1)`. The equivalence of e) and f) is a
consequence of `(7.2.2)` applied to the coherent $\mathcal{O}_{Y}$-Module $\mathcal{O}_{Y}$ itself. One has already
remarked `(5.11.7, (ii))` that if $A$ satisfies a), the same is so of every finite $A$-algebra and of every ring of
fractions of $A$. Condition a) for $A$ therefore entails (with the notations of e)) that the ring $C$ satisfies a),
hence also c); but since $C$ is integral and $\dim(C) \geq 2$, one may apply to $C$ the condition c) taking for $T$ the
closed point of $Y = \operatorname{Spec}(C)$; this proves that a) entails e). It remains to prove that e) entails a);
one may evidently reduce to the case where $A$ is integral and $B = A$, and the question is then to show that condition
e) entails condition `(7.2.3, c))`. With the notations of `(7.2.3, c))`, let us therefore consider a point $y' \in
f^{-1}(T) \cap \overline{x'}$, and set $y = f(y')$ and $C = \mathcal{O}_{X, y}$; since $y \in T$, one has by hypothesis
$\dim(C) \geq 2$, and consequently (with the notations of e)), $j_{*}(\mathcal{O}_{U})$ is a coherent
$\mathcal{O}_{Y}$-Module. Now, set $Y' = X' \times_{X} Y$; the morphism $f : X' \to X$ being flat, the same is so of $g
= f_{(Y)} : Y' \to Y$. Moreover the space underlying $Y'$ identifies with $f^{-1}(Y)$ `(I, 3.6.5)`, and since $A$ is
integral and $f$ flat, $Ass(\mathcal{O}_{X'})$ is contained in the fibre of the generic point of $X$ `(3.3.2)`; the
latter being contained in $Y$, one has $x' \in Y'$. Let $U' = g^{-1}(U)$, and let $j'$ be the canonical injection $U'
\to Y'$; since $j_{*}(\mathcal{O}_{U})$ is a coherent $\mathcal{O}_{Y}$-Module and $g$ is flat, it results from
`(5.9.4)` that $j'_{*}(\mathcal{O}_{U'})$ is a coherent $\mathcal{O}_{Y'}$-Module. Now one has $x' \in
Ass(\mathcal{O}_{U'})$, hence one concludes from `(5.10.10)` that one has, in $Y'$,

<!-- original page 190 -->

$codim(\overline{y'} \cap \overline{x'}, \overline{x'}) \geq 2$. Since $y'$ is arbitrary in $f^{-1}(T) \cap
\overline{x'}$, one has indeed $codim(f^{-1}(T) \cap \overline{x'}, \overline{x'}) \geq 2$ in $X'$. Q.E.D.

**Theorem (7.2.5).**

<!-- label: IV.7.2.5 -->

*Let $A$ be a Noetherian local ring. The following conditions are equivalent:*

*a) For every integral quotient ring $B$ of $A$, the completion $\hat{B}$ is strictly equidimensional `(7.2.1)`.*

*b) $A$ is formally catenary `(7.1.9)` and the fibres of the canonical morphism $\operatorname{Spec}(\hat{A}) \to
\operatorname{Spec}(A)$ satisfy `(S_1)` (in other words, have no embedded associated prime cycle).*

*c) $A$ is universally catenary `(5.6.2)` and for every integral quotient ring $B$ of $A$, the ring $B^{(1)}$ is a
finite $B$-algebra (cf. `(7.2.4)`).*

*d) $A$ is universally catenary and for every integral quotient ring $B$ of $A$ and every local ring $C = B_{q}$ at a
prime ideal $q$ of $B$, such that $\dim(C) \geq 2$, the ring $C^{(\omega)}$ is a finite $C$-algebra.*

*e) $A$ is universally catenary and for every integral quotient ring $B$ of $A$ and every local ring $C = B_{q}$ at a
prime ideal $q$ of $B$, such that $\dim(C) \geq 2$, the completed ring `Ĉ` is such that $\operatorname{Spec}(\hat{C})$
has no associated prime cycle of dimension `1`.*

*Moreover, when these conditions are satisfied, then, for every quotient ring $B$ of $A$ which is strictly
equidimensional, the completion $\hat{B}$ is strictly equidimensional.*

The equivalence of c), d) and e) was proved in `(7.2.4)`. To show that a) and b) are equivalent, recall `(7.1.9)` that
to say that $A$ is formally catenary means that for every integral quotient ring $B$ of $A$, $\hat{B}$ is
equidimensional. On the other hand, every fibre of the morphism $\operatorname{Spec}(\hat{A}) \to
\operatorname{Spec}(A)$ at a point $x \in \operatorname{Spec}(A)$ is the fibre of the morphism
$\operatorname{Spec}(\hat{B}) \to \operatorname{Spec}(B)$ at the generic point $x$ of $\operatorname{Spec}(B)$, where $B
= A/\mathfrak{j}_{x}$; to say that this fibre is without embedded associated prime cycle amounts to saying that
$\hat{B}$ has no embedded associated prime ideals, by virtue of `(3.3.3)`; this proves the equivalence of a) and b). The
same reasoning shows that if a) is satisfied, then, for every quotient ring $B$ of $A$ which is without embedded
associated prime ideals, the completion $\hat{B}$ is also without embedded associated prime ideals; on the other hand,
the hypothesis that $A$ is formally catenary entails that if $B$ is equidimensional, the same is so of $\hat{B}$
`(7.1.8)`; this establishes the last assertion of the theorem.

Let us now show that a) implies c). Condition a) implies that $A$ is universally catenary `(7.1.11)`; let us show on the
other hand that for every integral quotient ring $B$ of $A$, $B^{(1)}$ is then a finite $B$-algebra. Taking into account
`(7.2.3)` applied to $B$, the question is to show that if $X = \operatorname{Spec}(B)$, if $T$ is a closed part of $X$
of codimension $\geq 2$, $X' = \operatorname{Spec}(\hat{B})$, and $g : X' \to X$ the canonical morphism, then one has,
for every $x' \in Ass(\mathcal{O}_{X'})$, $codim(g^{-1}(T) \cap \overline{x'}, \overline{x'}) \geq 2$. But by hypothesis
$X'$ has no embedded associated prime cycle, hence $\inf(codim(g^{-1}(T) \cap \overline{x'}, \overline{x'}))$ when $x'$
runs through $Ass(\mathcal{O}_{X'})$ is none other than $codim(g^{-1}(T), X')$. Now, since $g$ is a faithfully flat
morphism, one has `(6.1.4)`

```text
                          codim(g⁻¹(T), X') = codim(T, X) ≥ 2.
```

<!-- original page 191 -->

It remains to prove that c) entails a). We reason by induction on $n = \dim(A)$, the theorem being trivial for $n = 0$;
one may moreover reduce to the case where $A = B$ is integral. Let us proceed in two stages, $n$ being $\geq 1$.

I) *Suppose first that $A$ satisfies `(S_2)`.* — Set $X = \operatorname{Spec}(A)$, $A' = \hat{A}$, $X' =
\operatorname{Spec}(A')$ and let $u : X' \to X$ be the canonical morphism; the question is to show that for every
element $x' \in Ass(\mathcal{O}_{X'})$, one has $\dim(\overline{x'}) = n$. Let $f \neq 0$ be an element of the maximal
ideal of $A$, and set $C = A/fA$; one knows `(5.7.6)` that $A/fA$ satisfies `(S_1)`; moreover, since the prime ideals of
$A$ minimal among those containing $f$ are of height `1` by virtue of the Hauptidealsatz, and since $C$ is catenary, $C
= A/fA$ is strictly equidimensional and $\dim(C) = n - 1$. One has $\hat{C} = C \otimes_{A} \hat{A} = A'/fA'$, and $f$
is $A'$-regular by flatness $(0_{I}, 6.3.4)$; if one sets $Y' = V(fA') = \operatorname{Spec}(\hat{C})$, then, for every
maximal point $y'$ of $Y' \cap \overline{x'}$, one has $y' \in Ass(\mathcal{O}_{Y'})$ by virtue of `(3.4.3)`; on the
other hand, one has $y' \neq x'$ since $u(x')$ is the generic point of $X$ `(3.3.2)` and one has $u(y') \in V(fA)$. One
concludes from `(5.1.8)` that

$$ (7.2.5.1) \dim(\overline{y'}) = \dim(\overline{x'}) - 1. $$

But the quotient ring $C = A/fA$ also satisfies hypothesis c) of the statement (`(5.6.1)` and `(5.11.7, (ii))`); by
virtue of the induction hypothesis, one has $\dim(\overline{y'}) = \dim(C) = n - 1$; the conclusion $\dim(\overline{x'})
= n$ therefore results in this case from `(7.2.5.1)`.

II) *General case.* — Since by hypothesis the ring $A^{(1)}$ is a finite $A$-algebra, it satisfies `(S_2)` by virtue of
`(5.10.17, (i))`; the same is so of each of its local rings $(A^{(1)})_{\mathfrak{n}}$ at a maximal ideal
$\mathfrak{n}$, and moreover, since $A$ is universally catenary, the rings $(A^{(1)})_{\mathfrak{n}}$ (which are finite
in number) are all of dimension $n$ `(5.6.10)`; moreover, these rings satisfy hypothesis c) of the statement (`(5.6.1)`
and `(5.11.7, (ii))`). One knows that the completion of $A^{(1)}$, equal to $\hat{A} \otimes_{A} A^{(1)}$, is the direct
product of the completions of the local rings $(A^{(1)})_{\mathfrak{n}}$. Set $X_{1} = \operatorname{Spec}(A^{(1)})$,
`X'_1 = Spec((A^{(1)})^^) = X' ×_X X_1`; for every $x'_{1} \in Ass(\mathcal{O}_{X'_{1}})$, it results from the foregoing
and from case I) that one has $\dim(\overline{x'_{1}}) = n$. Let $u_{1} = u_{(X_{1})} : X'_{1} \to X_{1}$ be the
canonical morphism; since $A$ and $A^{(1)}$ have the same field of fractions, the inverse image of the generic point $x$
of $X$ by the projection $X_{1} \to X$ reduces to the generic point $x_{1}$ of `X_1`, the inverse image by the
projection $X'_{1} \to X'$ of the fibre $u^{-1}(x)$ is the fibre $u^{-1}_{1}(x_{1})$ and this projection induces an
isomorphism of the prescheme $u^{-1}_{1}(x_{1})$ onto $u^{-1}(x)$. This said, the points of $Ass(\mathcal{O}_{X'})$
(resp. $Ass(\mathcal{O}_{X'_{1}})$) are the generic points of the associated prime cycles of $u^{-1}(x)$ (resp.
$u^{-1}_{1}(x_{1})$) `(3.3.1)`. For every $x' \in Ass(\mathcal{O}_{X'})$, there is therefore an $x'_{1} \in
Ass(\mathcal{O}_{X'_{1}})$ lying over $x'$, and if $Z'$ (resp. $Z'_{1}$) is the reduced closed sub-prescheme of $X'$
(resp. $X'_{1}$) having $\overline{x'}$ (resp. $\overline{x'_{1}}$) for underlying space, the projection $Z'_{1} \to Z'$
is a finite and surjective morphism; one concludes `(5.4.2)` that $\dim(\overline{x'}) = \dim(\overline{x'_{1}}) = n$.
Q.E.D.

**Definition (7.2.6).**

<!-- label: IV.7.2.6 -->

*When a Noetherian local ring $A$ satisfies the equivalent conditions of `(7.2.5)`, one says that it is **strictly
formally catenary**.*

<!-- original page 192 -->

**Corollary (7.2.7).**

<!-- label: IV.7.2.7 -->

*Let $A$ be a Noetherian local ring such that there exists a finitely generated $A$-module $M$ which is a Cohen-Macaulay
$A$-module and for which $Supp(M) = \operatorname{Spec}(A)$; then $A$ is strictly formally catenary.*

Indeed, $A$ is formally catenary (`(7.1.5)` and `(7.1.9)`), and on the other hand the fibres of the canonical morphism
$\operatorname{Spec}(\hat{A}) \to \operatorname{Spec}(A)$ are Cohen-Macaulay preschemes `(6.3.8)`, hence a fortiori
satisfy `(S_1)`.

**Corollary (7.2.8).**

<!-- label: IV.7.2.8 -->

*If $A$ is a strictly formally catenary Noetherian local ring, every local ring $B$ which is an $A$-algebra essentially
of finite type is strictly formally catenary.*

Indeed, $B$ is formally catenary `(7.1.11)` and it results from `(7.4.4)` [^1] that the fibres of
$\operatorname{Spec}(\hat{B}) \to \operatorname{Spec}(B)$ satisfy `(S_1)`, whence the conclusion.

**Corollary (7.2.9).**

<!-- label: IV.7.2.9 -->

*Every Noetherian local ring of dimension `1` is strictly formally catenary.*

Indeed, every integral quotient ring $B$ of such a ring $A$ is of dimension `0` or `1`, hence its completion is strictly
equidimensional `(7.2.1.1)`.

**Remarks (7.2.10).**

<!-- label: IV.7.2.10 -->

*(i) It results from `(7.2.7)` and `(7.2.8)` that every quotient ring of a Cohen-Macaulay local ring is strictly
formally catenary.*

*A Noetherian local ring of dimension `2` satisfying `(S_2)` is strictly formally catenary, since it is a Cohen-Macaulay
ring. Recall on the other hand that there are integral Noetherian local rings of dimension `2` which are not universally
catenary, nor a fortiori strictly formally catenary `(5.6.11)`.*

*(ii) It is not known whether a formally catenary ring `(7.1.9)` is strictly formally catenary; this is due to the fact
that one does not know whether, for an integral Noetherian local ring $B$, $\hat{B}$ is without embedded associated
prime ideals `(6.4.3)`. We are likewise unaware whether, in the equivalent conditions c), d), e) of `(7.2.5)`, one can
replace the hypothesis that $A$ is universally catenary by the hypothesis that $A$ is catenary; one can show that this
is so when $A$ is Henselian `(18.9.6)`.*

### 7.3. Formal fibres of Noetherian local rings

**(7.3.1)** We shall consider in this number and the two following ones properties $\mathbf{P}(Z, k)$ of the following
form:

«$Z$ is a locally Noetherian prescheme over a field $k$, and for every $z \in Z$, one has $\mathbf{Q}(\mathcal{O}_{z},
k)$»

where $\mathbf{Q}(A, k)$ is a property of a Noetherian local ring $A$ which is a $k$-algebra; one supposes that if $k'$
is a field isomorphic to $k$, and if $A'$ is a Noetherian local ring which is a $k'$-algebra di-isomorphic to $A$, the
properties $\mathbf{Q}(A, k)$ and $\mathbf{Q}(A', k')$ are equivalent.

<!-- original page 193 -->

If $X$, $Y$ are two locally Noetherian preschemes, we shall say that a morphism $f : X \to Y$ is a **𝐏-morphism** if:

1° $f$ is *flat*;

2° for every $y \in Y$, the property $\mathbf{P}(f^{-1}(y), \mathit{k}(y))$ is true.

**Lemma (7.3.2).**

<!-- label: IV.7.3.2 -->

*Let $X$, $Y$ be two locally Noetherian preschemes, $f : X \to Y$ a morphism. The following properties are equivalent:*

*a) $f$ is a 𝐏-morphism.*

*b) For every $x \in X$, if one sets $y = f(x)$, then $\mathcal{O}_{x}$ is a flat $\mathcal{O}_{y}$-module and the
property $\mathbf{Q}(\mathcal{O}_{x} \otimes_{\mathcal{O}_{y}} \mathit{k}(y), \mathit{k}(y))$ is true.*

*c) For every $x \in X$, if one sets $y = f(x)$, the morphism $\operatorname{Spec}(\mathcal{O}_{x}) \to
\operatorname{Spec}(\mathcal{O}_{y})$ corresponding to the homomorphism $\mathcal{O}_{y} \to \mathcal{O}_{x}$ is a
𝐏-morphism.*

*c') For every closed point $x \in X$, the morphism $\operatorname{Spec}(\mathcal{O}_{x}) \to
\operatorname{Spec}(\mathcal{O}_{y})$ is a 𝐏-morphism.*

The equivalence of a) and b) results indeed from the definitions; the same is so of the equivalence of b) and c), taking
into account `(I, 2.4.2)`; finally the equivalence of b) and c') results from the fact that for every $x \in X$,
$\overline{x}$ contains a closed point `(5.1.11)`.

**Corollary (7.3.3).**

<!-- label: IV.7.3.3 -->

*Let $A$, $B$ be two Noetherian rings, $\phi : A \to B$ a homomorphism such that the corresponding morphism
$\operatorname{Spec}(B) \to \operatorname{Spec}(A)$ is a 𝐏-morphism. Then, for every multiplicative part $S$ of $A$, the
morphism $\operatorname{Spec}(S^{-1}B) \to \operatorname{Spec}(S^{-1}A)$ is a 𝐏-morphism.*

This results at once from `(7.3.2)` and from `(I, 1.6.2)`.

**(7.3.4)** We shall always suppose in what follows that the property $\mathbf{Q}$ is such that the three following
conditions are satisfied:

`(P_I)` (*transitivity*). — If $f : X \to Y$ is a regular morphism `(6.8.1)` and $g : Y \to Z$ a 𝐏-morphism, then $g
\circ f$ is a 𝐏-morphism.

`(P_II)` (*descent*). — If $f : X \to Y$ and $g : Y \to Z$ are morphisms of locally Noetherian preschemes such that $f$
is faithfully flat and $g \circ f$ is a 𝐏-morphism, then $g$ is a 𝐏-morphism.

$(P_{III})$. — For every field $k$, the property $\mathbf{P}(\operatorname{Spec}(k), k)$ is true.

**Remarks (7.3.5).**

<!-- label: IV.7.3.5 -->

*(i) Conditions `(P_I)` and $(P_{III})$ entail that every regular morphism is a 𝐏-morphism.*

*(ii) Note that the hypotheses of `(P_I)` (resp. `(P_II)`) entail that $h = g \circ f$ is flat (resp. $g$ is flat)
`(2.2.13)`; the hypotheses of `(P_I)` or of `(P_II)` moreover entail that for every $z \in Z$, $f_{z} : h^{-1}(z) \to
g^{-1}(z)$ is flat `(2.1.4)`; since, for every $y \in g^{-1}(z)$, $f^{-1}_{z}(y)$ is isomorphic to $f^{-1}(y)$
`(I, 3.6.4)`, this shows that it suffices, to verify conditions `(P_I)` and `(P_II)`, to do so only when $Z$ is the
*spectrum of a field*.*

*(iii) In certain cases, the property $\mathbf{Q}$ will be such that the following condition is satisfied:*

$(P'_{I})$. — *If $f : X \to Y$ and $g : Y \to Z$ are two 𝐏-morphisms, then $g \circ f$ is a 𝐏-morphism.*

<!-- original page 194 -->

**(7.3.6)** We shall say that the property $\mathbf{P}$ is *geometric* if it satisfies (besides `(P_I)`, `(P_II)` and
$(P_{III})$) the condition:

`(P_IV)` (*finite-type extension of the base field*). — If $\mathbf{P}(Z, k)$ is true, then, for every extension $k'$ of
finite type of $k$, $\mathbf{P}(Z \otimes_{k} k', k')$ is true.

**Lemma (7.3.7).**

<!-- label: IV.7.3.7 -->

*Let $f : X \to Y$ be a 𝐏-morphism of locally Noetherian preschemes, $g : Y' \to Y$ a locally finite-type morphism.
Then, if $\mathbf{P}$ satisfies condition `(P_IV)`, the morphism $f' = f_{(Y')} : X \times_{Y} Y' \to Y'$ is a
𝐏-morphism.*

Indeed, for every $y' \in Y'$, if one sets $y = g(y')$, $\mathit{k}(y')$ is an extension of finite type of
$\mathit{k}(y)$ `(I, 6.4.11)` and $f'^{-1}(y') = f^{-1}(y) \otimes_{\mathit{k}(y)} \mathit{k}(y')$ `(I, 3.6.4)`; it then
suffices to apply `(P_IV)`.

**Examples (7.3.8).**

<!-- label: IV.7.3.8 -->

*The following properties $\mathbf{P}(Z, k)$ satisfy conditions `(P_I)`, `(P_II)` and $(P_{III})$:*

*(i) (also denoted $(i_{n})$) $Z$ is of codepth $\leq n$.*

*(ii) $Z$ is a Cohen-Macaulay prescheme.*

*(iii) (also denoted $(iii_{n})$) $Z$ satisfies $(S_{n})$.*

*(iv) $Z$ is regular.*

*(v) (also denoted $(v_{n})$) $Z$ satisfies $(R_{n})$.*

*(vi) $Z$ is reduced.*

*(vii) $Z$ is normal.*

For properties (ii) to (vii), this results from `(6.6.1)`, which in fact proves the stronger condition $(P'_{I})$. For
(i), property `(P_II)` results from `(6.6.2)`; property `(P_I)` results, by the same reasoning as in `(6.6.1, (i))`,
from `(6.3.2)` and from the fact that a regular prescheme is of codepth `0`.

In addition, it results from `(6.7.8)` that properties (i), (ii) and (iii) are *geometric*; by virtue of `(6.7.8)`, the
same is so of the following:

*(iv') $Z$ is geometrically regular.*

*(v') (also denoted $(v'_{n})$) $Z$ has the property $(R_{n})$ geometrically.*

*(vi') $Z$ is geometrically reduced.*

*(vii') $Z$ is geometrically normal.*

**Remarks (7.3.9).**

<!-- label: IV.7.3.9 -->

*(i) Each of the properties (iv'), (v'\_n), (vi'), (vii') entails respectively the corresponding property (iv), (v_n),
(vi), (vii). Property (iv) implies all the properties (i) to (vii), and property (iv') implies all the properties listed
in `(7.3.8)`. Recall also that $(i_{0})$ is equivalent to (ii); the conjunction of $(iii_{1})$ and $(v_{0})$ (resp. of
$(iii_{1})$ and $(v'_{0})$) is equivalent to (vi) (resp. (vi')) `(5.8.5)`; finally the conjunction of $(iii_{2})$ and
$(v_{1})$ (resp. $(iii_{2})$ and $(v'_{1})$) is equivalent to (vii) (resp. (vii')) `(5.8.6)`.*

*(ii) In all the examples of `(7.3.8)`, the property $\mathbf{Q}(\mathcal{O}_{z}, k)$ which serves to define
$\mathbf{P}$ is such that, for every generization $z'$ of $z$ in $Z$, $\mathbf{Q}(\mathcal{O}_{z}, k)$ entails
$\mathbf{Q}(\mathcal{O}_{z'}, k)$: by virtue of `(2.3.4)`, it suffices to verify it for the properties (i) to (vii) (and
even (i) to (v) by remark `(7.3.9, (i))`): now this is included in the definition for (iii) and (v) (`(5.7.2)` and
`(5.8.2)`), it results from `(6.3.9)` for (i), and finally from `(0, 16.5.10)` and `(17.3.2)` for (ii) and (iv).*

<!-- original page 195 -->

**(7.3.10)** We shall say that a property $\mathbf{P}(Z, k)$ is *of the first type* if the property $\mathbf{Q}(A, k)$
which serves to define $\mathbf{P}$ is a property $\mathbf{R}(A)$ not involving $k$ and true when $A$ is a *field*; we
shall say that $\mathbf{P}(Z, k)$ is *of the second type* if the property $\mathbf{Q}(A, k)$ is of the form

«for every extension $k'$ of finite type of $k$ and every point $z'$ of $\operatorname{Spec}(A \otimes_{k} k')$ lying
over the closed point of $\operatorname{Spec}(A)$, one has $\mathbf{R}(\mathcal{O}_{z'})$»

where $\mathbf{R}(A)$ is again assumed to be true when $A$ is a *field*. It is clear that in the examples of `(7.3.8)`,
properties (i) to (vii) are of the first type, properties (iv') to (vii') of the second type.

This being so, if one resumes the reasoning of `(6.6.1)` and `(6.8.3)`, one finds that when $\mathbf{P}$ is of the first
or second type for a property $\mathbf{R}(A)$, *conditions `(P_I)` and `(P_II)` are consequences of the following
conditions on $\mathbf{R}$:*

`(R_I)` Let $X$, $Y$ be two locally Noetherian preschemes, $f : X \to Y$ a regular morphism; then, for every $x \in X$,
the property $\mathbf{R}(\mathcal{O}_{f(x)})$ implies the property $\mathbf{R}(\mathcal{O}_{x})$.

`(R_II)` Let $\phi : A \to B$ be a local homomorphism of local Noetherian rings making $B$ an $A$-module *flat*; then
$\mathbf{R}(B)$ implies $\mathbf{R}(A)$.

Moreover, property $(P_{III})$ results by hypothesis from the fact that $\mathbf{R}(k)$ is true for every field $k$;
finally, when $\mathbf{P}$ is of the second type, condition `(P_IV)` is a consequence of the definition of $\mathbf{P}$
and of the transitivity of extensions of finite type.

**Remark (7.3.11).**

<!-- label: IV.7.3.11 -->

*We leave to the reader the task of formulating the property $\mathbf{R}$ corresponding to each of the examples of
`(7.3.8)`, and of verifying conditions `(R_I)` and `(R_II)` in each case, using the results of §6. In fact, except for
example (i) of `(7.3.8)`, the property $\mathbf{R}$ satisfies in the other cases the following condition:*

$(R'_{I})$ Let $X$, $Y$ be two locally Noetherian preschemes, $f : X \to Y$ a 𝐏-morphism (for the property $\mathbf{P}$
of the first or second type defined from $\mathbf{R}$); then, for every $x \in X$, the property
$\mathbf{R}(\mathcal{O}_{f(x)})$ implies the property $\mathbf{R}(\mathcal{O}_{x})$.

The reasonings of `(6.6.1)` and `(6.8.3)` prove that when $\mathbf{R}$ satisfies conditions $(R'_{I})$ and `(R_II)`,
then $\mathbf{P}$ satisfies conditions $(P'_{I})$ `(7.3.4, (iii))` and `(P_II)`.

**Proposition (7.3.12).**

<!-- label: IV.7.3.12 -->

*Let $\mathbf{P}$ be a property of the first or second type defined from a property $\mathbf{R}$ satisfying conditions
`(R_I)` and `(R_II)` (resp. $(R'_{I})$ and `(R_II)`). If for every locally Noetherian prescheme $X$, $U_{\mathbf{R}}(X)$
designates the set of $x \in X$ such that $\mathbf{R}(\mathcal{O}_{x})$ is true, then, for every regular morphism (resp.
every 𝐏-morphism) $f : X \to Y$ of locally Noetherian preschemes, one has*

$$ (7.3.12.1) U_{\mathbf{R}}(X) = f^{-1}(U_{\mathbf{R}}(Y)). $$

It is an immediate consequence of the definitions.

**(7.3.13)** Given a semi-local Noetherian ring $A$, we shall call **formal fibres** of $A$ the fibres of the canonical
morphism $f : \operatorname{Spec}(\hat{A}) \to \operatorname{Spec}(A)$; for every prime ideal $p$ of $A$, the formal
fibre at $p$ is therefore the scheme $\operatorname{Spec}(\hat{A} \otimes_{A} \mathit{k}(p))$; since the completion of
the local ring $A/p$ is $\hat{A}/p\hat{A} = (A/p) \otimes_{A} \hat{A}$, one sees that the formal fibre of $A$ at $p$ is
also *the formal fibre of $A/p$ at the generic point `(0)` of $\operatorname{Spec}(A/p)$*.

<!-- original page 196 -->

The property $\mathbf{P}$ being defined as in `(7.3.1)`, we shall say that *the formal fibres of $A$ have the property
$\mathbf{P}$*, or that *$A$ is a $\mathbf{P}$-ring*, if, for every $x \in \operatorname{Spec}(A)$,
$\mathbf{P}(f^{-1}(x), \mathit{k}(x))$ is true. Since $f$ is flat, it amounts to the same to say that $f$ is a
𝐏-morphism.

**Proposition (7.3.14).**

<!-- label: IV.7.3.14 -->

*Let $A$ be a semi-local Noetherian ring, $\mathfrak{m}_{i}$ $(1 \leq i \leq r)$ its maximal ideals, and set $A_{i} =
A_{\mathfrak{m}_{i}}$; in order that $A$ be a $\mathbf{P}$-ring, it is necessary and sufficient that each of the $A_{i}$
be so.*

Indeed, `Â` is the direct product of the $\hat{A}_{i}$, hence the formal fibre of $A$ at a point $x \in
\operatorname{Spec}(A)$ is the sum of the formal fibres at $x$ of those of the $A_{i}$ such that $x \in
\operatorname{Spec}(A_{i})$.

**Proposition (7.3.15).**

<!-- label: IV.7.3.15 -->

*Let $A$ be a semi-local Noetherian ring.*

*(i) If $A$ is a $\mathbf{P}$-ring, every quotient ring of $A$ is a $\mathbf{P}$-ring.*

*(ii) If moreover $\mathbf{P}$ satisfies condition `(P_IV)` `(7.3.6)`, then every finite $A$-algebra is a
$\mathbf{P}$-ring.*

For every ideal $\mathfrak{a}$ of $A$, $\hat{A} \otimes_{A} (A/\mathfrak{a})$ is the completion of $A/\mathfrak{a}$, and
the formal fibres of $A/\mathfrak{a}$ are the formal fibres of $A$ at the points of $V(\mathfrak{a})$, whence (i). On
the other hand, if $B$ is a finite $A$-algebra, hence a semi-local ring, one has $\hat{B} = B \otimes_{A} \hat{A}$, and
(ii) follows from `(7.3.7)`.

**Proposition (7.3.16).**

<!-- label: IV.7.3.16 -->

*Suppose that the property $\mathbf{P}$ is of the first (resp. second) type, defined from a property $\mathbf{R}$
`(7.3.10)`. When $\mathbf{P}$ is of the second type, suppose moreover that the relation*

«for every finite extension $k'$ of $k$, and every $z' \in Z \otimes_{k} k'$, $\mathbf{R}(\mathcal{O}_{z'})$ is true»

*entails $\mathbf{P}(Z, k)$ (which is verified for examples (iv') to (vii') of `(7.3.8)`, by virtue of `(6.7.7)` and
`(4.6.1)`).*

*Let $A$ be a semi-local Noetherian ring. If the property $\mathbf{R}$ satisfies `(R_I)` and `(R_II)`, the following
properties are equivalent:*

*a) $A$ is a $\mathbf{P}$-ring.*

*b) For every integral quotient ring $B$ of $A$ (resp. every integral finite $A$-algebra $B$) and every prime ideal $q$
of $\hat{B}$ whose inverse image in $B$ is `0`, $\mathbf{R}(\hat{B}_{q})$ is true.*

*If moreover $\mathbf{R}$ satisfies condition $(R'_{I})$, properties a) and b) are also equivalent to:*

*c) For every integral quotient ring $B$ of $A$ (resp. every integral finite $A$-algebra $B$), if one sets $Y =
\operatorname{Spec}(B)$, $Y' = \operatorname{Spec}(\hat{B})$, and if $g : Y' \to Y$ is the canonical morphism, one has
(with the notations of `(7.3.12)`)*

$$ (7.3.16.1) U_{\mathbf{R}}(Y') = g^{-1}(U_{\mathbf{R}}(Y)). $$

The equivalence of a) and b) is immediate when $\mathbf{P}$ is of the first type: indeed, for every prime ideal $p$ of
$A$, one has seen that the formal fibre of $B = A/p$ at the generic point `(0)` of $\operatorname{Spec}(B)$ is none
other than the formal fibre of $A$ at the point $p \in \operatorname{Spec}(A)$ `(7.3.13)`.

When $\mathbf{P}$ is of the second type, the equivalence of a) and b) results from the following more general lemma:

**Lemma (7.3.16.2).**

<!-- label: IV.7.3.16.2 -->

*Let $A$, $A'$ be two rings, $\phi : A \to A'$ a homomorphism, $f : \operatorname{Spec}(A') \to \operatorname{Spec}(A)$
the corresponding morphism. In order that for every $x \in \operatorname{Spec}(A)$, every*

<!-- original page 197 -->

*finite extension $k$ of $\mathit{k}(x)$ and every point $z$ of $f^{-1}(x) \otimes_{\mathit{k}(x)} k = Z$, the property
$\mathbf{R}(\mathcal{O}_{Z, z})$ be true, it is necessary and sufficient that the following condition be satisfied: for
every finite integral $A$-algebra $B$, if $g : \operatorname{Spec}(A' \otimes_{A} B) \to \operatorname{Spec}(B)$ is the
morphism deduced from $f$ by extension to $B$ of the base ring, and if $T = g^{-1}(\xi)$ is the fibre of the generic
point $\xi$ of $\operatorname{Spec}(B)$, then, for every $t \in T$, $\mathbf{R}(\mathcal{O}_{T, t})$ is true.*

The condition is trivially necessary since if $x$ is the point of $\operatorname{Spec}(A)$ over which $\xi$ lies,
$\mathit{k}(\xi)$ is a finite extension of $\mathit{k}(x)$. Conversely, consider an arbitrary point $x \in
\operatorname{Spec}(A)$ and let $k$ be a finite extension of $\mathit{k}(x)$. Setting $p = j_{x}$, $\mathit{k}(x)$ is
the field of fractions of $A/p$, and there is a base $k$ of $k$ over $\mathit{k}(x)$ formed of elements integral over
$A/p$; if $B$ is the subring of $k$ generated by these elements, $B$ is an integral finite $A$-algebra and $k$ is the
field $\mathit{k}(\xi)$ at the generic point $\xi$ of $\operatorname{Spec}(B)$; since $x$ is the image of $\xi$ in
$\operatorname{Spec}(A)$, the fibre $g^{-1}(\xi)$ is none other than $f^{-1}(x) \otimes_{\mathit{k}(x)} k$, which
finishes proving the lemma.

The fact that a) implies c) is an immediate consequence of `(7.3.15)` and `(7.3.12)`. On the other hand, let us
specialize c) to the case where $B$ is integral, and if $y$ denotes the generic point of $Y = \operatorname{Spec}(B)$,
one has $\mathcal{O}_{Y, y} = \mathit{k}(y)$, hence $y \in U_{\mathbf{R}}(Y)$, since $\mathbf{R}(k)$ is true for every
field $k$; expressing that every point $y' \in g^{-1}(y)$ belongs to $U_{\mathbf{R}}(Y')$, one obtains the statement,
hence c) implies b). Q.E.D.

**Proposition (7.3.17).**

<!-- label: IV.7.3.17 -->

*Suppose that the property $\mathbf{R}$ satisfies conditions $(R'_{I})$ and `(R_II)` and that $\mathbf{P}$ is the
property of the first (resp. second) type defined from $\mathbf{R}$ `(7.3.10)`. Then, if $A$ is a $\mathbf{P}$-ring, the
properties $\mathbf{R}(A)$ and $\mathbf{R}(\hat{A})$ are equivalent.*

This results from `(7.3.12.1)` applied to $Y = \operatorname{Spec}(A)$ and $X = \operatorname{Spec}(\hat{A})$.

**Proposition (7.3.18).**

<!-- label: IV.7.3.18 -->

*Suppose that $\mathbf{P}$ is a property of the first (resp. second) type defined from a property $\mathbf{R}$
satisfying conditions $(R'_{I})$ and `(R_II)` as well as the following condition:*

$(R_{III})$ *For every complete Noetherian local ring $C$, if one sets $Z = \operatorname{Spec}(C)$, the set
$U_{\mathbf{R}}(Z)$ `(7.3.12)` is open in $Z$.*

*Then, if $A$ is a $\mathbf{P}$-ring and if one sets $X = \operatorname{Spec}(A)$, the set $U_{\mathbf{R}}(X)$ is open
in $X$.*

Indeed, if $X' = \operatorname{Spec}(\hat{A})$ and if $f : X' \to X$ is the canonical morphism, one has
$U_{\mathbf{R}}(X') = f^{-1}(U_{\mathbf{R}}(X))$ `(7.3.12)`. Since $f$ is faithfully flat and quasi-compact and by
hypothesis $U_{\mathbf{R}}(X')$ is open in $X'$, the conclusion follows from `(2.3.12)`.

**Remarks (7.3.19).**

<!-- label: IV.7.3.19 -->

*(i) The property $\mathbf{R}$ which serves to define $\mathbf{P}$ satisfies condition $(R_{III})$ in all the examples
enumerated in `(7.3.8)`. For (i), (ii) and (iii), this results from `(6.11.2)` and from Cohen's theorem `(0, 19.8.8)`;
when $\mathbf{P}$ is one of the properties (iv), (iv'), (v), (v'), this follows from `(6.12.7)` and `(6.12.9)`, and when
$\mathbf{P}$ is one of the properties (vii), (vii'), from `(6.12.7)` and `(6.13.4)`; finally, for (vi) and (vi') the
assertion of `(7.3.18)` is trivial, being true for every locally Noetherian prescheme.*

<!-- original page 198 -->

*(ii) We have already pointed out `(6.4.3)` that when $\mathbf{P}$ is one of the properties (ii) or $(iii_{1})$ of
`(7.3.8)`, we are unaware whether every Noetherian local ring is a $\mathbf{P}$-ring; recall however that when $A$ is a
ring quotient of a Cohen-Macaulay ring, the formal fibres of $A$ are Cohen-Macaulay schemes `(6.3.8)`.*

*(iii) The most interesting case of the notion of $\mathbf{P}$-ring is that corresponding to the strongest property
(iv') of `(7.3.8)`, that is to say the rings whose formal fibres are geometrically regular. Fields, and more generally
complete Noetherian local rings, trivially satisfy this property.*

*(iv) Let $A$ be a Noetherian local ring of dimension `1`; $\operatorname{Spec}(A)$ is then formed of the closed point
$a$, corresponding to the maximal ideal $\mathfrak{m}$, and of the maximal points $b_{i}$ $(1 \leq i \leq r)$
corresponding to the minimal prime ideals of $A$. One has $\dim(\hat{A}) = 1$ and the maximal ideal of `Â` is
$\mathfrak{m}\hat{A}$; the formal fibre of $A$ at the point $a$ is therefore $\operatorname{Spec}(k)$, where $k =
A/\mathfrak{m}$ is the residue field of $A$; the formal fibre at each of the $b_{i}$ is the spectrum of an Artinian ring
whose residue fields are the residue fields $L_{ij}$ of $\operatorname{Spec}(\hat{A})$ at the maximal points $b_{ij}$
lying over $b_{i}$. Since an Artinian ring is a Cohen-Macaulay ring, one sees that $A$ is a $\mathbf{P}$-ring when
$\mathbf{P}$ is property (ii) of `(7.3.8)`. In addition, since a reduced Artinian ring is a direct sum of fields, the
following properties are equivalent `(6.7.7)`:*

*a) the formal fibres of $A$ are geometrically reduced;*

*b) the formal fibres of $A$ are geometrically normal;*

*c) the formal fibres of $A$ are geometrically regular;*

*moreover, when $A$ is reduced, they are also equivalent to:*

*d) `Â` is reduced and $L_{ij}$ is a separable extension of $K_{i}$ for every pair $(i, j)$ `(4.6.1)`.*

*In particular, if $A$ is a discrete valuation ring, $K$ its field of fractions, and if $\hat{K}$ is the completion of
$K$ for the valuation corresponding to $A$ (the field of fractions of `Â`), in order that the formal fibres of $A$ be
geometrically regular, it is necessary and sufficient that $\hat{K}$ be a separable extension of $K$. This will always
be the case when $K$ is of characteristic `0`.*

### 7.4. Permanence of properties of formal fibres

**(7.4.1)** In the whole of this number, we suppose that the property $\mathbf{P}$ is of the form defined in `(7.3.1)`,
and satisfies conditions `(P_I)`, `(P_II)` and $(P_{III})$ of `(7.3.4)`. We suppose moreover that the property
$\mathbf{Q}$ which serves to define $\mathbf{P}$ is such that, for every generization $z'$ of $z$ in $Z$,
$\mathbf{Q}(\mathcal{O}_{z}, k)$ entails $\mathbf{Q}(\mathcal{O}_{z'}, k)$.

**Lemma (7.4.2).**

<!-- label: IV.7.4.2 -->

*Let $A$, $A'$ be Noetherian local rings, $\phi : A \to A'$ a local homomorphism such that $f = {}^{a}\phi :
\operatorname{Spec}(A') \to \operatorname{Spec}(A)$ is a 𝐏-morphism. Then, if the formal fibres of $A'$ are
geometrically regular, $A$ is a $\mathbf{P}$-ring.*

<!-- original page 199 -->

Consider the completed homomorphism $\hat{\phi} : \hat{A} \to \hat{A}'$ and the corresponding morphism $\hat{f} =
{}^{a}\hat{\phi}$; one has the commutative diagram

$$ \operatorname{Spec}(\hat{A}) \leftarrow^{\hat{f}} \operatorname{Spec}(\hat{A}') \downarrow g \downarrow g'
\operatorname{Spec}(A) \leftarrow^{f} \operatorname{Spec}(A') $$

where $g$ and $g'$ are the canonical morphisms. Since by hypothesis $f$ is a 𝐏-morphism and $g'$ a regular morphism, it
results from `(P_I)` that $f \circ g' = g \circ \hat{f}$ is a 𝐏-morphism. On the other hand, the hypothesis that $f$ is
a 𝐏-morphism implies that $f$ is flat, hence the same is so of $\hat{f}$ (Bourbaki, *Alg. comm.*, chap. III, §5, n° 4,
cor. of prop. 3), which is moreover a local homomorphism, hence faithfully flat $(0_{I}, 6.6.2)$; it then results from
`(P_II)` that $g$ is a 𝐏-morphism.

**Corollary (7.4.3).**

<!-- label: IV.7.4.3 -->

*(i) Let $A$ be a Noetherian local $\mathbf{P}$-ring, $A' = \hat{A}$ its completion. Suppose that for every prime ideal
$p'$ of $A'$, the formal fibres of $A'_{p'}$ are geometrically regular; then, for every prime ideal $p$ of $A$, $A_{p}$
is a $\mathbf{P}$-ring.*

*(ii) Suppose that $\mathbf{P}$ verifies condition `(P_IV)` `(7.3.6)`. Let $A$ be a Noetherian local $\mathbf{P}$-ring,
$B$ an $A$-algebra essentially of finite type that is local, and such that the homomorphism $A \to B$ is local. Set $A'
= \hat{A}$, and let $\mathfrak{n}'$ be the unique prime ideal of $B' = B \otimes_{A} A'$ lying over the maximal ideal of
$B$ and over the maximal ideal of $A'$. If the formal fibres of $B'_{\mathfrak{n}'}$ are geometrically regular, then $B$
is a $\mathbf{P}$-ring.*

(i) Since by hypothesis $\operatorname{Spec}(A') \to \operatorname{Spec}(A)$ is a 𝐏-morphism, the same is so of
$\operatorname{Spec}(A'_{p}) \to \operatorname{Spec}(A_{p})$ by virtue of `(7.3.2, b))`, for every prime ideal $p$ of
$A$ and every prime ideal $p'$ of $A'$ lying over $p$. It then suffices to apply lemma `(7.4.2)` to this morphism,
noting that the morphism $\operatorname{Spec}(A') \to \operatorname{Spec}(A)$ is surjective.

(ii) By virtue of `(7.4.2)`, it suffices to prove that the morphism $\operatorname{Spec}(B'_{\mathfrak{n}'}) \to
\operatorname{Spec}(B)$ is a 𝐏-morphism. Now one has $B = C_{\mathfrak{n}}$, where $C$ is an $A$-algebra of finite type
and $\mathfrak{n}$ a prime ideal of $C$ lying over the maximal ideal of $A$. If one sets $C' = C \otimes_{A} A'$, it
results from the hypotheses and from `(7.3.7)` that $\operatorname{Spec}(C') \to \operatorname{Spec}(C)$ is a
𝐏-morphism; since $B'_{\mathfrak{n}'}$ is a local ring of $C'$ at a prime ideal of $C'$ lying over $\mathfrak{n}$, the
conclusion results from `(7.3.2, b))`.

**Theorem (7.4.4).**

<!-- label: IV.7.4.4 -->

*The hypotheses on $\mathbf{P}$ being those of `(7.4.1)`, let $A$ be a Noetherian local $\mathbf{P}$-ring.*

*(i) For every prime ideal $p$ of $A$, $A_{p}$ is a $\mathbf{P}$-ring.*

*(ii) Suppose moreover that $\mathbf{P}$ verifies condition `(P_IV)`. Then every local ring which is an $A$-algebra
essentially of finite type is a $\mathbf{P}$-ring.*

(i) Applying `(7.4.3, (i))`, the whole question is to see that for every prime ideal $p'$ of $A' = \hat{A}$, $A'_{p'}$
has geometrically regular formal fibres. Now, this has been proved in `(0, 22.3.3` and `22.5.8)`.

<!-- original page 200 -->

(ii) Let $B$ be an $A$-algebra essentially of finite type that is a local ring; if $p$ is the prime ideal of $A$ over
which the maximal ideal of $B$ lies, $B$ is also an $A_{p}$-algebra essentially of finite type `(1.3.8)`; by virtue of
(i), one may therefore suppose that $p$ is the maximal ideal $\mathfrak{m}$ of $A$. One has then $B = C_{q}$, where $C$
is an $A$-algebra of finite type, $q$ a prime ideal of $C$ lying over $\mathfrak{m}$; let $\mathfrak{n} \supset q$ be a
maximal ideal of $C$ (necessarily lying over $\mathfrak{m}$); if one sets $k = A/\mathfrak{m}$, $C/\mathfrak{m}C$ is a
$k$-algebra of finite type, hence the residue field $k'$ of $C$ at the maximal ideal $\mathfrak{n}$ is finite over $k$
`(I, 6.4.2)`; by virtue of (i), it will suffice to prove that $C_{\mathfrak{n}}$ is a $\mathbf{P}$-ring, since $C_{q}$
is a local ring of $C_{\mathfrak{n}}$ at a prime ideal of $C_{\mathfrak{n}}$. One is thus reduced to proving the

**Lemma (7.4.4.1).**

<!-- label: IV.7.4.4.1 -->

*Let $A$ be a Noetherian local $\mathbf{P}$-ring, $k$ its residue field, $C$ an $A$-algebra of finite type, $B$ a local
ring at a prime ideal $\mathfrak{n}$ of $C$, such that: 1° the homomorphism $A \to B$ is local; 2° the residue field
$k'$ of $B$ is a finite extension of $k$. If $\mathbf{P}$ satisfies `(P_IV)`, $B$ is a $\mathbf{P}$-ring.*

Let $(x_{i})_{1 \leq i \leq m}$ be a system of generators of the $A$-algebra $C$; let us show first that one may reason
by induction on $m$. Let $C'$ be the subalgebra of $C$ generated by $x_{1}, \cdots, x_{m-1}$, and let $\mathfrak{n}' =
\mathfrak{n} \cap C'$. The homomorphism $A \to C_{\mathfrak{n}}$ factors into $A \to C'_{\mathfrak{n}'} \to
C_{\mathfrak{n}}$, and it is clear that $A \to C'_{\mathfrak{n}'}$ and $C'_{\mathfrak{n}'} \to C_{\mathfrak{n}}$ are
local homomorphisms; if `k''` is the residue field of $C'_{\mathfrak{n}'}$, $k \to k''$ factors likewise into $k \to k''
\to k'$, hence `k''` is a finite extension of $k$ and $k'$ an extension of `k''`. The induction hypothesis entails that
$C'_{\mathfrak{n}'}$ is a $\mathbf{P}$-ring; moreover, if $S' = C' - \mathfrak{n}'$, $C_{\mathfrak{n}}$ is a local ring
of $S'^{-1} C$; as $C = C'[x_{m}]$, one has $S'^{-1} C = C'_{\mathfrak{n}'}[x_{m} / 1]$ and the induction hypothesis
again shows that $C_{\mathfrak{n}}$ is a $\mathbf{P}$-ring. One is thus reduced to the case where $C$ is an $A$-algebra
generated by a *single* element $t$.

Let us apply `(7.4.3, (ii))`; setting $A' = \hat{A}$, $B' = B \otimes_{A} A'$ is a local ring of $C \otimes_{A} A'$ at a
prime ideal lying over $\mathfrak{n}$; since $A$ and $A'$ have the same residue field $k$, the residue field of $C
\otimes_{A} A'$ at this prime ideal is equal to $k'$. Moreover $C \otimes_{A} A'$ is an $A'$-algebra generated by a
single element. It results then from `(7.4.3, (ii))` that one may reduce to proving `(7.4.4.1)` when $\mathbf{P}$ is
property (iv') of `(7.3.8)`, that $A$ is *complete* and $C$ generated by a single element $t$.

To show that the formal fibres of $B = C_{\mathfrak{n}}$ are then geometrically regular, let us apply criterion
`(7.3.16, b))`. Let `B_1` be an integral finite $B$-algebra, hence generated by a finite number of elements integral
over $B$. By multiplying these elements by an element of $S = C - \mathfrak{n}$, one may suppose they are integral over
$C$, and one may then write $B_{1} = S^{-1} C_{1}$, where `C_1` is a sub-$C$-algebra of `B_1` generated by a finite
number of elements integral over $C$, hence a *finite and integral* $C$-algebra. On the other hand, `B_1` is a
semi-local ring, and every local ring `B_2` of `B_1` at a maximal ideal is a local ring of `C_1` at a prime ideal, such
that $A \to B_{2}$ is a local homomorphism; moreover, the residue field of `B_2` is a finite extension of $k'$, hence of
$k$. One sees therefore (taking into account `(7.3.14)` and (i)) that one is reduced to the following question: let $C$
be an integral Noetherian ring, containing a subring `C_0` which is an $A$-algebra generated by a single element $t$ and
such that $C$ is a *finite* `C_0`-algebra; if $\mathfrak{n}$ is a maximal ideal of $C$

<!-- original page 201 -->

lying over the maximal ideal of $A$, and $B = C_{\mathfrak{n}}$, the question is to show that for every prime ideal $q$
of $\hat{B}$ whose inverse image in $B$ is `0`, the ring $\hat{B}_{q}$ is *regular*. One may moreover replace $A$ by its
image in $C$, which is a complete local ring (as a quotient of $A$) and integral. The conclusion to prove is then a
consequence of the following more general lemma:

**Lemma (7.4.4.2).**

<!-- label: IV.7.4.4.2 -->

*Let $A$ be a Noetherian local integral and complete ring, $k$ its residue field, $C$ an integral ring containing $A$,
such that there exists $t \in C$ for which $C$ is a finite `A[t]`-algebra. Let $\mathfrak{n}$ be a maximal ideal of $C$
lying over the maximal ideal $\mathfrak{m}$ of $A$; set $B = C_{\mathfrak{n}}$, $X = \operatorname{Spec}(B)$, $B' =
\hat{B}$, $X' = \operatorname{Spec}(\hat{B})$; if $U = Reg(X)$, $U' = Reg(X')$, and if $f : X' \to X$ is the canonical
morphism, one then has $f^{-1}(U) \subset U'$.*

The assertion to prove to obtain `(7.4.4.1)` will follow from this lemma observing that, since $B$ is integral, the
generic point of $X$ belongs to $U$.

One will note that since $C$ is an $A$-algebra of finite type, and $\mathfrak{n}$ a maximal ideal of $C$, the residue
field $k'$ of $C_{\mathfrak{n}} = B$ (hence also of $B'$) is a *finite* extension of $k$ (`(I, 6.4.11)` and `(6.4.2)`).

If one sets $Y = \operatorname{Spec}(C)$, it results from `(6.12.8)` that $Reg(Y)$ is open in $Y$; since the local rings
of $X$ are local rings of $Y$ `(I, 2.4.2)`, one has $U = X \cap Reg(Y)$, hence $U$ is open in $X$; on the other hand
`(6.12.7)` $U'$ is open in $X'$, hence $S' = X' - U'$ is closed; consequently $S' \cap f^{-1}(U)$ is locally closed in
$X'$, and the whole question is to prove that this set is empty. One knows `(5.1.10)` that in the contrary case, there
would exist a prime ideal $p'$ of $S' \cap f^{-1}(U)$ such that $\dim(B'/p') \leq 1$. Let us remark first that $p'$
cannot be the maximal ideal $\mathfrak{m}B'$ of $B'$, where $\mathfrak{m}$ is the maximal ideal of $B$. Indeed, this
would signify that $B = B_{\mathfrak{m}}$ is regular, hence also $B' = \hat{B}$ `(0, 17.1.5)`, and one would have by
hypothesis $\mathfrak{m}B' \in U'$ contrary to the hypothesis. One must therefore have $\dim(B'/p') = 1$. Set $p = B
\cap p'$; by hypothesis $B_{p}$ is regular, but $B'_{p'}$ is not so; since $B'_{p'}$ is a flat $B_{p}$-module, it
results from `(6.5.2)` that the fibre $Z$ of $f$ at the point $p$ is not regular at the point $p'$. Let us show that one
may reduce to the case where $p = 0$. Indeed, in the general case, if one sets $q = p \cap C$, $r = p \cap A$, $C/q$ is
an $(A/r)[\bar{t}]$-algebra finite (where $\bar{t}$ is the class of $t$ mod. $q$); since $p = qB$, $B/p$ equals
$(C/q)_{\mathfrak{n}/q}$, and $\mathfrak{n}/q$ is a maximal ideal of $C/q$ lying over the maximal ideal $\mathfrak{m}/r$
of $A/r$; one sees thus that the hypotheses of `(7.4.4.2)` are still satisfied by $A/r$, $C/q$ and $B/p$, and since the
completion of $B/p$ is $B'/pB'$, this proves our assertion. Suppose therefore that $p = 0$, so that $Z$ is the generic
fibre of $f$ and the homomorphism $B \to B'/p'$ is *injective*. Set $V = B'/p'$, and distinguish two cases:

I) *$V$ is a finite $A$-algebra.* — Since $B \subset V$, $B$ is a fortiori a finite $A$-algebra, and since $A$ is
complete, the same is so of $B$ (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9), whence $B' = B$, $p' =
0$, hence $B'_{p'}$ is a field, and consequently a regular local ring, contrary to the hypothesis.

II) *$V$ is not a finite $A$-algebra.* — Since the local ring $A$ is *complete*, this implies that $V$ is not a
quasi-finite $A$-algebra ($(0_{I}, 7.4.1)$ and `(7.4.2)`); but by hypothesis the residue field $k'$ of $V$ is a *finite*
extension of the residue field $k$ of $A$,

<!-- original page 202 -->

hence $(0_{I}, 7.4.4)$ the ideal $\mathfrak{m}V$ is *not an ideal of definition of $V$*. Since $V$ is an integral
Noetherian local ring of dimension `1`, `0` is the only ideal of $V$ that is not an ideal of definition, hence
$\mathfrak{m}V = 0$. But one has $A \subset V$ and $V$ is integral, whence $\mathfrak{m} = 0$ and $A = k$ is a field.
One deduces from this first of all $\dim(C) \leq 1$ $(0_{I}, 16.1.5)$; but since $\dim(V) = 1$, the relations
`dim(V) ≤ dim(B') = dim(B) ≤ dim(C)` show that this entails `dim(C) = dim(B) = dim(B') = dim(B'/p') = 1`, and
consequently $p'$ is necessarily a *minimal ideal* of $B'$. We shall thus arrive at a contradiction if we prove that
$B'_{p'}$ is a field, or again that the ring $B'$ is reduced. Now, since $C$ is a $k$-algebra of finite type, the
integral closure `C_1` of $C$ is a *finite* $C$-algebra (Bourbaki, *Alg. comm.*, chap. V, §3, n° 2, th. 2); if one sets
$S = C - \mathfrak{n}$, $B_{1} = S^{-1} C_{1}$ is the integral closure of $B$, hence a finite $B$-algebra, and
consequently a semi-local Noetherian, integral and integrally closed ring of dimension `1` `(0, 16.1.5)`; if
$\mathfrak{m}_{j}$ $(1 \leq j \leq h)$ are its maximal ideals, the $(B_{1})_{\mathfrak{m}_{j}}$ are therefore discrete
valuation rings `(II, 7.1.6)`, and the completion $B'_{1}$ of `B_1` is the direct composite of the completed discrete
valuation rings of the $(B_{1})_{\mathfrak{m}_{j}}$ (Bourbaki, *Alg. comm.*, chap. III, §2, n° 13, prop. 18); $B'_{1}$
is therefore reduced, and since the completion $B'$ of $B$ is a subring of $B'_{1}$ (Bourbaki, *Alg. comm.*, chap. IV,
§2, n° 5, cor. 3 of prop. 9), it is also a reduced ring. Q.E.D.

**Corollary (7.4.5).**

<!-- label: IV.7.4.5 -->

*Suppose that the property $\mathbf{P}$ satisfies conditions `(P_I)`, `(P_II)`, $(P_{III})$. Let $A$ be a Noetherian
ring. The following conditions are equivalent:*

*a) For every prime ideal $p$ of $A$, $A_{p}$ is a $\mathbf{P}$-ring.*

*b) For every maximal ideal $\mathfrak{m}$ of $A$, $A_{\mathfrak{m}}$ is a $\mathbf{P}$-ring.*

*If moreover $\mathbf{P}$ satisfies `(P_IV)`, properties a) and b) are also equivalent to:*

*c) For every $A$-algebra of finite type $B$ and every prime ideal $q$ of $B$, $B_{q}$ is a $\mathbf{P}$-ring.*

The equivalence of a) and b) results from `(7.4.4, (i))`, and that of a) and c) from `(7.4.4, (ii))`.

When condition a) of `(7.4.5)` is satisfied, one says that $A$ is a **𝐏-ring**; for semi-local Noetherian rings, this
definition coincides with that of `(7.3.13)`, when conditions `(P_I)`, `(P_II)` and $(P_{III})$ are satisfied. The ring
$Z$ is a 𝐏-ring `(7.3.19, (iv))`; every complete local ring is a 𝐏-ring.

**Proposition (7.4.6).**

<!-- label: IV.7.4.6 -->

*Suppose that the property $\mathbf{P}$ satisfies conditions `(P_I)`, `(P_II)` and $(P_{III})$. Let $A$ be a Noetherian
ring, $\mathfrak{J}$ an ideal of $A$, `Â` the separated completion of $A$ for the $\mathfrak{J}$-preadic topology. Then,
if $A$ is a $\mathbf{P}$-ring `(7.4.5)`, the canonical morphism $\operatorname{Spec}(\hat{A}) \to
\operatorname{Spec}(A)$ is a 𝐏-morphism.*

Using `(7.3.2, c'))`, it suffices to prove that for every maximal ideal $\mathfrak{n}$ of `Â`, of inverse image
$\mathfrak{m}$ in $A$, the morphism $\operatorname{Spec}((\hat{A})_{\mathfrak{n}}) \to
\operatorname{Spec}(A_{\mathfrak{m}})$ is a 𝐏-morphism. One knows (Bourbaki, *Alg. comm.*, chap. III, §3, n° 4, prop. 8)
that the canonical homomorphism $A_{\mathfrak{m}} \to (\hat{A})_{\mathfrak{n}}$ is injective, that the
$\mathfrak{m}A_{\mathfrak{m}}$-preadic topology on $A_{\mathfrak{m}}$ is induced by the
$\mathfrak{n}(\hat{A})_{\mathfrak{n}}$-preadic topology and that $A_{\mathfrak{m}}$ is dense in
$(\hat{A})_{\mathfrak{n}}$, so that the completion of $A_{\mathfrak{m}}$ for the $\mathfrak{m}A_{\mathfrak{m}}$-preadic
topology identifies with that of $(\hat{A})_{\mathfrak{n}}$ for the $\mathfrak{n}(\hat{A})_{\mathfrak{n}}$-preadic
topology. One therefore has two morphisms

```text
       Spec((A_𝔪)^)  →^{f}  Spec((Â)_𝔫)  →^{g}  Spec(A_𝔪)
```

<!-- original page 203 -->

such that $f$ is faithfully flat; since by hypothesis $g \circ f$ is a 𝐏-morphism, the same is so of $g$ by virtue of
`(P_II)`.

**Corollary (7.4.7).**

<!-- label: IV.7.4.7 -->

*Suppose that $\mathbf{P}$ verifies conditions `(P_I)`, $(P'_{I})$, `(P_II)`, $(P_{III})$ and `(P_IV)`. Then, if $A$ is
a $\mathbf{P}$-ring `(7.4.5)`, the canonical morphism $\operatorname{Spec}(A[[T_{1}, \cdots, T_{r}]]) \to
\operatorname{Spec}(A)$ is a 𝐏-morphism. In particular, if moreover $A$ is integral, $K$ its field of fractions, and if
$p$ is a prime ideal of $B = A[[T_{1}, \cdots, T_{r}]]$ such that $p \cap A = 0$, then the property $\mathbf{P}(B_{p},
K)$ is true.*

Indeed, the canonical morphism $\operatorname{Spec}(B) \to \operatorname{Spec}(A)$ factors into

```text
   Spec(A[[T_1, …, T_r]])  →^{f}  Spec(A[T_1, …, T_r])  →^{g}  Spec(A).
```

It is clear that the morphism $g$ is regular `(0, 17.3.7)`; by virtue of `(7.4.5)`, $A[T_{1}, \cdots, T_{r}]$ is a
$\mathbf{P}$-ring, hence it results from `(7.4.6)` that $f$ is a 𝐏-morphism; since $g$ is regular, hence also a
𝐏-morphism `(7.3.5, (i))`, the same is so of $g \circ f$ by virtue of $(P'_{I})$.

One will note that the conclusion is still valid if instead of supposing that $\mathbf{P}$ verifies $(P'_{I})$ and that
every regular morphism is a 𝐏-morphism, one supposes only that a composite morphism $g \circ f$ is a 𝐏-morphism when $g$
is regular and $f$ a 𝐏-morphism (a sort of symmetric condition of $(P'_{I})$).

**Remark (7.4.8).**

<!-- label: IV.7.4.8 -->

*The preceding results pose the following problems:*

*A) Let $A$ be a Zariski ring **complete**, and let $\mathfrak{J}$ be an ideal of definition of $A$; if the ring
$A/\mathfrak{J}$ is a $\mathbf{P}$-ring, is the same so of $A$? It would result from this that for every Noetherian
$\mathbf{P}$-ring $A$ and every ideal $\mathfrak{J}$ of $A$, the separated completion `Â` for the $\mathfrak{J}$-preadic
topology would also be a $\mathbf{P}$-ring.*

*B) Let $k$ be a complete non-discrete valued field; one again calls **ring of restricted formal series** $k{T_{1},
\cdots, T_{n}}$ the subring of the ring of formal series $k[[T_{1}, \cdots, T_{n}]]$ formed of the series whose
coefficients **tend to 0**. Is such a ring a $\mathbf{P}$-ring?*

*C) If $A$ is a linearly topologized $\mathbf{P}$-ring, $S$ a multiplicative part of $A$, are the rings $A{S^{-1}}$
$(0_{I}, 7.6.1)$ and $A_{(S)}$ $(0_{I}, 7.6.15)$ $\mathbf{P}$-rings?*

<!-- original page 203 -->

### 7.5. A criterion for $\mathbf{P}$-morphisms

**(7.5.0)** This number will not be used in the sequel of Chapter IV, and may therefore be omitted at a first reading.
We shall see moreover further on `(7.9.8)` that the results of the present number can be considerably improved when one
has at one's disposal "resolution of singularities".

In the sequel of this number, we shall consider a property $\mathbf{R}(A)$, and we shall denote by $\mathbf{P}(Z, k)$
the following property:

> "$Z$ is a locally Noetherian prescheme over a field $k$, and, for every finite extension $k'$ of $k$, if one sets $Z'
> = Z \otimes_{k} k'$, the property $\mathbf{R}(\mathcal{O}_{Z', z'})$ is true for every $z' \in Z'$."

**Theorem (7.5.1).**

<!-- label: IV.7.5.1 -->

*Let $A$, $B$ be two complete Noetherian local rings, $\mathfrak{m}$ the maximal ideal of $A$, $k = A/\mathfrak{m}$ its
residue field, $\phi : A \to B$ a local homomorphism such that:*

*(i) The residue field of $B$ is a finite extension of $k$.*

*(ii) $B$ is a flat $A$-module.*

*Let on the other hand $\mathbf{R}(C)$ be a property verifying condition $(R_{III})$ `(7.3.18)` and the following
condition:*

*`(R_IV)` For every local ring $C$ at a prime ideal of a complete Noetherian local ring and every $C$-regular element
$t$ in the maximal ideal of $C$, the property $\mathbf{R}(C/tC)$ implies $\mathbf{R}(C)$.*

*This being so, let $f = {}^{a}\phi : \operatorname{Spec}(B) \to \operatorname{Spec}(A)$, and suppose that the property
$\mathbf{P}(\operatorname{Spec}(B \otimes_{A} k), k)$ is true. Then, for every $x \in \operatorname{Spec}(A)$, the
property $\mathbf{P}(f^{-1}(x), \mathit{k}(x))$ is true.*

In other words, the property $\mathbf{P}$ for the fibre of the closed point of $\operatorname{Spec}(A)$ entails this
same property for all fibres of the morphism $f$ (in other words, $f$ is a $\mathbf{P}$-morphism `(7.3.1)`).

We shall proceed in several steps:

I) *Reduction to the study of the local rings of the generic fibre.* — Let us apply lemma `(7.3.16.2)`: it suffices to
see that for every finite integral $A$-algebra $A'$, of field of fractions $K'$, if one sets $B' = B \otimes_{A} A'$,
all the local rings of $\operatorname{Spec}(B' \otimes_{A'} K')$ verify the property $\mathbf{R}$. The ring $A'$ (resp.
$B'$) is complete semi-local ($B'$ being a finite $B$-algebra), hence a direct composite of complete local rings; since
$A'$ is assumed integral, it is local; every maximal ideal $\mathfrak{n}'$ of $B'$ lies above the maximal ideal
$\mathfrak{n}$ of $B$, hence above $\mathfrak{m}$, and consequently its inverse image in $A'$ is the maximal ideal
$\mathfrak{m}'$ of $A'$. Since every local ring of $\operatorname{Spec}(B' \otimes_{A'} K')$ is a local ring of
$\operatorname{Spec}(B')$, hence of one of the $\operatorname{Spec}(B'_{\mathfrak{n}'})$ (above the generic point of
$A'$), one sees that it will suffice to prove that the local rings of $\operatorname{Spec}(B'_{\mathfrak{n}'}
\otimes_{A'} K')$ possess the property $\mathbf{R}$. Now $A'$ and $B'_{\mathfrak{n}'}$ are complete Noetherian local
rings; the residue field of $B'_{\mathfrak{n}'}$ is a finite extension of that of $B$, hence also of $k$, and a fortiori
of the residue field $k'$ of $A'$; this remark and `(2.1.4)` show that $A'$ and $B'_{\mathfrak{n}'}$ verify conditions
(i) and (ii) of the statement. On the other hand, if `k''` is a finite extension of $k'$, `k''` is also a finite
extension of $k$, and the local rings of $\operatorname{Spec}(B'_{\mathfrak{n}'} \otimes_{A'} k'')$ are also local rings
of $\operatorname{Spec}(B \otimes_{A} k'')$; hence the hypothesis that $\mathbf{P}(\operatorname{Spec}(B \otimes_{A} k),
k)$ is true entails that $\mathbf{P}(\operatorname{Spec}(B'_{\mathfrak{n}'} \otimes_{A'} k''), k')$ is true.

One is thus reduced to the case where $A$ is moreover assumed integral, of field of fractions $K$, and to proving that
the local rings of $\operatorname{Spec}(B \otimes_{A} K)$ possess the property $\mathbf{R}$.

II) *Case where $\dim(A) = 1$.* — Let $A'$ be the integral closure of $A$; one knows `(0, 23.1.6)` that $A'$ is a finite
$A$-algebra and a complete local ring; if one sets $B' = B \otimes_{A} A'$, one has $B \otimes_{A} K = B' \otimes_{A'}
K$. The same reasoning as in I) shows that it suffices, for every maximal ideal $\mathfrak{n}'$ of $B'$, to prove that
the local rings of $B'_{\mathfrak{n}'} \otimes_{A'} K$ verify $\mathbf{R}$; moreover, this reasoning also shows that
$A'$ and $B'_{\mathfrak{n}'}$ verify the hypotheses (i) and (ii) of the statement and that
$\mathbf{P}(\operatorname{Spec}(B'_{\mathfrak{n}'} \otimes_{A'} k'), k')$ is true ($k'$ being the residue field of
$A'$). Moreover, since $\dim(A') = 1$ `(0, 16.1.5)` and $A'$ is integral and integrally closed, it is a complete
discrete valuation ring. One may therefore restrict to the case where $A$ is already a complete discrete valuation ring;
if then $u$ is a uniformizing parameter of $A$, the fact that $u$ is $A$-regular and that $B$ is a flat $A$-module
entails that $t = \phi(u)$ is a $B$-regular element, lying in the maximal ideal of $B$. The hypothesis that
$\mathbf{P}(\operatorname{Spec}(B \otimes_{A} k), k)$ is true entails in particular that $\mathbf{R}(B/tB)$ is true; by
virtue of `(R_IV)`, $\mathbf{R}(B)$ is therefore true. In other words, $U_{\mathbf{R}}(\operatorname{Spec}(B))$ contains
the closed point of $\operatorname{Spec}(B)$. But since $U_{\mathbf{R}}(\operatorname{Spec}(B))$ is open by virtue of
$(R_{III})$ and $\operatorname{Spec}(B)$ is the only open set of $\operatorname{Spec}(B)$ containing the closed point,
all the local rings of $\operatorname{Spec}(B)$ possess the property $\mathbf{R}$, and in particular those of
$\operatorname{Spec}(B \otimes_{A} K)$.

III) *General case.* — The case $\dim(A) = 0$ is trivial, since then $A = k$; one may therefore restrict to the case
where $\dim(A) \geq 1$. One knows `(6.12.7)` that $\operatorname{Spec}(A)$ contains a non-empty open set $V$ all of
whose points are regular; since $\dim(A) \geq 1$, the intersection $V'$ of $V$ and the complement of the closed point of
$\operatorname{Spec}(A)$ is a non-empty open set, hence containing the generic point of $\operatorname{Spec}(A)$. If we
prove that $f^{-1}(V') \subset U_{\mathbf{R}}(\operatorname{Spec}(B))$, the proposition will be proved a fortiori. In
other words, it suffices to see that the set $Z$, intersection of $f^{-1}(V')$ and the complement of
$U_{\mathbf{R}}(\operatorname{Spec}(B))$, is empty. Let us reason by contradiction: since, by virtue of $(R_{III})$,
$U_{\mathbf{R}}(\operatorname{Spec}(B))$ is open in $\operatorname{Spec}(B)$, $Z$ is locally closed in
$\operatorname{Spec}(B)$; if it were not empty, it would contain a point $x$ such that $\dim(\overline{x}) \geq 1$
`(5.1.10)`; since $f(x) \in V'$ is distinct from the closed point of $\operatorname{Spec}(A)$, $x$ is distinct from the
closed point of $\operatorname{Spec}(B)$, in other words $\dim(\overline{x}) = 1$. We shall prove that this is
impossible, in other words that, if $\dim(\overline{x}) = 1$ and $f(x) \in V'$, then one has
$\mathbf{R}(\mathcal{O}_{x})$. In other terms, the matter is to see that, if $\mathfrak{q}$ is a prime ideal of $B$ such
that $\dim(B/\mathfrak{q}) = 1$ and if $\mathfrak{p} = {}^{a}\phi^{-1}(\mathfrak{q})$ is distinct from $\mathfrak{m}$
and such that $A_{\mathfrak{p}}$ is regular, then one has $\mathbf{R}(B_{\mathfrak{q}})$. Since $\mathfrak{p} \neq
\mathfrak{m}$, $\mathfrak{m}(B/\mathfrak{q})$ is not reduced to `0`, hence is an ideal of definition of the integral
Noetherian local ring $B/\mathfrak{q}$ of dimension `1`; on the other hand, by virtue of (i), the residue field of
$B/\mathfrak{q}$ is a finite extension of the residue field $k$ of $A/\mathfrak{p}$, hence $B/\mathfrak{q}$ is a
quasi-finite $(A/\mathfrak{p})$-algebra $(0_{I}, 7.4.4)$. But $A/\mathfrak{p}$ is complete and $B/\mathfrak{q}$ is
separated for the $\mathfrak{m}$-preadic topology (which is identical to its local-ring topology); hence $(0_{I},
7.4.1)$, $B/\mathfrak{q}$ is a finite $(A/\mathfrak{p})$-algebra. Moreover, by definition, the homomorphism
$A/\mathfrak{p} \to B/\mathfrak{q}$ is injective, hence `(0, 16.1.5)` one has $\dim(A/\mathfrak{p}) =
\dim(B/\mathfrak{q}) = 1$. One can then apply to the rings $A/\mathfrak{p}$ and $B/\mathfrak{p}B$ the result of II), for
the residue fields of these local rings are respectively those of $A$ and of $B$, and $B/\mathfrak{p}B$ is a flat
$(A/\mathfrak{p})$-module; moreover, one has $(B/\mathfrak{p}B) \otimes_{A/\mathfrak{p}} k = B \otimes_{A} k =
B/\mathfrak{m}B$. Consequently, the local rings of $\operatorname{Spec}((B/\mathfrak{p}B) \otimes_{A/\mathfrak{p}}
\mathit{k}(\mathfrak{p}))$ verify $\mathbf{R}$. Now, $B_{\mathfrak{q}}/\mathfrak{p}B_{\mathfrak{q}}$ is one of the local
rings of $\operatorname{Spec}((B/\mathfrak{p}B) \otimes_{A/\mathfrak{p}} \mathit{k}(\mathfrak{p}))$. Moreover,
$B_{\mathfrak{q}}$ is a flat $A_{\mathfrak{p}}$-module, and $A_{\mathfrak{p}}$ is regular. Now one has the following
lemma:

<!-- original page 205 -->

**Lemma (7.5.1.1).**

<!-- label: IV.7.5.1.1 -->

*Let $\mathcal{C}$ be a full subcategory of the category of Noetherian local rings, such that every quotient ring of a
ring of $\mathcal{C}$ still belongs to $\mathcal{C}$. Let $\mathbf{R}(C)$ be a property such that if $C \in \mathcal{C}$
and if $t$ is a regular element of the maximal ideal of $C$ such that $\mathbf{R}(C/tC)$ is true, then $\mathbf{R}(C)$
is true.*

*This being so, let $C$ be a regular local ring, $k$ its residue field, $D$ a local ring belonging to $\mathcal{C}$,
$\phi : C \to D$ a local homomorphism making $D$ a flat $C$-module. Then, if $\mathbf{R}(D \otimes_{C} k)$ is true, the
same is so of $\mathbf{R}(D)$.*

Let us reason by induction on $n = \dim(C)$, the lemma being true by hypothesis if $n = 0$, since then $C = k$. Let $t$
be an element of the maximal ideal $\mathfrak{m}$ of $C$ not belonging to $\mathfrak{m}^{2}$; one knows then that $C/tC$
is regular and that $\dim(C/tC) = n - 1$ (`(0, 17.1.8)` and `(0, 16.3.4)`). Since $(D/tD) \otimes_{C/tC} k = D
\otimes_{C} k$, and $D/tD \in \mathcal{C}$, the induction hypothesis shows that $\mathbf{R}(D/tD)$ is true; moreover,
$t$ is $C$-regular, hence also $D$-regular by flatness $(0_{I}, 6.3.4)$; the hypothesis made on $\mathbf{R}$ therefore
shows that $\mathbf{R}(D)$ is true.

To finish the proof of `(7.5.1)`, it suffices here to apply lemma `(7.5.1.1)` taking for $\mathcal{C}$ the category of
the local rings of the spectra of complete local rings, taking into account the hypothesis `(R_IV)`, and taking for $C$
the ring $A_{\mathfrak{p}}$, for $D$ the ring $B_{\mathfrak{q}}$.

**Corollary (7.5.2).**

<!-- label: IV.7.5.2 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ the maximal ideal of $A$, $k = A/\mathfrak{m}$ its residue field,
$B$ a Noetherian local ring, $\phi : A \to B$ a local homomorphism such that:*

*(i) The residue field of $B$ is a finite extension of $k$.*

*(ii) $B$ is a flat $A$-module.*

*Let on the other hand $\mathbf{R}(C)$ be a property verifying conditions `(R_II)` `(7.3.10)`, $(R_{III})$ `(7.3.18)`
and `(R_IV)` `(7.5.1)`.*

*Finally, let $\mathbf{R}'(C)$ be a property verifying the following condition:*

*`(R_V)` If $C$, $D$ are two Noetherian local rings, $\psi : C \to D$ a local homomorphism such that* *$g = {}^{a}\psi :
\operatorname{Spec}(D) \to \operatorname{Spec}(C)$ is a $\mathbf{P}$-morphism, then the property $\mathbf{R}'(C)$
implies $\mathbf{R}(D)$.*

*Suppose that the canonical morphism $\operatorname{Spec}(\hat{A}) \to \operatorname{Spec}(A)$ is a
$\mathbf{P}'$-morphism, where $\mathbf{P}'$ is defined from $\mathbf{R}'$ as $\mathbf{P}$ from $\mathbf{R}$ in
`(7.5.0)`.*

*This being so, let $f = {}^{a}\phi : \operatorname{Spec}(B) \to \operatorname{Spec}(A)$, and suppose that the property
$\mathbf{P}(\operatorname{Spec}(B \otimes_{A} k), k)$ is true. Then, for every $x \in \operatorname{Spec}(A)$, the
property $\mathbf{P}(f^{-1}(x), \mathit{k}(x))$ is true (in other words, $f$ is a $\mathbf{P}$-morphism).*

Let us proceed once again in two steps:

I) *Reduction to the study of the local rings of the generic fibre.* — Let us apply once again lemma `(7.3.16.2)`; the
only difference with the reasoning of I) in `(7.5.1)` is that here the ring $A'$ is only a semi-local integral ring, but
not necessarily local; every maximal ideal $\mathfrak{n}'$ of $B'$ is then above a maximal ideal $\mathfrak{m}'$ of
$A'$; since every local ring of $\operatorname{Spec}(B' \otimes_{A'} K')$ is a local ring of $\operatorname{Spec}(B')$,
hence of one of the $\operatorname{Spec}(B'_{\mathfrak{n}'})$ (above the generic point of
$\operatorname{Spec}(A'_{\mathfrak{m}'})$), one is reduced to proving that the local rings of
$\operatorname{Spec}(B'_{\mathfrak{n}'} \otimes_{A'_{\mathfrak{m}'}} K')$ possess the property $\mathbf{R}$. Now, the
definition of $\mathbf{P}'$ implies that if $\mathbf{P}'(Z, k)$ is true, the same is so of $\mathbf{P}'(Z \otimes_{k}
k', k')$ for every finite extension $k'$ of $k$; the same reasoning as in `(7.3.7)` proves that the formal fibres of
$A'_{\mathfrak{m}'}$ possess the property $\mathbf{P}'$. One sees as in part I) of the proof of `(7.5.1)` that
$A'_{\mathfrak{m}'}$ and $B'_{\mathfrak{n}'}$ verify conditions (i) and (ii) of `(7.5.2)`; on the other hand, if $k'$ is
the residue field of $A'_{\mathfrak{m}'}$, the property $\mathbf{P}(\operatorname{Spec}(B'_{\mathfrak{n}'}
\otimes_{A'_{\mathfrak{m}'}} k'), k')$ is true: in effect, the completion of $A'_{\mathfrak{m}'}$ is one of the
component local rings of $\hat{A}' = \hat{A} \otimes_{A} A'$, and the completion of $B'_{\mathfrak{n}'}$ one of the
component local rings of $\hat{B}' = \hat{B} \otimes_{B} B' = \hat{B} \otimes_{A} A' = B \otimes_{A} \hat{A}'$; the
reasoning of I), in `(7.5.1)`, proves therefore our assertion.

One may therefore restrict to the case where $A$ is moreover assumed integral, and to proving that, if $K$ is the field
of fractions of $A$, the local rings of $\operatorname{Spec}(B \otimes_{A} K)$ possess the property $\mathbf{R}$.

II) *Reduction to the case where $A$ and $B$ are complete.* — Let $\xi$ be the generic point of
$\operatorname{Spec}(A)$, $y$ an arbitrary point of $f^{-1}(\xi)$; the matter is to prove that
$\mathbf{R}(\mathcal{O}_{y})$ is true; taking account of condition `(R_II)`, it will suffice to see that there exists in
$\operatorname{Spec}(\hat{B})$ a point $z$ above $y$ and such that $\mathbf{R}(\mathcal{O}_{z})$ is true. Now, it
results from the hypothesis made on $\operatorname{Spec}(B \otimes_{A} k)$ and from `(7.5.1)` that the morphism
$\hat{f} : \operatorname{Spec}(\hat{B}) \to \operatorname{Spec}(\hat{A})$ is a $\mathbf{P}$-morphism. On the other hand,
for every point $z \in \operatorname{Spec}(\hat{B})$ above $y$ (there exists such a point, since $\hat{B}$ is a
faithfully flat $B$-module), the image $x$ of $z$ in $\operatorname{Spec}(\hat{A})$ belongs to the fibre $h^{-1}(\xi)$
for the canonical morphism $h : \operatorname{Spec}(\hat{A}) \to \operatorname{Spec}(A)$; by virtue of the hypothesis
made on $A$, the property $\mathbf{R}'(\mathcal{O}_{x})$ is true; hence by virtue of `(R_V)`,
$\mathbf{R}(\mathcal{O}_{z})$ is true. Q.E.D.

**Examples (7.5.3).**

<!-- label: IV.7.5.3 -->

*Let us consider the following properties $\mathbf{R}(C)$ ($C$ being a Noetherian local ring):*

*(i) (also denoted $(i_{n})$) $coprof(C) \leq n$.*

<!-- original page 206 -->

*(ii) (also denoted $(ii_{k})$) $C$ verifies $(S_{k})$.*

*(iii) $C$ is a Cohen-Macaulay ring.*

*(iv) $C$ is a regular ring.*

*(v) (also denoted $(v_{k})$) $C$ is integral, integrally closed and verifies $(R_{k})$.*

*(vi) $C$ is integral and integrally closed.*

*(vii) $C$ is integral.*

*(viii) $C$ is reduced.*

All these properties verify $(R_{III})$, as one has seen in `(7.3.19, (i))`. They also verify `(R_IV)`: for (i), this
results from `(0, 16.4.10, (ii))`, and for (ii) and (iii), this results from `(5.12.4)` and from the fact that a
complete Noetherian local ring is catenary `(5.6.4)`; for (iv), this is a particular case of `(0, 17.1.8)`; for (vii),
this follows from `(3.4.5)` and for (viii) from `(3.4.6)`; for (vi) this results from `(5.12.7)` and from the fact that
a complete Noetherian local ring is catenary `(5.6.4)`; finally, for (v), this results from what precedes and from
`(5.12.5)`.

One can therefore apply the theorem `(7.5.1)` when $\mathbf{R}$ is any of the properties above. On the other hand, one
has already remarked `(7.3.11)` that the properties (i) to (viii) verify `(R_II)` (except for (vii), where the
verification of `(R_II)` is a consequence of `(2.1.14)`). As regards `(R_V)`, one will note that if one takes there
$\mathbf{R}' = \mathbf{R}$, the condition `(R_V)` reduces to the condition `(R_I)` of `(7.3.11)`, and one has noted that
the properties (ii) to (vi), as well as (viii), verify `(R_I)` `(7.3.11)`; for the property (i), one can take for
$\mathbf{R}'$ the property of being a Cohen-Macaulay ring, by virtue of `(6.3.2)`. Finally, for the property (vii), the
condition `(R_I)` is no longer verified (nor moreover `(R_I)`), as the example of `(6.15.11, (ii))` or of
`(6.5.5, (ii))` shows. By contrast, `(R_V)` is then true when one takes for $\mathbf{R}'$ the property of being regular:
it suffices in effect to apply lemma `(7.5.1.1)` taking for $\mathcal{C}$ the category of all Noetherian local rings,
and for $\mathbf{R}(C)$ the property of being integral; this is possible by virtue of `(3.4.5)`.

One sees thus in particular that when $\mathbf{R}$ is any of the properties (i) to (viii), the conclusion of corollary
`(7.5.2)` is applicable when one supposes that the formal fibres of $A$ are geometrically regular (cf. `(7.8.2)`).

**Remarks (7.5.4).**

<!-- label: IV.7.5.4 -->

*(i) It would be interesting to know whether the theorem `(7.5.1)` subsists without the finiteness hypothesis (i) on the
residue field of $B$. The answer is affirmative when the residue field $k$ of $A$ is of characteristic `0`, as one sees
using Hironaka's results on resolution of singularities (cf. `(7.9.8)`). Let us signal the following particular case of
the question raised here: Let $A$ and $B$ be two complete Noetherian rings, $k$ the residue field of $A$, $\phi : A \to
B$ a local homomorphism making $B$ a formally smooth $A$-algebra `(0, 19.3.1)` (which is equivalent to saying that $B$
is a flat $A$-module and that $B \otimes_{A} k$ is geometrically regular over $k$ `(0, 19.7.1)`). Are then the fibres of
the morphism ${}^{a}\phi : \operatorname{Spec}(B) \to \operatorname{Spec}(A)$ geometrically regular? Such is the case
when the residue field $k'$ of $B$ is a finite extension of $k$, by `(7.5.1)`; one can prove that the answer is still
affirmative when $k'$ is a finitely generated extension of $k$. We do not know the answer when $B \otimes_{A} k$ is a
field equal to the separable closure of $k$.*

*(ii) One could state a result analogous to `(7.5.1)` relative to an $A$-module $M$, a $B$-module $N$, both of finite
type, concerning the properties of $(M \otimes_{A} N)_{y} \otimes_{\mathcal{O}_{y}} \mathit{k}(y)$, where $y$ runs over
$\operatorname{Spec}(B)$ and $x = f(y)$, following from properties of the same type of $M_{x}$ and $N_{y}$.*

*(iii) When the property $\mathbf{R}$ verifies the conditions `(R_I)`, `(R_II)`, $(R_{III})$ and `(R_IV)` and the
hypotheses (i) and (ii) of `(7.5.2)` are fulfilled, then, from the properties $\mathbf{R}(A)$ and
$\mathbf{P}(\operatorname{Spec}(B \otimes k), k)$ one deduces $\mathbf{R}(B)$. This is the case, as one has seen
`(7.5.3)`, for the properties given as examples in `(7.5.3)`, except for (i) and (vii). As regards (vii), it is however
plausible that the answer to the following question is affirmative: let $\phi : A \to B$ be a local homomorphism of
Noetherian local rings, making $B$ a flat $A$-module. Suppose that $A$ is complete, integral and geometrically
unibranch, and that the fibre $\operatorname{Spec}(B \otimes_{A} k)$ (where $k$ is the residue field of $A$) is
geometrically locally integral; then is it true that $B$ is integral? One can prove it when $k$ is of characteristic
`0`, using Hironaka's resolution of singularities `(7.9.8)`; one can also show that the answer is affirmative when $B$
is an $A$-algebra essentially of finite type `(1.3.8)` (cf. `(11.3.10)` and `(11.3.11)`) or when $\operatorname{Spec}(B
\otimes_{A} k)$ is geometrically normal (for it results then from `(7.5.3)` that the morphism $\operatorname{Spec}(B)
\to \operatorname{Spec}(A)$ is normal, hence one concludes by `(6.15.10)`). But even supposing that the residue field of
$B$ is equal to that of $A$ and that $B$ is also complete, we do not know if the answer is affirmative in the general
case.*

*(iv) Let us consider the property $\mathbf{R}(C)$: "$C$ is reduced, equidimensional and verifies `(R_1)`"; it verifies
`(R_IV)`, by virtue of `(5.12.5)`, but it is not known on the other hand whether it verifies `(R_I)`, `(R_II)` or
$(R_{III})$, the difficulties coming from the verification of equidimensionality.*

<!-- original page 207 -->

In the sequel of this number, we shall apply `(7.5.1)` to the study of the completed tensor products $A
\hat{\otimes}_{k} B$ of Noetherian local rings that are algebras over a field $k$.

**Lemma (7.5.5).**

<!-- label: IV.7.5.5 -->

*Let $k$ be a field, $A$, $B$ two complete Noetherian local rings containing $k$, the residue field of $A$ being a
finite extension of $k$. Let $C$ be the completed tensor product $A \hat{\otimes}_{k} B$ $(0_{I}, 7.7.5)$. Then:*

*(i) $C$ is a complete semi-local Noetherian ring.*

*(ii) $C$ is a flat $A$-module and a flat $B$-module.*

*(iii) If $\mathfrak{m}$ is the maximal ideal of $A$, $\mathfrak{m}C$ is contained in the radical of $C$, and
$C/\mathfrak{m}C$ is isomorphic to $(A/\mathfrak{m}) \otimes_{k} B$.*

*(iv) The residue fields of the local components of $C$ are finite extensions of the residue field of $B$.*

Properties (i), (iii) and the first assertion of (ii) are particular cases of `(0, 19.7.1.2)`. To prove that $C$ is a
flat $B$-module, let us note that for every $h > 0$, $C/\mathfrak{m}^{h} C = (A/\mathfrak{m}^{h}) \otimes_{k} B$ is a
flat $B$-module, since $k$ is a field; it therefore suffices to apply $(0_{III}, 10.2.6)$ to each of the local
components of $C$ (of which $C$ is the direct composite). Finally, if $\mathfrak{n}$ is the maximal ideal of $B$, the
residue fields of the local components of $C$ are also those of the local components of the Artinian ring
$(A/\mathfrak{m}) \otimes_{k} (B/\mathfrak{n})$, which, by hypothesis, are finite extensions of $B/\mathfrak{n}$.

**Proposition (7.5.6).**

<!-- label: IV.7.5.6 -->

*Let $k$ be a field, $A$, $B$ two complete Noetherian local rings containing $k$, and whose residue fields are finite
extensions of $k$. Let on the other hand $\mathbf{R}$ be a property verifying conditions `(R_I)`, $(R_{III})$ and
`(R_IV)` (the property $\mathbf{P}$ being defined from $\mathbf{R}$ by `(7.5.0)`). Suppose that $\mathbf{R}(A)$ is true,
as well as $\mathbf{P}(\operatorname{Spec}(B), k)$ (which signifies that for every finite extension $k'$ of $k$ and for
each of the complete local rings $B_{h}$ of which $B \otimes_{k} k'$ is the direct composite, $\mathbf{R}(B_{h})$ is
true). Then, for each of the complete local rings $C_{j}$ of which $A \hat{\otimes}_{k} B$ is the direct composite,
$\mathbf{R}(C_{j})$ is true.*

It results from `(7.5.5, (iii))` that each of the homomorphisms $A \to C_{j}$ is local and from `(7.5.5, (ii))` that
each of the $C_{j}$ is a flat $A$-module; finally, by `(7.5.5, (iv))`, the residue fields of the $C_{j}$ are finite
extensions of $A/\mathfrak{m}$. On the other hand, the property $\mathbf{P}(\operatorname{Spec}(C_{j} \otimes_{A}
(A/\mathfrak{m})), A/\mathfrak{m})$ is true, since $C/\mathfrak{m}C = (A/\mathfrak{m}) \otimes_{k} B$, and the assertion
results from the definition of $\mathbf{P}$ and from the hypothesis that $A/\mathfrak{m}$ is a finite extension of $k$.
All the conditions of `(7.5.1)` are therefore verified for the local homomorphisms $A \to C_{j}$, and the corresponding
morphisms $\operatorname{Spec}(C_{j}) \to \operatorname{Spec}(A)$ are therefore $\mathbf{P}$-morphisms; the conclusion
results then from `(R_I)` and from the hypothesis that $\mathbf{R}(A)$ is true.

**Corollary (7.5.7) (Chevalley).**

<!-- label: IV.7.5.7 -->

*Let $k$ be a perfect (resp. algebraically closed) field, $A$, $B$ two complete Noetherian local rings containing $k$
and whose residue fields are finite extensions of $k$. Then, if $A$ and $B$ are reduced (resp. integral), the completed
tensor product $A \hat{\otimes}_{k} B$ is reduced (resp. integral).*

I) Suppose $k$ perfect, $A$ and $B$ reduced; let $A_{i}$ (resp. $B_{j}$) be the quotients of $A$ (resp. $B$) by its
minimal prime ideals ($1 \leq i \leq r$, $1 \leq j \leq s$), which are complete; the hypothesis entails that $A$ (resp.
$B$) identifies with a subring of the direct composite of the $A_{i}$ (resp. $B_{j}$); the tensor products being taken
over a field, $A \otimes_{k} B$ identifies with a subring of the direct composite of the $A_{i} \otimes_{k} B_{j}$, and
one verifies at once that the tensor-product topology of $A \otimes_{k} B$ is induced by the product of the topologies
of the $A_{i} \otimes_{k} B_{j}$. It results from this that $A \hat{\otimes}_{k} B$ identifies with a subring of the
direct composite of the $A_{i} \hat{\otimes}_{k} B_{j}$, and one is therefore reduced to the case where $A$ and $B$ are
integral. Let then $A'$ and $B'$ be the integral closures of $A$ and $B$ respectively; one knows, by Nagata's finiteness
theorem `(0, 23.1.6)`, that $A'$ (resp. $B'$) is a finite $A$-module (resp. $B$-module) and a complete local ring.
Moreover, $A \hat{\otimes}_{k} B$ identifies with a subring of $A' \hat{\otimes}_{k} B'$: indeed, it will suffice to
prove that $A \hat{\otimes}_{k} B$ identifies with a subring of $A' \hat{\otimes}_{k} B$, and the latter with a subring
of $A' \hat{\otimes}_{k} B'$. This results from the following lemma:

**Lemma (7.5.7.1).**

<!-- label: IV.7.5.7.1 -->

*Let $A$, $B$ be two complete Noetherian local rings containing a field $k$ and whose residue fields are finite
extensions of $k$. Let $\mathfrak{m}$ be the maximal ideal of $A$. For every $A$-module $M$ of finite type (endowed with
the $\mathfrak{m}$-adic topology), the completed tensor product $M \hat{\otimes}_{k} B$ $(0_{I}, 7.7.1)$ identifies
canonically with $M \otimes_{A} (A \hat{\otimes}_{k} B)$.*

Indeed, one has a canonical isomorphism $M \otimes_{k} B \xrightarrow{\sim} M \otimes_{A} (A \otimes_{k} B)$, hence a
canonical composite homomorphism

```text
   φ : M ⊗_k B  →  M ⊗_A (A ⊗_k B)  →  M ⊗_A (A ⊗̂_k B)
```

and it is immediate that this homomorphism is continuous for the tensor-product topologies; moreover, $M \otimes_{A} (A
\hat{\otimes}_{k} B)$ is separated and complete (`(7.5.5)` and $(0_{I}, 7.7.8)$), hence one also has by completion a
continuous homomorphism

```text
   φ̂ : M ⊗̂_k B  →  M ⊗_A (A ⊗̂_k B).
```

<!-- original page 208 -->

It is immediate that this homomorphism is bijective when $M$ is free of finite type; since one has an exact sequence $L'
\to L \to M \to 0$, where $L$ and $L'$ are finite free $A$-modules, one deduces from it a commutative diagram

```text
   L' ⊗̂_k B  ──────→  L ⊗̂_k B  ──────→  M ⊗̂_k B  ────→  0

   L' ⊗_A (A ⊗̂_k B) → L ⊗_A (A ⊗̂_k B) → M ⊗_A (A ⊗̂_k B) → 0
```

where the rows are exact (the first by virtue of the definition of the completed tensor product and of $(0_{I},
13.2.2)$); the first two vertical arrows being bijections, the same is so of the third.

The fact that $A \hat{\otimes}_{k} B$ identifies with a subring of $A' \hat{\otimes}_{k} (A \hat{\otimes}_{k} B)$
results then from the fact that $A$ is a subring of $A'$ and that $A \hat{\otimes}_{k} B$ is a flat $A$-module
`(7.5.5)`. One may thus suppose moreover that $A$ and $B$ are integrally closed; since moreover $k$ is assumed perfect,
$\operatorname{Spec}(A)$ and $\operatorname{Spec}(B)$ are geometrically normal over $k$ by virtue of `(6.7.7, b))`; one
can then apply `(7.5.6)` taking for $\mathbf{R}$ the property (vi) of `(7.5.3)`.

II) Suppose $k$ algebraically closed, $A$ and $B$ integral. The reasoning of I) reduces once again to the case where $A$
and $B$ are integrally closed; it then results from `(7.5.6)` that $\operatorname{Spec}(A \hat{\otimes}_{k} B)$ is
normal, hence $A \hat{\otimes}_{k} B$ is a direct composite of integrally closed complete local rings, and everything
comes down to seeing that $A \hat{\otimes}_{k} B$ is a local ring. It suffices for this to verify that if $\mathfrak{m}$
and $\mathfrak{n}$ are the maximal ideals of $A$ and $B$, $(A/\mathfrak{m}) \otimes_{k} (B/\mathfrak{n})$ is a local
ring (see proof of `(0, 19.7.1.2)`); but since $A/\mathfrak{m}$ and $B/\mathfrak{n}$ are finite extensions of $k$, they
are identical to $k$, whence the conclusion.

**Remark (7.5.8).**

<!-- label: IV.7.5.8 -->

*It would be interesting to determine whether, in `(7.5.7)`, one can replace the hypothesis that $k$ is perfect or
algebraically closed by the hypothesis that $\operatorname{Spec}(A)$ or $\operatorname{Spec}(B)$ is geometrically
integral over $k$, or at least by the hypothesis that $A$ (for example) is integral and contains a subring `A_0`
isomorphic to a ring of formal series $k[[T_{1}, \cdots, T_{n}]]$, such that the field of fractions $K$ of $A$ is
separable over the field of fractions `K_0` of `A_0` (one can show that this condition entails that $A$ is geometrically
integral over $k$, and that the two properties are equivalent when $[k : k^{p}]$ is finite ($p$ being the characteristic
exponent of $k$)). Likewise, it would be desirable to develop variants of `(7.5.6)` and `(7.5.7)` in which one would
weaken the hypothesis of finiteness of the residue fields of $A$ and $B$, by supposing for example that only one of them
is a finite extension of $k$, the other being arbitrary.*

### 7.6. Applications: I. Local Japanese rings

**Proposition (7.6.1).**

<!-- label: IV.7.6.1 -->

*Let $A$ be a reduced Noetherian local ring whose formal fibres are geometrically normal. Then the completion `Â` is
reduced, the integral closure $A'$ of $A$ in its total ring of fractions is a finite $A$-algebra (hence a semi-local
Noetherian ring) and its completion `Â'` is isomorphic to the integral closure of `Â` in its total ring of fractions.*

The formal fibres of $A$ are a fortiori geometrically reduced, hence the hypothesis that $A$ is reduced entails that the
same is so of `Â`, by virtue of `(7.3.17)`. Let $p_{i}$ $(1 \leq i \leq n)$ be the minimal prime ideals of $A$, and set
$B_{i} = A/p_{i}$; the formal fibres of the local rings $B_{i}$ are then also geometrically normal `(7.3.15)`, hence the
$\hat{B}_{i}$ are also reduced and it results from `(0, 23.1.7, (i))` that the integral closure $B'_{i}$ of $B_{i}$ in
its field of fractions is a $B_{i}$-module of finite type, hence an $A$-module of finite type; since $A'$ is the direct
composite of the $B'_{i}$ `(II, 6.3.8)`, one sees that $A'$ is an $A$-module of finite type. Let $\mathfrak{m}_{j}$ $(1
\leq j \leq r)$ be the maximal ideals of the semi-local ring $A'$; one knows that the completion `Â'` of $A'$ identifies
with the direct composite of the completions $\hat{A}'_{\mathfrak{m}_{j}}$ of the $A'_{\mathfrak{m}_{j}}$ (Bourbaki,
*Alg. comm.*, chap. III, §2, n° 13, cor. of prop. 19).

<!-- original page 209 -->

Now, it results from the hypothesis and from `(7.3.15)` that the formal fibres of the $A'_{\mathfrak{m}_{j}}$ are
geometrically normal; since $\operatorname{Spec}(A')$ is normal by definition, the same is so of the
$\operatorname{Spec}(A'_{\mathfrak{m}_{j}})$, and one deduces therefore from `(7.3.17)` that
$\operatorname{Spec}(\hat{A}'_{\mathfrak{m}_{j}})$ is normal for every $j$, hence also $\operatorname{Spec}(\hat{A}')$.
On the other hand (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9 and chap. III, §3, n° 4, th. 3), `Â'`
identifies with $A' \otimes_{A} \hat{A}$ since $A'$ is an $A$-module of finite type; since $A'$ contains $A$ and is
contained in the total ring of fractions $R$ of $A$, and since `Â` is a flat $A$-module, `Â'` contains `Â` and is
contained in $R' = R \otimes_{A} \hat{A}$; finally, since `Â` is a flat $A$-module, every regular element of $A$ is also
`Â`-regular $(0_{I}, 6.3.4)$; hence $R'$ identifies canonically with a subring of the total ring of fractions `R''` of
`Â` (Bourbaki, *Alg. comm.*, chap. II, §2, n° 1, Remark 7). Since $\operatorname{Spec}(\hat{A}')$ is normal and `Â'` is
an `Â`-module of finite type, `Â'` is indeed the integral closure of `Â` in `R''`.

**Corollary (7.6.2).**

<!-- label: IV.7.6.2 -->

*Under the hypotheses of `(7.6.1)`, there is a canonical bijective correspondence between the set of maximal ideals
$\mathfrak{m}_{j}$ of $A'$ (in other words, the set of points of $\operatorname{Spec}(A')$ above the closed point of
$A$) and the set of minimal prime ideals $\mathfrak{q}_{j}$ of `Â` (in other words, the set of maximal points of
$\operatorname{Spec}(\hat{A})$); in this correspondence, the completion $\hat{A}'_{\mathfrak{m}_{j}}$ of
$A'_{\mathfrak{m}_{j}}$ is isomorphic to the integral closure of $\hat{A}/\mathfrak{q}_{j}$.*

One knows indeed that the integral closure of `Â` in its total ring of fractions is the direct composite of the integral
closures of the $\hat{A}/\mathfrak{q}_{j}$, which are complete local rings `(0, 23.1.6)`.

**Corollary (7.6.3).**

<!-- label: IV.7.6.3 -->

*Under the hypotheses of `(7.6.1)`, in order that $A$ be integral, it is necessary and sufficient that `Â` be unibranch;
in order that $A$ be geometrically unibranch, it is necessary and sufficient that `Â` be so.*

This is a particular case of `(7.6.2)`.

**Theorem (7.6.4) (Zariski-Nagata).**

<!-- label: IV.7.6.4 -->

*Let $A$ be a semi-local Noetherian ring. The following conditions are equivalent:*

*a) For every reduced finite $A$-algebra $C$, the completion `Ĉ` is a reduced ring.*

*a') For every integral quotient ring $B$ of $A$, of field of fractions $K$, the completion $\hat{B}$ is reduced, and
the component fields $L_{j}$ of the total ring of fractions of $\hat{B}$ are separable extensions of $K$.*

*a'') The formal fibres of $A$ are geometrically reduced (in other words, for every integral quotient ring $B$ of $A$,
of field of fractions $K$, the $K$-algebra $\hat{B} \otimes_{B} K$ is separable `(4.6.2)`).*

*b) Every integral quotient ring $B$ of $A$ is a Japanese ring.*

To show that a) entails a'), it suffices to verify that the $L_{j}$ are separable extensions of $K$, or again `(4.6.1)`
that for every finite extension $K'$ of $K$, the ring $\hat{B} \otimes_{B} K'$ is reduced; now $K'$ is generated by a
finite number of elements integral over $B$, and these last generate a finite sub-$B$-algebra $B'$ of $K'$, of which
$K'$ is the field of fractions. One has $\hat{B}' = \hat{B} \otimes_{B} B'$ ($(0_{I}, 7.3.3)$ and Bourbaki, *Alg.
comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9),

<!-- original page 210 -->

hence $\hat{B} \otimes_{B} K' = \hat{B}' \otimes_{B'} K'$ by associativity of the tensor product; but $B'$ is a finite
integral $A$-algebra, hence $\hat{B}'$ is a reduced ring by virtue of a), and since $\hat{B}'$ is a flat $B'$-module,
the elements $\neq 0$ of $B'$ are $\hat{B}'$-regular, which entails that $\hat{B}' \otimes_{B'} K'$ identifies with a
subring of the total ring of fractions of $\hat{B}'$, and a fortiori is reduced.

To see that a') entails a''), let us consider an arbitrary point $x$ of $X = \operatorname{Spec}(A)$, and let $Y$ be the
integral closed sub-scheme of $X$ having ${x}$ for underlying space; one has $Y = \operatorname{Spec}(B)$, where $B$ is
an integral quotient ring of $A$, and $\operatorname{Spec}(\hat{B}) = Y \times_{X} \operatorname{Spec}(\hat{A})$, so
that the formal fibre of $A$ at the point $x$ is the same as that of $B$, or again is equal to
$\operatorname{Spec}(\hat{B} \otimes_{B} K)$. Since the local rings of $\operatorname{Spec}(\hat{B} \otimes_{B} K)$ are
those of $\operatorname{Spec}(\hat{B})$ at the points of the fibre of $x$, the hypothesis entails that $\hat{B}
\otimes_{B} K$ is reduced, and the conditions of a') entail therefore that $\hat{B} \otimes_{B} K$ is a separable
$K$-algebra `(4.6.1)`.

The condition a'') entails a), for it results from `(7.3.15)` that the formal fibres of $C$ are then geometrically
reduced, and if $C$ is reduced, the same is then so of `Ĉ` (particular case of `(7.3.17)`).

The fact that a') implies b) is a particular case of `(0, 23.1.7)`. It therefore remains to prove that b) entails a).
Let us note that if $C$ is a finite $A$-algebra, for every prime ideal $\mathfrak{q}$ of $C$, the inverse image
$\mathfrak{p}$ of $\mathfrak{q}$ in $A$ is a prime ideal and $C/\mathfrak{q}$ is a finite $(A/\mathfrak{p})$-algebra,
hence hypothesis b) entails that every integral quotient ring of $C$ is a Japanese ring. One is thus reduced to proving
that under hypothesis b), the completion of every integral quotient of $A$ is reduced. Let us reason by induction on $n
= \dim(A)$, the assertion being trivial for $n = 0$; by replacing $A$ by the quotients of $A$ by its minimal prime
ideals $p_{i}$, one can restrict to the case where $A$ is integral (every integral quotient of $A$ being a quotient of
one of the $A/p_{i}$). For every prime ideal $p \neq 0$, the induction hypothesis shows already that the completion of
$A/p$ is reduced, and it therefore suffices to prove that `Â` is reduced. Moreover, the integral closure $A'$ of $A$ is
by hypothesis an $A$-module of finite type, hence a semi-local Noetherian ring, and `Â` identifies with a subring of
`Â'` ($(0_{I}, 7.3.3)$ and Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9); it will therefore suffice to
prove that `Â'` is reduced; one has seen above that hypothesis b) is also verified by $A'$, which is moreover of
dimension $n$ `(0, 16.1.5)`; one may therefore restrict to the case where $A$ is integrally closed. Let $t \neq 0$ be an
element of the radical of $A$, and let $\mathfrak{q}_{j}$ $(1 \leq j \leq n)$ be the prime ideals minimal among those
containing `tA`; one has the following properties:

*(i) $t$ is regular.*

*(ii) $A/tA$ has no embedded associated prime ideals.*

*(iii) The $A_{\mathfrak{q}_{j}}$ are discrete valuation rings.*

*(iv) The completions of the $A/\mathfrak{q}_{j}$ are reduced.*

Indeed, (i) is trivial since $A$ is integral and $t \neq 0$. Since $A$ is integrally closed, $A/tA$ verifies `(S_1)`,
that is `(5.7.7)` has no embedded associated prime ideals (Bourbaki, *Alg. comm.*, chap. VII, §1, n° 4, prop. 8). Still
because $A$ is integrally closed, the $A_{\mathfrak{q}_{j}}$ are so and one knows (*loc. cit.*) that these rings are of
dimension `1`,

<!-- original page 211 -->

hence are discrete valuation rings, whence (iii). Finally, (iv) comes from the induction hypothesis. The proof will be
finished if we prove the

**Lemma (7.6.4.1) (Zariski).**

<!-- label: IV.7.6.4.1 -->

*Let $A$ be a semi-local Noetherian ring, $t$ an element of its radical verifying conditions (i) to (iv) above; then `Â`
is reduced.*

Let us set for simplicity $A' = \hat{A}$, and consider $t$ as an element of $A'$; one has $A'/tA' = (A/tA) \otimes_{A}
A'$, and since $A'$ is a flat $A$-module, it results from `(3.3.1)` that the prime ideals of $A'$ associated with the
$A'$-module $A'/tA'$ are the prime ideals $\mathfrak{q}'_{h}$ such that $\mathfrak{q}'_{h}$ lies above
$\mathfrak{q}_{j}$ and associated with the $\mathit{k}_{j}$-module $(A'/tA') \otimes_{A} \mathit{k}_{j}$, where
$\mathit{k}_{j}$ is the field of fractions of $A/\mathfrak{q}_{j}$. Now, $\operatorname{Spec}((A'/tA') \otimes_{A}
\mathit{k}_{j})$ is the formal fibre of $A$ at the point $\mathfrak{q}_{j}$, or also that of $A/\mathfrak{q}_{j}$ at the
point $\mathfrak{q}_{j}$ (generic point of $\operatorname{Spec}(A/\mathfrak{q}_{j})$). Since by virtue of (iv) the
completion $A'/\mathfrak{q}_{j} A'$ of $A/\mathfrak{q}_{j}$ is reduced, the same is so of the formal fibre of
$A/\mathfrak{q}_{j}$ at the generic point of $\operatorname{Spec}(A/\mathfrak{q}_{j})$; this formal fibre has therefore
no embedded associated prime cycle and its local rings at the generic points $\mathfrak{q}'_{h}$ of its irreducible
components are fields `(3.2.1)`. One sees therefore by `(3.3.3)` and hypothesis (ii) that $A'/tA'$ has no embedded
associated prime ideals, and on the other hand that $\mathfrak{q}_{j} A'_{\mathfrak{q}'_{h}}$ is the maximal ideal of
$A'_{\mathfrak{q}'_{h}}$ for every $h$; since $A_{\mathfrak{q}_{j}}$ is a discrete valuation ring, its maximal ideal
$\mathfrak{q}_{j} A_{\mathfrak{q}_{j}}$ is principal, hence the maximal ideal of the Noetherian local ring
$A'_{\mathfrak{q}'_{h}}$ is principal, which entails that this ring is a discrete valuation ring (Bourbaki, *Alg.
comm.*, chap. VI, §3, n° 6, prop. 9). We have thus verified hypotheses (i) to (iv) for the complete local ring $A'$. It
therefore suffices to show that if $A$ is complete and verifies hypotheses (i) to (iii) ((iv) being automatic in this
case), then $A$ is reduced. Now, hypotheses (i) and (ii) imply that, if $\phi : A \to \prod^{n}_{j=1}
A_{\mathfrak{q}_{j}}$ is the canonical homomorphism, one has $tA = \phi^{-1}(\phi(tA))$ `(3.4.9)`; since the canonical
image of `tA` in the discrete valuation ring $A_{\mathfrak{q}_{j}}$ is a power $\mathfrak{q}^{n_{j}}_{j}
A_{\mathfrak{q}_{j}}$ of the maximal ideal, one sees that on $A$ the `(tA)`-preadic topology is the inverse image by
$\phi$ of the product topology on $\prod^{n}_{j=1} A_{\mathfrak{q}_{j}}$. Now, since $t$ belongs to the radical of $A$,
the `(tA)`-preadic topology is separated, hence $\phi$ is injective. But by virtue of hypothesis (iii), the
$A_{\mathfrak{q}_{j}}$ are integral, hence $\prod^{n}_{j=1} A_{\mathfrak{q}_{j}}$ is reduced, and a fortiori the same is
so of $A$. Q.E.D.

**Corollary (7.6.5).**

<!-- label: IV.7.6.5 -->

*Let $A$ be a semi-local Noetherian ring verifying the equivalent conditions of `(7.6.4)`; every semi-local $A$-algebra
essentially of finite type also verifies the conditions of `(7.6.4)`.*

Condition a'') of `(7.6.4)` signifies indeed that $A$ is a $\mathbf{P}$-ring, where $\mathbf{P}(Z, k)$ is the property
"$Z$ is geometrically reduced over $k$"; the corollary is therefore a consequence of the general theorem `(7.4.4)`.

**Corollary (7.6.6).**

<!-- label: IV.7.6.6 -->

*Let $A$ be a semi-local Noetherian integral ring of dimension `1`, $K$ its field of fractions. In order that $A$ be a
Japanese ring, it is necessary and sufficient that the completion `Â`*

<!-- original page 212 -->

*of $A$ be reduced and that, if $\mathfrak{q}_{j}$ $(1 \leq j \leq n)$ are the minimal prime ideals of `Â`, the fields
of fractions of the integral rings $\hat{A}/\mathfrak{q}_{j}$ be separable extensions of $K$.*

The integral quotients of $A$ are indeed $A$ itself and fields, hence condition b) of `(7.6.4)` is equivalent to the
hypothesis that $A$ is a Japanese ring, and hypothesis a') to the conditions of the statement on `Â`, whence the
conclusion.

**Remarks (7.6.7).**

<!-- label: IV.7.6.7 -->

*(i) The equivalent conditions of `(7.6.6)` signify again that the formal fibres of $A$ are geometrically regular
`(7.3.19, (iv))`. One has already observed (*loc. cit.*) that this condition is verified when $A$ is a discrete
valuation ring whose field of fractions is of characteristic `0`.*

*(ii) The same reasoning as in the first part of the proof of `(7.6.4)` shows that for a semi-local Noetherian ring $A$,
the two following conditions are equivalent:*

*a) For every integral quotient ring $B$ of $A$, the completion $\hat{B}$ is reduced.*

*a') The formal fibres of $A$ are reduced.*

*Taking account of `(0, 23.1.7, (i))`, these two conditions imply the following:*

*b) For every integral quotient ring $B$ of $A$, the integral closure of $B$ is a finite $B$-algebra.*

*When $A$ is a universally catenary ring, one can prove that condition b) entails conversely a'); we shall have no need
to use this result.*

### 7.7. Applications: II. Universally Japanese rings

**(7.7.1)** Recall `(0, 23.1.1)` that one calls **universally Japanese ring** a ring $A$ such that every integral
$A$-algebra of finite type is a Japanese ring. It comes to the same to say that for every integral $A$-algebra of finite
type $B$, the integral closure of $B$ is a finite $B$-algebra.

**Theorem (7.7.2) (Nagata).**

<!-- label: IV.7.7.2 -->

*Let $A$ be a Noetherian ring. The following conditions are equivalent:*

*a) $A$ is a universally Japanese ring.*

*b) Every integral quotient ring of $A$ is a Japanese ring.*

*c) For every maximal ideal $\mathfrak{m}$ of $A$, every integral quotient ring of $A_{\mathfrak{m}}$ is a Japanese
ring, and for every integral quotient ring $B$ of $A$, of field of fractions $K$, every finite radicial extension $K'$
of $K$ and every finite sub-$B$-algebra $B'$ of $K'$, of field of fractions $K'$, there exists $f \neq 0$ in $B'$ such
that $B'_{f}$ be integrally closed (cf. `(6.13.7)`).*

*Moreover, if $A$ verifies these conditions, the same is so of every ring of fractions $S^{-1}A$ of $A$ and of every
$A$-algebra of finite type.*

Let us first show that b) entails c); every integral quotient ring of $A_{\mathfrak{m}}$ is a ring of fractions of an
integral quotient ring of $A$, hence a Japanese ring `(0, 23.1.1)`. On the other hand, every quotient $B$ of $A$ by one
of its prime ideals is a Japanese ring, hence the same is so of $B'$ `(0, 23.1.1)`. One deduces from this that the set
$Nor(\operatorname{Spec}(B'))$ is open `(6.13.3)`, hence contains a non-empty open set $D(f') =
\operatorname{Spec}(B'_{f'})$.

<!-- original page 213 -->

Let us show in the second place that if $A$ verifies c), the same is so of every $A$-algebra of finite type $B$. In the
first place, for every prime ideal $\mathfrak{q}$ of $B$, $B_{\mathfrak{q}}$ is the local ring at a prime ideal of
$S^{-1}B$, where $S = A - \mathfrak{p}$, $\mathfrak{p}$ being the inverse image of $\mathfrak{q}$ in $A$; since by
hypothesis every integral quotient ring of $A_{\mathfrak{p}}$ is a Japanese ring, the same is so of every integral
quotient ring of $B_{\mathfrak{q}}$, since $S^{-1}B$ is an $A_{\mathfrak{p}}$-algebra of finite type `(7.6.5)`. On the
other hand, if $C$ is an integral quotient of $B$, of field of fractions $K$, $K'$ a finite radicial extension of $K$
and $C'$ a finite sub-$C$-algebra of $K'$, of field of fractions $K'$, $C'$ is an integral $A$-algebra of finite type,
and by virtue of `(6.13.7)`, hypothesis c) on $A$ entails that the spectrum of $C'$ contains a non-empty open part all
of whose points are normal; in other words, there is a $g' \neq 0$ in $C'$ such that $C'_{g'}$ be integrally closed,
which proves our assertion.

This result shows that, to prove the equivalence of a), b) and c), it suffices to show that c) entails b), and even to
prove that for every integral quotient ring $B$ of $A$, of field of fractions $K$, the integral closure $B'$ is a
$B$-module of finite type. Now, condition c) entails that there exists $f \neq 0$ in $B$ such that $B_{f}$ be integrally
closed, and one has thus verified for $B$ condition (i) of `(6.13.6)`. On the other hand, condition (ii) of `(6.13.6)`
is also verified by $B$; indeed, for every maximal ideal $\mathfrak{q}$ of $B$, $B_{\mathfrak{q}}$ is a quotient of a
local ring $A_{\mathfrak{p}}$, where $\mathfrak{p}$ is maximal in $A$; since $A_{\mathfrak{p}}$ is by hypothesis a
Japanese ring, the same is so of $B_{\mathfrak{q}}$; moreover, for every prime ideal $\mathfrak{r}$ of $B$,
$B_{\mathfrak{r}}$ is a ring of fractions of a $B_{\mathfrak{q}}$, where $\mathfrak{q}$ is a maximal ideal of $B$, hence
is again a Japanese ring, which proves our assertion.

One has moreover seen above that if $A$ verifies the equivalent conditions a), b), c), the same is so of every
$A$-algebra of finite type. On the other hand, if $A$ verifies b), the same is so of every ring of fractions $S^{-1}A$,
for every integral quotient of $S^{-1}A$ is of the form $S^{-1}A / S^{-1}\mathfrak{p}$, where $\mathfrak{p}$ is a prime
ideal of $A$, and since $A/\mathfrak{p}$ is by hypothesis a Japanese ring, the same is so of $S^{-1}(A/\mathfrak{p})$
`(0, 23.1.1)`. This completes the proof of the last assertion of the statement.

**Corollary (7.7.3).**

<!-- label: IV.7.7.3 -->

*Let $A$ be a Noetherian ring verifying the following conditions:*

*(i) For every maximal ideal $\mathfrak{m}$ of $A$, the formal fibres of $A_{\mathfrak{m}}$ are geometrically reduced.*

*(ii) The equivalent conditions of `(6.12.4)` are verified.*

*Then $A$ is universally Japanese.*

Indeed, it results then from `(7.6.4)` that every integral quotient ring of $A_{\mathfrak{m}}$ is a Japanese ring;
whence the conclusion, by virtue of `(7.7.2)`.

**Corollary (7.7.4).**

<!-- label: IV.7.7.4 -->

*A Dedekind ring whose field of fractions is of characteristic `0` (in particular $\mathbb{Z}$) is a universally
Japanese ring. A Noetherian local ring whose formal fibres are geometrically reduced (in particular a complete
Noetherian local ring) is universally Japanese.*

The first assertion results from `(7.7.3)`, `(7.6.7, (i))` and `(6.12.6)`. The second results from `(7.6.4)` and
`(7.7.2)`.

<!-- original page 214 -->

### 7.8. Excellent rings

**(7.8.1)** The preceding numbers of this section (as well as `(6.11)`, `(6.12)` and `(6.13)`) have been devoted to the
study of problems one frequently encounters in the use of Noetherian rings and preschemes, and which can be grouped in
the following types:

A) For a Noetherian local ring $A$, are the properties of $A$ "transmitted" to its completion `Â`? For example, if $A$
is reduced (resp. integral, resp. integral and integrally closed), is the same so of `Â`? Most of these questions are
linked to the local properties of the formal fibres of $A$ (let us recall that these are the fibres of the canonical
morphism $\operatorname{Spec}(\hat{A}) \to \operatorname{Spec}(A)$). An exception is formed by the properties linked to
the notion of dimension, for example the property of being equidimensional; it is then the chain condition and its
various refinements that play the essential role.

B) For a locally Noetherian prescheme $X$ (in particular for an affine scheme $\operatorname{Spec}(A)$), is the set of
$x \in X$ where the local ring $\mathcal{O}_{x}$ possesses a certain property (for instance being integrally closed, or
Cohen-Macaulay, or regular) open?

C) For an integral ring $A$, is the integral closure of $A$ in a finite extension of its field of fractions an
$A$-module of finite type? Of course, this question can be translated for Noetherian preschemes `(II, 6.3)`.

The problems of type B) or C) can also be posed for local rings, but it does not in general suffice that they be
resolved affirmatively for every local ring $A_{\mathfrak{p}}$ of a ring $A$ for them to be so for $A$ (cf. `(6.13.6)`).

Let us emphasize moreover that in the study of these problems, we have systematically been concerned with whether the
affirmative answer to one of them is stable under the two most important operations of commutative algebra: localization
and passage to an algebra of finite type.

The results obtained in the study of these problems lead one to single out the definition of a class of Noetherian rings
whose behaviour in this regard is the best possible:

**Definition (7.8.2).**

<!-- label: IV.7.8.2 -->

*One says that a ring $A$ is **excellent** if it is Noetherian and verifies the following conditions:*

*(i) $A$ is universally catenary (or, what comes to the same `(5.6.3, (i))`, for every prime ideal $\mathfrak{p}$ of
$A$, $A_{\mathfrak{p}}$ is universally catenary).*

*(ii) For every prime ideal $\mathfrak{p}$ of $A$, the formal fibres of $A_{\mathfrak{p}}$ are geometrically regular.*

*(iii) For every integral quotient ring $B$ of $A$ and every finite radicial extension $K'$ of the field of fractions
$K$ of $B$, there exists a finite sub-$B$-algebra $B'$ of $K'$, containing $B$, having $K'$ for field of fractions, and
such that the set of regular points of $\operatorname{Spec}(B')$ contains a non-empty open set.*

With this terminology, the essential part of the results of §7 and of a part of §6 is then summarized as follows:

**Scholium (7.8.3).**

<!-- label: IV.7.8.3 -->

*(i) In conditions (i) and (ii) of definition `(7.8.2)` one may restrict to the ideals $\mathfrak{p}$ maximal in $A$. In
order that a Noetherian local ring be excellent, it is necessary and*

<!-- original page 215 -->

*sufficient that it be universally catenary and that its formal fibres be geometrically regular.*

*(ii) If $A$ is an excellent ring, the same is so of every ring of fractions $S^{-1}A$ and of every $A$-algebra of
finite type.*

*(iii) A complete local ring (in particular a field) is excellent. A Dedekind ring whose field of fractions is of
characteristic `0` (in particular $\mathbb{Z}$) is excellent.*

*(iv) Let $A$ be an excellent ring, $X = \operatorname{Spec}(A)$; the set $Reg(X)$ (resp. $Nor(X)$,
$U_{\mathbf{R}_{k}}(X)$) of points where $X$ is regular (resp. normal, resp. verifies $(R_{k})$) is open in $X$. For
every coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, the set $U_{C_{n}}(\mathcal{F})$ (resp. $U_{S_{k}}(\mathcal{F})$,
$CM(\mathcal{F})$) of $x \in X$ where $coprof(\mathcal{F}) \leq n$ (resp. of points where $\mathcal{F}$ verifies
$(S_{k})$, resp. of points where $\mathcal{F}$ is a Cohen-Macaulay $\mathcal{O}_{X}$-Module) is open in $X$.*

*(v) Let $A$ be an excellent ring, $\mathfrak{J}$ an ideal of $A$, `Â` the separated completion of $A$ for the
$\mathfrak{J}$-preadic topology. Then the canonical morphism $f : \operatorname{Spec}(\hat{A}) \to
\operatorname{Spec}(A)$ is regular (in other words, flat and with geometrically regular fibres). If one sets $X =
\operatorname{Spec}(A)$, $X' = \operatorname{Spec}(\hat{A})$, one has (with the notations of (iv) and setting
$\mathcal{F}' = \mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{X'}$),*

```text
(7.8.3.1)
   Reg(X') = f⁻¹(Reg(X)),     Nor(X') = f⁻¹(Nor(X)),         U_{𝐑_k}(X') = f⁻¹(U_{𝐑_k}(X))
   U_{C_n}(ℱ') = f⁻¹(U_{C_n}(ℱ)),  U_{S_k}(ℱ') = f⁻¹(U_{S_k}(ℱ)),  CM(ℱ') = f⁻¹(CM(ℱ))
```

*In particular, if $\mathfrak{J}$ is contained in the radical of $A$ (for example if $A$ is local and $\mathfrak{J}$ its
maximal ideal), in order that $A$ be regular (resp. normal, resp. reduced, resp. verifies $(R_{k})$, resp. be of codepth
$\leq n$, resp. verifies $(S_{k})$, resp. be a Cohen-Macaulay ring), it is necessary and sufficient that the same be so
of `Â`; in particular, in order that $A$ have no embedded associated prime ideals, it is necessary and sufficient that
the same be so of `Â`.*

*(vi) An excellent ring $A$ is universally Japanese; in particular, if $A$ is integral, its integral closure in every
finite extension of its field of fractions is a finite $A$-algebra.*

*(vii) Let $A$ be a reduced excellent local ring. Then the completion `Â` is reduced, the integral closure $A'$ of $A$
in its total ring of fractions is a finite $A$-algebra (hence a semi-local ring), and the integral closure of `Â` in its
total ring of fractions is isomorphic to the completion `Â'` of $A'$. Moreover, there is a canonical bijective
correspondence between the set of maximal points of $\operatorname{Spec}(\hat{A})$ (in other words, the set of minimal
prime ideals of `Â`) and the set of closed points of $\operatorname{Spec}(A')$ (in other words, the set of maximal
ideals of $A'$). In order that the local ring $A$ be unibranch, it is necessary and sufficient that `Â` be integral; in
order that $A$ be geometrically unibranch, it is necessary and sufficient that `Â` be so.*

*(viii) If $A$ is an excellent integral ring, the integral closure of $A$ is the intersection of the integral closures
of the rings $A_{\mathfrak{p}}$, where $\mathfrak{p}$ runs over the set of prime ideals of $A$ of height `1`.*

*(ix) Let $A$ be an excellent ring, $X = \operatorname{Spec}(A)$, $Z$ a closed part of $X$, $U = X - Z$, $i : U \to X$
the canonical injection, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. In order that the $\mathcal{O}_{X}$-Module
$i_{*}(\mathcal{F}|U)$ be coherent, it is necessary and sufficient that, for every $x \in Ass(\mathcal{F})$, one have
$codim(\overline{x} \cap Z, \overline{x}) \geq 2$. In particular, if $A$ is integral and $\mathcal{F}$ torsion-free, in
order that $i_{*}(\mathcal{F}|U)$ be coherent, it is necessary and sufficient that $codim(Z, X) \geq 2$.*

<!-- original page 216 -->

*(x) Let $A$ be an excellent local ring. For every integral quotient ring $B$ of $A$, $\hat{B}$ is equidimensional. In
order that $A$ be equidimensional, it is necessary and sufficient that `Â` be so.*

Most of these results have already been proved.

(i) The first assertion results from `(5.6.3, (i))` and `(7.4.4, (i))`; the second, from `(7.4.4)`, `(7.3.18)`,
`(6.12.7)` and `(6.12.4)`.

Assertion (ii) results from `(5.6.1)`, `(5.6.3, (i))`, `(7.4.4)` and `(6.12.4)`.

(iii) The first assertion was seen in `(5.6.4)` and `(7.4.4)`, taking account of (i). The second was seen in `(5.6.4)`
and `(7.3.19, (iv))`, taking account of (i).

Assertion (iv) results from `(6.12.4)`, `(6.13.5)`, `(6.12.9)` and `(6.11.8)` (taking account of (ii)).

The first assertion of (v) is a consequence of `(7.4.6)`; the relations `(7.8.3.1)` follow from it, taking account
respectively of `(6.5.1)`, `(6.5.4)`, `(6.5.3)`, `(6.3.5)` and `(6.4.2)`. The last assertion of (v) is the particular
case corresponding to property $(S_{k})$ for $n = 1$ `(5.7.5)`.

Assertion (vi) results from `(7.7.3)`, and assertion (vii) from `(7.6.1)`, `(7.6.2)` and `(7.6.3)`. To prove (viii), let
us note that the ring $A^{(1)}$, intersection of the $A_{\mathfrak{p}}$ for all the prime ideals $\mathfrak{p}$ of
height `1` of $A$, is a finite $A$-algebra, as results from (vi), from `(7.8.2, (i))` and from `(5.11.2)`. Since the
integral closure $A'$ of $A$ is a finite $A$-algebra, the prime ideals of height `1` of $A'$ are exactly those that lie
above the prime ideals of height `1` of $A$ `(5.10.17, (iv))`; the conclusion results therefore from `(0, 23.2.9)`.

The first assertion of (ix) is a consequence of (vi) and of `(5.11.4)`; the second is a particular case of it, if one
observes that when $\mathcal{F}$ is torsion-free, $Ass(\mathcal{F})$ is reduced to the generic point of
$\operatorname{Spec}(A)$. Finally, to prove (x), it suffices to observe that $B$ is an excellent local ring by (ii);
since $B$ is universally catenary and universally Japanese by virtue of (vi), the ring $B^{(1)}$ is a finite $B$-algebra
`(5.11.2)`, which shows that $A$ is strictly formally catenary by `(7.2.5, c))` and finishes the proof of (x).

**Remarks (7.8.4).**

<!-- label: IV.7.8.4 -->

*(i) If one considers the Noetherian rings $A$ that verify only conditions (ii) and (iii) of definition `(7.8.2)`, one
verifies by inspection of the preceding proofs that the assertions (ii), (iii), (iv), (v), (vi) and (vii) of `(7.8.3)`
are still valid, replacing "excellent" by "verifying" `(7.8.2, (ii) and (iii))`.*

*(ii) The catenary local ring $A$ constructed in `(5.6.11)` verifies conditions (ii) and (iii) (but not condition (i))
of definition `(7.8.2)`. Indeed, the formal fibre at the maximal ideal $\mathfrak{n}\mathcal{O}_{A}$ of $A$ is trivially
geometrically regular, and that at the other prime ideals $\mathfrak{p}$ of $A$ coincides with that of the ring $E$ at
these prime ideals; now $E$ is a $V$-algebra of finite type and $V$ is a discrete valuation ring, which is consequently
an excellent ring if one takes the field $k_{0}$ of characteristic `0` `(7.8.3, (iii))`; consequently $E$ is an
excellent ring `(7.8.3, (ii))` and this therefore proves that $A$ verifies condition `(7.8.2, (ii))`. On the other hand,
the complement of the closed point in $\operatorname{Spec}(A)$ is isomorphic to an open part of
$\operatorname{Spec}(E)$, of which an affine open part is the spectrum of an excellent*

<!-- original page 217 -->

*ring, hence verifies condition `(6.12.4, a))` by virtue of `(7.8.3, (v))`; this proves that $A$ itself verifies the
condition of `(6.12.4, a))`, hence also `(6.12.4, c))`, which is none other than condition `(7.8.2, (iii))`. Yet $A$
does not satisfy condition `(7.8.2, (i))`, since we have seen `(5.6.11)` that it is not universally catenary.*

*(iii) One may replace condition (i) of definition `(7.8.2)` by the following (apparently weaker, taking account of
`(5.6.10)`):*

*`(i')` For every minimal prime ideal $\mathfrak{p}_{i}$ of $A$ $(1 \leq i \leq r)$, let $A'_{i}$ be the integral
closure of the integral ring $A_{i} = A/\mathfrak{p}_{i}$; then, for every maximal ideal $\mathfrak{m}'$ of $A'_{i}$,
one has, designating by $\mathfrak{m}$ the inverse image of $\mathfrak{m}'$ in $A$,*

$$ (7.8.4.1) \dim(A_{\mathfrak{m}}) = \dim((A'_{i})_{\mathfrak{m}'}). $$

Indeed, one has seen (Remark (i)) that under the sole hypotheses (ii) and (iii) of `(7.8.2)`, the analogues of
properties (ii), (v), (vi) and (vii) of `(7.8.3)` are valid. One deduces therefore first from (vi) and (ii) that the
$A'_{i}$ verify `(7.8.2, (ii) and (iii))`; it follows then from (v) that the completions `((A'_i)_{𝔪'})^` are integral
(and integrally closed). Let now $\mathfrak{m}$ be an arbitrary maximal ideal of $A$; for every $i$ such that
$\mathfrak{p}_{i} \subset \mathfrak{m}$, the integral closure of $A_{\mathfrak{m}}/\mathfrak{p}_{i} A_{\mathfrak{m}}$ is
a $(A_{\mathfrak{m}}/\mathfrak{p}_{i} A_{\mathfrak{m}})$-algebra finite by (vi), hence semi-local, and its local
components are of the form $(A'_{i})_{\mathfrak{m}'}$, where $\mathfrak{m}'$ is a prime ideal (necessarily maximal) of
$A'_{i}$ above $\mathfrak{m}/\mathfrak{p}_{i}$; it results then from (vii), from what precedes and from `(7.8.4.1)` that
the quotients of the completion `(A_𝔪/𝔭_i A_𝔪)^` by its minimal prime ideals all have the same dimension equal to
$\dim(A_{\mathfrak{m}})$. Consequently (`7.1.9` and `7.1.8, b)`), $A_{\mathfrak{m}}$ is formally catenary, and a
fortiori `(7.1.11)` universally catenary; the same is therefore so of $A_{\mathfrak{p}}$ for every prime ideal
$\mathfrak{p}$ of $A$ `(5.6.3, (i))`, hence also of $A$.

In particular, if $A$ is normal, or more generally if $A_{\mathfrak{m}}$ is unibranch for every maximal ideal
$\mathfrak{m}$ of $A$, condition `(i')` is always fulfilled, since $\mathfrak{m}$ can contain only a single prime ideal
$\mathfrak{p}_{i}$ `(0, 16.1.5)`; one may in this case omit (i) in definition `(7.8.2)`. More particularly, *if $A$ is a
unibranch Noetherian local ring, it is excellent if and only if its formal fibres are geometrically regular*.

*(iv) Let us recall that a quotient ring of a local Cohen-Macaulay ring (and a fortiori a quotient ring of a local
regular ring) also verifies the properties `(7.8.3, (ix) and (x))` by virtue of `(7.2.7)`; but the interest of the
quotients of regular rings resides above all in their cohomological properties (chap. III, 3rd Part).*

*(v) We shall see further on (§18) that if $k$ is a non-discrete complete valued field, the ring $k{{T_{1}, \cdots,
T_{n}}}$ of convergent power series (in a neighbourhood of `0` in $k^{n}$) is an excellent ring.*

**(7.8.5)** One says that a locally Noetherian prescheme $X$ is **excellent** if for one cover $(U_{\alpha})$ of $X$
formed of affine open sets, each of the rings $A_{\alpha}$ of the $U_{\alpha}$ is excellent; this property is then true
for every cover $(U_{\alpha})$ of $X$ formed of affine open sets.

**Proposition (7.8.6).**

<!-- label: IV.7.8.6 -->

*Let $X$ be an excellent prescheme.*

*(i) If $f : X' \to X$ is a locally finite-type morphism, $X'$ is excellent.*

<!-- original page 218 -->

*(ii) If $X$ is reduced, its normalization $X'$ `(II, 6.3.8)` is finite over $X$.*

*(iii) The sets $Reg(X)$, $Nor(X)$, $U_{\mathbf{R}_{k}}(X)$ are open in $X$, as well as $U_{C_{n}}(\mathcal{F})$,
$U_{S_{k}}(\mathcal{F})$ and $CM(\mathcal{F})$ for every coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$.*

This results at once from `(7.8.3, (ii), (vi) and (iv))`. Let us note also that `(7.8.3, (ix))` is valid without
modification of statement when $X$ is an excellent prescheme.

### 7.9. Excellent rings and resolution of singularities

**(7.9.1)** Given a locally Noetherian reduced prescheme $X$, one calls **resolving morphism** for $X$ a morphism $f :
X' \to X$ such that $X'$ is regular and $f$ is proper and birational. When such a morphism exists, one says that one can
**resolve the singularities** of $X$ (or more simply that one can **resolve $X$**). For instance, if $A$ is a Japanese
ring of dimension `1`, one can resolve $X = \operatorname{Spec}(A)$ since the morphism $X' \to X$ (where $X'$ is the
normalization of $X$) is finite (hence proper) and birational, and the local rings of $X'$ are integrally closed rings
of dimension `1`, hence discrete valuation rings, and are consequently regular.

**(7.9.2)** It is clear that if one can resolve $X$, one can also resolve every prescheme induced on an open set of $X$
and every local prescheme $\operatorname{Spec}(\mathcal{O}_{x})$ of $X$ `(II, 5.4.2)`. On the other hand, if one can
resolve $X$, it is clear that there exists in $X$ an open set everywhere dense contained in $Reg(X)$. These remarks show
at once that if, for every integral closed sub-prescheme $Y$ of $X$ and every $Y$-prescheme $Y'$ integral, finite and
radicial over $Y$, one can resolve $Y'$, then the affine open sets of $X$ verify condition (iii) of `(7.8.2)`.

On the other hand, for local schemes, one has the following proposition:

**Proposition (7.9.3).**

<!-- label: IV.7.9.3 -->

*Let $A$ be a reduced Noetherian local ring, and suppose that one can resolve $\operatorname{Spec}(A)$. Then the fibres
of the canonical morphism $\operatorname{Spec}(\hat{A}) \to \operatorname{Spec}(A)$ at the maximal points of
$\operatorname{Spec}(A)$ are regular.*

Set $X = \operatorname{Spec}(A)$, $X' = \operatorname{Spec}(\hat{A})$, and let $g : X' \to X$ be the canonical morphism.
Let $f : Y \to X$ be a resolving morphism; set $Y' = X' \times_{X} Y$, and let $f' : Y' \to X'$ and $g' : Y' \to Y$ be
the canonical projections, so that one has a commutative diagram

```text
                X' ←──f'── Y'
                │          │
                g          g'
                │          │
                ▼          ▼
                X  ←──f─── Y
```

It will suffice to prove that the prescheme $Y'$ is regular: indeed, since $f$ is birational and of finite type, there
is an open set $U$ everywhere dense in $X$ such that the restriction $f^{-1}(U) \to U$ of $f$ is an isomorphism and that
$f^{-1}(U)$ be everywhere dense in $Y$ `(I, 6.5.5)`; the preschemes induced respectively on the open set $g^{-1}(U)$ of
$X'$ and the open set $g'^{-1}(f^{-1}(U))$ of $Y'$ are therefore isomorphic; this proves that $g^{-1}(U)$ is regular,
and a fortiori the same is so of the fibres of $g$ at the maximal points of $X$, which are contained in $U$.

<!-- original page 219 -->

Let us note that the morphism $f'$ is proper `(II, 5.4.2)`, and in particular of finite type, hence $Y'$ is Noetherian,
since it is so of $X'$. Let $a'$ be the closed point of $X'$; to see that $Y'$ is regular, it will suffice to prove that
for every $y' \in f'^{-1}(a')$, the local ring $\mathcal{O}_{Y', y'}$ is regular. Indeed, one will then have
$f'^{-1}(a') \subset Reg(Y')$. But since $X'$ is the spectrum of a complete local ring and $f'$ is of finite type,
$Reg(Y')$ is open in $Y'$ `(6.12.8)`, and since the morphism $f'$ is closed and $f'^{-1}(a') \subset Reg(Y')$, there
exists a neighbourhood $V$ of $a'$ in $X'$ such that $f'^{-1}(V) \subset Reg(Y')$. Since `Â` is a local ring, one
necessarily has $V = X'$, hence $Reg(Y') = Y'$ and the proposition will be proved.

Now, if $a$ is the closed point of $X$, one has $g^{-1}(a) = {a'}$ and the residue fields $\mathit{k}(a)$ and
$\mathit{k}(a')$ are isomorphic; hence $g'^{-1}(f^{-1}(a)) = f'^{-1}(a')$ and the restriction $f'^{-1}(a') \to
f^{-1}(a)$ of $g'$ is an isomorphism of these two fibres. Let $y = g'(y')$ and set $B = \mathcal{O}_{y}$; if
$\mathfrak{n} = \mathfrak{m}$ is the maximal ideal of $B$, what precedes shows that there exists in the (Noetherian)
ring $B' = B \otimes_{A} \hat{A}$ a single maximal ideal $\mathfrak{n}'$ above $\mathfrak{n}$ and that one has
$\mathcal{O}_{Y', y'} = B'_{\mathfrak{n}'}$. To show that the local ring $B'_{\mathfrak{n}'}$ is regular, it suffices to
establish that its completion `(0, 17.1.5)` is so; now, by hypothesis $B$ is regular, hence the same is so of its
completion $\hat{B}$. The conclusion will follow consequently from the following lemma:

**Lemma (7.9.3.1).**

<!-- label: IV.7.9.3.1 -->

*Let $A$, $B$ be two Noetherian local rings, $\phi : A \to B$ a local homomorphism such that the ring $B' = B
\otimes_{A} \hat{A}$ be Noetherian. Then, for every maximal ideal $\mathfrak{n}'$ of $B'$ above the maximal ideal
$\mathfrak{n}$ of $B$ and the maximal ideal of `Â`, the completions of $B$ and of $B'_{\mathfrak{n}'}$ are isomorphic.*

Let $\mathfrak{m}$ be the maximal ideal of $A$ and set $B'' = B'_{\mathfrak{n}'}$. For every integer $h > 0$, one has
$B'/\mathfrak{m}^{h} B' = B \otimes_{A} (\hat{A}/\mathfrak{m}^{h} \hat{A})$; but $\hat{A}/\mathfrak{m}^{h} \hat{A}$ is
isomorphic to $A/\mathfrak{m}^{h}$, hence $B'/\mathfrak{m}^{h} B'$ is isomorphic to $B/\mathfrak{m}^{h} B$, and in
particular is a local ring whose maximal ideal is $\mathfrak{n}'/\mathfrak{m}^{h} B'$; consequently
$B''/\mathfrak{m}^{h} B''$, isomorphic to $(B'/\mathfrak{m}^{h} B')_{\mathfrak{n}'}$, is $B$-isomorphic to
$B'/\mathfrak{m}^{h} B'$, and finally to $B/\mathfrak{m}^{h} B$; in particular, the maximal ideal of `B''` is equal to
$\mathfrak{n} B''$, and $B''/\mathfrak{n}^{h} B''$ is isomorphic to $B/\mathfrak{n}^{h}$ according to what precedes.
Since $\hat{B}'' = \lim B''/\mathfrak{n}^{h} B''$, the lemma is proved, as well as `(7.9.3)`.

**Corollary (7.9.4).**

<!-- label: IV.7.9.4 -->

*Let $A$ be a Noetherian local ring.*

*(i) If, for every integral quotient ring $B$ of $A$, one can resolve $\operatorname{Spec}(B)$, then the formal fibres
of $A$ are regular.*

*(ii) Suppose that, for every integral quotient ring $B$ of $A$, and every integral ring $B'$ containing $B$, which is a
$B$-algebra finite and whose field of fractions is radicial over that of $B$, one can resolve $\operatorname{Spec}(B')$;
then the formal fibres of $A$ are geometrically regular.*

Every formal fibre of $A$ being a formal fibre of an integral quotient ring of $A$ at the generic point of its spectrum,
it is clear that (i) is an immediate consequence of `(7.9.3)`, and (ii) results from (i) and from `(6.7.7)`.

**Proposition (7.9.5).**

<!-- label: IV.7.9.5 -->

*Let $X$ be a locally Noetherian prescheme, such that, for every prescheme $Y$ integral and finite over $X$, one can
resolve $Y$. Then the rings of the affine open sets of $X$ verify conditions (ii) and (iii) of `(7.8.2)`; if moreover
$X$ is universally catenary `(5.6.3)` (and*

<!-- original page 220 -->

*in particular if $X$ is locally immersible in a regular prescheme `(5.6.4)`), $X$ is an excellent prescheme `(7.8.5)`.*

This results at once from `(7.9.4)` and `(7.9.2)`.

**Remark (7.9.6).**

<!-- label: IV.7.9.6 -->

*It is possible that the converse of `(7.9.5)` is true, that is, that the hypothesis that $X$ is reduced and that the
rings of the affine open sets of $X$ verify conditions (ii) and (iii) of `(7.8.2)` implies the possibility of resolving
$X$ (and consequently also the possibility of resolving every reduced prescheme locally of finite type over $X$, by
virtue of `(7.4.4)` and `(6.12.4)`). This is true in any case when one restricts to reduced Noetherian preschemes whose
residue fields are of characteristic `0`, as Hironaka's recent results `[35]` show (the latter states his results under
hypotheses that are too restrictive, his reasonings being in fact valid under the sole hypotheses (ii) and (iii) of
`(7.8.2)` for the rings of the affine open sets of $X$, together with the fact that the residue fields are of
characteristic `0`). By contrast, for the general case, one has up to now resolved only the algebraic schemes of
dimension `2` over a perfect field `[36]`. In view of the importance that the resolution of singularities is taking on
in the topological study of schemes (notably as regards their homological and homotopic properties), this gives a
particular interest to the category of excellent rings or excellent preschemes.*

*One can also note in this connection that the least delicate part of Hironaka's reasonings (*loc. cit.*) shows that
independently of any hypothesis on the characteristics of the residue fields, and using only properties (ii) and (iii)
of `(7.8.2)` for the local rings of a prescheme $X$, the problem of resolution of singularities of $X$ is reduced to the
case where $X = \operatorname{Spec}(A)$, $A$ being a complete integral Noetherian local ring. Consequently, if later
results should put in default the conjecture advanced above, and should therefore lead to formulating more restrictive
conditions on the local rings of $X$, this could hardly be otherwise than by means of restrictive conditions imposed on
complete local rings (probably conditions concerning their residue fields, perhaps the condition* *$[k : k^{p}] \neq
+\infty$ ($p$ exponent characteristic of $k$)).*

**(7.9.7)** Let us consider on the one hand a full subcategory $\mathcal{C}$ of the category of locally Noetherian
preschemes, on the other hand a property $\mathbf{R}(A)$, subjected to the following conditions:

1° For every $X \in \mathcal{C}$, every prescheme locally of finite type over $X$ belongs to $\mathcal{C}$. For every
Noetherian ring $A$ such that $\operatorname{Spec}(A) \in \mathcal{C}$ and every multiplicative part $S$ of $A$, one has
$\operatorname{Spec}(S^{-1}A) \in \mathcal{C}$.

2° For every $X \in \mathcal{C}$, the set $U_{\mathbf{R}}(X)$ of $x \in X$ such that $\mathbf{R}(\mathcal{O}_{x})$ be
true is open in $X$.

3° For every Noetherian local ring $A$ such that $\operatorname{Spec}(A) \in \mathcal{C}$ and every regular element $t$
of the maximal ideal of $A$, $\mathbf{R}(A/tA)$ entails $\mathbf{R}(A)$.

Let us then denote as in `(7.5.0)` by $\mathbf{P}(Z, k)$, for a field $k$ and a $k$-prescheme $Z \in \mathcal{C}$, the
following property:

<!-- original page 221 -->

> "For every finite extension $k'$ of $k$, all the local rings of $Z \otimes_{k} k'$ verify the property $\mathbf{R}$."

We shall further suppose that $\mathbf{R}$ verifies the following condition:

4° If $\mathbf{P}(Z, k)$ is true, then, for every finitely generated extension `k''` of $k$, all the local rings of $Z
\otimes_{k} k''$ verify the property $\mathbf{R}$.

One will note that these conditions are verified when one takes for $\mathcal{C}$ the category of excellent preschemes
and for $\mathbf{R}$ one of the properties (i) to (viii) of `(7.5.3)`; for condition 1°, this results from
`(7.8.3, (ii))`, and for conditions 2° and 3°, from the reasonings of `(7.5.3)`, taking account of the fact that every
excellent ring is catenary. Finally, for condition 4°, it results, for (i), (ii) and (iii) from `(6.7.1)`; for (iv),
(v), (vi) from `(6.7.7)`, and for (viii) from `(4.6.1)`; as regards property (vii) of `(7.5.3)`, the corresponding
property $\mathbf{P}(Z, k)$ entails that $Z$ is locally integral (being locally Noetherian) and that each of the
integral sub-preschemes of which $Z$ is the sum is geometrically integral, by virtue of `(4.5.9)` and `(4.6.1)`; one
again concludes property 4° above in this case.

With these notations and hypotheses:

**Proposition (7.9.8).**

<!-- label: IV.7.9.8 -->

*Let $A$ be a Noetherian local ring, $k$ its residue field, $B$ a Noetherian local ring such that
$\operatorname{Spec}(B) \in \mathcal{C}$, $\phi : A \to B$ a local homomorphism making $B$ a flat $A$-module; set $Y =
\operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$ and let $f : X \to Y$ be the morphism corresponding to $\phi$.
Suppose that:*

*1° The property $\mathbf{P}(B \otimes_{A} k, k)$ is true;*

*2° For every finite morphism $Y_{1} \to Y$, one can resolve $(Y_{1})_{red}$.*

*Then, for every $y \in Y$, the property $\mathbf{P}(f^{-1}(y), \mathit{k}(y))$ is true.*

Let us note that condition 2° of `(7.9.8)` is still verified when one replaces $Y$ by the spectrum of a local ring at a
maximal ideal of a finite $A$-algebra $A'$ `(7.9.2)`; on the other hand, by virtue of condition 1° of `(7.9.7)`, the
spectrum of a ring of fractions of $B \otimes_{A} A'$ also belongs to $\mathcal{C}$. Lemma `(7.3.16.2)` then shows (as
in part I) of the reasoning of `(7.5.2)`) that it suffices to prove that, if $Y$ is integral and if $y$ is the generic
point of $Y$, the local rings of the fibre $f^{-1}(y)$ verify $\mathbf{R}$.

This being so, there exists by hypothesis a regular prescheme $Y'$ and a proper and birational morphism $g : Y' \to Y$;
since $Y'$ is Noetherian and locally integral, the hypothesis that $g$ is birational entails that $Y'$ is integral; let
$X' = X \times_{Y} Y'$, so that one has a commutative diagram

```text
                X ←──f'── X'
                │         │
                f         f'
                │         │
                ▼         ▼
                Y ←──g─── Y'
```

*(7.9.8.1)*

where $f'$ and $g'$ are the canonical projections. Taking account of condition 2° of `(7.9.7)`, the same reasoning as at
the beginning of `(7.9.3)`

<!-- original page 222 -->

shows that it suffices to prove that one has $U_{\mathbf{R}}(X') = X'$, then, denoting by $a$ the closed point of $X$,
that $g'^{-1}(a) \subset U_{\mathbf{R}}(X')$. Now, let $x' \in g'^{-1}(a)$, and set $y' = f'(x')$, so that $b = g(y')$
is the closed point of $Y$. One has therefore $f'^{-1}(y') = f^{-1}(b) \otimes_{\mathit{k}(b)} \mathit{k}(y')$, and
since $\mathit{k}(y')$ is a finitely generated extension of $k$ (since $g$ is proper, hence of finite type), the
hypothesis that $\mathbf{P}(f^{-1}(b), k)$ is true entails by virtue of condition 4° of `(7.9.7)` that the same is so of
$\mathbf{P}(f'^{-1}(y'), \mathit{k}(y'))$. But since $\mathcal{O}_{Y', y'}$ is a regular ring and
$\operatorname{Spec}(\mathcal{O}_{Y', y'}) \in \mathcal{C}$ by virtue of condition 1° of `(7.9.7)`, lemma `(7.5.1.1)`
proves that $\mathbf{R}(\mathcal{O}_{X', x'})$ is true, which finishes the proof.

**Corollary (7.9.9).**

<!-- label: IV.7.9.9 -->

*Let $A$, $B$ be two Noetherian local rings, $\phi : A \to B$ a local homomorphism making $B$ a flat $A$-module. Suppose
that $A$ is integral and geometrically unibranch, and that for every finite integral $A$-algebra $A'$ one can resolve
$\operatorname{Spec}(A')$ (which will be the case for example if the formal fibres of $A$ are geometrically regular and
the residue field of $A$ is of characteristic `0`, on account of Hironaka's results `[35]`). Let $k$ be the residue
field of $A$ and suppose that $\operatorname{Spec}(B \otimes_{A} k)$ is geometrically pointwise integral `(4.6.9)`. Then
$B$ is integral.*

We are going to apply `(7.9.8)` taking for $\mathcal{C}$ the category of all locally Noetherian preschemes, for
$\mathbf{R}$ the property of being integral; the reasonings of `(7.5.3)` and `(7.9.7)` show that conditions 1°, 2°, 3°
and 4° of `(7.9.7)` are satisfied in this case. The hypothesis on $B \otimes_{A} k$ and proposition `(7.9.8)` show
therefore (with the notations of `(7.9.8)`) that the fibres $f^{-1}(y)$ are geometrically pointwise integral for $y \in
Y$; a fortiori the $f^{-1}(y)$ for $y \in Y$ are reduced preschemes, and since $A$ is integral (and a fortiori reduced),
one sees already that $B$ is reduced `(3.3.5)`. It remains to prove that $X = \operatorname{Spec}(B)$ is irreducible.
Now, the proof of `(7.9.8)` proves that $X'$ is locally integral (being locally Noetherian). Since the morphism $g' : X'
\to X$ is surjective, it therefore suffices to see that $X'$ is irreducible, or (since $X'$ is locally integral) that
$X'$ is connected. But it suffices for this to prove that the fibre $g'^{-1}(a)$ is connected. Indeed, if this point is
established, $X'$ cannot be the sum of two non-empty open preschemes `X_1`, `X_2`, for one would then have for example
$g'^{-1}(a) \cap X_{1} = \emptyset$; but the restriction $X_{2} \to X$ of $g'$ being proper (since `X_2` is a closed
sub-prescheme of $X'$), $g'(X_{2})$ would be a non-empty closed part of $X$ not containing the closed point $a$, which
is absurd. Now, one has $g'^{-1}(a) = g^{-1}(b) \otimes_{\mathit{k}(b)} \mathit{k}(a')$; but $g : Y' \to Y$ is proper
and birational, hence, in the Stein factorization $Y' \to Y'' \to Y$ of the morphism $g$ `(III, 4.3.3)`, the finite
morphism $u$ is also birational and consequently `Y''` is integral. Since $A$ is assumed geometrically unibranch, it
results then from `(III, 4.3.4)` that $g^{-1}(b)$ is geometrically connected, which finishes the proof.

**Remarks (7.9.10).**

<!-- label: IV.7.9.10 -->

*(i) We shall show further on `(18.8.11)` that in order that a reduced local ring $B$ be geometrically unibranch, it is
necessary and sufficient that for every étale morphism $h : X' \to X = \operatorname{Spec}(B)$ and every point $x' \in
X'$ above the closed point of $X$, $\mathcal{O}_{X', x'}$ be integral. One deduces from this that if, in `(7.9.9)`, one
supposes, not only that $\operatorname{Spec}(B \otimes_{A} k)$ is geometrically pointwise integral, but geometrically
unibranch, then one can conclude that $B$ is geometrically unibranch.*

<!-- original page 223 -->

*(ii) Let $X$, $Y$ be two excellent preschemes, $f : X \to Y$ a flat morphism, and suppose that for every finite
morphism $Y_{1} \to Y$, one can resolve $(Y_{1})_{red}$. It results from `(7.9.8)`, taking for $\mathbf{R}$ the property
of being regular, that the set $U$ of points $x \in X$ such that the fibre at the point $f(x)$ of the morphism*

```text
   Spec(𝒪_x ⊗_{𝒪_{f(x)}} 𝒌(f(x))) → Spec(𝒌(f(x)))
```

*be geometrically regular, is stable under generization. We do not know whether this set is open (or, what comes to the
same $(0_{III}, 9.2.5)$, whether it is constructible), even in the particular case where $Y$ is the spectrum of
$\mathbb{Z}$ or of a ring of polynomials in one indeterminate `k[T]` over a field $k$, and where consequently the
condition of "resolvability" imposed on $Y$ is trivially satisfied.*

*(To be continued.)*

[^1]: Cor. `(7.2.8)` is not used to prove `(7.4.4)`.

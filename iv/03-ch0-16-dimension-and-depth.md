<!-- original page 118 -->

## §16. Dimension and depth in Noetherian local rings

### 16.1. Dimension of a ring

**(16.1.1)** We call *dimension* (or *Krull dimension*) of a ring $A$, and denote $\dim(A)$, the (combinatorial)
dimension of its spectrum $\operatorname{Spec}(A)$ `(14.2.1)`; since the irreducible closed subsets of
$\operatorname{Spec}(A)$ are the $V(\mathfrak{p})$, where $\mathfrak{p}$ is a prime ideal of $A$
`(Bourbaki, Alg. comm., chap. II, §4, n° 3, cor. 1 of prop. 14)`, it amounts to the same thing to say that $\dim(A)$ is
the supremum of the lengths of chains `(14.1.1)`

$$ \mathfrak{p}_{0} \subset \mathfrak{p}_{1} \subset \cdots \subset \mathfrak{p}_{n} $$

of prime ideals of $A$. If $A \neq 0$, one has $\dim(A) \geq 0$. An Artinian ring $\neq 0$ (in particular a field) is of
dimension `0` `(Bourbaki, Alg. comm., chap. IV, §2, n° 5, prop. 7)`; a Dedekind ring which is not a field (in particular
$\mathbb{Z}$ or a polynomial ring `k[T]` in one indeterminate over a field $k$) is of dimension `1`
`(Bourbaki, Alg. comm., chap. VII, §2)`. A Noetherian ring is not necessarily of finite dimension `[30]`.

If $(\mathfrak{p}_{\alpha})$ is the family of minimal prime ideals of $A$, one has `(14.1.2.1)`

```text
(16.1.1.1)              dim(A) = sup_α dim(A/𝔭_α).
```

**(16.1.2)** For every ideal $\mathfrak{a}$ of $A$, the prime ideals of $A/\mathfrak{a}$ correspond bijectively to the
prime ideals of $A$ containing $\mathfrak{a}$, hence

$$ (16.1.2.1) \dim(A/\mathfrak{a}) \leq \dim(A). $$

If in addition $\mathfrak{a}$ is not contained in any minimal prime ideal $\mathfrak{p}_{\alpha}$ of $A$, every chain of
prime ideals of $A$ containing $\mathfrak{a}$ can be completed by one of the $\mathfrak{p}_{\alpha}$, so one has

$$ (16.1.2.2) 1 + \dim(A/\mathfrak{a}) \leq \dim(A). $$

<!-- original page 119 -->

**(16.1.3)** If $S$ is a multiplicative subset of $A$, the prime ideals of $S^{-1}A$ correspond bijectively to the prime
ideals of $A$ not meeting $S$, hence one has

$$ (16.1.3.1) \dim(S^{-1}A) \leq \dim(A). $$

For every prime ideal $\mathfrak{p}$ of $A$, one has, by definition `(14.2.1)`

```text
(16.1.3.2)              dim(A_𝔭) = codim(V(𝔭), Spec(A)).
```

This number is also called the *height* of the prime ideal $\mathfrak{p}$ and denoted $ht(\mathfrak{p})$. More
generally, for every ideal $\mathfrak{a}$ of $A$, we call *height* of $\mathfrak{a}$ the number

$$ (16.1.3.3) ht(\mathfrak{a}) = codim(V(\mathfrak{a}), \operatorname{Spec}(A)). $$

If $(\mathfrak{p}_{\lambda})$ is the family of prime ideals minimal among those that contain $\mathfrak{a}$, one has
therefore `(14.2.1)`

$$ (16.1.3.4) ht(\mathfrak{a}) = \inf_{\lambda} ht(\mathfrak{p}_{\lambda}). $$

One has evidently

```text
(16.1.3.5)              dim(A) = sup_𝔪 dim(A_𝔪)
```

where $\mathfrak{m}$ ranges over the set of maximal ideals of $A$.

**(16.1.4)** For every prime ideal $\mathfrak{p}$ of $A$, one has `(14.2.2.2)`

```text
(16.1.4.1)              dim(A_𝔭) + dim(A/𝔭) ≤ dim(A).
```

We say that $A$ is *catenary* (resp. *equidimensional*, *equicodimensional*, *biequidimensional*) when
$\operatorname{Spec}(A)$ is catenary (resp. equidimensional, equicodimensional, biequidimensional). When $A$ is
Noetherian and biequidimensional, the two sides of `(16.1.4.1)` are equal for every prime ideal of $A$ `(14.3.5)`.

For every ideal $\mathfrak{a}$ of $A$, the prime ideals of $A/\mathfrak{a}$ correspond bijectively to the prime ideals
of $A$ containing $\mathfrak{a}$, so, if $A$ is catenary, so is $A/\mathfrak{a}$. Likewise, for every multiplicative
subset $S$ of $A$, the prime ideals of $S^{-1}A$ correspond bijectively to the prime ideals of $A$ not meeting $S$, so
if $A$ is catenary, so is $S^{-1}A$.

In addition, since the prime ideals of $A$ contained in a prime ideal $\mathfrak{p}$ correspond bijectively to the prime
ideals of $A_{\mathfrak{p}}$, for $A$ to be catenary it is necessary and sufficient that $A_{\mathfrak{p}}$ be so for
every $\mathfrak{p}$. To say that $A$ is catenary therefore means (`(14.3.2)` and `(16.1.3.2)`) that for every pair of
prime ideals $\mathfrak{p}$, $\mathfrak{q}$ of $A$ such that $\mathfrak{q} \subset \mathfrak{p}$, one has

```text
(16.1.4.2)              dim(A_𝔮) + dim(A_𝔭 / 𝔮 A_𝔭) = dim(A_𝔭).
```

If $A$ is biequidimensional, so is $A_{\mathfrak{p}}$ for every prime ideal $\mathfrak{p}$ of $A$.

**Proposition (16.1.5).**

<!-- label: 0_IV.16.1.5 -->

*Let $\rho : A \to B$ be a ring homomorphism making $B$ an $A$-algebra integral over $A$. Then one has $\dim(B) \leq
\dim(A)$; if in addition $\rho$ is injective, one has $\dim(B) = \dim(A)$.*

<!-- original page 120 -->

If $\mathfrak{n}$ is the kernel of $\rho$, $\rho(A)$ is isomorphic to $A/\mathfrak{n}$, so $\dim(\rho(A)) \leq \dim(A)$
by `(16.1.2.1)`, and since $B$ is integral over $\rho(A)$, one may restrict oneself to proving the second assertion when
$A \subset B$. If $\mathfrak{p}_{0} \subset \mathfrak{p}_{1} \subset \cdots \subset \mathfrak{p}_{n}$ is a chain of
prime ideals of $B$, the $\mathfrak{p}_{i} \cap A$ are then distinct prime ideals in $A$
`(Bourbaki, Alg. comm., chap. V, §2, n° 1, cor. 1 of prop. 1)`, hence form a chain of prime ideals. Conversely, for
every chain $\mathfrak{p}_{0} \subset \mathfrak{p}_{1} \subset \cdots \subset \mathfrak{p}_{n}$ of prime ideals of $A$,
one knows that there exists for each $i$ a prime ideal $\mathfrak{p}'_{i}$ of $B$ such that $\mathfrak{p}'_{i} \cap A =
\mathfrak{p}_{i}$ and that $\mathfrak{p}'_{i} \subset \mathfrak{p}'_{i+1}$ for $0 \leq i \leq n - 1$
`(loc. cit., cor. 2 of th. 1)`. Whence the conclusion.

**Proposition (16.1.6).**

<!-- label: 0_IV.16.1.6 -->

*Let $B$ be an integral ring, $A$ a local subring of $B$, $\mathfrak{m}$ its maximal ideal. Suppose that $A$ is
integrally closed and that $B$ is integral over $A$; then, for every maximal ideal $\mathfrak{n}$ of $B$, one has
$\dim(B_{\mathfrak{n}}) = \dim(A)$.*

The first part of the reasoning of `(16.1.5)` shows that $\dim(B_{\mathfrak{n}}) \leq \dim(A)$. Conversely, consider a
chain of prime ideals $\mathfrak{p}_{0} \subset \mathfrak{p}_{1} \subset \cdots \subset \mathfrak{p}_{n} = \mathfrak{m}$
of $A$; one knows that $\mathfrak{n} \cap A = \mathfrak{m}$ `(Bourbaki, Alg. comm., chap. V, §2, n° 1, prop. 1)` and by
virtue of the hypotheses made, one may apply the second Cohen-Seidenberg theorem
`(Bourbaki, Alg. comm., chap. V, §2, n° 4, th. 3)`, which proves the existence of a chain of prime ideals
$\mathfrak{p}'_{0} \subset \mathfrak{p}'_{1} \subset \cdots \subset \mathfrak{p}'_{n} = \mathfrak{n}$ of $B$ such that
$\mathfrak{p}'_{i} \cap A = \mathfrak{p}_{i}$ for every $i$; one deduces at once that $\dim(B_{\mathfrak{n}}) \geq
\dim(A)$, whence the proposition.

**(16.1.7)** Let $M$ be an $A$-module; we call *dimension* of $M$, and denote $\dim_{A}(M)$ or $\dim(M)$, the dimension
of the ring $A/Ann(M)$ (isomorphic to the ring `A_M` of homotheties of $M$). One has therefore $\dim(M^{k}) = \dim(M)$
for every $k > 0$. If $M$ is of finite type, the prime ideals of $A$ containing $Ann(M)$ are exactly those belonging to
$Supp(M)$ $(0_{I}, 1.7.4)$ and the latter is closed in $\operatorname{Spec}(A)$, hence one has then

```text
(16.1.7.1)              dim(M) = dim(Supp(M)) ≤ dim(A).
```

If $M$, $N$ are two $A$-modules such that $N \subset M$, one has

```text
(16.1.7.2)              dim(N) ≤ dim(M),         dim(M/N) ≤ dim(M).
```

If $S$ is a multiplicative subset of $A$ and if $M$ is of finite type, one has

$$ (16.1.7.3) \dim_{S^{-1}A}(S^{-1}M) \leq \dim_{A}(M). $$

Indeed, one has $Ann(S^{-1}M) = S^{-1}(Ann(M))$ `(Bourbaki, Alg. comm., chap. II, §2, n° 4)` and $S^{-1}A /
S^{-1}(Ann(M)) \cong S^{-1}(A / Ann(M))$.

On the other hand, every maximal chain of prime ideals containing $Ann(M)$ ends at a maximal ideal $\mathfrak{m}$, so
its length is equal to that of the chain of corresponding prime ideals of $A_{\mathfrak{m}}$ (which contain
$Ann(M_{\mathfrak{m}}) = (Ann(M))_{\mathfrak{m}}$); from this remark and from `(16.1.7.3)`, one obtains

```text
(16.1.7.4)              dim_A(M) = sup_𝔪 dim_{A_𝔪}(M_𝔪)
```

<!-- original page 121 -->

where $\mathfrak{m}$ ranges over the set of maximal ideals of $A$.

We say that $M$ is *catenary* (resp. *equidimensional*, *equicodimensional*, *biequidimensional*) when $A/Ann(M)$ is.

**Proposition (16.1.8).**

<!-- label: 0_IV.16.1.8 -->

*Let $A$ be a ring, $M$ an $A$-module of finite type, $\mathfrak{p}$ a prime ideal of $A$. One has then*

```text
(16.1.8.1)              dim_{A_𝔭}(M_𝔭) + dim_A(M/𝔭M) ≤ dim_A(M).
```

One has $Ann(M_{\mathfrak{p}}) = (Ann(M))_{\mathfrak{p}}$, hence the prime ideals of $A_{\mathfrak{p}}$ containing
$Ann(M_{\mathfrak{p}})$ correspond bijectively to the prime ideals of $A$ containing $Ann(M)$ and contained in
$\mathfrak{p}$. On the other hand, if $Ann(M) = \mathfrak{n}$, $V(Ann(M/\mathfrak{p}M)) = V(\mathfrak{p} +
\mathfrak{n})$ $(0_{I}, 1.7.5)$, hence the prime ideals of $A$ containing $Ann(M/\mathfrak{p}M)$ contain $\mathfrak{p} +
\mathfrak{n}$; whence the conclusion.

This last remark shows in addition that one has

$$ (16.1.8.2) \dim_{A/\mathfrak{p}}(M/\mathfrak{p}M) = \dim_{A}(M/\mathfrak{p}M). $$

**Proposition (16.1.9).**

<!-- label: 0_IV.16.1.9 -->

*Let $A$ be a Noetherian ring, $\rho : A \to B$ a ring homomorphism, $M$ a $B$-module such that $M_{[\rho]}$ is an
$A$-module of finite type. Then one has*

$$ (16.1.9.1) \dim_{A}(M_{[\rho]}) = \dim_{B}(M). $$

Indeed, the ring `B_M` of homotheties of the $B$-module $M$ identifies with a subring of $C =
\operatorname{End}_{A}(M_{[\rho]})$, and $C$ is an $A$-module of finite type
`(Bourbaki, Alg. comm., chap. III, §3, n° 1, lemma 2)`, hence so is `B_M`; moreover the ring `A_M` of homotheties of the
$A$-module $M_{[\rho]}$ is a subring of `B_M`, canonical image of $A$ in $C$, hence `B_M` is finite over `A_M`; the
conclusion thus results from `(16.1.5)`.

**(16.1.10)** Let $A$ be a Noetherian ring; if $M$ is an $A$-module of finite length, one knows
`(Bourbaki, Alg. comm., chap. IV, §2, n° 5, prop. 7 and cor. 1 of prop. 7)` that $Supp(M)$ is a finite discrete space,
hence $\dim(M) = 0$ if $M \neq 0$; conversely, if $M$ is an $A$-module of finite type such that $\dim(M) = 0$, every
point of $Supp(M)$ is closed, in other words is a maximal ideal of $A$, hence `(loc. cit., prop. 7)` $M$ is of finite
length.

### 16.2. Dimension of a Noetherian semi-local ring ¹

**(16.2.1)** Let $A$ be a Noetherian semi-local ring, $\mathfrak{r}$ its radical; recall that an *ideal of definition*
$\mathfrak{q}$ of $A$ is an ideal such that $\mathfrak{q} \subset \mathfrak{r}$ and that $\mathfrak{q}$ contains a power
of $\mathfrak{r}$; it amounts to the same thing to say that the only prime ideals containing $\mathfrak{q}$ are maximal,
or that $A/\mathfrak{q}$ is an Artinian ring. Let $M$ be an $A$-module of finite type; for every integer $n > 0$,
$M/\mathfrak{q}^{n} M$ is an $A$-module of finite length, equal to $\sum^{n-1}_{i=0} long(gr_{i}(M))$, where
$gr_{\bullet}(M)$ is the graded $(A/\mathfrak{q})$-module associated with $M$ endowed with the $\mathfrak{q}$-preadic
filtration. One knows that there exists a polynomial $Q(n)$ with rational coefficients such that $long(gr_{n}(M)) =
Q(n)$ for $n$ large enough `(III, 2.5.4)`; one deduces at once from this that there exists *a polynomial
$P_{\mathfrak{q}}(M, n)$ in $n$, with rational coefficients, such that $long(M/\mathfrak{q}^{n} M) = P_{\mathfrak{q}}(M,
n)$ for $n$ large enough*; it is clear that this polynomial is unique and that its leading coefficient is `> 0` if $M
\neq 0$; one says that it is the *Hilbert-Samuel polynomial* of $M$ for the $\mathfrak{q}$-preadic filtration.

______________________________________________________________________

¹ This number reproduces the exposition given by Serre in a course at the Collège de France in 1958.

<!-- original page 122 -->

**Lemma (16.2.2.1).**

<!-- label: 0_IV.16.2.2.1 -->

*Let $(M_{n})$ be a $\mathfrak{q}$-good filtration of $M$ `(Bourbaki, Alg. comm., chap. III, §3, n° 1)`; then
$long(M/M_{n})$ is equal, for $n$ large, to a polynomial in $n$ whose degree and leading coefficient are the same as
those of $P_{\mathfrak{q}}(M, n)$.*

Indeed, there exists $n_{0}$ such that $M_{n+1} = \mathfrak{q} M_{n}$ for $n \geq n_{0}$, whence the inclusions
$\mathfrak{q}^{n+n_{0}} M \subset M_{n+n_{0}} = \mathfrak{q}^{n} M_{n_{0}} \subset \mathfrak{q}^{n} M \subset M_{n}$ for
$n$ large, which entails

```text
            P_𝔮(M, n + n_0) ≥ long(M/M_{n+n_0}) ≥ P_𝔮(M, n) ≥ long(M/M_n)
```

and consequently the conclusion.

If $\mathfrak{q}'$ is a second ideal of definition, one has $\mathfrak{q}' \supset \mathfrak{q}^{m}$ for some integer
$m$, hence $P_{\mathfrak{q}'}(M, n) \leq P_{\mathfrak{q}}(M, mn)$; consequently the degree of $P_{\mathfrak{q}}(M, n)$
does not depend on the ideal of definition $\mathfrak{q}$ considered; one denotes it $d(M)$.

**Lemma (16.2.2.2).**

<!-- label: 0_IV.16.2.2.2 -->

*Let $0 \to M' \to M \to M'' \to 0$ be an exact sequence of $A$-modules of finite type. Then the polynomial
$P_{\mathfrak{q}}(M, n) - P_{\mathfrak{q}}(M', n) - P_{\mathfrak{q}}(M'', n)$ has degree $\leq d(M') - 1 \leq d(M) -
1$.*

Indeed, the filtration of the $M'_{n} = M' \cap \mathfrak{q}^{n} M$ is $\mathfrak{q}$-good
`(Bourbaki, Alg. comm., chap. III, §3, n° 1, prop. 1)`; since `long(M/𝔮^n M) = long(M''/𝔮^n M'') + long(M'/M'_n)`, the
lemma follows at once from `(16.2.2.1)` applied to $M'$.

**Theorem (16.2.3) (Krull-Chevalley-Samuel).**

<!-- label: 0_IV.16.2.3 -->

*Let $A$ be a Noetherian semi-local ring, $\mathfrak{r}$ its radical, $M \neq 0$ an $A$-module of finite type, $d(M)$
the degree of the Hilbert-Samuel polynomial of $M$ (for an arbitrary ideal of definition of $A$); let on the other hand
$s(M)$ be the infimum of the integers $n$ such that there exist elements $x_{1}, \cdots, x_{n}$ of $\mathfrak{r}$ for
which $M/(x_{1} M + \cdots + x_{n} M)$ is of finite length. Then one has*

$$ d(M) = s(M) = \dim(M). $$

**Lemma (16.2.3.1).**

<!-- label: 0_IV.16.2.3.1 -->

*For every $x \in \mathfrak{r}$, let ${}_{x} M$ be the submodule of $M$ formed of the elements annihilated by $x$.
Then:*

*(i) One has $s(M) \leq s(M/_{x} M) + 1$.*

*(ii) Let $\mathfrak{p}_{i}$ be the prime ideals belonging to $Supp(M)$ and such that*

```text
                        dim(A/𝔭_i) = dim(M)            (1 ≤ i ≤ m).
```

*If $x \notin \mathfrak{p}_{i}$ for every $i$, one has $\dim(M/xM) \leq \dim(M) - 1$.*

*(iii) If $\mathfrak{q}$ is an ideal of definition of $A$, the polynomial*

```text
                        P_𝔮(M, n) − P_𝔮(M/xM, n)
```

*is of degree $\leq d(M) - 1$.*

Assertion (i) is trivial, since if $(x_{i})_{1 \leq i \leq r}$ is such that for the module $N = M/_{x} M$, $N/(x_{1} N +
\cdots + x_{r} N)$ is of finite length, it suffices to observe that this module is isomorphic to $M/(xM + x_{1} M +
\cdots + x_{r} M)$.

To prove (ii), one observes that, if $\mathfrak{a}$ is the annihilator of $M$, the prime ideals containing the
annihilator of $M/xM$ are those that contain $\mathfrak{a} + Ax$ $(0_{I}, 1.7.5)$; none of the $\mathfrak{p}_{i}$ can
therefore contain $\mathfrak{a} + Ax$, and by definition of $\dim(M)$ `(16.1.7)` every chain of prime ideals containing
$\mathfrak{a} + Ax$ therefore has length $\leq \dim(M) - 1$.

<!-- original page 123 -->

Finally, to prove (iii), one notes that one has two exact sequences

```text
            0 → _x M → M --x→ xM → 0,        0 → xM → M → M/xM → 0
```

and the assertion follows at once from lemma `(16.2.2.2)`.

The proof of `(16.2.3)` is done in three steps:

**(16.2.3.2)** *One has $\dim(M) \leq d(M)$.*

We reason by induction on $d(M)$, the case $d(M) = 0$ being trivial. Suppose then $d(M) \geq 1$, and let
$\mathfrak{p}_{0} \in Supp(M)$ be such that $\dim(A/\mathfrak{p}_{0}) = \dim(M)$. This entails that $\mathfrak{p}_{0}$
is a minimal element of $Supp(M)$, hence it is associated with $M$ `(Bourbaki, Alg. comm., chap. IV, §1, n° 4, th. 2)`
and $M$ consequently contains a submodule $N$ isomorphic to $A/\mathfrak{p}_{0}$ `(loc. cit., §1, n° 1)`; since
$d(M) \geq d(N)$ by `(16.2.2.2)`, one is reduced to proving that $\dim(N) \leq d(N)$. Let then
$\mathfrak{p}_{0} \subset \mathfrak{p}_{1} \subset \cdots \subset \mathfrak{p}_{n}$ be a chain of distinct prime ideals
in $A$, and let us show that $n \leq d(N)$. This is evident if $n = 0$. Otherwise, there exists
$x \in \mathfrak{p}_{1} \cap \mathfrak{r}$ such that $x \notin \mathfrak{p}_{0}$, for the relation
$\mathfrak{p}_{0} \supset \mathfrak{p}_{1} \cap \mathfrak{r}$ would entail $\mathfrak{p}_{0} \supset \mathfrak{r}$ since
$\mathfrak{p}_{0}$ does not contain $\mathfrak{p}_{1}$, hence $\mathfrak{p}_{0}$ would be maximal, which is absurd. One
has $\mathfrak{p}_{i} \in Supp(N/xN)$ for $i \geq 1$, hence $n - 1 \leq \dim(N/xN)$ `(16.1.7)`. Since ${}_{x} N = 0$ by
virtue of the choice of $x$, one has $d(N/xN) \leq d(N) - 1$ by `(16.2.3.1, (iii))`. The induction hypothesis then
implies $d(N/xN) = \dim(N/xN) \geq n - 1$, hence $n - 1 \leq d(N) - 1$.

**(16.2.3.3)** *One has $d(M) \leq s(M)$.*

Let indeed $(x_{i})_{1 \leq i \leq n}$ be a family of elements of $\mathfrak{r}$ such that, on setting $\mathfrak{a} =
x_{1} A + \cdots + x_{n} A$, $M/\mathfrak{a}M$ is of finite length. The ideals associated with $M/\mathfrak{a}M$ are
then maximal `(Bourbaki, Alg. comm., chap. IV, §2, n° 5, prop. 7)` and since these are the only prime ideals containing
$\mathfrak{q} = \mathfrak{a} + (\mathfrak{r} \cap Ann(M))$, $A/\mathfrak{q}$ is Artinian `(loc. cit., prop. 9)` and
$\mathfrak{q}$ is an ideal of definition of $A$. But one has $\mathfrak{q}^{m} M / \mathfrak{q}^{m+1} M =
\mathfrak{a}^{m} M / \mathfrak{a}^{m+1} M$, and if $M$ is generated by $r$ elements $y_{j}$, $\mathfrak{a}^{m} M /
\mathfrak{a}^{m+1} M$ is an $(A/\mathfrak{q})$-module generated by the canonical images of the $x^{k_{1}}_{1}
x^{k_{2}}_{2} \cdots x^{k_{n}}_{n} y_{j}$ where $\sum k_{i} = m$, hence by $r\cdot(\binom{m+n-1}{n-1})$ elements; its
length is consequently $\leq \alpha\cdot\binom{m+n-1}{n-1}$, where $\alpha$ is a constant, and one deduces at once that
the degree of $P_{\mathfrak{q}}(M, n)$ is $\leq n$; whence $d(M) \leq s(M)$.

**(16.2.3.4)** *One has $s(M) \leq \dim(M)$.*

Let us first note that $n = \dim(M)$ is finite by `(16.2.3.2)`. We reason by induction on $n$; the proposition is
evident for $n = 0$, since $M$ is then of finite length `(16.1.10)`. Suppose $n \geq 1$, and let $\mathfrak{p}_{i}$ ($1
\leq i \leq m$) be the prime ideals of $Supp(M)$ such that $\dim(A/\mathfrak{p}_{i}) = n$; the definition of the
$\mathfrak{p}_{i}$ shows that they are minimal elements of $Supp(M)$, hence finite in number
`(Bourbaki, Alg. comm., chap. IV, §1, n° 4, th. 2)`. Since $n \geq 1$, the $\mathfrak{p}_{i}$ are not maximal, and there
exists therefore $x \in \mathfrak{r}$ such that $x \notin \mathfrak{p}_{i}$ for every $i$
`(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`. By virtue of `(16.2.3.1)`, one has $s(M) \leq s(M/xM) + 1$ and
$\dim(M) \geq \dim(M/xM) + 1$; the induction hypothesis entails that $s(M/xM) \leq \dim(M/xM)$, whence the conclusion.

**Corollary (16.2.4).**

<!-- label: 0_IV.16.2.4 -->

*Under the hypotheses of `(16.2.3)`, one has*

$$ (16.2.4.1) \dim_{A}(M) = \dim_{\hat{A}}(\hat{M}). $$

<!-- original page 124 -->

Indeed, $M/\mathfrak{r}^{n} M$ and $\hat{M}/\hat{\mathfrak{r}}^{n} \hat{M}$ are isomorphic, hence $d(M) = d(\hat{M})$.

**Corollary (16.2.5).**

<!-- label: 0_IV.16.2.5 -->

*The dimension of a Noetherian semi-local ring $A$ is finite and equal to the minimum number of elements of the radical
of $A$ generating an ideal of definition.*

This is the equality $s(M) = \dim(M)$ for $M = A$.

In particular:

**Corollary (16.2.6).**

<!-- label: 0_IV.16.2.6 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $k = A/\mathfrak{m}$ its residue field; one has*

$$ (16.2.6.1) \dim(A) \leq rg_{k}(\mathfrak{m}/\mathfrak{m}^{2}). $$

Indeed, one knows that if the $x_{i}$ ($1 \leq i \leq n$) are elements of $\mathfrak{m}$ whose classes mod
$\mathfrak{m}^{2}$ form a basis of the $k$-vector space $\mathfrak{m}/\mathfrak{m}^{2}$, the $x_{i}$ generate
$\mathfrak{m}$ `(Bourbaki, Alg. comm., chap. II, §3, n° 2, cor. 2 of prop. 4)`.

**Proposition (16.2.7).**

<!-- label: 0_IV.16.2.7 -->

*Let $k$ be a field, $B$ a graded $k$-algebra of finite type with positive degrees generated by its homogeneous elements
of degree `1` and such that $B_{0} = k$; let $E$ be a graded $B$-module of finite type, so that `(III, 2.5.4)`, for $n$
large enough, $rg_{k}(E_{n}) = r(n)$ is of the form $\Phi(n) - \Phi(n - 1)$, where $\Phi$ is a polynomial in $n$ of
degree $d$. Then there exists in $B$ a family $(t_{i})_{1 \leq i \leq d}$ of $d$ homogeneous elements of degrees $\geq
1$ such that $E/(\sum_{i} t_{i} E)$ is of finite rank over $k$.*

Let $\mathfrak{q}$ be the maximal ideal $\bigoplus_{n \geq 1} B_{n}$ of $B$, and, for every $n$, let $E^{n}$ be the
sub-$B$-module $\bigoplus_{h \geq n+1} E_{h}$ of $E$. Every element of $B - \mathfrak{q}$ determines an injective
homothety in the Artinian $B$-module $E/E^{n}$, and this homothety is therefore bijective
`(Bourbaki, Alg., chap. VIII, §2, n° 2, lemma 3)`, which entails that $(E/E^{n})_{\mathfrak{q}}$ identifies with
$E/E^{n}$; since the residue field of $B_{\mathfrak{q}}$ is $k$, one deduces from the hypothesis that
$long_{B_{\mathfrak{q}}}((E/E^{n})_{\mathfrak{q}})$ is a polynomial in $n$ of degree $d$. On the other hand, since $E$
is a $B$-module of finite type and $B$ is generated by its homogeneous elements of degree `1`, the filtration $(E^{n})$
on $E$ is $\mathfrak{q}$-good `(Bourbaki, Alg. comm., chap. III, §1, n° 3, lemma 1)`, hence the filtration
$((E^{n})_{\mathfrak{q}})$ on $E_{\mathfrak{q}}$ is $\mathfrak{q} B_{\mathfrak{q}}$-good. Since $B_{\mathfrak{q}}$ is a
Noetherian local ring, one concludes from `(16.2.3)` and `(16.2.2.1)` that one has $\dim(E_{\mathfrak{q}}) = d$. We then
reason by induction on $d$, the lemma being evident if $d = 0$. Suppose $d \geq 1$, and observe that the minimal prime
ideals $\mathfrak{p}_{i}$ ($1 \leq i \leq r$) in $Ass(E)$ are graded
`(Bourbaki, Alg. comm., chap. IV, §3, n° 1, prop. 1)`, and that $\mathfrak{q}$ is distinct from the union of the
$\mathfrak{p}_{i}$ since $d \geq 1$; there is therefore a homogeneous element $t_{1} \in \mathfrak{q}$ not belonging to
any of the $\mathfrak{p}_{i}$ `(Bourbaki, Alg. comm., chap. III, §1, n° 4, prop. 8)`. Since the prime ideals
$(\mathfrak{p}_{i})_{\mathfrak{q}}$ are the minimal elements of $Ass(E_{\mathfrak{q}})$
`(Bourbaki, Alg. comm., chap. IV, §1, n° 2, prop. 5)`, one has $\dim(E_{\mathfrak{q}} / t_{1} E_{\mathfrak{q}}) = d - 1$
`(16.3.4)`. It then suffices to apply the induction hypothesis to the graded $B$-module $E/t_{1} E$ to obtain the
conclusion.

### 16.3. Systems of parameters in a Noetherian local ring

**Proposition (16.3.1).**

<!-- label: 0_IV.16.3.1 -->

*Let $A$ be a Noetherian ring, $\mathfrak{p}$ a prime ideal of $A$, $n$ an integer. The following conditions are
equivalent:*

*a) $ht(\mathfrak{p}) = \dim(A_{\mathfrak{p}}) \leq n$;*

*b) there exist $n$ elements $x_{i}$ of $A$ ($1 \leq i \leq n$) such that $\mathfrak{p}$ is minimal in the set of prime
ideals containing the ideal $\mathfrak{a}$ generated by the $x_{i}$ (in other words $V(\mathfrak{p})$ is an irreducible
component of $V(\mathfrak{a})$).*

Condition b) entails that $\mathfrak{a} A_{\mathfrak{p}}$ is an ideal of definition of $A_{\mathfrak{p}}$, whence a) by
virtue of `(16.2.5)`. Conversely, if a) is satisfied, there exists an ideal of definition $\mathfrak{b}$ of
$A_{\mathfrak{p}}$ generated by $n$ elements $x_{i}/s$, with $s \in A - \mathfrak{p}$. By virtue of the bijective
correspondence between prime ideals of $A_{\mathfrak{p}}$ and prime ideals of $A$ contained in $\mathfrak{p}$, the ideal
$\mathfrak{a}$ of $A$ generated by the $x_{i}$ satisfies b).

<!-- original page 125 -->

For $n = 1$, one obtains the particular case:

**Corollary (16.3.2) (Hauptidealsatz).**

<!-- label: 0_IV.16.3.2 -->

*For a prime ideal in a Noetherian ring to be of height $\leq 1$, it is necessary and sufficient that it be minimal in
the set of prime ideals containing a suitable principal ideal.*

**Corollary (16.3.3) (Artin-Tate).**

<!-- label: 0_IV.16.3.3 -->

*Let $A$ be a Noetherian integral ring. The following conditions are equivalent:*

*a) $A$ is a semi-local ring of dimension $\leq 1$.*

*b) There exists $f \neq 0$ in $A$ such that $A_{f}$ is a field.*

Condition a) is equivalent to saying that $A$ has only a finite number of prime ideals $\mathfrak{m}_{i} \neq 0$, and
that these ideals are all maximal (`0` being a prime ideal). Since the product of the $\mathfrak{m}_{i}$ is not zero, as
$A$ is integral, an element $f \neq 0$ of this product belongs to all the $\mathfrak{m}_{i}$, hence `(0)` is the only
prime ideal of the integral ring $A_{f}$, in other words $A_{f}$ is a field. (One notes that this part of the proof does
not use the fact that $A$ is Noetherian.) Let us now prove that b) entails a); the hypothesis b) means that every prime
ideal $\mathfrak{p} \neq 0$ of $A$ contains $f$. Let $\mathfrak{p}_{i}$ ($1 \leq i \leq n$) be the prime ideals minimal
among those that contain $f$ (which are finite in number since $A/fA$ is Noetherian); it suffices to prove that the
$\mathfrak{p}_{i}$ are maximal ideals, for then every prime ideal $\neq 0$ necessarily contains one of the
$\mathfrak{p}_{i}$, hence is equal to it. Suppose then that there exists a maximal ideal $\mathfrak{m}$ containing one
of the $\mathfrak{p}_{i}$ and distinct from the $\mathfrak{p}_{i}$; $\mathfrak{m}$ is then not contained in the union of
the $\mathfrak{p}_{i}$ `(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`, in other words there exists $g \in
\mathfrak{m}$ not belonging to any of the $\mathfrak{p}_{i}$. Let $\mathfrak{q}$ be one of the prime ideals minimal
among those that contain $g$; it follows from the Hauptidealsatz `(16.3.2)` that $\mathfrak{q}$ is of height `1`, hence
$\neq 0$; consequently it contains $f$, hence also one of the $\mathfrak{p}_{i}$, and since $g \in \mathfrak{q}$ and $g$
belongs to no $\mathfrak{p}_{i}$, $\mathfrak{q}$ is distinct from the $\mathfrak{p}_{i}$; it would therefore be of
height $\geq 2$, which is contradictory.

**Proposition (16.3.4).**

<!-- label: 0_IV.16.3.4 -->

*Let $A$ be a Noetherian semi-local ring, $\mathfrak{r}$ its radical, $M$ an $A$-module of finite type,
$\mathfrak{p}_{i}$ the elements of $Supp(M)$ such that $\dim(A/\mathfrak{p}_{i}) = \dim(M)$. Then the $\mathfrak{p}_{i}$
are minimal elements of $Ass(M)$, and one has $\dim(M/\mathfrak{p}_{i} M) = \dim(M)$. For every $x \in \mathfrak{r}$,
one has*

$$ (16.3.4.1) \dim(M/xM) \geq \dim(M) - 1. $$

*In addition, for the two sides of `(16.3.4.1)` to be equal, it is necessary and sufficient that $x$ not belong to any
of the $\mathfrak{p}_{i}$.*

The first assertion is immediate, for the $\mathfrak{p}_{i}$ are by definition minimal elements of $Supp(M)$ `(16.1.6)`,
and the latter are also minimal elements of $Ass(M)$ `(Bourbaki, Alg. comm., chap. IV, §1, n° 4, th. 2)`. In addition,
$Supp(M/\mathfrak{p}_{i} M)$ is the set of prime ideals containing $\mathfrak{p}_{i}$ $(0_{I}, 1.7.5)$, hence
`dim(M/𝔭_i M) = dim(A/𝔭_i) = dim(M)`.

Set $N = M/xM$. If $y_{1}, \cdots, y_{r}$ are elements of $\mathfrak{r}$ such that $N/(y_{1} N + \cdots + y_{r} N)$ is
of finite length, this means that $M/(xM + y_{1} M + \cdots + y_{r} M)$ is of finite length, whence the inequality
`(16.3.4.1)` by virtue of `(16.2.3)`.

The fact that the two sides of `(16.3.4.1)` are equal when $x$ does not belong to any of the $\mathfrak{p}_{i}$ results
from `(16.3.4.1)` and from `(16.2.3.1)`. Conversely, if

<!-- original page 126 -->

$\dim(M/xM) = \dim(M) - 1$, none of the $\mathfrak{p}_{i}$ can belong to $Supp(M/xM)$, and the prime ideals of this
support are those that contain $Ann(M) + Ax$; since the $\mathfrak{p}_{i}$ contain $Ann(M)$, they cannot contain $x$.

**Corollary (16.3.5).**

<!-- label: 0_IV.16.3.5 -->

*With the notations of `(16.3.4)`, for every ideal $\mathfrak{a} \subset \mathfrak{p}_{i}$, one has
$\dim(M/\mathfrak{a}M) = \dim(M)$ and if one sets $N = M/\mathfrak{a}M$, the relation $\dim(M/xM) = \dim(M) - 1$ entails
$\dim(N/xN) = \dim(N) - 1$.*

Indeed, $Supp(N)$ is the set of prime ideals containing $\mathfrak{a} + Ann(M)$, hence $\mathfrak{p}_{i}$ belongs to
$Supp(N)$ and since `dim(N) ≤ dim(M) = dim(A/𝔭_i)`, one has $\dim(A/\mathfrak{p}_{i}) = \dim(N)$; in addition the prime
ideals $\mathfrak{q} \in Supp(N)$ such that $\dim(A/\mathfrak{q}) = \dim(N)$ are some of the $\mathfrak{p}_{j}$; if $x$
does not belong to any of the $\mathfrak{p}_{j}$, one has therefore $\dim(N/xN) = \dim(N) - 1$ by virtue of `(16.3.4)`.

**Definition (16.3.6).**

<!-- label: 0_IV.16.3.6 -->

*Let $A$ be a Noetherian semi-local ring, $\mathfrak{r}$ its radical, $M$ an $A$-module of finite type, and set $n =
\dim(M)$. We call **system of parameters for $M$** any system $(x_{i})_{1 \leq i \leq n}$ of $n$ elements of
$\mathfrak{r}$ such that $M/(x_{1} M + \cdots + x_{n} M)$ is of finite length.*

It has been seen `(16.2.3)` that such systems always exist.

It has been seen in the course of the proof of `(16.2.3.3)` that if $\mathfrak{j} = \sum_{i} x_{i} A$ is such that
$M/\mathfrak{j}M$ is of finite length, $\mathfrak{q} = \mathfrak{j} + Ann(M)$ is an ideal of definition of $A$, and
conversely, if this is so, $M/\mathfrak{q}^{n} M$ is a module of finite type over the Artinian ring $A/\mathfrak{q}$,
hence is of finite length. It therefore amounts to the same to say that $(x_{i})_{1 \leq i \leq n}$ is a system of
parameters for $M$ or for $A/Ann(M)$ (or again that their images in $A/Ann(M)$ form a system of parameters for this
ring). If $(x_{i})_{1 \leq i \leq n}$ is a system of parameters for $M$, so is $(x^{k}_{i})$ for every integer $k \geq
1$, since one may restrict oneself, by virtue of what precedes, to the case where $M = A$, and if $\mathfrak{j}$ is an
ideal of definition of $A$, the ideal $\sum^{n}_{i=1} x^{k}_{i} A$ contains $\mathfrak{j}^{kn}$, hence is also an ideal
of definition.

**Proposition (16.3.7).**

<!-- label: 0_IV.16.3.7 -->

*Let $A$ be a Noetherian semi-local ring, $\mathfrak{r}$ its radical, $x_{1}, \cdots, x_{k}$ elements of $\mathfrak{r}$,
$M$ an $A$-module of finite type. One has then*

```text
(16.3.7.1)              dim(M/(x_1 M + ⋯ + x_k M)) ≥ dim(M) − k.
```

*In addition, for the two sides of `(16.3.7.1)` to be equal, it is necessary and sufficient that there exist elements
$x_{i}$ ($k + 1 \leq i \leq n = \dim(M)$) of $\mathfrak{r}$ such that $(x_{i})_{1 \leq i \leq n}$ is a system of
parameters for $M$.*

The inequality `(16.3.7.1)` results from `(16.3.4.1)` by induction on $k$. If the two sides of `(16.3.7.1)` are equal,
and if $x_{k+1}, \cdots, x_{n}$ is a system of parameters for $M/(x_{1} M + \cdots + x_{k} M)$, it is clear that
$M/(x_{1} M + \cdots + x_{k} M + x_{k+1} M + \cdots + x_{n} M)$ is of finite length, hence $(x_{i})_{1 \leq i \leq n}$
is a system of parameters for $M$; conversely, if there exist $x_{i}$ ($k + 1 \leq i \leq n$) having this property and
if one sets $N = M/(x_{1} M + \cdots + x_{k} M)$, it is clear that $N/(x_{k+1} N + \cdots + x_{n} N)$ is of finite
length, hence $\dim(N) \leq n - k$, and the two sides are equal by virtue of `(16.3.7.1)`.

<!-- original page 127 -->

**Proposition (16.3.8).**

<!-- label: 0_IV.16.3.8 -->

*Let $A$ be a Noetherian semi-local ring, $X = \operatorname{Spec}(A)$ its spectrum, $\mathfrak{a}$ an ideal of $A$
distinct from $A$ such that $codim(V(\mathfrak{a}), X) = r > 0$. There exist then $r$ elements $x_{1}, \cdots, x_{r}$ of
$\mathfrak{a}$, forming part of a system of parameters of $A$, such that*

```text
                        codim(V(𝔞), V(A x_1 + ⋯ + A x_r)) = 0.
```

Let $\mathfrak{p}_{i}$ ($1 \leq i \leq m$) be the minimal prime ideals of the ring $A$, $\mathfrak{q}_{j}$ ($1 \leq j
\leq n$) the prime ideals minimal among those that contain $\mathfrak{a}$; one has `(14.2.1)`
`codim(V(𝔞), X) = inf_j codim(V(𝔮_j), X) = inf_j dim(A_{𝔮_j})` `(16.1.3.2)`. The hypothesis $r > 0$ entails that
$\mathfrak{a}$ is contained in none of the $\mathfrak{p}_{i}$; consequently there exists $x \in \mathfrak{a}$ not
belonging to any of the $\mathfrak{p}_{i}$ `(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`. One has as above
`codim(V(𝔞), V(Ax)) = inf_j dim((A/Ax)_{𝔮_j}) = inf_j dim(A_{𝔮_j}/x A_{𝔮_j})`; but since $x/1$ is not contained in any
of the minimal prime ideals of $A_{\mathfrak{q}_{j}}$, one has $\dim(A_{\mathfrak{q}_{j}}/x A_{\mathfrak{q}_{j}}) =
\dim(A_{\mathfrak{q}_{j}}) - 1$ `(16.3.4)`, whence $codim(V(\mathfrak{a}), V(Ax)) = r - 1$. For the same reason, one has
$\dim(A/Ax) = \dim(A) - 1$. We now reason by induction on $r$; if $r > 1$, there exist $r - 1$ elements $x'_{i}$ ($2
\leq i \leq r$) of $A' = A/Ax$, forming part of a system of parameters of this ring, belonging to $\mathfrak{a}/Ax$ and
such that $codim(V(\mathfrak{a}/Ax), V(A' x'_{2} + \cdots + A' x'_{r})) = 0$. Let $(x'_{i})_{r+1 \leq i \leq s}$ be a
system of elements of $A'$ such that $(x'_{i})_{2 \leq i \leq s}$ is a system of parameters of $A'$; for every $i$ such
that $2 \leq i \leq s$, let $x_{i}$ be an element of the class $x'_{i}$ in $A$, with $x_{i} \in \mathfrak{a}$ for $2
\leq i \leq r$; it is immediate that $A/(Ax + Ax_{2} + \cdots + Ax_{s})$ is of finite length, and since $\dim(A) = s$,
one sees that $x_{1} = x$ and the $x_{i}$ of indices $i \geq 2$ answer the conditions of the statement.

**Proposition (16.3.9).**

<!-- label: 0_IV.16.3.9 -->

*Let $A$, $B$ be two Noetherian local rings, $\mathfrak{m}$ the maximal ideal of $A$, $k$ its residue field, $\phi : A
\to B$ a local homomorphism.*

*(i) One has*

```text
(16.3.9.1)              dim(B) ≤ dim(A) + dim(B ⊗_A k).
```

*(ii) Let $M \neq 0$ be an $A$-module of finite type, $N \neq 0$ a $B$-module of finite type. One has*

```text
(16.3.9.2)              dim_B(M ⊗_A N) ≤ dim_A(M) + dim_{B ⊗_A k}(N ⊗_A k).
```

Let $m$ be the dimension of $A$, $(s_{i})_{1 \leq i \leq m}$ a system of parameters of $A$ `(16.3.6)`, so that if
$\mathfrak{a} = \sum_{i} s_{i} A$, $A/\mathfrak{a}$ is an $A$-module of finite length. Then the ring $A/\mathfrak{a}$ is
Artinian, so the maximal ideal $\mathfrak{m}/\mathfrak{a}$ of this ring is nilpotent; the ideal $\mathfrak{m} B /
\mathfrak{a} B$ of $B/\mathfrak{a}B$, image of $(\mathfrak{m}/\mathfrak{a}) \otimes_{A} B$, is itself also nilpotent,
and consequently one has $\dim(B/\mathfrak{a}B) = \dim(B/\mathfrak{m}B)$ (the spectra of these two rings having the same
underlying space). On the other hand $B/\mathfrak{a}B = B/(s_{1} B + \cdots + s_{m} B)$, and the images of the $s_{i}$
in $B$ belong to the maximal ideal of $B$. Consequently `(16.3.7)`, one has

```text
                        dim(B) ≤ m + dim(B ⊗_A k)
```

which is nothing other than `(16.3.9.1)`.

To prove `(16.3.9.2)`, note that if $\mathfrak{r}$ (resp. $\mathfrak{s}$) is the annihilator of $M$ (resp. $N$)

<!-- original page 128 -->

in $A$ (resp. $B$), one has $\dim_{A}(M) = \dim(A/\mathfrak{r})$, $\dim_{B}(N) = \dim(B/\mathfrak{s})$ by definition
`(16.1.7)`; on the other hand, $Supp(M \otimes_{A} N)$ is a closed subset of $\operatorname{Spec}(B)$ which identifies
`(I, 9.1.13)` with `Supp(M) ×_{Spec(A)} Supp(N) = Spec((B/𝔰) ⊗_A (A/𝔯)) = Spec(B/(𝔰 + 𝔯B))`. Since $N \otimes_{A} k$ is
a $B$-module of finite type, one has $\dim_{B \otimes_{A} k}(N \otimes_{A} k) = \dim_{B}(N \otimes_{A} k)$ `(16.1.9)`,
and $Supp(N \otimes_{A} k)$ is equal to $\operatorname{Spec}(B/(\mathfrak{s} + \mathfrak{m} B))$ by the same reasoning
as above. Applying `(16.3.9.1)` to $A/\mathfrak{r}$ and to $B/(\mathfrak{s} + \mathfrak{r}B)$ one gets

```text
            dim(B/(𝔰 + 𝔯B)) ≤ dim(A/𝔯) + dim(B/(𝔰 + 𝔪 B))
```

which is nothing other than `(16.3.9.2)`.

**Corollary (16.3.10).**

<!-- label: 0_IV.16.3.10 -->

*Under the hypotheses of `(16.3.9)`, if $\mathfrak{m} B$ is an ideal of definition of $B$, one has $\dim(B) \leq
\dim(A)$; if in addition $A$ is integral and $\dim(A) = \dim(B)$, $\phi$ is injective.*

The first assertion results from `(16.3.9)` since then $\dim(B/\mathfrak{m}B) = 0$. One may moreover replace $A$ by
$\phi(A)$, hence $\dim(B) \leq \dim(\phi(A))$; if $\mathfrak{a} = Ker(\phi) \neq 0$, and if $A$ is integral, one has
`dim(φ(A)) = dim(A/𝔞) < dim(A)` `(16.1.2.2)`, hence one cannot then have $\dim(A) = \dim(B)$ unless $\mathfrak{a} = 0$.

### 16.4. Depth and codepth ¹

**Proposition (16.4.1).**

<!-- label: 0_IV.16.4.1 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $M$ an $A$-module of finite type. Then every
$M$-regular sequence $(x_{i})_{1 \leq i \leq r}$ `(15.1.7)` formed of elements of $\mathfrak{m}$ forms part of a system
of parameters for $M$.*

We reason by induction on $r$; consider the $A$-module

```text
                        N = M/(x_1 M + ⋯ + x_{r-1} M);
```

by hypothesis $x_{1}, \cdots, x_{r-1}$ form part of a system of parameters for $M$, hence $\dim(N) = \dim(M) - (r - 1)$
`(16.3.7)`. Since by hypothesis the homothety of ratio $x_{r}$ in $N$ is injective, $x_{r}$ does not belong to any of
the prime ideals associated with $N$, hence `(16.3.4)` one has $\dim(N/x_{r} N) = \dim(N) - 1$, which is also written

```text
                        dim(M/(x_1 M + ⋯ + x_r M)) = dim(M) − r;
```

the conclusion follows therefore from `(16.3.7)`.

For an $A$-module $M \neq 0$, an $M$-regular sequence of elements of $\mathfrak{m}$ has therefore at most $\dim(M)$
elements.

**Lemma (16.4.2).**

<!-- label: 0_IV.16.4.2 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $k = A/\mathfrak{m}$ its residue field, $M$ an
$A$-module. For an $M$-regular sequence $(x_{i})_{1 \leq i \leq n}$ of elements of $\mathfrak{m}$ to be maximal, it is
necessary and sufficient that one have $\operatorname{Hom}_{A}(k, M/(x_{1} M + \cdots + x_{n} M)) \neq 0$.*

To say that $(x_{i})$ is maximal means that, for no $x \in \mathfrak{m}$, the homothety of ratio $x$ in
$N = M/(x_{1} M + \cdots + x_{n} M)$ is injective, or again that $\mathfrak{m}$ is contained in the union of the prime
ideals associated with $N$ `(Bourbaki, Alg. comm., chap. IV, §1, n° 1, cor. 2 of prop. 2)`, hence equal to one of these,
since it is a maximal ideal

______________________________________________________________________

¹ In the 3rd part of chap. III, we develop the notion of depth from the cohomological point of view and in a more
general framework.

<!-- original page 129 -->

`(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`; in other words, there is an element $z \in N$ whose annihilator
is $\mathfrak{m}$, and consequently the submodule `Az` of $N$ is isomorphic to $A/\mathfrak{m} = k$, whence the lemma.

**Lemma (16.4.3).**

<!-- label: 0_IV.16.4.3 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $k = A/\mathfrak{m}$ its residue field, $M$ an
$A$-module, $(x_{i})_{1 \leq i \leq n}$ an $M$-regular sequence of elements of $\mathfrak{m}$. Then the $A$-modules
$\operatorname{Hom}_{A}(k, M/(x_{1} M + \cdots + x_{n} M))$ and $Ext^{n}_{A}(k, M)$ are isomorphic, and for $n \geq 1$,
they are also isomorphic to $Ext^{n-1}_{A}(k, M/x_{1} M)$.*

We reason by induction on $n$, the proposition being evident for $n = 0$. Set $N = M/x_{1} M$; the sequence $(x_{i})_{2
\leq i \leq n}$ is $N$-regular, hence

```text
            Hom_A(k, M/(x_1 M + ⋯ + x_n M)) = Hom_A(k, N/(x_2 N + ⋯ + x_n N))
```

is isomorphic to $Ext^{n-1}_{A}(k, N)$ by virtue of the induction hypothesis. Consider then the exact sequence $0 \to M
--x_{1}\to M \to M/x_{1} M = N \to 0$; from it one deduces the exact sequence of `Ext`s

```text
(16.4.3.1)      Ext_A^{n-1}(k, M) → Ext_A^{n-1}(k, N) → Ext_A^n(k, M) --x_1→ Ext_A^n(k, M).
```

By virtue of the induction hypothesis, $Ext^{n-1}_{A}(k, M)$ is isomorphic to

```text
                        Hom_A(k, M/(x_1 M + ⋯ + x_{n-1} M)),
```

which is zero, since $(x_{i})_{1 \leq i \leq n-1}$ is not a maximal $M$-regular sequence `(16.4.2)`. On the other hand,
since $x_{1} \in \mathfrak{m}$, the homothety of ratio $x_{1}$ in the $A$-module $\operatorname{Hom}_{A}(k, T)$ is zero
for every $A$-module $T$, hence so is the homothety of ratio $x_{1}$ in every $A$-module $Ext^{i}_{A}(k, T)$; the
assertions of the lemma then follow at once from the exact sequence `(16.4.3.1)`.

**Corollary (16.4.4).**

<!-- label: 0_IV.16.4.4 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $k = A/\mathfrak{m}$ its residue field, $M$ an
$A$-module of finite type $\neq 0$. All maximal $M$-regular sequences of elements of $\mathfrak{m}$ have the same number
of elements, which is the smallest integer $n$ such that $Ext^{n}_{A}(k, M) \neq 0$.*

**Definition (16.4.5).**

<!-- label: 0_IV.16.4.5 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $M$ an $A$-module of finite type. We call
**depth** of $M$, and denote $prof_{\mathfrak{m}}(M)$ or $prof(M)$, the supremum of the number of elements of an
$M$-regular sequence formed of elements of $\mathfrak{m}$.*

One has therefore $prof(M) = +\infty$ if and only if $M = 0$, and, by `(16.4.1)`

```text
(16.4.5.1)              prof(M) ≤ dim(M)            if M ≠ 0.
```

One has evidently $prof(M^{k}) = prof(M)$ for every $k > 0$.

**Proposition (16.4.6).**

<!-- label: 0_IV.16.4.6 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $M$ an $A$-module of finite type.*

*(i) For $prof(M) = 0$, it is necessary and sufficient that $\mathfrak{m} \in Ass(M)$ (or again that there exist a
submodule of $M$ isomorphic to the residue field $k = A/\mathfrak{m}$ of $A$).*

*(ii) For every $M$-regular element $x$ belonging to $\mathfrak{m}$, one has*

$$ (16.4.6.1) prof(M/xM) = prof(M) - 1. $$

*(iii) If $M \neq 0$, one has*

```text
(16.4.6.2)              prof(M) ≤ inf_{𝔭 ∈ Ass(M)} dim(A/𝔭) ≤ dim(M).
```

<!-- original page 130 -->

*(iv) One has $prof_{A}(M) = prof_{\hat{A}}(\hat{M})$.*

(i) To say that $prof(M) = 0$ means that there exists no $x \in \mathfrak{m}$ such that the homothety of ratio $x$ in
$M$ is injective, in other words that every $x \in \mathfrak{m}$ belongs to a prime ideal associated with $M$
`(Bourbaki, Alg. comm., chap. IV, §1, n° 1, cor. 2 of prop. 2)`; but $\mathfrak{m}$ cannot be the union of the prime
ideals associated with $M$ unless it is equal to one of them `(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`.

(ii) If $(x_{i})_{1 \leq i \leq r}$ is an $(M/xM)$-regular sequence formed of elements of $\mathfrak{m}$, the sequence
formed of $x$ and the $x_{i}$ is $M$-regular, and it follows from the definition that it is maximal when the sequence
$(x_{i})_{1 \leq i \leq r}$ is a maximal $(M/xM)$-regular sequence; whence the conclusion.

(iii) We reason by induction on $n = prof(M)$, the assertion being evident for $n = 0$. We shall use the following
lemma:

**Lemma (16.4.6.3).**

<!-- label: 0_IV.16.4.6.3 -->

*Let $A$ be a Noetherian ring, $M$ an $A$-module of finite type, $t \in A$ an $M$-regular element. Then, for every
$\mathfrak{p} \in Ass(M)$, every prime ideal minimal among those containing $\mathfrak{p} + At$ is associated with
$M/tM$.*

One knows that there exists an exact sequence

$$ 0 \to M' \to M \to M'' \to 0 $$

such that $Ass(M') = {\mathfrak{p}}$, $Ass(M'') = Ass(M) - {\mathfrak{p}}$
`(Bourbaki, Alg. comm., chap. IV, §1, n° 1, prop. 4)`; since $t$ is $M$-regular, it is also $M'$-regular and
`M''`-regular `(loc. cit., §1, n° 1, cor. 2 of prop. 2)`. One deduces that the sequence

$$ 0 \to M'/tM' \to M/tM \to M''/tM'' \to 0 $$

is exact `(15.1.18)`. Consequently, one has $Ass(M'/tM') \subset Ass(M/tM)$. But the prime ideals of $A$ containing
$\mathfrak{p}$ are the points of $Supp(M')$ `(loc. cit., §1, n° 3, prop. 7)`, hence the prime ideals containing
$\mathfrak{p} + At$ are the points of the support of $M'/tM' = M' \otimes_{A} (A/tA)$ $(0_{I}, 1.7.5)$; a minimal
element of the set of these prime ideals therefore belongs to $Ass(M'/tM')$
`(Bourbaki, loc. cit., §1, n° 3, cor. 1 of prop. 7)`, and a fortiori to $Ass(M/tM)$.

This lemma being established, we return to the proof of (iii). Let $x \in \mathfrak{m}$ be an $M$-regular element, so
that $prof(M/xM) = n - 1$ by (ii); for every $\mathfrak{p} \in Ass(M)$, it follows from the lemma that there is an ideal
$\mathfrak{p}'$ associated with $M/xM$ and containing $\mathfrak{p} + Ax$; but as $x$ is $M$-regular, one has $x \notin
\mathfrak{p}$, whence $\mathfrak{p}' \neq \mathfrak{p}$ and consequently $\dim(A/\mathfrak{p}') \leq
\dim(A/\mathfrak{p}) - 1$. Now the induction hypothesis shows that $n - 1 \leq \dim(A/\mathfrak{p}')$; one concludes
that $n \leq \dim(A/\mathfrak{p})$ for every $\mathfrak{p} \in Ass(M)$.

(iv) One may restrict oneself to the case where $M \neq 0$. Recall that $\hat{M} = M \otimes_{A} \hat{A}$ up to a
canonical isomorphism $(0_{I}, 7.3.3)$; since `Â` is a flat $A$-module, one has canonical isomorphisms $Ext^{i}_{A}(k,
M) \otimes_{A} \hat{A} \cong Ext^{i}_{\hat{A}}(k, M \otimes_{A} \hat{A})$ since $k = k \otimes_{A} \hat{A}$ up to a
canonical isomorphism $(0_{III}, 12.3.5)$. Assertion (iv) thus results from `(16.4.4)` and from the fact that `Â` is a
faithfully flat $A$-module $(0_{I}, 7.3.5)$.

**(16.4.6.4)** One notes that if $\mathfrak{p}$ is a prime ideal of $A$, one may have either
$prof_{A_{\mathfrak{p}}}(M_{\mathfrak{p}}) < prof_{A}(M)$ or $prof_{A_{\mathfrak{p}}}(M_{\mathfrak{p}}) > prof_{A}(M)$;
for an example of the first case,

<!-- original page 131 -->

it suffices to take for $A$ a Noetherian local integral ring of dimension $\geq 1$; one has $prof(A) \geq 1$ but
$prof(K) = 0$ for the field of fractions $K$ of $A$. For an example of the second case, consider a Noetherian local
integral ring `A_0` of dimension $\geq 2$, with maximal ideal $\mathfrak{m}_{0}$ and let $k = A_{0}/\mathfrak{m}_{0}$ be
its residue field; let $A = A_{0} \oplus \mathfrak{j}$ be the trivial extension of `A_0` by the `A_0`-module $k$
`(18.2.3)`, the ideal $\mathfrak{j}$ being `A_0`-isomorphic to $k$ (so that multiplication in $A$ is given by $(x,
\xi)(x', \xi') = (xx', x\xi' + x'\xi)$). It is clear that $\mathfrak{j}$ is the nilradical of $A$ and $A/\mathfrak{j}$
is isomorphic to `A_0`, so that every prime ideal $\mathfrak{p}$ of $A$ is of the form $\mathfrak{p}_{0} \oplus
\mathfrak{j}$, where $\mathfrak{p}_{0}$ is a prime ideal of `A_0`; in particular $\mathfrak{m} = \mathfrak{m}_{0} \oplus
\mathfrak{j}$ is the unique maximal ideal of $A$. As every element of $\mathfrak{m}_{0}$ annihilates $\mathfrak{j}$, one
has $prof(A) = prof(A_{\mathfrak{m}}) = 0$; on the other hand, if $\mathfrak{p}_{0} \neq \mathfrak{m}_{0}$, the elements
of $\mathfrak{j}$ are annihilated by those of $\mathfrak{m}_{0} - \mathfrak{p}_{0}$, hence $A_{\mathfrak{p}}$ is
canonically isomorphic to $(A_{0})_{\mathfrak{p}_{0}}$, and as `A_0` is integral, $prof(A_{\mathfrak{p}}) =
prof((A_{0})_{\mathfrak{p}_{0}}) \geq 1$ if $\mathfrak{p}_{0} \neq 0$.

**Corollary (16.4.7).**

<!-- label: 0_IV.16.4.7 -->

*For a Noetherian reduced local ring $A$ to be of depth `0`, it is necessary and sufficient that $A$ be a field.*

Indeed, since the intersection of the minimal prime ideals of $A$ is `0`, $A$ has no embedded associated prime ideals;
by virtue of `(16.4.6, (i))`, if $prof(A) = 0$, the maximal ideal $\mathfrak{m}$ of $A$ is also a minimal prime ideal,
hence is the only prime ideal of $A$, and since $A$ is reduced, $\mathfrak{m} = 0$.

**Proposition (16.4.8).**

<!-- label: 0_IV.16.4.8 -->

*Let $A$, $B$ be two Noetherian local rings, $\rho : A \to B$ a local homomorphism, $M$ a $B$-module such that
$M_{[\rho]}$ is an $A$-module of finite type. Then one has*

$$ (16.4.8.1) prof_{A}(M_{[\rho]}) = prof_{B}(M). $$

One may restrict oneself to the case $M \neq 0$; suppose that $prof_{A}(M_{[\rho]}) = n$. If $(x_{i})_{1 \leq i \leq n}$
is a maximal $(M_{[\rho]})$-regular sequence formed of elements of the maximal ideal of $A$, the $\rho(x_{i})$
constitute an $M$-regular sequence formed of elements of the maximal ideal of $B$, and one has therefore, on setting $N
= M/(\rho(x_{1}) M + \cdots + \rho(x_{n}) M)$, $prof_{B}(N) = prof_{B}(M) - n$ `(16.4.6, (ii))`; similarly $N_{[\rho]} =
M_{[\rho]}/(x_{1} M_{[\rho]} + \cdots + x_{n} M_{[\rho]})$ and $prof_{A}(N_{[\rho]}) = 0$; one is thus reduced to
proving the proposition when $n = 0$. Let $k$ be the residue field of $A$; since $k$ is a quotient of $A$, the
$A$-module $P = \operatorname{Hom}_{A}(k, M_{[\rho]})$ is a submodule of $\operatorname{Hom}_{A}(A, M_{[\rho]}) =
M_{[\rho]}$ and the hypothesis entails that $P \neq 0$ `(16.4.6, (i))`; in addition, $P$ is an $A$-module of finite type
(since $M_{[\rho]}$ is an $A$-module of finite type), hence a $k$-vector space of finite type, being annihilated by the
maximal ideal of $A$, and finally an $A$-module of finite length. On the other hand, $P$ is also a submodule of the
$B$-module $M$, and since it is of finite length as an $A$-module, it is a fortiori so as a $B$-module. Since it is
$\neq 0$, it contains a simple sub-$B$-module, that is to say isomorphic to the residue field of $B$; one concludes then
from `(16.4.6, (i))` that one has indeed $prof_{B}(M) = 0$.

**Definition (16.4.9).**

<!-- label: 0_IV.16.4.9 -->

*Let $A$ be a Noetherian local ring, $M$ an $A$-module of finite type. If $M \neq 0$, we call **codepth** of $M$ and
denote $coprof_{\mathfrak{m}}(M)$ or $coprof(M)$, the finite integer $\dim_{A}(M) - prof_{A}(M) \geq 0$ `(16.4.5.1)`. If
$M = 0$, we set $coprof(M) = 0$.*

One has $coprof(M^{k}) = coprof(M)$ for every $k > 0$.

**Proposition (16.4.10).**

<!-- label: 0_IV.16.4.10 -->

*Let $A$ be a Noetherian local ring, $M$ an $A$-module of finite type.*

<!-- original page 132 -->

*(i) For every $M$-regular element $x$ belonging to the maximal ideal of $A$, one has $coprof(M/xM) = coprof(M)$.*

*(ii) One has $coprof_{A}(M) = coprof_{\hat{A}}(\hat{M})$.*

Indeed, (i) results from `(16.3.4)` and `(16.4.6, (ii))`, and (ii) from `(16.2.4)` and `(16.4.6, (iv))`.

We shall show later `(IV, 6.11.5)` that for every prime ideal $\mathfrak{p}$ of $A$, one has
$coprof_{A_{\mathfrak{p}}}(M_{\mathfrak{p}}) \leq coprof_{A}(M)$.

**Proposition (16.4.11).**

<!-- label: 0_IV.16.4.11 -->

*Under the hypotheses of `(16.4.8)`, one has*

$$ (16.4.11.1) coprof_{A}(M_{[\rho]}) \geq coprof_{B}(M). $$

This results from `(16.1.9)` and `(16.4.8)`.

### 16.5. Cohen-Macaulay modules

**Definition (16.5.1).**

<!-- label: 0_IV.16.5.1 -->

*Let $A$ be a Noetherian local ring. We say that an $A$-module of finite type $M$ is a **Cohen-Macaulay module** if
$coprof(M) = 0$, in other words if $M = 0$ or if $M \neq 0$ and $\dim(M) = prof(M)$. We say that $A$ is a
**Cohen-Macaulay ring** if the $A$-module $A$ is a Cohen-Macaulay module.*

An $A$-module of finite length is a Cohen-Macaulay module since it is of dimension `0` `(16.1.10)`. A reduced local ring
$A$ of dimension `1` is a Cohen-Macaulay ring, for then its maximal ideal $\mathfrak{m}$ cannot be associated with $A$
`(Bourbaki, Alg. comm., chap. IV, §2, n° 5, prop. 10)`, hence $prof(A) = 1$ by virtue of `(16.4.6, (i))`. If $A$ is an
integrally closed integral local ring of dimension $\geq 2$, one has $prof(A) \geq 2$: indeed, if $x \neq 0$ is an
element of $\mathfrak{m}$, one knows `(Bourbaki, Alg. comm., chap. VII, §1, n° 4, prop. 8)` that the prime ideals
associated with $A/xA$ are of height `1`, hence distinct from $\mathfrak{m}$, and their union is consequently distinct
from $\mathfrak{m}$ `(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`; there exist therefore sequences $(x, y)$
which are $A$-regular and formed of elements of $\mathfrak{m}$, whence our assertion. One concludes that *an integrally
closed local ring of dimension `2` is a Cohen-Macaulay ring*.

**Proposition (16.5.2).**

<!-- label: 0_IV.16.5.2 -->

*Let $A$ be a Noetherian local ring, $M$ an $A$-module of finite type. For $M$ to be a Cohen-Macaulay module, it is
necessary and sufficient that $\hat{M}$ be an `Â`-module of Cohen-Macaulay.*

This results at once from `(16.4.10, (ii))`.

**Proposition (16.5.3).**

<!-- label: 0_IV.16.5.3 -->

*Under the hypotheses of `(16.4.8)`, for $M$ to be a $B$-module of Cohen-Macaulay, it is necessary and sufficient that
$M_{[\rho]}$ be an $A$-module of Cohen-Macaulay.*

This results from `(16.4.11)`.

**Proposition (16.5.4).**

<!-- label: 0_IV.16.5.4 -->

*Let $A$ be a Noetherian local ring, $M$ an $A$-module of finite type $\neq 0$. If $M$ is a Cohen-Macaulay $A$-module,
one has $\dim(A/\mathfrak{p}) = \dim(M)$ for every prime ideal $\mathfrak{p} \in Ass(M)$; in particular no prime ideal
associated with $M$ is embedded.*

This results at once from the inequalities `(16.4.6.2)`.

One can also say that $M$ (or $Supp(M)$) is equidimensional `(16.1.7)`.

<!-- original page 133 -->

**Proposition (16.5.5).**

<!-- label: 0_IV.16.5.5 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $M$ an $A$-module of finite type $\neq 0$, $x$ an
element of $\mathfrak{m}$. Suppose that $M$ is a Cohen-Macaulay module; then the following conditions are equivalent:*

*a) $x$ is $M$-regular;*

*b) $\dim(M/xM) = \dim(M) - 1$;*

*c) $x$ belongs to no minimal element of $Supp(M)$.*

*In addition, $M/xM$ is then a Cohen-Macaulay module.*

It has been seen `(16.5.4)` that all elements $\mathfrak{p}$ of $Ass(M)$ are minimal in $Supp(M)$ and that
$\dim(A/\mathfrak{p}) = \dim(M)$; the equivalence of a) and c) results then from
`Bourbaki, Alg. comm., chap. IV, §1, n° 1, cor. 2 of prop. 2`; the equivalence of b) and c) results from `(16.3.4)`. The
fact that $M/xM$ is a Cohen-Macaulay module results finally from `(16.4.10, (i))`.

**Corollary (16.5.6).**

<!-- label: 0_IV.16.5.6 -->

*Under the hypotheses of `(16.5.5)`, let $(x_{i})_{1 \leq i \leq r}$ be a sequence of elements of $\mathfrak{m}$. The
following conditions are equivalent:*

*a) The sequence $(x_{i})$ is $M$-regular.*

*b) One has $\dim(M/(x_{1} M + \cdots + x_{r} M)) = \dim(M) - r$.*

*c) The $x_{i}$ form part of a system of parameters of $M$.*

*In addition, when these conditions are satisfied, $N = M/(x_{1} M + \cdots + x_{r} M)$ is a Cohen-Macaulay module,
hence, for every ideal $\mathfrak{p} \in Ass(N)$, one has $\dim(A/\mathfrak{p}) = \dim(M) - r$.*

One already knows that b) and c) are equivalent `(16.3.6)` and that a) entails c) `(16.4.1)` without hypothesis on $M$.
To see that c) implies a) and prove the last assertion of the statement, we reason by induction on $r$, the assertion
being trivial for $r = 0$. Since $x_{1}$ forms part of a system of parameters, $\dim(M/x_{1} M) = \dim(M) - 1$
`(16.3.6)`, hence $x_{1}$ is $M$-regular and $M/x_{1} M$ is a Cohen-Macaulay module by `(16.5.5)`. Since the sequence
$(x_{i})_{2 \leq i \leq r}$ forms part of a system of parameters for $P = M/x_{1} M$, the induction hypothesis shows
that $(x_{i})_{2 \leq i \leq r}$ is a $P$-regular sequence and that $P/(x_{2} P + \cdots + x_{r} P) = N$ is a
Cohen-Macaulay module; in addition $(x_{i})_{1 \leq i \leq r}$ is $M$-regular.

**Remark (16.5.7).**

<!-- label: 0_IV.16.5.7 -->

*It follows from `(16.5.6)` that there is identity between the systems of parameters for $M$ and the maximal $M$-regular
sequences of elements of $\mathfrak{m}$ when $M$ is a Cohen-Macaulay module. Conversely, it follows from `(16.4.1)` that
if a non-zero $A$-module $M$ of finite type is such that there is an $M$-regular sequence which is a system of
parameters for $M$, then $M$ is a Cohen-Macaulay module. The last property stated in `(16.5.6)` also characterizes
Cohen-Macaulay modules:*

**Proposition (16.5.8).**

<!-- label: 0_IV.16.5.8 -->

*Let $A$ be a Noetherian local ring, $M$ an $A$-module of finite type. Suppose that for every sequence $(x_{i})_{1 \leq
i \leq r}$ of elements of $\mathfrak{m}$ forming part of a system of parameters for $M$, and every prime ideal
$\mathfrak{p}$ associated with $N = M/(x_{1} M + \cdots + x_{r} M)$, one has $\dim(A/\mathfrak{p}) = \dim(N)$. Then $M$
is a Cohen-Macaulay module.*

Let $(y_{i})_{1 \leq i \leq n}$ be a system of parameters for $M$; it suffices to show that the sequence $(y_{i})$ is
$M$-regular. We reason by induction on $n = \dim(M)$, the proposition being trivial for $n = 0$. By hypothesis (applied
with $r = 0$) the prime ideals $\mathfrak{p}_{j}$ associated with $M$ are all such that $\dim(A/\mathfrak{p}_{j}) =
\dim(M)$; since $y_{1}$ forms part of a system of parameters

<!-- original page 134 -->

for $M$, it follows from `(16.3.7)` and `(16.3.4)` that $y_{1}$ does not belong to any of the $\mathfrak{p}_{j}$, hence
is $M$-regular. If one sets $P = M/y_{1} M$, $(y_{i})_{2 \leq i \leq n}$ is a system of parameters for $P$, and it is
immediate that $P$ satisfies the hypothesis of the statement; applying the induction hypothesis, one therefore sees that
$(y_{i})_{2 \leq i \leq n}$ is a $P$-regular sequence, which proves the proposition.

**Proposition (16.5.9).**

<!-- label: 0_IV.16.5.9 -->

*Let $A$ be a Noetherian local ring, $M$ an $A$-module of finite type; suppose that $M$ is a Cohen-Macaulay module. Let
$\mathfrak{p} \in Supp(M)$, and set $r = \dim(M) - \dim(M/\mathfrak{p}M)$. Then there exists an $M$-regular sequence
$(x_{i})_{1 \leq i \leq r}$ formed of elements of $\mathfrak{p}$; for every sequence having these properties, one has*

```text
            dim(M/(x_1 M + ⋯ + x_r M)) = dim(M/𝔭M) = dim(A/𝔭),
```

*and $\mathfrak{p}$ is a minimal element of $Ass(M/(x_{1} M + \cdots + x_{r} M))$.*

Let us first prove the existence of the $x_{i}$; there is nothing to prove for $r = 0$. For $r > 0$, we proceed by
induction on $r$. Since for every prime ideal $\mathfrak{q}_{i}$ associated with $M$ one has $\dim(A/\mathfrak{q}_{i}) =
\dim(M)$ `(16.5.4)`, the hypothesis $\dim(M/\mathfrak{p}M) < \dim(M)$ entails that $\mathfrak{p}$ cannot be contained in
any of the $\mathfrak{q}_{i}$, the latter being the prime ideals minimal among those that contain $Ann(M)$ (`(16.1.2.2)`
and `(16.1.7)`); one concludes that $\mathfrak{p}$ is also not contained in the union of the $\mathfrak{q}_{i}$
`(Bourbaki, Alg. comm., chap. II, §1, n° 1, prop. 2)`, and consequently there exists $x_{1} \in \mathfrak{p}$ which is
$M$-regular `(Bourbaki, Alg. comm., chap. IV, §1, n° 1, cor. 2 of prop. 2)`. One thus deduces from `(16.5.5)` that $N =
M/x_{1} M$ is a Cohen-Macaulay module, of dimension $\dim(M) - 1$; since $x_{1} \in \mathfrak{p}$, one has moreover
$N/\mathfrak{p}N = M/\mathfrak{p}M$, whence $\dim(N) - \dim(N/\mathfrak{p}N) = r - 1$; one may consequently apply to $N$
the induction hypothesis, and if $(x_{i})_{2 \leq i \leq r}$ is an $N$-regular sequence formed of elements of
$\mathfrak{p}$, it is clear that $(x_{i})_{1 \leq i \leq r}$ is an $M$-regular sequence formed of elements of
$\mathfrak{p}$. If one sets $P = M/(x_{1} M + \cdots + x_{r} M)$, one has $P/\mathfrak{p}P = M/\mathfrak{p}M$ since the
$x_{i}$ are in $\mathfrak{p}$, and $\dim(P) = \dim(P/\mathfrak{p}P)$ by `(16.5.6)`; but since $P$ is a Cohen-Macaulay
module, one has also $\dim(P) = \dim(A/\mathfrak{p}')$ for every $\mathfrak{p}' \in Ass(P)$ `(16.5.4)`. Since
$\mathfrak{p} \in Supp(P)$ $(0_{I}, 1.7.5)$, $\mathfrak{p}$ contains one of the ideals $\mathfrak{p}' \in Ass(P)$
`(Bourbaki, Alg. comm., chap. IV, §1, n° 4, th. 2)`, and since `dim(P) = dim(P/𝔭P) ≤ dim(A/𝔭) ≤ dim(A/𝔭') = dim(P)`, one
necessarily has $\mathfrak{p} = \mathfrak{p}'$ `(16.1.2.2)`, which completes the proof.

**Corollary (16.5.10).**

<!-- label: 0_IV.16.5.10 -->

*Under the same hypotheses as in `(16.5.9)`:*

*(i) $M_{\mathfrak{p}}$ is a Cohen-Macaulay $A_{\mathfrak{p}}$-module.*

*(ii) One has*

```text
(16.5.10.1)             dim(M) = dim_A(M/𝔭M) + dim_{A_𝔭}(M_𝔭).
```

With the notations of `(16.5.9)`, let $x'_{i}$ be the canonical images of the $x_{i}$ in $A_{\mathfrak{p}}$ ($1 \leq i
\leq r$); since the $x'_{i}$ belong to the maximal ideal of $A_{\mathfrak{p}}$ and form an $M_{\mathfrak{p}}$-regular
sequence by flatness `(15.1.14)`, one has

```text
            prof_{A_𝔭}(M_𝔭) ≥ r = dim(M) − dim(M/𝔭M) ≥ dim_{A_𝔭}(M_𝔭)
```

(by virtue of `(16.1.8.1)`). But taking `(16.4.5.1)` into account, the three terms of this inequality are necessarily
equal, whence the corollary.

<!-- original page 135 -->

**Corollary (16.5.11).**

<!-- label: 0_IV.16.5.11 -->

*Let $A$ be a Noetherian local ring; suppose that there exists an $A$-module of finite type $M$ of support
$\operatorname{Spec}(A)$, which is a Cohen-Macaulay module. Then, for every prime ideal $\mathfrak{p}$ of $A$, one has*

```text
(16.5.11.1)             dim(A) = dim(A/𝔭) + dim(A_𝔭).
```

Indeed, $Supp(M/\mathfrak{p}M) = \operatorname{Spec}(A/\mathfrak{p})$ $(0_{I}, 1.7.5)$ and $Supp(M_{\mathfrak{p}}) =
\operatorname{Spec}(A_{\mathfrak{p}})$; the relation `(16.5.11.1)` is therefore a particular case of `(16.5.10.1)`.

**Corollary (16.5.12).**

<!-- label: 0_IV.16.5.12 -->

*Every quotient ring of a Noetherian local ring $A$ satisfying the conditions of `(16.5.11)` (in particular every
quotient ring of a Cohen-Macaulay local ring) is catenary.*

It evidently suffices to prove that $A$ itself is catenary, in other words that, for two prime ideals $\mathfrak{p}
\subset \mathfrak{q}$ of $A$, one has `(16.1.4.2)`

```text
                        dim(A_𝔮) = dim(A_𝔭) + dim(A_𝔮 / 𝔭 A_𝔮).
```

Now, by virtue of `(16.5.10, (i))` $A_{\mathfrak{q}}$ satisfies the same hypotheses as $A$, and the preceding relation
is therefore nothing other than `(16.5.11.1)` applied to $A_{\mathfrak{q}}$ and to the prime ideal $\mathfrak{p}
A_{\mathfrak{q}}$ of $A_{\mathfrak{q}}$.

**(16.5.13)** Let $A$ be a Noetherian ring, $M$ an $A$-module of finite type. We say that $M$ is a *Cohen-Macaulay
$A$-module* if, for every prime ideal $\mathfrak{p}$ of $A$, $M_{\mathfrak{p}}$ is a Cohen-Macaulay
$A_{\mathfrak{p}}$-module; by virtue of `(16.5.10)` this definition coincides with `(16.5.1)` when $A$ is local. We say
that $A$ is a *Cohen-Macaulay ring* if all the $A_{\mathfrak{p}}$ are. It is clear that if $M$ (resp. $A$) is a
Cohen-Macaulay $A$-module (resp. a Cohen-Macaulay ring), $S^{-1}M$ is a Cohen-Macaulay $S^{-1}A$-module (resp. $S^{-1}A$
is a Cohen-Macaulay ring) for every multiplicative subset $S$ of $A$.

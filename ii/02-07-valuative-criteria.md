# §7. Valuative criteria

In this section we give valuative criteria of separation and properness for a morphism — that is, criteria that bring in
an auxiliary variable scheme of the form $\operatorname{Spec}(A)$, where $A$ is a valuation ring. Under suitable
"Noetherian" hypotheses, one may restrict in these criteria to the case where $A$ is a _discrete_ valuation ring. This
will doubtless be the only case we shall have to apply in what follows, and we have introduced arbitrary valuation
rings, in the general case, only in order to make the connection with classical developments.

<!-- original page 138 -->

## 7.1. Reminders on valuation rings

**(7.1.1)**

<!-- label: II.7.1.1 -->

Among the various equivalent properties characterising valuation rings, we shall use the following: a ring $A$ is called
a _valuation ring_ if it is an integral ring that is not a field and if, in the set of local rings contained in the
field of fractions $K$ of $A$ and distinct from $K$, $A$ is maximal for the relation of domination `(I, 8.1.1)`. Recall
that a valuation ring is _integrally closed_. If $A$ is a valuation ring, then $A_{\mathfrak{p}}$ is also a valuation
ring for every prime ideal $\mathfrak{p} \neq (0)$ of $A$.

**(7.1.2)**

<!-- label: II.7.1.2 -->

Let $K$ be a field and $A$ a local subring of $K$ that is not a field;

<!-- original page 139 -->

there then exists a valuation ring having $K$ as its field of fractions and dominating $A$ (`[1], p. 1-07, lemma 2`).

On the other hand, let $B$ be a valuation ring, $k$ its residue field, $K$ its field of fractions, and $L$ an extension
of $k$. Then there exists a _complete_ valuation ring $C$ that dominates $B$ and whose residue field is $L$. Indeed, $L$
is an algebraic extension of a pure transcendental extension $L' = k(T_{\mu})_{\mu\in M}$; we know that one can extend
the valuation of $K$ corresponding to $B$ to a valuation of $K' = K(T_{\mu})_{\mu\in M}$ in such a way that $L'$ is the
residue field of this valuation (`[24], p. 98`); replacing $B$ by the completion of the ring of this extended valuation,
we see that we may restrict to the case where $B$ is complete and $L$ is an algebraic closure of $k$. If $\bar{K}$ is an
algebraic closure of $K$, we can then extend to $\bar{K}$ the valuation that defines $B$, and the corresponding residue
field is an algebraic closure of $k$, as one sees by lifting to $\bar{K}$ the coefficients of a monic polynomial of
`k[T]`. We are thus finally reduced to the case where $L = k$, and it then suffices to take $C$ to be the completion of
$B$ in order to settle the question.

**(7.1.3)**

<!-- label: II.7.1.3 -->

Let $K$ be a field and $A$ a subring of $K$; the integral closure $A'$ of $A$ in $K$ is the intersection of the
valuation rings containing $A$ and having $K$ as field of fractions (`[11], p. 51, th. 2`). Proposition (7.1.2) is
expressed in the following equivalent geometric form:

**Proposition.**

<!-- label: II.7.1.4 -->

Let $Y$ be a prescheme, $p : X \to Y$ a morphism, $x$ a point of $X$, $y = p(x)$, and $y' \neq y$ a specialisation
`(0, 2.1.2)` of $y$. There then exists a local scheme $Y'$, spectrum of a valuation ring, and a separated morphism $f :
Y' \to Y$ such that, if $a$ denotes the unique closed point of $Y'$ and $b$ the generic point of $Y'$, one has $f(a) =
y'$ and $f(b) = y$. One may further suppose that one of the two additional properties below is satisfied:

(i) $Y'$ is the spectrum of a complete valuation ring whose residue field is algebraically closed, and there exists a
$\kappa(y)$-homomorphism $\kappa(x) \to \kappa(b)$.

(ii) There exists a $\kappa(y)$-isomorphism $\kappa(x) \xrightarrow{\sim} \kappa(b)$.

**Proof.** Let $Y_{1}$ be the closed reduced subprescheme of $Y$ having $\bar{y}$ as its underlying space `(I, 5.2.1)`,
and let $X_{1}$ be the closed subprescheme given by the inverse image $p^{-1}(Y_{1})$; since $y' \in \bar{y}$ by
hypothesis and since $\kappa(x)$ is the same in $X$ and in $X_{1}$, we may suppose $Y$ integral, with generic point $y$;
$\mathcal{O}_{y'}$ is then an integral local ring that is not a field and whose field of fractions is $\mathcal{O}_{y} =
\kappa(y)$, and $\kappa(x)$ is an extension of $\kappa(y)$. In order to satisfy the conditions $f(a) = y'$ and $f(b) =
y$ as well as the additional condition (i) (resp. (ii)), we take $Y' = \operatorname{Spec}(A')$, where $A'$ is a
valuation ring dominating $\mathcal{O}_{y'}$ and which is complete with residue field algebraically closed extension of
$\kappa(x)$ (resp. a valuation ring $A'$ dominating $\mathcal{O}_{y'}$ and whose field of fractions is $\kappa(x)$); the
existence of $A'$ is guaranteed by (7.1.2).

**(7.1.5)**

<!-- label: II.7.1.5 -->

Recall that a local ring $A$ is said to be _of dimension `1`_ if there exists a prime ideal distinct from the maximal
ideal $\mathfrak{m}$ and if every prime ideal of $A$ distinct from $\mathfrak{m}$ is a _minimal_ prime ideal; when $A$
is _integral_, this amounts to saying that $\mathfrak{m}$ and `(0)` are the only prime ideals and $\mathfrak{m} \neq
(0)$; in other words, $Y = \operatorname{Spec}(A)$ is reduced to two

<!-- original page 140 -->

points $a$ and $b$: $a$ is the unique _closed_ point, $\mathfrak{j}_{a} = \mathfrak{m}$, and $\kappa(a) = k$ is the
_residue field_ $k = A/\mathfrak{m}$; $b$ is the _generic point_ of $Y$, $\mathfrak{j}_{b} = (0)$, the set ${b}$ being
the unique open subset of $Y$ distinct from both $\emptyset$ and $Y$ (an open subset which is therefore _everywhere
dense_), and $\kappa(b) = K$ is the _field of fractions_ of $A$.

**(7.1.6)**

<!-- label: II.7.1.6 -->

For a local ring $A$, Noetherian and of dimension `1`, we know (`[1], p. 2-08 and 17-01`) that the following conditions
are equivalent:

(a) $A$ is normal;

(b) $A$ is regular;

(c) $A$ is a valuation ring;

furthermore, $A$ is then a _discrete valuation ring_. Propositions (7.1.2) and (7.1.3) then have the following analogues
for discrete valuation rings:

**Proposition.**

<!-- label: II.7.1.7 -->

Let $A$ be an integral local Noetherian ring that is not a field, $K$ its field of fractions, and $L$ an extension of
finite type of $K$. There then exists a discrete valuation ring having $L$ as its field of fractions and dominating $A$.

**Proof.** Suppose first $L = K$. Let $\mathfrak{m}$ be the maximal ideal of $A$, $(x_{1}, \cdots, x_{n})$ a system of
nonzero generators of $\mathfrak{m}$, and $B$ the subring $A[x_{2}/x_{1}, \cdots, x_{n}/x_{1}]$ of $K$, which is
Noetherian. It is immediate that the ideal $\mathfrak{m}B$ of $B$ is identical to the principal ideal $x_{1}B$; if
$\mathfrak{p}$ is a minimal prime ideal of $x_{1}B$, we know that $\mathfrak{p}$ is of rank `1` (`[13], t. I, p. 277`);
in other words, $B_{\mathfrak{p}}$ is a local Noetherian ring _of dimension `1`_; it is clear that
$\mathfrak{p}B_{\mathfrak{p}} \cap A$ is an ideal of $A$ containing $\mathfrak{m}$ and not containing `1`, hence equal
to $\mathfrak{m}$, so that $B_{\mathfrak{p}}$ _dominates_ $A$ `(I, 8.1.1)`. It follows from the Krull–Akizuki theorem
(`[25], p. 293`) that the integral closure $C$ of $B_{\mathfrak{p}}$ is a Noetherian ring (although $C$ is not
necessarily a $B_{\mathfrak{p}}$-module of finite type); if $\mathfrak{n}$ is a maximal ideal of $C$, then
$C_{\mathfrak{n}}$ is a normal local Noetherian ring of dimension `1` (`[25], p. 295`), hence a discrete valuation ring,
which dominates $B_{\mathfrak{p}}$ and _a fortiori_ $A$.

If now $L$ is an extension of finite type of $K$, we may, by what precedes, restrict to the case where $A$ is already a
discrete valuation ring. Let $w$ be a valuation of $K$ associated to $A$; there exists a discrete valuation $w'$ of $L$
that _extends_ $w$: indeed, by induction on the number of generators of $L$, we reduce to the case $L = K(\alpha)$, and
then the proposition is classical (`[24], p. 106`).

**Corollary.**

<!-- label: II.7.1.8 -->

Let $A$ be a Noetherian integral ring, $K$ its field of fractions, and $L$ an extension of finite type of $K$. Then the
integral closure of $A$ in $L$ is the intersection of the discrete valuation rings having $L$ as field of fractions and
containing $A$.

**Proof.** Indeed, such a discrete valuation ring, being normal, contains _a fortiori_ every element of $L$ that is
integral over $A$. It thus suffices to prove that if $x \in L$ is not integral over $A$, then there exists a discrete
valuation ring $C$ having $L$ as field of fractions, containing $A$, and not containing $x$. The hypothesis on $x$ means
that $x \notin B = A[1/x]$, in other words, that $1/x$ is not invertible in the Noetherian ring $B$. There is thus a
prime ideal $\mathfrak{p}$ of $B$ containing $1/x$. The integral local ring $B_{\mathfrak{p}}$ is Noetherian and
contained in $L$, which is an extension of finite type of the field of fractions of $B_{\mathfrak{p}}$ (the latter
containing $K$). By virtue of (7.1.7) there is then a discrete valuation ring $C$ dominating $B_{\mathfrak{p}}$ and
having $L$ as field of fractions; since $1/x \in \mathfrak{p}B_{\mathfrak{p}}$ belongs to the maximal ideal of $C$, we
have $x \notin C$, which concludes the proof.

The geometric form of (7.1.7) is the following:

<!-- original page 141 -->

**Proposition.**

<!-- label: II.7.1.9 -->

Let $Y$ be a locally Noetherian prescheme, $p : X \to Y$ a morphism locally of finite type, $x$ a point of $X$, $y =
p(x)$, and $y' \neq y$ a specialisation of $y$. There then exists a local scheme $Y'$, spectrum of a discrete valuation
ring, a separated morphism $f : Y' \to Y$, and a $Y$-rational map $g$ from $Y'$ to $X$ such that, denoting the closed
point of $Y'$ by $a$ and its generic point by $b$, one has $f(a) = y'$, $f(b) = y$, $g(b) = x$, and such that in the
commutative diagram

```text
                       κ(x)
                      ↗     ↘ γ
                   π /        ↘
                    /           ↘
              κ(y) ────φ────→ κ(b)                                       (7.1.9.1)
```

(where $\pi$, $\phi$, $\gamma$ are the homomorphisms corresponding to $p$, $f$, $g$ respectively), $\gamma$ is a
bijection.

**Proof.** As in (7.1.4), we may reduce to the case where $Y$ is integral with generic point $y$ (taking
`(I, 6.3.4, (iv))` into account); since the question is local on $X$ and $Y$, we may assume $p$ of finite type; we are
then in the situation of (7.1.4), with the additional property that $\kappa(x)$ is an extension of finite type of
$\kappa(y)$ `(I, 6.4.11)` and $\mathcal{O}_{y'}$ is Noetherian; this permits us to apply (7.1.7) and take $Y' =
\operatorname{Spec}(A')$, where $A'$ is a discrete valuation ring dominating $\mathcal{O}_{y'}$ and whose field of
fractions is $\kappa(x)$. We have thus defined a commutative diagram (7.1.9.1) where $\gamma$ is a bijection, and $\pi$
and $\phi$ correspond to the morphisms $p$ and $f$. Furthermore, since $X$ and $Y$ are locally Noetherian `(I, 6.6.2)`
and $Y'$ is integral, there is exactly one $Y$-rational map $g$ from $Y'$ to $X$ to which corresponds the isomorphism
$\gamma$ `(I, 7.1.15)`, which finishes the proof.

## 7.2. Valuative criterion of separation

**Proposition.**

<!-- label: II.7.2.1 -->

Let $X$, $Y$ be two preschemes, and $f : X \to Y$ a quasi-compact morphism. The following two conditions are equivalent:

(a) The morphism $f$ is closed.

(b) For every $x \in X$ and every specialisation $y'$ of $y = f(x)$ distinct from $y$, there exists a specialisation
$x'$ of $x$ such that $f(x') = y'$.

**Proof.** Condition (b) expresses that $f(\bar{x}) = \bar{y}$ and is thus a consequence of (a). To show that (b)
implies (a), consider a closed subset $X'$ of the underlying space $X$; let $Y' = f\bar{X'}$ and let us show that $Y' =
f(X')$. Consider the closed reduced subpreschemes of $X$ and $Y$ having $X'$ and $Y'$ respectively as their underlying
spaces `(I, 5.2.1)`; there is then a morphism $f' : X' \to Y'$ such that the diagram

```text
   X' ──f'──→ Y'
   │          │
   ↓          ↓
   X  ──f──→  Y
```

commutes `(I, 5.2.2)`, and since $f$ is quasi-compact, so too is $f'$. We are thus reduced to proving that if $f$ is a
quasi-compact and _dominant_ morphism, then

<!-- original page 142 -->

condition (b) implies that $f(X) = Y$. Indeed, let $y'$ be a point of $Y$, and let $y$ be the generic point of an
irreducible component of $Y$ containing $y'$; by (b), it suffices to show that $f^{-1}(y)$ is not empty. But this
property is a consequence of the fact that $f$ is dominant and quasi-compact `(I, 6.6.5)`.

**Corollary.**

<!-- label: II.7.2.2 -->

Let $f : X \to Y$ be a quasi-compact immersion morphism. For the underlying space $X$ to be closed in $Y$, it is
necessary and sufficient that it contain every specialisation (in $Y$) of each of its points.

**Proposition.**

<!-- label: II.7.2.3 -->

Let $Y$ be a prescheme (resp. a locally Noetherian prescheme), $f : X \to Y$ a morphism (resp. a morphism locally of
finite type). The following conditions are equivalent:

(a) $f$ is separated.

(b) The diagonal morphism $X \to X \times_{Y} X$ is quasi-compact, and for every $Y$-prescheme of the form $Y' =
\operatorname{Spec}(A)$, where $A$ is a valuation ring (resp. a discrete valuation ring), any two $Y$-morphisms from
$Y'$ to $X$ that coincide at the generic point of $Y'$ are equal.

(c) The diagonal morphism $X \to X \times_{Y} X$ is quasi-compact, and for every $Y$-prescheme of the form $Y' =
\operatorname{Spec}(A)$, where $A$ is a valuation ring (resp. a discrete valuation ring), any two $Y'$-sections of $X' =
X_{(Y')}$ that coincide at the generic point of $Y'$ are equal.

**Proof.** The equivalence of (b) and (c) results from the bijective correspondence between $Y$-morphisms from $Y'$ to
$X$ and $Y'$-sections of $X'$ `(I, 3.3.14)`. If $X$ is separated over $Y$, condition (b) is satisfied by virtue of
`(I, 7.2.2.1)`, since $Y'$ is integral. It remains to prove that (b) implies that the diagonal morphism $\Delta : X \to
X \times_{Y} X$ is closed, and it comes to the same to show that it satisfies the criterion of (7.2.2). So let $z$ be a
point of the diagonal $\Delta(X)$, and $z' \neq z$ a specialisation of $z$ in $X \times_{Y} X$. There exists then
(7.1.4) a valuation ring $A$ and a morphism $f$ from $Y' = \operatorname{Spec}(A)$ to $X \times_{Y} X$ which sends the
closed point $a$ of $Y'$ to $z'$ and the generic point $b$ of $Y'$ to $z$; this morphism makes $Y'$ into an $(X
\times_{Y} X)$-prescheme, and _a fortiori_ a $Y$-prescheme. If we compose $f$ with the two projections of $X \times_{Y}
X$, we obtain two $Y$-morphisms $g_{1}$, $g_{2}$ from $Y'$ to $X$, which by hypothesis coincide at the point $b$; they
are therefore equal to a single morphism $g$, which means `(I, 5.3.1)` that $f$ factors as $f = \Delta \circ g$, whence
$z' \in \Delta(X)$. When one supposes $Y$ locally Noetherian and $f$ locally of finite type, $X \times_{Y} X$ is locally
Noetherian `(I, 6.6.7)`; one may then take up the preceding argument by supposing that $A$ is a discrete valuation ring,
by virtue of (7.1.9).

**Remarks.**

<!-- label: II.7.2.4 -->

(i) The hypothesis that the morphism $\Delta$ is quasi-compact is always satisfied when $Y$ is locally Noetherian and
$f$ locally of finite type, since $X \times_{Y} X$ is then locally Noetherian `(I, 6.6.4, (i))`. In the general case, it
also means that for every covering $(U_{\alpha})$ of $X$ by affine opens, the sets $U_{\alpha} \cap U_{\beta}$ are
quasi-compact.

(ii) For $f$ to be separated, it suffices that condition (b) or condition (c) be satisfied for a valuation ring $A$
which is _complete_ and whose residue field is _algebraically closed_; this follows in fact from the proof of (7.2.3)
and from (7.1.4).

<!-- original page 143 -->

## 7.3. Valuative criterion of properness

**Proposition.**

<!-- label: II.7.3.1 -->

Let $A$ be a valuation ring, $Y = \operatorname{Spec}(A)$, $b$ the generic point of $Y$, $X$ an integral _scheme_, and
$f : X \to Y$ a _closed_ morphism such that $f^{-1}(b)$ reduces to a single point $x$ and the corresponding homomorphism
$\kappa(b) \to \kappa(x)$ is bijective. Then $f$ is an isomorphism.

**Proof.** Since $f$ is closed and dominant, $f(X) = Y$; it suffices `(I, 4.2.2)` to prove that for every $y' \neq b$ in
$Y$ there exists exactly one point $x'$ such that $f(x') = y'$ and the corresponding homomorphism $\mathcal{O}_{y'} \to
\mathcal{O}_{x'}$ is bijective, for then $f$ will be a homeomorphism. Now if $f(x') = y'$, $\mathcal{O}_{x'}$ is a local
ring contained in $K = \kappa(x) = \kappa(b)$ and dominating $\mathcal{O}_{y'}$; the latter is the local ring $A_{y'}$,
hence a valuation ring (7.1.1) having $K$ as field of fractions. On the other hand, $\mathcal{O}_{x'} \neq K$, since
$x'$ is not the generic point of $X$ `(0, 2.1.3)`; we conclude that $\mathcal{O}_{x'} = \mathcal{O}_{y'}$. Since $X$ is
an integral scheme, the relation $\mathcal{O}_{x'} = \mathcal{O}_{x''}$ entails $x' = x''$ `(I, 8.2.2)`, which concludes
the proof.

**(7.3.2)**

<!-- label: II.7.3.2 -->

Let $A$ be a valuation ring, $Y = \operatorname{Spec}(A)$, $b$ the generic point of $Y$, so that $\mathcal{O}_{b} =
\kappa(b)$ is equal to $K$, the field of fractions of $A$; let $f : X \to Y$ be a morphism. We know `(I, 7.1.4)` that
the _rational $Y$-sections_ of $X$ are in bijective correspondence with the _germs_ of $Y$-sections (defined in
neighbourhoods of $b$) at the point $b$, whence a canonical map

$$ \Gamma_{rat}(X/Y) \to \Gamma(f^{-1}(b)/\operatorname{Spec}(K)) (7.3.2.1) $$

the elements of $\Gamma(f^{-1}(b)/\operatorname{Spec}(K))$ being identified, by definition `(I, 3.4.5)`, with the points
of $f^{-1}(b) = X \otimes_{A} K$ that are rational over $K$. When $f$ is _separated_, it follows from `(I, 5.4.7)` that
the map (7.3.2.1) is _injective_, since $Y$ is an integral scheme.

Composing (7.3.2.1) with the canonical map $\Gamma(X/Y) \to \Gamma_{rat}(X/Y)$ `(I, 7.1.2)`, we obtain a canonical map

$$ \Gamma(X/Y) \to \Gamma(f^{-1}(b)/\operatorname{Spec}(K)). (7.3.2.2) $$

When $f$ is _separated_, this map is again _injective_ `(I, 5.4.7)`.

**Proposition.**

<!-- label: II.7.3.3 -->

Let $A$ be a valuation ring with field of fractions $K$, $Y = \operatorname{Spec}(A)$, $b$ the generic point of $Y$, and
$f : X \to Y$ a _separated_ and _closed_ morphism. Then the canonical map (7.3.2.2) is bijective (which amounts to
saying that it is _surjective_, and implies that the rational $Y$-sections of $X$ are _everywhere defined_).

**Proof.** Let $x$ be a point of $f^{-1}(b)$ rational over $K$. Since $f$ is separated, so too is the morphism
$f^{-1}(b) \to \operatorname{Spec}(K)$ corresponding to $f$ `(I, 5.5.1, (iv))`, and every section of $f^{-1}(b)$ being a
closed immersion `(I, 5.4.6)`, ${x}$ is closed in $f^{-1}(b)$. Consider the closed reduced subprescheme $X'$ of $X$
having for underlying space the closure $\bar{x}$ of ${x}$ in $X$. It is clear that the restriction of $f$ to $X'$
verifies the hypotheses of (7.3.1), and is therefore an isomorphism of $X'$ onto $Y$, whose inverse isomorphism is the
sought-for $Y$-section of $X$.

**(7.3.4)**

<!-- label: II.7.3.4 -->

To state the two following results, we make use of a terminology that will be justified and discussed in chapter IV: if
$F$ is a subset

<!-- original page 144 -->

of a prescheme $Y$, we call _codimension of $F$ in $Y$_, denoted $codim_{Y} F$, the lower bound of the integers
$\dim(\mathcal{O}_{z})$ as $z$ runs through $F$.

**Corollary.**

<!-- label: II.7.3.5 -->

Let $Y$ be a locally Noetherian reduced prescheme, $N$ the set of points $y \in Y$ where $Y$ is not regular
`(0, 4.1.4)`; suppose that $codim_{Y} N \geq 2$. Let $f : X \to Y$ be a morphism of finite type, both separated and
closed, and let $g$ be a rational $Y$-section of $X$; if $Y'$ is the set of points of $Y$ where $g$ is not defined (a
set which is closed `(I, 7.2.1)`), then $codim_{Y} Y' \geq 2$.

**Proof.** It suffices to prove that $g$ is defined at every point $z \in Y$ such that $\dim \mathcal{O}_{z} \leq 1$. If
$\dim \mathcal{O}_{z} = 0$, $z$ is the generic point of an irreducible component of $Y$ `(I, 1.1.14)`, so belongs to
every everywhere dense open subset of $Y$, and in particular to the domain of definition of $g$. Suppose then that $\dim
\mathcal{O}_{z} = 1$; $\mathcal{O}_{z}$ is then by hypothesis a regular Noetherian local ring, hence (7.1.6) a discrete
valuation ring. Let $Z = \operatorname{Spec}(\mathcal{O}_{z})$; since $U = Y \setminus Y'$ is everywhere dense, $U \cap
Z$ is not empty `(I, 2.4.2)`; let $g'$ be the rational map from $Z$ to $X$ induced by $g$ `(I, 7.2.8)`; it suffices to
show that $g'$ is a _morphism_ `(I, 7.2.9)`. Now, $g'$ may be regarded as a rational $Z$-section of the $Z$-prescheme
$f^{-1}(Z) = X \times_{Y} Z$; it is clear that the morphism $f^{-1}(Z) \to Z$ corresponding to $f$ is closed, and it
follows from `(I, 5.5.1, (i))` that it is separated; we conclude from (7.3.3) that $g'$ is everywhere defined; since $Z$
is reduced and $X$ is separated over $Y$, $g'$ is a morphism `(I, 7.2.2)`.

**Corollary.**

<!-- label: II.7.3.6 -->

Let $S$ be a locally Noetherian prescheme, and $X$, $Y$ two $S$-preschemes; suppose $Y$ reduced and, furthermore, that
the set $N$ of points $y \in Y$ where $Y$ is not regular is such that $codim_{Y} N \geq 2$; suppose finally that the
structure morphism $X \to S$ is proper. Let $f$ be an $S$-rational map from $Y$ to $X$, and let $Y'$ be the set of
points of $Y$ where $f$ is not defined; then $codim_{Y} Y' \geq 2$.

**Proof.** We know `(I, 7.1.2)` that the $S$-rational maps from $Y$ to $X$ may be identified with the $Y$-rational
sections of $X \times_{S} Y$; since the structure morphism $X \times_{S} Y \to Y$ is closed (5.4.1), we may apply
(7.3.5), whence the corollary.

**Remark.**

<!-- label: II.7.3.7 -->

The hypotheses made on $Y$ in (7.3.5) and (7.3.6) will be satisfied in particular when $Y$ is _normal_ `(0, 4.1.4)`, by
virtue of (7.1.6).

We can characterise the universally closed (resp. proper) morphisms by a converse of (7.3.3):

**Theorem.**

<!-- label: II.7.3.8 -->

Let $Y$ be a prescheme (resp. a locally Noetherian prescheme), $f : X \to Y$ a quasi-compact separated morphism (resp. a
morphism of finite type). The following conditions are equivalent:

(a) $f$ is universally closed (resp. proper).

(b) For every $Y$-scheme of the form $Y' = \operatorname{Spec}(A)$, where $A$ is a valuation ring (resp. a discrete
valuation ring) with field of fractions $K$, the canonical map

```text
  Hom_Y(Y', X) → Hom_Y(Spec(K), X)
```

corresponding to the canonical injection $A \to K$ is surjective (resp. bijective).

<!-- original page 144 (cont.) → 145 -->

(c) For every $Y$-scheme of the form $Y' = \operatorname{Spec}(A)$, where $A$ is a valuation ring (resp. a discrete
valuation ring), the canonical map (7.3.2.2) relative to the $Y'$-prescheme $X_{(Y')}$ is surjective (resp. bijective).

**Proof.** The equivalence of (b) and (c) follows immediately from `(I, 3.3.14)`. (a) implies (c), since (a) entails, in
either hypothesis, that $f_{(Y')}$ is separated `(I, 5.5.1, (iv))` and closed, and it suffices to apply (7.3.3). It
remains to prove that (b) implies (a). Place ourselves first in the case where $Y$ is arbitrary, $f$ separated and
quasi-compact. If condition (b) is satisfied by $f$, it is also satisfied by $f_{(Y'')} : X_{(Y'')} \to Y''$, where
`Y''` is an arbitrary $Y$-prescheme, by virtue of the equivalence of (b) and (c) and of the fact that $X_{(Y'')}
\times_{Y''} Y' = X \times_{Y} Y'$ for every morphism $Y' \to Y''$ `(I, 3.3.9.1)`; since moreover $f_{(Y'')}$ is
separated and quasi-compact when $f$ is `(I, 5.5.1, (iv) and 6.6.4, (iii))`, we are reduced to proving that (b) implies
that $f$ is closed. For this, it suffices to verify condition (b) of (7.2.1). Let then $x \in X$, $y'$ a specialisation
of $y = f(x)$, distinct from $y$; by virtue of (7.1.4), there is a scheme $Y'$, spectrum of a valuation ring, and a
separated morphism $g : Y' \to Y$ such that, if $a$ denotes the closed point and $b$ the generic point of $Y'$, one has
$g(a) = y'$, $g(b) = y$, and there exists a $\kappa(y)$-homomorphism $\kappa(x) \to \kappa(b)$. The latter corresponds
canonically to a $Y$-morphism $\operatorname{Spec}(\kappa(b)) \to X$ `(I, 2.4.6)`, and it follows from (b) that there
exists a $Y$-morphism $h : Y' \to X$ to which the previous morphism corresponds. We then have $h(b) = x$; if we set
$h(a) = x'$, then $x'$ is a specialisation of $x$, and we have $f(x') = f(h(a)) = g(a) = y'$.

If now $Y$ is locally Noetherian and $f$ of finite type, hypothesis (b) implies first that $f$ is _separated_, by virtue
of (7.2.3), the diagonal morphism $X \to X \times_{Y} X$ being quasi-compact (7.2.4). Moreover, to verify that $f$ is
proper, it suffices to show that $f_{(Y'')} : X_{(Y'')} \to Y''$ is closed for every $Y$-prescheme `Y''` of finite type,
taking (5.6.3) into account. Since `Y''` is then locally Noetherian, we may resume the reasoning made in the first case,
taking for $Y'$ a spectrum of a discrete valuation ring and applying (7.1.9) instead of (7.1.4).

**Remarks.**

<!-- label: II.7.3.9 -->

(i) When $Y$ is an arbitrary prescheme and $f$ a separated morphism, for $f$ to be universally closed, it suffices that
condition (b) or condition (c) be satisfied for the valuation rings $A$ that are _complete_ and whose residue field is
_algebraically closed_; this follows from the proof above and from (7.1.4).

(ii) From criterion (c) of (7.3.8) we deduce a new proof of the fact that a projective morphism $X \to Y$ is closed
(5.5.3), closer to the classical methods. One may indeed suppose $Y$ affine, and consequently $X$ identified with a
closed subprescheme of a projective bundle $\mathbb{P}^{n}_{Y}$ (5.3.3); to prove that $X \to Y$ is closed, it suffices
to verify that the structure morphism $\mathbb{P}^{n}_{Y} \to Y$ is closed, and criterion (c) of (7.3.8), combined with
(4.1.3.1), shows that we are reduced to proving the following fact: _if $Y$ is the spectrum of a valuation ring $A$ with
field of fractions $K$, every point of $\mathbb{P}^{n}_{Y}$ with values in $K$ comes (by restriction to the generic
point of $Y$) from a point of $\mathbb{P}^{n}_{Y}$ with values in $A$._ Indeed, every invertible
$\mathcal{O}_{Y}$-module is trivial `(I, 2.4.8)`; therefore, by (4.2.6), a point of $\mathbb{P}^{n}_{Y}$ with values in
$K$ is identified with a class of elements $(\zeta c_{0}, \zeta c_{1}, \cdots, \zeta c_{n})$ of $K$, where $\zeta \neq
0$ and the $c_{i}$ are elements of $K$ not all zero. Now, by multiplying the $c_{i}$ by an element of $A$ of

<!-- original page 145 → 146 -->

suitable valuation, one may suppose that the $c_{i}$ all belong to $A$ and that at least one of them is invertible. But
then (4.2.6) the system $(c_{0}, \cdots, c_{n})$ also defines a point of $\mathbb{P}^{n}_{Y}$ with values in $A$, which
proves our assertion.

(iii) The criteria (7.2.3) and (7.3.8) are especially convenient when one considers the data of a $Y$-prescheme $X$ as
equivalent to the data of the functor

$$ X(Y') = \operatorname{Hom}_{Y}(Y', X) $$

in a $Y$-prescheme $Y'$; these criteria will allow us, for example, to prove that under certain conditions the "Picard
schemes" are proper.

**Corollary.**

<!-- label: II.7.3.10 -->

Let $Y$ be an integral scheme (resp. an integral locally Noetherian scheme), $X$ an integral scheme, and $f : X \to Y$ a
dominant morphism.

(i) If $f$ is quasi-compact and universally closed, every valuation ring whose field of fractions is the field $R(X)$ of
rational functions on $X$ and which dominates a local ring of $Y$ also dominates a local ring of $X$.

(ii) Conversely, suppose $f$ of finite type, and that the property stated in (i) is satisfied by every valuation ring
(resp. every discrete valuation ring) having $R(X)$ as field of fractions. Then $f$ is proper.

**Proof.** Note first that the hypotheses imply, in any case, that $f$ is separated `(I, 5.5.9)`.

(i) Let $K = R(Y)$, $L = R(X)$, $y$ a point of $Y$, $A$ a valuation ring having $L$ as field of fractions and dominating
$\mathcal{O}_{y}$; the injection $\mathcal{O}_{y} \to A$ defines a morphism $h$ of $Y' = \operatorname{Spec}(A)$ into
$Y$ `(I, 2.4.4)` such that $h(a) = y$, in which we denote by $a$ the closed point of $Y'$; moreover, if $\eta$ is the
generic point of $Y$, which is also that of $\operatorname{Spec}(\mathcal{O}_{y})$, one has $h(b) = \eta$, denoting by
$b$ the generic point of $Y'$ (since $K \subset L$ by hypothesis). If $\xi$ is the generic point of $X$, one has
$\kappa(\xi) = \kappa(b) = L$ by hypothesis, whence a $Y$-morphism $g : \operatorname{Spec}(L) \to X$ such that $g(b) =
\xi$; by virtue of (7.3.8), $g$ comes from a $Y$-morphism $g' : Y' \to X$. If $x = g'(a)$, it is clear that $A$
dominates $\mathcal{O}_{x}$.

(ii) The question being local on $Y$, we may always suppose $Y$ affine (resp. affine and Noetherian). Since $f$ is of
finite type, we may apply Chow's lemma (5.6.1) in both cases. There is then a projective morphism $p : P \to Y$, an
immersion morphism $j : X' \to P$, and a projective, surjective, and birational morphism $g : X' \to X$ (with $X'$
integral) such that the diagram

```text
   P ←──j── X'
   │        │
  p│       g│
   ↓        ↓
   Y ←──f── X
```

commutes. It suffices to prove that $j$ is a _closed_ immersion, for then $f \circ g = p \circ j$ will be a projective
morphism, hence proper, and since $g$ is surjective, $f$ will also be proper (5.4.3). Let $Z$ be the closed reduced
subprescheme of $P$ having $j\bar{X'}$ as underlying space `(I, 5.2.1)`; since $X'$ is integral, $j$ factors as $i \circ
h$, where $i : Z \to P$ is the canonical injection, $h : X' \to Z$ a dominant open immersion `(I, 5.2.3)`, and $Z$ is
integral;

<!-- original page 146 → 147 -->

moreover, $Z$ is projective over $Y$, and we see that we may restrict to the case where $P$ is integral and $j$ dominant
and birational, and everything reduces to seeing that $j$ is surjective. So let $z \in P$; $\mathcal{O}_{z}$ is an
integral (resp. integral and Noetherian) local ring whose field of fractions is

```text
  L = R(P) = R(X') = R(X).
```

We may restrict to the case where $z$ is not the generic point of $P$. There is consequently (7.1.2 and 7.1.7) a
valuation ring (resp. a discrete valuation ring) $A$ having $L$ as field of fractions and dominating $\mathcal{O}_{z}$.
_A fortiori_, $A$ dominates $\mathcal{O}_{y}$, putting $y = p(z)$, and by hypothesis there is then an $x \in X$ such
that $A$ dominates $\mathcal{O}_{x}$. Since $g$ is proper, the first part of the proof shows that $A$ also dominates
some $\mathcal{O}_{x'}$ for an $x' \in X'$; it follows that $\mathcal{O}_{z}$ and $\mathcal{O}_{j(x')} =
\mathcal{O}_{x'}$ are allied `(I, 8.1.4)`, and since $P$ is a scheme, this entails $z = j(x')$ `(I, 8.2.2)`, which
concludes the proof.

**Corollary.**

<!-- label: II.7.3.11 -->

Let $X$, $Y$ be two integral schemes, $f : X \to Y$ a dominant, quasi-compact and universally closed morphism. Suppose
moreover $Y$ affine of (integral) ring $B$. Then $\Gamma(X, \mathcal{O}_{X})$ is canonically isomorphic to a subring of
the integral closure of $B$ in $R(X)$.

**Proof.** Indeed `(I, 8.2.1.1)`, $\Gamma(X, \mathcal{O}_{X})$ is identified with the intersection of the
$\mathcal{O}_{x}$ for $x \in X$; by virtue of (7.3.10), (7.1.2) and (7.1.3), $\Gamma(X, \mathcal{O}_{X})$ is
consequently contained in the intersection of the valuation rings containing $B$ and having $R(X)$ as field of
fractions; the conclusion then follows from (7.1.3).

**Remarks.**

<!-- label: II.7.3.12 -->

Under the hypotheses of (7.3.11), and when one supposes that $R(X)$ is an extension of finite type of $R(Y)$, one will
be able in many cases to conclude that $\Gamma(X, \mathcal{O}_{X})$ is a module of finite type over the ring $B =
\Gamma(Y, \mathcal{O}_{Y})$. This will be the case for example when $B$ is an algebra of finite type over a field, for
one knows then that the integral closure of $B$ in an extension of finite type of its field of fractions is a $B$-module
of finite type (`[13], t. I, p. 267, th. 9`); the conclusion then follows from (7.3.11) and from the fact that $B$ is
Noetherian.

In particular, _a scheme $X$ proper and affine over a field $K$ is finite._ Indeed, by virtue of (1.6.4), (5.4.6) and
`(I, 6.4.4, c))`, one may restrict to the case where $X$ is reduced. Furthermore, it will suffice to prove that each of
the closed subpreschemes of $X$ having for underlying space an irreducible component of $X$ (of which there are finitely
many) is finite over $K$, so that (taking (5.4.5) into account) one is finally reduced to the case where $X$ is
integral. But then the result follows from the remarks made above.

In chapter III we shall recover this last proposition by other methods and as a consequence of more general results,
showing that if $f : X \to Y$ is proper and $Y$ locally Noetherian, $f_{*}(\mathcal{F})$ is coherent for every coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$ (`III, 4.4.2`).

Let us note finally that the criterion (7.3.10) is taken as the _definition_ of proper morphisms in classical algebraic
geometry. We have mentioned it only for that reason, criterion (7.3.8) seeming more manageable in all the applications
known to us.

<!-- original page 147 → 148 -->

## 7.4. Algebraic curves and function fields of dimension `1`

The aim of this number is to show how the classical notion of algebraic curve (as it is presented, for example, in the
book of C. Chevalley `[23]`) is formulated in the language of schemes. _Throughout this number, $k$ denotes a field, all
schemes considered are $k$-schemes of finite type, and all morphisms are $k$-morphisms._

**Proposition.**

<!-- label: II.7.4.1 -->

Let $X$ be a prescheme of finite type over $k$ (hence Noetherian); let $x_{i}$ ($1 \leq i \leq n$) be the generic points
of the irreducible components $X_{i}$ of $X$, and let $K_{i} = \kappa(x_{i})$ ($1 \leq i \leq n$). The following
conditions are equivalent:

(a) Each of the $K_{i}$ is an extension of $k$ whose transcendence degree is equal to `1`.

(b) For every closed point $x$ of $X$, the local ring $\mathcal{O}_{x}$ is of dimension `1` (7.1.5).

(c) The irreducible closed subsets of $X$ distinct from the $X_{i}$ are the closed points of $X$.

**Proof.** Since $X$ is quasi-compact, every irreducible closed subset $F$ of $X$ contains a closed point `(0, 2.1.3)`.
By virtue of `(I, 2.4.2)`, there is a bijective correspondence between the prime ideals of $\mathcal{O}_{x}$ and the
irreducible closed subsets of $X$ containing $x$ `(I, 1.1.14)`; the equivalence of (b) and (c) follows immediately. On
the other hand, if $\mathfrak{p}_{\alpha}$ ($1 \leq \alpha \leq r$) are the minimal prime ideals of the Noetherian local
ring $\mathcal{O}_{x}$, the local rings $\mathcal{O}_{x}/\mathfrak{p}_{\alpha}$ are integral and have for fields of
fractions the $K_{i}$ such that $x \in X_{i}$. Furthermore, we know (`[1], p. 4-06, th. 2`) that the dimension of a
local integral $k$-algebra of finite type is equal to the transcendence degree over $k$ of its field of fractions.
Finally, the dimension of $\mathcal{O}_{x}$ is the upper bound of the dimensions of the
$\mathcal{O}_{x}/\mathfrak{p}_{\alpha}$; now, condition (a) implies that these dimensions are equal to `1`, so (a)
implies (b); conversely, if $\mathcal{O}_{x}$ is of dimension `1`, none of the $\mathfrak{p}_{\alpha}$ can be equal to
the maximal ideal of $\mathcal{O}_{x}$, otherwise $\mathcal{O}_{x}$ would be of dimension `0`; therefore each of the
$\mathcal{O}_{x}/\mathfrak{p}_{\alpha}$ is of dimension `1`, which shows that (b) entails (a).

We note that under the conditions of (7.4.1) the set $X$ is _empty or infinite_, as follows immediately from
`(I, 6.4.4)`.

**Definition.**

<!-- label: II.7.4.2 -->

We call an _algebraic curve over $k$_ a nonempty algebraic _scheme_ over $k$ satisfying the conditions of (7.4.1).

In the language of dimension, which will be introduced in chapter IV, this is expressed by saying that an algebraic
curve over $k$ is a nonempty algebraic $k$-scheme all of whose irreducible components are of dimension `1`.

We note that if $X$ is an algebraic curve over $k$, the closed reduced subpreschemes $X_{i}$ ($1 \leq i \leq n$) of $X$
having for underlying spaces the irreducible components of $X$ are algebraic curves over $k$.

**Corollary.**

<!-- label: II.7.4.3 -->

Let $X$ be an irreducible algebraic curve. The only non-closed point of $X$ is its generic point. The closed subsets of
$X$ distinct from $X$ are the finite sets of closed points; these are also the only subsets of $X$ that are not
everywhere dense.

**Proof.** If a point $x \in X$ is not closed, its closure in $X$ is an irreducible closed subset of $X$, hence
necessarily the whole of $X$ by virtue of (7.4.1), and consequently

<!-- original page 148 → 149 -->

$x$ is the generic point of $X$. A closed subset $F$ of $X$ distinct from $X$ cannot contain the generic point of $X$,
so all its points are closed (in $X$, and _a fortiori_ in $F$); by considering the closed reduced subprescheme of $X$
having $F$ as underlying space `(I, 5.2.1)`, it follows therefore from `(I, 6.2.2)` that $F$ is finite and discrete. The
closure in $X$ of an infinite subset of $X$ is therefore necessarily equal to $X$.

When $X$ is an arbitrary algebraic curve, applying (7.4.3) to the irreducible components of $X$ shows that the only
non-closed points of $X$ are the generic points of those components.

**Corollary.**

<!-- label: II.7.4.4 -->

Let $X$ and $Y$ be two irreducible algebraic curves over $k$, and $f : X \to Y$ a $k$-morphism. For $f$ to be dominant,
it is necessary and sufficient that $f^{-1}(y)$ be finite for every $y \in Y$.

**Proof.** Indeed, if $f$ is not dominant, $f(X)$ is necessarily a finite subset of $Y$ by virtue of (7.4.3), so it is
not possible that $f^{-1}(y)$ be finite for every point of $Y$, since otherwise $X$ would be finite, which is absurd
(7.4.1). Conversely, if $f$ is dominant, for every $y \in Y$ distinct from the generic point $\eta$ of $Y$, $f^{-1}(y)$
is closed in $X$ since ${y}$ is closed in $Y$ (7.4.3); on the other hand, by hypothesis, $f^{-1}(y)$ does not contain
the generic point $\xi$ of $X$, hence is finite by virtue of (7.4.3). Finally, to see that when $f$ is dominant,
$f^{-1}(\eta)$ is finite, one notes that the fibre $f^{-1}(\eta)$ is an irreducible scheme of finite type over
$\kappa(\eta)$, with generic point $\xi$ (`I, 6.3.9 and 6.4.11`). Since $\kappa(\xi)$ and $\kappa(\eta)$ are extensions
of finite type of $k$, of the same transcendence degree `1`, $\kappa(\xi)$ is necessarily an extension of finite degree
of $\kappa(\eta)$, hence $\xi$ is closed in $f^{-1}(\eta)$ `(I, 6.4.2)`, and $f^{-1}(\eta)$ is consequently reduced to
the point $\xi$.

We shall see in chapter III that a proper morphism $f : X \to Y$ of Noetherian preschemes such that $f^{-1}(y)$ is
finite for every $y \in Y$ is necessarily _finite_; it will then follow from (7.4.4) that a proper dominant morphism
from an irreducible algebraic curve to an algebraic curve is finite.

**Corollary.**

<!-- label: II.7.4.5 -->

Let $X$ be an algebraic curve over $k$. For $X$ to be regular, it is necessary and sufficient that $X$ be normal, or
again that the local rings of its closed points be discrete valuation rings.

**Proof.** This follows immediately from condition (b) of (7.4.1) and from (7.1.6).

**Corollary.**

<!-- label: II.7.4.6 -->

Let $X$ be a reduced algebraic curve, and $\mathcal{A}$ a reduced coherent $\mathcal{O}(X)$-algebra; then the integral
closure $X'$ of $X$ relative to $\mathcal{A}$ (6.3.4) is a normal algebraic curve, and the canonical morphism $X' \to X$
is finite.

**Proof.** The fact that $X' \to X$ is finite follows from (6.3.10); $X'$ is therefore an algebraic $k$-scheme;
moreover, if $x_{i}$ ($1 \leq i \leq n$) are the generic points of the irreducible components of $X$, $x'_{j}$ ($1 \leq
j \leq m$) those of the irreducible components of $X'$, each of the $\kappa(x'_{j})$ is a finite algebraic extension of
one of the $\kappa(x_{i})$ (6.3.6), hence has transcendence degree `1` over $k$. $X'$ is thus indeed an algebraic curve
over $k$, and moreover one knows that $X'$ is a sum of a finite number of integral and normal schemes (6.3.6 and 6.3.7).

**(7.4.7)**

<!-- label: II.7.4.7 -->

We say that an algebraic curve $X$ over $k$ is _complete_ if it is proper over $k$.

**Corollary.**

<!-- label: II.7.4.8 -->

For a reduced algebraic curve $X$ over $k$ to be complete, it is necessary and sufficient that its normalisation $X'$ be
so.

<!-- original page 149 → 150 -->

**Proof.** Indeed, the canonical morphism $f : X' \to X$ is then finite (7.4.6), hence proper (6.1.11) and surjective
(6.3.8); if $g : X \to \operatorname{Spec}(k)$ is the structure morphism, $g$ and $g \circ f$ are therefore proper
simultaneously, as follows from (5.4.2, (ii)) and (5.4.3, (ii)), $g$ being separated by hypothesis.

**Proposition.**

<!-- label: II.7.4.9 -->

Let $X$ be a normal algebraic curve over $k$, and $Y$ a proper algebraic $k$-scheme over $k$. Then every $k$-rational
map from $X$ to $Y$ is everywhere defined, in other words is a morphism.

**Proof.** Indeed, it follows from (7.3.7) that at the points $x \in X$ where such a map is not defined, the dimension
of $\mathcal{O}_{x}$ would have to be $\geq 2$, so the set of such points is empty; the last assertion comes from
`(I, 7.2.3)`.

**Corollary.**

<!-- label: II.7.4.10 -->

A normal algebraic curve over $k$ is quasi-projective over $k$.

**Proof.** Since $X$ is a sum of a finite number of integral and normal algebraic curves (6.3.8), one may restrict to
the case where $X$ is integral (5.3.6). Since $X$ is quasi-compact, it is covered by a finite number of affine opens
$U_{i}$ ($1 \leq i \leq n$), and since each of these is of finite type over $k$, there exist an integer $n_{i}$ and a
$k$-immersion $f_{i} : U_{i} \to \mathbb{P}^{n_{i}}_{k}$ (5.3.3 and 5.3.4, (i)). Since $U_{i}$ is dense in $X$, it
follows from (7.4.9) that $f_{i}$ extends to a $k$-morphism $g_{i} : X \to \mathbb{P}^{n_{i}}_{k}$, whence a
$k$-morphism $g = (g_{1}, \cdots, g_{n})_{k}$ of $X$ into the product $P$ of the $\mathbb{P}^{n_{i}}_{k}$ over $k$.
Moreover, for each index $i$, since the restriction of $g_{i}$ to $U_{i}$ is an immersion, so too is the restriction of
$g$ to $U_{i}$ `(I, 5.3.14)`. Since the $U_{i}$ cover $X$ and $g$ is separated `(I, 5.5.1, (v))`, $g$ is an immersion of
$X$ into $P$ `(I, 8.2.8)`. Since the Segre morphism (4.3.3) gives an immersion of $P$ into a $\mathbb{P}^{N}_{k}$, this
completes the proof that $X$ is quasi-projective.

**Corollary.**

<!-- label: II.7.4.11 -->

A normal algebraic curve $X$ is isomorphic to the scheme induced on an everywhere dense open subset of a normal complete
algebraic curve $\hat{X}$, determined up to a unique isomorphism.

**Proof.** If `X_1`, `X_2` are two normal complete curves, it follows immediately from (7.4.9) that every isomorphism of
an open `U_1` dense in `X_1` onto an open `U_2` dense in `X_2` extends in a unique way to an isomorphism of `X_1` onto
`X_2`; whence the uniqueness assertion. To prove the existence of $\hat{X}$, it suffices to remark that one may regard
$X$ as a subscheme of a projective bundle $\mathbb{P}^{n}_{k}$ (7.4.10). Let $\bar{X}$ be the closure of $X$ in
$\mathbb{P}^{n}_{k}$ `(I, 9.5.11)`; since $X$ is induced by $\bar{X}$ on an open dense in $\bar{X}$ `(I, 9.5.10)`, the
generic points $x_{i}$ of the irreducible components of $\bar{X}$ are also those of the irreducible components of $X$,
and the $\kappa(x_{i})$ are the same for these two schemes, so (7.4.1) $\bar{X}$ is an algebraic curve over $k$, which
is reduced `(I, 9.5.9)` and projective over $k$ (5.5.1), hence complete (5.5.3). Let us then take for $\hat{X}$ the
normalisation of $\bar{X}$, which is again complete (7.4.8); moreover, if $h : \hat{X} \to \bar{X}$ is the canonical
morphism, the restriction of $h$ to $h^{-1}(X)$ is an isomorphism onto $X$ since $X$ is normal (6.3.4), and since
$h^{-1}(X)$ contains the generic points of the irreducible components of $\hat{X}$ (6.3.8), it is dense in $\hat{X}$,
which concludes the proof.

<!-- original page 150 → 151 -->

**Remark.**

<!-- label: II.7.4.12 -->

We shall show in chapter V that the conclusion of (7.4.10) still holds without supposing the curve normal (nor even
reduced); we shall also show that for an algebraic curve (reduced or not) to be affine, it is necessary and sufficient
that its (reduced) irreducible components be not complete.

**Corollary.**

<!-- label: II.7.4.13 -->

Let $X$ be a normal irreducible curve with field $R(X) = K$, $Y$ an integral complete curve with field $L = R(Y)$. There
is a canonical bijective correspondence between dominant $k$-morphisms $X \to Y$ and $k$-monomorphisms $L \to K$.

**Proof.** By virtue of (7.4.9), the $k$-rational maps from $X$ to $Y$ are identified with the $k$-morphisms $u : X \to
Y$. The dominant morphisms $u$ being characterised by the fact that $u(x) = y$ (denoting by $x$ and $y$ the respective
generic points of $X$ and $Y$), the corollary follows from these remarks and from `(I, 7.1.13)`.

**(7.4.14)**

<!-- label: II.7.4.14 -->

One may sharpen the result of (7.4.13) when one takes for $Y$ the projective line $\mathbb{P}^{1}_{k} =
\operatorname{Proj}(k[T_{0}, T])$, $T_{0}$ and $T$ being two indeterminates. This is indeed an integral scheme (2.4.4),
and the scheme induced on the open $D_{+}(T_{0})$ of $Y$ is isomorphic to $\operatorname{Spec}(k[T])$ (2.3.6), so the
generic point of $Y$ is the ideal `(0)` of `k[T]` and its field of rational functions $k(T)$, which shows that $Y$ is a
complete algebraic curve over $k$. Moreover, the only graded prime ideal of $S = k[T_{0}, T]$ containing $T_{0}$ and
distinct from $S_{+}$ is the principal ideal $(T_{0})$, so the complement of $D_{+}(T_{0})$ in $Y = \mathbb{P}^{1}_{k}$
reduces to a single closed point, called the _"point at infinity"_, which we denote $\infty$ (for a general study of the
relations between vector bundles and projective bundles, see 8.4). With these notations:

**Corollary.**

<!-- label: II.7.4.15 -->

Let $X$ be a normal irreducible curve with field $R(X) = K$. There exists a canonical bijective map of $K$ onto the set
of morphisms $u$ of $X$ into $\mathbb{P}^{1}_{k}$ distinct from the constant morphism of value $\infty$. For $u$ to be
dominant, it is necessary and sufficient that the corresponding element of $K$ be transcendental over $k$.

**Proof.** This statement follows immediately from (7.4.9) and from the

**Lemma.**

<!-- label: II.7.4.15.1 -->

Let $X$ be an integral prescheme over $k$, and let $K = R(X)$ be its field of rational functions. There exists a
canonical bijective map of the set $K$ onto the set of rational maps $u$ of $X$ into $\mathbb{P}^{1}_{k}$ distinct from
the constant morphism of value $\infty$. For such a rational map to be dominant, it is necessary and sufficient that the
corresponding element of $K$ be transcendental over $k$.

First of all, the rational maps of $X$ into $\mathbb{P}^{1}_{k}$ correspond bijectively to the points of
$\mathbb{P}^{1}_{k}$ with values in the extension $K$ of $k$ `(I, 7.1.12)`. If such a point is localised `(I, 3.4.5)` at
the generic point of $\mathbb{P}^{1}_{k}$, the corresponding rational map is evidently dominant. In the contrary case,
since every point of $\mathbb{P}^{1}_{k}$ distinct from the generic point is closed (7.4.3), the image of the domain of
definition $U$ of $u$ by the unique morphism $U \to \mathbb{P}^{1}_{k}$ of the class $u$ `(I, 7.2.2)` reduces to a
closed point $y$ of $\mathbb{P}^{1}_{k}$, and this morphism (which is not necessarily everywhere defined in $X$) is
therefore not dominant; by abuse of language, one then says that the rational map $u$ is "constant, of value $y$". It
remains to put in bijective correspondence the points of $\mathbb{P}^{1}_{k}$ with values in $K$ of locality
`(I, 3.4.5)` distinct from $\infty$ and the elements of $K$, and to verify that the locality of such a point is the
generic point of $\mathbb{P}^{1}_{k}$ if and only if it corresponds to an

<!-- original page 151 → 152 -->

element transcendental over $k$. Now, this verification is immediate from (4.2.6, example 1°).

**Corollary.**

<!-- label: II.7.4.16 -->

Let $X$, $Y$ be two algebraic curves over $k$, normal, complete and irreducible; let $K = R(X)$, $L = R(Y)$ be their
fields. There is a canonical bijective correspondence between the set of $k$-isomorphisms $X \xrightarrow{\sim} Y$ and
the set of $k$-isomorphisms $L \xrightarrow{\sim} K$.

**Proof.** This is an evident consequence of (7.4.13).

**(7.4.17)**

<!-- label: II.7.4.17 -->

The corollary (7.4.16) shows that an algebraic curve over $k$, normal, complete and irreducible, is _determined by its
field of rational functions $K$ up to a unique isomorphism_; by definition, $K$ is an extension of finite type of $k$,
of transcendence degree `1` (what is classically called a _field of algebraic functions of one variable_). Moreover:

**Proposition.**

<!-- label: II.7.4.18 -->

For every extension $K$ of $k$, of finite type and of transcendence degree `1`, there exists a normal, complete and
irreducible algebraic curve $X$ such that $R(X) = K$ (determined up to unique isomorphism). The set of local rings of
$X$ is identified `(I, 8.2.1)` with the set consisting of $K$ and the valuation rings containing $k$ and having $K$ as
field of fractions.

**Proof.** Indeed, $K$ is an extension of finite degree of a pure transcendental extension $k(T)$ of $k$, which is
identified, as we have seen, with the field of rational functions of the projective line $Y = \mathbb{P}^{1}_{k}$. Let
$X$ be the integral closure of $Y$ relative to $K$ (6.3.4); $X$ is a normal algebraic curve with field $K$ (6.3.7), and
it is complete since the morphism $X \to Y$ is finite (7.4.6). The local rings $\mathcal{O}_{x}$ of $X$ are: the field
$K$ when $x$ is the generic point; if $x$ is distinct from the generic point, $\mathcal{O}_{x}$ is a discrete valuation
ring containing $k$ and having $K$ as field of fractions (7.4.5). Conversely, let $A$ be such a ring; since the morphism
$X \to \operatorname{Spec}(k)$ is proper and $A$ dominates $k$, $A$ dominates a local ring $\mathcal{O}_{x}$ of $X$
(7.3.10); the latter being a valuation ring having $K$ as field of fractions, is therefore necessarily equal to $A$.

**Remarks.**

<!-- label: II.7.4.19 -->

It follows from (7.4.16) and (7.4.18) that _the data of an algebraic curve over $k$, normal, complete and irreducible,
is essentially equivalent to the data of an extension $K$ of $k$, of finite type and of transcendence degree `1`_. We
note that if $k'$ is an extension of the base field $k$, $X \otimes_{k} k'$ will again be a complete algebraic curve
over $k'$ (5.4.2, (iii)), but in general it will be neither reduced nor irreducible. It will be so, however, if $K$ is a
separable extension of $k$ and $k$ is algebraically closed in $K$ (which is expressed, in a classical terminology that
we shall not follow, by saying that $K$ is a "regular extension" of $k$). But even in this case, it can happen that $X
\otimes_{k} k'$ is not normal. The reader will find details on these questions in chapter IV.

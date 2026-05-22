<!-- original page 86 -->

## §5. Dimension and depth in preschemes

This section confines itself to restating, in the geometric language and with various complements of a technical nature,
the notions and results of commutative algebra exposed in Chapter 0, §§16 and 17.

### 5.1. Dimension of preschemes

**(5.1.1)**

<!-- label: IV.5.1.1 -->

Let $A$ be a ring and $\mathfrak{J}$ an ideal of $A$. Recall `(0, 16.1)` that the definitions of the theory of dimension
of a ring `(0, 16.1.1)` and those of the theory of combinatorial dimension of topological spaces `(0, 14.1.2)` give the
following relations:

```text
  dim(Spec(A)) = dim(A)                                  (5.1.1.1)

  dim(V(𝔍)) = dim(A/𝔍)                                   (5.1.1.2)

  codim(V(𝔍), Spec(A)) = ht(𝔍)                           (5.1.1.3)
```

*(5.1.1.4)* $\operatorname{Spec}(A)$ is a catenary space ⟺ $A$ is a catenary ring.

*(5.1.1.5)* $\operatorname{Spec}(A)$ is equidimensional ⟺ $A$ is equidimensional ⟺ the minimal prime ideals
$\mathfrak{p}_{\alpha}$ of $A$ are such that the dimensions of the rings $A/\mathfrak{p}_{\alpha}$ are all equal.

*(5.1.1.6)* $\operatorname{Spec}(A)$ is equicodimensional ⟺ $A$ is equicodimensional ⟺ all the maximal ideals of $A$
have the same height.

Recall that a Noetherian ring $A$ is said to be **biequidimensional** if $\operatorname{Spec}(A)$ is biequidimensional,
that is to say if $\operatorname{Spec}(A)$ is Noetherian and $A$ is equidimensional, equicodimensional, catenary, and of
finite dimension.

**Proposition (5.1.2).**

<!-- label: IV.5.1.2 -->

*Let $X$ be a prescheme, $Y$ an irreducible closed part of $X$, $y$ the generic point of $Y$. One has*

$$ codim(Y, X) = \dim(\mathcal{O}_{X,y}) (5.1.2.1) $$

Indeed `(I, 2.4.2)`, the irreducible closed parts of $X$ containing $y$ are canonically in bijective correspondence with
the irreducible closed parts of $\operatorname{Spec}(\mathcal{O}_{X,y})$, hence in bijective correspondence with the
prime ideals of $\mathcal{O}_{X,y}$, and `(5.1.2.1)` follows from the definitions.

In particular, one recovers in this way the fact that the generic points of the irreducible components of $X$ are the
only points $x \in X$ such that $\dim(\mathcal{O}_{x}) = 0$ `(I, 1.1.14)`.

<!-- original page 87 -->

**Corollary (5.1.3).**

<!-- label: IV.5.1.3 -->

*For every closed part $Y$ of a prescheme $X$, one has*

```text
  codim(Y, X) = inf_{y ∈ Y} dim(𝒪_{X,y}).                (5.1.3.1)
```

*Moreover, if $X$ is locally Noetherian, one has, for every $x \in Y$,*

```text
  codim_x(Y, X) = inf_{y ∈ Y, x ∈ ‾{y}} dim(𝒪_{X,y}).    (5.1.3.2)
```

The relation `(5.1.3.2)` indeed follows from `(5.1.3.1)` and from `(0, 14.2.6)`.

This corollary allows us to *define*, for any part $Y$ of a prescheme $X$, the **codimension** $codim(Y, X)$ of $Y$ in
$X$ as equal to the second member of `(5.1.3.1)`.

**Proposition (5.1.4).**

<!-- label: IV.5.1.4 -->

*For every prescheme $X$, one has*

```text
  dim(X) = sup_{x ∈ X} (dim(𝒪_x)).                       (5.1.4.1)
```

*If every irreducible closed part of $X$ contains a closed point, one has also*

```text
  dim(X) = sup_{x ∈ F} (dim(𝒪_x))                        (5.1.4.2)
```

*where $F$ is the set of closed points of $X$.*

It suffices to remark (by virtue of `(I, 2.4.2)`) that the chains of irreducible closed parts of $X$ correspond
bijectively with the chains of irreducible closed parts of a local scheme of $X$; when every irreducible closed part of
$X$ contains a closed point, one can clearly restrict to the local schemes at the closed points of $X$.

We note that every irreducible closed part of $X$ contains a closed point when $X$ is quasi-compact $(0_{I}, 2.1.3)$; we
shall see a little further on `(5.1.11)` that the same holds when $X$ is locally Noetherian.

**Corollary (5.1.5).**

<!-- label: IV.5.1.5 -->

*For a prescheme $X$ to be catenary it is necessary and sufficient that, for every $x \in X$, the local ring
$\mathcal{O}_{x}$ be catenary. If moreover every irreducible closed part of $X$ contains a closed point, it suffices,
for $X$ to be catenary, that $\mathcal{O}_{x}$ be catenary for every closed point $x$ of $X$.*

The reasoning is the same as in `(5.1.4)`, since one is comparing chains of irreducible closed parts having the same
extremities.

**(5.1.6)**

<!-- label: IV.5.1.6 -->

We shall now examine the more special properties tied to Noetherian hypotheses.

Recall `(0, 16.2.3)` that a Noetherian local ring $A \neq 0$ is of finite dimension, equal to the minimum number of
generators of an ideal of definition of $A$; for every prime ideal $\mathfrak{p}$ of $A$, the height of $\mathfrak{p}$,
equal to $\dim(A_{\mathfrak{p}})$, is therefore also finite. These properties, together with `(5.1.2)`, `(5.1.3)`, and
`(5.1.4)`, show that:

**Proposition (5.1.7).**

<!-- label: IV.5.1.7 -->

*For every non-empty closed part $Y$ of a locally Noetherian prescheme $X$, $codim(Y, X)$ is finite. If $X$ is
Noetherian and affine and $Y$ an irreducible closed part of $X$, $codim(Y, X)$ is equal to the minimum number of
sections $s_{i}$ of $\mathcal{O}_{X}$ over $X$ such that $Y$ is an irreducible component of the set of $x \in X$ such
that $s_{i}(x) = 0$ for every $i$.*

**Corollary (5.1.8).**

<!-- label: IV.5.1.8 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-Module, $f$ a section of
$\mathcal{L}$ over $X$. Then every irreducible component of the set $Z$*

<!-- original page 88 -->

*of $x \in X$ such that $f(x) = 0$ is of codimension $\leq 1$ in $X$; it is of codimension `1` if $Z$ contains no
irreducible component of $X$.*

One can restrict to the case where $\mathcal{L} = \mathcal{O}_{X}$. If $y$ is a generic point of an irreducible
component $Y$ of $Z$, the ideal $(f_{y})$ of $\mathcal{O}_{X,y}$ must be such that $\mathcal{O}_{X,y}/(f_{y})$ has only
one prime ideal, which means that $f_{y}$ generates an ideal of definition of the Noetherian local ring
$\mathcal{O}_{X,y}$; one thus has $codim(Y, X) \leq 1$ `(5.1.7)`; if $Z$ contains no irreducible component of $X$, one
cannot have $codim(Y, X) = 0$ by virtue of `(0, 14.2.1)`.

**Proposition (5.1.9).**

<!-- label: IV.5.1.9 -->

*Let $X$ be a locally Noetherian prescheme, $Y$ a closed part of $X$. If $x \in Y$ is such that $\mathcal{O}_{X,x}$ is a
catenary ring, one has*

```text
  codim_x(Y, X) = dim(𝒪_{X,x}) − codim(‾{x}, Y)          (5.1.9.1)
                = dim(𝒪_{X,x}) − dim(𝒪_{Y,x}).
```

Let $Y_{i}$ ($1 \leq i \leq n$) be the irreducible components of $Y$ containing $x$ (which are finite in number since
$Y$ is locally Noetherian), and let $y_{i}$ be the generic point of $Y_{i}$. If one sets $A = \mathcal{O}_{X,x}$, and if
$\mathfrak{p}_{i}$ is the prime ideal of $A$ corresponding to $Y_{i} \cap \operatorname{Spec}(A)$, the irreducible
closed parts of $Y$ containing $x$ correspond bijectively with the prime ideals of $A$ containing one of the
$\mathfrak{p}_{i}$, so `dim(𝒪_{Y,x}) = sup_i dim(A/𝔭_i)`; on the other hand, one has $\mathcal{O}_{X,y_{i}} =
A_{\mathfrak{p}_{i}}$, and the hypothesis on $A$ entails `dim(A) = dim(A/𝔭_i) + dim(A_{𝔭_i})` `(0, 16.1.4)`; the
conclusion thus follows from the relation `codim_x(Y, X) = inf_i (dim(𝒪_{X,y_i}))` (`(5.1.2)` and `(0, 14.2.6)`).

**Proposition (5.1.10).**

<!-- label: IV.5.1.10 -->

*(i) In every prescheme $X$, every non-empty locally constructible part $E$ contains a point $x$ such that ${x}$ is a
locally closed part of $X$ (or, what amounts to the same, such that $x$ is isolated in $\overline{x}$).*

*(ii) Let $X$ be a locally Noetherian prescheme, $x$ a point of $X$ such that ${x}$ is locally closed in $X$; then one
has $\dim(\overline{x}) \leq 1$; every point $y \neq x$ of $\overline{x}$ is consequently closed in $X$.*

(i) The result is a particular case of the following lemma:

**Lemma (5.1.10.1).**

<!-- label: IV.5.1.10.1 -->

*Let $X$ be a topological space having the following property: for every locally closed part $Z \neq \emptyset$ of $X$,
there exists a part $Z'$ of $Z$, locally closed in $X$ (or in $Z$, what amounts to the same), and a point $x \in Z'$,
closed in $Z'$. Then every locally closed part $Z \neq \emptyset$ of $X$ contains a point $x$ isolated in
$\overline{x}$.*

Indeed, let $Z' \subset Z$ be a locally closed part of $Z$ containing a point $x$ such that $x$ is closed in $Z'$. There
is an open neighbourhood $U$ of $x$ in $X$ such that $Z' \cap U$ is closed in $U$, hence $x$ is also closed in $U$; this
means that $U \cap \overline{x} = {x}$, in other words that $x$ is isolated in $\overline{x}$.

The lemma applies to every underlying space of a prescheme $X$, for $Z$ is then also the underlying space of a prescheme
`(I, 5.2.1)` and it suffices to take for $Z'$ an affine open in $Z$, which is a quasi-compact Kolmogorov space, hence
contains a closed point $(0_{I}, 2.1.3)$.

<!-- original page 89 -->

(ii) Let $Z$ be the reduced sub-prescheme of $X$ having $\overline{x}$ as underlying space; the hypothesis entails that
${x}$ is open in $Z$; therefore, for every $z \in Z$, the generic point $x$ of $\operatorname{Spec}(\mathcal{O}_{Z,z})$
is isolated in $\operatorname{Spec}(\mathcal{O}_{Z,z})$; but the ring $A = \mathcal{O}_{Z,z}$ is an integral Noetherian
local ring, and the hypothesis entails that there exists $f \in A$ such that $A_{f}$ is a field; one knows `(0, 16.3.3)`
that this entails $\dim(A) \leq 1$. Since $\dim(\mathcal{O}_{Z,z}) \leq 1$ for every $z \in Z$, one indeed has $\dim(Z)
\leq 1$.

**Corollary (5.1.11).**

<!-- label: IV.5.1.11 -->

*If $X$ is a locally Noetherian prescheme, every non-empty closed part of $X$ contains a closed point.*

Indeed, every closed part of $X$ is constructible $(0_{III}, 9.1.1 and 9.1.5)$ and it suffices to apply `(5.1.10)`.

**(5.1.12)**

<!-- label: IV.5.1.12 -->

Let $X$ be a prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of finite type, $S = Supp(\mathcal{F})$
its support, which is closed in $X$ $(0_{I}, 5.2.2)$. If, for every $x \in X$, one considers $Supp(\mathcal{F}_{x})$ as
a closed part of the local scheme $\operatorname{Spec}(\mathcal{O}_{x})$, one has, by definition `(0, 16.1.7)`
`dim(ℱ_x) = dim(Supp(ℱ_x))`; but one has

```text
  Supp(ℱ_x) = S ∩ Spec(𝒪_{X,x}) = Spec(𝒪_{S,x})
```

where, in the last term, $S$ denotes any closed sub-prescheme of $X$ having $S$ as underlying space. If one remarks that
the irreducible components of $\operatorname{Spec}(\mathcal{O}_{S,x})$ are the intersections of
$\operatorname{Spec}(\mathcal{O}_{X,x})$ with the irreducible components of $S$ containing $x$, and correspond
bijectively with the latter, one sees that

$$ \dim(\mathcal{F}_{x}) = \dim(\mathcal{O}_{S,x}) (5.1.12.1) $$

by virtue of `(5.1.1.1)`; it also follows from `(5.1.2)` that one has

$$ \dim(\mathcal{F}_{x}) = codim(\overline{x}, S) (5.1.12.2) $$

if $X$ is locally Noetherian.

One says that $\mathcal{F}$ is **equidimensional at the point $x \in X$** if $\mathcal{F}_{x}$ is an equidimensional
$\mathcal{O}_{X,x}$-module, that is to say `(0, 16.1.7)` if $Supp(\mathcal{F}_{x})$ is equidimensional as a closed part
of $\operatorname{Spec}(\mathcal{O}_{X,x})$; this amounts to saying that the ring $\mathcal{O}_{S,x}$ is
equidimensional.

One calls **dimension of $\mathcal{F}$** and denotes by $\dim(\mathcal{F})$ the dimension of the support
$Supp(\mathcal{F})$; it follows from `(5.1.4)` and `(5.1.12.1)` that one has

```text
  dim(ℱ) = sup_{x ∈ X} dim(ℱ_x).                         (5.1.12.3)
```

If $X = \operatorname{Spec}(A)$ is an affine scheme and if $\mathcal{F} = \tilde{M}$, where $M$ is an $A$-module of
finite type, one has $\dim(\mathcal{F}) = \dim(M)$ by virtue of `(0, 16.1.7)` and `(5.1.4)`.

**Proposition (5.1.13).**

<!-- label: IV.5.1.13 -->

*Let $X$ be a prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module of finite type, $x$ a point of $X$,
$x'$ a generization of $x$ in $X$; one then has*

$$ \dim(\mathcal{F}_{x'}) \leq \dim(\mathcal{F}_{x}). (5.1.13.1) $$

This follows at once from `(5.1.12.1)` and the definitions.

<!-- original page 90 -->

### 5.2. Dimension of an algebraic prescheme

**Proposition (5.2.1).**

<!-- label: IV.5.2.1 -->

*Let $k$ be a field, $X$ an irreducible prescheme locally of finite type over $k$, $\xi$ its generic point. Then $X$ is
biequidimensional and one has $\dim(X) = deg.tr_{k} k(\xi)$.*

Every local ring $\mathcal{O}_{x}$ is the local ring of a $k$-algebra of finite type, hence a quotient of a regular
local ring `(0, 17.3.9)`, and one knows `(0, 16.5.12)` that such rings are catenary; consequently $X$ is a catenary
space `(5.1.5)`, and as $X$ is irreducible, it suffices `(5.1.1)` to show that for every closed point $x \in X$, one has

$$ \dim(\mathcal{O}_{x}) = deg.tr_{k} k(x). (5.2.1.1) $$

One may evidently suppose $X$ reduced and affine, hence integral with ring $A$, an algebra of finite type over $k$. Let
$n = deg.tr_{k} k(\xi)$, with $k(\xi) = K$ the field of fractions of $A$. One knows (Bourbaki, *Alg. comm.*, chap. V,
§3, n° 1, th. 1) that there exists a sub-$k$-algebra $B = k[t_{1}, \cdots, t_{n}]$ of $A$, where the $t_{i}$ are
algebraically independent over $k$, such that $A$ be a *finite* $B$-algebra. Let $\mathfrak{m} = j_{x}$, which by
hypothesis is a maximal ideal of $A$; $\mathfrak{n} = B \cap \mathfrak{m}$ is therefore a maximal ideal of $B$
(Bourbaki, *Alg. comm.*, chap. V, §2, n° 1, prop. 1), and $A_{\mathfrak{m}}$ is a local ring of the finite
$B_{\mathfrak{n}}$-algebra $S^{-1}A$, where $S = B - \mathfrak{n}$; as $B_{\mathfrak{n}}$ is integrally closed and
$S^{-1}A$ integral, one has $\dim(A_{\mathfrak{m}}) = \dim(B_{\mathfrak{n}})$ `(0, 16.1.6)`. One may therefore restrict
to the case where $A = k[t_{1}, \cdots, t_{n}]$; one knows then that $k' = k(x)$ is a finite extension of $k$
`(I, 6.4.2)`; let $A' = k'[t_{1}, \cdots, t_{n}]$; taking into account `(I, 2.4.6 and 3.3.14)`, there exists a maximal
ideal $\mathfrak{m}'$ of $A'$ above $\mathfrak{m}$ and such that $k'$ be the residue field of $A'_{\mathfrak{m}'}$.
Since $A'$ is integral and is a finite $A$-algebra, the same reasoning as above shows that $\dim(A'_{\mathfrak{m}'}) =
\dim(A_{\mathfrak{m}})$, so that one is reduced to the case where $A/\mathfrak{m} = k$. Now in this case $\mathfrak{m}$
is generated by polynomials $t_{i} - a_{i}$ (where $a_{i} \in k$, $1 \leq i \leq n$, the $a_{i}$ being the canonical
images of the $t_{i}$ in $A/\mathfrak{m}$). Replacing $t_{i}$ by $t_{i} - a_{i}$, one sees finally that one is reduced
to the case where $\mathfrak{m} = \sum^{n}_{i=1} A t_{i}$. The completion of the local ring $A_{\mathfrak{m}}$ is then
the formal series ring $k[[t_{1}, \cdots, t_{n}]]$; one knows that it has the same dimension as $A_{\mathfrak{m}}$
`(0, 16.2.4)`, and on the other hand, the dimension of $k[[t_{1}, \cdots, t_{n}]]$ is equal to $n$ `(0, 17.1.4)`; whence
the conclusion.

**Corollary (5.2.2).**

<!-- label: IV.5.2.2 -->

*For a prescheme $X$ locally of finite type over a field $k$, $\dim(X)$ coincides with the number defined in `(4.1.1)`.*

Indeed, if $X_{\alpha}$ are the reduced sub-preschemes having as underlying spaces the irreducible components of $X$,
one has `dim(X) = sup_α (dim(X_α))` `(0, 14.1.2.1)` and it suffices to apply `(5.2.1)` to the $X_{\alpha}$.

**Corollary (5.2.3).**

<!-- label: IV.5.2.3 -->

*Let $X$ be a prescheme locally of finite type over a field $k$, $x$ a point of $X$. One has*

```text
  dim_x(X) = dim(𝒪_x) + deg.tr_k k(x).                   (5.2.3.1)
```

One knows that there exists an open neighbourhood $U$ of $x$ in $X$ such that $\dim_{x}(X) = \dim(U)$ `(0, 14.1.4.1)`,
and one may suppose that the irreducible components of $U$ are the $X_{i} \cap U$, where the $X_{i}$ are the irreducible
components of $X$ containing $x$; as $U \cap X_{i}$

<!-- original page 91 -->

is dense in $X_{i}$, it follows from `(4.1.1.3)` that $\dim(X_{i}) = \dim(U \cap X_{i})$, so one has
`dim_x(X) = sup_i (dim(X_i))`. Moreover, the minimal prime ideals of $\mathcal{O}_{x}$ correspond to the generic points
of the $X_{i}$, hence `(0, 16.1.1.1)`, one has `dim(𝒪_{X,x}) = sup_i (dim(𝒪_{X_i, x}))`. One is thus reduced to the case
where $X$ is irreducible; as $X$ is biequidimensional by `(5.2.1)`, one has `dim(X) = dim(‾{x}) + codim(‾{x}, X)`
`(0, 14.3.5.1)`, and one knows that $\dim(\overline{x}) = deg.tr_{k} k(x)$ by `(5.2.1)` and $codim(\overline{x}, X) =
\dim(\mathcal{O}_{x})$ by `(5.1.2)`.

**Corollary (5.2.4).**

<!-- label: IV.5.2.4 -->

*Let $X$ be a prescheme locally of finite type over a field $k$, $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-Module,
$f$ a section of $\mathcal{L}$ over $X$, such that the set $Y$ of $x \in X$ for which $f(x) = 0$ is rare in $X$. Then
one has $\dim(Y) \leq \dim(X) - 1$; the two sides of this inequality are equal if $Y$ meets every irreducible component
of maximum dimension of $X$.*

If $(X_{\alpha})$ is the family of irreducible components of $X$, one has

```text
  dim(Y) = sup_α (dim(Y ∩ X_α))
```

and one is therefore reduced to the case where $X$ is irreducible ($Y \cap X_{\alpha}$ being rare in $X_{\alpha}$ since
each $X_{\alpha}$ has a non-empty interior in $X$). One may restrict to the case where $Y \neq \emptyset$; then, for
every maximal point $x$ of $Y$, one has (since $X$ is biequidimensional) `dim(‾{x}) = dim(X) − codim(‾{x}, X)`, and
since $Y$ is rare in $X$, one has

$$ codim(\overline{x}, X) = 1 $$

by `(5.1.8)`; whence the corollary.

**Remarks (5.2.5).**

<!-- label: IV.5.2.5 -->

*(i) Contrary to what happens for algebraic $k$-preschemes, a locally Noetherian prescheme $X$ is not necessarily
catenary (cf. `(5.6.11)`); it is, however, if all its local rings $\mathcal{O}_{x}$ are quotients of regular rings
`(0, 16.5.12)` and in particular if $X$ is regular `(I, 4.1.4)`. Nevertheless, even an (integral) scheme
$X = \operatorname{Spec}(A)$, where $A$ is a *regular* ring, is not necessarily *biequidimensional*; in other words
`(0, 14.3.3)` the codimensions in $X$ of the various closed points of $X$ are not necessarily the same. For example, let
$B$ be a discrete valuation ring, $\mathfrak{m} = B\pi$ its maximal ideal, $k = B/\mathfrak{m}$ its residue field, $K$
the field of fractions of $B$; let $A$ be the polynomial ring `B[T]`. In $A$ there are maximal ideals of height `2`, for
example $(\pi) + (T)$; but there are also maximal ideals of height `1`, for example the principal ideal $(\pi T - 1)$:
indeed, a principal prime ideal $\neq 0$ is of height `1` `(5.1.8)`; on the other hand $A/(\pi T - 1)$ is isomorphic to
the ring of fractions $B_{\pi}$ $(0_{I}, 1.2.3)$, which is none other than $K$ here, which proves that the ideal
$(\pi T - 1)$ is maximal and of height `1`.*

*(ii) When $X$ is a prescheme locally of finite type over a field, one has seen `(4.1.1.3)` that $\dim(U) = \dim(X)$ for
every dense open $U$ in $X$. This result does not extend to regular Noetherian preschemes, even if they are
biequidimensional. For example, let $B$ be a discrete valuation ring, $\mathfrak{m}$ its maximal ideal; $X =
\operatorname{Spec}(A)$ has two points, the ideal `(0)` and $\mathfrak{m}$, the latter being the only closed point; one
has $\dim(X) = 1$, but the open set $U = {(0)}$ is of dimension `0` (cf. §10).*

<!-- original page 92 -->

### 5.3. Dimension of the support of a Module and Hilbert polynomial

This number uses the results of Chapter III; it will not be used in the sequel of this chapter.

**Proposition (5.3.1).**

<!-- label: IV.5.3.1 -->

*Let $A$ be an Artinian local ring, $X$ a projective scheme over $\operatorname{Spec}(A)$, $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-Module very ample relative to $A$, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module $\neq 0$; set
$\mathcal{F}(n) = \mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{L}^{\otimes n}$ for $n \in \mathbb{Z}$. Then the degree
of the Hilbert polynomial $P(n) = \chi_{A}(\mathcal{F}(n))$ of $\mathcal{F}$ relative to $A$ `(III, 2.5.3)` is equal to
the dimension of $Supp(\mathcal{F})$.*

We reason by induction on $d = \dim(Supp(\mathcal{F}))$. One knows that there exists a closed sub-prescheme $Y$ of $X$
whose $Supp(\mathcal{F})$ is the underlying space, and an $\mathcal{O}_{Y}$-Module coherent $\mathcal{G}$ such that
$\mathcal{F} = j_{*}(\mathcal{G})$, where $j : Y \to X$ is the canonical injection $(Err_{III}, 30)$. It is immediate
that the Hilbert polynomials of $\mathcal{F}$ and of $\mathcal{G}$ are the same, so one may restrict to the case where
$X = Supp(\mathcal{F})$. Suppose first $d = 0$; all the points of $X$ being closed, $X$ is an Artinian scheme
`(I, 6.2.2)`, hence $\mathcal{F}(n) = \mathcal{F}$ for every integer $n$, and one has consequently `(III, 2.5.3)`

$$ \chi_{A}(\mathcal{F}(n)) = long_{A}(\Gamma(X, \mathcal{F})) $$

for $n$ large enough, and the degree of the Hilbert polynomial is therefore `0`. Suppose now $d > 0$, and set $Z =
Ass(\mathcal{F})$, which is a finite set `(3.1.6)`; there exist an integer $m > 0$ and a section $f \in \Gamma(X,
\mathcal{L}^{\otimes m})$ such that $X_{f}$ be a neighbourhood of $Z$ `(II, 4.5.4)`. Multiplication by $f$ is a
homomorphism

$$ \mu_{f} : \mathcal{F} \to \mathcal{F}(m) $$

which is injective `(3.1.8)`; one therefore has an exact sequence

```text
  0 → ℱ ─μ_f→ ℱ(m) → 𝒢 → 0                              (5.3.1.1)
```

where $\mathcal{G}$ is coherent. By virtue of Nakayama's lemma, the points $x \in Supp(\mathcal{G})$ are exactly those
for which $f(x) = 0$. We shall deduce from this that one has

$$ \dim(Supp(\mathcal{G})) = d - 1. (5.3.1.2) $$

This will follow from the following lemma:

**Lemma (5.3.1.3).**

<!-- label: IV.5.3.1.3 -->

*Let $A$ be an Artinian local ring, $X$ a projective scheme over $\operatorname{Spec}(A)$, $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-Module ample relative to $A$; then, for every section $g$ of $\mathcal{L}$ over $X$, the set $X_{g}$
of $x \in X$ such that $g(x) = 0$ meets every irreducible component of $X$ of dimension $\neq 0$.*

Indeed `(II, 5.5.7)`, the set $X_{g}$ is an affine open of $X$, and if it contains an irreducible component $X'$ of $X$,
the reduced closed sub-prescheme of $X$ having $X'$ as underlying space is at once projective and affine over $A$, hence
finite over $A$ `(III, 4.4.2)`, and consequently an Artinian scheme, hence of dimension `0`.

This lemma being established, note that since $Z$ contains the maximal points of $X$, $X_{f}$ is dense, hence
$Supp(\mathcal{G})$ is rare in $X$, and the relation `(5.3.1.2)` follows from the lemma and from `(5.2.4)`.

<!-- original page 93 -->

This being so, from the exact sequence `(5.3.1.1)` one deduces, for every $n$, the exact sequence

```text
  0 → ℱ(n) → ℱ(n + m) → 𝒢(n) → 0
```

and for $n$ large enough, one therefore also has the exact sequence `(III, 2.2.3)`

```text
  0 → Γ(X, ℱ(n)) → Γ(X, ℱ(n + m)) → Γ(X, 𝒢(n)) → 0
```

whence, taking `(III, 2.5.3)` into account, for $n$ large enough,

```text
  χ_A(𝒢(n)) = χ_A(ℱ(n + m)) − χ_A(ℱ(n)).
```

As, by virtue of `(5.3.1.2)` and the induction hypothesis, the degree of the polynomial $\chi_{A}(\mathcal{G}(n))$ is
$d - 1$, the preceding relation entails that the degree of $\chi_{A}(\mathcal{F}(n))$ is $d$. Q.E.D.

### 5.4. Dimension of the image of a morphism

**Proposition (5.4.1).**

<!-- label: IV.5.4.1 -->

*Let $X$, $Y$ be two locally Noetherian preschemes, $f : X \to Y$ a morphism.*

*(i) If $f$ is quasi-finite, one has `dim(X) ≤ dim(‾{f(X)}) ≤ dim(Y)`.*

*(ii) If $f$ is surjective and open (resp. surjective and closed), one has $\dim(X) \geq \dim(Y)$.*

(i) One can replace $f$ by $f_{red}$ `(II, 6.2.4)`, hence suppose $X$ and $Y$ reduced; if $Z$ is the reduced closed
sub-prescheme of $Y$ having as underlying space $\overline{f(X)}$, one has then $f = j \circ g$, where $j : Z \to Y$ is
the canonical injection and $g : X \to Z$ is a quasi-finite morphism `(I, 5.2.2 and II, 6.2.4)`. One may therefore
restrict to the case where $f(X)$ is dense in $Y$. For every $x \in X$, $\mathcal{O}_{x}$ is then a quasi-finite
$\mathcal{O}_{f(x)}$-module `(II, 6.2.2)`, and consequently $\mathfrak{m}_{f(x)} \mathcal{O}_{x}$ is an ideal of
definition of $\mathcal{O}_{x}$ $(0_{I}, 7.4.4)$; but one knows `(0, 16.3.10)` that if $A \to B$ is a local homomorphism
of Noetherian local rings such that, if $\mathfrak{m}$ is the maximal ideal of $A$, $\mathfrak{m} B$ is an ideal of
definition of $B$, then one has $\dim(B) \leq \dim(A)$; this completes the proof of (i) by virtue of `(5.1.4)`.

(ii) The definition of dimension `(0, 14.1.2)` shows that it suffices to prove that for every sequence $(y_{i})_{0 \leq
i \leq n}$ of distinct elements of $Y$ such that $y_{i} \in \overline{y_{i+1}}$ for $0 \leq i \leq n - 1$, there exists
a sequence $(x_{i})_{0 \leq i \leq n}$ of points of $X$ such that $x_{i} \in \overline{x_{i+1}}$ for $0 \leq i \leq n -
1$ and $f(x_{i}) = y_{i}$ for every $i$. Suppose first $f$ surjective and open and let us prove the existence of the
$x_{i}$ by induction on $i$; the existence of $x_{0} \in X$ such that $f(x_{0}) = y_{0}$ follows from the fact that $f$
is surjective. If the $x_{i}$ have been determined for $i \leq m$ so as to satisfy $f(x_{i}) = y_{i}$ for $i \leq m$ and
$x_{i} \in \overline{x_{i+1}}$ for $i < m$, one notes that since $f$ is open and $y_{m+1}$ a generization of $y_{m}$,
there exists $x_{m+1} \in f^{-1}(y_{m+1})$ which is a generization of $x_{m}$ `(1.10.3)` and the induction can proceed.

Suppose now $f$ surjective and closed and let us prove the existence of the $x_{i}$ by descending induction on $i$, the
existence of $x_{n}$ such that $f(x_{n}) = y_{n}$ still resulting from the fact that $f$ is surjective. If the $x_{i}$
have been determined so as to satisfy the desired conditions for $i > m$, one notes that $f(\overline{x_{m+1}})$ is the
closure of ${f(x_{m+1})} = {y_{m+1}}$ since $f$

<!-- original page 94 -->

is closed (Bourbaki, *Top. gén.*, chap. I, 3rd ed., §5, n° 4, prop. 9); there therefore exists $x_{m} \in
\overline{x_{m+1}}$ such that $f(x_{m}) = y_{m}$ and the descending induction can continue.

**Corollary (5.4.2).**

<!-- label: IV.5.4.2 -->

*If $X$, $Y$ are two locally Noetherian preschemes, $f : X \to Y$ a finite morphism (hence closed), one has $\dim(X) =
\dim(\overline{f(X)})$. If moreover $f$ is surjective, one has $\dim(X) = \dim(Y)$.*

**Remarks (5.4.3).**

<!-- label: IV.5.4.3 -->

*(i) One has seen in `(4.1.2)` that if $X$ and $Y$ are preschemes locally of finite type over a field $k$ and $f$ a
$k$-morphism, the inequality $\dim(Y) \leq \dim(X)$ is already verified when $f$ is quasi-compact and dominant. On the
contrary, one can have $\dim(Y) > \dim(X)$ even when $f$ is of finite type, bijective, and a local immersion, if one
only supposes $X$ and $Y$ locally Noetherian. For example, let $A$ be a discrete valuation ring, $K$ its field of
fractions, $k$ its residue field; if $Y = \operatorname{Spec}(A)$, and if $a$ is the generic point of $Y$ and $b$ its
closed point, one has therefore $k(a) = K$, $k(b) = k$. Let then $X$ be the sum prescheme of $\operatorname{Spec}(K)$
and $\operatorname{Spec}(k)$, $f : X \to Y$ the morphism which coincides on $\operatorname{Spec}(K)$ and
$\operatorname{Spec}(k)$ with the respective canonical morphisms `(I, 2.4.5)`; it is clear that $f$ is a bijective local
immersion, ${a}$ being open in $Y$; on the other hand $f$ is of finite type, for $K = A[\pi^{-1}]$, where $\pi$ is a
uniformizer of $A$, so $K$ is an $A$-algebra of finite type. However one has $\dim(X) = 0$ and $\dim(Y) = 1$.*

*(ii) If $A$ and $B$ are two Noetherian rings such that $A \subset B$ and that $B$ is a finite $A$-algebra, the
corollary `(5.4.2)` shows again that $\dim(B) = \dim(A)$ `(0, 16.1.5)`. Suppose moreover that $A$ is a Noetherian local
ring; then $B$ is a Noetherian semi-local ring (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9); if
$\mathfrak{n}_{i}$ ($1 \leq i \leq r$) are the maximal ideals of $B$, one has therefore*

```text
  dim(A) = sup_i dim(B_{𝔫_i}).                           (5.4.3.1)
```

*One will observe that, under these conditions, one does not necessarily have $\dim(B_{\mathfrak{n}_{i}}) = \dim(A)$ for
every $i$: it suffices to see this to replace $B$ by the direct product of $B$ and the residue field $k$ of $A$. But one
even has examples where $A$ and $B$ are in addition *integral rings of dimension `2`* and where certain of the
$B_{\mathfrak{n}_{i}}$ have dimension $< \dim(A)$ `(5.6.11)`. We shall, however, see further on `((5.6.4)` and
`(5.6.10))` that this last phenomenon cannot present itself when one supposes that $A$ is a quotient of a regular local
ring.*

### 5.5. Dimension formula for a morphism of finite type

**(5.5.1)**

<!-- label: IV.5.5.1 -->

Recall `(0, 16.3.9)` that if $A$, $B$ are two Noetherian local rings, $k$ the residue field of $A$, $\phi : A \to B$ a
local homomorphism, one has

```text
  dim(B) ≤ dim(A) + dim(B ⊗_A k).                        (5.5.1.1)
```

One deduces:

**Proposition (5.5.2).**

<!-- label: IV.5.5.2 -->

*Let $X$, $Y$ be two locally Noetherian preschemes, $f : X \to Y$ a morphism, $x$ a point of $X$, $y = f(x)$. Then one
has*

```text
  dim(𝒪_x) ≤ dim(𝒪_y) + dim(𝒪_x ⊗_{𝒪_y} k(y)).           (5.5.2.1)
```

<!-- original page 95 -->

In particular, if $x$ is a maximal point of the fibre $f^{-1}(y)$, one has

$$ \dim(\mathcal{O}_{x}) \leq \dim(\mathcal{O}_{y}) (5.5.2.2) $$

since $\mathcal{O}_{x} \otimes_{\mathcal{O}_{y}} k(y) = \mathcal{O}_{x} / \mathfrak{m}_{y} \mathcal{O}_{x}$ is the local
ring of $x$ in the prescheme $f^{-1}(y)$, and is therefore of dimension `0` by hypothesis.

We shall obtain a more precise formula than `(5.5.2.1)` when one supposes that $f$ is a morphism of finite type.

**Proposition (5.5.3).**

<!-- label: IV.5.5.3 -->

*Let $A$ be a Noetherian ring, $T$ an indeterminate, $\mathfrak{p}$ a prime ideal of $A$; then $\mathfrak{p}' =
\mathfrak{p} A[T]$ is prime in $B = A[T]$ and $\mathfrak{p}' \cap A = \mathfrak{p}$. There exists an infinity of prime
ideals of $B$ distinct from $\mathfrak{p}'$ whose intersection with $A$ is $\mathfrak{p}$; these ideals are pairwise
without inclusion relation. Moreover, if $\mathfrak{q}$ is such an ideal, one has*

```text
  dim(B_𝔮) = dim(B_{𝔭'}) + 1 = dim(A_𝔭) + 1.             (5.5.3.1)
```

In the first assertions, one reduces at once, by replacing $A$ by $A/\mathfrak{p}$ and observing that
$A[T]/\mathfrak{p} A[T] = (A/\mathfrak{p})[T]$, to the case $\mathfrak{p} = 0$; they then follow from the fact that the
prime ideals of $B = A[T]$ whose intersection with $A$ reduces to `0` are exactly those which do not meet the
multiplicative part $S = A - {0}$ of the integral ring $A$; now one knows that there is an increasing bijection of the
set of these ideals onto the set of prime ideals of $S^{-1}A[T] = K[T]$, where $K$ is the field of fractions of $A$
(Bourbaki, *Alg. comm.*, chap. II, §2, n° 5, prop. 11). Moreover, one has, according to `(5.5.1.2)`,
`dim(B_𝔮) ≤ dim(A_𝔭) + dim(B_𝔮/𝔭 B_𝔮)`, and if $k$ is the field of fractions of $A/\mathfrak{p}$,
$B_{\mathfrak{q}}/\mathfrak{p} B_{\mathfrak{q}}$ is canonically identified with $(k[T])_{\mathfrak{q}}$, hence is a
discrete valuation ring, so of dimension `1`. Finally, if
$\mathfrak{p} = \mathfrak{p}_{0} \supset \mathfrak{p}_{1} \supset \cdots \supset \mathfrak{p}_{m}$ is a chain of prime
ideals of $A$ of maximum length, the ideals $\mathfrak{p}_{j} B$ ($0 \leq j \leq m$) are prime in $B$, pairwise
distinct, and contained in $\mathfrak{q}$; hence $\dim(B_{\mathfrak{q}}) \geq m + 1 = \dim(A_{\mathfrak{p}}) + 1$ and
consequently $\dim(B_{\mathfrak{q}}) = \dim(A_{\mathfrak{p}}) + 1$. This relation can also be written
$ht(\mathfrak{q}) = ht(\mathfrak{p}) + 1$; as $\mathfrak{q} \neq \mathfrak{p}'$, one has moreover
$ht(\mathfrak{q}) \geq ht(\mathfrak{p}') + 1 \geq ht(\mathfrak{p}) + 1$ by definition of the height of a prime ideal;
this completes the proof of `(5.5.3.1)`.

**Corollary (5.5.4).**

<!-- label: IV.5.5.4 -->

*For every Noetherian ring $A$, one has*

```text
  dim(A[T_1, …, T_r]) = dim(A) + r                       (5.5.4.1)
```

*($T_{i}$ indeterminates).*

One will note, on the other hand, that there are examples of non-Noetherian local rings $A$ such that $\dim(A) = 1$ and
$\dim(A[T]) = 3$ `[30]`.

**Corollary (5.5.5).**

<!-- label: IV.5.5.5 -->

*For every locally Noetherian prescheme $X$, the dimension of $X[T_{1}, \cdots, T_{r}] = X \otimes_{\mathbb{Z}}
\mathbb{Z}[T_{1}, \cdots, T_{r}]$ ($T_{i}$ indeterminates) is $\dim(X) + r$.*

This follows from `(5.5.4)` and `(0, 14.1.7)`.

**Corollary (5.5.6).**

<!-- label: IV.5.5.6 -->

*Under the hypotheses of `(5.5.3)`, let $\mathfrak{q}$ be a prime ideal of $B = A[T]$ such that $\mathfrak{q} \cap A =
\mathfrak{p}$; if $k$ and $k'$ are the residue fields of $A_{\mathfrak{p}}$ and $B_{\mathfrak{q}}$ respectively, one
has*

```text
  dim(A_𝔭) + 1 = dim(B_𝔮) + deg.tr_k k'.                 (5.5.6.1)
```

<!-- original page 96 -->

If $\mathfrak{q} = \mathfrak{p} B$, one has, according to `(5.5.3.1)`, $\dim(B_{\mathfrak{q}}) =
\dim(A_{\mathfrak{p}})$, and in this case $k' = k(T)$, hence the formula `(5.5.6.1)` is indeed verified. In the contrary
case, $\dim(B_{\mathfrak{q}}) = \dim(A_{\mathfrak{p}}) + 1$, and as $\mathfrak{q}$ corresponds to a prime ideal
$\mathfrak{q}' \neq 0$ of `k[T]`, $k'$ is an algebraic extension of $k$, so one still has the formula `(5.5.6.1)`.

**Lemma (5.5.7).**

<!-- label: IV.5.5.7 -->

*Let $A$ be an integral Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $k$ its residue field.*

*(i) For every integral ring $B$ containing $A$, such that $B = A[x]$ (for some $x \in B$) and every prime ideal
$\mathfrak{q}$ of $B$ such that $\mathfrak{q} \cap A = \mathfrak{m}$, one has*

```text
  dim(A) + deg.tr_A B ≥ dim(B_𝔮) + deg.tr_k k'           (5.5.7.1)
```

*denoting by $k'$ the residue field of $B_{\mathfrak{q}}$ and by $deg.tr_{A} B$ the transcendence degree of the field of
fractions of $B$ over that of $A$.*

*(ii) Suppose that for every maximal ideal $\mathfrak{n}$ of `A[T]` such that $\mathfrak{n} \cap A = \mathfrak{m}$, the
ring $(A[T])_{\mathfrak{n}}$ is catenary; then the two sides of `(5.5.7.1)` are equal.*

(i) If $x$ is transcendent over the field of fractions of $A$, one has $deg.tr_{A} B = 1$ and the two sides of `(5.5.7)`
are equal by virtue of `(5.5.6)`. In the contrary case, one has $B = A[T]/\mathfrak{p}$, where $\mathfrak{p}$ is a prime
ideal $\neq 0$ of `A[T]`, such that $\mathfrak{p} \cap A = 0$ since $B$ contains $A$; one therefore has
$ht(\mathfrak{p}) = 1$ by virtue of `(5.5.3)`. The ideal $\mathfrak{q}$ of $B$ is of the form
$\mathfrak{n}/\mathfrak{p}$, where $\mathfrak{n} \supset \mathfrak{p}$ is a prime ideal of `A[T]` such that
$\mathfrak{n} \cap A = \mathfrak{m}$, and one has $B_{\mathfrak{q}} = (A[T])_{\mathfrak{n}} / \mathfrak{p}
(A[T])_{\mathfrak{n}}$; the formula `(0, 16.1.4.1)`, applied to $X = \operatorname{Spec}((A[T])_{\mathfrak{n}})$ and to
$Y = \operatorname{Spec}(B_{\mathfrak{q}})$, gives

```text
  dim((A[T])_𝔫) ≥ ht(𝔭 (A[T])_𝔫) + dim(B_𝔮) = 1 + dim(B_𝔮)     (5.5.7.2)
```

since $ht(\mathfrak{p} (A[T])_{\mathfrak{n}}) = ht(\mathfrak{p}) = 1$ by virtue of the bijective correspondence between
prime ideals of `A[T]` contained in $\mathfrak{n}$ and prime ideals of $(A[T])_{\mathfrak{n}}$. Finally, the formula
`(5.5.6.1)` gives

```text
  dim((A[T])_𝔫) = dim(A) + 1 − deg.tr_k k'               (5.5.7.3)
```

since the residue fields of $B_{\mathfrak{q}}$ and of $(A[T])_{\mathfrak{n}}$ are the same; on the other hand, one has
then $deg.tr_{A} B = 0$, which completes the proof of `(5.5.7.1)`.

(ii) If $(A[T])_{\mathfrak{n}}$ is catenary, the two sides of `(5.5.7.2)` are equal `(0, 16.1.4)`, hence also the two
sides of `(5.5.7.1)`.

**Theorem (5.5.8) (dimension formula).**

<!-- label: IV.5.5.8 -->

*Let $A$ be an integral Noetherian local ring, $B$ an integral ring containing $A$ which is an $A$-algebra of finite
type, $\mathfrak{q}$ a prime ideal of $B$ such that $\mathfrak{q} \cap A$ is the maximal ideal $\mathfrak{m}$ of $A$,
$k$ and $k'$ the residue fields of $A$ and $B_{\mathfrak{q}}$ respectively. One then has the inequality*

```text
  dim(A) + deg.tr_A B ≥ dim(B_𝔮) + deg.tr_k k'.          (5.5.8.1)
```

*Moreover the two sides are equal if, for every sub-$A$-algebra $A'$ of finite type of `B[T]` and every maximal ideal
$\mathfrak{m}'$ of $A'$ such that $\mathfrak{m}' \cap A = \mathfrak{m}$, $A'_{\mathfrak{m}'}$ is catenary.*

Let $B = A[x_{1}, \cdots, x_{n}]$ and let us reason by induction on $n$. Set $C = A[x_{1}, \cdots, x_{n-1}]$ and
$\mathfrak{r} = \mathfrak{q} \cap C$; $C_{\mathfrak{r}}$ is an integral Noetherian local ring, and if one sets $S = C -
\mathfrak{r}$, $B' = S^{-1} B$, $\mathfrak{q}' = S^{-1} \mathfrak{q}$, one has $B_{\mathfrak{q}} = B'_{\mathfrak{q}'}$,
$B' = C_{\mathfrak{r}}[x_{n}]$ and $\mathfrak{q}' \cap C_{\mathfrak{r}} = \mathfrak{r} C_{\mathfrak{r}}$; in addition
the fields of fractions

<!-- original page 97 -->

of $B'$ and $C_{\mathfrak{r}}$ are those of $B$ and $C$ respectively. If $k_{1}$ is the residue field of
$C_{\mathfrak{r}}$, one has therefore, according to `(5.5.7.1)`,

```text
  dim(C_𝔯) + deg.tr_C B ≥ dim(B_𝔮) + deg.tr_{k_1} k'.    (5.5.8.2)
```

On the other hand, the induction hypothesis gives

```text
  dim(A) + deg.tr_A C ≥ dim(C_𝔯) + deg.tr_k k_1          (5.5.8.3)
```

whence `(5.5.8.1)` by adding `(5.5.8.2)` and `(5.5.8.3)` term by term. To prove the second assertion, note first that
every sub-$A$-algebra of finite type of `C[T]` is also a sub-$A$-algebra of finite type of `B[T]`; by induction on $n$,
one may therefore suppose that the two sides of `(5.5.8.3)` are equal. On the other hand, to see that the two sides of
`(5.5.8.2)` are equal, it suffices, by virtue of `(5.5.7)`, to verify that if $\mathfrak{n}$ is a maximal ideal of
$C_{\mathfrak{r}}[T]$ such that $\mathfrak{n} \cap C_{\mathfrak{r}} = \mathfrak{r} C_{\mathfrak{r}}$, then
$(C_{\mathfrak{r}}[T])_{\mathfrak{n}}$ is catenary; but one has $C_{\mathfrak{r}}[T] = S'^{-1} C[T]$ where $S' = C -
\mathfrak{r}$; the ideal $\mathfrak{n}$ is therefore of the form $S'^{-1} \mathfrak{n}'$, where $\mathfrak{n}'$ is a
prime ideal of `C[T]` such that $\mathfrak{n}' \cap C = \mathfrak{r}$, whence $(C_{\mathfrak{r}}[T])_{\mathfrak{n}} =
(C[T])_{\mathfrak{n}'}$; if $\mathfrak{m}'$ is a maximal ideal of `C[T]` containing $\mathfrak{n}'$,
$(C[T])_{\mathfrak{n}'}$ is therefore a local ring of the ring $(C[T])_{\mathfrak{m}'}$, and as by hypothesis this
latter is catenary, so is $(C[T])_{\mathfrak{n}'}$ `(0, 16.1.4)`.

### 5.6. Dimension formula and universally catenary rings

**Proposition (5.6.1).**

<!-- label: IV.5.6.1 -->

*Let $A$ be a Noetherian ring. The following properties are equivalent:*

*a) Every polynomial ring $A[T_{1}, \cdots, T_{n}]$ is catenary.*

*b) Every algebra of finite type over $A$ is catenary.*

*c) $A$ is catenary, and for every integral local $A$-algebra essentially of finite type `(1.3.8)` $B'$, one has,
denoting by $\mathfrak{p}$ the inverse image in $A$ of the maximal ideal $\mathfrak{q}$ of $B'$, by $A'$ the image of
$A_{\mathfrak{p}}$ in $B'$, by $k$ and $k'$ the residue fields of $A'$ and $B'$ respectively,*

```text
  dim(A') + deg.tr_{A'}(B') = dim(B') + deg.tr_k k'.     (5.6.1.1)
```

The fact that b) entails c) follows from `(5.5.8)`; indeed, $B'$ is a local $A'$-algebra essentially of finite type
`(1.3.10)`, hence of the form $B''_{\mathfrak{q}''}$, where `B''` is a sub-$A'$-algebra of finite type of $B'$,
$\mathfrak{q}''$ a prime ideal of `B''` above the maximal ideal $\mathfrak{p}'$ of $A'$; moreover the fields of
fractions of $B'$ and `B''` are the same, hence $deg.tr_{A'}(B') = deg.tr_{A'}(B'')$. To prove `(5.6.1.1)`, it suffices
to show that (under hypothesis b)) every sub-$A'$-algebra `A_1` of finite type of `B'[T]` is catenary; indeed the two
sides of `(5.5.8.1)`, where one replaces $A$, $B$, and $\mathfrak{q}$ by $A'$, `B''`, and $\mathfrak{q}''$, will then be
equal, whence the equality `(5.6.1.1)`. Now the hypothesis b) entails that every $A$-algebra essentially of finite type
is catenary `(0, 16.1.4)`, and `A_1` is such an $A$-algebra `(1.3.9)`.

It is trivial that b) entails a); conversely, a) entails b), every $A$-algebra of finite type being a quotient of a
polynomial algebra `(0, 16.1.4)`.

It remains to prove that c) entails b). Since every quotient by a prime ideal

<!-- original page 98 -->

of an $A$-algebra of finite type is an integral $A$-algebra of finite type, it amounts to seeing that, if $B$ is an
integral $A$-algebra of finite type, $\mathfrak{q}$ and $\mathfrak{q}'$ two prime ideals of $B$ such that $\mathfrak{q}'
\subset \mathfrak{q}$, one has `(0, 16.1.4.2)`

```text
  dim(B_𝔮 / 𝔮' B_𝔮) + dim(B_{𝔮'}) = dim(B_𝔮).            (5.6.1.2)
```

Let $\mathfrak{p}$, $\mathfrak{p}'$ be the inverse images of $\mathfrak{q}$, $\mathfrak{q}'$ respectively in $A$,
$\mathfrak{n}$ the kernel of the homomorphism $A_{\mathfrak{p}} \to B_{\mathfrak{q}}$.

The image $A'$ of $A_{\mathfrak{p}}$ in $B_{\mathfrak{q}}$ being isomorphic to $A_{\mathfrak{p}}/\mathfrak{n}$, the
formula `(5.6.1.1)` applied to $A'$ and to $B' = B_{\mathfrak{q}}$ is written

```text
  dim(A_𝔭/𝔫) + deg.tr_{A'}(B_𝔮) = dim(B_𝔮) + deg.tr_{k(𝔭)} k(𝔮).  (5.6.1.3)
```

On the other hand, the kernel of $A_{\mathfrak{p}'} \to B_{\mathfrak{q}'}$ is $\mathfrak{n} A_{\mathfrak{p}'}$, hence,
applying the formula `(5.6.1.1)` where one replaces $A'$ by $A_{\mathfrak{p}'} / \mathfrak{n} A_{\mathfrak{p}'}$ and
$B'$ by $B_{\mathfrak{q}'}$, one has

```text
  dim(A_{𝔭'} / 𝔫 A_{𝔭'}) + deg.tr_{A_{𝔭'} / 𝔫 A_{𝔭'}} (B_{𝔮'})
        = dim(B_{𝔮'}) + deg.tr_{k(𝔭')} k(𝔮').            (5.6.1.4)
```

Finally, $B/\mathfrak{q}'$ is an integral $A$-algebra of finite type, the inverse image of $\mathfrak{q}/\mathfrak{q}'$
in $A$ is $\mathfrak{p}$, and the kernel of the homomorphism $A_{\mathfrak{p}} \to B_{\mathfrak{q}} / \mathfrak{q}'
B_{\mathfrak{q}}$ is $\mathfrak{p}' A_{\mathfrak{p}}$, hence, applying `(5.6.1.1)` where one replaces $A'$ by
$A_{\mathfrak{p}} / \mathfrak{p}' A_{\mathfrak{p}}$ and $B'$ by $B_{\mathfrak{q}} / \mathfrak{q}' B_{\mathfrak{q}}$, one
has

```text
  dim(A_𝔭/𝔭' A_𝔭) + deg.tr_{k(𝔭')}(B_𝔮 / 𝔮' B_𝔮)
        = dim(B_𝔮 / 𝔮' B_𝔮) + deg.tr_{k(𝔭)} k(𝔮).        (5.6.1.5)
```

Let us now add `(5.6.1.4)` and `(5.6.1.5)` term by term, and note that $k(\mathfrak{p}')$ (resp. $k(\mathfrak{q}')$) is
the field of fractions of $A_{\mathfrak{p}}/\mathfrak{p}' A_{\mathfrak{p}}$ (resp. $B_{\mathfrak{q}}/\mathfrak{q}'
B_{\mathfrak{q}}$); on the other hand $A_{\mathfrak{p}'} / \mathfrak{n} A_{\mathfrak{p}'}$ and
$A_{\mathfrak{p}}/\mathfrak{n}$ have the same field of fractions, and $B_{\mathfrak{q}'}$ and $B_{\mathfrak{q}}$ have
the same field of fractions; finally, since $A$ is supposed catenary, one has `(0, 16.1.4.2)`

```text
  dim(A_𝔭 / 𝔭' A_𝔭) + dim(A_{𝔭'} / 𝔫 A_{𝔭'}) = dim(A_𝔭/𝔫).
```

Taking these remarks and `(5.6.1.3)` into account, the relation `(5.6.1.2)` follows. Q.E.D.

**Definition (5.6.2).**

<!-- label: IV.5.6.2 -->

*One says that a Noetherian ring $A$ is **universally catenary** if it verifies the equivalent conditions a), b), c) of
`(5.6.1)`.*

**Remarks (5.6.3).**

<!-- label: IV.5.6.3 -->

*(i) If $A$ is universally catenary, so is $S^{-1}A$ for every multiplicative part $S$ of $A$, as follows at once from
`(5.6.1, a))` and from the fact that every ring of fractions of a catenary ring is catenary. Conversely, if, for every
prime ideal $\mathfrak{p}$ of $A$, the ring $A_{\mathfrak{p}}$ is universally catenary, then $A$ is universally
catenary: this follows from `(5.6.1, c))`, if one notes that setting $S = A - \mathfrak{p}$, $S^{-1} B$ is an
$A_{\mathfrak{p}}$-algebra of finite type, and $B_{\mathfrak{q}} = (S^{-1} B)_{S^{-1} \mathfrak{q}}$.*

*(ii) One says that a locally Noetherian prescheme $X$ is **universally catenary** if, for every $x \in X$, the ring
$\mathcal{O}_{x}$ is universally catenary. It follows from (i) that for $A$ to be a universally catenary ring, it is
necessary and sufficient that the scheme $\operatorname{Spec}(A)$ be so.*

*(iii) The criterion `(5.6.1, c))` involves only the images of $A$ in integral $A$-algebras of finite type, hence
integral quotient rings of $A$. One concludes that if*

<!-- original page 99 -->

*$\mathfrak{p}_{i}$ ($1 \leq i \leq n$) are the minimal prime ideals of $A$, it amounts to the same to say that $A$ is
universally catenary or that each of the $A/\mathfrak{p}_{i}$ is so. This also shows that it amounts to the same to say
that a locally Noetherian prescheme $X$ is universally catenary, or that $X_{red}$ is so.*

*(iv) The criterion `(5.6.1, b))` and the remark (i) show that, if $A$ is a universally catenary ring, so is every
$A$-algebra essentially of finite type `(1.3.8)`.*

**Proposition (5.6.4).**

<!-- label: IV.5.6.4 -->

*Every quotient ring of a regular ring is universally catenary.*

It all comes down to seeing that a regular ring $A$ is universally catenary `(5.6.3, (iv))`; now, one knows that
$A[T_{1}, \cdots, T_{n}]$ is regular `(0, 17.3.7)`, hence catenary `(0, 16.5.12)`, and one concludes by `(5.6.1, a))`.

In particular, it follows from Cohen's theorem `(0, 19.8.8)` that every complete Noetherian local ring is universally
catenary. Likewise, every algebra of finite type over a field being a quotient of a regular ring, every prescheme
locally of finite type over a field is universally catenary.

We shall see further on `(6.3.7)` that in `(5.6.4)`, one can replace "regular ring" by "Cohen-Macaulay ring".

**Proposition (5.6.5).**

<!-- label: IV.5.6.5 -->

*Let $Y$ be an irreducible locally Noetherian prescheme, $X$ an irreducible prescheme, $f : X \to Y$ a dominant morphism
locally of finite type. Let $\xi$ (resp. $\eta$) be the generic point of $X$ (resp. $Y$), and let $e =
\dim(f^{-1}(\eta)) = deg.tr_{k(\eta)} k(\xi)$ ("dimension of the generic fibre", cf. $(0_{I}, 2.1.8)$ and `(4.1.1)`).
For every $x \in X$, one has then, setting $y = f(x)$,*

```text
  e + dim(𝒪_y) ≥ deg.tr_k(y) k(x) + dim(𝒪_x)             (5.6.5.1)

  dim(𝒪_x) ≤ dim(𝒪_y) + dim(𝒪_x ⊗_{𝒪_y} k(y)) − δ(x)    (5.6.5.2)
```

*setting $\delta(x) = \dim_{x}(f^{-1}(y)) - e$.*

*Moreover, if $Y$ is universally catenary, the two sides of `(5.6.5.1)` (resp. `(5.6.5.2)`) are equal. If moreover $x$
is closed in $f^{-1}(y)$, one has*

$$ \dim(\mathcal{O}_{x}) = \dim(\mathcal{O}_{y}) + e. (5.6.5.3) $$

One may evidently restrict to the case where $X$ and $Y$ are affine (hence $f$ of finite type) and reduced `(I, 5.4)`,
hence integral. As $f$ is dominant, $\mathcal{O}_{y}$ is then identified with a sub-ring of $\mathcal{O}_{x}$, and the
respective fields of fractions of $\mathcal{O}_{y}$ and $\mathcal{O}_{x}$ with $k(\eta)$ and $k(\xi)$ `(I, 8.2.7)`;
moreover, $\mathcal{O}_{x}$ is a local ring of an integral $\mathcal{O}_{y}$-algebra of finite type $B$ at a prime ideal
$\mathfrak{q}$ `(I, 3.6.5)`; applying `(5.5.8.1)` to $A = \mathcal{O}_{y}$, $B$, and $\mathfrak{q}$, one obtains
`(5.6.5.1)`. Moreover, $\mathcal{O}_{x} \otimes_{\mathcal{O}_{y}} k(y) = \mathcal{O}_{x} / \mathfrak{m}_{y}
\mathcal{O}_{x}$ is none other than the local ring of the fibre $f^{-1}(y)$ at the point $x$ `(I, 3.6.1)`; as
$f^{-1}(y)$ is a prescheme of finite type over $k(y)$, it follows from `(5.2.3)` that one has

```text
  dim(𝒪_x ⊗_{𝒪_y} k(y)) = dim_x(f⁻¹(y)) − deg.tr_{k(y)} k(x);
```

the inequality `(5.6.5.2)` is therefore only another form of `(5.6.5.1)`.

The fact that the two sides of `(5.6.5.1)` are equal when $Y$ is universally

<!-- original page 100 -->

catenary is none other than the equality `(5.6.1.1)`, applied to $A = \mathcal{O}_{y}$ and $B' = \mathcal{O}_{x}$. To
prove that one moreover has `(5.6.5.3)` when $x$ is closed in $f^{-1}(y)$, it suffices to note that, in general,
$deg.tr_{k(y)} k(x)$ is the dimension of $\overline{x} \cap f^{-1}(y)$, as follows from `(5.2.1)` applied to the reduced
closed sub-prescheme of $f^{-1}(y)$ having this sub-space as underlying space.

We shall prove further on `(13.1.1)` that, under the conditions of `(5.6.5)`, one *always* has $\delta(x) \geq 0$, and
`(5.6.5.2)` therefore in this case makes `(5.5.2.1)` more precise.

**Corollary (5.6.6).**

<!-- label: IV.5.6.6 -->

*Under the general hypotheses of `(5.6.5)`, one has*

$$ \dim(X) \leq \dim(Y) + e. (5.6.6.1) $$

*If one supposes moreover $Y$ universally catenary, then, for the two sides of `(5.6.6.1)` to be equal, it is necessary
and sufficient that one have*

```text
  dim(Y) = sup_{y ∈ f(X)} dim(𝒪_y).                      (5.6.6.2)
```

*In particular, the two sides of `(5.6.6.1)` are equal when $Y$ is locally of finite type over a field.*

The inequality `(5.6.6.1)` indeed follows from `(5.6.5.1)` applied at a closed point $x$ of $X$, taking `(5.1.4.2)` and
`(5.1.11)` into account. On the other hand, every non-empty fibre $f^{-1}(y)$ contains a point $x$ closed in this fibre
`(5.1.11)`, and if one supposes $Y$ universally catenary, one has at this point the relation `(5.6.5.3)`. Taking the
upper bounds of the two sides of `(5.6.5.3)` as $x$ runs through $X$, and noting that every point $x$ closed in $X$ is
*a fortiori* closed in $f^{-1}(f(x))$, the second assertion of the corollary follows from `(5.1.4.1)` and `(5.1.4.2)`.

To prove the last assertion, note that there is an affine open neighbourhood $U$ of the generic point of $X$ such that
$f|U$ be of finite type, hence $f(U)$ is a constructible part of $Y$, dense in $Y$ `(1.8.5)`, and consequently contains
a non-empty open part (hence everywhere dense) of $Y$ $(0_{III}, 9.2.2)$. The hypothesis that $Y$ is locally of finite
type over a field then ensures, on the one hand, that $Y$ is universally catenary `(5.6.4)`, and on the other hand that
the two sides of `(5.6.6.2)` are equal `(5.2.2` and `4.1.1.3)`.

One will note that the condition `(5.6.6.2)` is trivially verified when $f$ is surjective.

**Corollary (5.6.7).**

<!-- label: IV.5.6.7 -->

*Let $Y$ be a locally Noetherian prescheme, $f : X \to Y$ a morphism locally of finite type, $n$ an integer. If, for
every $y \in Y$, $\dim(f^{-1}(y)) \leq n$, then one has*

$$ \dim(X) \leq \dim(Y) + n. (5.6.7.1) $$

By virtue of `(0, 14.1.7)` and `(1.5.4)`, one may restrict to the case where $X$ and $Y$ are affine, hence $f$ of finite
type, $X$ and $Y$ reduced; let $X_{i}$ ($1 \leq i \leq m$) be the closed (integral) sub-preschemes of $X$ having as
underlying spaces the irreducible components of $X$; one has `dim(X) = sup_i (dim(X_i))`. If $Z_{i}$ is the reduced
closed sub-prescheme of $Y$ having as underlying space $\overline{f(X_{i})}$, $Z_{i}$ is integral $(0_{I}, 2.1.5)$; the
restriction $X_{i} \to Y$ of $f$ factors as $X_{i} \xrightarrow{g_{i}} Z_{i} \xrightarrow{j_{i}} Y$, where $j_{i}$ is
the canonical injection `(I, 5.2.2)`, and $g_{i}$ is dominant

<!-- original page 101 -->

and of finite type `(1.5.4)`. One has $\dim(Z_{i}) \leq \dim(Y)$ for every $i$; on the other hand, if $\zeta_{i}$ is the
generic point of $Z_{i}$, one has $\dim(g^{-1}_{i}(\zeta_{i})) \leq n$ for every $i$ by hypothesis; one sees thus that
to prove `(5.6.7.1)`, it suffices to show that $\dim(X_{i}) \leq \dim(Z_{i}) + n$ for every $i$, which follows from
`(5.6.6.1)`.

**Corollary (5.6.8).**

<!-- label: IV.5.6.8 -->

*Let $Y$ be a locally Noetherian prescheme, $X$ an irreducible prescheme, $f : X \to Y$ a morphism locally of finite
type, $n$ an integer $\geq 0$. Suppose that $Y$ is universally catenary, and that for every $y \in Y$, one has
$\dim(f^{-1}(y)) \geq n$ (resp. $\dim(f^{-1}(y)) = n$). Then one has*

$$ \dim(X) \geq \dim(Y) + n (5.6.8.1) $$

*(resp.*

```text
  dim(X) = dim(Y) + n).                                  (5.6.8.2)
```

As $n \geq 0$, the hypothesis entails that $f$ is surjective, hence $Y$ irreducible; moreover, if $\eta$ is the generic
point of $Y$, one has $\dim(f^{-1}(\eta)) \geq n$ (resp. $\dim(f^{-1}(\eta)) = n$). The conclusion therefore follows
from `(5.6.6)`.

**Remarks (5.6.9).**

<!-- label: IV.5.6.9 -->

*(i) Even if $Y$ is regular, $X$ irreducible, $f : X \to Y$ dominant and of finite type, the two sides of `(5.6.6.1)`
are not necessarily equal, as shown by the example where $Y = \operatorname{Spec}(A)$ where $A$ is a discrete valuation
ring, $X = \operatorname{Spec}(K)$ where $K$ is the field of fractions of $A$, $f$ being the canonical morphism.*

*(ii) The example `(5.4.3, (i))` shows that in `(5.6.6)` and `(5.6.8)`, one cannot suppress the hypothesis that $X$ is
irreducible, the other hypotheses being verified. We shall, however, see `(10.6.1)` that with supplementary hypotheses
on $Y$, verified for example when $Y$ is a prescheme locally of finite type over a field, or over a Dedekind ring having
an infinity of prime ideals, such phenomena cannot present themselves.*

**Proposition (5.6.10).**

<!-- label: IV.5.6.10 -->

*Let $A$ be an integral universally catenary Noetherian local ring, $B$ an integral ring containing $A$ which is a
finite $A$-algebra. Then, for every maximal ideal $\mathfrak{n}$ of $B$, one has $\dim(B_{\mathfrak{n}}) = \dim(A)$.*

Indeed, one has $deg.tr_{A} B = 0$ and the residue field $k'$ of $B_{\mathfrak{n}}$ is an algebraic extension of the
field of fractions of $A$. The conclusion follows from the formula `(5.6.1.1)`, every maximal ideal of $B$ being above
that of $A$.

**Example (5.6.11).**

<!-- label: IV.5.6.11 -->

*Let $A$ be an integral Noetherian local ring and integrally closed; then one has seen `(0, 16.1.6)` that the conclusion
of `(5.6.10)` is valid for every finite integral $A$-algebra $B$ containing $A$. On the contrary, we shall construct an
example of an integral catenary Noetherian local ring $A$ for which the conclusion of `(5.6.10)` will be in default. We
shall use the construction of `(5.2.5, (i))`. Let $k_{0}$ be a field, $k$ a pure transcendental extension
$k_{0}(S_{i})_{i \in \mathbb{N}}$ of infinite transcendence degree, $V$ the discrete valuation ring $k[S]_{(S)}$, local
ring of the polynomial ring `k[S]` at the prime ideal `(S)`; finally let $E$ be the polynomial ring `V[T]`; one has seen
that in $E$ the maximal ideal $\mathfrak{m} = (S) + (T)$ is of height `2` and the maximal ideal $\mathfrak{m}' = (ST -
1)$ of height `1`;*

<!-- original page 102 -->

*the corresponding residue fields are $k(\mathfrak{m}) = k$ and $k(\mathfrak{m}') = k(S)$, field of fractions of $V$; by
virtue of the choice of $k$, these fields are isomorphic. Denote by $\epsilon$ and $\epsilon'$ the canonical
homomorphisms of $E$ onto $E/\mathfrak{m} = k(\mathfrak{m})$ and $E/\mathfrak{m}' = k(\mathfrak{m}')$ respectively; let
on the other hand $\sigma$ be an isomorphism of $k(\mathfrak{m})$ onto $k(\mathfrak{m}')$, and consider the sub-ring $C$
of $E$ formed by $x \in E$ such that $\epsilon'(x) = \sigma(\epsilon(x))$ (this construction is a particular case of the
"gluing procedures" which will be studied systematically in Chap. V). It is immediate that $\mathfrak{n} = \mathfrak{m}
\mathfrak{m}' = \mathfrak{m} \cap \mathfrak{m}'$ is a maximal ideal of $C$, $C/\mathfrak{m} \mathfrak{m}'$ being
identified with the sub-field of $(E/\mathfrak{m}) \times (E/\mathfrak{m}')$ formed by pairs $(z, \sigma(z))$. One has
$E = C + C(ST - 1)$, in other words $E$ is a finite $C$-algebra and is evidently the integral closure of $C$; we shall
see in addition that $C$ is Noetherian: this will follow from the following lemma:*

**Lemma (5.6.11.1).**

<!-- label: IV.5.6.11.1 -->

*Let $R$ be a ring, $S$ a sub-ring, $\mathfrak{K} = Ann_{S}(R/S)$ the **conductor** of $S$ in $R$ (largest ideal of $S$
which is also an ideal of $R$).*

*(i) For every ideal $\mathfrak{J} \subset \mathfrak{K}$ of $R$, there exists a strictly increasing map of the set of
ideals $\mathfrak{a}$ of $S$ such that $R \cdot \mathfrak{a} = \mathfrak{J}$ to the set of
sub-$(S/\mathfrak{K})$-modules of $\mathfrak{J}/\mathfrak{K} \mathfrak{J}$.*

*(ii) If $S/\mathfrak{K}$ and $R$ are Noetherian and if $R$ is an $S$-module of finite type, then every increasing
sequence of ideals of $S$ contained in $\mathfrak{K}$ is stationary.*

(i) One has indeed, $\mathfrak{K} \mathfrak{J} = \mathfrak{K}(R \cdot \mathfrak{a}) = \mathfrak{K} \mathfrak{a} \subset
\mathfrak{a}$ ($\mathfrak{a}$ being an ideal of $S$), whence the conclusion.

(ii) Let $(\mathfrak{L}_{n})$ be an increasing sequence of ideals of $S$ contained in $\mathfrak{K}$. The sequence of
ideals $R \cdot \mathfrak{L}_{n}$ of $R$ is stationary since $R$ is Noetherian; one may therefore suppose that all the
ideals $R \cdot \mathfrak{L}_{n}$ are equal to the same ideal $\mathfrak{J}$ of $R$. As $R$ is Noetherian,
$\mathfrak{J}/\mathfrak{K} \mathfrak{J}$ is an $R$-module of finite type, hence also an $S$-module of finite type, and
consequently an $(S/\mathfrak{K})$-module of finite type. But since $S/\mathfrak{K}$ is Noetherian,
$\mathfrak{J}/\mathfrak{K} \mathfrak{J}$ is an $(S/\mathfrak{K})$-Noetherian module, and the conclusion follows from
(i).

We shall apply this lemma taking $R = E$, $S = C$; it is clear that $\mathfrak{n}$ is the conductor of $C$ in $E$;
moreover, for every ideal $\mathfrak{a}$ of $C$, $\mathfrak{a}/(\mathfrak{n} \cap \mathfrak{a})$ is isomorphic to
$(\mathfrak{a} + \mathfrak{n})/\mathfrak{n}$, hence a sub-$C$-module of $C/\mathfrak{n}$, which is a simple $C$-module;
it therefore suffices to show that every ideal $\mathfrak{a} \subset \mathfrak{n}$ of $C$ is of finite type, and this
follows from `(5.6.11.1)`.

It follows from `(0, 16.1.5)` that one has $\dim(C) = \dim(E) = 2$. Take $A = C_{\mathfrak{n}}$; if $U = C -
\mathfrak{n}$, the ring of fractions $B = U^{-1} E$ is therefore the integral closure of $A$, and is an $A$-module of
finite type; moreover, as $\mathfrak{m}$ and $\mathfrak{m}'$ are the only prime ideals of $E$ containing $\mathfrak{n}$,
$B$ is a semi-local ring whose local rings at the two maximal ideals are isomorphic to $E_{\mathfrak{m}}$ and
$E_{\mathfrak{m}'}$ respectively, hence are respectively of dimension `2` and `1`. This shows that $\dim(B) = 2$, so
also $\dim(A) = 2$ `(0, 16.1.5)`. As $A$ is an integral local ring, it is necessarily catenary (every prime ideal
distinct from `0` and from the maximal ideal being necessarily of height `1`); but it does not verify the conclusion of
`(5.6.10)`, and *a fortiori* is not universally catenary.

Note further that $\mathfrak{n}$ is an ideal of height `2` in $C$, and that for every prime ideal $\mathfrak{p}$ of
height `1` in $C$, there exists a unique prime ideal $\mathfrak{p}'$ of $E$ above $\mathfrak{p}$, necessarily of height
`1`, and such that $C_{\mathfrak{p}} = E_{\mathfrak{p}'}$. Indeed, there is at least one prime ideal $\mathfrak{p}'$ of
$E$ above $\mathfrak{p}$ and it follows from the Cohen-Seidenberg theorem that such

<!-- original page 103 -->

an ideal is necessarily of height `1`; moreover, as $E$ is a finite $C$-algebra and $\mathfrak{p} \neq \mathfrak{n}$,
$C_{\mathfrak{p}}$ is integrally closed (Bourbaki, *Alg. comm.*, chap. V, §1, n° 5, cor. 5 of prop. 16), hence
$E_{\mathfrak{p}} = C_{\mathfrak{p}}$, which proves our assertions.

It would be interesting to know whether every integral Noetherian local ring verifying the conclusion of `(5.6.10)` is
universally catenary; this is what Nagata `[33]` affirmed, but his proof does not seem to be complete.

### 5.7. Depth and property $(S_{n})$

**Definition (5.7.1).**

<!-- label: IV.5.7.1 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. One calls **depth**
(resp. **codepth**) of $\mathcal{F}$ at a point $x \in X$ the number $prof(\mathcal{F}_{x})$ (resp.
$coprof(\mathcal{F}_{x})$) `(0, 16.4.5 and 16.4.9)`. One calls **codepth** of $\mathcal{F}$ the number*

```text
  coprof(ℱ) = sup_{x ∈ X} coprof(ℱ_x).                   (5.7.1.1)
```

One says that $\mathcal{F}$ is a **Cohen-Macaulay $\mathcal{O}_{X}$-Module at $x$** if $\mathcal{F}_{x}$ is a
Cohen-Macaulay $\mathcal{O}_{x}$-module, that is to say `(0, 16.5.1)` if $coprof(\mathcal{F}_{x}) = 0$. One says that
$\mathcal{F}$ is a **Cohen-Macaulay $\mathcal{O}_{X}$-Module** if it is so at every point, in other words if
$coprof(\mathcal{F}) = 0$. A point $x \in X$ such that $\mathcal{O}_{x}$ is a Cohen-Macaulay ring is also called a
**Cohen-Macaulay point** of $X$.

One calls **codepth of $X$** and denotes by $coprof(X)$ the number $coprof(\mathcal{O}_{X})$. One says that $X$ is a
**Cohen-Macaulay prescheme** if $\mathcal{O}_{X}$ is a Cohen-Macaulay $\mathcal{O}_{X}$-Module, in other words if
$coprof(X) = 0$. Every locally Noetherian prescheme of dimension `0` is evidently a Cohen-Macaulay prescheme. To say
that $\operatorname{Spec}(A)$ is a Cohen-Macaulay scheme means that $A$ is a Cohen-Macaulay ring `(0, 16.5.13)`.

**Definition (5.7.2).**

<!-- label: IV.5.7.2 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module, $k$ a positive or
negative integer. One says that $\mathcal{F}$ possesses the property $(S_{k})$ if, for every $x \in X$, one has*

```text
  prof(ℱ_x) ≥ inf(k, dim(ℱ_x)).                          (5.7.2.1)
```

*One says that $\mathcal{F}$ possesses the property $(S_{k})$ **at a point $x \in X$** if, for every generization $x'$
of $x$ in $X$, one has*

```text
  prof(ℱ_{x'}) ≥ inf(k, dim(ℱ_{x'})).                    (5.7.2.2)
```

One says that $X$ *verifies* the property $(S_{k})$ (resp. *verifies the property $(S_{k})$ at a point $x$*) if
$\mathcal{O}_{X}$ verifies the property $(S_{k})$ (resp. verifies the property $(S_{k})$ at the point $x$).

For $\mathcal{F}$ to verify the property $(S_{k})$, it is evidently necessary and sufficient that it verify it at every
point of $X$. If $U$ is an open of $X$ and if $\mathcal{F}$ verifies $(S_{k})$, so does $\mathcal{F}|U$; conversely, if
$(U_{\alpha})$ is an open cover of $X$ and if $\mathcal{F}|U_{\alpha}$ verifies $(S_{k})$ for every $\alpha$,
$\mathcal{F}$ verifies $(S_{k})$.

**Remarks (5.7.3).**

<!-- label: IV.5.7.3 -->

*(i) Recall that one always has $prof(\mathcal{F}_{x}) \leq \dim(\mathcal{F}_{x})$ `(0, 16.4.5.1)` if $\mathcal{F}_{x}
\neq 0$. To say that $\mathcal{F}$ possesses the property $(S_{k})$ therefore means that one has $prof(\mathcal{F}_{x})
\geq k$ except at points $x \in X$ such that $\dim(\mathcal{F}_{x}) < k$ and that at these latter points one has
$\dim(\mathcal{F}_{x}) = prof(\mathcal{F}_{x})$, that is to say `(0, 16.5.1)` that $\mathcal{F}$ is a Cohen-Macaulay
$\mathcal{O}_{x}$-Module at these points; one will note that at points where $\dim(\mathcal{F}_{x}) = k$, one has
$prof(\mathcal{F}_{x}) = k$,*

<!-- original page 104 -->

*hence $\mathcal{F}$ is again a Cohen-Macaulay $\mathcal{O}_{x}$-Module at these points. To say that $\mathcal{F}$
possesses the property $(S_{k})$ for every $k$ therefore means that $\mathcal{F}$ is a Cohen-Macaulay
$\mathcal{O}_{X}$-Module. It is clear that for $k' \geq k$, the property $(S_{k'})$ implies $(S_{k})$; for $k \leq 0$,
every coherent $\mathcal{O}_{X}$-Module has the property $(S_{k})$.*

*(ii) To verify the condition `(5.7.2.1)`, one may restrict to the case where $x \in Supp(\mathcal{F})$; in the contrary
case one has indeed $\dim(\mathcal{F}_{x}) = -\infty$ `(0, 14.1.2)`.*

*(iii) If $X = \operatorname{Spec}(A)$, where $A$ is a Noetherian ring, and $\mathcal{F} = \tilde{M}$, where $M$ is an
$A$-module of finite type, one says that $M$ possesses the property $(S_{k})$ if $\mathcal{F}$ possesses this property.
For an arbitrary locally Noetherian prescheme $X$, to say that $\mathcal{F}$ possesses the property $(S_{k})$ at a point
$x \in X$ therefore means that if one sets $Y = \operatorname{Spec}(\mathcal{O}_{x})$, the $\mathcal{O}_{Y}$-Module
$\tilde{\mathcal{F}}_{x}$ possesses the property $(S_{k})$; one will note that the condition `(5.7.2.1)` in general does
not entail `(5.7.2.2)` for every generization $x'$ of $x$, given that one has no inequality relation between
$prof(\mathcal{F}_{x})$ and $prof(\mathcal{F}_{x'})$ `(0, 16.4.6)`.*

*(iv) It follows at once from the definition that if $\mathcal{F}$ verifies $(S_{k})$ at a point $x$, it also verifies
$(S_{k})$ at every point $x'$ generization of $x$.*

*(v) The property $(S_{k})$ is most important for $k = 1$ and $k = 2$; it was introduced for $k = 2$ by Serre, to
express his criterion of normality (cf. `(5.8.5)`).*

*(vi) Let $X$ be a locally Noetherian prescheme, $Y$ a closed sub-prescheme of $X$, $j : Y \to X$ the canonical
injection, $\mathcal{G}$ a coherent $\mathcal{O}_{Y}$-Module. It is clear that for every $x \in Y$, one has
$\dim(\mathcal{G}_{x}) = \dim((j_{*}(\mathcal{G}))_{x})$ and $prof(\mathcal{G}_{x}) = prof((j_{*}(\mathcal{G}))_{x})$,
whence $coprof(\mathcal{G}_{x}) = coprof((j_{*}(\mathcal{G}))_{x})$. For $\mathcal{G}$ to verify $(S_{k})$, it is
necessary and sufficient that $j_{*}(\mathcal{G})$ verify $(S_{k})$.*

**Proposition (5.7.4).**

<!-- label: IV.5.7.4 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. Set
$S = Supp(\mathcal{F})$, and for every $n \geq 0$, denote by $Z_{n}$ the set of $z \in X$ such that
$coprof(\mathcal{F}_{z}) > n$, so that $Z_{n} \subset S$.*

*(i) For $\mathcal{F}$ to verify the property $(S_{k})$, it is necessary and sufficient that, for every $n \geq 0$, one
has*

```text
  codim(Z_n, S) > n + k.                                 (5.7.4.1)
```

*(ii) Suppose moreover that the $Z_{n}$ are closed in $X$. Then, for $\mathcal{F}$ to verify the property $(S_{k})$ at a
point $x \in S$, it is necessary and sufficient that, for every $n \geq 0$, one has*

```text
  codim_x(Z_n, S) > n + k.                               (5.7.4.2)
```

(i) One has indeed, by definition `(5.1.3)`, `codim(Z_n, S) = inf_{z ∈ Z_n} (dim(𝒪_{S,z}))` and the inequality
`(5.7.4.1)` therefore means `(5.1.12.2)` that, for every $z \in X$, and every $n \geq 0$, the relation

$$ \dim(\mathcal{F}_{z}) - prof(\mathcal{F}_{z}) \geq n + 1 $$

entails the relation

$$ \dim(\mathcal{F}_{z}) \geq n + k + 1. $$

But if one sets $a = \dim(\mathcal{F}_{z})$, $b = prof(\mathcal{F}_{z})$, one has $b \leq a$, and to say that for every
$n \geq 0$, the relation $b \leq a - n - 1$ implies $k \leq a - n - 1$ is equivalent to saying that $b \geq \inf(k, a)$,
whence the proposition.

<!-- original page 105 -->

(ii) The reasoning is the same as in (i), with this difference that one must limit oneself to the $z \in X$ which are
generizations of $x$, and take `(5.1.3.2)` into account.

**Proposition (5.7.5).**

<!-- label: IV.5.7.5 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. For $\mathcal{F}$ to
verify $(S_{k})$ ($k \geq 1$), it is necessary and sufficient that for every integer $r$ such that $0 \leq r < k$, every
open $U$ of $X$, and every $(\mathcal{F}|U)$-regular sequence $(f_{i})_{1 \leq i \leq r}$ of sections of
$\mathcal{O}_{X}$ over $U$, $(\mathcal{F}|U)/(\sum^{r}_{i=1} f_{i}(\mathcal{F}|U))$ is without embedded associated prime
cycle.*

Let us first prove the proposition for $k = 1$; it then states again that for $\mathcal{F}$ to verify `(S_1)`, it is
necessary and sufficient that $\mathcal{F}$ be without embedded associated prime cycle. Indeed, to say that
$\mathcal{F}$ verifies `(S_1)` means that at the points $x \in Supp(\mathcal{F})$ such that $\dim(\mathcal{F}_{x}) > 0$,
one has $prof(\mathcal{F}_{x}) \geq 1$ (since at the other points of $Supp(\mathcal{F})$ one has $\dim(\mathcal{F}_{x})
= 0$, hence $prof(\mathcal{F}_{x}) = 0$); but to say that $prof(\mathcal{F}_{x}) \geq 1$ means that $\mathfrak{m}_{x}$
is not associated to $\mathcal{F}_{x}$ `(0, 16.4.6, (i))`, or again that $x$ is not associated to $\mathcal{F}$
`(3.1.1)`; on the other hand, if $S$ is a sub-prescheme of $X$ having $Supp(\mathcal{F})$ as underlying space, one has
`(5.1.12.1)` $\dim(\mathcal{F}_{x}) = \dim(\mathcal{O}_{S,x})$; to say that $\dim(\mathcal{F}_{x}) > 0$ therefore means
that $x$ is not a maximal point of $Supp(\mathcal{F})$ `(5.1.2)`, whence the conclusion.

In the second place, let us show that, for any $k > 1$, the condition of the statement is *necessary*. One may restrict
to considering the case where $U = X$, and our assertion will be proved (by induction on $k$ and by virtue of the first
part of the reasoning) if we show that when $\mathcal{F}$ verifies $(S_{k})$ ($k > 1$) and $f$ is an
$\mathcal{F}$-regular section of $\mathcal{O}_{X}$ over $X$, then $\mathcal{F}/f\mathcal{F}$ verifies $(S_{k-1})$ (i.e.
verifies `(5.7.2.1)` with $k$ replaced by $k - 1$). Now, for every $x \in X$, $f_{x}$ is an $\mathcal{F}_{x}$-regular
element; if it is invertible, one has $\mathcal{F}_{x} / f_{x} \mathcal{F}_{x} = 0$ and the conclusion is trivial. If on
the contrary $f_{x} \in \mathfrak{m}_{x}$, one knows that one has $prof(\mathcal{F}_{x} / f_{x} \mathcal{F}_{x}) =
prof(\mathcal{F}_{x}) - 1$ `(0, 16.4.6, (i))`, and $\dim(\mathcal{F}_{x} / f_{x} \mathcal{F}_{x}) =
\dim(\mathcal{F}_{x}) - 1$ `(0, 16.3.4)`, and our assertion follows.

Let us prove finally that for $k > 1$, the condition of the statement is *sufficient*. We shall proceed by induction on
$k$; let $x$ be a point of $X$, and suppose first that $\dim(\mathcal{F}_{x}) \geq k$. The induction hypothesis entails
that $\mathcal{F}$ verifies $(S_{k-1})$, hence $prof(\mathcal{F}_{x}) \geq k - 1$; taking `(0, 15.2.4)` into account,
there is therefore an open neighbourhood $U$ of $x$ and an $(\mathcal{F}|U)$-regular sequence $(f_{i})_{1 \leq i \leq
k-1}$ of sections of $\mathcal{O}_{X}$ over $U$, such that $(f_{i})_{x} \in \mathfrak{m}_{x}$ for $1 \leq i \leq k - 1$.
The hypothesis entails that $\mathcal{G} = (\mathcal{F}|U)/(\sum^{k-1}_{i=1} f_{i}(\mathcal{F}|U))$ is without embedded
associated prime cycle; but one has $\dim(\mathcal{G}_{x}) = \dim(\mathcal{F}_{x}) - (k - 1) \geq 1$ `(0, 16.3.4)`, so
$x$ is not associated to $\mathcal{G}$; one therefore has $prof(\mathcal{G}_{x}) \geq 1$ `(0, 16.4.6)`, and as
$prof(\mathcal{G}_{x}) = prof(\mathcal{F}_{x}) - (k - 1)$

<!-- original page 106 -->

`(0, 16.4.6)`, one has $prof(\mathcal{F}_{x}) \geq k$. Suppose in the second place that $\dim(\mathcal{F}_{x}) = r < k$;
as $\mathcal{F}$ verifies $(S_{k-1})$, one has $prof(\mathcal{F}_{x}) \geq \inf(k - 1, r) = r$, and this completes the
proof.

**Corollary (5.7.6).**

<!-- label: IV.5.7.6 -->

*Suppose that $\mathcal{F}$ verifies $(S_{k})$ ($k \geq 1$); if $(f_{i})$ ($1 \leq i \leq r$) is an
$\mathcal{F}$-regular sequence of sections of $\mathcal{O}_{X}$ over $X$ and if $r < k$, $\mathcal{F}/(\sum^{r}_{i=1}
f_{i} \mathcal{F})$ verifies $(S_{k-r})$.*

This follows immediately from `(5.7.5)`.

**Corollary (5.7.7).**

<!-- label: IV.5.7.7 -->

*For $\mathcal{F}$ to verify `(S_2)`, it is necessary and sufficient that $\mathcal{F}$ be without embedded associated
prime cycle and that for every open $U$ of $X$ and every $(\mathcal{F}|U)$-regular section $f$ of $\mathcal{O}_{X}$ over
$U$, $(\mathcal{F}|U)/f(\mathcal{F}|U)$ be without embedded associated prime cycle.*

**Remarks (5.7.8).**

<!-- label: IV.5.7.8 -->

*Let $X$ be a locally Noetherian prescheme of dimension `1`; it then amounts to the same to say that $X$ is a
Cohen-Macaulay prescheme, or that it verifies `(S_1)`, or that it verifies one of the properties $(S_{n})$ for $n \geq
1$, by virtue of the definitions `(5.7.1)` and `(5.7.2)`. By virtue of `(5.7.5)`, it therefore again amounts to the
same, for preschemes of dimension `1`, to say that $X$ is a Cohen-Macaulay prescheme or that it has no embedded
associated prime cycle. For example, a locally Noetherian reduced prescheme of dimension `1` is a Cohen-Macaulay
prescheme.*

**Proposition (5.7.9).**

<!-- label: IV.5.7.9 -->

*Let $A$, $B$ be two Noetherian rings, $\rho : A \to B$ a ring homomorphism, $M$ a $B$-module such that $M_{[\rho]}$ is
an $A$-module of finite type. Let $\mathfrak{p}$ be a prime ideal of $A$; the prime ideals of $B$ above $\mathfrak{p}$
and belonging to $Supp(M)$ are finite in number, and if $(\mathfrak{q}_{i})_{1 \leq i \leq n}$ is the family of these
ideals, one has*

```text
  dim_{A_𝔭}(M_𝔭) = sup_i dim_{B_{𝔮_i}}(M_{𝔮_i})          (5.7.9.1)

  prof_{A_𝔭}(M_𝔭) = inf_i prof_{B_{𝔮_i}}(M_{𝔮_i}).       (5.7.9.2)
```

If $\mathfrak{b}$ is the annihilator of $M$, $B/\mathfrak{b}$ is identified with a sub-$A$-module of
$\operatorname{End}_{A}(M_{[\rho]})$, hence of finite type since $A$ is Noetherian; there are therefore only finitely
many prime ideals of $B$ above $\mathfrak{p}$ and containing $\mathfrak{b}$, and these are precisely those which belong
to $Supp(M)$. Replacing $B$ by $B/\mathfrak{b}$, which does not change the second members of `(5.7.9.1)` and `(5.7.9.2)`
(by `(0, 16.1.9)` and `(0, 16.4.8)`), one may therefore suppose that $B$ is a finite $A$-algebra. Set $S = A -
\mathfrak{p}$, and $B' = S^{-1} B$; $B'$ is a Noetherian semi-local ring whose maximal ideals are $S^{-1}
\mathfrak{q}_{i}$ ($1 \leq i \leq n$) and as $M_{\mathfrak{p}}$ is an $A_{\mathfrak{p}}$-module of finite type, one has
$\dim_{A_{\mathfrak{p}}}(M_{\mathfrak{p}}) = \dim_{B'}(M_{\mathfrak{p}})$ `(0, 16.1.9)`. This being so, the relation
`(5.7.9.1)` becomes a particular case of `(0, 16.1.7.4)`. To prove the relation `(5.7.9.2)`, one reduces at once as in
`(0, 16.4.8)` to the case where $prof_{A_{\mathfrak{p}}}(M_{\mathfrak{p}}) = 0$, and the same reasoning as in
`(0, 16.4.8)` shows that $M_{\mathfrak{p}}$ contains a sub-$B'$-module of finite length, and consequently also a
*simple* sub-$B'$-module, but such a sub-module is necessarily isomorphic to the residue field of one of the
$B'_{\mathfrak{q}_{i}}$, hence there is at least one index $i$ such that
$prof_{B_{\mathfrak{q}_{i}}}(M_{\mathfrak{q}_{i}}) = 0$ `(0, 16.4.6)`, which terminates the proof.

**Corollary (5.7.10).**

<!-- label: IV.5.7.10 -->

*Suppose the hypotheses of `(5.7.9)` are verified, and suppose moreover that $A$ is a local ring; then, for $M$ to be a
Cohen-Macaulay $A$-module, it is necessary and sufficient that, for all the prime ideals $\mathfrak{q}_{i}$ of $B$ above
the maximal ideal of $A$, $M$ be a Cohen-Macaulay $B_{\mathfrak{q}_{i}}$-module, and moreover that all the numbers
$\dim_{B_{\mathfrak{q}_{i}}}(M_{\mathfrak{q}_{i}})$ be equal.*

It indeed follows from `(5.7.9.1)` and `(5.7.9.2)` that these conditions are equivalent to the relation $\dim_{A}(M) =
prof_{A}(M)$.

**Corollary (5.7.11).**

<!-- label: IV.5.7.11 -->

*Suppose the hypotheses of `(5.7.9)` are verified.*

*(i) If $M_{[\rho]}$ verifies the property $(S_{k})$, so does $M$.*

*(ii) Suppose that for every pair of prime ideals $\mathfrak{q}$, $\mathfrak{q}'$ of $B$ such that
$\rho^{-1}(\mathfrak{q}) = \rho^{-1}(\mathfrak{q}')$, one has $\dim_{B_{\mathfrak{q}}}(M_{\mathfrak{q}}) =
\dim_{B_{\mathfrak{q}'}}(M_{\mathfrak{q}'})$. Then, if $M$ verifies the property $(S_{k})$, so does $M_{[\rho]}$.*

<!-- original page 107 -->

This follows at once from the relations `(5.7.9.1)` and `(5.7.9.2)` and from the definition of the property $(S_{k})$.

**(5.7.12)**

<!-- label: IV.5.7.12 -->

In conformity with the definitions of `(5.7.1)`, given any Noetherian ring $A$ and an $A$-module of finite type $M$, one
defines $coprof_{A}(M)$ as equal to `coprof(M̃) = sup_{x ∈ X} (coprof_{A_x}(M_x))`, where $X = \operatorname{Spec}(A)$;
we shall see further on `(6.11.5)` that this definition coincides with that of `(0, 16.4.9)` when $A$ is a Noetherian
*local* ring.

**Corollary (5.7.13).**

<!-- label: IV.5.7.13 -->

*Let $A$, $B$ be two Noetherian rings, $\rho : A \to B$ a ring homomorphism, $M$ a $B$-module such that $M_{[\rho]}$ is
an $A$-module of finite type. Then one has*

$$ coprof_{A}(M_{[\rho]}) \leq coprof_{B}(M). (5.7.13.1) $$

This follows from the preceding definition and from the relations `(5.7.9.1)` and `(5.7.9.2)`.

### 5.8. Regular preschemes and property $(R_{n})$. Serre's normality criterion

**(5.8.1)**

<!-- label: IV.5.8.1 -->

Recall $(0_{I}, 4.1.4)$ that a ringed space $(X, \mathcal{O}_{X})$ is said to be *regular* at a point $x \in X$ if
$\mathcal{O}_{x}$ is a regular ring. When dealing with preschemes, we shall use this terminology in this chapter only
when $X$ is locally Noetherian.

**Definition (5.8.2).**

<!-- label: IV.5.8.2 -->

*One says that a locally Noetherian prescheme $X$ is **regular in codimension $\leq k$**, or **possesses the property
$(R_{k})$** if the set of points where $X$ is not regular is of codimension $> k$ (in other words `(5.1.3)`, if, for
every $x \in X$, the relation $\dim(\mathcal{O}_{x}) \leq k$ entails that $\mathcal{O}_{x}$ is regular).*

To say that $X$ is regular means that $X$ possesses the property $(R_{k})$ for every $k$.

If $X = \operatorname{Spec}(A)$, where $A$ is a Noetherian ring, one will say that $A$ possesses the property $(R_{k})$
if $X$ possesses this property; to say that $X$ is regular means that the ring $A$ is regular `(0, 17.3.6)`. For any
locally Noetherian prescheme $X$, one will say that $X$ possesses the property $(R_{k})$ at a point $x \in X$ if the
local ring $\mathcal{O}_{x}$ possesses the property $(R_{k})$; this therefore means that for every generization $x'$ of
$x$ in $X$, the relation $\dim(\mathcal{O}_{x'}) \leq k$ entails that $\mathcal{O}_{x'}$ is a regular local ring. To say
that $X$ is regular at a point $x$ is equivalent to saying that $X$ verifies the property $(R_{n})$ for every $n \geq 0$
at the point $x$, by virtue of `(0, 17.3.6)`.

**Proposition (5.8.3).**

<!-- label: IV.5.8.3 -->

*If $k$ is a field, $X$ a prescheme locally of finite type over $k$, then, for every $x \in X$, there exists an open
neighbourhood of $x$ in $X$ isomorphic to a sub-scheme of a regular $k$-scheme.*

Indeed, there is an affine open neighbourhood $U$ of $x$ isomorphic to a $k$-scheme of the form
$\operatorname{Spec}(A)$, where $A$ is a $k$-algebra of finite type; $A$ is consequently isomorphic to a quotient of a
polynomial algebra $k[T_{1}, \cdots, T_{n}]$, and one knows that the latter is a regular ring `(0, 17.3.7)`.

**(5.8.4)**

<!-- label: IV.5.8.4 -->

By virtue of `(5.8.2)`, to say that $X$ possesses the property `(R_0)` means that for every maximal point $x$ of $X$,
the ring $\mathcal{O}_{x}$ is a field `(0, 17.1.4)`, in other words that $X$ is reduced at this point. As the set $U$ of
$x \in X$ where $X$ is reduced is open (the

<!-- original page 108 -->

nilradical of $X$ being a coherent $\mathcal{O}_{X}$-Module (`(I, 6.1.1)` and $(0_{I}, 5.2.2)$)), it amounts to the same
to say that $X$ possesses the property `(R_0)` or that the set $U$ is everywhere dense. Consequently:

**Proposition (5.8.5).**

<!-- label: IV.5.8.5 -->

*For a locally Noetherian prescheme $X$ to be reduced, it is necessary and sufficient that it verify the properties
`(S_1)` and `(R_0)`.*

Taking `(5.7.5)` into account, this follows from the preceding remark and from `(3.2.1)`.

**Theorem (5.8.6) (Serre's criterion).**

<!-- label: IV.5.8.6 -->

*Let $X$ be a locally Noetherian prescheme. For $X$ to be normal, it is necessary and sufficient that $X$ verify the
properties `(S_2)` and `(R_1)`, in other words, that for every $x \in X$, one has the following properties:*

*(i) If $\dim(\mathcal{O}_{x}) \leq 1$, $\mathcal{O}_{x}$ is regular (that is to say is a field or a discrete valuation
ring `(0, 17.1.4)`).*

*(ii) If $\dim(\mathcal{O}_{x}) \geq 2$, then $prof(\mathcal{O}_{x}) \geq 2$.*

The conditions are *necessary*. Indeed, to say that $X$ is normal means that for every $x \in X$, $\mathcal{O}_{x}$ is
an integrally closed Noetherian local ring. If $\dim(\mathcal{O}_{x}) = 0$ (resp. $\dim(\mathcal{O}_{x}) = 1$), one
concludes that $\mathcal{O}_{x}$ is a field since $\mathcal{O}_{x}$ is integral (resp. that $\mathcal{O}_{x}$ is a
discrete valuation ring, by virtue of `(II, 7.1.6)`). On the other hand, for every element $f_{x} \neq 0$ of
$\mathcal{O}_{x}$, one knows (Bourbaki, *Alg. comm.*, chap. VII, §1, n° 4, prop. 8) that the prime ideals associated to
$\mathcal{O}_{x} / f_{x} \mathcal{O}_{x}$ are non-embedded, so $\mathcal{O}_{x}$ verifies `(S_2)` `(5.7.7)`.

The conditions are *sufficient*. Indeed, it follows first from `(5.8.5)` that $X$ is reduced. The question being local,
one may moreover suppose that $X = \operatorname{Spec}(A)$, where $A$ is a reduced Noetherian ring `(I, 5.1.4)`; if $R$
is the total ring of fractions of $A$, $R$ is a direct composite of a finite number of fields, and (taking `(II, 6.3.6)`
into account), it will suffice to prove that $A$ is integrally closed in $R$. Let $h = f/g$ be an element of $R$
integral over $A$, with $g$ and $f$ elements of $A$ such that $g$ is not a zero-divisor. One has a relation of the form

```text
  f^n + ∑_{i=1}^n a_i f^{n−i} g^i = 0   with  a_i ∈ A   for 1 ≤ i ≤ n.   (5.8.6.1)
```

Let $\mathfrak{p}$ be a prime ideal of $A$ such that $\dim(A_{\mathfrak{p}}) = 1$; if $f_{\mathfrak{p}}$ and
$g_{\mathfrak{p}}$ are the images of $f$ and $g$ in $A_{\mathfrak{p}}$, it follows from `(5.8.6.1)` that
$f_{\mathfrak{p}}/g_{\mathfrak{p}}$ (which belongs to the total ring of fractions of $A_{\mathfrak{p}}$, since
$g_{\mathfrak{p}}$ is not a zero-divisor in $A_{\mathfrak{p}}$ by flatness $(0_{I}, 5.3.1)$) is integral over
$A_{\mathfrak{p}}$; but as $A_{\mathfrak{p}}$ is regular, hence integrally closed, one has
$f_{\mathfrak{p}}/g_{\mathfrak{p}} \in A_{\mathfrak{p}}$. In other terms, one has $(fA)_{\mathfrak{p}} \subset
(gA)_{\mathfrak{p}}$. But the hypothesis `(S_2)` entails `(5.7.7)`, since $g$ is not a zero-divisor in $A$, that $A/gA$
has only non-embedded associated prime ideals $\mathfrak{p}_{i}$ ($1 \leq i \leq n$); now, `gA` is the intersection of
primary ideals $\mathfrak{q}_{i}$ corresponding to the $\mathfrak{p}_{i}$, and from what has just been seen, the
$\mathfrak{q}_{i}$ are the inverse images in $A$, by the homomorphisms $A \to A_{\mathfrak{p}_{i}}$, of the ideals
$(gA)_{\mathfrak{p}_{i}}$ (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 3, prop. 5). But by virtue of the Hauptidealsatz
`(0, 16.3.2)` one has $\dim(A_{\mathfrak{p}_{i}}) = 1$ for $1 \leq i \leq n$, hence $(fA)_{\mathfrak{p}_{i}} \subset
(gA)_{\mathfrak{p}_{i}}$ for every $i$ according to what precedes; as `fA` is contained in the intersection of the
inverse images of the $(fA)_{\mathfrak{p}_{i}}$ ($1 \leq i \leq n$), one has $fA \subset gA$, that is to say $f/g \in
A$. Q.E.D.

<!-- original page 109 -->

### 5.9. $Z$-pure and $Z$-closed Modules

Part of the notions and results of this section and of the following one are special cases of notions and results
developed in Chapter III in the theory of local cohomology. For the convenience of the reader, we give here an
independent exposition.

**(5.9.1)**

<!-- label: IV.5.9.1 -->

Let $X$ be a locally Noetherian prescheme, $Z$ a part of $X$ stable under specialization: this means that for every
finite part $M$ of $Z$, the closure of $M$ is contained in $Z$, and consequently $Z$ is the union of an increasing
filtered family $(Z_{\alpha})$ of closed parts of $X$; conversely, it is clear that such a union is stable under
specialization.

Set $U_{\alpha} = X - Z_{\alpha}$, so that $X - Z$ is the intersection of the decreasing filtered family of open sets
$U_{\alpha}$; let $i_{\alpha} : U_{\alpha} \to X$ be the canonical injection, and for $U_{\alpha} \supset U_{\beta}$,
let $i_{\alpha \beta} : U_{\beta} \to U_{\alpha}$ be the canonical injection, so that one has $i_{\beta} = i_{\alpha}
\circ i_{\alpha \beta}$. Let $\mathcal{F}$ be an $\mathcal{O}_{X}$-Module (not necessarily quasi-coherent); one then has
$(i_{\beta})_{*}(\mathcal{F}|U_{\beta}) = (i_{\alpha})_{*}((i_{\alpha \beta})_{*}(\mathcal{F}|U_{\beta}))$; from the
canonical homomorphism $(0_{I}, 4.4.3.2)$

$$ \mathcal{F}|U_{\alpha} \to (i_{\alpha \beta})_{*}(\mathcal{F}|U_{\beta}) $$

one deduces, by application of the functor $(i_{\alpha})_{*}$, a homomorphism

$$ \rho_{\beta \alpha} : (i_{\alpha})_{*}(\mathcal{F}|U_{\alpha}) \to (i_{\beta})_{*}(\mathcal{F}|U_{\beta}) $$

and one verifies at once that one has $\rho_{\gamma \alpha} = \rho_{\gamma \beta} \circ \rho_{\beta \alpha}$ for
$U_{\alpha} \supset U_{\beta} \supset U_{\gamma}$; in other words, the $\mathcal{O}_{X}$-Modules
$(i_{\alpha})_{*}(\mathcal{F}|U_{\alpha})$ form an inductive system for the homomorphisms $\rho_{\beta \alpha}$. One
sets

$$ \mathcal{H}^{0}_{X/Z}(\mathcal{F}) = \lim\to_{\alpha} (i_{\alpha})_{*}(\mathcal{F}|U_{\alpha}). (5.9.1.1) $$

This $\mathcal{O}_{X}$-Module does not depend on the increasing family $(Z_{\alpha})$ of closed sets whose union is $Z$:
indeed, let $V$ be a Noetherian open set of $X$; one knows `(G, II, 3.10.1)` that in the category of
$\mathcal{O}_{V}$-Modules, the functor $\mathcal{F} \mapsto \Gamma(V, \mathcal{F})$ commutes with inductive limits;
hence by virtue of `(5.9.1.1)` one has

```text
  Γ(V, ℋ^0_{X/Z}(ℱ)) = lim→_α Γ(V ∩ U_α, ℱ).                        (5.9.1.2)
```

Let $(Z'_{\lambda})$ be a second increasing filtered family of closed sets of $X$ with union $Z$; $V \cap Z$ is then the
union of the $V \cap Z_{\alpha} \cap Z'_{\lambda}$; but $V \cap Z_{\alpha}$ is locally closed in $X$, hence every closed
irreducible part of $V \cap Z_{\alpha}$ admits a generic point; since the $V \cap Z_{\alpha} \cap Z'_{\lambda}$ are
closed in $V \cap Z_{\alpha}$ and form (for fixed $\alpha$) an increasing filtered family, there exists an index
$\lambda$ such that $V \cap Z_{\alpha} \cap Z'_{\lambda} = V \cap Z_{\alpha}$ $(0_{III}, 9.2.4)$, in other words $V \cap
Z_{\alpha} \subset V \cap Z'_{\lambda}$. This proves that the decreasing filtered families $V \cap U_{\alpha}$, $V \cap
U'_{\lambda}$ (where $U'_{\lambda} = X - Z'_{\lambda}$) are cofinal with one another, whence our assertion, by virtue of
`(5.9.1.2)`.

<!-- original page 110 -->

We note that the set $Z$ is not necessarily constructible: one has an example of this fact by taking $X =
\operatorname{Spec}(A)$, where $A$ is a Noetherian integral ring having an infinity of maximal ideals, and $Z$ the
complement of the generic point of $X$.

If $Z$ is closed and if $i : X - Z \to X$ is the canonical injection, one has

$$ \mathcal{H}^{0}_{X/Z}(\mathcal{F}) = i_{*}(\mathcal{F}|X - Z) (5.9.1.3) $$

and in particular, for $Z = \emptyset$, $\mathcal{H}^{0}_{X/Z}(\mathcal{F}) = \mathcal{F}$.

**Proposition (5.9.2).**

<!-- label: IV.5.9.2 -->

*(i) The functor $\mathcal{F} \mapsto \mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is left exact.*

*(ii) If $\mathcal{F}$ is quasi-coherent, so is $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$.*

Assertion (i) follows from the definition `(5.9.1.1)`, from the fact that $(i_{\alpha})_{*}$ is a left exact functor,
and from the fact that inductive limits preserve exactness in the category of $\mathcal{O}_{X}$-Modules. Assertion (ii)
follows from `(I, 9.2.2)` and from the fact that an inductive limit of quasi-coherent $\mathcal{O}_{X}$-Modules is
quasi-coherent `(I, 1.3.9)`.

**Remark (5.9.3).**

<!-- label: IV.5.9.3 -->

*If $\mathcal{F}$ is an $\mathcal{O}_{X}$-Algebra, so is $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ $(0_{I}, 4.2.4)$; in
particular $\mathcal{H}^{0}_{X/Z}(\mathcal{O}_{X})$ is a quasi-coherent $\mathcal{O}_{X}$-Algebra, and for every
$\mathcal{O}_{X}$-Module $\mathcal{F}$, $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is an
$\mathcal{H}^{0}_{X/Z}(\mathcal{O}_{X})$-Module which is quasi-coherent if $\mathcal{F}$ is quasi-coherent `(I, 9.6.1)`.
More particularly, suppose that $X = \operatorname{Spec}(A)$, where $A$ is integral and Noetherian; then
$\mathcal{H}^{0}_{X/Z}(\mathcal{O}_{X})$ is the $\mathcal{O}_{X}$-Algebra $\tilde{B}$, where*

```text
  B = ⋂_{𝔭 ∈ X − Z} A_𝔭.                                            (5.9.3.1)
```

This follows from `(5.9.1.2)` and from `(I, 8.2.1.1)`.

**Proposition (5.9.4).**

<!-- label: IV.5.9.4 -->

*Let $X$ be a locally Noetherian prescheme, $Z$ a part of $X$ stable under specialization, $X'$ a locally Noetherian
prescheme, $f : X' \to X$ a flat morphism. Then $Z' = f^{-1}(Z)$ is stable under specialization and for every
quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, one has a canonical isomorphism*

$$ f*(\mathcal{H}^{0}_{X/Z}(\mathcal{F})) \cong \mathcal{H}^{0}_{X'/Z'}(f*(\mathcal{F})). (5.9.4.1) $$

Indeed, with the notations of `(5.9.1)`, $Z'_{\alpha} = f^{-1}(Z_{\alpha})$ is closed in $X'$ and $Z'$ is the union of
the $Z'_{\alpha}$; in addition, $(i_{\alpha})_{(X')}$ is the canonical injection $i'_{\alpha} : U'_{\alpha} \to X'$, if
$U'_{\alpha} = X' - Z'_{\alpha} = f^{-1}(U_{\alpha})$. Since $f$ is flat, one knows `(2.3.1)` that the canonical
homomorphism $f*((i_{\alpha})_{*}(\mathcal{F}|U_{\alpha})) \to (i'_{\alpha})_{*}(f*(\mathcal{F})|U'_{\alpha})$ is
bijective; since, for $\alpha \leq \beta$, the diagram

<!-- original page 111 -->

$$ f*((i_{\alpha})_{*}(\mathcal{F}|U_{\alpha})) \xrightarrow{\sim} (i'_{\alpha})_{*}(f*(\mathcal{F})|U'_{\alpha})
\downarrow \downarrow f*((i_{\beta})_{*}(\mathcal{F}|U_{\beta})) \xrightarrow{\sim}
(i'_{\beta})_{*}(f*(\mathcal{F})|U'_{\beta}) $$

is commutative, one has, on passing to the limit, a canonical isomorphism $\lim\to_{\alpha}
(f*((i_{\alpha})_{*}(\mathcal{F}|U_{\alpha}))) \cong \mathcal{H}^{0}_{X'/Z'}(f*(\mathcal{F}))$. But since the functor
$f*$ commutes with inductive limits $(0_{I}, 4.3.2)$, this gives by definition the desired isomorphism `(5.9.4.1)`.

**Corollary (5.9.5).**

<!-- label: IV.5.9.5 -->

*Under the hypotheses of `(5.9.4)`, if $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is coherent, so is
$\mathcal{H}^{0}_{X'/Z'}(f*(\mathcal{F}))$. The converse is true when $f$ is a faithfully flat and quasi-compact
morphism.*

The first assertion follows from `(5.9.4.1)` and from $(0_{I}, 5.3.11)$; the second amounts to saying that if
$\mathcal{H}^{0}_{X'/Z'}(f*(\mathcal{F}))$ is of finite type, so is $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$; this follows
from `(5.9.4.1)` and from `(2.5.2)`.

**Corollary (5.9.6).**

<!-- label: IV.5.9.6 -->

*Let $X$ be a locally Noetherian prescheme, $Z$ a part of $X$ stable under specialization, $\mathcal{F}$ a
quasi-coherent $\mathcal{O}_{X}$-Module. For every $x \in X$, set $X_{x} = \operatorname{Spec}(\mathcal{O}_{x})$, $Z_{x}
= Z \cap X_{x}$; one has a canonical functorial isomorphism*

$$ (\mathcal{H}^{0}_{X/Z}(\mathcal{F}))_{x} \cong \mathcal{H}^{0}_{X_{x}/Z_{x}}(\tilde{\mathcal{F}}_{x}). (5.9.6.1) $$

It suffices to apply `(5.9.4)` to the canonical morphism $X_{x} \to X$, which is flat, and to take account of
`(I, 1.6.5)`.

**(5.9.7)**

<!-- label: IV.5.9.7 -->

With the notations of `(5.9.1)`, one has for every $\alpha$ a canonical functorial homomorphism $\mathcal{F} \to
(i_{\alpha})_{*}(\mathcal{F}|U_{\alpha})$ $(0_{I}, 4.4.3.2)$, and these homomorphisms form an inductive system; passing
to the inductive limit, one therefore deduces a canonical functorial homomorphism

$$ \rho_{X/Z} : \mathcal{F} \to \mathcal{H}^{0}_{X/Z}(\mathcal{F}). (5.9.7.1) $$

**Proposition (5.9.8).**

<!-- label: IV.5.9.8 -->

*Let $X$ be a locally Noetherian prescheme, $Z$ a part of $X$ stable under specialization, $\mathcal{F}$ an
$\mathcal{O}_{X}$-Module. The following properties are equivalent:*

*a) The homomorphism $\rho_{X/Z}$ `(5.9.7.1)` is injective (resp. bijective).*

*b) For every Noetherian open set $V$ of $X$, the homomorphism*

```text
  (ρ_{X/Z})_V : Γ(V, ℱ) → lim→_α Γ(V ∩ U_α, ℱ)
```

*is injective (resp. bijective).*

*a') For every closed part $T \subset Z$ of $X$, the canonical homomorphism \`(0_I, 4.4.3.2)*

$$ \mathcal{F} \to (i_{T})_{*}(\mathcal{F}|X - T) $$

*(where $i_{T} : X - T \to X$ is the canonical injection) is injective (resp. bijective).*

*b') For every closed part $T \subset Z$ of $X$ and every Noetherian open set $V$ of $X$, the restriction homomorphism*

```text
  Γ(V, ℱ) → Γ(V ∩ (X − T), ℱ)
```

*is injective (resp. bijective).*

Taking account of `(5.9.1.2)`, the equivalence of a) and b) (resp. a') and b')) follows from

<!-- original page 112 -->

the definition of the functor $\Gamma$ and the fact that it is left exact. Since the homomorphism $(\rho_{X/Z})_{V}$ is
the composite

```text
  Γ(V, ℱ) → Γ(V ∩ (X − T), ℱ) → lim→_α Γ(V ∩ U_α, ℱ)                (5.9.8.1)
```

for every closed part $T \subset Z$, if $(\rho_{X/Z})_{V}$ is injective, so is $\Gamma(V, \mathcal{F}) \to \Gamma(V \cap
(X - T), \mathcal{F})$; on the other hand, the fact that b') implies b) follows from the definition of an inductive
limit. It remains to show that if $\rho_{X/Z}$ is bijective, so is $\Gamma(V, \mathcal{F}) \to \Gamma(V \cap (X - T),
\mathcal{F})$, and for this it suffices, by virtue of `(5.9.8.1)`, to see that if $U' \subset U$ are two open sets
contained in $V$ and containing $V \cap Z$, the restriction homomorphism $\Gamma(U, \mathcal{F}) \to \Gamma(U',
\mathcal{F})$ is injective; but this follows from the fact that $\rho_{X/Z}$ is injective, by replacing $V$ by $U$ and
$V \cap (X - T)$ by $U'$ in what precedes.

**Definition (5.9.9).**

<!-- label: IV.5.9.9 -->

*Under the hypotheses of `(5.9.8)`, one says that $\mathcal{F}$ is **$Z$-pure** (resp. **$Z$-closed**) if the
homomorphism $\rho_{X/Z}$ is injective (resp. bijective).*

If $X = \operatorname{Spec}(A)$ is affine, $\mathcal{F} = \tilde{M}$ where $M$ is an $A$-module, one says that $M$ is
$Z$-pure (resp. $Z$-closed) when $\mathcal{F}$ is $Z$-pure (resp. $Z$-closed).

One says that $\mathcal{F}$ is $Z$-pure (resp. $Z$-closed) *at a point* $x \in X$ if (with the notations of `(5.9.6)`)
$\tilde{\mathcal{F}}_{x}$ is $Z_{x}$-pure (resp. $Z_{x}$-closed); equivalently, by virtue of `(5.9.6)`, the canonical
homomorphism $\mathcal{F}_{x} \to (\mathcal{H}^{0}_{X/Z}(\mathcal{F}))_{x}$ is injective (resp. bijective).

We note that for every $x \in X - Z$, $\mathcal{F}$ is $Z$-closed at the point $x$, by virtue of `(5.9.8)`.

**Corollary (5.9.10).**

<!-- label: IV.5.9.10 -->

*(i) Let $(V_{\lambda})$ be an open cover of $X$. For $\mathcal{F}$ to be $Z$-pure (resp. $Z$-closed), it is necessary
and sufficient that for every $\lambda$, $\mathcal{F}|V_{\lambda}$ be $(Z \cap V_{\lambda})$-pure (resp. $(Z \cap
V_{\lambda})$-closed).*

*(ii) Let $Z'$ be a part of $Z$ stable under specialization. If $\mathcal{F}$ is $Z$-pure (resp. $Z$-closed), it is
$Z'$-pure (resp. $Z'$-closed).*

This follows at once from `(5.9.8, b'))`.

**Proposition (5.9.11).**

<!-- label: IV.5.9.11 -->

*Under the hypotheses of `(5.9.8)`, the $\mathcal{O}_{X}$-Modules $Ker(\rho_{X/Z})$ and $Coker(\rho_{X/Z})$ have their
support contained in $Z$, and the $\mathcal{O}_{X}$-Module $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is $Z$-closed. Moreover,
if $u : \mathcal{F} \to \mathcal{F}'$ is a homomorphism of $\mathcal{O}_{X}$-Modules such that $\mathcal{F}'$ is
$Z$-closed, $u$ factors in a unique way as $\mathcal{F} \to^{\rho_{X/Z}} \mathcal{H}^{0}_{X/Z}(\mathcal{F}) \to^{v}
\mathcal{F}'$. If in addition the supports of $Ker(u)$ and $Coker(u)$ are contained in $Z$, $v$ is an isomorphism.*

The first assertion means that, for every $x \in X - Z$, one has

$$ Ker(\rho_{X/Z})_{x} = Coker(\rho_{X/Z})_{x} = 0, $$

i.e. that $(\rho_{X/Z})_{x}$ is bijective, or equivalently that $\mathcal{F}$ is $Z$-pure at $x$, as was noted above
`(5.9.9)`.

To show that $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is $Z$-closed, one has to see that for a Noetherian open $V$ of $X$,
$\lim\to_{\beta} \Gamma(V \cap U_{\beta}, \mathcal{H}^{0}_{X/Z}(\mathcal{F}))$ equals $\Gamma(V,
\mathcal{H}^{0}_{X/Z}(\mathcal{F}))$; but by definition $\Gamma(V \cap U_{\beta}, \mathcal{H}^{0}_{X/Z}(\mathcal{F})) =
\lim\to_{\alpha} \Gamma(V \cap U_{\alpha} \cap U_{\beta}, \mathcal{F})$. Now the double family $(U_{\alpha} \cap
U_{\beta})$ is filtered decreasing, and our assertion follows from `(5.9.1)` and from the theorem of the double
inductive limit.

<!-- original page 113 -->

Let us pass to the second part of the proposition. The existence and uniqueness of $v$ follow from the fact that for
every $\alpha$, $(i_{\alpha})_{*}(u)$ is the unique homomorphism making commutative the diagram

```text
  ℱ ────────u───────→ ℱ'
  ↓                    ↓
  (i_α)_*(ℱ|U_α) ─(i_α)_*(u)─→ (i_α)_*(ℱ'|U_α)
```

from the fact that there is a unique homomorphism $w$ making commutative all the diagrams

```text
  (i_α)_*(ℱ|U_α) ─(i_α)_*(u)─→ (i_α)_*(ℱ'|U_α)
        ↓                            ↓
  ℋ^0_{X/Z}(ℱ) ──────w────────→ ℋ^0_{X/Z}(ℱ')
```

and finally from the fact that $\mathcal{F}'$ and $\mathcal{H}^{0}_{X/Z}(\mathcal{F}')$ are canonically identified by
hypothesis.

It remains to see that if the supports of $Ker(u)$ and $Coker(u)$ are contained in $Z$, $v$ is an isomorphism. It
suffices to see that for every Noetherian open $V$, the corresponding homomorphism $\Gamma(V,
\mathcal{H}^{0}_{X/Z}(\mathcal{F})) \to \Gamma(V, \mathcal{F}')$ is then an isomorphism. Now, if a section $t \in
\Gamma(V, \mathcal{H}^{0}_{X/Z}(\mathcal{F}))$ has image `0` in $\Gamma(V, \mathcal{F}')$, note that for some index
$\alpha$, one has $t \in \Gamma(V \cap U_{\alpha}, \mathcal{F})$, and by virtue of the hypothesis on $u$, one has $t_{y}
= 0$ for every $y \in V \cap (X - Z)$; there is then an open set containing $V \cap (X - Z)$ such that the restriction
of $t$ to this open is zero, hence by definition $t$ is the element `0` of $\Gamma(V,
\mathcal{H}^{0}_{X/Z}(\mathcal{F}))$. Let us now prove that every section $s' \in \Gamma(V, \mathcal{F}')$ is the image
of a section of $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ over $V$. By hypothesis, for every $x \in V \cap (X - Z)$ there
exists a section $s^{(x)}$ of $\mathcal{F}$ over an open neighbourhood $W^{(x)}$ of $x$ in $X$, whose image by $u$ is
$s'|W^{(x)}$; $s'|W^{(x)}$ is therefore also the image by $v$ of the section $t^{(x)}$ of
$\mathcal{H}^{0}_{X/Z}(\mathcal{F})$, canonical image of $s^{(x)}$. In addition, since one has seen that $v$ is
injective, the restrictions of $t^{(x)}$ and $t^{(x')}$ to $W^{(x)} \cap W^{(x')}$ are identical for any two points $x$,
$x'$ of $V \cap (X - Z)$; the $t^{(x)}$ are therefore the restrictions of a single section $t$ of
$\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ over an open neighbourhood $U$ of $(X - Z) \cap V$. But since
$\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is $Z$-closed, $t$ extends in a unique way to a section of
$\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ over $V$, whose image by $v$ has the same restriction to $U$ as $s'$, hence
coincides with $s'$ for the same reason.

One says that $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is the **$Z$-closure** of $\mathcal{F}$.

<!-- original page 114 -->

**Remarks (5.9.12).**

<!-- label: IV.5.9.12 -->

*(i) Let $\mathcal{C}(X)$ be the category of $\mathcal{O}_{X}$-Modules, and let $\mathcal{C}_{Z}(X)$ be the subcategory
of $\mathcal{C}(X)$ formed by $\mathcal{O}_{X}$-Modules with support contained in $Z$; this subcategory is localizing in
the sense of Gabriel, and the functor $\mathcal{H}^{0}_{X/Z}$ is none other than the Gabriel localization functor (cf.
`[27]`; this would furnish another proof of `(5.9.11)`). When $Z$ is closed, the functor $i^{*} : \mathcal{C}(X) \to
\mathcal{C}(X - Z)$ (where $i : X - Z \to X$ is the canonical injection) defines an equivalence of categories
$\mathcal{C}(X)/\mathcal{C}_{Z}(X) \approx \mathcal{C}(X - Z)$.*

*(ii) It follows from `(5.9.11)` that the condition $\mathcal{H}^{0}_{X/Z}(\mathcal{F}) = 0$ is equivalent to
$Supp(\mathcal{F}) \subset Z$. It indeed entails the latter, since the kernel of $\rho_{X/Z}$ is then equal to
$\mathcal{F}$. Conversely, if $Supp(\mathcal{F}) \subset Z$, it suffices to apply the second part of `(5.9.11)` to the
unique homomorphism $u : \mathcal{F} \to 0$ to conclude that the corresponding homomorphism $v :
\mathcal{H}^{0}_{X/Z}(\mathcal{F}) \to 0$ is an isomorphism.*

*(iii) The preceding developments keep a sense for every locally Noetherian ringed space such that every closed
irreducible part admits exactly one generic point. In particular, they apply, on a locally Noetherian prescheme, to
arbitrary sheaves of abelian groups (considered as Modules over the simple sheaf associated with the constant presheaf
$\mathbb{Z}$). One still has, for every $x \in X$, the canonical isomorphism `(5.9.6.1)`, in which $\tilde{\mathcal{F}}$
denotes the sheaf induced on the subspace $X_{x}$ of $X$ by the sheaf $\mathcal{F}$; the direct proof follows at once
from the definition `(5.9.1.2)` and from the theorem of the double inductive limit.*

### 5.10. Property `(S_2)` and $Z$-closure

**(5.10.1)**

<!-- label: IV.5.10.1 -->

Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module; for every part $T$ of $X$,
we shall set

```text
  prof_T(ℱ) = inf_{x ∈ T} prof(ℱ_x).                                (5.10.1.1)
```

**Proposition (5.10.2).**

<!-- label: IV.5.10.2 -->

*Let $X$ be a locally Noetherian prescheme, $Z$ a part of $X$ stable under specialization, $\mathcal{F}$ a
quasi-coherent $\mathcal{O}_{X}$-Module. The following conditions are equivalent:*

*a) $\mathcal{F}$ is $Z$-pure.*

*b) $Ass(\mathcal{F})$ does not meet $Z$.*

*If in addition $\mathcal{F}$ is coherent, these conditions are also equivalent to:*

*c) $prof_{Z}(\mathcal{F}) \geq 1$.*

To say that $\mathcal{F}$ is $Z$-pure means that for every Noetherian open $V$ of $X$, and every open $U \supset X - Z$,
the restriction homomorphism $\Gamma(V, \mathcal{F}) \to \Gamma(V \cap U, \mathcal{F})$ is injective `(5.9.8)`; but
according to `(3.1.8)` this is equivalent to $V \cap Ass(\mathcal{F}) \subset U$, whence the equivalence of a) and b).
Furthermore, to say that $x \in Ass(\mathcal{F})$ means that no element of $\mathfrak{m}_{x}$ is
$\mathcal{F}_{x}$-regular `(3.1.2)`, hence, when $\mathcal{F}$ is coherent, this can still be written
$prof(\mathcal{F}_{x}) = 0$; one deduces at once in this case the equivalence of b) and c).

**Corollary (5.10.3).**

<!-- label: IV.5.10.3 -->

*Let $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ be an exact sequence of quasi-coherent
$\mathcal{O}_{X}$-Modules. If $\mathcal{F}$ is $Z$-pure, so is $\mathcal{F}'$; conversely, if $\mathcal{F}'$ and
$\mathcal{F}''$ are $Z$-pure, so is $\mathcal{F}$.*

<!-- original page 115 -->

This follows from the form `(5.10.2, b))` of the condition for a quasi-coherent $\mathcal{O}_{X}$-Module to be $Z$-pure,
and from `(3.1.7)`.

**Corollary (5.10.4).**

<!-- label: IV.5.10.4 -->

*Suppose $\mathcal{F}$ is coherent. For $\mathcal{F}$ to be $Z$-pure at a point $x \in X$, it is necessary and
sufficient that $prof_{Z_{x}}(\tilde{\mathcal{F}}_{x}) \geq 1$ (with the notations of `(5.9.6)`).*

This follows at once from `(5.10.2)` and `(5.9.6)`.

**Theorem (5.10.5).**

<!-- label: IV.5.10.5 -->

*Let $X$ be a locally Noetherian prescheme, $Z$ a part of $X$ stable under specialization, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module. For $\mathcal{F}$ to be $Z$-closed, it is necessary and sufficient that one have
$prof_{Z}(\mathcal{F}) \geq 2$.*

By virtue of `(5.10.2)`, one may restrict to the case where $\mathcal{F}$ is $Z$-pure and
$prof_{Z}(\mathcal{F}) \geq 1$. Moreover, to say that $prof_{Z}(\mathcal{F}) \geq 2$ is equivalent to saying that for
every closed part $Z_{\alpha}$ of $Z$, $prof_{Z_{\alpha}}(\mathcal{F}) \geq 2$; and likewise, it follows from `(5.9.8)`
that to say that $\mathcal{F}$ is $Z$-closed is equivalent to saying that $\mathcal{F}$ is $Z_{\alpha}$-closed for every
$\alpha$. One may therefore already restrict to the case where $Z$ is closed. The question being local, it suffices, for
every $x \in Z$, to prove the theorem for $\mathcal{F}|U$, $U$ being an affine open neighbourhood of $x$, and one may
therefore restrict to the case where $X = U$ is affine. One knows then that $Ass(\mathcal{F})$ is finite `(3.1.6)`, and
since $Ass(\mathcal{F}) \subset X - Z$, there is a section $f$ of $\mathcal{O}_{X}$ over $X$ such that
$Ass(\mathcal{F}) \subset X_{f} \subset X - Z$ `(II, 4.5.4)`; one deduces that $f$ is $\mathcal{F}$-regular `(3.1.9)`
and that for every $y \in Z$, one has $f_{y} \in \mathfrak{m}_{y}$, hence
$prof(\mathcal{F}_{y}) = 1 + prof(\mathcal{F}_{y}/f_{y} \mathcal{F}_{y})$ `(0, 16.4.6)`. The condition
$prof_{Z}(\mathcal{F}) \geq 2$ is thus equivalent to $prof_{Z}(\mathcal{F}/f\mathcal{F}) \geq 1$, or equivalently
`(5.10.2)` to the fact that $\mathcal{F}/f\mathcal{F}$ is $Z$-pure, and it suffices to see that this latter property is
equivalent to the fact that $\mathcal{F}$ is $Z$-closed.

Consider the exact sequence $0 \to \mathcal{F} \to^{f} \mathcal{F} \to \mathcal{F}/f\mathcal{F} \to 0$ (the homothety of
ratio $f : \mathcal{F} \to \mathcal{F}$ being by hypothesis injective); setting $W = X - Z$, one has the commutative
diagram

```text
  0 → Γ(X, ℱ) →^f Γ(X, ℱ) → Γ(X, ℱ/fℱ) → 0
        ↓             ↓             ↓
  0 → Γ(W, ℱ) →^f Γ(W, ℱ) → Γ(W, ℱ/fℱ)
```

whose two rows are exact ($X$ being affine). If the restriction homomorphism $\Gamma(X, \mathcal{F}) \to \Gamma(W,
\mathcal{F})$ is bijective, one deduces from this diagram that

```text
  Γ(X, ℱ/fℱ) → Γ(W, ℱ/fℱ)
```

is injective, and this shows `(5.9.8)` that if $\mathcal{F}$ is $Z$-closed, $\mathcal{F}/f\mathcal{F}$ is $Z$-pure.
Conversely, suppose that $\mathcal{F}/f\mathcal{F}$ is $Z$-pure, and let $s$ be a section of $\mathcal{F}$ over $W$;
since $X_{f} \subset W$, there exists an integer $n > 0$ such that $f^{n}(s|X_{f})$ extends to a section $t$ of
$\mathcal{F}$ over $X$ `(I, 1.4.1)`; furthermore, the restrictions of $t$ and $f^{n} s$ to $X_{f}$ being the same, it
follows that the restriction of $t$ to $W$ equals $f^{n} s$ by virtue of the relation $Ass(\mathcal{F}) \subset X_{f}$
`(5.10.2)`; since $f$ is $\mathcal{F}$-regular, it will suffice to see that $t$ is of the form $f^{n} t'$, where $t' \in
\Gamma(X, \mathcal{F})$,

<!-- original page 116 -->

to show that the homomorphism $\Gamma(X, \mathcal{F}) \to \Gamma(W, \mathcal{F})$ is surjective, hence bijective. Now to
say that $t = f^{n} t'$ means that the image of $t$ in $\Gamma(X, \mathcal{F}/f^{n} \mathcal{F})$ is zero. But since
$f^{k} \mathcal{F}/f^{k+1} \mathcal{F}$ is isomorphic to $\mathcal{F}/f\mathcal{F}$, hence $Z$-pure by hypothesis, one
deduces from `(5.10.3)`, by induction on $n$, that $\mathcal{F}/f^{n} \mathcal{F}$ is $Z$-pure. But by definition the
image of $t|W = f^{n} s$ in $\Gamma(W, \mathcal{F}/f^{n} \mathcal{F})$ is zero, whence the conclusion.

**Corollary (5.10.6).**

<!-- label: IV.5.10.6 -->

*Let $\mathcal{F}$ be a coherent $\mathcal{O}_{X}$-Module. For $\mathcal{F}$ to be $Z$-closed at a point $x$, it is
necessary and sufficient that $prof_{Z_{x}}(\tilde{\mathcal{F}}_{x}) \geq 2$.*

This follows from `(5.9.6)` and `(5.10.5)`.

**Theorem (5.10.7) (Hartshorne).**

<!-- label: IV.5.10.7 -->

*Let $X$ be a locally Noetherian prescheme, $Y$ a closed part of $X$. Suppose that for every $y \in Y$, one has
$prof(\mathcal{O}_{X,y}) \geq 2$; then for every connected component $C$ of $X$, $C - (C \cap Y)$ is connected.*

One may restrict to the case where $X$ is connected; it then follows from `(5.10.5)` that the canonical homomorphism
$\mathcal{O}_{X} \to i_{*}(\mathcal{O}_{X}|X - Y)$ (where $i : X - Y \to X$ is the canonical injection) is bijective.
Consequently the restriction homomorphism $\Gamma(X, \mathcal{O}_{X}) \to \Gamma(X - Y, \mathcal{O}_{X})$ is also
bijective. It suffices now to apply Lemma `(III, 7.8.6.1)`.

**Corollary (5.10.8).**

<!-- label: IV.5.10.8 -->

*Let $X$ be a locally Noetherian prescheme, $d$ an integer such that for every $x \in X$, the relation
$\dim(\mathcal{O}_{x}) \geq d$ entails $prof(\mathcal{O}_{x}) \geq 2$. Suppose $X$ connected; then, if $X'$, `X''` are
two distinct irreducible components of $X$, there exists a sequence $(X_{i})_{0 \leq i \leq n}$ of irreducible
components of $X$ such that $X_{0} = X'$, $X_{n} = X''$, and that, for $1 \leq i \leq n$, one has $codim(X_{i-1} \cap
X_{i}, X) \leq d - 1$ (one then says that $X$ is **connected in codimension $\leq d - 1$**).*

If $Y$ is a closed part of $X$ such that $codim(Y, X) \geq d$, one has $\dim(\mathcal{O}_{X,y}) \geq d$ for every $y \in
Y$ `(5.1.3)`, hence $prof(\mathcal{O}_{X,y}) \geq 2$ for every $y \in Y$, and it follows from `(5.10.7)` that $X - Y$ is
connected. On the other hand, for $codim(Y, X) \geq d$, it is necessary and sufficient that for every $y \in Y$, there
exist an open neighbourhood $V$ of $y$ in $X$ such that $codim(Y \cap V, V) \geq d$ `(0, 14.2.3)`. Note finally that if
$\mathfrak{F}$ denotes the set of closed parts $Y$ of $X$ of codimension $\geq d$, the union of two sets of
$\mathfrak{F}$ belongs to $\mathfrak{F}$ `(0, 14.2.5)`, and every closed set contained in a set of $\mathfrak{F}$
belongs to $\mathfrak{F}$, properties which one also expresses by saying that $\mathfrak{F}$ is an **antifilter** of
closed parts of $X$. The corollary then follows from the following topological lemma:

**Lemma (5.10.8.1).**

<!-- label: IV.5.10.8.1 -->

*Let $X$ be a connected locally Noetherian topological space, $\mathfrak{F}$ an antifilter of closed parts of $X$. One
assumes that if $Y$ is a closed part of $X$ such that for every $y \in Y$, there exist an open neighbourhood $V$ of $y$
in $X$ and a $Y_{y} \in \mathfrak{F}$ such that $V \cap Y = V \cap Y_{y}$, then $Y \in \mathfrak{F}$. The following
conditions are then equivalent:*

*a) For every $Y \in \mathfrak{F}$, $X - Y$ is connected.*

*b) If $X'$ and `X''` are two distinct irreducible components of $X$, there exists a sequence $(X_{i})_{0 \leq i \leq
n}$ of irreducible components of $X$ such that $X_{0} = X'$, $X_{n} = X''$ and that, for $1 \leq i \leq n$, one has
$X_{i-1} \cap X_{i} \notin \mathfrak{F}$.*

Suppose b) is verified and let us prove that $U = X - Y$ is connected for every $Y \in \mathfrak{F}$. If $U'$ and `U''`
are two distinct irreducible components of $U$, there exist two irreducible components $X'$, `X''` of $X$ such that $X'
\cap U = U'$, $X'' \cap U = U''$ $(0_{I}, 2.1.6)$;

<!-- original page 117 -->

let us form for these two components a sequence $(X_{i})$ having the property stated in b) and set $U_{i} = X_{i} \cap
U$ for $1 \leq i \leq n$; then $U_{i}$ is an irreducible component of $U$ $(0_{I}, 2.1.6)$ and moreover $U_{i} \cap
U_{i-1} \neq \emptyset$ for $1 \leq i \leq n$, otherwise one would have $X_{i} \cap X_{i-1} \subset Y$, hence $X_{i}
\cap X_{i-1} \in \mathfrak{F}$, contrary to the definition of the $X_{i}$. This entails that $U$ is connected.

Let us now show that a) entails b). Denote by $Y$ the union of the family $(X_{\alpha} \cap X_{\beta})$, where
$(X_{\alpha}, X_{\beta})$ runs through the set of pairs of distinct irreducible components of $X$ such that $X_{\alpha}
\cap X_{\beta} \in \mathfrak{F}$. For every point $y \in Y$, there is an open neighbourhood $V$ of $y$ in $X$ meeting
only a finite number of irreducible components of $X$; this shows on the one hand that $Y$ is closed and on the other
hand that $V \cap Y$ is the intersection of $V$ with a set of $\mathfrak{F}$; by virtue of the hypothesis made on
$\mathfrak{F}$, one has $Y \in \mathfrak{F}$, hence $U = X - Y$ is connected; in addition $Y$ is rare in $X$. Let then
$X'$, `X''` be two distinct irreducible components of $X$, $U'$, `U''` their respective traces on $U$; these are
distinct irreducible components of $U$ $(0_{I}, 2.1.6)$. Now the union of the irreducible components $W$ of $U$ for
which there exists a sequence $(U_{i})_{0 \leq i \leq n}$ of irreducible components of $U$ such that $U_{0} = U'$,
$U_{i-1} \neq U_{i}$ and $U_{i-1} \cap U_{i} \neq \emptyset$ for $1 \leq i \leq n$ and $U_{n} = W$, is an open and
closed set in $U$, since $U$ is locally Noetherian and consequently its irreducible components form a locally finite
family of closed sets. There is therefore such a sequence $(U_{i})$ for which $U_{n} = U''$; let $X_{i}$ $(0 \leq i \leq
n)$ be the irreducible component of $X$ such that $X_{i} \cap U = U_{i}$ $(0_{I}, 2.1.6)$; since $U_{i-1} \neq U_{i}$,
one has $X_{i-1} \neq X_{i}$ for $1 \leq i \leq n$; if one had $X_{i-1} \cap X_{i} \in \mathfrak{F}$ for some $i$ such
that $1 \leq i \leq n$, one would deduce $X_{i-1} \cap X_{i} \subset Y$ by definition of $Y$, whence $U_{i-1} \cap U_{i}
= \emptyset$, contrary to the hypothesis. This completes the proof of the lemma.

One will note that the hypothesis made on $X$ in `(5.10.8)` is verified when $X$ is a Cohen-Macaulay prescheme and $d
\geq 2$.

**Corollary (5.10.9).**

<!-- label: IV.5.10.9 -->

*If a Noetherian local ring $A$ verifies `(S_2)` and is catenary, it is equidimensional.*

The hypothesis of `(5.10.8)` is then verified by $X = \operatorname{Spec}(A)$, with $d = 2$. To show that all the
irreducible components of $X$ have the same dimension, it suffices then, by virtue of `(5.10.8)`, to show that two such
components $X'$, `X''` have the same dimension when one assumes in addition that $codim(X' \cap X'', X) = 1$. There is
then an irreducible component $Z$ of $X' \cap X''$ such that $codim(Z, X) = 1$, hence $codim(Z, X') = 1$, since
$codim(Z, X) \geq codim(Z, X') \geq 1$; likewise $codim(Z, X'') = 1$, and since $X$ is catenary, this entails $\dim(X')
= \dim(X'')$.

**Proposition (5.10.10).**

<!-- label: IV.5.10.10 -->

*Let $X$ be a locally Noetherian prescheme, $Z$ a part of $X$ stable under specialization, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module, and suppose that the $\mathcal{O}_{X}$-Module $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is
coherent. Then:*

*(i) One has $prof_{Z}(\mathcal{H}^{0}_{X/Z}(\mathcal{F})) \geq 2$.*

*(ii) For every point $x \in Ass(\mathcal{F}) \cap (X - Z)$, one has $codim(Z \cap \overline{x}, \overline{x}) \geq 2$.*

*(iii) The set $U$ of $x \in X$ such that $prof_{Z_{x}}(\tilde{\mathcal{F}}_{x}) \geq 2$ (notations of `(5.9.6)`) is
open in $X$; one has $X - U \subset Z$, and $U$ is the largest open set of $X$ such that $\mathcal{F}|U$ be $(Z \cap
U)$-closed.*

<!-- original page 118 -->

For brevity set $\mathcal{F}' = \mathcal{H}^{0}_{X/Z}(\mathcal{F})$. One knows `(5.9.11)` that $\mathcal{F}'$ is
$Z$-closed and assertion (i) follows therefore from `(5.10.5)` applied to $\mathcal{F}'$. Let $x \in Ass(\mathcal{F})
\cap (X - Z)$; since the restrictions of $\mathcal{F}$ and $\mathcal{F}'$ to $X - Z$ are canonically isomorphic
`(5.9.11)`, one has $x \in Ass(\mathcal{F}')$. Consider a point $y \in Z \cap \overline{x}$; the prime ideal
$\mathfrak{p}$ of $\mathcal{O}_{y}$ corresponding to $x$ is associated with the $\mathcal{O}_{y}$-module
$\mathcal{F}'_{y}$, hence one has, by virtue of (i) and of `(0, 16.4.6.2)`,
`2 ≤ prof(ℱ'_y) ≤ dim(𝒪_y/𝔭) = codim(‾{y}, ‾{x})`, whence (ii). Finally, to prove (iii), note that $U$ is the set of $x
\in X$ such that $\tilde{\mathcal{F}}_{x}$ is $Z_{x}$-closed `(5.10.5)`, or equivalently, by virtue of `(5.9.6)`, the
set of points where the canonical homomorphism $\mathcal{F}_{x} \to \mathcal{F}'_{x}$ is bijective; it is therefore the
complement of the union of the supports of $Ker(\rho_{X/Z})$ and $Coker(\rho_{X/Z})$, and these latter are coherent
$\mathcal{O}_{X}$-Modules by virtue of the hypothesis $(0_{I}, 5.3.4)$, hence have closed support $(0_{I}, 5.2.2)$; this
shows that $U$ is open, and $U$ is obviously the largest open such that $\mathcal{F}|U$ be $(Z \cap U)$-closed; finally
the inclusion $X - U \subset Z$ follows from `(5.9.11)`.

We shall see later `(5.11.1)` that in the most important cases assertion (ii) conversely entails that
$\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is coherent.

**(5.10.11)**

<!-- label: IV.5.10.11 -->

Let $X$ be a locally Noetherian prescheme, $Z$ a part of $X$ stable under specialization; one has seen that $\mathcal{A}
= \mathcal{H}^{0}_{X/Z}(\mathcal{O}_{X})$ is a quasi-coherent $\mathcal{O}_{X}$-Algebra `(5.9.3)`; the $X$-scheme $X' =
\operatorname{Spec}(\mathcal{H}^{0}_{X/Z}(\mathcal{O}_{X}))$ `(II, 1.3.1)` is called the **$Z$-closure** of $X$.
Moreover for every $\mathcal{O}_{X}$-Module $\mathcal{F}$, $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is an
$\mathcal{A}$-Module, which is quasi-coherent if $\mathcal{F}$ is a quasi-coherent $\mathcal{O}_{X}$-Module; in this
latter case there is therefore a unique $\mathcal{O}_{X'}$-Module $\mathcal{F}'$ such that one has, denoting by $g : X'
\to X$ the structure morphism `(II, 1.4.3)`,

$$ \mathcal{H}^{0}_{X/Z}(\mathcal{F}) = g_{*}(\mathcal{F}'). (5.10.11.1) $$

**Proposition (5.10.12).**

<!-- label: IV.5.10.12 -->

*Notations being those of `(5.10.11)`:*

*(i) Let $x$ be a point of $X$. For the morphism*

```text
  X' ×_X X_x → X_x   (= Spec(𝒪_{X,x}))
```

*deduced from $g$ by localization to be an isomorphism, it is necessary and sufficient that $\mathcal{O}_{x}$ be
$Z$-closed at the point $x$ (which is the case for every $x \in X - Z$).*

*(ii) Set $Z' = g^{-1}(Z)$, and suppose $X'$ locally Noetherian. Then $\mathcal{F}'$ is $Z'$-closed; if in addition
$\mathcal{F}'$ is a coherent $\mathcal{O}_{X'}$-Module, one has $prof_{Z'}(\mathcal{F}') \geq 2$.*

*(iii) Suppose that $\mathcal{H}^{0}_{X/Z}(\mathcal{O}_{X})$ and $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ are coherent. Then
the morphism $g : X' \to X$ is finite; the set $U$ of $x \in X$ such that one has $prof_{Z_{x}}(\tilde{\mathcal{O}}_{x})
\geq 2$ and $prof_{Z_{x}}(\tilde{\mathcal{F}}_{x}) \geq 2$ is open in $X$ and such that $X - U \subset Z$; in addition
$U$ is the largest open set of $X$ such that the restriction $g^{-1}(U) \to U$ of $g$ is an isomorphism and that the
restriction $\mathcal{F}|U \to \mathcal{F}'|g^{-1}(U)$ of the canonical $g$-morphism $\mathcal{F} \to \mathcal{F}'$ is
an isomorphism.*

Assertion (i) follows from the definitions, and (iii) is an immediate consequence of `(5.10.10, (iii))`. To prove (ii),
consider an open $V$ of $X$ containing $X - Z$

<!-- original page 119 -->

and its inverse image $V' = g^{-1}(V)$; if $i : V \to X$ and $i' : V' \to X'$ are the canonical injections, the
canonical homomorphism $\rho_{X'/Z'} : \mathcal{F}' \to i'_{*}(\mathcal{F}'|V')$ is such that $g_{*}(\rho_{X'/Z'})$ is
the canonical homomorphism $\rho_{X/Z} : \mathcal{H}^{0}_{X/Z}(\mathcal{F}) \to
i_{*}(\mathcal{H}^{0}_{X/Z}(\mathcal{F})|V)$ `(II, 1.4.2)`, taking account of `(5.10.11.1)`. Since
$\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is $Z$-closed `(5.9.11)`, $\rho_{X/Z}$ is an isomorphism, hence so is
$\rho_{X'/Z'}$. Since $X' - Z'$ is the intersection of the filtered family of $V'_{\alpha} = g^{-1}(V_{\alpha})$, where
$V_{\alpha}$ runs through the filtered family of open sets containing $X - Z$, one deduces that $\mathcal{F}'$ is
$Z'$-closed when $X'$ is locally Noetherian, by virtue of `(5.9.1)`.

**(5.10.13)**

<!-- label: IV.5.10.13 -->

We shall now apply the preceding results to the case where $Z$ is one of the sets $Z^{(n)}(X)$ (or simply $Z^{(n)}$),
defined as the set of $x \in X$ such that $\dim(\mathcal{O}_{x}) \geq n$; it is clear that $Z^{(n)}$ is stable under
specialization; for a closed part $T$ of $X$ to be contained in $Z^{(n)}$, it is necessary and sufficient that $codim(T,
X) \geq n$. We shall be interested here in the case $n = 2$.

**Proposition (5.10.14).**

<!-- label: IV.5.10.14 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module of support equal to $X$.*

*(i) For $\mathcal{F}$ to verify `(S_1)`, it is necessary and sufficient that it be $Z^{(1)}$-pure.*

*(ii) For $\mathcal{F}$ to verify `(S_2)`, it is necessary and sufficient that it be $Z^{(2)}$-closed and
$Z^{(1)}$-pure, or equivalently that it be $Z^{(2)}$-closed and have no associated prime cycle of codimension `1`.*

(i) To say that $\mathcal{F}$ possesses property `(S_1)` means that $\mathcal{F}$ has no embedded associated prime cycle
`(5.7.5)`, or equivalently that for every $x \in Ass(\mathcal{F})$, one has $\dim(\mathcal{F}_{x}) = 0$ `(3.1.4)`, in
other words `(5.1.12.1)` $\dim(\mathcal{O}_{x}) = 0$; but this is equivalent to saying that $Ass(\mathcal{F})$ does not
meet $Z^{(1)}$, and the conclusion follows from `(5.10.2)`.

(ii) To say that $\mathcal{F}$ is $Z^{(2)}$-closed means that $prof_{Z^{(2)}}(\mathcal{F}) \geq 2$, or equivalently
that, for every $x \in X$, the relation $\dim(\mathcal{O}_{x}) \geq 2$ entails $prof(\mathcal{F}_{x}) \geq 2$; this
shows that property `(S_2)` entails that $\mathcal{F}$ is $Z^{(2)}$-closed; it entails in addition that $\mathcal{F}$
verifies `(S_1)`, hence has no embedded associated prime cycle `(5.7.5)`, and since $Supp(\mathcal{F}) = X$, this still
means that all the associated prime cycles of $\mathcal{F}$ are of codimension `0`. Conversely, suppose that
$\mathcal{F}$ is $Z^{(2)}$-closed and has no associated prime cycle of codimension `1`; to see that $\mathcal{F}$
verifies `(S_2)`, it remains to show that if $x \in X$ is such that $\dim(\mathcal{O}_{x}) = 1$ (or, what amounts to the
same, $\dim(\mathcal{F}_{x}) = 1$), then one has $prof(\mathcal{F}_{x}) = 1$; but by hypothesis the relation
$\dim(\mathcal{O}_{x}) = 1$ entails $x \notin Ass(\mathcal{F})$, and this last relation is equivalent to
$prof(\mathcal{F}_{x}) \neq 0$, that is, here, to $prof(\mathcal{F}_{x}) = 1$. If $\mathcal{F}$ is $Z^{(1)}$-pure, hence
verifies `(S_1)`, one has noted above that by virtue of the relation $Supp(\mathcal{F}) = X$, all the associated prime
cycles of $\mathcal{F}$ are of codimension `0`, hence what precedes applies.

One will note that it can happen that $\mathcal{F}$ is $Z^{(2)}$-closed and does not verify `(S_1)`: this is the case
for example when $X$ is of dimension `1` (for then $Z^{(2)} = \emptyset$, and every $\mathcal{O}_{X}$-Module is
$Z^{(2)}$-closed) and has embedded associated prime cycles.

Let us recall that in Chapter III, in the study of local cohomology, one gives a cohomological characterization of
property $(S_{n})$ for every $n \geq 1$, generalizing `(5.10.14)`.

**Corollary (5.10.15).**

<!-- label: IV.5.10.15 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module of support $X$. Assume
that $\mathcal{F}$ has no associated prime cycles of codimension `1` and that $\mathcal{F}' =
\mathcal{H}^{0}_{X/Z^{(2)}}(\mathcal{F})$ is coherent. Then:*

*(i) $\mathcal{F}'$ verifies property `(S_2)`.*

<!-- original page 120 -->

*(ii) The set $U$ of $x \in X$ such that $\mathcal{F}$ verifies `(S_2)` at the point $x$ `(5.7.2)` is open in $X$, and
one has $codim(X - U, X) \geq 2$.*

(i) One knows `(5.9.11)` that $\mathcal{F}'$ is $Z^{(2)}$-closed, and moreover $Supp(\mathcal{F}') = X$, since the
maximal points of $X$ belong to $X - Z^{(2)}$ and at these points $\mathcal{F}'_{x} = \mathcal{F}_{x} \neq 0$, hence the
support of $\mathcal{F}'$ is dense in $X$, and since $\mathcal{F}'$ is coherent, $Supp(\mathcal{F}')$ is closed, hence
equal to $X$. It remains to see that $\mathcal{F}'$ has no associated prime cycle of codimension `1`. But if $x \in
Ass(\mathcal{F}')$ and $\dim(\mathcal{F}'_{x}) = \dim(\mathcal{O}_{x}) = 1$, one has $x \in X - Z^{(2)}$, hence, since
$\mathcal{F}'_{x} = \mathcal{F}_{x}$, one would have $x \in Ass(\mathcal{F})$, contrary to the hypothesis, which
completes the proof of (i).

(ii) One has $Z^{(n)}(X_{x}) = Z^{(n)}(X) \cap X_{x}$, with the notations of `(5.9.6)`, taking account of `(I, 2.4.2)`;
on the other hand, the hypothesis that $\mathcal{F}$ has no associated prime cycles of codimension `1` entails the same
hypothesis for $\tilde{\mathcal{F}}_{x}$; for $\tilde{\mathcal{F}}_{x}$ to verify `(S_2)`, it is therefore necessary and
sufficient, by virtue of `(5.10.14)`, that $\tilde{\mathcal{F}}_{x}$ be $Z^{(2)}(X_{x})$-closed; assertion (ii)
therefore follows from `(5.10.6)` and `(5.10.10, (iii))`.

**Proposition (5.10.16).**

<!-- label: IV.5.10.16 -->

*Let $X$ be a locally Noetherian prescheme,*

$$ X' = \operatorname{Spec}(\mathcal{H}^{0}_{X/Z^{(2)}}(\mathcal{O}_{X})) $$

*its $Z^{(2)}$-closure, $g : X' \to X$ the structure morphism. Suppose that $X$ has no associated prime cycle of
codimension `1`.*

*(i) For $X$ to verify `(S_2)` at a point $x \in X$, it is necessary and sufficient that the morphism $X'_{x} \to X_{x}$
deduced from $g$ (notations of `(5.10.12)`) be an isomorphism. This condition is always verified if $codim(\overline{x},
X) \leq 1$.*

*(ii) Suppose moreover that $g$ is a finite morphism (see in `(5.11.2)` sufficient conditions for this to be so). Then
the set $U$ of points where $X$ verifies `(S_2)` is open and $codim(X - U, X) \geq 2$; in addition $U$ is the largest
open set of $X$ such that the restriction $g^{-1}(U) \to U$ of $g$ is an isomorphism.*

*(iii) Under the same hypotheses as in (ii), $X'$ satisfies `(S_2)` and for every $x' \in X'$ such that
$codim(\overline{x'}, X') \leq 1$, the point $x = g(x')$ is such that $codim(\overline{x}, X) = codim(\overline{x'},
X')$.*

*(iv) The hypotheses being those of (ii), let $\mathcal{F}$ be a coherent $\mathcal{O}_{X}$-Module of support $X$ such
that $\mathcal{H}^{0}_{X/Z^{(2)}}(\mathcal{F})$ is coherent; then the $\mathcal{O}_{X'}$-Module $\mathcal{F}'$ such that
$g_{*}(\mathcal{F}') = \mathcal{H}^{0}_{X/Z^{(2)}}(\mathcal{F})$ is coherent and verifies `(S_2)`, and its support is a
union of irreducible components of $X'$.*

Assertions (i) and (ii) are inserted for memory, having already been proved in substance: (i) follows indeed from
`(5.10.12, (i))` and `(5.10.14)`, and (ii) is a special case of `(5.10.15, (ii))`.

Let us prove (iii); set $x = g(x')$; since $g$ is finite, so is the morphism $X'_{x} \to X_{x}$, hence
`dim(𝒪_{X',x'}) ≤ dim(X'_x) ≤ dim(X_x) = dim(𝒪_{X,x})` by virtue of `(5.4.1)`. Suppose first that
$\dim(\mathcal{O}_{X',x'}) \leq 1$ and let us show that then $\dim(\mathcal{O}_{X,x}) \leq 1$. Otherwise, one would have
$x \in Z^{(2)}$, hence by virtue of `(5.10.12, (ii))` applied to $\mathcal{O}_{X}$ one would have
$prof(\mathcal{O}_{X',x'}) \geq 2$, which is absurd. One has therefore $x \in X - Z^{(2)}$, and consequently
$\mathcal{O}_{X',x'}$ is isomorphic to $\mathcal{O}_{X,x}$ `(5.10.12, (i))`, whence $\dim(\mathcal{O}_{X',x'}) =
\dim(\mathcal{O}_{X,x})$. In addition, since $X$ has no associated prime cycles

<!-- original page 121 -->

of codimension `1`, the hypothesis $\dim(\mathcal{O}_{X,x}) = 1$ entails $x \notin Ass(\mathcal{O}_{X})$, hence
$prof(\mathcal{O}_{X,x}) = 1$, and consequently also $prof(\mathcal{O}_{X',x'}) = 1$. Suppose now
$\dim(\mathcal{O}_{X',x'}) \geq 2$, hence $\dim(\mathcal{O}_{X,x}) \geq 2$, that is, $x \in Z^{(2)}$; one deduces that
$prof(\mathcal{O}_{X',x'}) \geq 2$ by `(5.10.12, (ii))`. This establishes the assertions of (iii).

To prove (iv) it suffices to replace $\mathcal{O}_{X}$ by $\mathcal{F}$ in the preceding reasoning, which establishes
that $\mathcal{F}'$ verifies `(S_2)` and that if $\dim(\mathcal{F}_{x}) \leq 1$, $\mathcal{F}_{x}$ and
$\mathcal{F}'_{x'}$ are di-isomorphic; in particular if $\dim(\mathcal{F}_{x}) = 0$, one has $\dim(\mathcal{F}'_{x'}) =
0$, hence $\dim(\mathcal{O}_{X,x}) = 0$ since $\mathcal{F}$ has support $X$, and finally $\dim(\mathcal{O}_{X',x'}) =
0$; every irreducible component of $Supp(\mathcal{F}')$ is therefore an irreducible component of $X'$, since
$\mathcal{F}'$ is coherent, hence $Supp(\mathcal{F}')$ closed.

**Proposition (5.10.17).**

<!-- label: IV.5.10.17 -->

*Let $A$ be a Noetherian integral ring, and denote by $A^{(1)}$ the intersection of the local rings $A_{\mathfrak{p}}$,
where $\mathfrak{p}$ runs through the set of prime ideals of $A$ of height `1`. Suppose that $A^{(1)}$ is a finite
$A$-algebra. Then:*

*(i) The ring $A^{(1)}$ verifies condition `(S_2)`.*

*(ii) The set $U$ of $\mathfrak{p} \in \operatorname{Spec}(A)$ such that the canonical homomorphism $A_{\mathfrak{p}}
\to (A^{(1)})_{\mathfrak{p}}$ is bijective is equal to the set of $\mathfrak{p}$ such that $A_{\mathfrak{p}}$ verifies
`(S_2)`; $U$ is open in $X = \operatorname{Spec}(A)$ and one has $codim(X - U, X) \geq 2$.*

*(iii) For every multiplicative part $S$ of $A$, $(S^{-1}A)^{(1)}$ is a finite $(S^{-1}A)$-algebra.*

*(iv) Let $B$ be a finite $A$-algebra, integral and containing $A$. Then $B^{(1)}$ is a finite $B$-algebra. Moreover,
for every prime ideal $\mathfrak{q}$ of $B$, of height `1`, the prime ideal $\mathfrak{q} \cap A$ of $A$ is of height
`1`.*

If one takes account of formula `(5.9.3.1)`, one sees that $X' = \operatorname{Spec}(A^{(1)})$ is the $Z^{(2)}$-closure
of $X = \operatorname{Spec}(A)$; since $A$ has no embedded associated prime ideals, properties (i) and (ii) are special
cases of `(5.10.16, (i), (ii) and (iii))`. To prove (iii), it suffices to remark that one has $(S^{-1}A)^{(1)} =
S^{-1}A^{(1)}$, which is a special case of `(5.9.4)`: indeed $S^{-1}A$ is a flat $A$-module, the prime ideals of
$S^{-1}A$ are the ideals $S^{-1}\mathfrak{p}$, where $\mathfrak{p} \in \operatorname{Spec}(A)$ does not meet $S$, and
one has $ht(S^{-1}\mathfrak{p}) = ht(\mathfrak{p})$. Since $A^{(1)}$ is a finite $A$-algebra, $S^{-1}A^{(1)}$ is a
finite $S^{-1}A$-algebra, whence (iii).

To prove (iv), set $Y = \operatorname{Spec}(B)$, and let $f : Y \to X$ be the structure morphism; since it is finite, it
follows from `(5.4.1)` that for every $y \in Y$, one has $\dim(\mathcal{O}_{Y,y}) \leq \dim(\mathcal{O}_{X,f(y)})$;
hence, if $T = f^{-1}(Z^{(2)}(X))$, one has $T \supset Z^{(2)}(Y)$. Let us show that $\mathcal{G} =
\mathcal{H}^{0}_{X/Z^{(2)}(X)}(f_{*}(\mathcal{O}_{Y}))$ is coherent; indeed $f_{*}(\mathcal{O}_{Y}) = \tilde{B}$, $B$
being considered as $A$-module; but since $B$ is a finite integral $A$-algebra, its field of fractions is finite over
the field of fractions of $A$, hence $B$ is contained in a free $A$-module of finite type, and consequently
`(5.9.2, (i))` $\mathcal{G}$ is a quasi-coherent $\mathcal{O}_{X}$-submodule of
$(\mathcal{H}^{0}_{X/Z^{(2)}(X)}(\mathcal{O}_{X}))^{n}$ for some suitable $n$; this latter being coherent by hypothesis,
so is $\mathcal{G}$. Now, it follows from the definition `(5.9.1.2)` that $\mathcal{G}$ is isomorphic to
$f_{*}(\mathcal{H}^{0}_{Y/T}(\mathcal{O}_{Y}))$; this proves a fortiori that $\mathcal{H}^{0}_{Y/T}(\mathcal{O}_{Y})$ is
a coherent $\mathcal{O}_{Y}$-Module. It then follows from `(5.10.10, (ii))`, applied to $\mathcal{O}_{Y}$ and to the
generic point of $Y$, that one has $codim(T, Y) \geq 2$, that is, $T \subset Z^{(2)}(Y)$, and finally $T = Z^{(2)}(Y)$.
This proves both assertions of (iv).

<!-- original page 122 -->

### 5.11. Coherence criteria for the Modules $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$

**Proposition (5.11.1).**

<!-- label: IV.5.11.1 -->

*Let $X$ be a locally Noetherian prescheme, $Z$ a part of $X$ stable under specialization, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module. Denote by $(x_{\alpha})$ the family of points of $Ass(\mathcal{F}) \cap (X - Z)$ and, for each
$\alpha$, let $Y_{\alpha}$ be the reduced closed sub-prescheme of $X$ having $\overline{x_{\alpha}}$ as underlying
space, $Z_{\alpha} = Z \cap \overline{x_{\alpha}}$. The following two conditions are then equivalent:*

*a) $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is a coherent $\mathcal{O}_{X}$-Module.*

*b) For every $\alpha$, $\mathcal{H}^{0}_{Y_{\alpha}/Z_{\alpha}}(\mathcal{O}_{Y_{\alpha}})$ is a coherent
$\mathcal{O}_{Y_{\alpha}}$-Module.*

*These two conditions entail the following:*

*c) For every $\alpha$, one has $codim(Z_{\alpha}, Y_{\alpha}) \geq 2$.*

*Moreover, the three conditions a), b), c) are equivalent when in addition one of the following properties is verified:*

*(i) Every point of $X$ admits an open neighbourhood isomorphic to a sub-scheme of a regular scheme (in which case one
also says that $X$ is **locally immersible in a regular scheme**).*

*(ii) For every $\alpha$, $Y_{\alpha}$ is universally catenary `(5.6.2)` and its normalization `(II, 6.3.8)`
$\tilde{Y}_{\alpha}$ is finite over $Y_{\alpha}$.*

All the properties envisaged are local on $X$, hence one may restrict to the case where $X = \operatorname{Spec}(A)$ is
affine, $A$ being a Noetherian ring, and $\mathcal{F} = \tilde{M}$, where $M$ is an $A$-module of finite type. Then, for
every $\alpha$, if $h_{\alpha}$ is the canonical injection $Y_{\alpha} \to X$,
$(h_{\alpha})_{*}(\mathcal{O}_{Y_{\alpha}}) = \mathcal{G}_{\alpha}$ is the $\mathcal{O}_{X}$-Module corresponding to the
$A$-module quotient $A/\mathfrak{j}_{x_{\alpha}}$, and, by definition of $Ass(\mathcal{F})$, this $A$-module is
isomorphic to a sub-$A$-module of $M$. Since $\mathcal{H}^{0}_{X/Z}(\mathcal{G}_{\alpha})$ is a quasi-coherent
$\mathcal{O}_{X}$-submodule of $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ `(5.9.2)`, the hypothesis that
$\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is coherent entails that so is $\mathcal{H}^{0}_{X/Z}(\mathcal{G}_{\alpha})$. On
the other hand, it follows from the definition `(5.9.1.2)` that $\mathcal{H}^{0}_{X/Z}(\mathcal{G}_{\alpha})$ is
isomorphic to $(h_{\alpha})_{*}(\mathcal{H}^{0}_{Y_{\alpha}/Z_{\alpha}}(\mathcal{O}_{Y_{\alpha}}))$; this proves that a)
entails b). To see that b) entails a), it suffices to show that there is a finite filtration $(\mathcal{F}_{i})_{0 \leq
i \leq n}$ of $\mathcal{F}$ formed of coherent $\mathcal{O}_{X}$-Modules, with $\mathcal{F}_{0} = \mathcal{F}$,
$\mathcal{F}_{n} = 0$, and such that $\mathcal{H}^{0}_{X/Z}(\mathcal{F}_{i}/\mathcal{F}_{i+1})$ is coherent for every
$i$: this follows, by descending induction on $i$, from the exact sequences

$$ 0 \to \mathcal{F}_{i+1} \to \mathcal{F}_{i} \to \mathcal{F}_{i}/\mathcal{F}_{i+1} \to 0, $$

from the fact that $\mathcal{H}^{0}_{X/Z}$ is a left exact functor `(5.9.2)`, and finally from $(0_{I}, 5.3.3)$ and
`(I, 6.1.1)`. By virtue of `(3.2.8)`, it therefore suffices to prove that $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is
coherent when $\mathcal{F}$ is *irredundant*, that is, $Ass(M) = {\mathfrak{p}}$ is reduced to a single element. Let us
now note the

**Lemma (5.11.1.1).**

<!-- label: IV.5.11.1.1 -->

*Let $A$ be a Noetherian ring, $M$ an $A$-module of finite type, such that $Ass(M) = {\mathfrak{p}}$. There exists a
finite filtration $(M_{i})_{0 \leq i \leq r}$ of $M$ such that $M_{0} = M$, $M_{r} = 0$ and that $M_{i}/M_{i+1}$ is
isomorphic to a submodule of $A/\mathfrak{p}$.*

Note first that the canonical homomorphism $M \to M_{\mathfrak{p}} = N$ is injective (Bourbaki, Alg. comm., chap. IV,
§1, n° 2, prop. 6). Set $B = A_{\mathfrak{p}}$, $\mathfrak{m} = \mathfrak{p}A_{\mathfrak{p}}$, the maximal ideal of $B$;
one has $Ass(N) = {\mathfrak{m}}$ (loc. cit., prop. 5), and since $N$ is a $B$-module of finite type,

<!-- original page 123 -->

there exists an integer $r$ such that $\mathfrak{m}^{r} N = 0$; if one sets $N_{j} = \mathfrak{m}^{j} N$ for $0 \leq j
\leq r$, $N_{j}/N_{j+1}$ is a $(B/\mathfrak{m})$-module of finite type, hence a direct sum of a finite number of
submodules isomorphic to $B/\mathfrak{m}$, since $B/\mathfrak{m}$ is a field; in other words, there is a finite
filtration $(N_{i})_{0 \leq i \leq r}$ of $N$ such that $N_{r} = 0$ and that $N_{i}/N_{i+1}$ is isomorphic to
$B/\mathfrak{m}$, i.e. to the field of fractions of $A/\mathfrak{p}$; the filtration of $M_{i} = M \cap N_{i}$ answers
the question, for $M_{i}/M_{i+1}$ is isomorphic to a sub-$(A/\mathfrak{p})$-module of finite type of $N_{i}/N_{i+1} =
B/\mathfrak{m}$; but one knows that such a submodule is isomorphic to a submodule of $A/\mathfrak{p}$.

The existence of the filtration $(M_{i})$ then shows, by the same reasoning as above, that to prove (granting b)) that
$\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is coherent, one may restrict to showing that $\mathcal{H}^{0}_{X/Z}(\mathcal{H})$
is coherent, where $\mathcal{H} = (A/\mathfrak{p})^{\sim}$, $\mathfrak{p}$ being an associated ideal of $M$. But if
$\mathfrak{p} = \mathfrak{j}_{y}$ with $y \in Z$, the support of $\mathcal{H}$ is a closed set contained in $Z$, since
$Z$ is stable under specialization; the definition `(5.9.1.2)` then shows that $\mathcal{H}^{0}_{X/Z}(\mathcal{H}) = 0$.
If on the contrary $\mathfrak{p} = \mathfrak{j}_{x_{\alpha}}$ for some $\alpha$, one has $\mathcal{H} =
(h_{\alpha})_{*}(\mathcal{O}_{Y_{\alpha}})$ by definition, and one has seen above that
$\mathcal{H}^{0}_{X/Z}(\mathcal{H})$ is isomorphic to
$(h_{\alpha})_{*}(\mathcal{H}^{0}_{Y_{\alpha}/Z_{\alpha}}(\mathcal{O}_{Y_{\alpha}}))$, hence is coherent by virtue of
hypothesis b).

One has already seen `(5.10.10, (ii))` that a) entails c). It remains to prove that, under one or the other of
hypotheses (i), (ii), c) entails b). Note that if $X$ verifies (i), so does each $Y_{\alpha}$. It therefore suffices
`(5.9.3.1)` to prove the

**Corollary (5.11.2).**

<!-- label: IV.5.11.2 -->

*Let $A$ be a Noetherian integral ring, verifying one of the following two hypotheses:*

*(i) $A$ is a quotient of a regular Noetherian ring.*

*(ii) $A$ is universally catenary, and its integral closure $A'$ is a finite $A$-algebra.*

*Then the ring $A^{(1)}$, intersection of the $A_{\mathfrak{p}}$ where $\mathfrak{p}$ runs through the set of prime
ideals of $A$ of height `1`, is a finite $A$-algebra.*

(i) Set $X = \operatorname{Spec}(A)$. The set $U$ of points $x \in X$ where $X$ verifies `(S_2)` is open in $X$ under
hypothesis (i) `(6.11.2)` [^1]. In addition, if one sets $Z = X - U$, one has $codim(Z, X) \geq 2$: indeed, for every $x
\in X$ such that $\dim(\mathcal{O}_{x}) \leq 1$, one has $\dim(\mathcal{O}_{x'}) \leq 1$ for every $x'$ a generization
of $x$, and since $\mathcal{O}_{x'}$ is integral, $prof(\mathcal{O}_{x'}) \geq 1$, hence $X$ verifies `(S_2)` at the
point $x$. One has therefore $Z \subset Z^{(2)}$, and $\mathcal{H}^{0}_{X/Z^{(2)}}(\mathcal{O}_{X}) =
j_{*}(j*(\mathcal{O}_{X}))$, where $j : U \to X$ is the canonical injection `(5.9.1.2)`. But since the prescheme $U$
verifies `(S_2)`, it follows from `(5.10.14)` that $\mathcal{H}^{0}_{U/Z^{(2)}(U)}(\mathcal{O}_{U})$ is isomorphic to
$\mathcal{O}_{U}$; on the other hand, since $codim(Z, X) \geq 2$, one knows, according to Chapter III, §9, that
$j_{*}(\mathcal{O}_{U})$ is a coherent $\mathcal{O}_{X}$-Module, which proves the proposition in case (i).

(ii) The ring $A'$ is, by virtue of hypothesis (ii), a Noetherian integral and integrally closed ring, hence (Bourbaki,
Alg. comm., chap. VII, §1, n° 6, th. 4) the intersection of its local rings $A'_{\mathfrak{p}'}$, where $\mathfrak{p}'$
runs through the set of prime ideals of height `1` of $A'$. Now, for such a prime ideal $\mathfrak{p}'$, if one sets
$\mathfrak{p} = \mathfrak{p}' \cap A$ and $S = A - \mathfrak{p}$, $A'_{\mathfrak{p}'}$ is a local ring at the prime
ideal $S^{-1}\mathfrak{p}'$ of $S^{-1}A'$, and $S^{-1}A'$ is by hypothesis

<!-- original page 124 -->

a finite $A_{\mathfrak{p}}$-algebra; since $S^{-1}\mathfrak{p}'$ lies above the maximal ideal
$\mathfrak{p}A_{\mathfrak{p}}$ of $A_{\mathfrak{p}}$, it is a maximal ideal of $S^{-1}A'$; but by virtue of hypothesis
(ii) and of `(5.6.3, (i))`, $A_{\mathfrak{p}}$ is universally catenary. One deduces therefore from `(5.6.10)` that
$\dim(A_{\mathfrak{p}}) = \dim(A'_{\mathfrak{p}'}) = 1$. It follows from this that one has $A^{(1)} \subset A'$, and
since $A'$ is by hypothesis a finite $A$-module, so is $A^{(1)}$ since $A$ is Noetherian; the proposition is therefore
proved in case (ii).

**Remark (5.11.3).**

<!-- label: IV.5.11.3 -->

*The fact that $A^{(1)}$ is a finite $A$-algebra is no longer necessarily exact if, in hypothesis (ii) of `(5.11.2)`,
one assumes only that $A$ is catenary. An example is given by the catenary local ring $A$ constructed in `(5.6.11)`,
whose integral closure $A'$ (denoted $B$ in `(5.6.11)`) is a finite $A$-algebra; if $A^{(1)}$ were also a finite
$A$-algebra, since it is contained in the field of fractions of $A$, it would be contained in $A'$. But on the other
hand, with the notations of `(5.6.11)`, every prime ideal of height `1` in $A$ is of the form $\mathfrak{p}A$, where
$\mathfrak{p}$ is a prime ideal of height `1` in $C$, and one has $A_{\mathfrak{p}A} = C_{\mathfrak{p}}$; one knows
`(5.6.11)` that $C_{\mathfrak{p}} = E_{\mathfrak{p}'}$, where $\mathfrak{p}'$ is the unique prime ideal of $E$ above
$\mathfrak{p}$, hence $A_{\mathfrak{p}A}$ is integrally closed and consequently contains $A'$; by definition, one
therefore has $A' \subset A^{(1)}$, and the hypothesis that $A^{(1)}$ is a finite $A$-algebra would finally entail
$A^{(1)} = A'$. But this conclusion is absurd, for one of the two prime ideals of $A'$ above the maximal ideal
$\mathfrak{n}A$ of $A$ is of height `1`, whereas $\mathfrak{n}A$ is of height `2`, which would contradict
`(5.10.17, (iv))`.*

**Corollary (5.11.4).**

<!-- label: IV.5.11.4 -->

*Let $X$ be a locally Noetherian prescheme, $Z$ a closed part of $X$, $U = X - Z$, $i : U \to X$ the canonical
injection, $\mathcal{F}$ a coherent $\mathcal{O}_{U}$-Module. For $i_{*}(\mathcal{F})$ to be a coherent
$\mathcal{O}_{X}$-Module, it is necessary that for every $x \in Ass(\mathcal{F})$, one has $codim(\overline{x} \cap Z,
\overline{x}) \geq 2$. This condition is sufficient in each of the two following cases:*

*(i) The prescheme $X$ is locally immersible in a regular scheme.*

*(ii) The prescheme $X$ is universally catenary and universally Japanese (which means, by definition, that every point
$x \in X$ admits an affine open neighbourhood whose ring is universally Japanese `(0, 23.1.1)`).*

One knows `(I, 9.4.7)` that there exists a coherent $\mathcal{O}_{X}$-submodule $\mathcal{G}$ of $i_{*}(\mathcal{F})$
such that $\mathcal{G}|U = \mathcal{F}$. One evidently has `Ass(𝒢) ⊂ Ass(ℱ) ⊂ Ass(i_*(ℱ))`, and since

$$ Ass(i_{*}(\mathcal{F})) = Ass(\mathcal{F}) $$

`(3.1.13)`, one has $Ass(\mathcal{G}) = Ass(\mathcal{F})$; it then suffices to apply `(5.11.1)` to the coherent
$\mathcal{O}_{X}$-Module $\mathcal{G}$, noting that $i_{*}(\mathcal{F}) = \mathcal{H}^{0}_{X/Z}(\mathcal{G})$ and that,
when $X$ is universally catenary and universally Japanese, hypothesis (ii) of `(5.11.1)` is verified by definition.

**Corollary (5.11.5).**

<!-- label: IV.5.11.5 -->

*Let $X$ be a locally Noetherian prescheme, $Z$ a part of $X$ stable under specialization, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module such that one has $Ass(\mathcal{F}) \subset X - Z$. Then the condition:*

*a) $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is a coherent $\mathcal{O}_{X}$-Module*

*implies the following:*

*d) For every part $T$ of $Z$ closed in $X$ (or only for an increasing filtered family of closed parts $T$ of $Z$, of
union $Z$),*

<!-- original page 125 -->

*$i_{*}(\mathcal{F}|X - T)$ (where $i : X - T \to X$ is the canonical injection) is coherent.*

*When $X$ verifies one of the hypotheses (i), (ii) of `(5.11.1)`, a) and d) are equivalent.*

Note that one has $Ass(i_{*}(\mathcal{F}|X - T)) = Ass(\mathcal{F})$ by virtue of the hypothesis and of `(3.1.13)`; it
follows therefore from `(5.10.2)` that the canonical maps

$$ i_{*}(\mathcal{F}|X - T) \to \mathcal{H}^{0}_{X/Z}(\mathcal{F}) $$

are *injective*; the fact that a) implies d) is therefore a consequence of this remark. Conversely, the condition d)
implies, by virtue of `(5.11.1)`, that $codim(T \cap Y_{\alpha}, Y_{\alpha}) \geq 2$ with the notations of `(5.11.1)`;
consequently one has $codim(Z \cap Y_{\alpha}, Y_{\alpha}) \geq 2$ since $Z$ is the union of its parts which are closed
in $X$, and the last assertion of the corollary follows from `(5.11.1)`.

**Corollary (5.11.6).**

<!-- label: IV.5.11.6 -->

*Let $A$ be a Noetherian ring, $X = \operatorname{Spec}(A)$. Consider the following properties:*

*a) For every integral quotient ring $B$ of $A$, the ring $B^{(1)}$ (notation of `(5.11.2)`) is a finite $B$-algebra.*

*b) For every coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ and every part $Z$ of $X$, stable under specialization,
and such that for every $x \in Ass(\mathcal{F}) \cap (X - Z)$ one has $codim(\overline{x} \cap Z, \overline{x}) \geq 2$,
the $\mathcal{O}_{X}$-Module $\mathcal{H}^{0}_{X/Z}(\mathcal{F})$ is coherent.*

*c) For every closed part $T$ of $X$ and every coherent $\mathcal{O}_{U}$-Module $\mathcal{G}$ (where $U = X - T$) such
that for every $x \in Ass(\mathcal{G})$ one has $codim(\overline{x} \cap T, \overline{x}) \geq 2$, $i_{*}(\mathcal{G})$
(where $i : U \to X$ is the canonical injection) is a coherent $\mathcal{O}_{X}$-Module.*

*d) For every integral quotient ring $B$ of $A$ and every ideal $\mathfrak{J}$ of height $\geq 2$ in $B$, the ring
$\bigcap_{\mathfrak{p} \nsupseteq \mathfrak{J}} B_{\mathfrak{p}}$ is a finite $B$-algebra.*

*One then has the implications*

```text
  a) ⇔ b) ⇒ c) ⇔ d).
```

*Moreover, the conditions a), b), c) and d) are verified in each of the two following cases:*

*(i) $A$ is a quotient of a regular ring.*

*(ii) $A$ is universally catenary and universally Japanese.*

Let $B = A/\mathfrak{q}$, where $\mathfrak{q}$ is a prime ideal of $A$, so that $Y = \operatorname{Spec}(B)$ is the
closed part $V(\mathfrak{q})$ of $X$; set $Z = Z^{(2)}(Y)$, which is a part of $X$ stable under specialization; since
$B$ is integral, $Ass(A/\mathfrak{q})$ is reduced to the generic point $\mathfrak{q}$ of $Y$. If condition b) is
verified, one can apply it to the coherent $\mathcal{O}_{X}$-Module $\mathcal{F} = (A/\mathfrak{q})^{\sim}$ and to $Z$,
and by virtue of `(5.9.3.1)`, this shows that $B^{(1)}$ is an $A$-module of finite type, and a fortiori a $B$-module of
finite type. Conversely, suppose a) verified; then, if $\mathcal{F}$ is a coherent $\mathcal{O}_{X}$-Module such that
for every $x \in Ass(\mathcal{F}) \cap (X - Z)$ one has $codim(\overline{x} \cap Z, \overline{x}) \geq 2$, one can apply
(with the notations of `(5.11.1)`) to each of the affine schemes $Y_{\alpha} = \operatorname{Spec}(B_{\alpha})$, where
$B_{\alpha}$ is an integral quotient ring of $A$, the result of a); since by hypothesis $Z_{\alpha}$ is contained in
$Z^{(2)}(Y_{\alpha})$, condition a) (taking account of `(5.10.2)`

<!-- original page 126 -->

and of the fact that $Ass(\mathcal{O}_{Y_{\alpha}})$ is reduced to the generic point of $Y_{\alpha}$) entails that
$\mathcal{H}^{0}_{Y_{\alpha}/Z_{\alpha}}(\mathcal{O}_{Y_{\alpha}})$ is a coherent $\mathcal{O}_{Y_{\alpha}}$-Module, and
b) then follows from `(5.11.1)`.

To see that c) entails d), one reasons as above by applying c) to the case where $\mathcal{F} = (A/\mathfrak{q})^{\sim}$
and $Z = V(\mathfrak{J})$; conversely, one proves that d) entails c) by again using the equivalence of a) and b) in
`(5.11.1)`. It is evident that c) is a special case of b). Finally, the fact that a) (and consequently each of the other
conditions) is verified when $A$ verifies one of the hypotheses (i), (ii) follows from `(5.11.2)`, given the definition
of universally catenary rings and universally Japanese rings.

**Remarks (5.11.7).**

<!-- label: IV.5.11.7 -->

*(i) It is unknown whether, in `(5.11.5)`, condition d) implies a) without supplementary hypothesis on $X$; we shall see
later `(7.2.4)` that it is indeed so when $X$ is a local scheme. Likewise, we shall prove that when $A$ is a local
Noetherian ring the four properties a), b), c), d) of `(5.11.6)` are equivalent `(7.2.4)`. It is unknown whether this
result extends to all Noetherian rings.*

*(ii) If $A$ verifies property a) of `(5.11.6)`, so does every ring of fractions $S^{-1}A$ and every finite $A$-algebra
$C$. Indeed every integral quotient ring of $S^{-1}A$ is of the form $S^{-1}(A/\mathfrak{q})$, where $\mathfrak{q}$ is a
prime ideal of $A$ not meeting $S$; and on the other hand, if $\mathfrak{r}$ is a prime ideal of $C$, $\mathfrak{p}$ its
inverse image in $A$, $C/\mathfrak{r}$ is a finite integral $(A/\mathfrak{p})$-algebra containing $A/\mathfrak{p}$; our
assertions are therefore consequences of `(5.10.17, (iii) and (iv))`.*

### 5.12. Relations between the properties of a Noetherian local ring $A$ and of a quotient ring $A/tA$

One has already seen in `(3.4)` relations between the properties of $A$ and of $A/tA$ concerning associated prime
ideals, as well as the properties of being integral or reduced. One gives in this section other relations between the
properties of these rings, linked to the notions of dimension and depth.

**Proposition (5.12.1).**

<!-- label: IV.5.12.1 -->

*Let $A$ be a Noetherian local ring, $X = \operatorname{Spec}(A)$, $t$ an element of $A$ belonging to a system of
parameters `(0, 16.3.6)`, `X_0` the closed subspace $V(t)$ of $X$, `X_1` the complementary open set $X - X_{0}$. Let $Z$
be a part of $X$ such that every specialization of a point of $Z$ belongs to $Z$. Suppose that $X$ is biequidimensional
(which will be the case if $A$ is equidimensional and a quotient of a regular local ring `(0, 16.5.12)`). Then if one
sets $Z_{0} = Z \cap X_{0}$, $Z_{1} = Z \cap X_{1}$, one has*

```text
  codim(Z_0, X_0) ≤ codim(Z, X) ≤ codim(Z_1, X_1).                  (5.12.1.1)
```

The second inequality follows from the definition `(5.1.3)`; to prove the first, one may restrict to proving it when $Z$
is closed: indeed, by hypothesis $Z$ is the union of closed parts $Z_{\alpha}$, and if one has $codim(X_{0} \cap
Z_{\alpha}, X_{0}) \leq codim(Z_{\alpha}, X)$ for every $\alpha$, one will also have
`codim(Z_0, X_0) = inf_α(codim(X_0 ∩ Z_α, X_0)) ≤ inf_α(codim(Z_α, X)) = codim(Z, X)`. Suppose therefore $Z$ closed, so
that one has

```text
  codim(Z, X) = dim(X) − dim(Z)
```

<!-- original page 127 -->

by virtue of `(0, 14.3.5.1)`. On the other hand, `X_0` is evidently catenary, equidimensional and of dimension
$\dim(X) - 1$ by virtue of `(0, 16.3.4)`; one therefore also has

```text
  codim(Z_0, X_0) = dim(X_0) − dim(Z_0) = dim(X) − 1 − dim(Z_0).
```

But one has $\dim(Z_{0}) \geq \dim(Z) - 1$ `(0, 16.3.4)`, which completes the proof of the first inequality
`(5.12.1.1)`.

**Proposition (5.12.2).**

<!-- label: IV.5.12.2 -->

*Let $A$ be a Noetherian local ring, $M$ an $A$-module of finite type, $t$ an $M$-regular element belonging to the
maximal ideal $\mathfrak{m}$ of $A$, $k$ an integer $\geq 1$. Assume that $A$ is a catenary ring. Then, if $M/tM$ is
equidimensional and satisfies $(S_{k})$, so is $M$.*

Taking account of $(Err_{III}, 30)$ and of `(5.7.3, (vi))`, one may restrict to the case where $Supp(M) =
\operatorname{Spec}(A) = X$. Set $X_{0} = V(t) = \operatorname{Spec}(A/tA)$; since $M/tM$ verifies `(S_1)` by
hypothesis, it has no embedded associated prime ideals `(5.7.5)`. Applying `(3.4.4)` at the closed point of $X$ (and of
any closed sub-prescheme of $X$), one sees that the irreducible components of $Supp(M/tM)$ are exactly those of $Y_{i}
\cap X_{0}$, where $Y_{i}$ $(1 \leq i \leq r)$ are the irreducible components of $X$. Since $t$ is by hypothesis
$M$-regular, $V(t)$ contains no maximal point of $X$ `(3.1.8)`; each of the irreducible components of $Y_{i} \cap X_{0}$
is therefore of codimension `1` in $Y_{i}$ `(5.1.8)`; since $X$ is catenary and all the irreducible components of
$Supp(M/tM)$ have by hypothesis the same dimension, one concludes that the $Y_{i}$ all have the same dimension, in other
words $X$ is equidimensional, hence biequidimensional since $A$ is local and catenary. To see that $M$ verifies
$(S_{k})$, apply criterion `(5.7.4)`: one must verify (with the notations of `(5.7.4)`) that, for every integer $n \geq
0$, one has $codim(Z_{n}, X) > n + k$. Now, the hypothesis on $M/tM$ and criterion `(5.7.4)` show that one has
$codim(Z_{n} \cap X_{0}, X_{0}) > n + k$ for every integer $n \geq 0$. But every specialization of a point of $Z_{n}$
still belongs to $Z_{n}$, as we shall see in `(6.11.5)` [^2]; since $X$ is biequidimensional and $t$ belongs to a system
of parameters for $M$ `(0, 16.4.1)`, hence also for $A$ (the annihilator of $M$ being nilpotent by virtue of the
hypothesis $Supp(M) = \operatorname{Spec}(A)$), the conclusion follows from `(5.12.1)`.

**Remark (5.12.3).**

<!-- label: IV.5.12.3 -->

*If, in the statement of `(5.12.2)`, one assumes only that $M/tM$ is equidimensional, it does not necessarily follow
that $M$ is equidimensional. For example, let $k$ be a field, $B$ the polynomial ring `k[T, U, V]` in `3`
indeterminates, $C$ the local ring of $B$ at the maximal ideal $BT + BU + BV$ of $B$, and let $\mathfrak{p} = CU$,
$\mathfrak{q} = CV + C(T + U)$; consider then the local ring $A = C/\mathfrak{pq}$ (geometrically, if $X$ is the closed
sub-prescheme of affine space of `3` dimensions over $k$, formed of a plane and a line cutting this plane at a point
$x$, $A$ is the local ring of $X$ at the point $x$). Let $t$, $u$, $v$ be the canonical images of $T$, $U$, $V$ in $A$;
it is immediate that $t$ is not a zero-divisor in $A$, and $A/tA$ is isomorphic to $C_{0}/\mathfrak{p}_{0}
\mathfrak{q}_{0}$, where `C_0` is the local ring of $B_{0} = k[U, V]$ at the maximal ideal $B_{0} U + B_{0} V$, and
$\mathfrak{p}_{0} = C_{0} U$, $\mathfrak{q}_{0} = C_{0} U + C_{0} V$ ($\mathfrak{q}_{0}$ being therefore the maximal
ideal of `C_0`). It is immediate that $\operatorname{Spec}(A/tA)$*

<!-- original page 128 -->

*is irreducible and of dimension `1`, $A/tA$ does not verify `(S_1)` and $\operatorname{Spec}(A)$ is not
equidimensional.*

**Corollary (5.12.4).**

<!-- label: IV.5.12.4 -->

*Let $A$ be a Noetherian catenary local ring, $t$ a regular element belonging to the maximal ideal of $A$, $k$ an
integer $\geq 1$. If $A/tA$ verifies $(S_{k})$, so does $A$.*

If $k = 1$, the corollary follows from `(3.4.4)`, given the interpretation of condition `(S_1)` `(5.7.5)`. If $k \geq
2$, it follows from the Hartshorne criterion `(5.10.9)` that $A/tA$ is equidimensional, and one may apply `(5.12.2)`.

**Proposition (5.12.5).**

<!-- label: IV.5.12.5 -->

*Let $A$ be a Noetherian catenary local ring, $t$ a regular element of $A$ belonging to the maximal ideal of $A$, $k$ an
integer $\geq 0$. If the ring $A/tA$ is reduced, equidimensional and verifies property $(R_{k})$, the ring $A$ also
possesses these three properties.*

One knows already `(3.4.6)` that $A$ is reduced, and it follows from `(5.12.2)`, applied for $k = 1$, that $A$ is
equidimensional. Set $X = \operatorname{Spec}(A)$, $X_{0} = V(t) = \operatorname{Spec}(A/tA)$, and let $Z$ be the set of
points $x \in X$ where $X$ is not regular; by virtue of `(0, 17.3.2)` every specialization of a point of $Z$ belongs to
$Z$. It follows on the other hand from `(0, 17.1.8)` that for every point $x \in X_{0}$ where `X_0` is regular, $X$ is
also regular, hence the set $Z_{0}'$ of points where `X_0` is not regular contains $Z_{0} = Z \cap X_{0}$; the
hypothesis therefore entails that

```text
  k ≤ codim(Z_0', X_0) ≤ codim(Z_0, X_0).
```

But, since $A$ is equidimensional and catenary, one has, according to `(5.12.1)`

```text
  codim(Z_0, X_0) ≤ codim(Z, X)
```

which proves that $X$ verifies $(R_{k})$.

**Remark (5.12.6).**

<!-- label: IV.5.12.6 -->

*If, in the statement of `(5.12.5)`, one assumes only that $A/tA$ is reduced and possesses property $(R_{k})$, it does
not necessarily follow that $A$ possesses property $(R_{k})$. For example, let $k$ be a field, $P(U, V)$ an irreducible
polynomial of `k[U, V]` such that the curve $\Gamma$ defined by the principal ideal `(P)` in the affine plane
$\operatorname{Spec}(k[U, V])$ has a singular point corresponding to the maximal ideal $(U) + (V)$ (for example $P(U, V)
= U(U^{2} + V^{2}) + (U^{2} - V^{2})$, which gives a cubic with a double point). Let then $B$ be the polynomial ring in
`4` indeterminates `k[T, U, V, W]`, $C$ the local ring of $B$ at the maximal ideal $BT + BU + BV + BW$, and let*

```text
  𝔭 = CW + CP(U − T, V),    𝔮 = CU.
```

*Consider then the local ring $A = C/\mathfrak{pq}$ (geometrically, if $X$ is the closed sub-prescheme of affine space
of `4` dimensions, formed of a hyperplane $H$ and of a `2`-dimensional "cylinder" $L$ whose "base" is the curve $\Gamma$
and whose "singular line" $Y$ is not contained in the hyperplane $H$, then $A$ is the local ring of $X$ at the point $x$
where $Y$ meets $H$). One then sees at once that $\operatorname{Spec}(A/tA)$ (where $t$ is the canonical image of $T$ in
$A$) has as unique singular point $x$, whose local ring is $A/tA$ itself, which is reduced and of dimension `2`; on the
contrary, the generic point $y$ of the "singular line" $Y$ (defined by the image in $A$ of the ideal $C(U - T) + CV +
CW$) is a singular point of $X$, and $\mathcal{O}_{X,y}$ is of dimension `1`; in other words, $A/tA$ is reduced and
verifies `(R_1)`, but $A$ does not verify `(R_1)`.*

<!-- original page 129 -->

**Corollary (5.12.7).**

<!-- label: IV.5.12.7 -->

*Let $A$ be a Noetherian catenary local ring, $t$ a regular element of $A$ belonging to the maximal ideal of $A$. If
$A/tA$ is integral and integrally closed, so is $A$.*

By virtue of Serre's criterion `(5.8.6)` and of the fact that the ring $A$ is local, it suffices to show that
$\operatorname{Spec}(A)$ verifies `(S_2)` and `(R_1)`. But the hypothesis on $A/tA$ entails that $A$ verifies `(R_1)` by
`(5.12.5)`, and that $A$ verifies `(S_2)` by `(5.12.4)`.

**Proposition (5.12.8) (Hironaka's lemma).**

<!-- label: IV.5.12.8 -->

*Let $A$ be a reduced, equidimensional and catenary Noetherian local ring. Assume in addition that for every minimal
prime ideal $\mathfrak{q}_{i}$ of $A$, the ring $B_{i} = A/\mathfrak{q}_{i}$ is such that $B^{(1)}_{i}$ (notation of
`(5.10.17)`) is a finite $B_{i}$-algebra (which will be the case for example when $A$ possesses one of the properties
(i), (ii) of `(5.11.6)`). Let $t$ be an element of $A$, not a zero-divisor in $A$, and such that:*

*(i) The $A$-module $A/tA$ has only one non-embedded associated prime ideal $\mathfrak{p}$ (necessarily of height `1` by
virtue of the Hauptidealsatz `(0, 16.3.2)`, but one does not assume that this is the only associated prime ideal of
$A/tA$).*

*(ii) The ideal $\mathfrak{p}A_{\mathfrak{p}}$ of $A_{\mathfrak{p}}$ is generated by $t/1$.*

*(iii) The ring $A/\mathfrak{p}$ is integrally closed.*

*Under these conditions, the ring $A$ is integral and integrally closed, and one has $\mathfrak{p} = tA$.*

If $Z = V(tA)$, hypothesis (i) entails that $Z$ is an irreducible closed part of $X = \operatorname{Spec}(A)$, whose
generic point $z$ is such that $\mathfrak{j}_{z} = \mathfrak{p}$. Hypothesis (ii) shows that the maximal ideal
$\mathfrak{p}A_{\mathfrak{p}}$ of the Noetherian local ring $A_{\mathfrak{p}}$ is generated by a single element, hence
$A_{\mathfrak{p}}$ is a discrete valuation ring of which $t/1$ is a uniformizer (Bourbaki, Alg. comm., chap. VI, §3, n°
6, prop. 9); $A_{\mathfrak{p}}/tA_{\mathfrak{p}}$ is the residue field of $A_{\mathfrak{p}}$, hence an
$A_{\mathfrak{p}}$-module of length `1`. By virtue of `(3.4.2)`, this entails that $Z$ is contained in only one of the
irreducible components $X_{i}$ of $X$; for every other irreducible component $X_{j}$ of $X$, one consequently has
$\dim(X_{j} \cap Z) < \dim(Z)$. On the other hand, since $t$ is not a zero-divisor in $A$, it is contained in none of
the $\mathfrak{q}_{i}$, and one consequently has `(5.1.8)` $codim(X_{i} \cap Z, X_{i}) = codim(X_{j} \cap Z, X_{j}) =
1$, whatever $j \neq i$. Since $A$ is supposed biequidimensional, the relation $\dim(X_{i} \cap Z) \neq \dim(X_{j} \cap
Z)$ would therefore entail $\dim(X_{i}) \neq \dim(X_{j})$ `(0, 14.3.3.1)`, which is absurd. One sees therefore that
there is only one minimal prime ideal in $A$; since $A$ is by hypothesis reduced, this entails that it is integral. Note
now that since $A^{(1)}$ is a finite $A$-algebra, it is a Noetherian semi-local ring, and every non-embedded associated
prime ideal of $A^{(1)}/tA^{(1)}$ is therefore of height `1` by virtue of the Hauptidealsatz `(0, 16.3.2)`; now, for
such an ideal $\mathfrak{r}$, $\mathfrak{r} \cap A$ is of height `1` by virtue of `(5.10.17, (iv))` and since it
contains `tA`, it can only be $\mathfrak{p}$ by virtue of hypothesis (i). On the other hand, $A^{(1)}$ is contained in
the integral closure $A'$ of $A$; setting $S = A - \mathfrak{p}$, the integral closure of $A_{\mathfrak{p}}$ is
$S^{-1}A'$ (Bourbaki, Alg. comm., chap. V, §1, n° 5, prop. 17), hence $S^{-1}A' = A_{\mathfrak{p}}$ since
$A_{\mathfrak{p}}$ is a discrete valuation ring; it follows (loc. cit., §2, n° 1, lemme 1) that there exists only one
prime ideal $\mathfrak{p}'$ of $A'$ above $\mathfrak{p}$, and a fortiori only one prime ideal $\mathfrak{p}^{(1)}$ of
$A^{(1)}$ above $\mathfrak{p}$, and one has $A_{\mathfrak{p}} = A'_{\mathfrak{p}'} = A^{(1)}_{\mathfrak{p}^{(1)}}$. Note
now that $A^{(1)}$ verifies `(S_2)` `(5.10.17, (i))` and since $t$ is not a zero-divisor in $A^{(1)}$,
$A^{(1)}/tA^{(1)}$ has no embedded associated prime ideals

<!-- original page 130 -->

`(5.7.7)`. The ideal $\mathfrak{p}^{(1)}$ is therefore the only associated prime ideal of $A^{(1)}/tA^{(1)}$, in other
words $tA^{(1)}$ is a $\mathfrak{p}^{(1)}$-primary ideal of $A^{(1)}$; this means again that $tA^{(1)}$ is the inverse
image in $A^{(1)}$ of $tA^{(1)}_{\mathfrak{p}^{(1)}} = tA_{\mathfrak{p}}$, and this latter is the maximal ideal of
$A_{\mathfrak{p}}$ according to (ii); hence $tA^{(1)} = \mathfrak{p}^{(1)}$ is prime in $A^{(1)}$. On the other hand,
$A^{(1)}/\mathfrak{p}^{(1)}$ is finite over $A/\mathfrak{p}$ and has the same field of fractions (namely, the residue
field of $A^{(1)}_{\mathfrak{p}^{(1)}} = A_{\mathfrak{p}}$), hence it is identical to $A/\mathfrak{p}$ by virtue of
hypothesis (iii). One may therefore write $A^{(1)} = A + \mathfrak{p}^{(1)} = A + tA^{(1)}$, and since $t$ is contained
in the radical of the Noetherian semi-local ring $A^{(1)}$, Nakayama's lemma entails $A^{(1)} = A$, whence
$\mathfrak{p}^{(1)} = \mathfrak{p} = tA$. But since $A$ is catenary and $A/tA$ integral and integrally closed by virtue
of hypothesis (iii), one concludes from `(5.12.7)` that $A$ is integrally closed. Q.E.D.

**Remark (5.12.9).**

<!-- label: IV.5.12.9 -->

*The conclusion of `(5.12.8)` fails if one no longer assumes $A$ equidimensional. For example, let $k$ be a field, $B$
the polynomial ring `k[X, Y, Z]` in three indeterminates, $C$ the ring $B/\mathfrak{r}_{1} \mathfrak{r}_{2}$, where
$\mathfrak{r}_{1} = BZ$ and $\mathfrak{r}_{2} = BX + BY$; let $\mathfrak{m}$ be the maximal ideal $BX + BY + BZ$,
$\mathfrak{n} = \mathfrak{m}/\mathfrak{r}_{1} \mathfrak{r}_{2}$ its image in $C$, $A$ the local ring $C_{\mathfrak{n}}$.
Finally, let $t_{0}$ be the image in $C$ of the element $Y + Z$ of $B$, $t$ its image in $A$ ($\operatorname{Spec}(C)$
is therefore formed of a plane $P$ and of a line $D$ not contained in this plane, $\operatorname{Spec}(C/t_{0} C)$ of a
line $D'$ contained in $P$ and passing through the point $D \cap P$). The ring $A$ is reduced and catenary (being a
quotient of a regular ring) and its minimal prime ideals $\mathfrak{q}_{1}$, $\mathfrak{q}_{2}$ are the images of
$\mathfrak{r}_{1}$, $\mathfrak{r}_{2}$. The $A$-module $A/tA$ has only one non-embedded associated prime ideal
$\mathfrak{p}$, image of $BY + BZ$, $\mathfrak{p}A_{\mathfrak{p}}$ is generated by $t/1$ and $A/\mathfrak{p}$ is
isomorphic to `k[X]`; but $A$ is not integral.*

**Corollary (5.12.10).**

<!-- label: IV.5.12.10 -->

*Let $A$ be a Noetherian integral local ring, verifying one of the following hypotheses:*

*a) $A$ is a quotient of a regular ring.*

*b) $A$ is universally catenary and universally Japanese.*

*Let $(x_{i})_{1 \leq i \leq n}$ be a sequence of $n$ elements of $A$; set $\mathfrak{J} = x_{1} A + \cdots + x_{n} A$,
and suppose the following conditions are verified:*

*(i) There exists only one non-embedded associated prime ideal $\mathfrak{p}$ of $A/\mathfrak{J}$ and $\mathfrak{p}$ is
of height $n$.*

*(ii) The maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$ of $A_{\mathfrak{p}}$ is generated by the $x_{i}/1$ (hence
$A_{\mathfrak{p}}$ is a regular local ring of dimension $n$).*

*(iii) The ring $A/\mathfrak{p}$ is integrally closed.*

*Under these conditions, for every integer $i$ such that $0 \leq i \leq n$, the quotient ring $A/(x_{1} A + \cdots +
x_{i} A)$ is integrally closed and of dimension $\dim(A) - i$. In particular, $\mathfrak{J}$ is prime, equal to
$\mathfrak{p}$, $A$ is integrally closed and $(x_{i})_{1 \leq i \leq n}$ is an $A$-regular sequence.*

Let us proceed by induction on $n$, the proposition being trivial for $n = 0$ and reducing to Hironaka's lemma
`(5.12.8)` for $n = 1$. One may therefore assume $n \geq 2$. Let $\mathfrak{J}' = x_{1} A + \cdots + x_{n-1} A$, and let
$\mathfrak{q}$ be a minimal prime ideal among those containing $\mathfrak{J}'$; one has $ht(\mathfrak{q}) \leq n - 1$
`(0, 16.3.1)`; let us show that $\mathfrak{q} \subset \mathfrak{p}$. Indeed, if $\mathfrak{p}'$ is minimal among the
prime ideals of $A$ containing $\mathfrak{q} + x_{n} A$, $\mathfrak{p}'/\mathfrak{q}$ is of height `1` in
$A/\mathfrak{q}$ by the Hauptidealsatz `(0, 16.3.2)`, hence $\mathfrak{p}'$ is of height $\leq n$ since $A$ is catenary
`(0, 16.1.4)`; but since it contains $\mathfrak{J}$, it is necessarily equal to $\mathfrak{p}$, whence $\mathfrak{q}
\subset \mathfrak{p}$,

<!-- original page 131 -->

and $\mathfrak{q}$ is induced on $A$ by a prime ideal of $A_{\mathfrak{p}}$, minimal among those containing
$\mathfrak{J}'A_{\mathfrak{p}}$. But by virtue of hypothesis (ii) and of `(0, 17.1.7)`, $\mathfrak{J}'A_{\mathfrak{p}}$
is prime in $A_{\mathfrak{p}}$, hence $\mathfrak{q} = A \cap \mathfrak{J}'A_{\mathfrak{p}}$ is *the* unique non-embedded
associated prime ideal of $A/\mathfrak{J}'$ and it is of height $n - 1$, since $\mathfrak{J}'A_{\mathfrak{p}}$ is of
height $n - 1$ and $\mathfrak{q}$ of height $\leq n - 1$. In addition $\mathfrak{q}A_{\mathfrak{q}} =
\mathfrak{J}'A_{\mathfrak{q}}$ and since $A_{\mathfrak{q}} = (A_{\mathfrak{p}})_{\mathfrak{q}}$, the maximal ideal
$\mathfrak{q}A_{\mathfrak{q}}$ is generated by $\mathfrak{J}'$. One sees therefore that the sequence $(x_{i})_{1 \leq i
\leq n-1}$ already verifies conditions (i) and (ii) of the statement. Let us show that it also verifies (iii). Consider
for this the integral ring $B = A/\mathfrak{q}$, and let $t$ be the canonical image of $x_{n}$ in $B$. It is immediate
(cf. `(5.6.3, (iv))`) that if $A$ verifies hypothesis a) (resp. b)), so does $B$; since $x_{n} \notin \mathfrak{q}$, one
has $t \neq 0$; let us show that $B$ and $t$ verify the hypotheses of Hironaka's lemma. Indeed, a prime ideal
$\mathfrak{n}$ of $B$ minimal among those containing $t$ is the image of a prime ideal of $A$ minimal among those
containing $\mathfrak{q} + x_{n} A$, and one has seen that $\mathfrak{p}$ is this unique ideal; since $B_{\mathfrak{n}}
= A_{\mathfrak{p}}/\mathfrak{q}A_{\mathfrak{p}}$ and $\mathfrak{n}B_{\mathfrak{n}} =
\mathfrak{p}A_{\mathfrak{p}}/\mathfrak{q}A_{\mathfrak{p}}$, the fact that $\mathfrak{q}A_{\mathfrak{p}} =
\mathfrak{J}'A_{\mathfrak{p}}$ and that $\mathfrak{p}A_{\mathfrak{p}}$ is generated by $\mathfrak{J}$ entails that
$\mathfrak{n}B_{\mathfrak{n}}$ is generated by $t$. Finally, $B/\mathfrak{n} = A/\mathfrak{p}$ is integrally closed. The
application of `(5.12.8)` proves therefore that $B = A/\mathfrak{q}$ is integrally closed and that $\mathfrak{p} =
\mathfrak{q} + x_{n} A$. Let us now use the induction hypothesis, which shows that $A/(x_{1} A + \cdots + x_{i} A)$ is
integrally closed and of dimension $\dim(A) - i$ for $0 \leq i \leq n - 1$ and that $\mathfrak{q} = \mathfrak{J}'$,
whence $\mathfrak{p} = \mathfrak{J}' + x_{n} A = \mathfrak{J}$. One concludes that $A/\mathfrak{J} = A/\mathfrak{p}$ is
integrally closed; since $\dim(A_{\mathfrak{p}}) = n$ and `dim(A/𝔭) = dim(A) − dim(A_𝔭)` since $A$ is biequidimensional,
this completes the proof.

[^1]: The reader may verify that `(5.11.2)` is not used in the proof of `(6.11.2)`.

[^2]: The reader will verify that `(5.12.2)` is not used for the proof of `(6.11.5)`.

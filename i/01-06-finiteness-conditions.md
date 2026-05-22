# Chapter I — The Language of Schemes

## §6. Finiteness Conditions

<!-- label: I.6 -->

> **Translation status.** Skeleton with definitions and principal statements; full proofs reference .

### 6.1. Noetherian and locally Noetherian preschemes

<!-- label: I.6.1 -->

**Definition (6.1.1).** A prescheme $X$ is _locally Noetherian_ if every $x \in X$ admits an affine open neighborhood
$\operatorname{Spec}(A)$ with $A$ Noetherian. $X$ is _Noetherian_ if it is locally Noetherian and quasi-compact.

**Proposition (6.1.2).** A prescheme $X$ is locally Noetherian iff $X$ admits a covering by affine opens
$\operatorname{Spec}(A_{i})$ with each $A_{i}$ Noetherian.

**Proposition (6.1.3).** For $X$ locally Noetherian: every open subset is locally Noetherian; the underlying topological
space of $X$ is locally Noetherian.

**Proposition (6.1.4).** $X$ is Noetherian iff its underlying space is Noetherian and $X$ is covered by finitely many
affine opens $\operatorname{Spec}(A_{i})$ with each $A_{i}$ Noetherian.

**Proposition (6.1.6).** A closed subprescheme of a (locally) Noetherian prescheme is (locally) Noetherian.

**Corollary (6.1.7).** A locally closed subprescheme of a (locally) Noetherian prescheme is (locally) Noetherian.

**Proposition (6.1.10).** A locally Noetherian prescheme has only finitely many irreducible components in each
quasi-compact open set.

**Corollary (6.1.11).** Every closed subset of a locally Noetherian prescheme has the topology of a Noetherian space
locally.

**Proposition (6.1.13).** Every open subset of a Noetherian prescheme is quasi-compact.

### 6.2. Artinian preschemes

<!-- label: I.6.2 -->

**Definition (6.2.1).** A prescheme $X$ is _Artinian_ if $X = \operatorname{Spec}(A)$ for $A$ an Artinian ring.

**Proposition (6.2.2).** An Artinian prescheme is Noetherian and 0-dimensional; its underlying space is finite,
discrete.

### 6.3. Morphisms of finite type

<!-- label: I.6.3 -->

**Definition (6.3.1).** A morphism $f : X \to Y$ is _locally of finite type_ if for every $x \in X$ there are affine
opens $\operatorname{Spec}(A) \ni x$ and $\operatorname{Spec}(B) \ni f(x)$ with $f(\operatorname{Spec}(A)) \subset
\operatorname{Spec}(B)$ such that $A$ is a finitely generated $B$-algebra. $f$ is _of finite type_ if additionally $f$
is quasi-compact (i.e., the inverse image of every quasi-compact open is quasi-compact).

**Proposition (6.3.2).** Locally finite type is preserved under composition.

**Proposition (6.3.3).** Locally finite type is preserved under base change.

**Proposition (6.3.4).** Locally finite type can be checked on an affine open cover.

**Corollary (6.3.5).** Finite-type morphisms are stable under composition, base change, and product.

**Corollary (6.3.6).** Closed immersions are of finite type.

**Proposition (6.3.7).** A morphism of finite type between Noetherian preschemes has Noetherian source and target
compatibility.

**Proposition (6.3.10).** Finite-type morphisms with Noetherian target have Noetherian source.

### 6.4. Algebraic preschemes

<!-- label: I.6.4 -->

**Definition (6.4.1).** A _$K$-prescheme algebraic over a field $K$_ (or _algebraic $K$-prescheme_) is a $K$-prescheme
of finite type. $K$ is the _base field_.

**Proposition (6.4.2).** Every algebraic $K$-prescheme is Noetherian.

**Corollary (6.4.3).** Every closed subprescheme of an algebraic $K$-prescheme is algebraic.

**Proposition (6.4.4) (Hilbert's Nullstellensatz).** For an algebraic $K$-prescheme $X$ and any $K$-point $x \in X$
(closed point in particular), the residue field $\kappa(x)$ is a finite algebraic extension of $K$.

**Corollary (6.4.6).** A $K$-prescheme is finite over $K$ (a _finite $K$-scheme_) iff it is affine, of finite type over
$K$, and its space is finite.

**(6.4.5)** A _finite $K$-scheme_ is $\operatorname{Spec}(A)$ with $A$ a finite $K$-algebra; its _rank_ is $\dim_{K} A$.
The _separable rank_ is $\dim_{K} (A_{sep})$, where $A_{sep}$ is the maximal separable subalgebra.

**(6.4.8)** The _geometric number of points_ of an algebraic $K$-prescheme $X$ is the cardinality of the set of
$\bar{K}$-rational points, where $\bar{K}$ is an algebraic closure.

**Proposition (6.4.9).** Algebraic $K$-preschemes form a category, closed under fiber products over $K$.

**Proposition (6.4.11).** Properties of algebraic $K$-preschemes pass to extension fields $K \to L$.

### 6.5. Local determination of a morphism

<!-- label: I.6.5 -->

**Proposition (6.5.1).** A morphism of preschemes is determined by its restrictions to an open cover of the source
(i.e., morphisms can be glued from compatible restrictions).

**(6.5.6)** A morphism $f : X \to Y$ is _birational_ if `X, Y` have finitely many irreducible components and the induced
map on generic points is bijective with isomorphisms of local rings; see (2.2.9).

### 6.6. Quasi-compact morphisms

<!-- label: I.6.6 -->

**Definition (6.6.1).** A morphism $f : X \to Y$ is _quasi-compact_ if $f^{-1}(U)$ is quasi-compact for every
quasi-compact open $U \subset Y$. Equivalently, $f^{-1}(V)$ is quasi-compact for every affine open $V \subset Y$.

**(6.6.2)** _Morphism locally of finite type:_ defined in (6.3.1); the combination of "locally of finite type" +
"quasi-compact" yields "of finite type."

Composition and base change preserve quasi-compactness.

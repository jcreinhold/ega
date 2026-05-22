# Chapter 0 — Preliminaries

## §2. Irreducible Spaces. Noetherian Spaces

<!-- label: 0.2 -->

### 2.1. Irreducible spaces

<!-- label: 0.2.1 -->

**(2.1.1)** A topological space $X$ is called _irreducible_ if it is nonempty and is not the union of two proper closed
subspaces. Equivalently: $X \neq \emptyset$, and the intersection of any two (hence any finitely many) nonempty open
subsets of $X$ is nonempty; or every nonempty open subset of $X$ is dense; or every closed subset $\neq X$ is _nowhere
dense_ [EGA: rare]; or every open subset of $X$ is _connected_.

**(2.1.2)** A subspace $Y$ of a topological space $X$ is irreducible if and only if its closure $\bar{Y}$ is
irreducible. In particular, every subspace of the form $\bar{x}$ is irreducible; we shall express the relation $y \in
\bar{x}$ (equivalently, $\bar{y} \subset \bar{x}$) by saying that $y$ is a _specialization_ of $x$, or that $x$ is a
_generization_ of $y$. If an irreducible space $X$ contains a point $x$ with $X = \bar{x}$, we call $x$ a _generic
point_ of $X$. Every nonempty open subset of $X$ then contains $x$, and every subspace containing $x$ admits $x$ as a
generic point.

**(2.1.3)** Recall that a topological space $X$ is called a _Kolmogorov space_ if it satisfies the separation axiom:

> (T₀) If $x \neq y$ are two distinct points of $X$, there is an open set containing exactly one of $x$, $y$.

If an irreducible Kolmogorov space admits a generic point, it admits exactly _one_, since every nonempty open set
contains every generic point.

Recall that a topological space $X$ is called _quasi-compact_ if every open cover of $X$ admits a finite subcover
(equivalently, if every decreasing filtered family of nonempty closed sets has nonempty intersection). If $X$ is
quasi-compact, every nonempty closed subset $A \subset X$ contains a _minimal_ nonempty closed subset $M$ (since the set
of nonempty closed subsets of $A$ is inductive for the relation $\supset$); if $X$ is moreover a Kolmogorov space, $M$
is necessarily reduced to a single point, called by abuse of language a _closed point_.

**(2.1.4)** In an irreducible space $X$, every nonempty open subspace $U$ is irreducible, and if $X$ admits a generic
point $x$, then $x$ is also a generic point of $U$.

Let $(U_{\alpha})$ be a cover of a topological space $X$ by nonempty open sets, with nonempty index set. For $X$ to be
irreducible, it is necessary and sufficient that each $U_{\alpha}$ be irreducible and that $U_{\alpha} \cap U_{\beta}
\neq \emptyset$ for all $\alpha, \beta$. The condition is plainly necessary; for sufficiency, it suffices to show that
if $V$ is a nonempty open subset of $X$, then $V \cap U_{\alpha} \neq \emptyset$ for every $\alpha$, for then $V \cap
U_{\alpha}$ is dense in $U_{\alpha}$ for every $\alpha$, and so $V$ is dense in $X$. Now there is at least one index
$\gamma$ with $V \cap U_{\gamma} \neq \emptyset$; then $V \cap U_{\gamma}$ is dense in $U_{\gamma}$, and since
$U_{\alpha} \cap U_{\gamma} \neq \emptyset$ for every $\alpha$, we have $V \cap U_{\alpha} \cap U_{\gamma} \neq
\emptyset$.

**(2.1.5)** Let $X$ be an irreducible space and $f : X \to Y$ a continuous map into a topological space $Y$. Then $f(X)$
is irreducible, and if $x$ is a generic point of $X$, then $f(x)$ is a generic point of $f(X)$, hence also of
$f\bar{X}$. In particular, if moreover $Y$ is irreducible with a unique generic point $y$, then $f(X)$ is dense in $Y$
if and only if $f(x) = y$.

**(2.1.6)** Every irreducible subspace of a topological space $X$ is contained in a _maximal_ irreducible subspace,
which is necessarily closed. The maximal irreducible subspaces of $X$ are called the _irreducible components_ of $X$. If
$Z_{1}$, $Z_{2}$ are distinct irreducible components of $X$, then $Z_{1} \cap Z_{2}$ is nowhere dense in each of $Z_{1}$
and $Z_{2}$; in particular, if an irreducible component admits a generic point (2.1.2), that point lies in no other
irreducible component. If $X$ has only _finitely many_ irreducible components $Z_{i}$ ($1 \leq i \leq n$), and if $U_{i}
= Z_{i} \cap \complement(\bigcup_{j \neq i} Z_{j})$, then the $U_{i}$ are open, irreducible, pairwise disjoint, and
their union is dense in $X$.

Let $U$ be an open subset of a topological space $X$. If $Z$ is an irreducible subset of $X$ meeting $U$, then $Z \cap
U$ is open and dense in $Z$, hence irreducible; conversely, for every closed irreducible subset $Y$ of $U$, the closure
$\bar{Y}$ of $Y$ in $X$ is irreducible and $\bar{Y} \cap U = Y$. There is therefore a _bijective correspondence_ between
the irreducible components of $U$ and the irreducible components of $X$ meeting $U$.

**(2.1.7)** If a topological space $X$ is the union of _finitely many_ closed irreducible subspaces $Y_{i}$, then the
irreducible components of $X$ are the _maximal_ elements among the $Y_{i}$: for any closed irreducible $Z \subset X$,
$Z$ is the union of the $Z \cap Y_{i}$, so $Z$ must be contained in some $Y_{i}$. If $Y$ is a subspace of a topological
space $X$ and $Y$ has only finitely many irreducible components $Y_{i}$ ($1 \leq i \leq n$), then the closures
$\bar{Y}_{i}$ in $X$ are the irreducible components of $\bar{Y}$.

**(2.1.8)** Let $Y$ be an irreducible space with a unique generic point $y$, let $X$ be a topological space, and let
$f : X \to Y$ be continuous. Then for every irreducible component $Z$ of $X$ meeting $f^{-1}(y)$, $f(Z)$ is dense in
$Y$. The converse need not hold; however, if $Z$ admits a generic point $z$ and $f(Z)$ is dense in $Y$, then necessarily
$f(z) = y$ (2.1.5). Moreover, $Z \cap f^{-1}(y)$ is then the closure of ${z}$ in $f^{-1}(y)$, hence irreducible; and
since every irreducible subset of $f^{-1}(y)$ containing $z$ is contained in $Z$ (2.1.6), $z$ is a generic point of
$Z \cap f^{-1}(y)$. Since every irreducible component of $f^{-1}(y)$ is contained in some irreducible component of $X$,
one sees that if every irreducible component $Z$ of $X$ meeting $f^{-1}(y)$ admits a generic point, then there is a
_bijective correspondence_ between these components and the irreducible components of $f^{-1}(y)$, the generic points of
$Z$ coinciding with those of $Z \cap f^{-1}(y)$.

### 2.2. Noetherian spaces

<!-- label: 0.2.2 -->

**(2.2.1)** A topological space $X$ is called _Noetherian_ if the set of open subsets of $X$ satisfies the _ascending
chain condition_ (equivalently, if the set of closed subsets satisfies the _descending chain condition_). $X$ is called
_locally Noetherian_ if every $x \in X$ admits a neighborhood that is a Noetherian subspace.

**(2.2.2)** Let $E$ be an ordered set satisfying the descending chain condition, and let **P** be a property of elements
of $E$ such that: if $a \in E$ and **P**(x) holds for every $x < a$, then **P**(a) holds. Under these conditions,
**P**(x) _holds for every_ $x \in E$ — "principle of Noetherian induction". Indeed, let $F = {x \in E : \neg P(x)}$; if
$F$ were nonempty, it would have a minimal element $a$, and then **P**(x) would hold for every $x < a$, so **P**(a)
would hold too, a contradiction. We shall apply this principle in particular when $E$ is _a set of closed subsets of a
Noetherian space_.

**(2.2.3)** Every subspace of a Noetherian space is Noetherian. Conversely, every finite union of Noetherian subspaces
of a topological space is Noetherian.

**(2.2.4)** Every Noetherian space is quasi-compact; conversely, a topological space in which every open subset is
quasi-compact is Noetherian.

**(2.2.5)** A Noetherian space has only _finitely many_ irreducible components, as one sees by Noetherian induction.

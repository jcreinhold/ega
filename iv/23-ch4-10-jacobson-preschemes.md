<!-- original page 95 -->

## §10. Jacobson preschemes

We have already had occasion to observe `(5.2.5)` that even excellent preschemes `(7.8.5)` do not always behave like the
"varieties" of classical algebraic geometry, particularly as regards questions of dimension; thus if $X$ is the spectrum
of a complete discrete valuation ring, the set of closed points of $X$ (reduced to a single element) is not everywhere
dense in $X$, and its complement (also reduced to a single element) is an open set everywhere dense in $X$ but of
dimension zero, hence $< \dim(X)$. In this section we examine general conditions under which such phenomena do not
occur; the result is a more satisfactory behaviour, in certain respects, for the relations between dimension,
codimension, depth and codepth in such preschemes `(10.6 and 10.8)`. Moreover, in the preschemes considered, the fact
that the set of closed points is everywhere dense (and even "very dense" `(10.1.3)`) makes it possible to consider only
these points in many proofs; one thus rejoins the classical viewpoint of "algebraic varieties" which, from our
standpoint, are the sets of closed points of algebraic preschemes over a field, and one connects the language of schemes
with that of Serre's "varieties" or "algebraic spaces" `(10.9 and 10.10)`.

### 10.1. Very dense subsets of a topological space

**(10.1.1)**

<!-- label: IV.10.1.1 -->

We say that a subset of a topological space $X$ is *quasi-constructible* if it is a finite union of locally closed
subsets of $X$. We say that a subset $T$ of $X$ is *locally quasi-constructible* if for every $x \in X$, there exists an
open neighbourhood $V$ of $x$ such that $T \cap V$ is quasi-constructible in $V$. It is clear that every
quasi-constructible subset of $X$ is locally quasi-constructible; the converse holds if $X$ is quasi-compact. The
argument of $(0_{III}, 9.1.3)$, dropping the word "retrocompact", shows that the set of quasi-constructible (resp.
locally quasi-constructible) subsets of $X$, which we shall denote by $\mathcal{Q}c(X)$ (resp. $\mathcal{LQ}c(X)$), is
stable under finite union, finite intersection, and complementation. If $f : X \to Y$ is a continuous map, it follows
immediately from these definitions that for every quasi-constructible (resp. locally quasi-constructible) subset $Z$ of
$Y$, $f^{-1}(Z)$ is quasi-constructible (resp. locally quasi-constructible) in $X$.

The constructible (resp. locally constructible) subsets of $X$ are obviously quasi-constructible (resp. locally
quasi-constructible); the converse holds when $X$ is Noetherian (resp. locally Noetherian).

In what follows, we denote respectively by $\mathcal{O}(X)$, $\mathfrak{F}(X)$, $\mathcal{LF}(X)$, $\mathfrak{C}(X)$,
$\mathcal{L}\mathfrak{C}(X)$ the set of subsets of $X$ which are respectively open, closed, locally closed,
constructible, locally constructible.

<!-- original page 96 -->

**Proposition (10.1.2).**

<!-- label: IV.10.1.2 -->

*Let $X$ be a topological space, $X_{0}$ a subset of $X$. The following conditions are equivalent:*

*a) For every locally closed subset $Z \neq \emptyset$ of $X$, one has $Z \cap X_{0} \neq \emptyset$.*

*a') For every closed subset $Z$ of $X$, one has $Z = \overline{Z \cap X_{0}}$.*

*b) For every subset $Z \neq \emptyset$ of $X$ that is locally quasi-constructible, one has $Z \cap X_{0} \neq
\emptyset$.*

*b') For every locally quasi-constructible subset $Z$ of $X$, one has $Z \subset \overline{Z \cap X_{0}}$ (in other
words, $Z \cap X_{0}$ is dense in $Z$).*

*c) The map $U \mapsto U \cap X_{0}$ from $\mathcal{O}(X)$ to $\mathcal{O}(X_{0})$ is injective (hence bijective).*

*c') The map $F \mapsto F \cap X_{0}$ from $\mathfrak{F}(X)$ to $\mathfrak{F}(X_{0})$ is injective (hence bijective).*

*c'') The map $Z \mapsto Z \cap X_{0}$ from $\mathcal{LF}(X)$ to $\mathcal{LF}(X_{0})$ is injective (hence bijective).*

*c''') The map $Z \mapsto Z \cap X_{0}$ from $\mathcal{LQ}c(X)$ to $\mathcal{LQ}c(X_{0})$ is injective.*

*Moreover, when these conditions are satisfied, the map $Z \mapsto Z \cap X_{0}$ from $\mathcal{LQ}c(X)$ to
$\mathcal{LQ}c(X_{0})$ is bijective.*

Note that the surjectivity assertions in c) and c') are trivial; they imply that every locally closed subset of $X_{0}$
is the trace on $X_{0}$ of a locally closed subset of $X$, so the map $\mathcal{LF}(X) \to \mathcal{LF}(X_{0})$ defined
in c'') is also surjective.

We shall prove the implications

```text
  c''') ⟹ c'') ⟹ c') ⟹ c) ⟹ b) ⟹ b') ⟹ a') ⟹ a) ⟹ c''').
```

The first three are trivial. To see that c) implies b), note first that c) entails that $X_{0}$ is dense in $X$.
Replacing $X$ and $X_{0}$ by a suitable open set $U$ of $X$ and by $U \cap X_{0}$ respectively, we may then assume $Z$
is locally closed in $X$, hence $Z = V \cap \complement W$, where $V$ and $W$ are open in $X$; the hypothesis $Z \neq
\emptyset$ means $V \nsubset W$, or equivalently $V \cup W \neq W$. By c), one then has $(V \cup W) \cap X_{0} \neq W
\cap X_{0}$, hence $V \cap X_{0} \nsubset W$, and consequently $(V \cap \complement W) \cap X_{0} \neq \emptyset$.

To see that b) entails b'), it suffices to apply b) to $Z \cap U$, where $U$ is an arbitrary open neighbourhood of a
point of $Z$. Since $Z \cap X_{0} \subset Z$, it is trivial that b') implies a'). To show that a') entails a), note that
if $Z$ is locally closed in $X$, we may write $Z = F - F'$ where $F$ and $F'$ are closed in $X$ and $F' \subset F$;
hence $Z \cap X_{0} = (F \cap X_{0}) - (F' \cap X_{0})$. If one had $Z \cap X_{0} = \emptyset$, one would deduce $F \cap
X_{0} \subset F' \cap X_{0}$, hence $F = F'$ by a'), that is, $Z = \emptyset$.

To see that a) entails c'''), it suffices to show that if $Z \neq \emptyset$ is locally quasi-constructible, then $Z
\cap X_{0} \neq \emptyset$: indeed, the relation $Z' \cap X_{0} = Z'' \cap X_{0}$ is equivalent to $((Z' \cup Z'') - (Z'
\cap Z'')) \cap X_{0} = \emptyset$. In other words, it suffices to prove that a) entails b); moreover, replacing $X$ and
$X_{0}$ by an open set $U$ of $X$ and by $U \cap X_{0}$ respectively, we are reduced to the case where $Z$ is locally
closed in $X$, whence the conclusion.

It remains to show that the map $\mathcal{LQ}c(X) \to \mathcal{LQ}c(X_{0})$ is surjective. Let $Z_{0}$ be a locally
quasi-constructible subset of $X_{0}$: there is a cover $(V_{\alpha})$ of $X_{0}$ by open sets of $X_{0}$ such that
$Z_{0} \cap V_{\alpha}$ is quasi-constructible in $V_{\alpha}$ (and

<!-- original page 97 -->

hence also in $X_{0}$). By c), there exists for each $\alpha$ a unique open set $U_{\alpha}$ of $X$ such that $X_{0}
\cap U_{\alpha} = V_{\alpha}$, and by c'') a unique quasi-constructible set $Z_{\alpha}$ in $X$ such that $Z_{0} \cap
V_{\alpha} = X_{0} \cap Z_{\alpha}$. If $\alpha$ and $\beta$ are any two indices, one has $Z_{\beta} \cap U_{\alpha}
\cap X_{0} = U_{\alpha} \cap Z_{0} \cap V_{\beta} = V_{\alpha} \cap Z_{0} \cap V_{\beta} = Z_{\alpha} \cap X_{0} \cap
V_{\beta} \subset Z_{\alpha} \cap X_{0}$; since $Z_{\beta} \cap U_{\alpha}$ and $Z_{\alpha}$ are quasi-constructible in
$X$, it follows from c'') that $Z_{\beta} \cap U_{\alpha} \subset Z_{\alpha}$. Setting $Z = \bigcup Z_{\alpha}$, one
therefore has $Z \cap U_{\alpha} = Z_{\alpha}$ for every $\alpha$; moreover, since the $V_{\alpha}$ cover $X_{0}$, it
follows from c) that the $U_{\alpha}$ cover $X$, and one sees that $Z$ is locally quasi-constructible in $X$ and $Z_{0}
= Z \cap X_{0}$.

**Definition (10.1.3).**

<!-- label: IV.10.1.3 -->

*When a subset $X_{0}$ of a topological space $X$ satisfies the equivalent conditions of `(10.1.2)`, one says that
$X_{0}$ is **very dense** in $X$.*

It has already been seen in the course of the proof of `(10.1.2)` that $X_{0}$ is then dense in $X$.

**Corollary (10.1.4).**

<!-- label: IV.10.1.4 -->

*If $X_{0}$ is very dense in $X$ and $U$ is an open subset of $X$, then $U \cap X_{0}$ is very dense in $U$. Conversely,
if $(U_{\alpha})$ is an open cover of $X$ such that $U_{\alpha} \cap X_{0}$ is very dense in $U_{\alpha}$ for every
$\alpha$, then $X_{0}$ is very dense in $X$.*

Since every locally closed subset of $U$ is locally closed in $X$, the first assertion follows from criterion a) of
`(10.1.2)`; the same is true of the second, for if $Z \neq \emptyset$ is locally closed in $X$, then $Z \cap U_{\alpha}$
is locally closed in $U_{\alpha}$ for every $\alpha$, and $Z \cap U_{\alpha} \neq \emptyset$ for at least one $\alpha$.

### 10.2. Quasi-homeomorphisms

**Proposition (10.2.1).**

<!-- label: IV.10.2.1 -->

*Let $X_{0}$, $X$ be two topological spaces, $f : X_{0} \to X$ a continuous map. The following conditions are
equivalent:*

*a) The map $U \mapsto f^{-1}(U)$ from $\mathcal{O}(X)$ to $\mathcal{O}(X_{0})$ is bijective.*

*a') The map $F \mapsto f^{-1}(F)$ from $\mathfrak{F}(X)$ to $\mathfrak{F}(X_{0})$ is bijective.*

*b) The topology of $X_{0}$ is the inverse image under $f$ of that of $X$, and $f(X_{0})$ is very dense `(10.1.3)` in
$X$.*

*c) The functor $\mathcal{F} \mapsto f*(\mathcal{F})$ from the category of sheaves of sets (resp. sheaves of abelian
groups) on $X$ to the category of sheaves of sets (resp. sheaves of abelian groups) on $X_{0}$ is an equivalence of
categories.*

It is clear that a) and a') are equivalent, and a) implies that the topology of $X_{0}$ is the inverse image under $f$
of that of $X$. On the other hand, if $f(X_{0})$ is not very dense in $X$, there exist two distinct open sets $U_{1},
U_{2}$ of $X$ such that $U_{1} \cap f(X_{0}) = U_{2} \cap f(X_{0})$, and consequently $f^{-1}(U_{1}) = f^{-1}(U_{2})$,
which shows that a) entails b). Conversely, condition b) implies that the maps $U \mapsto U \cap f(X_{0})$ from
$\mathcal{O}(X)$ to $\mathcal{O}(f(X_{0}))$ and $V \mapsto f^{-1}(V)$ from $\mathcal{O}(f(X_{0}))$ to
$\mathcal{O}(X_{0})$ are bijective, hence so is their composite $U \mapsto f^{-1}(U)$.

To see that a) entails c), it suffices to apply the definition of $f*(\mathcal{F})$ $(0_{I}, 3.7.1)$ and the sheaf
axioms: a) entails that for every open $U$ of $X$, the canonical map $\Gamma(U, \mathcal{F}) \to \Gamma(f^{-1}(U),
f*(\mathcal{F}))$ is a bijection functorial in $\mathcal{F}$, whence c). It remains to show that c) entails b).

<!-- original page 98 -->

Suppose first that $f(X_{0})$ is not very dense in $X$; there then exist two distinct closed subsets $Y \supsetneq Y'$
of $X$ such that $Y \cap f(X_{0}) = Y' \cap f(X_{0})$. Let $\mathcal{F}$ (resp. $\mathcal{F}'$) be the sheaf of abelian
groups on $X$ direct image under the canonical injection $Y \to X$ (resp. $Y' \to X$) of the simple sheaf associated
with the constant presheaf $\mathbb{Z}$ on $Y$ (resp. $Y'$); the definition of $f*$ $(0_{I}, 3.7.1)$ shows that
$f*(\mathcal{F})$ is isomorphic to $f*(\mathcal{F}')$, but $\mathcal{F}$ is not isomorphic to $\mathcal{F}'$, so
condition c) is not satisfied. (Note that the functor $f*$ is then not even faithful, for if $u$ and $v$ are the
identity automorphism and the zero endomorphism of $\mathcal{F} \to \mathcal{F}'$, then $f*(u)$ and $f*(v)$ are equal.)

Let us now show that c) entails that the topology of $X_{0}$ is the inverse image of that of $X$ under $f$. Note that if
condition c) is satisfied for the category of sheaves of sets, it is also satisfied for the category of sheaves of
abelian groups, since it follows immediately from the definitions $(0_{III}, 8.2.5)$ that the latter is none other than
the category of group objects in the category of sheaves of sets. It therefore suffices to prove our assertion assuming
c) is satisfied for the categories of sheaves of abelian groups on $X$ and $X_{0}$. Now, if $\mathbb{Z}_{X}$ denotes the
simple sheaf on $X$ associated with the constant presheaf equal to $\mathbb{Z}$, one has a canonical isomorphism
$\Gamma(X, \mathcal{F}) \simeq \operatorname{Hom}(\mathbb{Z}_{X}, \mathcal{F})$ functorial in $\mathcal{F}$ (same
argument as in $(0_{I}, 5.1.1)$); since it is clear from the definition $(0_{I}, 3.7.1)$ that $f*(\mathbb{Z}_{X}) =
\mathbb{Z}_{X_{0}}$, the hypothesis that $f*$ is an equivalence entails that the canonical homomorphism $\Gamma(X,
\mathcal{F}) \to \Gamma(X_{0}, f*(\mathcal{F}))$ is bijective for every sheaf of abelian groups $\mathcal{F}$ on $X$.
Now let $Y_{0}$ be a closed subset of $X_{0}$; let $\mathcal{F}_{0}$ be the sheaf on $X_{0}$ direct image under the
canonical injection $Y_{0} \to X_{0}$ of the simple sheaf associated with the constant presheaf $\mathbb{Z}$ on $Y_{0}$.
Since $f*$ is an equivalence, $\mathcal{F}_{0}$ is isomorphic to a sheaf of the form $f*(\mathcal{F})$, where
$\mathcal{F}$ is a sheaf of abelian groups on $X$. Consider the section $s_{0}$ of $\mathcal{F}_{0}$ over $X_{0}$ such
that $(s_{0})_{x_{0}} = 1_{(\mathcal{F}_{0})_{x_{0}}}$ if $x_{0} \in Y_{0}$, $(s_{0})_{x_{0}} =
0_{(\mathcal{F}_{0})_{x_{0}}}$ if $x_{0} \notin Y_{0}$. The preceding remarks show that there exists a section $s$ of
$\mathcal{F}$ over $X$ such that $(s_{0})_{x_{0}} = s_{f(x_{0})}$ for every $x_{0} \in X_{0}$ (the fibres
$(\mathcal{F}_{0})_{x_{0}}$ and $\mathcal{F}_{f(x_{0})}$ being canonically identified $(0_{I}, 3.7.1)$); this entails
that $Y_{0}$ is the inverse image under $f$ of the set $Y$ of $x \in X$ such that $s_{x} \neq 0_{x}$, and $Y$ is closed
in $X$. Q.E.D.

**Definition (10.2.2).**

<!-- label: IV.10.2.2 -->

*When a continuous map $f : X_{0} \to X$ satisfies the equivalent conditions of `(10.2.1)`, one says that $f$ is a
**quasi-homeomorphism** of $X_{0}$ into $X$.*

By virtue of `(10.2.1, b))`, to say that a subset $X_{0}$ of a topological space $X$ is very dense in $X$ means that the
canonical injection $X_{0} \to X$ is a quasi-homeomorphism.

**Corollary (10.2.3).**

<!-- label: IV.10.2.3 -->

*The composite of two quasi-homeomorphisms is a quasi-homeomorphism.*

This follows immediately from `(10.2.1, a))`.

**Corollary (10.2.4).**

<!-- label: IV.10.2.4 -->

*Let $f : X \to Y$ be a quasi-homeomorphism, $Y'$ a locally quasi-constructible subset of $Y$, $X' = f^{-1}(Y')$; then
the restriction $f' = f|X' : X' \to Y'$ is a quasi-homeomorphism.*

It is clear by `(10.2.1, b))` that the topology induced on $X'$ by that of $X$ is the inverse image under $f'$ of the
topology induced on $Y'$ by that of $Y$. On the other hand,

<!-- original page 99 -->

let $Z \neq \emptyset$ be a closed subset of $Y'$, and $\xi \in Z$; there is an open neighbourhood $U$ of $\xi$ in $Y$
such that $U \cap Y'$ is a finite union of subsets $Y_{j}'$ closed in $U$; if $j$ is an index such that $\xi \in
Y_{j}'$, then $Z \cap Y_{j}'$ is closed in $U$. Since $f(X) \cap U$ is very dense in $U$ `(10.1.4)`, $Z \cap Y_{j}' \cap
f(X)$ is non-empty `(10.1.2, a))`, and a fortiori $Z \cap f(X)$; but since $Z \subset Y'$, one has $Z \cap f(X) = Z \cap
f'(X')$. Criterion `(10.1.2, a))` thus shows that `f'(X')` is very dense in $Y'$, and one concludes using
`(10.2.1, b))`.

**Corollary (10.2.5).**

<!-- label: IV.10.2.5 -->

*Let $f : X \to Y$ be a continuous map, $(V_{\alpha})$ an open cover of $Y$. If, for every $\alpha$, the restriction
$f^{-1}(V_{\alpha}) \to V_{\alpha}$ of $f$ is a quasi-homeomorphism, then $f$ is a quasi-homeomorphism.*

This follows immediately from criterion `(10.2.1, b))` and from `(10.1.4)`.

**Corollary (10.2.6).**

<!-- label: IV.10.2.6 -->

*Let $f : X \to Y$ be a quasi-homeomorphism, $Y'$ a locally quasi-constructible subset of $Y$, $X' = f^{-1}(Y')$. For
$Y'$ to be quasi-compact (resp. Noetherian, resp. retrocompact in $Y$), it is necessary and sufficient that $X'$ be
quasi-compact (resp. Noetherian, resp. retrocompact in $X$).*

Let us first prove the first two assertions; by virtue of `(10.2.4)`, we may assume $Y' = Y$. To say that $X$ is
quasi-compact (resp. Noetherian) means that for every filtered increasing family $(U_{\alpha})$ in $\mathcal{O}(X)$
having $X$ as largest element (resp. for every filtered increasing family $(U_{\alpha})$ in $\mathcal{O}(X)$), there
exists $\gamma$ such that $U_{\alpha} = U_{\gamma}$ for $\alpha \geqslant \gamma$. Since $U \mapsto f^{-1}(U)$ is a
bijection of $\mathcal{O}(Y)$ onto $\mathcal{O}(X)$, our assertion follows immediately from the preceding remark.

The quasi-compact open sets of $X$ are thus the sets of the form $f^{-1}(U)$ where $U$ is a quasi-compact open set in
$Y$, by `(10.2.1, a))` and what precedes. For $X'$ to be retrocompact in $X$, it is necessary and sufficient that for
every quasi-compact open $U$ in $Y$, $f^{-1}(U) \cap X' = f^{-1}(U \cap Y')$ be quasi-compact $(0_{III}, 9.1.1)$; the
first part of the proof shows that this is equivalent to saying that $U \cap Y'$ is quasi-compact for every
quasi-compact open $U$, that is, that $Y'$ is retrocompact in $Y$.

**Proposition (10.2.7).**

<!-- label: IV.10.2.7 -->

*Let $f : X \to Y$ be a quasi-homeomorphism. Then the map $Z \mapsto f^{-1}(Z)$ from $\mathfrak{P}(Y)$ to
$\mathfrak{P}(X)$ defines by restriction the following bijections (cf. `(10.1.1)` for the notation):*

$$ \mathcal{O}(Y) \simeq \mathcal{O}(X) \mathfrak{F}(Y) \simeq \mathfrak{F}(X) \mathcal{LF}(Y) \simeq \mathcal{LF}(X)
\mathcal{LQ}c(Y) \simeq \mathcal{LQ}c(X) \mathfrak{C}(Y) \simeq \mathfrak{C}(X) \mathcal{L}\mathfrak{C}(Y) \simeq
\mathcal{L}\mathfrak{C}(X). $$

For the first two, this is none other than the definition `(10.2.2)`; since the topology of $X$ is the inverse image
under $f$ of that of $f(X)$, the last five maps,

<!-- original page 100 -->

where one replaces $Y$ by $f(X)$, are bijective. One may therefore (by `(10.2.1, b))`) restrict to the case where $X$ is
a very dense subspace of $Y$, and the fact that the maps $\mathfrak{F}(Y) \to \mathfrak{F}(X)$, $\mathcal{LF}(Y) \to
\mathcal{LF}(X)$, $\mathcal{LQ}c(Y) \to \mathcal{LQ}c(X)$ are bijective has already been proved `(10.1.2)`. Every
locally constructible subset being locally quasi-constructible, the maps $\mathfrak{C}(Y) \to \mathfrak{C}(X)$ and
$\mathcal{L}\mathfrak{C}(Y) \to \mathcal{L}\mathfrak{C}(X)$ are injective; in addition, for every open $U \subset Y$,
the restriction $f^{-1}(U) \to U$ of $f$ is a quasi-homeomorphism `(10.2.4)`, so if one shows that $\mathfrak{C}(Y) \to
\mathfrak{C}(X)$ is surjective, the same will be true of $\mathcal{L}\mathfrak{C}(Y) \to \mathcal{L}\mathfrak{C}(X)$.
But by `(10.2.6)`, every open retrocompact subset $Z$ in $X$ is of the form $f^{-1}(T)$, where $T$ is open retrocompact
in $Y$; this evidently proves the surjectivity of $\mathfrak{C}(Y) \to \mathfrak{C}(X)$.

**Remarks (10.2.8).**

<!-- label: IV.10.2.8 -->

*(i)* It was seen in the proof of `(10.2.1)` that if $f$ is a quasi-homeomorphism, the canonical map

```text
(10.2.8.1)        Γ(Y, ℱ) → Γ(X, f*(ℱ))
```

is an isomorphism of abelian groups functorial in $\mathcal{F}$ in the category of sheaves of abelian groups on $Y$.
Since $f*$ is exact in this category $(0_{I}, 3.7.2)$, this implies that the canonical homomorphisms `(T, 3.2.2)`

```text
  H^i(Y, ℱ) → H^i(X, f*(ℱ))
```

are bijective for every $i$.

*(ii)* If $f : X \to Y$ is a continuous map and $\mathcal{F}, \mathcal{G}$ are two sheaves of abelian groups on $Y$, one
has $f*(\mathcal{F} \otimes_{\mathbb{Z}_{Y}} \mathcal{G}) = f*(\mathcal{F}) \otimes_{\mathbb{Z}_{X}} f*(\mathcal{G})$ up
to canonical isomorphism $(0_{I}, 4.3.3)$. One concludes that if $f$ is a quasi-homeomorphism, $f*$ is also an
equivalence of the category of sheaves of rings on $Y$ and the category of sheaves of rings on $X$; the datum of a
ringed-space structure on $Y$ is thus equivalent to that of a ringed-space structure on $X$.

Given two ringed spaces $(X, \mathcal{O}_{X})$, $(Y, \mathcal{O}_{Y})$, we shall say that a morphism of ringed spaces $f
= (\psi, \theta) : (X, \mathcal{O}_{X}) \to (Y, \mathcal{O}_{Y})$ is a *quasi-isomorphism* if $\psi$ is a
quasi-homeomorphism of $X$ into $Y$ and $\theta\sharp : \psi*(\mathcal{O}_{Y}) \to \mathcal{O}_{X}$ is an isomorphism of
sheaves of rings; when this is so, the ringed space $(X, \mathcal{O}_{X})$ is entirely determined, up to isomorphism, by
$(Y, \mathcal{O}_{Y})$, the space $X$, and the quasi-homeomorphism $\psi$ (which one may take arbitrary). When $f$ is a
quasi-isomorphism of ringed spaces, the functor

$$ \mathcal{F} \mapsto f*(\mathcal{F}) $$

is an equivalence of the category of $\mathcal{O}_{Y}$-Modules with that of $\mathcal{O}_{X}$-Modules, since
$f*(\mathcal{F})$ is here canonically identified with $\psi*(\mathcal{F})$. One concludes, for example, isomorphisms of
bi-$\partial$-functors

```text
  Ext^p_{𝒪_Y}(ℱ, 𝒢) ≃ Ext^p_{𝒪_X}(f*(ℱ), f*(𝒢)).
```

In general, one may say that the usual constructions of sheaf theory and homological algebra, performed on the ringed
space $Y$ or on the ringed space $X$, are equivalent.

<!-- original page 101 -->

### 10.3. Jacobson spaces

**Definition (10.3.1).**

<!-- label: IV.10.3.1 -->

*One says that a topological space $X$ is a **Jacobson space** if the set $X_{0}$ of closed points of $X$ is very dense
in $X$ (in other words, if the canonical injection $X_{0} \to X$ is a quasi-homeomorphism).*

This means therefore `(10.1.2)` that every locally closed (or only locally quasi-constructible) subset $Z \neq
\emptyset$ of $X$ contains a closed point of $X$, or also that *every closed subset of $X$ is the closure of the set of
its closed points*.

**Proposition (10.3.2).**

<!-- label: IV.10.3.2 -->

*Let $X$ be a Jacobson space, $Z$ a locally quasi-constructible subset of $X$; then the subspace $Z$ of $X$ is a
Jacobson space, and for a point of $Z$ to be closed in $Z$, it is necessary and sufficient that it be closed in $X$.*

If $X_{0}$ is the set of closed points of $X$, then $Z \cap X_{0}$ is very dense in $Z$ by virtue of `(10.2.4)` applied
to the injection $i : X_{0} \to X$; since the set $Z_{0}$ of closed points of $Z$ obviously contains $Z \cap X_{0}$, it
is a fortiori very dense in $Z$, so $Z$ is a Jacobson space. Let us now show that one has in fact $Z_{0} = Z \cap
X_{0}$; let $x \in Z$ be a point closed in $Z$; let $\overline{x}$ be its closure in $X$; then $\overline{x} \cap Z =
{x}$ is therefore a locally quasi-constructible subset of $X$, and since its intersection with $X_{0}$ is non-empty
`(10.1.2)`, one has $x \in X_{0}$.

**Proposition (10.3.3).**

<!-- label: IV.10.3.3 -->

*Let $X$ be a topological space, $(U_{\alpha})$ an open cover of $X$. For $X$ to be a Jacobson space, it is necessary
and sufficient that each of the subspaces $U_{\alpha}$ be one.*

The condition is necessary by virtue of `(10.3.2)`. Conversely, let us first show that the hypothesis that the
$U_{\alpha}$ are Jacobson spaces entails that for a point $x \in U_{\alpha}$ to be closed in $X$, it suffices that it be
closed in $U_{\alpha}$. It suffices in fact to see that this condition entails that $x$ is also closed in each of the
$U_{\beta}$ that contain it; but $U_{\alpha} \cap U_{\beta}$ is open in $U_{\alpha}$, so $x$ is closed in $U_{\alpha}
\cap U_{\beta}$, and by `(10.3.2)`, $x$ is also closed in $U_{\beta}$, which completes the proof.

### 10.4. Jacobson preschemes and Jacobson rings

**Definition (10.4.1).**

<!-- label: IV.10.4.1 -->

*One says that a prescheme $X$ is a **Jacobson prescheme** if the underlying topological space $X$ is a Jacobson space.
One says that a ring $A$ is a **Jacobson ring** if $\operatorname{Spec}(A)$ is a Jacobson prescheme.*

Every closed subset of $X = \operatorname{Spec}(A)$ is of the form $Z = V(\mathfrak{a})$, where $\mathfrak{a}$ is an
ideal equal to its radical, and the set $X_{0}$ of closed points of $X$ is the set of maximal ideals of $A$; to say that
$Z \cap X_{0}$ is dense in $Z$ means therefore that $\mathfrak{a}$ is an intersection of maximal ideals `(I, 1.1.4)`;
since $\mathfrak{a}$ is an intersection of prime ideals, this amounts to saying that every prime ideal of $A$ is an
intersection of maximal ideals; by virtue of `(10.3.1)` and `(10.1.2)`, the usual definition of Jacobson rings
`(Bourbaki, Alg. comm., chap. V, §3, n° 4, déf. 1)` therefore coincides with definition `(10.4.1)`.

<!-- original page 102 -->

**Proposition (10.4.2).**

<!-- label: IV.10.4.2 -->

*Let $X$ be a prescheme, $(U_{\alpha})$ a cover of $X$ by affine open sets. For $X$ to be a Jacobson prescheme, it is
necessary and sufficient that the rings $\Gamma(U_{\alpha}, \mathcal{O}_{X})$ of the $U_{\alpha}$ be Jacobson rings.*

This follows from `(10.3.3)` and from definition `(10.4.1)`.

**(10.4.3)**

<!-- label: IV.10.4.3 -->

A discrete prescheme is a Jacobson prescheme; an Artinian ring is therefore a Jacobson ring. Every principal ring having
infinitely many maximal ideals (for example $\mathbb{Z}$) is a Jacobson ring; a local Noetherian ring $A$ is a Jacobson
ring if and only if its maximal ideal is its only prime ideal, that is, if $A$ is Artinian. Every subprescheme of a
Jacobson prescheme is a Jacobson prescheme by virtue of `(10.3.2)`.

**Proposition (10.4.4).**

<!-- label: IV.10.4.4 -->

*Let $B$ be an integral ring. The following conditions are equivalent:*

*a) There exists $f \neq 0$ in $B$ such that $B_{f}$ is a field.*

*b) The field of fractions of $B$ is a $B$-algebra of finite type.*

*c) There exists a field $K$ containing $B$ which is a $B$-algebra of finite type.*

*d) The generic point of $\operatorname{Spec}(B)$ is isolated in $\operatorname{Spec}(B)$.*

It is clear that d) is equivalent to a), since d) means that there exists $f \neq 0$ in $B$ such that $D(f)$ is reduced
to the generic point of $\operatorname{Spec}(B)$. It is trivial that a) entails b) and that b) entails c). Finally, c)
entails a), by virtue of `(Bourbaki, Alg. comm., chap. V, §3, n° 1, cor. 2 of th. 1)`.

**Proposition (10.4.5).**

<!-- label: IV.10.4.5 -->

*Let $A$ be a ring. The following conditions are equivalent:*

*a) $A$ is a Jacobson ring.*

*b) For every non-maximal prime ideal $\mathfrak{p}$ of $A$ and every $f \neq 0$ in $B = A/\mathfrak{p}$, $B_{f}$ is not
a field.*

*b') Every $A$-algebra of finite type $K$ which is a field is a finite $A$-algebra.*

It is known that a) entails b') `(Bourbaki, Alg. comm., chap. V, §3, n° 4, cor. 3 of th. 3)`. Moreover, the kernel of
the homomorphism $A \to K$ is then a maximal ideal $\mathfrak{m}$ of $A$, and $K$ is a finite extension of
$A/\mathfrak{m}$ (loc. cit.). It is trivial that b') entails b), since $A/\mathfrak{p} = B$ is not a field, every
$B$-algebra of finite type is an $A$-algebra of finite type, and $B_{f}$ is a $B$-algebra of finite type. It remains to
see that b) implies a). We shall use the following lemma:

**Lemma (10.4.5.1).**

<!-- label: IV.10.4.5.1 -->

*Let $X$ be a topological space having the following property: for every locally closed subset $Z \neq \emptyset$ of
$X$, there exists a subset $Z'$ of $Z$, locally closed in $X$ (or in $Z$, which amounts to the same thing), and a point
$x \in Z'$, closed in $Z'$. Then, for $X$ to be a Jacobson space, it is necessary and sufficient that no non-closed
point $x$ of $X$ be isolated in $\overline{x}$.*

If $X$ is a Jacobson space, a non-closed point $x$ of $X$ cannot be isolated in $\overline{x}$, for this would mean that
there exists an open set $U$ of $X$ such that $U \cap \overline{x} = {x}$; but $U \cap \overline{x}$ is locally closed
in $X$ and would contain no point closed in $X$, which is contrary to the hypothesis that $X$ is a Jacobson space.
Conversely, suppose the condition of the statement is satisfied; then the set of closed points of $X$ is identical with
the set $X_{0}$ of $x \in X$ that are isolated in $\overline{x}$; but it follows from `(5.1.10.1)` that

<!-- original page 103 -->

this set is very dense in $X$, so $X$ is a Jacobson space by definition.

Recall `(5.1.10)` that the hypothesis made on $X$ in `(10.4.5.1)` is always satisfied when $X$ is the space underlying a
prescheme.

Returning then to the proof of `(10.4.5)`, condition b) entails that for every non-closed point $x$ of
$\operatorname{Spec}(A)$, the generic point $x$ of $\operatorname{Spec}(A/\mathfrak{p}) = V(\mathfrak{p}) =
\overline{x}$ is not isolated in $\overline{x}$, so b) entails a) by virtue of the lemma `(10.4.5.1)` and `(10.4.4)`.

**Corollary (10.4.6).**

<!-- label: IV.10.4.6 -->

*Every algebra of finite type $B$ over a Jacobson ring $A$ is a Jacobson ring, and the inverse image in $A$ of every
maximal ideal of $B$ is a maximal ideal of $A$. In particular, every algebra of finite type over a field or over
$\mathbb{Z}$ is a Jacobson ring.*

A $B$-algebra of finite type $K$ that is a field is also an $A$-algebra of finite type, hence an $A$-module of finite
type and a fortiori a $B$-module of finite type, whence the first assertion; the second was proved in the course of the
proof of `(10.4.5)`, applied to $K = B/\mathfrak{m}$.

**Corollary (10.4.7).**

<!-- label: IV.10.4.7 -->

*If $X$ is a Jacobson prescheme, $f : Y \to X$ a morphism locally of finite type, then $Y$ is a Jacobson prescheme and
the image under $f$ of every closed point in $Y$ is a closed point in $X$.*

The question being local on $X$ and on $Y$, one is reduced to the case where $X$ and $Y$ are affine, and the corollary
then follows from `(10.4.6)`.

**Corollary (10.4.8).**

<!-- label: IV.10.4.8 -->

*If $k$ is an algebraically closed field, $X$ a $k$-prescheme locally of finite type, the set of points of $X$ rational
over $k$ is very dense in $X$.*

Indeed, $X$ is a Jacobson prescheme `(10.4.7)` and the closed points of $X$ are exactly the points rational over $k$
`(I, 6.4.2)`.

**(10.4.9)**

<!-- label: IV.10.4.9 -->

The fact that preschemes locally of finite type over a field or over $\mathbb{Z}$ are Jacobson preschemes is
particularly important, in view of the possibility of reducing many questions of algebraic geometry to this case
`(8.1.2, c))`. We shall give two examples.

**Applications (10.4.10). I. Proof of `(6.15.9)`.**

<!-- label: IV.10.4.10 -->

Let $k$ be a separably closed field, $X$ a $k$-prescheme locally of finite type over $k$ and unibranch. It is known that
the integral closure of an integral $k$-algebra of finite type $A$ in a finite extension of its field of fractions is a
finite $A$-algebra `(Bourbaki, Alg. comm., chap. V, §3, n° 2, th. 2)`, so every $A$-algebra of finite type is a
universally Japanese ring; one concludes that the set of points $x \in X$ where $X$ is geometrically unibranch is
locally constructible `(9.7.10)`. But the hypothesis and the lemma `(6.15.8)` entail that this set contains all closed
points of $X$. The conclusion therefore results from `(10.4.6)`, `(10.3.1)`, and the bijectivity of the canonical map
$\mathcal{L}\mathfrak{C}(X) \to \mathcal{L}\mathfrak{C}(X_{0})$ (where $X_{0}$ is the set of closed points of $X$)
`(10.2.7)`.

**Applications. II. Proposition (10.4.11).**

<!-- label: IV.10.4.11 -->

*Let $S$ be a prescheme, $X$ an $S$-prescheme of finite type. Every $S$-endomorphism of $X$ that is radicial is
surjective (hence bijective).*

<!-- original page 104 -->

Let $f : X \to S$ be the structure morphism, $g : X \to X$ the $S$-endomorphism under consideration, and, for every $s
\in S$, let $g_{s}$ be the morphism deduced from $g$ by the base change $\operatorname{Spec}(k(s)) \to S$, which is a
$k(s)$-endomorphism of the fibre $f^{-1}(s) = X \times_{S} \operatorname{Spec}(k(s))$.

To prove that $g$ is surjective, it suffices to prove that $g_{s}$ is surjective for every $s \in S$, so one may (by
virtue of `(I, 3.5.7)`) assume $S = \operatorname{Spec}(k)$ is the spectrum of a field $k$, in which case $f$ is a
morphism of finite presentation, since $S$ is Noetherian. Applying `(8.9.1)` and `(8.10.5, (vii))`, one is reduced to
the case where $S = \operatorname{Spec}(A)$, where $A$ is a $\mathbb{Z}$-subalgebra of finite type of $k$. Now $X$ is
then a Jacobson prescheme `(10.4.7)`, and $g(X)$ is constructible in $X$ `(1.8.5)`, so to prove that $g(X) = X$, it
suffices to show that $g(X)$ contains all closed points of $X$ `(10.3.1)`.

**Lemma (10.4.11.1).**

<!-- label: IV.10.4.11.1 -->

*Let $Y$ be a $\mathbb{Z}$-prescheme of finite type.*

*(i) For a point $y \in Y$ to be closed in $Y$, it is necessary and sufficient that $k(y)$ be a finite field.*

*(ii) For every prime number $p$ and every integer $d \geqslant 1$, the set of points $y \in Y$ such that $k(y)$ is an
extension of $\mathbb{F}_{p}$ whose degree divides $d$ is finite.*

Assertion (i) follows from the fact that the image of a closed point $y \in Y$ in $\operatorname{Spec}(\mathbb{Z})$ is a
closed point `(10.4.7)`, in other words a prime number, and from `(I, 6.4.2)`. On the other hand, since $Y$ is a finite
union of affine open sets of finite type over $\mathbb{Z}$, one may restrict, to prove (ii), to the case where $Y =
\operatorname{Spec}(C)$, where $C$ is a $\mathbb{Z}$-algebra of finite type. Now the points $y \in Y$ such that the
degree of $k(y)$ over $\mathbb{F}_{p}$ divides $d$ correspond bijectively to the homomorphisms $C \to
\mathbb{F}_{p^{d}}$; but if $(t_{i})$ is a system of generators of the $\mathbb{Z}$-algebra $C$, every homomorphism of
$C$ is determined by its values on the elements $t_{i}$, and consequently there are only finitely many homomorphisms of
$C$ into a finite field.

This being so, $X$ is a $\mathbb{Z}$-prescheme of finite type; let $T_{p,d}$ be the set of closed points $z \in X$ such
that $k(z)$ is an extension of $\mathbb{F}_{p}$ of degree dividing $d$; it follows from `(10.4.11.1)` that the set
$T_{p,d}$ is finite and that the set of closed points of $X$ is the union of the $T_{p,d}$. Moreover, if $z \in T_{p,d}$
and if $h$ is any endomorphism of $X$, $k(h(z))$ is isomorphic to a subfield of $k(z)$, so $h(z) \in T_{p,d}$, in other
words $T_{p,d}$ is stable under every endomorphism of $X$. Since $g$ is by hypothesis injective, its restriction to
$T_{p,d}$ is bijective since $T_{p,d}$ is finite, which completes the proof of the proposition.

We shall see later `(17.9.7)` that when one further assumes, on the one hand, that $X$ is an $S$-prescheme of finite
presentation, and on the other hand, that $g$ is a monomorphism, then one can affirm that $g$ is an automorphism of $X$.

### 10.5. Noetherian Jacobson preschemes

**Proposition (10.5.1).**

<!-- label: IV.10.5.1 -->

*Let $B$ be a Noetherian integral ring. The equivalent conditions a) to d) of `(10.4.4)` are then also equivalent to the
following:*

*e) $\operatorname{Spec}(B)$ is finite.*

*f) $B$ is a semi-local ring of dimension $\leqslant 1$.*

It follows in fact from the Artin-Tate theorem `(0, 16.3.3)` that the conditions a) and f) are equivalent. The condition
f) implies that $\operatorname{Spec}(B)$ is the union of the finite set

<!-- original page 105 -->

of its closed points and its generic point, so f) implies e) without supposing $A$ Noetherian. Finally e) implies d)
without supposing $A$ Noetherian, for the generic point $x$ of $X$ is the complement of the union of the closures
$\overline{y}$, where $y$ ranges over the set of points $y \neq x$, and since these points are finite in number, ${x}$
is the complement of a closed set in $X$.

**Corollary (10.5.2).**

<!-- label: IV.10.5.2 -->

*Let $A$ be a Noetherian ring. For $A$ to be a Jacobson ring, it is necessary and sufficient that there exist no prime
ideal $\mathfrak{p}$ of $A$ such that $A/\mathfrak{p}$ be a semi-local ring of dimension `1`.*

This follows immediately from `(10.5.1)` and from condition b) of `(10.4.5)`, the prime ideals $\mathfrak{p}$ of $A$
such that $A/\mathfrak{p}$ is semi-local of dimension `0` being the maximal ideals of $A$.

**Corollary (10.5.3).**

<!-- label: IV.10.5.3 -->

*Let $X$ be a Noetherian irreducible prescheme. The following conditions are equivalent:*

*a) The generic point of $X$ is isolated.*

*b) $X$ is finite.*

*c) $X$ is of dimension $\leqslant 1$ and its set of closed points is finite.*

There exist by hypothesis a finite number of irreducible affine open sets $U_{i}$ ($1 \leqslant i \leqslant n$) covering
$X$, each of which therefore contains the generic point of $X$; it suffices to prove the equivalence of a), b), and c)
for each of the $(U_{i})_{red}$ (taking `(0, 14.1.7)` into account). But this equivalence then follows from `(10.5.1)`.

**Remark (10.5.4).**

<!-- label: IV.10.5.4 -->

A Noetherian prescheme $X$ satisfying the equivalent conditions of `(10.5.3)` is not necessarily an affine scheme; in
fact, it may even fail to be separated. One has an example by replacing, in example `(I, 5.5.11)` of the "affine line
with doubled point", `X_1` and `X_2` by the spectrum of the discrete valuation ring $(K[t])_{(t)}$, and $U_{12}$ and
$U_{21}$ by the open set reduced to the generic point in `X_1` and `X_2` respectively; the non-separated prescheme $X$
that one obtains has exactly 3 points.

**Proposition (10.5.5).**

<!-- label: IV.10.5.5 -->

*Let $X$ be a Noetherian prescheme.*

*(i) The set $X_{0}$ of points $x \in X$ such that $\overline{x}$ is finite is very dense in $X$.*

*(ii) For $X$ to be a Jacobson prescheme, it is necessary and sufficient that there exist no subprescheme of $X$
isomorphic to the spectrum of an integral semi-local ring of dimension `1`.*

The condition that $\overline{x}$ be finite is equivalent here `(10.5.3)` to the fact that $x$ be isolated in
$\overline{x}$, $\overline{x}$ being the space underlying a (Noetherian) subprescheme of $X$; assertion (i) therefore
follows from `(5.1.10.1)`. Similarly, taking `(10.4.5.1)` into account, to prove assertion (ii), note that for a
non-closed point $x$ of $X$ to belong to $X_{0}$, it is necessary and sufficient that the closed integral subprescheme
$Y$ of $X$ having $\overline{x}$ as underlying space be of dimension `1` and finite, hence a finite union of (open in
$Y$) affine subpreschemes $U_{i}$ that are spectra of integral semi-local rings of dimension `1`. Conversely, if there
is a subprescheme $Z$ of $X$ that is the spectrum of an integral semi-local ring of dimension `1`, then $Z$ is not a
Jacobson prescheme `(10.5.2)`, so neither is $X$ `(10.3.2)`.

<!-- original page 106 -->

**Remark (10.5.6).**

<!-- label: IV.10.5.6 -->

Assertion (ii) of `(10.5.5)` remains valid when $X$ is locally Noetherian: indeed, if $(V_{\alpha})$ is a cover of $X$
by (Noetherian) affine open sets, every subprescheme of a $V_{\alpha}$ is a subprescheme of $X$; conversely, if a
subprescheme $Z$ of $X$ is isomorphic to the spectrum of an integral semi-local ring of dimension `1`, there is some
$\alpha$ such that $V_{\alpha} \cap Z$ contains an affine open $U$ of $Z$ not reduced to the generic point of $Z$, which
is therefore also the spectrum of an integral semi-local ring of dimension `1`. One concludes by means of `(10.3.3)`.

**Proposition (10.5.7).**

<!-- label: IV.10.5.7 -->

*Let $X$ be a locally Noetherian prescheme, $Y$ a closed subset of $X$ such that every non-empty closed subset of $X$
meets $Y$. Then the prescheme induced on the open set $X - Y$ is a Jacobson prescheme.*

Apply criterion `(10.5.5, (ii))`, and suppose there is a subprescheme $Z$ of $X - Y$ that is the spectrum of an integral
semi-local ring of dimension `1`, the generic point $z$ of $Z$ being isolated in $Z$ (or in the closure $\overline{Z}$
of $Z$ in $X$), and $Z$ being distinct from ${z}$. Let $y \neq z$ be a point of $Z$; since it does not belong to $Y$, it
is not closed in $X$, and its closure $\overline{y}$ in $X$ meets $Y$ at a point $x \neq y$ which is therefore a
specialization of $y$. The existence of the chain ${x} \subset \overline{y} \subset \overline{z}$ shows then that the
dimension of $\overline{z}$ would be $\geqslant 2$, and the same would be true of the dimension of $U \cap
\overline{z}$, where $U$ is an affine (hence Noetherian) open neighbourhood of $x$ in $X$. But this contradicts the fact
that the generic point $z$ of $U \cap \overline{z}$ is isolated in $U \cap \overline{z}$ `(10.5.3)`.

**Corollary (10.5.8).**

<!-- label: IV.10.5.8 -->

*Let $A$ be a Noetherian ring; for every element $f$ of the radical $\mathfrak{N}$ of $A$, the ring $A_{f}$ is a
Jacobson ring, and the open set $\operatorname{Spec}(A) - V(\mathfrak{N})$ is a Jacobson scheme.*

If $X = \operatorname{Spec}(A)$, $Y = V(\mathfrak{J})$, where $\mathfrak{J}$ is an ideal of $A$, to say that every
non-empty closed subset of $X$ meets $Y$ is equivalent $(0_{I}, 2.1.3)$ to saying that $Y$ contains all closed points of
$X$, or again that $\mathfrak{J}$ is contained in the radical $\mathfrak{N}$ of $A$. If $f \in \mathfrak{N}$, the open
set $D(f)$ therefore does not meet $V(\mathfrak{N})$, and is a Jacobson space by virtue of `(10.5.7)`.

**Corollary (10.5.9).**

<!-- label: IV.10.5.9 -->

*Let $A$ be a local Noetherian ring, $\mathfrak{m}$ its maximal ideal, $X = \operatorname{Spec}(A)$, $Y = X -
{\mathfrak{m}}$; then $Y$ is a Jacobson scheme, whose closed points are the prime ideals $\mathfrak{p} \in
\operatorname{Spec}(A)$ such that $\dim(A/\mathfrak{p}) = 1$.*

The first assertion is a particular case of `(10.5.8)`; on the other hand the closed points of $Y$ are the prime ideals
$\mathfrak{p}$ of $A$ which are maximal elements in the set of prime ideals $\neq \mathfrak{m}$, which, by definition of
dimension, means that $\dim(A/\mathfrak{p}) = 1$.

**Proposition (10.5.10).**

<!-- label: IV.10.5.10 -->

*Let $A$ be a reduced complete local Noetherian ring which is not a field. Then the finite intersections of the kernels
of the local homomorphisms of $A$ into discrete valuation rings $V$ making $V$ a finite $A$-algebra form a filter base
tending to `0` for the adic topology of $A$.*

It suffices `(Bourbaki, Alg. comm., chap. III, §2, n° 7, prop. 8)` to prove that the intersection of the kernels
considered in the statement is reduced to `0`. Suppose first that $A$ is integral and of dimension `1`; by virtue of
Nagata's theorem `(0, 23.1.5 and 23.1.6)`, the integral closure $A'$ of $A$ is an integral complete local ring,

<!-- original page 107 -->

integrally closed, of dimension `1`, and a finite $A$-algebra; it is therefore a discrete valuation ring, and the
proposition follows immediately in this case.

Let us pass to the general case; let $x$ be the closed point of $X = \operatorname{Spec}(A)$, and set $Y = X - {x}$; one
knows `(10.5.9)` that $Y$ is a Jacobson prescheme. Let us show that this entails that the intersection of the prime
ideals $\mathfrak{p}$ of $A$ such that $\dim(A/\mathfrak{p}) = 1$ is reduced to `0`; the proposition will follow since,
for each of these ideals $\mathfrak{p}$, the intersection of the kernels of the local homomorphisms of $A/\mathfrak{p}$
into discrete valuation rings $V$, making $V$ a finite $(A/\mathfrak{p})$-algebra, is reduced to `0`. But to say that
the intersection of these prime ideals is reduced to `0` means that the set of these ideals is dense in $X$, or also in
$Y$ (since $Y$ is dense in $X$), and this follows immediately from `(10.5.9)`.

### 10.6. Dimension in Jacobson preschemes

The results of this number sharpen, in certain cases, and generalize results of §5.

**Proposition (10.6.1).**

<!-- label: IV.10.6.1 -->

*Let $S$ be a locally Noetherian prescheme satisfying in addition the following conditions: 1° $S$ is a Jacobson
prescheme; 2° for every $s \in S$, $\mathcal{O}_{S,s}$ is universally catenary `(5.6.2)`; 3° every irreducible component
$S'$ of $S$ is equicodimensional (in other words, for every closed point $s$ of $S'$ and every subprescheme of $S$
having $S'$ as underlying space, one has $\dim(S') = \dim(\mathcal{O}_{S',s})$). One then has the following properties:*

*(i) For every morphism $g : X \to S$ locally of finite type, $X$ satisfies the preceding conditions 1°, 2°, and 3°. In
particular, if $X$ is equidimensional (for example if $X$ is irreducible), then $X$ is biequidimensional (in other
words, $X$ is catenary and for every closed point $x$ of $X$, one has $\dim(\mathcal{O}_{X,x}) = \dim(X)$
`(0, 14.3.3)`).*

*(ii) Let $X$, $Y$ be two $S$-preschemes locally of finite type over $S$, $f : X \to Y$ an $S$-morphism; suppose $X$
irreducible and $f$ dominant. If $\xi$ (resp. $\eta$) is the generic point of $X$ (resp. $Y$) and $e =
\dim(f^{-1}(\eta)) = deg.tr_{k(\eta)} k(\xi)$, one has*

$$ (10.6.1.1) \dim(X) = \dim(Y) + e. $$

*(iii) Let $X$, $Y$ be two $S$-preschemes locally of finite type over $S$, $f : X \to Y$ an $S$-morphism, $n$ an integer
$\geqslant 0$ such that one has $\dim(f^{-1}(y)) \leqslant n$ (resp. $\dim(f^{-1}(y)) \geqslant n$) for every $y \in Y$.
Then one has*

$$ (10.6.1.2) \dim(X) \leqslant \dim(Y) + n $$

*(resp.*

```text
(10.6.1.3)        dim(X) ⩾ dim(Y) + n).
```

(i) Property 1° for $X$ follows from `(10.4.7)`. For every $x \in X$, $\mathcal{O}_{X,x}$ is the local ring at a prime
ideal of an $\mathcal{O}_{S,g(x)}$-algebra of finite type, and the homomorphism $\mathcal{O}_{S,g(x)} \to
\mathcal{O}_{X,x}$

<!-- original page 108 -->

is local; so `(5.6.3, (iv))` $\mathcal{O}_{X,x}$ is universally catenary. To prove that $X$ satisfies condition 3°,
consider several cases:

(a) $X$ is a closed irreducible subprescheme of $S$; let $S'$ be an irreducible component of $S$ containing $X$, $\xi$
the generic point of $X$, $x$ a closed point of $X$; for every $s \in S'$, $\mathcal{O}_{S',s}$, a quotient of
$\mathcal{O}_{S,s}$, is catenary `(5.6.1)`, so conditions 2° and 3° entail that $S'$ is biequidimensional `(0, 14.3.3)`.
By virtue of `(5.1.2)` and `(0, 14.3.3.2)`, one therefore has

```text
  dim(𝒪_{X,x}) = dim(𝒪_{S,x}) − dim(𝒪_{S,ξ}) = dim(S') − dim(𝒪_{S,ξ})
```

which shows that $\dim(\mathcal{O}_{X,x})$ does not depend on the closed point $x$ considered, whence the assertion in
this case `(5.1.4)`.

(b) $X$ is irreducible and $g$ dominant. Then, for every closed point $x$ of $X$, $g(x)$ is closed in $S$ by `(10.4.7)`;
since $\mathcal{O}_{S,g(x)}$ is universally catenary, it follows from `(5.6.5.3)` that one has

$$ \dim(\mathcal{O}_{X,x}) = \dim(\mathcal{O}_{S,g(x)}) + e $$

where $e = \dim(g^{-1}(\zeta))$, $\zeta$ being the generic point of $S$. Since $\dim(S) = \dim(\mathcal{O}_{S,s})$ by
virtue of condition 3° for $S$, one has $\dim(\mathcal{O}_{X,x}) = \dim(S) + e$ for every closed point $x \in X$; this
proves condition 3° for $X$ `(5.1.4)`, and at the same time the formula

$$ (10.6.1.4) \dim(X) = \dim(S) + e. $$

(c) General case. Considering a reduced subprescheme $X'$ of $X$ having an irreducible component of $X$ as underlying
space, one is reduced to the case where $X$ is integral; using `(I, 5.2.2)` and case (a) proved above, one may then
replace $S$ by the reduced subprescheme having $g(X)$ as underlying space; one is then reduced to case (b), and this
completes the proof of (i).

(ii) The morphism $f$ being locally of finite type `(1.3.4)`, one may apply the results of (i) replacing $S$ by $Y$;
moreover, since $X$ is irreducible and $f$ dominant, one may also replace $S$ by $Y$ in `(10.6.1.4)`, which gives
`(10.6.1.1)`.

(iii) The assertion concerning the case where $\dim(f^{-1}(y)) \leqslant n$ for every $y \in Y$ has already been proved
under more general hypotheses in `(5.6.7)`. Suppose that $\dim(f^{-1}(y)) \geqslant n$ for every $y \in Y$, and consider
a generic point $\eta$ of an irreducible component $Y'$ of $Y$; there exists at least one irreducible component $Z$ of
$f^{-1}(\eta)$ of dimension $\geqslant n$; if $\xi$ is the generic point of $Z$, then $\xi$ is also the generic point of
an irreducible component $X'$ of $X$ such that $f(X')$ is dense in $Y'$ $(0_{I}, 2.1.8)$. Consider the reduced
subpreschemes of $X$, $Y$ having respectively $X'$, $Y'$ as underlying spaces, and the restriction $X' \to Y'$ of $f$
`(I, 5.2.2)`; it then follows from (ii) that $\dim(X') \geqslant \dim(Y') + n$, and a fortiori $\dim(X) \geqslant
\dim(Y') + n$; this being true for every irreducible component $Y'$ of $Y$, one concludes the inequality `(10.6.1.2)`.

**Corollary (10.6.2).**

<!-- label: IV.10.6.2 -->

*Suppose that $X$ satisfies conditions 1°, 2°, and 3° of `(10.6.1)`. Then, for every open $U$ dense in $X$, one has
$\dim(U) = \dim(X)$.*

<!-- original page 109 -->

One knows in fact that $\dim(U) \leqslant \dim(X)$ `(0, 14.1.4)`; moreover, since $X$ is a Jacobson prescheme, $U$
contains a closed point of every irreducible component of $X$, so $\dim(U) = \dim(X)$ by virtue of `(10.6.1)` and
`(0, 14.1.2.1)`.

**Proposition (10.6.3).**

<!-- label: IV.10.6.3 -->

*Suppose that $X$ satisfies conditions 1°, 2°, and 3° of `(10.6.1)`, and let $Y$ be a closed subset of $X$. Then, for
every $x \in Y$, and every open neighbourhood $U$ of $x$ in $X$ not meeting the irreducible components of $Y$ which do
not contain $x$, one has*

```text
(10.6.3.1)        dim(U) = sup_i dim(U ∩ Y_i) = sup_i dim(Y_i) = dim_x(X)
```

*where $Y_{i}$ ($1 \leqslant i \leqslant m$) are the irreducible components of $Y$ containing $x$.*

By considering a closed subprescheme of $X$ having $Y$ as underlying space, we may restrict, by virtue of
`(10.6.1, (i))`, to the case where $Y = X$. By the choice of $U$, $U$ is the union of the $U \cap X_{i}$, so
`dim(U) = sup_i dim(U ∩ X_i)`; but by `(10.6.2)` applied to a closed subprescheme of $X$ having $X_{i}$ as underlying
space, one has (taking `(10.6.1, (i))` into account) $\dim(U \cap X_{i}) = \dim(X_{i})$; this proves that the second and
fourth terms of `(10.6.3.1)` are equal. Since $U \cap X_{i}$ is biequidimensional `(10.6.1, (i))` (since the immersion
$U \cap X_{i} \to X_{i}$ is of finite type `(I, 6.3.5)`), one has

```text
(10.6.3.2)        dim(U ∩ X_i) = dim(U ∩ ‾{x}) + codim(‾{x}, X_i)
```

`(0, 14.3.5)`. By `(10.6.2)` applied to a closed subprescheme of $X$ having $\overline{x}$ as underlying space, $\dim(U
\cap \overline{x}) = \dim(\overline{x})$; since one also has, for the same reasons,

```text
(10.6.3.3)        dim(X_i) = dim(‾{x}) + codim(‾{x}, X_i)
```

one obtains

```text
  dim(U) = dim(‾{x}) + sup_i codim(‾{x}, X_i) = dim(‾{x}) + codim(‾{x}, X)
```

by definition of codimension `(0, 14.2.1)`. This shows that $\dim(U)$ is independent of the open neighbourhood $U$ of
$x$ satisfying the conditions of the statement, hence is equal to $\dim_{x}(X)$, by `(0, 14.1.4.1)`.

**Corollary (10.6.4).**

<!-- label: IV.10.6.4 -->

*Under the hypotheses of `(10.6.3)`, let $\mathcal{F}$ be a coherent $\mathcal{O}_{X}$-Module, $Y$ its support. For
every $x \in Y$, one has*

```text
(10.6.4.1)        dim(‾{x}) + dim(ℱ_x) = dim_x(Y).
```

Indeed, this follows from `(10.6.3.1)` and from the formula $\dim(\mathcal{F}_{x}) = codim(\overline{x}, Y)$
`(5.1.12.2)`.

### 10.7. Examples and counterexamples

**(10.7.1)**

<!-- label: IV.10.7.1 -->

Let $S$ be a locally Noetherian prescheme of dimension $\geqslant 1$ and suppose that $S$ is a Jacobson prescheme; when
$S$ is Noetherian, this amounts to saying that the irreducible components of $S$ of dimension `1` are infinite, for
every $x \in S$ that is not closed is the generic point of such a component `(10.4.5 and 10.5.4)`. Then $S$ also
satisfies conditions 2° and 3° of `(10.6.1)`: indeed, every local ring $\mathcal{O}_{S,s}$ is of dimension `0` or `1`,
and consequently is universally catenary `(7.2.9)`; on the other hand, an irreducible component $S'$ of $S$ is either
reduced

<!-- original page 110 -->

to a point or of dimension `1`, and for every closed point $s \in S'$, $\mathcal{O}_{S',s}$ is necessarily of dimension
`1`.

One deduces from these remarks and from `(10.6.1)` that every prescheme locally of finite type over $S$ also satisfies
properties 1°, 2°, and 3° of `(10.6.1)`: this is so in particular for preschemes locally of finite type over a field or
over $\mathbb{Z}$.

**(10.7.2)**

<!-- label: IV.10.7.2 -->

Let $A$ be a local Noetherian universally catenary ring and let $S$ be the complement in $X = \operatorname{Spec}(A)$ of
the closed point $a$. Then $S$ satisfies conditions 1°, 2°, and 3° of `(10.6.1)`: indeed, it was already seen that $S$
is a Jacobson prescheme `(10.5.9)`; since $A$ is universally catenary, so are the local rings $A_{\mathfrak{p}}$ at the
prime ideals of $A$ `(5.6.3)`. On the other hand, an irreducible component $S'$ of $S$ is the complement of $a$ in an
irreducible component $X'$ of $X$; for every closed point $x$ of $S$, the closure of $x$ in $X$ is therefore `{x, a}`,
in other words $\dim(\overline{x}) = 1$ and consequently, since $X'$ is by hypothesis biequidimensional `(0, 14.3.3)`,
one has $\dim(\mathcal{O}_{X',x}) = \dim(X') - 1$ `(0, 14.3.2)`, which proves that $S'$ is equicodimensional `(5.1.4)`.

**(10.7.3)**

<!-- label: IV.10.7.3 -->

Let $A$ be a discrete valuation ring; let us show that in the ring $B = A[T_{1}, \cdots, T_{n}]$ of polynomials in $n$
indeterminates, there exist two maximal ideals $\mathfrak{m}$, $\mathfrak{n}$ of heights $n$ and $n + 1$ respectively.
This was seen in `(5.2.5, (i))` for $n = 1$; let us prove it by induction on $n$. Since $A[T_{1}, \cdots, T_{n+1}]$ is a
free $A[T_{1}, \cdots, T_{n}]$-module, hence faithfully flat, there are in $A[T_{1}, \cdots, T_{n+1}]$ two maximal
ideals $\mathfrak{m}'$, $\mathfrak{n}'$ lying respectively over $\mathfrak{m}$ and $\mathfrak{n}$ $(0_{I}, 6.5.1)$;
moreover, according to `(5.5.3)`, these ideals are necessarily of heights $n + 1$ and $n + 2$ respectively, whence our
assertion. Assume $n \geqslant 2$ in what follows. Let $\mathfrak{J}$ be the ideal $\mathfrak{m} \cap \mathfrak{n} =
\mathfrak{mn}$, and $R = 1 + \mathfrak{J}$, which is a multiplicative subset of $B$; if one sets $B' = R^{-1}B$, the
ideal $\mathfrak{J}' = R^{-1}\mathfrak{J}$ is contained in the radical of $B'$
`(Bourbaki, Alg. comm., chap. III, §3, n° 5, prop. 12)`; one knows that $X' = \operatorname{Spec}(B')$ is identified as
a topological space with a subspace of $X = \operatorname{Spec}(B)$, and that at the points $x$ of $X'$, the local rings
$\mathcal{O}_{X,x}$ and $\mathcal{O}_{X',x}$ are the same `(I, 1.6.2)`. Consider then in $X'$ the closed set $Y' =
V(\mathfrak{J}')$, and set $S = X' - Y'$; one knows `(10.5.7)` that $S$ is a Jacobson prescheme, obviously irreducible
and Noetherian; moreover the local rings $\mathcal{O}_{S,s} = \mathcal{O}_{X,s}$ are universally catenary for every $s
\in S$ by virtue of `(5.6.3)`, since $A$ is universally catenary `(5.6.4)`. Yet there are two closed points $a$, $b$ of
$S$ such that $\mathcal{O}_{S,a}$ and $\mathcal{O}_{S,b}$ do not have the same dimension, in other words $S$ does not
satisfy condition 3° of `(10.6.1)`. To see this, consider the two maximal ideals $\mathfrak{m}' = R^{-1}\mathfrak{m}$,
$\mathfrak{n}' = R^{-1}\mathfrak{n}$ of $B'$, which are of heights $n$ and $n + 1$ respectively; one has $\mathfrak{J}'
= \mathfrak{m}' \cap \mathfrak{n}'$, and $\mathfrak{J}'$ is therefore contained in no prime ideal of $B'$ distinct from
$\mathfrak{m}'$ and $\mathfrak{n}'$, which are consequently the only maximal ideals of $B'$. Let $a'$, $b'$ be the only
closed points of $X'$, corresponding to $\mathfrak{m}'$ and $\mathfrak{n}'$. There exists in $B'$ a non-maximal prime
ideal $\mathfrak{p}' \subset \mathfrak{m}'$ which is not contained in $\mathfrak{n}'$: it suffices to show that there is
in $B$ a non-maximal prime ideal contained in $\mathfrak{m}$ and not in $\mathfrak{n}$; for this, one may for example
consider the fibre of $\mathfrak{m}$ for the morphism corresponding to the injection $A[T_{1}] \to B = A[T_{1}, \cdots,
T_{n}]$, and apply `(6.1.2)`. By considering a maximal chain of prime ideals between $\mathfrak{p}'$ and $\mathfrak{m}'$
and replacing $\mathfrak{p}'$ by the next-to-last ideal of this chain, one may therefore suppose that the point $a$ of
$X'$ corresponding to $\mathfrak{p}'$ is such that its closure in $X'$ is `{a, a'}`; since $B'_{\mathfrak{m}'}$ is
biequidimensional, $\mathfrak{p}'$ is then of height $n - 1$. One constructs in the same way a non-maximal prime ideal
$\mathfrak{q}'$ of $B'$ of height $n$, such that if $b$ is the corresponding point of $X'$, the closure of $b$ in $X'$
is `{b, b'}`. This being so, $a$ and $b$ are in $S$, hence closed in $S$, and consequently answer the question.

### 10.8. Rectified depth

**Definition (10.8.1).**

<!-- label: IV.10.8.1 -->

*Let $X$ be a locally Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. For every $x \in X$, one
calls **rectified depth** of $\mathcal{F}$ at the point $x$, and one denotes by $prof*_{x}(\mathcal{F})$, the number
(integer $\geqslant 0$ or $+\infty$) equal to*

```text
(10.8.1.1)        prof*_x(ℱ) = prof(ℱ_x) + dim(‾{x})
```

*where $\overline{x}$ is the closure of the point $x$ in $X$. For every subset $Z$ of $X$, one calls **rectified depth**
of $\mathcal{F}$ along $Z$, and one denotes by $prof*_{Z}(\mathcal{F})$, the number*

```text
(10.8.1.2)        prof*_Z(ℱ) = inf_{x ∈ Z} prof*_x(ℱ).
```

In other words, for every integer $n$, the relation $prof*_{Z}(\mathcal{F}) \geqslant n$ is equivalent to
$prof*_{x}(\mathcal{F}) \geqslant n$ for every $x \in Z$. If $Z = X$, one writes $prof*(\mathcal{F})$ instead of
$prof*_{X}(\mathcal{F})$.

<!-- original page 111 -->

**Remarks (10.8.2).**

<!-- label: IV.10.8.2 -->

(i) At every closed point $x \in X$, the rectified depth is equal to the depth.

(ii) Let $Y$ be a closed subprescheme of $X$, $j : Y \to X$ the canonical injection, $\mathcal{G}$ a coherent
$\mathcal{O}_{Y}$-Module. One knows `(5.7.3, (vi))` that $prof(\mathcal{G}_{x}) = prof((j_{*}(\mathcal{G}))_{x})$ for
every $x \in Y$; one deduces that one also has $prof*_{x}(\mathcal{G}) = prof*_{x}(j_{*}(\mathcal{G}))$ for every $x \in
Y$.

(iii) The notion of rectified depth is of interest only when it is of local character, that is, when it does not change
on replacing $X$ by an arbitrary open neighbourhood $U$ of $x$. This evidently requires that $x$ not be isolated in
$\overline{x}$ when $x$ is not closed, and consequently that $X$ be a Jacobson prescheme `(10.4.5.1)`; most often, it
will also be necessary to know that $\dim(U) = \dim(X)$ for every open $U$ dense in $X$, and one will therefore have to
suppose that $X$ also satisfies conditions 2° and 3° of `(10.6.1)`.

**Lemma (10.8.3).**

<!-- label: IV.10.8.3 -->

*Let $X$ be a regular and biequidimensional prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module. Then one has,
for every $x \in X$,*

```text
(10.8.3.1)        prof*_x(ℱ) = dim(X) − dim. proj(ℱ_x).
```

Indeed, since $X$ is biequidimensional, one has `(0, 14.3.5.1)`

```text
  dim(‾{x}) = dim(X) − codim(‾{x}, X) = dim(X) − dim(𝒪_{X,x})
```

by virtue of `(5.1.2)`. On the other hand, since $X$ is regular, one has by `(0, 17.3.4)`

```text
  prof(ℱ_x) = dim(𝒪_{X,x}) − dim. proj(ℱ_x)
```

whence the lemma.

**Corollary (10.8.4).**

<!-- label: IV.10.8.4 -->

*Under the hypotheses of `(10.8.3)`, the function $x \mapsto prof*_{x}(\mathcal{F})$ is lower semi-continuous.*

This follows from `(10.8.3.1)`, since $x \mapsto \dim. proj(\mathcal{F}_{x})$ is upper semi-continuous `(6.11.1)`.

**Proposition (10.8.5).**

<!-- label: IV.10.8.5 -->

*Let $S$ be a locally Noetherian prescheme, $X$ a prescheme locally of finite type over $S$, $\mathcal{F}$ a coherent
$\mathcal{O}_{X}$-Module. Suppose that $S$ satisfies the following conditions: 1° $S$ is a Jacobson prescheme; 2° $S$ is
regular; 3° the irreducible components of $S$ are equicodimensional. Then the function $x \mapsto
prof*_{x}(\mathcal{F})$ is lower semi-continuous in $X$; in other words, for every integer $n$, the set $U_{n}$ of $x
\in X$ such that $prof*_{x}(\mathcal{F}) \geqslant n$ is open.*

Since the local rings $\mathcal{O}_{S,s}$ of $S$ are regular, they are universally catenary `(5.6.4)`; in other words,
$S$ satisfies conditions 1°, 2°, and 3° of `(10.6.1)`, so the same holds for $X$ `(10.6.1, (i))`. The notion of
rectified depth then being of local character `(10.8.2, (iii))`, one may restrict to the case where $S =
\operatorname{Spec}(A)$ and $X = \operatorname{Spec}(B)$ are affine, $A$ being a regular ring and $B$ an $A$-algebra of
finite type, hence a quotient of a polynomial ring $C = A[T_{1}, \cdots, T_{n}]$, and the latter is regular
`(0, 17.3.7)`. One may therefore suppose that $X$ is a closed subprescheme of a regular prescheme $Y$ also satisfying
conditions 1°, 2°, and 3° of `(10.6.1)`; taking remark `(10.8.2, (ii))` into account, one is thus reduced to the case
where $X$ is in addition regular and Noetherian. But since the local rings of $X$ are then integral, the irreducible
components of $X$ are

<!-- original page 112 -->

open `(I, 6.1.10)`, and one may consequently also suppose $X$ irreducible. Then, since the local rings of $X$ are
catenary `(0, 16.5.12)`, hypothesis 3° of `(10.6.1)` entails that $X$ is biequidimensional (`(5.1.5)` and
`(0, 14.3.3)`); it therefore suffices to apply `(10.8.4)`.

One notes that if $S$ is the spectrum of a field or of $\mathbb{Z}$, it satisfies the conditions of `(10.8.5)`.

**Corollary (10.8.6).**

<!-- label: IV.10.8.6 -->

*Under the hypotheses of `(10.8.5)`, for every $x \in X$, the number $prof*_{x}(\mathcal{F})$ is the unique integer $n$
having the following property: there exists an open neighbourhood $U$ of $x$ in $X$ such that for every point $x' \in U
\cap \overline{x}$, closed in $U$, one has $prof(\mathcal{F}_{x'}) = n$. In particular, for $prof*_{x}(\mathcal{F})
\geqslant m$ (resp. $prof*_{x}(\mathcal{F}) \leqslant m$), it is necessary and sufficient that there exist an open
neighbourhood $V$ of $x$ in $X$ such that, for every $x' \in V \cap \overline{x}$, closed in $V$, one has
$prof(\mathcal{F}_{x'}) \geqslant m$ (resp. $prof(\mathcal{F}_{x'}) \leqslant m$).*

Indeed, one may restrict to the case where $x$ is not closed; if $prof*_{x}(\mathcal{F}) = n$, the set of $y \in X$ such
that $prof*_{y}(\mathcal{F}) < n$ is closed by virtue of `(10.8.5)`, so contains $\overline{x}$; and by virtue of the
lower semi-continuity of $y \mapsto prof*_{y}(\mathcal{F})$, there exists an open neighbourhood $U$ of $x$ such that
$prof*_{y}(\mathcal{F}) = n$ for every $y \in U \cap \overline{x}$, hence $prof(\mathcal{F}_{x'}) = n$ if $x' \in U \cap
\overline{x}$ is closed in $U$ (since the notion of rectified depth is local).

For preschemes satisfying the hypotheses of `(10.8.5)`, the notion of rectified depth can therefore be defined by means
of the values of the depth at the closed points of $X$ (the latter forming a very dense set in every closed part of
$X$).

**Proposition (10.8.7).**

<!-- label: IV.10.8.7 -->

*Let $S$ be a locally Noetherian prescheme satisfying conditions 1°, 2°, and 3° of `(10.6.1)`. Let $X$ be a prescheme
locally of finite type over $S$, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module, $Y = Supp(\mathcal{F})$. Then, for
every $x \in Y$, one has*

```text
(10.8.7.1)        prof*_x(ℱ) = dim_x(Y) − coprof(ℱ_x).
```

Indeed, by definition, one has `coprof(ℱ_x) = dim(ℱ_x) − prof(ℱ_x)`, and it follows from `(10.6.4)` that one has
`dim_x(Y) = dim(‾{x}) + dim(ℱ_x)`; whence `(10.8.7.1)` by definition of $prof*_{x}(\mathcal{F})$.

**Corollary (10.8.8).**

<!-- label: IV.10.8.8 -->

*The hypotheses on $f$ and $\mathcal{F}$ being those of `(9.9.1)`, the function $x \mapsto
prof*_{x}(\mathcal{F}_{f(x)})$ is constructible.*

Note that for every $s \in S$, the fibre $X_{s}$ being a prescheme locally of finite type over $k(s)$, is a Jacobson
prescheme `(10.4.7)`; since in addition $\operatorname{Spec}(k(s))$ satisfies the conditions of `(10.6.1)`, one has
`prof*_x(ℱ_{f(x)}) = dim_x(Supp(ℱ_{f(x)})) − coprof((ℱ_{f(x)})_x)` `(10.8.7)`. Now, if $Z = Supp(\mathcal{F})$, one has
$Z_{f(x)} = Supp(\mathcal{F}_{f(x)})$ `(I, 9.1.13)` and $Z$ is locally constructible `(8.9.1)`; so the functions $x
\mapsto \dim_{x}(Supp(\mathcal{F}_{f(x)}))$ and $x \mapsto coprof((\mathcal{F}_{f(x)})_{x})$ are locally constructible
(`(9.9.1)` and `(9.9.3)`), which proves the proposition.

### 10.9. Maximal spectra and ultra-preschemes

*The results of this number will not be used in what follows.*

**(10.9.1)**

<!-- label: IV.10.9.1 -->

Let $X$ be a Jacobson prescheme, and let $S(X)$ be the ringed space whose underlying space is the subspace of closed
points of $X$, and whose sheaf of rings is the sheaf induced on this subspace by $\mathcal{O}_{X}$, in other words the
sheaf of rings $\psi*(\mathcal{O}_{X})$, where $\psi : S(X) \to X$ denotes the canonical injection. Since $\psi$ is a
quasi-

<!-- original page 113 -->

homeomorphism, it was seen `(10.2.8, (ii))` that if $\theta : \mathcal{O}_{X} \to \psi_{*}(\mathcal{O}_{S(X)})$ is the
homomorphism of sheaves of rings such that $\theta\sharp : \psi*(\mathcal{O}_{X}) \to \mathcal{O}_{S(X)}$ is the
identity, then $j_{X} = (\psi, \theta)$ is a quasi-isomorphism of ringed spaces, and $\mathcal{F} \mapsto
\psi*(\mathcal{F})$ an equivalence of the category of $\mathcal{O}_{X}$-Modules and that of
$\mathcal{O}_{S(X)}$-Modules. It is clear that in this equivalence, locally free (resp. coherent)
$\mathcal{O}_{X}$-Modules correspond to locally free (resp. coherent) $\mathcal{O}_{S(X)}$-Modules; in addition, if
$\mathcal{F}$ is a locally free $\mathcal{O}_{X}$-Module and $U$ is an open of $X$ such that $\mathcal{F}|U$ is
isomorphic to $(\mathcal{O}_{X}|U)^{n}$, $\psi*(\mathcal{F})$ is such that $\psi*(\mathcal{F})|(U \cap S(X))$ is
isomorphic to $(\mathcal{O}_{S(X)}|(U \cap S(X)))^{n}$.

**(10.9.2)**

<!-- label: IV.10.9.2 -->

Let $X$, $Y$ be two Jacobson preschemes and $f = (\phi, \lambda) : X \to Y$ a morphism locally of finite type. It was
seen `(10.4.7)` that $\phi(S(X)) \subset S(Y)$, and by restriction of $\phi$ to $S(X)$, one therefore defines a
continuous map $S(\phi) : S(X) \to S(Y)$. On the other hand, for every open $V$ of $Y$, one defines by composition a
ring homomorphism

```text
  Γ(V ∩ S(Y), 𝒪_{S(Y)}) → Γ(V, 𝒪_Y) → Γ(f⁻¹(V), 𝒪_X) → Γ(f⁻¹(V) ∩ S(X), 𝒪_{S(X)})
```

where the two extreme isomorphisms have been defined in `(10.9.1)`; it is clear that this defines a homomorphism of
sheaves of rings $S(\lambda) : \mathcal{O}_{S(Y)} \to S(\phi)_{*}(\mathcal{O}_{S(X)})$ (recalling that the open sets of
$S(X)$ (resp. $S(Y)$) correspond bijectively to those of $X$ (resp. $Y$) `(10.2.1)`); one thus obtains a morphism of
ringed spaces $S(f) = (S(\phi), S(\lambda)) : (S(X), \mathcal{O}_{S(X)}) \to (S(Y), \mathcal{O}_{S(Y)})$ such that the
diagram

```text
              S(f)
       S(X) ———→ S(Y)
        │           │
    j_X │           │ j_Y
        ↓           ↓
        X  ———→   Y
              f
```

is commutative; in addition, if $Z$ is a third Jacobson prescheme and $g : Y \to Z$ a morphism locally of finite type,
it is clear that $S(g \circ f) = S(g) \circ S(f)$. One has thus defined a covariant functor $S : \mathcal{C} \to
\mathcal{C}'$, where $\mathcal{C}'$ is the category of ringed spaces in local rings, and $\mathcal{C}$ the category
whose objects are the Jacobson preschemes and whose morphisms are the morphisms locally of finite type between Jacobson
preschemes.

**(10.9.3)**

<!-- label: IV.10.9.3 -->

Let us propose to determine the subcategory $\mathcal{C}''$ of $\mathcal{C}'$ formed by the ringed spaces isomorphic to
the $S(X)$ and whose morphisms come from the $S(f)$. Suppose first that $X = \operatorname{Spec}(A)$, where $A$ is a
Jacobson ring; then $S(X)$ is the set of maximal ideals of $A$, equipped with: 1° the topology induced by that of $X$,
so that a base of this topology is formed by the $D_{\mathfrak{m}}(h) = D(h) \cap S(X)$, the set of maximal ideals
$\mathfrak{m}$ of $A$ such that $h \notin \mathfrak{m}$, where $h$ runs through $A$; 2° the sheaf of rings
$\mathcal{O}_{S(X)}$ such that $\Gamma(D_{\mathfrak{m}}(h), \mathcal{O}_{S(X)}) = A_{h}$. We shall say that this ringed
space is the **maximal spectrum** of the Jacobson ring $A$ and we shall denote it by $Spm(A)$.

Note that if $j : D(h) \to X$ is the canonical injection, the ringed space induced on $D_{\mathfrak{m}}(h)$ by $S(X)$ is
$S(D(h))$ and the canonical injection $D_{\mathfrak{m}}(h) \to S(X)$ of ringed spaces is equal to $S(j)$.

Let $B$ be a second Jacobson ring, $Y = \operatorname{Spec}(B)$, $\phi : B \to A$ a ring homomorphism making $A$ a
$B$-algebra of finite type, $f = ({}^{a}\phi, {}^{a}\tilde{\phi}) : X \to Y$ the corresponding morphism of preschemes,
and

$$ S(f) : Spm(A) \to Spm(B) $$

the morphism of ringed spaces corresponding to $f$. It is clear that $S(f) = (\psi, \theta)$ is a morphism of ringed
spaces in local rings, that is $(Err_{III}, 1.8.2)$ that for every $x \in Spm(A)$, $\theta^{\sharp}_{x}$ is a local
homomorphism. Conversely:

**Proposition (10.9.4).**

<!-- label: IV.10.9.4 -->

*Let $A$, $B$ be two Jacobson rings. If $u = (\psi, \theta) : Spm(A) \to Spm(B)$ is a morphism of ringed spaces in local
rings such that $\Gamma(\theta) : B \to A$ makes $A$ a $B$-algebra of finite type, there exists a morphism of preschemes
$f : \operatorname{Spec}(A) \to \operatorname{Spec}(B)$ and only one such that $u = S(f)$.*

The uniqueness of $f$ is evident, since if $f = ({}^{a}\phi, {}^{a}\tilde{\phi})$, one must have $\phi =
\Gamma(\theta)$; it remains to see that $S(f)$ is defined and that one has $u = S(f)$. Now, the first assertion follows
from the fact that $\phi$ is assumed to make $A$ a $B$-algebra of finite type, and consequently $f(Spm(A)) \subset
Spm(B)$; the fact that $\theta^{\sharp}_{x}$ is a local homomorphism for every $x \in Spm(A)$ then allows one to repeat
the argument of `(I, 1.7.3)` while restricting to the points $x$ of $Spm(A)$: one thus shows successively that $\psi(x)
= {}^{a}\phi(x)$ for every $x \in Spm(A)$, then that $\theta^{\sharp}_{x} = \phi_{x} : B_{\psi(x)} \to A_{x}$, which
completes the proof that $u = S(f)$.

<!-- original page 114 -->

**(10.9.5)**

<!-- label: IV.10.9.5 -->

Let us now consider a ringed space $(X, \mathcal{O}_{X})$; we shall say that an open subset $U$ of $X$ is
**ultra-affine** if the induced ringed space $(U, \mathcal{O}_{X}|U)$ is isomorphic to a maximal spectrum $Spm(A)$,
where $A$ is a Jacobson ring. We shall say that $X$ is an **ultra-prescheme** if every point of $X$ admits an
ultra-affine open neighbourhood. One shows, as in `(I, 2.1.3 and 2.1.4)`, that the ultra-affine open sets form a base of
the topology of $X$ and that $X$ is a Kolmogorov space. If $Y$ is a second ultra-prescheme, we shall say that a morphism
of ringed spaces $f : X \to Y$ is a *morphism of ultra-preschemes* if it satisfies the following conditions: 1° $f$ is a
morphism of ringed spaces in local rings; 2° for every $x \in X$, there is an ultra-affine open neighbourhood $V$ of
$f(x)$ in $Y$ and an ultra-affine open neighbourhood $U$ of $x$ in $X$ such that $f(U) \subset V$ and such that the
homomorphism $\Gamma(V, \mathcal{O}_{Y}) \to \Gamma(U, \mathcal{O}_{X})$ corresponding to $f$ makes $\Gamma(U,
\mathcal{O}_{X})$ a $\Gamma(V, \mathcal{O}_{Y})$-algebra of finite type.

It is immediate that one thus defines morphisms, the composite of two morphisms being a third thanks to the final remark
of `(10.9.3)`. It is clear that the category $\mathcal{C}''_{0}$ thus defined is a subcategory of $\mathcal{C}'$ which
contains $\mathcal{C}''$; we propose to show that $\mathcal{C}'' = \mathcal{C}''_{0}$, in other words:

**Proposition (10.9.6).**

<!-- label: IV.10.9.6 -->

*The functor $X \mapsto S(X)$ from $\mathcal{C}$ to $\mathcal{C}''_{0}$ is an equivalence of categories.*

1° Let us first show that the functor $X \mapsto S(X)$ is fully faithful, in other words that for $X$, $Y$ in
$\mathcal{C}$, the canonical map

```text
  Hom_𝒞(X, Y) → Hom_{𝒞''_0}(S(X), S(Y))
```

is bijective. First, it is injective: let $f$, $g$ be two morphisms locally of finite type from $X$ to $Y$ and suppose
that $S(f) = S(g)$. This entails first that for every open $V$ of $Y$, one has $f^{-1}(V) \cap S(X) = g^{-1}(V) \cap
S(X)$, hence (`(10.3.1)` and `(10.2.7)`) $f^{-1}(V) = g^{-1}(V)$; it therefore suffices to prove that for every affine
open $V$ of $Y$, $f$ and $g$ coincide in $f^{-1}(V) = g^{-1}(V)$, in other words one is reduced to the case where $Y =
\operatorname{Spec}(B)$ is the spectrum of a Jacobson ring $B$. It suffices `(I, 2.2.4)` to show that the ring
homomorphisms $B \to \Gamma(X, \mathcal{O}_{X})$ corresponding to $f$ and $g$ are then the same. Now, for every $s \in
B$, the images of $s$ under these homomorphisms are two sections of $\mathcal{O}_{X}$ over $X$ which, by hypothesis,
induce the same section over $S(X)$; one knows therefore `(10.2.8)` that these sections are identical, whence our
assertion. Let us prove secondly that every morphism $h : S(X) \to S(Y)$ (for the category $\mathcal{C}''_{0}$) is of
the form $S(f)$, where $f : X \to Y$ is a morphism locally of finite type. By hypothesis, there exists an ultra-affine
open cover $(U'_{\lambda})$ (resp. $(V'_{\lambda})$) of $S(X)$ (resp. $S(Y)$) such that for every $\lambda$,
$h(U'_{\lambda})$ is contained in some $V'_{\lambda}$ and there corresponds to the morphism $h_{\lambda} : U'_{\lambda}
\to V'_{\lambda}$, restriction of $h$, a ring homomorphism $\Gamma(V'_{\lambda}, \mathcal{O}_{S(Y)}) \to
\Gamma(U'_{\lambda}, \mathcal{O}_{S(X)})$ making the second ring an algebra of finite type over the first. One may
suppose that $U'_{\lambda} = U_{\lambda} \cap S(X)$ and $V'_{\lambda} = V_{\lambda} \cap S(Y)$, where $U_{\lambda}$ and
$V_{\lambda}$ are affine open sets uniquely determined in $X$ and $Y$ respectively; if one shows that, for every
$\lambda$, $h_{\lambda} = S(f_{\lambda})$ where $f_{\lambda} : U_{\lambda} \to V_{\lambda}$ is a morphism of finite
type, then it follows from the first part of the argument, applied to the restrictions of $f_{\alpha}$ and $f_{\beta}$
to $U_{\alpha} \cap U_{\beta}$, that the $f_{\lambda}$ are the restrictions of a single morphism $f : X \to Y$, and one
will evidently have $h = S(f)$. One is thus reduced to the case where $X$ and $Y$ are affine, and the conclusion then
follows from `(10.9.4)`.

2° It remains to prove that every ultra-prescheme $X'$ is of the form $S(X)$ for a Jacobson prescheme $X$ (which will
necessarily be unique up to isomorphism, by virtue of 1°). There is a cover $(U'_{\alpha})$ of $X'$ by ultra-affine open
sets, each of which is of the form $S(U_{\alpha})$, $U_{\alpha}$ being the spectrum of a Jacobson ring. For every pair
of indices $\alpha$, $\beta$, consider the unique open $U_{\alpha \beta}$ of $U_{\alpha}$ whose trace on $U'_{\alpha}$
is $U'_{\alpha} \cap U'_{\beta}$; by virtue of 1°, the identity automorphism of $U'_{\alpha} \cap U'_{\beta}$ is of the
form $S(\theta_{\alpha \beta})$, where $\theta_{\alpha \beta} : U_{\alpha \beta} \to U_{\beta \alpha}$ is an isomorphism
of preschemes. One verifies immediately (by virtue of 1°) that the family $(\theta_{\alpha \beta})$ satisfies the gluing
condition $(0_{I}, 4.1.7)$, and that this family therefore defines a prescheme $X$, in which the $U_{\alpha}$ are
identified with affine open sets; it is then clear that one has $X' = S(X)$, which completes the proof.

### 10.10. Serre algebraic spaces

**(10.10.1)**

<!-- label: IV.10.10.1 -->

The language introduced by Serre in `(FAC)` is sometimes convenient, in particular in questions where the main interest
attaches to the points rational over the base field $k$ (algebraically closed by hypothesis) of the "algebraic
varieties" over $k$ that one considers. We shall sketch this language here while connecting it to the foregoing
considerations, to enable the reader to translate Serre's statements into the language of schemes. It is in fact
possible to develop Serre's language also for preschemes over a non-algebraically-closed field (and even over an
Artinian ring); but this introduces considerable technical complications, and besides,

<!-- original page 115 -->

over an arbitrary base field, the (mainly psychological) advantages of Serre's viewpoint disappear; we shall therefore
confine ourselves to the framework fixed by Serre. The present number, like the preceding one, will not be used in the
remainder of this Treatise, and we shall therefore confine ourselves to brief indications.

**(10.10.2)**

<!-- label: IV.10.10.2 -->

Given a fixed ultra-prescheme $R$, one may naturally (as in any category) define the notion of *$R$-ultra-prescheme*.
Consider in particular an algebraically closed field $k$; $Spm(k)$ is then identical with $\operatorname{Spec}(k)$; we
shall say that a $Spm(k)$-ultra-prescheme $X'$ is a **pre-algebraic space** over $k$: it is therefore a $k$-ringed space
in local rings each point of which has an open neighbourhood isomorphic to the maximal spectrum of a $k$-algebra of
finite type; this amounts to saying (by `(10.9.6)`) that $X' = S(X)$, where $X$ is a prescheme locally of finite type
over $k$. If $X$, $Y$, $Z$ are three $k$-preschemes locally of finite type, so is $X \times_{Z} Y$ `(1.3.4)`, so by
virtue of `(10.9.6)`, the notion of product exists in the category of pre-algebraic spaces over $k$ (both the product
"over $k$" $X' \times_{k} Y'$ and the "fibre product" $X' \times_{Z'} Y'$, where $X'$, $Y'$, $Z'$ are three
pre-algebraic spaces over $k$). One may therefore define the diagonal morphism $\Delta_{X'} : X' \to X' \times_{k} X'$
(which is moreover none other than $S(\Delta_{X})$); one says that $X'$ is an **algebraic space** over $k$ if $X$ is a
scheme, and this amounts to saying that the image of $\Delta_{X'}$ is a closed subset of $X' \times_{k} X'$.

**(10.10.3)**

<!-- label: IV.10.10.3 -->

The simplifications coming from the hypothesis that $k$ is algebraically closed are first that, for a $k$-prescheme $X$
locally of finite type, there is a bijective correspondence between closed points of $X$, points of $X$ with values in
$k$ `(I, 3.4.4)`, and points of $X$ rational over $k$ `(I, 3.4.5)`, by virtue of `(I, 6.4.2)`. This shows in particular
(by virtue of `(I, 3.4.3.1)`) that for two $k$-pre-algebraic spaces $X'$, $Y'$, the underlying set of the product $X'
\times_{k} Y'$ is identical with the *product set* $X' \times Y'$ of the underlying sets (but of course the topology of
the space underlying $X' \times_{k} Y'$ is not the product topology of the topologies of the spaces underlying $X'$ and
$Y'$; it is in general strictly finer than the latter).

On the other hand, the local rings $\mathcal{O}_{x}$ at the points of a pre-algebraic space $X'$ over $k$ are
$k$-algebras whose residue field has just been seen to be isomorphic to $k$; if $A$ and $B$ are two such local
$k$-algebras, every $k$-homomorphism $\phi : A \to B$ is necessarily local: indeed, if an element $x$ of the maximal
ideal of $A$ were such that $\phi(x)$ is invertible, there would exist $\lambda \in k$ non-zero such that $\phi(x -
\lambda \cdot 1)$ belongs to the maximal ideal of $B$, which is absurd since $x - \lambda \cdot 1$ is invertible in $A$.
One concludes immediately that if $X' = S(X)$, $Y' = S(Y)$ are two pre-algebraic spaces over $k$, every morphism $X' \to
Y'$ of $k$-ringed spaces is also a morphism of $k$-ringed spaces in local rings $(I, 1.8.2; cf. Err_{III})$. Moreover,
with the preceding notation, if $A$ and $B$ are $k$-algebras of finite type, $\phi$ makes $B$ an $A$-algebra of finite
type; so every morphism $X' \to Y'$ of $k$-ringed spaces is, by virtue of `(10.9.6)`, of the form $S(f)$, where $f : X
\to Y$ is a morphism of $k$-preschemes.

Finally, for every open $U$ of $X'$, every section $s \in \Gamma(U, \mathcal{O}_{X'})$, and every $x \in U$, $s(x)$
$(0_{I}, 5.5.1)$ is identified with an element of $k$, and one has thus associated to $s$ a map $\tilde{s} : x \mapsto
s(x)$ from $U$ to $k$, in other words a section over $U$ of the sheaf $\mathcal{A}(X')$ of germs of maps from $X'$ to
$k$; since the map $h_{U} : s \mapsto \tilde{s}$ is evidently a ring homomorphism $\Gamma(U, \mathcal{O}_{X'}) \to
\Gamma(U, \mathcal{A}(X'))$ and commutes with restrictions to an open $V \subset U$, the $h_{U}$ define a homomorphism
of sheaves of rings $h : \mathcal{O}_{X'} \to \mathcal{A}(X')$. If one takes for $U$ an ultra-affine open $Spm(A)$,
where $A$ is a Jacobson ring, to say that $\tilde{s} = 0$ means that for every maximal ideal $\mathfrak{m}$ of $A$, $s$
belongs to $\mathfrak{m}$, or equivalently that $s$ is in the radical of $A$; but since $A$ is a Jacobson ring, its
radical is equal to its nilradical; for $h_{U}$ to be injective, it is therefore necessary and sufficient that $A$ be
reduced.

**(10.10.4)**

<!-- label: IV.10.10.4 -->

One says that the $k$-pre-algebraic space $X' = S(X)$ is **reduced** if $X$ is so; since the set of points $x \in X$
where $X$ is reduced is open $(0_{I}, 5.2.2)$, its complement contains at least one closed point if it is non-empty
`(5.1.11)`, and it therefore amounts to the same to say that $X'$ is reduced or that each of its local rings
$\mathcal{O}_{x}$ (for $x \in X'$) is reduced. It was just seen in `(10.10.3)` that for the homomorphism $h :
\mathcal{O}_{X'} \to \mathcal{A}(X')$ to be injective, it is necessary and sufficient that $X'$ be reduced. In `(FAC)`,
Serre in fact restricts to reduced pre-algebraic spaces, which allows him to define $\mathcal{O}_{X'}$ as a subsheaf of
$\mathcal{A}(X')$. Note that if $X'$ and $Y'$ are reduced $k$-pre-algebraic spaces, so is $X' \times_{k} Y'$: indeed,
everything reduces to seeing that if $A$ and $B$ are two reduced $k$-algebras of finite type, so is $A \otimes_{k} B$;
but we have seen that the radicals of $A$ and $B$ are then reduced to `0`, and since $k$ is algebraically closed, $A$
and $B$ are "separable" algebras over $k$ in the sense of Bourbaki `(Bourbaki, Alg., chap. VIII, §7, n° 5, prop. 5)`; so
$A \otimes_{k} B$ has no radical (loc. cit., n° 6, cor. 3 of th. 3), and since it is a Jacobson ring, it is reduced.
However, if $Z'$ is a third pre-algebraic space over $k$, the "fibre product" $X' \times_{Z'} Y'$ of two reduced
pre-algebraic spaces over $Z'$ is in general not reduced, which implies that the category of these spaces is
insufficient in many questions (in particular in the theory of algebraic groups). But as was seen above, one may keep
Serre's language without restricting oneself, as he does (and he in addition only considers quasi-compact pre-algebraic
spaces), to the case of reduced pre-algebraic spaces.

<!-- original page 116 -->

**(10.10.5)**

<!-- label: IV.10.10.5 -->

Finally, one may also consider ultra-preschemes over an arbitrary field $k$ while keeping a language that remains close
to that of Serre, and introducing, as with Weil, a fixed algebraically closed extension $K$ of $k$ (chosen large enough,
for example of infinite transcendence degree over $k$, to have enough "generic points" in Weil's sense). To every
prescheme $X$ locally of finite type over $k$, one then associates the set $S_{K}(X) = S(X \otimes_{k} K)$ of points of
$X$ with values in $K$; one has a canonical map $j : S_{K}(X) \to X$ which one shows to be a quasi-homeomorphism when
one equips $S_{K}(X)$ with the inverse image of the topology of $X$ under $j$; one equips $S_{K}(X)$ with the sheaf of
$k$-algebras $j*(\mathcal{O}_{X})$, and one thus obtains a subcategory of the category of $k$-ringed spaces in local
rings, which one might call the *category of $(k, K)$-pre-algebraic spaces*. One can show that one may still define
products there and generalize the results of `(10.10.3)` and `(10.10.4)` ($\mathcal{A}(X')$ being here replaced by the
sheaf $\mathcal{A}_{K}(X')$ of germs of maps from $X'$ to $K$). However, this viewpoint gives an artificial role to an
arbitrarily chosen overfield of $k$, and we signal it only to reject it.

# Chapter I — The Language of Schemes

## §2. Preschemes and Morphisms of Preschemes

<!-- label: I.2 -->

### 2.1. Definition of preschemes

<!-- label: I.2.1 -->

**(2.1.1)** Given a ringed space $(X, \mathcal{O}_{X})$, an open subset $V \subset X$ is called an _affine open_ if the
ringed space $(V, \mathcal{O}_{X} | V)$ is an affine scheme (1.7.1).

**Definition (2.1.2).** A _prescheme_ [modern: scheme] is a ringed space $(X, \mathcal{O}_{X})$ such that every point of
$X$ admits an affine open neighborhood.

**Proposition (2.1.3).** If $(X, \mathcal{O}_{X})$ is a prescheme, the affine open subsets form a basis of the topology
of $X$.

**Proof.** Let $V$ be an open neighborhood of $x$, and $W$ an affine open neighborhood with ring $A$. Then $V \cap W$ is
open in $W$, so some $D(f) \subset V \cap W$ ($f \in A$) is an affine open neighborhood of $x$, by (1.1.10) and (1.3.6).

**Proposition (2.1.4).** The underlying space of a prescheme is a Kolmogorov space.

**Proposition (2.1.5).** In a prescheme $(X, \mathcal{O}_{X})$, every closed irreducible subset of $X$ admits a unique
generic point; thus $x \mapsto \bar{x}$ is a bijection of $X$ onto the set of closed irreducible subsets.

**Proof.** If $Y$ is closed irreducible and $y \in Y$, let $U$ be an affine open neighborhood of $y$. Then $U \cap Y$ is
dense in $Y$, irreducible, and closed in $U$; by (1.1.14), $U \cap Y = \bar{x} \cap U$ for some $x \in U$, so $Y =
\bar{x}$. Uniqueness follows from (2.1.4) and (0.2.1.3).

**(2.1.6)** If $Y \subset X$ is closed irreducible with generic point $y$, the local ring $\mathcal{O}_{y}$ (also
written $\mathcal{O}_{X/Y}$) is called the _local ring of $X$ along $Y$_ (or the _local ring of $Y$ in $X$_).

If $X$ is irreducible with generic point $x$, $\mathcal{O}_{x}$ is the _ring of rational functions on_ $X$ (cf. §7).

**Proposition (2.1.7).** For every open $U \subset X$, the ringed space $(U, \mathcal{O}_{X} | U)$ is a prescheme — the
_induced_ prescheme (or _restriction_) on $U$.

**(2.1.8)** A prescheme $(X, \mathcal{O}_{X})$ is _irreducible_ (resp. _connected_) if $X$ is. It is _integral_ if it is
irreducible and reduced (cf. (5.1.4)). It is _locally integral_ if every $x \in X$ admits an open neighborhood $U$ such
that the induced prescheme on $U$ is integral.

### 2.2. Morphisms of preschemes

<!-- label: I.2.2 -->

**Definition (2.2.1).** Given two preschemes $(X, \mathcal{O}_{X})$ and $(Y, \mathcal{O}_{Y})$, a _morphism of
preschemes_ $(X, \mathcal{O}_{X}) \to (Y, \mathcal{O}_{Y})$ is a morphism $(\psi, \theta)$ of ringed spaces such that
for every $x \in X$, $\theta^{\sharp}_{x} : \mathcal{O}_{\psi(x)} \to \mathcal{O}_{x}$ is a _local_ homomorphism.

Passing to quotients, the stalk map gives a monomorphism $\theta^{x} : \kappa(\psi(x)) \to \kappa(x)$, making
$\kappa(x)$ an extension of $\kappa(\psi(x))$.

**(2.2.2)** Composition of two morphisms of preschemes is a morphism of preschemes (by $\theta''^{\sharp} =
\theta^{\sharp} \circ \psi*(\theta'^{\sharp})$, (0.3.5.5)). Thus preschemes form a _category_; we write
$\operatorname{Hom}(X, Y)$ for the set of morphisms.

**Example (2.2.3).** For an open $U \subset X$, the canonical injection $(U, \mathcal{O}_{X} | U) \to (X,
\mathcal{O}_{X})$ is a _monomorphism_ of preschemes.

**Proposition (2.2.4).** Let $(X, \mathcal{O}_{X})$ be a prescheme and $(S, \mathcal{O}_{S})$ an affine scheme of ring
$A$. There is a canonical bijection between morphisms of preschemes $(X, \mathcal{O}_{X}) \to (S, \mathcal{O}_{S})$ and
ring homomorphisms $A \to \Gamma(X, \mathcal{O}_{X})$.

**Proof sketch.** Any morphism $(\psi, \theta)$ gives $\Gamma(\theta) : A \to \Gamma(X, \mathcal{O}_{X})$. Conversely,
given $\phi : A \to \Gamma(X, \mathcal{O}_{X})$, cover $X$ by affine opens $(V_{\alpha})$; composing with restriction
$\Gamma(X, \mathcal{O}_{X}) \to \Gamma(V_{\alpha}, \mathcal{O}_{X} | V_{\alpha})$ gives $\phi_{\alpha}$, which
corresponds by (1.7.3) to a morphism $(\psi_{\alpha}, \theta_{\alpha}) : V_{\alpha} \to S$. These agree on overlaps (by
(2.1.3) and stalkwise compatibility), so they glue to a morphism $(\psi, \theta) : X \to S$ of preschemes with
$\Gamma(\theta) = \phi$.

For $f \in A$, $\psi^{-1}(D(f)) = X_{\phi(f)}$ (the open set where the section $\phi(f)$ does not vanish; see
(0.5.5.2)). (2.2.4.1)

**Proposition (2.2.5).** Under the hypotheses of (2.2.4), let $\phi : A \to \Gamma(X, \mathcal{O}_{X})$, $f : X \to S$
the corresponding morphism, $\mathcal{G}$ an $\mathcal{O}_{X}$-module, $\mathcal{F}$ an $\mathcal{O}_{S}$-module, and $M
= \Gamma(S, \mathcal{F})$. There is a canonical bijection between $f$-morphisms $\mathcal{F} \to \mathcal{G}$ (0.4.4.1)
and $A$-homomorphisms $M \to (\Gamma(X, \mathcal{G}))_{[\phi]}$.

**(2.2.6)** A morphism $(\psi, \theta) : X \to Y$ of preschemes is _open_ (resp. _closed_) if for every open $U \subset
X$ (resp. closed $F \subset X$), $\psi(U)$ is open (resp. $\psi(F)$ is closed) in $Y$. It is _dominant_ if $\psi(X)$ is
dense in $Y$, and _surjective_ if $\psi$ is. These conditions depend only on $\psi$.

**Proposition (2.2.7).** Let $f : X \to Y$ and $g : Y \to Z$ be morphisms of preschemes.

> (i) If $f$, $g$ are both open (resp. closed, dominant, surjective), so is $g \circ f$. (ii) If $f$ is surjective and
> $g \circ f$ closed, then $g$ is closed. (iii) If $g \circ f$ is surjective, so is $g$.

**Proposition (2.2.8).** Let $f : X \to Y$ and $(U_{\alpha})$ an open cover of $Y$. $f$ is open (resp. closed,
surjective, dominant) iff each restriction $\psi^{-1}(U_{\alpha}) \to U_{\alpha}$ is.

**(2.2.9)** Let `X, Y` have finitely many irreducible components $X_{i}, Y_{i}$ ($1 \leq i \leq n$) with generic points
$\xi_{i}, \eta_{i}$ (2.1.5). A morphism $f = (\psi, \theta) : X \to Y$ is _birational_ if for every $i$,
$\psi^{-1}(\eta_{i}) = {\xi_{i}}$ and $\theta^{\sharp}_{\xi_{i}} : \mathcal{O}_{\eta_{i}} \to \mathcal{O}_{\xi_{i}}$ is
an _isomorphism_. A birational morphism is dominant (0.2.1.8), and surjective if it is closed.

**Notation (2.2.10).** When no confusion threatens, we suppress the structure sheaf (resp. the morphism of structure
sheaves) from notation. For an open $U \subset X$ of a prescheme, "the prescheme $U$" means the induced prescheme on
$U$.

### 2.3. Gluing of preschemes

<!-- label: I.2.3 -->

**(2.3.1)** By (2.1.2), every ringed space obtained by gluing preschemes (0.4.1.7) is a prescheme. In particular, every
prescheme can be obtained by _gluing affine schemes_.

**Example (2.3.2).** Let $K$ be a field, $B = K[s]$, $C = K[t]$ polynomial rings; set $X_{1} = \operatorname{Spec}(B)$,
$X_{2} = \operatorname{Spec}(C)$. In `X_1` (resp. `X_2`), let $U_{12} = D(s)$ (resp. $U_{21} = D(t)$), with ring $B_{s}$
(resp. $C_{t}$). Let $u_{12} : U_{21} \to U_{12}$ be the isomorphism corresponding to $B_{s} \to C_{t}$ sending
$f(s)/s^{m}$ to $f(1/t)/(1/t^{m})$. Glue $X_{1}, X_{2}$ along $U_{12}, U_{21}$ via $u_{12}$ (no cocycle condition). The
resulting prescheme $X$ is _not_ affine: $\Gamma(X, \mathcal{O}_{X}) = K$, since a global section is a polynomial $f(s)
= g(t) = f(1/t)$ on the overlap, forcing $f = g \in K$. (This is the projective line $\mathbb{P}^{1}_{K}$; see
(II.2.4.3).)

### 2.4. Local schemes

<!-- label: I.2.4 -->

**(2.4.1)** An affine scheme $X = \operatorname{Spec}(A)$ is a _local scheme_ if $A$ is a local ring; $X$ then has a
unique closed point $a$, and $a \in \bar{b}$ for every $b \in X$ (1.1.7).

For a prescheme $Y$ and $y \in Y$, the local scheme $\operatorname{Spec}(\mathcal{O}_{y})$ is the _local scheme of $Y$
at_ $y$. For an affine open $V \subset Y$ with ring $B$ containing $y$, $\mathcal{O}_{y} \cong B_{y}$, and the canonical
$B \to B_{y}$ gives a morphism $\operatorname{Spec}(\mathcal{O}_{y}) \to V \to Y$, independent of $V$ — the _canonical
morphism_ $\operatorname{Spec}(\mathcal{O}_{y}) \to Y$.

**Proposition (2.4.2).** Let $Y$ be a prescheme. For $y \in Y$, let $(\psi, \theta) :
\operatorname{Spec}(\mathcal{O}_{y}) \to Y$ be the canonical morphism. Then $\psi$ is a homeomorphism of
$\operatorname{Spec}(\mathcal{O}_{y})$ onto the subspace $S_{y} = {z \in Y : y \in \bar{z}}$ (the _generizations_ of
$y$); for $z = \psi(\mathfrak{p})$, $\theta^{\sharp}_{z} : \mathcal{O}_{z} \to (\mathcal{O}_{y})_{\mathfrak{p}}$ is an
isomorphism. So $(\psi, \theta)$ is a monomorphism of ringed spaces.

There is thus a bijection between $\operatorname{Spec}(\mathcal{O}_{y})$ and the set of closed irreducible subsets of
$Y$ containing $y$.

**Corollary (2.4.3).** $y \in Y$ is the generic point of an irreducible component of $Y$ iff $\mathcal{O}_{y}$ has only
its maximal ideal as prime — i.e., $\mathcal{O}_{y}$ has dimension zero.

**Proposition (2.4.4).** Let $X = \operatorname{Spec}(A)$ be a local scheme with closed point $a$, and $Y$ a prescheme.
Every morphism $u = (\psi, \theta) : X \to Y$ factors uniquely as $X \to \operatorname{Spec}(\mathcal{O}_{\psi(a)}) \to
Y$, where the second arrow is the canonical morphism and the first corresponds to a local homomorphism
$\mathcal{O}_{\psi(a)} \to A$. This gives a canonical bijection between $\operatorname{Hom}(X, Y)$ and the set of local
homomorphisms $\mathcal{O}_{y} \to A$ (for $y \in Y$).

**(2.4.5)** The spectrum of a field $K$ is a single point. For $A$ a local ring with maximal ideal $\mathfrak{m}$, a
local homomorphism $A \to K$ has kernel $\mathfrak{m}$, factoring as $A \to A/\mathfrak{m} \to K$ with the second map a
field monomorphism. Thus morphisms $\operatorname{Spec}(K) \to \operatorname{Spec}(A)$ correspond bijectively to field
monomorphisms $A/\mathfrak{m} \to K$.

For $y \in Y$ and an ideal $\mathfrak{a}_{y} \subset \mathcal{O}_{y}$, the canonical $\mathcal{O}_{y} \to
\mathcal{O}_{y} / \mathfrak{a}_{y}$ gives a morphism $\operatorname{Spec}(\mathcal{O}_{y}/\mathfrak{a}_{y}) \to
\operatorname{Spec}(\mathcal{O}_{y}) \to Y$, the _canonical morphism_. When $\mathfrak{a}_{y} = \mathfrak{m}_{y}$, this
gives the morphism $\operatorname{Spec}(\kappa(y)) \to Y$.

**Corollary (2.4.6).** Let $X = \operatorname{Spec}(K)$ for $K$ a field with unique point $\xi$, and $Y$ a prescheme.
Every morphism $u : X \to Y$ factors uniquely as $X \to \operatorname{Spec}(\kappa(\psi(\xi))) \to Y$, with the first
arrow given by a field monomorphism $\kappa(\psi(\xi)) \to K$. Hence `Hom(X, Y) ↔ ⨆_{y ∈ Y} Hom_{field}(κ(y), K)`.

**Corollary (2.4.7).** For every $y \in Y$, the canonical morphism $\operatorname{Spec}(\mathcal{O}_{y} /
\mathfrak{a}_{y}) \to Y$ is a monomorphism of ringed spaces.

**Remark (2.4.8).** On a local scheme, every invertible $\mathcal{O}_{X}$-module is _trivial_ (isomorphic to
$\mathcal{O}_{X}$), since every affine open containing the closed point equals $X$. This fails for general affine
schemes; for $A$ normal, invertibility implies triviality iff $A$ is a UFD.

### 2.5. Preschemes over a prescheme

<!-- label: I.2.5 -->

**Definition (2.5.1).** Given a prescheme $S$, a _prescheme over_ $S$ (or _$S$-prescheme_) is a prescheme $X$ together
with a morphism $\phi : X \to S$, the _structure morphism_. $S$ is the _base prescheme_. When $S =
\operatorname{Spec}(A)$, $X$ is an _$A$-prescheme_; this is equivalent to making $\mathcal{O}_{X}$ a sheaf of
$A$-algebras.

Every prescheme is canonically a $\mathbb{Z}$-prescheme.

For $\phi : X \to S$ and $x \in X$, $s \in S$, $x$ is _over_ $s$ if $\phi(x) = s$. $X$ _dominates_ $S$ if $\phi$ is
dominant.

**(2.5.2)** For $S$-preschemes `X, Y`, a morphism $u : X \to Y$ is an _$S$-morphism_ (or _morphism over $S$_) if
$\phi_{Y} \circ u = \phi_{X}$. $S$-preschemes form a category, with morphism set $\operatorname{Hom}_{S}(X, Y)$; the
identity is `1_X`. When $S = \operatorname{Spec}(A)$, we say _$A$-morphism_.

**(2.5.3)** A morphism $v : X' \to X$ makes any $S$-prescheme $X$ into an $S$-prescheme $X'$; restrictions of
$S$-morphisms to open subsets are $S$-morphisms; $S$-morphisms glue from compatible restrictions on an open cover.

**(2.5.4)** A morphism $S' \to S$ makes every $S'$-prescheme into an $S$-prescheme. If $S' \subset S$ is open and an
$S$-prescheme $X$ has $\phi(X) \subset S'$, then $X$ is naturally an $S'$-prescheme.

**(2.5.5)** An _$S$-section_ of an $S$-prescheme $X$ is an $S$-morphism $S \to X$ — i.e., $\psi : S \to X$ with $\phi
\circ \psi = 1_{S}$. Write $\Gamma(X/S)$ for the set of $S$-sections.

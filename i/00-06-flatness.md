# Chapter 0 — Preliminaries

## §6. Flatness

<!-- label: 0.6 -->

**(6.0)** The notion of flatness is due to J.-P. Serre [16]; in what follows, we omit proofs that are given in N.
Bourbaki's _Algèbre commutative_, to which we refer the reader. All rings are assumed commutative.[^6-1]

If $M$, $N$ are $A$-modules and $M'$ (resp. $N'$) is a submodule of $M$ (resp. $N$), we write $Im(M' \otimes_{A} N')$
for the submodule of $M \otimes_{A} N$ that is the image of the canonical map $M' \otimes_{A} N' \to M \otimes_{A} N$.

### 6.1. Flat modules

<!-- label: 0.6.1 -->

**(6.1.1)** Let $M$ be an $A$-module. The following are equivalent:

> a) The functor $M \otimes_{A} N$ in $N$ is exact on $A$-modules; b) $Tor^{A}_{i}(M, N) = 0$ for every $i > 0$ and
> every $A$-module $N$; c) $Tor^{A}_{1}(M, N) = 0$ for every $A$-module $N$.

When $M$ satisfies these conditions, $M$ is called a _flat_ $A$-module. Every free $A$-module is plainly flat.

For $M$ to be flat, it suffices that for every _finite-type_ ideal $\mathfrak{J}$ of $A$, the canonical map $M
\otimes_{A} \mathfrak{J} \to M \otimes_{A} A = M$ be _injective_.

**(6.1.2)** Every inductive limit of flat $A$-modules is flat. A direct sum $\oplus_{\lambda \in L} M_{\lambda}$ is flat
if and only if each $M_{\lambda}$ is flat. In particular, every projective $A$-module is flat.

Let $0 \to M' \to M \to M'' \to 0$ be an exact sequence with $M''$ _flat_. Then for every $A$-module $N$,

```
0 → M′ ⊗ N → M ⊗ N → M″ ⊗ N → 0
```

is exact. Moreover, for $M$ to be flat, it is necessary and sufficient that $M'$ be flat (but $M$ and $M'$ may both be
flat without $M'' = M/M'$ being flat).

**(6.1.3)** Let $M$ be a flat $A$-module and $N$ an arbitrary $A$-module. For two submodules $N', N''$ of $N$,

```
Im(M ⊗ (N′ + N″)) = Im(M ⊗ N′) + Im(M ⊗ N″)
Im(M ⊗ (N′ ∩ N″)) = Im(M ⊗ N′) ∩ Im(M ⊗ N″)
```

(images taken in $M \otimes N$).

**(6.1.4)** Let $M$, $N$ be $A$-modules, $M'$ (resp. $N'$) a submodule of $M$ (resp. $N$), and suppose one of $M/M',
N/N'$ is flat. Then $Im(M' \otimes N') = Im(M' \otimes N) \cap Im(M \otimes N')$ (images in $M \otimes N$). In
particular, if $\mathfrak{J}$ is an ideal of $A$ and $M/M'$ is flat, then $\mathfrak{J} M' = M' \cap \mathfrak{J} M$.

### 6.2. Change of ring

<!-- label: 0.6.2 -->

When an abelian group $M$ is endowed with several module structures over rings $A$, $B$, …, instead of saying that $M$
is flat as an $A$-module, $B$-module, etc., we shall sometimes say $M$ is $A$-_flat_, $B$-_flat_, etc.

**(6.2.1)** Let `A, B` be rings, $M$ an $A$-module, and $N$ an $(A, B)$-bimodule. If $M$ is flat and $N$ is $B$-flat,
then $M \otimes_{A} N$ is $B$-flat. In particular, if `M, N` are two flat $A$-modules, $M \otimes_{A} N$ is a flat
$A$-module. If $B$ is an $A$-algebra and $M$ is a flat $A$-module, the $B$-module $M_{(B)} = M \otimes_{A} B$ is flat.
Finally, if $B$ is an $A$-algebra which is flat as an $A$-module, and $N$ is a flat $B$-module, then $N$ is also
$A$-flat.

**(6.2.2)** Let $A$ be a ring and $B$ an $A$-algebra which is flat as an $A$-module. Let `M, N` be $A$-modules with $M$
admitting a finite presentation. The canonical homomorphism

```
(6.2.2.1)    Hom_A(M, N) ⊗_A B → Hom_B(M ⊗_A B, N ⊗_A B)
```

sending $u \otimes b$ to the homomorphism $m \otimes b' \mapsto u(m) \otimes b'b$ is an isomorphism.

**(6.2.3)** Let $(A_{\lambda}, \phi_{\mu \lambda})$ be a filtered inductive system of rings with $A = \varinjlim
A_{\lambda}$. For each $\lambda$, let $M_{\lambda}$ be an $A_{\lambda}$-module, and for $\lambda \leq \mu$ let
$\theta_{\mu \lambda} : M_{\lambda} \to M_{\mu}$ be a $\phi_{\mu \lambda}$-homomorphism, with $(M_{\lambda}, \theta_{\mu
\lambda})$ an inductive system; set $M = \varinjlim M_{\lambda}$, an $A$-module. If each $M_{\lambda}$ is
$A_{\lambda}$-_flat_, then $M$ is $A$-_flat_. Indeed, let $\mathfrak{J}$ be a finite-type ideal of $A$; by the
definition of the inductive limit, there is an index $\lambda$ and an ideal $\mathfrak{J}_{\lambda} \subset A_{\lambda}$
with $\mathfrak{J} = \mathfrak{J}_{\lambda} A$. Setting $\mathfrak{J}'_{\mu} = \mathfrak{J}_{\lambda} A_{\mu}$ for $\mu
\geq \lambda$, also $\mathfrak{J} = \varinjlim \mathfrak{J}'_{\mu}$ (over $\mu \geq \lambda$). Since $\varinjlim$ is
exact and commutes with tensor products,

```
M ⊗_A 𝔍 = lim⃗ (M_μ ⊗_{A_μ} 𝔍′_μ) = lim⃗ 𝔍′_μ M_μ = 𝔍 M.
```

### 6.3. Localization of flatness

<!-- label: 0.6.3 -->

**(6.3.1)** Let $A$ be a ring and $S$ a multiplicative subset. Then $S^{-1}A$ is a flat $A$-module: for every $A$-module
$N$, $N \otimes_{A} S^{-1}A$ is identified with $S^{-1}N$ (1.2.5), and $S^{-1}N$ is exact in $N$ (1.3.2).

If $M$ is a flat $A$-module, then $S^{-1}M = M \otimes_{A} S^{-1}A$ is $S^{-1}A$-flat (6.2.1) — hence also $A$-flat by
(6.2.1). In particular, if $P$ is an $S^{-1}A$-module viewed as an $A$-module (isomorphic to $S^{-1}P$), then $P$ is
$A$-flat if and only if it is $S^{-1}A$-flat.

**(6.3.2)** Let $A$ be a ring, $B$ an $A$-algebra, and $T$ a multiplicative subset of $B$. If $P$ is a $B$-module which
is $A$-_flat_, then $T^{-1}P$ is $A$-flat. Indeed, for every $A$-module $N$,

```
(T⁻¹P) ⊗_A N = (T⁻¹B ⊗_B P) ⊗_A N = T⁻¹B ⊗_B (P ⊗_A N) = T⁻¹(P ⊗_A N);
```

$T^{-1}(P \otimes_{A} N)$ is exact in $N$ as the composite of two exact functors $P \otimes_{A} N$ (in $N$) and
$T^{-1}Q$ (in $Q$). If $S \subset A$ is multiplicative with its image in $B$ _contained_ in $T$, then $T^{-1}P =
S^{-1}(T^{-1}P)$, so also $S^{-1}A$-flat by (6.3.1).

**(6.3.3)** Let $\phi : A \to B$ be a ring homomorphism and $M$ a $B$-module. The following are equivalent:

> a) $M$ is $A$-flat; b) For every maximal ideal $\mathfrak{n}$ of $B$, $M_{\mathfrak{n}}$ is $A$-flat; c) For every
> maximal ideal $\mathfrak{n}$ of $B$, with $\mathfrak{m} = \phi^{-1}(\mathfrak{n})$, $M_{\mathfrak{n}}$ is
> $A_{\mathfrak{m}}$-flat.

Indeed, since $M_{\mathfrak{n}} = (M_{\mathfrak{n}})_{\mathfrak{m}}$, the equivalence of _b)_ and _c)_ follows from
(6.3.1), and _a)_ ⟹ _b)_ is (6.3.2). For _b)_ ⟹ _a)_: given an injective $u : N' \to N$ of $A$-modules, we must show $v
= 1 \otimes u : M \otimes_{A} N' \to M \otimes_{A} N$ is injective. Since $v$ is also a $B$-module homomorphism, it
suffices that $v_{\mathfrak{n}}$ be injective for every maximal $\mathfrak{n}$. But

```
(M ⊗_A N)_𝔫 = B_𝔫 ⊗_B (M ⊗_A N) = M_𝔫 ⊗_A N,
```

so $v_{\mathfrak{n}}$ is $1 \otimes u : M_{\mathfrak{n}} \otimes_{A} N' \to M_{\mathfrak{n}} \otimes_{A} N$, injective
since $M_{\mathfrak{n}}$ is $A$-flat.

In particular (taking $B = A$), an $A$-module $M$ is flat iff $M_{\mathfrak{m}}$ is $A_{\mathfrak{m}}$-flat for every
maximal ideal $\mathfrak{m}$ of $A$.

**(6.3.4)** Let $M$ be an $A$-module. If $M$ is flat and $f \in A$ is not a zero divisor of $A$, then $f$ annihilates no
nonzero element of $M$: the homomorphism $m \mapsto f \cdot m$ is $1 \otimes u$, where $u : a \mapsto f \cdot a$ on $A$
and $M \cong M \otimes_{A} A$; $u$ is injective, so $1 \otimes u$ is injective since $M$ is flat. In particular, if $A$
is an integral ring, $M$ is _torsion-free_.

Conversely, suppose $A$ is integral and $M$ is torsion-free, and that for every maximal $\mathfrak{m}$ of $A$,
$A_{\mathfrak{m}}$ is a _discrete valuation ring_. Then $M$ is $A$-_flat_. By (6.3.3), it suffices to show
$M_{\mathfrak{m}}$ is $A_{\mathfrak{m}}$-flat, so assume $A$ is already a DVR. Since $M = \varinjlim M_{i}$ over its
finite-type submodules (each torsion-free), one may assume $M$ is of finite type (6.1.2); then $M$ is a free $A$-module,
whence the assertion.

In particular, if $A$ is integral and $\phi : A \to B$ is a homomorphism making $B$ a flat $A$-module with $B \neq {0}$,
then $\phi$ is _injective_. Conversely, if $B$ is integral, $A$ is a subring of $B$, and $A_{\mathfrak{m}}$ is a DVR for
every maximal $\mathfrak{m}$, then $B$ is $A$-flat.

### 6.4. Faithfully flat modules

<!-- label: 0.6.4 -->

**(6.4.1)** For an $A$-module $M$, the following are equivalent:

> a) A sequence $N' \to N \to N''$ of $A$-modules is exact iff $M \otimes N' \to M \otimes N \to M \otimes N''$ is
> exact; b) $M$ is flat, and for every $A$-module $N$, $M \otimes N = 0$ implies $N = 0$; c) $M$ is flat, and for every
> homomorphism $v : N \to N'$ of $A$-modules, $1_{M} \otimes v = 0$ implies $v = 0$; d) $M$ is flat, and $\mathfrak{m} M
> \neq M$ for every maximal ideal $\mathfrak{m}$ of $A$.

When $M$ satisfies these conditions, $M$ is _faithfully flat_; $M$ is then necessarily a _faithful_ module. Moreover,
for $u : N \to N'$, $u$ is injective (resp. surjective, bijective) iff $1 \otimes u : M \otimes N \to M \otimes N'$ is.

**(6.4.2)** A nonzero free module is faithfully flat. So is the direct sum of a flat module and a faithfully flat one.
If $S \subset A$ is multiplicative, $S^{-1}A$ is faithfully flat as an $A$-module only if $S$ consists of invertible
elements (so $S^{-1}A = A$).

**(6.4.3)** Let $0 \to M' \to M \to M'' \to 0$ be exact with $M'$ and $M''$ flat. If either is faithfully flat, then $M$
is faithfully flat.

**(6.4.4)** Let `A, B` be rings, $M$ an $A$-module, and $N$ an $(A, B)$-bimodule. If $M$ is faithfully flat and $N$ is a
faithfully flat $B$-module, then $M \otimes_{A} N$ is a faithfully flat $B$-module. In particular, if `M, N` are two
faithfully flat $A$-modules, so is $M \otimes_{A} N$. If $B$ is an $A$-algebra and $M$ is a faithfully flat $A$-module,
then $M_{(B)}$ is a faithfully flat $B$-module.

**(6.4.5)** If $M$ is a faithfully flat $A$-module and $S \subset A$ is multiplicative, then $S^{-1}M$ is a faithfully
flat $S^{-1}A$-module (since $S^{-1}M = M \otimes_{A} S^{-1}A$, by (6.4.4)). Conversely, if $M_{\mathfrak{m}}$ is
faithfully flat over $A_{\mathfrak{m}}$ for every maximal $\mathfrak{m}$, then $M$ is faithfully flat over $A$: it is
$A$-flat by (6.3.3), and

```
M_𝔪 / 𝔪 M_𝔪 = (M ⊗_A A_𝔪) ⊗_{A_𝔪} (A_𝔪 / 𝔪 A_𝔪) = M ⊗_A (A/𝔪) = M / 𝔪 M,
```

so the hypothesis gives $M / \mathfrak{m} M \neq 0$ for every maximal $\mathfrak{m}$, whence (6.4.1).

### 6.5. Restriction of scalars

<!-- label: 0.6.5 -->

**(6.5.1)** Let $A$ be a ring and $\phi : A \to B$ a homomorphism making $B$ an $A$-algebra. Suppose there is a
$B$-module $N$ that is a _faithfully flat_ $A$-module. Then for every $A$-module $M$, the map $x \mapsto 1 \otimes x$
from $M$ to $B \otimes_{A} M = M_{(B)}$ is _injective_. In particular, $\phi$ is injective; for every ideal
$\mathfrak{a} \subset A$, $\phi^{-1}(\mathfrak{a} B) = \mathfrak{a}$; for every maximal (resp. prime) ideal
$\mathfrak{m} \subset A$, there is a maximal (resp. prime) ideal $\mathfrak{n} \subset B$ with $\phi^{-1}(\mathfrak{n})
= \mathfrak{m}$.

**(6.5.2)** Under the conditions of (6.5.1), one identifies $A$ with a subring of $B$ via $\phi$; more generally, $M$ is
identified with an $A$-submodule of $M_{(B)}$. Note that if $B$ is _Noetherian_, so is $A$: the map $\mathfrak{a}
\mapsto \mathfrak{a} B$ is an increasing injection from ideals of $A$ into ideals of $B$, so a strictly increasing
infinite chain of ideals of $A$ would give one of $B$.

### 6.6. Faithfully flat rings

<!-- label: 0.6.6 -->

**(6.6.1)** Let $\phi : A \to B$ be a ring homomorphism. The following are equivalent:

> a) $B$ is a faithfully flat $A$-module (equivalently, $M_{(B)}$ is _exact and faithful_ in $M$); b) $\phi$ is
> injective and $B / \phi(A)$ is $A$-flat; c) $B$ is $A$-flat (so $M_{(B)}$ is exact) and $x \mapsto 1 \otimes x$ from
> $M$ to $M_{(B)}$ is injective for every $M$; d) $B$ is $A$-flat and $\phi^{-1}(\mathfrak{a} B) = \mathfrak{a}$ for
> every ideal $\mathfrak{a} \subset A$; e) $B$ is $A$-flat and for every maximal $\mathfrak{m} \subset A$ there is a
> maximal $\mathfrak{n} \subset B$ with $\phi^{-1}(\mathfrak{n}) = \mathfrak{m}$.

Under these conditions, $A$ is identified with a subring of $B$.

**(6.6.2)** Let $A$ be a _local_ ring with maximal ideal $\mathfrak{m}$ and $B$ an $A$-algebra with $\mathfrak{m} B \neq
B$ (this holds, for example, when $B$ is local and $A \to B$ is _local_). If $B$ is $A$-_flat_, then $B$ is
$A$-_faithfully flat_. Indeed, $\mathfrak{m} B \neq B$ gives a maximal ideal $\mathfrak{n} \subset B$ containing
$\mathfrak{m} B$; $\phi^{-1}(\mathfrak{n}) \cap A$ contains $\mathfrak{m}$ and not `1`, so $\phi^{-1}(\mathfrak{n}) =
\mathfrak{m}$, and criterion _e)_ of (6.6.1) applies. Consequently, if $B$ is Noetherian, so is $A$ (6.5.2).

**(6.6.3)** Let $B$ be an $A$-algebra which is faithfully flat as an $A$-module. For every $A$-module $M$ and submodule
$M' \subset M$, identifying $M$ with a submodule of $M_{(B)}$, one has $M' = M \cap M'_{(B)}$. For $M$ to be $A$-flat
(resp. faithfully flat), it is necessary and sufficient that $M_{(B)}$ be $B$-flat (resp. faithfully flat).

**(6.6.4)** Let $B$ be an $A$-algebra and $N$ a faithfully flat $B$-module. For $B$ to be $A$-flat (resp. faithfully
flat), it is necessary and sufficient that $N$ be.

In particular, let $C$ be a $B$-algebra. If $C$ is faithfully flat over $B$ and $B$ is faithfully flat over $A$, then
$C$ is faithfully flat over $A$. If $C$ is faithfully flat over $B$ and over $A$, then $B$ is faithfully flat over $A$.

### 6.7. Flat morphisms of ringed spaces

<!-- label: 0.6.7 -->

**(6.7.1)** Let $f : X \to Y$ be a morphism of ringed spaces and $\mathcal{F}$ an $\mathcal{O}_{X}$-Module.
$\mathcal{F}$ is $f$-_flat_ (or $Y$-_flat_ when no confusion about $f$ can arise) _at a point_ $x \in X$ if
$\mathcal{F}_{x}$ is a flat $\mathcal{O}_{f(x)}$-module; $\mathcal{F}$ is $f$-flat _over_ $y \in Y$ if it is $f$-flat at
every $x \in f^{-1}(y)$; $\mathcal{F}$ is $f$-_flat_ if it is $f$-flat at every point of $X$. The morphism $f$ is _flat
at_ $x \in X$ (resp. _flat over_ $y \in Y$, resp. _flat_) if $\mathcal{O}_{X}$ is $f$-flat at $x$ (resp. over $y$, resp.
$f$-flat).

**(6.7.2)** With the notation of (6.7.1), if $\mathcal{F}$ is $f$-flat at $x$, then for every open neighborhood $U$ of
$y = f(x)$, the functor $(f*(\mathcal{G}) \otimes_{\mathcal{O}_{X}} \mathcal{F})_{x}$ in $\mathcal{G}$ is _exact_ on
$(\mathcal{O}_{Y}|U)$-Modules: this stalk is canonically $\mathcal{G}_{y} \otimes_{\mathcal{O}_{y}} \mathcal{F}_{x}$,
whence the assertion. In particular, if $f$ is a flat morphism, $f*$ is exact on $\mathcal{O}_{Y}$-Modules.

**(6.7.3)** Conversely, suppose $\mathcal{O}_{Y}$ is _coherent_, and that for _every_ open neighborhood $U$ of $y$, the
functor $(f*(\mathcal{G}) \otimes_{\mathcal{O}_{X}} \mathcal{F})_{x}$ is exact in $\mathcal{G}$ on _coherent_
$(\mathcal{O}_{Y}|U)$-Modules. Then $\mathcal{F}$ is $f$-_flat at_ $x$. It suffices to show that for every finite-type
ideal $\mathfrak{J} \subset \mathcal{O}_{y}$, the canonical map $\mathfrak{J} \otimes_{\mathcal{O}_{y}} \mathcal{F}_{x}
\to \mathcal{F}_{x}$ is injective (6.1.1). By (5.3.8) there is an open $U \ni y$ and a coherent ideal sheaf $\mathcal{J}
\subset \mathcal{O}_{Y}|U$ with $\mathcal{J}_{y} = \mathfrak{J}$, whence the conclusion.

**(6.7.4)** The results of (6.1) on flat modules carry over at once to propositions on $f$-flat sheaves at a point:

If $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ is exact and $\mathcal{F}''$ is $f$-flat at $x$, then
for every open $U \ni y = f(x)$ and every $(\mathcal{O}_{Y}|U)$-Module $\mathcal{G}$, the sequence

```
0 → (f*(𝒢) ⊗_{𝒪_X} ℱ′)_x → (f*(𝒢) ⊗_{𝒪_X} ℱ)_x → (f*(𝒢) ⊗_{𝒪_X} ℱ″)_x → 0
```

is exact. For $\mathcal{F}$ to be $f$-flat at $x$, it is necessary and sufficient that $\mathcal{F}'$ be. Analogous
statements hold for $f$-flatness over $y \in Y$ and $f$-flatness on $X$.

**(6.7.5)** Let $f : X \to Y$ and $g : Y \to Z$ be morphisms of ringed spaces, $x \in X$, $y = f(x)$, and $\mathcal{F}$
an $\mathcal{O}_{X}$-Module. If $\mathcal{F}$ is $f$-flat at $x$ and $g$ is flat at $y$, then $\mathcal{F}$ is $(g \circ
f)$-flat at $x$ (6.2.1). In particular, if $f$ and $g$ are flat, so is $g \circ f$.

**(6.7.6)** Let `X, Y` be ringed spaces and $f : X \to Y$ a _flat_ morphism. The canonical homomorphism of bifunctors
(4.4.6)

```
(6.7.6.1)    f*(ℋom_{𝒪_Y}(ℱ, 𝒢)) → ℋom_{𝒪_X}(f*(ℱ), f*(𝒢))
```

is an _isomorphism_ when $\mathcal{F}$ admits a finite presentation (5.2.5).

Indeed, the question being local, one may assume an exact sequence $\mathcal{O}^{m}_{Y} \to \mathcal{O}^{n}_{Y} \to
\mathcal{F} \to 0$. Both sides of (6.7.6.1) are left exact in $\mathcal{F}$ (using flatness of $f$), so one reduces to
$\mathcal{F} = \mathcal{O}_{Y}$, where the assertion is trivial.

**(6.7.8)** A morphism $f : X \to Y$ of ringed spaces is _faithfully flat_ if $f$ is _surjective_ and, for every $x \in
X$, $\mathcal{O}_{x}$ is a faithfully flat $\mathcal{O}_{f(x)}$-module. When `X, Y` are spaces ringed in local rings
(5.5.1), this amounts to $f$ being surjective and flat (6.6.2). When $f$ is faithfully flat, $f*$ is exact and faithful
on $\mathcal{O}_{Y}$-Modules (6.6.1, _a)_), and an $\mathcal{O}_{Y}$-Module $\mathcal{G}$ is $Y$-flat iff
$f*(\mathcal{G})$ is (6.6.3).

[^6-1]: See the cited exposé of N. Bourbaki for the generalization of most results to the noncommutative case.

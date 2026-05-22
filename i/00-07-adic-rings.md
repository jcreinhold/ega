# Chapter 0 — Preliminaries

## §7. Adic Rings

<!-- label: 0.7 -->

### 7.1. Admissible rings

<!-- label: 0.7.1 -->

**(7.1.1)** Recall that in a topological ring $A$ (not necessarily separated), an element $x$ is _topologically
nilpotent_ if `0` is a limit of the sequence $(x^{n})_{n \geq 0}$. A topological ring $A$ is _linearly topologized_ if
there is a fundamental system of neighborhoods of `0` in $A$ consisting of (necessarily _open_) _ideals_.

**Definition (7.1.2).** In a linearly topologized ring $A$, an _ideal of definition_ is an open ideal $\mathfrak{J}$
such that for every neighborhood $V$ of `0` there is $n > 0$ with $\mathfrak{J}^{n} \subset V$ (by abuse of language:
_the sequence $(\mathfrak{J}^{n})$ tends to_ `0`). $A$ is _preadmissible_ if there is an ideal of definition in $A$; it
is _admissible_ if it is preadmissible, separated, and complete.

Plainly, if $\mathfrak{J}$ is an ideal of definition and $\mathfrak{L}$ an open ideal, then $\mathfrak{J} \cap
\mathfrak{L}$ is also an ideal of definition; so the ideals of definition of a preadmissible ring form a _fundamental
system of neighborhoods of_ `0`.

**Lemma (7.1.3).** Let $A$ be a linearly topologized ring.

> (i) For $x \in A$ to be topologically nilpotent, it is necessary and sufficient that for every open ideal
> $\mathfrak{J} \subset A$, the canonical image of $x$ in $A/\mathfrak{J}$ be nilpotent. The set $\mathfrak{T}$ of
> topologically nilpotent elements of $A$ is an ideal. (ii) Suppose $A$ is preadmissible and $\mathfrak{J}$ is an ideal
> of definition. Then $x$ is topologically nilpotent iff its image in $A/\mathfrak{J}$ is nilpotent; $\mathfrak{T}$ is
> the inverse image of the nilradical of $A/\mathfrak{J}$, and is therefore open.

**Proof.** (i) follows from the definitions. For (ii): for every neighborhood $V$ of `0`, some $\mathfrak{J}^{n} \subset
V$; if $x^{m} \in \mathfrak{J}$, then $x^{mq} \in V$ for $q \geq n$, so $x$ is topologically nilpotent.

**Proposition (7.1.4).** Let $A$ be a preadmissible ring with ideal of definition $\mathfrak{J}$.

> (i) For $\mathfrak{J}' \subset A$ to be contained in an ideal of definition, it is necessary and sufficient that
> $\mathfrak{J}'^{n} \subset \mathfrak{J}$ for some $n > 0$. (ii) For $x \in A$ to be contained in an ideal of
> definition, it is necessary and sufficient that $x$ be topologically nilpotent.

**Corollary (7.1.5).** In a preadmissible ring $A$, every open prime ideal contains every ideal of definition.

**Corollary (7.1.6).** Under the hypotheses of (7.1.4), the following are equivalent for an ideal $\mathfrak{J}_{0}$:

> (a) $\mathfrak{J}_{0}$ is the largest ideal of definition; (b) $\mathfrak{J}_{0}$ is a maximal ideal of definition;
> (c) $\mathfrak{J}_{0}$ is an ideal of definition such that $A/\mathfrak{J}_{0}$ is reduced.

Such $\mathfrak{J}_{0}$ exists if and only if the nilradical of $A/\mathfrak{J}$ is nilpotent; $\mathfrak{J}_{0}$ is
then the ideal $\mathfrak{T}$ of topologically nilpotent elements.

When the nilradical of $A/\mathfrak{J}$ is nilpotent, we write $A_{red}$ for the reduced quotient $A/\mathfrak{T}$.

**Corollary (7.1.7).** A preadmissible Noetherian ring has a largest ideal of definition.

**Corollary (7.1.8).** If $A$ is preadmissible and the powers $\mathfrak{J}^{n}$ ($n > 0$) of some ideal of definition
$\mathfrak{J}$ form a fundamental system of neighborhoods of `0`, the same holds for $\mathfrak{J}'^{n}$ for every ideal
of definition $\mathfrak{J}'$.

**Definition (7.1.9).** A preadmissible ring $A$ is _preadic_ if there is an ideal of definition $\mathfrak{J}$ whose
powers $\mathfrak{J}^{n}$ form a fundamental system of neighborhoods of `0` (equivalently, the $\mathfrak{J}^{n}$ are
open). An _adic_ ring is a separated and complete preadic ring.

If $\mathfrak{J}$ is an ideal of definition of a preadic (resp. adic) ring $A$, we also say $A$ is _𝔍-preadic_ (resp.
_𝔍-adic_), and its topology is the _𝔍-preadic_ (resp. _𝔍-adic_) topology. For an $A$-module $M$, the topology with
fundamental system of neighborhoods the submodules $\mathfrak{J}^{n}M$ is called the _𝔍-preadic_ (resp. _𝔍-adic_)
topology. By (7.1.8), these topologies are independent of the choice of ideal of definition $\mathfrak{J}$.

**Proposition (7.1.10).** Let $A$ be an admissible ring and $\mathfrak{J}$ an ideal of definition. Then $\mathfrak{J}$
is contained in the radical of $A$.

This is equivalent to any of the following:

**Corollary (7.1.11).** For every $x \in \mathfrak{J}$, $1 + x$ is invertible in $A$.

**Corollary (7.1.12).** For $f \in A$ to be invertible, it is necessary and sufficient that its image in
$A/\mathfrak{J}$ be invertible.

**Corollary (7.1.13).** For every $A$-module $M$ of finite type, $M = \mathfrak{J}M$ (equivalent to $M \otimes_{A}
(A/\mathfrak{J}) = 0$) implies $M = 0$.

**Corollary (7.1.14).** Let $u : M \to N$ be an $A$-module homomorphism with $N$ of finite type. For $u$ to be
surjective, it is necessary and sufficient that $u \otimes 1 : M \otimes_{A} (A/\mathfrak{J}) \to N \otimes_{A}
(A/\mathfrak{J})$ be.

**Proof of (7.1.10).** The equivalences with (7.1.11), (7.1.13), and (7.1.12) follow from standard results of Bourbaki
(_Alg._, Chap. VIII). To prove (7.1.11): since $A$ is separated and complete and $(\mathfrak{J}^{n})$ tends to `0`, the
series $\sum^{\infty}_{n=0} (-1)^{n} x^{n}$ converges in $A$; its sum $y$ satisfies $y(1 + x) = 1$.

### 7.2. Adic rings and projective limits

<!-- label: 0.7.2 -->

**(7.2.1)** Every projective limit of _discrete_ rings is plainly a linearly topologized, separated, and complete ring.
Conversely, let $A$ be linearly topologized with $(\mathfrak{J}_{\lambda})$ a fundamental system of open neighborhoods
of `0` consisting of ideals. The canonical maps $\phi_{\lambda} : A \to A/\mathfrak{J}_{\lambda}$ form a projective
system, defining a continuous map $\phi : A \to \varprojlim A/\mathfrak{J}_{\lambda}$; if $A$ is _separated_, $\phi$ is
a topological isomorphism onto a dense subring; if also _complete_, $\phi$ is a topological isomorphism onto
$\varprojlim A/\mathfrak{J}_{\lambda}$.

**Lemma (7.2.2).** A linearly topologized ring is admissible if and only if it is isomorphic to a projective limit $A =
\varprojlim A_{\lambda}$ of discrete rings indexed by a filtered ordered set $L$ with smallest element `0`, such that:

> 1. each $u_{\lambda} : A \to A_{\lambda}$ is surjective;
> 1. the kernel $\mathfrak{J}_{\lambda}$ of $u_{0\lambda} : A_{\lambda} \to A_{0}$ is nilpotent.

When this holds, the kernel $\mathfrak{J}$ of $u_{0} : A \to A_{0}$ equals $\varprojlim \mathfrak{J}_{\lambda}$.

**(7.2.3)** Let $A$ be admissible and $\mathfrak{J} \subset A$ an ideal contained in an ideal of definition
(equivalently, $(\mathfrak{J}^{n})$ tends to `0`). The ring topology on $A$ having the $\mathfrak{J}^{n}$ ($n > 0$) as
fundamental system of neighborhoods of `0` — also called the _𝔍-preadic_ topology — is separated, since $\bigcap_{n}
\mathfrak{J}^{n} = 0$. Let $\hat{A} = \varprojlim A/\mathfrak{J}^{n}$ (the $A/\mathfrak{J}^{n}$ discrete) be the
completion for this topology, and let $u : A \to \hat{A}$ be the (possibly discontinuous) projective limit of $u_{n} : A
\to A/\mathfrak{J}^{n}$. The $\mathfrak{J}$-preadic topology is finer than the given topology $\mathcal{T}$; extending
the identity of $A$ (with $\mathfrak{J}$-preadic topology) by continuity to $\mathcal{T}$ gives a continuous map $v :
\hat{A} \to A$.

**Proposition (7.2.4).** If $A$ is admissible and $\mathfrak{J}$ is contained in an ideal of definition, then $A$ is
separated and complete for the $\mathfrak{J}$-preadic topology.

**Proof.** With the notation of (7.2.3), $v \circ u = id_{A}$ directly, and $u_{n} \circ v$ is the canonical $\hat{A}
\to A/\mathfrak{J}^{n}$, so $u \circ v = id_{\hat{A}}$.

**Corollary (7.2.5).** Under the hypotheses of (7.2.3), the following are equivalent:

> (a) $u$ is continuous; (b) $v$ is bicontinuous; (c) $A$ is $\mathfrak{J}$-adic.

**Corollary (7.2.6).** Let $A$ be an admissible ring and $\mathfrak{J}$ an ideal of definition. $A$ is Noetherian if and
only if $A/\mathfrak{J}$ is Noetherian and $\mathfrak{J}/\mathfrak{J}^{2}$ is an $A/\mathfrak{J}$-module of finite type.

The conditions are clearly necessary. Conversely, by (7.2.4) $A$ is complete for the $\mathfrak{J}$-preadic topology, so
it is Noetherian if and only if the associated graded ring $grad(A)$ (for the filtration $(\mathfrak{J}^{n})$) is.
Choosing $a_{1}, \cdots, a_{n} \in \mathfrak{J}$ with classes mod $\mathfrak{J}^{2}$ generating
$\mathfrak{J}/\mathfrak{J}^{2}$, induction shows their degree-$m$ monomials generate
$\mathfrak{J}^{m}/\mathfrak{J}^{m+1}$ as $A/\mathfrak{J}$-module. Hence $grad(A)$ is a quotient of
$(A/\mathfrak{J})[T_{1}, \cdots, T_{n}]$.

**Proposition (7.2.7).** Let $(A_{i}, u_{ij})$ ($i \in \mathbb{N}$) be a projective system of discrete rings, and let
$\mathfrak{J}_{i} \subset A_{i}$ be the kernel of $u_{0i} : A_{i} \to A_{0}$. Suppose:

> (a) For $i \leq j$, $u_{ij}$ is surjective with kernel $\mathfrak{J}^{i+1}_{j}$ (so $A_{i} \cong A_{j} /
> \mathfrak{J}^{i+1}_{j}$). (b) $\mathfrak{J}_{1} / \mathfrak{J}^{2}_{1}$ ($= \mathfrak{J}_{1}$) is finite-type over
> $A_{0} = A_{1} / \mathfrak{J}_{1}$.

Let $A = \varprojlim_{i} A_{i}$, $u_{n} : A \to A_{n}$ the canonical map, and $\mathfrak{J}^{(n+1)} \subset A$ its
kernel. Then:

> (i) $A$ is adic, with $\mathfrak{J} = \mathfrak{J}^{(1)}$ an ideal of definition. (ii) $\mathfrak{J}^{(n)} =
> \mathfrak{J}^{n}$ for every $n \geq 1$. (iii) $\mathfrak{J} / \mathfrak{J}^{2}$ is isomorphic to $\mathfrak{J}_{1}$,
> hence finite-type over $A_{0} = A / \mathfrak{J}$.

**Proof.** The surjectivity of the $u_{ij}$ makes each $u_{n}$ surjective; (a) gives $\mathfrak{J}^{j+1}_{j} = 0$, so
$A$ is admissible by (7.2.2). The $\mathfrak{J}^{(n)}$ form a fundamental system of neighborhoods of `0`, so (ii) ⟹ (i).
Since $\mathfrak{J} = \varprojlim_{i} \mathfrak{J}_{i}$ with surjective maps to $\mathfrak{J}_{i}$, (ii) ⟹ (iii). For
(ii): $\mathfrak{J}^{(n)}$ consists of $(x_{k})$ with $x_{k} = 0$ for $k < n$, so $\mathfrak{J}^{(n)} \cdot
\mathfrak{J}^{(m)} \subset \mathfrak{J}^{(n+m)}$ — a filtration. Also $\mathfrak{J}^{(n)} / \mathfrak{J}^{(n+1)}$
projects to $\mathfrak{J}^{n}_{n}$ (an `A_0`-module). Choose $r$ elements $a_{j} = (a_{jk})$ of $\mathfrak{J}$ whose
$a_{j1}$ generate $\mathfrak{J}_{1}$ over `A_0`. We show by induction that monomials of degree $n$ in the $a_{j}$
generate $\mathfrak{J}^{(n)}$; the same argument (passage to graded modules) closes the induction.

**Corollary (7.2.8).** Under the hypotheses of (7.2.7), $A$ is Noetherian if and only if `A_0` is.

**Proof.** By (7.2.6).

**Proposition (7.2.9).** Under the hypotheses of (7.2.7), for each $i$ let $M_{i}$ be an $A_{i}$-module, and for $i \leq
j$ let $v_{ij} : M_{j} \to M_{i}$ be a $u_{ij}$-homomorphism with $(M_{i}, v_{ij})$ a projective system. Suppose `M_0`
is `A_0`-finite-type and each $v_{ij}$ is surjective with kernel $\mathfrak{J}^{i+1}_{j} M_{j}$. Then $M = \varprojlim
M_{i}$ is an $A$-module of finite type, and the kernel of the surjective $v_{n} : M \to M_{n}$ is $\mathfrak{J}^{n+1} M$
(so $M_{n} \cong M / \mathfrak{J}^{n+1} M = M \otimes_{A} (A / \mathfrak{J}^{n+1})$).

**Proof.** Choose $s$ elements $z_{h} = (z_{hk}) \in M$ such that the $z_{h0}$ generate `M_0`. Reducing to showing the
$z_{hn}$ generate $M_{n}$ over $A_{n}$, induction on $n$ using $M_{n-1} = M_{n} / \mathfrak{J}^{n}_{n} M_{n}$ plus
Nakayama closes the argument. Passage to graded modules then gives $\mathfrak{J}^{(n)} M = \mathfrak{J}^{n} M$, the
kernel of $M \to M_{n-1}$.

**Corollary (7.2.10).** Let $(N_{i}, w_{ij})$ be a second such projective system, $N = \varprojlim N_{i}$. There is a
bijective correspondence between projective systems $(h_{i})$ of $A_{i}$-homomorphisms $M_{i} \to N_{i}$ and
$A$-homomorphisms $M \to N$ (necessarily continuous for the $\mathfrak{J}$-adic topologies).

**Remark (7.2.11).** Let $A$ be adic with ideal of definition $\mathfrak{J}$ such that $\mathfrak{J}/\mathfrak{J}^{2}$
is $A/\mathfrak{J}$-finite-type. The $A_{i} = A / \mathfrak{J}^{i+1}$ satisfy (7.2.7), and $A = \varprojlim A_{i}$. Thus
(7.2.7) describes _all_ adic rings of this type — in particular all _adic Noetherian_ rings.

**Example (7.2.12).** Let $B$ be a ring, $\mathfrak{J} \subset B$ an ideal with $\mathfrak{J}/\mathfrak{J}^{2}$
finite-type over $B/\mathfrak{J}$; set $A = \varprojlim_{n} B / \mathfrak{J}^{n+1}$. Then $A$ is the separated
$\mathfrak{J}$-preadic completion of $B$. The $A_{n} = B / \mathfrak{J}^{n+1}$ satisfy (7.2.7); so $A$ is adic, the
closure $\bar{\mathfrak{J}}$ in $A$ of the image of $\mathfrak{J}$ is an ideal of definition, $\bar{\mathfrak{J}}^{n}$
is the closure of the image of $\mathfrak{J}^{n}$, $A / \bar{\mathfrak{J}}^{n} \cong B / \mathfrak{J}^{n}$, and
$\bar{\mathfrak{J}} / \bar{\mathfrak{J}}^{2}$ is isomorphic to $\mathfrak{J} / \mathfrak{J}^{2}$ as
$A/\bar{\mathfrak{J}}$-module. Likewise, if $N$ is a $B$-module with $N/\mathfrak{J}N$ finite-type, then $M =
\varprojlim_{i} N/\mathfrak{J}^{i+1} N$ is $A$-finite-type, isomorphic to the separated $\mathfrak{J}$-preadic
completion of $N$.

### 7.3. Preadic Noetherian rings

<!-- label: 0.7.3 -->

**(7.3.1)** Let $A$ be a ring, $\mathfrak{J} \subset A$ an ideal, $M$ an $A$-module. Write $\hat{A} = \varprojlim_{n}
A/\mathfrak{J}^{n}$ (resp. $\hat{M} = \varprojlim_{n} M/\mathfrak{J}^{n} M$) for the separated $\mathfrak{J}$-preadic
completion of $A$ (resp. $M$). For an exact sequence $M' \xrightarrow{u} M \xrightarrow{v} M'' \to 0$, the sequence
$M'/\mathfrak{J}^{n} M' \to M/\mathfrak{J}^{n} M \to M''/\mathfrak{J}^{n} M'' \to 0$ is exact for each $n$. Since
$v(\mathfrak{J}^{n} M) = \mathfrak{J}^{n} M''$, the limit $\hat{v} = \varprojlim v_{n}$ is surjective. For $z = (z_{k})
\in Ker \hat{v}$, lift each $z_{k}$ to $z_{k}' \in M'/\mathfrak{J}^{k} M'$; we find $z' = (z_{n}') \in \hat{M}'$ whose
first $k$ components under `û` match $z$. So $Im(\hat{u})$ is _dense_ in $Ker \hat{v}$.

If $A$ is _Noetherian_, so is `Â` by (7.2.12), and $\mathfrak{J}/\mathfrak{J}^{2}$ is $A$-finite-type. We also have:

**Theorem (7.3.2) (Krull).** Let $A$ be a Noetherian ring, $\mathfrak{J} \subset A$ an ideal, $M$ an $A$-module of
finite type, and $M' \subset M$ a submodule. Then the topology on $M'$ induced from the $\mathfrak{J}$-preadic topology
of $M$ agrees with the $\mathfrak{J}$-preadic topology of $M'$.

This follows from:

**Lemma (7.3.2.1) (Artin–Rees).** Under the hypotheses of (7.3.2), there is $p \geq 0$ with $M' \cap \mathfrak{J}^{n} M
= \mathfrak{J}^{n-p}(M' \cap \mathfrak{J}^{p} M)$ for $n \geq p$. (Bourbaki, _Alg. comm._)

**Corollary (7.3.3).** Under the hypotheses of (7.3.2), the canonical map $M \otimes_{A} \hat{A} \to \hat{M}$ is
bijective, and $M \otimes_{A} \hat{A}$ is exact in $M$ on $A$-modules of finite type; consequently `Â` is a flat
$A$-module (6.1.1).

**Proof.** First, $\hat{M}$ is exact on $A$-modules of finite type: for $0 \to M' \to M \to M'' \to 0$ exact, Krull
(7.3.2) shows the closure of the image of $M'$ in $\hat{M}$ is the completion of $M'$, so `û` is injective. The
canonical $M \otimes_{A} \hat{A} \to \hat{M}$ is bijective when $M = A^{p}$; for general $M$ of finite type, take a
presentation $A^{p} \to A^{q} \to M \to 0$ and apply right exactness of both functors.

**Corollary (7.3.4).** For $A$ Noetherian, $\mathfrak{J} \subset A$ an ideal, and `M, N` of finite type, there are
canonical functorial isomorphisms

```
(M ⊗_A N)^∧ ≅ M̂ ⊗_Â N̂,    (Hom_A(M, N))^∧ ≅ Hom_Â(M̂, N̂).
```

This follows from (7.3.3), (6.2.1), and (6.2.2).

**Corollary (7.3.5).** Let $A$ be Noetherian and $\mathfrak{J} \subset A$ an ideal. The following are equivalent:

> (a) $\mathfrak{J}$ is contained in the radical of $A$; (b) `Â` is a faithfully flat $A$-module (6.4.1); (c) Every
> $A$-module of finite type is separated for the $\mathfrak{J}$-preadic topology; (d) Every submodule of an $A$-module
> of finite type is closed for the $\mathfrak{J}$-preadic topology.

**Proof.** (b) ⟺ (c) by flatness of `Â` and (6.6.1). (c) ⟹ (d): if $N \subset M$ with $M$ of finite type, $M/N$ is
separated. (d) ⟹ (a): for $\mathfrak{m} \subset A$ maximal, $\mathfrak{m} = \bigcap_{p} (\mathfrak{m} +
\mathfrak{J}^{p})$; for large $p$, $\mathfrak{m} + \mathfrak{J}^{p} = \mathfrak{m}$, so $\mathfrak{J}^{p} \subset
\mathfrak{m}$, hence $\mathfrak{J} \subset \mathfrak{m}$. (a) ⟹ (b): let $P$ be the closure of `{0}` in an $M$ of finite
type for the $\mathfrak{J}$-preadic topology; by Krull, the induced topology on $P$ is the $\mathfrak{J}$-preadic, so
$\mathfrak{J} P = P$; Nakayama gives $P = 0$.

The conditions hold when $A$ is local Noetherian and $\mathfrak{J} \neq A$.

**Corollary (7.3.6).** If $A$ is $\mathfrak{J}$-preadic Noetherian, every $A$-module of finite type is separated and
complete for the $\mathfrak{J}$-preadic topology.

**Proof.** $\hat{A} = A$, so this follows from (7.3.3).

So (7.2.9) describes _all_ finite-type modules over an adic Noetherian ring.

**Corollary (7.3.7).** Under the hypotheses of (7.3.2), the kernel of $M \to \hat{M} = M \otimes_{A} \hat{A}$ is the set
of $x \in M$ killed by an element of $1 + \mathfrak{J}$.

### 7.4. Quasi-finite modules over local rings

<!-- label: 0.7.4 -->

**Definition (7.4.1).** Let $A$ be a local ring with maximal ideal $\mathfrak{m}$. An $A$-module $M$ is _quasi-finite_
(over $A$) if $M/\mathfrak{m}M$ is of finite rank over the residue field $k = A/\mathfrak{m}$.

When $A$ is Noetherian, the $\mathfrak{m}$-preadic completion $\hat{M}$ is then an `Â`-module of finite type; this
follows from (7.2.12) and the hypothesis on $M/\mathfrak{m}M$.

In particular, if $A$ is also complete and $M$ is separated for the $\mathfrak{m}$-preadic topology (i.e. $\bigcap_{n}
\mathfrak{m}^{n} M = 0$), then $M$ is $A$-finite-type: $\hat{M}$ is $A$-finite-type, $M \hookrightarrow \hat{M}$, and so
$M$ is also finite-type (and equal to its completion, by (7.3.6)).

**Proposition (7.4.2).** Let $A$, $B$ be local rings with maximal ideals $\mathfrak{m}$, $\mathfrak{n}$, and suppose $B$
is Noetherian. Let $\phi : A \to B$ be a local homomorphism, $M$ a $B$-module of finite type. If $M$ is
$A$-quasi-finite, then the $\mathfrak{m}$-preadic and $\mathfrak{n}$-preadic topologies on $M$ agree (so both are
separated).

**Proof.** $M/\mathfrak{m}M$ has finite length as $A$-module, hence as $B$-module. Therefore $\mathfrak{n}$ is the
unique prime ideal of $B$ containing $Ann(M/\mathfrak{m}M)$: reducing to $M/\mathfrak{m}M$ simple, we have
$M/\mathfrak{m}M \cong B/\mathfrak{n}$. By (0.1.7.5), the primes containing $Ann(M/\mathfrak{m}M)$ are those containing
$\mathfrak{m}B + \mathfrak{b}$, where $\mathfrak{b} = Ann_{B} M$. Since $B$ is Noetherian, $\mathfrak{m}B +
\mathfrak{b}$ is an ideal of definition for $B$; so for some $k > 0$, $\mathfrak{n}^{k} \subset \mathfrak{m}B +
\mathfrak{b} \subset \mathfrak{n}$, giving for every $h > 0$

```
𝔫^{hk} ⊂ (𝔪B + 𝔟)^h M = 𝔪^h M ⊂ 𝔫^h M.
```

Hence the two topologies agree; separation follows from (7.3.5).

**Corollary (7.4.3).** Under the hypotheses of (7.4.2), if $A$ is also Noetherian and complete for the
$\mathfrak{m}$-preadic topology, then $M$ is $A$-finite-type.

**(7.4.4)** The most important case of (7.4.2) is when $B$ is $A$-quasi-finite — i.e., $B/\mathfrak{m}B$ is a
finite-rank $k = A/\mathfrak{m}$-algebra. This breaks into:

> (i) $\mathfrak{m}B$ is an ideal of definition for $B$; (ii) $B/\mathfrak{n}$ is a finite-rank extension of
> $A/\mathfrak{m}$.

Then every $B$-module of finite type is $A$-quasi-finite.

**Corollary (7.4.5).** Under the hypotheses of (7.4.2), if $\mathfrak{b} = Ann_{B}(M)$, then $B/\mathfrak{b}$ is
$A$-quasi-finite.

### 7.5. Rings of restricted formal series

<!-- label: 0.7.5 -->

**(7.5.1)** Let $A$ be a linearly topologized ring, separated and complete; let $(\mathfrak{J}_{\lambda})$ be a
fundamental system of open ideals with $A \cong \varprojlim A/\mathfrak{J}_{\lambda}$ (7.2.1). For each $\lambda$, set
$B_{\lambda} = (A/\mathfrak{J}_{\lambda})[T_{1}, \cdots, T_{r}]$; the $B_{\lambda}$ form a projective system of discrete
rings. Set

```
A{T_1, …, T_r} = lim⃖ B_λ.
```

This ring is independent of $(\mathfrak{J}_{\lambda})$. Concretely, let $A'$ be the subring of $A[[T_{1}, \cdots,
T_{r}]]$ consisting of formal series $\sum_{\alpha} c_{\alpha} T^{\alpha}$ ($\alpha = (\alpha_{1}, \cdots, \alpha_{r})
\in \mathbb{N}_{r}$) with $\lim c_{\alpha} = 0$ (along the filter of cofinite subsets of $\mathbb{N}_{r}$); call these
_restricted formal series_ in the $T_{i}$ with coefficients in $A$. With the topology whose fundamental system of
neighborhoods of `0` consists of ${\sum c_{\alpha} T^{\alpha} : c_{\alpha} \in V}$ for $V$ a neighborhood of `0` in $A$,
$A'$ is a separated topological ring. There is a canonical topological isomorphism $A{T_{1}, \cdots, T_{r}}
\xrightarrow{\sim} A'$, given by sending $y \in A{T_{1}, \cdots, T_{r}}$ to $\sum_{\alpha} \phi_{\alpha}(y) T^{\alpha}$,
where $\phi_{\alpha}$ extracts the coefficient of $T^{\alpha}$ (the result is restricted because almost all components
vanish in each $A/\mathfrak{J}_{\lambda}$).

**(7.5.2)** Identify $A{T_{1}, \cdots, T_{r}}$ with the ring of restricted formal series via (7.5.1). The canonical
isomorphisms $(A/\mathfrak{J}_{\lambda})[T_{1}, \cdots, T_{r}][T_{r+1}, \cdots, T_{s}] \cong
(A/\mathfrak{J}_{\lambda})[T_{1}, \cdots, T_{s}]$ give a canonical isomorphism

```
(A{T_1, …, T_r}){T_{r+1}, …, T_s} ≅ A{T_1, …, T_s}.
```

**(7.5.3) Universal property.** For every continuous homomorphism $u : A \to B$ to a linearly topologized, separated,
complete ring $B$, and every system $(b_{1}, \cdots, b_{r})$ in $B$, there is a _unique_ continuous homomorphism
$\bar{u} : A{T_{1}, \cdots, T_{r}} \to B$ with $\bar{u}|A = u$ and $\bar{u}(T_{j}) = b_{j}$, namely

```
ū(∑_α c_α T^α) = ∑_α u(c_α) b_1^{α_1} ⋯ b_r^{α_r}.
```

This characterizes $A{T_{1}, \cdots, T_{r}}$ up to unique isomorphism.

**Proposition (7.5.4).**

> (i) If $A$ is admissible, so is $A' = A{T_{1}, \cdots, T_{r}}$. (ii) If $A$ is $\mathfrak{J}$-adic with
> $\mathfrak{J}/\mathfrak{J}^{2}$ finite-type over $A/\mathfrak{J}$, then setting $\mathfrak{J}' = \mathfrak{J} A'$,
> $A'$ is $\mathfrak{J}'$-adic with $\mathfrak{J}'/\mathfrak{J}'^{2}$ finite-type over $A'/\mathfrak{J}'$. If $A$ is
> Noetherian, so is $A'$.

**Proof.** (i) For an ideal of definition $\mathfrak{J} \subset A$, let $\mathfrak{J}' \subset A'$ consist of $\sum
c_{\alpha} T^{\alpha}$ with all $c_{\alpha} \in \mathfrak{J}$. Then $\mathfrak{J}'^{n} \subset (\mathfrak{J}^{n})'$, so
$\mathfrak{J}'$ is an ideal of definition. (ii) Apply (7.2.7) to the projective system $A_{i}' = A_{i}[T_{1}, \cdots,
T_{r}]$ with $A_{i} = A/\mathfrak{J}^{i+1}$. (One checks the kernels match $\mathfrak{J}_{j}'^{i+1}$ using induction;
details omitted.) Noetherianness follows from (7.2.8).

**Proposition (7.5.5).** Let $A$ be a Noetherian $\mathfrak{J}$-adic ring and $B$ an admissible topological ring; let
$\phi : A \to B$ be a continuous homomorphism making $B$ an $A$-algebra. The following are equivalent:

> (a) $B$ is Noetherian and $\mathfrak{J}B$-adic, and $B/\mathfrak{J}B$ is a finite-type algebra over $A/\mathfrak{J}$.
> (b) $B$ is topologically $A$-isomorphic to $\varprojlim B_{n}$, where $B_{n} = B_{m} / \mathfrak{J}^{n+1} B_{m}$ for
> $m \geq n$, and `B_1` is a finite-type $A_{1} = A/\mathfrak{J}^{2}$-algebra. (c) $B$ is topologically $A$-isomorphic
> to a quotient of some $A{T_{1}, \cdots, T_{r}}$ by a (necessarily closed) ideal.

**Proof sketch.** (c) ⟹ (a): $A' = A{T_{1}, \cdots, T_{r}}$ is Noetherian (7.5.4); $\mathfrak{J} A'$ is an ideal of
definition of $A'$, and $B/\mathfrak{J}B$ is a quotient of $(A/\mathfrak{J})[T_{1}, \cdots, T_{r}]$. (a) ⟹ (b): by
(7.2.11), $B \cong \varprojlim B/\mathfrak{J}^{n+1} B$. (b) ⟹ (c): choose generators $(c_{i})$ of the
$A/\mathfrak{J}$-algebra $B/\mathfrak{J}B$ and apply (7.5.3) to get a continuous $A$-homomorphism $u : A' \to B$;
surjectivity is checked passing to associated graded modules.

### 7.6. Completed rings of fractions

<!-- label: 0.7.6 -->

**(7.6.1)** Let $A$ be linearly topologized, $(\mathfrak{J}_{\lambda})$ a fundamental system of open neighborhoods of
`0` consisting of ideals, and $S \subset A$ a multiplicative subset. With $A_{\lambda} = A/\mathfrak{J}_{\lambda}$, set
$S_{\lambda} = u_{\lambda}(S)$; the $u_{\lambda \mu}$ give surjective $S^{-1}_{\mu} A_{\mu} \to S^{-1}_{\lambda}
A_{\lambda}$, a projective system. Write

```
A{S⁻¹} = lim⃖ S_λ⁻¹ A_λ.
```

This is independent of $(\mathfrak{J}_{\lambda})$:

**Proposition (7.6.2).** $A{S^{-1}}$ is topologically isomorphic to the separated completion of $S^{-1}A$ for the
topology with fundamental system of neighborhoods of `0` the $S^{-1} \mathfrak{J}_{\lambda}$.

**Corollary (7.6.3).** If $S'$ is the canonical image of $S$ in `Â`, then $A{S^{-1}} \cong \hat{A}{S'^{-1}}$.

If $A$ is separated and complete, $S^{-1}A$ need not be: take $S = {f^{n}}$ with $f$ topologically nilpotent but not
nilpotent; then $S^{-1}A \neq 0$ but $S^{-1} \mathfrak{J}_{\lambda} = S^{-1}A$ for each $\lambda$.

**Corollary (7.6.4).** If $0 \notin S$ in $A$, then $A{S^{-1}} \neq 0$.

**(7.6.5)** Call $A{S^{-1}}$ the _completed ring of fractions_ of $A$ with denominators in $S$. There is a canonical
continuous $A \to A{S^{-1}}$.

**(7.6.6) Universal property.** For every continuous $u : A \to B$ to a separated, complete linearly topologized ring
$B$ with $u(S)$ consisting of invertible elements, $u$ factors uniquely as $A \to A{S^{-1}} \xrightarrow{u'} B$ with
$u'$ continuous.

**(7.6.7) Functoriality.** For $\phi : A \to B$ continuous with $\phi(S) \subset T$, there is a unique continuous
$\phi' : A{S^{-1}} \to B{T^{-1}}$ extending $\phi$. For $B = A$, $\phi = id$, and $S \subset T$, this gives
$\rho^{T,S} : A{S^{-1}} \to A{T^{-1}}$ with $\rho^{U,S} = \rho^{U,T} \circ \rho^{T,S}$ for $S \subset T \subset U$.

**(7.6.8)** For multiplicative subsets $S_{1}, S_{2} \subset A$ with $S_{2}'$ the image of `S_2` in $A{S^{-1}_{1}}$,

$$ A{(S_{1} S_{2})^{-1}} \cong A{S^{-1}_{1}}{S_{2}'^{-1}}. $$

**(7.6.9)** Let $\mathfrak{a} \subset A$ be an _open_ ideal. Then $S^{-1} \mathfrak{a}$ is open in $S^{-1}A$; its
separated completion $\mathfrak{a}{S^{-1}} = \varprojlim (S^{-1} \mathfrak{a} / S^{-1} \mathfrak{J}_{\lambda})$ is an
open ideal of $A{S^{-1}}$, and $A{S^{-1}} / \mathfrak{a}{S^{-1}} \cong S^{-1} A / S^{-1} \mathfrak{a} = S^{-1}
(A/\mathfrak{a})$. Conversely, every open ideal of $A{S^{-1}}$ is of the form $\mathfrak{a}{S^{-1}}$ for a unique open
$\mathfrak{a} \supset \mathfrak{J}_{\lambda} \subset A$.

**Proposition (7.6.10).** The map $\mathfrak{p} \mapsto \mathfrak{p}{S^{-1}}$ is an increasing bijection between open
prime ideals of $A$ not meeting $S$ and open prime ideals of $A{S^{-1}}$; the residue field of
$A{S^{-1}}/\mathfrak{p}{S^{-1}}$ is canonically the field of fractions of $A/\mathfrak{p}$.

**Proposition (7.6.11).**

> (i) If $A$ is admissible, so is $A' = A{S^{-1}}$, and $\mathfrak{J}' = \mathfrak{J}{S^{-1}}$ is an ideal of definition
> for $A'$ whenever $\mathfrak{J}$ is for $A$. (ii) If $A$ is $\mathfrak{J}$-adic with $\mathfrak{J}/\mathfrak{J}^{2}$
> finite-type over $A/\mathfrak{J}$, then $A'$ is $\mathfrak{J}'$-adic with $\mathfrak{J}'/\mathfrak{J}'^{2}$
> finite-type over $A'/\mathfrak{J}'$. If $A$ is Noetherian, so is $A'$.

**Corollary (7.6.12).** Under (7.6.11)(ii), $(\mathfrak{J}{S^{-1}})^{n} = \mathfrak{J}^{n}{S^{-1}}$.

**Proposition (7.6.13).** Let $A$ be an adic Noetherian ring and $S \subset A$ multiplicative. Then $A{S^{-1}}$ is a
flat $A$-module.

**Proof.** $A{S^{-1}}$ is the completion of the Noetherian $S^{-1}A$ for its $S^{-1}\mathfrak{J}$-preadic topology,
hence flat over $S^{-1}A$ (7.3.3); transitivity (6.2.1) plus flatness of $S^{-1}A$ over $A$ (6.3.1) finishes the proof.

**Corollary (7.6.14).** Under (7.6.13), if $S' \subset S$, then $A{S^{-1}}$ is flat over $A{S'^{-1}}$.

**(7.6.15)** For $f \in A$, write $A_{f} = A{S^{-1}_{f}}$ with $S_{f} = {f^{n} : n \geq 0}$, and $\mathfrak{a}_{f} =
\mathfrak{a}{S^{-1}_{f}}$ for an open ideal $\mathfrak{a}$. For $g \in A$, there is a canonical $A_{f} \to A_{fg}$
(7.6.7). For $S$ multiplicative, set $A_{S} = \varinjlim_{f \in S} A_{f}$; there is a canonical $A_{S} \to A{S^{-1}}$.

**Proposition (7.6.16).** If $A$ is Noetherian, $A{S^{-1}}$ is flat over $A_{S}$.

**Proof.** By (7.6.14), $A{S^{-1}}$ is flat over each $A_{f}$ ($f \in S$); conclude by (6.2.3).

**Proposition (7.6.17).** Let $\mathfrak{p}$ be an open prime ideal in an admissible ring $A$, and $S = A -
\mathfrak{p}$. Then $A{S^{-1}}$ and $A_{S}$ are local rings, the canonical $A_{S} \to A{S^{-1}}$ is local, and both
residue fields are canonically the field of fractions of $A/\mathfrak{p}$.

**Corollary (7.6.18).** If moreover $A$ is adic Noetherian, then $A{S^{-1}}$ and $A_{S}$ are Noetherian local rings, and
$A{S^{-1}}$ is a faithfully flat $A_{S}$-module.

### 7.7. Completed tensor products

<!-- label: 0.7.7 -->

**(7.7.1)** Let $A$ be linearly topologized and `M, N` two linearly topologized $A$-modules. Let $\mathfrak{J} \subset
A$, $V \subset M$, $W \subset N$ be open submodules with $\mathfrak{J} M \subset V$, $\mathfrak{J} N \subset W$. The
$(M/V) \otimes_{A/\mathfrak{J}} (N/W)$ form a projective system; their limit is an `Â`-module, the _completed tensor
product_, written $(M \otimes_{A} N)^{\wedge}$. In terms of completions, $(M \otimes_{A} N)^{\wedge} \cong \hat{M}
\hat{\otimes}_{\hat{A}} \hat{N}$.

**(7.7.2)** $(M \otimes_{A} N)^{\wedge}$ is the separated completion of $M \otimes_{A} N$ for the topology whose
fundamental system of neighborhoods of `0` consists of $Im(V \otimes_{A} N) + Im(M \otimes_{A} W)$ (`V, W` open in
`M, N`); this is the _tensor product topology_.

**(7.7.3)** For continuous $u : M \to M'$ and $v : N \to N'$, there is a continuous $u \hat{\otimes} v : (M \otimes_{A}
N)^{\wedge} \to (M' \otimes_{A} N')^{\wedge}$. Thus $(M \otimes_{A} N)^{\wedge}$ is bifunctorial in `M, N`.

**(7.7.4)** Similarly for any finite number of factors, with associativity and commutativity.

**(7.7.5)** For $A$-algebras `B, C` linearly topologized, $B \otimes_{A} C$ carries a tensor-product ring topology whose
fundamental system of neighborhoods of `0` consists of ideals $Im(\mathfrak{K} \otimes_{A} C) + Im(B \otimes_{A}
\mathfrak{L})$ ($\mathfrak{K}, \mathfrak{L}$ open ideals of `B, C`). $(B \otimes_{A} C)^{\wedge}$ is a topological
`Â`-algebra.

**(7.7.6) Universal property.** For every separated, complete $A$-algebra $D$ and every pair $(u, v)$ of continuous
$A$-homomorphisms $u : B \to D$, $v : C \to D$, there is a unique continuous $A$-homomorphism $w : (B \otimes_{A}
C)^{\wedge} \to D$ with $u = w \circ \rho$, $v = w \circ \sigma$ (where $\rho, \sigma$ are the canonical maps from
`B, C`).

**Proposition (7.7.7).** If `B, C` are preadmissible $A$-algebras, then $(B \otimes_{A} C)^{\wedge}$ is admissible; if
$\mathfrak{K}, \mathfrak{L}$ are ideals of definition of `B, C`, the closure in $(B \otimes_{A} C)^{\wedge}$ of the
canonical image of $Im(\mathfrak{K} \otimes_{A} C) + Im(B \otimes_{A} \mathfrak{L})$ is an ideal of definition.

**Proof.** Use $\mathfrak{h}^{2n} \subset Im(\mathfrak{K}^{n} \otimes_{A} C) + Im(B \otimes_{A} \mathfrak{L}^{n})$.

**Proposition (7.7.8).** Let $A$ be preadic with ideal of definition $\mathfrak{J}$, $M$ an $A$-module of finite type
with the $\mathfrak{J}$-preadic topology. For every adic Noetherian $A$-algebra $B$, $B \otimes_{A} M$ is identified
with $(B \otimes_{A} M)^{\wedge}$.

### 7.8. Topologies on modules of homomorphisms

<!-- label: 0.7.8 -->

**(7.8.1)** Let $A$ be a Noetherian $\mathfrak{J}$-adic ring, `M, N` two $A$-modules of finite type with
$\mathfrak{J}$-preadic topology. By (7.3.6), they are separated and complete; every $A$-homomorphism $M \to N$ is
continuous, and $\operatorname{Hom}_{A}(M, N)$ is $A$-finite-type. With $A_{i} = A/\mathfrak{J}^{i+1}$, $M_{i} =
M/\mathfrak{J}^{i+1} M$, $N_{i} = N/\mathfrak{J}^{i+1} N$, the $\operatorname{Hom}_{A_{i}}(M_{i}, N_{i})$ form a
projective system, and by (7.2.10) there is a canonical `φ : Hom_A(M, N) ⥲ lim⃖_i Hom_{A_i}(M_i, N_i)`.

**Proposition (7.8.2).** Under the hypotheses of (7.8.1), the submodules $\operatorname{Hom}_{A}(M, \mathfrak{J}^{i+1}
N)$ form a fundamental system of neighborhoods of `0` in $\operatorname{Hom}_{A}(M, N)$ for the $\mathfrak{J}$-adic
topology, and $\phi$ is a topological isomorphism.

**Proof.** Reduce to $M = L = A^{m}$; then $\operatorname{Hom}_{A}(L, N) = N^{m}$ and $\operatorname{Hom}_{A}(L,
\mathfrak{J}^{i+1} N) = \mathfrak{J}^{i+1} N^{m}$.

**Proposition (7.8.3).** Under the hypotheses of (7.8.2), the set of injective (resp. surjective, bijective)
homomorphisms $M \to N$ is open in $\operatorname{Hom}_{A}(M, N)$.

**Proof.** For surjectivity: by (7.3.5) and (7.1.14), $u$ is surjective iff $u_{0} : M/\mathfrak{J}M \to
N/\mathfrak{J}N$ is, so the set is the preimage of a discrete subset under the continuous $\operatorname{Hom}_{A}(M, N)
\to \operatorname{Hom}_{A_{0}}(M_{0}, N_{0})$. For injectivity: let $v : M \to N$ be injective and set $M' = v(M)$. By
Artin–Rees (7.3.2.1), there is $k \geq 0$ with $M' \cap \mathfrak{J}^{m+k} N \subset \mathfrak{J}^{m} M'$ for $m > 0$.
For $w \in \mathfrak{J}^{k+1} \operatorname{Hom}_{A}(M, N)$, $u = v + w$ is injective: if $u(x) = 0$ and $x \in
\mathfrak{J}^{i} M$, then $w(x) \in \mathfrak{J}^{i+k+1} N$, so $v(x) = -w(x) \in M' \cap \mathfrak{J}^{i+k+1} N \subset
\mathfrak{J}^{i+1} M'$, hence $x \in \mathfrak{J}^{i+1} M$. By induction, $x \in \bigcap \mathfrak{J}^{i} M = 0$.

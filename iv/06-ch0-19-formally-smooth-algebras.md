<!-- original page 165 -->

## §19. Formally smooth algebras and Cohen rings

### 19.0. Introduction

**(19.0.1)** In Chapter IV we shall introduce and study, among other things, an important class of morphisms of
preschemes, the *smooth* morphisms.[^1] One of their fundamental properties (which, together with a finiteness
condition, characterizes them) is a property of *lifting morphisms*: if $f : X \to Y$ is a smooth morphism, $g : Y' \to
Y$ a morphism, then for every morphism $h : Y'' \to Y'$ making `Y''` a prescheme "little different" from $Y'$, every
$Y$-morphism $Y'' \to X$ *factors as* $Y'' \xrightarrow{h} Y' \to X$. More precisely, restricting ourselves to the case
where $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$ are affine, $B$ is then called a *formally smooth
$A$-algebra* if, for every $A$-algebra $C$ and every *nilpotent* ideal $\mathfrak{J}$ of $C$, every $A$-homomorphism $B
\to C/\mathfrak{J}$ lifts to $B \to C \to C/\mathfrak{J}$. In other words, the map

```text
                              Hom_A(B, C) → Hom_A(B, C/𝔍)
```

is surjective. In many applications $X$ will appear as an object representing a representable contravariant functor $Y'
\mapsto F(Y')$ from the category of $Y$-preschemes into that of sets, so that one has $(0_{III}, 8.1.8)$ $F(Y') \cong
\operatorname{Hom}_{Y}(Y', X)$. In the affine case, if one sets $F^{\circ}(C) = F(\operatorname{Spec}(C))$, the
verification that, under the conditions above, $F^{\circ}(C) \to F^{\circ}(C/\mathfrak{J})$ is surjective (which can be
done even *without knowing* that $F$ is representable) will establish that $f$ is smooth, provided the additional
finiteness condition is satisfied.

**(19.0.2)** For *topological algebras* over a topological ring $A$, there is an analogous notion of *formally smooth*
algebra which we shall not make precise here (cf. `(19.3.1)`). The study of these notions is first carried out from an
elementary point of view in §19, then, by means of the properties of differentials which will be developed in §§20 and
21, more delicate theorems will be proved in §22. We summarize here the principal results on formally smooth algebras:

I. — Let $A$, $B$ be two Noetherian local rings, $\phi : A \to B$ a local homomorphism, $k$ the residue field of $A$,
and let $B_{0} = B \otimes_{A} k$; equip $A$, $B$ with their preadic topologies and $k$ with the discrete topology.
Then, for $B$ to be a formally smooth $A$-algebra, it is necessary and sufficient that $B$ be a *flat* $A$-module and
that `B_0` be a formally smooth $k$-algebra `(19.7.1)`. This theorem thus reduces formal smoothness, for Noetherian
local rings, to the same question for Noetherian local rings which are algebras over a *field*.

II. — Let $k$ be a field, $A$ a Noetherian local ring which is a $k$-algebra. For $A$ to be formally smooth, it is
necessary and sufficient that $A$ be *geometrically regular* over $k$, that is, that for every *finite* extension $k'$
of $k$, the semi-local ring $A \otimes_{k} k'$ be

<!-- original page 166 -->

regular `(22.5.8)`; the completion `Â` of $A$ is then a ring isomorphic to a formal power series ring $K[[T_{1}, \cdots,
T_{n}]]$ `(19.6.5)`. Moreover, the structure of $k$-algebra of `Â`, when $A$ is assumed to be *complete* and formally
smooth over $k$, is entirely determined by the residue field $K$ of $A$ and by the dimension of $A$; the latter can
moreover be arbitrary provided it satisfies the inequality $\dim(A) \geqslant rg_{K}(\Upsilon_{K/k})$, where
$\Upsilon_{K/k}$ is the "imperfection module" of $K$ `(22.2.6)`.

In particular, for an extension $K$ of $k$ to be formally smooth, it is necessary and sufficient that $K$ be a
*separable* extension of $k$ `(19.6.1)`.

III. — Let $A$ be a Noetherian local ring, $\mathfrak{J}$ an ideal of $A$ distinct from $A$, $A_{0} = A/\mathfrak{J}$,
`B_0` a *complete* Noetherian local ring, $A_{0} \to B_{0}$ a local homomorphism making `B_0` a formally smooth
`A_0`-algebra. Then there exists a complete Noetherian local ring $B$, a local homomorphism $A \to B$ making $B$ a flat
$A$-module, and an `A_0`-isomorphism $B \otimes_{A} A_{0} \cong B_{0}$ (so that, by I, $B$ is a *formally smooth*
$A$-algebra); furthermore $B$ is determined by these properties up to isomorphism `(19.7.2)`. This theorem contains in
particular the *theorems of Cohen* on the structure of complete Noetherian local rings `(19.8)`, which will play an
important role in §§6 and 7 of Chapter IV.

IV. — The interest of the study of formally smooth Noetherian local rings over another arises from the following
"pointwise" characterization of smooth morphisms: if $X$ and $Y$ are locally Noetherian preschemes, $f : X \to Y$ a
morphism locally of finite type, then, for $f$ to be smooth, it is necessary and sufficient that for every $x \in X$,
the ring $\mathcal{O}_{x}$ be formally smooth over $\mathcal{O}_{f(x)}$. In particular, if $Y = \operatorname{Spec}(k)$,
where $k$ is a *perfect* field, to say that $f$ is smooth is equivalent to saying that $X$ is a *regular* prescheme.

V. — Finally, we shall see in §§20, 21, and 22 that the notion of formally smooth algebra arises naturally in the theory
of *Kähler differentials*, the two theories illuminating each other.

**(19.0.3)** In all this section and the following ones, the topological rings and modules will be assumed to be
*linearly topologized* $(0_{I}, 7.1.1)$; the topological rings considered will be assumed *commutative*, except when
explicitly stated otherwise. Recall that if $A$ and $B$ are two topological rings, $\rho : A \to B$ a ring homomorphism
defining on $B$ a structure of $A$-algebra, one says that $B$ is a *topological $A$-algebra* if $\rho$ is continuous for
the topologies in question.

To abbreviate, in a topological ring $A$ (resp. a topological $A$-module $M$), we shall say "fundamental system of
*open* ideals (resp. submodules)" instead of "fundamental system of neighbourhoods of `0` formed of ideals (resp.
submodules)".

Given a topological ring $A$ and an $A$-module $M$, the sets $\mathfrak{J}M$, where $\mathfrak{J}$ runs through a
fundamental system of open ideals, form a fundamental system of open submodules for a topology on $M$ making $M$ a
topological $A$-module, which is said to be *deduced from the topology of $A$*.

Let $M$ be a topological $A$-module whose topology is *coarser* than the topology deduced from that of $A$; then, if $N$
is an open submodule of $M$, the discrete $A$-module $M/N$ is annulled by an open ideal of $A$, for by hypothesis there
exists such an ideal $\mathfrak{K}$ with $\mathfrak{K} \cdot M \subset N$.

<!-- original page 167 -->

If $M$ and $N$ are two topological $A$-modules whose topologies are both deduced from that of $A$, then *every*
$A$-homomorphism $u : M \to N$ is *continuous*, for, for every neighbourhood $V$ of `0` in $N$, there exists by
hypothesis an open ideal $\mathfrak{J}$ of $A$ such that $\mathfrak{J}N \subset V$, and one therefore has
$u(\mathfrak{J}M) \subset \mathfrak{J}N \subset V$.

When $B$ is a topological $A$-algebra, the topology on $B$ *deduced* from that of $A$ is *finer* than the given
topology, for, for every open ideal $\mathfrak{K}$ of $B$, there is by hypothesis an open ideal $\mathfrak{J}$ of $A$
such that $\mathfrak{J}B \subset \mathfrak{K}$.

### 19.1. Formal epimorphisms and monomorphisms

**Proposition (19.1.1).**

<!-- label: 0_IV.19.1.1 -->

*Let $A$ be a topological ring, $M$, $N$ two topological $A$-modules, $(W_{\lambda})$ a fundamental system of open
submodules of $N$, $u : M \to N$ a continuous $A$-homomorphism, $\hat{M}$, $\hat{N}$ the separated completions of $M$
and $N$, $\hat{u} : \hat{M} \to \hat{N}$ the continuous extension of $u$ to the separated completions.*

*(i) The following conditions are equivalent:*

*a) $u(M)$ is dense in $N$.*

*a') $\hat{u}(\hat{M})$ is dense in $\hat{N}$.*

*a") For every $\lambda$, the composite homomorphism $M \xrightarrow{u} N \to N/W_{\lambda}$ is surjective.*

*(ii) The following conditions are equivalent:*

*b) The inverse image by $u$ of the topology of $N$ is equal to the topology of $M$.*

*b') `û` is an isomorphism of the topological `Â`-module $\hat{M}$ onto the topological sub-`Â`-module
$\hat{u}(\hat{M})$ of $\hat{N}$ (which is necessarily closed).*

*b") The $u^{-1}(W_{\lambda})$ form a fundamental system of neighbourhoods of `0` in $M$.*

This follows immediately from the definition of the separated completions and from the fact that $N/W_{\lambda}$ is
discrete.

**(19.1.2)** When the equivalent conditions of (i) (resp. (ii)) in `(19.1.1)` are satisfied, one says that $u$ is a
*formal epimorphism* (resp. a *formal monomorphism*). One says that $u$ is a *formal bimorphism* if it is at once a
formal monomorphism and a formal epimorphism; this amounts, by virtue of `(19.1.1)`, to saying that `û` is an
isomorphism of the topological `Â`-module $\hat{M}$ onto the topological `Â`-module $\hat{N}$.

**Proposition (19.1.3).**

<!-- label: 0_IV.19.1.3 -->

*Let $A$ be a topological ring, $M$, $N$ two topological $A$-modules, $u : M \to N$ a continuous $A$-homomorphism.
Assume that there exist two fundamental systems of open submodules $(V_{\lambda})$, $(W_{\lambda})$ in $M$ and $N$
respectively, having the same set of indices and such that $u(V_{\lambda}) \subset W_{\lambda}$ for every $\lambda$; let
$u_{\lambda} : M/V_{\lambda} \to N/W_{\lambda}$ be the homomorphism deduced from $u$ by passage to the quotients. Then:*

*(i) For $u$ to be a formal epimorphism, it is necessary and sufficient that, for every $\lambda$, $u_{\lambda}$ be
surjective.*

*(ii) For $u$ to be a formal monomorphism, it is necessary and sufficient that, for every $\lambda$, there exist a $\mu$
such that $V_{\mu} \subset V_{\lambda}$ and that $Ker(u_{\mu})$ be contained in the kernel $V_{\lambda}/V_{\mu}$ of the
canonical map $M/V_{\mu} \to M/V_{\lambda}$.*

*(iii) For $u$ to be a formal bimorphism, it is necessary and sufficient that, for every $\lambda$, $u_{\lambda}$ be
surjective and that there exist a $\mu$ such that $V_{\mu} \subset V_{\lambda}$ and that the canonical homomorphism
$M/V_{\mu} \to M/V_{\lambda}$*

<!-- original page 168 -->

*factor as $M/V_{\mu} \xrightarrow{u_{\mu}} N/W_{\mu} \to M/V_{\lambda}$ (where the homomorphism $N/W_{\mu} \to
M/V_{\lambda}$ is necessarily unique).*

Assertion (i) is immediate; on the other hand, $Ker(u_{\mu}) = u^{-1}(W_{\mu})/V_{\mu}$, and the kernel of the canonical
map $M/V_{\mu} \to M/V_{\lambda}$ is $V_{\lambda}/V_{\mu}$; the condition in (ii) thus amounts to saying that
$u^{-1}(W_{\mu}) \subset V_{\lambda}$, and assertion (ii) follows at once; finally, when $u_{\mu}$ is surjective, it
amounts to the same to say that $Ker(u_{\mu})$ is contained in $V_{\lambda}/V_{\mu}$, or to say that $M/V_{\mu} \to
M/V_{\lambda}$ factors as $v \circ u_{\mu}$, where $v$ is a homomorphism $N/W_{\mu} \to M/V_{\lambda}$, since
$N/W_{\mu}$ is then identified with $(M/V_{\mu})/Ker(u_{\mu})$.

**Corollary (19.1.4).**

<!-- label: 0_IV.19.1.4 -->

*Let $A$ be a topological ring, $M$, $N$ two topological $A$-modules whose topologies are deduced from that of $A$, $u :
M \to N$ a formal epimorphism. Let $(\mathfrak{J}_{\lambda})$ be a fundamental system of open ideals of $A$. For $u$ to
be a formal bimorphism, it is necessary and sufficient that for every $\lambda$, the homomorphism $u_{\lambda} :
M/\mathfrak{J}_{\lambda} M \to N/\mathfrak{J}_{\lambda} N$ deduced from $u$ by passage to the quotients be bijective.*

Indeed, one has $u(\mathfrak{J}_{\lambda} M) \subset \mathfrak{J}_{\lambda} N$ and one may apply the criterion
`(19.1.3, (iii))`; but if one has a factorization $M/\mathfrak{J}_{\lambda} M \xrightarrow{u_{\mu}} N/\mathfrak{J}_{\mu}
N \xrightarrow{v} M/\mathfrak{J}_{\lambda} M$, the image of $\mathfrak{J}_{\lambda} M/\mathfrak{J}_{\mu} M$ under
$u_{\mu}$ is $\mathfrak{J}_{\lambda} N/\mathfrak{J}_{\mu} N$, hence the image of $\mathfrak{J}_{\lambda}
N/\mathfrak{J}_{\mu} N$ under $v$ is `0` and $v$ factors as

```text
                            N/𝔍_μ N → N/𝔍_λ N ─v'→ M/𝔍_λ M;
```

but then the identity automorphism of $M/\mathfrak{J}_{\lambda} M$ factors as

```text
                            M/𝔍_λ M ─u_λ→ N/𝔍_λ N ─v'→ M/𝔍_λ M,
```

which shows that $u_{\lambda}$ is injective, and since one already knows it is surjective, this proves the corollary.

**Proposition (19.1.5).**

<!-- label: 0_IV.19.1.5 -->

*Let $A$ be a topological ring, $M$, $N$ two topological $A$-modules, $u : M \to N$ a continuous $A$-homomorphism. The
following conditions are equivalent:*

*a) For every discrete topological $A$-module $E$ and every continuous $A$-homomorphism $v : M \to E$, there exists a
continuous $A$-homomorphism $w : N \to E$ such that $v = w \circ u$.*

*b) For every open submodule $V$ of $M$, there exist an open submodule `W''` of $N$, an open submodule $V'' \subset V
\cap u^{-1}(W'')$ and a homomorphism $h : N/W'' \to M/V$ such that the canonical homomorphism $M/V'' \to M/V$ factors
as*

```text
                              M/V'' ─u''→ N/W'' ─h→ M/V
```

*where `u''` is deduced from $u$ by passage to the quotients.*

To see that a) implies b), it suffices to apply a) to $E = M/V$ and to the canonical homomorphism $v : M \to M/V$; then
$W'' = w^{-1}(0)$ is an open submodule of $N$ and $V'' = u^{-1}(W'')$ an open submodule of $M$ contained in $V$; these
submodules and the homomorphism $h : N/W'' \to M/V$ deduced from $w$ by passage to the quotient answer the question.
Conversely, to show that b) implies a), one may restrict to the case where $v$ is surjective, by replacing $E$ by
$v(M)$; then $V' = Ker(v)$ is an open submodule of $M$, hence $E$ is isomorphic to the discrete $A$-module $M/V'$, and
by applying b) one obtains

<!-- original page 169 -->

the desired continuous $A$-homomorphism $w$ as the composite $N \to N/W'' \xrightarrow{h} M/V'$, the diagram

```text
                              M ─────u───→ N
                              │            │
                              ↓            ↓
                            M/V'' ──────→ N/W''
                                    u''
```

being commutative.

When the equivalent conditions of `(19.1.5)` are satisfied, we shall say that $u$ is *formally left-invertible*; since
condition b) of `(19.1.5)` implies that $u^{-1}(W'') \subset V$, $u$ is then a formal monomorphism. The terminology is
further justified by the following corollaries:

**Corollary (19.1.6).**

<!-- label: 0_IV.19.1.6 -->

*If there exists a continuous `Â`-homomorphism $s : \hat{N} \to \hat{M}$ such that $s \circ \hat{u} = 1_{\hat{M}}$, then
$u$ is formally left-invertible.*

One observes that `û` is then a topological isomorphism of $\hat{M}$ onto a *topological direct factor* of $\hat{N}$. To
prove `(19.1.6)`, it suffices to note that with the notations of `(19.1.5, a))`, $v : M \to E$ extends to a continuous
`Â`-homomorphism $\hat{v} : \hat{M} \to E$ since $E$ is discrete; let $j : M \to \hat{M}$ and $j' : N \to \hat{N}$ be
the canonical homomorphisms; then, setting $w = \hat{v} \circ s \circ j'$, one has $w \circ u = \hat{v} \circ s \circ
\hat{u} \circ j = \hat{v} \circ j = v$.

**Corollary (19.1.7).**

<!-- label: 0_IV.19.1.7 -->

*Suppose that the topologies of $M$ and $N$ are deduced from that of $A$, and let $(\mathfrak{J}_{\lambda})$ be a
fundamental system of open ideals of $A$. For $u$ to be formally left-invertible, it is necessary and sufficient that,
for every $\lambda$, the homomorphism $u_{\lambda} : M/\mathfrak{J}_{\lambda} M \to N/\mathfrak{J}_{\lambda} N$, deduced
from $u$ by passage to the quotients, be left-invertible (in other words, be an isomorphism of $M/\mathfrak{J}_{\lambda}
M$ onto a direct factor of $N/\mathfrak{J}_{\lambda} N$).*

Indeed, the condition is sufficient, for, taking $V' = \mathfrak{J}_{\lambda} M$ in condition b) of `(19.1.5)`, one
answers the question by taking $W'' = \mathfrak{J}_{\lambda} N$, $V'' = V'$ and $h$ such that $h \circ u_{\lambda}$ is
the identity on $M/\mathfrak{J}_{\lambda} M$. Conversely, if $u$ is formally left-invertible, then, for every $\lambda$,
there is, by virtue of `(19.1.5, b))`, a $\mu$ such that $\mathfrak{J}_{\mu} \subset \mathfrak{J}_{\lambda}$ and a
homomorphism $h : N/\mathfrak{J}_{\mu} N \to M/\mathfrak{J}_{\lambda} M$ such that the canonical homomorphism
$M/\mathfrak{J}_{\mu} M \to M/\mathfrak{J}_{\lambda} M$ factors as $M/\mathfrak{J}_{\mu} M \xrightarrow{u_{\mu}}
N/\mathfrak{J}_{\mu} N \xrightarrow{h} M/\mathfrak{J}_{\lambda} M$; but since
$h(\mathfrak{J}_{\lambda}(N/\mathfrak{J}_{\mu} N)) = \mathfrak{J}_{\lambda} \cdot h(N/\mathfrak{J}_{\mu} N) \subset
\mathfrak{J}_{\lambda}(M/\mathfrak{J}_{\lambda} M) = 0$, $h$ factors canonically as $N/\mathfrak{J}_{\mu} N \to
N/\mathfrak{J}_{\lambda} N \xrightarrow{s} M/\mathfrak{J}_{\lambda} M$, and it is immediate that $s$ is a left inverse
of $u_{\lambda}$.

**Proposition (19.1.8).**

<!-- label: 0_IV.19.1.8 -->

*Let $A$ be a topological ring admitting a countable decreasing fundamental system $(\mathfrak{J}_{n})$ of open ideals.
Let $M$, $N$ be two topological $A$-modules whose topologies are deduced from that of $A$, $u : M \to N$ an
$A$-homomorphism. Set $M_{n} = M/\mathfrak{J}_{n} M$, $N_{n} = N/\mathfrak{J}_{n} N$ and let $u_{n} : M_{n} \to N_{n}$
be the $(A/\mathfrak{J}_{n})$-homomorphism deduced from $u$ by passage to the quotients. Suppose that, for every $n$,
$P_{n} = Coker(u_{n})$ is a projective $(A/\mathfrak{J}_{n})$-module and that $M$ is separated and complete. Then, for
$u$ to be formally left-invertible, it is necessary and sufficient that $u$ be left-invertible (and $u$ is then a
topological isomorphism of $M$ onto a topological direct factor of $N$).*

<!-- original page 170 -->

By virtue of `(19.1.7)`, one has the commutative diagrams

```text
                    u_n         p_n
       0 ───→ M_n ─────→ N_n ────────→ P_n ──→ 0
              │↑          │↑           │↑
              │f          │g           │h
              ↓│          ↓│           ↓│
       0 ──→ M_{n+1} ──→ N_{n+1} ──→ P_{n+1} ──→ 0
                  u_{n+1}      p_{n+1}
```

where the rows are *split* exact sequences; in other words, there exists for each $n$ a homomorphism $s_{n} : P_{n} \to
N_{n}$ such that $p_{n} \circ s_{n} = 1_{P_{n}}$. We shall show that one can, by induction on $n$, define a homomorphism
$s'_{n} : P_{n} \to N_{n}$ such that $p_{n} \circ s'_{n} = 1_{P_{n}}$ and that the diagrams

```text
                              s'_n
                       P_n ──────→ N_n
                       │↑          │↑
                       │h          │g
                       ↓│          ↓│
                       P_{n+1} ──→ N_{n+1}
                              s'_{n+1}
```

be commutative. Indeed, $g \circ s'_{n+1} - s'_{n} \circ h$ is a homomorphism of $P_{n+1}$ into $u_{n+1}(M_{n+1}) =
u_{n+1}(M_{n+1})/\mathfrak{J}_{n} u_{n+1}(M_{n+1})$; since $P_{n+1}$ is a *projective* $(A/\mathfrak{J}_{n+1})$-module,
this homomorphism factors as

```text
                P_{n+1} ─t_{n+1}→ u_{n+1}(M_{n+1}) → u_{n+1}(M_{n+1})/𝔍_n u_{n+1}(M_{n+1})
```

whence one concludes at once that $s'_{n+1} = s_{n+1} - t_{n+1}$ answers the question. This being so, from the
decomposition of $N_{n}$ as the direct sum of $u_{n}(M_{n})$ and of $s'_{n}(P_{n})$, one deduces at once a homomorphism
$w_{n} : N_{n} \to M_{n}$ left inverse of $u_{n}$ and such that the diagrams

```text
                              w_n
                       N_n ──────→ M_n
                       │↑          │↑
                       │g          │f
                       ↓│          ↓│
                       N_{n+1} ──→ M_{n+1}
                              w_{n+1}
```

be commutative. The projective system $(w_{n})$ then admits a projective limit $\hat{w} : \hat{N} \to \hat{M} = M$,
whence by composition with the canonical homomorphism $N \to \hat{N}$, a homomorphism $w : N \to M$ such that, for every
$n$, the endomorphism $(w \circ u)_{n}$ of $M_{n} = M/\mathfrak{J}_{n} M$ deduced from $w \circ u$ by passage to the
quotients is the identity; this entails that $w \circ u = 1_{M}$ since $M$ is separated and complete.

**Proposition (19.1.9).**

<!-- label: 0_IV.19.1.9 -->

*Let $A$ be a preadmissible topological ring $(0_{I}, 7.1.2)$, $\mathfrak{L}$ an ideal of definition of $A$,
$(\mathfrak{J}_{\lambda})$ a fundamental system of open ideals of $A$. Let $M$, $N$ be two topological $A$-modules whose
topologies are deduced from that of $A$, and such that for every $\lambda$, $N/\mathfrak{J}_{\lambda} N$ is a projective
$(A/\mathfrak{J}_{\lambda})$-module (cf. `(19.2.3)`). Let $u : M \to N$ be an $A$-homomorphism. Then the following
conditions are equivalent:*

<!-- original page 171 -->

*a) $u$ is formally left-invertible.*

*b) The homomorphism $u_{0} : M/\mathfrak{L}M \to N/\mathfrak{L}N$ deduced from $u$ by passage to the quotients is
left-invertible.*

We have seen `(19.1.7)` that condition a) is equivalent to saying that $u_{\lambda}$ is left-invertible for every
$\lambda$; since $\mathfrak{L}$ is an open ideal, hence contains a $\mathfrak{J}_{\lambda}$, one deduces at once that
$u_{0}$ is left-invertible. To show conversely that b) implies a), note that for every $\lambda$,
$\mathfrak{L}/\mathfrak{J}_{\lambda}$ is by hypothesis a nilpotent ideal of $A/\mathfrak{J}_{\lambda}$. Our assertion
will follow from the next proposition:

**Proposition (19.1.10).**

<!-- label: 0_IV.19.1.10 -->

*Let $A$ be a ring, $M$, $N$ two $A$-modules, with $N$ projective, $u : M \to N$ an $A$-homomorphism. Let $\mathfrak{J}$
be an ideal of $A$; suppose that one of the following conditions is satisfied:*

*(i) $\mathfrak{J}$ is nilpotent.*

*(ii) $\mathfrak{J}$ is contained in the radical of $A$ and $M$ is of finite type.*

*Then, for $u$ to be left-invertible, it is necessary and sufficient that the homomorphism $u_{0} : M/\mathfrak{J}M \to
N/\mathfrak{J}N$ of $(A/\mathfrak{J})$-modules, deduced from $u$ by passage to the quotients, be left-invertible.*

The condition being obviously necessary, let us prove that it is sufficient. Let $v_{0}$ be a left inverse of $u_{0}$;
the composite homomorphism $N \to N/\mathfrak{J}N \xrightarrow{v_{0}} M/\mathfrak{J}M$ factors as $N \xrightarrow{v} M
\to M/\mathfrak{J}M$ since $N$ is projective; then $w = v \circ u$ is an endomorphism of $M$ such that the endomorphism
$w_{0}$ of $M/\mathfrak{J}M$ deduced by passage to the quotients is the *identity*, and it suffices to prove that $w$ is
itself bijective (for then $w^{-1} v$ will be a left inverse of $u$). Let us now distinguish the two cases.

(i) For every $n$ one has the commutative diagram

```text
            (𝔍ⁿ/𝔍ⁿ⁺¹) ⊗_{A/𝔍} (M/𝔍M)  ──→  𝔍ⁿM/𝔍ⁿ⁺¹M
                   │                            │
                   │1 ⊗ gr⁰(w)                  │gr^n(w)
                   ↓                            ↓
            (𝔍ⁿ/𝔍ⁿ⁺¹) ⊗_{A/𝔍} (M/𝔍M)  ──→  𝔍ⁿM/𝔍ⁿ⁺¹M
```

where the horizontal arrows are *surjective*, and since $gr^{0}(w) = w_{0}$ is the *identity*, so is $gr^{n}(w)$, which
a fortiori is bijective. The $\mathfrak{J}$-preadic filtration on $M$ being finite since $\mathfrak{J}$ is nilpotent,
one concludes that $w$ is bijective (Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1).

(ii) It suffices to show that for every maximal ideal $\mathfrak{m}$ of $A$, the endomorphism $w_{\mathfrak{m}}$ of
$M_{\mathfrak{m}}$ is bijective (Bourbaki, Alg. comm., chap. II, §3, n° 3, th. 1) and since $\mathfrak{J}
A_{\mathfrak{m}} \subset \mathfrak{m} A_{\mathfrak{m}}$ and $A_{\mathfrak{m}}/\mathfrak{J} A_{\mathfrak{m}} =
(A/\mathfrak{J})_{\mathfrak{m}}$, one is reduced to proving the proposition when $A$ is a *local* ring. Moreover, one
may suppose that $\mathfrak{J}$ is the maximal ideal of $A$, for if $u_{0}$ is left-invertible,

<!-- original page 172 -->

then so is $u_{00} : M/\mathfrak{J}_{0} M \to N/\mathfrak{J}_{0} M$ obtained by tensoring $u_{0}$ with
$1_{A/\mathfrak{J}_{0}}$, since one has $M/\mathfrak{J}_{0} M = (M/\mathfrak{J}M) \otimes_{A/\mathfrak{J}}
(A/\mathfrak{J}_{0})$. Suppose then that $\mathfrak{J}$ is maximal, so that $A/\mathfrak{J}$ is a field. It clearly
suffices to show that $M$ is a *free* $A$-module under the conditions of the statement: indeed, $det(w_{0})$ is then the
canonical image of $det(w)$ in $A/\mathfrak{J}$, hence $det(w)$ does not belong to the ideal $\mathfrak{J}$ and is
consequently invertible. Now, the $(A/\mathfrak{J})$-vector space $M/\mathfrak{J}M$ being free of finite type, there is
an $A$-module $L$ of finite type and an $A$-homomorphism $f : L \to M$ such that the homomorphism $f_{0} :
L/\mathfrak{J}L \to M/\mathfrak{J}M$ deduced from $f$ by passage to the quotients is bijective. Since $M$ is of finite
type, one concludes first of all that $f$ is *surjective* by Nakayama's lemma (Bourbaki, Alg. comm., chap. II, §3, n° 2,
cor. 1 of prop. 4); furthermore, if $g = u \circ f$, the homomorphism $g_{0} : L/\mathfrak{J}L \to N/\mathfrak{J}N$
deduced by passage to the quotients is left-invertible, and since here $L$ is free, the remark at the beginning proves
that $g$ is itself left-invertible; but this clearly entails that $f$ is *injective*, which completes the proof.

Let us mention in passing the following corollaries of `(19.1.10)`:

**Corollary (19.1.11).**

<!-- label: 0_IV.19.1.11 -->

*Let $A$ be a local ring, $k$ its residue field, $M$ an $A$-module of finite type, $N$ a projective $A$-module, $u : M
\to N$ a homomorphism. For $u$ to be left-invertible, it is necessary and sufficient that there exist a system of
generators $(x_{i})_{1 \leqslant i \leqslant m}$ of $M$ such that the images under $u \otimes 1 : M \otimes_{A} k \to N
\otimes_{A} k$ of the $x_{i} \otimes 1$ be linearly independent in $N \otimes_{A} k$; the $x_{i}$ then form a basis of
$M$.*

The condition is obviously necessary, for if $u$ is left-invertible, $M$ is a projective $A$-module of finite type,
hence free. Conversely, if the condition is satisfied, it is clear that the $x_{i} \otimes 1$ form a basis of $M
\otimes_{A} k$ and that $u \otimes 1$ is left-invertible; it then suffices to apply `(19.1.10)` to the maximal ideal
$\mathfrak{J}$ of $A$.

**Corollary (19.1.12).**

<!-- label: 0_IV.19.1.12 -->

*Let $A$ be a ring, $M$ an $A$-module of finite type, $N$ a projective $A$-module, $u : M \to N$ a homomorphism. For
every prime ideal $\mathfrak{p} \in \operatorname{Spec}(A)$, the following conditions are equivalent:*

*a) The homomorphism $u_{\mathfrak{p}} : M_{\mathfrak{p}} \to N_{\mathfrak{p}}$ is left-invertible.*

*b) The homomorphism $u \otimes 1 : M \otimes_{A} k(\mathfrak{p}) \to N \otimes_{A} k(\mathfrak{p})$ is injective
(recall that $k(\mathfrak{p})$ denotes the residue field of $A$ at $\mathfrak{p}$).*

*c) There exists a finite system of elements $x_{i} \in M$ ($1 \leqslant i \leqslant m$) such that the images of the
$x_{i}$ in $M_{\mathfrak{p}}$ generate $M_{\mathfrak{p}}$, and a system of $m$ linear forms $y^{*}_{i}$ on $N$ ($1
\leqslant i \leqslant m$) such that $det(\langle y^{*}_{i}, u(x_{j})\rangle) \notin \mathfrak{p}$.*

*d) There exists $f \in A - \mathfrak{p}$ such that the homomorphism $u_{f} : M_{f} \to N_{f}$ is left-invertible.*

*Moreover, the set of $\mathfrak{p} \in \operatorname{Spec}(A)$ satisfying these conditions is open in
$\operatorname{Spec}(A)$.*

The last condition is a trivial consequence of d). Since $N$ is projective, it is a direct factor of a free $A$-module
$A^{(I)}$; furthermore, since $M$ is of finite type, $u(M)$ is contained in a sub-module of $A^{(I)}$ of the form
$A^{n}$ for $n$ finite; since each of the statements a), b), c), d) is equivalent to the corresponding statement where
one replaces $N$ by $N \oplus P$ (with $u$ still considered as mapping $M$ into $N$), one is reduced to the case where
$N$ is free of finite type. It is trivial that d) implies a), and a) and b) are equivalent by virtue of `(19.1.11)`;
moreover a) entails that $M_{\mathfrak{p}}$ is free `(19.1.11)`, hence a) entails c), by taking for the $x_{i}$ a family
whose images in $M_{\mathfrak{p}}$ form a basis of this

<!-- original page 173 -->

$A_{\mathfrak{p}}$-module and noting that (since $N$ is free of finite type) every linear form on the
$A_{\mathfrak{p}}$-module $N_{\mathfrak{p}}$ is written $u^{*} = v^{*}/f$, where $f \in A - \mathfrak{p}$, and $v^{*}$
is a linear form on the $A$-module $N$. It is clear that c) implies b), and it remains to see that a) implies d). Now,
since $N$ is of finite presentation, $(\operatorname{Hom}_{A}(N, M))_{\mathfrak{p}}$ is canonically identified with
$\operatorname{Hom}_{A_{\mathfrak{p}}}(N_{\mathfrak{p}}, M_{\mathfrak{p}})$ (Bourbaki, Alg. comm., chap. II, §2, n° 7,
prop. 19). If $w_{\mathfrak{p}}$ is a left inverse of $u_{\mathfrak{p}}$, there exists thus a homomorphism $w : N \to M$
and an element $f \in A - \mathfrak{p}$ such that $w_{\mathfrak{p}} = w \otimes (1/f) 1_{A_{\mathfrak{p}}}$. The
relation $w_{\mathfrak{p}} \circ u_{\mathfrak{p}} = 1_{M_{\mathfrak{p}}}$ thus also reads $(w \circ u) \otimes
1_{A_{\mathfrak{p}}} = f \cdot 1_{M_{\mathfrak{p}}}$. But since $M$ is an $A$-module of finite type, there exists $g \in
A - \mathfrak{p}$ such that the endomorphism $g((w \circ u) - f \cdot 1_{M})$ vanishes on all the generators of $M$,
hence is zero. Setting $h = fg$, and $u_{h} = u \otimes 1_{A_{h}}$, $w_{h} = w \otimes 1_{A_{h}}$, one therefore has
$w_{h}(u_{h}(z)) = (f/1) z$ for every $z \in M_{h}$; but since $h/1$ is invertible in $A_{h}$, so is $f/1 = f$, and
$f^{-1} w_{h}$ is consequently a left inverse of $u_{h}$, which completes the proof.

**Proposition (19.1.13).**

<!-- label: 0_IV.19.1.13 -->

*Suppose the hypotheses of `(19.1.9)` are satisfied and suppose further that $(\mathfrak{J}_{\lambda})$ is a decreasing
sequence $(\mathfrak{J}_{n})$ and that $M$ is separated and complete. Then conditions a) and b) of `(19.1.9)` are also
equivalent to:*

*c) $u$ is left-invertible.*

One already knows that c) implies a) `(19.1.6)`. Conversely, if a) is satisfied, one knows (with the notations of
`(19.1.8)`) that $M_{n}$ is a direct factor of the projective $(A/\mathfrak{J}_{n})$-module $N_{n}$, hence $P_{n}$ is
also isomorphic to a direct factor of $N_{n}$, and consequently is projective; it then suffices to apply `(19.1.8)`.

Let us finally note the following proposition:

**Proposition (19.1.14).**

<!-- label: 0_IV.19.1.14 -->

*Let $A$ be a ring, $M$ an $A$-module of finite type, $N$ a projective $A$-module, $u : M \to N$ an $A$-homomorphism.*

*(i) For $u$ to be left-invertible, it is necessary and sufficient that, for every maximal ideal $\mathfrak{m}$ of $A$,
$u_{\mathfrak{m}} : M_{\mathfrak{m}} \to N_{\mathfrak{m}}$ be left-invertible.*

*(ii) Let $A'$ be an $A$-algebra which is a faithfully flat $A$-module. For $u$ to be left-invertible, it is necessary
and sufficient that $u \otimes 1 : M \otimes_{A} A' \to N \otimes_{A} A'$ be left-invertible.*

As in `(19.1.12)`, one can restrict to the case where $N$ is free of finite type; to say that $u$ is left-invertible
then means that $u$ is injective and that the quotient module $P = N/u(M)$ is projective, for $u(M)$ will then be a
direct factor of $N$. Note further that since $M$ is of finite type, $P$ is of *finite presentation*. This being so:

(i) The condition is obviously necessary. Conversely, if it is satisfied, one knows that $u$ is injective (Bourbaki,
Alg. comm., chap. II, §3, n° 3, th. 1) and since $P_{\mathfrak{m}} =
N_{\mathfrak{m}}/u_{\mathfrak{m}}(M_{\mathfrak{m}})$ is projective for every $\mathfrak{m}$, one knows that this implies
that $P$ is projective (*loc. cit.*, §5, n° 2, th. 1).

(ii) Here again, the condition is trivially necessary. Conversely, if it is satisfied, one knows that $u$ is injective
$(0_{I}, 6.4.1)$ and since $P \otimes_{A} A' = Coker(u \otimes 1)$ is projective, hence flat, one deduces that $P$ is a
flat $A$-module $(0_{I}, 6.6.3)$, hence projective since it is of finite presentation (Bourbaki, Alg. comm., chap. II,
§5, n° 2, cor. 2 of th. 1).

<!-- original page 174 -->

**Remark (19.1.15).**

<!-- label: 0_IV.19.1.15 -->

*The notion "dual" to that of formally left-invertible homomorphism is that of *formally right-invertible* homomorphism;
such a continuous $A$-homomorphism $u : M \to N$ verifies, by definition, the following condition: for every open
submodule $W$ of $N$, there exist an open submodule $V' \subset u^{-1}(W')$ of $M$, an open submodule $W'' \subset W$ of
$N$ and a homomorphism $h : N/W'' \to M/V'$ such that the canonical homomorphism $N/W'' \to N/W$ factors as*

```text
                              N/W'' ─h→ M/V' ─u'→ N/W
```

*where $u'$ is deduced from $u$ by passage to the quotients. This implies that $u$ is a formal epimorphism; if there
exists a continuous $A$-homomorphism $r : N \to M$ such that $u \circ r = 1_{N}$, one verifies at once that $u$ is
formally right-invertible. If the conditions of `(19.1.7)` are satisfied, for $u$ to be formally right-invertible, it is
necessary and sufficient that the $u_{\lambda}$ be right-invertible (that is, that the kernel of $u_{\lambda}$ be a
direct factor of $M/\mathfrak{J}_{\lambda} M$ and that $u_{\lambda}$ be an isomorphism of a supplement of
$Ker(u_{\lambda})$ onto $N/\mathfrak{J}_{\lambda} N$). We leave to the reader the task of stating and proving the
propositions corresponding to `(19.1.8)` and `(19.1.9)` (in the analogue of `(19.1.8)`, one must assume $M$ separated
and complete and that $M_{n}$ is a projective $(A/\mathfrak{J}_{n})$-module; in the analogue of `(19.1.9)`, one must
drop the hypothesis on the $N/\mathfrak{J}_{\lambda} N$, but assume on the other hand that, for every $\lambda$,
$M/\mathfrak{J}_{\lambda} M$ is a projective $(A/\mathfrak{J}_{\lambda})$-module).*

### 19.2. Formally projective modules

**Definition (19.2.1).**

<!-- label: 0_IV.19.2.1 -->

*Let $A$ be a topological ring. One says that a topological $A$-module $M$ is **formally projective** if it satisfies
the following condition: for every open ideal $\mathfrak{J}$ of $A$, every pair of (discrete) $(A/\mathfrak{J})$-modules
$P$, $Q$, every surjective $A$-homomorphism $u : P \to Q$ and every continuous $A$-homomorphism $v : M \to Q$, there
exists a continuous $A$-homomorphism $w : M \to P$ such that $v = u \circ w$.*

**(19.2.2)** To verify the condition of `(19.2.1)`, one may evidently restrict (by replacing $Q$ by $v(M)$ and $P$ by
$u^{-1}(v(M))$) to the case where $v$ is itself surjective; then $Q$ is isomorphic to $M/V$, where $V$ is an open
submodule of $M$ such that $\mathfrak{J}M \subset V$; condition `(19.2.1)` is then equivalent to saying that for every
discrete $(A/\mathfrak{J})$-module $P$ and every surjective $A$-homomorphism $u : P \to M/V$, there exist an open
submodule $V' \subset V$ of $M$ and an $A$-homomorphism $w : M/V' \to P$ such that the canonical homomorphism $M/V' \to
M/V$ factors as $M/V' \xrightarrow{w} P \xrightarrow{u} M/V$. We note that it suffices to verify this condition when
$\mathfrak{J}$ runs through a fundamental system of neighbourhoods of `0` in $A$ formed of ideals.

**(19.2.3)** Suppose there exists a fundamental system $(\mathfrak{J}_{\lambda})$ of open ideals of $A$ and a
fundamental system $(V_{\lambda})$ of open submodules of $M$, having the same set of indices as
$(\mathfrak{J}_{\lambda})$ and such that, for every $\lambda$, $M/V_{\lambda}$ is a *projective*
$(A/\mathfrak{J}_{\lambda})$-module. Then $M$ is formally projective: it suffices indeed, with the notations of
`(19.2.2)`, to take $\lambda$ such that $\mathfrak{J}_{\lambda} \subset \mathfrak{J}$ and $V_{\lambda} \subset V$; since
$P$ is also an $(A/\mathfrak{J}_{\lambda})$-module, the factorization of the canonical homomorphism $M/V_{\lambda} \to
M/V$ as $M/V_{\lambda} \to P \to M/V$ follows from the fact that we deal with an
$(A/\mathfrak{J}_{\lambda})$-homomorphism and that $M/V_{\lambda}$ is assumed to be a projective
$(A/\mathfrak{J}_{\lambda})$-module.

When the stricter condition of this number is satisfied, one says that $M$ is *strictly formally projective*.

**Proposition (19.2.4).**

<!-- label: 0_IV.19.2.4 -->

*Let $A$ be a topological ring, $M$ a topological $A$-module whose topology is deduced from that of $A$. For $M$ to be
formally projective, it is necessary and sufficient that it be strictly formally projective.*

<!-- original page 175 -->

We have just seen that the condition is sufficient. Conversely, suppose $M$ is formally projective and let
$(\mathfrak{J}_{\lambda})$ be a fundamental system of open ideals of $A$. For every $\lambda$, let $P$ be a free
$(A/\mathfrak{J}_{\lambda})$-module and $u : P \to M/\mathfrak{J}_{\lambda} M$ a surjective
$(A/\mathfrak{J}_{\lambda})$-homomorphism. There exists therefore a $\mathfrak{J}_{\mu} \subset \mathfrak{J}_{\lambda}$
such that the canonical homomorphism $M/\mathfrak{J}_{\mu} M \to M/\mathfrak{J}_{\lambda} M$ factors as
$M/\mathfrak{J}_{\mu} M \xrightarrow{w} P \xrightarrow{u} M/\mathfrak{J}_{\lambda} M$; but since
$w(\mathfrak{J}_{\mu}(M/\mathfrak{J}_{\mu} M)) \subset \mathfrak{J}_{\mu} P = 0$, $w$ factors as $M/\mathfrak{J}_{\mu} M
\to M/\mathfrak{J}_{\lambda} M \xrightarrow{v} P$, and it is clear that $u \circ v$ is the identity on
$M/\mathfrak{J}_{\lambda} M$, which proves that this $(A/\mathfrak{J}_{\lambda})$-module is projective.

**Proposition (19.2.5).**

<!-- label: 0_IV.19.2.5 -->

*Let $A$ be a topological ring, $M$ a topological $A$-module.*

*(i) For $M$ to be formally projective (resp. strictly formally projective), it is necessary and sufficient that the
topological `Â`-module $\hat{M}$ be so.*

*(ii) Let $A'$ be a topological $A$-algebra. If $M$ is formally projective (resp. strictly formally projective), then $M
\otimes_{A} A'$ (equipped with the tensor product topology) is a formally projective (resp. strictly formally
projective) topological $A'$-module.*

(i) It suffices to remark that when $\mathfrak{J}$ (resp. $V$) runs through the set of open ideals of $A$ (resp. the set
of open submodules of $M$), the separated completion $\hat{\mathfrak{J}}$ (resp. $\hat{V}$) runs through the set of open
ideals of `Â` (resp. the set of open submodules of $\hat{M}$), and $\hat{A}/\hat{\mathfrak{J}} = A/\mathfrak{J}$ (resp.
$\hat{M}/\hat{V} = M/V$) up to a canonical isomorphism; since the notion of formally projective (resp. strictly formally
projective) module only involves the $A/\mathfrak{J}$ and the $M/V$, one deduces (i) at once.

(ii) Suppose first $M$ is formally projective and set $M' = M \otimes_{A} A'$; let $\mathfrak{J}'$ be an open ideal of
$A'$, $P'$, $Q'$ two discrete $(A'/\mathfrak{J}')$-modules, $u' : P' \to Q'$ a surjective $A'$-homomorphism, $v' : M'
\to Q'$ a continuous $A'$-homomorphism. There is an open ideal $\mathfrak{J}$ of $A$ such that $\mathfrak{J} A' \subset
\mathfrak{J}'$, hence $P'$ and $Q'$ are also discrete $(A/\mathfrak{J})$-modules. If one considers the composite
$A$-homomorphism $v : M \xrightarrow{j} M' \xrightarrow{v'} Q'$, which is continuous, the hypothesis implies that there
exists a continuous $A$-homomorphism $w : M \to P'$ such that $v = u' \circ w$; but since $P'$ is an $A'$-topological
module, $w$ factors as $M \xrightarrow{j} M' \xrightarrow{w'} P'$, where $w'$ is a continuous $A'$-homomorphism, and
since $v' \circ j = (u' \circ w') \circ j$, one concludes that $v' = u' \circ w'$.

Suppose next that $M$ is strictly formally projective; let $(\mathfrak{J}_{\lambda})$ (resp. $(V_{\lambda})$) be a
fundamental system of open ideals of $A$ (resp. of open submodules of $M$) such that $(M/V_{\lambda})$ is a projective
$(A/\mathfrak{J}_{\lambda})$-module, and let $(\mathfrak{J}'_{\mu})$ be a fundamental system of open ideals of $A'$. One
has a fundamental system of neighbourhoods of `0` in $M'$ by taking the submodules $Im(M \otimes_{A}
\mathfrak{J}'_{\mu}) + Im(V_{\lambda} \otimes_{A} A') = W_{\lambda \mu}$, where $\lambda$ and $\mu$ are such that
$\mathfrak{J}_{\lambda} A' \subset \mathfrak{J}'_{\mu}$. Since $(M \otimes_{A} A')/W_{\lambda \mu} = (M/V_{\lambda})
\otimes_{A/\mathfrak{J}_{\lambda}} (A'/\mathfrak{J}'_{\mu})$ and since $M/V_{\lambda}$ is a projective
$(A/\mathfrak{J}_{\lambda})$-module, $M'/W_{\lambda \mu}$ is a projective $(A'/\mathfrak{J}'_{\mu})$-module.

### 19.3. Formally smooth algebras

**Definition (19.3.1).**

<!-- label: 0_IV.19.3.1 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra. One says that $B$ is a **formally smooth $A$-algebra**
if, for every discrete topological $A$-algebra $C$*

<!-- original page 176 -->

*and every nilpotent ideal $\mathfrak{J}$ of $C$, every continuous $A$-homomorphism $u : B \to C/\mathfrak{J}$ factors
as $B \xrightarrow{v} C \xrightarrow{\phi} C/\mathfrak{J}$, where $v$ is a continuous homomorphism and $\phi$ is the
canonical homomorphism.*

Definition `(19.3.1)` amounts to saying that the following property holds:

(P) For every *open* ideal $\mathfrak{K}$ of the $A$-algebra $B$ and every $A$-homomorphism $u' : B/\mathfrak{K} \to
C/\mathfrak{J}$, there is an open ideal $\mathfrak{K}' \subset \mathfrak{K}$ of $B$ such that the homomorphism $B \to
B/\mathfrak{K} \xrightarrow{u'} C/\mathfrak{J}$ factors as $B \to B/\mathfrak{K}' \xrightarrow{v'} C \to
C/\mathfrak{J}$, where $v'$ is an $A$-homomorphism.

Indeed, if $u : B \to C/\mathfrak{J}$ is a continuous $A$-homomorphism, it has for kernel $\mathfrak{K}$ an open ideal
of $B$, hence $u$ factors as $B \to B/\mathfrak{K} \xrightarrow{u'} C/\mathfrak{J}$, and if (P) is satisfied, it
suffices to apply it to $u'$ and to take for $v$ the composite $B \to B/\mathfrak{K}' \xrightarrow{v'} C$ to satisfy the
conditions of `(19.3.1)`. Conversely, suppose that $B$ is a formally smooth $A$-algebra; let us give an open ideal
$\mathfrak{K}$ of $B$ and an $A$-homomorphism $u' : B/\mathfrak{K} \to C/\mathfrak{J}$ and apply definition `(19.3.1)`
to $u : B \to B/\mathfrak{K} \to C/\mathfrak{J}$; if $v : B \to C$ is a continuous $A$-homomorphism such that $u$
factors as $B \xrightarrow{v} C \to C/\mathfrak{J}$, the ideal $\mathfrak{K}' = Ker(v) \cap \mathfrak{K}$ of $B$ is open
and contained in $\mathfrak{K}$; consequently $v$ factors as $B \to B/\mathfrak{K}' \xrightarrow{v'} C$, and $v'$ indeed
satisfies condition (P).

**Proposition (19.3.2).**

<!-- label: 0_IV.19.3.2 -->

*Let $A$ be a discrete ring, $V$ a projective $A$-module; the symmetric algebra $B = S^{\bullet}_{A}(V)$, equipped with
the discrete topology, is a formally smooth $A$-algebra.*

Indeed, with the notations $C$ and $\mathfrak{J}$ having the same meaning as in `(19.3.1)`, let $u : B \to
C/\mathfrak{J}$ be a homomorphism of $A$-algebras, which by restriction to $V = S^{1}_{A}(V)$ gives a homomorphism of
$A$-modules $u_{1} : V \to C/\mathfrak{J}$; since $V$ is projective, $u_{1}$ factors as $V \xrightarrow{v_{1}} C \to
C/\mathfrak{J}$, and $v_{1}$ extends to a homomorphism of $A$-algebras $v : S^{\bullet}_{A}(V) \to C$, such that the
composite $\phi \circ v$ coincides with $u$ on $V$, hence $\phi \circ v = u$, which proves the proposition.

**Corollary (19.3.3).**

<!-- label: 0_IV.19.3.3 -->

*If $A$ is a discrete ring, every polynomial algebra $B = A[T_{\alpha}]_{\alpha \in I}$, equipped with the discrete
topology, is a formally smooth $A$-algebra.*

**Proposition (19.3.4).**

<!-- label: 0_IV.19.3.4 -->

*Let $A$ be a topological ring, and let $B = A[[T_{\alpha}]]_{\alpha \in I} = \sum_{\lambda \in \mathbb{N}^{(I)}}
c_{\lambda} T^{\lambda}$ be a formal power series ring (broad algebra over $A$ of the monoid $\mathbb{N}^{(I)}$,
identified as an $A$-module with the product $A^{\mathbb{N}^{(I)}}$). If one equips $B$ with the product topology, $B$
is a formally smooth $A$-algebra.*

Let $(\mathfrak{L}_{\mu})_{\mu \in M}$ be a fundamental system of open ideals of $A$. For every finite part $H$ of $I$,
every $\mu \in M$ and every integer $n$, denote by $\mathfrak{K}_{H, \mu, n}$ the neighbourhood of `0` in $B$ consisting
of the $(c_{\lambda})$ such that for every $\lambda = (\lambda_{\alpha})_{\alpha \in I}$ with $\lambda_{\alpha} = 0$ for
$\alpha \notin H$ and $\sum_{\alpha \in H} \lambda_{\alpha} \leqslant n$, one has $c_{\lambda} \in \mathfrak{L}_{\mu}$.
One verifies immediately that the $\mathfrak{K}_{H, \mu, n}$ form a fundamental system of neighbourhoods of `0` in $B$
and are ideals of $B$, hence the product topology is compatible with the $A$-algebra structure of $B$.

Let us first note, with the same notations, the

**Lemma (19.3.4.1).**

<!-- label: 0_IV.19.3.4.1 -->

*Let $E$ be a discrete $A$-algebra.*

*(i) If $f : B \to E$ is a continuous $A$-homomorphism, there exists a finite part $H$ of $I$ such that $f(T_{\alpha}) =
0$ for $\alpha \notin H$, and $f(T_{\alpha})$ is nilpotent in $E$ for every $\alpha \in H$.*

<!-- original page 177 -->

*(ii) Conversely, let $H$ be a finite part of $I$, $(z_{\alpha})_{\alpha \in H}$ a family of nilpotent elements of $E$.
There exists a continuous $A$-homomorphism $g : B \to E$ and only one such that $g(T_{\alpha}) = z_{\alpha}$ for $\alpha
\in H$ and $g(T_{\alpha}) = 0$ for $\alpha \notin H$.*

(i) follows at once from the fact that $f^{-1}(0)$ is a neighbourhood of `0` in the product $A$-module
$A^{\mathbb{N}^{(I)}}$, whence $f(T^{\lambda}) = 0$ except for a finite number of values of $\lambda \in
\mathbb{N}^{(I)}$. To prove (ii), it suffices to remark that the polynomial ring $B' = A[T_{\alpha}]_{\alpha \in I}$ is
dense in $B$; the existence and uniqueness of the restriction $g | B'$ are trivial and its continuity follows from the
hypothesis that the $f(T_{\alpha})$ for $\alpha \in H$ are nilpotent, for if $(f(T_{\alpha}))^{n} = 0$ for every $\alpha
\in H$, one has $g(T^{\lambda}) = 0$ for every $\lambda = (\lambda_{\alpha})_{\alpha \in I}$ of finite support except
those for which $\lambda_{\alpha} = 0$ for $\alpha \notin H$ and $\lambda_{\alpha} < n$ for $\alpha \in H$, that is,
except for a finite number of values of $\lambda$.

This lemma being established, and the notations $C$ and $\mathfrak{J}$ having the same meaning as in `(19.3.1)`, one has
$u(T_{\alpha}) = 0$ except for $\alpha \in H$, $H$ being a finite part of $I$, and the $z_{\alpha} = u(T_{\alpha})$ for
$\alpha \in H$ are nilpotent in $C/\mathfrak{J}$; since $\mathfrak{J}$ is nilpotent, there exists a family
$(x_{\alpha})_{\alpha \in H}$ of nilpotent elements of $C$ whose canonical images in $C/\mathfrak{J}$ are the
$z_{\alpha}$; if $v$ is the continuous $A$-homomorphism of $B$ into $C$ such that $v(T_{\alpha}) = 0$ for $\alpha \notin
H$, $v(T_{\alpha}) = x_{\alpha}$ for $\alpha \in H$, it is clear that $u$ factors as $B \xrightarrow{v} C \to
C/\mathfrak{J}$.

**Proposition (19.3.5).**

<!-- label: 0_IV.19.3.5 -->

*Let $A$ be a topological ring.*

*(i) $A$ is a formally smooth $A$-algebra.*

*(ii) If $B$ is a formally smooth $A$-algebra and $C$ a formally smooth $B$-algebra, then $C$ is a formally smooth
$A$-algebra.*

*(iii) Let $B$ be a formally smooth $A$-algebra, $A'$ a topological $A$-algebra; then the topological $A'$-algebra $B
\otimes_{A} A'$ $(0_{I}, 7.7.5 and 7.7.6)$ is formally smooth.*

*(iv) Let $B$ be a topological $A$-algebra, $S$ (resp. $T$) a multiplicative part of $A$ (resp. $B$) such that the
canonical image of $S$ in $B$ is contained in $T$. If $B$ is a formally smooth $A$-algebra, then $T^{-1} B$ is a
formally smooth $S^{-1} A$-algebra.*

*(v) Let $B_{i}$ ($1 \leqslant i \leqslant n$) be topological $A$-algebras. For $\prod^{n}_{i=1} B_{i}$ to be a formally
smooth $A$-algebra, it is necessary and sufficient that each of the $B_{i}$ be so.*

(i) If $C$ is a discrete $A$-algebra, $\phi : C \to C/\mathfrak{J}$ the canonical homomorphism of $C$ onto an arbitrary
quotient $A$-algebra of $C$, the only $A$-homomorphism of $A$ into $C/\mathfrak{J}$ is the composite homomorphism $A
\xrightarrow{\psi} C \xrightarrow{\phi} C/\mathfrak{J}$, where $\psi$ is the homomorphism defining the $A$-algebra
structure on $C$; since $\psi$ is continuous, the condition of `(19.3.1)` is trivially satisfied.

(ii) Let $\alpha : A \to B$, $\beta : B \to C$ be the continuous homomorphisms defining respectively the $A$-algebra
structure on $B$ and the $B$-algebra structure on $C$, so that $\beta \circ \alpha$ defines the $A$-algebra structure on
$C$. Let $E$ be a discrete $A$-algebra, $\mathfrak{L}$ a nilpotent ideal of $E$, $u : C \to E/\mathfrak{L}$ a continuous
$A$-homomorphism, so that $u \circ \beta \circ \alpha$ is the homomorphism defining the $A$-algebra structure of
$E/\mathfrak{L}$. Since $B$ is a formally smooth $A$-algebra, the continuous $A$-homomorphism $u \circ \beta : B \to
E/\mathfrak{L}$ factors as $B \xrightarrow{v} E \to E/\mathfrak{L}$, where $v$ is a continuous $A$-homomorphism; $v$ and
$u \circ \beta$ then define on $E$ and $E/\mathfrak{L}$ respectively structures of topological $B$-algebra, for which
$E/\mathfrak{L}$ is

<!-- original page 178 -->

still the (discrete) quotient algebra of the $B$-algebra $E$. Furthermore, $u$ is a continuous $B$-homomorphism, hence
factors as $C \xrightarrow{w} E \to E/\mathfrak{L}$, where $w$ is a continuous $B$-homomorphism; since $v \circ \alpha$
is the $A$-homomorphism defining the $A$-algebra structure on $E$, $w$ is indeed a continuous $A$-homomorphism, whence
our assertion.

(iii) Let $C$ be a discrete topological $A'$-algebra, $\mathfrak{J}$ a nilpotent ideal of $C$, $u : B \otimes_{A} A' \to
C/\mathfrak{J}$ a continuous $A'$-homomorphism. If one composes $u$ with the canonical homomorphism $\rho : B \to B
\otimes_{A} A'$, one obtains (since $A \to B \xrightarrow{\rho} B \otimes_{A} A'$ is equal to the composite $A \to A'
\xrightarrow{\sigma} B \otimes_{A} A'$) a continuous $A$-homomorphism which, by hypothesis, therefore factors as $B
\xrightarrow{v} C \to C/\mathfrak{J}$, where $v$ is a continuous $A$-homomorphism (for the topological $A$-algebra
structure on $C$ defined by the composite $A \to A' \xrightarrow{u} C$ of the canonical homomorphisms). The equality of
the composites $A \to B \xrightarrow{v} C$ and $A \to A' \xrightarrow{u} C$ thus entails the existence of a continuous
ring homomorphism $f : B \otimes_{A} A' \to C$ such that $v = f \circ \rho$ and $u = f \circ \sigma$ $(0_{I}, 7.7.6)$;
since the composite homomorphisms $B \xrightarrow{\rho} B \otimes_{A} A' \xrightarrow{f} C \to C/\mathfrak{J}$ and $B
\xrightarrow{\rho} B \otimes_{A} A' \xrightarrow{u} C/\mathfrak{J}$ (resp. $A' \xrightarrow{\sigma} B \otimes_{A} A'
\xrightarrow{f} C \to C/\mathfrak{J}$ and $A' \xrightarrow{\sigma} B \otimes_{A} A' \xrightarrow{u} C/\mathfrak{J}$) are
equal, one indeed has the factorization $u : B \otimes_{A} A' \to C \to C/\mathfrak{J}$, which establishes (iii).

(iv) The topology considered on $S^{-1} A$ (resp. $T^{-1} B$) is naturally that for which a fundamental system of
neighbourhoods of `0` is formed of the $S^{-1} \mathfrak{J}$ (resp. $T^{-1} \mathfrak{K}$), where $\mathfrak{J}$ (resp.
$\mathfrak{K}$) runs through a fundamental system of open ideals of $A$ (resp. $B$) $(0_{I}, 7.6.1)$. If $\alpha : A \to
B$ is the canonical homomorphism, it is clear that the canonical homomorphism $\alpha' : S^{-1} A \to T^{-1} B$ deduced
from $\alpha$ (and whose existence results from $\alpha(S) \subset T$ by hypothesis) is continuous $(0_{I}, 7.6.6)$. Let
then $C$ be a discrete topological $S^{-1} A$-algebra, $\mathfrak{J}$ a nilpotent ideal of this algebra, $u : T^{-1} B
\to C/\mathfrak{J}$ a continuous $S^{-1} A$-homomorphism; then the composite $B \to T^{-1} B \to C/\mathfrak{J}$ is a
continuous $A$-homomorphism which, by hypothesis, factors as $B \to C \to C/\mathfrak{J}$, where $v$ is a continuous
$A$-homomorphism. Since for every $t \in T$, $t/1$ is invertible in $T^{-1} B$, $u(t/1)$ is invertible in
$C/\mathfrak{J}$. Since $\mathfrak{J}$ is nilpotent, every element of the class $u(t/1)$ in $C$, and in particular
$v(t)$, is invertible in $C$ $(0_{I}, 7.1.12)$, and consequently $v$ factors as $B \to T^{-1} B \xrightarrow{w} C$;
since $v$ is continuous, so is $w$ $(0_{I}, 7.6.6)$, and it is an $S^{-1} A$-homomorphism because the composite $A \to B
\to T^{-1} B \to C$ is equal to

```text
                              A → S⁻¹ A → T⁻¹ B → C,
```

hence $S^{-1} A \to T^{-1} B \to C$ is the canonical homomorphism defining on $C$ the $S^{-1} A$-algebra structure.
Finally, the composite homomorphisms $B \to T^{-1} B \to C \to C/\mathfrak{J}$ and $B \to T^{-1} B \xrightarrow{u}
C/\mathfrak{J}$ being equal, the same reasoning shows that $u$ is indeed equal to the composite $T^{-1} B
\xrightarrow{w} C \to C/\mathfrak{J}$, whence (iv).

Finally, (v) is immediate, the data of a continuous $A$-homomorphism of $B = \prod^{n}_{i=1} B_{i}$ into $C$ (resp.
$C/\mathfrak{J}$) being equivalent to that of $n$ continuous $A$-homomorphisms $B_{i} \to C$

<!-- original page 179 -->

(resp. $B_{i} \to C/\mathfrak{J}$), and any continuous $A$-homomorphism $B_{j} \to C$ (resp. $B_{j} \to C/\mathfrak{J}$)
giving by composition a continuous $A$-homomorphism $B \to B_{j} \to C$ (resp. $B \to B_{j} \to C/\mathfrak{J}$).

**Proposition (19.3.6).**

<!-- label: 0_IV.19.3.6 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra, `Â` and $\hat{B}$ the respective separated completions of
$A$ and $B$, so that $\hat{B}$ is a topological `Â`-algebra. The following conditions are equivalent:*

*a) $B$ is a formally smooth $A$-algebra.*

*b) $\hat{B}$ is a formally smooth $A$-algebra.*

*c) $\hat{B}$ is a formally smooth `Â`-algebra.*

Of course, the `Â`-algebra structure on $\hat{B}$ is defined by the homomorphism $\hat{\phi}$, if $\phi : A \to B$ is
the homomorphism defining the $A$-algebra structure on $B$. Since every discrete $A$-algebra $C$ is separated and
complete, it is also an `Â`-algebra (by canonical extension of the homomorphism from $A$ into $C$), and a continuous
$A$-homomorphism from $B$ into $C$ gives by canonical extension an $A$-homomorphism (and *a fortiori* an
`Â`-homomorphism) from $\hat{B}$ into $C$ (in other words, every $A$-homomorphism $B \to C$ factors as $B \to \hat{B}
\to C$ in a unique way). These remarks and definition `(19.3.1)` entail the proposition at once.

**Corollary (19.3.7).**

<!-- label: 0_IV.19.3.7 -->

*Under the hypotheses of `(19.3.5, (iv))`, the topological $A{S^{-1}}$-algebra $B{T^{-1}}$ is formally smooth.*

This follows from the definitions $(0_{I}, 7.6.1 and 7.6.7)$ and from `(19.3.5, (iv))` and `(19.3.6)`.

**Proposition (19.3.8).**

<!-- label: 0_IV.19.3.8 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra, and suppose that for every open ideal $\mathfrak{K}$ of
$B$, $\mathfrak{K}^{2}$ is also open. Let $A'$, $B'$ be topological rings obtained by equipping $A$ and $B$ with
topologies finer than the initial topologies, and suppose that the canonical homomorphism $\phi : A \to B$ is still a
continuous homomorphism from $A'$ into $B'$. Then, if $B'$ is a formally smooth $A'$-algebra, $B$ is a formally smooth
$A$-algebra.*

It suffices to apply the following lemma:

**Lemma (19.3.8.1).**

<!-- label: 0_IV.19.3.8.1 -->

*Let $C$ be a discrete $A$-algebra, $\mathfrak{J}$ a nilpotent ideal of $C$. Suppose that the square of every open ideal
of $B$ is open. Then, if a composite homomorphism $v : B \xrightarrow{u} C \to C/\mathfrak{J}$ is continuous, the
homomorphism $u$ is continuous.*

Indeed, $\mathfrak{K} = u^{-1}(\mathfrak{J})$ is the kernel of $v$ and is open by hypothesis; since there exists an
integer $n$ such that $\mathfrak{J}^{n} = 0$, $\mathfrak{K}^{n}$ is contained in $Ker(u)$; but by induction on $h$, it
follows from the hypothesis that $\mathfrak{K}^{2}$ is open, hence so is $\mathfrak{K}^{n}$ for every $n$, and
consequently $Ker(u)$ is also open, which proves our assertion.

One observes that the hypothesis on $B$ means that the topology of $B$ is the *least upper bound* of the
$\mathfrak{K}$-preadic topologies, where $\mathfrak{K}$ runs through the set of open ideals of $B$. If $B$ is a preadic
ring $(0_{I}, 7.1.9)$, this condition is always satisfied.

**(19.3.9)** We are now going to see that the property of being formally smooth implies "lifting" properties of
homomorphisms under more general conditions than those of definition `(19.3.1)`.

<!-- original page 180 -->

**Proposition (19.3.10).**

<!-- label: 0_IV.19.3.10 -->

*Let $A$ be a topological ring, $B$ a formally smooth $A$-algebra. Let $C$ be a topological $A$-algebra, $\mathfrak{J}$
an ideal of $C$, satisfying the following conditions:*

*1° $C$ is metrizable and complete.*

*2° $\mathfrak{J}$ is closed and the sequence $(\mathfrak{J}^{n})$ tends to `0`.*

*Then every continuous $A$-homomorphism $u : B \to C/\mathfrak{J}$ factors as $B \xrightarrow{v} C \to C/\mathfrak{J}$,
where $v$ is a continuous $A$-homomorphism.*

Let $(\mathfrak{L}_{n})$ be a decreasing sequence of ideals of $C$ forming a fundamental system of neighbourhoods of
`0`. For every $n$, consider the discrete $A$-algebra $C/\mathfrak{L}_{n}$ and the ideal $(\mathfrak{J} +
\mathfrak{L}_{n})/\mathfrak{L}_{n}$ of this algebra; since there exists $k$ such that $\mathfrak{J}^{k} \subset
\mathfrak{L}_{n}$, $(\mathfrak{J} + \mathfrak{L}_{n})/\mathfrak{L}_{n}$ is nilpotent. For every $n$, let $u_{n}$ be the
continuous homomorphism $B \xrightarrow{u} C/\mathfrak{J} \to C/(\mathfrak{J} + \mathfrak{L}_{n}) =
(C/\mathfrak{L}_{n})/((\mathfrak{J} + \mathfrak{L}_{n})/\mathfrak{L}_{n})$; by hypothesis $u_{n}$ factors as $B
\xrightarrow{v_{n}} C/\mathfrak{L}_{n} \xrightarrow{\phi_{n}} C/(\mathfrak{J} + \mathfrak{L}_{n})$, where $v_{n}$ is a
continuous $A$-homomorphism. Let us show that one may choose the $v_{n}$ step by step so that $v_{n}$ factors as

```text
                              B ─v_{n+1}→ C/𝔏_{n+1} → C/𝔏_n
```

for every $n$ (in other words, so that the $v_{n}$ form a projective system of homomorphisms). This will follow from the
next lemma:

**Lemma (19.3.10.1).**

<!-- label: 0_IV.19.3.10.1 -->

*Let $B$ be a formally smooth $A$-algebra, $E$, $E'$ two discrete topological $A$-algebras, $\mathfrak{K}$ (resp.
$\mathfrak{K}'$) a nilpotent ideal of $E$ (resp. $E'$), $f : E \to E'$ a surjective $A$-homomorphism such that
$f(\mathfrak{K}) \subset \mathfrak{K}'$, $f' : E/\mathfrak{K} \to E'/\mathfrak{K}'$ the homomorphism deduced from $f$ by
passage to the quotients. Let $u : B \to E/\mathfrak{K}$ be a continuous $A$-homomorphism, $u'$ the composite
homomorphism $B \xrightarrow{u} E/\mathfrak{K} \xrightarrow{f'} E'/\mathfrak{K}'$, and let $v' : B \to E'$ be a
continuous $A$-homomorphism such that $u'$ factors as $B \xrightarrow{v'} E' \to E'/\mathfrak{K}'$. Then there exists a
continuous $A$-homomorphism $v : B \to E$ such that $v'$ factors as $B \xrightarrow{v} E \xrightarrow{f} E'$.*

In the commutative diagram

```text
                              E  ──f──→  E'
                              │          │
                              ↓          ↓
                              E/𝔎 ─f'─→ E'/𝔎'
```

all the homomorphisms are surjective; if $\mathfrak{L}$ is the kernel of $f$, $E'$ is identified with $E/\mathfrak{L}$
and $\mathfrak{K}'$ with $(\mathfrak{K} + \mathfrak{L})/\mathfrak{L}$. Let us now use the following elementary lemma:

**Lemma (19.3.10.2).**

<!-- label: 0_IV.19.3.10.2 -->

*Let $F$ be a ring (not necessarily commutative), $\mathfrak{a}$, $\mathfrak{b}$ two two-sided ideals of $F$; then the
fibre product $(F/\mathfrak{a}) \times_{F/(\mathfrak{a} + \mathfrak{b})} (F/\mathfrak{b})$ is canonically identified
with $F/(\mathfrak{a} \cap \mathfrak{b})$.*

This is none other than a particular application of `(18.1.7)`, where, in diagram `(18.1.7.1)`, one replaces $G$ by
$F/(\mathfrak{a} \cap \mathfrak{b})$, $\mathfrak{J}'$ by $\mathfrak{b}/(\mathfrak{a} \cap \mathfrak{b})$, $F$ by
$F/\mathfrak{b}$, $\mathfrak{K}$ by $(\mathfrak{a} + \mathfrak{b})/\mathfrak{b}$, $B$ by $F/(\mathfrak{a} +
\mathfrak{b})$ and $\theta$ by the canonical bijective $F$-homomorphism $(\mathfrak{a} + \mathfrak{b})/\mathfrak{b}
\cong \mathfrak{a}/(\mathfrak{a} \cap \mathfrak{b})$.

<!-- original page 181 -->

Applying this lemma to the situation of `(19.3.10.1)`, the commutativity of the diagram

```text
                              B ─v'→ E' = E/𝔏
                              │      │
                            u │      │
                              ↓      ↓
                              E/𝔎 ─f'─→ E'/𝔎'
```

shows the existence of a homomorphism $w : B \to E/(\mathfrak{K} \cap \mathfrak{L})$ such that $v'$ and $u$ factor as $B
\xrightarrow{w} E/(\mathfrak{K} \cap \mathfrak{L}) \to E/\mathfrak{L}$ and $B \xrightarrow{w} E/(\mathfrak{K} \cap
\mathfrak{L}) \to E/\mathfrak{K}$ respectively; since the kernel of $w$ contains the intersection of those of $v'$ and
$u$, it is open in $B$ and $w$ is continuous. Finally, it is clear that $\mathfrak{K} \cap \mathfrak{L}$ is nilpotent,
hence $w$ factors as $B \xrightarrow{v} E \to E/(\mathfrak{K} \cap \mathfrak{L})$, where $v$ is a continuous
$A$-homomorphism answering the question.

Returning to the proof of `(19.3.10)`, the existence of $v_{n+1}$ follows from lemma `(19.3.10.1)` applied by replacing
$E$, $E'$, $\mathfrak{K}$, $\mathfrak{K}'$ by $C/\mathfrak{L}_{n+1}$, $C/\mathfrak{L}_{n}$, $(\mathfrak{J} +
\mathfrak{L}_{n+1})/\mathfrak{L}_{n+1}$ and $(\mathfrak{J} + \mathfrak{L}_{n})/\mathfrak{L}_{n}$ respectively, and $u$,
$u'$ and $v'$ by $u_{n+1}$, $u_{n}$ and $v_{n}$ respectively. We note that, since $C$ is separated and complete, it is
equal to $\lim\leftarrow(C/\mathfrak{L}_{n})$, and $v = \lim\leftarrow v_{n}$ is a continuous $A$-homomorphism from $B$
into $C$. Since $\mathfrak{J}$ is closed in $C$, one has $\mathfrak{J} = \bigcap_{n} (\mathfrak{J} + \mathfrak{L}_{n})$;
since $C/\mathfrak{J}$ is metrizable and complete and since the $(\mathfrak{J} + \mathfrak{L}_{n})/\mathfrak{J}$ form a
fundamental system of neighbourhoods of `0` in $C/\mathfrak{J}$, one has $C/\mathfrak{J} =
\lim\leftarrow(C/(\mathfrak{J} + \mathfrak{L}_{n}))$ and $\lim\leftarrow \phi_{n}$ is the canonical map $\phi : C \to
C/\mathfrak{J}$. Since $\lim\leftarrow u_{n} = u$, one has indeed $u = v \circ \phi$. Q.E.D.

**Corollary (19.3.11).**

<!-- label: 0_IV.19.3.11 -->

*Let $A$ be a topological ring, $B$ a formally smooth $A$-algebra, $C$ a complete Noetherian local ring, $\mathfrak{J}$
an ideal distinct from $C$, $\phi : A \to C$ a continuous homomorphism, making $C$ a topological $A$-algebra. Then every
continuous $A$-homomorphism $u_{0} : B \to C_{0} = C/\mathfrak{J}$ factors as $B \to C \to C/\mathfrak{J}$, where $u$ is
a continuous $A$-homomorphism.*

All the conditions of `(19.3.10)` are indeed satisfied $(0_{I}, 7.3.5)$.

**Proposition (19.3.12).**

<!-- label: 0_IV.19.3.12 -->

*Let $A$ be a topological ring, $B$ a formally smooth $A$-algebra, $C$ a topological $A$-algebra, $\mathfrak{J}$ an
ideal of $C$, satisfying the following conditions:*

*1° There exists a fundamental system of open ideals $\mathfrak{L}_{\lambda}$ of $C$ such that the $C_{\lambda} =
C/\mathfrak{L}_{\lambda}$ are Artinian rings and that the canonical homomorphism $C \to \lim\leftarrow C_{\lambda}$ is
an isomorphism of topological rings.*

*2° The ideal $\mathfrak{J}$ is closed in $C$ and topologically nilpotent.*

*3° The square of every open ideal of $B$ is open.*

*Under these conditions, every continuous $A$-homomorphism $u : B \to C/\mathfrak{J}$ factors as $B \to C \to
C/\mathfrak{J}$, where $v$ is a continuous $A$-homomorphism.*

Let $\mathfrak{J}_{\lambda} = (\mathfrak{J} + \mathfrak{L}_{\lambda})/\mathfrak{L}_{\lambda}$ be the canonical image of
$\mathfrak{J}$ in $C_{\lambda}$, which is a nilpotent ideal, and let $u_{\lambda}$ be the composite homomorphism $B
\xrightarrow{u} C/\mathfrak{J} \to C_{\lambda}/\mathfrak{J}_{\lambda} = C/(\mathfrak{J} + \mathfrak{L}_{\lambda})$. Let
us show that every $A$-homomorphism $w : B \to C$ such that $u$ factors as $B \xrightarrow{w} C \to C/\mathfrak{J}$ is
necessarily *continuous*; in effect, for every $\lambda$, there is an open ideal $\mathfrak{K}$ of $B$ such that
$u(\mathfrak{K}) \subset (\mathfrak{J} + \mathfrak{L}_{\lambda})/\mathfrak{J}$, whence $w(\mathfrak{K}) \subset
\mathfrak{J} + \mathfrak{L}_{\lambda}$, hence there is a power $\mathfrak{K}^{2^{m}}$ of $\mathfrak{K}$ such that
$w(\mathfrak{K}^{2^{m}}) \subset \mathfrak{L}_{\lambda}$, which establishes our assertion since $\mathfrak{K}^{2^{m}}$
is open in $B$. One can therefore restrict to finding an $A$-homomorphism $w$ having the preceding property without
worrying about its continuity properties. Now, the set $\operatorname{Hom}(B, C)$ of all $A$-algebra homomorphisms of
$B$ into $C$ is equal to $\lim\leftarrow \operatorname{Hom}(B, C_{\lambda})$, and the latter is *closed* in the
$C$-module $C^{B}_{\lambda}$, equipped with the product topology, for which it is *linearly compact* since $C_{\lambda}$
is Artinian. For every $\lambda$, let $W_{\lambda}$

<!-- original page 182 -->

be the set of $w_{\lambda} \in \operatorname{Hom}(B, C_{\lambda})$ such that $u_{\lambda}$ factors as $B
\xrightarrow{w_{\lambda}} C_{\lambda} \to C_{\lambda}/\mathfrak{J}_{\lambda}$; $W_{\lambda}$ is a closed linear variety
in the $C$-module $\operatorname{Hom}(B, C_{\lambda})$, non-empty since $B$ is formally smooth. In the product
$\prod_{\mu \leqslant \lambda} \operatorname{Hom}(B, C_{\mu}) = E_{\lambda}$, consider the linear sub-variety
$U_{\lambda}$ formed by the $(w_{\mu})_{\mu \leqslant \lambda}$ such that $w_{\mu} = \phi_{\mu \lambda} \circ
w_{\lambda}$ for $\mu \leqslant \lambda$ and $w_{\lambda} \in W_{\lambda}$ (where $\phi_{\mu \lambda} : C_{\lambda} \to
C_{\mu}$ is the canonical homomorphism), which is also closed. Finally, let $V_{\lambda}$ be the linear variety in the
product $\prod_{\mu} \operatorname{Hom}(B, C_{\mu})$, product of $U_{\lambda}$ and of the $\operatorname{Hom}(B,
C_{\mu})$ for $\mu \nleqslant \lambda$, which is still closed. Everything reduces to seeing that the intersection of the
$V_{\lambda}$ is non-empty, for an element $w$ of this intersection will belong to $\lim\leftarrow \operatorname{Hom}(B,
C_{\lambda})$ by definition. Moreover, since $\mathfrak{J}$ is closed, and $C = \lim\leftarrow C_{\lambda}$ linearly
compact, $C/\mathfrak{J}$ is identified with $\lim\leftarrow C_{\lambda}/\mathfrak{J}_{\lambda}$ and the canonical map
$\phi : C \to C/\mathfrak{J}$ with $\lim\leftarrow \psi_{\lambda}$, where $\psi_{\lambda}$ is the canonical map
$C_{\lambda} \to C_{\lambda}/\mathfrak{J}_{\lambda}$. One then concludes as in `(19.3.10)` that $\psi \circ w = u$.

### 19.4. First criteria for formal smoothness

**Proposition (19.4.1).**

<!-- label: 0_IV.19.4.1 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra; suppose that there exist two decreasing filtering
families $(\mathfrak{J}_{\alpha})_{\alpha \in I}$, $(\mathfrak{K}_{\alpha})_{\alpha \in I}$ of ideals of $A$ and $B$
respectively, such that: 1° $(\mathfrak{J}_{\alpha})$ tends to `0` in $A$ and $(\mathfrak{K}_{\alpha})$ tends to `0` in
$B$; 2° for every $\alpha \in I$ one has $\mathfrak{J}_{\alpha} B \subset \mathfrak{K}_{\alpha}$ (so that
$B/\mathfrak{K}_{\alpha}$ is a topological $(A/\mathfrak{J}_{\alpha})$-algebra); 3° for every $\alpha \in I$,
$B/\mathfrak{K}_{\alpha}$ is a formally smooth $(A/\mathfrak{J}_{\alpha})$-algebra. Then $B$ is a formally smooth
$A$-algebra.*

Indeed, let $C$ be a discrete $A$-algebra, $\mathfrak{L}$ a nilpotent ideal of $C$, $\mathfrak{K}$ an open ideal of $B$;
by hypothesis there is an $\alpha \in I$ such that $\mathfrak{K}_{\alpha} \subset \mathfrak{K}$, hence $B/\mathfrak{K}$
is a quotient of $B/\mathfrak{K}_{\alpha}$ by an open ideal. Every $A$-homomorphism $u' : B/\mathfrak{K} \to
C/\mathfrak{L}$ is also an $(A/\mathfrak{J}_{\alpha})$-homomorphism, hence there exists an open ideal $\mathfrak{K}'$ of
$B$ such that $\mathfrak{K}_{\alpha} \subset \mathfrak{K}' \subset \mathfrak{K}$ and that $B/\mathfrak{K}_{\alpha} \to
B/\mathfrak{K} \xrightarrow{u'} C/\mathfrak{L}$ factors as $B/\mathfrak{K}_{\alpha} \to B/\mathfrak{K}' \xrightarrow{v'}
C \to C/\mathfrak{L}$, where $v'$ is an $(A/\mathfrak{J}_{\alpha})$-homomorphism; whence the conclusion, by virtue of
the remark following `(19.3.1)`.

**Corollary (19.4.2).**

<!-- label: 0_IV.19.4.2 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra, $(\mathfrak{J}_{\alpha})_{\alpha \in I}$ a decreasing
filtering family of ideals of $A$ tending to `0`. For $B$ to be a formally smooth $A$-algebra, it is necessary and
sufficient that for every $\alpha \in I$, if one sets $A_{\alpha} = A/\mathfrak{J}_{\alpha}$, $B_{\alpha} =
B/\mathfrak{J}_{\alpha} B$, $B_{\alpha}$ be a formally smooth $A_{\alpha}$-algebra.*

The condition is sufficient by `(19.4.1)`, and it is also necessary by `(19.3.5, (iii))`.

**Proposition (19.4.3).**

<!-- label: 0_IV.19.4.3 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra. Suppose that for every discrete $A$-algebra $C$ and every
ideal $\mathfrak{J}$ of $C$ such that $\mathfrak{J}^{2} = 0$, every continuous $A$-homomorphism $u : B \to
C/\mathfrak{J}$ factors as $B \to C \to C/\mathfrak{J}$, where $v$ is a continuous $A$-homomorphism. Then $B$ is a
formally smooth $A$-algebra.*

Indeed, with the same notations, let $\mathfrak{K}$ be an arbitrary nilpotent ideal of $C$, and consider a continuous
$A$-homomorphism $u' : B \to C/\mathfrak{K}$. Suppose that $\mathfrak{K}^{m} = 0$, and set $C_{i} = C/\mathfrak{K}^{i}$
for $1 \leqslant i \leqslant m$, so that $C_{m} = C$, $\mathfrak{K}^{i-1}/\mathfrak{K}^{i}$ is an ideal of square zero
$\mathfrak{J}_{i}$ in $C_{i}$, and $C_{i-1} = C_{i}/\mathfrak{J}_{i}$; the hypothesis then entails by induction on $i$
the existence of continuous $A$-homomorphisms $u_{i} : B \to C_{i}$ such that $u_{1} = u'$ and that $u_{i}$ factors as
$B \xrightarrow{u_{i+1}} C_{i+1} \to C_{i+1}/\mathfrak{J}_{i+1} = C_{i}$; whence the conclusion.

**Proposition (19.4.4).**

<!-- label: 0_IV.19.4.4 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra*

<!-- original page 183 -->

*(commutative). For $B$ to be a formally smooth $A$-algebra, it is necessary and sufficient that for every discrete
topological $B$-module $L$, annulled by an open ideal of $B$, one have (cf. `(18.5.1)`) $Exalcotop_{A}(B, L) = 0$.*

Let $(\mathfrak{K}_{\lambda})$ be a decreasing fundamental system of open ideals of $B$ and set $B_{\lambda} =
B/\mathfrak{K}_{\lambda}$. Consider a discrete topological $A$-algebra $C$ and an ideal $\mathfrak{J}$ of $C$ such that
$\mathfrak{J}^{2} = 0$, so that $C$ is an $A$-extension of $C/\mathfrak{J}$ by $\mathfrak{J}$; suppose given an
$A$-homomorphism $u : B_{\lambda} \to C/\mathfrak{J}$ and form the $A$-extension $E_{\lambda}$ of $B_{\lambda}$ by
$\mathfrak{J}$, inverse image of $C$ by the homomorphism $u$ `(18.2.5)`; this is a topological $A$-algebra for the
discrete topology. If $Exalcotop_{A}(B, L) = 0$, there exists by definition `(18.5.1)` a $\mu$ such that
$\mathfrak{K}_{\mu} \subset \mathfrak{K}_{\lambda}$ and such that the inverse image extension $E_{\mu}$ is $A$-trivial;
but this means `(18.1.6)` that there exists a continuous $A$-homomorphism $v : B_{\mu} \to E_{\mu}$ such that the
canonical homomorphism $B_{\mu} \to B_{\lambda}$ factors as $B_{\mu} \xrightarrow{v} E_{\mu} \to B_{\lambda}$; one
concludes at once that $B_{\mu} \to B_{\lambda} \to C/\mathfrak{J}$ factors as $B_{\mu} \to E_{\mu} \to C \to
C/\mathfrak{J}$, and this proves, by virtue of `(19.3.1)` and `(19.4.3)`, that $B$ is a formally smooth $A$-algebra. The
converse is immediate, by applying `(19.3.1)` to the case where $C$ is a topological $A$-algebra which is an
$A$-extension of $B_{\lambda}$ by $L$, and to the identity homomorphism $B_{\lambda} \to B_{\lambda} = C/L$.

When $A$ and $B$ are *discrete* rings, the criterion of formal smoothness `(19.4.4)` reduces to

```text
(19.4.4.1)            Exalcom_A(B, L) = 0      for every B-module L;
```

in other words, every commutative $A$-extension of $B$ by a $B$-module must be $A$-trivial.

**Corollary (19.4.5).**

<!-- label: 0_IV.19.4.5 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra (commutative).*

*(i) Suppose that $B$ is a formally smooth $A$-algebra. Then, for every open ideal $\mathfrak{K}$ of $B$, every
$(B/\mathfrak{K})$-module $L$ and every $A$-bilinear symmetric Hochschild 2-cocycle $f$ from $(B/\mathfrak{K}) \times
(B/\mathfrak{K})$ into $L$ `(18.4.3)`, there exists an open ideal $\mathfrak{K}' \subset \mathfrak{K}$ such that, if
$\phi : B/\mathfrak{K}' \to B/\mathfrak{K}$ is the canonical homomorphism, $f \circ (\phi \times \phi)$ is an
$A$-bilinear Hochschild 2-coboundary from $(B/\mathfrak{K}') \times (B/\mathfrak{K}')$ into $L$.*

*(ii) If $B$ is a formally projective $A$-module `(19.2.1)` and if condition (i) is satisfied, $B$ is a formally smooth
$A$-algebra.*

(i) The 2-cocycle $f$ defines a Hochschild $A$-extension $C$ of $B/\mathfrak{K}$ by $L$ `(18.4.3)`. Applying `(19.3.1)`
to $C$, to the square-zero ideal $L$ of $C$ and to the identity homomorphism $B/\mathfrak{K} \to B/\mathfrak{K} = C/L$,
one deduces condition (i) by virtue of `(18.4.3)`.

(ii) Let us apply criterion `(19.4.3)`, by considering an open ideal $\mathfrak{K}$ of $B$, an open ideal $\mathfrak{J}$
of $A$ such that $\mathfrak{J}^{2} = \mathfrak{K}$, and an $(A/\mathfrak{J})$-extension $E$ of $B/\mathfrak{K}$ by $L$.
Since $B$ is a formally projective $A$-module, the canonical continuous $A$-linear map $p : B \to B/\mathfrak{K}$
factors as $B \xrightarrow{w} E \to B/\mathfrak{K}$, where $w$ is a continuous $A$-linear map `(19.2.1)`, which itself
factors as $B \to B/\mathfrak{K}' \xrightarrow{w} E$ where $\mathfrak{K}'$ is an open ideal of $B$ contained in
$\mathfrak{K}$; replacing $\mathfrak{J}$ by a smaller ideal, one may suppose that $\mathfrak{J} B \subset
\mathfrak{K}'$. Then the inverse image by the canonical homomorphism $B/\mathfrak{K}' \to B/\mathfrak{K}$ of the
extension $E$ of $B/\mathfrak{K}$ by $L$ is an $(A/\mathfrak{J})$-Hochschild extension $E'$ of $B/\mathfrak{K}'$ by $L$;

<!-- original page 184 -->

applying (i) to a cocycle defining this extension `(18.4.3)`, one concludes that there is an open ideal $\mathfrak{K}''
\subset \mathfrak{K}'$ of $B$ such that the inverse image `E''` of $E$ by $B/\mathfrak{K}'' \to B/\mathfrak{K}'$ is
$A$-trivial. Q.E.D.

**Corollary (19.4.6).**

<!-- label: 0_IV.19.4.6 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra which is a formally projective $A$-module. Let $A'$ be an
$A$-algebra equipped with the topology deduced from that of $A$. Suppose furthermore that $A'$ is a faithfully flat
$A$-module, and that one of the following conditions is satisfied:*

*1° There exists a fundamental system $(\mathfrak{J}_{\lambda})$ of open ideals of $A$ and a fundamental system
$(\mathfrak{M}_{\lambda})$ of open ideals of $B$, having the same set of indices and such that, for every $\lambda$, one
has $\mathfrak{J}_{\lambda} B \subset \mathfrak{M}_{\lambda}$ and that $B/\mathfrak{M}_{\lambda}$ is a projective
$(A/\mathfrak{J}_{\lambda})$-module of finite type.*

*2° $A'$ is a projective $A$-module of finite type.*

*Then, for $B' = B \otimes_{A} A'$ (equipped with the tensor product topology) to be a formally smooth $A'$-algebra, it
is necessary and sufficient that $B$ be a formally smooth $A$-algebra.*

The sufficiency of the condition is contained in `(19.3.5, (iii))`, without any further hypothesis on $B$ or $A'$. To
prove the converse, we shall apply criterion `(19.4.5)`; under hypothesis 2°, we still denote by
$(\mathfrak{M}_{\lambda})$ a fundamental system of open ideals of $B$, and, for every $\lambda$, by
$\mathfrak{J}_{\lambda}$ an open ideal of $A$ such that $\mathfrak{J}_{\lambda} B \subset \mathfrak{M}_{\lambda}$; in
both cases, we shall set $A_{\lambda} = A/\mathfrak{J}_{\lambda}$, $B_{\lambda} = B/\mathfrak{M}_{\lambda}$,
$A'_{\lambda} = A_{\lambda} \otimes_{A} A'$, $B'_{\lambda} = B_{\lambda} \otimes_{A} A'$. Let $f$ be an
$A_{\lambda}$-bilinear symmetric Hochschild 2-cocycle from $B_{\lambda} \times B_{\lambda}$ into a $B_{\lambda}$-module
$L$; by extension of scalars, one deduces a Hochschild 2-cocycle $f' = f \otimes 1$, $A'$-bilinear symmetric, from
$B'_{\lambda} \times B'_{\lambda}$ into $L' = L \otimes_{A} A'$. Since by hypothesis $B'$ is a formally smooth
$A'$-algebra, there exists, by `(19.4.5, (i))`, an index $\mu$ such that $\mathfrak{M}_{\mu} \subset
\mathfrak{M}_{\lambda}$, and such that, if $\phi' : B'_{\mu} \to B'_{\lambda}$ is the canonical map, $f' \circ (\phi'
\times \phi')$ is a Hochschild 2-coboundary from $B'_{\mu} \times B'_{\mu}$ into $L'$; in other words, its image $c'$ in
the Hochschild group $H^{2}_{A'_{\mu}}(B'_{\mu}, L')^{s}$ is zero; it is clear that if $\phi : B_{\mu} \to B_{\lambda}$
is the canonical homomorphism, and $c$ the class of $f \circ (\phi \times \phi)$ in the Hochschild group
$H^{2}_{A_{\mu}}(B_{\mu}, L)^{s}$, $c'$ is the canonical image of $c$. Now, if $P_{\bullet}$ is the complex relative to
the rings $A_{\mu}$ and $B_{\mu}$ defined in `(18.4.5)`, serving for the computation of $H^{2}_{A_{\mu}}(B_{\mu},
L)^{s}$, the analogous complex relative to the rings $A'_{\mu}$ and $B'_{\mu}$ is evidently $P_{\bullet} \otimes_{A}
A'$; under hypothesis 1°, the construction of $P_{\bullet}$ shows that this is an $A_{\mu}$-projective module of finite
type. One concludes therefore from Bourbaki, Alg., chap. II, 3rd ed., §5, n° 3, prop. 7 that, under both hypotheses, one
has $\operatorname{Hom}_{A'_{\mu}}(P_{\bullet} \otimes_{A} A', L \otimes_{A} A') =
(\operatorname{Hom}_{A_{\mu}}(P_{\bullet}, L)) \otimes_{A} A'$ up to a canonical isomorphism; since $A'$ is a flat
$A$-module, one has therefore `(18.4.5)`

```text
                       H²_{A'_μ}(B'_μ, L')^s = (H²_{A_μ}(B_μ, L)^s) ⊗_A A'
```

and one may therefore write $c' = c \otimes 1$; but since $A'$ is a faithfully flat $A$-module, the hypothesis $c' = 0$
entails $c = 0$, which completes the proof.

**Proposition (19.4.7).**

<!-- label: 0_IV.19.4.7 -->

*Let $A$ be a preadmissible topological ring, $\mathfrak{J}$ an ideal of definition of $A$ $(0_{I}, 7.1.2)$, $B$ a
topological $A$-algebra which is a formally projective $A$-module. Consider the topological quotient rings $A_{0} =
A/\mathfrak{J}$, $B_{0} = B/\mathfrak{J} B$; then, for $B$ to be*

<!-- original page 185 -->

*a formally smooth $A$-algebra, it is necessary and sufficient that `B_0` be a formally smooth `A_0`-algebra.*

The necessity of the condition results from `(19.4.2)`. To see that it is sufficient, note first that by considering a
fundamental system of open neighbourhoods of `0` in $A$ formed of ideals $\mathfrak{J}_{\alpha}$ contained in
$\mathfrak{J}$, one can, by virtue of `(19.4.2)`, reduce to the case where $A$ is *discrete* since
$B/\mathfrak{J}_{\alpha} B$ is a formally projective $(A/\mathfrak{J}_{\alpha})$-module `(19.2.5)`; by definition of a
preadmissible ring, $\mathfrak{J}$ is then *nilpotent*. It moreover suffices to prove the proposition when
$\mathfrak{J}^{2} = 0$, for if $\mathfrak{J}^{m} = 0$, one will apply it successively to the rings $A_{k} =
A/\mathfrak{J}^{k}$ and $B_{k} = B/\mathfrak{J}^{k} B$ and to the ideal $\mathfrak{J}^{k-1}/\mathfrak{J}^{k}$ of $A_{k}$
for $k = 2, 3, \cdots, m$, noting `(19.2.5)` that $B_{k} = B \otimes_{A} A_{k}$ is a formally projective $A_{k}$-module.
Let us apply criterion `(19.4.5, (ii))` by considering an open ideal $\mathfrak{K}$ of $B$ and an $A$-bilinear symmetric
Hochschild 2-cocycle $f$ from $(B/\mathfrak{K}) \times (B/\mathfrak{K})$ into a $(B/\mathfrak{K})$-module $L$. Let us
consider first the special case where $\mathfrak{J} L = 0$, so that $L$ may also be considered as a $(B_{0}/\mathfrak{K}
B_{0})$-module, and $f$ factors as

```text
            (B/𝔎) × (B/𝔎) → (B_0/𝔎 B_0) × (B_0/𝔎 B_0) ─f_0→ L
```

where $f_{0}$ is a symmetric bilinear Hochschild 2-cocycle. By virtue of the hypothesis, there is therefore an open
ideal $\mathfrak{K}' \subset \mathfrak{K}$ in $B$ and an `A_0`-linear map $g_{0} : B_{0}/\mathfrak{K}' B_{0} \to L$ such
that $f_{0}(\phi_{0}(x), \phi_{0}(y)) = x g_{0}(y) - g_{0}(xy) + g_{0}(x) y$ for $x$, $y$ in $B_{0}/\mathfrak{K}'
B_{0}$, $\phi_{0} : B_{0}/\mathfrak{K}' B_{0} \to B_{0}/\mathfrak{K} B_{0}$ being the canonical homomorphism. One
concludes at once that the composite $A$-linear map $g : B/\mathfrak{K}' \to B_{0}/\mathfrak{K}' B_{0}
\xrightarrow{g_{0}} L$ is such that $dg = f \circ (\phi \times \phi)$, where $\phi : B/\mathfrak{K}' \to B/\mathfrak{K}$
is the canonical homomorphism.

Let us pass now to the general case, and consider first the $(B/\mathfrak{K})$-module $L/\mathfrak{J} L = L'$, for which
one has $\mathfrak{J} L' = 0$; if $f'$ is the $A$-bilinear map composed of $(B/\mathfrak{K}) \times (B/\mathfrak{K})
\xrightarrow{f} L \to L'$, $f'$ is still a symmetric Hochschild 2-cocycle, and by virtue of what precedes, there exist
an open ideal $\mathfrak{K}' \subset \mathfrak{K}$ in $B$ and an $A$-linear map $g' : B/\mathfrak{K}' \to L'$ satisfying
$dg' = f' \circ (\phi' \times \phi')$ for the canonical map $\phi' : B/\mathfrak{K}' \to B/\mathfrak{K}$. Since $B$ is a
formally projective $A$-module, there exist an open ideal $\mathfrak{K}'_{1} \subset \mathfrak{K}'$ and an $A$-linear
map $g_{1} : B/\mathfrak{K}'_{1} \to L$ such that the homomorphism $B/\mathfrak{K}'_{1} \to B/\mathfrak{K}'
\xrightarrow{g'} L'$ factors as $B/\mathfrak{K}'_{1} \xrightarrow{g_{1}} L \to L'$. Consider then the Hochschild
2-cocycle

```text
        f_1(x, y) = f(φ_1(x), φ_1(y)) − x g_1(y) + g_1(xy) − g_1(x) y,
```

an $A$-bilinear symmetric map of $(B/\mathfrak{K}'_{1}) \times (B/\mathfrak{K}'_{1})$ into $L$. The choice of $g_{1}$
entails that $f_{1}$ takes its values in $\mathfrak{J} L$. Since $\mathfrak{J}(\mathfrak{J} L) = 0$, one may once more
apply the first case, and there is therefore an open ideal $\mathfrak{K}'' \subset \mathfrak{K}'_{1}$ and an $A$-linear
map $g_{2} : B/\mathfrak{K}'' \to \mathfrak{J} L$ such that

```text
        f_1(φ_2(x), φ_2(y)) = x g_2(y) − g_2(xy) + g_2(x) y
```

in $(B/\mathfrak{K}'') \times (B/\mathfrak{K}'')$, $\phi_{2} : B/\mathfrak{K}'' \to B/\mathfrak{K}'_{1}$ being the
canonical map; the $A$-linear map $g = g_{2} + g_{1} \circ \phi_{2} : B/\mathfrak{K}'' \to L$ therefore satisfies $dg =
f \circ (\phi \times \phi)$ for the canonical map $\phi : B/\mathfrak{K}'' \to B/\mathfrak{K}$. Q.E.D.

<!-- original page 186 -->

### 19.5. Formal smoothness and associated graded rings

**(19.5.1)** Let $C$ be a (commutative) topological ring, let $V$ be a topological $C$-module, and consider the
symmetric algebra $S_{C}(V) = \oplus_{n} S^{n}_{C}(V)$, which we shall endow canonically with a linear topology
compatible with its $C$-algebra structure. For this, let $U$ be an open submodule of $V$, and let $U \cdot S_{C}(V)$ be
the graded ideal it generates in $S_{C}(V)$; we take as fundamental system of neighbourhoods of `0` in $S_{C}(V)$ the
set of sums $\mathfrak{a} \cdot S_{C}(V) + U \cdot S_{C}(V)$, where $\mathfrak{a}$ (resp. $U$) runs through a
fundamental system of open ideals (resp. of open submodules) of $C$ (resp. $V$). Note that if the topology of $V$ is
coarser than the topology induced from that of $C$, one may restrict to pairs $(\mathfrak{a}, U)$ such that
$\mathfrak{a} V \subset U$, so that $\mathfrak{a} \cdot S_{C}(V) + U \cdot S_{C}(V) = \mathfrak{a} \cdot S_{C}(V) + U
\cdot S_{C}(V)$; in this case the topology induced on each $S^{n}_{C}(V)$ for $n \geq 1$ admits as fundamental system of
neighbourhoods of `0` the $U \cdot S^{n-1}_{C}(V)$, where $U$ runs through the open submodules of $V$; in particular, on
$V = S^{1}_{C}(V)$ it coincides with the given topology (in general it is coarser than the latter). Furthermore, in
every case, the topological algebra $S_{C}(V)$ thus defined is, for the categories of topological $C$-modules and
topological $C$-algebras, the solution of the same universal problem as for the categories of $C$-modules and
$C$-algebras. Indeed, let $E$ be a topological $C$-algebra, $u : V \to E$ a homomorphism of $C$-modules, $S(u) =
\mathit{v}$ its canonical extension to $S_{C}(V)$. Suppose $u$ is continuous; then, if $\mathfrak{b}$ is an open ideal
of $E$, its inverse image $u^{-1}(\mathfrak{b})$ is an open $C$-submodule of $V$, and the image under $\mathit{v}$ of $U
\cdot S_{C}(V)$ is therefore contained in $\mathfrak{b}$; since moreover there exists an open ideal $\mathfrak{a}$ of
$C$ such that $\mathfrak{a} \cdot E \subset \mathfrak{b}$, whence $\mathit{v}(\mathfrak{a} \cdot S_{C}(V)) \subset
\mathfrak{b}$, this proves that $\mathit{v}$ is continuous. Conversely, if $\mathit{v}$ is continuous and $\mathfrak{b}$
is an open ideal of $E$, there exists an open submodule $U$ of $V$ such that $\mathit{v}(U \cdot S_{C}(V)) \subset
\mathfrak{b}$, and in particular $\mathit{v}(U \cdot S^{1}_{C}(V)) \subset \mathfrak{b}$, that is, $u(U) \subset
\mathfrak{b}$, so $u$ is continuous. Recall in addition that one has a canonical isomorphism of (discrete) topological
$C$-modules

```text
(19.5.1.1)                    S_C(V) / U · S_C(V) ⥲ S_{C/𝔞}(V/U).
```

**(19.5.2)** Let $A$ be a topological ring, $B$ a topological (commutative) $A$-algebra, $\mathfrak{J}$ an ideal of $B$
(not necessarily open or closed); throughout the sequel, we endow $\mathfrak{J}$ and the $\mathfrak{J}^{n}$ ($n \geq 2$)
with the topology induced from that of $B$, the quotients $C = B/\mathfrak{J}$, $\mathfrak{J}^{n}/\mathfrak{J}^{n+1} =
gr^{n}_{\mathfrak{J}}(B)$ with the quotient topology, so that the $\mathfrak{J}^{n}/\mathfrak{J}^{n+1}$ are topological
$C$-modules; the canonical injection $\mathfrak{J}/\mathfrak{J}^{2} \to gr^{\bullet}_{\mathfrak{J}}(B)$ extends to a
homomorphism (at first non-topological) of $C$-algebras

$$ \phi : S_{C}(\mathfrak{J}/\mathfrak{J}^{2}) \to gr^{\bullet}_{\mathfrak{J}}(B) $$

which for each $n$ gives a surjective homomorphism of $C$-modules

$$ (19.5.2.1) \phi_{n} : S^{n}_{C}(\mathfrak{J}/\mathfrak{J}^{2}) \to \mathfrak{J}^{n}/\mathfrak{J}^{n+1}. $$

When $S_{C}(\mathfrak{J}/\mathfrak{J}^{2})$ is endowed with the topology defined in `(19.5.1)`, the homomorphisms
$\phi_{n}$ are continuous, by virtue of the universal property `(19.5.1)` of $S_{C}(\mathfrak{J}/\mathfrak{J}^{2})$

<!-- original page 187 -->

applied to the topological $A$-algebra $E = gr^{\bullet}_{\mathfrak{J}}(B/\mathfrak{J}^{n+1})$ endowed with the product
topology of those of the $\mathfrak{J}^{j}/\mathfrak{J}^{j+1}$, and to the canonical injection
$\mathfrak{J}/\mathfrak{J}^{2} \to E$. Note that here the topology on $\mathfrak{J}/\mathfrak{J}^{2}$ is coarser than
the topology induced from that of $C$ (this latter topology on $\mathfrak{J}/\mathfrak{J}^{2}$ being also the topology
induced from that of $B$).

**Theorem (19.5.3).**

<!-- label: 0_IV.19.5.3 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra, $\mathfrak{J}$ an ideal of $B$, $C = B/\mathfrak{J}$ the
quotient topological $A$-algebra. Assume that the $A$-algebra $C$ is formally smooth. Then:*

*(i) If $B$ is a formally smooth $A$-algebra, $\mathfrak{J}/\mathfrak{J}^{2}$ is a formally projective topological
$C$-module `(19.2.1)`.*

*(ii) If $B$ is a formally smooth $A$-algebra and a preadmissible ring $(0_{I}, 7.1.2)$, the homomorphisms $\phi_{n}$
`(19.5.2)` are formal bimorphisms `(19.1.2)`.*

*(iii) Conversely, suppose that $B$ is preadmissible, that the sequence $(\mathfrak{J}^{n})$ tends to `0` in $B$, that
$\mathfrak{J}/\mathfrak{J}^{2}$ is a formally projective $C$-module, and that the $\phi_{n}$ are formal bimorphisms.
Then $B$ is a formally smooth $A$-algebra.*

The proof of this theorem is long and cluttered with technical details; we shall therefore begin by proving a simpler
corollary, in which the guiding ideas appear more clearly; this corollary is moreover the special case of theorem
`(19.5.3)` that will be most frequently used in the sequel.

**Corollary (19.5.4).**

<!-- label: 0_IV.19.5.4 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra, $\mathfrak{J}$ an ideal of $B$ such that the topology of
$B$ is the $\mathfrak{J}$-preadic topology. Assume that the discrete $A$-algebra $C = B/\mathfrak{J}$ is formally
smooth. Then the following three conditions are equivalent:*

*a) $B$ is a formally smooth $A$-algebra.*

*b) $\mathfrak{J}/\mathfrak{J}^{2}$ is a projective $C$-module and the canonical homomorphism*

$$ \phi : S_{C}(\mathfrak{J}/\mathfrak{J}^{2}) \to gr^{\bullet}_{\mathfrak{J}}(B) $$

*is bijective.*

*c) The separated completion $\hat{B}$ of $B$ is a topological $A$-algebra isomorphic to an $A$-algebra of the form
$\hat{B}'$, where $B' = S_{C}(V)$, $V$ being a projective $C$-module and $B'$ being endowed with the $B'^{+}$-preadic
topology, where $B'^{+}$ is the augmentation ideal.*

**(19.5.4.1)** Let us first prove that a) implies that $\mathfrak{J}/\mathfrak{J}^{2}$ is a projective $C$-module. Let
$P$ and $Q$ be two $C$-modules, $u : P \to Q$ a surjective $C$-homomorphism, and $v : \mathfrak{J}/\mathfrak{J}^{2} \to
Q$ a $C$-homomorphism. The ring $B/\mathfrak{J}^{2}$, considered as a $B$-extension of $C$ by
$\mathfrak{J}/\mathfrak{J}^{2}$, gives by $v$ a $B$-extension $E = (B/\mathfrak{J}^{2})
\oplus_{\mathfrak{J}/\mathfrak{J}^{2}} Q$ of $C$ by $Q$ `(18.2.8)`. Since $C$ is a formally smooth discrete $A$-algebra,
the extension $E$ is $A$-trivial `(19.4.4)` and can therefore be identified with $D_{C}(Q)$ `(18.2.3)`. The surjective
homomorphism $u : P \to Q$ then canonically defines a surjective $A$-homomorphism $\tilde{u} : D_{C}(P) \to D_{C}(Q)$
`(18.2.9)` whose kernel is an ideal $\mathfrak{a}$ of the extension $E' = D_{C}(P)$, contained in $P$, and a fortiori of
square zero. Let $f : B \to E = E'/\mathfrak{a}$ be the homomorphism defining the $B$-algebra structure of $E$; since
$\mathfrak{a}$ is of square zero and $B$ is a formally smooth

<!-- original page 188 -->

$A$-algebra, $f$ factors as $B \to E' \to E'/\mathfrak{a}$, where $g$ is a continuous $A$-homomorphism. The diagram

```text
                                          g
                                   B ────────→ E'
                                   │           │
                                   │           ↓ ũ
                                   ↓
                                  B/𝔍² ──────→ E
                                          v'
```

where $v'$ is deduced from $v$ `(18.2.8)`, is commutative. Furthermore, the image of $\mathfrak{J}$ under $\tilde{u}
\circ g$ is contained in $Q$, so the image of $\mathfrak{J}$ under $g$ is contained in $P + \mathfrak{a} = P$, and the
image of $\mathfrak{J}^{2}$ under $g$ is zero. Restricting $g$ and `ũ` to $\mathfrak{J}$, we obtain a commutative
diagram

```text
                                          u
                                  P ──────────→ Q
                                   ↖           ↗
                                     ↖       ↗
                                       w   v
                                          ↘
                                       𝔍/𝔍²
```

which proves that the $C$-module $\mathfrak{J}/\mathfrak{J}^{2}$ is projective.

**(19.5.4.2)** Let us prove next that a) implies that $\phi$ is bijective, which will complete the proof that a) implies
b). Set $E_{n} = B/\mathfrak{J}^{n+1}$, and denote by $F_{n}$ the quotient of $S_{C}(\mathfrak{J}/\mathfrak{J}^{2})$ by
the $(n+1)$-st power of its augmentation ideal. Since $\mathfrak{J}^{n+1}$ is nilpotent in $E_{n}$ and $C$ is a formally
smooth discrete $A$-algebra, the identity automorphism of $C$ factors as $C \to E_{n} \to C =
E_{n}/(\mathfrak{J}^{n+1})$ where $f$ is an $A$-homomorphism; on the other hand, since $\mathfrak{J}/\mathfrak{J}^{2}$
is a projective $C$-module by `(19.5.4.1)`, the identity automorphism of $\mathfrak{J}/\mathfrak{J}^{2}$ factors as
$\mathfrak{J}/\mathfrak{J}^{2} \to \mathfrak{J}/\mathfrak{J}^{n+1} \to \mathfrak{J}/\mathfrak{J}^{2}$, where $g$ is a
$C$-linear map; from $f$ and $g$ one obtains canonically a homomorphism of $C$-algebras
$S_{C}(\mathfrak{J}/\mathfrak{J}^{2}) \to E_{n}$ which moreover (by definition of $g$) vanishes on the $(n+1)$-st power
of the augmentation ideal of $S_{C}(\mathfrak{J}/\mathfrak{J}^{2})$, whence, on passing to the quotient, a surjective
$A$-homomorphism of algebras $\mathit{v} : F_{n} \to E_{n}$ such that $gr^{0}(\mathit{v})$ and $gr^{1}(\mathit{v})$ are
the identity automorphisms of $C$ and $\mathfrak{J}/\mathfrak{J}^{2}$. By definition of the canonical homomorphism
$\phi$, one sees that $gr^{j}(\mathit{v}) = \phi_{j}$ for every $j \leq n$. Note now that the kernel $\mathfrak{N}$ of
$\mathit{v}$ is a nilpotent ideal of $F_{n}$, so that $E_{n}$ may be identified with $F_{n}/\mathfrak{N}$. Since $B$ is
a formally smooth $A$-algebra, the canonical $A$-homomorphism $p_{n} : B \to E_{n} = B/\mathfrak{J}^{n+1}$, which is
continuous, factors as $B \to F_{n} \to E_{n}$, where $w$ is a continuous $A$-homomorphism; since $gr^{0}(\mathit{v})$
is the identity, $w(\mathfrak{J})$ is contained in the augmentation ideal of $F_{n}$, whence $w(\mathfrak{J}^{n+1}) =
0$, so that $w$ factors as $B \to B/\mathfrak{J}^{n+1} \to F_{n} \to E_{n}$, and the composite $E_{n} \to F_{n} \to
E_{n}$ is the identity. Furthermore, since $gr^{0}(\mathit{v})$ and $gr^{1}(\mathit{v})$ are the identity automorphisms
of $C$ and $\mathfrak{J}/\mathfrak{J}^{2}$, the same is true of $gr^{0}(w')$ and $gr^{1}(w')$. Since
$gr^{\bullet}(E_{n})$ is generated by $gr^{1}(E_{n})$, the composite homomorphism

```text
                                                  gr^j(w')           gr^j(𝑣)
                              gr^j(E_n) ──────────────→ gr^j(F_n) ──────────→ gr^j(E_n)
```

is the identity for every $j \leq n$, since this is true for $j = 0$ and $j = 1$; taking $j = n$, one thus proves that
$\phi_{n}$ is injective, which completes the proof that a) implies b).

<!-- original page 188 -->

**(19.5.4.3)** Let us prove next that b) implies a). The same reasoning as at the beginning of `(19.5.4.2)` proves the
existence of a surjective $A$-homomorphism of algebras $\mathit{v} : F_{n} \to E_{n}$ such that $gr^{j}(\mathit{v}) =
\phi_{j}$ for every $j$; since $\phi_{j}$ is bijective for every $j$ and the filtrations of $F_{n}$ and $E_{n}$ are
finite, one concludes that $\mathit{v}$ is bijective `(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1)`. Now
let $G$ be a discrete topological $A$-algebra, $\mathfrak{N}$ an ideal of square zero in $G$, $f : B \to G/\mathfrak{N}$
a continuous $A$-homomorphism of algebras. Since $G$ is discrete, there exists an integer $m$ such that $f$ vanishes on
$\mathfrak{J}^{m}$, so $f$ factors as $B \to E_{m} \to G/\mathfrak{N}$, where one takes $n = 2m$. One thus obtains by
composition a continuous $A$-homomorphism of algebras $r : C \to F_{n} \to E_{m} \to G/\mathfrak{N}$, and since $C$ is a
formally smooth discrete $A$-algebra, $r$ factors as $C \to G \to G/\mathfrak{N}$, so that $G$ is equipped by $r'$ with
a $C$-algebra structure. On the other hand, the restriction to $\mathfrak{J}/\mathfrak{J}^{2}$ of the homomorphism
$f_{n} : F_{n} \to E_{n} \to G/\mathfrak{N}$ is a $C$-linear map $g : \mathfrak{J}/\mathfrak{J}^{2} \to G/\mathfrak{N}$.
Since $\mathfrak{J}/\mathfrak{J}^{2}$ is a projective $C$-module, $g$ factors as $\mathfrak{J}/\mathfrak{J}^{2} \to G
\to G/\mathfrak{N}$, where $h$ is a $C$-linear map; by extension, one deduces a homomorphism of $C$-algebras $w :
S_{C}(\mathfrak{J}/\mathfrak{J}^{2}) \to G$, and by construction every element of degree $m$ has under $w$ an image
which is an element of $\mathfrak{N}$, so every element of degree $n = 2m$ has image zero, since $\mathfrak{N}^{2} = 0$;
in other words, $w$ factors as $S_{C}(\mathfrak{J}/\mathfrak{J}^{2}) \to F_{n} \to G$. By construction, the composite
$F_{n} \to G \to G/\mathfrak{N}$ coincides with $f_{n}$ on $C$ and on $\mathfrak{J}/\mathfrak{J}^{2}$, so is equal to
$f_{n}$. Finally, the composite

```text
                                 B → E_m → F_n → G → G/𝔑
```

being equal to $f$, one sees that $B$ is a formally smooth $A$-algebra.

**(19.5.4.4)** It remains to prove the equivalence of a) and c). First, c) implies a): indeed, $B'$ is a formally smooth
$C$-algebra for the discrete topology `(19.3.2)`, hence also for the $B'^{+}$-preadic topology `(19.3.8)`; since $C$ is
a formally smooth $A$-algebra, $B'$ is also a formally smooth $A$-algebra `(19.3.5, (ii))` and finally $\hat{B}'$ is a
formally smooth $A$-algebra `(19.3.6)`, so $B$ is a formally smooth $A$-algebra `(19.3.6)`. It remains to see that a)
implies c). Note first that since $C$ is a formally smooth $A$-algebra, the identity homomorphism $C \to B/\mathfrak{J}$
factors as $C \to B \to B/\mathfrak{J}$, where $C \to B$ is an $A$-homomorphism `(19.3.10)`; $B$, and consequently all
the $B/\mathfrak{J}^{n+1}$, are thus endowed with $C$-algebra structures. On the other hand, since
$\mathfrak{J}/\mathfrak{J}^{2}$ is a projective $C$-module by b), the canonical injection $\mathfrak{J}/\mathfrak{J}^{2}
\to B/\mathfrak{J}^{2}$ allows one to form a projective system of $C$-homomorphisms $v_{n} :
\mathfrak{J}/\mathfrak{J}^{2} \to B/\mathfrak{J}^{n+1}$ for $n \geq 1$, hence also (by the universal property of the
symmetric algebra) a projective system of homomorphisms of $C$-algebras $\mathit{v}_{n} :
S_{C}(\mathfrak{J}/\mathfrak{J}^{2}) = B' \to B/\mathfrak{J}^{n+1}$; moreover it is clear that $\mathit{v}_{n}$ vanishes
on $(B'^{+})^{n+1}$ and since $gr^{0}(\mathit{v}_{n}) = \phi_{0}$ and $gr^{1}(\mathit{v}_{n}) = \phi_{1}$, one has
$gr^{j}(\mathit{v}_{n}) = \phi_{j}$ for $0 \leq j \leq n$. Since the $\phi_{j}$ are isomorphisms by b), and the
filtrations of $B'/(B'^{+})^{n+1}$ and of $B/\mathfrak{J}^{n+1}$ are finite, one concludes that $\mathit{v}_{n}$ is
bijective for

<!-- original page 189 -->

every $n$ `(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1)`; whence c) by passage to the projective limit.

**Remark (19.5.5).**

<!-- label: 0_IV.19.5.5 -->

*Under the general hypotheses of `(19.5.4)`, suppose in addition that $\mathfrak{J}$ is a maximal ideal of $B$, so that
$C = B/\mathfrak{J}$ is a field, and that $\mathfrak{J}/\mathfrak{J}^{2}$ is a $C$-vector space of finite dimension.
Then conditions a), b) and c) of `(19.5.4)` are also equivalent to the following:*

*d) Given a polynomial algebra $E = C[T_{1}, \cdots, T_{n}]$ over the field $C$, and denoting by $\mathfrak{n}$ the
maximal ideal of $E$ generated by the $T_{i}$ ($1 \leq i \leq n$), then, for every ideal $\mathfrak{b}$ of $E$
containing some power $\mathfrak{n}^{h}$, every homomorphism $v : B \to E/\mathfrak{b}$ of $C$-augmented $A$-algebras
factors as $B \to E/\mathfrak{n}^{h} \to E/\mathfrak{b}$, where $w$ is an $A$-homomorphism.*

Indeed, since $\mathfrak{J}/\mathfrak{J}^{2}$ is here a free $C$-module, it suffices to verify that condition d) implies
that the canonical homomorphism $\phi : S_{C}(\mathfrak{J}/\mathfrak{J}^{2}) \to gr^{\bullet}_{\mathfrak{J}}(B)$ is
bijective. Now here $S_{C}(\mathfrak{J}/\mathfrak{J}^{2})$ is identified with the polynomial algebra $E = C[T_{1},
\cdots, T_{n}]$, where $n = rg_{C}(\mathfrak{J}/\mathfrak{J}^{2})$, and the augmentation ideal of $E$ is the ideal
$\mathfrak{n}$ generated by the $T_{i}$. For every integer $k \geq 0$, the hypothesis that $C$ is a formally smooth
discrete $A$-algebra entails, as in `(19.5.4.2)`, the existence of a surjective $A$-homomorphism $f :
E/\mathfrak{n}^{k+1} \to B/\mathfrak{J}^{k+1}$, such that $gr^{j}(f) = \phi_{j}$ for every $j \leq k$. If
$\mathfrak{b}/\mathfrak{n}^{k+1} = Ker(f)$, $B/\mathfrak{J}^{k+1}$ is thus identified with $E/\mathfrak{b}$, and the
hypothesis d) allows one to factor the canonical homomorphism $B \to B/\mathfrak{J}^{k+1}$ as $B \to
E/\mathfrak{n}^{k+1} \to B/\mathfrak{J}^{k+1}$; since $gr^{0}(f)$ is the identity, one has $w(\mathfrak{J}) \subset
\mathfrak{n}/\mathfrak{n}^{k+1}$, so $w(\mathfrak{J}^{k+1}) = 0$; one concludes as in `(19.5.4.2)` that $\phi_{k}$ is
injective for every $k$, which completes the proof of our assertion.

**(19.5.6)** *Proof of theorem `(19.5.3)`.* Let $(\mathfrak{b}_{\alpha})$ be a decreasing fundamental system of open
ideals of $B$. We shall set

```text
                              B_α = B/𝔟_α,        C_α = B/(𝔟_α + 𝔍),        𝔍_α = (𝔟_α + 𝔍)/𝔟_α,
```

so that

```text
                             C_α = B_α/𝔍_α,    and    𝔍_α^{n+1} = (𝔟_α + 𝔍^{n+1})/(𝔟_α + 𝔍^{n+1}).
```

The $C$-modules $((\mathfrak{b}_{\alpha} \cap \mathfrak{J}^{n}) + \mathfrak{J}^{n+1})/\mathfrak{J}^{n+1}$ of
$\mathfrak{J}^{n}/\mathfrak{J}^{n+1}$ form a fundamental system of open submodules of the topological $C$-module
$\mathfrak{J}^{n}/\mathfrak{J}^{n+1}$; since $(\mathfrak{b}_{\alpha} \cap \mathfrak{J}^{n}) + \mathfrak{J}^{n+1} =
\mathfrak{b}_{\alpha} \cap (\mathfrak{J}^{n} + \mathfrak{J}^{n+1})$, one has

```text
                   𝔍^n/((𝔟_α ∩ 𝔍^n) + 𝔍^{n+1}) = 𝔍^n/(𝔍^n ∩ (𝔟_α + 𝔍^{n+1})) = (𝔍^n + 𝔍^{n+1})/(𝔟_α + 𝔍^{n+1}) = 𝔍_α^n/𝔍_α^{n+1}.
```

**(19.5.6.1)** *Proof of `(19.5.3, (i))`.* Let $P$, $Q$ be two discrete $C_{\alpha}$-modules, $u : P \to Q$ a surjective
$C_{\alpha}$-homomorphism. The discrete ring $B/(\mathfrak{b}_{\alpha} + \mathfrak{J}^{2})$ is a $B$-extension of
$C_{\alpha}$ by the square-zero ideal $\mathfrak{J}_{\alpha}/\mathfrak{J}^{2}_{\alpha}$. Let $v :
\mathfrak{J}/\mathfrak{J}^{2} \to Q$ be a continuous $C$-homomorphism; replacing $\mathfrak{b}_{\alpha}$ if needed by a
smaller open ideal of $B$, one may suppose that the kernel of $v$ contains the open $C$-submodule
$((\mathfrak{b}_{\alpha} \cap \mathfrak{J}) + \mathfrak{J}^{2})/\mathfrak{J}^{2}$; passing to the quotient, one deduces
from $v$ a $C_{\alpha}$-homomorphism of discrete modules $v' : \mathfrak{J}_{\alpha}/\mathfrak{J}^{2}_{\alpha} \to Q$;
let $E_{\alpha}$ be the $B_{\alpha}$-extension of $C_{\alpha}$ by $Q$ deduced from $B/(\mathfrak{b}_{\alpha} +
\mathfrak{J}^{2})$ by means of $v'$, and let $h : B/(\mathfrak{b}_{\alpha} + \mathfrak{J}^{2}) \to E_{\alpha}$ be the
corresponding $B_{\alpha}$-homomorphism `(18.2.8)`; $E_{\alpha}$ is

<!-- original page 190 -->

a discrete topological $A$-algebra, and the canonical isomorphism $C_{\alpha} \xrightarrow{\sim} E_{\alpha}/Q$ gives by
composition a continuous $A$-homomorphism $f : C \to C_{\alpha} \to E_{\alpha}/Q$. But since $Q$ is of square zero in
$E_{\alpha}$ and $C$ is a formally smooth $A$-algebra, $f$ factors as $C \to E_{\alpha} \to E_{\alpha}/Q$, where $g$ is
a continuous $A$-homomorphism. Since $g$ is continuous and $E_{\alpha}$ discrete, there exists $\beta \geq \alpha$ such
that $g$ factors as $C \to C_{\beta} \to E_{\alpha}$. On the other hand, let $E_{\beta}$ be the $A$-extension of
$C_{\beta}$ by $Q$, inverse image of $E_{\alpha}$ under the canonical homomorphism $C_{\beta} \to C_{\alpha}$; the
existence of $g'$ (such that the composite $C_{\beta} \to E_{\beta} \to C_{\beta}$ is the canonical homomorphism) is
equivalent to the fact that $E_{\beta}$ is an $A$-trivial extension, and so can be identified with $D_{\beta}(Q)$. This
being so, the surjective homomorphism $u : P \to Q$ canonically defines a surjective homomorphism $D_{\beta}(P) \to
D_{\beta}(Q)$ `(18.2.9)`, whose kernel is an ideal $\mathfrak{S}$ of the extension $E'_{\beta} = D_{\beta}(P)$ contained
in $P$, and a fortiori of square zero. Let $h' : B \to E'_{\beta} = E_{\beta}/\mathfrak{S}$ be the continuous
$A$-homomorphism defining the topological $B$-algebra structure on $E_{\beta}$; since $\mathfrak{S}$ is of square zero
and $B$ is a formally smooth $A$-algebra, $h'$ factors as $B \to E'_{\beta} \to E_{\beta}/\mathfrak{S}$, where $h'$ is a
continuous $A$-homomorphism. The construction of $E_{\beta}$ gives by composition an $A$-homomorphism $t : E'_{\beta}
\to E_{\beta} \to E_{\alpha}$, and it is clear that the diagram

```text
                                                t
                                       E'_β ──────→ E_α
                                        │           ↑
                                      h'│           │ h
                                        ↓           │
                                        B ──────→ B/(𝔟_α + 𝔍²)
```

is commutative. Furthermore, the image under $t \circ h'$ of $\mathfrak{J}$ is contained in $Q$, so the image under $h'$
of $\mathfrak{J}$ is contained in $P$, and the image of $\mathfrak{J}^{2}$ under $h'$ is zero. Restricting $h'$ and $g'$
to $\mathfrak{J}$, one obtains a commutative diagram

```text
                                          u
                                       P ──→ Q
                                        ↖   ↗
                                          ↗
                                       𝔍/𝔍²
```

where $w$ is continuous, which proves that $\mathfrak{J}/\mathfrak{J}^{2}$ is a formally projective $C$-module.

**(19.5.6.2)** For every integer $n \geq 0$, we shall set

```text
                                E_n = B/𝔍^{n+1},                          so that E_0 = C;
```

the ideals $(\mathfrak{b}_{\alpha} + \mathfrak{J}^{n+1})/\mathfrak{J}^{n+1}$ form a fundamental system of open ideals in
$E_{n}$, and we shall set

```text
                                E_{α,n} = B/(𝔟_α + 𝔍^{n+1}) = E_n/(𝔟_α + 𝔍^{n+1})/𝔍^{n+1},
```

a discrete quotient ring. Likewise, in $gr^{n}_{\mathfrak{J}}(B) = \mathfrak{J}^{n}/\mathfrak{J}^{n+1}$, we have seen
that the $((\mathfrak{b}_{\alpha} \cap \mathfrak{J}^{n}) + \mathfrak{J}^{n+1})/\mathfrak{J}^{n+1}$ form a fundamental
system of neighbourhoods of `0`, the quotient of $\mathfrak{J}^{n}/\mathfrak{J}^{n+1}$ by this submodule being
canonically identified with $\mathfrak{J}^{n}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha}$. Consider the symmetric algebra
$S_{C}(\mathfrak{J}_{\alpha}/\mathfrak{J}^{2}_{\alpha})$; we denote by $F_{\alpha,n}$ the quotient of
$S_{C_{\alpha}}(\mathfrak{J}_{\alpha}/\mathfrak{J}^{2}_{\alpha})$ by the $(n+1)$-st power of its augmentation ideal. For
a fixed $n \geq 1$, it follows from `(19.5.1.1)` that the
$S^{n}_{C_{\alpha}}(\mathfrak{J}_{\alpha}/\mathfrak{J}^{2}_{\alpha})$ are the quotients of
$S^{n}_{C}(\mathfrak{J}/\mathfrak{J}^{2})$ by a fundamental system of open submodules in this topological $C$-module.

To abbreviate the language, we shall say that for $\alpha \leq \beta$, the canonical homomorphisms $B_{\beta} \to
B_{\alpha}$, $C_{\beta} \to C_{\alpha}$, $\mathfrak{J}_{\beta}/\mathfrak{J}^{2}_{\beta} \to
\mathfrak{J}_{\alpha}/\mathfrak{J}^{2}_{\alpha}$, $E_{\beta,n} \to E_{\alpha,n}$, $F_{\beta,n} \to F_{\alpha,n}$, etc.,
are the *transition homomorphisms*.

**Lemma (19.5.6.3).**

<!-- label: 0_IV.19.5.6.3 -->

*Suppose that the $A$-algebra $C$ is formally smooth, the ring $B$ preadmissible, and the $C$-module
$\mathfrak{J}/\mathfrak{J}^{2}$ formally projective. Then:*

*(i) For every $\alpha$, there exists $\beta \geq \alpha$ and a surjective $A$-homomorphism of algebras*

$$ \mathit{v}_{\alpha \beta} : F_{\beta,n} \to E_{\alpha,n} $$

*such that $gr^{0}(\mathit{v}_{\alpha \beta}) : C_{\beta} \to C_{\alpha}$ and $gr^{1}(\mathit{v}_{\alpha \beta}) :
\mathfrak{J}_{\beta}/\mathfrak{J}^{2}_{\beta} \to \mathfrak{J}_{\alpha}/\mathfrak{J}^{2}_{\alpha}$ are the transition
homomorphisms.*

*(ii) If $\beta \geq \alpha$ and $\mathit{v}_{\alpha \beta}$ satisfy the conditions of (i), then, for every $\gamma \geq
\beta$, there exists $\delta \geq \gamma$ and a surjective $A$-homomorphism of algebras $\mathit{v}_{\gamma \delta} :
F_{\delta,n} \to E_{\gamma,n}$ satisfying the conditions of (i) (for $\gamma \leq \delta$) and making the following
diagram commute*

```text
                                                 𝑣_{αβ}
                                       F_{β,n} ──────→ E_{α,n}
                                                                                     
(19.5.6.4)                                ↑              ↑
                                                                                     
                                       F_{δ,n} ──────→ E_{γ,n}
                                                 𝑣_{γδ}
```

*where the vertical arrows are the transition homomorphisms.*

(i) In the discrete topological $A$-algebra $E_{\alpha,n}$, the ideal
$\mathfrak{J}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha}$ is nilpotent, and the identity isomorphism $C_{\alpha} \to
E_{\alpha,n}/(\mathfrak{J}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha})$ gives by composition a continuous $A$-homomorphism $C
\to C_{\alpha} \to E_{\alpha,n}/(\mathfrak{J}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha})$;

<!-- original page 191 -->

since $C$ is a formally smooth $A$-algebra, this homomorphism factors as $C \to E_{\alpha,n} \to
E_{\alpha,n}/(\mathfrak{J}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha})$, where $f_{\alpha}$ is a continuous $A$-homomorphism;
consequently, $\mathfrak{J}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha}$ becomes, by means of $f_{\alpha}$, a discrete
topological $C$-module annihilated by an open ideal of $C$. The hypothesis that $\mathfrak{J}/\mathfrak{J}^{2}$ is a
formally projective $C$-module then entails the existence of a continuous $C$-linear map $g_{\alpha} :
\mathfrak{J}/\mathfrak{J}^{2} \to \mathfrak{J}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha}$ making commutative the diagram

```text
                                       𝔍_α/𝔍_α² ─→ 𝔍_α/𝔍_α^{n+1}
                                          ↑              ↑
                                          │            g_α
                                                
                                              𝔍/𝔍²
```

Since $f_{\alpha}$ and $g_{\alpha}$ are continuous, there exists $\beta \geq \alpha$ such that these homomorphisms
factor respectively as

$$ C \to C_{\beta} \to E_{\alpha,n} \mathfrak{J}/\mathfrak{J}^{2} \to \mathfrak{J}_{\beta}/\mathfrak{J}^{2}_{\beta} \to
\mathfrak{J}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha} $$

and from $f_{\alpha \beta}$ and $g_{\alpha \beta}$, one thus obtains canonically a homomorphism of $C_{\beta}$-algebras

$$ S_{C_{\beta}}(\mathfrak{J}_{\beta}/\mathfrak{J}^{2}_{\beta}) \to E_{\alpha,n} $$

which moreover (by definition of $g_{\alpha \beta}$) vanishes on the $(n+1)$-st power of the augmentation ideal of
$S_{C_{\beta}}(\mathfrak{J}_{\beta}/\mathfrak{J}^{2}_{\beta})$; passing to the quotient by this $(n+1)$-st power, one
obtains the desired homomorphism $\mathit{v}_{\alpha \beta}$, taking into account the definitions of $f_{\alpha \beta}$
and $g_{\alpha \beta}$; the surjectivity of $\mathit{v}_{\alpha \beta}$ follows in fact from that of the two
homomorphisms $gr^{0}(\mathit{v}_{\alpha \beta})$ and $gr^{1}(\mathit{v}_{\alpha \beta})$, since this entails that
$gr(\mathit{v}_{\alpha \beta})$ is surjective (the algebra $gr^{\bullet}(E_{\alpha,n})$ being generated by
$gr^{0}(E_{\alpha,n})$ and $gr^{1}(E_{\alpha,n})$), and since the filtrations considered are finite, one may apply
`Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1`.

(ii) The hypothesis that $B$ is preadmissible means that one may suppose all the $\mathfrak{b}_{\alpha}$ contained in a
single $\mathfrak{b}_{\alpha_{0}}$ whose powers tend to `0`. This entails in particular that the kernel of the
transition homomorphism $E_{\delta,n} \to E_{\gamma,n}$, equal to $(\mathfrak{b}_{\gamma} +
\mathfrak{J}^{n+1})/(\mathfrak{b}_{\delta} + \mathfrak{J}^{n+1})$, is nilpotent; applying lemma `(19.3.10.1)`, one sees
that one may suppose $f_{\gamma}$ chosen so that the diagram

```text
                                                f_γ
                                       C ──────────→ E_{γ,n}
                                       │             │
                                                     ↓
                                                 E_{α,n}
```

(where the vertical arrow is the transition homomorphism) is commutative. The hypothesis that
$\mathfrak{J}/\mathfrak{J}^{2}$ is a formally projective $C$-module on the other hand allows one to choose $g_{\gamma} :
\mathfrak{J}/\mathfrak{J}^{2} \to \mathfrak{J}_{\gamma}/\mathfrak{J}^{n+1}_{\gamma}$ so that the diagram

```text
                                        g_γ
                                𝔍_γ/𝔍_γ^{n+1} ────────────
                                       ↑                  │
                                                          ↓
                                       𝔍/𝔍²            𝔍_α/𝔍_α^{n+1}
                                          
                                                     g_α (∘ transition)
```

is commutative (it suffices to remark that the image of $(g_{\alpha}, p_{\gamma})$ of $\mathfrak{J}/\mathfrak{J}^{2}$ in
the product module $(\mathfrak{J}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha}) \times
(\mathfrak{J}_{\gamma}/\mathfrak{J}^{n+1}_{\gamma})$ is contained (in view of the definition of $g_{\alpha}$ and the
relation $\alpha \leq \gamma$) in the canonical image $Q$ in this product module of the

<!-- original page 192 -->

module $P = \mathfrak{J}_{\gamma}/\mathfrak{J}^{n+1}_{\gamma}$, and to apply the definition `(19.2.1)` to the surjective
homomorphism $P \to Q$ and to the homomorphism $(g_{\alpha}, p_{\gamma})$ of $\mathfrak{J}/\mathfrak{J}^{2}$ into $Q$).
This choice of $f_{\gamma}$ and $g_{\gamma}$ then allows one, by constructing $\mathit{v}_{\gamma \delta}$ as in (i), to
obtain in addition the commutativity of the diagram `(19.5.6.4)`.

**Lemma (19.5.6.5).**

<!-- label: 0_IV.19.5.6.5 -->

*Suppose that the $A$-algebras $B$ and $C$ are formally smooth and $B$ is preadmissible (so that by virtue of
`(19.5.6.1)` the conditions of `(19.5.6.3)` are satisfied). For every system of two indices $\alpha \leq \beta$ and a
homomorphism $\mathit{v}_{\alpha \beta}$ satisfying the conditions of `(19.5.6.3, (i))`, there exists an index $\lambda
\geq \beta$ and an $A$-homomorphism of algebras*

$$ w_{\beta \lambda} : E_{\lambda,n} \to F_{\beta,n} $$

*such that: 1° $gr^{0}(w_{\beta \lambda}) : C_{\lambda} \to C_{\beta}$ and $gr^{1}(w_{\beta \lambda}) :
\mathfrak{J}_{\lambda}/\mathfrak{J}^{2}_{\lambda} \to \mathfrak{J}_{\beta}/\mathfrak{J}^{2}_{\beta}$ are the transition
homomorphisms; 2° the composite $E_{\lambda,n} \to F_{\beta,n} \to E_{\alpha,n}$ is the transition homomorphism.*

Apply lemma `(19.5.6.3, (ii))` with $\gamma = \beta$, which gives a $\delta \geq \beta$ and a
$\mathit{v}_{\beta \delta} : F_{\delta,n} \to E_{\beta,n}$. Recall that $\mathit{v}_{\beta \delta}$ is surjective; on
the other hand, its kernel $\mathfrak{N}$ is nilpotent: indeed, the augmentation ideal $F^{+}_{\delta,n}$ of
$F_{\delta,n}$ is nilpotent by definition, and the kernel of
$gr^{0}(\mathit{v}_{\beta \delta}) : C_{\delta} \to C_{\beta}$ is also nilpotent by virtue of the hypothesis that $B$ is
preadmissible. One thus sees that $E_{\beta,n}$ is identified with $F_{\delta,n}/\mathfrak{N}$. Since $B$ is a formally
smooth $A$-algebra, the canonical $A$-homomorphism $p_{\beta} : B \to E_{\beta,n}$, which is continuous, factors as
$B \to F_{\delta,n} \to E_{\beta,n}$, where $w$ is a continuous $A$-homomorphism. Since $F_{\delta,n}$ is discrete,
there exists $\lambda \geq \delta$ such that $w$ is zero on $\mathfrak{b}_{\lambda}$, so $w$ factors as
$B \to B/\mathfrak{b}_{\lambda} \to F_{\delta,n}$. Consider the composite homomorphism
$w^{*}_{\beta \lambda} : B/\mathfrak{b}_{\lambda} \to F_{\delta,n} \to F_{\beta,n}$, where $q_{\beta \delta}$ is the
transition homomorphism; note that
$gr^{0}(q_{\beta \delta}) = gr^{0}(\mathit{v}_{\beta \delta}) : C_{\delta} \to C_{\beta}$ is the transition
homomorphism; since the composite $q_{\beta \delta} \circ w$ is the canonical homomorphism
$B/\mathfrak{b}_{\lambda} \to B/(\mathfrak{b}_{\beta} + \mathfrak{J}^{n+1})$, this shows that the image of
$(\mathfrak{b}_{\lambda} + \mathfrak{J})/\mathfrak{b}_{\lambda}$ under $w^{*}_{\beta \lambda}$ is contained in the
augmentation ideal $F^{+}_{\beta,n}$, and consequently the image under $w^{*}_{\beta \lambda}$ of
$\mathfrak{J}^{n+1}_{\lambda} = (\mathfrak{b}_{\lambda} + \mathfrak{J}^{n+1})/\mathfrak{b}_{\lambda}$ is zero. In other
words, $w^{*}_{\beta \lambda}$ factors as

```text
                                  B/𝔟_λ → B/(𝔟_λ + 𝔍^{n+1}) = E_{λ,n} → F_{β,n}
                            w_{βλ}^*        w_{βλ}
```

such that the composite $E_{\lambda,n} \to F_{\beta,n} \to E_{\alpha,n}$ is the transition homomorphism. The preceding
reasoning also shows that $gr^{0}(w_{\beta \lambda})$, which is the composite $B/(\mathfrak{b}_{\lambda} + \mathfrak{J})
\to gr^{0}(F_{\delta,n}) \to gr^{0}(F_{\beta,n})$, is the transition homomorphism $C_{\lambda} \to C_{\beta}$, since
$q_{\beta \delta} \circ w_{\beta \lambda}$ is the canonical homomorphism. In addition, one also has $gr^{1}(w_{\beta
\lambda}) = gr^{1}(w_{\beta \delta})$ (where $w_{\beta \delta} = q_{\beta \delta} \circ w$), so the same reasoning
proves that $gr^{1}(w_{\beta \lambda})$ is the transition homomorphism.

**(19.5.6.6)** *Proof of `(19.5.3, (ii))`.* To show that $\phi_{n}$ is a formal bimorphism, we shall apply the criterion
of `(19.1.3, (iii))`. The conditions of `(19.5.6.5)` being satisfied by hypothesis, let us determine, for every index
$\alpha$, $\mathit{v}_{\alpha \beta}$ and $w_{\beta \lambda}$ satisfying the conclusions of this lemma. The homomorphism

$$ gr^{n}(\mathit{v}_{\alpha \beta}) : gr^{n}(F_{\beta,n}) \to gr^{n}(E_{\alpha,n}) $$

is none other than the homomorphism

$$ \phi_{\alpha \beta,n} : S^{n}_{C}(\mathfrak{J}_{\beta}/\mathfrak{J}^{2}_{\beta}) \to
\mathfrak{J}^{n}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha} $$

deduced from the canonical homomorphism $\phi_{n}$ `(19.5.2.1)` by passage to the quotients; indeed, it follows from
`(19.5.6.3)` that $gr^{0}(\mathit{v}_{\alpha \beta})$ and $gr^{1}(\mathit{v}_{\alpha \beta})$ coincide respectively with
$\phi_{\alpha \beta,0}$ and $\phi_{\alpha \beta,1}$, and the definition of the canonical homomorphism $\phi$ then shows,
by recurrence on $j \leq n$, that $gr^{j}(\mathit{v}_{\alpha \beta})$ and $\phi_{\alpha \beta,j}$ are equal for every
$j$. This being so, since $\mathit{v}_{\alpha \beta}$ is surjective, it is *a fortiori* a formal epimorphism; in
addition, for $j \leq n$, the composite homomorphism

$$ gr^{j}(F_{\beta,n}) \to gr^{j}(E_{\alpha,n}) \to gr^{j}(F_{\alpha,n}) $$

is the transition homomorphism, for this is true for $j = 0$ and $j = 1$ by virtue of `(19.5.6.5)`, and since
$gr^{\bullet}(E_{\alpha,n})$ is generated by $gr^{1}(E_{\alpha,n})$ this proves the assertion by recurrence on $j$.
Composing with the transition homomorphism $gr^{j}(F_{\beta,n}) \to gr^{j}(F_{\alpha,n})$, one thus sees, for $j = n$,
that one has factored the transition homomorphism $gr^{n}(F_{\beta,n}) \to gr^{n}(F_{\alpha,n})$ as

$$ \phi_{\alpha \beta,n} S^{n}_{C}(\mathfrak{J}_{\beta}/\mathfrak{J}^{2}_{\beta}) \to
\mathfrak{J}^{n}_{\alpha}/\mathfrak{J}^{n+1}_{\alpha} \to gr^{n}(F_{\alpha,n}) $$

which is the condition of the criterion `(19.1.3)` for $\phi_{n}$ to be a formal bimorphism.

<!-- original page 193 -->

**Lemma (19.5.6.7).**

<!-- label: 0_IV.19.5.6.7 -->

*Suppose that $B$ is preadmissible, that $\mathfrak{J}/\mathfrak{J}^{2}$ is a formally projective $C$-module, that $C$
is a formally smooth $A$-algebra, and that the $\phi_{n}$ are formal bimorphisms. Then, for every pair of indices
$\alpha \leq \beta$ and every homomorphism $\mathit{v}_{\alpha \beta} : F_{\beta,n} \to E_{\alpha,n}$ satisfying the
conditions of `(19.5.6.3, (i))`, there exists an index $\gamma \geq \beta$ such that, for every index $\mu \geq \gamma$,
one has a commutative diagram of $A$-homomorphisms*

```text
                                                  𝑣_{αβ}
                                       F_{β,n} ──────→ E_{α,n}
                                          ↑              ↑
                                                       
                                       F_{μ,n} ←────── E_{μ,n}
                                                u_{αμ}
```

*where $p_{\alpha \mu}$ is the transition homomorphism.*

Applying the criterion `(19.1.3)` to each of the $\phi_{j}$ for $0 \leq j \leq n$, one sees that there exists an index
$\gamma \geq \beta$ and uniquely determined (and surjective) homomorphisms of $C_{\gamma}$-modules

$$ w_{n} : gr^{n}(E_{\gamma,n}) \to gr^{n}(F_{\beta,n}) $$

such that the composites

```text
                                                 φ_{γγ,n}        w_n
                                        gr^n(F_{γ,n}) ──────→ gr^n(E_{γ,n}) ──────→ gr^n(F_{β,n})
```

are the transition homomorphisms (the fact that one can choose the same index $\gamma$ for all the $w_{j}$ results from
the fact that they are finite in number). Furthermore, the uniqueness of the $w_{n}$ proves (since $\phi$ is a
homomorphism of graded algebras) that $w_{\bullet} = (\phi_{\gamma \gamma})^{-1} \circ w^{*}_{\bullet}$ is a
homomorphism of $C_{\gamma}$-algebras $gr^{\bullet}(E_{\gamma,n}) \to gr^{\bullet}(F_{\beta,n}) = F_{\beta,n}$. In
addition, since $\phi_{\gamma \gamma,0}$ and $\phi_{\gamma \gamma,1}$ are the identity homomorphisms, $w_{0} :
C_{\gamma} \to C_{\beta}$ and $w_{1} : \mathfrak{J}_{\gamma}/\mathfrak{J}^{2}_{\gamma} \to
\mathfrak{J}_{\beta}/\mathfrak{J}^{2}_{\beta}$ are the transition homomorphisms, and the same is therefore true of
$gr^{0}(\mathit{v}_{\alpha \beta} \circ w_{\bullet})$ and $gr^{1}(\mathit{v}_{\alpha \beta} \circ w_{\bullet})$; since
$gr^{\bullet}(E_{\gamma,n})$ is generated by $gr^{1}(E_{\gamma,n})$, one concludes that $gr^{j}(\mathit{v}_{\alpha
\beta} \circ w_{\bullet})$ is also the transition homomorphism for $0 \leq j \leq n$. Applying now to $\alpha$, $\beta$
and $\gamma$ the lemma `(19.5.6.3, (ii))`, this gives the diagram `(19.5.6.4)` with $\delta \geq \gamma$; then repeat
the reasoning of the beginning by replacing $\alpha$ and $\beta$ by $\gamma$ and $\delta$. One thus obtains an index
$\lambda \geq \delta$ and a commutative diagram of homomorphisms

```text
                                                w_•           𝑣_{γδ}
                                       gr^•(E_{γ,n}) ──→ F_{δ,n} ──→ E_{γ,n}
                                              ↑           ↑           ↑
                                                                      
                                              ↑          q_{βδ}       │ p_{αγ}
                                       gr^•(E_{λ,n}) ──→ F_{λ,n} ──→ E_{λ,n}
```

where the vertical arrows are the transition homomorphisms. Everything boils down to proving the existence of the
homomorphism $u_{\alpha \mu}$ leaving the diagram commutative, and for this it is obviously enough to show that one has
$Ker(\mathit{v}_{\gamma \delta}) \subset Ker(q_{\beta \delta})$, $\mathit{v}_{\gamma \delta}$ and $q_{\beta \delta}$
being surjective. Since $w_{\bullet}$ is surjective, this last relation is equivalent to
`Ker(𝑣_{γδ} ∘ w_•) ⊂ Ker(q_{βδ} ∘ w_•) = Ker(w_{βλ} ∘ (gr(p_{γλ})))`. But it was seen above that $gr(p_{\gamma \lambda})
= gr(\mathit{v}_{\gamma \delta} \circ w_{\bullet})$ and it is clear that
`Ker(𝑣_{γδ} ∘ w_{δμ}) ⊂ Ker(gr(𝑣_{γδ} ∘ w_{δμ})) = Ker(gr(p_{γλ})) ⊂ Ker(w_{βλ} ∘ (gr(p_{γλ})))`, which completes the
proof of the lemma, for any $\mu \geq \gamma$, it will suffice to define $u_{\alpha \mu}$ as the composite $E_{\mu,n}
\to E_{\gamma,n} \to F_{\beta,n}$.

**(19.5.6.8)** *Proof of `(19.5.3, (iii))`.* Let $G$ be a discrete topological $A$-algebra, $\mathfrak{N}$ an ideal of
square zero in $G$, $f : B \to G/\mathfrak{N}$ a continuous $A$-homomorphism of algebras. Since $G/\mathfrak{N}$ is
discrete, there is an index $\alpha$ such that $f$ vanishes on $\mathfrak{b}_{\alpha}$; by hypothesis, there exists an
integer $m$ such that $\mathfrak{J}^{m} \subset \mathfrak{b}_{\alpha}$, so $f$ factors as

```text
                                                        p_α
                                              B ──────→ E_{α,n} ──────→ G/𝔑
                                                         f_α
```

where one takes $n = 2m$. The hypotheses of lemma `(19.5.6.3)` being satisfied, one has first of all a $\beta \geq
\alpha$ and a composite $A$-homomorphism

```text
(19.5.6.9)                                  f_{α,n} ∘ 𝑣_{αβ} : F_{β,n} → E_{α,n} → G/𝔑
```

and since $F_{\beta,n}$ is a $C_{\beta}$-algebra, hence *a fortiori* a topological (discrete) $C$-algebra, this gives by
composition a continuous $A$-homomorphism $r : C \to F_{\beta,n} \to G/\mathfrak{N}$. Since on the other hand $C$ is a
formally smooth $A$-algebra,

<!-- original page 194 -->

this homomorphism factors as $r : C \to G \to G/\mathfrak{N}$ where $r'$ is a continuous $A$-homomorphism, so that $G$
is thus endowed with a structure of topological (discrete) $C$-algebra. On the other hand, by composition with the
canonical homomorphism

$$ \mathfrak{J}/\mathfrak{J}^{2} \to \mathfrak{J}_{\beta}/\mathfrak{J}^{2}_{\beta} \to F_{\beta,n} $$

one deduces from `(19.5.6.9)` a continuous $C$-homomorphism $g : \mathfrak{J}/\mathfrak{J}^{2} \to G/\mathfrak{N}$.
Since $\mathfrak{J}/\mathfrak{J}^{2}$ is a formally projective $C$-module, $g$ factors as $\mathfrak{J}/\mathfrak{J}^{2}
\to G \to G/\mathfrak{N}$, where $h$ is a continuous $C$-homomorphism. Since $G$ is discrete, there exists an index
$\gamma \geq \beta$ such that the image under $h$ of $((\mathfrak{b}_{\gamma} \cap \mathfrak{J}) +
\mathfrak{J}^{2})/\mathfrak{J}^{2}$ is zero, as is the image under $h$ of $(\mathfrak{b}_{\gamma} +
\mathfrak{J}^{2})/\mathfrak{J}^{2}$, so that $h$ factors as

$$ \mathfrak{J}/\mathfrak{J}^{2} \to \mathfrak{J}_{\gamma}/\mathfrak{J}^{2}_{\gamma} \to G $$

where $h'$ is a $C_{\gamma}$-homomorphism. By extension, one therefore deduces from $h'$ a homomorphism of
$C_{\gamma}$-algebras

$$ w : S_{C_{\gamma}}(\mathfrak{J}_{\gamma}/\mathfrak{J}^{2}_{\gamma}) \to G $$

and by construction, every element of degree $m$ has under $w$ an image which is an element of $\mathfrak{N}$, so every
element of degree $n = 2m$ has image zero, since $\mathfrak{N}^{2} = 0$; in other words, $w$ factors as

$$ S_{C_{\gamma}}(\mathfrak{J}_{\gamma}/\mathfrak{J}^{2}_{\gamma}) \to F_{\gamma,n} \to G. w_{\alpha \gamma} $$

Apply now to $\mathit{v}_{\alpha \gamma} : F_{\gamma,n} \to F_{\beta,n} \to E_{\alpha,n}$ the lemma `(19.5.6.7)`, whose
hypotheses are verified; there exists thus a $\delta \geq \gamma$ and a homomorphism $u_{\alpha \delta} : E_{\delta,n}
\to F_{\gamma,n}$ such that the composite $\mathit{v}_{\alpha \gamma} \circ u_{\alpha \delta}$ is the transition
homomorphism $p_{\alpha \delta} : E_{\delta,n} \to E_{\alpha,n}$. One finally obtains a commutative diagram of
continuous $A$-homomorphisms

```text
                                       B ──→ E_{δ,n} ──→ F_{γ,n} ──→ G ──→ G/𝔑
                                                 u_{αδ}      w_{αγ}
```

and the composite $f : B \to G$ of the homomorphisms of the lower line is such that $f$ factors as $B \to G \to
G/\mathfrak{N}$, which proves that $B$ is a formally smooth $A$-algebra.

The proof of theorem `(19.5.3)` is thus complete.

**Corollary (19.5.7).**

<!-- label: 0_IV.19.5.7 -->

*Let $A$ be a topological ring, $B$ a topological $A$-algebra, $(\mathfrak{b}_{\lambda})$ a fundamental system of open
ideals in $B$, $\mathfrak{J}$ an ideal of $B$, $C = B/\mathfrak{J}$ the quotient topological $A$-algebra. Set
$C_{\lambda} = B/(\mathfrak{b}_{\lambda} + \mathfrak{J})$. Assume that: 1° for every $n$, the topology induced on
$\mathfrak{J}^{n}$ by that of $B$ is also the topology of the $C$-module $\mathfrak{J}^{n}$ deduced from the topology of
$C$ `(19.0.2)` (this condition will be satisfied in particular if $B$ is Noetherian and its topology preadic $(0_{I},
7.3.2)$); 2° $C$ is a formally smooth $A$-algebra. Under these conditions:*

*(i) If $B$ is a formally smooth $A$-algebra, then, for every $\lambda$, $(\mathfrak{J}/\mathfrak{J}^{2}) \otimes_{C}
C_{\lambda}$ is a projective $C_{\lambda}$-module.*

*(ii) If $B$ is a formally smooth $A$-algebra and a preadmissible ring, then for every $\lambda$, the canonical
homomorphism*

```text
(19.5.7.1)                    φ_λ = φ ⊗ 1_{C_λ} : S_C(𝔍/𝔍²) ⊗_C C_λ → gr^•_𝔍(B) ⊗_C C_λ
```

*is bijective.*

<!-- original page 195 -->

*(iii) Conversely, suppose that $B$ is preadmissible, that the sequence $(\mathfrak{J}^{n})$ tends to `0`, and that, for
every $\lambda$, $(\mathfrak{J}/\mathfrak{J}^{2}) \otimes_{C} C_{\lambda}$ is a projective $C_{\lambda}$-module and the
homomorphism `(19.5.4.1)` is bijective. Then $B$ is a formally smooth $A$-algebra.*

Indeed, the topology of $\mathfrak{J}/\mathfrak{J}^{2}$ and that of the $S_{C}(\mathfrak{J}/\mathfrak{J}^{2})$ are then
also deduced from that of $B$ `(19.5.1)`; the conclusions then follow immediately from `(19.5.3)` and from the criteria
of `(19.1.4)` and `(19.2.4)` specific to this type of topologies.

**Remark (19.5.8).**

<!-- label: 0_IV.19.5.8 -->

*Suppose that $\mathfrak{J}/\mathfrak{J}^{2}$ is a $C$-module of finite type and that, for the quotient topology from
that of $B$, $C$ is a Zariski ring; let $\mathfrak{r}$ be an ideal of definition of $C$, so that the $\mathfrak{r}^{n}$
form a fundamental system of neighbourhoods of `0` in $C$. Then the conclusions of (i) and (ii) in `(19.5.7)` can be
replaced by the following:*

*(i') $\mathfrak{J}/\mathfrak{J}^{2}$ is a projective $C$-module.*

*(ii') The canonical homomorphism $\phi : S_{C}(\mathfrak{J}/\mathfrak{J}^{2}) \to gr^{\bullet}_{\mathfrak{J}}(B)$ is
bijective.*

Indeed, it is clear that (i') implies the conclusion of (i) in `(19.5.7)`. Conversely, if
$(\mathfrak{J}/\mathfrak{J}^{2}) \otimes_{C} C_{\lambda}$ is a projective $C_{\lambda}$-module for every $\lambda$, then
$(\mathfrak{J}/\mathfrak{J}^{2}) \otimes_{C} (C/\mathfrak{r}^{n})$ is a $(C/\mathfrak{r}^{n})$-module that is projective
(hence flat) for every $n$; one concludes that $\mathfrak{J}/\mathfrak{J}^{2}$ is a flat $C$-module $(0_{III}, 10.2.2)$,
hence projective since it is of finite presentation `(Bourbaki, Alg. comm., chap. II, §5, n° 2, cor. 2 of th. 1)`. On
the other hand, the $C$-modules $S_{C}(\mathfrak{J}/\mathfrak{J}^{2})$ and $gr^{\bullet}_{\mathfrak{J}}(B)$ are of
finite type, and one knows that when $C$ is a Zariski ring, it amounts to the same thing to say that $\phi_{n}$ is
bijective or that $\phi_{\lambda}$ is bijective `(Bourbaki, Alg. comm., chap. III, §3, n° 5, prop. 9)`, hence (ii) is
equivalent to (ii').

### 19.6. Case of algebras over a field

**Theorem (19.6.1) (Cohen).**

<!-- label: 0_IV.19.6.1 -->

*Let $k$ be a field, $K$ an extension of $k$, $k$ and $K$ being endowed with the discrete topologies. For $K$ to be a
formally smooth $k$-algebra, it is necessary and sufficient that $K$ be a separable extension of $k$.*

The necessity of the condition will be established in `(19.6.5.1)` (and naturally will not be used until then); we shall
confine ourselves here to proving that the condition is sufficient. Let us distinguish two cases:

I. — *$K$ is a separable extension of finite type of $k$.* One then knows `(Bourbaki, Alg., chap. V, §9, n° 3, th. 2)`
that there exists a pure subextension $K' = k(T_{1}, \cdots, T_{n})$ of $K$ such that $K$ is a finite separable
algebraic extension of $K'$. Taking `(19.3.5, (ii))` into account, one may therefore restrict to the case where $K = K'$
or to the case where $K$ is finite algebraic over $k$. In the first case, one knows that $A = k[T_{1}, \cdots, T_{n}]$
is a formally smooth $k$-algebra `(19.3.3)`, and so is $k(T_{1}, \cdots, T_{n}) = S^{-1}A$, where $S = A - {0}$
`(19.3.5, (iv))`. In the second case, all the Hochschild cohomology groups $H^{i}(K, L)$ for an arbitrary $(K,
K)$-bimodule $L$ are zero: indeed, if one considers the $k$-algebra tensor product $C = K \otimes_{k} K$, $L$ is a left
$C$-module and the cohomology group $H^{i}(K, L)$ is equal to $Ext^{i}_{C}(K, L)$, where $K$ is also considered as a
$(K, K)$-bimodule,

<!-- original page 196 -->

hence as a left $C$-module `(M, IX, 4)`. Now, since $K$ is a finite separable extension of $k$, one knows that $K
\otimes_{k} K$ is a direct composite of extensions of $k$, one of which is $K$ itself
`(Bourbaki, Alg., chap. VIII, §8, prop. 3)`; this therefore entails that $K$ is a projective $C$-module, whence our
assertion. Every $k$-extension of $K$ with kernel $L$ is therefore $k$-trivial, and *a fortiori* the commutative
$k$-extensions are, whence the theorem in this case `(19.4.4)`.

II. — *General case.* — With the notation of `(18.4.5)`, the question is to prove that
$\operatorname{Hom}_{K}(H^{2}(P^{K}_{\bullet}), L) = 0$ for every $K$-vector space $L$, which evidently means that
$H^{2}(P^{K}_{\bullet}) = 0$. If $K$ is the union of a filtered family of subextensions $K_{\alpha}$ of $k$,
$P^{K}_{\bullet}$ is the inductive limit of the corresponding complexes $P^{K_{\alpha}}_{\bullet}$, since the functor
`lim` commutes with the tensor product in the category of $k$-modules; by the exactness of the functor `lim` in this
category, one therefore has $H^{2}(P^{K}_{\bullet}) = \lim H^{2}(P^{K_{\alpha}}_{\bullet})$. Since the hypothesis that
$K$ is separable entails that the same is true of every subextension of $K$, and since $K$ is the union of subextensions
of finite type, the first part of the proof entails indeed that $K$ is a formally smooth $k$-algebra. Q.E.D.

**Corollary (19.6.2).**

<!-- label: 0_IV.19.6.2 -->

*Let $A$ be a separated and complete local ring, $K$ its residue field, $k$ a subfield of $K$ such that $K$ is a
separable extension of $k$. Then there exists a subfield $K'$ of $A$ containing $k$, such that the restriction to $K'$
of the canonical homomorphism $A \to K$ is an isomorphism of $K'$ onto $K$.*

Let $\mathfrak{m}$ be the maximal ideal of $A$. By virtue of the hypothesis and of `(19.6.1)`, $K$ is a formally smooth
$k$-algebra; applying `(19.3.10)` with $C$ replaced by $k$ and $\mathfrak{J}$ by $\mathfrak{m}$, one sees that the
identity automorphism of $K = A/\mathfrak{m}$ factors as $K \to A \to A/\mathfrak{m}$, where $f$ is a $k$-homomorphism,
hence necessarily a $k$-isomorphism of $K$ onto a subfield $K'$ containing $k$.

**Corollary (19.6.3).**

<!-- label: 0_IV.19.6.3 -->

*Let $A$ be a complete Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $k$ its residue field. The following
conditions are equivalent:*

*a) $A$ contains a subfield.*

*b) If $p$ is the characteristic of $k$, one has $pA = 0$.*

*c) There exists a field $K$ such that $A$ is isomorphic to a quotient ring of a formal power series ring $B = K[[T_{1},
\cdots, T_{n}]]$.*

*When this is the case, one may assume that $A$ is isomorphic to $B/\mathfrak{b}$, where $\mathfrak{b}$ is contained in
the square of the maximal ideal of $B$.*

It is immediate that c) implies a), for $A \neq 0$ since it is a local ring; since $K$ is a field and the composite
homomorphism $K \to B \to A$ (where $\phi$ is the canonical injection) is not zero, it is injective. To see that a)
implies b), it suffices to remark that if $k'$ is a subfield of $A$, $k'$ is isomorphic to a subfield of $k$ and has
therefore the same characteristic $p$; since $p \cdot 1 = 0$ in $k'$, hence in $A$, one has $pA = 0$. Conversely, b)
implies a), for the composite of the canonical homomorphisms $\mathbb{Z} \to A \to A$ has kernel $p\mathbb{Z}$, and one
has $f(p\mathbb{Z}) = 0$, hence $Ker(f) = p\mathbb{Z}$ and $A$ contains a ring $A'$ isomorphic to
$\mathbb{Z}/p\mathbb{Z}$ and not meeting $\mathfrak{m}$; if $p > 0$, $A'$ is a field; otherwise, every

<!-- original page 197 -->

element of $A'$ being invertible in $A$, the field of fractions of $A'$ (isomorphic to $\mathbb{Q}$) is also contained
in $A$.

Let us prove finally that a) implies c): condition a) entails that $A$ contains a prime subfield $k_{0}$, isomorphic to
the prime subfield of $k$, and of which $k$ is therefore a separable extension. Applying `(19.6.2)`, one sees first that
there exists an isomorphism $f$ of $k$ onto a subfield $K$ of $A$. On the other hand, let $(x_{i})_{1 \leq i \leq n}$ be
a system of elements of $\mathfrak{m}$ such that the classes mod $\mathfrak{m}^{2}$ of the $x_{i}$ form a basis (over
$k$) of $\mathfrak{m}/\mathfrak{m}^{2}$. Since $A$ is complete, there is then a continuous ring homomorphism $u :
k[[T_{1}, \cdots, T_{n}]] \to A$ such that $u$ is equal to $f$ on $k$ and $u(T_{i}) = x_{i}$ for every $i$, and this
homomorphism is surjective by virtue of the choice of the $x_{i}$
`(Bourbaki, Alg. comm., chap. III, §2, n° 9, prop. 11)`.

**Theorem (19.6.4).**

<!-- label: 0_IV.19.6.4 -->

*Let $k$ be a field, $A$ a Noetherian local $k$-algebra, $\mathfrak{m}$ its maximal ideal, $K = A/\mathfrak{m}$ its
residue field, $A$ being endowed with the $\mathfrak{m}$-preadic topology. Assume that $K$ is a separable extension of
$k$. Then the following conditions are equivalent:*

*a) $A$ is a formally smooth $k$-algebra.*

*b) The completion `Â` of $A$ is $k$-isomorphic to a formal power series ring $K[[T_{1}, \cdots, T_{n}]]$ (whose
$k$-algebra structure is defined by the composite homomorphism*

```text
                                    k → K → K[[T_1, …, T_n]],
```

*where $\psi$ is the canonical injection and $\phi$ the homomorphism defining the extension structure of $K$).*

*b') `Â` is a ring isomorphic to a formal power series ring $K[[T_{1}, \cdots, T_{n}]]$.*

*c) $A$ is a regular local ring.*

The fact that a) implies b) is the special case of (`(19.5.4)`, equivalence of a) and c)), applied by replacing $A$
there by $k$, $B$ by $A$ and $\mathfrak{J}$ by $\mathfrak{m}$, taking into account `(19.6.1)`. It is clear that b)
implies b') and b') implies c) by `(17.1.1)`. Finally, if c) is verified, it follows from `(17.1.1, e)` and from
(`(19.5.4)`, equivalence of b) and a)), applied with $K = A/\mathfrak{m}$ replacing $C$, that $A$ is a formally smooth
$k$-algebra.

**Corollary (19.6.5).**

<!-- label: 0_IV.19.6.5 -->

*Let $k$ be a field, $A$ a Noetherian local $k$-algebra, $\mathfrak{m}$ its maximal ideal, $A$ being endowed with the
$\mathfrak{m}$-preadic topology. Suppose that $A$ is a formally smooth $k$-algebra; then $A$ is geometrically regular
over $k$, in other words (cf. `(IV, 6.7.6)`), for every finite extension $k'$ of $k$, the semi-local ring $A' = A
\otimes_{k} k'$ is regular `(17.3.6)`. Furthermore, if $K$ is the residue field of $A$, `Â` is isomorphic to a formal
power series ring $K[[T_{1}, \cdots, T_{n}]]$.*

Since $\hat{A}' = \hat{A} \otimes_{k} k'$, it follows from `(19.3.6)` and from `(17.1.5)` (applied to the local rings at
the maximal ideals of $A'$) that one may restrict to the case where $A$ is complete; then $A'$ is a formally smooth
$k'$-algebra `(19.3.5, (iii))` and is moreover a direct composite of local $k'$-algebras, which are also formally smooth
`(19.3.5, (v))`. One is therefore reduced to proving that $A$ is regular. Let $k_{0}$ be the prime subfield of $k$;
since $k$ is a separable extension of $k_{0}$, it is a formally smooth $k_{0}$-algebra `(19.6.1)` and by virtue of the
hypothesis, the same is true of $A$ `(19.3.5, (ii))`. Since the residue field $K$ of $A$ is a separable extension of
$k_{0}$, one may then apply `(19.6.4)` to $A$ and $k_{0}$, whence the conclusion.

<!-- original page 198 -->

**Corollary (19.6.5.1).**

<!-- label: 0_IV.19.6.5.1 -->

*Let $A$ be a Noetherian local ring, $k$ a subfield of $A$ such that $A$ is a formally smooth $k$-algebra (for its
preadic topology). Then every field $K$ such that $k \subset K \subset A$ is a separable extension of $k$.*

Indeed, for every finite extension $k'$ of $k$, the ring $K \otimes_{k} k'$ is identified with a subring of $A' = A
\otimes_{k} k'$; since $A'$ is a regular ring, it is reduced, hence so is $K \otimes_{k} k'$, which proves that $K$ is a
separable extension of $k$ `(Bourbaki, Alg., chap. VIII, §7, n° 3, th. 1)`.

Note that this proves that the condition of the statement of `(19.6.1)` is necessary.

**Remark (19.6.5.2).**

<!-- label: 0_IV.19.6.5.2 -->

*If $K$ is a non-separable extension of $k$, the formal power series ring $K[[T_{1}, \cdots, T_{n}]]$ is therefore not a
formally smooth $k$-algebra (for the usual $k$-algebra structure recalled in `(19.6.4)`). On the other hand, there are
formally smooth $k$-algebras $A$ which are complete Noetherian local rings whose residue field $K$ is a non-separable
extension of $k$ (for example, the completions of the localizations of $B = k[T_{1}, \cdots, T_{n}]$ at maximal ideals
$\mathfrak{n}$ such that $B/\mathfrak{n}$ is a finite non-separable algebraic extension of $k$); such a ring cannot
therefore be $k$-isomorphic to $K[[T_{1}, \cdots, T_{n}]]$, although it is isomorphic to it by virtue of `(19.6.5)`.*

In certain cases one can sharpen corollary `(19.6.5)`:

**Proposition (19.6.6).**

<!-- label: 0_IV.19.6.6 -->

*Let $k$ be a field, $A$ a Noetherian local $k$-algebra, $\mathfrak{m}$ its maximal ideal, $A$ being endowed with the
$\mathfrak{m}$-preadic topology. Suppose that the residue field $K = A/\mathfrak{m}$ of $A$ is such that there exists a
finite radicial extension $k_{0}$ of $k$ for which the residue field of the local ring $K \otimes_{k} k_{0}$ is a
separable extension of $k_{0}$ (we shall later express this property by saying that $K$ is of finite radicial
multiplicity over $k$ `(IV, 4.7.4)` and we shall see that this condition is always satisfied when $K$ is a finitely
generated extension of $k$). Then the following conditions are equivalent:*

*a) $A$ is a formally smooth $k$-algebra.*

*b) There exists a finite radicial extension $k'$ of $k$ such that $\hat{A} \otimes_{k} k'$ is $k'$-isomorphic to a
formal power series algebra $K'[[T_{1}, \cdots, T_{n}]]$, where $K'$ is a separable extension of $k'$.*

*b') There exists a finite extension $k'$ of $k$ such that the semi-local ring $\hat{A} \otimes_{k} k'$ has at least one
local ring component which is $k'$-isomorphic to a formal power series algebra $K'[[T_{1}, \cdots, T_{n}]]$, where $K'$
is a separable extension of $k'$.*

*c) $A$ is geometrically regular over $k$ `(19.6.5)`.*

Let us first note that if $k'$ is a radicial extension of $k$, there is only one ideal of $A' = A \otimes_{k} k'$ above
$\mathfrak{m}$, formed of the elements of which some $p^{h}$-th power ($p$ the characteristic exponent of $k$) is in
$\mathfrak{m}$ for some suitable $h$ `(Bourbaki, Alg. comm., chap. V, §2, n° 3, lemma 4)`; $A'$ is thus a local ring,
and so is $K \otimes_{k} k' = (A \otimes_{k} k')/(\mathfrak{m} \otimes_{k} k')$; moreover the residue fields of these
two rings are identical. Recall on the other hand that if $K$ is a separable extension of $k$, then, for every finite
extension `k''` of $k$, $K \otimes_{k} k''$ is a direct composite of fields
`(Bourbaki, Alg., chap. VIII, §7, n° 3, cor. 1 of th. 1)`, and consequently $\mathfrak{m} \otimes_{k} k''$ is the
radical of $A \otimes_{k} k''$, and the field components of $K \otimes_{k} k''$ are the residue fields at the maximal
ideals of $A \otimes_{k} k''$; in

<!-- original page 199 -->

addition, these fields are separable extensions of `k''` since for every extension $k_{1}$ of `k''`, $K_{1} = K
\otimes_{k} k_{1} = (K \otimes_{k} k'') \otimes_{k''} k_{1}$ is without radical `(loc. cit., th. 1)`. If one applies
these remarks to the field $K$ of finite radicial multiplicity over $k$, one sees that for every finite extension `k''`
of $k_{0}$, $(K \otimes_{k} k')_{red}$ is separable over `k''`.

Let us pass to the proof of `(19.6.6)`. It is trivial that b) implies b'). Let us show that b') implies a). If one sets
$B' = K'[[T_{1}, \cdots, T_{n}]]$, the hypothesis that $K'$ is separable over $k'$ entails, by the initial remarks, that
for every finite extension `k''` of $k'$, the components of the complete semi-local ring $B' \otimes_{k'} k''$ (equal to
the formal power series ring $(K' \otimes_{k'} k'')[[T_{1}, \cdots, T_{n}]]$) are the rings $K_{i}''[[T_{1}, \cdots,
T_{n}]]$, where the $K_{i}''$ are the field components of $K' \otimes_{k'} k''$. Since the local components of $B'
\otimes_{k'} k''$ are also local components of $\hat{A} \otimes_{k} k'' = (\hat{A} \otimes_{k} k') \otimes_{k'} k''$,
one sees that the hypothesis b') is still verified when $k'$ is replaced by any of its finite extensions. In particular,
one may suppose that $k'$ is quasi-Galois, hence a Galois extension of a radicial extension $k_{0}'$ of $k$; $A_{0}' =
\hat{A} \otimes_{k} k'$ can then be written $A_{0}' \otimes_{k_{0}'} k'$, where $A_{0}' = \hat{A} \otimes_{k} k_{0}'$ is
a complete local ring. One then knows `(Bourbaki, Alg., chap. VIII, §8, prop. 4)` that $A'$ is a direct composite of
local rings isomorphic to $A_{0}'$ as $k_{0}'$-algebras. Now, one of these rings is by hypothesis $k'$-isomorphic to a
formal power series ring $K'[[T_{1}, \cdots, T_{n}]]$, where $K'$ is a separable extension of $k'$, hence also a
separable extension of $k_{0}'$; taking `(19.6.4)` into account, $A_{0}'$ is thus a formally smooth $k_{0}'$-algebra.
But since $k_{0}'$ is a faithfully flat, projective and finitely generated $k$-module, one concludes from `(19.4.7)`
that `Â` is a formally smooth $k$-algebra.

One has already seen `(19.6.5)` that a) implies c); it remains therefore to verify that c) implies b). Now, if c) is
verified, then, for every finite radicial extension $k'$ of $k$ containing $k_{0}$, $A \otimes_{k} k'$ is a regular
local ring, whose residue field $K'$ is a separable extension of $k'$; it follows therefore from `(19.6.4)` that its
completion $\hat{A} \otimes_{k} k'$ is $k'$-isomorphic to a formal power series ring $K'[[T_{1}, \cdots, T_{n}]]$.

**Remarks (19.6.7).**

<!-- label: 0_IV.19.6.7 -->

*(i) Note that the hypothesis that $K$ is of finite radicial multiplicity over $k$ has only been used in the proof of
the implication b') ⇒ a).*

*(ii) We shall later prove `(22.5.8)` that a) and c) are equivalent, without any hypothesis on the extension $K$ of
$k$.*

### 19.7. Case of local homomorphisms; existence and uniqueness theorems

In this number, when a semi-local ring is considered as a topological ring, it is always implicit that this is its
$\mathfrak{r}$-preadic topology, where $\mathfrak{r}$ is its radical. Every local homomorphism of local rings is
therefore automatically continuous.

**Theorem (19.7.1).**

<!-- label: 0_IV.19.7.1 -->

*Let $A$, $B$ be two Noetherian local rings, $\mathfrak{m}$, $\mathfrak{n}$ their respective maximal ideals, $k =
A/\mathfrak{m}$ the residue field of $A$; suppose $A$ and $B$ are endowed respectively with the $\mathfrak{m}$-preadic
and $\mathfrak{n}$-preadic topologies. Let $\phi : A \to B$ be a local homomorphism, and set $B_{0} = B \otimes_{A} k$.
The following properties are equivalent:*

*a) $B$ is a formally smooth $A$-algebra.*

<!-- original page 200 -->

*b) $B$ is a flat $A$-module and $B_{0} = B/\mathfrak{m}B$ (endowed with the quotient topology) is a formally smooth
$k$-algebra.*

The proof is in several steps.

**(19.7.1.1)** Let us first prove that b) implies a). We shall apply the criterion `(19.4.7)` with
$\mathfrak{J} = \mathfrak{m}$; by virtue of the second hypothesis in b), everything boils down to showing that $B$ is a
formally projective $A$-module. The hypothesis entails that for every $h > 0$, $B/\mathfrak{m}^{h} B$ is a flat
$(A/\mathfrak{m}^{h})$-module $(0_{III}, 10.2.1)$; since the $\mathfrak{m}^{h}$ form a fundamental system of
neighbourhoods of `0` in $A$, and $(B/\mathfrak{m}^{h} B)/\mathfrak{m}(B/\mathfrak{m}^{h} B) = B_{0}$, one may replace
$A$ and $B$ by $A/\mathfrak{m}^{h}$ and $B/\mathfrak{m}^{h} B$ respectively, and consequently suppose $A$ Artinian
(hence discrete). Since `B_0` is a formally smooth $k$-algebra, it is a regular ring `(19.6.5)`; let
$(x^{0}_{i})_{1 \leq i \leq n}$ be a regular system of parameters for `B_0` `(17.1.6)`, and for every $i$, let
$x_{i} \in B$ be such that $x^{0}_{i}$ is its image in $B_{0} = B/\mathfrak{m}B$; since the $x^{0}_{i}$ generate the
maximal ideal $\mathfrak{n}_{0} = \mathfrak{n}/\mathfrak{m}B$ of `B_0`, the ideals
$\mathfrak{J}^{0}_{m} = \sum (x^{0}_{i})^{m} B_{0}$ (for $m > 0$) form a fundamental system of neighbourhoods of `0` in
`B_0`, since $\mathfrak{J}^{0}_{m}$ is evidently contained in $\mathfrak{n}^{m}_{0}$, and on the other hand contains
$\mathfrak{n}^{m+n-1}_{0}$. Set $\mathfrak{J}_{m} = \sum x^{m}_{i} B$ for every $m > 0$; it is clear that
$\mathfrak{n} = \mathfrak{J}_{1} + \mathfrak{m}B$; since there exists $h > 0$ such that $\mathfrak{m}^{h} = 0$, one has
$\mathfrak{n}^{m} \subset \mathfrak{J}_{m-h} \subset \mathfrak{n}^{m-h}$ for $m > h$, and since one has seen that
$\mathfrak{J}_{m} \supset \mathfrak{J}_{m}$, one sees that the $\mathfrak{J}_{m}$ form a fundamental system of
neighbourhoods of `0` in $B$. Everything therefore boils down to proving that the $B/\mathfrak{J}_{m}$ are free
$A$-modules, and it amounts to the same to see that they are flat $A$-modules $(0_{III}, 10.1.3)$. Now, the hypothesis
that $(x^{0}_{i})$ is a `B_0`-regular sequence of elements of the maximal ideal of `B_0` entails the same property for
the sequence of the $(x^{m}_{i})$ ($1 \leq i \leq n$) for every $m > 0$ `(15.1.20)`; the conclusion then follows from
`(15.1.16, b) and c))`.

**Lemma (19.7.1.2).**

<!-- label: 0_IV.19.7.1.2 -->

*Let $A$ be a topological ring, $B$, $C$ two topological $A$-algebras which are Noetherian local rings. Suppose moreover
that $C$ is complete and that the residue field $B/\mathfrak{m}$ of $B$ is an $A$-module of finite type. Let $E$ be the
completed tensor product $B \hat{\otimes}_{A} C$. Then:*

*(i) $E$ is a complete Noetherian semi-local ring.*

*(ii) The ideal $\mathfrak{m}E$ is contained in the radical of $E$, and for every $h > 0$, $E/\mathfrak{m}^{h} E$ is
isomorphic to $(B/\mathfrak{m}^{h}) \otimes_{A} C$.*

*(iii) If $C$ is a flat $A$-module, $E$ is a flat $B$-module.*

By definition, $E$ is the separated completion of the tensor product $B \otimes_{A} C$ for the topology defined by the
ideals $Im(\mathfrak{m} \otimes_{A} C) + Im(B \otimes_{A} \mathfrak{n})$ $(0_{I}, 7.7.5)$. If one sets $\mathfrak{r} =
Im(\mathfrak{m} \otimes_{A} C) + Im(B \otimes_{A} \mathfrak{n})$, one has $\mathfrak{r}^{2} \subset Im(\mathfrak{m}^{2}
\otimes_{A} C) + Im(B \otimes_{A} \mathfrak{n}^{2})$, hence $E$ is also the separated completion of $B \otimes_{A} C$
for the $\mathfrak{r}$-preadic topology. By hypothesis, $(B \otimes_{A} C)/\mathfrak{r} = (B/\mathfrak{m}) \otimes_{A}
(C/\mathfrak{n})$ is a $(C/\mathfrak{n})$-module of finite type, hence an Artinian ring; in addition,
$\mathfrak{r}/\mathfrak{r}^{2}$, being a quotient of $((\mathfrak{m}/\mathfrak{m}^{2}) \otimes_{A} C) \oplus (B
\otimes_{A} (\mathfrak{n}/\mathfrak{n}^{2}))$, is a $(B \otimes_{A} C)$-module of finite type; applying $(0_{I},
7.2.11)$, one sees that $E$ is a Noetherian ring; furthermore, $E/\mathfrak{r}E$, isomorphic to $(B \otimes_{A}
C)/\mathfrak{r}$, being Artinian, $E$ is semi-local. Note now that $E$, which is isomorphic to
$\lim((B/\mathfrak{m}^{i}) \otimes_{A} (C/\mathfrak{n}^{j}))$, is also isomorphic, by the double-projective-limit
theorem, to `lim(lim((B/𝔪^i) ⊗_A (C/𝔫^j))) = lim((B/𝔪^i) ⊗_A C)`; now $\lim((B/\mathfrak{m}^{i}) \otimes_{A}
(C/\mathfrak{n}^{j}))$

<!-- original page 201 -->

is the separated completion of $(B/\mathfrak{m}^{i}) \otimes_{A} C$, and since $C$ is complete, this is none other than
$(B/\mathfrak{m}^{i}) \otimes_{A} C$ itself, $B/\mathfrak{m}^{i}$ being an $A$-module of finite type since
$\mathfrak{m}/\mathfrak{m}^{i}$ is a $(B/\mathfrak{m})$-module of finite type $(0_{I}, 7.3.6)$. One thus has $E =
\lim((B/\mathfrak{m}^{i}) \otimes_{A} C)$. For every integer $h > 0$, $\mathfrak{m}^{h} E$, being an ideal of $E$, is
closed in $E$ $(0_{I}, 7.3.5)$, hence complete, and on the other hand it is evidently dense in
$\lim(Im((\mathfrak{m}^{h}/\mathfrak{m}^{i}) \otimes_{A} C))$, hence equal to this latter projective limit. Furthermore,
all the projective systems considered are defined by surjective homomorphisms, hence it follows from $(0_{III}, 13.2.2)$
that $E/\mathfrak{m}^{h} E$ is isomorphic to $(B/\mathfrak{m}^{h}) \otimes_{A} C = (B \otimes_{A} C)/Im(\mathfrak{m}^{h}
\otimes_{A} C)$. In particular, since $Im(\mathfrak{m}^{h} \otimes_{A} C) \subset \mathfrak{r}$, this shows that
$\mathfrak{m}E$ is contained in $\mathfrak{r}E$, hence in the radical of $E$. Finally, the hypothesis that $C$ is a flat
$A$-module entails that $(B/\mathfrak{m}^{h}) \otimes_{A} C = E/\mathfrak{m}^{h} E$ is a flat
$(B/\mathfrak{m}^{h})$-module for every $h > 0$; since $B$ and $E$ are Noetherian and $\mathfrak{m}E$ is contained in
the radical of $E$, it follows from $(0_{III}, 10.2.2)$ that $E$ is a flat $B$-module.

**Lemma (19.7.1.3).**

<!-- label: 0_IV.19.7.1.3 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{m}$ its maximal ideal, $k$ its residue field, `B_0` a $k$-algebra;
suppose that `B_0` is a complete regular Noetherian local ring. Then there exists a topological $A$-algebra $B$ which is
a complete Noetherian local ring, a flat $A$-module, and such that `B_0` is $k$-isomorphic to $B \otimes_{A} k =
B/\mathfrak{m}B$.*

Since `Â` is flat over $A$ and has the same residue field, one may restrict to the case where $A$ is complete.

Let $K$ be the residue field of `B_0`, and let us distinguish two cases:

I) *$K$ is a separable extension of $k$.* By virtue of `(19.6.4)`, `B_0` is $k$-isomorphic to a formal power series ring
$K[[T_{1}, \cdots, T_{n}]]$. When $B_{0} = K$, the lemma has already been proved $(0_{III}, 10.3.1)$; let $C$ be a
complete Noetherian local ring which is a flat $A$-module and such that $C \otimes_{A} k$ is isomorphic to $K$. For $n
\geq 1$, it suffices to take (with the preceding notation) $B = C[[T_{1}, \cdots, T_{n}]]$; one indeed knows
`(Bourbaki, Alg. comm., chap. III, §3, n° 4, cor. 3 of th. 1)` that $B$ is a flat $C$-module, hence also a flat
$A$-module, and on the other hand, it is immediate that $C[[T_{1}, \cdots, T_{n}]] \otimes_{A} k$ is isomorphic to
$(C/\mathfrak{m}C)[[T_{1}, \cdots, T_{n}]] = B_{0}$.

II) *$K$ is of characteristic $p > 0$, and consequently the same is true of $k$.* Denote by $P$ the prime field
$\mathbb{F}_{p}$, and by $W(P)$ the complete local ring of $p$-adic numbers $\mathbb{Z}_{p}$, which is a (hence regular)
discrete valuation ring, and has $P$ as residue field. Let us first show that there exists a continuous ring
homomorphism $W(P) \to A$, thus making $A$ into a topological $W(P)$-algebra. Indeed, if $j : \mathbb{Z} \to A$ is the
canonical homomorphism, one has $j(p\mathbb{Z}) \subset \mathfrak{m}$ by hypothesis, whence $j^{-1}(\mathfrak{m}) =
p\mathbb{Z}$, and consequently $j$ factors as $\mathbb{Z} \to \mathbb{Z}_{p\mathbb{Z}} \to A$, where the latter is a
local, hence continuous, homomorphism, which (since $A$ is complete) extends by continuity to the desired homomorphism
$W(P) \to A$.

Since $k$ is a separable extension of $P$, case I) shows that there is a local homomorphism $W(P) \to W(k)$, where
$W(k)$ is a complete Noetherian local ring and a flat $W(P)$-module, such that $W(k) \otimes_{W(P)} P$ is isomorphic to
$k$. Furthermore, since the uniformizer $p$ of $W(P)$ is a $W(k)$-regular element by flatness $(0_{I}, 6.3.4)$, and
since

<!-- original page 202 -->

$W(k)/pW(k) = k$, $pW(k)$ is the maximal ideal of $W(k)$, which entails that this last ring is a complete discrete
valuation ring `(Bourbaki, Alg. comm., chap. VI, §3, n° 5, prop. 9)`. By `(19.7.1.1)` one sees in addition (since $k$ is
separable over $P$, hence a formally smooth $P$-algebra `(19.6.1)`) that $W(k)$ is a formally smooth $W(P)$-algebra. The
continuous $W(P)$-homomorphism $W(k) \to k$ thus factors as $W(k) \to A \to k$ `(19.3.11)`, which allows one to consider
$A$ as a topological $W(k)$-algebra. Applying now case I) to `B_0` considered as a $P$-algebra and to $W(P)$, one sees
that there exists a $W(P)$-algebra `B_P` which is a complete Noetherian local ring, a flat $W(P)$-module, and such that
$B_{P} \otimes_{W(P)} P$ is $P$-isomorphic to `B_0`. Using again the fact that $W(k)$ is a formally smooth
$W(P)$-algebra, one sees by `(19.3.11)` that the composite homomorphism $W(k) \to P \to B_{0}$ factors as $W(k) \to
B_{P} \to B_{0}$; furthermore, since $k = W(k)/pW(k)$, one has $B_{P} \otimes_{W(k)} k = B_{P}/pB_{P} = B_{P}
\otimes_{W(P)} P = B_{0}$. Let us show that `B_P` is a flat $W(k)$-module; since $W(k)$ is a discrete valuation ring of
which $p$ is the uniformizer, it suffices to verify that `B_P` is a torsion-free $W(k)$-module $(0_{I}, 6.3.4)$, or that
$p$ is a `B_P`-regular element, which follows from the fact that `B_P` is a flat $W(P)$-module $(0_{I}, 6.3.4)$.

Set now

```text
                                          B = B_P ⊗̂_{W(k)} A
```

and note that the residue field of $A$, being equal to that of $W(k)$, is *a fortiori* a $W(k)$-module of finite type.
It follows therefore first from `(19.7.1.2)` that $B$ is a complete Noetherian semi-local ring, $\mathfrak{m}B$ being
contained in the radical of $B$; furthermore $B/\mathfrak{m}B$ is $k$-isomorphic to $B_{P} \otimes_{W(k)} k = B_{0}$,
hence $B$ is in fact a local ring. Since `B_P` is a flat $W(k)$-module, `(19.7.1.2)` finally shows that $B$ is a flat
$A$-module. Q.E.D.

**Lemma (19.7.1.4).**

<!-- label: 0_IV.19.7.1.4 -->

*Let $A$ be a ring, $\mathfrak{J}$ an ideal of $A$, $M$, $N$ two $A$-modules separated for the $\mathfrak{J}$-preadic
topology. Suppose in addition that $N$ is complete for the $\mathfrak{J}$-preadic topology and that $M$ is a flat
$A$-module. Let $u : N \to M$ be an $A$-homomorphism; if $u \otimes 1 : N \otimes_{A} (A/\mathfrak{J}) \to M \otimes_{A}
(A/\mathfrak{J})$ is bijective, then $u$ is bijective.*

The associated graded modules being taken relative to the $\mathfrak{J}$-preadic filtrations, it follows from the
hypotheses on $M$ and $N$ relative to the $\mathfrak{J}$-preadic topologies that it suffices to prove that $gr(u) :
gr_{\bullet}(N) \to gr_{\bullet}(M)$ is bijective `(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1)`. Now,
one has a commutative diagram

```text
                                                 gr_0(u) ⊗ 1
                          gr_0(N) ⊗_{A_0} gr_•(A) ──────────→ gr_0(M) ⊗_{A_0} gr_•(A)
                                       │                                    │
                                     ψ_N│                                    │ ψ_M
                                       ↓                                    ↓
                                  gr_•(N)                              gr_•(M)
                                                      gr(u)
```

<!-- original page 203 -->

where $A_{0} = A/\mathfrak{J} = gr_{0}(A)$, and $\psi_{N}$ and $\psi_{M}$ are the canonical maps $(0_{III}, 10.1.1.2)$.
By hypothesis, $gr_{0}(u)$ is bijective, as is $\psi_{M}$ $(0_{III}, 10.2.1)$, and $\psi_{N}$ is surjective; one deduces
first that $gr_{0}(u) \otimes 1$ is bijective, then that $\psi_{N}$ is injective, hence bijective, and finally that
$gr(u)$ is bijective.

**Lemma (19.7.1.5).**

<!-- label: 0_IV.19.7.1.5 -->

*Let $A$ be a Noetherian ring, $\mathfrak{J}$ an ideal of $A$, $B$, $B'$ two $A$-algebras which are Noetherian local
rings, the homomorphisms $A \to B$, $A \to B'$ being continuous for the $\mathfrak{J}$-preadic topology on $A$. Suppose
that: 1° $B$ and $B'$ are complete for the $\mathfrak{J}$-preadic topologies; 2° $B$ is a formally smooth $A$-algebra;
3° $B'$ is a flat $A$-module. Set $A_{0} = A/\mathfrak{J}$, and let $u_{0} : B \otimes_{A} A_{0} \to B' \otimes_{A}
A_{0}$ be an `A_0`-isomorphism; then there exists an $A$-isomorphism $u : B \to B'$ such that $u_{0} = u \otimes 1$
(which entails that $B'$ is a formally smooth $A$-algebra and $B$ a flat $A$-module).*

Set $B_{0} = B \otimes_{A} A_{0}$, $B_{0}' = B' \otimes_{A} A_{0}$. Note that if $\mathfrak{m}$ and $\mathfrak{m}'$ are
the maximal ideals of $B$ and $B'$, the $\mathfrak{J}$-preadic topologies on $B$ and $B'$ are separated since
$\mathfrak{J}B \subset \mathfrak{m}$ and $\mathfrak{J}B' \subset \mathfrak{m}'$; furthermore, since $\mathfrak{J}B'$ is
closed in $B'$ for the $\mathfrak{J}$-preadic topology, the composite homomorphism $B \to B_{0} \to B_{0}'$, which is
continuous for the $\mathfrak{J}$-preadic topologies, factors as $B \to B' \to B_{0}'$, where $u$ is a continuous
$A$-homomorphism `(19.3.10)`. One clearly has $u_{0} = u \otimes 1$, and the hypothesis that $u_{0}$ is bijective
entails the same for $u$ by virtue of `(19.7.1.4)`.

**(19.7.1.6)** *End of the proof.* To complete the proof of `(19.7.1)`, one must show that a) implies b); one already
knows that a) entails that `B_0` is a formally smooth $k$-algebra `(19.3.5, (iii))`, so everything boils down to proving
that $B$ is a flat $A$-module. It amounts to the same to establish that $\hat{B}$ is a flat `Â`-module
`(Bourbaki, Alg. comm., chap. III, §5, n° 4, prop. 4)`, and one knows that $\hat{B}$ is a formally smooth `Â`-algebra
`(19.3.6)`; one may therefore restrict to the case where $A$ and $B$ are complete. Since `B_0` is a formally smooth
$k$-algebra, it is a regular ring `(19.6.5)` and complete $(0_{I}, 6.3.5)$; applying `(19.7.1.3)`, one sees that there
exists an $A$-algebra $B'$ which is a complete Noetherian local ring and a flat $A$-module, a local homomorphism $A \to
B'$ and an $A$-isomorphism $B_{0} \xrightarrow{\sim} B' \otimes_{A} k$. It then suffices to apply `(19.7.1.5)` taking
for $\mathfrak{J}$ the maximal ideal of $A$, to obtain that $B$ is $A$-isomorphic to $B'$, hence is a flat $A$-module.
Q.E.D.

**Theorem (19.7.2).**

<!-- label: 0_IV.19.7.2 -->

*Let $A$ be a Noetherian local ring, $\mathfrak{J}$ an ideal contained in the maximal ideal of $A$, $A_{0} =
A/\mathfrak{J}$, `B_0` a complete Noetherian local ring, $A_{0} \to B_{0}$ a local homomorphism making `B_0` into a
formally smooth `A_0`-algebra. Then there exists a complete Noetherian local ring $B$, a local homomorphism $A \to B$
making $B$ into a flat $A$-module, and an `A_0`-isomorphism $u : B \otimes_{A} A_{0} \xrightarrow{\sim} B_{0}$. If
`(B', u')` is a pair satisfying the same conditions as $(B, u)$, there exists an $A$-isomorphism $v : B
\xrightarrow{\sim} B'$ making the diagram*

```text
                                     B ⊗_A A_0 ──→ B' ⊗_A A_0
                                              ↘     ↙
                                                B_0
```

*commute.*

<!-- original page 204 -->

Let $\mathfrak{m}$ be the maximal ideal of $A$, so that $\mathfrak{m}_{0} = \mathfrak{m}/\mathfrak{J}$ is the maximal
ideal of `A_0`, $A$ and `A_0` having the same residue field $k$. Set $B_{00} = B_{0} \otimes_{A_{0}} k$; since $B_{00}$
is a formally smooth $k$-algebra `(19.3.5, (iii))`, it is a regular local ring `(19.6.5)`; applying `(19.7.1.3)`, one
sees that there exists a topological $A$-algebra $B$ which is a complete Noetherian local ring, a flat $A$-module, and
for which one has an $A$-isomorphism $u_{00} : B \otimes_{A} k \xrightarrow{\sim} B_{00}$. Note that by virtue of
`(19.7.1)`, $B$ is a formally smooth $A$-algebra, so $B \otimes_{A} A_{0} = B/\mathfrak{J}B$ is a formally smooth
`A_0`-algebra `(19.3.5, (iii))` and a complete Noetherian local ring; furthermore, `B_0` is a flat `A_0`-module by
virtue of the hypothesis and of `(19.7.1)`; since one has a $k$-isomorphism $u_{00} : B \otimes_{A} k = (B \otimes_{A}
A_{0}) \otimes_{A_{0}} k \xrightarrow{\sim} B_{0} \otimes_{A_{0}} k = B_{00}$, one deduces from `(19.7.1.5)`, applied
with $A$ replaced by `A_0` and $\mathfrak{J}$ by $\mathfrak{m}_{0}$, that there exists an `A_0`-isomorphism $u : B
\otimes_{A} A_{0} \xrightarrow{\sim} B_{0}$ such that $u_{00} = u \otimes 1$. As for the uniqueness assertion, note that
the ideals $\mathfrak{J}B$ (resp. $\mathfrak{J}B'$) are closed in $B$ (resp. $B'$) $(0_{I}, 7.3.5)$, hence $B$ and $B'$
are separated and complete for the $\mathfrak{J}$-preadic topologies
`(Bourbaki, Top. gén., chap. III, 3rd ed., §3, n° 5, cor. 2 of prop. 9)`; by hypothesis, one has an `A_0`-isomorphism
$v_{0} : B \otimes_{A} A_{0} \xrightarrow{\sim} B' \otimes_{A} A_{0}$ such that $u' \circ v_{0} = u$; since $B$ is a
formally smooth $A$-algebra and $B'$ a flat $A$-module, one may apply `(19.7.1.5)`, whence the existence of the
$A$-isomorphism $v$ answering the question.

**Remarks (19.7.3).**

<!-- label: 0_IV.19.7.3 -->

*(i) Note that the uniqueness assertion in `(19.7.2)` is still valid if one assumes only that $B$ and $B'$ are complete
for the $\mathfrak{J}$-preadic topologies. We do not know if one can improve the existence assertion in the same way, in
other words whether one can dispense with assuming the local ring `B_0` complete (for its $\mathfrak{n}_{0}$-preadic
topology, denoting by $\mathfrak{n}_{0}$ its maximal ideal) by requiring only that $B$ be complete for the
$\mathfrak{J}$-preadic topology. When `A_0` is complete for the $\mathfrak{m}$-preadic topology, one can see that this
problem reduces to the following: if `B_0` is a (not necessarily complete) regular Noetherian local ring containing the
prime field $\mathbb{F}_{p} = \mathbb{Z}/p\mathbb{Z}$, does there exist for every $n \geq 1$ a flat $(\mathbb{Z}/p^{n}
\mathbb{Z})$-algebra $B$ such that $B/pB$ is isomorphic to `B_0`?*

*(ii) Note that in general, the isomorphism $v$ whose existence is asserted in `(19.7.2)` is not unique (cf.
`(19.8.7)`).*

### 19.8. Cohen algebras and $p$-Cohen rings; application to the structure of complete local rings

The results of this section are immediate applications of the theorems of `(19.7)`, but deserve to be made explicit
because of their practical importance.

**Definition (19.8.1).**

<!-- label: 0_IV.19.8.1 -->

*Let $A$, $B$ be two Noetherian local rings, $\mathfrak{m}$ the maximal ideal of $A$, $k = A/\mathfrak{m}$ its residue
field, $\phi : A \to B$ a local homomorphism, making $B$ into an $A$-algebra. We say that $B$ is a **Cohen $A$-algebra**
if it satisfies the following conditions:*

*(i) $B$ is a complete ring.*

*(ii) $B$ is a flat $A$-module.*

*(iii) $B \otimes_{A} k$ is a field (in other words, $\mathfrak{m}B$ is the maximal ideal of $B$) which is a separable
extension of $k$.*

<!-- original page 205 -->

**Theorem (19.8.2).**

<!-- label: 0_IV.19.8.2 -->

*Let $A$ be a Noetherian local ring, $k$ its residue field.*

*(i) If $B$ is a Cohen $A$-algebra, $B$ is a formally smooth $A$-algebra. For every complete Noetherian local ring $C$,
every local homomorphism $A \to C$ and every ideal $\mathfrak{J} \neq C$ in $C$, every $A$-homomorphism $B \to
C/\mathfrak{J}$ therefore factors as $B \to C \to C/\mathfrak{J}$, where $v$ is a (necessarily local) $A$-homomorphism.*

*(ii) For every field $K$ which is a separable extension of $k$, there exists a Cohen $A$-algebra $B$ such that $B
\otimes_{A} k$ is $k$-isomorphic to $K$, and such an $A$-algebra is unique up to isomorphism.*

Since $K$ is a formally smooth $k$-algebra `(19.6.1)`, assertion (i) follows from `(19.7.1)`. To prove (ii), one may
restrict to the case where $A$ is complete, for it amounts to the same to say that $B$ is a flat $A$-module or a flat
`Â`-module $(0_{III}, 10.2.3)$, one has $\mathfrak{m}B = \mathfrak{m}\hat{A} B$ and $k$ is the residue field of `Â`. It
then suffices to apply `(19.7.2)` by taking $\mathfrak{J} = \mathfrak{m}$ and $B_{0} = K$ (and using `(19.6.1)`).

**Definition (19.8.3).**

<!-- label: 0_IV.19.8.3 -->

*We call **prime local ring** a local ring of the form $\mathbb{Z}_{p\mathbb{Z}}$, where $p\mathbb{Z}$ is a prime ideal
of $\mathbb{Z}$. We call **complete prime local ring** the completion of a prime local ring.*

The prime local rings are therefore of two kinds:

1° Those which correspond to the maximal ideals $p\mathbb{Z}$ where $p \neq 0$ is a prime number;
$\mathbb{Z}_{p\mathbb{Z}}$ is a discrete valuation ring, whose completion is *the ring of $p$-adic integers*, usually
denoted $\mathbb{Z}_{p}$ ⁽¹⁾.

2° For the prime ideal $p\mathbb{Z} = (0)$, $\mathbb{Z}_{(0)}$ is the field of rational numbers $\mathbb{Q}$, identical
to its completion (the topology being naturally the topology of Noetherian local ring, hence here the discrete
topology).

The terminology of `(19.8.3)`, analogous to that of "prime fields", is justified in the same way: for every local ring
$A$, consider the canonical homomorphism $\phi : \mathbb{Z} \to A$, and let $p\mathbb{Z}$ be the inverse image under
this homomorphism of the maximal ideal $\mathfrak{m}$ of $A$; $p\mathbb{Z}$ is a prime ideal of $\mathbb{Z}$ and the
preceding homomorphism therefore factors as $\mathbb{Z} \to \mathbb{Z}_{p\mathbb{Z}} \to A$; moreover, since $\phi$ is
the unique homomorphism of $\mathbb{Z}$ into $A$, $p$ and $\psi$ are uniquely determined. In other words, for every
local ring $A$, there is a unique homomorphism $\psi : P \to A$, where $P$ is a prime local ring; if in addition $A$ is
separated and complete, one can extend by completion this homomorphism, and there is therefore a unique homomorphism
$\psi : P \to A$, where $P$ is a complete prime local ring. Moreover, by passing to quotients, $\psi$ gives a
homomorphism of the residue field $\mathbb{F}_{p}$ if $p > 0$ (resp. $\mathbb{Q}$ if $p = 0$) into the residue field $k$
of $A$, and $p$ is therefore the characteristic of $k$.

If one takes in particular for $A$ a prime local ring (resp. complete prime local ring), one sees that there exists in
such a ring only *one* endomorphism, namely the identity.

______________________________________________________________________

⁽¹⁾ This notation, currently universally used, conflicts in this case with the notation $A_{f}$ adopted in $(0_{I},
1.2.3)$: with $A = \mathbb{Z}$ and $f = p$, $A_{p}$ indeed means the ring of rational numbers of the form $k/p^{n}$ ($k
\in \mathbb{Z}$, $n$ an integer $\geq 0$); we shall always avoid using the notation $\mathbb{Z}_{p}$ to designate this
latter ring.

<!-- original page 206 -->

**Definition (19.8.4).**

<!-- label: 0_IV.19.8.4 -->

*Let $A$ be a local ring, $P \to A$ the unique homomorphism of a prime local ring $P$ into $A$, $p$ the characteristic
of the residue fields of $P$ and $A$. We say that $A$ is a **Cohen ring** if it is a Cohen $P$-algebra, that is to say
`(19.8.1)` if:*

*1° $A$ is Noetherian and complete.*

*2° $A$ is a flat $P$-module (which is also equivalent to saying that $A$ is a flat $\hat{P}$-module
`(Bourbaki, Alg. comm., chap. III, §5, n° 4, prop. 4)`).*

*3° $A/pA$ is a field (necessarily separable over the residue field of $P$, this field being prime).*

If $p = 0$, these conditions are equivalent to saying that $A$ is a field of characteristic `0`. If $p > 0$, one
necessarily has $pA \neq 0$; condition 3° means that `pA` is the maximal ideal $\mathfrak{m}$ of $A$; condition 2° means
that $p$ is $A$-regular, since $P$ is a discrete valuation ring $(0_{I}, 6.3.4)$. Hence $A$ is a regular ring
`(17.1.1, d)` of dimension `1`, and consequently a complete discrete valuation ring by virtue of 1°; in summary:

**Proposition (19.8.5).**

<!-- label: 0_IV.19.8.5 -->

*The Cohen rings are the fields of characteristic `0` and the complete discrete valuation rings whose residue field has
characteristic $p > 0$ and whose maximal ideal is generated by $p \cdot 1$ (`1` being the unit of the ring).*

Note that in the second case, $p \cdot 1 \neq 0$ since $p$ is $A$-regular, so one can identify $p \cdot 1$ with the
integer $p$, the canonical homomorphism $\mathbb{Z} \to A$ is injective, and one identifies $p \cdot 1$ with the element
$p$ of $\mathbb{Z}_{p}$; one says in this case that $A$ is a **$p$-Cohen ring**.

**Theorem (19.8.6) (Cohen).**

<!-- label: 0_IV.19.8.6 -->

*(i) Let $W$ be a Cohen ring, $C$ a complete Noetherian local ring, $\mathfrak{J}$ an ideal of $C$ distinct from $C$.
Then every local homomorphism $u : W \to C/\mathfrak{J}$ factors as $W \to C \to C/\mathfrak{J}$, where $v$ is a local
homomorphism.*

*(ii) Let $K$ be a field. There exists a Cohen ring $W$ whose residue field is isomorphic to $K$. If $W'$ is a second
Cohen ring, $K'$ its residue field, every isomorphism $u : K \xrightarrow{\sim} K'$ arises by passage to quotients from
an isomorphism $v : W \xrightarrow{\sim} W'$.*

This is none other than `(19.8.2)` applied to the case where $A$ is a prime local ring.

**Remarks (19.8.7).**

<!-- label: 0_IV.19.8.7 -->

*(i) When $K$ is of characteristic `0`, part (ii) of `(19.8.6)` becomes trivial.*

*(ii) The homomorphism $v$ of `(19.8.6, (i))` is not necessarily uniquely determined by $u$, as is already shown by the
case where $W$ is a field of characteristic `0`, $\mathfrak{J} = 0$ and $u$ is an isomorphism (cf. `(21.5.5)`).
Likewise, in `(19.8.6, (ii))` the isomorphism $v$ is not necessarily uniquely determined by $u$ (cf. `(21.5.5)`).*

*However, when $K$ is perfect and of characteristic $p > 0$, one will see `(21.5.5)` that in `(19.8.6, (ii))` the
isomorphism $v$ is unique. One will also see later that in this case $W$ is identified with the ring $W_{\infty}(K)$ of
Witt vectors of infinite length over $K$.*

*(iii) In `(19.8.6, (i))`, one may weaken the hypotheses on $C$ by using `(19.3.10)` and `(19.3.12)`.*

**Theorem (19.8.8) (Cohen).**

<!-- label: 0_IV.19.8.8 -->

*Let $A$ be a complete Noetherian local ring, $k$ its residue field.*

<!-- original page 207 -->

*(i) There exists a Cohen ring $W$ such that $A$ is isomorphic to a quotient ring of a formal power series ring
$W[[T_{1}, \cdots, T_{n}]]$ (and in particular $A$ is isomorphic to a quotient of a complete regular local ring
`(17.3.8)`). If $A$ contains a field, it is isomorphic to a quotient ring of $k[[T_{1}, \cdots, T_{n}]]$.*

*(ii) Suppose in addition that $A$ is integral. Then there exists a subring $B$ of $A$ such that: 1° $B$ is isomorphic
to a formal power series ring over a ring $C$ which is a field or a Cohen ring (which entails that $B$ is a complete
regular local ring `(17.3.8)`); 2° $B$ has the same residue field as $A$ and the injection $B \to A$ is a local
homomorphism; 3° $A$ is a finite $B$-algebra.*

Let $\mathfrak{m}$ be the maximal ideal of $A$. There exists a Cohen ring $W$ whose residue field is isomorphic to $k$
`(19.8.6, (ii))`; one therefore has a local homomorphism $W \to A/\mathfrak{m}$, which consequently factors as $W \to A
\to A/\mathfrak{m}$, where $u$ is a local homomorphism `(19.8.6, (i))`. For every finite family $(x_{i})_{1 \leq i \leq
n}$ of elements of $\mathfrak{m}$, there then exists a local homomorphism $v : W[[T_{1}, \cdots, T_{n}]] \to A$
extending $u$ and such that $v(T_{i}) = x_{i}$ for every $i$ `(Bourbaki, Alg. comm., chap. III, §4, n° 5, prop. 6)`.
When $A$ contains a field, it contains a prime field $P$, of which $k$ is a (necessarily separable) extension, and
consequently $A$ contains a field isomorphic to $k$ `(19.6.2)`; one may then replace $W$ by $k$ in the preceding
definition of $v$.

(i) Let us first take for the $x_{i}$ a system of generators of $\mathfrak{m}$. Since $W$ has the same residue field as
$A$, and the classes of the $x_{i}$ in the graded ring $gr_{\bullet}(A)$ generate $gr_{\bullet}(A)$ as a $k$-algebra,
$gr(v) : gr_{\bullet}(W[[T_{1}, \cdots, T_{n}]]) \to gr_{\bullet}(A)$ is surjective; one deduces that $v$ itself is
surjective `(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 2 of th. 1)`. Recall that the case where $A$ contains a
field has already been seen and only figures here for reference `(19.6.3)`.

(ii) If $A$ contains a field, it contains a field $k'$ isomorphic to $k$ as one has seen; one then considers a system of
parameters $(y_{i})_{1 \leq i \leq m}$ of $A$ `(16.3.6)`, one takes $B = k[[T_{1}, \cdots, T_{m}]]$ and one considers
the local homomorphism $w : B \to A$ which coincides on $k$ with an isomorphism $k \to k'$ and which is such that
$w(T_{j}) = y_{j}$ for $1 \leq j \leq m$. If $A$ does not contain a field, the unique homomorphism
$\mathbb{Z}_{p\mathbb{Z}} \to A$ `(19.8.3)` is necessarily injective (otherwise, since $A$ is integral, its kernel would
be the maximal ideal of $\mathbb{Z}_{p\mathbb{Z}}$ and its image isomorphic to a field); furthermore, one has then $p >
0$ by hypothesis, $\mathbb{Z}_{p\mathbb{Z}}$ being a field if $p = 0$. The element $p \cdot 1$ of $A$ (identified with
$p$) is not a zero-divisor in $A$, and is contained in $\mathfrak{m}$, hence `(16.3.4 and 16.3.7)` there exists a family
$(y_{i})_{1 \leq i \leq m-1}$ which, with $p$, forms a system of parameters of $A$. The Cohen ring $W$ considered at the
beginning of the proof is then a discrete valuation ring of residue field $k$, in which $p$ generates the maximal ideal
`(19.8.5)`, and the unique homomorphism $u : W \to A$ defined at the beginning sends $p$ to itself. One then takes $B =
W[[T_{1}, \cdots, T_{m-1}]]$ and one considers the local homomorphism $w : B \to A$ which coincides with $u$ on $W$ and
is such that $w(T_{i}) = y_{i}$ for $1 \leq i \leq m - 1$. In both cases, if $\mathfrak{n}$ is the maximal ideal of $B$,
it is clear that $\mathfrak{n}A$ is an ideal of definition of $A$; since in addition $B/\mathfrak{n}$ and
$A/\mathfrak{m}$ are isomorphic, $A$ is a quasi-finite $B$-module $(0_{I}, 7.4.4)$, hence an $A$-module of finite type
since $B$ is complete and $A$ separated for the $\mathfrak{n}$-preadic topologies $(0_{I}, 7.4.1)$. On the other hand,

<!-- original page 208 -->

in both cases one has $\dim(B) = \dim(A) = m$; in the first case, this follows from `(17.1.4, (iii))`; in the second,
one sees directly that $p$ and the $T_{i}$ ($1 \leq i \leq m - 1$) form a $B$-regular sequence generating
$\mathfrak{n}$, or one can also use the fact that these elements generate $\mathfrak{n}$ and that one has $\dim(B) \geq
\dim(A)$ by `(16.3.10)`. Since $A$ and $B$ are integral, one finally deduces from `(16.3.10)` that $w$ is injective,
which completes the proof.

**Corollary (19.8.9).**

<!-- label: 0_IV.19.8.9 -->

*Let $A$ be a complete integral Noetherian local ring containing a field $k_{0}$; let $k$ be the residue field of $A$,
and suppose that $k$ is finite over $k_{0}$. Then, in the conclusion of `(19.8.8, (ii))`, one may replace 1° and 2° by
the condition that $B$ is of the form $k_{0}[[T_{1}, \cdots, T_{m}]]$, the canonical injection $B \to A$ being a
$k_{0}$-local homomorphism (for the usual $k_{0}$-algebra structure on $B$).*

Indeed, taking up the proof of `(19.8.8, (ii))`, one defines this time $w : k_{0}[[T_{1}, \cdots, T_{m}]] \to A$ as
coinciding on $k_{0}$ with the identity and sending $T_{j}$ to $y_{j}$ for $1 \leq j \leq n$. The hypothesis that $k$ is
of finite degree over $k_{0}$ still entails that $A$ is a quasi-finite $B$-module, hence of finite type by $(0_{I},
7.4.1)$, and one concludes as in `(19.8.8)`.

**Corollary (19.8.10).**

<!-- label: 0_IV.19.8.10 -->

*Let $A$ be an Artinian local ring whose maximal ideal $\mathfrak{m}$ is of square zero; there exists then a regular
Noetherian local ring $B$, with maximal ideal $\mathfrak{n}$, such that $A$ is isomorphic to $B/\mathfrak{n}^{2}$.*

Let $K$ be the residue field $A/\mathfrak{m}$ of $A$, $n$ the rank of $\mathfrak{m} = \mathfrak{m}/\mathfrak{m}^{2}$ on
$K$. If $A$ contains a field, it follows from `(19.6.3)` that $A$ is isomorphic to $B/\mathfrak{b}$, where $B =
K[[T_{1}, \cdots, T_{n}]]$ and $\mathfrak{b}$ is contained in the square of the maximal ideal $\mathfrak{n}$ of $B$; but
since $long(B/\mathfrak{n}^{2}) = n + 1 = long(A)$, one necessarily has $\mathfrak{b} = \mathfrak{n}^{2}$.

Suppose next that $A$ does not contain a field; this entails that $K$ is of characteristic $p > 0$ and that $p \cdot 1
\neq 0$ in $A$ `(19.6.3)`; hence $p \cdot 1$ is an element of $\mathfrak{m}$, and there are consequently $n - 1$ other
elements $x_{i}$ ($2 \leq i \leq n$) of $\mathfrak{m}$ forming with $p \cdot 1$ a basis of $\mathfrak{m}$ over $K$. Let
$W$ be a Cohen ring whose residue field is isomorphic to $K$; $W$ is a discrete valuation ring in which $p$ generates
the maximal ideal; one has seen in the proof of `(19.8.8)` that there is a homomorphism $u : W \to A$ sending $p$ to
itself and which by passage to quotients gives the identity on $K$. One takes $B = W[[T_{2}, \cdots, T_{n}]]$ and one
considers the local homomorphism $w : B \to A$ which coincides with $u$ on $W$ and is such that $w(T_{i}) = x_{i}$ for
$2 \leq i \leq n$. It is clear that $w$ is surjective and that its kernel $\mathfrak{b}$ is contained in the square of
the maximal ideal $\mathfrak{n} = pB + BT_{2} + \cdots + BT_{n}$ of $B$; since $long(B/\mathfrak{n}^{2}) = n + 1 =
long(A)$, one again has $\mathfrak{b} = \mathfrak{n}^{2}$.

**Proposition (19.8.11).**

<!-- label: 0_IV.19.8.11 -->

*Let $A$ be an Artinian local ring, $\mathfrak{m}$ its maximal ideal, $k$ its residue field. For $A$ to be isomorphic to
a quotient ring of a Cohen ring, it is necessary and sufficient that $\mathfrak{m}$ be generated by $p \cdot 1$, where
$p$ is the characteristic of $k$.*

The condition is clearly necessary `(19.8.5)`. To see that it is sufficient, one observes, as at the beginning of the
proof of `(19.8.8)`, that there exists a Cohen ring $W$ whose residue field is isomorphic to $k$ and a local
homomorphism $u : W \to A$. Furthermore, if one considers the composite homomorphism $\mathbb{Z}_{p\mathbb{Z}} \to W \to
A$ (which is necessarily the unique homomorphism of $\mathbb{Z}_{p\mathbb{Z}}$ into $A$), one sees that the image

<!-- original page 209 -->

under $u$ of the element $p \cdot 1$ of $W$ is the element $p \cdot 1$ of $A$; since the element $p \cdot 1$ of $W$
generates the maximal ideal of this ring, one deduces immediately from the hypothesis that $gr(u) : gr_{\bullet}(W) \to
gr_{\bullet}(A)$ is surjective, and consequently so is $u$
`(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 2 of th. 1)`.

### 19.9. Relatively formally smooth algebras

**Definition (19.9.1).**

<!-- label: 0_IV.19.9.1 -->

*Let $\Lambda$ be a topological ring, $A$ a topological $\Lambda$-algebra, $B$ a topological $A$-algebra. We say that
$B$ is a **formally smooth $A$-algebra relatively to $\Lambda$** if, for every discrete topological $A$-algebra $C$ and
every nilpotent ideal $\mathfrak{J}$ of $C$, every continuous $A$-homomorphism $u_{0} : B \to C/\mathfrak{J}$ which
factors as $B \to C \to C/\mathfrak{J}$, where $u$ is a continuous $\Lambda$-homomorphism, also factors as $B \to C \to
C/\mathfrak{J}$, where $v$ is a continuous $A$-homomorphism.*

It follows from this definition that if $B$ is a formally smooth $\Lambda$-algebra, then $B$ is also formally smooth
relatively to $\Lambda$, for any structure of topological $\Lambda$-algebra defined on $A$ (in other words, for any
continuous ring homomorphism $\Lambda \to A$).

**Proposition (19.9.2).**

<!-- label: 0_IV.19.9.2 -->

*Let $\Lambda$ be a topological ring, $A$ a topological $\Lambda$-algebra.*

*(i) $A$ is a formally smooth $A$-algebra relatively to $\Lambda$.*

*(ii) If $B$ is a formally smooth $A$-algebra relatively to $\Lambda$ and $C$ a formally smooth $B$-algebra relatively
to $\Lambda$, then $C$ is a formally smooth $A$-algebra relatively to $\Lambda$.*

*(iii) Let $B$ be a formally smooth $A$-algebra relatively to $\Lambda$, $A'$ a topological $A$-algebra; then the
topological $A'$-algebra $B \otimes_{A} A'$ is formally smooth relatively to $\Lambda$.*

*(iv) Let $B$ be a topological $A$-algebra, $S$ (resp. $T$) a multiplicative subset of $A$ (resp. $B$) such that the
canonical image of $S$ in $B$ is contained in $T$. If $B$ is a formally smooth $A$-algebra relatively to $\Lambda$, then
$T^{-1} B$ is a formally smooth $S^{-1} A$-algebra relatively to $\Lambda$.*

*(v) Let $B_{i}$ ($1 \leq i \leq n$) be topological $A$-algebras. For $\prod^{n}_{i=1} B_{i}$ to be a formally smooth
$A$-algebra relatively to $\Lambda$, it is necessary and sufficient that each of the $B_{i}$ be so.*

Assertion (i) is trivial, and the proof of the others is closely modeled on the proofs of `(19.3.5)`; it is therefore
left to the reader.

**Corollary (19.9.3).**

<!-- label: 0_IV.19.9.3 -->

*Let $\Lambda$ be a topological ring, $A$ and $A'$ two topological $\Lambda$-algebras. Then the topological $A$-algebra
$B' = B \otimes_{A} A'$ is a formally smooth $A$-algebra relatively to $\Lambda$.*

This follows from `(19.9.2, (i) and (iii))`.

**Proposition (19.9.4).**

<!-- label: 0_IV.19.9.4 -->

*Let $\Lambda$ be a topological ring, $A$ a topological $\Lambda$-algebra, $B$ a topological $A$-algebra. The following
conditions are equivalent:*

*a) $B$ is a formally smooth $A$-algebra relatively to $\Lambda$.*

*b) $B$ is a formally smooth `Â`-algebra relatively to $\Lambda$.*

*c) $\hat{B}$ is a formally smooth $A$-algebra relatively to $\Lambda$.*

*d) $\hat{B}$ is a formally smooth `Â`-algebra relatively to $\Lambda$.*

One again leaves to the reader the proof, modeled on that of `(19.3.6)`.

<!-- original page 210 -->

**(19.9.5)** Likewise, the statement `(19.3.8)` is still valid (with the same proof) when one replaces "formally smooth"
by "formally smooth relatively to $\Lambda$". If in the statement of `(19.3.10)` one replaces "formally smooth" by
"formally smooth relatively to $\Lambda$", the conclusion is replaced by the following (the proof remaining essentially
unchanged): every $\Lambda$-homomorphism $u_{0} : B \to C/\mathfrak{J}$ which factors as $B \to C \to C/\mathfrak{J}$,
where $u$ is a continuous $\Lambda$-homomorphism, also factors as $B \to C \to C/\mathfrak{J}$, where $v$ is a
continuous $A$-homomorphism.

**(19.9.6)** The criteria for formal smoothness `(19.4.1)` and `(19.4.2)` are valid when one replaces "formally smooth"
by "formally smooth relatively to $\Lambda$", the proofs remaining practically unchanged.

**Proposition (19.9.7).**

<!-- label: 0_IV.19.9.7 -->

*Let $\Lambda$ be a topological ring, $A$ a topological $\Lambda$-algebra, $B$ a topological $A$-algebra. Suppose that
for every discrete $A$-algebra $C$ and every ideal $\mathfrak{J}$ of $C$ such that $\mathfrak{J}^{2} = 0$, every
continuous $A$-homomorphism $u_{0} : B \to C/\mathfrak{J}$ which factors as $B \to C \to C/\mathfrak{J}$, where $u$ is a
continuous $\Lambda$-homomorphism, also factors as $B \to C \to C/\mathfrak{J}$, where $v$ is a continuous
$A$-homomorphism. Then $B$ is a formally smooth $A$-algebra relatively to $\Lambda$.*

The proof of `(19.4.3)` transcribes immediately.

**Proposition (19.9.8).**

<!-- label: 0_IV.19.9.8 -->

*Let $\Lambda$ be a topological ring, $A$ a topological $\Lambda$-algebra, $B$ a topological $A$-algebra. For $B$ to be
a formally smooth $A$-algebra relatively to $\Lambda$, it is necessary and sufficient that for every discrete
topological $B$-module $L$ annihilated by an open ideal of $B$, one have (cf. `18.4.2`) $Exalcotop_{A/\Lambda}(B, L) =
0$.*

With the notation of the proof of `(19.4.4)`, it suffices to note here that one may suppose that the extension
$E_{\lambda}$ of $B_{\lambda}$ is $\Lambda$-trivial; the rest of the proof is then unchanged.

When $\Lambda$, $A$ and $B$ are discrete rings, the criterion `(19.9.8)` reduces to

```text
(19.9.8.1)                            Exalcom_{A/Λ}(B, L) = 0              for every B-module L;
```

in other words, every commutative $A$-extension of $B$ by a $B$-module, which is $\Lambda$-trivial, is also $A$-trivial.

[^1]: Also called *simple morphisms* in certain recent works (inspired by the classical terminology "simple point");
    this terminology however leads to confusion, in particular in the theory of algebraic groups.

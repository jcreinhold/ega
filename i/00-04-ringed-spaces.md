# Chapter 0 — Preliminaries

## §4. Ringed Spaces

<!-- label: 0.4 -->

### 4.1. Ringed spaces; $\mathcal{A}$-Modules; $\mathcal{A}$-Algebras

<!-- label: 0.4.1 -->

**(4.1.1)** A _ringed space_ (resp. _topologically ringed space_) is a pair $(X, \mathcal{A})$ consisting of a
topological space $X$ and a sheaf of rings (not necessarily commutative) (resp. a sheaf of topological rings)
$\mathcal{A}$ on $X$; we call $X$ the topological space _underlying_ the ringed space $(X, \mathcal{A})$, and
$\mathcal{A}$ the _structure sheaf_. The latter will be written $\mathcal{O}_{X}$, and its stalk at $x \in X$ will be
written $\mathcal{O}_{X,x}$ or simply $\mathcal{O}_{x}$ when no confusion can arise.

We shall write `1` or $e$ for the _unit section_ of $\mathcal{O}_{X}$ over $X$ (the unit element of $\Gamma(X,
\mathcal{O}_{X})$).

Since in this treatise we shall mainly consider sheaves of _commutative_ rings, when we speak of a ringed space $(X,
\mathcal{A})$ without further qualification it will be understood that $\mathcal{A}$ is a sheaf of commutative rings.

Ringed spaces with structure sheaf not necessarily commutative (resp. topologically ringed spaces) form a _category_,
with morphisms $(X, \mathcal{A}) \to (Y, \mathcal{B})$ defined as pairs $(\psi, \theta) = \Psi$ consisting of a
continuous map $\psi : X \to Y$ and a _ψ-morphism_ $\theta : \mathcal{B} \to \mathcal{A}$ (3.5.1) of sheaves of rings
(resp. sheaves of topological rings). The _composite_ of a second morphism $\Psi' = (\psi', \theta') : (Y, \mathcal{B})
\to (Z, \mathcal{C})$ with $\Psi$, written $\Psi'' = \Psi' \circ \Psi$, is $(\psi'', \theta'')$ with $\psi'' = \psi'
\circ \psi$ and $\theta''$ the composite of $\theta$ and $\theta'$ (equal to $\psi'_{*}(\theta) \circ \theta'$; cf.
3.5.2). For ringed spaces, recall that $\theta''^{\sharp} = \theta^{\sharp} \circ \psi*(\theta'^{\sharp})$ (3.5.5);
hence if $\theta^{\sharp}$ and $\theta'^{\sharp}$ are _injective_ (resp. _surjective_) homomorphisms, so is
$\theta''^{\sharp}$, using that $\psi_{x} \circ \rho_{\psi(x)}$ is an isomorphism for every $x \in X$ (3.7.2). One
checks at once that when $\psi$ is _injective_ and $\theta^{\sharp}$ is _surjective_, the morphism $(\psi, \theta)$ is a
_monomorphism_ (T, 1.1) in the category of ringed spaces.

By abuse of language, we shall often replace $\psi$ by $\Psi$ in the notation — for instance writing $\Psi^{-1}(U)$ in
place of $\psi^{-1}(U)$ for $U \subset Y$ — when no confusion can arise.

**(4.1.2)** For every subset $M \subset X$, the pair $(M, \mathcal{A}|M)$ is plainly a ringed space, called _induced_ on
$M$ by $(X, \mathcal{A})$ (or the _restriction_ of $(X, \mathcal{A})$ to $M$). If $j : M \to X$ is the canonical
injection and $\omega$ the identity of $\mathcal{A}|M$, then $(j, \omega^{\flat})$ is a monomorphism $(M, \mathcal{A}|M)
\to (X, \mathcal{A})$ of ringed spaces, called the _canonical injection_. The composite of a morphism $\Psi : (X,
\mathcal{A}) \to (Y, \mathcal{B})$ with this injection is called the _restriction_ of $\Psi$ to $M$.

**(4.1.3)** We shall not return to the definition of $\mathcal{A}$-_Modules_ or _algebraic sheaves_ on a ringed space
$(X, \mathcal{A})$ (G, II, 2.2); when $\mathcal{A}$ is a sheaf of rings not necessarily commutative, by
$\mathcal{A}$-Module we shall always mean "left $\mathcal{A}$-Module" unless explicit mention is made to the contrary.
The $\mathcal{A}$-submodules of $\mathcal{A}$ will be called _sheaves of (left, right, or two-sided) ideals_ in
$\mathcal{A}$, or $\mathcal{A}$-_Ideals_.

When $\mathcal{A}$ is a sheaf of commutative rings, and the _module_ structure is replaced everywhere by an _algebra_
structure in the definition of $\mathcal{A}$-Modules, one obtains the definition of an $\mathcal{A}$-_Algebra_ on $X$.
Equivalently, an $\mathcal{A}$-Algebra (not necessarily commutative) is an $\mathcal{A}$-Module $\mathcal{C}$ together
with an $\mathcal{A}$-Module homomorphism $\phi : \mathcal{C} \otimes_{\mathcal{A}} \mathcal{C} \to \mathcal{C}$ and a
section $e$ over $X$ such that:

1° the diagram

```
𝒞 ⊗_𝒜 𝒞 ⊗_𝒜 𝒞 ──φ⊗1──→ 𝒞 ⊗_𝒜 𝒞
        │                         │
      1⊗φ                         φ
        │                         │
        ↓                         ↓
   𝒞 ⊗_𝒜 𝒞 ─────φ────→         𝒞
```

commutes;

2° for every open $U \subset X$ and every section $s \in \Gamma(U, \mathcal{C})$, $\phi((e|U) \otimes s) = \phi(s
\otimes (e|U)) = s$.

To say that $\mathcal{C}$ is a _commutative_ $\mathcal{A}$-Algebra is to say in addition that the diagram

```
𝒞 ⊗_𝒜 𝒞 ──σ──→ 𝒞 ⊗_𝒜 𝒞
       ↘φ      ↙φ
          𝒞
```

commutes, where $\sigma$ is the canonical symmetry of the tensor product $\mathcal{C} \otimes_{\mathcal{A}}
\mathcal{C}$.

Homomorphisms of $\mathcal{A}$-Algebras are defined as homomorphisms of $\mathcal{A}$-Modules as in (G, II, 2.2), but of
course no longer form an abelian group.

If $\mathcal{M}$ is an $\mathcal{A}$-submodule of an $\mathcal{A}$-Algebra $\mathcal{C}$, the _sub-$\mathcal{A}$-Algebra
of $\mathcal{C}$ generated by_ $\mathcal{M}$ is the sum of the images of the homomorphisms $\otimes^{n}\mathcal{M} \to
\mathcal{C}$ (for $n \geq 0$). It is also the sheaf associated with the presheaf of algebras $U \mapsto \mathcal{B}(U)$,
where $\mathcal{B}(U)$ is the subalgebra of $\Gamma(U, \mathcal{C})$ generated by the submodule $\Gamma(U,
\mathcal{M})$.

**(4.1.4)** A sheaf of rings $\mathcal{A}$ on a topological space $X$ is said to be _reduced at a point_ $x \in X$ if
the stalk $\mathcal{A}_{x}$ is a _reduced_ ring (1.1.1); $\mathcal{A}$ is _reduced_ if it is reduced at every point.
Recall that a ring $A$ is said to be _regular_ if each local ring $A_{\mathfrak{p}}$ ($\mathfrak{p}$ ranging over the
prime ideals of $A$) is a regular local ring; we say that a sheaf of rings $\mathcal{A}$ on $X$ is _regular at a point_
$x$ (resp. _regular_) if the stalk $\mathcal{A}_{x}$ is a regular ring (resp. if $\mathcal{A}$ is regular at every
point). Finally, we say that $\mathcal{A}$ is _normal at a point_ $x$ (resp. _normal_) if $\mathcal{A}_{x}$ is _integral
and integrally closed_ (resp. if $\mathcal{A}$ is normal at every point). A ringed space $(X, \mathcal{A})$ has one of
these properties if $\mathcal{A}$ does.

A sheaf of _graded rings_ $\mathcal{A}$ is by definition a sheaf of rings that is the direct sum (G, II, 2.7) of a
family $(\mathcal{A}_{n})_{n \in \mathbb{Z}}$ of sheaves of abelian groups with $\mathcal{A}_{m} \cdot \mathcal{A}_{n}
\subset \mathcal{A}_{m+n}$. A _graded_ $\mathcal{A}$-_Module_ is an $\mathcal{A}$-Module $\mathcal{F}$ that is a direct
sum of a family $(\mathcal{F}_{n})_{n \in \mathbb{Z}}$ of sheaves of abelian groups satisfying $\mathcal{A}_{m} \cdot
\mathcal{F}_{n} \subset \mathcal{F}_{m+n}$. Equivalently, $(\mathcal{A}_{m})_{x} (\mathcal{A}_{n})_{x} \subset
(\mathcal{A}_{m+n})_{x}$ (resp. $(\mathcal{A}_{m})_{x} (\mathcal{F}_{n})_{x} \subset (\mathcal{F}_{m+n})_{x}$) at every
point $x$.

**(4.1.5)** For a ringed space $(X, \mathcal{A})$ (not necessarily commutative), we shall not recall the definitions of
the bifunctors $\mathcal{F} \otimes_{\mathcal{A}} \mathcal{G}$, $\mathcal{H}om_{\mathcal{A}}(\mathcal{F}, \mathcal{G})$,
and $\operatorname{Hom}_{\mathcal{A}}(\mathcal{F}, \mathcal{G})$ (G, II, 2.8 and 2.2) on the categories of left or right
$\mathcal{A}$-Modules (as the case may be), with values in the category of sheaves of abelian groups (or more generally
$\mathcal{C}$-Modules, where $\mathcal{C}$ is the center of $\mathcal{A}$). The stalk $(\mathcal{F}
\otimes_{\mathcal{A}} \mathcal{G})_{x}$ at any $x \in X$ is canonically identified with $\mathcal{F}_{x}
\otimes_{\mathcal{A}_{x}} \mathcal{G}_{x}$, and there is a canonical functorial homomorphism
$(\mathcal{H}om_{\mathcal{A}}(\mathcal{F}, \mathcal{G}))_{x} \to \operatorname{Hom}_{\mathcal{A}_{x}}(\mathcal{F}_{x},
\mathcal{G}_{x})$ which in general is neither injective nor surjective. The bifunctors above are additive and in
particular commute with finite direct sums; $\mathcal{F} \otimes_{\mathcal{A}} \mathcal{G}$ is right exact in
$\mathcal{F}$ and in $\mathcal{G}$, commutes with inductive limits, and $\mathcal{A} \otimes \mathcal{G}$ (resp.
$\mathcal{F} \otimes_{\mathcal{A}} \mathcal{A}$) is canonically identified with $\mathcal{G}$ (resp. $\mathcal{F}$). The
functors $\mathcal{H}om_{\mathcal{A}}(\mathcal{F}, \mathcal{G})$ and $\operatorname{Hom}_{\mathcal{A}}(\mathcal{F},
\mathcal{G})$ are _left exact_ in $\mathcal{F}$ and $\mathcal{G}$; precisely, given an exact sequence $0 \to
\mathcal{G}' \to \mathcal{G} \to \mathcal{G}''$, the sequence

```
0 → ℋom_𝒜(ℱ, 𝒢′) → ℋom_𝒜(ℱ, 𝒢) → ℋom_𝒜(ℱ, 𝒢″)
```

is exact; given an exact sequence $\mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$, the sequence

```
0 → ℋom_𝒜(ℱ″, 𝒢) → ℋom_𝒜(ℱ, 𝒢) → ℋom_𝒜(ℱ′, 𝒢)
```

is exact; analogous properties hold for `Hom`. Moreover, $\mathcal{H}om_{\mathcal{A}}(\mathcal{A}, \mathcal{G})$ is
canonically identified with $\mathcal{G}$; finally, for every open $U \subset X$,

```
Γ(U, ℋom_𝒜(ℱ, 𝒢)) = Hom_{𝒜|U}(ℱ|U, 𝒢|U).
```

For any left (resp. right) $\mathcal{A}$-Module $\mathcal{F}$, the _dual_ of $\mathcal{F}$, written
$\check{\mathcal{F}}$, is the right (resp. left) $\mathcal{A}$-Module $\mathcal{H}om_{\mathcal{A}}(\mathcal{F},
\mathcal{A})$.

Finally, if $\mathcal{A}$ is a sheaf of commutative rings and $\mathcal{F}$ is an $\mathcal{A}$-Module, then $U \mapsto
\bigwedge^{p} \Gamma(U, \mathcal{F})$ is a presheaf whose associated sheaf is an $\mathcal{A}$-Module written
$\bigwedge^{p} \mathcal{F}$, called the _$p$-th exterior power of_ $\mathcal{F}$. One checks easily that the canonical
map of the presheaf $U \mapsto \bigwedge^{p} \Gamma(U, \mathcal{F})$ into $\bigwedge^{p} \mathcal{F}$ is _injective_,
and that for every $x \in X$, $(\bigwedge^{p} \mathcal{F})_{x} = \bigwedge^{p} (\mathcal{F}_{x})$. Plainly
$\bigwedge^{p} \mathcal{F}$ is a covariant functor in $\mathcal{F}$.

**(4.1.6)** Suppose $\mathcal{A}$ is a sheaf of rings not necessarily commutative, $\mathcal{J}$ a sheaf of left ideals
of $\mathcal{A}$, and $\mathcal{F}$ a left $\mathcal{A}$-Module. We write $\mathcal{JF}$ for the
sub-$\mathcal{A}$-Module of $\mathcal{F}$ that is the image of $\mathcal{J} \otimes_{\mathbb{Z}} \mathcal{F}$ (where
$\mathbb{Z}$ is the sheaf associated with the constant presheaf $U \mapsto \mathbb{Z}$) under the canonical map
$\mathcal{J} \otimes_{\mathbb{Z}} \mathcal{F} \to \mathcal{F}$; plainly $(\mathcal{JF})_{x} = \mathcal{J}_{x}
\mathcal{F}_{x}$ for every $x \in X$. When $\mathcal{A}$ is commutative, $\mathcal{JF}$ is also the canonical image of
$\mathcal{J} \otimes_{\mathcal{A}} \mathcal{F} \to \mathcal{F}$. It is immediate that $\mathcal{JF}$ is also the
$\mathcal{A}$-Module associated with the presheaf $U \mapsto \Gamma(U, \mathcal{J}) \Gamma(U, \mathcal{F})$. If
$\mathcal{J}_{1}, \mathcal{J}_{2}$ are two sheaves of left ideals, then $\mathcal{J}_{1}(\mathcal{J}_{2} \mathcal{F}) =
(\mathcal{J}_{1} \mathcal{J}_{2}) \mathcal{F}$.

**(4.1.7)** Let $(X_{\lambda}, \mathcal{A}_{\lambda})_{\lambda \in L}$ be a family of ringed spaces; for each pair
$(\lambda, \mu)$, suppose given an open subset $V_{\mu \lambda} \subset X_{\lambda}$ and an isomorphism of ringed spaces
$\phi_{\lambda \mu} : (V_{\mu \lambda}, \mathcal{A}_{\mu}|V_{\mu \lambda}) \xrightarrow{\sim} (V_{\lambda \mu},
\mathcal{A}_{\lambda}|V_{\lambda \mu})$, with $V_{\lambda \lambda} = X_{\lambda}$ and $\phi_{\lambda \lambda}$ the
identity. Suppose moreover that for every triple $(\lambda, \mu, \nu)$, writing $\phi'_{\lambda \mu}$ for the
restriction of $\phi_{\lambda \mu}$ to $V_{\mu \lambda} \cap V_{\mu \nu}$, the map $\phi'_{\lambda \mu}$ is an
isomorphism of $(V_{\mu \lambda} \cap V_{\mu \nu}, \mathcal{A}_{\mu}|(V_{\mu \lambda} \cap V_{\mu \nu}))$ onto
$(V_{\lambda \mu} \cap V_{\lambda \nu}, \mathcal{A}_{\lambda}|(V_{\lambda \mu} \cap V_{\lambda \nu}))$, and that
$\phi'_{\lambda \nu} = \phi'_{\lambda \mu} \circ \phi'_{\mu \nu}$ (_gluing condition_ for the $\phi_{\lambda \mu}$). One
first forms the topological space obtained by gluing the $X_{\lambda}$ along the $V_{\lambda \mu}$ via the
$\phi_{\lambda \mu}$; identifying $X_{\lambda}$ with the open subset $X'_{\lambda}$ of $X$, the hypotheses imply that
the three subsets $V_{\lambda \mu} \cap V_{\lambda \nu}$, $V_{\mu \nu} \cap V_{\mu \lambda}$, $V_{\nu \lambda} \cap
V_{\nu \mu}$ are identified with $X'_{\lambda} \cap X'_{\mu} \cap X'_{\nu}$. One then transports the ringed-space
structure of $X_{\lambda}$ to $X'_{\lambda}$; the resulting $\mathcal{A}'_{\lambda}$ satisfy the gluing condition
(3.3.1) and hence define a sheaf of rings $\mathcal{A}$ on $X$. One says that $(X, \mathcal{A})$ is the ringed space
obtained by _gluing_ the $(X_{\lambda}, \mathcal{A}_{\lambda})$ along the $V_{\lambda \mu}$ via the $\phi_{\lambda
\mu}$.

### 4.2. Direct image of an $\mathcal{A}$-Module

<!-- label: 0.4.2 -->

**(4.2.1)** Let $(X, \mathcal{A})$, $(Y, \mathcal{B})$ be two ringed spaces and $\Psi = (\psi, \theta)$ a morphism $(X,
\mathcal{A}) \to (Y, \mathcal{B})$. Then $\psi_{*}(\mathcal{A})$ is a sheaf of rings on $Y$ and $\theta : \mathcal{B}
\to \psi_{*}(\mathcal{A})$ is a sheaf-of-rings homomorphism. Let $\mathcal{F}$ be an $\mathcal{A}$-Module; its direct
image $\psi_{*}(\mathcal{F})$ is a sheaf of abelian groups on $Y$. Moreover, for every open $U \subset Y$,

```
Γ(U, ψ_*(ℱ)) = Γ(ψ⁻¹(U), ℱ)
```

is equipped with a module structure over the ring $\Gamma(U, \psi_{*}(\mathcal{A})) = \Gamma(\psi^{-1}(U),
\mathcal{A})$; the bilinear maps defining these structures are compatible with restriction, giving
$\psi_{*}(\mathcal{F})$ a structure of $\psi_{*}(\mathcal{A})$-Module. The homomorphism $\theta : \mathcal{B} \to
\psi_{*}(\mathcal{A})$ then equips $\psi_{*}(\mathcal{F})$ with a $\mathcal{B}$-Module structure as well; this
$\mathcal{B}$-Module is called the _direct image of_ $\mathcal{F}$ _by_ $\Psi$ and is written $\Psi_{*}(\mathcal{F})$.
If $\mathcal{F}_{1}, \mathcal{F}_{2}$ are two $\mathcal{A}$-Modules on $X$ and $u : \mathcal{F}_{1} \to \mathcal{F}_{2}$
is an $\mathcal{A}$-homomorphism, it is immediate (considering sections over open subsets of $Y$) that $\psi_{*}(u)$ is
a $\psi_{*}(\mathcal{A})$-homomorphism $\psi_{*}(\mathcal{F}_{1}) \to \psi_{*}(\mathcal{F}_{2})$, and _a fortiori_ a
$\mathcal{B}$-homomorphism $\Psi_{*}(\mathcal{F}_{1}) \to \Psi_{*}(\mathcal{F}_{2})$; as such, it is written
$\Psi_{*}(u)$. Thus $\Psi_{*}$ is a _covariant functor_ from $\mathcal{A}$-Modules to $\mathcal{B}$-Modules; it is _left
exact_ (G, II, 2.12).

On $\psi_{*}(\mathcal{A})$, the $\mathcal{B}$-Module structure together with the sheaf-of-rings structure gives a
structure of $\mathcal{B}$-Algebra; this $\mathcal{B}$-Algebra is written $\Psi_{*}(\mathcal{A})$.

**(4.2.2)** Let $\mathcal{M}$, $\mathcal{N}$ be two $\mathcal{A}$-Modules. For every open $U \subset Y$, there is a
canonical map

```
Γ(ψ⁻¹(U), ℳ) × Γ(ψ⁻¹(U), 𝒩) → Γ(ψ⁻¹(U), ℳ ⊗_𝒜 𝒩)
```

which is bilinear over $\Gamma(\psi^{-1}(U), \mathcal{A}) = \Gamma(U, \psi_{*}(\mathcal{A}))$, and _a fortiori_ over
$\Gamma(U, \mathcal{B})$; it defines a homomorphism

```
Γ(U, Ψ_*(ℳ)) ⊗_{Γ(U, ℬ)} Γ(U, Ψ_*(𝒩)) → Γ(U, Ψ_*(ℳ ⊗_𝒜 𝒩))
```

which is compatible with restriction; the result is a canonical functorial homomorphism of $\mathcal{B}$-Modules

```
(4.2.2.1)    Ψ_*(ℳ) ⊗_ℬ Ψ_*(𝒩) → Ψ_*(ℳ ⊗_𝒜 𝒩),
```

in general neither injective nor surjective. If $\mathcal{P}$ is a third $\mathcal{A}$-Module, the diagram

```
(4.2.2.2)    Ψ_*(ℳ) ⊗_ℬ Ψ_*(𝒩) ⊗_ℬ Ψ_*(𝒫) → Ψ_*(ℳ ⊗_𝒜 𝒩) ⊗_ℬ Ψ_*(𝒫)
                        │                                    │
                        ↓                                    ↓
             Ψ_*(ℳ) ⊗_ℬ Ψ_*(𝒩 ⊗_𝒜 𝒫) ─────────────→  Ψ_*(ℳ ⊗_𝒜 𝒩 ⊗_𝒜 𝒫)
```

commutes.

**(4.2.3)** Let $\mathcal{M}$, $\mathcal{N}$ be two $\mathcal{A}$-Modules. For every open $U \subset Y$, by definition
$\Gamma(\psi^{-1}(U), \mathcal{H}om_{\mathcal{A}}(\mathcal{M}, \mathcal{N})) =
\operatorname{Hom}_{\mathcal{A}|V}(\mathcal{M}|V, \mathcal{N}|V)$ with $V = \psi^{-1}(U)$. The map $u \mapsto
\psi_{*}(u)$ is a homomorphism

```
Hom_{𝒜|V}(ℳ|V, 𝒩|V) → Hom_{ℬ|U}(Ψ_*(ℳ)|U, Ψ_*(𝒩)|U)
```

for the $\Gamma(U, \mathcal{B})$-module structures. These homomorphisms are compatible with restriction, so they define
a canonical functorial homomorphism of $\mathcal{B}$-Modules

```
(4.2.3.1)    Ψ_*(ℋom_𝒜(ℳ, 𝒩)) → ℋom_ℬ(Ψ_*(ℳ), Ψ_*(𝒩)).
```

**(4.2.4)** If $\mathcal{C}$ is an $\mathcal{A}$-Algebra, the composite

```
Ψ_*(𝒞) ⊗_ℬ Ψ_*(𝒞) → Ψ_*(𝒞 ⊗_𝒜 𝒞) → Ψ_*(𝒞)
```

equips $\Psi_{*}(\mathcal{C})$ with a $\mathcal{B}$-Algebra structure, by (4.2.2.2). Similarly, if $\mathcal{M}$ is a
$\mathcal{C}$-Module, $\Psi_{*}(\mathcal{M})$ is canonically equipped with a $\Psi_{*}(\mathcal{C})$-Module structure.

**(4.2.5)** Consider the special case in which $X$ is a _closed_ subspace of $Y$ and $\psi$ is the canonical injection
$j : X \to Y$. Let $\mathcal{B}' = \mathcal{B}|X = j*(\mathcal{B})$ be the restriction of the sheaf of rings
$\mathcal{B}$ to $X$; an $\mathcal{A}$-Module $\mathcal{M}$ may be viewed as a $\mathcal{B}'$-Module via
$\theta^{\sharp} : \mathcal{B}' \to \mathcal{A}$. Then $\Psi_{*}(\mathcal{M})$ is the $\mathcal{B}$-Module that induces
$\mathcal{M}$ on $X$ and `0` elsewhere. If $\mathcal{N}$ is a second $\mathcal{A}$-Module, $\Psi_{*}(\mathcal{M})
\otimes_{\mathcal{B}} \Psi_{*}(\mathcal{N})$ is identified with $\Psi_{*}(\mathcal{M} \otimes_{\mathcal{B}'}
\mathcal{N})$, and $\mathcal{H}om_{\mathcal{B}}(\Psi_{*}(\mathcal{M}), \Psi_{*}(\mathcal{N}))$ with
$\Psi_{*}(\mathcal{H}om_{\mathcal{B}'}(\mathcal{M}, \mathcal{N}))$.

**(4.2.6)** Let $(Z, \mathcal{C})$ be a third ringed space and $\Psi' = (\psi', \theta') : (Y, \mathcal{B}) \to (Z,
\mathcal{C})$ a morphism; if $\Psi'' = \Psi' \circ \Psi$, then plainly $\Psi''_{*} = \Psi'_{*} \circ \Psi_{*}$.

### 4.3. Inverse image of a $\mathcal{B}$-Module

<!-- label: 0.4.3 -->

**(4.3.1)** Under the hypotheses and notation of (4.2.1), let $\mathcal{G}$ be a $\mathcal{B}$-Module and
$\psi*(\mathcal{G})$ its inverse image (3.7.1) — a sheaf of abelian groups on $X$. The construction of sections of
$\psi*(\mathcal{G})$ and $\psi*(\mathcal{B})$ (3.7.1) shows that $\psi*(\mathcal{G})$ is canonically a
$\psi*(\mathcal{B})$-Module. The homomorphism $\theta^{\sharp} : \psi*(\mathcal{B}) \to \mathcal{A}$ makes $\mathcal{A}$
a $\psi*(\mathcal{B})$-Module, written $\mathcal{A}_{[\theta]}$ when confusion threatens; the tensor product
$\psi*(\mathcal{G}) \otimes_{\psi*(\mathcal{B})} \mathcal{A}_{[\theta]}$ is then an $\mathcal{A}$-Module. We call this
$\mathcal{A}$-Module the _inverse image of_ $\mathcal{G}$ _by_ $\Psi$ and write it $\Psi*(\mathcal{G})$. If
$\mathcal{G}_{1}, \mathcal{G}_{2}$ are $\mathcal{B}$-Modules and $v : \mathcal{G}_{1} \to \mathcal{G}_{2}$ is a
$\mathcal{B}$-homomorphism, one checks at once that $v$ is a $\psi*(\mathcal{B})$-homomorphism $\psi*(\mathcal{G}_{1})
\to \psi*(\mathcal{G}_{2})$; hence $\psi*(v) \otimes 1$ is an $\mathcal{A}$-homomorphism $\Psi*(\mathcal{G}_{1}) \to
\Psi*(\mathcal{G}_{2})$, written $\Psi*(v)$. Thus $\Psi*$ is a _covariant functor_ from $\mathcal{B}$-Modules to
$\mathcal{A}$-Modules. Unlike $\psi*$, this functor is not exact in general but only _right exact_, tensoring with
$\mathcal{A}$ being a right-exact functor on $\psi*(\mathcal{B})$-Modules.

For every $x \in X$, by (3.7.2),

```
(Ψ*(𝒢))_x = 𝒢_{ψ(x)} ⊗_{ℬ_{ψ(x)}} 𝒜_x.
```

The support of $\Psi*(\mathcal{G})$ is therefore contained in $\psi^{-1}(Supp(\mathcal{G}))$.

**(4.3.2)** Let $(\mathcal{G}_{\lambda})$ be an inductive system of $\mathcal{B}$-Modules with $\mathcal{G} = \varinjlim
\mathcal{G}_{\lambda}$. The canonical homomorphisms $\mathcal{G}_{\lambda} \to \mathcal{G}$ give
$\psi*(\mathcal{B})$-homomorphisms $\psi*(\mathcal{G}_{\lambda}) \to \psi*(\mathcal{G})$, and so a canonical
homomorphism $\varinjlim \psi*(\mathcal{G}_{\lambda}) \to \psi*(\mathcal{G})$. Since the stalk of an inductive limit of
sheaves is the inductive limit of stalks (G, II, 1.11), this map is _bijective_ (3.7.2). Tensor product also commutes
with inductive limits, so there is a _canonical functorial isomorphism_ of $\mathcal{A}$-Modules

```
lim⃗ Ψ*(𝒢_λ) ⥲ Ψ*(lim⃗ 𝒢_λ).
```

For a finite direct sum $\oplus_{i} \mathcal{G}_{i}$ of $\mathcal{B}$-Modules, plainly $\psi*(\oplus_{i}
\mathcal{G}_{i}) = \oplus_{i} \psi*(\mathcal{G}_{i})$, so tensoring with $\mathcal{A}_{[\theta]}$ gives

```
(4.3.2.1)    Ψ*(⊕_i 𝒢_i) = ⊕_i Ψ*(𝒢_i).
```

By passage to inductive limit, the equality extends to arbitrary direct sums.

**(4.3.3)** Let $\mathcal{G}_{1}, \mathcal{G}_{2}$ be $\mathcal{B}$-Modules. From the construction of inverse images of
sheaves of abelian groups (3.7.1) one obtains at once a canonical homomorphism

```
ψ*(𝒢_1) ⊗_{ψ*(ℬ)} ψ*(𝒢_2) → ψ*(𝒢_1 ⊗_ℬ 𝒢_2)
```

of $\psi*(\mathcal{B})$-Modules; since the stalk of a tensor product of sheaves is the tensor product of stalks (G, II,
2.8), (3.7.2) shows that this map is an _isomorphism_. Tensoring with $\mathcal{A}$ gives a canonical functorial
isomorphism

```
(4.3.3.1)    Ψ*(𝒢_1) ⊗_𝒜 Ψ*(𝒢_2) ⥲ Ψ*(𝒢_1 ⊗_ℬ 𝒢_2).
```

**(4.3.4)** Let $\mathcal{C}$ be a $\mathcal{B}$-Algebra; giving $\mathcal{C}$ an algebra structure amounts to giving a
$\mathcal{B}$-homomorphism $\mathcal{C} \otimes_{\mathcal{B}} \mathcal{C} \to \mathcal{C}$ satisfying associativity and
commutativity (verified stalkwise). The isomorphism above transports this into an $\mathcal{A}$-Module homomorphism
$\Psi*(\mathcal{C}) \otimes_{\mathcal{A}} \Psi*(\mathcal{C}) \to \Psi*(\mathcal{C})$ with the same properties, equipping
$\Psi*(\mathcal{C})$ with an $\mathcal{A}$-Algebra structure. In particular, the $\mathcal{A}$-Algebra
$\Psi*(\mathcal{B})$ is equal to $\mathcal{A}$ (up to canonical isomorphism).

Similarly, if $\mathcal{M}$ is a $\mathcal{C}$-Module, giving the module structure amounts to a
$\mathcal{B}$-homomorphism $\mathcal{C} \otimes_{\mathcal{B}} \mathcal{M} \to \mathcal{M}$ satisfying associativity;
transport gives a $\Psi*(\mathcal{C})$-Module structure on $\Psi*(\mathcal{M})$.

**(4.3.5)** Let $\mathcal{J}$ be a sheaf of ideals of $\mathcal{B}$; since $\psi*$ is exact, the
$\psi*(\mathcal{B})$-Module $\psi*(\mathcal{J})$ is canonically identified with a sheaf of ideals of
$\psi*(\mathcal{B})$. The canonical injection $\psi*(\mathcal{J}) \to \psi*(\mathcal{B})$ then gives an
$\mathcal{A}$-Module homomorphism $\Psi*(\mathcal{J}) = \psi*(\mathcal{J}) \otimes_{\psi*(\mathcal{B})}
\mathcal{A}_{[\theta]} \to \mathcal{A}$; we write $\Psi*(\mathcal{J}) \cdot \mathcal{A}$, or $\mathcal{JA}$ when no
confusion threatens, for the image of $\Psi*(\mathcal{J})$ under this map. Thus by definition $\mathcal{JA} =
\theta^{\sharp}(\psi*(\mathcal{J})) \cdot \mathcal{A}$, and in particular $(\mathcal{JA})_{x} =
\theta^{\sharp}_{x}(\mathcal{J}_{\psi(x)}) \cdot \mathcal{A}_{x}$ using the canonical identification of stalks of
$\psi*(\mathcal{J})$ with those of $\mathcal{J}$ (3.7.2). If $\mathcal{J}_{1}, \mathcal{J}_{2}$ are two ideals of
$\mathcal{B}$, $(\mathcal{J}_{1} \mathcal{J}_{2}) \mathcal{A} = \mathcal{J}_{1}(\mathcal{J}_{2} \mathcal{A}) =
(\mathcal{J}_{1} \mathcal{A})(\mathcal{J}_{2} \mathcal{A})$. For an $\mathcal{A}$-Module $\mathcal{F}$, set
$\mathcal{JF} = (\mathcal{JA}) \mathcal{F}$.

**(4.3.6)** Let $(Z, \mathcal{C})$ be a third ringed space and $\Psi' = (\psi', \theta') : (Y, \mathcal{B}) \to (Z,
\mathcal{C})$ a morphism. If $\Psi'' = \Psi' \circ \Psi$, then by the definition (4.3.1) and (4.3.3.1), $\Psi''* = \Psi*
\circ \Psi'*$.

### 4.4. Relations between direct and inverse images

<!-- label: 0.4.4 -->

**(4.4.1)** Under the hypotheses and notation of (4.2.1), let $\mathcal{G}$ be a $\mathcal{B}$-Module. A
$\mathcal{B}$-Module homomorphism $u : \mathcal{G} \to \Psi_{*}(\mathcal{F})$ is also called a $\Psi$-_homomorphism_ of
$\mathcal{G}$ into $\mathcal{F}$ — or simply a _homomorphism of $\mathcal{G}$ into $\mathcal{F}$_, written $u :
\mathcal{G} \to \mathcal{F}$, when no confusion threatens. To give such a homomorphism is to give, for every pair $(U,
V)$ with $U \subset X$ open, $V \subset Y$ open, $\psi(U) \subset V$, a homomorphism $u_{U,V} : \Gamma(V, \mathcal{G})
\to \Gamma(U, \mathcal{F})$ of $\Gamma(V, \mathcal{B})$-modules — $\Gamma(U, \mathcal{F})$ viewed as a $\Gamma(V,
\mathcal{B})$-module via $\theta_{U,V} : \Gamma(V, \mathcal{B}) \to \Gamma(U, \mathcal{A})$ — with the $u_{U,V}$ making
the diagrams (3.5.1.1) commute. It suffices to give the $u_{U,V}$ for $U$ (resp. $V$) ranging over a basis
$\mathfrak{B}$ of the topology of $X$ (resp. $\mathfrak{B}'$ of $Y$), provided one checks (3.5.1.1) for those
restrictions.

**(4.4.2)** Under the hypotheses of (4.2.1) and (4.2.6), let $\mathcal{H}$ be a $\mathcal{C}$-Module and $v :
\mathcal{H} \to \Psi'_{*}(\mathcal{G})$ a $\Psi'$-morphism; then

```
w : ℋ ──v──→ Ψ′_*(𝒢) ──Ψ′_*(u)──→ Ψ′_*(Ψ_*(ℱ))
```

is a $\Psi''$-morphism, called the _composite_ of $u$ and $v$.

**(4.4.3)** We now show that there is a _canonical isomorphism of bifunctors in_ $\mathcal{F}$ _and_ $\mathcal{G}$

```
(4.4.3.1)    Hom_𝒜(Ψ*(𝒢), ℱ) ⥲ Hom_ℬ(𝒢, Ψ_*(ℱ)),
```

written $v \mapsto v^{\flat}$ (or simply $v \mapsto v^{\flat}$); the inverse is written $u \mapsto u^{\sharp}$. The
definition is as follows: composing $v : \Psi*(\mathcal{G}) \to \mathcal{F}$ with the canonical map $\psi*(\mathcal{G})
\to \Psi*(\mathcal{G})$ gives a sheaf-of-groups homomorphism $v' : \psi*(\mathcal{G}) \to \mathcal{F}$, which is also a
$\psi*(\mathcal{B})$-module homomorphism. From it (3.7.1) one deduces a homomorphism $v'^{\flat} : \mathcal{G} \to
\psi_{*}(\mathcal{F}) = \Psi_{*}(\mathcal{F})$, also a $\mathcal{B}$-Module homomorphism (as one checks); set $v^{\flat}
= v'^{\flat}$. Similarly, from $u : \mathcal{G} \to \Psi_{*}(\mathcal{F})$ one deduces (3.7.1) a
$\psi*(\mathcal{B})$-Module homomorphism $u^{\sharp} : \psi*(\mathcal{G}) \to \mathcal{F}$, and by tensoring with
$\mathcal{A}$ an $\mathcal{A}$-Module homomorphism $\Psi*(\mathcal{G}) \to \mathcal{F}$, which we write $u^{\sharp}$.
One verifies at once that $(u^{\sharp})^{\flat} = u$ and $(v^{\flat})^{\sharp} = v$, and the functoriality in
$\mathcal{F}$ of $v \mapsto v^{\flat}$. The functoriality in $\mathcal{G}$ of $u \mapsto u^{\sharp}$ then follows
formally as in (3.5.4) (this reasoning would also give the functoriality of $\Psi*$ established directly in (4.3.1)).

Taking $v$ to be the identity of $\Psi*(\mathcal{G})$, $v^{\flat}$ is a homomorphism

$$ (4.4.3.2) \rho_{\mathcal{G}} : \mathcal{G} \to \Psi_{*}(\Psi*(\mathcal{G})); $$

taking $u$ to be the identity of $\Psi_{*}(\mathcal{F})$, $u^{\sharp}$ is a homomorphism

$$ (4.4.3.3) \sigma_{\mathcal{F}} : \Psi*(\Psi_{*}(\mathcal{F})) \to \mathcal{F}; $$

these will be called _canonical_. In general they are neither injective nor surjective. Canonical factorizations
analogous to (3.5.3.3) and (3.5.4.4) hold.

Note that if $s$ is a section of $\mathcal{G}$ over an open $V \subset Y$, then $\rho_{\mathcal{G}}(s)$ is the section
$s' \otimes 1$ of $\Psi*(\mathcal{G})$ over $\psi^{-1}(V)$, where $s'_{x} = s_{\psi(x)}$ for $x \in \psi^{-1}(V)$. Note
also that any homomorphism $u : \mathcal{G} \to \psi_{*}(\mathcal{F})$ defines for each $x \in X$ a stalk homomorphism
$u_{x} : \mathcal{G}_{\psi(x)} \to \mathcal{F}_{x}$, factoring through the canonical map $s_{x} \mapsto s_{x} \otimes 1$
of $\mathcal{G}_{\psi(x)}$ into $(\Psi*(\mathcal{G}))_{x} = \mathcal{G}_{\psi(x)} \otimes_{\mathcal{B}_{\psi(x)}}
\mathcal{A}_{x}$. The map $u_{x}$ is also the inductive limit of $\Gamma(V, \mathcal{G}) \xrightarrow{u}
\Gamma(\psi^{-1}(V), \mathcal{F}) \to \mathcal{F}_{x}$ over neighborhoods $V$ of $\psi(x)$.

**(4.4.4)** Let $\mathcal{F}_{1}, \mathcal{F}_{2}$ be $\mathcal{A}$-Modules and $\mathcal{G}_{1}, \mathcal{G}_{2}$ be
$\mathcal{B}$-Modules, with $u_{i} : \mathcal{G}_{i} \to \mathcal{F}_{i}$ a homomorphism ($i = 1, 2$). We write $u_{1}
\otimes u_{2}$ for the homomorphism $u : \mathcal{G}_{1} \otimes_{\mathcal{B}} \mathcal{G}_{2} \to \mathcal{F}_{1}
\otimes_{\mathcal{A}} \mathcal{F}_{2}$ with $u^{\sharp} = (u_{1})^{\sharp} \otimes (u_{2})^{\sharp}$ (using (4.3.3.1));
one checks that $u$ is also the composite

```
𝒢_1 ⊗_ℬ 𝒢_2 → Ψ_*(ℱ_1) ⊗_ℬ Ψ_*(ℱ_2) → Ψ_*(ℱ_1 ⊗_𝒜 ℱ_2),
```

where the first arrow is the ordinary tensor product $u_{1} \otimes u_{2}$ and the second is the canonical map
(4.2.2.1).

**(4.4.5)** Let $(\mathcal{G}_{\lambda})_{\lambda \in L}$ be an inductive system of $\mathcal{B}$-Modules, and for each
$\lambda$ let $u_{\lambda} : \mathcal{G}_{\lambda} \to \Psi_{*}(\mathcal{F})$ be a homomorphism, forming an inductive
system. Set $\mathcal{G} = \varinjlim \mathcal{G}_{\lambda}$ and $u = \varinjlim u_{\lambda}$; then the
$(u_{\lambda})^{\sharp}$ form an inductive system of homomorphisms $\Psi*(\mathcal{G}_{\lambda}) \to \mathcal{F}$, whose
inductive limit is $u^{\sharp}$.

**(4.4.6)** Let $\mathcal{M}$, $\mathcal{N}$ be $\mathcal{B}$-Modules, $V \subset Y$ open, $U = \psi^{-1}(V)$. The map
$v \mapsto \Psi*(v)$ is a homomorphism

```
Hom_{ℬ|V}(ℳ|V, 𝒩|V) → Hom_{𝒜|U}(Ψ*(ℳ)|U, Ψ*(𝒩)|U)
```

for the $\Gamma(V, \mathcal{B})$-module structures ($\operatorname{Hom}_{\mathcal{A}|U}(\Psi*(\mathcal{M})|U,
\Psi*(\mathcal{N})|U)$ is naturally a $\Gamma(U, \psi*(\mathcal{B}))$-module, hence a $\Gamma(V, \mathcal{B})$-module
via the canonical homomorphism $\Gamma(V, \mathcal{B}) \to \Gamma(U, \psi*(\mathcal{B}))$ of (3.7.2)). These
homomorphisms are compatible with restriction, so they define a canonical functorial homomorphism

```
γ : ℋom_ℬ(ℳ, 𝒩) → Ψ_*(ℋom_𝒜(Ψ*(ℳ), Ψ*(𝒩))),
```

corresponding to a homomorphism

```
γ^♯ : Ψ*(ℋom_ℬ(ℳ, 𝒩)) → ℋom_𝒜(Ψ*(ℳ), Ψ*(𝒩)),
```

both functorial in $\mathcal{M}$ and $\mathcal{N}$.

**(4.4.7)** Suppose $\mathcal{F}$ (resp. $\mathcal{G}$) is an $\mathcal{A}$-Algebra (resp. a $\mathcal{B}$-Algebra). If
$u : \mathcal{G} \to \Psi_{*}(\mathcal{F})$ is a $\mathcal{B}$-Algebra homomorphism, then $u^{\sharp} :
\Psi*(\mathcal{G}) \to \mathcal{F}$ is an $\mathcal{A}$-Algebra homomorphism; this follows from the commutativity of

```
𝒢 ⊗_ℬ 𝒢 ────────────→ 𝒢
    │                    │
    ↓                    ↓ u
Ψ_*(ℱ ⊗_𝒜 ℱ) ────→ Ψ_*(ℱ)
```

and (4.4.4). Similarly, if $v : \Psi*(\mathcal{G}) \to \mathcal{F}$ is an $\mathcal{A}$-Algebra homomorphism, then
$v^{\flat} : \mathcal{G} \to \Psi_{*}(\mathcal{F})$ is a $\mathcal{B}$-Algebra homomorphism.

**(4.4.8)** Let $(Z, \mathcal{C})$ be a third ringed space, $\Psi' = (\psi', \theta') : (Y, \mathcal{B}) \to (Z,
\mathcal{C})$ a morphism, and $\Psi'' = \Psi' \circ \Psi : (X, \mathcal{A}) \to (Z, \mathcal{C})$. Let $\mathcal{H}$ be
a $\mathcal{C}$-Module and $v' : \mathcal{H} \to \Psi'_{*}(\mathcal{G})$ a homomorphism. The composite $v'' = v \circ
v'$ is defined as the homomorphism

```
ℋ ──v′──→ Ψ′_*(𝒢) ──Ψ′_*(v)──→ Ψ′_*(Ψ_*(ℱ));
```

one checks that $v''^{\sharp}$ is

```
Ψ*(Ψ′*(ℋ)) ──Ψ*(v′^♯)──→ Ψ*(𝒢) ──v^♯──→ ℱ.
```

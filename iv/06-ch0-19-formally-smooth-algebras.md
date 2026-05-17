<!-- original page 165 -->

## §19. Formally smooth algebras and Cohen rings

### 19.0. Introduction

**(19.0.1)** In Chapter IV we shall introduce and study, among other things, an important class of morphisms of
preschemes, the *smooth* morphisms.[^1] One of their fundamental properties (which, together with a finiteness
condition, characterizes them) is a property of *lifting morphisms*: if `f : X → Y` is a smooth morphism, `g : Y' → Y` a
morphism, then for every morphism `h : Y'' → Y'` making `Y''` a prescheme "little different" from `Y'`, every
`Y`-morphism `Y'' → X` *factors as* `Y'' ─h→ Y' ─→ X`. More precisely, restricting ourselves to the case where
`Y = Spec(A)`, `X = Spec(B)` are affine, `B` is then called a *formally smooth `A`-algebra* if, for every `A`-algebra
`C` and every *nilpotent* ideal `𝔍` of `C`, every `A`-homomorphism `B → C/𝔍` lifts to `B → C → C/𝔍`. In other words, the
map

```text
                              Hom_A(B, C) → Hom_A(B, C/𝔍)
```

is surjective. In many applications `X` will appear as an object representing a representable contravariant functor
`Y' ↦ F(Y')` from the category of `Y`-preschemes into that of sets, so that one has `(0_III, 8.1.8)`
`F(Y') ≅ Hom_Y(Y', X)`. In the affine case, if one sets `F°(C) = F(Spec(C))`, the verification that, under the
conditions above, `F°(C) → F°(C/𝔍)` is surjective (which can be done even *without knowing* that `F` is representable)
will establish that `f` is smooth, provided the additional finiteness condition is satisfied.

**(19.0.2)** For *topological algebras* over a topological ring `A`, there is an analogous notion of *formally smooth*
algebra which we shall not make precise here (cf. `(19.3.1)`). The study of these notions is first carried out from an
elementary point of view in §19, then, by means of the properties of differentials which will be developed in §§20 and
21, more delicate theorems will be proved in §22. We summarize here the principal results on formally smooth algebras:

I. — Let `A`, `B` be two Noetherian local rings, `φ : A → B` a local homomorphism, `k` the residue field of `A`, and let
`B_0 = B ⊗_A k`; equip `A`, `B` with their preadic topologies and `k` with the discrete topology. Then, for `B` to be a
formally smooth `A`-algebra, it is necessary and sufficient that `B` be a *flat* `A`-module and that `B_0` be a formally
smooth `k`-algebra `(19.7.1)`. This theorem thus reduces formal smoothness, for Noetherian local rings, to the same
question for Noetherian local rings which are algebras over a *field*.

II. — Let `k` be a field, `A` a Noetherian local ring which is a `k`-algebra. For `A` to be formally smooth, it is
necessary and sufficient that `A` be *geometrically regular* over `k`, that is, that for every *finite* extension `k'`
of `k`, the semi-local ring `A ⊗_k k'` be

<!-- original page 166 -->

regular `(22.5.8)`; the completion `Â` of `A` is then a ring isomorphic to a formal power series ring `K[[T_1, …, T_n]]`
`(19.6.5)`. Moreover, the structure of `k`-algebra of `Â`, when `A` is assumed to be *complete* and formally smooth over
`k`, is entirely determined by the residue field `K` of `A` and by the dimension of `A`; the latter can moreover be
arbitrary provided it satisfies the inequality `dim(A) ⩾ rg_K(Υ_{K/k})`, where `Υ_{K/k}` is the "imperfection module" of
`K` `(22.2.6)`.

In particular, for an extension `K` of `k` to be formally smooth, it is necessary and sufficient that `K` be a
*separable* extension of `k` `(19.6.1)`.

III. — Let `A` be a Noetherian local ring, `𝔍` an ideal of `A` distinct from `A`, `A_0 = A/𝔍`, `B_0` a *complete*
Noetherian local ring, `A_0 → B_0` a local homomorphism making `B_0` a formally smooth `A_0`-algebra. Then there exists
a complete Noetherian local ring `B`, a local homomorphism `A → B` making `B` a flat `A`-module, and an
`A_0`-isomorphism `B ⊗_A A_0 ≅ B_0` (so that, by I, `B` is a *formally smooth* `A`-algebra); furthermore `B` is
determined by these properties up to isomorphism `(19.7.2)`. This theorem contains in particular the *theorems of Cohen*
on the structure of complete Noetherian local rings `(19.8)`, which will play an important role in §§6 and 7 of Chapter
IV.

IV. — The interest of the study of formally smooth Noetherian local rings over another arises from the following
"pointwise" characterization of smooth morphisms: if `X` and `Y` are locally Noetherian preschemes, `f : X → Y` a
morphism locally of finite type, then, for `f` to be smooth, it is necessary and sufficient that for every `x ∈ X`, the
ring `𝒪_x` be formally smooth over `𝒪_{f(x)}`. In particular, if `Y = Spec(k)`, where `k` is a *perfect* field, to say
that `f` is smooth is equivalent to saying that `X` is a *regular* prescheme.

V. — Finally, we shall see in §§20, 21, and 22 that the notion of formally smooth algebra arises naturally in the theory
of *Kähler differentials*, the two theories illuminating each other.

**(19.0.3)** In all this section and the following ones, the topological rings and modules will be assumed to be
*linearly topologized* `(0_I, 7.1.1)`; the topological rings considered will be assumed *commutative*, except when
explicitly stated otherwise. Recall that if `A` and `B` are two topological rings, `ρ : A → B` a ring homomorphism
defining on `B` a structure of `A`-algebra, one says that `B` is a *topological `A`-algebra* if `ρ` is continuous for
the topologies in question.

To abbreviate, in a topological ring `A` (resp. a topological `A`-module `M`), we shall say "fundamental system of
*open* ideals (resp. submodules)" instead of "fundamental system of neighbourhoods of `0` formed of ideals (resp.
submodules)".

Given a topological ring `A` and an `A`-module `M`, the sets `𝔍M`, where `𝔍` runs through a fundamental system of open
ideals, form a fundamental system of open submodules for a topology on `M` making `M` a topological `A`-module, which is
said to be *deduced from the topology of `A`*.

Let `M` be a topological `A`-module whose topology is *coarser* than the topology deduced from that of `A`; then, if `N`
is an open submodule of `M`, the discrete `A`-module `M/N` is annulled by an open ideal of `A`, for by hypothesis there
exists such an ideal `𝔎` with `𝔎 · M ⊂ N`.

<!-- original page 167 -->

If `M` and `N` are two topological `A`-modules whose topologies are both deduced from that of `A`, then *every*
`A`-homomorphism `u : M → N` is *continuous*, for, for every neighbourhood `V` of `0` in `N`, there exists by hypothesis
an open ideal `𝔍` of `A` such that `𝔍N ⊂ V`, and one therefore has `u(𝔍M) ⊂ 𝔍N ⊂ V`.

When `B` is a topological `A`-algebra, the topology on `B` *deduced* from that of `A` is *finer* than the given
topology, for, for every open ideal `𝔎` of `B`, there is by hypothesis an open ideal `𝔍` of `A` such that `𝔍B ⊂ 𝔎`.

### 19.1. Formal epimorphisms and monomorphisms

**Proposition (19.1.1).**

<!-- label: 0_IV.19.1.1 -->

*Let `A` be a topological ring, `M`, `N` two topological `A`-modules, `(W_λ)` a fundamental system of open submodules of
`N`, `u : M → N` a continuous `A`-homomorphism, `M̂`, `N̂` the separated completions of `M` and `N`, `û : M̂ → N̂` the
continuous extension of `u` to the separated completions.*

*(i) The following conditions are equivalent:*

*a) `u(M)` is dense in `N`.*

*a') `û(M̂)` is dense in `N̂`.*

*a") For every `λ`, the composite homomorphism `M ─u→ N → N/W_λ` is surjective.*

*(ii) The following conditions are equivalent:*

*b) The inverse image by `u` of the topology of `N` is equal to the topology of `M`.*

*b') `û` is an isomorphism of the topological `Â`-module `M̂` onto the topological sub-`Â`-module `û(M̂)` of `N̂` (which
is necessarily closed).*

*b") The `u⁻¹(W_λ)` form a fundamental system of neighbourhoods of `0` in `M`.*

This follows immediately from the definition of the separated completions and from the fact that `N/W_λ` is discrete.

**(19.1.2)** When the equivalent conditions of (i) (resp. (ii)) in `(19.1.1)` are satisfied, one says that `u` is a
*formal epimorphism* (resp. a *formal monomorphism*). One says that `u` is a *formal bimorphism* if it is at once a
formal monomorphism and a formal epimorphism; this amounts, by virtue of `(19.1.1)`, to saying that `û` is an
isomorphism of the topological `Â`-module `M̂` onto the topological `Â`-module `N̂`.

**Proposition (19.1.3).**

<!-- label: 0_IV.19.1.3 -->

*Let `A` be a topological ring, `M`, `N` two topological `A`-modules, `u : M → N` a continuous `A`-homomorphism. Assume
that there exist two fundamental systems of open submodules `(V_λ)`, `(W_λ)` in `M` and `N` respectively, having the
same set of indices and such that `u(V_λ) ⊂ W_λ` for every `λ`; let `u_λ : M/V_λ → N/W_λ` be the homomorphism deduced
from `u` by passage to the quotients. Then:*

*(i) For `u` to be a formal epimorphism, it is necessary and sufficient that, for every `λ`, `u_λ` be surjective.*

*(ii) For `u` to be a formal monomorphism, it is necessary and sufficient that, for every `λ`, there exist a `μ` such
that `V_μ ⊂ V_λ` and that `Ker(u_μ)` be contained in the kernel `V_λ/V_μ` of the canonical map `M/V_μ → M/V_λ`.*

*(iii) For `u` to be a formal bimorphism, it is necessary and sufficient that, for every `λ`, `u_λ` be surjective and
that there exist a `μ` such that `V_μ ⊂ V_λ` and that the canonical homomorphism `M/V_μ → M/V_λ`*

<!-- original page 168 -->

*factor as `M/V_μ ─u_μ→ N/W_μ → M/V_λ` (where the homomorphism `N/W_μ → M/V_λ` is necessarily unique).*

Assertion (i) is immediate; on the other hand, `Ker(u_μ) = u⁻¹(W_μ)/V_μ`, and the kernel of the canonical map
`M/V_μ → M/V_λ` is `V_λ/V_μ`; the condition in (ii) thus amounts to saying that `u⁻¹(W_μ) ⊂ V_λ`, and assertion (ii)
follows at once; finally, when `u_μ` is surjective, it amounts to the same to say that `Ker(u_μ)` is contained in
`V_λ/V_μ`, or to say that `M/V_μ → M/V_λ` factors as `v ∘ u_μ`, where `v` is a homomorphism `N/W_μ → M/V_λ`, since
`N/W_μ` is then identified with `(M/V_μ)/Ker(u_μ)`.

**Corollary (19.1.4).**

<!-- label: 0_IV.19.1.4 -->

*Let `A` be a topological ring, `M`, `N` two topological `A`-modules whose topologies are deduced from that of `A`,
`u : M → N` a formal epimorphism. Let `(𝔍_λ)` be a fundamental system of open ideals of `A`. For `u` to be a formal
bimorphism, it is necessary and sufficient that for every `λ`, the homomorphism `u_λ : M/𝔍_λ M → N/𝔍_λ N` deduced from
`u` by passage to the quotients be bijective.*

Indeed, one has `u(𝔍_λ M) ⊂ 𝔍_λ N` and one may apply the criterion `(19.1.3, (iii))`; but if one has a factorization
`M/𝔍_λ M ─u_μ→ N/𝔍_μ N ─v→ M/𝔍_λ M`, the image of `𝔍_λ M/𝔍_μ M` under `u_μ` is `𝔍_λ N/𝔍_μ N`, hence the image of
`𝔍_λ N/𝔍_μ N` under `v` is `0` and `v` factors as

```text
                            N/𝔍_μ N → N/𝔍_λ N ─v'→ M/𝔍_λ M;
```

but then the identity automorphism of `M/𝔍_λ M` factors as

```text
                            M/𝔍_λ M ─u_λ→ N/𝔍_λ N ─v'→ M/𝔍_λ M,
```

which shows that `u_λ` is injective, and since one already knows it is surjective, this proves the corollary.

**Proposition (19.1.5).**

<!-- label: 0_IV.19.1.5 -->

*Let `A` be a topological ring, `M`, `N` two topological `A`-modules, `u : M → N` a continuous `A`-homomorphism. The
following conditions are equivalent:*

*a) For every discrete topological `A`-module `E` and every continuous `A`-homomorphism `v : M → E`, there exists a
continuous `A`-homomorphism `w : N → E` such that `v = w ∘ u`.*

*b) For every open submodule `V` of `M`, there exist an open submodule `W''` of `N`, an open submodule
`V'' ⊂ V ∩ u⁻¹(W'')` and a homomorphism `h : N/W'' → M/V` such that the canonical homomorphism `M/V'' → M/V` factors as*

```text
                              M/V'' ─u''→ N/W'' ─h→ M/V
```

*where `u''` is deduced from `u` by passage to the quotients.*

To see that a) implies b), it suffices to apply a) to `E = M/V` and to the canonical homomorphism `v : M → M/V`; then
`W'' = w⁻¹(0)` is an open submodule of `N` and `V'' = u⁻¹(W'')` an open submodule of `M` contained in `V`; these
submodules and the homomorphism `h : N/W'' → M/V` deduced from `w` by passage to the quotient answer the question.
Conversely, to show that b) implies a), one may restrict to the case where `v` is surjective, by replacing `E` by
`v(M)`; then `V' = Ker(v)` is an open submodule of `M`, hence `E` is isomorphic to the discrete `A`-module `M/V'`, and
by applying b) one obtains

<!-- original page 169 -->

the desired continuous `A`-homomorphism `w` as the composite `N → N/W'' ─h→ M/V'`, the diagram

```text
                              M ─────u───→ N
                              │            │
                              ↓            ↓
                            M/V'' ──────→ N/W''
                                    u''
```

being commutative.

When the equivalent conditions of `(19.1.5)` are satisfied, we shall say that `u` is *formally left-invertible*; since
condition b) of `(19.1.5)` implies that `u⁻¹(W'') ⊂ V`, `u` is then a formal monomorphism. The terminology is further
justified by the following corollaries:

**Corollary (19.1.6).**

<!-- label: 0_IV.19.1.6 -->

*If there exists a continuous `Â`-homomorphism `s : N̂ → M̂` such that `s ∘ û = 1_{M̂}`, then `u` is formally
left-invertible.*

One observes that `û` is then a topological isomorphism of `M̂` onto a *topological direct factor* of `N̂`. To prove
`(19.1.6)`, it suffices to note that with the notations of `(19.1.5, a))`, `v : M → E` extends to a continuous
`Â`-homomorphism `v̂ : M̂ → E` since `E` is discrete; let `j : M → M̂` and `j' : N → N̂` be the canonical homomorphisms;
then, setting `w = v̂ ∘ s ∘ j'`, one has `w ∘ u = v̂ ∘ s ∘ û ∘ j = v̂ ∘ j = v`.

**Corollary (19.1.7).**

<!-- label: 0_IV.19.1.7 -->

*Suppose that the topologies of `M` and `N` are deduced from that of `A`, and let `(𝔍_λ)` be a fundamental system of
open ideals of `A`. For `u` to be formally left-invertible, it is necessary and sufficient that, for every `λ`, the
homomorphism `u_λ : M/𝔍_λ M → N/𝔍_λ N`, deduced from `u` by passage to the quotients, be left-invertible (in other
words, be an isomorphism of `M/𝔍_λ M` onto a direct factor of `N/𝔍_λ N`).*

Indeed, the condition is sufficient, for, taking `V' = 𝔍_λ M` in condition b) of `(19.1.5)`, one answers the question by
taking `W'' = 𝔍_λ N`, `V'' = V'` and `h` such that `h ∘ u_λ` is the identity on `M/𝔍_λ M`. Conversely, if `u` is
formally left-invertible, then, for every `λ`, there is, by virtue of `(19.1.5, b))`, a `μ` such that `𝔍_μ ⊂ 𝔍_λ` and a
homomorphism `h : N/𝔍_μ N → M/𝔍_λ M` such that the canonical homomorphism `M/𝔍_μ M → M/𝔍_λ M` factors as
`M/𝔍_μ M ─u_μ→ N/𝔍_μ N ─h→ M/𝔍_λ M`; but since `h(𝔍_λ(N/𝔍_μ N)) = 𝔍_λ · h(N/𝔍_μ N) ⊂ 𝔍_λ(M/𝔍_λ M) = 0`, `h` factors
canonically as `N/𝔍_μ N → N/𝔍_λ N ─s→ M/𝔍_λ M`, and it is immediate that `s` is a left inverse of `u_λ`.

**Proposition (19.1.8).**

<!-- label: 0_IV.19.1.8 -->

*Let `A` be a topological ring admitting a countable decreasing fundamental system `(𝔍_n)` of open ideals. Let `M`, `N`
be two topological `A`-modules whose topologies are deduced from that of `A`, `u : M → N` an `A`-homomorphism. Set
`M_n = M/𝔍_n M`, `N_n = N/𝔍_n N` and let `u_n : M_n → N_n` be the `(A/𝔍_n)`-homomorphism deduced from `u` by passage to
the quotients. Suppose that, for every `n`, `P_n = Coker(u_n)` is a projective `(A/𝔍_n)`-module and that `M` is
separated and complete. Then, for `u` to be formally left-invertible, it is necessary and sufficient that `u` be
left-invertible (and `u` is then a topological isomorphism of `M` onto a topological direct factor of `N`).*

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

where the rows are *split* exact sequences; in other words, there exists for each `n` a homomorphism `s_n : P_n → N_n`
such that `p_n ∘ s_n = 1_{P_n}`. We shall show that one can, by induction on `n`, define a homomorphism
`s'_n : P_n → N_n` such that `p_n ∘ s'_n = 1_{P_n}` and that the diagrams

```text
                              s'_n
                       P_n ──────→ N_n
                       │↑          │↑
                       │h          │g
                       ↓│          ↓│
                       P_{n+1} ──→ N_{n+1}
                              s'_{n+1}
```

be commutative. Indeed, `g ∘ s'_{n+1} − s'_n ∘ h` is a homomorphism of `P_{n+1}` into
`u_{n+1}(M_{n+1}) = u_{n+1}(M_{n+1})/𝔍_n u_{n+1}(M_{n+1})`; since `P_{n+1}` is a *projective* `(A/𝔍_{n+1})`-module, this
homomorphism factors as

```text
                P_{n+1} ─t_{n+1}→ u_{n+1}(M_{n+1}) → u_{n+1}(M_{n+1})/𝔍_n u_{n+1}(M_{n+1})
```

whence one concludes at once that `s'_{n+1} = s_{n+1} − t_{n+1}` answers the question. This being so, from the
decomposition of `N_n` as the direct sum of `u_n(M_n)` and of `s'_n(P_n)`, one deduces at once a homomorphism
`w_n : N_n → M_n` left inverse of `u_n` and such that the diagrams

```text
                              w_n
                       N_n ──────→ M_n
                       │↑          │↑
                       │g          │f
                       ↓│          ↓│
                       N_{n+1} ──→ M_{n+1}
                              w_{n+1}
```

be commutative. The projective system `(w_n)` then admits a projective limit `ŵ : N̂ → M̂ = M`, whence by composition
with the canonical homomorphism `N → N̂`, a homomorphism `w : N → M` such that, for every `n`, the endomorphism
`(w ∘ u)_n` of `M_n = M/𝔍_n M` deduced from `w ∘ u` by passage to the quotients is the identity; this entails that
`w ∘ u = 1_M` since `M` is separated and complete.

**Proposition (19.1.9).**

<!-- label: 0_IV.19.1.9 -->

*Let `A` be a preadmissible topological ring `(0_I, 7.1.2)`, `𝔏` an ideal of definition of `A`, `(𝔍_λ)` a fundamental
system of open ideals of `A`. Let `M`, `N` be two topological `A`-modules whose topologies are deduced from that of `A`,
and such that for every `λ`, `N/𝔍_λ N` is a projective `(A/𝔍_λ)`-module (cf. `(19.2.3)`). Let `u : M → N` be an
`A`-homomorphism. Then the following conditions are equivalent:*

<!-- original page 171 -->

*a) `u` is formally left-invertible.*

*b) The homomorphism `u_0 : M/𝔏M → N/𝔏N` deduced from `u` by passage to the quotients is left-invertible.*

We have seen `(19.1.7)` that condition a) is equivalent to saying that `u_λ` is left-invertible for every `λ`; since `𝔏`
is an open ideal, hence contains a `𝔍_λ`, one deduces at once that `u_0` is left-invertible. To show conversely that b)
implies a), note that for every `λ`, `𝔏/𝔍_λ` is by hypothesis a nilpotent ideal of `A/𝔍_λ`. Our assertion will follow
from the next proposition:

**Proposition (19.1.10).**

<!-- label: 0_IV.19.1.10 -->

*Let `A` be a ring, `M`, `N` two `A`-modules, with `N` projective, `u : M → N` an `A`-homomorphism. Let `𝔍` be an ideal
of `A`; suppose that one of the following conditions is satisfied:*

*(i) `𝔍` is nilpotent.*

*(ii) `𝔍` is contained in the radical of `A` and `M` is of finite type.*

*Then, for `u` to be left-invertible, it is necessary and sufficient that the homomorphism `u_0 : M/𝔍M → N/𝔍N` of
`(A/𝔍)`-modules, deduced from `u` by passage to the quotients, be left-invertible.*

The condition being obviously necessary, let us prove that it is sufficient. Let `v_0` be a left inverse of `u_0`; the
composite homomorphism `N → N/𝔍N ─v_0→ M/𝔍M` factors as `N ─v→ M → M/𝔍M` since `N` is projective; then `w = v ∘ u` is an
endomorphism of `M` such that the endomorphism `w_0` of `M/𝔍M` deduced by passage to the quotients is the *identity*,
and it suffices to prove that `w` is itself bijective (for then `w⁻¹ v` will be a left inverse of `u`). Let us now
distinguish the two cases.

(i) For every `n` one has the commutative diagram

```text
            (𝔍ⁿ/𝔍ⁿ⁺¹) ⊗_{A/𝔍} (M/𝔍M)  ──→  𝔍ⁿM/𝔍ⁿ⁺¹M
                   │                            │
                   │1 ⊗ gr⁰(w)                  │gr^n(w)
                   ↓                            ↓
            (𝔍ⁿ/𝔍ⁿ⁺¹) ⊗_{A/𝔍} (M/𝔍M)  ──→  𝔍ⁿM/𝔍ⁿ⁺¹M
```

where the horizontal arrows are *surjective*, and since `gr⁰(w) = w_0` is the *identity*, so is `gr^n(w)`, which a
fortiori is bijective. The `𝔍`-preadic filtration on `M` being finite since `𝔍` is nilpotent, one concludes that `w` is
bijective (Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1).

(ii) It suffices to show that for every maximal ideal `𝔪` of `A`, the endomorphism `w_𝔪` of `M_𝔪` is bijective
(Bourbaki, Alg. comm., chap. II, §3, n° 3, th. 1) and since `𝔍 A_𝔪 ⊂ 𝔪 A_𝔪` and `A_𝔪/𝔍 A_𝔪 = (A/𝔍)_𝔪`, one is reduced to
proving the proposition when `A` is a *local* ring. Moreover, one may suppose that `𝔍` is the maximal ideal of `A`, for
if `u_0` is left-invertible,

<!-- original page 172 -->

then so is `u_{00} : M/𝔍_0 M → N/𝔍_0 M` obtained by tensoring `u_0` with `1_{A/𝔍_0}`, since one has
`M/𝔍_0 M = (M/𝔍M) ⊗_{A/𝔍} (A/𝔍_0)`. Suppose then that `𝔍` is maximal, so that `A/𝔍` is a field. It clearly suffices to
show that `M` is a *free* `A`-module under the conditions of the statement: indeed, `det(w_0)` is then the canonical
image of `det(w)` in `A/𝔍`, hence `det(w)` does not belong to the ideal `𝔍` and is consequently invertible. Now, the
`(A/𝔍)`-vector space `M/𝔍M` being free of finite type, there is an `A`-module `L` of finite type and an `A`-homomorphism
`f : L → M` such that the homomorphism `f_0 : L/𝔍L → M/𝔍M` deduced from `f` by passage to the quotients is bijective.
Since `M` is of finite type, one concludes first of all that `f` is *surjective* by Nakayama's lemma (Bourbaki, Alg.
comm., chap. II, §3, n° 2, cor. 1 of prop. 4); furthermore, if `g = u ∘ f`, the homomorphism `g_0 : L/𝔍L → N/𝔍N` deduced
by passage to the quotients is left-invertible, and since here `L` is free, the remark at the beginning proves that `g`
is itself left-invertible; but this clearly entails that `f` is *injective*, which completes the proof.

Let us mention in passing the following corollaries of `(19.1.10)`:

**Corollary (19.1.11).**

<!-- label: 0_IV.19.1.11 -->

*Let `A` be a local ring, `k` its residue field, `M` an `A`-module of finite type, `N` a projective `A`-module,
`u : M → N` a homomorphism. For `u` to be left-invertible, it is necessary and sufficient that there exist a system of
generators `(x_i)_{1 ⩽ i ⩽ m}` of `M` such that the images under `u ⊗ 1 : M ⊗_A k → N ⊗_A k` of the `x_i ⊗ 1` be
linearly independent in `N ⊗_A k`; the `x_i` then form a basis of `M`.*

The condition is obviously necessary, for if `u` is left-invertible, `M` is a projective `A`-module of finite type,
hence free. Conversely, if the condition is satisfied, it is clear that the `x_i ⊗ 1` form a basis of `M ⊗_A k` and that
`u ⊗ 1` is left-invertible; it then suffices to apply `(19.1.10)` to the maximal ideal `𝔍` of `A`.

**Corollary (19.1.12).**

<!-- label: 0_IV.19.1.12 -->

*Let `A` be a ring, `M` an `A`-module of finite type, `N` a projective `A`-module, `u : M → N` a homomorphism. For every
prime ideal `𝔭 ∈ Spec(A)`, the following conditions are equivalent:*

*a) The homomorphism `u_𝔭 : M_𝔭 → N_𝔭` is left-invertible.*

*b) The homomorphism `u ⊗ 1 : M ⊗_A k(𝔭) → N ⊗_A k(𝔭)` is injective (recall that `k(𝔭)` denotes the residue field of `A`
at `𝔭`).*

*c) There exists a finite system of elements `x_i ∈ M` (`1 ⩽ i ⩽ m`) such that the images of the `x_i` in `M_𝔭` generate
`M_𝔭`, and a system of `m` linear forms `y_i^*` on `N` (`1 ⩽ i ⩽ m`) such that `det(⟨y_i^*, u(x_j)⟩) ∉ 𝔭`.*

*d) There exists `f ∈ A − 𝔭` such that the homomorphism `u_f : M_f → N_f` is left-invertible.*

*Moreover, the set of `𝔭 ∈ Spec(A)` satisfying these conditions is open in `Spec(A)`.*

The last condition is a trivial consequence of d). Since `N` is projective, it is a direct factor of a free `A`-module
`A^{(I)}`; furthermore, since `M` is of finite type, `u(M)` is contained in a sub-module of `A^{(I)}` of the form `A^n`
for `n` finite; since each of the statements a), b), c), d) is equivalent to the corresponding statement where one
replaces `N` by `N ⊕ P` (with `u` still considered as mapping `M` into `N`), one is reduced to the case where `N` is
free of finite type. It is trivial that d) implies a), and a) and b) are equivalent by virtue of `(19.1.11)`; moreover
a) entails that `M_𝔭` is free `(19.1.11)`, hence a) entails c), by taking for the `x_i` a family whose images in `M_𝔭`
form a basis of this

<!-- original page 173 -->

`A_𝔭`-module and noting that (since `N` is free of finite type) every linear form on the `A_𝔭`-module `N_𝔭` is written
`u^* = v^*/f`, where `f ∈ A − 𝔭`, and `v^*` is a linear form on the `A`-module `N`. It is clear that c) implies b), and
it remains to see that a) implies d). Now, since `N` is of finite presentation, `(Hom_A(N, M))_𝔭` is canonically
identified with `Hom_{A_𝔭}(N_𝔭, M_𝔭)` (Bourbaki, Alg. comm., chap. II, §2, n° 7, prop. 19). If `w_𝔭` is a left inverse
of `u_𝔭`, there exists thus a homomorphism `w : N → M` and an element `f ∈ A − 𝔭` such that `w_𝔭 = w ⊗ (1/f) 1_{A_𝔭}`.
The relation `w_𝔭 ∘ u_𝔭 = 1_{M_𝔭}` thus also reads `(w ∘ u) ⊗ 1_{A_𝔭} = f · 1_{M_𝔭}`. But since `M` is an `A`-module of
finite type, there exists `g ∈ A − 𝔭` such that the endomorphism `g((w ∘ u) − f · 1_M)` vanishes on all the generators
of `M`, hence is zero. Setting `h = fg`, and `u_h = u ⊗ 1_{A_h}`, `w_h = w ⊗ 1_{A_h}`, one therefore has
`w_h(u_h(z)) = (f/1) z` for every `z ∈ M_h`; but since `h/1` is invertible in `A_h`, so is `f/1 = f`, and `f⁻¹ w_h` is
consequently a left inverse of `u_h`, which completes the proof.

**Proposition (19.1.13).**

<!-- label: 0_IV.19.1.13 -->

*Suppose the hypotheses of `(19.1.9)` are satisfied and suppose further that `(𝔍_λ)` is a decreasing sequence `(𝔍_n)`
and that `M` is separated and complete. Then conditions a) and b) of `(19.1.9)` are also equivalent to:*

*c) `u` is left-invertible.*

One already knows that c) implies a) `(19.1.6)`. Conversely, if a) is satisfied, one knows (with the notations of
`(19.1.8)`) that `M_n` is a direct factor of the projective `(A/𝔍_n)`-module `N_n`, hence `P_n` is also isomorphic to a
direct factor of `N_n`, and consequently is projective; it then suffices to apply `(19.1.8)`.

Let us finally note the following proposition:

**Proposition (19.1.14).**

<!-- label: 0_IV.19.1.14 -->

*Let `A` be a ring, `M` an `A`-module of finite type, `N` a projective `A`-module, `u : M → N` an `A`-homomorphism.*

*(i) For `u` to be left-invertible, it is necessary and sufficient that, for every maximal ideal `𝔪` of `A`,
`u_𝔪 : M_𝔪 → N_𝔪` be left-invertible.*

*(ii) Let `A'` be an `A`-algebra which is a faithfully flat `A`-module. For `u` to be left-invertible, it is necessary
and sufficient that `u ⊗ 1 : M ⊗_A A' → N ⊗_A A'` be left-invertible.*

As in `(19.1.12)`, one can restrict to the case where `N` is free of finite type; to say that `u` is left-invertible
then means that `u` is injective and that the quotient module `P = N/u(M)` is projective, for `u(M)` will then be a
direct factor of `N`. Note further that since `M` is of finite type, `P` is of *finite presentation*. This being so:

(i) The condition is obviously necessary. Conversely, if it is satisfied, one knows that `u` is injective (Bourbaki,
Alg. comm., chap. II, §3, n° 3, th. 1) and since `P_𝔪 = N_𝔪/u_𝔪(M_𝔪)` is projective for every `𝔪`, one knows that this
implies that `P` is projective (*loc. cit.*, §5, n° 2, th. 1).

(ii) Here again, the condition is trivially necessary. Conversely, if it is satisfied, one knows that `u` is injective
`(0_I, 6.4.1)` and since `P ⊗_A A' = Coker(u ⊗ 1)` is projective, hence flat, one deduces that `P` is a flat `A`-module
`(0_I, 6.6.3)`, hence projective since it is of finite presentation (Bourbaki, Alg. comm., chap. II, §5, n° 2, cor. 2 of
th. 1).

<!-- original page 174 -->

**Remark (19.1.15).**

<!-- label: 0_IV.19.1.15 -->

*The notion "dual" to that of formally left-invertible homomorphism is that of *formally right-invertible* homomorphism;
such a continuous `A`-homomorphism `u : M → N` verifies, by definition, the following condition: for every open
submodule `W` of `N`, there exist an open submodule `V' ⊂ u⁻¹(W')` of `M`, an open submodule `W'' ⊂ W` of `N` and a
homomorphism `h : N/W'' → M/V'` such that the canonical homomorphism `N/W'' → N/W` factors as*

```text
                              N/W'' ─h→ M/V' ─u'→ N/W
```

*where `u'` is deduced from `u` by passage to the quotients. This implies that `u` is a formal epimorphism; if there
exists a continuous `A`-homomorphism `r : N → M` such that `u ∘ r = 1_N`, one verifies at once that `u` is formally
right-invertible. If the conditions of `(19.1.7)` are satisfied, for `u` to be formally right-invertible, it is
necessary and sufficient that the `u_λ` be right-invertible (that is, that the kernel of `u_λ` be a direct factor of
`M/𝔍_λ M` and that `u_λ` be an isomorphism of a supplement of `Ker(u_λ)` onto `N/𝔍_λ N`). We leave to the reader the
task of stating and proving the propositions corresponding to `(19.1.8)` and `(19.1.9)` (in the analogue of `(19.1.8)`,
one must assume `M` separated and complete and that `M_n` is a projective `(A/𝔍_n)`-module; in the analogue of
`(19.1.9)`, one must drop the hypothesis on the `N/𝔍_λ N`, but assume on the other hand that, for every `λ`, `M/𝔍_λ M`
is a projective `(A/𝔍_λ)`-module).*

### 19.2. Formally projective modules

**Definition (19.2.1).**

<!-- label: 0_IV.19.2.1 -->

*Let `A` be a topological ring. One says that a topological `A`-module `M` is **formally projective** if it satisfies
the following condition: for every open ideal `𝔍` of `A`, every pair of (discrete) `(A/𝔍)`-modules `P`, `Q`, every
surjective `A`-homomorphism `u : P → Q` and every continuous `A`-homomorphism `v : M → Q`, there exists a continuous
`A`-homomorphism `w : M → P` such that `v = u ∘ w`.*

**(19.2.2)** To verify the condition of `(19.2.1)`, one may evidently restrict (by replacing `Q` by `v(M)` and `P` by
`u⁻¹(v(M))`) to the case where `v` is itself surjective; then `Q` is isomorphic to `M/V`, where `V` is an open submodule
of `M` such that `𝔍M ⊂ V`; condition `(19.2.1)` is then equivalent to saying that for every discrete `(A/𝔍)`-module `P`
and every surjective `A`-homomorphism `u : P → M/V`, there exist an open submodule `V' ⊂ V` of `M` and an
`A`-homomorphism `w : M/V' → P` such that the canonical homomorphism `M/V' → M/V` factors as `M/V' ─w→ P ─u→ M/V`. We
note that it suffices to verify this condition when `𝔍` runs through a fundamental system of neighbourhoods of `0` in
`A` formed of ideals.

**(19.2.3)** Suppose there exists a fundamental system `(𝔍_λ)` of open ideals of `A` and a fundamental system `(V_λ)` of
open submodules of `M`, having the same set of indices as `(𝔍_λ)` and such that, for every `λ`, `M/V_λ` is a
*projective* `(A/𝔍_λ)`-module. Then `M` is formally projective: it suffices indeed, with the notations of `(19.2.2)`, to
take `λ` such that `𝔍_λ ⊂ 𝔍` and `V_λ ⊂ V`; since `P` is also an `(A/𝔍_λ)`-module, the factorization of the canonical
homomorphism `M/V_λ → M/V` as `M/V_λ → P → M/V` follows from the fact that we deal with an `(A/𝔍_λ)`-homomorphism and
that `M/V_λ` is assumed to be a projective `(A/𝔍_λ)`-module.

When the stricter condition of this number is satisfied, one says that `M` is *strictly formally projective*.

**Proposition (19.2.4).**

<!-- label: 0_IV.19.2.4 -->

*Let `A` be a topological ring, `M` a topological `A`-module whose topology is deduced from that of `A`. For `M` to be
formally projective, it is necessary and sufficient that it be strictly formally projective.*

<!-- original page 175 -->

We have just seen that the condition is sufficient. Conversely, suppose `M` is formally projective and let `(𝔍_λ)` be a
fundamental system of open ideals of `A`. For every `λ`, let `P` be a free `(A/𝔍_λ)`-module and `u : P → M/𝔍_λ M` a
surjective `(A/𝔍_λ)`-homomorphism. There exists therefore a `𝔍_μ ⊂ 𝔍_λ` such that the canonical homomorphism
`M/𝔍_μ M → M/𝔍_λ M` factors as `M/𝔍_μ M ─w→ P ─u→ M/𝔍_λ M`; but since `w(𝔍_μ(M/𝔍_μ M)) ⊂ 𝔍_μ P = 0`, `w` factors as
`M/𝔍_μ M → M/𝔍_λ M ─v→ P`, and it is clear that `u ∘ v` is the identity on `M/𝔍_λ M`, which proves that this
`(A/𝔍_λ)`-module is projective.

**Proposition (19.2.5).**

<!-- label: 0_IV.19.2.5 -->

*Let `A` be a topological ring, `M` a topological `A`-module.*

*(i) For `M` to be formally projective (resp. strictly formally projective), it is necessary and sufficient that the
topological `Â`-module `M̂` be so.*

*(ii) Let `A'` be a topological `A`-algebra. If `M` is formally projective (resp. strictly formally projective), then
`M ⊗_A A'` (equipped with the tensor product topology) is a formally projective (resp. strictly formally projective)
topological `A'`-module.*

(i) It suffices to remark that when `𝔍` (resp. `V`) runs through the set of open ideals of `A` (resp. the set of open
submodules of `M`), the separated completion `𝔍̂` (resp. `V̂`) runs through the set of open ideals of `Â` (resp. the set
of open submodules of `M̂`), and `Â/𝔍̂ = A/𝔍` (resp. `M̂/V̂ = M/V`) up to a canonical isomorphism; since the notion of
formally projective (resp. strictly formally projective) module only involves the `A/𝔍` and the `M/V`, one deduces (i)
at once.

(ii) Suppose first `M` is formally projective and set `M' = M ⊗_A A'`; let `𝔍'` be an open ideal of `A'`, `P'`, `Q'` two
discrete `(A'/𝔍')`-modules, `u' : P' → Q'` a surjective `A'`-homomorphism, `v' : M' → Q'` a continuous
`A'`-homomorphism. There is an open ideal `𝔍` of `A` such that `𝔍 A' ⊂ 𝔍'`, hence `P'` and `Q'` are also discrete
`(A/𝔍)`-modules. If one considers the composite `A`-homomorphism `v : M ─j→ M' ─v'→ Q'`, which is continuous, the
hypothesis implies that there exists a continuous `A`-homomorphism `w : M → P'` such that `v = u' ∘ w`; but since `P'`
is an `A'`-topological module, `w` factors as `M ─j→ M' ─w'→ P'`, where `w'` is a continuous `A'`-homomorphism, and
since `v' ∘ j = (u' ∘ w') ∘ j`, one concludes that `v' = u' ∘ w'`.

Suppose next that `M` is strictly formally projective; let `(𝔍_λ)` (resp. `(V_λ)`) be a fundamental system of open
ideals of `A` (resp. of open submodules of `M`) such that `(M/V_λ)` is a projective `(A/𝔍_λ)`-module, and let `(𝔍'_μ)`
be a fundamental system of open ideals of `A'`. One has a fundamental system of neighbourhoods of `0` in `M'` by taking
the submodules `Im(M ⊗_A 𝔍'_μ) + Im(V_λ ⊗_A A') = W_{λμ}`, where `λ` and `μ` are such that `𝔍_λ A' ⊂ 𝔍'_μ`. Since
`(M ⊗_A A')/W_{λμ} = (M/V_λ) ⊗_{A/𝔍_λ} (A'/𝔍'_μ)` and since `M/V_λ` is a projective `(A/𝔍_λ)`-module, `M'/W_{λμ}` is a
projective `(A'/𝔍'_μ)`-module.

### 19.3. Formally smooth algebras

**Definition (19.3.1).**

<!-- label: 0_IV.19.3.1 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra. One says that `B` is a **formally smooth `A`-algebra**
if, for every discrete topological `A`-algebra `C`*

<!-- original page 176 -->

*and every nilpotent ideal `𝔍` of `C`, every continuous `A`-homomorphism `u : B → C/𝔍` factors as `B ─v→ C ─φ→ C/𝔍`,
where `v` is a continuous homomorphism and `φ` is the canonical homomorphism.*

Definition `(19.3.1)` amounts to saying that the following property holds:

(P) For every *open* ideal `𝔎` of the `A`-algebra `B` and every `A`-homomorphism `u' : B/𝔎 → C/𝔍`, there is an open
ideal `𝔎' ⊂ 𝔎` of `B` such that the homomorphism `B → B/𝔎 ─u'→ C/𝔍` factors as `B → B/𝔎' ─v'→ C → C/𝔍`, where `v'` is an
`A`-homomorphism.

Indeed, if `u : B → C/𝔍` is a continuous `A`-homomorphism, it has for kernel `𝔎` an open ideal of `B`, hence `u` factors
as `B → B/𝔎 ─u'→ C/𝔍`, and if (P) is satisfied, it suffices to apply it to `u'` and to take for `v` the composite
`B → B/𝔎' ─v'→ C` to satisfy the conditions of `(19.3.1)`. Conversely, suppose that `B` is a formally smooth
`A`-algebra; let us give an open ideal `𝔎` of `B` and an `A`-homomorphism `u' : B/𝔎 → C/𝔍` and apply definition
`(19.3.1)` to `u : B → B/𝔎 → C/𝔍`; if `v : B → C` is a continuous `A`-homomorphism such that `u` factors as
`B ─v→ C → C/𝔍`, the ideal `𝔎' = Ker(v) ∩ 𝔎` of `B` is open and contained in `𝔎`; consequently `v` factors as
`B → B/𝔎' ─v'→ C`, and `v'` indeed satisfies condition (P).

**Proposition (19.3.2).**

<!-- label: 0_IV.19.3.2 -->

*Let `A` be a discrete ring, `V` a projective `A`-module; the symmetric algebra `B = S_A^•(V)`, equipped with the
discrete topology, is a formally smooth `A`-algebra.*

Indeed, with the notations `C` and `𝔍` having the same meaning as in `(19.3.1)`, let `u : B → C/𝔍` be a homomorphism of
`A`-algebras, which by restriction to `V = S_A^1(V)` gives a homomorphism of `A`-modules `u_1 : V → C/𝔍`; since `V` is
projective, `u_1` factors as `V ─v_1→ C → C/𝔍`, and `v_1` extends to a homomorphism of `A`-algebras `v : S_A^•(V) → C`,
such that the composite `φ ∘ v` coincides with `u` on `V`, hence `φ ∘ v = u`, which proves the proposition.

**Corollary (19.3.3).**

<!-- label: 0_IV.19.3.3 -->

*If `A` is a discrete ring, every polynomial algebra `B = A[T_α]_{α ∈ I}`, equipped with the discrete topology, is a
formally smooth `A`-algebra.*

**Proposition (19.3.4).**

<!-- label: 0_IV.19.3.4 -->

*Let `A` be a topological ring, and let `B = A[[T_α]]_{α ∈ I} = ∑_{λ ∈ ℕ^{(I)}} c_λ T^λ` be a formal power series ring
(broad algebra over `A` of the monoid `ℕ^{(I)}`, identified as an `A`-module with the product `A^{ℕ^{(I)}}`). If one
equips `B` with the product topology, `B` is a formally smooth `A`-algebra.*

Let `(𝔏_μ)_{μ ∈ M}` be a fundamental system of open ideals of `A`. For every finite part `H` of `I`, every `μ ∈ M` and
every integer `n`, denote by `𝔎_{H, μ, n}` the neighbourhood of `0` in `B` consisting of the `(c_λ)` such that for every
`λ = (λ_α)_{α ∈ I}` with `λ_α = 0` for `α ∉ H` and `∑_{α ∈ H} λ_α ⩽ n`, one has `c_λ ∈ 𝔏_μ`. One verifies immediately
that the `𝔎_{H, μ, n}` form a fundamental system of neighbourhoods of `0` in `B` and are ideals of `B`, hence the
product topology is compatible with the `A`-algebra structure of `B`.

Let us first note, with the same notations, the

**Lemma (19.3.4.1).**

<!-- label: 0_IV.19.3.4.1 -->

*Let `E` be a discrete `A`-algebra.*

*(i) If `f : B → E` is a continuous `A`-homomorphism, there exists a finite part `H` of `I` such that `f(T_α) = 0` for
`α ∉ H`, and `f(T_α)` is nilpotent in `E` for every `α ∈ H`.*

<!-- original page 177 -->

*(ii) Conversely, let `H` be a finite part of `I`, `(z_α)_{α ∈ H}` a family of nilpotent elements of `E`. There exists a
continuous `A`-homomorphism `g : B → E` and only one such that `g(T_α) = z_α` for `α ∈ H` and `g(T_α) = 0` for `α ∉ H`.*

(i) follows at once from the fact that `f⁻¹(0)` is a neighbourhood of `0` in the product `A`-module `A^{ℕ^{(I)}}`,
whence `f(T^λ) = 0` except for a finite number of values of `λ ∈ ℕ^{(I)}`. To prove (ii), it suffices to remark that the
polynomial ring `B' = A[T_α]_{α ∈ I}` is dense in `B`; the existence and uniqueness of the restriction `g | B'` are
trivial and its continuity follows from the hypothesis that the `f(T_α)` for `α ∈ H` are nilpotent, for if
`(f(T_α))^n = 0` for every `α ∈ H`, one has `g(T^λ) = 0` for every `λ = (λ_α)_{α ∈ I}` of finite support except those
for which `λ_α = 0` for `α ∉ H` and `λ_α < n` for `α ∈ H`, that is, except for a finite number of values of `λ`.

This lemma being established, and the notations `C` and `𝔍` having the same meaning as in `(19.3.1)`, one has
`u(T_α) = 0` except for `α ∈ H`, `H` being a finite part of `I`, and the `z_α = u(T_α)` for `α ∈ H` are nilpotent in
`C/𝔍`; since `𝔍` is nilpotent, there exists a family `(x_α)_{α ∈ H}` of nilpotent elements of `C` whose canonical images
in `C/𝔍` are the `z_α`; if `v` is the continuous `A`-homomorphism of `B` into `C` such that `v(T_α) = 0` for `α ∉ H`,
`v(T_α) = x_α` for `α ∈ H`, it is clear that `u` factors as `B ─v→ C → C/𝔍`.

**Proposition (19.3.5).**

<!-- label: 0_IV.19.3.5 -->

*Let `A` be a topological ring.*

*(i) `A` is a formally smooth `A`-algebra.*

*(ii) If `B` is a formally smooth `A`-algebra and `C` a formally smooth `B`-algebra, then `C` is a formally smooth
`A`-algebra.*

*(iii) Let `B` be a formally smooth `A`-algebra, `A'` a topological `A`-algebra; then the topological `A'`-algebra
`B ⊗_A A'` `(0_I, 7.7.5 and 7.7.6)` is formally smooth.*

*(iv) Let `B` be a topological `A`-algebra, `S` (resp. `T`) a multiplicative part of `A` (resp. `B`) such that the
canonical image of `S` in `B` is contained in `T`. If `B` is a formally smooth `A`-algebra, then `T⁻¹ B` is a formally
smooth `S⁻¹ A`-algebra.*

*(v) Let `B_i` (`1 ⩽ i ⩽ n`) be topological `A`-algebras. For `∏_{i=1}^n B_i` to be a formally smooth `A`-algebra, it is
necessary and sufficient that each of the `B_i` be so.*

(i) If `C` is a discrete `A`-algebra, `φ : C → C/𝔍` the canonical homomorphism of `C` onto an arbitrary quotient
`A`-algebra of `C`, the only `A`-homomorphism of `A` into `C/𝔍` is the composite homomorphism `A ─ψ→ C ─φ→ C/𝔍`, where
`ψ` is the homomorphism defining the `A`-algebra structure on `C`; since `ψ` is continuous, the condition of `(19.3.1)`
is trivially satisfied.

(ii) Let `α : A → B`, `β : B → C` be the continuous homomorphisms defining respectively the `A`-algebra structure on `B`
and the `B`-algebra structure on `C`, so that `β ∘ α` defines the `A`-algebra structure on `C`. Let `E` be a discrete
`A`-algebra, `𝔏` a nilpotent ideal of `E`, `u : C → E/𝔏` a continuous `A`-homomorphism, so that `u ∘ β ∘ α` is the
homomorphism defining the `A`-algebra structure of `E/𝔏`. Since `B` is a formally smooth `A`-algebra, the continuous
`A`-homomorphism `u ∘ β : B → E/𝔏` factors as `B ─v→ E → E/𝔏`, where `v` is a continuous `A`-homomorphism; `v` and
`u ∘ β` then define on `E` and `E/𝔏` respectively structures of topological `B`-algebra, for which `E/𝔏` is

<!-- original page 178 -->

still the (discrete) quotient algebra of the `B`-algebra `E`. Furthermore, `u` is a continuous `B`-homomorphism, hence
factors as `C ─w→ E → E/𝔏`, where `w` is a continuous `B`-homomorphism; since `v ∘ α` is the `A`-homomorphism defining
the `A`-algebra structure on `E`, `w` is indeed a continuous `A`-homomorphism, whence our assertion.

(iii) Let `C` be a discrete topological `A'`-algebra, `𝔍` a nilpotent ideal of `C`, `u : B ⊗_A A' → C/𝔍` a continuous
`A'`-homomorphism. If one composes `u` with the canonical homomorphism `ρ : B → B ⊗_A A'`, one obtains (since
`A → B ─ρ→ B ⊗_A A'` is equal to the composite `A → A' ─σ→ B ⊗_A A'`) a continuous `A`-homomorphism which, by
hypothesis, therefore factors as `B ─v→ C → C/𝔍`, where `v` is a continuous `A`-homomorphism (for the topological
`A`-algebra structure on `C` defined by the composite `A → A' ─u→ C` of the canonical homomorphisms). The equality of
the composites `A → B ─v→ C` and `A → A' ─u→ C` thus entails the existence of a continuous ring homomorphism
`f : B ⊗_A A' → C` such that `v = f ∘ ρ` and `u = f ∘ σ` `(0_I, 7.7.6)`; since the composite homomorphisms
`B ─ρ→ B ⊗_A A' ─f→ C → C/𝔍` and `B ─ρ→ B ⊗_A A' ─u→ C/𝔍` (resp. `A' ─σ→ B ⊗_A A' ─f→ C → C/𝔍` and
`A' ─σ→ B ⊗_A A' ─u→ C/𝔍`) are equal, one indeed has the factorization `u : B ⊗_A A' → C → C/𝔍`, which establishes
(iii).

(iv) The topology considered on `S⁻¹ A` (resp. `T⁻¹ B`) is naturally that for which a fundamental system of
neighbourhoods of `0` is formed of the `S⁻¹ 𝔍` (resp. `T⁻¹ 𝔎`), where `𝔍` (resp. `𝔎`) runs through a fundamental system
of open ideals of `A` (resp. `B`) `(0_I, 7.6.1)`. If `α : A → B` is the canonical homomorphism, it is clear that the
canonical homomorphism `α' : S⁻¹ A → T⁻¹ B` deduced from `α` (and whose existence results from `α(S) ⊂ T` by hypothesis)
is continuous `(0_I, 7.6.6)`. Let then `C` be a discrete topological `S⁻¹ A`-algebra, `𝔍` a nilpotent ideal of this
algebra, `u : T⁻¹ B → C/𝔍` a continuous `S⁻¹ A`-homomorphism; then the composite `B → T⁻¹ B → C/𝔍` is a continuous
`A`-homomorphism which, by hypothesis, factors as `B → C → C/𝔍`, where `v` is a continuous `A`-homomorphism. Since for
every `t ∈ T`, `t/1` is invertible in `T⁻¹ B`, `u(t/1)` is invertible in `C/𝔍`. Since `𝔍` is nilpotent, every element of
the class `u(t/1)` in `C`, and in particular `v(t)`, is invertible in `C` `(0_I, 7.1.12)`, and consequently `v` factors
as `B → T⁻¹ B ─w→ C`; since `v` is continuous, so is `w` `(0_I, 7.6.6)`, and it is an `S⁻¹ A`-homomorphism because the
composite `A → B → T⁻¹ B → C` is equal to

```text
                              A → S⁻¹ A → T⁻¹ B → C,
```

hence `S⁻¹ A → T⁻¹ B → C` is the canonical homomorphism defining on `C` the `S⁻¹ A`-algebra structure. Finally, the
composite homomorphisms `B → T⁻¹ B → C → C/𝔍` and `B → T⁻¹ B ─u→ C/𝔍` being equal, the same reasoning shows that `u` is
indeed equal to the composite `T⁻¹ B ─w→ C → C/𝔍`, whence (iv).

Finally, (v) is immediate, the data of a continuous `A`-homomorphism of `B = ∏_{i=1}^n B_i` into `C` (resp. `C/𝔍`) being
equivalent to that of `n` continuous `A`-homomorphisms `B_i → C`

<!-- original page 179 -->

(resp. `B_i → C/𝔍`), and any continuous `A`-homomorphism `B_j → C` (resp. `B_j → C/𝔍`) giving by composition a
continuous `A`-homomorphism `B → B_j → C` (resp. `B → B_j → C/𝔍`).

**Proposition (19.3.6).**

<!-- label: 0_IV.19.3.6 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra, `Â` and `B̂` the respective separated completions of `A`
and `B`, so that `B̂` is a topological `Â`-algebra. The following conditions are equivalent:*

*a) `B` is a formally smooth `A`-algebra.*

*b) `B̂` is a formally smooth `A`-algebra.*

*c) `B̂` is a formally smooth `Â`-algebra.*

Of course, the `Â`-algebra structure on `B̂` is defined by the homomorphism `φ̂`, if `φ : A → B` is the homomorphism
defining the `A`-algebra structure on `B`. Since every discrete `A`-algebra `C` is separated and complete, it is also an
`Â`-algebra (by canonical extension of the homomorphism from `A` into `C`), and a continuous `A`-homomorphism from `B`
into `C` gives by canonical extension an `A`-homomorphism (and *a fortiori* an `Â`-homomorphism) from `B̂` into `C` (in
other words, every `A`-homomorphism `B → C` factors as `B → B̂ → C` in a unique way). These remarks and definition
`(19.3.1)` entail the proposition at once.

**Corollary (19.3.7).**

<!-- label: 0_IV.19.3.7 -->

*Under the hypotheses of `(19.3.5, (iv))`, the topological `A{S⁻¹}`-algebra `B{T⁻¹}` is formally smooth.*

This follows from the definitions `(0_I, 7.6.1 and 7.6.7)` and from `(19.3.5, (iv))` and `(19.3.6)`.

**Proposition (19.3.8).**

<!-- label: 0_IV.19.3.8 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra, and suppose that for every open ideal `𝔎` of `B`, `𝔎²` is
also open. Let `A'`, `B'` be topological rings obtained by equipping `A` and `B` with topologies finer than the initial
topologies, and suppose that the canonical homomorphism `φ : A → B` is still a continuous homomorphism from `A'` into
`B'`. Then, if `B'` is a formally smooth `A'`-algebra, `B` is a formally smooth `A`-algebra.*

It suffices to apply the following lemma:

**Lemma (19.3.8.1).**

<!-- label: 0_IV.19.3.8.1 -->

*Let `C` be a discrete `A`-algebra, `𝔍` a nilpotent ideal of `C`. Suppose that the square of every open ideal of `B` is
open. Then, if a composite homomorphism `v : B ─u→ C → C/𝔍` is continuous, the homomorphism `u` is continuous.*

Indeed, `𝔎 = u⁻¹(𝔍)` is the kernel of `v` and is open by hypothesis; since there exists an integer `n` such that
`𝔍^n = 0`, `𝔎^n` is contained in `Ker(u)`; but by induction on `h`, it follows from the hypothesis that `𝔎²` is open,
hence so is `𝔎^n` for every `n`, and consequently `Ker(u)` is also open, which proves our assertion.

One observes that the hypothesis on `B` means that the topology of `B` is the *least upper bound* of the `𝔎`-preadic
topologies, where `𝔎` runs through the set of open ideals of `B`. If `B` is a preadic ring `(0_I, 7.1.9)`, this
condition is always satisfied.

**(19.3.9)** We are now going to see that the property of being formally smooth implies "lifting" properties of
homomorphisms under more general conditions than those of definition `(19.3.1)`.

<!-- original page 180 -->

**Proposition (19.3.10).**

<!-- label: 0_IV.19.3.10 -->

*Let `A` be a topological ring, `B` a formally smooth `A`-algebra. Let `C` be a topological `A`-algebra, `𝔍` an ideal of
`C`, satisfying the following conditions:*

*1° `C` is metrizable and complete.*

*2° `𝔍` is closed and the sequence `(𝔍^n)` tends to `0`.*

*Then every continuous `A`-homomorphism `u : B → C/𝔍` factors as `B ─v→ C → C/𝔍`, where `v` is a continuous
`A`-homomorphism.*

Let `(𝔏_n)` be a decreasing sequence of ideals of `C` forming a fundamental system of neighbourhoods of `0`. For every
`n`, consider the discrete `A`-algebra `C/𝔏_n` and the ideal `(𝔍 + 𝔏_n)/𝔏_n` of this algebra; since there exists `k`
such that `𝔍^k ⊂ 𝔏_n`, `(𝔍 + 𝔏_n)/𝔏_n` is nilpotent. For every `n`, let `u_n` be the continuous homomorphism
`B ─u→ C/𝔍 → C/(𝔍 + 𝔏_n) = (C/𝔏_n)/((𝔍 + 𝔏_n)/𝔏_n)`; by hypothesis `u_n` factors as `B ─v_n→ C/𝔏_n ─φ_n→ C/(𝔍 + 𝔏_n)`,
where `v_n` is a continuous `A`-homomorphism. Let us show that one may choose the `v_n` step by step so that `v_n`
factors as

```text
                              B ─v_{n+1}→ C/𝔏_{n+1} → C/𝔏_n
```

for every `n` (in other words, so that the `v_n` form a projective system of homomorphisms). This will follow from the
next lemma:

**Lemma (19.3.10.1).**

<!-- label: 0_IV.19.3.10.1 -->

*Let `B` be a formally smooth `A`-algebra, `E`, `E'` two discrete topological `A`-algebras, `𝔎` (resp. `𝔎'`) a nilpotent
ideal of `E` (resp. `E'`), `f : E → E'` a surjective `A`-homomorphism such that `f(𝔎) ⊂ 𝔎'`, `f' : E/𝔎 → E'/𝔎'` the
homomorphism deduced from `f` by passage to the quotients. Let `u : B → E/𝔎` be a continuous `A`-homomorphism, `u'` the
composite homomorphism `B ─u→ E/𝔎 ─f'→ E'/𝔎'`, and let `v' : B → E'` be a continuous `A`-homomorphism such that `u'`
factors as `B ─v'→ E' → E'/𝔎'`. Then there exists a continuous `A`-homomorphism `v : B → E` such that `v'` factors as
`B ─v→ E ─f→ E'`.*

In the commutative diagram

```text
                              E  ──f──→  E'
                              │          │
                              ↓          ↓
                              E/𝔎 ─f'─→ E'/𝔎'
```

all the homomorphisms are surjective; if `𝔏` is the kernel of `f`, `E'` is identified with `E/𝔏` and `𝔎'` with
`(𝔎 + 𝔏)/𝔏`. Let us now use the following elementary lemma:

**Lemma (19.3.10.2).**

<!-- label: 0_IV.19.3.10.2 -->

*Let `F` be a ring (not necessarily commutative), `𝔞`, `𝔟` two two-sided ideals of `F`; then the fibre product
`(F/𝔞) ×_{F/(𝔞 + 𝔟)} (F/𝔟)` is canonically identified with `F/(𝔞 ∩ 𝔟)`.*

This is none other than a particular application of `(18.1.7)`, where, in diagram `(18.1.7.1)`, one replaces `G` by
`F/(𝔞 ∩ 𝔟)`, `𝔍'` by `𝔟/(𝔞 ∩ 𝔟)`, `F` by `F/𝔟`, `𝔎` by `(𝔞 + 𝔟)/𝔟`, `B` by `F/(𝔞 + 𝔟)` and `θ` by the canonical
bijective `F`-homomorphism `(𝔞 + 𝔟)/𝔟 ≅ 𝔞/(𝔞 ∩ 𝔟)`.

<!-- original page 181 -->

Applying this lemma to the situation of `(19.3.10.1)`, the commutativity of the diagram

```text
                              B ─v'→ E' = E/𝔏
                              │      │
                            u │      │
                              ↓      ↓
                              E/𝔎 ─f'─→ E'/𝔎'
```

shows the existence of a homomorphism `w : B → E/(𝔎 ∩ 𝔏)` such that `v'` and `u` factor as `B ─w→ E/(𝔎 ∩ 𝔏) → E/𝔏` and
`B ─w→ E/(𝔎 ∩ 𝔏) → E/𝔎` respectively; since the kernel of `w` contains the intersection of those of `v'` and `u`, it is
open in `B` and `w` is continuous. Finally, it is clear that `𝔎 ∩ 𝔏` is nilpotent, hence `w` factors as
`B ─v→ E → E/(𝔎 ∩ 𝔏)`, where `v` is a continuous `A`-homomorphism answering the question.

Returning to the proof of `(19.3.10)`, the existence of `v_{n+1}` follows from lemma `(19.3.10.1)` applied by replacing
`E`, `E'`, `𝔎`, `𝔎'` by `C/𝔏_{n+1}`, `C/𝔏_n`, `(𝔍 + 𝔏_{n+1})/𝔏_{n+1}` and `(𝔍 + 𝔏_n)/𝔏_n` respectively, and `u`, `u'`
and `v'` by `u_{n+1}`, `u_n` and `v_n` respectively. We note that, since `C` is separated and complete, it is equal to
`lim←(C/𝔏_n)`, and `v = lim← v_n` is a continuous `A`-homomorphism from `B` into `C`. Since `𝔍` is closed in `C`, one
has `𝔍 = ⋂_n (𝔍 + 𝔏_n)`; since `C/𝔍` is metrizable and complete and since the `(𝔍 + 𝔏_n)/𝔍` form a fundamental system of
neighbourhoods of `0` in `C/𝔍`, one has `C/𝔍 = lim←(C/(𝔍 + 𝔏_n))` and `lim← φ_n` is the canonical map `φ : C → C/𝔍`.
Since `lim← u_n = u`, one has indeed `u = v ∘ φ`. Q.E.D.

**Corollary (19.3.11).**

<!-- label: 0_IV.19.3.11 -->

*Let `A` be a topological ring, `B` a formally smooth `A`-algebra, `C` a complete Noetherian local ring, `𝔍` an ideal
distinct from `C`, `φ : A → C` a continuous homomorphism, making `C` a topological `A`-algebra. Then every continuous
`A`-homomorphism `u_0 : B → C_0 = C/𝔍` factors as `B → C → C/𝔍`, where `u` is a continuous `A`-homomorphism.*

All the conditions of `(19.3.10)` are indeed satisfied `(0_I, 7.3.5)`.

**Proposition (19.3.12).**

<!-- label: 0_IV.19.3.12 -->

*Let `A` be a topological ring, `B` a formally smooth `A`-algebra, `C` a topological `A`-algebra, `𝔍` an ideal of `C`,
satisfying the following conditions:*

*1° There exists a fundamental system of open ideals `𝔏_λ` of `C` such that the `C_λ = C/𝔏_λ` are Artinian rings and
that the canonical homomorphism `C → lim← C_λ` is an isomorphism of topological rings.*

*2° The ideal `𝔍` is closed in `C` and topologically nilpotent.*

*3° The square of every open ideal of `B` is open.*

*Under these conditions, every continuous `A`-homomorphism `u : B → C/𝔍` factors as `B → C → C/𝔍`, where `v` is a
continuous `A`-homomorphism.*

Let `𝔍_λ = (𝔍 + 𝔏_λ)/𝔏_λ` be the canonical image of `𝔍` in `C_λ`, which is a nilpotent ideal, and let `u_λ` be the
composite homomorphism `B ─u→ C/𝔍 → C_λ/𝔍_λ = C/(𝔍 + 𝔏_λ)`. Let us show that every `A`-homomorphism `w : B → C` such
that `u` factors as `B ─w→ C → C/𝔍` is necessarily *continuous*; in effect, for every `λ`, there is an open ideal `𝔎` of
`B` such that `u(𝔎) ⊂ (𝔍 + 𝔏_λ)/𝔍`, whence `w(𝔎) ⊂ 𝔍 + 𝔏_λ`, hence there is a power `𝔎^{2^m}` of `𝔎` such that
`w(𝔎^{2^m}) ⊂ 𝔏_λ`, which establishes our assertion since `𝔎^{2^m}` is open in `B`. One can therefore restrict to
finding an `A`-homomorphism `w` having the preceding property without worrying about its continuity properties. Now, the
set `Hom(B, C)` of all `A`-algebra homomorphisms of `B` into `C` is equal to `lim← Hom(B, C_λ)`, and the latter is
*closed* in the `C`-module `C_λ^B`, equipped with the product topology, for which it is *linearly compact* since `C_λ`
is Artinian. For every `λ`, let `W_λ`

<!-- original page 182 -->

be the set of `w_λ ∈ Hom(B, C_λ)` such that `u_λ` factors as `B ─w_λ→ C_λ → C_λ/𝔍_λ`; `W_λ` is a closed linear variety
in the `C`-module `Hom(B, C_λ)`, non-empty since `B` is formally smooth. In the product `∏_{μ ⩽ λ} Hom(B, C_μ) = E_λ`,
consider the linear sub-variety `U_λ` formed by the `(w_μ)_{μ ⩽ λ}` such that `w_μ = φ_{μλ} ∘ w_λ` for `μ ⩽ λ` and
`w_λ ∈ W_λ` (where `φ_{μλ} : C_λ → C_μ` is the canonical homomorphism), which is also closed. Finally, let `V_λ` be the
linear variety in the product `∏_μ Hom(B, C_μ)`, product of `U_λ` and of the `Hom(B, C_μ)` for `μ ⩽̸ λ`, which is still
closed. Everything reduces to seeing that the intersection of the `V_λ` is non-empty, for an element `w` of this
intersection will belong to `lim← Hom(B, C_λ)` by definition. Moreover, since `𝔍` is closed, and `C = lim← C_λ` linearly
compact, `C/𝔍` is identified with `lim← C_λ/𝔍_λ` and the canonical map `φ : C → C/𝔍` with `lim← ψ_λ`, where `ψ_λ` is the
canonical map `C_λ → C_λ/𝔍_λ`. One then concludes as in `(19.3.10)` that `ψ ∘ w = u`.

### 19.4. First criteria for formal smoothness

**Proposition (19.4.1).**

<!-- label: 0_IV.19.4.1 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra; suppose that there exist two decreasing filtering
families `(𝔍_α)_{α ∈ I}`, `(𝔎_α)_{α ∈ I}` of ideals of `A` and `B` respectively, such that: 1° `(𝔍_α)` tends to `0` in
`A` and `(𝔎_α)` tends to `0` in `B`; 2° for every `α ∈ I` one has `𝔍_α B ⊂ 𝔎_α` (so that `B/𝔎_α` is a topological
`(A/𝔍_α)`-algebra); 3° for every `α ∈ I`, `B/𝔎_α` is a formally smooth `(A/𝔍_α)`-algebra. Then `B` is a formally smooth
`A`-algebra.*

Indeed, let `C` be a discrete `A`-algebra, `𝔏` a nilpotent ideal of `C`, `𝔎` an open ideal of `B`; by hypothesis there
is an `α ∈ I` such that `𝔎_α ⊂ 𝔎`, hence `B/𝔎` is a quotient of `B/𝔎_α` by an open ideal. Every `A`-homomorphism
`u' : B/𝔎 → C/𝔏` is also an `(A/𝔍_α)`-homomorphism, hence there exists an open ideal `𝔎'` of `B` such that
`𝔎_α ⊂ 𝔎' ⊂ 𝔎` and that `B/𝔎_α → B/𝔎 ─u'→ C/𝔏` factors as `B/𝔎_α → B/𝔎' ─v'→ C → C/𝔏`, where `v'` is an
`(A/𝔍_α)`-homomorphism; whence the conclusion, by virtue of the remark following `(19.3.1)`.

**Corollary (19.4.2).**

<!-- label: 0_IV.19.4.2 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra, `(𝔍_α)_{α ∈ I}` a decreasing filtering family of ideals
of `A` tending to `0`. For `B` to be a formally smooth `A`-algebra, it is necessary and sufficient that for every
`α ∈ I`, if one sets `A_α = A/𝔍_α`, `B_α = B/𝔍_α B`, `B_α` be a formally smooth `A_α`-algebra.*

The condition is sufficient by `(19.4.1)`, and it is also necessary by `(19.3.5, (iii))`.

**Proposition (19.4.3).**

<!-- label: 0_IV.19.4.3 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra. Suppose that for every discrete `A`-algebra `C` and every
ideal `𝔍` of `C` such that `𝔍² = 0`, every continuous `A`-homomorphism `u : B → C/𝔍` factors as `B → C → C/𝔍`, where `v`
is a continuous `A`-homomorphism. Then `B` is a formally smooth `A`-algebra.*

Indeed, with the same notations, let `𝔎` be an arbitrary nilpotent ideal of `C`, and consider a continuous
`A`-homomorphism `u' : B → C/𝔎`. Suppose that `𝔎^m = 0`, and set `C_i = C/𝔎^i` for `1 ⩽ i ⩽ m`, so that `C_m = C`,
`𝔎^{i−1}/𝔎^i` is an ideal of square zero `𝔍_i` in `C_i`, and `C_{i−1} = C_i/𝔍_i`; the hypothesis then entails by
induction on `i` the existence of continuous `A`-homomorphisms `u_i : B → C_i` such that `u_1 = u'` and that `u_i`
factors as `B ─u_{i+1}→ C_{i+1} → C_{i+1}/𝔍_{i+1} = C_i`; whence the conclusion.

**Proposition (19.4.4).**

<!-- label: 0_IV.19.4.4 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra*

<!-- original page 183 -->

*(commutative). For `B` to be a formally smooth `A`-algebra, it is necessary and sufficient that for every discrete
topological `B`-module `L`, annulled by an open ideal of `B`, one have (cf. `(18.5.1)`) `Exalcotop_A(B, L) = 0`.*

Let `(𝔎_λ)` be a decreasing fundamental system of open ideals of `B` and set `B_λ = B/𝔎_λ`. Consider a discrete
topological `A`-algebra `C` and an ideal `𝔍` of `C` such that `𝔍² = 0`, so that `C` is an `A`-extension of `C/𝔍` by `𝔍`;
suppose given an `A`-homomorphism `u : B_λ → C/𝔍` and form the `A`-extension `E_λ` of `B_λ` by `𝔍`, inverse image of `C`
by the homomorphism `u` `(18.2.5)`; this is a topological `A`-algebra for the discrete topology. If
`Exalcotop_A(B, L) = 0`, there exists by definition `(18.5.1)` a `μ` such that `𝔎_μ ⊂ 𝔎_λ` and such that the inverse
image extension `E_μ` is `A`-trivial; but this means `(18.1.6)` that there exists a continuous `A`-homomorphism
`v : B_μ → E_μ` such that the canonical homomorphism `B_μ → B_λ` factors as `B_μ ─v→ E_μ → B_λ`; one concludes at once
that `B_μ → B_λ → C/𝔍` factors as `B_μ → E_μ → C → C/𝔍`, and this proves, by virtue of `(19.3.1)` and `(19.4.3)`, that
`B` is a formally smooth `A`-algebra. The converse is immediate, by applying `(19.3.1)` to the case where `C` is a
topological `A`-algebra which is an `A`-extension of `B_λ` by `L`, and to the identity homomorphism `B_λ → B_λ = C/L`.

When `A` and `B` are *discrete* rings, the criterion of formal smoothness `(19.4.4)` reduces to

```text
(19.4.4.1)            Exalcom_A(B, L) = 0      for every B-module L;
```

in other words, every commutative `A`-extension of `B` by a `B`-module must be `A`-trivial.

**Corollary (19.4.5).**

<!-- label: 0_IV.19.4.5 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra (commutative).*

*(i) Suppose that `B` is a formally smooth `A`-algebra. Then, for every open ideal `𝔎` of `B`, every `(B/𝔎)`-module `L`
and every `A`-bilinear symmetric Hochschild 2-cocycle `f` from `(B/𝔎) × (B/𝔎)` into `L` `(18.4.3)`, there exists an open
ideal `𝔎' ⊂ 𝔎` such that, if `φ : B/𝔎' → B/𝔎` is the canonical homomorphism, `f ∘ (φ × φ)` is an `A`-bilinear Hochschild
2-coboundary from `(B/𝔎') × (B/𝔎')` into `L`.*

*(ii) If `B` is a formally projective `A`-module `(19.2.1)` and if condition (i) is satisfied, `B` is a formally smooth
`A`-algebra.*

(i) The 2-cocycle `f` defines a Hochschild `A`-extension `C` of `B/𝔎` by `L` `(18.4.3)`. Applying `(19.3.1)` to `C`, to
the square-zero ideal `L` of `C` and to the identity homomorphism `B/𝔎 → B/𝔎 = C/L`, one deduces condition (i) by virtue
of `(18.4.3)`.

(ii) Let us apply criterion `(19.4.3)`, by considering an open ideal `𝔎` of `B`, an open ideal `𝔍` of `A` such that
`𝔍² = 𝔎`, and an `(A/𝔍)`-extension `E` of `B/𝔎` by `L`. Since `B` is a formally projective `A`-module, the canonical
continuous `A`-linear map `p : B → B/𝔎` factors as `B ─w→ E → B/𝔎`, where `w` is a continuous `A`-linear map `(19.2.1)`,
which itself factors as `B → B/𝔎' ─w→ E` where `𝔎'` is an open ideal of `B` contained in `𝔎`; replacing `𝔍` by a smaller
ideal, one may suppose that `𝔍 B ⊂ 𝔎'`. Then the inverse image by the canonical homomorphism `B/𝔎' → B/𝔎` of the
extension `E` of `B/𝔎` by `L` is an `(A/𝔍)`-Hochschild extension `E'` of `B/𝔎'` by `L`;

<!-- original page 184 -->

applying (i) to a cocycle defining this extension `(18.4.3)`, one concludes that there is an open ideal `𝔎'' ⊂ 𝔎'` of
`B` such that the inverse image `E''` of `E` by `B/𝔎'' → B/𝔎'` is `A`-trivial. Q.E.D.

**Corollary (19.4.6).**

<!-- label: 0_IV.19.4.6 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra which is a formally projective `A`-module. Let `A'` be an
`A`-algebra equipped with the topology deduced from that of `A`. Suppose furthermore that `A'` is a faithfully flat
`A`-module, and that one of the following conditions is satisfied:*

*1° There exists a fundamental system `(𝔍_λ)` of open ideals of `A` and a fundamental system `(𝔐_λ)` of open ideals of
`B`, having the same set of indices and such that, for every `λ`, one has `𝔍_λ B ⊂ 𝔐_λ` and that `B/𝔐_λ` is a projective
`(A/𝔍_λ)`-module of finite type.*

*2° `A'` is a projective `A`-module of finite type.*

*Then, for `B' = B ⊗_A A'` (equipped with the tensor product topology) to be a formally smooth `A'`-algebra, it is
necessary and sufficient that `B` be a formally smooth `A`-algebra.*

The sufficiency of the condition is contained in `(19.3.5, (iii))`, without any further hypothesis on `B` or `A'`. To
prove the converse, we shall apply criterion `(19.4.5)`; under hypothesis 2°, we still denote by `(𝔐_λ)` a fundamental
system of open ideals of `B`, and, for every `λ`, by `𝔍_λ` an open ideal of `A` such that `𝔍_λ B ⊂ 𝔐_λ`; in both cases,
we shall set `A_λ = A/𝔍_λ`, `B_λ = B/𝔐_λ`, `A'_λ = A_λ ⊗_A A'`, `B'_λ = B_λ ⊗_A A'`. Let `f` be an `A_λ`-bilinear
symmetric Hochschild 2-cocycle from `B_λ × B_λ` into a `B_λ`-module `L`; by extension of scalars, one deduces a
Hochschild 2-cocycle `f' = f ⊗ 1`, `A'`-bilinear symmetric, from `B'_λ × B'_λ` into `L' = L ⊗_A A'`. Since by hypothesis
`B'` is a formally smooth `A'`-algebra, there exists, by `(19.4.5, (i))`, an index `μ` such that `𝔐_μ ⊂ 𝔐_λ`, and such
that, if `φ' : B'_μ → B'_λ` is the canonical map, `f' ∘ (φ' × φ')` is a Hochschild 2-coboundary from `B'_μ × B'_μ` into
`L'`; in other words, its image `c'` in the Hochschild group `H²_{A'_μ}(B'_μ, L')^s` is zero; it is clear that if
`φ : B_μ → B_λ` is the canonical homomorphism, and `c` the class of `f ∘ (φ × φ)` in the Hochschild group
`H²_{A_μ}(B_μ, L)^s`, `c'` is the canonical image of `c`. Now, if `P_•` is the complex relative to the rings `A_μ` and
`B_μ` defined in `(18.4.5)`, serving for the computation of `H²_{A_μ}(B_μ, L)^s`, the analogous complex relative to the
rings `A'_μ` and `B'_μ` is evidently `P_• ⊗_A A'`; under hypothesis 1°, the construction of `P_•` shows that this is an
`A_μ`-projective module of finite type. One concludes therefore from Bourbaki, Alg., chap. II, 3rd ed., §5, n° 3, prop.
7 that, under both hypotheses, one has `Hom_{A'_μ}(P_• ⊗_A A', L ⊗_A A') = (Hom_{A_μ}(P_•, L)) ⊗_A A'` up to a canonical
isomorphism; since `A'` is a flat `A`-module, one has therefore `(18.4.5)`

```text
                       H²_{A'_μ}(B'_μ, L')^s = (H²_{A_μ}(B_μ, L)^s) ⊗_A A'
```

and one may therefore write `c' = c ⊗ 1`; but since `A'` is a faithfully flat `A`-module, the hypothesis `c' = 0`
entails `c = 0`, which completes the proof.

**Proposition (19.4.7).**

<!-- label: 0_IV.19.4.7 -->

*Let `A` be a preadmissible topological ring, `𝔍` an ideal of definition of `A` `(0_I, 7.1.2)`, `B` a topological
`A`-algebra which is a formally projective `A`-module. Consider the topological quotient rings `A_0 = A/𝔍`,
`B_0 = B/𝔍 B`; then, for `B` to be*

<!-- original page 185 -->

*a formally smooth `A`-algebra, it is necessary and sufficient that `B_0` be a formally smooth `A_0`-algebra.*

The necessity of the condition results from `(19.4.2)`. To see that it is sufficient, note first that by considering a
fundamental system of open neighbourhoods of `0` in `A` formed of ideals `𝔍_α` contained in `𝔍`, one can, by virtue of
`(19.4.2)`, reduce to the case where `A` is *discrete* since `B/𝔍_α B` is a formally projective `(A/𝔍_α)`-module
`(19.2.5)`; by definition of a preadmissible ring, `𝔍` is then *nilpotent*. It moreover suffices to prove the
proposition when `𝔍² = 0`, for if `𝔍^m = 0`, one will apply it successively to the rings `A_k = A/𝔍^k` and
`B_k = B/𝔍^k B` and to the ideal `𝔍^{k−1}/𝔍^k` of `A_k` for `k = 2, 3, …, m`, noting `(19.2.5)` that `B_k = B ⊗_A A_k`
is a formally projective `A_k`-module. Let us apply criterion `(19.4.5, (ii))` by considering an open ideal `𝔎` of `B`
and an `A`-bilinear symmetric Hochschild 2-cocycle `f` from `(B/𝔎) × (B/𝔎)` into a `(B/𝔎)`-module `L`. Let us consider
first the special case where `𝔍 L = 0`, so that `L` may also be considered as a `(B_0/𝔎 B_0)`-module, and `f` factors as

```text
            (B/𝔎) × (B/𝔎) → (B_0/𝔎 B_0) × (B_0/𝔎 B_0) ─f_0→ L
```

where `f_0` is a symmetric bilinear Hochschild 2-cocycle. By virtue of the hypothesis, there is therefore an open ideal
`𝔎' ⊂ 𝔎` in `B` and an `A_0`-linear map `g_0 : B_0/𝔎' B_0 → L` such that
`f_0(φ_0(x), φ_0(y)) = x g_0(y) − g_0(xy) + g_0(x) y` for `x`, `y` in `B_0/𝔎' B_0`, `φ_0 : B_0/𝔎' B_0 → B_0/𝔎 B_0` being
the canonical homomorphism. One concludes at once that the composite `A`-linear map `g : B/𝔎' → B_0/𝔎' B_0 ─g_0→ L` is
such that `dg = f ∘ (φ × φ)`, where `φ : B/𝔎' → B/𝔎` is the canonical homomorphism.

Let us pass now to the general case, and consider first the `(B/𝔎)`-module `L/𝔍 L = L'`, for which one has `𝔍 L' = 0`;
if `f'` is the `A`-bilinear map composed of `(B/𝔎) × (B/𝔎) ─f→ L → L'`, `f'` is still a symmetric Hochschild 2-cocycle,
and by virtue of what precedes, there exist an open ideal `𝔎' ⊂ 𝔎` in `B` and an `A`-linear map `g' : B/𝔎' → L'`
satisfying `dg' = f' ∘ (φ' × φ')` for the canonical map `φ' : B/𝔎' → B/𝔎`. Since `B` is a formally projective
`A`-module, there exist an open ideal `𝔎'_1 ⊂ 𝔎'` and an `A`-linear map `g_1 : B/𝔎'_1 → L` such that the homomorphism
`B/𝔎'_1 → B/𝔎' ─g'→ L'` factors as `B/𝔎'_1 ─g_1→ L → L'`. Consider then the Hochschild 2-cocycle

```text
        f_1(x, y) = f(φ_1(x), φ_1(y)) − x g_1(y) + g_1(xy) − g_1(x) y,
```

an `A`-bilinear symmetric map of `(B/𝔎'_1) × (B/𝔎'_1)` into `L`. The choice of `g_1` entails that `f_1` takes its values
in `𝔍 L`. Since `𝔍(𝔍 L) = 0`, one may once more apply the first case, and there is therefore an open ideal `𝔎'' ⊂ 𝔎'_1`
and an `A`-linear map `g_2 : B/𝔎'' → 𝔍 L` such that

```text
        f_1(φ_2(x), φ_2(y)) = x g_2(y) − g_2(xy) + g_2(x) y
```

in `(B/𝔎'') × (B/𝔎'')`, `φ_2 : B/𝔎'' → B/𝔎'_1` being the canonical map; the `A`-linear map
`g = g_2 + g_1 ∘ φ_2 : B/𝔎'' → L` therefore satisfies `dg = f ∘ (φ × φ)` for the canonical map `φ : B/𝔎'' → B/𝔎`. Q.E.D.

<!-- original page 186 -->

### 19.5. Formal smoothness and associated graded rings

**(19.5.1)** Let `C` be a (commutative) topological ring, let `V` be a topological `C`-module, and consider the
symmetric algebra `S_C(V) = ⊕_n S^n_C(V)`, which we shall endow canonically with a linear topology compatible with its
`C`-algebra structure. For this, let `U` be an open submodule of `V`, and let `U · S_C(V)` be the graded ideal it
generates in `S_C(V)`; we take as fundamental system of neighbourhoods of `0` in `S_C(V)` the set of sums
`𝔞 · S_C(V) + U · S_C(V)`, where `𝔞` (resp. `U`) runs through a fundamental system of open ideals (resp. of open
submodules) of `C` (resp. `V`). Note that if the topology of `V` is coarser than the topology induced from that of `C`,
one may restrict to pairs `(𝔞, U)` such that `𝔞 V ⊂ U`, so that `𝔞 · S_C(V) + U · S_C(V) = 𝔞 · S_C(V) + U · S_C(V)`; in
this case the topology induced on each `S^n_C(V)` for `n ≥ 1` admits as fundamental system of neighbourhoods of `0` the
`U · S^{n-1}_C(V)`, where `U` runs through the open submodules of `V`; in particular, on `V = S^1_C(V)` it coincides
with the given topology (in general it is coarser than the latter). Furthermore, in every case, the topological algebra
`S_C(V)` thus defined is, for the categories of topological `C`-modules and topological `C`-algebras, the solution of
the same universal problem as for the categories of `C`-modules and `C`-algebras. Indeed, let `E` be a topological
`C`-algebra, `u : V → E` a homomorphism of `C`-modules, `S(u) = 𝑣` its canonical extension to `S_C(V)`. Suppose `u` is
continuous; then, if `𝔟` is an open ideal of `E`, its inverse image `u⁻¹(𝔟)` is an open `C`-submodule of `V`, and the
image under `𝑣` of `U · S_C(V)` is therefore contained in `𝔟`; since moreover there exists an open ideal `𝔞` of `C` such
that `𝔞 · E ⊂ 𝔟`, whence `𝑣(𝔞 · S_C(V)) ⊂ 𝔟`, this proves that `𝑣` is continuous. Conversely, if `𝑣` is continuous and
`𝔟` is an open ideal of `E`, there exists an open submodule `U` of `V` such that `𝑣(U · S_C(V)) ⊂ 𝔟`, and in particular
`𝑣(U · S^1_C(V)) ⊂ 𝔟`, that is, `u(U) ⊂ 𝔟`, so `u` is continuous. Recall in addition that one has a canonical
isomorphism of (discrete) topological `C`-modules

```text
(19.5.1.1)                    S_C(V) / U · S_C(V) ⥲ S_{C/𝔞}(V/U).
```

**(19.5.2)** Let `A` be a topological ring, `B` a topological (commutative) `A`-algebra, `𝔍` an ideal of `B` (not
necessarily open or closed); throughout the sequel, we endow `𝔍` and the `𝔍^n` (`n ≥ 2`) with the topology induced from
that of `B`, the quotients `C = B/𝔍`, `𝔍^n/𝔍^{n+1} = gr^n_𝔍(B)` with the quotient topology, so that the `𝔍^n/𝔍^{n+1}`
are topological `C`-modules; the canonical injection `𝔍/𝔍^2 → gr^•_𝔍(B)` extends to a homomorphism (at first
non-topological) of `C`-algebras

```text
                                  φ : S_C(𝔍/𝔍²) → gr^•_𝔍(B)
```

which for each `n` gives a surjective homomorphism of `C`-modules

```text
(19.5.2.1)                  φ_n : S^n_C(𝔍/𝔍²) → 𝔍^n/𝔍^{n+1}.
```

When `S_C(𝔍/𝔍²)` is endowed with the topology defined in `(19.5.1)`, the homomorphisms `φ_n` are continuous, by virtue
of the universal property `(19.5.1)` of `S_C(𝔍/𝔍²)`

<!-- original page 187 -->

applied to the topological `A`-algebra `E = gr^•_𝔍(B/𝔍^{n+1})` endowed with the product topology of those of the
`𝔍^j/𝔍^{j+1}`, and to the canonical injection `𝔍/𝔍² → E`. Note that here the topology on `𝔍/𝔍²` is coarser than the
topology induced from that of `C` (this latter topology on `𝔍/𝔍²` being also the topology induced from that of `B`).

**Theorem (19.5.3).**

<!-- label: 0_IV.19.5.3 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra, `𝔍` an ideal of `B`, `C = B/𝔍` the quotient topological
`A`-algebra. Assume that the `A`-algebra `C` is formally smooth. Then:*

*(i) If `B` is a formally smooth `A`-algebra, `𝔍/𝔍²` is a formally projective topological `C`-module `(19.2.1)`.*

*(ii) If `B` is a formally smooth `A`-algebra and a preadmissible ring `(0_I, 7.1.2)`, the homomorphisms `φ_n`
`(19.5.2)` are formal bimorphisms `(19.1.2)`.*

*(iii) Conversely, suppose that `B` is preadmissible, that the sequence `(𝔍^n)` tends to `0` in `B`, that `𝔍/𝔍²` is a
formally projective `C`-module, and that the `φ_n` are formal bimorphisms. Then `B` is a formally smooth `A`-algebra.*

The proof of this theorem is long and cluttered with technical details; we shall therefore begin by proving a simpler
corollary, in which the guiding ideas appear more clearly; this corollary is moreover the special case of theorem
`(19.5.3)` that will be most frequently used in the sequel.

**Corollary (19.5.4).**

<!-- label: 0_IV.19.5.4 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra, `𝔍` an ideal of `B` such that the topology of `B` is the
`𝔍`-preadic topology. Assume that the discrete `A`-algebra `C = B/𝔍` is formally smooth. Then the following three
conditions are equivalent:*

*a) `B` is a formally smooth `A`-algebra.*

*b) `𝔍/𝔍²` is a projective `C`-module and the canonical homomorphism*

```text
                                      φ : S_C(𝔍/𝔍²) → gr^•_𝔍(B)
```

*is bijective.*

*c) The separated completion `B̂` of `B` is a topological `A`-algebra isomorphic to an `A`-algebra of the form `B̂'`,
where `B' = S_C(V)`, `V` being a projective `C`-module and `B'` being endowed with the `B'⁺`-preadic topology, where
`B'⁺` is the augmentation ideal.*

**(19.5.4.1)** Let us first prove that a) implies that `𝔍/𝔍²` is a projective `C`-module. Let `P` and `Q` be two
`C`-modules, `u : P → Q` a surjective `C`-homomorphism, and `v : 𝔍/𝔍² → Q` a `C`-homomorphism. The ring `B/𝔍²`,
considered as a `B`-extension of `C` by `𝔍/𝔍²`, gives by `v` a `B`-extension `E = (B/𝔍²) ⊕_{𝔍/𝔍²} Q` of `C` by `Q`
`(18.2.8)`. Since `C` is a formally smooth discrete `A`-algebra, the extension `E` is `A`-trivial `(19.4.4)` and can
therefore be identified with `D_C(Q)` `(18.2.3)`. The surjective homomorphism `u : P → Q` then canonically defines a
surjective `A`-homomorphism `ũ : D_C(P) → D_C(Q)` `(18.2.9)` whose kernel is an ideal `𝔞` of the extension
`E' = D_C(P)`, contained in `P`, and a fortiori of square zero. Let `f : B → E = E'/𝔞` be the homomorphism defining the
`B`-algebra structure of `E`; since `𝔞` is of square zero and `B` is a formally smooth

<!-- original page 188 -->

`A`-algebra, `f` factors as `B → E' → E'/𝔞`, where `g` is a continuous `A`-homomorphism. The diagram

```text
                                          g
                                   B ────────→ E'
                                   │           │
                                   │           ↓ ũ
                                   ↓
                                  B/𝔍² ──────→ E
                                          v'
```

where `v'` is deduced from `v` `(18.2.8)`, is commutative. Furthermore, the image of `𝔍` under `ũ ∘ g` is contained in
`Q`, so the image of `𝔍` under `g` is contained in `P + 𝔞 = P`, and the image of `𝔍²` under `g` is zero. Restricting `g`
and `ũ` to `𝔍`, we obtain a commutative diagram

```text
                                          u
                                  P ──────────→ Q
                                   ↖           ↗
                                     ↖       ↗
                                       w   v
                                          ↘
                                       𝔍/𝔍²
```

which proves that the `C`-module `𝔍/𝔍²` is projective.

**(19.5.4.2)** Let us prove next that a) implies that `φ` is bijective, which will complete the proof that a) implies
b). Set `E_n = B/𝔍^{n+1}`, and denote by `F_n` the quotient of `S_C(𝔍/𝔍²)` by the `(n+1)`-st power of its augmentation
ideal. Since `𝔍^{n+1}` is nilpotent in `E_n` and `C` is a formally smooth discrete `A`-algebra, the identity
automorphism of `C` factors as `C → E_n → C = E_n/(𝔍^{n+1})` where `f` is an `A`-homomorphism; on the other hand, since
`𝔍/𝔍²` is a projective `C`-module by `(19.5.4.1)`, the identity automorphism of `𝔍/𝔍²` factors as
`𝔍/𝔍² → 𝔍/𝔍^{n+1} → 𝔍/𝔍²`, where `g` is a `C`-linear map; from `f` and `g` one obtains canonically a homomorphism of
`C`-algebras `S_C(𝔍/𝔍²) → E_n` which moreover (by definition of `g`) vanishes on the `(n+1)`-st power of the
augmentation ideal of `S_C(𝔍/𝔍²)`, whence, on passing to the quotient, a surjective `A`-homomorphism of algebras
`𝑣 : F_n → E_n` such that `gr⁰(𝑣)` and `gr¹(𝑣)` are the identity automorphisms of `C` and `𝔍/𝔍²`. By definition of the
canonical homomorphism `φ`, one sees that `gr^j(𝑣) = φ_j` for every `j ≤ n`. Note now that the kernel `𝔑` of `𝑣` is a
nilpotent ideal of `F_n`, so that `E_n` may be identified with `F_n/𝔑`. Since `B` is a formally smooth `A`-algebra, the
canonical `A`-homomorphism `p_n : B → E_n = B/𝔍^{n+1}`, which is continuous, factors as `B → F_n → E_n`, where `w` is a
continuous `A`-homomorphism; since `gr⁰(𝑣)` is the identity, `w(𝔍)` is contained in the augmentation ideal of `F_n`,
whence `w(𝔍^{n+1}) = 0`, so that `w` factors as `B → B/𝔍^{n+1} → F_n → E_n`, and the composite `E_n → F_n → E_n` is the
identity. Furthermore, since `gr⁰(𝑣)` and `gr¹(𝑣)` are the identity automorphisms of `C` and `𝔍/𝔍²`, the same is true of
`gr⁰(w')` and `gr¹(w')`. Since `gr^•(E_n)` is generated by `gr¹(E_n)`, the composite homomorphism

```text
                                                  gr^j(w')           gr^j(𝑣)
                              gr^j(E_n) ──────────────→ gr^j(F_n) ──────────→ gr^j(E_n)
```

is the identity for every `j ≤ n`, since this is true for `j = 0` and `j = 1`; taking `j = n`, one thus proves that
`φ_n` is injective, which completes the proof that a) implies b).

<!-- original page 188 -->

**(19.5.4.3)** Let us prove next that b) implies a). The same reasoning as at the beginning of `(19.5.4.2)` proves the
existence of a surjective `A`-homomorphism of algebras `𝑣 : F_n → E_n` such that `gr^j(𝑣) = φ_j` for every `j`; since
`φ_j` is bijective for every `j` and the filtrations of `F_n` and `E_n` are finite, one concludes that `𝑣` is bijective
`(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1)`. Now let `G` be a discrete topological `A`-algebra, `𝔑`
an ideal of square zero in `G`, `f : B → G/𝔑` a continuous `A`-homomorphism of algebras. Since `G` is discrete, there
exists an integer `m` such that `f` vanishes on `𝔍^m`, so `f` factors as `B → E_m → G/𝔑`, where one takes `n = 2m`. One
thus obtains by composition a continuous `A`-homomorphism of algebras `r : C → F_n → E_m → G/𝔑`, and since `C` is a
formally smooth discrete `A`-algebra, `r` factors as `C → G → G/𝔑`, so that `G` is equipped by `r'` with a `C`-algebra
structure. On the other hand, the restriction to `𝔍/𝔍²` of the homomorphism `f_n : F_n → E_n → G/𝔑` is a `C`-linear map
`g : 𝔍/𝔍² → G/𝔑`. Since `𝔍/𝔍²` is a projective `C`-module, `g` factors as `𝔍/𝔍² → G → G/𝔑`, where `h` is a `C`-linear
map; by extension, one deduces a homomorphism of `C`-algebras `w : S_C(𝔍/𝔍²) → G`, and by construction every element of
degree `m` has under `w` an image which is an element of `𝔑`, so every element of degree `n = 2m` has image zero, since
`𝔑² = 0`; in other words, `w` factors as `S_C(𝔍/𝔍²) → F_n → G`. By construction, the composite `F_n → G → G/𝔑` coincides
with `f_n` on `C` and on `𝔍/𝔍²`, so is equal to `f_n`. Finally, the composite

```text
                                 B → E_m → F_n → G → G/𝔑
```

being equal to `f`, one sees that `B` is a formally smooth `A`-algebra.

**(19.5.4.4)** It remains to prove the equivalence of a) and c). First, c) implies a): indeed, `B'` is a formally smooth
`C`-algebra for the discrete topology `(19.3.2)`, hence also for the `B'⁺`-preadic topology `(19.3.8)`; since `C` is a
formally smooth `A`-algebra, `B'` is also a formally smooth `A`-algebra `(19.3.5, (ii))` and finally `B̂'` is a formally
smooth `A`-algebra `(19.3.6)`, so `B` is a formally smooth `A`-algebra `(19.3.6)`. It remains to see that a) implies c).
Note first that since `C` is a formally smooth `A`-algebra, the identity homomorphism `C → B/𝔍` factors as
`C → B → B/𝔍`, where `C → B` is an `A`-homomorphism `(19.3.10)`; `B`, and consequently all the `B/𝔍^{n+1}`, are thus
endowed with `C`-algebra structures. On the other hand, since `𝔍/𝔍²` is a projective `C`-module by b), the canonical
injection `𝔍/𝔍² → B/𝔍²` allows one to form a projective system of `C`-homomorphisms `v_n : 𝔍/𝔍² → B/𝔍^{n+1}` for
`n ≥ 1`, hence also (by the universal property of the symmetric algebra) a projective system of homomorphisms of
`C`-algebras `𝑣_n : S_C(𝔍/𝔍²) = B' → B/𝔍^{n+1}`; moreover it is clear that `𝑣_n` vanishes on `(B'⁺)^{n+1}` and since
`gr⁰(𝑣_n) = φ_0` and `gr¹(𝑣_n) = φ_1`, one has `gr^j(𝑣_n) = φ_j` for `0 ≤ j ≤ n`. Since the `φ_j` are isomorphisms by
b), and the filtrations of `B'/(B'⁺)^{n+1}` and of `B/𝔍^{n+1}` are finite, one concludes that `𝑣_n` is bijective for

<!-- original page 189 -->

every `n` `(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1)`; whence c) by passage to the projective limit.

**Remark (19.5.5).**

<!-- label: 0_IV.19.5.5 -->

*Under the general hypotheses of `(19.5.4)`, suppose in addition that `𝔍` is a maximal ideal of `B`, so that `C = B/𝔍`
is a field, and that `𝔍/𝔍²` is a `C`-vector space of finite dimension. Then conditions a), b) and c) of `(19.5.4)` are
also equivalent to the following:*

*d) Given a polynomial algebra `E = C[T_1, …, T_n]` over the field `C`, and denoting by `𝔫` the maximal ideal of `E`
generated by the `T_i` (`1 ≤ i ≤ n`), then, for every ideal `𝔟` of `E` containing some power `𝔫^h`, every homomorphism
`v : B → E/𝔟` of `C`-augmented `A`-algebras factors as `B → E/𝔫^h → E/𝔟`, where `w` is an `A`-homomorphism.*

Indeed, since `𝔍/𝔍²` is here a free `C`-module, it suffices to verify that condition d) implies that the canonical
homomorphism `φ : S_C(𝔍/𝔍²) → gr^•_𝔍(B)` is bijective. Now here `S_C(𝔍/𝔍²)` is identified with the polynomial algebra
`E = C[T_1, …, T_n]`, where `n = rg_C(𝔍/𝔍²)`, and the augmentation ideal of `E` is the ideal `𝔫` generated by the `T_i`.
For every integer `k ≥ 0`, the hypothesis that `C` is a formally smooth discrete `A`-algebra entails, as in
`(19.5.4.2)`, the existence of a surjective `A`-homomorphism `f : E/𝔫^{k+1} → B/𝔍^{k+1}`, such that `gr^j(f) = φ_j` for
every `j ≤ k`. If `𝔟/𝔫^{k+1} = Ker(f)`, `B/𝔍^{k+1}` is thus identified with `E/𝔟`, and the hypothesis d) allows one to
factor the canonical homomorphism `B → B/𝔍^{k+1}` as `B → E/𝔫^{k+1} → B/𝔍^{k+1}`; since `gr⁰(f)` is the identity, one
has `w(𝔍) ⊂ 𝔫/𝔫^{k+1}`, so `w(𝔍^{k+1}) = 0`; one concludes as in `(19.5.4.2)` that `φ_k` is injective for every `k`,
which completes the proof of our assertion.

**(19.5.6)** *Proof of theorem `(19.5.3)`.* Let `(𝔟_α)` be a decreasing fundamental system of open ideals of `B`. We
shall set

```text
                              B_α = B/𝔟_α,        C_α = B/(𝔟_α + 𝔍),        𝔍_α = (𝔟_α + 𝔍)/𝔟_α,
```

so that

```text
                             C_α = B_α/𝔍_α,    and    𝔍_α^{n+1} = (𝔟_α + 𝔍^{n+1})/(𝔟_α + 𝔍^{n+1}).
```

The `C`-modules `((𝔟_α ∩ 𝔍^n) + 𝔍^{n+1})/𝔍^{n+1}` of `𝔍^n/𝔍^{n+1}` form a fundamental system of open submodules of the
topological `C`-module `𝔍^n/𝔍^{n+1}`; since `(𝔟_α ∩ 𝔍^n) + 𝔍^{n+1} = 𝔟_α ∩ (𝔍^n + 𝔍^{n+1})`, one has

```text
                   𝔍^n/((𝔟_α ∩ 𝔍^n) + 𝔍^{n+1}) = 𝔍^n/(𝔍^n ∩ (𝔟_α + 𝔍^{n+1})) = (𝔍^n + 𝔍^{n+1})/(𝔟_α + 𝔍^{n+1}) = 𝔍_α^n/𝔍_α^{n+1}.
```

**(19.5.6.1)** *Proof of `(19.5.3, (i))`.* Let `P`, `Q` be two discrete `C_α`-modules, `u : P → Q` a surjective
`C_α`-homomorphism. The discrete ring `B/(𝔟_α + 𝔍²)` is a `B`-extension of `C_α` by the square-zero ideal `𝔍_α/𝔍_α²`.
Let `v : 𝔍/𝔍² → Q` be a continuous `C`-homomorphism; replacing `𝔟_α` if needed by a smaller open ideal of `B`, one may
suppose that the kernel of `v` contains the open `C`-submodule `((𝔟_α ∩ 𝔍) + 𝔍²)/𝔍²`; passing to the quotient, one
deduces from `v` a `C_α`-homomorphism of discrete modules `v' : 𝔍_α/𝔍_α² → Q`; let `E_α` be the `B_α`-extension of `C_α`
by `Q` deduced from `B/(𝔟_α + 𝔍²)` by means of `v'`, and let `h : B/(𝔟_α + 𝔍²) → E_α` be the corresponding
`B_α`-homomorphism `(18.2.8)`; `E_α` is

<!-- original page 190 -->

a discrete topological `A`-algebra, and the canonical isomorphism `C_α ⥲ E_α/Q` gives by composition a continuous
`A`-homomorphism `f : C → C_α → E_α/Q`. But since `Q` is of square zero in `E_α` and `C` is a formally smooth
`A`-algebra, `f` factors as `C → E_α → E_α/Q`, where `g` is a continuous `A`-homomorphism. Since `g` is continuous and
`E_α` discrete, there exists `β ≥ α` such that `g` factors as `C → C_β → E_α`. On the other hand, let `E_β` be the
`A`-extension of `C_β` by `Q`, inverse image of `E_α` under the canonical homomorphism `C_β → C_α`; the existence of
`g'` (such that the composite `C_β → E_β → C_β` is the canonical homomorphism) is equivalent to the fact that `E_β` is
an `A`-trivial extension, and so can be identified with `D_β(Q)`. This being so, the surjective homomorphism `u : P → Q`
canonically defines a surjective homomorphism `D_β(P) → D_β(Q)` `(18.2.9)`, whose kernel is an ideal `𝔖` of the
extension `E'_β = D_β(P)` contained in `P`, and a fortiori of square zero. Let `h' : B → E'_β = E_β/𝔖` be the continuous
`A`-homomorphism defining the topological `B`-algebra structure on `E_β`; since `𝔖` is of square zero and `B` is a
formally smooth `A`-algebra, `h'` factors as `B → E'_β → E_β/𝔖`, where `h'` is a continuous `A`-homomorphism. The
construction of `E_β` gives by composition an `A`-homomorphism `t : E'_β → E_β → E_α`, and it is clear that the diagram

```text
                                                t
                                       E'_β ──────→ E_α
                                        │           ↑
                                      h'│           │ h
                                        ↓           │
                                        B ──────→ B/(𝔟_α + 𝔍²)
```

is commutative. Furthermore, the image under `t ∘ h'` of `𝔍` is contained in `Q`, so the image under `h'` of `𝔍` is
contained in `P`, and the image of `𝔍²` under `h'` is zero. Restricting `h'` and `g'` to `𝔍`, one obtains a commutative
diagram

```text
                                          u
                                       P ──→ Q
                                        ↖   ↗
                                          ↗
                                       𝔍/𝔍²
```

where `w` is continuous, which proves that `𝔍/𝔍²` is a formally projective `C`-module.

**(19.5.6.2)** For every integer `n ≥ 0`, we shall set

```text
                                E_n = B/𝔍^{n+1},                          so that E_0 = C;
```

the ideals `(𝔟_α + 𝔍^{n+1})/𝔍^{n+1}` form a fundamental system of open ideals in `E_n`, and we shall set

```text
                                E_{α,n} = B/(𝔟_α + 𝔍^{n+1}) = E_n/(𝔟_α + 𝔍^{n+1})/𝔍^{n+1},
```

a discrete quotient ring. Likewise, in `gr^n_𝔍(B) = 𝔍^n/𝔍^{n+1}`, we have seen that the
`((𝔟_α ∩ 𝔍^n) + 𝔍^{n+1})/𝔍^{n+1}` form a fundamental system of neighbourhoods of `0`, the quotient of `𝔍^n/𝔍^{n+1}` by
this submodule being canonically identified with `𝔍_α^n/𝔍_α^{n+1}`. Consider the symmetric algebra `S_C(𝔍_α/𝔍_α²)`; we
denote by `F_{α,n}` the quotient of `S_{C_α}(𝔍_α/𝔍_α²)` by the `(n+1)`-st power of its augmentation ideal. For a fixed
`n ≥ 1`, it follows from `(19.5.1.1)` that the `S_{C_α}^n(𝔍_α/𝔍_α²)` are the quotients of `S_C^n(𝔍/𝔍²)` by a fundamental
system of open submodules in this topological `C`-module.

To abbreviate the language, we shall say that for `α ≤ β`, the canonical homomorphisms `B_β → B_α`, `C_β → C_α`,
`𝔍_β/𝔍_β² → 𝔍_α/𝔍_α²`, `E_{β,n} → E_{α,n}`, `F_{β,n} → F_{α,n}`, etc., are the *transition homomorphisms*.

**Lemma (19.5.6.3).**

<!-- label: 0_IV.19.5.6.3 -->

*Suppose that the `A`-algebra `C` is formally smooth, the ring `B` preadmissible, and the `C`-module `𝔍/𝔍²` formally
projective. Then:*

*(i) For every `α`, there exists `β ≥ α` and a surjective `A`-homomorphism of algebras*

```text
                                              𝑣_{αβ} : F_{β,n} → E_{α,n}
```

*such that `gr⁰(𝑣_{αβ}) : C_β → C_α` and `gr¹(𝑣_{αβ}) : 𝔍_β/𝔍_β² → 𝔍_α/𝔍_α²` are the transition homomorphisms.*

*(ii) If `β ≥ α` and `𝑣_{αβ}` satisfy the conditions of (i), then, for every `γ ≥ β`, there exists `δ ≥ γ` and a
surjective `A`-homomorphism of algebras `𝑣_{γδ} : F_{δ,n} → E_{γ,n}` satisfying the conditions of (i) (for `γ ≤ δ`) and
making the following diagram commute*

```text
                                                 𝑣_{αβ}
                                       F_{β,n} ──────→ E_{α,n}
                                                                                     
(19.5.6.4)                                ↑              ↑
                                                                                     
                                       F_{δ,n} ──────→ E_{γ,n}
                                                 𝑣_{γδ}
```

*where the vertical arrows are the transition homomorphisms.*

(i) In the discrete topological `A`-algebra `E_{α,n}`, the ideal `𝔍_α/𝔍_α^{n+1}` is nilpotent, and the identity
isomorphism `C_α → E_{α,n}/(𝔍_α/𝔍_α^{n+1})` gives by composition a continuous `A`-homomorphism
`C → C_α → E_{α,n}/(𝔍_α/𝔍_α^{n+1})`;

<!-- original page 191 -->

since `C` is a formally smooth `A`-algebra, this homomorphism factors as `C → E_{α,n} → E_{α,n}/(𝔍_α/𝔍_α^{n+1})`, where
`f_α` is a continuous `A`-homomorphism; consequently, `𝔍_α/𝔍_α^{n+1}` becomes, by means of `f_α`, a discrete topological
`C`-module annihilated by an open ideal of `C`. The hypothesis that `𝔍/𝔍²` is a formally projective `C`-module then
entails the existence of a continuous `C`-linear map `g_α : 𝔍/𝔍² → 𝔍_α/𝔍_α^{n+1}` making commutative the diagram

```text
                                       𝔍_α/𝔍_α² ─→ 𝔍_α/𝔍_α^{n+1}
                                          ↑              ↑
                                          │            g_α
                                                
                                              𝔍/𝔍²
```

Since `f_α` and `g_α` are continuous, there exists `β ≥ α` such that these homomorphisms factor respectively as

```text
                                              C → C_β → E_{α,n}
                                              𝔍/𝔍² → 𝔍_β/𝔍_β² → 𝔍_α/𝔍_α^{n+1}
```

and from `f_{αβ}` and `g_{αβ}`, one thus obtains canonically a homomorphism of `C_β`-algebras

```text
                                            S_{C_β}(𝔍_β/𝔍_β²) → E_{α,n}
```

which moreover (by definition of `g_{αβ}`) vanishes on the `(n+1)`-st power of the augmentation ideal of
`S_{C_β}(𝔍_β/𝔍_β²)`; passing to the quotient by this `(n+1)`-st power, one obtains the desired homomorphism `𝑣_{αβ}`,
taking into account the definitions of `f_{αβ}` and `g_{αβ}`; the surjectivity of `𝑣_{αβ}` follows in fact from that of
the two homomorphisms `gr⁰(𝑣_{αβ})` and `gr¹(𝑣_{αβ})`, since this entails that `gr(𝑣_{αβ})` is surjective (the algebra
`gr^•(E_{α,n})` being generated by `gr⁰(E_{α,n})` and `gr¹(E_{α,n})`), and since the filtrations considered are finite,
one may apply `Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1`.

(ii) The hypothesis that `B` is preadmissible means that one may suppose all the `𝔟_α` contained in a single `𝔟_{α_0}`
whose powers tend to `0`. This entails in particular that the kernel of the transition homomorphism `E_{δ,n} → E_{γ,n}`,
equal to `(𝔟_γ + 𝔍^{n+1})/(𝔟_δ + 𝔍^{n+1})`, is nilpotent; applying lemma `(19.3.10.1)`, one sees that one may suppose
`f_γ` chosen so that the diagram

```text
                                                f_γ
                                       C ──────────→ E_{γ,n}
                                       │             │
                                                     ↓
                                                 E_{α,n}
```

(where the vertical arrow is the transition homomorphism) is commutative. The hypothesis that `𝔍/𝔍²` is a formally
projective `C`-module on the other hand allows one to choose `g_γ : 𝔍/𝔍² → 𝔍_γ/𝔍_γ^{n+1}` so that the diagram

```text
                                        g_γ
                                𝔍_γ/𝔍_γ^{n+1} ────────────
                                       ↑                  │
                                                          ↓
                                       𝔍/𝔍²            𝔍_α/𝔍_α^{n+1}
                                          
                                                     g_α (∘ transition)
```

is commutative (it suffices to remark that the image of `(g_α, p_γ)` of `𝔍/𝔍²` in the product module
`(𝔍_α/𝔍_α^{n+1}) × (𝔍_γ/𝔍_γ^{n+1})` is contained (in view of the definition of `g_α` and the relation `α ≤ γ`) in the
canonical image `Q` in this product module of the

<!-- original page 192 -->

module `P = 𝔍_γ/𝔍_γ^{n+1}`, and to apply the definition `(19.2.1)` to the surjective homomorphism `P → Q` and to the
homomorphism `(g_α, p_γ)` of `𝔍/𝔍²` into `Q`). This choice of `f_γ` and `g_γ` then allows one, by constructing `𝑣_{γδ}`
as in (i), to obtain in addition the commutativity of the diagram `(19.5.6.4)`.

**Lemma (19.5.6.5).**

<!-- label: 0_IV.19.5.6.5 -->

*Suppose that the `A`-algebras `B` and `C` are formally smooth and `B` is preadmissible (so that by virtue of
`(19.5.6.1)` the conditions of `(19.5.6.3)` are satisfied). For every system of two indices `α ≤ β` and a homomorphism
`𝑣_{αβ}` satisfying the conditions of `(19.5.6.3, (i))`, there exists an index `λ ≥ β` and an `A`-homomorphism of
algebras*

```text
                                                w_{βλ} : E_{λ,n} → F_{β,n}
```

*such that: 1° `gr⁰(w_{βλ}) : C_λ → C_β` and `gr¹(w_{βλ}) : 𝔍_λ/𝔍_λ² → 𝔍_β/𝔍_β²` are the transition homomorphisms; 2°
the composite `E_{λ,n} → F_{β,n} → E_{α,n}` is the transition homomorphism.*

Apply lemma `(19.5.6.3, (ii))` with `γ = β`, which gives a `δ ≥ β` and a `𝑣_{βδ} : F_{δ,n} → E_{β,n}`. Recall that
`𝑣_{βδ}` is surjective; on the other hand, its kernel `𝔑` is nilpotent: indeed, the augmentation ideal `F_{δ,n}^+` of
`F_{δ,n}` is nilpotent by definition, and the kernel of `gr⁰(𝑣_{βδ}) : C_δ → C_β` is also nilpotent by virtue of the
hypothesis that `B` is preadmissible. One thus sees that `E_{β,n}` is identified with `F_{δ,n}/𝔑`. Since `B` is a
formally smooth `A`-algebra, the canonical `A`-homomorphism `p_β : B → E_{β,n}`, which is continuous, factors as
`B → F_{δ,n} → E_{β,n}`, where `w` is a continuous `A`-homomorphism. Since `F_{δ,n}` is discrete, there exists `λ ≥ δ`
such that `w` is zero on `𝔟_λ`, so `w` factors as `B → B/𝔟_λ → F_{δ,n}`. Consider the composite homomorphism
`w_{βλ}^* : B/𝔟_λ → F_{δ,n} → F_{β,n}`, where `q_{βδ}` is the transition homomorphism; note that
`gr⁰(q_{βδ}) = gr⁰(𝑣_{βδ}) : C_δ → C_β` is the transition homomorphism; since the composite `q_{βδ} ∘ w` is the
canonical homomorphism `B/𝔟_λ → B/(𝔟_β + 𝔍^{n+1})`, this shows that the image of `(𝔟_λ + 𝔍)/𝔟_λ` under `w_{βλ}^*` is
contained in the augmentation ideal `F_{β,n}^+`, and consequently the image under `w_{βλ}^*` of
`𝔍_λ^{n+1} = (𝔟_λ + 𝔍^{n+1})/𝔟_λ` is zero. In other words, `w_{βλ}^*` factors as

```text
                                  B/𝔟_λ → B/(𝔟_λ + 𝔍^{n+1}) = E_{λ,n} → F_{β,n}
                            w_{βλ}^*        w_{βλ}
```

such that the composite `E_{λ,n} → F_{β,n} → E_{α,n}` is the transition homomorphism. The preceding reasoning also shows
that `gr⁰(w_{βλ})`, which is the composite `B/(𝔟_λ + 𝔍) → gr⁰(F_{δ,n}) → gr⁰(F_{β,n})`, is the transition homomorphism
`C_λ → C_β`, since `q_{βδ} ∘ w_{βλ}` is the canonical homomorphism. In addition, one also has
`gr¹(w_{βλ}) = gr¹(w_{βδ})` (where `w_{βδ} = q_{βδ} ∘ w`), so the same reasoning proves that `gr¹(w_{βλ})` is the
transition homomorphism.

**(19.5.6.6)** *Proof of `(19.5.3, (ii))`.* To show that `φ_n` is a formal bimorphism, we shall apply the criterion of
`(19.1.3, (iii))`. The conditions of `(19.5.6.5)` being satisfied by hypothesis, let us determine, for every index `α`,
`𝑣_{αβ}` and `w_{βλ}` satisfying the conclusions of this lemma. The homomorphism

```text
                                        gr^n(𝑣_{αβ}) : gr^n(F_{β,n}) → gr^n(E_{α,n})
```

is none other than the homomorphism

```text
                                       φ_{αβ,n} : S_C^n(𝔍_β/𝔍_β²) → 𝔍_α^n/𝔍_α^{n+1}
```

deduced from the canonical homomorphism `φ_n` `(19.5.2.1)` by passage to the quotients; indeed, it follows from
`(19.5.6.3)` that `gr⁰(𝑣_{αβ})` and `gr¹(𝑣_{αβ})` coincide respectively with `φ_{αβ,0}` and `φ_{αβ,1}`, and the
definition of the canonical homomorphism `φ` then shows, by recurrence on `j ≤ n`, that `gr^j(𝑣_{αβ})` and `φ_{αβ,j}`
are equal for every `j`. This being so, since `𝑣_{αβ}` is surjective, it is *a fortiori* a formal epimorphism; in
addition, for `j ≤ n`, the composite homomorphism

```text
                                        gr^j(F_{β,n}) → gr^j(E_{α,n}) → gr^j(F_{α,n})
```

is the transition homomorphism, for this is true for `j = 0` and `j = 1` by virtue of `(19.5.6.5)`, and since
`gr^•(E_{α,n})` is generated by `gr¹(E_{α,n})` this proves the assertion by recurrence on `j`. Composing with the
transition homomorphism `gr^j(F_{β,n}) → gr^j(F_{α,n})`, one thus sees, for `j = n`, that one has factored the
transition homomorphism `gr^n(F_{β,n}) → gr^n(F_{α,n})` as

```text
                                           φ_{αβ,n}
                                    S_C^n(𝔍_β/𝔍_β²) → 𝔍_α^n/𝔍_α^{n+1} → gr^n(F_{α,n})
```

which is the condition of the criterion `(19.1.3)` for `φ_n` to be a formal bimorphism.

<!-- original page 193 -->

**Lemma (19.5.6.7).**

<!-- label: 0_IV.19.5.6.7 -->

*Suppose that `B` is preadmissible, that `𝔍/𝔍²` is a formally projective `C`-module, that `C` is a formally smooth
`A`-algebra, and that the `φ_n` are formal bimorphisms. Then, for every pair of indices `α ≤ β` and every homomorphism
`𝑣_{αβ} : F_{β,n} → E_{α,n}` satisfying the conditions of `(19.5.6.3, (i))`, there exists an index `γ ≥ β` such that,
for every index `μ ≥ γ`, one has a commutative diagram of `A`-homomorphisms*

```text
                                                  𝑣_{αβ}
                                       F_{β,n} ──────→ E_{α,n}
                                          ↑              ↑
                                                       
                                       F_{μ,n} ←────── E_{μ,n}
                                                u_{αμ}
```

*where `p_{αμ}` is the transition homomorphism.*

Applying the criterion `(19.1.3)` to each of the `φ_j` for `0 ≤ j ≤ n`, one sees that there exists an index `γ ≥ β` and
uniquely determined (and surjective) homomorphisms of `C_γ`-modules

```text
                                          w_n : gr^n(E_{γ,n}) → gr^n(F_{β,n})
```

such that the composites

```text
                                                 φ_{γγ,n}        w_n
                                        gr^n(F_{γ,n}) ──────→ gr^n(E_{γ,n}) ──────→ gr^n(F_{β,n})
```

are the transition homomorphisms (the fact that one can choose the same index `γ` for all the `w_j` results from the
fact that they are finite in number). Furthermore, the uniqueness of the `w_n` proves (since `φ` is a homomorphism of
graded algebras) that `w_• = (φ_{γγ})^{-1} ∘ w_•^*` is a homomorphism of `C_γ`-algebras
`gr^•(E_{γ,n}) → gr^•(F_{β,n}) = F_{β,n}`. In addition, since `φ_{γγ,0}` and `φ_{γγ,1}` are the identity homomorphisms,
`w_0 : C_γ → C_β` and `w_1 : 𝔍_γ/𝔍_γ² → 𝔍_β/𝔍_β²` are the transition homomorphisms, and the same is therefore true of
`gr⁰(𝑣_{αβ} ∘ w_•)` and `gr¹(𝑣_{αβ} ∘ w_•)`; since `gr^•(E_{γ,n})` is generated by `gr¹(E_{γ,n})`, one concludes that
`gr^j(𝑣_{αβ} ∘ w_•)` is also the transition homomorphism for `0 ≤ j ≤ n`. Applying now to `α`, `β` and `γ` the lemma
`(19.5.6.3, (ii))`, this gives the diagram `(19.5.6.4)` with `δ ≥ γ`; then repeat the reasoning of the beginning by
replacing `α` and `β` by `γ` and `δ`. One thus obtains an index `λ ≥ δ` and a commutative diagram of homomorphisms

```text
                                                w_•           𝑣_{γδ}
                                       gr^•(E_{γ,n}) ──→ F_{δ,n} ──→ E_{γ,n}
                                              ↑           ↑           ↑
                                                                      
                                              ↑          q_{βδ}       │ p_{αγ}
                                       gr^•(E_{λ,n}) ──→ F_{λ,n} ──→ E_{λ,n}
```

where the vertical arrows are the transition homomorphisms. Everything boils down to proving the existence of the
homomorphism `u_{αμ}` leaving the diagram commutative, and for this it is obviously enough to show that one has
`Ker(𝑣_{γδ}) ⊂ Ker(q_{βδ})`, `𝑣_{γδ}` and `q_{βδ}` being surjective. Since `w_•` is surjective, this last relation is
equivalent to `Ker(𝑣_{γδ} ∘ w_•) ⊂ Ker(q_{βδ} ∘ w_•) = Ker(w_{βλ} ∘ (gr(p_{γλ})))`. But it was seen above that
`gr(p_{γλ}) = gr(𝑣_{γδ} ∘ w_•)` and it is clear that
`Ker(𝑣_{γδ} ∘ w_{δμ}) ⊂ Ker(gr(𝑣_{γδ} ∘ w_{δμ})) = Ker(gr(p_{γλ})) ⊂ Ker(w_{βλ} ∘ (gr(p_{γλ})))`, which completes the
proof of the lemma, for any `μ ≥ γ`, it will suffice to define `u_{αμ}` as the composite `E_{μ,n} → E_{γ,n} → F_{β,n}`.

**(19.5.6.8)** *Proof of `(19.5.3, (iii))`.* Let `G` be a discrete topological `A`-algebra, `𝔑` an ideal of square zero
in `G`, `f : B → G/𝔑` a continuous `A`-homomorphism of algebras. Since `G/𝔑` is discrete, there is an index `α` such
that `f` vanishes on `𝔟_α`; by hypothesis, there exists an integer `m` such that `𝔍^m ⊂ 𝔟_α`, so `f` factors as

```text
                                                        p_α
                                              B ──────→ E_{α,n} ──────→ G/𝔑
                                                         f_α
```

where one takes `n = 2m`. The hypotheses of lemma `(19.5.6.3)` being satisfied, one has first of all a `β ≥ α` and a
composite `A`-homomorphism

```text
(19.5.6.9)                                  f_{α,n} ∘ 𝑣_{αβ} : F_{β,n} → E_{α,n} → G/𝔑
```

and since `F_{β,n}` is a `C_β`-algebra, hence *a fortiori* a topological (discrete) `C`-algebra, this gives by
composition a continuous `A`-homomorphism `r : C → F_{β,n} → G/𝔑`. Since on the other hand `C` is a formally smooth
`A`-algebra,

<!-- original page 194 -->

this homomorphism factors as `r : C → G → G/𝔑` where `r'` is a continuous `A`-homomorphism, so that `G` is thus endowed
with a structure of topological (discrete) `C`-algebra. On the other hand, by composition with the canonical
homomorphism

```text
                                            𝔍/𝔍² → 𝔍_β/𝔍_β² → F_{β,n}
```

one deduces from `(19.5.6.9)` a continuous `C`-homomorphism `g : 𝔍/𝔍² → G/𝔑`. Since `𝔍/𝔍²` is a formally projective
`C`-module, `g` factors as `𝔍/𝔍² → G → G/𝔑`, where `h` is a continuous `C`-homomorphism. Since `G` is discrete, there
exists an index `γ ≥ β` such that the image under `h` of `((𝔟_γ ∩ 𝔍) + 𝔍²)/𝔍²` is zero, as is the image under `h` of
`(𝔟_γ + 𝔍²)/𝔍²`, so that `h` factors as

```text
                                              𝔍/𝔍² → 𝔍_γ/𝔍_γ² → G
```

where `h'` is a `C_γ`-homomorphism. By extension, one therefore deduces from `h'` a homomorphism of `C_γ`-algebras

```text
                                              w : S_{C_γ}(𝔍_γ/𝔍_γ²) → G
```

and by construction, every element of degree `m` has under `w` an image which is an element of `𝔑`, so every element of
degree `n = 2m` has image zero, since `𝔑² = 0`; in other words, `w` factors as

```text
                                              S_{C_γ}(𝔍_γ/𝔍_γ²) → F_{γ,n} → G.
                                                                   w_{αγ}
```

Apply now to `𝑣_{αγ} : F_{γ,n} → F_{β,n} → E_{α,n}` the lemma `(19.5.6.7)`, whose hypotheses are verified; there exists
thus a `δ ≥ γ` and a homomorphism `u_{αδ} : E_{δ,n} → F_{γ,n}` such that the composite `𝑣_{αγ} ∘ u_{αδ}` is the
transition homomorphism `p_{αδ} : E_{δ,n} → E_{α,n}`. One finally obtains a commutative diagram of continuous
`A`-homomorphisms

```text
                                       B ──→ E_{δ,n} ──→ F_{γ,n} ──→ G ──→ G/𝔑
                                                 u_{αδ}      w_{αγ}
```

and the composite `f : B → G` of the homomorphisms of the lower line is such that `f` factors as `B → G → G/𝔑`, which
proves that `B` is a formally smooth `A`-algebra.

The proof of theorem `(19.5.3)` is thus complete.

**Corollary (19.5.7).**

<!-- label: 0_IV.19.5.7 -->

*Let `A` be a topological ring, `B` a topological `A`-algebra, `(𝔟_λ)` a fundamental system of open ideals in `B`, `𝔍`
an ideal of `B`, `C = B/𝔍` the quotient topological `A`-algebra. Set `C_λ = B/(𝔟_λ + 𝔍)`. Assume that: 1° for every `n`,
the topology induced on `𝔍^n` by that of `B` is also the topology of the `C`-module `𝔍^n` deduced from the topology of
`C` `(19.0.2)` (this condition will be satisfied in particular if `B` is Noetherian and its topology preadic
`(0_I, 7.3.2)`); 2° `C` is a formally smooth `A`-algebra. Under these conditions:*

*(i) If `B` is a formally smooth `A`-algebra, then, for every `λ`, `(𝔍/𝔍²) ⊗_C C_λ` is a projective `C_λ`-module.*

*(ii) If `B` is a formally smooth `A`-algebra and a preadmissible ring, then for every `λ`, the canonical homomorphism*

```text
(19.5.7.1)                    φ_λ = φ ⊗ 1_{C_λ} : S_C(𝔍/𝔍²) ⊗_C C_λ → gr^•_𝔍(B) ⊗_C C_λ
```

*is bijective.*

<!-- original page 195 -->

*(iii) Conversely, suppose that `B` is preadmissible, that the sequence `(𝔍^n)` tends to `0`, and that, for every `λ`,
`(𝔍/𝔍²) ⊗_C C_λ` is a projective `C_λ`-module and the homomorphism `(19.5.4.1)` is bijective. Then `B` is a formally
smooth `A`-algebra.*

Indeed, the topology of `𝔍/𝔍²` and that of the `S_C(𝔍/𝔍²)` are then also deduced from that of `B` `(19.5.1)`; the
conclusions then follow immediately from `(19.5.3)` and from the criteria of `(19.1.4)` and `(19.2.4)` specific to this
type of topologies.

**Remark (19.5.8).**

<!-- label: 0_IV.19.5.8 -->

*Suppose that `𝔍/𝔍²` is a `C`-module of finite type and that, for the quotient topology from that of `B`, `C` is a
Zariski ring; let `𝔯` be an ideal of definition of `C`, so that the `𝔯^n` form a fundamental system of neighbourhoods of
`0` in `C`. Then the conclusions of (i) and (ii) in `(19.5.7)` can be replaced by the following:*

*(i') `𝔍/𝔍²` is a projective `C`-module.*

*(ii') The canonical homomorphism `φ : S_C(𝔍/𝔍²) → gr^•_𝔍(B)` is bijective.*

Indeed, it is clear that (i') implies the conclusion of (i) in `(19.5.7)`. Conversely, if `(𝔍/𝔍²) ⊗_C C_λ` is a
projective `C_λ`-module for every `λ`, then `(𝔍/𝔍²) ⊗_C (C/𝔯^n)` is a `(C/𝔯^n)`-module that is projective (hence flat)
for every `n`; one concludes that `𝔍/𝔍²` is a flat `C`-module `(0_III, 10.2.2)`, hence projective since it is of finite
presentation `(Bourbaki, Alg. comm., chap. II, §5, n° 2, cor. 2 of th. 1)`. On the other hand, the `C`-modules
`S_C(𝔍/𝔍²)` and `gr^•_𝔍(B)` are of finite type, and one knows that when `C` is a Zariski ring, it amounts to the same
thing to say that `φ_n` is bijective or that `φ_λ` is bijective `(Bourbaki, Alg. comm., chap. III, §3, n° 5, prop. 9)`,
hence (ii) is equivalent to (ii').

### 19.6. Case of algebras over a field

**Theorem (19.6.1) (Cohen).**

<!-- label: 0_IV.19.6.1 -->

*Let `k` be a field, `K` an extension of `k`, `k` and `K` being endowed with the discrete topologies. For `K` to be a
formally smooth `k`-algebra, it is necessary and sufficient that `K` be a separable extension of `k`.*

The necessity of the condition will be established in `(19.6.5.1)` (and naturally will not be used until then); we shall
confine ourselves here to proving that the condition is sufficient. Let us distinguish two cases:

I. — *`K` is a separable extension of finite type of `k`.* One then knows `(Bourbaki, Alg., chap. V, §9, n° 3, th. 2)`
that there exists a pure subextension `K' = k(T_1, …, T_n)` of `K` such that `K` is a finite separable algebraic
extension of `K'`. Taking `(19.3.5, (ii))` into account, one may therefore restrict to the case where `K = K'` or to the
case where `K` is finite algebraic over `k`. In the first case, one knows that `A = k[T_1, …, T_n]` is a formally smooth
`k`-algebra `(19.3.3)`, and so is `k(T_1, …, T_n) = S⁻¹A`, where `S = A − {0}` `(19.3.5, (iv))`. In the second case, all
the Hochschild cohomology groups `H^i(K, L)` for an arbitrary `(K, K)`-bimodule `L` are zero: indeed, if one considers
the `k`-algebra tensor product `C = K ⊗_k K`, `L` is a left `C`-module and the cohomology group `H^i(K, L)` is equal to
`Ext^i_C(K, L)`, where `K` is also considered as a `(K, K)`-bimodule,

<!-- original page 196 -->

hence as a left `C`-module `(M, IX, 4)`. Now, since `K` is a finite separable extension of `k`, one knows that `K ⊗_k K`
is a direct composite of extensions of `k`, one of which is `K` itself `(Bourbaki, Alg., chap. VIII, §8, prop. 3)`; this
therefore entails that `K` is a projective `C`-module, whence our assertion. Every `k`-extension of `K` with kernel `L`
is therefore `k`-trivial, and *a fortiori* the commutative `k`-extensions are, whence the theorem in this case
`(19.4.4)`.

II. — *General case.* — With the notation of `(18.4.5)`, the question is to prove that `Hom_K(H^2(P_•^K), L) = 0` for
every `K`-vector space `L`, which evidently means that `H^2(P_•^K) = 0`. If `K` is the union of a filtered family of
subextensions `K_α` of `k`, `P_•^K` is the inductive limit of the corresponding complexes `P_•^{K_α}`, since the functor
`lim` commutes with the tensor product in the category of `k`-modules; by the exactness of the functor `lim` in this
category, one therefore has `H^2(P_•^K) = lim H^2(P_•^{K_α})`. Since the hypothesis that `K` is separable entails that
the same is true of every subextension of `K`, and since `K` is the union of subextensions of finite type, the first
part of the proof entails indeed that `K` is a formally smooth `k`-algebra. Q.E.D.

**Corollary (19.6.2).**

<!-- label: 0_IV.19.6.2 -->

*Let `A` be a separated and complete local ring, `K` its residue field, `k` a subfield of `K` such that `K` is a
separable extension of `k`. Then there exists a subfield `K'` of `A` containing `k`, such that the restriction to `K'`
of the canonical homomorphism `A → K` is an isomorphism of `K'` onto `K`.*

Let `𝔪` be the maximal ideal of `A`. By virtue of the hypothesis and of `(19.6.1)`, `K` is a formally smooth
`k`-algebra; applying `(19.3.10)` with `C` replaced by `k` and `𝔍` by `𝔪`, one sees that the identity automorphism of
`K = A/𝔪` factors as `K → A → A/𝔪`, where `f` is a `k`-homomorphism, hence necessarily a `k`-isomorphism of `K` onto a
subfield `K'` containing `k`.

**Corollary (19.6.3).**

<!-- label: 0_IV.19.6.3 -->

*Let `A` be a complete Noetherian local ring, `𝔪` its maximal ideal, `k` its residue field. The following conditions are
equivalent:*

*a) `A` contains a subfield.*

*b) If `p` is the characteristic of `k`, one has `pA = 0`.*

*c) There exists a field `K` such that `A` is isomorphic to a quotient ring of a formal power series ring
`B = K[[T_1, …, T_n]]`.*

*When this is the case, one may assume that `A` is isomorphic to `B/𝔟`, where `𝔟` is contained in the square of the
maximal ideal of `B`.*

It is immediate that c) implies a), for `A ≠ 0` since it is a local ring; since `K` is a field and the composite
homomorphism `K → B → A` (where `φ` is the canonical injection) is not zero, it is injective. To see that a) implies b),
it suffices to remark that if `k'` is a subfield of `A`, `k'` is isomorphic to a subfield of `k` and has therefore the
same characteristic `p`; since `p · 1 = 0` in `k'`, hence in `A`, one has `pA = 0`. Conversely, b) implies a), for the
composite of the canonical homomorphisms `ℤ → A → A` has kernel `pℤ`, and one has `f(pℤ) = 0`, hence `Ker(f) = pℤ` and
`A` contains a ring `A'` isomorphic to `ℤ/pℤ` and not meeting `𝔪`; if `p > 0`, `A'` is a field; otherwise, every

<!-- original page 197 -->

element of `A'` being invertible in `A`, the field of fractions of `A'` (isomorphic to `ℚ`) is also contained in `A`.

Let us prove finally that a) implies c): condition a) entails that `A` contains a prime subfield `k_0`, isomorphic to
the prime subfield of `k`, and of which `k` is therefore a separable extension. Applying `(19.6.2)`, one sees first that
there exists an isomorphism `f` of `k` onto a subfield `K` of `A`. On the other hand, let `(x_i)_{1 ≤ i ≤ n}` be a
system of elements of `𝔪` such that the classes mod `𝔪²` of the `x_i` form a basis (over `k`) of `𝔪/𝔪²`. Since `A` is
complete, there is then a continuous ring homomorphism `u : k[[T_1, …, T_n]] → A` such that `u` is equal to `f` on `k`
and `u(T_i) = x_i` for every `i`, and this homomorphism is surjective by virtue of the choice of the `x_i`
`(Bourbaki, Alg. comm., chap. III, §2, n° 9, prop. 11)`.

**Theorem (19.6.4).**

<!-- label: 0_IV.19.6.4 -->

*Let `k` be a field, `A` a Noetherian local `k`-algebra, `𝔪` its maximal ideal, `K = A/𝔪` its residue field, `A` being
endowed with the `𝔪`-preadic topology. Assume that `K` is a separable extension of `k`. Then the following conditions
are equivalent:*

*a) `A` is a formally smooth `k`-algebra.*

*b) The completion `Â` of `A` is `k`-isomorphic to a formal power series ring `K[[T_1, …, T_n]]` (whose `k`-algebra
structure is defined by the composite homomorphism*

```text
                                    k → K → K[[T_1, …, T_n]],
```

*where `ψ` is the canonical injection and `φ` the homomorphism defining the extension structure of `K`).*

*b') `Â` is a ring isomorphic to a formal power series ring `K[[T_1, …, T_n]]`.*

*c) `A` is a regular local ring.*

The fact that a) implies b) is the special case of (`(19.5.4)`, equivalence of a) and c)), applied by replacing `A`
there by `k`, `B` by `A` and `𝔍` by `𝔪`, taking into account `(19.6.1)`. It is clear that b) implies b') and b') implies
c) by `(17.1.1)`. Finally, if c) is verified, it follows from `(17.1.1, e)` and from (`(19.5.4)`, equivalence of b) and
a)), applied with `K = A/𝔪` replacing `C`, that `A` is a formally smooth `k`-algebra.

**Corollary (19.6.5).**

<!-- label: 0_IV.19.6.5 -->

*Let `k` be a field, `A` a Noetherian local `k`-algebra, `𝔪` its maximal ideal, `A` being endowed with the `𝔪`-preadic
topology. Suppose that `A` is a formally smooth `k`-algebra; then `A` is geometrically regular over `k`, in other words
(cf. `(IV, 6.7.6)`), for every finite extension `k'` of `k`, the semi-local ring `A' = A ⊗_k k'` is regular `(17.3.6)`.
Furthermore, if `K` is the residue field of `A`, `Â` is isomorphic to a formal power series ring `K[[T_1, …, T_n]]`.*

Since `Â' = Â ⊗_k k'`, it follows from `(19.3.6)` and from `(17.1.5)` (applied to the local rings at the maximal ideals
of `A'`) that one may restrict to the case where `A` is complete; then `A'` is a formally smooth `k'`-algebra
`(19.3.5, (iii))` and is moreover a direct composite of local `k'`-algebras, which are also formally smooth
`(19.3.5, (v))`. One is therefore reduced to proving that `A` is regular. Let `k_0` be the prime subfield of `k`; since
`k` is a separable extension of `k_0`, it is a formally smooth `k_0`-algebra `(19.6.1)` and by virtue of the hypothesis,
the same is true of `A` `(19.3.5, (ii))`. Since the residue field `K` of `A` is a separable extension of `k_0`, one may
then apply `(19.6.4)` to `A` and `k_0`, whence the conclusion.

<!-- original page 198 -->

**Corollary (19.6.5.1).**

<!-- label: 0_IV.19.6.5.1 -->

*Let `A` be a Noetherian local ring, `k` a subfield of `A` such that `A` is a formally smooth `k`-algebra (for its
preadic topology). Then every field `K` such that `k ⊂ K ⊂ A` is a separable extension of `k`.*

Indeed, for every finite extension `k'` of `k`, the ring `K ⊗_k k'` is identified with a subring of `A' = A ⊗_k k'`;
since `A'` is a regular ring, it is reduced, hence so is `K ⊗_k k'`, which proves that `K` is a separable extension of
`k` `(Bourbaki, Alg., chap. VIII, §7, n° 3, th. 1)`.

Note that this proves that the condition of the statement of `(19.6.1)` is necessary.

**Remark (19.6.5.2).**

<!-- label: 0_IV.19.6.5.2 -->

*If `K` is a non-separable extension of `k`, the formal power series ring `K[[T_1, …, T_n]]` is therefore not a formally
smooth `k`-algebra (for the usual `k`-algebra structure recalled in `(19.6.4)`). On the other hand, there are formally
smooth `k`-algebras `A` which are complete Noetherian local rings whose residue field `K` is a non-separable extension
of `k` (for example, the completions of the localizations of `B = k[T_1, …, T_n]` at maximal ideals `𝔫` such that `B/𝔫`
is a finite non-separable algebraic extension of `k`); such a ring cannot therefore be `k`-isomorphic to
`K[[T_1, …, T_n]]`, although it is isomorphic to it by virtue of `(19.6.5)`.*

In certain cases one can sharpen corollary `(19.6.5)`:

**Proposition (19.6.6).**

<!-- label: 0_IV.19.6.6 -->

*Let `k` be a field, `A` a Noetherian local `k`-algebra, `𝔪` its maximal ideal, `A` being endowed with the `𝔪`-preadic
topology. Suppose that the residue field `K = A/𝔪` of `A` is such that there exists a finite radicial extension `k_0` of
`k` for which the residue field of the local ring `K ⊗_k k_0` is a separable extension of `k_0` (we shall later express
this property by saying that `K` is of finite radicial multiplicity over `k` `(IV, 4.7.4)` and we shall see that this
condition is always satisfied when `K` is a finitely generated extension of `k`). Then the following conditions are
equivalent:*

*a) `A` is a formally smooth `k`-algebra.*

*b) There exists a finite radicial extension `k'` of `k` such that `Â ⊗_k k'` is `k'`-isomorphic to a formal power
series algebra `K'[[T_1, …, T_n]]`, where `K'` is a separable extension of `k'`.*

*b') There exists a finite extension `k'` of `k` such that the semi-local ring `Â ⊗_k k'` has at least one local ring
component which is `k'`-isomorphic to a formal power series algebra `K'[[T_1, …, T_n]]`, where `K'` is a separable
extension of `k'`.*

*c) `A` is geometrically regular over `k` `(19.6.5)`.*

Let us first note that if `k'` is a radicial extension of `k`, there is only one ideal of `A' = A ⊗_k k'` above `𝔪`,
formed of the elements of which some `p^h`-th power (`p` the characteristic exponent of `k`) is in `𝔪` for some suitable
`h` `(Bourbaki, Alg. comm., chap. V, §2, n° 3, lemma 4)`; `A'` is thus a local ring, and so is
`K ⊗_k k' = (A ⊗_k k')/(𝔪 ⊗_k k')`; moreover the residue fields of these two rings are identical. Recall on the other
hand that if `K` is a separable extension of `k`, then, for every finite extension `k''` of `k`, `K ⊗_k k''` is a direct
composite of fields `(Bourbaki, Alg., chap. VIII, §7, n° 3, cor. 1 of th. 1)`, and consequently `𝔪 ⊗_k k''` is the
radical of `A ⊗_k k''`, and the field components of `K ⊗_k k''` are the residue fields at the maximal ideals of
`A ⊗_k k''`; in

<!-- original page 199 -->

addition, these fields are separable extensions of `k''` since for every extension `k_1` of `k''`,
`K_1 = K ⊗_k k_1 = (K ⊗_k k'') ⊗_{k''} k_1` is without radical `(loc. cit., th. 1)`. If one applies these remarks to the
field `K` of finite radicial multiplicity over `k`, one sees that for every finite extension `k''` of `k_0`,
`(K ⊗_k k')_{red}` is separable over `k''`.

Let us pass to the proof of `(19.6.6)`. It is trivial that b) implies b'). Let us show that b') implies a). If one sets
`B' = K'[[T_1, …, T_n]]`, the hypothesis that `K'` is separable over `k'` entails, by the initial remarks, that for
every finite extension `k''` of `k'`, the components of the complete semi-local ring `B' ⊗_{k'} k''` (equal to the
formal power series ring `(K' ⊗_{k'} k'')[[T_1, …, T_n]]`) are the rings `K_i''[[T_1, …, T_n]]`, where the `K_i''` are
the field components of `K' ⊗_{k'} k''`. Since the local components of `B' ⊗_{k'} k''` are also local components of
`Â ⊗_k k'' = (Â ⊗_k k') ⊗_{k'} k''`, one sees that the hypothesis b') is still verified when `k'` is replaced by any of
its finite extensions. In particular, one may suppose that `k'` is quasi-Galois, hence a Galois extension of a radicial
extension `k_0'` of `k`; `A_0' = Â ⊗_k k'` can then be written `A_0' ⊗_{k_0'} k'`, where `A_0' = Â ⊗_k k_0'` is a
complete local ring. One then knows `(Bourbaki, Alg., chap. VIII, §8, prop. 4)` that `A'` is a direct composite of local
rings isomorphic to `A_0'` as `k_0'`-algebras. Now, one of these rings is by hypothesis `k'`-isomorphic to a formal
power series ring `K'[[T_1, …, T_n]]`, where `K'` is a separable extension of `k'`, hence also a separable extension of
`k_0'`; taking `(19.6.4)` into account, `A_0'` is thus a formally smooth `k_0'`-algebra. But since `k_0'` is a
faithfully flat, projective and finitely generated `k`-module, one concludes from `(19.4.7)` that `Â` is a formally
smooth `k`-algebra.

One has already seen `(19.6.5)` that a) implies c); it remains therefore to verify that c) implies b). Now, if c) is
verified, then, for every finite radicial extension `k'` of `k` containing `k_0`, `A ⊗_k k'` is a regular local ring,
whose residue field `K'` is a separable extension of `k'`; it follows therefore from `(19.6.4)` that its completion
`Â ⊗_k k'` is `k'`-isomorphic to a formal power series ring `K'[[T_1, …, T_n]]`.

**Remarks (19.6.7).**

<!-- label: 0_IV.19.6.7 -->

*(i) Note that the hypothesis that `K` is of finite radicial multiplicity over `k` has only been used in the proof of
the implication b') ⇒ a).*

*(ii) We shall later prove `(22.5.8)` that a) and c) are equivalent, without any hypothesis on the extension `K` of
`k`.*

### 19.7. Case of local homomorphisms; existence and uniqueness theorems

In this number, when a semi-local ring is considered as a topological ring, it is always implicit that this is its
`𝔯`-preadic topology, where `𝔯` is its radical. Every local homomorphism of local rings is therefore automatically
continuous.

**Theorem (19.7.1).**

<!-- label: 0_IV.19.7.1 -->

*Let `A`, `B` be two Noetherian local rings, `𝔪`, `𝔫` their respective maximal ideals, `k = A/𝔪` the residue field of
`A`; suppose `A` and `B` are endowed respectively with the `𝔪`-preadic and `𝔫`-preadic topologies. Let `φ : A → B` be a
local homomorphism, and set `B_0 = B ⊗_A k`. The following properties are equivalent:*

*a) `B` is a formally smooth `A`-algebra.*

<!-- original page 200 -->

*b) `B` is a flat `A`-module and `B_0 = B/𝔪B` (endowed with the quotient topology) is a formally smooth `k`-algebra.*

The proof is in several steps.

**(19.7.1.1)** Let us first prove that b) implies a). We shall apply the criterion `(19.4.7)` with `𝔍 = 𝔪`; by virtue of
the second hypothesis in b), everything boils down to showing that `B` is a formally projective `A`-module. The
hypothesis entails that for every `h > 0`, `B/𝔪^h B` is a flat `(A/𝔪^h)`-module `(0_III, 10.2.1)`; since the `𝔪^h` form
a fundamental system of neighbourhoods of `0` in `A`, and `(B/𝔪^h B)/𝔪(B/𝔪^h B) = B_0`, one may replace `A` and `B` by
`A/𝔪^h` and `B/𝔪^h B` respectively, and consequently suppose `A` Artinian (hence discrete). Since `B_0` is a formally
smooth `k`-algebra, it is a regular ring `(19.6.5)`; let `(x_i^0)_{1 ≤ i ≤ n}` be a regular system of parameters for
`B_0` `(17.1.6)`, and for every `i`, let `x_i ∈ B` be such that `x_i^0` is its image in `B_0 = B/𝔪B`; since the `x_i^0`
generate the maximal ideal `𝔫_0 = 𝔫/𝔪B` of `B_0`, the ideals `𝔍_m^0 = ∑ (x_i^0)^m B_0` (for `m > 0`) form a fundamental
system of neighbourhoods of `0` in `B_0`, since `𝔍_m^0` is evidently contained in `𝔫_0^m`, and on the other hand
contains `𝔫_0^{m+n−1}`. Set `𝔍_m = ∑ x_i^m B` for every `m > 0`; it is clear that `𝔫 = 𝔍_1 + 𝔪B`; since there exists
`h > 0` such that `𝔪^h = 0`, one has `𝔫^m ⊂ 𝔍_{m−h} ⊂ 𝔫^{m−h}` for `m > h`, and since one has seen that `𝔍_m ⊃ 𝔍_m`, one
sees that the `𝔍_m` form a fundamental system of neighbourhoods of `0` in `B`. Everything therefore boils down to
proving that the `B/𝔍_m` are free `A`-modules, and it amounts to the same to see that they are flat `A`-modules
`(0_III, 10.1.3)`. Now, the hypothesis that `(x_i^0)` is a `B_0`-regular sequence of elements of the maximal ideal of
`B_0` entails the same property for the sequence of the `(x_i^m)` (`1 ≤ i ≤ n`) for every `m > 0` `(15.1.20)`; the
conclusion then follows from `(15.1.16, b) and c))`.

**Lemma (19.7.1.2).**

<!-- label: 0_IV.19.7.1.2 -->

*Let `A` be a topological ring, `B`, `C` two topological `A`-algebras which are Noetherian local rings. Suppose moreover
that `C` is complete and that the residue field `B/𝔪` of `B` is an `A`-module of finite type. Let `E` be the completed
tensor product `B ⊗̂_A C`. Then:*

*(i) `E` is a complete Noetherian semi-local ring.*

*(ii) The ideal `𝔪E` is contained in the radical of `E`, and for every `h > 0`, `E/𝔪^h E` is isomorphic to
`(B/𝔪^h) ⊗_A C`.*

*(iii) If `C` is a flat `A`-module, `E` is a flat `B`-module.*

By definition, `E` is the separated completion of the tensor product `B ⊗_A C` for the topology defined by the ideals
`Im(𝔪 ⊗_A C) + Im(B ⊗_A 𝔫)` `(0_I, 7.7.5)`. If one sets `𝔯 = Im(𝔪 ⊗_A C) + Im(B ⊗_A 𝔫)`, one has
`𝔯² ⊂ Im(𝔪² ⊗_A C) + Im(B ⊗_A 𝔫²)`, hence `E` is also the separated completion of `B ⊗_A C` for the `𝔯`-preadic
topology. By hypothesis, `(B ⊗_A C)/𝔯 = (B/𝔪) ⊗_A (C/𝔫)` is a `(C/𝔫)`-module of finite type, hence an Artinian ring; in
addition, `𝔯/𝔯²`, being a quotient of `((𝔪/𝔪²) ⊗_A C) ⊕ (B ⊗_A (𝔫/𝔫²))`, is a `(B ⊗_A C)`-module of finite type;
applying `(0_I, 7.2.11)`, one sees that `E` is a Noetherian ring; furthermore, `E/𝔯E`, isomorphic to `(B ⊗_A C)/𝔯`,
being Artinian, `E` is semi-local. Note now that `E`, which is isomorphic to `lim((B/𝔪^i) ⊗_A (C/𝔫^j))`, is also
isomorphic, by the double-projective-limit theorem, to `lim(lim((B/𝔪^i) ⊗_A (C/𝔫^j))) = lim((B/𝔪^i) ⊗_A C)`; now
`lim((B/𝔪^i) ⊗_A (C/𝔫^j))`

<!-- original page 201 -->

is the separated completion of `(B/𝔪^i) ⊗_A C`, and since `C` is complete, this is none other than `(B/𝔪^i) ⊗_A C`
itself, `B/𝔪^i` being an `A`-module of finite type since `𝔪/𝔪^i` is a `(B/𝔪)`-module of finite type `(0_I, 7.3.6)`. One
thus has `E = lim((B/𝔪^i) ⊗_A C)`. For every integer `h > 0`, `𝔪^h E`, being an ideal of `E`, is closed in `E`
`(0_I, 7.3.5)`, hence complete, and on the other hand it is evidently dense in `lim(Im((𝔪^h/𝔪^i) ⊗_A C))`, hence equal
to this latter projective limit. Furthermore, all the projective systems considered are defined by surjective
homomorphisms, hence it follows from `(0_III, 13.2.2)` that `E/𝔪^h E` is isomorphic to
`(B/𝔪^h) ⊗_A C = (B ⊗_A C)/Im(𝔪^h ⊗_A C)`. In particular, since `Im(𝔪^h ⊗_A C) ⊂ 𝔯`, this shows that `𝔪E` is contained
in `𝔯E`, hence in the radical of `E`. Finally, the hypothesis that `C` is a flat `A`-module entails that
`(B/𝔪^h) ⊗_A C = E/𝔪^h E` is a flat `(B/𝔪^h)`-module for every `h > 0`; since `B` and `E` are Noetherian and `𝔪E` is
contained in the radical of `E`, it follows from `(0_III, 10.2.2)` that `E` is a flat `B`-module.

**Lemma (19.7.1.3).**

<!-- label: 0_IV.19.7.1.3 -->

*Let `A` be a Noetherian local ring, `𝔪` its maximal ideal, `k` its residue field, `B_0` a `k`-algebra; suppose that
`B_0` is a complete regular Noetherian local ring. Then there exists a topological `A`-algebra `B` which is a complete
Noetherian local ring, a flat `A`-module, and such that `B_0` is `k`-isomorphic to `B ⊗_A k = B/𝔪B`.*

Since `Â` is flat over `A` and has the same residue field, one may restrict to the case where `A` is complete.

Let `K` be the residue field of `B_0`, and let us distinguish two cases:

I) *`K` is a separable extension of `k`.* By virtue of `(19.6.4)`, `B_0` is `k`-isomorphic to a formal power series ring
`K[[T_1, …, T_n]]`. When `B_0 = K`, the lemma has already been proved `(0_III, 10.3.1)`; let `C` be a complete
Noetherian local ring which is a flat `A`-module and such that `C ⊗_A k` is isomorphic to `K`. For `n ≥ 1`, it suffices
to take (with the preceding notation) `B = C[[T_1, …, T_n]]`; one indeed knows
`(Bourbaki, Alg. comm., chap. III, §3, n° 4, cor. 3 of th. 1)` that `B` is a flat `C`-module, hence also a flat
`A`-module, and on the other hand, it is immediate that `C[[T_1, …, T_n]] ⊗_A k` is isomorphic to
`(C/𝔪C)[[T_1, …, T_n]] = B_0`.

II) *`K` is of characteristic `p > 0`, and consequently the same is true of `k`.* Denote by `P` the prime field `𝔽_p`,
and by `W(P)` the complete local ring of `p`-adic numbers `ℤ_p`, which is a (hence regular) discrete valuation ring, and
has `P` as residue field. Let us first show that there exists a continuous ring homomorphism `W(P) → A`, thus making `A`
into a topological `W(P)`-algebra. Indeed, if `j : ℤ → A` is the canonical homomorphism, one has `j(pℤ) ⊂ 𝔪` by
hypothesis, whence `j⁻¹(𝔪) = pℤ`, and consequently `j` factors as `ℤ → ℤ_{pℤ} → A`, where the latter is a local, hence
continuous, homomorphism, which (since `A` is complete) extends by continuity to the desired homomorphism `W(P) → A`.

Since `k` is a separable extension of `P`, case I) shows that there is a local homomorphism `W(P) → W(k)`, where `W(k)`
is a complete Noetherian local ring and a flat `W(P)`-module, such that `W(k) ⊗_{W(P)} P` is isomorphic to `k`.
Furthermore, since the uniformizer `p` of `W(P)` is a `W(k)`-regular element by flatness `(0_I, 6.3.4)`, and since

<!-- original page 202 -->

`W(k)/pW(k) = k`, `pW(k)` is the maximal ideal of `W(k)`, which entails that this last ring is a complete discrete
valuation ring `(Bourbaki, Alg. comm., chap. VI, §3, n° 5, prop. 9)`. By `(19.7.1.1)` one sees in addition (since `k` is
separable over `P`, hence a formally smooth `P`-algebra `(19.6.1)`) that `W(k)` is a formally smooth `W(P)`-algebra. The
continuous `W(P)`-homomorphism `W(k) → k` thus factors as `W(k) → A → k` `(19.3.11)`, which allows one to consider `A`
as a topological `W(k)`-algebra. Applying now case I) to `B_0` considered as a `P`-algebra and to `W(P)`, one sees that
there exists a `W(P)`-algebra `B_P` which is a complete Noetherian local ring, a flat `W(P)`-module, and such that
`B_P ⊗_{W(P)} P` is `P`-isomorphic to `B_0`. Using again the fact that `W(k)` is a formally smooth `W(P)`-algebra, one
sees by `(19.3.11)` that the composite homomorphism `W(k) → P → B_0` factors as `W(k) → B_P → B_0`; furthermore, since
`k = W(k)/pW(k)`, one has `B_P ⊗_{W(k)} k = B_P/pB_P = B_P ⊗_{W(P)} P = B_0`. Let us show that `B_P` is a flat
`W(k)`-module; since `W(k)` is a discrete valuation ring of which `p` is the uniformizer, it suffices to verify that
`B_P` is a torsion-free `W(k)`-module `(0_I, 6.3.4)`, or that `p` is a `B_P`-regular element, which follows from the
fact that `B_P` is a flat `W(P)`-module `(0_I, 6.3.4)`.

Set now

```text
                                          B = B_P ⊗̂_{W(k)} A
```

and note that the residue field of `A`, being equal to that of `W(k)`, is *a fortiori* a `W(k)`-module of finite type.
It follows therefore first from `(19.7.1.2)` that `B` is a complete Noetherian semi-local ring, `𝔪B` being contained in
the radical of `B`; furthermore `B/𝔪B` is `k`-isomorphic to `B_P ⊗_{W(k)} k = B_0`, hence `B` is in fact a local ring.
Since `B_P` is a flat `W(k)`-module, `(19.7.1.2)` finally shows that `B` is a flat `A`-module. Q.E.D.

**Lemma (19.7.1.4).**

<!-- label: 0_IV.19.7.1.4 -->

*Let `A` be a ring, `𝔍` an ideal of `A`, `M`, `N` two `A`-modules separated for the `𝔍`-preadic topology. Suppose in
addition that `N` is complete for the `𝔍`-preadic topology and that `M` is a flat `A`-module. Let `u : N → M` be an
`A`-homomorphism; if `u ⊗ 1 : N ⊗_A (A/𝔍) → M ⊗_A (A/𝔍)` is bijective, then `u` is bijective.*

The associated graded modules being taken relative to the `𝔍`-preadic filtrations, it follows from the hypotheses on `M`
and `N` relative to the `𝔍`-preadic topologies that it suffices to prove that `gr(u) : gr_•(N) → gr_•(M)` is bijective
`(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 3 of th. 1)`. Now, one has a commutative diagram

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

where `A_0 = A/𝔍 = gr_0(A)`, and `ψ_N` and `ψ_M` are the canonical maps `(0_III, 10.1.1.2)`. By hypothesis, `gr_0(u)` is
bijective, as is `ψ_M` `(0_III, 10.2.1)`, and `ψ_N` is surjective; one deduces first that `gr_0(u) ⊗ 1` is bijective,
then that `ψ_N` is injective, hence bijective, and finally that `gr(u)` is bijective.

**Lemma (19.7.1.5).**

<!-- label: 0_IV.19.7.1.5 -->

*Let `A` be a Noetherian ring, `𝔍` an ideal of `A`, `B`, `B'` two `A`-algebras which are Noetherian local rings, the
homomorphisms `A → B`, `A → B'` being continuous for the `𝔍`-preadic topology on `A`. Suppose that: 1° `B` and `B'` are
complete for the `𝔍`-preadic topologies; 2° `B` is a formally smooth `A`-algebra; 3° `B'` is a flat `A`-module. Set
`A_0 = A/𝔍`, and let `u_0 : B ⊗_A A_0 → B' ⊗_A A_0` be an `A_0`-isomorphism; then there exists an `A`-isomorphism
`u : B → B'` such that `u_0 = u ⊗ 1` (which entails that `B'` is a formally smooth `A`-algebra and `B` a flat
`A`-module).*

Set `B_0 = B ⊗_A A_0`, `B_0' = B' ⊗_A A_0`. Note that if `𝔪` and `𝔪'` are the maximal ideals of `B` and `B'`, the
`𝔍`-preadic topologies on `B` and `B'` are separated since `𝔍B ⊂ 𝔪` and `𝔍B' ⊂ 𝔪'`; furthermore, since `𝔍B'` is closed
in `B'` for the `𝔍`-preadic topology, the composite homomorphism `B → B_0 → B_0'`, which is continuous for the
`𝔍`-preadic topologies, factors as `B → B' → B_0'`, where `u` is a continuous `A`-homomorphism `(19.3.10)`. One clearly
has `u_0 = u ⊗ 1`, and the hypothesis that `u_0` is bijective entails the same for `u` by virtue of `(19.7.1.4)`.

**(19.7.1.6)** *End of the proof.* To complete the proof of `(19.7.1)`, one must show that a) implies b); one already
knows that a) entails that `B_0` is a formally smooth `k`-algebra `(19.3.5, (iii))`, so everything boils down to proving
that `B` is a flat `A`-module. It amounts to the same to establish that `B̂` is a flat `Â`-module
`(Bourbaki, Alg. comm., chap. III, §5, n° 4, prop. 4)`, and one knows that `B̂` is a formally smooth `Â`-algebra
`(19.3.6)`; one may therefore restrict to the case where `A` and `B` are complete. Since `B_0` is a formally smooth
`k`-algebra, it is a regular ring `(19.6.5)` and complete `(0_I, 6.3.5)`; applying `(19.7.1.3)`, one sees that there
exists an `A`-algebra `B'` which is a complete Noetherian local ring and a flat `A`-module, a local homomorphism
`A → B'` and an `A`-isomorphism `B_0 ⥲ B' ⊗_A k`. It then suffices to apply `(19.7.1.5)` taking for `𝔍` the maximal
ideal of `A`, to obtain that `B` is `A`-isomorphic to `B'`, hence is a flat `A`-module. Q.E.D.

**Theorem (19.7.2).**

<!-- label: 0_IV.19.7.2 -->

*Let `A` be a Noetherian local ring, `𝔍` an ideal contained in the maximal ideal of `A`, `A_0 = A/𝔍`, `B_0` a complete
Noetherian local ring, `A_0 → B_0` a local homomorphism making `B_0` into a formally smooth `A_0`-algebra. Then there
exists a complete Noetherian local ring `B`, a local homomorphism `A → B` making `B` into a flat `A`-module, and an
`A_0`-isomorphism `u : B ⊗_A A_0 ⥲ B_0`. If `(B', u')` is a pair satisfying the same conditions as `(B, u)`, there
exists an `A`-isomorphism `v : B ⥲ B'` making the diagram*

```text
                                     B ⊗_A A_0 ──→ B' ⊗_A A_0
                                              ↘     ↙
                                                B_0
```

*commute.*

<!-- original page 204 -->

Let `𝔪` be the maximal ideal of `A`, so that `𝔪_0 = 𝔪/𝔍` is the maximal ideal of `A_0`, `A` and `A_0` having the same
residue field `k`. Set `B_{00} = B_0 ⊗_{A_0} k`; since `B_{00}` is a formally smooth `k`-algebra `(19.3.5, (iii))`, it
is a regular local ring `(19.6.5)`; applying `(19.7.1.3)`, one sees that there exists a topological `A`-algebra `B`
which is a complete Noetherian local ring, a flat `A`-module, and for which one has an `A`-isomorphism
`u_{00} : B ⊗_A k ⥲ B_{00}`. Note that by virtue of `(19.7.1)`, `B` is a formally smooth `A`-algebra, so
`B ⊗_A A_0 = B/𝔍B` is a formally smooth `A_0`-algebra `(19.3.5, (iii))` and a complete Noetherian local ring;
furthermore, `B_0` is a flat `A_0`-module by virtue of the hypothesis and of `(19.7.1)`; since one has a `k`-isomorphism
`u_{00} : B ⊗_A k = (B ⊗_A A_0) ⊗_{A_0} k ⥲ B_0 ⊗_{A_0} k = B_{00}`, one deduces from `(19.7.1.5)`, applied with `A`
replaced by `A_0` and `𝔍` by `𝔪_0`, that there exists an `A_0`-isomorphism `u : B ⊗_A A_0 ⥲ B_0` such that
`u_{00} = u ⊗ 1`. As for the uniqueness assertion, note that the ideals `𝔍B` (resp. `𝔍B'`) are closed in `B` (resp.
`B'`) `(0_I, 7.3.5)`, hence `B` and `B'` are separated and complete for the `𝔍`-preadic topologies
`(Bourbaki, Top. gén., chap. III, 3rd ed., §3, n° 5, cor. 2 of prop. 9)`; by hypothesis, one has an `A_0`-isomorphism
`v_0 : B ⊗_A A_0 ⥲ B' ⊗_A A_0` such that `u' ∘ v_0 = u`; since `B` is a formally smooth `A`-algebra and `B'` a flat
`A`-module, one may apply `(19.7.1.5)`, whence the existence of the `A`-isomorphism `v` answering the question.

**Remarks (19.7.3).**

<!-- label: 0_IV.19.7.3 -->

*(i) Note that the uniqueness assertion in `(19.7.2)` is still valid if one assumes only that `B` and `B'` are complete
for the `𝔍`-preadic topologies. We do not know if one can improve the existence assertion in the same way, in other
words whether one can dispense with assuming the local ring `B_0` complete (for its `𝔫_0`-preadic topology, denoting by
`𝔫_0` its maximal ideal) by requiring only that `B` be complete for the `𝔍`-preadic topology. When `A_0` is complete for
the `𝔪`-preadic topology, one can see that this problem reduces to the following: if `B_0` is a (not necessarily
complete) regular Noetherian local ring containing the prime field `𝔽_p = ℤ/pℤ`, does there exist for every `n ≥ 1` a
flat `(ℤ/p^n ℤ)`-algebra `B` such that `B/pB` is isomorphic to `B_0`?*

*(ii) Note that in general, the isomorphism `v` whose existence is asserted in `(19.7.2)` is not unique (cf.
`(19.8.7)`).*

### 19.8. Cohen algebras and `p`-Cohen rings; application to the structure of complete local rings

The results of this section are immediate applications of the theorems of `(19.7)`, but deserve to be made explicit
because of their practical importance.

**Definition (19.8.1).**

<!-- label: 0_IV.19.8.1 -->

*Let `A`, `B` be two Noetherian local rings, `𝔪` the maximal ideal of `A`, `k = A/𝔪` its residue field, `φ : A → B` a
local homomorphism, making `B` into an `A`-algebra. We say that `B` is a **Cohen `A`-algebra** if it satisfies the
following conditions:*

*(i) `B` is a complete ring.*

*(ii) `B` is a flat `A`-module.*

*(iii) `B ⊗_A k` is a field (in other words, `𝔪B` is the maximal ideal of `B`) which is a separable extension of `k`.*

<!-- original page 205 -->

**Theorem (19.8.2).**

<!-- label: 0_IV.19.8.2 -->

*Let `A` be a Noetherian local ring, `k` its residue field.*

*(i) If `B` is a Cohen `A`-algebra, `B` is a formally smooth `A`-algebra. For every complete Noetherian local ring `C`,
every local homomorphism `A → C` and every ideal `𝔍 ≠ C` in `C`, every `A`-homomorphism `B → C/𝔍` therefore factors as
`B → C → C/𝔍`, where `v` is a (necessarily local) `A`-homomorphism.*

*(ii) For every field `K` which is a separable extension of `k`, there exists a Cohen `A`-algebra `B` such that
`B ⊗_A k` is `k`-isomorphic to `K`, and such an `A`-algebra is unique up to isomorphism.*

Since `K` is a formally smooth `k`-algebra `(19.6.1)`, assertion (i) follows from `(19.7.1)`. To prove (ii), one may
restrict to the case where `A` is complete, for it amounts to the same to say that `B` is a flat `A`-module or a flat
`Â`-module `(0_III, 10.2.3)`, one has `𝔪B = 𝔪Â B` and `k` is the residue field of `Â`. It then suffices to apply
`(19.7.2)` by taking `𝔍 = 𝔪` and `B_0 = K` (and using `(19.6.1)`).

**Definition (19.8.3).**

<!-- label: 0_IV.19.8.3 -->

*We call **prime local ring** a local ring of the form `ℤ_{pℤ}`, where `pℤ` is a prime ideal of `ℤ`. We call **complete
prime local ring** the completion of a prime local ring.*

The prime local rings are therefore of two kinds:

1° Those which correspond to the maximal ideals `pℤ` where `p ≠ 0` is a prime number; `ℤ_{pℤ}` is a discrete valuation
ring, whose completion is *the ring of `p`-adic integers*, usually denoted `ℤ_p` ⁽¹⁾.

2° For the prime ideal `pℤ = (0)`, `ℤ_{(0)}` is the field of rational numbers `ℚ`, identical to its completion (the
topology being naturally the topology of Noetherian local ring, hence here the discrete topology).

The terminology of `(19.8.3)`, analogous to that of "prime fields", is justified in the same way: for every local ring
`A`, consider the canonical homomorphism `φ : ℤ → A`, and let `pℤ` be the inverse image under this homomorphism of the
maximal ideal `𝔪` of `A`; `pℤ` is a prime ideal of `ℤ` and the preceding homomorphism therefore factors as
`ℤ → ℤ_{pℤ} → A`; moreover, since `φ` is the unique homomorphism of `ℤ` into `A`, `p` and `ψ` are uniquely determined.
In other words, for every local ring `A`, there is a unique homomorphism `ψ : P → A`, where `P` is a prime local ring;
if in addition `A` is separated and complete, one can extend by completion this homomorphism, and there is therefore a
unique homomorphism `ψ : P → A`, where `P` is a complete prime local ring. Moreover, by passing to quotients, `ψ` gives
a homomorphism of the residue field `𝔽_p` if `p > 0` (resp. `ℚ` if `p = 0`) into the residue field `k` of `A`, and `p`
is therefore the characteristic of `k`.

If one takes in particular for `A` a prime local ring (resp. complete prime local ring), one sees that there exists in
such a ring only *one* endomorphism, namely the identity.

______________________________________________________________________

⁽¹⁾ This notation, currently universally used, conflicts in this case with the notation `A_f` adopted in `(0_I, 1.2.3)`:
with `A = ℤ` and `f = p`, `A_p` indeed means the ring of rational numbers of the form `k/p^n` (`k ∈ ℤ`, `n` an integer
`≥ 0`); we shall always avoid using the notation `ℤ_p` to designate this latter ring.

<!-- original page 206 -->

**Definition (19.8.4).**

<!-- label: 0_IV.19.8.4 -->

*Let `A` be a local ring, `P → A` the unique homomorphism of a prime local ring `P` into `A`, `p` the characteristic of
the residue fields of `P` and `A`. We say that `A` is a **Cohen ring** if it is a Cohen `P`-algebra, that is to say
`(19.8.1)` if:*

*1° `A` is Noetherian and complete.*

*2° `A` is a flat `P`-module (which is also equivalent to saying that `A` is a flat `P̂`-module
`(Bourbaki, Alg. comm., chap. III, §5, n° 4, prop. 4)`).*

*3° `A/pA` is a field (necessarily separable over the residue field of `P`, this field being prime).*

If `p = 0`, these conditions are equivalent to saying that `A` is a field of characteristic `0`. If `p > 0`, one
necessarily has `pA ≠ 0`; condition 3° means that `pA` is the maximal ideal `𝔪` of `A`; condition 2° means that `p` is
`A`-regular, since `P` is a discrete valuation ring `(0_I, 6.3.4)`. Hence `A` is a regular ring `(17.1.1, d)` of
dimension `1`, and consequently a complete discrete valuation ring by virtue of 1°; in summary:

**Proposition (19.8.5).**

<!-- label: 0_IV.19.8.5 -->

*The Cohen rings are the fields of characteristic `0` and the complete discrete valuation rings whose residue field has
characteristic `p > 0` and whose maximal ideal is generated by `p · 1` (`1` being the unit of the ring).*

Note that in the second case, `p · 1 ≠ 0` since `p` is `A`-regular, so one can identify `p · 1` with the integer `p`,
the canonical homomorphism `ℤ → A` is injective, and one identifies `p · 1` with the element `p` of `ℤ_p`; one says in
this case that `A` is a **`p`-Cohen ring**.

**Theorem (19.8.6) (Cohen).**

<!-- label: 0_IV.19.8.6 -->

*(i) Let `W` be a Cohen ring, `C` a complete Noetherian local ring, `𝔍` an ideal of `C` distinct from `C`. Then every
local homomorphism `u : W → C/𝔍` factors as `W → C → C/𝔍`, where `v` is a local homomorphism.*

*(ii) Let `K` be a field. There exists a Cohen ring `W` whose residue field is isomorphic to `K`. If `W'` is a second
Cohen ring, `K'` its residue field, every isomorphism `u : K ⥲ K'` arises by passage to quotients from an isomorphism
`v : W ⥲ W'`.*

This is none other than `(19.8.2)` applied to the case where `A` is a prime local ring.

**Remarks (19.8.7).**

<!-- label: 0_IV.19.8.7 -->

*(i) When `K` is of characteristic `0`, part (ii) of `(19.8.6)` becomes trivial.*

*(ii) The homomorphism `v` of `(19.8.6, (i))` is not necessarily uniquely determined by `u`, as is already shown by the
case where `W` is a field of characteristic `0`, `𝔍 = 0` and `u` is an isomorphism (cf. `(21.5.5)`). Likewise, in
`(19.8.6, (ii))` the isomorphism `v` is not necessarily uniquely determined by `u` (cf. `(21.5.5)`).*

*However, when `K` is perfect and of characteristic `p > 0`, one will see `(21.5.5)` that in `(19.8.6, (ii))` the
isomorphism `v` is unique. One will also see later that in this case `W` is identified with the ring `W_∞(K)` of Witt
vectors of infinite length over `K`.*

*(iii) In `(19.8.6, (i))`, one may weaken the hypotheses on `C` by using `(19.3.10)` and `(19.3.12)`.*

**Theorem (19.8.8) (Cohen).**

<!-- label: 0_IV.19.8.8 -->

*Let `A` be a complete Noetherian local ring, `k` its residue field.*

<!-- original page 207 -->

*(i) There exists a Cohen ring `W` such that `A` is isomorphic to a quotient ring of a formal power series ring
`W[[T_1, …, T_n]]` (and in particular `A` is isomorphic to a quotient of a complete regular local ring `(17.3.8)`). If
`A` contains a field, it is isomorphic to a quotient ring of `k[[T_1, …, T_n]]`.*

*(ii) Suppose in addition that `A` is integral. Then there exists a subring `B` of `A` such that: 1° `B` is isomorphic
to a formal power series ring over a ring `C` which is a field or a Cohen ring (which entails that `B` is a complete
regular local ring `(17.3.8)`); 2° `B` has the same residue field as `A` and the injection `B → A` is a local
homomorphism; 3° `A` is a finite `B`-algebra.*

Let `𝔪` be the maximal ideal of `A`. There exists a Cohen ring `W` whose residue field is isomorphic to `k`
`(19.8.6, (ii))`; one therefore has a local homomorphism `W → A/𝔪`, which consequently factors as `W → A → A/𝔪`, where
`u` is a local homomorphism `(19.8.6, (i))`. For every finite family `(x_i)_{1 ≤ i ≤ n}` of elements of `𝔪`, there then
exists a local homomorphism `v : W[[T_1, …, T_n]] → A` extending `u` and such that `v(T_i) = x_i` for every `i`
`(Bourbaki, Alg. comm., chap. III, §4, n° 5, prop. 6)`. When `A` contains a field, it contains a prime field `P`, of
which `k` is a (necessarily separable) extension, and consequently `A` contains a field isomorphic to `k` `(19.6.2)`;
one may then replace `W` by `k` in the preceding definition of `v`.

(i) Let us first take for the `x_i` a system of generators of `𝔪`. Since `W` has the same residue field as `A`, and the
classes of the `x_i` in the graded ring `gr_•(A)` generate `gr_•(A)` as a `k`-algebra,
`gr(v) : gr_•(W[[T_1, …, T_n]]) → gr_•(A)` is surjective; one deduces that `v` itself is surjective
`(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 2 of th. 1)`. Recall that the case where `A` contains a field has
already been seen and only figures here for reference `(19.6.3)`.

(ii) If `A` contains a field, it contains a field `k'` isomorphic to `k` as one has seen; one then considers a system of
parameters `(y_i)_{1 ≤ i ≤ m}` of `A` `(16.3.6)`, one takes `B = k[[T_1, …, T_m]]` and one considers the local
homomorphism `w : B → A` which coincides on `k` with an isomorphism `k → k'` and which is such that `w(T_j) = y_j` for
`1 ≤ j ≤ m`. If `A` does not contain a field, the unique homomorphism `ℤ_{pℤ} → A` `(19.8.3)` is necessarily injective
(otherwise, since `A` is integral, its kernel would be the maximal ideal of `ℤ_{pℤ}` and its image isomorphic to a
field); furthermore, one has then `p > 0` by hypothesis, `ℤ_{pℤ}` being a field if `p = 0`. The element `p · 1` of `A`
(identified with `p`) is not a zero-divisor in `A`, and is contained in `𝔪`, hence `(16.3.4 and 16.3.7)` there exists a
family `(y_i)_{1 ≤ i ≤ m−1}` which, with `p`, forms a system of parameters of `A`. The Cohen ring `W` considered at the
beginning of the proof is then a discrete valuation ring of residue field `k`, in which `p` generates the maximal ideal
`(19.8.5)`, and the unique homomorphism `u : W → A` defined at the beginning sends `p` to itself. One then takes
`B = W[[T_1, …, T_{m−1}]]` and one considers the local homomorphism `w : B → A` which coincides with `u` on `W` and is
such that `w(T_i) = y_i` for `1 ≤ i ≤ m − 1`. In both cases, if `𝔫` is the maximal ideal of `B`, it is clear that `𝔫A`
is an ideal of definition of `A`; since in addition `B/𝔫` and `A/𝔪` are isomorphic, `A` is a quasi-finite `B`-module
`(0_I, 7.4.4)`, hence an `A`-module of finite type since `B` is complete and `A` separated for the `𝔫`-preadic
topologies `(0_I, 7.4.1)`. On the other hand,

<!-- original page 208 -->

in both cases one has `dim(B) = dim(A) = m`; in the first case, this follows from `(17.1.4, (iii))`; in the second, one
sees directly that `p` and the `T_i` (`1 ≤ i ≤ m − 1`) form a `B`-regular sequence generating `𝔫`, or one can also use
the fact that these elements generate `𝔫` and that one has `dim(B) ≥ dim(A)` by `(16.3.10)`. Since `A` and `B` are
integral, one finally deduces from `(16.3.10)` that `w` is injective, which completes the proof.

**Corollary (19.8.9).**

<!-- label: 0_IV.19.8.9 -->

*Let `A` be a complete integral Noetherian local ring containing a field `k_0`; let `k` be the residue field of `A`, and
suppose that `k` is finite over `k_0`. Then, in the conclusion of `(19.8.8, (ii))`, one may replace 1° and 2° by the
condition that `B` is of the form `k_0[[T_1, …, T_m]]`, the canonical injection `B → A` being a `k_0`-local homomorphism
(for the usual `k_0`-algebra structure on `B`).*

Indeed, taking up the proof of `(19.8.8, (ii))`, one defines this time `w : k_0[[T_1, …, T_m]] → A` as coinciding on
`k_0` with the identity and sending `T_j` to `y_j` for `1 ≤ j ≤ n`. The hypothesis that `k` is of finite degree over
`k_0` still entails that `A` is a quasi-finite `B`-module, hence of finite type by `(0_I, 7.4.1)`, and one concludes as
in `(19.8.8)`.

**Corollary (19.8.10).**

<!-- label: 0_IV.19.8.10 -->

*Let `A` be an Artinian local ring whose maximal ideal `𝔪` is of square zero; there exists then a regular Noetherian
local ring `B`, with maximal ideal `𝔫`, such that `A` is isomorphic to `B/𝔫²`.*

Let `K` be the residue field `A/𝔪` of `A`, `n` the rank of `𝔪 = 𝔪/𝔪²` on `K`. If `A` contains a field, it follows from
`(19.6.3)` that `A` is isomorphic to `B/𝔟`, where `B = K[[T_1, …, T_n]]` and `𝔟` is contained in the square of the
maximal ideal `𝔫` of `B`; but since `long(B/𝔫²) = n + 1 = long(A)`, one necessarily has `𝔟 = 𝔫²`.

Suppose next that `A` does not contain a field; this entails that `K` is of characteristic `p > 0` and that `p · 1 ≠ 0`
in `A` `(19.6.3)`; hence `p · 1` is an element of `𝔪`, and there are consequently `n − 1` other elements `x_i`
(`2 ≤ i ≤ n`) of `𝔪` forming with `p · 1` a basis of `𝔪` over `K`. Let `W` be a Cohen ring whose residue field is
isomorphic to `K`; `W` is a discrete valuation ring in which `p` generates the maximal ideal; one has seen in the proof
of `(19.8.8)` that there is a homomorphism `u : W → A` sending `p` to itself and which by passage to quotients gives the
identity on `K`. One takes `B = W[[T_2, …, T_n]]` and one considers the local homomorphism `w : B → A` which coincides
with `u` on `W` and is such that `w(T_i) = x_i` for `2 ≤ i ≤ n`. It is clear that `w` is surjective and that its kernel
`𝔟` is contained in the square of the maximal ideal `𝔫 = pB + BT_2 + ⋯ + BT_n` of `B`; since
`long(B/𝔫²) = n + 1 = long(A)`, one again has `𝔟 = 𝔫²`.

**Proposition (19.8.11).**

<!-- label: 0_IV.19.8.11 -->

*Let `A` be an Artinian local ring, `𝔪` its maximal ideal, `k` its residue field. For `A` to be isomorphic to a quotient
ring of a Cohen ring, it is necessary and sufficient that `𝔪` be generated by `p · 1`, where `p` is the characteristic
of `k`.*

The condition is clearly necessary `(19.8.5)`. To see that it is sufficient, one observes, as at the beginning of the
proof of `(19.8.8)`, that there exists a Cohen ring `W` whose residue field is isomorphic to `k` and a local
homomorphism `u : W → A`. Furthermore, if one considers the composite homomorphism `ℤ_{pℤ} → W → A` (which is
necessarily the unique homomorphism of `ℤ_{pℤ}` into `A`), one sees that the image

<!-- original page 209 -->

under `u` of the element `p · 1` of `W` is the element `p · 1` of `A`; since the element `p · 1` of `W` generates the
maximal ideal of this ring, one deduces immediately from the hypothesis that `gr(u) : gr_•(W) → gr_•(A)` is surjective,
and consequently so is `u` `(Bourbaki, Alg. comm., chap. III, §2, n° 8, cor. 2 of th. 1)`.

### 19.9. Relatively formally smooth algebras

**Definition (19.9.1).**

<!-- label: 0_IV.19.9.1 -->

*Let `Λ` be a topological ring, `A` a topological `Λ`-algebra, `B` a topological `A`-algebra. We say that `B` is a
**formally smooth `A`-algebra relatively to `Λ`** if, for every discrete topological `A`-algebra `C` and every nilpotent
ideal `𝔍` of `C`, every continuous `A`-homomorphism `u_0 : B → C/𝔍` which factors as `B → C → C/𝔍`, where `u` is a
continuous `Λ`-homomorphism, also factors as `B → C → C/𝔍`, where `v` is a continuous `A`-homomorphism.*

It follows from this definition that if `B` is a formally smooth `Λ`-algebra, then `B` is also formally smooth
relatively to `Λ`, for any structure of topological `Λ`-algebra defined on `A` (in other words, for any continuous ring
homomorphism `Λ → A`).

**Proposition (19.9.2).**

<!-- label: 0_IV.19.9.2 -->

*Let `Λ` be a topological ring, `A` a topological `Λ`-algebra.*

*(i) `A` is a formally smooth `A`-algebra relatively to `Λ`.*

*(ii) If `B` is a formally smooth `A`-algebra relatively to `Λ` and `C` a formally smooth `B`-algebra relatively to `Λ`,
then `C` is a formally smooth `A`-algebra relatively to `Λ`.*

*(iii) Let `B` be a formally smooth `A`-algebra relatively to `Λ`, `A'` a topological `A`-algebra; then the topological
`A'`-algebra `B ⊗_A A'` is formally smooth relatively to `Λ`.*

*(iv) Let `B` be a topological `A`-algebra, `S` (resp. `T`) a multiplicative subset of `A` (resp. `B`) such that the
canonical image of `S` in `B` is contained in `T`. If `B` is a formally smooth `A`-algebra relatively to `Λ`, then
`T⁻¹ B` is a formally smooth `S⁻¹ A`-algebra relatively to `Λ`.*

*(v) Let `B_i` (`1 ≤ i ≤ n`) be topological `A`-algebras. For `∏_{i=1}^n B_i` to be a formally smooth `A`-algebra
relatively to `Λ`, it is necessary and sufficient that each of the `B_i` be so.*

Assertion (i) is trivial, and the proof of the others is closely modeled on the proofs of `(19.3.5)`; it is therefore
left to the reader.

**Corollary (19.9.3).**

<!-- label: 0_IV.19.9.3 -->

*Let `Λ` be a topological ring, `A` and `A'` two topological `Λ`-algebras. Then the topological `A`-algebra
`B' = B ⊗_A A'` is a formally smooth `A`-algebra relatively to `Λ`.*

This follows from `(19.9.2, (i) and (iii))`.

**Proposition (19.9.4).**

<!-- label: 0_IV.19.9.4 -->

*Let `Λ` be a topological ring, `A` a topological `Λ`-algebra, `B` a topological `A`-algebra. The following conditions
are equivalent:*

*a) `B` is a formally smooth `A`-algebra relatively to `Λ`.*

*b) `B` is a formally smooth `Â`-algebra relatively to `Λ`.*

*c) `B̂` is a formally smooth `A`-algebra relatively to `Λ`.*

*d) `B̂` is a formally smooth `Â`-algebra relatively to `Λ`.*

One again leaves to the reader the proof, modeled on that of `(19.3.6)`.

<!-- original page 210 -->

**(19.9.5)** Likewise, the statement `(19.3.8)` is still valid (with the same proof) when one replaces "formally smooth"
by "formally smooth relatively to `Λ`". If in the statement of `(19.3.10)` one replaces "formally smooth" by "formally
smooth relatively to `Λ`", the conclusion is replaced by the following (the proof remaining essentially unchanged):
every `Λ`-homomorphism `u_0 : B → C/𝔍` which factors as `B → C → C/𝔍`, where `u` is a continuous `Λ`-homomorphism, also
factors as `B → C → C/𝔍`, where `v` is a continuous `A`-homomorphism.

**(19.9.6)** The criteria for formal smoothness `(19.4.1)` and `(19.4.2)` are valid when one replaces "formally smooth"
by "formally smooth relatively to `Λ`", the proofs remaining practically unchanged.

**Proposition (19.9.7).**

<!-- label: 0_IV.19.9.7 -->

*Let `Λ` be a topological ring, `A` a topological `Λ`-algebra, `B` a topological `A`-algebra. Suppose that for every
discrete `A`-algebra `C` and every ideal `𝔍` of `C` such that `𝔍² = 0`, every continuous `A`-homomorphism
`u_0 : B → C/𝔍` which factors as `B → C → C/𝔍`, where `u` is a continuous `Λ`-homomorphism, also factors as
`B → C → C/𝔍`, where `v` is a continuous `A`-homomorphism. Then `B` is a formally smooth `A`-algebra relatively to `Λ`.*

The proof of `(19.4.3)` transcribes immediately.

**Proposition (19.9.8).**

<!-- label: 0_IV.19.9.8 -->

*Let `Λ` be a topological ring, `A` a topological `Λ`-algebra, `B` a topological `A`-algebra. For `B` to be a formally
smooth `A`-algebra relatively to `Λ`, it is necessary and sufficient that for every discrete topological `B`-module `L`
annihilated by an open ideal of `B`, one have (cf. `18.4.2`) `Exalcotop_{A/Λ}(B, L) = 0`.*

With the notation of the proof of `(19.4.4)`, it suffices to note here that one may suppose that the extension `E_λ` of
`B_λ` is `Λ`-trivial; the rest of the proof is then unchanged.

When `Λ`, `A` and `B` are discrete rings, the criterion `(19.9.8)` reduces to

```text
(19.9.8.1)                            Exalcom_{A/Λ}(B, L) = 0              for every B-module L;
```

in other words, every commutative `A`-extension of `B` by a `B`-module, which is `Λ`-trivial, is also `A`-trivial.

[^1]: Also called *simple morphisms* in certain recent works (inspired by the classical terminology "simple point");
    this terminology however leads to confusion, in particular in the theory of algebraic groups.

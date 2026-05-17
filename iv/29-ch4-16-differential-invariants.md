<!-- original page 5 -->

## §16. Differential invariants. Differentially smooth morphisms

In this section we present, in global form, certain notions of differential calculus particularly useful in algebraic
geometry. We pass over many developments that are classical in differential geometry (connections, infinitesimal
transformations associated with a vector field, jets, etc.), although these notions are written in a particularly
natural way in the framework of schemes. We likewise pass over here the phenomena special to characteristic `p > 0`
(some of which are studied, in the affine setting, in `(0, 21)`). For certain complements to the differential formalism
in preschemes the reader may consult Exposés II and VII of `[42]`, as well as later chapters of this Treatise.

### 16.1. Normal invariants of an immersion

**(16.1.1).**

<!-- label: IV.16.1.1 -->

Let `(X, 𝒪_X)`, `(Y, 𝒪_Y)` be two ringed spaces, `f = (ψ, θ) : Y → X` a morphism of ringed spaces `(0_I, 4.1.1)` such
that the homomorphism

```text
  θ^# : ψ*(𝒪_X) → 𝒪_Y
```

is surjective, so that `𝒪_Y` is identified with a quotient sheaf of rings `ψ*(𝒪_X)/𝓘_f`. One can then endow `ψ*(𝒪_X)`
with the `𝓘_f`-preadic filtration.

**Definition (16.1.2).**

<!-- label: IV.16.1.2 -->

*The `𝒪_Y`-augmented sheaf of rings `ψ*(𝒪_X)/𝓘_f^{n+1}` is called the **`n`-th normal invariant of `f`**; the ringed
space `(Y, ψ*(𝒪_X)/𝓘_f^{n+1})` is called the **`n`-th infinitesimal neighbourhood of `Y` for the morphism `f`**, and
denoted `Y_f^{(n)}` or simply `Y^{(n)}`. The sheaf of graded rings associated with the sheaf of filtered rings
`ψ*(𝒪_X)`*

```text
  (16.1.2.1)    𝒢ℛ_•(f) = ⨁_{n ⩾ 0} (𝓘_f^n / 𝓘_f^{n+1})
```

*is called the **sheaf of graded rings associated with `f`**. The sheaf `𝒢ℛ_1(f) = 𝓘_f / 𝓘_f^2` is called the **conormal
sheaf** of `f` (and is also denoted `𝒩_{Y/X}` when no confusion results).*

It is clear that the `𝒪_{Y^{(n)}} = ψ*(𝒪_X)/𝓘_f^{n+1}` (also denoted `𝒪_{Y_f^{(n)}}`) form a

<!-- original page 6 -->

projective system of sheaves of rings on `Y`, the transition homomorphism `φ_{nm} : 𝒪_{Y^{(m)}} → 𝒪_{Y^{(n)}}` for
`n ⩽ m` identifying `𝒪_{Y^{(n)}}` with the quotient of `𝒪_{Y^{(m)}}` by the power `(𝓘_f / 𝓘_f^{m+1})^{n+1}` of the
augmentation ideal of `𝒪_{Y^{(m)}}`, kernel of `φ_{0n} : 𝒪_{Y^{(n)}} → 𝒪_Y`. The `Y^{(n)}` therefore form an inductive
system of ringed spaces, all having the space `Y` as underlying space, and one has canonical morphisms of ringed spaces
`h_n : Y^{(n)} → X` equal to `(ψ, θ_n)`, where `θ_n^#` is the canonical morphism `ψ*(𝒪_X) → ψ*(𝒪_X)/𝓘_f^{n+1}`. It is
clear that the sheaf `𝒢ℛ_•(f)` is a sheaf of graded algebras over the sheaf of rings `𝒪_Y = 𝒢ℛ_0(f)`, and the `𝒢ℛ_k(f)`
are `𝒪_Y`-Modules.

As for any sheaf of filtered rings, one has a canonical surjective homomorphism of graded `𝒪_Y`-algebras

```text
  (16.1.2.2)    𝐒_{𝒪_Y}^•(𝒢ℛ_1(f)) → 𝒢ℛ_•(f)
```

coinciding in degrees `0` and `1` with the identity homomorphisms.

**Examples (16.1.3).**

<!-- label: IV.16.1.3 -->

*(i) Suppose that `X` is a space ringed in local rings, that `Y` is reduced to a single point `y` (endowed with a ring
`𝒪_y`), and that, if `x = ψ(y)`, `θ^# : 𝒪_x → 𝒪_y` is a surjective homomorphism of rings having as kernel the maximal
ideal `𝔪_x` of `𝒪_x`. Then the `𝒪_{Y^{(n)}}` are identified with the rings `𝒪_x/𝔪_x^{n+1}`, and `𝒢ℛ_•(f)` with the
graded ring associated with the local ring `𝒪_x` endowed with its `𝔪_x`-preadic filtration.*

*(ii) Suppose that `Y` is a closed subset of an open subspace `U` of `X` and that `𝒪_Y` is induced on `Y` by a quotient
sheaf `𝒪_U/𝓘`, where `𝓘` is an Ideal of `𝒪_U` such that `𝓘_x = 𝒪_x` for every `x ∉ Y`; if `X` is a space ringed in local
rings, we suppose in addition that `𝓘_x ≠ 𝒪_x` for `x ∈ Y`, so that `(Y, 𝒪_Y)` is again a space ringed in local rings.
Let `ψ_0 : Y → U` be the canonical injection, and denote by `θ_0 : 𝒪_U → (ψ_0)_*(𝒪_Y)` the homomorphism such that
`θ_0^#` is the canonical homomorphism `ψ_0*(𝒪_U) = 𝒪_U|Y → (𝒪_U/𝓘)|Y`, so that `j_0 = (ψ_0, θ_0) : Y → U` is a morphism
of ringed spaces (and of spaces ringed in local rings if `X` is a space ringed in local rings); if `i : U → X` is the
canonical injection (morphism of ringed spaces), `j = i ∘ j_0` is the morphism `(ψ, θ)` of `Y` into `X`, where
`ψ : Y → X` is the canonical injection and `θ : 𝒪_X → ψ_*(𝒪_Y)` is the homomorphism such that `θ^# = θ_0^#`. Since `θ^#`
is surjective, one can apply the preceding definitions; `𝒪_{Y^{(n)}}` is equal to `ψ_0*(𝒪_U/𝓘^{n+1})`, and one has
`(ψ_0)_*(𝒪_{Y^{(n)}}) = 𝒪_U/𝓘^{n+1}` and `𝒢ℛ_n(j) = 𝒢ℛ_n(j_0) = ψ_0*(𝓘^n/𝓘^{n+1}) = j_0*(𝓘^n/𝓘^{n+1})`.*

**(16.1.4).**

<!-- label: IV.16.1.4 -->

The example `(16.1.3, (ii))` shows that in general the `𝒪_{Y^{(n)}}` are not canonically endowed with a structure of
`𝒪_Y`-Module, still less *a fortiori* with a structure of `𝒪_Y`-Algebra. To give such a structure amounts to giving a
homomorphism of sheaves of rings `λ_n : 𝒪_Y → 𝒪_{Y^{(n)}}`, right inverse of the augmentation homomorphism `φ_{0n}`;
equivalently, to giving a morphism of ringed spaces `(1_Y, λ_n) : Y^{(n)} → Y`, left inverse of the canonical morphism
`(1_Y, φ_{0n}) : Y → Y^{(n)}`.

**Proposition (16.1.5).**

<!-- label: IV.16.1.5 -->

*Let `f = (ψ, θ) : Y → X` be an immersion of preschemes. Then:*

*(i) `𝒢ℛ_•(f)` is a quasi-coherent graded `𝒪_Y`-Algebra.*

<!-- original page 7 -->

*(ii) The `Y^{(n)}` are preschemes, canonically isomorphic to sub-preschemes of `X`.*

*(iii) Every homomorphism of sheaves of rings `λ_n : 𝒪_Y → 𝒪_{Y^{(n)}}`, right inverse of the augmentation homomorphism
`φ_{0n}`, makes the `𝒪_{Y^{(n)}}` and the `𝒪_{Y^{(k)}}` for `k ⩽ n` into quasi-coherent `𝒪_Y`-Algebras; the `𝒪_Y`-Module
structures deduced from the preceding structures on the `𝒢ℛ_k(f)` for `k ⩽ n` coincide with those defined in
`(16.1.2)`.*

(i) The question being local on `X` and on `Y`, one can restrict oneself to the case where `Y` is a closed sub-prescheme
of `X` defined by a quasi-coherent Ideal `𝓘` of `𝒪_X`; since `𝒪_Y` is the restriction to `Y` of `𝒪_X/𝓘`, assertion (i)
is evident, and `Y^{(n)}` is the closed sub-prescheme of `X` defined by the quasi-coherent Ideal `𝓘^{n+1}` of `𝒪_X`.
Finally, to prove (iii), note that the datum of `λ_n` makes the Ideal `𝓘/𝓘^{n+1}` of the augmentation `φ_{0n}` and its
quotients `𝓘^k/𝓘^{n+1}` (`1 ⩽ k ⩽ n`) into `𝒪_Y`-Modules, and it suffices to prove by induction on `k` that the
`𝓘^k/𝓘^{n+1}` are quasi-coherent `𝒪_Y`-Modules and that the quotient `𝒪_Y`-Module structure deduced on `𝓘^k/𝓘^{k+1}` is
the same as that defined in `(16.1.2)`. The second assertion is immediate, `𝓘^k/𝓘^{k+1}` being annihilated by
`𝓘/𝓘^{n+1}`; the first follows by induction on `k`: it is trivial for `k = 1`, and `𝓘^k/𝓘^{n+1}` is an extension of
`𝓘^k/𝓘^{k+1}` by `𝓘^{k+1}/𝓘^{n+1}` `(III, 1.4.17)`.

**Corollary (16.1.6).**

<!-- label: IV.16.1.6 -->

*Under the general hypotheses of `(16.1.5)`, if the immersion `f` is locally of finite presentation, the `𝒢ℛ_n(f)` are
quasi-coherent `𝒪_Y`-Modules of finite type.*

Indeed, with the notation of the proof of `(16.1.5)`, `𝓘` is an Ideal of finite type of `𝒪_X` `(1.4.7)`, so the
`𝓘^n/𝓘^{n+1}` are `𝒪_Y`-Modules of finite type, whence the conclusion.

**Corollary (16.1.7).**

<!-- label: IV.16.1.7 -->

*Under the general hypotheses of `(16.1.5)`, let `g : X → Y` be a morphism of preschemes left inverse to `f`. Then, for
every `n`, the composite morphism `(1_Y, λ_n) : Y^{(n)} → X → Y` defines a homomorphism of sheaves of rings
`λ_n : 𝒪_Y → 𝒪_{Y^{(n)}}` right inverse of the augmentation `φ_{0n}`, making `𝒪_{Y^{(n)}}` into a quasi-coherent
`𝒪_Y`-Algebra; for these homomorphisms, the transition homomorphisms `φ_{nm} : 𝒪_{Y^{(m)}} → 𝒪_{Y^{(n)}}` (`n ⩽ m`) are
homomorphisms of `𝒪_Y`-Algebras. In addition, if `g` is locally of finite type, the `𝒪_{Y^{(n)}}` are quasi-coherent
`𝒪_Y`-Modules of finite type.*

The first assertion follows at once from the definitions and from `(16.1.5)`. On the other hand, if `g` is locally of
finite type, then `f` is locally of finite presentation `(1.4.3, (v))`; the `𝒢ℛ_n(f)` are then quasi-coherent
`𝒪_Y`-Modules of finite type by `(16.1.6)`, so the same holds for the `𝒪_Y`-Modules `𝓘/𝓘^{n+1}`, which are extensions of
finitely many of the `𝒢ℛ_k(f)` `(III, 1.4.17)`.

**Proposition (16.1.8).**

<!-- label: IV.16.1.8 -->

*Let `X` be a locally Noetherian prescheme, `j : Y → X` an immersion. Then the `Y^{(n)}` are locally Noetherian
preschemes, the `𝒢ℛ_n(j)` are coherent `𝒪_Y`-Modules, and `𝒢ℛ_•(j)` is a coherent sheaf of rings on the space `Y`.*

Everything being local on `X` and `Y`, one is reduced to the case where `X` is affine and `j` is a closed immersion;
then all the assertions are evident except the last, which follows from the fact that if `A` is a Noetherian ring and
`𝔍` is an ideal of `A`, then `gr_𝔍^•(A)` is a Noetherian ring, taking into account the exactness of the functor `ψ*` and
`(0_I, 5.3.7)`.

<!-- original page 8 -->

**Proposition (16.1.9).**

<!-- label: IV.16.1.9 -->

*Let `X` be a prescheme, `j : Y → X` an immersion locally of finite presentation, `y` a point of `Y`. The following
conditions are equivalent:*

*a) There exists an open neighbourhood `U` of `y` in `Y` such that `j|U` is a homeomorphism of `U` onto an open subset
of `X`.*

*b) There exists an integer `n > 0` such that the canonical homomorphism*

```text
  (φ_{n-1, n})_y : 𝒪_{Y^{(n)}, y} → 𝒪_{Y^{(n-1)}, y}
```

*is bijective.*

*c) There exists an integer `n > 0` such that `(𝒢ℛ_n(j))_y = 0`.*

*Furthermore, if the integer `n` satisfies b) or c), then there exists a neighbourhood `V` of `y` in `Y` such that
`𝒢ℛ_m(j)|V = 0` for `m ⩾ n` and `φ_{nm}|V : 𝒪_{Y^{(m)}}|V → 𝒪_{Y^{(n)}}|V` is bijective for `m ⩾ n`.*

The question being local on `Y`, one can restrict to the case where `j` is a closed immersion, `Y` being defined by a
quasi-coherent Ideal of finite type `𝓘` of `𝒪_X`. The equivalence of b) and c), for a given `n`, is then immediate;
furthermore, since `𝓘^n/𝓘^{n+1}` is an `𝒪_X`-Module of finite type, there exists an open neighbourhood `U` of `y` in `X`
such that `𝓘^n|U = 𝓘^{n+1}|U` `(0_I, 5.2.2)`, hence also `𝓘^n|U = 𝓘^m|U` for `m ⩾ n`, which proves the last assertions.
To prove that a) implies b), one can restrict to the case where the space underlying `Y` is equal to the space
underlying `X`, and where `𝓘` is generated by a finite number of its sections over `X`: as `𝓘` is then contained in the
nilradical `𝒩` of `𝒪_X` `(I, 5.1.2)`, it is nilpotent, which proves b). Finally, to prove that b) implies a), one can
also restrict to the case where `𝓘^n = 𝓘^{n+1}`; then, for every `y ∈ Y`, since `𝓘_y ⊂ 𝔪_y`, the maximal ideal of
`𝒪_{X, y}`, one necessarily has `𝓘_y^n = 0` by Nakayama's lemma, since `𝓘_y` is an ideal of finite type. The set of
`x ∈ X` such that `𝓘_x^n = 0` is therefore an open subset `U` of `X` containing `Y` `(0_I, 5.2.2)`; since on the other
hand `𝓘_x ≠ 0` for `x ∉ Y`, one necessarily has `U = Y`.

**Corollary (16.1.10).**

<!-- label: IV.16.1.10 -->

*For the restriction of the immersion `j` to a neighbourhood of `y` in `Y` to be an open immersion (in other words, for
`j` to be a local isomorphism at the point `y`), it is necessary and sufficient that `(𝒢ℛ_1(j))_y = (𝒩_{Y/X})_y = 0`.*

The condition is obviously necessary, and the preceding reasoning, applied for `n = 1`, proves that it is sufficient.

**Remarks (16.1.11).**

<!-- label: IV.16.1.11 -->

(i) Under the conditions of Definition `(16.1.1)`, the projective limit of the projective system `(𝒪_{Y^{(n)}}, φ_{nm})`
of sheaves of rings on `Y` is called the **normal invariant of infinite order** of `f`, and sometimes denoted
`𝒪_{Y^{(∞)}}`. When `X` is a locally Noetherian prescheme and `j : Y → X` is a closed immersion, so that `Y` is a closed
sub-prescheme of `X` defined by a coherent Ideal `𝓘`, `𝒪_{Y^{(∞)}}` is none other than the formal completion of `𝒪_X`
along `Y` `(I, 10.8.4)`, and `Y^{(∞)} = (Y, 𝒪_{Y^{(∞)}})` is the formal prescheme that is the completion of `X` along
`Y` `(I, 10.8.5)`. In all cases, one may say that `Y^{(∞)}` is the **formal neighbourhood** of `Y` in `X` (for the
morphism `f`). In the particular case just considered, it is therefore the formal prescheme that is the inductive limit
of the infinitesimal neighbourhoods of order `n`.

(ii) Note that for a morphism of preschemes `f = (ψ, θ) : Y → X`, it can happen that the homomorphism
`θ^# : ψ*(𝒪_X) → 𝒪_Y` is surjective without `f` being a local

<!-- original page 9 -->

immersion, and without `ψ` being injective. One has an example by taking for `Y` a sum of preschemes `Y_λ` all
isomorphic to `Spec(𝒪_x)`, where `x ∈ X`, and for `f` the morphism equal to the canonical morphism on each of the `Y_λ`.

### 16.2. Functorial properties of normal invariants of an immersion

**(16.2.1).**

<!-- label: IV.16.2.1 -->

Let `f = (ψ, θ) : Y → X` and `f' = (ψ', θ') : Y' → X'` be two morphisms of ringed spaces such that the homomorphisms
`θ^#` and `θ'^#` are surjective; consider a commutative diagram of morphisms of ringed spaces

```text
  (16.2.1.1)
                  Y  ──f──>  X
                  ↑          ↑
                  u          v
                  │          │
                  Y' ──f'─>  X'
```

Set `u = (ρ, λ)`, `v = (σ, μ)`. One has `ρ*(ψ*(𝒪_X)) = ψ'*(σ*(𝒪_X))`, and consequently a commutative diagram of
homomorphisms of sheaves of rings on `Y'`

```text
  ρ*(ψ*(𝒪_X)) = ψ'*(σ*(𝒪_X)) ──ψ'*(μ^#)──> ψ'*(𝒪_{X'})
              │                                │
              ρ*(θ^#)                          θ'^#
              ↓                                ↓
            ρ*(𝒪_Y) ────────λ^#──────────> 𝒪_{Y'}
```

from which one concludes, if `𝓘` and `𝓘'` are the kernels of `θ^#` and `θ'^#`, that one has `ψ'*(μ^#)(ρ*(𝓘)) ⊂ 𝓘'`, by
exactness of the functor `ρ*`. One deduces at once that for every integer `n`, `ψ'*(μ^#)(ρ*(𝓘^n)) ⊂ 𝓘'^n`, which shows
that `ψ'*(μ^#)` defines, by passage to the quotients, a homomorphism of sheaves of rings

```text
  (16.2.1.2)    ν_n : ρ*(ψ*(𝒪_X)/𝓘^{n+1}) → ψ'*(𝒪_{X'})/𝓘'^{n+1}
```

and consequently a morphism of ringed spaces `w_n = (ρ, ν_n) : Y'^{(n)} → Y^{(n)}` (which, for `n = 0`, is none other
than `u`). It follows at once from this definition that the diagrams

```text
  Y^{(n)}  ──h_{mn}──>  Y^{(m)}  ──h_m──>  X
     ↑                    ↑                ↑
     w_n                  w_m              v        (n ⩽ m)
     │                    │                │
  Y'^{(n)} ──h'_{mn}──> Y'^{(m)} ──h'_m──> X'
```

(where the horizontal arrows are the canonical morphisms `(16.1.2)`) are commutative.

By passage to the quotients from the homomorphisms `(16.2.1.2)`, and taking into

<!-- original page 10 -->

account the exactness of the functor `ρ*`, one obtains a di-homomorphism of graded Algebras (relative to the
homomorphism `λ^# : ρ*(𝒪_Y) → 𝒪_{Y'}`)

```text
  (16.2.1.3)    gr(u) : ρ*(𝒢ℛ_•(f)) → 𝒢ℛ_•(f')
```

(or, if one prefers, a `ρ`-morphism `(0_I, 3.5.1)` `𝒢ℛ_•(f) → 𝒢ℛ_•(f')`), and in particular a di-homomorphism of
conormal sheaves

```text
  gr_1(u) : ρ*(𝒢ℛ_1(f)) → 𝒢ℛ_1(f').
```

It is immediate, moreover, that these homomorphisms give rise to a commutative diagram

```text
  (16.2.1.4)
       ρ*(𝐒_{𝒪_Y}^•(𝒢ℛ_1(f))) ────────> ρ*(𝒢ℛ_•(f))
              │                              │
              𝐒(gr_1(u))                     gr(u)
              ↓                              ↓
       𝐒_{𝒪_{Y'}}^•(𝒢ℛ_1(f'))  ────────>  𝒢ℛ_•(f')
```

where the horizontal arrows are the canonical homomorphisms `(16.1.2.2)`.

Finally, if one has a commutative diagram of morphisms of ringed spaces

```text
       Y   ──f──>  X
       ↑           ↑
       u           v
       │           │
       Y'  ──f'─>  X'
       ↑           ↑
       u'          v'
       │           │
       Y'' ──f''─> X''
```

where `f'' = (ψ'', θ'')` is such that `θ''^#` is surjective, and if `w_n` and `w_n'` are defined from `u`, `v` on the
one hand, and from `u'' = u ∘ u'`, `v'' = v ∘ v'` on the other, then one has `w_n'' = w_n ∘ w_n'`, as follows at once
from the definitions and from `(0_I, 3.5.5)`; likewise `gr(u'') = gr(u') ∘ ρ'*(gr(u))` if `u' = (ρ', λ')`. One can
therefore say that the `Y^{(n)}` and the `𝒢ℛ_•(f)` *depend functorially* on `f`.

**Proposition (16.2.2).**

<!-- label: IV.16.2.2 -->

*With the notation and hypotheses of `(16.2.1)`, suppose moreover that `f`, `f'`, `u` and `v` are morphisms of
preschemes. Then:*

*(i) The morphisms `w_n : Y'^{(n)} → Y^{(n)}` are morphisms of preschemes.*

*(ii) If `Y' = Y ×_X X'`, with `u` and `f'` the canonical projections, and if `f` is an immersion or `v` is flat, one
has `Y'^{(n)} = Y^{(n)} ×_X X'`.*

*(iii) If `Y' = Y ×_X X'` and if `v` is flat (resp. if `f` is an immersion), the homomorphism*

```text
  Gr(u) = gr(u) ⊗ 1 : 𝒢ℛ_•(f) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒢ℛ_•(f')
```

*is bijective (resp. surjective).*

(i) The hypotheses at once imply that for every `y' ∈ Y'`, `ρ_{y'}*(θ_{ψ'(y')}^#)` is a local homomorphism `(I, 1.6.2)`,
so `w_n` is a morphism of preschemes `(I, 2.2.1)`.

<!-- original page 11 -->

(ii) and (iii). If `f` is an immersion, one can restrict to the case where `f` is a closed immersion, `Y` being defined
by the quasi-coherent Ideal `𝓘` of `𝒪_X`, and `Y^{(n)}` by the Ideal `𝓘^{n+1}`; the assertions then follow from
`(I, 4.4.5)`.

Suppose next that `v` is flat; one can restrict to the case where `X = Spec(A)`, `Y = Spec(B)`, `X' = Spec(A')` are
affine, `A'` being a flat `A`-module; then `Y' = Spec(B')` with `B' = B ⊗_A A'`. Moreover, if `𝔍` is the kernel of the
homomorphism `A → B`, the kernel `𝔍'` of `A' → B'` is identified with `𝔍 ⊗_A A'` by flatness, and
`𝔍'^n/𝔍'^{n+1} = (𝔍^n/𝔍^{n+1}) ⊗_A A'`. One deduces at once, taking `(0_I, 4.3.3)` into account, that the
`𝒪_{Y'}`-Module `𝓘'^n/𝓘'^{n+1}` is equal to `(𝓘^n/𝓘^{n+1}) ⊗_{𝒪_Y} 𝒪_{Y'}`, and in particular for `n = 0` one has

```text
  𝒪_{Y'} = ρ*(𝒪_Y) ⊗_{ρ*(ψ*(𝒪_X))} ψ'*(𝒪_{X'}),
```

which proves (iii). Set now `C_n = Γ(Y, 𝒪_{Y^{(n)}})`, `C'_n = Γ(Y', 𝒪_{Y'^{(n)}})`. Since `Y^{(n)}` and `Y'^{(n)}` are
affine schemes `(16.1.5)`, the kernel `𝔎_n` (resp. `𝔎'_n`) of the homomorphism `C_n → C_{n-1}` (resp. `C'_n → C'_{n-1}`)
is `Γ(Y, 𝓘^n/𝓘^{n+1})` (resp. `Γ(Y', 𝓘'^n/𝓘'^{n+1})`), so one deduces from the foregoing that `𝔎'_n = 𝔎_n ⊗_A A'`. One
has a commutative diagram

```text
  0 ──> 𝔎_n ⊗_A A' ──> C_n ⊗_A A' ──> C_{n-1} ⊗_A A' ──> 0
         │                │                │
         r                s_n              s_{n-1}
         ↓                ↓                ↓
  0 ──>  𝔎'_n   ──────> C'_n  ─────────> C'_{n-1}  ─────> 0
```

where the left vertical arrow is bijective and the two rows are exact (`A'` being a flat `A`-module). One deduces by
induction that `s_n` is bijective for all `n`, since it is so by hypothesis for `n = 0`, and the induction step follows
from the five lemma. This proves the second assertion of (ii).

**Corollary (16.2.3).**

<!-- label: IV.16.2.3 -->

*Let `g : X → Y`, `u : Y' → Y` be two morphisms of preschemes, `X' = X ×_Y Y'`, and let `g' : X' → Y'` and `v : X' → X`
be the canonical projections. Let `f : Y → X` be a `Y`-section of `X` (hence an immersion), `f' = f_{(Y')} : Y' → X'`
the `Y'`-section of `X'` deduced from `f` by the base change `u`. Then:*

*(i) The morphism `w_n : Y'_{f'}^{(n)} → Y_f^{(n)}` corresponding to `f`, `f'`, `u`, `v` `(16.2.1)` and the canonical
morphism `h'_n : Y'_{f'}^{(n)} → X'` identify `Y'_{f'}^{(n)}` with the product `Y_f^{(n)} ×_X X'`.*

*(ii) If one endows `𝒪_{Y_f^{(n)}}` (resp. `𝒪_{Y'_{f'}^{(n)}}`) with the structure of `𝒪_Y`-Algebra defined by `g`
(resp. with the structure of `𝒪_{Y'}`-Algebra defined by `g'`) `(16.1.7)`, the homomorphism of `𝒪_{Y'}`-Algebras*

```text
  (16.2.3.1)    ρ*(𝒪_{Y_f^{(n)}}) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒪_{Y'_{f'}^{(n)}}
```

<!-- original page 12 -->

*deduced from the homomorphism `ν_n` `(16.2.1.2)` is bijective. Furthermore, the homomorphism of `𝒪_{Y'}`-Modules*

```text
  (16.2.3.2)    Gr_1(u) : 𝒢ℛ_1(f) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒢ℛ_1(f')
```

*is bijective.*

(i) Note first that the morphisms `f' : Y' → X'` and `u : Y' → Y` identify `Y'` with the product `Y ×_X X'` (for the
structure morphisms `f : Y → X` and `v : X' → X`) `(14.5.12.1)`. The conclusion of (i) then follows from
`(16.2.2, (ii))`, the morphism `g` being an immersion.

(ii) The commutative diagram

```text
                w_n
  Y_f^{(n)} <─────── Y'_{f'}^{(n)}
     │ h_n               │ h'_n
     ↓                   ↓
     X      <─── v ───   X'
     │ g                 │ g'
     ↓                   ↓
     Y      <─── u ───   Y'
```

identifies `Y'_{f'}^{(n)}` with the product `Y_f^{(n)} ×_X X'`, so `(I, 3.3.9)` identifies (for the morphisms
`g' ∘ h'_n` and `w_n`) `Y'_{f'}^{(n)}` with the product `Y_f^{(n)} ×_Y Y'`. Since `Y_f^{(n)}` (resp. `Y'_{f'}^{(n)}`) is
the affine prescheme over `Y` (resp. `Y'`) associated with the `𝒪_Y`-Algebra `𝒪_{Y_f^{(n)}}` (resp. with the
`𝒪_{Y'}`-Algebra `𝒪_{Y'_{f'}^{(n)}}`), the fact that the canonical homomorphism `(16.2.3.1)` is bijective follows from
`(II, 1.5.2)`. Finally, the canonical homomorphism `(16.2.3.1)` is compatible with the augmentations
`𝒪_{Y_f^{(n)}} → 𝒪_Y` and `𝒪_{Y'_{f'}^{(n)}} → 𝒪_{Y'}`; as `𝒪_{Y_f^{(n)}}` is the direct sum (as an `𝒪_Y`-Module) of
`𝒪_Y` and of the augmentation ideal `𝓘/𝓘^{n+1}`, one sees that the canonical homomorphism `(16.2.3.1)`, restricted to
`(𝓘/𝓘^{n+1}) ⊗_{𝒪_Y} 𝒪_{Y'}`, is a bijection of the latter onto `𝓘'/𝓘'^{n+1}`. For `n = 1`, this shows that `Gr_1(u)` is
bijective.

One will note that, under the hypotheses of `(16.2.3)`, the homomorphisms `Gr_n(u)` are surjective by virtue of the
foregoing, but are not bijective in general for `n ⩾ 2`. However:

**Corollary (16.2.4).**

<!-- label: IV.16.2.4 -->

*Under the hypotheses of `(16.2.3)`, suppose that `u : Y' → Y` is a flat morphism (resp. that the `𝒢ℛ_n(f)` are flat
`𝒪_Y`-Modules for `n ⩽ m`). Then the homomorphism*

```text
  Gr_n(u) : 𝒢ℛ_n(f) ⊗_{𝒪_Y} 𝒪_{Y'} → 𝒢ℛ_n(f')
```

*is bijective for every `n` (resp. for `n ⩽ m`).*

If `u` is flat, then so is `v : X' → X`, which is deduced from it by base change, and one knows already in this case
that `Gr(u)` is bijective `(16.2.2, (iii))`. If the `𝒢ℛ_n(f)` are flat for `n ⩽ m`, one sees first by induction on `n`
that the same holds for the `𝓘/𝓘^{n+1}` for `n ⩽ m`, by virtue of the exact sequences

```text
  0 → 𝓘^n/𝓘^{n+1} → 𝓘/𝓘^{n+1} → 𝓘/𝓘^n → 0
```

<!-- original page 13 -->

`(0_I, 6.1.2)`; furthermore one then has commutative diagrams

```text
  0 → (𝓘^n/𝓘^{n+1}) ⊗ 𝒪_{Y'} → (𝓘/𝓘^{n+1}) ⊗ 𝒪_{Y'} → (𝓘/𝓘^n) ⊗ 𝒪_{Y'} → 0
           │                            │                       │
           ↓                            ↓                       ↓
  0 ──>  𝓘'^n/𝓘'^{n+1}    ─────>    𝓘'/𝓘'^{n+1}    ─────>   𝓘'/𝓘'^n   ────> 0
```

in which the rows are exact (the first by flatness `(0_I, 6.1.2)`) and the last two vertical arrows are bijective by
virtue of `(16.2.3, (ii))`; whence the conclusion.

**Remarks (16.2.5).**

<!-- label: IV.16.2.5 -->

(i) The reasoning of `(16.2.2, (i))` still applies when in `(16.2.1.1)` one is dealing with morphisms of spaces ringed
in local rings `(Err_III, (1.8.2))`.

(ii) In `(16.2.2, (ii))`, the conclusion is no longer necessarily valid when one only supposes that `v` and `f` are
morphisms of preschemes (`f` satisfying the condition of `(16.1.1)`). For example (with the notation of the proof of
`(16.2.2, (ii))`), it may happen that `𝔍 = 0` while the kernel `𝔍'` of `A' → B' = B ⊗_A A'` is not zero and `B' ≠ 0`, in
which case one has `Y^{(n)} = Y` for all `n`, but `Y'^{(n)} ≠ Y'`. One has an example of this by taking `A = ℤ`,
`B = ℚ`, `A' = ∏_{h=1}^∞ (ℤ/m^h ℤ)` where `m > 1`.

**(16.2.6).**

<!-- label: IV.16.2.6 -->

Consider the particular case of the diagram `(16.2.1.1)` where `X' = X`, `v` is the identity, `X` is a prescheme, `Y` a
sub-prescheme of `X`, `Y'` a sub-prescheme of `Y`, and `f`, `u`, `f' = f ∘ u` are the canonical injections; the
di-homomorphism `(16.2.1.3)` gives, by tensoring with `𝒪_{Y'}` over `ρ*(𝒪_Y)`, a homomorphism of graded
`𝒪_{Y'}`-Algebras

```text
  (16.2.6.1)    u*(𝒢ℛ_•(f)) → 𝒢ℛ_•(f').
```

On the other hand, one identifies `𝒪_Y` with `ψ*(𝒪_X)/𝓘_f` and `𝒪_{Y'}` with `ρ*(𝒪_Y)/𝓘_u`; since `ρ*` is an exact
functor, one has `ρ*(𝒪_Y) = ρ*(ψ*(𝒪_X))/ρ*(𝓘_f) = ψ'*(𝒪_X)/ρ*(𝓘_f)`, and since `𝒪_{Y'}` is on the other hand identified
with `ψ'*(𝒪_X)/𝓘_{f'}`, one sees that `𝓘_u = 𝓘_{f'}/ρ*(𝓘_f)`. One deduces from this, for every integer `n`, a canonical
homomorphism `𝓘_{f'}^n/𝓘_{f'}^{n+1} → 𝓘_u^n/𝓘_u^{n+1}`, whence a canonical homomorphism of graded `𝒪_{Y'}`-Algebras

```text
  (16.2.6.2)    𝒢ℛ_•(f') → 𝒢ℛ_•(u).
```

**Proposition (16.2.7).**

<!-- label: IV.16.2.7 -->

*Let `X` be a prescheme, `Y` a sub-prescheme of `X`, `Y'` a sub-prescheme of `Y`, `j : Y' → Y` the canonical injection.
Then one has an exact sequence of conormal sheaves (`𝒪_{Y'}`-Modules)*

```text
  (16.2.7.1)    j*(𝒩_{Y/X}) → 𝒩_{Y'/X} → 𝒩_{Y'/Y} → 0
```

*where the arrows are the degree-`1` components of the canonical homomorphisms `(16.2.6.1)` and `(16.2.6.2)`.*

The question being local, one can restrict to the case where `X = Spec(A)`, `Y = Spec(A/𝔍)`, `Y' = Spec(A/𝔎)`, with `𝔍`
and `𝔎` ideals of `A` such that `𝔍 ⊂ 𝔎`; everything reduces to showing

<!-- original page 14 -->

that the sequence of canonical homomorphisms `𝔍/𝔎𝔍 → 𝔎/𝔎² → (𝔎/𝔍)/(𝔎/𝔍)² → 0` is exact, which is immediate, since the
image of `𝔍/𝔎𝔍` in `𝔎/𝔎²` is `(𝔍 + 𝔎²)/𝔎²` and `(𝔎/𝔍)/(𝔎/𝔍)²` is identified with `𝔎/(𝔍 + 𝔎²)`.

It is easy to give examples where the sequence `(16.2.7.1)` extended on the left by a `0` is no longer exact; with the
preceding notation, it suffices to take `A = k[T]`, `𝔍 = AT²`, `𝔎 = AT`, because then one has `(𝔍 + 𝔎²)/𝔎² = 0` and
`𝔍/𝔎𝔍 ≠ 0`. See, however, `(16.9.13)` and `(19.1.5)` for useful cases where the extended sequence remains exact.

### 16.3. Fundamental differential invariants of a morphism of preschemes

**Definition (16.3.1).**

<!-- label: IV.16.3.1 -->

*Let `f : X → S` be a morphism of preschemes, `Δ_f : X → X ×_S X` the corresponding diagonal morphism, which is an
immersion `(I, 5.3.9` and `Err_III, 10)`. One denotes by `𝒫_f^n` or `𝒫_{X/S}^n`, and calls the **sheaf of principal
parts of order `n` of the `S`-prescheme `X`**, the `𝒪_X`-augmented sheaf of rings `n`-th normal invariant of `Δ_f`
`(16.1.2)`. One sets `𝒫_f^∞ = 𝒫_{X/S}^∞ = lim←_n 𝒫_{X/S}^n`, `𝒢ℛ_n(𝒫_f) = 𝒢ℛ_n(𝒫_{X/S}) = 𝒢ℛ_n(Δ_f)` `(16.1.2)`; the
`𝒪_X`-Module `𝒢ℛ_1(Δ_f)`, augmentation ideal of `𝒫_{X/S}^1`, is also denoted `Ω_f^1` or `Ω_{X/S}^1`, and is called the
**`𝒪_X`-Module of `1`-differentials** of `f`, or of `X` with respect to `S`, or of the `S`-prescheme `X`.*

It follows from this definition that `𝒫_{X/S}^0` is canonically identified with `𝒪_X` `(16.1.2)`.

One has `(16.1.2.2)` a canonical surjective homomorphism of graded `𝒪_X`-Algebras

```text
  (16.3.1.1)    𝐒_{𝒪_X}^•(Ω_{X/S}^1) → 𝒢ℛ_•(𝒫_{X/S}).
```

It also follows from Definition `(16.3.1)` that for every open `U` of `X`, one has `𝒫_{f|U}^n = 𝒫_f^n|U`,
`𝒫_{f|U}^∞ = 𝒫_f^∞|U`, `𝒢ℛ_n(𝒫_{f|U}) = 𝒢ℛ_n(𝒫_f)|U`, `Ω_{f|U}^1 = Ω_f^1|U` (in other words, the notions introduced are
local on `X`).

**(16.3.2).**

<!-- label: IV.16.3.2 -->

Denote by `p_1`, `p_2` the two canonical projections of the product `X ×_S X`; since `Δ_f` is an `X`-section of
`X ×_S X` for both morphisms `p_1` and `p_2`, *each* of these morphisms defines, for every `n`, a homomorphism of
sheaves of rings `𝒪_X → 𝒫_{X/S}^n`, right inverse to the augmentation `𝒫_{X/S}^n → 𝒪_X` `(16.1.7)`; one can also say
that one thus defines on `𝒫_{X/S}^n` *two* quasi-coherent augmented `𝒪_X`-Algebra structures; the corresponding
`𝒪_X`-Module structures on `𝒢ℛ_n(𝒫_{X/S})` are the same. One similarly has, by passage to the limit, two `𝒪_X`-Algebra
structures on `𝒫_{X/S}^∞`.

**(16.3.3).**

<!-- label: IV.16.3.3 -->

The morphism `s = (p_2, p_1)_S : X ×_S X → X ×_S X` is an involutive automorphism of `X ×_S X`, called the **canonical
symmetry**, such that

```text
  (16.3.3.1)    p_1 ∘ s = p_2,   p_2 ∘ s = p_1,   s ∘ Δ_f = Δ_f.
```

If one sets `s = (ρ, λ)`, `p_i = (π_i, μ_i)` (`i = 1, 2`), `Δ_f = (δ, ν)`, then `λ^#` is an isomorphism of
`ρ*(π_1*(𝒪_X))` onto `π_2*(𝒪_X)`, and `δ*(λ^#)` leaves invariant `δ*(𝒪_{X ×_S X})` and the kernel `𝓘` of the
homomorphism `ν^# : δ*(𝒪_{X ×_S X}) → 𝒪_X`. Therefore:

**Proposition (16.3.4).**

<!-- label: IV.16.3.4 -->

*The homomorphism `σ = δ*(λ^#)` deduced from `s` (and also called the canonical symmetry) is an involutive automorphism
of the projective system `(𝒫_{X/S}^n)` of `𝒪_X`-augmented*

<!-- original page 15 -->

*sheaves of rings, and consequently also of their projective limit `𝒫_{X/S}^∞`. This automorphism permutes the two
`𝒪_X`-Algebra structures on the `𝒫_{X/S}^n` and on `𝒫_{X/S}^∞`.*

**(16.3.5).**

<!-- label: IV.16.3.5 -->

In what follows, the two `𝒪_X`-Algebra structures defined on the `𝒫_{X/S}^n` and on `𝒫_{X/S}^∞` will play very different
roles: *we shall agree from now on, unless expressly stated otherwise, that when `𝒫_{X/S}^n` or `𝒫_{X/S}^∞` is
considered as an `𝒪_X`-Algebra, it is the algebra structure defined by `p_1` that is meant.*

For every open `U` of `X` and every section `t ∈ Γ(U, 𝒪_X)`, one will denote simply by `t · 1` or even `t` the image of
`t` under the structural homomorphism `Γ(U, 𝒪_X) → Γ(U, 𝒫_{X/S}^n)` (resp. `Γ(U, 𝒪_X) → Γ(U, 𝒫_{X/S}^∞)`) (that is to
say, the homomorphism corresponding to `p_1`).

**Definition (16.3.6).**

<!-- label: IV.16.3.6 -->

*One denotes by `d_f^n`, or `d_{X/S}^n` (resp. `d_f^∞`, or `d_{X/S}^∞`), or simply `d^n` (resp. `d^∞`), the homomorphism
of sheaves of rings `𝒪_X → 𝒫_f^n = 𝒫_{X/S}^n` (resp. `𝒪_X → 𝒫_f^∞ = 𝒫_{X/S}^∞`) deduced from `p_2`. For every open `U`
of `X` and every `t ∈ Γ(U, 𝒪_X)`, `d^n t` (resp. `d^∞ t`) is called the **principal part of order `n`** (resp.
**principal part of infinite order**) of `t`. One sets `dt = d^1 t - t · 1`, and `dt` is called the **differential of
`t`** (an element of `Γ(U, Ω_{X/S}^1)`, also denoted `d_{X/S}(t)`).*

It follows at once from this definition that one has

```text
  (16.3.6.1)    d(t_1 t_2) = t_1 dt_2 + t_2 dt_1
```

for any `t_1`, `t_2` in `Γ(U, 𝒪_X)`, that is to say, *`d` is a derivation* of the ring `Γ(U, 𝒪_X)` into the
`Γ(U, 𝒪_X)`-module `Γ(U, Ω_{X/S}^1)`.

In all the notation introduced in `(16.3.1)` and `(16.3.6)`, one will sometimes replace `S` by `A` when `S = Spec(A)`.

**(16.3.7).**

<!-- label: IV.16.3.7 -->

Suppose in particular that `S = Spec(A)` and `X = Spec(B)` are affine schemes, `B` being therefore an `A`-algebra. Then
`Δ_f` corresponds to the canonical surjective homomorphism `π : B ⊗_A B → B` such that `π(b ⊗ b') = b b'`, with kernel
`𝔍 = 𝔍_{B/A}` `(0, 20.4.1)`; `𝒫_f^n` is the structure sheaf of the prescheme `Spec(P_{B/A}^n)`, where

```text
  P_{B/A}^n = (B ⊗_A B) / 𝔍^{n+1};
```

`𝒢ℛ_•(𝒫_f)` is the quasi-coherent `𝒪_X`-Module corresponding to the graded `B`-module

```text
  gr_𝔍^•(B ⊗_A B) = ⨁_{n ⩾ 0} (𝔍^n / 𝔍^{n+1});
```

in particular `Ω_f^1 = Ω_{X/S}^1` is the quasi-coherent `𝒪_X`-Module corresponding to the `B`-module of
`1`-differentials of `B` with respect to `A`, namely `Ω_{B/A}^1` `(0, 20.4.3)`. The projection morphisms
`p_1 : X ×_S X → X`, `p_2 : X ×_S X → X` correspond to the two ring homomorphisms `j_1 : B → B ⊗_A B`,
`j_2 : B → B ⊗_A B` such that `j_1(b) = b ⊗ 1`, `j_2(b) = 1 ⊗ b`, so that (by the convention of `(16.3.5)`) `P_{B/A}^n`
is always considered as a `B`-algebra via the composite homomorphism `B → B ⊗_A B → P_{B/A}^n`; the ring homomorphism
`B → B ⊗_A B → P_{B/A}^n` deduced from `j_2` is denoted `d_{B/A}^n` and corresponds to `d_{X/S}^n` acting on
`Γ(X, 𝒪_X)`; for every `t ∈ B`, `dt` is equal to `d_{B/A} t`, defined in `(0, 20.4.6)` (cf. `Err_IV, 11`).

If `π_n : B ⊗_A B → P_{B/A}^n` is the canonical homomorphism, one therefore has, by virtue of the preceding definitions,

```text
  (16.3.7.1)    π_n(b ⊗ b') = b · π_n(1 ⊗ b') = b · d_{B/A}^n(b')   for b ∈ B, b' ∈ B.
```

<!-- original page 16 -->

**Proposition (16.3.8).**

<!-- label: IV.16.3.8 -->

*The image of the homomorphism `d_{X/S}^n : 𝒪_X → 𝒫_{X/S}^n` generates the `𝒪_X`-Module `𝒫_{X/S}^n`.*

One reduces at once to the case where `X = Spec(B)` and `S = Spec(A)` are affine, and the proposition follows from
`(16.3.7.1)` since `π_n` is surjective. Note that in general `d_{X/S}^n` is not surjective (even already for `n = 1`).

**Proposition (16.3.9).**

<!-- label: IV.16.3.9 -->

*Suppose that `f : X → S` is a morphism locally of finite type. Then the `𝒫_{X/S}^n` and the `𝒢ℛ_n(𝒫_{X/S})` are
quasi-coherent `𝒪_X`-Modules of finite type.*

This follows from `(16.1.6)` and from the fact that `Δ_f` is locally of finite presentation `(1.4.3.1)`.

### 16.4. Functorial properties of differential invariants

**(16.4.1).**

<!-- label: IV.16.4.1 -->

Consider a commutative diagram of morphisms of preschemes

```text
  (16.4.1.1)
                  X   <──u──   X'
                  │            │
                  f            f'
                  ↓            ↓
                  S   <──w──   S'
```

One deduces a commutative diagram

```text
                   X        <──u──    X'
                   │                  │
                   Δ_f                Δ_{f'}
                   ↓                  ↓
                X ×_S X   <──v──   X' ×_{S'} X'
```

where `v` is the composite morphism `(I, 5.3.5` and `5.3.15)`

```text
  (16.4.1.2)    X' ×_{S'} X' ──(p'_1, p'_2)_S──> X' ×_S X' ──u ×_S u──> X ×_S X.
```

One therefore deduces from `u` and `v`, as was explained in `(16.2.1)`, homomorphisms of augmented sheaves of rings

```text
  (16.4.1.3)    ν_n : ρ*(𝒫_{X/S}^n) → 𝒫_{X'/S'}^n
```

(where one has set `u = (ρ, λ)`); these homomorphisms form a projective system, and consequently give at the limit a
homomorphism of augmented sheaves of rings

```text
  (16.4.1.4)    ν_∞ : ρ*(𝒫_{X/S}^∞) → 𝒫_{X'/S'}^∞;
```

on the other hand, by passage to the quotients, the homomorphisms `ν_n` give a di-homomorphism of graded Algebras
(relative to `λ^#`):

```text
  (16.4.1.5)    gr(u) : ρ*(𝒢ℛ_•(𝒫_{X/S})) → 𝒢ℛ_•(𝒫_{X'/S'}).
```

<!-- original page 17 -->

**(16.4.2).**

<!-- label: IV.16.4.2 -->

If one has a commutative diagram

```text
        X   <──u──   X'  <──u'──  X''
        │            │            │
        f            f'           f''
        ↓            ↓            ↓
        S   <──w──   S'  <──w'──  S''
```

one deduces a commutative diagram

```text
              X       <──u──     X'     <──u'──     X''
              │                  │                  │
              Δ_f                Δ_{f'}             Δ_{f''}
              ↓                  ↓                  ↓
           X ×_S X   <──v──   X' ×_{S'} X'  <─v'─  X'' ×_{S''} X''
```

where `v'` is defined from `u'`, `w'`, `f'`, `f''` as `v` was from `u`, `w`, `f`, `f'`. One verifies at once that if
`u'' = u ∘ u'`, `w'' = w ∘ w'`, then the composite morphism `v ∘ v'` is equal to the morphism `v''` defined from `u''`,
`w''`, `f`, `f''` as `v` was from `u`, `w`, `f`, `f'`. If one sets `u' = (ρ', λ')`, `u'' = (ρ'', λ'')`, it then follows
from `(16.2.1)` that the homomorphism `ν''_n : ρ''*(𝒫_{X/S}^n) → 𝒫_{X''/S''}^n` is equal to the composite

```text
  ρ'*(ρ*(𝒫_{X/S}^n)) ──ρ'*(ν_n)──> ρ'*(𝒫_{X'/S'}^n) ──ν'_n──> 𝒫_{X''/S''}^n,
```

and one has analogous transitivity properties for the homomorphisms `(16.4.1.4)` and `(16.4.1.5)`, which allows one to
say that the `𝒫_{X/S}^n`, `𝒫_{X/S}^∞` and `𝒢ℛ_•(𝒫_{X/S})` *depend functorially on `f`*.

**(16.4.3).**

<!-- label: IV.16.4.3 -->

One verifies at once (for example by reducing to the affine case using `(16.3.7)`) that with the notation of `(16.4.1)`,
the diagram

```text
  (16.4.3.1)
              ρ*(𝒪_X)  ──λ^#──>  𝒪_{X'}
                │                  │
                ↓                  ↓
            ρ*(𝒫_{X/S}^n) ──ν_n──> 𝒫_{X'/S'}^n
```

where the vertical arrows are those defining the algebra structures chosen in `(16.3.5)` (that is to say, those coming
from the first projections), is commutative; the same holds for the diagram

```text
  (16.4.3.2)
              ρ*(𝒪_X)         ──λ^#──>      𝒪_{X'}
                │                              │
                ρ*(d_{X/S}^n)                  d_{X'/S'}^n
                ↓                              ↓
            ρ*(𝒫_{X/S}^n)   ──ν_n──>      𝒫_{X'/S'}^n
```

<!-- original page 18 -->

the vertical arrows here defining the algebra structures coming from the second projections; moreover, if `σ` and `σ'`
are the canonical symmetries corresponding to `f` and `f'` `(16.3.4)`, one has

```text
  ν_n ∘ ρ*(σ) = σ' ∘ ν_n
```

which lets one pass from one of the preceding diagrams to the other. One therefore deduces from `(16.4.3.1)` a canonical
homomorphism of augmented `𝒪_{X'}`-Algebras

```text
  (16.4.3.3)    P^n(u) : u*(𝒫_{X/S}^n) = 𝒫_{X/S}^n ⊗_{𝒪_X} 𝒪_{X'} → 𝒫_{X'/S'}^n
```

and it follows from `(16.4.3.2)` that the diagram

```text
  (16.4.3.4)
              𝒪_{X'}             ──id──>          𝒪_{X'}
                │                                  │
                u*(d_{X/S}^n)                      d_{X'/S'}^n
                ↓                                  ↓
            u*(𝒫_{X/S}^n)     ──P^n(u)──>      𝒫_{X'/S'}^n
```

is commutative. One deduces from it a homomorphism of graded `𝒪_{X'}`-Algebras

```text
  (16.4.3.5)    Gr_•(u) : u*(𝒢ℛ_•(𝒫_{X/S})) → 𝒢ℛ_•(𝒫_{X'/S'})
```

and in particular a homomorphism of `𝒪_{X'}`-Modules

```text
  (16.4.3.6)    Gr_1(u) : Ω_{X/S}^1 ⊗_{𝒪_X} 𝒪_{X'} → Ω_{X'/S'}^1
```

giving rise to a commutative diagram

```text
  (16.4.3.7)
              𝒪_{X'}                ──id──>               𝒪_{X'}
                │                                            │
                d_{X/S} ⊗ 1                                  d_{X'/S'}
                ↓                                            ↓
            Ω_{X/S}^1 ⊗_{𝒪_X} 𝒪_{X'}    ────────────>    Ω_{X'/S'}^1
```

**(16.4.4).**

<!-- label: IV.16.4.4 -->

When `S = Spec(A)`, `S' = Spec(A')`, `X = Spec(B)`, `X' = Spec(B')` are affine, so that one has a commutative diagram of
ring homomorphisms

```text
              B  ──>  B'
              ↑       ↑
              A  ──>  A'
```

the image of `𝔍_{B/A}` in `B' ⊗_{A'} B'` is contained in `𝔍_{B'/A'}`, and the homomorphism `ν_n` corresponds to the ring
homomorphism `P_{B/A}^n → P_{B'/A'}^n` deduced from the homomorphism `B ⊗_A B → B' ⊗_{A'} B'` by passage to the
quotients. The homomorphism `(16.4.3.6)` corresponds to the homomorphism defined in `(0, 20.5.4.1)`, and the commutative
diagram `(16.4.3.7)` to the diagram `(0, 20.5.4.2)`.

**Proposition (16.4.5).**

<!-- label: IV.16.4.5 -->

*Suppose that `X' = X ×_S S'`, with `f'` and `u` the canonical projections.*

<!-- original page 19 -->

*Then the canonical homomorphisms `P^n(u)` `(16.4.3.3)` and `Gr_1(u)` `(16.4.3.6)` are bijective.*

One indeed has `X' ×_{S'} X' = (X ×_S X) ×_S S'`, and it suffices to apply `(16.2.3, (ii))` replacing `g` by the first
projection `p_1 : X ×_S X → X` and `f` by the diagonal `Δ_f`.

One will note also that under the hypotheses of `(16.4.5)`, the homomorphism `Gr_•(u)` `(16.4.3.5)` is surjective, but
not bijective in general. However `(16.2.4)`:

**Corollary (16.4.6).**

<!-- label: IV.16.4.6 -->

*With the hypotheses of `(16.4.5)`, suppose in addition that `w : S' → S` is flat (resp. that the `𝒢ℛ_n(𝒫_{X/S})` are
flat `𝒪_X`-Modules for `n ⩽ m`); then the homomorphism*

```text
  Gr_n(u) : u*(𝒢ℛ_n(𝒫_{X/S})) → 𝒢ℛ_n(𝒫_{X'/S'})
```

*is bijective for every `n` (resp. for `n ⩽ m`).*

Indeed, if `w` is flat, so is `v : X' ×_{S'} X' → X ×_S X`, deduced from it by base change, and the conclusion follows
from `(16.2.4)`.

**(16.4.7).**

<!-- label: IV.16.4.7 -->

Let `S` be a prescheme, `ℰ` a quasi-coherent `𝒪_S`-Module, and set `X = 𝐕(ℰ)` `(II, 1.7.8)`, the **vector bundle**
associated with `ℰ`, equal to `Spec(𝐒_{𝒪_S}(ℰ))`. Let `f : X → S` be the structure morphism. For every open `U` of `S`
and every section `t ∈ Γ(U, ℰ)`, `t` is identified with a section of `𝐒_{𝒪_S}(ℰ)` over `U`; let `t'` be its image in
`Γ(f^{-1}(U), 𝒪_X) = Γ(U, f_*(𝒪_X)) = Γ(U, 𝐒_{𝒪_S}(ℰ))`, and set

```text
  (16.4.7.1)    δ(t) = d_{X/S}^n(t') - t' ∈ Γ(f^{-1}(U), 𝒫_{X/S}^n);
```

it is clear that `δ` is a di-homomorphism of modules (corresponding to the ring homomorphism
`Γ(U, 𝒪_S) → Γ(f^{-1}(U), 𝒪_X)`) of `Γ(U, ℰ)` into `Γ(f^{-1}(U), 𝒫_{X/S}^n)`, whose image moreover belongs to the
augmentation ideal of `Γ(f^{-1}(U), 𝒫_{X/S}^n)`. One deduces (by varying `U`) a canonical homomorphism of `𝒪_X`-Algebras

```text
  (16.4.7.2)    f*(𝐒_{𝒪_S}(ℰ)) → 𝒫_{X/S}^n
```

and by the preceding remark, if `𝒦` is the Ideal kernel of the augmentation `𝐒_{𝒪_S}(ℰ) → 𝒪_S`, the image of `𝒦^{n+1}`
under `(16.4.7.2)` is zero, so that by factoring through `𝒦^{n+1}` one finally has a canonical homomorphism

```text
  (16.4.7.3)    δ_n : f*(𝐒_{𝒪_S}(ℰ)/𝒦^{n+1}) → 𝒫_{X/S}^n.
```

**Proposition (16.4.8).**

<!-- label: IV.16.4.8 -->

*Under the conditions of `(16.4.7)`, the homomorphisms `δ_n` are bijective and form a projective system of isomorphisms;
one deduces an isomorphism of graded `𝒪_X`-Algebras*

```text
  (16.4.8.1)    f*(𝐒_{𝒪_S}^•(ℰ)) ⥲ 𝒢ℛ_•(𝒫_{X/S}).
```

The fact that the homomorphisms `(16.4.7.3)` form a projective system follows at once from their definition. To prove
that they are isomorphisms, it suffices to

<!-- original page 20 -->

show that `(16.4.8.1)` is an isomorphism, the filtrations of the two sides of `(16.4.7.3)` being finite (Bourbaki, *Alg.
comm.*, chap. III, §2, n° 8, cor. 3 of th. 1). For this, consider the split exact sequence of `𝒪_S`-Modules

```text
  (16.4.8.2)    0 → ℰ ──u──> ℰ ⊕ ℰ ──v──> ℰ → 0
```

where, for every pair of sections `s`, `t` of `ℰ` over an open `U` of `S`, one takes `u(s) = (-s, s)` and
`v(s, t) = s + t`. One has

```text
  X ×_S X = Spec(𝐒_{𝒪_S}(ℰ) ⊗_{𝒪_S} 𝐒_{𝒪_S}(ℰ)) = Spec(𝐒_{𝒪_S}(ℰ ⊕ ℰ))
```

`(II, 1.4.6` and `1.7.11)`, and the diagonal morphism `X → X ×_S X` corresponds `(II, 1.2.7)` to the homomorphism of
`𝒪_S`-Algebras `𝐒(v) : 𝐒_{𝒪_S}(ℰ ⊕ ℰ) → 𝐒_{𝒪_S}(ℰ)` `(II, 1.7.4)`, so that if `𝓘` is the kernel of this homomorphism,
one has

```text
  𝒫_{X/S}^n = f*(𝐒_{𝒪_S}(ℰ ⊕ ℰ) / 𝓘^{n+1}).
```

The proposition will be a consequence of the following lemma:

**Lemma (16.4.8.3).**

<!-- label: IV.16.4.8.3 -->

*Let `Y` be a ringed space, `0 → ℱ' ──u──> ℱ ──v──> ℱ'' → 0` an exact sequence of `𝒪_Y`-Modules such that every point
`y ∈ Y` has an open neighbourhood `V` such that the sequence `0 → ℱ'|V → ℱ|V → ℱ''|V → 0` is split. Let `𝓘` be the Ideal
kernel of `𝐒(v) : 𝐒_{𝒪_Y}(ℱ) → 𝐒_{𝒪_Y}(ℱ'')`, and let `gr_𝓘^•(𝐒_{𝒪_Y}(ℱ))` be the graded `𝒪_Y`-Algebra associated with
the `𝒪_Y`-Algebra `𝐒_{𝒪_Y}(ℱ)` endowed with the `𝓘`-preadic filtration. Then the homomorphism of graded `𝒪_Y`-Algebras*

```text
  (16.4.8.4)    𝐒_{𝒪_Y}^•(ℱ') ⊗_{𝒪_Y} 𝐒_{𝒪_Y}^•(ℱ'') → gr_𝓘^•(𝐒_{𝒪_Y}(ℱ))
```

*(where the first member is the graded tensor product of symmetric `𝒪_Y`-Algebras endowed with their canonical gradation
`(II, 1.7.4` and `2.1.2)`), arising from the canonical injection*

```text
  ℱ' → 𝓘 = gr_𝓘^1(𝐒_{𝒪_Y}(ℱ)),
```

*is bijective.*

The injection `ℱ' → 𝓘` indeed canonically gives a homomorphism of graded `𝒪_Y`-Algebras
`𝐒_{𝒪_Y}^•(ℱ') → gr_𝓘^•(𝐒_{𝒪_Y}(ℱ))`, and since the second member is by definition a graded `𝐒_{𝒪_Y}^•(ℱ'')`-Algebra,
one deduces the canonical homomorphism `(16.4.8.4)` by tensoring the previous one with `𝐒_{𝒪_Y}^•(ℱ'')`. To prove the
lemma, since the question is local, one can restrict to the case where `ℱ = ℱ' ⊕ ℱ''`, with `u` and `v` the canonical
homomorphisms. Then the graded Algebra `𝐒_{𝒪_Y}^•(ℱ)` is canonically identified with the graded tensor product
`𝐒_{𝒪_Y}^•(ℱ') ⊗_{𝒪_Y} 𝐒_{𝒪_Y}^•(ℱ'')` `(II, 1.7.4)`, and it is immediate that `𝓘` is then the Ideal
`𝓘' ⊗_{𝒪_Y} 𝐒_{𝒪_Y}^•(ℱ'')`, where `𝓘'` is the augmentation ideal of `𝐒_{𝒪_Y}^•(ℱ')`, that is to say the (direct) sum of
the `𝐒_{𝒪_Y}^m(ℱ')` for `m ⩾ 1`. One concludes that `𝓘^n = 𝓘'^n ⊗_{𝒪_Y} 𝐒_{𝒪_Y}^•(ℱ'')`, where this time `𝓘'^n` is the
(direct) sum of the `𝐒_{𝒪_Y}^m(ℱ')` for `m ⩾ n`; one therefore has `𝓘^n/𝓘^{n+1} = 𝐒_{𝒪_Y}^n(ℱ') ⊗_{𝒪_Y} 𝐒_{𝒪_Y}^•(ℱ'')`,
which proves that `(16.4.8.4)` is bijective.

<!-- original page 21 -->

The lemma being established, it remains to check that the homomorphism `(16.4.8.1)` is the image under `f*` of the
homomorphism `(16.4.8.4)` corresponding to the exact sequence `(16.4.8.2)`; one verifies easily that this follows from
the definition of `u` `(16.4.8.2)` and of `δ` `(16.4.7.1)`, taking into account the definition of the `𝒪_X`-Algebra
structure on `𝒫_{X/S}^n` and that of `d_{X/S}^n` `(16.3.5` and `16.3.6)`.

In particular:

**Corollary (16.4.9).**

<!-- label: IV.16.4.9 -->

*Under the conditions of `(16.4.7)`, one has a canonical isomorphism*

```text
  (16.4.9.1)    gr_1(δ) : f*(ℰ) ⥲ Ω_{X/S}^1.
```

**Corollary (16.4.10).**

<!-- label: IV.16.4.10 -->

*If `S = Spec(A)`, `ℰ = 𝒪_S^m`, so that*

```text
  X = Spec(A[T_1, …, T_m]),
```

*then `𝒫_{X/S}^n` is canonically identified with the `𝒪_X`-Algebra corresponding to the quotient
`A[T_1, …, T_m]`-algebra `A[T_1, …, T_m, U_1, …, U_m]/𝔎^{n+1}`, where the `U_i` (`1 ⩽ i ⩽ m`) are `m` new indeterminates
and `𝔎` is the ideal generated by `U_1, …, U_m`.*

One thus recovers in particular the structure of `Ω_{X/S}^1` in this case `(0, 20.5.13)`.

Note moreover that `d_{X/S}^n` then assigns to a polynomial `F(T_1, …, T_m)` the class modulo `𝔎^{n+1}` of
`F(T_1 + U_1, …, T_m + U_m)`, as follows from the definition `(16.4.7.1)`.

**Proposition (16.4.11).**

<!-- label: IV.16.4.11 -->

*Let `f : X → S` be a morphism, `g : S → X` an `S`-section of `X`, `S_g^{(n)}` the `n`-th infinitesimal neighbourhood of
`S` for the immersion `g` `(16.1.2)`. Then there exists one and only one isomorphism of `𝒪_S`-Algebras*

```text
  (16.4.11.1)    ϖ_n : g*(𝒫_{X/S}^n) ⥲ 𝒪_{S_g^{(n)}}
```

*(for the `𝒪_S`-Algebra structure on `𝒪_{S_g^{(n)}}` defined by `f` `(16.1.7)`) making the diagram*

```text
  (16.4.11.2)
              𝒪_S = g*(𝒪_X)  ────λ_n────>  𝒪_{S_g^{(n)}}
                     ╲                     ╱
            g*(d_{X/S}^n) ╲               ╱ ϖ_n
                          ↘             ↗
                          g*(𝒫_{X/S}^n)
```

*commutative (where `λ_n` is the structural homomorphism).*

By virtue of `(I, 5.3.7)`, where one replaces `X`, `Y`, `S` by `S`, `X`, `S` respectively and `f` by `g`, the diagrams

```text
  (16.4.11.3)
       S  ──g──>  X                  S  ──g──>  X
       │          │                  │          │
       g          Δ_f                g          Δ_f
       ↓          ↓                  ↓          ↓
       X ──(g∘f, 1_X)_S──> X ×_S X   X ──(1_X, g∘f)_S──> X ×_S X
```

<!-- original page 22 -->

identify `S` with the product of the `(X ×_S X)`-preschemes `X` and `X` for the morphisms `Δ_f` and `(g ∘ f, 1_X)_S`
(resp. `(1_X, g ∘ f)_S`). On the other hand, the diagrams

```text
  (16.4.11.4)
       X ──(g∘f, 1_X)_S──> X ×_S X    X ──(1_X, g∘f)_S──> X ×_S X
       │                   │          │                   │
       f                   p_1        f                   p_2
       ↓                   ↓          ↓                   ↓
       S ─────g─────>      X          S ─────g─────>      X
```

identify `X` with the product of the `X`-preschemes `S` and `X ×_S X` for the morphisms `g` and `p_1` (resp. `p_2`) (a
particular case of the associativity formula `(I, 3.3.9.1)`). One can say that `Δ_f`, considered as an `X`-section of
`X ×_S X` (relative to `p_1` or `p_2`), plays the role of a *universal section* for the `S`-sections of `X`: each such
section `g` is in fact deduced from it by the base change `(g ∘ f, 1_X)_S : X → X ×_S X`. The definition of the
homomorphism `ϖ_n` and the fact that it is bijective therefore follow from these remarks and from `(16.2.3, (ii))`
applied to the first diagram `(16.4.11.4)`. The commutativity of the diagram `(16.4.11.2)` likewise follows from
`(16.2.3, (ii))` applied this time to the second diagram `(16.4.11.4)`. To make `ϖ_n` explicit, one can restrict to the
case where `g` is a closed immersion: indeed, for every `s ∈ S`, there is an open neighbourhood `W` of `s` in `S` such
that `g(W)` is closed in an open set `U` of `X`, and it is clear that `g|W` is a `W`-section of the morphism
`U ∩ f^{-1}(W) → W`, restriction of `f`, and `g(W)` is *a fortiori* closed in `U ∩ f^{-1}(W)`. One can therefore suppose
that `S` is a closed sub-prescheme of `X` defined by a quasi-coherent Ideal `𝒦`. The preceding definitions show that if
`W` is an open of `S` and `t` is a section of `𝒪_X` over `f^{-1}(W)`, `ϖ_n(d_{X/S}^n t|W)` is equal to the canonical
image of `t` in `Γ(W, (𝒪_X/𝒦^{n+1})|W)`. The uniqueness of `ϖ_n` then follows since the image of `𝒪_X` under `d_{X/S}^n`
generates the `𝒪_X`-Module `𝒫_{X/S}^n` `(16.3.8)`.

**Corollary (16.4.12).**

<!-- label: IV.16.4.12 -->

*Let `k` be a field, `X` a `k`-prescheme, `x` a point of `X` rational over `k`. Then `(𝒫_{X/k}^n)_x ⊗_{𝒪_x} k(x)` is
canonically isomorphic (as an augmented `k(x)`-algebra) to `𝒪_x/𝔪_x^{n+1}`.*

It suffices to consider the unique `k`-section `g` of `X` such that `g(Spec(k)) = {x}`.

**Corollary (16.4.13).**

<!-- label: IV.16.4.13 -->

*Let `f : X → S` be a morphism, `s` a point of `S`, `X_s = X ×_S Spec(k(s))` the fibre of `f` at `s`. If `x ∈ X_s` is
rational over `k(s)`, `(𝒫_{X/S}^n)_x ⊗_{𝒪_s} k(s)` is canonically isomorphic to `𝒪_{X_s, x}/𝔪'^{n+1}_x`, where `𝔪'_x` is
the maximal ideal of `𝒪_{X_s, x}`; more precisely, this isomorphism sends `(d^n t)_x ⊗ 1` (where `t` is a section of
`𝒪_X` over an open neighbourhood of `x` in `X`) to the class of `t_x ⊗ 1` modulo `𝔪'^{n+1}_x`.*

This follows from `(16.4.5)` and `(16.4.12)`.

The preceding corollaries justify the terminology "sheaf of principal parts of order `n`".

**Proposition (16.4.14).**

<!-- label: IV.16.4.14 -->

*Let `ρ : A → B` be a ring homomorphism, `S` a multiplicatively stable subset of `B`. Then the canonical homomorphisms*

```text
  (16.4.14.1)    S^{-1} P_{B/A}^n → P_{S^{-1}B/A}^n
```

<!-- original page 23 -->

*deduced from the canonical homomorphisms `P_{B/A}^n → P_{S^{-1}B/A}^n` `(16.4.4)` form a projective system and are
bijective.*

It suffices to remark that `S^{-1}((B ⊗_A B)/𝔍^{n+1}) = S^{-1}(B ⊗_A B)/(S^{-1}𝔍)^{n+1}` by flatness, and that
`S^{-1}(B ⊗_A B) = (S^{-1}B) ⊗_A (S^{-1}B)` `(I, 1.3.4)`.

**Corollary (16.4.15).**

<!-- label: IV.16.4.15 -->

*With the notation of `(16.4.14)`, let `R` be a multiplicative subset of `A` such that `ρ(R) ⊂ S`. Then one has
canonical isomorphisms*

```text
  (16.4.15.1)    S^{-1} P_{B/A}^n ⥲ P_{S^{-1}B/R^{-1}A}^n
```

*forming a projective system.*

It evidently suffices to define canonical isomorphisms

```text
  (16.4.15.2)    P_{S^{-1}B/A}^n ⥲ P_{S^{-1}B/R^{-1}A}^n
```

that is to say, one is reduced to the case where `ρ(R)` is made up of invertible elements of `B`. But then the
isomorphism `(16.4.15.2)` is simply deduced from the canonical isomorphism `B ⊗_A B → B ⊗_{R^{-1}A} B` by passage to the
quotients `(0_I, 1.5.3)`.

**Corollary (16.4.16).**

<!-- label: IV.16.4.16 -->

*Let `f : X → S` be a morphism of preschemes, `x` a point of `X`, `s = f(x)`. Then one has canonical isomorphisms*

```text
  (16.4.16.1)    (𝒫_{X/S}^n)_x ⥲ P_{𝒪_x/𝒪_s}^n
```

*forming a projective system.*

One deduces isomorphisms for the associated graded rings, and in particular a canonical isomorphism

```text
  (16.4.16.2)    (Ω_{X/S}^1)_x ⥲ Ω_{𝒪_x/𝒪_s}^1.
```

**Corollary (16.4.17).**

<!-- label: IV.16.4.17 -->

*Let `k` be a field, `K` the field of rational functions `k(T_1, …, T_r)`. Then, for every integer `n`, the homomorphism
of `K[U_1, …, U_r]` (`U_i` indeterminates) into `P_{K/k}^n` which sends every `U_i` to `d^n T_i - T_i · 1` is surjective
and defines an isomorphism of the quotient `K[U_1, …, U_r]/𝔪^{n+1}` (where `𝔪` is the ideal generated by the `U_i`) onto
`P_{K/k}^n`.*

This follows from `(16.4.8)`, `(16.4.10)` and `(16.4.14)`, where one takes `A = k`, `B = k[T_1, …, T_r]` and
`S = B - {0}`.

One thus recovers the fact that the `dT_i` form a basis of the `K`-vector space `Ω_{K/k}^1` `(0, 20.5.10)`.

**Proposition (16.4.18).**

<!-- label: IV.16.4.18 -->

*Let `f : X → Y`, `g : Y → Z` be two morphisms of preschemes, and consider the canonical homomorphisms of augmented
`𝒪_X`-Algebras `(16.4.3.3)`*

```text
  (16.4.18.1)    g_{X/Y/Z} : 𝒫_{X/Z}^n → 𝒫_{X/Y}^n
```

```text
  (16.4.18.2)    f_{X/Y/Z} : f*(𝒫_{Y/Z}^n) → 𝒫_{X/Z}^n.
```

*Then `g_{X/Y/Z}` is surjective, and its kernel is the Ideal generated by the image under `f_{X/Y/Z}` of the
augmentation ideal of `f*(𝒫_{Y/Z}^n)`.*

<!-- original page 24 -->

Note first that `g_{X/Y/Z}` corresponds to the case in `(16.4.3.3)` where `X' = X`, `S' = Y`, `S = Z`, `u = 1_X`, and
`f_{X/Y/Z}` to the case where one replaces `X'`, `X`, `S`, `S'` by `X`, `Y`, `Z`, `Z` respectively and `u`, `f` by `f`,
`g` respectively.

One has a commutative diagram `(I, 5.3.5)`

```text
  (16.4.18.3)
              X   ──Δ_f──> X ×_Y X  ──j──> X ×_Z X
                ╲             │              │
                f ╲           p              f ×_Z f
                  ↘           ↓              ↓
                              Y  ──Δ_g──>  Y ×_Z Y
```

where `j = (1_X, 1_X)_Z` is an immersion, `j ∘ Δ_f = Δ_{g ∘ f}`, and `p` is the structure morphism. Since one can
restrict to the case where `X`, `Y`, `Z` are affine, one can suppose the immersions `Δ_f`, `Δ_g` and `j` to be closed,
so that `𝒪_X` and `𝒪_{X ×_Y X}` are identified respectively with `𝒪_{X ×_Z X}/𝓘` and `𝒪_{X ×_Z X}/𝓛`, where `𝓛 ⊃ 𝓘` are
two quasi-coherent Ideals corresponding respectively to the immersions `Δ_{g ∘ f}` and `j`. The `𝒪_X`-Algebra
`𝒫_{X/Z}^n` is therefore identified with `𝒪_{X ×_Z X}/𝓘^{n+1}`, and `𝒫_{X/Y}^n` is identified with
`𝒪_{X ×_Y X}/(𝓘/𝓛)^{n+1}`, that is to say with `𝒪_{X ×_Z X}/(𝓘^{n+1} + 𝓛)`, and consequently with the quotient of
`𝒫_{X/Z}^n` by `(𝓘^{n+1} + 𝓛)/𝓘^{n+1}`. But one knows (*loc. cit.*) that `p` and `j` make `X ×_Y X` the product of the
`(Y ×_Z Y)`-preschemes `Y` and `X ×_Z X`, so if `𝒪_Y` is identified with `𝒪_{Y ×_Z Y}/𝒦`, where `𝒦` is the Ideal
corresponding to `Δ_g`, then `𝓛` is equal to `(f ×_Z f)*(𝒦) · 𝒪_{X ×_Z X}` `(I, 4.4.5)`. Since `(𝓘^{n+1} + 𝓛)/𝓘^{n+1}`
is the Ideal of `𝒫_{X/Z}^n` generated by the image of `𝓛`, the proposition follows.

**Corollary (16.4.19).**

<!-- label: IV.16.4.19 -->

*With the notation of `(16.4.18)`, one has an exact sequence of quasi-coherent `𝒪_X`-Modules*

```text
  (16.4.19.1)    f*(Ω_{Y/Z}^1) ──f_{X/Y/Z}──> Ω_{X/Z}^1 ──g_{X/Y/Z}──> Ω_{X/Y}^1 → 0.
```

When `X`, `Y`, `Z` are affine, one thus recovers the exact sequence `(0, 20.5.7.1)`.

**Proposition (16.4.20).**

<!-- label: IV.16.4.20 -->

*Let `f : Y → Z` be a morphism, `j : X → Y` a closed immersion, `𝒦` the quasi-coherent Ideal of `𝒪_Y` corresponding to
`j`. Then one has `𝒫_{X/Y}^n = 𝒪_X = 𝒪_Y/𝒦`, the canonical homomorphism `j_{X/Y/Z} : j*(𝒫_{Y/Z}^n) → 𝒫_{X/Z}^n` is
surjective, and its kernel is the Ideal of `j*(𝒫_{Y/Z}^n)` generated by `j*(𝒪_Y · d_{Y/Z}^n(𝒦))` (note that
`d_{Y/Z}^n(𝒦)` is a subsheaf of abelian groups of `𝒫_{Y/Z}^n`, but is not an `𝒪_Y`-Module in general).*

One knows `(I, 5.3.8)` that the diagonal `Δ_j : X → X ×_Y X` is an isomorphism, whence the first assertion. If `ϖ_1` and
`ϖ_2` are the two homomorphisms of Algebras `𝒪_Y → 𝒫_{Y/Z}^n` corresponding respectively to the two canonical
projections `p_1`, `p_2` of `Y ×_Z Y` onto `Y`, recall that by definition `(16.3.5` and `16.3.6)` `ϖ_1` is the
structural homomorphism of the `𝒪_Y`-Algebra `𝒫_{Y/Z}^n` and `ϖ_2 = d_{Y/Z}^n`. The `𝒪_X`-Algebra `j*(𝒫_{Y/Z}^n)` is
therefore identified with `𝒫_{Y/Z}^n/ϖ_1(𝒦) 𝒫_{Y/Z}^n`, and its quotient by the Ideal generated by `j*(d_{Y/Z}^n(𝒦))`
with `𝒫_{Y/Z}^n/(ϖ_1(𝒦) + ϖ_2(𝒦)) 𝒫_{Y/Z}^n`. Now note that one has a commutative diagram

<!-- original page 25 -->

```text
              Y  <──j──   X
              │           │
              Δ_f         Δ_{f ∘ j}
              ↓           ↓
           Y ×_Z Y <─j ×_Z j── X ×_Z X
```

identifying `X` with the product of the `(Y ×_Z Y)`-preschemes `Y` and `X ×_Z X` `(I, 5.3.7)`. Since `j ×_Z j` is an
immersion, one deduces from this remark and from `(16.2.2)` that if `Δ_{Y/Z}^n` and `Δ_{X/Z}^n` denote the infinitesimal
neighbourhoods of order `n` of `Y` and `X` for the canonical immersions `Δ_f` and `Δ_{f ∘ j}` respectively, one has a
diagram

```text
              Δ_{Y/Z}^n   <───   Δ_{X/Z}^n
                  │                  │
                  ↓                  ↓
               Y ×_Z Y <─j ×_Z j── X ×_Z X
```

making `Δ_{X/Z}^n` the product of the `(Y ×_Z Y)`-preschemes `Δ_{Y/Z}^n` and `X ×_Z X`. One can also say that
`𝒫_{X/Z}^n` is identified with the sheaf of rings `𝒫_{Y/Z}^n ⊗_{𝒪_{Y ×_Z Y}} 𝒪_{X ×_Z X}`. But one sees at once (for
example by reducing to the affine case) that `𝒪_{X ×_Z X} = 𝒪_{Y ×_Z Y}/(p_1*(𝒦) + p_2*(𝒦)) 𝒪_{Y ×_Z Y}`. Therefore
`𝒫_{X/Z}^n` is identified with the quotient of `𝒫_{Y/Z}^n` by the Ideal generated by the image in `𝒫_{Y/Z}^n` of
`p_1*(𝒦) + p_2*(𝒦)`. But by definition this Ideal is also generated by `ϖ_1(𝒦) + ϖ_2(𝒦)`. Q.E.D.

**Corollary (16.4.21).**

<!-- label: IV.16.4.21 -->

*Let `f : Y → Z` be a morphism, `j : X → Y` an immersion. One has an exact sequence of quasi-coherent `𝒪_X`-Modules*

```text
  (16.4.21.1)    𝒩_{X/Y} → j*(Ω_{Y/Z}^1) → Ω_{X/Z}^1 → 0.
```

When `X`, `Y`, `Z` are affine, one thus recovers the exact sequence `(0, 20.5.12.1)`.

**Corollary (16.4.22).**

<!-- label: IV.16.4.22 -->

*If `f : X → S` is a morphism locally of finite presentation, `𝒫_{X/S}^n` and `Ω_{X/S}^1` are quasi-coherent
`𝒪_X`-Modules of finite presentation.*

One is at once reduced to the case where `S = Spec(A)` is affine, `X = Spec(B)`, where `B = A[T_1, …, T_r]/𝔎`, with `𝔎`
an ideal of finite type of `C = A[T_1, …, T_r]`. One then applies `(16.4.20)` with `Z = S`, `Y = Spec(C)` and `𝒦 = 𝔎̃`.
Then `j*(𝒫_{Y/Z}^n)` is a free `𝒪_X`-Module of finite rank `(16.4.10)`, and the hypothesis on `𝔎` implies that
`j*(𝒪_Y · d_{Y/Z}^n(𝒦))` generates a quasi-coherent `𝒪_X`-Module of finite type; whence the conclusion.

**Proposition (16.4.23).**

<!-- label: IV.16.4.23 -->

*Let `X`, `Y` be two `S`-preschemes, `Z = X ×_S Y` their product, `p : X ×_S Y → X` and `q : X ×_S Y → Y` the canonical
projections. Then the canonical homomorphism*

```text
  (16.4.23.1)    p_{Z/X/S} ⊕ q_{Z/Y/S} : p*(Ω_{X/S}^1) ⊕ q*(Ω_{Y/S}^1) → Ω_{(X ×_S Y)/S}^1
```

*is bijective.*

<!-- original page 26 -->

The commutative diagram

```text
              Y  <──q──  X ×_S Y  <──id──  X ×_S Y
              │            │                  │
              g            h                  p
              ↓            ↓                  ↓
              S  <──id──    S    <───f───    X
```

gives a factorisation of the canonical isomorphism `P^n(p)` `(16.4.5)`

```text
  p*(𝒫_{X/S}^n) → 𝒫_{Z/S}^n → 𝒫_{Z/Y}^n
```

and similarly, by interchanging the roles of `X` and `Y`, one has a factorisation of the isomorphism `P^n(q)`

```text
  q*(𝒫_{Y/S}^n) → 𝒫_{Z/S}^n → 𝒫_{Z/X}^n.
```

This proves that the canonical homomorphism `(16.4.18.1)`

```text
  p_{Z/X/S} : p*(𝒫_{X/S}^n) → 𝒫_{Z/S}^n   (resp. q_{Z/Y/S} : q*(𝒫_{Y/S}^n) → 𝒫_{Z/S}^n)
```

is injective, and that the kernel of the canonical surjective homomorphism `(16.4.18.2)`

```text
  𝒫_{Z/S}^n → 𝒫_{Z/Y}^n   (resp. 𝒫_{Z/S}^n → 𝒫_{Z/X}^n)
```

is a complement of the image of `p_{Z/X/S}` (resp. `q_{Z/Y/S}`). On the other hand, this kernel is, by virtue of
`(16.4.18)`, generated by the image under `q_{Z/Y/S}` (resp. `p_{Z/X/S}`) of the augmentation ideal of `q*(𝒫_{Y/S}^n)`
(resp. `p*(𝒫_{X/S}^n)`). One concludes the proposition by considering the case `n = 1`.

One generalizes `(16.4.23)` at once to the case of a product of an arbitrary finite number of `S`-preschemes.

**Remarks (16.4.24).**

<!-- label: IV.16.4.24 -->

(i) We shall see `(17.2.3)` that when the morphism `f : X → Y` in `(16.4.18)` is smooth, the homomorphism `f_{X/Y/Z}` in
`(16.4.19.1)` is locally left invertible and in particular injective. Likewise, when the morphism `f ∘ j : X → Z` of
`(16.4.20)` is smooth, the homomorphism on the left in `(16.4.21.1)` is locally left invertible and *a fortiori*
injective `(17.2.5)`. In Chapter V, we shall also give a variant, in the case of Modules over preschemes, of the
"imperfection modules" studied in `(0, 20.6)`, and of the exact sequences in which they appear.

(ii) Let `X` be a topological space, `𝒜` a sheaf of rings on `X`, and `ℬ` an `𝒜`-Algebra on `X`. Then it is clear that

```text
  U ↦ P_{Γ(U, ℬ)/Γ(U, 𝒜)}^n   (U open in X)
```

is a presheaf of augmented `Γ(U, ℬ)`-algebras, so the associated sheaf `𝒫_{ℬ/𝒜}^n` is an augmented `ℬ`-Algebra. In the
particular case where `X` is a prescheme and `f = (ψ, θ) : X → S` is a morphism of preschemes, it follows easily from
`(16.4.16)` and from the exactness of the functor `lim→` that `𝒫_{X/S}^n` is canonically isomorphic to
`𝒫_{𝒪_X/ψ*(𝒪_S)}^n`. It follows that the formalism developed in the present section could be regarded as a

<!-- original page 27 -->

particular case of a differential formalism for ringed spaces endowed with a sheaf of algebras over the structure sheaf.
We did not, however, wish to start from this point of view, which is less intuitive and less convenient for
applications. It seems, moreover, that, for the various species of "varieties", the "global" construction of the `𝒫^n`
analogous to the one we use here is also better suited to applications.

### 16.5. Relative tangent sheaves and bundles; derivations

**(16.5.1).**

<!-- label: IV.16.5.1 -->

Let `f = (ψ, θ) : X → S` be a morphism of ringed spaces. For every `𝒪_X`-Module `ℱ`, an **`S`-derivation** (or
**`(X/S)`-derivation**, or **`f`-derivation**) **of `𝒪_X` into `ℱ`** is by definition any homomorphism of sheaves of
additive groups `D : 𝒪_X → ℱ` satisfying the following conditions:

a) for every open `V` of `X` and every pair of sections `(t_1, t_2)` of `𝒪_X` over `V`, one has

```text
  (16.5.1.1)    D(t_1 t_2) = t_1 D(t_2) + D(t_1) t_2;
```

b) for every open `V` of `X`, every section `t` of `𝒪_X` over `V`, and every section `s` of `𝒪_S` over an open `U` of
`S` such that `V ⊂ f^{-1}(U)`, one has

```text
  (16.5.1.2)    D((s|V) t) = (s|V) D(t).
```

It is clear that this amounts to saying that for every `x ∈ X`, the homomorphism of additive groups `D_x : 𝒪_x → ℱ_x` is
an `𝒪_{f(x)}`-derivation.

Another interpretation consists in considering the `𝒪_X`-Algebra `𝒟_{𝒪_X}(ℱ)` equal to `𝒪_X ⊕ ℱ`, the algebra structure
being defined by the requirement that for every open `V` of `X`, the product of two sections of `𝒪_X` (resp. of a
section of `𝒪_X` and a section of `ℱ`) over `V` is defined by the ring structure of `Γ(V, 𝒪_X)` (resp. the
`Γ(V, 𝒪_X)`-module structure on `Γ(V, ℱ)`), and the product of two sections of `ℱ` over `V` is taken to be zero. Then
`ℱ` is an Ideal of `𝒟_{𝒪_X}(ℱ)`, kernel of the canonical augmentation `𝒟_{𝒪_X}(ℱ) → 𝒪_X`, and to say that `D` is an
`S`-derivation of `𝒪_X` into `ℱ` means that `1_{𝒪_X} + D` is an `𝒪_S`-homomorphism of Algebras from `𝒪_X` into
`𝒟_{𝒪_X}(ℱ)` which, composed with the augmentation, gives `1_{𝒪_X}`.

The `S`-derivations of `𝒪_X` into `ℱ` obviously form a `Γ(X, 𝒪_X)`-module `Der_S(𝒪_X, ℱ)`.

When `ℱ = 𝒪_X`, an `S`-derivation of `𝒪_X` into itself is simply called an **`S`-derivation of `𝒪_X`**.

**Proposition (16.5.2).**

<!-- label: IV.16.5.2 -->

*Let `A` be a ring, `B` an `A`-algebra, `L` a `B`-module; set `S = Spec(A)`, `X = Spec(B)`, `ℱ = L̃`. Then the map
`D ↦ Γ(D)` which, to every `S`-derivation `D` of `𝒪_X` into `ℱ`, assigns the map `Γ(D) : t ↦ D(t)` of `B` into `L`, is
an isomorphism of `B`-modules from `Der_S(𝒪_X, ℱ)` onto `Der_A(B, L)` (cf. `(0, 20.1.2)`).*

This follows at once from the interpretation given above of `S`-derivations in terms

<!-- original page 28 -->

of homomorphisms of Algebras, from the analogous interpretation given in `(0, 20.1.6)`, and from the canonical
correspondence between homomorphisms of `𝒪_X`-Algebras and homomorphisms of `B`-algebras `(I, 1.3.13` and `1.3.8)`.

**Proposition (16.5.3).**

<!-- label: IV.16.5.3 -->

*Let `f = (ψ, θ) : X → S` be a morphism of preschemes.*

*(i) The differential `d_{X/S} : 𝒪_X → Ω_{X/S}^1` `(16.3.6)` is an `S`-derivation.*

*(ii) For every `𝒪_X`-Module `ℱ`, the map `u ↦ u ∘ d_{X/S}` is an isomorphism of `Γ(X, 𝒪_X)`-modules*

```text
  (16.5.3.1)    Hom_{𝒪_X}(Ω_{X/S}^1, ℱ) ⥲ Der_S(𝒪_X, ℱ).
```

Assertion (i) has already been noted `(16.3.6)`. On the other hand, it is immediate (by virtue of `(0, 20.4.8)`) that
`u ↦ u ∘ d_{X/S}` is injective, by considering the restrictions to a fibre `𝒪_x` of both sides and using `(16.4.16.2)`.
To see that the homomorphism `(16.5.3.1)` is surjective, consider an `S`-derivation `D : 𝒪_X → ℱ`; for every affine open
`V = Spec(B)` of `X` such that `f(V)` is contained in an affine open `U = Spec(A)` of `S`, `D_V : B → Γ(V, ℱ)` is an
`A`-derivation, so there exists a unique `B`-homomorphism `u_V : Ω_{B/A}^1 → Γ(V, ℱ)` such that `D_V = u_V ∘ d_{B/A}`
`(0, 20.4.8)`; furthermore, the uniqueness of `u_V` shows at once that for every affine open `W ⊂ V`, one has
`u_W = u_V|W`, so the `u_V` define a homomorphism of `𝒪_X`-Modules `u : Ω_{X/S}^1 → ℱ` answering the question.

**(16.5.4).**

<!-- label: IV.16.5.4 -->

With the notation of `(16.5.1)`, for every open `U` of `X`, `Der_S(𝒪_U, ℱ|U)` is a `Γ(U, 𝒪_X)`-module, and it is clear
that the map `U ↦ Der_S(𝒪_U, ℱ|U)` is a presheaf; in fact, it is even a sheaf (hence an `𝒪_X`-Module), by virtue of the
pointwise characterization of `S`-derivations seen in `(16.5.1)`. This `𝒪_X`-Module is denoted by `𝒟ℯ𝓇_S(𝒪_X, ℱ)` and is
called the **sheaf of `S`-derivations of `𝒪_X` into `ℱ`**, and what one has just seen is also expressed by the following
corollary:

**Corollary (16.5.5).**

<!-- label: IV.16.5.5 -->

*For every `𝒪_X`-Module `ℱ`, the homomorphism of `𝒪_X`-Modules deduced from `u ↦ u ∘ d_{X/S}`*

```text
  (16.5.5.1)    ℋℴ𝓂_{𝒪_X}(Ω_{X/S}^1, ℱ) → 𝒟ℯ𝓇_S(𝒪_X, ℱ)
```

*is bijective.*

**Corollary (16.5.6).**

<!-- label: IV.16.5.6 -->

*(i) If the morphism `f : X → S` is locally of finite presentation and `ℱ` is a quasi-coherent `𝒪_X`-Module, then
`𝒟ℯ𝓇_S(𝒪_X, ℱ)` is a quasi-coherent `𝒪_X`-Module.*

*(ii) If, in addition, `S` is locally Noetherian and `ℱ` is coherent, then `𝒟ℯ𝓇_S(𝒪_X, ℱ)` is a coherent `𝒪_X`-Module.*

Assertion (i) follows from the isomorphism `(16.5.5.1)`, from `(16.4.22)`, and from `(I, 1.3.12)`; assertion (ii)
follows from `(0_I, 5.3.5)`.

**(16.5.7).**

<!-- label: IV.16.5.7 -->

One sets

```text
  (16.5.7.1)    𝒯_{X/S} = ℋℴ𝓂_{𝒪_X}(Ω_{X/S}^1, 𝒪_X) = 𝒟ℯ𝓇_S(𝒪_X, 𝒪_X)
```

and one says that this is the **sheaf of `S`-derivations of `𝒪_X`**, or also the **tangent sheaf of `X` relative to
`S`**: it is therefore the dual of the `𝒪_X`-Module `Ω_{X/S}^1`. If `f` is locally of finite presentation,

<!-- original page 29 -->

`𝒯_{X/S}` is a quasi-coherent `𝒪_X`-Module; if in addition `S` is locally Noetherian, `𝒯_{X/S}` is coherent `(16.5.6)`.

**(16.5.8).**

<!-- label: IV.16.5.8 -->

Suppose more particularly that `Ω_{X/S}^1` is a locally free `𝒪_X`-Module (of finite rank) (which will be the case when
`f` is smooth `(17.2.3)`); then `𝒯_{X/S}` is a locally free `𝒪_X`-Module, of the same rank as `Ω_{X/S}^1` at each point.
More precisely, suppose that `Ω_{X/S}^1` is of rank `n` at a point `x`; then there are `n` sections `s_i` (`1 ⩽ i ⩽ n`)
of `𝒪_X` over an affine neighbourhood `U` of `x` such that the canonical images of the `ds_i` in
`Ω_{X/S}^1 ⊗_{𝒪_x} k(x)` form a basis of this `k(x)`-vector space; by virtue of Nakayama's lemma, the germs
`(ds_i)_x = d(s_i)_x` of the `ds_i` at the point `x` form a basis of the `𝒪_x`-module `(Ω_{X/S}^1)_x`, so by restricting
`U` one can suppose that the `ds_i` form a basis of the `Γ(U, 𝒪_X)`-module `Γ(U, Ω_{X/S}^1)`. Then the
`Γ(U, 𝒪_X)`-module `Γ(U, 𝒯_{X/S})` is dual to the preceding one; one denotes by `(D_i)_{1 ⩽ i ⩽ n}` or
`(∂/∂s_i)_{1 ⩽ i ⩽ n}` the dual basis of `(ds_i)_{1 ⩽ i ⩽ n}`, so that, by `(16.5.3)`, one has

```text
  (16.5.8.1)    D_i s_j = ⟨D_i, ds_j⟩ = ⟨∂/∂s_i, ds_j⟩ = δ_{ij}   (Kronecker symbol).
```

Every `Γ(S, 𝒪_S)`-derivation of the `Γ(S, 𝒪_S)`-algebra `Γ(U, 𝒪_X)` is therefore written in one and only one way as

```text
  D = ∑_{i=1}^n a_i D_i = ∑_{i=1}^n a_i (∂/∂s_i),
```

where the `a_i` (`1 ⩽ i ⩽ n`) are sections of `𝒪_X` over `U`. For every section `g ∈ Γ(U, 𝒪_X)`, if one sets
`dg = ∑_{i=1}^n c_i ds_i`, one has `c_i = ⟨D_i, dg⟩ = D_i g` by virtue of `(16.5.8.1)`, in other words

```text
  (16.5.8.2)    dg = ∑_{i=1}^n (D_i g) ds_i = ∑_{i=1}^n (∂g/∂s_i) ds_i.
```

**(16.5.9).**

<!-- label: IV.16.5.9 -->

Let `D_1`, `D_2` be two `S`-derivations of `𝒪_X`. For every open `U` of `X`, if `D_1^U`, `D_2^U` are the corresponding
derivations of the ring `Γ(U, 𝒪_X)`, the **bracket**

```text
  [D_1^U, D_2^U] = D_1^U ∘ D_2^U - D_2^U ∘ D_1^U
```

is also a derivation of this ring, so the `ψ*(𝒪_S)`-endomorphism of `𝒪_X`

```text
  (16.5.9.1)    [D_1, D_2] = D_1 ∘ D_2 - D_2 ∘ D_1
```

is again an `S`-derivation; as one checks at once that this bracket satisfies the Jacobi identity, one sees that one has
thus defined on `Der_S(𝒪_X, 𝒪_X)` a `Γ(S, 𝒪_S)`-Lie-algebra structure. Since the definition of this structure commutes
with restriction to an open subset of `X`, one sees that `𝒯_{X/S}` is canonically endowed with a `ψ*(𝒪_S)`-Lie-algebra
structure. Note that the map `(D_1, D_2) ↦ [D_1, D_2]` is *not* `Γ(X, 𝒪_X)`-bilinear.

**(16.5.10).**

<!-- label: IV.16.5.10 -->

For every base change `g : S' → S`, if one sets `X' = X ×_S S'`, one has seen `(16.4.5)` that one has a canonical
isomorphism

```text
  (16.5.10.1)    Ω_{X/S}^1 ⊗_{𝒪_S} 𝒪_{S'} ⥲ Ω_{X'/S'}^1
```

<!-- original page 30 -->

from which one deduces, by virtue of `(16.5.10.1)`, a canonical homomorphism (Bourbaki, *Alg.*, chap. II, 3rd ed., §5,
n° 3)

```text
  (16.5.10.2)    𝒯_{X/S} ⊗_{𝒪_S} 𝒪_{S'} → 𝒯_{X'/S'}
```

which is in general neither injective nor surjective. However:

**Proposition (16.5.11).**

<!-- label: IV.16.5.11 -->

*(i) If `g : S' → S` is a flat morphism and `f` is locally of finite type (resp. locally of finite presentation), the
homomorphism `(16.5.10.2)` is injective (resp. bijective).*

*(ii) If `Ω_{X/S}^1` is a locally free `𝒪_X`-Module of finite type, the homomorphism `(16.5.10.2)` is bijective.*

Indeed, assertion (ii) follows from Bourbaki, *Alg.*, chap. II, 3rd ed., §5, n° 3, prop. 7. Assertion (i) follows
similarly from Bourbaki, *Alg. comm.*, chap. I, §2, n° 10, prop. 11 and from the fact that if `f` is locally of finite
type (resp. locally of finite presentation), `Ω_{X/S}^1` is an `𝒪_X`-Module of finite type (resp. of finite
presentation) (`(16.3.9)` and `(16.4.22)`).

**(16.5.12).**

<!-- label: IV.16.5.12 -->

Since `Ω_{X/S}^1` is a quasi-coherent `𝒪_X`-Module, one can consider the vector bundle over `X` defined by `Ω_{X/S}^1`
`(II, 1.7.8)`

```text
  (16.5.12.1)    T_{X/S} = 𝐕(Ω_{X/S}^1)
```

which is called the **tangent bundle of `X` relative to `S`**. One has therefore a canonical bijection `(II, 1.7.9)`

```text
  Γ(T_{X/S}/S) ⥲ Hom_{𝒪_X}(Ω_{X/S}^1, 𝒪_X) = Γ(X, 𝒯_{X/S})
```

by definition of `𝒯_{X/S}`, and in this isomorphism one can replace `X` by an arbitrary open `U` of `X`; one can
therefore say that the tangent sheaf of `X` relative to `S` is isomorphic to the sheaf of germs of `S`-sections of the
tangent bundle of `X` relative to `S`. If `f : X → Y` is an `S`-morphism, one has seen `(16.4.19)` that one has a
canonical homomorphism `f_{X/Y/S} : f*(Ω_{Y/S}^1) → Ω_{X/S}^1`; this gives, taking into account that

```text
  𝐕(f*(Ω_{Y/S}^1)) = 𝐕(Ω_{Y/S}^1) ×_Y X   (II, 1.7.11),
```

an `X`-morphism `T_{X/S}(f) : T_{X/S} → T_{Y/S} ×_Y X`. If `g : Y → Z` is a second `S`-morphism, one has
`T_{X/S}(g ∘ f) = (T_{Y/S}(g) × 1_X) ∘ T_{X/S}(f)` `(0, 20.5.4.1)`.

It follows from `(16.5.10.1)` and from `(II, 1.7.11)` that for every base change `g : S' → S`, one has a canonical
isomorphism

```text
  (16.5.12.2)    T_{X'/S'} ⥲ T_{X/S} ×_S S' = T_{X/S} ×_X X'.
```

**(16.5.13).**

<!-- label: IV.16.5.13 -->

For every point `x ∈ X`, one calls the **tangent space to `X` at the point `x`** (relative to `S`) the set of points of
the fibre `T_{X/S} ×_X Spec(k(x))` rational over `k(x)`, that is to say the set

```text
  (16.5.13.1)    T_{X/S}(x) = Hom_{k(x)}(Ω_{X/S}^1 ⊗_{𝒪_x} k(x), k(x))
```

which is the dual of the `k(x)`-vector space `Ω_{𝒪_x/𝒪_s}^1/𝔪_x · Ω_{𝒪_x/𝒪_s}^1`. When `Ω_{X/S}^1` is an `𝒪_X`-Module of
finite type, `T_{X/S}(x)` is therefore a vector space of finite rank over `k(x)`, and for every base

<!-- original page 31 -->

change `g : S' → S` and every point `x' ∈ X' = X ×_S S'` over `x`, one has a canonical isomorphism

```text
  (16.5.13.2)    T_{X'/S'}(x') ⥲ T_{X/S}(x) ⊗_{k(x)} k(x').
```

If `x` is rational over `k(s)`, where `s = f(x)` (so that `k(s) → k(x)` is an isomorphism), it follows from `(16.4.13)`
that one has a canonical isomorphism

```text
  (16.5.13.3)    T_{X/S}(x) = T_{X_s/k(s)}(x) = Hom_{k(s)}(𝔪'_x/𝔪'^2_x, k(x))
```

where `𝔪'_x` is the maximal ideal of `𝒪_{X_s, x} = 𝒪_{X, x}/𝔪_s 𝒪_{X, x}`. In the case where `S` is the spectrum of a
field `k`, one thus recovers the Zariski definition of the tangent space at a point `x ∈ X` rational over `k`, as the
dual of `𝔪_x/𝔪_x^2`.

Let `Y` be a second `S`-prescheme and let `g : Y → X` be an `S`-morphism; one has then a canonical homomorphism of
`𝒪_Y`-Modules `(16.4.19)`

```text
  (16.5.13.4)    g_{Y/X/S} : g*(Ω_{X/S}^1) → Ω_{Y/S}^1.
```

Now note that if `y ∈ Y` and `x = g(y)`, one has

```text
  g*(Ω_{X/S}^1) ⊗_{𝒪_Y} k(y) = (Ω_{X/S}^1 ⊗_{𝒪_X} k(x)) ⊗_{k(x)} k(y),
```

and consequently, if `Ω_{X/S}^1` is an `𝒪_X`-Module of finite type, one can identify

```text
  Hom_{k(y)}(g*(Ω_{X/S}^1) ⊗_{𝒪_Y} k(y), k(y))
```

with `T_{X/S}(x) ⊗_{k(x)} k(y)`. One therefore deduces from the homomorphism `(16.5.13.4)` a homomorphism of
`k(y)`-vector spaces

```text
  (16.5.13.5)    T_y(g) : T_{Y/S}(y) → T_{X/S}(x) ⊗_{k(x)} k(y)
```

called the **linear map tangent to `g` at the point `y`**. When `y` is rational over `k(s)`, one can identify `k(s)`,
`k(y)` and `k(x)`, and `T_y(g)` is then a homomorphism of `k(s)`-vector spaces `T_{Y/S}(y) → T_{X/S}(x)`; note moreover
that in this case `g*(Ω_{X/S}^1) ⊗_{𝒪_Y} k(y)` is identified with `Ω_{X/S}^1 ⊗_{𝒪_X} k(x)`, and the preceding
homomorphism is therefore defined without any finiteness condition on `Ω_{X/S}^1`, and is none other than the
homomorphism `T_{Y/S}(g)` `(16.5.12)` restricted to the fibre at the point `y` of `T_{Y/S}`.

**(16.5.14).**

<!-- label: IV.16.5.14 -->

The interpretation of derivations of an `A`-algebra `B` into a `B`-module `L`, given in `(0, 20.1.1)`, translates into
the language of preschemes in the following way.

Consider two morphisms of preschemes `f : X → S`, `g : Y → S`, and a closed sub-prescheme `Y_0` of `Y` defined by a
square-zero Ideal `𝓘` of `𝒪_Y` (so that `Y` and `Y_0` have the same underlying topological space). Suppose given an
`S`-morphism `u_0 : Y_0 → X`, so that one has a commutative diagram

```text
  (16.5.14.1)
              X   <──u_0──   Y_0
              │              │
              f              j
              ↓              ↓
              S   <──g──     Y
```

<!-- original page 32 -->

and we propose to look for `S`-morphisms `u : Y → X` such that `u_0 = u ∘ j` (in other words, whether it is possible to
complete the preceding diagram by the dotted arrow `u` so as to leave it commutative).

For this, consider an affine open `U = Spec(C)` of `Y`; its inverse image `j^{-1}(U)` is the affine open
`U_0 = Spec(C/𝔏)`, where `𝔏 = Γ(U, 𝓘)`, an ideal of square zero in `C`; we shall suppose `U` small enough that
`u_0(U_0)` is contained in an affine open `V = Spec(B)` of `X`, and `g(U) = f(u_0(U_0))` contained in an affine open
`W = Spec(A)` of `S`, so that `B` and `C` are `A`-algebras and `u_0|U_0` corresponds to an `A`-homomorphism `ψ` of `B`
into `C/𝔏`; let `P(U_0)` be the set of restrictions `u|U` of the sought-for homomorphisms, which correspond canonically
to the `A`-homomorphisms of algebras `φ : B → C` such that the composite `B ──φ──> C → C/𝔏` is equal to `ψ`. One knows
therefore `(0, 20.1.1)` that the set of these homomorphisms is empty or of the form `φ_1 + Der_A(B, 𝔏)`; when `P(U_0)`
is not empty, the additive group `Der_A(B, 𝔏)` acts by addition on `P(U_0)`, which is then an **affine space** for the
additive group `Der_A(B, 𝔏)` (or also a **principal homogeneous space** (or **torsor**) under `Der_A(B, 𝔏)`).

Now remark that, since `𝔏` is endowed with a `B`-module structure via `ψ`, one has an isomorphism `v ↦ v ∘ d_{B/A}` from
`Hom_B(Ω_{B/A}^1, 𝔏)` onto `Der_A(B, 𝔏)` `(0, 20.4.8)`. Moreover, as `𝔏` is of square zero, hence a `(C/𝔏)`-module,
every `B`-homomorphism `v : Ω_{B/A}^1 → 𝔏` can be considered as a `(C/𝔏)`-homomorphism `Ω_{B/A}^1 ⊗_B (C/𝔏) → 𝔏`. Since
`𝓘` is of square zero, it can be considered as a quasi-coherent `𝒪_{Y_0}`-Module; introduce the `𝒪_{Y_0}`-Module

```text
  (16.5.14.2)    𝒢 = ℋℴ𝓂(u_0*(Ω_{X/S}^1), 𝓘);
```

it follows then from the fact that `Ω_{B/A}^1 = Γ(V, Ω_{X/S}^1)` `(16.3.7)` that one can write
`Der_A(B, 𝔏) = Γ(U_0, 𝒢)`.

As `P(U_0)` is defined as the set of `S`-morphisms `U → X`, it is clear that `U_0 ↦ P(U_0)` is a *sheaf of sets* `𝒫` on
`Y_0`. We use this fact to prove that the map `h : Γ(U_0, 𝒢) × P(U_0) → P(U_0)` defining the torsor structure on
`P(U_0)` is independent of the choice of `V` and `W`, and in addition that, if `U' ⊂ U` is a second affine open of `Y`
and `U'_0` is its inverse image in `Y_0`, the diagram

```text
  (16.5.14.3)
              Γ(U_0, 𝒢) × P(U_0)   ──h──>   P(U_0)
                   │                          │
                   ↓                          ↓
              Γ(U'_0, 𝒢) × P(U'_0) ──h'──>   P(U'_0)
```

is commutative (the vertical arrows being the restriction operators). By virtue of the preceding remark, one is reduced
to proving the commutativity of the preceding diagram when `h` is defined as above from the affine opens `V`, `W` and
`h'` from affine

<!-- original page 33 -->

opens `V' ⊂ V` and `W' ⊂ W`. But by virtue of the preceding description of `h`, this follows from the commutativity of
the diagram `(0, 20.5.4.2)`.

The maps `Γ(U_0, 𝒢) × P(U_0) → P(U_0)` therefore define a homomorphism of sheaves of sets `m : 𝒢 × 𝒫 → 𝒫` such that, for
every open `U_0` for which `Γ(U_0, 𝒫) ≠ ∅`, `m_{U_0} : Γ(U_0, 𝒢) × Γ(U_0, 𝒫) → Γ(U_0, 𝒫)` is an external law defining on
`Γ(U_0, 𝒫)` a torsor structure under the group `Γ(U_0, 𝒢)`.

**(16.5.15).**

<!-- label: IV.16.5.15 -->

In general, when one is given on a topological space `Z` a sheaf of sets `𝒫`, a sheaf of groups `𝒢` (not necessarily
commutative), and a homomorphism of sheaves of sets `m : 𝒢 × 𝒫 → 𝒫` such that, for every open `U ⊂ Z` with
`Γ(U, 𝒫) ≠ ∅`, `m_U : Γ(U, 𝒢) × Γ(U, 𝒫) → Γ(U, 𝒫)` makes `Γ(U, 𝒫)` a torsor under the group `Γ(U, 𝒢)`, one says that `𝒫`
is a **pseudo-torsor** (or **formally principal homogeneous sheaf**) under the sheaf of groups `𝒢`. One says that `𝒫` is
a **torsor** (or **principal homogeneous sheaf**) under `𝒢` if, in addition, `Γ(U, 𝒫) ≠ ∅` for every non-empty open `U`
in a suitable base of the topology of `Z`.

For the general theory of torsors, we refer to `[42]`; we shall limit ourselves here to recalling the canonical
correspondence between isomorphism classes of these torsors (for a given `𝒢`) and the elements of the cohomology set
`H^1(Z, 𝒢)`. Consider indeed a torsor `𝒫` under `𝒢` and an open cover `(U_λ)` of `Z` such that `Γ(U_λ, 𝒫) ≠ ∅` for every
`λ`; denote by `p_λ` an element of `Γ(U_λ, 𝒫)`. For every pair of indices `λ`, `μ` such that `U_λ ∩ U_μ ≠ ∅`, there
exists then one and only one element `γ_{λμ}` of `Γ(U_λ ∩ U_μ, 𝒢)` such that `γ_{λμ} · (p_μ|U_λ ∩ U_μ) = p_λ|U_λ ∩ U_μ`;
furthermore, if `λ`, `μ`, `ν` are three indices such that `U_λ ∩ U_μ ∩ U_ν ≠ ∅`, the restrictions `γ'_{λμ}`, `γ'_{μν}`,
`γ'_{λν}` of `γ_{λμ}`, `γ_{μν}`, `γ_{λν}` to `U_λ ∩ U_μ ∩ U_ν` satisfy the condition `γ'_{λν} = γ'_{λμ} γ'_{μν}`; in
other words, `(λ, μ) ↦ γ_{λμ}` is a **`1`-cocycle** of the cover `(U_λ)` with values in `𝒢`. If, for every `λ`, `p'_λ`
is a second element of `Γ(U_λ, 𝒫)`, there exists one and only one element `β_λ ∈ Γ(U_λ, 𝒢)` such that
`p'_λ = β_λ · p_λ`, and the `1`-cocycle `(γ'_{λμ})` corresponding to the family `(p'_λ)` is given by
`γ'_{λμ} = β_λ γ_{λμ} β_μ^{-1}`, that is to say, is **cohomologous** to `(γ_{λμ})`. Conversely, the datum of a
`1`-cocycle `(γ_{λμ})` defines, for every pair `(λ, μ)`, an automorphism `θ_{λμ}` of the sheaf of sets `𝒢|U_λ ∩ U_μ`,
namely the right translation by `γ_{λμ}`, and the fact that it is a cocycle shows that one can glue the sheaves of sets
`𝒢|U_λ` by means of the automorphisms `θ_{λμ}` `(0_I, 3.3.1)`; one thus obtains in the obvious way a torsor under `𝒢`,
say `𝒫`, and if one takes for `p_λ` the unit section over `U_λ`, the corresponding `1`-cocycle is none other than the
given `1`-cocycle `(γ_{λμ})`; furthermore, if one replaces `(γ_{λμ})` by a `1`-cocycle `γ'_{λμ} = β_λ γ_{λμ} β_μ^{-1}`
cohomologous to it, one verifies at once that the torsor obtained is isomorphic to `𝒫`.

In particular, if `(γ_{λμ})` is a **`1`-coboundary**, in other words of the form `γ_{λμ} = β_λ β_μ^{-1}`, the torsor `𝒫`
obtained is isomorphic to `𝒢` (considered as a torsor under itself for left translations); one says in this case that
`𝒫` is **trivial**, and the converse is evident.

More particularly, it follows from `(III, 1.3.1)` that one has:

**Proposition (16.5.16).**

<!-- label: IV.16.5.16 -->

*Let `Z` be an affine scheme, `𝒢` a quasi-coherent `𝒪_Z`-Module; then every torsor under `𝒢` is trivial.*

<!-- original page 34 -->

Returning to the problem considered in `(16.5.14)`, one therefore obtains:

**Proposition (16.5.17).**

<!-- label: IV.16.5.17 -->

*Let `X`, `Y` be two `S`-preschemes, `Y_0` a closed sub-prescheme of `Y` defined by a quasi-coherent Ideal `𝓘` of `𝒪_Y`
such that `𝓘^2 = 0`, `j : Y_0 → Y` the canonical injection. Let `u_0 : Y_0 → X` be an `S`-morphism, and `𝒫` the sheaf of
sets on `Y` such that, for every open `U` of `Y`, `Γ(U, 𝒫)` is the set of `S`-morphisms `u : U → X` such that
`u_0|U_0 = u ∘ (j|U_0)`, where `U_0 = j^{-1}(U)`. Then there exists on `𝒫` a structure of pseudo-torsor under the
`𝒪_{Y_0}`-Module `𝒢 = ℋℴ𝓂_{𝒪_{Y_0}}(u_0*(Ω_{X/S}^1), 𝓘)`.*

In particular:

**Corollary (16.5.18).**

<!-- label: IV.16.5.18 -->

*With the notation of `(16.5.17)`, suppose that `Y` is affine and `Ω_{X/S}^1` is of finite presentation; if there exists
an open cover `(U_α)` of `Y` and, for each index `α`, an `S`-morphism `v_α : U_α → X` such that, putting
`U_α^0 = j^{-1}(U_α)`, one has `v_α ∘ (j|U_α^0) = u_0|U_α^0`, then there exists an `S`-morphism `u : Y → X` such that
`u ∘ j = u_0`.*

Indeed, `𝒢` is then a quasi-coherent `𝒪_{Y_0}`-Module `(I, 1.3.12)`; by virtue of `(16.5.16)` and of the fact that `Y_0`
is then affine, the sheaf `𝒫`, which is by hypothesis a torsor under `𝒢`, and not only a pseudo-torsor, is trivial; but
if `w` is an isomorphism from `𝒢` onto `𝒫` (as torsors under `𝒢`), the image under `w` of the zero section of `𝒢` is the
sought-for `S`-morphism `u`.

<!-- original page 34 -->

### 16.6. Sheaves of `Ω`-differentials and exterior differential

**(16.6.1).**

<!-- label: IV.16.6.1 -->

Let `f : X → S` be a morphism of preschemes. We call the *sheaf of `p`-differentials of `X` relative to `S`* (`p` an
integer) the *`p`-th exterior power* `(0_I, 4.1.5)` of the `𝒪_X`-Module `Ω^1_{X/S}`, denoted

```text
  (16.6.1.1)    Ω^p_{X/S} = Λ^p(Ω^1_{X/S}).
```

One thus has `Ω^0_{X/S} = 𝒪_X` and `Ω^p_{X/S} = 0` for `p < 0`; the `Ω^p_{X/S}` are the homogeneous components of the
exterior algebra of `Ω^1_{X/S}`

```text
  (16.6.1.2)    Ω^•_{X/S} = Λ(Ω^1_{X/S}) = ⊕_{p ∈ ℤ} Λ^p(Ω^1_{X/S}),
```

which is therefore a quasi-coherent graded `𝒪_X`-Algebra, anti-commutative, and whose elements of degree `1` are of
square zero. For every affine open set `U` of `X`, one has `Γ(U, Ω^•_{X/S}) = Λ(Γ(U, Ω^1_{X/S}))`, where
`Γ(U, Ω^1_{X/S})` is considered as a `Γ(U, 𝒪_X)`-module.

When `S = Spec(A)` and `X = Spec(B)` are affine, `B` being then an `A`-algebra, one has `(0_I, 4.1.5)`
`Ω^p_{X/S} = (Ω^p_{B/A})^∼`, on setting `Ω^p_{B/A} = Λ^p Ω^1_{B/A}`.

**Theorem (16.6.2).**

<!-- label: IV.16.6.2 -->

*There exists one and only one endomorphism `d` of the sheaf of additive groups `Ω^•_{X/S}` having the following
properties:*

*(i) `d ∘ d = 0`.*

*(ii) For every open set `U` of `X` and every section `f ∈ Γ(U, 𝒪_X)`, one has `df = d_{X/S} f`.*

<!-- original page 35 -->

*(iii) For every open set `U` of `X`, every pair of integers `p, q` and every pair of sections `ω'_p ∈ Γ(U, Ω^p_{X/S})`,
`ω''_q ∈ Γ(U, Ω^q_{X/S})`, one has*

```text
  (16.6.2.1)    d(ω'_p ∧ ω''_q) = (dω'_p) ∧ ω''_q + (−1)^p ω'_p ∧ (dω''_q).
```

*Moreover, `d` is an endomorphism of graded `ψ*(𝒪_S)`-Modules of degree `+1`.*

Suppose the existence of the endomorphism `d` is established. For every affine open set `U` of `X`, every section of
`Ω^p_{X/S}` over `U` is, by virtue of (ii), a linear combination of finitely many elements of the form
`g(df_1 ∧ df_2 ∧ ⋯ ∧ df_p)`, where `g` and the `f_i` are sections of `𝒪_X` over `U` `(0, 20.4.7)`. The conditions (i)
and (iii) then show, by induction on `p`, that one necessarily has

```text
  (16.6.2.2)    d(g(df_1 ∧ df_2 ∧ ⋯ ∧ df_p)) = dg ∧ df_1 ∧ df_2 ∧ ⋯ ∧ df_p.
```

This proves the *uniqueness* of `d` and the last assertion of the theorem. By virtue of this uniqueness property, to
establish the existence of `d` one may restrict to the case where `S = Spec(A)` and `X = Spec(B)` are affine. Now
(Bourbaki, *Alg.*, chap. III, 3rd ed., §10), to define an `A`-antiderivation `D` of degree `+1` of an exterior algebra
`Λ(M)` (where `M` is a `B`-module and `B` an `A`-algebra), this antiderivation taking its values in a graded
anti-commutative `A`-algebra `C = ⊕_{n=0}^∞ C_n` whose elements of degree `1` are of square zero, it suffices to
arbitrarily prescribe an `A`-derivation `D_0` of `B` into `C_1` and an `A`-homomorphism `D_1` of `M` into `C_2`; there
then exists one and only one `A`-antiderivation `D` of `Λ(M)` into `C` coinciding with `D_0` on `B` and with `D_1` on
`M`.

In the present case, `D_0` is necessarily equal to `d_{B/A}` by virtue of (ii); everything comes down to showing, taking
`(16.6.2.2)` into account, that there is an `A`-homomorphism `u` of `Ω^1_{B/A}` into `Ω^2_{B/A}` such that

```text
  (16.6.2.3)    u(g · df) = dg ∧ df
```

for arbitrary `f, g` in `B`; for this it will suffice to show that there exists an `A`-homomorphism
`v : B ⊗_A Ω^1_{B/A} → Ω^2_{B/A}` such that

```text
  (16.6.2.4)    v(g · ω) = dg ∧ ω
```

for `g ∈ B` and `ω ∈ Ω^1_{B/A}`. Finally, since `Ω^1_{B/A} = 𝔍/𝔍²` (where `𝔍 = 𝔍_{B/A}` is the kernel of the canonical
homomorphism `B ⊗_A B → B`) and since `Ω^1_{B/A}` is generated by elements of the form `g · df`, it suffices to define
an `A`-homomorphism `w : B ⊗_A (B ⊗_A B) → Ω^2_{B/A}` such that

```text
  (16.6.2.5)    w(g' ⊗ g ⊗ f) = dg' ∧ (g · df)
```

and such that `w` vanishes on the image of `B ⊗_A 𝔍²`. Now, since the right-hand side of `(16.6.2.5)` is `A`-trilinear
in `g', g, f`, the existence of `w` satisfying `(16.6.2.5)` is immediate. On the other hand, since `𝔍` is generated by
the elements `1 ⊗ x − x ⊗ 1` (`x ∈ B`), one is reduced to verifying that when `z = (1 ⊗ x − x ⊗ 1)(1 ⊗ y − y ⊗ 1)`, one
has `w(g' ⊗ z) = 0`. Now, since `z = 1 ⊗ (xy) + (xy) ⊗ 1 − x ⊗ y − y ⊗ x`, the formula `(16.6.2.4)` shows that it

<!-- original page 36 -->

suffices to see that one has `d(xy) − x · dy − y · dx = 0`, which expresses that `d` is a derivation.

It remains to prove that `d` satisfies condition (i). Now, the square of an antiderivation is a derivation (Bourbaki,
*loc. cit.*), and since `Ω^•_{B/A}` is generated by `Ω^1_{B/A}` as a `B`-algebra, it suffices to verify that `d(dz) = 0`
for `z ∈ B` and for `z ∈ Ω^1_{B/A}`. In the first case, this follows from formula `(16.6.2.3)` with `g = 1`; in the
second, one may restrict to the case where `z = g · df` with `f, g` in `B`, and then, by virtue of `(16.6.2.1)` and
`(16.6.2.3)`, one has

```text
  d(d(g · df)) = d(dg ∧ df) = (d(dg)) ∧ (df) − (dg) ∧ (d(df)) = 0.
```

Q.E.D.

**Definition (16.6.3).**

<!-- label: IV.16.6.3 -->

*The antiderivation `d` defined in `(16.6.2)` (also denoted `d_{X/S}`) is called the **exterior differential** on `X`
(relative to `S`).*

**Proposition (16.6.4).**

<!-- label: IV.16.6.4 -->

*For every base change `g : S' → S`, on setting `X' = X ×_S S'`, the canonical homomorphism*

```text
  (16.6.4.1)    Ω^•_{X/S} ⊗_S S' → Ω^•_{X'/S'}
```

*deduced from the isomorphism `(16.5.9.1)` is bijective. Moreover, if `s` is a section of `Ω^•_{X/S}` over an open set
`U` of `X`, and `s ⊗ 1` its inverse image, a section of `Ω^•_{X'/S'}` over the inverse image `U'` of `U` in `X'`, one
has `d_{X'/S'}(s ⊗ 1) = d_{X/S}(s) ⊗ 1`.*

The first assertion is immediate, since the formation of the exterior algebra of a module commutes with every extension
of the ring of scalars. To prove the second, by virtue of `(16.6.2.2)` one may restrict to the case `s ∈ Γ(U, 𝒪_X)`, and
in that case the assertion has already been proved `(16.4.3.7)`.

**(16.6.5).**

<!-- label: IV.16.6.5 -->

Suppose that `Ω^1_{X/S}` is a locally free `𝒪_X`-Module of rank `n` at a point `x`, so that there exist `n` sections
`s_i ∈ Γ(U, 𝒪_X)` such that the `ds_i` form a basis of the `Γ(U, 𝒪_X)`-module `Γ(U, Ω^1_{X/S})` `(16.5.8)`. Then, for
every integer `p ≥ 1`, the `p`-differentials `ds_{i_1} ∧ ds_{i_2} ∧ ⋯ ∧ ds_{i_p}` (for `i_1 < i_2 < ⋯ < i_p`, elements
of `[1, n]`) form a basis of `binom(n, p)` elements of `Γ(U, Ω^p_{X/S})` over `Γ(U, 𝒪_X)`. Moreover, formula
`(16.6.2.2)` shows that for every section `g ∈ Γ(U, 𝒪_X)`, one has

```text
  (16.6.5.1)    d(g · ds_{i_1} ∧ ds_{i_2} ∧ ⋯ ∧ ds_{i_p})
                  = ∑_k (−1)^r (∂g/∂s_k) ds_{i_1} ∧ ⋯ ∧ ds_{i_r} ∧ ds_k ∧ ds_{i_{r+1}} ∧ ⋯ ∧ ds_{i_p}
```

where, on the right-hand side, `k` ranges over the set of `n − p` indices distinct from the `i_h`, `i_r` being the
largest index `< k`.

One notes that the relation `d(dg) = 0` for every section `g ∈ Γ(U, 𝒪_X)` is expressed in the form

```text
  D_i(D_j g) = D_j(D_i g)    for i ≠ j;
```

in other words, the derivations `D_i` defined in `(16.5.7)` commute pairwise.

### 16.7. The `𝒫^n_{X/S}(ℱ)`

**(16.7.1).**

<!-- label: IV.16.7.1 -->

Let `f : X → S` be a morphism of preschemes and `ℱ` an `𝒪_X`-Module. Let `X^{(n)}_{Δ_f}` denote the *`n`-th
infinitesimal neighbourhood* of `X` for the diagonal morphism

<!-- original page 36 -->

`Δ_f : X → X ×_S X`, let `h_n : X^{(n)}_{Δ_f} → X ×_S X` be the canonical morphism `(16.1.2)`, and consider the two
composite morphisms

```text
  p_1^{(n)} : X^{(n)}_{Δ_f} ──h_n──▶ X ×_S X ──p_1──▶ X,
  p_2^{(n)} : X^{(n)}_{Δ_f} ──h_n──▶ X ×_S X ──p_2──▶ X
```

so that, by definition, `p_1^{(n)}` corresponds to the homomorphism of sheaves of rings `𝒪_X → 𝒫^n_{X/S}` that we have
chosen in order to define the `𝒪_X`-Algebra structure on `𝒫^n_{X/S}` `(16.3.5)`, and `p_2^{(n)}` to the homomorphism of
sheaves of rings `d^n_{X/S} : 𝒪_X → 𝒫^n_{X/S}` `(16.3.6)`. Since `X^{(n)}_{Δ_f}` and `X` have the same underlying space,
one can write

```text
  (16.7.1.1)    𝒫^n_{X/S} = (p_1^{(n)})_* ((p_2^{(n)})*(𝒪_X)).
```

More generally, we shall set

```text
  (16.7.1.2)    𝒫^n_{X/S}(ℱ) = (p_1^{(n)})_* ((p_2^{(n)})*(ℱ))
```

so that `𝒫^n_{X/S} = 𝒫^n_{X/S}(𝒪_X)`; by definition, `𝒫^n_{X/S}(ℱ)` is then an `𝒪_X`-Module.

**(16.7.2).**

<!-- label: IV.16.7.2 -->

Returning to the definitions of inverse images of Modules on ringed spaces `(0_I, 4.3.1)` and taking into account that
`X^{(n)}_{Δ_f}` and `X` have the same underlying space, one sees that one may also write the definition `(16.7.1.2)` in
the form

```text
  (16.7.2.1)    𝒫^n_{X/S}(ℱ) = 𝒫^n_{X/S} ⊗_{𝒪_X} ℱ,
```

but where one must take care that, in the interpretation of the symbol `⊗`, `𝒫^n_{X/S}` is endowed with its `𝒪_X`-Module
structure defined by *the homomorphism of sheaves of rings `d^n_{X/S} : 𝒪_X → 𝒫^n_{X/S}`*. It follows immediately from
this formula (or directly from `(16.7.1.2)`) that `𝒫^n_{X/S}(ℱ)` is canonically endowed with a `𝒫^n_{X/S}`-Module
structure.

**Proposition (16.7.3).**

<!-- label: IV.16.7.3 -->

*(i) The functor `ℱ ↦ 𝒫^n_{X/S}(ℱ)` from the category of `𝒪_X`-Modules to the category of `𝒫^n_{X/S}`-Modules is right
exact and commutes with arbitrary inductive limits; it is exact when `𝒫^n_{X/S}` is a flat `𝒪_X`-Module.*

*(ii) If `ℱ` is a quasi-coherent (resp. finite type, resp. finitely presented) `𝒪_X`-Module, then `𝒫^n_{X/S}(ℱ)` is a
quasi-coherent (resp. finite type, resp. finitely presented) `𝒫^n_{X/S}`-Module.*

The assertions of (i) follow immediately from formula `(16.7.2.1)` together with the symmetry of `𝒫^n_{X/S}` `(16.3.4)`.
The assertions of (ii) follow from the right exactness of the functor `ℱ ↦ 𝒫^n_{X/S}(ℱ)`.

**(16.7.4).**

<!-- label: IV.16.7.4 -->

The two `𝒪_X`-Module structures on `𝒫^n_{X/S}` define on `𝒫^n_{X/S}(ℱ)` two `𝒪_X`-Module structures, which are moreover
permutable, hence an `𝒪_X`-Bimodule structure. It is convenient to denote on the *left* the structure coming from the
structure homomorphism `𝒪_X → 𝒫^n_{X/S}` (chosen in `(16.3.5)`) and on the *right* the one coming from the homomorphism
`d^n_{X/S} : 𝒪_X → 𝒫^n_{X/S}`. In other words, for every open set `U` of `X` and every triple of elements
`a ∈ Γ(U, 𝒪_X)`, `b ∈ Γ(U, 𝒫^n_{X/S})`, `t ∈ Γ(U, ℱ)`, one has by definition

```text
  (16.7.4.1)    a(b ⊗ t) = (ab) ⊗ t,    (b ⊗ t) a = (b · d^n a) ⊗ t = b ⊗ (at) = (d^n a) · (b ⊗ t).
```

The `𝒪_X`-Module structure coming from the definition `(16.7.1.2)` is, with these conventions, the *left* `𝒪_X`-Module
structure.

<!-- original page 38 -->

If `ℱ` is a quasi-coherent `𝒪_X`-Module, the same holds of `𝒫^n_{X/S}(ℱ)` for either of its `𝒪_X`-Module structures. If,
moreover, `ℱ` is of finite type (resp. finitely presented) and `f : X → S` is locally of finite type (resp. locally of
finite presentation), then `𝒫^n_{X/S}(ℱ)` is (for either of its `𝒪_X`-Module structures) of finite type (resp. finitely
presented), as follows from `(16.3.9)` and `(16.4.22)`.

**(16.7.5).**

<!-- label: IV.16.7.5 -->

The definition `(16.7.2.1)` entails the existence of a homomorphism of sheaves of commutative groups

```text
  (16.7.5.1)    d^n_{X/S, ℱ} : ℱ → 𝒫^n_{X/S}(ℱ)    (also written d^n_{X/S})
```

such that, in the notations of `(16.7.4)`, one has

```text
  (16.7.5.2)    d^n_{X/S, ℱ}(t) = 1 ⊗ t
```

and consequently, by virtue of `(16.7.4.1)`,

```text
  (16.7.5.3)    d^n_{X/S, ℱ}(at) = (1 ⊗ t) a = (d^n_{X/S, ℱ}(t)) · a,
```

```text
  (16.7.5.4)    d^n_{X/S, ℱ}(at) = (d^n_{X/S}(a)) · (1 ⊗ t) = (d^n_{X/S}(a)) · (d^n_{X/S, ℱ}(t)).
```

It is therefore `𝒪_X`-linear for the right `𝒪_X`-Module structure on `𝒫^n_{X/S}(ℱ)`, and *semilinear* (relative to the
automorphism `σ` `(16.3.4)`) for the left `𝒪_X`-Module structure.

**Proposition (16.7.6).**

<!-- label: IV.16.7.6 -->

*The right `𝒪_X`-Module `𝒫^n_{X/S}(ℱ)` is generated by the image of `ℱ` under the canonical homomorphism
`d^n_{X/S, ℱ}`.*

This follows immediately from `(16.7.5.3)` and the particular case `ℱ = 𝒪_X` `(16.3.8)`.

**(16.7.7).**

<!-- label: IV.16.7.7 -->

The canonical homomorphisms of sheaves of rings

```text
  φ_{nm} : 𝒫^m_{X/S} → 𝒫^n_{X/S}
```

for `n ≤ m` `(16.1.2)` define, by virtue of `(16.7.2.1)`, canonical homomorphisms

```text
  𝒫^m_{X/S}(ℱ) → 𝒫^n_{X/S}(ℱ)    (n ≤ m)
```

which are homomorphisms of `𝒪_X`-Bimodules by virtue of `(16.1.6)` and `(16.7.4.1)`; moreover, one has commutative
diagrams

```text
            𝒫^m_{X/S}(ℱ) ────▶ 𝒫^n_{X/S}(ℱ)
                ▲                  ▲
       d^m_{X/S, ℱ}       d^n_{X/S, ℱ}
                  ╲              ╱
                       ℱ
```

One thus has a projective system of `𝒪_X`-Bimodules `(𝒫^n_{X/S}(ℱ))`, and one sets

```text
  (16.7.7.1)    𝒫^∞_{X/S}(ℱ) = lim_← 𝒫^n_{X/S}(ℱ).
```

Moreover, the preceding shows that the homomorphisms `(16.7.5.1)` form a projective system of homomorphisms, and
therefore define a canonical homomorphism

```text
  (16.7.7.2)    d^∞_{X/S, ℱ} : ℱ → 𝒫^∞_{X/S}(ℱ).
```

<!-- original page 39 -->

**(16.7.8).**

<!-- label: IV.16.7.8 -->

Let `ℱ, 𝒢` be two `𝒪_X`-Modules; it follows immediately from the definition `(16.7.2.1)` that there is a canonical
isomorphism of `𝒫^n_{X/S}`-Modules

```text
  (16.7.8.1)    𝒫^n_{X/S}(ℱ ⊗_{𝒪_X} 𝒢) ⥲ 𝒫^n_{X/S}(ℱ) ⊗_{𝒫^n_{X/S}} 𝒫^n_{X/S}(𝒢)
```

(Bourbaki, *Alg.*, chap. II, 3rd ed., §5, n° 1, prop. 3).

One concludes in particular (or one sees directly from the definition `(16.7.2.1)`) that if `ℱ` is endowed with an
`𝒪_X`-Algebra structure (not necessarily associative), then `𝒫^n_{X/S}(ℱ)` is canonically endowed with a
`𝒫^n_{X/S}`-Algebra structure; this Algebra is associative (resp. commutative, resp. unital, resp. a Lie Algebra)
whenever `ℱ` is. Furthermore, the canonical homomorphisms `𝒫^m_{X/S}(ℱ) → 𝒫^n_{X/S}(ℱ)` for `n ≤ m` `(16.7.7)` are then
di-homomorphisms of Algebras; similarly, `(16.7.5.1)` is then a homomorphism of `𝒪_X`-Algebras when `𝒫^n_{X/S}(ℱ)` is
endowed with its `𝒪_X`-Algebra structure coming from its right `𝒪_X`-Module structure.

With the same notations, one also has a canonical homomorphism of `𝒫^n_{X/S}`-Modules

```text
  (16.7.8.2)    𝒫^n_{X/S}(ℋom_{𝒪_X}(ℱ, 𝒢)) → ℋom_{𝒫^n_{X/S}}(𝒫^n_{X/S}(ℱ), 𝒫^n_{X/S}(𝒢))
```

(Bourbaki, *Alg.*, chap. II, 3rd ed., §5, n° 3), which is bijective when `ℱ` is a locally free `𝒪_X`-Module of finite
type (*loc. cit.*, prop. 7).

**(16.7.9).**

<!-- label: IV.16.7.9 -->

Suppose one is in the situation described in `(16.4.1)`; then, from the canonical homomorphism `P^n(u)` `(16.4.3.3)`,
one deduces immediately a canonical homomorphism of `𝒪_{X'}`-Bimodules

```text
  (16.7.9.1)    u*(𝒫^n_{X/S}(ℱ)) → 𝒫^n_{X'/S'}(u*(ℱ)).
```

We leave to the reader the task of extending to this homomorphism the properties seen in `(16.4)` for the case
`ℱ = 𝒪_X`.

**Remark (16.7.10).**

<!-- label: IV.16.7.10 -->

The definition of `𝒫^n_{X/S}(ℱ)` in the form `(16.7.1.2)` still makes sense when `ℱ` is an arbitrary sheaf of sets (the
inverse image of a sheaf of sets under `p_2^{(n)}` being defined in `(0_I, 3.7.1)`); a variant of this definition allows
one to define the *"scheme of jets"* (relative to `S`) of an arbitrary `X`-prescheme.

### 16.8. Differential operators[^16.8-gabriel]

**Definition (16.8.1).**

<!-- label: IV.16.8.1 -->

*Let `f = (ψ, θ) : X → S` be a morphism of preschemes, `ℱ`, `𝒢` two `𝒪_X`-Modules, `n` an integer `≥ 0`. We say that a
homomorphism of sheaves of additive groups `D : ℱ → 𝒢` is a **differential operator of order `≤ n`** (relative to `S`)
if there exists a homomorphism of `𝒪_X`-Modules `u : 𝒫^n_{X/S}(ℱ) → 𝒢` (where `𝒫^n_{X/S}(ℱ)` is endowed with its left
`𝒪_X`-Module structure `(16.7.4)`) such that `D = u ∘ d^n_{X/S, ℱ}`.*

It is clear, by virtue of the existence of canonical homomorphisms

```text
  𝒫^m_{X/S}(ℱ) → 𝒫^n_{X/S}(ℱ)
```

<!-- original page 40 -->

for `n ≤ m` `(16.7.7)`, that a differential operator of order `≤ n` is also a differential operator of order `≤ m` for
every `m ≥ n`. If `D : ℱ → 𝒢` is a differential operator of order `≤ n`, then, for every open set `U` of `X`,
`D | U : ℱ | U → 𝒢 | U` is also a differential operator of order `≤ n`.

We say that a homomorphism `D : ℱ → 𝒢` of the sheaves of additive groups underlying `ℱ` and `𝒢` is a *differential
operator* (relative to `S`) if, for every `x ∈ X`, there exist an open neighbourhood `U` of `x` and an integer `n ≥ 0`
such that `D | U : ℱ | U → 𝒢 | U` is a differential operator of order `≤ n`. The *order* of a differential operator
`D : ℱ → 𝒢` is the infimum of integers `n` such that `D` is a differential operator of order `≤ n` (and is therefore
`+∞` if no such integer exists); this order is always finite when `X` is quasi-compact. The differential operators of
order `0` are precisely the homomorphisms of `𝒪_X`-Modules `ℱ → 𝒢`; by convention, every differential operator of order
`< 0` is zero. For `n ≥ 0`, a differential operator is not in general a homomorphism of `𝒪_X`-Modules but is always a
homomorphism of `ψ*(𝒪_S)`-Modules.

When `ℱ = 𝒪_X`, a differential operator of order `≤ 1` from `𝒪_X` to `𝒢` can be written in one and only one way in the
form `v + D`, where `v : 𝒪_X → 𝒢` is an `𝒪_X`-homomorphism and `D` an *`S`-derivation* `(16.5.1)` of `𝒪_X` into `𝒢`:
this follows from the structure of `𝒫^1_{B/A}` `(0, 20.4.8)`.

**(16.8.2).**

<!-- label: IV.16.8.2 -->

In order to describe more explicitly a differential operator of order `≤ n`, `D : ℱ → 𝒢`, it suffices, for every affine
open set `U` of `X` whose image in `S` is contained in an affine open set `V`, to characterize the homomorphism
`D = D_U : Γ(U, ℱ) → Γ(U, 𝒢)`. On setting `Γ(V, 𝒪_S) = A`, `Γ(U, 𝒪_X) = B`, so that `B` is an `A`-algebra, one has
`Γ(U, 𝒫^n_{X/S}(ℱ)) = (B ⊗_A B)/𝔍^{n+1}`, where for brevity one writes `𝔍 = 𝔍_{B/A}`. Set moreover `M = Γ(U, ℱ)`,
`N = Γ(U, 𝒢)`; then the definition of `D` means that, for each pair `(U, V)` satisfying the above conditions, the
`A`-homomorphism `D : M → N` factors as

```text
  M → ((B ⊗_A B)/𝔍^{n+1}) ⊗_B M ──v──▶ N
```

where the first arrow is the canonical homomorphism `t ↦ 1 ⊗ t`, and `v` is a `B`-homomorphism; the `B`-module structure
on `((B ⊗_A B)/𝔍^{n+1}) ⊗_B M` comes from the first factor `B` (whereas we recall that, in the formation of the tensor
product over `B`, the `B`-module structure of `(B ⊗_A B)/𝔍^{n+1}` is given by the second factor `B`). Note now that the
`B`-module `((B ⊗_A B)/𝔍^{n+1}) ⊗_B M` is isomorphic to `(B ⊗_A M)/𝔍^{n+1}(B ⊗_A M)`, where `B ⊗_A M` is considered as a
`(B ⊗_A B)`-module and its `B`-module structure comes from the homomorphism `b ↦ b ⊗ 1` of `B` into `B ⊗_A B`. Let then
`D'` be the `B`-homomorphism of `B ⊗_A M` into `N` such that `D'(b ⊗ t) = b · D(t)`; the factorization condition on `D`
is again expressed by saying that `D'` must vanish on the `B`-module `𝔍^{n+1}(B ⊗_A M)`.

**(16.8.3).**

<!-- label: IV.16.8.3 -->

It is clear that the set of differential operators of order `≤ n` from `ℱ` to `𝒢` is an additive group, denoted
`Diff^n_{X/S}(ℱ, 𝒢)`; when `ℱ = 𝒢 = 𝒪_X`, one also writes `Diff^n_{X/S}` instead of `Diff^n_{X/S}(𝒪_X, 𝒪_X)`.

It has been seen `(16.8.1)` that, for two open sets `U ⊃ V` of `X`, one has a canonical restriction homomorphism

```text
  Diff^n_{U/S}(ℱ | U, 𝒢 | U) → Diff^n_{V/S}(ℱ | V, 𝒢 | V),
```

<!-- original page 41 -->

so that `U ↦ Diff^n_{U/S}(ℱ | U, 𝒢 | U)` is a presheaf of additive groups; in fact it is even a sheaf, since for `U`
ranging over the open sets of `X`, the homomorphisms `u ↦ u ∘ d^n_{X/S, ℱ}` are *isomorphisms* of additive groups

```text
  (16.8.3.1)    Hom_{𝒪_U}(𝒫^n_{U/S}(ℱ | U), 𝒢 | U) ⥲ Diff^n_{U/S}(ℱ | U, 𝒢 | U),
```

by virtue of the fact that the image of `ℱ` under `d^n_{X/S, ℱ}` generates `𝒫^n_{X/S}(ℱ)` `(16.7.6)`. This sheaf is
denoted `𝒟iff^n_{X/S}(ℱ, 𝒢)`, and one therefore has:

**Proposition (16.8.4).**

<!-- label: IV.16.8.4 -->

*The isomorphisms `(16.8.3.1)` define an isomorphism of sheaves of additive groups*

```text
  (16.8.4.1)    ℋom_{𝒪_X}(𝒫^n_{X/S}(ℱ), 𝒢) ⥲ 𝒟iff^n_{X/S}(ℱ, 𝒢).
```

When `ℱ = 𝒢 = 𝒪_X`, one also writes `𝒟iff^n_{X/S}` instead of `𝒟iff^n_{X/S}(𝒪_X, 𝒪_X)`; it follows from `(16.8.4)` that
`𝒟iff^n_{X/S}` is canonically identified with the *dual* of the `𝒪_X`-Module `𝒫^n_{X/S}`; one also writes `⟨t, D⟩`
instead of `u(t)` if `t` is a section of `𝒫^n_{X/S}` over an open set and `u` is the homomorphism from `𝒫^n_{X/S}` to
`𝒪_X` corresponding to `D`.

**(16.8.5).**

<!-- label: IV.16.8.5 -->

Since `𝒫^n_{X/S}(ℱ)` is endowed with an `𝒪_X`-Bimodule structure `(16.7.4)`, one canonically deduces an `𝒪_X`-Bimodule
structure on `ℋom_{𝒪_X}(𝒫^n_{X/S}(ℱ), 𝒢)`, and hence also on `𝒟iff^n_{X/S}(ℱ, 𝒢)` by virtue of `(16.8.4.1)`. More
precisely, to the left `𝒪_X`-Module structure on `𝒫^n_{X/S}(ℱ)` corresponds, by virtue of the definition `(16.8.1)`, the
left `𝒪_X`-Module structure on `𝒟iff^n_{X/S}(ℱ, 𝒢)` explicitly described as follows: for every open set `U` of `X`,
every section `a ∈ Γ(U, 𝒪_X)` and every differential operator `D : ℱ | U → 𝒢 | U`, `aD` is the differential operator
which, to every section `t ∈ Γ(U, ℱ)`, associates the section

```text
  (16.8.5.1)    (aD)(t) = a · D(t)
```

of `Γ(U, 𝒢)`. Similarly, to the right `𝒪_X`-Module structure on `𝒫^n_{X/S}(ℱ)` corresponds the right `𝒪_X`-Module
structure on `𝒟iff^n_{X/S}(ℱ, 𝒢)` explicitly described as follows: with the same notations, `Da` is the differential
operator which, to `t ∈ Γ(U, ℱ)`, associates the section

```text
  (16.8.5.2)    (Da)(t) = D(at).
```

**Proposition (16.8.6).**

<!-- label: IV.16.8.6 -->

*If `f : X → S` is a morphism locally of finite presentation, `ℱ` a quasi-coherent `𝒪_X`-Module of finite presentation,
and `𝒢` a quasi-coherent `𝒪_X`-Module, then `𝒟iff^n_{X/S}(ℱ, 𝒢)` is a quasi-coherent `𝒪_X`-Module for either of the
structures defined in `(16.8.5)`.*

The proposition follows from the fact that, under the hypotheses made, `𝒫^n_{X/S}(ℱ)` is a quasi-coherent `𝒪_X`-Module
of finite presentation `(16.7.4)`, and from `(I, 1.3.12)`.

**(16.8.7).**

<!-- label: IV.16.8.7 -->

The set of differential operators from `ℱ` to `𝒢` (of unspecified order, `(16.8.1)`) is denoted `Diff_{X/S}(ℱ, 𝒢)`; one
sees as in `(16.8.3)` that `U ↦ Diff_{U/S}(ℱ | U, 𝒢 | U)` is a sheaf of additive groups, which we shall denote
`𝒟iff_{X/S}(ℱ, 𝒢)`. It is immediate that `𝒟iff_{X/S}(ℱ, 𝒢)` is the union of the increasing filtered family of its
subsheaves `𝒟iff^n_{X/S}(ℱ, 𝒢)`; if `X` is quasi-compact, `Diff_{X/S}(ℱ, 𝒢)`

<!-- original page 42 -->

is likewise the union of its subgroups `Diff^n_{X/S}(ℱ, 𝒢)` `(16.8.1)`. The `𝒪_X`-Bimodule structures on the
`𝒟iff^n_{X/S}(ℱ, 𝒢)` therefore define an `𝒪_X`-Bimodule structure on `𝒟iff_{X/S}(ℱ, 𝒢)`, again made explicit by
`(16.8.5.1)` and `(16.8.5.2)`.

Note that, for `n ≤ m`, one has a commutative diagram

```text
  (16.8.7.1)
              ℋom_{𝒪_X}(𝒫^n_{X/S}(ℱ), 𝒢) ──~──▶ 𝒟iff^n_{X/S}(ℱ, 𝒢)
                       │                              │
                       ▼                              ▼
              ℋom_{𝒪_X}(𝒫^m_{X/S}(ℱ), 𝒢) ──~──▶ 𝒟iff^m_{X/S}(ℱ, 𝒢)
```

where the horizontal arrows are the isomorphisms `(16.8.4.1)` and the left vertical arrow comes from the canonical
homomorphism `𝒫^m_{X/S}(ℱ) → 𝒫^n_{X/S}(ℱ)` `(16.7.7)`. For every open set `U` of `X`, let us endow
`Γ(U, 𝒫^∞_{X/S}(ℱ)) = lim_← Γ(U, 𝒫^n_{X/S}(ℱ))` with the projective limit topology of the discrete topologies on the
`Γ(U, 𝒫^n_{X/S}(ℱ))`; this defines on `Γ(U, 𝒫^∞_{X/S}(ℱ))` a topological `Γ(U, 𝒪_X)`-bimodule structure, so that
`𝒫^∞_{X/S}(ℱ)` appears as a sheaf with values in the category of topological commutative groups `(0_I, 3.2.6)`. Then
`(G, II, 1.11)` the limit of the inductive system of sheaves of commutative groups `(ℋom_{𝒪_X}(𝒫^n_{X/S}(ℱ), 𝒢))` is
none other than the sheaf of germs of continuous homomorphisms from `𝒫^∞_{X/S}(ℱ)` to `𝒢` (the latter being equipped
with the discrete topology): the continuous homomorphisms from `Γ(U, 𝒫^∞_{X/S}(ℱ))` into the discrete group `Γ(U, 𝒢)`
correspond bijectively to the inductive systems of group homomorphisms `Γ(U, 𝒫^n_{X/S}(ℱ)) → Γ(U, 𝒢)`. One may therefore
restate `(16.8.4)` by saying that there is a canonical isomorphism

```text
  ℋom^{cont}_{𝒪_X}(𝒫^∞_{X/S}(ℱ), 𝒢) ⥲ 𝒟iff_{X/S}(ℱ, 𝒢)
```

where the left-hand member denotes the sheaf of germs of continuous homomorphisms from `𝒫^∞_{X/S}(ℱ)` to `𝒢`.

**Proposition (16.8.8).**

<!-- label: IV.16.8.8 -->

*Let `ℱ`, `𝒢` be two `𝒪_X`-Modules, `D : ℱ → 𝒢` a homomorphism of `ψ*(𝒪_S)`-Modules, `n` an integer `≥ 0`. The following
conditions are equivalent:*

*a) `D` is a differential operator of order `≤ n`.*

*b) For every section `a` of `𝒪_X` over an open set `U`, the homomorphism `D_a : ℱ | U → 𝒢 | U` such that, for every
section `t` of `ℱ` over an open set `V ⊂ U`, one has*

```text
  (16.8.8.1)    D_a(t) = D(at) − a · D(t),
```

*is a differential operator of order `≤ n − 1`.*

*c) For every open set `U` of `X`, every family `(a_i)_{1 ≤ i ≤ n+1}` of `n + 1` sections of `𝒪_X` over `U`, and every
section `t` of `ℱ` over `U`, one has the identity*

```text
  (16.8.8.2)    ∑_{H ⊂ I_{n+1}} (−1)^{Card(H)} (∏_{i ∈ H} a_i) · D((∏_{i ∉ H} a_i) t) = 0
```

*(where `I_{n+1}` denotes the interval `1 ≤ i ≤ n + 1` of `ℕ`).*

<!-- original page 43 -->

Let us first prove the equivalence of a) and c). By definition, in order to prove that `D` is a differential operator of
order `≤ n` it suffices to show that this is so for the restriction `D | U : ℱ | U → 𝒢 | U` to every affine open set `U`
of `X`; on the other hand, property c) holds for every open set `U` of `X` if it holds for every affine open set. One
may therefore restrict to the case where `S = Spec(A)` and `X = Spec(B)` are affine. By virtue of `(16.8.2)` (whose
notations we retain), condition a) means that the `A`-homomorphism `D' : B ⊗_A M → N` such that `D'(b ⊗ t) = b · D(t)`
vanishes on `𝔍^{n+1}(B ⊗_A M)`, which, by virtue of `(0, 20.4.4)`, is equivalent to saying that `D'` vanishes on all
elements of the form

```text
  (∏_{i=1}^{n+1} (a_i ⊗ 1 − 1 ⊗ a_i)) · (1 ⊗ t)
```

where `a_i ∈ B` and `t ∈ M`. Now this element can be written `∑_{H ⊂ I_{n+1}} (∏_{i ∈ H} a_i) ⊗ ((∏_{i ∉ H} a_i) t)`,
and the value of `D'` on this element is exactly the left-hand side of `(16.8.8.2)`, which proves the equivalence of a)
and c).

Let us now prove the equivalence of b) and c). We argue by induction on `n`, the assertion being trivial for `n = 0`.
Writing `a_{n+1}` instead of `a` in condition b), one sees, by the induction hypothesis, that condition b) means that
for every family `(a_i)_{1 ≤ i ≤ n}` of `n` sections of `𝒪_X` over `U` and every section `t` of `ℱ` over `U`,

```text
  ∑_{H' ⊂ I_n} (−1)^{Card(H')} (∏_{i ∈ H'} a_i) · D_{a_{n+1}}((∏_{i ∉ H'} a_i) t) = 0.
```

But if in this relation one replaces `D_{a_{n+1}}` by its definition `(16.8.8.1)`, one immediately sees that one
obtains, up to sign, the left-hand side of `(16.8.8.2)`; whence the conclusion.

**Proposition (16.8.9).**

<!-- label: IV.16.8.9 -->

*If `D : ℱ → 𝒢` is a differential operator of order `≤ n`, and `D' : 𝒢 → ℋ` a differential operator of order `≤ n'`,
then `D' ∘ D : ℱ → ℋ` is a differential operator of order `≤ n + n'`.*

By hypothesis, one may write `D = u ∘ d^n_{X/S, ℱ}` and `D' = v ∘ d^{n'}_{X/S, 𝒢}`, where `u : 𝒫^n_{X/S} ⊗_{𝒪_X} ℱ → 𝒢`
and `v : 𝒫^{n'}_{X/S} ⊗_{𝒪_X} 𝒢 → ℋ` are `𝒪_X`-homomorphisms. Everything comes down to showing that the composite
homomorphism of sheaves of additive groups

```text
  ℱ ──d^n_{X/S, ℱ}──▶ 𝒫^n_{X/S} ⊗_{𝒪_X} ℱ ──u──▶ 𝒢 ──d^{n'}_{X/S, 𝒢}──▶ 𝒫^{n'}_{X/S} ⊗_{𝒪_X} 𝒢
```

factors as

```text
  ℱ ──d^{n+n'}_{X/S, ℱ}──▶ 𝒫^{n+n'}_{X/S} ⊗_{𝒪_X} ℱ ──w──▶ 𝒫^{n'}_{X/S} ⊗_{𝒪_X} 𝒢
```

where `w` is an `𝒪_X`-homomorphism. It will suffice to prove the

**Lemma (16.8.9.1).**

<!-- label: IV.16.8.9.1 -->

*There exists one and only one `𝒪_X`-homomorphism*

```text
  (16.8.9.2)    δ : 𝒫^{n+n'}_{X/S} → 𝒫^{n'}_{X/S}(𝒫^n_{X/S}) = 𝒫^{n'}_{X/S} ⊗_{𝒪_X} 𝒫^n_{X/S}
```

<!-- original page 44 -->

*making the diagram*

```text
  (16.8.9.3)
                          d^{n+n'}_{X/S}
                𝒪_X ──────────────▶ 𝒫^{n+n'}_{X/S}
                  │                     │
            d^n_{X/S}                   δ
                  ▼                     ▼
              𝒫^n_{X/S} ────────▶ 𝒫^{n'}_{X/S}(𝒫^n_{X/S})
                       d^{n'}_{X/S, 𝒫^n_{X/S}}
```

*commute.*

One will then indeed have a commutative diagram deduced from `(16.8.9.3)` by tensoring with `ℱ`

```text
                            d^{n+n'}_{X/S, ℱ}
                  ℱ ──────────────────▶ 𝒫^{n+n'}_{X/S}(ℱ)
                    │                          │
              d^n_{X/S, ℱ}                 δ ⊗ 1
                    ▼                          ▼
                𝒫^n_{X/S}(ℱ) ─────────▶ 𝒫^{n'}_{X/S}(𝒫^n_{X/S}(ℱ))
                              d^{n'}_{X/S, 𝒫^n_{X/S}(ℱ)}
```

and, on the other hand, one verifies immediately from the definition `(16.7.5)` that the diagram

```text
                                   u
                𝒫^n_{X/S}(ℱ) ──────▶ 𝒢
                    │                │
        d^{n'}_{X/S, 𝒫^n_{X/S}(ℱ)}   d^{n'}_{X/S, 𝒢}
                    ▼                ▼
        𝒫^{n'}_{X/S}(𝒫^n_{X/S}(ℱ)) ─1 ⊗ u─▶ 𝒫^{n'}_{X/S}(𝒢)
```

is commutative. One will therefore answer the question by taking `w` to be the composite `𝒪_X`-homomorphism

```text
  𝒫^{n+n'}_{X/S}(ℱ) ──δ ⊗ 1──▶ 𝒫^{n'}_{X/S}(𝒫^n_{X/S}(ℱ)) ──1 ⊗ u──▶ 𝒫^{n'}_{X/S}(𝒢).
```

It remains to prove Lemma `(16.8.9.1)`. Taking `(16.7.6)` into account, which proves the uniqueness of `δ`, one is
reduced to the case where `S = Spec(A)` and `X = Spec(B)` are affine; on setting `𝔍 = 𝔍_{B/A}`, it is a matter of
defining a canonical homomorphism of `B`-modules

```text
  φ : (B ⊗_A B)/𝔍^{n+n'+1} → ((B ⊗_A B)/𝔍^{n'+1}) ⊗_B ((B ⊗_A B)/𝔍^{n+1}),
```

the `B`-module structures on both sides coming from the first factor `B`; let us recall that, in the tensor product of
the right-hand side, `(B ⊗_A B)/𝔍^{n'+1}` is to be considered

<!-- original page 45 -->

as a right `B`-module via its second factor `B`, and `(B ⊗_A B)/𝔍^{n+1}` as a left `B`-module via its first factor `B`
`(16.7.2)`. It amounts to the same to define a homomorphism of `B`-modules

```text
  φ_0 : B ⊗_A B → ((B ⊗_A B)/𝔍^{n'+1}) ⊗_B ((B ⊗_A B)/𝔍^{n+1})
```

and to prove that it vanishes on `𝔍^{n+n'+1}`. Now, such a homomorphism is immediately defined by the condition

```text
  φ_0(b ⊗ b') = π_{n'}(b ⊗ 1) ⊗ π_n(1 ⊗ b')    for b, b' in B
```

with the notations of `(16.3.7)`. Moreover, it is immediate that `φ_0` is a homomorphism of *rings*. Now, one can write

```text
  φ_0(b ⊗ 1 − 1 ⊗ b)
        = π_{n'}(b ⊗ 1 − 1 ⊗ b) ⊗ π_n(1 ⊗ 1)
          + π_{n'}(1 ⊗ b) ⊗ π_n(1 ⊗ 1) − π_{n'}(1 ⊗ 1) ⊗ π_n(1 ⊗ b)
```

and one has

```text
  π_{n'}(1 ⊗ b) ⊗ π_n(1 ⊗ 1) = π_{n'}(1 ⊗ 1) · b ⊗ π_n(1 ⊗ 1)
        = π_{n'}(1 ⊗ 1) ⊗ b · π_n(1 ⊗ 1) = π_{n'}(1 ⊗ 1) ⊗ π_n(b ⊗ 1)
```

whence finally

```text
  (16.8.9.4)    φ_0(b ⊗ 1 − 1 ⊗ b)
                  = π_{n'}(b ⊗ 1 − 1 ⊗ b) ⊗ π_n(1 ⊗ 1) + π_{n'}(1 ⊗ 1) ⊗ π_n(b ⊗ 1 − 1 ⊗ b).
```

A product of `n + n' + 1` terms of the form `(16.8.9.4)` is therefore necessarily zero, since the same is true for a
product of `n + 1` terms of the form `π_n(b ⊗ 1 − 1 ⊗ b)` and a product of `n' + 1` terms of the form
`π_{n'}(b ⊗ 1 − 1 ⊗ b)`. The conclusion thus follows from `(0, 20.4.4)`.

**Corollary (16.8.10).**

<!-- label: IV.16.8.10 -->

*The sheaf `𝒟iff_{X/S}(𝒪_X, 𝒪_X)` (also denoted `𝒟iff_{X/S}`) is canonically endowed with a structure of sheaf of rings,
the `𝒟iff^n_{X/S}` forming an increasing filtration compatible with this structure.*

In particular, `𝒟iff^0_{X/S}` is a sheaf of subrings of `𝒟iff_{X/S}`, canonically identified with `𝒪_X` `(16.8.1)`.
Formulas `(16.8.5.1)` and `(16.8.5.2)` show that the `𝒪_X`-Bimodule structure on `𝒟iff_{X/S}` comes from left and right
multiplication by sections of `𝒪_X` considered as a sheaf of subrings of `𝒟iff_{X/S}`.

**Remarks (16.8.11).**

<!-- label: IV.16.8.11 -->

(i) Suppose that `ℱ = ⊕_{λ ∈ L} ℱ_λ`; then it is clear `(16.7.2.1)` that `𝒫^n_{X/S}(ℱ) = ⊕_{λ ∈ L} 𝒫^n_{X/S}(ℱ_λ)`; as
the functor `ℱ ↦ Γ(U, ℱ)` commutes with the formation of arbitrary direct sums, `d^n_{X/S, ℱ}` is the homomorphism whose
restriction to each `ℱ_λ` is `d^n_{X/S, ℱ_λ} : ℱ_λ → 𝒫^n_{X/S}(ℱ_λ)`; one concludes immediately that one has

```text
  Diff^n_{X/S}(ℱ, 𝒢) = ∏_{λ ∈ L} Diff^n_{X/S}(ℱ_λ, 𝒢),
```

and consequently also `(0_I, 3.2.6)`

```text
  𝒟iff^n_{X/S}(ℱ, 𝒢) = ∏_{λ ∈ L} 𝒟iff^n_{X/S}(ℱ_λ, 𝒢).
```

On the other hand, if `𝒢 = ∏_{μ ∈ M} 𝒢_μ` `(0_I, 3.2.6)`, one has

```text
  Hom_{𝒪_X}(𝒫^n_{X/S}(ℱ), 𝒢) = ∏_{μ ∈ M} Hom_{𝒪_X}(𝒫^n_{X/S}(ℱ), 𝒢_μ),
```

<!-- original page 46 -->

every homomorphism `u` from `𝒫^n_{X/S}(ℱ)` to `𝒢` corresponding bijectively to the family of its composites
`u_μ : 𝒫^n_{X/S}(ℱ) → 𝒢 → 𝒢_μ`. One therefore has

```text
  Diff^n_{X/S}(ℱ, 𝒢) = ∏_{μ ∈ M} Diff^n_{X/S}(ℱ, 𝒢_μ),
```

and consequently also

```text
  𝒟iff^n_{X/S}(ℱ, 𝒢) = ∏_{μ ∈ M} 𝒟iff^n_{X/S}(ℱ, 𝒢_μ).
```

(ii) Up to now, one has hardly encountered differential operators `ℱ → 𝒢` other than when `ℱ` and `𝒢` are locally free
`𝒪_X`-Modules of finite rank, in which case their structure reduces locally, by virtue of (i), to that of the sheaf
`𝒟iff_{X/S}`; the latter will be studied below `(16.11)` in a particular case.

### 16.9. Regular and quasi-regular immersions

**Definition (16.9.1).**

<!-- label: IV.16.9.1 -->

*Let `X` be a ringed space. We say that an Ideal `𝒥` of `𝒪_X` is **regular** (resp. **quasi-regular**) if, for every
point `x ∈ Supp(𝒪_X/𝒥)`, there exist an open neighbourhood `U` of `x` in `X` and a regular sequence `(0, 15.2.2)` (resp.
quasi-regular sequence `(0, 15.2.2)`) of elements of `Γ(U, 𝒪_X)` generating `𝒥 | U`.*

We say that a regular (resp. quasi-regular) sequence of sections of `𝒪_X` over `U` generating `𝒥 | U` is a *regular
system* (resp. *quasi-regular system*) of generators of `𝒥 | U`.

**Definition (16.9.2).**

<!-- label: IV.16.9.2 -->

*Let `j : Y → X` be an immersion of preschemes and let `U` be an open set of `X` such that `j(Y) ⊂ U` and `j` is a
closed immersion of `Y` into `U`. We say that `j` is **regular** (resp. **quasi-regular**) if the closed sub-prescheme
`j(Y)` of `U` associated to `j` is defined by a regular (resp. quasi-regular) Ideal of `𝒪_U` (a condition independent of
the chosen open set `U`).*

We say that a sub-prescheme `Y` of a prescheme `X` is *regularly immersed* (resp. *quasi-regularly immersed*) if the
canonical injection `j : Y → X` is a regular (resp. quasi-regular) immersion. If `Y` is a closed sub-prescheme of `X`
and `𝒥` is the Ideal of `𝒪_X` defining `Y`, this amounts to saying that `𝒥` is regular (resp. quasi-regular).

For example, if `A` is an *integral* ring and `f` is a nonzero element of `A`, the closed sub-prescheme `V(f)` of
`Spec(A)` (isomorphic to `Spec(A/fA)`) is *regularly immersed* in `Spec(A)`.

Every regular Ideal is quasi-regular `(0, 15.2.2)`; every regular immersion is quasi-regular (cf. `(16.9.11)` for a
partial converse).

**Proposition (16.9.3).**

<!-- label: IV.16.9.3 -->

*Let `X` be a ringed space, `𝒥` an Ideal of `𝒪_X`, `(f_i)_{1 ≤ i ≤ n}` a finite sequence of sections of `𝒪_X` over `X`
generating `𝒥`. For `(f_i)` to be a quasi-regular sequence `(0, 15.2.2)`, it is necessary and sufficient that the
following conditions hold:*

*(i) The canonical images of the `f_i` in `𝒥/𝒥²` form a basis of this `𝒪_X/𝒥`-Module.*

*(ii) The canonical surjective homomorphism `(16.1.2.2)`*

```text
  𝕊^•_{𝒪_X/𝒥}(𝒥/𝒥²) → gr^•_𝒥(𝒪_X)
```

*is bijective.*

*Moreover, if this is so, every sequence `(f'_i)_{1 ≤ i ≤ n}` of `n` sections of `𝒥` over `X` which generates `𝒥` is
quasi-regular.*

<!-- original page 47 -->

The two conditions of the statement merely translate the definition given in `(0, 15.2.2)`, taking into account the
definition of the canonical homomorphisms `(0, 15.2.1.1)`. The last assertion follows from the fact that if a module `M`
over a commutative ring `A` admits a basis of `n` elements, then every system of `n` generators of `M` is a basis of `M`
(Bourbaki, *Alg. comm.*, chap. II, §3, cor. 5 of th. 1).

**Corollary (16.9.4).**

<!-- label: IV.16.9.4 -->

*Let `X` be a locally ringed space, `𝒥` an Ideal of `𝒪_X`. For `𝒥` to be quasi-regular, it is necessary and sufficient
that the following conditions hold:*

*(i) `𝒥` is of finite type.*

*(ii) `𝒥/𝒥²` is a locally free `(𝒪_X/𝒥)`-Module.*

*(iii) The canonical homomorphism*

```text
  (16.9.4.1)    𝕊^•_{𝒪_X/𝒥}(𝒥/𝒥²) → gr^•_𝒥(𝒪_X)
```

*is bijective.*

The necessity of the conditions follows immediately from `(16.9.3)`. To see that the conditions are sufficient, it
suffices, by virtue of `(16.9.3)`, to show that if, at a point `x ∈ Supp(𝒪_X/𝒥)`, there exist an open neighbourhood `U`
of `x` in `X` and `n` sections `f_i` (`1 ≤ i ≤ n`) of `𝒥` over `U` whose canonical images in `𝒥/𝒥²` form a basis of
`(𝒥/𝒥²) | U` over `(𝒪_X/𝒥) | U`, then there exists an open neighbourhood `V ⊂ U` of `x` such that the `f_i | V` generate
`𝒥 | V`. Now, by hypothesis, `𝒥_x ≠ 𝒪_x`, so that `𝒥_x` is contained in the maximal ideal of `𝒪_x`; since `𝒥_x` is an
`𝒪_x`-module of finite type and the classes of the `(f_i)_x` in `𝒥_x/𝒥_x²` generate this `(𝒪_x/𝒥_x)`-module, Nakayama's
lemma shows that the `(f_i)_x` generate `𝒥_x`. Since `𝒥` is of finite type, one concludes by `(0_I, 5.2.2)`.

**Corollary (16.9.5).**

<!-- label: IV.16.9.5 -->

*Let `X` be a locally ringed space, `𝒥` a quasi-regular Ideal of `𝒪_X`, `(f_i)_{1 ≤ i ≤ n}` a sequence of sections of
`𝒥` over `X`, `x` a point of `Supp(𝒪_X/𝒥)`. The following conditions are equivalent:*

*a) There exists an open neighbourhood `U` of `x` in `X` such that the `f_i | U` form a quasi-regular sequence of
elements of `Γ(U, 𝒪_X)` generating `𝒥 | U`.*

*b) The `(f_i)_x` form a system of generators of `𝒥_x` of smallest possible cardinality.*

*b') The `(f_i)_x` form a minimal system of generators of `𝒥_x`.*

*c) If `f̄_i` is the canonical image of `f_i` in `Γ(X, 𝒥/𝒥²)`, the `(f̄_i)_x` form a basis of the `(𝒪_x/𝒥_x)`-module
`𝒥_x/𝒥_x²`.*

By hypothesis, `𝒪_x` is a local ring and `𝒥_x` is an ideal of finite type of `𝒪_x` contained in the maximal ideal of
`𝒪_x`; the equivalence of b), b') and c) thus follows from Nakayama's lemma (Bourbaki, *Alg. comm.*, chap. II, §3, n° 2,
prop. 5). It is clear that a) implies c) by virtue of `(16.9.3)`; on the other hand, it follows from `(0_I, 5.2.2)`
that, if condition c) is verified (hence also b)), there exists an open neighbourhood `U` of `x` in `X` such that
`(𝒥/𝒥²) | U` has constant rank `n`, and such that the `f_i | U` generate `𝒥 | U`; it suffices then to apply, in `U`, the
last assertion of `(16.9.3)`.

**Remarks (16.9.6).**

<!-- label: IV.16.9.6 -->

(i) Under the general hypotheses of `(16.9.5)`, it is not enough that the `(f̄_i)_y` form a basis of the
`(𝒪_y/𝒥_y)`-module `𝒥_y/𝒥_y²` for every `y ∈ X` for the sequence `(f_i)` to generate `𝒥`. One has an example by

<!-- original page 48 -->

taking `X = Spec(A)`, where `A` is a Dedekind ring, and `𝒥 = 𝔍̃`, where `𝔍` is a *non-principal* prime ideal of `A`;
then `𝒥_y/𝒥_y² = 0` at every point `y` distinct from the point `x ∈ X` corresponding to `𝔍`, and `𝒥_x/𝒥_x²` has rank `1`
over the field `𝒪_x/𝒥_x`; moreover, `𝒥` is clearly a regular Ideal.

(ii) In `(16.9.5)`, one cannot replace "quasi-regular" by "regular", even when `X` is a prescheme (cf. `(16.9.12)`).
Indeed, let `B` denote the ring of germs of infinitely differentiable functions at the point `0` of `ℝ`; it has a
maximal ideal `𝔪` generated by the germ `t` of the identity map of `ℝ` at the point `0`, and the intersection `𝔫` of the
`𝔪^k` for `k > 0` is not reduced to `0`. Now let `A` be the quotient ring `B[T]/𝔫 T B[T]`, and let `f_1, f_2` be the
canonical images in `A` of the elements `t` and `T` of `B[T]`. The sequence `(f_1, f_2)` is *regular* in `A`: indeed,
`f_1` is not a zero-divisor in `A`, since the relation `t P[T] ∈ 𝔫 T B[T]`, for a polynomial `P ∈ B[T]`, entails that
the products of `t` by the coefficients of `P` belong to the ideal `𝔫`, and it follows immediately that these
coefficients are themselves in `𝔫`, hence `P[T] ∈ 𝔫 T B[T]`. As `B/tB` is isomorphic to `ℝ`, `A/f_1 A` is isomorphic to
the polynomial ring `ℝ[T]`, hence integral, and the image of `f_2` in `A/f_1 A`, being equal to `T`, is not a
zero-divisor, which proves our assertion. However, `f_2` is a zero-divisor in `A`, for, given any non-zero element
`x ∈ 𝔫`, the image of `x` in `A` is `≠ 0`, but the image of `xT` is zero. One concludes that the sequence `(f_2, f_1)`
is *not regular* in `A`; on the other hand, the ideal `𝔍 = f_1 A + f_2 A` is distinct from `A`, so conditions b), b')
and c) of `(16.9.5)` do not imply condition a) when one replaces "quasi-regular" by "regular".

**(16.9.7).**

<!-- label: IV.16.9.7 -->

If `X = Spec(A)` is an affine scheme, we shall say that an ideal `𝔍` of `A` is *regular* (resp. *quasi-regular*) if the
Ideal `𝒥 = 𝔍̃` of `𝒪_X` is regular (resp. quasi-regular); note that this notion is *local* and does not in any way imply
the existence of a system of generators of `𝔍` forming in `A` a regular (resp. quasi-regular) sequence, as the example
`(16.9.6, (i))` shows; however, this does hold when `A` is local `(16.9.5)`.

Proposition `(16.9.4)` is translated in terms of quasi-regular immersions as follows:

**Proposition (16.9.8).**

<!-- label: IV.16.9.8 -->

*Let `j : Y → X` be a morphism of preschemes; for `j` to be a quasi-regular immersion, it is necessary and sufficient
that `j` satisfy the following conditions:*

*(i) `j` is an immersion locally of finite presentation.*

*(ii) The conormal sheaf `gr^1(j) = 𝒩_{Y/X}` `(16.1.2)` is a locally free `𝒪_Y`-Module.*

*(iii) The canonical homomorphism `(16.1.2.2)`*

```text
  𝕊^•_{𝒪_Y}(gr^1(j)) → gr^•(j)
```

*is bijective.*

The question being local on `Y`, one may restrict to the case where `j` is the canonical injection of a closed
sub-prescheme `Y` of `X`, in which case the translation of `(16.9.4)` into `(16.9.8)` results from the description of
`gr^1(j)` and `gr^•(j)` in terms of the Ideal `𝒥` of `𝒪_X` defining the sub-prescheme `Y` `(16.1.3, (ii))`.

**Corollary (16.9.9).**

<!-- label: IV.16.9.9 -->

*Let `Y` be a prescheme, `X` a `Y`-prescheme, `j : Y → X` a `Y`-section of `X`, so that the `n`-th normal invariant
`𝒜^{(n)}` of `j` `(16.1.2)` is an augmented `𝒪_Y`-Algebra `(16.1.7)`; set `𝒜^{(∞)} = lim_← 𝒜^{(n)}`. For `j` to be a
quasi-regular immersion, it is necessary and sufficient that `j` be locally of finite presentation and that every
`y ∈ Y` admit an affine open neighbourhood `U` of ring `C` such that `𝒜^{(∞)} | U` is isomorphic, as an augmented
topological `𝒪_U`-Algebra, to `𝒪_U[[T_1, …, T_n]]`.*

One may restrict to the case where `j` is a closed immersion by passing to a sufficiently small neighbourhood of `y`
(see the argument of `(16.4.11)`), and then `𝒪_Y` is identified with a quotient Algebra `𝒪_X/𝒥` and the canonical
surjective homomorphism `𝒪_X → 𝒪_Y` admits a

<!-- original page 49 -->

right inverse `(16.1.7)`. One may therefore suppose `X = Spec(B)` and `Y = Spec(A)` affine, `B` being an augmented
`A`-algebra and the augmentation ideal `𝔍` being of finite type. Since `𝒜^{(n)}` is then identified with
`(B/𝔍^{n+1})^∼`, the corollary follows from the equivalence of b) and c) in `(0, 19.5.4)`, since `B/𝔍 = A`.

One notes that, in the affine case considered, the fact that `j` is a quasi-regular immersion is moreover equivalent, by
virtue of `(0, 19.5.4)`, to the statement that `B` is a *formally smooth* `A`-algebra for the `𝔍`-preadic topology.

One also notes that the condition that `j` be an immersion locally of finite presentation is always satisfied when the
morphism `X → Y` is locally of finite type `(IV, 1.4.3, (v))`.

**Proposition (16.9.10).**

<!-- label: IV.16.9.10 -->

*Let `X` be a locally Noetherian prescheme, `Y` a sub-prescheme of `X`, `j : Y → X` the canonical injection, `y` a point
of `Y`.*

*(i) For there to exist an open neighbourhood `U` of `y` in `X` such that the restriction `Y ∩ U → U` of `j` is a
regular immersion, it is necessary and sufficient that the kernel `𝒥_y` of the surjective homomorphism
`𝒪_{X, y} → 𝒪_{Y, y}` be generated by a regular sequence of elements of `𝒪_{X, y}`.*

*(ii) For the immersion `j` to be regular, it is necessary and sufficient that it be quasi-regular.*

(i) One may restrict to the case where `Y` is a closed sub-prescheme of `X` defined by a coherent Ideal `𝒥` of `𝒪_X`.
The condition is obviously necessary. Conversely, if `𝒥_y` is generated by a regular sequence `(s_i)_y`, where the `s_i`
are sections of `𝒥` over an open neighbourhood `U` of `y` in `X`, one may suppose that the `s_i` generate `𝒥 | U`
`(0_I, 5.2.2)` and form a regular sequence `(0, 15.2.4)`, whence the assertion.

(ii) The fact that a quasi-regular immersion is regular follows from (i) and from the identification of quasi-regular
sequences and regular sequences in `𝒪_{X, y}` consisting of elements of the maximal ideal `(0, 15.1.11)`.

When (without Noetherian hypothesis on `X`) the kernel `𝒥` of `𝒪_X → 𝒪_Y` is generated by a regular sequence of elements
of `𝒪_X`, one says that the immersion `j` is *regular at the point `y`*.

**Corollary (16.9.11).**

<!-- label: IV.16.9.11 -->

*Let `X` be a locally Noetherian prescheme; then every quasi-regular Ideal of `𝒪_X` is regular.*

**Remarks (16.9.12).**

<!-- label: IV.16.9.12 -->

(i) One notes that a regular immersion is not in general a flat morphism, nor *a fortiori* a regular morphism in the
sense of `(IV, 6.8.1)`.

(ii) Let `A` be a local Noetherian ring; it follows immediately from `(16.9.4)` and from `(0, 17.1.1)` that for `A` to
be *regular*, it is necessary and sufficient that its maximal ideal `𝔪` be *quasi-regular* (or regular, which amounts to
the same since `A` is Noetherian). For a Noetherian affine scheme `X` to be *regular*, it is necessary and sufficient
that, for every closed point `x ∈ X`, the canonical injection `Spec(κ(x)) → X` be a *regular* immersion.

**Proposition (16.9.13).**

<!-- label: IV.16.9.13 -->

*Let `X` be a locally Noetherian prescheme, `Y` a sub-prescheme of `X`, `Y'` a sub-prescheme of `Y` such that the
canonical injection `j : Y' → Y` is regular. Then the sequence of `𝒪_{Y'}`-Modules*

```text
  (16.9.13.1)    0 → j*(𝒩_{Y/X}) → 𝒩_{Y'/X} → 𝒩_{Y'/Y} → 0
```

<!-- original page 50 -->

*is exact; moreover, for every `x ∈ X`, there exists an open neighbourhood `U` of `x` such that the restrictions to `U`
of the homomorphisms in `(16.9.13.1)` form an exact and split sequence.*

Let us first prove the following lemma:

**Lemma (16.9.13.2).**

<!-- label: IV.16.9.13.2 -->

*Let `A` be a ring, `𝔍` an ideal of `A`, `A' = A/𝔍`, `(f_i)_{1 ≤ i ≤ r}` a sequence of elements of `A` which is
`A'`-regular, `𝔎 = ∑_i f_i A`, `𝔏 = 𝔍 + 𝔎`, `𝔎' = ∑_i f'_i A'` (where `f'_i` is the image of `f_i` in `A'`), so that
`C = A/𝔏` is isomorphic to `A'/𝔎'`. Then for every integer `n > 0` and every integer `N ≥ n`, one has the relation*

```text
  (16.9.13.3)    𝔍 ∩ 𝔎^n = 𝔍 𝔎^n + 𝔍 𝔎^N.
```

It clearly suffices to prove that every element of the left-hand side is contained in the right-hand side, and by
induction on `n` one is reduced to the case `N = n + 1`. An element of the left-hand side of `(16.9.13.3)`, being in
`𝔎^n`, is written `P(f_1, …, f_r)`, where `P ∈ A[T_1, …, T_r]` is homogeneous of degree `n`. If `f'_i` is the canonical
image of `f_i` in `A'`, the hypothesis `P(f_1, …, f_r) ∈ 𝔍` means that `P(f'_1, …, f'_r) = 0`. But
`P(f'_1, …, f'_r) ∈ 𝔎'^n`, so the canonical image of `P(f'_1, …, f'_r)` in `𝔎'^n/𝔎'^{n+1}` is zero. Now the hypothesis
that the sequence `(f'_i)` is `A'`-regular implies that the canonical homomorphism `𝕊^n_C(𝔎'/𝔎'^2) → 𝔎'^n/𝔎'^{n+1}` is
bijective `(0, 15.1.9)`; one concludes that the coefficients of `P` belong to `𝔏 = 𝔍 + 𝔎`. It follows immediately that
`P(f_1, …, f_r) ∈ 𝔍 𝔎^n + 𝔎^{n+1}`, and since `P(f_1, …, f_r) ∈ 𝔍`, one finally has
`P(f_1, …, f_r) ∈ 𝔍 𝔎^n + 𝔍 𝔎^{n+1}`, which proves the lemma.

Taking the quotient of the two sides of `(16.9.13.3)` by `𝔍 𝔎^n`, one sees that the relations `(16.9.13.3)` for `N ≥ n`
entail

```text
  (16.9.13.4)    (𝔍 ∩ 𝔎^n)/𝔍 𝔎^n ⊂ ⋂_{N ≥ n} 𝔎^N · (A/(𝔍 𝔎^n)).
```

One deduces the

**Corollary (16.9.13.5).**

<!-- label: IV.16.9.13.5 -->

*Suppose the hypotheses of `(16.9.13.2)` are verified and, moreover, that the ring `A` is Noetherian and that `𝔎` is
contained in the radical of `A`. Then for every integer `n > 0`,*

```text
  (16.9.13.6)    𝔍 ∩ 𝔎^n = 𝔍 𝔎^n.
```

Indeed, the right-hand side of `(16.9.13.4)` is then zero, since `A/𝔍 𝔎^n` is an `A`-module of finite type (Bourbaki,
*Alg. comm.*, chap. III, §3, n° 3, prop. 6).

Taking in particular `n = 2` in `(16.9.13.6)`, and noting that one has `𝔏² = 𝔍² + 𝔍𝔎 + 𝔎² = 𝔍𝔏 + 𝔎²`; since `𝔍𝔏 ⊂ 𝔏²`,
one deduces

```text
  𝔍 ∩ 𝔏² = 𝔍𝔏 + (𝔍 ∩ 𝔎²) = 𝔍𝔏 + 𝔍 𝔎² = 𝔍𝔏,
```

in other words

```text
  (16.9.13.7)    𝔍 ∩ 𝔏² = 𝔍𝔏,
```

which can also be expressed by saying that the canonical homomorphism

```text
  𝔍/𝔍𝔏 → (𝔍 + 𝔎²)/𝔎²
```

is bijective.

These lemmas being established, let us prove the first assertion of `(16.9.13)`: it clearly suffices

<!-- original page 51 -->

to prove that the sequence of stalks of the sheaves appearing in `(16.9.13.1)`, at a point `x ∈ Y'`, is exact. Now, on
setting `A = 𝒪_{X, x}`, one can write `𝒪_{Y, x} = A' = A/𝔍`, where `𝔍` is an ideal contained in the maximal ideal of
`A`, then `𝒪_{Y', x} = A'/𝔎'`, where `𝔎'` is generated by an `A'`-regular sequence of elements of `A'`, themselves
images of elements of an `A'`-regular sequence of elements of `A` belonging to the maximal ideal of `A`. If `𝔎` is the
ideal generated by the latter and `𝔏 = 𝔍 + 𝔎`, one has `𝒪_{Y', x} = A/𝔏`, and since one is in the situation of
`(16.9.13.5)`, the canonical homomorphism `𝔍/𝔍𝔏 → (𝔍 + 𝔎²)/𝔎²` is bijective. But this shows that the sequence

```text
  0 → 𝔍/𝔍𝔏 → 𝔏/𝔏² → (𝔏/𝔍)/(𝔏/𝔍)² → 0
```

is exact (see the proof of `(16.2.7)`), and the modules figuring in this sequence are precisely the stalks at `x` of the
sheaves in `(16.9.13.1)`. The second assertion follows from the fact that `𝒩_{Y'/Y}` is a locally free `𝒪_{Y'}`-Module
`(16.9.8)` and from Bourbaki, *Alg.*, chap. II, 3rd ed., §1, n° 11, prop. 21.

### 16.10. Differentially smooth morphisms

**Definition (16.10.1).**

<!-- label: IV.16.10.1 -->

*We say that a morphism of preschemes `f : X → S` is **differentially smooth** (or that `X` is **differentially smooth**
over `S`) if it satisfies the following conditions:*

*(i) `Ω^1_{X/S}` is a locally projective `𝒪_X`-Module, that is, every point of `X` admits an affine open neighbourhood
`U` such that `Γ(U, Ω^1_{X/S})` is a projective `Γ(U, 𝒪_X)`-module (not necessarily of finite type).*

*(ii) The canonical homomorphism `(16.3.1.1)`*

```text
  𝕊^•_{𝒪_X}(Ω^1_{X/S}) → gr^•(𝒫_{X/S})
```

*is bijective.*

*In particular, if `Ω^1_{X/S}` is locally free of finite rank, the `𝒫^n_{X/S}` are locally free `𝒪_X`-Modules of finite
rank (being extensions of such Modules).*

We say that `f` is *differentially smooth at a point `x ∈ X`* (or that `X` is differentially smooth over `S` at the
point `x`) if there exists an open neighbourhood `U` of `x` in `X` such that `f | U` is differentially smooth.

We shall see later `(17.12.4)` that a smooth morphism is differentially smooth, which justifies the terminology; but the
converse is not true. Indeed, a *monomorphism* `f : X → S` is differentially smooth, since `Ω^1_{X/S} = 0` by virtue of
`(I, 5.3.8)`, and consequently the surjective homomorphism `(16.3.1.1)` is clearly bijective; yet a monomorphism is not
even necessarily flat, hence *a fortiori* not necessarily smooth. Let us limit ourselves to noting the following
proposition:

**Proposition (16.10.2).**

<!-- label: IV.16.10.2 -->

*Let `A` be a ring, `B` a formally smooth `A`-algebra for the discrete topologies `(0, 19.3.1)`. Then `Spec(B)` is
differentially smooth over `Spec(A)`.*

Indeed, `B ⊗_A B` is then (for the discrete topologies) a formally smooth `B`-algebra (for either of the canonical
homomorphisms `b ↦ b ⊗ 1`, `b ↦ 1 ⊗ b` of `B`

<!-- original page 52 -->

into `B ⊗_A B`) `(0, 19.3.5, (iii))`; hence `B ⊗_A B` is also a formally smooth `A`-algebra for the discrete topologies
`(0, 19.3.5, (ii))`. On setting `𝔍 = 𝔍_{B/A}`, it follows that `B ⊗_A B` is also a formally smooth `A`-algebra for the
`𝔍`-preadic topology `(0, 19.3.8)`; since by hypothesis `B = (B ⊗_A B)/𝔍` is a formally smooth `A`-algebra for the
discrete topologies, the proposition follows from the equivalence of a) and b) in `(0, 19.5.4)`.

**Proposition (16.10.3).**

<!-- label: IV.16.10.3 -->

*For a morphism `f : X → S` to be differentially smooth, it is necessary and sufficient that, for every `x ∈ X`, there
exist an affine open neighbourhood `U` of `x`, of ring `A`, such that `Γ(U, 𝒫^∞_{X/S})` is an augmented topological
`A`-algebra isomorphic to the completed algebra `B̂`, where `B = 𝕊_A(V)`, `V` being a projective `A`-module and `B`
being endowed with the `B^+`-preadic topology (where `B^+` is the augmentation ideal). If `Ω^1_{X/S}` is locally free of
finite rank, one may replace `B̂` by the formal power series algebra `A[[T_1, …, T_n]]`.*

The notion of a differentially smooth morphism being clearly local on `X`, one may restrict to the case where
`S = Spec(B)`, `X = Spec(C)`. Consider `C ⊗_B C` as a `C`-algebra (via the first factor); set `𝔍 = 𝔍_{C/B}` and endow
`C ⊗_B C` with the `𝔍`-preadic topology; one may apply to the `C`-algebra `C ⊗_B C` and to the ideal `𝔍` of `C ⊗_B C`
the equivalence of b) and c) in `(0, 19.5.4)`, since `(C ⊗_B C)/𝔍 = C` is obviously a formally smooth `C`-algebra for
the discrete topologies. The topology on `Γ(U, 𝒫^∞_{X/S})` is clearly the projective limit topology on this ring
`(16.1.11)`.

One notes that the integer `n` in the statement of `(16.10.3)` is the rank of `Ω^1_{X/S}` at the point `x`. We shall see
below `(17.13.5)` that, when `f` is differentially smooth and locally of finite type, `n` is moreover equal to the
dimension of the fibre `f^{−1}(f(x))` at the point `x`.

**Proposition (16.10.4).**

<!-- label: IV.16.10.4 -->

*Let `f : X → S`, `g : S' → S` be two morphisms, and set `X' = X ×_S S'`, `f' = f_{(S')} : X' → S'`.*

*(i) If `f` is differentially smooth, the same is true of `f'`.*

*(ii) Conversely, if `g` is faithfully flat and quasi-compact, and if `f'` is differentially smooth and `Ω^1_{X'/S'}` is
an `𝒪_{X'}`-Module of finite type, then `f` is differentially smooth and `Ω^1_{X/S}` is an `𝒪_X`-Module of finite type.*

Indeed, if `f` is differentially smooth, the `gr_n(𝒫^n_{X/S})` are flat `𝒪_X`-Modules; consequently `(16.4.6)`, the
homomorphism `gr_n(𝒫^n_{X/S}) ⊗_{𝒪_X} 𝒪_{X'} → gr_n(𝒫^n_{X'/S'})` is bijective for every `n`, and by virtue of the
commutativity of the diagram `(16.2.1.3)`, it follows from the definition `(16.10.1)` that `f'` is differentially
smooth. On the other hand, if `g` is faithfully flat and quasi-compact, it again follows from `(16.4.6)` that
`gr_n(𝒫^n_{X/S}) ⊗_{𝒪_X} 𝒪_{X'} → gr_n(𝒫^n_{X'/S'})` is bijective for every `n`. Suppose then that `f'` is
differentially smooth and `Ω^1_{X'/S'}` of finite rank. Since the canonical projection `X' → X` is faithfully flat and
quasi-compact, it follows first from `(2.5.2)` that `Ω^1_{X/S}` is a locally free `𝒪_X`-Module of finite rank, then from
`(2.2.7)` that the canonical homomorphism `(16.3.1.1)` is bijective, and therefore `f` is differentially smooth.

**Proposition (16.10.5).**

<!-- label: IV.16.10.5 -->

*For a morphism locally of finite type `f : X → S` to be differentially smooth, it is necessary and sufficient that the
diagonal immersion `Δ_f : X → X ×_S X` be quasi-regular.*

<!-- original page 53 -->

The question being local, one may restrict to the case where `S` and `X` are affine, in which case the diagonal
sub-prescheme of `X ×_S X` is closed. The hypothesis that `f` is locally of finite type entails that `Δ_f` is locally of
finite presentation `(IV, 1.4.3.1)`, hence the diagonal sub-prescheme of `X ×_S X` is defined by an Ideal `𝒥` of finite
type, and `Ω^1_{X/S} = 𝒥/𝒥²` is an `𝒪_X`-Module of finite type. The proposition then follows immediately from the
comparison of the conditions of `(16.10.1)` and `(16.9.4)`.

**Remark (16.10.6).**

<!-- label: IV.16.10.6 -->

Let `f : X → S` be a morphism such that the `𝒪_X`-Module `Ω^1_{X/S}` is locally free of finite rank. It follows from
`(0, 20.4.7)` that every `x ∈ X` has an open neighbourhood `U` such that there exists a finite family `(z_λ)_{λ ∈ L}` of
sections of `𝒪_X` over `U` for which `(dz_λ)_{λ ∈ L}` forms a basis of the `Γ(U, 𝒪_X)`-module `Γ(U, Ω^1_{X/S})`.

### 16.11. Differential operators on a differentially smooth `S`-prescheme

**(16.11.1).**

<!-- label: IV.16.11.1 -->

Let `f : X → S` be a morphism, `U` an open set of `X`, and `(z_λ)_{λ ∈ L}` a family of sections of `𝒪_X` over `U` such
that the `dz_λ` form a system of generators of `Ω^1_{X/S} | U = Ω^1_{U/S}`. Let `m` be an integer or the symbol `∞`, and
set, for every `λ`,

```text
  (16.11.1.1)    ζ_λ = δ z_λ = d^m z_λ − z_λ ∈ Γ(U, 𝒫^m_{X/S}).
```

We shall use the customary notations of analysis; for every `𝐩 = (p_λ) ∈ ℕ^{(L)}` (so that `p_λ = 0` except for finitely
many indices), we set

```text
  (16.11.1.2)    |𝐩| = ∑_λ p_λ,    𝐩! = ∏_λ (p_λ!),
```

```text
  (16.11.1.3)    binom(𝐩, 𝐪) = 𝐩!/(𝐪!(𝐩 − 𝐪)!)    for 𝐩, 𝐪 in ℕ^{(L)}, 𝐪 ≤ 𝐩,
```

with the convention that `binom(𝐩, 𝐪) = 0` if `𝐪 ⊀ 𝐩`,

```text
  (16.11.1.4)    𝐳^𝐩 = ∏_λ (z_λ)^{p_λ},    𝛇^𝐩 = ∏_λ (ζ_λ)^{p_λ}.
```

One thus has, with these notations,

```text
  (16.11.1.5)    d^m(𝐳^𝐩) = (d^m 𝐳)^𝐩 = (𝛇 + 𝐳)^𝐩 = ∑_{𝐪 ≤ 𝐩} binom(𝐩, 𝐪) 𝐳^{𝐩 − 𝐪} 𝛇^𝐪,
```

```text
  (16.11.1.6)    𝛇^𝐩 = (d^m 𝐳 − 𝐳)^𝐩 = ∑_{𝐪 ≤ 𝐩} (−1)^{|𝐩 − 𝐪|} binom(𝐩, 𝐪) 𝐳^{𝐩 − 𝐪} d^m(𝐳^𝐪).
```

Since the `dz_λ` generate `Ω^1_{X/S}` and are the images of the `δ z_λ`, and the canonical homomorphism `(16.3.1.1)` is
surjective, one concludes that, for finite `m`, the `δ z_λ` generate the `𝒪_U`-Algebra `𝒫^m_{U/S}` (Bourbaki, *Alg.
comm.*, chap. III, §2, n° 8, cor. 2 of th. 1). Therefore the `𝛇^𝐩` (for `|𝐩| ≤ m`) generate the `𝒪_U`-Module
`𝒫^m_{U/S}`. A differential operator `D ∈ Diff^m_{U/S}` is consequently entirely determined by the values of `⟨𝛇^𝐩, D⟩`
for `|𝐩| ≤ m`, or, what amounts to the same by `(16.11.1.5)` and `(16.11.1.6)`, by the values

<!-- original page 54 -->

of the `⟨d^m(𝐳^𝐩), D⟩ = D(𝐳^𝐩)` for `|𝐩| ≤ m`; more precisely, it follows from `(16.11.1.5)` that one has

```text
  (16.11.1.7)    D(𝐳^𝐩) = ⟨d^m(𝐳^𝐩), D⟩ = ∑_{𝐪 ≤ 𝐩} binom(𝐩, 𝐪) ⟨𝛇^𝐪, D⟩ 𝐳^{𝐩 − 𝐪}.
```

**Theorem (16.11.2).**

<!-- label: IV.16.11.2 -->

*Let `f : X → S` be a morphism, `U` an open set of `X`, `(z_λ)_{λ ∈ L}` a family of sections of `𝒪_X` over `U` such that
the family `(dz_λ)_{λ ∈ L}` generates `Ω^1_{X/S} | U = Ω^1_{U/S}`. The following conditions are equivalent:*

*a) `f | U` is differentially smooth and `(dz_λ)` is a basis of the `𝒪_U`-Module `Ω^1_{U/S}`.*

*b) There exists a family `(D_𝐩)_{𝐩 ∈ ℕ^{(L)}}` of differential operators from `𝒪_U` into itself satisfying the
conditions*

```text
  (16.11.2.1)    D_𝐩(𝐳^𝐪) = binom(𝐪, 𝐩) 𝐳^{𝐪 − 𝐩}    (𝐩, 𝐪 in ℕ^{(L)}).
```

*Moreover, when these conditions are verified, the family `(D_𝐩)` is uniquely determined by the conditions `(16.11.2.1)`
and satisfies the relations*

```text
  (16.11.2.2)    D_𝐩 ∘ D_𝐪 = D_𝐪 ∘ D_𝐩 = ((𝐩 + 𝐪)!/(𝐩! 𝐪!)) D_{𝐩 + 𝐪}    (𝐩, 𝐪 in ℕ^{(L)}).
```

*Finally, if `L` is finite, then for every integer `m` the `D_𝐩` such that `|𝐩| ≤ m` form a basis of the `𝒪_U`-Module
`𝒟iff^m_{U/S}`; in other words, every differential operator of order `≤ m` on `U` can be written in one and only one way
in the form*

```text
  D = ∑_{|𝐩| ≤ m} a_𝐩 D_𝐩
```

*where the `a_𝐩` are sections of `𝒪_X` over `U`.*

Note first that, by virtue of `(16.11.1.6)` and `(16.11.1.5)`, one verifies immediately that the conditions
`(16.11.2.1)` are equivalent to

```text
  (16.11.2.3)    ⟨𝛇^𝐩, D_𝐪⟩ = δ_{𝐩 𝐪}    (Kronecker's symbol).
```

The existence of the family `(D_𝐩)` satisfying these relations first entails (on taking `|𝐩| = 1`) that the `dz_λ` are
linearly independent, hence form a basis of the `𝒪_U`-Module `Ω^1_{U/S}`. Then, for every integer `m ≥ 1`, one similarly
deduces from `(16.11.2.3)` that the `𝛇^𝐩` such that `|𝐩| ≤ m` are linearly independent; consequently the canonical
homomorphism `(16.3.1.1)` is injective, hence bijective, and this proves that b) implies a). The converse follows at
once from the definition `(16.10.1)`: the fact that the `𝛇^𝐩` form a basis of `𝒫^m_{U/S}` for `|𝐩| ≤ m` entails the
existence and uniqueness of a family of homomorphisms `u_{𝐪, m} : 𝒫^m_{U/S} → 𝒪_U` (`|𝐪| ≤ m`) such that
`⟨𝛇^𝐩, u_{𝐪, m}⟩ = δ_{𝐩 𝐪}` for `|𝐩| ≤ m`, `|𝐪| ≤ m`. For a given value of `𝐪`, the differential operators corresponding
to the `u_{𝐪, m}` for `m ≥ |𝐪|` are identified to a single operator `D_𝐪`. This proves that a) implies b) and moreover
that the family `(D_𝐩)` is uniquely determined, and that, if `L` is finite, for `|𝐩| ≤ m`, the `D_𝐩` form a basis of the
dual `𝒟iff^m_{U/S}` of `𝒫^m_{U/S}`. Finally, the relations `(16.11.2.2)` follow at once from the expression of the
values of the three operators considered on the `𝐳^𝐫`, and from the fact that the `𝛇^𝐫` for `|𝐫| ≤ m` generate
`𝒫^m_{U/S}`.

<!-- original page 55 -->

**Remarks (16.11.3).**

<!-- label: IV.16.11.3 -->

(i) The fact that the `D_𝐩` commute pairwise by virtue of `(16.11.2.2)` does not, of course, imply that the
`𝒪_U`-Algebra `𝒟iff_{U/S}` is commutative, since the `D_𝐩` commute with multiplication by sections of `𝒪_U` only when
`n = 0`.

(ii) The indices `𝐩` such that `|𝐩| = 1` are the `𝛜_λ = (ε_{λμ})_{μ ∈ L}`, where `ε_{λμ} = 0` if `μ ≠ λ` and
`ε_{λλ} = 1`; when `L` is finite, the operators `D_{𝛜_λ}` are none other than the `S`-derivations `D_i` introduced in
`(16.5.7)`. One notes that in general (and contrary to what happens in classical analysis), it is not the case that a
differential operator of arbitrary order can be written as a linear combination of powers of the `D_i` (cf. `(16.12)`).

(iii) For every integer `r ≥ 1`, one can define the notion of a morphism *differentially smooth up to order `r`* by
replacing in `(16.10.1)` condition (ii) by the requirement that the homomorphisms

```text
  𝕊^m_{𝒪_X}(Ω^1_{X/S}) → gr_m(𝒫^m_{X/S})
```

be bijective for every `m ≤ r`. The argument of `(16.11.2)` then shows that if, in condition a), one replaces
"differentially smooth" by "differentially smooth up to order `r`", this condition is equivalent to condition b)
restricted to `𝐩 ∈ ℕ^{(L)}`, `𝐪 ∈ ℕ^{(L)}` with `|𝐩| ≤ r`, `|𝐪| ≤ r`.

### 16.12. Case of characteristic zero — Jacobian criterion for differentially smooth morphisms

**(16.12.1).**

<!-- label: IV.16.12.1 -->

We say that a prescheme `X` is *of characteristic `p`* (`p` equal to `0` or to a prime number) if, for every affine open
set `U` of `X`, the ring `Γ(U, 𝒪_X)` is of characteristic `p` `(0, 21.1.1)`. It follows from `(0, 21.1.3)` that for `X`
to be of characteristic `0` it is necessary and sufficient that, for every closed point `x` of `X`, the residue field
`κ(x)` is of characteristic `0`, or equivalently that `X` can be endowed with a structure of `ℚ`-prescheme (necessarily
unique).

**Theorem (16.12.2).**

<!-- label: IV.16.12.2 -->

*Let `X` be a prescheme of characteristic `0`, `f : X → S` a morphism. If `Ω^1_{X/S}` is a locally free `𝒪_X`-Module
(not necessarily of finite type), then `f` is differentially smooth.*

The question being local on `X`, one may suppose that there exists a family `(z_λ)` of sections of `𝒪_X` over `X` such
that `(dz_λ)` is a basis of the `𝒪_X`-Module `Ω^1_{X/S}`. Applying criterion `(16.11.2)`, it suffices to verify that the
operators

```text
  D_𝐩 = (𝐩!)^{−1} ∏_λ D_λ^{p_λ}
```

(where the `D_λ` are the coordinate forms corresponding to the basis `(dz_λ)`) satisfy the relations `(16.11.2.1)`,
which is a consequence of the fact that the `D_λ` are derivations.

**(16.12.3).**

<!-- label: IV.16.12.3 -->

The preceding theorem no longer holds if one drops the hypothesis that `X` is of characteristic `0`. For example, if
`S = Spec(k)`, where `k` is a field of characteristic `p > 0`, `X = Spec(K)` where `K = k(α)` with `α ∉ k`, `α^p ∈ k`,
one verifies immediately

<!-- original page 56 -->

that `Ω^1_{X/S}` is of rank `1`, and that the morphism `X → S` is differentially smooth up to order `p − 1`
`(16.11.3, (iii))`, but not up to order `p`. However, the proof of `(16.12.2)` shows that if `Ω^1_{X/S}` is locally
free, and if `n! · 1_{𝒪_X}` is invertible in `Γ(X, 𝒪_X)`, then `X` is differentially smooth over `S` up to order `n`.

[^16.8-gabriel]: For a more general formalism, see Exposé VII of `[42]` (due to P. Gabriel).

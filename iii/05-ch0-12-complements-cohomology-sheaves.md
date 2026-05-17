# Chapter 0_III

## §12. Complements on the cohomology of sheaves

<!-- original page 49 -->

### 12.1. Cohomology of sheaves of modules on ringed spaces

**12.1.1.**

<!-- label: 0_III.12.1.1 -->

Let `(X, 𝒪_X)` be a ringed space. Recall that for every `𝒪_X`-module `ℱ` one defines the cohomology `H^•(X, ℱ)`, which
is a universal cohomological functor `(T, 2.2)` from the category `C(X)` of `𝒪_X`-modules to the category of abelian
groups; it is the right-derived functor of the left-exact functor `ℱ ↦ Γ(X, ℱ)`. The functor `H^•(X, ℱ)` is isomorphic

<!-- original page 50 -->

to the restriction to the category `C(X)` of the cohomological functor defined in the same way on the category of
*sheaves of abelian groups* on `X` `(G, II, 7.2.1)`.

**12.1.2.**

<!-- label: 0_III.12.1.2 -->

Set `A = Γ(X, 𝒪_X)`. Since every element of `A` defines an endomorphism of the abelian group `Γ(X, ℱ)`, it defines by
functoriality an endomorphism of the `∂`-functor `H^•(X, ℱ)`; these endomorphisms equip each `H^p(X, ℱ)` with a
structure of `A`-module, and the operator `∂` is `A`-linear. Moreover, for any two non-negative integers `p`, `q` and
any two `𝒪_X`-modules `ℱ`, `𝒢`, one has a homomorphism of `A`-modules, called the *cup product*

```text
  H^p(X, ℱ) ⊗_A H^q(X, 𝒢) → H^{p+q}(X, ℱ ⊗_{𝒪_X} 𝒢)                          (12.1.2.1)
```

`(G, II, 6.6)`. These homomorphisms make the direct sum `S` of the `H^p(X, 𝒪_X)` (for `p ≥ 0`) into a graded
anticommutative `A`-algebra, and the direct sum of the `H^p(X, ℱ)` into a graded `S`-module.

For every open cover `𝔘` of `X`, we shall always denote by `C^•(𝔘, ℱ)` (contrary to `(G, II, 5.1)`) the complex of
*alternating* cochains of the nerve of `𝔘` with values in the system of coefficients `Γ(U_σ, ℱ)`. It is clear that
`C^•(𝔘, ℱ)` is a graded `A`-module, so the cohomology groups `H^•(𝔘, ℱ)` of this complex are endowed with a structure of
`A`-module; moreover, the canonical maps `H^•(𝔘, ℱ) → H^•(X, ℱ)` `(G, II, 5.4)` are `A`-linear.

**12.1.3.**

<!-- label: 0_III.12.1.3 -->

Let `(X', 𝒪_{X'})` be a second ringed space, and let `f = (ψ, θ)` be a morphism from `X'` to `X`.

Set `A' = Γ(X', 𝒪_{X'})`; the `ψ`-morphism `θ` defines canonically a ring homomorphism `A → A'`. Let `ℱ` be an
`𝒪_X`-module and `ℱ'` an `𝒪_{X'}`-module; for every `f`-morphism `u : ℱ → ℱ'` `(0_I, 4.4.1)` we shall see that one can
define, for every `p ≥ 0`, a di-homomorphism

```text
  u_p : H^p(X, ℱ) → H^p(X', ℱ').                                             (12.1.3.1)
```

Indeed, since `ψ^*` is exact in the category of sheaves of abelian groups on `X`, `ℱ ↦ H^•(X', ψ^*(ℱ))` is a `∂`-functor
in this category, and one knows that one has a canonical homomorphism of `∂`-functors

```text
  H^•(X, ℱ) → H^•(X', ψ^*(ℱ))                                                (12.1.3.2)
```

uniquely determined by the condition of reducing to the canonical homomorphism `Γ(X, ℱ) → Γ(X', ψ^*(ℱ))` in degree `0`
`(T, 3.2.2)`. Moreover, every element of `A` determines an endomorphism `μ` of `Γ(X, ℱ)` and an endomorphism `μ'` of
`Γ(X', ψ^*(ℱ))` such that the diagram

```text
                 Γ(X, ℱ)   →   Γ(X', ψ^*(ℱ))
                    ↓μ              ↓μ'                                       (12.1.3.3)
                 Γ(X, ℱ)   →   Γ(X', ψ^*(ℱ))
```

<!-- original page 51 -->

is commutative; by the uniqueness property of extension of morphisms for universal cohomological functors `(T, 2.2)`,
one deduces unique extensions of `μ` and `μ'` to the cohomology making the diagrams analogous to `(12.1.3.3)`
commutative, which means that `(12.1.3.2)` is a homomorphism of `A`-modules. Now note that one has
`f^*(ℱ) = ψ^*(ℱ) ⊗_{ψ^*(𝒪_X)} 𝒪_{X'}`, so one has a canonical di-homomorphism `ψ^*(ℱ) → f^*(ℱ)` of the `ψ^*(𝒪_X)`-module
`ψ^*(ℱ)` into the `𝒪_{X'}`-module `f^*(ℱ)`. By functoriality, one therefore deduces a functorial di-homomorphism

```text
  H^p(X', ψ^*(ℱ)) → H^p(X', f^*(ℱ))                                          (12.1.3.4)
```

with corresponding rings `A` and `A'`; composing this di-homomorphism with `(12.1.3.2)`, one obtains a canonical
di-homomorphism functorial in `ℱ`

```text
  θ_p : H^p(X, ℱ) → H^p(X', f^*(ℱ)).                                         (12.1.3.5)
```

Finally, by functoriality, one deduces from the homomorphism `u^♭ : f^*(ℱ) → ℱ'` a homomorphism of `A'`-modules
`H^p(X', f^*(ℱ)) → H^p(X', ℱ')`, which, composed with `(12.1.3.5)`, gives `(12.1.3.1)`.

Let `f' = (ψ', θ') : X'' → X'` be a second morphism of ringed spaces, `f'' = f ∘ f'` the composite morphism. Taking into
account the commutativity of the functor `ψ^*` with tensor product `(0_I, 4.3.3)`, one verifies immediately that the
composite of the di-homomorphism `H^p(X', f^*(ℱ)) → H^p(X'', f'^*(f^*(ℱ)))` with `(12.1.3.5)` is the corresponding
di-homomorphism `H^p(X, ℱ) → H^p(X'', f''^*(ℱ))`.

**12.1.4.**

<!-- label: 0_III.12.1.4 -->

A direct definition of the homomorphism `(12.1.3.2)` can be obtained as follows: one considers an injective resolution
`ℒ^• = (ℒ^i)` of `ℱ` formed of sheaves of abelian groups on `X`; since the functor `ψ^*` is exact, `ψ^*(ℒ^•)` is a
resolution of `ψ^*(ℱ)` formed of sheaves on `X'`. If `ℒ'^• = (ℒ'^i)` is an injective resolution of `ψ^*(ℱ)` in the
category of sheaves of abelian groups on `X'`, there is therefore a morphism `ψ^*(ℒ^•) → ℒ'^•` of complexes of sheaves
of abelian groups, compatible with the augmentations `(M, V, 1.1 a))`, well-determined up to homotopy. One thus deduces
homomorphisms

```text
  Γ(X, ℒ^•) → Γ(X', ψ^*(ℒ^•)) → Γ(X', ℒ'^•)
```

of complexes of abelian groups, whose composite, by passage to cohomology, gives a morphism of `∂`-functors
`H^•(X, ℱ) → H^•(X', ψ^*(ℱ))`; since it coincides with `(12.1.3.2)` in degree `0`, it is identical to it `(T, 2.2)`.

Now consider an open cover `𝔘 = (U_α)` of `X`, and let `𝔘' = (ψ^{-1}(U_α))` be the open cover of `X'` obtained as the
inverse image of `𝔘`. The canonical homomorphisms `Γ(V, ℱ) → Γ(ψ^{-1}(V), f^*(ℱ))` for every open `V` of `X` define at
once (cf. `G, II, 5.1`) a homomorphism of complexes `C^•(𝔘, ℱ) → C^•(𝔘', f^*(ℱ))`, whence the canonical homomorphisms

```text
  θ_p : H^p(𝔘, ℱ) → H^p(𝔘', f^*(ℱ)).                                         (12.1.4.1)
```

<!-- original page 52 -->

Moreover, one has commutative diagrams

```text
              H^p(𝔘, ℱ)    →^{θ_p}    H^p(𝔘', f^*(ℱ))
                  ↓                       ↓                                   (12.1.4.2)
              H^p(X, ℱ)    →^{θ_p}    H^p(X', f^*(ℱ))
```

where the vertical arrows are the canonical homomorphisms of `(G, II, 5.2)`. To establish the commutativity of
`(12.1.4.2)`, consider the complex of sheaves of (alternating) cochains of `ℱ` relative to `𝔘`, `𝒞^•(𝔘, ℱ)`, such that
`Γ(X, 𝒞^•(𝔘, ℱ)) = C^•(𝔘, ℱ)` `(G, II, 5.2)`. The canonical homomorphisms `Γ(V, ℱ) → Γ(ψ^{-1}(V), ψ^*(ℱ))` then define a
`ψ`-morphism `𝒞^•(𝔘, ℱ) → 𝒞^•(𝔘', ψ^*(ℱ))`, and one has, with the notation above, a commutative diagram

```text
   Γ(X, 𝒞^•(𝔘, ℱ))   →   Γ(X', 𝒞^•(𝔘', ψ^*(ℱ)))
         ↓                          ↓
   Γ(X, ℒ^•)         →   Γ(X', ψ^*(ℒ^•))   →   Γ(X', ℒ'^•)
```

which, on passing to cohomology, gives commutative diagrams

```text
              H^p(𝔘, ℱ)    →    H^p(𝔘', ψ^*(ℱ))
                  ↓                  ↓
              H^p(X, ℱ)    →    H^p(X', ψ^*(ℱ))
```

where the vertical arrows are the canonical homomorphisms of `(G, II, 5.2)`. It then suffices to combine these diagrams
with the commutative diagrams

```text
              H^p(𝔘', ψ^*(ℱ))   →   H^p(𝔘', f^*(ℱ))
                  ↓                       ↓
              H^p(X', ψ^*(ℱ))   →   H^p(X', f^*(ℱ))
```

<!-- original page 53 -->

which come from the homomorphism `ψ^*(ℱ) → f^*(ℱ)` and from the functorial character of the canonical homomorphisms of
`(G, II, 5.2)`, to obtain the commutativity of `(12.1.4.2)`.

Note that if `A = Γ(X, 𝒪_X)`, `A' = Γ(X', 𝒪_{X'})`, the homomorphism `(12.1.4.1)` is a di-homomorphism of modules
corresponding to the rings `A` and `A'`. One has a *transitivity* property for `(12.1.4.1)` with respect to the
composite of two morphisms, analogous to the transitivity of `(12.1.3.5)`. Finally, note that in the preceding
definitions, instead of an injective resolution `ℒ^•` of `ℱ`, one could equally well have started from a resolution such
that `H^p(X, ℒ^i) = 0` for all `i` and all `p > 0` `(G, II, 4.7.1)`.

**12.1.5.**

<!-- label: 0_III.12.1.5 -->

Let `ℱ`, `𝒢`, `𝓗` be three `𝒪_X`-modules, and consider an `𝒪_X`-homomorphism `u : ℱ ⊗_{𝒪_X} 𝒢 → 𝓗`, which gives, for
cohomology, homomorphisms

```text
  H^p(X, ℱ) ⊗_A H^q(X, 𝒢) → H^{p+q}(X, 𝓗)                                    (12.1.5.1)
```

deduced from the cup product `(12.1.2.1)`. We show that, with the hypotheses and notation of `(12.1.3)`, one has
commutative diagrams

```text
   H^p(X, ℱ) ⊗_A H^q(X, 𝒢)                  →   H^{p+q}(X, 𝓗)
            ↓                                          ↓                      (12.1.5.2)
   H^p(X', f^*(ℱ)) ⊗_{A'} H^q(X', f^*(𝒢))   →   H^{p+q}(X', f^*(𝓗))
```

where the vertical arrows come from the canonical homomorphisms `(12.1.3.5)`. For this, recall that `(12.1.5.1)` can be
obtained by starting from the *canonical* resolutions `(G, II, 4.3)` `ℒ^•`, `ℳ^•`, `𝒩^•` of `ℱ`, `𝒢`, `𝓗` respectively
(which are formed of `𝒪_X`-modules), from the linear map `ℒ^• ⊗_{𝒪_X} ℳ^• → 𝒩^•` of complexes of `𝒪_X`-modules
corresponding to `u`, which yields a homomorphism of complexes of `A`-modules `Γ(X, ℒ^•) ⊗_A Γ(X, ℳ^•) → Γ(X, 𝒩^•)`, and
by passing to cohomology, the homomorphisms `H^p(Γ(X, ℒ^•)) ⊗_A H^q(Γ(X, ℳ^•)) → H^{p+q}(Γ(X, 𝒩^•))` `(G, II, 6.6)`.
Now, one clearly has a commutative diagram

```text
   Γ(X, ℒ^•) ⊗_A Γ(X, ℳ^•)                                              →   Γ(X, 𝒩^•)
            ↓                                                                  ↓        (12.1.5.3)
   Γ(X', ψ^*(ℒ^•)) ⊗_{Γ(X', ψ^*(𝒪_X))} Γ(X', ψ^*(ℳ^•))                  →   Γ(X', ψ^*(𝒩^•))
```

<!-- original page 54 -->

which gives, on passing to cohomology, the commutative diagrams

```text
   H^p(X, ℱ) ⊗_A H^q(X, 𝒢)                                                                                →   H^{p+q}(X, 𝓗)
            ↓                                                                                                       ↓                        (12.1.5.4)
   H^p(Γ(X', ψ^*(ℒ^•))) ⊗_{Γ(X', ψ^*(𝒪_X))} H^q(Γ(X', ψ^*(ℳ^•)))                                       →   H^{p+q}(Γ(X', ψ^*(𝒩^•))).
```

But since `ψ^*(ℒ^•)`, `ψ^*(ℳ^•)` and `ψ^*(𝒩^•)` are *resolutions* of `ψ^*(ℱ)`, `ψ^*(𝒢)`, `ψ^*(𝓗)` respectively, one has
a commutative diagram `(G, II, 6.6.1)`

```text
   H^p(Γ(X', ψ^*(ℒ^•))) ⊗_{Γ(X', ψ^*(𝒪_X))} H^q(Γ(X', ψ^*(ℳ^•)))   →   H^{p+q}(Γ(X', ψ^*(𝒩^•)))
            ↓                                                                  ↓                                 (12.1.5.5)
   H^p(X', ψ^*(ℱ)) ⊗_{Γ(X', ψ^*(𝒪_X))} H^q(X', ψ^*(𝒢))            →   H^{p+q}(X', ψ^*(𝓗)).
```

Finally, by functoriality, one has a commutative diagram

```text
   H^p(X', ψ^*(ℱ)) ⊗_{Γ(X', ψ^*(𝒪_X))} H^q(X', ψ^*(𝒢))   →   H^{p+q}(X', ψ^*(𝓗))
            ↓                                                       ↓                       (12.1.5.6)
   H^p(X', f^*(ℱ)) ⊗_{A'} H^q(X', f^*(𝒢))                →   H^{p+q}(X', f^*(𝓗))
```

and by combining the three diagrams `(12.1.5.4)`, `(12.1.5.5)` and `(12.1.5.6)`, one obtains the desired commutative
diagram `(12.1.5.2)`.

<!-- original page 55 -->

**Remark (12.1.6).**

<!-- label: 0_III.12.1.6 -->

With the notation of `(12.1.3)`, suppose one has a commutative diagram

```text
   0  →  ℱ   →^r   𝒢   →^s   𝓗   →  0
              ↓u         ↓v         ↓w                                        (12.1.6.1)
   0  →  ℱ'  →^{r'}  𝒢'  →^{s'}  𝓗'  →  0
```

where `r`, `s` are homomorphisms of `𝒪_X`-modules, `r'`, `s'` are homomorphisms of `𝒪_{X'}`-modules, `u`, `v`, `w` are
`f`-morphisms, and the rows are exact. One then deduces a commutative diagram

```text
   ⋯ → H^p(X, ℱ)   → H^p(X, 𝒢)   → H^p(X, 𝓗)   →^∂  H^{p+1}(X, ℱ)   → ⋯
            ↓u_p          ↓v_p          ↓w_p           ↓u_{p+1}                (12.1.6.2)
   ⋯ → H^p(X', ℱ') → H^p(X', 𝒢') → H^p(X', 𝓗') →^∂ H^{p+1}(X', ℱ') → ⋯.
```

Indeed, `(12.1.6.1)` factors as

```text
   0  →  ℱ          →   𝒢          →   𝓗          →  0
              ↓               ↓               ↓
   0  →  ψ^*(ℱ)     →   ψ^*(𝒢)     →   ψ^*(𝓗)     →  0
              ↓               ↓               ↓
   0  →  ℱ'         →   𝒢'         →   𝓗'         →  0
```

where the middle row is exact `(0_I, 3.7.2)`, and it suffices to use the fact that `(12.1.3.2)` is a homomorphism of
`∂`-functors and that the `H^p(X', ℱ')` form a `∂`-functor in `ℱ'`.

**12.1.7.**

<!-- label: 0_III.12.1.7 -->

The hypotheses and notation being those of `(12.1.3)`, consider now the case where `ℱ = f_*(ℱ') = ψ_*(ℱ')`; we shall see
that the di-homomorphism defined in `(12.1.3)`

```text
  H^p(X, f_*(ℱ')) → H^p(X', ℱ')                                              (12.1.7.1)
```

can be obtained (up to an automorphism of `H^p(X', ℱ')`) as an *edge homomorphism* of a spectral sequence of the
composite functor `ℱ' ↦ Γ(X', ψ_*(ℱ'))` `(T, 2.4)`. The description of the homomorphism `(12.1.7.1)` given in `(12.1.4)`
shows here that one can obtain this homomorphism as follows: one considers injective resolutions `ℒ^•` and `ℒ'^•` of
`ψ_*(ℱ')` and of `ℱ'` respectively, then one takes a homomorphism of complexes `v : ψ^*(ℒ^•) → ℒ'^•` "lying above" the
canonical homomorphism `ψ^*(ψ_*(ℱ')) → ℱ'`;

<!-- original page 56 -->

one then notes that one has `Γ(X', ℒ'^•) = Γ(X, ψ_*(ℒ'^•))` and that the composite homomorphism

```text
  Γ(X, ℒ^•) → Γ(X', ψ^*(ℒ^•)) →^{Γ(v)} Γ(X', ℒ'^•)
```

is none other than

```text
  Γ(v^♭) : Γ(X, ℒ^•) → Γ(X, ψ_*(ℒ'^•))                                       (12.1.7.2)
```

`(0_I, 3.7.1)`, and `(12.1.7.1)` is obtained by passage to cohomology in `(12.1.7.2)`. On the other hand, the spectral
sequences of the composite functor `ℱ' ↦ Γ(X, ψ_*(ℱ'))` are obtained by considering an injective Cartan–Eilenberg
resolution `ℳ^{••} = (ℳ^{ij})` of the complex `ψ_*(ℒ'^•)` in the category of sheaves of abelian groups on `X`; the
spectral sequences in question are those of the bicomplex `Γ(X, ℳ^{••})` (which are biregular since `ℳ^{ij} = 0` for
`i < 0` or `j < 0`). Now, the first spectral sequence of this bicomplex *degenerates*, for the sheaves `ψ_*(ℒ'^i)` are
flasque `(G, II, 3.1.1)`, hence `H_{II}^q(Γ(X, ℳ^{i•})) = H^q(ψ_*(ℒ'^i)) = 0` for `q > 0` `(G, II, 4.4.3)`; one
therefore has *bijective* edge homomorphisms `(11.1.6)`

```text
  'E_2^{i,0} = H^i(H_{II}^0(Γ(X, ℳ^{••}))) → H^i(Γ(X, ℳ^{••}))               (12.1.7.3)
```

and one knows `(11.3.4)` that this homomorphism comes, by passage to cohomology, from the augmentation

```text
  Γ(X, ψ_*(ℒ'^•)) → Γ(X, ℳ^{••})                                             (12.1.7.4)
```

which itself comes from the augmentation `η : ψ_*(ℒ'^•) → ℳ^{•0}`. On the other hand, for the second spectral sequence
one has edge homomorphisms

```text
  ″E_2^{i,0} = H^i(H_I^0(Γ(X, ℳ^{••}))) → H^i(Γ(X, ℳ^{••}))                  (12.1.7.5)
```

coming `(11.3.4)`, by passage to cohomology, from the homomorphism of complexes `Z_I^0(Γ(X, ℳ^{••})) → Γ(X, ℳ^{••})`.
Now, since `ψ_*` is left-exact, the sequence

```text
  0 → ψ_*(ℱ') → ψ_*(ℒ'^0) → ψ_*(ℒ'^1)
```

is exact; by the definition of a Cartan–Eilenberg resolution `(11.4.2)`, one can therefore take `B_I^0(ℳ^{••}) = 0`,
`Z_I^0(ℳ^{••}) = ℒ^•`; since the diagram

```text
                    ℒ^0   →^{i^0}   ℳ^{00}
                  ε ↓         ↗^{ε''}     ↑η^0
                    ψ_*(ℱ')   →^{ε'}    ψ_*(ℒ'^0)
```

is commutative, the injection of complexes `i : ℒ^• → ℳ^{•0}` is compatible with the augmentations `ε` and `ε''`. One
thus has two homomorphisms of complexes from `ℒ^•` into `ℳ^{•0}`

```text
                    ℒ^•   →^i      ℳ^{•0}
                  v^♭ ↘    ↗ η
                    ψ_*(ℒ'^•)
```

<!-- original page 57 -->

compatible with the augmentations `ε` and `ε''`; since `ℒ^•` is an injective resolution and `ℳ^{•0}` is formed of
injective sheaves, it follows from `(M, V, 1.1 a))` that these two homomorphisms are *homotopic*; the same is therefore
true of the two corresponding homomorphisms `Γ(X, ℒ^•) → Γ(X, ℳ^{•0})`, and on passing to cohomology one obtains the
*same* homomorphism; in other words, one has shown that the edge homomorphism `(12.1.7.5)`, which is written
`H^p(X, ψ_*(ℱ')) → H^p(Γ(X, ℳ^{••}))`, is composed of `(12.1.7.1)` and of `(12.1.7.3)`, which is written
`H^p(X', ℱ') → H^p(Γ(X, ℳ^{••}))` and which we have seen to be an *isomorphism*; whence our assertion.

### 12.2. Higher direct images

**12.2.1.**

<!-- label: 0_III.12.2.1 -->

Let `(X, 𝒪_X)`, `(Y, 𝒪_Y)` be two ringed spaces, `f = (ψ, θ)` a morphism from `X` to `Y`, which defines the *direct
image functor* `f_* : C(X) → C(Y)`, identical moreover with the restriction to `C(X)` of the functor `ψ_*` defined in
the category of sheaves of abelian groups on `X`. This last functor is additive and left-exact, and since every sheaf of
abelian groups on `X` is isomorphic to a subsheaf of an *injective* sheaf of abelian groups, one defines the
*right-derived functors* `ℱ ↦ R^p ψ_*(ℱ)` of the functor `ψ_*`; the `R^p ψ_*(ℱ)` are sheaves of abelian groups on `Y`,
and the `R^p ψ_*` form a *universal cohomological functor* `(T, 2.3)`.

Moreover, the sheaf `R^p ψ_*(ℱ)` is the sheaf associated to the presheaf `V ↦ H^p(ψ^{-1}(V), ℱ)` `(T, 3.7.2)`. Suppose
now that `ℱ` is an `𝒪_X`-module. Then `H^p(ψ^{-1}(V), ℱ)` is naturally endowed with a structure of
`Γ(ψ^{-1}(V), 𝒪_X)`-module, hence of `Γ(V, ψ_*(𝒪_X))`-module, and the data of the homomorphism `θ : 𝒪_Y → ψ_*(𝒪_X)`
allows one to deduce a structure of `Γ(V, 𝒪_Y)`-module. For the structures thus defined, it is clear that restriction
from an open set `V` to an open set `V' ⊆ V` defines a di-homomorphism, and this permits us to define on each of the
`R^p ψ_*(ℱ)` a structure of `𝒪_Y`-module; this is the `𝒪_Y`-module that we shall denote by `R^p f_*(ℱ)`, with `R^p f_*`
thus defined as an additive functor from `C(X)` to `C(Y)`. Moreover, the `R^p f_*` form a `∂`-functor, for if
`0 → ℱ' → ℱ → ℱ'' → 0` is an exact sequence of `𝒪_X`-modules, the description of the `R^p ψ_*` and of the `𝒪_Y`-module
structure on `R^p f_*(ℱ)` given above shows at once that the homomorphism `∂ : R^p f_*(ℱ'') → R^{p+1} f_*(ℱ')` is in
this case a homomorphism of `𝒪_Y`-modules. Finally, the `R^p f_*` identify with the right-derived functors of `f_*`:
indeed, every `𝒪_X`-module admits an injective resolution formed of `𝒪_X`-modules, and since such a resolution is formed
of flasque sheaves of abelian groups `(G, II, 7.1)`, it can serve to compute the `R^p ψ_*(ℱ)`, since `R^n ψ_*(𝒢) = 0`
for `n ≥ 1` and every flasque sheaf `𝒢` `(T, 2.4.1, Remark 3, and cor. of Prop. 3.3.2)`. One thus concludes that the
`R^p f_*` form a *universal cohomological functor* from `C(X)` to `C(Y)` `(T, 2.3)`.

**12.2.2.**

<!-- label: 0_III.12.2.2 -->

Let `ℱ` and `𝒢` be two `𝒪_X`-modules. With the notation of `(12.2.1)`, for every open `V` of `Y` one has the cup-product
homomorphism `(12.1.2.1)`

```text
  H^p(ψ^{-1}(V), ℱ) ⊗_{Γ(ψ^{-1}(V), 𝒪_X)} H^q(ψ^{-1}(V), 𝒢)
      → H^{p+q}(ψ^{-1}(V), ℱ ⊗_{𝒪_X} 𝒢)
```

<!-- original page 58 -->

and it follows at once from the definition of the cup product `(G, II, 6.6)` that these homomorphisms commute with
passage from `V` to an open subspace `V'` of `V`. On the other hand, one has a homomorphism of rings

```text
  Γ(V, 𝒪_Y) → Γ(V, ψ_*(𝒪_X)) = Γ(ψ^{-1}(V), 𝒪_X)
```

coming from `θ`, whence a canonical homomorphism of tensor products

```text
  H^p(ψ^{-1}(V), ℱ) ⊗_{Γ(V, 𝒪_Y)} H^q(ψ^{-1}(V), 𝒢)
      → H^p(ψ^{-1}(V), ℱ) ⊗_{Γ(ψ^{-1}(V), 𝒪_X)} H^q(ψ^{-1}(V), 𝒢)
```

which is also compatible with the restriction from `V` to `V'`. By composition, one therefore obtains a homomorphism of
`Γ(V, 𝒪_Y)`-modules, which defines a canonical functorial-in-`ℱ`-and-`𝒢` homomorphism for the sheaves associated to the
presheaves considered:

```text
  R^p f_*(ℱ) ⊗_{𝒪_Y} R^q f_*(𝒢) → R^{p+q} f_*(ℱ ⊗_{𝒪_X} 𝒢).                  (12.2.2.1)
```

Note that for `p = q = 0`, this homomorphism reduces to `(0_I, 4.2.2.1)`.

**Proposition (12.2.3).**

<!-- label: 0_III.12.2.3 -->

*For every `𝒪_X`-module `ℱ` and every `𝒪_Y`-module locally free of finite rank `ℒ`, one has canonical functorial
isomorphisms*

```text
  R^p f_*(ℱ) ⊗_{𝒪_Y} ℒ ⥲ R^p f_*(ℱ ⊗_{𝒪_X} f^*(ℒ)).                          (12.2.3.1)
```

**Proof.** The homomorphism `(12.2.3.1)` is obtained by composing the homomorphism, a particular case of `(12.2.2.1)`,

```text
  R^p f_*(ℱ) ⊗_{𝒪_Y} f_*(f^*(ℒ)) → R^p f_*(ℱ ⊗_{𝒪_X} f^*(ℒ))                 (12.2.3.2)
```

with the homomorphism from the first member of `(12.2.3.1)` to that of `(12.2.3.2)` coming from the canonical
homomorphism `(0_I, 4.4.3.2)`. To verify that `(12.2.3.1)` is an isomorphism when `ℒ` is locally free, one can
immediately reduce to the case `ℒ = 𝒪_Y`, the question being local on `Y`, and the functors considered being additive in
`ℒ`. But then, the proposition reduces, in view of the definition of `(12.2.2.1)`, to the verification that the
corresponding homomorphism of presheaves is bijective, which is immediate by virtue of the relation `f^*(𝒪_Y) = 𝒪_X`.

**12.2.4.**

<!-- label: 0_III.12.2.4 -->

Let `(Z, 𝒪_Z)` be a third ringed space, `g : Y → Z` a morphism of ringed spaces. One knows `(G, II, 7.1 and 3.1.1)` that
for every injective `𝒪_Y`-module `𝒢`, `f_*(𝒢)` is a flasque sheaf of abelian groups, and consequently `(12.2.1)` one has
`R^p g_*(f_*(𝒢)) = 0` for every `p > 0`. It follows `(T, 2.4.1)` that the *Leray spectral sequence* of the composed
functors is applicable to the composite functor `g_* f_*`: there is a biregular spectral sequence whose abutment is the
functor `R^• h_*` where `h = g ∘ f`, and whose `E_2` term is given by

```text
  E_2^{p,q} = R^p g_*(R^q f_*(ℱ)).                                           (12.2.4.1)
```

**12.2.5.**

<!-- label: 0_III.12.2.5 -->

Under the conditions of `(12.2.4)`, we shall define directly canonical homomorphisms of `𝒪_Z`-modules

```text
  R^n g_*(f_*(ℱ)) → R^n h_*(ℱ)                                               (12.2.5.1)
  R^n h_*(ℱ) → g_*(R^n f_*(ℱ))                                               (12.2.5.2)
```

<!-- original page 59 -->

which could be identified with the "edge homomorphisms" of the Leray spectral sequence (cf. `(12.1.7)`). It suffices to
operate on the presheaves to which the higher direct image sheaves `(12.2.1)` are associated. For this, consider any
open set `W` of `Z` and its inverse image `g^{-1}(W)` in `Y`; one has a canonical di-homomorphism

```text
  H^n(g^{-1}(W), f_*(ℱ)) → H^n(f^{-1}(g^{-1}(W)), f^*(f_*(ℱ)))                (12.2.5.3)
```

with corresponding rings `Γ(g^{-1}(W), 𝒪_Y)` and `Γ(h^{-1}(W), 𝒪_X)`; on the other hand, the canonical homomorphism
`(0_I, 4.4.3.3)` yields by functoriality canonical homomorphisms

```text
  H^n(h^{-1}(W), f^*(f_*(ℱ))) → H^n(h^{-1}(W), ℱ)                            (12.2.5.4)
```

which are homomorphisms of `Γ(h^{-1}(W), 𝒪_X)`-modules. Taking into account the ring homomorphism
`Γ(W, 𝒪_Z) → Γ(h^{-1}(W), 𝒪_X)`, one sees that by composing `(12.2.5.4)` and `(12.2.5.3)` one obtains a homomorphism of
presheaves, which yields the homomorphism of sheaves `(12.2.5.1)`.

The definition of `(12.2.5.2)` is even simpler; by definition, `R^n h_*(ℱ)` is associated to the presheaf
`W ↦ H^n(f^{-1}(g^{-1}(W)), ℱ)` and `R^n f_*(ℱ)` to the presheaf `V ↦ H^n(f^{-1}(V), ℱ)`; one therefore has a canonical
homomorphism

```text
  H^n(f^{-1}(g^{-1}(W)), ℱ) → Γ(g^{-1}(W), R^n f_*(ℱ)),
```

and it is immediate that these homomorphisms define a homomorphism of presheaves, which in turn defines `(12.2.5.2)`.

**12.2.6.**

<!-- label: 0_III.12.2.6 -->

Under the hypotheses of `(12.2.4)`, let `ℱ`, `𝒢`, `𝓗` be three `𝒪_X`-modules and `u : ℱ ⊗ 𝒢 → 𝓗` an `𝒪_X`-homomorphism.
One then has commutative diagrams

```text
   R^p g_*(f_*(ℱ)) ⊗_{𝒪_Z} R^q g_*(f_*(𝒢))   →   R^{p+q} g_*(f_*(𝓗))
            ↓                                          ↓                       (12.2.6.1)
   R^p h_*(ℱ) ⊗_{𝒪_Z} R^q h_*(𝒢)             →   R^{p+q} h_*(𝓗)
```

and

```text
   R^p h_*(ℱ) ⊗_{𝒪_Z} R^q h_*(𝒢)             →   R^{p+q} h_*(𝓗)
            ↓                                          ↓                       (12.2.6.2)
   g_*(R^p f_*(ℱ)) ⊗_{𝒪_Z} g_*(R^q f_*(𝒢))   →   g_*(R^{p+q} f_*(𝓗))
```

<!-- original page 60 -->

where the horizontal arrows come from `(12.2.2.1)` (the last combined with `(0_I, 4.2.2.1)`) and the vertical arrows
from the homomorphisms `(12.2.5.1)` and `(12.2.5.2)` respectively.

It indeed suffices to verify this for the corresponding homomorphisms of presheaves; returning to the definitions given
in `(12.2.2)` and `(12.2.5)` for these homomorphisms, one is immediately reduced, for `(12.2.6.1)`, to the commutative
diagrams `(12.1.5.2)`; the verification is even simpler for `(12.2.6.2)`.

### 12.3. Complements on the Ext functors of sheaves

**12.3.1.**

<!-- label: 0_III.12.3.1 -->

Consider a ringed space `(X, 𝒪_X)`; we shall not return to the definition and principal properties of the bifunctors
`Ext^p_{𝒪_X}(X; ℱ, 𝒢)` from the category of `𝒪_X`-modules to that of `Γ(X, 𝒪_X)`-modules, and `ℰxt^p_{𝒪_X}(ℱ, 𝒢)` from
the category of `𝒪_X`-modules to itself, nor to the biregular spectral sequence `E(ℱ, 𝒢)` relating them
`(T, 4.2 and G, II, 7.3)`.

**12.3.2.**

<!-- label: 0_III.12.3.2 -->

One defines, in the same way as in `(M, XIV, 1)`, the notion of *extension* of an `𝒪_X`-module `ℱ` by an `𝒪_X`-module
`𝒢` and the composition law between classes of equivalent extensions: the arguments made for modules adapt indeed in an
obvious way to any abelian category. The second proof of `(M, XIV, 1.1)`, which uses only the existence of embeddings in
injective objects, is therefore still valid for the category of `𝒪_X`-modules, and thus shows that
`Ext^1_{𝒪_X}(X; ℱ, 𝒢)` is canonically identified with the abelian group of classes of *extensions* of `ℱ` by `𝒢`.

**Proposition (12.3.3).**

<!-- label: 0_III.12.3.3 -->

*Let `(X, 𝒪_X)` be a ringed space such that the sheaf of rings `𝒪_X` is coherent. Then, for every pair of coherent
`𝒪_X`-modules `ℱ`, `𝒢` and every `p ≥ 0`, `ℰxt^p_{𝒪_X}(ℱ, 𝒢)` is a coherent `𝒪_X`-module.*

**Proof.** Note that the `ℰxt^p_{𝒪_X}(ℱ, 𝒢)` form a cohomological functor contravariant in `ℱ`. Since `ℱ` is coherent,
there exist, for every `p` and every point `x ∈ X`, an open neighborhood `U` of `x` and an exact sequence of
`(𝒪_X ∣ U)`-modules

```text
  0 → ℛ → ℒ_{p−1} → ⋯ → ℒ_0 → ℱ ∣ U → 0
```

where each of the `ℒ_i` (`0 ≤ i ≤ p−1`) is isomorphic to an `𝒪_X^{n_i} ∣ U` and `ℛ` is coherent: this follows by
induction on `p` from `(0_I, 5.3.2)` and `(0_I, 5.3.4)`, in view of the hypothesis that `𝒪_X` is coherent.

Now note that, for `p ≥ 1`, one has `Ext^p_{𝒪_X ∣ U}(ℒ ∣ U, 𝒢 ∣ U) = 0` for every `𝒪_X`-module `ℒ` such that `ℒ ∣ U` is
isomorphic to an `𝒪_X^n ∣ U` `(T, 4.2.3)`; the argument of `(M, V, 7.2)` therefore applies to the contravariant
cohomological functor `ℱ ↦ ℋom_{𝒪_X ∣ U}(ℱ ∣ U, 𝒢 ∣ U)`, and gives an exact sequence

```text
  ℋom_{𝒪_X ∣ U}(ℒ_{p−1}, 𝒢 ∣ U) → ℋom_{𝒪_X ∣ U}(ℛ, 𝒢 ∣ U) → ℰxt^p_{𝒪_X ∣ U}(ℱ ∣ U, 𝒢 ∣ U) → 0
```

and since the first two terms of this sequence are coherent `(𝒪_X ∣ U)`-modules `(0_I, 5.3.5)`, so is the third
`(0_I, 5.3.4)`.

<!-- original page 61 -->

**Proposition (12.3.4).**

<!-- label: 0_III.12.3.4 -->

*Let `f : X → Y` be a flat morphism of ringed spaces, and let `ℱ`, `𝒢` be two `𝒪_Y`-modules.*

*(i) There exists a homomorphism of cohomological bifunctors*

```text
  f^*(ℰxt^p_{𝒪_Y}(ℱ, 𝒢)) ⥲ ℰxt^p_{𝒪_X}(f^*(ℱ), f^*(𝒢))                       (12.3.4.1)
```

*reducing in degree `0` to the canonical homomorphism `(0_I, 4.4.6)`.*

*(ii) There exists a canonical morphism of spectral sequences*

```text
  E(ℱ, 𝒢) → E(f^*(ℱ), f^*(𝒢))                                                (12.3.4.2)
```

*which, for the `E_2` terms, reduces to the homomorphisms*

```text
  H^p(Y, ℰxt^q_{𝒪_Y}(ℱ, 𝒢)) → H^p(X, ℰxt^q_{𝒪_X}(f^*(ℱ), f^*(𝒢)))             (12.3.4.3)
```

*deduced from `(12.3.4.1)` and `(12.1.3.1)`.*

**Proof.**

*(i)* Since `f^*` is an exact functor on the category of `𝒪_Y`-modules `(0_I, 6.7.2)`, the functors
`𝒢 ↦ f^*(ℋom_{𝒪_Y}(ℱ, 𝒢))` and `𝒢 ↦ ℋom_{𝒪_X}(f^*(ℱ), f^*(𝒢))` are left-exact; one deduces canonically from
`(0_I, 4.4.6)` a homomorphism of their derived functors. To compute the latter, one takes an injective resolution
`ℒ^• = (ℒ^i)` of `𝒢`, and one therefore has morphisms `ℋ^p(f^*(ℋom_{𝒪_Y}(ℱ, ℒ^•))) → ℋ^p(ℋom_{𝒪_X}(f^*(ℱ), f^*(ℒ^•)))`
of cohomologies of complexes of sheaves. Moreover, by the exactness of `f^*`, one has
`ℋ^p(f^*(ℋom_{𝒪_Y}(ℱ, ℒ^•))) = f^*(ℋ^p(ℋom_{𝒪_Y}(ℱ, ℒ^•))) = f^*(ℰxt^p_{𝒪_Y}(ℱ, 𝒢))` by definition. On the other hand,
the exactness of `f^*` entails that `f^*(ℒ^•)` is a resolution of `f^*(𝒢)`; if `ℒ'^• = (ℒ'^i)` is an injective
resolution of `f^*(𝒢)` in the category of `𝒪_X`-modules, there is therefore a homomorphism of complexes
`f^*(ℒ^•) → ℒ'^•`, determined up to homotopy, and which defines by consequence a well-determined homomorphism in
cohomology; composing this homomorphism with the one defined above, one obtains `(12.3.4.1)`.

*(ii)* With the preceding notation, one has a homomorphism of complexes of sheaves of `𝒪_X`-modules
`f^*(ℋom_{𝒪_Y}(ℱ, ℒ^•)) → ℋom_{𝒪_X}(f^*(ℱ), ℒ'^•)`. Let `ℳ^{••}` be a Cartan–Eilenberg injective resolution of the
complex `ℋom_{𝒪_Y}(ℱ, ℒ^•)` in the category of `𝒪_Y`-modules; then, by the exactness of the functor `f^*`, `f^*(ℳ^{••})`
is a Cartan–Eilenberg resolution of the complex `f^*(ℋom_{𝒪_Y}(ℱ, ℒ^•))`; if `ℳ'^{••}` is a Cartan–Eilenberg injective
resolution of the complex `ℋom_{𝒪_X}(f^*(ℱ), ℒ'^•)`, there is therefore `(11.4.2)` a homomorphism (determined up to
homotopy) `f^*(ℳ^{••}) → ℳ'^{••}` compatible with the homomorphism considered above, in other words an `f`-morphism
`ℳ^{••} → ℳ'^{••}` of bicomplexes of sheaves. From this one deduces a di-homomorphism `Γ(Y, ℳ^{••}) → Γ(X, ℳ'^{••})` of
bicomplexes of modules, determined up to homotopy, and a well-determined morphism of spectral sequences `(11.3.2)`,
which is none other than the morphism `(12.3.4.2)` sought, the characterization of `(12.3.4.3)` following at once from
the definitions.

**Proposition (12.3.5).**

<!-- label: 0_III.12.3.5 -->

*Under the hypotheses of `(12.3.4)`, suppose in addition the sheaf of rings `𝒪_Y` coherent; then, for every coherent
`𝒪_Y`-module `ℱ`, the canonical homomorphisms `(12.3.4.1)` are bijective.*

<!-- original page 62 -->

**Proof.** The question being local on `Y`, one may suppose there exists an exact sequence `0 → ℛ → 𝒪_Y^n → ℱ → 0`, and
`ℛ` is then also a coherent `𝒪_Y`-module `(0_I, 5.3.4)`. To prove that the homomorphisms

```text
  f^*(ℰxt^p_{𝒪_Y}(ℱ, 𝒢)) → ℰxt^p_{𝒪_X}(f^*(ℱ), f^*(𝒢))
```

are bijective, we argue by induction on `p`, the proposition resulting from `(0_I, 6.7.6.1)` when `p = 0`. Now, one has
the commutative diagram

```text
   f^*(ℰxt^{p−1}_{𝒪_Y}(𝒪_Y^n, 𝒢)) → f^*(ℰxt^{p−1}_{𝒪_Y}(ℛ, 𝒢)) →^∂ f^*(ℰxt^p_{𝒪_Y}(ℱ, 𝒢)) → f^*(ℰxt^p_{𝒪_Y}(𝒪_Y^n, 𝒢))
            ↓                              ↓                              ↓                                ↓
   ℰxt^{p−1}_{𝒪_X}(𝒪_X^n, f^*(𝒢)) → ℰxt^{p−1}_{𝒪_X}(f^*(ℛ), f^*(𝒢)) →^∂ ℰxt^p_{𝒪_X}(f^*(ℱ), f^*(𝒢)) → ℰxt^p_{𝒪_X}(𝒪_X^n, f^*(𝒢))
```

since `f^*(𝒪_Y) = 𝒪_X`; as `f^*` is exact, the two rows are exact. Moreover, one has `ℰxt^p_{𝒪_Y}(𝒪_Y^n, 𝒢) = 0` for
every `p > 0` and likewise `ℰxt^p_{𝒪_X}(𝒪_X^n, f^*(𝒢)) = 0` for every `p > 0` `(T, 4.2.3)`. In view of the induction
hypothesis, the first two vertical arrows of the preceding diagram are isomorphisms, and the terms on the right are `0`,
hence `f^*(ℰxt^p_{𝒪_Y}(ℱ, 𝒢)) → ℰxt^p_{𝒪_X}(f^*(ℱ), f^*(𝒢))` is an isomorphism.

### 12.4. Hypercohomology of the direct image functor

**12.4.1.**

<!-- label: 0_III.12.4.1 -->

Let `(X, 𝒪_X)`, `(Y, 𝒪_Y)` be two ringed spaces, `f : X → Y` a morphism of ringed spaces. One can take the
*hypercohomology* of `f_*` with respect to any complex of `𝒪_X`-modules `𝒦^• = (𝒦^i)_{i ∈ ℤ}` `(11.4.4)`, for in the
abelian category of `𝒪_Y`-modules, filtered inductive limits exist and are exact `(T, 3.1.1)`. The `𝒪_Y`-modules of
hypercohomology `R^p f_*(𝒦^•)` will also be denoted `ℋ^p(f, 𝒦^•)` or `ℋ^p(𝒦^•)`. Recall that `ℋ^•(f, 𝒦^•)` is the
cohomology of the bicomplex of `𝒪_Y`-modules `f_*(ℒ^{••})`, where `ℒ^{••}` is an injective Cartan–Eilenberg resolution
of `𝒦^•` in the category of `𝒪_X`-modules; `ℋ^•(f, 𝒦^•)` is the abutment of two spectral sequences `'ℰ(f, 𝒦^•)` and
`″ℰ(f, 𝒦^•)` whose `E_2` terms are given by

```text
  'E_2^{pq} = ℋ^p(ℋ^q(f, 𝒦^•))                                               (12.4.1.1)
  ″E_2^{pq} = ℋ^p(f, ℋ^q(𝒦^•))     (= R^p f_*(ℋ^q(𝒦^•)))                     (12.4.1.2)
```

In these formulas, we have adopted the general notation `T(A^•)` for the transform of a complex by a functor `(11.2.1)`,
and one writes `ℋ^p(f, ℱ)` instead of `R^p f_*(ℱ)` for an `𝒪_X`-module `ℱ`. Recall further that the sequence
`'ℰ(f, 𝒦^•)` is always *regular*; the two spectral sequences `'ℰ(f, 𝒦^•)` and `″ℰ(f, 𝒦^•)` are *biregular* when `𝒦^•` is
bounded below,

<!-- original page 63 -->

or when there exists an integer `m` such that every `𝒪_X`-module admits a flasque resolution of length `≤ m` `(11.4.4)`.

**12.4.2.**

<!-- label: 0_III.12.4.2 -->

We shall likewise denote by `H^•(X, 𝒦^•)` the hypercohomology of the functor `Γ` with respect to a complex `𝒦^•` of
`𝒪_X`-modules; the `H^p(X, 𝒦^•)` are therefore `Γ(X, 𝒪_X)`-modules. One can moreover consider `H^•(X, 𝒦^•)` as a
particular case of `ℋ^•(f, 𝒦^•)`, where `f` is a morphism of `(X, 𝒪_X)` to a ringed space reduced to a point endowed
with the ring `Γ(X, 𝒪_X)`.

For every open set `V` of `X`, we shall write `H^•(V, 𝒦^•)` instead of `H^•(V, 𝒦^• ∣ V)`.

**Proposition (12.4.3).**

<!-- label: 0_III.12.4.3 -->

*For every integer `p ∈ ℤ`, the `𝒪_Y`-module `ℋ^p(f, 𝒦^•)` is canonically isomorphic to the sheaf associated to the
presheaf `U ↦ H^p(f^{-1}(U), 𝒦^•)` on `Y`.*

**Proof.** Indeed, with the notation of `(12.4.1)`, the cohomology sheaf `ℋ^p(f_*(ℒ^{••}))` is associated to the
presheaf `U ↦ H^p(Γ(U, f_*(ℒ^{••}))) = H^p(Γ(f^{-1}(U), ℒ^{••}))`. But it is clear that `ℒ^{••} ∣ f^{-1}(U)` is an
injective Cartan–Eilenberg resolution of `𝒦^• ∣ f^{-1}(U)` `(T, 3.1.3)`, so
`H^p(Γ(f^{-1}(U), ℒ^{••})) = H^p(f^{-1}(U), 𝒦^•)` by definition.

**Proposition (12.4.4).**

<!-- label: 0_III.12.4.4 -->

*The hypercohomology `ℋ^•(f, 𝒦^•)` is a cohomological functor in `𝒦^•` in each of the following cases:*

*a) `𝒦^•` varies in the category of complexes bounded below.*

*b) There exists an integer `m` such that every `𝒪_X`-module admits a flasque resolution of length `≤ m`.*

*c) `X` is a Noetherian space.*

**Proof.** Cases *a)* and *b)* are particular cases of `(11.5.4)`. On the other hand, case *c)* follows from `(11.5.2)`,
for one knows that in this case the functor `f_*` commutes with inductive limits `(G, II, 3.10.1)`.

**12.4.5.**

<!-- label: 0_III.12.4.5 -->

Consider now an open cover `𝔘 = (U_α)` of `X`, and for every complex of presheaves `𝒦^• = (𝒦^j)` on `X`, the bicomplex
`C^•(𝔘, 𝒦^•)`, whose component of indices `(i, j)` is `C^i(𝔘, 𝒦^j)`, the group of `i`-cochains alternating in the nerve
of `𝔘` with values in `𝒦^j` `(G, II, 5.1)`. We shall say that the cohomology of this bicomplex is the *hypercohomology
of the cover `𝔘` with coefficients in `𝒦^•`*, and we shall denote it `H^•(𝔘, 𝒦^•) = H^•(C^•(𝔘, 𝒦^•))`. The Leray
spectral sequence of a cover `(T, 3.8.1 and G, II, 5.9.1)` generalizes as follows to hypercohomology:

**Proposition (12.4.6).**

<!-- label: 0_III.12.4.6 -->

*Let `𝒦^• = (𝒦^j)` be a complex of `𝒪_X`-modules. There exists a regular spectral functor in `𝒦^•` having as abutment
the hypercohomology `H^•(X, 𝒦^•)`, and whose `E_2` term is given by*

```text
  E_2^{pq} = H^p(𝔘, ℎ^q(𝒦^•))                                                (12.4.6.1)
```

*where `ℎ^q(𝒦^•)` denotes the complex of presheaves `V ↦ H^q(V, 𝒦^•)` on `X`. The preceding spectral sequence is
biregular if `𝒦^•` is bounded below.*

**Proof.** Consider an injective Cartan–Eilenberg resolution `ℒ^{••}` of `𝒦^•`, and the tricomplex
`C^•(𝔘, ℒ^{••}) = (C^i(𝔘, ℒ^{jk}))`; consider this tricomplex first as a bicomplex for the degrees `i` and `j + k`.
Since `i` takes only values `≥ 0`, the second spectral sequence of this bicomplex is regular `(11.3.3)` and degenerate,
for one has `H^q(𝔘, ℒ^{jk}) = 0` for every `q > 0`, the `𝒪_X`-modules `ℒ^{jk}` being flasque sheaves

<!-- original page 64 -->

`(G, II, 5.2.3)`. One therefore has `(11.1.6)` a canonical isomorphism `H^n(C^•(𝔘, ℒ^{••})) ⥲ H^n(Γ(X, ℒ^{••}))` (by
virtue of `(G, II, 5.2.2)`), hence by definition `(12.4.2)` an isomorphism `H^n(C^•(𝔘, ℒ^{••})) ⥲ H^n(X, 𝒦^•)`. Consider
on the other hand the tricomplex `C^•(𝔘, ℒ^{••})` as a bicomplex for the degrees `i + j` and `k`. Since `k` takes only
values `≥ 0`, the first spectral sequence of this bicomplex is always regular; it is biregular if `ℒ^{jk} = 0` for
`j < j_0`, that is, when `𝒦^•` is bounded below `(11.3.3)`. This spectral sequence is the one sought; indeed, for every
`j`, `ℒ^{j•}` is an injective resolution of `𝒦^j`; consequently, `H^q(C^•(𝔘, ℒ^{j•}))` is none other than the complex of
cochains `C^•(𝔘, ℎ^q(𝒦^j))`, which completes the proof.

**Corollary (12.4.7).**

<!-- label: 0_III.12.4.7 -->

*If, for every simplex `σ` of the nerve of `𝔘`, and for every integer `i`, one has `H^q(U_σ, 𝒦^i) = 0` for `q > 0`, then
one has a canonical isomorphism*

```text
  H^•(𝔘, 𝒦^•) ⥲ H^•(X, 𝒦^•).                                                 (12.4.7.1)
```

**Proof.** Indeed, the hypothesis entails that `C^•(𝔘, ℎ^q(𝒦^j)) = 0` for `q > 0`, hence `E_2^{pq} = 0` for `q > 0`; the
sequence `(12.4.6.1)` being degenerate and regular, the conclusion follows from the definition `(12.4.5)` of
`H^•(𝔘, 𝒦^•)` and from `(11.1.6)`.

**12.4.8.**

<!-- label: 0_III.12.4.8 -->

Let `(X', 𝒪_{X'})` be a second ringed space, and let `f = (ψ, θ)` be a morphism from `X'` to `X`. By the same method as
in `(12.1.3)` and `(12.1.4)`, one defines a di-homomorphism for the hypercohomology of a complex `𝒦^•` of `𝒪_X`-modules

```text
  H^p(X, 𝒦^•) → H^p(X', f^*(𝒦^•)).                                           (12.4.8.1)
```

One starts from a Cartan–Eilenberg injective resolution `ℒ^{••}` of `𝒦^•`, and since `ψ^*` is exact, `ψ^*(ℒ^{••})` is a
Cartan–Eilenberg resolution of `ψ^*(𝒦^•)` in the category of `ψ^*(𝒪_X)`-modules; there is then a morphism
`ψ^*(ℒ^{••}) → ℒ'^{••}`, where `ℒ'^{••}` is a Cartan–Eilenberg injective resolution of `ψ^*(𝒦^•)`, and from this one
deduces a morphism for cohomology `H^•(X, 𝒦^•) → H^•(X', ψ^*(𝒦^•))`; by composition with the morphism deduced by
functoriality from `ψ^*(𝒦^•) → f^*(𝒦^•)`, one obtains the morphism `(12.4.8.1)` sought.

Starting from `(12.4.8.1)` and `(12.4.3)`, one can then, reasoning as in `(12.2.5)`, define, for two morphisms
`f : X → Y`, `g : Y → Z` of ringed spaces, homomorphisms for the hypercohomology of a complex `𝒦^•` of `𝒪_X`-modules

```text
  ℋ^n(g, f_*(𝒦^•)) → ℋ^n(h, 𝒦^•)                                             (12.4.8.2)
  ℋ^n(h, 𝒦^•) → g_*(ℋ^n(f, 𝒦^•)).                                            (12.4.8.3)
```

We leave the details of the definitions to the reader.

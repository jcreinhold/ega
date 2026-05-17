# §4. Projective bundles. Ample sheaves

## 4.1. Definition of projective bundles

**Definition.**

<!-- label: II.4.1.1 -->

Let `Y` be a prescheme, `𝓔` a quasi-coherent `𝒪_Y`-module, and `𝕊_{𝒪_Y}(𝓔)` the symmetric `𝒪_Y`-algebra of `𝓔` (1.7.4),
which is quasi-coherent (1.7.7). We call the _projective bundle over `Y` defined by `𝓔`_, and denote by `ℙ(𝓔)`, the
`Y`-scheme `P = Proj(𝕊_{𝒪_Y}(𝓔))`. The `𝒪_P`-module `𝒪_P(1)` is called the _tautological sheaf on `P`_.

> _Translator's note._ EGA's 1961 term `faisceau fondamental` (literally "fundamental sheaf") is the modern
> _tautological line bundle_, or _Serre line bundle_, `𝒪_{ℙ(𝓔)}(1)`. We render it as "tautological sheaf" throughout §4;
> the term is recorded in the ledger under §4.1.1.

When `Y` is affine of ring `A`, we have `𝓔 = Ẽ` for some `A`-module `E`, and we then write `ℙ(E)` in place of `ℙ(Ẽ)`.

When we take `𝓔 = 𝒪_Y^n`, we write `ℙ_Y^{n−1}` in place of `ℙ(𝓔)`; if in addition `Y` is affine of ring `A`, we also
write `ℙ_A^{n−1}` in place of `ℙ_Y^{n−1}`. Since `𝕊_{𝒪_Y}(𝒪_Y)` is canonically identified with `𝒪_Y[T]` (1.7.4), `ℙ_Y^0`
is canonically identified with `Y` (3.1.7); the example (2.4.3) is then nothing but `ℙ_K^1`.

**(4.1.2)**

<!-- label: II.4.1.2 -->

Let `𝓔`, `𝓕` be two quasi-coherent `𝒪_Y`-modules and `u : 𝓔 → 𝓕` an `𝒪_Y`-homomorphism; there is canonically associated
to it a homomorphism `𝕊(u) : 𝕊_{𝒪_Y}(𝓔) → 𝕊_{𝒪_Y}(𝓕)` of graded `𝒪_Y`-algebras (1.7.4). If `u` is _surjective_, then so
is `𝕊(u)`, and therefore (3.6.2, (i)) `Proj(𝕊(u))` is a _closed immersion_ `ℙ(𝓕) → ℙ(𝓔)`, which we denote by `ℙ(u)`. We
may therefore say that `ℙ(𝓔)` is a _contravariant functor_ in `𝓔`, provided we restrict the morphisms of quasi-coherent
`𝒪_Y`-modules to the surjective homomorphisms.

Still supposing `u` surjective and setting `P = ℙ(𝓔)`, `Q = ℙ(𝓕)`, and `j = ℙ(u)`, we have, up to isomorphism,

```text
  j*(𝒪_P(n)) = 𝒪_Q(n)            for all n ∈ ℤ,                            (4.1.2.1)
```

as follows from (3.6.3).

**(4.1.3)**

<!-- label: II.4.1.3 -->

Now let `ψ : Y' → Y` be a morphism and set `𝓔' = ψ*(𝓔)`; we then have `𝕊_{𝒪_{Y'}}(𝓔') = ψ*(𝕊_{𝒪_Y}(𝓔))` (1.7.5); hence
(3.5.3),

```text
  ℙ(ψ*(𝓔)) = ℙ(𝓔) ×_Y Y'                                                   (4.1.3.1)
```

up to canonical isomorphism. Furthermore, we evidently have

```text
  ψ*((𝕊_{𝒪_Y}(𝓔))(n)) = (𝕊_{𝒪_{Y'}}(𝓔'))(n)
```

for all `n ∈ ℤ`; setting `P = ℙ(𝓔)` and `P' = ℙ(𝓔')`, we therefore have (3.5.4), up to isomorphism,

```text
  𝒪_{P'}(n) = 𝒪_P(n) ⊗_Y 𝒪_{Y'}    for all n ∈ ℤ.                          (4.1.3.2)
```

<!-- original page 72 -->

**Proposition.**

<!-- label: II.4.1.4 -->

Let `ℒ` be an invertible `𝒪_Y`-module. For every quasi-coherent `𝒪_Y`-module `𝓔`, there exists a canonical
`Y`-isomorphism `i_ℒ : ℙ(𝓔) ⥲ ℙ(𝓔 ⊗ ℒ)`; furthermore, setting `P = ℙ(𝓔)` and `Q = ℙ(𝓔 ⊗ ℒ)`, `i_ℒ*(𝒪_Q(n))` is
canonically isomorphic to `𝒪_P(n) ⊗_Y ℒ^{⊗n}` for all `n ∈ ℤ`.

**Proof.** Note first that if `A` is a ring, `E` an `A`-module, and `L` a _free monogenic_ `A`-module, one canonically
defines a homomorphism of `A`-modules

```text
  𝕊_n(E ⊗ L) → 𝕊_n(E) ⊗ L^{⊗n}
```

by sending `(x_1 ⊗ y_1) ⋯ (x_n ⊗ y_n)` to

```text
  (x_1 x_2 ⋯ x_n) ⊗ (y_1 ⊗ y_2 ⊗ ⋯ ⊗ y_n)         (x_i ∈ E, y_i ∈ L, for 1 ≤ i ≤ n).
```

One verifies immediately (by reducing to the case `L = A`) that this homomorphism is in fact an isomorphism. We conclude
a canonical isomorphism of graded `A`-algebras `𝕊_A(E ⊗ L) ⥲ ⊕_{n≥0} 𝕊_n(E) ⊗ L^{⊗n}`. Returning to the situation of
(4.1.4), the preceding remarks allow us to define a canonical isomorphism of graded `𝒪_Y`-algebras

```text
  𝕊_{𝒪_Y}(𝓔 ⊗_{𝒪_Y} ℒ) ⥲ ⊕_{n≥0} 𝕊_n(𝓔) ⊗_{𝒪_Y} ℒ^{⊗n}                    (4.1.4.1)
```

by defining this isomorphism as one of presheaves and using (1.7.4), `(I, 1.3.9)`, and `(I, 1.3.12)`. The proposition
then follows from (3.1.8, (iii)) and (3.2.10).

**(4.1.5)**

<!-- label: II.4.1.5 -->

With the hypotheses of (4.1.1), set `P = ℙ(𝓔)` and denote by `p` the structure morphism `P → Y`. Since by definition
`𝓔 = (𝕊_{𝒪_Y}(𝓔))_1`, we have a canonical homomorphism `α_1 : 𝓔 → p_*(𝒪_P(1))` (3.3.2.2), and therefore also
`(0, 4.4.3)` a canonical homomorphism

```text
  α_1♯ : p*(𝓔) → 𝒪_P(1).                                                   (4.1.5.1)
```

**Proposition.**

<!-- label: II.4.1.6 -->

The canonical homomorphism (4.1.5.1) is surjective.

**Proof.** We saw in (3.3.2) that `α_1♯` corresponds functorially to the canonical homomorphism
`𝓔 ⊗_{𝒪_Y} 𝕊_{𝒪_Y}(𝓔) → (𝕊_{𝒪_Y}(𝓔))(1)`; since by definition `𝓔` generates `𝕊_{𝒪_Y}(𝓔)`, this homomorphism is
surjective, whence the conclusion by (3.2.4).

## 4.2. Morphisms from a prescheme to a projective bundle

**(4.2.1)**

<!-- label: II.4.2.1 -->

Keeping the notation of (4.1.5), let `X` be a `Y`-prescheme, `q : X → Y` its structure morphism, and `r : X → P` a
`Y`-_morphism_, so that we have the commutative diagram

```text
         r
   P ←─────── X
    \       /
   p \     / q
      ↘   ↙
        Y
```

<!-- original page 73 -->

Since the functor `r*` is right exact `(0, 4.3.1)`, from the surjective homomorphism (4.1.5.1) we obtain a surjective
homomorphism

```text
  r*(α_1♯) : r*(p*(𝓔)) → r*(𝒪_P(1)).
```

But `r*(p*(𝓔)) = q*(𝓔)`, and `r*(𝒪_P(1))` is locally isomorphic to `r*(𝒪_P) = 𝒪_X`, in other words an _invertible_ sheaf
`ℒ_r` on `𝒪_X`. We have thus defined, starting from `r`, a canonical surjective `𝒪_X`-homomorphism

```text
  φ_r : q*(𝓔) → ℒ_r.                                                       (4.2.1.1)
```

When `Y = Spec(A)` is affine and `𝓔 = Ẽ`, this homomorphism may be made more explicit as follows: given `f ∈ E`, it
follows from (2.6.3) that

```text
  r⁻¹(D₊(f)) = X_{φ_r♭(f)}.                                                (4.2.1.2)
```

Let `V` be an affine open of `X` contained in `r⁻¹(D₊(f))`, and let `B` be its ring, an `A`-algebra; set `S = 𝕊_A(E)`.
The restriction of `r` to `V` corresponds to an `A`-homomorphism `ω : S_{(f)} → B`; we have `q*(𝓔)|V = (E ⊗_A B)~` and
`ℒ_r|V = L̃_r`, where `L_r = (S(1))_{(f)} ⊗_{S_{(f)}} B_{[ω]}` `(I, 1.6.5)`. The restriction of `φ_r` to `q*(𝓔)|V`
corresponds to the `B`-homomorphism `u : E ⊗_A B → L_r` sending `x ⊗ 1` to `(x/1) ⊗ f = (f/1) ⊗ ω(x/f)`. The canonical
extension of `φ_r` to a homomorphism of `𝒪_X`-algebras

```text
  ψ_r : q*(𝕊(𝓔)) = 𝕊(q*(𝓔)) → 𝕊(ℒ_r) = ⊕_{n≥0} ℒ_r^{⊗n}
```

is thus such that the restriction of `ψ_r` to `q*(𝕊_n(𝓔))|V` corresponds to the homomorphism
`𝕊_n(E ⊗_A B) = 𝕊_n(E) ⊗_A B → L_r^{⊗n}` sending `s ⊗ 1` to `(f/1)^{⊗n} ⊗ ω(s/f^n)`.

**(4.2.2)**

<!-- label: II.4.2.2 -->

Conversely, suppose given a morphism `q : X → Y`, an invertible `𝒪_X`-module `ℒ`, and a quasi-coherent `𝒪_Y`-module `𝓔`;
to a homomorphism `φ : q*(𝓔) → ℒ` there canonically corresponds a homomorphism of quasi-coherent `𝒪_X`-algebras

```text
  ψ : 𝕊(q*(𝓔)) = q*(𝕊(𝓔)) → ⊕_{n≥0} ℒ^{⊗n}
```

and therefore (3.7.1) a `Y`-morphism `r_{ℒ,ψ} : G(ψ) → Proj(𝕊(𝓔)) = ℙ(𝓔)`, which we denote `r_{ℒ,φ}`. If `φ` is
surjective, then so is `ψ`, and therefore (3.7.4) `r_{ℒ,φ}` is _everywhere defined_. Moreover, with the notation of
(4.2.1) and (4.2.2):

**Proposition.**

<!-- label: II.4.2.3 -->

Given a morphism `q : X → Y` and a quasi-coherent `𝒪_Y`-module `𝓔`, the maps `r ↦ (ℒ_r, φ_r)` and `(ℒ, φ) ↦ r_{ℒ,φ}` put
into bijective correspondence the set of `Y`-morphisms `r : X → ℙ(𝓔)` and the set of equivalence classes of pairs
`(ℒ, φ)` consisting of an invertible `𝒪_X`-module `ℒ` and a surjective homomorphism `φ : q*(𝓔) → ℒ`, two pairs `(ℒ, φ)`
and `(ℒ', φ')` being equivalent if there exists an `𝒪_X`-isomorphism `τ : ℒ ⥲ ℒ'` such that `φ' = τ ∘ φ`.

**Proof.** Start first from a `Y`-morphism `r : X → ℙ(𝓔)`, form `ℒ_r` and `φ_r` (4.2.1), and set `r' = r_{ℒ_r, φ_r}`; it
follows at once from (4.2.1) and (3.7.2) that the morphisms `r` and `r'` are identical (taking as generator of `ℒ_r` the
element `(f/1) ⊗ 1` in order to define the homomorphisms `v_n` of (3.7.2)). Conversely, start from a pair `(ℒ, φ)` and
form

<!-- original page 74 -->

`r'' = r_{ℒ,φ}`, then `ℒ_{r''}` and `φ_{r''}`; we show there is a canonical isomorphism `τ : ℒ_{r''} ⥲ ℒ` such that
`φ = τ ∘ φ_{r''}`. To define it we may place ourselves in the case `Y = Spec(A)`, `X = Spec(B)` affine, and (with the
notation of (4.2.1) and (3.7.2)) assign to each element `(x/1) ⊗ 1` of `L_{r''}` (with `x ∈ E`) the element `v_1(x) c`
of `L`. One verifies at once that `τ` does not depend on the chosen generator `c` of `L`; since `v_1` is surjective by
hypothesis, to prove `τ` is an isomorphism it suffices to show that if `x/1 = 0` in `(S(1))_{(f)}`, then `v_1(x)/1 = 0`
in `B_g`; but the first relation says that `f^n x = 0` in `𝕊_{n+1}(E)` for some `n`, whence
`v_{n+1}(f^n x) = g^n v_1(x) = 0` in `B`, whence the conclusion. Finally, it is immediate that for two equivalent pairs
`(ℒ, φ)` and `(ℒ', φ')` we have `r_{ℒ,φ} = r_{ℒ',φ'}`.

In particular, for `X = Y`:

**Theorem.**

<!-- label: II.4.2.4 -->

The set of `Y`-sections of `ℙ(𝓔)` is in canonical bijective correspondence with the set of quasi-coherent
sub-`𝒪_Y`-modules `𝓕` of `𝓔` such that `𝓔/𝓕` is invertible.

Note that this property corresponds to the classical definition of "projective space" as the set of hyperplanes of a
vector space (the classical case corresponds to `Y = Spec(K)`, `K` a field, and `𝓔 = Ẽ`, `E` a finite-dimensional
`K`-vector space; the `𝓕` with the property stated in (4.2.4) then correspond to the hyperplanes of `E`, and we know on
the other hand that the `Y`-sections of `ℙ(𝓔)` are then the `K`-rational points of `ℙ(𝓔)` `(I, 3.4.5)`).

**Remark.**

<!-- label: II.4.2.5 -->

Since there is a canonical bijective correspondence between `Y`-morphisms from `X` to `P` and their graph morphisms, the
`X`-sections of `P ×_Y X` `(I, 3.3.14)`, we see that conversely (4.2.3) can be deduced from (4.2.4). Denote by
`Hyp_Y(X, 𝓔)` the set of quasi-coherent sub-`𝒪_X`-modules `𝓕` of `𝓔 ⊗_Y 𝒪_X = q*(𝓔)` such that `q*(𝓔)/𝓕` is an
invertible `𝒪_X`-module. If `g : X' → X` is a `Y`-morphism, the right-exactness of `g*` gives
`g*(q*(𝓔)/𝓕) = g*(q*(𝓔))/g*(𝓕)`, so the latter sheaf is invertible, and therefore `Hyp_Y(X, 𝓔)` is a _contravariant
functor_ on the category of `Y`-preschemes. The theorem (4.2.4) may then be interpreted as defining a _canonical
isomorphism_ of functors `Hom_Y(X, ℙ(𝓔))` and `Hyp_Y(X, 𝓔)`, contravariant in the variable `X` over the category of
`Y`-preschemes. This also gives a characterization of the projective bundle `P = ℙ(𝓔)` by the following _universal
property_, closer to geometric intuition than the constructions of §§2 and 3: for every morphism `q : X → Y` and every
invertible `𝒪_X`-module `ℒ` that is a quotient of `𝓔 ⊗_{𝒪_Y} 𝒪_X`, there exists a unique `Y`-morphism `r : X → P` such
that `ℒ = r*(𝒪_P(1))`.

We shall see later how, in the same way, one may define, among other things, the "Grassmannian" schemes.

**Corollary.**

<!-- label: II.4.2.6 -->

Suppose every invertible `𝒪_Y`-module is trivial `(I, 2.4.8)`. Let `V` be the group `Hom_{𝒪_Y}(𝓔, 𝒪_Y)`, regarded as a
module over the ring `A = Γ(Y, 𝒪_Y)`, and let `V*` be the subset of `V` formed by the surjective homomorphisms. Then the
set of `Y`-sections of `ℙ(𝓔)` is canonically identified with `V*/A*`, where `A*` is the group of units of `A`.

<!-- original page 75 -->

In particular:

1. Corollary (4.2.6) applies whenever `Y` is a _local scheme_ `(I, 2.4.8)`. Let `Y` be an arbitrary prescheme, `y` a
    point of `Y`, and `Y' = Spec(κ(y))`; the fibre `p⁻¹(y)` of `ℙ(𝓔)` is, by (4.1.3.1), identified with `ℙ(𝓔^y)`, where
    `𝓔^y = 𝓔_y ⊗_{𝒪_y} κ(y) = 𝓔_y / 𝔪_y 𝓔_y` is regarded as a vector space over `κ(y)`. More generally, if `K` is an
    extension of `κ(y)`, then `p⁻¹(y) ⊗_{κ(y)} K` is identified with `ℙ(𝓔^y ⊗_{κ(y)} K)`. Corollary (4.2.6) therefore
    shows that the set of geometric points of `ℙ(𝓔)` with values in the extension `K` of `κ(y)` `(I, 3.4.5)`, which one
    may also call the _rational geometric fibre over `K` of `ℙ(𝓔)` over the point `y`_, is identified with the
    _projective space_ associated to the _dual_ of the `K`-vector space `𝓔^y ⊗_{κ(y)} K`.
1. Suppose `Y` is affine of ring `A`, and that every invertible `𝒪_Y`-module is trivial; take in addition `𝓔 = 𝒪_Y^n`.
    Then in (4.2.6), `V` is identified with `A^n` `(I, 1.3.8)`, and `V*` with the set of systems `(f_i)_{1≤i≤n}` of
    elements of `A` generating the ideal `A`; two such systems define the same `Y`-section of `ℙ_Y^{n−1} = ℙ_A^{n−1}` —
    in other words, the same _point of `ℙ_A^{n−1}` with values in `A`_ — if and only if one is obtained from the other
    by multiplication by an invertible element of `A`.

These properties justify the terminology "projective bundle" for `ℙ(𝓔)`. Note that the definition of "projective space"
so obtained is in fact _dual_ to the classical definition; this is forced upon us by the need to define `ℙ(𝓔)` for an
_arbitrary_ quasi-coherent `𝒪_Y`-module `𝓔`, not necessarily locally free.

**Remark.**

<!-- label: II.4.2.7 -->

We shall see in Chapter V that, if `Y` is locally Noetherian and connected and `𝓔` is locally free, then, setting
`P = ℙ(𝓔)`, every invertible `𝒪_P`-module `ℒ` is isomorphic to one of the form `ℒ' ⊗_{𝒪_Y} 𝒪_P(m)`, where `ℒ'` is an
invertible `𝒪_Y`-module, well-determined up to isomorphism, and `m` is a well-determined integer. In other words,
`H¹(P, 𝒪_P*)` is isomorphic to `ℤ × H¹(Y, 𝒪_Y*)` `(0, 5.4.7)`. We shall also see
`(III, 2.1.14, taking (0, 5.4.10) into account)` that `p_*(ℒ^{⊗m}) = 0` for `m < 0` and `p_*(ℒ^{⊗m})` is isomorphic to
`ℒ' ⊗_{𝒪_Y} (𝕊_{𝒪_Y}(𝓔))_m` for `m ≥ 0`. If `𝓕` is a quasi-coherent `𝒪_Y`-module, every `Y`-morphism `ℙ(𝓕) → ℙ(𝓔)` is
therefore determined by the data of an invertible `𝒪_Y`-module `ℒ'`, an integer `m ≥ 0`, and an `𝒪_Y`-homomorphism
`ψ : 𝓕 → ℒ' ⊗_{𝒪_Y} (𝕊_{𝒪_Y}(𝓔))_m` such that the corresponding homomorphism `ψ♯` of `𝒪_{ℙ(𝓕)}`-modules is surjective.
We shall also see that if the `Y`-morphism in question is an isomorphism, then `m = 1` and `𝓕` is isomorphic to
`𝓔 ⊗_{𝒪_Y} ℒ'` (the converse of (4.1.4)). This will let us determine the sheaf of germs of automorphisms of `ℙ(𝓔)` as
the quotient of the sheaf of groups `𝓐𝓾𝓽(𝓔)` (which is locally isomorphic to `GL(n, 𝒪_Y)` if `𝓔` is of rank `n`) by
`𝒪_Y*`.

**(4.2.8)**

<!-- label: II.4.2.8 -->

Keeping the notation of (4.2.1), let `u : X' → X` be a morphism; if the `Y`-morphism `r : X → P` corresponds to the
homomorphism `φ : q*(𝓔) → ℒ`, then the `Y`-morphism `r ∘ u` corresponds to `u*(φ) : u*(q*(𝓔)) → u*(ℒ)`, as follows
immediately from the definitions.

**(4.2.9)**

<!-- label: II.4.2.9 -->

Let `𝓔`, `𝓕` be two quasi-coherent `𝒪_Y`-modules, `v : 𝓔 → 𝓕` a surjective homomorphism, and `j = ℙ(v)` the
corresponding closed immersion `ℙ(𝓕) → ℙ(𝓔)` (4.1.2). If the `Y`-morphism `r : X → ℙ(𝓕)` corresponds to the homomorphism
`φ : q*(𝓕) → ℒ`, then the

<!-- original page 76 -->

`Y`-morphism `j ∘ r` corresponds to `q*(𝓔) ─q*(v)→ q*(𝓕) ─φ→ ℒ`; this again follows from the definition given in
(4.2.1).

**(4.2.10)**

<!-- label: II.4.2.10 -->

Let `ψ : Y' → Y` be a morphism, and set `𝓔' = ψ*(𝓔)`. If the `Y`-morphism `r : X → P` corresponds to the homomorphism
`φ : q*(𝓔) → ℒ`, then the `Y'`-morphism

```text
  r_{(Y')} : X_{(Y')} → P' = ℙ(𝓔')
```

corresponds to `φ_{(Y')} : q_{(Y')}*(𝓔') = q*(𝓔) ⊗_Y 𝒪_{Y'} → ℒ ⊗_Y 𝒪_{Y'}`. Indeed, by (4.1.3.1) we have the
commutative diagram

```text
   Y' ←─── P' = P_{(Y')} ←─── X_{(Y')}
   │           │                │
   │           │ u              │ v
   ↓           ↓                ↓
   Y  ←─── P            ←─── X
              p              r
```

By (4.1.3.2),

```text
  (r_{(Y')})*(𝒪_{P'}(1)) = (r_{(Y')})*(u*(𝒪_P(1))) = v*(r*(𝒪_P(1)))
                         = v*(ℒ) = ℒ ⊗_Y 𝒪_{Y'};
```

on the other hand, `u*(α_1♯)` is precisely the canonical homomorphism `α_1♯ : (p_{(Y')})*(𝓔') → 𝒪_{P'}(1)`, as one sees
by making the canonical homomorphisms `α_1♯` for `P` and `P'` explicit as in (4.1.6). Whence our assertion.

## 4.3. The Segre morphism

**(4.3.1)**

<!-- label: II.4.3.1 -->

Let `Y` be a prescheme and `𝓔`, `𝓕` two quasi-coherent `𝒪_Y`-modules; set `P_1 = ℙ(𝓔)`, `P_2 = ℙ(𝓕)`, and let
`p_1 : P_1 → Y`, `p_2 : P_2 → Y` be the structure morphisms. Let `Q = P_1 ×_Y P_2`, and let `q_1 : Q → P_1`,
`q_2 : Q → P_2` be the canonical projections; the `𝒪_Q`-module
`ℒ = 𝒪_{P_1}(1) ⊗_Y 𝒪_{P_2}(1) = q_1*(𝒪_{P_1}(1)) ⊗_{𝒪_Q} q_2*(𝒪_{P_2}(1))` is invertible, as the tensor product of two
invertible `𝒪_Q`-modules `(0, 5.4.4)`. On the other hand, if `r = p_1 ∘ q_1 = p_2 ∘ q_2` is the structure morphism
`Q → Y`, then `r*(𝓔 ⊗_{𝒪_Y} 𝓕) = q_1*(p_1*(𝓔)) ⊗_{𝒪_Q} q_2*(p_2*(𝓕))` `(0, 4.3.3)`. The canonical surjective
homomorphisms (4.1.5.1) `p_1*(𝓔) → 𝒪_{P_1}(1)` and `p_2*(𝓕) → 𝒪_{P_2}(1)` therefore yield, by tensor product, a
canonical homomorphism

```text
  s : r*(𝓔 ⊗_{𝒪_Y} 𝓕) → ℒ                                                   (4.3.1.1)
```

which is evidently surjective; from this we obtain (4.2.2) a canonical morphism, called the _Segre morphism_:

```text
  ς : ℙ(𝓔) ×_Y ℙ(𝓕) → ℙ(𝓔 ⊗_{𝒪_Y} 𝓕).                                       (4.3.1.2)
```

Let us make `ς` explicit when `Y = Spec(A)` is affine, `𝓔 = Ẽ`, `𝓕 = F̃`, with `E`, `F` two `A`-modules, so that
`𝓔 ⊗_{𝒪_Y} 𝓕 = (E ⊗_A F)~` `(I, 1.3.12)`; set `R = 𝕊_A(E)`, `S = 𝕊_A(F)`, `T = 𝕊_A(E ⊗_A F)`. Let `f ∈ E`, `g ∈ F`, and
consider the affine open

```text
  D₊(f) ×_Y D₊(g) = Spec(B)
```

<!-- original page 77 -->

of `Q`, where `B = R_{(f)} ⊗_A S_{(g)}`; the restriction of `ℒ` to this affine open is `L̃`, where

```text
  L = (R(1))_{(f)} ⊗_A (S(1))_{(g)},
```

and the element `c = (f/1) ⊗ (g/1)` is a generator of `L`, regarded as a free `B`-module (2.5.7). The homomorphism
(4.3.1.1) corresponds to the homomorphism

```text
  (x ⊗ y) ⊗ b ↦ b ((x/1) ⊗ (y/1))
```

from `(E ⊗_A F) ⊗_A B` to `L`. With the notation of (3.7.2) we therefore have `v_1(x ⊗ y) = (x/f) ⊗ (y/g)`; the
restriction of `ς` to `D₊(f) ×_Y D₊(g)` is a morphism of this affine scheme to `D₊(f ⊗ g)`, corresponding to the ring
homomorphism `ω : T_{(f⊗g)} → R_{(f)} ⊗_A S_{(g)}` defined by

```text
  ω((x ⊗ y)/(f ⊗ g)) = (x/f) ⊗ (y/g)                                       (4.3.1.3)
```

for `x ∈ E` and `y ∈ F`.

**(4.3.2)**

<!-- label: II.4.3.2 -->

It follows from (4.2.3) that we have a canonical isomorphism

```text
  τ : ς*(𝒪_P(1)) ⥲ 𝒪_{P_1}(1) ⊗_Y 𝒪_{P_2}(1)                              (4.3.2.1)
```

where we have set `P = ℙ(𝓔 ⊗_{𝒪_Y} 𝓕)`. We show that, for `x ∈ Γ(Y, 𝓔)` and `y ∈ Γ(Y, 𝓕)`,

```text
  τ(α_1(x ⊗ y)) = α_1(x) ⊗ α_1(y).                                         (4.3.2.2)
```

Indeed, we reduce to the case `Y` affine, and we then have, with the notation of (4.3.1) and (2.6.2),
`α_1^{f⊗g}(x ⊗ y) = (x ⊗ y)/1` in `(T(1))_{(f⊗g)}`, `α_1^f(x) = x/1` in `(R(1))_{(f)}`, and `α_1^g(y) = y/1` in
`(S(1))_{(g)}`. The definition of `τ` given in (4.2.3) and the computation of `v_1` done in (4.3.1) prove (4.3.2.2) at
once. From this we derive

```text
  ς⁻¹(P_{x⊗y}) = (P_1)_x ×_Y (P_2)_y                                        (4.3.2.3)
```

with the notation of (3.1.4). Indeed, taking (3.3.3) into account, the formula (4.3.2.2) reduces (returning to the
affine case via `(I, 3.2.7)` and `(I, 3.2.3)`) to proving the following lemma:

**Lemma.**

<!-- label: II.4.3.2.4 -->

Let `B`, `B'` be two `A`-algebras, and set `Y = Spec(A)`, `Z = Spec(B)`, `Z' = Spec(B')`. For any `t ∈ B` and `t' ∈ B'`,
we have `D(t ⊗ t') = D(t) ×_Y D(t')`.

**Proof.** If `p : Z ×_Y Z' → Z` and `p' : Z ×_Y Z' → Z'` are the canonical projections, it follows from `(I, 1.2.2.2)`
that `p⁻¹(D(t)) = D(t ⊗ 1)` and `p'⁻¹(D(t')) = D(1 ⊗ t')`; the conclusion follows from `(I, 3.2.7)` and `(I, 1.1.9.1)`,
since `(t ⊗ 1)(1 ⊗ t') = t ⊗ t'`.

**Proposition.**

<!-- label: II.4.3.3 -->

The Segre morphism is a closed immersion.

**Proof.** The question being local on `Y`, we reduce to the case where `Y` is affine. With the notation of (4.3.1) and
(4.3.2), the `D₊(f ⊗ g)` form a basis for the topology of `P`, since the `f ⊗ g` generate `T` when `f` ranges over `E`
and `g` over `F`. On the other hand, by (4.3.2.3), `ς⁻¹(D₊(f ⊗ g)) = D₊(f) ×_Y D₊(g)`. It thus suffices `(I, 4.2.4)` to
prove that the restriction of `ς` to `D₊(f) ×_Y D₊(g)` is a closed immersion into `D₊(f ⊗ g)`. But, with the same
notation, formula (4.3.1.3) shows that `ω` is surjective, which completes the proof.

**(4.3.4)**

<!-- label: II.4.3.4 -->

The Segre morphism is functorial in `𝓔` and `𝓕`, when one restricts the

<!-- original page 78 -->

homomorphisms of quasi-coherent `𝒪_Y`-modules to surjective homomorphisms. Indeed, we must show that if `𝓔 → 𝓔'` is a
surjective `𝒪_Y`-homomorphism, then the diagram

```text
                       j × 1
   ℙ(𝓔') × ℙ(𝓕) ─────────────→ ℙ(𝓔) × ℙ(𝓕)

         │                          │
       ς │                          │ ς
         ↓                          ↓

   ℙ(𝓔' ⊗ 𝓕) ────────────────→ ℙ(𝓔 ⊗ 𝓕)
```

commutes, `j` denoting the canonical closed immersion `ℙ(𝓔') → ℙ(𝓔)`. Set `P_1' = ℙ(𝓔')` and keep the other notation of
(4.3.1); `j × 1` is a closed immersion `(I, 4.3.1)`, and up to isomorphism

```text
  (j × 1)*(𝒪_{P_1}(1) ⊗ 𝒪_{P_2}(1))
    = j*(𝒪_{P_1}(1)) ⊗ 𝒪_{P_2}(1)
    = 𝒪_{P_1'}(1) ⊗ 𝒪_{P_2}(1)
```

by (4.1.2.1) and `(I, 9.1.5)`; our assertion therefore follows from (4.2.8) and (4.2.9).

**(4.3.5)**

<!-- label: II.4.3.5 -->

With the notation of (4.3.1), let `ψ : Y' → Y` be a morphism, and set `𝓔' = ψ*(𝓔)`, `𝓕' = ψ*(𝓕)`. Then the Segre
morphism `ℙ(𝓔') × ℙ(𝓕') → ℙ(𝓔' ⊗ 𝓕')` is identified with `ς_{(Y')}`. Indeed, keeping the notation of (4.3.1), set in
addition `P_1' = ℙ(𝓔')`, `P_2' = ℙ(𝓕')`; we know (4.1.3.1) that `P_i'` is identified with `(P_i)_{(Y')}` (`i = 1, 2`),
so the structure morphism `P_1' × P_2' → Y'` is identified with `r_{(Y')}`. On the other hand, `𝓔' ⊗ 𝓕'` is identified
with `ψ*(𝓔 ⊗ 𝓕)`, so `ℙ(𝓔' ⊗ 𝓕')` is identified with `(ℙ(𝓔 ⊗ 𝓕))_{(Y')}` (4.1.3.1). Finally,
`𝒪_{P_1'}(1) ⊗_{Y'} 𝒪_{P_2'}(1) = ℒ'` is identified with `ℒ ⊗_Y 𝒪_{Y'}`, by (4.1.3.2) and `(I, 9.1.11)`. The canonical
homomorphism `(r_{(Y')})*(𝓔' ⊗ 𝓕') → ℒ'` is then identified with `s_{(Y')}`, and our assertion follows from (4.2.10).

**Remark.**

<!-- label: II.4.3.6 -->

The prescheme given by the disjoint sum of `ℙ(𝓔)` and `ℙ(𝓕)` is likewise canonically isomorphic to a _closed
subprescheme of `ℙ(𝓔 ⊕ 𝓕)`_. Indeed, the surjective homomorphisms `𝓔 ⊕ 𝓕 → 𝓔` and `𝓔 ⊕ 𝓕 → 𝓕` correspond to closed
immersions `ℙ(𝓔) → ℙ(𝓔 ⊕ 𝓕)` and `ℙ(𝓕) → ℙ(𝓔 ⊕ 𝓕)`; everything comes down to showing that the underlying spaces of the
closed subpreschemes of `ℙ(𝓔 ⊕ 𝓕)` so obtained have no point in common. The question being local on `Y`, we may adopt
the notation of (4.3.1); now `𝕊_n(E)` and `𝕊_n(F)` are identified with submodules of `𝕊_n(E ⊕ F)` whose intersection
reduces to `0`; and if `𝔭` is a graded prime ideal of `𝕊(E)` such that `𝔭 ∩ 𝕊_n(E) ≠ 𝕊_n(E)` for every `n ≥ 0`, then it
corresponds in `𝕊(E ⊕ F)` to a graded prime ideal whose trace on `𝕊_n(E)` is `𝔭 ∩ 𝕊_n(E)`, but which _contains_ `𝕊₊(F)`,
as one sees at once. Hence two points of `Proj(𝕊(E))` and `Proj(𝕊(F))` respectively cannot have the same image in
`Proj(𝕊(E ⊕ F))`.

## 4.4. Immersions into projective bundles. Very ample sheaves

**Proposition.**

<!-- label: II.4.4.1 -->

Let `Y` be a quasi-compact scheme or a prescheme whose underlying space is Noetherian, `q : X → Y` a morphism _of finite
type_, and `ℒ` an invertible `𝒪_X`-module.

1. Let `𝒮` be a quasi-coherent graded `𝒪_Y`-algebra with positive degrees, and `ψ : q*(𝒮) → ⊕_{n≥0} ℒ^{⊗n}` a
    homomorphism of graded algebras. For `r_{ℒ,ψ}` to be everywhere defined and an immersion, it is necessary

<!-- original page 79 -->

```
and sufficient that there exist an integer `n ≥ 0` and a quasi-coherent
sub-`𝒪_Y`-module `𝓔` of `𝒮_n` _of finite type_ such that the
homomorphism
`φ' = ψ_n ∘ q*(j) : q*(𝓔) → ℒ^{⊗n} = ℒ'`
(with `j` the injection `𝓔 → 𝒮_n`) is surjective and the morphism
`r_{ℒ',φ'} : X → ℙ(𝓔)` is an immersion.
```

1. Let `𝓕` be a quasi-coherent `𝒪_Y`-module, and `φ : q*(𝓕) → ℒ` a surjective homomorphism. For the morphism `r_{ℒ,φ}`
    to be an immersion `X → ℙ(𝓕)`, it is necessary and sufficient that there exist a quasi-coherent sub-`𝒪_Y`-module
    `𝓔` of `𝓕` _of finite type_ such that the homomorphism `φ' = φ ∘ q*(j) : q*(𝓔) → ℒ` (with `j : 𝓔 → 𝓕` the canonical
    injection) is surjective and `r_{ℒ,φ'} : X → ℙ(𝓔)` is an immersion.

**Proof.**

(i) The fact that `r_{ℒ,ψ}` is everywhere defined and an immersion is equivalent, by (3.8.5), to the existence of an
`n ≥ 0` and an `𝓔` such that, if `𝒮'` is the sub-algebra of `𝒮` generated by `𝓔`, the homomorphism `q*(𝓔) → ℒ^{⊗n}` is
surjective and `r_{ℒ,ψ'} : X → Proj(𝒮')` is everywhere defined and an immersion. We have on the other hand a canonical
surjective homomorphism `𝕊(𝓔) → 𝒮'`, to which corresponds a closed immersion `Proj(𝒮') → ℙ(𝓔)` (3.6.2); whence the
conclusion.

(ii) Since `𝓕` is the direct limit of its quasi-coherent submodules of finite type `𝓔_λ` `(I, 9.4.9)`, `𝕊(𝓕)` is the
direct limit of the `𝕊(𝓔_λ)`; the conclusion follows from (3.8.4), upon observing that in the proof of (3.8.4) one may
take all the `n_i` equal to `1`: indeed (assuming `Y` affine), if `r = r_{ℒ,φ}` is an immersion, then `r(X)` is a
quasi-compact subspace of `ℙ(𝓕)` that may be covered by finitely many open subsets of `ℙ(𝓕)` of the form `D₊(f)` with
`f ∈ F`, such that `D₊(f) ∩ r(X)` is closed.

**Definition.**

<!-- label: II.4.4.2 -->

Let `Y` be a prescheme, `q : X → Y` a morphism. We say that an invertible `𝒪_X`-module `ℒ` is _very ample for `q`_ (or
_very ample for `Y`_, or simply _very ample_ if no confusion results) if there exists a quasi-coherent `𝒪_Y`-module `𝓔`
and a `Y`-immersion `i` of `X` into `P = ℙ(𝓔)` such that `ℒ` is isomorphic to `i*(𝒪_P(1))`.

It is equivalent (4.2.3) to say that there exists a quasi-coherent `𝒪_Y`-module `𝓔` and a surjective homomorphism
`φ : q*(𝓔) → ℒ` such that `r_{ℒ,φ} : X → ℙ(𝓔)` is an _immersion_.

Note that the existence of a very-ample-for-`Y` `𝒪_X`-module implies that `q` is _separated_ ((3.1.3) and
`(I, 5.5.1, (i) and (ii))`).

**Corollary.**

<!-- label: II.4.4.3 -->

Suppose there exists a quasi-coherent graded `𝒪_Y`-algebra `𝒮` generated by `𝒮_1` and a `Y`-immersion
`i : X → P = Proj(𝒮)` such that `ℒ` is isomorphic to `i*(𝒪_P(1))`; then `ℒ` is very ample relative to `q`.

**Proof.** If `𝓕 = 𝒮_1`, the canonical homomorphism `𝕊(𝓕) → 𝒮` is surjective; composing the corresponding closed
immersion `Proj(𝒮) → ℙ(𝓕)` (3.6.2) with the immersion `i`, we obtain an immersion `j : X → ℙ(𝓕) = P'` such that `ℒ` is
isomorphic to `j*(𝒪_{P'}(1))` (3.6.3).

**Proposition.**

<!-- label: II.4.4.4 -->

Let `q : X → Y` be a quasi-compact morphism, and `ℒ` an invertible `𝒪_X`-module. The following properties are
equivalent:

a) `ℒ` is very ample relative to `q`. b) `q_*(ℒ)` is quasi-coherent, the canonical homomorphism `σ : q*(q_*(ℒ)) → ℒ` is
surjective, and the morphism `r_{ℒ,σ} : X → ℙ(q_*(ℒ))` is an immersion.

**Proof.** Since `q` is quasi-compact, we know `q_*(ℒ)` is quasi-coherent when `q` is separated `(I, 9.2.2)`.

<!-- original page 80 -->

We know (3.4.7) that the existence of a surjective homomorphism `φ : q*(𝓔) → ℒ` (with `𝓔` a quasi-coherent `𝒪_Y`-module)
implies that `σ` is surjective; moreover, to the factorization `q*(𝓔) → q*(q_*(ℒ)) ─σ→ ℒ` of `φ` corresponds canonically
a factorization

```text
  q*(𝕊(𝓔)) → q*(𝕊(q_*(ℒ))) → ⊕_{n≥0} ℒ^{⊗n}
```

so (3.8.3) the hypothesis that `r_{ℒ,φ}` is an immersion implies that so is `j = r_{ℒ,σ}`; moreover (4.2.4), `ℒ` is
isomorphic to `j*(𝒪_{P'}(1))` with `P' = ℙ(q_*(ℒ))`. Thus (a) and (b) are equivalent.

**Corollary.**

<!-- label: II.4.4.5 -->

Suppose `q` is quasi-compact. For `ℒ` to be very ample relative to `Y`, it is necessary and sufficient that there exist
an open cover `(U_α)` of `Y` such that `ℒ | q⁻¹(U_α)` is very ample relative to `U_α` for every `α`.

**Proof.** Indeed, condition (b) of (4.4.4) is local on `Y`.

**Proposition.**

<!-- label: II.4.4.6 -->

Let `Y` be a quasi-compact scheme or a prescheme whose underlying space is Noetherian, `q : X → Y` a morphism _of finite
type_, and `ℒ` an invertible `𝒪_X`-module. Then conditions (a) and (b) of (4.4.4) are equivalent to the following:

a') There exists a quasi-coherent `𝒪_Y`-module `𝓔` _of finite type_ and a surjective homomorphism `φ : q*(𝓔) → ℒ` such
that `r_{ℒ,φ}` is an immersion. b') There exists a coherent sub-`𝒪_Y`-module `𝓔` of `q_*(ℒ)` _of finite type_ with the
properties stated in (a').

**Proof.** It is clear that (a') or (b') implies (a); on the other hand, (a) implies (a') by (4.4.1), and similarly (b)
implies (b').

**Corollary.**

<!-- label: II.4.4.7 -->

Suppose `Y` is a quasi-compact scheme or a Noetherian prescheme. If `ℒ` is very ample for `q`, then there exists a
quasi-coherent graded `𝒪_Y`-algebra `𝒮` such that `𝒮_1` is of finite type and generates `𝒮`, and a dominant open
`Y`-immersion `i : X → P = Proj(𝒮)` such that `ℒ` is isomorphic to `i*(𝒪_P(1))`.

**Proof.** Condition (b') of (4.4.6) is satisfied; the structure morphism `p : ℙ(𝓔) = P' → Y` is then separated and of
finite type (3.1.3), so `P'` is a quasi-compact scheme (resp. a Noetherian prescheme) if `Y` is one. Let `Z` be the
closure `(I, 9.5.11)` of the subprescheme `X'` of `P'` associated to the immersion `j = r_{ℒ,φ}` of `X` into `P'`; it is
clear that `j` factors as the canonical injection `Z → P'` followed by a dominant open immersion `i : X → Z`. But `Z` is
identified with a prescheme `Proj(𝒮)`, where `𝒮` is a graded `𝒪_Y`-algebra quotient of `𝕊(𝓔)` by a quasi-coherent graded
sheaf of ideals (3.6.2); it is clear that `𝒮_1` is of finite type and generates `𝒮`. Moreover, `𝒪_Z(1)` is the inverse
image of `𝒪_{P'}(1)` under the canonical injection (3.6.3), so `ℒ = i*(𝒪_Z(1))`.

**Proposition.**

<!-- label: II.4.4.8 -->

Let `q : X → Y` be a morphism, `ℒ` a very-ample-relative-to-`q` `𝒪_X`-module, and `ℒ'` an invertible `𝒪_X`-module such
that there exist a quasi-coherent `𝒪_Y`-module `𝓔'` and a surjective homomorphism `q*(𝓔') → ℒ'`. Then `ℒ ⊗_{𝒪_X} ℒ'` is
very ample relative to `q`.

**Proof.** The hypothesis implies the existence of a `Y`-morphism `r' : X → P' = ℙ(𝓔')` such that `ℒ' = r'*(𝒪_{P'}(1))`
(4.2.1). By hypothesis there is also a quasi-coherent `𝒪_Y`-module `𝓔` and a

<!-- original page 81 -->

`Y`-immersion `r : X → P = ℙ(𝓔)` such that `ℒ = r*(𝒪_P(1))`. Set `Q = ℙ(𝓔 ⊗ 𝓔')` and consider the Segre morphism
`ς : P ×_Y P' → Q` (4.3.1). Since `r` is an immersion, so is `(r, r')_Y : X → P ×_Y P'` `(I, 5.3.14)`; but `ς` is an
immersion (4.3.3), so `r'' : X ─(r,r')→ P ×_Y P' ─ς→ Q` is too. On the other hand (4.3.2.1), `ς*(𝒪_Q(1))` is isomorphic
to `𝒪_P(1) ⊗_Y 𝒪_{P'}(1)`, so `(I, 9.1.4)` `r''*(𝒪_Q(1))` is isomorphic to `ℒ ⊗ ℒ'`, which proves the proposition.

**Corollary.**

<!-- label: II.4.4.9 -->

Let `q : X → Y` be a morphism.

1. Let `ℒ` be an invertible `𝒪_X`-module and `𝒦` an invertible `𝒪_Y`-module. For `ℒ` to be very ample relative to `q`,
    it is necessary and sufficient that `ℒ ⊗ q*(𝒦)` be so.
1. If `ℒ` and `ℒ'` are two `𝒪_X`-modules very ample relative to `q`, then so is `ℒ ⊗ ℒ'`; in particular, `ℒ^{⊗n}` is
    very ample relative to `q` for every `n > 0`.

**Proof.** (ii) is an immediate consequence of (4.4.8), as is the necessity of (i); on the other hand, if `ℒ ⊗ q*(𝒦)` is
very ample, so is `(ℒ ⊗ q*(𝒦)) ⊗ q*(𝒦⁻¹)` by the above, and this latter `𝒪_X`-module is isomorphic to `ℒ`
`(0, 5.4.3 and 5.4.5)`.

**Proposition.**

<!-- label: II.4.4.10 -->

1. For every prescheme `Y`, every invertible `𝒪_Y`-module `ℒ` is very ample relative to the identity morphism `1_Y`.
1. (i bis) Let `f : X → Y` be a morphism and `j : X' → X` an immersion. If `ℒ` is an `𝒪_X`-module very ample relative to
    `f`, then `j*(ℒ)` is very ample relative to `f ∘ j`.
1. Let `Z` be a quasi-compact prescheme, `f : X → Y` a morphism of finite type, `g : Y → Z` a quasi-compact morphism,
    `ℒ` an `𝒪_X`-module very ample relative to `f`, and `𝒦` an `𝒪_Y`-module very ample relative to `g`. Then there
    exists an integer `n_0 > 0` such that `ℒ ⊗ f*(𝒦^{⊗n})` is very ample relative to `g ∘ f` for all `n ≥ n_0`.
1. Let `f : X → Y` and `g : Y' → Y` be morphisms, and set `X' = X_{(Y')}`. If `ℒ` is an `𝒪_X`-module very ample relative
    to `f`, then `ℒ' = ℒ ⊗_Y 𝒪_{Y'}` is an `𝒪_{X'}`-module very ample relative to `f_{(Y')}`.
1. Let `f_i : X_i → Y_i` (`i = 1, 2`) be two `S`-morphisms. If `ℒ_i` is an `𝒪_{X_i}`-module very ample relative to `f_i`
    (`i = 1, 2`), then `ℒ_1 ⊗_S ℒ_2` is very ample relative to `f_1 ×_S f_2`.
1. Let `f : X → Y` and `g : Y → Z` be morphisms. If an `𝒪_X`-module `ℒ` is very ample relative to `g ∘ f`, then `ℒ` is
    very ample relative to `f`.
1. Let `f : X → Y` be a morphism, and `j` the canonical injection `X_red → X`. If `ℒ` is an `𝒪_X`-module very ample
    relative to `f`, then `j*(ℒ)` is very ample relative to `f_red`.

**Proof.** Property (i bis) follows immediately from Definition (4.4.2), and it is immediate that (vi) follows formally
from (i bis) and (v) by an argument modeled on `(I, 5.5.12)`, which we leave to the reader. To prove (v), consider, as
in `(I, 5.5.12)`, the factorization `X ─Γ_f→ X ×_Z Y ─p_2→ Y`, noting that `p_2 = (g ∘ f) × 1_Y`. It follows from the
hypothesis and from (i) and (iv) that `ℒ ⊗_{𝒪_Z} 𝒪_Y` is very ample for `p_2`; on the other hand,
`ℒ = Γ_f*(ℒ ⊗_{𝒪_Z} 𝒪_Y)` `(I, 9.1.4)`, and `Γ_f` is an immersion `(I, 5.3.11)`; we may therefore apply (i bis).

<!-- original page 82 -->

To prove (i), we apply Definition (4.4.2) with `𝓔 = ℒ`, noting that then `ℙ(𝓔)` is identified with `Y` (4.1.4).

Let us prove (iii). There exists a quasi-coherent `𝒪_Y`-module `𝓔` and a `Y`-immersion `i : X → ℙ(𝓔) = P` such that
`ℒ = i*(𝒪_P(1))`; setting `𝓔' = g*(𝓔)`, `𝓔'` is a quasi-coherent `𝒪_{Y'}`-module, and `P' = ℙ(𝓔') = P_{(Y')}` (4.1.3.1);
`i_{(Y')}` is an immersion of `X_{(Y')}` into `P'` `(I, 4.3.2)`, and `ℒ'` is isomorphic to `(i_{(Y')})*(𝒪_{P'}(1))`
(4.2.10).

To prove (iv), note that by hypothesis there is a `Y_i`-immersion `r_i : X_i → P_i = ℙ(𝓔_i)`, where `𝓔_i` is a
quasi-coherent `𝒪_{Y_i}`-module, and `ℒ_i = r_i*(𝒪_{P_i}(1))` (`i = 1, 2`); `r_1 ×_S r_2` is an `S`-immersion of
`X_1 ×_S X_2` into `P_1 ×_S P_2` `(I, 4.3.1)`, and the inverse image of `𝒪_{P_1}(1) ⊗_S 𝒪_{P_2}(1)` under this immersion
is `ℒ_1 ⊗_S ℒ_2`. Set `T = Y_1 ×_S Y_2`, and let `p_1`, `p_2` be the projections of `T` to `Y_1`, `Y_2` respectively.
Setting `P_i' = ℙ(p_i*(𝓔_i))` (`i = 1, 2`), we have by (4.1.3.1) `P_i' = P_i ×_{Y_i} T`, whence

```text
  P_1' ×_T P_2' = (P_1 ×_{Y_1} T) ×_T (P_2 ×_{Y_2} T)
                = P_1 ×_{Y_1} (T ×_{Y_2} P_2)
                = P_1 ×_{Y_1} (Y_1 ×_S P_2)
                = P_1 ×_S P_2
```

up to canonical isomorphism. Similarly, `𝒪_{P_i'}(1) = 𝒪_{P_i}(1) ⊗_{Y_i} 𝒪_T` (4.1.3.2), and an analogous computation
(based notably on `(I, 9.1.9.1 and 9.1.2)`) shows that, in the above identification, `𝒪_{P_1'}(1) ⊗_T 𝒪_{P_2'}(1)` is
identified with `𝒪_{P_1}(1) ⊗_S 𝒪_{P_2}(1)`. We may thus regard `r_1 ×_S r_2` as a `T`-immersion of `X_1 ×_S X_2` into
`P_1' ×_T P_2'`, the inverse image of `𝒪_{P_1'}(1) ⊗_T 𝒪_{P_2'}(1)` being `ℒ_1 ⊗_S ℒ_2`. We finish the argument as in
(4.4.8) using the Segre morphism.

It remains to prove (ii). We may first restrict to the case where `Z` is an affine scheme, since in general there is a
finite cover `(U_i)` of `Z` by affine opens; if the proposition is proved for `𝒦 | g⁻¹(U_i)`, `ℒ | f⁻¹(g⁻¹(U_i))`, and
an integer `n_i`, it suffices to take `n_0` the largest of the `n_i` to obtain the result for `𝒦` and `ℒ` (4.4.5). The
hypothesis implies that `f` and `g` are separated, so `X` and `Y` are quasi-compact schemes.

There is an immersion `r : X → P = ℙ(𝓔)`, where `𝓔` is a quasi-coherent `𝒪_Y`-module of finite type, and
`ℒ = r*(𝒪_P(1))`, by (4.4.6). We shall see that there exists an `𝒪_P`-module `ℳ` very ample relative to the composed
morphism `P ─h→ Y ─g→ Z` such that `𝒪_P(1)` is isomorphic to `ℳ ⊗_Y 𝒦^{⊗(−m)}` for some integer `m`. For `n ≥ m + 1`,
`𝒪_P(1) ⊗_Y 𝒦^{⊗n}` will thus be very ample for `Z` by hypothesis and (iv) applied to the morphisms `h : P → Y` and
`1_Y`; since `r` is an immersion and `ℒ ⊗ f*(𝒦^{⊗n}) = r*(𝒪_P(1) ⊗_Y 𝒦^{⊗n})`, the conclusion will follow from (i bis).
To prove our claim about `𝒪_P(1)`, we use the following lemma:

**Lemma.**

<!-- label: II.4.4.10.1 -->

Let `Z` be a quasi-compact scheme or a prescheme whose underlying space is Noetherian, `g : Y → Z` a quasi-compact
morphism, `𝒦` an invertible `𝒪_Y`-module very ample for `g`, and `𝓔` a quasi-coherent `𝒪_Y`-module of finite type. Then
there exists an integer `m_0` such that, for every `m ≥ m_0`, `𝓔` is isomorphic to a quotient of an `𝒪_Y`-module of the
form `g*(𝓕) ⊗ 𝒦^{⊗(−m)}`, where `𝓕` is a quasi-coherent `𝒪_Z`-module of finite type (depending on `m`).

This lemma will be proved in (4.5.10.1); the reader may verify that (4.4.10) is not used anywhere in §4.5.

<!-- original page 83 -->

This lemma being granted, there is a closed immersion `j_1` of `P` into

```text
  P_1 = ℙ(g*(𝓕) ⊗ 𝒦^{⊗(−m)})
```

such that `𝒪_P(1)` is isomorphic to `j_1*(𝒪_{P_1}(1))` (4.1.2). On the other hand, there is an isomorphism from `P_1` to
`P_2 = ℙ(g*(𝓕))`, identifying `𝒪_{P_2}(1) ⊗_Y 𝒦^{⊗(−m)}` with `𝒪_{P_1}(1)` (4.1.4); we therefore have a closed immersion
`j_2 : P → P_2` such that `𝒪_P(1)` is isomorphic to `j_2*(𝒪_{P_2}(1)) ⊗_Y 𝒦^{⊗(−m)}`. Finally, `P_2` is identified with
`P_3 ×_Z Y`, where `P_3 = ℙ(𝓕)`, and `𝒪_{P_2}(1)` with `𝒪_{P_3}(1) ⊗_Z 𝒪_Y` (4.1.3). By definition, `𝒪_{P_3}(1)` is very
ample for `Z`; since so is `𝒦`, we conclude from (iv) that `𝒪_{P_2}(1) ⊗_Y 𝒦` is very ample for `Z`; so is
`ℳ = j_2*(𝒪_{P_2}(1) ⊗_Y 𝒦)` by (i bis), and `𝒪_P(1)` is isomorphic to `ℳ ⊗_Y 𝒦^{⊗(−m−1)}`, which completes the proof.

**Proposition.**

<!-- label: II.4.4.11 -->

Let `f : X → Y` and `f' : X' → Y` be two morphisms, `X''` the sum prescheme `X ⊔ X'`, and `f'' : X'' → Y` the morphism
that agrees with `f` (resp. `f'`) on `X` (resp. `X'`). Let `ℒ` (resp. `ℒ'`) be an invertible `𝒪_X`-module (resp.
`𝒪_{X'}`-module), and let `ℒ''` be the invertible `𝒪_{X''}`-module that agrees with `ℒ` on `X` and with `ℒ'` on `X'`.
For `ℒ''` to be very ample relative to `f''`, it is necessary and sufficient that `ℒ` be very ample relative to `f` and
`ℒ'` very ample relative to `f'`.

**Proof.** We reduce at once to `Y` affine. If `ℒ''` is very ample, then so are `ℒ` and `ℒ'` by (4.4.10, (i bis)).
Conversely, if `ℒ` and `ℒ'` are very ample, it follows at once from Definition (4.4.2) and from (4.3.6) that `ℒ''` is
very ample.

## 4.5. Ample sheaves

**(4.5.1)**

<!-- label: II.4.5.1 -->

Given a prescheme `X` and an invertible `𝒪_X`-module `ℒ`, we set, for every `𝒪_X`-module `𝓕` (when no confusion over `ℒ`
is possible), `𝓕(n) = 𝓕 ⊗_{𝒪_X} ℒ^{⊗n}` (`n ∈ ℤ`); we also set `S = ⊕_{n≥0} Γ(X, ℒ^{⊗n})` (a graded subring of the ring
`Γ_•(ℒ)` defined in `(0, 5.4.6)`). Regarding `X` as a `ℤ`-prescheme with `p : X → Spec(ℤ)` the structure morphism, there
is a bijective correspondence between the homomorphisms `p*(S̃) → ⊕_{n≥0} ℒ^{⊗n}` of graded `𝒪_X`-algebras and the
endomorphisms of the graded ring `S` `(I, 2.2.5)`; the homomorphism `ε : p*(S̃) → ⊕_{n≥0} ℒ^{⊗n}` corresponding in this
way to the identity automorphism of `S` is called _canonical_. It corresponds (3.7.1) to a morphism `G(ε) → Proj(S)`
which is also called _canonical_.

**Theorem.**

<!-- label: II.4.5.2 -->

Let `X` be a quasi-compact scheme or a prescheme whose underlying space is Noetherian, `ℒ` an invertible `𝒪_X`-module,
and `S` the graded ring `⊕_{n≥0} Γ(X, ℒ^{⊗n})`. The following conditions are equivalent:

a) When `f` ranges over the set of homogeneous elements of `S₊`, the `X_f` form a basis for the topology of `X`. a')
When `f` ranges over the set of homogeneous elements of `S₊`, the `X_f` that are affine form a cover of `X`. b) The
canonical morphism `G(ε) → Proj(S)` (4.5.1) is everywhere defined and is a dominant open immersion.

<!-- original page 84 -->

b') The canonical morphism `G(ε) → Proj(S)` is everywhere defined and is a homeomorphism of the underlying space of `X`
onto a subspace of `Proj(S)`. c) For every quasi-coherent `𝒪_X`-module `𝓕`, denoting by `𝓕_n` the sub-`𝒪_X`-module of
`𝓕(n)` generated by the sections of `𝓕(n)` over `X`, `𝓕` is the sum of the sub-`𝒪_X`-modules `𝓕_n(−n)` for the integers
`n > 0`. c') Property (c) holds for every quasi-coherent sheaf of ideals of `𝒪_X`.

Furthermore, if `(f_α)` is a family of homogeneous elements of `S₊` such that the `X_{f_α}` are affine, then the
restriction to `⋃_α X_{f_α}` of the canonical morphism `X → Proj(S)` is an isomorphism of `⋃_α X_{f_α}` onto
`⋃_α (Proj(S))_{f_α}`.

**Proof.** It is clear that (b) implies (b'), and (b') implies (a) by formula (3.7.3.1) (taking into account that `ε♭`
is the identity). Condition (a) implies (a'): every `x ∈ X` has an affine neighbourhood `U` such that `ℒ | U` is
isomorphic to `𝒪_X | U`; if `f ∈ Γ(X, ℒ^{⊗n})` satisfies `x ∈ X_f ⊂ U`, then `X_f` is also the set of `x' ∈ U` with
`(f | U)(x') ≠ 0`, and is therefore an affine open `(I, 1.3.6)`. To show that (a') implies (b), it suffices to prove the
last assertion of the statement, and to verify in addition that, if `X = ⋃ X_{f_α}`, condition (iv) of (3.8.2) is
satisfied. This last point follows at once from `(I, 9.3.1, (i))`. As for the last assertion of (4.5.2), since `X_{f_α}`
is the inverse image of `(Proj(S))_{f_α}` under `G(ε) → Proj(S)`, it suffices to apply `(I, 9.3.2)`. Hence (a), (a'),
(b), (b') are equivalent.

To show that (a') implies (c), note that if `X_f` is affine (with `f ∈ S_k`), then `𝓕 | X_f` is generated by its
sections over `X_f` `(I, 1.3.9)`; on the other hand `(I, 9.3.1, (ii))`, such a section `s` is of the form
`(t | X_f) ⊗ (f | X_f)^{−m}`, where `t ∈ Γ(X, 𝓕(km))`; by definition `t` is also a section of `𝓕_{km}`, so `s` is indeed
a section of `𝓕_{km}(−km)` over `X_f`, which proves (c). It is clear that (c) implies (c'), and it remains to show that
(c') implies (a). Let `U` be an open neighbourhood of `x ∈ X`, and `𝒥` a quasi-coherent sheaf of ideals of `𝒪_X`
defining a closed subprescheme of `X` with `X − U` as underlying space `(I, 5.2.1)`. Hypothesis (c') implies that there
exists an integer `n > 0` and a section `f` of `𝒥(n)` over `X` such that `f(x) ≠ 0`. But evidently `f ∈ S_n`, and
`x ∈ X_f ⊂ U`, which proves (a).

When `X` is a prescheme whose underlying space is Noetherian, the equivalent conditions of (4.5.2) imply that `X` is a
_scheme_, since it is isomorphic to a subprescheme of the scheme `S = Proj(A)` by (4.5.2, b).

**Definition.**

<!-- label: II.4.5.3 -->

We say that an invertible `𝒪_X`-module `ℒ` is _ample_ if `X` is a quasi-compact scheme and the equivalent conditions of
(4.5.2) are satisfied.

It follows evidently from criterion (4.5.2, a) that, if `ℒ` is an ample `𝒪_X`-module, then for every open `U` of `X`,
`ℒ | U` is an ample `(𝒪_X | U)`-module.

It also follows from the proof of (4.5.2) that the _affine_ `X_f` already form a basis for the topology of `X`.
Moreover:

**Corollary.**

<!-- label: II.4.5.4 -->

Let `ℒ` be an ample `𝒪_X`-module. For every finite subspace `Z` of `X` and every neighbourhood `U` of `Z`, there exists
an integer `n` and an `f ∈ Γ(X, ℒ^{⊗n})` such that `X_f` is an affine neighbourhood of `Z` contained in `U`.

<!-- original page 85 -->

**Proof.** By (4.5.2, b), it suffices to show that for every finite part `Z'` of `Proj(S)` and every open neighbourhood
`U` of `Z'`, there exists a homogeneous element `f ∈ S₊` such that `Z ⊂ (Proj(S))_f ⊂ U` (2.4.1). By definition the
closed set `Y`, complement of `U` in `Proj(S)`, is of the form `V₊(𝔍)`, where `𝔍` is a graded ideal of `S` not
containing `S₊` (2.3.2); on the other hand, the points of `Z'` are by definition graded prime ideals `𝔭_i` of `S₊` not
containing `𝔍` (2.3.1). There thus exists an element `f ∈ 𝔍` not belonging to any of the `𝔭_i` (Bourbaki, _Alg. comm._,
chap. II, §1, no. 1, prop. 2), and since the `𝔭_i` are graded, the argument _loc. cit._ shows that one may even take `f`
to be homogeneous; this element answers the question.

**Proposition.**

<!-- label: II.4.5.5 -->

Suppose `X` is a quasi-compact scheme or a prescheme whose underlying space is Noetherian. Then conditions (a) to (c')
of (4.5.2) are also equivalent to the following:

d) For every quasi-coherent `𝒪_X`-module `𝓕` of finite type, there exists an integer `n_0` such that, for every
`n ≥ n_0`, `𝓕(n)` is generated by its sections over `X`. d') For every quasi-coherent `𝒪_X`-module `𝓕` of finite type,
there exist integers `n > 0` and `k > 0` such that `𝓕` is isomorphic to a quotient of the `𝒪_X`-module
`ℒ^{⊗(−n)} ⊗ 𝒪_X^k`. d'') Property (d') holds for every quasi-coherent sheaf of ideals of `𝒪_X` of finite type.

**Proof.** Since `X` is quasi-compact, if a quasi-coherent `𝒪_X`-module `𝓕` of finite type is such that `𝓕(n)` (which is
of finite type) is generated by its sections over `X`, then `𝓕(n)` is generated by a finite number of these sections
`(0, 5.2.3)`; so (d) implies (d'), and it is clear that (d') implies (d''). Since every quasi-coherent `𝒪_X`-module `𝒢`
is the direct limit of its sub-`𝒪_X`-modules of finite type `(I, 9.4.9)`, to verify condition (c') of (4.5.2), it
suffices to do so for a quasi-coherent sheaf of ideals of `𝒪_X` of finite type, so (d'') implies (c'). It remains to see
that if `ℒ` is ample, property (d) holds. Consider a finite cover of `X` by `X_{f_i}` (`f_i ∈ S_{n_i}`) which we may
assume affine; replacing the `f_i` by suitable powers (which does not change the `X_{f_i}`), we may suppose all the
`n_i` equal to a single integer `m`. The sheaf `𝓕 | X_{f_i}`, of finite type by hypothesis, is generated by a finite
number of sections `h_{ij}` over `X_{f_i}` `(I, 1.3.13)`; so there is an integer `k_0` such that the section
`h_{ij} ⊗ f_i^{⊗k_0}` extends to a section of `𝓕(k_0 m)` over `X` for every pair `(i, j)` `(I, 9.3.1)`. _A fortiori_ the
`h_{ij} ⊗ f_i^{⊗k}` extend to sections of `𝓕(km)` over `X` for every `k ≥ k_0`, and for these values of `k`, `𝓕(km)` is
generated by its sections over `X`. For every `p` with `0 < p < m`, `𝓕(p)` is also of finite type, so there is an
integer `k_p` such that `𝓕(p)(km) = 𝓕(p + km)` is generated by its sections over `X` for `k ≥ k_p`. Taking `n_0` larger
than all the `k_p m`, we conclude that `𝓕(n)` is generated by its sections over `X` for every `n ≥ n_0`, since such an
`n` writes `n = km + p` with `k ≥ k_p` and `0 ≤ p < m`.

**Proposition.**

<!-- label: II.4.5.6 -->

Let `X` be a quasi-compact scheme and `ℒ` an invertible `𝒪_X`-module.

1. Let `n > 0` be an integer. For `ℒ` to be ample, it is necessary and sufficient that `ℒ^{⊗n}` be ample.
1. Let `ℒ'` be an invertible `𝒪_X`-module such that for every `x ∈ X` there exists an integer `n > 0`

<!-- original page 86 -->

```
and a section `s'` of `ℒ'^{⊗n}` over `X` such that `s'(x) ≠ 0`. Then
if `ℒ` is ample, so is `ℒ ⊗ ℒ'`.
```

**Proof.** Property (i) is an evident consequence of criterion (a) of (4.5.2), since `X_{f^{⊗n}} = X_f`. On the other
hand, if `ℒ` is ample, then for every `x ∈ X` and every neighbourhood `U` of `x` there is `m > 0` and `f ∈ Γ(X, ℒ^{⊗m})`
such that `x ∈ X_f ⊂ U` (4.5.2, a); if `f' ∈ Γ(X, ℒ'^{⊗n})` satisfies `f'(x) ≠ 0`, then `s(x) ≠ 0` for
`s = f^{⊗n} ⊗ f'^{⊗m} ∈ Γ(X, (ℒ ⊗ ℒ')^{⊗mn})`, so `x ∈ X_s ⊂ X_f ⊂ U`, which proves that `ℒ ⊗ ℒ'` is ample (4.5.2, a).

**Corollary.**

<!-- label: II.4.5.7 -->

The tensor product of two ample `𝒪_X`-modules is ample.

**Corollary.**

<!-- label: II.4.5.8 -->

Let `ℒ` be an ample `𝒪_X`-module and `ℒ'` an invertible `𝒪_X`-module. Then there exists an integer `n_0 > 0` such that
`ℒ^{⊗n} ⊗ ℒ'` is ample and generated by its sections over `X` for `n ≥ n_0`.

**Proof.** By (4.5.5) there is an integer `m_0` such that `ℒ^{⊗m} ⊗ ℒ'` is generated by its sections over `X` for
`m ≥ m_0`; by (4.5.6) we may then take `n_0 = m_0 + 1`.

**Remark.**

<!-- label: II.4.5.9 -->

Let `P = H¹(X, 𝒪_X*)` be the group of classes of invertible `𝒪_X`-modules `(0, 5.4.7)`, and let `P⁺` be the part of `P`
formed by the classes of ample sheaves. Suppose `P⁺` is non-empty. Then it follows from (4.5.7) and (4.5.8) that

```text
  P⁺ + P⁺ ⊂ P⁺    and    P⁺ − P⁺ = P,
```

in other words, `P⁺ ∪ {0}` is the set of positive elements in `P` for a _preorder_ structure on `P` compatible with its
group structure, which is even _archimedean_ by (4.5.8). For this reason one sometimes says "positive sheaf" instead of
ample sheaf, and "negative sheaf" for the inverse of such a sheaf (terminology that we shall not follow).

**Proposition.**

<!-- label: II.4.5.10 -->

Let `Y` be an affine scheme, `q : X → Y` a quasi-compact separated morphism, and `ℒ` an invertible `𝒪_X`-module.

1. If `ℒ` is very ample relative to `q`, then `ℒ` is ample.
1. Suppose in addition that the morphism `q` is _of finite type_. Then, for `ℒ` to be ample, it is necessary and
    sufficient that it possess one of the following equivalent properties: e) There exists `n_0 > 0` such that for
    every integer `n ≥ n_0`, `ℒ^{⊗n}` is very ample relative to `q`. e') There exists `n > 0` such that `ℒ^{⊗n}` is
    very ample relative to `q`.

**Proof.** The first claim follows from Definition (4.4.2) of a very ample `𝒪_X`-module: if `A` is the ring of `Y`,
there exists an `A`-module `E` and a surjective homomorphism

```text
  ψ : q*((𝕊(E))~) → ⊕_{n≥0} ℒ^{⊗n}
```

such that `i = r_{ℒ,ψ}` is an everywhere-defined immersion `X → P = ℙ(Ẽ)` and `ℒ = i*(𝒪_P(1))`; since the `D₊(f)` for
`f` homogeneous in `(𝕊(E))₊` form a basis of the topology of `P`, and `i⁻¹(D₊(f)) = X_{ψ♭(f)}` by (3.7.3.1), we see that
condition (a) of (4.5.2) is satisfied, so `ℒ` is ample.

Now we prove that if `q` is of finite type and `ℒ` is ample, then `ℒ` satisfies (e). First, it follows from criterion
(b) of (4.5.2) and from (4.4.1, (i)) that there exists

<!-- original page 86 -->

an integer `k_0 > 0` such that `ℒ^{⊗k_0}` is very ample relative to `q`. Also by (4.5.5) there is an integer `m_0` such
that for `m ≥ m_0`, `ℒ^{⊗m}` is generated by its sections over `X`. Set `n_0 = k_0 + m_0`; if `n ≥ n_0`, write
`n = k_0 + m` with `m ≥ m_0`, whence `ℒ^{⊗n} = ℒ^{⊗k_0} ⊗ ℒ^{⊗m}`. Since `ℒ^{⊗m}` is generated by its sections over `X`,
it follows from (4.4.8) and (3.4.7) that `ℒ^{⊗n}` is very ample relative to `q`. Finally, it is clear that (e) implies
(e'), and (e') implies that `ℒ` is ample by (i) and (4.5.6, (i)).

**(4.5.10.1)** _Proof of Lemma (4.4.10.1)._

<!-- label: II.4.5.10.1 -->

Set `𝓔(n) = 𝓔 ⊗ 𝒦^{⊗n}`; since `g` is separated (4.4.2), the argument of (3.4.8) applies and reduces matters to showing
that the canonical homomorphism `g*(g_*(𝓔(n))) → 𝓔(n)` is surjective for `n` large enough. Furthermore, since `Z` is
quasi-compact, the argument of (3.4.6) reduces the proposition to the case where `Z` is affine. But `𝒦` is then ample by
(4.5.10, (i)), and the conclusion follows from (4.5.5, d').

**Corollary.**

<!-- label: II.4.5.11 -->

Let `Y` be an affine scheme, `q : X → Y` a separated morphism of finite type, `ℒ` an ample `𝒪_X`-module, and `ℒ'` an
invertible `𝒪_X`-module. There exists an integer `n_0` such that for `n ≥ n_0`, `ℒ^{⊗n} ⊗ ℒ'` is very ample relative to
`q`.

**Proof.** There is an `m_0` such that for `m ≥ m_0`, `ℒ^{⊗m} ⊗ ℒ'` is generated by its sections over `X` (4.5.8); on
the other hand there is a `k_0` such that `ℒ^{⊗k}` is very ample relative to `q` for `k ≥ k_0`. Therefore
`ℒ^{⊗(k + m_0)} ⊗ ℒ'` is very ample for `k ≥ k_0` ((4.4.8) and (3.4.7)).

**Remark.**

<!-- label: II.4.5.12 -->

It is not known whether the hypothesis that an `𝒪_X`-module `ℒ` is such that `ℒ^{⊗n}` is very ample (relative to `q`)
implies the same conclusion for `ℒ^{⊗(n+1)}`.

**Proposition.**

<!-- label: II.4.5.13 -->

Let `X` be a quasi-compact prescheme, `Z` a closed subprescheme of `X` defined by a _nilpotent_ quasi-coherent sheaf `𝒥`
of ideals of `𝒪_X`, and `j` the canonical injection `Z → X`. For an invertible `𝒪_X`-module `ℒ` to be ample, it is
necessary and sufficient that `ℒ' = j*(ℒ)` be an ample `𝒪_Z`-module.

**Proof.** _The condition is necessary._ Indeed, for every section `f` of `ℒ^{⊗n}` over `X`, let `f'` be its canonical
image `f ⊗ 1`, a section of `ℒ'^{⊗n} = ℒ^{⊗n} ⊗_{𝒪_X} (𝒪_X/𝒥)` over the space `Z` (which is identical to `X`); it is
clear that `X_f = Z_{f'}`, so criterion (a) of (4.5.2) shows that `ℒ'` is ample.

To see that the condition is _sufficient_, note first that we may reduce to the case `𝒥² = 0` by considering the
(finite) sequence of preschemes `X_k = (X, 𝒪_X / 𝒥^{k+1})`, each a closed subprescheme of the next defined by a sheaf of
ideals of square zero. Moreover, `X` is a scheme, since `X_red` is by hypothesis (4.5.3 and `(I, 5.5.1)`). Criterion (a)
of (4.5.2) shows that it suffices to prove the

**Lemma.**

<!-- label: II.4.5.13.1 -->

Under the hypotheses of (4.5.13), suppose in addition that `𝒥` is of square zero; `ℒ` being an invertible `𝒪_X`-module,
let `g` be a section of `ℒ'^{⊗n}` over `Z` such that `Z_g` is affine. Then there exists an integer `m > 0` such that
`g^{⊗m}` is the canonical image of a section `f` of `ℒ^{⊗nm}` over `X`.

**Proof.** We have the exact sequence of `𝒪_X`-modules

```text
  0 → 𝒥(n) → 𝒪_X(n) = ℒ^{⊗n} → 𝒪_Z(n) = ℒ'^{⊗n} → 0
```

<!-- original page 88 -->

since `𝓕(n)` is an exact functor in `𝓕`; whence the cohomology exact sequence

```text
  0 → Γ(X, 𝒥(n)) → Γ(X, ℒ^{⊗n}) → Γ(X, ℒ'^{⊗n}) ─∂→ H¹(X, 𝒥(n))
```

which associates to `g` in particular an element `∂g ∈ H¹(X, 𝒥(n))`.

Note that since `𝒥² = 0`, `𝒥` may be regarded as a quasi-coherent `𝒪_Z`-module, and for every `k` we have
`ℒ'^{⊗k} ⊗_{𝒪_Z} 𝒥(n) = 𝒥(n + k)`; for every section `s ∈ Γ(X, ℒ'^{⊗k})`, tensor multiplication by `s` is a homomorphism
`𝒥(n) → 𝒥(n + k)` of `𝒪_Z`-modules, which therefore yields a homomorphism `H¹(X, 𝒥(n)) → H¹(X, 𝒥(n + k))` of cohomology
groups.

We shall see that

```text
  g^{⊗m} ⊗ ∂g = 0                                                         (4.5.13.2)
```

for `m > 0` large enough. Indeed, `Z_g` is an affine open of `Z`, so `H¹(Z_g, 𝒥(n)) = 0` when `𝒥(n)` is viewed as an
`𝒪_Z`-module `(I, 5.1.9.2)`. In particular, if `g' = g | Z_g`, and considering its image under the map
`∂ : Γ(Z_g, ℒ'^{⊗n}) → H¹(Z_g, 𝒥(n))`, we have `∂g' = 0`. To make this relation explicit, observe that in dimension 1
the cohomology of a sheaf of abelian groups coincides with its Čech cohomology (G, II, 5.9); to compute `∂g`, we must
thus consider a fine enough open cover `(U_α)` of `X`, which we may take _finite_ and made of affine opens, take for
each `α` a section `g_α ∈ Γ(U_α, ℒ^{⊗n})` whose canonical image in `Γ(U_α, ℒ'^{⊗n})` is `g | U_α`, and consider the
cocycle class of `(g_{α|β} − g_{β|α})`, with `g_{α|β}` the restriction of `g_α` to `U_α ∩ U_β` (this cocycle taking
values in `𝒥(n)`). One may further suppose that `∂g'` is computed in the same way using the cover formed by the
`U_α ∩ Z_g` and the restrictions `g_α | (U_α ∩ Z_g)` (replacing `(U_α)` by a finer cover if needed); the relation
`∂g' = 0` then means there exists for each `α` a section `h_α ∈ Γ(U_α ∩ Z_g, 𝒥(n))` such that
`(g_{α|β} − g_{β|α}) | (U_α ∩ U_β ∩ Z_g) = h_{α|β} − h_{β|α}`, with `h_{α|β}` the restriction of `h_α` to
`U_α ∩ U_β ∩ Z_g` (G, II, 5.11). Then there exists an integer `m > 0` such that `g^{⊗m} ⊗ h_α` is the restriction to
`U_α ∩ Z_g` of a section `t_α ∈ Γ(U_α, 𝒥(n + nm))` for every `α` `(I, 9.3.1)`; hence
`g^{⊗m} ⊗ (g_{α|β} − g_{β|α}) = t_{α|β} − t_{β|α}` for every pair of indices, which proves (4.5.13.2).

Note further that if `s ∈ Γ(X, 𝒪_Z(p))`, `t ∈ Γ(X, 𝒪_Z(q))`, then in the group `H¹(X, 𝒥(p + q))`

```text
  ∂(s ⊗ t) = (∂s) ⊗ t + s ⊗ (∂t).                                          (4.5.13.3)
```

Indeed, to compute both sides we may again consider an open cover `(U_α)` of `X`, and for each `α` a section
`s_α ∈ Γ(U_α, 𝒪_X(p))` (resp. `t_α ∈ Γ(U_α, 𝒪_X(q))`) whose canonical image in `Γ(U_α, 𝒪_Z(p))` (resp. `Γ(U_α, 𝒪_Z(q))`)
is `s | U_α` (resp. `t | U_α`); the relation (4.5.13.3) then follows from

```text
  (s_{α|β} ⊗ t_{α|β}) − (s_{β|α} ⊗ t_{β|α})
    = (s_{α|β} − s_{β|α}) ⊗ t_{α|β} + s_{β|α} ⊗ (t_{α|β} − t_{β|α})
```

with the same notation. By induction on `k` we therefore have

```text
  ∂(g^{⊗k}) = (k g^{⊗(k−1)}) ⊗ (∂g)                                        (4.5.13.4)
```

<!-- original page 89 -->

and we conclude from (4.5.13.2) and (4.5.13.4) that `∂(g^{⊗(m+1)}) = 0`; hence `g^{⊗(m+1)}` is the canonical image of a
section `f` of `ℒ^{⊗n(m+1)}` over `X`, which completes the proof of (4.5.13).

**Corollary.**

<!-- label: II.4.5.14 -->

Let `X` be a Noetherian scheme, and `j` the canonical injection `X_red → X`. For an invertible `𝒪_X`-module `ℒ` to be
ample, it is necessary and sufficient that `j*(ℒ)` be an ample `𝒪_{X_red}`-module.

**Proof.** This follows from `(I, 6.1.6)`.

## 4.6. Relatively ample sheaves

**Definition.**

<!-- label: II.4.6.1 -->

Let `f : X → Y` be a quasi-compact morphism, and `ℒ` an invertible `𝒪_X`-module. We say that `ℒ` is _ample relative to
`f`_, or _relative to `Y`_, or _`f`-ample_, or _`Y`-ample_ (or even simply _ample_, if no confusion arises with the
notion defined in (4.5.3)) if there exists an affine open cover `(U_α)` of `Y` such that, setting `X_α = f⁻¹(U_α)`,
`ℒ | X_α` is an ample `𝒪_{X_α}`-module for every `α`.

The existence of an `f`-ample `𝒪_X`-module implies that `f` is necessarily _separated_ ((4.5.3) and `(I, 5.5.5)`).

**Proposition.**

<!-- label: II.4.6.2 -->

Let `f : X → Y` be a quasi-compact morphism, and `ℒ` an invertible `𝒪_X`-module. If `ℒ` is very ample relative to `f`,
then it is ample relative to `f`.

**Proof.** This follows from the local (on `Y`) character of the notion of very ample sheaf (4.4.5), from Definition
(4.6.1), and from criterion (4.5.10, (i)).

**Proposition.**

<!-- label: II.4.6.3 -->

Let `f : X → Y` be a quasi-compact morphism, `ℒ` an invertible `𝒪_X`-module, and let `𝒮` be the graded `𝒪_Y`-algebra
`⊕_{n≥0} f_*(ℒ^{⊗n})`. The following conditions are equivalent:

a) `ℒ` is `f`-ample. b) `𝒮` is quasi-coherent and the canonical homomorphism `σ : f*(𝒮) → ⊕_{n≥0} ℒ^{⊗n}` `(0, 4.4.3)`
is such that the `Y`-morphism `r_{ℒ,σ} : G(σ) → Proj(𝒮) = P` is everywhere defined and is a dominant open immersion. b')
The morphism `f` is separated, the `Y`-morphism `r_{ℒ,σ}` is everywhere defined and is a homeomorphism of the underlying
space of `X` onto a subspace of `Proj(𝒮)`.

Furthermore, when these hold, for every `n ∈ ℤ` the canonical homomorphism

```text
  r_{ℒ,σ}*(𝒪_P(n)) → ℒ^{⊗n}                                                (4.6.3.1)
```

defined in (3.7.9.1) is an isomorphism.

Finally, for every quasi-coherent `𝒪_X`-module `𝓕`, setting `ℳ = ⊕_{n≥0} f_*(𝓕 ⊗ ℒ^{⊗n})`, the canonical homomorphism

```text
  r_{ℒ,σ}*(ℳ̃) → 𝓕                                                          (4.6.3.2)
```

defined in (3.7.9.2) is an isomorphism.

**Proof.** We have noted that (a) implies `f` is separated, so `𝒮` is quasi-coherent `(I, 9.2.2, a)`. Since `r_{ℒ,σ}`
being an everywhere defined immersion is of local character on `Y`, to prove (a) implies (b) we may suppose `Y` affine
and `ℒ` ample;

<!-- original page 89 -->

the assertion then follows from (4.5.2, b). It is clear that (b) implies (b'); finally, to prove (b') implies (a), it
suffices to consider an affine open cover of `Y` by `U_α` and to apply criterion (4.5.2, b') to each sheaf
`ℒ | f⁻¹(U_α)`.

For the last two assertions, we use the fact that `σ♭` here is the identity, and the explicit description of the
homomorphisms (3.7.9.1) and (3.7.9.2); it follows at once that (4.6.3.1) is an isomorphism. As for (4.6.3.2), we may
reduce to `Y` affine, hence `ℒ` ample; it is clear that (4.6.3.2) is injective, and criterion (4.5.2, c) shows it is
surjective, whence the conclusion.

**Corollary.**

<!-- label: II.4.6.4 -->

Let `(U_α)` be an open cover of `Y`. For `ℒ` to be ample relative to `Y`, it is necessary and sufficient that
`ℒ | f⁻¹(U_α)` be ample relative to `U_α` for every `α`.

**Proof.** Condition (b) is indeed local on `Y`.

**Corollary.**

<!-- label: II.4.6.5 -->

Let `𝒦` be an invertible `𝒪_Y`-module. For `ℒ` to be `Y`-ample, it is necessary and sufficient that `ℒ ⊗ f*(𝒦)` be so.

**Proof.** This is an evident consequence of (4.6.4), taking the `U_α` such that `𝒦 | U_α` is isomorphic to `𝒪_Y | U_α`
for every `α`.

**Corollary.**

<!-- label: II.4.6.6 -->

Suppose `Y` affine; for `ℒ` to be `Y`-ample it is necessary and sufficient that `ℒ` be ample.

**Proof.** This is an immediate consequence of Definition (4.6.1) and of the criteria (4.6.3, b) and (4.5.2, b), since
here `Proj(𝒮) = Proj(Γ(Y, 𝒮))` by definition.

**Corollary.**

<!-- label: II.4.6.7 -->

Let `f : X → Y` be a quasi-compact morphism. Suppose there exist a quasi-coherent `𝒪_Y`-module `𝓔` and a `Y`-morphism
`g : X → P = ℙ(𝓔)` that is a homeomorphism of the underlying space of `X` onto a subspace of `P`; then `ℒ = g*(𝒪_P(1))`
is `Y`-ample.

**Proof.** We may suppose `Y` affine; the corollary then follows from criterion (4.5.2, a), from formula (3.7.3.1), and
from (4.2.3).

**Proposition.**

<!-- label: II.4.6.8 -->

Let `X` be a quasi-compact scheme or a prescheme whose underlying space is Noetherian, and `f : X → Y` a quasi-compact
separated morphism. For an invertible `𝒪_X`-module `ℒ` to be `f`-ample, it is necessary and sufficient that one of the
following equivalent conditions hold:

c) For every quasi-coherent `𝒪_X`-module `𝓕` of finite type, there exists an integer `n_0 > 0` such that for every
`n ≥ n_0`, the canonical homomorphism `σ : f*(f_*(𝓕 ⊗ ℒ^{⊗n})) → 𝓕 ⊗ ℒ^{⊗n}` is surjective. c') For every quasi-coherent
sheaf `𝒥` of ideals of `𝒪_X` of finite type, there exists an integer `n > 0` such that the canonical homomorphism
`σ : f*(f_*(𝒥 ⊗ ℒ^{⊗n})) → 𝒥 ⊗ ℒ^{⊗n}` is surjective.

**Proof.** Since `X` is quasi-compact, so is `f(X)`, so there exists a finite cover `(U_i)` of `f(X)` by affine opens of
`Y`. To prove (c) when `ℒ` is `f`-ample, we may replace `Y` by the `U_i` and `X` by the `f⁻¹(U_i)`: if we obtain for
each `i` an integer `n_i` such that (c) holds (for `U_i`, `f⁻¹(U_i)`, and `ℒ | f⁻¹(U_i)`) for every `n ≥ n_i`, it
suffices to take `n_0` the largest of the `n_i` to obtain (c) for `Y`, `X`, `ℒ`. But when `Y` is affine, condition (c)
follows from (4.5.5, d) taking (4.6.6) into account. It is trivial that (c) implies (c'). Finally, to prove that (c')
implies that `ℒ` is `f`-ample, we may again restrict to `Y` affine: indeed, every quasi-coherent sheaf `𝒥_i` of ideals
of `𝒪_X | f⁻¹(U_i)` of finite type is the restriction of a coherent sheaf of ideals of `𝒪_X` of finite type
`(I, 9.4.7)`, and hypothesis (c') implies

<!-- original page 91 -->

that `𝒥_i ⊗ (ℒ^{⊗n} | f⁻¹(U_i))` is generated by its sections (taking `(I, 9.2.2)` and (3.4.7) into account); it then
suffices to apply criterion (4.5.5, d'').

**Proposition.**

<!-- label: II.4.6.9 -->

Let `f : X → Y` be a quasi-compact morphism, `ℒ` an invertible `𝒪_X`-module.

1. Let `n > 0` be an integer. For `ℒ` to be `f`-ample, it is necessary and sufficient that `ℒ^{⊗n}` be `f`-ample.
1. Let `ℒ'` be an invertible `𝒪_X`-module, and suppose there exists an integer `n > 0` such that the canonical
    homomorphism `σ : f*(f_*(ℒ'^{⊗n})) → ℒ'^{⊗n}` is surjective. Then, if `ℒ` is `f`-ample, so is `ℒ ⊗ ℒ'`.

**Proof.** We reduce immediately to the case `Y` affine, and the proposition is then an immediate consequence of
(4.5.6).

**Corollary.**

<!-- label: II.4.6.10 -->

The tensor product of two `f`-ample `𝒪_X`-modules is `f`-ample.

**Proposition.**

<!-- label: II.4.6.11 -->

Let `Y` be a quasi-compact prescheme, `f : X → Y` a morphism of finite type, and `ℒ` an invertible `𝒪_X`-module. For `ℒ`
to be `f`-ample, it is necessary and sufficient that it possess one of the following equivalent properties:

d) There exists `n_0 > 0` such that for every integer `n ≥ n_0`, `ℒ^{⊗n}` is very ample relative to `f`. d') There
exists `n > 0` such that `ℒ^{⊗n}` is very ample relative to `f`.

**Proof.** If `ℒ` is ample relative to `f`, there is a finite cover `(U_i)` of `Y` by affine opens such that the
`ℒ | f⁻¹(U_i)` are ample. We then conclude (4.5.10) that there exists an integer `n_0` such that `ℒ^{⊗n} | f⁻¹(U_i)` is
very ample relative to `f⁻¹(U_i) → U_i` for every `n ≥ n_0` and every `i`, so `ℒ^{⊗n}` is very ample relative to `f`
(4.4.5). Conversely, (d') already implies `ℒ^{⊗n}` is `f`-ample (4.6.2), so the same holds for `ℒ` (4.6.9, (i)).

**Corollary.**

<!-- label: II.4.6.12 -->

Let `Y` be a quasi-compact prescheme, `f : X → Y` a morphism of finite type, and `ℒ`, `ℒ'` two invertible `𝒪_X`-modules.
If `ℒ` is `f`-ample, there exists an `n_0` such that `ℒ^{⊗n} ⊗ ℒ'` is very ample relative to `f` for every `n ≥ n_0`.

**Proof.** One argues as in (4.6.11) using a finite affine open cover of `Y` and (4.5.11).

**Proposition.**

<!-- label: II.4.6.13 -->

1. For every prescheme `Y`, every invertible `𝒪_Y`-module `ℒ` is ample relative to the identity morphism `1_Y`.
1. (i bis) Let `f : X → Y` be a quasi-compact morphism, and `j : X' → X` a quasi-compact morphism that is a
    homeomorphism of the underlying space of `X'` onto a subspace of `X`. If `ℒ` is an `𝒪_X`-module ample relative to
    `f`, then `j*(ℒ)` is ample relative to `f ∘ j`.
1. Let `Z` be a quasi-compact prescheme, `f : X → Y` and `g : Y → Z` quasi-compact morphisms, `ℒ` an `𝒪_X`-module ample
    relative to `f`, and `𝒦` an `𝒪_Y`-module ample relative to `g`. Then there exists an integer `n_0 > 0` such that
    `ℒ ⊗ f*(𝒦^{⊗n})` is ample relative to `g ∘ f` for every `n ≥ n_0`.
1. Let `f : X → Y` be a quasi-compact morphism, `g : Y' → Y` a morphism, and set `X' = X_{(Y')}`. If `ℒ` is an
    `𝒪_X`-module ample relative to `f`, then `ℒ' = ℒ ⊗_Y 𝒪_{Y'}` is an `𝒪_{X'}`-module ample relative to `f_{(Y')}`.
1. Let `f_i : X_i → Y_i` (`i = 1, 2`) be two quasi-compact `S`-morphisms. If `ℒ_i` is an `𝒪_{X_i}`-module ample relative
    to `f_i` (`i = 1, 2`), then `ℒ_1 ⊗_S ℒ_2` is ample relative to `f_1 ×_S f_2`.
1. Let `f : X → Y` and `g : Y → Z` be morphisms with `g ∘ f` quasi-compact. If an

<!-- original page 92 -->

```
`𝒪_X`-module `ℒ` is ample relative to `g ∘ f`, and if `g` is
separated or the underlying space of `X` is locally Noetherian, then
`ℒ` is ample relative to `f`.
```

1. Let `f : X → Y` be a quasi-compact morphism, and `j` the canonical injection `X_red → X`. If `ℒ` is an `𝒪_X`-module
    ample relative to `f`, then `j*(ℒ)` is ample relative to `f_red`.

**Proof.** Note first that (v) and (vi) follow from (i), (i bis), and (iv) by the same argument as in (4.4.10), using
(4.6.4) in place of (4.4.5); we leave the details to the reader. Assertion (i) is trivially a consequence of (4.4.10,
(i)) and (4.6.2). To prove (i bis), (iii) and (iv) we use the following lemma:

**Lemma.**

<!-- label: II.4.6.13.1 -->

1. Let `u : Z → S` be a morphism, `ℒ` an invertible `𝒪_S`-module, `s` a section of `ℒ` over `S`, and `s'` the section of
    `u*(ℒ) = ℒ'` over `Z` canonically corresponding to it. Then `Z_{s'} = u⁻¹(S_s)`.
1. Let `Z`, `Z'` be two `S`-preschemes, `p`, `p'` the projections of `T = Z ×_S Z'`, `ℒ` (resp. `ℒ'`) an invertible
    `𝒪_Z`-module (resp. `𝒪_{Z'}`-module), `t` (resp. `t'`) a section of `ℒ` (resp. `ℒ'`) over `Z` (resp. `Z'`), and `s`
    (resp. `s'`) the section of `p*(ℒ)` (resp. `p'*(ℒ')`) over `Z ×_S Z'` corresponding to it. Then
    `T_{s ⊗ s'} = Z_t ×_S Z'_{t'}`.

**Proof.** The definitions show that we may reduce to the case where all preschemes considered are affine. Furthermore,
in (i), we may assume `ℒ = 𝒪_S`; assertion (i) then follows at once from `(I, 1.2.2.2)`. Similarly, in (ii) we may
restrict to `ℒ = 𝒪_Z`, `ℒ' = 𝒪_{Z'}`, and the assertion then reduces to Lemma (4.3.2.4).

We now prove (i bis). We may suppose `Y` affine (4.6.4), hence `ℒ` ample (4.6.6); when `s` ranges over the union of the
`Γ(X, ℒ^{⊗n})` (`n > 0`), the `X_s` form a basis for the topology of `X` (4.5.2, a), so by hypothesis the `j⁻¹(X_s)`
form a basis for the topology of `X'`. By Lemma (4.6.13.1, (i)) and (4.5.2, a), `j*(ℒ)` is ample.

Now we prove (iii). We may again suppose `Y`, `Y'` affine (4.6.4), whence the projection `h : X' → X` is affine (1.5.5).
Since `ℒ` is ample (4.6.6), as `s` ranges over the sections of the `ℒ^{⊗n}` (`n > 0`) over `X` such that `X_s` is
affine, the `X_s` cover `X` (4.5.2, a'), so the `h⁻¹(X_s)` are affine (1.2.5) and cover `X'`; it follows again from
Lemma (4.6.13.1, (i)) and (4.5.2, a') that `ℒ'` is ample, the morphism `f_{(Y')}` being quasi-compact
`(I, 6.6.4, (iii))`.

To prove (iv), note first that `f_1 ×_S f_2` is quasi-compact `(I, 6.6.4, (iv))`. We may further suppose `S`, `Y_1`,
`Y_2` affine ((4.6.4) and `(I, 3.2.7)`), hence `ℒ_i` ample (`i = 1, 2`) (4.6.6). The opens `(X_1)_{s_1} ×_S (X_2)_{s_2}`
form a cover of `X_1 ×_S X_2` as `s_i` ranges over the sections of `ℒ_i^{⊗n_i}` such that `(X_i)_{s_i}` is affine
(4.5.2, a'). Replacing `s_1` and `s_2` by suitable powers (which does not change the `(X_i)_{s_i}`), we may always
suppose `n_1 = n_2`. We deduce from (4.6.13.1, (ii)) and (4.5.2, a') that `ℒ_1 ⊗_S ℒ_2` is ample, whence the assertion,
since `Y_1 ×_S Y_2` is affine (4.6.6).

It remains to prove (ii). By the same argument as in (4.4.10), but using (4.6.4) here, we may restrict to the case `Z`
affine. Since `𝒦` is then ample, and `Y` quasi-compact, there are finitely many sections `s_i ∈ Γ(Y, 𝒦^{⊗k_i})` such
that the `Y_{s_i}`

<!-- original page 93 -->

are _affine_ and cover `Y` (4.5.2, a'); replacing the `s_i` by suitable powers, we may further suppose all the `k_i`
equal to a single integer `k`. Let `s_i'` be the sections of `f*(𝒦^{⊗k})` over `X` canonically corresponding to the
`s_i`, so that the `X_{s_i'} = f⁻¹(Y_{s_i})` (4.6.13.1, (i)) cover `X`. Since `ℒ | X_{s_i'}` is ample (4.6.4 and 4.6.6),
there exist for each `i` finitely many sections `t_{ij} ∈ Γ(X, ℒ^{⊗n_{ij}})` such that the `X_{t_{ij}}` are affine,
contained in `X_{s_i'}`, and cover `X_{s_i'}` (4.5.2, a'); we may further suppose all the `n_{ij}` equal to a single
integer `n`. With this, `X` is separated and quasi-compact, so there exists an integer `m > 0` and, for every `(i, j)`,
a section

```text
  u_{ij} ∈ Γ(X, ℒ^{⊗n} ⊗_X f*(𝒦^{⊗mk}))
```

such that `t_{ij} ⊗ s_i'^{⊗m}` is the restriction to `X_{s_i'}` of `u_{ij}` `(I, 9.3.1)`; moreover
`X_{u_{ij}} = X_{t_{ij}}`, so the `X_{u_{ij}}` are affine and cover `X`. We may also suppose `m` is of the form `nr`;
setting `n_0 = rk`, we see (4.5.2, a') that `ℒ ⊗_{𝒪_X} f*(𝒦^{⊗n_0})` is ample. Furthermore, there exists `h_0 > 0` such
that `𝒦^{⊗h}` is generated by its sections over `Y` for every `h ≥ h_0` (4.5.5); _a fortiori_ `f*(𝒦^{⊗h})` is generated
by its sections over `X` for `h ≥ h_0`, by the definition of inverse images `(0, 3.7.1 and 4.4.1)`. We conclude that
`ℒ ⊗ f*(𝒦^{⊗(n_0 + h)})` is ample for every `h ≥ h_0` (4.5.6), which completes the proof.

**Remark.**

<!-- label: II.4.6.14 -->

Under the conditions of (ii), one should refrain from believing that `ℒ ⊗ f*(𝒦)` is ample for `g ∘ f`: indeed, since
`ℒ ⊗ f*(𝒦⁻¹)` is also ample for `f` (4.6.5), one would conclude that `ℒ` is ample for `g ∘ f`; taking in particular `g`
to be the identity morphism, _every_ invertible `𝒪_X`-module would be ample for `f`, which is not the case in general
(see (5.1.6), (5.3.4, (i)), and (5.3.1)).

**Proposition.**

<!-- label: II.4.6.15 -->

Let `f : X → Y` be a quasi-compact morphism, `𝒥` a quasi-coherent locally nilpotent sheaf of ideals of `𝒪_X`, `Z` the
closed subprescheme of `X` defined by `𝒥`, and `j : Z → X` the canonical injection. For an invertible `𝒪_X`-module `ℒ`
to be ample for `f`, it is necessary and sufficient that `j*(ℒ)` be ample for `f ∘ j`.

**Proof.** The question being local on `Y` (4.6.4), we may suppose `Y` affine; since `X` is then quasi-compact, we may
suppose `𝒥` nilpotent. Taking (4.6.6) into account, the proposition is then nothing but (4.5.13).

**Corollary.**

<!-- label: II.4.6.16 -->

Let `X` be a locally Noetherian prescheme, `f : X → Y` a quasi-compact morphism. For an invertible `𝒪_X`-module `ℒ` to
be ample for `f`, it is necessary and sufficient that its inverse image `ℒ'` under the canonical injection `X_red → X`
be ample for `f_red`.

**Proof.** We have already seen that the condition is necessary (4.6.13, (vi)); conversely, if it is satisfied, we may
restrict, to prove that `ℒ` is ample for `f`, to the case `Y` affine (4.6.4); then `Y_red` is also affine, so `ℒ'` is
ample (4.6.6), and so is `ℒ` by (4.5.13), since `X` is then Noetherian and `X_red` a closed subprescheme of `X` defined
by a quasi-coherent nilpotent sheaf of ideals `(I, 6.1.6)`.

**Proposition.**

<!-- label: II.4.6.17 -->

With the notation and hypotheses of (4.4.11), for `ℒ''` to be ample relative to `f''`, it is necessary and sufficient
that `ℒ` be ample relative to `f` and `ℒ'` ample relative to `f'`.

<!-- original page 94 -->

**Proof.** The necessity of the condition follows from (4.6.13, (i bis)). To see that the condition is sufficient, we
may restrict to `Y` affine, and then the fact that `ℒ''` is ample follows from criterion (4.5.2, a) applied to `ℒ`,
`ℒ'`, and `ℒ''`, observing that a section of `ℒ` over `X` extends (by `0`) to a section of `ℒ''` over `X''`.

**Proposition.**

<!-- label: II.4.6.18 -->

Let `Y` be a quasi-compact prescheme, `𝒮` a quasi-coherent graded `𝒪_Y`-algebra of finite type, `X = Proj(𝒮)`, and
`f : X → Y` the structure morphism. Then `f` is of finite type, and there exists an integer `d > 0` such that `𝒪_X(d)`
is invertible and `f`-ample.

**Proof.** By (3.1.10), there exists an integer `d > 0` such that `𝒮^{(d)}` is generated by `𝒮_d`. Under the canonical
isomorphism between `X` and `X^{(d)} = Proj(𝒮^{(d)})`, `𝒪_X(d)` is identified with `𝒪_{X^{(d)}}(1)` (3.2.9, (ii)). We
see that we are reduced to the case where `𝒮` is generated by `𝒮_1`; the proposition then follows from (4.4.3) and
(4.6.2) (taking into account that `f` is a morphism of finite type (3.4.1)).

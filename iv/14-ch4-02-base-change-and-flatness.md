<!-- original page 5 -->

# Chapter IV (continued)

## §2. Base change and flatness

This section (unlike §6) appeals only exceptionally to Noetherian techniques. Nos. 1 and 2 are scarcely more than
translations of elementary properties of flatness from commutative algebra (cf. Bourbaki, _Alg. comm._, chap. I) and are
included here for the convenience of references. The following numbers are devoted above all to "descent" properties
along flat or faithfully flat morphisms: if `g : Y' → Y` is such a morphism, the issue is to be able to assert that a
part of `Y`, or an `𝒪_Y`-Module, or a morphism `X → Y`, has a certain property, when one knows that its inverse image
under `g` has that property. We restrict ourselves here to properties that do not appeal to the general technique of
"descent", which will be developed in Chapter V.

### 2.1. Flat modules on preschemes

**(2.1.1)**

<!-- label: IV.2.1.1 -->

Let `f : X → Y` be a morphism of preschemes and `ℱ` an `𝒪_X`-Module; recall `(0_I, 6.7.1)` that `ℱ` is said to be
**`f`-flat** (or **`Y`-flat**) **at a point `x ∈ X`** if `ℱ_x` is a flat `𝒪_{f(x)}`-module, **`f`-flat** (or
**`Y`-flat**) if it is `f`-flat at every `x ∈ X`, and finally that the morphism `f` is said to be **flat at the point
`x ∈ X`** (resp. **flat**) if `𝒪_X` is `f`-flat at `x` (resp. `f`-flat). When `f = 1_X`, one says simply that an
`𝒪_X`-Module `ℱ` is **flat at the point `x`** (resp. **flat**) if it is `X`-flat at this point (resp. at every point
`x ∈ X`), that is, if `ℱ_x` is a flat `𝒪_x`-module (resp. if this holds for every `x ∈ X`). Recall that we have proved
`(III, 1.4.15.1)` the following property:

**Proposition (2.1.2).**

<!-- label: IV.2.1.2 -->

*Let `A`, `B` be two rings, `φ : A → B` a ring homomorphism, `X = Spec(B)`, `Y = Spec(A)`, `f : X → Y` the morphism
corresponding to `φ`, `M` a `B`-module. For `ℱ = M̃` to be `f`-flat, it is necessary and sufficient that `M` be a flat
`A`-module.*

<!-- original page 6 -->

**Proposition (2.1.3).**

<!-- label: IV.2.1.3 -->

*Let `f : X → Y` be a morphism of preschemes, `ℱ` a quasi-coherent `𝒪_X`-Module. The following conditions are
equivalent:*

*a) For every base change `g : Y' → Y`, if one sets `X' = X ×_Y Y'`, the functor `ℱ' ↦ ℱ ⊗_Y ℱ'` from the category of
quasi-coherent `𝒪_{Y'}`-Modules to that of quasi-coherent `𝒪_{X'}`-Modules is exact.*

*a') Condition a) is satisfied for all canonical morphisms `g : Spec(𝒪_y) → Y` `(I, 2.4.1)`, where `y` runs over `Y`.*

*b) `ℱ` is `f`-flat.*

The questions being local on `X` and `Y`, one may restrict to the case where `Y = Spec(B)`, `X = Spec(A)`, `ℱ = M̃`,
where `M` is an `A`-module. It is clear that a) entails a'); condition a') entails that for every `x ∈ X` the functor
`N ↦ M_𝔫 ⊗_{B_𝔫} N` is exact in the category of `B_𝔫`-modules, `𝔫` being the ideal `𝔧_{f(x)}` of `B`; this means that
`M_𝔫` is a flat `B_𝔫`-module, and it results from `(0_I, 6.3.3)` and from `(2.1.2)` that `ℱ` is `f`-flat. Finally, to
see that b) entails a), one may also restrict to the case where `Y' = Spec(A')` is affine and `ℱ' = Ñ'`, where `N'` is
an `A'`-module; the conclusion then again follows from `(2.1.2)` and the definition of flatness, since
`(M ⊗_A N')~ = ℱ ⊗_Y ℱ'`.

**Proposition (2.1.4).**

<!-- label: IV.2.1.4 -->

*Let `f : X → Y`, `g : Y' → Y` be two morphisms of preschemes, `ℱ` a quasi-coherent `𝒪_X`-Module; set `X' = X ×_Y Y'`,
`f' = f_{(Y')} : X' → Y'`, `ℱ' = ℱ ⊗_Y 𝒪_{Y'}`, and let `g'` be the canonical projection `X' → X`. Let `x'` be a point
of `X'`, `x = g'(x')`, `y' = f'(x')`, `y = f(x) = g(y')`. If `ℱ` is `f`-flat at the point `x`, then `ℱ'` is `f'`-flat at
the point `x'`; in particular if `ℱ` is `f`-flat, `ℱ'` is `f'`-flat; if `f` is flat, `f'` is flat.*

It suffices to prove the first assertion; applying `(I, 3.6.5)` three times, as well as `(I, 2.4.4)`, one may reduce to
the case where `Y = Spec(𝒪_y)`, `X = Spec(𝒪_x)`, `Y' = Spec(𝒪_{y'})`, `ℱ = M̃`, where `M = ℱ_x`; the hypothesis and
`(2.1.2)` then entail that `ℱ` is `f`-flat — in other words one is reduced to proving a particular case of the second
assertion, and this last follows at once from `(2.1.3)`.

**Proposition (2.1.5).**

<!-- label: IV.2.1.5 -->

*Consider a commutative diagram of morphisms of preschemes*

```text
  X  ←─g'──  X'
  │           │
  f│         │f'
  ↓           ↓
  Y  ←──g──  Y'
              │
              │h
              ↓
              Z
```

*where `X' = X ×_Y Y'` and `f' = f_{(Y')}`. Let `x'` be a point of `X'`, and set `x = g'(x')`, `y' = f'(x')`,
`y = f(x) = g(y')`, `z = h(y')`. Let `ℱ` be a quasi-coherent `𝒪_X`-Module that is `f`-flat at the point `x` (resp.
`f`-flat), and `𝒢'` a quasi-coherent `𝒪_{Y'}`-Module that is `h`-flat at the point `y'` (resp. `h`-flat); then
`ℱ ⊗_{𝒪_Y} 𝒢'` is a quasi-coherent `𝒪_{X'}`-Module that is `(h ∘ f')`-flat at the point `x'` (resp. `(h ∘ f')`-flat).*

As in `(2.1.4)`, one reduces to the case where `X = Spec(𝒪_x)`, `Y = Spec(𝒪_y)`,

<!-- original page 7 -->

`Y' = Spec(𝒪_{y'})` and `Z = Spec(𝒪_z)`, and it then suffices to prove that `ℱ ⊗_{𝒪_Y} 𝒢'` is `(h ∘ f')`-flat. Taking
`(2.1.2)` into account, the proposition follows from Bourbaki, _Alg. comm._, chap. I, §2, n° 7, prop. 8.

**Corollary (2.1.6).**

<!-- label: IV.2.1.6 -->

*Let `f : X → Y`, `g : Y → Z` be two morphisms of preschemes, `ℱ` an `𝒪_X`-Module. If `ℱ` is `f`-flat at the point
`x ∈ X` and `g` is flat at the point `f(x)`, then `ℱ` is `(g ∘ f)`-flat at the point `x`. In particular, if `f` and `g`
are flat morphisms, so is `g ∘ f`.*

This is the particular case of `(2.1.5)` with `Y' = Y`, `𝒢' = 𝒪_{Y'}`.

**Corollary (2.1.7).**

<!-- label: IV.2.1.7 -->

*If `f : X → X'`, `g : Y → Y'` are two flat `S`-morphisms, then `f ×_S g : X ×_S Y → X' ×_S Y'` is a flat morphism.*

This follows from `(2.1.4)` and `(2.1.6)` (cf. `(I, 3.5.1)`).

**Proposition (2.1.8).**

<!-- label: IV.2.1.8 -->

*Let `f : X → Y` be a morphism of preschemes,*

```text
  0 → ℱ' → ℱ → ℱ'' → 0
```

*an exact sequence of quasi-coherent `𝒪_X`-Modules such that `ℱ''` is `Y`-flat.*

*(i) For every morphism `g : Y' → Y` and every quasi-coherent `𝒪_{Y'}`-Module `𝒢'`, the sequence*

```text
  0 → ℱ' ⊗_Y 𝒢' → ℱ ⊗_Y 𝒢' → ℱ'' ⊗_Y 𝒢' → 0
```

*of `𝒪_{X'}`-Modules (where `X' = X ×_Y Y'`) is exact.*

*(ii) For `ℱ` to be `Y`-flat, it is necessary and sufficient that `ℱ'` be so.*

One may obviously suppose `X`, `Y`, `Y'` affine; the conclusion then follows from `(2.1.2)` and `(0_I, 6.1.2)`.

**Corollary (2.1.9).**

<!-- label: IV.2.1.9 -->

*Let `ℒ^•` be a complex of quasi-coherent `𝒪_X`-Modules, `i` an index such that if one denotes by `d^i : ℒ^i → ℒ^{i+1}`
the differential, `ℬ^{i+1}(ℒ^•) = Im(d^i)` and `𝒵^{i+1}(ℒ^•) = Coker(d^i)` are `Y`-flat. Then, with the notations of
`(2.1.8)`, the canonical homomorphism*

```text
  ℋ^i(ℒ^•) ⊗_Y 𝒢' → ℋ^i(ℒ^• ⊗_Y 𝒢')
```

*is bijective.*

Since the tensor product is right exact, one has

```text
  𝒵^{i+1}(ℒ^•) ⊗_Y 𝒢' = Coker(d^i ⊗ 1) = 𝒵^{i+1}(ℒ^• ⊗_Y 𝒢')
```

and `𝒵^{′i}(ℒ^•) ⊗_Y 𝒢' = 𝒵^{′i}(ℒ^• ⊗_Y 𝒢')`. Moreover, in the exact sequence

```text
  0 → ℬ^{i+1}(ℒ^•) → ℒ^{i+1} → 𝒵^{i+1}(ℒ^•) → 0
```

`𝒵^{i+1}(ℒ^•)` is `Y`-flat, so it follows from `(2.1.8, (i))` that one has the exact sequence

```text
  0 → ℬ^{i+1}(ℒ^•) ⊗_Y 𝒢' → ℒ^{i+1} ⊗_Y 𝒢' → 𝒵^{i+1}(ℒ^• ⊗_Y 𝒢') → 0
```

whence `ℬ^{i+1}(ℒ^•) ⊗_Y 𝒢' = Im(d^i ⊗ 1) = ℬ^{i+1}(ℒ^• ⊗_Y 𝒢')`. Then, in the exact sequence

```text
  0 → ℋ^i(ℒ^•) → 𝒵^i(ℒ^•) → ℬ^{i+1}(ℒ^•) → 0
```

`ℬ^{i+1}(ℒ^•)` is `Y`-flat, so it follows from `(2.1.8, (i))` and what precedes that one has the exact sequence

```text
  0 → ℋ^i(ℒ^•) ⊗_Y 𝒢' → 𝒵^i(ℒ^• ⊗_Y 𝒢') → ℬ^{i+1}(ℒ^• ⊗_Y 𝒢') → 0
```

which proves the corollary.

<!-- original page 8 -->

**Corollary (2.1.10).**

<!-- label: IV.2.1.10 -->

*Let `f : X → Y` be a morphism of preschemes, `ℱ` a quasi-coherent and `Y`-flat `𝒪_X`-Module, `ℒ_• = (ℒ_i)` a left
resolution of `ℱ` formed of quasi-coherent and `Y`-flat `𝒪_X`-Modules. Then, for every morphism `g : Y' → Y` and every
quasi-coherent `𝒪_{Y'}`-Module `𝒢'`, the complex `ℒ_• ⊗_Y 𝒢' = (ℒ_i ⊗_Y 𝒢')_{i ≥ 0}` is a left resolution of
`ℱ ⊗_Y 𝒢'`.*

*Moreover, if `𝒵_i(ℒ_•) = Ker(ℒ_i → ℒ_{i−1})`, the `𝒵_i(ℒ_•)` are `Y`-flat, and one has*

```text
  𝒵_i(ℒ_•) ⊗_Y 𝒢' = 𝒵_i(ℒ_• ⊗_Y 𝒢') = Ker(ℒ_i ⊗_Y 𝒢' → ℒ_{i−1} ⊗_Y 𝒢').
```

Set `ℛ_i = Im(ℒ_{i+1} → ℒ_i) = 𝒵_i(ℒ_•)`; one then has the exact sequences

```text
  0 ← ℱ ← ℒ_0 ← ℛ_0 ← 0
  ⋮
  0 ← ℛ_i ← ℒ_{i+1} ← ℛ_{i+1} ← 0
  ⋮
```

and since `ℱ` and the `ℒ_i` are `Y`-flat, one deduces from `(2.1.8, (ii))` by induction that all the `ℛ_i` are also
`Y`-flat; using `(2.1.8, (i))`, one therefore has the exact sequences

```text
  0 ← ℱ ⊗_Y 𝒢' ← ℒ_0 ⊗_Y 𝒢' ← ℛ_0 ⊗_Y 𝒢' ← 0
  0 ← ℛ_i ⊗_Y 𝒢' ← ℒ_{i+1} ⊗_Y 𝒢' ← ℛ_{i+1} ⊗_Y 𝒢' ← 0          (i ≥ 0)
```

which prove the corollary.

**Proposition (2.1.11).**

<!-- label: IV.2.1.11 -->

*Let `f : X → Y` be a flat morphism, `ℱ` a quasi-coherent `𝒪_Y`-Module of finite presentation. If `𝒥` is the Ideal of
`𝒪_Y` annihilator of `ℱ`, then `f*(𝒥)` is the Ideal of `𝒪_X` annihilator of `f*(ℱ)`.*

One has by definition an exact sequence `(0_I, 5.3.7)`

```text
  0 → 𝒥 → 𝒪_Y → ℋom_{𝒪_Y}(ℱ, ℱ)
```

whence, since `f` is flat, an exact sequence

```text
  0 → f*(𝒥) → 𝒪_X → f*(ℋom_{𝒪_Y}(ℱ, ℱ))
```

and since by hypothesis `ℱ` is an `𝒪_Y`-Module of finite presentation, `f*(ℋom_{𝒪_Y}(ℱ, ℱ))` is canonically identified
with `ℋom_{𝒪_X}(f*(ℱ), f*(ℱ))` `(0_I, 6.7.6)`, whence the conclusion.

**Proposition (2.1.12).**

<!-- label: IV.2.1.12 -->

*Let `X` be a prescheme, `ℱ` an `𝒪_X`-Module of finite presentation, `x` a point of `X`. The following conditions are
equivalent:*

*a) `ℱ_x` is a flat `𝒪_x`-module.*

*b) There exists an open neighbourhood `U` of `x` such that `ℱ|U` is a locally free `(𝒪_X|U)`-Module.*

Indeed, `ℱ_x` is an `𝒪_x`-module of finite presentation and `𝒪_x` a local ring; it therefore amounts to the same to say
that `ℱ_x` is a flat `𝒪_x`-module or a free `𝒪_x`-module (Bourbaki, _Alg. comm._, chap. II, §3, n° 2, cor. 2 of prop.
5); whence the conclusion, taking account of `(0_I, 5.2.7)`. We note that the proposition is valid for an arbitrary
ringed space in local rings.

**Proposition (2.1.13).**

<!-- label: IV.2.1.13 -->

\*Let `f : X → Y` be a morphism of preschemes. If `f` is flat at a point `x ∈ X` and the ring `𝒪_x` is reduced (resp.
integral and integrally closed), then the ring `𝒪_{f(x)}`

<!-- original page 9 -->

is reduced (resp. integral and integrally closed). If `f` is faithfully flat and `X` is reduced (resp. normal), then `Y`
is reduced (resp. normal).\*

Set `𝒪_{f(x)} = A`, `𝒪_x = B`. If `B` is a flat `A`-module, it is also a faithfully flat `A`-module `(0_I, 6.6.2)`, so
`A` is identified with a subring of `B`; if `B` is reduced, so therefore is `A`. Suppose now that `B` is integral and
integrally closed, and let `L` be its field of fractions; then `A ⊂ B` is integral; denote by `K ⊂ L` its field of
fractions. The hypothesis entails that `B ∩ K = A` (Bourbaki, _Alg. comm._, chap. I, §3, n° 5, prop. 10). If then
`t ∈ K` is integral over `A`, it is also integral over `B`, hence belongs to `B` by hypothesis, and consequently
`t ∈ A`, which proves that `A` is integrally closed.

**Proposition (2.1.14).**

<!-- label: IV.2.1.14 -->

*Let `f : X → Y` be a faithfully flat morphism. If `X` is locally integral and the space underlying `Y` is locally
Noetherian, then `Y` is locally integral.*

Indeed, every `y ∈ Y` is of the form `f(x)` for some `x ∈ X` and by hypothesis `𝒪_y` is identified with a subring of
`𝒪_x` `(0_I, 6.6.1)`; since `𝒪_x` is integral, so is `𝒪_y`, and this proves the proposition `(I, 5.1.4)`.

### 2.2. Faithfully flat modules on preschemes

**Proposition (2.2.1).**

<!-- label: IV.2.2.1 -->

*Let `f : X → Y` be a morphism of preschemes, `ℱ` a quasi-coherent `𝒪_X`-Module. The following conditions are
equivalent:*

*a) For every base change `g : Y' → Y`, if one sets `X' = X ×_Y Y'`, the functor `𝒢' ↦ ℱ ⊗_Y 𝒢'` from the category of
quasi-coherent `𝒪_{Y'}`-Modules to that of quasi-coherent `𝒪_{X'}`-Modules is exact and faithful.*

*a') Condition a) is satisfied for all canonical morphisms `g : Spec(𝒪_y) → Y` `(I, 2.4.1)`, where `y` runs over `Y`.*

*a'') Condition a) is satisfied for all canonical immersions `Y' → Y`, where `Y'` runs over the set of affine open
subschemes of `Y`.*

*b) `ℱ` is `Y`-flat and, for every `y ∈ Y`, if one denotes by `X_y` the fibre `f⁻¹(y)`, the `𝒪_{X_y}`-Module
`ℱ_y = ℱ ⊗_Y k(y)` is `≠ 0`.*

It is clear that a) implies a') and a''); condition a') first implies that `ℱ` is `Y`-flat `(2.1.3)`; on the other hand
it implies that for every `y ∈ Y` the functor `N ↦ ℱ_y ⊗_{𝒪_y} Ñ` is faithful in the category of `𝒪_y`-modules; taking
in particular `N = k(y)`, one obtains the second assertion of b). To show that b) implies a), one may restrict to the
case where `Y` is affine, the question being local on `Y`. Similarly, to prove that a'') implies a), one is reduced to
proving that when `Y` is affine, the fact that `𝒢' ↦ ℱ ⊗_Y 𝒢'` is an exact and faithful functor entails condition a). In
other words, one is reduced to proving the following more precise proposition:

**Proposition (2.2.2).**

<!-- label: IV.2.2.2 -->

*Let `Y = Spec(A)` be an affine scheme, `f : X → Y` a morphism of preschemes, `ℱ` a quasi-coherent `𝒪_X`-Module.
Condition a) of `(2.2.1)` is equivalent to each of the following:*

*b') `ℱ` is `Y`-flat and, for every closed point `y` of `Y`, one has `ℱ_y ≠ 0`.*

<!-- original page 10 -->

*c) The functor `𝒢 ↦ ℱ ⊗_Y 𝒢` from the category of quasi-coherent `𝒪_Y`-Modules to that of quasi-coherent `𝒪_X`-Modules
is exact and faithful.*

If b') is satisfied, there is at least one `x ∈ f⁻¹(y)` such that `(ℱ_y)_x ≠ 0`; let `U = Spec(B)` be an affine open
neighbourhood of `x`, and let `ℱ|U = M̃`, where `M` is a `B`-module. Then b') implies that `M/𝔧_y M ≠ 0`, and
consequently (since `M` is a flat `A`-module by `(2.1.2)`) that `M ⊗_A A_y` is a faithfully flat `A_y`-module
`(0_I, 6.4.5)`. The relation `(ℱ ⊗_Y 𝒢) ⊗_{𝒪_Y} 𝒪_y = 0` for a closed point `y` of `Y` implies
`(ℱ ⊗_{𝒪_Y} 𝒪_U)_x ⊗_{𝒪_y} 𝒢_y = 0`, hence `𝒢_y = 0`. But if `𝒢_y = 0` for every closed point `y` of `Y`, one concludes
that `𝒢 = 0`; indeed, if `𝒢 = Ñ`, the annihilator of an element of `N` is contained in no maximal ideal of `A`, so it
equals all of `A`. The relation `ℱ ⊗_Y 𝒢 = 0` therefore implies `𝒢 = 0`; in other words, the functor `𝒢 ↦ ℱ ⊗_Y 𝒢` is
faithful; we know moreover that this functor is exact `(2.1.3)`, which shows that b') entails c).

Finally, to see that c) entails a), one may restrict to the case where `Y'` is also affine; as `g : Y' → Y` is then an
affine morphism, so is the projection `g' : X' → X` `(II, 1.5.5)`; in addition, the functor `ℋ ↦ g'_*(ℋ)` is then exact
in the category of quasi-coherent `𝒪_{X'}`-Modules `(I, 1.6.4)`, and if `g'_*(ℋ) = ℋ`, one has `ℋ' = ℋ̃`, so the
preceding functor is also faithful; to see that `𝒢' ↦ ℱ ⊗_Y 𝒢'` is exact and faithful, it therefore suffices to see that
the functor `𝒢' ↦ g'_*(ℱ ⊗_Y 𝒢')` is. Now, if `f' = f_{(Y')} : X' → Y'`, one has
`g'_*(ℱ ⊗_Y 𝒢') = g'_*(g'*(ℱ) ⊗_{𝒪_{X'}} f'*(𝒢'))`; the fact that `g` is affine entails that one has a canonical
isomorphism

```text
  ℱ ⊗_{𝒪_X} f*(g_*(𝒢')) ⥲ g'_*(g'*(ℱ) ⊗_{𝒪_{X'}} f'*(𝒢')).            (2.2.2.1)
```

Indeed, one knows `(II, 1.5.2)` that one has a canonical isomorphism

```text
  f*(g_*(𝒢')) ⥲ g'_*(f'*(𝒢')),
```

and on the other hand one has a canonical homomorphism `ℱ → g'_*(g'*(ℱ))` `(0_I, 4.4.3.2)`; composing the homomorphism
`ℱ ⊗_{𝒪_X} f*(g_*(𝒢')) → g'_*(g'*(ℱ)) ⊗_{𝒪_X} g'_*(f'*(𝒢'))` with the canonical homomorphism `(0_I, 4.2.2.1)`, one
deduces the homomorphism `(2.2.2.1)`; the verification that it is an isomorphism is immediate by reducing to the case
where `X` is affine. This being so, the functor `𝒢' ↦ g_*(𝒢')` is exact and faithful and by hypothesis so is
`𝒢 ↦ ℱ ⊗_Y 𝒢 = ℱ ⊗_{𝒪_X} f*(𝒢)`; their composite is therefore exact and faithful, which completes the proof of `(2.2.1)`
and `(2.2.2)`.

**Corollary (2.2.3).**

<!-- label: IV.2.2.3 -->

*Let `X = Spec(B)`, `Y = Spec(A)` be two affine schemes, `f : X → Y` a morphism, `ℱ = M̃` a quasi-coherent `𝒪_X`-Module.
For `ℱ` to satisfy the equivalent conditions of `(2.2.1)` (or `(2.2.2)`), it is necessary and sufficient that the
`A`-module `M` be faithfully flat.*

Indeed, condition c) of `(2.2.2)` then means that the functor `N ↦ M ⊗_A N` from the category of `A`-modules to that of
`B`-modules is exact and faithful, and the conclusion follows from `(0_I, 6.4.1)`.

**Definition (2.2.4).**

<!-- label: IV.2.2.4 -->

*When the equivalent conditions of `(2.2.1)` are satisfied, one says that the quasi-coherent `𝒪_X`-Module `ℱ` is
**faithfully flat relative to `f`** (or **to `Y`**).*

<!-- original page 11 -->

One notes that this notion is local on `Y`, but *not* on `X`; in particular one can have `ℱ_x = 0` for certain `x ∈ X`,
in other words `Supp(ℱ)` is not necessarily equal to `X`. Nevertheless, it follows at once from criterion `(2.2.1, b)`
that for every `y ∈ Y` there exists at least one `x ∈ f⁻¹(y)` such that `(ℱ_y)_x = ℱ_x ⊗_{𝒪_y} k(y) ≠ 0`, and *a
fortiori* `ℱ_x ≠ 0`; in other words:

**Corollary (2.2.5).**

<!-- label: IV.2.2.5 -->

*If `ℱ` is a quasi-coherent `𝒪_X`-Module, faithfully flat relative to `f`, one has `f(Supp(ℱ)) = Y`, and a fortiori `f`
is a surjective morphism.*

This result admits a partial converse:

**Corollary (2.2.6).**

<!-- label: IV.2.2.6 -->

*Let `ℱ` be a quasi-coherent `𝒪_X`-Module of finite type. For `ℱ` to be faithfully flat relative to `f`, it is necessary
and sufficient that `ℱ` be `f`-flat and that `f(Supp(ℱ)) = Y`.*

Indeed `(I, 9.1.13 and 3.6.1)` one has `Supp(ℱ_y) = f⁻¹(y) ∩ Supp(ℱ)`, so in this case criterion `(2.2.1, b)` is none
other than the condition of the corollary.

In particular, the `𝒪_X`-Module `𝒪_X` is faithfully flat relative to `f` if and only if it is `f`-flat and `f` is
surjective, in other words if and only if the morphism `f` is **faithfully flat** `(0_I, 6.7.8)`.

Let us make explicit the properties involved in definition `(2.2.4)`:

**Proposition (2.2.7).**

<!-- label: IV.2.2.7 -->

*Let `f : X → Y` be a morphism of preschemes, `ℱ` a quasi-coherent `𝒪_X`-Module faithfully flat relative to `f`. Then,
for a sequence `𝒢' → 𝒢 → 𝒢''` of quasi-coherent `𝒪_Y`-Modules to be exact, it is necessary and sufficient that the
corresponding sequence `ℱ ⊗_Y 𝒢' → ℱ ⊗_Y 𝒢 → ℱ ⊗_Y 𝒢''` be so. In particular, for a homomorphism `u : 𝒢 → 𝒢'` of
quasi-coherent `𝒪_Y`-Modules to be injective (resp. surjective, bijective, zero), it is necessary and sufficient that
`1_ℱ ⊗ f*(u) : ℱ ⊗_Y 𝒢 → ℱ ⊗_Y 𝒢'` be so. For a quasi-coherent `𝒪_Y`-Module `𝒢` to be zero, it is necessary and
sufficient that `ℱ ⊗_Y 𝒢 = 0`. For every quasi-coherent `𝒪_Y`-Module `𝒢`, the map `𝒢' ↦ ℱ ⊗_Y 𝒢'` from the set of
quasi-coherent sub-`𝒪_Y`-Modules of `𝒢` to the set of quasi-coherent sub-`𝒪_X`-Modules of `ℱ ⊗_Y 𝒢` is injective.*

To prove the last assertion — that is, that for two quasi-coherent sub-`𝒪_Y`-Modules `𝒢'`, `𝒢''` of `𝒢`, the relation
`ℱ ⊗_Y 𝒢' = ℱ ⊗_Y 𝒢''` entails `𝒢' = 𝒢''` — one may (replacing `𝒢''` by `𝒢' + 𝒢''`) reduce to the case where `𝒢' ⊂ 𝒢''`,
and it then suffices to apply the second assertion of the statement to the injection `u : 𝒢' → 𝒢''`.

**Corollary (2.2.8).**

<!-- label: IV.2.2.8 -->

*Let `f : X → Y` be a faithfully flat morphism. For every quasi-coherent `𝒪_Y`-Module `𝒢`, the canonical map*

```text
  Γ(Y, 𝒢) → Γ(X, f*(𝒢))                                       (2.2.8.1)
```

*is injective.*

Indeed, `Γ(Y, 𝒢)` is canonically identified with `Hom_{𝒪_Y}(𝒪_Y, 𝒢)` `(0_I, 5.1.1)` and likewise `Γ(X, f*(𝒢))` with
`Hom_{𝒪_X}(𝒪_X, f*(𝒢))`. By virtue of `(2.2.1)` and `(2.2.4)`, the hypothesis entails that the functor `𝒢 ↦ f*(𝒢)` is
exact and faithful in the category of quasi-coherent `𝒪_Y`-Modules, and consequently a homomorphism `u : 𝒪_Y → 𝒢` is
zero if and only if `f*(u) : f*(𝒪_Y) = 𝒪_X → f*(𝒢)` is zero.

**Remark (2.2.9).**

<!-- label: IV.2.2.9 -->

*The results of `(2.2.7)` and `(2.2.8)` still hold when the `𝒪_Y`-Modules `𝒢'`, `𝒢`, `𝒢''` appearing there are arbitrary
(not necessarily quasi-coherent). Indeed, for every `y ∈ Y`, there exists `x ∈ f⁻¹(y)` such that `ℱ_x` is a
`𝒪_y`-module*

<!-- original page 12 -->

*faithfully flat, and consequently the functor `𝒢_y ↦ 𝒢_y ⊗_{𝒪_y} ℱ_x` is faithful; since moreover for every
`x ∈ f⁻¹(y)` the functor `𝒢_y ↦ 𝒢_y ⊗_{𝒪_y} ℱ_x` is exact, one deduces the conclusion at once.*

**Proposition (2.2.10).**

<!-- label: IV.2.2.10 -->

*Let `f : X → Y`, `g : Y' → Y`, `h : Y' → Z` be three morphisms of preschemes, `X' = X ×_Y Y'`, `ℱ` a quasi-coherent
`𝒪_X`-Module, faithfully flat relative to `Y`, `𝒢'` a quasi-coherent `𝒪_{Y'}`-Module. For `𝒢'` to be flat (resp.
faithfully flat) relative to `Z`, it is necessary and sufficient that `ℱ ⊗_Y 𝒢'` be a flat (resp. faithfully flat)
`𝒪_{X'}`-Module relative to `Z`.*

One knows already that if `𝒢'` is `Z`-flat, then so is `ℱ ⊗_Y 𝒢'` `(2.1.5)`. Consider an arbitrary base change `Z'' → Z`
and set `X'' = X' ×_Z Z''`; if `𝒢'` is faithfully flat relative to `Z`, the functor

```text
  ℋ'' ↦ ℋ'' ⊗_Z 𝒢' → (ℋ'' ⊗_Z 𝒢') ⊗_Y ℱ = ℋ'' ⊗_Z (𝒢' ⊗_Y ℱ)        (2.2.10.1)
```

from the category of quasi-coherent `𝒪_{Z''}`-Modules to that of `𝒪_{X''}`-Modules is the composite of two exact and
faithful functors, hence is exact and faithful. Conversely, if this composite functor is exact (resp. exact and
faithful), so is `ℳ'' ↦ ℳ'' ⊗_Z 𝒢'`, since the functor `ℳ' ↦ ℳ' ⊗_Y ℱ` (from the category of quasi-coherent
`𝒪_{Y'}`-Modules to that of `𝒪_{X'}`-Modules) is exact and faithful by hypothesis.

**Corollary (2.2.11).**

<!-- label: IV.2.2.11 -->

*(i) Let `f : X → Y`, `g : Y' → Y` be two morphisms, `X' = X ×_Y Y'`, `ℱ` a quasi-coherent `𝒪_X`-Module. If `ℱ` is
faithfully flat relative to `Y`, then `ℱ' = ℱ ⊗_Y 𝒪_{Y'}` is faithfully flat relative to `Y'`.*

*(ii) Let `f : X → Y`, `g : Y → Z` be two morphisms, `ℱ` a quasi-coherent `𝒪_X`-Module, faithfully flat relative to `Y`.
For `g` to be a faithfully flat morphism, it is necessary and sufficient that `ℱ` be faithfully flat relative to `Z`.*

*(iii) Let `f : X → Y`, `g : Y → Z` be two morphisms, `𝒢` a quasi-coherent `𝒪_Y`-Module. Suppose the morphism `f` is
faithfully flat. For `𝒢` to be flat (resp. faithfully flat) relative to `Z`, it is necessary and sufficient that `f*(𝒢)`
be flat (resp. faithfully flat) relative to `Z`.*

*(iv) Let `f : X → Y`, `g : Y → Z` be two morphisms, `x` a point of `X`. Suppose `f` is flat at the point `x`. For
`g ∘ f` to be flat at the point `x`, it is necessary and sufficient that `g` be flat at the point `f(x)`.*

To prove (i), one applies `(2.2.10)` replacing `Z` by `Y'` and `𝒢'` by `𝒪_{Y'}`. To prove (ii), one applies `(2.2.10)`
taking the identity for the morphism `Y' → Y` and replacing `𝒢'` by `𝒪_Y`. To prove (iii), one applies `(2.2.10)` again
taking the identity for `Y' → Y` and replacing `ℱ` by `𝒪_X` and `𝒢'` by `𝒢`. Finally (iv) is deduced from (ii) by
replacing `X` by `Spec(𝒪_x)`, `ℱ` by `𝒪_X`, `Y` by `Spec(𝒪_{f(x)})`, and `Z` by `Spec(𝒪_{g(f(x))})`, taking account of
`(0_I, 6.6.2)`.

**Corollary (2.2.12).**

<!-- label: IV.2.2.12 -->

*Let `Y` be an affine scheme, `f : X → Y` a quasi-compact morphism, `ℱ` a quasi-coherent `𝒪_X`-Module. If `ℱ` is
faithfully flat relative to `f`, there exists an affine scheme `X'` and a surjective local isomorphism `g : X' → X` such
that `g*(ℱ)` is faithfully flat relative to `f ∘ g`.*

Indeed, `X` is quasi-compact, hence a finite union of affine open sets `X_i`; it suffices to take for `X'` the affine
scheme sum of the preschemes induced on the open sets `X_i`, and for `g : X' → X` the canonical morphism; it is clear
that `g` is faithfully flat, and

<!-- original page 13 -->

the hypothesis entails that `g*(ℱ)` is faithfully flat relative to `f ∘ g`, by virtue of `(2.2.11, (iii))`.

**Corollary (2.2.13).**

<!-- label: IV.2.2.13 -->

*(i) Let `f : X → Y`, `g : Y' → Y` be two morphisms, `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`. If `f` is a faithfully
flat morphism, so is `f'`.*

*(ii) If `f : X → X'`, `g : Y → Y'` are two faithfully flat `S`-morphisms, then*

```text
  f ×_S g : X ×_S Y → X' ×_S Y'
```

*is faithfully flat.*

*(iii) Let `f : X → Y`, `g : Y → Z` be two morphisms such that `f` is faithfully flat. For `g` to be a flat (resp.
faithfully flat) morphism, it is necessary and sufficient that `g ∘ f` be a flat (resp. faithfully flat) morphism.*

**Proposition (2.2.14).**

<!-- label: IV.2.2.14 -->

*Let `f : X → Y` be a faithfully flat and quasi-compact morphism. If `X` is locally Noetherian, so is `Y`.*

The question being local on `Y`, one may suppose `Y = Spec(A)` affine; since `f` is quasi-compact, it follows from
`(2.2.12)` that one may also restrict to the case where `X = Spec(B)` is affine. Then `B` is a Noetherian ring by
hypothesis, and a faithfully flat `A`-module `(2.2.3)`; hence `A` is Noetherian `(0_I, 6.5.2)`.

**Proposition (2.2.15).**

<!-- label: IV.2.2.15 -->

*Let `f : X → Y` be a faithfully flat morphism. If `𝔖(X)` and `𝔖(Y)` denote respectively the set of sub-preschemes of
`X` and `Y`, the map `Z ↦ f⁻¹(Z)` from `𝔖(Y)` to `𝔖(X)` is injective.*

Since `f` is surjective, one has, for the underlying set of a sub-prescheme `Z` of `Y`, `f(f⁻¹(Z)) = Z`. On the other
hand, if `U` is an open set of `Y` containing `Z` and in which `Z` is closed, `f⁻¹(U)` is open in `X`, `f⁻¹(Z)` is
closed in `f⁻¹(U)`, and the restriction `f⁻¹(U) → U` of `f` is a faithfully flat morphism. One may therefore restrict to
considering only closed sub-preschemes of `Y`. Now, if `Z` is a closed sub-prescheme of `Y` corresponding to a
quasi-coherent Ideal `𝒥` of `𝒪_Y`, one knows that `f⁻¹(Z)` corresponds to the quasi-coherent Ideal `f*(𝒥) 𝒪_X` of `𝒪_X`
`(I, 4.4.5)`, and since `f` is flat, `f*(𝒥) 𝒪_X` is identified with `f*(𝒥)`. But the map `𝒥 ↦ f*(𝒥)` from the set of
quasi-coherent Ideals of `𝒪_Y` to the set of quasi-coherent Ideals of `𝒪_X` is injective `(2.2.7)`, whence the
conclusion.

**Corollary (2.2.16).**

<!-- label: IV.2.2.16 -->

*Let `X`, `Y` be two `S`-preschemes; if `S' → S` is a faithfully flat morphism, the map `f ↦ f_{(S')}` from
`Hom_S(X, Y)` to `Hom_{S'}(X_{(S')}, Y_{(S')})` is injective.*

One has `X_{(S')} ×_{S'} Y_{(S')} = (X ×_S Y)_{(S')}` `(I, 3.3.10)`, so the projection morphism
`X_{(S')} ×_{S'} Y_{(S')} → X ×_S Y` is faithfully flat `(2.2.13)`. The elements of `Hom_S(X, Y)` correspond bijectively
to the sub-preschemes of `X ×_S Y` that are the *graphs* of these `S`-morphisms `(I, 5.3.11)`, and if `Z_f` is the graph
of `f ∈ Hom_S(X, Y)`, one has `Z_{f_{(S')}} = g⁻¹(Z_f)` `(I, 5.3.12)`. It therefore suffices to apply proposition
`(2.2.15)` to `g`.

**Proposition (2.2.17).**

<!-- label: IV.2.2.17 -->

*Let `A` be a ring, `B` an `A`-algebra such that `B` is a faithfully flat and finitely presented `A`-module. Then the
structure homomorphism `φ : A → B` is an isomorphism of the `A`-module `A` onto a direct factor of the `A`-module `B`.
If `A` is a local ring, `B` is a free `A`-module and there exists a basis of this module containing the unit element of
`B`.*

<!-- original page 14 -->

By virtue of Bourbaki, _Alg. comm._, chap. II, §3, n° 3, prop. 12, it suffices to prove the proposition when `A` is a
local ring; one then knows (_loc. cit._, n° 2, cor. 2 of prop. 5) that `B` is a free `A`-module of finite type, and the
conclusion follows from _loc. cit._, prop. 5.

### 2.3. Topological properties of flat morphisms

**Lemma (2.3.1).**

<!-- label: IV.2.3.1 -->

*Let `f : X → Y` be a quasi-compact and quasi-separated morphism, `g : Y' → Y` a flat morphism; set `X' = X ×_Y Y'`,
`f' = f_{(Y')} : X' → Y'`. Then, for every quasi-coherent `𝒪_X`-Module `ℱ`, the canonical homomorphism*

```text
  g*(f_*(ℱ)) → f'_*(ℱ ⊗_{𝒪_X} 𝒪_{X'})                            (2.3.1.1)
```

*is bijective.*

This is a particular case of `(III, 1.4.15)` (improved in `(1.7.21)`).

**Proposition (2.3.2).**

<!-- label: IV.2.3.2 -->

*Let `S` be a prescheme, `f : X → Y` a quasi-compact and quasi-separated `S`-morphism; let `Z` be the sub-prescheme of
`Y`, closed image of `X` under `f` `((I, 9.5.3)` and `(1.7.8))`, and let `j : Z → Y` be the canonical injection, so that
one has `f = j ∘ g`, where `g : X → Z` is a morphism `(loc. cit.)`. Let `h : S' → S` be a flat morphism, and set
`f' = f_{(S')} : X_{(S')} → Y_{(S')}`; then `j' = j_{(S')} : Z_{(S')} → Y_{(S')}` is identified with the canonical
injection of the sub-prescheme of `Y_{(S')}` closed image of `X_{(S')}` under `f'`.*

Since the morphism `Y_{(S')} → Y` is flat `(2.1.4)`, one may restrict to the case where `S = Y` `(I, 3.3.11)`; if
`f = (ψ, θ)`, one knows that `Z` is the closed sub-prescheme of `S` defined by the (quasi-coherent) Ideal `𝒥` of `𝒪_S`,
kernel of the homomorphism `θ : 𝒪_S → f_*(𝒪_X)` `(I, 9.5.2)`. Since `h` is a flat morphism, the quasi-coherent Ideal
`𝒥 𝒪_{S'}` of `𝒪_{S'}` is identified with the kernel of `h*(θ) : 𝒪_{S'} → h*(f_*(𝒪_X))`. Now, if `f' = (ψ', θ')`, one
verifies easily (for example by reducing to the case where `Y` and `Y'` are affine and using `(I, 2.2.4)`) that
`θ' : 𝒪_{S'} → f'_*(𝒪_{X'})` is the composite of the canonical homomorphism `(2.3.1.1)` `h*(f_*(𝒪_X)) → f'_*(𝒪_{X'})`
and of `h*(θ)`; the conclusion therefore follows from `(2.3.1)` and `(I, 9.5.2)`, since `f` is quasi-compact and
quasi-separated `(1.1.2 and 1.2.2)`.

**(2.3.3)**

<!-- label: IV.2.3.3 -->

We shall say that a morphism `f : X → Y` is **quasi-flat** if there exists a quasi-coherent `𝒪_X`-Module `ℱ` of finite
type that is `f`-flat and whose support is equal to `X`. We shall say that `f` is **quasi-faithfully flat** if it is
quasi-flat and surjective. Every flat (resp. faithfully flat) morphism is quasi-flat (resp. quasi-faithfully flat),
since then `ℱ = 𝒪_X` satisfies the preceding conditions.

It follows at once from `(2.1.4)` and `(I, 9.1.13)` that if `f` is quasi-flat, then for every morphism `Y' → Y` the
morphism `f_{(Y')} : X ×_Y Y' → Y'` is quasi-flat. Similarly (taking `(I, 3.5.2)` into account), if `f` is
quasi-faithfully flat, so is `f_{(Y')}`.

**Proposition (2.3.4).**

<!-- label: IV.2.3.4 -->

*Let `f : X → Y` be a quasi-flat morphism `(2.3.3)`. Then `f` possesses the following properties (which are equivalent
by virtue of `(1.10.4)`):*

*(i) For every `x ∈ X` and every generization `y'` of `y = f(x)`, there exists a generization `x'` of `x` such that
`f(x') = y'`.*

*(ii) For every `x ∈ X`, the image under `f` of `Spec(𝒪_{X,x})` is `Spec(𝒪_{Y,y})`.*

<!-- original page 15 -->

*(iii) For every irreducible closed part `Y'` of `Y`, every irreducible component of `f⁻¹(Y')` dominates `Y'`.*

It suffices, for example, to prove (ii). By hypothesis, there is a quasi-coherent `𝒪_X`-Module of finite type `ℱ`, which
is `f`-flat and such that `Supp(ℱ) = X`. For every `x ∈ X`, `ℱ_x` is then an `𝒪_x`-module of finite type, not reduced to
`0`, and moreover `ℱ_x` is a flat `𝒪_y`-module, for the homomorphism `ρ : 𝒪_y → 𝒪_x`. Since this latter is local and
`ℱ_x ≠ 0`, Nakayama's lemma shows that `ℱ_x ⊗_{𝒪_y} k(y) ≠ 0`, hence `ℱ_x` is a faithfully flat `𝒪_y`-module
`(0_I, 6.4.1)`. It results that for every prime ideal `𝔮` of `𝒪_y`, there exists a prime ideal `𝔭` of `𝒪_x` such that
`𝔮 = ρ⁻¹(𝔭)` `(0_I, 6.5.1)`, which proves (ii).

**Corollary (2.3.5).**

<!-- label: IV.2.3.5 -->

*Let `f : X → Y` be a morphism satisfying the equivalent conditions (i), (ii), (iii) of `(2.3.4)` (in particular a
quasi-flat morphism, or an open morphism `(1.10.4)`).*

*(i) Let `Z`, `Z'` be two irreducible closed parts of `Y` such that `Z ⊂ Z'`, and let `T` be an irreducible component of
`f⁻¹(Z)`; then there exists an irreducible component `T'` of `f⁻¹(Z')` containing `T` (and dominating `Z'`).*

*(ii) For every irreducible component `T` of `X`, `‾{f(T)}` is an irreducible component of `Y`.*

*(iii) Suppose `Y` is irreducible, and, if `y` is its generic point, suppose that `f⁻¹(y)` is irreducible. Then `X` is
irreducible.*

(i) It suffices to apply `(2.3.4, (i))` taking for `x` the generic point of `T` (`y = f(x)` then being the generic point
of `Z`) and for `y'` the generic point of `Z'`.

(ii) It is clear that `f(T) = Z` is irreducible, and by virtue of (i), `Z` cannot be strictly contained in an
irreducible closed part `Z'` of `Y`.

(iii) By virtue of (ii), every irreducible component of `X` dominates `Y`, hence meets `f⁻¹(y)`; the conclusion then
follows from `(0_I, 2.1.8)`.

**Proposition (2.3.6).**

<!-- label: IV.2.3.6 -->

*Let `Y` be a prescheme whose set of irreducible components is locally finite (which is the case if the space underlying
`Y` is locally Noetherian (cf. `(I, 6.1.9)`)).*

*(i) Every closed part `W` of `Y` stable under generization `(0_I, 2.1.2)` is open. In particular, every connected
component of `Y` is open.*

*(ii) Let `f : X → Y` be a closed morphism satisfying moreover the equivalent conditions (i), (ii), (iii) of `(2.3.4)`
(which will be the case if `f` is quasi-flat or open). Then the image under `f` of every connected component `C` of `X`
is a connected component of `Y`.*

*(iii) Let `f : X → Y` be a morphism satisfying the equivalent conditions (i), (ii), (iii) of `(2.3.4)` and such
moreover that for every `y ∈ Y` the set `f⁻¹(y)` is finite (which will be the case if `f` is quasi-finite or radicial).
Then the set of irreducible components of `X` is locally finite.*

(i) If `y ∈ W`, the generic points `η_i` (`1 ≤ i ≤ m`) of the irreducible components `Y_i` of `Y` containing `y` belong
by hypothesis to `W`; hence, since `W` is closed, these components themselves are contained in `W`; since by hypothesis
there is a neighbourhood `U` of `y` such that `U` is the union of the `U ∩ Y_i` `(0_I, 2.1.6)`, one has `U ⊂ W`, so `W`

<!-- original page 16 -->

is open. Since for every `y ∈ Y`, `‾{y}` is connected, a connected component of `Y` is stable under generization, so the
second assertion follows at once from the first.

(ii) Since `C` is closed in `X`, `f(C)` is closed in `Y` by hypothesis. Furthermore, since `C` is stable under
generization, the hypothesis on `f` entails that `f(C)` is stable under generization; hence, by virtue of (i), `f(C)` is
open and closed, and since it is connected it is a connected component of `Y`.

(iii) Let `x ∈ X`; by hypothesis, there is an open neighbourhood `U` of `y = f(x)` meeting only a finite number of
irreducible components `Y_i` of `Y` (`1 ≤ i ≤ n`); let `y_i` be the generic point of `Y_i` (`1 ≤ i ≤ n`). For every
irreducible component `Z` of `X` meeting `f⁻¹(U)`, the generic point `z` of `Z` is necessarily in one of the sets
`f⁻¹(y_i)` `(2.3.4)`. Since each of these sets is finite by hypothesis, this proves our assertion.

**Proposition (2.3.7).**

<!-- label: IV.2.3.7 -->

*Let `f : X → Y` be a morphism, `g : Y' → Y` a quasi-flat morphism, `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`.*

*(i) If `f` is quasi-compact and dominant, so is `f'`.*

*(ii) If every irreducible component of `X` dominates an irreducible component of `Y`, then every irreducible component
of `X'` dominates an irreducible component of `Y'`.*

Denote by `g' : X' → X` the canonical projection, which is a quasi-flat morphism `(2.3.3)`.

(i) One already knows `(1.1.2)` that `f'` is quasi-compact; furthermore, if `y'` is a maximal point `(1.1.4)` of `Y'`,
`y = g(y')` is a maximal point of `Y`, as results from `(2.3.4, (iii))`. By hypothesis `(1.1.5)` there exists `x ∈ X`
such that `f(x) = y`; hence `(I, 3.4.7)` there exists `x' ∈ X'` such that `f'(x') = y'`.

(ii) Let `x'` be a maximal point of `X'`, and let `x = g'(x')`; it follows from `(2.3.4, (ii))` that `x` is a maximal
point of `X`, and by hypothesis `y = f(x)` is a maximal point of `Y`. Set `y' = f'(x')`, so that `g(y') = y`; the issue
is to show that `y'` is a maximal point of `Y'`. By virtue of `(I, 5.1.7)` and `(2.3.3)`, one may restrict to the case
where `X` and `Y` are reduced, so `𝒪_x` and `𝒪_y` are fields; moreover, by virtue of `(I, 3.6.5)` applied twice and of
`(I, 2.4.4)`, one may restrict to the case where `Y = Spec(𝒪_y)` and `Y' = Spec(𝒪_{y'})`. Then `f` is a flat morphism
since `𝒪_y` is a field `(2.1.2)`, and the same is true of `f'` `(2.1.4)`; hence it follows from `(2.3.4, (ii))` that
`y' = f'(x')` is a maximal point of `Y'`.

**Corollary (2.3.8) (Zariski).**

<!-- label: IV.2.3.8 -->

*Let `A`, `B` be two Noetherian local rings, `𝔪`, `𝔫` their respective maximal ideals, `φ : A → B` a local homomorphism.
Suppose the following hypotheses are satisfied:*

*1° `B` is an `A`-algebra essentially of finite type `(1.3.8)`.*

*2° The completion `Â` of `A` for the `𝔪`-adic topology is integral.*

*3° `φ` is injective.*

*Then the `𝔪`-adic topology of `A` is induced by the `𝔫`-adic topology of `B`.*

Set `B' = B ⊗_A Â`; by virtue of 1°, `B'` is of the form `S⁻¹(C ⊗_A Â)`, where `C` is an `A`-algebra of finite type and
`S` a multiplicative subset of `C`, so `B'` is a Noetherian ring. Since `A` is identified with a subring of `Â`
`(0_I, 7.3.5)`, `A` is integral by 2°. Hypothesis 3° then entails that there exists a prime ideal `𝔮` of `B` inducing
the ideal `0` of `A` `(0_I, 1.5.8)`, and consequently the local homomorphism `A → B/𝔮` is injective. One may therefore
restrict to proving the conclusion of `(2.3.8)` by adding the hypothesis that `B` is an integral local ring. Apply
`(2.3.7, (ii))` to `Y = Spec(A)`, `X = Spec(B)`, `Y' = Spec(Â)` and `X' = Spec(B')`; since the morphism `Y' → Y` is flat
and `X`

<!-- original page 17 -->

(which is integral) dominates the integral scheme `Y`, every irreducible component of `X'` dominates the scheme
(integral by hypothesis) `Y'`. If `y`, `x`, `y'` are the closed points of `Y`, `X`, `Y'` respectively, there is a point
`x' ∈ X'` (in fact unique) above `x` and `y'` `(I, 3.4.9)` and `Spec(𝒪_{x'})` therefore dominates `Spec(𝒪_{y'})`;
consequently one has a commutative diagram of local homomorphisms of Noetherian local rings

```text
  B = 𝒪_x ────────→ 𝒪_{x'}
    ↑                  ↑
   φ│                 │v
    │                  │
  A = 𝒪_y ────u────→ 𝒪_{y'} = Â
```

such that `u` and `v` are injective `(I, 1.2.7)`; identifying `A` and `Â` with subrings of `𝒪_{x'}`, and denoting by `𝔯`
the maximal ideal of `𝒪_{x'}`, the intersection of the ideals `𝔯^k ∩ Â` is therefore zero `(0_I, 7.3.5)`; since `Â` is
complete and these ideals are open in `Â`, this entails (Bourbaki, _Alg. comm._, chap. III, §2, n° 7, prop. 8) that the
topology of `Â` is induced by the `𝔯`-preadic topology of `𝒪_{x'}`; a fortiori the same is true of the topology of `A`
`(0_I, 7.3.5)`. Moreover one has `𝔫^k ∩ A ⊂ 𝔯^k ∩ A`, so the `𝔫`-preadic topology of `B` induces on `A` a topology finer
than the `𝔪`-preadic topology; but since `𝔪^k ⊂ 𝔫^k ∩ A`, these two topologies are identical. Q.E.D.

**Remark (2.3.9).**

<!-- label: IV.2.3.9 -->

*We shall see further on `(7.8.3, (vii))` that for the Noetherian local rings `A` most usual in algebraic geometry, the
hypothesis that `A` is integral and integrally closed implies that the same holds for `Â`. That is why, in algebraic
geometry over a base field, one generally states `(2.3.8)` under the hypothesis that `A` is integral and integrally
closed.*

**Theorem (2.3.10).**

<!-- label: IV.2.3.10 -->

*Let `f : X → Y` be a quasi-flat morphism `(2.3.3)`. Then, for every proconstructible part `(1.9.4)` `Z` of `Y`, one has
`‾{f⁻¹(Z)} = f⁻¹(‾Z)`.*

Since `f` is continuous, one has `f⁻¹(Z) ⊂ f⁻¹(‾Z)` and everything reduces to proving that for every `x ∈ X` such that
`f(x) ∈ ‾Z`, `x` is adherent to `f⁻¹(Z)`; it is clear that the question is local on `Y`, so one may suppose `Y` affine.
By virtue of the hypothesis, there exists an affine scheme `Y'` and a morphism `g : Y' → Y` such that `g(Y') = Z`
`(1.9.5, (ix))`. Let `Y_1` be the closed image of `Y'` under `g` `(I, 9.5.3)`, and let `X_1` be the closed sub-prescheme
`f⁻¹(Y_1)` of `X`; if `f_1 : X_1 → Y_1` is the restriction of `f` to `X_1`, one knows that `f_1` is quasi-flat
`(2.3.3)`; one may therefore replace `X`, `Y` by `X_1`, `Y_1` respectively, in other words suppose that `g` is dominant.
Set then `X' = X ×_Y Y'`, and let `f'` and `g'` be the projections of `X'` onto `Y'` and `X` respectively, so that one
has the commutative diagram

```text
  X  ←─g'──  X'
  │           │
  f│         │f'
  ↓           ↓
  Y  ←──g──  Y'
```

Since `f` is quasi-flat, `g` quasi-compact and dominant, it follows from `(2.3.7)` (where the roles of `f` and `g` are
interchanged) that `g'` is a dominant morphism, which proves the theorem.

**Corollary (2.3.11).**

<!-- label: IV.2.3.11 -->

*Let `f` be a quasi-flat and quasi-compact morphism, `F` a closed part of `X` such that `F = f⁻¹(f(F))`; then one has
`F = f⁻¹(‾{f(F)})`.*

Let `Y'` be the reduced sub-prescheme of `X` having `F` as underlying space `(I, 5.2.1)` and let `j : Y' → X` be the
canonical injection; then `f ∘ j` is quasi-compact `(1.1.2)`,

<!-- original page 18 -->

so `Z = f(F)` is pro-constructible in `Y` `(1.9.5, (vii))`, and the corollary follows from the fact that `F` is closed.

One may further write the result of `(2.3.11)` in the form `F = f⁻¹(f(X) ∩ ‾{f(F)})`, in other words, the closed sets of
the subspace `f(X)` of `Y` are the parts `Z ⊂ f(X)` such that `f⁻¹(Z)` is closed in `X`; this also means that *the
topology induced by `Y` on `f(X)` is the quotient of that of `X` by the equivalence relation defined by `f`*. In
particular:

**Corollary (2.3.12).**

<!-- label: IV.2.3.12 -->

*Let `f : X → Y` be a quasi-faithfully flat `(2.3.3)` and quasi-compact morphism. Then the topology of `Y` is the
quotient of that of `X` by the equivalence relation defined by `f` (in other words, for `Z ⊂ Y` to be open (resp.
closed) in `Y`, it is necessary and sufficient that `f⁻¹(Z)` be open (resp. closed) in `X`).*

Indeed, one then has `f(X) = Y`.

**Corollary (2.3.13).**

<!-- label: IV.2.3.13 -->

*Let `X`, `Y` be two `S`-preschemes, `f : X → Y` a faithfully flat and quasi-compact `S`-morphism. For `Y` to be
separated over `S`, it is necessary and sufficient that the canonical immersion `j : X ×_Y X → X ×_S X` `(I, 5.3.10)` be
closed.*

Let us note for this that one has the commutative diagram `(I, 5.3.5)`

```text
  X ×_Y X  ──j──→  X ×_S X
    │                │
    π│              │f ×_S f
    ↓                ↓
    Y    ──Δ_Y──→  Y ×_S Y
```

identifying `X ×_Y X` with the product of the `(Y ×_S Y)`-preschemes `Y` and `X ×_S X`. Since `f` is surjective, so are
`π` and `f ×_S f`, so the diagonal `Δ_Y(Y)` has as inverse image under `f ×_S f` the image `j(X ×_Y X)` `(I, 3.4.8)`.
Since `f ×_S f` is faithfully flat and quasi-compact `(1.1.2 and 2.2.13)`, it suffices to apply `(2.3.12)` to this
morphism.

**Corollary (2.3.14).**

<!-- label: IV.2.3.14 -->

*Let `f : X → Y` be a quasi-faithfully flat and quasi-compact morphism, and let `Z` be a part of `Y`. For `Z` to be a
locally closed pro-constructible part of `Y`, it is necessary and sufficient that `f⁻¹(Z)` be a locally closed
pro-constructible part of `X`.*

One already knows `(1.9.12)` that, for `Z` to be a pro-constructible part of `Y`, it is necessary and sufficient that
`f⁻¹(Z)` be a pro-constructible part of `X`. The condition is evidently necessary. To prove that it is sufficient,
consider the reduced closed sub-prescheme `Y_1` of `Y` having `‾Z` as underlying space, and let `X_1` be its inverse
image under `f`, which has as underlying space `f⁻¹(‾Z) = ‾{f⁻¹(Z)}` by virtue of `(2.3.10)`. Since `f⁻¹(Z)` is locally
closed in `X`, it is open in `‾{f⁻¹(Z)}`, hence in `X_1`; now the morphism `f_1 : X_1 → Y_1` deduced from `f` by
restriction is quasi-faithfully flat and quasi-compact `(1.1.2 and 2.3.3)`; one therefore deduces from `(2.3.12)` that
`Z` is open in `‾Z`, which shows that `Z` is locally closed in `Y`.

**Remark (2.3.15).**

<!-- label: IV.2.3.15 -->

*It does not suffice, in `(2.3.12)`, to suppose only that `f` is faithfully flat. For example, take for `Y` a reduced
irreducible algebraic curve*

<!-- original page 19 -->

*`(II, 7.4.2)`, for `X` the prescheme sum of the schemes `Spec(𝒪_y)`, where `y` runs over `Y` `(I, 3.1)`, for `f` the
canonical morphism, which is faithfully flat `(I, 2.4.2)`; if `η` denotes the generic point of `Y`, `Z = {η}` is not
open in `Y` `(II, 7.4.3)`, but `f⁻¹(Z) = Spec(𝒪_η)` since `𝒪_η` is a field, and consequently `f⁻¹(Z)` is open in `X`.*

### 2.4. Universally open morphisms and flat morphisms

**(2.4.1)**

<!-- label: IV.2.4.1 -->

We have already defined `(II, 5.4.9)` the notion of *universally closed* morphism; in the same way, one poses the
following definitions:

**Definition (2.4.2).**

<!-- label: IV.2.4.2 -->

*One says that a morphism of preschemes `f : X → Y` is **universally open** (resp. **universally bicontinuous**, resp. a
**universal homeomorphism**) if, for every morphism `g : Y' → Y`, the morphism `f_{(Y')} : X ×_Y Y' → Y'` is open (resp.
a homeomorphism onto its image, resp. a homeomorphism onto `Y'`).*

We shall see further on `(14.3.2)` that when `Y` is locally Noetherian, the definition of universally open morphism
given here is equivalent to the definition `(III, 4.3.9)` for morphisms of finite type; the reader may verify that we do
not use this latter definition before §14.

**Proposition (2.4.3).**

<!-- label: IV.2.4.3 -->

*(i) An immersion (resp. an open immersion, resp. a closed immersion) is universally bicontinuous (resp. universally
open, resp. universally closed).*

*(ii) The composite of two universally open (resp. universally closed, resp. universally bicontinuous, resp. two
universal homeomorphisms) morphisms is also.*

*(iii) If `f : X → Y` is a universally open (resp. universally closed, resp. universally bicontinuous, resp. a universal
homeomorphism) `S`-morphism, so is `f_{(S')} : X_{(S')} → Y_{(S')}` for every base change `S' → S`.*

*(iv) If `f : X → X'`, `g : Y → Y'` are two universally open (resp. universally closed, resp. universally bicontinuous,
resp. two universal homeomorphism) `S`-morphisms, so is `f ×_S g : X ×_S Y → X' ×_S Y'`.*

*(v) Let `f : X → Y`, `g : Y → Z` be two morphisms such that `f` is surjective; if `g ∘ f` is universally open (resp.
universally closed, resp. universally bicontinuous, resp. a universal homeomorphism), so is `g`.*

*(vi) For `f` to be a universally open (resp. universally closed, resp. universally bicontinuous, resp. a universal
homeomorphism) morphism, it is necessary and sufficient that `f_red` be so.*

*(vii) Let `(U_α)` be an open cover of `Y`. For `f : X → Y` to be universally open (resp. universally closed, resp.
universally bicontinuous, resp. a universal homeomorphism), it is necessary and sufficient that for every `α`, its
restriction `f⁻¹(U_α) → U_α` be so.*

Assertion (i) results from `(I, 4.3.2)`. Assertion (ii) follows at once from the definitions, and so does (iii) on
reducing to the case where `Y = S`, `Y' = S'`, which one may do thanks to `(I, 3.3.11)`; one knows that (iv) follows
from (ii) and (iii) `(I, 3.5.1)`. To prove (v), note that for every morphism `Z' → Z`, `f_{(Z')} : X_{(Z')} → Y_{(Z')}`
is surjective `(I, 3.5.2)`; one may therefore restrict to proving that if `g ∘ f` is open (resp. closed, resp. a

<!-- original page 20 -->

homeomorphism onto its image, resp. a bijective homeomorphism), so is `g`, and so the matter is a purely topological
question. For the case where `g ∘ f` is open (resp. closed), the fact that `g` is then open (resp. closed) results from
Bourbaki, _Top. gén._, chap. I, 3rd ed., §5, n° 1, prop. 1; for the two other cases, one may restrict to supposing that
`g(f(X)) = g(Y) = Z`, in other words to the case where `g ∘ f` is a homeomorphism of `X` onto `Z`; since `f` is
surjective, `g` is necessarily bijective, and since `g` is a continuous open map by what precedes, `g` is indeed a
homeomorphism of `Y` onto `Z`.

To prove (vi), note that saying that a morphism `g` is open (resp. closed, resp. a homeomorphism onto its image, resp. a
bijective homeomorphism) amounts to saying that `g_red` has the same property. On the other hand `(I, 5.1.8)`, for every
morphism `Y' → Y`, one has `(X_red ×_{Y_red} Y'_red)_red = (X ×_Y Y')_red`, so the preceding remark shows that if
`f_red` is universally open (resp. universally closed, resp. universally bicontinuous, resp. a universal homeomorphism),
so is `f`. The converse is proved similarly, noting here that for every morphism `Y'' → Y_red`, one has
`(X_red ×_{Y_red} Y'')_red = (X ×_Y Y'')_red` `(I, 5.1.3)`.

Finally, the necessity of (vii) results at once from (iii). Conversely, suppose condition (vii) holds, and let
`g : Y' → Y` be a morphism; then the `g⁻¹(U_α) = U'_α` form an open cover of `Y'`, and if one denotes by `f_α` the
restriction `f⁻¹(U_α) → U_α` of `f`, and by `f'` the morphism `f_{(Y')}`, the restriction `f'⁻¹(U'_α) → U'_α` is none
other than `(f_α)_{(U'_α)}`. One may therefore restrict to proving that `f` is open (resp. closed, resp. a homeomorphism
onto its image, resp. a homeomorphism onto `Y`), which is immediate.

**Proposition (2.4.4).**

<!-- label: IV.2.4.4 -->

*A universally bicontinuous morphism `f : X → Y` is radicial (hence separated `(1.7.7.1)`).*

Indeed, `f` is universally injective by hypothesis `(I, 3.5.11)`.

**Proposition (2.4.5).**

<!-- label: IV.2.4.5 -->

*(i) A morphism `f : X → Y` that is integral, surjective and radicial is a universal homeomorphism.*

*(ii) Conversely, suppose `Y` locally Noetherian. Then, if a morphism of finite type `f : X → Y` is a universal
homeomorphism, it is finite, surjective and radicial.*

(i) It suffices to observe that the three properties of `f` are preserved by base change
`(I, 3.5.2, I, 3.5.7 and II, 6.1.5)`, and since an integral morphism is closed `(II, 6.1.10)`, it is clear that `f` is a
homeomorphism of `X` onto `Y`.

(ii) Since `f` is of finite type and universally closed by hypothesis and separated by `(2.4.4)`, it is proper
`(II, 5.4.1)`, and for every `y ∈ Y`, `f⁻¹(y)` is reduced to a single element; hence `(III, 4.4.2)` `f` is finite; it is
clear that `f` is surjective, and it is radicial since it is universally injective `(I, 3.5.11)`.

**Theorem (2.4.6).**

<!-- label: IV.2.4.6 -->

*Let `f : X → Y` be a quasi-flat `(2.3.3)` and locally of finite presentation morphism. Then `f` is universally open. In
particular, a flat morphism locally of finite presentation is universally open.*

One knows that for every base change `Y' → Y`, `f_{(Y')}` is quasi-flat `(2.3.3)` and locally of finite presentation
`(1.4.3, (iii))`. It therefore suffices to prove that `f` is an

<!-- original page 21 -->

open morphism. But this follows from criterion `(1.10.4)` for morphisms locally of finite presentation, conditions b),
b'), and c) of `(1.10.4)` being none other than conditions (i), (ii), (iii) of `(2.3.4)`.

**Corollary (2.4.7).**

<!-- label: IV.2.4.7 -->

*For every prescheme `Y`, the structure morphism `𝐕^n_Y → Y` (where `𝐕^n_Y = Y ⊗_ℤ Spec(ℤ[T_1, …, T_n])`, also denoted
`Y[T_1, …, T_n]`) is universally open.*

Indeed, for `Y = Spec(A)`, `Y[T_1, …, T_n] = Spec(A[T_1, …, T_n])`, and `A[T_1, …, T_n]` is a free `A`-algebra of finite
presentation.

**Remarks (2.4.8).**

<!-- label: IV.2.4.8 -->

*(i) One notes that a faithfully flat and quasi-compact morphism `f : X → Y` is not necessarily open, even when `X` and
`Y` are Noetherian. Take for example for `Y` a reduced irreducible algebraic curve `(II, 7.4)` with generic point `y`,
and let `X` be the prescheme sum `Y ⨿ Spec(k(y))`, `f` being the canonical morphism; it is clear that `f` is flat and
surjective, hence faithfully flat, and quasi-compact, but the image under `f` of the open part `Spec(k(y))` of `X` is
the set `{y}`, which is not open in `Y` `(II, 7.4.3)`.*

*(ii) For every prescheme `X`, the canonical morphism `f : X_red → X` is a closed immersion and a universal
homeomorphism `(2.4.4, (vi))`; but when `X` is locally Noetherian, `f` is flat only if `X` is reduced, hence `f = 1_X`
`(2.2.17)`.*

**Proposition (2.4.9).**

<!-- label: IV.2.4.9 -->

*Let `Y` be a discrete prescheme. Then every morphism `f : X → Y` is universally open.*

The question being local on `Y` `(2.4.3, (vii))`, one may restrict to the case where the space underlying `Y` is reduced
to a point; replacing `f` by `f_red` `(2.4.3, (vi))`, one may furthermore suppose that `Y` is the spectrum of a field
`k`; on the other hand, for every base change `Y' → Y`, the open sets of `X' = X ×_Y Y'` inverse images of the affine
open sets of `X` cover `X'`, so one may suppose `X = Spec(B)` affine, `B` being a `k`-algebra. The issue is therefore to
prove that for every `k`-algebra `A'`, if one sets `B' = B ⊗_k A'`, the image under `f' : Spec(B') → Spec(A')` of every
open set of the form `U = D(t)` (`t ∈ B'`) is open in `Spec(A')`. Now, `B` is the direct limit of the increasing
filtered family `(B_α)` of its sub-`k`-algebras of finite type, hence (the functor `lim` commuting with tensor
products), `B'` is the direct limit of the `A'`-algebras `B_α ⊗_k A' = B'_α`; there exists `α` such that `t` is the
image in `B'` of an element `t_α ∈ B'_α`, hence `D(t)` is the inverse image under the canonical morphism
`u_α : Spec(B') → Spec(B'_α)` of the open set `U_α = D(t_α)` `(I, 1.2.2.2)`. But since `k` is a field, `B_α` is a
`k`-algebra of finite presentation and a flat `k`-module, hence `B'_α` is an `A'`-algebra of finite presentation and a
flat `A'`-module; one therefore concludes from `(2.4.6)` that the image of `U_α` under `f'_α : Spec(B'_α) → Spec(A')` is
open in `Spec(A')`. Everything therefore reduces to seeing that `f'(U) = f'_α(U_α)`; it is clear that
`f'(U) ⊂ f'_α(U_α)`, and it therefore remains to see that for every point `y' ∈ f'_α(U_α)`, the intersection
`V = U ∩ f'⁻¹(y')` is non-empty. Now one has `V = v⁻¹(V_α)`, where `V_α = U_α ∩ f'⁻¹_α(y')`; in other words, `V_α` is a
non-empty open set (by definition of `y'`) of the prescheme `Spec(B'_α ⊗_{A'} k(y')) = Spec(B_α ⊗_k k(y'))` and `V` is
its inverse image under the morphism `v : Spec(B ⊗_k k(y')) → Spec(B_α ⊗_k k(y'))`. Since `B_α` is a subalgebra of `B`
and `k` is a field, the homomorphism `B_α ⊗_k k(y') → B ⊗_k k(y')`

<!-- original page 22 -->

is injective by flatness, so the morphism `v` is dominant `(I, 1.2.7)`, which completes the proof.

**Corollary (2.4.10).**

<!-- label: IV.2.4.10 -->

*Let `k` be a field; `X`, `Y` `k`-preschemes; then the projection morphism `X ×_k Y → X` is universally open. In
particular, for every extension `K` of `k`, the projection morphism `X_{(K)} → X` is universally open.*

It suffices to apply `(2.4.9)` to the structure morphism `Y → Spec(k)`.

**Remark (2.4.11).**

<!-- label: IV.2.4.11 -->

*If `f : X → Y` is an open morphism, one knows that, for every part `E` of `Y`, one has `f⁻¹(‾E) = ‾{f⁻¹(E)}` (Bourbaki,
_Top. gén._, chap. I, 3rd ed., §5, n° 4, prop. 7). This remark applies for example when `f` is a flat morphism locally
of finite presentation `(2.4.6)`, or a projection morphism `X ×_k Y → X` where `X`, `Y` are preschemes over a field `k`
`(2.4.10)`, and then generalizes `(2.3.10)`.*

<!-- original page 22 -->

### 2.5. Permanence of properties of Modules under faithfully flat descent

**Proposition (2.5.1).**

<!-- label: IV.2.5.1 -->

*Let `f : X → Y` be a morphism, `ℱ` a quasi-coherent `𝒪_X`-Module, `g : Y' → Y` a faithfully flat morphism,
`X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`, `ℱ' = ℱ ⊗_{𝒪_Y} 𝒪_{Y'}`. For `ℱ` to be flat (resp. faithfully flat) relative
to `f`, it is necessary and sufficient that `ℱ'` be flat (resp. faithfully flat) relative to `f'`.*

It suffices to apply `(2.2.10)` after replacing `X`, `Y'`, `Z`, `ℱ`, `𝒢` by `Y'`, `X`, `Y`, `𝒪_{Y'}`, `ℱ` respectively;
one concludes that for `ℱ'` to be flat (resp. faithfully flat) relative to `f'`, it is necessary and sufficient that `ℱ`
be flat (resp. faithfully flat) relative to `g ∘ f'`. But if `g' : X' → X` is the canonical projection, `g'` is
faithfully flat `(2.2.13)` and one has `g ∘ f' = f ∘ g'`; hence for `ℱ` to be flat (resp. faithfully flat) relative to
`f ∘ g'`, it is necessary and sufficient that `ℱ` be so relative to `f` `(2.2.11, (iii))`.

**Proposition (2.5.2).**

<!-- label: IV.2.5.2 -->

*Let `f : X' → X` be a faithfully flat and quasi-compact morphism, `ℱ` a quasi-coherent `𝒪_X`-Module, `ℱ' = f*(ℱ)`.
Consider, for a quasi-coherent Module, the property of being:*

*(i) of finite type;*

*(ii) of finite presentation;*

*(iii) locally free of finite type;*

*(iv) locally free of rank `n`.*

*Then, if `P` denotes one of the preceding properties, for `ℱ` to possess the property `P` it is necessary and
sufficient that `ℱ'` possess it.*

For a quasi-coherent `𝒪_X`-Module to be locally free of finite type, it is necessary and sufficient that it be flat over
`X` and of finite presentation (Bourbaki, *Alg. comm.*, chap. II, §5, n° 2, cor. 2 of th. 1, taking `(2.1.2)` into
account); since `ℱ` is flat over `X` if and only if `ℱ'` is flat over `X'` by virtue of `(2.5.1)` (applied with `f`
taken to be the identity), one sees that in order to prove the proposition in case (iii) it suffices to have proved it
in cases (i) and (ii); the same holds for (iv), since `f*(𝒪_X) = 𝒪_{X'}`, so that if `ℱ` and `ℱ'` are locally free of
finite type and `x = f(x')`, the rank of `ℱ'` at `x'` equals that of `ℱ` at `x`, and our assertion follows from the
surjectivity of `f`. To treat cases (i) and (ii),

<!-- original page 23 -->

note that the question is local on `X`, and one may therefore suppose `X` affine; one then knows `(2.2.12)` that there
exists an affine scheme `X''` and a faithfully flat morphism `g : X'' → X'` which is a local isomorphism. Consequently,
it amounts to the same thing to say that `f*(ℱ)` possesses the property `P` or that `g*(f*(ℱ))` does. We are thus
reduced to the case where `X = Spec(A)`, `X' = Spec(A')`; in view of `(2.2.3)` and `(II, 6.1.4.1)`, it therefore
suffices to prove the

**Lemma (2.5.3).**

<!-- label: IV.2.5.3 -->

*Let `A` be a ring, `A'` a faithfully flat `A`-algebra, `M` an `A`-module, `M' = M ⊗_A A'`. For `M` to be of finite type
(resp. of finite presentation), it is necessary and sufficient that `M'` be so.*

For the proof, see Bourbaki, *Alg. comm.*, chap. I, §3, n° 6, prop. 11.

**Remark (2.5.4).**

<!-- label: IV.2.5.4 -->

*The assertions of `(2.5.2)` for the properties (i) and (ii) are still valid if one supposes only that `f` is
quasi-faithfully flat `(2.3.3)` and quasi-compact. Indeed, one is reduced (Bourbaki, *loc. cit.*) to proving the*

**Lemma (2.5.4.1).**

<!-- label: IV.2.5.4.1 -->

*Let `ρ : A → A'` be a homomorphism of rings such that the corresponding morphism `f : Spec(A') → Spec(A)` is
surjective; suppose there exists an `A'`-module `N'` of finite type which is `A`-flat and has `Spec(A')` as support.
Then, if `u : P → Q` is a homomorphism of `A`-modules such that `u ⊗ 1 : P ⊗_A A' → Q ⊗_A A'` is surjective, `u` is
surjective.*

Indeed, one deduces first that the homomorphism `u ⊗ 1_{N'} : (P ⊗_A A') ⊗_{A'} N' → (Q ⊗_A A') ⊗_{A'} N'` is
surjective. Let `𝔮` be a prime ideal of `A'`, and let `𝔭 = ρ⁻¹(𝔮)`; the corresponding homomorphism
`(P ⊗_A N')_𝔮 → (Q ⊗_A N')_𝔮` is surjective, and it can be written `u_𝔭 ⊗ 1 : P_𝔭 ⊗_{A_𝔭} N'_𝔮 → Q_𝔭 ⊗_{A_𝔭} N'_𝔮`
`(0_I, 1.5.4)`. By hypothesis `N'_𝔮 ≠ 0`, and `N'_𝔮` is a flat `A_𝔭`-module `(0_I, 6.3.1)`; by virtue of Nakayama's
lemma, `𝔮 N'_𝔮 ≠ N'_𝔮`, and a fortiori `𝔭 N'_𝔮 ≠ N'_𝔮`, so `N'_𝔮` is a faithfully flat `A_𝔭`-module `(0_I, 6.4.1)`. It
follows that `u_𝔭` is surjective `(0_I, 6.4.1)`, and since this holds for every `𝔭 ∈ Spec(A)`, `f` being surjective, one
finally concludes that `u` is surjective (Bourbaki, *Alg. comm.*, chap. II, §3, n° 3, th. 1).

**Proposition (2.5.5).**

<!-- label: IV.2.5.5 -->

*Let `f : X → Y` be a morphism, `ℱ` a quasi-coherent `𝒪_X`-Module of finite type and `f`-flat, `𝒢` a quasi-coherent
`𝒪_Y`-Module of finite type; for every `y ∈ Y`, put `ℱ_y = ℱ ⊗_{𝒪_Y} k(y)`. For a point `x ∈ X` to be a maximal point of
`Supp(ℱ ⊗_Y 𝒢)`, it is necessary and sufficient that `y = f(x)` be a maximal point of `Supp(𝒢)` and that `x` be a
maximal point of `Supp(ℱ_y)` in `f⁻¹(y)`. When this is so, one has*

```text
(2.5.5.1)         long((ℱ ⊗_Y 𝒢)_x) = long(𝒢_y) · long((ℱ_y)_x).
```

It is clear that `f(Supp(ℱ ⊗_Y 𝒢)) ⊂ Supp(𝒢)` `(0_I, 5.2.2)`; the image under `f` of every irreducible component of
`Supp(ℱ ⊗_Y 𝒢)` is therefore contained in an irreducible component of `Supp(𝒢)`. One may restrict to the case where
`Supp(𝒢) = Y`. Indeed `(Err_II, 30)`, since `𝒢` is of finite type, there exists a closed sub-prescheme `Y'` of `Y`
having `Supp(𝒢)` as underlying space and a quasi-coherent `𝒪_{Y'}`-Module of finite type `𝒢_1` such that, if
`j : Y' → Y` is the canonical injection, one has `𝒢 = j_*(𝒢_1)`. If one then puts `f_1 = j ∘ f'`, where
`f' : X' = X ×_Y Y' → Y'`, it is clear that `ℱ' = ℱ ⊗_Y 𝒪_{Y'}` is `f'`-flat and that
`Supp(ℱ' ⊗_{Y'} 𝒢_1) = Supp(ℱ ⊗_Y 𝒢)`.

Suppose therefore `Supp(𝒢) = Y`; if `Z` is an irreducible component of `Supp(𝒢)`, one has `f⁻¹(Z) ⊂ Supp(ℱ ⊗_Y 𝒢)`
`(I, 9.1.13)`, and it follows from `(2.3.4)` that every irreducible component of `f⁻¹(Z)` dominates `Z`. In other words,
if `x` is the generic point of an irreducible component of `Supp(ℱ ⊗_Y 𝒢)` contained in `f⁻¹(Z)`, then `y = f(x)` is the
generic point of `Z`; furthermore `(0_I, 2.1.8)`, `x` is the generic point of an irreducible component of
`f⁻¹(y) = Supp(ℱ_y)` `(I, 9.1.13)`, and conversely every generic point of one of these components is the generic point
of an irreducible component of `f⁻¹(Z)`.

<!-- original page 24 -->

It remains to prove `(2.5.5.1)`; one has `(ℱ ⊗_Y 𝒢)_x = ℱ_x ⊗_{𝒪_y} 𝒢_y` `(I, 9.1.12)` and `(ℱ_y)_x = ℱ_x / 𝔪_y ℱ_x`;
one is therefore reduced to proving the

**Lemma (2.5.5.2).**

<!-- label: IV.2.5.5.2 -->

*Let `A`, `B` be two local rings, `ρ : A → B` a local homomorphism, `𝔪` the maximal ideal of `A`. Let `M` be an
`A`-module, `N` a `B`-module which is a faithfully flat `A`-module and is such that `N/𝔪 N` is a `B`-module of finite
length; then one has*

```text
(2.5.5.3)         long_B(M ⊗_A N) = long_A(M) · long_B(N/𝔪 N).
```

If `M` has infinite length, then so does `M ⊗_A N`, for every strictly increasing sequence of `n` sub-modules `M_i ⊂ M`
(`1 ≤ i ≤ n`) yields sub-modules `M_i ⊗_A N` of `M ⊗_A N` which are pairwise distinct; since `N ≠ 𝔪 N` (because `N` is a
faithfully flat `A`-module), the formula `(2.5.5.3)` is true in this case. Suppose then that `M` has finite length. If
`M = 0`, both members of `(2.5.5.3)` are zero, so we may suppose `M ≠ 0`. The `𝔪^k M` are sub-modules of `M`, hence of
finite length, and if `𝔪^k M ≠ 0`, Nakayama's lemma implies `𝔪^{k+1} M ≠ 𝔪^k M`; consequently there exists necessarily
an integer `r` such that `𝔪^r M = 0`. The `𝔪^k M ⊗_A N` then identify with sub-`B`-modules of `M ⊗_A N`, and
`(𝔪^k M ⊗_A N) / (𝔪^{k+1} M ⊗_A N)` is isomorphic to `(𝔪^k M / 𝔪^{k+1} M) ⊗_A N`, hence also to
`(𝔪^k M / 𝔪^{k+1} M) ⊗_{A/𝔪} (N/𝔪 N)` `(0 ≤ k ≤ r − 1)`. The length of the latter, regarded as a `B`-module, is
therefore the product of `long_B(N/𝔪 N)` by the rank of the `(A/𝔪)`-vector space `𝔪^k M / 𝔪^{k+1} M`, which equals the
length of the `A`-module `𝔪^k M / 𝔪^{k+1} M`. Summing over `0 ≤ k ≤ r − 1`, one deduces at once the formula `(2.5.5.3)`.

**Remark (2.5.5.4).**

<!-- label: IV.2.5.5.4 -->

*Note that when `N` is an `A`-module of finite type, to say that `N` is a faithfully flat `A`-module amounts to saying
that `N ≠ 0` and that `N` is a flat `A`-module; indeed, Nakayama's lemma then shows that `𝔪 N ≠ N`.*

**Lemma (2.5.6).**

<!-- label: IV.2.5.6 -->

*Let `B` be a (not necessarily commutative) ring, `V`, `W` two isomorphic left `B`-modules, `C = End_B(V)`, and let
`M = Hom_B(V, W)`, equipped with its canonical structure of right `C`-module. Then `M` is a `C`-module isomorphic to
`C_d`; furthermore, for every `u ∈ M`, the following conditions are equivalent:*

*a) `{u}` is a basis of the `C`-module `M`.*

*b) `u` is an isomorphism of `V` onto `W`.*

If `u` is an isomorphism of `V` onto `W`, the map `v ↦ u ∘ v` from `C` to `M` is obviously a bijection, so b) implies
a). Conversely, suppose that `{u}` is a basis of the `C`-module `M`. By hypothesis there exists an isomorphism `u'` of
`V` onto `W`, and `{u'}` is then a basis of `M`; hence there is an invertible element `w` of `C` (i.e. an automorphism
of `V`) such that `u = u' ∘ w`, which implies that `u` is an isomorphism of `V` onto `W`.

**Corollary (2.5.7).**

<!-- label: IV.2.5.7 -->

*The hypotheses on `B`, `V`, `W` being those of `(2.5.6)`, suppose furthermore that one of the following conditions
holds:*

*(i) `V` and `W` are Noetherian `B`-modules;*

*(ii) `V` and `W` are modules of finite presentation over a commutative subring of `B`.*

*Then the conditions a) and b) of `(2.5.6)` are also equivalent to the following:*

*a') `u` is a generator of the `C`-module `M`.*

*b') `u` is an epimorphism of `V` onto `W`.*

One knows that an epimorphism of an `A`-module `E` onto itself is bijective in the following two cases: 1° `E` is a
Noetherian `A`-module (Bourbaki, *Alg.*, chap. VIII, §2, n° 2, lemma 3); 2° `A` is commutative and `E` is an `A`-module
of finite presentation `(8.9.3)` (¹); hence b) and b') are equivalent. On the other hand, if `u` generates `M`

______________________________________________________________________

(¹) The reader may verify that `(2.5.7)` and `(2.5.8)` are not used before §9.

<!-- original page 25 -->

and `{u'}` is a basis of `M`, there exists `v ∈ C` such that `u' = u ∘ v`, which proves that `u` is surjective;
therefore a') implies b'), and as a) evidently implies a'), this finishes the proof of the corollary.

**Proposition (2.5.8).**

<!-- label: IV.2.5.8 -->

*Let `A` be a commutative semi-local ring, `B` an `A`-algebra (not necessarily commutative), `V` and `W` two
`B`-modules. Let `A'` be a commutative `A`-algebra which is a faithfully flat `A`-module; put `B' = B ⊗_A A'`,
`V' = V ⊗_A A'`, `W' = W ⊗_A A'`, so that `B'` is an `A'`-algebra and `V'`, `W'` are `B'`-modules. Suppose furthermore
that one of the following conditions holds:*

*(i) `A` and `A'` are Noetherian, `V` and `W` are `A`-modules of finite type.*

*(ii) `B` is an `A`-module of finite type, `V` is a projective `B`-module of finite type and an `A`-module of finite
presentation.*

*Then, if `V'` and `W'` are isomorphic as `B'`-modules, `V` and `W` are isomorphic as `B`-modules.*

We note that in case (ii), `W'`, being `A'`-isomorphic to `V'`, is an `A'`-module of finite type, from which it follows
that `W` is an `A`-module of finite type (Bourbaki, *Alg. comm.*, chap. I, §3, n° 6, prop. 11); hence in all cases `V`
and `W` are `A`-modules of finite type. Furthermore:

*(2.5.8.1) Under either of the hypotheses (i), (ii), `Hom_B(V, W)` is an `A`-module of finite type.*

This is evident in case (i), for `Hom_A(V, W)` is then an `A`-module of finite type, and `Hom_B(V, W)` is an
`A`-sub-module of `Hom_A(V, W)`. In case (ii), `V` is a direct factor of a free `B`-module `B^n`, so `Hom_B(V, W)` is a
direct factor of `Hom_B(B^n, W) = W^n`, and since `W` is an `A`-module of finite type, so is `Hom_B(V, W)`.

Put

```text
                  C = End_B(V),     M = Hom_B(V, W),
```

which are `A`-modules of finite type in cases (i) and (ii). One knows that under either of the conditions (i), (ii), the
canonical homomorphism

```text
(2.5.8.2)         Hom_A(V, W) ⊗_A A' → Hom_{A'}(V', W')
```

is bijective (Bourbaki, *Alg. comm.*, chap. II, §2, n° 10, prop. 11). Since `A'` is a flat `A`-module,
`Hom_B(V, W) ⊗_A A'` is canonically identified with a sub-`A'`-module of `Hom_A(V, W) ⊗_A A'`. The image of this
sub-module under the homomorphism `(2.5.8.2)` is contained in `Hom_{B'}(V', W')`, for if `u ∈ Hom_B(V, W)` and
`a' ∈ A'`, the image of `u ⊗ a'` under `(2.5.8.2)` is the homomorphism `u' : V' → W'` such that `u'(x ⊗ 1) = u(x) ⊗ a'`;
for every `b ∈ B`, one has `u'((b ⊗ 1)(x ⊗ 1)) = u'(bx ⊗ 1) = u(bx) ⊗ a' = b u(x) ⊗ a' = (b ⊗ 1)(u(x) ⊗ a')`, whence our
assertion. This being so:

*(2.5.8.3) Under either of the hypotheses (i), (ii), the homomorphism*

```text
(2.5.8.4)         Hom_B(V, W) ⊗_A A' → Hom_{B'}(V', W')
```

*is bijective.*

For every `b ∈ B`, write `h(b)` (resp. `h'(b)`) for the homothety `x ↦ bx` of `V` (resp. `W`), which is an
`A`-endomorphism. Let `(b_α)_{α ∈ I}` be a system of generators of the `A`-algebra `B`; the map

```text
                  u ↦ (h'(b_α) ∘ u − u ∘ h(b_α))_α
```

from `Hom_A(V, W)` to `(Hom_A(V, W))^I` is `A`-linear, and by definition its kernel is precisely `Hom_B(V, W)`; in other
words, one has an exact sequence

```text
                  0 → Hom_B(V, W) → Hom_A(V, W) → (Hom_A(V, W))^I.
```

The same reasoning applies upon replacing `A`, `B`, `V`, `W` by `A'`, `B'`, `V'`, `W'`; moreover, one has a diagram

```text
                  0 ──→ Hom_B(V, W) ⊗_A A' ──→ Hom_A(V, W) ⊗_A A' ──→ (Hom_A(V, W))^I ⊗_A A'

(2.5.8.5)                       │ r                       │ s                          │ t
                                ↓                         ↓                            ↓

                  0 ──→ Hom_{B'}(V', W') ───→ Hom_{A'}(V', W') ───→ (Hom_{A'}(V', W'))^I
```

where `r` is the homomorphism `(2.5.8.4)`, `s` is the homomorphism `(2.5.8.2)`, and `t` is the composite homomorphism

```text
                  (Hom_A(V, W))^I ⊗_A A' →w (Hom_A(V, W) ⊗_A A')^I →s^I (Hom_{A'}(V', W'))^I,
```

`w` being the canonical homomorphism (Bourbaki, *Alg.*, chap. II, 3rd ed., §3, n° 7). One verifies at once that the
diagram `(2.5.8.5)` is commutative, and since `A'` is a flat `A`-module its rows are exact. Finally, we have seen

<!-- original page 26 -->

that `s` is an isomorphism, hence so is `s^I`; in case (ii), one may take `I` finite, and one then knows that `w` is
bijective (Bourbaki, *loc. cit.*, prop. 7); in case (i), one notes that if `B'` (resp. `B''`) is the image of `B` under
`h` (resp. `h'`) in `End_A(V)` (resp. `End_A(W)`), then `B'` and `B''` are `A`-modules of finite type, so one may again
take `I` finite. Thus in all cases `t` is bijective, and one concludes that `r` is bijective too.

It therefore follows from `(2.5.8.4)` that, if one puts

```text
                  C' = C ⊗_A A',    M' = M ⊗_A A',
```

one has canonical bijections

```text
(2.5.8.6)         C' ≅ End_{B'}(V'),    M' ≅ Hom_{B'}(V', W'),
```

the first of which is an isomorphism of `A'`-algebras, the second forming with the first a di-isomorphism of right
`C'`-modules.

*(2.5.8.7) Reduction to the case `V = B_d`.* The hypothesis that `V'` and `W'` are isomorphic `B'`-modules implies that
`C'_d` and `M'` are isomorphic right `C'`-modules `(2.5.6)`. We show that to prove `(2.5.8)`, it suffices to find an
element `u ∈ M` which is a generator of `M` as a right `C`-module. Indeed, `u' = u ⊗ 1` will be a generator of `M'` as a
right `C'`-module; now in case (i), `V'` and `W'` are `A'`-modules of finite type, hence Noetherian since `A'` is
Noetherian; in case (ii), `V'` and `W'` are (isomorphic) `A'`-modules of finite presentation. One may therefore apply
`(2.5.7)` to `A'`, `B'`, `V'`, `W'` and conclude that `u'` is a `B'`-isomorphism of `V'` onto `W'`. But since `A'` is
faithfully flat over `A`, this implies that `u` is bijective `(0_I, 6.4.1)`, which is the conclusion of `(2.5.8)`.
Noting that in case (i), `C` and `M` are `A`-modules of finite type, and that in case (ii), `C` is (as seen in
`(2.5.8.1)`) a direct factor of `V^n`, hence a projective `A`-module of finite type, one sees that one is reduced
(changing notation) to proving `(2.5.8)` in the particular case where `V = B_d`, and that it suffices to prove the
existence of a generator of the `B`-module `W`. Note that in this case `B` is an `A`-module of finite type.

*(2.5.8.8) Reduction to the case where `A` and `A'` are fields, `B` a simple `A`-algebra with centre `A`.* Let `𝔯` be
the radical of the semi-local ring `A`; it suffices to prove that `W/𝔯 W` is a monogenic `(B/𝔯 B)`-module, for if there
exists a surjective homomorphism `B_d/𝔯 B_d → W/𝔯 W`, it gives by composition a homomorphism `B_d → B_d/𝔯 B_d → W/𝔯 W`,
which itself (since `B_d` is a free `B`-module) can be written `B_d → W → W/𝔯 W`, so that the surjective homomorphism
considered is `f ⊗ 1 : B_d ⊗_A (A/𝔯) → W ⊗_A (A/𝔯)`. Since `W` is an `A`-module of finite type, Nakayama's lemma shows
that `f` is surjective (Bourbaki, *Alg. comm.*, chap. II, §3, n° 2, cor. 1 of prop. 4). If one puts `A_1 = A/𝔯`,
`A'_1 = A' ⊗_A A_1 = A'/𝔯 A'`, `B_1 = B/𝔯 B = B ⊗_A A_1`, `W_1 = W/𝔯 W = W ⊗_A A_1`, the hypotheses (i) (resp. (ii))
remain satisfied when one replaces in them `A`, `A'`, `B`, `V = B_d`, `W` by `A_1`, `A'_1`, `B_1`, `V_1 = (B_1)_d`,
`W_1` respectively; furthermore, `V'_1 = V' ⊗_A A_1 = V_1 ⊗_{A_1} A'_1` and `W'_1 = W' ⊗_A A_1 = W_1 ⊗_{A_1} A'_1` are
`B'_1`-isomorphic (with `B'_1 = B' ⊗_A A_1 = B_1 ⊗_{A_1} A'_1`), and `A'_1` is a faithfully flat `A_1`-module. One may
therefore suppose, for the proof of `(2.5.8)`, that `A` is a finite product of (commutative) fields. Since `B` is an
`A`-module of finite type, it is an Artinian ring; let `𝔑` be its radical. It will now suffice to prove that `W/𝔑 W` is
a monogenic `(B/𝔑)`-module, for one sees as above, using Nakayama's lemma, that this implies `W` is a monogenic
`B`-module; on the other hand, `W'/𝔑 W'` is `(B'/𝔑 B')`-isomorphic to `(B'/𝔑 B')_d`, and one has
`B'/𝔑 B' = (B ⊗_A A')/(𝔑 ⊗_A A') = (B/𝔑) ⊗_A A'`, and likewise `W'/𝔑 W' = (W ⊗_A A')/(𝔑 W ⊗_A A') = (W/𝔑 W) ⊗_A A'`. We
may therefore further suppose `𝔑 = 0`, i.e. that `B` is a semi-simple `A`-algebra.

Note now that since `A` is a finite product of fields `k_i` (`1 ≤ i ≤ n`), `A'` is a direct composite of `k_i`-algebras
`A'_i` (`1 ≤ i ≤ n`), each `A'_i` being annihilated by the `k_j` with `j ≠ i`; the hypothesis that `A'` is a faithfully
flat `A`-module implies that the `A'_i` are non-zero. Consequently, there exists a quotient `A''_i` of `A'_i` which is a
field, and `A''`, the direct composite of the `A''_i`, is a faithfully flat `A`-module and a quotient of `A'`.
Considering then the ring `B'' = B ⊗_A A'' = B' ⊗_{A'} A''`, `W'' = W ⊗_A A'' = W' ⊗_{A'} A''` is a `B''`-module
isomorphic to `B''_d`; one may therefore restrict to proving `(2.5.8)` after replacing `A'` by `A''`, i.e. one may also
suppose that `A'` is a finite product of fields.

Let `Z` be the centre of `B`, which is a finite product of fields and an `A`-module of finite type; note that `B` and
`W` are `Z`-modules of finite type, projective like every `Z`-module; furthermore, one has `B' = B ⊗_Z Z'` and
`W' = W ⊗_Z Z'`, where `Z' = Z ⊗_A A'`, and `Z'` is a faithfully flat `Z`-module. One may therefore replace `A` by `Z`
in the hypothesis, in other words suppose that `A` is the centre of `B`, with `B` semi-simple and `A'` a finite product
of fields. If `k_i` (`1 ≤ i ≤ n`) are the field components of `A`, then `B` is a direct composite of simple rings `B_i`,
`k_i` being the centre of `B_i`, and `W` is a direct sum of sub-modules `W_i` (`1 ≤ i ≤ n`), `W_i` being annihilated by
the `B_j` with `j ≠ i`; furthermore, the reasoning made above shows that one may suppose that `A'` is a product of
fields `k'_i` (`1 ≤ i ≤ n`), `k'_i` being an extension of `k_i` and annihilated by the `k_j` with `j ≠ i`. The
hypothesis that `B'_d` and `W'` are isomorphic `B'`-modules then implies that, for

<!-- original page 27 -->

every `i`, `(B_i ⊗_{k_i} k'_i)_d` and `W_i ⊗_{k_i} k'_i` are isomorphic `(B_i ⊗_{k_i} k'_i)`-modules; it therefore
suffices to prove `(2.5.8)` when `n = 1`, i.e. in the case where `A` and `A'` are fields and `B` is a simple algebra
with centre `A`.

*(2.5.8.9) End of the proof.* One knows (Bourbaki, *Alg.*, chap. VIII, §5, props. 6 and 8) that every `B`-module is a
direct sum of modules isomorphic to a minimal ideal of `B`, and two `B`-modules of finite rank over `A` are therefore
isomorphic if and only if they have the same rank over `A`. By hypothesis, one has `[W' : A'] = [B'_d : A']`. But
`[W' : A'] = [W : A]` and `[B'_d : A'] = [B_d : A]`; hence `[W : A] = [B_d : A]`, which finishes the proof.

### 2.6. Permanence of set-theoretic and topological properties of morphisms under faithfully flat descent

**Proposition (2.6.1).**

<!-- label: IV.2.6.1 -->

*Let `f : X → Y` be an `S`-morphism of `S`-preschemes, `g : S' → S` a surjective morphism, `X' = X_{(S')}`,
`Y' = Y_{(S')}`, `f' = f_{(S')} : X' → Y'`. Consider, for a morphism, the property of being:*

*(i) surjective;*

*(ii) injective;*

*(iii) with finite fibres (as sets);*

*(iv) bijective;*

*(v) radicial.*

*Then, if `P` denotes one of the preceding properties and `f'` possesses the property `P`, the same holds for `f`.*

Since the projection morphism `Y' → Y` is itself surjective `(I, 3.5.2)`, one may, by virtue of `(I, 3.3.11)`, restrict
to the case where `Y = S`, `Y' = S'`. For every `y ∈ Y` (resp. `y' ∈ Y'`) denote by `X_y` (resp. `X'_{y'}`) the fibre
prescheme `f⁻¹(y)` (resp. `f'⁻¹(y')`) `(I, 3.6.2)`; one knows that for `y' ∈ Y'` over `y = g(y')` one has a canonical
isomorphism `X'_{y'} ≅ X_y ⊗_{k(y)} k(y')` `(I, 3.6.4)`; since the morphism `Spec(k(y')) → Spec(k(y))` is surjective, so
is the projection `X'_{y'} → X_y` `(I, 3.5.2)`. Hence if `X'_{y'}` is non-empty (resp. has at most one point, resp. is a
finite set), so is `X_y`; since `g : Y' → Y` is surjective, this proves the proposition in cases (i), (ii) and (iii),
and (iv) follows from (i) and (ii). Finally, to prove (v), it suffices to show that if `f'` is universally injective
`(I, 3.5.11)`, then so is `f`; now let `Y_1 → Y` be an arbitrary morphism; put `X_1 = X ×_Y Y_1` and `f_1 = f_{(Y_1)}`.
On the other hand, put `Y'_1 = Y_1 ×_Y Y'`, `X'_1 = X' ×_{Y'} Y'_1 = X_1 ×_{Y_1} Y'_1`,
`f'_1 = f_{(Y'_1)} = (f_1)_{(Y'_1)} : X'_1 → Y'_1`; since `g_1 = g_{(Y_1)} : Y'_1 → Y_1` is surjective `(I, 3.5.2)` and
`f'` is universally injective, `f'_1` is injective, and it follows from (ii) that `f_1` is injective, whence our
assertion.

**Proposition (2.6.2).**

<!-- label: IV.2.6.2 -->

*The notations being those of `(2.6.1)`, suppose the morphism `g : S' → S` faithfully flat and quasi-compact. Consider,
for a morphism, the property of being:*

*(i) open;*

*(ii) closed;*

*(iii) quasi-compact and a homeomorphism onto the image subspace;*

*(iv) a homeomorphism.*

*Then, if `P` denotes one of the preceding properties and `f'` possesses the property `P`, the same holds for `f`.*

<!-- original page 28 -->

Since the morphism `Y' → Y` is faithfully flat and quasi-compact `(2.2.13` and `1.1.2)`, one may, by virtue of
`(I, 3.3.11)`, restrict to the case where `Y = S`, `Y' = S'`. If `g'` is the projection `X' → X`, one knows that for
every subset `M` of `X`, one has `g⁻¹(f(M)) = f'(g'⁻¹(M))` `(I, 3.4.8)`. If `f'` is an open (resp. closed) morphism,
then, for every open (resp. closed) subset `M` of `X`, `f'(g'⁻¹(M))` is open (resp. closed) in `Y'`, and since `g` is
faithfully flat and quasi-compact, one concludes that `f(M)` is open (resp. closed) in `Y` by virtue of `(2.3.12)`. This
proves the proposition in cases (i) and (ii). Let us prove it in case (iii) (which will imply case (iv), taking
`(2.6.1, (iv))` into account). By virtue of `(2.6.1, (ii))`, `f` is injective, and it remains to prove that `f`, viewed
as a map of `X` onto `f(X)`, is a quasi-compact and open map. Since `f'` is quasi-compact, so is `f` `(1.1.4)`. It
therefore suffices to prove that for every closed subset `Z` of `X`, one has `Z = f⁻¹(f(Z))`; since `g'` is surjective,
this relation is equivalent to `g'⁻¹(Z) = g'⁻¹(f⁻¹(f(Z)))`, or again to `g'⁻¹(Z) = f'⁻¹(g⁻¹(f(Z)))`. Now, since `f` is
quasi-compact, so is its composite with the canonical injection `Z → X` (`Z` here being the reduced closed sub-prescheme
of `X` having `Z` as underlying space). Applying `(2.3.10)` to the subset `f(Z)` of `Y` (the image of the morphism
`f|Z`), one obtains `g⁻¹(f(Z)) = f'(g'⁻¹(Z))`; the formula to be proved therefore amounts to `Z' = f'⁻¹(f'(Z'))`, where
`Z' = g'⁻¹(Z)`; but this formula follows from the hypothesis that `f'` is a homeomorphism of `X'` onto `f'(X')`.

**Remark (2.6.3).**

<!-- label: IV.2.6.3 -->

*In cases (i) and (ii), the conclusions of `(2.6.2)` remain valid when one supposes only `g` quasi-faithfully flat
`(2.3.3)` and quasi-compact; indeed, by virtue of `(2.1.4)`, `(I, 3.5.2)` and `(I, 9.1.13.1)`, one may again reduce to
the case where `Y = S`, `Y' = S'`; the conclusion then follows from `(2.3.12)`. In cases (iii) and (iv), the conclusions
remain valid when one supposes only `g` quasi-faithfully flat, provided one supposes additionally that `f'` is
quasi-compact; indeed, one then uses only `(2.3.10)` and the fact that `g` is surjective. Finally, if `g` is faithfully
flat and locally of finite presentation, or if `g` is surjective and `S` discrete, the conclusion of `(2.6.2)` is valid
when `P` is the property:*

*(iii bis) being a homeomorphism onto the image subspace;*

*this results indeed from the proof given in `(2.6.2)` and from Remark `(2.4.11)`.*

**Corollary (2.6.4).**

<!-- label: IV.2.6.4 -->

*The notations being those of `(2.6.1)`, suppose the morphism `g : S' → S` faithfully flat and quasi-compact. Consider
for a morphism the property of being:*

*(i) universally open;*

*(ii) universally closed;*

*(iii) quasi-compact and universally bicontinuous;*

*(iv) a universal homeomorphism;*

*(v) quasi-compact;*

*(vi) quasi-compact and dominant.*

*Then, if `P` denotes one of the preceding properties, for `f` to possess the property `P`, it is necessary and
sufficient that `f'` possess it.*

<!-- original page 29 -->

Properties (v) and (vi) are mentioned only for the record, being consequences of `(1.1.4)`, `(1.1.6)` and `(2.3.7)`. As
for the others, the condition is necessary by virtue of `(2.4.3)`. Conversely, suppose for instance that `f'` is
universally open, and let `Y_1 → Y` be an arbitrary morphism; put `X_1 = X ×_Y Y_1` and `f_1 = f_{(Y_1)}`. On the other
hand, put `Y'_1 = Y_1 ×_Y Y'`, `X'_1 = X' ×_{Y'} Y'_1 = X_1 ×_{Y_1} Y'_1`,
`f'_1 = f'_{(Y'_1)} = (f_1)_{(Y'_1)} : X'_1 → Y'_1`; since `g_1 = g_{(Y'_1)} : Y'_1 → Y_1` is faithfully flat and
quasi-compact `(2.2.13` and `1.1.2)` and `f'` is universally open, `f'_1` is open, and it follows from `(2.6.2)` that
`f_1` is open; hence `f` is universally open. The same reasoning applies in the other cases.

One notes again here that one may replace "faithfully flat" by "quasi-faithfully flat", and, when `g` is additionally
locally of finite presentation, or when `g` is surjective and `S` discrete, one may replace property (iii) by:

*(iii bis) universally bicontinuous.*

### 2.7. Permanence of various properties of morphisms under faithfully flat descent

**Proposition (2.7.1).**

<!-- label: IV.2.7.1 -->

*Let `f : X → Y` be an `S`-morphism of `S`-preschemes, `g : S' → S` a faithfully flat and quasi-compact morphism,
`X' = X_{(S')}`, `Y' = Y_{(S')}`, `f' = f_{(S')} : X' → Y'`. Consider, for a morphism, the property of being:*

*(i) separated;*

*(ii) quasi-separated;*

*(iii) locally of finite type;*

*(iv) locally of finite presentation;*

*(v) of finite type;*

*(vi) of finite presentation;*

*(vii) proper;*

*(viii) an isomorphism;*

*(ix) a monomorphism;*

*(x) an open immersion;*

*(xi) a quasi-compact immersion;*

*(xii) a closed immersion;*

*(xiii) affine;*

*(xiv) quasi-affine;*

*(xv) finite;*

*(xvi) quasi-finite;*

*(xvii) integral.*

*Then, if `P` denotes one of the preceding properties, for `f` to possess the property `P`, it is necessary and
sufficient that `f'` possess it.*

It has been proved in chapters I, II, and in chapter IV §1, that if `f` possesses one of the above properties `P`, the
same holds for `f'` (without any hypothesis on the morphism `g : S' → S`). It therefore remains to prove the converse;
since the projection `Y' → Y` is

<!-- original page 30 -->

a faithfully flat and quasi-compact morphism `(2.2.13` and `1.1.2)`, one may restrict to the case where `S = Y`,
`S' = Y'` by virtue of `(I, 3.3.11)`.

(i) To say that `f` is separated means that the diagonal morphism `Δ_f : X → X ×_Y X` is closed; since
`Δ_{f'} = (Δ_f)_{(Y')}` `(I, 5.3.4)`, if `Δ_{f'}` is closed, so is `Δ_f` by virtue of `(2.6.2)`, hence `f` is separated.

(ii) has already been proved under weaker hypotheses `(1.2.5)`.

(iii) and (iv): The question is evidently local on `X` and `Y`, and, taking `(2.2.12)` into account, it therefore
suffices to prove the

**Lemma (2.7.1.1).**

<!-- label: IV.2.7.1.1 -->

*Let `A` be a ring, `B` an `A`-algebra, `A'` an `A`-algebra which is a faithfully flat `A`-module, `B' = B ⊗_A A'`. For
`B` to be an `A`-algebra of finite type (resp. of finite presentation), it is necessary and sufficient that `B'` be an
`A'`-algebra of finite type (resp. of finite presentation).*

One knows already that the condition is necessary without any hypothesis on `A` `(1.3.4, 1.3.6, 1.4.3, 1.4.6)`. Suppose
that `B'` is an `A'`-algebra of finite type; let `(B_α)_{α ∈ I}` be the filtered increasing family of `A`-sub-algebras
of `B`, so that `B = lim B_α`, and therefore also `B' = lim (B_α ⊗_A A')`, since the tensor product commutes with
inductive limits; if `(x'_i)` is a finite system of generators of the `A'`-algebra `B'`, there exists an index `α` such
that all the `x'_i` belong to the sub-algebra `B_α ⊗_A A'` of `B'`, whence `B' = B_α ⊗_A A'`, and since `A'` is
faithfully flat, `B = B_α` `(0_I, 6.4.1)`.

Suppose now that `B'` is an `A'`-algebra of finite presentation; one knows already from what precedes that `B` is an
`A`-algebra of finite type, so there exists a polynomial `A`-algebra `C = A[T_1, …, T_n]` and a surjective
`A`-homomorphism of algebras `C → B`; let `𝔧` be the kernel of this homomorphism, so that one has an exact sequence
`0 → 𝔧 → C → B → 0`, and therefore also an exact sequence `0 → 𝔧' → C' → B' → 0` (since `A'` is `A`-flat), upon putting
`C' = C ⊗_A A' = A'[T_1, …, T_n]` and `𝔧' = 𝔧 ⊗_A A'` (identified with an ideal of `C'`). Since `B'` is an `A'`-algebra
of finite presentation, `𝔧'` is a `C'`-module of finite type `(1.4.4)`; but one has `𝔧' = 𝔧 ⊗_C C'`, and `C'` is a
faithfully flat `C`-module `(2.2.13` and `2.2.3)`; one knows then that the hypothesis that `𝔧'` is a `C'`-module of
finite type implies that `𝔧` is a `C`-module of finite type (Bourbaki, *Alg. comm.*, chap. I, §3, n° 6, prop. 11); hence
`B` is an `A`-algebra of finite presentation.

(v) follows from (iii) and from `(2.6.2, (v))` by virtue of `(1.5.2)`.

(vi) follows similarly from (iv), (v) and (ii) by virtue of `(1.6.1)`.

(vii) follows from (i), (v) and `(2.6.4, (ii))` `(II, 5.4.1)`.

(viii) Note first that since `f'` is an isomorphism, it is a universal homeomorphism, so the same is true of `f`
`(2.6.4)`; one already concludes that `f` is quasi-compact and separated `(2.4.4)`. Write `f = (ψ, θ)`, where `ψ` is
therefore a homeomorphism; it must be proved that `θ : 𝒪_Y → f_*(𝒪_X)` is an isomorphism of `𝒪_Y`-Modules. Now, if one
writes `f' = (ψ', θ')`, the homomorphism `θ' : 𝒪_{Y'} → f'_*(𝒪_{X'})` is composed of the canonical homomorphism
`g*(f_*(𝒪_X)) → f'_*(𝒪_{X'})` and of `g*(θ)` `(2.3.2)`; but the first of these two homomorphisms is bijective by virtue
of the hypothesis on `g` `(2.3.1)`, so if `θ'` is bijective,

<!-- original page 31 -->

so is `g*(θ)`, and since `g` is faithfully flat, `θ` is bijective `(2.2.7)`, which proves (viii).

(ix) The proposition follows from (viii), from `(I, 5.3.4)`, and from `(I, 5.3.8)`, which reduces monomorphisms to
isomorphisms.

(x) If `f'` is an open immersion, `f'(X')` is open in `Y'`, and one has `f'(X') = g⁻¹(f(X))` `(I, 3.4.8)`; it follows
from `(2.3.12)` that `f(X)` is open. One may then replace `Y` (resp. `Y'`) by the sub-prescheme induced on the open set
`f(X)` (resp. `f'(X')`), taking `(1.1.2)` and `(2.2.13)` into account; then `f'` becomes an isomorphism, hence the same
is true of `f` by (viii), and this establishes (x).

(xi) If `f'` is a quasi-compact immersion, `f'` is a quasi-compact and quasi-separated morphism `(1.2.2)`, so the same
holds for `f` by (ii) and `(2.6.2, (v))`. Let `Z` be the sub-prescheme of `Y` closed image of `X` under `f` `(1.7.8)`,
and put `f = j ∘ g`, where `j : Z → Y` is the canonical injection; one then has `f' = j' ∘ g'` with `j' = j_{(Y')}`,
`g' = g_{(Y')}`, and one knows that `j'` identifies with the canonical injection `Z' → Y'` of the sub-prescheme `Z'` of
`Y'`, the closed image of `X'` under `f'` `(2.3.2)`. The hypothesis on `f'` then means that `g'` is an open immersion
`(I, 9.5.10)`, hence the same holds for `g` by (x), and this shows that `f` is an immersion.

(xii) To say that `f'` (resp. `f`) is a closed immersion means that `f'` (resp. `f`) is a quasi-compact immersion and a
closed morphism; one therefore sees that (xii) follows from (xi) and from `(2.6.2, (ii))`.

(xiii) and (xiv) Suppose `f'` affine (resp. quasi-affine); note then that `f'` is quasi-compact and quasi-separated
`(II, 5.1.1)`, so the same holds for `f` by (ii) and `(2.6.2, (v))`. Put `𝒜 = f_*(𝒪_X)`, `𝒜' = f'_*(𝒪_{X'})`; by virtue
of `(2.3.1)`, the canonical homomorphism of `𝒪_{Y'}`-Algebras `g*(𝒜) → 𝒜'` is bijective; consequently, if
`h : Z = Spec(𝒜) → Y` is the structure morphism, the structure morphism `h' : Z' = Spec(𝒜') → Y'` identifies with
`h_{(Y')}` `(II, 1.5.2)`. Let then `u : X → Z` (resp. `u' : X' → Z'`) be the canonical `Y`-morphism (resp.
`Y'`-morphism) corresponding to the identity homomorphism of `𝒜` (resp. `𝒜'`) `(II, 1.2.7)`; since one has the
commutative diagram

```text
                       X  ←—— X'
                       │       │
                       u│      │u'
                       ↓       ↓
                       Z  ←—— Z'
                       │       │
                       h│      │h'
                       ↓       ↓
                       Y  ←—— Y'
                          g
```

and `h' ∘ u' = f'`, it follows from `(II, 1.2.7)` that `u' = u_{(Y')}`. Moreover, `g'` is faithfully flat and
quasi-compact `(1.1.2` and `2.2.13)`. This being so, the hypothesis on `f'` means that `u'` is an isomorphism (resp. an
open immersion) `(II, 5.1.6)`; it then follows from (viii) (resp. (x)) that `u` is an isomorphism (resp. an open
immersion), whence (xiii) (resp. (xiv)).

<!-- original page 32 -->

(xv) If `f'` is finite, it is affine, hence so is `f` by (xiii); furthermore, with the notations of the proof of (xiii),
`𝒜'` is an `𝒪_{Y'}`-Module of finite type, and `𝒜'` is isomorphic to `g*(𝒜)`; it follows from `(2.5.2)` that `𝒜` is an
`𝒪_Y`-Module of finite type, hence `f` is a finite morphism.

(xvi) To say that `f` is quasi-finite means that `f` is a morphism of finite type and that for every `y ∈ Y`, `f⁻¹(y)`
is finite `(II, 6.2.2` and `I, 6.4.4)`; the conclusion therefore follows from (v) and (xv).

(xvii) One sees as in (xv) that `f` is affine. One may restrict to the case where `Y = Spec(A)`, `Y' = Spec(A')`, and
then `X = Spec(B)`, `X' = Spec(B')`, where `B' = B ⊗_A A'`; `B` is equal to the inductive limit of its `A`-sub-algebras
of finite type `B_α`, so one has `B' = lim B'_α`, where `B'_α = B_α ⊗_A A'`, and `B'_α` is an `A'`-algebra of finite
type. But by hypothesis `B'` is integral over `A'`, so `B'_α` is an `A'`-module of finite type, and `B_α` is therefore
an `A`-module of finite type `(2.5.2)`. Q.E.D.

**Corollary (2.7.2).**

<!-- label: IV.2.7.2 -->

*The hypotheses and notations being those of `(2.7.1)`, suppose `f` quasi-compact; let `ℒ` be an invertible
`𝒪_X`-Module, `ℒ' = ℒ ⊗_{𝒪_X} 𝒪_{X'}` its inverse image. For `ℒ` to be ample (resp. very ample) for `f`, it is necessary
and sufficient that `ℒ'` be ample (resp. very ample) for `f'`.*

The condition is necessary without any hypothesis on `g : S' → S` `(II, 4.4.10` and `4.6.13)`; to see that it is
sufficient, one may, as in `(2.7.1)`, restrict to the case where `S = Y`, `S' = Y'`. The hypothesis on `ℒ'` implies that
`f'` is quasi-compact and separated `(II, 4.6.1)`, hence the same holds for `f` (by `(2.6.2, (v))` and `(2.7.1, (i))`).
Put `ℰ = f_*(ℒ)`, `ℰ' = f'_*(ℒ')`; it follows from `(2.3.1)` that the canonical homomorphism `u : g*(ℰ) → ℰ'` is
bijective. If `ℒ'` is very ample for `f'`, the canonical homomorphism `σ' : f'*(ℰ') → ℒ'` is surjective, and the
morphism `r' = r_{ℰ', ℒ'} : X' → P(ℰ')` is an immersion `(II, 4.4.4, b))`, necessarily quasi-compact `(1.1.2, (v))`. The
fact that `u : g*(ℰ) → ℰ'` is bijective implies that, if `h : P(ℰ) → Y`, `h' : P(ℰ') → Y'` are the structure morphisms,
then `h'` identifies with `h_{(Y')}` `(II, 4.1.3)`. On the other hand, denoting by `g'` the projection `X' → X`, `g'` is
faithfully flat `(2.2.13)`, one has `f ∘ g' = g ∘ f'`, and one verifies easily that the homomorphism
`g'*(f*(ℰ)) ≅ f'*(g*(ℰ)) → f'*(ℰ')` is identical with the composite homomorphism

```text
                  g'*(f*(f_*(ℒ))) → g'*(ℒ) → ℒ'
```

(for example by reducing to the case where `Y` and `Y'` are affine). Since `σ'` is surjective and `f'*(u)` is bijective,
one sees that `g'*(σ)` is surjective, hence the same is true of `σ` `(2.2.7)`. One concludes that the morphism
`r = r_{ℰ, ℒ} : X → P(ℰ)` is everywhere defined `(II, 3.7.4)`; furthermore, if one puts `P = P(ℰ)`, `P' = P(ℰ')` and if
`g''` is the projection `P' → P`, then `r'` identifies with `r_{(Y')}` `(II, 4.2.10)` and `g''` is faithfully flat and
quasi-compact `(1.1.2` and `2.2.13)`. One therefore concludes from `(2.7.1, (xi))` that `r` is an immersion, and
consequently `ℒ` is very ample `(II, 4.4.4, b))`.

Suppose now that `ℒ'` is ample for `f'`; to prove that `ℒ` is ample for `f`, one may restrict to the case where `Y` is
affine `(II, 4.6.4)`, and by virtue of `(2.2.12)` and `(II, 4.6.13)`, one may also suppose that `Y'` is affine. Then `X`
and `X'` are

<!-- original page 33 -->

quasi-compact schemes, and to prove that `ℒ` is `f`-ample, one may apply the criterion of `(II, 4.6.8, a))`. Let then
`ℱ` be a quasi-coherent `𝒪_X`-Module of finite type; if `σ : f*(f_*(ℱ ⊗ ℒ^{⊗ n})) → ℱ ⊗ ℒ^{⊗ n}` is the canonical
homomorphism, one sees as above that `g'*(σ)` is the composite homomorphism

```text
                  f'*(g*(f_*(ℱ ⊗ ℒ^{⊗ n}))) →u f'*(f'_*(ℱ' ⊗ ℒ'^{⊗ n})) →σ' ℱ' ⊗ ℒ'^{⊗ n},
```

upon putting `ℱ' = g'*(ℱ)`, taking `(0_I, 4.3.3.1)` into account and denoting by `u` the canonical homomorphism
`g*(f_*(ℱ ⊗ ℒ^{⊗ n})) → f'_*(g'*(ℱ ⊗ ℒ^{⊗ n}))`. Now, one knows that `u` is bijective for every `n` `(2.3.1)`; on the
other hand, since `ℱ` is quasi-coherent and of finite type, the hypothesis that `ℒ'` is ample for `f'` implies the
existence of an `n_0` such that `σ'` is surjective for `n ≥ n_0`; one therefore sees that `g'*(σ)` is surjective for
`n ≥ n_0`, and since `g'` is faithfully flat, `σ` is surjective for these values of `n` `(2.2.7)`, which completes the
proof.

**Remarks (2.7.3).**

<!-- label: IV.2.7.3 -->

*(i) It follows from `(2.6.1)`, `(2.6.4)` and `(2.5.4.1)` that the conclusions of `(2.7.1)` are still valid in cases
(i), (iii), (v), (vii) and (xvi) when one supposes only that `g` is quasi-compact and quasi-faithfully flat `(2.3.3)`;
we have already remarked that `(2.7.1)` is valid in case (ii) under the sole hypothesis that `g` is surjective and
quasi-compact.*

*(ii) With the notations and hypotheses of `(2.7.1)`, it may happen that `f` is proper and `f'` projective without `f`
being quasi-projective. Indeed, Hironaka [34] has given an example of a proper, non-projective morphism `f : X → Y`,
where `X` and `Y` are two regular algebraic schemes `(0_I, 4.1.4)` over the same field `k`, with `Y` projective over
`k`; furthermore, `Y` is the union of two affine open sets `Y_i` (`i = 1, 2`) such that `f : X ×_Y Y_i → Y_i` is
projective for `i = 1, 2`. Let then `Y' = Y_1 ⨿ Y_2` be the sum prescheme; it is clear that the canonical morphism
`g : Y' → Y`, coinciding with the canonical injections on `Y_1` and `Y_2`, is faithfully flat, and is quasi-compact by
virtue of `(I, 5.5.10)`; yet, although `f' : X ×_Y Y' → Y'` (coinciding with `f_i` on each of the `Y_i`) is projective
`(II, 5.5.6)`, the same is not true of `f`. There therefore exists an invertible `𝒪_{X'}`-Module `ℒ'` which is
`f'`-ample but is not of the form `g'*(ℒ)` for an invertible `𝒪_X`-Module `ℒ`, by virtue of `(2.7.2)`.*

*(iii) Under the hypotheses of `(2.7.1)`, it may happen that `f'` is a local isomorphism without `f` being a local
immersion. Indeed, let `k` be a field, `k̄` an algebraic closure of `k`, `K` a separable extension of finite degree of
`k`, distinct from `k`; then the structure morphism `f : X → Y`, where `X = Spec(K)` and `Y = Spec(k)`, is not a local
immersion, but if one takes `Y' = Spec(k̄)`, the morphism `Y' → Y` is faithfully flat and quasi-compact, and
`f' = f_{(Y')}` is a local isomorphism, since `X' = X ×_Y Y'` is a sum of a finite number of schemes isomorphic to
`Y'`.*

### 2.8. Preschemes over a regular base of dimension 1; closure of a closed sub-prescheme of the generic fibre

**Proposition (2.8.1).**

<!-- label: IV.2.8.1 -->

*Let `Y` be a locally Noetherian, regular, irreducible prescheme of dimension 1, with generic point `η`, `f : X → Y` a
morphism, `X_η = f⁻¹(η)` the fibre at the*

<!-- original page 34 -->

*generic point, `i : X_η → X` the canonical morphism. Let `ℱ` be a quasi-coherent `𝒪_X`-Module, `ℱ_η = i*(ℱ)`, `𝒢_η` an
`𝒪_{X_η}`-Module quotient of `ℱ_η`, and let `𝒢` be the `𝒪_X`-Module image of `ℱ` under the composite homomorphism
\`(0_I, 4.4.3.2)*

```text
                  ℱ →ρ i_*(i*(ℱ)) = i_*(ℱ_η) → i_*(𝒢_η).
```

*Then `𝒢` is a quasi-coherent and `f`-flat `𝒪_X`-Module quotient of `ℱ`, such that `i*(𝒢) = 𝒢_η`, and it is the unique
`𝒪_X`-Module quotient of `ℱ` having these properties.*

Since `i` is quasi-compact and quasi-separated `(1.1.2` and `1.2.2)`, it follows from `(1.7.4)` that for every
quasi-coherent `𝒪_{X_η}`-Module `ℋ`, `i_*(ℋ)` is a quasi-coherent `𝒪_X`-Module; furthermore, for every open `U` of `X`,
one has `(i_*(ℋ))(U) = (i_*(ℋ|U ∩ X_η))(U ∩ X_η) = ℋ(U ∩ X_η)` by definition `(0_I, 3.4.1)`. If one proves the
proposition when `X` and `Y` are affine, it will follow by gluing in the general case, in view of the uniqueness
assertion valid in the affine case. In other words, one is reduced to proving the

**Lemma (2.8.1.1).**

<!-- label: IV.2.8.1.1 -->

*Let `A` be a regular Noetherian ring `(0, 17.3.6)`, integral and of dimension 1, `K` its field of fractions, `M` an
`A`-module, `N'_η` a `K`-module quotient of `M_{(K)} = M ⊗_A K` by a sub-`K`-module `P'`, `N` the image of `M` under the
composite homomorphism `M → M_{(K)} → N'_η`. Then `N` is a flat `A`-module, and it is the unique quotient module `N` of
`M` which is a flat `A`-module and such that the kernel of the surjective homomorphism `M_{(K)} → N_{(K)}` equals `P'`.*

Since for every maximal ideal `𝔪` of `A`, `A_𝔪` is a regular local ring of dimension 1, hence a discrete valuation ring,
it amounts to the same thing to say that an `A`-module `N` is flat or that it is torsion-free `(0_I, 6.3.4)`. Since
`N'_η` is a `K`-vector space, it is a torsion-free `A`-module, so the same is true of `N`, a sub-module of `N'_η`;
furthermore, it is immediate to verify that `N_{(K)}` identifies with `N'_η`. Conversely, if `N` is a quotient
`A`-module of `M` having the properties of the statement, the fact that `N` is a flat `A`-module implies that the
canonical homomorphism `N → N_{(K)} = N ⊗_A K` is injective. Since `N_{(K)}` identifies with `N'_η`, the conclusion
follows from the commutativity of the diagram

```text
                  M     ──→  N
                  │           │
                  ↓           ↓
                  M_{(K)} ──→ N_{(K)}.
```

**Corollary (2.8.2).**

<!-- label: IV.2.8.2 -->

*Under the conditions of `(2.8.1)`, for `ℱ` to be `f`-flat, it is necessary and sufficient that the canonical
homomorphism `ℱ → i_*(i*(ℱ)) = i_*(ℱ_η)` be injective.*

**(2.8.3)**

<!-- label: IV.2.8.3 -->

The formation of the `𝒪_X`-Module `𝒢` is functorial in `ℱ` and `𝒢_η`: more precisely, if `ℱ_1`, `ℱ_2` are two
quasi-coherent `𝒪_X`-Modules, `u : ℱ_1 → ℱ_2` an `𝒪_X`-homomorphism, `𝒢_{η,i}` an `𝒪_{X_η}`-Module quotient of `(ℱ_i)_η`
(`i = 1, 2`) and `v : 𝒢_{η,1} → 𝒢_{η,2}` a homomorphism making the diagram

```text
                  (ℱ_1)_η ──→ (ℱ_2)_η
                       │          │
                       ↓          ↓
                  𝒢_{η,1}  ──v──→ 𝒢_{η,2}
```

<!-- original page 35 -->

commutative (homomorphism uniquely determined (when it exists) by this property), then the diagram

```text
                  ℱ_1            ──→         ℱ_2
                       │                          │
                       ↓                          ↓
                  i_*(𝒢_{η,1})  ──i_*(v)──→  i_*(𝒢_{η,2})
```

is commutative, and consequently there is a unique homomorphism `w : 𝒢_1 → 𝒢_2` making the diagram

```text
                  ℱ_1   ──→  ℱ_2
                       │          │
                       ↓          ↓
                  𝒢_1  ──w──→ 𝒢_2
```

commutative.

**Proposition (2.8.4).**

<!-- label: IV.2.8.4 -->

*The hypotheses on `Y` being those of `(2.8.1)`, let `X_1`, `X_2` be two `Y`-preschemes, `ℱ_i` a quasi-coherent
`𝒪_{X_i}`-Module, `𝒢_{η,i}` an `𝒪_{(X_i)_η}`-Module quotient of `(ℱ_i)_η` (`i = 1, 2`). Then one has*

```text
(2.8.4.1)         (𝒢_{η,1} ⊠_{k(η)} 𝒢_{η,2})^∼ = 𝒢_1 ⊠_Y 𝒢_2.
```

Indeed, put `X = X_1 ×_Y X_2`; the left-hand side of `(2.8.4.1)` is a quasi-coherent `𝒪_X`-Module which is `Y`-flat
`(0_I, 6.2.1)`, whose inverse image in `X_η` is `𝒢_{η,1} ⊠ 𝒢_{η,2}` `(I, 9.1.5)`, and which is a quotient of
`ℱ_1 ⊠_Y ℱ_2`; the conclusion therefore follows from the uniqueness property of `(2.8.1)`.

**Proposition (2.8.5).**

<!-- label: IV.2.8.5 -->

*The hypotheses on `X` and `Y` being those of `(2.8.1)`, let `Z'` be a closed sub-prescheme of `X_η`. There then exists
a unique closed sub-prescheme `Z̄` of `X` which is `Y`-flat and such that `i⁻¹(Z̄) = Z'`.*

If `𝒥'` is the quasi-coherent Ideal of `𝒪_{X_η}` defining `Z'`, it suffices to apply `(2.8.1)` to the case where
`ℱ = 𝒪_X` and `𝒢_η = 𝒪_{X_η}/𝒥'`; if `𝒢 = 𝒪_X/𝒥̄`, one has indeed `𝒥' = i*(𝒥̄)`, so `i⁻¹(Z̄) = Z'` `(I, 4.4.5)`.

One notes that the prescheme `Z̄` is the closed image of `Z'` under the composite morphism `Z' → X_η → X`, where the
first arrow is the canonical injection `(I, 9.5.3)`; its underlying space is the closure in `X` of `Z'` `(I, 9.5.4)`,
which justifies the notation adopted. One also says that `Z̄` is the **closure sub-prescheme** of `Z'` in `X`.

**Corollary (2.8.6).**

<!-- label: IV.2.8.6 -->

*Let `X_1`, `X_2` be two `Y`-preschemes, `Z'_i` a closed sub-prescheme of `(X_i)_η` (`i = 1, 2`). Then one has*

```text
(2.8.6.1)         (Z'_1 ×_{k(η)} Z'_2)^− = Z̄_1 ×_Y Z̄_2.
```

This results from `(2.8.4)` and `(2.8.5)`.

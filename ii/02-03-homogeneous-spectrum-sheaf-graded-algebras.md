# §3. Homogeneous spectrum of a sheaf of graded algebras

## 3.1. Homogeneous spectrum of a quasi-coherent graded `𝒪_Y`-algebra

**(3.1.1)**

<!-- label: II.3.1.1 -->

Let `Y` be a prescheme, `𝒮` a graded `𝒪_Y`-algebra, and `ℳ` a graded `𝒮`-module. If `𝒮` is _quasi-coherent_, then each
of its homogeneous components `𝒮_n` is a quasi-coherent `𝒪_Y`-module, since they are the images of `𝒮` under a
homomorphism from `𝒮` to itself (`I, 1.3.8` and `1.3.9`); likewise, if `ℳ` is quasi-coherent as an `𝒪_Y`-module, then
its homogeneous components `ℳ_n` are also quasi-coherent, and conversely. For an integer `d > 0`, we denote by `𝒮^{(d)}`
the direct sum of the `𝒪_Y`-modules `𝒮_{nd}` (for `n ∈ ℤ`), which is quasi-coherent if `𝒮` is `(I, 1.3.9)`; for every
integer `k` with `0 ≤ k ≤ d − 1`, we denote by `ℳ^{(d, k)}` (or `ℳ^{(d)}` for `k = 0`) the direct sum of the `ℳ_{nd+k}`
(for `n ∈ ℤ`), which is a graded `𝒮^{(d)}`-module, quasi-coherent if `𝒮` and `ℳ` are quasi-coherent `(I, 9.6.1)`. We
denote by `ℳ(n)` the graded `𝒮`-module such that `(ℳ(n))_k = ℳ_{n+k}` for all `k ∈ ℤ`; if `𝒮` and `ℳ` are
quasi-coherent, then `ℳ(n)` is a quasi-coherent graded `𝒮`-module `(I, 9.6.1)`.

We say that `ℳ` is a graded `𝒮`-module _of finite type_ (resp. admits a _finite presentation_) if, for every `y ∈ Y`,
there exists an open neighbourhood `U` of `y` and integers `n_i` (resp. integers `m_i` and `n_j`) such that there is a
surjective degree-`0` homomorphism

```text
  ⊕_{i=1}^r (𝒮(n_i)|U) → ℳ|U
```

(resp. such that `ℳ|U` is isomorphic to the cokernel of a degree-`0` homomorphism

```text
  ⊕_{i=1}^r (𝒮(m_i)|U) → ⊕_{j=1}^s (𝒮(n_j)|U)).
```

<!-- original page 49 -->

Let `U` be an affine open of `Y`, with ring `A = Γ(U, 𝒪_Y)`; by hypothesis, the graded `(𝒪_Y|U)`-algebra `𝒮|U` is
isomorphic to `S̃`, where `S = Γ(U, 𝒮)` is a graded `A`-algebra `(I, 1.4.3)`. Set `X_U = Proj(Γ(U, 𝒮))`. Let `U' ⊂ U` be
a second affine open of `Y`, with ring `A'`, and let `j : U' → U` be the canonical injection, which corresponds to the
restriction homomorphism `A → A'`; we have `𝒮|U' = j*(𝒮|U)`, and so `S' = Γ(U', 𝒮)` is canonically identified with
`S ⊗_A A'` `(I, 1.6.5)`. We

<!-- original page 50 -->

conclude (2.8.10) that `X_{U'}` is canonically identified with `X_U ×_U U'`, and so also with `f_U⁻¹(U')`, where `f_U`
denotes the structure morphism `X_U → U` `(I, 4.4.1)`. We denote by `σ_{U', U}` the canonical isomorphism
`f_U⁻¹(U') ⥲ X_{U'}` so defined, and by `ρ_{U', U}` the open immersion `X_{U'} → X_U` obtained by composing
`σ_{U', U}⁻¹` with the canonical injection `f_U⁻¹(U') → X_U`. It is immediate that, if `U'' ⊂ U'` is a third affine open
of `Y`, then `ρ_{U'', U} = ρ_{U'', U'} ∘ ρ_{U', U}`.

**Proposition.**

<!-- label: II.3.1.2 -->

Let `Y` be a prescheme. For every quasi-coherent positively-graded `𝒪_Y`-algebra `𝒮`, there exists a prescheme `X` over
`Y`, unique up to `Y`-isomorphism, with the following property: if `f : X → Y` is the structure morphism, then for every
affine open `U` of `Y`, there exists an isomorphism `η_U` from the induced prescheme `f⁻¹(U)` to `X_U = Proj(Γ(U, 𝒮))`
such that, if `V` is a second affine open of `Y` contained in `U`, then the diagram

```text
              η_V
   f⁻¹(V) ─────────→ X_V                                                  (3.1.2.1)
     │                │
     ↓                ↓ ρ_{V, U}
   f⁻¹(U) ─────────→ X_U
              η_U
```

commutes.

**Proof.** For two affine opens `U`, `V` of `Y`, let `X_{U, V}` be the prescheme induced on `f_U⁻¹(U ∩ V)` by `X_U`; we
will define a `Y`-isomorphism `θ_{U, V} : X_{V, U} ⥲ X_{U, V}`. For this, consider an affine open `W ⊂ U ∩ V`: by
composing the isomorphisms

```text
                   σ_{W, U}            σ_{W, V}⁻¹
   f_U⁻¹(W) ─────────────→ X_W ─────────────→ f_V⁻¹(W),
```

we obtain an isomorphism `τ_W`, and one checks at once that, if `W' ⊂ W` is an affine open, then `τ_{W'}` is the
restriction of `τ_W` to `f_U⁻¹(W')`; the `τ_W` are therefore the restrictions of a `Y`-isomorphism `θ_{V, U}`. Moreover,
if `U`, `V`, `W` are three affine opens of `Y`, and `θ'_{U, V}`, `θ'_{V, W}`, `θ'_{U, W}` denote the restrictions of
`θ_{U, V}`, `θ_{V, W}`, `θ_{U, W}` to the inverse images of `U ∩ V ∩ W` in `X_V`, `X_W`, `X_W` respectively, it follows
from the above definitions that `θ'_{U, V} ∘ θ'_{V, W} = θ'_{U, W}`. The existence of an `X` satisfying the stated
properties therefore follows from `(I, 2.3.1)`; its uniqueness up to `Y`-isomorphism is trivial in view of (3.1.2.1).

**(3.1.3)**

<!-- label: II.3.1.3 -->

We say that the prescheme `X` defined in (3.1.2) is the _homogeneous spectrum_ of the quasi-coherent graded
`𝒪_Y`-algebra `𝒮`, and we denote it by `Proj(𝒮)`. It is immediate that `Proj(𝒮)` is _separated over_ `Y` ((2.4.2) and
`(I, 5.5.5)`); if `𝒮` is an `𝒪_Y`-algebra _of finite type_ `(I, 9.6.2)`, then `Proj(𝒮)` is _of finite type_ over `Y`
((2.7.1, (ii)) and `(I, 6.3.1)`).

If `f` is the structure morphism `X → Y`, then for every prescheme induced by `Y` on an open subset `U` of `Y`, `f⁻¹(U)`
is identified with the homogeneous spectrum `Proj(𝒮|U)`.

**Proposition.**

<!-- label: II.3.1.4 -->

Let `f ∈ Γ(Y, 𝒮_d)` for `d > 0`. There exists an open subset `X_f` of the underlying space of `X = Proj(𝒮)` with the
following property: for every affine open `U` of `Y`, `X_f ∩ φ⁻¹(U) = D_+(f|U)` in `φ⁻¹(U)` identified with
`X_U = Proj(Γ(U, 𝒮))` (where `φ` denotes the structure morphism `X → Y`).

<!-- original page 51 -->

Furthermore, the prescheme induced on `X_f` is affine over `Y` and is canonically isomorphic to
`Spec(𝒮^{(d)}/(f − 1)𝒮^{(d)})` (1.3.1).

**Proof.** We have `f|U ∈ Γ(U, 𝒮_d) = (Γ(U, 𝒮))_d`. If `U`, `U'` are affine opens of `Y` with `U' ⊂ U`, then `f|U'` is
the image of `f|U` under the restriction homomorphism

```text
  Γ(U, 𝒮) → Γ(U', 𝒮),
```

so `D_+(f|U')` is equal (with the notation of (3.1.1)) to the prescheme induced on the inverse image
`ρ_{U', U}⁻¹(D_+(f|U))` in `X_{U'}` (2.8.1); whence the first assertion. Furthermore, the prescheme induced on
`D_+(f|U)` by `X_U` is canonically identified with `Spec((Γ(U, 𝒮))_{(f|U)})`, these identifications being compatible
with the restriction homomorphisms (2.8.1); the second assertion then follows from (2.2.5) and the commutativity of
diagram (2.8.2.1).

We also say that `X_f` (as an open subset of the underlying space `X`) is the set of `x ∈ X` where `f` _does not
vanish_.

**Corollary.**

<!-- label: II.3.1.5 -->

If `f ∈ Γ(Y, 𝒮_d)` and `g ∈ Γ(Y, 𝒮_e)`, then

```text
  X_{fg} = X_f ∩ X_g.                                                     (3.1.5.1)
```

**Proof.** It suffices to consider the intersection of both sides with a set `φ⁻¹(U)`, where `U` is an affine open of
`Y`, and to apply formula (2.3.3.2).

**Corollary.**

<!-- label: II.3.1.6 -->

Let `(f_α)` be a family of sections of `𝒮` over `Y` such that `f_α ∈ Γ(Y, 𝒮_{d_α})`; if the sheaf of ideals of `𝒮`
generated by this family `(0, 5.1.1)` contains all the `𝒮_n` from some rank on, then the underlying space `X` is the
union of the `X_{f_α}`.

**Proof.** For every affine open `U` of `Y`, `φ⁻¹(U)` is the union of the `X_{f_α} ∩ φ⁻¹(U)` (2.3.14).

**Corollary.**

<!-- label: II.3.1.7 -->

Let `𝒜` be a quasi-coherent `𝒪_Y`-algebra; set

```text
  𝒮 = 𝒜[T] = 𝒜 ⊗_ℤ ℤ[T]
```

where `T` is an indeterminate (and `ℤ`, `ℤ[T]` are viewed as constant sheaves on `Y`). Then `X = Proj(𝒮)` is canonically
identified with `Spec(𝒜)`. In particular, `Proj(𝒪_Y[T])` is identified with `Y`.

**Proof.** Applying (3.1.6) to the unique section `f ∈ Γ(Y, 𝒮)` that equals `T` at each point of `Y`, we see that
`X_f = X`. Here `d = 1`, and `𝒮^{(1)}/(f − 1)𝒮^{(1)} = 𝒮/(f − 1)𝒮` is canonically isomorphic to `𝒜`; whence the
corollary, by (1.2.2).

Let `g ∈ Γ(Y, 𝒪_Y)`; taking `𝒮 = 𝒪_Y[T]`, we have `g ∈ Γ(Y, 𝒮_0)`; set

```text
  h = gT ∈ Γ(Y, 𝒮_1).
```

If `X = Proj(𝒮)`, then the canonical identification defined in (3.1.7) identifies `X_h` with the open subset `Y_g` of
`Y` (in the sense of `(0, 5.5.2)`): indeed, we may reduce to the case `Y = Spec(A)` affine, and everything then reduces
(taking (2.2.5) into account) to the fact that the ring of fractions `A_g` is canonically identified with
`A[T]/(gT − 1)A[T]` `(0, 1.2.3)`.

**Proposition.**

<!-- label: II.3.1.8 -->

Let `𝒮` be a quasi-coherent positively-graded `𝒪_Y`-algebra.

1. For every `d > 0`, there is a canonical `Y`-isomorphism from `Proj(𝒮)` to `Proj(𝒮^{(d)})`.

<!-- original page 52 -->

1. Let `𝒮'` be the graded `𝒪_Y`-algebra given by the direct sum of `𝒪_Y` with the `𝒮_n` (`n ≥ 0`); then `Proj(𝒮')` and
    `Proj(𝒮)` are canonically `Y`-isomorphic.
1. Let `ℒ` be an invertible `𝒪_Y`-module `(0, 5.4.1)`, and let `𝒮_{(ℒ)}` be the graded `𝒪_Y`-algebra given by the direct
    sum of the `𝒮_d ⊗ ℒ^{⊗ d}` (`d ≥ 0`); then `Proj(𝒮)` and `Proj(𝒮_{(ℒ)})` are canonically `Y`-isomorphic.

**Proof.** In each of the three cases, it suffices to define the isomorphism locally on `Y`, since the verification of
compatibility with restriction from one open to a smaller one is trivial. We may thus suppose `Y` affine, and then (i)
follows from (2.4.7, (i)) and (ii) from (2.4.8). As for (iii), if we further suppose `ℒ` isomorphic to `𝒪_Y` (allowed,
the question being local on `Y`), the isomorphism between `Proj(𝒮)` and `Proj(𝒮_{(ℒ)})` is evident; to define a
_canonical_ isomorphism, let `Y = Spec(A)` and `𝒮 = S̃`, where `S` is a graded `A`-algebra, and let `c` be a generator
of the free `A`-module `L` such that `ℒ = L̃`; then, for every `n > 0`, `x_n ↦ x_n ⊗ c^{⊗ n}` is an `A`-isomorphism from
`S_n` to `S_n ⊗ L^{⊗ n}`, and these `A`-isomorphisms define an `A`-isomorphism of graded algebras
`φ_c : S → S_{(L)} = ⊕_{n ≥ 0} S_n ⊗ L^{⊗ n}`. Now let `f ∈ S_+` be homogeneous of degree `d`; for every `x ∈ S_{nd}`,
we have `(x ⊗ c^{nd})/(f ⊗ c^d)^n = (x ⊗ (εc)^{nd})/(f ⊗ (εc)^d)^n` for every invertible `ε ∈ A`, which shows that the
isomorphism `S_{(f)} → (S_{(L)})_{(f ⊗ c^d)}` induced from `φ_c` is _independent_ of the generator `c` of `L`,
completing the proof.

**(3.1.9)**

<!-- label: II.3.1.9 -->

Recall `(0, 4.1.3)` and `(I, 1.3.14)` that, for the quasi-coherent graded `𝒪_Y`-algebra `𝒮` to be _generated by the
`𝒪_Y`-module `𝒮_1`_, it is necessary and sufficient that there exist an affine open covering `(U_α)` of `Y` such that
the graded algebra `Γ(U_α, 𝒮)` over `Γ(U_α, 𝒮_0)` is generated by the set `Γ(U_α, 𝒮_1)` of its homogeneous elements of
degree `1`. For every open `V` of `Y`, `𝒮|V` is then generated by the `(𝒪_Y|V)`-module `𝒮_1|V`.

**Proposition.**

<!-- label: II.3.1.10 -->

Suppose there exists a finite affine open covering `(U_i)` of `Y` such that each graded algebra `Γ(U_i, 𝒮)` is of finite
type over `Γ(U_i, 𝒪_Y)`. Then there exists `d > 0` such that `𝒮^{(d)}` is generated by `𝒮_d`, with `𝒮_d` an `𝒪_Y`-module
of finite type.

**Proof.** By (2.1.6, (v)), for each `i` there exists an integer `m_i` such that
`Γ(U_i, 𝒮_{nm_i}) = (Γ(U_i, 𝒮_{m_i}))^n` for every `n > 0`; it suffices to take `d` to be a common multiple of the
`m_i`, in view of (2.1.6, (i)).

**Corollary.**

<!-- label: II.3.1.11 -->

Under the hypotheses of (3.1.10), `Proj(𝒮)` is `Y`-isomorphic to a homogeneous spectrum `Proj(𝒮')`, where `𝒮'` is a
graded `𝒪_Y`-algebra generated by `𝒮'_1`, with `𝒮'_1` an `𝒪_Y`-module of finite type.

**Proof.** It suffices to take `𝒮' = 𝒮^{(d)}`, with `d` determined by the property of (3.1.10), and to apply (3.1.8,
(i)).

**(3.1.12)**

<!-- label: II.3.1.12 -->

If `𝒮` is a quasi-coherent positively-graded `𝒪_Y`-algebra, we know `(I, 5.1.1)` that its _nilradical_ `𝒩` is a
quasi-coherent `𝒪_Y`-module; we say that `𝒩_+ = 𝒩 ∩ 𝒮_+` is the _nilradical of `𝒮_+`_; this is a quasi-coherent graded
`𝒮_0`-module, since we reduce at once to the case `Y` affine, and the proposition then follows from (2.1.10). For every
`y ∈ Y`, `(𝒩_+)_y` is then the nilradical of `(𝒮_+)_y = (𝒮_y)_+` `(I, 5.1.1)`. We say that the graded `𝒪_Y`-algebra `𝒮`
is _essentially reduced_ if `𝒩_+ = 0`, which is equivalent

<!-- original page 53 -->

to saying that `𝒮_y` is an essentially reduced graded `𝒪_y`-algebra for every `y ∈ Y`. For every graded `𝒪_Y`-algebra
`𝒮`, `𝒮/𝒩_+` is essentially reduced.

We say that `𝒮` is _integral_ if, for every `y ∈ Y`, `𝒮_y` is an integral ring and moreover `(𝒮_y)_+ = (𝒮_+)_y ≠ 0`.

**Proposition.**

<!-- label: II.3.1.13 -->

Let `𝒮` be a positively-graded `𝒪_Y`-algebra. If `X = Proj(𝒮)`, then the `Y`-scheme `X_red` is canonically isomorphic to
`Proj(𝒮/𝒩_+)`; in particular, if `𝒮` is essentially reduced, then `X` is reduced.

**Proof.** That `X' = Proj(𝒮/𝒩_+)` is reduced follows immediately from (2.4.4, (i)), the property being local; moreover,
for every affine open `U ⊂ Y`, `φ'⁻¹(U) = (φ⁻¹(U))_red` (where `φ` and `φ'` denote the structure morphisms `X → Y` and
`X' → Y`); one checks at once that the canonical `U`-morphisms `φ'⁻¹(U) → φ⁻¹(U)` are compatible with restriction and so
define a closed immersion `X' → X` that is a homeomorphism of underlying spaces; whence the conclusion `(I, 5.1.2)`.

**Proposition.**

<!-- label: II.3.1.14 -->

Let `Y` be an integral prescheme, and `𝒮` a quasi-coherent graded `𝒪_Y`-algebra such that `𝒮_0 = 𝒪_Y`.

1. If `𝒮` is integral (3.1.12), then `X = Proj(𝒮)` is integral and the structure morphism `φ : X → Y` is dominant.
1. Suppose further that `𝒮` is essentially reduced. Then conversely, if `X` is integral and `φ` is dominant, then `𝒮` is
    integral.

**Proof.**

(i) If `(U_α)` is a base of `Y` consisting of non-empty affine opens, it suffices to prove the proposition with `Y`
replaced by one of the `U_α` and `𝒮` by `𝒮|U_α`: indeed, on the one hand the underlying spaces `φ⁻¹(U_α)` will be
irreducible (hence non-empty) opens of `X` such that `φ⁻¹(U_α) ∩ φ⁻¹(U_β) ≠ ∅` for every pair of indices (since
`U_α ∩ U_β` contains some `U_γ`), so `X` will be irreducible `(0, 2.1.4)`; on the other hand, `X` will be reduced, since
this is a local property, and so `X` will be integral and `φ(X)` dense in `Y`.

Suppose then that `Y = Spec(A)`, `A` integral `(I, 5.1.4)`, and `𝒮 = S̃`, with `S` a graded `A`-algebra; the hypothesis
is that for every `y ∈ Y`, `S̃_y = S_y` is an integral graded ring with `(S_y)_+ ≠ 0`. It suffices to show `S` is an
_integral_ ring, since then `S_+ ≠ 0` and we may apply (2.4.4, (ii)). Let `f, g ≠ 0` in `S` and suppose `fg = 0`; for
every `y ∈ Y` we have `(f/1)(g/1) = 0` in `S_y`, so `f/1 = 0` or `g/1 = 0` by hypothesis. Suppose, say, `f/1 = 0` in
`S_y`; this means there exists `a ∈ A` with `a ∉ 𝔧_y` and `af = 0`; then for every `z ∈ Y`, `(a/1)(f/1) = 0` in the
integral ring `S_z`, and since `a/1 ≠ 0` (since `A` is integral), `f/1 = 0`, which forces `f = 0`.

(ii) The question being local on `Y`, we may again assume `Y = Spec(A)`, `A` integral, and `𝒮 = S̃`. By hypothesis, for
every `y ∈ Y`, `(S_y)_+` contains no non-zero nilpotent element, and the same holds for `(S_0)_y = A_y` by hypothesis;
so `S_y` is a reduced ring for every `y ∈ Y`, whence `S` itself is reduced `(I, 5.1.1)`. The hypothesis that `X` is
integral implies that `S` is essentially integral (2.4.4, (ii)), and everything reduces to showing that the annihilator
`𝔍` of `S_+` in `A = S_0` is reduced to `0` (2.1.11). Otherwise we would have

<!-- original page 54 -->

`(S_h)_+ = 0` for some `h ≠ 0` in `𝔍`, hence (3.1.1) `φ⁻¹(D(h)) = ∅`, and `φ(X)` would not be dense in `Y` contrary to
hypothesis (since `D(h) ≠ ∅`, `h` being non-nilpotent).

## 3.2. Sheaf on `Proj(𝒮)` associated to a graded `𝒮`-module

**(3.2.1)**

<!-- label: II.3.2.1 -->

Let `Y` be a prescheme, `𝒮` a quasi-coherent positively-graded `𝒪_Y`-algebra, and `ℳ` a quasi-coherent graded `𝒮`-module
(on `(Y, 𝒪_Y)`, or equivalently `(I, 9.6.1)` on the ringed space `(Y, 𝒮)`). With the notation of (3.1.1), we denote by
`ℳ̃_U` the quasi-coherent `𝒪_{X_U}`-module `(Γ(U, ℳ))̃`; for `U' ⊂ U`, `Γ(U', ℳ)` is canonically identified with
`Γ(U, ℳ) ⊗_A A'` `(I, 1.6.4)`; thus `ℳ̃_{U'} = ρ_{U', U}*(ℳ̃_U)` (2.8.11).

**Proposition.**

<!-- label: II.3.2.2 -->

There exists on `Proj(𝒮) = X` a unique quasi-coherent `𝒪_X`-module `ℳ̃` such that, for every affine open `U` of `Y`,
`η_U*((Γ(U, ℳ))̃) = ℳ̃|f⁻¹(U)` (where `η_U` denotes the isomorphism `f⁻¹(U) ⥲ Proj(Γ(U, 𝒮))` and `f` is the structure
morphism `X → Y`).

**Proof.** Since `ρ_{U', U}` is identified with the injection morphism `f⁻¹(U') → f⁻¹(U)` (3.1.2.1), the proposition
follows at once from the relation `ℳ̃_{U'} = ρ_{U', U}*(ℳ̃_U)` and the gluing principle for sheaves `(0, 3.3.1)`.

We say that `ℳ̃` is the `𝒪_X`-module _associated to_ the quasi-coherent graded `𝒮`-module `ℳ`.

**Proposition.**

<!-- label: II.3.2.3 -->

Let `ℳ` be a quasi-coherent graded `𝒮`-module, and let `f ∈ Γ(Y, 𝒮_d)` (`d > 0`). If `ξ_f` is the canonical isomorphism
from `X_f` to the `Y`-prescheme `Z_f = Spec(𝒮^{(d)}/(f − 1)𝒮^{(d)})` (3.1.4), then `(ξ_f)_*(ℳ̃|X_f)` is the
`𝒪_{Z_f}`-module `(ℳ^{(d)}/(f − 1)ℳ^{(d)})̃` (1.4.3).

**Proof.** The question being local on `Y`, we reduce immediately to (2.2.5), using the commutativity of diagram
(2.8.12.1).

**Proposition.**

<!-- label: II.3.2.4 -->

The `𝒪_X`-module `ℳ̃` is a covariant additive exact functor in `ℳ` from the category of quasi-coherent graded
`𝒮`-modules to the category of quasi-coherent `𝒪_X`-modules, which commutes with inductive limits and direct sums.

**Proof.** The question being local on `Y`, we reduce to `(I, 1.3.11)`, `(I, 1.3.9)`, and (2.5.4).

In particular, if `𝒩` is a quasi-coherent graded sub-`𝒮`-module of `ℳ`, then `𝒩̃` is canonically identified with a
quasi-coherent sub-`𝒪_X`-module of `ℳ̃`; more specifically, for every quasi-coherent graded sheaf of ideals `𝒥` of `𝒮`,
`𝒥̃` is a quasi-coherent sheaf of ideals of `𝒪_X`.

If `ℳ` is a quasi-coherent graded `𝒮`-module and `ℐ` a quasi-coherent sheaf of ideals of `𝒪_Y`, then `ℐℳ` is a
quasi-coherent graded sub-`𝒮`-module of `ℳ`, and

```text
  (ℐℳ)̃ = ℐ · ℳ̃                                                            (3.2.4.1)
```

(the right-hand side in the sense of `(0, 4.3.5)`). It suffices to verify this in the case `Y = Spec(A)` affine,
`𝒮 = S̃` with `S` a graded `A`-algebra, `ℳ = M̃`

<!-- original page 55 -->

with `M` a graded `S`-module, and `ℐ = 𝔍` with `𝔍` an ideal of `A`. For every homogeneous element `f` of `S_+`, the
restriction to `D_+(f) = Spec(S_{(f)})` of the left-hand side of (3.2.4.1) is associated to `(𝔍M)_{(f)} = 𝔍 · M_{(f)}`,
and the same holds for the restriction of the right-hand side, by `(I, 1.3.13)` and `(I, 1.6.9)`.

**Proposition.**

<!-- label: II.3.2.5 -->

Let `f ∈ Γ(Y, 𝒮_d)` (`d > 0`). On the open subset `X_f`, the `(𝒪_X|X_f)`-module `(𝒮(nd))̃|X_f` is canonically isomorphic
to `𝒪_X|X_f` for every `n ∈ ℤ`. In particular, if the `𝒪_Y`-algebra `𝒮` is generated by `𝒮_1` (3.1.9), then the
`𝒪_X`-modules `(𝒮(n))̃` are invertible for every `n ∈ ℤ`.

**Proof.** Indeed, for every affine open `U` of `Y`, we defined in (2.5.7) a canonical isomorphism from
`(𝒮(nd))̃|(X_f ∩ φ⁻¹(U))` to `𝒪_X|(X_f ∩ φ⁻¹(U))`, in view of (3.1.4) (where `φ` is the structure morphism `X → Y`); one
checks at once that these isomorphisms are compatible with restriction from `U` to an affine open `U' ⊂ U`, whence the
first assertion. For the second, note that if `𝒮` is generated by `𝒮_1`, there is an affine open covering `(U_α)` of `Y`
such that `Γ(U_α, 𝒮)` is generated by `Γ(U_α, 𝒮)_1 = Γ(U_α, 𝒮_1)`; we then apply (2.5.9), the property of being
invertible being local.

We also set, for every `n ∈ ℤ`,

```text
  𝒪_X(n) = (𝒮(n))̃                                                         (3.2.5.1)
```

and, for every `𝒪_X`-module `ℱ`,

```text
  ℱ(n) = ℱ ⊗_{𝒪_X} 𝒪_X(n).                                                (3.2.5.2)
```

It follows at once from these definitions that, for every open `U` of `Y`,

```text
  ((𝒮|U)(n))̃ = 𝒪_X(n)|f⁻¹(U)
```

where `f` is the structure morphism `X → Y`.

**Proposition.**

<!-- label: II.3.2.6 -->

Let `ℳ` and `𝒩` be quasi-coherent graded `𝒮`-modules. There is a canonical homomorphism, functorial in `ℳ` and `𝒩`,

```text
  λ : ℳ̃ ⊗_{𝒪_X} 𝒩̃ → (ℳ ⊗_𝒮 𝒩)̃                                            (3.2.6.1)
```

and a canonical homomorphism, functorial in `ℳ` and `𝒩`,

```text
  μ : (𝓗𝓸𝓶_𝒮(ℳ, 𝒩))̃ → 𝓗𝓸𝓶_{𝒪_X}(ℳ̃, 𝒩̃).                                   (3.2.6.2)
```

Furthermore, if `𝒮` is generated by `𝒮_1` (3.1.9), then `λ` is an isomorphism; if in addition `ℳ` admits a finite
presentation (3.1.1), then `μ` is an isomorphism.

**Proof.** The isomorphisms `λ` and `μ` were defined in (2.5.11.2) and (2.5.12.2) when `Y` is affine; these definitions
being local, they extend at once to the general case considered here, in view of (2.8.14).

**Corollary.**

<!-- label: II.3.2.7 -->

If `𝒮` is generated by `𝒮_1`, then for any `m, n ∈ ℤ`,

```text
  𝒪_X(m) ⊗_{𝒪_X} 𝒪_X(n) = 𝒪_X(m + n)                                      (3.2.7.1)

  𝒪_X(n) = (𝒪_X(1))^{⊗ n}                                                 (3.2.7.2)
```

up to canonical isomorphism.

<!-- original page 56 -->

**Corollary.**

<!-- label: II.3.2.8 -->

If `𝒮` is generated by `𝒮_1`, then for every graded `𝒮`-module `ℳ` and every `n ∈ ℤ`,

```text
  (ℳ(n))̃ = ℳ̃(n)                                                          (3.2.8.1)
```

up to canonical isomorphism.

**Proof.** This follows from the corresponding properties for `Y` affine ((2.5.14) and (2.5.15)) together with (2.8.11).

**Remarks.**

<!-- label: II.3.2.9 -->

(i) If `𝒮 = 𝒜[T]` with `𝒜` a quasi-coherent `𝒪_Y`-algebra (3.1.7), one checks at once that all the invertible
`𝒪_X`-modules `𝒪_X(n)` are canonically isomorphic to `𝒪_X`.

Furthermore, let `𝒩` be a quasi-coherent `𝒜`-module, and set `ℳ = 𝒩 ⊗_𝒜 𝒜[T]`. It then follows from (3.2.3) and (3.1.7)
that, under the canonical identification of `X = Proj(𝒜[T])` with `X' = Spec(𝒜)`, the `𝒪_X`-module `ℳ̃` is identified
with the `𝒪_{X'}`-module `𝒩̃` associated to `𝒩` (in the sense of (1.4.3)).

(ii) Let `𝒮` be an arbitrary graded `𝒪_Y`-algebra, and let `𝒮'` be the graded `𝒪_Y`-algebra such that `𝒮'_0 = 𝒪_Y` and
`𝒮'_n = 𝒮_n` for every `n > 0`; the canonical isomorphism from `X = Proj(𝒮)` to `X' = Proj(𝒮')` (3.1.8, (ii)) identifies
`𝒪_X(n)` with `𝒪_{X'}(n)` for every `n ∈ ℤ`: this follows from the same proposition in the affine case (2.5.16) and from
the fact that, on the affine opens of `Y`, these identifications commute with restriction. Similarly, let
`X^{(d)} = Proj(𝒮^{(d)})`; the canonical isomorphism from `X` to `X^{(d)}` (3.1.8, (i)) identifies `𝒪_X(nd)` with
`𝒪_{X^{(d)}}(n)` for every `n ∈ ℤ`.

**Proposition.**

<!-- label: II.3.2.10 -->

Let `ℒ` be an invertible `𝒪_Y`-module, and let `g` be the canonical isomorphism `X_{(ℒ)} = Proj(𝒮_{(ℒ)}) ⥲ X = Proj(𝒮)`
(3.1.8, (iii)). For every `n ∈ ℤ`, `g_*(𝒪_{X_{(ℒ)}}(n))` is canonically isomorphic to `𝒪_X(n) ⊗_Y ℒ^{⊗ n}`.

**Proof.** Suppose first that `Y` is affine with ring `A` and `ℒ = L̃`, with `L` a free `A`-module of rank `1`. With the
notation of the proof of (3.1.8, (iii)), we define, for `f ∈ S_d`, an isomorphism from `(S(n))_{(f)} ⊗_A L^{⊗ n}` to
`(S_{(L)}(n))_{(f ⊗ c^d)}` by sending `(x/f^k) ⊗ c^n`, with `x ∈ S_{kd+n}`, to `(x ⊗ c^{n+kd})/(f ⊗ c^d)^k`; one checks
at once that this isomorphism is independent of the chosen generator `c` of `L`; furthermore, the isomorphisms so
defined for each `f ∈ S_+` are compatible with the restriction operators `D_+(f) → D_+(fg)`. Finally, in the general
case, one sees easily, going back to the definitions (3.1.1), that the isomorphisms so defined for each affine open `U`
of `Y` are compatible with passage from `U` to an affine open `U' ⊂ U`.

## 3.3. Graded `𝒮`-module associated to a sheaf on `Proj(𝒮)`

_Throughout this entire section we suppose that the graded `𝒪_Y`-algebra `𝒮` is generated by `𝒮_1` (3.1.9)._ Recall
that, by (3.1.8, (i)), this restriction is not essential, given the finiteness conditions (3.1.10).

**(3.3.1)**

<!-- label: II.3.3.1 -->

Let `p` be the structure morphism `X = Proj(𝒮) → Y`. For every `𝒪_X`-module `ℱ`, set

```text
  Γ_*(ℱ) = ⊕_{n ∈ ℤ} p_*(ℱ(n))                                            (3.3.1.1)
```

<!-- original page 57 -->

and in particular

```text
  Γ_*(𝒪_X) = ⊕_{n ∈ ℤ} p_*(𝒪_X(n)).                                       (3.3.1.2)
```

We know `(0, 4.2.2)` that there is a canonical homomorphism

```text
  p_*(ℱ) ⊗_{𝒪_Y} p_*(𝒢) → p_*(ℱ ⊗_{𝒪_X} 𝒢)
```

for two `𝒪_X`-modules `ℱ` and `𝒢`; we therefore deduce from (3.2.7.1) that `Γ_*(𝒪_X)` is endowed with the structure of a
_graded `𝒪_Y`-algebra_, and (3.2.5.2) similarly defines on `Γ_*(ℱ)` the structure of a _graded `Γ_*(𝒪_X)`-module_.

By (3.2.5) and the left-exactness of `p_*` `(0, 4.2.1)`, `Γ_*(ℱ)` is a covariant additive left-exact functor in `ℱ` from
the category of `𝒪_X`-modules to the category of graded `𝒪_Y`-modules (with morphisms of degree `0`). In particular, if
`𝒥` is a sheaf of ideals of `𝒪_X`, then `Γ_*(𝒥)` is identified with a graded sheaf of ideals of `Γ_*(𝒪_X)`.

**(3.3.2)**

<!-- label: II.3.3.2 -->

Let `ℳ` be a quasi-coherent graded `𝒮`-module. For every affine open `U` of `Y`, we defined in (2.6.2) a homomorphism of
abelian groups

```text
  α_{0, U} : Γ(U, ℳ_0) → Γ(p⁻¹(U), ℳ̃).
```

It is immediate that these homomorphisms commute with restriction (2.8.13.1) and so define (without using the hypothesis
that `𝒮` is generated by `𝒮_1`) a homomorphism of sheaves of abelian groups

```text
  α_0 : ℳ_0 → p_*(ℳ̃).                                                    (3.3.2.1)
```

Applying this to each `ℳ_n = (ℳ(n))_0` and using (3.2.8.1), we define a homomorphism of sheaves of abelian groups

```text
  α_n : ℳ_n → p_*(ℳ̃(n))                                                  (3.3.2.2)
```

for every `n ∈ ℤ`, whence a functorial homomorphism (of degree `0`) of graded sheaves of abelian groups

```text
  α : ℳ → Γ_*(ℳ̃)                                                         (3.3.2.3)
```

(also denoted `α_ℳ`).

Taking `ℳ = 𝒮` in particular, one checks that `α : 𝒮 → Γ_*(𝒪_X)` is a homomorphism of graded `𝒪_Y`-algebras, and that
(3.3.2.3) is a di-homomorphism of graded modules relative to this homomorphism of graded algebras.

We also note that to each `α_n` corresponds `(0, 4.4.3)` a canonical homomorphism of `𝒪_X`-modules

```text
  α_n♯ : p*(ℳ_n) → ℳ̃(n).                                                 (3.3.2.4)
```

One checks without difficulty that this homomorphism is precisely the one which corresponds functorially (3.2.4) to the
canonical homomorphism (of degree `0`) of graded `𝒪_Y`-modules

```text
  ℳ_n ⊗_{𝒪_Y} 𝒮 → ℳ(n)                                                   (3.3.2.5)
```

<!-- original page 58 -->

where the grading on the right-hand side comes naturally from that of `𝒮`. We may restrict to the case `Y = Spec(A)`
affine, `ℳ = M̃`, and `𝒮 = S̃`, with the graded `A`-algebra `S` generated by `S_1`, so that as `f` runs over `S_1` the
`D_+(f)` form a covering of `X`. Returning to the definitions (2.6.2) and using `(I, 1.6.7)`, the restriction to
`D_+(f)` of the homomorphism (3.3.2.4) corresponds `(I, 1.3.8)` to the homomorphism of `S_{(f)}`-modules
`M_n ⊗_A S_{(f)} → (S(n))_{(f)}` sending `x ⊗ 1` (with `x ∈ M_n`) to `x/1`; this proves the claim.

**Proposition.**

<!-- label: II.3.3.3 -->

For every section `f ∈ Γ(Y, 𝒮_d)` (`d > 0`), `X_f` coincides with the set of points of `X` where `α_d(f)` (considered as
a section of `𝒪_X(d)`) does not vanish `(0, 5.5.2)`.

**Proof.** (Note that `α_d(f)` is a section of `p_*(𝒪_X(d))` over `Y`, but by definition such a section is also a
section of `𝒪_X(d)` over `X` `(0, 4.2.1)`.) The definition of `X_f` (3.1.4) reduces us to the case `Y` affine, which was
handled in (2.6.3).

**(3.3.4)**

<!-- label: II.3.3.4 -->

From now on, in addition to the hypothesis at the start of this section, we suppose that for every quasi-coherent
`𝒪_X`-module `ℱ`, the `p_*(ℱ(n))` are quasi-coherent on `Y`, so that `Γ_*(ℱ) = ⊕_{n ∈ ℤ} p_*(ℱ(n))` is also a
quasi-coherent `𝒪_Y`-module (`(I, 1.4.1)` and `(I, 1.3.9)`); this will always be the case in particular if `X` is of
finite type over `Y` `(I, 9.2.2)`. We thus conclude that `(Γ_*(ℱ))̃` is defined and is a quasi-coherent `𝒪_X`-module.
For every affine open `U` of `Y`, we have (`(I, 1.3.9)` and (2.5.4))

```text
  (Γ(U, ⊕_{n ∈ ℤ} p_*(ℱ(n))))̃
    = ⊕_{n ∈ ℤ} (Γ(U, p_*(ℱ(n))))̃
    = ⊕_{n ∈ ℤ} (Γ(p⁻¹(U), ℱ(n)))̃
    = (⊕_{n ∈ ℤ} Γ(p⁻¹(U), ℱ(n)))̃
    = (Γ_*(ℱ|p⁻¹(U)))̃
```

and so (2.6.4) we have a canonical homomorphism

```text
  β_U : (Γ(U, ⊕_{n ∈ ℤ} p_*(ℱ(n))))̃ → ℱ|p⁻¹(U).
```

Furthermore, the commutativity of (2.8.13.2) shows that these homomorphisms commute with restriction on `Y`; we thus
obtain a canonical functorial homomorphism

```text
  β : (Γ_*(ℱ))̃ → ℱ                                                       (3.3.4.1)
```

(also denoted `β_ℱ`) for quasi-coherent `𝒪_X`-modules.

**Proposition.**

<!-- label: II.3.3.5 -->

Let `ℳ` be a quasi-coherent graded `𝒮`-module, and `ℱ` a quasi-coherent `𝒪_X`-module; the composite homomorphisms

```text
                α̃                    β
  ℳ̃ ─────→ (Γ_*(ℳ̃))̃ ─────→ ℳ̃                                            (3.3.5.1)

                  α                          Γ_*(β)
  Γ_*(ℱ) ─────→ Γ_*((Γ_*(ℱ))̃) ─────→ Γ_*(ℱ)                              (3.3.5.2)
```

are the identity isomorphisms.

**Proof.** The question is local on `Y`, so we reduce to (2.6.5).

<!-- original page 59 -->

## 3.4. Finiteness conditions

**Proposition.**

<!-- label: II.3.4.1 -->

Let `Y` be a prescheme, `𝒮` a quasi-coherent `𝒪_Y`-algebra generated by `𝒮_1` (3.1.9); suppose further that `𝒮_1` is of
finite type. Then `X = Proj(𝒮)` is of finite type over `Y`.

**Proof.** The question being local on `Y`, we may suppose `Y` affine with ring `A`; then `𝒮 = S̃` with `S = Γ(Y, 𝒮)`,
and by hypothesis `S` is an `A`-algebra generated by `S_1 = Γ(Y, 𝒮_1)`, where we may further assume that `S_1` is an
`A`-module of finite type (`(I, 1.3.9)` and `(I, 1.3.12)`). Then `S` is a graded `A`-algebra of finite type, and we
reduce to (2.7.1, (ii)).

**(3.4.2)**

<!-- label: II.3.4.2 -->

Let `𝒮` be a quasi-coherent graded `𝒪_Y`-algebra; for a quasi-coherent graded `𝒮`-module `ℳ`, we consider the following
finiteness conditions:

- **(TF)** _There exists an integer `n` such that the `𝒮`-module `⊕_{k ≥ n} ℳ_k` is of finite type._
- **(TN)** _There exists an integer `n` such that `ℳ_k = 0` for `k ≥ n`._

If `ℳ` satisfies (TN), then `ℳ̃ = 0`, since this is a local property on `Y` (2.7.2).

Let `ℳ`, `𝒩` be quasi-coherent graded `𝒮`-modules; we say that a homomorphism `u : ℳ → 𝒩` of degree `0` is
_(TN)-injective_ (resp. _(TN)-surjective_, _(TN)-bijective_) if there exists an integer `n` such that `u_k : ℳ_k → 𝒩_k`
is injective (resp. surjective, bijective) for `k ≥ n`; then `ũ : ℳ̃ → 𝒩̃` is injective (resp. surjective, bijective) by
(2.7.2), the question being local on `Y`, and in view of `(I, 1.3.9)`; when `u` is (TN)-bijective, we also say that `u`
is a _(TN)-isomorphism_.

**Proposition.**

<!-- label: II.3.4.3 -->

Let `Y` be a prescheme, `𝒮` a quasi-coherent graded `𝒪_Y`-algebra generated by `𝒮_1`, with `𝒮_1` assumed of finite type.
Let `ℳ` be a quasi-coherent graded `𝒮`-module.

1. If `ℳ` satisfies (TF), then `ℳ̃` is of finite type.
1. Suppose `ℳ` satisfies (TF); for `ℳ̃ = 0`, it is necessary and sufficient that `ℳ` satisfy (TN).

**Proof.** The questions being local on `Y`, we reduce to the case `Y` affine with ring `A`, `𝒮 = S̃` with `S` a graded
`A`-algebra such that the ideal `S_+` is of finite type, and `ℳ = M̃` with `M` a graded `S`-module; the proposition then
follows from (2.7.3).

**Theorem.**

<!-- label: II.3.4.4 -->

Let `Y` be a prescheme, `𝒮` a quasi-coherent graded `𝒪_Y`-algebra generated by `𝒮_1`, with `𝒮_1` assumed of finite type;
let `X = Proj(𝒮)`. For every quasi-coherent `𝒪_X`-module `ℱ`, the canonical homomorphism `β` (3.3.4) is an isomorphism.

**Proof.** First, `β` is defined by virtue of (3.4.1). To see that `β` is an isomorphism, we reduce to the case `Y`
affine with ring `A`, `𝒮 = S̃` with `S` a graded `A`-algebra generated by `S_1`, and `S_1` an `A`-module of finite type.
It then suffices to apply (2.7.5).

**Corollary.**

<!-- label: II.3.4.5 -->

Under the hypotheses of (3.4.4), every quasi-coherent `𝒪_X`-module `ℱ` is isomorphic to an `𝒪_X`-module of the form
`ℳ̃`, where `ℳ` is a quasi-coherent graded `𝒮`-module. If furthermore `ℱ` is of finite type, and if we assume that `Y`
is a quasi-compact scheme or that the underlying space of `Y` is Noetherian, then we may take `ℳ` to be of finite type.

<!-- original page 60 -->

**Proof.** The first assertion follows at once from (3.4.4) by taking `ℳ = Γ_*(ℱ)`. To establish the second, it suffices
to show that `ℳ` is the inductive limit of its _graded_ sub-`𝒮`-modules of finite type `𝒩_λ`: indeed, it will follow
that `ℳ̃` is the inductive limit of the `𝒩̃_λ` (3.2.4), hence `ℱ` is the inductive limit of the `β(𝒩̃_λ)`; since `X` is
quasi-compact ((3.4.1) and `(I, 6.3.1)`) and `ℱ` is of finite type, `ℱ` will necessarily equal one of the `β(𝒩̃_λ)`
`(0, 5.2.3)`.

To define the `𝒩_λ` having `ℳ` as inductive limit, it suffices to consider, for each `n ∈ ℤ`, the quasi-coherent
`𝒪_Y`-module `ℳ_n`, which is the inductive limit of its sub-`𝒪_Y`-modules `ℳ_n^{(μ_n)}` of finite type, by the
hypothesis on `Y` `(I, 9.4.9)`; one sees at once that `𝒫_{μ_n} = 𝒮 · ℳ_n^{(μ_n)}` is a graded `𝒮`-module of finite type,
and that taking the `𝒩_λ` to be the finite sums of `𝒮`-modules of the form `𝒫_{μ_n}` gives the desired objects.

**Corollary.**

<!-- label: II.3.4.6 -->

Suppose the hypotheses of (3.4.4) are satisfied and, moreover, that the underlying space of `Y` is quasi-compact; let
`ℱ` be a quasi-coherent `𝒪_X`-module of finite type. Then there exists `n_0` such that for every `n ≥ n_0` the canonical
homomorphism `σ : p*(p_*(ℱ(n))) → ℱ(n)` `(0, 4.4.3)` is surjective.

**Proof.** For every `y ∈ Y`, let `U` be an affine open neighbourhood of `y` in `Y`. There exists an integer `n_0(U)`
such that, for `n ≥ n_0(U)`, `ℱ(n)|p⁻¹(U)` is generated by finitely many of its sections over `p⁻¹(U)` (2.7.9); but
these sections are the canonical images of sections of `p*(p_*(ℱ(n)))` over `p⁻¹(U)` (`(0, 3.7.1)` and `(0, 4.4.3)`), so
`ℱ(n)|p⁻¹(U)` equals the canonical image of `p*(p_*(ℱ(n)))|p⁻¹(U)`. Finally, since `Y` is quasi-compact, there is a
finite cover of `Y` by affine opens `U_i`, and taking `n_0` to be the largest of the `n_0(U_i)` finishes the proof.

**Remarks.**

<!-- label: II.3.4.7 -->

If `p = (ψ, θ) : X → Y` is a morphism of ringed spaces and `ℱ` an `𝒪_X`-module, then the fact that the canonical
homomorphism `σ : p*(p_*(ℱ)) → ℱ` is surjective can be made explicit as follows `(0, 4.4.1)`: for every `x ∈ X` and
every section `s` of `ℱ` over an open neighbourhood `V` of `x`, there exist an open neighbourhood `U` of `p(x)` in `Y`,
finitely many sections `t_i` (`1 ≤ i ≤ m`) of `ℱ` over `p⁻¹(U)`, a neighbourhood `W ⊂ V ∩ p⁻¹(U)` of `x`, and sections
`a_i` (`1 ≤ i ≤ m`) of `𝒪_X` over `W` such that

```text
  s|W = ∑_{i=1}^m a_i · (t_i|W).
```

When `Y` is an _affine scheme_ and `p_*(ℱ)` is _quasi-coherent_, this condition is equivalent to `ℱ` being _generated by
its sections over `X`_ `(0, 5.5.1)`: indeed, if `Y = Spec(A)`, we may suppose `U = D(f)` with `f ∈ A`; then there exist
an integer `n > 0` and sections `s_i` of `ℱ` over `X` such that `t_i` is the restriction to `p⁻¹(U)` of `s_i g^n`, with
`g = θ(f)` (by applying `(I, 1.4.1)` to `p_*(ℱ)`); since `g` is invertible over `p⁻¹(U)`, we have

```text
  s|W = ∑_i b_i · (s_i|W)
```

with `b_i = a_i (g|W)^{−n}`, whence the claim. When `Y` is affine, corollary (3.4.6) thus recovers (2.7.9).

We thus conclude that, when `Y` is an arbitrary prescheme, the following three conditions on a quasi-coherent
`𝒪_X`-module `ℱ` such that `p_*(ℱ)` is

<!-- original page 61 -->

quasi-coherent are equivalent:

- a) _The canonical homomorphism `σ : p*(p_*(ℱ)) → ℱ` is surjective._
- b) _There exists a quasi-coherent `𝒪_Y`-module `𝒢` and a surjective homomorphism `p*(𝒢) → ℱ`._
- c) _For every affine open `U` of `Y`, `ℱ|p⁻¹(U)` is generated by its sections over `p⁻¹(U)`._

We have just shown the equivalence of a) and c). On the other hand, it is clear that a) implies b), `p_*(ℱ)` being
quasi-coherent by hypothesis. Conversely, every homomorphism `u : p*(𝒢) → ℱ` factors as `p*(𝒢) → p*(p_*(ℱ)) ─σ→ ℱ`
`(0, 3.5.4.4)`, so if `u` is surjective so is `σ`, which shows that b) implies a).

**Corollary.**

<!-- label: II.3.4.8 -->

Suppose the hypotheses of (3.4.4) are satisfied, and further that `Y` is a quasi-compact scheme or that the underlying
space of `Y` is Noetherian. Let `ℱ` be a quasi-coherent `𝒪_X`-module of finite type; then there exists an integer `n_0`
such that for every `n ≥ n_0`, `ℱ` is isomorphic to a quotient of an `𝒪_X`-module of the form `(p*(𝒢))(−n)`, where `𝒢`
is a quasi-coherent `𝒪_Y`-module of finite type (depending on `n`).

**Proof.** Since the structure morphism `X → Y` is separated and of finite type, `p_*(ℱ(n))` is quasi-coherent
(`(I, 9.2.2, b)`), hence the inductive limit of its quasi-coherent sub-`𝒪_Y`-modules of finite type, by the hypothesis
on `Y` `(I, 9.4.9)`. We thus deduce from (3.4.6), `(0, 4.3.2)`, and `(0, 5.2.3)` that `ℱ(n)` is the canonical image of
an `𝒪_X`-module of the form `p*(𝒢)`, where `𝒢` is a quasi-coherent sub-`𝒪_Y`-module of `p_*(ℱ(n))` of finite type; the
corollary follows from (3.2.5.2) and (3.2.7.1).

## 3.5. Functorial behaviour

**(3.5.1)**

<!-- label: II.3.5.1 -->

Let `Y` be a prescheme, `𝒮`, `𝒮'` two quasi-coherent positively-graded `𝒪_Y`-algebras; set `X = Proj(𝒮)`,
`X' = Proj(𝒮')`, and let `p`, `p'` be the structure morphisms of `X` and `X'` into `Y`. Let `φ : 𝒮' → 𝒮` be an
`𝒪_Y`-homomorphism of graded algebras. For every affine open `U` of `Y`, set `S_U = Γ(U, 𝒮)`, `S'_U = Γ(U, 𝒮')`; the
homomorphism `φ` defines a homomorphism `φ_U : S'_U → S_U` of graded `A_U`-algebras, where `A_U = Γ(U, 𝒪_Y)`. There
corresponds in `p⁻¹(U)` an open subset `G(φ_U)` and a morphism `Φ_U : G(φ_U) → p'⁻¹(U)` (2.8.1). Furthermore, if `V ⊂ U`
is an affine open, the diagram

```text
              φ_U
   S'_U ───────────→ S_U                                                  (3.5.1.1)
     │                │
     ↓                ↓
   S'_V ───────────→ S_V
              φ_V
```

commutes, and one checks at once from the definitions (2.8.1) that

```text
  G(φ_V) = G(φ_U) ∩ p⁻¹(V)
```

and that `Φ_V` is the restriction of `Φ_U` to `G(φ_V)`. We have thus defined an open subset `G(φ)` of `X` such that
`G(φ) ∩ p⁻¹(U) = G(φ_U)` for every affine open `U ⊂ Y`, and an affine `Y`-morphism `Φ : G(φ) → X'`, which we say is

<!-- original page 62 -->

_associated_ to `φ` and which we denote by `Proj(φ)`. When, for every `y ∈ Y`, there is an affine neighbourhood `U` of
`y` such that the `Γ(U, 𝒪_Y)`-module `Γ(U, 𝒮_+)` is generated by `φ(Γ(U, 𝒮'_+))`, then `G(φ_U) = p⁻¹(U)`, and so
`G(φ) = X`.

**Proposition.**

<!-- label: II.3.5.2 -->

1. If `ℳ` is a quasi-coherent graded `𝒮`-module, there is a canonical functorial isomorphism from the `𝒪_{X'}`-module
    `(ℳ_{[φ]})̃` to the `𝒪_{X'}`-module `Φ_*(ℳ̃|G(φ))`.
1. If `ℳ'` is a quasi-coherent graded `𝒮'`-module, there is a canonical functorial homomorphism `ν` from the
    `(𝒪_X|G(φ))`-module `Φ*(ℳ̃')` to the `(𝒪_X|G(φ))`-module `(ℳ' ⊗_{𝒮'} 𝒮)̃|G(φ)`. If `𝒮'` is generated by `𝒮'_1`,
    then `ν` is an isomorphism.

**Proof.** The homomorphisms considered have already been defined when `Y` is affine ((2.8.7) and (2.8.8)); in the
general case, it suffices to check that they are compatible with restriction from an affine open of `Y` to a smaller
one, which follows at once from the commutativity of (3.5.1.1).

In particular, for every `n ∈ ℤ`, we have a canonical homomorphism

```text
  Φ*(𝒪_{X'}(n)) → 𝒪_X(n)|G(φ).                                           (3.5.2.1)
```

**Proposition.**

<!-- label: II.3.5.3 -->

Let `Y`, `Y'` be two preschemes, `ψ : Y' → Y` a morphism, and `𝒮` a quasi-coherent graded `𝒪_Y`-algebra; set
`𝒮' = ψ*(𝒮)`. Then the `Y'`-scheme `X' = Proj(𝒮')` is canonically identified with `Proj(𝒮) ×_Y Y'`. Furthermore, if `ℳ`
is a quasi-coherent graded `𝒮`-module, then the `𝒪_{X'}`-module `(ψ*(ℳ))̃` is identified with `ℳ̃ ⊗_Y 𝒪_{Y'}`.

**Proof.** First note that `ψ*(𝒮)` and `ψ*(ℳ)` are quasi-coherent `𝒪_{Y'}`-modules, as are their homogeneous components
`(0, 5.1.4)`. Let `U` be an affine open of `Y`, `U' ⊂ ψ⁻¹(U)` an affine open of `Y'`, `A`, `A'` the rings of `U`, `U'`;
then `𝒮|U = S̃`, with `S` a graded `A`-algebra, and `𝒮'|U'` is identified with `(S ⊗_A A')̃` `(I, 1.6.5)`; the first
assertion then follows from (2.8.10) and `(I, 3.2.6.2)`, since one verifies at once that the projection
`Proj(𝒮'|U') → Proj(𝒮|U)` defined by the above identification is compatible with restriction on `U` and `U'` and so
defines a morphism `Proj(𝒮') → Proj(𝒮)`. Now let

```text
  q  : Proj(𝒮) → Y,    q' : Proj(𝒮') → Y'
```

be the structure morphisms; `q'⁻¹(U')` is then identified with `q⁻¹(U) ×_U U'`, and the two sheaves `(ψ*(ℳ))̃|q'⁻¹(U')`
and `(ℳ̃ ⊗_Y 𝒪_{Y'})|q'⁻¹(U')` are then both canonically identified with `(M ⊗_A A')̃`, where `M = Γ(U, ℳ)`, by (2.8.10)
and `(I, 1.6.5)`; whence the second assertion, the compatibility of the above identifications with restriction again
being immediate.

**Corollary.**

<!-- label: II.3.5.4 -->

With the notation of (3.5.3), `𝒪_{X'}(n)` is canonically identified with `𝒪_X(n) ⊗_Y 𝒪_{Y'}` for every `n ∈ ℤ` (with
`X = Proj(𝒮)`).

**Proof.** Indeed, with the notation of (3.5.3), it is clear that `ψ*(𝒮(n)) = 𝒮'(n)` for every `n ∈ ℤ`.

**(3.5.5)**

<!-- label: II.3.5.5 -->

Keeping the previous notation, denote by `Ψ` the canonical projection `X' → X`, and set `ℳ' = ψ*(ℳ)`; we further suppose
that `𝒮` is generated by `𝒮_1`

<!-- original page 63 -->

and that `X` is of finite type over `Y`; it then follows that `𝒮'` is generated by `𝒮'_1` (as one sees by reducing to
the case `Y` and `Y'` affine) and that `X'` is of finite type over `Y'` `(I, 6.3.4)`. Let `ℱ` be an `𝒪_X`-module and set
`ℱ' = Ψ*(ℱ)`; it then follows from (3.5.4) and `(0, 4.3.3)` that `ℱ'(n) = Ψ*(ℱ(n))` for every `n ∈ ℤ`. We further define
a canonical `Ψ`-homomorphism `θ_n : q_*(ℱ(n)) → q'_*(ℱ'(n))` as follows: in view of the commutativity of the diagram

```text
                  Ψ
   X ←───────── X'
   │             │
 q │             │ q'
   ↓             ↓
   Y ←───────── Y'
                  ψ
```

it suffices to define a homomorphism `q_*(ℱ(n)) → ψ_*(q'_*(Ψ*(ℱ(n)))) = q_*(Ψ_*(Ψ*(ℱ(n))))`, and we take the
homomorphism `θ_n = q_*(ρ_n)`, with `ρ_n` the canonical homomorphism `ℱ(n) → Ψ_*(Ψ*(ℱ(n)))` `(0, 4.4.3)`. It is
immediate that for every affine open `U` of `Y` and every affine open `U'` of `Y'` with `U' ⊂ ψ⁻¹(U)`, the homomorphism
`θ_n` gives, on sections, the canonical homomorphism `(0, 3.7.2)` `Γ(q⁻¹(U), ℱ(n)) → Γ(q'⁻¹(U'), ℱ'(n))`.

The commutativity of (2.8.13.2) then shows that if `ℱ` is quasi-coherent, the diagram

```text
                      ρ
              ℱ ─────────→ ℱ'
              ↑               ↑
       β_ℱ    │               │  β_ℱ'
              │               │
        (Γ_*(ℱ))̃ ─────→ (Γ_*(ℱ'))̃
                      θ̃
```

commutes (the top horizontal arrow being the canonical `Ψ`-morphism `ℱ → Ψ*(ℱ)`).

Similarly, the commutativity of (2.8.13.1) shows that the diagram

```text
                      θ
   Γ_*(ℳ̃) ─────────→ Γ_*(ℳ̃')
       ↑                 ↑
 α_ℳ   │                 │  α_ℳ'
       │                 │
       ℳ ─────────────→ ℳ'
                  ρ
```

commutes (the bottom horizontal arrow being the canonical `ψ`-morphism `ℳ → ψ*(ℳ)`).

**(3.5.6)**

<!-- label: II.3.5.6 -->

Now consider two preschemes `Y`, `Y'`, a morphism `g : Y' → Y`, a quasi-coherent graded `𝒪_Y`-algebra (resp.
`𝒪_{Y'}`-algebra) `𝒮` (resp. `𝒮'`), and a `g`-morphism of graded algebras `u : 𝒮 → 𝒮'` — that is, an `𝒪_Y`-homomorphism
of graded algebras `𝒮 → g_*(𝒮')`; we already know this is equivalent to giving an `𝒪_{Y'}`-homomorphism of graded
algebras `u♯ : g*(𝒮) → 𝒮'`. From `u♯` we canonically obtain a `Y'`-morphism `W = Proj(u♯) : G(u♯) → Proj(g*(𝒮))`, where
`G(u♯)` is an open subset of `X' = Proj(𝒮')` (3.5.1). On the other hand, `X'' = Proj(g*(𝒮))` is canonically

<!-- original page 64 -->

identified with `X ×_Y Y'`, with `X = Proj(𝒮)` (3.5.3); composing the first projection `p : X ×_Y Y' → X` with
`Proj(u♯)`, we obtain a morphism `v : G(u♯) → X`, which we denote by `Proj(u)`, and such that the diagram

```text
              v
   G(u♯) ─────→ X
     │           │
     ↓           ↓
     Y' ─────→ Y
              g
```

commutes.

Furthermore, for every quasi-coherent graded `𝒪_Y`-module `ℳ`, we have a canonical `v`-morphism

```text
  ν : ℳ̃ → (g*(ℳ) ⊗_{g*(𝒮)} 𝒮')̃|G(u♯).                                   (3.5.6.1)
```

Indeed, `ν♯` is obtained by composing the homomorphisms

```text
  v*(ℳ̃) = w*(p*(ℳ̃)) → w*((g*(ℳ))̃) → (g*(ℳ) ⊗_{g*(𝒮)} 𝒮')̃|G(u♯)
```

where the first arrow comes from the isomorphism (3.5.3) and the second is the homomorphism (3.5.2, (i)); when `𝒮` is
generated by `𝒮_1`, it follows from (3.5.2) that `ν♯` is an isomorphism.

As a particular case of (3.5.6.1), we have, for every `n ∈ ℤ`, a canonical `v`-morphism

```text
  ν : 𝒪_X(n) → 𝒪_{X'}(n)|G(u♯).                                          (3.5.6.2)
```

## 3.6. Closed subpreschemes of a prescheme `Proj(𝒮)`

**(3.6.1)**

<!-- label: II.3.6.1 -->

Let `Y` be a prescheme, `φ : 𝒮 → 𝒮'` a degree-`0` homomorphism of quasi-coherent graded `𝒪_Y`-algebras. We say that `φ`
is _(TN)-surjective_ (resp. _(TN)-injective_, _(TN)-bijective_) if there exists `n` such that, for every `k ≥ n`,
`φ_k : 𝒮_k → 𝒮'_k` is surjective (resp. injective, bijective). When this is the case, the study of the corresponding
morphism `Φ : Proj(𝒮') → Proj(𝒮)` reduces to the case where `φ` is surjective (resp. injective, bijective). This is
shown as in (2.9.1) (which is the particular case `Y` affine) using (3.1.8). Instead of saying that `φ` is
(TN)-bijective, we also say that it is a _(TN)-isomorphism_.

**Proposition.**

<!-- label: II.3.6.2 -->

Let `Y` be a prescheme, `𝒮` a quasi-coherent graded `𝒪_Y`-algebra, and `X = Proj(𝒮)`.

1. If `φ : 𝒮 → 𝒮'` is a (TN)-surjective homomorphism of graded `𝒪_Y`-algebras, then the corresponding morphism
    `Φ = Proj(φ)` (3.5.1) is defined on all of `Proj(𝒮')` and is a closed immersion of `Proj(𝒮')` into `X`. If `𝒥` is
    the kernel of `φ`, then the closed subprescheme of `X` associated to `Φ` is defined by the quasi-coherent sheaf of
    ideals `𝒥̃` of `𝒪_X`.
1. Suppose further that `𝒮_0 = 𝒪_Y`, that `𝒮` is generated by `𝒮_1`, and that `𝒮_1` is of finite type. Let `X'` be a
    closed subprescheme of `X = Proj(𝒮)` defined by a quasi-coherent sheaf of ideals `ℐ` of `𝒪_X`. Let `𝒥` be

<!-- original page 65 -->

```
the quasi-coherent graded sheaf of ideals of `𝒮` given by the inverse image of
`Γ_*(ℐ)` under the canonical homomorphism `α : 𝒮 → Γ_*(𝒪_X)` (3.3.2), and set
`𝒮' = 𝒮/𝒥`. Then `X'` is the subprescheme associated `(I, 4.2.1)` to the
closed immersion `Proj(𝒮') → X` corresponding to the canonical homomorphism
`𝒮 → 𝒮'` of graded `𝒪_Y`-algebras.
```

**Proof.**

(i) We may assume `φ` is surjective (3.6.1). Then, for every affine open `U` of `Y`, `Γ(U, 𝒮) → Γ(U, 𝒮')` is surjective
`(I, 1.3.9)`, so (3.5.1) `G(φ) = X`. We reduce immediately to proving the proposition when `Y` is affine, where it
follows from (2.9.2, (i)).

(ii) We reduce to proving that the homomorphism `𝒥̃ → 𝒪_X` deduced from the canonical injection `𝒥 → 𝒮` is an
isomorphism from `𝒥̃` onto `ℐ`; since the question is local on `Y`, we may take `Y` affine with ring `A`, so `𝒮 = S̃`
with `S` a graded `A`-algebra generated by `S_1`, with `S_1` of finite type over `A`. It then suffices to apply (2.9.2,
(ii)).

**Corollary.**

<!-- label: II.3.6.3 -->

Under the conditions of (3.6.2, (i)), suppose further that `𝒮` is generated by `𝒮_1`. Then `Φ*(𝒪_X(n))` is canonically
identified with `𝒪_{X'}(n)` for every `n ∈ ℤ`.

**Proof.** We defined such a canonical isomorphism when `Y` is affine (2.9.3); in the general case, it suffices to check
that the isomorphisms so defined for each affine open `U` of `Y` are compatible with passage from `U` to an affine open
`U' ⊂ U`, which is immediate.

**Corollary.**

<!-- label: II.3.6.4 -->

Let `Y` be a prescheme, `𝒮` a quasi-coherent graded `𝒪_Y`-algebra generated by `𝒮_1`, `ℰ` a quasi-coherent `𝒪_Y`-module,
`u` a surjective `𝒪_Y`-homomorphism `ℰ → 𝒮_1`, and `ū : 𝕊_{𝒪_Y}(ℰ) → 𝒮` the homomorphism of graded `𝒪_Y`-algebras
extending `u` (1.7.4). Then the morphism corresponding to `ū` is a closed immersion of `Proj(𝒮)` into
`Proj(𝕊_{𝒪_Y}(ℰ))`.

**Proof.** Indeed, `ū` is surjective by hypothesis, and we apply (3.6.1, (i)).

## 3.7. Morphisms from a prescheme to a homogeneous spectrum

**(3.7.1)**

<!-- label: II.3.7.1 -->

Let `q : X → Y` be a morphism of preschemes, `ℒ` an invertible `𝒪_X`-module, and `𝒮` a quasi-coherent positively-graded
`𝒪_Y`-algebra; then `q*(𝒮)` is a quasi-coherent positively-graded `𝒪_X`-algebra. Consider the quasi-coherent graded
`𝒪_X`-algebra `𝒮' = ⊕_{n ≥ 0} ℒ^{⊗ n}` and suppose given an `𝒪_X`-homomorphism of graded algebras

```text
  ψ : q*(𝒮) → 𝒮' = ⊕_{n ≥ 0} ℒ^{⊗ n}
```

which is equivalent to giving a `q`-morphism of graded algebras

```text
  ψ♭ : 𝒮 → q_*(𝒮').
```

We know that `Proj(𝒮')` is canonically identified with `X` ((3.1.7) and (3.1.8, (iii))); we canonically obtain from `ψ`
an open subset `G(ψ)` of `X` and a `Y`-morphism

```text
  r_{ℒ, ψ} : G(ψ) → Proj(𝒮) = P                                          (3.7.1.1)
```

<!-- original page 66 -->

which we call the morphism _associated to_ `ℒ` and `ψ`; recall (3.5.6) that this morphism is obtained by composing the
`Y`-morphism

```text
  τ = Proj(ψ) : G(ψ) → Proj(q*(𝒮))
```

with the first projection `π : Proj(q*(𝒮)) = P ×_Y X → P`.

**(3.7.2)**

<!-- label: II.3.7.2 -->

We make `r = r_{ℒ, ψ}` explicit when `Y = Spec(A)` is affine, so `𝒮 = S̃` with `S` a positively-graded `A`-algebra.
Suppose first that `X = Spec(B)` is also affine and that `ℒ = L̃`, with `L` a free `B`-module of rank `1`. Then
`q*(𝒮) = (S ⊗_A B)̃` `(I, 1.6.5)`; if `c` is a generator of `L`, then `ψ_n : q*(𝒮_n) → ℒ^{⊗ n}` corresponds to a
homomorphism `w_n : s ⊗ b ↦ b v_n(s) c^{⊗ n}` from `S_n ⊗_A B` to `L^{⊗ n}`, where `v_n : S_n → B` is a homomorphism of
`A`-modules, the `v_n` forming a homomorphism of algebras `S → B`. Let `f ∈ S_d` (`d > 0`) and set `g = v_d(f)`; we have
`π⁻¹(D_+(f)) = D_+(f ⊗ 1)` by (2.8.10) and the identification of `D_+(f)` with `Spec(S_{(f)})` (2.3.6); furthermore, by
formula (2.8.1.1) (in view of the canonical identification of `X` with `Proj(𝒮')`),

```text
  τ⁻¹(D_+(f ⊗ 1)) = D(g)
```

whence

```text
  r⁻¹(D_+(f)) = D(g).                                                    (3.7.2.1)
```

Moreover, the morphism `τ = Proj(ψ)`, restricted to `D(g)`, corresponds to the homomorphism that sends
`(s ⊗ 1)/(f ⊗ 1)^n` (for `s ∈ S_{nd}`) to `v_{nd}(s)/g^n` (2.8.1), and the projection `π`, restricted to `D_+(f ⊗ 1)`,
corresponds to the homomorphism `s/f^n ↦ (s ⊗ 1)/(f ⊗ 1)^n`; we conclude that `r`, restricted to `D(g)`, corresponds to
the homomorphism of `A`-algebras `ω : S_{(f)} → B_g` such that `ω(s/f^n) = v_{nd}(s)/g^n` (for `s ∈ S_{nd}`, `n > 0`).
Passing to the case where `X` is arbitrary (still with `Y` affine), and taking (2.8.1) into account, we obtain:

**Proposition.**

<!-- label: II.3.7.3 -->

If `Y = Spec(A)` is affine and `𝒮 = S̃`, with `S` a graded `A`-algebra, then for every `f ∈ S_d = Γ(Y, 𝒮_d)`,

```text
  r_{ℒ, ψ}⁻¹(D_+(f)) = X_{ψ♭(f)}     (where ψ♭(f) ∈ Γ(X, ℒ^{⊗ d}))       (3.7.3.1)
```

and the restriction `X_{ψ♭(f)} → D_+(f) = Spec(S_{(f)})` of `r_{ℒ, ψ}` corresponds `(I, 2.2.4)` to the homomorphism of
algebras

```text
  ψ♭_{(f)} : S_{(f)} → Γ(X_{ψ♭(f)}, 𝒪_X)                                 (3.7.3.2)
```

such that, for `s ∈ S_{nd} = Γ(Y, 𝒮_{nd})`,

```text
  ψ♭_{(f)}(s/f^n) = (ψ♭(s)|X_{ψ♭(f)}) · (ψ♭(f)|X_{ψ♭(f)})^{−n}.          (3.7.3.3)
```

We say that `r_{ℒ, ψ}` is _everywhere defined_ if `G(ψ) = X`. For this it is clearly necessary and sufficient that
`G(ψ) ∩ q⁻¹(U) = q⁻¹(U)` for every affine open `U ⊂ Y`; in other words, the question is local on `Y`. If `Y` is affine,
`G(ψ)` is the union of the `r⁻¹(D_+(f))` for `f` homogeneous in `S_+` (2.8.1); by (3.7.3.1), the `X_{ψ♭(f)}` must
therefore form a covering of `X`; in other words:

**Corollary.**

<!-- label: II.3.7.4 -->

Under the hypotheses of (3.7.3), for `r_{ℒ, ψ}` to be everywhere defined it is necessary and sufficient that, for every
`x ∈ X`, there exist an integer `n > 0` and a section `s` of `𝒮_n` over `Y` such that, setting
`t = ψ♭(s) ∈ Γ(X, ℒ^{⊗ n})`, we have `t(x) ≠ 0`.

<!-- original page 67 -->

Note that this condition is always satisfied if `ψ` is (TN)-surjective.

Similarly, whether `r_{ℒ, ψ}` is dominant is a local question on `Y`, and we have:

**Corollary.**

<!-- label: II.3.7.5 -->

Under the hypotheses of (3.7.3), for `r_{ℒ, ψ}` to be dominant it is necessary and sufficient that, for every integer
`n > 0`, every section `s ∈ S_n` such that `ψ♭(s) ∈ Γ(X, ℒ^{⊗ n})` is locally nilpotent be itself nilpotent.

**Proof.** We must express that `r_{ℒ, ψ}⁻¹(D_+(s))` is non-empty only if `D_+(s)` is non-empty, and the corollary
follows from (3.7.3.1) and (2.3.7).

**Proposition.**

<!-- label: II.3.7.6 -->

Let `q : X → Y` be a morphism, `ℒ` an invertible `𝒪_X`-module, `𝒮`, `𝒮'` two quasi-coherent graded `𝒪_Y`-algebras,
`u : 𝒮' → 𝒮` a homomorphism of graded algebras, `ψ : q*(𝒮) → ⊕_{n ≥ 0} ℒ^{⊗ n}` a homomorphism of graded algebras, and
`ψ' = ψ ∘ q*(u)` the composite. If `r_{ℒ, ψ'}` is everywhere defined, so is `r_{ℒ, ψ}`; if `u` is (TN)-surjective and
`r_{ℒ, ψ'}` is dominant, then so is `r_{ℒ, ψ}`; conversely, if `u` is (TN)-injective and `r_{ℒ, ψ}` is dominant, then
`r_{ℒ, ψ'}` is dominant.

**Proof.** We have `G(ψ') ⊂ G(ψ)` (2.8.4), whence the first assertion; if `u` is (TN)-surjective, then
`Proj(u) : Proj(𝒮) → Proj(𝒮')` is everywhere defined and is a closed immersion; since `r_{ℒ, ψ'}` is the composition of
`Proj(u)` with the restriction of `r_{ℒ, ψ}` to `G(ψ')`, we conclude that if `r_{ℒ, ψ'}` is dominant so is `r_{ℒ, ψ}`.
Finally, if `u` is (TN)-injective, we know that `Proj(u)` is a dominant morphism from `G(u)` to `Proj(𝒮')` (2.8.3);
since `G(ψ')` is the inverse image of `G(u)` under `r_{ℒ, ψ}`, we see that if `r_{ℒ, ψ}` is dominant so is `r_{ℒ, ψ'}`.

**Proposition.**

<!-- label: II.3.7.7 -->

Let `Y` be a quasi-compact prescheme, `q : X → Y` a quasi-compact morphism, `ℒ` an invertible `𝒪_X`-module, `𝒮` a
quasi-coherent graded `𝒪_Y`-algebra given as the filtered inductive limit of an inductive system `(𝒮^λ)` of
quasi-coherent `𝒪_Y`-algebras. Let `φ_λ : 𝒮^λ → 𝒮` be the canonical homomorphism, `ψ : q*(𝒮) → ⊕_{n ≥ 0} ℒ^{⊗ n}` a
homomorphism of graded algebras, and set `ψ_λ = ψ ∘ q*(φ_λ)`. For `r_{ℒ, ψ}` to be everywhere defined it is necessary
and sufficient that there exist `λ` such that `r_{ℒ, ψ_λ}` is everywhere defined; `r_{ℒ, ψ_μ}` is then everywhere
defined for every `μ ≥ λ`.

**Proof.** The condition is sufficient by (3.7.6). Conversely, suppose `r_{ℒ, ψ}` is everywhere defined; we may reduce
to `Y` affine, since if for every affine open `U ⊂ Y` there exists `λ(U)` such that the restriction of `r_{ℒ, ψ_{λ(U)}}`
to `q⁻¹(U)` is everywhere defined, it suffices (`Y` being quasi-compact) to cover `Y` by finitely many affine opens
`U_i` and to take `λ ≥ λ(U_i)` for all `i`, by (3.7.6). If `Y` is affine, the hypothesis implies that, for every
`x ∈ X`, there is a section `s^{(x)}` of some `S_n` such that, setting `t^{(x)} = ψ♭(s^{(x)})`, we have `t^{(x)}(x) ≠ 0`
(with `t^{(x)}` considered as a section of `ℒ^{⊗ n}` over `X`), which implies that `t^{(x)}(z) ≠ 0` for every `z` in
some neighbourhood `V(x)` of `x`. Cover `X` by finitely many `V(x_i)` and let `s^{(i)}` be the corresponding sections of
`S`; then there exists `λ` such that all the `s^{(i)}` are of the form `φ_λ(s'^{(i)}_λ)`, with `s'^{(i)}_λ ∈ S^λ` for
every `i`; it then follows from (3.7.4) that `r_{ℒ, ψ_λ}` is everywhere defined. The last assertion is a trivial
consequence of (3.7.6).

**Corollary.**

<!-- label: II.3.7.8 -->

Under the hypotheses of (3.7.7), if the `r_{ℒ, ψ_λ}` are dominant, so is `r_{ℒ, ψ}`; the converse holds if the `φ_λ` are
injective.

<!-- original page 68 -->

**Proof.** The second assertion is a particular case of (3.7.6); to show that `r_{ℒ, ψ}` is dominant, we may restrict to
`Y` affine; if `s ∈ S` is such that `ψ♭(s)` is locally nilpotent, since we can write `s = φ_λ(s_λ)` for at least one
`λ`, we conclude from the hypothesis and (3.7.5) that `s_λ` is nilpotent, hence so is `s`, and the criterion of (3.7.5)
applies.

**Remarks.**

<!-- label: II.3.7.9 -->

(i) With the notation of (3.7.1), and taking (3.2.10) into account, we have, for every `n ∈ ℤ`, a canonical homomorphism

```text
  θ : r_{ℒ, ψ}*(𝒪_P(n)) → ℒ^{⊗ n}                                        (3.7.9.1)
```

defined in general in (3.5.6.2). One sees at once that under the conditions of (3.7.3), the restriction of this
homomorphism to `X_{ψ♭(f)}` sends `s/f^k` (with `s ∈ S_{n+kd}`) to the element
`(ψ♭(s)|X_{ψ♭(f)}) · (ψ♭(f)|X_{ψ♭(f)})^{−k}`.

(ii) Let `ℱ` be a quasi-coherent `𝒪_X`-module, and suppose `q` is quasi-compact and separated, so that for every
`n ≥ 0`, `q_*(ℱ ⊗ ℒ^{⊗ n})` is a quasi-coherent `𝒪_Y`-module `(I, 9.2.2)`. Let `ℳ' = ⊕_{n ≥ 0} ℱ ⊗ ℒ^{⊗ n}`, which is a
quasi-coherent graded `𝒮'`-module, and consider its image `ℳ = q_*(ℳ') = ⊕_{n ≥ 0} q_*(ℱ ⊗ ℒ^{⊗ n})` (which is a
quasi-coherent `𝒮`-module, via the homomorphism `ψ♭`). We are going to show the existence of a canonical homomorphism of
`𝒪_X`-modules

```text
  ξ : r_{ℒ, ψ}*(ℳ̃) → ℱ|G(ψ).                                            (3.7.9.2)
```

Indeed, we have already defined (3.5.6.1) a canonical homomorphism

```text
  r_{ℒ, ψ}*(ℳ̃) → (q*(ℳ) ⊗_{q*(𝒮)} 𝒮')̃|G(ψ)                              (3.7.9.3)
```

where the right-hand side is regarded as a quasi-coherent sheaf on `Proj(𝒮')`. We also have a canonical homomorphism

```text
  q*(q_*(ℳ')) ⊗_{q*(𝒮)} 𝒮' → ℳ'                                         (3.7.9.4)
```

for every quasi-coherent graded `𝒮'`-module `ℳ'`: for every open `U` of `X`, every section `t'` of `q*(q_*(ℳ'_h))` over
`U`, and every section `b'` of `𝒮'_k` over `U`, we send `t' ⊗ b'` to the section `b' σ(t')` of `ℳ'_{h+k}`, where `σ(t')`
is the section of `ℳ'_h` over `U` corresponding canonically `(0, 4.4.3)` to `t'`. We thus obtain a canonical
homomorphism

```text
  (q*(q_*(ℳ')) ⊗_{q*(𝒮)} 𝒮')̃|G(ψ) → ℳ̃'|G(ψ)                             (3.7.9.5)
```

and since finally `ℳ̃'` is canonically identified with `ℱ` (3.2.9, (i)), we obtain the desired canonical homomorphism.

Under the conditions of (3.7.3), the restriction of this homomorphism to `X_{ψ♭(f)}` is made explicit as follows: given
a section `t_{nd}` of `ℱ ⊗ ℒ^{⊗ nd}` over `X`, if `t'_{nd}` is `t_{nd}` viewed as a section of `q_*(ℱ ⊗ ℒ^{⊗ n})` over
`Y`, then `t'_{nd}/f^n` is sent to the section `(t_{nd}|X_{ψ♭(f)}) · (ψ♭(f)|X_{ψ♭(f)})^{−n}` of `ℱ` over `X_{ψ♭(f)}`.

## 3.8. Criteria for immersion into a homogeneous spectrum

<!-- original page 69 -->

**(3.8.1)**

<!-- label: II.3.8.1 -->

With the notation of (3.7.1), whether `r_{ℒ, ψ}` is an immersion (resp. an open immersion, a closed immersion) is
clearly _local on `Y`_.

**Proposition.**

<!-- label: II.3.8.2 -->

Under the hypotheses of (3.7.3), for `r_{ℒ, ψ}` to be everywhere defined and an immersion, it is necessary and
sufficient that there exist a family of sections `s_α ∈ S_{n_α}` (with `n_α > 0`) such that, setting `f_α = ψ♭(s_α)`,
the following conditions are satisfied:

1. The `X_{f_α}` form a covering of `X`.
1. The `X_{f_α}` are affine opens.
1. For every `α` and every `t ∈ Γ(X_{f_α}, 𝒪_X)`, there exist an integer `m > 0` and an `s ∈ S_{m n_α}` such that
    `t = (ψ♭(s)|X_{f_α}) · (f_α|X_{f_α})^{−m}`.

For `r_{ℒ, ψ}` to be everywhere defined and an open immersion, it is necessary and sufficient that there exist a family
`(s_α)` satisfying (i), (ii), (iii) and:

- (iv) For every `n > 0` and every `s ∈ S_{n n_α}` such that `ψ♭(s)|X_{f_α} = 0`, there exists an integer `k > 0` such
    that `s_α^k s = 0`.

For `r_{ℒ, ψ}` to be everywhere defined and a closed immersion, it is necessary and sufficient that there exist a family
`(s_α)` satisfying (i), (ii), (iii) and:

- (v) The `D_+(s_α)` form a covering of `P = Proj(𝒮)`.

**Proof.** For `r` to be an immersion (resp. a closed immersion), it is necessary and sufficient that there exist a
covering of `r(G(ψ))` (resp. of `P`) by the `D_+(s_α)` such that, setting `V_α = r⁻¹(D_+(s_α))`, the restriction of `r`
to `V_α` is a closed immersion of `V_α` into `D_+(s_α)` `(I, 4.2.4)`. Condition (i) expresses both that `r` is
everywhere defined and that the `D_+(s_α)` cover `r(X)`, by (3.7.3.1); since `D_+(s_α)` is affine, conditions (ii) and
(iii) express that the restriction of `r` to `X_{f_α}` is a closed immersion into `D_+(s_α)`, by `(I, 4.2.3)`; finally,
since (iii) and (iv) express that `ψ♭_{(s_α)}` is bijective (notation of (3.7.3.2)), conditions (ii), (iii), and (iv)
express that the restriction of `r` to `X_{f_α}` is an isomorphism onto `D_+(s_α)` for every `α`, so (i), (ii), (iii),
and (iv) together express that `r` is an open immersion.

**Corollary.**

<!-- label: II.3.8.3 -->

Under the hypotheses of (3.7.6), if `r_{ℒ, ψ'}` is everywhere defined and an immersion, so is `r_{ℒ, ψ}`. If we further
suppose `u` is (TN)-surjective, then if `r_{ℒ, ψ'}` is an open (resp. closed) immersion, so is `r_{ℒ, ψ}`.

**Proof.** By (3.8.2), there is a family `s'_α ∈ S'_{n_α}` such that, setting `f_α = ψ'♭(s'_α)`, conditions (i), (ii),
(iii) are satisfied. Setting `s_α = u(s'_α)`, we also have `f_α = ψ♭(s_α)`, and if
`t = (ψ'♭(s')|X_{f_α}) · (f_α|X_{f_α})^{−m}`, then also `t = (ψ♭(s)|X_{f_α}) · (f_α|X_{f_α})^{−m}` on setting
`s = u(s')`, whence the first assertion. The second follows at once from the fact that `Proj(u)` is a closed immersion.

**Proposition.**

<!-- label: II.3.8.4 -->

Suppose the hypotheses of (3.7.7) are satisfied and, in addition, that `q : X → Y` is a morphism of finite type. Then,
for `r_{ℒ, ψ}` to be everywhere defined and an immersion, it is necessary and sufficient that there exist `λ` such that
`r_{ℒ, ψ_λ}` is everywhere defined and an immersion; in this case `r_{ℒ, ψ_μ}` is everywhere defined and an immersion
for every `μ ≥ λ`.

<!-- original page 70 -->

**Proof.** In view of (3.8.3), it suffices to show that if `r_{ℒ, ψ}` is everywhere defined and an immersion, then so is
`r_{ℒ, ψ_λ}` for at least one `λ`. By the same argument as in (3.7.7), using the quasi-compactness of `Y`, we first
reduce to `Y` affine. Since `X` is quasi-compact, (3.8.2) shows the existence of a finite family `(s_i)` of elements of
`S` (`s_i ∈ S_{n_i}`) satisfying (i), (ii), (iii). The morphism `X_{f_i} → Y` (where `f_i = ψ♭(s_i)`) is of finite type:
indeed, it is a morphism of affine schemes, so it is quasi-compact `(I, 6.6.1)`, and locally of finite type since `q` is
of finite type `(I, 6.3.2)`, and the conclusion follows from `(I, 6.6.3)`. The ring `B_i` of `X_{f_i}` is therefore an
`A`-algebra of finite type `(I, 6.3.3)`; let `(t_{ij})` be a family of generators of this algebra. By hypothesis, there
are elements `s'_{ij} ∈ S_{m_{ij} n_i}` such that

```text
  t_{ij} = (ψ♭(s'_{ij})|X_{f_i}) · (ψ♭(s_i)|X_{f_i})^{−m_{ij}}.
```

Also by hypothesis, there exist `λ` and elements `s_{iλ} ∈ S^λ_{n_i}`, `s'_{ijλ} ∈ S^λ_{m_{ij} n_i}` whose images under
`φ_λ` are `s_i` and `s'_{ij}` respectively; it is clear that `r_{ℒ, ψ_λ}` satisfies conditions (i), (ii), and (iii) of
(3.8.2).

**Proposition.**

<!-- label: II.3.8.5 -->

Let `Y` be a quasi-compact scheme, or a prescheme whose underlying space is Noetherian, `q : X → Y` a morphism _of
finite type_, `ℒ` an invertible `𝒪_X`-module, `𝒮` a quasi-coherent graded `𝒪_Y`-algebra, and
`ψ : q*(𝒮) → ⊕_{n ≥ 0} ℒ^{⊗ n}` a homomorphism of graded algebras. For `r_{ℒ, ψ}` to be everywhere defined and an
immersion, it is necessary and sufficient that there exist an integer `n > 0` and a quasi-coherent sub-`𝒪_Y`-module of
finite type `ℰ` of `𝒮_n` such that

- a) the homomorphism `ψ_n ∘ q*(j_n) : q*(ℰ) → ℒ^{⊗ n}` (where `j_n : ℰ → 𝒮` is the canonical injection) is surjective;
- b) if `𝒮'` denotes the (graded) sub-`𝒪_Y`-algebra of `𝒮` generated by `ℰ`, and `ψ'` the homomorphism `ψ ∘ q*(j')`
    (with `j'` the injection of `𝒮'` into `𝒮`), then `r_{ℒ, ψ'}` is everywhere defined and an immersion.

When this is the case, every quasi-coherent sub-`𝒪_Y`-module `ℰ'` of `𝒮_n` containing `ℰ` has the same property, as does
the image of `⊗^k ℰ` in `𝒮_{kn}` for every `k > 0`.

**Proof.** The sufficiency of the condition and the last two assertions are particular cases of (3.8.3), in view of the
canonical isomorphism between `Proj(𝒮)` and `Proj(𝒮^{(k)})` (3.1.8).

Let `(U_i)` be a finite cover of `Y` by affine opens and set `A_i = A(U_i)`. Since `q⁻¹(U_i)` is quasi-compact, the
hypothesis that `r_{ℒ, ψ}` be everywhere defined and an immersion implies, together with (3.8.2), the existence of a
finite family `(s_{ij} ∈ S^{(i)}_{n_{ij}})` of elements of `S^{(i)} = Γ(U_i, 𝒮)` satisfying (i), (ii), (iii). As in the
proof of (3.8.4), one sees that the morphism `X_{f_{ij}} → U_i` (where `f_{ij} = ψ♭(s_{ij})`) is of finite type, and so
the ring `B_{ij}` of `X_{f_{ij}}` is an `A_i`-algebra of finite type, with a system of generators of the form
`(ψ♭(t_{ijk})|X_{f_{ij}}) · (f_{ij}|X_{f_{ij}})^{−m_{ijk}}`, where `t_{ijk} ∈ S^{(i)}_{m_{ijk} n_{ij}}`. Let `n` be a
common multiple of the `m_{ijk} n_{ij}`; replacing (for each `(i, j, k)`) `s_{ij}` by a power `s_{ij}^ρ` such that
`ρ m_{ijk} n_{ij} = n`, and multiplying `t_{ijk}` by `s_{ij}^{ρ − m_{ijk}}`, we may assume that for each `i` all the
`s_{ij}` and `t_{ijk}` belong to `S^{(i)}_n` and that `m_{ijk} = 1`. Let `E_i` be the sub-`A_i`-module of `S^{(i)}_n`
generated by these elements (for fixed `i`). There exists a coherent sub-`𝒪_Y`-module of finite type `ℰ_i` of `𝒮_n` such
that `ℰ_i|U_i = (E_i)̃` `(I, 9.4.7)`.

<!-- original page 71 -->

It is clear that the sub-`𝒪_Y`-module `ℰ` of `𝒮_n` given by the sum of the `ℰ_i` solves the problem (each section
`f_{ij}` is such that, for every `x ∈ X_{f_{ij}}`, there is an affine neighbourhood `V ⊂ X_{f_{ij}}` of `x` such that
`f|V` is a basis for `Γ(V, ℒ^{⊗ n})`).

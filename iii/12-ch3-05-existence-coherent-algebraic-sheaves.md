# §5. An existence theorem for coherent algebraic sheaves

<!-- original page 149 -->

## 5.1. Statement of the theorem

**(5.1.1)**

<!-- label: III.5.1.1 -->

Let `A` be an *adic Noetherian* ring, `𝔍` an ideal of definition of `A`, so that `A` is separated and complete for the
`𝔍`-adic topology. If `Y = Spec(A)`, the affine formal scheme `Spf(A)` is identified with the completion `Ŷ` of `Y`
along the closed subset `Y' = V(𝔍)` `(I, 10.10.1)`. Let `X` be a (usual) `Y`-prescheme of finite type, `f : X → Y` the
structure morphism; we shall denote by `𝔛` the completion of `X` along the closed subset `X' = f⁻¹(Y')`, or equivalently
the `Ŷ`-formal prescheme `X ×_Y Ŷ`; by `f̂ : 𝔛 → Ŷ` the extension of `f` to the completions; finally, for every coherent
`𝒪_X`-module `ℱ`, we shall denote by `𝓕̂` its completion `ℱ_{/X'}`, which is a coherent `𝒪_𝔛`-module.

**Proposition (5.1.2).**

<!-- label: III.5.1.2 -->

*The hypotheses and notation being those of (5.1.1), let `ℱ` be a coherent `𝒪_X`-module whose support is proper over `Y`
`(II, 5.4.10)`. The canonical homomorphisms (4.1.4)*

```text
  ρ_i : H^i(X, ℱ) → H^i(𝔛, 𝓕̂)
```

*are then isomorphisms.*

**Proof.** Since `H^i(X, ℱ)` is an `A`-module of finite type (3.2.4), hence identical to its Hausdorff completion for
the `𝔍`-preadic topology `(0_I, 7.3.6)`, the proposition is only a particular case of (4.1.10).

Recall that the canonical isomorphisms `ρ_i` commute with the coboundaries for every exact sequence
`0 → ℱ' → ℱ → ℱ'' → 0` of coherent `𝒪_X`-modules (`(0, 12.1.6)` and `(I, 10.8.9)`).

**Corollary (5.1.3).**

<!-- label: III.5.1.3 -->

*Let `ℱ`, `𝒢` be two coherent `𝒪_X`-modules such that the intersection of their supports is proper over `Y`. Then the
canonical homomorphism*

```text
  Hom_{𝒪_X}(ℱ, 𝒢) → Hom_{𝒪_𝔛}(𝓕̂, 𝓖̂)                                          (5.1.3.1)
```

*which associates to every homomorphism `u : ℱ → 𝒢` its completion `û : 𝓕̂ → 𝓖̂`, is an isomorphism. Moreover, when the
morphism `f` is closed, in order that `û` be injective (resp. surjective) it is necessary and sufficient that `u` be
so.*

**Proof.** The first assertion is a particular case of (4.5.3), again due to the fact that the first member of (5.1.3.1)
is an `A`-module of finite type, hence identical to its Hausdorff completion. To prove the second, note by virtue of
`(I, 10.8.14)` that `û` is injective (resp. surjective) if and only if there exists a neighbourhood of `X'` in which `u`
is injective (resp. surjective).

<!-- original page 150 -->

The conclusion therefore follows from the following lemma:

**Lemma (5.1.3.1).**

<!-- label: III.5.1.3.1 -->

*Under the hypotheses of (5.1.1), if one assumes in addition that the morphism `f` is closed, then every neighbourhood
of `X'` in `X` is identical to `X`.*

**Proof.** First, we may reduce to the case where `f(X) = Y`. Indeed, by hypothesis, `f(X)` is a closed subset `Z` of
`Y`; we may in addition replace `f` by `f_{red}` `(I, 6.3.4)`, and suppose consequently `X` and `Y` reduced; we may then
replace `Y` by the reduced closed subprescheme of `Y` with `Z` as underlying space `(I, 5.2.2)`, since every ideal of
`A` is closed, and every quotient ring of `A` is therefore adic and Noetherian. One then has `f(X') = Y'`; if `V` is an
open neighbourhood of `X'` in `X`, `f(X − V)` is closed in `Y` by hypothesis, and does not meet `Y'`; but this is
impossible unless `X − V` is empty, since `𝔍` is contained in the radical of `A` `(I, 1.1.15` and `0_I, 7.1.10)`, whence
the conclusion.

When one restricts to coherent `𝒪_X`-modules whose support is proper over `Y`, (5.1.3) can be stated, in the language of
categories, by saying that the functor `ℱ ↦ 𝓕̂` is *fully faithful* from the category of `𝒪_X`-modules of the preceding
type into the category of coherent `𝒪_𝔛`-modules, and consequently establishes an *equivalence* of the first of these
categories with a *full* subcategory of the second `(0, 8.1.6)`. The existence theorem will prove that when `X` is
proper over `Y`, this subcategory is in fact the category of *all* coherent `𝒪_𝔛`-modules. More precisely:

**Theorem (5.1.4).**

<!-- label: III.5.1.4 -->

*Let `A` be an adic Noetherian ring, `Y = Spec(A)`, `𝔍` an ideal of definition of `A`, `Y' = V(𝔍)`, `f : X → Y` a
separated morphism of finite type, `X' = f⁻¹(Y')`. Let `Ŷ = Y_{/Y'} = Spf(A)`, `𝔛 = X_{/X'}` be the completions of `Y`
and `X` along `Y'` and `X'`, `f̂ : 𝔛 → Ŷ` the extension of `f` to the completions; then the functor `ℱ ↦ 𝓕̂ = ℱ_{/X'}`
is an equivalence of the category of coherent `𝒪_X`-modules of support proper over `Spec(A)` with the category of
coherent `𝒪_𝔛`-modules of support proper over `Spf(A)`.*

In other words, taking (5.1.3) into account:

**Corollary (5.1.5).**

<!-- label: III.5.1.5 -->

*For an `𝒪_𝔛`-module to be isomorphic to the completion of an `𝒪_X`-module which is coherent and of support proper over
`Spec(A)`, it is necessary and sufficient that it be coherent and of support proper over `Spf(A)`.*

The most important case is the:

**Corollary (5.1.6).**

<!-- label: III.5.1.6 -->

*Suppose `X` proper over `Y = Spec(A)`. Then the functor `ℱ ↦ 𝓕̂` is an equivalence of the category of coherent
`𝒪_X`-modules and of the category of coherent `𝒪_𝔛`-modules.*

**Scholium (5.1.7).**

<!-- label: III.5.1.7 -->

If one takes into account the characterization of coherent sheaves on formal preschemes `(I, 10.11.3)`, one sees that
under the conditions of (5.1.1), the data of a coherent `𝒪_𝔛`-module of support proper over `Spec(A)` is equivalent (on
setting `Y_n = Spec(A/𝔍^{n+1})` and `X_n = X ×_Y Y_n`) to the data of a projective system of coherent `𝒪_{X_n}`-modules
`(𝓕_n)` such that for `m ≤ n` one has `𝓕_m = 𝓕_n ⊗_{𝒪_{Y_n}} 𝒪_{Y_m}` (or equivalently `𝓕_m = 𝓕_n / 𝔍^{m+1} 𝓕_n`) and
that the support of `𝓕_0` is a part of `X_0` proper over `Y_0`. By means of `(I, 10.11.4)`, one likewise interprets
homomorphisms of coherent `𝒪_𝔛`-modules as homomorphisms of projective systems of coherent `𝒪_{X_n}`-modules.

<!-- original page 151 -->

In all known cases of application, `A` is in fact an *adic local Noetherian* ring, so the `Y_n` are spectra of *artinian
local rings*, and the results of this section and the preceding ones reduce in large measure algebraic geometry over an
adic local Noetherian ring to algebraic geometry over artinian local rings.

**Corollary (5.1.8).**

<!-- label: III.5.1.8 -->

*Under the conditions of (5.1.4), the map `Z ↦ Ẑ = Z_{/(Z ∩ X')}` is a bijection of the set of closed subpreschemes `Z`
of `X`, proper over `Y`, onto the set of closed formal subpreschemes of `𝔛`, proper over `Ŷ`.*

**Proof.** Indeed, a closed formal subprescheme of `𝔛` is of the form `(𝔗, (𝒪_𝔛/𝒜) | 𝔗)`, where `𝒜` is a coherent Ideal
of `𝒪_𝔛` `(I, 10.14.2)`; if `𝔗` is proper over `Ŷ`, it follows from (5.1.4) that `𝒪_𝔛 / 𝒜` is isomorphic to an
`𝒪_𝔛`-module of the form `𝓕̂`, where `ℱ` is a coherent `𝒪_X`-module of support proper over `Y`; in addition, it follows
from (5.1.3) that the canonical homomorphism `𝒪_𝔛 → 𝒪_𝔛/𝒜` is of the form `û`, where `u : 𝒪_X → ℱ` is a *surjective*
homomorphism of `𝒪_X`-modules. Hence `ℱ` is of the form `𝒪_X / 𝒩`, where `𝒩` is a coherent Ideal of `𝒪_X`, and `𝒜 = 𝒩̂`
`(I, 10.8.8)`, whence the conclusion `(I, 10.14.7)`.

## 5.2. Proof of the existence theorem: projective and quasi-projective cases

**(5.2.1)**

<!-- label: III.5.2.1 -->

Under the conditions of (5.1.4), we shall say *provisionally* that a coherent `𝒪_𝔛`-module is *algebraizable* if it is
isomorphic to a completion `𝓕̂` of a coherent `𝒪_X`-module `ℱ` of support proper over `Y`.

**Lemma (5.2.2).**

<!-- label: III.5.2.2 -->

*Let `𝓕'`, `𝓖'` be two algebraizable `𝒪_𝔛`-modules. For every homomorphism `u : 𝓕' → 𝓖'`, `Ker(u)`, `Im(u)` and
`Coker(u)` are algebraizable.*

**Proof.** Indeed, if `𝓕' = 𝓕̂`, `𝓖' = 𝓖̂`, where `ℱ` and `𝒢` are coherent `𝒪_X`-modules of supports proper over `Y`,
one has `u = v̂`, where `v : ℱ → 𝒢` is a homomorphism (5.1.3). By virtue of the exactness of the functor `ℱ ↦ 𝓕̂`,
`Ker(u)` is isomorphic to `(Ker(v))̂`, and since the support of `Ker(v)` is contained in that of `ℱ`, one sees that
`Ker(u)` is algebraizable; analogous proof for `Im(u)` and `Coker(u)`.

**Proposition (5.2.3).**

<!-- label: III.5.2.3 -->

*Let `A` be an adic Noetherian ring, `𝔍` an ideal of definition of `A`, `𝔜 = Spf(A)`, `f : 𝔛 → 𝔜` a proper morphism of
formal preschemes. Set `Y_k = Spec(A/𝔍^{k+1})`, `X_k = 𝔛 ×_𝔜 Y_k`, and for every `𝒪_𝔛`-module `𝓕`,
`𝓕_k = 𝓕 ⊗_{𝒪_𝔛} 𝒪_{X_k} = 𝓕 / 𝔍^{k+1} 𝓕`. Let `ℒ` be an invertible `𝒪_𝔛`-module, and suppose that `ℒ_0 = ℒ/𝔍ℒ` is an
ample `𝒪_{X_0}`-module; for every `𝒪_𝔛`-module `𝓕` and every integer `n`, set `𝓕(n) = 𝓕 ⊗ ℒ^{⊗n}`. Then, for every
coherent `𝒪_𝔛`-module `𝓕`, there exists an integer `n_0` such that, for every `n ≥ n_0`, the following properties hold:*

*(i) The canonical homomorphism `H^0(𝔛, 𝓕(n)) → H^0(𝔛, 𝓕_k(n))` is surjective for every `k ≥ 0`.*

*(ii) One has `H^q(𝔛, 𝓕(n)) = 0` for every `q > 0`.*

**Proof.** We know that the underlying spaces of `𝔛` and `X_0` are the same; the sheaves `ℳ_k = 𝔍^k 𝓕 / 𝔍^{k+1} 𝓕`,
being annihilated by `𝔍`, may be considered as coherent `𝒪_{X_0}`-modules `(0_I, 5.3.10)`; in addition, if one sets
`ℳ_k(n) = ℳ_k ⊗_{𝒪_{X_0}} ℒ_0^{⊗n}`, one sees at once that `ℳ_k(n) = 𝔍^k 𝓕(n) / 𝔍^{k+1} 𝓕(n)`. Note that, since `ℒ_0` is
ample for `f_0 : X_0 → Y_0`, and

<!-- original page 152 -->

`f_0` is proper, we conclude that `f_0` is *projective* `(II, 5.5.4)`. Let `𝒮 = ⊕_{k ≥ 0} 𝔍^k / 𝔍^{k+1}` be the graded
`A`-algebra associated to the `𝔍`-adic filtration of `A`, which is of finite type since `A` is Noetherian; if one sets
`𝒮' = f_0^*(𝒮̃)`, `𝒮'` is a quasi-coherent `𝒪_{X_0}`-algebra of finite type, and `ℳ = ⊕_{k ≥ 0} ℳ_k` a graded
quasi-coherent `𝒮'`-module of finite type (since `𝓕_0` is coherent and generates the `𝒮'`-module `ℳ`). We are therefore
in the conditions of application of theorem (2.4.1, (ii)), and we conclude that there exists `n_0` such that, for
`n ≥ n_0` and for every `k`, one has

```text
  H^q(X_0, ℳ_k(n)) = 0           for every q > 0.                              (5.2.3.1)
```

One therefore also has `H^q(𝔛, ℳ_k(n)) = 0` for `q > 0` and `n ≥ n_0`, `ℳ_k(n)` being this time considered as
`𝒪_𝔛`-module. Applying the exact cohomology sequence to

```text
  0 → 𝔍^h 𝓕(n) / 𝔍^{k+1} 𝓕(n) → 𝔍^h 𝓕(n) / 𝔍^k 𝓕(n) →
                                              𝔍^k 𝓕(n) / 𝔍^{k+1} 𝓕(n) → 0,
```

one deduces first that for `0 ≤ h < k`, `n ≥ n_0` and `q > 0`, one has, by induction on `k − h`,

```text
  H^q(𝔛, 𝔍^h 𝓕(n) / 𝔍^k 𝓕(n)) = 0                                              (5.2.3.2)
```

and in particular for `h = 0`,

```text
  H^q(𝔛, 𝓕_k(n)) = 0           for n ≥ n_0, k ≥ 0 and q > 0.                   (5.2.3.3)
```

Another portion of the exact cohomology sequence, for `h = 0`, gives the exact sequence

```text
  H^0(𝔛, 𝓕_{k+1}(n)) → H^0(𝔛, 𝓕_k(n)) → H^1(𝔛, 𝔍^k 𝓕(n) / 𝔍^{k+1} 𝓕(n)) = 0,   (5.2.3.4)
```

whence one deduces that for `h ≤ k`, the canonical map

```text
  H^0(𝔛, 𝓕_{k+1}(n)) → H^0(𝔛, 𝓕_h(n))                                          (5.2.3.5)
```

is surjective. For every `q`, the projective system `(H^q(𝔛, 𝓕_k(n)))_{k ≥ 0}` therefore satisfies condition `(ML)` for
`n ≥ n_0`. Moreover, every formal affine open `U` of `𝔛` is also an affine open in each of the `X_k` `(I, 10.5.2)`,
hence one has `H^q(U, 𝓕_k(n)) = 0` for every `q > 0` (1.3.1), and `H^0(U, 𝓕_{k+1}(n)) → H^0(U, 𝓕_k(n))` is surjective
for `h ≤ k` `(I, 1.3.9)`. The conditions of application of `(0_III, 13.3.1)` are consequently fulfilled, and we conclude
that, for `n ≥ n_0`:

1° For every `q > 0`, `H^q(𝔛, 𝓕(n)) → lim_← H^q(𝔛, 𝓕_k(n))` is bijective, hence, by virtue of (5.2.3.3),
`H^q(𝔛, 𝓕(n)) = 0`.

2° The homomorphism `H^0(𝔛, 𝓕(n)) → lim_← H^0(𝔛, 𝓕_k(n))` is bijective; moreover, since the homomorphisms (5.2.3.5) are
surjective, so is each of the homomorphisms

```text
  lim_← H^0(𝔛, 𝓕_k(n)) → H^0(𝔛, 𝓕_h(n)),
```

which completes the proof.

**Corollary (5.2.4).**

<!-- label: III.5.2.4 -->

*The hypotheses being those of (5.2.3), for every coherent `𝒪_𝔛`-module `𝓕`, there exists an integer `N` such that for
`n ≥ N`, `𝓕(n)` is generated by its sections above*

<!-- original page 153 -->

*`𝔛`; in other words, `𝓕` is isomorphic to the quotient of an `𝒪_𝔛`-module of the form `(ℒ^{⊗(−n)})^h`.*

**Proof.** Since `X_0` is Noetherian, it follows from the hypothesis on `ℒ_0` and from `(II, 4.5.5)` that there exists
`n_0` such that, for `n ≥ n_0`, `𝓕_0(n)` is generated by its sections above `X_0`; moreover, one may suppose `n_0`
chosen large enough that the homomorphism `Γ(𝔛, 𝓕(n)) → Γ(X_0, 𝓕_0(n))` is surjective for `n ≥ n_0` (5.2.3). There thus
exists a finite number of sections `s_i ∈ Γ(𝔛, 𝓕(n))` whose images in `Γ(X_0, 𝓕_0(n))` generate `𝓕_0(n)` `(0_I, 5.2.3)`.
Since `𝔍` is contained in the maximal ideal of the local ring at every point of `𝔛`, it follows from Nakayama's lemma,
applied to these local rings, that the `s_i` generate `𝓕(n)` `(0_I, 5.1.1)`.

**(5.2.5) Proof of the existence theorem: projective case.**

<!-- label: III.5.2.5 -->

The notation being that of (5.1.4), suppose `f` *projective*, so that there exists an ample `𝒪_X`-module `ℒ`
`(I, 5.5.4)`. By definition, `X_n = X ×_Y Y_n` is equal to the closed subprescheme `X_n ×_Y Y_n = f⁻¹(Y_n)` of `X`; if
`ℒ'` is the completion `ℒ ⊗_{𝒪_X} 𝒪_𝔛` of `ℒ`, one has `ℒ'_0 = ℒ / 𝔍ℒ`, considered as `𝒪_{X_0}`-module; one knows that
`ℒ'_0` is ample `(II, 4.6.13, (i bis))`. One may therefore apply to `ℒ'` and to every coherent `𝒪_𝔛`-module `𝓕`
Corollary (5.2.4); one sees thus that `𝓕` is isomorphic to a quotient of `𝓖 = (ℒ'^{⊗(−n)})^k` for suitable integers
`n > 0` and `k > 0`. Now, it is clear that `𝓖` is the completion of `(ℒ^{⊗(−n)})^k` `(I, 10.8.10)`, and is therefore
algebraizable. Next consider the canonical surjective homomorphism `u : 𝓖 → 𝓕`, and let `ℋ = Ker(u)`, which is a
coherent `𝒪_𝔛`-module `(0_I, 5.3.4)`. One sees in the same way that there exists an algebraizable `𝒪_𝔛`-module `𝒦` and a
homomorphism `v : 𝒦 → 𝓖` such that `ℋ = Im(v)`. One then has `𝓕 = Coker(v)`, and `𝓕` is algebraizable by virtue of
(5.2.2).

**(5.2.6) Proof of the existence theorem: quasi-projective case.**

<!-- label: III.5.2.6 -->

The notation being still that of (5.1.4), suppose now that `f` is *quasi-projective*. Then there exists a projective
morphism `g : Z → Y` such that `X` is identified with the `Y`-prescheme induced on an open subset of `Z` `(II, 5.3.2)`;
if one sets `Z' = g⁻¹(Y')`, one has `X' = X ∩ Z'`. Consequently, the completion `𝔛 = X_{/X'}` is identified with the
formal prescheme induced by the completion `𝔍 = Z_{/Z'}` on the open subset `X ∩ Z'` of `𝔍` `(I, 10.8.5)`. Let `𝓕` be a
coherent `𝒪_𝔛`-module whose support `T'` is proper over `Ŷ`; this means by definition that there exists a closed
subprescheme of `X'`, having `T' ⊂ X'` as underlying space, such that the restriction `T' → Y'` of `f` is proper; it
follows that `T'` is proper over `Y`, hence *closed* in `Z'` `(II, 5.4.10)`. It follows that `𝓕` is the sheaf induced on
`𝔛` by the `𝒪_𝔍`-module `𝓕'` obtained by glueing of `𝓕` (defined on the open subset `𝔛` of `𝔍`) and the sheaf `0` on the
open subset `𝔍 − T'` of `𝔍`, these two sheaves coinciding on the intersection open subset `𝔛 − T'`. It is clear that
`𝓕'` is coherent; by virtue of (5.2.5), there exists a coherent `𝒪_Z`-module `𝒢` such that `𝓕' = 𝓖̂`; let `T` be the
support of `𝒢`, so that `T' = T ∩ Z'` `(I, 10.8.12)`. If `h` is the restriction of `g` to the reduced closed
subprescheme of `Z` having `T` as underlying space, one then has `T' = h⁻¹(Y') = T ∩ g⁻¹(Y')`, and consequently `X ∩ T`
is an open subset of `T` containing `T'`.

<!-- original page 154 -->

Since `h` is proper `(II, 5.4.2)`, hence closed, it follows from (5.1.3.1) that `X ∩ T = T`; in other words `T ⊂ X`, and
since `T` is closed in `Z`, `T` is proper over `Y`. If `ℱ` is the sheaf induced on `X` by `𝒢`, its completion `𝓕̂` is
induced on `𝔛` by `𝓖̂` `(I, 10.8.4)`, hence is equal to `𝓕'`, which completes the proof.

## 5.3. Proof of the existence theorem: general case

**Lemma (5.3.1).**

<!-- label: III.5.3.1 -->

*Under the conditions of (5.1.4), if `0 → ℋ → 𝓕 → 𝒢 → 0` is an exact sequence of coherent `𝒪_𝔛`-modules such that `𝒢`
and `ℋ` are algebraizable, then `𝓕` is algebraizable.*

**Proof.** Indeed, suppose `𝒢 = 𝓑̂`, `ℋ = 𝓒̂`, where `𝓑` and `𝓒` are coherent `𝒪_X`-modules with supports proper over
`Y`; `𝓕` canonically defines an element of the `A`-module `Ext^1_{𝒪_𝔛}(𝔛; 𝓑̂, 𝓒̂)` `(0, 12.3.2)`, and the hypotheses
imply that this `A`-module is canonically isomorphic to `Ext^1_{𝒪_X}(X; 𝓑, 𝓒)` (4.5.2); there thus exists an exact
sequence `0 → 𝓒 → 𝒜 → 𝓑 → 0` of coherent `𝒪_X`-modules such that the canonical image of the element of
`Ext^1_{𝒪_X}(X; 𝓑, 𝓒)` corresponding to `𝒜` is the element of `Ext^1_{𝒪_𝔛}(𝔛; 𝓑̂, 𝓒̂)` corresponding to `𝓕`. But by
definition (taking `(I, 10.8.8, (ii))` into account), this means that `𝓕` is isomorphic to `𝓐̂`, whence the lemma, since
`Supp(𝒜)` is contained in the union of `Supp(𝓑)` and `Supp(𝓒)`, hence is proper over `Y`.

**Corollary (5.3.2).**

<!-- label: III.5.3.2 -->

*Under the conditions of (5.1.1), let `u : 𝓕 → 𝒢` be a homomorphism of coherent `𝒪_𝔛`-modules; if `𝒢`, `Ker(u)` and
`Coker(u)` are algebraizable, then so is `𝓕`.*

**Proof.** The lemma (5.2.2) applied to the homomorphism `𝒢 → Coker(u)` shows indeed that `Im(u)` is algebraizable, and
it then suffices to apply lemma (5.3.1) to the exact sequence `0 → Ker(u) → 𝓕 → Im(u) → 0`.

**Lemma (5.3.3).**

<!-- label: III.5.3.3 -->

*Under the conditions of (5.1.1), let `h : Z → Y` be a morphism of finite type, `𝔷 = Z_{/Z'}` the completion of `Z`
along `Z' = h⁻¹(Y')`, `g : Z → X` a proper `Y`-morphism, `ĝ : 𝔷 → 𝔛` its extension to the completions. For every
algebraizable `𝒪_𝔷`-module `𝓕'`, `ĝ_*(𝓕')` is an algebraizable `𝒪_𝔛`-module.*

**Proof.** Indeed, if `ℱ` is a coherent `𝒪_Z`-module such that `𝓕' = 𝓕̂`, it follows from the first comparison theorem
(4.1.5) that `ĝ_*(𝓕')` is isomorphic to the completion of `g_*(ℱ)`.

**Lemma (5.3.4).**

<!-- label: III.5.3.4 -->

*Let `X` be a (usual) Noetherian scheme, `X'` a closed subset of `X`, `f : Z → X` a proper morphism, `Z' = f⁻¹(X')`,
`𝔛 = X_{/X'}`, `𝔷 = Z_{/Z'}`, `f̂ : 𝔷 → 𝔛` the extension of `f` to the completions. Let `ℳ` be a coherent Ideal of `𝒪_X`
such that, if `U = X − Supp(𝒪_X / ℳ)`, the restriction `f⁻¹(U) → U` of `f` is an isomorphism. Then, for every coherent
`𝒪_𝔛`-module `𝓕`, there exists an integer `n > 0` such that the kernel and cokernel of the canonical homomorphism
`ρ_𝓕 : 𝓕 → f̂_*(f̂^*(𝓕))` `(0_I, 4.4.3)` are annihilated by `ℳ̂^n`.*

**Proof.** We may restrict to the case where `X = Spec(B)`, `B` a Noetherian ring, hence `X' = V(𝔎)`, where `𝔎` is an
ideal of `B`. We are going to see that one may reduce to the case where `B` is an *adic Noetherian* ring and `𝔎` an
ideal of definition of `B`. Indeed, let `B_1` be the Hausdorff completion of `B` for the `𝔎`-preadic topology; if
`𝔎_1 = 𝔎 B_1`, `B_1` is therefore an

<!-- original page 155 -->

adic Noetherian ring of which `𝔎_1` is an ideal of definition. Set `X_1 = Spec(B_1)` and let `h : X_1 → X` be the
morphism corresponding to the canonical homomorphism `B → B_1`; if `X'_1 = h⁻¹(X')`, one then has `X'_1 = V(𝔎_1)`. Set
finally `Z_1 = Z ×_X X_1 = Z_{(X_1)}`, `f_1 = f_{(X_1)} : Z_1 → X_1`, which is a proper morphism `(II, 5.4.2)`, and
denote by `𝔛_1` the completion of `X_1` along `X'_1`, by `𝔷_1 = Z_1 ×_X 𝔛_1` the completion of `Z_1` along
`Z'_1 = f_1⁻¹(X'_1)`, by `f̂_1` the extension of `f_1` to the completions. It is immediate that the extension
`ĥ : 𝔛_1 → 𝔛` of `h` to the completions is an isomorphism, corresponding to the identity map of `B_1` `(I, 10.9.1)`; one
concludes that the corresponding homomorphism `𝔷_1 → 𝔷` is also an isomorphism, these isomorphisms identifying `f̂_1`
and `f̂`. Finally, `ℳ_1 = h^*(ℳ)` is a coherent Ideal of `𝒪_{X_1}` and `Supp(𝒪_{X_1} / ℳ_1) = h⁻¹(Supp(𝒪_X / ℳ))`
`(I, 9.1.13)`, hence, if `U_1 = X_1 − Supp(𝒪_{X_1} / ℳ_1)`, one has `U_1 = h⁻¹(U)`, whence it follows at once that the
restriction `f_1⁻¹(U_1) → U_1` of `f_1` is an isomorphism `(I, 3.2.7)`; in addition, the completions `ℳ̂` and `ℳ̂_1` are
identified by `ĥ` `(I, 10.9.5)`. All hypotheses of (5.3.4) are therefore fulfilled by `X_1`, `X'_1`, `f_1` and `ℳ_1`,
and one may therefore from now on suppose `B` adic Noetherian and `𝔎` an ideal of definition of `B`. One then has
`𝔛 = Spf(B)`, and `𝓕 = N^Δ`, where `N` is a `B`-module of finite type, whence `𝓕 = 𝓖̂`, where `𝒢` is the coherent
`𝒪_X`-module `Ñ` `(I, 10.10.5)`, and consequently `f̂^*(𝓕) = (f^*(𝒢))̂` `(I, 10.9.5)`. In addition, by virtue of the
first comparison theorem (4.1.5), `f̂_*((f^*(𝒢))̂)` is canonically identified with `(f_*(f^*(𝒢)))̂`, and the canonical
homomorphism `ρ_𝓕` is none other than `ρ̂_𝒢` by virtue of (5.1.3). Now, the kernel `𝒫` and the cokernel `𝒬` of
`ρ_𝒢 : 𝒢 → f_*(f^*(𝒢))` are coherent `𝒪_X`-modules, and by hypothesis their restrictions to `U` are obviously zero.
There thus exists an integer `n > 0` such that `ℳ^n 𝒫 = ℳ^n 𝒬 = 0` `(I, 9.3.4)`; one concludes that
`ℳ̂^n 𝒫̂ = ℳ̂^n 𝒬̂ = 0` `(I, 10.8.8` and `10.8.10)`.

**5.3.5. End of the proof of the existence theorem.**

<!-- label: III.5.3.5 -->

The hypotheses being those of (5.1.4), we shall use the principle of Noetherian induction `(0_I, 2.2.2)`, supposing
therefore the theorem true for every closed subprescheme `T` of `X` whose underlying space is distinct from `X` (the
completion `𝔗` being of course the completion of `T` along `T ∩ X'`). We may suppose `X` non-empty. Since `f` is
separated and of finite type, we may apply Chow's lemma `(II, 5.6.1)`: there thus exists a `Y`-scheme `Z` and a
`Y`-morphism `g : Z → X` such that the structure morphism `h : Z → Y` is quasi-projective, the morphism `g` projective
and surjective, and in addition a non-empty open subset `U` of `X` such that the restriction `g⁻¹(U) → U` is an
isomorphism. Let `ℳ` be a coherent Ideal of `𝒪_X` defining a closed subprescheme of underlying space `X − U`
`(I, 5.2.2)`, and let `𝓕` be a coherent `𝒪_𝔛`-module whose support `E` is proper over `Y`; denote by `𝔷` the completion
of `Z` along `h⁻¹(Y')`, by `ĝ : 𝔷 → 𝔛` the extension of `g` to the completions. Then `ĝ^*(𝓕)` is a coherent `𝒪_𝔷`-module
whose support is contained in `g⁻¹(E)` and is consequently proper over `Y`, since `g` is projective, hence proper
`(II, 5.4.6)`. Since `h` is quasi-projective, `ĝ^*(𝓕)` is algebraizable by virtue of (5.2.6). We conclude

<!-- original page 156 -->

that `ĝ_*(ĝ^*(𝓕))` is an algebraizable `𝒪_𝔛`-module (5.3.3) since `g` is proper. We may now apply to `ℳ` and to `g` the
result of (5.3.4): the kernel `𝒫` and the cokernel `𝒬` of the homomorphism `ρ_𝓕 : 𝓕 → ĝ_*(ĝ^*(𝓕))` are annihilated by a
power `ℳ̂^n`; let `T` be the closed subprescheme of `X` defined by `ℳ^n`, having `X − U` as underlying space,
`j : T → X` the canonical injection, so that the extension to the completions `ĵ : 𝔗 → 𝔛` is the canonical injection
`(I, 10.14.7)`. One may therefore write `𝒫 = ĵ_*(ĵ^*(𝒫))` and `𝒬 = ĵ_*(ĵ^*(𝒬))`, and since `U` is non-empty, it follows
from the induction hypothesis that `ĵ^*(𝒫)` and `ĵ^*(𝒬)` are algebraizable `𝒪_𝔗`-modules; by virtue of (5.3.3), `𝒫` and
`𝒬` are algebraizable, and one may then apply (5.3.2), which finally proves that `𝓕` is algebraizable. Q.E.D.

## 5.4. Application: comparison of morphisms of usual schemes and of morphisms of formal schemes. Algebraizable formal schemes

**Theorem (5.4.1).**

<!-- label: III.5.4.1 -->

*Let `A` be an adic Noetherian ring, `𝔍` an ideal of definition of `A`, `S = Spec(A)`, `S' = V(𝔍)`. Let `u : X → S` be a
proper morphism, `v : Y → S` a separated morphism of finite type, and let `Ŝ`, `𝔛`, `𝔜` be the completions of `S`, `X`,
`Y` along `S'`, `u⁻¹(S')`, `v⁻¹(S')` respectively. If, for every `S`-morphism `f : X → Y`, `f̂ : 𝔛 → 𝔜` is the extension
of `f` to the completions, the map `f ↦ f̂` is a bijection*

```text
  Hom_S(X, Y) ⥲ Hom_Ŝ(𝔛, 𝔜).
```

**Proof.** Let us first show that `f ↦ f̂` is *injective*. Suppose indeed that two `S`-morphisms `f`, `g` from `X` to
`Y` are such that `f̂ = ĝ`. One then knows `(I, 10.9.4)` that there exists an open neighbourhood `V` of `X' = u⁻¹(S')`
in which `f` and `g` coincide. Now, since `u` is a closed map, one has `V = X` (5.1.3.1), whence `f = g`.

Let us now prove that `f ↦ f̂` is *surjective*, and let `h` therefore be an `Ŝ`-morphism `𝔛 → 𝔜`. Let `Z = X ×_S Y`, and
denote by `p : Z → X` and `q : Z → Y` the canonical projections; `Z` is of finite type over `S` `(I, 6.3.4)`, hence
Noetherian; denote by `𝔷` its completion along `Z' = p⁻¹(u⁻¹(S'))`; one knows that `𝔷` is canonically identified with
`𝔛 ×_Ŝ 𝔜`, the projections `𝔷 → 𝔛` and `𝔷 → 𝔜` being identified with the extensions `p̂` and `q̂` `(I, 10.9.7)`. Since
`Y` is separated over `S`, `𝔜` is separated over `Ŝ` `(I, 10.15.7)`, hence the graph morphism `Γ_h = (1_𝔛, h) : 𝔛 → 𝔷`
is a closed immersion `(I, 10.15.4)`. Let `𝔗` be the closed formal subprescheme of `𝔷` associated to this immersion, and
`j : 𝔗 → 𝔷` the canonical injection, so that `Γ_h = j ∘ w`, where `w : 𝔛 → 𝔗` is an isomorphism `(I, 10.14.3)` whose
inverse isomorphism is `p̂ ∘ j`; in addition, `𝔗` is obviously proper over `Ŝ`, since `𝔛` is; one concludes (5.1.8) that
there exists a closed subprescheme `T` of `Z` such that `𝔗 = T̂ = T_{/(T ∩ Z')}`, and that `j = î`, where `i` is the
canonical injection `T → Z` `(I, 10.14.7)`. Then `p ∘ i : T → X` is an isomorphism, since it is so for
`(p ∘ i)̂ = p̂ ∘ î` by hypothesis, and it suffices to apply

<!-- original page 157 -->

(4.6.8), noting as above that `S` is the only neighbourhood of `S'` in `S`. Let `g : X → T` be the inverse isomorphism
of `p ∘ i`, and set `f = q ∘ i ∘ g`, which is a morphism `X → Y` whose graph is by definition `Γ_f = i ∘ g`. Since `ĝ`
is the inverse isomorphism of `(p ∘ i)̂ = w`, one has `(Γ_f)̂ = î ∘ ĝ = j ∘ w = Γ_h`. But one knows that
`(Γ_f)̂ = Γ_{f̂}` `(I, 10.9.8)`, whence finally `h = f̂`, which completes the proof.

One may therefore say, in the language of categories, that the functor `X ↦ 𝔛` is *fully faithful* `(0, 8.1.6)` from the
category of proper schemes over `Spec(A)` into the category of proper formal schemes over `Spf(A)`, for every adic
Noetherian ring `A`; it consequently establishes an *equivalence* between the first of these categories and a
subcategory of the second; the objects of the latter will be called *algebraizable formal schemes*. For such a scheme
`𝔛`, there exists a usual scheme `X`, proper over `Spec(A)`, determined up to unique isomorphism, such that `𝔛` is
isomorphic to `X̂`.

**Scholium (5.4.2).**

<!-- label: III.5.4.2 -->

With the notation of (5.4.1), set `S_n = Spec(A/𝔍^{n+1})`, `X_n = X ×_S S_n`, `Y_n = Y ×_S S_n`. It follows from (5.4.1)
and from `(I, 10.12.3)` that to give an `S`-morphism `f : X → Y` is equivalent to giving an `(S_n)`-adic inductive
system `(I, 10.12.2)` of `S_n`-morphisms `f_n : X_n → Y_n`.

**Remark (5.4.3).**

<!-- label: III.5.4.3 -->

Contrary to what the existence theorem (5.1.6) might suggest, there exist formal schemes proper over `Spf(A)` that are
*not* algebraizable (just as there exist compact analytic spaces that do not come from complex algebraic varieties). We
shall later encounter such schemes in "moduli theory", which deals precisely (when the base field is `ℂ`) with the
infinitesimal variations of the complex structure of a complete algebraic variety, and it is known that such variations
may give rise to analytic varieties that are not algebraic.

**Proposition (5.4.4).**

<!-- label: III.5.4.4 -->

*Let `A` be an adic Noetherian ring, `𝔖 = Spf(A)`, `g : 𝔛 → 𝔖`, `h : 𝔜 → 𝔖` two proper morphisms of formal schemes,
`f : 𝔛 → 𝔜` an `𝔖`-morphism. If `f` is finite and if `𝔜` is algebraizable, then `𝔛` is algebraizable.*

**Proof.** Note that the hypotheses on `g` and `h` already entail that `f` is proper (3.4.1), and for `f` to be finite,
it suffices that for every `y ∈ 𝔜`, the fibre `f⁻¹(y)` is finite (4.8.11). The hypothesis entails that `𝓑 = f_*(𝒪_𝔛)` is
a coherent `𝒪_𝔜`-Algebra (4.8.6), hence it follows from the existence theorem that, if `𝔜 = Ŷ` and `h = ŵ`, where
`w : Y → Spec(A)` is a proper morphism of usual schemes, there exists a coherent `𝒪_Y`-Algebra `𝒞` such that `𝓑 = 𝒞̂`.
Let `X = Spec(𝒞)`, and `u : X → Y` the structure morphism; it then follows at once from the definition of `𝔛` from `𝓑`
(4.8.7) that `𝔛` is canonically isomorphic to `X̂` and that `f` is identified with `û` (it suffices to see this for the
case where `Y` is affine).

Note that (5.1.8) is a particular case of (5.4.4).

**Theorem (5.4.5).**

<!-- label: III.5.4.5 -->

*Let `A` be an adic Noetherian ring, `𝔍` an ideal of definition of `A`, `S = Spec(A)`, `𝔖 = Ŝ = Spf(A)`, `f : 𝔛 → 𝔖` a
proper morphism of formal schemes. Set `S_k = Spec(A/𝔍^{k+1})`, `X_k = 𝔛 ×_𝔖 S_k`, and for every `𝒪_𝔛`-module `𝓕`,
`𝓕_k = 𝓕 ⊗_{𝒪_𝔛} 𝒪_{X_k} = 𝓕 / 𝔍^{k+1} 𝓕`.*

<!-- original page 158 -->

*Let `ℒ` be an invertible `𝒪_𝔛`-module, and suppose that `ℒ_0 = ℒ / 𝔍ℒ` is an ample `𝒪_{X_0}`-module. Then `𝔛` is
algebraizable, and if `X` is a proper `S`-scheme such that `𝔛` is isomorphic to `X̂`, there exists an ample `𝒪_X`-module
`ℳ` such that `ℒ` is isomorphic to `ℳ̂` (which implies that `X` is projective over `S`).*

**Proof.** Let us apply (5.2.3) to `𝓕 = 𝒪_𝔛`: there thus exists an integer `n_0` such that for `n ≥ n_0`, the canonical
homomorphism `Γ(𝔛, ℒ^{⊗n}) → Γ(X_0, ℒ_0^{⊗n})` is surjective. One may suppose `n ≥ n_0` chosen large enough that
`ℒ_0^{⊗n}` is *very ample* for `S_0` `(II, 4.5.10)`. Since the morphism `f_0 : X_0 → S_0` is proper, `Γ(X_0, ℒ_0^{⊗n})`
is an `A`-module of finite type (3.2.1), hence there exists a sub-`A`-module of finite type `E` of `Γ(𝔛, ℒ^{⊗n})` whose
image in `Γ(X_0, ℒ_0^{⊗n})` is this latter module in its entirety. This being so, for every `k ≥ 0`, consider the
homomorphism `u_k : E / 𝔍^{k+1} E → Γ(X_k, ℒ_k^{⊗n})` deduced from the canonical injection `E → Γ(𝔛, ℒ^{⊗n})`. Note that
`(f_k)_*(ℒ_k^{⊗n})` is quasi-coherent, and since `Γ(S_k, (f_k)_*(ℒ_k^{⊗n})) = Γ(X_k, ℒ_k^{⊗n})`, `u_k` defines a
homomorphism `ũ_k : (E / 𝔍^{k+1} E)^∼ → (f_k)_*(ℒ_k^{⊗n})`, and consequently also a homomorphism
`ũ_k^♯ : f_k^*((E / 𝔍^{k+1} E)^∼) → ℒ_k^{⊗n}`. Moreover, if one sets `𝒢_k = f_k^*((E / 𝔍^{k+1} E)^∼)`, one has
`𝒢_k = 𝒢_0 / 𝔍^k 𝒢_0` `(I, 9.1.5)`, hence `ũ_k^♯ : 𝒢_k / 𝔍^k 𝒢_k → ℒ_k^{⊗n} / 𝔍^k ℒ_k^{⊗n}` is deduced from `ũ_0^♯` by
passage to quotients. Now, by definition of `E`, `ũ_0^♯` is none other than the canonical homomorphism
`σ : f_0^*((f_0)_*(ℒ_0^{⊗n})) → ℒ_0^{⊗n}`, and the hypothesis that `ℒ_0^{⊗n}` is very ample entails that `ũ_0^♯` is
*surjective* `(II, 4.4.3)`; one then deduces from Nakayama's lemma that each of the `ũ_k^♯` is also surjective. Each of
the `ũ_k^♯` therefore defines `(II, 4.2.2)` an `S_k`-morphism `g_k : X_k → P_k = 𝐏(E / 𝔍^{k+1} E)`, and since
`P_h = P_k ×_{S_k} S_h` for `h ≤ k` by virtue of `(II, 4.1.3)`, `(g_k)` is an `(S_k)`-adic inductive system
`(I, 10.12.2)` by virtue of the relations between the `ũ_k^♯` and of `(II, 4.2.10)`. The `g_k` therefore define an
`𝔖`-morphism of formal schemes `g : 𝔛 → 𝔓`, where `𝔓` is the inductive limit of the system `(P_k)`, or equivalently the
completion `P̂`, where `P = 𝐏(E)`. In addition, the hypothesis that `ℒ_0^{⊗n}` is very ample entails that `g_0` is a
closed immersion `(II, 4.4.3)`; one concludes that `g` is a closed immersion of formal schemes (4.8.10), hence `𝔛` is
algebraizable (5.1.8). The fact that `ℒ` is isomorphic to the completion `ℳ̂` of an invertible `𝒪_X`-module then follows
from the existence theorem (5.1.6). In addition, `ℒ^{⊗n}` is then the completion of `ℳ^{⊗n}` `(I, 10.8.10)`, and the
homomorphisms `ũ_k^♯` define a well-determined homomorphism `v̂ : f^*(Ẽ) → ℳ̂^{⊗n}` (5.1.7); moreover, since `v̂` is
surjective, so is `v` `(I, 10.11.5)`, hence so is `u` (5.1.3); in addition, the morphism `r : X → P` defined by `v`
`(II, 4.2.2)` has as extension to the completions `g`, and since `g` is a closed immersion, so is `r`, by (5.1.8) and
(5.4.1); one concludes that `ℳ^{⊗n}` is very ample `(II, 4.4.6)` and `ℳ` is ample `(II, 4.5.10)`.

**Remark (5.4.6).**

<!-- label: III.5.4.6 -->

Let `A` be an adic Noetherian ring, `𝔖 = Spf(A)`, `f : 𝔛 → 𝔖` a proper morphism of formal schemes. Let `𝒩` be the
coherent Ideal of `𝒪_𝔛` such that for every formal affine open `U` of `𝔛`, `Γ(U, 𝒩)` is the nilradical of `Γ(U, 𝒪_𝔛)`;
the existence of this Ideal follows easily from `(I, 10.10.2)` and from the fact that every ring homomorphism `B → C`
sends the nilradical of `B` into that of `C`. Let `𝔛'` be the closed formal subscheme of `𝔛` defined by `𝒩`
`(I, 10.14.2)`; it would be interesting to know whether, when `𝔛'` is algebraizable, `𝔛` itself is algebraizable. One
would no doubt arrive at a solution to this problem if one knew how to classify (for example by means of invariants of

<!-- original page 159 -->

cohomological nature) the *extensions* of a structure sheaf `𝒪_𝔛` (for a usual prescheme or a formal prescheme) by an
Ideal of square zero, in other words the `𝒪_𝔛`-Algebras `𝒜` such that `𝒪_𝔛` is isomorphic to `𝒜 / 𝒥`, where `𝒥` is an
Ideal of square zero of `𝒜`.

## 5.5. A decomposition of certain schemes

**Proposition (5.5.1).**

<!-- label: III.5.5.1 -->

*Let `A` be an adic Noetherian ring, `𝔍` an ideal of definition of `A`, `Y = Spec(A)`. Let `f : X → Y` be a separated
morphism of finite type; set `Y_0 = Spec(A/𝔍)`, `X_0 = X ×_Y Y_0 = f⁻¹(Y_0)`. Let `Z_0` be an open part of `X_0`, proper
over `Y_0`; then there exists in `X` an open and closed part `Z`, proper over `Y` and such that `Z ∩ X_0 = Z_0`.*

**Proof.** By hypothesis, there is an open subset `T` of `X` such that `T ∩ X_0 = Z_0`; let `𝔗` be the completion along
`Z_0` of the scheme induced by `X` on the open subset `T`; the support of `𝒪_𝔗` being `Z_0`, which is proper over `Y_0`,
`𝔗` is proper over `Ŷ = Spf(A)` (3.4.1). It follows from (5.1.8) that there exists a closed subscheme `Z` of `T` proper
over `Y` such that, if `i : Z → T` is the canonical injection, `î : 𝒵̂ → 𝔗` is an isomorphism (`𝒵̂` being the completion
of `Z` along `Z_0`). One concludes (4.6.8) that there exists in `T` an open neighbourhood `V` of `Z_0` such that the
restriction `i⁻¹(V) → V` of `i` is an isomorphism. But `i⁻¹(V)` is a neighbourhood of `Z_0` in `Z`, hence is necessarily
identical to `Z` (5.1.3.1). One concludes that `Z` is open in `T`, hence in `X`, which completes the proof.

**Corollary (5.5.2).**

<!-- label: III.5.5.2 -->

*If `X_0` is proper over `Y_0`, `X` is the union of two disjoint open parts `Z` and `Z'` such that `Z` is proper over
`Y` and contains `X_0`; in addition, every closed part `P` of `X`, proper over `Y`, is contained in `Z`.*

**Proof.** The last assertion follows from the fact that `P ∩ Z'`, being closed in `P`, is proper over `Y`; if `P ∩ Z'`
were not empty, `f(P ∩ Z')` would be closed non-empty in `Y`, hence would meet `Y_0` (5.1.3.1), which contradicts the
definition of `Z`.

*(To be continued.)*

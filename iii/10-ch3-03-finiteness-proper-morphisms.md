# §3. The finiteness theorem for proper morphisms

<!-- original page 115 -->

## 3.1. The dévissage lemma

**Definition (3.1.1).**

<!-- label: III.3.1.1 -->

Let `𝒞` be an abelian category. We say that a subset `𝒞'` of the set of objects of `𝒞` is *exact* if `0 ∈ 𝒞'` and if,
for every exact sequence `0 → A' → A → A'' → 0` in `𝒞` such that two of the objects `A`, `A'`, `A''` are in `𝒞'`, then
the third is also in `𝒞'`.

**Theorem (3.1.2).**

<!-- label: III.3.1.2 -->

*Let `X` be a Noetherian prescheme; denote by `𝒞` the abelian category of coherent `𝒪_X`-modules. Let `𝒞'` be an exact
subset of `𝒞`, and `X'` a closed subset of the underlying space of `X`. Suppose that for every closed irreducible subset
`Y` of `X'`, with generic point `y`, there exists an `𝒪_X`-module `𝒢 ∈ 𝒞'` such that `𝒢_y` is a `κ(y)`-vector space of
dimension `1`. Then every coherent `𝒪_X`-module with support contained in `X'` belongs to `𝒞'` (and in particular, if
`X' = X`, then `𝒞' = 𝒞`).*

**Proof.** Consider the following property `P(Y)` of a closed subset `Y` of `X'`: every coherent `𝒪_X`-module with
support contained in `Y` belongs to `𝒞'`. By virtue of the principle of Noetherian induction `(0_I, 2.2.2)`, we see that
we are reduced to proving that *if `Y` is a closed subset of `X'` such that the property `P(Y')` is true for every
closed subset `Y'` of `Y`, distinct from `Y`, then `P(Y)` is true*.

So let `ℱ ∈ 𝒞` have support contained in `Y`, and let us prove that `ℱ ∈ 𝒞'`. Denote also by `Y` the closed reduced
subprescheme of `X` having `Y` for underlying space `(I, 5.2.1)`; it is defined by a coherent sheaf of ideals `𝒥` of
`𝒪_X`. We know `(I, 9.3.4)` that there exists an integer `n > 0` such that `𝒥^n ℱ = 0`; for `1 ≤ k ≤ n`, we thus have an
exact sequence

```text
  0 → 𝒥^{k−1} ℱ / 𝒥^k ℱ → ℱ / 𝒥^k ℱ → ℱ / 𝒥^{k−1} ℱ → 0
```

of coherent `𝒪_X`-modules `(0_I, 5.3.6 and 5.3.3)`; as `𝒞'` is exact, we see, by induction on `k`, that it suffices to
show that each of the `ℱ_k = 𝒥^{k−1} ℱ / 𝒥^k ℱ` is in `𝒞'`. We are thus reduced to proving that `ℱ ∈ 𝒞'` under the
additional hypothesis that `𝒥 ℱ = 0`; this is equivalent to saying that `ℱ = j_*(j^*(ℱ))`, where `j` is the canonical
injection `Y → X`. We now distinguish two cases:

a) *`Y` is reducible.* Let `Y = Y' ∪ Y''`, where `Y'` and `Y''` are closed subsets of `Y`, distinct from `Y`; denote
also by `Y'`, `Y''` the closed reduced subpreschemes of `X` having `Y'`, `Y''` respectively for underlying spaces,
defined respectively by the coherent sheaves of ideals `𝒥'`, `𝒥''` of `𝒪_X`. Set `ℱ' = ℱ ⊗_{𝒪_X} (𝒪_X / 𝒥')` and
`ℱ'' = ℱ ⊗_{𝒪_X} (𝒪_X / 𝒥'')`. The canonical homomorphisms `ℱ → ℱ'`, `ℱ → ℱ''` thus define a homomorphism
`u : ℱ → ℱ' ⊕ ℱ''`. We show that for every `z ∉ Y' ∩ Y''`, the homomorphism `u_z : ℱ_z → ℱ'_z ⊕ ℱ''_z` is *bijective*.
Indeed, we have `𝒥' ∩ 𝒥'' = 𝒥`, since the question is local and

<!-- original page 116 -->

the preceding equality results from `(I, 5.2.1 and 1.1.5)`; if `z ∉ Y''`, we then have `𝒥''_z = 𝒪_{X,z}`, hence
`ℱ''_z = 0` and `ℱ'_z = ℱ_z`, which establishes our assertion in this case; we reason similarly for `z ∉ Y'`.
Consequently, the kernel and cokernel of `u`, which are in `𝒞` `(0_I, 5.3.4)`, have their support in `Y' ∩ Y''`, and are
thus in `𝒞'` by hypothesis; for the same reason, `ℱ'` and `ℱ''` are in `𝒞'`, hence also `ℱ' ⊕ ℱ''`, since `𝒞'` is exact.
The conclusion then follows from the consideration of the two exact sequences

```text
  0 → Im u → ℱ' ⊕ ℱ'' → Coker u → 0,
  0 → Ker u → ℱ → Im u → 0,
```

and from the hypothesis that `𝒞'` is exact.

b) *`Y` is irreducible*, and consequently the subprescheme `Y` of `X` is *integral*. If `y` is its generic point, we
have `(𝒪_Y)_y = κ(y)`, and as `j^*(ℱ)` is a coherent `𝒪_Y`-module, `ℱ_y = (j^*(ℱ))_y` is a `κ(y)`-vector space of finite
dimension `m`. By hypothesis, there is a coherent `𝒪_X`-module `𝒢 ∈ 𝒞'` (necessarily of support `Y`) such that `𝒢_y` is
a `κ(y)`-vector space of dimension `1`. Consequently, there is a `κ(y)`-isomorphism `(𝒢_y)^m ⥲ ℱ_y`, which is also an
`𝒪_Y`-isomorphism, and since `𝒢^m` and `ℱ` are coherent, there exists an open neighbourhood `W` of `y` in `X` and an
isomorphism `𝒢^m ∣ W ⥲ ℱ ∣ W` `(0_I, 5.2.7)`. Let `ℋ` be the graph of this isomorphism, which is a coherent
`(𝒪_X ∣ W)`-submodule of `(𝒢^m ⊕ ℱ) ∣ W`, canonically isomorphic to `𝒢^m ∣ W` and to `ℱ ∣ W`; there thus exists a
coherent `𝒪_X`-submodule `ℋ_0` of `𝒢^m ⊕ ℱ`, inducing `ℋ` on `W` and `0` on `X − Y`, since `𝒢^m` and `ℱ` have `Y` for
support `(I, 9.4.7)`. The restrictions `v : ℋ_0 → 𝒢^m` and `w : ℋ_0 → ℱ` of the canonical projections of `𝒢^m ⊕ ℱ` are
then homomorphisms of coherent `𝒪_X`-modules, which, on `W` and on `X − Y`, reduce to isomorphisms; in other words, the
kernels and cokernels of `v` and `w` have their support in the closed set `Y − (Y ∩ W)`, distinct from `Y`. They are
thus in `𝒞'`; on the other hand, `𝒢^m ∈ 𝒞'` since `𝒢 ∈ 𝒞'` and `𝒞'` is exact. We conclude successively, by the exactness
of `𝒞'`, that `ℋ_0 ∈ 𝒞'` and then `ℱ ∈ 𝒞'`. Q.E.D.

**Corollary (3.1.3).**

<!-- label: III.3.1.3 -->

*Suppose that the exact subset `𝒞'` of `𝒞` has in addition the property that every coherent direct factor of a coherent
`𝒪_X`-module `ℳ ∈ 𝒞'` is again in `𝒞'`. Under these conditions, the conclusion of (3.1.2) remains valid when the
condition "`𝒢_y` is a `κ(y)`-vector space of dimension `1`" is replaced by `𝒢_y ≠ 0` (which is equivalent to
`Supp(𝒢) = Y`).*

**Proof.** Indeed, the reasoning of (3.1.2) need be modified only in case b); this time `𝒢_y` is a `κ(y)`-vector space
of dimension `q > 0`, and we have consequently an `𝒪_Y`-isomorphism `(𝒢_y)^m ⥲ (ℱ_y)^q`; the end of the reasoning of
(3.1.2) then proves that `ℱ^q ∈ 𝒞'`, and the additional hypothesis on `𝒞'` implies that `ℱ ∈ 𝒞'`.

## 3.2. The finiteness theorem: case of usual schemes

**Theorem (3.2.1).**

<!-- label: III.3.2.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism. For every coherent `𝒪_X`-module `ℱ`, the
`𝒪_Y`-modules `R^q f_*(ℱ)` are coherent for `q ≥ 0`.*

**Proof.** The question being local on `Y`, we may suppose `Y` Noetherian, hence `X` Noetherian `(I, 6.3.7)`. The
coherent `𝒪_X`-modules `ℱ` for which the conclusion of Theorem (3.2.1) is true form an *exact* subset `𝒞'` of the
category `𝒞` of coherent `𝒪_X`-modules.

<!-- original page 117 -->

Indeed, let `0 → ℱ' → ℱ → ℱ'' → 0` be an exact sequence of coherent `𝒪_X`-modules; suppose for example that `ℱ'` and
`ℱ''` belong to `𝒞'`; we have the long exact sequence in cohomology

```text
  R^{q−1} f_*(ℱ'') →^∂ R^q f_*(ℱ') → R^q f_*(ℱ) → R^q f_*(ℱ'') →^∂ R^{q+1} f_*(ℱ'),
```

in which by hypothesis the four outer terms are coherent; the middle term `R^q f_*(ℱ)` is therefore likewise coherent by
`(0_I, 5.3.4 and 5.3.3)`. One shows in the same way that when `ℱ` and `ℱ'` (resp. `ℱ` and `ℱ''`) are in `𝒞'`, so is
`ℱ''` (resp. `ℱ'`). Moreover, every coherent *direct factor* `ℱ'` of an `𝒪_X`-module `ℱ ∈ 𝒞'` also belongs to `𝒞'`:
indeed, `R^q f_*(ℱ')` is then a direct factor of `R^q f_*(ℱ)` `(G, II, 4.4.4)`, hence of finite type, and since it is
quasi-coherent (1.4.10), it is coherent, `Y` being Noetherian. By virtue of (3.1.3), we are reduced to proving that when
`X` is *irreducible* with generic point `x`, there exists *one* coherent `𝒪_X`-module `ℱ` belonging to `𝒞'` such that
`ℱ_x ≠ 0`: indeed, if this point is established, it can be applied to every irreducible closed subprescheme `Y` of `X`,
since if `j : Y → X` is the canonical injection, then `f ∘ j` is proper `(II, 5.4.2)`, and if `𝒢` is a coherent
`𝒪_Y`-module with support `Y`, then `j_*(𝒢)` is a coherent `𝒪_X`-module such that `R^q (f ∘ j)_*(𝒢) = R^q f_*(j_*(𝒢))`
`(G, II, 4.9.1)`, so we are indeed in the conditions of application of (3.1.3).

Now, by virtue of Chow's lemma `(II, 5.6.2)`, there exists an irreducible prescheme `X'` and a *projective* and
surjective morphism `g : X' → X` such that `f ∘ g : X' → Y` is *projective*. There exists an `𝒪_{X'}`-module `ℒ` ample
for `g` `(II, 5.3.1)`; let us apply the fundamental theorem of projective morphisms (2.2.1) to `g : X' → X` and to `ℒ`:
there thus exists an integer `n` such that `ℱ = g_*(𝒪_{X'}(n))` is a coherent `𝒪_X`-module and `R^q g_*(𝒪_{X'}(n)) = 0`
for all `q > 0`; in addition, since `g^*(g_*(𝒪_{X'}(n))) → 𝒪_{X'}(n)` is surjective for `n` large enough (2.2.1), we see
that we may suppose that, at the generic point `x` of `X`, we have `ℱ_x ≠ 0` `(II, 3.4.7)`. On the other hand, since
`f ∘ g` is projective and `Y` Noetherian, the `R^p(f ∘ g)_*(𝒪_{X'}(n))` are *coherent* (2.2.1). This being so,
`R^•(f ∘ g)_*(𝒪_{X'}(n))` is the abutment of a Leray spectral sequence, whose `E_2`-term is given by
`E_2^{p,q} = R^p f_*(R^q g_*(𝒪_{X'}(n)))`; what precedes shows that this spectral sequence is degenerate, and we then
know `(0_III, 11.1.6)` that `E_2^{p,0} = R^p f_*(ℱ)` is isomorphic to `R^p(f ∘ g)_*(𝒪_{X'}(n))`, which completes the
proof.

**Corollary (3.2.2).**

<!-- label: III.3.2.2 -->

*Let `Y` be a locally Noetherian prescheme. For every proper morphism `f : X → Y`, the direct image under `f` of any
coherent `𝒪_X`-module is a coherent `𝒪_Y`-module.*

**Corollary (3.2.3).**

<!-- label: III.3.2.3 -->

*Let `A` be a Noetherian ring, `X` a proper scheme over `A`; for every coherent `𝒪_X`-module `ℱ`, the `H^p(X, ℱ)` are
`A`-modules of finite type, and there exists an integer `r > 0` such that for every coherent `𝒪_X`-module `ℱ` and every
`p > r`, `H^p(X, ℱ) = 0`.*

**Proof.** The second assertion has already been proved (1.4.12); the first follows from the finiteness theorem (3.2.1),
taking (1.4.11) into account.

In particular, if `X` is a *proper algebraic scheme* over a field `k`, then, for every coherent `𝒪_X`-module `ℱ`, the
`H^p(X, ℱ)` are `k`-vector spaces of *finite dimension*.

**Corollary (3.2.4).**

<!-- label: III.3.2.4 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism of finite type. For every coherent `𝒪_X`-module `ℱ`
whose support is proper over `Y` `(II, 5.4.10)`, the `𝒪_Y`-modules `R^q f_*(ℱ)` are coherent.*

<!-- original page 118 -->

**Proof.** The question being local on `Y`, we may suppose `Y` Noetherian, and it is then the same for `X` `(I, 6.3.7)`.
By hypothesis, every closed subprescheme `Z` of `X` whose underlying space is `Supp(ℱ)` is proper over `Y`; in other
words, if `j : Z → X` is the canonical injection, then `f ∘ j : Z → Y` is proper. Now, we may suppose `Z` is such that
`ℱ = j_*(𝒢)`, where `𝒢 = j^*(ℱ)` is a coherent `𝒪_Z`-module `(I, 9.3.5)`; as we have `R^q f_*(ℱ) = R^q (f ∘ j)_*(𝒢)` by
(1.3.4), the conclusion follows immediately from (3.2.1).

## 3.3. Generalization of the finiteness theorem (usual schemes)

**Proposition (3.3.1).**

<!-- label: III.3.3.1 -->

*Let `Y` be a Noetherian prescheme, `𝒮` a quasi-coherent `𝒪_Y`-algebra of finite type, graded in positive degrees,
`Y' = Proj(𝒮)` and `g : Y' → Y` the structure morphism. Let `f : X → Y` be a proper morphism, `𝒮' = f^*(𝒮)`,
`ℳ = ⊕_{k ∈ ℤ} ℳ_k` a quasi-coherent graded `𝒮'`-module of finite type. Then the `R^p f_*(ℳ) = ⊕_{k ∈ ℤ} R^p f_*(ℳ_k)`
are graded `𝒮`-modules of finite type for every `p`. Suppose in addition that `𝒮` is generated by `𝒮_1`; then, for each
`p ∈ ℤ`, there exists an integer `k_p` such that for every `k ≥ k_p` and every `r ≥ 0`, we have*

```text
  R^p f_*(ℳ_{k+r}) = 𝒮_r R^p f_*(ℳ_k).                                       (3.3.1.1)
```

**Proof.** The first assertion is identical to the statement of (2.4.1, (i)), where one has simply replaced "projective
morphism" by "proper morphism". Now, in the proof of (2.4.1, (i)), the hypothesis on `f` was used only to show (with the
notation of that proof) that `R^p f'_*(ℳ̃)` is a coherent `𝒪_{Y'}`-module. With the hypotheses of (3.3.1), `f'` is
proper `(II, 5.4.2, (iii))`, so the entire proof of (2.4.1, (i)) can be taken over without change, thanks to the
finiteness theorem (3.2.1).

As for the second assertion, it suffices to remark that there is a finite affine open cover `(U_i)` of `Y` such that the
restrictions to `U_i` of the two sides of (3.3.1.1) are equal for every `k ≥ k_{p,i}` `(II, 2.1.6, (ii))`; it suffices
to take for `k_p` the largest of the `k_{p,i}`.

**Corollary (3.3.2).**

<!-- label: III.3.3.2 -->

*Let `A` be a Noetherian ring, `𝔪` an ideal of `A`, `X` a proper `A`-scheme, `ℱ` a coherent `𝒪_X`-module. Then, for
every `p ≥ 0`, the direct sum `⊕_{k ≥ 0} H^p(X, 𝔪^k ℱ)` is a module of finite type over the ring `S = ⊕_{k ≥ 0} 𝔪^k`; in
particular, there exists an integer `k_p ≥ 0` such that for every `k ≥ k_p` and every `r ≥ 0`, we have*

```text
  H^p(X, 𝔪^{k+r} ℱ) = 𝔪^r H^p(X, 𝔪^k ℱ).                                     (3.3.2.1)
```

**Proof.** It suffices to apply (3.3.1) with `Y = Spec(A)`, `𝒮 = S̃`, `ℳ_k = 𝔪^k ℱ`, taking (1.4.11) into account.

It is worth recalling that the `S`-module structure on `⊕_{k ≥ 0} H^p(X, 𝔪^k ℱ)` is obtained by considering, for every
`a ∈ 𝔪^r`, the map `H^p(X, 𝔪^k ℱ) → H^p(X, 𝔪^{k+r} ℱ)` which comes by passage to cohomology from the multiplication
`𝔪^k ℱ → 𝔪^{k+r} ℱ` defined by `a` (2.4.1).

<!-- original page 119 -->

## 3.4. The finiteness theorem: case of formal schemes

The results of this section (apart from definition (3.4.1)) will not be used in the rest of this chapter.

**(3.4.1)**

<!-- label: III.3.4.1 -->

Let `𝔛` and `𝔖` be two locally Noetherian formal preschemes `(I, 10.4.2)`, `f : 𝔛 → 𝔖` a morphism of formal preschemes.
We say that `f` is a *proper morphism* if it satisfies the following conditions:

1° *`f` is a morphism of finite type `(I, 10.13.3)`*.

2° *If `𝒦` is a sheaf of ideals of definition of `𝔖` and if we set `𝒥 = f^*(𝒦) 𝒪_𝔛`, `X_0 = (𝔛, 𝒪_𝔛 / 𝒥)`,
`S_0 = (𝔖, 𝒪_𝔖 / 𝒦)`, the morphism `f_0 : X_0 → S_0` deduced from `f` `(I, 10.5.6)` is proper.*

It is immediate that this definition does not depend on the sheaf of ideals of definition `𝒦` of `𝔖` considered; indeed,
if `𝒦'` is a second sheaf of ideals of definition such that `𝒦' ⊂ 𝒦`, and if we set `𝒥' = f^*(𝒦') 𝒪_𝔛`,
`X'_0 = (𝔛, 𝒪_𝔛 / 𝒥')`, `S'_0 = (𝔖, 𝒪_𝔖 / 𝒦')`, the morphism `f'_0 : X'_0 → S'_0` deduced from `f` is such that the
diagram

```text
  X_0  →^{f_0}   S_0
   ↓ i           ↓ j
  X'_0 →^{f'_0}  S'_0
```

is commutative, `i` and `j` being surjective immersions; it thus comes to the same thing to say that `f_0` or `f'_0` is
proper, by virtue of `(II, 5.4.5)`.

Note that, for every `n ≥ 0`, if we set `X_n = (𝔛, 𝒪_𝔛 / 𝒥^{n+1})`, `S_n = (𝔖, 𝒪_𝔖 / 𝒦^{n+1})`, the morphism
`f_n : X_n → S_n` deduced from `f` `(I, 10.5.6)` is proper for every `n` as soon as it is for `n = 0` `(II, 5.4.6)`.

If `g : Y → Z` is a proper morphism of usual locally Noetherian preschemes, `Z'` a closed subset of `Z`, `Y'` a closed
subset of `Y` such that `g(Y') ⊂ Z'`, the extension `ĝ : Y_{/Y'} → Z_{/Z'}` of `g` to the completions `(I, 10.9.1)` is a
proper morphism of formal preschemes, as follows from the definition and from `(II, 5.4.5)`.

Let `𝔛` and `𝔖` be two locally Noetherian formal preschemes, `f : 𝔛 → 𝔖` a morphism of finite type `(I, 10.13.3)`; with
the notation being the same as above, one says that a subset `Z` of the underlying space of `𝔛` is *proper over `𝔖`* (or
*proper for `f`*) if, considered as a subset of `X_0`, `Z` is *proper over `S_0`* `(II, 5.4.10)`. All the properties of
proper subsets of usual preschemes stated in `(II, 5.4.10)` are still valid for proper subsets of formal preschemes, as
follows immediately from the definitions.

**Theorem (3.4.2).**

<!-- label: III.3.4.2 -->

*Let `𝔛`, `𝔜` be two locally Noetherian formal preschemes, `f : 𝔛 → 𝔜` a proper morphism. For every coherent
`𝒪_𝔛`-module `ℱ`, the `𝒪_𝔜`-modules `R^q f_*(ℱ)` are coherent for every `q ≥ 0`.*

Let `𝒥` be a sheaf of ideals of definition of `𝔜`, `𝒦 = f^*(𝒥) 𝒪_𝔛`, and consider the `𝒪_𝔛`-modules

```text
  ℱ_k = ℱ ⊗_{𝒪_𝔜} (𝒪_𝔜 / 𝒥^{k+1}) = ℱ / 𝒦^{k+1} ℱ            (k ≥ 0)         (3.4.2.1)
```

which obviously form a *projective system* of topological `𝒪_𝔛`-modules, such that

<!-- original page 120 -->

`ℱ = lim_← ℱ_k` `(I, 10.11.3)`. On the other hand, it will follow from (3.4.2) that each of the `R^q f_*(ℱ)`, being
coherent, is naturally equipped with a structure of topological `𝒪_𝔜`-module `(I, 10.11.6)`, and the same is true of the
`R^q f_*(ℱ_k)`. To the canonical homomorphisms `ℱ → ℱ_k = ℱ / 𝒦^{k+1} ℱ` there canonically correspond homomorphisms

```text
  R^q f_*(ℱ) → R^q f_*(ℱ_k),
```

which are necessarily continuous for the topological `𝒪_𝔜`-module structures above `(I, 10.11.6)`, and form a projective
system, giving in the limit a canonical functorial homomorphism

```text
  R^q f_*(ℱ) → lim_← R^q f_*(ℱ_k),                                           (3.4.2.2)
                k
```

which will be a continuous homomorphism of topological `𝒪_𝔜`-modules. We shall prove at the same time as (3.4.2) the

**Corollary (3.4.3).**

<!-- label: III.3.4.3 -->

*Each of the homomorphisms (3.4.2.2) is a topological isomorphism. Furthermore, if `𝔜` is Noetherian, the projective
system `(R^q f_*(ℱ / 𝒦^{k+1} ℱ))_{k ≥ 0}` satisfies the (ML)-condition `(0_III, 13.1.1)`.*

We shall begin by establishing (3.4.2) and (3.4.3) when `𝔜` is a Noetherian formal affine scheme `(I, 10.4.1)`:

**Corollary (3.4.4).**

<!-- label: III.3.4.4 -->

*Under the hypotheses of (3.4.2), suppose in addition that `𝔜 = Spf(A)`, where `A` is an adic Noetherian ring. Let `𝔍`
be an ideal of definition of `A`, and set `ℱ_k = ℱ / 𝔍^{k+1} ℱ` for `k ≥ 0`. Then the `H^n(𝔛, ℱ)` are `A`-modules of
finite type; the projective system `(H^n(𝔛, ℱ_k))_{k ≥ 0}` satisfies the (ML)-condition for every `n`; if we set*

```text
  N_{n,k} = Ker(H^n(𝔛, ℱ) → H^n(𝔛, ℱ_k))                                     (3.4.4.1)
```

*(also equal to `Im(H^n(𝔛, 𝔍^{k+1} ℱ) → H^n(𝔛, ℱ))` by the exact sequence in cohomology), the `N_{n,k}` define on
`H^n(𝔛, ℱ)` a `𝔍`-good filtration `(0_III, 13.7.7)`; finally, the canonical homomorphism*

```text
  H^n(𝔛, ℱ) → lim_← H^n(𝔛, ℱ_k)                                              (3.4.4.2)
                k
```

*is a topological isomorphism for every `n` (the left-hand side being equipped with the `𝔍`-adic topology, the
`H^n(𝔛, ℱ_k)` with the discrete topology).*

**Proof.** Set

```text
  S = gr(A) = ⊕_{k ≥ 0} 𝔍^k / 𝔍^{k+1},   ℳ = gr(ℱ) = ⊕_{k ≥ 0} 𝔍^k ℱ / 𝔍^{k+1} ℱ. (3.4.4.3)
```

We know that `𝔍^Δ` is a sheaf of ideals of definition of `𝔜` `(I, 10.3.1)`; let `𝒦 = f^*(𝔍^Δ) 𝒪_𝔛`,
`X_0 = (𝔛, 𝒪_𝔛 / 𝒦)`, `Y_0 = (𝔜, 𝒪_𝔜 / 𝔍^Δ) = Spec(A_0)` with `A_0 = A / 𝔍`. It is clear that the
`ℳ_k = 𝔍^k ℱ / 𝔍^{k+1} ℱ` are coherent `𝒪_{X_0}`-modules `(I, 10.11.3)`. On the other hand, consider the quasi-coherent
graded `𝒪_{X_0}`-algebra

```text
  𝒮 = 𝒪_{X_0} ⊗_{A_0} S = gr(𝒪_𝔛) = ⊕_{k ≥ 0} 𝒦^k / 𝒦^{k+1}.                  (3.4.4.4)
```

The hypothesis that `ℱ` is an `𝒪_𝔛`-module of finite type implies first that `ℳ` is

<!-- original page 121 -->

a graded `𝒮`-module *of finite type*. Indeed, the question is local on `𝔛`, and we may therefore suppose, in order to
treat it, that `𝔛 = Spf(B)`, where `B` is an adic Noetherian ring, and `ℱ = N^Δ`, where `N` is a `B`-module of finite
type `(I, 10.10.5)`; we have in addition `X_0 = Spec(B_0)` where `B_0 = B / 𝔍 B`, and the quasi-coherent
`𝒪_{X_0}`-modules `𝒮` and `ℳ` are respectively equal to `S̃'` and `M̃'`, where
`S' = ⊕_{k ≥ 0} ((𝔍^k / 𝔍^{k+1}) ⊗_{A_0} B_0)` and `M' = ⊕_{k ≥ 0} ((𝔍^k / 𝔍^{k+1}) ⊗_{A_0} N_0)`, with `N_0 = N / 𝔍 N`;
we then obviously have `M' = S' ⊗_{B_0} N_0`, and since `N_0` is a `B_0`-module of finite type, `M'` is an `S'`-module
of finite type, whence our assertion `(I, 1.3.13)`.

Since the morphism `f_0 : X_0 → Y_0` is *proper* by hypothesis, we may apply (3.3.2) to `𝒮`, `ℳ`, and the morphism
`f_0`; taking (1.4.11) into account, we conclude that for *every `n ≥ 0`*, `⊕_{k ≥ 0} H^n(X_0, ℳ_k)` is a graded
`S`-module *of finite type*. This proves that condition `(F_n)` of `(0_III, 13.7.7)` is satisfied for every `n ≥ 0`,
when we consider the strict projective system `(ℱ / 𝔍^k ℱ)_{k ≥ 0}` of sheaves of abelian groups on `X_0`, each equipped
with its natural structure of "filtered `A`-module". We may therefore apply `(0_III, 13.7.7)`, which proves that:

1° The projective system `(H^n(𝔛, ℱ_k))_{k ≥ 0}` satisfies the (ML)-condition.

2° If `H'^n = lim_← H^n(𝔛, ℱ_k)`, then `H'^n` is an `A`-module of finite type.

3° The filtration defined on `H'^n` by the kernels of the canonical homomorphisms `H'^n → H^n(𝔛, ℱ_k)` is `𝔍`-good.

Note on the other hand that if we set `X_k = (𝔛, 𝒪_𝔛 / 𝒦^{k+1})`, `ℱ_k` is a coherent `𝒪_{X_k}`-module `(I, 10.11.3)`,
and if `U` is an affine open set in `X_0`, then `U` is also an affine open set in each of the `X_k` `(I, 5.1.9)`, so
`H^n(U, ℱ_k) = 0` for every `n > 0` and every `k` (1.3.1) and `H^0(U, ℱ_k) → H^0(U, ℱ_h)` is surjective for `h ≤ k`
`(I, 1.3.9)`. We are therefore in the conditions of `(0_III, 13.3.2)`, and the application of `(0_III, 13.3.1)` proves
that `H'^n` is canonically identified with `H^n(𝔛, lim_← ℱ_k) = H^n(𝔛, ℱ)`; this completes the proof of (3.4.4).

**(3.4.5)**

<!-- label: III.3.4.5 -->

We now return to the proof of (3.4.2) and (3.4.3). We first prove these propositions in the case `𝔜 = Spf(A)` envisaged
in (3.4.4); for this, for every `g ∈ A`, apply (3.4.4) to the Noetherian affine formal scheme induced on the open set
`𝔜_g = 𝔇(g)` of `𝔜`, which is equal to `Spf(A_{{g}})`, and to the formal prescheme induced by `𝔛` on `f^{-1}(𝔜_g)`; note
that `𝔜_g` is also an affine open set in the prescheme `Y_k = (𝔜, 𝒪_𝔜 / (𝔍^Δ)^{k+1})`, and since `ℱ_k` is a coherent
`𝒪_{X_k}`-module, we have

```text
  H^n(f^{-1}(𝔜_g), ℱ_k) = Γ(𝔜_g, R^n f_*(ℱ_k))
```

for every `k ≥ 0` by virtue of (1.4.11). The canonical homomorphism

```text
  H^n(f^{-1}(𝔜_g), ℱ) → lim_← Γ(𝔜_g, R^n f_*(ℱ_k))
                          k
```

is an isomorphism; but we have `(0_I, 3.2.6)`

```text
  lim_← Γ(𝔜_g, R^n f_*(ℱ_k)) = Γ(𝔜_g, lim_← R^n f_*(ℱ_k))
    k                                   k
```

<!-- original page 122 -->

and as the sheaf `R^n f_*(ℱ)` is the sheaf associated to the presheaf `𝔜_g ↦ H^n(f^{-1}(𝔜_g), ℱ)` on the `𝔜_g`
`(0_I, 3.2.1)`, we have indeed shown that the homomorphism (3.4.2.2) is *bijective*. Let us next prove that `R^n f_*(ℱ)`
is a coherent `𝒪_𝔜`-module, and more precisely that we have

```text
  R^n f_*(ℱ) = (H^n(𝔛, ℱ))^Δ.                                                (3.4.5.1)
```

With the preceding notation, we have, since `ℱ_k` is a coherent `𝒪_{X_k}`-module (1.4.13),

```text
  Γ(𝔜_g, R^n f_*(ℱ_k)) = (Γ(𝔜, R^n f_*(ℱ_k)))_g = (H^n(𝔛, ℱ_k))_g.
```

Now, the `H^n(𝔛, ℱ_k)` form a projective system satisfying (ML), and their projective limit `H^n(𝔛, ℱ)` is an `A`-module
of finite type. We conclude `(0_III, 13.7.8)` that we have

```text
  lim_← ((H^n(𝔛, ℱ_k))_g) = H^n(𝔛, ℱ) ⊗_A A_{{g}} = Γ(𝔜_g, (H^n(𝔛, ℱ))^Δ),
    k
```

taking `(I, 10.10.8)` applied to `A` and `A_{{g}}` into account; this proves (3.4.5.1) since
`Γ(𝔜_g, R^n f_*(ℱ)) = lim_← Γ(𝔜_g, R^n f_*(ℱ_k))`.

As (3.4.2.2) is then an isomorphism of coherent `𝒪_𝔜`-modules, it is necessarily a *topological* isomorphism
`(I, 10.11.6)`. Finally, it follows from the relations `R^n f_*(ℱ_k) = (H^n(X, ℱ_k))^Δ` that the projective system
`(R^n f_*(ℱ_k))_{k ≥ 0}` satisfies (ML) `(I, 10.10.2)`.

Once (3.4.2) and (3.4.3) are proved in the case where the formal prescheme `𝔜` is affine Noetherian, it is immediate to
pass from there to the general case for (3.4.2) and the first assertion of (3.4.3), which are local on `𝔜`. As for the
second assertion of (3.4.3), it suffices, `𝔜` being Noetherian, to cover it by a finite number of Noetherian affine open
sets `U_i` and to remark that the restrictions of the projective system `(R^q f_*(ℱ_k))` to each of the `U_i` satisfy
(ML).

We have moreover proved along the way:

**Corollary (3.4.6).**

<!-- label: III.3.4.6 -->

*Under the hypotheses of (3.4.4), the canonical homomorphism*

```text
  H^q(𝔛, ℱ) → Γ(𝔜, R^q f_*(ℱ))                                               (3.4.6.1)
```

*is bijective.*

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iii/09-c3-s03-theoreme-finitude-morphismes-propres.md;
     cross-ref: /Users/jcreinhold/Code/ega/ega3/ega3-3.tex;
     PDF: ~/Code/pdfs/ega/EGA-III-1.pdf, pp. 115–122 -->

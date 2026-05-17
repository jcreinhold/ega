<!-- original page 134 -->

## §6. Flat morphisms of locally Noetherian preschemes

Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a morphism. For every `y ∈ Y`, the fibre
`f⁻¹(y) = X ×_Y Spec(k(y))` is also a locally Noetherian prescheme: it is enough to check this when `Y = Spec(A)` and
`X = Spec(B)` are spectra of Noetherian rings, and then `B ⊗_A k(y)` is a ring of fractions of the quotient ring `B/𝔍B`,
hence Noetherian. We propose first in this section to relate the properties of `X`, of `Y` and of the fibres `f⁻¹(y)`
(where `y` runs through `Y`), under the hypothesis that the morphism `f` is flat. The questions treated will reduce to
the study of the relations between the Noetherian local rings `𝒪_y`, `𝒪_x` and `𝒪_x ⊗_{𝒪_y} k(y)`, the homomorphism
`𝒪_y → 𝒪_x` being local and making `𝒪_x` into a flat `𝒪_y`-module. In nos. (6.11) to (6.13) (rather separate from the
rest of the section, by their "absolute" rather than "relative" nature), we apply certain of the preceding results to
find criteria allowing us to assert that the singular locus (or certain analogous sets) of certain preschemes are closed
sets; these criteria will play an important role in §7.

### 6.1. Flatness and dimension

**Proposition (6.1.1).**

<!-- label: IV.6.1.1 -->

*Let `A`, `B` be two Noetherian local rings, `𝔪` the maximal ideal of `A`, `k = A/𝔪` its residue field, `φ : A → B` a
local homomorphism. Suppose that for every prime ideal `𝔭` of `A` distinct from `𝔪`, and for every minimal element `𝔮`
of the set of prime ideals of `B` containing `𝔭B`, `φ⁻¹(𝔮)` is distinct from `𝔪` (in other words, that no irreducible
component of `Spec(B/𝔭B)` is contained in the inverse image of the closed point `𝔪` of `Spec(A)` in `Spec(B)`). Then one
has*

```text
  (6.1.1.1)            dim(B) = dim(A) + dim(B ⊗_A k).
```

We argue by induction on `n = dim(A)`; the assertion is trivial for `n = 0`, since `𝔪B` is then contained in the
nilradical of `B`, because `𝔪` is the nilradical of `A`. We may therefore suppose `n > 0`. Let `𝔮_i` (`1 ≤ i ≤ s`) be
the minimal prime ideals of `B`, and set `𝔭_i = φ⁻¹(𝔮_i)`; for every `i`, one has `𝔭_i ≠ 𝔪`, for otherwise (since
`n > 0`) there would exist a prime ideal `𝔭 ≠ 𝔪` contained in `𝔭_i`, and since `𝔮_i` is minimal among prime ideals of
`B` containing `𝔭B`, one would reach a contradiction with the hypothesis. Consequently `𝔪` is distinct from the union of
the `𝔭_i` and of the minimal prime ideals `𝔭'_j` (`1 ≤ j ≤ r`) of `A` (Bourbaki, *Alg. comm.*, chap. II, §1, n° 1, prop.
2), and there exists `a ∈ 𝔪` belonging to none of the `𝔭_i` nor the `𝔭'_j`. Set `A' = A/aA`, `B' = B/aB`; one has (0,
16.3.4)

```text
  dim(A') = dim(A) − 1,           dim(B') = dim(B) − 1
```

by construction of `a`, and on the other hand `B' ⊗_{A'} k = B ⊗_A k = B/𝔪B`, hence

```text
  dim(B' ⊗_{A'} k) = dim(B ⊗_A k);
```

it therefore suffices to prove (6.1.1.1) for `A'` and `B'`. But, by virtue of the bijective correspondence between
ideals of `A` (resp. `B`) containing `a` and ideals of `A'` (resp. `B'`), the hypotheses of the statement also hold for
`A'` and `B'`; one may therefore apply the inductive hypothesis, which completes the proof.

**Corollary (6.1.2).**

<!-- label: IV.6.1.2 -->

*Let `A`, `B` be two Noetherian local rings, `k` the residue field of `A`, `φ : A → B` a local homomorphism, `M ≠ 0` an
`A`-module of finite type, `N ≠ 0` a `B`-module of finite type. If `N` is a flat `A`-module (resp. if `B` is a flat
`A`-module), one has*

```text
  (6.1.2.1)        dim_B(M ⊗_A N) = dim_A(M) + dim_{B ⊗_A k}(N ⊗_A k)
```

*(resp. (6.1.1.1)).*

It suffices to prove the assertion concerning `N`; on the other hand, if `𝔟` is the annihilator of `N`, one may replace
`B` by `B/𝔟`, and hence suppose that `Supp(N) = Spec(B)`; the hypothesis then means that the morphism
`f : Spec(B) → Spec(A)` corresponding to `φ` is quasi-flat (2.3.3); one deduces (2.3.4) that for every prime ideal
`𝔭 ≠ 𝔪` of `A`,

<!-- original page 136 -->

every irreducible component of `f⁻¹(V(𝔭))` dominates `V(𝔭)`, and consequently the condition of (6.1.1) is satisfied,
whence the conclusion.

**Corollary (6.1.3).**

<!-- label: IV.6.1.3 -->

*Let `A`, `B` be two Noetherian local rings, `𝔪` the maximal ideal of `A`, `k` its residue field, `φ : A → B` a local
homomorphism. Suppose that `dim(B ⊗_A k) = 0` (that is to say (0, 16.2.1), that `𝔪B` is an ideal of definition of `B`).
Then one has `dim(B) ≤ dim(A)`. If moreover there exists a `B`-module of finite type `N` which is a flat `A`-module and
has support equal to `Spec(B)` (which holds in particular when `B` is a flat `A`-module), one has `dim(B) = dim(A)`.*

The first assertion follows from (5.5.1) and the second from (6.1.2).

**Corollary (6.1.4).**

<!-- label: IV.6.1.4 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a surjective morphism. For every closed subset `Z` of
`Y`, one has*

```text
  (6.1.4.1)            codim(f⁻¹(Z), X) ≤ codim(Z, Y).
```

*Moreover, if `f` is quasi-flat (2.3.3), the two sides of (6.1.4.1) are equal.*

Indeed, if `y` is a maximal point of `Z` and `x` a maximal point of the fibre `f⁻¹(y)`, one has
`dim(𝒪_x) ≤ dim(𝒪_{Y,y})` by virtue of (5.5.2); the inequality (6.1.4.1) follows from (5.1.2.1) and (5.1.3.1) and from
the fact that `f` is surjective. If moreover `f` is quasi-flat, one knows (2.3.4) that every irreducible component of
`f⁻¹(Z)` dominates an irreducible component of `Z`; the maximal points of `f⁻¹(Z)` are therefore the maximal points of
the fibres `f⁻¹(y)`, where `y` runs through the set of maximal points of `Z` (0_I, 2.1.8), and at each of these maximal
points `x` one has `dim(𝒪_x ⊗ k(x)) = 0`; since moreover `𝒪_x` is a flat `𝒪_y`-module, one has `dim(𝒪_x) = dim(𝒪_y)` by
virtue of (6.1.1), whence the equality in (6.1.4.1), in view of the fact that `f` is surjective.

Proposition (6.1.1) admits the following partial converse:

**Proposition (6.1.5).**

<!-- label: IV.6.1.5 -->

*Let `A`, `B` be two Noetherian local rings, `k` the residue field of `A`, `φ : A → B` a local homomorphism, `M` a
`B`-module of finite type. Suppose that:*

*1° `A` is a regular ring.*

*2° `M` is a Cohen-Macaulay `B`-module.*

*3° One has `dim_B(M) = dim(A) + dim_{B ⊗_A k}(M ⊗_A k)`.*

*Then `M` is a flat `A`-module.*

We proceed by induction on `n = dim(A)`. If `n = 0`, `A` is a field since it is regular (0, 17.1.4) and the assertion is
trivial. Suppose `n > 0`; let `𝔪` be the maximal ideal of `A`, and let `x ∈ 𝔪` be an element not belonging to `𝔪²`; one
then knows (0, 17.1.8) that `A' = A/xA` is regular and `dim(A') = dim(A) − 1`. Set

```text
  B' = B/xB,            M' = M/xM = M ⊗_A A';
```

one has therefore

```text
  B' ⊗_{A'} k = B ⊗_A k,           M' ⊗_{A'} k = M ⊗_A k
```

and by virtue of (5.5.1.2) one has

```text
  dim_{B'}(M') ≤ dim_B(M) + dim_{B' ⊗_{A'} k}(M' ⊗_{A'} k);
```

<!-- original page 137 -->

one therefore concludes from (0, 16.3.4) that one has

```text
  dim_B(M) ≤ dim_{B'}(M') + 1 ≤ (dim(A') + dim_{B ⊗_A k}(M ⊗_A k)) + 1 = dim(A) + dim_{B ⊗_A k}(M ⊗_A k).
```

Since by hypothesis the extreme members of these inequalities are equal, one necessarily has: (i)
`dim_{B'}(M') = dim_B(M) − 1`, and since `M` is by hypothesis a Cohen-Macaulay `B`-module, this means that `x` is
`M`-regular (0, 16.1.9 and 16.5.5); (ii) `dim_{B'}(M') = dim(A') + dim_{B' ⊗_{A'} k}(M' ⊗_{A'} k)`; since `M'` is a
Cohen-Macaulay `B'`-module by virtue of (i) and of (0, 16.1.9 and 16.5.5) and since `A'` is regular, the inductive
hypothesis proves that `M'` is a flat `A'`-module; one then deduces from (0_III, 10.2.7) that `M` is a flat `A`-module,
since `x` is `M`-regular by (i).

### 6.2. Flatness and projective dimension

**Proposition (6.2.1).**

<!-- label: IV.6.2.1 -->

*(i) Let `A`, `B` be two rings, `φ : A → B` a homomorphism such that `B` is a flat `A`-module. Then, for every
`A`-module `M`, one has*

```text
  (6.2.1.1)               dim. proj_B(M ⊗_A B) ≤ dim. proj_A(M).
```

*(ii) Suppose moreover that `A` is a Noetherian ring, `B` is a faithfully flat `A`-module and `M` is an `A`-module of
finite type; then*

```text
  (6.2.1.2)               dim. proj_B(M ⊗_A B) = dim. proj_A(M).
```

(i) One may restrict to the case where `n = dim. proj_A(M)` is finite; there exists therefore a left resolution

```text
  0 → P_n → P_{n−1} → ⋯ → P_0 → M → 0
```

of `M` by projective `A`-modules; since `B` is a flat `A`-module, the sequence

```text
  0 → P_n ⊗_A B → P_{n−1} ⊗_A B → ⋯ → P_0 ⊗_A B → M ⊗_A B → 0
```

is exact; moreover the `P_i ⊗_A B` are projective `B`-modules; whence the conclusion.

(ii) Suppose `dim. proj_B(M ⊗_A B) = m`, and consider an exact sequence

```text
  0 → R → P_{m−1} → P_{m−2} → ⋯ → P_0 → M → 0
```

where the `P_i` (`0 ≤ i ≤ m − 1`) are projective `A`-modules of finite type; since `A` is Noetherian, `R` is also an
`A`-module of finite type. Since `B` is a flat `A`-module, one also has an exact sequence

```text
  0 → R ⊗_A B → P_{m−1} ⊗_A B → ⋯ → P_0 ⊗_A B → M ⊗_A B → 0
```

and the hypothesis on `M ⊗_A B` implies that `R ⊗_A B` is a projective `B`-module (0, 17.2.1). Since `B` is a faithfully
flat `A`-module, one concludes that `R` is a projective `A`-module (Bourbaki, *Alg. comm.*, chap. I, §3, n° 6, prop.
12); hence `dim. proj_A(M) ≤ m`, which completes the proof.

**Corollary (6.2.2).**

<!-- label: IV.6.2.2 -->

*Let `f : X → Y` be a flat morphism of preschemes, `ℰ` a quasi-coherent `𝒪_Y`-Module. If `dim. proj(ℰ) ≤ n` (0,
17.2.14), one has `dim. proj(f*(ℰ)) ≤ n`.*

<!-- original page 138 -->

**Proposition (6.2.3).**

<!-- label: IV.6.2.3 -->

*Let `A`, `B` be two Noetherian local rings, `k` the residue field of `A`, `φ : A → B` a local homomorphism, `N` a
`B`-module of finite type. Suppose that `B` and `N` are flat `A`-modules. Then one has*

```text
  (6.2.3.1)               dim. proj_B(N) = dim. proj_{B ⊗_A k}(N ⊗_A k).
```

Consider in effect a left resolution of `N` by free `B`-modules of finite type

```text
  ⋯ → L_i → L_{i−1} → ⋯ → L_0 → N → 0.
```

Since the `L_i` and `N` are flat `A`-modules (`B` being a flat `A`-module), it follows from (2.1.10) that the `Z_i(L_•)`
are flat `A`-modules, that `L_• ⊗_A k` is a left resolution of the `(B ⊗_A k)`-module `N ⊗_A k`, and that one has
`Z_i(L_• ⊗_A k) = Z_i(L_•) ⊗_A k` for every `i`. Note that since `B` is Noetherian, the `Z_i(L_•)` are `B`-modules of
finite type, hence the `Z_i(L_• ⊗_A k)` are `(B ⊗_A k)`-modules of finite type. Now, to say that a `B`-module (resp. a
`(B ⊗_A k)`-module) of finite type is flat amounts to saying that it is free or also projective (0_III, 10.1.3). Since
the `Z_i(L_•)` are flat `A`-modules, it follows on the other hand from (0_III, 10.2.5) (where one takes `C = B`) that,
for `Z_i(L_•)` to be a flat `B`-module, it is necessary and sufficient that `Z_i(L_• ⊗_A k) = Z_i(L_•) ⊗_A k` be a flat
`(B ⊗_A k)`-module. The smallest integer `n` such that `Z_{n−1}(L_•)` is a free `B`-module is therefore also the
smallest integer such that `Z_{n−1}(L_• ⊗_A k)` is a free `(B ⊗_A k)`-module, which proves the proposition (0, 17.2.1).

### 6.3. Flatness and depth

**Proposition (6.3.1).**

<!-- label: IV.6.3.1 -->

*Let `A`, `B` be two Noetherian local rings, `k` the residue field of `A`, `φ : A → B` a local homomorphism, `M` an
`A`-module of finite type, `N` a `B`-module of finite type. If `N` is a flat `A`-module `≠ 0`, one has*

```text
  (6.3.1.1)            prof_B(M ⊗_A N) = prof_A(M) + prof_{B ⊗_A k}(N ⊗_A k).
```

One may restrict to the case where `M ≠ 0`, otherwise both sides of (6.3.1.1) are equal to `+∞`. We proceed by induction
on the integer `n` equal to the second member of (6.3.1.1) (which is finite by virtue of the hypotheses, of (0,
16.4.6.2) and of Nakayama's lemma applied to `N`). Suppose first `n = 0`; then, if `𝔪` and `𝔫` denote the maximal ideals
of `A` and `B` respectively, `𝔪` is a prime ideal associated with `M` and `𝔫/𝔪B` a prime ideal of `B/𝔪B = B ⊗_A k`
associated with `N ⊗_A k` (0, 16.4.6, (i)). One then concludes from (3.3.1) that `𝔫` is a prime ideal of `B` associated
with `M ⊗_A N`, hence (0, 16.4.6, (i)) that `prof_B(M ⊗_A N) = 0`. Suppose therefore `n > 0`, and distinguish two cases:

*a)* Suppose `prof_A(M) > 0`. Let `x ∈ 𝔪` be an `M`-regular element, and set

```text
  A' = A/xA,           B' = B/xB,           M' = M/xM,           N' = N/xN;
```

one has

```text
  B' ⊗_{A'} k = B ⊗_A k,          N' ⊗_{A'} k = N ⊗_A k
```

since `x ∈ 𝔪`, and

```text
  M' ⊗_{A'} N' = M ⊗_A N/x(M ⊗_A N);
```

<!-- original page 139 -->

moreover, since `N` is a flat `A`-module, the hypothesis that `x` is `M`-regular entails that `x` is also
`(M ⊗_A N)`-regular (0_I, 6.1.1). One has consequently (0, 16.4.6, (ii) and 16.4.8)

```text
  prof_{A'}(M') = prof_A(M) − 1,            prof_{B'}(M' ⊗_{A'} N') = prof_B(M ⊗_A N) − 1
```

and

```text
  prof_{B' ⊗_{A'} k}(N' ⊗_{A'} k) = prof_{B ⊗_A k}(N ⊗_A k).
```

The equality (6.3.1.1) is therefore a consequence of the same relation for `A'`, `B'`, `M'` and `N'`; but since `N` is a
flat `A`-module, `N' = N ⊗_A A'` is a flat `A'`-module (0_I, 6.2.1); one may consequently apply the inductive
hypothesis, which proves (6.3.1.1) in this case.

*b)* Suppose `prof_{B ⊗_A k}(N ⊗_A k) > 0`. Consider an element `y ∈ 𝔪` which is `(N ⊗_A k)`-regular; it follows from
(0_III, 10.2.4) that `y` is then `N`-regular and that

```text
  N' = N/yN
```

is a flat `A`-module, since `N` is supposed to be a flat `A`-module. Applying (0_I, 6.1.2) to the exact sequence of
`A`-modules

```text
  0 → N →^y N → N' → 0
```

one concludes isomorphisms

```text
  (M ⊗_A N)/y(M ⊗_A N) ⥲ M ⊗_A N'         and          N' ⊗_A k ⥲ (N ⊗_A k)/y(N ⊗_A k)
```

and moreover that `y` is `(M ⊗_A N)`-regular. One has consequently

```text
  prof_{B ⊗_A k}(N' ⊗_A k) = prof_{B ⊗_A k}(N ⊗_A k) − 1
```

and

```text
  prof_B(M ⊗_A N') = prof_B(M ⊗_A N) − 1;
```

the inductive hypothesis shows that the relation (6.3.1.1) is valid for `A`, `B`, `M` and `N'`, and from what precedes,
one deduces (6.3.1.1) for `A`, `B`, `M` and `N`.

**Corollary (6.3.2).**

<!-- label: IV.6.3.2 -->

*Under the hypotheses of (6.3.1), suppose moreover `M ≠ 0` and `N ≠ 0`; then one has*

```text
  (6.3.2.1)            coprof_B(M ⊗_A N) = coprof_A(M) + coprof_{B ⊗_A k}(N ⊗_A k).
```

This follows at once from (6.3.1.1) and (6.1.2) and from the definition of codepth (0, 16.4.9).

**Corollary (6.3.3).**

<!-- label: IV.6.3.3 -->

*Under the hypotheses of (6.3.1), suppose moreover `M ≠ 0` and `N ≠ 0`; for `M ⊗_A N` to be a Cohen-Macaulay `B`-module,
it is necessary and sufficient that `M` be a Cohen-Macaulay `A`-module and that `N ⊗_A k` be a Cohen- Macaulay
`(B ⊗_A k)`-module.*

This follows from corollary (6.3.2) and from the definition of Cohen-Macaulay modules by the fact that their codepth is
zero (0, 16.5.1), taking into account that the condition `N ≠ 0` is equivalent to `N ⊗_A k ≠ 0` by virtue of Nakayama's
lemma.

**Corollary (6.3.4).**

<!-- label: IV.6.3.4 -->

*Under the hypotheses of (6.3.1), suppose moreover that `N ⊗_A k` is a `B`-module of finite length; then one has*

```text
  (6.3.4.1)               prof_B(M ⊗_A N) = prof_A(M).
```

<!-- original page 140 -->

*If moreover `M ≠ 0` and `N ≠ 0`, one has*

```text
  (6.3.4.2)               coprof_B(M ⊗_A N) = coprof_A(M).
```

Indeed, it amounts to the same to say that `N ⊗_A k` is a `B`-module of finite length or a `(B ⊗_A k)`-module of finite
length, and one knows (0, 16.2.3) that modules of finite length `≠ 0` are of dimension `0` and of depth `0`.

Corollary (6.3.4) will be applicable in particular when `B ⊗_A k` is a ring of finite length, that is to say when `𝔪B`
is an ideal of definition of the ring `B`.

**Corollary (6.3.5).**

<!-- label: IV.6.3.5 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a flat morphism.*

*(i) If, at a point `x ∈ X`, one has `coprof(𝒪_x) ≤ n`, then, setting `y = f(x)`, one has `coprof(𝒪_y) ≤ n` and
`coprof(𝒪_x ⊗_{𝒪_y} k(y)) ≤ n`; in particular, if `𝒪_x` is a Cohen-Macaulay ring, so are `𝒪_y` and `𝒪_x ⊗_{𝒪_y} k(y)`.*

*(ii) Suppose conversely that `𝒪_x ⊗_{𝒪_y} k(y)` is a Cohen-Macaulay ring. Then, if `coprof(𝒪_y) ≤ n` (resp. if `𝒪_y` is
a Cohen-Macaulay ring), one has `coprof(𝒪_x) ≤ n` (resp. `𝒪_x` is a Cohen-Macaulay ring).*

It suffices to apply (6.3.2) for `M = A = 𝒪_y` and `N = B = 𝒪_x`.

**Corollary (6.3.6).**

<!-- label: IV.6.3.6 -->

*Let `A` be a Cohen-Macaulay ring. Then `A' = A[T_1, …, T_n]` (`T_i` indeterminates) is a Cohen-Macaulay ring.*

Indeed, if one sets `Y = Spec(A)`, `X = Spec(A')` and if `f : X → Y` is the canonical morphism, `f` is flat (since `A'`
is a free `A`-module (2.1.2)) and for every `y ∈ Y`, `k(y)[T_1, …, T_n]` is a regular ring (0, 17.3.7), hence *a
fortiori* Cohen-Macaulay; it therefore suffices to apply (6.3.5).

**Corollary (6.3.7).**

<!-- label: IV.6.3.7 -->

*Every quotient of a Cohen-Macaulay ring is universally catenary.*

This follows from (6.3.6), from (5.6.1) and from (0, 16.5.12).

**Proposition (6.3.8).**

<!-- label: IV.6.3.8 -->

*Let `A` be a Noetherian local ring; suppose that there exists an `A`-module `M` of finite type which is a Cohen-
Macaulay `A`-module and whose support is equal to `Spec(A)`. Let `B` be a quotient ring of `A`, and let
`f : Spec(B̂) → Spec(B)` be the canonical morphism; then, for every `x ∈ Spec(B)`, `f⁻¹(x)` is a Cohen-Macaulay scheme.*

Since `B` is an `A`-module of finite type, one has `B̂ = B ⊗_A Â` (0_I, 7.3.3), hence `f` is the restriction to
`Spec(B̂)` of the canonical morphism `Spec(Â) → Spec(A)`, and the fibres of these two morphisms at a point of `Spec(B)`
are therefore the same. One is therefore reduced to proving the proposition when `B = A`. So let `𝔭 = 𝔧_x` be a prime
ideal of `A`; since by hypothesis `𝔭 ∈ Supp(M)`, one knows (0, 16.5.6 and 16.5.9) that there exists an `M`-regular
sequence `(t_i)_{1 ≤ i ≤ r}` of elements of `𝔭` such that `N = M/(∑_{i=1}^r t_i M)` is a Cohen-Macaulay `A`-module, `𝔭`
a minimal associated prime ideal of `N` and `dim(N) = dim(M/𝔭M) = dim(A/𝔭)`. The same reasoning as at the start shows
that one may replace `M` by `N` and `A` by `A/(∑_{i=1}^r t_i A)`, and consequently suppose that `𝔭` is a minimal prime
ideal of `A`.

<!-- original page 141 -->

Set for simplicity `A' = Â`, `M' = M̂ = M ⊗_A A'` (0_I, 7.3.3); one knows (0, 16.5.2) that `M'` is a Cohen-Macaulay
`A'`-module, which entails that for every prime ideal `𝔭'` of `A'`, `M'_{𝔭'}` is a Cohen-Macaulay `A'_{𝔭'}`-module (0,
16.5.10). Taking (I, 3.6.5) into account, one sees that if one sets `A'' = A' ⊗_A A_𝔭` and `M'' = M' ⊗_A A_𝔭`, `M''` is
a Cohen-Macaulay `A''`-module. For every prime ideal `𝔭''` of `A''` over `𝔭`, `M''_{𝔭''} = M_𝔭 ⊗_{A_𝔭} A''_{𝔭''}` is
therefore a Cohen-Macaulay `A''_{𝔭''}`-module (0, 16.5.10); on the other hand, `M_𝔭` is by hypothesis a Cohen-Macaulay
`A_𝔭`-module and `A''_{𝔭''}` is a flat `A_𝔭`-module since `A'` is a flat `A`-module (0_I, 7.3.3 and 6.3.2). One
concludes from (6.3.3) that, if `k` is the residue field of `A_𝔭`, `k ⊗_{A_𝔭} A''_{𝔭''}` is a Cohen-Macaulay ring. But
since `A_𝔭` is of dimension `0`, the prime ideals of `A''` correspond bijectively to those of `k ⊗_{A_𝔭} A''` (I,
3.5.7), and if `𝔮''` is the prime ideal of `k ⊗_{A_𝔭} A''` corresponding to `𝔭''`, the local rings
`(k ⊗_{A_𝔭} A'')_{𝔮''}` and `k ⊗_{A_𝔭} A''_{𝔭''}` are isomorphic. Consequently (0, 16.5.13), the ring `k ⊗_{A_𝔭} A''` is
a Cohen-Macaulay ring. Q.E.D.

### 6.4. Flatness and property `(S_n)`

**Proposition (6.4.1).**

<!-- label: IV.6.4.1 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a morphism, `ℰ` a coherent `𝒪_Y`-Module, `ℱ` a coherent
`𝒪_X`-Module that is `f`-flat.*

*(i) Let `x ∈ Supp(ℱ)` be such that `ℰ ⊗_Y ℱ` has property `(S_k)` at the point `x`; then `ℰ` has property `(S_k)` at
the point `y = f(x)`.*

*(ii) Suppose that for every `y ∈ f(Supp(ℱ))`, `ℱ_y = ℱ ⊗_{𝒪_y} k(y)` has property `(S_k)`; then, if for a point
`y ∈ f(Supp(ℱ))`, `ℰ` has property `(S_k)` at the point `y`, `ℰ ⊗_Y ℱ` has property `(S_k)` at every point of `f⁻¹(y)`.*

(i) One knows (Err_III, 30) that there exists a closed sub-prescheme `X'` of `X` with underlying space `Supp(ℱ)` and a
coherent `𝒪_{X'}`-Module `ℱ'` such that `ℱ = j_*(ℱ')`, where `j` is the canonical injection `X' → X`; one may replace
`X` by `X'` and `ℱ` by `ℱ'`, in other words suppose that `Supp(ℱ) = X`. Let then `y'` be a generization of `y` in `Y`;
one knows (2.3.4) that there is a generization `x'` of `x` in `X` such that `y' = f(x')`; one may moreover suppose that
`x'` is a generic point of an irreducible component of `f⁻¹(y')`; one has consequently
`dim(ℱ_{x'} ⊗_{𝒪_{y'}} k(y')) = 0`. By virtue of (6.1.2), one therefore has, setting `𝒢 = ℰ ⊗_Y ℱ`,

```text
  dim(𝒢_{x'}) = dim(ℰ_{y'})
```

and by virtue of (6.3.1)

```text
  prof(𝒢_{x'}) = prof(ℰ_{y'})
```

taking into account that depth is always at most equal to dimension. By hypothesis, one has

```text
  prof(𝒢_{x'}) ≥ inf(k, dim(𝒢_{x'}))
```

hence

```text
  prof(ℰ_{y'}) ≥ inf(k, dim(ℰ_{y'}))
```

which proves the first assertion.

<!-- original page 142 -->

(ii) Since for every generization `x'` of `x ∈ f⁻¹(y)`, `y' = f(x')` is a generization of `y`, one may restrict to
verifying that if `x ∈ Supp(ℱ)` and `f(x) = y`, one has `prof(𝒢_x) ≥ inf(k, dim(𝒢_x))`; it follows from (6.1.2) and
(6.3.1) that one has

```text
  dim(𝒢_x) = dim(ℰ_y) + dim(ℱ_x ⊗_{𝒪_y} k(y))
```

```text
  prof(𝒢_x) = prof(ℰ_y) + prof(ℱ_x ⊗_{𝒪_y} k(y)).
```

By hypothesis, one has

```text
  prof(ℰ_y) ≥ inf(k, dim(ℰ_y))
```

```text
  prof(ℱ_x ⊗_{𝒪_y} k(y)) ≥ inf(k, dim(ℱ_x ⊗_{𝒪_y} k(y)))
```

whence, adding term by term,

```text
  prof(𝒢_x) ≥ inf(k, dim(ℰ_y)) + inf(k, dim(ℱ_x ⊗_{𝒪_y} k(y))) ≥
            ≥ inf(k, dim(ℰ_y) + dim(ℱ_x ⊗_{𝒪_y} k(y))) = inf(k, dim(𝒢_x))
```

which proves (ii).

**Corollary (6.4.2).**

<!-- label: IV.6.4.2 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a flat morphism, `ℰ` a coherent `𝒪_Y`-Module. Suppose
that for every `y ∈ Y`, the prescheme `f⁻¹(y)` has property `(S_k)`. Then, for `f*(ℰ)` to satisfy `(S_k)` at a point
`x`, it is necessary and sufficient that `ℰ` have property `(S_k)` at the point `f(x)`.*

**Remark (6.4.3).**

<!-- label: IV.6.4.3 -->

Let `A`, `B` be two Noetherian local rings, `k` the residue field of `A`, `φ : A → B` a local homomorphism, `M` a
`B`-module of finite type which is a flat `A`-module, and suppose moreover that the `A`-module `A` and the
`(B ⊗_A k)`-module `M ⊗_A k` have property `(S_n)`; can one then conclude that the `B`-module `M` has property `(S_n)`?
We do not know this, even when `n = 1`, `M = B` and `B = Â`; in other words, we do not know whether in general the
completion of a Noetherian local ring satisfying `(S_n)` also satisfies `(S_n)`, even for `n = 1`. Setting
`Y = Spec(A)`, `X = Spec(B)` and `ℱ = M̃`, it would suffice, by virtue of (6.4.1, (ii)), to show that for every `y ∈ Y`,
`ℱ_y` has property `(S_n)` (and not only when `y` is the closed point of `Y`); it would also suffice to show that the
set `U` of `x ∈ X` such that `ℱ_x ⊗ k(f(x))` satisfies `(S_n)` is open in `X` (since it contains the closed point of `X`
by hypothesis). We shall show below (12.1.4) that `U` is open when `B` is a local ring of an `A`-algebra of finite type
and `M = B`. On the other hand, for `B = Â` and `M = B`, we saw in (6.3.8) that the preschemes `f⁻¹(y)` are
Cohen-Macaulay preschemes (in other words satisfy `(S_n)` for every `n`) when one supposes that `A` is a quotient of a
Cohen-Macaulay local ring. One concludes that when `A` is a quotient of a Cohen-Macaulay local ring (or more generally
of a local ring satisfying the hypotheses of (6.3.8)), for `A` to satisfy `(S_n)`, it is necessary and sufficient that
its completion `Â` satisfy `(S_n)`. It would remain to be seen whether this property persists without restriction on
`A`.

<!-- original page 143 -->

### 6.5. Flatness and property `(R_n)`

**Proposition (6.5.1).**

<!-- label: IV.6.5.1 -->

*Let `A`, `B` be two Noetherian local rings, `k` the residue field of `A`, `φ : A → B` a local homomorphism for which
`B` is a flat `A`-module. Then:*

*(i) If `B` is regular, `A` is regular.*

*(ii) If `A` and `B ⊗_A k` are regular, `B` is regular.*

This proposition is given for the record, having already been proved in (0, 17.3.3).

**Corollary (6.5.2).**

<!-- label: IV.6.5.2 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a flat morphism.*

*(i) If `X` is regular at a point `x`, `Y` is regular at the point `f(x)`.*

*(ii) If for `y ∈ f(X)`, `Y` is regular at the point `y` and if `f⁻¹(y)` is a prescheme regular at a point `x`, then `X`
is regular at the point `x`.*

**Proposition (6.5.3).**

<!-- label: IV.6.5.3 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a flat morphism.*

*(i) If `X` has property `(R_k)` at a point `x` (resp. if `X` has property `(R_k)`), `Y` has property `(R_k)` at the
point `f(x)` (resp. `Y` has property `(R_k)` at every point of `f(X)`).*

*(ii) Suppose that for every `y ∈ f(X)`, the prescheme `f⁻¹(y)` has property `(R_k)`; then, if for a point `y ∈ f(X)`,
`Y` has property `(R_k)` at the point `y`, `X` has property `(R_k)` at every point of `f⁻¹(y)`.*

(i) Set `y = f(x)` and let `y'` be a generization of `y`; as in the proof of (6.4.1), there is a generic point `x'` of
an irreducible component of `f⁻¹(y')` which is a generization of `x`; hence one has `dim(𝒪_{x'} ⊗_{𝒪_{y'}} k(y')) = 0`
and by virtue of the hypothesis and of (6.1.2), `dim(𝒪_{y'}) = dim(𝒪_{x'})`. The hypothesis entails either that
`dim(𝒪_x) > k`, in which case `dim(𝒪_{y'}) > k`, or that `𝒪_x` is a regular ring, and then `𝒪_{y'}` is a regular ring by
virtue of (6.5.1).

(ii) Since, for every generization `x'` of `x ∈ f⁻¹(y)`, `y' = f(x')` is a generization of `y`, one may restrict to
verifying that if `dim(𝒪_x) ≤ k`, then `𝒪_x` is a regular ring. Now, one has, by virtue of (6.1.2)

```text
  dim(𝒪_x) = dim(𝒪_y) + dim(𝒪_x ⊗_{𝒪_y} k(y))
```

hence if `dim(𝒪_x) ≤ k`, one has *a fortiori* `dim(𝒪_y) ≤ k` and `dim(𝒪_x ⊗_{𝒪_y} k(y)) ≤ k`, and the hypothesis entails
that `𝒪_y` and `𝒪_x ⊗_{𝒪_y} k(y)` are regular rings. One then concludes from (6.5.1) that `𝒪_x` is a regular ring.

**Corollary (6.5.4).**

<!-- label: IV.6.5.4 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a flat morphism.*

*(i) If `X` is normal at a point `x`, `Y` is normal at the point `f(x)`.*

*(ii) If, for every `y ∈ f(X)`, `f⁻¹(y)` is a normal prescheme and if `Y` is normal at a point `y ∈ f(X)`, then `X` is a
normal prescheme at every point of `f⁻¹(y)`.*

This follows at once from Serre's normality criterion (5.8.6) and from (6.4.1) applied for `k = 2` and (6.5.3) applied
for `k = 1`.

<!-- original page 144 -->

**Remarks (6.5.5).**

<!-- label: IV.6.5.5 -->

*(i)* Let `A`, `B` be two Noetherian local rings, `φ : A → B` a local homomorphism such that `B` is a flat `A`-module.
Let `k` be the residue field of `A`, and suppose that the two rings `A` and `B ⊗_A k` satisfy property `(R_i)` (5.8.2);
then it does *not* necessarily follow that `B` satisfies `(R_i)`, even in the particular case where `i = 0` or `i = 1`
and where `B` is the completion `Â` of `A`. Nagata has indeed given an example where `A` is normal (hence satisfies
`(R_1)`) but where `Â` is not even reduced (hence does not satisfy `(R_0)`) [30]. One cannot apply proposition (6.5.3)
to this case because the fibres `f⁻¹(y)` do not necessarily satisfy property `(R_i)` at points distinct from the closed
point of `Y = Spec(A)`. We shall however show below (7.8.3, (v)) that such phenomena do not occur for the Noetherian
local rings which one most often encounters in applications.

*(ii)* The property of being integral for a prescheme does not behave at all like the properties we have just examined
in this no. and the preceding ones: it can happen that `f : X → Y` is a flat morphism of finite type, that all the
fibres `f⁻¹(y)` are regular (and even geometrically regular (6.7.6)) and that `Y` is integral, without `X` being even
locally integral. For example, let `k` be an algebraically closed field of characteristic `0`, and let `A` be the
integral ring `k[U, V]/(UV − (U + V)³)` (whose spectrum is therefore a "cubic with a double point"); `A` is not
integrally closed, and if `u`, `v` are the canonical images of `U`, `V` in `A`, the integral closure of `A` is the ring
`C = A[t]`, with `t = (u − v)/(u + v)`, which satisfies the equation `t² = 1 + u + v`, whence one gets
`u = ½(t³ + t² − t)`, `v = ½(−t³ + t² + t)` and consequently `C = k[t]`, isomorphic to the ring of polynomials in one
indeterminate over `k`. If `𝔪 = Au + Av`, the maximal ideal of `A` (corresponding to the "double point" of the cubic),
there are two maximal ideals `𝔫_1`, `𝔫_2` of `C`, generated respectively by `t − 1` and `t + 1`. Let then `B` be the
sub-ring of the product `C × C` formed of the pairs of polynomials `(f, g)` such that `f(1) = g(−1)` and `f(−1) = g(1)`
(`Spec(B)` is the scheme obtained by "gluing" two copies of `Spec(C)`, the point `𝔫_1` (resp. `𝔫_2`) of one of the two
copies being "glued" to the point `𝔫_2` (resp. `𝔫_1`) of the other; cf. chap. V, where this operation will be discussed
in general). There are therefore two maximal ideals `𝔯_1`, `𝔯_2` of `B` above the maximal ideal `𝔪` of `A`. Moreover,
since the process of "gluing" commutes with localization and completion, one verifies easily that the canonical
homomorphisms `Â_𝔪 → B̂_{𝔯_1}` and `Â_𝔪 → B̂_{𝔯_2}` are bijective, and consequently (Bourbaki, *Alg. comm.*, chap. III,
§3, n° 5, prop. 10) `B_{𝔯_1}` and `B_{𝔯_2}` are flat `A_𝔪`-modules, having moreover the same residue field as `A_𝔪`. For
every other maximal ideal `𝔭` of `A`, it is immediate that there are two maximal ideals `𝔮_1`, `𝔮_2` of `B` above `𝔭`,
and that the homomorphisms `A_𝔭 → B_{𝔮_1}` and `A_𝔭 → B_{𝔮_2}` are bijective. One sees thus that the morphism
`Spec(B) → Spec(A)` is flat and finite, and that all its fibres are geometrically regular (it is even étale, as we shall
see later (17.6.3)); however it is immediate that `B` is not integral.

<!-- original page 145 -->

### 6.6. Transitivity properties

**Proposition (6.6.1).**

<!-- label: IV.6.6.1 -->

*For a locally Noetherian prescheme `Z`, denote by `P(Z)` any one of the following properties:*

*a) `Z` is a Cohen-Macaulay prescheme.*

*b) `Z` satisfies `(S_n)`.*

*c) `Z` is regular.*

*d) `Z` satisfies `(R_n)`.*

*e) `Z` is normal.*

*f) `Z` is reduced.*

*Let then `X`, `Y`, `Z` be three locally Noetherian preschemes, `f : X → Y`, `g : Y → Z` two morphisms.*

*(i) Suppose that `f` and `g` are flat and that for every `y ∈ f(X)` (resp. every `z ∈ g(Y)`), the prescheme `f⁻¹(y)`
(resp. `g⁻¹(z)`) satisfies `P`. Then `h = g ∘ f` is flat and for every `z ∈ h(X)`, `h⁻¹(z)` satisfies `P`.*

*(ii) Suppose the following conditions hold: `f` is faithfully flat, `h = g ∘ f` is flat, for every `y ∈ Y` the
prescheme `f⁻¹(y)` satisfies `P`, and for every `z ∈ h(X)` the prescheme `h⁻¹(z)` satisfies `P`. Then `g` is flat, and
for every `z ∈ g(Y)`, `g⁻¹(z)` satisfies `P`.*

(i) One already knows (2.1.6) that `h` is flat; on the other hand, for every `z ∈ Z`,
`f_z = f ⊗ 1_{k(z)} : h⁻¹(z) → g⁻¹(z)` is flat (2.1.4), and for every `y ∈ g⁻¹(z)`, `f_z⁻¹(y)` is isomorphic to `f⁻¹(y)`
by transitivity of fibres (I, 3.6.4). The conclusion then follows respectively from (6.3.5, (ii)), (6.4.2), (6.5.2,
(ii)), (6.5.3, (ii)), (6.5.4, (ii)) and (3.3.5, (ii)).

(ii) One already knows that `g` is flat (2.2.13); moreover, for every `z ∈ Z`, `f_z` is faithfully flat (2.2.13). The
conclusion then follows respectively from (6.3.5, (i)), (6.4.2), (6.5.2, (i)), (6.5.3, (i)), (6.5.4, (ii)) and (2.1.13).

**Remark (6.6.2).**

<!-- label: IV.6.6.2 -->

Suppose `h` flat, `f` faithfully flat, and suppose that for every `z ∈ Z`, `h⁻¹(z)` is of codepth `≤ n` (5.7.1); then it
follows from the reasoning of (6.6.1, (ii)) and from (6.3.2) that `g⁻¹(z)` is of codepth `≤ n` for every `z ∈ g(Y)` and
that for every `y ∈ Y`, `f⁻¹(y)` is of codepth `≤ n`.

### 6.7. Application to base changes in algebraic preschemes

**Proposition (6.7.1).**

<!-- label: IV.6.7.1 -->

*Let `k` be a field, `X` a locally Noetherian `k`-prescheme, `ℱ` a coherent `𝒪_X`-Module. Let `k'` be an extension of
`k`; set `X' = X ⊗_k k'`, `ℱ' = ℱ ⊗_k k'` and let `p : X' → X` be the canonical projection. Suppose either that `X` is
locally of finite type over `k`, or that `k'` is an extension of finite type of `k`, so that in both cases `X'` is
locally Noetherian. Let `x'` be a point of `X'`, `x = p(x')`. Then:*

*(i) One has `coprof(ℱ_x) = coprof(ℱ'_{x'})`; in particular, for `ℱ_x` to be a Cohen-Macaulay `𝒪_x`-module, it is
necessary and sufficient that `ℱ'_{x'}` be a Cohen-Macaulay `𝒪_{x'}`-module.*

*(ii) For `ℱ` to satisfy property `(S_n)` at the point `x`, it is necessary and sufficient that `ℱ'` satisfy `(S_n)` at
the point `x'`.*

<!-- original page 146 -->

One knows that `p` is faithfully flat (2.2.13); the two assertions are therefore respective consequences of (6.3.2) and
(6.4.2), provided one proves that `p⁻¹(x) = Spec(k(x) ⊗_k k')` is a Cohen-Macaulay prescheme; since one of the two
fields `k(x)`, `k'` is an extension of finite type of `k` by hypothesis, one is reduced to proving the

**Lemma (6.7.1.1).**

<!-- label: IV.6.7.1.1 -->

*Let `K`, `L` be two extensions of a field `k`, one of which is of finite type (so that the ring `K ⊗_k L` is
Noetherian). Then `K ⊗_k L` is a Cohen-Macaulay ring.*

Suppose for example that `L` is an extension of finite type of `k`, so that `L` is a finite extension of a pure
extension `k(𝐭)` of `k` (`𝐭` being a system `(t_i)_{1 ≤ i ≤ m}` of indeterminates). If one sets `A = K ⊗_k k(𝐭)`,
`B = K ⊗_k L`, `B` is a flat `A`-module (0_I, 6.2.1) and of finite type; the morphism `h : Spec(B) → Spec(A)` is hence
finite, and since every Artinian prescheme is Cohen-Macaulay, to prove that `B` is a Cohen-Macaulay ring, it suffices to
prove that `A` is a Cohen-Macaulay ring (6.3.5). Now, if `S` is the set of elements `≠ 0` of `k[𝐭]`, one has
`A = S⁻¹A'`, where `A' = K ⊗_k k[𝐭] = K[𝐭]`; by virtue of (0, 16.5.13), it suffices to prove that `A'` is a Cohen-
Macaulay ring; but this follows from the fact that `A'` is regular (0, 17.3.7).

**Corollary (6.7.2).**

<!-- label: IV.6.7.2 -->

*For `𝒪_x` to be a Cohen-Macaulay ring (resp. for `X` to satisfy `(S_n)` at the point `x`), it is necessary and
sufficient that `𝒪_{x'}` be a Cohen-Macaulay ring (resp. that `X'` satisfy `(S_n)` at the point `x'`).*

**Corollary (6.7.3).**

<!-- label: IV.6.7.3 -->

*Let `X`, `Y` be two locally Noetherian `k`-preschemes, at least one of which is locally of finite type over `k`. Let
`ℱ` (resp. `𝒢`) be a coherent `𝒪_X`-Module (resp. a coherent `𝒪_Y`-Module). If `ℱ` and `𝒢` satisfy property `(S_n)`, so
does `ℱ ⊗_k 𝒢`.*

The hypothesis entails that `X ×_k Y` is locally Noetherian; let `p : X ×_k Y → X` and `q : X ×_k Y → Y` be the
canonical projections, which are flat morphisms. Suppose for example that `X` is locally of finite type over `k`; one
may write `ℱ ⊗_k 𝒢 = p*(ℱ) ⊗_{𝒪} q*(𝒢)`, and since `ℱ` is flat relative to the structure morphism `X → Spec(k)`, `p*(ℱ)`
is `q`-flat (2.1.4). Apply criterion (6.4.1, (ii)) to the morphism `q`; it suffices to see that for every `y ∈ Y`,
`p*(ℱ) ⊗_{𝒪_y} k(y)` has property `(S_n)`; but `p*(ℱ) ⊗_{𝒪_y} k(y) = ℱ ⊗_k k(y)`, and since `X` is locally of finite
type over `k`, the conclusion follows from (6.7.1, (ii)).

**Proposition (6.7.4).**

<!-- label: IV.6.7.4 -->

*For a locally Noetherian prescheme `Z`, and a point `z ∈ Z`, let `P(Z, z)` be one of the following properties:*

*a) `Z` is regular at the point `z`.*

*b) `Z` satisfies `(R_n)` at the point `z`.*

*c) `Z` is normal at the point `z`.*

*d) `Z` is reduced at the point `z`.*

*This being so, under the hypotheses and with the notation of (6.7.1), if `P(X', x')` is true, so is `P(X, x)`. The
converse is true if `k'` is a separable extension of `k`.*

The case where `P` is property *d)* has been listed only for the record, having already been treated (2.1.13 and 4.6.1).
The same reasoning as at the start of (6.7.1) shows that the first assertion follows respectively from (6.5.2, (i)),
(6.5.3, (i)) and (6.5.4, (i)); likewise, the second assertion will follow from (6.5.2, (ii)), (6.5.3, (ii)) and (6.5.4,
(ii))

<!-- original page 147 -->

provided one proves that `p⁻¹(x)` is a regular prescheme; in other words, one is reduced to proving the

**Lemma (6.7.4.1).**

<!-- label: IV.6.7.4.1 -->

*Let `K`, `L` be two extensions of a field `k`, one of which is of finite type. If `L` is a separable extension of `k`,
the ring `K ⊗_k L` is regular.*

Let us distinguish two cases:

*A)* `L` is an extension of finite type of `k`. Then, with the notation of (6.7.1.1), one may suppose that `L` is a
finite separable extension of `k(𝐭)`. For every `s ∈ Spec(A)`, `k(s) ⊗_{k(𝐭)} L` is then a direct composite of a finite
number of fields, finite separable extensions of `k(s)`, hence a regular ring; it follows then from (6.5.2, (ii)) that
it suffices to prove that the ring `A` is regular; since `A = S⁻¹A'`, it suffices to prove that `A'` is regular (0,
17.3.6); but it was seen that this was indeed so in the proof of (6.7.1.1).

*B)* Let `(L_λ)` be the filtered family of sub-extensions of `L` which are of finite type over `k`; by virtue of *A)*,
each of the rings `C_λ = K ⊗_k L_λ` is regular; on the other hand, for `L_λ ⊂ L_μ`, `L_μ` is a flat `L_λ`-module, hence
`C_μ` is a flat `C_λ`-module (0_I, 6.2.1). Since `C = K ⊗_k L = lim⃗(K ⊗_k L_λ)` is Noetherian, one may apply (5.13.7),
and `C` is therefore regular.

**Remarks (6.7.5).**

<!-- label: IV.6.7.5 -->

*(i)* In the proof of the fact that `P(X, x)` entails `P(X', x')`, one cannot dispense with the hypothesis that `k'` is
a separable extension of `k`. This has already been seen (4.6.1) when `P` is property *d)*; but even when `X` is
geometrically integral (4.6.2), it can happen that `X` is regular without `X'` being normal.

Take for example `X` to be a normal algebraic curve over `k` (II, 7.4.2); the local rings of `X` being integrally closed
and of dimension `1` are discrete valuation rings, hence regular (II, 7.1.6), and `X` is therefore a regular `k`-scheme
(and *a fortiori* satisfies `(R_n)` for every `n ≥ 0`). To say that `X` is geometrically integral means then that the
field `K` of rational functions on `X` is a separable and primary extension of `k` (4.6.3). Now, take `k` to be a
non-perfect field of characteristic `p > 2`, and let `a ∈ k` be an element not belonging to `k^p`. Let `B` be the
polynomial ring `k[S, T]` in two indeterminates `S`, `T`; the polynomial `P(S, T) = T² − S^p + a` is irreducible in `B`,
for one verifies at once that `S^p − a` is not a square in the ring `k[S]`; hence `X = Spec(A)`, where `A = B/PB`, is an
irreducible affine curve over `k`. To see that the scheme `X` is regular, it suffices to show that it is normal (II,
7.4.5); now `A = k[S][t]`, where `t` is a root of the polynomial `P` regarded as a polynomial in `T` over `k[S]`, so
that the field `K = R(X)` of rational functions on `X` is the field of fractions `k(S)[T]/(P)` of `A`, a quadratic
extension of `k(S)`, hence separable over `k(S)`, and *a fortiori* over `k`. Since `2` is invertible in `k`, one
verifies at once that `A` is the integral closure of `k[S]` in `K`, hence is integrally closed, which shows that `X` is
regular. Moreover, if an element `f + tg` of `K` (with `f`, `g` in `k(S)`) is algebraic over `k`, so are its norm and
its trace over `k(S)`, and since `k(S)` is a pure extension of `k`, one concludes easily that one must have `f ∈ k` and
`g = 0`, in other words `k` is algebraically closed in `K`, and *a fortiori* `K` is a primary extension

<!-- original page 148 -->

of `k` (4.3.1). However, if `k' = k(a^{1/p})`, `X' = X ⊗_k k'` is not normal, for in `k'[S]` one may write
`S^p − a = (S − a^{1/p})^p`, and `X'` is therefore isomorphic to `Spec(A')`, where `A' = k'[S][t']`, `t'` being a root
of the polynomial `T² − S^p`. Now, `A'` is not integrally closed, for the element `t'' = t'/S` of the field of fractions
`K' = k'(S)[t']` of `A'` satisfies the integral dependence equation `t''² − S^{p−2} = 0` over `A'` and does not belong
to `A'`. In the classical theory, this is expressed by saying that the "genus" over `k'` of the field `K'` of rational
functions of `X'` is *strictly less* than that of `K` over `k`.

*(ii)* As recalled in (i), it follows from (4.6.1) that when `X` is an algebraic prescheme over `k` that is not
geometrically reduced, there are finite radicial extensions `k'` of `k` such that `X' = X ⊗_k k'` is not reduced. It is
interesting to give an example of this fact where `X` is a *regular* scheme over `k`, such that `k` is *algebraically
closed* in the field `K` of rational functions of `X`. Let `k` be a field of characteristic `p > 0`, in which there
exist two elements `a`, `b` forming a `p`-free family over `k^p`. Again denoting by `B` the ring `k[S, T]`, let us
consider this time the polynomial `P(S, T) = T^p − aS^p − b`; since `aS^p + b` is not a `p`-th power in `k(S)`, `P` is
irreducible as a polynomial of `k(S)[T]`, and the scheme `X_0 = Spec(B/PB)` is therefore an integral affine curve over
`k`, whose field of rational functions is `K = k(S)[t]`, where `t` is a root of `P`; let us show that `k` is
algebraically closed in `K`. Suppose indeed that `K` contains an element `z` algebraic over `k` and not in `k`; one
would then also have `z ∉ k(S)`, hence `[k(S)[z] : k(S)] > 1`; since `[K : k(S)] = p`, one would have `K = k(S)[z]`, and
since `K` is radicial over `k(S)`, one would have `z^p ∈ k(S)`, hence `c = z^p ∈ k` since `z` is algebraic over `k`; but
one would have `t^p = aS^p + b ∈ k^p(S^p)(c)` hence `a` and `b` would belong to `k^p(c)`, which is absurd. Let then `X`
be the normalization of the curve `X_0` in `K`, which is therefore a normal (and consequently regular) curve over `k`.
If `k' = k(a^{1/p}, b^{1/p})`, it is clear that `aS^p + b` is a `p`-th power in `k'(S)`, hence `K ⊗_k k'` is not
reduced, nor *a fortiori* the scheme `X ⊗_k k'`.

**Definition (6.7.6).**

<!-- label: IV.6.7.6 -->

*Let `k` be a field, `X` a locally Noetherian `k`-prescheme. We say that `X` is **geometrically regular at a point `x`**
(resp. **has the geometric property `(R_n)` at a point `x`**, resp. is **geometrically normal at a point `x`**) if, for
every finite extension `k'` of `k`, `X' = X_{(k')} = X ⊗_k k'` is regular (resp. has property `(R_n)`, resp. is normal)
at every point `x'` whose projection in `X` is `x`. We say that `X` is **geometrically regular** (resp. **has the
geometric property `(R_n)`** (or also is **geometrically regular in codimension `≤ n`**), resp. is **geometrically
normal**) if `X` is geometrically regular (resp. has the geometric property `(R_n)`, resp. is geometrically normal) at
every point.*

*We say that an algebra `A` over `k` is a **geometrically regular ring** (resp. **geometrically normal**, resp.
**geometrically reduced**, resp. **having the geometric property `(R_n)`**) if `Spec(A)` has the same property.*

If `X = Spec(K)`, where `K` is an extension of `k`, it amounts to the same to say that `X` is geometrically regular, or
geometrically normal, or geometrically reduced, or that `K` is a separable extension of `k`: this follows from (4.6.1)
and from the fact that if `K` is a separable extension of `k` and `k'` a finite extension of `k`, `K ⊗_k k'` is a direct
composite of a finite number of fields (Bourbaki, *Alg.*, chap. VIII, §7, n° 3, cor. 1 of th. 1).

<!-- original page 149 -->

**Proposition (6.7.7).**

<!-- label: IV.6.7.7 -->

*Let `k` be a field, `X` a locally Noetherian `k`-prescheme, `x` a point of `X`; denote by `Q(k')` the relation "`k'` is
an extension of `k`, and `P(X_{(k')}, x')` is true for every point `x'` of `X_{(k')}` whose projection in `X` is `x`",
where `P(Z, z)` is one of the properties a), b), c) of the statement (6.7.4). Then the following properties are
equivalent:*

*a) `Q(k')` is true for every finite extension `k'` of `k`.*

*b) `Q(k')` is true for every finite radicial extension `k'` of `k`.*

*c) `Q(k')` is true for every extension of finite type `k'` of `k`.*

*Suppose moreover that `X` is locally of finite type over `k`; then the three preceding properties are also equivalent
to the following:*

*d) `Q(k')` is true for every extension `k'` of `k`.*

*e) `Q(k')` is true for a perfect extension `k'` of `k`.*

*f) `Q(k')` is true for every extension `k' = k^{p^{−s}}`, where `p` is the characteristic exponent of `k`, and
`s > 0`.*

To prove the equivalence of a), b) and c), it suffices evidently to establish that b) entails c). So let `K` be an
extension of finite type of `k`, which is therefore the field of fractions of a `k`-algebra of finite type `A`; set
`Y = Spec(A)`. One knows (4.6.6) that there exists a finite radicial extension `k'` of `k` such that
`Y' = (Y ⊗_k k')_{red}` is separable over `k'`; if `η'` is the generic point of `Y'`, `K' = k(η')` is a separable
extension of `k'` by (4.6.1). This being so, `P(X_{(k')}, x')` is true by hypothesis for every point `x'` of `X_{(k')}`
above `x`, hence it follows from (6.7.4) that `P(X_{(K')}, x'')` is true for every point `x''` of `X_{(K')}` above `x`,
since `X_{(K')} = (X_{(k')})_{(K')}`, since `x''` is above a point `x'` of `X_{(k')}`, itself above `x`, and since `K'`
is separable over `k'`. But one also has `X_{(K')} = (X_{(K)})_{(K')}` and for every `x_0 ∈ X_{(K)}` above `x`, there
exists `x'' ∈ X_{(K')}` above `x_0`; it follows then from (6.7.4) that `P(X_{(K)}, x_0)` is true.

Suppose now `X` locally of finite type over `k`, so that for every extension `K` of `k`, `X_{(K)}` is locally
Noetherian. Since a radicial extension of `k` is isomorphic to a sub-extension of an arbitrary perfect extension of `k`,
it follows at once from (6.7.4) that e) implies f); likewise, every finite radicial extension of `k` is contained in an
extension `k^{p^{−s}} ⊂ k^{p^{−∞}}`, hence f) entails b); d) trivially entails e), and finally e) entails d). Indeed, if
`K` is any extension of `k`, there exists an extension `K'` of `k` containing (up to `k`-isomorphism) `k'` and `K`;
since `K'` is a separable extension of `k'`, one deduces from (6.7.4) that `Q(k')` is true, then that `Q(K)` is true,
reasoning as in the first part of the proof. It therefore suffices to prove that b) entails e). We shall take
`k' = k^{p^{−∞}}` in e).

The question being local on `X`, one may moreover restrict to the case where `X` is affine and of finite type over `k`,
replacing `X` by a neighbourhood of `x`; so let `X = Spec(B)`, where `B` is a `k`-algebra of finite type; moreover, by
definition of property `P` in the cases considered, one may also replace `X` by the local scheme of `X` at the point
`x`, hence suppose that `B` is a Noetherian local ring. Set `B' = B ⊗_k k'`; `k'` is the inductive limit of its finite
sub-extensions `k'_λ`, and if one sets `B'_λ = B ⊗_k k'_λ`, the morphism `f_λ : Spec(B') → Spec(B'_λ)` is a
homeomorphism of `Spec(B')` onto `Spec(B'_λ)` for every `λ`;

<!-- original page 150 -->

indeed `f_λ` is bijective by virtue of (I, 3.5.2, 3.5.7 and 3.5.8); on the other hand, it is closed by (II, 6.1.10). One
may now apply (5.13.6), which proves (by virtue of hypothesis b)) that b) entails e) when `P(Z, z)` is property `(R_n)`
at the point `z`. The case where `P(Z, z)` is the property of being regular (i.e. of having property `(R_n)` for every
`n`) follows trivially. Finally, taking into account Serre's normality criterion (5.8.6), b) entails again e) when
`P(Z, z)` is the property of being normal at the point `z`, for this amounts to saying that `Z` has at the point `z`
properties `(S_2)` and `(R_1)`: one applies then what precedes for `n = 1`, and (6.7.2, (ii)) for `n = 2`.

**Corollary (6.7.8).**

<!-- label: IV.6.7.8 -->

*Let `k` be a field; for a locally Noetherian `k`-prescheme `X` and a point `x ∈ X`, denote by `P(X, x)` one of the
following properties:*

*(i) `coprof(𝒪_x) ≤ n`.*

*(ii) `𝒪_x` is a Cohen-Macaulay ring.*

*(iii) `X` satisfies property `(S_n)` at the point `x`.*

*(iv) `X` is geometrically regular at the point `x`.*

*(v) `X` has the geometric property `(R_n)` at the point `x`.*

*(vi) `X` is geometrically normal at the point `x`.*

*(vii) `X` is geometrically reduced (i.e. separable) at the point `x`.*

*Let `k'` be an extension of `k`; suppose either that `k'` is of finite type, or that `X` is locally of finite type over
`k`, so that `X' = X ⊗_k k'` is locally Noetherian. Let `x'` be a point of `X'` whose projection in `X` is `x`. Then,
for `P(X, x)` to be true, it is necessary and sufficient that `P(X', x')` be so.*

This has already been seen for property (vii) (4.6.11), and for properties (i), (ii) and (iii) (6.7.1). For (iv), (v)
and (vi), it follows from (6.7.7): indeed, the fact that the condition is necessary follows from the equivalence of the
criteria a) and c), and from the equivalence of c) and d) when `X` is locally of finite type over `k`. To see that the
condition is sufficient, let `k''` be a finite radicial extension of `k`; one may always regard `k'` and `k''` as
sub-extensions of an extension `K` of `k`; set `X'' = X ⊗_k k''`, `X_0 = X ⊗_k K`, and note that since `k''` is a
radicial extension of `k`, there is only *one* point `x''` of `X''` above `x` (I, 3.5.7 and 3.5.8). Let then `x_0` be
any point of `X_0` above `x'`; if `P(X', x')` is true, so is `P(X_0, x_0)` by virtue of (6.7.7, c) and d)) (for if `k'`
is an extension of `k` of finite type, one may suppose that `K` is too, and if `X` is locally of finite type over `k`,
`X'` is locally of finite type over `k'`). One then deduces from (6.7.4) that property `Q(k'')` is true (with the
notation of (6.7.7)), hence `P(X, x)` is true by (6.7.7, b)).

### 6.8. Regular, normal, reduced, smooth morphisms

**Definition (6.8.1).**

<!-- label: IV.6.8.1 -->

*Let `X`, `Y` be two preschemes, `f : X → Y` a morphism such that the fibre `f⁻¹(y)` is a locally Noetherian prescheme
for every `y ∈ Y`, `x` a point of `X`. We say respectively that `f` is a morphism:*

*(i) **of codepth `≤ n` at the point `x`**;*

*(ii) **Cohen-Macaulay at the point `x`**;*

<!-- original page 151 -->

*(iii) **`(S_n)` at the point `x`**;*

*(iv) **regular at the point `x`**;*

*(v) **`(R_n)` at the point `x`**;*

*(vi) **normal at the point `x`**;*

*(vii) **reduced at the point `x`**;*

*if `f` is flat at the point `x`, and if in addition the corresponding property `P(f⁻¹(f(x)), x)` (notation of (6.7.8))
is true.*

*We say that `f` is **smooth at the point `x`** if it is locally of finite presentation in a neighbourhood of `x` in
`X`, and if it is regular at the point `x`. We say respectively that `f` is a morphism: **of codepth `≤ n`, Cohen-
Macaulay, `(S_n)`, regular, `(R_n)`, normal, reduced, smooth**, if it has the corresponding property at every point of
`X`.*

**Proposition (6.8.2).**

<!-- label: IV.6.8.2 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a morphism, `x` a point of `X`. Designate by `M(f, x)`
one of the properties (i) to (vii) of definition (6.8.1), or the property for `f` of being smooth at the point `x`. Let
`Y'` be a locally Noetherian prescheme, `g : Y' → Y` a morphism, `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`. One
supposes that `f` or `g` is locally of finite type. Then, for every `x' ∈ X'` above `x`, the property `M(f, x)` entails
`M(f', x')`.*

Set `y = f(x)`, `y' = f'(x')`; by transitivity of fibres (I, 3.6.4), one has `f'⁻¹(y') = f⁻¹(y) ⊗_{k(y)} k(y')`; since
either `f⁻¹(y)` is locally of finite type over `k(y)`, or `k(y')` is of finite type over `k(y)` (I, 6.4.11), it follows
from (6.7.8) that the properties `P(f⁻¹(y), x)` and `P(f'⁻¹(y'), x')` are equivalent; moreover, if `f` is flat at the
point `x`, `f'` is flat at the point `x'` (2.1.4), which proves the proposition, in view of (1.4.3, (iii)).

**Proposition (6.8.3).**

<!-- label: IV.6.8.3 -->

*For a morphism `f` of locally Noetherian preschemes, let `M(f)` denote one of the following properties: being Cohen-
Macaulay, `(S_n)`, regular, `(R_n)`, normal, reduced.*

*(i) Let `X`, `Y`, `Z` be three locally Noetherian preschemes, `f : X → Y`, `g : Y → Z` two morphisms. If `M(f)` and
`M(g)` are true, `M(g ∘ f)` is true.*

*(ii) Conversely, if `f` is surjective and if `M(f)` and `M(g ∘ f)` are true, then `M(g)` is true.*

*(iii) Let `X`, `Y`, `Y'` be three locally Noetherian preschemes, `f : X → Y`, `h : Y' → Y` two morphisms; set
`X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`. Suppose that `f` or `h` is locally of finite type. Then, if `M(f)` is true,
so is `M(f')`; the converse is true when `h` is faithfully flat.*

*The conclusions of (i) and (iii) remain true when `M` is the property of being smooth and (in (iii)) `h` is
quasi-compact.*

(i) One already knows that if `f` and `g` are flat, so is `u = g ∘ f`, and that if `f` and `g ∘ f` are flat and `f`
surjective, `g` is flat (2.1.6 and 2.2.13). On the other hand, for every `z ∈ Z`, the morphism
`f_z = f ⊗ 1_{k(z)} : u⁻¹(z) → g⁻¹(z)` is flat (resp. faithfully flat if `f` is) and for every `y ∈ g⁻¹(z)`, `f_z⁻¹(y)`
is isomorphic to `f⁻¹(y)` (I, 3.6.4). If `M(f)` and `M(g)` are true, `M(g ∘ f)` is therefore true for the cases where
`M` is the property of being Cohen-Macaulay or `(S_n)`, by virtue of (6.6.1). On the other hand let `k'` be a finite
extension of `k(z)`; set `Y'_z = g⁻¹(z) ⊗_{k(z)} k'`, `X'_z = u⁻¹(z) ⊗_{k(z)} k'`, and
`f'_z = f_z ⊗ 1_{k'} : X'_z → Y'_z`; the morphism `f'_z`

<!-- original page 152 -->

is flat (resp. faithfully flat) and for every `y' ∈ Y'_z`, the fibre `f'_z⁻¹(y')` is isomorphic to
`f⁻¹(y) ⊗_{k(y)} k(y')`, designating by `y` the image of `y'` in `g⁻¹(z)` (I, 3.6.4). When `M` is the property of being
regular, `(R_n)`, normal or reduced, the hypothesis that `M(f)` and `M(g)` are true entails that `Y'_z` and each of the
fibres `f'_z⁻¹(y')` have for `y' ∈ Y'_z` the corresponding property among the properties c), d), e), f) of (6.6.1); one
deduces from (6.6.1, (i)) that `X'_z` has the same property, hence `M(g ∘ f)` is true.

(ii) Conversely, the hypothesis that `M(g ∘ f)` and `M(f)` are true and that `f` is surjective entails that `Y'_z` has
the corresponding property by virtue of (6.6.1, (ii)), `f'_z` being surjective for every `z`; hence `M(g)` is true.

(iii) The first assertion follows at once from (6.8.2). On the other hand, if `h` is faithfully flat and `f'` flat, `f`
is flat (2.4.1); since, with the notation of (6.8.2), the properties `P(f⁻¹(y), x)` and `P(f'⁻¹(y'), x')` are equivalent
(6.7.8), one sees that `M(f)` and `M(f')` are then equivalent.

Finally, the last assertion of the proposition follows from (1.4.3, (iii)) and from (2.7.1, (iv)).

**Remarks (6.8.4).**

<!-- label: IV.6.8.4 -->

*(i)* If `f` is faithfully flat, `g` flat and if `g ∘ f` is of codepth `≤ n`, then `g` is of codepth `≤ n`, as follows
from (6.6.2).

*(ii)* When, in (6.8.1), one takes for `Y` the spectrum of a field `k`, the notions (iv), (v) and (vi) reduce to those
defined in (6.7.5). It is clear that the latter are relative to the base field `k`. Definition (6.8.1) then leads to
saying that a prescheme `X` is "regular (resp. `(R_n)`, resp. normal) over `k`" instead of saying that it is
"geometrically regular (resp. `(R_n)`, resp. normal) relative to `k`"; one will take care not to confuse this notion
with the property of being regular (resp. `(R_n)`, resp. normal) which is independent of `k`. The same remarks apply
here as in (4.5.12).

**Proposition (6.8.5).**

<!-- label: IV.6.8.5 -->

*Let `k` be a field, `X`, `Y` two locally Noetherian `k`-preschemes, one of which is locally of finite type over `k`.
For a `k`-prescheme `Z`, designate by `P(Z)` one of the properties c) to f) of (6.6.1); the property "geometric `P(Z)`"
is then defined in (6.7.6) (resp. (4.6.1)) when `P(Z)` is one of the properties c), d), e) (resp. f)) of (6.6.1). Then:*

*(i) If `X` has property `P`, and `Y` has the geometric property `P`, `X ×_k Y` has property `P`.*

*(ii) If `X` and `Y` have the geometric property `P`, so does `X ×_k Y`.*

Let indeed `f : X ×_k Y → X`, `g : X → Spec(k)` be the structure morphisms, which are faithfully flat (2.2.13). The
hypothesis that `Y` has the geometric property `P` entails by virtue of (6.8.2) that `M(f)` is true, `M` being the
property of (6.8.3) which corresponds to `P`; under hypothesis (ii), `M(g)` is also true, hence assertion (ii) follows
from (6.8.3, (i)). As to assertion (i), it follows directly from (6.6.1, (i)).

**Theorem (6.8.6).**

<!-- label: IV.6.8.6 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a morphism locally of finite type, `x` a point of `X`,
`y = f(x)`. The following properties are equivalent:*

*a) `f` is smooth at the point `x`.*

*b) `f` is regular at the point `x`.*

<!-- original page 153 -->

*c) `𝒪_x` is a formally smooth `𝒪_y`-algebra (0, 19.3.1) for the preadic topologies on `𝒪_x` and `𝒪_y`.*

*c') `𝒪_x` is a formally smooth `𝒪_y`-algebra (0, 19.3.1) for the discrete topologies on `𝒪_x` and `𝒪_y`.*

The equivalence of a) and b) follows from definitions (6.8.1) and from the fact that for locally Noetherian preschemes,
morphisms locally of finite type are locally of finite presentation (1.4.2).

In the second place, for `𝒪_x` to be a formally smooth `𝒪_y`-algebra for the preadic topologies, it is necessary and
sufficient that `𝒪_x` be a flat `𝒪_y`-module and that `𝒪_x ⊗_{𝒪_y} k(y)` be a formally smooth `k(y)`-algebra for its
preadic topology (0, 19.7.1); but for `𝒪_x ⊗_{𝒪_y} k(y)` to be a formally smooth `k(y)`-algebra for its preadic
topology, it is necessary and sufficient that it be a geometrically regular `k(y)`-algebra (0, 19.6.6); this therefore
proves the equivalence of b) and c). Finally, to prove the equivalence of c) and c'), one may restrict to the case where
`Y = Spec(A)` and `X = Spec(C)` are affine, `A` being Noetherian and `C` an `A`-algebra of finite type, that one may
therefore write in the form `A[T_1, …, T_n]/𝔍`. Since here `𝔍/𝔍²` is a `C`-module of finite presentation, the
equivalence of c) and c') follows from (0, 22.6.4) applied to `A`, `B = A[T_1, …, T_n]` and `C = B/𝔍`.

**Corollary (6.8.7).**

<!-- label: IV.6.8.7 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a morphism locally of finite type. Then the set of
points `x ∈ X` where `f` is smooth (or regular) is open in `X`.*

It follows indeed from (0, 22.6.5) that the set of `x ∈ X` satisfying condition c') of (6.8.6) is open in `X`, and one
concludes by (6.8.6).

**Remark (6.8.8).**

<!-- label: IV.6.8.8 -->

In (17.5.1), we shall show that the equivalence of b) and c') in (6.8.6), as well as corollary (6.8.7), remain valid
without Noetherian hypothesis on `X` and `Y`, provided one restricts to morphisms locally of finite presentation.

### 6.9. The generic flatness theorem

**Theorem (6.9.1).**

<!-- label: IV.6.9.1 -->

*Let `Y` be a locally Noetherian and integral prescheme, `u : X → Y` a morphism of finite type, `ℱ` a coherent
`𝒪_X`-Module. There exists then a non-empty open set `U` of `Y` such that `ℱ|u⁻¹(U)` is flat over `U`.*

One may evidently restrict to the case where `Y = Spec(A)` is affine; then `X` is a finite union of affine open sets
`X_i` of finite type over `Y`; if, for each `i`, there is a non-empty open set `U_i` in `Y` such that
`ℱ|(X_i ∩ u⁻¹(U_i))` is flat over `U_i`, it is clear that taking for `U` the intersection of the `U_i` will answer the
question; one may therefore suppose that `X = Spec(B)`, where `B` is an `A`-algebra of finite type. One has then
`ℱ = M̃`, where `M` is a `B`-module of finite type; the theorem will follow from the

**Lemma (6.9.2).**

<!-- label: IV.6.9.2 -->

*Let `A` be a Noetherian integral ring, `B` an `A`-algebra of finite type, `M` a `B`-module of finite type. Then there
exists `f ≠ 0` in `A` such that `M_f` is a free `A_f`-module.*

Designate by `K` the field of fractions of `A`; then `B ⊗_A K` is an algebra of finite type over `K` and `M ⊗_A K` a
`(B ⊗_A K)`-module of finite type. We shall reason by induction

<!-- original page 154 -->

on the dimension `n` of the support of `M ⊗_A K`, which is `−∞` or finite and `≥ 0`. Suppose first `n = −∞`, that is to
say `M ⊗_A K = 0`; if `(m_i)_{1 ≤ i ≤ r}` is a system of generators of the `B`-module `M`, there exists therefore an
`f ≠ 0` in `A` such that `fm_i = 0` for `1 ≤ i ≤ r`; hence `M_f = 0` and the lemma is true in this case. Suppose now
`n ≥ 0`. One knows that there exists a composition series `M = M_1 ⊃ M_2 ⊃ ⋯ ⊃ M_q = 0` of the `B`-module `M` such that
each of the quotients `N_i = M_i/M_{i+1}` is isomorphic to a `B`-module of the form `B/𝔭_i`, where `𝔭_i` is a prime
ideal of `B` (Bourbaki, *Alg. comm.*, chap. IV, §1, n° 4, th. 1). If the theorem is true for each of the `N_i`, there is
for each `i` an `f_i ≠ 0` in `A` such that `(N_i)_{f_i}` is free over `A_{f_i}`; setting `f = f_1 f_2 ⋯ f_{q−1}`, it
follows that `(N_i)_f` is a free `A_f`-module for `1 ≤ i ≤ q − 1`. But `(N_i)_f = (M_i)_f/(M_{i+1})_f` (0_I, 1.3.2) and
since an extension of free modules is free, one then deduces that `M_f` is a free `A_f`-module. Replacing `B` by `B/𝔭`
(`𝔭` prime ideal of `B`), which is still of finite type over `A`, one sees that one may restrict to the case where
`M = B` and `B` is integral. One then knows (Bourbaki, *Alg. comm.*, chap. V, §3, n° 1, cor. 1 of th. 1) that there
exists an element `g ≠ 0` in `A` and elements `t_i` (`1 ≤ i ≤ m`) of `B`, algebraically independent over `A` and such
that `B_g` is integral over `A_g[t_1, …, t_m]`. One may replace `A` by `A_g`, `B` by `B_g`, and consequently suppose
that `B` is integral over `C = A[t_1, …, t_m]`, hence a `C`-module of finite type and torsion-free. One also knows
(4.1.2) that the dimension of `Spec(B ⊗_A K)` is equal to `m`, hence one has `m = n`.

This being so, if `h` is the rank of the torsion-free `C`-module `B`, there exists an exact sequence of `C`-modules

```text
  0 → C^h → B → M' → 0
```

where `M'` is a torsion `C`-module of finite type; the support of `M'` does not therefore contain the generic point of
`Spec(C)` (I, 7.4.6) and consequently the support of `M' ⊗_A K` does not contain the generic point of `Spec(C ⊗_A K)`
(I, 9.1.13.1); one concludes (4.1.2.1) that its dimension is `< n`. By virtue of the inductive hypothesis, there exists
an `f ≠ 0` in `A` such that `M'_f` is a free `A_f`-module; moreover `C_f^h` is a free `A_f`-module; so likewise is
`B_f`, which by virtue of (0_I, 1.3.2) is an extension of free modules. Q.E.D.

**Corollary (6.9.3).**

<!-- label: IV.6.9.3 -->

*Let `S` be a Noetherian prescheme, `u : X → S` a morphism of finite type, `ℱ` a coherent `𝒪_X`-Module. There exists
then a partition `(S_i)_{1 ≤ i ≤ n}` of `S` into a finite number of locally closed sets in `S`, such that, if one
denotes again by `S_i` the reduced sub-prescheme of `S` having `S_i` as underlying space, and if one sets
`X_i = X ×_S S_i`, the `𝒪_{X_i}`-Module `ℱ_i = ℱ ⊗_{𝒪_S} 𝒪_{S_i}` is flat over `S_i`.*

We proceed by Noetherian induction (0_I, 2.2.2) on the set of closed subsets `T` of `S` such that the reduced
sub-prescheme of `S` having `T` as underlying space satisfies the conclusion of (6.9.3). One may therefore restrict to
proving the corollary for `S` while supposing it true for every closed reduced sub-prescheme of `S` having as underlying
space a closed subset `≠ S`. Since the morphism `S_{red} → S` is of finite type and surjective, one may replace `S` by
`S_{red}`, hence suppose `S` reduced and non-empty. Since `S` is Noetherian, the interior `T` of an irreducible
component of `S` is non-empty, and the prescheme induced on `T` is integral; there is therefore by virtue of (6.9.1) a
non-empty open set `U ⊂ T`

<!-- original page 155 -->

such that `ℱ|u⁻¹(U)` is flat over `U`. If `Y` is then the reduced sub-prescheme of `S` having `S − U` as underlying
space, there is by hypothesis a partition `(Y_i)` of `Y` into locally closed sets in `Y` (hence in `S`) such that
`ℱ_i = ℱ ⊗_{𝒪_S} 𝒪_{Y_i}` is flat over `Y_i` for every `i`; it is clear that the `Y_i` and `U` form a partition
answering the question.

### 6.10. Dimension and depth of a Module normally flat along a closed sub-prescheme

**(6.10.1)** Let `X` be a locally Noetherian prescheme, `𝔍` a quasi-coherent Ideal of `𝒪_X`, `Y` the closed
sub-prescheme of `X` defined by `𝔍`, `j : Y → X` the canonical injection. For every integer `k ≥ 0`, the `𝒪_X`-Module
`𝔍^k ℱ/𝔍^{k+1} ℱ` is annihilated by `𝔍`, hence of the form `j_*(𝒢_k)`, where `𝒢_k = j*(𝔍^k ℱ/𝔍^{k+1} ℱ) = j*(𝔍^k ℱ)` is
a coherent `𝒪_Y`-Module. By abuse of language, we shall denote by `gr^•_𝔍(ℱ)` the graded `𝒪_Y`-Module equal to the
direct sum

```text
  ⨁_{k=0}^∞ 𝒢_k = j*(⨁_{k=0}^∞ 𝔍^k ℱ/𝔍^{k+1} ℱ);
```

in particular, one has `gr^0_𝔍(ℱ) = 𝒢_0 = ℱ ⊗_{𝒪_X} 𝒪_Y = j*(ℱ)`. We shall say (with Hironaka) that `ℱ` is **normally
flat along `Y`** if `gr^•_𝔍(ℱ)` is a flat `𝒪_Y`-Module. It amounts to the same ((2.1.12) and (0_I, 6.1.2)) to say that
each of the `𝒪_Y`-Modules `𝒢_k = j*(𝔍^k ℱ)` is locally free.

**Proposition (6.10.2).**

<!-- label: IV.6.10.2 -->

*Let `X` be a locally Noetherian prescheme, `Y` an integral closed sub-prescheme of `X`. For every coherent `𝒪_X`-Module
`ℱ`, there exists an open set `U` of `X` such that `Y ∩ U ≠ ∅` and that `ℱ|U` is normally flat along `Y ∩ U`.*

Indeed, let `𝔍` be the coherent Ideal of `𝒪_X` defining `Y`; the `𝒪_Y`-Algebra `ℬ = gr^•_𝔍(𝒪_X)` is quasi-coherent and
of finite type, since it is generated by `gr^1_𝔍(𝒪_X)`, the inverse image of `𝔍/𝔍²`; since `gr^•_𝔍(ℱ)` is a
quasi-coherent `ℬ`-module generated by `gr^1_𝔍(ℱ)`, it is a `ℬ`-Module of finite type. If one sets `Z = Spec(ℬ)`, the
structure morphism `u : Z → Y` is then of finite type, and if `ℋ` is the coherent `𝒪_Z`-Module such that
`u_*(ℋ) = gr^•_𝔍(ℱ)`, it suffices to apply to `u` and `ℋ` the generic flatness theorem (6.9.1) to prove the proposition.

**Proposition (6.10.3).**

<!-- label: IV.6.10.3 -->

*The notation being that of (6.10.1), suppose that `ℱ` is normally flat along `Y`. Then:*

*(i) `Y ∩ Supp(ℱ)` is at once an open and closed part of `Y` (in other words, a union of connected components of `Y`).*

*(ii) If `𝔍` is locally nilpotent, `Supp(ℱ)` is an open and closed part of `X`, and for every `x ∈ Supp(ℱ)`, one has*

```text
  (6.10.3.1)               dim(ℱ_x) = dim(𝒪_{Y,x})
```

```text
  (6.10.3.2)               prof(ℱ_x) = prof(𝒪_{Y,x})
```

```text
  (6.10.3.3)               coprof(ℱ_x) = coprof(𝒪_{Y,x}).
```

(i) With the notation of (6.10.1), one has `Y ∩ Supp(ℱ) = Supp(𝒢_0)` (I, 9.1.13), and since by hypothesis `𝒢_0` is a
locally free `𝒪_Y`-Module of finite type, its support is at once open and closed in `Y`.

<!-- original page 156 -->

(ii) The hypothesis that `𝔍` is locally nilpotent entails that the underlying spaces of `X` and of `Y` are the same,
whence the first two assertions of (ii), taking (5.1.12.1) into account; it remains to prove (6.10.3.2), for one will
deduce at once (6.10.3.3) by difference. Let `(f_i)_{1 ≤ i ≤ p}` be a finite sequence of elements of the maximal ideal
of `𝒪_{X,x}` whose images in `𝒪_{Y,x} = 𝒪_{X,x}/𝔍_x` form a maximal `𝒪_{Y,x}`-regular sequence; the hypothesis on `ℱ`
and `𝔍` entails that the `𝒪_{Y,x}`-module `gr^•_{𝔍_x}(ℱ_x)` is free of finite type, hence the sequence `(f_i)` is
`gr^•_{𝔍_x}(ℱ_x)`-regular; one deduces that this sequence is also `ℱ_x`-regular (0, 15.1.19). Let on the other hand `n`
be the largest integer such that `ℱ_x^{(n)} = 𝔍_x^n ℱ_x ≠ 0`. The hypothesis also entails that
`gr^•_{𝔍_x}(ℱ_x/ℱ_x^{(n)})` is free of finite type, hence the sequence `(f_i)` is also `(ℱ_x/ℱ_x^{(n)})`-regular (loc.
cit.). Applying lemma (3.4.1.4), one concludes by induction on `i` an exact sequence

```text
  0 → ℱ_x^{(n)}/(∑_{i=1}^p f_i ℱ_x^{(n)}) → ℱ_x/(∑_{i=1}^p f_i ℱ_x).
```

But the hypothesis entails that `ℱ_x^{(n)}` is a free `𝒪_{Y,x}`-module of finite type and `≠ 0`, hence
`ℱ_x^{(n)}/(∑_{i=1}^p f_i ℱ_x^{(n)})` is isomorphic to a module of the form `(𝒪_{Y,x}/(∑_{i=1}^p f_i 𝒪_{Y,x}))^m` with
`m > 0`; since `prof(𝒪_{Y,x}/(∑_{i=1}^p f_i 𝒪_{Y,x})) = 0` (0, 16.4.6) one has also, by the characterization (0, 16.4.6,
(i)) of modules of depth zero, `prof(ℱ_x^{(n)}/(∑_{i=1}^p f_i ℱ_x^{(n)})) = 0`, then
`prof(ℱ_x/(∑_{i=1}^p f_i ℱ_x)) = 0`; the `(f_i)_x` belonging to the maximal ideal of `𝒪_{Y,x}` and forming an
`ℱ_x`-regular sequence, this shows that one has `prof(ℱ_x) = p` (0, 16.4.6, (ii)).

**Corollary (6.10.4).**

<!-- label: IV.6.10.4 -->

*Let `U_{S_n}(ℱ)` (resp. `U_{C_n}(ℱ)`) be the set of `x ∈ X` such that `ℱ` satisfies `(S_n)` at the point `x` (resp.
such that `coprof(ℱ_x) ≤ n`). If `ℱ` is normally flat along `Y`, if `Supp(ℱ) = X` and if `𝔍` is locally nilpotent, one
has `U_{S_n}(ℱ) = U_{S_n}(𝒪_Y)` and `U_{C_n}(ℱ) = U_{C_n}(𝒪_Y)`.*

**Proposition (6.10.5).**

<!-- label: IV.6.10.5 -->

*The notation being that of (6.10.1), suppose that `Y` is connected and non-empty, and that `ℱ` is normally flat along
`Y`. For every integer `n ≥ 0`, set*

```text
  (6.10.5.1)               r(n) = rg_{𝒪_Y}(gr^n_𝔍(ℱ))
```

*(the locally free `𝒪_Y`-Module `gr^n_𝔍(ℱ)` being necessarily of constant rank). Then:*

*(i) There exists a polynomial `P ∈ ℚ[T]` such that `P(n) = r(n)` for every `n` large enough.*

*(ii) One has `Y ∩ Supp(ℱ) = ∅` (in other words `ℱ/𝔍ℱ = 0`), or `Y ∩ Supp(ℱ) = Y` (in other words `Y ⊂ Supp(ℱ)`). In the
second case, let `d − 1` be the degree of `P`; for every maximal point `y` of `Y`, one has*

```text
  (6.10.5.2)               dim(ℱ_y) = d
```

*and in particular*

```text
  (6.10.5.3)               codim(Y, Supp(ℱ)) = d.
```

*(iii) Suppose `Y ⊂ Supp(ℱ)`. For every `x ∈ Y`, one has*

```text
  (6.10.5.4)               dim(ℱ_x) = dim(𝒪_{Y,x}) + d.
```

*More precisely, there exist in `𝔍_x` elements `f_i` (`1 ≤ i ≤ d`) belonging to a system of parameters for `ℱ_x` (0,
16.3.6) and such that, in `Spec(𝒪_{X,x})`, one has `V(𝔍_x) = V(∑_{i=1}^d f_i 𝒪_{X,x}) ∩ Supp(ℱ)`.*

<!-- original page 157 -->

Since `Y` is supposed connected, the first assertion of (ii) follows from (6.10.3, (i)). If one has `Y ∩ Supp(ℱ) = ∅`,
assertion (i) is trivial with `P = 0`. Suppose that `Supp(ℱ) ⊃ Y`, and let `y` be a maximal point of `Y`; since one then
has `Y_y = Supp(𝒪_{Y,y})`, `ℱ_y/𝔍_y ℱ_y` is an `𝒪_y`-module of finite length (3.1.4); setting
`s(n) = long(gr^n_{𝔍_y}(ℱ_y))`, one knows that there is a polynomial `R ∈ ℚ[T]` such that `s(n) = R(n)` for `n` large
enough, namely the polynomial `H(n + 1) − H(n)`, where `H` is the Hilbert-Samuel polynomial of `ℱ_y` for the
`𝔍_y`-preadic filtration (0, 16.2.1). Since the `𝒪_{Y,y}`-modules `gr^n_{𝔍_y}(ℱ_y)` are free by hypothesis, one has
`r(n) = s(n)/m`, denoting by `m` the length of the `𝒪_{Y,y}`-module `𝒪_{Y,y} = 𝒪_y/𝔍_y`; one therefore satisfies (i) by
taking `P = (1/m)R`. One knows in addition (0, 16.2.3) that `deg(H) = dim(ℱ_y)`, whence the relation (6.10.5.2); the
relation (6.10.5.3) follows from this by means of (5.1.12.2).

It remains to prove (iii) for any point `x ∈ Y`. Set `A = 𝒪_{X,x}`, `𝔍 = 𝔍_x`, so that `𝒪_{Y,x} = A/𝔍`, and `M = ℱ_x`;
let `S = gr^•_𝔍(A)`, which is a graded `(A/𝔍)`-algebra of finite type, with positive degrees, such that `S_0 = A/𝔍`, and
generated by its homogeneous elements of degree `1`; let finally `N = gr^•_𝔍(M)`, which is a graded `S`-module of finite
type, each homogeneous component `N_n` being by hypothesis a free `(A/𝔍)`-module of length `r(n)`. Let `𝔪` be the
maximal ideal of `A`, `k = A/𝔪` its residue field; `B = S ⊗_A k` is a graded `k`-algebra of finite type, with positive
degrees, generated by its homogeneous elements of degree `1` and such that `B_0 = k`, so that `𝔮 = B_+ = ⨁_{n ≥ 1} B_n`
is a maximal ideal in `B`; `E = N ⊗_A k` is a graded `B`-module of finite type such that `rg_k(E_n) = r(n)`. Apply (0,
16.2.7) to the graded ring `B = S ⊗_A k` and to the graded `B`-module `E = N ⊗_A k`, and let `f̄_i ∈ 𝔮^{n_i}`
(`1 ≤ i ≤ d`) be an element of which `f_i` is the image in `B_{n_i}`. For `n ≥ sup(n_i)`, consider the sub-`A`-module
`∑_{i=1}^d f_i 𝔍^{n−n_i} M` of `M`; since the homogeneous component of degree `n` of the sub-module `∑_{i=1}^d f̄_i E`
of `E` is equal to `E_n` once `n` is large enough, one sees that, for `n` large enough, one has

```text
  𝔍^n M = ∑_{i=1}^d f_i 𝔍^{n−n_i} M + 𝔪 𝔍^n M
```

and since `𝔍^n M` is an `A`-module of finite type, this entails, by Nakayama's lemma,

```text
  𝔍^n M = ∑_{i=1}^d f_i 𝔍^{n−n_i} M ⊂ ∑_{i=1}^d f_i M.
```

If `𝔞` is the annihilator of `M`, one has therefore (0_I, 1.7.5) in `Spec(A)`

```text
  V(∑_{i=1}^d f_i A) ∩ V(𝔞) ⊂ V(𝔍^n M) = V(𝔍) ∩ V(𝔞) = V(𝔍)
```

since by hypothesis `Y ∩ Spec(A) = V(𝔍) ∩ Supp(M) = V(𝔍)`. Since on the other hand the `f_i` belong to `𝔍`, one has
`V(𝔍) ⊂ V(∑_{i=1}^d f_i A)`, which proves the last relation of (iii). It remains to show that the `f_i` belong to a
system of parameters for `M`. Replacing `A` by `A/𝔞` and the `f_i` by their images in `A/𝔞`, one may restrict to the
case where `𝔞 = 0`; one has just seen that one has `dim(A/𝔍) = dim(A/(∑_{i=1}^d f_i A))` and it therefore remains to
prove (0, 16.3.7) that one has

```text
  dim(A) ≤ dim(A/𝔍) + d.
```

Now, let `𝔭` be a prime ideal of `A` containing `𝔍` and such that `dim(A/𝔍) = dim(A/𝔭)`, so that `𝔭` is minimal among
the prime ideals containing `𝔍`. One has therefore `𝔭 = 𝔧_y`, where `y ∈ Spec(A)` is a maximal point of `Y`. But by
virtue of (6.10.5.2) and of the hypothesis `Spec(A) = Supp(M)`, one has `dim(A_𝔭) = d`; the inequality
`dim(A/𝔭) + dim(A_𝔭) ≤ dim(A)` (0, 16.1.4) completes the proof.

**Proposition (6.10.6).**

<!-- label: IV.6.10.6 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module, `Y` an irreducible closed sub-prescheme of `X`,
of generic point `y ∈ Supp(ℱ)`. There exists then a non-empty open neighbourhood `U` of `y` in `X` such that, for every
`x ∈ U ∩ Y`, one has*

```text
  (6.10.6.1)               dim(ℱ_x) = dim(ℱ_y) + dim(𝒪_{Y,x})
```

```text
  (6.10.6.2)               prof(ℱ_x) = prof(ℱ_y) + prof(𝒪_{Y,x})
```

```text
  (6.10.6.3)               coprof(ℱ_x) = coprof(ℱ_y) + coprof(𝒪_{Y,x}).
```

<!-- original page 158 -->

Let `Y' = Y_{red}`, which is an integral closed sub-prescheme of `Y` having the same underlying space, and defined by a
locally nilpotent Ideal `𝒦` of `𝒪_Y` (I, 6.1.6). It follows that `gr^•_𝒦(𝒪_Y)` is a coherent `𝒪_{Y'}`-Module, and since
`Y'` is integral, there is a neighbourhood `V` of `y` in `Y'` such that `gr^•_𝒦(𝒪_Y)|V` is locally free (0_I, 5.2.7); in
other words, up to replacing `X` by a neighbourhood of `y`, one may suppose that `𝒪_Y` is normally flat along `Y'`; one
deduces from (6.10.3) that one has

```text
  dim(𝒪_{Y,x}) = dim(𝒪_{Y',x}),           prof(𝒪_{Y,x}) = prof(𝒪_{Y',x})
```

for every `x ∈ Y`; this allows us to restrict to the case where the closed sub-prescheme `Y` is integral.

This being so, by virtue of (6.10.2), one may, replacing `X` by an open neighbourhood of `y`, suppose that `ℱ` is
normally flat along `Y`. Since `y ∈ Supp(ℱ)`, the relation (6.10.6.1) follows from (6.10.5.2) and (6.10.5.4). Set now
`p = prof(ℱ_y)`; replacing `X` if necessary by an open neighbourhood of `y`, one may suppose that there exist `p`
sections `f_i` (`1 ≤ i ≤ p`) of `𝒪_X` above `X`, forming an `ℱ`-regular sequence, such that the `(f_i)_y` belong to the
maximal ideal `𝔪_y` of `𝒪_y` and `prof(ℱ_y/(∑_{i=1}^p (f_i)_y ℱ_y)) = 0` (0, 16.4.6). If `𝔍` is the Ideal of `𝒪_X`
defining `Y`, one has `𝔍_y ⊂ 𝔪_y`, and, replacing `X` again if necessary by a neighbourhood of `y`, one may suppose that
`f_i ∈ Γ(X, 𝔍)` for `1 ≤ i ≤ p`. Moreover, if one sets `𝒢 = ℱ/(∑_{i=1}^p f_i ℱ)`, the hypothesis `prof(ℱ_y) = 0` entails
that `𝒢_y` contains a sub-module isomorphic to `𝒪_y/𝔍_y` (0, 16.4.6); the same reasoning (taking (0_I, 5.3.8 and 5.2.7)
into account) shows that one may suppose there exists a sub-`𝒪_X`-Module `𝒮` of `𝒢` isomorphic to `𝒪_X/𝔍` such that
`𝒮 = 𝒪_{Y,y}` for every `x ∈ Y`. Set `𝒢' = 𝒢/𝒮`; replacing `X` by an open neighbourhood of `y`, one may, by virtue of
(6.10.2), suppose that `𝒮` and `𝒢'` are normally flat along `Y`. Let then `x` be any point of `Y`, and set
`q = prof(𝒪_{Y,x}) = prof(𝒮_x)`; let `(g_j)_{1 ≤ j ≤ q}` be a maximal `𝒮_x`-regular sequence of elements of the maximal
ideal `𝔪_x` of `𝒪_{X,x}`. Each of the homogeneous components of `gr^•_{𝔍_x}(𝒢)` is a flat `𝒪_{Y,x}`-module of finite
type by hypothesis, hence is a free `𝒪_{X,x}`-module, and so is likewise `gr^•_{𝔍_x}(𝒢')`; since the sequence `(g_j)` is
`𝒪_{Y,x}`-regular, it is consequently `gr^•_{𝔍_x}(𝒢')`-regular, whence one concludes it is `𝒢'_x`-regular (0, 15.1.19).
Applying lemma (0, 15.1.18) to the exact sequence

```text
  0 → 𝒮_x → 𝒢_x → 𝒢'_x → 0
```

by induction on `j`, one concludes an exact sequence

```text
  0 → 𝒮_x/(∑_{j=1}^q g_j 𝒮_x) → 𝒢_x/(∑_{j=1}^q g_j 𝒢_x).
```

But by hypothesis `prof(𝒮_x/(∑_{j=1}^q g_j 𝒮_x)) = 0` (0, 16.4.6); by the characterization (0, 16.4.6) of modules of
depth zero, one concludes that `prof(𝒢_x/(∑_{j=1}^q g_j 𝒢_x)) = 0 = prof(ℱ_x/(∑_{i=1}^p f_i ℱ_x + ∑_{j=1}^q g_j ℱ_x))`;
the sequence `(g_j)` being `𝒮_x`-regular and `𝒢'_x`-regular, is also `𝒢_x`-regular; finally, the sequence `((f_i)_x)` is
`ℱ_x`-regular by hypothesis and is formed of elements of the maximal ideal `𝔪_x`; one deduces (0, 16.4.6) that
`prof(ℱ_x) = p + q`, which completes the proof.

### 6.11. Criteria for the sets `U_{S_n}(ℱ)` or `U_{C_n}(ℱ)` to be open

**Lemma (6.11.1).**

<!-- label: IV.6.11.1 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module; then the function `x ↦ dim. proj(ℱ_x)` is upper
semi-continuous on `X`.*

One may restrict to the case where `X = Spec(A)` is the spectrum of a Noetherian ring and `ℱ = M̃`, where `M` is an
`A`-module of finite type. Suppose that for an `x ∈ X`, one has `dim. proj(M_x) = n < +∞` (if `n = +∞` there is nothing
to prove); there exists a resolution of `M`

```text
  L_{n−1} → L_{n−2} → ⋯ → L_0 → M → 0
```

<!-- original page 159 -->

where the `L_i` are free `A`-modules of finite type (`A` being Noetherian), whence an exact sequence

```text
  0 → R → L_{n−1} → L_{n−2} → ⋯ → L_0 → M → 0
```

where `R` is an `A`-module of finite type; one deduces an exact sequence

```text
  0 → R_x → (L_{n−1})_x → ⋯ → (L_0)_x → M_x → 0
```

where the `(L_i)_x` are free `A_x`-modules of finite type; since by hypothesis `dim. proj(M_x) = n`, this entails that
`R_x` is a projective `A_x`-module of finite type (M, VI, 2.1) and consequently a free `A_x`-module of finite type
(0_III, 10.1.3). One concludes that there exists an open neighbourhood `U` of `x` in `X` such that, for every `x' ∈ U`,
`R_{x'}` is a free `A_{x'}`-module (0_I, 5.2.7), hence `M_{x'}` admits a projective resolution of length `n`, in other
words `dim. proj(M_{x'}) ≤ n`, which proves the lemma.

**Proposition (6.11.2).**

<!-- label: IV.6.11.2 -->

*Let `X` be a locally Noetherian prescheme locally immersible in a regular scheme (5.11.1); let `ℱ` be a coherent
`𝒪_X`-Module. Then:*

*(i) (M. Auslander) The function `x ↦ coprof(ℱ_x)` is upper semi-continuous on `X` (in other words, for every integer
`n`, the set `U_{C_n}(ℱ)` of `x ∈ X` such that `coprof(ℱ_x) ≤ n` is open).*

*(ii) For every integer `n`, the set `U_{S_n}(ℱ)` of `x ∈ X` such that `ℱ` has property `(S_n)` at the point `x` is
open.*

(i) The question being local on `X`, one may, by virtue of the hypothesis, restrict to the case where `X` is a closed
sub-scheme of a regular affine scheme `Y`. If `j : X → Y` is the canonical injection, and `𝒢 = j_*(ℱ)`, one knows that
one then has, for every `x ∈ X`, `dim(ℱ_x) = dim(𝒢_x)` and `prof(ℱ_x) = prof(𝒢_x)`, hence `coprof(ℱ_x) = coprof(𝒢_x)`,
and since `coprof(𝒢_y) = 0` for `y ∈ Y − X`, one is reduced to proving the property for `𝒢`; in other words, one may
restrict to the case where `X` is a regular affine scheme. One then knows (0, 17.3.4) that one has

```text
  prof(ℱ_x) = dim(𝒪_x) − dim. proj(ℱ_x).
```

On the other hand, if `S` is the unique closed sub-prescheme of `X` with underlying space `Supp(ℱ)`, one has
`dim(ℱ_x) = codim({x}, S)` (5.1.12.1), and, by virtue of (5.1.9)

```text
  dim(ℱ_x) = dim(𝒪_{X,x}) − codim_x(S, X)
```

since `𝒪_x` is a regular ring, and *a fortiori* biequidimensional (0, 16.5.12). One may therefore write

```text
  (6.11.2.1)            coprof(ℱ_x) = dim. proj(ℱ_x) − codim_x(S, X)
```

and the proposition then follows from (6.11.1) and from (0, 14.2.6).

(ii) Since the `U_{C_n}(ℱ)` are open for every `n` by (i), the `Z_n = X − U_{C_n}(ℱ)` are closed in `X`; moreover it is
clear that `Z_{n+1} ⊂ Z_n`, and since `dim(ℱ_x)` is finite for every `x ∈ X` and `coprof(ℱ_x) ≤ dim(ℱ_x)`, the
intersection of the `Z_n` is empty; since one may restrict to the case where `X` is affine, hence quasi-compact, one may
suppose that there exists an `m`

<!-- original page 160 -->

such that `Z_m = ∅`. Now, it follows from (5.7.4) that the relation `x ∈ U_{S_n}(ℱ)` is equivalent to the set of
relations

```text
  (6.11.2.2)            codim_x(Z_k, S) > n + k
```

for every `k ≥ 0`; but for `k ≥ m` this relation is automatically satisfied, hence one has in fact only to consider the
relations (6.11.2.2) for `0 ≤ k < m`. Now (0, 14.2.6) the set `V_{n,k}` of `x` satisfying (6.11.2.2) is open, and
`U_{S_n}(ℱ)`, intersection of the `V_{n,k}` for `0 ≤ k < m`, is also open. Q.E.D.

Recall that the hypothesis that `X` is locally immersible in a regular scheme is always fulfilled when `X` is a
prescheme locally of finite type over a field `k` (5.8.3).

**Corollary (6.11.3).**

<!-- label: IV.6.11.3 -->

*Under the hypotheses of (6.11.2), the set `CM(ℱ)` of points `x ∈ X` such that `ℱ_x` is a Cohen-Macaulay module is open
in `X`.*

Indeed, it is the set `U_{C_0}(ℱ)`.

**Remarks (6.11.4).**

<!-- label: IV.6.11.4 -->

*(i)* The reasoning of (6.11.2, (ii)) proves that (without hypothesis on `X`) when `U_{C_n}(ℱ)` is open for every
integer `n`, then `U_{S_n}(ℱ)` is open for every integer `n`.

*(ii)* One has `CM(ℱ) = ⋂_n U_{S_n}(ℱ)`. If every point `x ∈ X` admits an open neighbourhood `V` of finite dimension,
the sequence of intersections `V ∩ U_{S_n}(ℱ)` is stationary since there exists an `m` such that `dim(ℱ_x) ≤ m` for
every `x ∈ V`; consequently, if the `U_{S_n}(ℱ)` are open for every integer `n`, `CM(ℱ)` is then open in `X`.

*(iii)* One will write `U_{S_n}(X)`, `U_{C_n}(X)`, `CM(X)` instead of `U_{S_n}(𝒪_X)`, `U_{C_n}(𝒪_X)`, `CM(𝒪_X)`.

**Proposition (6.11.5).**

<!-- label: IV.6.11.5 -->

*Let `A` be a Noetherian local ring, `M` an `A`-module of finite type. For every prime ideal `𝔭` of `A`, one has*

```text
  (6.11.5.1)               coprof_{A_𝔭}(M_𝔭) ≤ coprof_A(M).
```

One may restrict to the case `M_𝔭 ≠ 0`. Since `Â` is a faithfully flat `A`-module (0_I, 7.3.5), there exists a prime
ideal `𝔮` of `Â` above `𝔭` (0_I, 6.5.1); since `M̂_𝔭 = (M ⊗_A Â) ⊗_A A_𝔭 = M ⊗_A Â_𝔭` and `Â_𝔮` is a flat `Â`-module,
hence a flat `A_𝔭`-module (0_I, 6.2.1), it follows from (6.3.2), applied to the local homomorphism `A_𝔭 → Â_𝔮`, to `M_𝔭`
and `M̂_𝔮 = M_𝔭 ⊗_{A_𝔭} Â_𝔮`, that one has `coprof_{A_𝔭}(M_𝔭) ≤ coprof_{Â_𝔮}(M̂_𝔮)`. On the other hand, `X = Spec(Â)` is
isomorphic to a sub-scheme of a regular scheme by virtue of Cohen's theorem (0, 19.8.8, (i)). One therefore deduces from
(6.11.2) that one has `coprof_{Â_𝔮}(M̂_𝔮) ≤ coprof_{Â}(M̂)`; finally, one knows that `coprof_{Â}(M̂) = coprof_A(M)` (0,
16.4.10), which completes the proof of (6.11.5).

This proposition justifies the definition of the codepth of an `A`-module when `A` is not a local ring, given in
(5.7.12).

**Proposition (6.11.6).**

<!-- label: IV.6.11.6 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module, `n` an integer `> 0`. Suppose that for every
integral closed sub-prescheme `Y` of `X`, there exists a non-empty open part `W` of `Y` such that the sub-prescheme of
`Y` induced on the open set `W` satisfies `(S_n)`. Then the set `U_{S_n}(ℱ)` is open in `X`.*

<!-- original page 161 -->

The question being local on `X`, one may restrict to the case where `X` is Noetherian. We shall reason by induction on
`n`: for `n = 1`, the set `U_{S_1}(ℱ)` is open in `X`, for the set of `x ∈ X` where `ℱ` does not satisfy `(S_1)` is the
set of `x` such that `ℱ_x` admits embedded associated prime ideals (5.7.5); if `(Z_λ)` is the finite family of prime
cycles associated with `ℱ` which are embedded, one has consequently `U_{S_1}(ℱ) = X − ⋃ Z_λ`, whence our assertion since
the `Z_λ` are closed. We shall therefore suppose henceforth that `n > 1`. In the second place, one may restrict to the
case where `Supp(ℱ) = X`, for there is a closed sub-prescheme `T` of `X` with `Supp(ℱ)` as underlying space, and a
coherent `𝒪_T`-Module `ℱ'` such that `ℱ = j_*(ℱ')`, `j : T → X` being the canonical injection (Err_III, 30); since it
amounts to the same to prove that `ℱ` or `ℱ'` satisfies `(S_n)` at a point `x ∈ Supp(ℱ)`, one may restrict to
considering the case where `T = X`. Note finally that by definition (5.7.2), `U_{S_n}(ℱ)` is stable under generization.
We shall use the following lemma:

**Lemma (6.11.6.1).**

<!-- label: IV.6.11.6.1 -->

*Let `X` be a Noetherian space in which every irreducible closed part admits a generic point, `E` a part of `X`. For `E`
to be open in `X`, it is necessary and sufficient that `E` be stable under generization, and that, for every open part
`V` of `X` and every irreducible part `Y` closed in `V`, such that `V − Y ⊂ E` and the generic point of `Y` belongs to
`E`, `E ∩ Y` contain a non-empty open part of `Y`.*

One will observe that this criterion entails that of (0_III, 9.2.6) when every irreducible closed part of `X` admits a
generic point. There is evidently only the sufficiency of the conditions stated to prove.

Consider the interior `U` of `E`; the closed set `X − U` is the union of its irreducible components, which are finite in
number and closed in `X`. If one had `E ≠ U`, the hypothesis that `E` is stable under generization would entail that the
generic point `ξ` of one of the irreducible components of `X − U` would belong to `E`. Now, `ξ` belongs to only one of
the irreducible components of `X − U`; if `T` is the union of the other irreducible components of `X − U`, `V = X − T`
is open in `X`, union of `U` and of the set `Y = {ξ}̄ ∩ V` closed in `V` and irreducible. By hypothesis `E ∩ Y` contains
a part `W` open in `Y`; one concludes that `U ∪ W` is open in `V`, hence in `X`, which is absurd since `U` is supposed
to be the interior of `E`.

By virtue of this lemma, one may suppose that there exists in `X` an integral sub-prescheme `Y` with generic point `y`
such that `ℱ` satisfies `(S_n)` at the point `y` and at all points of `X − Y`, and it remains to verify that there
exists in `X` an open neighbourhood of `y` such that `ℱ` satisfies `(S_n)` in this neighbourhood. Let us then
distinguish two cases:

*1°* `y` is a maximal point of `X`; since there exists an open neighbourhood of `y` meeting no irreducible component of
`X` other than `{y}̄`, one may suppose that `X` is irreducible, hence has the same underlying space as `Y`, so that `Y`
is defined by the Nilradical of `𝒪_X`, which is nilpotent. On the other hand, one may, replacing `X` by an open
neighbourhood of `y`, suppose that `ℱ` is normally flat along `Y` (6.9.1); it then follows from (6.10.4) that
`U_{S_n}(ℱ) = U_{S_n}(𝒪_Y)`, and since the latter is by hypothesis a neighbourhood of `y` in `X`, this proves the
proposition in this case.

<!-- original page 162 -->

*2°* `y` is not a maximal point of `X`, in other words (since `Supp(ℱ) = X`), `dim(ℱ_y) ≥ 1`, hence also `prof(ℱ_y) ≥ 1`
since `ℱ` satisfies by hypothesis `(S_n)` (and *a fortiori* `(S_1)`) at the point `y`. Replacing `X` if necessary by an
open neighbourhood of `y`, one may therefore suppose that there exists a section `f` of `𝒪_X` above `X`, `ℱ`-regular and
such that `f ∈ 𝔪_y`, or also `f(y) = 0` (0, 15.2.4); one therefore has again `f(x) = 0` for every `x ∈ Y` (0_I, 5.5.2).
One knows that `ℱ/fℱ` satisfies `(S_{n−1})` at the point `y` (5.7.6). Applying the inductive hypothesis, and replacing
`X` if necessary by an open neighbourhood of `y`, one may therefore suppose that `ℱ/fℱ` satisfies `(S_{n−1})` at every
point of `X`. But for every `x ∈ Y`, the relation `f(x) = 0` entails that one has `prof(ℱ_x/fℱ_x) = prof(ℱ_x) − 1` and
`dim(ℱ_x/fℱ_x) = dim(ℱ_x) − 1` (0, 16.3.4 and 16.4.6); the relation

```text
  prof(ℱ_x/fℱ_x) ≥ inf(n − 1, dim(ℱ_x/fℱ_x))
```

is therefore equivalent to

```text
  prof(ℱ_x) ≥ inf(n, dim(ℱ_x)).
```

Since one has supposed that `ℱ` satisfies `(S_n)` at every point of `X − Y`, this completes the proof.

**Corollary (6.11.7).**

<!-- label: IV.6.11.7 -->

*The notation being that of (6.11.6):*

*(i) The set `U_{S_1}(ℱ)` is open in `X`.*

*(ii) For the set `U_{S_2}(ℱ)` to be open, it suffices that every maximal point `x` of `Supp(ℱ)` belonging to
`U_{S_1}(ℱ)` be interior to `U_{S_1}(ℱ)`.*

Assertion (i) was proved in the course of the proof of (6.11.6); on the other hand, for `n = 2` case *2°* of the proof
of (6.11.6) is valid without any hypothesis on `X`, since (with the same notation) `U_{S_1}(ℱ)` and `U_{S_1}(ℱ/fℱ)` are
open in `X`. As to case *1°* of this proof, the hypothesis precisely assures that it is unnecessary to consider it.

**Proposition (6.11.8).**

<!-- label: IV.6.11.8 -->

*Let `X` be a locally Noetherian prescheme satisfying the following property:*

*(CMU) Every integral closed sub-prescheme `Y` of `X` contains a non-empty open set `W` such that the prescheme induced
by `Y` on `W` is a Cohen-Macaulay prescheme.*

*Then, for every coherent `𝒪_X`-Module `ℱ`, the function `x ↦ coprof(ℱ_x)` is locally constructible and upper
semi-continuous; the sets `U_{C_n}(ℱ)` and `U_{S_n}(ℱ)` are open in `X`.*

Indeed, let `Y` be an integral closed sub-prescheme of `X`, of generic point `y`; by virtue of (6.10.6), there is in `Y`
an open neighbourhood `V` of `y` such that, for every `x ∈ V ∩ Y`, one has

```text
  (6.11.8.1)               coprof(ℱ_x) = coprof(ℱ_y) + coprof(𝒪_{Y,x}).
```

But by hypothesis there exists a non-empty open set `W` of `Y` such that, for `x ∈ V ∩ W`, one has
`coprof(𝒪_{Y,x}) = 0`, hence `coprof(ℱ_x)` is constant in a neighbourhood of `y` in `Y`, which proves that the function
`x ↦ coprof(ℱ_x)` is locally constructible (0_III, 9.3.2); moreover it follows then from (6.11.5) and from (0_III,
9.3.4) that this function is upper semi-continuous. The last assertion follows from (6.11.4, (i)), or also from
(6.11.6).

**Remarks (6.11.9).**

<!-- label: IV.6.11.9 -->

*(i)* If `X` satisfies hypothesis (CMU) of (6.11.8), then, for every morphism `u : X' → X` locally of finite type, `X'`
also satisfies (CMU). Indeed, let `Y'` be an integral closed sub-prescheme of `X'`, `y'` its generic point, `y = u(y')`,
and let `Y` be the integral sub-prescheme of `X` having `{y}̄` as underlying space; then `u|Y'` factors as
`Y' →^v Y →^j X`, where `j` is the canonical injection (I, 5.2.2), and `v` is locally of finite type (I, 6.6.6). By
restricting to affine open neighbourhoods of `y` and `y'` respectively, one may therefore restrict to the case where
`X = Spec(A)`, `A` an integral Cohen-Macaulay ring, and `X' = Spec(A')`, where `A'` is an integral ring

<!-- original page 163 -->

containing `A` and which is an `A`-algebra of finite type. Replacing `A` if necessary by a ring of fractions `A_f` (with
`f ≠ 0`), one may moreover suppose that `A'` contains a polynomial ring `A[T_1, …, T_n] = A''`, and is a finite
`A''`-algebra (Bourbaki, *Alg. comm.*, chap. V, §3, n° 1, cor. 1 of th. 1). But `A''` is a Cohen-Macaulay ring (6.3.6);
so one may restrict to the case where moreover `A'` is a finite `A`-algebra. There is then `g ≠ 0` in `A` such that
`A'_g` is a free `A_g`-module of finite type (Bourbaki, *Alg. comm.*, chap. II, §5, n° 1, cor. of prop. 2), hence one
may suppose moreover that `A'` is a free `A`-module. But then `A'` is a Cohen-Macaulay `A`-module (0, 16.5.1), and since
`A'` is an `A`-module of finite type, `A'` is also a Cohen-Macaulay `A'`-module (0, 16.5.3), hence a Cohen-Macaulay
ring.

*(ii)* Suppose there exists a coherent `𝒪_X`-Module `ℱ` such that `Supp(ℱ) = X` and `ℱ` is a Cohen-Macaulay
`𝒪_X`-Module. Then `X` satisfies the condition (CMU): indeed, with the notation of the proof of (6.11.8), the relation
(6.11.8.1) shows that one has `coprof(𝒪_{Y,y}) = 0` in a neighbourhood (with respect to `Y`) of the generic point `y` of
`Y`.

One does not know whether there exist locally Noetherian preschemes of dimension `≥ 2` which do not satisfy (CMU) (if
`dim(X) = 1`, it is immediate that every maximal point of `X_{red}` admits an integral open neighbourhood of dimension
`1`, hence Cohen-Macaulay).

<!-- original page 163 -->

### 6.12. Nagata's criteria for `Reg(X)` to be open

**(6.12.1).**

<!-- label: IV.6.12.1 -->

Given a locally Noetherian prescheme `X`, we call **singular locus** of `X` and denote by `Sing(X)` the set of points
`x ∈ X` such that `X` is not regular at the point `x` (in other words, such that the local ring `𝒪_x` is not regular);
the complement `X − Sing(X)`, that is, the set of `x ∈ X` where `X` is regular, is denoted by `Reg(X)`. We propose in
this number to give conditions under which `Sing(X)` is closed (i.e. `Reg(X)` is open).

**Proposition (6.12.2).**

<!-- label: IV.6.12.2 -->

*Let `X` be a locally Noetherian prescheme. The following conditions are equivalent:*

*a) `Reg(X)` is open in `X`.*

*b) For every `x ∈ Reg(X)`, there exists a non-empty open subset of `{x}̄` contained in `Reg(X)`.*

*Moreover, these conditions are entailed by the following:*

*c) For every `x ∈ Reg(X)`, if one denotes by `Y` the reduced closed sub-prescheme of `X` having `{x}̄` as underlying
space, `Reg(Y)` is a neighbourhood of `x` in `Y`.*

The equivalence of a) and b) follows from the fact that `Reg(X)` is stable under generization (0, 17.3.2) and from
`(0_III, 9.2.6)`. To prove that c) entails b), one may restrict to the case where `X = Spec(A)` is an affine open
neighbourhood of `x`; if `(t_i)_{1 ≤ i ≤ n}` is a regular system of parameters (0, 17.1.6) of the regular local ring
`A_𝔭`, one may suppose (replacing `X` if necessary by an open neighbourhood of `x`) that `t_i = (s_i)_𝔭` for every `i`,
where `s_i ∈ A` and where the family `(s_i)_{1 ≤ i ≤ n}` is `A`-regular (0, 15.2.4). One has then `Y = Spec(A/𝔭)`, where
`𝔭 = j_x`; as the `t_i` generate the maximal ideal `𝔪 = 𝔭A_𝔭` of `A_𝔭`, one may again suppose (replacing `X` by a
smaller neighbourhood of `x`) that the `s_i` generate `𝔭`. For every `y ∈ Y`, the `(s_i)_y` therefore generate `𝔭_y`; as
they form an `A_y`-regular sequence, they form part of a system of parameters of `A_y` (0, 16.4.1); hence one deduces
from (0, 17.1.7) that if `(A/𝔭)_y = A_y/𝔭_y` is regular, the same holds for `A_y`, whence the conclusion.

**Corollary (6.12.3).**

<!-- label: IV.6.12.3 -->

*Let `X` be a locally Noetherian prescheme. The following conditions are equivalent:*

*a) For every sub-prescheme `Y` of `X`, `Reg(Y)` is open in `Y`.*

<!-- original page 164 -->

*b) For every integral closed sub-prescheme `Y` of `X`, `Reg(Y)` contains a non-empty open subset of `Y`.*

It is clear that a) entails b), for if `Y` is integral and `y` is its generic point, `𝒪_{Y,y}` is a field, so
`y ∈ Reg(Y)`. Conversely, to see that b) entails a), consider an integral closed sub-prescheme `Z` of `Y` of generic
point `z`; if `Y'` is the integral sub-prescheme of `X` having for underlying space the closure `Y' = {z}̄` of `z` in
`X`, then `Z` is open in `Y'` and the sub-prescheme `Z` of `Y'`, being reduced, is induced by `Y'` on the open set `Z`
of the underlying space of `Y'`. Now the hypothesis entails that `Reg(Y')` is a neighbourhood of `z` in `Y'`, hence
`Reg(Z)` is a neighbourhood of `z` in `Z`; it then suffices to apply (6.12.2) with `Y` replaced by `Z` and `X` by `Y`.

**Theorem (6.12.4) (Nagata).**

<!-- label: IV.6.12.4 -->

*Let `A` be a Noetherian ring, `X = Spec(A)`. The following conditions are equivalent:*

*a) For every prescheme `X'` locally of finite type over `X`, `Reg(X')` is open in `X'`.*

*b) For every finite integral `A`-algebra `A'`, there exists a non-empty open subset of `X' = Spec(A')` contained in
`Reg(X')`.*

*c) For every prime ideal `𝔭` of `A` and every finite radicial extension `K'` of the fraction field `K` of `A/𝔭`, there
exists a sub-`A`-algebra `A'` of `K'`, finite over `A`, having `K'` as fraction field, and such that there exists in
`X' = Spec(A')` a non-empty open set contained in `Reg(X')`.*

It is clear that a) implies b). To see that b) entails c), it suffices to remark that one may take as generators of the
extension `K'` of `K` elements integral over `A/𝔭` (and *a fortiori* over `A`), and since these elements are finite in
number, they generate a finite `A`-algebra `A'` of which `K'` is the fraction field; one may then apply b) to `A'`. It
remains to prove that c) entails a). The question being local on `X'`, one may first suppose that `X' = Spec(A')`, where
`A'` is an `A`-algebra of finite type; in view of (6.12.2), it suffices to prove that for every integral closed
sub-prescheme `Y'` of `X'`, `Reg(Y')` contains a non-empty open subset of `Y'`. In other words, one may restrict to
proving that if `A'` is an integral `A`-algebra of finite type and `X' = Spec(A')`, then `Reg(X')` contains a non-empty
open subset of `X'`. Let `K'` be the fraction field of `A'`; if `𝔭` is the canonical image in `X` of the generic point
of `X'`, `K'` is an extension of the fraction field `K` of `A/𝔭`, and `A/𝔭` is identified with a sub-ring of `A'`, `A'`
being an `(A/𝔭)`-algebra of finite type. One may evidently restrict in what follows to the case `𝔭 = 0`. Distinguish now
two cases:

**I)** `K'` is a separable extension of `K`. — One is then reduced to proving the

**Lemma (6.12.4.1).**

<!-- label: IV.6.12.4.1 -->

*Let `A` be an integral Noetherian ring, `A'` an integral `A`-algebra of finite type, containing `A` and such that the
fraction field `K'` of `A'` is a separable extension of the fraction field `K` of `A`. If `Spec(A)` contains a non-empty
open set formed of regular points, the same holds for `Spec(A')`.*

Replacing `A` by a ring of fractions `A_f` such that `D(f) ⊂ Reg(Spec(A))`, one may already suppose the ring `A`
regular. By hypothesis there exists in `K'` a system `(t_i)_{1 ≤ i ≤ n}` of elements algebraically independent over `K`
and such that `K'` is a finite separable algebraic extension of `K(t_1, …, t_n)`; by considering a finite system

<!-- original page 165 -->

of generators `t'_j` (`1 ≤ j ≤ m`) of `K'` over `K(t_1, …, t_n)`, which one may suppose integral over
`A_1 = A[t_1, …, t_n]`, one sees that `A'_1 = A_1[t'_1, …, t'_m]` is finite over `A_1` and has `K'` as fraction field.
If one sets `X' = Spec(A')`, `X'_1 = Spec(A'_1)`, it follows from the fact that the fields of rational functions `R(X')`
and `R(X'_1)` are both isomorphic to `K'`, and from the fact that `X'` and `X'_1` are `A`-preschemes of finite type,
that there exists an open set `U' ⊂ X'` and an open set `U'_1 ⊂ X'_1` which are `A`-isomorphic (I, 6.5.5). One is
therefore reduced to proving that `Reg(X'_1)` contains a non-empty open set; in other words one may suppose that `A'` is
a finite `A_1`-algebra. Now one knows (0, 17.3.7) that `A_1` is a regular ring, and one may therefore restrict to the
case where `A'` is a finite `A`-algebra and `K'` a finite separable extension of `K`. If `ξ` is the generic point of
`X`, `A'_ξ = K'` is then a free module over `A_ξ = K`, hence (Bourbaki, *Alg. comm.*, chap. II, §5, n° 1, cor. of prop.
2\) one may, replacing `A` if necessary by an `A_f`, suppose that `A'` is a free `A`-module of finite type. Let then
`(x_i)_{1 ≤ i ≤ r}` be a basis of this `A`-module, and set

```text
  (6.12.4.2)         d = det(Tr_{A'/A}(x_i x_j)) = det(Tr_{K'/K}(x_i x_j)) ∈ A.
```

Since `K'` is separable over `K`, one knows (Bourbaki, *Alg.*, chap. IX, §2, prop. 5) that `d ≠ 0`; replacing `A` if
necessary by the ring of fractions `A_d`, one may suppose `d` invertible in `A`. But then, for every `x ∈ Spec(A)`, if
one denotes by `x̄_i` (`1 ≤ i ≤ r`) the canonical image of `x_i` in `A'(x) = A' ⊗_A k(x)`, one has
`det(Tr_{A'(x)/k(x)}(x̄_i x̄_j)) = d̄`, the canonical image of `d` in `k(x) = A_x/𝔪_x`; and since `d̄` is invertible
(hence `≠ 0`) in `k(x)`, one knows (*loc. cit.*) that `A'(x)` is a separable `k(x)`-algebra, hence a direct composition
of fields, finite separable extensions of `k(x)`. Such an algebra being a regular ring, one sees that the morphism
`g : X' → X` is flat and that its fibres `g⁻¹(x)` are regular for every `x ∈ X`; one then concludes from (6.5.2, (ii))
that `X'` is regular, which terminates the proof in this case.

**II)** *General case.* — As `A'` is a torsion-free `A`-module, `A' ⊗_A K` is identified with a sub-ring of `K'`, hence
`X'' = Spec(A' ⊗_A K)` is an integral `K`-prescheme of which `K'` is the field of rational functions. One knows (4.6.6)
that there exists a finite radicial extension `K_1` of `K` such that if `X''_1 = Spec(A' ⊗_A K_1) = X'' ⊗_K K_1`, then
`(X''_1)_{red}` is a `K_1`-prescheme geometrically reduced and of finite type; moreover, the morphism
`Spec(K_1) → Spec(K)` being radicial, finite and surjective, is a universal homeomorphism (2.4.5), hence `X''_1` is
homeomorphic to `X''`, and consequently `(X''_1)_{red}` is integral; moreover, its field of rational functions `K'_1` is
a finite radicial extension of `K'` and a separable extension of finite type of `K_1` (4.6.1). By virtue of hypothesis
c) of the statement, there is a sub-`A`-algebra *finite* `A_1` of `K_1`, having `K_1` as fraction field, and such that
if one sets `X_1 = Spec(A_1)`, then `Reg(X_1)` contains a non-empty open set of `X_1`. Let `A'_1` be the image of the
canonical homomorphism `A' ⊗_A A_1 → K'_1`, and set `X'_1 = Spec(A'_1)`; `A'_1` is an integral ring which is a finite
`A`-algebra and whose fraction field is `K'_1` by construction; moreover, as the composite homomorphism
`A' → A' ⊗_A A_1 → A'_1 → K'_1` is identical to `A' → K' → K'_1`, hence injective, the homomorphism `A' → A'_1` is
injective; the morphism `g : X'_1 → X'` is therefore finite and surjective (II, 6.1.10). This being so, the hypothesis
on `A_1` and Part I) of the proof entail that `Reg(X'_1)`

<!-- original page 166 -->

contains a non-empty open set `V'_1`; as `g` is closed (II, 6.1.10), one may suppose that `V'_1 = g⁻¹(V')`, where `V'`
is an affine open set of `X'`; replacing `A'` by the ring of `V'` and `A'_1` by that of `V'_1`, one may therefore
suppose that `X'_1` is regular. Moreover, the same reasoning as in I) applied to the generic point `ξ'` of `X'` allows
one (replacing `X'` if necessary by a neighbourhood of `ξ'`) to suppose that `A'_1` is a free `A'`-module, and
consequently that the morphism `g` is flat. But it then follows from (6.5.2, (i)) that `X'` is regular. Q.E.D.

**Corollary (6.12.5) (Zariski).**

<!-- label: IV.6.12.5 -->

*Let `k` be a field; for every `k`-prescheme `X` locally of finite type over `k`, the set of `x ∈ X` where `X` is
regular (resp. geometrically regular over `k`) is open in `X`.*

The assertion of the corollary concerning the property of being regular follows from (6.12.4) by taking `A = k`. The
assertion concerning the property of being geometrically regular already follows from (6.8.7); one may also deduce it
from (6.12.4) in the following way. Set `k' = k^{p⁻∞}` (`p` characteristic exponent of `k`); as the morphism
`Spec(k') → Spec(k)` is radicial, integral and surjective, it is a universal homeomorphism (2.4.5), hence the projection
morphism `X ⊗_k k' → X` is a homeomorphism. The projection in `X` of `Reg(X ⊗_k k')` is the set of points of `X` where
`X` is geometrically regular over `k`, by virtue of (6.7.7, e)), hence this set is open by what precedes.

**Corollary (6.12.6).**

<!-- label: IV.6.12.6 -->

*Let `A` be a ring having one of the following properties:*

*(i) `A` is a Dedekind ring and its fraction field `K` is of characteristic `0`.*

*(ii) `A` is a Noetherian semi-local ring of dimension `≤ 1`.*

*Then, for every prescheme `X` locally of finite type over `A`, `Reg(X)` is open in `X`.*

Let us verify in both cases condition c) of (6.12.4). In both cases, a prime ideal `𝔭` of `A` is maximal or minimal; if
`𝔭` is maximal, a finite integral `(A/𝔭)`-algebra is a field, and condition c) of (6.12.4) is trivially verified.
Suppose then `𝔭` not maximal, and distinguish the two cases of the statement.

(i) If `K` is of characteristic `0`, there is no radicial extension of `K` other than `K` itself; as a Dedekind ring is
regular (0, 17.1.4), condition c) of (6.12.4) is trivially verified.

(ii) One may then suppose `A` integral (6.12.2); let `K` be its fraction field; if `K'` is a finite radicial extension
of `K`, and `A'` a sub-`A`-algebra of `K'` generated by a finite system of generators of `K'` over `K`, integral over
`A`, then `A'` is a semi-local integral ring of dimension `1` (0, 16.1.5), and consequently, in `X' = Spec(A')`, the set
reduced to the generic point is open and evidently contained in `Reg(X')`, which proves condition c) of (6.12.4) in this
case.

This corollary applies notably when `A = ℤ`.

**Theorem (6.12.7) (Nagata).**

<!-- label: IV.6.12.7 -->

*Let `A` be a complete Noetherian local ring, `X = Spec(A)`. Then `Reg(X)` is open in `X`.*

In view of (6.12.2), one is reduced to the case where `A` is moreover integral, and to proving that in this case
`Reg(X)` contains a non-empty open subset of `X`. Distinguish

<!-- original page 167 -->

two cases:

**I)** *The fraction field `K` of `A` is of characteristic `0`.* — One knows then (0, 19.8.8) that there exists a
complete discrete valuation ring `C` and a sub-ring `B` of `A` such that `A` is a finite `B`-algebra and `B` is
isomorphic to a ring of formal series `C[[T_1, …, T_n]]`. Since `C` is regular (II, 7.1.6), the same holds for `B` (0,
17.3.8); moreover, the fraction field `L` of `B` being of characteristic `0`, `K` is a finite separable extension of
`L`, hence one may apply (6.12.4.1) to `B`, and this then proves the proposition.

**II)** *The fraction field `K` of `A` is of characteristic `p > 0`.* — Then `A` contains the prime field `𝔽_p`, and the
theorem was proved in this case in (0, 22.7.6).

**Corollary (6.12.8).**

<!-- label: IV.6.12.8 -->

*Let `A` be a complete Noetherian local ring. Then, for every prescheme `X` locally of finite type over `A`, `Reg(X)` is
open in `X`.*

Let us verify condition c) of (6.12.4). If `𝔭` is prime in `A`, `A/𝔭` is still a complete Noetherian local ring; if `K'`
is a finite extension of the fraction field `K` of `A/𝔭`, then `K'` is the fraction field of a finite sub-`A`-algebra
`A'` of `K'`, generated by a system of generators of `K'` over `K`, integral over `A`. One knows then that `A'` is a
complete semi-local ring (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9), hence a product of complete
local rings, and since `A'` is integral, it is a complete local ring; by virtue of (6.12.7), if `X' = Spec(A')`,
`Reg(X')` is open and non-empty, whence the conclusion.

**Proposition (6.12.9).**

<!-- label: IV.6.12.9 -->

*Let `X` be a locally Noetherian prescheme such that `Reg(X)` is open; then, for every `n ≥ 0`, the set `U_{R_n}(X)` of
points `x ∈ X` where `X` satisfies `(R_n)` is open.*

Indeed (5.8.2), `U_{R_n}(X)` is the union of `Reg(X)` and of the set of `x ∈ Sing(X)` such that the generic points `z`
of the irreducible components of `Sing(X)` containing `x` satisfy the relation `dim(𝒪_{x,z}) ≥ n + 1` (since one has
`z ∉ Reg(X)`); in other words, these points `x ∈ Sing(X)` are those for which `codim_x(Sing(X), X) ≥ n + 1` (0, 14.2.1);
as the function `x ↦ codim_x(Sing(X), X)` is lower semi-continuous (0, 14.2.6), the set of these points is open in
`Sing(X)`, which completes the proof.

Let us also note the following elementary result:

**Proposition (6.12.10).**

<!-- label: IV.6.12.10 -->

*Let `X` be a locally Noetherian prescheme. The set `U_{R_0}(X)` is open in `X`. For `U_{S_1}(X)` to be open in `X`, it
is necessary and sufficient that every maximal point `x ∈ X` such that `x ∈ U_{S_1}(X)` (which means that `X` is reduced
at `x`) be interior to `U_{S_1}(X)`.*

By definition (5.8.2), `U_{R_0}(X)` is the set `X − ⋃ X_λ`, where `X_λ` runs through the set of irreducible components
of `X` such that `X` is not reduced at their generic point;

<!-- original page 168 -->

as the set of irreducible components of `X` is locally finite, `U_{R_0}(X)` is open. Concerning `U_{S_1}(X)`, the
condition of the statement being trivially necessary, let us prove that it is sufficient. Let `X_μ` be the irreducible
components of `X` such that at their generic point `x_μ` the prescheme `X` is reduced; by hypothesis there exists an
open set `U ⊂ U_{S_1}(X)` containing all the `x_μ`. Denote then by `Z_λ` the irreducible components of the closed set
`Z = X − U` whose generic point `z_λ` is such that `dim(𝒪_{x,z_λ}) ≥ 1` and such that `𝒪_{z_λ}` is non-regular. No point
belonging to one of the `Z_λ` can belong to `U_{S_1}(X)`; but conversely, if `x ∈ Z` belongs to none of the `Z_λ`, then,
for every generization `x'` of `x`, either `x' ∈ U`, or one has `dim(𝒪_{x,x'}) ≥ 2`, or one has `dim(𝒪_{x,x'}) = 1`, and
as `x'` belongs to none of the `Z_λ`, `{x'}̄` is necessarily an irreducible component of `Z`, of codimension `1` in `X`,
distinct from the `Z_λ`, hence `𝒪_{x'}` is regular by definition. One concludes that `U_{S_1}(X) = X − ⋃ Z_λ`; as the
set of `Z_λ` is locally finite in `Z`, `⋃ Z_λ` is closed, which completes the proof that `U_{S_1}(X)` is open in `X`.

### 6.13. Criteria for `Nor(X)` to be open

**(6.13.1).**

<!-- label: IV.6.13.1 -->

Given a locally Noetherian prescheme `X`, we shall denote by `Nor(X)` the set of `x ∈ X` where `X` is normal; this set
contains `Reg(X)` and is contained in the (open) set of points `x` such that `𝒪_x` is integral (i.e. the set of points
`x` where `X` is reduced, and which belong to a single irreducible component of `X`).

**Proposition (6.13.2).**

<!-- label: IV.6.13.2 -->

*Let `X` be a reduced locally Noetherian prescheme, `X'` its normalization (II, 6.3.8). If the canonical morphism
`f : X' → X` is finite, `Nor(X)` is open in `X`.*

Indeed, one has `X' = Spec(f_*(𝒪_{X'}))` and `f_*(𝒪_{X'})` is a coherent `𝒪_X`-algebra by hypothesis (II, 6.1.3). To say
that `X` is normal at a point `x` means that the canonical homomorphism `𝒪_x → (f_*(𝒪_{X'}))_x` is bijective (II,
6.3.4); but the set of these points is open since `𝒪_X` and `f_*(𝒪_{X'})` are coherent `(0_I, 5.2.7)`.

**Corollary (6.13.3).**

<!-- label: IV.6.13.3 -->

*If `A` is a Japanese integral Noetherian ring, `Nor(Spec(A))` is open in `Spec(A)`.*

**Proposition (6.13.4).**

<!-- label: IV.6.13.4 -->

*Let `X` be a locally Noetherian prescheme. For `Nor(X)` to be open, it is necessary and sufficient that every maximal
point `x` of `X` such that `x ∈ Nor(X)` (which means that `X` is reduced at the point `x`) be interior to `Nor(X)`.*

There is only the sufficiency of the condition to prove. By virtue of the remark made in (6.13.1), one may restrict
(replacing `X` by an open subset of `X` in which `X` is reduced) to the case where `X` is reduced, i.e. suppose that the
maximal points of `X` belong to `U_{S_2}(X)` and to `U_{R_1}(X)`; as `Nor(X) = U_{S_2}(X) ∩ U_{R_1}(X)` by virtue of
Serre's criterion (5.8.6), one deduces therefore from (6.11.7) and (6.12.10) that these two sets are open; consequently
`Nor(X)` is open in `X`.

**Corollary (6.13.5).**

<!-- label: IV.6.13.5 -->

*If `X` is such that `Reg(X)` is open in `X`, then `Nor(X)` is open in `X`.*

Indeed, every maximal point `x` where `X` is reduced (hence `𝒪_x` a field) belongs to `Reg(X)`, hence is interior to
`Reg(X)` by hypothesis, and *a fortiori* interior to `Nor(X)`.

**Proposition (6.13.6) (Nagata).**

<!-- label: IV.6.13.6 -->

*Let `A` be an integral Noetherian ring, `K` its fraction field, `K'` a finite extension of `K`, `A'` the integral
closure of `A` in `K'`. For `A'` to be a finite `A`-algebra, it is necessary and sufficient that the following two
conditions be satisfied:*

*(i) There exists `f ≠ 0` in `A` such that the integral closure `A'_f` of the ring of fractions `A_f` in `K'` is a
finite `A_f`-algebra.*

<!-- original page 169 -->

*(ii) For every prime ideal `𝔭 ∈ Spec(A)`, the integral closure `A'_𝔭` of the local ring `A_𝔭` in `K'` is a finite
`A_𝔭`-algebra.*

The conditions are necessary, for, for every multiplicative subset `S` of `A`, `S⁻¹A'` is the integral closure of `S⁻¹A`
in `K'` and is by hypothesis a finitely generated `S⁻¹A`-module. To see that the conditions are sufficient, consider the
increasing filtered family `(B_λ)` of the sub-`A`-algebras of `K'` which are finite `A`-algebras and have `K'` as
fraction field. Set `Y = Spec(A)`, `X_λ = Spec(B_λ)`, denote by `u_λ` the morphism `X_λ → Y`, and let
`S_λ = X_λ − Nor(X_λ)`, `T_λ = u_λ(S_λ)`. One may restrict to the `B_λ` containing a finite set whose image in `A'` is a
system of generators of the `A_f`-module `A'_f`; this entails, by virtue of hypothesis (i), that `(B_λ)_f = A'_f` for
every `λ`, or also that `u_λ⁻¹(D(f))` is contained in `Nor(X_λ)`. By virtue of (6.13.2), `S_λ` is therefore closed in
`X_λ`, and as `u_λ` is a finite morphism, `T_λ` is closed in `Y`. But for every `𝔭 ∈ Spec(A)`, there exists by virtue of
(ii) a `λ` such that `(B_λ)_𝔭 = A'_𝔭`, and consequently all points of `X_λ` over `𝔭` belong to `Nor(X_λ)`; in other
words, one has `⋂ T_λ = ∅`; as `Y` is Noetherian and the `T_λ` are closed, there exists a `λ` such that `T_λ = ∅`; hence
`B_λ` is integrally closed, and as its fraction field is `K'`, one has `B_λ = A'`. Q.E.D.

**Proposition (6.13.7).**

<!-- label: IV.6.13.7 -->

*Let `A` be a Noetherian ring, `X = Spec(A)`. The following conditions are equivalent:*

*a) For every prescheme `X'` locally of finite type over `X`, `Nor(X')` is open in `X'`.*

*b) For every finite integral `A`-algebra `A'`, `Nor(Spec(A'))` is open in `Spec(A')`.*

*c) For every prime ideal `𝔭` of `A` and every finite radicial extension `K'` of the fraction field `K` of `A/𝔭`, there
exists a sub-`A`-algebra `A'` of `K'`, finite over `A`, having `K'` as fraction field and such that `Nor(Spec(A'))` is
open in `Spec(A')`.*

The fact that a) implies b) and that b) implies c) is proved as in (6.12.4). To show that c) entails a), in view of
(6.13.2), one reduces as in (6.12.4) to proving that if `A'` is an integral `A`-algebra of finite type, the generic
point of `Spec(A')` is interior to `Nor(Spec(A'))`. One then distinguishes two cases as in (6.12.4), first proving the

**Lemma (6.13.7.1).**

<!-- label: IV.6.13.7.1 -->

*Let `A` be an integral Noetherian ring, `A'` an integral `A`-algebra of finite type, containing `A` and such that the
fraction field `K'` of `A'` is a separable extension of the fraction field `K` of `A`. If `Nor(Spec(A))` is open in
`Spec(A)`, `Nor(Spec(A'))` is open in `Spec(A')`.*

It is a question of proving (in view of (6.13.2)) that the generic point of `Spec(A')` is interior to `Nor(Spec(A'))`.
The proof follows the same course as that of (6.12.4.1), whose notations we retain. One remarks first that one may
suppose that `A` is integrally closed, and then one knows that `A_1 = A[t_1, …, t_n]` is integrally closed (Bourbaki,
*Alg. comm.*, chap. V, §1, n° 3, cor. 2 of prop. 13); one then reduces to the case where `A'` is a free `A`-module of
finite type; the reasoning of (6.12.4.1) then proves (replacing `A` if necessary by a ring `A_f` with `f ≠ 0`) that the
fibres `g⁻¹(x)` of the morphism `g : X' → X` are regular and *a fortiori* normal. Moreover `g` is flat and `X` is
normal, hence (6.5.4, (ii)) `X'` is normal.

This lemma being proved, one passes to the general case as in (6.12.4; II)), whose notations we again retain; applying
hypothesis c), one sees this time that `Nor(X_1)` is open and one thus reduces to the case where `X_1` is normal and
`g : X'_1 → X'` flat and surjective; one concludes this time that `X'` is normal by means of (6.5.4, (i)).

### 6.14. Base change and integral closure

**Proposition (6.14.1).**

<!-- label: IV.6.14.1 -->

*Let `Y`, `Y'` be two locally Noetherian preschemes, `g : Y' → Y` a normal morphism (6.8.1). Then, for every normal
`Y`-prescheme `X`, the prescheme `X' = X ×_Y Y'` is normal.*

Note that in this statement one does not suppose `X` locally Noetherian.

**Lemma (6.14.1.1).**

<!-- label: IV.6.14.1.1 -->

*Let `R` be a ring direct composition of a finite number of fields.*

<!-- original page 170 -->

*(i) For a sub-ring `A` of `R` having `R` as total ring of fractions to be normal, it is necessary and sufficient that
it be integrally closed in `R`.*

*(ii) Let `(A_λ)` be a family of normal sub-rings of `R`; if `A = ⋂ A_λ` admits `R` as total ring of fractions, then `A`
is normal.*

(i) Since `A` is a sub-ring of `R`, `A_𝔭` is a sub-ring of `R_𝔭` for every prime ideal `𝔭` of `A`, and `R_𝔭` is a ring
of fractions of `A_𝔭`; moreover `R_𝔭` is necessarily a direct composition of a finite number of fields, hence every
non-zero-divisor in `R_𝔭` is invertible; this proves that `R_𝔭` is the total ring of fractions of `A_𝔭`. If `A` is
integrally closed in `R`, `A_𝔭` is therefore integrally closed in `R_𝔭`; but if `R_𝔭` is a direct composition of at
least two fields, the integral closure of `A_𝔭` in `R_𝔭` is a direct composition of at least two rings not reduced to
`0`, which is absurd since `A_𝔭` is a local ring; hence `R_𝔭` is necessarily a field and `A_𝔭` is integral and
integrally closed, which by definition means that `A` is normal. Conversely, if `A` is normal, `R_𝔭`, the total ring of
fractions of an integral ring `A_𝔭`, is a field, and `A_𝔭` is integrally closed in `R_𝔭`; if `x ∈ R` is an element
integral over `A`, its image in each `R_𝔭` is integral over `A_𝔭`, hence belongs to `A_𝔭`; one concludes that `x ∈ A`
(Bourbaki, *Alg. comm.*, chap. II, §3, n° 3, cor. 1 of th. 1), and consequently `A` is integrally closed in `R`.

(ii) Since `A ⊂ A_λ ⊂ R` for every `λ`, `R` is also the total ring of fractions of each `A_λ`. In view of the
characterization of normal rings having `R` as total ring of fractions given in (i), assertion (ii) follows from
Bourbaki, *Alg. comm.*, chap. V, §1, n° 3, prop. 12.

This lemma being proved, the proof of (6.14.1) proceeds in several steps.

**I)** *Reduction to the case where `Y = Spec(A)`, `Y' = Spec(A')`, `X = Spec(B)`, `A`, `A'` being Noetherian local
rings, `A` integral, `B` the integral closure of `A`.* — It is a question of proving that for every `x' ∈ X'`, the local
ring `𝒪_{x'}` is integral and integrally closed; let `x`, `y`, `y'` be the canonical images of `x'` in `X`, `Y`, `Y'`
respectively; if one sets `A = 𝒪_y`, `A' = 𝒪_{y'}`, `B = 𝒪_x`, the rings `𝒪_{x'}` for `x`, `y`, `y'` fixed are the local
rings at the prime ideals of the ring `B' = B ⊗_A A'` (I, 3.6.5), and it is therefore a question of proving that `B'` is
a normal ring. Note moreover that `Spec(A') → Spec(A)` is a normal morphism by definition (6.8.1 and I, 3.6.5); one is
therefore reduced to the case where `Y` and `Y'` are local schemes, `X` the spectrum of an integrally closed integral
local ring `B`. Denote by `(B_α)` the family of integral closures of the sub-`A`-algebras of finite type of `B`; it is
clear that `B` is the union of the filtered increasing family of the `B_α`. Since the functor `lim` commutes with tensor
product, `B'` is therefore isomorphic to `lim B'_α`, where one has set `B'_α = B_α ⊗_A A'`. To prove that `B'` is
normal, it will suffice, by virtue of (5.13.6), to show that the rings `B'_α` are normal and that, for `α ≤ β`, every
irreducible component of `Spec(B'_β)` dominates an irreducible component of `Spec(B'_α)`. But this latter property
follows from the hypothesis that `A'` is a flat `A`-module and from (2.3.7, (ii)), since `B_α` and `B_β` are integral
and `B_α ⊂ B_β`.

One may therefore restrict to proving that `B' = B ⊗_A A'` is normal when `B` is

<!-- original page 171 -->

the integral closure of an integral `A`-algebra of finite type `C`; in this case, if one sets `C' = C ⊗_A A'`, the
morphism `Spec(C') → Spec(C)` is normal (6.8.2); as `B' = B ⊗_C C'`, one sees that one may replace `A` and `A'` by `C`
and `C'` respectively, hence suppose that `A` is integral and that `B` is the integral closure of `A`. Finally, the
procedure of the beginning permits one to restrict to the case where `A` is local (taking into account that, if `B` is
the integral closure of `A`, then `B_𝔭` is the integral closure of `A_𝔭` for every prime ideal `𝔭` of `A`).

**II)** *Reduction to the case where `A` is an integral local ring of dimension `1`, `B` a discrete valuation ring,
integral closure of `A`, and the morphism `Spec(B) → Spec(A)` radicial.* — Let `K` be the fraction field of `A`. One
knows (0, 23.2.7) that `B` is the intersection of a family `(V_λ)` of discrete valuation rings such that, for every
`x ∈ K`, one has `x ∈ V_λ` except for a finite number of indices `λ`. One has therefore an exact sequence of `A`-modules

```text
  0 → B → K → ⨁ (K/V_λ).
```

Set `K' = K ⊗_A A'`, `V'_λ = V_λ ⊗_A A'`; by flatness, one deduces from the preceding exact sequence a new exact
sequence

```text
  0 → B' → K' → ⨁ (K'/V'_λ)
```

and consequently `B' = ⋂ V'_λ`. Moreover `Spec(K')` is the fibre of the morphism `Spec(A') → Spec(A)` at the generic
point of `Spec(A)`, hence `K'` is a Noetherian normal ring, and consequently a direct composition of a finite number of
integral and integrally closed rings; the direct composition `L'` of the fraction fields of these latter is the total
ring of fractions of `A'`, hence also that of `B'`. One may therefore apply Lemma (6.14.1.1), and if one proves that
each of the `V'_λ` is a normal ring, the same will hold for `B'`.

One knows on the other hand (0, 23.2.7) that one may take the `V_λ` such that there is a finite sub-`A`-algebra `C` of
`K` such that `V_λ` is the integral closure of `C_{𝔭_λ}`, where `𝔭_λ` is a prime ideal of height `1` in `C`. If one sets
`C'_{𝔭_λ} = C_{𝔭_λ} ⊗_A A'`, the morphism `Spec(C'_{𝔭_λ}) → Spec(C_{𝔭_λ})` is normal (6.8.2) and one has
`V'_λ = V_λ ⊗_{C_{𝔭_λ}} C'_{𝔭_λ}`; one may therefore replace `B` by `V_λ` and `A` by `C_{𝔭_λ}`, hence suppose that `A`
is local, integral and of dimension `1`, `B` its integral closure and a discrete valuation ring. There is a finite
sub-`A`-algebra `A_1` of `B` such that the morphism `Spec(B) → Spec(A_1)` is radicial (0, 23.2.5), which entails in
particular that `A_1` is also a local ring (evidently of dimension `1`); moreover one may suppose that `B` and `A_1`
have the same residue field (*loc. cit.*). One may therefore by the same method replace `A` by `A_1`. Applying if
necessary the procedure of the beginning of I), one may finally suppose that `A'` is also a local ring and that the
homomorphism `A → A'` is local.

**III)** *End of the proof.* — We shall establish first the following lemma:

**Lemma (6.14.1.2).**

<!-- label: IV.6.14.1.2 -->

*Let `A` be an integral Noetherian local ring of dimension `1`, `A'` a Noetherian local ring, `A → A'` a local
homomorphism such that the corresponding morphism `Spec(A') → Spec(A)` is normal. Let `K` be the fraction field of `A`,
`𝔪` the maximal ideal of `A`, `k = A/𝔪` its residue field.*

<!-- original page 172 -->

*(i) If `𝔮'_j` (`1 ≤ j ≤ r`) are the minimal prime ideals of `A'`, then `K' = K ⊗_A A'` is a direct composition of
integral and integrally closed rings `K'_j ⊃ A'/𝔮'_j` (`1 ≤ j ≤ r`), `K'_j` having as fraction field the fraction field
`L'_j` of `A'/𝔮'_j` (`1 ≤ j ≤ r`), so that the total ring of fractions `L'` of `A'` is identified with the direct
composition of the `L'_j` and `A'` with a sub-ring of `K'`.*

*(ii) The ideal `𝔭' = 𝔪 A'` of `A'` is prime; the ring `A'_{𝔭'}` is of dimension `1` and is identified with a sub-ring
of the product of the fields `L'_j` for the indices `j` such that `𝔮'_j ⊂ 𝔭'`.*

*(iii) If `Â'_{𝔭'}` denotes the sub-ring of `L'` product of `A'_{𝔭'}` and of the `L'_j` such that `𝔮'_j ⊄ 𝔭'`, one has*

```text
  (6.14.1.3)              A' = K' ∩ Â'_{𝔭'}.
```

Assertion (i) has already been seen in the course of the proof of II) and is independent of the dimension hypothesis on
`A`. The hypothesis that the morphism `Spec(A') → Spec(A)` is normal entails that `A' ⊗_A k = A'/𝔪A'` is a normal local
Noetherian ring, hence *integral*, which already shows that `𝔭' = 𝔪 A'` is prime. One has, by (6.1.2),
`dim(A'_{𝔭'}) = dim(A) + dim(A'_{𝔭'}/𝔪 A'_{𝔭'})`. But `A'_{𝔭'}/𝔪 A'_{𝔭'} = A'_{𝔭'}/𝔭' A'_{𝔭'}` is the residue field of
`A'_{𝔭'}`, hence `dim(A'_{𝔭'}) = 1`. The fact that `A'_{𝔭'}` is contained in the direct composition of the `L'_j` such
that `𝔮'_j ⊂ 𝔭'` follows from the fact that the ideals `𝔮'_j A'_{𝔭'}` for these indices `j` are the minimal prime ideals
of `A'_{𝔭'}`.

It remains to prove (6.14.1.3). One has evidently `A' ⊂ K' ∩ Â'_{𝔭'}`. Conversely, let `y'` be an element of this
intersection; let `a` be a "parameter" for `A`, so that `Aa` is `𝔪`-primary, and let `a'` be the image of `a` in `A'`;
every element of `K` may be written `x/aⁿ` for `x ∈ A` and an integer `n > 0`, since `Aa` contains a power of `𝔪`; hence
one may write `y' = x'/a'ⁿ` with `x' ∈ A'`. Note now that `𝔭'` is the only prime ideal associated with
`A'/aⁿA' = (A/aⁿA) ⊗_A A'`: as `A'` is a flat `A`-module, this follows from (3.3.1), `𝔪` being the only prime ideal
associated with `A/aⁿA` and `k ⊗_A A'` being integral. Consequently, `aⁿ A'` is the inverse image in `A'` of
`a'ⁿ A'_{𝔭'}`; as by hypothesis `y' ∈ Â'_{𝔭'}`, the image of `x'` in `A'_{𝔭'}` belongs to `a'ⁿ A'_{𝔭'}`; whence
`x' ∈ aⁿA'` and `y' ∈ A'`, which completes the proof.

This lemma being established, in the case to which we are reduced at the end of II), `B'` is radicial over `A'` (I,
3.5.7) and consequently is also a *local* ring; moreover `B'` is integral over `A'`, hence, if `𝔮'` is the unique prime
ideal of `B'` above `𝔭'`, `𝔮' B'_{𝔭'}` is the only maximal ideal of `B'_{𝔭'}` (Bourbaki, *Alg. comm.*, chap. V, §2, n°
1, prop. 1), hence `B'_{𝔮'} = B'_{𝔭'} = B ⊗_A A'_{𝔭'}`. We shall first show that `B'_{𝔭'}` is a Noetherian and normal
ring. Now, since `B` contains `A` and is contained in `K` and `A'_{𝔭'}` is a flat `A`-module, `B'_{𝔭'}` contains
`A'_{𝔭'}` and is contained in `K'_{𝔭'}`, hence in the product `L''` of the `L'_j` such that `𝔮'_j ⊂ 𝔭'`. For every index
`j` such that `𝔮'_j ⊄ 𝔭'`, let `𝔡'_j` be the product of the `L'_h` such that `h ≠ j`, so that `𝔡'_j ∩ A' = 𝔮'_j`; as
every element of `A − 𝔭'` is regular in `L''`, one has also

```text
  𝔡'_j ∩ A'_{𝔭'} = 𝔮'_j A'_{𝔭'}.
```

Let `𝔯'_j = B'_{𝔭'} ∩ 𝔡'_j`, so that `B'_{𝔭'}/𝔯'_j` is isomorphic to the projection of `B'_{𝔭'}` in `L'_j`; hence
`B'_{𝔭'}/𝔯'_j` contains the integral local ring of dimension `1`, `A'_{𝔭'}/𝔮'_j A'_{𝔭'}`, and is contained in its
fraction field `L'_j`; it is consequently Noetherian by virtue of the Krull-Akizuki theorem (Bourbaki, *Alg. comm.*,
chap. VII, §2, n° 5, prop. 5).

<!-- original page 173 -->

Since the intersection of the `𝔯'_j` is reduced to `0`, one deduces that `B'_{𝔭'}` itself is Noetherian, by reason of
the following classical lemma:

**Lemma (6.14.1.4).**

<!-- label: IV.6.14.1.4 -->

*Let `R` be a ring, `𝔞` and `𝔟` two ideals of `R`; if `R/𝔞` and `R/𝔟` are Noetherian, the same holds for `R/(𝔞 ∩ 𝔟)`.*

Indeed, let `𝔠` be an ideal of `R` such that `𝔞 ∩ 𝔟 ⊂ 𝔠`; one has therefore `𝔞 ∩ 𝔟 ⊂ 𝔞 ∩ 𝔠 ⊂ 𝔠`; now `𝔠/(𝔞 ∩ 𝔠)` is an
`R`-module isomorphic to `(𝔞 + 𝔠)/𝔞`, hence to an ideal of `R/𝔞`, and consequently is of finite type; on the other hand
`(𝔞 ∩ 𝔠)/(𝔞 ∩ 𝔟)` is a sub-`R`-module of `𝔞/(𝔞 ∩ 𝔟)`, and this latter is isomorphic to `(𝔞 + 𝔟)/𝔟`, hence is of finite
type as an ideal of `R/𝔟`; hence `(𝔞 ∩ 𝔠)/(𝔞 ∩ 𝔟)` is also an `R`-module of finite type, and so is `𝔠/(𝔞 ∩ 𝔟)`.

Note on the other hand that `Spec(A)` consists of the closed point `𝔪` and the generic point `(0)`, of residue fields
`k` and `K` respectively; as in the case in which we have placed ourselves, the fraction field of `B` and its residue
field are respectively isomorphic to `K` and `k`, the fibres of the morphism `u : Spec(B'_{𝔭'}) → Spec(B)` at the closed
point and at the generic point of `Spec(B)` are respectively isomorphic to the fibres of the morphism
`Spec(A'_{𝔭'}) → Spec(A)` at the closed point and at the generic point of `Spec(A)` (I, 3.6.4), hence are geometrically
normal by hypothesis; as moreover the morphism `u` is flat, one concludes that it is normal (6.8.1). But since `B` and
`B'_{𝔭'}` are Noetherian and `B` is normal, one deduces from (6.5.4) that `B'_{𝔭'}` is normal.

This being so, `B` is the union of the increasing filtered family of its finite sub-`A`-algebras `A_α`; by flatness,
`B'` is the union of the increasing filtered family of the `A'_α = A_α ⊗_A A'`; if one sets `𝔭'_α = 𝔮' ∩ A'_α`,
`B'_{𝔮'}` is also the union of the increasing filtered family of the `(A'_α)_{𝔭'_α}` (5.13.3). Denote by `L''` the
direct composition of the fields `L'_j` such that `𝔮'_j ⊄ 𝔭'`; then for every `α`, `(A'_α)_{𝔭'_α}` is contained in
`K'_{𝔭'}`, and the ring `B'_{𝔮'} ≅ L'' × B'_{𝔭'}` is therefore the union of the rings
`L'' × (A'_α)_{𝔭'_α} = (Â'_α)_{𝔭'_α}`. But each of the `A_α` is local, Noetherian, integral and of dimension `1`, and
the morphism `Spec(A'_α) → Spec(A_α)` is normal (6.8.2), hence one may apply Lemma (6.14.1.2) to it and one has

```text
  A'_α = K' ∩ (Â'_α)_{𝔭'_α}
```

for every `α`; taking the inductive limit of each of the two members, it comes

```text
  B' = K' ∩ B'_{𝔮'}.
```

But `B'_{𝔮'}`, direct composition of the normal rings `L''` and `B'_{𝔭'}`, is normal, and as the same holds for `K'`,
Lemma (6.14.1.1) shows that `B'` is normal. Q.E.D.

**Corollary (6.14.2).**

<!-- label: IV.6.14.2 -->

*Let `k` be a field, `X` a normal `k`-prescheme (not necessarily locally Noetherian). Then, for every separable
extension `k'` of `k`, `X' = X ⊗_k k'` is normal.*

One knows indeed (6.7.6) that the morphism `Spec(k') → Spec(k)` is then normal.

**Corollary (6.14.3).**

<!-- label: IV.6.14.3 -->

*Let `k` be a field; `X`, `Y` two integral and normal `k`-preschemes, whose fields of rational functions `K = R(X)`,
`L = R(Y)` are separable extensions of `k`. Then the prescheme `X ×_k Y` is normal.*

<!-- original page 174 -->

The question being local on `X` and `Y`, one may suppose that `X = Spec(A)`, `Y = Spec(B)`, where `A` and `B` are two
integral and integrally closed rings, of fraction fields `K` and `L` respectively; suppose first that `A` is a
`k`-algebra of finite type, hence `K` an extension of finite type of `k`. By flatness, `A ⊗_k B` is a sub-ring of
`K ⊗_k L`; now `K ⊗_k L` is a Noetherian normal ring (by virtue of (6.7.4.1) or (6.14.2)), hence direct composition of
integral rings `C_i` in finite number, so that if `E_i` is the fraction field of `C_i`, the direct composition `E` of
the `E_i` is the total ring of fractions of `K ⊗_k L`; this is moreover also the total ring of fractions of `A ⊗_k B`,
since `K ⊗_k L` is a ring of fractions of `A ⊗_k B`. This being so, one may write `A ⊗_k B = (A ⊗_k L) ∩ (K ⊗_k B)`, and
it follows from (6.14.2) that `A ⊗_k L` and `K ⊗_k B` are normal, hence `A ⊗_k B` is normal by virtue of (6.14.1.1).

Consider now the general case; `A` is then the union of the increasing filtered family of its sub-`k`-algebras of finite
type `A_α`, hence `A ⊗_k B` is the inductive limit of the normal rings `A_α ⊗_k B`. To prove that `A ⊗_k B` is normal,
it suffices therefore (5.13.6) to prove that every irreducible component of `Spec(A_β ⊗_k B)` dominates an irreducible
component of `Spec(A_α ⊗_k B)` for `A_α ⊂ A_β`, which follows at once from the fact that `B` is a flat `k`-module, from
(2.3.7, (ii)) and from the fact that `A_α` and `A_β` are integral rings.

**Proposition (6.14.4).**

<!-- label: IV.6.14.4 -->

*Let `A` be a Noetherian ring, `A'` a Noetherian `A`-algebra such that the morphism `Spec(A') → Spec(A)` is normal. Let
`B` be an `A`-algebra, `C` the integral closure of `A` in `B`; set `B' = B ⊗_A A'`, `C' = C ⊗_A A'`, `C'` identifying
with a sub-ring of `B'`; then `C'` is the integral closure of `A'` in `B'`.*

We proceed in several steps.

**I)** *Reduction to the case where the ring `B` is reduced.* — Set `B_0 = B_{red} = B/𝔑`, where `𝔑` is the nilradical
of `B`, and let `C_0` be the integral closure of `A` in `B_0`. One has the following lemma:

**Lemma (6.14.4.1).**

<!-- label: IV.6.14.4.1 -->

*Let `A` be a ring, `B` an `A`-algebra, `B_0 = B/𝔫` the quotient of `B` by a nil-ideal. If `C_0` is the integral closure
of `A` in `B_0`, the inverse image `C` of `C_0` by the canonical homomorphism `φ : B → B_0` is the integral closure of
`A` in `B`.*

Indeed, if `x ∈ B` is such that `φ(x)` satisfies an integral dependence equation with coefficients in `A`, one deduces
that `x` satisfies a relation of the form `xⁿ + a_1 xⁿ⁻¹ + ⋯ + a_n = z` with `a_i ∈ A` and `z ∈ 𝔫`, whence, by raising
to a sufficiently large power, an integral dependence equation for `x`, with coefficients in `A`.

One has therefore the exact sequence of `A`-modules

```text
  0 → C → B → B_0/C_0
```

whence, by flatness, the exact sequence

```text
  0 → C' → B' → B'_0/C'_0
```

where one has set `B'_0 = B_0 ⊗_A A'`, `C'_0 = C_0 ⊗_A A'`. If one proves that `C'_0` is the integral closure of `A'` in
`B'_0`, Lemma (6.14.4.1) will prove that `C'` is the integral closure of `A'` in `B'`.

**II)** *Reduction to the case where `B` is an integral `A`-algebra of finite type containing `A`.* — Let `(B_α)` be the
increasing filtered family of sub-`A`-algebras of finite type of `B`, and let `C_α` be the integral closure

<!-- original page 175 -->

of `A` in `B_α`. It follows at once from the definition of the integral closure that `C` is the union of the `C_α`; if
one sets `B'_α = B_α ⊗_A A'`, `C'_α = C_α ⊗_A A'`, then `C'_α` is contained in `B'_α` by flatness, and for the same
reason `B'` is the union of the increasing filtered family of the `B'_α` and `C'` the union of the increasing filtered
family of the `C'_α`. If one proves that `C'_α` is the integral closure of `A'` in `B'_α`, it will follow at once that
`C'` is the integral closure of `A'` in `B'`. One may therefore restrict to the case where `B` is an `A`-algebra of
finite type, hence Noetherian; let `𝔮_i` (`1 ≤ i ≤ n`) be its minimal prime ideals; as `B` is supposed reduced, it is
identified with a sub-ring of the product `B_0` of the `B/𝔮_i`; if `C_0` is the integral closure of `A` in `B_0`, one
has `C = B ∩ C_0`; if one sets `B'_0 = B_0 ⊗_A A'`, `C'_0 = C_0 ⊗_A A'`, one has, by flatness, `C' = B' ∩ C'_0`
`(0_I, 6.1.3)`; it therefore suffices to prove that `C'_0` is the integral closure of `A'` in `B'_0`. But `C_0` is the
direct composition of the `C_i`, integral closures of `A` in `B_i = B/𝔮_i`; consequently `C'_0` is the direct
composition of the `C'_i = C_i ⊗_A A'` and it suffices to show that `C'_i` is the integral closure of `A'` in
`B'_i = B_i ⊗_A A'`. One is thus reduced to the case where `B` is integral and an `A`-algebra of finite type; if `𝔭` is
the kernel of the homomorphism `A → B`, one has also `B' = B ⊗_{A/𝔭}(A'/𝔭A')`; as the morphism
`Spec(A'/𝔭A') → Spec(A/𝔭)` is normal, one may replace `A` by `A/𝔭` and `A'` by `A'/𝔭A'`, and consequently suppose that
`A ⊂ B`.

**III)** *Case where `A` is a field, `B` a field, extension of finite type of `A` and such that `A` is algebraically
closed in `B`.* — One has then `C = A`, and `A'` is a Noetherian geometrically normal `A`-algebra, hence direct
composition of integral and integrally closed rings `A'_λ`, the fraction fields `K'_λ` of the `A'_λ` being separable
extensions of `A` (4.6.1). The `A'`-algebra `B'` is therefore direct composition of the `B ⊗_A A'_λ = B'_λ`, and one may
therefore restrict to the case where `A'` is integral, its fraction field `K'` being a separable extension of `A`. Now,
as `B` is a flat `A`-module, `B ⊗_A A' = B'` is identified with a sub-ring of `B ⊗_A K'`; as `K'` is a separable
extension of `A`, `B ⊗_A K'` is reduced (4.3.7), and as moreover `B` is a primary extension of `A`, `B ⊗_A K'` is
integral (4.3.2); the same therefore holds for `B'`. Let `L'` be the fraction field of `B ⊗_A K'` (which is also that of
`B'`); it is evidently a composite field `B(K')` of its sub-fields `B` and `K'`; as `A` is algebraically closed in `B`,
`K'` is a separable extension of `A`, and `B` and `K'` are linearly disjoint over `A`, `K'` is algebraically closed in
`B(K') = L'` (Bourbaki, *Alg.*, chap. V, §9, exerc. 2); *a fortiori* `A'`, being integrally closed, is integrally closed
in `L'`, hence in `B'`, which proves the proposition in this case.

**IV)** *Case where `A` is integral, `B` a field, finite extension of the fraction field `K` of `A`.* — Then
`B' = A' ⊗_A K ⊗_K B` is a Noetherian geometrically normal `B`-algebra, and consequently `B'` is direct composition of
integral rings; the total ring of fractions `L'` of `B'` is then direct composition of a finite number of fields. This
being so, as `B` is the fraction field of `C`, `B'` is a ring of fractions of `C'` and `L'` is therefore also the total
ring of fractions of `C'`. Now (6.14.1), since `C` is a normal ring and `Spec(A') → Spec(A)` a normal morphism of
Noetherian rings, `C'` is a normal ring; but it follows from (6.14.1.1) that `C'` is then integrally closed in `L'`, and
*a fortiori* in `B'`, and consequently is the integral closure of `A'` in `B'`.

<!-- original page 176 -->

**V)** *End of the proof.* — According to II), one may suppose that `B` is an integral `A`-algebra of finite type
containing `A`. Let `K` be the fraction field of `A`, `L` that of `B`, which is an extension of finite type of `K`. Let
`M` be the algebraic closure of `K` in `L`, which is a finite algebraic extension of `K`; let `C_0` be the integral
closure of `A` in `M`, which is also the integral closure of `A` in `L`; one has therefore `C = B ∩ C_0`; if one sets
`C'_0 = C_0 ⊗_A A'`, one has consequently `C' = B' ∩ C'_0` by flatness `(0_I, 6.1.3)`. Now, it follows from IV) that
`C'_0` is the integral closure of `A'` in `M' = M ⊗_A A'`; moreover, `M'` is a Noetherian ring and the morphism
`Spec(M') → Spec(M)` is normal (as one saw in IV)); applying III) to `M` and `M'` in place of `A` and `A'` and to `L` in
place of `B`, one deduces that `M'` is integrally closed in `L' = L ⊗_A A'`; hence `C'_0` is the integral closure of
`A'` in `L'`, and `C' = C'_0 ∩ B'` is the integral closure of `A'` in `B'`. Q.E.D.

**Corollary (6.14.5).**

<!-- label: IV.6.14.5 -->

*Let `A` be a Noetherian ring, `A'` a Noetherian `A`-algebra such that the morphism `Spec(A') → Spec(A)` is normal. Let
`B`, `C` be two `A`-algebras, `φ : B → C` an `A`-homomorphism making `C` into a `B`-algebra, `D` the integral closure of
`B` in `C`. If one sets `B' = B ⊗_A A'`, `C' = C ⊗_A A'`, `D' = D ⊗_A A'`, then `D'` is the integral closure of `B'` in
`C'`.*

Let `(B_λ)` be the increasing filtered family of sub-`A`-algebras of finite type of `B`, and set `B'_λ = B_λ ⊗_A A'`, so
that `B'` is the union of the increasing filtered family of the sub-`A'`-algebras of finite type `B'_λ`. Let `D_λ` be
the integral closure of `B_λ` in `C`, and set `D'_λ = D_λ ⊗_A A'`, so that `D` is the union of the `D_λ` and `D'` the
union of the `D'_λ`; if we prove that `D'_λ` is the integral closure of `B'_λ` in `C'`, it will follow that `D'` is the
integral closure of `B'` in `C'`. Now `B_λ` and `B'_λ` are Noetherian and the morphism `Spec(B'_λ) → Spec(B_λ)` is
normal (6.8.2); one may therefore apply (6.14.4) replacing `A`, `A'` and `B` by `B_λ`, `B'_λ` and `C` respectively,
whence the corollary.

One may for example apply (6.14.5) when `A` is an excellent local ring and `A'` its completion `Â`, since in this case
`Spec(A') → Spec(A)` is a regular morphism (7.8.2).

### 6.15. Geometrically unibranch preschemes

**(6.15.1).**

<!-- label: IV.6.15.1 -->

We shall say that a prescheme `X` is **unibranch** (resp. **geometrically unibranch**) at a point `x`, or that the point
`x` is unibranch (resp. geometrically unibranch) in `X`, if the local ring `𝒪_x` is unibranch (resp. geometrically
unibranch) (0, 23.2.1); we shall say that `X` is unibranch (resp. geometrically unibranch) if it is so at every point.
It follows from this definition that, for `X` to be unibranch (resp. geometrically unibranch) at a point, it is
necessary and sufficient that `X_{red}` be so at this point.

**(6.15.2).**

<!-- label: IV.6.15.2 -->

One must take care that, with the definitions of (6.15.1), a local ring `A` may be unibranch (resp. geometrically
unibranch) without `Spec(A)` being so; in other words, it may happen that there are prime ideals `𝔭` of `A` such that
`A_𝔭` is not unibranch; it amounts to the same to say that on a prescheme, the notion of geometrically unibranch point
is not stable under generization. We shall see this on the following example.

<!-- original page 177 -->

Let `K` be an algebraically closed field of characteristic `0`, `B` the integral ring
`K[U, V, W]/(U²(U − W) − V²(U + W))` (`U`, `V`, `W` indeterminates), so that `Y = Spec(B)` is a "cone with vertex at the
origin, having a double generator". We shall denote by `u`, `v`, `w` the images of `U`, `V`, `W` in `B`. Let `R` be the
fraction field of `B`, and consider in `R` the element `t = v(u + w)/u`, which does not belong to `B`; we show that
`C = B[t]` is the integral closure of `B`. Indeed, one has `t² = u² − w²`, hence `t` is integral over `B`, and
`v = tu/(u + w)`; the ring `C_1 = K[t, u, w]` is integrally closed, for it is isomorphic to `K[T, U, W]/(T² − U² + W²)`
and is therefore the integral closure of the integrally closed ring `K[U, W]` in the quadratic extension
`K(U, W)(√(U² − W²))` of its fraction field (Bourbaki, *Alg. comm.*, chap. V, §1, n° 6, prop. 18). The ring of fractions
`K[t, u, w, 1/(u + w)]` of `C_1` is therefore also integrally closed. In the same way, one sees that the ring
`C_2 = K[t, v, w]` is integrally closed, for `t` satisfies an integral dependence equation over `K[v, w]` (an explicit
polynomial relation deducible from `t² = u² − w²` and `v = tu/(u + w)` by eliminating `u`), and consequently
`K[t, v, w, 1/(t − v)] = K[t, v/(u + w), w, 1/(tw)]` is integrally closed. Finally, taking into account that `u` and `w`
are algebraically independent over `K`, one easily proves that
`C = K[t, u, v, w] = K[t, u, w, 1/(u + w)] ∩ K[t, v, w, 1/(t − v)]`, which completes the proof that `C` is the integral
closure of `B`. It is immediate that if `𝔪_0` is the maximal ideal of `B` generated by `u`, `v`, `w` ("vertex of the
cone"), there exists a single maximal ideal `𝔫_0` of `C` above `𝔪_0`, namely the ideal generated by `t`, `u`, `v`, `w`.
If one sets `A = B_{𝔪_0}`, one deduces easily that `A' = C_{𝔫_0}` is the integral closure of `A`, which is therefore
unibranch, and consequently also geometrically unibranch since its residue field `K` is algebraically closed. But in `A`
the prime ideal `𝔭` generated by `u` and `v` is such that the integral closure `A_𝔭[t]` of `A_𝔭` is not a local ring.

We shall see however further on (9.7.10) that when `X` is a locally Noetherian prescheme such that, if `X'` is the
normalization of `X_{red}`, the canonical morphism `X' → X` is finite (which will be the case if `X` is such that the
rings of its affine open sets are universally Japanese (0, 23.1.1)), then the set of points `x ∈ X` where `X` is
geometrically unibranch is locally constructible.

**(6.15.3).**

<!-- label: IV.6.15.3 -->

We shall say for short that a morphism `f : X → Y` is **radicial at a point** `y ∈ Y` if `f⁻¹(y)` is empty or reduced to
a single point `x` and if `k(x)` is a radicial extension of `k(y)`. It amounts to the same to say that `f` is radicial
at all points of `Y` or that `f` is radicial (I, 3.5.8). If `g : f⁻¹(y) → Spec(k(y))` is the inverse image morphism of
`f` by the base change `Spec(k(y)) → Y`, it amounts to the same to say that `f` is radicial at the point `y ∈ Y`, or
that `g` is radicial.

**Lemma (6.15.3.1).**

<!-- label: IV.6.15.3.1 -->

*(i) Let `f : X → Y`, `g : Y → Z` be two morphisms. If `f` is radicial at a point `y` and `g` radicial at the point
`z = g(y)`, then `g ∘ f` is radicial at the point `g(y)`. The converse is true if `f` is surjective.*

*(ii) Let `f : X → Y`, `h : Y' → Y` be two morphisms, and let `f' = f_{(Y')} : X ×_Y Y' → Y'`. Let `y' ∈ Y'` and
`y = h(y')`; then for `f` to be radicial at the point `y`, it is necessary and sufficient that `f'` be radicial at the
point `y'`.*

<!-- original page 178 -->

(i) If `f` is radicial at the point `y` and `g` radicial at the point `z`, then `g⁻¹(z)` is reduced to `y` and
`f⁻¹(g⁻¹(z)) = f⁻¹(y)` is empty or reduced to a single point `x`; moreover `k(x)` is a radicial extension of `k(y)` and
`k(y)` a radicial extension of `k(z)`, hence `k(x)` is a radicial extension of `k(z)`. Conversely, suppose `f`
surjective; if `g ∘ f` is radicial at the point `z = g(y)`, then `g⁻¹(z)` reduces to the single point `y`, otherwise
`f⁻¹(g⁻¹(z))` would have at least two distinct points; moreover, `f⁻¹(y) = f⁻¹(g⁻¹(z))` reduces to a single point `x`,
and by hypothesis one has `k(z) ⊂ k(y) ⊂ k(x)`, and `k(x)` is radicial over `k(z)`, hence `k(y)` is radicial over `k(z)`
and `k(x)` radicial over `k(y)`.

(ii) Let `g : f⁻¹(y) → Spec(k(y))`, `g' : f'⁻¹(y') → Spec(k(y'))` be the inverse image morphisms of `f` and `f'`
respectively; as `f'⁻¹(y') = f⁻¹(y) ⊗_{k(y)} k(y')` (I, 3.6.4), `g'` is the inverse image of `g`, and the assertion
reduces to (2.6.1, (v)).

Let then `X` be a reduced prescheme having only a finite number of irreducible components, and let `X'` be its
normalization (II, 6.3.8); one knows (*loc. cit.*) that the canonical morphism `f : X' → X` is surjective. The
definition (6.15.1) then shows that for `X` to be geometrically unibranch at a point `x`, it is necessary and sufficient
that `f` be radicial at this point; for `X` to be geometrically unibranch, it is therefore necessary and sufficient that
`f` be radicial.

**(6.15.4).**

<!-- label: IV.6.15.4 -->

Generalizing the definition given in (I, 2.2.9), we shall say that, for two reduced preschemes `X`, `Y`, a morphism
`f : X → Y` is **birational** if the restriction of `f` to the set of maximal points of `X` is a bijection of this set
onto the set of maximal points of `Y`, and if, for every maximal point `y` of `Y`, the morphism
`X ×_Y Spec(𝒪_y) → Spec(𝒪_y)` deduced from `f` is an isomorphism (in other words, if the fibre `f⁻¹(y)` reduces to a
single point `x` (maximal in `X`) and if the homomorphism `k(y) → k(x)` deduced from `f` is bijective); this notion
reduces to that of (I, 2.2.9) when `X` and `Y` have only a finite number of irreducible components.

**Lemma (6.15.4.1).**

<!-- label: IV.6.15.4.1 -->

*Let `f : X → Y` be a morphism, `g : Y' → Y` a flat morphism, `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`. If `f` is
birational, the same holds for `f'`.*

Indeed, if `y'` is a maximal point of `Y'`, one knows (2.3.4, (ii)) that `y = g(y')` is a maximal point of `Y`; there
exists a single point `x` of `X` in `f⁻¹(y)` by hypothesis; moreover `x` is maximal in `X` and such that `k(x) = k(y)`.
It follows therefore from (I, 3.4.9) that `f'⁻¹(y')` reduces to a single point `x'` and that `k(x') = k(y')`. One
concludes the reasoning by remarking that according to (2.3.7, (ii)), every irreducible component of `X'` dominates an
irreducible component of `Y'`.

**Proposition (6.15.5).**

<!-- label: IV.6.15.5 -->

*Let `f : X → Y` be a morphism such that `f_{red}` is integral and birational (6.15.4), hence surjective.*

*(i) For `Y` to be geometrically unibranch at a point `y`, it is necessary and sufficient that `f` be radicial at the
point `y` and that `X` be geometrically unibranch at the unique point `x` of `f⁻¹(y)`.*

*(ii) For `Y` to be geometrically unibranch, it is necessary and sufficient that `X` be geometrically unibranch and that
`f` be radicial.*

One may evidently restrict to the case where `X` and `Y` are reduced; the fact that `f` is surjective follows from the
fact that `f` is a closed morphism (II, 6.1.10) and that `f(X)` contains by hypothesis all maximal points of `Y`. This
shows at once that (i) entails (ii). Using (I, 3.6.5) and (II, 6.1.5), one may suppose, to prove (i), that
`Y = Spec(𝒪_{Y,y})`,

<!-- original page 179 -->

in other words `Y = Spec(A)`, where `A` is local. As `f` is affine, one has also `X = Spec(B)`. If `A` is geometrically
unibranch, it is integral, hence the same holds for `B` since `f` is birational; conversely, if `f` is radicial at the
point `y` and `X` geometrically unibranch at the point `x`, `B` has only a single maximal ideal (since it is integral
over `A` and every maximal ideal of `B` is therefore above that of `A`), in other words `B` is a local ring, and to say
that `X` is geometrically unibranch at the point `x` means that `B` is geometrically unibranch, hence integral. As `f`
is dominant by hypothesis and `A` is reduced, one concludes that `A ⊂ B` (I, 1.2.7); hence `A` is also integral. Thus,
to prove (i), one may restrict to the case where `A` and `B` are local, integral, `A` being contained in `B` and having
the same fraction field, and consequently (since `B` is integral over `A`) the same integral closure `C`. But then the
assertion follows from (6.15.3.1, (i)) applied to the morphisms `Spec(C) → Spec(B)` and `Spec(B) → Spec(A)`, in view of
the interpretation given in (6.15.3) of the property of being geometrically unibranch at a point.

**Proposition (6.15.6).**

<!-- label: IV.6.15.6 -->

*Let `k` be a field, `X` a `k`-prescheme. If `X` is normal, then, for every extension `k'` of `k`, `X' = X ⊗_k k'` is
geometrically unibranch.*

One knows that `k'` is an algebraic extension of a pure extension `k_0` of `k`, and if `k''` is the largest separable
extension of `k_0` contained in `k'`, `k'` is a radicial extension of `k''` and `k''` a separable extension of `k`. One
knows (6.14.2) that `X'' = X ⊗_k k''` is normal; as `X ⊗_k k' = X'' ⊗_{k''} k'`, one sees that one may restrict to the
case where the extension `k'` of `k` is radicial. Moreover (I, 3.6.5), one may suppose that `X = Spec(A)`, where `A` is
an integrally closed integral local ring (since `X` is normal). The projection morphism `f : X' → X` is a homeomorphism,
since `Spec(k') → Spec(k)` is a universal homeomorphism (2.4.5); as `X' = Spec(A')` where `A' = A ⊗_k k'`, one sees
therefore that `A'` is a local ring whose nilradical `𝔑'` is the unique minimal prime ideal, whence
`X'_{red} = Spec(A_0)`, where `A_0 = A'/𝔑'` is an integral local ring; moreover, if `K` is the fraction field of `A`,
the fraction field `K_0` of `A_0` is radicial over `K`, since the morphism `f` is radicial. As `A_0` is integral over
`A`, its integral closure `B` is also the integral closure of `A` in `K_0`. But as `A` is integrally closed, one knows
(Bourbaki, *Alg. comm.*, chap. V, §2, n° 3, lemma 3) that `B` is the set of `x ∈ K_0` of which some `pᵐ`-th power (for
`m` sufficiently large) belongs to `A` (`p` being the characteristic exponent of `K`); moreover there exists only one
prime ideal of `B` above each prime ideal of `A`; in particular `B` is a local ring and its residue field is a radicial
extension of that of `A`, and *a fortiori* of that of `A_0`, which proves that `A_0` is geometrically unibranch, and
consequently the same holds for `X'`.

**Proposition (6.15.7).**

<!-- label: IV.6.15.7 -->

*Let `k` be a field, `X` a `k`-prescheme, `k'` an extension of `k`, `X' = X ⊗_k k'`. Let `x'` be a point of `X'`, `x`
its projection in `X`. For `X` to be geometrically unibranch at the point `x`, it is necessary and sufficient that `X'`
be geometrically unibranch at the point `x'`. For `X` to be geometrically unibranch, it is necessary and sufficient that
`X'` be so.*

The second assertion follows from the first and from the fact that the projection `f : X' → X` is a surjective morphism.
To prove the first assertion, one may, by virtue of (I, 5.1.8), restrict to the case where `X` is reduced, and by virtue
of (I, 3.6.5), to the case

<!-- original page 180 -->

where `X = Spec(A)` (with `A = 𝒪_{X,x}`) is a local scheme. Note that `A' = 𝒪_{X',x'}` is by hypothesis a faithfully
flat `A`-module, hence containing `A`, and consequently the hypothesis that `X` is geometrically unibranch at the point
`x`, or the hypothesis that `X'` is geometrically unibranch at the point `x'`, both entail that `A` is an integral local
ring (since `A`, being reduced, is also isomorphic to a sub-ring of `A'`). Let `K` be the fraction field of `A`, `B` the
integral closure of `A`, and set `Y = Spec(B)`; it amounts to the same to say that `X` is geometrically unibranch at the
point `x` or that the morphism `g : Y → X` is radicial at the point `x` (6.15.3). Let `Y' = Y ⊗_k k' = Y ×_X X'`, so
that one has the commutative diagram

```text
              Y  ⟵ Y'
              ↓     ↓
              X  ⟵ X'
                 f
```

Note that `f` is a flat morphism; hence (6.15.4.1) the integral morphism `g'` is birational. On the other hand, as `Y`
is normal, `Y'` is geometrically unibranch (6.15.6). For `X'` to be geometrically unibranch at `x'`, it is therefore
necessary and sufficient that `g'` be radicial at the point `x'` (6.15.5). Now, `x` is the projection of `x'` in `X` and
it is equivalent to say that `g` is radicial at the point `x` or that `g'` is radicial at the point `x'` (6.15.3.1);
finally, for `X` to be geometrically unibranch at the point `x`, it is necessary and sufficient that `g` be radicial at
this point, whence the proposition.

**Lemma (6.15.8).**

<!-- label: IV.6.15.8 -->

*Let `k` be a separably closed field (in other words, such that the algebraic closure of `k` is radicial over `k`), `X`
a `k`-prescheme locally of finite type over `k`, `x` a closed point of `X`. If `X` is unibranch at the point `x`, it is
geometrically unibranch at this point.*

Indeed, one knows (I, 6.4.2) that `k(x)` is an algebraic extension of `k`; as the residue field of the integral closure
of `(𝒪_x)_{red}` (integral closure which is by hypothesis a local ring) is an algebraic extension of `k(x)`, it is a
radicial extension of `k` by hypothesis, hence also of `k(x)`.

**Corollary (6.15.9).**

<!-- label: IV.6.15.9 -->

*Let `k` be a field, `X` a `k`-prescheme locally of finite type over `k`, `k'` a separably closed extension of `k` (in
other words, such that the algebraic closure of `k'` is radicial over `k'`); then, for `X` to be geometrically
unibranch, it is necessary and sufficient that `X' = X ⊗_k k'` be unibranch.*

In view of (6.15.7), one is reduced to proving that if `X` is unibranch and `k` separably closed, then `X` is
geometrically unibranch. Now, `X` is geometrically unibranch at its closed points (6.15.8); we shall conclude in
(10.4.9) that `X` is geometrically unibranch at all its points, by relying on the fact (signalled at the end of
(6.15.2)) that the set of points where `X` is geometrically unibranch is constructible (of course, cor. (6.15.9) will
not be used until then).

This result justifies, to a certain extent, the terminology "geometrically unibranch".

<!-- original page 181 -->

**Proposition (6.15.10).**

<!-- label: IV.6.15.10 -->

*Let `Y`, `Y'` be two locally Noetherian preschemes, `g : Y' → Y` a normal morphism (6.8.1), `f : X → Y` a morphism; set
`X' = X ×_Y Y'` and let `p : X' → X` be the canonical projection, `x'` a point of `X'`. Then, if `X` is reduced (resp.
geometrically unibranch, resp. integral and geometrically unibranch) at the point `x = p(x')`, `X'` is reduced (resp.
geometrically unibranch, resp. integral and geometrically unibranch) at the point `x'`.*

By virtue of (I, 3.6.5), one may restrict to the case where `Y = Spec(A)`, `Y' = Spec(A')`, `X = Spec(B)`, where `A`,
`A'` and `B` are local rings, the homomorphisms `A → A'` and `A → B` being local, `A`, `A'` Noetherian rings, and `x`
being the closed point of `X`; it is a question of proving that if `B` is reduced (resp. geometrically unibranch, resp.
integral and geometrically unibranch) then `B' = B ⊗_A A'` is reduced (resp. `Spec(B')` is geometrically unibranch at
the points of `p⁻¹(x)`, resp. `Spec(B')` is integral and geometrically unibranch at these points). Suppose first only
`B` reduced; `B` is the union of the increasing family of its sub-`A`-algebras of finite type `B_λ`, and by flatness,
`B'` is the union of the increasing filtered family of its sub-`A'`-algebras `B'_λ = B_λ ⊗_A A'`. Now, the morphism
`Spec(B'_λ) → Spec(B_λ)` is normal (6.8.2), and *a fortiori* reduced; the fact that `B'_λ` is reduced is therefore a
consequence of (3.3.5); one concludes that `B'` itself is reduced by (5.13.2).

Suppose now `B` geometrically unibranch; in view of (I, 5.1.8), one may moreover suppose `B` reduced, hence integral.
Let `C` be its integral closure, which is by hypothesis a local ring; set `Z = Spec(C)`, `C' = C ⊗_A A'`,
`Z' = Spec(C') = Z ×_X X'`, so that one has the commutative diagram

```text
              Z  ⟵ Z'
              ↓     ↓
              X  ⟵ X'
                 p
```

By virtue of the first part of the reasoning, `X'` is reduced; on the other hand, as `Z' = Z ×_Y Y'`, it follows from
(6.14.1) that `Z'` is normal (and *a fortiori* geometrically unibranch). As `f` is integral and birational, the same
holds for `f'` by (6.15.4.1), since `p` is flat. Finally, the hypothesis that `X` is geometrically unibranch at the
point `x` entails that `f` is radicial at this point (6.15.5); one concludes therefore from (6.15.3.1) that `f'` is
radicial at every point `x' ∈ p⁻¹(x)`, and it follows then from (6.15.5) that `X'` is geometrically unibranch (hence
integral since it is reduced) at each of these points.

**Remarks (6.15.11).**

<!-- label: IV.6.15.11 -->

*(i) In the proof of (6.15.10), one cannot dispense with appealing to (6.14.1), even when `X = Y`, for one brings into
play the integral closure of the ring `B`, which is not necessarily a Noetherian ring even if `B` is so.*

*(ii) The example (6.5.5, (ii)) shows that in (6.15.10), one cannot replace "geometrically unibranch" by "integral" in
the statement, even if the residue field `k(x)` is algebraically closed and the morphism `g` étale.*

<!-- original page 182 -->

One cannot either in this statement replace "geometrically unibranch" by "unibranch". Let `A` be the complete integral
local ring `ℝ[[U, V]]/(U² + V²)`; if `u`, `v` are the images of `U`, `V` in `A`, the maximal ideal of `A` is `Au + Av`.
One verifies easily that the integral closure of `A` is the ring `A[t]`, where `t = u/v` satisfies the relation
`t² = −1`, so that `A[t]` is isomorphic to the local ring `ℂ[[U]]`; as the residue field of `ℂ[[U]]` is `ℂ`, one sees
that `A` is unibranch but not geometrically unibranch. But `A ⊗_ℝ ℂ` is not an integral ring, being isomorphic to
`ℂ[[U, V]]/(U − iV)(U + iV)`.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/18-c4-s06-morphismes-plats-preschemas.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-2.pdf, pp. 163-182 -->

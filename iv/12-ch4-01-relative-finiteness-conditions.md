<!-- original page 224 -->

## §1. Relative finiteness conditions. Constructible sets in preschemes

In this section we resume, in completed form, the exposition of the "finiteness conditions" for a morphism of preschemes
`f : X → Y` given in `(I, 6.3 and 6.6)`. There are essentially two notions of "finiteness" of *global* nature on `X`,
that of *quasi-compact* morphism (defined in `(I, 6.6.1)`) and that of *quasi-separated* morphism; there are on the
other hand two notions of "finiteness" of *local* nature on `X`, that of morphism *locally of finite type* (defined in
`(I, 6.6.2)`) and that of morphism *locally of finite presentation*. Combining these local notions with the preceding
global notions, one obtains the notions of morphism *of finite type* (defined in `(I, 6.3.1)`) and of morphism *of
finite presentation*. For the reader's convenience we shall give again, in this section, the principal properties stated
in `(I, 6.3 and 6.6)`, of course referring back to those numbers of Chapter I for their proofs.

In nos. (1.8) and (1.9) we complete, in the framework of preschemes and making use of the preceding finiteness notions,
the results on constructible sets given in `(0_III, §9)`.

### 1.1. Quasi-compact morphisms

**Definition (1.1.1).**

<!-- label: IV.1.1.1 -->

*We say that a morphism of preschemes `f : X → Y` is **quasi-compact** if the continuous map `f` from the topological
space `X` to the topological space `Y` is quasi-compact `(0_I, 9.1.1)`, in other words if the inverse image `f⁻¹(U)` of
every quasi-compact open set `U` of `Y` is quasi-compact (cf. `(I, 6.6.1)`).*

If `𝔅` is a base of the topology of `Y` formed of affine open sets, then for `f` to be quasi-compact it is necessary and
sufficient that for every `V ∈ 𝔅`, `f⁻¹(V)` be a finite union of affine open sets. For example, if `Y` is affine and `X`
is quasi-compact, every morphism `f : X → Y` is quasi-compact `(I, 6.6.1)`.

If `f : X → Y` is a quasi-compact morphism, it is clear that for every open set `V` of `Y` the restriction of `f` to
`f⁻¹(V)` is a quasi-compact morphism `f⁻¹(V) → V`. Conversely, if `(U_α)` is an open cover of `Y` and `f : X → Y` is a
morphism such that the restrictions `f⁻¹(U_α) → U_α` are quasi-compact, then `f` is quasi-compact. Consequently, if
`f : X → Y` is an `S`-morphism of `S`-preschemes and there exists an open cover `(S_λ)` of `S` such that the
restrictions `g⁻¹(S_λ) → h⁻¹(S_λ)` of `f` (where `g` and `h` are the structure morphisms) are quasi-compact, then `f` is
quasi-compact.

**Proposition (1.1.2).**

<!-- label: IV.1.1.2 -->

*(i) An immersion `X → Y` is quasi-compact if it is closed, or if the space underlying `Y` is locally Noetherian, or if
the space underlying `X` is Noetherian.*

*(ii) The composite of two quasi-compact morphisms is quasi-compact.*

*(iii) If `f : X → Y` is a quasi-compact `S`-morphism, then so is `f_{(S')} : X_{(S')} → Y_{(S')}` for every extension
`g : S' → S` of the base prescheme.*

*(iv) If `f : X → X'` and `g : Y → Y'` are two quasi-compact `S`-morphisms,*

```text
  f ×_S g : X ×_S Y → X' ×_S Y'
```

*is quasi-compact.*

*(v) If the composite `g ∘ f` of two morphisms `f : X → Y`, `g : Y → Z` is quasi-compact, and if `g` is separated, or
the space underlying `X` locally Noetherian, then `f` is quasi-compact.*

*(vi) For a morphism `f` to be quasi-compact, it is necessary and sufficient that `f_red` be so.*

For the proof, see `(I, 6.6.4)`. We note that assertion (vi) is also a consequence of the more general proposition:

**Proposition (1.1.3).**

<!-- label: IV.1.1.3 -->

*Let `f : X → Y`, `g : Y → Z` be two morphisms. If `g ∘ f` is quasi-compact and `f` is surjective, then `g` is
quasi-compact.*

Indeed, if `V` is a quasi-compact open set in `Z`, `f⁻¹(g⁻¹(V))` is quasi-compact by hypothesis, and one has
`g⁻¹(V) = f(f⁻¹(g⁻¹(V)))`, since `f` is surjective; hence `g⁻¹(V)` is quasi-compact.

<!-- original page 225 -->

**Corollary (1.1.4).**

<!-- label: IV.1.1.4 -->

*Let `f : X → Y`, `g : Y' → Y` be two morphisms, `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`; suppose `g` is
quasi-compact and surjective (resp. surjective). Then, for `f` to be quasi-compact (resp. dominant), it suffices that
`f'` be so.*

If `g' : X' → X` is the canonical projection, `g'` is a surjective morphism `(I, 3.5.2)`, and one has `f ∘ g' = g ∘ f'`;
if `f'` is quasi-compact (resp. dominant), so is `g ∘ f'`, since `g` is quasi-compact `(1.1.2)` (resp. surjective);
since `f ∘ g'` is quasi-compact (resp. dominant) and `g'` is surjective, one deduces from `(1.1.3)` that `f` is
quasi-compact (resp. dominant).

To abbreviate, we shall call a **maximal point** of a prescheme `X` any generic point of an irreducible component of
`X`; if `X = Spec(A)` is affine, the maximal points of `X` are the *minimal* prime ideals of `A`.

**Proposition (1.1.5).**

<!-- label: IV.1.1.5 -->

*Let `f : X → Y` be a quasi-compact morphism. The following conditions are equivalent:*

*a) `f` is dominant;*

*b) for every maximal point `y` of `Y`, one has `f⁻¹(y) ≠ ∅`;*

*c) for every maximal point `y` of `Y`, `f⁻¹(y)` contains a maximal point of `X`.*

The equivalence of a) and c) was proved in `(I, 6.6.5)`. It is clear that c) implies b); on the other hand, if `X'` is
an irreducible component of `X` meeting `f⁻¹(y)`, then `f(X')` is irreducible and contains `y`, so it is contained in
the irreducible component `Y' = ‾{y}` of `Y` `(0_I, 2.1.6)`; if `x` is the generic point of `X'`, one therefore has
necessarily `f(x) = y` `(0_I, 2.1.5)`; hence b) implies c).

<!-- original page 226 -->

**Proposition (1.1.6).**

<!-- label: IV.1.1.6 -->

*Let `f' : X' → Y`, `f'' : X'' → Y` be two morphisms, `X` the sum prescheme `X' ⨿ X''`, `f : X → Y` the morphism equal
to `f'` on `X'` and to `f''` on `X''`. For `f` to be quasi-compact it is necessary and sufficient that `f'` and `f''` be
so.*

This results immediately from the definition.

### 1.2. Quasi-separated morphisms

**Definition (1.2.1).**

<!-- label: IV.1.2.1 -->

*Let `X`, `Y` be two preschemes. We say that a morphism `f : X → Y` is **quasi-separated** (or that `X` is
**quasi-separated over `Y`**) if the diagonal morphism `Δ_f = (1_X, 1_X)_Y : X → X ×_Y X` is quasi-compact. We say that
a prescheme `X` is **quasi-separated** if it is quasi-separated over `Spec(ℤ)`.*

By definition, every separated morphism is quasi-separated, `Δ_f` being a closed immersion `(1.1.2, (i))`; a scheme `X`
is a quasi-separated prescheme, being separated over `Spec(ℤ)` `(I, 5.4.1)`.

**Proposition (1.2.2).**

<!-- label: IV.1.2.2 -->

*(i) Every monomorphism of preschemes `f : X → Y` (in particular, every immersion) is quasi-separated.*

*(ii) If `f : X → Y` and `g : Y → Z` are two quasi-separated morphisms, then `g ∘ f : X → Z` is quasi-separated.*

*(iii) Let `X`, `Y` be two `S`-preschemes, `f : X → Y` a quasi-separated `S`-morphism. Then, for every base change
`g : S' → S`, the morphism `f_{(S')} : X_{(S')} → Y_{(S')}` is quasi-separated.*

*(iv) If `f : X → Y`, `f' : X' → Y'` are two quasi-separated `S`-morphisms, then*

```text
  f ×_S f' : X ×_S X' → Y ×_S Y'
```

*is quasi-separated.*

*(v) If `f : X → Y`, `g : Y → Z` are two morphisms such that `g ∘ f` is quasi-separated, then `f` is quasi-separated.*

*(vi) If `f : X → Y` is a quasi-separated morphism, then `f_red : X_red → Y_red` is quasi-separated.*

By virtue of `(I, 5.5.12)`, it suffices to prove (i), (ii), and (iii).

Assertion (i) is trivial, every monomorphism being separated `(I, 5.5.1)`. To prove (iii), one reduces immediately to
the case where `Y = S` `(I, 3.3.11)`, and the assertion results from the fact that `Δ_{f'} = (Δ_f)_{(S')}` `(I, 5.3.4)`
and from `(1.1.2, (iii))`. To prove (ii), consider the projections `p` and `q` from `X ×_Y X` onto `X`; if
`i = (p, q)_Z`, one knows that the diagram

```text
  X ×_Y X  ──i──→  X ×_Z X
    │                │
    π│              │f ×_Z f
    ↓                ↓
    Y    ──Δ_g──→  Y ×_Z Y
```

(where `π` is the structure morphism) is commutative and identifies `X ×_Y X` with the product of the
`(Y ×_Z Y)`-preschemes `Y` and `X ×_Z X` `(I, 5.3.5)`. If `g` is quasi-separated, `Δ_g` is quasi-compact,

<!-- original page 227 -->

so the same is true of `i` `(1.1.2, (iii))`; if in addition `f` is quasi-separated, `Δ_f` is quasi-compact, hence so is
`i ∘ Δ_f` `(1.1.2, (ii))`, which is equal to `Δ_{g ∘ f}`.

**Corollary (1.2.3).**

<!-- label: IV.1.2.3 -->

*(i) Let `X` be a quasi-separated prescheme. Then every morphism `f : X → Y` is quasi-separated.*

*(ii) Let `Y` be a quasi-separated prescheme. For a morphism `f : X → Y` to be quasi-separated, it is necessary and
sufficient that the prescheme `X` be quasi-separated.*

This results at once from `(1.2.2, (ii) and (v))` applied to `X`, `Y`, and `Spec(ℤ)`.

**Proposition (1.2.4).**

<!-- label: IV.1.2.4 -->

*Let `f : X → Y` be a morphism, `g : Y → Z` a quasi-separated morphism. If `g ∘ f` is quasi-compact, then so is `f`.*

One knows that `f` is the composite morphism `X ─Γ_f→ X ×_Z Y ─pr_2→ Y` `(I, 5.3.13)`; on the other hand, `pr_2`
identifies with `(g ∘ f) ×_Z 1_Y` `(I, 3.3.4)`, and if `g ∘ f` is quasi-compact, then so is `pr_2` `(1.1.2, (iv))`.
Finally, one has the commutative diagram

```text
  X        ──Γ_f──→  X ×_Z Y                                    (1.2.4.1)
  │                    │
  f│                  │f × 1_Y
  ↓                    ↓
  Y        ──Δ_g──→  Y ×_Z Y
```

which identifies `X` with the product of the `(Y ×_Z Y)`-preschemes `Y` and `X ×_Z Y` `(I, 5.3.7)`. Since by hypothesis
`Δ_g` is a quasi-compact morphism, so is `Γ_f` `(1.1.2, (iii))`; the conclusion therefore follows from `(1.1.2, (ii))`.

**Proposition (1.2.5).**

<!-- label: IV.1.2.5 -->

*Let `f : X → Y`, `g : Y' → Y` be two morphisms, `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`. If `g` is quasi-compact and
surjective and `f'` is quasi-separated, then `f` is quasi-separated.*

Indeed, one has `(X' ×_{Y'} X') = (X ×_Y X)_{(Y')}` and `Δ_{f'} = (Δ_f)_{(Y')}` `(I, 5.3.4)`; as the projection
`X' ×_{Y'} X' → X ×_Y X` is quasi-compact `(1.1.2, (iii))` and surjective `(I, 3.5.2)`, one may, by virtue of
`(I, 3.3.11)`, apply `(1.1.4)`, which shows that since `Δ_{f'}` is a quasi-compact morphism, so is `Δ_f`.

**Proposition (1.2.6).**

<!-- label: IV.1.2.6 -->

*Let `f : X → Y` be a morphism, `(U_α)` a cover of `Y` by open sets such that the induced preschemes `U_α` are
quasi-separated. For `f` to be quasi-separated it is necessary and sufficient that each of the preschemes induced by `X`
on the open sets `f⁻¹(U_α)` be quasi-separated.*

The inverse image in `X ×_Y X` of `U_α` is `X_α ×_{U_α} X_α`, where `X_α = f⁻¹(U_α)`, and the restriction
`X_α → X_α ×_{U_α} X_α` of `Δ_f` is none other than `Δ_{f_α}`, denoting by `f_α` the restriction `X_α → U_α` of `f`. By
virtue of definition `(1.2.1)` and of the local character of the notion of quasi-compact morphism `(1.1.1)`, for `f` to
be quasi-separated it is necessary and sufficient that each of the morphisms `f_α` be so. But since by hypothesis the
morphism `U_α → Spec(ℤ)` is quasi-separated, to say that `f_α` is quasi-separated is the same as to say that the
composite `X_α ─f_α→ U_α → Spec(ℤ)` is so `(1.2.2, (ii) and (v))`, whence the proposition.

<!-- original page 228 -->

To check that a morphism is quasi-separated, one is therefore reduced to giving criteria for a prescheme to be
quasi-separated:

**Proposition (1.2.7).**

<!-- label: IV.1.2.7 -->

*Let `X` be a prescheme, `(U_α)` a cover of `X` formed of quasi-compact open sets. The following properties are
equivalent:*

*a) `X` is quasi-separated.*

*b) For every quasi-compact open set `U` of `X`, the canonical immersion `U → X` is quasi-compact (in other words, `U`
is **retrocompact** in `X`).*

*b') The intersection of two quasi-compact open sets of `X` is quasi-compact.*

*c) For every pair of indices `(α, β)`, the intersection `U_α ∩ U_β` is quasi-compact.*

Properties b) and b') are trivially equivalent by definition of a quasi-compact morphism. Since a quasi-compact open set
is a finite union of affine open sets, for two quasi-compact open sets `U`, `V` of `X`, `U ×_ℤ V` is a quasi-compact
open set of `X ×_ℤ X` `(I, 3.2.7)`, whose inverse image under `Δ_X` is `U ∩ V`; hence a) implies b'). It is trivial that
b') implies c); finally, if c) holds, the `U_α ×_ℤ U_β` form a cover of `X ×_ℤ X` by quasi-compact open sets, and one
knows that for the morphism `Δ_X : X → X ×_ℤ X` to be quasi-compact it suffices that the inverse images `U_α ∩ U_β` of
the `U_α ×_ℤ U_β` under `Δ_X` be quasi-compact `(1.1.1)`; hence c) implies a).

**Corollary (1.2.8).**

<!-- label: IV.1.2.8 -->

*Every prescheme `X` whose underlying space is locally Noetherian (for example, a locally Noetherian prescheme) is
quasi-separated; every morphism `f : X → Y` is then quasi-separated.*

**Proposition (1.2.9).**

<!-- label: IV.1.2.9 -->

*Let `X'`, `X''` be two preschemes, `X = X' ⨿ X''` their sum, `f' : X' → Y`, `f'' : X'' → Y` two morphisms, `f : X → Y`
the morphism that coincides with `f'` on `X'` and with `f''` on `X''`. For `f` to be quasi-separated it is necessary and
sufficient that `f'` and `f''` be so.*

Indeed, `X ×_Y X` is the sum of the four preschemes `X' ×_Y X'`, `X' ×_Y X''`, `X'' ×_Y X'`, and `X'' ×_Y X''`, and
`Δ_f` is the morphism that coincides with `Δ_{f'}` on `X'` and with `Δ_{f''}` on `X''`; the proposition therefore
results at once from the definitions.

### 1.3. Morphisms locally of finite type

**(1.3.1)**

<!-- label: IV.1.3.1 -->

Recall that if `A` is a ring, an (commutative) `A`-algebra `B` is said to be **of finite type** if it is generated by a
finite number of elements of `B`, or — what amounts to the same — if it is isomorphic to a quotient of a polynomial
algebra `A[T_1, …, T_n]` by an ideal of that algebra. It is clear that for every (commutative) `A`-algebra `A'`,
`B ⊗_A A'` is then an `A'`-algebra of finite type. If `B` is an `A`-algebra of finite type and `C` a `B`-algebra of
finite type, then `C` is an `A`-algebra of finite type; for if `C` is a quotient of `B[T_1, …, T_n]` and `B` a quotient
of `A[S_1, …, S_m]`, then `B[T_1, …, T_n] = B ⊗_A A[T_1, …, T_n]` is a quotient of `A[S_1, …, S_m, T_1, …, T_n]`, hence
so is `C`.

**Definition (1.3.2).**

<!-- label: IV.1.3.2 -->

*Let `f : X → Y` be a morphism of preschemes, `x` a point of `X`, `y = f(x)`. We say that `f` is **of finite type at
`x`** if there exist an affine open neighbourhood `V` of `y` and an affine open neighbourhood `U` of `x` such that
`f(U) ⊂ V` and the ring `A(U)` is an `A(V)`-algebra of finite type. We say that `f` is **locally of finite type** if it
is of finite type at every point of `X`.*

<!-- original page 229 -->

**Proposition (1.3.3).**

<!-- label: IV.1.3.3 -->

*If `Y` is a locally Noetherian prescheme and `f : X → Y` a morphism locally of finite type, then `X` is locally
Noetherian.*

For the proof, see `(I, 6.3.7)`.

**Proposition (1.3.4).**

<!-- label: IV.1.3.4 -->

*(i) Every local immersion is locally of finite type.*

*(ii) If two morphisms `f : X → Y`, `g : Y → Z` are locally of finite type, then so is `g ∘ f`.*

*(iii) If `f : X → Y` is an `S`-morphism locally of finite type, then `f_{(S')} : X_{(S')} → Y_{(S')}` is locally of
finite type for every extension `S' → S` of the base prescheme.*

*(iv) If `f : X → X'` and `g : Y → Y'` are two `S`-morphisms locally of finite type, then `f ×_S g` is locally of finite
type.*

*(v) If the composite `g ∘ f` of two morphisms is locally of finite type, then `f` is locally of finite type.*

*(vi) If a morphism `f` is locally of finite type, then so is `f_red`.*

For the proof, see `(I, 6.6.6)`.

**Corollary (1.3.5).**

<!-- label: IV.1.3.5 -->

*Let `f : X → Y` be a morphism locally of finite type. For every morphism `Y' → Y` such that `Y'` is locally Noetherian,
`X ×_Y Y'` is locally Noetherian.*

Indeed, `f_{(Y')} : X ×_Y Y' → Y'` is locally of finite type by `(1.3.4, (iii))`, and it suffices to apply `(1.3.3)`.

**Proposition (1.3.6).**

<!-- label: IV.1.3.6 -->

*Let `φ : A → B` be a ring homomorphism. For the corresponding morphism `f : Spec(B) → Spec(A)` to be locally of finite
type, it is necessary and sufficient that `B` be an `A`-algebra of finite type.*

For the proof, see `(I, 6.3.3)`, taking into account that `f` is quasi-compact and that `(I, 6.6.3)` holds.

**Proposition (1.3.7).**

<!-- label: IV.1.3.7 -->

*For a morphism `f : X → Y` locally of finite type to be surjective, it is necessary and sufficient that for every
algebraically closed field `Ω` the map `X(Ω) → Y(Ω)` corresponding to `f` `(I, 3.4.1)` be surjective.*

For the proof, see `(I, 6.3.10)`.

**(1.3.8)**

<!-- label: IV.1.3.8 -->

Let `A` be a ring. We say that an `A`-algebra `B` is **essentially of finite type** if `B` is `A`-isomorphic to an
`A`-algebra of the form `S⁻¹C`, where `C` is an `A`-algebra of finite type and `S` a multiplicative subset of `C`.

**Proposition (1.3.9).**

<!-- label: IV.1.3.9 -->

*(i) If `B` is an `A`-algebra essentially of finite type and `C` a `B`-algebra essentially of finite type, then `C` is
an `A`-algebra essentially of finite type.*

*(ii) Let `B` be an `A`-algebra essentially of finite type, `A'` an `A`-algebra; then `B' = B ⊗_A A'` is an `A'`-algebra
essentially of finite type.*

(i) Let `B = S'⁻¹B'` and `C = T'⁻¹C'`, where `B'` (resp. `C'`) is an `A`-algebra (resp. a `B`-algebra) of finite type
and `S'` (resp. `T'`) a multiplicative subset of `B'` (resp. `C'`); then `C'` is of the form `S'⁻¹C''`, where `C''` is a
`B'`-algebra of finite type, so `C` is also a ring of fractions of `C''`; since `C''` is an `A`-algebra of finite type,
this proves our assertion.

(ii) If `B` is a ring of fractions of an `A`-algebra of finite type `C`, then `B'` is a ring of fractions of the
`A'`-algebra of finite type `C ⊗_A A'`, whence (ii).

<!-- original page 230 -->

**(1.3.10)**

<!-- label: IV.1.3.10 -->

If `B` is a *local* `A`-algebra essentially of finite type, then `B` is of the form `C_𝔮`, where `C` is an `A`-algebra
of finite type and `𝔮` a prime ideal of `C` `(Bourbaki, Alg. comm., chap. II, §5, prop. 11)`. Let `𝔭` be the inverse
image in `A` of the ideal `𝔮`; setting `S = A − 𝔭`, `C_𝔮` is also a local ring at a prime ideal of `S⁻¹C`; since `S⁻¹C`
is an algebra of finite type over `A_𝔭 = S⁻¹A`, one sees that `B` is also an `A_𝔭`-algebra essentially of finite type,
and in addition the homomorphism `A_𝔭 → B` is local.

**Proposition (1.3.11).**

<!-- label: IV.1.3.11 -->

*If `B` is a local `A`-algebra essentially of finite type, then `B` is `A`-isomorphic to a quotient `A`-algebra of an
`A`-algebra of the form `C_𝔮`, where `C` is a polynomial algebra `A[T_1, …, T_n]` and `𝔮` a prime ideal of `C`.*

Indeed, by definition, `B` is isomorphic to `C'_{𝔮'}`, where `C'` is an `A`-algebra of finite type and `𝔮'` a prime
ideal of `C'`; but `C' = C/𝔟`, where `C = A[T_1, …, T_n]` and `𝔟` is an ideal of `C`; so `𝔮' = 𝔮/𝔟`, where `𝔮` is a
prime ideal of `C`, and `C'_{𝔮'}` is isomorphic to `C_𝔮 / 𝔟 C_𝔮`.

### 1.4. Morphisms locally of finite presentation

**(1.4.1)**

<!-- label: IV.1.4.1 -->

Given a ring `A`, we shall say that an (commutative) `A`-algebra `B` is **of finite presentation** if it is isomorphic
to the quotient `A[T_1, …, T_n] / 𝔞` of a polynomial algebra over `A` by an *ideal of finite type* `𝔞` of
`A[T_1, …, T_n]`. For every (commutative) `A`-algebra `A'`, `B ⊗_A A'` is then an `A'`-algebra of finite presentation,
being isomorphic to the quotient of `A'[T_1, …, T_n]` by the canonical image in this ring of `𝔞 ⊗_A A'`, which is
manifestly an `A'[T_1, …, T_n]`-module of finite type. If `B` is an `A`-algebra of finite presentation and `C` a
`B`-algebra of finite presentation, then `C` is an `A`-algebra of finite presentation. Indeed, let
`B = A[S_1, …, S_m] / 𝔞` and `C = B[T_1, …, T_n] / 𝔟`, where `𝔞` (resp. `𝔟`) is an ideal of finite type of
`A[S_1, …, S_m]` (resp. of `B[T_1, …, T_n]`); the ring `B[T_1, …, T_n]` is isomorphic to
`A[S_1, …, S_m, T_1, …, T_n] / 𝔞'`, where `𝔞'` is the canonical image of `𝔞 ⊗_A A[T_1, …, T_n]`, and is therefore an
ideal of finite type of `A[S_1, …, S_m, T_1, …, T_n]`; the ideal `𝔟` of `B[T_1, …, T_n]` is of the form `𝔟'/𝔞'`, where
`𝔟'` is an ideal of `A[S_1, …, S_m, T_1, …, T_n]`; since `𝔞'` and `𝔟'/𝔞'` are modules of finite type over
`A[S_1, …, S_m, T_1, …, T_n]`, so is `𝔟'`, and `C`, isomorphic to `A[S_1, …, S_m, T_1, …, T_n] / 𝔟'`, is therefore an
`A`-algebra of finite presentation. Note finally that if `A` is Noetherian, then so is `A[T_1, …, T_n]`, so every
`A`-algebra of finite type is then of finite presentation.

**Definition (1.4.2).**

<!-- label: IV.1.4.2 -->

*Let `f : X → Y` be a morphism of preschemes, `x` a point of `X`, `y = f(x)`. We say that `f` is **of finite
presentation at `x`** if there exist an affine open neighbourhood `V` of `y` and an affine open neighbourhood `U` of `x`
such that `f(U) ⊂ V` and the ring `A(U)` is an `A(V)`-algebra of finite presentation. We say that `f` is **locally of
finite presentation** if it is of finite presentation at every point of `X`.*

If `Y` is locally Noetherian, to say that `f` is locally of finite type and to say that `f` is locally of finite
presentation are equivalent.

**Proposition (1.4.3).**

<!-- label: IV.1.4.3 -->

*(i) Every local isomorphism is locally of finite presentation.*

*(ii) If two morphisms `f : X → Y`, `g : Y → Z` are locally of finite presentation, then so is `g ∘ f`.*

<!-- original page 231 -->

*(iii) If `f : X → Y` is an `S`-morphism locally of finite presentation, then `f_{(S')} : X_{(S')} → Y_{(S')}` is
locally of finite presentation for every extension `S' → S` of the base prescheme.*

*(iv) If `f : X → X'` and `g : Y → Y'` are two `S`-morphisms locally of finite presentation, then `f ×_S g` is locally
of finite presentation.*

*(v) If the composite `g ∘ f` of two morphisms is locally of finite presentation and if `g` is locally of finite type,
then `f` is locally of finite presentation.*

Assertion (i) is trivial. To prove (iii) one may restrict to the case where `S = Y` `(I, 3.3.11)`; let `x'` be a point
of `X_{(S')}`, and `s'`, `x` its projections onto `S'` and `X` respectively, `s` the common projection of `s'` and `x`
onto `S`. By hypothesis there is an affine open neighbourhood `V` (resp. `U`) of `s` (resp. `x`) such that the image of
`U` is contained in `V` and `A(U)` is an `A(V)`-algebra of finite presentation; let `V'` be an affine open neighbourhood
of `s'` whose image in `S` is contained in `V`; then `U ×_V V'` is an affine open neighbourhood of `x'` whose image in
`S'` is contained in `V'`, and whose ring `A(U) ⊗_{A(V)} A(V')` is an `A(V')`-algebra of finite presentation `(1.4.1)`.

To prove (ii), consider a point `x ∈ X`, and let `y = f(x)`, `z = g(f(x))`. By hypothesis there is an affine open
neighbourhood `W = Spec(C)` (resp. `V = Spec(B)`) of `z` (resp. `y`) such that `g(V) ⊂ W` and `B` is a `C`-algebra of
finite presentation. On the other hand, there is an affine open neighbourhood `V' = Spec(B')` (resp. `U = Spec(A)`) of
`y` (resp. `x`) such that `f(U) ⊂ V'` and `A` is a `B'`-algebra of finite presentation. Let `s ∈ B` be such that the
open set `D(s) = Spec(B_s)` in `V` is a neighbourhood of `y` contained in `V'`, and let `U' = f⁻¹(D(s)) ⊂ U`; one has
`U' = Spec(A ⊗_{B'} B_s)`, and `A ⊗_{B'} B_s` is a `B_s`-algebra of finite presentation `(1.4.1)`; on the other hand,
`B_s = B[T] / (1 − sT)` is a `B`-algebra of finite presentation by definition; consequently `(1.4.1)`, `A ⊗_{B'} B_s` is
a `C`-algebra of finite presentation, which proves (ii).

One knows that (iv) results from (i), (ii), and (iii) `(I, 3.5.1)`. To prove (v), consider the commutative diagram

```text
  X        ──Γ_f──→  X ×_Z Y
  │                    │
  f│                  │f × 1
  ↓                    ↓
  Y        ──Δ_g──→  Y ×_Z Y
```

which identifies `X` with the product of the `(Y ×_Z Y)`-preschemes `Y` and `X ×_Z Y` `(I, 5.3.7)`, `Δ_g` being the
diagonal morphism. If we know that `Δ_g` is locally of finite presentation, it will follow from (iii) that the same is
true of `Γ_f`. On the other hand, one has the factorization of `f` as `X ─Γ_f→ X ×_Z Y ─p_2→ Y` `(I, 5.3.13)`, where the
projection `p_2` is equal to `(g ∘ f) ×_Z 1_Y`; since `g ∘ f` is supposed locally of finite presentation, so is `p_2` by
(iv), and it will finally result from (ii) that `f` too is locally of finite presentation. One sees therefore that one
is reduced to proving:

**Corollary (1.4.3.1).**

<!-- label: IV.1.4.3.1 -->

*Let `g : Y → Z` be a morphism locally of finite type; then the diagonal morphism `Δ_g : Y → Y ×_Z Y` is locally of
finite presentation.*

<!-- original page 232 -->

One may restrict to the case where `Z = Spec(A)`, `Y = Spec(B)`, `B` being an `A`-algebra of finite type; the morphism
`Δ_g` then corresponds to the *augmentation homomorphism* `δ : B ⊗_A B → B` such that `δ(x ⊗ y) = xy`. In view of
definition `(1.4.2)`, it suffices to show that the kernel `𝔍` of `δ` is an ideal of finite type, which results from
`(0_IV, 20.4.4)`.

**Proposition (1.4.4).**

<!-- label: IV.1.4.4 -->

*Let `A` be a ring, `B` an `A`-algebra, `B'` a polynomial algebra `A[T_1, …, T_n]`, `u : B' → B` a surjective
homomorphism of `A`-algebras. For `B` to be an `A`-algebra of finite presentation it is necessary and sufficient that
the kernel `𝔍` of `u` be an ideal of finite type of `B'`.*

The condition is sufficient by definition `(1.4.1)`. To see that it is necessary, remark that the morphism
`g : Spec(B') → Spec(A)` is locally of finite type; if `B` is an `A`-algebra of finite presentation, the morphism
`f : Spec(B) → Spec(B')` corresponding to `u` is such that `g ∘ f : Spec(B) → Spec(A)` is locally of finite
presentation, so it results from `(1.4.3, (v))` that `f` is also locally of finite presentation. Now, to show that the
ideal `𝔍` is of finite type, it suffices to prove that `𝔍̃` is a `B̃'`-Module of finite type `(II, 6.1.4.1)`. Returning
to definition `(1.4.2)`, one is finally reduced to proving:

**Lemma (1.4.4.1).**

<!-- label: IV.1.4.4.1 -->

*Let `𝔞` be an ideal of a ring `C`, `s` an element of `C`, such that `C_s / 𝔞_s` is a `C`-algebra of finite
presentation; then `𝔞_s` is an ideal of finite type in the ring `C_s`.*

By hypothesis, there exist a polynomial `C`-algebra `C' = C[T_1, …, T_n]` and a surjective `C`-homomorphism
`v : C' → C_s / 𝔞_s` whose kernel `𝔟` is of finite type. Let `p : C_s → C_s / 𝔞_s` be the canonical homomorphism; for
each `i` there is a `t_i ∈ C` such that `p(t_i / s^k) = v(T_i)` (one may suppose the exponent `k` is the same for all
indices `i`). Consider then the `C_s`-algebra `D = C_s[T_1, …, T_n]`, and the homomorphism of `C_s`-algebras
`w : D → C_s` such that `w(T_i) = t_i / s^k`; `w` is manifestly surjective, and consequently so is
`v' = p ∘ w : D → C_s / 𝔞_s`. On the other hand, every polynomial in `D` may be written `P / s^m`, where
`P ∈ C' = C[T_1, …, T_n]`, and one has `v'(P / s^m) = (1 / s^m) v(P)`; since `1 / s` is invertible in `C_s`, the
relation `v'(P / s^m) = 0` in `C_s / 𝔞_s` is equivalent to `v(P) = 0`, and consequently the kernel `𝔟'` of `v'` is
generated by the canonical image of `𝔟` in `D`, and *a fortiori* is of finite type in the ring `D`. But
`𝔟' = v'⁻¹(0) = w⁻¹(p⁻¹(0)) = w⁻¹(𝔞_s)`, and since `w` is surjective, `𝔞_s = w(𝔟')`, which proves that `𝔞_s` is an ideal
of finite type of `C_s`.

**Corollary (1.4.5).**

<!-- label: IV.1.4.5 -->

*Let `X`, `Y` be two preschemes, `j : X → Y` an immersion, `U` an open set of `Y` such that `j(X)` is closed in `U`, `𝒥`
the quasi-coherent Ideal of `𝒪_U` defining the closed subprescheme of `U` associated with `j`. For `j` to be locally of
finite presentation it is necessary and sufficient that `𝒥` be an `𝒪_U`-Module of finite type.*

**Proposition (1.4.6).**

<!-- label: IV.1.4.6 -->

*Let `φ : A → B` be a ring homomorphism. For the corresponding morphism `f : Spec(B) → Spec(A)` to be locally of finite
presentation, it is necessary and sufficient that `B` be an `A`-algebra of finite presentation.*

The condition being trivially sufficient, it remains to prove that it is necessary. If `f` is locally of finite
presentation, it already follows from `(1.3.6)` that `B` is an `A`-algebra of finite type, so there exists a surjective
homomorphism `u : B' = A[T_1, …, T_n] → B` of `A`-algebras; it results from `(1.4.3, (v))` that the immersion
`j : Spec(B) → Spec(B')` is locally

<!-- original page 233 -->

of finite presentation; therefore `(1.4.5)`, if `𝔍` is the kernel of `u`, the `B̃'`-Module `𝔍̃` is of finite type, and
consequently `(II, 6.1.4.1)` `𝔍` is an ideal of finite type.

**Proposition (1.4.7).**

<!-- label: IV.1.4.7 -->

*Let `ρ : A → B` be a ring homomorphism making `B` into a finite `A`-algebra. For `B` to be an `A`-algebra of finite
presentation it is necessary and sufficient that `B` be an `A`-module of finite presentation.*

We will use:

**Lemma (1.4.7.1).**

<!-- label: IV.1.4.7.1 -->

*If `B` is a finite `A`-algebra, there exists a surjective `A`-homomorphism of algebras `u : B' → B`, where `B'` is a
finite `A`-algebra and of finite presentation which is a free `A`-module.*

Indeed, there is a finite system `(a_i)_{1 ≤ i ≤ m}` of generators of the `A`-algebra `B` such that each `a_i` satisfies
a relation `F_i(a_i) = 0`, where `F_i ∈ A[X]` is a unitary polynomial of degree `> 0`; the quotient `A`-algebra
`B'_i = A[X] / (F_i)` is therefore free of finite rank over `A`; let `c_i` be the class of `X` in `B'_i`. There exists
an `A`-homomorphism of algebras `u_i : B'_i → B` such that `u_i(c_i) = a_i`; it then suffices to take for `B'` the
tensor product `B'_1 ⊗_A B'_2 ⊗ ⋯ ⊗_A B'_m`, and to consider the homomorphism `u_1 ⊗ u_2 ⊗ ⋯ ⊗ u_m : B' → B`, which is
surjective by construction. Moreover, if `B'' = A[T_1, …, T_m]` and if `b'_i` denotes the canonical image of `c_i` in
`B'`, the `A`-homomorphism of algebras `v : B'' → B'` such that `v(T_i) = b'_i` (`1 ≤ i ≤ m`) is surjective, and its
kernel `𝔟'` is the ideal of `B''` generated by the `F_i(T_i)`, hence of finite type; this proves that `B'` is an
`A`-algebra of finite presentation.

This lemma being proved, keep the same notations and let `w = v ∘ u : B'' → B`. If `𝔟` (resp. `𝔞`) is the kernel of `w`
(resp. `u`), one has `𝔞 = v(𝔟)` since `v` is surjective. Now `(1.4.4)`, if `B` is an `A`-algebra of finite presentation,
`𝔟` is an ideal of finite type of `B''`, so `𝔞` is an ideal of finite type of `B'`, hence an `A`-module of finite type
since `B'` is a finite `A`-algebra; since `B'` is a free `A`-module, `B` is an `A`-module of finite presentation.
Conversely, if `B` is an `A`-module of finite presentation, `𝔞` is an `A`-module of finite type
`(Bourbaki, Alg. comm., chap. I, §2, n° 8, lemme 9)`, and *a fortiori* an ideal of finite type of `B'`; consequently,
`B` is by definition a `B'`-algebra of finite presentation, and since `B'` is an `A`-algebra of finite presentation, `B`
is an `A`-algebra of finite presentation.

### 1.5. Morphisms of finite type

**Proposition (1.5.1).**

<!-- label: IV.1.5.1 -->

*Let `f : X → Y` be a morphism, `(U_α)` a cover of `Y` formed of affine open sets. The following conditions are
equivalent:*

*a) `f` is locally of finite type and quasi-compact.*

*b) For every `α`, `f⁻¹(U_α)` is a finite union of affine open sets `V_{α i}` such that each ring `A(V_{α i})` is an
`A(U_α)`-algebra of finite type.*

*c) For every affine open set `U` of `Y`, `f⁻¹(U)` is a finite union of affine open sets `V_i` such that the rings
`A(V_i)` are `A(U)`-algebras of finite type.*

For the proof, see `(I, 6.3.2 and 6.6.3)`.

**Definition (1.5.2).**

<!-- label: IV.1.5.2 -->

*We say that a morphism `f` is **of finite type** if it satisfies the equivalent conditions of proposition `(1.5.1)`.*

<!-- original page 234 -->

**Proposition (1.5.3).**

<!-- label: IV.1.5.3 -->

*Let `f : X → Y` be a morphism of finite type; if `Y` is Noetherian, then so is `X`.*

For the proof, see `(I, 6.3.7)`.

**Proposition (1.5.4).**

<!-- label: IV.1.5.4 -->

*(i) Let `j : X → Y` be a morphism of immersion. If `j` is quasi-compact (which is the case if `j` is a closed
immersion, or if the space underlying `X` is Noetherian, or if the space underlying `Y` is locally Noetherian), then `j`
is of finite type.*

*(ii) The composite of two morphisms of finite type is of finite type.*

*(iii) If `f : X → Y` is an `S`-morphism of finite type, then `f_{(S')} : X_{(S')} → Y_{(S')}` is of finite type for
every extension `S' → S` of the base prescheme.*

*(iv) If `f : X → X'` and `g : Y → Y'` are two `S`-morphisms of finite type, then `f ×_S g` is of finite type.*

*(v) If the composite `g ∘ f` of two morphisms is of finite type, and if `g` is quasi-separated or `X` is Noetherian,
then `f` is of finite type.*

*(vi) If a morphism `f` is of finite type, then so is `f_red`.*

This results at once (except case (v) where `X` is Noetherian, proved in `(I, 6.3.6)`) from the definitions and from
`(1.1.2)`, `(1.2.4)`, and `(1.3.4)`.

**Corollary (1.5.5).**

<!-- label: IV.1.5.5 -->

*Let `f : X → Y` be a morphism of finite type. For every morphism `Y' → Y` such that `Y'` is Noetherian, `X ×_Y Y'` is
Noetherian.*

This results from `(1.5.4, (iii))` and from `(1.5.3)`.

**Corollary (1.5.6).**

<!-- label: IV.1.5.6 -->

*Let `X` be a prescheme of finite type over a locally Noetherian prescheme `S`. Then every `S`-morphism `f : X → Y` is
of finite type.*

For the proof, see `(I, 6.3.9)`.

**Proposition (1.5.7).**

<!-- label: IV.1.5.7 -->

*Let `φ : A → B` be a ring homomorphism. For the corresponding morphism `f : Spec(B) → Spec(A)` to be of finite type, it
is necessary and sufficient that `φ` make `B` into an `A`-algebra of finite type.*

For the proof, see `(I, 6.3.3)`.

### 1.6. Morphisms of finite presentation

**Definition (1.6.1).**

<!-- label: IV.1.6.1 -->

*Let `X`, `Y` be two preschemes. We say that a morphism `f : X → Y` is **of finite presentation** if it satisfies the
three following conditions:*

*(i) `f` is locally of finite presentation;*

*(ii) `f` is quasi-compact (which, when (i) is satisfied, is equivalent to saying that `f` is of finite type
`(1.5.2)`);*

*(iii) `f` is quasi-separated.*

*We say in this case that `X` is **of finite presentation over `Y`**, or a **`Y`-prescheme of finite presentation**.*

Condition (iii) is automatically satisfied if `f` is separated, or if `X` is locally Noetherian `(1.2.8)`; when `Y` is
locally Noetherian, to say that `f` is of finite presentation and to say that `f` is of finite type are equivalent (the
latter condition implying that `X` is locally Noetherian `(1.3.3)`).

<!-- original page 235 -->

**Proposition (1.6.2).**

<!-- label: IV.1.6.2 -->

*(i) Every quasi-compact immersion locally of finite presentation (in particular, every quasi-compact open immersion) is
of finite presentation.*

*(ii) The composite of two morphisms of finite presentation is of finite presentation.*

*(iii) Let `X`, `Y` be two `S`-preschemes, `f : X → Y` an `S`-morphism of finite presentation. Then, for every morphism
`S' → S`, the morphism `f_{(S')} : X_{(S')} → Y_{(S')}` is of finite presentation.*

*(iv) Let `f : X → Y`, `f' : X' → Y'` be two `S`-morphisms of finite presentation; then `f ×_S f' : X ×_S X' → Y ×_S Y'`
is of finite presentation.*

*(v) If the composite `g ∘ f` of two morphisms is of finite presentation, and if `g` is quasi-separated and locally of
finite presentation, then `f` is of finite presentation.*

This results immediately from `(1.1.2)`, `(1.2.2)`, `(1.2.4)`, and `(1.4.3)`.

It follows in particular from `(1.6.2, (iii))` that if `f` is a morphism of finite presentation and `U` an open set of
`Y`, the restriction `f⁻¹(U) → U` of `f` is a morphism of finite presentation. Conversely, let `(U_α)` be a cover of `Y`
by affine open sets, and suppose that the restrictions `f⁻¹(U_α) → U_α` of `f` are morphisms of finite presentation; it
then follows that `f` is of finite presentation, since `f` is manifestly locally of finite presentation, quasi-compact
by virtue of `(1.1.1)`, and quasi-separated by virtue of `(1.2.6)`. One may therefore say that the property of a
morphism `f : X → Y` of being of finite presentation is *local on `Y`*.

If `X` is a quasi-separated prescheme, every morphism `f : X → Y` is quasi-separated `(1.2.3)`. Therefore, if `f` is
quasi-compact and locally of finite presentation, `f` is then of finite presentation.

In particular:

**Corollary (1.6.3).**

<!-- label: IV.1.6.3 -->

*Let `φ : A → B` be a ring homomorphism. For the corresponding morphism `f : Spec(B) → Spec(A)` to be of finite
presentation, it is necessary and sufficient that `φ` make `B` into an `A`-algebra of finite presentation.*

The necessity of the condition results from `(1.4.6)`.

**Remark (1.6.4).**

<!-- label: IV.1.6.4 -->

In definition `(1.6.1)`, condition (iii) is not a consequence of the two others. Let, for example, `Y` be an affine
scheme whose underlying space is not Noetherian, and let `U` be a non-quasi-compact open set in `Y`. Let `X` be the
prescheme obtained by gluing two preschemes `Y_1`, `Y_2` isomorphic to `Y` along the open sets `U_1`, `U_2`
corresponding to `U` `(0_I, 4.1.7)`, so that `X` is a union of two open sets isomorphic respectively to `Y_1` and `Y_2`
(and which we identify with these), with `Y_1 ∩ Y_2 = U`. In addition, there is a morphism `f : X → Y` that coincides on
`Y_i` with the given isomorphism `Y_i → Y` (`i = 1, 2`). It is clear that `f` satisfies condition (i) of `(1.6.1)`,
being a local isomorphism; it also satisfies (ii), the inverse image of a quasi-compact open set of `Y` being the union
of its images in `Y_1` and `Y_2`; but as `Y_1 ∩ Y_2` is not quasi-compact, `f` is not quasi-separated `(1.2.7)`.

**Proposition (1.6.5).**

<!-- label: IV.1.6.5 -->

*Let `X'`, `X''` be two preschemes, `X = X' ⨿ X''` their sum, `f' : X' → Y`, `f'' : X'' → Y` two morphisms, `f : X → Y`
the morphism that coincides with `f'` on `X'` and with `f''` on `X''`. For `f` to be of finite presentation it is
necessary and sufficient that `f'` and `f''` be so.*

It suffices to show that for `f` to possess one of the three properties of definition

<!-- original page 236 -->

`(1.6.1)`, it is necessary and sufficient that `f'` and `f''` possess it; this is clear for the property of being
locally of finite presentation, which is local on `X`; for the property of being quasi-compact, this was seen in
`(1.1.6)`, and for the property of being quasi-separated, in `(1.2.9)`.

### 1.7. Improvements of earlier results

We give in this number a list of propositions proved in the preceding chapters whose statement may be improved by means
of the new finiteness conditions introduced above.

**(1.7.1)** In the statements of `(I, 6.4.2, 6.4.3, and 6.4.9)`, one may, instead of supposing that `X` and `Y` are of
finite type over the field `K`, suppose only that they are *locally of finite type* over `K`; for `(I, 6.4.2)`, it
suffices to observe that every point of a prescheme `X` which is closed in every affine open set of `X` is closed in
`X`, and an affine scheme locally of finite type over `K` is *ipso facto* of finite type `(1.5.1)`. For `(I, 6.4.9)`,
one uses `(1.3.7)` and `(1.3.4, (v))`.

**(1.7.2)** In `(I, 6.5.1, (ii))`, one may, instead of supposing that `S` is locally Noetherian and `Y` of finite type
over `S`, suppose only that `Y` is *locally of finite presentation* over `S`, as the proof immediately shows (applying
definition `(1.4.2)`). Similarly, in `(I, 6.5.4, (ii))` and `(I, 6.5.5, (ii))` it suffices to suppose that `f` is an
`S`-morphism, `Y` being locally of finite presentation over `S`.

**(1.7.3)** In `(I, 7.1.11)`, for the second assertion, instead of supposing `S` locally Noetherian and `Y` of finite
type over `S`, one may suppose only `Y` locally of finite presentation over `S` (the proof depending on
`(I, 6.5.1, (ii))`); similarly in `(I, 7.1.12 to 7.1.15)`.

**(1.7.4)** In `(I, 9.2.2)`, one may replace the three hypotheses by the single hypothesis (entailed by each of the
others) that `f` is *quasi-compact and quasi-separated*, by virtue of `(1.2.6)` and `(1.2.7)`. Note that in
`(I, 9.2.1)`, the hypothesis means exactly that `f` is quasi-compact and quasi-separated.

**(1.7.5)** In `(I, 9.3.1, 9.3.2, and 9.3.3)`, one may replace the two hypotheses on `X` by the hypothesis (less
restrictive) that `X` is a *quasi-compact and quasi-separated* prescheme, the proof using exactly these two properties
(by virtue of `(1.2.7)`).

**(1.7.6)** In `(I, 9.3.4 and 9.3.5)`, it suffices to suppose `X` quasi-compact, and `ℱ` and `𝒥` quasi-coherent and of
finite type.

**(1.7.7)** In `(I, 9.4.7)`, one may weaken hypothesis b) by supposing only `X` *quasi-separated*, since it suffices
only that the canonical immersion `U → X` be quasi-compact `(1.2.7)`. One may make the same modification in
`(I, 9.4.8, 9.4.9, and 9.4.10)`.

**(1.7.8)** In `(I, 9.5.1)`, the conditions indicated in parentheses in the statement may be replaced by the condition
that `f` be quasi-compact and quasi-separated.

**(1.7.9)** In `(I, 9.6.5)`, one may replace the hypotheses on `X` by the less restrictive hypothesis that `X` is
*quasi-compact and quasi-separated*, as the proof shows, since it

<!-- original page 237 -->

uses only `(I, 9.4.7)`. In `(I, 9.6.6)`, the hypothesis "`X` is a quasi-compact scheme" may be replaced by "`X` is a
quasi-compact and quasi-separated prescheme".

**(1.7.10)** In `(II, 1.7.15)`, one may suppose only that `Y` is quasi-compact and quasi-separated, the proof using only
`(I, 9.6.5)`.

**(1.7.11)** In the second assertion of `(II, 3.4.5)`, one may substitute for the two hypotheses on `Y` the weaker
hypothesis that `Y` is quasi-compact and quasi-separated. Similarly in `(II, 3.4.8)`.

**(1.7.12)** In `(II, 3.8.5)`, one may likewise suppose only that `Y` is quasi-compact and quasi-separated, this
hypothesis intervening through `(I, 9.4.7)`.

**(1.7.13)** In `(II, 4.4.1, 4.4.6, and 4.4.7)`, it suffices to suppose that `Y` is *quasi-compact and quasi-separated*,
taking account of `(1.2.3)` in the proof of `(II, 4.4.7)`. Similarly, in `(II, 4.4.10.1)`, it suffices to suppose `Z`
quasi-compact and quasi-separated.

**(1.7.14)** In `(II, 4.5.2)` and `(II, 4.5.5)`, it suffices to suppose `X` *quasi-compact and quasi-separated*, this
hypothesis intervening through `(I, 9.3.1 and 9.3.2)`.

**(1.7.15)** In `(II, 4.6.8)`, it again suffices to suppose `X` *quasi-compact and quasi-separated*, this hypothesis
intervening through `(I, 9.4.7)`.

**(1.7.16)** In `(II, 5.1.2)`, it suffices to suppose that `X` is quasi-compact and quasi-separated (the hypothesis
intervening through `(II, 4.5.2 and 4.5.5)`). Similarly in `(II, 5.1.9)`, where one uses `(I, 9.6.5)`.

**(1.7.17)** In `(II, 5.2.1)`, it again suffices to suppose `X` quasi-compact and quasi-separated (the hypothesis
intervening through `(II, 4.5.2)`).

**(1.7.18)** In `(II, 5.2.2)`, one must suppose `f` quasi-compact and `X` quasi-separated; the present proof is in fact
insufficient (with the hypotheses made), for from the fact that for every quasi-coherent `𝒪_X`-Module `ℱ` one has
`R^1 f_*(ℱ) = 0`, it does not necessarily follow, for an affine open set `U` of `Y`, that the same property holds for
the quasi-coherent `(𝒪_X | f⁻¹(U))`-Modules, if one does not know that such a Module is the *restriction* of a
quasi-coherent `𝒪_X`-Module (the same remark applying to conditions b) and c')); when `f` is quasi-compact and `X`
quasi-separated, this extension is possible by virtue of `(I, 9.4.7)`, modified above `(1.7.7)`.

**(1.7.19)** In `(II, 5.3.2)`, it suffices to suppose `Y` quasi-compact and quasi-separated (which intervenes through
`(II, 4.4.6 and 4.4.7)`). Similarly in `(II, 5.5.3, (ii))`.

**(1.7.20)** In `(III, 1.2.2, 1.2.3, and 1.2.4)`, one may replace the two hypotheses on `X` by the less restrictive
hypothesis that `X` is a quasi-compact and quasi-separated prescheme, the proof using only `(I, 9.3.3)`.

**(1.7.21)** In `(III, 1.4.10 to 1.4.14)`, one may replace "separated" by "quasi-separated", this hypothesis serving
only to allow application of `(I, 9.2.2)` (see above `(1.7.4)`). Similarly, in `(III, 1.4.15)`, it suffices to suppose
that the morphism `u` is quasi-separated and quasi-compact.

**(1.7.22)** In `(III, 2.1.3)`, one may again replace the hypotheses by the less restrictive hypothesis that `X` is a
quasi-compact and quasi-separated prescheme, the reasoning being the same as in `(III, 1.2.2)`.

<!-- original page 238 -->

### 1.8. Morphisms of finite presentation and constructible sets

**(1.8.1)**

<!-- label: IV.1.8.1 -->

Let `X` be a prescheme; one knows that every quasi-compact open set in `X` is a finite union of affine open sets, and
conversely. For an open set `U` of `X` to be **retrocompact** in `X` `(0_III, 9.1.1)`, it is therefore necessary and
sufficient that for every affine open set `V` of `X`, `U ∩ V` be quasi-compact. When `X` is *quasi-separated* `(1.2.1)`,
every quasi-compact open set in `X` is retrocompact in `X` `(1.2.7)`, so every locally constructible part of `X` is
retrocompact in `X` `(0_III, 9.1.13)`; if moreover `X` is *quasi-compact*, there is identity between constructible parts
and locally constructible parts in `X` `(0_III, 9.1.12)`, and between open constructible parts and open quasi-compact
parts `(0_III, 9.1.5)`.

**Proposition (1.8.2).**

<!-- label: IV.1.8.2 -->

*Let `X`, `Y` be two preschemes, `f : X → Y` a morphism. For every constructible (resp. locally constructible) part `Z`
of `Y`, `f⁻¹(Z)` is a constructible (resp. locally constructible) part of `X`.*

Suppose `Z` locally constructible; for every `x ∈ X` there will be an affine open neighbourhood `V` of `f(x)` such that
`Z ∩ V` is constructible in `V`; if the proposition is proved for constructible parts, `f⁻¹(Z) ∩ f⁻¹(V)` will be
constructible in `f⁻¹(V)`, so `f⁻¹(Z)` will be locally constructible. It therefore suffices to consider the case where
`Z` is constructible, and, taking account of `(0_III, 9.1.3)`, one is reduced to the case where `Z` is open and
retrocompact in `Y`, that is, such that the canonical injection `Z → Y` is a quasi-compact morphism; it then suffices to
see that `f⁻¹(Z)` is retrocompact in `X`, that is, such that the canonical injection `f⁻¹(Z) → X` is a quasi-compact
morphism; but this results from `(1.1.2, (iii))`, since `f⁻¹(Z) = Z ×_Y X` `(I, 4.4.1)`.

**Lemma (1.8.3).**

<!-- label: IV.1.8.3 -->

*Let `X` be a quasi-compact and quasi-separated prescheme, `Z` a constructible part of `X`. There then exist an affine
scheme `X'` and a morphism of finite presentation `f : X' → X` such that `f(X') = Z`.*

As `X` is quasi-compact, it is a finite union of affine open sets `X_i` (`i ∈ I`), and as `X` is quasi-separated, it
follows from `(1.2.7)` that each of the canonical immersions `g_i : X_i → X` is of finite presentation; one concludes
that if `f_i : X'_i → X_i` is a morphism of finite presentation, so is `g_i ∘ f_i : X'_i → X` `(1.6.2)`, and if `X'` is
the sum prescheme of the `X'_i`, the morphism `h : X' → X` coinciding with `g_i ∘ f_i` on each `X'_i` is also of finite
presentation `(1.6.5)`. As `Z ∩ X_i` is constructible in `X_i` `(0_III, 9.1.8)`, one sees that one is reduced to proving
the lemma when `X_i` is affine of ring `A`. Since `Z` is then a finite union of sets of the form `U ∩ ∁V`, where `U` and
`V` are quasi-compact open sets `(0_III, 9.1.3)`, one sees, by considering again a suitable sum of preschemes, that one
may reduce to the case where `Z = U ∩ ∁V`; moreover, since `U` is a finite union of affine open sets, one may even
restrict to the case where `U` is affine. Since `V` is quasi-compact, it is a finite union of open sets of the form
`X_{f_i}`, where `f_i ∈ A`; let `𝔍` be the ideal of `A` generated by the `f_i`, and let `Z'` be the closed affine
subscheme of `X` that it defines (and which is by construction of finite presentation over `X`); by definition
`V = ∁Z'`, so `U ∩ ∁V = U ∩ Z'`. Consider the affine scheme `X' = Z' ×_X U`,

<!-- original page 239 -->

and let `f : X' → X` be the structure morphism; one has just seen that the canonical immersion `Z' → X` is of finite
presentation, and the same is true of the open immersion `U → X`, which is quasi-compact since `U` and `X` are affine;
one concludes therefore from `(1.6.2, (iv))` that `f` is of finite presentation, and one has `f(X') = Z' ∩ U`
`(I, 3.4.8)`, which completes the proof.

**Theorem (1.8.4) (Chevalley).**

<!-- label: IV.1.8.4 -->

*Let `f : X → Y` be a morphism of finite presentation. For every locally constructible part `Z` of `X`, `f(Z)` is
locally constructible in `Y`.*

Let `y ∈ Y` and `V` an affine open neighbourhood of `y`; since `f` is quasi-compact and quasi-separated, so is its
restriction `f⁻¹(V) → V`, hence `f⁻¹(V)` is a quasi-compact and quasi-separated prescheme `(1.2.3)`; as `Z ∩ f⁻¹(V)` is
constructible in `f⁻¹(V)` `(1.8.1)`, one sees that one may restrict to the case where `Y` is affine and `Z`
constructible; `X` is then quasi-compact and quasi-separated, so `(1.8.3)` there exists a morphism of finite
presentation `g : X' → X` such that `Z = g(X')`; since `f ∘ g` is of finite presentation, one sees that one is reduced
to the case where `Z = X`; in other words, it will suffice to prove:

**Lemma (1.8.4.1).**

<!-- label: IV.1.8.4.1 -->

*Let `Y` be an affine scheme, `f : X → Y` a quasi-compact morphism locally of finite presentation; then `f(X)` is a
constructible part of `Y`.*

As `X` is quasi-compact, it is a finite union of affine open sets; one may therefore restrict to the case where
`Y = Spec(A)`, `X = Spec(B)`, `B` being an `A`-algebra of finite presentation `(1.4.6)`. Now, one has:

**Lemma (1.8.4.2).**

<!-- label: IV.1.8.4.2 -->

*Let `A_0` be a ring, `(A_λ)_{λ ∈ L}` an inductive system of `A_0`-algebras, `A = lim_→ A_λ`; if `B` is an `A`-algebra
of finite presentation, there exist a `λ` and an `A_λ`-algebra of finite presentation `B_λ` such that `B` is isomorphic
to `B_λ ⊗_{A_λ} A`.*

By hypothesis, `B` is isomorphic to an algebra of the form `A[T_1, …, T_n] / 𝔍`, where the `T_i` are indeterminates and
`𝔍` an ideal of finite type; let `(F_j)` (`1 ≤ j ≤ m`) be a system of generators of `𝔍`. Let `φ_λ : A_λ → A` be the
canonical homomorphism. As `L` is filtered, there exists `λ` such that each of the coefficients of each of the
polynomials `F_j` is the image under `φ_λ` of an element of `A_λ`. In other words, there exists a system of polynomials
`(F_{j λ})_{1 ≤ j ≤ m}` of `A_λ[T_1, …, T_n]` such that `F_j = φ_λ(F_{j λ})` for `1 ≤ j ≤ m`. If `𝔍_λ` is the ideal of
`A_λ[T_1, …, T_n]` generated by the `F_{j λ}`, `𝔍` is the image of `𝔍_λ ⊗_{A_λ} A` in
`A[T_1, …, T_n] = A_λ[T_1, …, T_n] ⊗_{A_λ} A`; the ring `B_λ = A_λ[T_1, …, T_n] / 𝔍_λ` answers the question.

One will apply this lemma here by considering `A` as the inductive limit of its sub-`ℤ`-algebras of finite type. One
sees therefore that there exists such a sub-`ℤ`-algebra `A_0` of `A`, and an `A_0`-algebra of finite presentation `B_0`
such that `B` is isomorphic to `B_0 ⊗_{A_0} A`; set `X_0 = Spec(B_0)`, `Y_0 = Spec(A_0)`, so that `X = X_0 ×_{Y_0} Y`,
`f` being the projection `X → Y`; let `f_0 : X_0 → Y_0`, `g_0 : Y → Y_0` be the structure morphisms; it follows from
`(I, 3.4.8)` that one has `f(X) = g_0⁻¹(f_0(X_0))`; taking account of `(1.8.2)`, it therefore suffices to show that
`f_0(X_0)` is constructible. In other words, one is finally reduced to proving:

**Corollary (1.8.5).**

<!-- label: IV.1.8.5 -->

*Let `Y` be a Noetherian prescheme, `f : X → Y` a morphism of finite type. For every constructible part `Z` of `X`,
`f(Z)` is a constructible part of `Y`.*

<!-- original page 240 -->

One reduces as above to proving that `f(X)` is constructible. Apply criterion `(0_III, 9.2.3)`: it suffices to prove
that for every irreducible closed part `T` of `Y`, `T ∩ f(X) = f(f⁻¹(T))` is either rare in `T` or contains a non-empty
open of `T`; taking a subprescheme of `Y` having `T` as underlying space `(I, 5.2.1)` and considering its inverse image
under `f`, one sees finally (taking account of `(1.5.4, (iii))`) that one is reduced to proving that if one supposes `Y`
*irreducible* and `f` *dominant*, then `f(X)` contains a non-empty open of `Y`. One may further suppose `Y` affine; then
`X` is a finite union of affine open sets `V_i`, and as `f(X)` is dense in `Y`, the same is true of at least one of the
`f(V_i)`. One may therefore also suppose `X` affine; if `(X_j)` is the (finite) family of irreducible components of `X`,
one sees as above that at least one of the `f(X_j)` is dense in `Y`; one may therefore suppose `X` irreducible. Finally,
replacing `f` by `f_red` `(1.5.4, (vi))`, one may suppose `X` and `Y` integral. Then `X = Spec(B)`, `Y = Spec(A)`, where
`A` is a Noetherian integral ring, `B` an integral `A`-algebra of finite type containing `A` `(I, 1.2.7)`. It suffices
to show that there exists `g ∈ A` such that, for every `y ∈ D(g)` (that is, such that `g ∉ 𝔧_y`), the ideal `𝔧_y` is the
intersection of `A` and a prime ideal of `B`, for this will show that `D(g) ⊂ f(X)`. Finally, it suffices to prove:

**Lemma (1.8.5.1).**

<!-- label: IV.1.8.5.1 -->

*Let `A` be an integral ring, `B` an integral `A`-algebra of finite type. There exists `g ∈ A` such that every
homomorphism of `A` into an algebraically closed field `Ω`, non-zero on `g`, extends to a homomorphism of `B` into `Ω`.*

Now, this is a classical result of commutative algebra `(Bourbaki, Alg. comm., chap. V, §3, n° 1, cor. 3 du th. 1)`.

**Corollary (1.8.6).**

<!-- label: IV.1.8.6 -->

*Let `Y` be an irreducible prescheme, `η` its generic point, `f : X → Y` a morphism locally of finite type. If `f⁻¹(η)`
is not empty, there exists an open neighbourhood `U` of `η` in `Y` such that `f⁻¹(y)` is non-empty for every `y ∈ U`. If
`ℱ` is a quasi-coherent `𝒪_X`-Module of finite type, and if `ℱ_η = ℱ ⊗_{𝒪_Y} k(η)` is not zero, then there exists an
open neighbourhood `U'` of `η` in `Y` such that `ℱ_y = ℱ ⊗_{𝒪_Y} k(y)` is not zero for every `y ∈ U'`.*

If `p_y` is the canonical projection of the fibre `f⁻¹(y) = X ×_Y Spec(k(y))` into `X`, one has `ℱ_y = p_y^*(ℱ)`, so
`Supp(ℱ_y) = p_y⁻¹(Supp(ℱ)) = Supp(ℱ) ∩ f⁻¹(y)` by virtue of `(I, 9.1.13.1)` and `(I, 3.6.1)`, since `ℱ` is of finite
type; furthermore `Supp(ℱ)` is closed in `X` `(0_I, 5.2.2)`, and if `Z` is a closed subprescheme of `X` having `Supp(ℱ)`
as underlying space `(I, 5.2.1)`, and `j` the canonical immersion `Z → X`, `f ∘ j` is locally of finite type `(1.3.4)`;
this shows that the first assertion entails the second. To prove the first assertion, remark first that one may suppose
`X` and `Y` reduced `(1.3.4, (vi))`, that is, `Y` integral. Let `ξ` be a point of `f⁻¹(η)`; one may replace `X` and `Y`
by affine open neighbourhoods of `ξ` and `η` respectively, and hence suppose that `X = Spec(B)`, `Y = Spec(A)`, `B`
being an `A`-algebra of finite type. In addition, if `Z` is the reduced closed subprescheme of `X` having `‾{ξ}` as
underlying set `(I, 5.2.1)`, one may, as above, replace `X` by `Z`, that is, suppose `B` integral `(I, 5.1.4)`. As the
morphism `f` is then dominant, the corresponding homomorphism `φ : A → B` is injective `(I, 1.2.7)`; so the corollary
results finally from lemma `(1.8.5.1)`.

<!-- original page 241 -->

**Proposition (1.8.7).**

<!-- label: IV.1.8.7 -->

*Let `S` be a prescheme, `g : X → S`, `h : Y → S` two morphisms of finite presentation, `f : X → Y` an `S`-morphism. For
every `s ∈ S`, set `X_s = g⁻¹(s) = X ×_S Spec(k(s))`, `Y_s = h⁻¹(s) = Y ×_S Spec(k(s))`, `f_s = f × 1 : X_s → Y_s`. Then
the set of `s ∈ S` such that `f_s` is surjective (resp. radicial) is locally constructible.*

Let `E` be the set of `s ∈ S` such that `f_s` is surjective; the set `S − E` is equal to `h(Y − f(X))`; now `f` is of
finite presentation `(1.6.2, (v))`, so `f(X)` is locally constructible in `Y` `(1.8.4)`; since `h` is of finite
presentation, `h(Y − f(X))` is locally constructible in `S`, hence so is `E`.

To show that the set `E'` of `s ∈ S` such that `f_s` is radicial is locally constructible, we will use:

**Lemma (1.8.7.1).**

<!-- label: IV.1.8.7.1 -->

*Let `U`, `V` be two preschemes; for a morphism `f : U → V` to be radicial, it is necessary and sufficient that the
diagonal morphism `Δ_f : U → U ×_V U` be surjective. Consequently, every radicial morphism is separated.*

Indeed, `Δ_f`, being an immersion `(I, 5.3.9)`, is a morphism locally of finite type `(1.3.4)`; to say that `Δ_f` is
surjective therefore means that for every algebraically closed field `K`, the corresponding map
`U(K) → (U ×_V U)(K) = U(K) ×_{V(K)} U(K)` is surjective `(1.3.7 and I, 3.4.2.1)`; but by definition of a fibre product
of sets, this means that the map `U(K) → V(K)` corresponding to `f` is injective, and this is equivalent to saying that
`f` is radicial `(I, 3.5.5)`.

This being so, `Δ_{f_s}` is deduced from `Δ_f : X → X ×_Y X` by the base change `Spec(k(s)) → S` `(I, 5.3.4)`. Since `f`
is of finite presentation, so is the structure morphism `X ×_Y X → Y` `(1.6.2, (iv))`, hence also `Δ_f` `(1.6.2, (v))`;
it therefore suffices to apply the first part of the proposition to `Δ_f`, using lemma `(1.8.7.1)`.

### 1.9. Pro-constructible and ind-constructible sets

**Lemma (1.9.1).**

<!-- label: IV.1.9.1 -->

*Let `(A_α)_{α ∈ I}` be an inductive system of rings whose index set `I` is filtered to the right, and let
`A = lim_→ A_α`. For `A = 0` it is necessary and sufficient that there exist an index `γ` such that `A_γ = 0` (and one
then has `A_β = 0` for every `β ≥ γ`).*

Indeed, for every `α ∈ I`, the canonical homomorphism `φ_α : A_α → A` transforms the unit element into the unit element;
to say that `A = 0` means that `φ_α(1) = 0`, or again that `φ_α(1) = φ_α(0)`; one knows that this is equivalent to
saying that there exists an index `γ ≥ α` such that the homomorphism `φ_{γα} : A_α → A_γ` is such that
`φ_{γα}(1) = φ_{γα}(0)`, and this last relation is equivalent to `A_γ = 0`, whence the lemma.

**Proposition (1.9.2).**

<!-- label: IV.1.9.2 -->

*Let `B` be a ring, `(A_α)_{α ∈ I}` an inductive system of `B`-algebras whose index set `I` is filtered to the right,
and let `A = lim_→ A_α`; set `Y = Spec(B)`, `X_α = Spec(A_α)`, `X = Spec(A)`, and let `u : X → Y`, `u_α : X_α → Y` be
the morphisms corresponding to the structure homomorphisms `B → A`, `B → A_α`. Then:*

*(i) For `X = ∅` it is necessary and sufficient that there exist a `γ ∈ I` such that `X_γ = ∅`, and one then has
`X_α = ∅` for `α ≥ γ`.*

<!-- original page 242 -->

*(ii) One has*

```text
  u(X) = ⋂_{α ∈ I} u_α(X_α).                                                    (1.9.2.1)
```

Assertion (i) is nothing but the translation of `(1.9.1)`. To prove (ii), note that, since `u` factors as
`X → X_α ─u_α→ Y`, the first member of `(1.9.2.1)` is contained in the second. Conversely, let `y ∈ Y − u(X)`; one has
`u⁻¹(y) = ∅`, and `u⁻¹(y)` is the space underlying the `k(y)`-prescheme `Spec(A ⊗_B k(y))`; as in the category of
`B`-modules the functor `lim_→` commutes with the tensor product, `A ⊗_B k(y)` is the inductive limit of the inductive
system of rings `A_α ⊗_B k(y)`; lemma `(1.9.1)` shows that there exists `α` such that `A_α ⊗_B k(y) = 0`, that is,
`u_α⁻¹(y) = ∅`, hence `y ∉ u_α(X_α)`. C.Q.F.D.

**Proposition (1.9.3).**

<!-- label: IV.1.9.3 -->

*Let `X` be a quasi-compact and quasi-separated prescheme, `E` a part of `X`, `(X_α)_{α ∈ I}` an affine open cover of
`X`, and for every `α ∈ I`, set `E_α = E ∩ X_α`. The following conditions are equivalent:*

*a) There exists a quasi-compact morphism `f : X' → X` such that `E = f(X')`.*

*a') For every `α`, there exists a quasi-compact morphism `f_α : X'_α → X_α` such that `E_α = f_α(X'_α)`.*

*a'') For every `α`, there exist an affine scheme `X'_α` and a morphism `f_α : X'_α → X_α` such that `f_α(X'_α) = E_α`.*

*b) `E` is an intersection of constructible parts of `X`.*

*b') `F = X − E` is a union of constructible parts of `X`.*

It is clear that b) and b') are equivalent. Condition a) entails a') by taking for `X'_α` the prescheme induced on the
open set `f⁻¹(X_α)` of `X'` and for `f_α` the restriction of `f`. To see that a') entails a''), it suffices to remark
that `X'_α` is a union of affine open sets `X''_{αλ}` (`λ ∈ L_α`); let `X''_α` be the sum prescheme of the `X''_{αλ}`
(`λ ∈ L_α`), which is an affine scheme; if `g_α : X''_α → X'_α` is the morphism coinciding with the identity on each of
the `X''_{αλ}`, it is clear that if one sets `f'_α = f_α ∘ g_α`, one has `E_α = f'_α(X''_α)` since `g_α` is surjective.
To show that a'') entails a), note that there is a finite subset `J` of `I` such that the `X_α` of indices `α ∈ J` cover
`X`; let `X'` be the sum prescheme of the `X'_α` for `α ∈ J`, and let `f : X' → X` be the morphism coinciding with
`j_α ∘ f_α` for every `α ∈ J`, where `j_α : X_α → X` is the canonical injection. As `E` is the union of the `E ∩ X_α`
for `α ∈ J`, one has indeed `E = f(X')`, and it remains to see that `f` is a quasi-compact morphism; but the hypothesis
that `X` is quasi-separated entails that `j_α` is quasi-compact `(1.2.7)`, hence so is `j_α ∘ f_α` `(1.1.1 and 1.1.2)`
and finally `f` `(1.1.6)`.

It remains then to prove the equivalence of a'') and b). Let us prove first that a'') entails b): consider a finite
subset `J` of `I` such that the `X_α` for `α ∈ J` cover `X`; it will suffice to show that, for every `α ∈ J`, `E_α` is
an intersection of constructible parts `F_{αλ}` of `X_α` (`λ ∈ L_α`); indeed, every `F_{αλ}` is also a constructible
part of `X` by virtue of `(0_III, 9.1.8, (ii))`, because the hypothesis that `X` is quasi-separated entails that every
`X_α` is retrocompact in `X` `(1.2.7)`; `E` being the union of the `E_α` for `α ∈ J`, is intersection of the (finite)
unions `⋃_{α ∈ J} F_{α, λ(α)}`, for all choices of `λ(α) ∈ L_α`; these unions being constructible in `X`, this
establishes our assertion. One may therefore restrict to the case

<!-- original page 243 -->

where `X = Spec(A)` and where `E = f(X')`, `X' = Spec(A')` being affine, `f : X' → X` a morphism corresponding to a ring
homomorphism `A → A'`. Note now that `A'` is the inductive limit of the family `(A'_λ)` of its sub-`A`-algebras of
finite type, ordered by inclusion; if `X'_λ = Spec(A'_λ)`, `f` factors as `X' → X'_λ ─f_λ→ X` and it results from
`(1.9.2, (ii))` that one has `f(X') = ⋂_λ f_λ(X'_λ)`; if one shows that `f_λ(X'_λ)` is an intersection of constructible
parts of `X`, the same will be true of `f(X')`. One may therefore restrict to the case where `A'` is an `A`-algebra of
finite type. Now, one has the following lemma:

**Lemma (1.9.3.1).**

<!-- label: IV.1.9.3.1 -->

*Let `A` be a ring, `A'` an `A`-algebra of finite type. Then `A'` is `A`-isomorphic to a filtered inductive limit
`lim_→ A''_μ` where the `A''_μ` are `A`-algebras of finite presentation `(1.4.1)`.*

Indeed, one may write `A' = B / 𝔍`, with `B = A[T_1, …, T_n]` and `𝔍` an ideal of `B`. But `𝔍` is the inductive limit of
the ideals of finite type `𝔍'_μ` of `B`, contained in `𝔍`, ordered by inclusion; as in the category of `B`-modules the
functor `lim_→` is exact, one concludes that `A' ≅ lim_→ B / 𝔍'_μ` up to an `A`-isomorphism.

The same reasoning as above then allows one to reduce to the case where `A'` is an `A`-algebra of finite presentation;
but then `f(X')` is constructible in `X` by virtue of Chevalley's theorem `(1.8.5)`, which proves b).

Let us finally prove that b) entails a''). If `E` is an intersection of a family `(G_λ)_{λ ∈ L}` of constructible parts
of `X`, each `E_α` is the intersection of the `G_λ ∩ X_α`, which are constructible in `X_α` `(0_III, 9.1.8, (i))`, so
one is reduced to the case where `X = Spec(A)` is affine.

One then knows `(1.8.3)` that for every `λ ∈ L` there exists a morphism `f_λ : X'_λ → X`, where `X'_λ = Spec(A'_λ)` is
affine, such that `f_λ(X'_λ) = G_λ`. It therefore suffices to prove the following lemma:

**Lemma (1.9.3.2).**

<!-- label: IV.1.9.3.2 -->

*Let `(A'_λ)_{λ ∈ L}` be a family of `A`-algebras, `X = Spec(A)`, `X'_λ = Spec(A'_λ)`, and let `f_λ : X'_λ → X` be the
structure morphism. For every finite subset `J` of `L`, set `A'_J = ⨂_{λ ∈ J} A'_λ` (tensor product of `A`-algebras),
`X'_J = Spec(A'_J)`, and let `f_J : X'_J → X` be the structure morphism. One then has*

```text
  f_J(X'_J) = ⋂_{λ ∈ J} f_λ(X'_λ).
```

*If `A' = lim_→ A'_J`, `J` running over the filtered set of finite parts of `L`, `X' = Spec(A')`, and if `f : X' → X` is
the structure morphism, one has*

```text
  f(X') = ⋂_{λ ∈ L} f_λ(X'_λ).
```

The first assertion results from `(I, 3.4.7)`; the second results from `(1.9.2, (ii))`, which gives the relation
`f(X') = ⋂_J f_J(X'_J)`.

**Definition (1.9.4).**

<!-- label: IV.1.9.4 -->

*Let `X` be a topological space. We say that a part `E` of `X` is **pro-constructible** (resp. **ind-constructible**) in
`X` if, for every `x ∈ X`, there exists an open neighbourhood `U` of `x` in `X` such that `E ∩ U` is the intersection
(resp. union) of locally constructible parts of `U`.*

Taking account of `(1.2.7)` and `(0_III, 9.1.8 and 9.1.12)`, the equivalent conditions of proposition `(1.9.3)` are
therefore expressed by saying that `E` is pro-constructible in `X`, the locally constructible sets in `X` being
identical to the constructible sets in `X` under the hypotheses of `(1.9.3)`.

<!-- original page 244 -->

**Proposition (1.9.5).**

<!-- label: IV.1.9.5 -->

*Let `X` be a prescheme.*

*(i) For a part `E` of `X` to be pro-constructible, it is necessary and sufficient that `X − E` be ind-constructible.*

*(ii) Every finite union and every intersection of pro-constructible parts of `X` is pro-constructible. Every finite
intersection and every union of ind-constructible parts of `X` is ind-constructible.*

*(iii) Every intersection (resp. union) of locally constructible parts of `X` is pro-constructible (resp.
ind-constructible). Conversely, if `X` is quasi-compact and quasi-separated, every pro-constructible (resp.
ind-constructible) part of `X` is an intersection (resp. union) of constructible parts of `X`.*

*(iv) Let `(U_α)` be an open cover of `X`. For a part `E` of `X` to be pro-constructible (resp. ind-constructible) in
`X`, it is necessary and sufficient that for every `α`, `E ∩ U_α` be pro-constructible (resp. ind-constructible) in
`U_α`.*

*(v) Every pro-constructible part `E` of `X` is retrocompact in `X`. For a locally closed part `E` of `X` to be
retrocompact in `X`, it is necessary and sufficient that it be pro-constructible in `X`.*

*(vi) Let `f : X' → X` be a morphism of preschemes; for every pro-constructible (resp. ind-constructible) part `E` of
`X`, `f⁻¹(E)` is pro-constructible (resp. ind-constructible) in `X'`.*

*(vii) Let `f : X' → X` be a quasi-compact morphism; for every pro-constructible part `E'` of `X'`, `f(E')` is
pro-constructible in `X`; in particular `f(X')` is pro-constructible in `X`.*

*(viii) Let `f : X' → X` be a morphism locally of finite presentation; for every ind-constructible part `E'` of `X'`,
`f(E')` is ind-constructible in `X`; in particular `f(X')` is ind-constructible in `X`.*

*(ix) Suppose `X` is quasi-compact and quasi-separated; then, for a part `E` of `X` to be pro-constructible, it is
necessary and sufficient that there exist an affine scheme `X'` and a morphism (necessarily quasi-compact) `f : X' → X`
such that `E = f(X')`.*

Properties (i), (ii), (iv), and the first assertion of (iii) result from definition `(1.9.4)` and are valid for an
arbitrary topological space, using the mutual distributivity of intersection and union and the fact that if `T` is
locally constructible in `X`, `T ∩ U` is locally constructible in `U` for every open `U` of `X`. If `X` is quasi-compact
and quasi-separated and `E` is pro-constructible in `X`, there is a finite cover `(U_i)` of `X` formed of affine open
sets such that `E ∩ U_i` is the intersection of constructible parts `M_{iλ}` of `U_i` (`λ ∈ L_i`); the `M_{iλ}` are also
constructible in `X` by virtue of `(1.2.7)` and `(0_III, 9.1.8, (ii))`, and `E` is the intersection of the finite unions
`⋃_i M_{i, λ(i)}` (where `λ(i) ∈ L_i` for every `i`), which are constructible parts of `X`; this proves the second
assertion of (iii). Assertion (ix) results from (iii) and from `(1.9.3)`. To prove the first assertion of (v), one may
restrict to the case where `X` is affine, and prove then that `E` is quasi-compact `(0_III, 9.1.1)`; but since `X` is
then quasi-separated, there exists by virtue of (ix) a quasi-compact morphism `f : X' → X` such that `E = f(X')`; as
`X'` is quasi-compact, the same is true of its image `E` under a continuous map.

To prove (vi), one may restrict, by virtue of (iv), to the case where `X` is affine; the conclusion then results from
(iii) and from `(1.8.2)`.

<!-- original page 245 -->

Similarly, to prove (vii), one may restrict to the case where `X` is affine; then `X'` is a finite union of affine open
sets `X'_i` and `f(E')` is the union of the `f(E' ∩ X'_i)`, so that one may also suppose `X'` affine, by virtue of (ii);
but then `E' = g(X'')`, where `g : X'' → X'` is a quasi-compact morphism, by virtue of (ix), and one has
`f(E') = f(g(X''))`, hence `f(E')` is pro-constructible since `g ∘ f` is quasi-compact.

One deduces from (vii) the proof of the second assertion of (v): indeed, let `E` be a locally closed and retrocompact
part of `X`, and consider a subprescheme of `X` having `E` as underlying space `(I, 5.2.1)`; the canonical injection
`j : E → X` is then by hypothesis a quasi-compact morphism, and it results from (vii) that `E = j(E)` is
pro-constructible in `X`.

Finally, to prove (viii), one may again suppose `X` affine; in addition, if `(X'_α)` is an affine open cover of `X'`
such that `E' ∩ X'_α` is a union of constructible parts of `X'_α` ((iii) and (iv)), `f(E')` is the union of the
`f(E' ∩ X'_α)`, and, by virtue of Chevalley's theorem `(1.8.4)`, each of the `f(E' ∩ X'_α)` is a union of constructible
parts of `X`, whence the conclusion.

**Exemples (1.9.6).**

<!-- label: IV.1.9.6 -->

Every *finite* part of a prescheme `X` is pro-constructible: indeed, it suffices to consider the parts `{x}` reduced to
a single point `(1.9.5, (ii))`, and `{x}` is the image of `Spec(k(x))` under the canonical morphism `Spec(k(x)) → X`,
which is quasi-compact; whence the conclusion by `(1.9.5, (vii))`. By contrast, a part `{x}` reduced to a point is not
necessarily ind-constructible; for example, let `A` be a Noetherian integral ring having an infinity of maximal ideals,
and let `x` be the generic point of `X = Spec(A)`; if `{x}` were ind-constructible in `X`, it would be constructible by
virtue of `(1.9.5, (iii))` and consequently would contain a non-empty open of `X` `(0_III, 9.2.2)`; but this contradicts
the hypothesis that `A` has infinitely many maximal ideals, by virtue of Artin–Tate's theorem `(0_IV, 16.3.3)`.

Every *closed* part `Y` of a prescheme `X` is pro-constructible, by `(1.9.5, (v))`. Every open part of `X` is therefore
ind-constructible, but an open part `U` of `X` is pro-constructible only if it is *retrocompact*, again by virtue of
`(1.9.5, (v))`.

Finally, if `X` is a *Noetherian* prescheme, hence quasi-separated `(1.2.8)`, it follows from `(1.9.5, (iii))` and from
`(0_III, 9.1.7)` that the ind-constructible parts of `X` are the *unions of locally closed parts* of `X`.

**Theorem (1.9.7).**

<!-- label: IV.1.9.7 -->

*Let `X` be a quasi-compact prescheme, `E` an ind-constructible part of `X`, `(F_λ)_{λ ∈ L}` a family of pro-
constructible parts of `X` such that `⋂_{λ ∈ L} F_λ ⊂ E`; then there exists a finite subset `J` of `L` such that
`⋂_{λ ∈ J} F_λ ⊂ E`.*

Note that the sets `F = X − E` and `F ∩ F_λ` are pro-constructible, so one is reduced to:

**Corollary (1.9.8).**

<!-- label: IV.1.9.8 -->

*Let `X` be a quasi-compact prescheme, `(F_λ)_{λ ∈ L}` a family of pro-constructible parts of `X` whose intersection is
empty; then there exists a finite subfamily `(F_λ)_{λ ∈ J}` whose intersection is empty.*

Covering `X` by a finite number of affine open sets, and using `(1.9.5, (iv))`, one is reduced to the case where `X` is
affine; by virtue of `(1.9.5, (ix))`, one has `F_λ = f_λ(X'_λ)`,

<!-- original page 246 -->

where `X'_λ = Spec(A'_λ)` is affine, and `f_λ` is a morphism `X'_λ → X`; then, with the notations of `(1.9.3.2)`, one
has by hypothesis `f(X') = ∅`, hence `X' = ∅`; but this entails by `(1.9.2, (i))` that there exists a finite subset `J`
of `L` such that `X'_J = ∅`, hence `f_J(X'_J) = ⋂_{λ ∈ J} F_λ = ∅`.

**Corollary (1.9.9).**

<!-- label: IV.1.9.9 -->

*Let `X` be a quasi-compact prescheme, `F` a pro-constructible part of `X`, `(E_λ)_{λ ∈ L}` a family of ind-
constructible parts of `X` such that `F ⊂ ⋃_{λ ∈ L} E_λ`; then there exists a finite subset `J` of `L` such that
`F ⊂ ⋃_{λ ∈ J} E_λ`. In particular, from every cover of `X` by ind-constructible parts, one can extract a finite cover
of `X`.*

This results from `(1.9.7)` by passing to complements.

**Proposition (1.9.10).**

<!-- label: IV.1.9.10 -->

*Let `X` be a prescheme. For a part `E` of `X` to be ind-constructible, it is necessary that, for every `x ∈ X`, the
intersection `E ∩ ‾{x}` be a neighbourhood of `x` in `‾{x}`. If `X` is locally Noetherian, this condition is
sufficient.*

Suppose `E` is ind-constructible, and let `Y` be the intersection of `‾{x}` and an affine open in `X` containing `x`;
there is therefore a subprescheme of `X` having `Y` as underlying space `(I, 5.2.1)`, and if `j : Y → X` is the
canonical injection, `E ∩ Y = j⁻¹(E)` is ind-constructible in `Y` `(1.9.5, (vi))`. Since `Y` is quasi-compact and
separated, `E ∩ Y` is therefore a union of constructible parts of `Y` `(1.9.5, (iii))`; consequently, there are two
opens `U`, `V` in `Y` such that `x ∈ U ∩ ∁V ⊂ E ∩ Y` `(0_III, 9.1.3)`. But as `x` is generic point of the irreducible
space `Y`, `V` is necessarily empty and one has `U ⊂ E ∩ Y`.

Suppose now `X` locally Noetherian, and let `E` be a part of `X` satisfying the condition of the statement. By virtue of
definition `(1.9.4)`, one may restrict to the case where `X` is Noetherian. Then, for every `x ∈ X`, `E ∩ ‾{x}` contains
a non-empty part of the form `U ∩ ‾{x}`, where `U` is open in `X`; this shows that `E` is a union of locally closed
parts of `X`, hence is ind-constructible `(1.9.6)`.

**Proposition (1.9.11).**

<!-- label: IV.1.9.11 -->

*Let `X` be a prescheme, `E` a part of `X`. The following properties are equivalent:*

*a) `E` is locally constructible.*

*b) `E` is ind-constructible and pro-constructible.*

*c) `E` and `X − E` are pro-constructible.*

*d) `E` and `X − E` are ind-constructible.*

It manifestly suffices to prove that d) entails a), and one may restrict to the case where `X` is affine. Then
`(1.9.5, (iii))`, `E` (resp. `X − E`) is a union of a family `(E_λ)` (resp. `(E'_μ)`) of constructible parts of `X`; as
the `E_λ` and the `E'_μ` form a cover of `X`, it follows from `(1.9.9)` that there are indices in finite number `λ_i`,
`μ_j` such that the `E_{λ_i}` and the `E'_{μ_j}` form a cover of `X`; this implies that `E` is the union of the
`E_{λ_i}`, hence is constructible.

**Corollary (1.9.12).**

<!-- label: IV.1.9.12 -->

*Let `f : X → Y` be a surjective morphism, which is either quasi-compact or locally of finite presentation. For a part
`E` of `Y` to be locally constructible (resp. pro-constructible, resp. ind-constructible), it is necessary and
sufficient that `f⁻¹(E)` be so in `X`.*

<!-- original page 247 -->

One knows that the condition is necessary `((1.8.2)` and `(1.9.5, (vi)))`; to show that it is sufficient, one is reduced
to the case where `X` is affine, by virtue of `(1.9.5, (iv))`; moreover, by virtue of `(1.9.11)`, one may restrict to
the case where `f⁻¹(E)` is pro-constructible, or to the case where `f⁻¹(E)` is ind-constructible. If `f` is surjective
and quasi-compact, and `f⁻¹(E)` pro-constructible, it follows from `(1.9.5, (vii))` that `E = f(f⁻¹(E))` is
pro-constructible. If `f` is surjective and locally of finite presentation, and `f⁻¹(E)` ind-constructible,
`E = f(f⁻¹(E))` is ind-constructible by `(1.9.5, (viii))`, which completes the proof.

**(1.9.13)**

<!-- label: IV.1.9.13 -->

Let `X` be a prescheme, `𝒯` its topology; it follows from `(1.9.5, (i) and (ii))` that the ind-constructible (resp.
pro-constructible) parts of `X` are the open (resp. closed) parts for a topology on `X`, called the **constructible
topology** and which we shall denote `𝒯_cons`; we shall denote by `X^cons` the set `X` endowed with the topology
`𝒯_cons`.

**Proposition (1.9.14).**

<!-- label: IV.1.9.14 -->

*Let `X` be a prescheme, `𝒯` its topology, `𝒯_cons` the constructible topology on `X`.*

*(i) The topology `𝒯_cons` is finer than `𝒯`.*

*(ii) The locally constructible parts of `X` are identical to the parts of the space `X^cons` that are at once open and
closed.*

*(iii) For every morphism `f : X → Y`, the underlying map from `X^cons` to `Y^cons` is continuous; we denote it
`f^cons`.*

*(iv) If the morphism `f : X → Y` is quasi-compact, `f^cons` is a closed map; in particular, if `f` is quasi-compact and
bijective, `f^cons` is a homeomorphism.*

*(v) If a morphism `f : X → Y` is locally of finite presentation, `f^cons` is an open map; in particular, if `f` is
bijective and locally of finite presentation, `f^cons` is a homeomorphism.*

*(vi) For every open `U` of `X`, the topology induced by `𝒯_cons` on `U` is identical to the topology of `U^cons`.*

Indeed, (i) results from the fact that every open for `𝒯` is an open for `𝒯_cons` `(1.9.6)`, and (ii) is a translation
of `(1.9.11)`; (iii), (iv), and (v) translate respectively `(1.9.5)`, (vi), (vii), and (viii). Finally to prove (vi), it
suffices to remark that the canonical injection `j : U → X` is locally of finite presentation `(1.4.3)`, so
`j^cons : U^cons → X^cons` is a continuous open map.

**Proposition (1.9.15).**

<!-- label: IV.1.9.15 -->

*Let `X` be a prescheme.*

*(i) For `X^cons` to be quasi-compact, it is necessary and sufficient that `X` be quasi-compact.*

*(ii) For `X^cons` to be separated, it is necessary and sufficient that `X` be quasi-separated, and `X^cons` is then
locally compact and totally disconnected.*

*(iii) For `X^cons` to be compact, it is necessary and sufficient that `X` be quasi-compact and quasi-separated.*

*(iv) Every point of `X` admits, for the topology `𝒯_cons`, an open and compact neighbourhood.*

*(v) For a morphism `f : X → Y` to be quasi-compact, it is necessary and sufficient that the continuous map
`f^cons : X^cons → Y^cons` be proper.*

(i) Since `𝒯_cons` is finer than `𝒯`, it is clear that if `X^cons` is quasi-compact, so is `X`; the converse results
from `(1.9.9)`.

(ii) Suppose `X` quasi-separated, and let us show that `X^cons` is totally disconnected: indeed, if `x`, `y` are two
distinct points of `X` and if for example `x ∉ ‾{y}`, there exists an

<!-- original page 248 -->

affine open neighbourhood `U` of `x` in `X` not containing `y`; as `X` is quasi-separated, `U` is retrocompact in `X`
`(1.2.7)`, so `U` and `X − U` are locally constructible in `X`, and consequently open in `X^cons` by virtue of
`(1.9.11)`, whence our assertion. Since on every affine open `U` of `X` the topology induced by `𝒯_cons` is that of
`U^cons` by virtue of `(1.9.14, (vi))`, it follows from the foregoing that `X^cons` is locally compact, since `U` is
open in `X^cons` and `U^cons` is compact. It remains to prove that if `X^cons` is separated, then `X` is
quasi-separated; consider in effect an affine open `U` of `X`; the topology induced on `U` by `𝒯_cons` is that of
`U^cons` `(1.9.14, (vi))`, so `U` is compact for this induced topology, since `U^cons` is compact by the first part of
the reasoning. If `V` is a second affine open in `X`, `U ∩ V` is then a compact part of the separated space `X^cons`,
being the intersection of two compact parts of this space; as the topology induced by `𝒯_cons` on `U ∩ V` is that of
`(U ∩ V)^cons` `(1.9.14, (vi))` and the identity map `(U ∩ V)^cons → U ∩ V` is continuous, one concludes that `U ∩ V` is
quasi-compact for the topology induced by `𝒯`; `X` is consequently quasi-separated by virtue of `(1.2.7)`.

(iii) is an immediate corollary of (i) and (ii).

(iv) For every `x ∈ X`, an affine open neighbourhood `U` of `x` for `𝒯` is also a neighbourhood of `x` for `𝒯_cons`, and
it is compact by virtue of (iii) and `(1.9.14, (vi))`, the topology induced on `U` by `𝒯_cons` being identical to that
of `U^cons`.

(v) Suppose `f` quasi-compact; then one already knows `(1.9.14, (iv))` that `f^cons` is a closed map. Let on the other
hand `y` be a point of `Y`, and set

```text
  Z = f⁻¹(y) = X ×_Y Spec(k(y));
```

`Z` is quasi-compact `(1.1.2, (iii))` and as the canonical morphism `p : Z → X` is injective, it results from (i) and
from the fact that the map `p^cons` is continuous that the topology induced on `f⁻¹(y)` by that of `X^cons` makes
`f⁻¹(y)` a quasi-compact space. This proves that `f^cons` is a proper map
`(Bourbaki, Top. gén., chap. I, 3e éd., §10, n° 2, th. 1)`. Conversely, suppose the continuous map `f^cons` is proper,
and let `V` be a quasi-compact open of `Y`; if `h : V → Y` is the canonical injection, `h^cons : V^cons → Y^cons` is
continuous and injective and `V^cons` is quasi-compact by (i), so the topology induced on `V` by that of `Y^cons` makes
`V` a quasi-compact space. The hypothesis that `f^cons` is proper then entails that the topology induced on `f⁻¹(V)` by
that of `X^cons` makes `f⁻¹(V)` a quasi-compact space `(loc. cit., prop. 6)`, so `f⁻¹(V)` is also a quasi-compact
subspace of `X`, which shows that the morphism `f` is quasi-compact.

**(1.9.16)**

<!-- label: IV.1.9.16 -->

We shall show later how one may, for every prescheme `X`, endow the space `X^cons` with a sheaf of rings making it a
prescheme whose local rings are all fields, identical to the residue fields at the points of `X`. Such preschemes are
introduced, for example, in a natural way in the translation, in the language of schemes, of Néron's constructions [32]
in his theory of the reduction of abelian varieties.

<!-- original page 249 -->

### 1.10. Application to open morphisms

**Theorem (1.10.1).**

<!-- label: IV.1.10.1 -->

*Let `X` be a prescheme, `E` an ind-constructible part of `X` `(1.9.4)`, `x` a point of `X`. For `x` to be interior to
`E`, it is necessary and sufficient that every generization `(0_I, 2.1.2)` `x'` of `x` belong to `E`, in other words
`(I, 2.4.2)` that one have `Spec(𝒪_{X,x}) ⊂ E`.*

The condition is obviously necessary, every neighbourhood of `x` containing the generizations of `x`. To see that it is
sufficient, one may obviously restrict to the case where `X = Spec(A)` is affine, `x` being a prime ideal `𝔭` of `A`.
One then knows `(1.9.5, (ix))` that there exists an affine scheme `X' = Spec(A')` and a morphism `f : X' → X` such that
`f(X') = X − E`. Set `Y = Spec(𝒪_{X,x})` and `Y' = X' ×_X Y`; the hypothesis means (by virtue of `(I, 3.6.5)`) that one
has `Y' = ∅`, in other words `A' ⊗_A A_𝔭 = 0`. As `A_𝔭 = lim_→ A_t`, where `t` runs over `A − 𝔭` `(0_I, 1.4.5)`, one has
`lim_→ A'_t = 0`, the functor `lim_→` commuting with the tensor product. Consequently `(1.9.1)`, there exists a
`t ∈ A − 𝔭` such that `A'_t = 0`, and `D(t)` is then an open neighbourhood of `x` in `X` contained in `E`.

**Corollary (1.10.2).**

<!-- label: IV.1.10.2 -->

*Let `f : X → Y` be a morphism locally of finite presentation, and let `y ∈ Y`. For `y` to be interior to `f(X)` it is
necessary and sufficient that every generization `y'` of `y` belong to `f(X)`.*

One knows indeed `(1.9.5, (viii))` that `f(X)` is ind-constructible in `Y`, and it suffices to apply `(1.10.1)`.

We shall say that a continuous map `f : X → Y` is **open at a point `x ∈ X`** if the image under `f` of every
neighbourhood of `x` in `X` is a neighbourhood of `f(x)` in `Y`.

**Proposition (1.10.3).**

<!-- label: IV.1.10.3 -->

*Let `f : X → Y` be a morphism, `x` a point of `X`, `y = f(x)`. Consider the following conditions:*

*a) `f` is open at the point `x`.*

*b) For every generization `y'` of `y`, there exists a generization `x'` of `x` such that `f(x') = y'`.*

*b') The image under `f` of `Spec(𝒪_{X,x})` is `Spec(𝒪_{Y,y})`.*

*c) For every irreducible closed part `Y'` of `Y` containing `y`, there exists an irreducible component of
`X' = f⁻¹(Y')` containing `x` and dominating `Y'`.*

*Then one has the implications a) ⟹ b) ⟺ b') ⟸ c). If in addition `f` is locally of finite presentation, the four
conditions are equivalent.*

By definition of a generization, the image under `f` of `Spec(𝒪_{X,x})` is always contained in `Spec(𝒪_{Y,y})`, so b)
and b') are equivalent. It is immediate that c) entails b), because if `y'` is a generization of `y`, `Y' = ‾{y'}` is an
irreducible part of `Y` containing `y`; if `x'` is the generic point of an irreducible component of `f⁻¹(Y')` which
contains `x` and dominates `Y'`, one has `f(x') = y'` `(0_I, 2.1.5)` and `x'` is a generization of `x`. Conversely, b)
entails c): indeed, let `y'` be the generic point of `Y'` and let `x'` be a generization of `x` such that `f(x') = y'`;
let `Z'` be an irreducible component of `f⁻¹(Y')` containing `x'` (hence `x`); as `f(x')` is already dense in `Y'`, *a
fortiori* so is `f(Z')`.

To see that a) entails b'), one may obviously restrict to the case where `X = Spec(B)` and `Y = Spec(A)` are affine, `x`
being a prime ideal `𝔮` of `B`, so that `𝒪_{X,x} = B_𝔮 = lim_→ B_t`,

<!-- original page 250 -->

where `t` runs over `B − 𝔮`. One then has, by `(1.9.2)`, `f(Spec(𝒪_{X,x})) = ⋂_t f(Spec(B_t)) = ⋂_t f(D(t))`, and by
hypothesis, for every `t ∈ B − 𝔮`, `y` is interior to `f(D(t))`, so `f(D(t))` contains `Spec(𝒪_{Y,y})`; whence
`Spec(𝒪_{Y,y}) ⊂ f(Spec(𝒪_{X,x}))`, which establishes our assertion. Finally, when `f` is locally of finite
presentation, b) implies a) by virtue of `(1.10.2)` applied to the restriction `U → Y` of `f` to an arbitrary open
neighbourhood `U` of `x`.

**Corollary (1.10.4).**

<!-- label: IV.1.10.4 -->

*Let `f : X → Y` be a morphism. Consider the following conditions:*

*a) `f` is open.*

*b) For every `x ∈ X` and every generization `y'` of `y = f(x)`, there exists a generization `x'` of `x` such that
`f(x') = y'`.*

*b') For every `x ∈ X`, the image under `f` of `Spec(𝒪_{X,x})` is `Spec(𝒪_{Y,f(x)})`.*

*c) For every irreducible closed part `Y'` of `Y`, every irreducible component of `f⁻¹(Y')` dominates `Y'`.*

*Then one has the implications a) ⟹ b) ⟺ b') ⟸ c). If in addition `f` is locally of finite presentation, the four
conditions are equivalent.*

To say that `f` is open means that `f` is open at every point `x ∈ X`, so the implications a) ⟹ b) ⟺ b') result from the
analogous implications in `(1.10.3)`, as does the implication b) ⟹ a) when `f` is locally of finite presentation. The
implication c) ⟹ b) also results from the analogous implication in `(1.10.3)`; let us finally prove that b) entails c).
Indeed, let `x'` be the generic point of an irreducible component of `f⁻¹(Y')`, and let us show that `y' = f(x')` is the
generic point of `Y'`. Let `y''` be a generization of `y'`; there exists by hypothesis a generization `x''` of `x'` such
that `f(x'') = y''`, and as `x'' ∈ f⁻¹(Y')`, one has necessarily `x'' = x'`, hence `y'' = y'`, which completes the
proof.

*(To be continued.)*

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/12-c4-s01-conditions-finitude-relatives.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-1.pdf, pp. 224-250 -->

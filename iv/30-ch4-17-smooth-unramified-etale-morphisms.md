<!-- original page 56 -->

## §17. Smooth, unramified, étale morphisms

In the present section, we take up again the notions studied in `(0, 19)`, expressed by means of the geometric language
of schemes and from the global point of view, for preschemes locally of finite presentation over a given base prescheme.
Most of the results (with the exception of nos. 17.7, 17.8, 17.9, 17.13, and 17.16) in fact reduce to variants of
properties already encountered in `(0, 19)`. For more special results on étale morphisms, the reader will consult §18.

### 17.1. Formally smooth, formally unramified, formally étale morphisms

**Definition (17.1.1).**

<!-- label: IV.17.1.1 -->

*Let `f : X → Y` be a morphism of preschemes. One says that `f` is **formally smooth** (resp. **formally unramified**,
resp. **formally étale**) if, for every affine scheme `Y'`, every closed subscheme `Y_0` of `Y'` defined by a nilpotent
Ideal `𝓙` of `𝒪_{Y'}`, and every morphism `Y' → Y`, the map*

```text
  (17.1.1.1)    Hom_Y(Y', X) → Hom_Y(Y_0, X)
```

*deduced from the canonical injection `Y_0 → Y'`, is surjective (resp. injective, resp. bijective).*

*One also says in that case that `X` is **formally smooth** (resp. **formally unramified**, resp. **formally étale**)
over `Y`.*

It is clear that to say that `f` is formally étale signifies that it is at once formally smooth and formally unramified.

**Remarks (17.1.2).** — (i) Suppose that `Y = Spec(A)` and `X = Spec(B)` are affine, so that `f` comes from a ring
homomorphism `φ : A → B`. By virtue of `(0, 19.3.1 and 0, 19.10.1)`, to say that `f` is formally smooth (resp. formally
unramified, resp. formally étale) signifies that `φ` makes `B` into a formally smooth (resp. formally unramified, resp.
formally étale) `A`-algebra for the discrete topologies on `A` and `B`.

(ii) To verify that `f` is formally smooth (resp. formally unramified, resp. formally étale), one can, in the definition
`(17.1.1)`, restrict to the case where `𝓙² = 0`. Indeed, if `f` verifies the corresponding condition of definition
`(17.1.1)` in this particular case, and if one has `𝓙^n = 0`, one considers the closed subscheme `Y'_j` of `Y'` defined
by the Ideal `𝓙^{j+1}` for `0 ⩽ j ⩽ n − 1`, so that `Y'_j` is a closed subscheme of `Y'_{j+1}` defined by an Ideal of
square zero; the hypothesis implies that each of the maps

```text
  Hom_Y(Y'_{j+1}, X) → Hom_Y(Y'_j, X)    (0 ⩽ j ⩽ n − 1)
```

<!-- original page 57 -->

is surjective (resp. injective, resp. bijective); by composition, one concludes that it is the same for `(17.1.1.1)`.

(iii) One will note that the properties of the morphism `f` defined in `(17.1.1)` are properties of the representable
functor `(0_III, 8.1.8)`

```text
  Y' ↦ Hom_Y(Y', X)
```

from the category of `Y`-preschemes to the category of sets; they retain a meaning for any contravariant functor having
the same source and target categories, representable or not.

(iv) Suppose that the morphism `f` is formally unramified (resp. formally étale); consider an arbitrary `Y`-prescheme
`Z` and a closed sub-prescheme `Z_0` of `Z` defined by a locally nilpotent Ideal `𝓙` of `𝒪_Z`. Then the map

```text
  (17.1.2.1)    Hom_Y(Z, X) → Hom_Y(Z_0, X)
```

deduced from the canonical injection `Z_0 → Z`, is still injective (resp. bijective). Indeed, let `(U_α)` be an affine
open cover of `Z` such that the Ideals `𝓙 | U_α` are nilpotent, and for each `α`, let `U_{α,0}` be the inverse image of
`U_α` in `Z_0`, which is the closed sub-prescheme of `U_α` defined by `𝓙 | U_α`. Let `f_0 : Z_0 → X` be a `Y`-morphism;
by hypothesis, for each `α`, there is at most one (resp. one and only one) `Y`-morphism `f_α : U_α → X` whose
restriction to `U_{α,0}` is equal to `f_0 | U_{α,0}`. One concludes at once that if `f_α` and `f_β` are defined, then,
for every affine open `V ⊂ U_α ∩ U_β`, one has `f_α | V = f_β | V`, since the restrictions of these morphisms to the
inverse image `V_0` of `V` in `Z_0` coincide. Hence there is at most one (resp. one and only one) `Y`-morphism
`f : Z → X` whose restriction to `Z_0` coincides with `f_0`.

**Proposition (17.1.3).**

<!-- label: IV.17.1.3 -->

*(i) A monomorphism of preschemes is formally unramified; an open immersion is formally étale.*

*(ii) The composite of two formally smooth (resp. formally unramified, resp. formally étale) morphisms is formally
smooth (resp. formally unramified, resp. formally étale).*

*(iii) If `f : X → Y` is a formally smooth (resp. formally unramified, resp. formally étale) `S`-morphism, then so is
`f_{(S')} : X_{(S')} → Y_{(S')}` for every extension `S' → S` of the base prescheme.*

*(iv) If `f : X → X'` and `g : Y → Y'` are two formally smooth (resp. formally unramified, resp. formally étale)
`S`-morphisms, then so is `f ×_S g : X ×_S Y → X' ×_S Y'`.*

*(v) Let `f : X → Y`, `g : Y → Z` be two morphisms; if `g ∘ f` is formally unramified, then so is `f`.*

*(vi) If `f : X → Y` is a formally unramified morphism, then so is `f_red : X_red → Y_red`.*

By virtue of `(I, 5.5.12)`, it suffices to prove (i), (ii), and (iii). The two assertions of (i) are trivial. To prove
(ii), consider two morphisms `f : X → Y`, `g : Y → Z`, an affine scheme `Z'`, a closed subscheme `Z'_0` of `Z'` defined
by a nilpotent Ideal, and a morphism `Z' → Z`. Suppose `f` and `g` are formally smooth, and consider a `Z`-morphism

<!-- original page 58 -->

`u_0 : Z'_0 → X`; the hypothesis on `g` implies that there exists a `Z`-morphism `v : Z' → Y` such that
`f ∘ u_0 = v ∘ j` (where `j : Z'_0 → Z'` is the canonical injection); the hypothesis on `f` then implies that there
exists a morphism `u : Z' → X` such that `f ∘ u = v` and `u ∘ j = u_0`, hence `(g ∘ f) ∘ u` is equal to the given
morphism `Z' → Z` and `u ∘ j = u_0`, which proves that `g ∘ f` is formally smooth; one reasons similarly when one
supposes `f` and `g` formally unramified.

Finally, to prove (iii), set `X' = X_{(S')}`, `Y' = Y_{(S')}`, `f' = f_{(S')}`; consider an affine scheme `Y''`, a
closed subscheme `Y''_0` of `Y''` defined by a nilpotent Ideal, and a morphism `q : Y'' → Y'` making `Y''` into a
`Y'`-prescheme; one knows then `(I, 3.3.8)` that `Hom_{Y'}(Y'', X')` canonically identifies with `Hom_Y(Y'', X)` and
`Hom_{Y'}(Y''_0, X')` with `Hom_Y(Y''_0, X)`, and the conclusion then results immediately from definition `(17.1.1)`.

One will note that a closed immersion is not necessarily a formally smooth morphism.

**Proposition (17.1.4).**

<!-- label: IV.17.1.4 -->

*Let `f : X → Y`, `g : Y → Z` be two morphisms, and suppose `g` formally unramified. Then, if `g ∘ f` is formally smooth
(resp. formally étale), so is `f`.*

Indeed, let `Y'` be an affine scheme, `Y'_0` a closed subscheme of `Y'` defined by a nilpotent Ideal, `h : Y' → Y` a
morphism, `j : Y'_0 → Y'` the canonical injection, `u_0 : Y'_0 → X` a `Y`-morphism, hence such that `f ∘ u_0 = h ∘ j`.
Suppose `g ∘ f` formally smooth; then there exists a morphism `u : Y' → X` such that `u ∘ j = u_0` and
`(g ∘ f) ∘ u = g ∘ h`. But these relations imply that `f ∘ u` and `h` are two `Z`-morphisms from `Y'` to `Y` such that
`(f ∘ u) ∘ j = h ∘ j`; by virtue of the hypothesis that `g` is formally unramified, one deduces that `f ∘ u = h`, in
other words `u` is a `Y`-morphism; hence `f` is formally smooth. Taking `(17.1.3, (v))` into account, this proves the
proposition.

**Corollary (17.1.5).**

<!-- label: IV.17.1.5 -->

*Suppose `g` formally étale; then, for `g ∘ f` to be formally smooth (resp. formally unramified, resp. formally étale),
it is necessary and sufficient that `f` be so.*

This results from `(17.1.4)` and `(17.1.3, (ii) and (v))`.

**Proposition (17.1.6).**

<!-- label: IV.17.1.6 -->

*Let `f : X → Y` be a morphism of preschemes.*

*(i) Let `(U_α)` be an open cover of `X` and, for each `α`, let `i_α : U_α → X` be the canonical injection. For `f` to
be formally smooth (resp. formally unramified, resp. formally étale), it is necessary and sufficient that each of the
morphisms `f ∘ i_α` be so.*

*(ii) Let `(V_λ)` be an open cover of `Y`. For `f` to be formally smooth (resp. formally unramified, resp. formally
étale), it is necessary and sufficient that each of the restrictions `f^{-1}(V_λ) → V_λ` of `f` be so.*

We first note that (ii) is a consequence of (i): indeed, if `j_λ : V_λ → Y` and `i_λ : f^{-1}(V_λ) → X` are the
canonical injections, the restriction `f_λ : f^{-1}(V_λ) → V_λ` of `f` is such that `j_λ ∘ f_λ = f ∘ i_λ`; if `f` is
formally smooth (resp. formally unramified), so is `f ∘ i_λ` since `i_λ` is formally étale `(17.1.3)`; but since `j_λ`
is formally étale, this implies that `f_λ` is formally smooth (resp. formally unramified) by virtue of `(17.1.5)`.
Conversely, if all the `f_λ` are formally smooth (resp. formally unramified), so are the `j_λ ∘ f_λ` `(17.1.3)`, hence
also `f` by virtue of (i).

<!-- original page 59 -->

If one takes into account the fact that the `i_α` are formally étale, everything reduces to proving that if the
`f ∘ i_α` are formally smooth (resp. formally unramified), then so is `f`.

Let then `Y'` be an affine scheme, `Y'_0` a closed subscheme of `Y'` defined by a nilpotent Ideal `𝓙`, which one may
suppose such that `𝓙² = 0` `(17.1.2, (ii))`, and finally let `q : Y' → Y` be a morphism. Suppose given a `Y`-morphism
`u_0 : Y'_0 → X`; designate by `W'_α` (resp. `W'_{α,0}`) the prescheme induced by `Y'` (resp. `Y'_0`) on the open
`u_0^{-1}(U_α)` (recall that `Y'` and `Y'_0` have the same underlying topological space). Suppose first that the
`f ∘ i_α` are formally unramified, and let us show that, if `u'` and `u''` are two `Y`-morphisms from `Y'` to `X` whose
restrictions to `Y'_0` coincide, then `u' = u''`. Indeed, taking `(17.1.2, (iv))` into account, the hypothesis that the
`f ∘ i_α` are unramified implies that for each `α`, one has `u' | W'_α = u'' | W'_α`, since the restrictions of these
two `Y`-morphisms to `W'_{α,0}` coincide. Whence the conclusion in this case.

Suppose now all the `f ∘ i_α` formally smooth and let us prove that there exists a `Y`-morphism `u : Y' → X` of which
`u_0` is the restriction to `Y'_0`. Now, since `Y'` is an affine scheme, one can apply `(16.5.17)`, whose hypotheses are
satisfied, and whose conclusion proves precisely the existence of `u`.

One can therefore say that the notions introduced in `(17.1.1)` are local on `X` and on `Y`, which always allows one, by
virtue of `(17.1.2, (i))`, to reduce to the study of formally smooth (resp. formally unramified, resp. formally étale)
algebras.

### 17.2. General differential properties

**Proposition (17.2.1).**

<!-- label: IV.17.2.1 -->

*For a morphism `f : X → Y` to be formally unramified, it is necessary and sufficient that `Ω^1_{X/Y} = 0` (which is
also written `Ω_{X/Y} = 0` `(16.3.1)`).*

Taking `(17.1.6)` into account, one is reduced to the case where `Y = Spec(A)` and `X = Spec(B)` are affine, and the
conclusion then results from `(0, 20.7.4)` and the interpretation of `Ω_{X/Y}` in this case `(16.3.7)`.

**Corollary (17.2.2).**

<!-- label: IV.17.2.2 -->

*Let `f : X → Y`, `g : Y → Z` be two morphisms. For `f` to be formally unramified, it is necessary and sufficient that
the canonical homomorphism `(16.4.19)`*

```text
  f*(Ω^1_{Y/Z}) → Ω^1_{X/Z}
```

*be surjective.*

This is an immediate consequence of `(17.2.1)` and of the exact sequence `(16.4.19.1)`.

**Proposition (17.2.3).**

<!-- label: IV.17.2.3 -->

*Let `f : X → Y` be a formally smooth morphism.*

*(i) The `𝒪_X`-Module `Ω^1_{X/Y}` is locally projective `(16.10.1)`. If `f` is locally of finite type, `Ω^1_{X/Y}` is
locally free of finite type.*

*(ii) For every morphism `g : Y → Z`, the sequence `(16.4.19)` of `𝒪_X`-Modules*

```text
  (17.2.3.1)    0 → f*(Ω^1_{Y/Z}) → Ω^1_{X/Z} → Ω^1_{X/Y} → 0
```

*is exact; moreover, for every `x ∈ X`, there exists an open neighbourhood `U` of `x` such that the restrictions to `U`
of the homomorphisms of `(17.2.3.1)` form an exact and split sequence.*

<!-- original page 60 -->

(i) One knows `(16.3.9)` that if `f` is locally of finite type, `Ω^1_{X/Y}` is an `𝒪_X`-Module of finite type. To prove
that, in every case, it is locally projective, one can restrict, by virtue of `(17.1.6)`, to the case where
`Y = Spec(A)` and `X = Spec(B)` are affine, and this results from the hypothesis on `f` and from
`(0, 20.4.9 and 0, 19.2.1)`.

(ii) Here again, one can restrict to the case where `X`, `Y`, and `Z` are affine `(17.1.6)`, and the conclusion results
in this case from the interpretation of the Modules figuring in the sequence `(17.2.3.1)` and from `(0, 20.5.7)`.

**Corollary (17.2.4).**

<!-- label: IV.17.2.4 -->

*If `f : X → Y` is a formally étale morphism, then, for every morphism `g : Y → Z`, the canonical homomorphism of
`𝒪_X`-Modules*

```text
  f*(Ω^1_{Y/Z}) → Ω^1_{X/Z}
```

*is bijective.*

This results from the exactness of the sequence `(17.2.3.1)` and from the fact that one then has `Ω^1_{X/Y} = 0`
`(17.2.1)`.

**Proposition (17.2.5).**

<!-- label: IV.17.2.5 -->

*Let `f : X → Y` be a morphism, `X'` a sub-prescheme of `X` such that the composite morphism `X' →^j X →^f Y` (where `j`
is the canonical injection) is formally smooth. Then the sequence of `𝒪_{X'}`-Modules `(16.4.21)`*

```text
  (17.2.5.1)    0 → 𝒩_{X'/X} → Ω^1_{X/Y} ⊗ 𝒪_{X'} → Ω^1_{X'/Y} → 0
```

*is exact; moreover, for every `x ∈ X'`, there exists an open neighbourhood `U` of `x` such that the restrictions to `U`
of the homomorphisms of `(17.2.5.1)` form an exact and split sequence.*

Still by virtue of `(17.1.6)`, one can restrict to the case where `Y = Spec(A)` and `X = Spec(B)` are affine, and
`X' = Spec(B/𝔧)`, where `𝔧` is an ideal of `B`. Then the conormal sheaf `𝒩_{X'/X}` corresponds to the `B`-module `𝔧/𝔧²`
`(16.1.3)`, and the conclusion follows from `(0, 20.5.14)`.

**Proposition (17.2.6).**

<!-- label: IV.17.2.6 -->

*Let `X`, `Y` be two preschemes, `f : X → Y` a morphism locally of finite type. The following conditions are
equivalent:*

*a) `f` is a monomorphism.*

*b) `f` is radicial and formally unramified.*

*c) For every `y ∈ Y`, the fibre `f^{-1}(y)` is empty or `k(y)`-isomorphic to `Spec(k(y))` (in other words, is reduced
to a single point `x` such that `k(y) → 𝒪_{X, x}/𝔪_y 𝒪_{X, x}` is an isomorphism).*

The fact that a) implies c) results from `(8.11.5.1)`. It is clear that c) implies that `f` is radicial; let us show
that it also follows from c) that `Ω^1_{X/Y} = 0`, which will prove that c) implies b) `(17.2.1)`. Note that the
`𝒪_X`-Module `Ω^1_{X/Y}` is quasi-coherent of finite type `(16.3.9)`. It therefore results from `(I, 9.1.13.1)` that,
for `(Ω^1_{X/Y})_x = 0`, it is necessary and sufficient that if one puts `Y_1 = Spec(k(y))`,
`X_1 = f^{-1}(y) = X ×_Y Y_1`, one has `(Ω^1_{X_1/Y_1})_x = 0`; but since the morphism `f_1 : X_1 → Y_1` deduced from
`f` is formally unramified by virtue of hypothesis c) `(17.1.3)`, the conclusion results from `(17.2.1)`. Let us prove
finally that b) implies a); for this, consider the diagonal morphism `g = Δ_f : X → X ×_Y X`; since `f` is radicial, `g`
is surjective `(I, 8.7.1)`; on the other hand, `Ω^1_{X/Y}` is by definition the conormal sheaf `𝒩(g)` of the immersion
`g` `(16.3.1)`, and to say that `f` is formally unramified therefore signifies that

<!-- original page 61 -->

`𝒩(g) = 0` `(17.2.1)`. Moreover, `g` is locally of finite presentation `(1.4.3.1)`; hence the hypothesis `𝒩(g) = 0`
implies that `g` is an open immersion `(16.1.10)`; being surjective, this immersion is an isomorphism, hence `f` is a
monomorphism `(I, 5.3.8)`.

### 17.3. Smooth, unramified, étale morphisms

**Definition (17.3.1).**

<!-- label: IV.17.3.1 -->

*One says that a morphism `f : X → Y` is **smooth** (resp. **unramified**, or **net**[^17.3.1.note], resp. **étale**) if
it is locally of finite presentation and formally smooth (resp. formally unramified, resp. formally étale).*

*One also says in that case that `X` is **smooth** (resp. **unramified** or **net**, resp. **étale**) over `Y`.*

We shall see further on `(17.5.2)` that this definition of a smooth morphism coincides with the one already given in
`(6.8.1)`; until then, it is the definition of `(17.3.1)` that we shall use exclusively.

It is clear that to say that `f` is étale signifies that it is at once smooth and unramified.

**Remarks (17.3.2).** — (i) One will note that definition `(17.3.1)` can be expressed solely by means of the functor

```text
  Y' ↦ Hom_Y(Y', X)
```

considered in `(17.1.2, (iii))`, since to say that `f` is locally of finite presentation amounts to saying that the
preceding functor commutes with projective limits of affine schemes `(8.14.2)`.

(ii) Let `A` be a ring, `B` an `A`-algebra. One says that `B` is a **smooth** (resp. **unramified**, resp. **étale**)
`A`-algebra if the corresponding morphism `Spec(B) → Spec(A)` is smooth (resp. unramified, resp. étale). It amounts to
the same to say that `B` is an `A`-algebra of finite presentation `(1.4.6)` and formally smooth (resp. formally
unramified, resp. formally étale) for the discrete topologies.

(iii) It results from `(17.1.6)` and from the definition of a morphism locally of finite presentation `(1.4.2)` that the
notions of smooth, unramified, and étale morphism are local on `X` and on `Y`.

**Proposition (17.3.3).**

<!-- label: IV.17.3.3 -->

*(i) An open immersion is étale. For an immersion to be unramified, it is necessary and sufficient that it be locally of
finite presentation.*

*(ii) The composite of two smooth (resp. unramified, resp. étale) morphisms is smooth (resp. unramified, resp. étale).*

*(iii) If `f : X → Y` is a smooth (resp. unramified, resp. étale) `S`-morphism, then so is
`f_{(S')} : X_{(S')} → Y_{(S')}` for every extension `S' → S` of the base prescheme.*

*(iv) If `f : X → X'` and `g : Y → Y'` are two smooth (resp. unramified, resp. étale) `S`-morphisms, then so is
`f ×_S g : X ×_S Y → X' ×_S Y'`.*

<!-- original page 62 -->

*(v) Let `f : X → Y`, `g : Y → Z` be two morphisms; if `g` is locally of finite type and `g ∘ f` is unramified, then `f`
is unramified.*

This results immediately from `(1.4.3)` and `(17.1.3)`.

**Proposition (17.3.4).**

<!-- label: IV.17.3.4 -->

*Let `f : X → Y`, `g : Y → Z` be two morphisms, and suppose `g` unramified. Then, if `g ∘ f` is smooth (resp.
unramified, resp. étale), so is `f`.*

Indeed, since `g` and `g ∘ f` are locally of finite presentation, so is `f` `(1.4.3, (v))`; the conclusion thus results
from `(17.1.4)` and `(17.1.3, (v))`.

**Corollary (17.3.5).**

<!-- label: IV.17.3.5 -->

*Suppose `g` étale; then, for `f` to be smooth (resp. unramified, resp. étale), it is necessary and sufficient that
`g ∘ f` be so.*

This results from `(17.3.4)` and `(17.3.3, (ii))`.

**Proposition (17.3.6).**

<!-- label: IV.17.3.6 -->

*Let `g : Y → S`, `h : X → S` be two morphisms locally of finite presentation. For an `S`-morphism `f : X → Y` to be
unramified, it is necessary and sufficient that the canonical homomorphism `(16.4.19)`*

```text
  f*(Ω^1_{Y/S}) → Ω^1_{X/S}
```

*be surjective.*

Since `f` is then locally of finite presentation `(1.4.3, (v))`, the proposition results immediately from `(17.2.2)`.

**Definition (17.3.7).**

<!-- label: IV.17.3.7 -->

*Let `f : X → Y` be a morphism. One says that `f` is **smooth** (resp. **unramified**, resp. **étale**) at a point
`x ∈ X` if there exists an open neighbourhood `U` of `x` in `X` such that the restriction `f | U` is a smooth (resp.
unramified, resp. étale) morphism from `U` to `Y`.*

*One also says in that case that `X` is **smooth** (resp. **unramified**, resp. **étale**) over `Y` at the point `x`.*

Taking the remark `(17.3.2, (iii))` into account, it amounts to the same to say that `f` is a smooth (resp. unramified,
resp. étale) morphism or that it is smooth (resp. unramified, resp. étale) at every point of `X`.

It is clear that the set of points of `X` where a morphism `f : X → Y` is smooth (resp. unramified, resp. étale) is open
in `X`.

**Proposition (17.3.8).**

<!-- label: IV.17.3.8 -->

*For every prescheme `Y` and every locally free `𝒪_Y`-Module `ℰ` of finite type, the vector-bundle prescheme `𝐕(ℰ)`
`(II, 1.7.8)` is a smooth `Y`-prescheme.*

Indeed `(17.3.2, (iii))`, one can restrict to the case where `Y = Spec(A)` is affine and `𝐕(ℰ) = Spec(A[T_1, …, T_r])`;
since `A[T_1, …, T_r]` is an `A`-algebra formally smooth for the discrete topologies `(0, 19.3.2)` and of finite
presentation, this proves the proposition `(17.3.2, (ii))`.

**Corollary (17.3.9).**

<!-- label: IV.17.3.9 -->

*Under the hypotheses of `(17.3.8)`, the projective-bundle prescheme `𝐏(ℰ)` `(II, 4.1.1)` is a smooth `Y`-prescheme.*

One can again restrict to the case where `Y = Spec(A)` is affine and `𝐏(ℰ) = 𝐏^r_A`. One knows then `(II, 2.3.14)` that
one has a finite open cover of `𝐏^r_A` by taking the `D_+(T_i)` `(0 ⩽ i ⩽ r)`, equal respectively to the spectra of the
rings `S_{(T_i)}`, where one replaces `S` by `A[T_0, T_1, …, T_r]` and `f` by `T_i`; but it follows at once from the
definition of `S_{(f)}` `(II, 2.2.1)` that this ring, in the case considered, is isomorphic to
`A[T_0, …, T_{i−1}, T_{i+1}, …, T_r]`; hence the corollary results from `(17.3.8)`.

<!-- original page 63 -->

### 17.4. Characterizations of unramified morphisms

**Theorem (17.4.1).**

<!-- label: IV.17.4.1 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `x` a point of `X`. The following properties are
equivalent:*

*a) `f` is unramified at the point `x`.*

*b) The diagonal morphism `Δ_f : X → X ×_Y X` is a local isomorphism at the point `x`.*

*b') If one sets `Δ_f = (𝟏_X, θ)`, `Z = X ×_Y X` and `z = Δ_f(x)`, the homomorphism `θ_x : 𝒪_{Z, z} → 𝒪_{X, x}` is
bijective.*

*b'') For every morphism `g : Y' → Y`, and every point `y' ∈ Y'` over `y = f(x)`, every `Y'`-section `s'` of
`X' = X ×_Y Y'` such that `x' = s'(y')` lies over `x` is a local isomorphism at the point `y'`.*

*c) One has `(Ω^1_{X/Y})_x = 0`.*

*d) The `k(y)`-prescheme `f^{-1}(y)` is unramified over `k(y)` at the point `x`.*

*d') The point `x` is isolated in `X_y = f^{-1}(y)` (in other words `(Err_{III}, 20)`, the morphism `f` is quasi-finite
at the point `x`) and the ring `𝒪_{X_y, x}` is a field, separable extension of `k(y)`.*

*d'') The ring `𝒪_{X_y, x} = 𝒪_{X, x}/𝔪_y 𝒪_{X, x}` is a field, finite separable extension of `k(y)`.*

*e) The ring `𝒪_{X, x}` is an `𝒪_{Y, y}`-algebra formally unramified for the discrete topologies.*

Since `f` is locally of finite type, the `𝒪_X`-Module `Ω^1_{X/Y}` is of finite type `(16.3.9)`, so it amounts to the
same to say that `(Ω^1_{X/Y})_x = 0` or that there exists an open neighbourhood `U` of `x` such that
`Ω^1_{X/Y} | U = 0`. Taking `(17.2.1)` into account, this proves the equivalence of a) and c). On the other hand, if one
sets `A = 𝒪_{Y, y}`, `B = 𝒪_{X, x}`, one has `(Ω^1_{X/Y})_x = Ω^1_{B/A}` `(16.4.5)`, and the equivalence of c) and e)
therefore results from `(0, 20.7.4)`.

Since d') involves only properties of the morphism `X_y → Spec(k(y))`, the equivalence of a) and d') will ipso facto
imply that of d) and d'). On the other hand d') and d'') are equivalent, since it amounts to the same to say that
`𝒪_{X_y, x}` is a finite `k(y)`-algebra or that `x` is an isolated point of `X_y`, since `X_y` is a `k(y)`-prescheme
locally of finite type `(I, 6.4.4)`.

Let us now prove the equivalence of b) and b'). One can limit oneself to the case where `Y = Spec(R)` and `X = Spec(S)`
are affine and `f` of finite presentation; then one has `Z = Spec(S ⊗_R S)` and `Δ_f` corresponds to the canonical
surjective homomorphism `S ⊗_R S → S`, whose kernel `𝔧` is known to be an ideal of finite type `(0, 20.4.4)`. If one
sets `𝓘 = 𝔧̃`, the `𝒪_Z`-Module `𝒪_X = 𝒪_Z/𝓘` is thus of finite presentation, and the hypothesis that the homomorphism
`θ_x : 𝒪_{Z, z} → (𝒪_X)_z` is bijective implies that, replacing `X` if needed by an open neighbourhood of `x`, the
homomorphism `θ : 𝒪_Z → j_*(𝒪_X)` is itself bijective `(0_I, 5.2.7)`. This therefore shows that b') implies b); the
converse is evident.

On the other hand, the equivalence of b) and b'') results from `(I, 5.3.7)` without any finiteness hypothesis on `f`:
the datum of a `Y'`-section `s' : Y' → X'` is equivalent to that of a

<!-- original page 64 -->

`Y`-morphism `h = g' ∘ s' : Y' → X` (where `g' : X' → X` is the canonical projection), so that `s' = (𝟏_{Y'}, h)_X`, and
then the diagram

```text
  (17.4.1.1)
                       Y' ──s'──→ X' ──→ Y' ×_Y X
                       │                    │
                       h                  𝟏_{Y'} × Δ_f
                       ↓                    ↓
                       X ──────Δ_f─────→ X ×_Y X
```

identifies `Y'` with the product of the `(X ×_Y X)`-preschemes `X` and `X'`. Consequently `(I, 4.3.2)`, if `Δ_f` is a
local isomorphism at the point `x`, `s'` is a local isomorphism at the point `y'` (since `x = h(y')`), which proves that
b) implies b''). The converse is obtained by applying b'') to the case where one takes `Y' = X`, `y' = x`, `g = f`, and
`s' = Δ_f`.

To complete the proof of `(17.4.1)`, it suffices to prove the implications

```text
  d'') ⇒ c) ⇒ b) ⇒ d'').
```

d'') ⇒ c): Since `Ω^1_{X/Y}` is an `𝒪_X`-Module of finite type, it results from Nakayama's lemma that the condition c)
is equivalent to `(Ω^1_{X/Y})_x ⊗_{𝒪_{X, x}} k(x) = 0`, that is `(16.4.5)`, `(Ω^1_{X_y/Spec(k(y))})_x = 0`. One is
therefore reduced to the case where `Y` is the spectrum of a field `k` and `X` a `k`-algebraic prescheme. The hypothesis
that `𝒪_{X, x}` is a field `k'`, finite extension of `k`, implies first that `x` is closed in `X` `(I, 6.4.2)`, then
that `x` is a maximal point of the Noetherian prescheme `X`, hence is an isolated point of `X`. Replacing `X` by the
open set `{x}` of `X`, one can therefore suppose that `X = Spec(k')`; but then the hypothesis that `k'` is a finite
separable extension of `k` implies `Ω^1_{k'/k} = 0` `(0, 20.6.20)`, which proves c).

c) ⇒ b): One has seen above that one then has `Ω^1_{X/Y} | U = 0` for an open neighbourhood `U` of `x` in `X`; the
assertion b) results then from the definition of `Ω^1_{X/Y}` `(16.3.1)` and from `(16.1.9)`.

b) ⇒ d''): Replacing `X` by an open neighbourhood of `x`, one can suppose that `Δ_f` is an open immersion; if one
designates by `f_y : X_y → Spec(k(y))` the morphism deduced from `f` by base change, `Δ_{f_y}` is then also an open
immersion `(I, 5.3.4)`, and since condition d'') concerns only the prescheme `X_y`, one sees that one can restrict to
the case where `Y` is the spectrum of a field `k`, `X` the spectrum of a `k`-algebra `A` of finite type; property d'')
will be established if one proves that `A` is a finite separable `k`-algebra, such an algebra being a direct composite
of finite separable extensions of `k`. If `K` is an algebraically closed extension of `k`, it amounts to the same to say
that `A ⊗_k K` is a finite separable `K`-algebra `(4.6.1)`, so one sees that one can restrict to the case where `k` is
algebraically closed. Let us first show that `A` is a finite `k`-algebra: it will suffice to show that every closed
point `x` of `X` is isolated, since then the set of these points is open in `X` and discrete, hence finite since it is
quasi-compact (`X` being Noetherian), which will establish our assertion by virtue of `(I, 6.4.4)`. Now, one then has
`k(x) = k` since `k` is algebraically closed `(I, 6.4.3)`, hence there is a `Y`-section `s` of `X` such that
`s(Y) = {x}`, and by virtue of `(17.4.1.1)`, `{x}` is the inverse image of the diagonal `Δ_f(X)` by a morphism
`X → X ×_Y X`, hence `{x}` is open in `X` by virtue of hypothesis b). One has thus shown that `A` is a

<!-- original page 65 -->

finite `k`-algebra, direct composite of finite local `k`-algebras. To express that `Δ_f` is an open immersion, one can
therefore restrict to the case where `A` is a finite local `k`-algebra, `X = Spec(A)` being thus reduced to a single
point; the residue field of `A`, being a finite extension of `k`, is necessarily identical to `k`, and consequently
`(I, 3.4.9)` `X ×_k X` is reduced to a single point and `Δ_f` is therefore necessarily an isomorphism. Now, since `A` is
a `k`-algebra, the canonical homomorphism `A ⊗_k A → A` can be bijective only if `A = k`. Q.E.D.

**Remark (17.4.1.2).** — Suppose only that `f` is locally of finite type. Then `Ω^1_{X/Y}` is still an `𝒪_X`-Module of
finite type `(16.3.9)`, and `Δ_f` a morphism locally of finite presentation `(1.4.3.1)`. The entire proof of `(17.4.1)`
is then valid, provided that one replace a) by: *the restriction of `f` to a suitable neighbourhood of `x` is a formally
unramified morphism*. One sees in addition that in this case the restriction of `f` to a suitable neighbourhood of `x`
is a morphism locally quasi-finite.

**Corollary (17.4.2).**

<!-- label: IV.17.4.2 -->

*Let `f : X → Y` be a morphism locally of finite presentation. The following properties are equivalent:*

*a) `f` is unramified.*

*b) The diagonal morphism `Δ_f : X → X ×_Y X` is an open immersion.*

*b') For every morphism `Y' → Y`, every `Y'`-section of `X' = X ×_Y Y'` is an open immersion.*

*c) One has `Ω^1_{X/Y} = 0`.*

*d) For every `y ∈ Y`, the `k(y)`-prescheme `f^{-1}(y)` is unramified over `k(y)`.*

*d') For every `y ∈ Y`, the `k(y)`-prescheme `f^{-1}(y)` is isomorphic to a prescheme of the form `∐_{λ ∈ L} Spec(K_λ)`,
where, for each `λ ∈ L`, `K_λ` is a finite separable extension of `k(y)`.*

*e) For every `x ∈ X`, the ring `𝒪_{X, x}` is an `𝒪_{Y, f(x)}`-algebra formally unramified for the discrete topologies.*

**Corollary (17.4.3).**

<!-- label: IV.17.4.3 -->

*If `f : X → Y` is unramified, then `f` is locally quasi-finite `(Err_{III}, 20)`.*

**Proposition (17.4.4).**

<!-- label: IV.17.4.4 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`,
`y = f(x)`. Set `A = 𝒪_{Y, y}`, `B = 𝒪_{X, x}`, which are Noetherian local rings, and let `k` be the residue field of
`A`. Then the equivalent conditions a) to e) of theorem `(17.4.1)` are also equivalent to each of the following:*

*f) `B̂ ⊗_Â k` is a field, finite separable extension of `k` (which implies that `B̂` is a finite `Â`-algebra).*

*f') `B` is an `A`-algebra formally unramified for the adic topologies.*

*If moreover `k(x) = k(y)`, or if `k` is separably closed, these conditions are also equivalent to:*

*f'') The homomorphism `Â → B̂` is surjective.*

Let us first note, by the same reasoning as in `(0, 19.3.6)`, that it amounts to the same to say that `B` is an
`A`-algebra formally unramified for the preadic topologies, or that `B̂` is an `Â`-algebra formally unramified for the
adic topologies. On the other hand, the hypothesis that `f` is locally of finite type implies that `Ω^1_{B/A}`

<!-- original page 66 -->

is a `B`-module of finite type `(16.3.9)`, hence separated for the `𝔫`-preadic topology (where `𝔫` is the maximal ideal
of `B`) `(0_I, 7.3.5)`; it amounts to the same to say that `Ω^1_{B/A} = 0` or that `Ω^1_{B̂/Â} = 0`; hence
`(0, 20.7.4)`, it amounts to the same to say that `B` is an `A`-algebra formally unramified for the discrete topologies,
or that `B̂` is an `Â`-algebra formally unramified for the preadic topologies. This proves the equivalence of conditions
e) and f'). If `𝔪` is the maximal ideal of `A`, one has `k = A/𝔪 = Â/𝔪 Â`, so `B̂ ⊗_Â k = B̂/𝔪 B̂ = B̂ ⊗_B (B/𝔪 B)`, and
consequently `(0_I, 7.3.5)` `B̂/𝔪 B̂` is the completion of `B/𝔪 B = B ⊗_A k` for the `𝔫`-preadic topology; this proves
the equivalence of d'') and f). Finally, when `k(x) = k(y)` or when `k` is separably closed, the condition f) implies
that the homomorphism `A/𝔪 A → B/𝔫 B` is bijective; the condition f) implies on the other hand that `B` is a
quasi-finite `Â`-algebra `(0_I, 7.4.4)`, hence finite since `Â` is complete and `B̂` separated for the `𝔫`-preadic
topology, `𝔪 B̂` being an ideal of definition of `B̂` `(0_I, 7.4.1)`. The homomorphism `Â → B̂` is therefore surjective
by virtue of Nakayama's lemma. Hence f) implies f''), and the converse is evident.

**(17.4.5)** Given an `S`-prescheme `Y` and two `S`-morphisms `f : X → Y`, `g : X → Y`, one canonically deduces an
`S`-morphism `(f, g)_S : X → Y ×_S Y`. We shall call **prescheme of coincidences** of `f` and `g` the inverse image by
`(f, g)_S` of the diagonal `Δ_{Y/S}`; it is therefore a sub-prescheme of `X`, which is closed when `Y` is an `S`-scheme
`(I, 5.4.1)`.

**Proposition (17.4.6).**

<!-- label: IV.17.4.6 -->

*Let `h : Y → S` be an unramified morphism and let `f : X → Y`, `g : X → Y` be two `S`-morphisms. Then the prescheme `C`
of coincidences of `f` and `g` is a sub-prescheme induced on an open set of `X`; if moreover `Y` is an `S`-scheme
`(I, 5.4.1)`, `C` is a closed sub-prescheme of `X`.*

Indeed, since `Δ_{Y/S} : Y → Y ×_S Y` is an open immersion `(17.4.2)`, the inverse image by `(f, g)_S` of `Δ_{Y/S}` is a
sub-prescheme induced on an open set of `X` `(I, 4.4.1)`. The last assertion results from `(17.4.5)`.

**Corollary (17.4.7).**

<!-- label: IV.17.4.7 -->

*Under the hypotheses of `(17.4.6)`, let `x` be a point of `X` such that the two composite morphisms
`Spec(k(x)) → X →^f Y` and `Spec(k(x)) → X →^g Y` are equal. Then there exists an open neighbourhood `U` of `x` such
that `f | U = g | U`. If moreover `Y` is an `S`-scheme, there exists an open and closed neighbourhood `X'` of `x` in `X`
such that `f | X' = g | X'`. If finally one supposes in addition that `X` is connected, one has `f = g`.*

This results from `(17.4.6)` and `(I, 5.3.17)`.

**Corollary (17.4.8).**

<!-- label: IV.17.4.8 -->

*Under the hypotheses of `(17.4.6)`, suppose that the structure morphism `φ = h ∘ f = h ∘ g` from `X` to `S` is closed.
Let `s` be a point of `S`; let `X_s` be the `k(s)`-prescheme `φ^{-1}(s)` and suppose that the two composite morphisms
`X_s → X →^f Y` and `X_s → X →^g Y` are equal. Then there exists an open neighbourhood `V` of `s` in `S` such that
`f | φ^{-1}(V) = g | φ^{-1}(V)`. If moreover `Y` is an `S`-scheme and if `φ` is open one can take `V` open and closed.
If finally one supposes in addition `S` connected, one has `f = g`.*

It results from `(17.4.7)` that the prescheme `C` of coincidences of `f` and `g` is induced on an open of `X` and
contains `X_s`. Since `φ` is closed, there exists an open neighbourhood `V` of `s` such that `φ^{-1}(V) ⊂ C`. If
moreover `Y` is an `S`-scheme, `C` is closed, hence `φ(X − C)` is at

<!-- original page 67 -->

once open and closed in `S`, and its complement `V` in `S` is therefore an open and closed neighbourhood of `s` such
that `φ^{-1}(V) ⊂ C`.

**Proposition (17.4.9).**

<!-- label: IV.17.4.9 -->

*Let `Y` be a connected prescheme, `f : X → Y` an unramified and separated morphism. Then every `Y`-section `g` of `X`
is an isomorphism of `Y` onto an open connected component of `X`, and the map `g ↦ g(Y)` is a bijection of `Γ(X/Y)` onto
the set of connected components `Z` of `X` (necessarily open in `X`) such that the restriction of `f` to `Z` be an
isomorphism of `Z` onto `Y`. In particular, if `g'` and `g''` are two `Y`-sections of `X` such that `g'(y) = g''(y)` for
some `y ∈ Y`, one has `g' = g''`.*

It results indeed from `(17.4.1, b''))` that a `Y`-section `s` of `X` is an open immersion, and since `X` is a
`Y`-scheme, `s` is also a closed immersion `(I, 5.4.7)`; it follows that `s` is an isomorphism of `Y` onto a
sub-prescheme of `X` induced on an open and closed part of `X`, and since `s(Y)` is connected, it is necessarily a
connected component of `X`. The rest of the proposition is immediate.

**Remark (17.4.10).** — Taking the remark `(17.4.1.2)` into account, one sees that, in the statements `(17.4.6)` to
`(17.4.9)`, one can everywhere replace the words "unramified" by "formally unramified and locally of finite type".

### 17.5. Characterizations of smooth morphisms

**Theorem (17.5.1).**

<!-- label: IV.17.5.1 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `x` a point of `X`, `y = f(x)`. The following conditions
are equivalent:*

*a) `f` is smooth at the point `x`.*

*b) `f` is flat at the point `x` and the `k(y)`-prescheme `f^{-1}(y)` is smooth over `k(y)` at the point `x`.*

*b') `f` is regular at the point `x` `(6.8.1)`.*

*c) The ring `𝒪_{X, x}` is an `𝒪_{Y, y}`-algebra formally smooth for the discrete topologies.*

One can restrict to the case where `Y = Spec(A)`, `X = Spec(C)`, where `C = B/𝔧`, `B = A[T_1, …, T_n]` being a
polynomial algebra and `𝔧` an ideal of `B` of finite type. The equivalence of a) and c) then results from the
equivalence of a) and c) in `(0, 22.6.4)`. On the other hand, applying this result to the morphism locally of finite
type `f^{-1}(y) → Spec(k(y))`, one sees that the equivalence of b) and b') results from the equivalence of a) and b) in
`(6.8.6)`. It thus remains to prove the equivalence of a) and b).

Let us first show that a) implies b); denote by `𝔭` the prime ideal `𝔧_x` in `C`, `𝔯` the prime ideal `𝔧_y` in `A`; one
has `𝔭 = 𝔮/𝔧`, where `𝔮` is a prime ideal of `B` and `𝔯` is the inverse image of `𝔮` in `A`. The hypothesis a) implies
first that `f^{-1}(y)` is smooth over `k(y)` at the point `x` by `(17.3.3)`, and it is a question of showing moreover
that `C_𝔭 = 𝒪_{X, x}` is a flat `A_𝔯`-module. Since `C_𝔭` is a formally smooth `A_𝔯`-algebra and `B` is a formally
smooth `A`-algebra (for the discrete topologies), the Jacobian criterion `(0, 22.6.4)`, together with `(0, 19.1.12)`,
implies that there exists in `𝔧` a system of `r` polynomials `g_i` `(1 ⩽ i ⩽ r)` and `r` indices `j_i` `(1 ⩽ i ⩽ r)`
such that the images of the `g_i` in `𝔧_𝔮/𝔧_𝔮²` generate this `B_𝔮`-module and that one has

```text
  (17.5.1.1)    det(∂g_i/∂T_{j_k}) ∉ 𝔮.
```

<!-- original page 68 -->

Let us now note that if `g : Spec(B) → Spec(A)` is the structure morphism, the fibre `g^{-1}(y)` is the spectrum of the
regular ring `k(y)[T_1, …, T_n]` `(0, 17.3.7)`, hence the Noetherian local ring `B_𝔮/𝔯 B_𝔮` at a point of this fibre is
regular. Now, condition `(17.5.1.1)` implies that the canonical images `u̅_i` of the `g_i` in the maximal ideal `𝔪` of
`B_𝔮/𝔯 B_𝔮` are linearly independent mod. `𝔪²`: otherwise, there would exist polynomials `w_i ∈ B` `(1 ⩽ i ⩽ r)` not all
belonging to `𝔮` and such that `∑_{i=1}^r w_i g_i ∈ 𝔮²`. Differentiating with respect to the `T_{j_k}`, one would
conclude that `∑ w_i (∂g_i/∂T_{j_k}) ∈ 𝔮` for `1 ⩽ k ⩽ r`, which would contradict `(17.5.1.1)` since `𝔮` is prime. One
concludes therefore from `(0, 17.1.7)` that `(u̅_i)` is a regular sequence in `B_𝔮/𝔯 B_𝔮`. But since the morphism `g` is
locally of finite presentation and `B` is a flat `A`-module, it results from `(11.3.8)` that the canonical images `u'_i`
of the `g_i` in `B_𝔮` also form a regular sequence and that `B_𝔮/(∑ u'_i B_𝔮)` is a flat `A_𝔯`-module. Since the images
of the `u'_i` in `𝔧_𝔮/𝔧_𝔮²` generate this `B_𝔮`-module, it results from Nakayama's lemma that one has
`∑ u'_i B_𝔮 = 𝔧_𝔮`, and `C_𝔭 = B_𝔮/𝔧_𝔮` is therefore indeed a flat `A_𝔯`-module.

Let us finally prove that b) implies a). With the same notation, the hypothesis that `B_𝔮/𝔧_𝔮` is a flat `A_𝔯`-module
implies that the canonical homomorphism `𝔧_𝔮/𝔯 𝔧_𝔮 → B_𝔮/𝔯 B_𝔮` is injective `(0_I, 6.1.2)`, so that `𝔧_𝔮/𝔯 𝔧_𝔮` is
identified with an ideal of `B_𝔮/𝔯 B_𝔮`. Since `B_𝔮/𝔯 B_𝔮` is an `A_𝔯`-algebra formally smooth for the discrete
topologies, one can apply, to `C_𝔭 = (B_𝔮/𝔯 B_𝔮)/(𝔧_𝔮/𝔯 𝔧_𝔮)`, the Jacobian criterion `(0, 22.6.4)`; together with
`(0, 19.1.12)`, the latter proves, by virtue of hypothesis b), the existence of `r` polynomials
`v_i ∈ k(y)[T_1, …, T_n]` such that their images in `(𝔧_𝔮/𝔯 𝔧_𝔮)/(𝔧_𝔮/𝔯 𝔧_𝔮)²` generate this `(B_𝔮/𝔯 B_𝔮)`-module and
that one has

```text
  (17.5.1.2)    det(∂v_i/∂T_{j_k}) ∉ 𝔮 B_𝔮/𝔯 B_𝔮.
```

If, for each `i`, one then designates by `g_i` an element of `𝔧` whose `v_i` is the canonical image, it follows from
`(17.5.1.2)` that the `g_i` verify condition `(17.5.1.1)`; on the other hand, by virtue of Nakayama's lemma, the images
`u'_i` of the `g_i` in `𝔧_𝔮` generate this `B_𝔮`-module. The Jacobian criterion `(0, 22.6.4)` together with
`(0, 19.1.12)` then proves that `C_𝔭 = B_𝔮/𝔧_𝔮` is an `A_𝔯`-algebra formally smooth for the discrete topologies. Q.E.D.

**Corollary (17.5.2).**

<!-- label: IV.17.5.2 -->

*Let `f : X → Y` be a morphism locally of finite presentation. For `f` to be smooth (in the sense of `(17.3.1)`), it is
necessary and sufficient that `f` be regular `(6.8.1)`, in other words that `f` be flat and that for every `y ∈ Y`,
`f^{-1}(y)` be a geometrically regular `k(y)`-prescheme `(6.7.6)`.*

One has thus established the equivalence of the two definitions of "smooth morphism" given in `(6.8.1)` and `(17.3.1)`.

**Proposition (17.5.3).**

<!-- label: IV.17.5.3 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`,
`y = f(x)`. Set `A = 𝒪_{Y, y}`, `B = 𝒪_{X, x}`, which are Noetherian local rings. Then the equivalent conditions a) to
c) of `(17.5.1)` are also equivalent to each of the following:*

<!-- original page 69 -->

*d) `B` is an `A`-algebra formally smooth for the preadic topologies.*

*d') `B̂` is an `Â`-algebra formally smooth for the adic topologies.*

*If moreover `k(x) = k(y)`, these conditions are also equivalent to:*

*d'') `B̂` is an `Â`-algebra isomorphic to a formal power series algebra `Â[[T_1, …, T_n]]`.*

The equivalence of condition c) of `(17.5.1)` and d) results from the equivalence of a) and d) in the Jacobian criterion
`(0, 22.6.4)`, and the equivalence of d) and d') results from `(0, 19.3.6)`. On the other hand, d'') implies d') without
any hypothesis on the residue fields `(0, 19.3.4)`. Finally, if `𝔪` designates the maximal ideal of `Â`, the hypothesis
d') implies that `B̂/𝔪 B̂` is a complete Noetherian local `k(y)`-algebra, formally smooth for its adic topology
`(0, 19.3.5)`; the hypothesis `k(y) = k(x)` then implies that `B̂/𝔪 B̂` is `k(y)`-isomorphic to a formal power series
algebra `k(y)[[T_1, …, T_n]]` `(0, 19.6.4)`. Since on the other hand, `Â[[T_1, …, T_n]]` is a flat `Â`-module and a
complete Noetherian local `Â`-algebra, one concludes from `(0, 19.7.1.5)` that this algebra is isomorphic to `B̂`. Hence
d') implies d'') under the additional hypothesis `k(x) = k(y)`.

**Remark (17.5.4).** — Suppose that `Y` is a locally Noetherian prescheme, and `f : X → Y` a morphism locally of finite
type. The criterion `(17.5.3, d)`, together with `(0, 22.1.4)`, shows that to prove that `f` is smooth, one can apply
definition `(17.1.1)`, restricting to the case where the affine scheme `Y'` is the spectrum of an Artinian local ring.

**Proposition (17.5.5).**

<!-- label: IV.17.5.5 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`,
`y = f(x)`. Suppose that `Y` is reduced at the point `y`. Then, for `f` to be smooth at the point `x`, it is necessary
and sufficient that `f` be universally open in a neighbourhood of `x` in `f^{-1}(y)` and that `f^{-1}(y)` be a
geometrically regular `k(y)`-prescheme at the point `x`.*

Taking `(17.5.1)` into account, everything reduces to seeing that, if `f^{-1}(y)` is a geometrically regular
`k(y)`-prescheme at the point `x`, it is equivalent to say that `f` is flat at the point `x` or universally open in a
neighbourhood of `x` in `f^{-1}(y)`. Now, if `f` is flat at the point `x`, it is so in a neighbourhood of `x` in `X`
`(11.1.1)` and consequently universally open in this neighbourhood `(2.4.6)`. Conversely, the hypothesis that `f` is
universally open in a neighbourhood of `x` in `f^{-1}(y)` and that `f^{-1}(y)` is a geometrically regular
`k(y)`-prescheme at the point `x` implies that `f` is flat at the point `x`, since `𝒪_{Y, y}` is reduced `(15.2.2)`.

**Corollary (17.5.6).**

<!-- label: IV.17.5.6 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`,
`y = f(x)`. Suppose that `Y` is reduced and geometrically unibranch `(6.15.1)` at the point `y`. Then, for `f` to be
smooth at the point `x`, it is necessary and sufficient that `f` be equidimensional at the point `x` and that
`f^{-1}(y)` be a geometrically regular `k(y)`-prescheme at the point `x`.*

Noting that the set of points where `f` is equidimensional is open `(13.3.2)`, one sees that the corollary results from
`(17.5.5)` and from Chevalley's criterion `(14.4.4)`.

The fact that `f` is a smooth morphism at a point implies in particular that `f` verifies at this point

<!-- original page 70 -->

all the properties defined in `(6.8.1)`. One has therefore the following properties, which we recall for the convenience
of references:

**Proposition (17.5.7).**

<!-- label: IV.17.5.7 -->

*Let `f : X → Y` be a morphism locally of finite presentation, smooth at a point `x ∈ X`; set `y = f(x)`. Then, for the
ring `𝒪_{X, x}` to be reduced (resp. integrally closed, resp. geometrically unibranch), it is necessary and sufficient
that `𝒪_{Y, y}` be so.*

This has indeed been proved in `(11.3.13)` and `(11.3.14)`, completed by `Err_{IV}, 30`.

**Proposition (17.5.8).**

<!-- label: IV.17.5.8 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, smooth at a point `x ∈ X`;
set `y = f(x)`. Then:*

*(i) One has `dim(𝒪_{X, x}) = dim(𝒪_{Y, y}) + dim(𝒪_{X, x} ⊗_{𝒪_{Y, y}} k(y))`.*

*(ii) One has `coprof(𝒪_{X, x}) = coprof(𝒪_{Y, y})`.*

*(iii) For the ring `𝒪_{X, x}` to possess property `(S_n)` `(5.7.2)` (resp. `(R_n)` `(5.8.2)`), it is necessary and
sufficient that the ring `𝒪_{Y, y}` possess it. In particular, for `𝒪_{X, x}` to be regular, it is necessary and
sufficient that `𝒪_{Y, y}` be so.*

These are particular cases of `(6.1.2)`, `(6.3.2)`, `(6.4.1)`, and `(6.5.3)`.

### 17.6. Characterizations of étale morphisms

**Theorem (17.6.1).**

<!-- label: IV.17.6.1 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `x` a point of `X`, `y = f(x)`. The following conditions
are equivalent:*

*a) `f` is étale at the point `x`.*

*a') `f` is smooth at the point `x` and unramified at the point `x`.*

*b) `f` is smooth at the point `x` and quasi-finite at the point `x` `(Err_{III}, 20)`.*

*c) `f` is flat at the point `x` and unramified at the point `x`.*

*c') `f` is flat at the point `x` and the ring `𝒪_{X, x}/𝔪_y 𝒪_{X, x}` is a field, finite separable extension of
`k(y)`.*

*d) The ring `𝒪_{X, x}` is an `𝒪_{Y, y}`-algebra formally étale for the discrete topologies.*

The equivalence of a) and a') results at once from the definitions; that of a) and d) results from the equivalence of a)
and e) in `(17.4.1)` and of the equivalence of a) and c) in `(17.5.1)`. The equivalence of c) and c') results from the
equivalence of a) and d'') in `(17.4.1)`. The fact that a') implies c') follows from `(17.5.1)`; conversely, if c') is
verified, `f` is regular (hence smooth by `(17.5.1)`) at the point `x`, since if `K` is a finite separable extension of
a field `k`, then, for every extension `k'` of `k`, `Spec(K ⊗_k k')` is regular, being the sum of a finite number of
spectra of fields. The fact that a') implies b) results from `(17.4.1, d')` and `(17.5.1, b)`. It remains therefore to
see that b) implies c), and since one already knows that `f` is flat at the point `x` by `(17.5.1)`, it suffices to show
that `f^{-1}(y)` is a `k(y)`-prescheme unramified over `k(y)`; in other words, one is reduced to proving that b) implies
c) when `Y = Spec(k)` is the spectrum of a field `k`. Since the question is local on `X`, one can restrict to the case
where `X = Spec(A)`, where `A` is a finite local `k`-algebra `(0_I, 7.4.1)`. By virtue of hypothesis b), `A` is a
`k`-algebra formally smooth for the discrete topologies, which coincide here with the preadic topologies; hence
`(0, 19.6.5)`, `A` is a regular local ring, hence

<!-- original page 71 -->

a field since it is Artinian, and it then results from `(0, 19.6.5.1)` that `A` must be a finite separable extension of
`k`, which completes the proof `(17.4.1)`.

**Corollary (17.6.2).**

<!-- label: IV.17.6.2 -->

*Let `f : X → Y` be a morphism locally of finite presentation. The following conditions are equivalent:*

*a) `f` is étale.*

*a') `f` is smooth and unramified.*

*b) `f` is smooth and locally quasi-finite `(Err_{III}, 20)`.*

*c) `f` is flat and unramified.*

*c') `f` is flat, and every fibre `f^{-1}(y)` is a `k(y)`-scheme sum of spectra of fields, finite separable extensions
of `k(y)`.*

*c'') `f` is flat, and for every `y ∈ Y` and every algebraically closed extension `k'` of `k(y)`, the "geometric fibre"
`f^{-1}(y) ⊗_{k(y)} k'` is a sum of spectra of fields isomorphic to `k'`.*

The only point that remains to prove is the equivalence of c') and c''). It is clear that c') implies c'') by base
change `(17.3.3)`. On the other hand, since the projection morphism `f^{-1}(y) ⊗_{k(y)} k' → f^{-1}(y)` is open
`(2.4.10)`, the hypothesis c'') implies that the space `f^{-1}(y)` is discrete, hence, for every point
`x ∈ X_y = f^{-1}(y)`, the local ring `𝒪_{X_y, x} = A` is a finite `k(y)`-algebra, hence an Artinian local ring; in
addition it results from c'') that `Spec(A ⊗_{k(y)} k')` is a sum of spectra of fields isomorphic to `k'`, which is
possible only if `A` is a field, finite separable extension of `k(y)` `(4.6.1)`.

**Proposition (17.6.3).**

<!-- label: IV.17.6.3 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`,
`y = f(x)`. Set `A = 𝒪_{Y, y}`, `B = 𝒪_{X, x}`, which are Noetherian local rings, and let `k` be the residue field of
`A`. Then the equivalent conditions a) to d) of `(17.6.1)` are also equivalent to each of the following:*

*e) `B` is an `A`-algebra formally étale for the adic topologies.*

*e') `B̂` is a free `Â`-module and `B̂ ⊗_Â k` is a field, finite separable extension of `k` (which implies that `B̂` is
a finite `Â`-algebra).*

*If moreover `k(x) = k(y)`, or if `k` is separably closed, these conditions are also equivalent to:*

*e'') The canonical homomorphism `Â → B̂` is bijective.*

The equivalence of e) with each of the conditions of `(17.6.1)` results at once from `(17.4.4, f')` and `(17.5.3, d')`.
The fact that e) implies e') results from `(17.4.4, f)` and from `(0, 19.7.1)`, taking into account that `B̂` is then a
finite `Â`-algebra `(17.4.4)` and that it amounts to the same to say that `B̂` is a flat `Â`-module or a free `Â`-module
`(0_{III}, 10.1.3)`. Conversely, the fact that e') implies e) results from `(17.4.4)` and from `(0, 19.7.1)`. Finally,
e') implies that the homomorphism `Â → B̂` is injective, and if `k(x) = k(y)` or if `k` is separably closed, this
homomorphism is surjective by `(17.4.4)`. The converse is immediate.

**Proposition (17.6.4).**

<!-- label: IV.17.6.4 -->

*Under the hypotheses of `(17.6.3)`, if `f` is étale at the point `x`, one has `dim(𝒪_{X, x}) = dim(𝒪_{Y, y})`.*

This is a particular case of `(17.5.8, (i))` since `x` is isolated in its fibre `f^{-1}(y)`.

<!-- original page 72 -->

### 17.7. Descent properties, passage to the limit, and constructibility

**Proposition (17.7.1).**

<!-- label: IV.17.7.1 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `g : Y' → Y` a morphism, `X' = X ×_Y Y'`,
`f' = f_{(Y')} : X' → Y'` and `g' : X' → X` the canonical projections. Let `x'` be a point of `X'` and set `x = g'(x')`,
`y' = f'(x')`.*

*(i) If `f'` is unramified at the point `x'`, then `f` is unramified at the point `x`.*

*(ii) Suppose moreover that `g` is flat at the point `y'`. Then, if `f'` is smooth (resp. étale) at the point `x'`, `f`
is smooth (resp. étale) at the point `x`.*

Set `y = f(x) = g(y')`, so that one has `f'^{-1}(y') = f^{-1}(y) ⊗_{k(y)} k(y')`; note that `f'` is locally of finite
presentation.

(i) Since the property for a morphism (locally of finite presentation) of being unramified at a point involves only the
fibre of the morphism at that point `(17.4.1, d)`, one can restrict to the case where `Y` and `Y'` are spectra of
fields. But then it amounts to the same to say that `f` (resp. `f'`) is unramified at `x` (resp. `x'`) or that it is
étale at this point `(17.6.1, c)`, hence (i) is a consequence of (ii).

(ii) Since `f'` is flat at the point `x'` `(17.5.1)`, the hypothesis that `g` is flat at the point `y'` implies that `f`
is flat at the point `x`, since the projection `g' : X' → X` is a morphism flat at the point `x'`, and `f ∘ g' = g ∘ f'`
is a morphism flat at the point `x'`, whence the conclusion `(2.2.11, (iv))`. The fact that `f` is smooth (resp. étale)
at the point `x` then involves only the fibre `f^{-1}(y)` `(17.5.1` and `17.6.1)`, and one is therefore again reduced to
the case where `Y = Spec(k)` and `Y' = Spec(k')` are spectra of fields. To say that `f'` is smooth at the point `x'`
then signifies `(17.5.1)` that `X'` is a geometrically regular `k'`-prescheme at the point `x'`, and this implies
`(6.7.8)` that `X` is a geometrically regular `k`-prescheme at the point `x`, hence that `f` is smooth at the point `x`.
Suppose in addition that `f'` is étale at the point `x'`, so that `x'` is isolated in `f'^{-1}(y')` `(17.6.1)`; since
the projection `f'^{-1}(y') → f^{-1}(y)` is an open morphism `(2.4.10)`, `x` is isolated in `f^{-1}(y)`; since one
already knows that `f` is smooth at the point `x`, it is étale at this point `(17.6.1)`.

**Corollary (17.7.2).**

<!-- label: IV.17.7.2 -->

*(i) With the notation of `(17.7.1)`, let `U` (resp. `U'`) be the set of points of `X` (resp. `X'`) where `f` (resp.
`f'`) is unramified; then one has `U' = g'^{-1}(U)`.*

*(ii) Suppose moreover that `g` is flat, and let `V` (resp. `V'`) be the set of points of `X` (resp. `X'`) where `f`
(resp. `f'`) is smooth; then `V' = g'^{-1}(V)`.*

**Corollary (17.7.3).**

<!-- label: IV.17.7.3 -->

*(i) Suppose `g` surjective; then, for `f` to be unramified, it is necessary and sufficient that `f'` be so.*

*(ii) Let `f : X → Y` be an `S`-morphism, `g : S' → S` a faithfully flat morphism. Suppose that `f` is locally of finite
presentation, or that `g` is quasi-compact. Then, for `f` to be smooth (resp. unramified, resp. étale), it is necessary
and sufficient that `f'` be so.*

In (ii), the case where `f` is locally of finite presentation results from `(17.7.1)`. If `g` is quasi-compact and `f'`
smooth (resp. unramified, resp. étale), `f'` is locally of finite presentation by `(2.7.1, (iv))` and one is reduced to
the first case.

**Proposition (17.7.4).**

<!-- label: IV.17.7.4 -->

*Let `f : X → Y` be a morphism, `g : Y' → Y` a morphism flat and locally of finite presentation, `X' = X ×_Y Y'`,
`f' = f_{(Y')} : X' → Y'` and `g' : X' → X` the canonical projections.*

<!-- original page 73 -->

*Let `V` (resp. `V'`) be the set of `x ∈ X` (resp. `x' ∈ X'`) where `f` possesses one of the following properties (resp.
where `f'` possesses the same property): being:*

*(i) locally of finite type;*

*(ii) locally of finite presentation;*

*(iii) flat;*

*(iv) unramified;*

*(v) smooth;*

*(vi) étale.*

*Then one has `V' = g'^{-1}(V)` (in other words, for `f'` to have the property in question at a point `x'`, it is
necessary and sufficient that `f` have this property at the point `x = g'(x')`).*

Property (iii) is included only for the record, and does not require the hypothesis that `g` be locally of finite
presentation (`(2.2.11, (iv))`, taking into account the fact that the projection `g' : X' → X` is a flat morphism). By
virtue of `(17.7.2)`, the assertions relative to properties (iv), (v), and (vi) are consequences of the assertion
relative to (ii). It therefore suffices to consider cases (i) and (ii). It is clear that `V' ⊃ g'^{-1}(V)`; it remains
therefore to show that `V' ⊂ g'^{-1}(V)`; note that the sets `V` and `V'` are open, and `W = g'(V')` is also open in `X`
by virtue of `(2.4.6)`. It is therefore a question of proving that the morphism `f | W : W → Y` is locally of finite
type (resp. locally of finite presentation); since by hypothesis the composite `V' →^{g''} W → Y` (where `g''` is the
restriction of `g'`), equal to `V' → Y' → Y`, is locally of finite type (resp. locally of finite presentation) and `g''`
is surjective (hence faithfully flat), one is reduced to proving the following lemma, which improves `(11.3.16)`:

**Lemma (17.7.5).**

<!-- label: IV.17.7.5 -->

*Let `f : X → Y` be a faithfully flat morphism and locally of finite presentation, `g : Y → Z` a morphism such that
`g ∘ f : X → Z` has one of the following properties: being:*

*(i) locally of finite type;*

*(ii) locally of finite presentation;*

*(iii) of finite type.*

*Then `g` has the same property.*

*If in addition `f` is quasi-compact or `g` quasi-separated, the same conclusion is valid for the property:*

*(iv) being of finite presentation.*

In cases (i) and (ii), it is a question of seeing that for every `y ∈ Y`, there is an affine open neighbourhood `V` of
`y` in `Y` and an affine open neighbourhood `W` of `z = g(y)` in `Z` containing `g(V)` such that the morphism `V → W`,
restriction of `g`, be of finite type (resp. of finite presentation). Now, by hypothesis there exist `x ∈ X` such that
`f(x) = y`, an affine open neighbourhood `U` of `x` in `X`, an affine open neighbourhood `V` of `y` in `Y` containing
`f(U)`, and an affine open neighbourhood `W` of `z` in `Z` containing `g(V)` such that the morphism `f_1 : U → V`
restriction of `f` be flat and of finite presentation, and the morphism `g_1 : V → W` restriction of `g` such that
`g_1 ∘ f_1` be of finite type (resp. of finite presentation). Then `f(U)` is open in `Y` `(2.4.6)`, and if `V' ⊂ f(U)`
is an affine neighbourhood of `y`, the morphism `f_2 : f_1^{-1}(V') → V'`,

<!-- original page 74 -->

restriction of `f_1`, is still of finite presentation and is moreover faithfully flat; in addition, if `g_2 = g_1 | V'`,
`g_2 ∘ f_2` is of finite type (resp. of finite presentation), the open `f_1^{-1}(V')` being quasi-compact (resp.
quasi-compact and quasi-separated). One is then reduced to the hypotheses of `(11.3.16)`, whence one concludes that
`g_2` is a morphism of finite type (resp. of finite presentation).

In case (iii) the question is local on `Z`, so one can suppose `Z` affine, and it then follows that `X` is
quasi-compact, hence so is `Y = f(X)`. Case (iii) is therefore a consequence of (i).

In case (iv) (with the supplementary hypotheses on `f` or `g`), one can also suppose `Z` affine, hence `X` and `Y`
quasi-compact; one already knows in addition that `g` is locally of finite presentation and quasi-compact `(1.1.3)`, so
everything reduces to seeing that `g` is quasi-separated, and it therefore suffices to show that this property is true
when one supposes `f` quasi-compact. Now, since `g ∘ f` is quasi-separated, so is `f` `(1.2.2, (v))`; since `f` is
quasi-compact and locally of finite presentation, it is of finite presentation `(1.6.1)`; it then suffices to repeat the
reasoning of the first paragraph of the proof of `(11.3.16)`.

**Remark (17.7.6).** — In the assertion relative to property (iv), one cannot suppress the hypothesis that `f` is
quasi-compact; otherwise, this would imply that every morphism `g : Y → Z` quasi-compact and locally of finite
presentation would be of finite presentation, a conclusion which is known to be erroneous `(1.6.4)`. Indeed, one can
restrict to the case where `Z` is affine, hence `Y` quasi-compact; there is consequently a finite cover `(U_α)` of `Y`
by affine opens such that the restrictions `g | U_α` are of finite presentation; it would then suffice to take for `X`
the prescheme sum of the `U_α`, for `f : X → Y` the canonical morphism, which is evidently faithfully flat and locally
of finite presentation `(1.4.3)`; `g ∘ f` would be of finite presentation by virtue of the choice of the `U_α` and
`(1.6.5)`, whence our assertion.

**Proposition (17.7.7).**

<!-- label: IV.17.7.7 -->

*Let `f : Y → S` and `h : X → S` be two morphisms locally of finite presentation, `g : X → Y` an `S`-morphism, `x` a
point of `X`, `y = g(x)`. Suppose that `g` is flat at the point `x`. Then, if `h` is smooth (resp. unramified, resp.
étale) at the point `x`, `f` is smooth (resp. unramified, resp. étale) at the point `y`.*

Set `s = h(x) = f(y)`. To say that `h` is unramified at the point `x` (resp. that `f` is unramified at the point `y`)
amounts to saying that `h^{-1}(s)` is étale over `k(s)` at the point `x` (resp. that `f^{-1}(s)` is étale over `k(s)` at
the point `y`) `(17.4.1` and `17.6.1)`; since the morphism `g_s : h^{-1}(s) → f^{-1}(s)` deduced from `g` is flat at the
point `x`, one sees that one can restrict to proving the proposition when `h` is smooth or étale at the point `x`. In
addition, since `h` is then flat at the point `x` `(17.5.1)`, `f` is flat at the point `y`, as results from
`(2.2.11, (iv))`. It amounts therefore to the same `(17.5.1)` to say that `f` is smooth (resp. étale) at the point `y`,
or that `f^{-1}(s)` is smooth (resp. étale) over `k(s)` at the point `y`. One is thus reduced to the case where
`S = Spec(k)` is the spectrum of a field.

(i) *Case of smooth morphisms.* Since `g` is a morphism locally of finite presentation `(1.4.3, (v))`, there is an open
neighbourhood `U` of `x` in `X` in which `g` is flat `(11.3.1)` and `h` smooth. In addition `g(U)` is an open
neighbourhood of `y` in `Y` `(2.4.6)`; replacing `X` by `U` and `Y` by `g(U)`, one can therefore suppose that `g` is
faithfully flat and that `h` is smooth, and one is reduced to proving that `f` is then smooth. If `k'` is an

<!-- original page 75 -->

algebraically closed extension of `k`, `X ⊗_k k'` is then smooth over `k'` and by virtue of `(17.7.3, (ii))`, it
suffices to prove that `Y ⊗_k k'` is smooth over `k'` (since `Spec(k') → Spec(k)` is faithfully flat); one can therefore
restrict to the case where `k` is algebraically closed. Since the set of points of `Y` rational over `k` is then very
dense in `Y` `(10.4.8)` and since the set of points of `Y` where `Y` is smooth over `k` is open, one sees that it
suffices to prove that `Y` is smooth over `k` at every point rational over `k`. But at such a point `y`, to say that `Y`
is smooth over `k` at this point amounts to saying that `Y` is regular at `y` `(17.5.1` and `6.7.8)`. Now one has
`y = g(x)` for some `x ∈ X` and by hypothesis `(17.5.1)` `X` is regular at the point `x`; since `X` and `Y` are then
locally Noetherian and `g` is flat, `Y` is indeed regular at the point `y` `(6.5.1, (i))`.

(ii) *Case of étale morphisms.* By (i) one already knows that `f` is smooth at the point `y`; by virtue of `(17.6.1)`,
it therefore suffices to show that `f` is quasi-finite at the point `y`, or again that `𝒪_{Y, y}` is a finite
`k`-algebra. Now, since `𝒪_{X, x}` is a faithfully flat `𝒪_{Y, y}`-module `(0_I, 6.6.2)`, `𝒪_{Y, y}` identifies with a
sub-`k`-module of `𝒪_{X, x}` and since `𝒪_{X, x}` is by hypothesis a finite `k`-algebra, so is `𝒪_{Y, y}`.

**Proposition (17.7.8).**

<!-- label: IV.17.7.8 -->

*The notations being those of `(8.8.1)`, suppose `X_α` and `Y_α` locally of finite presentation over `S_α`. Let
`f_α : X_α → Y_α` be an `S_α`-morphism, `f : X → Y` the corresponding `S`-morphism.*

*(i) Let `x` be a point of `X`, `x_α` its canonical projection in `X_α`. For `f` to be smooth (resp. unramified, resp.
étale) at the point `x`, it is necessary and sufficient that there exist `λ ≽ α` such that `f_λ` be smooth (resp.
unramified, resp. étale) at the point `x_λ`.*

*(ii) Suppose moreover `X_α` quasi-compact. For `f` to be smooth (resp. unramified, resp. étale), it is necessary and
sufficient that there exist `λ ≽ α` such that `f_λ` be smooth (resp. unramified, resp. étale).*

(i) If `y = f(x)`, `y_α = f_α(x_α)` is the canonical projection of `y` in `Y_α`, and one has
`f^{-1}(y) = f_α^{-1}(y_α) ⊗_{k(y_α)} k(y)`; the part of the statement concerning unramified morphisms therefore results
from `(17.7.1, (i))`, and it suffices therefore to consider the case of smooth morphisms. Since `f` and `f_α` are
locally of finite presentation, it amounts to the same to say

<!-- original page 76 -->

that `f^{-1}(y)` is geometrically regular at the point `x` or that `f_α^{-1}(y_α)` is geometrically regular at the point
`x_α` `(6.7.8)`. The proposition therefore results from `(17.5.1)` and from `(11.2.6)`.

(ii) For each `λ`, let `U_λ` be the open set of `x_λ ∈ X_λ` such that `f_λ` is smooth (resp. unramified, resp. étale) at
the point `x_λ`; let `V_λ` be its inverse image in `X`. Since, by hypothesis, for each `x ∈ X` there exists, by virtue
of (i), a `λ` such that `f_λ` is smooth (resp. unramified, resp. étale) at the point `x_λ`, `X` is the union of the
`V_λ`. Moreover `(17.3.3)`, for `λ ≼ μ` one has `V_λ ⊂ V_μ`; hence, since `X` is quasi-compact, there exists an index
`μ` such that `X = V_μ`. Since the `X_λ` are quasi-compact, it then results from `(8.3.4)` that there exists an index
`ν ≽ μ` such that the inverse image of `U_ν` in `X_ν` is `X_ν` in its entirety, which signifies that `f_ν` is smooth
(resp. unramified, resp. étale) by `(17.3.3)`.

**Corollary (17.7.9).**

<!-- label: IV.17.7.9 -->

*Let `S = Spec(A)` be an affine scheme, `f : X → S` a morphism. The following conditions are equivalent:*

*a) `f` is a morphism of finite presentation and smooth (resp. unramified, resp. étale).*

*b) There exist a Noetherian affine scheme `S_0 = Spec(A_0)`, a morphism of finite type `f_0 : X_0 → S_0`, and a
morphism `S → S_0` such that the `S`-prescheme `X_0 ⊗_{S_0} S` be `S`-isomorphic to `X` and that `f_0` be smooth (resp.
unramified, resp. étale).*

*c) The conditions of b) are verified, and in addition `A_0` is a sub-`ℤ`-algebra of finite type of `A`, the morphism
`S → S_0` corresponding to the canonical injection `A_0 → A`.*

The proof from `(17.7.8)` is the same as that of `(11.2.7)` from `(11.2.6)`.

**Proposition (17.7.10).**

<!-- label: IV.17.7.10 -->

*Let `f : Y → S`, `h : X → S` be two morphisms locally of finite presentation, `g : X → Y` an `S`-morphism, `x` a point
of `X`, `y = g(x)`. Suppose that `h` is flat at the point `x` and that `f` is unramified at the point `y`. Then `f` is
étale at the point `y` and `g` is flat at the point `x`.*

(One will see further on `(18.4.9)` that one can in fact dispense with the hypothesis that `h` is locally of finite
presentation.)

The question being local on `S`, `X`, and `Y`, one can suppose that `S`, `X`, and `Y` are affine, `f`, `g`, `h`
morphisms of finite presentation, `h` flat and `f` unramified. Taking `(11.2.7)` and `(17.7.9)` into account, one can in
addition suppose that `S`, `X`, and `Y` are Noetherian; finally one can restrict to the case where `S = Spec(𝒪_{S, s})`
(where `s = f(y) = h(x)`). The ring `A = 𝒪_{S, s}` being a Noetherian local ring, there exists a complete Noetherian
local ring `B`, with algebraically closed residue field and a local homomorphism `A → B` making `B` into a faithfully
flat `A`-module `(0_{III}, 10.3.1)`. Replacing `X` and `Y` by `X ×_S Spec(B)` and `Y ×_S Spec(B)`, one concludes by
`(2.5.1)` and `(17.7.1)` that one can restrict to the case where `A` is complete and has an algebraically closed residue
field. The hypothesis that `f` is unramified at the point `y` then implies `(17.4.4)` that `𝒪_{Y, y}` is a finite
`𝒪_{S, s}`-algebra and a complete Noetherian local ring `(0_I, 7.4.2)`, and since the residue field of `𝒪_{S, s}` is
algebraically closed, the homomorphism `𝒪_{S, s} → 𝒪_{Y, y}` is surjective `(17.4.4)`. But, on the other hand, the
hypothesis that `h` is flat at the point `x` implies that the composite homomorphism `𝒪_{S, s} → 𝒪_{Y, y} → 𝒪_{X, x}` is
injective `(0_I, 6.5.1)`, hence the homomorphism `𝒪_{S, s} → 𝒪_{Y, y}` is bijective, which shows that `f` is étale at
the point `y` `(17.6.3)`; in addition, `𝒪_{X, x}` is a flat `𝒪_{Y, y}`-module, hence `g` is flat at the point `x`.

**Proposition (17.7.11).**

<!-- label: IV.17.7.11 -->

*Let `S` be a prescheme, `X`, `Y` two `S`-preschemes locally of finite presentation over `S`, `f : X → Y` an
`S`-morphism. For each `s ∈ S`, denote by `X_s`, `Y_s`, `f_s` the preschemes and the morphism deduced from `X`, `Y`, `f`
by the base change `Spec(k(s)) → S`. Then:*

*(i) The set of `x ∈ X` such that, if `s` is the image of `x` in `S`, `f_s : X_s → Y_s` be smooth (resp. unramified,
resp. étale, resp. differentially smooth) at the point `x`, is locally constructible.*

*(ii) Suppose `f` of finite presentation. The set of `y ∈ Y` such that, if `s` is the image of `y` in `S`, `f_s` be
smooth (resp. unramified, resp. étale, resp. differentially smooth) at every point of `f_s^{-1}(y)`, is locally
constructible.*

*(iii) Suppose `X` and `Y` of finite presentation over `S`. The set of `s ∈ S` such that `f_s` be smooth (resp.
unramified, resp. étale, resp. differentially smooth) is locally constructible.*

Let `E` be the set of `x ∈ X` verifying the property considered in (i). Then the set `F` of `y ∈ Y` verifying the
corresponding property considered in (ii) is none

<!-- original page 77 -->

other than `Y − f(X − E)`, hence (ii) results from (i) and from Chevalley's theorem when `f` is of finite presentation
`(1.8.4)`. Likewise, if `h : Y → S` is the structure morphism, the set of `s ∈ S` verifying the corresponding property
considered in (iii) is `S − h(Y − F)`, hence (iii) follows again from (ii) and from Chevalley's theorem when `f` and `h`
are of finite presentation. It therefore suffices to prove the assertions of (i).

Let us first prove (i) when it is a question of the property of being smooth.

The question being local on `X`, one can restrict to the case where `S = Spec(A)`, `X = Spec(B)`, and `Y = Spec(C)` are
affine, `B` and `C` being `A`-algebras of finite presentation. Reasoning as at the beginning of `(9.9.1)` and using
`(17.7.2, (ii))`, one reduces to the case where `A` is Noetherian. By virtue of `(0_{III}, 9.2.3)`, one is reduced to
seeing that if `x ∈ E` (resp. if `x ∉ E`), there exists a neighbourhood `V` of `x` in `‾{x}` contained in `E` (resp. in
`X − E`). Designating by `g : X → S` and `h : Y → S` the structure morphisms, one can first replace `S` by the reduced
sub-prescheme `S'` of `S` having `‾{g(x)}` as underlying space, `X` by `g^{-1}(S')`, `Y` by `h^{-1}(S')`, the fibres of
`X` and `X'` (resp. `Y` and `Y'`) at the points of `S'` being the same. In other words one can restrict to the case
where `S` is integral and where `η = g(x) = h(y)` (where `y = f(x)`) is its generic point.

1° Suppose first that `x ∈ E`. The local rings `𝒪_{X_η, x}` and `𝒪_{Y_η, y}` are respectively equal to `𝒪_{X, x}` and
`𝒪_{Y, y}`; since the smoothness property of a morphism of finite presentation at a point depends only on the local ring
of that point and on the local ring of its image `(17.5.1)`, one sees that the hypothesis `x ∈ E` amounts to saying that
the morphism `f` is smooth at the point `x`; it still possesses this property at the points of an open neighbourhood of
`x` in `X`, and it suffices to apply `(17.3.3, (iii))` to obtain the conclusion.

2° Suppose secondly that `x ∈ X − E`, and that the morphism `f_η` is not flat at the point `x`. The conclusion then
results from the following lemma which makes `(11.2.8)` more precise:

**Lemma (17.7.11.1).**

<!-- label: IV.17.7.11.1 -->

*Let `g : X → S`, `h : Y → S` be two morphisms locally of finite presentation, `f : X → Y` an `S`-morphism, `ℱ` a
quasi-coherent `𝒪_X`-Module of finite presentation. Then the set `E` of `x ∈ X` such that `ℱ_x` is
`𝒪_{Y_{g(x)}, f(x)}`-flat at the point `x` is locally constructible.*

Reasoning again as at the beginning of `(9.9.1)` and using `(2.5.1)`, one reduces to the case where `S`, `X`, and `Y`
are Noetherian; then one reduces as above to the case where `S` is integral, where `η = g(x) = h(f(x))` is its generic
point, and one has to show that if `x ∈ E` (resp. `x ∉ E`) there is a neighbourhood `V` of `x` in `‾{x}` contained in
`E` (resp. in `X − E`). The case where `x ∈ E` is an immediate consequence of `(11.1.1)`. To treat the case where
`x ∉ E`, one reasons as in `(9.4.7.1)`, whose notation we preserve, so that one can suppose, replacing possibly `Y` and
`X` by neighbourhoods of `f(x)` and `x` respectively, that there exist two coherent `𝒪_Y`-Modules `𝒢`, `ℋ` and an
`𝒪_Y`-homomorphism `u : 𝒢 → ℋ` such that for each `s ∈ S`, `u_s : 𝒢_s → ℋ_s` be injective, but that the homomorphism
`1 ⊗ u : ℱ ⊗_{𝒪_Y} 𝒢 → ℱ ⊗_{𝒪_Y} ℋ` is not injective at the point `x`, in other words `x ∈ Supp(Ker(1 ⊗ u))`; if one
sets `T = ‾{x}`, one therefore has `Supp(Ker(1 ⊗ u)) ⊃ T_η`. But one can suppose that for each `s ∈ S`, one has
`Ker(1 ⊗ u_s) = (Ker(1 ⊗ u))_s` `(9.4.2)`, hence

<!-- original page 78 -->

`Supp(Ker(1 ⊗ u_s)) = (Supp(Ker(1 ⊗ u)))_s` `(I, 9.1.13.1)`; it follows finally from `(9.5.2)` that for `s` in a
neighbourhood of `η`, one has `(Supp(Ker(1 ⊗ u_s)))_s ⊃ T_s`, which establishes the lemma.

3° Suppose now that `x ∈ X − E`, that the morphism `f_η` is flat at the point `x`, but that `f_η` is not smooth at the
point `x`. Note that to say that `f_η` is flat at the point `x` amounts to saying that `f` itself is flat at the point
`x` and replacing `X` by a neighbourhood of `x`, one can suppose that `f` is flat `(11.1.1)`; one concludes that the
same is true of `f_s` for every `s ∈ S`, and since for every `y ∈ Y`, `f_s^{-1}(y) = f^{-1}(y)`, it amounts to the same
to say that `f_{g(x')}` is smooth at the point `x'` or to say that `f` is smooth at the point `x'`. But the set of
`x' ∈ X` where `f` is smooth is open in `X` `(12.1.7)`, hence the set of `x' ∈ X` where `f` is not smooth is closed, and
since it contains `x` by hypothesis, it also contains `‾{x}`, which completes the proof for the first property
considered in (i).

Let us prove secondly (i) when it is a question of the property of being étale. Note for this that this property for `f`
at the point `x` amounts to saying that `f` is at the same time smooth and quasi-finite at the point `x` `(17.6.1)`.
Now, it amounts to the same to say that `f_{g(x)}` is quasi-finite at the point `x` or that `f` is itself quasi-finite
at this point; it follows therefore from `(13.1.4)` that the set of points `x` such that `f_{g(x)}` be quasi-finite at
the point `x` is open in `X`, and a fortiori locally constructible; the conclusion follows therefore from the fact that
the set of `x` such that `f_{g(x)}` be smooth at the point `x` is also locally constructible.

Let us pass to the proof of (i) when it is a question of the property of being *differentially smooth*. Let
`p : X ×_Y X → X` be the second canonical projection; the second projection `X_s ×_{Y_s} X_s → X_s` is none other than
`p_s` for each `s ∈ S`, and it follows therefore from `(17.12.5.1)`[^17.7.11.note1] that for `f_{g(x)}` to be
differentially smooth at the point `x`, it is necessary and sufficient that `p_{g(x)}` be smooth at the point `Δ_f(x)`.
Since `p` is locally of finite presentation, the set of points `ξ ∈ X ×_Y X` such that `p_{g(ξ)}` is smooth at the point
`ξ` is locally constructible, and the intersection of this set with the locally closed set `Δ_f(X)` is therefore also
locally constructible in `Δ_f(X)` `(1.8.2)`; the restriction of `p` to `Δ_f(X)` being an isomorphism onto `X`, one sees
that the set of `x ∈ X` such that `f_{g(x)}` be differentially smooth at the point `x` is locally constructible.

Consider finally the property of being unramified; note that the diagonal morphism `Δ_f : X → X ×_Y X` is an immersion
locally of finite presentation `(1.4.3.1)` and for each `s ∈ S`, the diagonal morphism `Δ_{f_s} : X_s → X_s ×_{Y_s} X_s`
is none other than `(Δ_f)_s`; to say that `f_{g(x)}` is unramified at the point `x` amounts to saying that
`(Δ_f)_{g(x)}` is a local isomorphism at the point `x` `(17.4.1)`, and since it is an immersion locally of finite
presentation, it amounts to the same `(17.9.1)`[^17.7.11.note2] to say that `(Δ_f)_{g(x)}` is étale at the point `x`; it
therefore suffices to apply what was seen above for the property of being étale.

<!-- original page 79 -->

### 17.8. Criteria for smoothness and unramifiedness by fibres

**Proposition (17.8.1).**

<!-- label: IV.17.8.1 -->

*Let `g : Y → S`, `h : X → S` be two morphisms locally of finite presentation. For an `S`-morphism `f : X → Y` to be
unramified, it is necessary and sufficient that for each `s ∈ S`, the morphism `f_s : h^{-1}(s) → g^{-1}(s)` deduced
from `f` by the base change `Spec(k(s)) → S` be unramified.*

This results at once from the fact that, for a morphism locally of finite presentation, the property of being unramified
is a property of the fibres of this morphism `(17.4.1, d)`, and from the fact that, for every `y ∈ Y`, one has
`f^{-1}(y) = f_s^{-1}(y)` if `s = g(y)`.

**Proposition (17.8.2).**

<!-- label: IV.17.8.2 -->

*Let `g : Y → S`, `h : X → S` be two morphisms locally of finite presentation; suppose moreover that `h` is flat. For an
`S`-morphism `f : X → Y` to be smooth (resp. étale), it is necessary and sufficient that, for each `s ∈ S`, the morphism
`f_s : h^{-1}(s) → g^{-1}(s)` deduced from `f` by the base change `Spec(k(s)) → S` be smooth (resp. étale). When this is
so, the morphism `g` is flat at the points of `f(X)`.*

One knows indeed `(11.3.10)` that for `f` to be flat, it is necessary and sufficient that `f_s` be so for each `s ∈ S`,
and that then `g` is flat at the points of `f(X)`. But for a flat morphism locally of finite presentation, the property
of being smooth is a property of the fibres of this morphism `(17.5.1, b)`, and for every `y ∈ Y`, one has
`f^{-1}(y) = f_s^{-1}(y)` if `s = g(y)`.

**Remark (17.8.3).** — The preceding proofs show (taking `(11.3.10)` into account) that if the hypotheses on `g` and `h`
are the same as above, then, for `f` to be unramified (resp. smooth, resp. étale) at a point `x ∈ X`, it suffices that,
if one sets `s = h(x)`, `f_s` be unramified (resp. smooth, resp. étale) at the point `x`.

### 17.9. Étale morphisms and open immersions

**Theorem (17.9.1).**

<!-- label: IV.17.9.1 -->

*Let `f : X → Y` be a morphism. The following properties are equivalent:*

*a) `f` is an open immersion.*

*b) `f` is a flat monomorphism locally of finite presentation.*

*c) `f` is étale and radicial.*

It results from `(1.4.3, (i))` that a) implies b). Condition b) implies that for every `y ∈ Y`, the fibre `f^{-1}(y)` is
empty or isomorphic to `Spec(k(y))` `(8.11.5.1)`, hence b) implies c) by virtue of `(17.6.2, c)`. It remains to see that
c) implies a).

The question being local on `X` and on `Y` (since `f` is injective), one can restrict to the case where `Y` is affine
and `f` of finite presentation. Since `f` is flat, it is an open morphism `(2.4.6)`, hence, replacing `Y` by `f(X)`, one
can suppose that `f` is surjective. For every morphism `Y' → Y`, `f' = f_{(Y')} : X' → Y'` is still étale, radicial,
surjective, and of finite presentation, hence open, and consequently a homeomorphism; in other words, `f` is a universal
homeomorphism, and being of finite type and separated `(1.8.7.1)`, `f` is proper. The hypothesis that `f` is radicial
and of finite type then implies that `f` is quasi-finite; hence `(8.11.1)` `f` is a finite morphism. To prove that `f`
is an isomorphism, one can restrict to the case

<!-- original page 80 -->

where `Y = Spec(A)`, `A` being a local ring. Since `f` is of finite presentation, one has `X = Spec(B)`, where `B` is a
flat `A`-module of finite presentation `(1.4.7)`, hence free
`(Bourbaki, Alg. comm., chap. II, §5, n° 2, cor. 2 of th. 1)`. In addition, if `𝔪` is the maximal ideal of `A` and `k`
its residue field, `B/𝔪 B` is by hypothesis a field, at once radicial extension and finite separable extension of `k`,
since `f` is étale and radicial `(17.6.1)`; hence `B/𝔪 B` is isomorphic to `k`, and since `B` is a free `A`-module, `B`
is isomorphic to `A`. Q.E.D.

**Corollary (17.9.2).**

<!-- label: IV.17.9.2 -->

*Let `X` be a connected prescheme; if `f : X → Y` is an étale closed immersion, then `f` is an isomorphism of `X` onto
an open connected component of `Y`.*

Indeed `f` is étale and radicial, hence an isomorphism of `X` onto a sub-prescheme induced on an open part of `Y`; but
by hypothesis `f(X)` is closed in `Y`, hence at once open and closed, and since `f(X)` is connected, it is a connected
component of `Y`.

**Corollary (17.9.3).**

<!-- label: IV.17.9.3 -->

*Let `f : X → Y` be an étale (resp. étale and separated) morphism. Then every `Y`-section `g : Y → X` of `X` is an open
immersion (resp. open and closed); in addition the map `g ↦ g(Y)` is a bijection of the set `Γ(X/Y)` of `Y`-sections of
`X` onto the set of open parts `Z` (resp. open and closed) of `X` such that the restriction of `f` to `Z` be a
surjective and radicial morphism from `Z` onto `Y`.*

Indeed, the fact that `g` is an open immersion already results from the fact that `f` is unramified `(17.4.1, b'')`, and
the restriction of `f` to the open `g(Y)` of `X` is an isomorphism. Conversely, if `Z` is an open of `X` such that
`f | Z` be a surjective and radicial morphism from `Z` onto `Y`, `f | Z` is an isomorphism by virtue of `(17.9.1)`,
since it is étale. If `f` is in addition separated, one knows that `g` is a closed immersion `(I, 5.4.6)`, which
completes the proof of the corollary.

**Corollary (17.9.4).**

<!-- label: IV.17.9.4 -->

*Let `Y` be a connected prescheme, `f : X → Y` an étale and separated morphism. Then every `Y`-section `g` of `X` is an
isomorphism of `Y` onto an open connected component of `X`, and the map `g ↦ g(Y)` is a bijection of `Γ(X/Y)` onto the
set of open connected components `Z` of `X` such that the restriction of `f` to `Z` be a surjective and radicial
morphism from `Z` onto `Y`.*

**Corollary (17.9.5).**

<!-- label: IV.17.9.5 -->

*Let `g : Y → S`, `h : X → S` be two morphisms locally of finite presentation; suppose moreover that `h` is flat. For an
`S`-morphism `f : X → Y` to be an open immersion (resp. an isomorphism), it is necessary and sufficient that, for each
`s ∈ S`, the morphism `f_s : h^{-1}(s) → g^{-1}(s)` deduced from `f` by the base change `Spec(k(s)) → S` be an open
immersion (resp. an isomorphism).*

Indeed, if `f_s` is an open immersion for each `s ∈ S`, it results from `(17.8.3)` that `f` is an étale morphism; since
for every `y ∈ Y`, one has `f^{-1}(y) = f_s^{-1}(y)` with `s = g(y)`, `f` is radicial; hence `f` is an open immersion by
virtue of `(17.9.1)`. If in addition `f_s` is surjective for each `s ∈ S`, `f` is surjective, hence an isomorphism.

The following proposition makes `(10.4.11)` more precise:

**Proposition (17.9.6).**

<!-- label: IV.17.9.6 -->

*Let `S` be a prescheme, `X` an `S`-prescheme of finite presentation. Every `S`-endomorphism of `X` which is a
monomorphism is an automorphism of `X`.*

Let `f : X → S` be the structure morphism, `g` the `S`-endomorphism in question. The question is local on `S`, and one
can consequently suppose that `S` is affine. Using `(8.9.1)` and `(8.10.5, (i bis))`, one is reduced to the case where
`S = Spec(A)`, where `A` is a `ℤ`-algebra of finite type, and consequently `X` is a `ℤ`-prescheme of finite type. It
already results from `(10.4.11)` that `g` is a bijective morphism, since a monomorphism is radicial `(8.11.5.1)`; it
will therefore suffice to show

<!-- original page 81 -->

that `g` is an open immersion, and since `g` is radicial, it will suffice, by virtue of `(17.9.1)`, to prove that `g` is
étale. In addition, since the set of points where `g` is étale is open and since `X` is a Jacobson prescheme `(10.4.7)`,
it will suffice to show that `g` is étale at every closed point of `X` `(10.3.1)`. Set `z' = g(z)`; it results from
`(10.4.11.1, (i))` that `z'` is also a closed point of `X` and since `g` is a monomorphism, the map `k(z') → k(z)`
deduced from `g` is an isomorphism. For `g` to be étale at the point `z` it is therefore necessary and sufficient that
the canonical homomorphism `𝒪_{X, z'} → 𝒪_{X, z}` be bijective `(17.6.3, e'')`. To do this we shall prove that for every
integer `n`, the canonical homomorphism `𝒪_{X, z'}/𝔪_{z'}^{n+1} → 𝒪_{X, z}/𝔪_z^{n+1}` is bijective, whence the
conclusion will follow at once. One can suppose that `z` belongs to the finite set `T_{p, d}` of closed points `t` of
`X` such that `k(t)` is an extension of `𝔽_p` whose degree divides `d`; in which case it is the same for `z'`. Designate
by `𝓘` the coherent Ideal of `𝒪_X` such that `𝓘_x = 𝒪_x` for `x ∉ T_{p, d}`, and `𝓘_x = 𝔪_x^{n+1}` for `x ∈ T_{p, d}`.
Let `T_{p, d, n}` be the closed sub-prescheme of `X` defined by `𝓘`, `j : T_{p, d, n} → X` the canonical injection; the
composite morphism `g ∘ j : T_{p, d, n} → X` maps the set `T_{p, d}` into itself, and for every `x ∈ T_{p, d}`, the
homomorphism `𝒪_{g(x)} → 𝒪_x/𝔪_x^{n+1}` factors as

```text
  𝒪_{g(x)} → 𝒪_{g(x)}/𝔪_{g(x)}^{n+1} → 𝒪_x/𝔪_x^{n+1}.
```

Hence `(I, 4.1.9)` there exists a unique endomorphism `g'` of `T_{p, d, n}` such that `j ∘ g' = g ∘ j`. Since `j` is a
monomorphism, and the same holds for `g` by hypothesis, one deduces that `g'` is also a monomorphism, and the
proposition will be proved if one shows that `g'` is an automorphism of `T_{p, d, n}`. Now, for every `x ∈ T_{p, d, n}`,
one has seen that `k(x)` is a finite field, and since `𝒪_x` is Noetherian, each of the `𝔪_x^i/𝔪_x^{i+1}` is a
`k(x)`-vector space of finite rank; whence one concludes at once that the local ring `𝒪_x/𝔪_x^{n+1}` of `T_{p, d, n}` at
the point `x` has a finite number of elements, and a fortiori is a `ℤ`-module of finite type. Since `T_{p, d, n}` is a
sum of the preschemes `Spec(𝒪_x/𝔪_x^{n+1})` in finite number, it is a *finite* `ℤ`-prescheme; the endomorphism `g'` is
therefore itself finite `(II, 6.1.5, (v))`, hence proper. But a proper monomorphism is a closed immersion `(8.11.5)`; if
`T_{p, d, n} = Spec(B)`, `g'` corresponds therefore to a surjective endomorphism `φ : B → B` of the ring `B`. Now, the
set `B` is finite, hence `φ` is necessarily bijective. Q.E.D.

<!-- original page 81 -->

### 17.10. Relative dimension of a smooth prescheme over another

**Definition (17.10.1).**

<!-- label: IV.17.10.1 -->

*Let `f : X → Y` be a morphism locally of finite type. One calls **relative dimension of `f` at the point `x ∈ X`** (or
**relative dimension of `X` over `Y` at the point `x`**) and one denotes by `dim_x f` the positive integer
`dim_x(f⁻¹(f(x)))`.*

To say that `f` is quasi-finite at the point `x` `(II, §1, n° 20)` thus amounts to saying that `dim_x f = 0`. We have
seen `(13.1.3)` that the function `x ↦ dim_x f` is upper semi-continuous. One will note that, even when the morphism `f`
has property `(S₁)` (in other words `(6.8.1)` is flat and such that its fibres have no immersed associated prime cycle),
the function `x ↦ dim_x f` is not necessarily continuous, as shown by the example where `Y = Spec(k)`, with `k` a field,
and `X = Spec(k[U, V, W]/𝔭𝔮)`, where `𝔭 = (W)` and `𝔮 = (U) + (V − W)` are prime ideals of `k[U, V, W]` (`X` being thus
the union, in 3-dimensional space, of a plane and a line not parallel to this plane).

To say that a morphism locally of finite presentation `f : X → Y` is étale at the point `x ∈ X` means again that `f` is
smooth at the point `x` and that `dim_x f = 0` `(17.6.1)`.

**Proposition (17.10.2).**

<!-- label: IV.17.10.2 -->

*Let `f : X → Y` be a smooth morphism. For every `x ∈ X`, the locally free `𝒪_X`-Module `Ω_{X/Y}^1` `(17.2.3)` has a
rank at `x` equal to `dim_x f` (which implies that `x ↦ dim_x f` is a continuous function on `X`).*

Indeed, if `y = f(x)`, `X_y = f⁻¹(y)` is smooth over `k(y)`, and if `f_y : X_y → Spec(k(y))` is the structure morphism,
one has `Ω_{X_y/k(y)}^1 = Ω_{X/Y}^1 ⊗_{𝒪_Y} k(y)` `(16.4.5)`; one can thus restrict to the case where `Y = Spec(k)` is
the spectrum of a field; moreover, by virtue of `(16.4.5)` and `(17.7.1)`, one can replace `k` by an algebraically
closed extension, in other words

<!-- original page 82 -->

suppose `k` algebraically closed. The set of points of `X` rational over `k` being then dense in `X` `(10.4.8)`, one can
restrict to the case where `x` is rational over `k`. Now `(16.4.12)` `(Ω_{X/k}^1)_x ⊗_{𝒪_x} k(y)` is then `k`-isomorphic
to `𝔪_x/𝔪_x^2`, and since `𝒪_x` is a regular local ring `(17.5.1)`, `rg_k(𝔪_x/𝔪_x^2) = dim(𝒪_x)` `(0, 17.1.1)`;
therefore `rg_k(Ω_{X/k}^1)_x = dim(𝒪_x)`. But since `k(x) = k`, one has `dim_x f = dim(𝒪_x)` `(5.2.3)`. Q.E.D.

We shall prove later a converse of this result `(17.15.5)`.

**Corollary (17.10.3).**

<!-- label: IV.17.10.3 -->

*Let `f : X → Y`, `g : Y → Z` be two smooth morphisms. Then, for every `x ∈ X`, one has*

```text
  (17.10.3.1)    dim_x(g ∘ f) = dim_x f + dim_{f(x)} g.
```

Indeed, `g ∘ f` is smooth `(17.3.3)`, hence the three `𝒪_X`-Modules `Ω_{X/Y}^1`, `Ω_{X/Z}^1` and `f*(Ω_{Y/Z}^1)` are
locally free `(17.2.3` and `0_I, 5.4.5)`; in addition the rank at `x` of `f*(Ω_{Y/Z}^1)` is equal to the rank at
`y = f(x)` of `Ω_{Y/Z}^1`. Equality `(17.10.3.1)` is therefore a consequence of `(17.10.2)` and of the exactness of the
sequence `(17.2.3.1)`.

**Corollary (17.10.4).**

<!-- label: IV.17.10.4 -->

*Let `f : X → Y` be a smooth morphism, `X'` a subprescheme of `X` such that the composite morphism `X' → X → Y` (where
`j` is the canonical injection) is smooth. Then the conormal sheaf `𝒩_{X'/X}` is a locally free `𝒪_{X'}`-Module, and for
every `x ∈ X'`, one has*

```text
  (17.10.4.1)    dim_x f = dim_x(j ∘ f) + rg_{k(x)}(𝒩_{X'/X})_x.
```

Indeed, `Ω_{X/Y}^1 ⊗_{𝒪_X} 𝒪_{X'}` and `Ω_{X'/Y}^1` are both locally free and the exact sequence `(17.2.5.1)` is split
in a suitable neighbourhood of each point of `X'`, hence `𝒩_{X'/X}` is locally free (Bourbaki, _Alg. comm._, chap. II,
§5, n° 2, th. 1), and relation `(17.10.4.1)` follows immediately from the exactness of the sequence `(17.2.5.1)`.

### 17.11. Smooth morphisms of smooth preschemes

**Theorem (17.11.1).**

<!-- label: IV.17.11.1 -->

*Let `f : Y → S` and `h : X → S` be two morphisms locally of finite presentation, `g : X → Y` an `S`-morphism, `x` a
point of `X`; set `y = g(x)`, `s = f(y) = h(x)`. The following conditions are equivalent:*

*a) `f` is smooth at the point `y` and `g` is smooth at the point `x`.*

*b) `g` and `h` are smooth at the point `x`.*

*c) `h` is smooth at the point `x`, and the canonical homomorphism `(16.4.18)`*

```text
  (17.11.1.1)    (g*(Ω_{Y/S}^1))_x → (Ω_{X/S}^1)_x
```

*is left-invertible (in other words is an isomorphism onto a direct factor of `(Ω_{X/S}^1)_x`).*

*c') `h` is smooth at the point `x`, and the canonical homomorphism*

```text
  (17.11.1.2)    (Ω_{Y/S}^1 ⊗_{𝒪_Y} k(y)) ⊗_{k(y)} k(x) → (Ω_{X/S}^1)_x ⊗_{𝒪_x} k(x)
```

*is injective.*

*Suppose moreover that the homomorphism `k(y) → k(x)` is bijective. Then the preceding conditions are also equivalent to
the following:*

<!-- original page 83 -->

*d) `h` is smooth at the point `x`, and the canonical map `T_{X/S}(x) → T_{Y/S}(y)` from the tangent vector space at `x`
to `X` into the tangent vector space at `y` to `Y` `(16.5.12)` is surjective.*

The fact that a) entails b) results trivially from `(17.3.3, (ii))`; b) entails c) by application of `(17.2.3, (ii))`.
To see that c) is equivalent to c'), let us note that by virtue of `(17.2.3, (i))`, `Ω_{X/S}^1` is a locally free
`𝒪_X`-Module of finite type; it suffices then to apply `(0, 19.1.12)` to the local ring `𝒪_{X, x}` and to the
homomorphism `(17.11.1.1)` of `𝒪_{X, x}`-modules of finite type. When `k(x) = k(y)`, the tangent linear map
`T_{X/S}(x) → T_{Y/S}(y)` is the transpose of `(17.11.1.2)`, by `(16.5.12)`, which establishes in this case the
equivalence of c') and d).

It remains therefore to prove that c) entails a). One can restrict to the case where `S = Spec(A)`, `Y = Spec(B)`,
`X = Spec(C)` are affine. The hypothesis implies `(17.2.3, (i))` that `(Ω_{X/S}^1)_x ⊗_{𝒪_x} k(x)` is a free
`𝒪_x`-module: indeed `(16.10.6)` there exist elements `s_i (1 ⩽ i ⩽ r)` of `B_y = 𝒪_{Y, y}` such that the differentials
`d_{B/A}(s_i)` generate the `B`-module `Ω_{B/A}^1` and their images in `Ω_{C/A}^1` form part of a basis of this free
`C`-module. As `Ω_{Y/S}^1` (resp. `Ω_{X/S}^1`) is an `𝒪_Y`-Module (resp. an `𝒪_X`-Module) of finite presentation
`(16.4.22)`, one can, by replacing if necessary `X` and `Y` by suitable affine open neighbourhoods of `x` and `y`
respectively, suppose that `Ω_{C/A}^1` is a free `C`-module and that the `t_i` are the images of elements
`s_i (1 ⩽ i ⩽ r)` of `B` such that the `d_{B/A}(s_i)` generate the `B`-module `Ω_{B/A}^1` and their images in
`Ω_{C/A}^1` form part of a basis of this `C`-module (Bourbaki, _Alg. comm._, chap. II, §5, n° 1, prop. 2). Let `φ` be
the `A`-homomorphism of `B' = A[T_1, …, T_r]` into `B` such that `φ(T_i) = s_i` for every `i`; the corresponding
di-homomorphism `Ω_{B'/A}^1 → Ω_{B/A}^1` `(0, 20.5.2)` transforms the `d_{B'/A}(T_i)`, which form a basis of
`Ω_{B'/A}^1` `(0, 20.4.13)`, into the `d_{B/A}(s_i)` and is consequently surjective; if `Y' = Spec(B')` and if
`u : Y → Y'` is the `S`-morphism corresponding to `φ`, one concludes from `(17.2.2)` that `u` is unramified. If one
proves that the composite morphism `u ∘ g : X → Y'` is smooth at the point `x`, it will then follow from `(17.7.10)`
that `u` is étale at the point `x`, then from `(17.3.5)` that `g` is smooth at the point `x`; and finally, since the
structure morphism `f' : Y' → S` is smooth `(17.3.8)`, `f = f' ∘ u` will be smooth at the point `x`. Since the canonical
images of the `d_{B'/A}(T_i)` in `Ω_{C/A}^1` are those of the `d_{B/A}(s_i)`, they form part of a basis of `Ω_{C/A}^1`.
One thus sees that to prove that c) implies a), one can restrict to the case where `Y' = Y`, and consequently suppose
that `f` is a smooth morphism.

By virtue of `(17.8.2)`, one can then restrict to the case where `S = Spec(k)` is the spectrum of a field; further,
thanks to `(17.7.1, (ii))`, one can suppose that `k` is algebraically closed; finally, by replacing if necessary `X` and
`Y` by open neighbourhoods of `x` and `y` respectively, one can suppose that `f` and `h` are both smooth, and that the
canonical homomorphism

```text
  g*(Ω_{Y/S}^1) → Ω_{X/S}^1
```

is left-invertible `(0, 19.1.12)`. Then the set of points of `X` rational over `k` is very dense in `X` `(10.4.8)`,
hence, to prove that `g` is smooth, it suffices to prove that `g` is smooth at every point `x ∈ X` rational over `k`, or
again, that at such a point, `𝒪_{X, x}` is a flat `𝒪_y`-module and `𝒪_{X, x}/𝔪_y 𝒪_{X, x}` is a regular ring `(17.5.1)`.
Now, `y = g(x)` is

<!-- original page 84 -->

a fortiori rational over `k`, and since `𝒪_{Y, y}` is then a `k`-algebra formally smooth for the discrete topologies and
`𝒪_{Y, y}/𝔪_y = k`, it follows from `(0, 20.5.14)` that the canonical homomorphism
`𝔪_y/𝔪_y^2 → (Ω_{Y/S}^1)_y ⊗_{𝒪_y} k(y)` is bijective; likewise, the canonical homomorphism
`𝔪_x/𝔪_x^2 → (Ω_{X/S}^1)_x ⊗_{𝒪_x} k(x)` is bijective. The hypothesis c'), equivalent to c), signifies therefore here
that the canonical homomorphism

```text
  (𝔪_y/𝔪_y^2) ⊗_{k(y)} k(x) → 𝔪_x/𝔪_x^2
```

is injective. Since the ring `𝒪_{X, x}` is regular, the conclusion follows from `(0, 17.3.3)`. Q.E.D.

**Corollary (17.11.2).**

<!-- label: IV.17.11.2 -->

*Under the general hypotheses of `(17.11.1)`, the following conditions are equivalent:*

*a) `f` is smooth at the point `y` and `g` is étale at the point `x`.*

*b) `h` is smooth at the point `x` and `g` is étale at the point `x`.*

*c) `h` is smooth at the point `x`, and the canonical homomorphism*

```text
  (g*(Ω_{Y/S}^1))_x → (Ω_{X/S}^1)_x
```

*is bijective.*

*c') `h` is smooth at the point `x`, and the canonical homomorphism*

```text
  (Ω_{Y/S}^1 ⊗_{𝒪_Y} k(y)) ⊗_{k(y)} k(x) → (Ω_{X/S}^1)_x ⊗_{𝒪_x} k(x)
```

*is bijective.*

*Suppose moreover that the homomorphism `k(y) → k(x)` is bijective. Then the preceding conditions are also equivalent to
the following:*

*d) `h` is smooth at the point `x`, and the canonical map `T_{X/S}(x) → T_{Y/S}(y)` `(16.5.12)` is bijective.*

Each of the conditions a), b), c) of `(17.11.2)` is equivalent to the conjunction of the corresponding condition of
`(17.11.1)` and the fact that `g` is unramified at the point `x`, taking into account `(17.2.2)` for what concerns
condition c); whence the equivalence of a), b) and c). The equivalence of c) and c') results from the equivalence of the
corresponding conditions of `(17.11.1)` and from Nakayama's lemma; the equivalence of c') and d) when `k(x) = k(y)` is
immediate by transposition `(16.5.12)`.

**Corollary (17.11.3).**

<!-- label: IV.17.11.3 -->

*Let `h : X → S` be a smooth morphism, `s_i (1 ⩽ i ⩽ r)` sections of `𝒪_X` above `X` (which are also sections of
`h*(𝒪_X)` above `S`), `g : X → S[T_1, …, T_r] = V_S` the `S`-morphism corresponding to the homomorphism of `𝒪_S`-Modules
`𝒪_S^r → h*(𝒪_X)` defined by these sections `(II, 1.2.7)`. For `g` to be smooth (resp. étale) at a point `x ∈ X`, it is
necessary and sufficient that the `(d_{X/S}(s_i))_x` form part of a basis (resp. constitute a basis) of the `𝒪_x`-module
`(Ω_{X/S}^1)_x`.*

It suffices to apply `(17.11.1)` (resp. `(17.11.2)`) taking for `f` the structure morphism `S[T_1, …, T_r] → S`.

**Corollary (17.11.4).**

<!-- label: IV.17.11.4 -->

*For a morphism `h : X → S` to be smooth at a point `x ∈ X`, it is necessary and sufficient that there exist an open
neighbourhood `U` of `x`, an integer `r`, and an étale `S`-morphism `U → S[T_1, …, T_r]`.*

<!-- original page 85 -->

The condition is evidently sufficient since the structure morphism `S[T_1, …, T_r] → S` is smooth `(17.3.8)`. To show
that it is necessary, let us note that since `h` is smooth at the point `x`, there exists an open neighbourhood `U` of
`x` such that `Ω_{X/S}^1 | U` is locally free `(17.2.3)`; it then suffices to use `(16.10.6)` to obtain (by restricting
`U` if necessary) sections `s_i` of `𝒪_X` above `U` such that the `d_{X/S}(s_i)` form a basis of `Ω_{X/S}^1 | U`; one
concludes by applying `(17.11.3)`.

**Proposition (17.11.5).**

<!-- label: IV.17.11.5 -->

*Let `f : Y → S`, `h : X → S` be two smooth morphisms. For an `S`-morphism `g : X → Y` to be an open immersion, it is
necessary and sufficient that `g` be a monomorphism of preschemes and that for every `x ∈ X`, setting `y = g(x)`, one
have `dim_x(f) = dim_y(h)` (for a generalization of this proposition, see `(18.10.5)`).*

The condition is evidently necessary; let us prove that it is sufficient.

By virtue of `(17.9.5)`, one is immediately reduced to the case where `S = Spec(k)` is the spectrum of a field, and by
virtue of `(2.7.1, (x))`, one can suppose `k` algebraically closed. Taking into account `(17.9.1)`, it then suffices to
prove that `g` is étale, and since the set of points where `g` is étale is open, it suffices to show that `g` is étale
at the closed points (or again, those rational over `k`) of `X` `(10.4.8)`. Let `x` be such a point, and set `y = g(x)`,
which is also rational over `k`; by hypothesis, the ring `A = 𝒪_{Y, y}` is regular and of residue field `k`; let
`d = dim(A)` and `(t_i)_{1 ⩽ i ⩽ d}` a regular system of parameters for `A`. Set `B = 𝒪_{X, x}`, `C = B/𝔪_y B`. Since
`g` is a monomorphism, so is the morphism `Spec(C) → Spec(k(y)) = Spec(k)` deduced from `g` by base change
`(I, 3.3.12)`; but this means that the corresponding homomorphism `u : k → C` is surjective (hence bijective), for `u`
admits a left inverse `v : C → k`, and `u ∘ v` and the identity of `C`, composed with `u`, give the same morphism
`u : k → C`. As by hypothesis `B` is a regular ring of dimension `d`, the images of the `t_i` in `B` form a regular
system of parameters for `B` `(0, 17.1.7)`; condition `(17.6.3, e″)` is therefore verified by `g` at the point `x`
`(0, 17.1.1` and Bourbaki, _Alg. comm._, chap. III, §2, n° 8, cor. 3 of th. 1), which completes the proof.

### 17.12. Smooth subpreschemes of a smooth prescheme. Smooth morphisms and differentially smooth morphisms

**Theorem (17.12.1).**

<!-- label: IV.17.12.1 -->

*Let `f : X → S`, `h : Y → S` be two morphisms locally of finite presentation, `j : Y → X` an immersion, `y` a point of
`Y`, `x = j(y)`. The following conditions are equivalent:*

*a) `h` is smooth at the point `y` and `f` is smooth at the point `x`.*

*b) `f` is smooth at the point `x`, and the canonical homomorphism `(16.4.21)`*

```text
  (𝒩_{Y/X})_y → (j*(Ω_{X/S}^1))_y
```

*is left-invertible.*

*c) `h` is smooth at the point `y` and there exists an open neighbourhood `U` of `y` in `Y` such that `j | U : U → X` is
a regular immersion `(16.9.2)`.*

<!-- original page 86 -->

*c') `h` is smooth at the point `y` and there exists an open neighbourhood `U` of `y` in `Y` such that `j | U : U → X`
is a quasi-regular immersion (in other words `(16.9.8)`, there exists a neighbourhood `U` of `y` in `Y` in which
`𝒩_{Y/X}` is a locally free `𝒪_Y`-Module and the canonical homomorphism `S_{𝒪_Y}^•(𝒩_{Y/X}) → 𝒢ℛ_•(j)` is bijective).*

To prove the equivalence of a) and b), one can restrict to the case where `S = Spec(A)` and `X = Spec(B)` are affine,
with `Y = Spec(B/𝔧)`, where `𝔧` is an ideal of finite type of `B`, and `B` is a smooth `A`-algebra `(17.3.2, (ii))`. It
then suffices to apply the Jacobian criterion `(0, 22.6.1)` as well as `(0, 19.1.14)`, taking into account that
`Ω_{X/S}^1` is a locally free `𝒪_X`-Module in a neighbourhood of `x` and `𝒩_{Y/X}` an `𝒪_Y`-Module of finite type
`(16.1.6)`.

In the second place, let us prove that a) entails c'). One can again restrict to the case where `S`, `X`, `Y` are
affine, `B` and `B/𝔧` smooth `A`-algebras, and it then follows from `(17.7.9)` and `(8.10.5, (iv))` that there exist a
Noetherian subring `A'` of `A`, an `A'`-algebra of finite type `B'` and an ideal `𝔧'` of `B'` such that
`B = B' ⊗_{A'} A`, `𝔧 = 𝔧' B` and `B'` and `B'/𝔧'` are smooth `A'`-algebras. Let us note that, by `(0, 19.3.8)`, `B'` is
still a formally smooth `A'`-algebra when one endows `A'` with the discrete topology and `B'` with the `𝔧'`-preadic
topology. Consequently `(0, 19.5.4)`, `𝔧'/𝔧'^2` is a `(B'/𝔧')`-projective module and the canonical homomorphism
`S_{B'/𝔧'}^•(𝔧'/𝔧'^2) → gr_{𝔧'}^•(B')` is bijective. In other words `(16.9.8)`, the immersion `Spec(B'/𝔧') → Spec(B')`
is quasi-regular, hence regular since `B'` is Noetherian `(16.9.10)`. But since by hypothesis `B'/𝔧'` is a flat
`A'`-module `(17.5.1)` and `B'` an `A'`-algebra of finite presentation, one can apply `(11.3.8)` by replacing `f` by
`𝔧'`, and one therefore sees (by base change) that `j` is a regular immersion, and a fortiori quasi-regular. The fact
that `B` is an `A`-algebra of finite presentation and a flat `A`-module shows moreover, by virtue of `(11.3.8)`, that
conditions c') and c) are equivalent, and are stable under base change.

Let us finally show that c) entails a). From the fact that, in `(11.3.8)`, condition b) entails c), one already sees
that if c) is verified, `f` is flat at the point `x`; by virtue of `(17.5.1)`, everything reduces to seeing that under
hypothesis c), `f⁻¹(s)` is smooth over `k(s)` at the point `x`, setting `s = h(x)`; as one has remarked that condition
c) is stable under base change, one sees that one is reduced to the case where `S = Spec(k)` is the spectrum of a field,
and taking into account `(17.7.1, (ii))` one can suppose that `k` is algebraically closed. It then suffices to prove
that `𝒪_{X, x}` is a regular ring `(17.5.1)`. Now, by hypothesis one has `𝒪_{Y, y} = 𝒪_{X, x}/𝔧_x`, where `𝔧_x` is an
ideal generated by an `𝒪_{X, x}`-regular sequence `(t_i)`, and `𝒪_{Y, y}` is a regular ring; since the `t_i` form part
of a system of parameters for `𝒪_{X, x}` `(0, 16.4.1)`, the conclusion follows from `(0, 17.1.7)`.

**Corollary (17.12.2).**

<!-- label: IV.17.12.2 -->

*With the notations of `(17.12.1)`, suppose that `f` is smooth at the point `x`, and let `Y` be a closed subprescheme of
`X` defined by an Ideal `𝓘` of `𝒪_X`, and `S`-smooth at the point `x`. Let `g_i (1 ⩽ i ⩽ r)` be sections of `𝓘` above
`X`. The following conditions are equivalent:*

*a) The `(g_i)_x` form a system of generators of the `𝒪_{X, x}`-module `𝓘_x` whose number of elements is the smallest
possible.*

*b) If `g_i'` is the canonical image of `g_i` in `Γ(X, 𝓘/𝓘^2)`, the `(g_i')_x` form a basis of the `(𝒪_{Y, x})_x`-module
`(𝓘/𝓘^2)_x`.*

<!-- original page 87 -->

*c) The images of the `d_{X/S}(g_i)` in `(Ω_{X/S}^1)_x ⊗_{𝒪_x} k(x)` are `k(x)`-linearly independent elements, and the
`(g_i)_x` generate `𝓘_x`.*

*d) There exists an open neighbourhood `U` of `x` in `X` and sections `g_j (r + 1 ⩽ j ⩽ n)` of `𝒪_X` above `U` such that
the `S`-morphism `u : U → S[T_1, …, T_n]` corresponding to the homomorphism `𝒪_S^n → h*(𝒪_U)` defined by the sections
`g_i | U (1 ⩽ i ⩽ r)` and `g_j (r + 1 ⩽ j ⩽ n)` `(II, 1.2.7)` is an étale morphism, and that the inverse image of the
subprescheme `Y' = S[T_{r+1}, …, T_n]` under this morphism is the prescheme induced by `j(Y)` on the open `U ∩ j(Y)`.*

Since `(g_i')_x` is the canonical image of `(g_i)_x`, the equivalence of a) and b) results from Nakayama's lemma, `𝓘_x`
being of finite type and `𝓘_x/𝓘_x^2` an `(𝒪_{X, x}/𝓘_x)`-free module `(17.10.4)` (Bourbaki, _Alg. comm._, chap. II, §3,
n° 2, prop. 5). By virtue of `(17.12.1, b))`, `𝓘_x/𝓘_x^2` is canonically identified with a direct factor of the
`(𝒪_{X, x}/𝓘_x)`-free module of rank `n`, `(Ω_{X/S}^1)_x ⊗_{𝒪_x} (𝒪_{X, x}/𝓘_x)`, and the equivalence of b) and c)
results from Bourbaki, _loc. cit._. Moreover, if a) is verified, `(g_i')_x` is thus identified with
`(d_{X/S}(g_i))_x ⊗ 1` for `1 ⩽ i ⩽ r`; the `𝒪_{X, x}`-module `(Ω_{X/S}^1)_x` being free of rank `n`, it follows again
from Bourbaki, _loc. cit._, that by replacing if necessary `X` by an open neighbourhood of `x`, one can suppose that
there exist `n − r` sections `g_j (r + 1 ⩽ j ⩽ n)` of `𝒪_X` above `X`, such that the `(d_{X/S}(g_i))_x` for `1 ⩽ i ⩽ n`
form a basis of `(Ω_{X/S}^1)_x`; the fact that the corresponding morphism `u` is étale at the point `x` then results
from `(17.11.3)`; for the same reason, the morphism `u⁻¹(Y') → Y'`, restriction of `u`, is étale at the point `x`; by
replacing `X` by a neighbourhood of `x`, one can suppose these two morphisms étale. Moreover, it is immediate that `Y`
(identified, for simplicity, with the closed subprescheme `j(Y)` of `X`) is a closed subprescheme of `u⁻¹(Y')`, and by
virtue of the choice of the `g_j` for `j > r` and of `(17.2.5)` and `(17.11.2)`, the restriction to `Y` of `u` can again
be supposed étale. One deduces that for every `y' ∈ Y'`, the immersion `Y ∩ u⁻¹(y') → u⁻¹(y')` is open, whence one
concludes by means of `(17.9.6)` that `Y → u⁻¹(Y')` is an open immersion; this proves that a) entails d). The converse
follows at once from `(17.11.3)`.

**Corollary (17.12.3).**

<!-- label: IV.17.12.3 -->

*Let `f : X → S` be a morphism locally of finite presentation, `u : S → X` an `S`-section of `X`. For `f` to be smooth
at a point `x ∈ X`, it is necessary and sufficient that `u` be a quasi-regular immersion in a neighbourhood of
`s = f(x)`.*

The conclusion follows from `(17.12.1)`, since `f ∘ u = 1_S` is smooth.

**Proposition (17.12.4).**

<!-- label: IV.17.12.4 -->

*Every smooth morphism `f : X → S` is differentially smooth (in other words `(16.10.5)` `Δ_f : X → X ×_S X` is a
quasi-regular immersion). In particular, the `Ω_{X/S}^n` and the `gr_n(𝒩_{X/X ×_S X})` are locally free `𝒪_S`-Modules of
finite type.*

It suffices to remark that the structure morphism `p_2 : X ×_S X → X` is smooth `(17.3.3, (iii))` and that `Δ_f` is an
`X`-section for `p_2`; the conclusion follows from `(17.12.3)`.

**Proposition (17.12.5).**

<!-- label: IV.17.12.5 -->

*Let `f : X → Y` be a morphism locally of finite presentation. The following conditions are equivalent:*

*a) `f` is differentially smooth.*

*b) For every morphism `g : Y' → Y`, if one sets `X' = X ×_Y Y'` and `f' = f_{(Y')} : X' → Y'`, then, for every
`Y'`-section `s'` of `X'`, `f'` is smooth at all points of `s'(Y')`.*

*c) The second projection `p_2 : X ×_Y X → X` is smooth at all points of the diagonal `Δ_f(X)`.*

<!-- original page 88 -->

Condition c) is a particular case of b): it suffices indeed to take `Y' = X` and `g = f` in b), for then `f'` is none
other than the second projection `p_2`, and `Δ_f` is an `X`-section of `X ×_Y X`. In the second place, c) entails a),
for `p_2` is a morphism locally of finite presentation, and if `p_2` is smooth at the points of `Δ_f(X)`, `Δ_f` is a
quasi-regular immersion `(17.12.3)`, hence `f` is differentially smooth. Finally, let us show that a) entails b); if
`Δ_f` is a quasi-regular immersion, `p_2` is smooth at all points of `Δ_f(X)` `(17.12.3)`. Now, if `g' : X' → X` is the
canonical projection, and `v = (g', g)_{Y'} : X' → X ×_Y X`, one verifies at once that the diagram

```text
                              v
            X ×_Y X  ←——————  X'

              p_2              f'

              X    ←——————    Y'
                   h = g' ∘ s'
```

is commutative and identifies `X'` with the product `(X ×_Y X) ×_X Y'` `(I, 3.3.9)`; taking into account that the
diagram `(17.4.1.1)` identifies `Y'` with the product of the `(X ×_Y X)`-preschemes `X` and `X'`, one concludes, from
the fact that `p_2` is smooth at every point of `Δ_f(X)`, that `f'` is smooth at every point of `s'(Y')`
`(17.3.3, (iii))`.

**Corollary (17.12.6).**

<!-- label: IV.17.12.6 -->

*The notations being those of `(8.8.1)`, suppose `X_α` quasi-compact, and `f_α : X_α → S_α` locally of finite
presentation. For `f : X → S` to be differentially smooth, it is necessary and sufficient that there exist `λ ⩾ α` such
that `f_λ : X_λ → S_λ` be differentially smooth (in which case `f_μ : X_μ → S_μ` is differentially smooth for `μ ⩾ λ`).*

The sufficiency of the condition and the last assertion result from `(16.10.4)`. To prove that the condition is
necessary, let us note that `Δ_f : X → X ×_S X` and `p_2 : X ×_S X → X` are deduced by base change from
`Δ_{f_α} : X_α → X_α ×_{S_α} X_α` and `p_{2, α} : X_α ×_{S_α} X_α → X_α`. By virtue of `(17.12.5)`, for every
`z ∈ Δ_f(X)`, there exists an affine open neighbourhood `U(z)` of `z` in `X ×_S X` such that `p_2` is smooth in `U(z)`;
by virtue of `(8.2.11)` and `(17.7.8)`, there exists an index `λ(z)` and a neighbourhood `U_{λ(z)}` of the projection of
`z` in `X_{λ(z)} ×_{S_{λ(z)}} X_{λ(z)}` such that `U(z)` is the inverse image of `U_{λ(z)}`, and such that `p_{2, λ(z)}`
is smooth in `U_{λ(z)}`. As `X` is quasi-compact, one can cover `Δ_f(X)` by a finite number of neighbourhoods `U(z_i)`;
by virtue of `(8.3.4)`, there exists a `λ` greater than all the `λ(z_i)` such that the inverse images of the
`U_{λ(z_i)}` in `X_λ ×_{S_λ} X_λ` form a cover of `Δ_{f_λ}(X_λ)`; it then follows from `(17.12.5)` that this index `λ`
answers the question.

**Example (17.12.7).**

<!-- label: IV.17.12.7 -->

*Let `S` be a prescheme, `G` an `S`-prescheme in groups, locally of finite presentation over `S`. Then, for `G` to be
differentially smooth, it is necessary and sufficient that `G` be smooth over `S` at the points of the "unit section"
`e` of `G`.*

The condition is indeed necessary by `(17.12.5)`. Conversely, suppose it satisfied; for every morphism `S' → S`,
`G' = G ×_S S'` is then an `S'`-prescheme in groups locally of finite presentation over `S'`; one can therefore, by
virtue of `(17.12.5)`, restrict to proving that for every `S`-section `s` of `G`, `f` is smooth at the points of `s(S)`.
Now, if `m : G ×_S G → G` is the morphism which defines the structure of prescheme in groups of `G`,
`m ∘ (s × 1_G) : S ×_S G → G ×_S G → G` is an

<!-- original page 89 -->

`S`-isomorphism of the prescheme `G`, the "left translation" `T_s`, transforming the points of the unit section of `G`
into the points of `s(S)`; one concludes that `G` is smooth over `S` at the points of `s(S)`.

**Remark (17.12.8).**

<!-- label: IV.17.12.8 -->

*An `S`-prescheme in groups `G`, of finite type (and even finite) over a locally Noetherian prescheme `S`, can be
differentially smooth over `S` without being smooth (nor even flat) over `S`. Take for example for `S` the spectrum of
the algebra of dual numbers `D = k[T]/T^2 k[T]` over a field `k`, for `G` the spectrum of the `D`-algebra direct
composite `E = D ⊕ k`. One defines on `G` a structure of `S`-scheme in groups by defining a "diagonal map" `δ`,
homomorphism of `E` into `E ⊗_D E`: if `e'`, `e″` are the idempotents, canonical images of the unit `1` of `D` in the
factors `D` and `k` of `E`, one verifies without difficulty that one obtains such a diagonal map by taking
`δ(e') = e' ⊗ e' + e″ ⊗ e″` and `δ(e″) = e' ⊗ e″ + e″ ⊗ e'`. The unit section of the scheme in groups `G` corresponds to
the homomorphism `E → D` which is the identity on `D` and `0` on `k`; it is an isomorphism of `S` onto a connected
component of `G`, and a fortiori `G` is differentially smooth over `S` `(17.12.6)`, but it is clear that `G` is not
`S`-flat.*

### 17.13. Transversal morphisms

**(17.13.1)** Let `S` be a prescheme, `X`, `Y`, `X'` three `S`-preschemes, `i : Y → X` an `S`-immersion, `f : X' → X` an
`S`-morphism. Set `Y' = Y ×_X X'`, and let `g : Y' → Y`, `j : Y' → X'` be the canonical projections, so that one has the
commutative diagram

```text
  (17.13.1.1)    Y  ←———  Y'

                 X  ←———  X'
                       f
```

and that `j` is an `S`-immersion. One then has a commutative diagram of quasi-coherent `𝒪_{Y'}`-Modules

```text
  (17.13.1.2)
                  g*(𝒩_{Y/X})  ———→  g*(Ω_{X/S}^1 ⊗ 𝒪_Y)  ———→  g*(Ω_{Y/S}^1)  ———→  0
                       gr_1(g)            ↓                       ↓

                  𝒩_{Y'/X'}    ———→  Ω_{X'/S}^1 ⊗ 𝒪_{Y'}    ———→  Ω_{Y'/S}^1    ———→  0
```

where the lower row is the exact sequence `(16.4.21)` applied to `j`, the upper row comes from the same exact sequence
for `i`, by application of the right-exact functor `g*` (which therefore leaves it exact); `gr_1(g)` is defined in
`(16.2.1)`, and the commutativity of the two squares results from `(0, 20.5.7.3)` and `(0, 20.5.11.3)`.

<!-- original page 90 -->

One has seen moreover `(16.2.2, (iii))` that `gr_1(g)` is here surjective, hence one deduces from `(17.13.1.2)` the
exact sequence

```text
  (17.13.1.3)    g*(𝒩_{Y/X}) ⟶^α Ω_{X'/S}^1 ⊗ 𝒪_{Y'} ⟶ Ω_{Y'/S}^1 ⟶ 0.
```

**Proposition (17.13.2).**

<!-- label: IV.17.13.2 -->

*The notations being those of `(17.13.1)`, let `x'` be a point of `Y'`, `x = g'(x')` its image in `Y`; suppose `X` and
`Y` smooth over `S` at the point `x`, `X'` smooth over `S` at the point `x'`. Let `m`, `m − c` be the relative
dimensions of `X` and `Y` over `S` at the point `x` `(17.10.1)`, and let `n` be the relative dimension of `X'` over `S`
at the point `x'`. The following conditions are equivalent:*

*a) `Y'` is smooth over `S` at the point `x'` and of relative dimension `n − c`.*

*b) The homomorphism `α ⊗ 1 : g*(𝒩_{Y/X}) ⊗_{𝒪_{Y'}} k(x') → Ω_{X'/S}^1 ⊗_{𝒪_{X'}} k(x')` deduced from the homomorphism
`α` of `(17.13.1.3)` is injective.*

*Let `s` be the canonical image of `x` in `S`, and suppose that `x'` is rational over `k(s)`. Then conditions a) and b)
are also equivalent to the following:*

*b') The homomorphism transpose of `α ⊗ 1`*

```text
  T_{X'/S}(x') → (𝒩_{Y/X} ⊗ k(x'))* = T_{X/S}(x)/T_{Y/S}(x)
```

*(cf. `(16.5.12)`) is surjective.*

*Moreover, when conditions a) and b) are verified at `x'`, they are so in a neighbourhood of `x'` in `Y'`; by replacing
if necessary `X'` by a neighbourhood of `x'`, the homomorphism*

```text
  gr_1(g) : g*(𝒩_{Y/X}) → 𝒩_{Y'/X'}
```

*is bijective, and the sequence*

```text
  (17.13.2.1)    0 ⟶ g*(𝒩_{Y/X}) ⟶ Ω_{X'/S}^1 ⊗ 𝒪_{Y'} ⟶ Ω_{Y'/S}^1 ⟶ 0
```

*obtained by adjoining a `0` to `(17.13.1.3)`, is exact.*

The fact that if the equivalent conditions a) and b) are verified at the point `x'`, they are so also in a neighbourhood
of `x'` in `Y'`, results from the fact that the set of points where a morphism is smooth is open `(17.3.7)` and from
`(17.10.2)`.

By virtue of `(17.12.1)` applied to `X'` and `Y'`, to say that `Y'` is smooth over `S` at the point `x'` amounts to
saying that the homomorphism

```text
  δ ⊗ 1 : 𝒩_{Y'/X'} ⊗_{𝒪_{Y'}} k(x') → Ω_{X'/S}^1 ⊗_{𝒪_{X'}} k(x')
```

is injective, taking into account `(0, 19.1.12)` and the fact that `Ω_{X'/S}^1` is a locally free `𝒪_{X'}`-Module at the
point `x'` `(17.2.3)`; since `Ω_{Y'/S}^1` is then also a locally free `𝒪_{Y'}`-Module in a neighbourhood of `x'` and the
sequence

```text
  (17.13.2.2)    0 → 𝒩_{Y'/X'} → Ω_{X'/S}^1 ⊗ 𝒪_{Y'} → Ω_{Y'/S}^1 → 0
```

is exact `(17.2.5)`, to say that `Y'` is of relative dimension `n − c` over `S` at the point `x'` signifies, by
`(17.10.2)`, that `𝒩_{Y'/X'}` (which is locally free in a neighbourhood of `x'`) is of rank `c` at the point `x'`. But
by virtue of the hypotheses on `X` and `Y` at the point `x`, and by the same reasoning, `𝒩_{Y/X}` is locally free and of
rank `c` at the point `x`, hence `g*(𝒩_{Y/X})` is also locally free and of rank `c` at the point `x'`. As the
homomorphism `gr_1(g) : g*(𝒩_{Y/X}) → 𝒩_{Y'/X'}` is surjective, the preceding conditions are equivalent to saying that
this homomorphism is

<!-- original page 91 -->

bijective at the point `x'` (Bourbaki, _Alg. comm._, chap. II, §3, n° 2, cor. of prop. 6), hence also in a neighbourhood
of `x'` `(0_I, 5.2.7)`; this evidently entails b), as well as the last assertion of the statement, by virtue of the
exactness of `(17.13.2.2)`. Conversely, since `α ⊗ 1` factors as

```text
  g*(𝒩_{Y/X}) ⊗ k(x') ⟶^{gr_1(g) ⊗ 1} 𝒩_{Y'/X'} ⊗ k(x') ⟶^{δ ⊗ 1} Ω_{X'/S}^1 ⊗ k(x')
```

and `gr_1(g)` is surjective, to say that `α ⊗ 1` is injective entails that `δ ⊗ 1` is and that `gr_1(g) ⊗ 1` is
bijective. One concludes `(17.12.1)` that `Y'` is smooth over `S` at the point `x'`, and that `gr_1(g)` is bijective in
a neighbourhood of `x'` (Bourbaki, _loc. cit._). Moreover, since the sequence `(17.13.2.2)` is then exact, and
`𝒩_{Y'/X'}`, isomorphic to `g*(𝒩_{Y/X})`, is of rank `c` at the point `x'`, `Ω_{Y'/S}^1` is of rank `n − c` at this
point, which completes the proof of the equivalence of a) and b), by virtue of `(17.10.2)`.

It remains to show the equivalence of b) and b') when `x'` is rational over `k(s)` (which implies that the same holds
for `x`); then `g*(𝒩_{Y/X}) ⊗_{𝒪_{Y'}} k(x')` is identified with `𝒩_{Y/X} ⊗_{𝒪_Y} k(x)`, and since the sequence

```text
  0 → 𝒩_{Y/X} → Ω_{X/S}^1 ⊗ 𝒪_Y → Ω_{Y/S}^1 → 0
```

is exact at the point `x` and formed of `𝒪_Y`-Modules locally free, the dual of `𝒩_{Y/X} ⊗_{𝒪_Y} k(x)` is identified
with the quotient space `T_{X/S}(x)/T_{Y/S}(x)` `(16.5.12)`; whence the equivalence of b) and b').

**Definition (17.13.3).**

<!-- label: IV.17.13.3 -->

*With the notations of `(17.13.1)`, one says that the morphism `f` is **transversal to `Y` at the point `x'`, relative
to `S`**, if `X` and `Y` are smooth over `S` at the point `x`, `X'` smooth over `S` at the point `x'`, and if the
equivalent conditions a), b) of `(17.13.2)` are satisfied.*

When no confusion is to be feared, one suppresses the mention of the prescheme `S` and one simply says that `f` is
**transversal to `Y` at the point `x'`**.

**Remarks (17.13.4).** — (i) Suppose that `X`, `Y` and `X'` are flat and locally of finite presentation over `S`. For
every `s ∈ S`, let us note `X_s`, `Y_s`, `X'_s`, `Y'_s` the fibres of `X`, `Y`, `X'`, `Y'` at the point `s`,
`f_s : X'_s → X_s` the morphism deduced from `f` by base change. It then follows from `(17.5.9)` that for `f` to be a
morphism transversal to `Y` at the point `x'`, it is necessary and sufficient that, if `s` is the image of `x` in `S`,
`f_s` be transversal to `Y_s` at the point `x'`, relative to `k(s)`.

(ii) One has seen in `(17.13.2)` that the set of points `x' ∈ Y'` where `f` is transversal to `Y` is open in `Y'`; if
`Y'` is moreover proper over `S`, one deduces that the set of `s ∈ S` such that `f` be transversal to `Y` at all points
of `Y'_s`, relative to `S`, is open in `S`. When `X`, `Y` and `X'` are flat and locally of finite presentation over `S`,
it follows from (i) that the set of `x' ∈ Y'` such that `f_s` be transversal to `Y_s` at the point `x'` (`s` image of
`x'` in `S`), relative to `k(s)`, is open in `Y'`. If moreover `Y'` is proper over `S`, the set of `s ∈ S` such that
`f_s` be transversal to `Y_s` at all points of `Y'_s` (relative to `k(s)`) is open in `S`.

(iii) The property of being smooth over `S`, as well as the notion of relative dimension at a point with respect to `S`,
being stable under any base change `S' → S` (`(17.3.3)` and `(4.2.7)`), the same is true of the property for a morphism
`f : X' → X` of being transversal to a subprescheme of `X` at a point, relative to `S`.

<!-- original page 92 -->

(iv) Condition b) of `(17.13.2)` expresses again that the homomorphism `α : g*(𝒩_{Y/X}) → Ω_{X'/S}^1 ⊗_{𝒪_{X'}} 𝒪_{Y'}`
is universally injective relative to `Y'` `(11.9.18)`.

**(17.13.5)** Let us now consider a prescheme `S`, three `S`-preschemes `X`, `Y`, `Z`, two `S`-morphisms `f : Y → X`,
`g : Z → X`; set `T = Y ×_X Z`; one knows then `(I, 5.3.5)` that one has a commutative diagram

```text
  (17.13.5.1)
                            X    ←———  Y ×_X Z = T

                            Δ                ↓ u

                       X ×_S X  ←———  Y ×_S Z
```

making `T` the product of the `(X ×_S X)`-preschemes `X` and `Y ×_S Z`, where `u = f ×_S g`. As `Δ` is an `S`-immersion
`(I, 5.3.9)`, one is in the situation of the diagram `(17.13.1.1)`; what corresponds to `Ω_{X/S}^1` in `(17.13.1)` is
then `(Ω_{Y/S}^1 ⊗ 𝒪_T) ⊕ (Ω_{Z/S}^1 ⊗ 𝒪_T)` by virtue of `(16.4.23)`. On the other hand, what corresponds to the
`𝒪_Y`-Module `𝒩_{Y/X}` in `(17.13.1)` is here by definition `Ω_{X/S}^1` `(16.3.1)`; there corresponds therefore to
`(17.13.1.3)` an exact sequence

```text
  (17.13.5.2)    Ω_{X/S}^1 ⊗ 𝒪_T ⟶^ρ (Ω_{Y/S}^1 ⊗ 𝒪_T) ⊕ (Ω_{Z/S}^1 ⊗ 𝒪_T) ⟶^σ Ω_{T/S}^1 ⟶ 0
```

where it remains to make precise the homomorphisms `ρ` and `σ`. Taking into account first `(16.4.23)` and `(0, 20.5.2)`,
one sees that if `p : T → Y`, `q : T → Z` are the canonical projections, one has, with the notations of `(16.4.19)`,

```text
  (17.13.5.3)    σ = h_{T/Y/S} + h_{T/Z/S}.
```

On the other hand, to evaluate `ρ`, let us use the commutativity of the left square in `(17.13.1.2)`, which, in the
present case, reduces first to making explicit the canonical homomorphism

```text
  ρ' : Ω_{X/S}^1 → Ω_{(X ×_S X)/S}^1 ⊗_{𝒪_{X ×_S X}} 𝒪_X
```

defined in `(16.4.21)` applied to the immersion `Δ`. One can restrict to the case where `S = Spec(A)`, `X = Spec(B)` are
affine, and then `ρ'` corresponds to the homomorphism `δ` of `(0, 20.5.11.2)`, where one must replace `B` by `B ⊗_A B`
and `C` by `B = (B ⊗_A B)/𝔧_{B/A}`. One then sees that `δ` carries the class of `x ⊗ 1 − 1 ⊗ x` mod. `𝔧_{B/A}` (for an
`x ∈ B`) to the image of

```text
  (x ⊗ 1 − 1 ⊗ x) ⊗ (1 ⊗ 1) − (1 ⊗ 1) ⊗ (x ⊗ 1 − 1 ⊗ x)
```

in `Ω_{(B ⊗_A B)/A}^1 ⊗_{B ⊗_A B} B`, but the preceding element can be written

```text
  ((x ⊗ 1) ⊗ (1 ⊗ 1) − (1 ⊗ 1) ⊗ (x ⊗ 1)) − ((1 ⊗ x) ⊗ (1 ⊗ 1) − (1 ⊗ 1) ⊗ (1 ⊗ x))
```

and one therefore sees that `ρ'` is the difference of the two homomorphisms `π_1` and `π_2` of `Ω_{X/S}^1` into
`Ω_{(X ×_S X)/S}^1 ⊗_{𝒪_{X ×_S X}} 𝒪_X`, corresponding respectively to the first and the second projection of `X ×_S X`
into `X`, by `(16.4.3.3)`. To obtain `ρ`, one must first

<!-- original page 93 -->

consider the homomorphism `ρ″ : Ω_{(X ×_S X)/S}^1 ⊗_{𝒪_{X ×_S X}} 𝒪_{Y ×_S Z} → Ω_{(Y ×_S Z)/S}^1` corresponding by
`(16.4.3.3)` to the morphism `u` of `(17.13.5.1)`, then, after tensorization by `𝒪_T`, form the composite
`(ρ″ ⊗ 1) ∘ (ρ' ⊗ 1)`; it follows from what precedes that one has, with the notations of `(16.4.18)`

```text
  (17.13.5.4)    ρ = (h_{Y/X/S} ⊗ 1_{𝒪_T}, −h_{Z/X/S} ⊗ 1_{𝒪_T}).
```

This said, the application of `(17.13.2)` to the situation of the diagram `(17.13.5.1)` (taking into account
`(17.3.3, (iv))`, which implies that `X ×_S X` is smooth over `S` at `x` if `X` is so) gives the

**Corollary (17.13.6).**

<!-- label: IV.17.13.6 -->

*Let `S` be a prescheme, `X`, `Y`, `Z` three `S`-preschemes, `f : Y → X`, `g : Z → X` two `S`-morphisms; set
`T = Y ×_X Z`, and let `p : T → Y`, `q : T → Z` be the canonical projections. Let `t` be a point of `T`, `y = p(t)`,
`z = q(t)`, `x = f(y) = g(z)`. Suppose that `X` is smooth over `S` at the point `x`, of relative dimension `m`, `Y`
(resp. `Z`) smooth over `S` at the point `y` (resp. `z`), of relative dimension `m + a` (resp. `m + b`), `a` and `b`
being positive or negative. Then the following conditions are equivalent:*

*a) `T` is smooth over `S` at the point `t`, of relative dimension `m + a + b`.*

*b) The homomorphism*

```text
  ρ ⊗ 1 : Ω_{X/S}^1 ⊗_{𝒪_X} k(x) → (Ω_{Y/S}^1 ⊗_{𝒪_Y} k(y)) ⊕ (Ω_{Z/S}^1 ⊗_{𝒪_Z} k(z))
```

*where `ρ` is given by `(17.13.5.4)`, is injective.*

*c) The morphism `T = Y ×_X Z → X ×_S X` is transversal to the diagonal of `X ×_S X` at the point `t`.*

*If `t` is rational over the residue field of its image `s` in `S`, these conditions are also equivalent to the
following:*

*b') The homomorphism*

```text
  (17.13.6.1)    T_y(f) − T_z(g) : T_{Y/S}(y) ⊕ T_{Z/S}(z) → T_{X/S}(x)
```

*(cf. `(16.5.12.5)`) is surjective.*

*Moreover, when conditions a) and b) are verified at `t`, they are so in a neighbourhood of `t` in `T`, and by
restricting `T` to such a neighbourhood, the sequence*

```text
  (17.13.6.2)    0 ⟶ Ω_{X/S}^1 ⊗ 𝒪_T ⟶ (Ω_{Y/S}^1 ⊗ 𝒪_T) ⊕ (Ω_{Z/S}^1 ⊗ 𝒪_T) ⟶ Ω_{T/S}^1 ⟶ 0
```

*(where `ρ` is given by `(17.13.5.3)`) is exact.*

The only point that remains to prove in `(17.13.6)` concerns b'), and follows from the fact that, under the hypothesis
that `t` is rational over `k(s)`, the homomorphism `ρ ⊗ 1` is the transpose of `T_y(f) − T_z(g)`, by virtue of
`(17.13.5.4)`.

When the equivalent conditions of `(17.13.6)` are satisfied, one says that `f` and `g` **form a pair of transversal
morphisms at the point `t`, relative to `S`**; here again, one often suppresses the mention of `S`.

**(17.13.7)** Let us consider in particular the case where `Y` and `Z` are subpreschemes of `X`, `f` and `g` being the
canonical injections; `T` is then the "intersection" subprescheme

<!-- original page 94 -->

`inf(Y, Z)` of `X` `(I, 4.4.3)`, and one has `t = y = z = x`. Instead of saying that the pair `(f, g)` is transversal at
the point `x`, one then says that **`Y` and `Z` intersect transversally at the point `x`** (relative to `S`). Denoting
by `X_s`, `Y_s`, `Z_s`, `T_s` the fibres of `X`, `Y`, `Z`, `T` at the point `s`, image of `x` in `S`, and taking into
account `(5.2.3)`, `(5.1.9)` and `(0, 16.5.12)`, one sees that for this to be so (when `X`, `Y`, `Z` are smooth over `S`
at the point `x`), it is necessary and sufficient that `T` be smooth over `S` at the point `x`, and that one have the
relation

```text
  (17.13.7.1)    codim_x(T_s, X_s) = codim_x(Y_s, X_s) + codim_x(Z_s, X_s).
```

**Proposition (17.13.8).**

<!-- label: IV.17.13.8 -->

*Let `S` be a prescheme, `X` an `S`-prescheme locally of finite presentation over `S`, `Y`, `Z` two subpreschemes of
`X`, `T = inf(Y, Z)` the "intersection" subprescheme of `Y` and `Z`, `x` a point of `T`. The following conditions are
equivalent:*

*a) The canonical injection `i : Y → X` is a morphism transversal to `Z` at the point `x`, relative to `S` `(17.13.3)`.*

*a') The canonical injection `j : Z → X` is a morphism transversal to `Y` at the point `x`, relative to `S`.*

*a″) `Y` and `Z` intersect transversally at the point `x`, relative to `S`.*

*b) `X`, `Y`, `Z` are smooth over `S` at the point `x`, and the homomorphism `ρ` `(17.13.5.4)` is such that*

```text
  ρ ⊗ 1 : Ω_{X/S}^1 ⊗ k(x) → (Ω_{Y/S}^1 ⊗ k(x)) ⊕ (Ω_{Z/S}^1 ⊗ k(x))
```

*is injective.*

*When `x` is rational over `k(s)` (`s` image of `x` in `S`) these conditions are also equivalent to the following:*

*b') The homomorphism*

```text
  T_x(i) − T_x(j) : T_{Y/S}(x) ⊕ T_{Z/S}(x) → T_{X/S}(x)
```

*is surjective.*

*Moreover, when the equivalent conditions a) to b) are verified at the point `x`, they are so in a neighbourhood of `x`
in `T`, and by restricting `X` to a neighbourhood of `x`, the sequence `(17.13.6.2)` is exact, and one has a canonical
isomorphism*

```text
  (17.13.8.1)    𝒩_{T/X} ⥲ (𝒩_{Y/X} ⊗ 𝒪_T) ⊕ (𝒩_{Z/X} ⊗ 𝒪_T).
```

Conditions a), a'), a″) all imply that `X`, `Y`, `Z` are smooth over `S` at the point `x`. Let further `m`, `m − a`,
`m − b` be the relative dimensions of `X`, `Y`, `Z` over `S` at the point `x`. It then follows from `(17.13.2)` applied
by replacing `X'` by `Z` and `Y'` by `T = Y ×_X Z`, that conditions a), a') are both equivalent to saying that `T` is
smooth over `S` at the point `x` and of relative dimension `m − a − b` at this point; but by virtue of `(17.13.7)`, this
signifies precisely that condition a″) is verified, whence the equivalence of a), a') and a″). The equivalence of a″)
and of b) (or b') when `x` is rational over `k(s)`) has been proved in `(17.13.6)`, as well as the fact that if these
conditions are satisfied at the point `x`, they are so in a neighbourhood of `x`, and the exactness of the sequence
`(17.13.6.2)` in such a neighbourhood. It remains to define the canonical isomorphism `(17.13.8.1)`.

<!-- original page 95 -->

Let us denote by `α` and `−β` the homomorphisms appearing on the right-hand side of `(17.13.5.4)`, `γ` and `δ` those
appearing on the right-hand side of `(17.13.5.2)`. To say that the sequence `(17.13.6.2)`

```text
  0 → Ω_{X/S}^1 ⊗ 𝒪_T → (Ω_{Y/S}^1 ⊗ 𝒪_T) ⊕ (Ω_{Z/S}^1 ⊗ 𝒪_T) → Ω_{T/S}^1 → 0
```

is exact means that, in the category of `𝒪_T`-Modules, `Ω_{X/S}^1 ⊗ 𝒪_T` is canonically identified with the fibred
product of `Ω_{Y/S}^1 ⊗ 𝒪_T` and `Ω_{Z/S}^1 ⊗ 𝒪_T` over `Ω_{T/S}^1`, for the homomorphisms `γ` and `δ`. The same
reasoning as in `(0, 18.1.2` and `18.1.3)`, where one replaces rings and two-sided ideals respectively by Modules and
sub-Modules, furnishes a commutative diagram

```text
        0                                  0                  0
        ↓                                  ↓                  ↓
  (𝒩_{Y/X} ⊗ 𝒪_T) ⊕ (𝒩_{Z/X} ⊗ 𝒪_T)  →  𝒩_{Z/X} ⊗ 𝒪_T  →  𝒩_{T/Y}
        ↓                                  ↓                  ↓
  0 → 𝒩_{Y/X} ⊗ 𝒪_T   →   Ω_{X/S}^1 ⊗ 𝒪_T  →α  Ω_{Y/S}^1 ⊗ 𝒪_T → 0
        ↓                                  ↓                  ↓
  0 →    𝒩_{T/Z}      →   Ω_{Z/S}^1 ⊗ 𝒪_T  →   Ω_{T/S}^1     → 0
        ↓                                  ↓                  ↓
        0                                  0                  0
```

where the 3rd and 4th rows and columns are exact by virtue of the smoothness hypotheses. The fact that the composite
homomorphism `𝒩_{T/Y} ⊗ 𝒪_T → δ ∘ β` is the homomorphism corresponding to the canonical injection `T → X` follows from
`(0, 20.5.2.7)`. Since the diagonal of the preceding diagram is exact, `Ker(ε)` is canonically identified with
`𝒩_{T/X}`, taking into account that `T` is smooth over `S` `(17.2.5)`; hence one has a canonical isomorphism
`(17.13.8.1)` inverse of `ε`.

**(17.13.9)** One can generalize the results of `(17.13.5)` and `(17.13.6)` to any finite number of `S`-morphisms
`f_i : Y_i → X` (`i ∈ I`, `I` a finite set). For this, let us denote by `X^I` the product of the family `(X_i)_{i ∈ I}`
of `S`-preschemes all identical to `X` `(I, 3.3.5)`, and let `p_i (i ∈ I)` be the canonical projections. The diagonal
morphism `Δ : X → X^I` is defined (as in `(I, 5.3.1)`) as the unique `S`-morphism such that `p_i ∘ Δ = 1_X` for every
`i ∈ I`. It is an `X`-section of `X^I` for the morphism `p_i`, hence `(I, 5.3.11)` an immersion.

<!-- original page 96 -->

Let then `Y` be the product of the `S`-preschemes `Y_i` (for the composed morphisms `Y_i ⟶^{f_i} X → S`), `T` the
product of the `X`-preschemes `Y_i` (for the morphisms `f_i`). One proves as in `(I, 5.3.5)` that one has a commutative
diagram

```text
  (17.13.9.1)
                            X    ←———  T

                            Δ                ↓

                            X^I  ←———  Y
                                     u
```

(where `u` is the product (over `S`) of the `f_i`), which makes `T` the product of the `X^I`-preschemes `X` and `Y`.

By recurrence on the number of elements of `I`, it follows from `(16.4.23)` that `Ω_{X^I/S}^1` (resp. `Ω_{Y/S}^1`) is
canonically identified with the direct sum of the `p_i*(Ω_{X/S}^1)` (resp. of the `r_i*(Ω_{Y_i/S}^1)`, if
`r_i : Y → Y_i` are the canonical projections).

Suppose now that `X` is smooth over `S` at a point `x` (hence in a neighbourhood of this point). The same is then true
of `X^I` at this point `(17.3.3, (iv))`, and by restricting `X` to a neighbourhood of `x`, one has `(17.2.5)` an exact
sequence of locally free `𝒪_X`-Modules

```text
  0 → 𝒩_{X/X^I} → (Ω_{X^I/S}^1)|_X → Ω_{X/S}^1 → 0.
```

Set `𝓜 = 𝒩_{X/X^I}`; one deduces from the preceding sequence an exact sequence of locally free `𝒪_T`-Modules

```text
  (17.13.9.1')    0 → α*(𝓜) ⟶^α (Ω_{X/S}^1)^I ⊗_{𝒪_X} 𝒪_T ⟶ Ω_{X/S}^1 ⊗_{𝒪_X} 𝒪_T → 0
```

which corresponds to the first row of the diagram `(17.13.1.2)`, and where `α` is none other than the canonical
homomorphism which, to each family `(t_i')_{i ∈ I}` of sections of `Ω_{X/S}^1 ⊗_{𝒪_X} 𝒪_T` above an open of `T`,
associates its sum.

On the other hand, what corresponds here to the second vertical arrow of the diagram `(17.13.1.2)` is the homomorphism

```text
  (17.13.9.2)    τ : (Ω_{X/S}^1)^I ⊗_{𝒪_X} 𝒪_T → ⊕_{i ∈ I} (Ω_{Y_i/S}^1 ⊗_{𝒪_{Y_i}} 𝒪_T)
```

which, to every family `(t_i' ⊗ 1)_{i ∈ I}`, where here the `t_i'` are sections above an open of `X` of `Ω_{X/S}^1`,
associates the sum of the `(h_{T/Y_i/S}(t_i'))_{i ∈ I}`, with the notation of `(16.4.18)`. The homomorphism `ρ`
corresponding to the homomorphism `α` of `(17.13.1.3)` is therefore the restriction to `α*(𝓜) ⊗ 𝒪_T` of the preceding
homomorphism `τ`.

These hypotheses and notations being made precise, one can apply to the situation of `(17.13.9.1')` Prop. `(17.13.2)`,
which gives the

**Corollary (17.13.10).**

<!-- label: IV.17.13.10 -->

*Under the general hypotheses of `(17.13.9)`, let `t` be a point of `T`, `y_i (i ∈ I)` its projections in the `Y_i`, `x`
the point of `X` equal to each of the `f_i(y_i)`. Suppose that `X` is smooth over `S` at the point `x` and of relative
dimension `d`, and that each of the `Y_i` is smooth over `S` at the point `y_i`; let `d + c_i` (`c_i` positive or
negative integer) be the relative dimension of `Y_i` at the point `y_i`. Then the following conditions are equivalent:*

<!-- original page 97 -->

*a) `T` is smooth over `S` at the point `t`, of relative dimension `d + ∑_i c_i`.*

*b) The homomorphism*

```text
  ρ ⊗ 1 : 𝓜 ⊗_{𝒪_X} k(t) → ⊕_{i ∈ I} (Ω_{Y_i/S}^1 ⊗_{𝒪_{Y_i}} k(y_i))
```

*is injective.*

*When `t` is rational over the field `k(s)` (where `s` is the image of `t` in `S`), these conditions are also equivalent
to the following:*

*b') The homomorphism transpose of `ρ ⊗ 1`*

```text
  ⊕_{i ∈ I} T_{Y_i/S}(y_i) → T_{X/S}(x)^I/δ(T_{X/S}(x))
```

*(where `δ` is the diagonal map) is surjective.*

It suffices to remark that `X^I` is smooth over `S` and of relative dimension `d · Card(I)`, and `Y` smooth over `S` of
relative dimension `d · Card(I) + ∑_{i ∈ I} c_i`.

When the equivalent conditions of `(17.13.10)` are verified, one says again that the `f_i` **form a family of
transversal morphisms at the point `t`, relative to `S`**. One sees again that the set of points `t ∈ T` where this
holds is open in `T`. Remark `(17.13.4, (ii))` then shows that if `X` and the `Y_i` are flat and locally of finite
presentation over `S`, and moreover if `T` is proper over `S`, the set of `s ∈ S` such that the `f_i` form a family of
transversal morphisms at all points of `T_s`, relative to `S`, is open in `S`.

**(17.13.11)** Let us consider in particular the case, generalizing `(17.13.7)`, where the `Y_i (i ∈ I)` are
subpreschemes of `X`, the `f_i` being the canonical injections, so that `T = inf(Y_i)` is again the "intersection"
subprescheme of the `Y_i`, and `t = y_i = x` for every `i`; instead of saying that the `f_i` form a family of
transversal morphisms at the point `x`, one says again that the **`Y_i` intersect transversally at the point `x`**
(relative to `S`). Condition a) of `(17.13.10)` is again expressed in the relation that generalizes `(17.13.7.1)`

```text
  (17.13.11.1)    codim_x(T_s, X_s) = ∑_i codim_x((Y_i)_s, X_s).
```

Moreover, one has the following property, which extends `(17.13.8.1)`, and gives another proof of it when `I` has `2`
elements:

**Corollary (17.13.12).**

<!-- label: IV.17.13.12 -->

*When the `Y_i` intersect transversally at the point `x`, one has a canonical isomorphism*

```text
  (17.13.12.1)    𝒩_{T/X} ⥲ ⊕_i (𝒩_{Y_i/X} ⊗_{𝒪_{Y_i}} 𝒪_T).
```

One can restrict to the case where the `Y_i` are closed subpreschemes of `X`, defined by quasi-coherent Ideals `𝓘_i`, so
that `T` is defined by the Ideal `𝓘 = ∑_i 𝓘_i`. By definition of the conormal sheaf of an immersion `(16.1.3)`, the
canonical homomorphism `⨁_i 𝓘_i → 𝓘` gives, by passage to quotients, a surjective homomorphism

```text
  (17.13.12.2)    ⨁_i (𝒩_{Y_i/X} ⊗_{𝒪_{Y_i}} 𝒪_T) → 𝒩_{T/X}.
```

<!-- original page 98 -->

But here the `𝒪_T`-Modules of the two sides of `(17.13.12.2)` are locally free and of the same rank `∑_i c_i` (if `c_i`
is the rank of `𝒩_{Y_i/X}`), by virtue of `(17.2.5)` and of condition a) of `(17.13.10)`; one concludes therefore from
Bourbaki, _Alg. comm._, chap. II, §3, n° 2, cor. of prop. 6, that `(17.13.12.2)` is bijective, and `(17.13.12.1)` is the
inverse isomorphism.

### 17.14. Local and infinitesimal characterizations of smooth morphisms, unramified morphisms, and étale morphisms

**Proposition (17.14.1).**

<!-- label: IV.17.14.1 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `x` a point of `X`, `y = f(x)`. For `f` to be smooth
(resp. unramified, resp. étale) at the point `x`, it is necessary and sufficient that the following condition be
verified:*

*For every local scheme `Y' = Spec(A')` with closed point `y'`, every morphism `h : Y' → Y` such that `h(y') = y`, every
closed subscheme `Y_0 = Spec(A'/𝔧')` of `Y'`, where the ideal `𝔧'` is of square zero, and every `Y`-morphism
`g_0 : Y_0 → X` such that `g_0(y') = x`, there exists at least one (resp. at most one, resp. one and only one)
`Y`-morphism `g : Y' → X` of which `g_0` is the restriction to `Y_0`.*

Taking into account the definitions `(17.1.1` and `17.3.1)`, it is a question of showing that the condition of the
statement is sufficient for `f` to be smooth (resp. unramified) at the point `x`.

(i) **Case of smooth morphisms.** One can restrict to the case where `Y = Spec(A)` and `X = Spec(C)` are affine, with
`C = B/𝔞`, where `B = A[T_1, …, T_n]` is a polynomial `A`-algebra and `𝔞` an ideal of finite type of `B`. To prove that
`f` is smooth at the point `x`, it suffices to establish that `𝒪_{X, x}` is a formally smooth `𝒪_{Y, y}`-algebra for the
discrete topologies `(17.5.1)`. Now one has `𝒪_{X, x} = B_𝔮/𝔞 B_𝔮`, where `𝔮` is a prime ideal of `B`, and if `𝔭` is the
inverse image of `𝔮` in `A`, `B_𝔮` is a formally smooth `A_𝔭`-algebra for the discrete topologies `(0, 19.3.2` and
`19.3.5)`. By application of the Jacobian criterion `(0, 22.6.1` and `20.5.12)` it therefore suffices to see that
`B_𝔮/𝔞 B_𝔮` is an `A_𝔭`-trivial extension of `B_𝔮/𝔞 B_𝔮` by `𝔞 B_𝔮/𝔞^2 B_𝔮`. But this follows precisely from the
hypothesis applied to `A' = B_𝔮/𝔞^2 B_𝔮` and `𝔧' = 𝔞 B_𝔮/𝔞^2 B_𝔮` and to the morphism `g_0` corresponding to the
identity automorphism of `A'/𝔧' = 𝒪_{X, x}`.

(ii) **Case of unramified morphisms.** Set here `A = 𝒪_{Y, y}`, `B = 𝒪_{X, x}`, and note that by virtue of
`(17.4.1, c))`, it suffices to show that `Ω_{B/A}^1 = (Ω_{X/Y}^1)_x = 0`. Now, with the notations of `(0, 20.4.1)`, the
ring `C = P_{B/A}^1 = (B ⊗_A B)/𝔧^2` is local since the same holds for `C/(𝔧/𝔧^2)` isomorphic to `B`. The hypothesis
applied to `A' = C` and `𝔧' = 𝔧/𝔧^2` shows by definition that the map `d_{B/A} : B → Ω_{B/A}^1` is zero `(0, 20.4.6)`,
hence that `Ω_{B/A}^1 = 0` by `(0, 20.4.7)`.

**Proposition (17.14.2).**

<!-- label: IV.17.14.2 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`,
`y = f(x)`. For `f` to be smooth (resp. unramified, resp. étale) at the point `x`, it is necessary and sufficient that
it verify the condition of `(17.14.1)` where one supposes moreover that the local ring `A'` is Artinian, that
`𝔪'^{n+1} = 0`, where `𝔪'` is the maximal ideal of `A'`, and that the residue field `A'/𝔪'` of `A'` is equal to `k(x)`.*

It is again a question of showing that these conditions are sufficient in the case of smooth morphisms and the case of
unramified morphisms.

<!-- original page 99 -->

(i) **Case of smooth morphisms.** If one sets `A = 𝒪_{Y, y}` and `B = 𝒪_{X, x}`, it is a question here of proving,
taking into account `(17.5.3)`, that `B` is a formally smooth `A`-algebra for the preadic topologies. Now, by virtue of
`(0, 22.1.4)`, this follows from the hypothesis when one replaces in the latter the condition `𝔪'^{n+1} = 0` by
`𝔧' ⊂ 𝔪'`. But since `𝔪'` is nilpotent, one sees that the condition of the statement is already sufficient by
considering the rings `A'/𝔪'^j` and reasoning by recurrence on `j` as in `(0, 19.4.3)`.

(ii) **Case of unramified morphisms.** Let us take up the notations of the proof of `(17.14.1, (ii))`; to prove that the
ideal `𝔧/𝔧^2` of `C` is zero, let us note that `C` is then a Noetherian local ring, being a local ring of the ring of an
affine open of a subprescheme of `X ×_Y X`, which is locally of finite type over `X`, hence also over `Y`. If `𝔯` is the
maximal ideal of `C`, it therefore suffices to verify that one has `𝔧/𝔧^2 ⊂ 𝔯^n` for every `n` `(0_I, 7.3.5)`, or again,
that `𝔧/𝔧^2 = 𝔯^n + (𝔧/𝔧^2)`. With the notations of `(0, 20.4.6)`, this means again that for every `n`, the two composed
maps `B → C → C/𝔯^n` and `B → C → C/𝔯^n` are identical; but since `C/𝔯^n` is Artinian, this identity results from the
hypothesis applied, by recurrence on `n`, to `A' = C/𝔯^n` and `𝔧' = (𝔯^n + (𝔧/𝔧^2))/𝔯^n`.

**Remark (17.14.3).** — One will note that, under the hypotheses of `(17.14.2)`, if moreover the field `k(x)` is a
**finite** extension of `k(y)`, then the `A'`-modules `𝔪'^j/𝔪'^{j+1}` are `k(y)`-vector spaces of finite rank, hence a
fortiori `A'` is a finite `𝒪_{Y, y}`-algebra.

### 17.15. Case of preschemes over a base field

Let us first recall `(6.7.7, 6.7.8` and `6.8.1)` the

**Proposition (17.15.1).**

<!-- label: IV.17.15.1 -->

*Let `k` be a field, `X` a prescheme locally of finite type over `k`. For `X` to be smooth at a point `x`, it is
necessary and sufficient that for every radicial extension `k'` of `k` (or only for every finite radicial extension of
`k`), the local ring `𝒪_{X, x} ⊗_k k'` be regular. If `k(x)` is a separable extension of `k` (in particular if `k` is
perfect), it amounts to the same to say that `𝒪_{X, x}` is regular.*

**Corollary (17.15.2).**

<!-- label: IV.17.15.2 -->

*Under the conditions of `(17.15.1)`, for `X` to be smooth over `k`, it is necessary and sufficient that `X` be
geometrically regular over `k` `(6.7.6)`, which entails that `X` is regular. If `k` is perfect, then `X` is smooth over
`k` if and only if `X` is regular.*

**Proposition (17.15.3).**

<!-- label: IV.17.15.3 -->

*Let `k` be a field, `X` a prescheme locally of finite type over `k`, `x` a point of `X`, `n = dim_x(X)`. Let
`(g_i)_{1 ⩽ i ⩽ n}` be a family of `n` sections of `𝒪_X` above `X`, and let `f : X → Y = Spec(k[T_1, …, T_n])` be the
morphism corresponding to the `k`-homomorphism `k[T_1, …, T_n] → Γ(X, 𝒪_X)` transforming `T_i` into `g_i` `(I, 2.2.4)`.
The following conditions are equivalent (and imply that `X` is smooth over `k` at the point `x` and consequently regular
at the point `x`):*

*a) `f` is étale at the point `x`.*

*b) The images of the `d_{X/k}(g_i)` form a basis of the `𝒪_x`-module `(Ω_{X/k}^1)_x`.*

*c) The images of the `d_{X/k}(g_i)` generate the `𝒪_{X, x}`-module `(Ω_{X/k}^1)_x`.*

If `f` is étale at the point `x`, `X` is smooth over `k` at the point `x` since `Y = Spec(k[T_1, …, T_n])` is smooth
over `k` `(17.3.8)`; the fact that a) entails b) is therefore a particular case of `(17.11.3)`. Since b) trivially
entails c), it remains to see that c) implies a). Let us note first

<!-- original page 100 -->

that the hypothesis entails that the homomorphism `(f*(Ω_{Y/k}^1))_x → (Ω_{X/k}^1)_x` is surjective, hence, by replacing
`X` by an open neighbourhood of `x`, one can suppose that the homomorphism `f*(Ω_{Y/k}^1) → Ω_{X/k}^1` is surjective
(Bourbaki, _Alg. comm._, chap. II, §5, n° 1, prop. 2); consequently `f` is unramified `(17.2.2)`. We shall see first
that one can restrict to the case where `x` is rational over `k`. Indeed, if one sets `k' = k(x)`, and `X' = X ⊗_k k'`,
`Y' = Y ⊗_k k' = Spec(k'[T_1, …, T_n])`, there exists a point `x' ∈ X'` above `x`, such that `k(x') = k'`. To prove that
`f` is étale at the point `x`, it suffices to show that `f' = f_{(k')} : X' → Y'` is étale at the point `x'`
`(17.7.1, (ii))`; moreover, `f'` is unramified `(17.3.3, (iii))` and one has `dim_{x'}(X') = n` `(4.2.7)`. In the same
way one can, by replacing `k'` by an algebraically closed extension of `k'`, suppose that `k` is algebraically closed.
Set then `y = f(x)`, `A = 𝒪_{Y, y}`, `B = 𝒪_{X, x}`; since the residue field of `B` is equal to `k`, the same holds for
that of `A`, hence `x` (resp. `y`) is a closed point of `X` (resp. `Y`) `(I, 6.4.2)` and one consequently has
`dim(A) = dim(B) = n`. Since `f` is unramified, the homomorphism `A → B` is surjective `(17.4.1, f″)`; but since
`dim(A) = dim(B) = n`, and `A`, being a regular ring, is integral, the homomorphism `A → B` is also injective
`(0, 16.3.10)`. This homomorphism is therefore bijective, which completes the proof that `f` is étale at the point `x`
`(17.6.3, e″)`.

**Corollary (17.15.4).**

<!-- label: IV.17.15.4 -->

*Under the general hypotheses of `(17.15.3)`, suppose moreover that `k(x)` is a finite and separable extension of `k`
and that the germs `(g_i)_x` belong to `𝔪_x`. Then conditions a), b), c) of `(17.15.3)` are also equivalent to each of
the following:*

*d) The `n` germs `(g_i)_x` generate the maximal ideal `𝔪_x` of `𝒪_{X, x}`.*

*d') The ring `𝒪_{X, x}` is regular and the `(g_i)_x` form a regular system of parameters for this ring `(0, 17.1.6)`.*

Indeed, d') trivially entails d). On the other hand, since `k(x)` is a finite and separable extension of `k`, one has
`Υ_{k(x)/k} = 0` `(0, 20.6.20)` and `k(x) = 𝒪_{X, x}/𝔪_x` is a formally smooth `k`-algebra for the discrete topologies
`(0, 19.6.1)`, hence the exact sequence `(0, 20.5.14.1)` applies to `A = k`, `B = 𝒪_{X, x}`, `𝔧 = 𝔪_x`, and furnishes a
canonical isomorphism

```text
  δ : 𝔪_x/𝔪_x^2 ⥲ (Ω_{X/k}^1)_x ⊗_{𝒪_x} k(x).
```

From this one deduces first the equivalence of conditions c) and d), taking into account Nakayama's lemma. On the other
hand, if `f` is étale at the point `x`, the ring `𝒪_{X, x}` is regular and of dimension `n`, since `x` is a closed point
of `X` `(I, 6.4.2)`, and `n` elements of `𝔪_x` which generate this maximal ideal then necessarily form a regular system
of parameters for `𝒪_{X, x}` `(0, 17.1.6)`; which proves that a) entails d').

**Proposition (17.15.5).**

<!-- label: IV.17.15.5 -->

*Let `k` be a field, `X` a prescheme locally of finite type over `k`, `x` a point of `X`, `n = dim_x(X)`. The following
conditions are equivalent:*

*a) `X` is smooth over `k` at the point `x`.*

*b) `X` is differentially smooth over `k` at the point `x`.*

*c) `(Ω_{X/k}^1)_x` is an `𝒪_x`-free module of rank `n`.*

*d) `(Ω_{X/k}^1)_x` is an `𝒪_{X, x}`-module admitting a system of `n` generators.*

<!-- original page 101 -->

*e) There exists a perfect extension `k'` of `k` and an open neighbourhood `U` of `x` in `X` such that the prescheme
`U ⊗_k k'` is regular.*

The fact that `X` be smooth over `k` at the point `x` entails the existence of an open neighbourhood `U` of `x` which is
smooth over `k`, hence `U ⊗_k k'` is regular for every extension `k'` of `k` `(17.15.2)`, which proves that a) implies
e). Conversely e) implies a), for then `U ⊗_k k'` is smooth over `k'` `(17.15.2)`, hence `U` is smooth over `k`
`(17.7.1, (ii))`.

One has already proved that a) entails c) `(17.10.2)`; c) implies d) trivially and the fact that d) implies a) results
from `(0, 20.4.7)` and `(17.15.3, c))`.

Finally, one has already seen that a) implies b) `(17.12.4)`. Conversely, to prove that b) entails a), one can restrict
to the case where `x` is rational over `k`, by considering, as in the proof of `(17.15.3)`, a point `x'` of
`X' = X ⊗_k k'` above `x` and such that `k(x') = k' = k(x)`, using again `(17.7.1, (ii))` and the fact that if `X` is
differentially smooth at the point `x`, `X'` is differentially smooth at the point `x'` `(16.10.4)`. Supposing therefore
`x` rational over `k`, the fact that `f` be smooth at `x` then follows from hypothesis b) and from `(17.12.5)` applied
to the `k`-section `u : Spec(k) → X` such that `u(Spec(k)) = {x}`.

**Corollary (17.15.6).**

<!-- label: IV.17.15.6 -->

*Let `X` be a prescheme of finite type over a field `k`. For `X` to be smooth over `k`, it is necessary and sufficient
that the `𝒪_X`-Module `Ω_{X/k}^1` be locally free, and that the local rings at the maximal points of `X` be fields,
separable extensions of `k` (this last condition being automatically verified if `k` is a perfect field and `X` a
reduced prescheme).*

The conditions are necessary, for if `X` is smooth over `k`, it follows from `(17.10.2)` that `Ω_{X/k}^1` is locally
free; on the other hand, `X` is regular, hence a fortiori reduced, hence at every maximal point `x` of `X`, `𝒪_{X, x}`
is a field, which must be a `k`-algebra formally smooth for the discrete topologies `(17.5.1)`, hence a separable
extension of `k` `(0, 19.6.1)`.

The conditions are sufficient. One can indeed restrict to the case where `X` is connected, hence `Ω_{X/k}^1` locally
free of constant rank `n`. For every maximal point `x` of `X`, one has then `rg_{k(x)} Ω_{k(x)/k}^1 = n` since
`𝒪_{X, x} = k(x)`; as by hypothesis `k(x)` is a separable extension of `k`, one has `Υ_{k(x)/k} = 0` `(0, 20.6.3)`,
hence `deg.tr_k k(x) = n` by Cartier's equality `(0, 21.7.1)`. All the irreducible components of `X` have therefore the
same dimension `n` `(5.2.1)`, and one concludes that `X` is smooth over `k` at every point by virtue of the fact that c)
entails a) in `(17.15.5)`.

**Corollary (17.15.7).**

<!-- label: IV.17.15.7 -->

*If `k` is of characteristic `0`, then, for `X` to be smooth over `k` at the point `x`, it is necessary and sufficient
that `(Ω_{X/k}^1)_x` be a free `𝒪_{X, x}`-module.*

This follows from `(16.12.2)` and from the equivalence of b) and a) in `(17.15.5)`.

**Proposition (17.15.8).**

<!-- label: IV.17.15.8 -->

*Let `k` be a field, `X` a prescheme locally of finite type over `k`, `x` a point of `X`; set `n = dim_x(X)`,
`r = dim(𝒪_{X, x})`, so that `n − r = deg.tr_k k(x)` `(5.2.3)`. Let `(g_i)_{1 ⩽ i ⩽ n}` be a family of `n` sections of
`𝒪_X` above `X`, such that `(g_i)_x ∈ 𝔪_x` for `1 ⩽ i ⩽ r`; let `f : X → Y = Spec(k[T_1, …, T_n])` be the morphism
corresponding to the `k`-homomorphism `k[T_1, …, T_n] → Γ(X, 𝒪_X)` transforming `T_i` into `g_i`. The following
conditions are equivalent (and imply that `X` is smooth over `k` at the point `x` and that `k(x)` is a separable
extension of `k`):*

*a) `f` is étale at the point `x`.*

<!-- original page 102 -->

*b) The `(g_i)_x` such that `1 ⩽ i ⩽ r` generate `𝔪_x` (and consequently form a regular system of parameters for
`𝒪_{X, x}` `(0, 17.1.6)`) and the images in `Ω_{k(x)/k}^1` of the elements `(d_{X/k}(g_j))_x` for `r + 1 ⩽ j ⩽ n`
generate `Ω_{k(x)/k}^1`.*

One has indeed `(0, 20.5.12.1)` the exact sequence of `k(x)`-modules

```text
  (17.15.8.1)    𝔪_x/𝔪_x^2 → (Ω_{X/k}^1)_x ⊗_{𝒪_x} k(x) → Ω_{k(x)/k}^1 → 0
```

and condition b) entails consequently that the `(d_{X/k}(g_i))_x` generate `(Ω_{X/k}^1)_x` taking into account
Nakayama's lemma; the fact that b) implies a) therefore results from `(17.15.3)`. Conversely, if a) is verified, the
`(d_{X/k}(g_i))_x` for `1 ⩽ i ⩽ n` form a basis of `(Ω_{X/k}^1)_x` by virtue of `(17.15.3)`. If `t_i (1 ⩽ i ⩽ n)` is the
image of `(g_i)_x` in `k(x)`, one concludes from what precedes that the `dt_i` generate `Ω_{k(x)/k}^1` for `1 ⩽ i ⩽ n`,
and since by hypothesis `t_i = 0` for `1 ⩽ i ⩽ r`, the `dt_i` for `r + 1 ⩽ i ⩽ n` already generate `Ω_{k(x)/k}^1`. As
`deg.tr_k k(x) = n − r`, it follows from Cartier's equality `(0, 21.7.1)` that `Υ_{k(x)/k} = 0`, hence `k(x)` is a
separable extension of `k` `(0, 20.6.3)`, and the sequence of `k(x)`-vector spaces

```text
  (17.15.8.2)    0 → 𝔪_x/𝔪_x^2 → (Ω_{X/k}^1)_x ⊗_{𝒪_x} k(x) → Ω_{k(x)/k}^1 → 0
```

is exact (`(0, 20.5.14)` and `(0, 19.6.1)`); moreover the `dt_i` for `r + 1 ⩽ i ⩽ n` form a basis of `Ω_{k(x)/k}^1`,
hence none of the `t_i` such that `r + 1 ⩽ i ⩽ n` can be zero. This shows that the images of the `(g_i)_x` in
`𝔪_x/𝔪_x^2` for `1 ⩽ i ⩽ r` necessarily generate `𝔪_x/𝔪_x^2`, hence the `(g_i)_x` for `1 ⩽ i ⩽ r` generate `𝔪_x` by
virtue of Nakayama's lemma, which completes the proof that a) implies b).

**Corollary (17.15.9).**

<!-- label: IV.17.15.9 -->

*Let `X` be a prescheme locally of finite type over a field `k`, `x` a point of `X` and set `n = dim_x(X)`,
`r = dim(𝒪_{X, x})`. The following conditions are equivalent:*

*a) The ring `𝒪_{X, x}` is regular and `k(x)` is a separable extension of `k`.*

*b) `X` is smooth over `k` at the point `x`, and the canonical homomorphism*

```text
  𝔪_x/𝔪_x^2 → (Ω_{X/k}^1)_x ⊗_{𝒪_x} k(x)
```

*is injective.*

*c) There exist `n` sections `g_i` of `𝒪_X` above an open neighbourhood `U` of `x` such that `(g_i)_x ∈ 𝔪_x` for
`1 ⩽ i ⩽ r` and that the morphism `U → Spec(k[T_1, …, T_n])` corresponding to the `g_i` (cf. `(17.15.8)`) is étale at
the point `x`.*

*d) There exist `n` sections `g_i (1 ⩽ i ⩽ n)` of `𝒪_X` above an open neighbourhood `U` of `x`, such that the `(g_i)_x`
for `1 ⩽ i ⩽ r` generate `𝔪_x` and the images in `Ω_{k(x)/k}^1` of the `(d_{X/k}(g_j))_x` for `r + 1 ⩽ j ⩽ n` generate
`Ω_{k(x)/k}^1`.*

The equivalence of c) and d) follows from `(17.15.8)`. Moreover, one has seen in the proof of `(17.15.8)` that condition
c) entails that `X` is smooth over `k` at the point `x` and that the sequence `(17.15.8.2)` is exact, hence c) entails
b). Condition b) entails that the ring `𝒪_{X, x}` is regular, hence `𝔪_x/𝔪_x^2` is of rank `r`; moreover,
`(Ω_{X/k}^1)_x` is then an `𝒪_{X, x}`-free module of rank `n` `(17.10.2)`; since the sequence `(17.15.7.2)` is exact by
hypothesis, `Ω_{k(x)/k}^1` is of rank `n − r = deg.tr_k k(x)` and Cartier's equality shows that `Υ_{k(x)/k} = 0`; hence
`k(x)` is separable over `k` `(0, 20.6.3)`; thus b) entails a). Finally, if a)

<!-- original page 103 -->

is verified, one deduces again from Cartier's equality that `Ω_{k(x)/k}^1` is of rank `n − r`. As on the other hand the
ring `𝒪_{X, x}` is regular, the existence of the `g_i` verifying the conditions of d) is immediate.

**Remarks (17.15.10).** — (i) For a prescheme of finite type `X` over `k` to be smooth over `k`, it does not suffice
that `Ω_{X/k}^1` be locally free, as shown by the example where `X = Spec(K)`, with `K` a finite non-separable extension
of `k`.

(ii) When `k` is not perfect, it can happen that `X` is smooth over `k` without `k(x)` being separable over `k`. One has
an example by taking `X = Spec(k[T])` and for `x` the point corresponding to the principal prime ideal `(T^p − λ)`
(`p > 0` characteristic of `k`, `λ ∈ k − k^p`).

(iii) However, if `X` is a smooth prescheme over `k`, the set of closed points of `X` such that `k(x)` is separable (and
finite) over `k` is dense in `X`. Indeed, let `f : X → Spec(k)` be the structure morphism; for every `x_0 ∈ X`, there is
an open neighbourhood `U` of `x_0` in `X` and a factorization of `f | U : U → Spec(k[T_1, …, T_n]) → Spec(k)` where `g`
is étale `(17.11.4)`. As one can restrict to the case where `k` is not perfect, hence infinite, the set of points of the
open `g(U)` which are rational over `k` is non-empty; if `y` is such a point and `x ∈ U` a point above `y`, `x` is
closed in `X` and `k(x)` is separable over `k(y) = k` `(17.6.2)`.

**Proposition (17.15.11).**

<!-- label: IV.17.15.11 -->

*Let `X` be a prescheme of finite type over a field `k`. The following conditions are equivalent:*

*a) `X` is étale over `k`.*

*b) `X` is unramified over `k`.*

*c) `X` is isomorphic to `Spec(A)`, where `A` is a finite and separable `k`-algebra.*

This results from `(17.6.2)` and `(17.4.2)`, taking into account that condition b) implies here that `X` is finite over
`k`.

**Proposition (17.15.12).**

<!-- label: IV.17.15.12 -->

*Let `k` be a field, `X` a prescheme locally of finite type over `k`. For there to exist an everywhere dense open `U` of
`X` which is smooth over `k`, it is necessary and sufficient that for every maximal point `x` of `X`, `X` be reduced at
this point and that `k(x)` be a separable extension of `k`. For there to exist an everywhere dense open `U` of `X` such
that `U_{red}` be smooth over `k`, it is necessary and sufficient that for every maximal point `x` of `X`, `k(x)` be a
separable extension of `k`.*

The second assertion evidently follows from the first. To say that there exists an everywhere dense open `U` smooth over
`k` signifies that `X` is smooth over `k` at each of its maximal points `x`. It is necessary for that that `𝒪_{X, x}` be
regular `(17.15.1)` and a fortiori reduced, hence a field, equal to `k(x)`; moreover `(17.15.1)`, `k(x) ⊗_k k'` must be
regular for every radicial extension `k'` of `k`, hence `k(x)` must be a separable extension of `k` `(4.3.5)`; the
converse is immediate, by virtue of `(17.15.1)`.

**Corollary (17.15.13).**

<!-- label: IV.17.15.13 -->

*Let `X` be an algebraic prescheme over a field `k`. Then there exists an everywhere dense open `U` in `X` and a finite
radicial extension `k'` of `k` such that `(U_{(k')})_{red}` be smooth over `k'`.*

Indeed, there is such an extension `k'` such that `(X_{(k')})_{red}` be geometrically reduced over `k'` `(4.6.6)`, which
amounts to saying `(4.6.1)` that for every maximal point `x'` of `X_{k'}`, `k(x')` is a separable extension of `k'`. One
thus concludes from `(17.15.12)` that there is an everywhere dense open `U'` of `X_{k'}` such that `U'_{red}` be smooth
over `k'`. But the

<!-- original page 104 -->

morphism `X_{k'} → X` is a homeomorphism `(2.4.5)`, hence `U'` is of the form `U_{k'}`, where `U` is an everywhere dense
open in `X`.

**Proposition (17.15.14).**

<!-- label: IV.17.15.14 -->

*Let `X` be an algebraic prescheme over `k`, of dimension `⩽ 1`. Then there exists a finite radicial extension `k'` of
`k` such that the normalization `(II, 6.3.8)` of `(X_{(k')})_{red}` be smooth over `k'`.*

Let us first prove the two following lemmas:

**Lemma (17.15.14.1).**

<!-- label: IV.17.15.14.1 -->

*Let `X` be a reduced prescheme whose set of irreducible components is locally finite, `f : Y → X` a morphism. For `Y`
to be `X`-isomorphic to the normalization `X'` of `X` `(II, 6.3.8)`, it is necessary and sufficient that the following
conditions be verified:*

*(i) `Y` is normal;*

*(ii) `f` is an integral and birational morphism.*

*When there exists in `X` a dense and normal open (which is always the case when `X` is excellent `(7.8.3)`, in
particular when `X` is locally of finite type over a field), one can replace condition (ii) by the following:*

*(ii bis) `f` is integral and there exists a dense open `U` in `X` such that `f⁻¹(U)` be dense in `Y` and that the
restriction `f⁻¹(U) → U` of `f` be an isomorphism.*

The question being local on `X`, one can suppose that `X` has only a finite number of irreducible components; let
`X_i (1 ⩽ i ⩽ m)` be the reduced subpreschemes of `X` having these components as underlying spaces. One knows
`(II, 6.3.6)` that `X'` is the sum of the normalizations `X'_i` of the `X_i`; each of the structure morphisms
`f_i : X'_i → X_i` is therefore integral and birational, hence `f` is integral and birational; it is immediate that (ii)
entails (ii bis) when there exists an open `V` dense and normal in `X`, by taking `U = V`. Conversely, if conditions (i)
and (ii) are fulfilled, `Y` has only a finite number of irreducible components `Y_i (1 ⩽ i ⩽ m)`, `Y_i` dominating `X_i`
for each index `i` `(6.15.4)`; `Y` is the sum of the `Y_i` since it is normal, and the morphism `g_i : Y_i → X_i` into
which the restriction `Y_i → X` of `f` factors `(I, 5.2.2)` is birational; since `X_i` and `Y_i` are integral, it then
follows from the fact that `g_i` is integral and `Y_i` normal that, for every affine open `V` of `X_i`,
`Γ(g_i⁻¹(V), 𝒪_Y)` is the integral closure of `Γ(V, 𝒪_{X_i})`, hence `Y` is canonically identified with `X'`
`(II, 6.3.4)`. Finally, if one supposes condition (ii bis) verified, one can restrict to the case where `U` is a union
of disjoint irreducible opens `U_i (1 ⩽ i ⩽ m)`, hence `f⁻¹(U)` a disjoint union of the `V_i = f⁻¹(U_i)`. Since the
`V_i` are irreducible and `f⁻¹(U)` dense in `Y`, the `V_i` are the irreducible components of `Y` and consequently `f` is
birational.

**Lemma (17.15.14.2).**

<!-- label: IV.17.15.14.2 -->

*Let `k` be a field, `X` an algebraic prescheme over `k`. Then there exists a finite radicial extension `k'` of `k` such
that `(X_{(k')})_{red}` be geometrically reduced over `k'` and that its normalization be geometrically normal over
`k'`.*

Taking into account `(4.6.6)` and `(I, 5.1.8)`, one can restrict to the case where `X` is already geometrically reduced
over `k`. Let `p` be the characteristic exponent of `k` and `k_1 = k^{p^{-∞}}` the smallest perfect extension of `k`;
`k_1` is thus the inductive limit of the finite radicial extensions of `k`. Set `X_1 = X_{(k_1)}`, which is reduced by
hypothesis, and let `Y_1` be its normalization; if `f_1 : Y_1 → X_1` is the structure morphism, `f_1` is therefore
finite `(7.8.3, (vi))` and surjective, and there exists a dense open `U_1` in `X_1` such that `f_1⁻¹(U_1) = V_1` be
dense in `Y_1` and that

<!-- original page 105 -->

the morphism `V_1 → U_1` restriction of `f_1` be an isomorphism `(17.15.14.1)`. Applying `(8.9.1)` and `(8.10.5, (vi)`
and `(x))`, one therefore first sees that there exists a finite radicial extension `k″` of `k` and a finite surjective
morphism `Y″ → X″ = X_{(k″)}` such that `Y_1 = Y″ ⊗_{k″} k_1`; since `Y_1` is normal and `k_1` perfect, it follows from
`(6.7.7)` that `Y″` is geometrically normal over `k″`. As the projections `X_1 → X″` and `Y_1 → Y″` are integral,
surjective and radicial morphisms, they are homeomorphisms `(2.4.5)`, and if `U″` and `V″` are the images of `U_1` and
`V_1` in `X″` and `Y″` respectively, they are dense opens in `X″` and `Y″` respectively such that `V″ = f″⁻¹(U″)`, where
`f″ : Y″ → X″` is the structure morphism. As one has `U_1 = U″ ⊗_{k″} k_1`, it follows from `(8.10.5, (i))` that there
exists a finite radicial extension `k'` of `k″` such that if one sets `X' = X_{(k')} = X″ ⊗_{k″} k'`,
`Y' = Y″ ⊗_{k″} k'`, `f' = f″_{(k')} : Y' → X'`, and if `U'` and `V'` are the images of `U″` and `V″` in `X'` and `Y'`
respectively, the restriction `V' → U'` of `f'` be an isomorphism. Since `Y'` is normal and `f'` integral and
birational, one concludes from `(17.15.14.1)` that `Y'` is isomorphic to the normalization of `X'`, which proves the
lemma since `Y'` is geometrically normal.

Let us now return to the proof of `(17.15.14)`, and apply lemma `(17.15.14.2)` to `k` and `X`; since `dim(X) ⩽ 1`, one
has also `dim(X_{k'}) ⩽ 1` `(4.1.4)`, and the normalization `Y'` of `X_{k'}` is also of dimension `⩽ 1` `(5.4.2` and
`II, 7.4.6)`. To say that `Y'` is geometrically normal over `k'` then amounts to saying, by virtue of the definitions
and of `(II, 7.4.5)`, that `Y'` is geometrically regular over `k'`, hence smooth over `k'` `(17.5.1)`, which proves
`(17.15.14)`.

**Proposition (17.15.15).**

<!-- label: IV.17.15.15 -->

*Let `f : X → Y` be a morphism locally of finite presentation. For `f` to be smooth at a point `x ∈ X`, it is necessary
and sufficient that `f` be flat at the point `x` and that `Ω_{X/Y}^1` be a locally free `𝒪_X`-Module in a neighbourhood
of `x`, of rank at `x` equal to `dim_x f`.*

The necessity of the conditions follows from `(17.5.1)` and `(17.10.2)`. Conversely, if these conditions are verified,
and if `y = f(x)`, it suffices to show `(17.5.1)` that `f⁻¹(y)` is smooth over `k(y)` at the point `x`; but this follows
from the definition of `dim_x f` `(17.10.1)`, from `(16.4.5)` and from `(17.15.5)`.

### 17.16. Quasi-sections of flat or smooth morphisms

The statements of this number complete those of `(14.5)`, with hypotheses of flatness.

**Proposition (17.16.1).**

<!-- label: IV.17.16.1 -->

*Let `f : X → S` be a flat morphism locally of finite presentation. Let `s ∈ S`, `x` a closed point of `X_s` such that
`𝒪_{X_s, x}` be a Cohen-Macaulay ring; then there exists an open neighbourhood `U` of `s` in `S` and a subprescheme
`X' ⊂ f⁻¹(U)` of `X` such that `x ∈ X'` and that the morphism `X' → U`, restriction of `f`, be flat, quasi-finite and of
finite presentation.*

The question being local on `X` and `Y`, one can suppose `f` of finite presentation.

Let `(t_i)_{1 ⩽ i ⩽ m}` be a system of parameters of the local ring `𝒪_{X_s, x}`; there exists an affine open
neighbourhood `V = Spec(A)` of `x` in `X` and `m` sections `s_i` of `𝒪_X` above `V` such that

<!-- original page 106 -->

the images of the `(s_i)_x ∈ 𝒪_{X, x}` in `𝒪_{X_s, x} = 𝒪_{X, x}/𝔪_s 𝒪_{X, x}` be equal to the `t_i`. Let `X'` be the
closed subprescheme of `V` defined by the ideal of `A` generated by the `s_i`; the sequence `(s_i)` being by hypothesis
regular `(0, 16.5.7)`, it follows from `(11.3.8)` that by replacing if necessary `V` by a smaller open neighbourhood,
one can suppose that the morphism `X' → S`, restriction of `f`, is flat and of finite presentation. On the other hand,
since the `s_i` form a system of parameters of `𝒪_{X_s, x}`, the ring `𝒪_{X'_s, x}` is by definition Artinian, and since
`x` is closed in `X_s`, one concludes that it is isolated in `X'_s`. By replacing `V` if necessary by a smaller
neighbourhood of `x`, one concludes, thanks to `(13.1.4)`, that the morphism `X' → S` is quasi-finite.

**Corollary (17.16.2).**

<!-- label: IV.17.16.2 -->

*Let `f : X → S` be a faithfully flat morphism and locally of finite presentation. Then there exists a morphism
`g : S' → S`, faithfully flat, locally of finite presentation and locally quasi-finite, such that there exists an
`S`-morphism `S' → X` (in other words, such that there exists an `S'`-section of `X' = X ×_S S'` `(I, 3.3.14)`). If `S`
is quasi-compact (resp. quasi-compact and quasi-separated), one can suppose `S'` affine (resp. `S'` affine and the
morphism `g` quasi-finite).*

For every `s ∈ S`, the fibre `X_s` is non-empty by hypothesis and is a prescheme locally of finite type over `k(s)`; the
set `U_s` of points `x` of `X_s` where `𝒪_{X_s, x}` is a Cohen-Macaulay ring is open in `X_s` `(6.11.3)` and is
non-empty, since it contains the maximal points of `X_s` `(0, 16.5.1)`; it consequently contains a point `x_s` closed in
`X_s` `(10.4.7)`. Let `X'(s)` be an affine subprescheme of `X` containing `x_s` and verifying the conditions of
`(17.16.1)`. To obtain a prescheme `S'` verifying the conditions of the statement, it suffices to take the sum of the
`X'(s)`, where `s` runs through `S`. Since the morphism `X'(s) → S` is flat and locally of finite presentation, the
image `U(s)` of `X'(s)` is open in `S` `(2.4.6)`; when `S` is quasi-compact, one can therefore cover `S` by a finite
number of `U(s_i)` and the prescheme `S'` sum of the `X'(s_i)` again answers the question and is affine. If moreover `S`
is quasi-separated, one can suppose the open immersions `U(s) → S` quasi-compact `(1.2.7)`, hence of finite presentation
`(1.6.2)`, and then the morphisms `X'(s_i) → S` are of finite presentation `(1.6.2)` and consequently so is the morphism
`S' → S`.

**Corollary (17.16.3).**

<!-- label: IV.17.16.3 -->

*(i) Let `f : X → S` be a smooth morphism. Let `s ∈ S`, `x` a closed point of `X_s` such that the residue field `k(x)`
be separable over `k(s)`; then, in the conclusion of `(17.16.1)`, one can take `X'` such that the morphism `X' → U`,
restriction of `f`, be étale.*

*(ii) Let `f : X → S` be a smooth surjective morphism. Then, in the conclusions of `(17.16.2)`, one can suppose moreover
that `g : S' → S` is étale.*

It is clear that (ii) deduces from (i) as `(17.16.2)` from `(17.16.1)`, taking into account that, for every `s ∈ S`,
since `X_s` is non-empty and smooth over `k(s)`, there exists a closed point `x ∈ X_s` such that `k(x)` is separable
over `k(s)` `(17.15.10, (iii))`. It therefore suffices to prove (i). One will note that the ring `𝒪_{X_s, x}` is here
regular; if one repeats the construction made in `(17.16.1)` by taking for `(s_i)` a regular system of parameters of
`𝒪_{X_s, x}`, the ring `𝒪_{X'_s, x}` is a field isomorphic to `k(x)`, hence separable over `k(s)` by hypothesis. The
conclusion then results from `(17.6.1, c'))`.

**Proposition (17.16.4).**

<!-- label: IV.17.16.4 -->

*Let `S` be a quasi-compact and quasi-separated prescheme, `f : X → S` a surjective morphism locally of finite
presentation. Then there exists a finite family `(S_i)_{i ∈ I}`*

<!-- original page 107 -->

*of affine subpreschemes of `S`, of finite presentation over `S`, pairwise disjoint, with union `S`, and having the
following property: for each `i ∈ I`, there exist two finite morphisms of finite presentation and surjective
`S_i″ →^{g_i} S_i' →^{h_i} S_i`, where `h_i` is étale and `g_i` flat and radicial, and an `S`-morphism `S_i″ → X` (in
other words an `S_i″`-section of `X_i″ = X ×_S S_i″`).*

There is a finite cover `(U_i)_{1 ⩽ i ⩽ n}` of `S` by affine opens; for every `i`, the intersection
`W_i = ⋂_{j ≠ i} U_j` is quasi-compact `(1.2.7)`, hence there exists a closed subprescheme `V_i` of `U_i` having as
underlying space `U_i − W_i` and defined by an ideal of finite type of the ring of `U_i`; hence `V_i` is an affine
subprescheme of `S` which is of finite presentation over `S` `(1.6.2)`. It is clear that one can restrict to proving the
proposition where one replaces `S` by `V_i` and `X` by `X ×_S V_i`. In other words, one can already suppose `S` affine.
On the other hand, `X` is a union of affine opens `W_α` and the `f(W_α)` are constructible in `S` `(1.8.4)` and form a
cover of `S`; consequently `(1.9.9)` there exists a finite subfamily `(W_{α_j})_{1 ⩽ j ⩽ r}` such that the `f(W_{α_j})`
already form a cover of `S`. Let then `X'` be the prescheme sum of the subpreschemes induced on the opens `W_{α_j}` of
`X`; it is immediate that it suffices to prove the proposition by replacing `X` by `X'` since an `S`-morphism
`S_i″ → X'` gives by composition an `S`-morphism `S_i″ → X' → X`.

One can therefore suppose `X` affine and `f` of finite presentation. One can then `(8.9.1)` write `X` in the form
`X_0 ×_{S_0} S`, where `S_0` is Noetherian, `X_0 → S_0` a morphism of finite type, which one can suppose surjective
`(8.10.5, (vi))`. If the proposition is proved for this morphism, it will follow at once for `X` by base change
`S → S_0`. One can therefore suppose moreover `S` Noetherian and `f` of finite type.

Let `s_h (1 ⩽ h ⩽ r)` be the maximal points of `S`. Let us show that it suffices to prove the statement by replacing `S`
by a sufficiently small open neighbourhood `U_h` of each of the `s_h`, `X` by the inverse image of `U_h` in `X`. Indeed,
suppose the proposition established in this case, and let us reason by Noetherian recurrence `(0_I, 2.2.2)` by supposing
the statement established for every closed subprescheme of `S` having an underlying space `≠ S`. One can suppose the
`U_h` pairwise without common point; if `T` is a closed subprescheme having as underlying space `S − (⋃ U_h)`, the
recurrence hypothesis entails that the statement is true for `T`; as it is also true for each of the `U_h`, it is
evidently so for `S`.

As one can evidently (by replacing `S` by `S_{red}` and `X` by `X ×_S S_{red}`) suppose `S` reduced, each of the
`𝒪_{S, s_h}` is a field `k(s_h)`. Suppose that one has proved the proposition when `S` is the spectrum of a field and
`f` is of finite type. Then the existence of the `U_h` follows from the method of `(8.1.2, a))` and of `(8.8.2, (i)` and
`(ii))`, `(8.10.5, (vi), (vii)` and `(x))`, `(11.2.6, (ii))` and `(17.7.8, (ii))`.

Suppose therefore `S = Spec(k)`, where `k` is a field, `X` being of finite type over `k` and `X ≠ ∅`. As `X` is
Noetherian, there exists in `X` a closed point `x` `(0_I, 2.1.3)`, hence `k(x)` is a finite extension of `k`
`(I, 6.4.2)`. There is consequently a finite separable extension `k'` of `k` such that `k″ = k(x)` be a finite radicial
extension of `k'`. One answers then the question by taking `I` reduced to one element, `S_1' = Spec(k')`,
`S_1″ = Spec(k″)`.

<!-- original page 108 -->

**Corollary (17.16.5).**

<!-- label: IV.17.16.5 -->

*Let `f : X → S` be a surjective morphism locally of finite presentation. Then there exists a morphism `g : S' → S`
surjective, locally of finite presentation and locally quasi-finite, such that there exists an `S`-morphism `S' → X` (in
other words such that there exists an `S'`-section of `X' = X ×_S S'`). If `S` is quasi-compact (resp. quasi-compact and
quasi-separated), one can suppose `S'` affine (resp. `S'` affine and the morphism `g` of finite presentation and
quasi-finite).*

It suffices to prove the corollary by supposing `S` affine: `S` is indeed a union of a family `(S_α)` of affine opens,
and if for each `α`, `S'_α` is affine and the morphism `g_α : S'_α → S_α` answers the question and is of finite
presentation and quasi-finite, then by taking for `S'` the prescheme sum of the `S'_α`, `g : S' → S` coinciding with
`g_α` in each of the `S'_α`, this morphism answers the question; in addition, if `S` is quasi-compact, one can suppose
the family `(S_α)` finite, hence `S'` affine; if moreover `S` is quasi-separated, the immersions `S_α → S` are of finite
presentation `(1.6.2)`, hence so is `g`.

Let us consider therefore the case where `S` is affine: one then forms the finite morphisms of finite presentation
`S_i″ → S_i` of `(17.16.4)`; since the immersions `S_i → S` are of finite presentation (the `S_i` being affine), the
morphisms `g_i″ : S_i″ → S_i → S` are of finite presentation and quasi-finite, and one answers the question by taking
`S'` equal to the sum of the `S_i″` and `g` coinciding with `g_i″` in each of the `S_i″`.

**Proposition (17.16.6).**

<!-- label: IV.17.16.6 -->

*Let `S` be a quasi-compact and quasi-separated prescheme, `f : X → S` a morphism of finite presentation such that, for
every `s ∈ S`, `X_s = f⁻¹(s)` be a prescheme proper over `k(s)`. Then there exists a finite family `(S_i)_{i ∈ I}` of
affine subpreschemes of `S`, of finite presentation over `S`, pairwise disjoint, with union `S` and such that, for every
`i`, the morphism `X_i = X ×_S S_i → S_i` be proper and flat. If moreover, for every `s ∈ S`, `X_s` is finite over
`k(s)`, one can take the `S_i` such that each of the morphisms `X_i → S_i` factors as*

```text
                u_i      h_i
            X_i ⟶  X_i' ⟶  S_i
```

*where `u_i` and `h_i` are finite and locally free `(18.2.7)`, `h_i` is étale, `u_i` is radicial and surjective.*

One follows an analogous procedure to that of `(17.16.4)`. One reduces first to the case where `S` is affine and `f` is
flat, by using the generic flatness theorem `(8.9.5)` (one will observe that the subpreschemes `S_i` defined in the
proof of `(8.9.5)` are affine). Since `f` is of finite presentation, one can next write `X = X_0 ×_{S_0} S`, where `S_0`
is Noetherian, `X_0 → S_0` a morphism of finite type and flat `(11.2.7)`; moreover each fibre `(X_0)_s` is again proper
over `k(s_0)`, as follows from `(2.7.1, (vii))` and one is therefore reduced to the case where `S` is Noetherian. By
Noetherian recurrence and application of the procedure of `(8.1.2, a))` (using also this time `(8.10.5, (xii))`), one is
finally reduced, to prove the first assertion, to the case where `S` is the spectrum of a field, which results trivially
from the hypothesis (with `S_1 = S`). One treats in the same way the case where `X_s` is supposed finite over `k(s)` for
every `s ∈ S` (one must this time use `(2.7.1, (xv))`, `(8.10.5, (x), (iv), (vi)` and `(vii))`, `(17.7.8)` and
`(2.1.12)`), and one is reduced to proving the last assertion of the statement when `S = Spec(k)` is the spectrum of a
field. But then `X = Spec(A)`, where `A` is a finite `k`-algebra `(I, 6.4.4)`; therefore `A` is a direct composite of
finite `k`-algebras `A_j`

<!-- original page 109 -->

which are local rings `(1 ⩽ j ⩽ m)`; since `A_j` is an Artinian ring and a `k`-algebra, it contains a subfield `K_j`
canonically isomorphic to the residue field of `A_j` `(0, 19.6.2)`. One then takes `X_i = X`, `X_i'` the sum of the
`Spec(K_j)` and it is clear that one answers thus the question since for every `j` one has two homomorphisms
`K_j → A_j → k(A_j)` whose composite is an isomorphism.

[^17.3.1.note]: The words "net" and "formally net" appear distinctly preferable to the established terminology "non
    ramifié" (resp. "formellement non ramifié") and will be employed almost exclusively from chap. V
    onwards. In this chapter, we have kept the older terminology so as not to come into conflict with
    `(0, 19.10)`.

[^17.7.11.note1]: The reader will verify that the result of `(17.7.11)` is not used in the rest of §17, and that there
    is therefore no vicious circle.

[^17.7.11.note2]: The reader will verify that the result of `(17.7.11)` is not used in the rest of §17, and that there
    is therefore no vicious circle.

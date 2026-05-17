<!-- original page 187 -->

## §13. Equidimensional morphisms

This section is devoted to the study of the variation of the dimension of the fibres of a morphism locally of finite
type `f : X → Y` (which has already come up in connection with the "dimension formula" in `(5.5)` and `(5.6)`). We prove
first `(13.1.3)` that the function `x ↦ dim_x(f⁻¹(f(x)))` is always upper semi-continuous in `X` (Chevalley's
*semi-continuity theorem*). We then study more specifically the morphisms, called *equidimensional*, for which this
function is locally constant. Unfortunately the notion of equidimensional morphism is not stable under base change;

<!-- original page 188 -->

this is why in numerous questions it is more convenient to work with the notion of universally open morphism, the study
of which is the object of §§14 and 15.

### 13.1. Chevalley's semi-continuity theorem

**Lemma (13.1.1).**

<!-- label: IV.13.1.1 -->

*Let `Y` be a locally Noetherian irreducible prescheme, `X` an irreducible prescheme, `f : X → Y` a dominant morphism of
finite type. Let `ξ` (resp. `η`) be the generic point of `X` (resp. `Y`) and let `e = dim(f⁻¹(η))`. Then, for every
`x ∈ X`, every irreducible component of `f⁻¹(f(x))` is of dimension `≥ e`.*

The proposition is immediate when, for every `y ∈ f(X)`, `𝒪_y` is a universally catenary ring: indeed, if `x` is the
generic point of an irreducible component `Z` of `f⁻¹(y)`, it follows from `(5.6.5)`, joined with `(5.2.1)`, that one has
`e + dim(𝒪_y) = dim(Z) + dim(𝒪_x)`; but by virtue of `(0, 16.3.9)` one has `dim(𝒪_x) ≤ dim(𝒪_y)`, whence the conclusion
in this case.

We shall reduce the general case to this particular case. The question is evidently local on `Y`, and, in view of
`(4.1.1.3)`, it is also local on `X`; one may therefore restrict to the case where `Y = Spec(A)` and `X = Spec(B)` are
affine and irreducible, `B` being an `A`-algebra of finite type. Moreover `(1.5.4)`, one may suppose `X` and `Y`
reduced, hence `A` and `B` integral, and, since `f` is dominant, `A` is then a sub-ring of `B`. Consider `A` as the
inductive limit of its sub-`ℤ`-algebras of finite type; it then follows from `(8.9.1)` that there exists such a
sub-algebra `A_0` and an `A_0`-algebra of finite type `B_0` such that `B = B_0 ⊗_{A_0} A`. Set `Y_0 = Spec(A_0)`,
`X_0 = Spec(B_0)`, and let `f_0 : X_0 → Y_0` be the morphism corresponding to the homomorphism `A_0 → B_0`, so that
`f = f_0 ×_{Y_0} 1_Y`. It is not evident a priori that the prescheme `X_0` is integral, but we shall see that one can
reduce to this case. Let `η_0` be the generic point of `Y_0`, so that if `g` is the morphism `Y → Y_0`, one has
`g(η) = η_0`; by transitivity of fibres `(I, 3.6.4)`, one has `f⁻¹(η) = f_0⁻¹(η_0) ⊗_{𝒌(η_0)} 𝒌(η)`, and since `f⁻¹(η)`
is irreducible by hypothesis, so is `f_0⁻¹(η_0)` `(4.4.1)`. Our assertion will then result from the following lemma:

**Lemma (13.1.2).**

<!-- label: IV.13.1.2 -->

*Let `Y_0`, `Y` be two integral preschemes with generic points `η_0`, `η`, `g : Y → Y_0` a dominant morphism,
`f_0 : X_0 → Y_0` a dominant morphism such that `f_0⁻¹(η_0)` is irreducible. Let `X'_0` be the unique irreducible
component of `X_0` meeting `f_0⁻¹(η_0)` `(0_I, 2.1.8)`, and denote again by `X'_0` the reduced closed sub-prescheme of
`X_0` having `X'_0` as underlying space. Suppose that the prescheme `X = X'_0 ×_{Y_0} Y` is integral; then `X` is
isomorphic to `X'_0 ×_{Y_0} Y`.*

Indeed, if `j_0 : X'_0 → X_0` is the canonical injection, which is a closed immersion,
`j = j_0 ×_{Y_0} 1_Y : X'_0 ×_{Y_0} Y → X_0 ×_{Y_0} Y = X` is a closed immersion. On the other hand, `X'_0` contains the
fibre `f_0⁻¹(η_0)`, so `X'_0 ×_{Y_0} Y` contains `f⁻¹(η)`; note moreover that `f⁻¹(η)` is non-empty `(I, 3.4.7)`, hence
contains the generic point of `X`; consequently the image of `j` is necessarily all of `X`. But since `X` is integral,
the only closed sub-prescheme of `X` having `X` as underlying space is `X` itself, hence `j` is an isomorphism.

This lemma being established, one may therefore suppose that `X_0` is integral; for every `y_0 ∈ Y_0`, `𝒪_{y_0}` is a
`ℤ`-algebra essentially of finite type, hence a universally catenary ring

<!-- original page 189 -->

`(5.6.4)`; consequently, for every `y_0 ∈ f_0(X_0)`, every irreducible component of `f_0⁻¹(y_0)` has dimension `≥ e`,
since one knows that `dim(f_0⁻¹(η_0)) = e` by transitivity of fibres `(4.1.4)`. For every `y ∈ f(X)`, one then has
`y_0 = g(y) ∈ f_0(X_0)`, and by transitivity of fibres and `(4.2.7)` one completes the proof.

**Theorem (13.1.3) (Chevalley).**

<!-- label: IV.13.1.3 -->

*Let `f : X → Y` be a morphism locally of finite type. For every integer `n`, the set `F_n(X)` of `x ∈ X` such that
`dim_x(f⁻¹(f(x))) ≥ n` is closed; in other words, the function `x ↦ dim_x(f⁻¹(f(x)))` is upper semi-continuous in `X`.*

I) Suppose first that `f` is locally of finite presentation.

The question is evidently local on `X` and on `Y`, and one may therefore suppose `Y = Spec(A)`, `X = Spec(B)` affine,
`B` being an `A`-algebra of finite presentation. One then knows `(8.9.1)` that there is a Noetherian sub-ring `A_0` of
`A` and an `A_0`-algebra of finite type `B_0` such that, if one sets `Y_0 = Spec(A_0)`, `X_0 = Spec(B_0)`, one has
`X = X_0 ×_{Y_0} Y`, `f = f_0 ×_{Y_0} 1_Y`, where `f_0 : X_0 → Y_0` corresponds to the homomorphism `A_0 → B_0`. Let
`g : Y → Y_0` be the morphism corresponding to the canonical injection `A_0 → A`, `y` a point of `Y`, `y_0 = g(y)`; one
knows that `f⁻¹(y) = f_0⁻¹(y_0) ⊗_{𝒌(y_0)} 𝒌(y)`, and it follows from `(4.2.7)` that if `p` is the canonical projection
`f⁻¹(y) → f_0⁻¹(y_0)`, the irreducible components of `f⁻¹(y)` are the irreducible components of the sets `p⁻¹(Z_0)`,
where `Z_0` ranges over the set of irreducible components of `f_0⁻¹(y_0)`, and each of the irreducible components of
`p⁻¹(Z_0)` dominates `Z_0` and has dimension equal to `dim(Z_0)`. Taking `(0, 14.1.5)` into account, one sees that if
`g' : X → X_0` is the canonical projection, `x` a point of `X` and `x_0 = g'(x)`, one has
`dim_x(f⁻¹(f(x))) = dim_{x_0}(f_0⁻¹(f_0(x_0)))`, whence `F_n(X) = g'⁻¹(F_n(X_0))`, and one is consequently reduced to
proving the theorem when `Y` is Noetherian, which we shall suppose henceforth.

One may evidently suppose `X` and `Y` reduced `(1.5.4)`. Considering the set of closed subsets `Y'` of `Y` such that the
theorem is true for the closed sub-prescheme of `Y` having `Y'` as underlying space and for `X' = f⁻¹(Y')`, one may argue
by Noetherian induction `(0_I, 2.2.2)` and suppose that the theorem is true for every closed subset `Y' ≠ Y` of `Y`. If
`X_i` (`1 ≤ i ≤ m`) are the reduced closed sub-preschemes of `X` having as underlying spaces the irreducible components
of `X`, one has `F_n(X) = ⋃_i F_n(X_i)` by virtue of `(0, 14.1.5)`, and one may therefore restrict to proving the theorem
for each of the `X_i`; in other words, one may suppose `X` irreducible. If `Z` is the closed sub-prescheme of `Y` having
`‾{f(X)}` as underlying space, `f` factors as `X ─g→ Z ─j→ Y`, where `j` is the canonical injection `(I, 5.2.2)`, and
`g` is of finite type `(1.5.4)`, hence it suffices to prove the theorem for `Z` and `g`; by virtue of the inductive
hypothesis, one is therefore reduced to considering only the case where `Z = Y`, in other words where `Y` is irreducible
and `f` dominant. Let then `η` be the generic point of `Y` and set `e = dim(f⁻¹(η))`; it follows from `(13.1.1)` that
for `n ≤ e` one has `F_n(X) = X`, and consequently one may restrict to the case where `n > e`. But then `(9.5.6)`, there
is an open neighbourhood `U` of `η` in `Y` such that `F_n(X) ⊂ f⁻¹(Y − U)`; since `Y − U ≠ Y`, the inductive hypothesis
entails that `F_n(X)` is closed.

II) We now pass to the general case, still supposing that `S = Spec(A)` and `X = Spec(B)` are affine, `B` being an
`A`-algebra of finite type, hence of the form

<!-- original page 190 -->

`B = A[T_1, …, T_n]/𝔍`. Let `(𝔍_λ)` be the family of ideals of finite type of `A[T_1, …, T_n]` contained in `𝔍`, so that
`𝔍` is the filtered union of the `𝔍_λ`; if `X` and the `X_λ = Spec(A[T_1, …, T_n]/𝔍_λ)` are considered as closed
sub-preschemes of `Z = Spec(A[T_1, …, T_n])`, one therefore has, for the underlying spaces, `X = ⋂_λ X_λ`. If
`f_λ : X_λ → S` is the structure morphism, one deduces that `f⁻¹(s) = ⋂_λ f_λ⁻¹(s)` for every `s ∈ S`, and since the
sets `f_λ⁻¹(s)` are closed in the Noetherian space `Z_s`, there exists a `λ` (depending on `s`) such that
`f⁻¹(s) = f_λ⁻¹(s)`. If then, for every `x ∈ X`, one sets `d(x) = dim_x(f⁻¹(f(x)))`,
`d_λ(x) = dim_x(f_λ⁻¹(f_λ(x)))`, what precedes proves that one has `d(x) = inf_λ d_λ(x)`; the functions `d_λ` being
upper semi-continuous by the first part of the proof, so is `d`. Q.E.D.

**Corollary (13.1.4).**

<!-- label: IV.13.1.4 -->

*Under the hypotheses of `(13.1.3)`, the set of `x ∈ X` such that `x` is isolated in `f⁻¹(f(x))` is open in `X`.*

Indeed, it is the complement of `F_1(X)` `(0, 14.1.10)`.

One notes that one recovers in this way, under more general hypotheses, the consequence `(III, 4.4.10)` of Zariski's
"Main theorem".

**Corollary (13.1.5).**

<!-- label: IV.13.1.5 -->

*Under the hypotheses of `(13.1.3)`, suppose moreover that `f` is a closed morphism. Then, for every integer `n`, the
set of `y ∈ Y` such that `dim(f⁻¹(y)) ≥ n` is closed; in other words, the map `y ↦ dim(f⁻¹(y))` is upper semi-continuous;
in particular, if `y` is a specialization of `y'`, one has `dim(f⁻¹(y)) ≥ dim(f⁻¹(y'))`.*

Indeed, to say that `dim(f⁻¹(y)) ≥ n` means that `y ∈ f(F_n(X))` `(0, 14.1.6)`.

**Corollary (13.1.6).**

<!-- label: IV.13.1.6 -->

*Let `X`, `Y` be two irreducible preschemes, `f : X → Y` a dominant morphism locally of finite type. Let `ξ` (resp. `η`)
be the generic point of `X` (resp. `Y`) and let `e = dim(f⁻¹(η))`. Then, for every `x ∈ X`, one has
`dim_x(f⁻¹(f(x))) ≥ e`.*

Indeed, the set of `x` such that `dim_x(f⁻¹(f(x))) < e` is open by virtue of `(13.1.3)`, and since it cannot contain
`ξ`, it is empty.

Let us finally note the following easier result:

**Proposition (13.1.7).**

<!-- label: IV.13.1.7 -->

*Let `Y` be a quasi-compact prescheme, `f : X → Y` a morphism of finite type. There exists an integer `n` such that,
for every `y ∈ Y`, one has `dim(f⁻¹(y)) ≤ n`.*

Since there is a finite affine open cover `(V_i)` of `Y` such that each `f⁻¹(V_i)` is a finite union of affine open
sets, one is immediately reduced to the case where `Y = Spec(A)` and `X = Spec(B)` are affine, `B` being an `A`-algebra
of finite type. If `B` admits a system of `n` generators, then for every `y ∈ Y`, `B ⊗_A 𝒌(y)` is a `𝒌(y)`-algebra
admitting `n` generators, hence `dim(f⁻¹(y)) ≤ n` by virtue of `(4.1.1)`.

### 13.2. Equidimensional morphisms: case of dominant morphisms of irreducible preschemes

**(13.2.1)** Let `Y` be an irreducible prescheme, `X` an irreducible prescheme, `f : X → Y` a dominant morphism locally
of finite type; let `η` be the generic point of `Y`. One knows `(13.1.6)` that for every `x ∈ X`, one has

<!-- original page 191 -->

```text
                       dim_x(f⁻¹(f(x))) ≥ dim(f⁻¹(η)).
```

**Definition (13.2.2).**

<!-- label: IV.13.2.2 -->

*Under the hypotheses of `(13.2.1)`, we say that `f` is **equidimensional at the point `x`** (or that `X` is
**equidimensional over `Y` at the point `x`**) if*

```text
                       dim_x(f⁻¹(f(x))) = dim(f⁻¹(η)).
```

*We say that `f` is **equidimensional** (or that `X` is **equidimensional over `Y`**) if `f` is equidimensional at every
point `x ∈ X`.*

It follows from Chevalley's theorem `(13.1.3)` that the set of `x ∈ X` where `f` is equidimensional is *open and
non-empty*. Moreover, if `f` is equidimensional at the point `x`, every irreducible component of `f⁻¹(f(x))` that
contains `x` has the same dimension, since each of them has a dimension which is `≥ dim(f⁻¹(η))` `(13.1.6)` and
`≤ dim_x(f⁻¹(f(x)))` by virtue of `(0, 14.1.5)`.

**Proposition (13.2.3).**

<!-- label: IV.13.2.3 -->

*Let `Y` be a locally Noetherian irreducible prescheme, `X` an irreducible prescheme, `f : X → Y` a dominant morphism
locally of finite type; let `η` be the generic point of `Y`, `x` a point of `X`, `y = f(x)`, and suppose that one has*

```text
  (13.2.3.1)            dim(𝒪_x) = dim(𝒪_y) + dim(𝒪_x ⊗_{𝒪_y} 𝒌(y)).
```

*Then `f` is equidimensional at the point `x`. The converse is true if the two sides of the inequality `(5.6.5.2)` are
equal, in particular if `𝒪_y` is universally catenary.*

This follows at once from `(5.6.5.2)` and the inequality `δ(x) ≥ 0` `(13.1.1)`.

**(13.2.4)** Let now, in a general way, `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism of finite type,
`x` a point of `X`, `X'` an irreducible closed subset of `X` containing `x`, `y = f(x)`, `Y' = ‾{f(X')}`, `η'` the
generic point of `Y'`. Denote again by `X'` and `Y'` the reduced closed sub-preschemes of `X` and `Y` respectively
having `X'` and `Y'` as underlying spaces; the restriction `X' → Y` of `f` factors then as `X' ─f'→ Y' ─j→ Y`, where `j`
is the canonical injection `(I, 5.2.2)`, and `f'` is of finite type `(1.5.4)`. Set then, to abbreviate,

```text
  (13.2.4.1)        A = 𝒪_{Y, y},   B = 𝒪_{X, x},   A' = 𝒪_{Y', y},   B' = 𝒪_{X', x}.
```

Formula `(5.6.5.2)` applied to the dominant morphism `f'` and to the irreducible preschemes `X'`, `Y'` gives

```text
  (13.2.4.2)        dim(B') ≤ dim(A') + dim(B' ⊗_{A'} 𝒌(y)) − (dim_x(f'⁻¹(y)) − dim(f'⁻¹(η'))).
```

On the other hand, the local ring `A'` (resp. `B'`, `B' ⊗_{A'} 𝒌(y)`) is a quotient ring of `A` (resp. `B`,
`B ⊗_A 𝒌(y)`), hence `(0, 16.1.2.1)` one has

```text
  (13.2.4.3)    dim(A') ≤ dim(A),   dim(B') ≤ dim(B),   dim(B' ⊗_{A'} 𝒌(y)) ≤ dim(B ⊗_A 𝒌(y)).
```

One deduces therefore first from `(13.2.4.3)` and `(0, 16.3.9)`

```text
  (13.2.4.4)            dim(B') ≤ dim(A') + dim(B' ⊗_{A'} 𝒌(y)) ≤ dim(A) + dim(B ⊗_A 𝒌(y)).
```

Moreover, by virtue of `(0, 16.3.9)`, one also has the inequalities

```text
  (13.2.4.5)            dim(B') ≤ dim(B) ≤ dim(A) + dim(B ⊗_A 𝒌(y)).
```

<!-- original page 192 -->

The comparison of these inequalities therefore shows that:

**Lemma (13.2.5).**

<!-- label: IV.13.2.5 -->

*With the notations of `(13.2.4)`, the following conditions are equivalent:*

*a) `dim(B') = dim(A) + dim(B ⊗_A 𝒌(y))`.*

*b) One has simultaneously the following relations:*

*(i) `dim(A') = dim(A)`.*

*(ii) `dim(B' ⊗_{A'} 𝒌(y)) = dim(B ⊗_A 𝒌(y))`, in other words*

```text
                       dim_x(X' ∩ f⁻¹(y)) = dim_x(f⁻¹(y)).
```

*(iii) `dim_x(f'⁻¹(y)) = dim(f'⁻¹(η'))`, in other words `f' : X' → Y'` is equidimensional `(13.2.2)` at the point `x`.*

*(iv) One has the equality*

```text
                       dim(B') = dim(A') + dim(B' ⊗_{A'} 𝒌(y))
```

*(a relation which is always satisfied when `A = 𝒪_{Y, y}` is a universally catenary ring, in virtue of `(5.6.5)`).*

*c) One has simultaneously the following relations:*

*(i) `dim(B') = dim(B)`.*

*(ii) `dim(B) = dim(A) + dim(B ⊗_A 𝒌(y))`.*

**(13.2.6)** Let us now recall that the irreducible components `X_i` of `X` containing `x` are in finite number and
that one has (`(5.1.2.1)` and `(0, 14.2.1.1)`)

```text
  (13.2.6.1)            dim(𝒪_{X, x}) = sup_i dim(𝒪_{X_i, x}).
```

The equivalence of conditions b) and c) in `(13.2.5)` implies consequently, in view of `(0, 16.3.9)` and `(0, 14.2.1)`:

**Proposition (13.2.7).**

<!-- label: IV.13.2.7 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism of finite type, `x` a point of `X`, `f(x) = y`; one
has*

```text
  (13.2.7.1)            dim(𝒪_{X, x}) ≤ dim(𝒪_{Y, y}) + dim(𝒪_{X, x} ⊗_{𝒪_{Y, y}} 𝒌(y)).
```

*For the two sides of `(13.2.7.1)` to be equal, it is necessary and sufficient that there exist an irreducible closed
subset `X'` of `X` containing `x` and satisfying simultaneously the following conditions:*

*(i) If `Y' = ‾{f(X')}`, one has `dim(𝒪_{Y', y}) = dim(𝒪_{Y, y})`.*

*(ii) `dim_x(X' ∩ f⁻¹(y)) = dim_x(f⁻¹(y))` (in other words, `X'` contains one of the irreducible components of `f⁻¹(y)`
that contain `x`, of maximal dimension among all these components). This amounts to saying that
`dim(𝒪_{X, x} ⊗_{𝒪_{Y, y}} 𝒌(y)) = dim(𝒪_{X', x} ⊗_{𝒪_{Y', y}} 𝒌(y))`.*

*(iii) `X'` is equidimensional over `Y'` at the point `x`, in other words, one has*

```text
                       dim_x(X' ∩ f⁻¹(y)) = dim(X' ∩ f'⁻¹(η')),
```

*where `η'` is the generic point of `Y'` (and consequently, all the irreducible components of `X' ∩ f⁻¹(y)` containing
`x` have the same dimension `(13.2.2)`).*

<!-- original page 193 -->

*(iv) One has the equality*

```text
                       dim(𝒪_{X', x}) = dim(𝒪_{Y', y}) + dim(𝒪_{X', x} ⊗_{𝒪_{Y', y}} 𝒌(y))
```

*(a condition always implied by (iii) when `𝒪_{Y, y}` is a universally catenary ring).*

*Moreover, `X'` is then an irreducible component of `X` and `Y'` an irreducible component of `Y`.*

In the statement, the local rings `𝒪_{X', x}` and `𝒪_{Y', y}` refer to the reduced closed sub-preschemes of `X`, `Y`
having `X'` and `Y'` respectively as underlying spaces.

Moreover, this proves the following:

**Corollary (13.2.8).**

<!-- label: IV.13.2.8 -->

*If the two sides of `(13.2.7.1)` are equal, the irreducible closed subsets `X'` of `X` containing `x` and satisfying
conditions (i) to (iv) of `(13.2.7)` are exactly those for which one has `dim(𝒪_{X', x}) = dim(𝒪_{X, x})` (which
necessarily implies that `X'` is an irreducible component of `X`).*

Proposition `(13.2.7)` entails:

**Corollary (13.2.9).**

<!-- label: IV.13.2.9 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism of finite type, `x` a point of `X`, `f(x) = y`.
Suppose that `𝒪_{Y, y}` is a universally catenary ring. Then the following conditions are equivalent:*

*a) The two sides of `(13.2.7.1)` are equal.*

*b) There exists an irreducible component `Z` of `f⁻¹(y)` containing `x`, of dimension `dim_x(f⁻¹(y))`, such that for
every `x'` in a neighbourhood of `x` in `Z`, one has*

```text
  (13.2.9.1)        dim(𝒪_{X, x'}) = dim(𝒪_{Y, y}) + dim(𝒪_{X, x} ⊗_{𝒪_{Y, y}} 𝒌(y)).
```

*c) There exists an irreducible component `Z` of `f⁻¹(y)` containing `x`, of dimension `dim_x(f⁻¹(y))`, such that for
the generic point `z` of `Z`, one has*

```text
  (13.2.9.2)            dim(𝒪_{X, z}) = dim(𝒪_{Y, y}).
```

Let us show that a) entails b). Set `dim_x(f⁻¹(y)) = n`; by virtue of `(13.2.7)`, there exists an irreducible component
`X'` of `X` satisfying conditions (i) to (iv) of `(13.2.7)`; let `Z` be an irreducible component of dimension `n` of
`f⁻¹(y)`, containing `x` and contained in `X'`. Since `f⁻¹(y)` is locally Noetherian, there exists an open
neighbourhood `U` of `x` in `Z` such that `U` meets no irreducible component of `f⁻¹(y)` other than those that contain
`x`, hence `(4.1.1.3)` `dim_{x'}(f⁻¹(y)) = n` for every `x' ∈ U`; it is then clear that conditions (i) to (iii) of
`(13.2.7)` are satisfied when one replaces `x` by an arbitrary point `x' ∈ U`, and so is condition (iv) since
`𝒪_{Y, y}` is universally catenary; whence the conclusion by `(13.2.7)`. Condition b) trivially entails c) by virtue
of `(5.1.2)`. Finally, if c) is satisfied and if `X''` is an irreducible component of `X` containing `Z` and such that
conditions (i) to (iv) of `(13.2.7)` are satisfied when one replaces `X'` by `X''` and `x` by `z`, it is clear that
these conditions are also satisfied for `X''` and `x` since `𝒪_{Y, y}` is universally catenary, hence c) implies a).

**Proposition (13.2.10).**

<!-- label: IV.13.2.10 -->

*Let `Y` be a locally Noetherian irreducible prescheme, `η` its generic point, `f : X → Y` a morphism of finite type, `y`
a point of `f(X)`. Let `Z_i` be the*

<!-- original page 194 -->

*irreducible components of `f⁻¹(y)`, `z_i` the generic point of `Z_i`, and consider the following conditions:*

*a) For every `x ∈ f⁻¹(y)`, one has the relation*

```text
  (13.2.10.1)       dim(𝒪_{X, x}) = dim(𝒪_{Y, y}) + dim(𝒪_{X, x} ⊗_{𝒪_{Y, y}} 𝒌(y)).
```

*b) For every `i`, one has*

```text
  (13.2.10.2)           dim(𝒪_{X, z_i}) = dim(𝒪_{Y, y}).
```

*c) For every `i`, there exists an irreducible component `X_i` of `X` containing `Z_i` and such that
`dim(X_i ∩ f⁻¹(η)) = dim(Z_i)` (in other words, such that the reduced closed sub-prescheme `X_i` of `X` is
equidimensional over `Y` at the point `z_i`).*

*Then a) entails b) and b) entails c); moreover, if `𝒪_{Y, y}` is universally catenary, the three conditions a), b),
c) are equivalent.*

The ring `𝒪_{X, z_i} ⊗_{𝒪_{Y, y}} 𝒌(y)` being of dimension `0` `(5.1.2)`, a) evidently entails b); b) entails c) by
virtue of `(13.2.7)` applied at the point `z_i`. Conversely, suppose that `𝒪_{Y, y}` is universally catenary; since
condition c) implies that `f(X_i)` is dense in `Y`, it follows from c) that conditions (i) to (iv) of `(13.2.7)` are
satisfied on replacing `X'` by `X_i` and `x` by `z_i`, hence c) implies b); finally b) implies a) by virtue of
`(13.2.9)`.

**Corollary (13.2.11).**

<!-- label: IV.13.2.11 -->

*The notations being those of `(13.2.10)`, suppose that `𝒪_{Y, y}` is universally catenary. For every `y' ∈ Y`, let
`E(y')` be the set of dimensions of the irreducible components of `f⁻¹(y')` and set
`d(y') = dim(f⁻¹(y')) = sup(E(y'))`. Then, if the equivalent conditions a), b), c) of `(13.2.10)` are satisfied, one
has `E(y) ⊂ E(η)`, whence `d(y) ≤ d(η)`.*

Indeed, with the notations of `(13.2.10)`, `X_i ∩ f⁻¹(η)` is non-empty and is consequently an irreducible component of
`f⁻¹(η)` `(0_I, 2.1.8)`.

**Remarks (13.2.12).**

<!-- label: IV.13.2.12 -->

(i) Recall `(6.1.2)` that the relation `(13.2.10.1)` is always satisfied when the morphism `f` is flat at the point `x`.

(ii) With the notations of `(13.2.10)`, suppose that `𝒪_{Y, y}` is universally catenary and moreover that the morphism
`f` is proper; then, if the equivalent conditions a), b), c) of `(13.2.10)` are satisfied, one has even `d(y) = d(η)`,
since it follows from `(13.1.5)` that one has `d(y) ≥ d(η)`.

(iii) The morphism of `(12.2.3, (b))` is proper and flat and all local rings of `Y` are universally catenary; moreover,
the two irreducible components `X_1`, `X_2` of `X` are equidimensional over `Y` at every point; but `E(y)` has *two*
elements for every `y ≠ y_0`, while `E(y_0)` is reduced to a *single* element, hence `E(y)` is not constant on `Y`.

### 13.3. Equidimensional morphisms: general case

**Proposition (13.3.1).**

<!-- label: IV.13.3.1 -->

*Let `Y` be a prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`, `y = f(x)`. Denote by `Y_α`
the irreducible components of `Y` containing `y`. Then the following conditions are equivalent:*

<!-- original page 195 -->

*a) There exist an integer `e` and an open neighbourhood `U` of `x` such that the image under `f` of every irreducible
component of `U` is dense in some `Y_α`, and that, for every `x' ∈ U`, the space `U ∩ f⁻¹(f(x'))` is equidimensional
and of dimension `e`.*

*a') There exist an integer `e` and an open neighbourhood `U` of `x` such that the image under `f` of every irreducible
component of `U` is dense in some `Y_α` and such that, if one denotes by `y_α` the generic point of `Y_α`, every
irreducible component of the spaces `U ∩ f⁻¹(y)`, `U ∩ f⁻¹(y_α)` is of dimension `e`.*

*a'') There exist an integer `e` and an open neighbourhood `U` of `x` such that, for each of the irreducible components
`U_λ` of `U`, `f(U_λ)` is dense in some `Y_α` and such that, for every `x' ∈ U_λ`, the irreducible components of
`U_λ ∩ f⁻¹(f(x'))` are all of dimension `e`.*

*b) There exist an integer `e`, an open neighbourhood `U` of `x` and a `Y`-morphism quasi-finite
`g : U → Y ⊗_ℤ ℤ[T_1, …, T_e]` (a prescheme that we shall also denote `Y[T_1, …, T_e]` for brevity) such that the image
under `g` of every irreducible component of `U` is dense in an irreducible component of `Y[T_1, …, T_e]`.*

It is immediate that a'') entails a), for, for every `x ∈ U`, the irreducible components of `U ∩ f⁻¹(f(x))` are each an
irreducible component of one of the `U_λ ∩ f⁻¹(f(x))`, whence the conclusion by `(0, 14.1.4)`. Condition a) trivially
entails a'). Let us next show that a') entails a''); one may restrict to the case where `f` is of finite type and `X`
and `Y` reduced `(1.5.4)`. Let `U_λ` be an irreducible component of `U`, and suppose that `f(U_λ)` is dense in `Y_α`;
then the restriction of `f` to `U_λ` factors as `U_λ ─f_α→ Y_α ─→ Y`, where `f_α` is of finite type and dominant
`(I, 5.2.2)`. Let `x_λ` be the generic point of `U_λ`; by virtue of `(0_I, 2.1.8)`, `U_λ ∩ f_α⁻¹(y_α)` is the unique
irreducible component of `U ∩ f⁻¹(y_α)` containing `x_λ` and is by hypothesis of dimension `e`, equal to the dimensions
of all the irreducible components of `U_λ ∩ f⁻¹(y)`, by virtue of the hypothesis and of `(13.1.1)`. But by virtue of
Chevalley's theorem `(13.1.3)` and of `(13.1.1)`, the set `V_λ` of `x' ∈ U_λ` such that
`dim_{x'}(f_α⁻¹(f_α(x'))) = e` is open and contains `x`, and it suffices to take the union of the `V_λ` to obtain an
open set satisfying the conditions of a'').

Let us now prove that a) entails b); one may restrict to the case where `Y = Spec(A)` and `X = Spec(B)` are affine and
where `U = X`. Let us first prove the following lemma:

**Lemma (13.3.1.1).**

<!-- label: IV.13.3.1.1 -->

*Let `Y = Spec(A)`, `X = Spec(B)` be two affine schemes, `f : X → Y` a morphism of finite type, `y` a point of `f(X)`,
and set `e = dim(f⁻¹(y))`. Then there exists a `Y`-morphism `g : X → Y[T_1, …, T_e]` such that (if one sets
`X_y = X ×_Y Spec(𝒌(y))`) the morphism `g_y : X_y → Spec(𝒌(y)[T_1, …, T_e])` is finite. Moreover, for such a morphism
`g`, `g_y` is necessarily surjective and there exists an open neighbourhood `U` of `f⁻¹(y)` in `X` such that `g|U` is
quasi-finite.*

Set `𝔭 = j_y`; the ring `B ⊗_A 𝒌(𝔭)` is a `𝒌(𝔭)`-algebra of finite type, hence the normalization lemma
(Bourbaki, *Alg. comm.*, chap. V, §3, n° 1, th. 1) proves that there is in `B ⊗_A 𝒌(𝔭)` a finite sequence `(t_i)_{1 ≤ i ≤ r}`
of elements algebraically independent over `𝒌(𝔭)` and such that, if one sets `C' = 𝒌(𝔭)[t_1, …, t_r]`,
`B ⊗_A 𝒌(𝔭)` is a *finite* `C'`-algebra; one therefore has `dim(B ⊗_A 𝒌(𝔭)) = dim(C')` `(0, 16.1.5)`, and since
`dim(C') = r` `(5.2.1)`, one has `r = e`. Since `B ⊗_A 𝒌(𝔭) = (B/𝔭B) ⊗_{A/𝔭} 𝒌(𝔭)`, one can, by multiplying the `t_i`
by a suitable non-zero element

<!-- original page 196 -->

of `A/𝔭`, suppose that each `t_i` is the canonical image in `B ⊗_A 𝒌(𝔭)` of an element `s_i ∈ B`. Let then
`u : A[T_1, …, T_e] → B` be the homomorphism such that `u(T_i) = s_i` for every `i`, and let `g : X → Y[T_1, …, T_e]`
be the corresponding morphism. It is clear that, by reason of the choice of the `s_i`, `g_y` is a finite morphism. For
every morphism `g : X → Y[T_1, …, T_e]` such that `g_y` is finite, it follows from `(5.4.2)` and `(4.1.2.1)` that `g_y`
is necessarily surjective. On the other hand, by virtue of `(13.1.4)`, the set `U` of `x ∈ X` that are isolated in
their fibre `g⁻¹(g(x))` is open in `X` and contains `f⁻¹(y)`, and by definition the restriction `g|U` is a quasi-finite
morphism.

This lemma being established, to prove that a) implies b), it remains to see that if `x_λ` is a maximal point of `U`,
`g(x_λ) = z_λ` is a maximal point of `Z = Y[T_1, …, T_e]`. By virtue of hypothesis a), one may (on restricting `U` if
necessary) suppose that `f(x_λ)` is one of the generic points `y_α` of the irreducible components of `Y` containing
`y`; if `p : Z → Y` is the structure morphism, one therefore has `p(z_λ) = y_α`, and one consequently deduces from `g`
a `𝒌(y_α)`-morphism quasi-finite `h : U ∩ f⁻¹(y_α) → p⁻¹(y_α)`. Now `p⁻¹(y_α) = Spec(𝒌(y_α)[T_1, …, T_e])` is integral
and of dimension `e`; if `z_λ` were not a maximal point of `Z`, it would not be a maximal point of `p⁻¹(y_α)`
`(0_I, 2.1.8)` and its closure `Z'_λ` in `p⁻¹(y_α)` would therefore be of dimension `< e` `(4.1.2.1)`. But since `h` is
quasi-finite, it follows from `(4.1.2)` and from hypothesis a) that one has `dim(Z'_λ) ≥ e` (the restriction of `h` to
`‾{x_λ}` factoring as `‾{x_λ} → Z'_λ → p⁻¹(y_α)` by virtue of `(I, 5.2.2)`); one thus arrives at a contradiction, which
shows that a) entails b).

Let us finally prove that b) implies a). Note that the structure morphism `p : Z = Y[T_1, …, T_e] → Y` is faithfully
flat; hence `(2.3.4)` the maximal points of `Z` have as their images under `p` the maximal points of `Y`; this already
proves that the `f(x_λ)` are generic points of the `Y_α`. Moreover, if `f(x_λ) = y_α`, the `𝒌(y_α)`-morphism
`h : U ∩ f⁻¹(y_α) → p⁻¹(y_α)` deduced from `g` is dominant and quasi-finite by hypothesis; one therefore has
`dim(U_λ ∩ f⁻¹(y_α)) = e` by virtue of `(4.1.2)` (`U_λ` being the irreducible component of `U` with generic point
`x_λ`). Likewise, for every `x' ∈ U_λ`, the morphism `U_λ ∩ f⁻¹(f(x')) → p⁻¹(f(x'))` deduced from `g` is a
`𝒌(f(x'))`-morphism quasi-finite, hence `(4.1.2)` one has `dim(f⁻¹(f(x')) ∩ U_λ) ≤ e`; but on the other hand one knows
`(13.1.6)` that all the irreducible components of `U_λ ∩ f⁻¹(f(x'))` are of dimension `≥ e`; one thus sees that these
components are exactly of dimension `e`, hence b) entails a). Q.E.D.

**Definition (13.3.2).**

<!-- label: IV.13.3.2 -->

*Let `Y` be a prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`. We say that `f` is
**equidimensional at the point `x`** (or that `X` is **equidimensional over `Y` at the point `x`**) if the equivalent
conditions of `(13.3.1)` are satisfied. We say that `f` is **equidimensional** (or that `X` is **equidimensional over
`Y`**) if `f` is equidimensional at every point `x ∈ X`.*

It is clear that, for `f` to be equidimensional at a point `x`, it is necessary and sufficient that `f_red` be so.
Moreover, the conditions of `(13.3.1)` show that the set of points where `f` is equidimensional is *open* in `X`.

One notes that when `X` and `Y` are irreducible, to say that `f` is equidimensional

<!-- original page 197 -->

at the point `x` means, by virtue of `(13.3.1, a'')`, that `f` is dominant and that
`dim_x(f⁻¹(f(x))) = dim(f⁻¹(η))` (where `η` is the generic point of `Y`); definition `(13.3.2)` therefore coincides in
this case with definition `(13.2.2)`.

**Proposition (13.3.3).**

<!-- label: IV.13.3.3 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`, `X_j`
the irreducible components of `X` (in finite number) containing `x`. For `f` to be equidimensional at the point `x`, it
is necessary and sufficient that, for every `j`, `Y_j = ‾{f(X_j)}` be an irreducible component of `Y` and, denoting by
`X_j` and `Y_j` the reduced closed sub-preschemes of `X` and `Y` with `X_j` and `Y_j` as underlying spaces, by
`f_j : X_j → Y_j` the morphism deduced from `f` `(I, 5.2.2)`, by `y_j` the generic point of `Y_j`, that `f_j` be
equidimensional at the point `x` and that all the numbers `dim(f_j⁻¹(y_j))` be equal.*

This follows at once from `(13.3.1, a')`.

**Corollary (13.3.4).**

<!-- label: IV.13.3.4 -->

*With the notations of `(13.3.3)`, set `y = f(x)`. If `𝒪_{Y, y}` is a universally catenary ring and if `f` is
equidimensional at the point `x`, one has*

```text
  (13.3.4.1)        dim(𝒪_{X_j, x}) = dim(𝒪_{Y_j, y}) + e − deg.tr_{𝒌(y)} 𝒌(x)
```

*where `e` is the common value of the numbers `dim(f_j⁻¹(y_j))`.*

Since each of the `𝒪_{Y_j, y}`, a quotient of `𝒪_{Y, y}`, is a universally catenary ring `(5.6.1)`, the equality is a
consequence of `(5.6.5)`.

**Corollary (13.3.5).**

<!-- label: IV.13.3.5 -->

*With the notations of `(13.3.4)`, suppose that `f` is equidimensional at the point `x` and that `𝒪_{Y, y}` is a
universally catenary ring. If the ring `𝒪_{Y, y}` is equidimensional, so is `𝒪_{X, x}`. The converse is true if the
image under `f` of the union of the `X_j` is dense in a neighbourhood of `y`.*

Indeed, to say that `𝒪_{Y, y}` is equidimensional means that the numbers `dim(𝒪_{Y'_i, y})` are equal for all the
irreducible components `Y'_i` of `Y` containing `y`, as follows from `(5.1.1.5)` applied to the local scheme
`Spec(𝒪_{Y, y})`; since one has the relation `(13.3.4.1)`, it follows by the same reasoning that `𝒪_{X, x}` is then
equidimensional. Conversely, if `𝒪_{X, x}` is equidimensional, all the numbers `dim(𝒪_{Y_j, y})` are equal by
`(13.3.4.1)`; one deduces that `𝒪_{Y, y}` is equidimensional if the `Y_j` are *all* the irreducible components of `Y`
containing `y`, which follows from the additional hypothesis.

**Proposition (13.3.6).**

<!-- label: IV.13.3.6 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`,
`y = f(x)`. Suppose that the ring `𝒪_y` is equidimensional. Then, if `𝒪_x` is equidimensional and if one has the
equality*

```text
  (13.3.6.1)        dim(𝒪_x) = dim(𝒪_y) + dim(𝒪_x ⊗_{𝒪_y} 𝒌(y))
```

*(cf. `(13.2.7.1)`), `f` is equidimensional at the point `x`, and the converse is true if `𝒪_y` is a universally
catenary ring.*

Let us keep the notations of `(13.3.3)`; it follows from `(13.2.8)` and from the hypothesis that `𝒪_x` is
equidimensional, that each of the `Y_j` is an irreducible component of `Y` and that each of the `f_j` is
equidimensional at the point `x`; moreover `(13.2.8)`, one has (taking `(5.6.5)` into account)

```text
  dim(𝒪_{X_j, x}) = dim(𝒪_{Y_j, y}) + dim_x(X_j ∩ f⁻¹(y)) − deg.tr_{𝒌(y)} 𝒌(x).
```

<!-- original page 198 -->

Now, since `𝒪_y` is supposed equidimensional, this equality is written

```text
  (13.3.6.2)        dim_x(X_j ∩ f⁻¹(y)) = dim(𝒪_{X, x}) − dim(𝒪_{Y, y}) + deg.tr_{𝒌(y)} 𝒌(x).
```

The left-hand side of `(13.3.6.2)` is therefore independent of `j`; but since `f_j` is equidimensional at the point
`x`, one has `dim_x(X_j ∩ f⁻¹(y)) = dim(f_j⁻¹(y_j))`, hence the criterion `(13.3.3)` shows that `f` is equidimensional
at the point `x`.

Conversely, suppose that `𝒪_{Y, y}` is a universally catenary ring and that `f` is equidimensional at the point `x`;
then `(13.3.5)` `𝒪_{X, x}` is equidimensional, and it then follows from `(13.3.4)` that one has the relation

```text
  dim(𝒪_{X, x}) = dim(𝒪_{Y, y}) + e − deg.tr_{𝒌(y)} 𝒌(x)
```

where `e` is the common value of the numbers `dim(f_j⁻¹(y_j)) = dim_x(X_j ∩ f⁻¹(y))`; but by definition `e` is also
equal to `dim_x(f⁻¹(y))`, whence the relation `(13.3.6.1)`, taking `(5.6.5.2)` into account.

**Proposition (13.3.7).**

<!-- label: IV.13.3.7 -->

*Let `Y` be a prescheme, `f : X → Y` a morphism locally of finite type and equidimensional, `Z` a closed subset of `X`.
Then the function*

```text
  (13.3.7.1)            x ↦ codim_x(Z ∩ f⁻¹(f(x)), f⁻¹(f(x)))
```

*is lower semi-continuous in `X`.*

Since all the irreducible components of `f⁻¹(f(x))` containing `x` have by hypothesis the same dimension `(13.3.1)`,
one has, by virtue of `(5.2.1)`,

```text
  codim_x(Z ∩ f⁻¹(f(x)), f⁻¹(f(x))) = dim_x(f⁻¹(f(x))) − dim_x(Z ∩ f⁻¹(f(x))).
```

But by hypothesis the first term of the right-hand side is a *continuous* function of `x` `(13.3.1)` and the second is
an upper semi-continuous function of `x` by virtue of `(13.3.3)`; whence the conclusion.

**Proposition (13.3.8).**

<!-- label: IV.13.3.8 -->

*Let `Y` be a prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`. Let `Y'` be a prescheme,
`g : Y' → Y` a flat morphism, `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`; if `f` is equidimensional at the point `x`,
then `f'` is equidimensional at every point `x' ∈ X'` above `x`.*

The question being local on `X` and `Y`, one may restrict to the case where every irreducible component of `X` (resp.
`Y`) contains `x` (resp. `y`); since the image under `f` of every irreducible component of `X` is then dense in an
irreducible component of `Y` `(13.3.1)`, one knows `(2.3.5)` that the image under `f'` of every irreducible component
of `X'` is dense in an irreducible component of `Y'`. On the other hand, by transitivity of fibres `(I, 3.6.4)`, it
follows from `(4.2.8)` and from `(13.3.1)` that, for every `z' ∈ X'`, the set of dimensions of the irreducible
components of `f'⁻¹(f'(z'))` is the same as the set of dimensions of the irreducible components of `f⁻¹(f(z))`, where
`z` is the projection of `z'` in `X`; whence the conclusion by virtue of `(13.3.1, a)`.

**Remark (13.3.9).**

<!-- label: IV.13.3.9 -->

The equidimensionality property of a morphism `f : X → Y` is not stable under arbitrary base change `g : Y' → Y`, even
when `g` is the canonical injection of an irreducible component `Y'` of `Y` into `Y` (`Y'` being

<!-- original page 199 -->

considered as a reduced closed sub-prescheme of `Y`). For example, let `k` be a field, `A_0 = k[S, T]` the polynomial
ring in two indeterminates, `𝔞 = 𝔭_1 𝔭_2`, where `𝔭_1` and `𝔭_2` are the prime ideals `A_0 S` and `A_0 T` of `A_0`; let
`A = A_0/𝔞` and `Y = Spec(A)`, which has two irreducible components `Y_1 = Spec(A/𝔭_1)`, `Y_2 = Spec(A/𝔭_2)`; take
`X = Y_1`, `f : X → Y` being the canonical injection, which is evidently an equidimensional morphism. Take on the other
hand `Y' = Y_2`, `g : Y' → Y` being the canonical injection; then one has
`X' = X ×_Y Y' = Spec((A/𝔭_1) ⊗_A (A/𝔭_2)) = Spec(A/(𝔭_1 + 𝔭_2))`, and `𝔭_1 + 𝔭_2` is a maximal ideal of `A`, hence
`X'` is reduced to a point, and the morphism `f' : X' → Y'` is *not dominant*, the image under `f'` of the unique point
of `X'` being a closed point of `Y'`; hence `f'` is not equidimensional.

One can also give a counterexample where `X` and `Y` are integral, `f` finite and birational (and a fortiori
equidimensional by `(13.3.1, b)`), `g : Y' → Y` finite and dominant. Let `A` and `Ā` be the local rings defined in
`(11.7.5)`, and take `Y = Spec(A)`, `X = Spec(Ā)`; on the other hand, with the notations of `(11.7.5)`, take
`Y' = Spec(B)`; then `X' = Spec(Ā ⊗_A B) = Spec(B̄ ⊗_B B)`; but one verifies at once that `B̄ ⊗_B B` is the direct
composite of the rings `B̄/𝔭'`, `B̄/𝔭''` and of two rings isomorphic to `B̄/𝔫`, whose spectra are therefore reduced to
a point; since the projections of these points are closed points of `Y'`, here again one sees that `f'` does not
transform an irreducible component of `X'` into an everywhere dense part of an irreducible component of `Y'`, hence
`f'` is not equidimensional.

In this example, the ring `A` is not geometrically unibranch; we shall see in the following section `(14.4.6)` that
such phenomena cannot occur when the points of `Y` are geometrically unibranch. The lack of stability of the notion
of equidimensional morphism greatly restricts its interest, in favour of the notion of universally open morphism,
which will be studied in detail in the following section.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/25-c4-s13-morphismes-equidimensionnels.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-3.pdf -->

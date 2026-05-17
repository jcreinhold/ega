<!-- original page 173 -->

## §12. Study of the fibres of flat morphisms of finite presentation

### 12.0. Introduction

Throughout this section we shall use the general notations of `(9.4.1)`.

**(12.0.1)**

<!-- label: IV.12.0.1 -->

Given a morphism `f : X → Y` locally of finite presentation, we saw `(9.9)` that for certain *local* properties `P` of
preschemes over fields or of Modules on such preschemes, the set `E` of `x ∈ X` such that the property `P` holds for the
fibre `X_{f(x)}` at the point `x` of that fibre is locally constructible in `X`. We propose to show that, for most of
these properties, if one supposes moreover that the morphism `f` is *flat*, then the set `E` is even *open* in `X`.
Likewise (`(9.2)` through `(9.8)`) we have shown that if `f` is of finite presentation, and if this time `P` denotes
certain *global* properties of preschemes over fields or of Modules on such preschemes, then the set `F` of `y ∈ Y`
such that the property `P` holds for the fibre `X_y` is locally constructible in `Y`. We shall show that if one supposes
moreover that the morphism `f` is *proper and flat*, then `F` is even *open* in `Y`.

**(12.0.2)**

<!-- label: IV.12.0.2 -->

The general method of proof of the properties in question comprises three steps. One first reduces to the case where
`Y` is affine and `X` of finite presentation; then:

A) Using `(8.9.1)` (and possibly other results of §8) and `(11.2.6)`, one reduces to the case where `X` and `Y` are
Noetherian.

B) One applies the results of §9 recalled in `(12.0.1)` proving that `E` (resp. `F`) is constructible.

C) To see that `E` is open, it suffices, by virtue of `(0_III, 9.2.5)`, to show that if `x ∈ E`, then every generization
`x'` of `x` also belongs to `E`. Using `(II, 7.1.7)`, one sees, since `Y` is Noetherian, that there exists a spectrum of
a discrete valuation ring `Y_1` and a morphism `h : Y_1 → X` such that, if `y_1` (resp. `y'_1`) is the closed point
(resp. the generic point) of `Y_1`, one has `h(y_1) = x`, `h(y'_1) = x'`. One then makes the base change
`g = f ∘ h : Y_1 → Y`; taking into account the results of §§4 and 6 on locally Noetherian preschemes over fields and
changes of base field, one is reduced to proving the assertion in question for a point `x_1` of `X_1 = X ×_Y Y_1` above
`y_1` and for a generization `x'_1` of `x_1` above `y'_1`. Since `Y_1 = Spec(A)`, where `A` is a discrete valuation
ring with uniformizer `t`, one must in the end, for an `A`-module `M`, prove a property of `M`, knowing that `M/tM` has
the same property and that `t` is `M`-regular (which follows from the flatness hypothesis); for this one uses the
results of `(3.4)` and `(5.12)`. One proceeds in the same way for the set `F ⊂ Y`.

<!-- original page 174 -->

### 12.1. Local properties of the fibres of a flat morphism locally of finite presentation

**Theorem (12.1.1).**

<!-- label: IV.12.1.1 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `ℱ` an `𝒪_X`-Module that is `f`-flat and of finite
presentation, `Φ` a finite subset of `ℤ ∪ {±∞}`, `k` an integer. The following subsets of `X` are open:*

*(i) The set of `x ∈ X` such that the dimensions of the associated prime cycles of `ℱ_{f(x)}` containing `x` are elements
of `Φ`.*

*(ii) The set of `x ∈ X` such that the associated prime cycles of `ℱ_{f(x)}` containing `x` all have dimension `k`.*

*(iii) The set of `x ∈ X` such that `x` belongs to no embedded associated prime cycle of `ℱ_{f(x)}`.*

*(iv) The set of `x ∈ X` such that `ℱ_{f(x)}` is equidimensional at the point `x` and possesses property `(S_k)` at the
point `x` `(5.7.2)`.*

*(v) The set of `x ∈ X` such that `coprof((ℱ_{f(x)})_x) ≤ k` `(0, 16.4.9)`.*

*(vi) The set of `x ∈ X` such that `ℱ_{f(x)}` is a Cohen-Macaulay `𝒪_X`-Module at the point `x` `(5.7.1)`.*

*(vii) The set of `x ∈ X` such that `ℱ_{f(x)}` is geometrically reduced at the point `x` `(4.6.22)`.*

*(viii) The set of `x ∈ X` such that `ℱ_{f(x)}` is geometrically pointwise integral at the point `x` `(4.6.22)`.*

The questions being local on `X`, one reduces first to the case where `X = Spec(B)` and `Y = Spec(A)` are affine, with
`f` a morphism of finite presentation. There then exists a Noetherian sub-ring `A_0` of `A`, an `A_0`-prescheme of
finite type `X_0`, and a coherent `𝒪_{X_0}`-Module `ℱ_0` such that `ℱ_0 ⊗_{A_0} A` is isomorphic to `ℱ` `(8.9.1)`; in
addition, by virtue of `(11.2.6)`, one may suppose that `ℱ_0` is `Y_0`-flat (with `Y_0 = Spec(A_0)`). If
`h : X → X_0` is the canonical projection, the set `E` of points `x ∈ X` where one of properties (i) to (viii) holds is
equal to `h⁻¹(E_0)`, where `E_0` is the set of `x_0 ∈ X_0` where the corresponding property for `ℱ_0` holds: this
follows, for properties (i) to (iii), from `(4.2.7)`; for properties (iv) to (vi), from `(6.7.1)`; for properties (vii)
and (viii), from `(4.7.11)`.

One is thus reduced to the case where `A` and `B` are Noetherian, `f` of finite type, and `ℱ = M̃`, where `M` is a
`B`-module of finite type. By virtue of `(9.9.2)`, one knows that the set `E` is constructible for all the properties
considered, and there remains in each case step C) of `(12.0.2)`, where one must prove that `E` is stable under
generization.

**(12.1.1.1)**

<!-- label: IV.12.1.1.1 -->

Let us begin with case (iii), which is the simplest. Let `x' ≠ x` be a generization of `x` in `X`. Set `y = f(x)`,
`y' = f(x')`; there exists a spectrum of a discrete valuation ring `Y_1` and a morphism `u : Y_1 → X` such that, if
`y_1` and `y'_1` are the closed point and the generic point of `Y_1`, one has `u(y_1) = x` and `u(y'_1) = x'`
`(II, 7.1.7)`; set `g = f ∘ u : Y_1 → Y`; if `X_1 = X ×_Y Y_1`, there exists a `Y_1`-section `u_1 : Y_1 → X_1` such that
`u = g_1 ∘ u_1`, where `g_1 : X_1 → X` is the canonical projection. Setting `x_1 = u_1(y_1)`, `x'_1 = u_1(y'_1)`, one
therefore has `g_1(x_1) = x` and `g_1(x'_1) = x'`, and `x'_1` is a generization of `x_1`. Applying `(4.2.7)` again, one
sees

<!-- original page 175 -->

that one is reduced to the case where `Y = Spec(A)` is the spectrum of a discrete valuation ring, `y` being the closed
point and `y'` the generic point of `Y`. If `t` is a uniformizer of `A`, the hypothesis that `ℱ` is `f`-flat entails
that `t` is `ℱ`-regular `(0_I, 6.3.4)`. By hypothesis none of the embedded associated prime cycles of `ℱ/tℱ` contains
`x`. Then, it follows from `(3.4.4)` that `x` belongs to no embedded associated prime cycle of `ℱ`, and the same is
therefore true of every generization of `x`. In particular, `x'` belongs to no embedded associated prime cycle of `ℱ`,
nor *a fortiori* to any of those associated to `ℱ_{y'}` (`X_{y'}` being a sub-prescheme induced on an open set of `X`).

**(12.1.1.2)**

<!-- label: IV.12.1.1.2 -->

Let us consider next cases (iv) and (v) ((vi) is only a special case of (v)). One proceeds as above (using `(6.7.1)`
instead of `(4.2.7)`) and one is reduced to the case where `Y` is the spectrum of a discrete valuation ring `A`.

The ring `C = 𝒪_{X, x}` is then a localization of a finitely generated `A`-algebra, hence catenary `(5.6.4)`, and by
hypothesis the `C`-module `M_x/tM_x` satisfies `(S_k)` and is equidimensional (resp. one has
`coprof(M_x/tM_x) ≤ k`); one therefore deduces from `(5.12.2)` (resp. from `(0, 16.4.10)`) that `M_x` satisfies `(S_k)`
and is equidimensional (resp. that `coprof(M_x) ≤ k`), since `t` is `M_x`-regular and belongs to the maximal ideal of
`C`. Whence the conclusions, since `x'` is a generization of `x` and `(ℱ_{y'})_{x'} = ℱ_{x'}`.

**(12.1.1.3)**

<!-- label: IV.12.1.1.3 -->

Let us pass to cases (vii) and (viii). One may evidently replace `Y` by the integral sub-scheme having `‾{y}` as
underlying space, and `X` by `f⁻¹(‾{y})`, without changing the fibres at `y` and `y'`; one may therefore suppose `A`
integral, with field of fractions `K = k(y)`. One knows (`(4.5.11)` and `(4.7.8)`) that there exists a finite extension
`K'` of `K` such that, for the `(𝒪_X ⊗_A K')`-Module `ℱ' = ℱ ⊗_A K'`, the associated prime cycles are geometrically
irreducible and the geometric lengths of `ℱ'` at the maximal points `z'` of its support are respectively equal to the
lengths of `ℱ'_{z'}` at these points; it therefore amounts to the same to say that `ℱ` is geometrically reduced (resp.
geometrically pointwise integral) at a point `x'` of `X_{y'} = X ⊗_A K`, or to say that `ℱ'` is reduced (resp.
integral) at the points of `X ⊗_A K'` above `x'`, taking `(4.2.7)` into account. Let `A'` be a finite `A`-algebra of
which `K'` is the field of fractions; it follows from `(4.7.11)` that at every point of `X ⊗_A A'` above `x`,
`ℱ ⊗_A A'` has property (vii) (resp. (viii)). Replacing `A` by `A'` and `X` by `X ⊗_A A'`, one sees that one may
confine oneself to proving that `ℱ_x` is reduced (resp. integral) at every generization `x'` of `x`. One then proceeds
as in `(12.1.1.1)`, this time using `(4.7.11)`, and one is once again reduced to the case where `A` is a discrete
valuation ring, `y` being the closed point and `y'` the generic point of `Y`, with the uniformizer `t` of `A` being an
`ℱ`-regular element. Since by hypothesis `ℱ/tℱ` is reduced (resp. integral) at the point `x`, it follows from `(3.4.6)`
(resp. `(3.4.5)`) that `ℱ` is reduced (resp. integral) at the point `x`, hence also in a neighbourhood of `x`, and in
particular at the point `x'`, which completes the proof in cases (vii) and (viii).

**(12.1.1.4)**

<!-- label: IV.12.1.1.4 -->

It remains to examine cases (i) and (ii). Replacing `Y` by the integral sub-scheme having `‾{y}` as underlying space,
one may confine oneself to the case where `Y` is irreducible and `y` its generic point. Let `z'` be a generic point of
an associated prime cycle of `ℱ_{y'}`

<!-- original page 176 -->

containing `x'`, and let `Z'` be the closure of `z'` in `X`, so that one has `x ∈ Z'`. To treat case (i), it will
suffice to prove:

**Proposition (12.1.1.5).**

<!-- label: IV.12.1.1.5 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent `𝒪_X`-Module
that is `f`-flat; for every `y ∈ Y`, set `ℱ_y = ℱ ⊗_{𝒪_Y} k(y)`. Let `z'` be a point of `X`, `y' = f(z')`, and suppose
that `z' ∈ Ass(ℱ_{y'})`. Let `Z'` (resp. `Y'`) be the reduced sub-prescheme of `X` (resp. `Y`) having as underlying
space the closure of `{z'}` in `X` (resp. of `{y'}` in `Y`). Then, for every `y ∈ f(Z')`, the dimensions of all the
irreducible components of `Z'_y` are equal to `dim(Z'_{y'})` (the dimension of the closure of `z'` in `X_{y'}`) (which
we shall express later `(13.2.2)` by saying that the restriction `Z' → Y'` of `f` is an **equidimensional morphism**);
moreover, at every maximal point `z` of `Z'_y`, one has `z ∈ Ass(ℱ_y)`.*

For this, we shall reduce to the case where `Y` is the spectrum of a discrete valuation ring. Take a spectrum of a
discrete valuation ring `Y_1` and a morphism `h : Y_1 → X` such that `h(y_1) = z`, `h(y'_1) = z'`, where `y_1` and
`y'_1` are the closed point and the generic point of `Y_1` respectively `(II, 7.1.7)`. Let `g = f ∘ h : Y_1 → Y`,
`X_1 = X ×_Y Y_1`, and let `f_1 : X_1 → Y_1`, `g_1 : X_1 → X` be the canonical projections; there is a `Y_1`-section
`h_1 : Y_1 → X_1` such that `h = g_1 ∘ h_1` `(I, 3.3.14)`. If `Z'_1 = Z'_{y'} ⊗_{k(y')} k(y'_1)`, one knows `(4.2.6)`
that the irreducible components of `Z'_1` dominate `Z'_{y'}`; let `z'_1` be the generic point of one of these
components which contains `h_1(y'_1)`, so that `f_1(z'_1) = y'_1` and `g_1(z'_1) = z'`. Since `h_1(y_1)` is a
specialization of `h_1(y'_1)`, it is *a fortiori* a specialization of `z'_1`; let `z_1` be a generic point of one of
the irreducible components of `‾{z'_1} ∩ (X_1)_{y_1}` containing `h_1(y_1)`. Then `g_1(z_1)` is a specialization of
`g_1(z'_1) = z'` in `X`, and `z = h(y_1) = g_1(h_1(y_1))` is a specialization of `g_1(z_1)`; but since
`f(g_1(z_1)) = y` and `z` is a generic point of `Z'_y`, one necessarily has `z = g_1(z_1)`.

Suppose now that one has proved that, if one sets `ℱ_1 = ℱ ⊗_{𝒪_Y} 𝒪_{Y_1}`, one has `z_1 ∈ Ass((ℱ_1)_{y_1})`; it will
follow from `(4.2.7)` that `z ∈ Ass(ℱ_y)`; moreover, the dimensions of `‾{z_1} ∩ (X_1)_{y_1}` and of `‾{z} ∩ X_y` are
equal, and likewise the dimensions of `‾{z'_1} ∩ (X_1)_{y'_1}` and of `‾{z'} ∩ X_{y'}` `(4.2.7)`; one has therefore
indeed reduced, as announced, to the case where `Y` is the spectrum of a discrete valuation ring `A`, `y` and `y'`
being its closed point and its generic point respectively.

This being so, since `z_1 ∈ Ass((ℱ_1)_{y_1})`, one has *a fortiori* `z' ∈ Ass(ℱ)`. If `t` is a uniformizer of `A`, `t`
is `ℱ`-regular by flatness, hence `(3.4.3)` one has `z ∈ Ass(ℱ/tℱ) = Ass(ℱ_y)`. As for the assertion concerning
dimensions, it follows from `(7.1.13)`, applied to a closed sub-prescheme of `X` having `Z'` as underlying space.

Let us tackle finally case (ii) of `(12.1.1)`. With the same notation, one must prove that if all the associated prime
cycles of `ℱ_y` containing `x` have dimension `k`, then the same is true of all the associated prime cycles of
`ℱ_{y'}` containing `x'`. Now we have just seen that every associated prime cycle of `ℱ_{y'}` containing `x'` has the
same dimension as one of the associated prime cycles of `ℱ_y` containing `x`; this therefore proves (ii).

**Remarks (12.1.2).**

<!-- label: IV.12.1.2 -->

*(i) Under the conditions of `(12.1.1.5)` with `ℱ = 𝒪_X` (so that `f` is flat), one cannot in general assert that the
restriction `Z' → Y'` of `f` is a flat morphism, nor even an open morphism. This is what the example* `(6.5.5,*

<!-- original page 177 -->

*(ii))` *shows, where one takes for `Z'` one of the two irreducible components of `X = Spec(B)`. It is immediate that
this restriction morphism is not open at the points of `Z'` above the "double point" of `Y' = Y`.*

*(ii) In the hypotheses of `(12.1.1.5)`, with `ℱ = 𝒪_X`, one cannot weaken the condition "`f` is flat" to "`f` is
universally open" (cf. `(2.4.6)`), as we shall see later from an example `(14.4.10, (i))`.*

**Corollary (12.1.3).**

<!-- label: IV.12.1.3 -->

*Under the hypotheses of `(12.1.1)`, the function `x ↦ coprof((ℱ_{f(x)})_x)` is upper semi-continuous in `X` and the
function `x ↦ prof_x(ℱ_x)` `(10.8.1)` is lower semi-continuous in `X`.*

The first assertion is none other than an equivalent formulation of `(12.1.1, (v))`. To prove the second, one may
first, taking `(10.8.7)` and `(10.8.8)` into account, reduce as in `(12.1.1)` to the case where `Y` is the spectrum of
a discrete valuation ring `A` with closed point `y` and generic point `y'`, with `X = Spec(B)` affine, `ℱ = M̃`, where
`M` is a `B`-module of finite type. Since `ℱ` is `f`-flat, every irreducible component of `Supp(ℱ)` that contains
`x ∈ X_y` dominates `Y` `(2.3.4)`, in other words its generic point `z'` belongs to `X_{y'}`; the irreducible
components `Z` of `Supp(ℱ)` that contain a generization `x'` of `x` belonging to `X_{y'}` are therefore exactly those
that contain `x`, and moreover, by `(12.1.1.5)`, one has `dim(Z_{y'}) = dim(Z_y)`, whence, if `T = Supp(ℱ)`,
`dim_x(T_y) = dim_{x'}(T_{y'})`. In addition, for a uniformizer `t` of `A`, one saw in `(12.1.1, (v))` that one has
`coprof(M_x) = coprof(M_x/tM_x)`, and since on the other hand `coprof(M_{x'}) ≤ coprof(M_x)` `(6.11.5)`, one sees that
one has `coprof_{x'}(ℱ_{y'}) ≤ coprof_x(ℱ_y)`; the relation `prof_{x'}(ℱ_{y'}) ≥ prof_x(ℱ_y)` then follows from
`(10.8.7)`.

**Remark (12.1.4).**

<!-- label: IV.12.1.4 -->

*One also deduces from `(12.1.1, (i))` that the function `x ↦ dim_x(X_{f(x)})` is upper semi-continuous in `X`, but we
shall see later `(13.1.3)` that this property is true even without supposing `f` flat.*

**Corollary (12.1.5).**

<!-- label: IV.12.1.5 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent `𝒪_X`-Module
that is `f`-flat, `𝒢` a coherent `𝒪_Y`-Module, `x` a point of `X`, `y = f(x)`. Suppose that `𝒢` has property `(S_k)` at
the point `y`, and that `ℱ_y` has property `(S_k)` at the point `x` and is equidimensional at the point `x`. Then:*

*(i) `ℱ ⊗_{𝒪_Y} 𝒢` possesses property `(S_k)` at the point `x`.*

*(ii) If moreover `Y` is locally immersible in a regular scheme, or is an excellent prescheme `(7.8.5)`, there exists a
neighbourhood of `x` in `X` such that `ℱ ⊗_{𝒪_Y} 𝒢` has property `(S_k)` in this neighbourhood.*

Indeed, by `(12.1.1, (iv))`, there exists an open neighbourhood `V` of `x` such that for every `x' ∈ V`, `ℱ_{f(x')}`
satisfies `(S_k)` at the point `x'`. On the other hand, `𝒢` satisfies `(S_k)` at every point of `Y' = Spec(𝒪_y)`
`(5.7.2)`. Replacing `Y` by `Y'` and `X` by `V ×_Y Y'`, one is reduced (taking `(I, 3.6.5)` into account) to the case
where `𝒢` satisfies `(S_k)` in `Y` entirely and where, for every `y ∈ f(X)`, `ℱ_y` possesses property `(S_k)` at every
point of `f⁻¹(y)`; since `ℱ` is `f`-flat, one then knows `(6.4.1)` that `ℱ ⊗_{𝒪_Y} 𝒢` possesses property `(S_k)` in
`X`, which proves (i). To prove (ii), it suffices to observe that, under the hypotheses made, `𝒢` possesses

<!-- original page 178 -->

property `(S_k)` in a neighbourhood `U` of `y` in `Y` (`(6.11.2)` and `(7.8.3, (iv))`); one then concludes in the same
way, replacing this time `Y` by `U` and `X` by `V ×_Y U`.

**Theorem (12.1.6).**

<!-- label: IV.12.1.6 -->

*Let `f : X → Y` be a flat morphism locally of finite presentation, `k` an integer. The following subsets of `X` are
open:*

*(i) The set of points `x ∈ X` such that `X_{f(x)}` satisfies property `(S_k)` at the point `x`.*

*(ii) The set of `x ∈ X` such that `X_{f(x)}` satisfies geometric property `(R_k)` at the point `x`, is equidimensional
at the point `x`, and moreover `x` belongs to no embedded associated prime cycle of `X_{f(x)}`.*

*(iii) The set of `x ∈ X` such that `X_{f(x)}` is geometrically regular (i.e. smooth) at the point `x`.*

*(iv) The set of `x ∈ X` such that `X_{f(x)}` is geometrically normal at the point `x`.*

Steps A) and B) of `(12.0.2)` are carried out here as in `(12.1.1)`; for step A), one uses `(6.7.8)`, as well as
`(4.2.7)` for (ii); for step B), one uses `(9.9.2)` and `(9.9.4)`. It remains to examine step C) in each case.

(i) As in `(12.1.1.2)`, one reduces (using `(6.7.8)`) to the case where `Y` is the spectrum of a discrete valuation
ring `A`, `X = Spec(B)`, where `B` is an `A`-algebra of finite type, `x`, `x'` two points of `X` such that `f(x) = y` is
the closed point and `y' = f(x')` the generic point of `Y`, with `x'` moreover a generization of `x`. Since the task is
to prove that `X` satisfies `(S_k)` at the point `x'`, one may replace `X` by `Spec(𝒪_{X, x'})`, that is, suppose the
ring `B` local, the homomorphism `A → B` local, and `B` essentially of finite type over `A` `(1.3.8)`. Then, by
hypothesis, if `t` is a uniformizer of `A`, `t` is a `B`-regular element by flatness, and `B/tB` satisfies `(S_k)`. But
since `A` is a universally catenary ring `(5.6.4)`, `B` is catenary, hence, by `(5.12.4)`, it follows that `B`
satisfies `(S_k)`, which completes the proof in case (i).

(iii) Here step C) is unnecessary; since `f` is flat, one knows in effect `(6.8.7)` that when `Y` is locally Noetherian
and `f` locally of finite type, the set of `x ∈ X` such that `X_{f(x)}` is geometrically regular at the point `x` is
open in `X`.

(ii) Reasoning as in `(12.1.1.3)`, to prove that the property considered is stable under generization, one may first,
by considering an arbitrary finite extension `K'` of `k(y)`, and taking account of definition `(6.7.6)` of geometric
property `(R_k)`, as well as of the invariance under base-field change of the two other properties figuring in (ii),
replace in (ii) the geometric property `(R_k)` by property `(R_k)`. Proceeding then as in (i), one reduces to the case
where `Y` is the spectrum of a discrete valuation ring `A`, and since `A` is catenary, it suffices to apply `(5.12.5)`
to conclude.

(iv) The set of points `x ∈ X` such that `X_{f(x)}` is geometrically normal at the point `x` is contained in the set of
`x ∈ X` such that `X_{f(x)}` is geometrically pointwise integral and satisfies `(S_2)` at the point `x`, and the latter
is open in `X` by virtue of `(12.1.1, (viii))`. One may therefore already suppose that, for every `x ∈ X`,
`X_{f(x)}` is geometrically pointwise integral and satisfies `(S_2)` at the point `x`, and *a fortiori* it is
equidimensional. On the other hand, by virtue of Serre's criterion `(5.8.6)`, to say that `X_{f(x)}` is geometrically
normal at the point `x` means that `X_{f(x)}` satisfies `(S_2)` and geometric property `(R_1)` at `x`;

<!-- original page 179 -->

but by virtue of (ii) and the preceding remarks, this set is the intersection of two open sets of `X`, hence is open in
`X`. Q.E.D.

**Corollary (12.1.7).**

<!-- label: IV.12.1.7 -->

*Let `f : X → Y` be a morphism locally of finite presentation. Then the set of points `x ∈ X` where `f` possesses one
of the following properties `(6.8.1)`:*

*(i) satisfies property `(S_n)`;*

*(ii) is of codepth `≤ n`;*

*(iii) is Cohen-Macaulay;*

*(iv) is regular (or smooth, which amounts to the same);*

*(v) is normal;*

*(vi) is reduced;*

*is open in `X`.*

Indeed, it follows from `(11.3.1)` that the set of `x ∈ X` where `f` is flat is open. One may therefore confine oneself
to the case where `f` is flat, and then the corollary follows from `(12.1.1, (iv), (vi), and (vii))` and from
`(12.1.6, (i), (ii), and (iv))`.

**Remarks (12.1.8).**

<!-- label: IV.12.1.8 -->

*(i) In `(12.1.6, (ii))`, one cannot suppress the hypothesis that `x` belongs to no embedded associated prime cycle of
`X_{f(x)}`. This is what the example `(5.12.3)` shows, where one takes `X = Spec(A)`, `Y` being the spectrum of the
local ring `A_0` of `k[T]` corresponding to the prime ideal `(T)` and the morphism `X → Y` corresponding to the
injective homomorphism `A_0 → A`, deduced by localization and passage to the quotient from the injection
`k[T] → k[T, U, V]`; this morphism is flat since `A` is a torsion-free `A_0`-module `(0_I, 6.3.4)`. Here the fibre
`X_y` at the closed point `y` of `Y`, equal to `Spec(A/tA)`, is irreducible, of dimension `1`, and satisfies the
geometric condition `(R_0)`, since the local ring at its generic point is a field. By contrast, at the generic point
`y'` of `Y`, the fibre `X_{y'}` has two irreducible components of respective dimensions `0` and `1`, and the one of
dimension `0` is not reduced, so `X_{y'}` does not satisfy condition `(R_0)`.*

*(ii) In `(12.1.6, (ii))`, neither can one suppress the hypothesis that `X_{f(x)}` is equidimensional at the point
`x`. One sees this here on the example `(5.12.6)` with `X = Spec(A)`, `Y = Spec(A_0)`, where `A_0` is defined as in
(i), the morphism `X → Y` coming again from the injection `k[T] → k[T, U, V, W]` by localization and passage to the
quotient, and being flat since `A` is a torsion-free `A_0`-module `(0_I, 6.3.4)`. The fibre `X_y` at the closed point
`y` of `Y` is reduced (hence satisfies `(S_1)`) and satisfies `(R_1)`, but has two irreducible components of
dimensions `2` and `1`, while the fibre `X_{y'}` at the generic point `y'` of `Y` does not satisfy [condition `(R_1)`].*

### 12.2. Local and global properties of the fibres of a proper, flat morphism of finite presentation

**Theorem (12.2.1).**

<!-- label: IV.12.2.1 -->

*Let `f : X → Y` be a proper morphism of finite presentation, `ℱ` an `𝒪_X`-Module that is `f`-flat and of finite
presentation, `Φ` a finite subset of `ℤ ∪ {±∞}`, `k` an integer. The following subsets of `Y` are open:*

*(i) The set of `y ∈ Y` such that the set of dimensions of the associated prime cycles of `ℱ_y` is contained in `Φ`.*

*(ii) The set of `y ∈ Y` such that the set of dimensions of the irreducible components of `Supp(ℱ_y)` contains `Φ`.*

*(iii) The set of `y ∈ Y` such that all the associated prime cycles of `ℱ_y` have the same dimension equal to `k`.*

*(iv) The set of `y ∈ Y` such that `ℱ_y` has no embedded associated prime cycle and that the set of dimensions of the
irreducible components of `Supp(ℱ_y)` is equal to `Φ`.*

<!-- original page 180 -->

*(v) The set of `y ∈ Y` such that `ℱ_y` has property `(S_k)` and is equidimensional at every point of `X_y`.*

*(vi) The set of `y ∈ Y` such that `coprof(ℱ_y) ≤ k`.*

*(vii) The set of `y ∈ Y` such that `ℱ_y` is a Cohen-Macaulay `𝒪_X`-Module.*

*(viii) The set of `y ∈ Y` such that `ℱ_y` is geometrically reduced.*

*(ix) The set of `y ∈ Y` such that `ℱ_y` is geometrically pointwise integral at each point of `X_y`.*

*(x) The set of `y ∈ Y` such that `ℱ_y` is geometrically integral.*

*(xi) The set of `y ∈ Y` such that `ℱ_y` has no embedded associated prime cycle and that the sum `l(y)` of the total
multiplicities `(4.7.12)` of `ℱ_y` at the maximal points of `Supp(ℱ_y)` is `≤ k`.*

With the exception of (ii), (iii), (iv), (x), and (xi), the properties `P(y)` considered are of the following form:
"for every `x ∈ X_y`, `ℱ_y` has property `Q(x)`", where `Q(x)` is one of properties (i) to (viii) of `(12.1.1)`. It
follows from `(12.1.1)` that the set `U` of `x ∈ X` such that `Q(x)` is true is open, and the set `V` of `y ∈ Y` such
that `P(y)` is true is none other than the set `Y − f(X − U)`; in all these cases, the theorem is therefore already
true on the sole hypothesis that the morphism `f` is closed. For (iii), one applies (i) with `Φ` reduced to a single
element. There remain cases (ii), (iv), and (xi) to examine separately ((x) deducing at once from (xi) and `(4.7.14)`),
always applying the method described in `(12.0.2)`.

**(12.2.1.1)**

<!-- label: IV.12.2.1.1 -->

*Case (ii):* Steps A) and B) of the proof proceed as in the beginning of `(12.1.1)`; for step A), one uses `(8.9.1)`,
`(11.2.6)`, and `(4.2.7)`; for step B), one uses `(9.5.5)` applied to `Supp(ℱ)`. It remains to show that if (supposing
`Y` Noetherian) the set of dimensions of the irreducible components of `Supp(ℱ_y)` contains `Φ`, then the same is true
of the set of dimensions of the irreducible components of `Supp(ℱ_{y'})`, for every generization `y'` of `y` in `Y`.
Let `Y_1` be a spectrum of a discrete valuation ring such that, if `y_1` and `y'_1` are the closed point and the
generic point of `Y_1`, there is a morphism `h : Y_1 → Y` with `h(y_1) = y`, `h(y'_1) = y'` `(II, 7.1.7)`. Applying
`(4.2.7)`, one sees that one may replace `Y` by `Y_1` and `X` by `X_1 = X ×_Y Y_1`, in other words confine oneself to
the case where `Y` is the spectrum of a discrete valuation ring, `y` its closed point and `y'` its generic point.

Using `(Err_III, 30)`, one may confine oneself to the case where `Supp(ℱ) = X`, so that `f` is quasi-flat `(2.3.3)`;
the irreducible components `Z_i` of `X` then dominate `Y` `(2.3.4)`, in other words their generic points belong to
`X_{y'}` and the `Z_i ∩ X_{y'}` are the irreducible components of `X_{y'}`. But every irreducible component of `X_y`
is contained in one of the `Z_i`, hence is an irreducible component of `(Z_i)_y`; now one knows `(7.1.13)` that the
dimensions of all the irreducible components of `(Z_i)_y` are equal to `dim((Z_i)_{y'})`, which completes the proof of
(ii).

**(12.2.1.2)**

<!-- label: IV.12.2.1.2 -->

*Case (iv):* The same reasoning as at the beginning shows, using `(12.1.1, (iii))`, that one may already suppose
(replacing `Y` by an open set of `Y`) that for every `y ∈ Y`, `ℱ_y` has no embedded associated prime cycle. The
assertion of case (iv) is then an immediate consequence of the assertions of cases (i) and (ii).

<!-- original page 181 -->

**(12.2.1.3)**

<!-- label: IV.12.2.1.3 -->

*Case (xi):* For step A) of the reasoning, one uses `(8.9.1)`, `(11.2.6)`, `(8.10.5, (xii))` (to preserve the
hypothesis that `f` is proper), as well as `(4.2.7)`, `(4.5.6)`, and `(4.7.9)`. For step B), one sees, as in case (iv),
that one may suppose that for every `y ∈ Y`, `ℱ_y` has no embedded associated prime cycle, and one applies `(9.8.8)`,
which proves that the function `z ↦ l(z)` is constructible. It therefore remains to see (supposing `Y` Noetherian and
`f` proper) that for every generization `y'` of a point `y ∈ Y`, one has `l(y') ≤ l(y)`. Reasoning as in `(12.1.1.3)`,
one sees (using `(4.7.8)` and `(4.5.11)`) that one may suppose that the irreducible components of `Supp(ℱ_{y'})` are
geometrically irreducible and that `l(y')` is the sum of the lengths of `(ℱ_{y'})_{z'_j}` at the maximal points `z'_j`
of `Supp(ℱ_{y'})`. Applying `(4.2.7)`, `(4.5.6)`, and `(4.7.9)` again, one reduces, as in `(12.2.1.1)`, to the case
where `Y` is the spectrum of a discrete valuation ring, `y` its closed point and `y'` its generic point. The fact that
`l(y') ≤ l(y)` will then be a consequence of:

**Lemma (12.2.1.4).**

<!-- label: IV.12.2.1.4 -->

*Let `Y` be the spectrum of a discrete valuation ring, `y` its closed point, `y'` its generic point, `f : X → Y` a
proper morphism, `ℱ` a coherent `𝒪_X`-Module that is `f`-flat, `z_i` (resp. `z'_j`) the maximal points of `Supp(ℱ_y)`
(resp. `Supp(ℱ_{y'})`). Suppose that `ℱ_y` has no embedded associated prime cycle. Then one has*

```text
  (12.2.1.4.1)         ∑_j long((ℱ_{y'})_{z'_j}) ≤ ∑_i long((ℱ_y)_{z_i}).
```

One has `Y = Spec(A)`, where `A` is a discrete valuation ring, of which we denote by `t` a uniformizer, so that
`ℱ_y = ℱ/tℱ`. Since `ℱ` is `f`-flat, the `z'_j` are also the maximal points of `Supp(ℱ)` `(2.3.4)`; for every `z_i`,
let us denote by `z'_{ij}` those of the `z'_j` that are generizations of `z_i`; it follows from `(3.4.1.1)` that one
has

```text
  long((ℱ_y)_{z_i}) ≥ ∑_j long((ℱ_{y'})_{z'_{ij}}),
```

whence on summing

```text
  ∑_i long((ℱ_y)_{z_i}) ≥ ∑_{i, j} long((ℱ_{y'})_{z'_{ij}}).
```

The lemma will therefore be proved if we establish that for every `z'_j` there is at least one index `i` such that
`z'_j` is one of the `z'_{ij}`. Now, since `f` is proper (hence closed) and `f(z'_j) = y'`, there exists `x ∈ X` which
is a specialization of `z'_j` and is such that `f(x) = y`, in other words `‾{z'_j} ∩ X_y` is non-empty. Since `t` is
`ℱ`-regular by flatness, one deduces from `(3.4.3)` that there is at least one point of `Ass(ℱ_y)` of which `z'_j` is a
generization; but since the points of `Ass(ℱ_y)` are by hypothesis the `z_i`, this completes the proof.

**Corollary (12.2.2).**

<!-- label: IV.12.2.2 -->

*Under the hypotheses of `(12.2.1)`:*

*(i) The function `y ↦ dim(Supp(ℱ_y))` is continuous (hence locally constant) in `Y`.*

*(ii) The function `y ↦ coprof(ℱ_y)` `(5.7.1)` is upper semi-continuous in `Y`.*

*(iii) The function `y ↦ l(y)` `(12.2.1, (xi))` is upper semi-continuous in `Y` when the `ℱ_y` have no embedded
associated prime cycle.*

*(iv) The function `y ↦ prof_*(ℱ_y)` `(10.8.1)` is lower semi-continuous in `Y`.*

<!-- original page 182 -->

(i) It follows from `(12.2.1, (i))` applied to `Φ` equal to the smallest interval of `ℕ` containing the dimensions of
the associated prime cycles of `ℱ_y`, that `z ↦ dim(Supp(ℱ_z))` is upper semi-continuous at the point `y`; it follows
on the other hand from `(12.2.1, (ii))` applied to `Φ` equal to the set of dimensions of the irreducible components of
`Supp(ℱ_y)`, that this same function is lower semi-continuous at the point `y`, whence the conclusion. Assertions (ii)
and (iii) are nothing but other formulations of `(12.2.1, (vi) and (xi))`. Finally, by `(12.1.3)`, the set of `x ∈ X`
such that `prof_x(ℱ_x) ≥ k` is open, and the conclusion of (iv) follows by the same reasoning as at the beginning of
`(12.2.1)`.

**Remarks (12.2.3).**

<!-- label: IV.12.2.3 -->

*(i) One will observe that for `(12.2.1, (ii))`, one may dispense with the hypothesis that `f` is proper.*

*(ii) In `(12.2.1, (ii))`, one cannot replace the condition that the set `E(y)` of dimensions of the irreducible
components of `Supp(ℱ_y)` contain `Φ`, by the condition that `E(y)` be equal to `Φ`. Indeed, let `k` be a field, and
consider the projective space of dimension `3`, `P = P^3_k = Proj(C)`, where `C = k[t_0, t_1, t_2, t_3]` (with `t_i`
indeterminates); in `P`, let `X_0` be the closed sub-scheme "union of the line `X_1` defined by `t_1 = t_2 = 0` and of
the plane `X_2` defined by `t_2 − t_3 = 0`", which describes in geometric terms the fact that `X_0` is equal to
`Proj(C/𝔞)`, where the graded ideal `𝔞` is equal to `𝔟𝔠`, with `𝔟 = Ct_1 + Ct_2`, `𝔠 = C(t_2 − t_3)`; consider the
morphism `f_0 : X_0 → X_1` which, in geometric terms, is the "projection of `X_0` onto `X_1` from the line at infinity
`D` defined by `t_0 − t_2 = 0`"; in algebraic form, `f_0` corresponds to the homomorphism of graded algebras
`k[t_0, t_1] → k[t_0, t_1, t_2, t_3]/𝔞` obtained by passage to the quotient from the canonical injection
`k[t_0, t_1] → k[t_0, t_1, t_2, t_3]`. It is clear that `f_0` is a projective morphism, hence proper; so is its
restriction `f : X → Y`, where `Y = D_+(t_0)` and `X = f_0⁻¹(Y)`; to see that `f` is flat, it suffices to remark that
`k[t_1]` is a principal ring and the ring `C' = k[t_1, t_2, t_3]/(t_2 − t_3)(t_1) + (t_2)` a torsion-free
`k[t_1]`-module `(0_I, 6.3.4)`. For every `y ∈ Y` distinct from the point `y_0` defined by `t_2 = 0`, `f⁻¹(y)` then has
two irreducible components, of dimensions `0` and `1`, while `f⁻¹(y_0)` has only one irreducible component of dimension
`1`.*

*(iii) In `(12.2.1, (i))`, one cannot either replace the condition that the set `E'(y) ⊃ E(y)` of dimensions of the
associated prime cycles of `ℱ_y` be contained in `Φ` by the condition that it be equal to `Φ`. Indeed, let `k` be a
field, `A` the polynomial ring `k[t]`, `B` the sub-ring `k[t^4, t^3 u, tu^3, u^4]` of the polynomial ring `k[t, u]`
(with `t`, `u` indeterminates); `B` is not integrally closed, the element `t^2 u^2` belonging to its integral closure
but not being in `B`; if `𝔪` is the maximal ideal of `B`, generated by `t^4`, `t^3 u`, `tu^3`, and `u^4`, `𝔪` is an
embedded associated prime ideal of `A/tA`. Set `Y = Spec(A)`, `X = Spec(B)`, and let `f : X → Y` be the morphism
corresponding to the homomorphism `A → B` which transforms `t` into `t^4`. Since this homomorphism makes `B` a
torsion-free `A`-module, `f` is flat `(0_I, 6.3.4)`. If `y` is the point of `Y` corresponding to the maximal ideal
`tA`, the prescheme `f⁻¹(y)` is irreducible and of dimension `1`, but admits an embedded associated prime cycle of
dimension `0`; on the contrary, if `y'` is the generic point of `Y`, `f⁻¹(y')` has no embedded associated prime cycle,
being the spectrum of an integral `k(y')`-algebra of dimension `1`. In this example, `f` is an affine morphism that is
not proper; one can immediately deduce from it an analogous example where `f` is proper and flat by considering `X` as
a dense open set of a projective scheme over `Y` (`(II, 5.3.4 and 5.3.2)`), or by proceeding directly as in Remark
(ii).*

*Remarks (ii) and (iii) show the necessity of including in `(12.2.1, (iv))` the condition that `ℱ_y` have no embedded
associated prime cycle.*

*(iv) In `(12.2.1, (xi))`, one cannot suppress the hypothesis that `f` is proper. Indeed, let `k` be a field, `Y` the
"affine line", spectrum of the polynomial ring `k[t]` (`t` indeterminate), `X` the sum prescheme of `Y` and of the
complementary open set of the closed point `y` of `Y` defined by `t = 0`. It is clear that the morphism `f : X → Y`
which is equal to the canonical injections on each of the components of `X` is flat and that if one takes `ℱ = 𝒪_X`,
`ℱ_z` has no embedded associated prime cycle for any `z ∈ Y`. However, one sees at once that one has `l(y) = 1` and
`l(z) = 2` for every `z ≠ y`.*

*(v) In `(12.2.1, (xi))`, neither can one suppress the hypothesis that `ℱ_y` is without embedded associated prime
cycle. This is what the example of Remark (ii) shows: one sees at once in effect that one has, with `ℱ = 𝒪_X`,
`l(y_0) = 1` and `l(y) = 2` for `y ≠ y_0` in `Y`.*

*(vi) We do not know whether in `(12.2.1, (xi))` one may replace the hypothesis that `ℱ` is `f`-flat by the hypothesis
that `Supp(ℱ) = X` and that `f` is universally open. Taking up the proof of `(12.2.1.4)` again, one sees (also using
`(14.3.6)`) that one would have to resolve the following question: let `A` be a Noetherian local ring, `M` an
`A`-module*

<!-- original page 183 -->

*of finite type, `t` an element of the maximal ideal `𝔪` of `A` that is contained in no minimal prime ideal of `A`; if
there exists one of these minimal prime ideals `𝔭` such that `dim(A/𝔭) = 1`, is it true that `𝔪` is an associated prime
ideal of `M/tM` (`t` not being supposed `M`-regular)?*

*One will note however that one cannot, in `(12.2.1, (xi))`, suppress purely and simply the hypothesis that `ℱ` is
`f`-flat. One will take here `P` as in Remark (ii), then in `P` the closed sub-scheme `X_0` union of the three lines
`X_1`, `X_2`, `X_3` defined respectively by `t_1 = t_3 = 0`, `t_1 − t_0 = t_3 = 0`, `t_2 = t_3 = 0`; one defines the
projection `f_0` of `X_0` onto `X_1` as before, and its restriction `f : X → Y`, where `Y = D_+(t_0)` is the affine
line and `X = f_0⁻¹(Y)`; `f` is proper but not flat, and if one takes `ℱ = 𝒪_X`, `ℱ_y` has no embedded associated
prime cycles for any `y ∈ Y`. But one has `l(y_0) = 1` and `l(y) = 2` for `y ≠ y_0` in `Y`.*

**Theorem (12.2.4).**

<!-- label: IV.12.2.4 -->

*Let `f : X → Y` be a proper, flat morphism of finite presentation, `k` an integer `≥ 1`. The following subsets of `Y`
are open:*

*(i) The set of `y ∈ Y` such that `X_y` possesses property `(S_k)`.*

*(ii) The set of `y ∈ Y` such that `X_y` satisfies geometric property `(R_k)`, is equidimensional at every point, and
has no embedded associated prime cycle.*

*(iii) The set of `y ∈ Y` such that `X_y` is geometrically regular (i.e. smooth over `k(y)`).*

*(iv) The set of `y ∈ Y` such that `X_y` is geometrically normal.*

*(v) The set of `y ∈ Y` such that `X_y` is geometrically reduced.*

*(vi) The set of `y ∈ Y` such that `X_y` is geometrically reduced and that the geometric number of connected components
of `X_y` is equal to `k`.*

*(vii) The set of `y ∈ Y` such that `X_y` is geometrically pointwise integral `(4.6.9)`.*

*(viii) The set of `y ∈ Y` such that `X_y` is geometrically integral.*

*(ix) The set of `y ∈ Y` such that `X_y` has no embedded associated prime cycle and that the total multiplicity
`(4.7.4)` of `X_y` over `k(y)` is `≤ k`.*

Except for (vi), these assertions are special cases of assertions of `(12.2.1)`, or are deduced from assertions of
`(12.1.6)` as at the beginning of the proof of `(12.2.1)`. For (vi), one reduces as always (taking into account the
invariance under base change of the geometric number of connected components `(4.5.6)`) to the case where `Y` is
Noetherian. The set `U` of `y ∈ Y` such that `X_y` is geometrically reduced is open in `Y` by virtue of (v); it then
follows from `(III, 7.8.7 and 7.8.6)` that for every `y ∈ U`, there is a neighbourhood `V ⊂ U` of `y` and an integer
`m` such that, for every `z ∈ V`, `Γ(X_z, 𝒪_{X_z})` is isomorphic to `(k(z))^m`; but by virtue of `(III, 4.3.4)`, `m`
is then the geometric number of connected components of `X_z`, whence the conclusion. One will give another proof of
(vi) in `(15.5.9)`.

### 12.3. Local cohomological properties of the fibres of a flat morphism locally of finite presentation

**Lemma (12.3.1).**

<!-- label: IV.12.3.1 -->

*Let `A` be a ring, `B` an `A`-algebra of finite presentation that is a flat `A`-module, `M` a `B`-module of finite
presentation that is a flat `A`-module. Then the following conditions are equivalent:*

*a) `M` is a projective `B`-module.*

*b) `M` is a flat `B`-module.*

*c) For every `y ∈ Spec(A)`, `M ⊗_A k(y)` is a projective `(B ⊗_A k(y))`-module.*

<!-- original page 184 -->

The equivalence of a) and b) follows from Bourbaki, *Alg. comm.*, chap. II, §5, n° 2, cor. 2 of th. 1. Since a) implies
c) trivially, it remains to prove that c) implies b), which follows from the fibrewise flatness criterion `(11.3.10)`,
applied with `g = h`, `f = 1_X`.

**Proposition (12.3.2).**

<!-- label: IV.12.3.2 -->

*Let `A` be a ring, `B` an `A`-algebra of finite presentation that is a flat `A`-module, `M` a `B`-module of finite
presentation that is a flat `A`-module. Then:*

*(i) There exists a left resolution of `M` by free `B`-modules of finite type.*

*(ii) One has*

```text
  (12.3.2.1)    dim. proj_B(M) = sup_{y ∈ Spec(A)} dim. proj_{B ⊗_A k(y)}(M ⊗_A k(y)) = Tor.dim_B(M)
```

*where `Tor.dim_B(M)` is the smallest integer `i` such that `Tor_j^B(M, N) = 0` for every `j > i` and every `B`-module
`N` (and `+∞` if no such integer `i` exists).*

(i) By virtue of `(8.9.1)`, there exists a Noetherian sub-ring `A_0` of `A`, an `A_0`-algebra of finite type `B_0` and
a `B_0`-module of finite type `M_0` such that `B` is isomorphic to `B_0 ⊗_{A_0} A` and `M` to `M_0 ⊗_{A_0} A`.
Moreover `(11.2.7)`, one may suppose that `B_0` and `M_0` are flat `A_0`-modules. There then exists a left resolution
`(L_0)_•` of `M_0` formed of free `B_0`-modules of finite type, and since `M_0` and the `L_{0, i}` are flat
`A_0`-modules, `(L_0)_• ⊗_{A_0} A` is a left resolution of `M` formed of free `B`-modules of finite type `(2.1.10)`.

(ii) By virtue of `(0, 17.2.2, (ii))`, one has `Tor.dim_B(M) ≤ dim. proj_B(M)`, and the definition of the projective
dimension immediately shows that, for every `y ∈ Spec(A)`, one has
`dim. proj_{B ⊗_A k(y)}(M ⊗_A k(y)) ≤ dim. proj_B(M)`. To prove the reverse inequalities, consider a left resolution
`(L_i)` of `M` by free `B`-modules of finite type, and suppose that `Tor.dim_B(M) = n` (resp.
`dim. proj_{B ⊗_A k(y)}(M ⊗_A k(y)) ≤ n` for every `y ∈ Spec(A)`). Then `R = Im(L_n → L_{n−1}) = Ker(L_{n−1} → L_{n−2})`
is a `B`-module of finite type that is also a flat `A`-module, by virtue of the hypothesis on `M` and `B` and of
`(2.1.10)`. In addition, one has `Tor_{j+1}^B(M, N) = Tor_j^B(R, N)` for every `B`-module `N` `(M, V, 7)`. The
hypothesis `Tor.dim_B(M) = n` therefore entails `Tor_1^B(R, N) = 0` for every `B`-module `N`, that is to say that `R`
is a flat `B`-module, hence projective by virtue of `(12.3.1)`; this establishes that `dim. proj_B(M) ≤ n`. The
hypothesis `dim. proj_{B ⊗_A k(y)}(M ⊗_A k(y)) ≤ n` for every `y ∈ Spec(A)` entails on the other hand, by
tensorization with `k(y)`, that in each of the sequences (exact by virtue of the flatness over `A` of `M`, of the
`L_i`, and of `R` `(2.1.10)`)

```text
  0 → R ⊗_A k(y) → L_{n−1} ⊗_A k(y) → ⋯ → L_0 ⊗_A k(y) → M ⊗_A k(y) → 0,
```

`R ⊗_A k(y)` is a projective `(B ⊗_A k(y))`-module (for `y ∈ Spec(A)`). One concludes once again from `(12.3.1)` that
`R` is a projective `B`-module, hence `dim. proj_B(M) ≤ n`.

**Proposition (12.3.3).**

<!-- label: IV.12.3.3 -->

*Let `f : X → S` be a morphism locally of finite presentation, `ℒ_•` a complex formed of quasi-coherent `𝒪_X`-Modules
of finite presentation; for every `s ∈ S`, let `(ℒ_•)_s` be the complex `ℒ_• ⊗_{𝒪_S} k(s)` of `𝒪_{X_s}`-Modules of
finite type. Suppose that `ℒ_{n−1}` is `f`-flat. Then the set `U` of `x ∈ X` such that `(ℋ_n((ℒ_•)_{f(x)}))_x = 0` is
open in `X`. If moreover `ℒ_n` is `f`-flat, then one has `ℋ_n(ℒ_•) | U = 0`.*

One may evidently confine oneself to the case where `n = 1` and where the complex `ℒ_•` reduces to
`0 → ℒ_2 → ℒ_1 → ℒ_0 → 0`. One may first reduce to the case where `S = Spec(A)` and `X`

<!-- original page 185 -->

are affine, then to the case where `S` is Noetherian; indeed, by `(8.9.1)` and `(8.5.2)`, one knows that there exist a
Noetherian prescheme `S' = Spec(A')`, where `A'` is a sub-ring of `A`, a morphism of finite type `f' : X' → S'`, and
three coherent `𝒪_{X'}`-Modules `ℒ'_i` (`0 ≤ i ≤ 2`) such that `X = X' ×_{S'} S`, `f = f'_{(S)}`,
`ℒ_i = ℒ'_i ⊗_{S'} S`, as well as two homomorphisms `u'`, `v'` such that `u = u' ⊗ 1`, `v = v' ⊗ 1`, and
`v' ∘ u' = 0`. One may moreover suppose that `ℒ'_0` is `f'`-flat `(11.2.7)`, and that `ℒ'_1` is `f'`-flat when `ℒ_1`
is supposed `f`-flat. By faithful flatness, the hypothesis `(ℋ_1((ℒ_•)_{f(x)}))_x = 0` is equivalent to
`(ℋ_1((ℒ'_•)_{f'(x')}))_{x'} = 0`, where `x'` is the projection of `x` in `X'`; if `U'` is the set of `x' ∈ X'` such
that `(ℋ_1((ℒ'_•)_{f'(x')}))_{x'} = 0`, then `U` is the inverse image of `U'` by the projection `X → X'`, which
reduces, for the first assertion, to the case where `S` is Noetherian. For the second assertion, one further remarks
that `A` is an inductive limit of its sub-rings `A_λ` that are `A'`-algebras of finite type; set
`X_λ = X' ×_{S'} S_λ`, where `S_λ = Spec(A_λ)`, `ℒ_•^{(λ)} = ℒ'_• ⊗_{S'} S_λ`, and let
`u_λ = u' ⊗ 1 : ℒ_2^{(λ)} → ℒ_1^{(λ)}`, `v_λ = v' ⊗ 1 : ℒ_1^{(λ)} → ℒ_0^{(λ)}`, so that one has
`ℋ_1(ℒ_•^{(λ)}) = Ker(v_λ)/Im(u_λ)`. Now, since the functor `lim` is exact in the category of commutative groups, one
has `Ker(v) = lim Ker(v_λ)`, `Im(u) = lim Im(u_λ)`, and `ℋ_1(ℒ_•) = lim ℋ_1(ℒ_•^{(λ)})`. If one has supposed that
`ℒ_1` is `f`-flat and (by reducing to the case where `X = U`) that one has proved `ℋ_1(ℒ_•^{(λ)}) = 0` for every `λ`,
one will indeed deduce the assertion.

I) Suppose henceforth `S` Noetherian. One knows (without flatness hypothesis on `ℒ_0`) that the set `U` is
constructible in `X` `(9.9.6)`. Using now `(0_III, 9.2.5)`, it remains to show that for every generization `x'` of
`x ∈ U` in `X`, one has also `x' ∈ U`. The method exposed in `(12.0.2)` applies without change (taking into account
the fact that for a prescheme `Z` over a field `k` and an extension `k'` of `k`, the projection `Z ⊗_k k' → Z` is
faithfully flat). One may therefore suppose that `S` is the spectrum of a discrete valuation ring `A`, of which one
denotes by `t` a uniformizer, with `x` above the closed point of `S` and `x'` above the generic point of `S`. The
hypothesis that `ℒ_0` is `f`-flat entails that `t` is `ℒ_0`-regular `(0_I, 6.3.4)`. One is then reduced to proving the
following lemma (where `B`, `M`, `N`, `P` will be replaced by `𝒪_x`, `(ℒ_2)_x`, `(ℒ_1)_x`, and `(ℒ_0)_x` respectively):

**Lemma (12.3.3.1).**

<!-- label: IV.12.3.3.1 -->

*Let `B` be a Noetherian local ring, `M`, `N`, `P` three `B`-modules, with `N` of finite type, `M ─u→ N ─v→ P` two
homomorphisms such that `v ∘ u = 0`. Let `t` be an element of the maximal ideal of `B` such that `t` is `P`-regular and
such that the sequence*

```text
  (12.3.3.2)        M/tM ─u⊗1→ N/tN ─v⊗1→ P/tP
```

*is exact. Then the sequence `M → N → P` is exact.*

Let us first note that if one replaces `M` by its image `Q` in `N` and `u` by the injection `j : Q ↪ N`, the image of
`j ⊗ 1` is the same as that of `u ⊗ 1`, hence one may, without changing the hypothesis nor the conclusion, suppose `u`
injective. On the other hand, if `R` is the image of `v` and `p : N → R` the canonical surjection, `t` is evidently
`R`-regular, one has `p ∘ u = 0`, and the kernel of `p ⊗ 1` is contained in that of `v ⊗ 1`; it is consequently equal
to it if the sequence `(12.3.3.2)` is exact; since on the other hand one has evidently `Ker(p) = Ker(v)`,

<!-- original page 186 -->

one sees that one may, to prove the lemma, suppose moreover `v` surjective. The lemma will then be a consequence of:

**Lemma (12.3.3.3).**

<!-- label: IV.12.3.3.3 -->

*Let `B` be a ring, `M`, `N`, `P` three `B`-modules, `u : M → N`, `v : N → P` two homomorphisms such that `u` is
injective, `v` surjective, and `v ∘ u = 0`. Let `t` be an element of `B` such that `t` is `P`-regular. Then one has*

```text
  (12.3.3.4)        Ker(v ⊗ 1)/Im(u ⊗ 1) = (Ker(v)/Im(u)) ⊗_B (B/tB)
```

*up to a canonical isomorphism.*

Indeed, the hypothesis that the sequence `(12.3.3.2)` is exact will then entail `(Ker(v)/Im(u)) ⊗_B (B/tB) = 0`, and
since `t` belongs to the maximal ideal of `B` and `Ker(v)` is a `B`-module of finite type (since `B` is supposed
Noetherian in `(12.3.3.1)`), Nakayama's lemma will prove that `Ker(v) = Im(u)`.

It therefore remains to prove `(12.3.3.3)`. Set `u' = u ⊗ 1`, `v' = v ⊗ 1`, `Z = Ker(v)`, `H = Z/Im(u)`, so that one
has the exact sequences

```text
  0 → M → Z → H → 0
  0 → Z → N ─v→ P → 0
```

whence, by tensorizing with `B/tB` and using lemma `(3.4.1.4)` and the fact that `t` is `P`-regular, the exact
sequences

```text
  M/tM ─w'→ Z/tZ → H/tH → 0
  0 → Z/tZ → N/tN ─v'→ P/tP → 0
```

whence `Ker(v') = Z/tZ`, and since `Im(w') = Im(u')`, one obtains `(12.3.3.4)`.

II) Suppose now in addition that `ℒ_1` is `f`-flat; replacing furthermore possibly `X` by `U`, one may suppose that
`X = U`. The task is to see that for every `x ∈ X`, one has `(ℋ_1(ℒ_•))_x = 0`. Let `s = f(x)`, and let `𝔫` be the
ideal `𝔪_s 𝒪_{X, x}`, which is contained in the maximal ideal of `𝒪_{X, x}`; since `(ℋ_1(ℒ_•))_x` is an
`𝒪_{X, x}`-module of finite type (`X` being locally Noetherian), it is separated for the `𝔫`-adic topology
`(0_I, 7.3.5)`, hence it suffices to show that its separated completion for this topology is `0`. Now, by virtue of
`(III, 7.4.7.2)`, this separated completion is equal to `lim_k ℋ_1(ℒ_• ⊗_{𝒪_S} (𝒪_{S, s}/𝔪_s^{k+1}))`, and it will
therefore suffice to prove that each of the terms of this projective system is null. But this is true by hypothesis
for `k = 0`; let us therefore reason by induction on `k`. The conclusion will follow from the more general lemma
below (which one will apply for `A = 𝒪_{S, s}/𝔪_s^{k+1}` and `𝔍` equal to the maximal ideal `𝔪_s/𝔪_s^{k+1}` of `A`):

**Lemma (12.3.3.5).**

<!-- label: IV.12.3.3.5 -->

*Let `A` be a ring, `𝔍` a nilpotent ideal of `A`, `L_• : P ─u→ Q ─v→ R` a complex of `A`-modules. Set `A_0 = A/𝔍`,
`L_•^{(0)} = L_• ⊗_A A_0 : P_0 ─u_0→ Q_0 ─v_0→ R_0`, and suppose that `gr_𝔍^•(A)` is a flat `A_0`-module, and that `Q`
and `R` are flat `A`-modules. Then the relation `H_1(L_•^{(0)}) = 0` entails `H_1(L_•) = 0`.*

Set `L_•^{(k)} = L_• ⊗_A (A/𝔍^{k+1}) : P_k ─u_k→ Q_k ─v_k→ R_k`; since there exists an integer `k ≥ 1` such that
`L_•^{(k)} = L_•`, it will suffice to prove, by induction on `k`, that the sequence `P_k ─u_k→ Q_k ─v_k→ R_k` is

<!-- original page 187 -->

exact (this assertion following from the hypothesis for `k = 0`). Let then `x ∈ Q_k` be an element such that
`v_k(x) = 0`. Since by the inductive hypothesis the sequence `P_{k−1} ─u_{k−1}→ Q_{k−1} ─v_{k−1}→ R_{k−1}` is exact,
the canonical image of `x` in `Q_{k−1} = Q_k/(𝔍^k Q_k/𝔍^{k+1} Q_k)` belongs to `Im(u_{k−1})`, hence there exists
`z ∈ P_k` such that `x = u_k(z) + x'` with `x' ∈ 𝔍^k Q_k/𝔍^{k+1} Q_k`. Since one has `v_k ∘ u_k = 0`, the relation
`v_k(x) = 0` entails `v_k(x') = 0`, and on the other hand one evidently has `v_k(x') ∈ 𝔍^k R_k/𝔍^{k+1} R_k`;
everything therefore comes down to proving that the sequence

```text
  𝔍^k P/𝔍^{k+1} P ─u''→ 𝔍^k Q/𝔍^{k+1} Q ─v''→ 𝔍^k R/𝔍^{k+1} R
```

(where `u''` and `v''` come from `u` and `v` by restriction and passage to the quotients) is exact. Now, by
hypothesis, `𝔍^k/𝔍^{k+1}` is a flat `(A/𝔍)`-module, hence the sequence

```text
  (P/𝔍P) ⊗_{A/𝔍} (𝔍^k/𝔍^{k+1}) ─u''→ (Q/𝔍Q) ⊗_{A/𝔍} (𝔍^k/𝔍^{k+1}) ─v''→ (R/𝔍R) ⊗_{A/𝔍} (𝔍^k/𝔍^{k+1})
```

is exact. But `(Q/𝔍Q) ⊗_{A/𝔍} (𝔍^k/𝔍^{k+1}) = Q ⊗_A (𝔍^k/𝔍^{k+1})` identifies with `𝔍^k Q/𝔍^{k+1} Q`, by virtue of
the flatness of `Q` over `A`, and likewise `(R/𝔍R) ⊗_{A/𝔍} (𝔍^k/𝔍^{k+1})` identifies with `𝔍^k R/𝔍^{k+1} R`. Finally,
the image of `u'` identifies with that of `u''`, and this completes the proof.

**Corollary (12.3.4).**

<!-- label: IV.12.3.4 -->

*Let `f : X → S` be a flat morphism locally of finite presentation, `ℱ`, `𝒢` two `𝒪_X`-Modules of finite presentation
and `f`-flat. Let `n` be an integer `≥ 0`, `U` the set of `x ∈ X` such that
`(ℰxt^n_{𝒪_{X_{f(x)}}}(ℱ_{f(x)}, 𝒢_{f(x)}))_x = 0` (resp. `(𝒯or_n^{𝒪_{X_{f(x)}}}(ℱ_{f(x)}, 𝒢_{f(x)}))_x = 0`). Then
`U` is open, and one has `ℰxt^n_{𝒪_X}(ℱ, 𝒢) | U = 0` (resp. `𝒯or_n^{𝒪_X}(ℱ, 𝒢) | U = 0`).*

One may evidently confine oneself to the case where `S` and `X` are affine. Then `(12.3.2)`, there exists a left
resolution `ℒ_• = (ℒ_i)` of `ℱ` formed of free `𝒪_X`-Modules of finite type. If one sets `ℳ^• = ℋom(ℒ_•, 𝒢)` (resp.
`𝒩_• = ℒ_• ⊗_{𝒪_X} 𝒢`), one deduces that each of the `ℳ^i` (resp. `𝒩_i`) is isomorphic to an `𝒪_X`-Module of the form
`𝒢^m`, hence the `ℳ^i` and `𝒩_i` are `𝒪_X`-Modules of finite presentation and `f`-flat. In addition, for every base
change `S' → S`, if one sets `X' = X ×_S S'`, `ℱ' = ℱ ⊗_S S'`, `𝒢' = 𝒢 ⊗_S S'`, then `ℒ'_• = ℒ_• ⊗_S S'` is still a
left resolution of `ℱ'` by free `𝒪_{X'}`-Modules of finite type `(2.1.10)`, and `ℳ'^• = ℳ^• ⊗_S S'` is equal to
`ℋom(ℒ'_•, 𝒢')` (resp. `𝒩'_• = 𝒩_• ⊗_S S'` is equal to `ℒ'_• ⊗_{𝒪_{X'}} 𝒢'`) according to what precedes. In
particular, one has, for every `s ∈ S`, `ℰxt^n_{𝒪_{X_s}}(ℱ_s, 𝒢_s) = ℋ^n((ℳ^•)_s)` (resp.
`𝒯or_n^{𝒪_{X_s}}(ℱ_s, 𝒢_s) = ℋ_n((𝒩_•)_s)`). Applying `(12.3.3)` to the complexes of `f`-flat Modules `ℳ^•` and
`𝒩_•`, one deduces the corollary at once.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/24-c4-s12-etude-fibres-morphismes-plats.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-3.pdf -->

<!-- original page 199 -->

## §14. Universally open morphisms

§§14 and 15 are devoted to the study of the notion of *universally open morphism* `(2.4.2)`. One has already seen
`(2.4.6)` that a flat morphism locally of finite presentation is universally open, the converse being inexact. In §14 we
first examine the properties of the dimensions of the fibres of a universally open morphism `f : X → Y`; when `X` and
`Y` are locally Noetherian, `f` behaves in this respect `(14.2.1)` like a flat morphism (cf. `(6.1.2)`), and is in
particular equidimensional when it is locally of finite type and dominant and `X` is irreducible `(14.2.2)`. Conversely,
an equidimensional morphism `f : X → Y` locally of finite type is universally open when one supposes in addition that
`Y` is geometrically unibranch, and in particular when `Y` is normal (Chevalley's criterion, `(14.4.4)`). We show also
that the universally open morphisms `f : X → Y` locally of finite type (when `X` and `Y` are locally Noetherian and `Y`
is irreducible) admit "sufficiently many" quasi-sections, i.e. in a neighbourhood of a closed point `x` of a fibre
`f⁻¹(y)`, there exists a closed subprescheme `X'` of `X` containing `x` such that the restriction `X' → Y` of `f` is a
quasi-finite (hence with discrete fibres) and dominant morphism `(14.5.3)`.

<!-- original page 200 -->

In §15 we study various properties of the fibres of universally open morphisms `f : X → Y` locally of finite type,
notably when `X` and `Y` are locally Noetherian. One thus obtains in particular a criterion for a point `x ∈ X` to
belong to only one irreducible component of `X`, in terms of properties of the fibre `f⁻¹(f(x))` of `x`: it suffices
that `Y` be geometrically unibranch (for example normal) at the point `f(x)` and that `f⁻¹(f(x))` be geometrically
pointwise integral at the point `x` `(15.3.3)`; if in addition `Y` is locally integral at the point `f(x)`, `f` is flat
at the point `x` and `X` is locally integral at the point `x`. We also study the variation of the geometric number of
connected components of a fibre `f⁻¹(y)`; for example, if `f` is universally open and proper, and the fibres of `f` are
geometrically reduced, this number is locally constant `(15.5.7)`. Finally, when `f` admits a section `g` (which will be
the case when `X` is a `Y`-group scheme), and when for every `y ∈ Y` one denotes by `X°_y` the connected component of
the fibre `X_y = f⁻¹(y)` at the point `g(y)` (the "neutral component" in the case of groups), one studies the union `X°`
of the `X°_y` for `y ∈ Y`, and one shows `(15.6.4)` that if `f` is universally open and the fibres `X_y` geometrically
reduced, then `X°` is an open set in `X`.

### 14.1. Open morphisms

**(14.1.1)**

<!-- label: IV.14.1.1 -->

Recall `(1.10.2)` that a continuous map `ψ : X → Y` is said to be **open at a point `x ∈ X`** if the image under `ψ` of
every neighbourhood of `x` in `X` is a neighbourhood of `ψ(x)` in `Y`.

One notes that this does not imply that there exists a fundamental system of neighbourhoods of `x` whose images are open
in `Y`.

**Proposition (14.1.2).**

<!-- label: IV.14.1.2 -->

*Let `X`, `Y` be two topological spaces, `ψ : X → Y` a continuous map, `x` a point of `X`, `y = ψ(x)`.*

*(i) If `ψ` is open at `x`, then for every part `Y'` of `Y` containing `ψ(x)` the restriction `ψ⁻¹(Y') → Y'` of `ψ` to
`Y'` is open at the point `x`.*

*(ii) Suppose that `Y` is the union of a locally finite family of closed parts `(Y_i)` and that for every `i` such that
`ψ(x) ∈ Y_i`, the restriction `ψ⁻¹(Y_i) → Y_i` of `ψ` is open at the point `x`; then `ψ` is open at the point `x`.*

*(iii) Let `γ : X' → X` be a continuous map, `x'` a point of `X'`; if the composite map `ψ ∘ γ : X' → Y` is open at the
point `x'`, then `ψ` is open at the point `γ(x')`.*

If `U` is a neighbourhood of `x`, one has `ψ(U ∩ ψ⁻¹(Y')) = ψ(U) ∩ Y'`; whence (i) at once. To prove (ii), note that
there is a neighbourhood `W` of `ψ(x)` in `Y` meeting only finitely many of the closed parts `Y_i` that contain `ψ(x)`;
hence `W` is the union of the `W ∩ Y_i` for these indices. Now, if `U` is a neighbourhood of `x` such that `ψ(U) ∩ Y_i`
is a neighbourhood of `ψ(x)` in `Y_i`, there exists a neighbourhood `V ⊂ W` of `ψ(x)` in `Y` such that for all `i` with
`ψ(x) ∈ Y_i` one has `V ∩ Y_i ⊂ ψ(U) ∩ Y_i`, and since the union of the `V ∩ Y_i` for these indices is `V`, one has
`V ⊂ ψ(U)`, hence `ψ(U)` is a neighbourhood of `ψ(x)` in `Y`. Assertion (iii) is trivial.

**Remarks (14.1.3).**

<!-- label: IV.14.1.3 -->

*(i) The set `Z` of points `x ∈ X` where a morphism is open is not necessarily open.* For example, let `K` be a field,
`A` the polynomial ring `K[S, T]`, `V` the affine plane `Spec(A)`, `X` the closed subprescheme of `V` "the union of the
line `X_1` defined by `T = 0` and the line `X_2` defined by `S = 0`", that is to say `Spec(A/𝔞)`, where `𝔞 = AST`; take
`Y = X_2 = Spec(A/AS)` and for `f` the projection corresponding to the canonical injection `K[T] → A/𝔞`; then one has
`Z = X_2`, which is not open in `X`.

*(ii)* Let `X`, `Y` be two Noetherian irreducible preschemes with generic points `ξ`, `η` respectively, and `f : X → Y`
a dominant morphism locally of finite type; then `f` is open at the point `ξ`. Indeed, one may obviously restrict to the
case where `X` and `Y` are reduced (hence integral) `(1.5.4)` and affine; by virtue of the generic flatness theorem
`(6.9.1)`, there exists a non-empty open set `V` of `Y` such that the restriction `f⁻¹(V) → V` of `f` is a flat
morphism, and one concludes from `(2.4.6)` that this restriction is an open morphism. However, as there exist dominant
morphisms of finite type `f : X → Y` (where `X` and `Y` are irreducible) which are not open (see for example
`(II, 8.1)`), the set of points where such a morphism is open is not necessarily closed in `X`.

*(iii)* We do not know whether, when `X` and `Y` are locally Noetherian and `f : X → Y` is a morphism locally of finite
type, the set of points of `X` where `f` is open is or is not locally constructible.

**Proposition (14.1.4).**

<!-- label: IV.14.1.4 -->

*Let `X`, `Y` be two topological spaces, `ψ : X → Y` a continuous map. For every `y ∈ Y`, the set of `x ∈ ψ⁻¹(y)` where
`ψ` is open is a closed part of `ψ⁻¹(y)`.*

Indeed, suppose that `ψ` is not open at a point `x ∈ ψ⁻¹(y)`; there exists then an open neighbourhood `V` of `x` in `X`
such that `ψ(V)` is not a neighbourhood of `y`; it follows that for every `x' ∈ V ∩ ψ⁻¹(y)`, `ψ` is not open at the
point `x'`.

**Remark (14.1.5).**

<!-- label: IV.14.1.5 -->

Even if `X` and `Y` are locally Noetherian and `f` is a finite morphism, it can happen that `f` be open at all points of
a fibre `f⁻¹(y)`, without there existing a neighbourhood of `f⁻¹(y)` at all points of which `f` is open. Let for example
`K` be a field, `A` the polynomial ring `K[T_1, T_2, T_3]`, `V = Spec(A)` affine 3-space over `K`, `X = Spec(A/𝔞)`,
where `𝔞 = 𝔟𝔠`, with `𝔟 = (T_3)` and `𝔠 = (T_1) + (T_2 − T_3)` in `A`, so that `X` is the union of the plane
`X_1 = Spec(A/𝔟)` ("plane of equation `T_3 = 0`") and the line `X_2 = Spec(A/𝔠)` ("line of equations `T_1 = 0`,
`T_2 = T_3`"), which are its irreducible components. Take `Y = X_1` and let `f : X → Y` be the projection corresponding
to the canonical injection `K[T_1, T_2] → A/𝔞`; if `y` is the point common to `X_1` and `X_2`, `f⁻¹(y)` reduces to `y`
and `f` is open at this point but is open at no point of `X_2` in a neighbourhood of `y` and distinct from `y`.

**(14.1.6)**

<!-- label: IV.14.1.6 -->

In what follows, the essential role will be played by the criterion `(1.10.3)` characterizing the morphisms locally of
finite presentation `f : X → Y` that are open at a point `x` by "lifting of generizations": for every generization `y'`
of `y = f(x)`, there exists `x' ∈ X`, a generization of `x`, such that `y' = f(x')`.

<!-- original page 201 -->

### 14.2. Open morphisms and the dimension formula

**Theorem (14.2.1).**

<!-- label: IV.14.2.1 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a morphism, `x` a point of `X`, `y = f(x)`. Suppose that
`f` is open at the generic points of the irreducible components of `f⁻¹(y)` containing `x`. Then one has the relation*

```text
  (14.2.1.1)             dim(𝒪_x) = dim(𝒪_y) + dim_x(f⁻¹(y)).
```

Let `y'` be any generization of `y` distinct from `y`, and consider the reduced closed subprescheme `Y'` of `Y` with
underlying space `‾{y'}`; then no irreducible component `X'` of `f⁻¹(Y')` containing `x` can be contained in `f⁻¹(y)`:
indeed, if `x'` is the generic point of `X'`, one would have `f(x') = y ≠ y'`, and as `x'` is its only generization in
`f⁻¹(Y')`, this would contradict the hypothesis that `f` is open at the point `x'`, by virtue of the fact that a)
implies c) in `(1.10.3)`. One can therefore apply `(6.1.2)` to the local homomorphism of Noetherian rings `𝒪_y → 𝒪_x`,
whence the conclusion.

**Corollary (14.2.2).**

<!-- label: IV.14.2.2 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`,
`y = f(x)`. Suppose `f` open at the generic points of the irreducible components of `f⁻¹(y)` containing `x`. Then `f` is
equidimensional at the point `x` in each of the following two cases:*

*(i) `X` is irreducible and `f` is dominant.*

*(ii) The rings `𝒪_x` and `𝒪_y` are equidimensional.*

For (i), this results from `(14.2.1)` and `(13.2.3)`. For (ii), this results from `(14.2.1)` and `(13.3.6)`.

**Proposition (14.2.3).**

<!-- label: IV.14.2.3 -->

*Let `Y` be an irreducible locally Noetherian prescheme, `η` its generic point, `f : X → Y` a morphism locally of finite
type, `y` a point of `f(X)`, `Z` an irreducible component of `f⁻¹(y)` such that `f` is open at the generic point of `Z`.
Then `Z` is contained in an irreducible component `X'` of `X` dominating `Y` and such that*

```text
  dim_z(X') = dim(𝒪_y) + dim(Z) = dim(𝒪_y) + dim_z(f⁻¹(y)).
```

This results indeed from `(14.2.1)` applied to the generic point of `Z`, and from `(13.2.7)`.

**Corollary (14.2.4).**

<!-- label: IV.14.2.4 -->

*With the notation of `(14.2.3)`, suppose that `f` is open at all points of `f⁻¹(y)`. For every `z ∈ Y`, let `E(z)` be
the set of dimensions of the irreducible components of `f⁻¹(z)` and `d(z) = sup E(z) = dim(f⁻¹(z))`. Then one has
`E(y) ⊂ E(η)`, whence `d(y) ≤ d(η)`.*

This results at once from `(14.2.3)`.

**Corollary (14.2.5).**

<!-- label: IV.14.2.5 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism, `y ∈ Y` a point such that `f` is open at all
points of `f⁻¹(y)`. Then the function `z ↦ dim(f⁻¹(z))` is constant in a neighbourhood of `y`.*

Let `Y_i` (`1 ≤ i ≤ n`) be the reduced closed subpreschemes of `Y` whose underlying spaces are the irreducible
components of `Y` containing `y`; if `f_i : f⁻¹(Y_i) → Y_i` is the restriction of `f`, one knows that each of the `f_i`
is proper `(II, 5.4.5)` and open at all points of `f⁻¹(y)` `(14.1.2)`. As the union of the `Y_i` is a neighbourhood of
`y` in `Y`,

<!-- original page 202 -->

one sees that one may restrict to proving the corollary when `Y` is irreducible; let `η` be its generic point. It
follows from `(14.2.4)` that `d(y) ≤ d(η)`; on the other hand, since `f` is proper, one deduces from `(13.1.5)` that
`z ↦ dim(f⁻¹(z))` is upper semi-continuous; in particular `d(y) ≥ d(η)`, hence `d(y) = d(η)`. Moreover, there is a
neighbourhood `V` of `y` such that `d(z) ≤ d(y)` for every `z ∈ V`; but as `z` is a specialization of `η`, one has on
the other hand `d(z) ≥ d(η)`, whence finally `d(z) = d(y)` for `z ∈ V`.

**Corollary (14.2.6).**

<!-- label: IV.14.2.6 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` an open morphism of finite type, `y` a point of `Y`. Let `y_i`
(`1 ≤ i ≤ n`) be the generic points of the irreducible components of `Y` containing `y`. Then, with the notation of
`(14.2.4)`:*

*(i) If for `1 ≤ i ≤ n`, one has `E(y) = E(y_i)` (resp. `d(y) = d(y_i)`), the function `E` (resp. `d`) is constant in a
neighbourhood of `y`.*

*(ii) There exists an open neighbourhood `U` of `f⁻¹(y)` such that the function `z ↦ dim(U ∩ f⁻¹(z))` is constant in a
neighbourhood of `y`.*

(i) The same reasoning as in `(14.2.5)` shows that one may restrict to the case where `Y` is irreducible, of generic
point `η`. If `y'` is any generization of `y`, one has (applying `(14.2.4)` to the restriction `f⁻¹(Y') → Y'` of `f`,
where `Y' = ‾{y'}`, and using `(14.1.2)`) `E(y) ⊂ E(y') ⊂ E(η)` and `d(y) ≤ d(y') ≤ d(η)`; this shows that the relation
`E(y) = E(η)` (resp. `d(y) = d(η)`) entails `E(y) = E(y')` (resp. `d(y) = d(y')`) for every generization `y'` of `y`.
Now, by virtue of `(9.5.5)`, the functions `E` and `d` are locally constructible, hence it follows from `(0_III, 9.2.5)`
applied to the set of `z` such that `E(z) = E(y)` (resp. `d(z) = d(y)`) that this set is a neighbourhood of `y`.

(ii) For each of the `y_i`, `f⁻¹(y_i)` is a Noetherian space since `f` is of finite type; let `x_{ij}` (`1 ≤ j ≤ m_i`)
be the generic points of its irreducible components, and set `X_{ij} = ‾{x_{ij}}`; we show that the complement `U` in
`X` of the union of the `X_{ij}` that do not meet `f⁻¹(y)` (which is evidently an open neighbourhood of `f⁻¹(y)`)
answers the question. Indeed, the restriction `f|U : U → Y` of `f` is an open morphism of finite type `(I, 6.3.5)`; for
every pair `(i, j)` such that `x_{ij} ∈ U`, `x_{ij}` is a maximal point of `U ∩ f⁻¹(y_i)` and it follows from `(13.1.1)`
applied to the restriction `X_{ij} → ‾{y_i}` of `f` (taking into account `(I, 5.2.2)` and `(I, 5.4)`) that all the
irreducible components of `X_{ij} ∩ f⁻¹(y)` have a dimension `≥ dim(X_{ij} ∩ f⁻¹(y_i))`. Taking into account `(14.2.3)`
applied to the restriction `f⁻¹(Y_i) → Y_i` of `f` which is an open morphism `(14.1.2)`, `f⁻¹(y)` is, for each `i`, the
union of the irreducible components of `X_{ij} ∩ f⁻¹(y)` (`1 ≤ j ≤ m_i`), hence `dim(f⁻¹(y)) ≥ dim(U ∩ f⁻¹(y))`; but
since `f|U` is open, one also has `dim(f⁻¹(y)) ≤ dim(f⁻¹(y) ∩ U)` by virtue of `(14.2.4)`; one sees therefore that one
may apply (i) to `f|U`, whence the conclusion.

**Remark (14.2.7).**

<!-- label: IV.14.2.7 -->

The example `(13.2.12, (iii))` shows that under the hypotheses of `(14.2.5)` or `(14.2.6, (ii))`, one cannot, in the
conclusion, replace the function `z ↦ dim(f⁻¹(z))` by the function `z ↦ E(z)`; indeed, in that example, `f` is proper
and flat (hence universally open `(2.4.6)`) and every neighbourhood of the unique point of `f⁻¹(y)` contains the generic
points of the irreducible components of `f⁻¹(η)`.

<!-- original page 203 -->

### 14.3. Universally open morphisms

**(14.3.1)**

<!-- label: IV.14.3.1 -->

Recall `(2.4.2)` that to say that a morphism `f : X → Y` is **universally open** signifies that for every morphism
`g : Y' → Y`, `f_{(Y')} : X_{(Y')} → Y'` is open; it moreover suffices that this hold when `Y' = Y[T_1, …, T_e]`, for
every `e` `(8.10.2)` (and if `Y` is locally Noetherian, it therefore suffices that this hold for every locally
Noetherian `Y'`).

**Proposition (14.3.2).**

<!-- label: IV.14.3.2 -->

*Let `f : X → Y` be a morphism of preschemes. If `f` is universally open, then, for every morphism `g : Y' → Y`, where
`Y'` is irreducible, the image under `f' = f_{(Y')} : X_{(Y')} → Y'` of every irreducible component of `X_{(Y')}` is
dense in `Y'`. Conversely, if this condition is satisfied for every irreducible `Y'` and every morphism of finite type
`g : Y' → Y`, and if moreover `f` is locally of finite presentation, then `f` is universally open.*

Indeed, it follows from `(1.10.4)` that if `f` is universally open, it satisfies the condition of the statement.
Conversely, suppose that `f` is locally of finite presentation, and let us show that for every integer `e`, if one sets
`Y'' = Y[T_1, …, T_e]`, `f_{(Y'')}` is open. Indeed, let `Y'` be a closed subprescheme of `Y''` whose underlying space
is an irreducible closed part of `Y''`; the composite morphism `Y' → Y'' → Y` is of finite type, hence every irreducible
component of `X_{(Y')}` dominates `Y'` by hypothesis; one therefore deduces from `(1.10.4)` that `f_{(Y'')}` is an open
morphism.

This proposition shows that the definition `(III, 4.3.9)` coincides in the case considered with the general definition
of universally open morphisms given in `(2.4.2)`.

To the notion of morphism open at a point `(14.1.1)` likewise corresponds the following:

**Definition (14.3.3).**

<!-- label: IV.14.3.3 -->

*Let `f : X → Y` be a morphism of preschemes, `x` a point of `X`. One says that `f` is **universally open at the point
`x`** if, for every morphism `g : Y' → Y`, setting `X' = X ×_Y Y'`, the morphism `f' = f_{(Y')} : X' → Y'` is open at
every point `x'` of `X'` whose projection in `X` is `x`.*

**Remarks (14.3.3.1).**

<!-- label: IV.14.3.3.1 -->

*(i)* The reasoning of `(8.10.1)` shows (with the same notation) that if `x` is a point of `X` and `x_λ` its projection
in `X_λ`, then, if `f_λ` is open at the point `x_λ` for every `λ ∈ X`, `f` is open at the point `x`; it suffices to
restrict to the open sets `U` of `X` containing `x` and to remark that the hypothesis implies that `f_λ(U_λ)` is a
neighbourhood of `f_λ(x_λ)`, hence `f(p_λ⁻¹(U_λ))` is a neighbourhood of `f(x)`. One deduces that the statement
`(8.10.2)` is still exact when one replaces "universally open" by "universally open at the point `x`", and "open
morphism" by "open morphism at every point `x''` of `X''` whose projection in `X` is `x`": it suffices in the proof to
restrict to the open sets `V` containing some `x''`.

*(ii)* The result of `(14.1.4)` remains valid for a morphism `f : X → Y`, replacing "open" by "universally open".
Indeed, suppose that `f` is not universally open at a point `x ∈ f⁻¹(y)`; there is consequently a morphism `Y' → Y` and
a point `x' ∈ X'` projecting to `x`, such that `f'` is not open at the point `x'`.

<!-- original page 204 -->

Now, if `y' = f'(x')`, the projection `f'⁻¹(y') → f⁻¹(y)` is an open morphism `(2.4.10)`, and there is, by virtue of
`(14.1.4)`, a neighbourhood `V` of `x'` in `f'⁻¹(y')` where `f'` is not open; hence `f` is not universally open at the
points of the image of `V` in `f⁻¹(y)`, which is a neighbourhood of `x` in `f⁻¹(y)`.

**Proposition (14.3.4).**

<!-- label: IV.14.3.4 -->

*(i) Let `f : X → Y`, `g : Y → Z` be two morphisms, `x` a point of `X`, `y = f(x)`. If `f` is universally open at the
point `x` and `g` universally open at the point `y`, then `g ∘ f` is universally open at the point `x`. Conversely, if
`g ∘ f` is universally open at the point `x`, `g` is universally open at the point `y`.*

*(ii) If `f : X → Y` is an `S`-morphism universally open at the point `x ∈ X`, then, for every base change `S' → S`,
`f_{(S')} : X_{(S')} → Y_{(S')}` is universally open at every point of `X_{(S')}` above `x`.*

*(iii) For `f : X → Y` to be universally open at the point `x ∈ X`, it is necessary and sufficient that `f_red` be so.*

*(iv) Let `f : X → Y` be a morphism locally of finite presentation, `x` a point of `X`, `y = f(x)`; set
`Y_1 = Spec(𝒪_y)`, `X_1 = X ×_Y Y_1`, `f_1 = f_{(Y_1)}`. For `f` to be universally open at the point `x`, it is
necessary and sufficient that `f_1` be so* (one recalls `(I, 3.6.5)` that `X_1` is canonically identified with a
subspace of `X`).

Indeed (ii) is an evident consequence of the definition `(14.3.3)`; it also results from the definition that to prove
assertion (i), it suffices to do so when one suppresses the word "universally" everywhere, and this then results from
`(14.1.2)`. Assertion (iii) results from (ii) and from the fact that the canonical morphism `X_red → X` is surjective.
Finally, condition (iv) is trivially necessary. On the other hand, if it is satisfied, and if `g : Y' → Y` is an
arbitrary morphism, `X' = X_{(Y')}`, `f' = f_{(Y')}`, `x'` a point of `X'` above `x`, then `f'` is locally of finite
presentation, and to see that it is open at the point `x'`, it suffices to apply the criterion `(1.10.3, c))`. Set
`y' = f'(x')`, `Y'_1 = Spec(𝒪_{y'})`, `X'_1 = X' ×_{Y'} Y'_1`, `f'_1 = f'_{(Y'_1)}`. Since `g(y') = y`, the composite
morphism `Y'_1 → Y' → Y` factors as `Y'_1 → Y_1 → Y` `(I, 2.4.4)`, hence `X'_1 = X_1 ×_{Y_1} Y'_1` and
`f'_1 = (f_1)_{(Y'_1)}`; the conclusion then results at once from the hypothesis that `f_1` is open at the point `x'`
and from `(1.10.3)`.

**Proposition (14.3.5).**

<!-- label: IV.14.3.5 -->

*Let `X`, `Y` be two preschemes, `f : X → Y` a morphism, `x` a point of `X`. Let `(Y_i)_{1 ≤ i ≤ n}` be a locally finite
family of closed subpreschemes of `Y` such that the space `Y` is the union of the `Y_i`, and suppose that for every `i`
such that `f(x) ∈ Y_i`, the restriction `f⁻¹(Y_i) → Y_i` of `f` is a morphism universally open at the point `x`; then
`f` is universally open at the point `x`.*

Taking the definition into account, this results from the analogous proposition `(14.1.2, (ii))` for morphisms open at a
point.

**Proposition (14.3.6).**

<!-- label: IV.14.3.6 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type. For `f` to be universally
open at a point `x ∈ X`, it is necessary and sufficient that the following condition be satisfied: for every morphism
`g : Y' → Y`, where `Y' = Spec(A)` is the spectrum of a discrete valuation ring, such that the image `g(y')` of the
closed point `y'` of `Y'` is equal to `y = f(x)`, and for every point `x' ∈ X' = X ×_Y Y'` whose projections on `X` and
`Y'` are `x` and `y'` respectively, there exists a generization `z'` of `x'` in `X'` whose projection in `Y'` is the
generic point of `Y'` (in other words, there exists an irreducible component of `X'` containing `x'` and dominating
`Y'`).*

<!-- original page 205 -->

*Moreover, one may, in the preceding condition, restrict to the case where `A` is complete, has an algebraically closed
residue field, and where `x'` is rational over `k(y')`.*

If `Y'` is as in the statement, the necessity of the condition results from the fact that `f'` must be open at the point
`x'`, and from the criterion `(1.10.3)`. To see that the condition is sufficient, consider a morphism of finite type
`g : Y'' → Y`, and let `X'' = X ×_Y Y''`, `f'' = f_{(Y'')} : X'' → Y''`, and `x''` a point of `X''` above `x`. Set
`y'' = f''(x'')`, and let `t` be a generization of `y''` in `Y''`, distinct from `y''`. Since `Y''` is locally
Noetherian, it follows from `(II, 7.1.9)` and `(0_III, 10.3.1)` that there exists a scheme `Y' = Spec(A)`, where `A` is
a complete discrete valuation ring whose residue field is an algebraic closure of `k(x'')`, and a morphism
`g : Y' → Y''` such that, if `s'` and `y'` are the generic point and closed point of `Y'`, one has `g(s') = t` and
`g(y') = y''`. There is then a point `x'` of `X' = X ×_Y Y' = X'' ×_{Y''} Y'` whose projections in `X''` and `Y'` are
`x''` and `y'` respectively, and which is rational over `k(y')` `(I, 3.4.9)`. The hypothesis implies that there is a
generization `z'` of `x'` in `X'` whose projection in `Y'` is `s'`; if `z''` is the projection of `z'` in `X''`, `z''`
is a generization of `x''` and its projection in `Y''` is `t`; one therefore concludes from `(1.10.3)` that `f''` is
open at the point `x''`, hence that `f` is universally open at the point `x` `(14.3.3.1, (i))`.

**Corollary (14.3.7).**

<!-- label: IV.14.3.7 -->

*The notation being that of `(14.3.6)`:*

*(i) Given a point `y ∈ Y`, for `f` to be universally open at all points of `f⁻¹(y)`, it is necessary and sufficient
that for every morphism `g : Y' → Y`, where `Y'` is the spectrum of a discrete valuation ring, and where the image
`g(y')` of the closed point `y'` of `Y'` is `y`, every irreducible component of `X' = X ×_Y Y'` dominates `Y'`.*

*(ii) For `f` to be universally open, it is necessary and sufficient that for every morphism `g : Y' → Y`, where `Y'` is
the spectrum of a discrete valuation ring, every irreducible component of `X' = X ×_Y Y'` dominates `Y'`.*

It is clear that it suffices to prove (i); the necessity of (i) results from `(14.3.2)` and its sufficiency from
`(14.3.6)`.

**Proposition (14.3.8).**

<!-- label: IV.14.3.8 -->

*Let `Y` be a locally Noetherian prescheme, irreducible, regular and of dimension `1` (for example the spectrum of a
Dedekind ring), `f : X → Y` a morphism locally of finite type, `y` a point of `Y`. The following conditions are
equivalent:*

*a) `f_red` is flat at every point of `f⁻¹(y)`.*

*b) `f` is universally open in a neighbourhood of `f⁻¹(y)`.*

*c) `f` is open in a neighbourhood of `f⁻¹(y)`.*

*d) Every irreducible component of `X` meeting `f⁻¹(y)` dominates `Y`.*

Since `f_red` is locally of finite type `(1.3.4)`, a) entails that `f_red` is flat in a neighbourhood of `f⁻¹(y)`
`(11.1.1)`, and it suffices to apply `(2.4.6)` in such a neighbourhood to see that a) entails b). The implication b) ⟹
c) is trivial, and the implication c) ⟹ d) results from `(1.10.4)` applied to a neighbourhood of `f⁻¹(y)`. It remains to
see that d) entails a). One may obviously, by virtue of `(1.3.4)`, restrict to the case where `X` is reduced. The
question being moreover local on `X` and on `Y`, one may suppose `Y = Spec(A)` and `X = Spec(B)` affine; if `X_i`
(`1 ≤ i ≤ n`) are the closed (integral) subpreschemes of `X` whose

<!-- original page 206 -->

underlying spaces are the irreducible components of `X`, then, for every `x ∈ X`, `𝒪_{X,x}`, being reduced, is a
sub-ring of the direct product of the `𝒪_{X_i,x}`; if `y = f(x)`, it will suffice to show that each of the `𝒪_{X_i,x}`
is a torsion-free `𝒪_y`-module, for it will then be the same for `𝒪_{X,x}`; as by hypothesis `𝒪_y` is a regular local
ring of dimension `1`, that is to say `(II, 7.1.6)` a discrete valuation ring, it will then result from `(0_I, 6.3.4)`
that `𝒪_{X,x}` is a flat `𝒪_y`-module. But if `X_i = Spec(B_i)`, where `B_i` is an integral ring, hypothesis d) entails
that the homomorphism `A → B_i` is injective `(I, 1.2.7)`; hence `B_i` is a torsion-free `A`-module, and *a fortiori*
`𝒪_{X_i,x}` is a torsion-free `𝒪_y`-module.

**Remarks (14.3.9).**

<!-- label: IV.14.3.9 -->

*(i)* In the statement of `(14.3.8)`, one cannot dispense with the hypothesis that `Y` is regular. With the notation of
`(11.7.5)`, take indeed `Y = Spec(A)`, `X = Spec(Â)`, so that `f : X → Y` is a finite surjective morphism; as `A` is an
integral local ring of dimension `1`, as is `Â`, it follows at once from `(1.10.4)` that the morphism `f` is open.
However `f` is not universally open (nor *a fortiori* flat), as is shown by `(11.7.5)`. One would have an analogous
example by taking for `Y` the local scheme at the double point of an algebraic curve having an "ordinary double point"
and for `X` the normalization of `Y`.

*(ii)* The example of `(14.1.3, (i))` shows that the set of points of `X` where a morphism is universally open is not
necessarily open, the morphism `f` in that example being universally open at all points where it is open. The example
`f : X → Y` seen above in (i) shows similarly that the set of points where a morphism is universally open is not
necessarily closed, for it is immediate that at all points of `X` except one the morphism `f` is universally open (it is
even a local isomorphism). It would be interesting to know whether the set of points where a morphism is universally
open is locally constructible.

The two following propositions have been pointed out to us by M. Artin:

**Lemma (14.3.10).**

<!-- label: IV.14.3.10 -->

*Let `A` be a valuation ring (not necessarily discrete), `k` its residue field, `K` its field of fractions, and set
`S = Spec(A)`. Let `X` be an irreducible prescheme, `f : X → S` a dominant morphism of finite type; let `X_0 = X ⊗_A k`
(resp. `X_1 = X ⊗_A K`) be the fibre of `f` at the closed point (resp. at the generic point) of `S`. Then, if `X_0 ≠ ∅`,
one has `dim(X_0) = dim(X_1)`.*

One may restrict to the case where `X` is affine, replacing `X` if need be by an affine open set containing a generic
point of an irreducible component of `X_0` of maximal dimension, and using `(4.1.1.3)`. Let `n = dim(X_0) ≥ 0`; it
follows from `(13.3.1.1)` that there exists a neighbourhood `U` of `X_0` in `X` and an `S`-morphism quasi-finite
`g : U → S[T_1, …, T_n] = Z` such that the restriction morphism `g_0 : U_0 = U ∩ X_0 → Z_0 = Spec(k[T_1, …, T_n])` is
finite and surjective. By the base change `Spec(K) → S` and restriction to the open set `U_1 = U ∩ X_1` of `X_1`, one
deduces from `g` a quasi-finite morphism `g_1 : U_1 → Z_1 = Spec(K[T_1, …, T_n])`. Since `U_1` is dense in `X_1`, one
has `dim(U_1) = dim(X_1)` `(4.1.1.3)`; the proposition will be established, by virtue of `(4.1.2)`, if we prove that the
morphism `g_1` is dominant. Suppose the contrary; there would then exist a non-zero polynomial `F_1 ∈ K[T_1, …, T_n]`
such that `g_1(U_1) ⊂ V(F_1)`. If `ω` is a valuation on `K` associated with `A`, and if `(c_α)` is the family of
coefficients of `F_1`, one may, after multiplication of `F_1` by a non-zero element of `K`, suppose that one has
`inf_α(ω(c_α)) = 0`; in other words, `F_1` comes from a polynomial `F ∈ A[T_1, …, T_n]`

<!-- original page 207 -->

(with which it identifies) such that the image `F_0` of `F` in `k[T_1, …, T_n]` is non-zero. Consider then in `Z` the
closed set `V(F)`; one has `V(F) ∩ Z_1 = V(F_1)`, and as `U_1` is dense in `U` (since it contains the generic point of
`X`), `g(U) ⊂ V(F)`; in

<!-- original page 208 -->

particular, one would have `g_0(U_0) ⊂ V(F) ∩ Z_0 = V(F_0)`; but since `F_0 ≠ 0`, `V(F_0)` is a closed part of `Z_0`
distinct from `Z_0`, and one reaches a contradiction. Q.E.D.

**Proposition (14.3.11).**

<!-- label: IV.14.3.11 -->

*Let `f : X → S` be a morphism of finite type, `(g_λ)_{λ ∈ L}` a family of universally open morphisms `g_λ : Y_λ → S`,
and for every `λ ∈ L`, let `u_λ : Y_λ → X` be an `S`-morphism. For every `s ∈ S`, set `X_s = X ×_S Spec(k(s))`,
`(Y_λ)_s = Y_λ ×_S Spec(k(s))`, and let `(u_λ)_s : (Y_λ)_s → X_s` be the morphism `u_λ ×_S 1` deduced from `u_λ` by base
change. Let `Z(s)` be the closure in `X_s` of the union of the sets `(u_λ)_s((Y_λ)_s)`, and set `d(s) = dim(Z(s))`.
Then, for every generization `s'` of a point `s ∈ S`, one has `d(s) ≤ d(s')`.*

One knows `(II, 7.1.4)` that there exists a valuation ring `A'` and a morphism `h : S' = Spec(A') → S` such that if `a`
(resp. `b`) is the closed point (resp. the generic point) of `S'`, one has `h(a) = s`, `h(b) = s'`. Moreover, the
projection morphism `p : X_s ⊗_{k(s)} k(a) → X_s` is surjective and open `(2.4.10)`, hence makes `X_s` a quotient space
of `X_s ⊗_{k(s)} k(a)` by an open equivalence relation; for every part `M` of `X_s`, `p⁻¹(M̄)` is therefore equal to the
closure `‾{p⁻¹(M)}` (Bourbaki, *Top. gén.*, chap. I, 4th ed., §5, n° 3, prop. 7); one reasons similarly for `X_{s'}`,
and taking into account `(I, 3.4.8)`, `(4.2.7)` and the fact that the `g_λ` are universally open, one sees that one may
reduce to proving the proposition in the situation obtained after base change `S' → S`. Suppose therefore `S' = S`, `s`
being the closed point and `s'` the generic point of `S`. The hypothesis that `g_λ` is open entails that every
irreducible component of `Y_λ` dominates `S` `(1.10.4)`, hence that its generic point is a maximal point of
`(Y_λ)_{s'}`; if `Z` denotes the closure in `X` of `Z(s')`, one therefore has `u_λ(Y_λ) ⊂ Z`, and consequently
`(u_λ)_s((Y_λ)_s) ⊂ Z_s = Z ∩ X_s`; in other words, one has `Z(s) ⊂ Z_s`, whence `dim(Z(s)) ≤ dim(Z_s)`. But applying
`(14.3.10)` to a reduced subprescheme of `X` whose underlying space is an irreducible component of `Z`, one obtains
`dim(Z_s) ≤ dim(Z_{s'})` (the inequality coming from the fact that there may be irreducible components of `Z` not
meeting `X_s`). On the other hand, since `Z(s')` is by definition closed in `X_{s'}`, one has `Z_{s'} = Z(s')`, which
completes the proof.

**Remark (14.3.12).**

<!-- label: IV.14.3.12 -->

The case envisaged by M. Artin was that where `Y_λ = S` for every `λ`, in other words the case where `(u_λ)` is a family
of `S`-sections of `X`. Another useful case is that where the family `(u_λ)` is reduced to a single element; one can
moreover always reduce to this case by considering the prescheme `Y` sum of the `Y_λ` and the morphisms `g : Y → S` and
`u : Y → X` whose restrictions to each `Y_λ` are respectively `g_λ` and `u_λ`.

**Proposition (14.3.13).**

<!-- label: IV.14.3.13 -->

*Let `f : X → Y` be a morphism locally of finite type, `y` a point of `Y`, `x` a maximal point of the fibre
`X_y = X ×_Y Spec(k(y))`.*

*Consider the following conditions:*

*a) `f` is universally open at the point `x` (or equivalently, at every point of the irreducible component of `X_y` of
generic point `x` `(14.3.3.1, (ii))`).*

*b) For every irreducible component `Y_0` of `Y` containing `y`, there exists an irreducible component `Z` of `X`
containing `x`, dominating `Y_0` and such that `dim_x(X_y) = dim_x(Z ∩ X_y) ≤ dim(Z ∩ X_η)`, where `η` is the generic
point of `Y_0` (which entails that `Z` is equidimensional over `Y_0` at the point `x` `(13.2.2)`).*

<!-- original page 209 -->

*b') For every open neighbourhood `U` of `x` in `X` and every generization `y'` of `y`, one has
`dim(U ∩ X_{y'}) ≥ dim_x(U ∩ X_y)`.*

*Then one has the implications a) ⟹ b) ⟺ b').*

To show that b) implies b'), it suffices to remark that `y'` belongs to an irreducible component `Y_0` of `Y` containing
`y`, of generic point `η`; taking `Z` as in b) and noting that the generic point of `Z` (which is also that of `Z ∩ X_η`
`(0_I, 2.1.8)`) is contained in `U`, one has `dim(U ∩ X_{y'}) ≥ dim(U ∩ Z ∩ X_{y'})`, and, by virtue of `(13.1.6)`,
`dim(U ∩ Z ∩ X_{y'}) ≥ dim(Z ∩ X_η)`; whence the assertion, since `dim_x(U ∩ X_y) = dim_x(X_y)` `(4.1.1.3)`.

To prove that b') implies b), one may first replace `X` by `f⁻¹(Y_0)`, hence suppose `Y_0 = Y`; one may restrict to the
case where `X` and `Y` are affine, since `dim_x(U ∩ X_y) = dim_x(X_y)` `(4.1.1.3)`. The irreducible components `W_i` of
the Noetherian prescheme `X_y` are then finite in number, and the complement of the union of the `W̄_i` (closures in
`X`) that do not contain `x` is an open neighbourhood `V` of `x`. Replacing `X` by `V`, one may therefore suppose that
`x ∈ W̄_i` for every `i` (hypothesis b') entails `dim(V ∩ X_y) ≥ 0`, hence `x` belongs to one of the `W̄_i` for at least
one `i`). Moreover, the `W̄_i` are exactly the irreducible components of `X` that dominate `Y` `(0_I, 2.1.8)`; this
being so, if one had, for each of these components `Z`, `dim(Z ∩ X_η) < dim_x(X_y)`, one would conclude
`dim(X_η) < dim_x(X_y)`, contrary to hypothesis b'). The relation `dim_x(Z ∩ X_y) = dim(Z ∩ X_η)` then results from
`(13.1.6)`.

It remains to prove that a) entails b'). Taking `(II, 7.1.4)` and the invariance of the hypotheses and the conclusion
under base change into account (by virtue of `(4.2.7)`), one may restrict to the case where `Y` is a spectrum of a
valuation ring, with closed point `y` and generic point `y'`, and where `U = X`. The hypothesis that `f` is open at the
point `x` entails that there exists an irreducible component `Z` of `X` containing `x` and dominating `Y` `(1.10.3)`.
Applying `(14.3.10)` to a neighbourhood of `x` in `Z`, one concludes that `dim(Z ∩ X_{y'}) = dim(Z ∩ X_y)`; but since
`x` is maximal in `X_y`, `Z ∩ X_y` contains the irreducible component of `X_y` of generic point `x`, hence
`dim_x(Z ∩ X_y) = dim_x(X_y)`; on the other hand, one has `dim(X_{y'}) ≥ dim(Z ∩ X_{y'})`, which completes the proof of
b').

**Remark (14.3.14).**

<!-- label: IV.14.3.14 -->

We do not know whether in `(14.3.13)` the conclusion remains valid when one replaces the hypothesis a) by the weaker
hypothesis that `f` is open at the point `x`. One may show easily that it would suffice to treat the case where `Y` is
the spectrum of an integral local ring whose generic point is isolated, and where `X` is a closed subprescheme of the
vector bundle `Y[T]`.

### 14.4. Chevalley's criterion for universally open morphisms

**Theorem (14.4.1).**

<!-- label: IV.14.4.1 -->

*Let `f : X → Y` be a morphism locally of finite type, `y` a point of `Y`, `x` a maximal point of the fibre
`X_y = X ×_Y Spec(k(y))`. Suppose `y` geometrically unibranch. Then the following conditions are equivalent:*

*a) `f` is universally open at the point `x` (or equivalently, at every point of the irreducible component of `X_y` of
generic point `x` `(14.3.3.1, (ii))`).*

<!-- original page 210 -->

*b) If `Y_0` is the unique irreducible component of `Y` containing `y` and `η` its generic point, there exists an
irreducible component `Z` of `X` containing `x`, dominating `Y_0` and such that `dim_x(Z ∩ X_y) = dim(Z ∩ X_η)` (which
signifies that `Z` is equidimensional over `Y_0` at the point `x` `(13.2.2)`).*

*b') For every open neighbourhood `U` of `x` in `X` and every generization `y'` of `y`, one has
`dim(U ∩ X_{y'}) ≥ dim_x(U ∩ X_y)`.*

*If moreover `Y` is locally Noetherian, these conditions are also equivalent to the following:*

*c) `f` is open at the point `x`.*

Note first that since `(𝒪_y)_red` is integral, `y` belongs to only one irreducible component `Y_0` of `Y`. The fact that
b) and b') are equivalent and that a) implies b') results from `(14.3.13)`; on the other hand, if `Y` is locally
Noetherian, one has seen in `(14.2.3)` that c) implies b). It therefore remains to show that when `y` is geometrically
unibranch, b) entails a).

**Lemma (14.4.1.1).**

<!-- label: IV.14.4.1.1 -->

*Let `Y` be a prescheme, `Y' = Y[T_1, …, T_n]`, `y'` a point of `Y'`, `y` its image in `Y`. If `Y` is geometrically
unibranch at the point `y`, then `Y'` is geometrically unibranch at the point `y'`.*

Indeed, since for every `y ∈ Y`, `Spec(k(y)[T_1, …, T_n])` is geometrically regular over `k(y)` `(0, 17.3.7)`, the
structure morphism `Y' → Y` is smooth `(6.8.1)`, and it suffices to apply `(11.3.14)`.

**Lemma (14.4.1.2).**

<!-- label: IV.14.4.1.2 -->

*Let `A` be an integral unibranch local ring, `B` an integral ring containing `A` and integral over `A`, `𝔫` a prime
ideal of `B` above the maximal ideal `𝔪` of `A`. Then the morphism `Spec(B_𝔫) → Spec(A)` is surjective; in other words,
for every prime ideal `𝔭` of `A`, there exists a prime ideal `𝔮` of `B` such that `𝔮 ⊂ 𝔫` and `𝔮 ∩ A = 𝔭`.*

Let `K` (resp. `L`) be the field of fractions of `A` (resp. `B`), `A'` the integral closure of `A`, `B'` the sub-ring of
`L` generated by `A'` and `B`, so that one has a commutative diagram of canonical injections

```text
                B  ─→  B'
                ↑       ↑
                A  ─→  A'
```

As `B'` is integral over `B`, there exists a prime ideal `𝔫'` of `B'` such that `𝔫' ∩ B = 𝔫` (Bourbaki, *Alg. comm.*,
chap. V, §2, n° 1, th. 1), and (for the same reason) `Spec(A') → Spec(A)` is surjective. On the other hand, since `A` is
unibranch, `A'` is a local ring; hence `𝔫' ∩ A'`, which is above the maximal ideal `𝔪` of `A`, is necessarily equal to
the unique maximal ideal `𝔪'` of `A'`. By virtue of the second Cohen-Seidenberg theorem (*loc. cit.*, §2, n° 4, th. 3),
the morphism `Spec(B'_{𝔫'}) → Spec(A')` is surjective, hence so is the composite `Spec(B'_{𝔫'}) → Spec(A') → Spec(A)`;
but this morphism is also the composite `Spec(B'_{𝔫'}) → Spec(B_𝔫) → Spec(A)`, hence the morphism `Spec(B_𝔫) → Spec(A)`
is surjective.

These lemmas being established, let us return to the proof of the implication b) ⟹ a) in `(14.4.1)`. By virtue of
`(14.3.3.1, (i))`, it suffices to prove that, for every integer `n ≥ 0` and every point `x'` of `X' = X[T_1, …, T_n]`
above `x`, the morphism

<!-- original page 211 -->

`f' : X' → Y' = Y[T_1, …, T_n]`, deduced from `f` by base change, is open at the point `x'`. Taking the lemma
`(14.4.1.1)`, `(2.3.4)` and `(4.2.7)` into account, one is therefore reduced to proving that `f` is open at the point
`x`: moreover, it evidently suffices `(14.1.2, (iii))` to show that the restriction of `f` to a closed subprescheme of
`X` having `Z` for underlying space is open at the point `x`, so that one may restrict to the case where `X = Z` is
irreducible. Replacing `X` by an open neighbourhood `V` of `x` such that `V ∩ X_y` is irreducible, one may suppose, by
virtue of `(13.3.1)`, that the morphism `f` factors as `X → Y'' = Y[T_1, …, T_m] → Y`, where `g` is quasi-finite,
dominant and locally of finite type. As the structure morphism `Y'' → Y` is open `(2.4.6)`, one is reduced to proving
that `g : X → Y''` is open at the point `x`. Moreover, by virtue of `(14.4.1.1)`, `g(x)` is a geometrically unibranch
point of `Y''`. One is therefore reduced to proving the following lemma:

**Lemma (14.4.1.3).**

<!-- label: IV.14.4.1.3 -->

*Let `X`, `Y` be two irreducible preschemes, `f : X → Y` a morphism locally quasi-finite and dominant. If `x ∈ X` is
such that `y = f(x)` is unibranch over `Y`, then `f` is open at the point `x`.*

It suffices to prove that `f(Spec(𝒪_{X,x})) = Spec(𝒪_{Y,y})` `(1.10.3)`. One may therefore restrict, by the base change
`Spec(𝒪_{Y,y}) → Y`, to the case where `Y = Spec(A)`, where `A` is a local ring and `y` is the closed point of `Y`
(taking into account `(I, 3.6.5)` and `(0_I, 2.1.8)`, which prove that `X ×_Y Spec(𝒪_{Y,y})` is irreducible); replacing
`f` by `f_red`, one may suppose `X` and `Y` reduced, hence integral. Replacing if necessary `X` and `Y` by affine
neighbourhoods of `x` and `y` respectively, one may suppose `(8.12.9)` that the morphism `f` factors as `X → X_1 → Y`,
where `j` is an open immersion and `g` a *finite* morphism (evidently dominant); as `X` and `X_1` are affine, `j` is
affine, hence separated and quasi-compact, and consequently factors as `X → X_2 → X_1`, where `X_2` is the closed image
of `X` by `j`, `h` the canonical injection and `u` an open immersion `(I, 9.5.3)`. In other words, one may suppose that
`X_1` is integral, or also of the form `X_1 = Spec(B)`, where `B` is an integral and finite `A`-algebra, containing `A`
since `g` is dominant. If `𝔫` is the prime ideal of `B` corresponding to the point `x`, the hypothesis that `A` is
unibranch then implies `(14.4.1.2)` that the morphism `Spec(B_𝔫) → Spec(A)` is surjective, that is,
`Spec(𝒪_{X,x}) → Spec(𝒪_{Y,y})` is surjective. Q.E.D.

**Corollary (14.4.2).**

<!-- label: IV.14.4.2 -->

*Let `f : X → Y` be a morphism locally of finite type, `y` a geometrically unibranch point of `Y`, `η` the generic point
of the unique irreducible component `Y_0` of `Y` containing `y`. The following conditions are equivalent:*

*a) `f` is universally open at all points of `X_y` (or, what comes to the same `(14.3.3.1, (ii))`, at the maximal points
of `X_y`).*

*b) For every `x ∈ X_y`, there exists an irreducible component `Z` of `X` containing `x` and equidimensional over `Y` at
the point `x` `(13.2.2)`.*

*b') For every `x ∈ X_y` and every open neighbourhood `U` of `x` in `X`, one has `dim(U ∩ X_η) ≥ dim_x(U ∩ X_y)`.*

*b'') For every open `U` of `X`, one has `dim(U ∩ X_η) ≥ dim(U ∩ X_y)`.*

<!-- original page 212 -->

*When moreover `Y` is locally Noetherian, these conditions are still equivalent to the following:*

*c) `f` is open at all points of `X_y` (or, what comes to the same `(14.3.3.1, (ii))`, at the maximal points of `X_y`).*

The equivalence of a) and c) when `Y` is locally Noetherian results from `(14.4.1)`; conditions b) or b'), applied to
the maximal points of `X_y`, entail a) by virtue also of `(14.3.3.1, (ii))`; finally, b') and b'') are equivalent, since

```text
   dim(U ∩ X_y) = sup_x(dim_x(U ∩ X_y)).
```

It remains to see that condition a) entails b) and b') at every point `x ∈ X_y`. Set `d = dim_x(X_y)`, and let `x'` be
the generic point of an irreducible component of `X_y` containing `x` and of dimension `d`. By virtue of a) and of
`(14.4.1)`, there is an irreducible component `Z` of `X` containing `x'` and equidimensional over `Y` at the point `x'`,
hence such that `dim_{x'}(Z ∩ X_y) = dim(Z ∩ X_η)`. But by construction `dim_{x'}(Z ∩ X_y) = dim_{x'}(X_y) = d`, and
`dim_x(Z ∩ X_y) ≤ dim(Z ∩ X_y) = d`; taking `(13.1.6)` into account, this proves that `Z` is equidimensional over `Y` at
the point `x`; hence a) entails b). Moreover, one has `dim(X_η) ≥ dim(Z ∩ X_η) = d = dim_x(X_y)`. Replacing `X` by an
open neighbourhood `U` of `x`, one sees thus that a) entails b'). Q.E.D.

**Corollary (14.4.3).**

<!-- label: IV.14.4.3 -->

*Let `Y` be a geometrically unibranch prescheme, `f : X → Y` a morphism locally of finite type. The following conditions
are equivalent:*

*a) `f` is universally open.*

*b) For every open `U` of `X`, every `y ∈ Y` and every generization `y'` of `y` one has
`dim(U ∩ X_{y'}) ≥ dim(U ∩ X_y)`.*

*If moreover `Y` is locally Noetherian, these conditions are also equivalent to the following:*

*c) `f` is open.*

**Corollary (14.4.4) (Chevalley's criterion).**

<!-- label: IV.14.4.4 -->

*Let `f : X → Y` be a morphism locally of finite type.*

*(i) If `f` is equidimensional at a point `x ∈ X` `(13.3.2)` and if `y = f(x)` is a geometrically unibranch point of
`Y`, `f` is universally open at the point `x`.*

*(ii) If `Y` is geometrically unibranch, `f` is universally open at all points of `X` where `f` is equidimensional, and
the set of these points is open in `X`. In particular, if `f` is equidimensional, it is universally open.*

Assertion (ii) is a trivial consequence of (i), since one already knows that the set of points where `f` is
equidimensional is open `(13.3.2)`. As for assertion (i), it results from the fact that the hypothesis implies that
condition b) of `(14.4.1)` is satisfied at the generic point of an irreducible component of `X_y` containing `x`, taking
`(13.3.1)` into account; it therefore suffices to apply `(14.4.1)`.

**Remark (14.4.5).**

<!-- label: IV.14.4.5 -->

One can prove that if `Y` is locally Noetherian, and if all the generizations of `y = f(x)` are geometrically unibranch
points of `Y` (cf. `(6.15.2)`), then, if `f` is equidimensional at the point `x`, it is universally open in a
neighbourhood of `x`.

<!-- original page 213 -->

**Corollary (14.4.6).**

<!-- label: IV.14.4.6 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type. Let `y` be a geometrically
unibranch point of `Y`, and suppose in addition that for every `x ∈ f⁻¹(y)`, the ring `𝒪_x` is equidimensional. Then the
following conditions are equivalent:*

*a) `f` is equidimensional `(13.3.2)` at all points of `f⁻¹(y)`.*

*b) `f` is open at all points of `f⁻¹(y)`.*

*c) `f` is universally open at all points of `f⁻¹(y)`.*

Indeed, c) trivially implies b), and a) implies c) by virtue of `(14.4.4)`; finally, in view of the hypotheses on `𝒪_y`
and `𝒪_x`, b) implies a) by `(14.2.2)`. More generally:

**Proposition (14.4.7).**

<!-- label: IV.14.4.7 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`, such that
`y = f(x)` is geometrically unibranch. The following conditions are equivalent:*

*a) `f` is equidimensional `(13.3.2)` at the point `x`.*

*b) The ring `𝒪_x` is equidimensional and `f` is open at the generic points of the irreducible components of `f⁻¹(y)`
containing `x` (hence also at every point of such a component).*

*c) The ring `𝒪_x` is equidimensional, and `f` is universally open at the generic points of the irreducible components
of `f⁻¹(y)` containing `x` (hence also at every point of such a component).*

*Moreover, when these conditions are satisfied, for every reduced closed subprescheme `X_i` of `X` whose underlying
space is an irreducible component of `X` containing `x`, the restriction `f_i : X_i → Y` of `f` is a morphism
equidimensional at the point `x`, and universally open at all points of the irreducible components of `f_i⁻¹(y) ∩ X_i`
that contain `x`.*

Condition a) implies that `f` is equidimensional at all generic points of the irreducible components of `f⁻¹(y)`
containing `x` `(13.3.1)`, and consequently `(14.4.4)` universally open at these points; the same reasoning applied to
each `f_i` (taking `(13.3.3)` into account) proves the last assertion of the proposition, taking `(14.3.3.1, (ii))` into
account. Moreover, by `(14.2.1)`, one has the relations

```text
  (14.4.7.1)              dim(𝒪_{X_i,x}) = dim(𝒪_y) + dim_x(f_i⁻¹(y))

  (14.4.7.2)              dim(𝒪_x) = dim(𝒪_y) + dim_x(f⁻¹(y))
```

and since `f` is equidimensional at the point `x`, it results from `(13.3.1)` that one has

```text
  dim_x(f⁻¹(y)) = dim_x(f_i⁻¹(y))    for every i.
```

One therefore concludes that `dim(𝒪_{X_i,x}) = dim(𝒪_x)` for every `i`, in other words `𝒪_x` is equidimensional, and
this completes the proof that a) entails c). It is clear that c) entails b); finally, b) entails the relation
`(14.4.7.2)` by virtue of `(14.2.1)`; it then results from `(13.3.6)` that b) entails a).

**Proposition (14.4.8).**

<!-- label: IV.14.4.8 -->

*Let `Y` be a Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `y` a point of `Y`, `x` a maximal
point of `X_y = f⁻¹(y)`. The following conditions are equivalent:*

*a) The morphism `f` is universally open at the point `x`, in other words, for every base change `g : Y' → Y`, one has
the property P(Y'): for every point `x'` of `X' = X ×_Y Y'` above `x`, the morphism `f' = f_{(Y')} : X' → Y'` is open at
the point `x'`.*

<!-- original page 214 -->

*a') Property P(Y') is true for every finite morphism `g : Y' → Y`.*

*a'') Property P(Y'') is true for the normalization `Y''` of `Y_red` `(II, 6.3.8)`.*

*b) For every point `x''` of `X'' = X ×_Y Y''` above `x`, there exists an irreducible component `Z''` of `X''`
containing `x''` and equidimensional over `Y''` at the point `x''`.*

It is trivial that a) implies a'). To show that a') implies a''), note that one may write `Y'' = Spec(ℬ)`, where `ℬ` is
a quasi-coherent `𝒪_Y`-Algebra integral over `𝒪_Y`; as `Y` is Noetherian, `ℬ` is the inductive limit of its
sub-`𝒪_Y`-Algebras `ℬ_λ` which are quasi-coherent and of finite type `(I, 9.6.6)`; but then the `ℬ_λ` are finite
`𝒪_Y`-Algebras `(II, 6.1.2)`; one may therefore write `Y'' = lim Y'_λ`, where `Y'_λ = Spec(ℬ_λ)`, whence
`X'' = X ×_Y Y'' = lim X'_λ`, with `X'_λ = X ×_Y Y'_λ`. By virtue of a'), the morphisms `f'_λ : X'_λ → Y'_λ` are open at
all points of `X'_λ` above `x`; one concludes that `f''` is open at all points of `X''` above `x`, by `(8.10.1)` and
`(14.3.3.1, (i))`.

As the prescheme `Y''` is normal by definition, the fact that b) entails a'') results from `(14.4.4)` applied to the
equidimensional irreducible component of the statement and to the restriction of `f''` to this component. It remains
therefore to show that a'') entails a) and b). Taking `(1.10.3)` into account, one may restrict to the case where
`Y = Spec(𝒪_y)`, noting that the canonical morphism `Spec(𝒪_y) → Y` is universally bicontinuous `(I, 3.6.5)`, and on the
other hand that `Y'' ×_Y Spec(𝒪_y)` is the normalization of `(Spec(𝒪_y))_red` as it results from the permutability of
the operations of integral closure and of localization (Bourbaki, *Alg. comm.*, chap. V, §1, n° 5, prop. 16). Supposing
therefore `Y = Spec(A)`, where `A` is a Noetherian local ring, and `y` the closed point of `Y`, one knows `(0, 23.2.5)`
that there exists a factorization

```text
   Y''  ─v─→  Y_1  ─u─→  Y
```

of the structure morphism, such that `v` is a finite surjective morphism, `u` an integral, radicial and dominant (hence
surjective `(II, 6.1.10)`, and consequently a universal homeomorphism `(2.4.5)`) morphism. If one sets
`X_1 = X ×_Y Y_1`, the projection `X'' → X_1` is therefore a homeomorphism, and hypothesis a'') consequently entails
that `f_1 = f_{(Y_1)} : X_1 → Y_1` is open at all points of `X_1` above `x`. Moreover, this shows that to prove property
b), it suffices to prove the same property where one replaces `Y''`, `X''` and `x''` by `Y_1`, `X_1` and a point `x_1`
of `X_1` above `x`. But `Y_1` is Noetherian and moreover it is geometrically unibranch since `Y''` is normal and `u`
radicial `(6.15.1)`; the property to be proven thus results from `(14.4.1)`. It remains to show that `f` is universally
open at the point `x`, which will result from the following lemma:

**Lemma (14.4.8.1).**

<!-- label: IV.14.4.8.1 -->

*Let `v : Y_1 → Y` be a closed (resp. universally closed) and surjective morphism. For a morphism `f : X → Y` to be open
(resp. universally open) at a point `x ∈ X`, it suffices that `f_1 = f_{(Y_1)} : X_1 = X ×_Y Y_1 → Y_1` be open (resp.
universally open) at all points of `X_1` above `x`.*

The second assertion results trivially from the first and from the fact that for every base change `Y' → Y`, the
morphism `v_{(Y')} : Y_1 ×_Y Y' → Y'` is still surjective and is closed if `v` is universally closed. To prove the first
assertion, consider

<!-- original page 215 -->

an open neighbourhood `U` of `x` in `X`; as `v` is closed and surjective, for `f(U)` to be a neighbourhood of
`y = f(x)`, it is necessary and sufficient that `v⁻¹(f(U))` be a neighbourhood of `v⁻¹(y)`. But if `p : X_1 → X` is the
canonical projection, one has `v⁻¹(f(U)) = f_1(p⁻¹(U))` `(I, 3.4.8)`, and the hypothesis implies that `f_1(p⁻¹(U))` is a
neighbourhood of `f_1(p⁻¹(x)) = v⁻¹(y)` `(I, 3.4.8)`.

**Corollary (14.4.9).**

<!-- label: IV.14.4.9 -->

*Let `Y` be a Noetherian prescheme, `f : X → Y` a morphism locally of finite type. The following conditions are
equivalent:*

*a) `f` is universally open, in other words, for every base change `Y' → Y`, the morphism `f_{(Y')} : X ×_Y Y' → Y'` is
open.*

*a') For every finite morphism `Y_1 → Y`, `f_{(Y_1)}` is open.*

*a'') If `Y''` is the normalization of `Y_red`, `f_{(Y'')}` is open.*

*b) For every point `x''` of `X'' = X ×_Y Y''`, there exists an irreducible component `Z''` of `X''` containing `x''`
and equidimensional over `Y''` at the point `x''` (cf. `(14.4.10, (ii))`).*

This results at once from `(14.4.8)` and `(14.1.4)`.

**Remarks (14.4.10).**

<!-- label: IV.14.4.10 -->

*(i)* The equivalence of conditions a) and b) in `(14.4.8)` (resp. `(14.4.9)`) remains valid for an arbitrary prescheme
`Y` and a morphism `f` locally of finite type. Indeed, a) entails b) by virtue of `(14.4.1)`; conversely, b) entails
that `f''` is universally open at the points of `X''` above `x` (resp. at every point of `X''`) by virtue of `(14.4.1)`,
and one concludes property a) by applying lemma `(14.4.8.1)` to the integral surjective morphism `Y'' → Y`.

It may be that, in `(14.4.1)`, for the equivalence of a) and c), the supplementary hypothesis that `Y` is Noetherian is
superfluous (cf. `(14.3.14)`). If so, the Noetherian hypotheses are also superfluous in `(14.4.2)`, `(14.4.3)`,
`(14.4.8)` and `(14.4.9)`.

*(ii)* One can give examples of morphisms `f : X → Y` having the following properties: `Y` is Noetherian, regular and of
dimension `2`, `f` is universally open and of finite type, `X` has two irreducible components `X_1`, `X_2`, but the
restriction `X_1 → Y` of `f` to one of them is not an open morphism. The principle of the construction relies on the
general method of "gluing" that will be explained in chap. V, and can therefore only be sketched here. One starts from a
closed point `y` of `Y`, and considers the `Y`-scheme `Y_1` obtained by blowing up `y` `(II, 8.1.3)`; if `f_1 : Y_1 → Y`
is the structure morphism, one knows that the restriction of `f_1` to `f_1⁻¹(Y − {y})` is an isomorphism onto `Y − {y}`
(*loc. cit.*), while the fibre `f_1⁻¹(y)` is isomorphic to `Proj(S)`, where `S = ⊕_{k = 0}^∞ 𝔪_y^k / 𝔪_y^{k+1}`
`(II, 3.5.3)`, that is to say here to `P¹_{k(y)}`; it follows from `(14.4.1)` that `f_1` is not open at the generic
point of `f_1⁻¹(y)`. On the other hand, set `Y_2 = P¹_Y`, and let `f_2 : Y_2 → Y` be the structure morphism; it follows
from `(II, 8.4.4)` that `f_2` is flat, hence universally open `(2.4.6)`; moreover `(II, 3.5.3)`, `f_2⁻¹(y)` is
isomorphic to `P¹_{k(y)}`; it then suffices to "glue" `Y_1` and `Y_2` along the isomorphic fibres `f_1⁻¹(y)` and
`f_2⁻¹(y)`, which gives a morphism `f : X → Y` where the irreducible components `X_1`, `X_2` of `X` are canonically
identified with `Y_1` and `Y_2` respectively, and the restrictions of `f` to these components with `f_1` and `f_2`.

Recall nevertheless `(12.1.1.5)` that if `Y` is locally Noetherian, `f : X → Y` of finite type and flat, then every
irreducible component of `X` is equidimensional over `Y` (and consequently the restriction of `f` to such a component is
universally open if all points of `Y` are geometrically unibranch).

*(iii)* Recall `(12.1.2, (i))` that there are morphisms `f : X → Y` having the following properties: `Y` is Noetherian
(not geometrically unibranch), `f` is finite and flat (and even étale `(17.6.3)`), but the restriction of `f` to an
irreducible component of `X` is not an open morphism (although `f` itself is by `(2.4.6)`).

*(iv)* Chevalley's criterion `(14.4.4)` explains the importance of the notion of universally open morphism. This notion
permits in effect, in numerous more or less classical results, to replace a hypothesis of normality by the hypothesis
that a certain morphism is universally open; the more general statement

<!-- original page 216 -->

obtained will apply in particular to flat morphisms `(2.4.6)`, whose importance in algebraic geometry is increasing. One
can consider that statements involving the hypothesis that a morphism is universally open are common generalizations of
statements involving a hypothesis of normality and of statements involving a hypothesis of flatness.

### 14.5. Universally open morphisms and quasi-sections

**Lemma (14.5.1).**

<!-- label: IV.14.5.1 -->

*Let `Y` be an irreducible locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of
`X`, such that `f` is equidimensional `(13.3.2)` at the point `x`; set `y = f(x)`, `e = dim_x(f⁻¹(y))`. Let `X'` be an
irreducible closed part of `X` containing `x`, `n` an integer such that one has `codim(X', X) ≤ n` and
`dim_x(X' ∩ f⁻¹(y)) ≥ e − n`. Then one necessarily has `codim(X', X) = n`, `dim_x(X' ∩ f⁻¹(y)) = e − n`, and the
restriction `X' → Y` of `f` is a morphism equidimensional at `x` (and *a fortiori* dominant).*

The question being local on `X`, one may suppose that `f` is of finite type and equidimensional, so that for every
`z ∈ Y`, all the irreducible components of `f⁻¹(z)` are of dimension `e` `(13.3.1, a''))`. Let `x'` be the generic point
of `X'`, `y' = f(x')`, `Y' = ‾{y'} = ‾{f(X')}`, and set `Z = f⁻¹(Y')`. By virtue of `(0, 14.2.2)`, one has

```text
  (14.5.1.1)            codim(X', Z) ≤ n
```

and if the two members are equal, one has necessarily `codim(X', X) = n` and `Z` contains an irreducible component of
`X`, which entails `(13.3.1)` that `f(X')` is dense in `Y` and consequently `Z = X`; hence the equality
`codim(X', Z) = n` is equivalent to the conjunction of the equality `codim(X', X) = n` and the relation `Z = X`.

On the other hand, reasoning in the reduced preschemes of `Y` and `X` having `Y'` and `Z` respectively for underlying
spaces, one deduces from `(5.1.2)` and `(I, 3.6.5)` that one has

```text
  (14.5.1.2)        codim(X' ∩ f⁻¹(y'), f⁻¹(y')) = codim(X', Z).
```

By virtue of the hypothesis, `f⁻¹(y')` is biequidimensional `(5.2.1)` and of dimension `e`, hence `(0, 14.3.5)`, one
has, by virtue of `(14.5.1.2)` and `(14.5.1.1)`,

```text
  (14.5.1.3)        e' = dim(X' ∩ f⁻¹(y')) = e − codim(X', Z) ≥ e − n
```

the equality holding if and only if `codim(X', X) = n` and `f(X')` is dense in `Y`.

Finally, by `(13.1.1)`, one has `dim_x(X' ∩ f⁻¹(y)) ≥ e'`, whence, by `(14.5.1.3)`,

```text
  (14.5.1.4)        dim_x(X' ∩ f⁻¹(y)) ≥ e' ≥ e − n.
```

Now, by hypothesis, one also has `dim_x(X' ∩ f⁻¹(y)) ≤ e − n`, whence the conclusions of the proposition.

**Corollary (14.5.2).**

<!-- label: IV.14.5.2 -->

*The hypotheses on `f`, `X`, `Y`, `x` being those of `(14.5.1)`, suppose in addition that `x` is not a maximal point of
`f⁻¹(y)`. Then there exists an affine open neighbourhood `U` of `x` in `X`, and a section `g ∈ Γ(U, 𝒪_X)` such that the
set `X'` of `x' ∈ U` such that `g(x') = 0` contains `x` and contains no maximal point of `f⁻¹(y)`. For every `g` having
these properties, `X'` is equidimensional over `Y` at the point `x`, and one has*

```text
  (14.5.2.1)         dim_x(X' ∩ f⁻¹(y)) = e − 1   and   codim(X', X) = 1.
```

<!-- original page 217 -->

One may restrict to the case where `X = U` is an affine open neighbourhood of `x` such that all the irreducible
components of `f⁻¹(y)` contain `x`. These components correspond to the minimal prime ideals of `𝒪_x|y = 𝒪_x/𝔪_y 𝒪_x`,
and by hypothesis these ideals are distinct from `𝔪_x/𝔪_y 𝒪_x` (Bourbaki, *Alg. comm.*, chap. II, §1, n° 1, prop. 2); to
obtain a `g ∈ Γ(U, 𝒪_X)` satisfying the conditions of the statement, it suffices to take `g ∈ 𝔪_x` such that the image
of `g` in `𝔪_x` does not belong to any of the preceding prime ideals. Moreover, one has `codim(X', X) ≤ 1` `(5.1.8)`,
and as `X'` contains none of the irreducible components of `f⁻¹(y)` and these are of dimension `e`, one has
`(0, 14.2.2.2)` `dim_x(X' ∩ f⁻¹(y)) ≤ e − 1`. It then suffices to apply `(14.5.1)`.

**Proposition (14.5.3).**

<!-- label: IV.14.5.3 -->

*Let `Y` be an irreducible locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of
`X`. Suppose that `f` is equidimensional at the point `x` and that `x` is closed in `f⁻¹(f(x))`. Then there exists an
irreducible part `X'` of `X`, locally closed in `X`, containing `x` and such that the restriction `X' → Y` of `f` (where
`X'` is the reduced subprescheme of `X` having `X'` as underlying space) is a quasi-finite dominant morphism.*

Indeed, with the notation of `(14.5.2)`, the hypothesis that `x` is closed in `f⁻¹(y)` entails that `x` is not a maximal
point of `X' ∩ f⁻¹(y)` as long as `e − 1 ≥ 1`. It therefore suffices to apply `(14.5.2)` reasoning by descending
induction on `e = dim_x(f⁻¹(f(x)))` until one reaches `e = 1`; the application of `(14.5.2)` in this last case gives an
`X'` such that `X' ∩ f⁻¹(f(x))` is Noetherian and of dimension `0`, hence finite and discrete; as `X'` is then
equidimensional over `Y`, `X' ∩ f⁻¹(f(x'))` is of dimension `0` for every `x' ∈ X'`, which entails that the restriction
`X' → Y` of `f` is a quasi-finite morphism `(II, 6.2.2)`.

**Corollary (14.5.4).**

<!-- label: IV.14.5.4 -->

*Under the hypotheses of `(14.5.3)`, suppose in addition that `Y = Spec(A)`, where `A` is a Noetherian integral complete
local ring, and that `y = f(x)` is the unique closed point of `Y`. Then there exists an integral local ring `A'`,
containing `A`, which is a finite `A`-algebra and has the following property: if one sets `Y' = Spec(A')` and
`X' = X ×_Y Y'`, there exists a `Y'`-section `h : Y' → X'` such that the composite morphism `Y' → X' → X` is an
immersion whose image contains `x`.*

Replacing if need be `X` by an irreducible reduced subprescheme of `X`, one may, by virtue of `(14.5.3)`, restrict to
the case where the morphism `f` is already quasi-finite and dominant. Using `(II, 6.2.5)`, one deduces that `𝒪_x = A'`
is an integral ring that is a finite `A`-algebra, and that `X` is the disjoint sum of the closed subprescheme
`Y' = Spec(A')` and a subprescheme `Y''`; the scheme `Y'` answers the question, the composite morphism `Y' → X' → X`
being none other than the canonical morphism `Spec(𝒪_x) → X`.

**Remark (14.5.5).**

<!-- label: IV.14.5.5 -->

If one does not require that in the statement of `(14.5.4)`, the morphism `Y' → X` be an immersion, one may suppose in
addition that `A'` is integrally closed: it suffices indeed to replace `A'` by its integral closure `A_1`, since one
knows `(0, 23.1.5)` that `A_1` is an `A`-module of finite type.

**Proposition (14.5.6).**

<!-- label: IV.14.5.6 -->

*Let `Y` be a locally Noetherian, irreducible, regular prescheme of dimension `1`, `f : X → Y` a morphism locally of
finite type, `y` a point of `Y`. The following conditions are equivalent:*

*a) `f_red` is flat at every point of `f⁻¹(y)`.*

<!-- original page 218 -->

*b) `f` is universally open in a neighbourhood of `f⁻¹(y)`.*

*c) `f` is open in a neighbourhood of `f⁻¹(y)`.*

*d) Every irreducible component of `X` meeting `f⁻¹(y)` dominates `Y`.*

*e) For every point `x ∈ f⁻¹(y)`, closed in `f⁻¹(y)`, and every irreducible component `X_i` of `X` containing `x`, there
exists an irreducible part `X'` of `X`, locally closed in `X`, containing `x`, contained in `X_i`, and such that the
restriction `X' → Y` of `f` is a quasi-finite dominant morphism.*

The equivalence of a), b), c) and d) has already been proved `(14.3.8)`. It is clear that e) entails d), for every
irreducible component `X_i` of `X` meeting `f⁻¹(y)` contains in `X_i ∩ f⁻¹(y)` a point closed in this space `(5.1.11)`.
Finally, to prove that c) entails e), one may restrict to the case where `f` is a morphism of finite type; consider a
closed point `x` of `f⁻¹(y)` and let `X_i` be an irreducible component of `X` containing `x`. As the restriction
`f_i : X_i → Y` of `f` to `X_i` is a dominant morphism, it follows from the equivalence of c) and d) for `f_i` that this
morphism is open at the generic points of `X_i ∩ f⁻¹(y)`. It follows therefore from `(14.2.2)` that `f_i` is
equidimensional at the point `x`, and one then concludes with the help of `(14.5.3)`.

**Remark (14.5.7).**

<!-- label: IV.14.5.7 -->

If, in the statement of `(14.5.5)`, one supposes that `Y = Spec(A)`, where `A` is a complete discrete valuation ring,
and that `y` is the closed point of `Y`, one may in addition suppose that `X' = Spec(A')`, where `A'` is a discrete
valuation ring that is a finite `A`-algebra, as is shown by the proof of `(14.5.4)` and the fact that an integral
regular local ring of dimension `1` is a discrete valuation ring `(II, 7.1.6)`.

**Proposition (14.5.8).**

<!-- label: IV.14.5.8 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `y` a point of `Y`.*

*For every `Y`-prescheme `Y'`, set `X(Y') = Hom_Y(Y', X)`. Let `x` be a point of `f⁻¹(y)`; in order that `f` be
universally open at the point `x`, it is necessary and sufficient that the following condition be satisfied:*

*For every complete discrete valuation ring `A`, with algebraically closed residue field, every morphism
`g : Y' = Spec(A) → Y` such that the image under `g` of the closed point `y'` of `Y'` is equal to `y`, and every element
`u_0 ∈ X(Spec(k(y')))` such that `u_0(y') = x`, there exists a discrete valuation ring `B`, a local homomorphism `A → B`
making `B` a finite `A`-algebra, and, setting `Z' = Spec(B)`, an element `u ∈ X(Z')` such that, if `z'` is the closed
point of `Z'`, the diagram*

```text
       Spec(k(z'))  ────→  Z' = Spec(B)
            │                    │
            │                    │ u
            ↓                    ↓
       Spec(k(y'))  ──u_0────→   X
```

*is commutative.*

Note that if `A` and `B` satisfy the conditions of the statement, `B` is a complete discrete valuation ring (Bourbaki,
*Alg. comm.*, chap. III, §3, n° 3, prop. 7 and chap. IV, §2, n° 2, cor. 3 of prop. 9) with residue field isomorphic to
that of `A`, hence

<!-- original page 219 -->

algebraically closed, and since `u(z') = x`, there is in `X'' = X ×_Y Z'` a point `x''` whose projections in `X` and
`Z'` are `x` and `z'` and which is rational over `k(z')`; in addition, since there exists a `Z'`-section `v` of `X''`
such that `v(z') = x''`, the image under `v` of the generic point `s` of `Z'` is a generization `t` of `x''` whose
projection in `Z'` is `s`; applying `(14.3.6)`, one sees that the condition of the statement is sufficient. Let us now
prove that it is necessary. Set `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`. There is by hypothesis a point `x' ∈ X'`
above `x` and `y'` and rational over `k(y')` `(I, 3.3.14)`, hence closed in `f'⁻¹(y')`. By virtue of `(14.3.6)`, there
is an irreducible component `T'` of `X'` containing `x'` and dominating `Y'`, hence (`(14.3.8)` and `(14.3.13)`) the
restriction `T' → Y'` of `f'` is equidimensional at the point `x`. One deduces from `(14.5.5)` that there is a finite
`A`-algebra `B` that is an integral integrally closed local ring and dominates `A` (hence is a discrete valuation ring);
and, setting `Z' = Spec(B)` and `X'' = X ×_Y Z' = X' ×_{Y'} Z'`, a `Z'`-section `v : Z' → X''` such that the image of
the closed point `z'` of `Z'` by the composite morphism `Z' → X'' → X'` is `x'`; the composite morphism
`u : Z' → X'' → X` then answers the question.

**Proposition (14.5.9).**

<!-- label: IV.14.5.9 -->

*Let `Y` be a locally Noetherian irreducible prescheme, `f : X → Y` a morphism locally of finite type, `y` a
geometrically unibranch point of `Y`. Then the following conditions are equivalent:*

*a) `f` is universally open at every point of `f⁻¹(y)`.*

*b) `f` is open at every point of `f⁻¹(y)`.*

*c) For every irreducible component `Z` of `f⁻¹(y)`, of generic point `z`, there exists an irreducible component `X_i`
of `X` containing `z` and equidimensional over `Y` at the point `z`.*

*d) For every closed point `x` of `f⁻¹(y)`, there exists an irreducible part `X'` of `X`, locally closed in `X`,
containing `x`, and such that the restriction `X' → Y` of `f` is a quasi-finite dominant morphism.*

The equivalence of a), b) and c) has already been proved `(14.4.2)`. To prove that a) entails d), note that by virtue of
`(14.4.2)`, a) entails that there exists an irreducible component `Z` of `X` containing `x` and equidimensional over `Y`
at the point `x`; the existence of `X'` then comes from `(14.5.3)` applied to the restriction `Z → Y` of `f`.
Conversely, suppose d) satisfied; by virtue of Chevalley's criterion `(14.4.4)`, the restriction `X' → Y` of `f` is a
morphism universally open at the point `x`, and *a fortiori* `f` is open at the point `x`; `f` is therefore open at all
the closed points of `X_y = f⁻¹(y)`. But `X_y` is a `k(y)`-prescheme locally of finite type, hence a Jacobson prescheme;
the set of closed points of `X_y` is therefore dense in `X_y` `(10.3.1)`, and it follows from `(14.1.4)` that `f` is
open at all points of `X_y`, which completes the proof that d) entails b).

The following result has been brought out by D. Mumford:

**Proposition (14.5.10).**

<!-- label: IV.14.5.10 -->

*Let `Y` be a Noetherian prescheme, `f : X → Y` a universally open, surjective and locally of finite type morphism. Then
there exists a finite surjective morphism `g : Y' → Y` such that, setting `X' = X ×_Y Y'` and `f' = f_{(Y')} : X' → Y'`,
every point `y' ∈ Y'` admits an open neighbourhood `U'` such that there exists a `U'`-section of `f'⁻¹(U')`.*

We shall prove the proposition in several steps.

<!-- original page 220 -->

I) *Reduction to the case where `Y` is integral.* — If one has proved the proposition for each of the reduced
subpreschemes `Y_i` having for underlying space an irreducible component of `Y`, and for the inverse images `f⁻¹(Y_i)`,
it is clear that the prescheme `Y'` sum of the corresponding `Y'_i` will answer the question. One may therefore suppose
`Y` integral and we shall in what follows restrict to this case. Then, in the conclusion, one may also take `Y'`
integral (replacing it if need be by a suitable irreducible component).

II) *Local character on `Y`.* — We shall show that if one can cover `Y` by finitely many open sets `U_j` such that, for
every `j`, the conclusion of the proposition is true for the morphism `f⁻¹(U_j) → U_j`, restriction of `f`, then the
conclusion is true also for `f`. Indeed, one may evidently suppose the `U_j` affine, so that `U_j = Spec(A_j)`, where
`A_j` is a Noetherian integral ring whose field of fractions `K = R(Y)` is the field of rational functions on `Y`. For
every `j`, there is by hypothesis a finite integral `A_j`-algebra `A'_j` such that the homomorphism `A_j → A'_j` is
injective `(I, 1.2.7)` and the corresponding morphism `g_j : U'_j = Spec(A'_j) → Spec(A_j) = U_j` satisfies the
conditions of the proposition (for `U_j` and `f⁻¹(U_j)`). Let then `K'` be a finite extension of `K` containing the
fields of fractions of all the `A'_j` (which are finite extensions of `K`). Consider the normalization `Y''` of `Y` in
`K'` `(II, 6.3.8)`, which is of the form `Spec(ℬ)`, where `ℬ` is an integral quasi-coherent `𝒪_Y`-Algebra, integral
closure of `𝒪_Y` in `K'` `(II, 6.3.4)`. These definitions prove that for every `j`,
`A''_j = Γ(U_j, ℬ) = Γ(U'_j, (g_j)_*(𝒪_{U'_j}))` is identified with a finite sub-`A_j`-algebra of `Γ(U_j, ℬ)`; in other
words, `(g_j)_*(𝒪_{U'_j}) = ℬ_j` is a coherent `𝒪_{U_j}`-Algebra, sub-Algebra of `ℬ|U_j`. There exists therefore a
coherent sub-`𝒪_Y`-Module `𝒞` of `ℬ` such that `𝒞|U_j = ℬ_j` `(I, 9.4.7)`. If one sets `𝒞' = 𝒞`, the sub-`𝒪_Y`-Algebra
`ℬ'` of `ℬ` generated by `𝒞` is coherent since `ℬ` is an integral `𝒪_Y`-Algebra. Let us show then that `Y' = Spec(ℬ')`
answers the question. Indeed, it is clear that the morphism `g : Y' → Y` is finite surjective and that `Y'` is integral;
in addition, for every `j`, `Γ(U_j, ℬ')` is a finite `A_j`-algebra, in other words the morphism `g⁻¹(U_j) → U_j`,
restriction of `g`, factors as `g⁻¹(U_j) → U'_j → U_j`, and as local existence of sections is stable under base change,
this establishes our assertion, every `y ∈ Y` belonging to some `U_j`.

III) *Reduction to the case where `Y` is integral, local and geometrically unibranch.* — Suppose first that the
proposition has been proved when `Y` is integral and local (with `Y'` integral), and let us show that it is valid when
`Y` is any (Noetherian) integral affine. Indeed, by virtue of the reduction II), it suffices to prove that for every
point `y ∈ Y`, the proposition is true for an affine open neighbourhood `V` of `y` in `Y`. Let `Y = Spec(A)`,
`Y_1 = Spec(A_𝔭)`, where `𝔭 = 𝔧_y`, and set `X_1 = X ×_Y Y_1`; by hypothesis, there exists a finite surjective morphism
`g_1 : Y'_1 → Y_1`, where `Y'_1 = Spec(B_1)`, `B_1` being an integral finite `A_𝔭`-algebra, hence a semi-local ring,
such that `g_1` satisfies the conditions of the statement for `Y_1` and `X_1`. If `y'_j` (`1 ≤ j ≤ r`) are the closed
points of `Y'_1`, there is therefore a covering of `Y'_1` by open sets `U'_j` such that `y'_j ∈ U'_j` and that there
exists a `U'_j`-section `h_j` of `X ×_Y U'_j` (`1 ≤ j ≤ r`). The `A_𝔭`-module `B_1` admits a finite system of generators
of the form `z_j/s` (with `s ∈ A − 𝔭`,

<!-- original page 221 -->

`z_j` integral over `A`), which one may suppose (multiplying if need be `s` by an element of `A`) to be elements of the
field of fractions of `B_1`, integral over `A_s`, so that if `V` is the affine open set `D(s) = Spec(A_s) ⊂ Y`, `Y'_1`
is identified with `Y' ×_Y V`, where `Y'` is the spectrum of the finite `A_s`-algebra generated by the `z_j/s`;
`g : Y' → V` is therefore a finite surjective morphism and `g_1 = g_{(Y_1)}`. Moreover, applying the method of
`(8.1.2, a))`, one may suppose that each of the `U'_j` is the inverse image under `p : Y'_1 → Y'` of an open set `W'_j`
of `Y'`, such that the `W'_j` cover `Y'` `(8.3.11)`, and that each of the sections `h_j` is of the form `(v'_j)_{(Y_1)}`
where `v'_j` is a `W'_j`-section of `X ×_Y W'_j` `(8.8.2, (i))`. One is therefore indeed reduced to proving the
proposition when `Y = Spec(A)`, `A` being a Noetherian integral local ring. One then knows that there exists a finite
integral `A`-algebra `B`, having the same field of fractions as `A`, such that `A ⊂ B` and `Spec(B)` is geometrically
unibranch (`(0, 23.2.5)` and `(6.15.5)`); as the morphism `Spec(B) → Spec(A)` is surjective, one may evidently replace
`Y` by `Spec(B)` and `X` by `X ⊗_A B` to prove the proposition. Reasoning as at the beginning of reduction III), one may
therefore suppose `A` local, integral and `Y = Spec(A)` geometrically unibranch.

IV) *Reduction to the case where `X` is integral, affine, and `f` quasi-finite, surjective, birational and universally
open.* — Suppose therefore `Y = Spec(A)` integral, local and geometrically unibranch. There then exists an irreducible
subprescheme `X_0` of `X` such that the restriction `f_0 : X_0 → Y` of `f` is a quasi-finite dominant morphism and
`f_0(X_0)` contains the closed point `y` of `Y` `(14.5.9)`; since `Y` is geometrically unibranch, it follows from
`(14.4.1)` that `f_0` is still universally open. As moreover one may suppose `X_0` reduced, hence integral, one sees
that one may, replacing `X` by `X_0`, suppose that `X` is integral and `f` quasi-finite and dominant, and such that
`f(X)` contains `y`; as `f` is open and every open of `Y` containing `y` is equal to `Y`, `f` is surjective.

Let `ξ`, `η` be the generic points of `X` and `Y` respectively; `k(ξ)` is then a finite extension of `K = k(η)`.
Consequently `(4.6.8)`, there is a finite extension `K'` of `K` such that `(Spec(k(ξ) ⊗_K K'))_red` is geometrically
reduced over `K'` and its irreducible components are geometrically irreducible; it follows (`(4.5.9)` and `(4.6.1)`)
that the residue fields of `Spec(k(ξ) ⊗_K K')` are finite, primary and separable extensions of `K'`, hence are equal to
`K'`. Applying again `(0, 23.2.5)` and `(6.15.5)`, there exists a finite integral `A`-algebra `B`, having `K'` for field
of fractions, containing `A` and such that `Spec(B)` is geometrically unibranch; one may therefore again replace `Y` by
`Spec(B)` and `X` by `(X ⊗_A B)_red` to prove the proposition; the reduction III) then allows one to suppose still `A`
local, integral and `Y = Spec(A)` geometrically unibranch, with closed point `y`. Moreover, `f` is then a *quasi-finite,
surjective and universally open* morphism; each of the irreducible components `X_i` of `X` (`1 ≤ i ≤ m`) dominates `Y`
`(1.10.4)` and is birational over `Y`. Let then `x` be a point of `f⁻¹(y)` and let `X_i` be an irreducible component of
`X` containing `x`; let us still denote by `X_i` the reduced (hence integral) subprescheme of `X` having `X_i` as
underlying space, and let `f_i : X_i → Y` be the restriction of `f`. Applying again `(14.4.1)` to the quasi-finite
dominant morphism `f_i`, one sees that `f_i` is universally open; if `U` is an affine open of `X_i` containing `x`,
`f_i(U)` is therefore

<!-- original page 222 -->

open in `Y` and contains `y`, hence is equal to `Y`. One may thus replace `X` by `U` to prove the proposition.

V) *End of the proof.* — We therefore suppose `Y` local, integral and geometrically unibranch, `X` integral and affine,
`f` quasi-finite, surjective, birational and universally open; it follows that `f` is automatically separated. By virtue
of the Main theorem `(8.12.6)`, there exists a factorization `X → Z → Y`, where `j` is an open immersion and `u` a
finite morphism. Replacing moreover `Z` by the closed image of `j` `(I, 9.5.10)`, one may suppose that `Z` is integral;
as `u` is finite and birational and `Y` geometrically unibranch, it follows from `(III, 4.3.5 and 4.3.4)` that `u` (and
consequently `f`) is a *radicial* morphism; as `f` is universally open and surjective, it is therefore a universal
homeomorphism. Consequently `(2.4.5, (ii))` `f` is a finite morphism. But then one answers the conditions of the
statement with `Y'` integral by simply taking `Y' = X` and `g = f`, the `Y'`-section being the diagonal morphism `Δ_f`.
Q.E.D.

This result can be used to develop "descent" criteria for various properties by universally open and surjective
morphisms. We point out in particular the following criterion, due to D. Mumford:

**Corollary (14.5.11).**

<!-- label: IV.14.5.11 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `g : Y' → Y` a morphism
locally of finite type, universally open and surjective; set `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`. Then, for `f`
to be affine, it is necessary and sufficient that `f'` be so.*

One must only prove that the condition is sufficient. The question being local on `Y`, one may suppose `Y` affine, hence
Noetherian. By virtue of `(14.5.10)`, there exists a finite surjective morphism `h : Y_1 → Y` such that, setting
`Y'_1 = Y' ×_Y Y_1`, and `g' = g_{(Y_1)} : Y'_1 → Y_1`, every point of `Y_1` admits an open neighbourhood `U_1` such
that there exists a `U_1`-section of `g'⁻¹(U_1)`. If one sets `X_1 = X ×_Y Y_1`, the canonical projection `p : X_1 → X`
is a finite surjective morphism, hence, if one proves that `X_1` is an affine scheme, it will result first that `X` is
quasi-compact, hence Noetherian, then that `X` is affine by virtue of Chevalley's theorem `(II, 6.7.1)`. It therefore
suffices to prove that the morphism `f_1 = f_{(Y_1)} : X_1 → Y_1` is affine. Now, if one sets

```text
   X'_1 = X_1 ×_{Y_1} Y'_1 = X' ×_Y Y'_1   and   f'_1 = (f_1)_{(Y'_1)},
```

`f'_1` is affine by virtue of the hypothesis. One is therefore reduced to proving the corollary when one replaces `Y`,
`X`, `f` and `Y'` by `Y_1`, `X_1`, `f_1` and `Y'_1`, in other words, it suffices to prove that `f` is affine when one
makes in addition, in the statement of `(14.5.11)`, the hypothesis that every point of `Y` admits an open neighbourhood
`U` such that there exists a `U`-section of `g⁻¹(U)`. The question being local on `Y`, one may even suppose that there
exists a `Y`-section `s` of `Y'`. Now, one has the following elementary lemma (valid in every category admitting fibre
products):

**Lemma (14.5.11.1).**

<!-- label: IV.14.5.11.1 -->

*Let `f : X → S`, `g : Y → S` be two morphisms, `p_1 : X ×_S Y → X`, `p_2 : X ×_S Y → Y` the canonical projections. If
`s : S → Y` is a section of `g`, then `s' = (1, s ∘ f)_S` is a section of `p_1` and `X`, equipped with the morphisms
`f : X → S` and `s' : X → X ×_S Y`, is identified with the product of the `Y`-preschemes `S` and `X ×_S Y` for the
morphisms `s : S → Y` and `p_2 : X ×_S Y → Y`.*

<!-- original page 223 -->

This is a particular case of `(I, 3.3.11)`, where one replaces the diagram by

```text
       X  ─s'─→  X ×_S Y  ─p_1─→  X
       │            │              │
     f │          p_2│            f│
       ↓            ↓              ↓
       S  ──s──→    Y    ──g───→   S
```

Applying this lemma replacing `S`, `Y` by `Y`, `Y'`, one sees that one may write `f = (f')_{(Y)}` for the base change
`s : Y → Y'`, hence `f` is affine since `f'` is. Q.E.D.

A variant of this criterion is the following:

**Corollary (14.5.12).**

<!-- label: IV.14.5.12 -->

*With the notation and general hypotheses of `(14.5.11)`, let `ℒ` be an invertible `𝒪_X`-Module. Suppose that there
exists a closed part `Z` of `X` proper over `Y` `(II, 5.4.10)` and such that the prescheme induced by `X` on the open
set `X − Z` is normal. Then, for `ℒ` to be ample relatively to `f`, it is necessary and sufficient that
`ℒ' = ℒ ⊗_{𝒪_X} 𝒪_{X'}` be ample relatively to `f'`.*

Let us keep the notation of the proof of `(14.5.11)`. Set `ℒ_1 = ℒ ⊗_{𝒪_X} 𝒪_{X_1}`; it will suffice to prove that `ℒ_1`
is ample relatively to `f ∘ p`, by virtue of `(III, 2.6.2)`; but `f ∘ p = h ∘ f_1`, and, taking `(II, 4.6.13, (v))` into
account, it will suffice to prove that `ℒ_1` is ample relatively to `f_1`. The question being local on `Y_1`, one may
again suppose that `g'` admits a section `s`; if `ℒ'_1 = ℒ' ⊗_{𝒪_{X'}} 𝒪_{X'_1}`, one may then write, by virtue of lemma
`(14.5.11.1)`, `ℒ_1 = ℒ'_1 ⊗_{𝒪_{X'_1}} 𝒪_{X_1}` for the base change `s : Y_1 → Y'_1`; the conclusion therefore results
from two applications of `(II, 4.6.13, (iii))`.

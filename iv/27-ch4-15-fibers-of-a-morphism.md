<!-- original page 223 -->

## §15. Study of the fibres of a universally open morphism

### 15.1. Multiplicities of the fibres of a universally open morphism

**Proposition (15.1.1).**

<!-- label: IV.15.1.1 -->

*Let `Y` be an irreducible locally Noetherian prescheme, of generic point `η`, `f : X → Y` a morphism locally of
finite type, `y` a point of `Y`, `ℱ` a coherent `𝒪_X`-Module; one sets `ℱ_y = ℱ ⊗_{𝒪_Y} k(y)` (sheaf of modules on
the fibre `f⁻¹(y)`). Let `z` be the generic point of an irreducible component of `Supp(ℱ_y)`, and let `X_i`
(`1 ≤ i ≤ m`) be those of the reduced closed subpreschemes of `X` whose underlying space is an irreducible component
of `Supp(ℱ)` containing `z`, and such that the restriction `X_i → Y` of `f` is a morphism universally open at the
point `z`; let `z_i` be the generic point of `X_i` (`1 ≤ i ≤ m`). If `λ_x(ℱ_y)` (resp. `λ_t(ℱ_η)`) denotes the
geometric length of `ℱ_y` at a point `x ∈ f⁻¹(y)` (resp. that of `ℱ_η` at a point `t ∈ f⁻¹(η)`) `(4.7.5)`, then one
has*

```text
  (15.1.1.1)             λ_z(ℱ_y) ≥ ∑_{i=1}^{m} λ_{z_i}(ℱ_η).
```

*If moreover one supposes the ring `𝒪_y` regular, then one has*

```text
  (15.1.1.2)             long((ℱ_y)_z) ≥ ∑_{i=1}^{m} long((ℱ_η)_{z_i}).
```

The fibres `f⁻¹(y')` of `f` (for every `y' ∈ Y`) do not change when one replaces `f` by `f_red`; one may therefore
suppose that `X` and `Y` are reduced `(2.4.3, (vi))`, hence `Y` integral; one will set `K = k(η)`. One may in
addition replace `f` by the restriction `Supp(ℱ) → Y` of `f` to the reduced closed subprescheme of `X` having
`Supp(ℱ)` as underlying space, hence restrict to the case where `X = Supp(ℱ)`. Finally, if `y = η`, there is only one
irreducible component `X_i` of `X` containing `z` `(0_I, 2.1.8)` and one has `z_i = z`, which makes `(15.1.1.1)` and
`(15.1.1.2)` trivial (without hypotheses on `f`). One may therefore restrict to the case `y ≠ η`; it then follows
from the hypothesis and from `(1.10.3)` that the `z_i` belong to `f⁻¹(η)`, the right-hand sides of `(15.1.1.1)` and
`(15.1.1.2)` being therefore defined. Let `Z_i` be the reduced closed subprescheme of `f⁻¹(η)` having `X_i ∩ f⁻¹(η)`
as underlying space; one knows `(4.6.6)` that there exists a finite radicial extension `K'` of `K` such that, for
every `i`, the `K'`-prescheme `(Z_i ⊗_K K')_red` is geometrically reduced over `K'`. Moreover, the projection
morphism `f⁻¹(η) ⊗_K K' → f⁻¹(η)` is finite, dominant and radicial `(I, 3.5.7)`, hence is a homeomorphism `(2.4.5)`.
If `ζ_i` is the unique point of `f⁻¹(η) ⊗_K K'` above `z_i`, it follows from `(4.7.9)` and `(4.7.5)` that one has

```text
  (15.1.1.3)             λ_{z_i}(ℱ_η) = λ_{ζ_i}(ℱ_η ⊗_K K').
```

Let `V` be a discrete valuation ring, of fraction field `K'`, dominating `𝒪_y` `(II, 7.1.7)`; set `Y' = Spec(V)`,
`X' = X ×_Y Y'`, `ℱ' = ℱ ⊗_Y Y'`, `f' = f_{(Y')} : X' → Y'`; if `g : Y' → Y` is the structure morphism, `η'` the
generic point of `Y'` and `y'` its closed point, one has `g(y') = y`, `g(η') = η`; the morphism
`Spec(k(y')) → Spec(k(y))` being faithfully flat, the same is true of the projection
`g' : f'⁻¹(y') → f⁻¹(y)` `(2.2.13)`, hence `(2.3.4)` there is a generic point `z'` of an irreducible component of
`f'⁻¹(y')` such that `g'(z') = z`. By construction, one has `k(η') = K'`, hence `f'⁻¹(η') = f⁻¹(η) ⊗_K K'`; on the
other hand, if one sets `X'_i = X_i ×_Y Y'`, the restriction `X'_i → Y'` of `f'` is a morphism universally open at
the point `z'`, hence `(1.10.3)` there exists a point `ζ'_i ∈ f'⁻¹(η')` which is a generization of `z'`, and one may
evidently suppose that `ζ'_i` is a generic point of an irreducible component of `X'_i ∩ f'⁻¹(η')`; as the projection
of `X'_i ∩ f'⁻¹(η')` into `f⁻¹(η)` is `Z_i`, one has `ζ'_i = ζ_i`. By virtue of `(4.7.9)` and `(4.7.5)`, one has

```text
  (15.1.1.4)             λ_{z'}(ℱ'_{y'}) = λ_z(ℱ_y),
```

and it therefore follows from this inequality and from `(15.1.1.3)` that, in order to establish `(15.1.1.1)`, it
suffices to demonstrate the inequality

<!-- original page 224 -->

```text
  (15.1.1.5)             λ_{z'}(ℱ'_{y'}) ≥ ∑_{i=1}^{m} λ_{ζ_i}(ℱ'_{η'}).
```

Consider now the second inequality `(15.1.1.2)`; we shall use the following lemma:

**Lemma (15.1.1.6).**

<!-- label: IV.15.1.1.6 -->

*Let `A` be a regular local ring that is not a field, `K` its fraction field, `k` its residue field. There exists a
discrete valuation ring `V` dominating `A`, having `K` as fraction field and whose residue field is a pure
transcendental extension of `k`.*

Set `S = Spec(A)`, and consider the `S`-scheme `P` obtained by blowing up the closed point `s` of `S` `(II, 8.1.3)`;
if `𝔪` is the maximal ideal of `A`, one has by definition `P = Proj(B)`, where `B` is the graded `A`-algebra
`⊕_{n ≥ 0} 𝔪^n`. If `h : P → S` is the structure morphism, the fibre `h⁻¹(s)` is isomorphic to `Proj(B ⊗_A k)`
`(II, 2.8.10)`, and by definition `B ⊗_A k` is the graded `A`-algebra `⊕_{n ≥ 0} 𝔪^n / 𝔪^{n+1}`; but since `A` is
regular, this algebra is isomorphic to a polynomial algebra `k[t_1, …, t_e]` (`t_i` indeterminates) `(0, 17.1.1)`,
and consequently `h⁻¹(s)` is isomorphic to `P_k^{e-1}`. Let `ζ` be the generic point of `h⁻¹(s)`; if `t_i`
(`1 ≤ i ≤ e`) are the elements of `𝔪` whose classes mod `𝔪²` are the `t_i`, `B_{(t_e)}` is the ring of an affine
open neighbourhood of `ζ` in `P`, and one has `k(ζ) = k(t_1, …, t_{e-1})`; on the other hand, as `A` is integrally
closed, one verifies easily that the same holds for `B` (Bourbaki, _Alg. comm._, chap. V, §1, n° 8, cor. 1 of
prop. 21), hence `B_{(t_e)}` is also integrally closed, and consequently so is the local ring `𝒪_{P,ζ}`. Finally,
since `A = 𝒪_s` is regular, hence a universally catenary ring `(5.6.4)`, one has, by virtue of `(5.6.5)`,
`dim(𝒪_{P,ζ}) = dim(𝒪_s) − (e − 1)`, since `h` is a birational morphism, `dim(h⁻¹(s)) = e − 1`, and the local ring of
the fibre `h⁻¹(s)` at its generic point `ζ` is of dimension `0`. But `dim(𝒪_s) = e`, hence `dim(𝒪_{P,ζ}) = 1`, and
`𝒪_{P,ζ} = V` is a discrete valuation ring, being Noetherian, of dimension `1` and integrally closed `(II, 7.1.6)`;
it evidently answers the question.

This lemma being established, one may resume the reasoning made for the inequality `(15.1.1.1)` with `Y' = Spec(V)`;
this time `k(y')` is a separable extension of `k(y)`, and consequently `(4.7.9)`, one has
`long((ℱ_y)_z) = long((ℱ'_{y'})_{z'})`; as moreover `f'⁻¹(η') = f⁻¹(η)` and `ℱ'_{η'} = ℱ_η`, one is again reduced to
proving the inequality `(15.1.1.5)`. Now, if `t` is a uniformizer of `𝒪_{y'}`, `f'⁻¹(y')` is the closed
subprescheme of `X'` defined by the Ideal `t 𝒪_{X'}`, and one has `𝒪_{y'} = 𝒪'/t 𝒪'`; on the other hand, one verifies
at once `(I, 9.1.12)` that `(ℱ'_{η'})_{z'} = ℱ'_{z'}`; the inequality to be demonstrated `(15.1.1.5)` is then nothing
but a particular case of `(3.4.1.1)`.

**Corollary (15.1.2).**

<!-- label: IV.15.1.2 -->

*The hypotheses being those of `(15.1.1)`, suppose moreover that `λ_z(ℱ_y) = 1` (resp. that `𝒪_y` is regular and
`long((ℱ_y)_z) = 1`). Then there exists at most one irreducible component `X_i` of `Supp(ℱ)` containing `z` and such
that the restriction `X_i → Y` of `f` is universally open at the point `z`. Moreover, if `z_i` is the generic point
of this component, one has `λ_{z_i}(ℱ_η) = 1` (resp. `long((ℱ_η)_{z_i}) = 1`).*

This results at once from `(15.1.1)` on noting that one necessarily has, by definition of `X_i`, `(ℱ_η)_{z_i} ≠ 0`
`(I, 9.1.13)`.

**Corollary (15.1.3).**

<!-- label: IV.15.1.3 -->

*Let `Y` be an irreducible locally Noetherian prescheme with generic point `η`, `f : X → Y` a morphism locally of
finite type, `ℱ` a coherent `𝒪_X`-Module of support `X`, `x` a point of `X`, `y = f(x)`. Suppose that: 1° `x` belongs
to only one irreducible component `Z` of `f⁻¹(y)`; 2° `ℱ_y = ℱ ⊗_{𝒪_Y} k(y)` is geometrically reduced over `k(y)`,
in other words, if `z` is the generic point of `Z`, `λ_z(ℱ_y) = 1` (resp. `𝒪_y` is regular and `long((ℱ_y)_z) = 1`).
Then, there exists at most one irreducible component `X'` of `X` containing `x`, such that
`dim_x(X' ∩ f⁻¹(y)) = dim_x(f⁻¹(y))` and that the restriction `X' → Y` of `f` is universally open at the generic
points of the irreducible components of `X' ∩ f⁻¹(y)` containing `x`. Moreover, if there exists such a component
`X'` and if `z'` is its generic point, one has `λ_{z'}(ℱ_η) = 1` (resp. `long((ℱ_η)_{z'}) = 1`).*

<!-- original page 225 -->

Indeed, an irreducible component `X'` of `X` containing `x` and such that
`dim_x(X' ∩ f⁻¹(y)) = dim_x(f⁻¹(y))` necessarily contains `Z`, since an irreducible component of `X' ∩ f⁻¹(y)`
containing `x` must be of the same dimension as the unique irreducible component `Z` of `f⁻¹(y)` containing `x`. One
may then apply `(15.1.2)` to `z`.

**Remarks (15.1.4).**

<!-- label: IV.15.1.4 -->

*(i)* In the statement of `(15.1.1)`, one cannot replace "universally open" by "equidimensional", as is shown by the
example `(14.4.10, (ii))` where one takes `ℱ = 𝒪_X`; the fibres of `f` are then reduced Artinian schemes, hence (with
the notation introduced *loc. cit.*) one has `λ_{ζ}(ℱ_η) = 1`, but there are two irreducible components `X_1`, `X_2`
of `X` containing `x'`, and the right-hand side of `(15.1.1.1)` is therefore equal to `2`, although the restriction
of `f` to each of the components `X_1`, `X_2` is a morphism equidimensional at every point. The same example shows
also that in `(15.1.2)` and `(15.1.3)`, one cannot replace the hypothesis "universally open" by "equidimensional".

*(ii)* It is plausible that for the validity of the inequality `(15.1.1.2)`, one cannot suppress the hypothesis that
`𝒪_y` is regular.

### 15.2. Flatness of universally open morphisms with geometrically reduced fibres

**(15.2.1)**

<!-- label: IV.15.2.1 -->

One has seen `(2.4.6)` that a flat morphism locally of finite presentation is universally open. One has a partial
converse of this result by means of additional hypotheses:

**Theorem (15.2.2).**

<!-- label: IV.15.2.2 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent
`𝒪_X`-Module, `x` a point of `X`, `y = f(x)`. Suppose the following conditions verified:*

*(i) `Supp(ℱ) = X`.*

*(ii) `f` is universally open at the generic points of the irreducible components of `f⁻¹(y)` containing `x`.*

*(iii) `ℱ_y = ℱ ⊗_{𝒪_Y} k(y)` is geometrically reduced at the point `x` `(4.6.22)`.*

*(iv) The ring `𝒪_y` is reduced.*

*Then `ℱ` is `f`-flat at the point `x`.*

Since `𝒪_y` is reduced and Noetherian, we shall apply the valuative criterion of flatness `(11.8.1)`. Consider then
a local homomorphism `𝒪_y → A'`, where `A'` is a discrete valuation ring; set `Y' = Spec(A')`, `X' = X ×_Y Y'`,
`f' = f_{(Y')} : X' → Y'`, and let `x'` be a point of `X'` whose projections in `X` and `Y'` are respectively `x`
and the closed point `y'` of `Y'`; if one sets `ℱ' = ℱ ⊗_Y Y'`, one has `Supp(ℱ') = X'` by `(I, 9.1.13)`; every
generic point `z'` of an irreducible component of `f'⁻¹(y')` containing `x'` has as projection in `f⁻¹(y)` a generic
point `z` of an irreducible component of `f⁻¹(y)` containing `x`, by virtue of `(4.2.6)`; hence `f'` is universally
open at the point `z'`. Finally, it follows from `(4.7.11)` that `ℱ'_{y'}` is geometrically reduced at the point
`x'`. One sees therefore that one is reduced to demonstrating the

**Lemma (15.2.2.1).**

<!-- label: IV.15.2.2.1 -->

*Let `Y = Spec(A)` be the spectrum of a discrete valuation ring, `y` its closed point, `f : X → Y` a morphism
locally of finite type, `x` a point of `f⁻¹(y)`, `ℱ` a coherent `𝒪_X`-Module. Suppose the following conditions
verified:*

*(i) `Supp(ℱ) = X`.*

*(ii) `f` is open at the generic points of the irreducible components of `f⁻¹(y)` containing `x`.*

*(iii) `ℱ_y = ℱ ⊗_{𝒪_Y} k(y)` is reduced at the point `x` `(3.2.2)`.*

*Then `ℱ` is `f`-flat at the point `x`.*

Designate then by `t` a uniformizer of `A`, set `B = 𝒪_x` and `ℱ_x = M`; condition (i) implies that
`Supp(M) = Spec(B)` `(I, 9.1.13)`. Condition (ii) implies, by virtue of `(14.3.2)`, that every irreducible component
of `X` containing `x` dominates `Y`; in other words, the inverse image in `A` of every minimal prime ideal `𝔭_i` of
`B` is `0`, which means again that one has `t ∉ 𝔭_i` for every `i`. Finally, (iii) means that `M/tM` is a reduced
`(B/tB)`-module `(3.2.2)`. It is a question of showing that under these conditions `M` is a torsion-free `A`-module
`(0_I, 6.3.4)`, and for this it suffices evidently to show that `t` is an `M`-regular element; but this results from
`(3.4.6.1)`.

**Corollary (15.2.3).**

<!-- label: IV.15.2.3 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `x` a point of `X`,
`y = f(x)`. Suppose the following conditions verified:*

*(i) `f` is universally open at the generic points of the irreducible components of `f⁻¹(y)` containing `x`.*

*(ii) `f⁻¹(y)` is geometrically reduced (over `k(y)`) at the point `x` `(4.6.9)`.*

*(iii) The ring `𝒪_y` is reduced.*

*Under these conditions `f` is flat at the point `x`.*

It suffices to apply `(15.2.2)` to `ℱ = 𝒪_X` `(4.6.22)`.

<!-- original page 226 -->

**Remarks (15.2.4).**

<!-- label: IV.15.2.4 -->

*(i)* The first three of the conditions of `(15.2.2)` do not change when one replaces `f` by `f_red`; but if `𝔑` is
the nilradical of a Noetherian local ring `A`, `A/𝔑` is flat over `A/𝔑` but not over `A` itself when `𝔑 ≠ 0`
(Bourbaki, _Alg. comm._, chap. II, §3, n° 2, cor. 2 of prop. 5). One sees therefore that one cannot in `(15.2.2)`
suppress condition (iv).

*(ii)* It follows from `(2.4.6)` that if the conclusion of `(15.2.2)` is true, as well as hypothesis (i), `f` is
universally open in a neighbourhood of `x`, and in particular at the generic points of the irreducible components of
`f⁻¹(y)` containing `x`. Even when (i), (iii) and (iv) are verified, one cannot replace (ii) by the weaker
hypothesis that `f` is universally open at the point `x` only. This is what is shown by the example
`(14.1.3, (i))`, where `f` is evidently universally open at every point of `X_2`, hence in particular at the point
`x`, intersection of `X_1` and `X_2`; conditions (ii) and (iii) of `(15.2.3)` are also verified by this example.
Nevertheless, `𝒪_x` is not a torsion-free `𝒪_y`-module, `𝒪_y` being identified with a subring of `𝒪_x` that
contains zero-divisors in `𝒪_x`; hence `f` is not flat at the point `x`.

*(iii)* In `(15.2.3)`, the conclusion is no longer necessarily valid when one replaces hypothesis (ii) by the weaker
hypothesis that `f⁻¹(y)`, considered as a `k(y)`-prescheme, has no embedded associated prime cycles. An example is
furnished by taking for `Y` a curve having a cusp at a point `y`, for example
`Y = Spec(K[S, T]/(S³ − T²))`, `K` being an algebraically closed field, and for `X` its normalization `(II, 6.3.8)`.
If `s` and `t` are the classes of `S` and `T` in `A = K[S, T]/(S³ − T²)`, one verifies at once that
`X = Spec(B)`, where `B = K[s, t, u]`, `u` being the element `t/s` of the fraction field of `A`, and as `s = u²`,
`t = u³`, one has also `B = K[u]`, isomorphic to the polynomial ring in one indeterminate over `K`. The only point
`x` of `X` above the point `y` corresponding to the maximal ideal `(s) + (t)` corresponds to the maximal ideal `(u)`;
but as the class `ū` of `u` in `𝒪_x / 𝔪_y 𝒪_x` is such that `ū² = 0`, `f⁻¹(y)` is not a reduced `k(y)`-prescheme.
Here `f` is a finite, surjective and radicial morphism, hence a universal homeomorphism `(2.4.5)`, but is not flat at
the point `x`, for if `𝒪_x` were a flat `𝒪_y`-module, it would be a free `𝒪_y`-module of rank `1` generated by the
element `1` of `𝒪_x` (Bourbaki, _Alg. comm._, chap. II, §3, n° 2, prop. 5), which is absurd.

*(iv)* Let us show finally that in `(15.2.2)` or `(15.2.3)`, one cannot replace "geometrically reduced" by "reduced".
We shall in fact define two rings `A`, `A'` having the following properties:

1) `A` is a Noetherian local ring of maximal ideal `𝔪`, integral, complete, of dimension `1` and geometrically
   unibranch.

2) `A'` is the integral closure of `A`, a finite `A`-algebra whose maximal ideal is `𝔪 A'`, and the residue field
   `k'` a finite radicial non-trivial extension of the residue field `k = A/𝔪` of `A`.

One may then take `Y = Spec(A)`, `X = Spec(A')`, `y = 𝒪_y`, `y` and `x` being the closed points of `Y` and `X`
respectively; hypotheses (i) and (iv) of `(15.2.2)` are trivially verified; as `A` is of dimension `1`,
`f : X → Y` is radicial, finite and surjective, hence a universal homeomorphism `(2.4.5)`, which proves hypothesis
(i) of `(15.2.3)`. Finally, it is clear that `f⁻¹(y)` is reduced. Nevertheless `f` is not flat at the point `x`, for
if `A'` were a flat `A`-module, it would be a free `A`-module of rank `1` (since it has the same fraction field as
`A`) generated by the element `1` of `A` (Bourbaki, _Alg. comm._, chap. II, §3, n° 2, prop. 5), which is absurd.

To construct the rings `A` and `A'`, start from an imperfect field `k` of characteristic `p > 0`; let
`K_0 = k((T))` be the field of formal power series over `k`, `A_0` the valuation ring for `K_0` corresponding to the
discrete valuation equal to the *order* of the formal series; the residue field of `A_0` is therefore `k`. Let `α`
be an element of `k` which is not a `p`-th power, and take `k' = k(α^{1/p})`; `K = k'((T))` is then a finite radicial
extension of `K_0`, and `A' = A_0 ⊗_k k'` the discrete valuation ring for `K` corresponding to the order of formal
series over `K`. If `𝔪'` is the maximal ideal of `A'`, one will answer conditions 1) and 2) by taking
`A = A_0 + 𝔪'`: indeed, as `A_0` is Noetherian and `A'` an `A_0`-module of finite type, `A` is a finite
`A_0`-algebra, hence a Noetherian ring; as `A'` is finite over `A`, `𝔪'` is the only maximal ideal of `A`, which is
therefore a complete local ring, evidently of dimension `1` (being finite over `A_0`) and geometrically unibranch
since `A'` is integrally closed and has the same fraction field `K` as `A`.

*(v)* The proof of `(15.2.2)` shows nevertheless that one may weaken condition (iii) by replacing in it
"geometrically reduced" by "reduced" when one can apply the valuative criterion of flatness `(11.8.1)` using only
discrete valuation rings `A'` whose residue field `k'` is separable over `k(y)`; indeed, if `x'` and `z'` have the
same significations as in `(15.2.2)`, the radicial multiplicities `μ_r(k(x') | k')` and `μ_r(k(z) | k(y))` are the
same, by virtue of `(4.7.3)`, hence it follows from `(4.7.9)` that `long((ℱ_y)_z)` and `long((ℱ'_{y'})_{z'})` are
equal, and one is again reduced to the case where `Y` is the spectrum of a discrete valuation ring and `y` its
closed point. For example, one will be able to obtain this stronger result when `𝒪_y` is unibranch and dominated by
a discrete valuation ring whose residue field is a separable extension of `k(y)`, by virtue of `(11.6.4)`. This is
the case when `𝒪_y` is a regular ring, after `(15.1.1.6)`. But, as Hironaka has pointed out to us, there exist
integrally closed Noetherian local rings of dimension `2` (coming from algebraic schemes over imperfect fields)
which do not satisfy the preceding condition.

### 15.3. Applications: criteria of reduction and of irreducibility

**Proposition (15.3.1).**

<!-- label: IV.15.3.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent
`𝒪_X`-Module, `x` a point of `X`, `y = f(x)`. Suppose conditions (i), (ii) and (iii) of `(15.2.2)` verified. Then:*

*(i) There exists a neighbourhood `U` of `x` in `X` such that `f | U` be universally open and that, for every
`x' ∈ U`, `ℱ_{x'}` be geometrically reduced over `k(f(x'))` at the point `x'`.*

*(ii) If moreover `Y` is reduced at the point `y`, there exists a neighbourhood `U_1 ⊂ U` of `x` such that
`ℱ | U_1` be `f`-flat and reduced.*

<!-- original page 227 -->

Taking into account `(I, 5.1.8)`, `(4.2.7)` and `(4.7.11)`, the hypotheses do not change, nor the conclusion (i) of
the statement, if one replaces `Y` by `Y_red` and `X` by `X ×_Y Y_red`, and one may therefore suppose `Y` reduced. It
then follows from `(15.2.2)` that `ℱ` is `f`-flat at the point `x`, hence also `(11.1.1)` in a neighbourhood of `x`,
and a fortiori `f` is universally open in this neighbourhood `(2.4.6)`. The fact that `ℱ_{x'}` is then geometrically
reduced at the point `x'` for all points of a neighbourhood of `x` follows from `(12.1.1, (vii))`. Assertion (ii)
therefore follows from what precedes and from `(3.3.4)`.

**Proposition (15.3.2).**

<!-- label: IV.15.3.2 -->

*The notation being that of `(15.3.1)`, suppose that conditions (i), (ii), (iii) of `(15.2.2)` are verified, and
moreover that `f⁻¹(y)` is equidimensional at the point `x`. Then `f` is equidimensional at the point `x`.*

One has, for every `y' ∈ Y`, `Supp(ℱ_{y'}) = f⁻¹(y')`. By hypothesis `ℱ_y` is reduced (hence satisfies `(S_1)`) and
is equidimensional at the point `x`. By virtue of `(12.1.1, (ii))`, one may therefore suppose that `ℱ_{y'}` is
equidimensional and of constant dimension `e = dim_x(f⁻¹(y))` at the point `x'` for all `x' ∈ U`, which means that
`f⁻¹(f(x'))` is equidimensional and of dimension `e` at the point `x'`. As moreover `ℱ | U` is `f`-flat, it follows
from `(2.3.4)` and from `(13.3.1, a))` that `f` is equidimensional at the point `x`.

**Corollary (15.3.3).**

<!-- label: IV.15.3.3 -->

*The notation being that of `(15.3.1)`, suppose the following conditions verified:*

*(i) `Supp(ℱ) = X`.*

*(ii) `f` is universally open at the generic points of the irreducible components of `f⁻¹(y)` containing `x`.*

*(iii) `ℱ_y` is geometrically pointwise integral over `k(y)` at the point `x` `(4.6.22)`.*

*(iv) `Y` is geometrically unibranch at the point `y`.*

*Then `x` belongs to only one irreducible component of `X`.*

*If moreover `Y` is integral at the point `y` and `ℱ = 𝒪_X`, then `X` is integral at the point `x` and `f` is flat
at the point `x`.*

Note first that (i) and (iii) entail that `x` belongs to only one irreducible component `Z` of `f⁻¹(y)`. It follows
therefore from `(14.4.7)` and from `(15.3.2)` that for every irreducible component `X_i` of `X` containing `x`
(hence `Z`), the restriction `f_i` of `f` to `X_i` is a morphism equidimensional at the point `x`, and universally
open at the generic point of `Z`. The first assertion of the statement then follows from `(15.1.3)` and the second
from `(15.3.1)`.

**Remarks (15.3.4).**

<!-- label: IV.15.3.4 -->

*(i)* The example `(14.4.10, (ii))` shows that, in `(15.3.3)`, one cannot suppress the hypothesis that `Y` is
geometrically unibranch at the point `y`.

*(ii)* The remark `(15.2.4, (v))` shows that the conclusion of `(15.3.3)` is still valid under the following
hypotheses: `𝒪_y` is regular, `Supp(ℱ) = X` and `ℱ_y` is integral at the point `x`. We do not know whether in this
statement, one may replace the hypothesis that `𝒪_y` is regular by the hypothesis that it is geometrically
unibranch, or even integral and integrally closed.

### 15.4. Complements on Cohen-Macaulay morphisms

**Proposition (15.4.1).**

<!-- label: IV.15.4.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent
`𝒪_X`-Module such that `Supp(ℱ) = X`, `x` a point of `X`, `y = f(x)`. One sets, for every `x' ∈ X`,
`X_{f(x')} = f⁻¹(f(x'))`, `ℱ_{f(x')} = ℱ ⊗_{𝒪_Y} k(f(x'))`. Suppose that `ℱ` is `f`-flat at the point `x` and that
`ℱ_y` is a Cohen-Macaulay `𝒪_{X_y}`-Module at the point `x`. Then `f` is equidimensional at the point `x`.*

<!-- original page 228 -->

Indeed (`(11.1.1)` and `(12.1.1, (vi))`), there exists a neighbourhood `U` of `x` such that `ℱ | U` be `f`-flat and
that for every `x' ∈ U`, `ℱ_{f(x')}` be a Cohen-Macaulay `𝒪_{X_{f(x')}}`-Module at the point `x'`; this latter
property entails that `ℱ_{f(x')}` is equidimensional at the point `x'` and that `x'` belongs to no embedded
associated prime cycle associated with `ℱ_{f(x')}` `(0_IV, 16.5.4)`. Moreover, by virtue of `(12.1.1, (ii))`, one
may suppose that the dimensions of the irreducible components of `Supp(ℱ_{f(x')} | (U ∩ X_{f(x')}))` have a (same)
value independent of `x'`. As `Supp(ℱ_{f(x')}) = X_{f(x')}` by hypothesis, it follows from `(2.3.4)` and from
`(13.3.1, a))` that `f` is equidimensional at the point `x`.

**Proposition (15.4.2).**

<!-- label: IV.15.4.2 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `ℱ` a coherent
`𝒪_X`-Module such that `Supp(ℱ) = X`, `x` a point of `X`, `y = f(x)`. Suppose that `𝒪_y` is regular and that `ℱ` is
a Cohen-Macaulay `𝒪_X`-Module at the point `x`. Then (with the notation of `(15.4.1)`) the following conditions are
equivalent:*

*a) `ℱ` is `f`-flat at the point `x` and `ℱ_y` is a Cohen-Macaulay `𝒪_{X_y}`-Module at the point `x`.*

*b) `ℱ` is `f`-flat at the point `x`.*

*c) `f` is universally open in a neighbourhood of `x`.*

*d) `f` is open at the generic points of the irreducible components of `X_y` containing `x`.*

*e) `dim(𝒪_{X_y, x}) = dim(𝒪_x) − dim(𝒪_y)`.*

*e') `dim_x(ℱ_y) = dim_x(ℱ) − dim(𝒪_y)`.*

Since `Supp(ℱ) = X`, conditions e) and e') are equivalent by definition `(5.1.12)`. Condition a) implies trivially
b); b) entails that `ℱ` is `f`-flat at the points of a neighbourhood of `x` `(11.1.1)`, hence b) entails c)
`(2.4.6)`; c) entails trivially d), and d) entails e') by `(14.2.1)`. Finally, since `𝒪_y` is regular and `ℱ_x` is
a Cohen-Macaulay `𝒪_x`-module, it follows from `(6.1.4)` that e) entails a).

**Proposition (15.4.3).**

<!-- label: IV.15.4.3 -->

*Let `f : X → Y` be a morphism locally of finite presentation, `ℱ` an `𝒪_X`-Module of finite presentation, such that
`Supp(ℱ) = X`, `x` a point of `X`, `y = f(x)`. Then (with the notation of `(15.4.1)`) the following conditions are
equivalent:*

*a) `ℱ` is `f`-flat at the point `x` and `ℱ_y` is a Cohen-Macaulay `𝒪_{X_y}`-Module at the point `x`.*

*b) There exists an open neighbourhood `U` of `x` in `X`, and a `Y`-morphism quasi-finite
`g : U → Y' = Y[T_1, …, T_m]` (`T_i` indeterminates), such that `ℱ | U` be `g`-flat at the point `x`.*

Let us first show that b) entails a). Set `h : Y' → Y`; the `k(y)`-prescheme `Y'_y = h⁻¹(y)` is regular
`(0, 17.3.7)`; let `A` be the local ring of this prescheme at the point `y' = g(x)`, `k` its residue field, and
let `B` be the local ring of `X_y` at the point `x`; set on the other hand `(ℱ_y)_x = M`, which is a `B`-module of
finite type. The hypothesis that the morphism `g` is quasi-finite entails that the same holds for
`g_y : X_y → Y'_y` `(II, 6.2.4)`, hence `M ⊗_A k` is a `(B ⊗_A k)`-module of finite length `(II, 6.2.2)`; as by
hypothesis `M` is a flat `A`-module and `A` a Cohen-Macaulay ring, `M` is a Cohen-Macaulay `B`-module `(6.3.3)`. The
fact that `ℱ` is `f`-flat at the point `x` follows from the fact that it is `g`-flat and from the fact that the
morphism `h` is flat `(2.1.6)`.

Let us now show that a) entails b). The question being local on `X` and `Y`, one may suppose `X` and `Y` affine;
using `(8.9.1)` and `(11.2.7)`, one reduces to the case where `X` and `Y` are Noetherian, taking `(6.7.1)` into
account. The hypothesis entails that `f` is

<!-- original page 229 -->

equidimensional at the point `x` `(15.4.1)`, whence the existence of a quasi-finite morphism
`g : U → Y'` such that every irreducible component of `U` dominates `Y'` `(13.3.1, b))` and that `g_y : U_y → Y'_y`
be finite and surjective `(13.3.1.1)`. On the other hand, in order to prove that `ℱ | U` is `g`-flat at the point
`x`, it suffices, since `h : Y' → Y` is flat, to show (by virtue of the fibrewise flatness criterion `(11.3.10)`)
that `ℱ_y` is `g_y`-flat at the point `x`. But by hypothesis `ℱ_y` is a Cohen-Macaulay `𝒪_{X_y}`-Module at the point
`x` and `Y'_y` a regular prescheme; on the other hand, as `g_y` is finite and surjective, it satisfies condition
e') of `(15.4.2)` by virtue of `(5.6.10)`; it therefore suffices to conclude to apply `(15.4.2)` to `g_y` and to
`ℱ_y`.

### 15.5. Separable rank of the fibres of a quasi-finite and universally open morphism. Application to the geometric connected components of the fibres of a proper morphism

**Proposition (15.5.1).**

<!-- label: IV.15.5.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a separated and quasi-finite morphism. For every `z ∈ Y`,
let `n(z)` be the geometric number of points of `f⁻¹(z)` (or separable rank of `f⁻¹(z)` over `k(z)`; cf.
`(I, 6.4.8)`). One has the following properties:*

*(i) The function `z ↦ n(z)` is lower semi-continuous at every point `y ∈ Y` such that `f` is universally open at
the points of `f⁻¹(y)`.*

*(ii) Let `y` be a point of `Y` such that `f` is universally open at the points of `f⁻¹(y)`; if the function
`z ↦ n(z)` is constant in a neighbourhood of `y`, then `f` is proper at the point `y` `(15.7.1)`.*

*(iii) Suppose that `f` is universally open and that every point of `Y` is geometrically unibranch; then, if the
function `z ↦ n(z)` is locally constant in `Y`, the irreducible components of `X` are pairwise disjoint.*

(i) Note that since `f` is quasi-finite, the number `n(z)` is the geometric number of connected components of
`f⁻¹(z)`; one knows that the function `z ↦ n(z)` is locally constructible `(9.7.9)`; taking `(0_III, 9.3.4)` into
account, one is reduced to proving the

**Corollary (15.5.2).**

<!-- label: IV.15.5.2 -->

*Under the general hypotheses of `(15.5.1)`, let `y` be a point of `Y` such that `f` is universally open at the
points of `f⁻¹(y)`. Then, if `y'` is a generization of `y`, one has*

```text
  (15.5.2.1)             n(y') ≥ n(y).
```

For every base change `g : Z → Y`, `f_{(Z)} : X_{(Z)} → Z` is separated, quasi-finite and universally open at the
points of `X_{(Z)}` projecting into `f⁻¹(y)`; moreover, if `z`, `z'` are two points of `Z` such that `g(z) = y`,
`g(z') = y'` and that `z'` is a generization of `z`, one has `n(z) = n(y)` and `n(z') = n(y')` `(I, 6.4.12)`; it
therefore suffices to demonstrate `(15.5.2.1)` for a suitable `g`. One may evidently suppose `y ≠ y'`. We shall use
the following lemma:

**Lemma (15.5.2.2).**

<!-- label: IV.15.5.2.2 -->

*Under the general hypotheses of `(15.5.1)`, if `y` is a point of `Y`, `y'` a generization of `y` distinct from `y`,
there exists a spectrum of a discrete valuation ring `Z`, of closed point `z` and of generic point `z'`, and a
morphism `g : Z → Y` such that: 1° `g(z) = y`, `g(z') = y'`; 2° if one sets `f' = f_{(Z)}`, `n(y)` is the number of
points of `f'⁻¹(z)` and `n(y')` is the number of points of `f'⁻¹(z')`.*

Indeed, there exists a discrete valuation ring `A_1` and a morphism `g_1` of `Z_1 = Spec(A_1)` into `Y` such that
if `z_1` and `z'_1` are the closed point and the generic point of `Z_1`,

<!-- original page 230 -->

one has `g_1(z_1) = y` and `g_1(z'_1) = y'` `(II, 7.1.9)`; one may therefore already suppose that `Y` is the spectrum
of a discrete valuation ring `A`, `y` its closed point and `y'` its generic point. For every `x ∈ f⁻¹(y)`, `k(x)`
is a finite extension of `k(y)` by hypothesis `(II, 6.2.2)`; one deduces from `(4.5.11)` that there exists a finite
algebraic extension `k` of `k(y)` such that the number of points of `f⁻¹(y) ⊗_{k(y)} k` be equal to `n(y)`. As there
is a discrete valuation ring `A_2` dominating `A` and whose residue field is finite over `k(y)` and contains `k`
`(II, 7.1.2)`, one may in the second place suppose that `n(y)` is the number of points of `f⁻¹(y)`. Finally, the
same reasoning shows that there is a finite extension `K` of `k(y')` such that the number of points of
`f⁻¹(y') ⊗_{k(y')} K` be equal to `n(y')`; if `w` is a valuation of `k(y')` associated with `A`, there is a discrete
valuation of `K` extending `w`, and the ring `A_3` of this valuation dominates `A`, has `K` as fraction field, and
answers the conditions of the lemma.

One may therefore henceforth suppose that `Y` is the spectrum of a discrete valuation ring, `y` its closed point,
`y'` its generic point, and that `n(y)` and `n(y')` are the numbers of points of `f⁻¹(y)` and `f⁻¹(y')`, so that for
every `x ∈ f⁻¹(y)` (resp. every `x' ∈ f⁻¹(y')`) one has `k(x) = k(y)` (resp. `k(x') = k(y')`).

Designate then by `X_i` the reduced subpreschemes of `X` having as underlying spaces the irreducible components of
`X` (`1 ≤ i ≤ m`). By virtue of `(1.10.4)`, the restriction `X_i → Y` of `f` to every `X_i` is a dominant morphism,
and as `f⁻¹(y')` is discrete, each of the intersections `X_i ∩ f⁻¹(y')` reduces to the generic point of `X_i`,
whence (denoting by `n_i(z)` the geometric number of points of `X_i ∩ f⁻¹(z)` for every `z ∈ Y`), `n_i(y') = 1` for
every `i`, and `n(y') = ∑_i n_i(y') = m`. On the other hand, `f⁻¹(y)` is the union of the `X_i ∩ f⁻¹(y)`, whence

```text
  (15.5.2.3)             n(y) ≤ ∑_i n_i(y),
```

and to prove `(15.5.2.1)`, it suffices to establish that `n_i(y) ≤ 1` for every `i`. In other words, one may suppose
`X` integral, and the morphism `f` birational. But then, for every `x ∈ f⁻¹(y)`, one has `𝒪_y ⊂ 𝒪_x ⊂ K`, where
`K = k(y')` is the fraction field of `𝒪_y`. As `𝒪_y` is a valuation ring and `𝒪_x` dominates `𝒪_y`, one necessarily
has `𝒪_y = 𝒪_x` `(II, 7.1.1)`. There exists then a `Y`-section `h : Y → X` such that `h(y) = x` `(I, 2.4.4)`; as `Y`
is reduced and `X` is separated over `Y`, such a section is unique `(I, 7.2.2)`, hence the set `f⁻¹(y)` contains
only a single point, which finishes proving (i).

(ii) As at the beginning of (i), one is reduced to showing that if the two sides of `(15.5.2.1)` are equal for every
generization `y'` of `y`, `f` is proper at the point `y`. Thanks to the criterion of local properness `(15.7.5)` and
the remarks at the beginning one may again suppose that `Y = Spec(A)` is the spectrum of a discrete valuation ring
`A`, `y` its closed point and `y'` its generic point, and it is then a question of showing that `f` is proper.

Using `(15.5.2.2)` and noting that if `A'` is a discrete valuation ring dominating `A`, `A'` is a torsion-free
`A`-module, hence the morphism `Spec(A') → Spec(A)` is faithfully flat and quasi-compact, it amounts to the same to
say that `f` is proper or that the morphism deduced from `f` by the base change `Spec(A') → Spec(A)` is proper

<!-- original page 231 -->

`(2.7.1, (vii))`; one may therefore suppose that `n(y)` and `n(y')` are the numbers of points of the fibres
`f⁻¹(y)` and `f⁻¹(y')` respectively. With the notation of (i), one then has by `(15.5.2.3)` and `(15.5.2.1)`

```text
  (15.5.2.4)             n(y) ≤ ∑_i n_i(y) ≤ ∑_i n_i(y') = n(y'),
```

and for the extreme terms to be equal, it is necessary that `n_i(y) = n_i(y') = 1` for every `i`. As one has seen
in (i), if `n_i(y) = 1` for every `i`, `X_i ∩ f⁻¹(y)` is non-empty and the restriction `X_i → Y` of `f` is an
isomorphism; as the `X_i` are closed subpreschemes of `X`, this entails that `f` is proper `(II, 5.4.5)`.

(iii) One may restrict to the case where `Y` is affine and reduced, and as `Y` is by hypothesis locally integral
`(I, 5.1.4)`, one may suppose `Y` integral, and the function `y ↦ n(y)` constant in `Y`. Let again `X_i`
(`1 ≤ i ≤ m`) be the irreducible components of `X`. It follows from `(1.10.4)` that if `y'` is the generic point
of `Y`, each of the `X_i ∩ f⁻¹(y')` reduces to a single point; the restriction `f_i : X_i → Y` of `f` being a
quasi-finite and dominant morphism and every point of `Y` being geometrically unibranch, it follows from
Chevalley's criterion `(14.4.4)` that `f_i` is universally open. If then `y` is any point of `Y`, one has
`n_i(y) ≥ n_i(y')`; on the other hand, as the `X_i ∩ f⁻¹(y')` are pairwise disjoint,
`∑_i n_i(y') = n(y')`; one therefore has again the relations `(15.5.2.4)`. But by hypothesis the extreme terms are
equal, hence `n(y) = ∑_i n_i(y)`, which implies that the `X_i ∩ f⁻¹(y)` are pairwise disjoint, and finishes the
demonstration.

Combining this proposition with Zariski's connectedness theorem and its consequences `(III, 4.3)`, one obtains the
following results which complete `(III, 4.3.7 and 4.3.10)`:

**Proposition (15.5.3).**

<!-- label: IV.15.5.3 -->

*Let `Y` be an irreducible locally Noetherian prescheme, `f : X → Y` a proper morphism; for every `y ∈ Y`, let
`n(y)` be the geometric number of connected components `(4.5.2)` of `f⁻¹(y)`. Suppose that the restriction of `f`
to every irreducible component of `X` is a morphism dominant in `Y`. Then, if `y_0` is a geometrically unibranch
point of `Y`, the function `y ↦ n(y)` is lower semi-continuous at the point `y_0`.*

Consider the Stein factorization `f = g ∘ f'` of `f` `(III, 4.3.3)`, where `g : Y' → Y` is a finite morphism and
`f' : X → Y'` a surjective morphism whose fibres are geometrically connected `(III, 4.3.4)`. Since `f'` is
surjective, the inverse image under `f'` of every irreducible component of `Y'` contains an irreducible component of
`X` at least; hence each of the irreducible components of `Y'` dominates `Y`. One may therefore apply Chevalley's
criterion `(14.4.4)` to the restrictions of `g` to each of these irreducible components, and one concludes that `g`
is universally open at every point of `g⁻¹(y_0)`. The conclusion therefore follows from `(15.5.2)` and from the fact
that the geometric number of connected components of `f⁻¹(y)` is equal to the geometric number of points of
`g⁻¹(y)` `(III, 4.3.4)`.

**Corollary (15.5.4).**

<!-- label: IV.15.5.4 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism; let `y` be a point of `Y` such that `f`
be universally open at the points of `f⁻¹(y)`;

<!-- original page 232 -->

then, with the notation of `(15.5.3)`, the function `z ↦ n(z)` is lower semi-continuous at the point `y`.*

With the notation of `(15.5.3)`, note that in the Stein factorization `f = g ∘ f'`, `f'` is surjective; as `f` is
universally open at the points of `f⁻¹(y)`, `g` is universally open at the points of `g⁻¹(y)` `(14.3.4, (i))`; it
then suffices to apply to `g` proposition `(15.5.1, (i))` taking `(III, 4.3.4)` into account.

**Remarks (15.5.5).**

<!-- label: IV.15.5.5 -->

*(i)* Even if `Y` is integral and normal, `X` integral, `f` finite and surjective (hence universally open by virtue
of Chevalley's criterion `(14.4.4)`), the function `y ↦ n(y)` is not necessarily locally constant. One has an example
of this by taking `Y = Spec(k[T])` where `k` is algebraically closed, and `X = Spec(A)`, where
`A = k[S, T]/(S² + T² − 1)`; at the points `y'`, `y''` of `Y` corresponding to the maximal ideals `(T − 1)` and
`(T + 1)`, one has `n(y') = n(y'') = 1`, but `n(y) = 2` at all the other points of `Y`. We shall give below an
additional condition assuring that `y ↦ n(y)` is locally constant `(15.5.7)`.

*(ii)* The example `(14.4.10, (ii))` shows that in `(15.5.1, (iii))`, one cannot suppress the hypothesis that the
points of `Y` are geometrically unibranch.

*(iii)* The example `(11.7.5)` shows that the conclusion of `(15.5.1, (i))` is no longer valid if one supposes only
that the morphism `f` is open (even if, as is the case in the example cited, `f` is finite and surjective).

*(iv)* Finally, in `(15.5.1)`, one cannot dispense with the hypothesis that the morphism `f` is separated, as is
shown by the example where `X` is the affine line of which one has "doubled a point" `(I, 5.5.11)`, and `Y` the
affine line: here `f` is a local isomorphism (hence is flat) and is quasi-finite, but `z ↦ n(z)` is not lower
semi-continuous.

**Lemma (15.5.6).**

<!-- label: IV.15.5.6 -->

*Let `Y` be the spectrum of a discrete valuation ring, `a` its closed point, `b` its generic point. Let
`f : X → Y` be a morphism locally of finite type and open. Suppose that `X` is connected and that the fibre
`f⁻¹(a)` is a reduced prescheme. Then `f⁻¹(b)` is connected.*

We shall use the following purely topological lemma (particular case of a more general result of chap. III, 3rd
Part):

**Lemma (15.5.6.1).**

<!-- label: IV.15.5.6.1 -->

*Let `X` be a locally Noetherian space, every closed irreducible part of which admits a generic point. Let `Z` be
a rare closed part of `X` having the following property: for every `x ∈ Z`, if one designates by `T_x` the set of
generizations of `x` in `X`, then `T_x − {x}` is connected. Under these conditions, if `X` is connected, `X − Z` is
connected.*

Let us give an independent demonstration. Reasoning by contradiction, suppose that the open set `U = X − Z`,
everywhere dense in `X`, is the union of two non-empty open sets with no common point `U'`, `U''`, and designate by
`X'` and `X''` the closures in `X` of `U'` and `U''`. As `X = U ⊂ X' ∪ X''` and `X` is connected, one has
`X' ∩ X'' ≠ ∅`, and it is clear that `X' ∩ X'' ⊂ Z`. Let `x` be a generic point of an irreducible component of
`X' ∩ X''`. As `X` is locally Noetherian, there is an open neighbourhood `V` of `x` in `X` such that `V ∩ U'` and
`V ∩ U''` have only a finite number of irreducible components; as `x` is adherent to `U'` and to `U''`, it is
necessarily in the closure of an irreducible component `Z'` of `V ∩ U'` and in the closure of an irreducible
component `Z''` of `V ∩ U''`. But `Z'` (resp. `Z''`) is closed and irreducible in `X`, hence admits a generic point
`z'` (resp. `z''`), and one necessarily has `z' ∈ U'` and `z'' ∈ U''`. This proves that the intersections of
`T_x − {x}` with `U'` and `U''` are non-empty. But by definition `(X' ∩ X'') ∩ (T_x − {x}) = ∅`; hence the
intersections of `X'` and `X''` with `T_x − {x}` are two non-empty closed disjoint subsets in `T_x − {x}`, whose
union is `T_x − {x}`; now this contradicts the hypothesis that `T_x − {x}` is connected. Q.E.D.

<!-- original page 233 -->

To prove `(15.5.6)`, we shall apply the lemma `(15.5.6.1)` to `X` and to its closed part `Z = f⁻¹(a)` which is rare
since `f` is open. Note that the hypothesis, taking `(15.2.2.1)` into account, implies that `f` is flat at the
points of `f⁻¹(a)`. For such a point `x`, `𝒪_x` is then a torsion-free `𝒪_a`-module `(0_I, 6.3.4)`, and in
particular, if `t` is a uniformizer of `𝒪_a`, `t` is `𝒪_x`-regular. Moreover `𝒪_x / t 𝒪_x` is reduced by hypothesis;
if it is of depth `0`, it is therefore a field `(0, 16.4.7)`, and as `t 𝒪_x` is then the maximal ideal of `𝒪_x`,
`𝒪_x` is a discrete valuation ring `(0, 17.1.4)`, hence `Spec(𝒪_x) − {x}` reduces to a point, and *a fortiori* is
connected. If on the contrary `prof(𝒪_x / t 𝒪_x) ≥ 1`, one has `prof(𝒪_x) ≥ 2` since `t` is `𝒪_x`-regular
`(0, 16.4.6)`; it then follows from Hartshorne's theorem `(5.10.7)` that `Spec(𝒪_x) − {x}` is connected, which ends
the demonstration.

**Proposition (15.5.7).**

<!-- label: IV.15.5.7 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a proper morphism. For every `z ∈ Y`, let `n(z)` be the
geometric number of connected components of `f⁻¹(z)`. Let `y` be a point of `Y` such that `f` be universally open
at the points of `f⁻¹(y)` and that `f⁻¹(y)` be geometrically reduced over `k(y)` `(4.6.2)`. Then the function
`z ↦ n(z)` is constant in a neighbourhood of `y`.*

One knows already `(15.5.4)` that under the conditions of the statement, `z ↦ n(z)` is lower semi-continuous at the
point `y`; everything comes down to seeing that it is also upper semi-continuous, and by the same reasoning as at the
beginning of the demonstration of `(15.5.1, (i))`, it suffices to show that if `y'` is a generization of `y`, one has

```text
  (15.5.7.1)             n(y') ≤ n(y).
```

Using the reasoning at the beginning of the demonstration of `(15.5.2)` and the lemma `(15.5.2.2)` applied to the
finite morphism `g` of the Stein factorization `f = g ∘ f'` of `f` (recalling that the geometric number of points of
`g⁻¹(y)` is equal to that of the connected components of `f⁻¹(y)` `(III, 4.3.4)`), one is reduced to the case where
`n(y)` and `n(y')` are respectively the number of connected components of `f⁻¹(y)` and `f⁻¹(y')`, and where `Y` is
the spectrum of a discrete valuation ring, `y` the closed point and `y'` the generic point of `Y`. One may in
addition replace `X` by any one of its connected components, these latter being open and closed in `X`, and proper
over `Y`. Suppose then `X` connected; the hypothesis that `f` is open at the points of `f⁻¹(y)` entails that if
`f⁻¹(y) ≠ ∅`, one has also `f⁻¹(y') ≠ ∅` `(1.10.3)`; the hypothesis that `f` is closed entails that if
`f⁻¹(y') ≠ ∅`, one has also `f⁻¹(y) ≠ ∅` `(II, 7.2.1)`. Hence, if `X ≠ ∅` (which one may evidently suppose, the
proposition being trivial in the contrary case), `f⁻¹(y)` and `f⁻¹(y')` are both non-empty. Moreover, the hypothesis
entails that the prescheme `f⁻¹(y)` is reduced `(4.6.1)`; as `f` is open at the points of `f⁻¹(y)`, the lemma
`(15.5.6)` implies that `f⁻¹(y')` is connected, in other words `n(y') = 1`. As `f⁻¹(y)` is not empty, this proves
`(15.5.7.1)`.

**Remark (15.5.8).**

<!-- label: IV.15.5.8 -->

The relation `(15.5.7.1)` is no longer necessarily valid if `f` is not supposed proper, even if it verifies the
other hypotheses of `(15.5.7)`. With the notation of `(15.5.5, (i))`, it suffices to see this to consider the
restriction of `f` to `X − {x'}`, where `x'` is one of the two points of `X` above a point `y` distinct from `y'`
and `y''`; one then has `n(y) = 1`, while if `η` is the generic point of `Y`, `n(η) = 2`.

<!-- original page 234 -->

**Proposition (15.5.9).**

<!-- label: IV.15.5.9 -->

*Let `f : X → Y` be a flat morphism locally of finite presentation; for every `y ∈ Y`, let `n(y)` be the geometric
number of connected components of `f⁻¹(y)`.*

*(i) If `f` is separated and quasi-finite, the function `y ↦ n(y)` (then equal to the geometric number of points of
`f⁻¹(y)`) is lower semi-continuous in `Y`; if it is constant in a neighbourhood of `y_0`, `f` is proper at the point
`y_0`.*

*(ii) If `f` is proper, the function `y ↦ n(y)` is lower semi-continuous in `Y`; if moreover `f⁻¹(y_0)` is
geometrically reduced over `k(y_0)`, `n(y)` is constant in a neighbourhood of `y_0`.*

In all cases, the questions are local on `Y`, hence one may suppose `Y` affine and `f` of finite presentation; using
`(8.9.1)`, `(8.10.5)` and `(11.2.7)`, one is reduced to the case where `Y` is Noetherian (using in addition
`(8.2.11)` for the second assertion of (i)). As moreover `f` is then universally open `(2.4.6)`, it suffices to
apply `(15.5.1)`, `(15.5.4)` and `(15.5.7)` to conclude.

**Remark (15.5.10).**

<!-- label: IV.15.5.10 -->

One will note that one has thus obtained another demonstration of `(12.2.4, (vi))`. Conversely, one may deduce
`(15.5.7)` from `(12.2.4, (vi))`: indeed, one may restrict to the case where `Y` is reduced (replacing `f` by
`f_red`), and it then follows from the hypotheses of `(15.5.7)` and from `(15.2.3)` that `f` is flat in an open
neighbourhood of `f⁻¹(y)`; as moreover `f` is proper, one may suppose that this neighbourhood is of the form
`f⁻¹(U)`, where `U` is an open neighbourhood of `y` in `Y`. One then concludes by `(12.2.4, (vi))`. The
demonstration of `(15.5.7)` given above has the advantage of bringing out the result `(15.5.6)`, which has an
independent interest.

### 15.6. Connected components of the fibres along a section

**Proposition (15.6.1).**

<!-- label: IV.15.6.1 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `g : Y → X` a `Y`-section
of `X` `(I, 2.5.5)`. For every `y ∈ Y`, designate by `X°_y` the connected component of `f⁻¹(y)` containing the point
`g(y)`. Let `y` be a point of `Y`, `y'` a generization of `y` in `Y`. Then:*

*(i) If there exists an irreducible component `Z` of `X°_{y'}`, of dimension equal to `dim(X°_{y'})` and containing
`g(y')` (which will be the case if `X°_{y'}` is irreducible), one has*

```text
  (15.6.1.1)             dim(X°_y) ≥ dim(X°_{y'}).
```

*(ii) If moreover `X°_y` is irreducible and if the two sides of `(15.6.1.1)` are equal, then
`X°_y ⊂ ‾{X°_{y'}}` (closure in `X`).*

(i) Let `‾Z` be the closure of `Z` in `X`; as `y` is adherent to `y'` and `g` continuous, one has `g(y) ∈ ‾Z`. As
`Z = ‾Z ∩ f⁻¹(y')`, it follows from Chevalley's semi-continuity theorem `(13.1.3)` applied to the restriction of
`f` to the reduced closed subprescheme of `X` having `‾Z` as underlying space, that one has
`dim_{g(y)}(‾Z ∩ f⁻¹(y)) ≥ dim(Z)`; but the irreducible components of `‾Z ∩ f⁻¹(y)` containing `g(y)` are
evidently contained in `X°_y`, whence *a fortiori* the inequality `(15.6.1.1)`.

(ii) The reasoning of (i) shows in addition that if the two sides of `(15.6.1.1)` are equal, one necessarily has
`dim_{g(y)}(‾Z ∩ f⁻¹(y)) = dim_{g(y)}(X°_y)`; if `X°_y` is irreducible, this entails `‾Z ∩ f⁻¹(y) = X°_y`, hence
`X°_y` is contained in `‾Z`, and *a fortiori* in `‾{X°_{y'}}`.

<!-- original page 235 -->

**Corollary (15.6.2).**

<!-- label: IV.15.6.2 -->

*With the notation of `(15.6.1)`, suppose in addition that for every `y ∈ Y`, `X°_y` is irreducible. Then the
function `z ↦ dim(X°_z)` is upper semi-continuous in `Y`. If moreover this function is constant in a neighbourhood
of a point `y ∈ Y`, then one has `X°_y ⊂ ‾{X°_{y'}}` for every generization `y'` of `y`.*

Let `y` be a point of `Y`, and let `U` be an affine open neighbourhood of `g(y)` in `X`; then there is an open
neighbourhood `V` of `y` in `Y` such that `g(V) ⊂ U`, and for every `z ∈ V`, `U ∩ X°_z` is dense in `X°_z`, hence
`dim(X°_z) = dim(U ∩ X°_z)` `(4.1.1.3)`. Replacing `X` by `U`, one may therefore suppose that `f` is a morphism of
finite type. One then knows `(9.7.10)` that the function `z ↦ dim(X°_z)` is locally constructible, and the
assertions of the corollary therefore follow from `(15.6.1)` and from `(0_III, 9.3.4)`.

**Proposition (15.6.3).**

<!-- label: IV.15.6.3 -->

*With the notation of `(15.6.1)`, suppose that for every `y ∈ Y`, `X°_y` is geometrically irreducible `(4.5.2)`.
Then, for every `y ∈ Y` such that the function `z ↦ dim(X°_z)` is constant in a neighbourhood of `y`, `f` is
universally open at the points of `X°_y`.*

Let us apply criterion `(14.3.7)`. Let then `h : Y' → Y` be a morphism, `Y'` being the spectrum of a discrete
valuation ring, of which we shall designate by `t`, `t'` the closed point and the generic point respectively, and
suppose that `h(t) = y`, so that `y' = h(t')` is a generization of `y`. Set `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`,
`g' = g_{(Y')} : Y' → X'`. With the same notation as in `(15.6.1)`, the hypothesis made on the `X°_z` implies that
`X'°_t = X°_y ⊗_{k(y)} k(t)` and `X'°_{t'} = X°_{y'} ⊗_{k(y')} k(t')`, and that `X'°_t` and `X'°_{t'}` are irreducible
`(4.4.1)`; as `dim(X°_y) = dim(X'°_t)` and `dim(X°_{y'}) = dim(X'°_{t'})` `(4.1.4)`, one sees that one is reduced to
proving the proposition for `f'` and `X'°_t`, in other words one may restrict to the case where `Y` is the spectrum
of a discrete valuation ring, `y` its closed point and `y'` its generic point; if `x'` is the generic point of
`X°_{y'}`, it follows then from `(15.6.2)` that every point of `X°_y` is a specialization of `x'`, whence the
conclusion.

**Proposition (15.6.4).**

<!-- label: IV.15.6.4 -->

*Under the general hypotheses of `(15.6.1)`, let `X°` be the union of the `X°_y` as `y` runs over `Y`. If `y ∈ Y` is
such that `X°_y` is geometrically reduced over `k(y)` `(4.6.2)` and if `f` is universally open at every point of
`X°_y`, then `X°` is a neighbourhood of `X°_y` in `X`. In particular, if `f` is universally open and if, for every
`y ∈ Y`, `X°_y` is geometrically reduced over `k(y)`, `X°` is open in `X`.*

Let us first show that one may reduce to the case where `f` is a morphism of finite type. Let `x` be a point of
`X°_y`; it follows from `(5.10.8.1)` (with `S = {0}`) that there is a finite sequence `(Z_i)_{0 ≤ i ≤ n}` of
irreducible components of `f⁻¹(y)` such that `g(y) ∈ Z_0`, `x ∈ Z_n`, and `Z_i ∩ Z_{i+1} ≠ ∅` for
`0 ≤ i ≤ n − 1`; the `Z_i` being irreducible, there is a finite sequence `(U_i)` (`0 ≤ i ≤ n`) of affine open sets
in `f⁻¹(y)` such that `g(y) ∈ U_0`, `x ∈ U_n`, `U_i` being an affine neighbourhood of a point `x_i` of
`Z_i ∩ Z_{i-1}` for `1 ≤ i ≤ n`. There is for each `i` a quasi-compact open set `W_i` in `X` such that
`U_i = f⁻¹(y) ∩ W_i`; let `W` be the quasi-compact open set of `X` union of the `W_i`. As `g` is continuous, there
is an affine open neighbourhood `V` of `y` in `Y` such that `g(V) ⊂ W`; if `X' = W ∩ f⁻¹(V)`, the restriction of `f`
to `X'` is of finite type; moreover, if, for every `z ∈ V`, `X'°_z` is the connected component of `X' ∩ f⁻¹(z)`
containing `g(z)`, one has `X'°_z ⊂ X°_z`, and `x` belongs to `X'°_y`. Indeed, each of the `U_i` contains the two
irreducible sets `U_i ∩ Z_{i-1}` and `U_i ∩ Z_i` which meet, and the irreducible sets `U_i ∩ Z_{i-1}` and
`U_{i-1} ∩ Z_{i-1}` meet for `1 ≤ i ≤ n`;

<!-- original page 236 -->

the union of the `U_i ∩ Z_{i-1}` and the `U_i ∩ Z_i` for `0 ≤ i ≤ n` is therefore connected and contains `x` and
`g(y)`. As `f | X'` is universally open at the points of `X'°_y`, this ends proving our assertion, for if the
proposition is proved when `f` is of finite type, the union `X'°` of the `X'°_z` for `z ∈ V` will be a neighbourhood
of `x`, and the same will hold for `X°`.

Suppose then `f` of finite type. Then `X°` is locally constructible `(9.7.12)`; it therefore suffices to show that
`X°` contains every generization `x'` of `x` `(0_III, 9.2.5)`. Set `y' = f(x')`; there exists a discrete valuation
ring `A` and a morphism `u` of `Y' = Spec(A)` into `X` such that, if `z` is the closed point and `z'` the generic
point of `Y'`, one has `u(z) = x` and `u(z') = x'` `(II, 7.1.9)`; if `h = f ∘ u`, one therefore has `h(z) = y` and
`h(z') = y'`. Set `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`, which is a morphism of finite type universally open
at the points of `f'⁻¹(z)`, and `g' = g_{(Y')}`, which is a `Y'`-section of `X'`. If
`p_y : f'⁻¹(z) → f⁻¹(y)` (resp. `p_{y'} : f'⁻¹(z') → f⁻¹(y')`) is the canonical projection, `p_y⁻¹(X°_y)`
(resp. `p_{y'}⁻¹(X°_{y'})`) is the connected component of `f'⁻¹(z)` (resp. `f'⁻¹(z')`) containing
`g'(z)` (resp. `g'(z')`), for the `X°_z` are geometrically connected `(4.5.13)` and it suffices to apply `(4.4.1)`.
Moreover, the morphism `u` corresponds to a `Y'`-section `v` of `X'` such that `p_y(v(y)) = x`,
`p_{y'}(v(y')) = x'`, so that `v(y')` is a generization of `v(y)`, and it will therefore suffice to prove that
`v(y')` belongs to `p_{y'}⁻¹(X°_{y'})`. Finally, it is clear that `p_y⁻¹(X°_y)` is geometrically reduced over
`k(z)`.

In other words, one is reduced to the case where `Y` is the spectrum of a discrete valuation ring, `y` its closed
point, `y'` its generic point. As `f⁻¹(y) − X°_y` is then closed in `X`, one may, replacing `X` by the open set
`X − (f⁻¹(y) − X°_y)`, suppose that `X°_y = f⁻¹(y)`; in the same way, one may replace `X` by the open set, connected
component of `X`, which contains `g(Y)`, this connected component evidently containing `X°`; in other words, one
may suppose `X` connected. The proposition will then be established if one shows that `X° = X`, or again that
`X°_{y'}` is connected; but `f⁻¹(y')` is geometrically reduced over `k(y')`, and *a fortiori* reduced; as moreover
`f` is open at the points of `f⁻¹(y)`, one may apply the lemma `(15.5.6)`, whence the conclusion.

**Corollary (15.6.5).**

<!-- label: IV.15.6.5 -->

*Let `f : X → Y` be a flat morphism of finite presentation, `g` a `Y`-section of `X`; for every `y ∈ Y`, let
`X°_y` be the connected component of `f⁻¹(y)` containing `g(y)`, and let `X°` be the union of the `X°_y` as `y`
runs over `Y`. Then, for every `y ∈ Y` such that `X°_y` be geometrically reduced over `k(y)`, `X°` is a
neighbourhood of `X°_y` in `X`. In particular, if `f` is reduced `(6.8.1)`, `X°` is open in `X`.*

The question being local on `Y`, one may suppose `Y = Spec(A)` affine. There exists therefore a Noetherian subring
`A_0` and a flat morphism of finite type `f_0 : X_0 → Y_0 = Spec(A_0)` such that `X = X_0 ×_{Y_0} Y` and
`f = (f_0)_{(Y)}` (`(8.9.1)` and `(11.2.7)`); moreover, one may suppose that there exists a `Y_0`-section `g_0` of
`X_0` such that `g = (g_0)_{(Y)}` `(8.8.2)`. For every `y ∈ Y`, let `y_0` be its projection in `Y_0`; it follows
from `(4.5.13)` that `(X_0)°_{y_0}` is geometrically connected, hence, if `p : f⁻¹(y) → f_0⁻¹(y_0)` is the canonical
projection, one has `X°_y = p⁻¹((X_0)°_{y_0})` `(4.4.1)`; in addition, the hypothesis that `X°_y` is geometrically
reduced over `k(y)` entails that `(X_0)°_{y_0}` is geometrically reduced over `k(y_0)` `(4.6.10)`. One is thus
reduced to the case where one supposes

<!-- original page 237 -->

in addition `Y` Noetherian; as `f` is universally open `(11.1.1)`, it then suffices to apply `(15.6.4)`.

**Proposition (15.6.6).**

<!-- label: IV.15.6.6 -->

*Let `f : X → Y` be a morphism such that `Y` be locally Noetherian and `f` locally of finite type, or that `f` be of
finite presentation. Let `g` be a `Y`-section of `X`; for every `y ∈ Y`, let `X°_y` be the connected component of
`f⁻¹(y)` containing `g(y)`; finally, let `X°` be the union of the `X°_y` as `y` runs over `Y`.*

*Suppose that, for every `y ∈ Y`, `X°_y` is geometrically irreducible. Then:*

*(i) The function `y ↦ dim(X°_y)` is upper semi-continuous in `Y`.*

*(ii) Let `x_0 ∈ X°`, `y_0 = f(x_0)`. If the function `y ↦ dim(X°_y)` is constant in a neighbourhood of `y_0`,
there exists an open neighbourhood `U` of `y_0` such that `f` be universally open at the points of
`X° ∩ f⁻¹(U)`. If moreover `Y` is reduced and `f⁻¹(y_0)` geometrically reduced over `k(y_0)` at the point `x_0`,
`f` is flat at the point `x_0`.*

*(iii) Conversely, suppose that `f` is universally open at the generic point of `X°_{y_0}` and moreover that one of
the following conditions is verified:*

*α) The fibre `f⁻¹(y_0)` is geometrically reduced over `k(y_0)` at the point `g(y_0)` and the ring `𝒪_{Y, y_0}` is
Noetherian.*

*β) For every generic point `y'` of an irreducible component of `Y` containing `y_0`, one has*

```text
  dim(X°_{y'}) ≥ dim(X°_{y_0}).
```

*Then the function `y ↦ dim(X°_y)` is constant in a neighbourhood of `y_0`.*

*(iv) The set `W` of points `x ∈ X°` such that the function `y ↦ dim(X°_y)` be constant in a neighbourhood of
`f(x)` and that `X°_{f(x)}` be geometrically reduced over `k(f(x))`, is open in `X`.*

The questions being local on `Y`, one may suppose that `Y = Spec(A)` is affine. When `f` is of finite presentation,
there exists therefore a Noetherian subring `A_1` of `A` and a morphism of finite type
`f_1 : X_1 → Y_1 = Spec(A_1)` such that `X = X_1 ×_{Y_1} Y` and `f = (f_1)_{(Y)}` `(8.9.1)`; moreover, one may
suppose that there exists a `Y_1`-section `g_1` of `X_1` such that `g = (g_1)_{(Y)}` `(8.8.2)`. For every `y ∈ Y`,
let `y_1` be its projection in `Y_1`; it follows from `(4.5.13)` that `(X_1)°_{y_1}` is geometrically connected,
hence, if `p : f⁻¹(y) → f_1⁻¹(y_1)` is the canonical projection, one has `X°_y = p⁻¹((X_1)°_{y_1})` `(4.4.1)`. Note
on the other hand that one may, by virtue of `(9.7.11)` and `(9.7.12)`, apply `(9.3.3)` to the property of being
geometrically irreducible; one may therefore suppose `A_1` chosen so that `(X_1)°_{y_1}` be geometrically irreducible
for every `y_1 ∈ Y_1`. One has `dim(X°_y) = dim((X_1)°_{y_1})` `(4.1.4)`, and by applying again `(9.3.3)` to the
property of having a given dimension (and using `(9.5.5)` and `(9.7.12)`), one may suppose (restricting if necessary
`Y` to a neighbourhood of `y_0`) that if `dim(X°_y)` is constant in `Y`, then `dim((X_1)°_{y_1})` is constant in
`Y_1`. If `Y` is reduced, the same holds for `Y_1` since `A_1 ⊂ A`; on the other hand, if `f⁻¹(y_0)` is
geometrically reduced at the point `x_0`, `f_1⁻¹(y_{01})` is so at the point `x_{01}` (`x_{01}` and `y_{01}` being
the respective projections in `X_1` and `Y_1` of `x_0` and `y_0`) `(4.6.10)`.

These remarks show that to demonstrate (i) and (ii), one may restrict to the case where `Y` is Noetherian and `f`
locally of finite type. But in this case, the assertion (i) follows from `(15.6.2)` and the first assertion of (ii)
from `(15.6.3)`. On the other hand, if `Y` is reduced and `f⁻¹(y_0)` geometrically reduced over `k(y_0)` at the
point `x_0` (`Y` being always supposed

<!-- original page 238 -->

Noetherian), as `X°_y` is the only irreducible component of `f⁻¹(y)` containing `x_0`, one deduces from `(15.6.3)`
and `(15.2.3)` that if `dim(X°_y)` is constant in a neighbourhood of `y_0`, `f` is flat at the point `x_0`.

To prove (iii), let us first remark that the set `X°` is locally constructible in `X` `(9.7.12)`, hence, by
`(9.5.5)`, the set `E` of `y ∈ Y` such that `dim(X°_y) = dim(X°_{y_0})` is locally constructible in `Y`. Let us then
apply `(1.10.1)` to `E`: it suffices to prove (taking (i) into account) that `dim(X°_{y'}) = dim(X°_{y_0})` for the
generic point `y'` of an irreducible component of `Y` containing `y_0`; this already allows us to suppose that
`Y = Spec(𝒪_{Y, y_0})`.

If one is in case α), one reduces at once, by virtue of `(II, 7.1.9)`, and using `(4.5.13)` and `(4.4.1)` as in
`(15.6.4)`, to the case where `Y` is the spectrum of a discrete valuation ring, `y_0` its closed point and `y'` its
generic point. But then the hypotheses entail, by virtue of `(15.2.2.1)`, that `f` is flat at the point `g(y_0)`,
hence also in a neighbourhood `V` of this point in `X` `(11.1.1)`. To demonstrate our assertion, one may replace
`X` by `V`, for `V ∩ X°_{y'}` is not empty by virtue of `(2.3.4)`, hence is an everywhere dense open set in
`X°_{y'}`, and consequently has the same dimension `(4.1.1.3)`; moreover, as `X°_{y'}` is also the connected
component of `f⁻¹(y')` containing `g(y')`, one may suppose `V` chosen such that `V` meets no other irreducible
component of `f⁻¹(y_0)` nor of `f⁻¹(y')`, in other words one may suppose that `X°_y = X`; but then the conclusion
follows from `(12.1.1, (i))`, since by hypothesis `X°_{y_0}` is integral.

Suppose now that one is in case β). Let us apply this time `(II, 7.1.4)` in the same way as `(II, 7.1.9)` in case
α): one is then reduced to the case where `Y` is the spectrum of a valuation ring (not necessarily discrete),
`y_0` its closed point and `y'` its generic point. By virtue of `(14.3.13)`, there exists an irreducible component
`Z` of `X` containing `X°_{y_0}` and dominating `Y`, and such that
`dim(Z ∩ f⁻¹(y')) = dim(X°_{y_0})`; but hypothesis β) and the fact that `dim(Z ∩ f⁻¹(y_0)) ≤ dim(f⁻¹(y_0))` show
that `dim(X°_{y_0}) ≤ dim(X°_{y'})`, whence `dim(X°_{y_0}) = dim(X°_{y'})` by virtue of (i).

It remains to prove (iv). Note first that the sets envisaged do not change when one replaces `f` by
`f_{(Y_red)} : X ×_Y Y_red → Y_red`, the projection `X ×_Y Y_red → X` being a homeomorphism. In other words, one
may suppose `Y` reduced, and then it follows from (ii) that `f` is flat at the points of `W`. Consider a point `x_0`
of `W` and let us prove that `W` is a neighbourhood of `x_0`; proceeding as at the beginning of the demonstration,
and using also `(11.2.7)`, one may in addition suppose `Y` Noetherian; it then follows from (ii) and from
`(15.6.4)` that `X°` is a neighbourhood of `x_0` in `X`, and from `(12.1.1, (vii))` that `W` is also a neighbourhood
of `x_0` in `X`.

**Corollary (15.6.7).**

<!-- label: IV.15.6.7 -->

*Suppose the preliminary conditions of `(15.6.6)` on `f` verified, and suppose in addition that for every `y ∈ Y`,
`X°_y` is geometrically integral over `k(y)`. Then the following conditions are equivalent:*

*a) The function `y ↦ dim(X°_y)` is locally constant in `Y`.*

*b) The morphism `f_{(Y_red)} : X ×_Y Y_red → Y_red` deduced from `f` by base change, is flat at the points of
`X°`.*

<!-- original page 239 -->

*Moreover, these conditions entail that `X°` is open in `X`. Finally, when `Y` is locally Noetherian, a) and b) are
also equivalent to*

*b') `f` is universally open at the points of `X°`.*

The fact that a) entails b) follows from `(15.6.6, (ii))`, as well as the fact that `X°` is then open in `X`. If
b) is verified, one may restrict to the case where `Y` is reduced and `f` flat; then, one reduces, as at the
beginning of `(15.6.6)`, and using in addition `(11.2.7)`, to the case where `Y` is Noetherian, a case where the
conclusion follows from `(15.6.6, (iii), case α))`. The equivalence of b) and b') has already been proved when `Y`
is locally Noetherian `(15.2.2.1)`, taking into account that the morphism `X ×_Y Y_red → X` is a universal
homeomorphism.

**Proposition (15.6.8).**

<!-- label: IV.15.6.8 -->

*Let `f : X → Y` be a separated morphism of finite presentation, `g` a `Y`-section of `X`; for every `y ∈ Y`, let
`X°_y` be the connected component of `f⁻¹(y)` that contains `g(y)`, and let `X°` be the union of the `X°_y` as `y`
runs over `Y`. Then, if `y ∈ Y` is such that `X°_y` be proper over `k(y)`, `X°` is proper over `Y` at the point `y`
(i.e. `(15.7.1)`, there exists an open neighbourhood `U` of `y` in `Y` such that `X° ∩ f⁻¹(U)` be closed in
`f⁻¹(U)` and proper over `U`).*

Proceeding as at the beginning of `(15.6.6)` (where one uses `(8.10.5, (v))`, and where one replaces `(9.7.11)` by
`(9.6.7)`), one reduces to the case where `Y` is Noetherian and `f` of finite type. One then knows `(9.7.12)` that
`X°` is locally constructible in `X`; on the other hand, the `X°_z` are geometrically connected (for every
`z ∈ Y`) by virtue of `(4.5.13)`; finally, as `g(Y) ⊂ X°`, `X°` is universally submersive over `Y` `(15.7.8)`. It
then suffices to apply to `X°` the criterion `(15.7.9)`.

**Corollary (15.6.9).**

<!-- label: IV.15.6.9 -->

*Let `f : X → Y` be a separated morphism such that `Y` be locally Noetherian and `f` locally of finite type, or
that `f` be of finite presentation. Let `g` be a `Y`-section of `X`, and for every `y ∈ Y`, let `X°_y` be the
connected component of `f⁻¹(y)` containing `g(y)`. Let `y` be a point of `Y` such that `X°_y` be proper over
`k(y)`. Then, for every generization `y'` of `y`, one has `dim(X°_{y'}) ≤ dim(X°_y)`.*

Suppose first `f` of finite presentation; then by replacing if necessary `Y` by a neighbourhood of `y`, one may
suppose that `f | X°` is proper `(15.6.8)`, and it suffices to apply `(13.1.5)` to this restriction. If `Y` is
locally Noetherian and `f` locally of finite type, `X` is locally Noetherian; moreover the hypothesis that `X°_y`
is proper over `k(y)` entails that `X°_y` is Noetherian; there exists therefore a Noetherian open set `V ⊂ X`
containing `X°_y`; consequently there is an open neighbourhood `W` of `y` in `Y` such that `g(W) ⊂ V`. Moreover,
if `z` is a maximal point of `X°_{y'}`, one may suppose that `z ∈ V`. The restriction of `f` to `V ∩ f⁻¹(W)` is
then a morphism of finite type, and `g | W` a `W`-section; by applying to this morphism the result already
obtained, one sees that if `Z` is the irreducible component of `X°_{y'}` of generic point `z`, one has
`dim(Z) ≤ dim(X°_y)`. As `z` is any maximal point of `X°_{y'}`, one has indeed `dim(X°_{y'}) ≤ dim(X°_y)`.

**Remarks (15.6.10).**

<!-- label: IV.15.6.10 -->

*(i)* The additional hypothesis on the existence of an irreducible component of `X°_{y'}` containing `g(y')` and of
dimension equal to `dim(X°_{y'})`, made in `(15.6.1)`, is not superfluous, as is shown by the following example.
Let `A` be a discrete valuation ring, `π` a uniformizer of `A`, `K` the fraction field of `A`, `k` its residue
field. Take `Y = Spec(A)`, and designate by `y` and `y'` the closed point and the generic point of `Y`. Consider
the two following `Y`-schemes: `X_1 = Spec(A[t])`, `X_2 = Spec(K[u, v])`, where `t`, `u`, `v` are indeterminates

<!-- original page 240 -->

(one will note that the projection of `X_2` into `Y` is therefore `{y'}`). In the ring `A[t]`, the principal ideal
`(πt − 1)` is maximal, and therefore corresponds to a closed point `x_1` of `X_1`, which projects to the generic
point `y'` of `Y` and is such that `k(x_1) = K`. Consider on the other hand the closed point `x_2` of `X_2`
corresponding to the maximal ideal `(u) + (v)` of `K[u, v]`; one has also `k(x_2) = K`. As one will see in chap. V,
one may therefore glue `X_1` and `X_2` along the two closed subpreschemes `Z_1`, `Z_2` of `X_1`, `X_2` having
respectively `{x_1}` and `{x_2}` as underlying spaces, following the unique `Y`-isomorphism of `Z_1` onto `Z_2`.
Designate by `X` the `Y`-prescheme thus obtained, by `x` the point of `X` image of `x_1` and `x_2`. The "zero
section" `g` of `X_1` `(II, 1.7.9)` is then again a `Y`-section of `X`; `f⁻¹(y)` is equal to `(X_1)_y`, while
`f⁻¹(y')` has two irreducible components, respectively isomorphic to `(X_1)_{y'}` and `(X_2)_{y'}`, having a unique
common point `x`, and of respective dimensions `1` and `2`. See however prop. `(15.6.9)`.

*(ii)* Consider the morphism `f` defined in `(12.2.3, (ii))`, which is proper and flat; moreover, the restriction
of `f` to `X_1 ∩ f_0⁻¹(Y)` is an isomorphism, hence the inverse morphism `g : Y → X` is a `Y`-section of `X`. One
then has `dim(X°_{y_0}) = 1` while `dim(X°_y) = 0` for `y ≠ y_0`, although `X°_y` is geometrically irreducible for
every `y ∈ Y` (but `X°_{y_0}` is not reduced); one sees therefore that in `(15.6.6, (iii))`, one cannot suppress the
hypotheses α) and β). Moreover, `X°` is not a neighbourhood of `X°_{y_0}`, which proves that in `(15.6.4)`, one
cannot dispense with the hypothesis that `X°_y` is reduced.

*(iii)* In chap. VI, we shall apply the preceding results to the `Y`-preschemes in groups locally of finite type
over a locally Noetherian prescheme `Y`. If `G` is such a prescheme, there exists a canonical `Y`-section `g`, the
"unit section", and one shows that `G_y` is always geometrically irreducible and that one has
`dim(G°_y) = dim(G_y)`, on setting `G_y = f⁻¹(y)`. It will therefore follow from `(15.6.2)` and `(15.6.3)` that the
function `z ↦ dim(G_z)` is upper semi-continuous, and that if it is constant in the neighbourhood of a point `y`,
`f` is universally open at the points of `G°_y`. If moreover `G_y` is geometrically reduced over `k(y)` at one of
its points, one shows that `G_y` is smooth `(6.8.1)` over `k(y)` at all its points; it will then follow from
`(15.6.6)` that if moreover `𝒪_y` is reduced, then `f` is smooth at all the points of `G°` (but not necessarily at
all the points of `G_y`). These results will apply for example in the theory of Picard schemes, where we shall have
at our disposal a general theorem assuring that, under certain conditions, the function `z ↦ dim(G_z)` is locally
constant. Let us remark that it is in view of applications of this nature that the statements such as `(15.6.1)` are
given for morphisms locally of finite type, and not only for morphisms of finite type.

One will also note that in the case of a `Y`-prescheme in groups `G`, hypothesis β) of `(15.6.6)` is always
verified.

### 15.7. Appendix: Valuative criteria of local properness

This number gives complements to the valuative criterion of properness demonstrated in `(II, 7.3.10)`; it is
independent of the rest of §15.

**Definition (15.7.1).**

<!-- label: IV.15.7.1 -->

*Let `f : X → Y` be a morphism of preschemes, `y` a point of `Y`. One says that `f` is **proper at the point `y`**
if there exists an open neighbourhood `U` of `y` in `Y` such that the restriction `f⁻¹(U) → U` of `f` be a proper
morphism. One says that a part `Z` of `X` is **proper over `Y` at the point `y`** if there exists an open
neighbourhood `U` of `y` such that `Z ∩ f⁻¹(U)` be closed in `f⁻¹(U)` and proper over `U` `(II, 5.4.10)` (which
amounts to saying that for every closed subprescheme of `X` having `Z` as underlying space, the restriction
`Z → Y` of `f` to `Z` is proper at the point `y`).*

Let `g : Y' → Y` be an arbitrary morphism; set `X' = X ×_Y Y'`, `f' = f_{(Y')}` and, if `p : X' → X` is the canonical
projection, `Z' = p⁻¹(Z)`. Then, if `Z` is proper over `Y` at the point `y`, `Z'` is proper over `Y'` at every
point `y'` above `y` `(II, 5.4.2)`.

**Proposition (15.7.2).**

<!-- label: IV.15.7.2 -->

*Let `Y` be an integral locally Noetherian prescheme, `X` an integral prescheme, `f : X → Y` a separated, dominant
morphism of finite type, `y` a point of `Y`. The following conditions are equivalent:*

*a) `f` is proper at the point `y`.*

*b) If `Y_1 = Spec(𝒪_y)`, `X_1 = X ×_Y Y_1`, the morphism `f_1 = f_{(Y_1)} : X_1 → Y_1` is proper.*

*c) Every discrete valuation ring having `R(X)` as fraction field and dominating `𝒪_y` dominates a local ring
`𝒪_x` of `X` (in which case one has necessarily `f(x) = y`).*

<!-- original page 241 -->

The fact that a) implies b) follows from `(II, 5.4.2)`, and the implication b) ⟹ c) follows from `(II, 7.3.10)`.
There remains therefore to show that c) entails a). The question being local on `Y`, one may suppose `Y` affine,
hence Noetherian. By virtue of Chow's lemma `(II, 5.6.1)`, there exists an integral prescheme `X'`, a projective
morphism `p : P → Y`, a dominant open immersion `j : X' → P`, and a projective and birational (hence surjective)
morphism `q : X' → X` such that the diagram

```text
                       j
              P  ←──────────  X'
              │                │
            p │              q │
              ↓                ↓
              Y  ←─────f─────  X
```

is commutative. As `X'` is integral and `j` dominant, `P` is irreducible, and one may, replacing `P` by `P_red`,
suppose `P` integral `(I, 5.2.2 and II, 5.5.5, (vi))`. Everything comes down to proving that there exists an open
neighbourhood `U` of `y` such that `p⁻¹(U) ⊂ j(X')`, for then the restriction of `j` to
`j⁻¹(p⁻¹(U)) = q⁻¹(f⁻¹(U)) = V` will be an isomorphism onto `p⁻¹(U)`, hence the restriction `V → U` of `p ∘ q` will
be proper, and as the restriction `V → f⁻¹(U)` of `q` is surjective, the restriction `f⁻¹(U) → U` will be proper
`(II, 5.4.3)`. As `T = P − j(X')` is closed in `P`, `p(T)` is closed in `Y`, and it suffices to show that
`y ∉ p(T)`, or again that every `z' ∈ P` such that `p(z') = y` belongs to `j(X')`. Now, the field of rational
functions `R(P)` is equal to `R(X')`, hence to `R(X)` by construction; as one may restrict to the case where `z'`
is not the generic point of `P`, there exists a discrete valuation ring `A` having `R(X)` as fraction field and
dominating `𝒪_{z'}` `(II, 7.1.7)`; as `p(z') = y`, `A` dominates also `𝒪_y`, hence by hypothesis there exists `x ∈ X`
such that `f(x) = y` and that `A` dominates `𝒪_x`. As `q` is proper, there exists `x' ∈ X'` such that `q(x') = x`
and that `A` dominates `𝒪_{x'}` `(II, 7.3.10)`; hence `z'` and `j(x')` are two points of `P` whose local rings
`𝒪_{z'}` and `𝒪_{j(x')} = 𝒪_{x'}` are related `(I, 8.1.4)`; as `P` is a scheme, this entails `z' = j(x')`
`(I, 8.2.2)`, which finishes the demonstration.

**Remark (15.7.3).**

<!-- label: IV.15.7.3 -->

One may in `(15.7.2)` suppress the hypothesis that `Y` is locally Noetherian, by replacing in condition c) the
discrete valuation rings by arbitrary valuation rings; the demonstration is then unchanged, taking `(II, 7.3.10)`
into account.

**Corollary (15.7.4).**

<!-- label: IV.15.7.4 -->

*Let `Y` be a Noetherian prescheme, `f : X → Y` a separated morphism of finite type, `Z` a part of `X` such that
the maximal points of its closure `‾Z` belong to `Z` (which is the case when `Z` is finite, or when `Z` is
constructible `(0_III, 9.2.2)`). Let `y` be a point of `Y`. The following conditions are equivalent:*

*a) The set `Z` is proper over `Y` at the point `y`.*

*b) If `Y_1 = Spec(𝒪_y)`, `X_1 = X ×_Y Y_1`, and if `g_1 : X_1 → X` is the canonical projection and
`Z_1 = g_1⁻¹(Z)`, the closure `‾Z_1` of `Z_1` in `X_1` is proper over `Y_1`.*

*c) For every scheme `Y' = Spec(A')`, where `A'` is a discrete valuation ring, and every morphism `g : Y' → Y`,
such that the image `g(y')` of the closed point `y'` of `Y'` be `y`, one has the following property: setting
`X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`, `g' = g_{(Y')} : X' → X`, `Z' = g'⁻¹(Z)`, and designating by `η'`

<!-- original page 242 -->

the generic point of `Y'`, then, for every point `x' ∈ ‾{Z'} ∩ f'⁻¹(η')` rational over `k(η')`, there exists a
`Y'`-section of `X'` containing `x'`.*

The fact that a) entails b) follows from the fact that `Z_1 ⊂ g_1⁻¹(Z)` and that `g_1⁻¹(Z)` is proper over `Y_1`
`(15.7.1)`. The fact that b) entails c) follows from `(II, 7.3.3)`. There remains therefore to see that c) implies
a). It suffices evidently to prove that every irreducible component of `‾Z` is proper over `Y` at the point `y`,
and the hypothesis therefore allows us to restrict to the case where `Z` is reduced to a single point `z`. One may
evidently also, taking into account `(I, 5.2.2)` and `(II, 5.4.6)`, suppose that `X` and `Y` are reduced, then
(by definition of a proper part `(II, 5.4.10)`) suppose that `Z = X = {z}` and (applying again `(I, 5.2.2)`) that
`f` is dominant, hence `X` and `Y` integral and Noetherian; it must then be proved that `f` is proper at the point
`y` of `Y`. Let us show for this that `f` verifies condition c) of `(15.7.2)`. Let `A'` be a discrete valuation
ring having `R(X) = k(z)` as fraction field and dominating `𝒪_y`; with the notation of c), one has therefore
`g(y') = y`, and `g(η')` is the generic point `η = f(z)` of `Y`. As by definition `k(η') = k(z)`, there exists a
`k(η')`-morphism `Spec(k(η')) → Spec(k(z))` taking `η'` to `z`, hence a `k(η')`-section of `f'⁻¹(η')`
`(I, 3.3.14)`; if `z'` is the image of `η'` by this section, `z'` is therefore rational over `k(η')` and
`g'(z') = z`. One therefore concludes from hypothesis c) that there exists a `Y'`-section `h'` of `X'` such that
`h'(η') = z'`; let `h = g' ∘ h' : Y' → X` be the corresponding `Y`-morphism, and let `x = h(y')`; it is clear that
`f(x) = y` and that `A' = 𝒪_{y'}` dominates `𝒪_x`, which finishes the demonstration.

**Corollary (15.7.5).**

<!-- label: IV.15.7.5 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a separated morphism of finite type, `y` a point of `Y`. The
following conditions are equivalent:*

*a) `f` is proper at the point `y`.*

*b) If `Y_1 = Spec(𝒪_y)`, `X_1 = X ×_Y Y_1`, the morphism `f_1 = f_{(Y_1)} : X_1 → Y_1` is proper.*

*c) For every scheme `Y' = Spec(A')`, where `A'` is a discrete valuation ring, and every morphism `g : Y' → Y`,
such that the image `g(y')` of the closed point `y'` of `Y'` be `y`, one has the following property: setting
`X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'` and designating by `η'` the generic point of `Y'`, then, for every
`x' ∈ f'⁻¹(η')` rational over `k(η')`, there exists a `Y'`-section of `X'` containing `x'`.*

**Corollary (15.7.6).**

<!-- label: IV.15.7.6 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism of finite type. The following conditions are
equivalent:*

*a) There exists a proper morphism `g : X → Z` and an immersion `h : Z → Y` such that `f = h ∘ g`.*

*b) The subspace `f(X)` is locally closed in `Y`, and if `Z'` is the subprescheme of `Y` closed image of `X` by `f`
`(I, 9.5.3 and 9.5.1)`, and `Z''` the prescheme induced by `Z'` on the open set `f(X)` of `Z'`, so that `f`
factors in unique fashion as `f = j ∘ g` (where `j : Z'' → Y` is the canonical injection), then `g : X → Z''` is
proper.*

*c) For every `y ∈ f(X)`, `f` is proper at the point `y`.*

*d) For every scheme `Y' = Spec(A')`, where `A'` is a discrete valuation ring, and every morphism `g : Y' → Y` such
that `g(Y') ⊂ f(X)`, every rational `Y'`-section `(I, 7.1.2)` of `X' = X ×_Y Y'` extends in a unique way to a
`Y'`-section of `X'`.*

It is clear that b) entails a). To see that a) entails c), let us first remark that a) entails that `h(Z)` is
locally closed in `Y` and `g(X)` closed in `Z`, hence `f(X)` is locally closed in `Y`; for every `y ∈ f(X)`, there
is therefore an open neighbourhood `U`

<!-- original page 243 -->

of `y` in `Y` such that `f(X) ∩ U` be closed in `U`; then the restriction `h⁻¹(U) → U` of `h` is a closed immersion,
and the restriction `f⁻¹(U) = g⁻¹(h⁻¹(U)) → h⁻¹(U)` of `g` is proper, hence the restriction `f⁻¹(U) → U` of `f` is
proper `(II, 5.4.2)`. To see that c) entails b), note first that, for every `y ∈ f(X)`, there exists, by virtue of
c), an open neighbourhood `U` of `y` in `Y` such that `f(X) ∩ U` be closed in `U`, hence `f(X)` is locally closed,
and consequently open in its closure. As this latter is the underlying space of `Z'`, and as `f` factors as
`f = j_0 ∘ g_0`, where `j_0 : Z' → Y` is the canonical injection and `g_0` is a morphism of `X` into `Z'`, the fact
that `g_0(X) = Z''` (which is open in `Z'`) entails the factorization of the statement of b); the fact that `g` is
proper then follows from the local character (over `Z''`) of this property, and from `(II, 5.4.3)`. It is clear
that c) implies d) by virtue of `(15.7.5)`, the uniqueness of the extension of a rational `Y'`-section following
from the hypothesis that `f` is separated `(I, 7.2.2)`. Let us finally prove that d) entails c); in the first
place, it follows from d), taking `(II, 7.2.3 and 7.2.4)` into account, that `f` is separated; one may then apply
the criterion `(15.7.5, c))`, which shows that `f` is proper at every point of `f(X)`.

**Remarks (15.7.7).**

<!-- label: IV.15.7.7 -->

*(i)* In `(15.7.4, c))`, `(15.7.5, c))` and `(15.7.6, d))`, one may restrict to the case where the discrete
valuation ring `A'` is complete and admits an algebraically closed residue field. Indeed, in the demonstration of
`(15.7.4)`, if one considers a complete discrete valuation ring `A''` dominating `A'` and having an algebraically
closed residue field `(0_III, 10.3.1)`, hypothesis c) is then verified for `Y'' = Spec(A'')`, `X'' = X ×_Y Y''` and
`f'' = f_{(Y'')}`; but `X'' = X' ×_{Y'} Y''`, and it follows then from the remark `(II, 7.3.9, (i))` that `f'` is
proper; consequently `Y'`, `X'` and `f'` also verify hypothesis c) `(II, 7.3.8)`.

*(ii)* Taking `(II, 7.3.8)` into account, condition c) of `(15.7.5)` can be replaced by the condition that `f'` is
proper.

**(15.7.8)**

<!-- label: IV.15.7.8 -->

One says that a morphism of preschemes `f : X → Y` is **submersive** if it is surjective and if the topology of
`Y` is equal to the quotient of the topology of `X` by the equivalence relation defined by `f`. One says that `f`
is **universally submersive** if for every base change `Y' → Y`, the morphism `f' = f_{(Y')} : X ×_Y Y' → Y'` is
submersive. Every surjective universally open, or universally closed, or faithfully flat and quasi-compact
morphism is universally submersive `(2.3.12)`. Given a morphism `f : X → Y`, one says that a subset `Z` of `X` is
submersive over `f(Z)` if the topology of the subspace `f(Z)` of `Y` is quotient of the topology of the subspace
`Z` of `X` by the equivalence relation defined by `f | Z`. One says that `Z` is universally submersive over `f(Z)`
if, for every base change `g : Y' → Y`, the inverse image `Z' = p⁻¹(Z)` of `Z` under the projection
`p : X ×_Y Y' → Y'` is a submersive set over `f'(Z') = g⁻¹(f(Z))`. One will note that if the morphism `f` admits a
`Y`-section `h : Y → X`, every set `Z` containing `h(Y)` is universally submersive over `Y`.

**Proposition (15.7.9).**

<!-- label: IV.15.7.9 -->

*Let `Y` be a locally Noetherian prescheme, `y` a point of `Y`, `f : X → Y` a separated morphism of finite type.
Let `Z` be a locally constructible part of `X` having the following properties:*

*(i) For every generization `y'` of `y`, `Z_{y'} = Z ∩ f⁻¹(y')` is a connected component of `f⁻¹(y')` and is
geometrically connected over `k(y')` `(4.5.2)`.*

<!-- original page 244 -->

*(ii) `Z_y` is proper over `Spec(k(y))`.*

*(iii) `Z` is universally submersive over `f(Z)` `(15.7.8)`.*

*Then `Z` is proper over `Y` at the point `y` (in other words `(15.7.1)`, there exists an open neighbourhood `U`
of `y` such that `Z ∩ f⁻¹(U)` be closed in `f⁻¹(U)` and proper over `U`).*

Using the method of `(8.1.2, a))` and `(8.10.5, (xii))`, one is reduced to proving that when `Y = Spec(A)` is the
spectrum of a Noetherian local ring, hypotheses (i), (ii) and (iii) entail that `Z` is proper over `Y`.

Note first that if `A'` is a Noetherian local ring, `φ : A → A'` a local homomorphism, `Y' = Spec(A')` and
`g : Y' → Y` the morphism corresponding to `φ`, the inverse image `Z'` of `Z` by the canonical projection
`p : X ×_Y Y' → X` has, with respect to `Y'`, the properties (i), (ii), (iii) of the statement, taking
`(1.8.2)` into account; using `(2.7.1, (vii))`, it amounts to the same to demonstrate that `Z'` is proper over
`Y'`, provided that `A'` be a faithfully flat `A`-module. We shall use this remark by taking `A' = ‾A` `(0_I, 7.3.5)`,
in other words we may restrict to the case where `A` is complete. As `Z_y` is a connected component of `f⁻¹(y)`,
proper over `k(y)`, it follows from `(III, 5.5.2)` that `X` is a sum of two subpreschemes `X_0`, `X_1` induced on
open and closed parts of `X`, such that `X_0` be proper over `Y` and that `X_0 ∩ f⁻¹(y) = Z_y`. Set
`Z_0 = X_0 ∩ Z`, `Z_1 = X_1 ∩ Z`, so that these sets form a partition of `Z` into two parts open and closed in
`Z`. As the `Z_{y'}` are connected, one necessarily has `Z_{y'} ⊂ Z_0` or `Z_{y'} ⊂ Z_1`, hence
`f(Z_0) ∩ f(Z_1) = ∅`. But as `Z_0` and `Z_1` are saturated for the equivalence relation defined by `f | Z`, it
follows from (iii) that `f(Z_0)` and `f(Z_1)` are open in `f(Z)`. But `f(Z_0)` contains `y`, and every
neighbourhood of `y` in `Y` is equal to `Y`, hence `f(Z_0) = f(Z)`, and consequently `f(Z_1) = ∅`, hence
`Z_1 = ∅` and `Z ⊂ X_0`.

One may therefore now suppose in addition that `f` is proper, and there remains to prove that `Z` is closed in
`X`. In other words, it will suffice to prove that a constructible part `Z` of a prescheme `X` proper over `Y`
that satisfies the two sole conditions (i) and (iii), is closed in `X`. By virtue of `(0_III, 9.2.5)`, it therefore
suffices to prove that for every `x' ∈ Z` and every specialization `x` of `x'` in `X`, one has `x ∈ Z`. Let `A_1`
be a complete discrete valuation ring, `u` a morphism of `Y_1 = Spec(A_1)` into `X` such that, if `y_1` and `y'_1`
are the closed point and the generic point of `Y_1`, one has `u(y_1) = x`, `u(y'_1) = x'` `(II, 7.1.7)`; set
`g = f ∘ u : Y_1 → Y` and `X_1 = X ×_Y Y_1`; there exists a `Y_1`-section `u_1 : Y_1 → X_1` of
`f_1 = f_{(Y_1)}` such that `u = p ∘ u_1`, where `p : X_1 → X` is the canonical projection. If `x_1 = u_1(y_1)`,
`x'_1 = u_1(y'_1)`, one has therefore `p(x_1) = x` and `p(x'_1) = x'`, and `x_1` is a specialization of `x'_1`.
Moreover, one has `x'_1 ∈ Z_1 = p⁻¹(Z)`; as we have remarked that conditions (i) and (iii) are stable under every
base change, as well as the property of being constructible, one sees that one is reduced to the following
situation: `Y` is the spectrum of a complete discrete valuation ring, `X` is proper over `Y`, `f(x) = y` is the
closed point of `Y`, `y' = f(x')` its generic point, there exists a `Y`-section `h` of `X` such that `h(y) = x`,
`h(y') = x'`, and finally one has `x' ∈ Z`; it must be proved that `x ∈ Z`. Now, `Z_y` is a connected component of
`f⁻¹(y)`, proper over `Spec(k(y))` since `X` is proper over `Y`. Applying again `(III, 5.5.2)`, one sees as above
that there is an open and closed part `X'` of `X` such that `X' ∩ f⁻¹(y) = Z_y`; as `Z_y` is connected,

<!-- original page 245 -->

one may suppose `X'` connected (replacing if necessary `X'` by that of its connected components containing `Z_y`).
But then the same reasoning as at the beginning proves that one necessarily has `Z ⊂ X'`; as `h(Y)` is connected
and contains `x'`, it is necessarily contained in `X'`, hence `x = h(y) ∈ X' ∩ f⁻¹(y) = Z_y`. Q.E.D.

**Corollary (15.7.10).**

<!-- label: IV.15.7.10 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a separated morphism of finite type, universally
submersive `(15.7.8)` and such that all the fibres `X_y = f⁻¹(y)` be geometrically connected. Then, if `y ∈ Y` is
such that `X_y` be proper over `k(y)`, `f` is proper at the point `y`.*

Taking `(15.7.5)` into account, one is reduced to the case where `Y = Spec(𝒪_y)` since the hypotheses are stable
under base change. But in this case it suffices to apply `(15.7.9)` to `Z = X`.

**Corollary (15.7.11).**

<!-- label: IV.15.7.11 -->

*Let `f : X → Y` be a separated morphism of finite presentation; suppose that there exists a surjective morphism
of finite presentation `g : Y' → Y`, which is in addition proper or flat, and such that if one sets
`X' = X ×_Y Y'`, there exists a `Y'`-section of `X'` (or again a `Y`-morphism `Y' → X` `(I, 3.3.14)`). Suppose
finally that the fibres `X_y = f⁻¹(y)` be geometrically connected. Then the set `U` of `y ∈ Y` such that `X_y` be
proper over `k(y)` is open in `Y`, and the restriction `f⁻¹(U) → U` of `f` is proper.*

The question being local on `Y`, one may suppose `Y = Spec(A)` affine. Applying `(8.9.1)` to `f` and to `g`, one
sees that there exists a Noetherian subring `A_0` of `A` and two morphisms of finite type
`f_0 : X_0 → Y_0 = Spec(A_0)`, `g_0 : Y'_0 → Y_0` such that `X = X_0 ×_{Y_0} Y`, `Y' = Y'_0 ×_{Y_0} Y`,
`f = (f_0)_{(Y)}` and `g = (g_0)_{(Y)}`; moreover, using `(8.10.5, (v), (vi) and (xii))` and `(11.2.7)`, one may
suppose `f_0` separated, `g_0` surjective and proper (resp. flat) if `g` is proper (resp. flat); using `(8.8.2)`,
one may moreover suppose that there exists a `Y'_0`-section of `X_0`. On the other hand, using `(9.7.7)`, one may
apply `(9.3.3)` to the property of being geometrically connected, and one may therefore suppose `A_0` chosen so
that the `f_0⁻¹(y_0)` be geometrically connected for every `y_0 ∈ Y_0`. Finally, using `(2.7.1, (vii))`, it amounts
to the same to say that `f⁻¹(y)` is proper over `k(y)` or that `f_0⁻¹(y_0)` is proper over `k(y_0)`, where `y_0` is
the projection of `y` in `Y_0`. These remarks show that one is reduced to demonstrating the corollary when `Y` is
Noetherian. Note now the

**Lemma (15.7.11.1).**

<!-- label: IV.15.7.11.1 -->

*Let `f : X → Y` be a morphism, `g : Y' → Y` a surjective morphism, which is in addition proper or flat and
quasi-compact. Set `X' = X ×_Y Y'`, `f' = f_{(Y')} : X' → Y'`. Then, if `f'` is submersive (resp. universally
submersive), the same holds for `f`.*

One may restrict to the case where `f'` is submersive. Indeed, suppose the lemma proved in this case, and let us
show that if `f'` is universally submersive, `f` is so too. Let then `Y_1 → Y` be any morphism, and set
`Y'_1 = Y' ×_Y Y_1`; if `X'_1 = X' ×_{Y_1} Y'_1` and `f'_1 = (f')_{(Y'_1)} : X'_1 → Y'_1`, `f'_1` is submersive by
hypothesis; moreover the morphism `g_1 : Y'_1 → Y_1` is surjective, and proper (resp. flat and quasi-compact) if
`g` is. Hence, if one sets `X_1 = X ×_Y Y_1`, `f_1 = f_{(Y_1)}`, it follows from the hypothesis and from the fact
that `X'_1 = X_1 ×_{Y_1} Y'_1`, that `f_1` is submersive, hence `f` universally submersive. Suppose then only that
`f'` be submersive. It is clear first of all that `f` is surjective. Let `E` be a part of `Y` such that
`f⁻¹(E)` be closed in `X`; then, if `p : X' → X` is the canonical projection,

<!-- original page 246 -->

`p⁻¹(f⁻¹(E)) = f'⁻¹(g⁻¹(E))` is closed in `X'`, hence, since `f'` is submersive, `g⁻¹(E)` is closed in `Y'`; but
as `g` is also universally submersive `(15.7.8)`, `E` is closed in `Y`, which proves the lemma.

This being so, as there exists by hypothesis a `Y'`-section of `X'`, `f'` is universally submersive `(15.7.8)`,
hence the same holds for `f` according to the lemma `(15.7.11.1)`. It then suffices to apply `(15.7.10)`,
remarking that the set of `y ∈ Y` such that `f` be proper at `y` is by definition open in `Y`.

(To be continued.)

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/27-c4-s15-etude-fibres-morphisme-universellement-ouvert.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-3.pdf, pp. 223-248 -->

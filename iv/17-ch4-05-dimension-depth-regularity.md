<!-- original page 86 -->

## §5. Dimension and depth in preschemes

This section confines itself to restating, in the geometric language and with various complements of a technical nature,
the notions and results of commutative algebra exposed in Chapter 0, §§16 and 17.

### 5.1. Dimension of preschemes

**(5.1.1)**

<!-- label: IV.5.1.1 -->

Let `A` be a ring and `𝔍` an ideal of `A`. Recall `(0, 16.1)` that the definitions of the theory of dimension of a ring
`(0, 16.1.1)` and those of the theory of combinatorial dimension of topological spaces `(0, 14.1.2)` give the following
relations:

```text
  dim(Spec(A)) = dim(A)                                  (5.1.1.1)

  dim(V(𝔍)) = dim(A/𝔍)                                   (5.1.1.2)

  codim(V(𝔍), Spec(A)) = ht(𝔍)                           (5.1.1.3)
```

*(5.1.1.4)* `Spec(A)` is a catenary space ⟺ `A` is a catenary ring.

*(5.1.1.5)* `Spec(A)` is equidimensional ⟺ `A` is equidimensional ⟺ the minimal prime ideals `𝔭_α` of `A` are such that
the dimensions of the rings `A/𝔭_α` are all equal.

*(5.1.1.6)* `Spec(A)` is equicodimensional ⟺ `A` is equicodimensional ⟺ all the maximal ideals of `A` have the same
height.

Recall that a Noetherian ring `A` is said to be **biequidimensional** if `Spec(A)` is biequidimensional, that is to say
if `Spec(A)` is Noetherian and `A` is equidimensional, equicodimensional, catenary, and of finite dimension.

**Proposition (5.1.2).**

<!-- label: IV.5.1.2 -->

*Let `X` be a prescheme, `Y` an irreducible closed part of `X`, `y` the generic point of `Y`. One has*

```text
  codim(Y, X) = dim(𝒪_{X,y})                             (5.1.2.1)
```

Indeed `(I, 2.4.2)`, the irreducible closed parts of `X` containing `y` are canonically in bijective correspondence with
the irreducible closed parts of `Spec(𝒪_{X,y})`, hence in bijective correspondence with the prime ideals of `𝒪_{X,y}`,
and `(5.1.2.1)` follows from the definitions.

In particular, one recovers in this way the fact that the generic points of the irreducible components of `X` are the
only points `x ∈ X` such that `dim(𝒪_x) = 0` `(I, 1.1.14)`.

<!-- original page 87 -->

**Corollary (5.1.3).**

<!-- label: IV.5.1.3 -->

*For every closed part `Y` of a prescheme `X`, one has*

```text
  codim(Y, X) = inf_{y ∈ Y} dim(𝒪_{X,y}).                (5.1.3.1)
```

*Moreover, if `X` is locally Noetherian, one has, for every `x ∈ Y`,*

```text
  codim_x(Y, X) = inf_{y ∈ Y, x ∈ ‾{y}} dim(𝒪_{X,y}).    (5.1.3.2)
```

The relation `(5.1.3.2)` indeed follows from `(5.1.3.1)` and from `(0, 14.2.6)`.

This corollary allows us to *define*, for any part `Y` of a prescheme `X`, the **codimension** `codim(Y, X)` of `Y` in
`X` as equal to the second member of `(5.1.3.1)`.

**Proposition (5.1.4).**

<!-- label: IV.5.1.4 -->

*For every prescheme `X`, one has*

```text
  dim(X) = sup_{x ∈ X} (dim(𝒪_x)).                       (5.1.4.1)
```

*If every irreducible closed part of `X` contains a closed point, one has also*

```text
  dim(X) = sup_{x ∈ F} (dim(𝒪_x))                        (5.1.4.2)
```

*where `F` is the set of closed points of `X`.*

It suffices to remark (by virtue of `(I, 2.4.2)`) that the chains of irreducible closed parts of `X` correspond
bijectively with the chains of irreducible closed parts of a local scheme of `X`; when every irreducible closed part of
`X` contains a closed point, one can clearly restrict to the local schemes at the closed points of `X`.

We note that every irreducible closed part of `X` contains a closed point when `X` is quasi-compact `(0_I, 2.1.3)`; we
shall see a little further on `(5.1.11)` that the same holds when `X` is locally Noetherian.

**Corollary (5.1.5).**

<!-- label: IV.5.1.5 -->

*For a prescheme `X` to be catenary it is necessary and sufficient that, for every `x ∈ X`, the local ring `𝒪_x` be
catenary. If moreover every irreducible closed part of `X` contains a closed point, it suffices, for `X` to be catenary,
that `𝒪_x` be catenary for every closed point `x` of `X`.*

The reasoning is the same as in `(5.1.4)`, since one is comparing chains of irreducible closed parts having the same
extremities.

**(5.1.6)**

<!-- label: IV.5.1.6 -->

We shall now examine the more special properties tied to Noetherian hypotheses.

Recall `(0, 16.2.3)` that a Noetherian local ring `A ≠ 0` is of finite dimension, equal to the minimum number of
generators of an ideal of definition of `A`; for every prime ideal `𝔭` of `A`, the height of `𝔭`, equal to `dim(A_𝔭)`, is
therefore also finite. These properties, together with `(5.1.2)`, `(5.1.3)`, and `(5.1.4)`, show that:

**Proposition (5.1.7).**

<!-- label: IV.5.1.7 -->

*For every non-empty closed part `Y` of a locally Noetherian prescheme `X`, `codim(Y, X)` is finite. If `X` is
Noetherian and affine and `Y` an irreducible closed part of `X`, `codim(Y, X)` is equal to the minimum number of
sections `s_i` of `𝒪_X` over `X` such that `Y` is an irreducible component of the set of `x ∈ X` such that `s_i(x) = 0`
for every `i`.*

**Corollary (5.1.8).**

<!-- label: IV.5.1.8 -->

*Let `X` be a locally Noetherian prescheme, `ℒ` an invertible `𝒪_X`-Module, `f` a section of `ℒ` over `X`. Then every
irreducible component of the set `Z`*

<!-- original page 88 -->

*of `x ∈ X` such that `f(x) = 0` is of codimension `≤ 1` in `X`; it is of codimension `1` if `Z` contains no irreducible
component of `X`.*

One can restrict to the case where `ℒ = 𝒪_X`. If `y` is a generic point of an irreducible component `Y` of `Z`, the
ideal `(f_y)` of `𝒪_{X,y}` must be such that `𝒪_{X,y}/(f_y)` has only one prime ideal, which means that `f_y` generates
an ideal of definition of the Noetherian local ring `𝒪_{X,y}`; one thus has `codim(Y, X) ≤ 1` `(5.1.7)`; if `Z` contains
no irreducible component of `X`, one cannot have `codim(Y, X) = 0` by virtue of `(0, 14.2.1)`.

**Proposition (5.1.9).**

<!-- label: IV.5.1.9 -->

*Let `X` be a locally Noetherian prescheme, `Y` a closed part of `X`. If `x ∈ Y` is such that `𝒪_{X,x}` is a catenary
ring, one has*

```text
  codim_x(Y, X) = dim(𝒪_{X,x}) − codim(‾{x}, Y)          (5.1.9.1)
                = dim(𝒪_{X,x}) − dim(𝒪_{Y,x}).
```

Let `Y_i` (`1 ≤ i ≤ n`) be the irreducible components of `Y` containing `x` (which are finite in number since `Y` is
locally Noetherian), and let `y_i` be the generic point of `Y_i`. If one sets `A = 𝒪_{X,x}`, and if `𝔭_i` is the prime
ideal of `A` corresponding to `Y_i ∩ Spec(A)`, the irreducible closed parts of `Y` containing `x` correspond bijectively
with the prime ideals of `A` containing one of the `𝔭_i`, so `dim(𝒪_{Y,x}) = sup_i dim(A/𝔭_i)`; on the other hand, one
has `𝒪_{X,y_i} = A_{𝔭_i}`, and the hypothesis on `A` entails `dim(A) = dim(A/𝔭_i) + dim(A_{𝔭_i})` `(0, 16.1.4)`; the
conclusion thus follows from the relation `codim_x(Y, X) = inf_i (dim(𝒪_{X,y_i}))` (`(5.1.2)` and `(0, 14.2.6)`).

**Proposition (5.1.10).**

<!-- label: IV.5.1.10 -->

*(i) In every prescheme `X`, every non-empty locally constructible part `E` contains a point `x` such that `{x}` is a
locally closed part of `X` (or, what amounts to the same, such that `x` is isolated in `‾{x}`).*

*(ii) Let `X` be a locally Noetherian prescheme, `x` a point of `X` such that `{x}` is locally closed in `X`; then one
has `dim(‾{x}) ≤ 1`; every point `y ≠ x` of `‾{x}` is consequently closed in `X`.*

(i) The result is a particular case of the following lemma:

**Lemma (5.1.10.1).**

<!-- label: IV.5.1.10.1 -->

*Let `X` be a topological space having the following property: for every locally closed part `Z ≠ ∅` of `X`, there
exists a part `Z'` of `Z`, locally closed in `X` (or in `Z`, what amounts to the same), and a point `x ∈ Z'`, closed in
`Z'`. Then every locally closed part `Z ≠ ∅` of `X` contains a point `x` isolated in `‾{x}`.*

Indeed, let `Z' ⊂ Z` be a locally closed part of `Z` containing a point `x` such that `x` is closed in `Z'`. There is an
open neighbourhood `U` of `x` in `X` such that `Z' ∩ U` is closed in `U`, hence `x` is also closed in `U`; this means
that `U ∩ ‾{x} = {x}`, in other words that `x` is isolated in `‾{x}`.

The lemma applies to every underlying space of a prescheme `X`, for `Z` is then also the underlying space of a
prescheme `(I, 5.2.1)` and it suffices to take for `Z'` an affine open in `Z`, which is a quasi-compact Kolmogorov
space, hence contains a closed point `(0_I, 2.1.3)`.

<!-- original page 89 -->

(ii) Let `Z` be the reduced sub-prescheme of `X` having `‾{x}` as underlying space; the hypothesis entails that `{x}` is
open in `Z`; therefore, for every `z ∈ Z`, the generic point `x` of `Spec(𝒪_{Z,z})` is isolated in `Spec(𝒪_{Z,z})`; but
the ring `A = 𝒪_{Z,z}` is an integral Noetherian local ring, and the hypothesis entails that there exists `f ∈ A` such
that `A_f` is a field; one knows `(0, 16.3.3)` that this entails `dim(A) ≤ 1`. Since `dim(𝒪_{Z,z}) ≤ 1` for every `z ∈ Z`,
one indeed has `dim(Z) ≤ 1`.

**Corollary (5.1.11).**

<!-- label: IV.5.1.11 -->

*If `X` is a locally Noetherian prescheme, every non-empty closed part of `X` contains a closed point.*

Indeed, every closed part of `X` is constructible `(0_III, 9.1.1 and 9.1.5)` and it suffices to apply `(5.1.10)`.

**(5.1.12)**

<!-- label: IV.5.1.12 -->

Let `X` be a prescheme, `ℱ` a quasi-coherent `𝒪_X`-Module of finite type, `S = Supp(ℱ)` its support, which is closed in
`X` `(0_I, 5.2.2)`. If, for every `x ∈ X`, one considers `Supp(ℱ_x)` as a closed part of the local scheme `Spec(𝒪_x)`,
one has, by definition `(0, 16.1.7)` `dim(ℱ_x) = dim(Supp(ℱ_x))`; but one has

```text
  Supp(ℱ_x) = S ∩ Spec(𝒪_{X,x}) = Spec(𝒪_{S,x})
```

where, in the last term, `S` denotes any closed sub-prescheme of `X` having `S` as underlying space. If one remarks that
the irreducible components of `Spec(𝒪_{S,x})` are the intersections of `Spec(𝒪_{X,x})` with the irreducible components
of `S` containing `x`, and correspond bijectively with the latter, one sees that

```text
  dim(ℱ_x) = dim(𝒪_{S,x})                                (5.1.12.1)
```

by virtue of `(5.1.1.1)`; it also follows from `(5.1.2)` that one has

```text
  dim(ℱ_x) = codim(‾{x}, S)                              (5.1.12.2)
```

if `X` is locally Noetherian.

One says that `ℱ` is **equidimensional at the point `x ∈ X`** if `ℱ_x` is an equidimensional `𝒪_{X,x}`-module, that is
to say `(0, 16.1.7)` if `Supp(ℱ_x)` is equidimensional as a closed part of `Spec(𝒪_{X,x})`; this amounts to saying that
the ring `𝒪_{S,x}` is equidimensional.

One calls **dimension of `ℱ`** and denotes by `dim(ℱ)` the dimension of the support `Supp(ℱ)`; it follows from
`(5.1.4)` and `(5.1.12.1)` that one has

```text
  dim(ℱ) = sup_{x ∈ X} dim(ℱ_x).                         (5.1.12.3)
```

If `X = Spec(A)` is an affine scheme and if `ℱ = M̃`, where `M` is an `A`-module of finite type, one has
`dim(ℱ) = dim(M)` by virtue of `(0, 16.1.7)` and `(5.1.4)`.

**Proposition (5.1.13).**

<!-- label: IV.5.1.13 -->

*Let `X` be a prescheme, `ℱ` a quasi-coherent `𝒪_X`-Module of finite type, `x` a point of `X`, `x'` a generization of
`x` in `X`; one then has*

```text
  dim(ℱ_{x'}) ≤ dim(ℱ_x).                                (5.1.13.1)
```

This follows at once from `(5.1.12.1)` and the definitions.

<!-- original page 90 -->

### 5.2. Dimension of an algebraic prescheme

**Proposition (5.2.1).**

<!-- label: IV.5.2.1 -->

*Let `k` be a field, `X` an irreducible prescheme locally of finite type over `k`, `ξ` its generic point. Then `X` is
biequidimensional and one has `dim(X) = deg.tr_k k(ξ)`.*

Every local ring `𝒪_x` is the local ring of a `k`-algebra of finite type, hence a quotient of a regular local ring
`(0, 17.3.9)`, and one knows `(0, 16.5.12)` that such rings are catenary; consequently `X` is a catenary space
`(5.1.5)`, and as `X` is irreducible, it suffices `(5.1.1)` to show that for every closed point `x ∈ X`, one has

```text
  dim(𝒪_x) = deg.tr_k k(x).                              (5.2.1.1)
```

One may evidently suppose `X` reduced and affine, hence integral with ring `A`, an algebra of finite type over `k`. Let
`n = deg.tr_k k(ξ)`, with `k(ξ) = K` the field of fractions of `A`. One knows (Bourbaki, *Alg. comm.*, chap. V, §3, n° 1,
th. 1) that there exists a sub-`k`-algebra `B = k[t_1, …, t_n]` of `A`, where the `t_i` are algebraically independent
over `k`, such that `A` be a *finite* `B`-algebra. Let `𝔪 = j_x`, which by hypothesis is a maximal ideal of `A`;
`𝔫 = B ∩ 𝔪` is therefore a maximal ideal of `B` (Bourbaki, *Alg. comm.*, chap. V, §2, n° 1, prop. 1), and `A_𝔪` is a
local ring of the finite `B_𝔫`-algebra `S⁻¹A`, where `S = B − 𝔫`; as `B_𝔫` is integrally closed and `S⁻¹A` integral, one
has `dim(A_𝔪) = dim(B_𝔫)` `(0, 16.1.6)`. One may therefore restrict to the case where `A = k[t_1, …, t_n]`; one knows
then that `k' = k(x)` is a finite extension of `k` `(I, 6.4.2)`; let `A' = k'[t_1, …, t_n]`; taking into account
`(I, 2.4.6 and 3.3.14)`, there exists a maximal ideal `𝔪'` of `A'` above `𝔪` and such that `k'` be the residue field of
`A'_{𝔪'}`. Since `A'` is integral and is a finite `A`-algebra, the same reasoning as above shows that
`dim(A'_{𝔪'}) = dim(A_𝔪)`, so that one is reduced to the case where `A/𝔪 = k`. Now in this case `𝔪` is generated by
polynomials `t_i − a_i` (where `a_i ∈ k`, `1 ≤ i ≤ n`, the `a_i` being the canonical images of the `t_i` in `A/𝔪`).
Replacing `t_i` by `t_i − a_i`, one sees finally that one is reduced to the case where `𝔪 = ∑_{i=1}^n A t_i`. The
completion of the local ring `A_𝔪` is then the formal series ring `k[[t_1, …, t_n]]`; one knows that it has the same
dimension as `A_𝔪` `(0, 16.2.4)`, and on the other hand, the dimension of `k[[t_1, …, t_n]]` is equal to `n`
`(0, 17.1.4)`; whence the conclusion.

**Corollary (5.2.2).**

<!-- label: IV.5.2.2 -->

*For a prescheme `X` locally of finite type over a field `k`, `dim(X)` coincides with the number defined in `(4.1.1)`.*

Indeed, if `X_α` are the reduced sub-preschemes having as underlying spaces the irreducible components of `X`, one has
`dim(X) = sup_α (dim(X_α))` `(0, 14.1.2.1)` and it suffices to apply `(5.2.1)` to the `X_α`.

**Corollary (5.2.3).**

<!-- label: IV.5.2.3 -->

*Let `X` be a prescheme locally of finite type over a field `k`, `x` a point of `X`. One has*

```text
  dim_x(X) = dim(𝒪_x) + deg.tr_k k(x).                   (5.2.3.1)
```

One knows that there exists an open neighbourhood `U` of `x` in `X` such that `dim_x(X) = dim(U)` `(0, 14.1.4.1)`, and
one may suppose that the irreducible components of `U` are the `X_i ∩ U`, where the `X_i` are the irreducible components
of `X` containing `x`; as `U ∩ X_i`

<!-- original page 91 -->

is dense in `X_i`, it follows from `(4.1.1.3)` that `dim(X_i) = dim(U ∩ X_i)`, so one has
`dim_x(X) = sup_i (dim(X_i))`. Moreover, the minimal prime ideals of `𝒪_x` correspond to the generic points of the
`X_i`, hence `(0, 16.1.1.1)`, one has `dim(𝒪_{X,x}) = sup_i (dim(𝒪_{X_i, x}))`. One is thus reduced to the case where
`X` is irreducible; as `X` is biequidimensional by `(5.2.1)`, one has `dim(X) = dim(‾{x}) + codim(‾{x}, X)`
`(0, 14.3.5.1)`, and one knows that `dim(‾{x}) = deg.tr_k k(x)` by `(5.2.1)` and `codim(‾{x}, X) = dim(𝒪_x)` by
`(5.1.2)`.

**Corollary (5.2.4).**

<!-- label: IV.5.2.4 -->

*Let `X` be a prescheme locally of finite type over a field `k`, `ℒ` an invertible `𝒪_X`-Module, `f` a section of `ℒ`
over `X`, such that the set `Y` of `x ∈ X` for which `f(x) = 0` is rare in `X`. Then one has `dim(Y) ≤ dim(X) − 1`; the
two sides of this inequality are equal if `Y` meets every irreducible component of maximum dimension of `X`.*

If `(X_α)` is the family of irreducible components of `X`, one has

```text
  dim(Y) = sup_α (dim(Y ∩ X_α))
```

and one is therefore reduced to the case where `X` is irreducible (`Y ∩ X_α` being rare in `X_α` since each `X_α` has a
non-empty interior in `X`). One may restrict to the case where `Y ≠ ∅`; then, for every maximal point `x` of `Y`, one
has (since `X` is biequidimensional) `dim(‾{x}) = dim(X) − codim(‾{x}, X)`, and since `Y` is rare in `X`, one has

```text
  codim(‾{x}, X) = 1
```

by `(5.1.8)`; whence the corollary.

**Remarks (5.2.5).**

<!-- label: IV.5.2.5 -->

*(i) Contrary to what happens for algebraic `k`-preschemes, a locally Noetherian prescheme `X` is not necessarily
catenary (cf. `(5.6.11)`); it is, however, if all its local rings `𝒪_x` are quotients of regular rings `(0, 16.5.12)`
and in particular if `X` is regular `(I, 4.1.4)`. Nevertheless, even an (integral) scheme `X = Spec(A)`, where `A` is a
*regular* ring, is not necessarily *biequidimensional*; in other words `(0, 14.3.3)` the codimensions in `X` of the
various closed points of `X` are not necessarily the same. For example, let `B` be a discrete valuation ring,
`𝔪 = Bπ` its maximal ideal, `k = B/𝔪` its residue field, `K` the field of fractions of `B`; let `A` be the polynomial
ring `B[T]`. In `A` there are maximal ideals of height `2`, for example `(π) + (T)`; but there are also maximal ideals
of height `1`, for example the principal ideal `(πT − 1)`: indeed, a principal prime ideal `≠ 0` is of height `1`
`(5.1.8)`; on the other hand `A/(πT − 1)` is isomorphic to the ring of fractions `B_π` `(0_I, 1.2.3)`, which is none
other than `K` here, which proves that the ideal `(πT − 1)` is maximal and of height `1`.*

*(ii) When `X` is a prescheme locally of finite type over a field, one has seen `(4.1.1.3)` that `dim(U) = dim(X)` for
every dense open `U` in `X`. This result does not extend to regular Noetherian preschemes, even if they are
biequidimensional. For example, let `B` be a discrete valuation ring, `𝔪` its maximal ideal; `X = Spec(A)` has two
points, the ideal `(0)` and `𝔪`, the latter being the only closed point; one has `dim(X) = 1`, but the open set
`U = {(0)}` is of dimension `0` (cf. §10).*

<!-- original page 92 -->

### 5.3. Dimension of the support of a Module and Hilbert polynomial

This number uses the results of Chapter III; it will not be used in the sequel of this chapter.

**Proposition (5.3.1).**

<!-- label: IV.5.3.1 -->

*Let `A` be an Artinian local ring, `X` a projective scheme over `Spec(A)`, `ℒ` an invertible `𝒪_X`-Module very ample
relative to `A`, `ℱ` a coherent `𝒪_X`-Module `≠ 0`; set `ℱ(n) = ℱ ⊗_{𝒪_X} ℒ^{⊗n}` for `n ∈ ℤ`. Then the degree of the
Hilbert polynomial `P(n) = χ_A(ℱ(n))` of `ℱ` relative to `A` `(III, 2.5.3)` is equal to the dimension of `Supp(ℱ)`.*

We reason by induction on `d = dim(Supp(ℱ))`. One knows that there exists a closed sub-prescheme `Y` of `X` whose
`Supp(ℱ)` is the underlying space, and an `𝒪_Y`-Module coherent `𝒢` such that `ℱ = j_*(𝒢)`, where `j : Y → X` is the
canonical injection `(Err_III, 30)`. It is immediate that the Hilbert polynomials of `ℱ` and of `𝒢` are the same, so
one may restrict to the case where `X = Supp(ℱ)`. Suppose first `d = 0`; all the points of `X` being closed, `X` is an
Artinian scheme `(I, 6.2.2)`, hence `ℱ(n) = ℱ` for every integer `n`, and one has consequently `(III, 2.5.3)`

```text
  χ_A(ℱ(n)) = long_A(Γ(X, ℱ))
```

for `n` large enough, and the degree of the Hilbert polynomial is therefore `0`. Suppose now `d > 0`, and set
`Z = Ass(ℱ)`, which is a finite set `(3.1.6)`; there exist an integer `m > 0` and a section
`f ∈ Γ(X, ℒ^{⊗m})` such that `X_f` be a neighbourhood of `Z` `(II, 4.5.4)`. Multiplication by `f` is a homomorphism

```text
  μ_f : ℱ → ℱ(m)
```

which is injective `(3.1.8)`; one therefore has an exact sequence

```text
  0 → ℱ ─μ_f→ ℱ(m) → 𝒢 → 0                              (5.3.1.1)
```

where `𝒢` is coherent. By virtue of Nakayama's lemma, the points `x ∈ Supp(𝒢)` are exactly those for which `f(x) = 0`.
We shall deduce from this that one has

```text
  dim(Supp(𝒢)) = d − 1.                                  (5.3.1.2)
```

This will follow from the following lemma:

**Lemma (5.3.1.3).**

<!-- label: IV.5.3.1.3 -->

*Let `A` be an Artinian local ring, `X` a projective scheme over `Spec(A)`, `ℒ` an invertible `𝒪_X`-Module ample
relative to `A`; then, for every section `g` of `ℒ` over `X`, the set `X_g` of `x ∈ X` such that `g(x) = 0` meets every
irreducible component of `X` of dimension `≠ 0`.*

Indeed `(II, 5.5.7)`, the set `X_g` is an affine open of `X`, and if it contains an irreducible component `X'` of `X`,
the reduced closed sub-prescheme of `X` having `X'` as underlying space is at once projective and affine over `A`,
hence finite over `A` `(III, 4.4.2)`, and consequently an Artinian scheme, hence of dimension `0`.

This lemma being established, note that since `Z` contains the maximal points of `X`, `X_f` is dense, hence `Supp(𝒢)`
is rare in `X`, and the relation `(5.3.1.2)` follows from the lemma and from `(5.2.4)`.

<!-- original page 93 -->

This being so, from the exact sequence `(5.3.1.1)` one deduces, for every `n`, the exact sequence

```text
  0 → ℱ(n) → ℱ(n + m) → 𝒢(n) → 0
```

and for `n` large enough, one therefore also has the exact sequence `(III, 2.2.3)`

```text
  0 → Γ(X, ℱ(n)) → Γ(X, ℱ(n + m)) → Γ(X, 𝒢(n)) → 0
```

whence, taking `(III, 2.5.3)` into account, for `n` large enough,

```text
  χ_A(𝒢(n)) = χ_A(ℱ(n + m)) − χ_A(ℱ(n)).
```

As, by virtue of `(5.3.1.2)` and the induction hypothesis, the degree of the polynomial `χ_A(𝒢(n))` is `d − 1`, the
preceding relation entails that the degree of `χ_A(ℱ(n))` is `d`. Q.E.D.

### 5.4. Dimension of the image of a morphism

**Proposition (5.4.1).**

<!-- label: IV.5.4.1 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a morphism.*

*(i) If `f` is quasi-finite, one has `dim(X) ≤ dim(‾{f(X)}) ≤ dim(Y)`.*

*(ii) If `f` is surjective and open (resp. surjective and closed), one has `dim(X) ≥ dim(Y)`.*

(i) One can replace `f` by `f_red` `(II, 6.2.4)`, hence suppose `X` and `Y` reduced; if `Z` is the reduced closed
sub-prescheme of `Y` having as underlying space `‾{f(X)}`, one has then `f = j ∘ g`, where `j : Z → Y` is the canonical
injection and `g : X → Z` is a quasi-finite morphism `(I, 5.2.2 and II, 6.2.4)`. One may therefore restrict to the case
where `f(X)` is dense in `Y`. For every `x ∈ X`, `𝒪_x` is then a quasi-finite `𝒪_{f(x)}`-module `(II, 6.2.2)`, and
consequently `𝔪_{f(x)} 𝒪_x` is an ideal of definition of `𝒪_x` `(0_I, 7.4.4)`; but one knows `(0, 16.3.10)` that if
`A → B` is a local homomorphism of Noetherian local rings such that, if `𝔪` is the maximal ideal of `A`, `𝔪 B` is an
ideal of definition of `B`, then one has `dim(B) ≤ dim(A)`; this completes the proof of (i) by virtue of `(5.1.4)`.

(ii) The definition of dimension `(0, 14.1.2)` shows that it suffices to prove that for every sequence
`(y_i)_{0 ≤ i ≤ n}` of distinct elements of `Y` such that `y_i ∈ ‾{y_{i+1}}` for `0 ≤ i ≤ n − 1`, there exists a
sequence `(x_i)_{0 ≤ i ≤ n}` of points of `X` such that `x_i ∈ ‾{x_{i+1}}` for `0 ≤ i ≤ n − 1` and `f(x_i) = y_i` for
every `i`. Suppose first `f` surjective and open and let us prove the existence of the `x_i` by induction on `i`; the
existence of `x_0 ∈ X` such that `f(x_0) = y_0` follows from the fact that `f` is surjective. If the `x_i` have been
determined for `i ≤ m` so as to satisfy `f(x_i) = y_i` for `i ≤ m` and `x_i ∈ ‾{x_{i+1}}` for `i < m`, one notes that
since `f` is open and `y_{m+1}` a generization of `y_m`, there exists `x_{m+1} ∈ f⁻¹(y_{m+1})` which is a generization
of `x_m` `(1.10.3)` and the induction can proceed.

Suppose now `f` surjective and closed and let us prove the existence of the `x_i` by descending induction on `i`, the
existence of `x_n` such that `f(x_n) = y_n` still resulting from the fact that `f` is surjective. If the `x_i` have been
determined so as to satisfy the desired conditions for `i > m`, one notes that `f(‾{x_{m+1}})` is the closure of
`{f(x_{m+1})} = {y_{m+1}}` since `f`

<!-- original page 94 -->

is closed (Bourbaki, *Top. gén.*, chap. I, 3rd ed., §5, n° 4, prop. 9); there therefore exists `x_m ∈ ‾{x_{m+1}}` such
that `f(x_m) = y_m` and the descending induction can continue.

**Corollary (5.4.2).**

<!-- label: IV.5.4.2 -->

*If `X`, `Y` are two locally Noetherian preschemes, `f : X → Y` a finite morphism (hence closed), one has
`dim(X) = dim(‾{f(X)})`. If moreover `f` is surjective, one has `dim(X) = dim(Y)`.*

**Remarks (5.4.3).**

<!-- label: IV.5.4.3 -->

*(i) One has seen in `(4.1.2)` that if `X` and `Y` are preschemes locally of finite type over a field `k` and `f` a
`k`-morphism, the inequality `dim(Y) ≤ dim(X)` is already verified when `f` is quasi-compact and dominant. On the
contrary, one can have `dim(Y) > dim(X)` even when `f` is of finite type, bijective, and a local immersion, if one only
supposes `X` and `Y` locally Noetherian. For example, let `A` be a discrete valuation ring, `K` its field of fractions,
`k` its residue field; if `Y = Spec(A)`, and if `a` is the generic point of `Y` and `b` its closed point, one has
therefore `k(a) = K`, `k(b) = k`. Let then `X` be the sum prescheme of `Spec(K)` and `Spec(k)`, `f : X → Y` the morphism
which coincides on `Spec(K)` and `Spec(k)` with the respective canonical morphisms `(I, 2.4.5)`; it is clear that `f` is
a bijective local immersion, `{a}` being open in `Y`; on the other hand `f` is of finite type, for `K = A[π⁻¹]`, where
`π` is a uniformizer of `A`, so `K` is an `A`-algebra of finite type. However one has `dim(X) = 0` and `dim(Y) = 1`.*

*(ii) If `A` and `B` are two Noetherian rings such that `A ⊂ B` and that `B` is a finite `A`-algebra, the corollary
`(5.4.2)` shows again that `dim(B) = dim(A)` `(0, 16.1.5)`. Suppose moreover that `A` is a Noetherian local ring; then
`B` is a Noetherian semi-local ring (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 3 of prop. 9); if
`𝔫_i` (`1 ≤ i ≤ r`) are the maximal ideals of `B`, one has therefore*

```text
  dim(A) = sup_i dim(B_{𝔫_i}).                           (5.4.3.1)
```

*One will observe that, under these conditions, one does not necessarily have `dim(B_{𝔫_i}) = dim(A)` for every `i`: it
suffices to see this to replace `B` by the direct product of `B` and the residue field `k` of `A`. But one even has
examples where `A` and `B` are in addition *integral rings of dimension `2`* and where certain of the `B_{𝔫_i}` have
dimension `< dim(A)` `(5.6.11)`. We shall, however, see further on `((5.6.4)` and `(5.6.10))` that this last phenomenon
cannot present itself when one supposes that `A` is a quotient of a regular local ring.*

### 5.5. Dimension formula for a morphism of finite type

**(5.5.1)**

<!-- label: IV.5.5.1 -->

Recall `(0, 16.3.9)` that if `A`, `B` are two Noetherian local rings, `k` the residue field of `A`, `φ : A → B` a local
homomorphism, one has

```text
  dim(B) ≤ dim(A) + dim(B ⊗_A k).                        (5.5.1.1)
```

One deduces:

**Proposition (5.5.2).**

<!-- label: IV.5.5.2 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a morphism, `x` a point of `X`, `y = f(x)`. Then one
has*

```text
  dim(𝒪_x) ≤ dim(𝒪_y) + dim(𝒪_x ⊗_{𝒪_y} k(y)).           (5.5.2.1)
```

<!-- original page 95 -->

In particular, if `x` is a maximal point of the fibre `f⁻¹(y)`, one has

```text
  dim(𝒪_x) ≤ dim(𝒪_y)                                    (5.5.2.2)
```

since `𝒪_x ⊗_{𝒪_y} k(y) = 𝒪_x / 𝔪_y 𝒪_x` is the local ring of `x` in the prescheme `f⁻¹(y)`, and is therefore of
dimension `0` by hypothesis.

We shall obtain a more precise formula than `(5.5.2.1)` when one supposes that `f` is a morphism of finite type.

**Proposition (5.5.3).**

<!-- label: IV.5.5.3 -->

*Let `A` be a Noetherian ring, `T` an indeterminate, `𝔭` a prime ideal of `A`; then `𝔭' = 𝔭 A[T]` is prime in
`B = A[T]` and `𝔭' ∩ A = 𝔭`. There exists an infinity of prime ideals of `B` distinct from `𝔭'` whose intersection with
`A` is `𝔭`; these ideals are pairwise without inclusion relation. Moreover, if `𝔮` is such an ideal, one has*

```text
  dim(B_𝔮) = dim(B_{𝔭'}) + 1 = dim(A_𝔭) + 1.             (5.5.3.1)
```

In the first assertions, one reduces at once, by replacing `A` by `A/𝔭` and observing that
`A[T]/𝔭 A[T] = (A/𝔭)[T]`, to the case `𝔭 = 0`; they then follow from the fact that the prime ideals of `B = A[T]` whose
intersection with `A` reduces to `0` are exactly those which do not meet the multiplicative part `S = A − {0}` of the
integral ring `A`; now one knows that there is an increasing bijection of the set of these ideals onto the set of prime
ideals of `S⁻¹A[T] = K[T]`, where `K` is the field of fractions of `A` (Bourbaki, *Alg. comm.*, chap. II, §2, n° 5,
prop. 11). Moreover, one has, according to `(5.5.1.2)`, `dim(B_𝔮) ≤ dim(A_𝔭) + dim(B_𝔮/𝔭 B_𝔮)`, and if `k` is the field
of fractions of `A/𝔭`, `B_𝔮/𝔭 B_𝔮` is canonically identified with `(k[T])_𝔮`, hence is a discrete valuation ring, so of
dimension `1`. Finally, if `𝔭 = 𝔭_0 ⊃ 𝔭_1 ⊃ ⋯ ⊃ 𝔭_m` is a chain of prime ideals of `A` of maximum length, the ideals
`𝔭_j B` (`0 ≤ j ≤ m`) are prime in `B`, pairwise distinct, and contained in `𝔮`; hence `dim(B_𝔮) ≥ m + 1 = dim(A_𝔭) + 1`
and consequently `dim(B_𝔮) = dim(A_𝔭) + 1`. This relation can also be written `ht(𝔮) = ht(𝔭) + 1`; as `𝔮 ≠ 𝔭'`, one has
moreover `ht(𝔮) ≥ ht(𝔭') + 1 ≥ ht(𝔭) + 1` by definition of the height of a prime ideal; this completes the proof of
`(5.5.3.1)`.

**Corollary (5.5.4).**

<!-- label: IV.5.5.4 -->

*For every Noetherian ring `A`, one has*

```text
  dim(A[T_1, …, T_r]) = dim(A) + r                       (5.5.4.1)
```

*(`T_i` indeterminates).*

One will note, on the other hand, that there are examples of non-Noetherian local rings `A` such that `dim(A) = 1` and
`dim(A[T]) = 3` `[30]`.

**Corollary (5.5.5).**

<!-- label: IV.5.5.5 -->

*For every locally Noetherian prescheme `X`, the dimension of `X[T_1, …, T_r] = X ⊗_ℤ ℤ[T_1, …, T_r]` (`T_i`
indeterminates) is `dim(X) + r`.*

This follows from `(5.5.4)` and `(0, 14.1.7)`.

**Corollary (5.5.6).**

<!-- label: IV.5.5.6 -->

*Under the hypotheses of `(5.5.3)`, let `𝔮` be a prime ideal of `B = A[T]` such that `𝔮 ∩ A = 𝔭`; if `k` and `k'` are
the residue fields of `A_𝔭` and `B_𝔮` respectively, one has*

```text
  dim(A_𝔭) + 1 = dim(B_𝔮) + deg.tr_k k'.                 (5.5.6.1)
```

<!-- original page 96 -->

If `𝔮 = 𝔭 B`, one has, according to `(5.5.3.1)`, `dim(B_𝔮) = dim(A_𝔭)`, and in this case `k' = k(T)`, hence the formula
`(5.5.6.1)` is indeed verified. In the contrary case, `dim(B_𝔮) = dim(A_𝔭) + 1`, and as `𝔮` corresponds to a prime ideal
`𝔮' ≠ 0` of `k[T]`, `k'` is an algebraic extension of `k`, so one still has the formula `(5.5.6.1)`.

**Lemma (5.5.7).**

<!-- label: IV.5.5.7 -->

*Let `A` be an integral Noetherian local ring, `𝔪` its maximal ideal, `k` its residue field.*

*(i) For every integral ring `B` containing `A`, such that `B = A[x]` (for some `x ∈ B`) and every prime ideal `𝔮` of
`B` such that `𝔮 ∩ A = 𝔪`, one has*

```text
  dim(A) + deg.tr_A B ≥ dim(B_𝔮) + deg.tr_k k'           (5.5.7.1)
```

*denoting by `k'` the residue field of `B_𝔮` and by `deg.tr_A B` the transcendence degree of the field of fractions of
`B` over that of `A`.*

*(ii) Suppose that for every maximal ideal `𝔫` of `A[T]` such that `𝔫 ∩ A = 𝔪`, the ring `(A[T])_𝔫` is catenary; then
the two sides of `(5.5.7.1)` are equal.*

(i) If `x` is transcendent over the field of fractions of `A`, one has `deg.tr_A B = 1` and the two sides of `(5.5.7)`
are equal by virtue of `(5.5.6)`. In the contrary case, one has `B = A[T]/𝔭`, where `𝔭` is a prime ideal `≠ 0` of
`A[T]`, such that `𝔭 ∩ A = 0` since `B` contains `A`; one therefore has `ht(𝔭) = 1` by virtue of `(5.5.3)`. The ideal
`𝔮` of `B` is of the form `𝔫/𝔭`, where `𝔫 ⊃ 𝔭` is a prime ideal of `A[T]` such that `𝔫 ∩ A = 𝔪`, and one has
`B_𝔮 = (A[T])_𝔫 / 𝔭 (A[T])_𝔫`; the formula `(0, 16.1.4.1)`, applied to `X = Spec((A[T])_𝔫)` and to `Y = Spec(B_𝔮)`,
gives

```text
  dim((A[T])_𝔫) ≥ ht(𝔭 (A[T])_𝔫) + dim(B_𝔮) = 1 + dim(B_𝔮)     (5.5.7.2)
```

since `ht(𝔭 (A[T])_𝔫) = ht(𝔭) = 1` by virtue of the bijective correspondence between prime ideals of `A[T]` contained in
`𝔫` and prime ideals of `(A[T])_𝔫`. Finally, the formula `(5.5.6.1)` gives

```text
  dim((A[T])_𝔫) = dim(A) + 1 − deg.tr_k k'               (5.5.7.3)
```

since the residue fields of `B_𝔮` and of `(A[T])_𝔫` are the same; on the other hand, one has then
`deg.tr_A B = 0`, which completes the proof of `(5.5.7.1)`.

(ii) If `(A[T])_𝔫` is catenary, the two sides of `(5.5.7.2)` are equal `(0, 16.1.4)`, hence also the two sides of
`(5.5.7.1)`.

**Theorem (5.5.8) (dimension formula).**

<!-- label: IV.5.5.8 -->

*Let `A` be an integral Noetherian local ring, `B` an integral ring containing `A` which is an `A`-algebra of finite
type, `𝔮` a prime ideal of `B` such that `𝔮 ∩ A` is the maximal ideal `𝔪` of `A`, `k` and `k'` the residue fields of `A`
and `B_𝔮` respectively. One then has the inequality*

```text
  dim(A) + deg.tr_A B ≥ dim(B_𝔮) + deg.tr_k k'.          (5.5.8.1)
```

*Moreover the two sides are equal if, for every sub-`A`-algebra `A'` of finite type of `B[T]` and every maximal ideal
`𝔪'` of `A'` such that `𝔪' ∩ A = 𝔪`, `A'_{𝔪'}` is catenary.*

Let `B = A[x_1, …, x_n]` and let us reason by induction on `n`. Set `C = A[x_1, …, x_{n−1}]` and `𝔯 = 𝔮 ∩ C`; `C_𝔯` is
an integral Noetherian local ring, and if one sets `S = C − 𝔯`, `B' = S⁻¹ B`, `𝔮' = S⁻¹ 𝔮`, one has `B_𝔮 = B'_{𝔮'}`,
`B' = C_𝔯[x_n]` and `𝔮' ∩ C_𝔯 = 𝔯 C_𝔯`; in addition the fields of fractions

<!-- original page 97 -->

of `B'` and `C_𝔯` are those of `B` and `C` respectively. If `k_1` is the residue field of `C_𝔯`, one has therefore,
according to `(5.5.7.1)`,

```text
  dim(C_𝔯) + deg.tr_C B ≥ dim(B_𝔮) + deg.tr_{k_1} k'.    (5.5.8.2)
```

On the other hand, the induction hypothesis gives

```text
  dim(A) + deg.tr_A C ≥ dim(C_𝔯) + deg.tr_k k_1          (5.5.8.3)
```

whence `(5.5.8.1)` by adding `(5.5.8.2)` and `(5.5.8.3)` term by term. To prove the second assertion, note first that
every sub-`A`-algebra of finite type of `C[T]` is also a sub-`A`-algebra of finite type of `B[T]`; by induction on `n`,
one may therefore suppose that the two sides of `(5.5.8.3)` are equal. On the other hand, to see that the two sides of
`(5.5.8.2)` are equal, it suffices, by virtue of `(5.5.7)`, to verify that if `𝔫` is a maximal ideal of `C_𝔯[T]` such
that `𝔫 ∩ C_𝔯 = 𝔯 C_𝔯`, then `(C_𝔯[T])_𝔫` is catenary; but one has `C_𝔯[T] = S'⁻¹ C[T]` where `S' = C − 𝔯`; the ideal
`𝔫` is therefore of the form `S'⁻¹ 𝔫'`, where `𝔫'` is a prime ideal of `C[T]` such that `𝔫' ∩ C = 𝔯`, whence
`(C_𝔯[T])_𝔫 = (C[T])_{𝔫'}`; if `𝔪'` is a maximal ideal of `C[T]` containing `𝔫'`, `(C[T])_{𝔫'}` is therefore a local
ring of the ring `(C[T])_{𝔪'}`, and as by hypothesis this latter is catenary, so is `(C[T])_{𝔫'}` `(0, 16.1.4)`.

### 5.6. Dimension formula and universally catenary rings

**Proposition (5.6.1).**

<!-- label: IV.5.6.1 -->

*Let `A` be a Noetherian ring. The following properties are equivalent:*

*a) Every polynomial ring `A[T_1, …, T_n]` is catenary.*

*b) Every algebra of finite type over `A` is catenary.*

*c) `A` is catenary, and for every integral local `A`-algebra essentially of finite type `(1.3.8)` `B'`, one has,
denoting by `𝔭` the inverse image in `A` of the maximal ideal `𝔮` of `B'`, by `A'` the image of `A_𝔭` in `B'`, by `k`
and `k'` the residue fields of `A'` and `B'` respectively,*

```text
  dim(A') + deg.tr_{A'}(B') = dim(B') + deg.tr_k k'.     (5.6.1.1)
```

The fact that b) entails c) follows from `(5.5.8)`; indeed, `B'` is a local `A'`-algebra essentially of finite type
`(1.3.10)`, hence of the form `B''_{𝔮''}`, where `B''` is a sub-`A'`-algebra of finite type of `B'`, `𝔮''` a prime ideal
of `B''` above the maximal ideal `𝔭'` of `A'`; moreover the fields of fractions of `B'` and `B''` are the same, hence
`deg.tr_{A'}(B') = deg.tr_{A'}(B'')`. To prove `(5.6.1.1)`, it suffices to show that (under hypothesis b)) every
sub-`A'`-algebra `A_1` of finite type of `B'[T]` is catenary; indeed the two sides of `(5.5.8.1)`, where one replaces
`A`, `B`, and `𝔮` by `A'`, `B''`, and `𝔮''`, will then be equal, whence the equality `(5.6.1.1)`. Now the hypothesis b)
entails that every `A`-algebra essentially of finite type is catenary `(0, 16.1.4)`, and `A_1` is such an `A`-algebra
`(1.3.9)`.

It is trivial that b) entails a); conversely, a) entails b), every `A`-algebra of finite type being a quotient of a
polynomial algebra `(0, 16.1.4)`.

It remains to prove that c) entails b). Since every quotient by a prime ideal

<!-- original page 98 -->

of an `A`-algebra of finite type is an integral `A`-algebra of finite type, it amounts to seeing that, if `B` is an
integral `A`-algebra of finite type, `𝔮` and `𝔮'` two prime ideals of `B` such that `𝔮' ⊂ 𝔮`, one has `(0, 16.1.4.2)`

```text
  dim(B_𝔮 / 𝔮' B_𝔮) + dim(B_{𝔮'}) = dim(B_𝔮).            (5.6.1.2)
```

Let `𝔭`, `𝔭'` be the inverse images of `𝔮`, `𝔮'` respectively in `A`, `𝔫` the kernel of the homomorphism
`A_𝔭 → B_𝔮`.

The image `A'` of `A_𝔭` in `B_𝔮` being isomorphic to `A_𝔭/𝔫`, the formula `(5.6.1.1)` applied to `A'` and to
`B' = B_𝔮` is written

```text
  dim(A_𝔭/𝔫) + deg.tr_{A'}(B_𝔮) = dim(B_𝔮) + deg.tr_{k(𝔭)} k(𝔮).  (5.6.1.3)
```

On the other hand, the kernel of `A_{𝔭'} → B_{𝔮'}` is `𝔫 A_{𝔭'}`, hence, applying the formula `(5.6.1.1)` where one
replaces `A'` by `A_{𝔭'} / 𝔫 A_{𝔭'}` and `B'` by `B_{𝔮'}`, one has

```text
  dim(A_{𝔭'} / 𝔫 A_{𝔭'}) + deg.tr_{A_{𝔭'} / 𝔫 A_{𝔭'}} (B_{𝔮'})
        = dim(B_{𝔮'}) + deg.tr_{k(𝔭')} k(𝔮').            (5.6.1.4)
```

Finally, `B/𝔮'` is an integral `A`-algebra of finite type, the inverse image of `𝔮/𝔮'` in `A` is `𝔭`, and the kernel of
the homomorphism `A_𝔭 → B_𝔮 / 𝔮' B_𝔮` is `𝔭' A_𝔭`, hence, applying `(5.6.1.1)` where one replaces `A'` by
`A_𝔭 / 𝔭' A_𝔭` and `B'` by `B_𝔮 / 𝔮' B_𝔮`, one has

```text
  dim(A_𝔭/𝔭' A_𝔭) + deg.tr_{k(𝔭')}(B_𝔮 / 𝔮' B_𝔮)
        = dim(B_𝔮 / 𝔮' B_𝔮) + deg.tr_{k(𝔭)} k(𝔮).        (5.6.1.5)
```

Let us now add `(5.6.1.4)` and `(5.6.1.5)` term by term, and note that `k(𝔭')` (resp. `k(𝔮')`) is the field of fractions
of `A_𝔭/𝔭' A_𝔭` (resp. `B_𝔮/𝔮' B_𝔮`); on the other hand `A_{𝔭'} / 𝔫 A_{𝔭'}` and `A_𝔭/𝔫` have the same field of
fractions, and `B_{𝔮'}` and `B_𝔮` have the same field of fractions; finally, since `A` is supposed catenary, one has
`(0, 16.1.4.2)`

```text
  dim(A_𝔭 / 𝔭' A_𝔭) + dim(A_{𝔭'} / 𝔫 A_{𝔭'}) = dim(A_𝔭/𝔫).
```

Taking these remarks and `(5.6.1.3)` into account, the relation `(5.6.1.2)` follows. Q.E.D.

**Definition (5.6.2).**

<!-- label: IV.5.6.2 -->

*One says that a Noetherian ring `A` is **universally catenary** if it verifies the equivalent conditions a), b), c) of
`(5.6.1)`.*

**Remarks (5.6.3).**

<!-- label: IV.5.6.3 -->

*(i) If `A` is universally catenary, so is `S⁻¹A` for every multiplicative part `S` of `A`, as follows at once from
`(5.6.1, a))` and from the fact that every ring of fractions of a catenary ring is catenary. Conversely, if, for every
prime ideal `𝔭` of `A`, the ring `A_𝔭` is universally catenary, then `A` is universally catenary: this follows from
`(5.6.1, c))`, if one notes that setting `S = A − 𝔭`, `S⁻¹ B` is an `A_𝔭`-algebra of finite type, and
`B_𝔮 = (S⁻¹ B)_{S⁻¹ 𝔮}`.*

*(ii) One says that a locally Noetherian prescheme `X` is **universally catenary** if, for every `x ∈ X`, the ring
`𝒪_x` is universally catenary. It follows from (i) that for `A` to be a universally catenary ring, it is necessary and
sufficient that the scheme `Spec(A)` be so.*

*(iii) The criterion `(5.6.1, c))` involves only the images of `A` in integral `A`-algebras of finite type, hence
integral quotient rings of `A`. One concludes that if*

<!-- original page 99 -->

*`𝔭_i` (`1 ≤ i ≤ n`) are the minimal prime ideals of `A`, it amounts to the same to say that `A` is universally
catenary or that each of the `A/𝔭_i` is so. This also shows that it amounts to the same to say that a locally
Noetherian prescheme `X` is universally catenary, or that `X_red` is so.*

*(iv) The criterion `(5.6.1, b))` and the remark (i) show that, if `A` is a universally catenary ring, so is every
`A`-algebra essentially of finite type `(1.3.8)`.*

**Proposition (5.6.4).**

<!-- label: IV.5.6.4 -->

*Every quotient ring of a regular ring is universally catenary.*

It all comes down to seeing that a regular ring `A` is universally catenary `(5.6.3, (iv))`; now, one knows that
`A[T_1, …, T_n]` is regular `(0, 17.3.7)`, hence catenary `(0, 16.5.12)`, and one concludes by `(5.6.1, a))`.

In particular, it follows from Cohen's theorem `(0, 19.8.8)` that every complete Noetherian local ring is universally
catenary. Likewise, every algebra of finite type over a field being a quotient of a regular ring, every prescheme
locally of finite type over a field is universally catenary.

We shall see further on `(6.3.7)` that in `(5.6.4)`, one can replace "regular ring" by "Cohen-Macaulay ring".

**Proposition (5.6.5).**

<!-- label: IV.5.6.5 -->

*Let `Y` be an irreducible locally Noetherian prescheme, `X` an irreducible prescheme, `f : X → Y` a dominant morphism
locally of finite type. Let `ξ` (resp. `η`) be the generic point of `X` (resp. `Y`), and let
`e = dim(f⁻¹(η)) = deg.tr_{k(η)} k(ξ)` ("dimension of the generic fibre", cf. `(0_I, 2.1.8)` and `(4.1.1)`). For every
`x ∈ X`, one has then, setting `y = f(x)`,*

```text
  e + dim(𝒪_y) ≥ deg.tr_k(y) k(x) + dim(𝒪_x)             (5.6.5.1)

  dim(𝒪_x) ≤ dim(𝒪_y) + dim(𝒪_x ⊗_{𝒪_y} k(y)) − δ(x)    (5.6.5.2)
```

*setting `δ(x) = dim_x(f⁻¹(y)) − e`.*

*Moreover, if `Y` is universally catenary, the two sides of `(5.6.5.1)` (resp. `(5.6.5.2)`) are equal. If moreover `x`
is closed in `f⁻¹(y)`, one has*

```text
  dim(𝒪_x) = dim(𝒪_y) + e.                               (5.6.5.3)
```

One may evidently restrict to the case where `X` and `Y` are affine (hence `f` of finite type) and reduced `(I, 5.4)`,
hence integral. As `f` is dominant, `𝒪_y` is then identified with a sub-ring of `𝒪_x`, and the respective fields of
fractions of `𝒪_y` and `𝒪_x` with `k(η)` and `k(ξ)` `(I, 8.2.7)`; moreover, `𝒪_x` is a local ring of an integral
`𝒪_y`-algebra of finite type `B` at a prime ideal `𝔮` `(I, 3.6.5)`; applying `(5.5.8.1)` to `A = 𝒪_y`, `B`, and `𝔮`, one
obtains `(5.6.5.1)`. Moreover, `𝒪_x ⊗_{𝒪_y} k(y) = 𝒪_x / 𝔪_y 𝒪_x` is none other than the local ring of the fibre
`f⁻¹(y)` at the point `x` `(I, 3.6.1)`; as `f⁻¹(y)` is a prescheme of finite type over `k(y)`, it follows from `(5.2.3)`
that one has

```text
  dim(𝒪_x ⊗_{𝒪_y} k(y)) = dim_x(f⁻¹(y)) − deg.tr_{k(y)} k(x);
```

the inequality `(5.6.5.2)` is therefore only another form of `(5.6.5.1)`.

The fact that the two sides of `(5.6.5.1)` are equal when `Y` is universally

<!-- original page 100 -->

catenary is none other than the equality `(5.6.1.1)`, applied to `A = 𝒪_y` and `B' = 𝒪_x`. To prove that one moreover
has `(5.6.5.3)` when `x` is closed in `f⁻¹(y)`, it suffices to note that, in general, `deg.tr_{k(y)} k(x)` is the
dimension of `‾{x} ∩ f⁻¹(y)`, as follows from `(5.2.1)` applied to the reduced closed sub-prescheme of `f⁻¹(y)` having
this sub-space as underlying space.

We shall prove further on `(13.1.1)` that, under the conditions of `(5.6.5)`, one *always* has `δ(x) ≥ 0`, and
`(5.6.5.2)` therefore in this case makes `(5.5.2.1)` more precise.

**Corollary (5.6.6).**

<!-- label: IV.5.6.6 -->

*Under the general hypotheses of `(5.6.5)`, one has*

```text
  dim(X) ≤ dim(Y) + e.                                   (5.6.6.1)
```

*If one supposes moreover `Y` universally catenary, then, for the two sides of `(5.6.6.1)` to be equal, it is necessary
and sufficient that one have*

```text
  dim(Y) = sup_{y ∈ f(X)} dim(𝒪_y).                      (5.6.6.2)
```

*In particular, the two sides of `(5.6.6.1)` are equal when `Y` is locally of finite type over a field.*

The inequality `(5.6.6.1)` indeed follows from `(5.6.5.1)` applied at a closed point `x` of `X`, taking `(5.1.4.2)` and
`(5.1.11)` into account. On the other hand, every non-empty fibre `f⁻¹(y)` contains a point `x` closed in this fibre
`(5.1.11)`, and if one supposes `Y` universally catenary, one has at this point the relation `(5.6.5.3)`. Taking the
upper bounds of the two sides of `(5.6.5.3)` as `x` runs through `X`, and noting that every point `x` closed in `X` is
*a fortiori* closed in `f⁻¹(f(x))`, the second assertion of the corollary follows from `(5.1.4.1)` and `(5.1.4.2)`.

To prove the last assertion, note that there is an affine open neighbourhood `U` of the generic point of `X` such that
`f|U` be of finite type, hence `f(U)` is a constructible part of `Y`, dense in `Y` `(1.8.5)`, and consequently contains
a non-empty open part (hence everywhere dense) of `Y` `(0_III, 9.2.2)`. The hypothesis that `Y` is locally of finite
type over a field then ensures, on the one hand, that `Y` is universally catenary `(5.6.4)`, and on the other hand that
the two sides of `(5.6.6.2)` are equal `(5.2.2` and `4.1.1.3)`.

One will note that the condition `(5.6.6.2)` is trivially verified when `f` is surjective.

**Corollary (5.6.7).**

<!-- label: IV.5.6.7 -->

*Let `Y` be a locally Noetherian prescheme, `f : X → Y` a morphism locally of finite type, `n` an integer. If, for
every `y ∈ Y`, `dim(f⁻¹(y)) ≤ n`, then one has*

```text
  dim(X) ≤ dim(Y) + n.                                   (5.6.7.1)
```

By virtue of `(0, 14.1.7)` and `(1.5.4)`, one may restrict to the case where `X` and `Y` are affine, hence `f` of finite
type, `X` and `Y` reduced; let `X_i` (`1 ≤ i ≤ m`) be the closed (integral) sub-preschemes of `X` having as underlying
spaces the irreducible components of `X`; one has `dim(X) = sup_i (dim(X_i))`. If `Z_i` is the reduced closed
sub-prescheme of `Y` having as underlying space `‾{f(X_i)}`, `Z_i` is integral `(0_I, 2.1.5)`; the restriction
`X_i → Y` of `f` factors as `X_i ─g_i→ Z_i ─j_i→ Y`, where `j_i` is the canonical injection `(I, 5.2.2)`, and `g_i` is
dominant

<!-- original page 101 -->

and of finite type `(1.5.4)`. One has `dim(Z_i) ≤ dim(Y)` for every `i`; on the other hand, if `ζ_i` is the generic
point of `Z_i`, one has `dim(g_i⁻¹(ζ_i)) ≤ n` for every `i` by hypothesis; one sees thus that to prove `(5.6.7.1)`, it
suffices to show that `dim(X_i) ≤ dim(Z_i) + n` for every `i`, which follows from `(5.6.6.1)`.

**Corollary (5.6.8).**

<!-- label: IV.5.6.8 -->

*Let `Y` be a locally Noetherian prescheme, `X` an irreducible prescheme, `f : X → Y` a morphism locally of finite
type, `n` an integer `≥ 0`. Suppose that `Y` is universally catenary, and that for every `y ∈ Y`, one has
`dim(f⁻¹(y)) ≥ n` (resp. `dim(f⁻¹(y)) = n`). Then one has*

```text
  dim(X) ≥ dim(Y) + n                                    (5.6.8.1)
```

*(resp.*

```text
  dim(X) = dim(Y) + n).                                  (5.6.8.2)
```

As `n ≥ 0`, the hypothesis entails that `f` is surjective, hence `Y` irreducible; moreover, if `η` is the generic point
of `Y`, one has `dim(f⁻¹(η)) ≥ n` (resp. `dim(f⁻¹(η)) = n`). The conclusion therefore follows from `(5.6.6)`.

**Remarks (5.6.9).**

<!-- label: IV.5.6.9 -->

*(i) Even if `Y` is regular, `X` irreducible, `f : X → Y` dominant and of finite type, the two sides of `(5.6.6.1)` are
not necessarily equal, as shown by the example where `Y = Spec(A)` where `A` is a discrete valuation ring,
`X = Spec(K)` where `K` is the field of fractions of `A`, `f` being the canonical morphism.*

*(ii) The example `(5.4.3, (i))` shows that in `(5.6.6)` and `(5.6.8)`, one cannot suppress the hypothesis that `X` is
irreducible, the other hypotheses being verified. We shall, however, see `(10.6.1)` that with supplementary
hypotheses on `Y`, verified for example when `Y` is a prescheme locally of finite type over a field, or over a
Dedekind ring having an infinity of prime ideals, such phenomena cannot present themselves.*

**Proposition (5.6.10).**

<!-- label: IV.5.6.10 -->

*Let `A` be an integral universally catenary Noetherian local ring, `B` an integral ring containing `A` which is a
finite `A`-algebra. Then, for every maximal ideal `𝔫` of `B`, one has `dim(B_𝔫) = dim(A)`.*

Indeed, one has `deg.tr_A B = 0` and the residue field `k'` of `B_𝔫` is an algebraic extension of the field of
fractions of `A`. The conclusion follows from the formula `(5.6.1.1)`, every maximal ideal of `B` being above that of
`A`.

**Example (5.6.11).**

<!-- label: IV.5.6.11 -->

*Let `A` be an integral Noetherian local ring and integrally closed; then one has seen `(0, 16.1.6)` that the
conclusion of `(5.6.10)` is valid for every finite integral `A`-algebra `B` containing `A`. On the contrary, we shall
construct an example of an integral catenary Noetherian local ring `A` for which the conclusion of `(5.6.10)` will be
in default. We shall use the construction of `(5.2.5, (i))`. Let `k_0` be a field, `k` a pure transcendental extension
`k_0(S_i)_{i ∈ ℕ}` of infinite transcendence degree, `V` the discrete valuation ring `k[S]_{(S)}`, local ring of the
polynomial ring `k[S]` at the prime ideal `(S)`; finally let `E` be the polynomial ring `V[T]`; one has seen that in
`E` the maximal ideal `𝔪 = (S) + (T)` is of height `2` and the maximal ideal `𝔪' = (ST − 1)` of height `1`;*

<!-- original page 102 -->

*the corresponding residue fields are `k(𝔪) = k` and `k(𝔪') = k(S)`, field of fractions of `V`; by virtue of the choice
of `k`, these fields are isomorphic. Denote by `ε` and `ε'` the canonical homomorphisms of `E` onto `E/𝔪 = k(𝔪)` and
`E/𝔪' = k(𝔪')` respectively; let on the other hand `σ` be an isomorphism of `k(𝔪)` onto `k(𝔪')`, and consider the
sub-ring `C` of `E` formed by `x ∈ E` such that `ε'(x) = σ(ε(x))` (this construction is a particular case of the
"gluing procedures" which will be studied systematically in Chap. V). It is immediate that `𝔫 = 𝔪 𝔪' = 𝔪 ∩ 𝔪'` is a
maximal ideal of `C`, `C/𝔪 𝔪'` being identified with the sub-field of `(E/𝔪) × (E/𝔪')` formed by pairs `(z, σ(z))`. One
has `E = C + C(ST − 1)`, in other words `E` is a finite `C`-algebra and is evidently the integral closure of `C`; we
shall see in addition that `C` is Noetherian: this will follow from the following lemma:*

**Lemma (5.6.11.1).**

<!-- label: IV.5.6.11.1 -->

*Let `R` be a ring, `S` a sub-ring, `𝔎 = Ann_S(R/S)` the **conductor** of `S` in `R` (largest ideal of `S` which is also
an ideal of `R`).*

*(i) For every ideal `𝔍 ⊂ 𝔎` of `R`, there exists a strictly increasing map of the set of ideals `𝔞` of `S` such that
`R · 𝔞 = 𝔍` to the set of sub-`(S/𝔎)`-modules of `𝔍/𝔎 𝔍`.*

*(ii) If `S/𝔎` and `R` are Noetherian and if `R` is an `S`-module of finite type, then every increasing sequence of
ideals of `S` contained in `𝔎` is stationary.*

(i) One has indeed, `𝔎 𝔍 = 𝔎(R · 𝔞) = 𝔎 𝔞 ⊂ 𝔞` (`𝔞` being an ideal of `S`), whence the conclusion.

(ii) Let `(𝔏_n)` be an increasing sequence of ideals of `S` contained in `𝔎`. The sequence of ideals `R · 𝔏_n` of `R` is
stationary since `R` is Noetherian; one may therefore suppose that all the ideals `R · 𝔏_n` are equal to the same ideal
`𝔍` of `R`. As `R` is Noetherian, `𝔍/𝔎 𝔍` is an `R`-module of finite type, hence also an `S`-module of finite type, and
consequently an `(S/𝔎)`-module of finite type. But since `S/𝔎` is Noetherian, `𝔍/𝔎 𝔍` is an `(S/𝔎)`-Noetherian module,
and the conclusion follows from (i).

We shall apply this lemma taking `R = E`, `S = C`; it is clear that `𝔫` is the conductor of `C` in `E`; moreover, for
every ideal `𝔞` of `C`, `𝔞/(𝔫 ∩ 𝔞)` is isomorphic to `(𝔞 + 𝔫)/𝔫`, hence a sub-`C`-module of `C/𝔫`, which is a simple
`C`-module; it therefore suffices to show that every ideal `𝔞 ⊂ 𝔫` of `C` is of finite type, and this follows from
`(5.6.11.1)`.

It follows from `(0, 16.1.5)` that one has `dim(C) = dim(E) = 2`. Take `A = C_𝔫`; if `U = C − 𝔫`, the ring of fractions
`B = U⁻¹ E` is therefore the integral closure of `A`, and is an `A`-module of finite type; moreover, as `𝔪` and `𝔪'`
are the only prime ideals of `E` containing `𝔫`, `B` is a semi-local ring whose local rings at the two maximal ideals
are isomorphic to `E_𝔪` and `E_{𝔪'}` respectively, hence are respectively of dimension `2` and `1`. This shows that
`dim(B) = 2`, so also `dim(A) = 2` `(0, 16.1.5)`. As `A` is an integral local ring, it is necessarily catenary (every
prime ideal distinct from `0` and from the maximal ideal being necessarily of height `1`); but it does not verify the
conclusion of `(5.6.10)`, and *a fortiori* is not universally catenary.

Note further that `𝔫` is an ideal of height `2` in `C`, and that for every prime ideal `𝔭` of height `1` in `C`, there
exists a unique prime ideal `𝔭'` of `E` above `𝔭`, necessarily of height `1`, and such that `C_𝔭 = E_{𝔭'}`. Indeed,
there is at least one prime ideal `𝔭'` of `E` above `𝔭` and it follows from the Cohen-Seidenberg theorem that such

<!-- original page 103 -->

an ideal is necessarily of height `1`; moreover, as `E` is a finite `C`-algebra and `𝔭 ≠ 𝔫`, `C_𝔭` is integrally closed
(Bourbaki, *Alg. comm.*, chap. V, §1, n° 5, cor. 5 of prop. 16), hence `E_𝔭 = C_𝔭`, which proves our assertions.

It would be interesting to know whether every integral Noetherian local ring verifying the conclusion of `(5.6.10)` is
universally catenary; this is what Nagata `[33]` affirmed, but his proof does not seem to be complete.

### 5.7. Depth and property `(S_n)`

**Definition (5.7.1).**

<!-- label: IV.5.7.1 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module. One calls **depth** (resp. **codepth**) of `ℱ`
at a point `x ∈ X` the number `prof(ℱ_x)` (resp. `coprof(ℱ_x)`) `(0, 16.4.5 and 16.4.9)`. One calls **codepth** of `ℱ`
the number*

```text
  coprof(ℱ) = sup_{x ∈ X} coprof(ℱ_x).                   (5.7.1.1)
```

One says that `ℱ` is a **Cohen-Macaulay `𝒪_X`-Module at `x`** if `ℱ_x` is a Cohen-Macaulay `𝒪_x`-module, that is to say
`(0, 16.5.1)` if `coprof(ℱ_x) = 0`. One says that `ℱ` is a **Cohen-Macaulay `𝒪_X`-Module** if it is so at every point,
in other words if `coprof(ℱ) = 0`. A point `x ∈ X` such that `𝒪_x` is a Cohen-Macaulay ring is also called a
**Cohen-Macaulay point** of `X`.

One calls **codepth of `X`** and denotes by `coprof(X)` the number `coprof(𝒪_X)`. One says that `X` is a
**Cohen-Macaulay prescheme** if `𝒪_X` is a Cohen-Macaulay `𝒪_X`-Module, in other words if `coprof(X) = 0`. Every
locally Noetherian prescheme of dimension `0` is evidently a Cohen-Macaulay prescheme. To say that `Spec(A)` is a
Cohen-Macaulay scheme means that `A` is a Cohen-Macaulay ring `(0, 16.5.13)`.

**Definition (5.7.2).**

<!-- label: IV.5.7.2 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module, `k` a positive or negative integer. One says
that `ℱ` possesses the property `(S_k)` if, for every `x ∈ X`, one has*

```text
  prof(ℱ_x) ≥ inf(k, dim(ℱ_x)).                          (5.7.2.1)
```

*One says that `ℱ` possesses the property `(S_k)` **at a point `x ∈ X`** if, for every generization `x'` of `x` in `X`,
one has*

```text
  prof(ℱ_{x'}) ≥ inf(k, dim(ℱ_{x'})).                    (5.7.2.2)
```

One says that `X` *verifies* the property `(S_k)` (resp. *verifies the property `(S_k)` at a point `x`*) if `𝒪_X`
verifies the property `(S_k)` (resp. verifies the property `(S_k)` at the point `x`).

For `ℱ` to verify the property `(S_k)`, it is evidently necessary and sufficient that it verify it at every point of
`X`. If `U` is an open of `X` and if `ℱ` verifies `(S_k)`, so does `ℱ|U`; conversely, if `(U_α)` is an open cover of
`X` and if `ℱ|U_α` verifies `(S_k)` for every `α`, `ℱ` verifies `(S_k)`.

**Remarks (5.7.3).**

<!-- label: IV.5.7.3 -->

*(i) Recall that one always has `prof(ℱ_x) ≤ dim(ℱ_x)` `(0, 16.4.5.1)` if `ℱ_x ≠ 0`. To say that `ℱ` possesses the
property `(S_k)` therefore means that one has `prof(ℱ_x) ≥ k` except at points `x ∈ X` such that `dim(ℱ_x) < k` and
that at these latter points one has `dim(ℱ_x) = prof(ℱ_x)`, that is to say `(0, 16.5.1)` that `ℱ` is a Cohen-Macaulay
`𝒪_x`-Module at these points; one will note that at points where `dim(ℱ_x) = k`, one has `prof(ℱ_x) = k`,*

<!-- original page 104 -->

*hence `ℱ` is again a Cohen-Macaulay `𝒪_x`-Module at these points. To say that `ℱ` possesses the property `(S_k)` for
every `k` therefore means that `ℱ` is a Cohen-Macaulay `𝒪_X`-Module. It is clear that for `k' ≥ k`, the property
`(S_{k'})` implies `(S_k)`; for `k ≤ 0`, every coherent `𝒪_X`-Module has the property `(S_k)`.*

*(ii) To verify the condition `(5.7.2.1)`, one may restrict to the case where `x ∈ Supp(ℱ)`; in the contrary case one
has indeed `dim(ℱ_x) = −∞` `(0, 14.1.2)`.*

*(iii) If `X = Spec(A)`, where `A` is a Noetherian ring, and `ℱ = M̃`, where `M` is an `A`-module of finite type, one
says that `M` possesses the property `(S_k)` if `ℱ` possesses this property. For an arbitrary locally Noetherian
prescheme `X`, to say that `ℱ` possesses the property `(S_k)` at a point `x ∈ X` therefore means that if one sets
`Y = Spec(𝒪_x)`, the `𝒪_Y`-Module `ℱ̃_x` possesses the property `(S_k)`; one will note that the condition `(5.7.2.1)`
in general does not entail `(5.7.2.2)` for every generization `x'` of `x`, given that one has no inequality relation
between `prof(ℱ_x)` and `prof(ℱ_{x'})` `(0, 16.4.6)`.*

*(iv) It follows at once from the definition that if `ℱ` verifies `(S_k)` at a point `x`, it also verifies `(S_k)` at
every point `x'` generization of `x`.*

*(v) The property `(S_k)` is most important for `k = 1` and `k = 2`; it was introduced for `k = 2` by Serre, to express
his criterion of normality (cf. `(5.8.5)`).*

*(vi) Let `X` be a locally Noetherian prescheme, `Y` a closed sub-prescheme of `X`, `j : Y → X` the canonical
injection, `𝒢` a coherent `𝒪_Y`-Module. It is clear that for every `x ∈ Y`, one has `dim(𝒢_x) = dim((j_*(𝒢))_x)` and
`prof(𝒢_x) = prof((j_*(𝒢))_x)`, whence `coprof(𝒢_x) = coprof((j_*(𝒢))_x)`. For `𝒢` to verify `(S_k)`, it is necessary
and sufficient that `j_*(𝒢)` verify `(S_k)`.*

**Proposition (5.7.4).**

<!-- label: IV.5.7.4 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module. Set `S = Supp(ℱ)`, and for every `n ≥ 0`,
denote by `Z_n` the set of `z ∈ X` such that `coprof(ℱ_z) > n`, so that `Z_n ⊂ S`.*

*(i) For `ℱ` to verify the property `(S_k)`, it is necessary and sufficient that, for every `n ≥ 0`, one has*

```text
  codim(Z_n, S) > n + k.                                 (5.7.4.1)
```

*(ii) Suppose moreover that the `Z_n` are closed in `X`. Then, for `ℱ` to verify the property `(S_k)` at a point
`x ∈ S`, it is necessary and sufficient that, for every `n ≥ 0`, one has*

```text
  codim_x(Z_n, S) > n + k.                               (5.7.4.2)
```

(i) One has indeed, by definition `(5.1.3)`, `codim(Z_n, S) = inf_{z ∈ Z_n} (dim(𝒪_{S,z}))` and the inequality
`(5.7.4.1)` therefore means `(5.1.12.2)` that, for every `z ∈ X`, and every `n ≥ 0`, the relation

```text
  dim(ℱ_z) − prof(ℱ_z) ≥ n + 1
```

entails the relation

```text
  dim(ℱ_z) ≥ n + k + 1.
```

But if one sets `a = dim(ℱ_z)`, `b = prof(ℱ_z)`, one has `b ≤ a`, and to say that for every `n ≥ 0`, the relation
`b ≤ a − n − 1` implies `k ≤ a − n − 1` is equivalent to saying that `b ≥ inf(k, a)`, whence the proposition.

<!-- original page 105 -->

(ii) The reasoning is the same as in (i), with this difference that one must limit oneself to the `z ∈ X` which are
generizations of `x`, and take `(5.1.3.2)` into account.

**Proposition (5.7.5).**

<!-- label: IV.5.7.5 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module. For `ℱ` to verify `(S_k)` (`k ≥ 1`), it is
necessary and sufficient that for every integer `r` such that `0 ≤ r < k`, every open `U` of `X`, and every
`(ℱ|U)`-regular sequence `(f_i)_{1 ≤ i ≤ r}` of sections of `𝒪_X` over `U`, `(ℱ|U)/(∑_{i=1}^r f_i(ℱ|U))` is without
embedded associated prime cycle.*

Let us first prove the proposition for `k = 1`; it then states again that for `ℱ` to verify `(S_1)`, it is necessary
and sufficient that `ℱ` be without embedded associated prime cycle. Indeed, to say that `ℱ` verifies `(S_1)` means that
at the points `x ∈ Supp(ℱ)` such that `dim(ℱ_x) > 0`, one has `prof(ℱ_x) ≥ 1` (since at the other points of `Supp(ℱ)`
one has `dim(ℱ_x) = 0`, hence `prof(ℱ_x) = 0`); but to say that `prof(ℱ_x) ≥ 1` means that `𝔪_x` is not associated to
`ℱ_x` `(0, 16.4.6, (i))`, or again that `x` is not associated to `ℱ` `(3.1.1)`; on the other hand, if `S` is a
sub-prescheme of `X` having `Supp(ℱ)` as underlying space, one has `(5.1.12.1)` `dim(ℱ_x) = dim(𝒪_{S,x})`; to say that
`dim(ℱ_x) > 0` therefore means that `x` is not a maximal point of `Supp(ℱ)` `(5.1.2)`, whence the conclusion.

In the second place, let us show that, for any `k > 1`, the condition of the statement is *necessary*. One may restrict
to considering the case where `U = X`, and our assertion will be proved (by induction on `k` and by virtue of the
first part of the reasoning) if we show that when `ℱ` verifies `(S_k)` (`k > 1`) and `f` is an `ℱ`-regular section of
`𝒪_X` over `X`, then `ℱ/fℱ` verifies `(S_{k−1})` (i.e. verifies `(5.7.2.1)` with `k` replaced by `k − 1`). Now, for
every `x ∈ X`, `f_x` is an `ℱ_x`-regular element; if it is invertible, one has `ℱ_x / f_x ℱ_x = 0` and the conclusion
is trivial. If on the contrary `f_x ∈ 𝔪_x`, one knows that one has `prof(ℱ_x / f_x ℱ_x) = prof(ℱ_x) − 1`
`(0, 16.4.6, (i))`, and `dim(ℱ_x / f_x ℱ_x) = dim(ℱ_x) − 1` `(0, 16.3.4)`, and our assertion follows.

Let us prove finally that for `k > 1`, the condition of the statement is *sufficient*. We shall proceed by induction on
`k`; let `x` be a point of `X`, and suppose first that `dim(ℱ_x) ≥ k`. The induction hypothesis entails that `ℱ`
verifies `(S_{k−1})`, hence `prof(ℱ_x) ≥ k − 1`; taking `(0, 15.2.4)` into account, there is therefore an open
neighbourhood `U` of `x` and an `(ℱ|U)`-regular sequence `(f_i)_{1 ≤ i ≤ k−1}` of sections of `𝒪_X` over `U`, such that
`(f_i)_x ∈ 𝔪_x` for `1 ≤ i ≤ k − 1`. The hypothesis entails that `𝒢 = (ℱ|U)/(∑_{i=1}^{k−1} f_i(ℱ|U))` is without
embedded associated prime cycle; but one has `dim(𝒢_x) = dim(ℱ_x) − (k − 1) ≥ 1` `(0, 16.3.4)`, so `x` is not
associated to `𝒢`; one therefore has `prof(𝒢_x) ≥ 1` `(0, 16.4.6)`, and as `prof(𝒢_x) = prof(ℱ_x) − (k − 1)`

<!-- original page 106 -->

`(0, 16.4.6)`, one has `prof(ℱ_x) ≥ k`. Suppose in the second place that `dim(ℱ_x) = r < k`; as `ℱ` verifies
`(S_{k−1})`, one has `prof(ℱ_x) ≥ inf(k − 1, r) = r`, and this completes the proof.

**Corollary (5.7.6).**

<!-- label: IV.5.7.6 -->

*Suppose that `ℱ` verifies `(S_k)` (`k ≥ 1`); if `(f_i)` (`1 ≤ i ≤ r`) is an `ℱ`-regular sequence of sections of `𝒪_X`
over `X` and if `r < k`, `ℱ/(∑_{i=1}^r f_i ℱ)` verifies `(S_{k−r})`.*

This follows immediately from `(5.7.5)`.

**Corollary (5.7.7).**

<!-- label: IV.5.7.7 -->

*For `ℱ` to verify `(S_2)`, it is necessary and sufficient that `ℱ` be without embedded associated prime cycle and that
for every open `U` of `X` and every `(ℱ|U)`-regular section `f` of `𝒪_X` over `U`, `(ℱ|U)/f(ℱ|U)` be without embedded
associated prime cycle.*

**Remarks (5.7.8).**

<!-- label: IV.5.7.8 -->

*Let `X` be a locally Noetherian prescheme of dimension `1`; it then amounts to the same to say that `X` is a
Cohen-Macaulay prescheme, or that it verifies `(S_1)`, or that it verifies one of the properties `(S_n)` for `n ≥ 1`,
by virtue of the definitions `(5.7.1)` and `(5.7.2)`. By virtue of `(5.7.5)`, it therefore again amounts to the same,
for preschemes of dimension `1`, to say that `X` is a Cohen-Macaulay prescheme or that it has no embedded associated
prime cycle. For example, a locally Noetherian reduced prescheme of dimension `1` is a Cohen-Macaulay prescheme.*

**Proposition (5.7.9).**

<!-- label: IV.5.7.9 -->

*Let `A`, `B` be two Noetherian rings, `ρ : A → B` a ring homomorphism, `M` a `B`-module such that `M_{[ρ]}` is an
`A`-module of finite type. Let `𝔭` be a prime ideal of `A`; the prime ideals of `B` above `𝔭` and belonging to
`Supp(M)` are finite in number, and if `(𝔮_i)_{1 ≤ i ≤ n}` is the family of these ideals, one has*

```text
  dim_{A_𝔭}(M_𝔭) = sup_i dim_{B_{𝔮_i}}(M_{𝔮_i})          (5.7.9.1)

  prof_{A_𝔭}(M_𝔭) = inf_i prof_{B_{𝔮_i}}(M_{𝔮_i}).       (5.7.9.2)
```

If `𝔟` is the annihilator of `M`, `B/𝔟` is identified with a sub-`A`-module of `End_A(M_{[ρ]})`, hence of finite type
since `A` is Noetherian; there are therefore only finitely many prime ideals of `B` above `𝔭` and containing `𝔟`, and
these are precisely those which belong to `Supp(M)`. Replacing `B` by `B/𝔟`, which does not change the second members
of `(5.7.9.1)` and `(5.7.9.2)` (by `(0, 16.1.9)` and `(0, 16.4.8)`), one may therefore suppose that `B` is a finite
`A`-algebra. Set `S = A − 𝔭`, and `B' = S⁻¹ B`; `B'` is a Noetherian semi-local ring whose maximal ideals are
`S⁻¹ 𝔮_i` (`1 ≤ i ≤ n`) and as `M_𝔭` is an `A_𝔭`-module of finite type, one has
`dim_{A_𝔭}(M_𝔭) = dim_{B'}(M_𝔭)` `(0, 16.1.9)`. This being so, the relation `(5.7.9.1)` becomes a particular case of
`(0, 16.1.7.4)`. To prove the relation `(5.7.9.2)`, one reduces at once as in `(0, 16.4.8)` to the case where
`prof_{A_𝔭}(M_𝔭) = 0`, and the same reasoning as in `(0, 16.4.8)` shows that `M_𝔭` contains a sub-`B'`-module of finite
length, and consequently also a *simple* sub-`B'`-module, but such a sub-module is necessarily isomorphic to the
residue field of one of the `B'_{𝔮_i}`, hence there is at least one index `i` such that
`prof_{B_{𝔮_i}}(M_{𝔮_i}) = 0` `(0, 16.4.6)`, which terminates the proof.

**Corollary (5.7.10).**

<!-- label: IV.5.7.10 -->

*Suppose the hypotheses of `(5.7.9)` are verified, and suppose moreover that `A` is a local ring; then, for `M` to be a
Cohen-Macaulay `A`-module, it is necessary and sufficient that, for all the prime ideals `𝔮_i` of `B` above the
maximal ideal of `A`, `M` be a Cohen-Macaulay `B_{𝔮_i}`-module, and moreover that all the numbers
`dim_{B_{𝔮_i}}(M_{𝔮_i})` be equal.*

It indeed follows from `(5.7.9.1)` and `(5.7.9.2)` that these conditions are equivalent to the relation
`dim_A(M) = prof_A(M)`.

**Corollary (5.7.11).**

<!-- label: IV.5.7.11 -->

*Suppose the hypotheses of `(5.7.9)` are verified.*

*(i) If `M_{[ρ]}` verifies the property `(S_k)`, so does `M`.*

*(ii) Suppose that for every pair of prime ideals `𝔮`, `𝔮'` of `B` such that `ρ⁻¹(𝔮) = ρ⁻¹(𝔮')`, one has
`dim_{B_𝔮}(M_𝔮) = dim_{B_{𝔮'}}(M_{𝔮'})`. Then, if `M` verifies the property `(S_k)`, so does `M_{[ρ]}`.*

<!-- original page 107 -->

This follows at once from the relations `(5.7.9.1)` and `(5.7.9.2)` and from the definition of the property `(S_k)`.

**(5.7.12)**

<!-- label: IV.5.7.12 -->

In conformity with the definitions of `(5.7.1)`, given any Noetherian ring `A` and an `A`-module of finite type `M`,
one defines `coprof_A(M)` as equal to `coprof(M̃) = sup_{x ∈ X} (coprof_{A_x}(M_x))`, where `X = Spec(A)`; we shall see
further on `(6.11.5)` that this definition coincides with that of `(0, 16.4.9)` when `A` is a Noetherian *local* ring.

**Corollary (5.7.13).**

<!-- label: IV.5.7.13 -->

*Let `A`, `B` be two Noetherian rings, `ρ : A → B` a ring homomorphism, `M` a `B`-module such that `M_{[ρ]}` is an
`A`-module of finite type. Then one has*

```text
  coprof_A(M_{[ρ]}) ≤ coprof_B(M).                       (5.7.13.1)
```

This follows from the preceding definition and from the relations `(5.7.9.1)` and `(5.7.9.2)`.

### 5.8. Regular preschemes and property `(R_n)`. Serre's normality criterion

**(5.8.1)**

<!-- label: IV.5.8.1 -->

Recall `(0_I, 4.1.4)` that a ringed space `(X, 𝒪_X)` is said to be *regular* at a point `x ∈ X` if `𝒪_x` is a regular
ring. When dealing with preschemes, we shall use this terminology in this chapter only when `X` is locally Noetherian.

**Definition (5.8.2).**

<!-- label: IV.5.8.2 -->

*One says that a locally Noetherian prescheme `X` is **regular in codimension `≤ k`**, or **possesses the property
`(R_k)`** if the set of points where `X` is not regular is of codimension `> k` (in other words `(5.1.3)`, if, for
every `x ∈ X`, the relation `dim(𝒪_x) ≤ k` entails that `𝒪_x` is regular).*

To say that `X` is regular means that `X` possesses the property `(R_k)` for every `k`.

If `X = Spec(A)`, where `A` is a Noetherian ring, one will say that `A` possesses the property `(R_k)` if `X` possesses
this property; to say that `X` is regular means that the ring `A` is regular `(0, 17.3.6)`. For any locally Noetherian
prescheme `X`, one will say that `X` possesses the property `(R_k)` at a point `x ∈ X` if the local ring `𝒪_x`
possesses the property `(R_k)`; this therefore means that for every generization `x'` of `x` in `X`, the relation
`dim(𝒪_{x'}) ≤ k` entails that `𝒪_{x'}` is a regular local ring. To say that `X` is regular at a point `x` is
equivalent to saying that `X` verifies the property `(R_n)` for every `n ≥ 0` at the point `x`, by virtue of
`(0, 17.3.6)`.

**Proposition (5.8.3).**

<!-- label: IV.5.8.3 -->

*If `k` is a field, `X` a prescheme locally of finite type over `k`, then, for every `x ∈ X`, there exists an open
neighbourhood of `x` in `X` isomorphic to a sub-scheme of a regular `k`-scheme.*

Indeed, there is an affine open neighbourhood `U` of `x` isomorphic to a `k`-scheme of the form `Spec(A)`, where `A` is
a `k`-algebra of finite type; `A` is consequently isomorphic to a quotient of a polynomial algebra `k[T_1, …, T_n]`,
and one knows that the latter is a regular ring `(0, 17.3.7)`.

**(5.8.4)**

<!-- label: IV.5.8.4 -->

By virtue of `(5.8.2)`, to say that `X` possesses the property `(R_0)` means that for every maximal point `x` of `X`,
the ring `𝒪_x` is a field `(0, 17.1.4)`, in other words that `X` is reduced at this point. As the set `U` of `x ∈ X`
where `X` is reduced is open (the

<!-- original page 108 -->

nilradical of `X` being a coherent `𝒪_X`-Module (`(I, 6.1.1)` and `(0_I, 5.2.2)`)), it amounts to the same to say that
`X` possesses the property `(R_0)` or that the set `U` is everywhere dense. Consequently:

**Proposition (5.8.5).**

<!-- label: IV.5.8.5 -->

*For a locally Noetherian prescheme `X` to be reduced, it is necessary and sufficient that it verify the properties
`(S_1)` and `(R_0)`.*

Taking `(5.7.5)` into account, this follows from the preceding remark and from `(3.2.1)`.

**Theorem (5.8.6) (Serre's criterion).**

<!-- label: IV.5.8.6 -->

*Let `X` be a locally Noetherian prescheme. For `X` to be normal, it is necessary and sufficient that `X` verify the
properties `(S_2)` and `(R_1)`, in other words, that for every `x ∈ X`, one has the following properties:*

*(i) If `dim(𝒪_x) ≤ 1`, `𝒪_x` is regular (that is to say is a field or a discrete valuation ring `(0, 17.1.4)`).*

*(ii) If `dim(𝒪_x) ≥ 2`, then `prof(𝒪_x) ≥ 2`.*

The conditions are *necessary*. Indeed, to say that `X` is normal means that for every `x ∈ X`, `𝒪_x` is an integrally
closed Noetherian local ring. If `dim(𝒪_x) = 0` (resp. `dim(𝒪_x) = 1`), one concludes that `𝒪_x` is a field since
`𝒪_x` is integral (resp. that `𝒪_x` is a discrete valuation ring, by virtue of `(II, 7.1.6)`). On the other hand, for
every element `f_x ≠ 0` of `𝒪_x`, one knows (Bourbaki, *Alg. comm.*, chap. VII, §1, n° 4, prop. 8) that the prime
ideals associated to `𝒪_x / f_x 𝒪_x` are non-embedded, so `𝒪_x` verifies `(S_2)` `(5.7.7)`.

The conditions are *sufficient*. Indeed, it follows first from `(5.8.5)` that `X` is reduced. The question being local,
one may moreover suppose that `X = Spec(A)`, where `A` is a reduced Noetherian ring `(I, 5.1.4)`; if `R` is the total
ring of fractions of `A`, `R` is a direct composite of a finite number of fields, and (taking `(II, 6.3.6)` into
account), it will suffice to prove that `A` is integrally closed in `R`. Let `h = f/g` be an element of `R` integral
over `A`, with `g` and `f` elements of `A` such that `g` is not a zero-divisor. One has a relation of the form

```text
  f^n + ∑_{i=1}^n a_i f^{n−i} g^i = 0   with  a_i ∈ A   for 1 ≤ i ≤ n.   (5.8.6.1)
```

Let `𝔭` be a prime ideal of `A` such that `dim(A_𝔭) = 1`; if `f_𝔭` and `g_𝔭` are the images of `f` and `g` in `A_𝔭`, it
follows from `(5.8.6.1)` that `f_𝔭/g_𝔭` (which belongs to the total ring of fractions of `A_𝔭`, since `g_𝔭` is not a
zero-divisor in `A_𝔭` by flatness `(0_I, 5.3.1)`) is integral over `A_𝔭`; but as `A_𝔭` is regular, hence integrally
closed, one has `f_𝔭/g_𝔭 ∈ A_𝔭`. In other terms, one has `(fA)_𝔭 ⊂ (gA)_𝔭`. But the hypothesis `(S_2)` entails
`(5.7.7)`, since `g` is not a zero-divisor in `A`, that `A/gA` has only non-embedded associated prime ideals
`𝔭_i` (`1 ≤ i ≤ n`); now, `gA` is the intersection of primary ideals `𝔮_i` corresponding to the `𝔭_i`, and from what
has just been seen, the `𝔮_i` are the inverse images in `A`, by the homomorphisms `A → A_{𝔭_i}`, of the ideals
`(gA)_{𝔭_i}` (Bourbaki, *Alg. comm.*, chap. IV, §2, n° 3, prop. 5). But by virtue of the Hauptidealsatz `(0, 16.3.2)`
one has `dim(A_{𝔭_i}) = 1` for `1 ≤ i ≤ n`, hence `(fA)_{𝔭_i} ⊂ (gA)_{𝔭_i}` for every `i` according to what precedes;
as `fA` is contained in the intersection of the inverse images of the `(fA)_{𝔭_i}` (`1 ≤ i ≤ n`), one has `fA ⊂ gA`,
that is to say `f/g ∈ A`. Q.E.D.

<!-- original page 109 -->

### 5.9. `Z`-pure and `Z`-closed Modules

Part of the notions and results of this section and of the following one are special cases of notions and results developed in Chapter III in the theory of local cohomology. For the convenience of the reader, we give here an independent exposition.

**(5.9.1)**

<!-- label: IV.5.9.1 -->

Let `X` be a locally Noetherian prescheme, `Z` a part of `X` stable under specialization: this means that for every finite part `M` of `Z`, the closure of `M` is contained in `Z`, and consequently `Z` is the union of an increasing filtered family `(Z_α)` of closed parts of `X`; conversely, it is clear that such a union is stable under specialization.

Set `U_α = X − Z_α`, so that `X − Z` is the intersection of the decreasing filtered family of open sets `U_α`; let `i_α : U_α → X` be the canonical injection, and for `U_α ⊃ U_β`, let `i_{αβ} : U_β → U_α` be the canonical injection, so that one has `i_β = i_α ∘ i_{αβ}`. Let `ℱ` be an `𝒪_X`-Module (not necessarily quasi-coherent); one then has `(i_β)_*(ℱ|U_β) = (i_α)_*((i_{αβ})_*(ℱ|U_β))`; from the canonical homomorphism `(0_I, 4.4.3.2)`

```text
  ℱ|U_α → (i_{αβ})_*(ℱ|U_β)
```

one deduces, by application of the functor `(i_α)_*`, a homomorphism

```text
  ρ_{βα} : (i_α)_*(ℱ|U_α) → (i_β)_*(ℱ|U_β)
```

and one verifies at once that one has `ρ_{γα} = ρ_{γβ} ∘ ρ_{βα}` for `U_α ⊃ U_β ⊃ U_γ`; in other words, the `𝒪_X`-Modules `(i_α)_*(ℱ|U_α)` form an inductive system for the homomorphisms `ρ_{βα}`. One sets

```text
  ℋ^0_{X/Z}(ℱ) = lim→_α (i_α)_*(ℱ|U_α).                              (5.9.1.1)
```

This `𝒪_X`-Module does not depend on the increasing family `(Z_α)` of closed sets whose union is `Z`: indeed, let `V` be a Noetherian open set of `X`; one knows `(G, II, 3.10.1)` that in the category of `𝒪_V`-Modules, the functor `ℱ ↦ Γ(V, ℱ)` commutes with inductive limits; hence by virtue of `(5.9.1.1)` one has

```text
  Γ(V, ℋ^0_{X/Z}(ℱ)) = lim→_α Γ(V ∩ U_α, ℱ).                        (5.9.1.2)
```

Let `(Z'_λ)` be a second increasing filtered family of closed sets of `X` with union `Z`; `V ∩ Z` is then the union of the `V ∩ Z_α ∩ Z'_λ`; but `V ∩ Z_α` is locally closed in `X`, hence every closed irreducible part of `V ∩ Z_α` admits a generic point; since the `V ∩ Z_α ∩ Z'_λ` are closed in `V ∩ Z_α` and form (for fixed `α`) an increasing filtered family, there exists an index `λ` such that `V ∩ Z_α ∩ Z'_λ = V ∩ Z_α` `(0_III, 9.2.4)`, in other words `V ∩ Z_α ⊂ V ∩ Z'_λ`. This proves that the decreasing filtered families `V ∩ U_α`, `V ∩ U'_λ` (where `U'_λ = X − Z'_λ`) are cofinal with one another, whence our assertion, by virtue of `(5.9.1.2)`.

<!-- original page 110 -->

We note that the set `Z` is not necessarily constructible: one has an example of this fact by taking `X = Spec(A)`, where `A` is a Noetherian integral ring having an infinity of maximal ideals, and `Z` the complement of the generic point of `X`.

If `Z` is closed and if `i : X − Z → X` is the canonical injection, one has

```text
  ℋ^0_{X/Z}(ℱ) = i_*(ℱ|X − Z)                                       (5.9.1.3)
```

and in particular, for `Z = ∅`, `ℋ^0_{X/Z}(ℱ) = ℱ`.

**Proposition (5.9.2).**

<!-- label: IV.5.9.2 -->

*(i) The functor `ℱ ↦ ℋ^0_{X/Z}(ℱ)` is left exact.*

*(ii) If `ℱ` is quasi-coherent, so is `ℋ^0_{X/Z}(ℱ)`.*

Assertion (i) follows from the definition `(5.9.1.1)`, from the fact that `(i_α)_*` is a left exact functor, and from the fact that inductive limits preserve exactness in the category of `𝒪_X`-Modules. Assertion (ii) follows from `(I, 9.2.2)` and from the fact that an inductive limit of quasi-coherent `𝒪_X`-Modules is quasi-coherent `(I, 1.3.9)`.

**Remark (5.9.3).**

<!-- label: IV.5.9.3 -->

*If `ℱ` is an `𝒪_X`-Algebra, so is `ℋ^0_{X/Z}(ℱ)` `(0_I, 4.2.4)`; in particular `ℋ^0_{X/Z}(𝒪_X)` is a quasi-coherent `𝒪_X`-Algebra, and for every `𝒪_X`-Module `ℱ`, `ℋ^0_{X/Z}(ℱ)` is an `ℋ^0_{X/Z}(𝒪_X)`-Module which is quasi-coherent if `ℱ` is quasi-coherent `(I, 9.6.1)`. More particularly, suppose that `X = Spec(A)`, where `A` is integral and Noetherian; then `ℋ^0_{X/Z}(𝒪_X)` is the `𝒪_X`-Algebra `B̃`, where*

```text
  B = ⋂_{𝔭 ∈ X − Z} A_𝔭.                                            (5.9.3.1)
```

This follows from `(5.9.1.2)` and from `(I, 8.2.1.1)`.

**Proposition (5.9.4).**

<!-- label: IV.5.9.4 -->

*Let `X` be a locally Noetherian prescheme, `Z` a part of `X` stable under specialization, `X'` a locally Noetherian prescheme, `f : X' → X` a flat morphism. Then `Z' = f⁻¹(Z)` is stable under specialization and for every quasi-coherent `𝒪_X`-Module `ℱ`, one has a canonical isomorphism*

```text
  f*(ℋ^0_{X/Z}(ℱ)) ≅ ℋ^0_{X'/Z'}(f*(ℱ)).                            (5.9.4.1)
```

Indeed, with the notations of `(5.9.1)`, `Z'_α = f⁻¹(Z_α)` is closed in `X'` and `Z'` is the union of the `Z'_α`; in addition, `(i_α)_{(X')}` is the canonical injection `i'_α : U'_α → X'`, if `U'_α = X' − Z'_α = f⁻¹(U_α)`. Since `f` is flat, one knows `(2.3.1)` that the canonical homomorphism `f*((i_α)_*(ℱ|U_α)) → (i'_α)_*(f*(ℱ)|U'_α)` is bijective; since, for `α ≤ β`, the diagram

<!-- original page 111 -->

```text
  f*((i_α)_*(ℱ|U_α)) ⥲ (i'_α)_*(f*(ℱ)|U'_α)
        ↓                       ↓
  f*((i_β)_*(ℱ|U_β)) ⥲ (i'_β)_*(f*(ℱ)|U'_β)
```

is commutative, one has, on passing to the limit, a canonical isomorphism `lim→_α (f*((i_α)_*(ℱ|U_α))) ≅ ℋ^0_{X'/Z'}(f*(ℱ))`. But since the functor `f*` commutes with inductive limits `(0_I, 4.3.2)`, this gives by definition the desired isomorphism `(5.9.4.1)`.

**Corollary (5.9.5).**

<!-- label: IV.5.9.5 -->

*Under the hypotheses of `(5.9.4)`, if `ℋ^0_{X/Z}(ℱ)` is coherent, so is `ℋ^0_{X'/Z'}(f*(ℱ))`. The converse is true when `f` is a faithfully flat and quasi-compact morphism.*

The first assertion follows from `(5.9.4.1)` and from `(0_I, 5.3.11)`; the second amounts to saying that if `ℋ^0_{X'/Z'}(f*(ℱ))` is of finite type, so is `ℋ^0_{X/Z}(ℱ)`; this follows from `(5.9.4.1)` and from `(2.5.2)`.

**Corollary (5.9.6).**

<!-- label: IV.5.9.6 -->

*Let `X` be a locally Noetherian prescheme, `Z` a part of `X` stable under specialization, `ℱ` a quasi-coherent `𝒪_X`-Module. For every `x ∈ X`, set `X_x = Spec(𝒪_x)`, `Z_x = Z ∩ X_x`; one has a canonical functorial isomorphism*

```text
  (ℋ^0_{X/Z}(ℱ))_x ≅ ℋ^0_{X_x/Z_x}(ℱ̃_x).                           (5.9.6.1)
```

It suffices to apply `(5.9.4)` to the canonical morphism `X_x → X`, which is flat, and to take account of `(I, 1.6.5)`.

**(5.9.7)**

<!-- label: IV.5.9.7 -->

With the notations of `(5.9.1)`, one has for every `α` a canonical functorial homomorphism `ℱ → (i_α)_*(ℱ|U_α)` `(0_I, 4.4.3.2)`, and these homomorphisms form an inductive system; passing to the inductive limit, one therefore deduces a canonical functorial homomorphism

```text
  ρ_{X/Z} : ℱ → ℋ^0_{X/Z}(ℱ).                                       (5.9.7.1)
```

**Proposition (5.9.8).**

<!-- label: IV.5.9.8 -->

*Let `X` be a locally Noetherian prescheme, `Z` a part of `X` stable under specialization, `ℱ` an `𝒪_X`-Module. The following properties are equivalent:*

*a) The homomorphism `ρ_{X/Z}` `(5.9.7.1)` is injective (resp. bijective).*

*b) For every Noetherian open set `V` of `X`, the homomorphism*

```text
  (ρ_{X/Z})_V : Γ(V, ℱ) → lim→_α Γ(V ∩ U_α, ℱ)
```

*is injective (resp. bijective).*

*a') For every closed part `T ⊂ Z` of `X`, the canonical homomorphism `(0_I, 4.4.3.2)*

```text
  ℱ → (i_T)_*(ℱ|X − T)
```

*(where `i_T : X − T → X` is the canonical injection) is injective (resp. bijective).*

*b') For every closed part `T ⊂ Z` of `X` and every Noetherian open set `V` of `X`, the restriction homomorphism*

```text
  Γ(V, ℱ) → Γ(V ∩ (X − T), ℱ)
```

*is injective (resp. bijective).*

Taking account of `(5.9.1.2)`, the equivalence of a) and b) (resp. a') and b')) follows from

<!-- original page 112 -->

the definition of the functor `Γ` and the fact that it is left exact. Since the homomorphism `(ρ_{X/Z})_V` is the composite

```text
  Γ(V, ℱ) → Γ(V ∩ (X − T), ℱ) → lim→_α Γ(V ∩ U_α, ℱ)                (5.9.8.1)
```

for every closed part `T ⊂ Z`, if `(ρ_{X/Z})_V` is injective, so is `Γ(V, ℱ) → Γ(V ∩ (X − T), ℱ)`; on the other hand, the fact that b') implies b) follows from the definition of an inductive limit. It remains to show that if `ρ_{X/Z}` is bijective, so is `Γ(V, ℱ) → Γ(V ∩ (X − T), ℱ)`, and for this it suffices, by virtue of `(5.9.8.1)`, to see that if `U' ⊂ U` are two open sets contained in `V` and containing `V ∩ Z`, the restriction homomorphism `Γ(U, ℱ) → Γ(U', ℱ)` is injective; but this follows from the fact that `ρ_{X/Z}` is injective, by replacing `V` by `U` and `V ∩ (X − T)` by `U'` in what precedes.

**Definition (5.9.9).**

<!-- label: IV.5.9.9 -->

*Under the hypotheses of `(5.9.8)`, one says that `ℱ` is **`Z`-pure** (resp. **`Z`-closed**) if the homomorphism `ρ_{X/Z}` is injective (resp. bijective).*

If `X = Spec(A)` is affine, `ℱ = M̃` where `M` is an `A`-module, one says that `M` is `Z`-pure (resp. `Z`-closed) when `ℱ` is `Z`-pure (resp. `Z`-closed).

One says that `ℱ` is `Z`-pure (resp. `Z`-closed) *at a point* `x ∈ X` if (with the notations of `(5.9.6)`) `ℱ̃_x` is `Z_x`-pure (resp. `Z_x`-closed); equivalently, by virtue of `(5.9.6)`, the canonical homomorphism `ℱ_x → (ℋ^0_{X/Z}(ℱ))_x` is injective (resp. bijective).

We note that for every `x ∈ X − Z`, `ℱ` is `Z`-closed at the point `x`, by virtue of `(5.9.8)`.

**Corollary (5.9.10).**

<!-- label: IV.5.9.10 -->

*(i) Let `(V_λ)` be an open cover of `X`. For `ℱ` to be `Z`-pure (resp. `Z`-closed), it is necessary and sufficient that for every `λ`, `ℱ|V_λ` be `(Z ∩ V_λ)`-pure (resp. `(Z ∩ V_λ)`-closed).*

*(ii) Let `Z'` be a part of `Z` stable under specialization. If `ℱ` is `Z`-pure (resp. `Z`-closed), it is `Z'`-pure (resp. `Z'`-closed).*

This follows at once from `(5.9.8, b'))`.

**Proposition (5.9.11).**

<!-- label: IV.5.9.11 -->

*Under the hypotheses of `(5.9.8)`, the `𝒪_X`-Modules `Ker(ρ_{X/Z})` and `Coker(ρ_{X/Z})` have their support contained in `Z`, and the `𝒪_X`-Module `ℋ^0_{X/Z}(ℱ)` is `Z`-closed. Moreover, if `u : ℱ → ℱ'` is a homomorphism of `𝒪_X`-Modules such that `ℱ'` is `Z`-closed, `u` factors in a unique way as `ℱ →^{ρ_{X/Z}} ℋ^0_{X/Z}(ℱ) →^v ℱ'`. If in addition the supports of `Ker(u)` and `Coker(u)` are contained in `Z`, `v` is an isomorphism.*

The first assertion means that, for every `x ∈ X − Z`, one has

```text
  Ker(ρ_{X/Z})_x = Coker(ρ_{X/Z})_x = 0,
```

i.e. that `(ρ_{X/Z})_x` is bijective, or equivalently that `ℱ` is `Z`-pure at `x`, as was noted above `(5.9.9)`.

To show that `ℋ^0_{X/Z}(ℱ)` is `Z`-closed, one has to see that for a Noetherian open `V` of `X`, `lim→_β Γ(V ∩ U_β, ℋ^0_{X/Z}(ℱ))` equals `Γ(V, ℋ^0_{X/Z}(ℱ))`; but by definition `Γ(V ∩ U_β, ℋ^0_{X/Z}(ℱ)) = lim→_α Γ(V ∩ U_α ∩ U_β, ℱ)`. Now the double family `(U_α ∩ U_β)` is filtered decreasing, and our assertion follows from `(5.9.1)` and from the theorem of the double inductive limit.

<!-- original page 113 -->

Let us pass to the second part of the proposition. The existence and uniqueness of `v` follow from the fact that for every `α`, `(i_α)_*(u)` is the unique homomorphism making commutative the diagram

```text
  ℱ ────────u───────→ ℱ'
  ↓                    ↓
  (i_α)_*(ℱ|U_α) ─(i_α)_*(u)─→ (i_α)_*(ℱ'|U_α)
```

from the fact that there is a unique homomorphism `w` making commutative all the diagrams

```text
  (i_α)_*(ℱ|U_α) ─(i_α)_*(u)─→ (i_α)_*(ℱ'|U_α)
        ↓                            ↓
  ℋ^0_{X/Z}(ℱ) ──────w────────→ ℋ^0_{X/Z}(ℱ')
```

and finally from the fact that `ℱ'` and `ℋ^0_{X/Z}(ℱ')` are canonically identified by hypothesis.

It remains to see that if the supports of `Ker(u)` and `Coker(u)` are contained in `Z`, `v` is an isomorphism. It suffices to see that for every Noetherian open `V`, the corresponding homomorphism `Γ(V, ℋ^0_{X/Z}(ℱ)) → Γ(V, ℱ')` is then an isomorphism. Now, if a section `t ∈ Γ(V, ℋ^0_{X/Z}(ℱ))` has image `0` in `Γ(V, ℱ')`, note that for some index `α`, one has `t ∈ Γ(V ∩ U_α, ℱ)`, and by virtue of the hypothesis on `u`, one has `t_y = 0` for every `y ∈ V ∩ (X − Z)`; there is then an open set containing `V ∩ (X − Z)` such that the restriction of `t` to this open is zero, hence by definition `t` is the element `0` of `Γ(V, ℋ^0_{X/Z}(ℱ))`. Let us now prove that every section `s' ∈ Γ(V, ℱ')` is the image of a section of `ℋ^0_{X/Z}(ℱ)` over `V`. By hypothesis, for every `x ∈ V ∩ (X − Z)` there exists a section `s^{(x)}` of `ℱ` over an open neighbourhood `W^{(x)}` of `x` in `X`, whose image by `u` is `s'|W^{(x)}`; `s'|W^{(x)}` is therefore also the image by `v` of the section `t^{(x)}` of `ℋ^0_{X/Z}(ℱ)`, canonical image of `s^{(x)}`. In addition, since one has seen that `v` is injective, the restrictions of `t^{(x)}` and `t^{(x')}` to `W^{(x)} ∩ W^{(x')}` are identical for any two points `x`, `x'` of `V ∩ (X − Z)`; the `t^{(x)}` are therefore the restrictions of a single section `t` of `ℋ^0_{X/Z}(ℱ)` over an open neighbourhood `U` of `(X − Z) ∩ V`. But since `ℋ^0_{X/Z}(ℱ)` is `Z`-closed, `t` extends in a unique way to a section of `ℋ^0_{X/Z}(ℱ)` over `V`, whose image by `v` has the same restriction to `U` as `s'`, hence coincides with `s'` for the same reason.

One says that `ℋ^0_{X/Z}(ℱ)` is the **`Z`-closure** of `ℱ`.

<!-- original page 114 -->

**Remarks (5.9.12).**

<!-- label: IV.5.9.12 -->

*(i) Let `𝒞(X)` be the category of `𝒪_X`-Modules, and let `𝒞_Z(X)` be the subcategory of `𝒞(X)` formed by `𝒪_X`-Modules with support contained in `Z`; this subcategory is localizing in the sense of Gabriel, and the functor `ℋ^0_{X/Z}` is none other than the Gabriel localization functor (cf. `[27]`; this would furnish another proof of `(5.9.11)`). When `Z` is closed, the functor `i^* : 𝒞(X) → 𝒞(X − Z)` (where `i : X − Z → X` is the canonical injection) defines an equivalence of categories `𝒞(X)/𝒞_Z(X) ≈ 𝒞(X − Z)`.*

*(ii) It follows from `(5.9.11)` that the condition `ℋ^0_{X/Z}(ℱ) = 0` is equivalent to `Supp(ℱ) ⊂ Z`. It indeed entails the latter, since the kernel of `ρ_{X/Z}` is then equal to `ℱ`. Conversely, if `Supp(ℱ) ⊂ Z`, it suffices to apply the second part of `(5.9.11)` to the unique homomorphism `u : ℱ → 0` to conclude that the corresponding homomorphism `v : ℋ^0_{X/Z}(ℱ) → 0` is an isomorphism.*

*(iii) The preceding developments keep a sense for every locally Noetherian ringed space such that every closed irreducible part admits exactly one generic point. In particular, they apply, on a locally Noetherian prescheme, to arbitrary sheaves of abelian groups (considered as Modules over the simple sheaf associated with the constant presheaf `ℤ`). One still has, for every `x ∈ X`, the canonical isomorphism `(5.9.6.1)`, in which `ℱ̃` denotes the sheaf induced on the subspace `X_x` of `X` by the sheaf `ℱ`; the direct proof follows at once from the definition `(5.9.1.2)` and from the theorem of the double inductive limit.*

### 5.10. Property `(S_2)` and `Z`-closure

**(5.10.1)**

<!-- label: IV.5.10.1 -->

Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module; for every part `T` of `X`, we shall set

```text
  prof_T(ℱ) = inf_{x ∈ T} prof(ℱ_x).                                (5.10.1.1)
```

**Proposition (5.10.2).**

<!-- label: IV.5.10.2 -->

*Let `X` be a locally Noetherian prescheme, `Z` a part of `X` stable under specialization, `ℱ` a quasi-coherent `𝒪_X`-Module. The following conditions are equivalent:*

*a) `ℱ` is `Z`-pure.*

*b) `Ass(ℱ)` does not meet `Z`.*

*If in addition `ℱ` is coherent, these conditions are also equivalent to:*

*c) `prof_Z(ℱ) ≥ 1`.*

To say that `ℱ` is `Z`-pure means that for every Noetherian open `V` of `X`, and every open `U ⊃ X − Z`, the restriction homomorphism `Γ(V, ℱ) → Γ(V ∩ U, ℱ)` is injective `(5.9.8)`; but according to `(3.1.8)` this is equivalent to `V ∩ Ass(ℱ) ⊂ U`, whence the equivalence of a) and b). Furthermore, to say that `x ∈ Ass(ℱ)` means that no element of `𝔪_x` is `ℱ_x`-regular `(3.1.2)`, hence, when `ℱ` is coherent, this can still be written `prof(ℱ_x) = 0`; one deduces at once in this case the equivalence of b) and c).

**Corollary (5.10.3).**

<!-- label: IV.5.10.3 -->

*Let `0 → ℱ' → ℱ → ℱ'' → 0` be an exact sequence of quasi-coherent `𝒪_X`-Modules. If `ℱ` is `Z`-pure, so is `ℱ'`; conversely, if `ℱ'` and `ℱ''` are `Z`-pure, so is `ℱ`.*

<!-- original page 115 -->

This follows from the form `(5.10.2, b))` of the condition for a quasi-coherent `𝒪_X`-Module to be `Z`-pure, and from `(3.1.7)`.

**Corollary (5.10.4).**

<!-- label: IV.5.10.4 -->

*Suppose `ℱ` is coherent. For `ℱ` to be `Z`-pure at a point `x ∈ X`, it is necessary and sufficient that `prof_{Z_x}(ℱ̃_x) ≥ 1` (with the notations of `(5.9.6)`).*

This follows at once from `(5.10.2)` and `(5.9.6)`.

**Theorem (5.10.5).**

<!-- label: IV.5.10.5 -->

*Let `X` be a locally Noetherian prescheme, `Z` a part of `X` stable under specialization, `ℱ` a coherent `𝒪_X`-Module. For `ℱ` to be `Z`-closed, it is necessary and sufficient that one have `prof_Z(ℱ) ≥ 2`.*

By virtue of `(5.10.2)`, one may restrict to the case where `ℱ` is `Z`-pure and `prof_Z(ℱ) ≥ 1`. Moreover, to say that `prof_Z(ℱ) ≥ 2` is equivalent to saying that for every closed part `Z_α` of `Z`, `prof_{Z_α}(ℱ) ≥ 2`; and likewise, it follows from `(5.9.8)` that to say that `ℱ` is `Z`-closed is equivalent to saying that `ℱ` is `Z_α`-closed for every `α`. One may therefore already restrict to the case where `Z` is closed. The question being local, it suffices, for every `x ∈ Z`, to prove the theorem for `ℱ|U`, `U` being an affine open neighbourhood of `x`, and one may therefore restrict to the case where `X = U` is affine. One knows then that `Ass(ℱ)` is finite `(3.1.6)`, and since `Ass(ℱ) ⊂ X − Z`, there is a section `f` of `𝒪_X` over `X` such that `Ass(ℱ) ⊂ X_f ⊂ X − Z` `(II, 4.5.4)`; one deduces that `f` is `ℱ`-regular `(3.1.9)` and that for every `y ∈ Z`, one has `f_y ∈ 𝔪_y`, hence `prof(ℱ_y) = 1 + prof(ℱ_y/f_y ℱ_y)` `(0, 16.4.6)`. The condition `prof_Z(ℱ) ≥ 2` is thus equivalent to `prof_Z(ℱ/fℱ) ≥ 1`, or equivalently `(5.10.2)` to the fact that `ℱ/fℱ` is `Z`-pure, and it suffices to see that this latter property is equivalent to the fact that `ℱ` is `Z`-closed.

Consider the exact sequence `0 → ℱ →^f ℱ → ℱ/fℱ → 0` (the homothety of ratio `f : ℱ → ℱ` being by hypothesis injective); setting `W = X − Z`, one has the commutative diagram

```text
  0 → Γ(X, ℱ) →^f Γ(X, ℱ) → Γ(X, ℱ/fℱ) → 0
        ↓             ↓             ↓
  0 → Γ(W, ℱ) →^f Γ(W, ℱ) → Γ(W, ℱ/fℱ)
```

whose two rows are exact (`X` being affine). If the restriction homomorphism `Γ(X, ℱ) → Γ(W, ℱ)` is bijective, one deduces from this diagram that

```text
  Γ(X, ℱ/fℱ) → Γ(W, ℱ/fℱ)
```

is injective, and this shows `(5.9.8)` that if `ℱ` is `Z`-closed, `ℱ/fℱ` is `Z`-pure. Conversely, suppose that `ℱ/fℱ` is `Z`-pure, and let `s` be a section of `ℱ` over `W`; since `X_f ⊂ W`, there exists an integer `n > 0` such that `f^n(s|X_f)` extends to a section `t` of `ℱ` over `X` `(I, 1.4.1)`; furthermore, the restrictions of `t` and `f^n s` to `X_f` being the same, it follows that the restriction of `t` to `W` equals `f^n s` by virtue of the relation `Ass(ℱ) ⊂ X_f` `(5.10.2)`; since `f` is `ℱ`-regular, it will suffice to see that `t` is of the form `f^n t'`, where `t' ∈ Γ(X, ℱ)`,

<!-- original page 116 -->

to show that the homomorphism `Γ(X, ℱ) → Γ(W, ℱ)` is surjective, hence bijective. Now to say that `t = f^n t'` means that the image of `t` in `Γ(X, ℱ/f^n ℱ)` is zero. But since `f^k ℱ/f^{k+1} ℱ` is isomorphic to `ℱ/fℱ`, hence `Z`-pure by hypothesis, one deduces from `(5.10.3)`, by induction on `n`, that `ℱ/f^n ℱ` is `Z`-pure. But by definition the image of `t|W = f^n s` in `Γ(W, ℱ/f^n ℱ)` is zero, whence the conclusion.

**Corollary (5.10.6).**

<!-- label: IV.5.10.6 -->

*Let `ℱ` be a coherent `𝒪_X`-Module. For `ℱ` to be `Z`-closed at a point `x`, it is necessary and sufficient that `prof_{Z_x}(ℱ̃_x) ≥ 2`.*

This follows from `(5.9.6)` and `(5.10.5)`.

**Theorem (5.10.7) (Hartshorne).**

<!-- label: IV.5.10.7 -->

*Let `X` be a locally Noetherian prescheme, `Y` a closed part of `X`. Suppose that for every `y ∈ Y`, one has `prof(𝒪_{X,y}) ≥ 2`; then for every connected component `C` of `X`, `C − (C ∩ Y)` is connected.*

One may restrict to the case where `X` is connected; it then follows from `(5.10.5)` that the canonical homomorphism `𝒪_X → i_*(𝒪_X|X − Y)` (where `i : X − Y → X` is the canonical injection) is bijective. Consequently the restriction homomorphism `Γ(X, 𝒪_X) → Γ(X − Y, 𝒪_X)` is also bijective. It suffices now to apply Lemma `(III, 7.8.6.1)`.

**Corollary (5.10.8).**

<!-- label: IV.5.10.8 -->

*Let `X` be a locally Noetherian prescheme, `d` an integer such that for every `x ∈ X`, the relation `dim(𝒪_x) ≥ d` entails `prof(𝒪_x) ≥ 2`. Suppose `X` connected; then, if `X'`, `X''` are two distinct irreducible components of `X`, there exists a sequence `(X_i)_{0 ≤ i ≤ n}` of irreducible components of `X` such that `X_0 = X'`, `X_n = X''`, and that, for `1 ≤ i ≤ n`, one has `codim(X_{i−1} ∩ X_i, X) ≤ d − 1` (one then says that `X` is **connected in codimension `≤ d − 1`**).*

If `Y` is a closed part of `X` such that `codim(Y, X) ≥ d`, one has `dim(𝒪_{X,y}) ≥ d` for every `y ∈ Y` `(5.1.3)`, hence `prof(𝒪_{X,y}) ≥ 2` for every `y ∈ Y`, and it follows from `(5.10.7)` that `X − Y` is connected. On the other hand, for `codim(Y, X) ≥ d`, it is necessary and sufficient that for every `y ∈ Y`, there exist an open neighbourhood `V` of `y` in `X` such that `codim(Y ∩ V, V) ≥ d` `(0, 14.2.3)`. Note finally that if `𝔉` denotes the set of closed parts `Y` of `X` of codimension `≥ d`, the union of two sets of `𝔉` belongs to `𝔉` `(0, 14.2.5)`, and every closed set contained in a set of `𝔉` belongs to `𝔉`, properties which one also expresses by saying that `𝔉` is an **antifilter** of closed parts of `X`. The corollary then follows from the following topological lemma:

**Lemma (5.10.8.1).**

<!-- label: IV.5.10.8.1 -->

*Let `X` be a connected locally Noetherian topological space, `𝔉` an antifilter of closed parts of `X`. One assumes that if `Y` is a closed part of `X` such that for every `y ∈ Y`, there exist an open neighbourhood `V` of `y` in `X` and a `Y_y ∈ 𝔉` such that `V ∩ Y = V ∩ Y_y`, then `Y ∈ 𝔉`. The following conditions are then equivalent:*

*a) For every `Y ∈ 𝔉`, `X − Y` is connected.*

*b) If `X'` and `X''` are two distinct irreducible components of `X`, there exists a sequence `(X_i)_{0 ≤ i ≤ n}` of irreducible components of `X` such that `X_0 = X'`, `X_n = X''` and that, for `1 ≤ i ≤ n`, one has `X_{i−1} ∩ X_i ∉ 𝔉`.*

Suppose b) is verified and let us prove that `U = X − Y` is connected for every `Y ∈ 𝔉`. If `U'` and `U''` are two distinct irreducible components of `U`, there exist two irreducible components `X'`, `X''` of `X` such that `X' ∩ U = U'`, `X'' ∩ U = U''` `(0_I, 2.1.6)`;

<!-- original page 117 -->

let us form for these two components a sequence `(X_i)` having the property stated in b) and set `U_i = X_i ∩ U` for `1 ≤ i ≤ n`; then `U_i` is an irreducible component of `U` `(0_I, 2.1.6)` and moreover `U_i ∩ U_{i−1} ≠ ∅` for `1 ≤ i ≤ n`, otherwise one would have `X_i ∩ X_{i−1} ⊂ Y`, hence `X_i ∩ X_{i−1} ∈ 𝔉`, contrary to the definition of the `X_i`. This entails that `U` is connected.

Let us now show that a) entails b). Denote by `Y` the union of the family `(X_α ∩ X_β)`, where `(X_α, X_β)` runs through the set of pairs of distinct irreducible components of `X` such that `X_α ∩ X_β ∈ 𝔉`. For every point `y ∈ Y`, there is an open neighbourhood `V` of `y` in `X` meeting only a finite number of irreducible components of `X`; this shows on the one hand that `Y` is closed and on the other hand that `V ∩ Y` is the intersection of `V` with a set of `𝔉`; by virtue of the hypothesis made on `𝔉`, one has `Y ∈ 𝔉`, hence `U = X − Y` is connected; in addition `Y` is rare in `X`. Let then `X'`, `X''` be two distinct irreducible components of `X`, `U'`, `U''` their respective traces on `U`; these are distinct irreducible components of `U` `(0_I, 2.1.6)`. Now the union of the irreducible components `W` of `U` for which there exists a sequence `(U_i)_{0 ≤ i ≤ n}` of irreducible components of `U` such that `U_0 = U'`, `U_{i−1} ≠ U_i` and `U_{i−1} ∩ U_i ≠ ∅` for `1 ≤ i ≤ n` and `U_n = W`, is an open and closed set in `U`, since `U` is locally Noetherian and consequently its irreducible components form a locally finite family of closed sets. There is therefore such a sequence `(U_i)` for which `U_n = U''`; let `X_i` `(0 ≤ i ≤ n)` be the irreducible component of `X` such that `X_i ∩ U = U_i` `(0_I, 2.1.6)`; since `U_{i−1} ≠ U_i`, one has `X_{i−1} ≠ X_i` for `1 ≤ i ≤ n`; if one had `X_{i−1} ∩ X_i ∈ 𝔉` for some `i` such that `1 ≤ i ≤ n`, one would deduce `X_{i−1} ∩ X_i ⊂ Y` by definition of `Y`, whence `U_{i−1} ∩ U_i = ∅`, contrary to the hypothesis. This completes the proof of the lemma.

One will note that the hypothesis made on `X` in `(5.10.8)` is verified when `X` is a Cohen-Macaulay prescheme and `d ≥ 2`.

**Corollary (5.10.9).**

<!-- label: IV.5.10.9 -->

*If a Noetherian local ring `A` verifies `(S_2)` and is catenary, it is equidimensional.*

The hypothesis of `(5.10.8)` is then verified by `X = Spec(A)`, with `d = 2`. To show that all the irreducible components of `X` have the same dimension, it suffices then, by virtue of `(5.10.8)`, to show that two such components `X'`, `X''` have the same dimension when one assumes in addition that `codim(X' ∩ X'', X) = 1`. There is then an irreducible component `Z` of `X' ∩ X''` such that `codim(Z, X) = 1`, hence `codim(Z, X') = 1`, since `codim(Z, X) ≥ codim(Z, X') ≥ 1`; likewise `codim(Z, X'') = 1`, and since `X` is catenary, this entails `dim(X') = dim(X'')`.

**Proposition (5.10.10).**

<!-- label: IV.5.10.10 -->

*Let `X` be a locally Noetherian prescheme, `Z` a part of `X` stable under specialization, `ℱ` a coherent `𝒪_X`-Module, and suppose that the `𝒪_X`-Module `ℋ^0_{X/Z}(ℱ)` is coherent. Then:*

*(i) One has `prof_Z(ℋ^0_{X/Z}(ℱ)) ≥ 2`.*

*(ii) For every point `x ∈ Ass(ℱ) ∩ (X − Z)`, one has `codim(Z ∩ ‾{x}, ‾{x}) ≥ 2`.*

*(iii) The set `U` of `x ∈ X` such that `prof_{Z_x}(ℱ̃_x) ≥ 2` (notations of `(5.9.6)`) is open in `X`; one has `X − U ⊂ Z`, and `U` is the largest open set of `X` such that `ℱ|U` be `(Z ∩ U)`-closed.*

<!-- original page 118 -->

For brevity set `ℱ' = ℋ^0_{X/Z}(ℱ)`. One knows `(5.9.11)` that `ℱ'` is `Z`-closed and assertion (i) follows therefore from `(5.10.5)` applied to `ℱ'`. Let `x ∈ Ass(ℱ) ∩ (X − Z)`; since the restrictions of `ℱ` and `ℱ'` to `X − Z` are canonically isomorphic `(5.9.11)`, one has `x ∈ Ass(ℱ')`. Consider a point `y ∈ Z ∩ ‾{x}`; the prime ideal `𝔭` of `𝒪_y` corresponding to `x` is associated with the `𝒪_y`-module `ℱ'_y`, hence one has, by virtue of (i) and of `(0, 16.4.6.2)`, `2 ≤ prof(ℱ'_y) ≤ dim(𝒪_y/𝔭) = codim(‾{y}, ‾{x})`, whence (ii). Finally, to prove (iii), note that `U` is the set of `x ∈ X` such that `ℱ̃_x` is `Z_x`-closed `(5.10.5)`, or equivalently, by virtue of `(5.9.6)`, the set of points where the canonical homomorphism `ℱ_x → ℱ'_x` is bijective; it is therefore the complement of the union of the supports of `Ker(ρ_{X/Z})` and `Coker(ρ_{X/Z})`, and these latter are coherent `𝒪_X`-Modules by virtue of the hypothesis `(0_I, 5.3.4)`, hence have closed support `(0_I, 5.2.2)`; this shows that `U` is open, and `U` is obviously the largest open such that `ℱ|U` be `(Z ∩ U)`-closed; finally the inclusion `X − U ⊂ Z` follows from `(5.9.11)`.

We shall see later `(5.11.1)` that in the most important cases assertion (ii) conversely entails that `ℋ^0_{X/Z}(ℱ)` is coherent.

**(5.10.11)**

<!-- label: IV.5.10.11 -->

Let `X` be a locally Noetherian prescheme, `Z` a part of `X` stable under specialization; one has seen that `𝒜 = ℋ^0_{X/Z}(𝒪_X)` is a quasi-coherent `𝒪_X`-Algebra `(5.9.3)`; the `X`-scheme `X' = Spec(ℋ^0_{X/Z}(𝒪_X))` `(II, 1.3.1)` is called the **`Z`-closure** of `X`. Moreover for every `𝒪_X`-Module `ℱ`, `ℋ^0_{X/Z}(ℱ)` is an `𝒜`-Module, which is quasi-coherent if `ℱ` is a quasi-coherent `𝒪_X`-Module; in this latter case there is therefore a unique `𝒪_{X'}`-Module `ℱ'` such that one has, denoting by `g : X' → X` the structure morphism `(II, 1.4.3)`,

```text
  ℋ^0_{X/Z}(ℱ) = g_*(ℱ').                                           (5.10.11.1)
```

**Proposition (5.10.12).**

<!-- label: IV.5.10.12 -->

*Notations being those of `(5.10.11)`:*

*(i) Let `x` be a point of `X`. For the morphism*

```text
  X' ×_X X_x → X_x   (= Spec(𝒪_{X,x}))
```

*deduced from `g` by localization to be an isomorphism, it is necessary and sufficient that `𝒪_x` be `Z`-closed at the point `x` (which is the case for every `x ∈ X − Z`).*

*(ii) Set `Z' = g⁻¹(Z)`, and suppose `X'` locally Noetherian. Then `ℱ'` is `Z'`-closed; if in addition `ℱ'` is a coherent `𝒪_{X'}`-Module, one has `prof_{Z'}(ℱ') ≥ 2`.*

*(iii) Suppose that `ℋ^0_{X/Z}(𝒪_X)` and `ℋ^0_{X/Z}(ℱ)` are coherent. Then the morphism `g : X' → X` is finite; the set `U` of `x ∈ X` such that one has `prof_{Z_x}(𝒪̃_x) ≥ 2` and `prof_{Z_x}(ℱ̃_x) ≥ 2` is open in `X` and such that `X − U ⊂ Z`; in addition `U` is the largest open set of `X` such that the restriction `g⁻¹(U) → U` of `g` is an isomorphism and that the restriction `ℱ|U → ℱ'|g⁻¹(U)` of the canonical `g`-morphism `ℱ → ℱ'` is an isomorphism.*

Assertion (i) follows from the definitions, and (iii) is an immediate consequence of `(5.10.10, (iii))`. To prove (ii), consider an open `V` of `X` containing `X − Z`

<!-- original page 119 -->

and its inverse image `V' = g⁻¹(V)`; if `i : V → X` and `i' : V' → X'` are the canonical injections, the canonical homomorphism `ρ_{X'/Z'} : ℱ' → i'_*(ℱ'|V')` is such that `g_*(ρ_{X'/Z'})` is the canonical homomorphism `ρ_{X/Z} : ℋ^0_{X/Z}(ℱ) → i_*(ℋ^0_{X/Z}(ℱ)|V)` `(II, 1.4.2)`, taking account of `(5.10.11.1)`. Since `ℋ^0_{X/Z}(ℱ)` is `Z`-closed `(5.9.11)`, `ρ_{X/Z}` is an isomorphism, hence so is `ρ_{X'/Z'}`. Since `X' − Z'` is the intersection of the filtered family of `V'_α = g⁻¹(V_α)`, where `V_α` runs through the filtered family of open sets containing `X − Z`, one deduces that `ℱ'` is `Z'`-closed when `X'` is locally Noetherian, by virtue of `(5.9.1)`.

**(5.10.13)**

<!-- label: IV.5.10.13 -->

We shall now apply the preceding results to the case where `Z` is one of the sets `Z^{(n)}(X)` (or simply `Z^{(n)}`), defined as the set of `x ∈ X` such that `dim(𝒪_x) ≥ n`; it is clear that `Z^{(n)}` is stable under specialization; for a closed part `T` of `X` to be contained in `Z^{(n)}`, it is necessary and sufficient that `codim(T, X) ≥ n`. We shall be interested here in the case `n = 2`.

**Proposition (5.10.14).**

<!-- label: IV.5.10.14 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module of support equal to `X`.*

*(i) For `ℱ` to verify `(S_1)`, it is necessary and sufficient that it be `Z^{(1)}`-pure.*

*(ii) For `ℱ` to verify `(S_2)`, it is necessary and sufficient that it be `Z^{(2)}`-closed and `Z^{(1)}`-pure, or equivalently that it be `Z^{(2)}`-closed and have no associated prime cycle of codimension `1`.*

(i) To say that `ℱ` possesses property `(S_1)` means that `ℱ` has no embedded associated prime cycle `(5.7.5)`, or equivalently that for every `x ∈ Ass(ℱ)`, one has `dim(ℱ_x) = 0` `(3.1.4)`, in other words `(5.1.12.1)` `dim(𝒪_x) = 0`; but this is equivalent to saying that `Ass(ℱ)` does not meet `Z^{(1)}`, and the conclusion follows from `(5.10.2)`.

(ii) To say that `ℱ` is `Z^{(2)}`-closed means that `prof_{Z^{(2)}}(ℱ) ≥ 2`, or equivalently that, for every `x ∈ X`, the relation `dim(𝒪_x) ≥ 2` entails `prof(ℱ_x) ≥ 2`; this shows that property `(S_2)` entails that `ℱ` is `Z^{(2)}`-closed; it entails in addition that `ℱ` verifies `(S_1)`, hence has no embedded associated prime cycle `(5.7.5)`, and since `Supp(ℱ) = X`, this still means that all the associated prime cycles of `ℱ` are of codimension `0`. Conversely, suppose that `ℱ` is `Z^{(2)}`-closed and has no associated prime cycle of codimension `1`; to see that `ℱ` verifies `(S_2)`, it remains to show that if `x ∈ X` is such that `dim(𝒪_x) = 1` (or, what amounts to the same, `dim(ℱ_x) = 1`), then one has `prof(ℱ_x) = 1`; but by hypothesis the relation `dim(𝒪_x) = 1` entails `x ∉ Ass(ℱ)`, and this last relation is equivalent to `prof(ℱ_x) ≠ 0`, that is, here, to `prof(ℱ_x) = 1`. If `ℱ` is `Z^{(1)}`-pure, hence verifies `(S_1)`, one has noted above that by virtue of the relation `Supp(ℱ) = X`, all the associated prime cycles of `ℱ` are of codimension `0`, hence what precedes applies.

One will note that it can happen that `ℱ` is `Z^{(2)}`-closed and does not verify `(S_1)`: this is the case for example when `X` is of dimension `1` (for then `Z^{(2)} = ∅`, and every `𝒪_X`-Module is `Z^{(2)}`-closed) and has embedded associated prime cycles.

Let us recall that in Chapter III, in the study of local cohomology, one gives a cohomological characterization of property `(S_n)` for every `n ≥ 1`, generalizing `(5.10.14)`.

**Corollary (5.10.15).**

<!-- label: IV.5.10.15 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module of support `X`. Assume that `ℱ` has no associated prime cycles of codimension `1` and that `ℱ' = ℋ^0_{X/Z^{(2)}}(ℱ)` is coherent. Then:*

*(i) `ℱ'` verifies property `(S_2)`.*

<!-- original page 120 -->

*(ii) The set `U` of `x ∈ X` such that `ℱ` verifies `(S_2)` at the point `x` `(5.7.2)` is open in `X`, and one has `codim(X − U, X) ≥ 2`.*

(i) One knows `(5.9.11)` that `ℱ'` is `Z^{(2)}`-closed, and moreover `Supp(ℱ') = X`, since the maximal points of `X` belong to `X − Z^{(2)}` and at these points `ℱ'_x = ℱ_x ≠ 0`, hence the support of `ℱ'` is dense in `X`, and since `ℱ'` is coherent, `Supp(ℱ')` is closed, hence equal to `X`. It remains to see that `ℱ'` has no associated prime cycle of codimension `1`. But if `x ∈ Ass(ℱ')` and `dim(ℱ'_x) = dim(𝒪_x) = 1`, one has `x ∈ X − Z^{(2)}`, hence, since `ℱ'_x = ℱ_x`, one would have `x ∈ Ass(ℱ)`, contrary to the hypothesis, which completes the proof of (i).

(ii) One has `Z^{(n)}(X_x) = Z^{(n)}(X) ∩ X_x`, with the notations of `(5.9.6)`, taking account of `(I, 2.4.2)`; on the other hand, the hypothesis that `ℱ` has no associated prime cycles of codimension `1` entails the same hypothesis for `ℱ̃_x`; for `ℱ̃_x` to verify `(S_2)`, it is therefore necessary and sufficient, by virtue of `(5.10.14)`, that `ℱ̃_x` be `Z^{(2)}(X_x)`-closed; assertion (ii) therefore follows from `(5.10.6)` and `(5.10.10, (iii))`.

**Proposition (5.10.16).**

<!-- label: IV.5.10.16 -->

*Let `X` be a locally Noetherian prescheme,*

```text
  X' = Spec(ℋ^0_{X/Z^{(2)}}(𝒪_X))
```

*its `Z^{(2)}`-closure, `g : X' → X` the structure morphism. Suppose that `X` has no associated prime cycle of codimension `1`.*

*(i) For `X` to verify `(S_2)` at a point `x ∈ X`, it is necessary and sufficient that the morphism `X'_x → X_x` deduced from `g` (notations of `(5.10.12)`) be an isomorphism. This condition is always verified if `codim(‾{x}, X) ≤ 1`.*

*(ii) Suppose moreover that `g` is a finite morphism (see in `(5.11.2)` sufficient conditions for this to be so). Then the set `U` of points where `X` verifies `(S_2)` is open and `codim(X − U, X) ≥ 2`; in addition `U` is the largest open set of `X` such that the restriction `g⁻¹(U) → U` of `g` is an isomorphism.*

*(iii) Under the same hypotheses as in (ii), `X'` satisfies `(S_2)` and for every `x' ∈ X'` such that `codim(‾{x'}, X') ≤ 1`, the point `x = g(x')` is such that `codim(‾{x}, X) = codim(‾{x'}, X')`.*

*(iv) The hypotheses being those of (ii), let `ℱ` be a coherent `𝒪_X`-Module of support `X` such that `ℋ^0_{X/Z^{(2)}}(ℱ)` is coherent; then the `𝒪_{X'}`-Module `ℱ'` such that `g_*(ℱ') = ℋ^0_{X/Z^{(2)}}(ℱ)` is coherent and verifies `(S_2)`, and its support is a union of irreducible components of `X'`.*

Assertions (i) and (ii) are inserted for memory, having already been proved in substance: (i) follows indeed from `(5.10.12, (i))` and `(5.10.14)`, and (ii) is a special case of `(5.10.15, (ii))`.

Let us prove (iii); set `x = g(x')`; since `g` is finite, so is the morphism `X'_x → X_x`, hence `dim(𝒪_{X',x'}) ≤ dim(X'_x) ≤ dim(X_x) = dim(𝒪_{X,x})` by virtue of `(5.4.1)`. Suppose first that `dim(𝒪_{X',x'}) ≤ 1` and let us show that then `dim(𝒪_{X,x}) ≤ 1`. Otherwise, one would have `x ∈ Z^{(2)}`, hence by virtue of `(5.10.12, (ii))` applied to `𝒪_X` one would have `prof(𝒪_{X',x'}) ≥ 2`, which is absurd. One has therefore `x ∈ X − Z^{(2)}`, and consequently `𝒪_{X',x'}` is isomorphic to `𝒪_{X,x}` `(5.10.12, (i))`, whence `dim(𝒪_{X',x'}) = dim(𝒪_{X,x})`. In addition, since `X` has no associated prime cycles

<!-- original page 121 -->

of codimension `1`, the hypothesis `dim(𝒪_{X,x}) = 1` entails `x ∉ Ass(𝒪_X)`, hence `prof(𝒪_{X,x}) = 1`, and consequently also `prof(𝒪_{X',x'}) = 1`. Suppose now `dim(𝒪_{X',x'}) ≥ 2`, hence `dim(𝒪_{X,x}) ≥ 2`, that is, `x ∈ Z^{(2)}`; one deduces that `prof(𝒪_{X',x'}) ≥ 2` by `(5.10.12, (ii))`. This establishes the assertions of (iii).

To prove (iv) it suffices to replace `𝒪_X` by `ℱ` in the preceding reasoning, which establishes that `ℱ'` verifies `(S_2)` and that if `dim(ℱ_x) ≤ 1`, `ℱ_x` and `ℱ'_{x'}` are di-isomorphic; in particular if `dim(ℱ_x) = 0`, one has `dim(ℱ'_{x'}) = 0`, hence `dim(𝒪_{X,x}) = 0` since `ℱ` has support `X`, and finally `dim(𝒪_{X',x'}) = 0`; every irreducible component of `Supp(ℱ')` is therefore an irreducible component of `X'`, since `ℱ'` is coherent, hence `Supp(ℱ')` closed.

**Proposition (5.10.17).**

<!-- label: IV.5.10.17 -->

*Let `A` be a Noetherian integral ring, and denote by `A^{(1)}` the intersection of the local rings `A_𝔭`, where `𝔭` runs through the set of prime ideals of `A` of height `1`. Suppose that `A^{(1)}` is a finite `A`-algebra. Then:*

*(i) The ring `A^{(1)}` verifies condition `(S_2)`.*

*(ii) The set `U` of `𝔭 ∈ Spec(A)` such that the canonical homomorphism `A_𝔭 → (A^{(1)})_𝔭` is bijective is equal to the set of `𝔭` such that `A_𝔭` verifies `(S_2)`; `U` is open in `X = Spec(A)` and one has `codim(X − U, X) ≥ 2`.*

*(iii) For every multiplicative part `S` of `A`, `(S⁻¹A)^{(1)}` is a finite `(S⁻¹A)`-algebra.*

*(iv) Let `B` be a finite `A`-algebra, integral and containing `A`. Then `B^{(1)}` is a finite `B`-algebra. Moreover, for every prime ideal `𝔮` of `B`, of height `1`, the prime ideal `𝔮 ∩ A` of `A` is of height `1`.*

If one takes account of formula `(5.9.3.1)`, one sees that `X' = Spec(A^{(1)})` is the `Z^{(2)}`-closure of `X = Spec(A)`; since `A` has no embedded associated prime ideals, properties (i) and (ii) are special cases of `(5.10.16, (i), (ii) and (iii))`. To prove (iii), it suffices to remark that one has `(S⁻¹A)^{(1)} = S⁻¹A^{(1)}`, which is a special case of `(5.9.4)`: indeed `S⁻¹A` is a flat `A`-module, the prime ideals of `S⁻¹A` are the ideals `S⁻¹𝔭`, where `𝔭 ∈ Spec(A)` does not meet `S`, and one has `ht(S⁻¹𝔭) = ht(𝔭)`. Since `A^{(1)}` is a finite `A`-algebra, `S⁻¹A^{(1)}` is a finite `S⁻¹A`-algebra, whence (iii).

To prove (iv), set `Y = Spec(B)`, and let `f : Y → X` be the structure morphism; since it is finite, it follows from `(5.4.1)` that for every `y ∈ Y`, one has `dim(𝒪_{Y,y}) ≤ dim(𝒪_{X,f(y)})`; hence, if `T = f⁻¹(Z^{(2)}(X))`, one has `T ⊃ Z^{(2)}(Y)`. Let us show that `𝒢 = ℋ^0_{X/Z^{(2)}(X)}(f_*(𝒪_Y))` is coherent; indeed `f_*(𝒪_Y) = B̃`, `B` being considered as `A`-module; but since `B` is a finite integral `A`-algebra, its field of fractions is finite over the field of fractions of `A`, hence `B` is contained in a free `A`-module of finite type, and consequently `(5.9.2, (i))` `𝒢` is a quasi-coherent `𝒪_X`-submodule of `(ℋ^0_{X/Z^{(2)}(X)}(𝒪_X))^n` for some suitable `n`; this latter being coherent by hypothesis, so is `𝒢`. Now, it follows from the definition `(5.9.1.2)` that `𝒢` is isomorphic to `f_*(ℋ^0_{Y/T}(𝒪_Y))`; this proves a fortiori that `ℋ^0_{Y/T}(𝒪_Y)` is a coherent `𝒪_Y`-Module. It then follows from `(5.10.10, (ii))`, applied to `𝒪_Y` and to the generic point of `Y`, that one has `codim(T, Y) ≥ 2`, that is, `T ⊂ Z^{(2)}(Y)`, and finally `T = Z^{(2)}(Y)`. This proves both assertions of (iv).

<!-- original page 122 -->

### 5.11. Coherence criteria for the Modules `ℋ^0_{X/Z}(ℱ)`

**Proposition (5.11.1).**

<!-- label: IV.5.11.1 -->

*Let `X` be a locally Noetherian prescheme, `Z` a part of `X` stable under specialization, `ℱ` a coherent `𝒪_X`-Module. Denote by `(x_α)` the family of points of `Ass(ℱ) ∩ (X − Z)` and, for each `α`, let `Y_α` be the reduced closed sub-prescheme of `X` having `‾{x_α}` as underlying space, `Z_α = Z ∩ ‾{x_α}`. The following two conditions are then equivalent:*

*a) `ℋ^0_{X/Z}(ℱ)` is a coherent `𝒪_X`-Module.*

*b) For every `α`, `ℋ^0_{Y_α/Z_α}(𝒪_{Y_α})` is a coherent `𝒪_{Y_α}`-Module.*

*These two conditions entail the following:*

*c) For every `α`, one has `codim(Z_α, Y_α) ≥ 2`.*

*Moreover, the three conditions a), b), c) are equivalent when in addition one of the following properties is verified:*

*(i) Every point of `X` admits an open neighbourhood isomorphic to a sub-scheme of a regular scheme (in which case one also says that `X` is **locally immersible in a regular scheme**).*

*(ii) For every `α`, `Y_α` is universally catenary `(5.6.2)` and its normalization `(II, 6.3.8)` `Ỹ_α` is finite over `Y_α`.*

All the properties envisaged are local on `X`, hence one may restrict to the case where `X = Spec(A)` is affine, `A` being a Noetherian ring, and `ℱ = M̃`, where `M` is an `A`-module of finite type. Then, for every `α`, if `h_α` is the canonical injection `Y_α → X`, `(h_α)_*(𝒪_{Y_α}) = 𝒢_α` is the `𝒪_X`-Module corresponding to the `A`-module quotient `A/𝔧_{x_α}`, and, by definition of `Ass(ℱ)`, this `A`-module is isomorphic to a sub-`A`-module of `M`. Since `ℋ^0_{X/Z}(𝒢_α)` is a quasi-coherent `𝒪_X`-submodule of `ℋ^0_{X/Z}(ℱ)` `(5.9.2)`, the hypothesis that `ℋ^0_{X/Z}(ℱ)` is coherent entails that so is `ℋ^0_{X/Z}(𝒢_α)`. On the other hand, it follows from the definition `(5.9.1.2)` that `ℋ^0_{X/Z}(𝒢_α)` is isomorphic to `(h_α)_*(ℋ^0_{Y_α/Z_α}(𝒪_{Y_α}))`; this proves that a) entails b). To see that b) entails a), it suffices to show that there is a finite filtration `(ℱ_i)_{0 ≤ i ≤ n}` of `ℱ` formed of coherent `𝒪_X`-Modules, with `ℱ_0 = ℱ`, `ℱ_n = 0`, and such that `ℋ^0_{X/Z}(ℱ_i/ℱ_{i+1})` is coherent for every `i`: this follows, by descending induction on `i`, from the exact sequences

```text
  0 → ℱ_{i+1} → ℱ_i → ℱ_i/ℱ_{i+1} → 0,
```

from the fact that `ℋ^0_{X/Z}` is a left exact functor `(5.9.2)`, and finally from `(0_I, 5.3.3)` and `(I, 6.1.1)`. By virtue of `(3.2.8)`, it therefore suffices to prove that `ℋ^0_{X/Z}(ℱ)` is coherent when `ℱ` is *irredundant*, that is, `Ass(M) = {𝔭}` is reduced to a single element. Let us now note the

**Lemma (5.11.1.1).**

<!-- label: IV.5.11.1.1 -->

*Let `A` be a Noetherian ring, `M` an `A`-module of finite type, such that `Ass(M) = {𝔭}`. There exists a finite filtration `(M_i)_{0 ≤ i ≤ r}` of `M` such that `M_0 = M`, `M_r = 0` and that `M_i/M_{i+1}` is isomorphic to a submodule of `A/𝔭`.*

Note first that the canonical homomorphism `M → M_𝔭 = N` is injective (Bourbaki, Alg. comm., chap. IV, §1, n° 2, prop. 6). Set `B = A_𝔭`, `𝔪 = 𝔭A_𝔭`, the maximal ideal of `B`; one has `Ass(N) = {𝔪}` (loc. cit., prop. 5), and since `N` is a `B`-module of finite type,

<!-- original page 123 -->

there exists an integer `r` such that `𝔪^r N = 0`; if one sets `N_j = 𝔪^j N` for `0 ≤ j ≤ r`, `N_j/N_{j+1}` is a `(B/𝔪)`-module of finite type, hence a direct sum of a finite number of submodules isomorphic to `B/𝔪`, since `B/𝔪` is a field; in other words, there is a finite filtration `(N_i)_{0 ≤ i ≤ r}` of `N` such that `N_r = 0` and that `N_i/N_{i+1}` is isomorphic to `B/𝔪`, i.e. to the field of fractions of `A/𝔭`; the filtration of `M_i = M ∩ N_i` answers the question, for `M_i/M_{i+1}` is isomorphic to a sub-`(A/𝔭)`-module of finite type of `N_i/N_{i+1} = B/𝔪`; but one knows that such a submodule is isomorphic to a submodule of `A/𝔭`.

The existence of the filtration `(M_i)` then shows, by the same reasoning as above, that to prove (granting b)) that `ℋ^0_{X/Z}(ℱ)` is coherent, one may restrict to showing that `ℋ^0_{X/Z}(ℋ)` is coherent, where `ℋ = (A/𝔭)^∼`, `𝔭` being an associated ideal of `M`. But if `𝔭 = 𝔧_y` with `y ∈ Z`, the support of `ℋ` is a closed set contained in `Z`, since `Z` is stable under specialization; the definition `(5.9.1.2)` then shows that `ℋ^0_{X/Z}(ℋ) = 0`. If on the contrary `𝔭 = 𝔧_{x_α}` for some `α`, one has `ℋ = (h_α)_*(𝒪_{Y_α})` by definition, and one has seen above that `ℋ^0_{X/Z}(ℋ)` is isomorphic to `(h_α)_*(ℋ^0_{Y_α/Z_α}(𝒪_{Y_α}))`, hence is coherent by virtue of hypothesis b).

One has already seen `(5.10.10, (ii))` that a) entails c). It remains to prove that, under one or the other of hypotheses (i), (ii), c) entails b). Note that if `X` verifies (i), so does each `Y_α`. It therefore suffices `(5.9.3.1)` to prove the

**Corollary (5.11.2).**

<!-- label: IV.5.11.2 -->

*Let `A` be a Noetherian integral ring, verifying one of the following two hypotheses:*

*(i) `A` is a quotient of a regular Noetherian ring.*

*(ii) `A` is universally catenary, and its integral closure `A'` is a finite `A`-algebra.*

*Then the ring `A^{(1)}`, intersection of the `A_𝔭` where `𝔭` runs through the set of prime ideals of `A` of height `1`, is a finite `A`-algebra.*

(i) Set `X = Spec(A)`. The set `U` of points `x ∈ X` where `X` verifies `(S_2)` is open in `X` under hypothesis (i) `(6.11.2)` [^1]. In addition, if one sets `Z = X − U`, one has `codim(Z, X) ≥ 2`: indeed, for every `x ∈ X` such that `dim(𝒪_x) ≤ 1`, one has `dim(𝒪_{x'}) ≤ 1` for every `x'` a generization of `x`, and since `𝒪_{x'}` is integral, `prof(𝒪_{x'}) ≥ 1`, hence `X` verifies `(S_2)` at the point `x`. One has therefore `Z ⊂ Z^{(2)}`, and `ℋ^0_{X/Z^{(2)}}(𝒪_X) = j_*(j*(𝒪_X))`, where `j : U → X` is the canonical injection `(5.9.1.2)`. But since the prescheme `U` verifies `(S_2)`, it follows from `(5.10.14)` that `ℋ^0_{U/Z^{(2)}(U)}(𝒪_U)` is isomorphic to `𝒪_U`; on the other hand, since `codim(Z, X) ≥ 2`, one knows, according to Chapter III, §9, that `j_*(𝒪_U)` is a coherent `𝒪_X`-Module, which proves the proposition in case (i).

(ii) The ring `A'` is, by virtue of hypothesis (ii), a Noetherian integral and integrally closed ring, hence (Bourbaki, Alg. comm., chap. VII, §1, n° 6, th. 4) the intersection of its local rings `A'_{𝔭'}`, where `𝔭'` runs through the set of prime ideals of height `1` of `A'`. Now, for such a prime ideal `𝔭'`, if one sets `𝔭 = 𝔭' ∩ A` and `S = A − 𝔭`, `A'_{𝔭'}` is a local ring at the prime ideal `S⁻¹𝔭'` of `S⁻¹A'`, and `S⁻¹A'` is by hypothesis

[^1]: The reader may verify that `(5.11.2)` is not used in the proof of `(6.11.2)`.

<!-- original page 124 -->

a finite `A_𝔭`-algebra; since `S⁻¹𝔭'` lies above the maximal ideal `𝔭A_𝔭` of `A_𝔭`, it is a maximal ideal of `S⁻¹A'`; but by virtue of hypothesis (ii) and of `(5.6.3, (i))`, `A_𝔭` is universally catenary. One deduces therefore from `(5.6.10)` that `dim(A_𝔭) = dim(A'_{𝔭'}) = 1`. It follows from this that one has `A^{(1)} ⊂ A'`, and since `A'` is by hypothesis a finite `A`-module, so is `A^{(1)}` since `A` is Noetherian; the proposition is therefore proved in case (ii).

**Remark (5.11.3).**

<!-- label: IV.5.11.3 -->

*The fact that `A^{(1)}` is a finite `A`-algebra is no longer necessarily exact if, in hypothesis (ii) of `(5.11.2)`, one assumes only that `A` is catenary. An example is given by the catenary local ring `A` constructed in `(5.6.11)`, whose integral closure `A'` (denoted `B` in `(5.6.11)`) is a finite `A`-algebra; if `A^{(1)}` were also a finite `A`-algebra, since it is contained in the field of fractions of `A`, it would be contained in `A'`. But on the other hand, with the notations of `(5.6.11)`, every prime ideal of height `1` in `A` is of the form `𝔭A`, where `𝔭` is a prime ideal of height `1` in `C`, and one has `A_{𝔭A} = C_𝔭`; one knows `(5.6.11)` that `C_𝔭 = E_{𝔭'}`, where `𝔭'` is the unique prime ideal of `E` above `𝔭`, hence `A_{𝔭A}` is integrally closed and consequently contains `A'`; by definition, one therefore has `A' ⊂ A^{(1)}`, and the hypothesis that `A^{(1)}` is a finite `A`-algebra would finally entail `A^{(1)} = A'`. But this conclusion is absurd, for one of the two prime ideals of `A'` above the maximal ideal `𝔫A` of `A` is of height `1`, whereas `𝔫A` is of height `2`, which would contradict `(5.10.17, (iv))`.*

**Corollary (5.11.4).**

<!-- label: IV.5.11.4 -->

*Let `X` be a locally Noetherian prescheme, `Z` a closed part of `X`, `U = X − Z`, `i : U → X` the canonical injection, `ℱ` a coherent `𝒪_U`-Module. For `i_*(ℱ)` to be a coherent `𝒪_X`-Module, it is necessary that for every `x ∈ Ass(ℱ)`, one has `codim(‾{x} ∩ Z, ‾{x}) ≥ 2`. This condition is sufficient in each of the two following cases:*

*(i) The prescheme `X` is locally immersible in a regular scheme.*

*(ii) The prescheme `X` is universally catenary and universally Japanese (which means, by definition, that every point `x ∈ X` admits an affine open neighbourhood whose ring is universally Japanese `(0, 23.1.1)`).*

One knows `(I, 9.4.7)` that there exists a coherent `𝒪_X`-submodule `𝒢` of `i_*(ℱ)` such that `𝒢|U = ℱ`. One evidently has `Ass(𝒢) ⊂ Ass(ℱ) ⊂ Ass(i_*(ℱ))`, and since

```text
  Ass(i_*(ℱ)) = Ass(ℱ)
```

`(3.1.13)`, one has `Ass(𝒢) = Ass(ℱ)`; it then suffices to apply `(5.11.1)` to the coherent `𝒪_X`-Module `𝒢`, noting that `i_*(ℱ) = ℋ^0_{X/Z}(𝒢)` and that, when `X` is universally catenary and universally Japanese, hypothesis (ii) of `(5.11.1)` is verified by definition.

**Corollary (5.11.5).**

<!-- label: IV.5.11.5 -->

*Let `X` be a locally Noetherian prescheme, `Z` a part of `X` stable under specialization, `ℱ` a coherent `𝒪_X`-Module such that one has `Ass(ℱ) ⊂ X − Z`. Then the condition:*

*a) `ℋ^0_{X/Z}(ℱ)` is a coherent `𝒪_X`-Module*

*implies the following:*

*d) For every part `T` of `Z` closed in `X` (or only for an increasing filtered family of closed parts `T` of `Z`, of union `Z`),*

<!-- original page 125 -->

*`i_*(ℱ|X − T)` (where `i : X − T → X` is the canonical injection) is coherent.*

*When `X` verifies one of the hypotheses (i), (ii) of `(5.11.1)`, a) and d) are equivalent.*

Note that one has `Ass(i_*(ℱ|X − T)) = Ass(ℱ)` by virtue of the hypothesis and of `(3.1.13)`; it follows therefore from `(5.10.2)` that the canonical maps

```text
  i_*(ℱ|X − T) → ℋ^0_{X/Z}(ℱ)
```

are *injective*; the fact that a) implies d) is therefore a consequence of this remark. Conversely, the condition d) implies, by virtue of `(5.11.1)`, that `codim(T ∩ Y_α, Y_α) ≥ 2` with the notations of `(5.11.1)`; consequently one has `codim(Z ∩ Y_α, Y_α) ≥ 2` since `Z` is the union of its parts which are closed in `X`, and the last assertion of the corollary follows from `(5.11.1)`.

**Corollary (5.11.6).**

<!-- label: IV.5.11.6 -->

*Let `A` be a Noetherian ring, `X = Spec(A)`. Consider the following properties:*

*a) For every integral quotient ring `B` of `A`, the ring `B^{(1)}` (notation of `(5.11.2)`) is a finite `B`-algebra.*

*b) For every coherent `𝒪_X`-Module `ℱ` and every part `Z` of `X`, stable under specialization, and such that for every `x ∈ Ass(ℱ) ∩ (X − Z)` one has `codim(‾{x} ∩ Z, ‾{x}) ≥ 2`, the `𝒪_X`-Module `ℋ^0_{X/Z}(ℱ)` is coherent.*

*c) For every closed part `T` of `X` and every coherent `𝒪_U`-Module `𝒢` (where `U = X − T`) such that for every `x ∈ Ass(𝒢)` one has `codim(‾{x} ∩ T, ‾{x}) ≥ 2`, `i_*(𝒢)` (where `i : U → X` is the canonical injection) is a coherent `𝒪_X`-Module.*

*d) For every integral quotient ring `B` of `A` and every ideal `𝔍` of height `≥ 2` in `B`, the ring `⋂_{𝔭 ⊉ 𝔍} B_𝔭` is a finite `B`-algebra.*

*One then has the implications*

```text
  a) ⇔ b) ⇒ c) ⇔ d).
```

*Moreover, the conditions a), b), c) and d) are verified in each of the two following cases:*

*(i) `A` is a quotient of a regular ring.*

*(ii) `A` is universally catenary and universally Japanese.*

Let `B = A/𝔮`, where `𝔮` is a prime ideal of `A`, so that `Y = Spec(B)` is the closed part `V(𝔮)` of `X`; set `Z = Z^{(2)}(Y)`, which is a part of `X` stable under specialization; since `B` is integral, `Ass(A/𝔮)` is reduced to the generic point `𝔮` of `Y`. If condition b) is verified, one can apply it to the coherent `𝒪_X`-Module `ℱ = (A/𝔮)^∼` and to `Z`, and by virtue of `(5.9.3.1)`, this shows that `B^{(1)}` is an `A`-module of finite type, and a fortiori a `B`-module of finite type. Conversely, suppose a) verified; then, if `ℱ` is a coherent `𝒪_X`-Module such that for every `x ∈ Ass(ℱ) ∩ (X − Z)` one has `codim(‾{x} ∩ Z, ‾{x}) ≥ 2`, one can apply (with the notations of `(5.11.1)`) to each of the affine schemes `Y_α = Spec(B_α)`, where `B_α` is an integral quotient ring of `A`, the result of a); since by hypothesis `Z_α` is contained in `Z^{(2)}(Y_α)`, condition a) (taking account of `(5.10.2)`

<!-- original page 126 -->

and of the fact that `Ass(𝒪_{Y_α})` is reduced to the generic point of `Y_α`) entails that `ℋ^0_{Y_α/Z_α}(𝒪_{Y_α})` is a coherent `𝒪_{Y_α}`-Module, and b) then follows from `(5.11.1)`.

To see that c) entails d), one reasons as above by applying c) to the case where `ℱ = (A/𝔮)^∼` and `Z = V(𝔍)`; conversely, one proves that d) entails c) by again using the equivalence of a) and b) in `(5.11.1)`. It is evident that c) is a special case of b). Finally, the fact that a) (and consequently each of the other conditions) is verified when `A` verifies one of the hypotheses (i), (ii) follows from `(5.11.2)`, given the definition of universally catenary rings and universally Japanese rings.

**Remarks (5.11.7).**

<!-- label: IV.5.11.7 -->

*(i) It is unknown whether, in `(5.11.5)`, condition d) implies a) without supplementary hypothesis on `X`; we shall see later `(7.2.4)` that it is indeed so when `X` is a local scheme. Likewise, we shall prove that when `A` is a local Noetherian ring the four properties a), b), c), d) of `(5.11.6)` are equivalent `(7.2.4)`. It is unknown whether this result extends to all Noetherian rings.*

*(ii) If `A` verifies property a) of `(5.11.6)`, so does every ring of fractions `S⁻¹A` and every finite `A`-algebra `C`. Indeed every integral quotient ring of `S⁻¹A` is of the form `S⁻¹(A/𝔮)`, where `𝔮` is a prime ideal of `A` not meeting `S`; and on the other hand, if `𝔯` is a prime ideal of `C`, `𝔭` its inverse image in `A`, `C/𝔯` is a finite integral `(A/𝔭)`-algebra containing `A/𝔭`; our assertions are therefore consequences of `(5.10.17, (iii) and (iv))`.*

### 5.12. Relations between the properties of a Noetherian local ring `A` and of a quotient ring `A/tA`

One has already seen in `(3.4)` relations between the properties of `A` and of `A/tA` concerning associated prime ideals, as well as the properties of being integral or reduced. One gives in this section other relations between the properties of these rings, linked to the notions of dimension and depth.

**Proposition (5.12.1).**

<!-- label: IV.5.12.1 -->

*Let `A` be a Noetherian local ring, `X = Spec(A)`, `t` an element of `A` belonging to a system of parameters `(0, 16.3.6)`, `X_0` the closed subspace `V(t)` of `X`, `X_1` the complementary open set `X − X_0`. Let `Z` be a part of `X` such that every specialization of a point of `Z` belongs to `Z`. Suppose that `X` is biequidimensional (which will be the case if `A` is equidimensional and a quotient of a regular local ring `(0, 16.5.12)`). Then if one sets `Z_0 = Z ∩ X_0`, `Z_1 = Z ∩ X_1`, one has*

```text
  codim(Z_0, X_0) ≤ codim(Z, X) ≤ codim(Z_1, X_1).                  (5.12.1.1)
```

The second inequality follows from the definition `(5.1.3)`; to prove the first, one may restrict to proving it when `Z` is closed: indeed, by hypothesis `Z` is the union of closed parts `Z_α`, and if one has `codim(X_0 ∩ Z_α, X_0) ≤ codim(Z_α, X)` for every `α`, one will also have `codim(Z_0, X_0) = inf_α(codim(X_0 ∩ Z_α, X_0)) ≤ inf_α(codim(Z_α, X)) = codim(Z, X)`. Suppose therefore `Z` closed, so that one has

```text
  codim(Z, X) = dim(X) − dim(Z)
```

<!-- original page 127 -->

by virtue of `(0, 14.3.5.1)`. On the other hand, `X_0` is evidently catenary, equidimensional and of dimension `dim(X) − 1` by virtue of `(0, 16.3.4)`; one therefore also has

```text
  codim(Z_0, X_0) = dim(X_0) − dim(Z_0) = dim(X) − 1 − dim(Z_0).
```

But one has `dim(Z_0) ≥ dim(Z) − 1` `(0, 16.3.4)`, which completes the proof of the first inequality `(5.12.1.1)`.

**Proposition (5.12.2).**

<!-- label: IV.5.12.2 -->

*Let `A` be a Noetherian local ring, `M` an `A`-module of finite type, `t` an `M`-regular element belonging to the maximal ideal `𝔪` of `A`, `k` an integer `≥ 1`. Assume that `A` is a catenary ring. Then, if `M/tM` is equidimensional and satisfies `(S_k)`, so is `M`.*

Taking account of `(Err_III, 30)` and of `(5.7.3, (vi))`, one may restrict to the case where `Supp(M) = Spec(A) = X`. Set `X_0 = V(t) = Spec(A/tA)`; since `M/tM` verifies `(S_1)` by hypothesis, it has no embedded associated prime ideals `(5.7.5)`. Applying `(3.4.4)` at the closed point of `X` (and of any closed sub-prescheme of `X`), one sees that the irreducible components of `Supp(M/tM)` are exactly those of `Y_i ∩ X_0`, where `Y_i` `(1 ≤ i ≤ r)` are the irreducible components of `X`. Since `t` is by hypothesis `M`-regular, `V(t)` contains no maximal point of `X` `(3.1.8)`; each of the irreducible components of `Y_i ∩ X_0` is therefore of codimension `1` in `Y_i` `(5.1.8)`; since `X` is catenary and all the irreducible components of `Supp(M/tM)` have by hypothesis the same dimension, one concludes that the `Y_i` all have the same dimension, in other words `X` is equidimensional, hence biequidimensional since `A` is local and catenary. To see that `M` verifies `(S_k)`, apply criterion `(5.7.4)`: one must verify (with the notations of `(5.7.4)`) that, for every integer `n ≥ 0`, one has `codim(Z_n, X) > n + k`. Now, the hypothesis on `M/tM` and criterion `(5.7.4)` show that one has `codim(Z_n ∩ X_0, X_0) > n + k` for every integer `n ≥ 0`. But every specialization of a point of `Z_n` still belongs to `Z_n`, as we shall see in `(6.11.5)` [^2]; since `X` is biequidimensional and `t` belongs to a system of parameters for `M` `(0, 16.4.1)`, hence also for `A` (the annihilator of `M` being nilpotent by virtue of the hypothesis `Supp(M) = Spec(A)`), the conclusion follows from `(5.12.1)`.

**Remark (5.12.3).**

<!-- label: IV.5.12.3 -->

*If, in the statement of `(5.12.2)`, one assumes only that `M/tM` is equidimensional, it does not necessarily follow that `M` is equidimensional. For example, let `k` be a field, `B` the polynomial ring `k[T, U, V]` in `3` indeterminates, `C` the local ring of `B` at the maximal ideal `BT + BU + BV` of `B`, and let `𝔭 = CU`, `𝔮 = CV + C(T + U)`; consider then the local ring `A = C/𝔭𝔮` (geometrically, if `X` is the closed sub-prescheme of affine space of `3` dimensions over `k`, formed of a plane and a line cutting this plane at a point `x`, `A` is the local ring of `X` at the point `x`). Let `t`, `u`, `v` be the canonical images of `T`, `U`, `V` in `A`; it is immediate that `t` is not a zero-divisor in `A`, and `A/tA` is isomorphic to `C_0/𝔭_0 𝔮_0`, where `C_0` is the local ring of `B_0 = k[U, V]` at the maximal ideal `B_0 U + B_0 V`, and `𝔭_0 = C_0 U`, `𝔮_0 = C_0 U + C_0 V` (`𝔮_0` being therefore the maximal ideal of `C_0`). It is immediate that `Spec(A/tA)`*

[^2]: The reader will verify that `(5.12.2)` is not used for the proof of `(6.11.5)`.

<!-- original page 128 -->

*is irreducible and of dimension `1`, `A/tA` does not verify `(S_1)` and `Spec(A)` is not equidimensional.*

**Corollary (5.12.4).**

<!-- label: IV.5.12.4 -->

*Let `A` be a Noetherian catenary local ring, `t` a regular element belonging to the maximal ideal of `A`, `k` an integer `≥ 1`. If `A/tA` verifies `(S_k)`, so does `A`.*

If `k = 1`, the corollary follows from `(3.4.4)`, given the interpretation of condition `(S_1)` `(5.7.5)`. If `k ≥ 2`, it follows from the Hartshorne criterion `(5.10.9)` that `A/tA` is equidimensional, and one may apply `(5.12.2)`.

**Proposition (5.12.5).**

<!-- label: IV.5.12.5 -->

*Let `A` be a Noetherian catenary local ring, `t` a regular element of `A` belonging to the maximal ideal of `A`, `k` an integer `≥ 0`. If the ring `A/tA` is reduced, equidimensional and verifies property `(R_k)`, the ring `A` also possesses these three properties.*

One knows already `(3.4.6)` that `A` is reduced, and it follows from `(5.12.2)`, applied for `k = 1`, that `A` is equidimensional. Set `X = Spec(A)`, `X_0 = V(t) = Spec(A/tA)`, and let `Z` be the set of points `x ∈ X` where `X` is not regular; by virtue of `(0, 17.3.2)` every specialization of a point of `Z` belongs to `Z`. It follows on the other hand from `(0, 17.1.8)` that for every point `x ∈ X_0` where `X_0` is regular, `X` is also regular, hence the set `Z_0'` of points where `X_0` is not regular contains `Z_0 = Z ∩ X_0`; the hypothesis therefore entails that

```text
  k ≤ codim(Z_0', X_0) ≤ codim(Z_0, X_0).
```

But, since `A` is equidimensional and catenary, one has, according to `(5.12.1)`

```text
  codim(Z_0, X_0) ≤ codim(Z, X)
```

which proves that `X` verifies `(R_k)`.

**Remark (5.12.6).**

<!-- label: IV.5.12.6 -->

*If, in the statement of `(5.12.5)`, one assumes only that `A/tA` is reduced and possesses property `(R_k)`, it does not necessarily follow that `A` possesses property `(R_k)`. For example, let `k` be a field, `P(U, V)` an irreducible polynomial of `k[U, V]` such that the curve `Γ` defined by the principal ideal `(P)` in the affine plane `Spec(k[U, V])` has a singular point corresponding to the maximal ideal `(U) + (V)` (for example `P(U, V) = U(U^2 + V^2) + (U^2 − V^2)`, which gives a cubic with a double point). Let then `B` be the polynomial ring in `4` indeterminates `k[T, U, V, W]`, `C` the local ring of `B` at the maximal ideal `BT + BU + BV + BW`, and let*

```text
  𝔭 = CW + CP(U − T, V),    𝔮 = CU.
```

*Consider then the local ring `A = C/𝔭𝔮` (geometrically, if `X` is the closed sub-prescheme of affine space of `4` dimensions, formed of a hyperplane `H` and of a `2`-dimensional "cylinder" `L` whose "base" is the curve `Γ` and whose "singular line" `Y` is not contained in the hyperplane `H`, then `A` is the local ring of `X` at the point `x` where `Y` meets `H`). One then sees at once that `Spec(A/tA)` (where `t` is the canonical image of `T` in `A`) has as unique singular point `x`, whose local ring is `A/tA` itself, which is reduced and of dimension `2`; on the contrary, the generic point `y` of the "singular line" `Y` (defined by the image in `A` of the ideal `C(U − T) + CV + CW`) is a singular point of `X`, and `𝒪_{X,y}` is of dimension `1`; in other words, `A/tA` is reduced and verifies `(R_1)`, but `A` does not verify `(R_1)`.*

<!-- original page 129 -->

**Corollary (5.12.7).**

<!-- label: IV.5.12.7 -->

*Let `A` be a Noetherian catenary local ring, `t` a regular element of `A` belonging to the maximal ideal of `A`. If `A/tA` is integral and integrally closed, so is `A`.*

By virtue of Serre's criterion `(5.8.6)` and of the fact that the ring `A` is local, it suffices to show that `Spec(A)` verifies `(S_2)` and `(R_1)`. But the hypothesis on `A/tA` entails that `A` verifies `(R_1)` by `(5.12.5)`, and that `A` verifies `(S_2)` by `(5.12.4)`.

**Proposition (5.12.8) (Hironaka's lemma).**

<!-- label: IV.5.12.8 -->

*Let `A` be a reduced, equidimensional and catenary Noetherian local ring. Assume in addition that for every minimal prime ideal `𝔮_i` of `A`, the ring `B_i = A/𝔮_i` is such that `B_i^{(1)}` (notation of `(5.10.17)`) is a finite `B_i`-algebra (which will be the case for example when `A` possesses one of the properties (i), (ii) of `(5.11.6)`). Let `t` be an element of `A`, not a zero-divisor in `A`, and such that:*

*(i) The `A`-module `A/tA` has only one non-embedded associated prime ideal `𝔭` (necessarily of height `1` by virtue of the Hauptidealsatz `(0, 16.3.2)`, but one does not assume that this is the only associated prime ideal of `A/tA`).*

*(ii) The ideal `𝔭A_𝔭` of `A_𝔭` is generated by `t/1`.*

*(iii) The ring `A/𝔭` is integrally closed.*

*Under these conditions, the ring `A` is integral and integrally closed, and one has `𝔭 = tA`.*

If `Z = V(tA)`, hypothesis (i) entails that `Z` is an irreducible closed part of `X = Spec(A)`, whose generic point `z` is such that `𝔧_z = 𝔭`. Hypothesis (ii) shows that the maximal ideal `𝔭A_𝔭` of the Noetherian local ring `A_𝔭` is generated by a single element, hence `A_𝔭` is a discrete valuation ring of which `t/1` is a uniformizer (Bourbaki, Alg. comm., chap. VI, §3, n° 6, prop. 9); `A_𝔭/tA_𝔭` is the residue field of `A_𝔭`, hence an `A_𝔭`-module of length `1`. By virtue of `(3.4.2)`, this entails that `Z` is contained in only one of the irreducible components `X_i` of `X`; for every other irreducible component `X_j` of `X`, one consequently has `dim(X_j ∩ Z) < dim(Z)`. On the other hand, since `t` is not a zero-divisor in `A`, it is contained in none of the `𝔮_i`, and one consequently has `(5.1.8)` `codim(X_i ∩ Z, X_i) = codim(X_j ∩ Z, X_j) = 1`, whatever `j ≠ i`. Since `A` is supposed biequidimensional, the relation `dim(X_i ∩ Z) ≠ dim(X_j ∩ Z)` would therefore entail `dim(X_i) ≠ dim(X_j)` `(0, 14.3.3.1)`, which is absurd. One sees therefore that there is only one minimal prime ideal in `A`; since `A` is by hypothesis reduced, this entails that it is integral. Note now that since `A^{(1)}` is a finite `A`-algebra, it is a Noetherian semi-local ring, and every non-embedded associated prime ideal of `A^{(1)}/tA^{(1)}` is therefore of height `1` by virtue of the Hauptidealsatz `(0, 16.3.2)`; now, for such an ideal `𝔯`, `𝔯 ∩ A` is of height `1` by virtue of `(5.10.17, (iv))` and since it contains `tA`, it can only be `𝔭` by virtue of hypothesis (i). On the other hand, `A^{(1)}` is contained in the integral closure `A'` of `A`; setting `S = A − 𝔭`, the integral closure of `A_𝔭` is `S⁻¹A'` (Bourbaki, Alg. comm., chap. V, §1, n° 5, prop. 17), hence `S⁻¹A' = A_𝔭` since `A_𝔭` is a discrete valuation ring; it follows (loc. cit., §2, n° 1, lemme 1) that there exists only one prime ideal `𝔭'` of `A'` above `𝔭`, and a fortiori only one prime ideal `𝔭^{(1)}` of `A^{(1)}` above `𝔭`, and one has `A_𝔭 = A'_{𝔭'} = A^{(1)}_{𝔭^{(1)}}`. Note now that `A^{(1)}` verifies `(S_2)` `(5.10.17, (i))` and since `t` is not a zero-divisor in `A^{(1)}`, `A^{(1)}/tA^{(1)}` has no embedded associated prime ideals

<!-- original page 130 -->

`(5.7.7)`. The ideal `𝔭^{(1)}` is therefore the only associated prime ideal of `A^{(1)}/tA^{(1)}`, in other words `tA^{(1)}` is a `𝔭^{(1)}`-primary ideal of `A^{(1)}`; this means again that `tA^{(1)}` is the inverse image in `A^{(1)}` of `tA^{(1)}_{𝔭^{(1)}} = tA_𝔭`, and this latter is the maximal ideal of `A_𝔭` according to (ii); hence `tA^{(1)} = 𝔭^{(1)}` is prime in `A^{(1)}`. On the other hand, `A^{(1)}/𝔭^{(1)}` is finite over `A/𝔭` and has the same field of fractions (namely, the residue field of `A^{(1)}_{𝔭^{(1)}} = A_𝔭`), hence it is identical to `A/𝔭` by virtue of hypothesis (iii). One may therefore write `A^{(1)} = A + 𝔭^{(1)} = A + tA^{(1)}`, and since `t` is contained in the radical of the Noetherian semi-local ring `A^{(1)}`, Nakayama's lemma entails `A^{(1)} = A`, whence `𝔭^{(1)} = 𝔭 = tA`. But since `A` is catenary and `A/tA` integral and integrally closed by virtue of hypothesis (iii), one concludes from `(5.12.7)` that `A` is integrally closed. Q.E.D.

**Remark (5.12.9).**

<!-- label: IV.5.12.9 -->

*The conclusion of `(5.12.8)` fails if one no longer assumes `A` equidimensional. For example, let `k` be a field, `B` the polynomial ring `k[X, Y, Z]` in three indeterminates, `C` the ring `B/𝔯_1 𝔯_2`, where `𝔯_1 = BZ` and `𝔯_2 = BX + BY`; let `𝔪` be the maximal ideal `BX + BY + BZ`, `𝔫 = 𝔪/𝔯_1 𝔯_2` its image in `C`, `A` the local ring `C_𝔫`. Finally, let `t_0` be the image in `C` of the element `Y + Z` of `B`, `t` its image in `A` (`Spec(C)` is therefore formed of a plane `P` and of a line `D` not contained in this plane, `Spec(C/t_0 C)` of a line `D'` contained in `P` and passing through the point `D ∩ P`). The ring `A` is reduced and catenary (being a quotient of a regular ring) and its minimal prime ideals `𝔮_1`, `𝔮_2` are the images of `𝔯_1`, `𝔯_2`. The `A`-module `A/tA` has only one non-embedded associated prime ideal `𝔭`, image of `BY + BZ`, `𝔭A_𝔭` is generated by `t/1` and `A/𝔭` is isomorphic to `k[X]`; but `A` is not integral.*

**Corollary (5.12.10).**

<!-- label: IV.5.12.10 -->

*Let `A` be a Noetherian integral local ring, verifying one of the following hypotheses:*

*a) `A` is a quotient of a regular ring.*

*b) `A` is universally catenary and universally Japanese.*

*Let `(x_i)_{1 ≤ i ≤ n}` be a sequence of `n` elements of `A`; set `𝔍 = x_1 A + ⋯ + x_n A`, and suppose the following conditions are verified:*

*(i) There exists only one non-embedded associated prime ideal `𝔭` of `A/𝔍` and `𝔭` is of height `n`.*

*(ii) The maximal ideal `𝔭A_𝔭` of `A_𝔭` is generated by the `x_i/1` (hence `A_𝔭` is a regular local ring of dimension `n`).*

*(iii) The ring `A/𝔭` is integrally closed.*

*Under these conditions, for every integer `i` such that `0 ≤ i ≤ n`, the quotient ring `A/(x_1 A + ⋯ + x_i A)` is integrally closed and of dimension `dim(A) − i`. In particular, `𝔍` is prime, equal to `𝔭`, `A` is integrally closed and `(x_i)_{1 ≤ i ≤ n}` is an `A`-regular sequence.*

Let us proceed by induction on `n`, the proposition being trivial for `n = 0` and reducing to Hironaka's lemma `(5.12.8)` for `n = 1`. One may therefore assume `n ≥ 2`. Let `𝔍' = x_1 A + ⋯ + x_{n−1} A`, and let `𝔮` be a minimal prime ideal among those containing `𝔍'`; one has `ht(𝔮) ≤ n − 1` `(0, 16.3.1)`; let us show that `𝔮 ⊂ 𝔭`. Indeed, if `𝔭'` is minimal among the prime ideals of `A` containing `𝔮 + x_n A`, `𝔭'/𝔮` is of height `1` in `A/𝔮` by the Hauptidealsatz `(0, 16.3.2)`, hence `𝔭'` is of height `≤ n` since `A` is catenary `(0, 16.1.4)`; but since it contains `𝔍`, it is necessarily equal to `𝔭`, whence `𝔮 ⊂ 𝔭`,

<!-- original page 131 -->

and `𝔮` is induced on `A` by a prime ideal of `A_𝔭`, minimal among those containing `𝔍'A_𝔭`. But by virtue of hypothesis (ii) and of `(0, 17.1.7)`, `𝔍'A_𝔭` is prime in `A_𝔭`, hence `𝔮 = A ∩ 𝔍'A_𝔭` is *the* unique non-embedded associated prime ideal of `A/𝔍'` and it is of height `n − 1`, since `𝔍'A_𝔭` is of height `n − 1` and `𝔮` of height `≤ n − 1`. In addition `𝔮A_𝔮 = 𝔍'A_𝔮` and since `A_𝔮 = (A_𝔭)_𝔮`, the maximal ideal `𝔮A_𝔮` is generated by `𝔍'`. One sees therefore that the sequence `(x_i)_{1 ≤ i ≤ n−1}` already verifies conditions (i) and (ii) of the statement. Let us show that it also verifies (iii). Consider for this the integral ring `B = A/𝔮`, and let `t` be the canonical image of `x_n` in `B`. It is immediate (cf. `(5.6.3, (iv))`) that if `A` verifies hypothesis a) (resp. b)), so does `B`; since `x_n ∉ 𝔮`, one has `t ≠ 0`; let us show that `B` and `t` verify the hypotheses of Hironaka's lemma. Indeed, a prime ideal `𝔫` of `B` minimal among those containing `t` is the image of a prime ideal of `A` minimal among those containing `𝔮 + x_n A`, and one has seen that `𝔭` is this unique ideal; since `B_𝔫 = A_𝔭/𝔮A_𝔭` and `𝔫B_𝔫 = 𝔭A_𝔭/𝔮A_𝔭`, the fact that `𝔮A_𝔭 = 𝔍'A_𝔭` and that `𝔭A_𝔭` is generated by `𝔍` entails that `𝔫B_𝔫` is generated by `t`. Finally, `B/𝔫 = A/𝔭` is integrally closed. The application of `(5.12.8)` proves therefore that `B = A/𝔮` is integrally closed and that `𝔭 = 𝔮 + x_n A`. Let us now use the induction hypothesis, which shows that `A/(x_1 A + ⋯ + x_i A)` is integrally closed and of dimension `dim(A) − i` for `0 ≤ i ≤ n − 1` and that `𝔮 = 𝔍'`, whence `𝔭 = 𝔍' + x_n A = 𝔍`. One concludes that `A/𝔍 = A/𝔭` is integrally closed; since `dim(A_𝔭) = n` and `dim(A/𝔭) = dim(A) − dim(A_𝔭)` since `A` is biequidimensional, this completes the proof.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/iv/17-c4-s05-dimension-profondeur-regularite.md;
     PDF: ~/Code/pdfs/ega/EGA-IV-2.pdf -->

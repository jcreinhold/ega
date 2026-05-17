# §7. Valuative criteria

In this section we give valuative criteria of separation and properness for a
morphism — that is, criteria that bring in an auxiliary variable scheme of the
form `Spec(A)`, where `A` is a valuation ring. Under suitable "Noetherian"
hypotheses, one may restrict in these criteria to the case where `A` is a
_discrete_ valuation ring. This will doubtless be the only case we shall have
to apply in what follows, and we have introduced arbitrary valuation rings, in
the general case, only in order to make the connection with classical
developments.

<!-- original page 138 -->

## 7.1. Reminders on valuation rings

**(7.1.1)**

<!-- label: II.7.1.1 -->

Among the various equivalent properties characterising valuation rings, we
shall use the following: a ring `A` is called a _valuation ring_ if it is an
integral ring that is not a field and if, in the set of local rings contained
in the field of fractions `K` of `A` and distinct from `K`, `A` is maximal for
the relation of domination `(I, 8.1.1)`. Recall that a valuation ring is
_integrally closed_. If `A` is a valuation ring, then `A_𝔭` is also a valuation
ring for every prime ideal `𝔭 ≠ (0)` of `A`.

**(7.1.2)**

<!-- label: II.7.1.2 -->

Let `K` be a field and `A` a local subring of `K` that is not a field;

<!-- original page 139 -->

there then exists a valuation ring having `K` as its field of fractions and
dominating `A` (`[1], p. 1-07, lemma 2`).

On the other hand, let `B` be a valuation ring, `k` its residue field, `K` its
field of fractions, and `L` an extension of `k`. Then there exists a _complete_
valuation ring `C` that dominates `B` and whose residue field is `L`. Indeed,
`L` is an algebraic extension of a pure transcendental extension
`L' = k(T_μ)_{μ∈M}`; we know that one can extend the valuation of `K`
corresponding to `B` to a valuation of `K' = K(T_μ)_{μ∈M}` in such a way that
`L'` is the residue field of this valuation (`[24], p. 98`); replacing `B` by
the completion of the ring of this extended valuation, we see that we may
restrict to the case where `B` is complete and `L` is an algebraic closure of
`k`. If `K̄` is an algebraic closure of `K`, we can then extend to `K̄` the
valuation that defines `B`, and the corresponding residue field is an algebraic
closure of `k`, as one sees by lifting to `K̄` the coefficients of a monic
polynomial of `k[T]`. We are thus finally reduced to the case where `L = k`,
and it then suffices to take `C` to be the completion of `B` in order to settle
the question.

**(7.1.3)**

<!-- label: II.7.1.3 -->

Let `K` be a field and `A` a subring of `K`; the integral closure `A'` of `A`
in `K` is the intersection of the valuation rings containing `A` and having `K`
as field of fractions (`[11], p. 51, th. 2`). Proposition (7.1.2) is expressed
in the following equivalent geometric form:

**Proposition.**

<!-- label: II.7.1.4 -->

Let `Y` be a prescheme, `p : X → Y` a morphism, `x` a point of `X`,
`y = p(x)`, and `y' ≠ y` a specialisation `(0, 2.1.2)` of `y`. There then
exists a local scheme `Y'`, spectrum of a valuation ring, and a separated
morphism `f : Y' → Y` such that, if `a` denotes the unique closed point of `Y'`
and `b` the generic point of `Y'`, one has `f(a) = y'` and `f(b) = y`. One may
further suppose that one of the two additional properties below is satisfied:

(i) `Y'` is the spectrum of a complete valuation ring whose residue field is
algebraically closed, and there exists a `κ(y)`-homomorphism `κ(x) → κ(b)`.

(ii) There exists a `κ(y)`-isomorphism `κ(x) ⥲ κ(b)`.

**Proof.** Let `Y₁` be the closed reduced subprescheme of `Y` having `{y}̄` as
its underlying space `(I, 5.2.1)`, and let `X₁` be the closed subprescheme
given by the inverse image `p⁻¹(Y₁)`; since `y' ∈ {y}̄` by hypothesis and since
`κ(x)` is the same in `X` and in `X₁`, we may suppose `Y` integral, with
generic point `y`; `𝒪_{y'}` is then an integral local ring that is not a field
and whose field of fractions is `𝒪_y = κ(y)`, and `κ(x)` is an extension of
`κ(y)`. In order to satisfy the conditions `f(a) = y'` and `f(b) = y` as well
as the additional condition (i) (resp. (ii)), we take `Y' = Spec(A')`, where
`A'` is a valuation ring dominating `𝒪_{y'}` and which is complete with
residue field algebraically closed extension of `κ(x)` (resp. a valuation ring
`A'` dominating `𝒪_{y'}` and whose field of fractions is `κ(x)`); the
existence of `A'` is guaranteed by (7.1.2).

**(7.1.5)**

<!-- label: II.7.1.5 -->

Recall that a local ring `A` is said to be _of dimension `1`_ if there exists
a prime ideal distinct from the maximal ideal `𝔪` and if every prime ideal of
`A` distinct from `𝔪` is a _minimal_ prime ideal; when `A` is _integral_, this
amounts to saying that `𝔪` and `(0)` are the only prime ideals and `𝔪 ≠ (0)`;
in other words, `Y = Spec(A)` is reduced to two

<!-- original page 140 -->

points `a` and `b`: `a` is the unique _closed_ point, `𝔧_a = 𝔪`, and
`κ(a) = k` is the _residue field_ `k = A/𝔪`; `b` is the _generic point_ of
`Y`, `𝔧_b = (0)`, the set `{b}` being the unique open subset of `Y` distinct
from both `∅` and `Y` (an open subset which is therefore _everywhere dense_),
and `κ(b) = K` is the _field of fractions_ of `A`.

**(7.1.6)**

<!-- label: II.7.1.6 -->

For a local ring `A`, Noetherian and of dimension `1`, we know
(`[1], p. 2-08 and 17-01`) that the following conditions are equivalent:

(a) `A` is normal;

(b) `A` is regular;

(c) `A` is a valuation ring;

furthermore, `A` is then a _discrete valuation ring_. Propositions (7.1.2) and
(7.1.3) then have the following analogues for discrete valuation rings:

**Proposition.**

<!-- label: II.7.1.7 -->

Let `A` be an integral local Noetherian ring that is not a field, `K` its
field of fractions, and `L` an extension of finite type of `K`. There then
exists a discrete valuation ring having `L` as its field of fractions and
dominating `A`.

**Proof.** Suppose first `L = K`. Let `𝔪` be the maximal ideal of `A`,
`(x₁, …, x_n)` a system of nonzero generators of `𝔪`, and `B` the subring
`A[x₂/x₁, …, x_n/x₁]` of `K`, which is Noetherian. It is immediate that the
ideal `𝔪B` of `B` is identical to the principal ideal `x₁B`; if `𝔭` is a
minimal prime ideal of `x₁B`, we know that `𝔭` is of rank `1`
(`[13], t. I, p. 277`); in other words, `B_𝔭` is a local Noetherian ring _of
dimension `1`_; it is clear that `𝔭B_𝔭 ∩ A` is an ideal of `A` containing
`𝔪` and not containing `1`, hence equal to `𝔪`, so that `B_𝔭` _dominates_ `A`
`(I, 8.1.1)`. It follows from the Krull–Akizuki theorem (`[25], p. 293`) that
the integral closure `C` of `B_𝔭` is a Noetherian ring (although `C` is not
necessarily a `B_𝔭`-module of finite type); if `𝔫` is a maximal ideal of `C`,
then `C_𝔫` is a normal local Noetherian ring of dimension `1`
(`[25], p. 295`), hence a discrete valuation ring, which dominates `B_𝔭` and
_a fortiori_ `A`.

If now `L` is an extension of finite type of `K`, we may, by what precedes,
restrict to the case where `A` is already a discrete valuation ring. Let `w`
be a valuation of `K` associated to `A`; there exists a discrete valuation
`w'` of `L` that _extends_ `w`: indeed, by induction on the number of
generators of `L`, we reduce to the case `L = K(α)`, and then the proposition
is classical (`[24], p. 106`).

**Corollary.**

<!-- label: II.7.1.8 -->

Let `A` be a Noetherian integral ring, `K` its field of fractions, and `L` an
extension of finite type of `K`. Then the integral closure of `A` in `L` is the
intersection of the discrete valuation rings having `L` as field of fractions
and containing `A`.

**Proof.** Indeed, such a discrete valuation ring, being normal, contains _a
fortiori_ every element of `L` that is integral over `A`. It thus suffices to
prove that if `x ∈ L` is not integral over `A`, then there exists a discrete
valuation ring `C` having `L` as field of fractions, containing `A`, and not
containing `x`. The hypothesis on `x` means that `x ∉ B = A[1/x]`, in other
words, that `1/x` is not invertible in the Noetherian ring `B`. There is thus
a prime ideal `𝔭` of `B` containing `1/x`. The integral local ring `B_𝔭` is
Noetherian and contained in `L`, which is an extension of finite type of the
field of fractions of `B_𝔭` (the latter containing `K`). By virtue of (7.1.7)
there is then a discrete valuation ring `C` dominating `B_𝔭` and having `L`
as field of fractions; since `1/x ∈ 𝔭B_𝔭` belongs to the maximal ideal of
`C`, we have `x ∉ C`, which concludes the proof.

The geometric form of (7.1.7) is the following:

<!-- original page 141 -->

**Proposition.**

<!-- label: II.7.1.9 -->

Let `Y` be a locally Noetherian prescheme, `p : X → Y` a morphism locally of
finite type, `x` a point of `X`, `y = p(x)`, and `y' ≠ y` a specialisation of
`y`. There then exists a local scheme `Y'`, spectrum of a discrete valuation
ring, a separated morphism `f : Y' → Y`, and a `Y`-rational map `g` from `Y'`
to `X` such that, denoting the closed point of `Y'` by `a` and its generic
point by `b`, one has `f(a) = y'`, `f(b) = y`, `g(b) = x`, and such that in
the commutative diagram

```text
                       κ(x)
                      ↗     ↘ γ
                   π /        ↘
                    /           ↘
              κ(y) ────φ────→ κ(b)                                       (7.1.9.1)
```

(where `π`, `φ`, `γ` are the homomorphisms corresponding to `p`, `f`, `g`
respectively), `γ` is a bijection.

**Proof.** As in (7.1.4), we may reduce to the case where `Y` is integral with
generic point `y` (taking `(I, 6.3.4, (iv))` into account); since the question
is local on `X` and `Y`, we may assume `p` of finite type; we are then in the
situation of (7.1.4), with the additional property that `κ(x)` is an extension
of finite type of `κ(y)` `(I, 6.4.11)` and `𝒪_{y'}` is Noetherian; this
permits us to apply (7.1.7) and take `Y' = Spec(A')`, where `A'` is a discrete
valuation ring dominating `𝒪_{y'}` and whose field of fractions is `κ(x)`. We
have thus defined a commutative diagram (7.1.9.1) where `γ` is a bijection,
and `π` and `φ` correspond to the morphisms `p` and `f`. Furthermore, since
`X` and `Y` are locally Noetherian `(I, 6.6.2)` and `Y'` is integral, there is
exactly one `Y`-rational map `g` from `Y'` to `X` to which corresponds the
isomorphism `γ` `(I, 7.1.15)`, which finishes the proof.

## 7.2. Valuative criterion of separation

**Proposition.**

<!-- label: II.7.2.1 -->

Let `X`, `Y` be two preschemes, and `f : X → Y` a quasi-compact morphism. The
following two conditions are equivalent:

(a) The morphism `f` is closed.

(b) For every `x ∈ X` and every specialisation `y'` of `y = f(x)` distinct
from `y`, there exists a specialisation `x'` of `x` such that `f(x') = y'`.

**Proof.** Condition (b) expresses that `f({x}̄) = {y}̄` and is thus a
consequence of (a). To show that (b) implies (a), consider a closed subset
`X'` of the underlying space `X`; let `Y' = f(X')̄` and let us show that
`Y' = f(X')`. Consider the closed reduced subpreschemes of `X` and `Y` having
`X'` and `Y'` respectively as their underlying spaces `(I, 5.2.1)`; there is
then a morphism `f' : X' → Y'` such that the diagram

```text
   X' ──f'──→ Y'
   │          │
   ↓          ↓
   X  ──f──→  Y
```

commutes `(I, 5.2.2)`, and since `f` is quasi-compact, so too is `f'`. We are
thus reduced to proving that if `f` is a quasi-compact and _dominant_
morphism, then

<!-- original page 142 -->

condition (b) implies that `f(X) = Y`. Indeed, let `y'` be a point of `Y`, and
let `y` be the generic point of an irreducible component of `Y` containing
`y'`; by (b), it suffices to show that `f⁻¹(y)` is not empty. But this
property is a consequence of the fact that `f` is dominant and quasi-compact
`(I, 6.6.5)`.

**Corollary.**

<!-- label: II.7.2.2 -->

Let `f : X → Y` be a quasi-compact immersion morphism. For the underlying
space `X` to be closed in `Y`, it is necessary and sufficient that it contain
every specialisation (in `Y`) of each of its points.

**Proposition.**

<!-- label: II.7.2.3 -->

Let `Y` be a prescheme (resp. a locally Noetherian prescheme), `f : X → Y` a
morphism (resp. a morphism locally of finite type). The following conditions
are equivalent:

(a) `f` is separated.

(b) The diagonal morphism `X → X ×_Y X` is quasi-compact, and for every
`Y`-prescheme of the form `Y' = Spec(A)`, where `A` is a valuation ring (resp.
a discrete valuation ring), any two `Y`-morphisms from `Y'` to `X` that
coincide at the generic point of `Y'` are equal.

(c) The diagonal morphism `X → X ×_Y X` is quasi-compact, and for every
`Y`-prescheme of the form `Y' = Spec(A)`, where `A` is a valuation ring (resp.
a discrete valuation ring), any two `Y'`-sections of `X' = X_{(Y')}` that
coincide at the generic point of `Y'` are equal.

**Proof.** The equivalence of (b) and (c) results from the bijective
correspondence between `Y`-morphisms from `Y'` to `X` and `Y'`-sections of
`X'` `(I, 3.3.14)`. If `X` is separated over `Y`, condition (b) is satisfied
by virtue of `(I, 7.2.2.1)`, since `Y'` is integral. It remains to prove that
(b) implies that the diagonal morphism `Δ : X → X ×_Y X` is closed, and it
comes to the same to show that it satisfies the criterion of (7.2.2). So let
`z` be a point of the diagonal `Δ(X)`, and `z' ≠ z` a specialisation of `z`
in `X ×_Y X`. There exists then (7.1.4) a valuation ring `A` and a morphism
`f` from `Y' = Spec(A)` to `X ×_Y X` which sends the closed point `a` of `Y'`
to `z'` and the generic point `b` of `Y'` to `z`; this morphism makes `Y'`
into an `(X ×_Y X)`-prescheme, and _a fortiori_ a `Y`-prescheme. If we compose
`f` with the two projections of `X ×_Y X`, we obtain two `Y`-morphisms `g₁`,
`g₂` from `Y'` to `X`, which by hypothesis coincide at the point `b`; they
are therefore equal to a single morphism `g`, which means `(I, 5.3.1)` that
`f` factors as `f = Δ ∘ g`, whence `z' ∈ Δ(X)`. When one supposes `Y`
locally Noetherian and `f` locally of finite type, `X ×_Y X` is locally
Noetherian `(I, 6.6.7)`; one may then take up the preceding argument by
supposing that `A` is a discrete valuation ring, by virtue of (7.1.9).

**Remarks.**

<!-- label: II.7.2.4 -->

(i) The hypothesis that the morphism `Δ` is quasi-compact is always satisfied
when `Y` is locally Noetherian and `f` locally of finite type, since
`X ×_Y X` is then locally Noetherian `(I, 6.6.4, (i))`. In the general case,
it also means that for every covering `(U_α)` of `X` by affine opens, the
sets `U_α ∩ U_β` are quasi-compact.

(ii) For `f` to be separated, it suffices that condition (b) or condition
(c) be satisfied for a valuation ring `A` which is _complete_ and whose
residue field is _algebraically closed_; this follows in fact from the proof
of (7.2.3) and from (7.1.4).

<!-- original page 143 -->

## 7.3. Valuative criterion of properness

**Proposition.**

<!-- label: II.7.3.1 -->

Let `A` be a valuation ring, `Y = Spec(A)`, `b` the generic point of `Y`, `X`
an integral _scheme_, and `f : X → Y` a _closed_ morphism such that `f⁻¹(b)`
reduces to a single point `x` and the corresponding homomorphism
`κ(b) → κ(x)` is bijective. Then `f` is an isomorphism.

**Proof.** Since `f` is closed and dominant, `f(X) = Y`; it suffices
`(I, 4.2.2)` to prove that for every `y' ≠ b` in `Y` there exists exactly one
point `x'` such that `f(x') = y'` and the corresponding homomorphism
`𝒪_{y'} → 𝒪_{x'}` is bijective, for then `f` will be a homeomorphism. Now if
`f(x') = y'`, `𝒪_{x'}` is a local ring contained in `K = κ(x) = κ(b)` and
dominating `𝒪_{y'}`; the latter is the local ring `A_{y'}`, hence a valuation
ring (7.1.1) having `K` as field of fractions. On the other hand,
`𝒪_{x'} ≠ K`, since `x'` is not the generic point of `X` `(0, 2.1.3)`; we
conclude that `𝒪_{x'} = 𝒪_{y'}`. Since `X` is an integral scheme, the
relation `𝒪_{x'} = 𝒪_{x''}` entails `x' = x''` `(I, 8.2.2)`, which concludes
the proof.

**(7.3.2)**

<!-- label: II.7.3.2 -->

Let `A` be a valuation ring, `Y = Spec(A)`, `b` the generic point of `Y`, so
that `𝒪_b = κ(b)` is equal to `K`, the field of fractions of `A`; let
`f : X → Y` be a morphism. We know `(I, 7.1.4)` that the _rational
`Y`-sections_ of `X` are in bijective correspondence with the _germs_ of
`Y`-sections (defined in neighbourhoods of `b`) at the point `b`, whence a
canonical map

```text
  Γ_rat(X/Y) → Γ(f⁻¹(b)/Spec(K))                                          (7.3.2.1)
```

the elements of `Γ(f⁻¹(b)/Spec(K))` being identified, by definition
`(I, 3.4.5)`, with the points of `f⁻¹(b) = X ⊗_A K` that are rational over
`K`. When `f` is _separated_, it follows from `(I, 5.4.7)` that the map
(7.3.2.1) is _injective_, since `Y` is an integral scheme.

Composing (7.3.2.1) with the canonical map
`Γ(X/Y) → Γ_rat(X/Y)` `(I, 7.1.2)`, we obtain a canonical map

```text
  Γ(X/Y) → Γ(f⁻¹(b)/Spec(K)).                                             (7.3.2.2)
```

When `f` is _separated_, this map is again _injective_ `(I, 5.4.7)`.

**Proposition.**

<!-- label: II.7.3.3 -->

Let `A` be a valuation ring with field of fractions `K`, `Y = Spec(A)`, `b`
the generic point of `Y`, and `f : X → Y` a _separated_ and _closed_
morphism. Then the canonical map (7.3.2.2) is bijective (which amounts to
saying that it is _surjective_, and implies that the rational `Y`-sections of
`X` are _everywhere defined_).

**Proof.** Let `x` be a point of `f⁻¹(b)` rational over `K`. Since `f` is
separated, so too is the morphism `f⁻¹(b) → Spec(K)` corresponding to `f`
`(I, 5.5.1, (iv))`, and every section of `f⁻¹(b)` being a closed immersion
`(I, 5.4.6)`, `{x}` is closed in `f⁻¹(b)`. Consider the closed reduced
subprescheme `X'` of `X` having for underlying space the closure `{x}̄` of
`{x}` in `X`. It is clear that the restriction of `f` to `X'` verifies the
hypotheses of (7.3.1), and is therefore an isomorphism of `X'` onto `Y`,
whose inverse isomorphism is the sought-for `Y`-section of `X`.

**(7.3.4)**

<!-- label: II.7.3.4 -->

To state the two following results, we make use of a terminology that will be
justified and discussed in chapter IV: if `F` is a subset

<!-- original page 144 -->

of a prescheme `Y`, we call _codimension of `F` in `Y`_, denoted
`codim_Y F`, the lower bound of the integers `dim(𝒪_z)` as `z` runs through
`F`.

**Corollary.**

<!-- label: II.7.3.5 -->

Let `Y` be a locally Noetherian reduced prescheme, `N` the set of points
`y ∈ Y` where `Y` is not regular `(0, 4.1.4)`; suppose that
`codim_Y N ≥ 2`. Let `f : X → Y` be a morphism of finite type, both separated
and closed, and let `g` be a rational `Y`-section of `X`; if `Y'` is the set
of points of `Y` where `g` is not defined (a set which is closed
`(I, 7.2.1)`), then `codim_Y Y' ≥ 2`.

**Proof.** It suffices to prove that `g` is defined at every point `z ∈ Y`
such that `dim 𝒪_z ≤ 1`. If `dim 𝒪_z = 0`, `z` is the generic point of an
irreducible component of `Y` `(I, 1.1.14)`, so belongs to every everywhere
dense open subset of `Y`, and in particular to the domain of definition of
`g`. Suppose then that `dim 𝒪_z = 1`; `𝒪_z` is then by hypothesis a regular
Noetherian local ring, hence (7.1.6) a discrete valuation ring. Let
`Z = Spec(𝒪_z)`; since `U = Y ∖ Y'` is everywhere dense, `U ∩ Z` is not empty
`(I, 2.4.2)`; let `g'` be the rational map from `Z` to `X` induced by `g`
`(I, 7.2.8)`; it suffices to show that `g'` is a _morphism_ `(I, 7.2.9)`.
Now, `g'` may be regarded as a rational `Z`-section of the `Z`-prescheme
`f⁻¹(Z) = X ×_Y Z`; it is clear that the morphism `f⁻¹(Z) → Z` corresponding
to `f` is closed, and it follows from `(I, 5.5.1, (i))` that it is
separated; we conclude from (7.3.3) that `g'` is everywhere defined; since
`Z` is reduced and `X` is separated over `Y`, `g'` is a morphism
`(I, 7.2.2)`.

**Corollary.**

<!-- label: II.7.3.6 -->

Let `S` be a locally Noetherian prescheme, and `X`, `Y` two `S`-preschemes;
suppose `Y` reduced and, furthermore, that the set `N` of points `y ∈ Y`
where `Y` is not regular is such that `codim_Y N ≥ 2`; suppose finally that
the structure morphism `X → S` is proper. Let `f` be an `S`-rational map
from `Y` to `X`, and let `Y'` be the set of points of `Y` where `f` is not
defined; then `codim_Y Y' ≥ 2`.

**Proof.** We know `(I, 7.1.2)` that the `S`-rational maps from `Y` to `X`
may be identified with the `Y`-rational sections of `X ×_S Y`; since the
structure morphism `X ×_S Y → Y` is closed (5.4.1), we may apply (7.3.5),
whence the corollary.

**Remark.**

<!-- label: II.7.3.7 -->

The hypotheses made on `Y` in (7.3.5) and (7.3.6) will be satisfied in
particular when `Y` is _normal_ `(0, 4.1.4)`, by virtue of (7.1.6).

We can characterise the universally closed (resp. proper) morphisms by a
converse of (7.3.3):

**Theorem.**

<!-- label: II.7.3.8 -->

Let `Y` be a prescheme (resp. a locally Noetherian prescheme), `f : X → Y` a
quasi-compact separated morphism (resp. a morphism of finite type). The
following conditions are equivalent:

(a) `f` is universally closed (resp. proper).

(b) For every `Y`-scheme of the form `Y' = Spec(A)`, where `A` is a valuation
ring (resp. a discrete valuation ring) with field of fractions `K`, the
canonical map

```text
  Hom_Y(Y', X) → Hom_Y(Spec(K), X)
```

corresponding to the canonical injection `A → K` is surjective (resp.
bijective).

<!-- original page 144 (cont.) → 145 -->

(c) For every `Y`-scheme of the form `Y' = Spec(A)`, where `A` is a
valuation ring (resp. a discrete valuation ring), the canonical map (7.3.2.2)
relative to the `Y'`-prescheme `X_{(Y')}` is surjective (resp. bijective).

**Proof.** The equivalence of (b) and (c) follows immediately from
`(I, 3.3.14)`. (a) implies (c), since (a) entails, in either hypothesis, that
`f_{(Y')}` is separated `(I, 5.5.1, (iv))` and closed, and it suffices to
apply (7.3.3). It remains to prove that (b) implies (a). Place ourselves
first in the case where `Y` is arbitrary, `f` separated and quasi-compact.
If condition (b) is satisfied by `f`, it is also satisfied by
`f_{(Y'')} : X_{(Y'')} → Y''`, where `Y''` is an arbitrary `Y`-prescheme, by
virtue of the equivalence of (b) and (c) and of the fact that
`X_{(Y'')} ×_{Y''} Y' = X ×_Y Y'` for every morphism `Y' → Y''`
`(I, 3.3.9.1)`; since moreover `f_{(Y'')}` is separated and quasi-compact
when `f` is `(I, 5.5.1, (iv) and 6.6.4, (iii))`, we are reduced to proving
that (b) implies that `f` is closed. For this, it suffices to verify
condition (b) of (7.2.1). Let then `x ∈ X`, `y'` a specialisation of
`y = f(x)`, distinct from `y`; by virtue of (7.1.4), there is a scheme `Y'`,
spectrum of a valuation ring, and a separated morphism `g : Y' → Y` such
that, if `a` denotes the closed point and `b` the generic point of `Y'`,
one has `g(a) = y'`, `g(b) = y`, and there exists a `κ(y)`-homomorphism
`κ(x) → κ(b)`. The latter corresponds canonically to a `Y`-morphism
`Spec(κ(b)) → X` `(I, 2.4.6)`, and it follows from (b) that there exists a
`Y`-morphism `h : Y' → X` to which the previous morphism corresponds. We
then have `h(b) = x`; if we set `h(a) = x'`, then `x'` is a specialisation
of `x`, and we have `f(x') = f(h(a)) = g(a) = y'`.

If now `Y` is locally Noetherian and `f` of finite type, hypothesis (b)
implies first that `f` is _separated_, by virtue of (7.2.3), the diagonal
morphism `X → X ×_Y X` being quasi-compact (7.2.4). Moreover, to verify
that `f` is proper, it suffices to show that
`f_{(Y'')} : X_{(Y'')} → Y''` is closed for every `Y`-prescheme `Y''` of
finite type, taking (5.6.3) into account. Since `Y''` is then locally
Noetherian, we may resume the reasoning made in the first case, taking for
`Y'` a spectrum of a discrete valuation ring and applying (7.1.9) instead
of (7.1.4).

**Remarks.**

<!-- label: II.7.3.9 -->

(i) When `Y` is an arbitrary prescheme and `f` a separated morphism, for
`f` to be universally closed, it suffices that condition (b) or condition
(c) be satisfied for the valuation rings `A` that are _complete_ and whose
residue field is _algebraically closed_; this follows from the proof above
and from (7.1.4).

(ii) From criterion (c) of (7.3.8) we deduce a new proof of the fact that a
projective morphism `X → Y` is closed (5.5.3), closer to the classical
methods. One may indeed suppose `Y` affine, and consequently `X` identified
with a closed subprescheme of a projective bundle `ℙ_Y^n` (5.3.3); to prove
that `X → Y` is closed, it suffices to verify that the structure morphism
`ℙ_Y^n → Y` is closed, and criterion (c) of (7.3.8), combined with
(4.1.3.1), shows that we are reduced to proving the following fact: _if
`Y` is the spectrum of a valuation ring `A` with field of fractions `K`,
every point of `ℙ_Y^n` with values in `K` comes (by restriction to the
generic point of `Y`) from a point of `ℙ_Y^n` with values in `A`._ Indeed,
every invertible `𝒪_Y`-module is trivial `(I, 2.4.8)`; therefore, by
(4.2.6), a point of `ℙ_Y^n` with values in `K` is identified with a class
of elements `(ζc₀, ζc₁, …, ζc_n)` of `K`, where `ζ ≠ 0` and the `c_i` are
elements of `K` not all zero. Now, by multiplying the `c_i` by an element
of `A` of

<!-- original page 145 → 146 -->

suitable valuation, one may suppose that the `c_i` all belong to `A` and
that at least one of them is invertible. But then (4.2.6) the system
`(c₀, …, c_n)` also defines a point of `ℙ_Y^n` with values in `A`, which
proves our assertion.

(iii) The criteria (7.2.3) and (7.3.8) are especially convenient when one
considers the data of a `Y`-prescheme `X` as equivalent to the data of the
functor

```text
  X(Y') = Hom_Y(Y', X)
```

in a `Y`-prescheme `Y'`; these criteria will allow us, for example, to
prove that under certain conditions the "Picard schemes" are proper.

**Corollary.**

<!-- label: II.7.3.10 -->

Let `Y` be an integral scheme (resp. an integral locally Noetherian
scheme), `X` an integral scheme, and `f : X → Y` a dominant morphism.

(i) If `f` is quasi-compact and universally closed, every valuation ring
whose field of fractions is the field `R(X)` of rational functions on `X`
and which dominates a local ring of `Y` also dominates a local ring of `X`.

(ii) Conversely, suppose `f` of finite type, and that the property stated
in (i) is satisfied by every valuation ring (resp. every discrete
valuation ring) having `R(X)` as field of fractions. Then `f` is proper.

**Proof.** Note first that the hypotheses imply, in any case, that `f` is
separated `(I, 5.5.9)`.

(i) Let `K = R(Y)`, `L = R(X)`, `y` a point of `Y`, `A` a valuation ring
having `L` as field of fractions and dominating `𝒪_y`; the injection
`𝒪_y → A` defines a morphism `h` of `Y' = Spec(A)` into `Y` `(I, 2.4.4)`
such that `h(a) = y`, in which we denote by `a` the closed point of `Y'`;
moreover, if `η` is the generic point of `Y`, which is also that of
`Spec(𝒪_y)`, one has `h(b) = η`, denoting by `b` the generic point of `Y'`
(since `K ⊂ L` by hypothesis). If `ξ` is the generic point of `X`, one has
`κ(ξ) = κ(b) = L` by hypothesis, whence a `Y`-morphism `g : Spec(L) → X`
such that `g(b) = ξ`; by virtue of (7.3.8), `g` comes from a `Y`-morphism
`g' : Y' → X`. If `x = g'(a)`, it is clear that `A` dominates `𝒪_x`.

(ii) The question being local on `Y`, we may always suppose `Y` affine
(resp. affine and Noetherian). Since `f` is of finite type, we may apply
Chow's lemma (5.6.1) in both cases. There is then a projective morphism
`p : P → Y`, an immersion morphism `j : X' → P`, and a projective,
surjective, and birational morphism `g : X' → X` (with `X'` integral)
such that the diagram

```text
   P ←──j── X'
   │        │
  p│       g│
   ↓        ↓
   Y ←──f── X
```

commutes. It suffices to prove that `j` is a _closed_ immersion, for then
`f ∘ g = p ∘ j` will be a projective morphism, hence proper, and since
`g` is surjective, `f` will also be proper (5.4.3). Let `Z` be the closed
reduced subprescheme of `P` having `j(X')̄` as underlying space
`(I, 5.2.1)`; since `X'` is integral, `j` factors as `i ∘ h`, where
`i : Z → P` is the canonical injection, `h : X' → Z` a dominant open
immersion `(I, 5.2.3)`, and `Z` is integral;

<!-- original page 146 → 147 -->

moreover, `Z` is projective over `Y`, and we see that we may restrict to
the case where `P` is integral and `j` dominant and birational, and
everything reduces to seeing that `j` is surjective. So let `z ∈ P`;
`𝒪_z` is an integral (resp. integral and Noetherian) local ring whose
field of fractions is

```text
  L = R(P) = R(X') = R(X).
```

We may restrict to the case where `z` is not the generic point of `P`.
There is consequently (7.1.2 and 7.1.7) a valuation ring (resp. a
discrete valuation ring) `A` having `L` as field of fractions and
dominating `𝒪_z`. _A fortiori_, `A` dominates `𝒪_y`, putting `y = p(z)`,
and by hypothesis there is then an `x ∈ X` such that `A` dominates `𝒪_x`.
Since `g` is proper, the first part of the proof shows that `A` also
dominates some `𝒪_{x'}` for an `x' ∈ X'`; it follows that `𝒪_z` and
`𝒪_{j(x')} = 𝒪_{x'}` are allied `(I, 8.1.4)`, and since `P` is a scheme,
this entails `z = j(x')` `(I, 8.2.2)`, which concludes the proof.

**Corollary.**

<!-- label: II.7.3.11 -->

Let `X`, `Y` be two integral schemes, `f : X → Y` a dominant, quasi-compact
and universally closed morphism. Suppose moreover `Y` affine of (integral)
ring `B`. Then `Γ(X, 𝒪_X)` is canonically isomorphic to a subring of the
integral closure of `B` in `R(X)`.

**Proof.** Indeed `(I, 8.2.1.1)`, `Γ(X, 𝒪_X)` is identified with the
intersection of the `𝒪_x` for `x ∈ X`; by virtue of (7.3.10), (7.1.2)
and (7.1.3), `Γ(X, 𝒪_X)` is consequently contained in the intersection
of the valuation rings containing `B` and having `R(X)` as field of
fractions; the conclusion then follows from (7.1.3).

**Remarks.**

<!-- label: II.7.3.12 -->

Under the hypotheses of (7.3.11), and when one supposes that `R(X)` is an
extension of finite type of `R(Y)`, one will be able in many cases to
conclude that `Γ(X, 𝒪_X)` is a module of finite type over the ring
`B = Γ(Y, 𝒪_Y)`. This will be the case for example when `B` is an algebra
of finite type over a field, for one knows then that the integral closure
of `B` in an extension of finite type of its field of fractions is a
`B`-module of finite type (`[13], t. I, p. 267, th. 9`); the conclusion
then follows from (7.3.11) and from the fact that `B` is Noetherian.

In particular, _a scheme `X` proper and affine over a field `K` is finite._
Indeed, by virtue of (1.6.4), (5.4.6) and `(I, 6.4.4, c))`, one may
restrict to the case where `X` is reduced. Furthermore, it will suffice to
prove that each of the closed subpreschemes of `X` having for underlying
space an irreducible component of `X` (of which there are finitely many)
is finite over `K`, so that (taking (5.4.5) into account) one is finally
reduced to the case where `X` is integral. But then the result follows
from the remarks made above.

In chapter III we shall recover this last proposition by other methods
and as a consequence of more general results, showing that if
`f : X → Y` is proper and `Y` locally Noetherian, `f_*(ℱ)` is coherent
for every coherent `𝒪_X`-module `ℱ` (`III, 4.4.2`).

Let us note finally that the criterion (7.3.10) is taken as the
_definition_ of proper morphisms in classical algebraic geometry. We have
mentioned it only for that reason, criterion (7.3.8) seeming more
manageable in all the applications known to us.

<!-- original page 147 → 148 -->

## 7.4. Algebraic curves and function fields of dimension `1`

The aim of this number is to show how the classical notion of algebraic
curve (as it is presented, for example, in the book of C. Chevalley
`[23]`) is formulated in the language of schemes. _Throughout this number,
`k` denotes a field, all schemes considered are `k`-schemes of finite
type, and all morphisms are `k`-morphisms._

**Proposition.**

<!-- label: II.7.4.1 -->

Let `X` be a prescheme of finite type over `k` (hence Noetherian); let
`x_i` (`1 ≤ i ≤ n`) be the generic points of the irreducible components
`X_i` of `X`, and let `K_i = κ(x_i)` (`1 ≤ i ≤ n`). The following
conditions are equivalent:

(a) Each of the `K_i` is an extension of `k` whose transcendence degree
is equal to `1`.

(b) For every closed point `x` of `X`, the local ring `𝒪_x` is of
dimension `1` (7.1.5).

(c) The irreducible closed subsets of `X` distinct from the `X_i` are
the closed points of `X`.

**Proof.** Since `X` is quasi-compact, every irreducible closed subset
`F` of `X` contains a closed point `(0, 2.1.3)`. By virtue of
`(I, 2.4.2)`, there is a bijective correspondence between the prime
ideals of `𝒪_x` and the irreducible closed subsets of `X` containing `x`
`(I, 1.1.14)`; the equivalence of (b) and (c) follows immediately. On
the other hand, if `𝔭_α` (`1 ≤ α ≤ r`) are the minimal prime ideals of
the Noetherian local ring `𝒪_x`, the local rings `𝒪_x/𝔭_α` are integral
and have for fields of fractions the `K_i` such that `x ∈ X_i`.
Furthermore, we know (`[1], p. 4-06, th. 2`) that the dimension of a
local integral `k`-algebra of finite type is equal to the transcendence
degree over `k` of its field of fractions. Finally, the dimension of
`𝒪_x` is the upper bound of the dimensions of the `𝒪_x/𝔭_α`; now,
condition (a) implies that these dimensions are equal to `1`, so (a)
implies (b); conversely, if `𝒪_x` is of dimension `1`, none of the
`𝔭_α` can be equal to the maximal ideal of `𝒪_x`, otherwise `𝒪_x` would
be of dimension `0`; therefore each of the `𝒪_x/𝔭_α` is of dimension
`1`, which shows that (b) entails (a).

We note that under the conditions of (7.4.1) the set `X` is _empty or
infinite_, as follows immediately from `(I, 6.4.4)`.

**Definition.**

<!-- label: II.7.4.2 -->

We call an _algebraic curve over `k`_ a nonempty algebraic _scheme_ over
`k` satisfying the conditions of (7.4.1).

In the language of dimension, which will be introduced in chapter IV,
this is expressed by saying that an algebraic curve over `k` is a
nonempty algebraic `k`-scheme all of whose irreducible components are of
dimension `1`.

We note that if `X` is an algebraic curve over `k`, the closed reduced
subpreschemes `X_i` (`1 ≤ i ≤ n`) of `X` having for underlying spaces
the irreducible components of `X` are algebraic curves over `k`.

**Corollary.**

<!-- label: II.7.4.3 -->

Let `X` be an irreducible algebraic curve. The only non-closed point of
`X` is its generic point. The closed subsets of `X` distinct from `X`
are the finite sets of closed points; these are also the only subsets
of `X` that are not everywhere dense.

**Proof.** If a point `x ∈ X` is not closed, its closure in `X` is an
irreducible closed subset of `X`, hence necessarily the whole of `X`
by virtue of (7.4.1), and consequently

<!-- original page 148 → 149 -->

`x` is the generic point of `X`. A closed subset `F` of `X` distinct
from `X` cannot contain the generic point of `X`, so all its points
are closed (in `X`, and _a fortiori_ in `F`); by considering the closed
reduced subprescheme of `X` having `F` as underlying space
`(I, 5.2.1)`, it follows therefore from `(I, 6.2.2)` that `F` is finite
and discrete. The closure in `X` of an infinite subset of `X` is
therefore necessarily equal to `X`.

When `X` is an arbitrary algebraic curve, applying (7.4.3) to the
irreducible components of `X` shows that the only non-closed points of
`X` are the generic points of those components.

**Corollary.**

<!-- label: II.7.4.4 -->

Let `X` and `Y` be two irreducible algebraic curves over `k`, and
`f : X → Y` a `k`-morphism. For `f` to be dominant, it is necessary and
sufficient that `f⁻¹(y)` be finite for every `y ∈ Y`.

**Proof.** Indeed, if `f` is not dominant, `f(X)` is necessarily a
finite subset of `Y` by virtue of (7.4.3), so it is not possible that
`f⁻¹(y)` be finite for every point of `Y`, since otherwise `X` would
be finite, which is absurd (7.4.1). Conversely, if `f` is dominant,
for every `y ∈ Y` distinct from the generic point `η` of `Y`,
`f⁻¹(y)` is closed in `X` since `{y}` is closed in `Y` (7.4.3); on the
other hand, by hypothesis, `f⁻¹(y)` does not contain the generic point
`ξ` of `X`, hence is finite by virtue of (7.4.3). Finally, to see that
when `f` is dominant, `f⁻¹(η)` is finite, one notes that the fibre
`f⁻¹(η)` is an irreducible scheme of finite type over `κ(η)`, with
generic point `ξ` (`I, 6.3.9 and 6.4.11`). Since `κ(ξ)` and `κ(η)` are
extensions of finite type of `k`, of the same transcendence degree
`1`, `κ(ξ)` is necessarily an extension of finite degree of `κ(η)`,
hence `ξ` is closed in `f⁻¹(η)` `(I, 6.4.2)`, and `f⁻¹(η)` is
consequently reduced to the point `ξ`.

We shall see in chapter III that a proper morphism `f : X → Y` of
Noetherian preschemes such that `f⁻¹(y)` is finite for every
`y ∈ Y` is necessarily _finite_; it will then follow from (7.4.4) that
a proper dominant morphism from an irreducible algebraic curve to an
algebraic curve is finite.

**Corollary.**

<!-- label: II.7.4.5 -->

Let `X` be an algebraic curve over `k`. For `X` to be regular, it is
necessary and sufficient that `X` be normal, or again that the local
rings of its closed points be discrete valuation rings.

**Proof.** This follows immediately from condition (b) of (7.4.1) and
from (7.1.6).

**Corollary.**

<!-- label: II.7.4.6 -->

Let `X` be a reduced algebraic curve, and `𝒜` a reduced coherent
`𝒪(X)`-algebra; then the integral closure `X'` of `X` relative to `𝒜`
(6.3.4) is a normal algebraic curve, and the canonical morphism
`X' → X` is finite.

**Proof.** The fact that `X' → X` is finite follows from (6.3.10); `X'`
is therefore an algebraic `k`-scheme; moreover, if `x_i`
(`1 ≤ i ≤ n`) are the generic points of the irreducible components of
`X`, `x'_j` (`1 ≤ j ≤ m`) those of the irreducible components of
`X'`, each of the `κ(x'_j)` is a finite algebraic extension of one of
the `κ(x_i)` (6.3.6), hence has transcendence degree `1` over `k`.
`X'` is thus indeed an algebraic curve over `k`, and moreover one
knows that `X'` is a sum of a finite number of integral and normal
schemes (6.3.6 and 6.3.7).

**(7.4.7)**

<!-- label: II.7.4.7 -->

We say that an algebraic curve `X` over `k` is _complete_ if it is
proper over `k`.

**Corollary.**

<!-- label: II.7.4.8 -->

For a reduced algebraic curve `X` over `k` to be complete, it is
necessary and sufficient that its normalisation `X'` be so.

<!-- original page 149 → 150 -->

**Proof.** Indeed, the canonical morphism `f : X' → X` is then finite
(7.4.6), hence proper (6.1.11) and surjective (6.3.8); if
`g : X → Spec(k)` is the structure morphism, `g` and `g ∘ f` are
therefore proper simultaneously, as follows from (5.4.2, (ii)) and
(5.4.3, (ii)), `g` being separated by hypothesis.

**Proposition.**

<!-- label: II.7.4.9 -->

Let `X` be a normal algebraic curve over `k`, and `Y` a proper algebraic
`k`-scheme over `k`. Then every `k`-rational map from `X` to `Y` is
everywhere defined, in other words is a morphism.

**Proof.** Indeed, it follows from (7.3.7) that at the points `x ∈ X`
where such a map is not defined, the dimension of `𝒪_x` would have to
be `≥ 2`, so the set of such points is empty; the last assertion comes
from `(I, 7.2.3)`.

**Corollary.**

<!-- label: II.7.4.10 -->

A normal algebraic curve over `k` is quasi-projective over `k`.

**Proof.** Since `X` is a sum of a finite number of integral and normal
algebraic curves (6.3.8), one may restrict to the case where `X` is
integral (5.3.6). Since `X` is quasi-compact, it is covered by a finite
number of affine opens `U_i` (`1 ≤ i ≤ n`), and since each of these is
of finite type over `k`, there exist an integer `n_i` and a
`k`-immersion `f_i : U_i → ℙ_k^{n_i}` (5.3.3 and 5.3.4, (i)). Since
`U_i` is dense in `X`, it follows from (7.4.9) that `f_i` extends to a
`k`-morphism `g_i : X → ℙ_k^{n_i}`, whence a `k`-morphism
`g = (g_1, …, g_n)_k` of `X` into the product `P` of the
`ℙ_k^{n_i}` over `k`. Moreover, for each index `i`, since the
restriction of `g_i` to `U_i` is an immersion, so too is the
restriction of `g` to `U_i` `(I, 5.3.14)`. Since the `U_i` cover `X`
and `g` is separated `(I, 5.5.1, (v))`, `g` is an immersion of `X`
into `P` `(I, 8.2.8)`. Since the Segre morphism (4.3.3) gives an
immersion of `P` into a `ℙ_k^N`, this completes the proof that `X` is
quasi-projective.

**Corollary.**

<!-- label: II.7.4.11 -->

A normal algebraic curve `X` is isomorphic to the scheme induced on an
everywhere dense open subset of a normal complete algebraic curve `X̂`,
determined up to a unique isomorphism.

**Proof.** If `X_1`, `X_2` are two normal complete curves, it follows
immediately from (7.4.9) that every isomorphism of an open `U_1`
dense in `X_1` onto an open `U_2` dense in `X_2` extends in a unique
way to an isomorphism of `X_1` onto `X_2`; whence the uniqueness
assertion. To prove the existence of `X̂`, it suffices to remark that
one may regard `X` as a subscheme of a projective bundle `ℙ_k^n`
(7.4.10). Let `X̄` be the closure of `X` in `ℙ_k^n` `(I, 9.5.11)`;
since `X` is induced by `X̄` on an open dense in `X̄` `(I, 9.5.10)`,
the generic points `x_i` of the irreducible components of `X̄` are
also those of the irreducible components of `X`, and the `κ(x_i)` are
the same for these two schemes, so (7.4.1) `X̄` is an algebraic curve
over `k`, which is reduced `(I, 9.5.9)` and projective over `k`
(5.5.1), hence complete (5.5.3). Let us then take for `X̂` the
normalisation of `X̄`, which is again complete (7.4.8); moreover, if
`h : X̂ → X̄` is the canonical morphism, the restriction of `h` to
`h⁻¹(X)` is an isomorphism onto `X` since `X` is normal (6.3.4), and
since `h⁻¹(X)` contains the generic points of the irreducible
components of `X̂` (6.3.8), it is dense in `X̂`, which concludes the
proof.

<!-- original page 150 → 151 -->

**Remark.**

<!-- label: II.7.4.12 -->

We shall show in chapter V that the conclusion of (7.4.10) still holds
without supposing the curve normal (nor even reduced); we shall also
show that for an algebraic curve (reduced or not) to be affine, it is
necessary and sufficient that its (reduced) irreducible components be
not complete.

**Corollary.**

<!-- label: II.7.4.13 -->

Let `X` be a normal irreducible curve with field `R(X) = K`, `Y` an
integral complete curve with field `L = R(Y)`. There is a canonical
bijective correspondence between dominant `k`-morphisms `X → Y` and
`k`-monomorphisms `L → K`.

**Proof.** By virtue of (7.4.9), the `k`-rational maps from `X` to `Y`
are identified with the `k`-morphisms `u : X → Y`. The dominant
morphisms `u` being characterised by the fact that `u(x) = y` (denoting
by `x` and `y` the respective generic points of `X` and `Y`), the
corollary follows from these remarks and from `(I, 7.1.13)`.

**(7.4.14)**

<!-- label: II.7.4.14 -->

One may sharpen the result of (7.4.13) when one takes for `Y` the
projective line `ℙ_k^1 = Proj(k[T₀, T])`, `T₀` and `T` being two
indeterminates. This is indeed an integral scheme (2.4.4), and the
scheme induced on the open `D₊(T₀)` of `Y` is isomorphic to `Spec(k[T])`
(2.3.6), so the generic point of `Y` is the ideal `(0)` of `k[T]` and
its field of rational functions `k(T)`, which shows that `Y` is a
complete algebraic curve over `k`. Moreover, the only graded prime
ideal of `S = k[T₀, T]` containing `T₀` and distinct from `S_+` is the
principal ideal `(T₀)`, so the complement of `D₊(T₀)` in `Y = ℙ_k^1`
reduces to a single closed point, called the _"point at infinity"_,
which we denote `∞` (for a general study of the relations between
vector bundles and projective bundles, see 8.4). With these notations:

**Corollary.**

<!-- label: II.7.4.15 -->

Let `X` be a normal irreducible curve with field `R(X) = K`. There
exists a canonical bijective map of `K` onto the set of morphisms `u`
of `X` into `ℙ_k^1` distinct from the constant morphism of value `∞`.
For `u` to be dominant, it is necessary and sufficient that the
corresponding element of `K` be transcendental over `k`.

**Proof.** This statement follows immediately from (7.4.9) and from
the

**Lemma.**

<!-- label: II.7.4.15.1 -->

Let `X` be an integral prescheme over `k`, and let `K = R(X)` be its
field of rational functions. There exists a canonical bijective map
of the set `K` onto the set of rational maps `u` of `X` into `ℙ_k^1`
distinct from the constant morphism of value `∞`. For such a rational
map to be dominant, it is necessary and sufficient that the
corresponding element of `K` be transcendental over `k`.

First of all, the rational maps of `X` into `ℙ_k^1` correspond
bijectively to the points of `ℙ_k^1` with values in the extension `K`
of `k` `(I, 7.1.12)`. If such a point is localised `(I, 3.4.5)` at the
generic point of `ℙ_k^1`, the corresponding rational map is evidently
dominant. In the contrary case, since every point of `ℙ_k^1` distinct
from the generic point is closed (7.4.3), the image of the domain of
definition `U` of `u` by the unique morphism `U → ℙ_k^1` of the class
`u` `(I, 7.2.2)` reduces to a closed point `y` of `ℙ_k^1`, and this
morphism (which is not necessarily everywhere defined in `X`) is
therefore not dominant; by abuse of language, one then says that the
rational map `u` is "constant, of value `y`". It remains to put in
bijective correspondence the points of `ℙ_k^1` with values in `K` of
locality `(I, 3.4.5)` distinct from `∞` and the elements of `K`, and
to verify that the locality of such a point is the generic point of
`ℙ_k^1` if and only if it corresponds to an

<!-- original page 151 → 152 -->

element transcendental over `k`. Now, this verification is immediate
from (4.2.6, example 1°).

**Corollary.**

<!-- label: II.7.4.16 -->

Let `X`, `Y` be two algebraic curves over `k`, normal, complete and
irreducible; let `K = R(X)`, `L = R(Y)` be their fields. There is a
canonical bijective correspondence between the set of `k`-isomorphisms
`X ⥲ Y` and the set of `k`-isomorphisms `L ⥲ K`.

**Proof.** This is an evident consequence of (7.4.13).

**(7.4.17)**

<!-- label: II.7.4.17 -->

The corollary (7.4.16) shows that an algebraic curve over `k`, normal,
complete and irreducible, is _determined by its field of rational
functions `K` up to a unique isomorphism_; by definition, `K` is an
extension of finite type of `k`, of transcendence degree `1` (what is
classically called a _field of algebraic functions of one variable_).
Moreover:

**Proposition.**

<!-- label: II.7.4.18 -->

For every extension `K` of `k`, of finite type and of transcendence
degree `1`, there exists a normal, complete and irreducible algebraic
curve `X` such that `R(X) = K` (determined up to unique isomorphism).
The set of local rings of `X` is identified `(I, 8.2.1)` with the set
consisting of `K` and the valuation rings containing `k` and having
`K` as field of fractions.

**Proof.** Indeed, `K` is an extension of finite degree of a pure
transcendental extension `k(T)` of `k`, which is identified, as we
have seen, with the field of rational functions of the projective line
`Y = ℙ_k^1`. Let `X` be the integral closure of `Y` relative to `K`
(6.3.4); `X` is a normal algebraic curve with field `K` (6.3.7), and
it is complete since the morphism `X → Y` is finite (7.4.6). The local
rings `𝒪_x` of `X` are: the field `K` when `x` is the generic point;
if `x` is distinct from the generic point, `𝒪_x` is a discrete
valuation ring containing `k` and having `K` as field of fractions
(7.4.5). Conversely, let `A` be such a ring; since the morphism
`X → Spec(k)` is proper and `A` dominates `k`, `A` dominates a local
ring `𝒪_x` of `X` (7.3.10); the latter being a valuation ring having
`K` as field of fractions, is therefore necessarily equal to `A`.

**Remarks.**

<!-- label: II.7.4.19 -->

It follows from (7.4.16) and (7.4.18) that _the data of an algebraic
curve over `k`, normal, complete and irreducible, is essentially
equivalent to the data of an extension `K` of `k`, of finite type and
of transcendence degree `1`_. We note that if `k'` is an extension of
the base field `k`, `X ⊗_k k'` will again be a complete algebraic
curve over `k'` (5.4.2, (iii)), but in general it will be neither
reduced nor irreducible. It will be so, however, if `K` is a separable
extension of `k` and `k` is algebraically closed in `K` (which is
expressed, in a classical terminology that we shall not follow, by
saying that `K` is a "regular extension" of `k`). But even in this
case, it can happen that `X ⊗_k k'` is not normal. The reader will
find details on these questions in chapter IV.

<!-- source: /Users/jcreinhold/Code/papers/books/ega/ii/02-07-criteres-valuatifs.md;
     cross-ref: /Users/jcreinhold/Code/ega/ega2/ega2-7.tex;
     PDF: ~/Code/pdfs/ega/EGA-II.pdf, pp. 138–152 -->

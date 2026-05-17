<!-- original page 36 -->

## §3. Associated prime cycles and primary decompositions

In this section we mainly give the translation of the results on modules expounded in Bourbaki, *Alg. comm.*, chap. IV,
which we follow very closely. The notions that follow seem to be of interest only in the case of *locally Noetherian*
preschemes.

### 3.1. Associated prime cycles of a Module

**Definition (3.1.1).**

<!-- label: IV.3.1.1 -->

*Let `X` be a prescheme, `ℱ` a quasi-coherent `𝒪_X`-Module. We say that a point `x ∈ X` is **associated to** `ℱ` if the
maximal ideal `𝔪_x` of `𝒪_x` is associated to the `𝒪_x`-Module `ℱ_x` (in other words, if `𝔪_x` is the annihilator of an
element of `ℱ_x`). We denote by `Ass(ℱ)` the set of `x ∈ X` associated to `ℱ`. We say that a closed irreducible subset
`Z` of `X` is an **associated prime cycle of `ℱ`** if its generic point is associated to `ℱ`. When `ℱ = 𝒪_X`, we shall
also say that the points (resp. prime cycles) associated to `ℱ` are associated to the prescheme `X`.*

*We say that an associated prime cycle of `ℱ` (resp. `X`) is **embedded** if it is contained in another associated prime
cycle of `ℱ` (resp. `X`) (in other words, if it is not maximal in the set of these cycles).*

If `X` is locally Noetherian, the irreducible components of `X` are nothing other than the maximal (or non-embedded)
prime cycles associated to `X`.

It is clear that if `x ∈ Ass(ℱ)`, then `ℱ_x ≠ 0`; in other words

```text
(3.1.1.1)                              Ass(ℱ) ⊂ Supp(ℱ).
```

If `x ∈ X` is associated to `ℱ`, it is evidently associated to `ℱ|U` for every open neighbourhood `U` of `x`, and
conversely, if it is associated to `ℱ|U` for one of these neighbourhoods, it is associated to `ℱ`.

We note finally that for a quasi-coherent `𝒪_X`-Module `ℱ`, the existence of embedded associated prime cycles is a
*local* question, since if `y` and `z` are two points of `Ass(ℱ)` with `y ∈ ‾{z}`, every neighbourhood of `y` contains
`z`.

**Proposition (3.1.2).**

<!-- label: IV.3.1.2 -->

*Let `A` be a Noetherian ring, `M` an `A`-module, `X = Spec(A)`, `ℱ = M̃`; for a point `x ∈ X` to be associated to `ℱ`,
it is necessary and sufficient that the prime ideal `𝔧_x` of `A` be associated to the module `M` (in other words, be the
annihilator of an element `f ∈ M`).*

This results from the definition `(3.1.1)` and from Bourbaki, *loc. cit.*, §1, n° 2, cor. of prop. 5, applied to
`S = A − 𝔧_x`.

**Proposition (3.1.3).**

<!-- label: IV.3.1.3 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a quasi-coherent `𝒪_X`-Module, `x` a point of `X`, `Z` the reduced
closed sub-prescheme of `X` having `‾{x}` as underlying space `(I, 5.2.1)`. The following conditions are equivalent:*

*a) `x ∈ Ass(ℱ)`.*

<!-- original page 37 -->

*b) There exists an open neighbourhood `U` of `x` and a section `f ∈ Γ(U, ℱ)` such that `U ∩ Z` is equal to
`Supp(𝒪_U · f)`.*

*b') There exists an open neighbourhood `U` of `x` and a section `f ∈ Γ(U, ℱ)` such that `U ∩ Z` is an irreducible
component of `Supp(𝒪_U · f)`.*

*c) There exists an open neighbourhood `U` of `x` and a sub-Module of `ℱ|U` isomorphic to `𝒪_Z|U` (`𝒪_Z` being
identified with a quotient of `𝒪_X`).*

*c') There exists an open neighbourhood `U` of `x` and a coherent sub-Module `𝒢` of `ℱ|U` such that `U ∩ Z` is an
irreducible component of `Supp(𝒢)`.*

It is clear that c) implies b), since it suffices to take for `f` the element of `Γ(U, ℱ)` corresponding to the unit
section of `𝒪_Z|U`. As `U ∩ Z` is irreducible `(0_I, 2.1.6)`, b) implies b'), and b') implies c') since `𝒪_X` is
coherent `(0_I, 5.3.4)`. To see that c') implies a), we may restrict to the case where `U = X = Spec(A)` is affine, `A`
therefore Noetherian, and where `ℱ = M̃`, `M` being an `A`-module, and `𝒢 = Ñ`, where `N` is a sub-module of `M`, of
finite type. We then know that the minimal elements of `Supp(𝒢)` are the maximal points of `V(Ann(N))` `(0_I, 1.7.4)`,
and these are also the minimal elements of `Ass(N)` (Bourbaki, *Alg. comm.*, chap. IV, §1, n° 3, cor. 1 of prop. 7);
since `Ass(N) ⊂ Ass(M) = Ass(ℱ)`, we see that c') implies a). Finally, a) implies c) by virtue of `(3.1.2)`, taking
again `X` affine, `ℱ = M̃`, and `Z` defined by the ideal `𝔧_x · A` (with the notation of `(3.1.2)`).

**Corollary (3.1.4).**

<!-- label: IV.3.1.4 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module. Then the maximal prime cycles associated to
`ℱ` are the irreducible components of `Supp(ℱ)`, and the generic points of these components are the points `x ∈ X` such
that `ℱ_x` is an `𝒪_x`-Module of finite length and `≠ 0`.*

Indeed, if `x` is the generic point of one of the irreducible components `Z` of `Supp(ℱ)`, it follows from the
equivalence of a) and c') in `(3.1.3)` that `x` belongs to `Ass(ℱ)`, and `Z` is an associated prime cycle of `ℱ`,
necessarily maximal by virtue of `(3.1.1.1)`; the converse follows trivially from `(3.1.1.1)`. Finally, the last
assertion, being evidently local, follows from Bourbaki, *Alg. comm.*, chap. IV, §2, n° 5, cor. 2 of prop. 7.

**Corollary (3.1.5).**

<!-- label: IV.3.1.5 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a quasi-coherent `𝒪_X`-Module. For `ℱ = 0`, it is necessary and
sufficient that `Ass(ℱ) = ∅`.*

The question being local, we are reduced to the case where `X` is affine, and the conclusion follows immediately
from `(3.1.2)` and from Bourbaki, *Alg. comm.*, chap. IV, §1, n° 1, cor. 1 of prop. 2.

**Proposition (3.1.6).**

<!-- label: IV.3.1.6 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module; then `Ass(ℱ)` is locally finite (that is to
say, every point of `X` admits a neighbourhood whose intersection with `Ass(ℱ)` is finite).*

It suffices to consider the case where `X` is affine, hence Noetherian, and then the proposition follows from `(3.1.2)`
and from Bourbaki, *Alg. comm.*, chap. IV, §1, n° 4, cor. of th. 2.

<!-- original page 38 -->

**Proposition (3.1.7).**

<!-- label: IV.3.1.7 -->

*Let `X` be a prescheme.*

*(i) Let `0 → ℱ' → ℱ → ℱ'' → 0` be an exact sequence of quasi-coherent `𝒪_X`-Modules. Then
`Ass(ℱ') ⊂ Ass(ℱ) ⊂ Ass(ℱ') ∪ Ass(ℱ'')`.*

*(ii) Let `ℱ` be a quasi-coherent `𝒪_X`-Module, `(ℱ_α)` a family of quasi-coherent sub-`𝒪_X`-Modules of `ℱ` such that
`ℱ` is the union of the `ℱ_α`. Then `Ass(ℱ) = ⋃_α Ass(ℱ_α)`.*

*(iii) For every family `(ℱ_α)` of quasi-coherent `𝒪_X`-Modules, one has `Ass(⨁_α ℱ_α) = ⋃_α Ass(ℱ_α)`.*

One is immediately reduced to the corresponding propositions for modules (Bourbaki, *loc. cit.*, §1, n° 1, formula (1),
prop. 3 and cor. 1 of prop. 3).

**Proposition (3.1.8).**

<!-- label: IV.3.1.8 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a quasi-coherent `𝒪_X`-Module, `U` an open subset of `X`, `𝔍` a coherent
Ideal of `𝒪_X` defining a closed sub-prescheme of `X` having `X − U` as underlying space. The following conditions are
equivalent:*

*a) `Ass(ℱ) ⊂ U`.*

*b) For every affine open subset `V`, every section of `ℱ` over `V` whose restriction to `V ∩ U` is zero, is equal
to `0`.*

*c) The canonical homomorphism `ℱ → ℋom_{𝒪_X}(𝔍, ℱ)` is injective.*

The question being local, we may suppose `X = Spec(A)` affine, `A` being a Noetherian ring, `ℱ = M̃`, `M` an `A`-module,
and `𝔍 = 𝔍̃`, where `𝔍` is an ideal of `A`. The homomorphism `M → Hom_A(𝔍, M)` associates to `m ∈ M` the homomorphism
`x ↦ x m` from `𝔍` to `M`; to say that it is not injective means that there exists `m ≠ 0` in `M` such that `𝔍 m = 0`.

Let us first show that c) implies a): indeed, if `Ass(ℱ)` then met `X − U`, there would be a prime ideal
`𝔭 ∈ Ass(M)` containing `𝔍`, hence an element `m ≠ 0` of `M` such that `𝔭 m = 0`. Secondly, b) implies c): indeed, if
one then had `𝔍 m = 0` for some `m ≠ 0` in `M`, then for every prime ideal `𝔮 ⊉ 𝔍`, there exists `a ∈ 𝔍` not in `𝔮`,
hence the relation `a m = 0` entails that the canonical image of `m` in `M_𝔮` is `0`; in other words `m` would be a
section `≠ 0` of `ℱ` over `X` whose restriction to `U` would be zero. Finally, a) entails b). To see this, let us note
that the canonical homomorphism `M → ∏_{𝔭 ∈ Ass(M)} M_𝔭` is injective: indeed, if `N` is the kernel of this
homomorphism, one has `Ass(N) ⊂ Ass(M)`; if there existed `𝔭 ∈ Ass(N)`, there would be an element `n ∈ N` whose
annihilator would be `𝔭`; but by definition of `N`, there is an element `s ∉ 𝔭` such that `s n = 0`, which is absurd;
one concludes that `Ass(N) = ∅`, whence `N = 0`. Now condition a) entails that if `m ∈ M` is a section of `ℱ` whose
restriction to `U` is zero, the canonical image of `m` in `M_𝔭` is zero for every `𝔭 ∈ Ass(M)`, hence `m = 0`. Q.E.D.

**Corollary (3.1.9).**

<!-- label: IV.3.1.9 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a quasi-coherent `𝒪_X`-Module, `f` a section of `𝒪_X` over `X`. For `f`
to be `ℱ`-regular `(0, 15.2.2)`, it is necessary and sufficient that `Ass(ℱ) ⊂ X_f`.*

Indeed, it is immediate that to say that `f` is `ℱ`-regular means that the canonical homomorphism
`ℱ → ℋom_{𝒪_X}(f 𝒪_X, ℱ)` is injective, and it suffices to apply `(3.1.8)` to the Ideal `𝔍 = f 𝒪_X`.

<!-- original page 39 -->

**Proposition (3.1.10).**

<!-- label: IV.3.1.10 -->

*Let `X`, `Y` be locally Noetherian preschemes, `f : X → Y` an integral morphism. Then, for every quasi-coherent
`𝒪_X`-Module `ℱ`, one has `f(Ass(ℱ)) = Ass(f_*(ℱ))`.*

The question being local on `Y` and the morphism `f` being affine, one is immediately reduced to the case where `Y` is
affine; in other words, to the

**Lemma (3.1.10.1).**

<!-- label: IV.3.1.10.1 -->

*Let `A`, `B` be two Noetherian rings, `ρ : A → B` a ring homomorphism making `B` into an integral `A`-algebra, `M` a
`B`-module. Then the prime ideals `𝔭 ∈ Ass(M_{[ρ]})` are the inverse images by `ρ` of the prime ideals `𝔮 ∈ Ass(M)`.*

Indeed, if `𝔮 ∈ Ass(M)`, `𝔮` is the annihilator in `B` of an element `x ∈ M`, hence `ρ⁻¹(𝔮)` is the annihilator in `A`
of `x`. Conversely, let `𝔭 ∈ Ass(M_{[ρ]})`, so that `𝔭` is the inverse image by `ρ` of the annihilator `𝔟` in `B` of an
element `x ∈ M`; it follows from the first theorem of Cohen-Seidenberg that there exists a prime ideal `𝔮` of `B`
containing `𝔟` and whose inverse image is `𝔭` (Bourbaki, *Alg. comm.*, chap. V, §2, n° 1, cor. 2 of th. 1); on
considering one of the prime ideals minimal among those contained in `𝔮` and containing `𝔟`, we may evidently suppose
that `𝔮` itself is one of these minimal ideals. But as `B · x ⊂ M` is isomorphic to `B/𝔟`, we know that one then has
`𝔮 ∈ Ass(B/𝔟) ⊂ Ass(M)` (Bourbaki, *Alg. comm.*, chap. IV, §1, n° 4, th. 2).

**Corollary (3.1.11).**

<!-- label: IV.3.1.11 -->

*Under the hypotheses of `(3.1.10)`, for `ℱ` to be without embedded associated prime cycle, it suffices that the same be
true of `f_*(ℱ)`.*

Suppose indeed that `f_*(ℱ)` has no embedded associated prime cycle. Note that if `A` is an integral algebra over a
field `k`, all the prime ideals of `A` are maximal (Bourbaki, *Alg. comm.*, chap. V, §2, n° 1, prop. 1); it follows from
`(I, 6.2.2)` that the fibres of `f` are *discrete* spaces. If `x`, `x'` are two distinct points of `Ass(ℱ)`, neither of
them can be adherent to the other if `f(x) = f(x')`; and if `f(x) ≠ f(x')`, `(3.1.10)` and the hypothesis entail that
neither of the two points `f(x)`, `f(x')` can be adherent to the other, hence the same is true of `x` and `x'`.

**Remark (3.1.12).**

<!-- label: IV.3.1.12 -->

*Under the hypotheses of `(3.1.10)`, it can on the other hand happen that `ℱ` is without embedded associated prime
cycle, but not `f_*(ℱ)`. Take for example `Y = Spec(k[T])` where `k` is a field ("affine line"), and `X` the sum of
`X_1 = Y` and `X_2 = Spec(k)`, the morphism `X_2 → Y` corresponding to the canonical homomorphism `k[T] → k[T]/𝔪`, where
`𝔪` is the maximal ideal `(T)`. It is clear that the morphism `f : X → Y` is finite; if one takes `ℱ = 𝒪_X`, then `ℱ`
is without embedded associated prime cycle, but `f_*(ℱ) = M̃`, where `M` is the `k[T]`-module direct sum of `k[T]` and
`k`, hence `Ass(M)` is formed of the generic point `(0)` of `Y` and the point `𝔪`.*

**Proposition (3.1.13).**

<!-- label: IV.3.1.13 -->

*Let `X` be a locally Noetherian prescheme, `U` an open subset of `X`, `i : U → X` the canonical injection. For every
quasi-coherent `𝒪_U`-Module `ℱ`, one has `Ass(i_*(ℱ)) = Ass(ℱ)`.*

Recall that `i_*(ℱ)` is a quasi-coherent `𝒪_X`-Module `(1.2.2 and 1.7.4)`; as `i_*(ℱ)|U = ℱ`, one has
`(Ass(i_*(ℱ))) ∩ U = Ass(ℱ)`, and it therefore remains to prove that `Ass(i_*(ℱ)) ⊂ U`. But by `(3.1.8)`, this relation
means that for every affine open `V` of `X`, every section of `i_*(ℱ)` over `V` which is zero in `U ∩ V`, is zero, a
condition trivially verified since `Γ(V, i_*(ℱ)) = Γ(U ∩ V, ℱ) = Γ(U ∩ V, i_*(ℱ))`.

<!-- original page 40 -->

### 3.2. Irredundant decompositions

**Proposition (3.2.1).**

<!-- label: IV.3.2.1 -->

*Let `X` be a locally Noetherian prescheme, `U` a dense open subset of `X`. The following conditions are equivalent:*

*a) `X` is reduced.*

*b) The induced sub-prescheme on `U` is reduced and `X` is without embedded prime cycle.*

*c) `X` is without embedded prime cycle and for every generic point `x` of an irreducible component of `X`, one has
`long(𝒪_x) = 1`.*

*The prime cycles associated to `X` are then identical to the irreducible components of `X`.*

It is clear that if `X` is reduced, the same is true of the sub-prescheme induced on `U`. Moreover, the existence of
embedded prime cycles being local, we may restrict to the case where `X = Spec(A)` is affine, `A` Noetherian. If `A`
is reduced, we know that the minimal prime ideals of `A` form a reduced primary decomposition of `(0)` (Bourbaki, *Alg.
comm.*, chap. IV, §2, n° 5, prop. 10) and are the elements of `Ass(A)`, hence there exist no embedded prime ideals
associated to `A`, which shows that a) implies b). It is immediate that b) entails c), since a generic point `x` of an
irreducible component of `X` belongs to `U`, hence `𝒪_x` is a field. Finally, c) entails a): it suffices indeed to note
that if `𝒩` is the Nilradical of `𝒪_X`, which is a coherent Ideal, `Supp(𝒩)` cannot contain any of the generic points
of the irreducible components of `X` by hypothesis; if `Supp(𝒩)` were not empty and if `x` were one of the maximal
points of this closed set, the criterion `(3.1.3, c'))` would show that `x ∈ Ass(𝒪_X)`, and `‾{x}` would therefore be an
*embedded* prime cycle of `X`, contrary to the hypothesis; hence `𝒩 = 0`.

**Definition (3.2.2).**

<!-- label: IV.3.2.2 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module. We say that `ℱ` is **reduced** if it satisfies
the two following conditions: 1° `ℱ` is without embedded associated prime cycle; 2° for every maximal point `x` of
`Supp(ℱ)`, one has `long(ℱ_x) = 1`.*

Condition 1° means that the associated prime cycles of `ℱ` are the irreducible components of `Supp(ℱ)` `(3.1.4)`, and
condition 2° means that for every generic point `x` of such a component one has `long(ℱ_x) = 1`.

For an affine scheme `X`, this definition gives in particular the notion of *reduced module* on a Noetherian ring `A`;
an `A`-module of finite type `M` is said to be *reduced* if it has no embedded associated prime ideals and if, for every
`𝔭 ∈ Ass(M)`, `long_{A_𝔭}(M_𝔭) = 1`. Returning to the case of a locally Noetherian prescheme `X` and of a coherent
`𝒪_X`-Module `ℱ`, we say that `ℱ` is *reduced at a point* `x ∈ X` if `ℱ_x` is a reduced `𝒪_x`-module; that signifies
again that, on the local scheme `Spec(𝒪_x)`, `ℱ̃_x` is reduced; it therefore amounts to the same to say *that `x`
belongs to no embedded associated prime cycle of `ℱ` and that `long(ℱ_z) = 1` for every maximal point `z` of `Supp(ℱ)`
such that `x ∈ ‾{z}`*. It is clear that if `ℱ` is a reduced coherent `𝒪_X`-Module, it is reduced at every point of `X`;
conversely, if `ℱ` is reduced at a point `x`, there exists an open neighbourhood `U` of `x` such that `ℱ|U` is a reduced
`𝒪_U`-Module: it suffices indeed to take `U` meeting no embedded associated prime cycle of `ℱ` (such a neighbourhood
exists since these cycles form a locally finite set of closed parts

<!-- original page 41 -->

of `X`). To say that `𝒪_X` is reduced at a point `x` amounts to saying that `X` is reduced at the point `x`.

**Proposition (3.2.3).**

<!-- label: IV.3.2.3 -->

*Let `X` be a locally Noetherian prescheme, `U` an open subset of `X`, `ℱ` a coherent `𝒪_X`-Module such that
`U ∩ Supp(ℱ)` is dense in `Supp(ℱ)`. The following conditions are equivalent:*

*a) `ℱ` is reduced.*

*b) `ℱ|U` is reduced and `ℱ` is without embedded associated prime cycle.*

*c) There exist a reduced closed sub-prescheme `X'` of `X` and a coherent `𝒪_{X'}`-Module `ℱ'` torsion-free and of
rank 1 on every irreducible component of `X'` such that, if `j : X' → X` is the canonical injection, one has
`j_*(ℱ') = ℱ`.*

*Moreover, when this is so, the sub-prescheme `X'` is defined by the Ideal `𝔍` of `𝒪_X` annihilator of `ℱ`.*

To see that c) implies a), one may, by virtue of `(3.1.3)`, restrict to the case where `X' = X` is integral, with generic
point `x`, and one may moreover suppose `X = Spec(A)` affine and `ℱ = M̃`, where `A` is therefore integral and `M` is a
torsion-free `A`-module of rank 1; the annihilator of every element of `M` then being reduced to `0`, one has
`Ass(ℱ) = {x}` and `ℱ_x` is isomorphic to `𝒪_x`, the field of fractions of `A`, so the conditions of definition `(3.2.2)`
are satisfied. As the existence of embedded associated prime cycles is local, it is clear that if `ℱ` has no such cycles
and if `U ∩ Supp(ℱ)` is dense in `Supp(ℱ)`, then `Ass(ℱ) = Ass(ℱ|U)`, hence a) and b) are equivalent. If a) is
satisfied, take for `X'` the reduced closed sub-prescheme of `X` whose underlying space is `Supp(ℱ)` `(I, 5.2.1)`, and
let `ℱ' = j*(ℱ)`; a point `x` of `Ass(ℱ)` is necessarily a maximal point of `X'`, and as `long(ℱ_x) = 1`, `ℱ'_x` is
isomorphic to `ℱ_x`, hence to the field `k(x) = 𝒪_{X', x}`, which proves that `ℱ'` is torsion-free and of rank `1`
`(I, 7.4.6 and 7.4.2)`. Finally, the last assertion is trivial, since for every `y ∈ X'`, the annihilator of the
`𝒪_{X', y}`-Module `ℱ'_y` is zero.

**Definition (3.2.4).**

<!-- label: IV.3.2.4 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a quasi-coherent `𝒪_X`-Module. We say that `ℱ` is **irredundant** if
`Ass(ℱ)` is reduced to a single element `x`; if `ℱ` is of finite type, we say that `ℱ` is **integral** if moreover `ℱ`
is reduced (in other words if `long(ℱ_x) = 1`). We say that a quasi-coherent sub-`𝒪_X`-Module `𝒢` of a quasi-coherent
`𝒪_X`-Module `ℱ` is **primary in `ℱ`** if `ℱ/𝒢` is irredundant.*

For an affine scheme `X`, this definition gives in particular the notion of *integral module* on a Noetherian ring `A`;
an `A`-module `M` is said to be *integral* if it is of finite type, if `M` is primary (that is, `Ass(M)` is reduced to a
single prime ideal `𝔭`) and if moreover `long_{A_𝔭}(M_𝔭) = 1`. Returning to the case of an arbitrary locally Noetherian
prescheme `X` and of a coherent `𝒪_X`-Module `ℱ`, we say that `ℱ` is *integral at a point* `x ∈ X` if `ℱ_x` is an
integral `𝒪_x`-module: that means again that `x` belongs to only a single associated prime cycle (necessarily
non-embedded) of `ℱ` and that `long(ℱ_z) = 1` at its generic point `z`. It is clear that if `ℱ` is an integral coherent
`𝒪_X`-Module, it is integral at every point of `X`; conversely, if `ℱ` is integral at a point `x`, there exists an open
neighbourhood `U` of `x` such that `ℱ|U` is

<!-- original page 42 -->

an integral `𝒪_U`-Module: it suffices indeed to take `U` such that `ℱ|U` is a reduced `𝒪_U`-Module `(3.2.2)`.

We say that the locally Noetherian prescheme `X` is *irredundant* if `𝒪_X` is irredundant (which implies that `X` is
*irreducible*); for `X` to be *integral*, it is necessary and sufficient that the `𝒪_X`-Module `𝒪_X` be integral
(`(I, 2.1.8)` and `(3.2.1)`). If `𝒪_X` is integral at a point `x`, that is, if the ring `𝒪_x` is integral, we say that
`X` is *integral at the point* `x`. We say that a closed sub-prescheme `Y` of `X` is *primary in `X`* if the Ideal `𝔍`
of `𝒪_X` that defines `Y` is primary in `𝒪_X`.

**Definition (3.2.5).**

<!-- label: IV.3.2.5 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module. We call an **irredundant decomposition** of `ℱ`
a family `(ℱ_α)_{α ∈ I}` of `𝒪_X`-Module quotients of `ℱ` such that the `ℱ_α` are irredundant, the family
`(Supp(ℱ_α))` is locally finite, and the canonical homomorphism `ℱ → ⨁_α ℱ_α` is injective. We say that such a
decomposition is **reduced** if the sets `Ass(ℱ_α)` are pairwise distinct, and if there exists no subset `J ≠ I` such
that the sub-family `(ℱ_α)_{α ∈ J}` is an irredundant decomposition of `ℱ`.*

If `(ℱ_α)_{α ∈ I}` is an irredundant decomposition (resp. reduced irredundant decomposition) of `ℱ` and if one sets
`ℱ_α = ℱ/𝒢_α`, we also say that the family `(𝒢_α)_{α ∈ I}` of sub-`𝒪_X`-Modules of `ℱ` is a *primary decomposition*
of `0` in `ℱ`; we note that the hypothesis of injectivity of the canonical homomorphism `ℱ → ⨁_α ℱ_α` is equivalent
to the condition `⋂_{α ∈ I} 𝒢_α = 0`.

If `(ℱ_α)` is an irredundant decomposition of `ℱ`, to say that it is reduced is equivalent to saying that the
`Ass(ℱ_α)` are pairwise distinct and contained in `Ass(ℱ)`; if `Ass(ℱ_α) = {x_α}` for every `α ∈ I`, `α ↦ x_α` is a
bijection of `I` onto `Ass(ℱ)`: these properties are indeed local and therefore result from Bourbaki, *Alg. comm.*,
chap. IV, §2, n° 3, prop. 4.

**Proposition (3.2.6).**

<!-- label: IV.3.2.6 -->

*Let `X` be a locally Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module. Then there exists a reduced irredundant
decomposition `(ℱ^{(x)})_{x ∈ Ass(ℱ)}` formed of coherent `𝒪_X`-Modules such that for every `x ∈ Ass(ℱ)`, one has
`Ass(ℱ^{(x)}) = {x}`. For every `x ∈ Ass(ℱ)` such that `‾{x}` is not embedded, `ℱ^{(x)}` is uniquely determined as the
image of the canonical homomorphism `ℱ → i_*(i^*(ℱ))`, where `i` is the canonical morphism `Spec(k(x)) → X`.*

For every `x ∈ Ass(ℱ)`, let `U` be an affine open neighbourhood of `x`, with ring `A`, and let `ℱ|U = M̃`, where `M` is
an `A`-module of finite type. We know (Bourbaki, *Alg. comm.*, chap. IV, §1, n° 1, prop. 4) that there exists a
sub-module `N` of `M` such that, if one sets `P = M/N`, one has `Ass(P) = {x}` and `Ass(N) = Ass(M) − {x}`. Let
`𝒢 = P̃`, which is a quasi-coherent `𝒪_U`-Module, and let `j` be the canonical injection `U → X`; let
`u : j*(ℱ) → 𝒢` be the surjective homomorphism corresponding to the homomorphism `M → P`; from this one deduces a
homomorphism `j_*(u) : j_*(j*(ℱ)) → j_*(𝒢)`, whence by composition a homomorphism

```text
                            ρ_ℱ                j_*(u)
                  v : ℱ ──────→ j_*(j*(ℱ)) ────────→ j_*(𝒢)
```

of which `u` is the restriction to `U`; we shall designate by `ℱ^{(x)}` the image of `ℱ` by this homomorphism, which is
a coherent `𝒪_X`-Module `(I, 6.1.1)`. One has `Ass(j_*(𝒢)) = {x}` by virtue of `(3.1.13)`, and a fortiori
`(3.1.7)` `Ass(ℱ^{(x)}) = {x}`, since `ℱ^{(x)} ≠ 0`. Moreover, if

<!-- original page 43 -->

`𝒩^{(x)} = Ker(v)`, one has `𝒩^{(x)}|U = Ñ`, hence `x ∉ Ass(𝒩^{(x)})`. It follows that the homomorphism
`ℱ → ⨁_{x ∈ Ass(ℱ)} ℱ^{(x)}` is injective, for its kernel `ℋ` is contained in every `𝒩^{(x)}`, hence `Ass(ℋ)` is
contained in the intersection of the `Ass(𝒩^{(x)})`, which is empty; consequently `(3.1.5)`, `ℋ = 0`. Taking into
account that `Ass(ℱ)` is locally finite `(3.1.6)`, it is clear that `(ℱ^{(x)})_{x ∈ Ass(ℱ)}` is a reduced irredundant
decomposition of `ℱ` verifying the conditions of the statement. The characterization of `ℱ^{(x)}` when `‾{x}` is not
embedded follows from Bourbaki, *Alg. comm.*, chap. IV, §2, n° 3, prop. 5, the question being local, and taking
account of `(I, 1.6.7)`.

**Corollary (3.2.7).**

<!-- label: IV.3.2.7 -->

*Under the hypotheses of `(3.2.6)`, if `ℱ` has no embedded associated prime cycle, there exists only one reduced
irredundant decomposition of `ℱ`.*

**Corollary (3.2.8).**

<!-- label: IV.3.2.8 -->

*Let `X` be a Noetherian prescheme, `ℱ` a coherent `𝒪_X`-Module. There exists a finite filtration `(ℱ_i)_{0 ≤ i ≤ n}`
of `ℱ` such that `ℱ_0 = ℱ`, `ℱ_n = 0`, formed of coherent `𝒪_X`-Modules and such that the quotients `ℱ_i/ℱ_{i+1}` are
zero or irredundant, and `Ass(ℱ_i/ℱ_{i+1}) ⊂ Ass(ℱ)`.*

Indeed, `ℱ` is isomorphic to a sub-`𝒪_X`-Module of a finite direct sum `⨁_{j=1}^n 𝒢_j`, where the `𝒢_j` are irredundant
and coherent `(3.2.6)`; as every quasi-coherent sub-`𝒪_X`-Module of `𝒢_j` is zero or irredundant `(3.1.7)`, the
`ℱ_i = ℱ ∩ (⨁_{j=1}^{n-i} 𝒢_j)` answer the question, `ℱ_i/ℱ_{i+1}` being isomorphic to a coherent sub-`𝒪_X`-Module
of `𝒢_{n-i}`.

### 3.3. Relations with flatness

**Proposition (3.3.1).**

<!-- label: IV.3.3.1 -->

*Let `f : X → Y` be a morphism, `ℱ` a quasi-coherent `𝒪_X`-Module and `f`-flat, `𝒢` a quasi-coherent `𝒪_Y`-Module. If,
for every `y ∈ Y`, one sets `ℱ_y = ℱ ⊗_{𝒪_Y} k(y)`, one has*

```text
(3.3.1.1)                       Ass(ℱ ⊗_{𝒪_Y} 𝒢) ⊃ ⋃_{y ∈ Ass(𝒢)} Ass(ℱ_y)
```

*and the two sides are equal if `Y` is locally Noetherian.*

(Of course, `ℱ_y` is a sheaf on the fibre `f⁻¹(y)`, and one identifies this fibre with a subspace of `X` `(I, 3.6.1)`.)
The question being local on `X` and on `Y`, one is reduced to the case where `X` and `Y` are affine, and the proposition
is then proved in Bourbaki, *Alg. comm.*, chap. IV, §2, n° 6, th. 2.

**Corollary (3.3.2).**

<!-- label: IV.3.3.2 -->

*Let `Y` be a locally Noetherian prescheme without embedded associated prime cycles, `f : X → Y` a morphism, `ℱ` a
quasi-coherent `𝒪_X`-Module and `f`-flat. Then, for every `x ∈ Ass(ℱ)`, `f(x)` is a maximal point of `Y`.*

It suffices to apply `(3.3.1)` with `𝒢 = 𝒪_Y`, since `Ass(𝒪_Y)` is by hypothesis the set of maximal points of `Y`.

**Corollary (3.3.3).**

<!-- label: IV.3.3.3 -->

*Under the hypotheses of `(3.3.1)`, suppose in addition that `X` and `Y` are locally Noetherian, `ℰ` and `ℱ` coherent.
Then the following conditions are equivalent:*

*a) `ℰ ⊗_Y ℱ` is without embedded associated prime cycle.*

*b) For every point `y ∈ Ass(ℰ) ∩ f(Supp(ℱ))`, `‾{y}` is a non-embedded associated prime cycle of `ℰ` and `ℰ_y ⊗ ℱ_y`
is without embedded associated prime cycle.*

<!-- original page 44 -->

Suppose a) verified. The hypotheses imply that `ℰ ⊗_Y ℱ` is a coherent `𝒪_X`-Module `(0_I, 5.3.11 and 5.3.5)`; its
associated prime cycles are therefore the irreducible components of `Supp(ℰ ⊗_Y ℱ)` `(3.1.4)`, and for every maximal
point `x` of `Supp(ℰ ⊗_Y ℱ)`, `f(x) = y` is a maximal point of `Supp(ℰ)` and `x` a maximal point of `Supp(ℱ_y)` `(2.5.5)`.
Since, by virtue of `(3.3.1)` and the fact that the relation `y ∈ f(Supp(ℱ))` entails `ℱ_y ≠ 0` `(I, 9.1.13)`, every
point of `Ass(ℰ) ∩ f(Supp(ℱ))` is the image by `f` of a maximal point of `Supp(ℰ ⊗_Y ℱ)`, we see that condition b) is
verified.

Conversely, suppose b) verified, and let us show that if `z`, `z'` are two distinct points of `Ass(ℰ ⊗_Y ℱ)`, neither
of them can be adherent to the other. First, if `f(z) = f(z') = y`, one has `y ∈ Ass(ℰ)` and `z` and `z'` belong to
`Ass(ℱ_y)` by `(3.3.1)`, whence `y ∈ f(Supp(ℱ))`; as by hypothesis neither of the two points `z`, `z'` is adherent to the
other in `f⁻¹(y)`, neither of them can be adherent to the other in `X`. If `y = f(z)` and `y' = f(z')` are distinct, they
belong to `Ass(ℰ) ∩ f(Supp(ℱ))`, hence neither of them can be adherent to the other in `Y`; it follows from the
continuity of `f` that neither of the points `z`, `z'` can be adherent to the other in `X`.

**Proposition (3.3.4).**

<!-- label: IV.3.3.4 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a morphism, `ℰ` a coherent `𝒪_Y`-Module, `ℱ` a coherent
`𝒪_X`-Module and `f`-flat. Then the following conditions are equivalent:*

*a) `ℰ ⊗_Y ℱ` is reduced `(3.2.2)`.*

*b) For every point `y ∈ Ass(ℰ) ∩ f(Supp(ℱ))`, `‾{y}` is a non-embedded associated prime cycle of `ℰ`,
`long(ℰ_y) = 1` and `ℱ_y` is reduced.*

Suppose a) verified. We already know `(3.3.3)` that for every `y ∈ Ass(ℰ) ∩ f(Supp(ℱ))`, `‾{y}` is a non-embedded
associated prime cycle of `ℰ` and `ℱ_y` is without embedded associated prime cycle. Moreover `(2.5.5)`, for every
`x ∈ Ass(ℰ ⊗_Y ℱ) ∩ f⁻¹(y)`, one has `1 = long((ℰ ⊗_Y ℱ)_x) = long(ℰ_y) · long((ℱ_y)_x)`, hence
`long(ℰ_y) = long((ℱ_y)_x) = 1`, which proves b).

Conversely, suppose b) verified; we already know that every point `x ∈ Ass(ℰ ⊗_Y ℱ)` is a maximal point of
`Supp(ℰ ⊗_Y ℱ)`, that `y = f(x)` is a maximal point of `Supp(ℰ)` and `x` a maximal point of `Supp(ℱ_y)` `(3.3.1 and
3.3.3)`; moreover it follows from the hypothesis and from `(2.5.5)` that `long((ℰ ⊗_Y ℱ)_x) = 1`, which proves a).

**Corollary (3.3.5).**

<!-- label: IV.3.3.5 -->

*Let `X`, `Y` be two locally Noetherian preschemes, `f : X → Y` a flat morphism; if `Y` is reduced at the points of
`f(X)` and if `f⁻¹(y)` is a reduced `k(y)`-prescheme for every `y ∈ f(X)`, then `X` is reduced.*

Since the Nilradical `𝒩_Y` is coherent, the set of points where `Y` is reduced is open `(0_I, 5.2.2)`, and one may
restrict to the case where `Y` is reduced. It then suffices to apply `(3.3.4)` to `ℰ = 𝒪_Y` and `ℱ = 𝒪_X`.

**Proposition (3.3.6).**

<!-- label: IV.3.3.6 -->

*Let `f : X → S`, `g : Y → S` be two morphisms, `ℱ` a quasi-coherent `𝒪_X`-Module, `𝒢` a quasi-coherent `𝒪_Y`-Module.
Suppose that: 1° `𝒢` is `g`-flat; 2° `X` is locally Noetherian, and for every `s ∈ S`, `g⁻¹(s)` is locally Noetherian
(which will be the case if `Y` is also locally Noetherian). Let `Z = X ×_S Y`; for every couple `(x, y)` such that
`x ∈ X`, `y ∈ Y` and*

<!-- original page 45 -->

*`f(x) = g(y) = s`, let `T_{x,y}` be the prescheme `Spec(k(x) ⊗_{k(s)} k(y))`, and let `I_{x,y}` be the image of
`Ass(𝒪_{T_{x,y}})` by the canonical monomorphism `T_{x,y} → Z` `(I, 3.4.9)`. One then has*

```text
(3.3.6.1)              Ass(ℱ ⊗_S 𝒢) = ⋃_{x ∈ Ass(ℱ)} ( ⋃_{y ∈ Ass(𝒢_{f(x)})} I_{x,y} )
```

*where for every `s ∈ S`, `𝒢_s = 𝒢 ⊗_{𝒪_S} k(s)`.*

Let `p : Z → X`, `q : Z → Y` be the canonical projections, so that one has the commutative diagram

```text
                                X ←─── Z
                                       p
                                ↓ f    ↓ q
                                S ←─── Y
                                   g
```

Set `𝒢' = q*(𝒢)`, so that `ℱ ⊗_S 𝒢 = ℱ ⊗_X 𝒢'`; as `𝒢'` is `p`-flat `(2.1.4)`, it follows from `(3.3.1)` that one has

```text
(3.3.6.2)                       Ass(ℱ ⊗_X 𝒢') = ⋃_{x ∈ Ass(ℱ)} Ass(𝒢'_x)
```

with `𝒢'_x = 𝒢' ⊗_{𝒪_X} k(x)`. If `s = f(x)`, one has `𝒢_s = 𝒢 ⊗_{𝒪_S} k(s)`, and `p⁻¹(x) = g⁻¹(s) ⊗_{k(s)} k(x)`;
moreover, since the field `k(x)` is a flat `k(s)`-module, the morphism `p⁻¹(x) → g⁻¹(s)` is flat `(2.1.4)`; applying
`(3.3.1)` to this morphism, it comes

```text
(3.3.6.3)                       Ass(𝒢'_x) = ⋃_{y ∈ Ass(𝒢_s)} Ass(𝒪_{T_{x,y}})
```

whence the proposition.

We note that if, in the statement, one suppresses hypothesis 2°, one may still conclude, by virtue of `(3.3.1)`, the
relation

```text
(3.3.6.4)             Ass(ℱ ⊗_S 𝒢) ⊃ ⋃_{x ∈ Ass(ℱ)} ( ⋃_{y ∈ Ass(𝒢_{f(x)})} I_{x,y} ).
```

**Corollary (3.3.7).**

<!-- label: IV.3.3.7 -->

*Under the hypotheses of `(3.3.6)`, suppose in addition that `S` is locally Noetherian and that `f(Ass(ℱ)) ⊂ Ass(𝒪_S)`.
Then one has*

```text
(3.3.7.1)                             Ass(ℱ ⊗_S 𝒢) = ⋃_{(x,y) ∈ C} I_{x,y}
```

*where `C` is the set of couples `(x, y)` such that `x ∈ Ass(ℱ)`, `y ∈ Ass(𝒢)` and `f(x) = g(y)`.*

Since `𝒢` is `g`-flat, it follows indeed from `(3.3.1)` that the relation "`s ∈ Ass(𝒪_S)` and `y ∈ Ass(𝒢_s)`" is
equivalent to `y ∈ Ass(𝒢)`: the conclusion follows from `(3.3.6.1)`.

**Remarks (3.3.8).**

<!-- label: IV.3.3.8 -->

*We shall see later `(4.2.2)` that under the hypotheses of `(3.3.6)`, `T_{x,y}` is a prescheme without embedded
associated prime cycle; it will follow that if `ℱ` and the `𝒢_s` are without embedded associated prime cycle, the same
is true of `ℱ ⊗_S 𝒢`.*

**Corollary (3.3.9).**

<!-- label: IV.3.3.9 -->

*Under the conditions of `(3.3.7)`, one has*

```text
(3.3.9.1)                             q(Ass(ℱ ⊗_S 𝒢)) ⊂ Ass(𝒢)
```

*(where `q : X ×_S Y → Y` is the canonical projection).*

Indeed, if `(x, y) ∈ Z`, one has `q(I_{x,y}) = {y} ⊂ Ass(𝒢)`.

<!-- original page 46 -->

### 3.4. Properties of the sheaves `ℱ/tℱ`

**Proposition (3.4.1).**

<!-- label: IV.3.4.1 -->

*Let `X` be a locally Noetherian prescheme, `t` a section of `𝒪_X` over `X`, `Y` the closed sub-prescheme of `X` defined
by the Ideal `t 𝒪_X` of `𝒪_X`. Let `ℱ` be a coherent `𝒪_X`-Module, `S` the reduced closed sub-prescheme of `X` having
`Supp(ℱ)` as underlying space, `(S_i)` the family of reduced closed sub-preschemes of `X` having as underlying spaces
the irreducible components of `S`; we designate by `s_i` the generic point of `S_i`. Finally, let `Z` be an irreducible
component of `Supp(ℱ/tℱ) = S ∩ Y`, `z` its generic point.*

*(i) For every `i` such that `Z ⊂ S_i`, `Z` is an irreducible component of `S_i ∩ Y`.*

*(ii) If `Z` is not equal to any of the `S_i`, one has*

```text
(3.4.1.1)                            long((ℱ/tℱ)_z) ≥ ∑_i long(ℱ_{s_i})
```

*where the sum on the right-hand side is extended to all `i` such that `Z ⊂ S_i`.*

*(iii) Suppose that `Z` is equal to none of the `S_i`. For the two sides of `(3.4.1.1)` to be equal, it is necessary and
sufficient that the two following conditions be satisfied:*

*α) `t_z` is `ℱ_z`-regular `(0, 15.1.4)`.*

*β) For every `i` such that `Z ⊂ S_i`, the canonical image of the germ `t_z` in `𝒪_{S_i, z}` generates the maximal ideal
of this ring (which entails that `𝒪_{S_i, z}` is a discrete valuation ring and the image of `t_z` a uniformizer of this
ring).*

(i) If `j : Y → X` is the canonical injection, one has `ℱ/tℱ = ℱ ⊗_{𝒪_X} 𝒪_Y = j*(ℱ)`, hence
`Supp(ℱ/tℱ) = j⁻¹(S) = S ∩ Y` `(I, 9.1.13)`, whence the assertion.

(ii) and (iii). As the `s_i` such that `Z ⊂ S_i` are those belonging to `Spec(𝒪_z)`, we may, in order to prove (ii) and
(iii), replace `X` by `Spec(𝒪_z)`; and if `M = ℱ_z`, we may therefore suppose that `ℱ = M̃`, whence `ℱ_{s_i} = M_{𝔭_i}`,
where we designate by `𝔭_i` the minimal ideals of `𝒪_z`. Moreover, as `M` is an `𝒪_z`-module of finite type, one has
`S = S'_red`, with `S' = Spec(𝒪_z/𝔞)`, where `𝔞` is the annihilator of `M` in `𝒪_z` `(0_I, 1.7.4)`, and the two sides
of `(3.4.1.1)` keep the same values, whether one considers `M` as an `𝒪_z`-module or as an `(𝒪_z/𝔞)`-module; one
therefore sees that one can finally replace `X` by `S' = Spec(A)`, where `A` is a Noetherian local ring, `M` being a
*faithful* `A`-module; since `Z` is closed in `S`, the hypothesis that `Z ≠ S_i` for every `i` means that `s_i ∉ Z`,
hence that `dim(A) > 0`; finally, to say that `z` is the generic point of `Z`, an irreducible component of `S ∩ V(t)`,
means that `A/tA` is of dimension `0` (in other words, is a local Artinian ring). One is therefore reduced to proving
the following statement:

**Lemma (3.4.1.2).**

<!-- label: IV.3.4.1.2 -->

*Let `A` be a Noetherian local ring of dimension `> 0`, `𝔭_i` the minimal prime ideals of `A`, `𝔪` its maximal ideal, `t`
an element of `𝔪` such that `A/tA` is Artinian. Then, for every `A`-module of finite type `M`, one has*

```text
(3.4.1.3)                            long(M/tM) ≥ ∑_i long(M_{𝔭_i});
```

*moreover, for the two sides of `(3.4.1.3)` to be equal, it is necessary and sufficient that the following conditions be
satisfied:*

<!-- original page 47 -->

*α) `t` is `M`-regular;*

*β) for every `i` such that `M_{𝔭_i} ≠ 0`, the image of `t` in `A/𝔭_i` generates the maximal ideal of this ring (which
entails that `A/𝔭_i` is a discrete valuation ring).*

As `A` is not of dimension `0` and `A/tA` is Artinian, one has necessarily `dim(A) = 1` `(0, 16.3.4)` and `t ∉ 𝔭_i` for
every `i`: the principal ideal `(t)` is therefore an ideal of definition of `A`, and hence contains a power of its
maximal ideal `𝔪`. Let `N` be the submodule of elements of `M` annihilated by a power of `t` (or by a power of `𝔪`,
which amounts to the same thing as we have just seen); if one sets `P = M/N`, `t` is `P`-regular, since the relation
`tx ∈ N` for an `x ∈ M` entails `t^k(tx) = 0` for some integer `k`, hence `x ∈ N`. This being so, one has the

**Lemma (3.4.1.4).**

<!-- label: IV.3.4.1.4 -->

*Let `A` be a ring,*

```text
                                 0 → M' → M → M'' → 0
```

*an exact sequence of `A`-modules. If `t ∈ A` is `M''`-regular, the sequence*

```text
                       0 → M'/tM' → M/tM → M''/tM'' → 0
```

*is exact.*

Since `M/tM = M ⊗_A (A/tA)`, it suffices to prove exactness at `M'/tM'`; now, if the image `x ∈ M` of an element `x'` of
`M'` is such that `x = ty` with `y ∈ M`, one deduces, for the images `x''`, `y''` of `x, y` in `M''`, `x'' = ty''`; but
as `x'' = 0`, the hypothesis entails `y'' = 0`, hence `y` is the image of an element `y' ∈ M'`, and the relation
`x = ty` entails `x' = ty'` since `M' → M` is injective.

This lemma established, one derives from it the relation

```text
(3.4.1.5)                       long(M/tM) = long(N/tN) + long(P/tP).
```

On the other hand, for every `i`, one has `N_{𝔭_i} = 0` since `t ∉ 𝔭_i`, hence `M_{𝔭_i} = P_{𝔭_i}`; to prove
`(3.4.1.3)`, it suffices to do so by replacing `M` by `P`; on the other hand, if the two sides of `(3.4.1.3)` are equal,
it follows from the same inequality for `P` and from `(3.4.1.5)` that one necessarily has `long(N/tN) = 0`, hence
`N/tN = 0` and finally `N = 0`, by Nakayama's lemma, `N` being of finite type; now, `N = 0` means that `t` is
`M`-regular. One may therefore reduce to the case where `M = P`, that is, suppose already that `t` is `M`-regular. Note
that this entails `𝔪 ∉ Ass(M)`, since `t` cannot annihilate an element `≠ 0` of `M`. As `A` is of dimension `1`, one
therefore has necessarily `Ass(M) ⊂ ⋃_i {𝔭_i}`.

Let us then proceed by induction on `n = ∑_i long(M_{𝔭_i})`. If `n = 0`, one has necessarily `M_{𝔭_i} = 0` for every
`i`, hence `M = 0` since none of the `𝔭_i` belongs to `Ass(M)`; the two sides of `(3.4.1.3)` are then zero, and
assertion β) of `(3.4.1.2)` is trivial. If `n > 0`, the reasoning at the beginning of the proof of `(3.4.1)` allows us
to suppose moreover that the `A`-module `M` is faithful: this entails `M_{𝔭_i} ≠ 0` for every `i` (Bourbaki, *Alg.
comm.*, chap. II, §2, n° 2, cor. 2 of prop. 4), and consequently `Ass(M) = ⋃_i {𝔭_i}`.

Suppose first `n = 1`; there is then only a single minimal prime ideal `𝔭` of `A`,

<!-- original page 48 -->

and to say that `M_𝔭` is of length `1` means that `M_𝔭` is isomorphic to the residue field `k = A_𝔭/𝔭 A_𝔭` as an
`A_𝔭`-module. Consequently `M_𝔭` is annihilated by `𝔭 A_𝔭`, hence `𝔭` is the annihilator of `M` (Bourbaki, *Alg. comm.*,
chap. II, §2, n° 4, formula (9)), which entails `𝔭 = 0` since `M` is supposed faithful; the ring `A` is therefore
integral. This being so, the hypothesis `M ≠ 0` entails `M/tM ≠ 0` by Nakayama's lemma, and consequently
`long(M/tM) ≥ 1`, which proves `(3.4.1.3)` in this case. Moreover, if `long(M/tM) = 1`, `M` is necessarily monogenic
(Bourbaki, *Alg. comm.*, chap. II, §3, n° 2, cor. 2 of prop. 4), hence isomorphic to a quotient `A/𝔟`; since it is
faithful, one necessarily has `𝔟 = 0` and `M` is isomorphic to `A`; as `long(A/tA) = 1`, `tA` is necessarily equal to
the maximal ideal `𝔪`, and as `A` is a Noetherian integral local ring, this proves that `A` is a discrete valuation
ring (Bourbaki, *Alg. comm.*, chap. VI, §3, n° 6, prop. 9), of which `t` is the uniformizer. Conversely, if `A` is a
discrete valuation ring, `t` its uniformizer, `long(M_𝔭) = 1` and if `t` is `M`-regular, then `M` is torsion-free, hence
isomorphic to a sub-module of `A` (`M` being of finite type), and consequently isomorphic to `A` itself, whence
`long(M/tM) = long(A/tA) = 1`.

Suppose now `n ≥ 2`; there then exists an exact sequence

```text
                                 0 → M' → M → M'' → 0
```

with `M' ≠ 0`, `M'' ≠ 0` and `Ass(M) = Ass(M') ∪ Ass(M'')`; indeed, if `Ass(M)` is not reduced to a single element, this
follows from Bourbaki, *Alg. comm.*, chap. IV, §1, n° 1, prop. 4; if on the contrary `Ass(M)` is reduced to a single
prime ideal, this latter is necessarily the unique minimal prime ideal `𝔭` of `A`; the hypothesis then entails
`long(M_𝔭) ≥ 2` and it suffices to take for `M'` the inverse image of a submodule of `M_𝔭` distinct from `0` and from
`M_𝔭`. As `t` is `M`-regular, `t` does not belong to any of the prime ideals of `Ass(M)` (Bourbaki, *Alg. comm.*,
chap. IV, §1, n° 1, cor. 2 of prop. 2), hence, for the same reason, `t` is `M'`-regular and `M''`-regular. This last
property entails by `(3.4.1.4)` that the sequence

```text
                          0 → M'/tM' → M/tM → M''/tM'' → 0
```

is exact; as it is moreover the case for the sequence

```text
                              0 → M'_{𝔭_i} → M_{𝔭_i} → M''_{𝔭_i} → 0
```

for every `i`, one has

```text
                  long(M/tM)     = long(M'/tM') + long(M''/tM'')
                  long(M_{𝔭_i})  = long(M'_{𝔭_i}) + long(M''_{𝔭_i})
```

and the induction hypothesis therefore entails the inequality `(3.4.1.3)`. Moreover the two sides cannot be equal
unless the analogous inequalities for `M'` and `M''` are also equalities. By virtue of the induction hypothesis, this is
equivalent to property β) for the `𝔭_i` such that `M'_{𝔭_i} ≠ 0` or `M''_{𝔭_i} ≠ 0`; but these ideals are precisely those
for which `M_{𝔭_i} ≠ 0`. Q.E.D.

<!-- original page 49 -->

**Corollary (3.4.2).**

<!-- label: IV.3.4.2 -->

*Under the general hypotheses of `(3.4.1)`, suppose that `Z` is not equal to any of the `S_i` and that
`long((ℱ/tℱ)_z) = 1`. Then there exists only one of the `S_i` containing `Z`, and for this value of `i`, one has
`long(ℱ_{s_i}) = 1`; moreover `𝒪_{S_i, z}` is a discrete valuation ring of which `t_z` is a uniformizer, and `t_z` is
`ℱ_z`-regular.*

This results from `(3.4.1)`, the two sides of `(3.4.1.1)` then being equal.

**Proposition (3.4.3).**

<!-- label: IV.3.4.3 -->

*Let `X` be a locally Noetherian prescheme, `t` a section of `𝒪_X` over `X`, `Y` the closed sub-prescheme of `X` defined
by the Ideal `t 𝒪_X` of `𝒪_X`. Let `ℱ` be a coherent `𝒪_X`-Module, `T` an associated prime cycle of `ℱ`, `T'` an
irreducible component of `T ∩ Y`, `x` the generic point of `T'`. Suppose that `t_x` is `ℱ_x`-regular; then one has
`x ∈ Ass(ℱ/tℱ)`.*

As in the proof of `(3.4.1)`, we can reduce to the case where `X = Spec(𝒪_x)`; the proposition is then (taking
into account `(3.1.2)`) a consequence of `(0, 16.4.6.3)`.

**Proposition (3.4.4).**

<!-- label: IV.3.4.4 -->

*Let `X` be a locally Noetherian prescheme, `t` a section of `𝒪_X` over `X`, `Y` the closed sub-prescheme of `X` defined
by the Ideal `t 𝒪_X` of `𝒪_X`. Let `ℱ` be a coherent `𝒪_X`-Module, `(S_i)` the family of irreducible components of
`Supp(ℱ)`. Let `y` be a point of `Y` such that `t_y` is `ℱ_y`-regular and no embedded associated prime cycle of
`ℱ/tℱ` contains `y`. Then the irreducible components of `Supp(ℱ/tℱ)` that contain `y` are exactly the irreducible
components of the `S_i ∩ Y` that contain `y`, and the associated prime cycles of `ℱ` containing `y` are non-embedded.*

Let us first prove the last assertion. Let `T ⊃ T_1` be two associated prime cycles of `ℱ` containing `y`; if `x` is the
generic point of an irreducible component of `T ∩ Y` containing `y`, `x` is a generization of `y`, hence contained in
every neighbourhood of `y`, and the hypothesis that `t_y` is `ℱ_y`-regular entails that `t_x` is `ℱ_x`-regular
`(0, 15.2.4)`, hence, by virtue of `(3.4.3)`, one has `x ∈ Ass(ℱ/tℱ)`. Let `x_1` be the generic point of an irreducible
component of `T_1 ∩ Y` containing `y`, and let `x` be the generic point of an irreducible component of `T ∩ Y`
containing `x_1`; it follows from what precedes that `x_1` and `x` both belong to `Ass(ℱ/tℱ)`, and as `x_1 ∈ ‾{x}`, the
hypothesis entails that `x_1 = x`. Let us again denote by `T` and `T_1` the integral closed sub-preschemes of `X` having
`T` and `T_1` as underlying spaces respectively, and set `A = 𝒪_{T, x}`, `A_1 = 𝒪_{T_1, x}`; one has therefore
`A_1 = A/𝔭`, where `𝔭` is a prime ideal of `A`. By the definition of `x` and `x_1`, `A/tA` and `A_1/tA_1` are Artinian
rings; on the other hand, we saw above that `t_x` is `ℱ_x`-regular, hence `x` cannot belong to `Ass(ℱ)`, and
consequently `A_1` is not Artinian. One therefore has `dim A = dim A_1 = 1`; but this entails `𝔭 = 0` and `A = A_1`
`(0, 16.1.2.2)`; as `Spec(A)` and `Spec(A_1)` are respectively dense in `T` and `T_1`, one has indeed `T = T_1`.

The `S_i` containing `y` are therefore all the associated prime cycles of `ℱ` containing `y`; if `x` is the generic
point of an irreducible component of `S_i ∩ Y` containing `y`, one again deduces from `(0, 15.2.4)` that `t_x` is
`ℱ_x`-regular, hence, by `(3.4.3)`, that `x ∈ Ass(ℱ/tℱ)`; this proves the first assertion of `(3.4.4)`.

**Proposition (3.4.5).**

<!-- label: IV.3.4.5 -->

*Let `X` be a locally Noetherian prescheme, `t` a section of `𝒪_X` over `X`, `Y` the closed sub-prescheme of `X` defined
by the Ideal `t 𝒪_X` of `𝒪_X`. Let `ℱ`*

<!-- original page 50 -->

*be a coherent `𝒪_X`-Module, `y` a point of `Y`; suppose that `t_y` is `ℱ_y`-regular and that `ℱ/tℱ` is integral at the
point `y` `(3.2.4)`. Then `ℱ` is integral at the point `y`.*

Taking into account `(3.4.4)`, it suffices to prove that `y` is contained in a single irreducible component of
`Supp(ℱ)`, and that if `s` is the generic point of this component, one has `long(ℱ_s) = 1`. Now, by hypothesis, `y`
belongs to only a single irreducible component of `Supp(ℱ/tℱ)`, and if `z` is the generic point of this component, one
has `long((ℱ/tℱ)_z) = 1`; the conclusion therefore follows from `(3.4.2)`.

**Proposition (3.4.6).**

<!-- label: IV.3.4.6 -->

*The hypotheses being those of `(3.4.1)`, let `x` be a point of `Y`. Suppose that `Y` contains none of the `S_i`
containing `x`, and that `ℱ/tℱ` is reduced at the point `x` `(3.2.2)`. Then `t_x` is `ℱ_x`-regular and `ℱ` is reduced at
the point `x`. Moreover, if `z` is the generic point of an irreducible component of `Supp(ℱ/tℱ)` containing `x`, `z` is
contained in a single one of the `S_i`, and `𝒪_{S_i, z}` is a discrete valuation ring of which `t_z` is a uniformizer.*

The fact that `t_x` is `ℱ_x`-regular results from the following lemma applied to the ring `𝒪_x`:

**Lemma (3.4.6.1).**

<!-- label: IV.3.4.6.1 -->

*Let `A` be a Noetherian ring, `M` an `A`-module of finite type, `𝔭_i` the minimal elements of `Supp(M)`, `t` an element
of `A`. Suppose that `t` belongs to none of the `𝔭_i` and that `M/tM` is a reduced `A`-module `(3.2.2)`. Then `t` is
`M`-regular.*

Every prime ideal `𝔭 ∈ Supp(M)` contains one of the `𝔭_i`; as `t` belongs to none of the `𝔭_i`, the homothety of ratio
`t` in `M_𝔭` is not nilpotent (Bourbaki, *Alg. comm.*, chap. IV, §1, n° 4, cor. of prop. 9). Let us designate by `N` the
submodule of `M` formed of elements annihilated by a power of `t`, and set `P = M/N`; we shall show that `N = 0`. Since
`t` is `P`-regular, one has an exact sequence `(3.4.1.4)`

```text
                          0 → N/tN → M/tM → P/tP → 0.
```

As `N` is of finite type, it is annihilated by a power of `t`, and it therefore suffices to show that `N/tN = 0`. As
`N/tN` is a submodule of `M/tM`, it suffices to prove that `(N/tN)_𝔭 = 0` for every `𝔭 ∈ Ass(M/tM)`, or again that the
homomorphism `u_𝔭 : (M/tM)_𝔭 → (P/tP)_𝔭` is bijective for every `𝔭 ∈ Ass(M/tM)`. Now one has `(P/tP)_𝔭 ≠ 0`; indeed, as
`𝔭 ∈ Supp(M/tM) = Supp(M) ∩ V(t)` `(0_I, 1.7.5)`, the image of `t` in `A_𝔭` is contained in the maximal ideal `𝔭 A_𝔭`,
hence the hypothesis `P_𝔭 = tP_𝔭` would entail `P_𝔭 = 0` by Nakayama's lemma; one would therefore have `M_𝔭 = N_𝔭` and
the homothety of ratio `t` in `M_𝔭` would be nilpotent; but this contradicts the remark made at the beginning, since
`𝔭 ∈ Supp(M)`. This being so, the hypothesis that `M/tM` is reduced entails `long((M/tM)_𝔭) = 1`, and as
`(P/tP)_𝔭 ≠ 0`, `u_𝔭` is necessarily bijective, which proves the lemma.

By hypothesis, none of the embedded associated prime cycles of `ℱ/tℱ` contains `x`, hence none of the embedded
associated prime cycles of `ℱ` contains `x`, by virtue of `(3.4.4)`. On the other hand, applying `(3.4.2)` to an
irreducible component of `Supp(ℱ/tℱ)` containing `x`, one sees that `long(ℱ_{s_i}) = 1` for every `S_i` containing `x`,
which completes the proof that `ℱ_x` is reduced; finally, the last assertions are also consequences of `(3.4.2)`.

**Corollary (3.4.7).**

<!-- label: IV.3.4.7 -->

*Let `A` be a Noetherian local ring, `𝔪` its maximal ideal, `M` an `A`-module of finite type, `(x_i)_{1 ≤ i ≤ k}` a
family of elements of `𝔪` forming part of a system of*

<!-- original page 51 -->

*parameters for `M` `(0, 16.3.6)`. If the `A`-module `N = M/(∑_{i=1}^k x_i M)` is integral `(3.2.4)`, then `M` is
integral and the sequence `(x_i)_{1 ≤ i ≤ k}` is `M`-regular.*

By induction on `k`, one is immediately reduced to the case `k = 1`; we shall write `x` instead of `x_1`; the hypothesis
that `x` is part of a system of parameters for `M` entails that `dim(N) = dim(M) − 1` `(0, 16.3.7)`. Set `n = dim(N)`;
there is therefore a minimal element `𝔭` of `Supp(M)` such that `dim(M/𝔭 M) = n + 1` `(0, 16.3.4)`, and for every
integer `j > 0` one also then has `dim(M/𝔭^j M) = n + 1` `(0, 16.3.5)`; moreover `x` is part of a system of parameters
for `M/𝔭^j M` `(0, 16.3.5)`, hence, if one sets `M' = M/𝔭^j M` and `N' = M'/xM'`, one has `dim(N') = n`. It is clear
that one has a surjective homomorphism `v : N → N'`; let us show that `v` is bijective. Indeed, if `P = Ker(v)`, one has
`Ass(P) ⊂ Ass(N)`, and since `N` is integral, the hypothesis `P ≠ 0` would entail that `Ass(P)` and `Ass(N)` would
both be reduced to the unique point `𝔮` of `Ass(N) = Supp(N)`; but since `dim(N') = dim(N)`, one has `N'_𝔮 ≠ 0`, and the
hypothesis `long(N_𝔮) = 1` entails `long(N'_𝔮) = 1` since `N_𝔮 → N'_𝔮` is surjective. One would therefore have
`P_𝔮 = 0`, contrary to the hypothesis, whence our assertion. But then `N'`, being isomorphic to `N`, is integral;
moreover, the support of `N'` (equal to the intersection of `Supp(M)` and `V(x)`) cannot contain `Supp(M')`, and this
latter set is irreducible by construction. The hypothesis that `M'/xM'` is integral (hence reduced) then entails that
`x` is `M'`-regular by virtue of `(3.4.6)`. One concludes that the kernel of the homothety `z ↦ x z` in `M` is contained
in `𝔭^j M ⊂ 𝔪^j M` for every integer `j`, and this kernel is therefore reduced to `0` `(0_I, 7.3.5)`, which proves that
`x` is `M`-regular. One can then apply `(3.4.5)`, which proves that `M` is integral.

**Remark (3.4.8).**

<!-- label: IV.3.4.8 -->

*The proposition analogous to `(3.4.7)`, where one replaces "integral" by "reduced", is no longer necessarily exact.
Consider for example the polynomial ring `C = K[X, Y, Z]` over a field `K`, the quotient ring `B = C/𝔭𝔮`, where
`𝔭 = CZ`, `𝔮 = CX² + CY`; let `A` be the local ring of `B` corresponding to the image maximal ideal of `CX + CY + CZ` in
`B`. If `x`, `z` are the canonical images of `X`, `Z` in `A`, it is clear that `xz ≠ 0` but `x² z² = 0`; on the other
hand, as `A/xA` is isomorphic to `K[Y, Z]/(YZ)`, one has `dim(A/xA) = 1` while `dim(A) = 2`, hence `x` belongs to a
system of parameters for `A` `(0, 16.3.4)`, `A/xA` is reduced, but `A` is not.*

**Proposition (3.4.9).**

<!-- label: IV.3.4.9 -->

*Let `A` be a Noetherian ring, `M` an `A`-module of finite type, `f` an `M`-regular element of `A` such that `M/fM` has
no embedded associated prime ideals. If `𝔭_i` `(1 ≤ i ≤ m)` are the prime ideals associated to `M/fM`, then, for every
integer `n > 0`, `f^n M` is the intersection of the inverse images of the `f^n M_{𝔭_i}` by the canonical maps
`M → M_{𝔭_i}` `(1 ≤ i ≤ m)`.*

Everything reduces to showing that the `𝔭_i` are also the prime ideals associated to `M/f^n M`, since then the saturates
of `f^n M` for the `𝔭_i` are the submodules of the reduced primary decomposition (necessarily unique) of `f^n M` in
`M`. Now, one has

```text
        Ass(f^{n-1} M/f^n M) ⊂ Ass(M/f^n M) ⊂ Ass(M/f^{n-1} M) ∪ Ass(f^{n-1} M/f^n M)
```

by `(3.1.7)`, and since `f` is `M`-regular, `f^{n-1} M/f^n M` is isomorphic to `M/fM`; it then suffices to reason by
induction on `n`.


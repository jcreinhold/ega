# §9. Constructible sets

<!-- original page 356 -->

## 9.1. Constructible sets

**Definition (9.1.1).**

<!-- label: 0_III.9.1.1 -->

*We say that a continuous map `f : X → Y` is **quasi-compact** if, for every quasi-compact open set `U` of `Y`, `f⁻¹(U)`
is quasi-compact. We say that a subset `Z` of a topological space `X` is **retrocompact in `X`** if the canonical
injection `Z ↪ X` is quasi-compact, in other words if, for every quasi-compact open set `U` of `X`, `U ∩ Z` is
quasi-compact.*

A closed subset of `X` is retrocompact in `X`, but a quasi-compact subset of `X` is not necessarily retrocompact in `X`.
If `X` is quasi-compact, every open subset retrocompact in `X` is quasi-compact. It is clear that every finite union of
subsets retrocompact in `X` is retrocompact in `X`, since every finite union of quasi-compact sets is quasi-compact.
Every finite intersection of open sets retrocompact in `X` is an open set retrocompact in `X`. In a locally Noetherian
space `X`, every quasi-compact subset is a Noetherian subspace, and hence every subset of `X` is retrocompact in `X`.

**Definition (9.1.2).**

<!-- label: 0_III.9.1.2 -->

*Given a topological space `X`, we say that a subset of `X` is **constructible** if it belongs to the smallest set of
subsets `𝔉` of `X` containing all the open subsets retrocompact in `X` and stable under finite intersection and passage
to the complement (which implies that `𝔉` is also stable under finite union).*

**Proposition (9.1.3).**

<!-- label: 0_III.9.1.3 -->

*For a subset of `X` to be constructible, it is necessary and sufficient that it be a finite union of sets of the form
`U ∩ ∁V`, where `U` and `V` are open sets retrocompact in `X`.*

**Proof.** It is clear that the condition is sufficient. To see that it is necessary, consider the set `𝔊` of finite
unions of sets of the form `U ∩ ∁V` where `U` and `V` are open sets retrocompact in `X`; it suffices to show that every
complement of a set in `𝔊` belongs to `𝔊`. Let then `Z = ⋃_{i ∈ I} (U_i ∩ ∁V_i)`, where `I` is finite and the `U_i`,
`V_i` are open sets retrocompact in `X`; we have `∁Z = ⋂_{i ∈ I} (V_i ∪ ∁U_i)`, so `Z` is a finite union of sets that
are intersections of a certain number of the `V_i` and of a certain number of the `∁U_i`, hence of the form

<!-- original page 357 -->

`V ∩ ∁U`, where `U` is a union of a certain number of the `U_i` and `V` an intersection of a certain number of the
`V_i`; but we observed above that finite unions and intersections of open sets retrocompact in `X` are open sets
retrocompact in `X`, whence the conclusion.

**Corollary (9.1.4).**

<!-- label: 0_III.9.1.4 -->

*Every constructible subset of `X` is retrocompact in `X`.*

**Proof.** It suffices to show that if `U` and `V` are open sets retrocompact in `X`, then `U ∩ ∁V` is retrocompact in
`X`; now, if `W` is a quasi-compact open set in `X`, then `W ∩ U ∩ ∁V` is closed in the quasi-compact space `W ∩ U`, so
is quasi-compact.

In particular:

**Corollary (9.1.5).**

<!-- label: 0_III.9.1.5 -->

*For an open subset `U` of `X` to be constructible, it is necessary and sufficient that it be retrocompact in `X`. For a
closed subset `F` of `X` to be constructible, it is necessary and sufficient that the open set `∁F` be retrocompact.*

**9.1.6.**

<!-- label: 0_III.9.1.6 -->

An important case is the one in which every quasi-compact open subset of `X` is retrocompact, in other words, in which
the intersection of two quasi-compact open subsets of `X` is quasi-compact (cf. `(I, 5.5.6)`). When `X` itself is
quasi-compact, this means that the open subsets retrocompact in `X` are identical to the quasi-compact open subsets of
`X`, and the constructible subsets of `X` to the finite unions of sets of the form `U ∩ ∁V`, where `U` and `V` are
quasi-compact open sets.

**Corollary (9.1.7).**

<!-- label: 0_III.9.1.7 -->

*For a subset of a Noetherian space `X` to be constructible, it is necessary and sufficient that it be a finite union of
locally closed subsets of `X`.*

**Proposition (9.1.8).**

<!-- label: 0_III.9.1.8 -->

*Let `X` be a topological space, `U` an open subset of `X`.*

*(i) If `T` is a constructible subset of `X`, then `T ∩ U` is a constructible subset of `U`.*

*(ii) Suppose in addition that `U` is retrocompact in `X`. For a subset `Z` of `U` to be constructible in `X`, it is
necessary and sufficient that it be constructible in `U`.*

**Proof.** (i) Using (9.1.3), we are reduced to showing that if `T` is open retrocompact in `X`, then `T ∩ U` is open
retrocompact in `U`, in other words, for every quasi-compact open `W ⊆ U`, that `T ∩ U ∩ W = T ∩ W` is quasi-compact,
which follows immediately from the hypothesis.

(ii) The condition being necessary by (i), it remains to prove that it is sufficient. Taking (9.1.3) into account, it
suffices to consider the case where `Z` is open retrocompact in `U`, for it will then follow that `U − Z` is
constructible in `X`, and if `Z`, `Z'` are two open sets retrocompact in `U`, then `Z ∩ (U − Z')` will indeed be
constructible in `X`. Now, if `W` is open quasi-compact in `X` and `Z` is open retrocompact in `U`, we have
`Z ∩ W = Z ∩ (W ∩ U)` and by hypothesis `W ∩ U` is open quasi-compact in `U`; so `W ∩ Z` is indeed quasi-compact, and
consequently `Z` is open retrocompact in `X`, and *a fortiori* constructible in `X`.

**Corollary (9.1.9).**

<!-- label: 0_III.9.1.9 -->

*Let `X` be a topological space, `(U_i)_{i ∈ I}` a finite cover of `X` by open sets retrocompact in `X`. For a subset
`Z` of `X` to be constructible in `X`, it is necessary and sufficient that for every `i ∈ I`, `Z ∩ U_i` be constructible
in `U_i`.*

**9.1.10.**

<!-- label: 0_III.9.1.10 -->

Suppose in particular that `X` is quasi-compact and that every point

<!-- original page 358 -->

of `X` admits a fundamental system of open neighborhoods retrocompact in `X` (and *a fortiori* quasi-compact); then the
condition for a subset `Z` of `X` to be constructible in `X` is of local nature, in other words, it is necessary and
sufficient that for every `x ∈ X` there exist an open neighborhood `V` of `x` such that `V ∩ Z` be constructible in `V`.
Indeed, if this condition is satisfied, then for every `x ∈ X` there exists an open neighborhood `V` of `x` retrocompact
in `X` and such that `V ∩ Z` is constructible in `V`, by virtue of the hypothesis on `X` and of (9.1.8, (i)); it then
suffices to cover `X` by finitely many of these neighborhoods and to apply (9.1.9).

**Definition (9.1.11).**

<!-- label: 0_III.9.1.11 -->

*Let `X` be a topological space. We say that a subset `T` of `X` is **locally constructible in `X`** if, for every
`x ∈ X`, there exists an open neighborhood `V` of `x` such that `T ∩ V` be constructible in `V`.*

It follows immediately from (9.1.8, (i)) that if `V` is such that `V ∩ T` is constructible in `V`, then for every open
set `W ⊆ V`, `W ∩ T` is constructible in `W`. If `T` is locally constructible in `X`, then, for every open set `U` of
`X`, `T ∩ U` is locally constructible in `U`, as follows from the preceding remark. The same remark shows that the set
of subsets locally constructible in `X` is stable under finite union and finite intersection; it is clear, on the other
hand, that it is also stable under passage to complements.

**Proposition (9.1.12).**

<!-- label: 0_III.9.1.12 -->

*Let `X` be a topological space. Every set constructible in `X` is locally constructible in `X`. The converse is true if
`X` is quasi-compact and if its topology admits a base formed of sets retrocompact in `X`.*

**Proof.** The first assertion follows from the definition (9.1.11), and the second from (9.1.10).

**Corollary (9.1.13).**

<!-- label: 0_III.9.1.13 -->

*Let `X` be a topological space whose topology admits a base formed of sets retrocompact in `X`. Then every subset `T`
locally constructible in `X` is retrocompact in `X`.*

**Proof.** Indeed, let `U` be a quasi-compact open set in `X`; then `T ∩ U` is locally constructible in `U`, hence
constructible in `U` by virtue of (9.1.12), and consequently quasi-compact by virtue of (9.1.4).

## 9.2. Constructible sets in Noetherian spaces

**9.2.1.**

<!-- label: 0_III.9.2.1 -->

We have seen (9.1.7) that, in a Noetherian space `X`, the constructible subsets in `X` are the finite unions of locally
closed subsets of `X`.

The inverse image of a constructible set in `X` under a continuous map of a Noetherian space `X'` into `X` is
constructible in `X'`. If `Y` is a constructible subset of a Noetherian space `X`, the subsets of `Y` that are
constructible as subspaces of `Y` are identical to those that are constructible as subspaces of `X`.

**Proposition (9.2.2).**

<!-- label: 0_III.9.2.2 -->

*Let `X` be an irreducible Noetherian space, `E` a constructible subset of `X`. For `E` to be everywhere dense in `X`,
it is necessary and sufficient that `E` contain a nonempty open subset of `X`.*

<!-- original page 359 -->

**Proof.** The condition is obviously sufficient, every nonempty open set being dense in `X`. Conversely, let
`E = ⋃_{i=1}^n (U_i ∩ F_i)` be a constructible subset of `X`, the `U_i` being nonempty open sets and the `F_i` closed
sets in `X`; we then have `Ē ⊆ ⋃_i F_i`. Consequently, if `Ē = X`, then `X` equals one of the `F_i`, so `E ⊇ U_i`, which
completes the proof.

When `X` admits a generic point `x` `(0_I, 2.1.2)`, the condition of (9.2.2) is equivalent to the relation `x ∈ E`.

**Proposition (9.2.3).**

<!-- label: 0_III.9.2.3 -->

*Let `X` be a Noetherian space. For a subset `E` of `X` to be constructible, it is necessary and sufficient that, for
every closed irreducible subset `Y` of `X`, `E ∩ Y` be rare in `Y` or contain a nonempty open subset of `Y`.*

**Proof.** The necessity of the condition comes from the fact that `E ∩ Y` must be a constructible subset of `Y` and
from (9.2.2), for a non-dense subset of `Y` is necessarily rare in the irreducible space `Y` `(0_I, 2.1.1)`. To prove
that the condition is sufficient, we apply the principle of Noetherian induction `(0_I, 2.2.2)` to the set `𝔉` of closed
subsets `Y` of `X` such that `Y ∩ E` is constructible (with respect to `Y` or with respect to `X`, which comes to the
same thing): we may therefore suppose that for every closed subset `Y ≠ X` of `X`, `E ∩ Y` is constructible. Suppose
first that `X` is not irreducible, and let `X_i` (`1 ≤ i ≤ m`) be its irreducible components, necessarily finite in
number `(0_I, 2.2.5)`; by hypothesis, the `E ∩ X_i` are constructible, hence so is their union `E`. Suppose next that
`X` is irreducible; then, by hypothesis, either `E` is rare, so `Ē ≠ X` and `E = E ∩ Ē` is constructible; or `E`
contains a nonempty open set `U` of `E`, hence is the union of `U` and `E ∩ (X − U)`; but `X − U` is a closed set
distinct from `X`, so `E ∩ (X − U)` is constructible; `E` itself is therefore constructible, which completes the proof.

**Corollary (9.2.4).**

<!-- label: 0_III.9.2.4 -->

*Let `X` be a Noetherian space, `(E_α)` an increasing filtering family of constructible subsets of `X`, such that:*

*1° `X` is the union of the family `(E_α)`.*

*2° Every closed irreducible subset of `X` is contained in the closure of one of the `E_α`.*

*Then there exists an index `α` such that `X = E_α`.*

*When every closed irreducible subset of `X` admits a generic point, hypothesis 2° may be suppressed.*

**Proof.** We apply the principle of Noetherian induction `(0_I, 2.2.2)` to the set `𝔐` of closed subsets of `X`
contained in at least one of the `E_α`; we may therefore suppose that every closed subset `Y ≠ X` of `X` is contained in
one of the `E_α`. The proposition is evident if `X` is not irreducible, for each of the irreducible components `X_i` of
`X` (`1 ≤ i ≤ m`) is contained in some `E_{α_i}`, and there exists an `E_α` containing all the `E_{α_i}`. Suppose
therefore that `X` is irreducible. By hypothesis, there exists `β` such that `X = Ē_β`, so by (9.2.2) `E_β` contains a
nonempty open set `U` of `X`. But then the closed set `X − U` is contained in some `E_γ`, and it suffices to take `E_α`
containing `E_β` and `E_γ`. When every closed irreducible subset `Y` of `X`

<!-- original page 360 -->

admits a generic point `y`, there exists `α` such that `y ∈ E_α`, hence `Y = {y}̄ ⊆ Ē_α`, and condition 2° is a
consequence of 1°.

**Proposition (9.2.5).**

<!-- label: 0_III.9.2.5 -->

*Let `X` be a Noetherian space, `x` a point of `X`, `E` a constructible subset of `X`. For `E` to be a neighborhood of
`x`, it is necessary and sufficient that for every closed irreducible subset `Y` of `X` containing `x`, `E ∩ Y` be dense
in `Y` (if there exists a generic point `y` of `Y`, this also means (9.2.2) that `y ∈ E`).*

**Proof.** The condition is obviously necessary; let us prove that it is sufficient. Applying the principle of
Noetherian induction to the set `𝔐` of closed subsets `Y` of `X` containing `x` and such that `E ∩ Y` be a neighborhood
of `x` in `Y`, we may suppose that every closed subset `Y ≠ X` of `X` containing `x` belongs to `𝔐`. If `X` is not
irreducible, each of the irreducible components `X_i` of `X` containing `x` is distinct from `X`, so `E ∩ X_i` is a
neighborhood of `x` with respect to `X_i`; consequently, `E` is a neighborhood of `x` in the union of the irreducible
components of `X` containing `x`, and since this union is a neighborhood of `x` in `X`, the same holds for `E`. If `X`
is irreducible, then `E` is dense in `X` by hypothesis, hence contains a nonempty open subset `U` of `X` (9.2.2); the
proposition is then evident if `x ∈ U`; otherwise, `x` is by hypothesis interior to `E ∩ (X − U)` with respect to
`X − U`, so the closure in `X` of `X − E` does not contain `x`, and the complement of this closure is a neighborhood of
`x` contained in `E`, which completes the proof.

**Corollary (9.2.6).**

<!-- label: 0_III.9.2.6 -->

*Let `X` be a Noetherian space, `E` a subset of `X`. For `E` to be an open set in `X`, it is necessary and sufficient
that for every closed irreducible subset `Y` of `X` meeting `E`, `E ∩ Y` contain a nonempty open subset of `Y`.*

**Proof.** The condition is obviously necessary; conversely, if it is satisfied, it implies that `E` is constructible by
virtue of (9.2.3). In addition, (9.2.5) shows that `E` is then a neighborhood of each of its points, whence the
conclusion.

## 9.3. Constructible functions

**Definition (9.3.1).**

<!-- label: 0_III.9.3.1 -->

*Let `h` be a map from a topological space `X` to a set `T`. We say that `h` is **constructible** if `h⁻¹(t)` is
constructible for every `t ∈ T`, and empty except for finitely many values of `t`; for every subset `S` of `T`, `h⁻¹(S)`
is then constructible. We say that `h` is **locally constructible** if every `x ∈ X` has an open neighborhood `V` such
that `h ∣ V` is constructible.*

Every constructible function is locally constructible; the converse is true when `X` is quasi-compact and admits a base
formed of open sets retrocompact in `X` (in particular when `X` is Noetherian).

**Proposition (9.3.2).**

<!-- label: 0_III.9.3.2 -->

*Let `h` be a map from a Noetherian space `X` to a set `T`. For `h` to be constructible, it is necessary and sufficient
that for every closed irreducible subset `Y` of `X`, there exist a nonempty subset `U` of `Y`, open with respect to `Y`,
in which `h` is constant.*

**Proof.** The condition is necessary: indeed, by hypothesis, `h` takes only finitely many values `t_i` in `Y`, and each
of the sets `h⁻¹(t_i) ∩ Y` is constructible in `Y` (9.2.1); since they cannot all be rare subsets of the space `Y`, at
least one of them contains a nonempty open set (9.2.3).

<!-- original page 361 -->

To see that the condition is sufficient, we apply the principle of Noetherian induction to the set `𝔐` of closed subsets
`Y` of `X` such that the restriction `h ∣ Y` is constructible; we may therefore suppose that for every closed subset
`Y ≠ X` of `X`, `h ∣ Y` is constructible. If `X` is not irreducible, the restriction of `h` to each of the irreducible
components `X_i` of `X` (finite in number) is therefore constructible, and it then follows immediately from the
definition (9.3.1) that `h` is constructible. If `X` is irreducible, there exists by hypothesis a nonempty open subset
`U` of `X` in which `h` is constant; on the other hand, the restriction of `h` to `X − U` is constructible by
hypothesis, and it follows immediately that `h` is constructible.

**Corollary (9.3.3).**

<!-- label: 0_III.9.3.3 -->

*Let `X` be a Noetherian space in which every closed irreducible subset admits a generic point. If `h` is a map of `X`
into a set `T` such that, for every `t ∈ T`, `h⁻¹(t)` is constructible, then `h` is constructible.*

**Proof.** Indeed, if `Y` is a closed irreducible subset of `X` and `y` its generic point, then `Y ∩ h⁻¹(h(y))` is
constructible and contains `y`, so by (9.2.2) this set contains a nonempty open subset of `Y`, and it suffices to apply
(9.3.2).

**Proposition (9.3.4).**

<!-- label: 0_III.9.3.4 -->

*Let `X` be a Noetherian space in which every closed irreducible subset admits a generic point, `h` a constructible map
of `X` into an ordered set. For `h` to be upper semi-continuous in `X`, it is necessary and sufficient that for every
`x ∈ X` and every generization `(0_I, 2.1.2)` `x'` of `x`, one have `h(x') ≤ h(x)`.*

**Proof.** The function `h` takes only finitely many values; to say that it is upper semi-continuous therefore means
that for every `x ∈ X`, the set `E` of `y ∈ X` such that `h(y) ≤ h(x)` is a neighborhood of `x`. By hypothesis, `E` is a
constructible subset of `X`; on the other hand, to say that a closed irreducible subset `Y` of `X` contains `x` means
that its generic point `y` is a generization of `x`; the conclusion then follows from (9.2.5).

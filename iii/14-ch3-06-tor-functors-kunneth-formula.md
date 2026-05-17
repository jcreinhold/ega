# §6. Local and global Tor functors; the Künneth formula

> _Translator's note._ This section is translated in two parts for length: §6.1–§6.6 here, §6.7–§6.9 in the companion
> file. They will be concatenated for the final volume.

<!-- original page 137 -->

## 6.1. Introduction.

**6.1.1.**

<!-- label: III.6.1.1 -->

Let `f : X → Y` be a morphism of preschemes and let `ℱ` be a quasi-coherent `𝒪_X`-module. In the study of the "higher
direct images" `R^n f_*(ℱ)`, one is led to consider the following general problem: given a "base change" morphism
`g : Y' → Y`, we set `X' = X_{(Y')} = X ×_Y Y'`, `ℱ' = ℱ ⊗_{𝒪_Y} 𝒪_{Y'}`, `f' = f_{(Y')} : X' → Y'`, and we propose to
obtain information on the higher direct images `R^n f'_*(ℱ')` (assuming the `R^n f_*(ℱ)` known). One sees easily (cf.
for example `(7.7.2)`) that one is reduced to studying the variations of `R^n f_*(ℱ ⊗_{𝒪_Y} 𝒢)` for a variable
quasi-coherent `𝒪_Y`-module `𝒢`, in other words the functor `𝒢 ↦ R^n f_*(ℱ ⊗_{𝒪_Y} 𝒢)`. If `ℱ` is flat over `Y`, the
functor `𝒢 ↦ ℱ ⊗_{𝒪_Y} 𝒢` is exact `(0_I, 6.7.4)`, and consequently the composite functor `𝒢 ↦ R^n f_*(ℱ ⊗_{𝒪_Y} 𝒢)` is
again a cohomological functor. But this is no longer the case in general; in order to be able to apply the cohomological
methods, one is led to substitute for `𝒢 ↦ R^n f_*(ℱ ⊗_{𝒪_Y} 𝒢)` other functors which this time are *always*
cohomological functors. These functors, which generalize the "Tor" functors of module theory, are defined in n°s `6.3`
to `6.7`; there are moreover two such generalizations, one "local" and the other "global", related by spectral sequences
that will be discussed in n° `6.7`; as an application of these spectral sequences, one obtains in particular, under
certain conditions, a "Künneth formula" expressing `R^n (f_1 × f_2)_*(ℱ_1 ⊗_Y ℱ_2)` by means of the higher direct images
`R^p f_{1*}(ℱ_1)` and `R^q f_{2*}(ℱ_2)`. Other spectral sequences `(6.8)` generalize the associativity spectral
sequences of the "Tor" functor of modules; finally, the base-change problem itself leads to spectral sequences `(6.9)`.

**6.1.2.**

<!-- label: III.6.1.2 -->

In addition, one observes `(6.10)` that the cohomological functors `𝒢 ↦ 𝒯_i(𝒢)` so defined are locally (on `Y`) of the
type `𝒢 ↦ ℋ_i(ℒ_• ⊗_Y 𝒢)`, where `ℒ_•` is a complex of locally free `𝒪_Y`-modules (defined up to homotopy) and `ℋ_•`
denotes homology. There is then an interest in forgetting the particular situation that gave

<!-- original page 138 -->

rise to `𝒯_i`, and in studying in general the functors of the preceding form `𝒢 ↦ ℋ_i(ℒ_• ⊗_Y 𝒢)` (where one moreover,
if appropriate, makes finiteness hypotheses on the `ℒ_i` or the `ℋ_i(ℒ_•)`): this is the object of §7, whose reading,
for the essentials, is independent of §6. The most important properties of these functors concern the exactness
properties of a component `𝒯_i` of `𝒯_•`; we shall give various criteria allowing such properties to be established; as
an application, one will obtain conditions allowing one to assert (with the notations of `(6.1.1)`) that the functor
`𝒢 ↦ R^n f_*(ℱ ⊗_{𝒪_Y} 𝒢)` is exact (which one will express by saying that `ℱ` is *cohomologically flat over* `Y` in
dimension `n`). Another important property for the components `𝒯_i` of `𝒯_•(𝒢) = ℋ_i(ℒ_• ⊗_Y 𝒢)` is the *semi-continuity
property* of the function `y ↦ dim_{κ(y)}(𝒯_i(κ(y)))`; when `𝒯_i` is exact, this property is replaced by a *continuity
property*, the converse being moreover true according to Grauert when `Y` is reduced `(7.8.4)`.

**6.1.3.**

<!-- label: III.6.1.3 -->

In §§ 6 and 7, we have systematically made use of *hypercohomology*, taking everywhere as arguments *complexes* of
sheaves instead of sheaves, although the necessity of this point of view will appear only in later chapters. The
cohomological formalism developed on this occasion will moreover become more transparent in the chapter of this Treatise
that will be devoted to the elaboration of an algebra of cohomological functors of coherent sheaves, including the
duality formalism. But that will require developments which fall outside the framework of the present chapter.

**6.1.4.**

<!-- label: III.6.1.4 -->

To abbreviate, given two complexes `K^•`, `K'^•` in an abelian category `𝒞`, we shall say that a morphism of complexes
`f : K^• → K'^•` is a *homotopism* if there exists a morphism `g : K'^• → K^•` such that the composite morphisms `f ∘ g`
and `g ∘ f` are both homotopic to the identity (by abuse of language, when such a homotopism exists, one also says that
`K^•` and `K'^•` are *homotopic*). When one can define the hypercohomology of a covariant additive functor `T` from `𝒞`
into an abelian category `𝒞'` with respect to a complex of `𝒞` `(0_III, 11.4.3)`, it is immediate that a homotopism
`K^• → K'^•` of complexes of `𝒞` canonically defines an isomorphism `R^• T(K^•) → R^• T(K'^•)` for hypercohomology (loc.
cit.).

## 6.2. Hypercohomology of complexes of modules on a prescheme.

**6.2.1.**

<!-- label: III.6.2.1 -->

Let `X` be a prescheme and `𝒦^• = (𝒦^i)_{i ∈ ℤ}` a complex of `𝒪_X`-modules whose differential is of degree `+1`. Recall
that for every morphism `f : X → Y` of preschemes, one has defined `(0_III, 12.4.1)` the `𝒪_Y`-modules of
hypercohomology `ℋ^n(f, 𝒦^•)` (also denoted `ℋ^n(𝒦^•)` or `R^n f_*(𝒦^•)`) for every `n ∈ ℤ`; the hypercohomology
`ℋ^•(f, 𝒦^•)` is the abutment of the two spectral functors `'ℰ(f, 𝒦^•)` and `''ℰ(f, 𝒦^•)`, whose `E_2` terms are given
by

```text
  'E_2^{p,q} = ℋ^p(ℋ^q(f, 𝒦^•))                                                (6.2.1.1)
  ''E_2^{p,q} = ℋ^p(f, ℋ^q(𝒦^•)) = R^p f_*(ℋ^q(𝒦^•))                            (6.2.1.2)
```

<!-- original page 139 -->

where `ℋ^•(f, 𝒦^•)` is the complex whose component of degree `i` is `ℋ^i(f, 𝒦^•) = R^i f_*(𝒦^i)` (loc. cit.). Recall
also that when `Y` is reduced to a point, one denotes the corresponding hypercohomology by `H^•(X, 𝒦^•)` (which is
formed of modules over `Γ(X, 𝒪_X)` independent of the punctual prescheme `Y` considered); when `Y = X` and `f = 1_X`,
one has `ℋ^n(f, 𝒦^•) = ℋ^n(𝒦^•)` (cohomology of the complex `𝒦^•`); when `𝒦^i = 0` except for `i = i_0`, one has

```text
  ℋ^n(f, 𝒦^•) = R^{n − i_0} f_*(𝒦^{i_0}).
```

The spectral sequence `'ℰ(f, 𝒦^•)` is always regular; the two spectral sequences are biregular when `𝒦^•` is bounded
below `(0_III, 12.4.1)`. Every homotopism `h : 𝒦^• → 𝒦'^•` of complexes of `𝒪_X`-modules `(6.1.4)` gives an isomorphism
`ℋ^•(f, 𝒦^•) ⥲ ℋ^•(f, 𝒦'^•)` for hypercohomology. The same holds when one assumes only that
`ℋ^•(h) : ℋ^•(𝒦^•) → ℋ^•(𝒦'^•)` is an isomorphism and that `𝒦^•` and `𝒦'^•` are *bounded below*, as follows at once from
`(0_III, 11.1.5)` applied to the spectral sequence `(6.2.1.2)` and to the analogous one for `𝒦'^•`. Finally, for every
open cover `𝔘 = (U_α)` of `X`, one has also defined `(0_III, 12.4.5)` the hypercohomology `H^•(𝔘, 𝒦^•)` as the
cohomology of the bicomplex `C^•(𝔘, 𝒦^•)` (whose component of bi-indices `(i, j)` is by definition `C^i(𝔘, 𝒦^j)`); the
`H^n(𝔘, 𝒦^•)` are again modules over `Γ(X, 𝒪_X)`.

**Proposition (6.2.2).**

<!-- label: III.6.2.2 -->

*Let `X` be a scheme and `𝔘 = (U_α)` a cover of `X` by affine open sets. For every complex `𝒦^•` of quasi-coherent
`𝒪_X`-modules, the hypercohomology modules `H^•(X, 𝒦^•)` and `H^•(𝔘, 𝒦^•)` are canonically isomorphic.*

**Proof.** Indeed, every finite intersection `V` of open sets of the cover `𝔘` is affine `(I, 5.5.6)`, so
`H^q(V, 𝒦^i) = 0` for every `i` and every `q > 0` `(1.3.1)`; the proposition is therefore a particular case of
`(0_III, 12.4.7)`.

**Proposition (6.2.3).**

<!-- label: III.6.2.3 -->

*Let `f : X → Y` be a quasi-compact and separated morphism of preschemes. For every complex `𝒦^•` of quasi-coherent
`𝒪_X`-modules, the `𝒪_Y`-modules `ℋ^n(f, 𝒦^•)` are quasi-coherent.*

**Proof.** Since the `ℋ^q(f, 𝒦^i) = R^q f_*(𝒦^i)` are quasi-coherent `𝒪_Y`-modules `(1.4.10)`, the same holds for
`'E_2^{p,q}`, which, by `(6.2.1.1)`, is a quotient of a kernel of a homomorphism of quasi-coherent modules by an image
of such a homomorphism `(I, 4.1.1)`. For the same reason, all the `𝒪_Y`-modules `'E_r^{p,q}`, `B_r('E_r^{p,q})`,
`Z_r('E_r^{p,q})` of the first spectral sequence are quasi-coherent. The regularity of the spectral sequence
`'ℰ(f, 𝒦^•)` implies that `Z_∞('E_2^{p,q})` is equal to one of the `Z_k('E_2^{p,q})`, hence is quasi-coherent, and the
same holds for `B_∞('E_2^{p,q}) = lim_→ B_k('E_2^{p,q})` `(0_III, 11.2.4)` and `(I, 4.1.1)`; the `'E_∞^{p,q}` are
therefore also quasi-coherent. The preceding spectral sequence being regular, the filtration of the `F^p(ℋ^n(f, 𝒦^•))`
is discrete and exhaustive; in other words, the `𝒪_Y`-module `ℋ^n(f, 𝒦^•)` is the union of an increasing sequence
`(𝒢_k)_{k ≥ 0}` of `𝒪_Y`-modules such that `𝒢_0 = 0` and such that each `𝒢_k/𝒢_{k−1}` is equal to one of the
`𝒪_Y`-modules `'E_∞^{p,q}`, hence is quasi-coherent. By induction on `k`, one deduces that the `𝒢_k` are quasi-coherent
`(I, 4.1.17)`, and since `ℋ^n(f, 𝒦^•) = lim_→ 𝒢_k`, the proposition is proved `(I, 4.1.1)`.

<!-- original page 140 -->

**Corollary (6.2.4).**

<!-- label: III.6.2.4 -->

*Under the hypotheses of `(6.2.3)`, for every affine open `V` of `Y`, the canonical homomorphism*

```text
  H^n(f⁻¹(V), 𝒦^•) → Γ(V, ℋ^n(f, 𝒦^•))                                          (6.2.4.1)
```

*is bijective for every `n ∈ ℤ`.*

**Proof.** The proof is the same as that of `(1.4.11)`, using `(6.2.2)`, replacing `ℱ` by `𝒦^•`, `𝒦^•` by
`f_*(𝒞^•(𝔘, 𝒦^•))`, `ℋ^•(𝒦^•)` by `ℋ^•(f, 𝒦^•)`, and noting that the latter is a quasi-coherent `𝒪_Y`-module by
`(6.2.3)`.

**Proposition (6.2.5).**

<!-- label: III.6.2.5 -->

*Let `Y` be a locally noetherian prescheme, `f : X → Y` a proper morphism, `𝒦^•` a complex of `𝒪_X`-modules such that
the `𝒪_X`-modules `ℋ^q(𝒦^•)` are coherent. Then the `𝒪_Y`-modules `ℋ^n(f, 𝒦^•)` are coherent.*

**Proof.** The question being local on `Y`, one may restrict to the case where `Y` is noetherian and affine, and it is
therefore, by `(6.2.4)`, a matter of proving that the `H^n(X, 𝒦^•)` are `Γ(Y, 𝒪_Y)`-modules of finite type. One has then
`H^•(X, 𝒦^•) = H^•(𝔘, 𝒦^•)` `(6.2.2)`, where one may assume that `𝔘` is *finite*, since `X` is quasi-compact. The
cochains of each complex `C^•(𝔘, 𝒦^i)` being *alternating* by definition, there is an integer `r > 0` such that
`C^i(𝔘, 𝒦^j) = 0` for `i < 0` and `i > r`; one concludes `(0_III, 11.3.3)` that the two spectral sequences of the
bicomplex `C^•(𝔘, 𝒦^•)` are biregular. Since the intersections of the sets of `𝔘` are affine open sets `(I, 5.5.6)`,
each functor `ℱ ↦ C^i(𝔘, ℱ)` is exact in the category of quasi-coherent `𝒪_X`-modules; hence
`H_q^i(C^•(𝔘, 𝒦^•)) = C^i(𝔘, ℋ^q(𝒦^•))`, and the `E_2` terms of the second spectral sequence of `C^•(𝔘, 𝒦^•)` are given
`(0_III, 11.3.2)` by

```text
  ''E_2^{p,q} = H^p(C^•(𝔘, ℋ^q(𝒦^•))) = H^p(𝔘, ℋ^q(𝒦^•)) = H^p(X, ℋ^q(𝒦^•))
```

by `(1.4.1)`; since `f` is proper, these are `Γ(Y, 𝒪_Y)`-modules of finite type `(3.2.1)`. The spectral sequence
`''ℰ(C^•(𝔘, 𝒦^•))` being biregular, one deduces that the `H^n(X, 𝒦^•)` are `Γ(Y, 𝒪_Y)`-modules of finite type
`(0_III, 11.1.8)`.

*A fortiori*, if `𝒦^•` is a complex of coherent `𝒪_X`-modules, the `𝒪_Y`-modules `ℋ^n(f, 𝒦^•)` are coherent under the
hypotheses of `(6.2.5)` relative to `Y` and `f` `(0_I, 5.3.4)`.

**6.2.6.**

<!-- label: III.6.2.6 -->

The hypercohomology `ℋ^•(f, 𝒦^•)` is a cohomological functor in the category of complexes of `𝒪_X`-modules *bounded
below* `(0_III, 12.4.4)`. It is a cohomological functor in the category of all complexes of `𝒪_X`-modules when the
morphism `f` is quasi-compact and the space underlying `X` is locally noetherian: indeed, it then follows from
`(G, II, 3.10.1)` that `f_*` commutes with inductive limits (the question being local on `Y`), and one may apply
`(0_III, 11.5.2)`.

Finally, if `f` is *separated*, `ℋ^•(f, 𝒦^•)` is a cohomological functor in the category of complexes of quasi-coherent
`𝒪_X`-modules. This is immediate when `Y` is affine, since `X` is then a scheme, and so, by virtue of the canonical
isomorphism `(6.2.2)`, one is reduced to seeing that `𝒦^• ↦ H^•(𝔘, 𝒦^•)` is a cohomological functor in the category of
complexes of quasi-coherent `𝒪_X`-modules, which is immediate since the functor `𝒦^• ↦ C^•(𝔘, 𝒦^•)` is exact in this
category `(I, 1.3.7)`. In the general case, for every affine open `V`

<!-- original page 141 -->

of `Y`, `f⁻¹(V)` is a scheme, and to apply what precedes, it suffices to verify that for an exact sequence
`0 → 𝒦^• → 𝒦'^• → 𝒦''^• → 0` of complexes of quasi-coherent `𝒪_X`-modules, the homomorphism
`∂ : ℋ^n(f, 𝒦''^•)|V → ℋ^{n+1}(f, 𝒦^•)|V` does not depend on the affine open cover `𝔘` of `f⁻¹(V)` used to define it.
But this follows from the fact that, if `𝔘'` is an affine open cover finer than `𝔘`, the diagram

```text
                       ↗  H^•(f⁻¹(V), 𝒦^•)
  H^•(𝔘,  𝒦^•)  ≀
                  ↓
                       ↘
  H^•(𝔘', 𝒦^•)
```

of canonical isomorphisms is commutative, as is the diagram

```text
  H^n(𝔘,  𝒦''^•)   →^∂   H^{n+1}(𝔘,  𝒦^•)
       ↓ ≀                  ↓ ≀
  H^n(𝔘', 𝒦''^•)   →^∂   H^{n+1}(𝔘', 𝒦^•).
```

When one of the preceding conditions is satisfied and `𝒦^• → 𝒦'^•` is a homotopism `(6.1.4)`, the corresponding
isomorphism `ℋ^•(f, 𝒦^•) ⥲ ℋ^•(f, 𝒦'^•)` is then an isomorphism of `∂`-functors `(0_III, 11.4.4)`.

**6.2.7.**

<!-- label: III.6.2.7 -->

All the preceding applies naturally without change (apart from notation) to a complex `𝒦_•` of quasi-coherent
`𝒪_X`-modules whose differential is of degree `−1`; it suffices to consider the complex `𝒦^• = (𝒦^i)` where
`𝒦^i = 𝒦_{−i}` for every `i ∈ ℤ`.

## 6.3. Hypertor of two complexes of modules.

**6.3.1.**

<!-- label: III.6.3.1 -->

Let `A` be a commutative ring and `P_•`, `Q_•` two complexes of `A`-modules whose differentials are of degree `−1`; let
`L_{•,•}` (resp. `M_{•,•}`) be a Cartan–Eilenberg projective resolution of `P_•` (resp. `Q_•`) `(0_III, 11.6.1)`;
`L_{•,•} ⊗_A M_{•,•}` is then (for the sum of the first degrees and the sum of the second degrees) a bicomplex (with
differentials of degree `−1`), whose homology `H_•(L_{•,•} ⊗_A M_{•,•})` does not depend on the chosen Cartan–Eilenberg
resolutions `L_{•,•}`, `M_{•,•}`, and is by definition the *hyperhomology* of the bifunctor `P_• ⊗_A Q_•` in `P_•` and
`Q_•` `(0_III, 11.6.5)`. We shall set by definition

```text
  Tor_n^A(P_•, Q_•) = H_n(L_{•,•} ⊗_A M_{•,•})                                  (6.3.1.1)
```

<!-- original page 142 -->

and we shall say that this `A`-module is the *hypertor of index* `n` of the two complexes `P_•`, `Q_•`. One knows that
in the category of complexes of `A`-modules *bounded below*, the `Tor_n^A(P_•, Q_•)` form a homological bifunctor in
`P_•`, `Q_•` `(0_III, 11.6.5)`. Moreover:

**Proposition (6.3.2).**

<!-- label: III.6.3.2 -->

*The bifunctor `Tor_n^A(P_•, Q_•)` is the common abutment of two spectral bifunctors `'E(P_•, Q_•)`, `''E(P_•, Q_•)`,
whose `E_2` terms are*

```text
  'E_{p,q}^2 = H_p(Tor_q^A(P_•, Q_•))                                           (6.3.2.1)
  ''E_{p,q}^2 = ⊕_{q'+q''=q} Tor_p^A(H_{q'}(P_•), H_{q''}(Q_•))                  (6.3.2.2)
```

*where, in `(6.3.2.1)`, `Tor_q^A(P_•, Q_•)` denotes the bicomplex formed by the `A`-modules `Tor_q^A(P_i, Q_j)`. The
spectral sequence `(6.3.2.2)` is always regular; if `P_•` and `Q_•` are bounded below, or if `A` is of finite
cohomological dimension, the two spectral sequences `(6.3.2.1)` and `(6.3.2.2)` are biregular.*

**Proof.** This follows from `(0_III, 11.6.5)`, since when `A` is of finite cohomological dimension `n`, every
`A`-module admits a projective resolution of length `n` `(M, VI, 2.1)`.

**Corollary (6.3.3).**

<!-- label: III.6.3.3 -->

*Let `P'_•`, `Q'_•` be two complexes of `A`-modules, `u : P_• → P'_•`, `v : Q_• → Q'_•` two homomorphisms of complexes.
If the homomorphisms `H_•(u) : H_•(P_•) → H_•(P'_•)`, `H_•(v) : H_•(Q_•) → H_•(Q'_•)` deduced respectively from `u` and
`v` are bijective, then the homomorphism `Tor_•^A(P_•, Q_•) → Tor_•^A(P'_•, Q'_•)` deduced from `u` and `v` is
bijective.*

**Proof.** Indeed, the homomorphism of spectral sequences `''E(P_•, Q_•) → ''E(P'_•, Q'_•)` deduced from `u` and `v` is
then an isomorphism on the `E_2` terms, and the conclusion follows from the fact that these spectral sequences are
regular by `(6.3.2)` `(0_III, 11.1.5)`.

**Proposition (6.3.4).**

<!-- label: III.6.3.4 -->

*Let `P_•`, `Q_•` be two complexes of `A`-modules, bounded below. Let `L_{•,•}` (resp. `M_{•,•}`) be a bicomplex formed
by flat `A`-modules such that for every `i`, `L_{i,•}` (resp. `M_{i,•}`) is a resolution of `P_i` (resp. `Q_i`). Then
one has canonical isomorphisms*

```text
  Tor_•^A(P_•, Q_•) ⥲ H_•(L_{•,•} ⊗_A Q_•) ⥲ H_•(P_• ⊗_A M_{•,•}) ⥲ H_•(L_{•,•} ⊗_A M_{•,•}).
                                                                                (6.3.4.1)
```

**Proof.** This follows from `(0_III, 11.6.5, (ii) and (iii))` and from the definition of flat `A`-modules.

**Remarks (6.3.5).**

<!-- label: III.6.3.5 -->

*(i)* With the notations of `(6.3.1)`, the bicomplexes `L_{•,•} ⊗_A M_{•,•}` and `M_{•,•} ⊗_A L_{•,•}` are canonically
isomorphic, whence a canonical isomorphism `Tor_•^A(P_•, Q_•) ⥲ Tor_•^A(Q_•, P_•)`.

*(ii)* If `F` and `G` are two `A`-modules, `P_•` and `Q_•` the complexes of `A`-modules reduced to `F` and `G`
respectively in degree `0` and zero in the other degrees, then two projective resolutions `L_•`, `M_•` of `F` and `G`
respectively may be considered as Cartan–Eilenberg resolutions of `P_•` and `Q_•` by completing them by zeros. One has
consequently in this case `Tor_•^A(P_•, Q_•) ⥲ Tor_•^A(F, G)`.

**Proposition (6.3.6).**

<!-- label: III.6.3.6 -->

*Let `(P_•^λ)`, `(Q_•^μ)` be two filtered inductive systems of complexes of `A`-modules; one has a canonical
isomorphism*

```text
  lim_→  Tor_•^A(P_•^λ, Q_•^μ) ⥲ Tor_•^A(lim_→ P_•^λ, lim_→ Q_•^μ).             (6.3.6.1)
        λ,μ                              λ          μ
```

**Proof.** Set `P_• = lim_→ P_•^λ`, `Q_• = lim_→ Q_•^μ`; by functoriality, it is clear that the `Tor_•^A(P_•^λ, Q_•^μ)`
form an inductive system and that the applications `Tor_•^A(P_•^λ, Q_•^μ) → Tor_•^A(P_•, Q_•)` deduced

<!-- original page 143 -->

from the canonical applications `P_•^λ → P_•`, `Q_•^μ → Q_•` form an inductive system of homomorphisms, whence a
canonical homomorphism `(6.3.6.1)`, and more generally a canonical homomorphism
`lim_→ ''E(P_•^λ, Q_•^μ) → ''E(P_•, Q_•)` of which `(6.3.6.1)` is the homomorphism of abutments. In addition, the
spectral sequence `''E(P_•, Q_•)` is regular `(6.3.2)`, and the same holds for the spectral sequence
`lim_→ ''E(P_•^λ, Q_•^μ)`, as follows from the definitions `(0_III, 11.1.7)` and from the proof of `(0_III, 11.3.3)`; to
show that `(6.3.6.1)` is bijective, it therefore suffices `(0_III, 11.1.5)` to prove that the homomorphism

```text
  lim_→ ''E(P_•^λ, Q_•^μ) → ''E(P_•, Q_•)                                       (6.3.6.2)
```

is bijective on the `E_2` terms. Since the functor `H_•` commutes with the inductive limit of complexes of modules, one
is finally reduced to proving that for two filtered inductive systems `(F^λ)`, `(G^μ)` of `A`-modules, the canonical
homomorphism

```text
  lim_→ (Tor_•^A(F^λ, G^μ)) → Tor_•^A(lim_→ F^λ, lim_→ G^μ)
       λ,μ                              λ          μ
```

is bijective. For that, consider for each `F^λ` the *canonical free resolution*

```text
  L_•^λ : ⋯ → L_{i+1}^λ → L_i^λ → ⋯ → L_1^λ → L_0^λ → 0
```

where `L_0^λ` is the `A`-module of formal linear combinations of elements of `F^λ` and `L_{i+1}^λ` is the `A`-module of
formal linear combinations of elements of `Ker(L_i^λ → L_{i−1}^λ)`; one verifies immediately that the `L_•^λ` form an
inductive system of complexes, and if one sets `F = lim_→ F^λ`, `L_i = lim_→ L_i^λ`, the `L_i` form a resolution `L_•`
of `F`, since the functor `lim_→` is exact; in addition, the `L_i`, inductive limits of free `A`-modules, are flat
`(0_I, 6.1.2)`. One considers similarly for each `μ` the canonical free resolution `M_•^μ` of `G^μ`, and
`M_• = lim_→ M_•^μ` is a flat resolution of `G = lim_→ G^μ`. One then has
`Tor_•^A(lim_→ F^λ, lim_→ G^μ) = H_•(L_• ⊗_A M_•)` by virtue of `(6.3.5)` and `(6.3.4)`; but
`H_•(L_• ⊗_A M_•) = lim_→ H_•(L_•^λ ⊗_A M_•^μ)` since `H_•` commutes with inductive limits of complexes of modules;
since `H_•(L_•^λ ⊗_A M_•^μ) = Tor_•^A(F^λ, G^μ)`, this completes the proof.

When one assumes that there exists `i_0` such that `P_i^λ = Q_i^μ = 0` for `i < i_0` for all `λ` and `μ`, one proves in
the same way that the canonical homomorphism

```text
  lim_→ 'E(P_•^λ, Q_•^μ) → 'E(P_•, Q_•)                                         (6.3.6.3)
```

is bijective.

**Proposition (6.3.7).**

<!-- label: III.6.3.7 -->

*Assume `P_•` and `Q_•` bounded below. If the complex `P_•` is formed of flat `A`-modules, one has a canonical
`A`-isomorphism of `∂`-functors in `Q_•`*

```text
  Tor_•^A(P_•, Q_•) ⥲ H_•(P_• ⊗_A Q_•).                                         (6.3.7.1)
```

**Proof.** Indeed, the spectral sequence `(6.3.2.1)` is biregular and degenerate, and the existence of the isomorphism
`(6.3.7.1)` follows from `(0_III, 11.1.6)`. In addition, by computing the hypertor from a Cartan–Eilenberg projective
resolution of `P_•` `(6.3.4)`, one sees at once that the isomorphism so defined is an isomorphism of `∂`-functors in
`Q_•`.

<!-- original page 144 -->

**6.3.8.**

<!-- label: III.6.3.8 -->

Let `ρ : A → A'` be a homomorphism of rings. We propose to define an `A`-homomorphism of degree `0` functorial in `P_•`,
`Q_•`, canonically associated with `ρ`:

```text
  ρ_{P_•, Q_•} : Tor_•^A(P_•, Q_•) → Tor_•^{A'}(P_• ⊗_A A', Q_• ⊗_A A').        (6.3.8.1)
```

For this, consider a Cartan–Eilenberg *projective* resolution `L_{•,•}` of `P_•`; consider on the other hand a
Cartan–Eilenberg *projective* resolution `L'_{•,•}` of `P_• ⊗_A A'`. We shall see that one can define an
`A'`-homomorphism of complexes `L_{•,•} ⊗_A A' → L'_{•,•}`, determined up to homotopy. Indeed, the construction of
`L_{•,•}` is entirely determined when one is given (arbitrarily), for each `i`, a projective resolution
`(X_{ij}^B)_{j ≥ 0}` of `B_i(P_•)` and a projective resolution `(X_{ij}^H)_{j ≥ 0}` of `H_i(P_•)`, which are
respectively equal to `B_i^I(L_{•,•})` and `H_i^I(L_{•,•})`; one deduces successively
`Z_i^I(L_{•,•}) = H_i^I(L_{•,•}) ⊕ B_i^I(L_{•,•})`, then `L_{i,•} = Z_i^I(L_{•,•}) ⊕ B_{i−1}^I(L_{•,•})`. That being so,
`X_{i,•}^B ⊗_A A'` is in general no longer a resolution of `B_i(P_•) ⊗_A A'`, but it is still a complex formed of
*projective* `A'`-modules, and there is therefore an `A'`-homomorphism `X_{i,•}^B ⊗_A A' → B_i^I(L'_{•,•})` compatible
with the augmentations, and determined up to homotopy `(M, V, 1.1)`. One has similarly an `A'`-homomorphism
`X_{i,•}^H ⊗_A A' → H_i^I(L'_{•,•})` determined up to homotopy, from which one deduces, by the construction recalled
above, an `A'`-homomorphism `L_{i,•} ⊗_A A' → L'_{i,•}` for every `i`; these homomorphisms (for `i ∈ ℤ`) are compatible
with the differentials `L_{i,•} → L_{i−1,•}` and the analogous ones for `L'_{i,•}`, by virtue of the same construction,
and they therefore constitute the desired `A'`-homomorphism `L_{•,•} ⊗_A A' → L'_{•,•}`.

To define `(6.3.8.1)`, it then suffices to consider similarly a Cartan–Eilenberg projective resolution `M_{•,•}` (resp.
`M'_{•,•}`) of `Q_•` (resp. `Q_• ⊗_A A'`), and an `A'`-homomorphism `M_{•,•} ⊗_A A' → M'_{•,•}`. From these
homomorphisms one deduces an `A'`-homomorphism `(L_{•,•} ⊗_A A') ⊗_{A'} (M_{•,•} ⊗_A A') → L'_{•,•} ⊗_{A'} M'_{•,•}`,
then by composition an `A`-homomorphism of bicomplexes `L_{•,•} ⊗_A M_{•,•} → L'_{•,•} ⊗_{A'} M'_{•,•}`, and on passing
to homology one obtains `(6.3.8.1)`, which is well defined since it comes from a morphism of complexes defined up to
homotopy.

If `ρ' : A' → A''` is a second homomorphism of rings, and `ρ'' : A → A''` the composite homomorphism `ρ' ∘ ρ`, it is
clear that `ρ''_{P_•, Q_•} = ρ'_{P'_•, Q'_•} ∘ ρ_{P_•, Q_•}`, where `P'_• = P_• ⊗_A A'`, `Q'_• = Q_• ⊗_A A'`.

Note further that the morphism of bicomplexes `L_{•,•} ⊗_A M_{•,•} → L'_{•,•} ⊗_{A'} M'_{•,•}` considered above defines
functorial morphisms (in `P_•` and `Q_•`) of spectral sequences

```text
  'E_{pq}^r(P_•, Q_•) → 'E_{pq}^r(P_• ⊗_A A', Q_• ⊗_A A')
  ''E_{pq}^r(P_•, Q_•) → ''E_{pq}^r(P_• ⊗_A A', Q_• ⊗_A A'),
```

independent of the Cartan–Eilenberg resolutions considered, and having also the preceding transitivity property.

**Proposition (6.3.9).**

<!-- label: III.6.3.9 -->

*Let `ρ : A → A'` be a homomorphism of rings such that `A'` is a flat `A`-module. Then one has functorial canonical
isomorphisms*

```text
  Tor_•^{A'}(P_• ⊗_A A', Q_• ⊗_A A') ⥲ Tor_•^A(P_•, Q_•) ⊗_A A'                 (6.3.9.1)
  'E(P_• ⊗_A A', Q_• ⊗_A A') ⥲ 'E(P_•, Q_•) ⊗_A A'                              (6.3.9.2)
  ''E(P_• ⊗_A A', Q_• ⊗_A A') ⥲ ''E(P_•, Q_•) ⊗_A A'.
```

<!-- original page 145 -->

**Proof.** Indeed, given the exactness of the functor `M ⊗_A A'` in `M`, `L_{•,•} ⊗_A A'` and `M_{•,•} ⊗_A A'` are then
Cartan–Eilenberg projective resolutions of `P_• ⊗_A A'` and `Q_• ⊗_A A'` respectively, whence the conclusion.

**6.3.10.**

<!-- label: III.6.3.10 -->

Let `ρ : A → A'` be a homomorphism of rings; for every complex `P'_•` of `A'`-modules, `P'_{•,[ρ]}` is a complex of
`A`-modules; moreover, the identity application `P'_{•,[ρ]} → P'_•` can be considered as composed of the canonical
applications

```text
  P'_{•,[ρ]} → P'_{•,[ρ]} ⊗_A A' →^μ P'_•,
```

where `μ` is the `A'`-homomorphism `μ(x ⊗ a') = a' x`. If `Q'_•` is a second complex of `A'`-modules, one has therefore
canonical functorial homomorphisms of degree `0`

```text
  Tor_•^A(P'_{•,[ρ]}, Q'_{•,[ρ]}) → Tor_•^{A'}(P'_{•,[ρ]} ⊗_A A', Q'_{•,[ρ]} ⊗_A A')
                                  → Tor_•^{A'}(P'_•, Q'_•)                      (6.3.10.1)
```

where the first arrow is the `A`-homomorphism defined in `(6.3.8)` and the second is deduced from the `A'`-homomorphisms
`P'_{•,[ρ]} ⊗_A A' → P'_•` and `Q'_{•,[ρ]} ⊗_A A' → Q'_•` by functoriality. One has analogous homomorphisms for the
spectral sequences of `(6.3.2)`, and obvious transitivity properties, which we leave to the reader to state.

**Proposition (6.3.11).**

<!-- label: III.6.3.11 -->

*Let `ρ : A → A'` be a homomorphism of rings making `A'` a flat `A`-module. For every complex `P'_•` of `A'`-modules and
every complex `Q_•` of `A`-modules bounded below, one has a functorial canonical isomorphism*

```text
  Tor_•^A(P'_{•,[ρ]}, Q_•) ⥲ Tor_•^{A'}(P'_•, Q_• ⊗_A A').                      (6.3.11.1)
```

**Proof.** Indeed, if `M_{•,•}` is a Cartan–Eilenberg projective resolution of `Q_•`, `M_{•,•} ⊗_A A'` is a
Cartan–Eilenberg projective resolution of `Q_• ⊗_A A'`, and one has, up to a canonical isomorphism,
`P'_{•,[ρ]} ⊗_A M_{•,•} = P'_• ⊗_{A'} (M_{•,•} ⊗_A A')`; the conclusion follows from `(6.3.4)`.

**Remark (6.3.12).**

<!-- label: III.6.3.12 -->

Let `(A^λ)` be a filtered inductive system of rings, and let `(P_•^λ)`, `(Q_•^λ)` be two inductive systems of complexes
of `(A^λ)`-modules; one then has a canonical isomorphism generalizing `(6.3.6.1)`

```text
  lim_→ Tor_•^{A^λ}(P_•^λ, Q_•^λ) ⥲ Tor_•^A(P_•, Q_•)                            (6.3.12.1)
```

where `A = lim_→ A^λ`, `P_• = lim_→ P_•^λ`, `Q_• = lim_→ Q_•^λ`. Once the homomorphisms

```text
  Tor_•^{A^λ}(P_•^λ, Q_•^λ) → Tor_•^{A^μ}(P_•^μ, Q_•^μ)
```

for `λ ≤ μ` are defined, with the help of `(6.3.10)`, the proof is that of `(6.3.6)`.

**Proposition (6.3.13).**

<!-- label: III.6.3.13 -->

*Let `S` be a multiplicative subset of `A`, `P_•` and `Q_•` two complexes of `A`-modules in which the homotheties
defined by the elements of `S` are bijective, so that, if `A' = S⁻¹ A`, `P_•` and `Q_•` are formed of `A'`-modules. Then
one has a canonical isomorphism `Tor_•^A(P_•, Q_•) ⥲ Tor_•^{A'}(P_•, Q_•)`.*

**Proof.** Indeed, the hypothesis implies that the canonical homomorphisms `P_• → P_• ⊗_A A'`, `Q_• → Q_• ⊗_A A'` are
bijective. On the other hand, the functoriality of the hypertor shows that every `s ∈ S` defines a bijective homothety
in `Tor_•^A(P_•, Q_•)`, and consequently

```text
  Tor_•^A(P_•, Q_•) → Tor_•^A(P_•, Q_•) ⊗_A A'
```

<!-- original page 146 -->

is also a bijective homomorphism. Since `A'` is a flat `A`-module, the conclusion follows from `(6.3.9)`, and one has
similarly canonical isomorphisms for the spectral sequences.

## 6.4. Local hypertor functors of complexes of quasi-coherent modules: case of affine schemes.

**6.4.1.**

<!-- label: III.6.4.1 -->

Let `S` be an affine scheme with ring `A`, and `X`, `Y` two affine `S`-schemes with rings `B`, `C` respectively, so that
`B` and `C` are algebras over `A`. Every complex `𝒫_•` (resp. `𝒬_•`) of quasi-coherent `𝒪_X`-modules (resp.
`𝒪_Y`-modules) is of the form `P̃_•` (resp. `Q̃_•`), where `P_•` (resp. `Q_•`) is a complex of `B`-modules (resp.
`C`-modules) `(I, 1.3.7 and 1.3.8)`. One may obviously consider `P_•` and `Q_•` as complexes of `A`-modules and form the
`Tor_n^A(P_•, Q_•)`; furthermore, by virtue of the bifunctorial character of `Tor_n^A(P_•, Q_•)`, the `A`-algebras `B`
and `C` operate on this `A`-module, and these operations make it a `(B, C)`-bimodule, or, equivalently, a module over
`B ⊗_A C = A(X ×_S Y)`. One has thereby defined a quasi-coherent `𝒪_{X×_S Y}`-module

```text
  𝒯or_n^{𝒪_S}(𝒫_•, 𝒬_•) = (Tor_n^A(P_•, Q_•))~                                   (6.4.1.1)
```

which is called the *local hypertor of index* `n` of the complexes `𝒫_•` and `𝒬_•`, and which is also denoted
`𝒯or_n^S(𝒫_•, 𝒬_•)`.

**Lemma (6.4.2).**

<!-- label: III.6.4.2 -->

*With the notations of `(6.4.1)`, suppose that the ring `A` is of the form `R⁻¹ A'`, where `A'` is a ring and `R` a
multiplicative subset of `A'`. Let `S' = Spec(A')`, so that `X` and `Y` may be considered as `S'`-preschemes and one has
`X ×_{S'} Y = X ×_S Y` `(I, 1.6.2 and 3.2.4)`. Then one has `𝒯or_•^{S'}(𝒫_•, 𝒬_•) = 𝒯or_•^S(𝒫_•, 𝒬_•)`.*

**Proof.** This follows from formula `(6.4.1.1)` and from `(6.3.13)`.

**6.4.3.**

<!-- label: III.6.4.3 -->

With the notations and hypotheses of `(6.4.1)`, let `ℱ = F̃` be a quasi-coherent `𝒪_X`-module, `𝒢 = G̃` a quasi-coherent
`𝒪_Y`-module; considering `ℱ` and `𝒢` as complexes of modules, one will denote by `𝒯or_n^S(ℱ, 𝒢)` or `𝒯or_n^{𝒪_S}(ℱ, 𝒢)`
their hypertor of index `n`; it follows from `(6.3.5, (ii))` that one has

```text
  𝒯or_n^{𝒪_S}(ℱ, 𝒢) = (Tor_n^A(F, G))~.                                          (6.4.3.1)
```

Returning now to the general case of two complexes of quasi-coherent modules `𝒫_•`, `𝒬_•`, formulas `(6.4.1.1)` and
`(6.4.3.1)` show, taking into account Prop. `(6.3.2)`, that `𝒯or_•^S(𝒫_•, 𝒬_•)` is the abutment of two spectral
sequences `'ℰ(𝒫_•, 𝒬_•)`, `''ℰ(𝒫_•, 𝒬_•)`, whose `E_2` terms are given by

```text
  'ℰ_{pq}^2 = ℋ_p(𝒯or_q^S(𝒫_•, 𝒬_•))                                            (6.4.3.2)
  ''ℰ_{pq}^2 = ⊕_{q'+q''=q} 𝒯or_p^S(ℋ_{q'}(𝒫_•), ℋ_{q''}(𝒬_•))                   (6.4.3.3)
```

where `𝒯or_q^S(𝒫_•, 𝒬_•)` is the bicomplex of quasi-coherent `𝒪_{X×_S Y}`-modules `𝒯or_q^S(𝒫_i, 𝒬_j)`.

**6.4.4.**

<!-- label: III.6.4.4 -->

Consider now two further affine schemes `X^{(1)} = Spec(B^{(1)})`, `Y^{(1)} = Spec(C^{(1)})`, where `B^{(1)}` and
`C^{(1)}` are `A`-algebras, and suppose given two

<!-- original page 147 -->

`S`-morphisms `u : X^{(1)} → X`, `v : Y^{(1)} → Y`, corresponding to `A`-homomorphisms `φ : B → B^{(1)}`,
`ψ : C → C^{(1)}`. Consider the complexes `u^*(𝒫_•) = (P_• ⊗_B B^{(1)})~` of `𝒪_{X^{(1)}}`-modules,
`v^*(𝒬_•) = (Q_• ⊗_C C^{(1)})~` of `𝒪_{Y^{(1)}}`-modules. The canonical `A`-homomorphisms

```text
  P_• → P_• ⊗_B B^{(1)},   Q_• → Q_• ⊗_C C^{(1)}
```

give by functoriality an `A`-homomorphism

```text
  Tor_•^A(P_•, Q_•) → Tor_•^A(P_• ⊗_B B^{(1)}, Q_• ⊗_C C^{(1)});
```

moreover, again by functoriality, this homomorphism is in fact a homomorphism of `(B ⊗_A C)`-modules. From this one
concludes that one has thereby defined a `(u ×_S v)`-morphism

```text
  θ : 𝒯or_•^S(𝒫_•, 𝒬_•) → 𝒯or_•^S(u^*(𝒫_•), v^*(𝒬_•))                            (6.4.4.1)
```

and consequently, a homomorphism of `𝒪_{X^{(1)} ×_S Y^{(1)}}`-modules

```text
  θ^♯ : (u ×_S v)^*(𝒯or_•^S(𝒫_•, 𝒬_•)) → 𝒯or_•^S(u^*(𝒫_•), v^*(𝒬_•))             (6.4.4.2)
```

which is evidently a morphism of bi-`∂`-functors in the categories of quasi-coherent modules bounded below.

The homomorphism `(6.4.4.2)` is not necessarily bijective; however:

**Lemma (6.4.5).**

<!-- label: III.6.4.5 -->

*With the notations of `(6.4.4)`, suppose that `u` and `v` are open immersions; then the homomorphism `(6.4.4.2)` is
bijective.*

**Proof.** Identify `X^{(1)}` (resp. `Y^{(1)}`) with an open subset of `X` (resp. `Y`); `X^{(1)}` (resp. `Y^{(1)}`) is
then a union of open sets of the form `D(f)` (resp. `D(g)`), where `f ∈ B` (resp. `g ∈ C`), and the induced preschemes
`D(φ(f))` and `D(f)` (resp. `D(ψ(g))` and `D(g)`) are isomorphic. It will suffice to prove the lemma when `X^{(1)}`
(resp. `Y^{(1)}`) is of the form `D(f)` (resp. `D(g)`); indeed, if this point is established, and if one returns to the
general case, it suffices to prove that the restriction of `θ^♯` to each open set `D(f) ×_S D(g)` is an isomorphism;
now, if `u_1 : D(f) → X^{(1)}`, `v_1 : D(g) → Y^{(1)}` are the canonical injections, the preceding restriction is none
other than `(u_1 ×_S v_1)^*(θ^♯)`; but it is immediate, by virtue of definitions `(6.4.4)` and `(0_I, 4.4.8)`, that on
composing it with the canonical homomorphism

```text
  (u_1 ×_S v_1)^*(𝒯or_•^S(u^*(𝒫_•), v^*(𝒬_•))) → 𝒯or_•^S(u'^*(𝒫_•), v'^*(𝒬_•))   (6.4.5.1)
```

where `u' = u ∘ u_1` and `v' = v ∘ v_1`, one obtains the canonical homomorphism

```text
  (u' ×_S v')^*(𝒯or_•^S(𝒫_•, 𝒬_•)) → 𝒯or_•^S(u'^*(𝒫_•), v'^*(𝒬_•))               (6.4.5.2)
```

and if one knows that `(6.4.5.1)` and `(6.4.5.2)` are isomorphisms, it will follow that the same holds for
`(u_1 ×_S v_1)^*(θ^♯)`.

Suppose then that `X^{(1)} = D(f)` and `Y^{(1)} = D(g)`, so that `B^{(1)} = B_f` and `C^{(1)} = C_g`; `u^*(𝒫_•)` (resp.
`v^*(𝒬_•)`) is then identified with `(P_•)~_f` (resp. `(Q_•)~_g`); on the other hand, `X^{(1)} ×_S Y^{(1)}` is
identified with the open subscheme `D(f ⊗ g)` of `X ×_S Y = Spec(B ⊗_A C)` `(II, 4.3.2.4)`; it is a matter of proving
that the homomorphism

```text
  (Tor_•^A(P_•, Q_•))_{f ⊗ g} → Tor_•^A((P_•)_f, (Q_•)_g)                       (6.4.5.3)
```

<!-- original page 148 -->

deduced by functoriality from the canonical homomorphisms `P_• → (P_•)_f`, `Q_• → (Q_•)_g`, is bijective. Now
`(0_I, 1.6.1)`, one may write `(P_•)_f = lim_→ P_•^{(n)}`, where the `P_•^{(n)}` are all complexes of `B`-modules
identical to `P_•`, the application `P_•^{(m)} → P_•^{(n)}` for `m ≤ n` being multiplication by `f^{n−m}`; one has an
analogous result for `Q_•` replacing `f` by `g`; on the other hand, it is clear that the homomorphism

```text
  Tor_•^A(P_•^{(m)}, Q_•^{(m)}) → Tor_•^A(P_•^{(n)}, Q_•^{(n)})
```

corresponding to the homomorphisms `P_•^{(m)} → P_•^{(n)}` and `Q_•^{(m)} → Q_•^{(n)}` is by definition multiplication
by `(f ⊗ g)^{n−m}`. The conclusion follows from `(0_I, 1.6.1)` applied to the first member of `(6.4.5.3)` and from
`(6.3.6)`.

**6.4.6.**

<!-- label: III.6.4.6 -->

With the notations of `(6.4.4)`, one defines similarly canonical homomorphisms of spectral functors

```text
  (u ×_S v)^*('ℰ(𝒫_•, 𝒬_•)) → 'ℰ(u^*(𝒫_•), v^*(𝒬_•))                              (6.4.6.1)
  (u ×_S v)^*(''ℰ(𝒫_•, 𝒬_•)) → ''ℰ(u^*(𝒫_•), v^*(𝒬_•))
```

and the reasoning of `(6.4.5)` shows that when `u` and `v` are *open immersions*, the homomorphisms `(6.4.6.1)` are
bijective: indeed, taking into account `(6.3.6.2)` and `(6.3.6.3)`, it proves that it is an isomorphism on the `E_2`
terms, and `(6.4.5)` shows that it is an isomorphism on the abutments; one concludes therefore with the help of
`(0_III, 11.1.2)` and `(0_III, 11.2.4)`.

## 6.5. Local hypertor functors of complexes of quasi-coherent modules: general case.

**6.5.1.**

<!-- label: III.6.5.1 -->

Consider now an arbitrary prescheme `S` and two arbitrary `S`-preschemes `X`, `Y`; let `𝒫_•` (resp. `𝒬_•`) be a complex
of quasi-coherent `𝒪_X`-modules (resp. `𝒪_Y`-modules). Set `Z = X ×_S Y`; we are going to define quasi-coherent
`𝒪_Z`-modules `𝒯or_n^S(𝒫_•, 𝒬_•)`, called the *local hypertor* of `𝒫_•` and `𝒬_•`, which reduce to those already defined
in `(6.4)` when `S`, `X`, and `Y` are affine.

When `𝒫_•` and `𝒬_•` reduce respectively to their terms of degree `0`, `ℱ` and `𝒢` (the others being zero), one will
write `𝒯or_n^S(ℱ, 𝒢)` instead of `𝒯or_n^S(𝒫_•, 𝒬_•)`.

**6.5.2.**

<!-- label: III.6.5.2 -->

Suppose first that `S` is affine, and let `(X_λ)`, `(Y_μ)` be covers of `X` and `Y` respectively by affine open sets;
then the `Z_{λμ} = X_λ ×_S Y_μ` form an affine open cover of `Z`. Set `𝒫_{λ,•} = 𝒫_•|X_λ`, `𝒬_{μ,•} = 𝒬_•|Y_μ`; we have
therefore for every pair `(λ, μ)` a quasi-coherent `𝒪_{Z_{λμ}}`-module `ℱ_{λμ} = 𝒯or_n^S(𝒫_{λ,•}, 𝒬_{μ,•})`, and it must
be shown that the `ℱ_{λμ}` satisfy the gluing condition `(0_I, 3.3.1)`. For this, it suffices to verify that for every
affine open set `U ⊂ X_λ ∩ X_{λ'}` (resp. `V ⊂ Y_μ ∩ Y_{μ'}`), the restrictions of `ℱ_{λμ}` and `ℱ_{λ'μ'}` to `U ×_S V`
are canonically isomorphic; but this follows at once from the existence of canonical isomorphisms of these restrictions
onto `𝒯or_n^S(𝒫_•|U, 𝒬_•|V)` `(6.4.5)`. Moreover, it follows at once from this definition and from `(6.4.5)` that the
`𝒪_Z`-module so defined does not depend (up to isomorphism) on the open covers `(X_λ)`, `(Y_μ)` considered;

<!-- original page 149 -->

we shall therefore denote it `𝒯or_n^S(𝒫_•, 𝒬_•)`; it follows finally from `(6.4.5)` that for *every* open subset `U`
(resp. `V`) of `X` (resp. `Y`), the restriction of `𝒯or_n^S(𝒫_•, 𝒬_•)` to `U ×_S V` is canonically isomorphic to
`𝒯or_n^S(𝒫_•|U, 𝒬_•|V)`.

**6.5.3.**

<!-- label: III.6.5.3 -->

Passing now to the general case where `S` is arbitrary, let `(S_α)` be a cover of `S` formed of affine open sets; denote
by `X_α` (resp. `Y_α`) the inverse image of `S_α` in `X` (resp. `Y`); it still must be proved that the sheaves
`𝒯or_n^{S_α}(𝒫_•|X_α, 𝒬_•|Y_α) = 𝒢_α` satisfy the gluing condition. It suffices to define, for every affine open set `T`
contained in `S_α ∩ S_β`, canonical isomorphisms of the restrictions of `𝒢_α` and `𝒢_β` to `U ×_S V` (where `U` and `V`
denote the inverse images of `T` in `X` and `Y` respectively) onto `𝒯or_n^T(𝒫_•|U, 𝒬_•|V)`; one may, in addition,
restrict to the case where `T` is written as both `D(f_α)` and `D(f_β)`, `f_α` (resp. `f_β`) being a section of `𝒪_S`
over `S_α` (resp. `S_β`); but then `𝒯or_n^T(𝒫_•|U, 𝒬_•|V)` is canonically isomorphic to `𝒯or_n^{S_α}(𝒫_•|U, 𝒬_•|V)` on
the one hand, and to `𝒯or_n^{S_β}(𝒫_•|U, 𝒬_•|V)` on the other, by virtue of `(6.4.2)`; since one has just defined
canonical isomorphisms of `𝒢_α` onto `𝒯or_n^{S_α}(𝒫_•|U, 𝒬_•|V)` and of `𝒢_β` onto `𝒯or_n^{S_β}(𝒫_•|U, 𝒬_•|V)`
`(6.5.2)`, this completes the definition of the `𝒪_Z`-module `𝒯or_n^S(𝒫_•, 𝒬_•)`. Moreover, for every open subset `U`
(resp. `V`) of `X` (resp. `Y`), `𝒯or_n^S(𝒫_•|U, 𝒬_•|V)` is canonically isomorphic to the restriction of
`𝒯or_n^S(𝒫_•, 𝒬_•)` to `U ×_S V`.

It is immediate that one has thereby defined (in the categories of complexes of quasi-coherent modules bounded below) a
bi-`∂`-functor `𝒯or_•^S(𝒫_•, 𝒬_•)` with values in the category of `𝒪_Z`-modules, for it is clear that the question is
local on `X`, `Y`, and `S`, by virtue of `(6.4.5)` and of the remark that `(6.4.4.2)` is a morphism of bi-`∂`-functors.
Note that if `𝒫_•` and `𝒬_•` are reduced respectively to their terms of degree `0`, `ℱ` and `𝒢`, `𝒯or_0^S(ℱ, 𝒢)` is none
other, by virtue of `(6.4.1.1)`, than the external tensor product `ℱ ⊗_S 𝒢` defined in `(I, 9.1.2)`; this follows indeed
from `(I, 9.1.3)`.

**6.5.4.**

<!-- label: III.6.5.4 -->

It follows from the preceding construction and from the remarks made in `(6.4.6)` that `𝒯or_•^S(𝒫_•, 𝒬_•)` is the
abutment of two spectral functors `'ℰ(𝒫_•, 𝒬_•)`, `''ℰ(𝒫_•, 𝒬_•)`, with `E_2` terms equal to

```text
  'ℰ_{pq}^2 = ℋ_p(𝒯or_q^S(𝒫_•, 𝒬_•))                                            (6.5.4.1)
  ''ℰ_{pq}^2 = ⊕_{q'+q''=q} 𝒯or_p^S(ℋ_{q'}(𝒫_•), ℋ_{q''}(𝒬_•)).                  (6.5.4.2)
```

The spectral sequence `(6.5.4.2)` is always regular; the two spectral sequences are biregular if `𝒫_•` and `𝒬_•` are
bounded below. Another case where the two preceding sequences are biregular is the following:

**6.5.5.**

<!-- label: III.6.5.5 -->

We shall say that on a topological space `T` a sheaf of rings `𝒜` is *of cohomological dimension `≤ n`* if, for every
`t ∈ T`, the ring `𝒜_t` is of cohomological dimension `≤ n`; one then also says that the *ringed space* `(T, 𝒜)` is *of
cohomological dimension `≤ n`*. One says that a sheaf of rings (resp. a ringed space) is of *finite* cohomological
dimension if there exists an integer `n` such that it is of cohomological dimension `≤ n`. Note that if the `𝒜_t` are
*noetherian (commutative) local* rings,

<!-- original page 150 -->

to say that they are of cohomological dimension `≤ n` means that they are *regular* and of (Krull) dimension `≤ n`
`(0_IV, 17.3.1)`. With the terminology of dimension theory that we shall introduce in chap. IV, it is equivalent to say
that a locally noetherian prescheme `T` is of cohomological dimension `≤ n`, or to say that it is *regular*
`(0_I, 4.1.4)` and of dimension `≤ n`; this means that for every affine open `U` of `T`, the ring `Γ(U, 𝒪_T)` is of
cohomological dimension `≤ n` `(0_IV, 17.2.6)`. That being so, this last remark, joined to `(6.3.2)`, proves that *if
`S` is locally noetherian and of finite cohomological dimension, the spectral sequences `'ℰ(𝒫_•, 𝒬_•)` and
`''ℰ(𝒫_•, 𝒬_•)` are biregular.*

It is clear that `𝒯or_•^S(𝒫_•, 𝒬_•)` is transformed into `𝒯or_•^S(𝒬_•, 𝒫_•)` (up to isomorphism) by the canonical
isomorphism of `X ×_S Y` onto `Y ×_S X`.

**Proposition (6.5.6).**

<!-- label: III.6.5.6 -->

*Let `(𝒫_{α,•})` be a filtered inductive system of complexes of quasi-coherent `𝒪_X`-modules; then there exists a
canonical isomorphism*

```text
  lim_→ (𝒯or_•^S(𝒫_{α,•}, 𝒬_•)) ⥲ 𝒯or_•^S(lim_→ 𝒫_{α,•}, 𝒬_•).                   (6.5.6.1)
```

**Proof.** The question being local on `S`, `X`, and `Y`, one may suppose `S`, `X`, `Y` affine, and the proposition then
reduces to `(6.3.6)`.

**Remarks (6.5.7).**

<!-- label: III.6.5.7 -->

*(i)* Consider in particular the case where `S = X = Y`, `𝒫_•` and `𝒬_•` being thus two complexes of quasi-coherent
`𝒪_S`-modules; then the `𝒯or_n^S(𝒫_•, 𝒬_•)` are quasi-coherent `𝒪_S`-modules; moreover, for every point `z ∈ S`, it
follows from `(6.5.6)` that one has a canonical isomorphism

```text
  (𝒯or_n^S(𝒫_•, 𝒬_•))_z ⥲ Tor_n^{𝒪_z}((𝒫_•)_z, (𝒬_•)_z)                          (6.5.7.1)
```

since the question is local and one is reduced to the case of modules, by virtue of `(6.4.1.1)`.

*(ii)* One may generalize the definition of hypertor to the case of two complexes of `𝒪_X`-modules `𝒫_•`, `𝒬_•` on the
same ringed space `(X, 𝒪_X)`; for every open subset `U` of `X`, set indeed `A(U) = Γ(U, 𝒪_X)`, `P_•(U) = Γ(U, 𝒫_•)`,
`Q_•(U) = Γ(U, 𝒬_•)`; the `A(U)`-modules `Tor_n^{A(U)}(P_•(U), Q_•(U))` then form a *presheaf* on `X`, and one denotes
by `𝒯or_n^X(𝒫_•, 𝒬_•)` the `𝒪_X`-module associated with this presheaf. When `X` is a prescheme, it follows from
`(6.3.12)` that this `𝒪_X`-module is canonically isomorphic to the hypertor defined above. We shall not develop this
generalization further.

**Proposition (6.5.8).**

<!-- label: III.6.5.8 -->

*Let `X`, `Y` be two `S`-preschemes, `ℱ` (resp. `𝒢`) a quasi-coherent `𝒪_X`-module (resp. `𝒪_Y`-module). If `ℱ` or `𝒢`
is `S`-flat, one has `𝒯or_n^S(ℱ, 𝒢) = 0` for `n ≠ 0`.*

**Proof.** The question being local on `X` and `Y`, one may suppose `X`, `Y`, `S` affine, with respective rings `B`,
`C`, `A`, and `ℱ = M̃`, `𝒢 = Ñ`, `M` (resp. `N`) being a `B`-module (resp. `C`-module). Suppose for example that `ℱ` is
`S`-flat, which means that for every `s ∈ S`, `M_s` is a flat `A_s`-module `(0_I, 6.7.1)`; consequently `M` is a flat
`A`-module `(0_I, 6.3.3)`, and one knows that `Tor_n^A(M, N) = 0` for `n > 0` and for every `C`-module `N`
`(0_I, 6.1.1)`, whence

<!-- original page 151 -->

the conclusion by `(6.4.1.1)`.

**Corollary (6.5.9).**

<!-- label: III.6.5.9 -->

*Let `X`, `Y` be two `S`-preschemes, `𝒫_•` (resp. `𝒬_•`) a complex of quasi-coherent `𝒪_X`-modules (resp. `𝒪_Y`-modules)
bounded below. Suppose that all the `𝒫_i` are `S`-flat. Then there exists a canonical isomorphism of `∂`-functors in
`𝒬_•`*

```text
  𝒯or_•^S(𝒫_•, 𝒬_•) ⥲ ℋ_•(𝒫_• ⊗_S 𝒬_•).                                         (6.5.9.1)
```

**Proof.** This is none other than `(6.3.7)` when `S`, `X`, `Y` are affine; one passes from there to the general case by
the reasoning of `(6.5.2)` and `(6.5.3)`.

**Corollary (6.5.10).**

<!-- label: III.6.5.10 -->

*Suppose that `X` is flat over `S` `(0_I, 6.7.1)`, that `𝒫_•` and `𝒬_•` are bounded below, and that all the `𝒫_i` are
locally free `𝒪_X`-modules (not necessarily of finite type). Then the homomorphism `(6.5.9.1)` is bijective.*

**Proof.** Indeed, the hypothesis of `(6.5.9)` is satisfied, since flatness is a pointwise property on `X` by definition
and every direct sum of flat modules is a flat module `(0_I, 6.1.2)`.

**Proposition (6.5.11).**

<!-- label: III.6.5.11 -->

*Let `X'`, `Y'` be two `S`-preschemes, `f : X → X'`, `g : Y → Y'` two affine `S`-morphisms. Let `𝒫_•` (resp. `𝒬_•`) be a
complex of quasi-coherent `𝒪_X`-modules (resp. `𝒪_Y`-modules); one then has a functorial canonical isomorphism*

```text
  (f ×_S g)_*(𝒯or_•^S(𝒫_•, 𝒬_•)) ⥲ 𝒯or_•^S(f_*(𝒫_•), g_*(𝒬_•)).                  (6.5.11.1)
```

**Proof.** Since `f` and `g` are affine, `f_*(𝒫_•)` and `g_*(𝒬_•)` are complexes of quasi-coherent modules
`(II, 1.2.6)`, and if one sets `Z' = X' ×_S Y'`, the two members of `(6.5.11.1)` are quasi-coherent `𝒪_{Z'}`-modules
`(6.5.1)`; one reduces easily to the case where `S`, `X'`, and `Y'` are affine; but then it is also the case for `X` and
`Y` by hypothesis, and the verification follows at once from `(6.4.1.1)` and `(I, 1.6.3)`.

**Remark (6.5.12).**

<!-- label: III.6.5.12 -->

Let `X'`, `Y'` be two `S`-preschemes and suppose that `X'` is `S`-flat; let `X` be a closed subprescheme of `X'`,
`i : X → X'` the canonical injection, `𝒫_•` (resp. `𝒬_•`) a complex of `𝒪_X`-modules (resp. `𝒪_{Y'}`-modules)
quasi-coherent, bounded below. Let finally `ℒ'_{•,•}` be a resolution of `i_*(𝒫_•)` formed of locally free
`𝒪_{X'}`-modules, such that every point of `X'` has an affine open neighborhood `U` for which `ℒ'_{•,•}|U` is a free
resolution of `i_*(𝒫_j)|U` for every `j`. One then has a canonical isomorphism

```text
  (i ×_S 1)_*(𝒯or_•^S(𝒫_•, 𝒬_•)) ⥲ ℋ_•(ℒ'_{•,•} ⊗_S 𝒬_•).                         (6.5.12.1)
```

**Proof.** If `S`, `X'`, `Y'` are affine and if `ℒ'_{j,•}` is a free resolution of `i_*(𝒫_j)` for every `j`, one is
reduced, by virtue of `(6.5.11)`, to the case where `X' = X` is `S`-flat, and it suffices to apply `(6.3.4)`. In the
general case, one defines the isomorphism `(6.5.12.1)` locally, and it remains to verify that this definition does give
a global isomorphism. For this, one must refer to the definition of the first isomorphism `(6.3.4.1)`, which comes from
an isomorphism of spectral sequences `(0_III, 11.6.5 and 11.5.3)`, obtained itself from a morphism of bicomplexes
`L_{•,•} → L'_{•,•}`, where `L_{•,•}` is the given resolution of `P_•`, `L'_{•,•}` a projective resolution of `P_•` in
the category of complexes of `A`-modules bounded below

<!-- original page 152 -->

(cf. `(0_III, 11.5.2.2)`); our assertion follows from the fact that the isomorphism `(6.3.4.1)` does not depend on the
chosen projective resolution `L'_{•,•}`, by virtue of the existence of a homotopism between two such resolutions
`(M, V, 1.2)`.

**Proposition (6.5.13).**

<!-- label: III.6.5.13 -->

*Let `X`, `Y` be two `S`-preschemes, and suppose verified one of the following conditions:*

*(i)* `X` *and* `Z = X ×_S Y` *are locally noetherian and* `X` *is flat over* `S`.

*(ii)* `S` *and* `X` *are locally noetherian and* `Y` *is of finite type over* `S`.

*Let `𝒫_•` (resp. `𝒬_•`) be a complex of quasi-coherent `𝒪_X`-modules (resp. `𝒪_Y`-modules), bounded below. Suppose in
addition that, for every `n`, `ℋ_n(𝒫_•)` (resp. `ℋ_n(𝒬_•)`) is a `𝒪_X`-module (resp. `𝒪_Y`-module) of finite type. Then
the `𝒯or_n^S(𝒫_•, 𝒬_•)` are coherent `𝒪_Z`-modules.*

**Proof.** Since `𝒫_•` and `𝒬_•` are bounded below, the spectral sequence `''ℰ(𝒫_•, 𝒬_•)` is biregular `(6.5.4)`, and by
virtue of `(0_III, 11.1.8)`, it suffices (since in the two cases (i), (ii), `Z` is locally noetherian) to prove that the
terms `''ℰ_{pq}^2` are coherent. The hypothesis on the `ℋ_n(𝒫_•)` and `ℋ_n(𝒬_•)` and the expression `(6.5.4.2)` of the
`''ℰ_{pq}^2` therefore show that the proposition is equivalent to its particular case corresponding to `𝒫_•` and `𝒬_•`
reduced to their terms of degree `0`, in other words to its

**Corollary (6.5.14).**

<!-- label: III.6.5.14 -->

*Suppose verified one of the conditions (i), (ii) of `(6.5.13)`, and let `ℱ` (resp. `𝒢`) be a quasi-coherent
`𝒪_X`-module (resp. `𝒪_Y`-module) of finite type; then the `𝒯or_n^S(ℱ, 𝒢)` are coherent `𝒪_Z`-modules.*

**Proof.** The question being local on `X` and `Y`, one may suppose `S`, `X`, `Y` affine.

*(i)* Under the hypotheses of (i), `S`, `X`, and `Z` are noetherian. There therefore exists a locally free resolution
`ℒ_•` of `ℱ` formed of `𝒪_X`-modules of finite type `(I, 1.3.7)`; since `X` is flat over `S`, it follows from `(6.3.4)`
that one has `𝒯or_•^S(ℱ, 𝒢) = ℋ_•(ℒ_• ⊗_S 𝒢)`; now, the `ℒ_i ⊗_S 𝒢` are quasi-coherent `𝒪_Z`-modules of finite type
`(I, 9.1.1)`, hence coherent. One concludes that `ℋ_•(ℒ_• ⊗_S 𝒢)` is coherent `(0_I, 5.3.4)`.

*(ii)* Suppose now that the conditions (ii) are verified. Since the ring `A(Y)` is a quotient of an `A(S)`-algebra of
polynomials in a finite number of indeterminates `(I, 6.3.3)`, `Y` is a closed sub-`S`-prescheme of an affine
`S`-prescheme `Y'`, flat and of finite type over `S`; `Y'` being noetherian `(I, 6.3.7)`, there exists a locally free
resolution `ℳ_•` of `j_*(𝒢)` by `𝒪_{Y'}`-modules of finite type (`j : Y → Y'` being the canonical injection); by virtue
of `(6.5.12)`, `𝒯or_•^S(ℱ, 𝒢)` is the inverse image, by `1 × j`, of the `𝒪_{Z'}`-module `ℋ_•(ℱ ⊗_S ℳ_•)` (where
`Z' = X ×_S Y'`); one sees as in (i) that the `ℱ ⊗_S ℳ_i` are coherent `𝒪_{Z'}`-modules, and one again draws the
conclusion from `(0_I, 5.3.4)`.

**6.5.15.**

<!-- label: III.6.5.15 -->

The theory developed above for two complexes `𝒫_•`, `𝒬_•` of quasi-coherent sheaves on two `S`-preschemes `X`, `Y`
generalizes without difficulty to the case where one considers an arbitrary finite number of `S`-preschemes `X^{(i)}`
(`1 ≤ i ≤ m`) and on each `X^{(i)}` a complex `𝒫_•^{(i)}` of quasi-coherent `𝒪_{X^{(i)}}`-modules; if
`Z = X^{(1)} ×_S X^{(2)} ×_S ⋯ ×_S X^{(m)}`, one defines in this way a quasi-coherent `𝒪_Z`-module
`𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)}, …, 𝒫_•^{(m)})`. We leave to the reader the task of developing the theory in this general
case, and we restrict ourselves to writing, for later reference, the `E_2` term of the second (regular) spectral
sequence whose abutment is `𝒯or_•^S(𝒫_•^{(1)}, 𝒫_•^{(2)}, …, 𝒫_•^{(m)})`:

<!-- original page 153 -->

```text
  ''ℰ_{pq}^2 = ⊕_{q_1 + q_2 + ⋯ + q_m = q}
                 𝒯or_p^S(ℋ_{q_1}(𝒫_•^{(1)}), …, ℋ_{q_m}(𝒫_•^{(m)})).             (6.5.15.1)
```

We shall study in `(6.8)` the associativity spectral sequences to which these hypertor functors of an arbitrary number
of complexes give rise.

## 6.6. Global hypertor functors of complexes of quasi-coherent modules and Künneth spectral sequences: case of an affine base.

**6.6.1.**

<!-- label: III.6.6.1 -->

Consider an affine scheme `S = Spec(A)` and two quasi-compact `S`-schemes `X^{(i)}` (`i = 1, 2`); let `𝒫_•^{(i)}` be a
complex of quasi-coherent `𝒪_{X^{(i)}}`-modules, *bounded below*, whose differential is of degree `−1` (`i = 1, 2`).
Consider on the other hand a *finite* cover `𝔘^{(i)} = (U_α^{(i)})` of `X^{(i)}` by affine open sets; let
`X = X^{(1)} ×_S X^{(2)}`, which is a quasi-compact `S`-scheme `(I, 5.5.1 and 6.6.4)`, and let `𝔘 = 𝔘^{(1)} ×_S 𝔘^{(2)}`
be the cover of `X` formed of the affine open sets `U_α^{(1)} ×_S U_β^{(2)}`. For every pair of integers `p ≤ 0`,
`q ∈ ℤ`, the group of `(−p)`-alternating cochains `C^{−p}(𝔘^{(i)}, 𝒫_q^{(i)})` of the cover `𝔘^{(i)}` with coefficients
in the sheaf `𝒫_q^{(i)}` `(G, II, 5.1)` is an `A`-module; for `p > 0`, one will set `C^p(𝔘^{(i)}, 𝒫_q^{(i)}) = 0`; one
has thereby defined a bicomplex `C^•(𝔘^{(i)}, 𝒫_•^{(i)})` of `A`-modules, whose *two* differentials are of degree `−1`.
It follows from definitions `(0_III, 12.1.2)` that the homology `A`-module `H_n(C^•(𝔘^{(i)}, 𝒫_•^{(i)}))` of this
bicomplex (considered as usual as a simple complex for the total degree) is none other than the *hypercohomology
`A`-module* `H^{−n}(𝔘^{(i)}, 𝒫^{(i)•})`, where `𝒫^{(i)•}` is the complex with differential of degree `+1` obtained by
taking `𝒫_q^{(i)}` as the component of degree `q`; by abuse of notation, we shall write it `H^{−n}(𝔘^{(i)}, 𝒫_•^{(i)})`.
It then follows from `(6.2.2)` that this `A`-module is canonically isomorphic to the hypercohomology `A`-module
`H^{−n}(X^{(i)}, 𝒫^{(i)•})`, which we shall similarly write `H^{−n}(X^{(i)}, 𝒫_•^{(i)})`; it therefore does not depend
on the chosen finite cover `𝔘^{(i)}`.

**6.6.2.**

<!-- label: III.6.6.2 -->

We shall apply to the two bicomplexes of `A`-modules

```text
  L_{•,•}^{(i)} = C^•(𝔘^{(i)}, 𝒫_•^{(i)})                            (i = 1, 2)
```

and to the covariant bifunctor `L_{•,•}^{(1)} ⊗_A L_{•,•}^{(2)}` in these two bicomplexes, the general theory of
hyperhomology of functors with respect to bicomplexes `(0_III, 11.7.4)`. Since the cochains considered are *alternating*
and the covers `𝔘^{(i)}` finite, one will note that the modules `C^{−p}(𝔘^{(i)}, 𝒫_q^{(i)})` are `≠ 0` only for a
*finite* number (independent of `q`) of values of `p`, and in particular the two degrees of each of the `L_{•,•}^{(i)}`
are *bounded below*. We shall denote by `Tor_n^A(L_{•,•}^{(1)}, L_{•,•}^{(2)})` or
`Tor_n^S(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})` the `n`-th hyperhomology module of `L_{•,•}^{(1)} ⊗_A L_{•,•}^{(2)}`,
which we shall call the *hypertor of index `n`* of `𝒫_•^{(1)}` and `𝒫_•^{(2)}`, *relative to the covers* `𝔘^{(1)}` *and*
`𝔘^{(2)}`. When `𝒫_•^{(1)}` and `𝒫_•^{(2)}` are reduced to their terms of degree `0`, `ℱ^{(1)}` and `ℱ^{(2)}`, one
writes `Tor_n^S(𝔘^{(1)}, 𝔘^{(2)}; ℱ^{(1)}, ℱ^{(2)})` for their hypertor. One will denote by
`𝒯or_n^S(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})`, following the general conventions, the *bicomplex* whose component of
indices `(j, k)` is `Tor_n^S(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_j^{(1)}, 𝒫_k^{(2)})`.

Since `L_{•,•}^{(i)}` is an exact functor in `𝒫_•^{(i)}`, since the intersections of the sets

<!-- original page 154 -->

of `𝔘^{(i)}` are affine `(I, 5.5.6 and 1.3.11)`, `Tor_n^S(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})` is a covariant
bi-`∂`-functor in `𝒫_•^{(1)}`, `𝒫_•^{(2)}`, with values in the category of `A`-modules `(0_III, 11.7.3)`. Moreover, one
knows `(0_III, 11.7.2)` that this bifunctor is the common abutment of *six* biregular spectral functors, which we shall
denote by `^{(t)}E(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})` or `^{(t)}E(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})`, where
`t` must be replaced by one of the letters `a`, `b`, `a'`, `b'`, `c`, `d`, and whose `E_2` terms are the following:

```text
  ^{(a)}E_{pq}^2  = ⊕_{q_1 + q_2 = q} Tor_p^A(H_{q_1}(L_{•,•}^{(1)}), H_{q_2}(L_{•,•}^{(2)}))
  ^{(b)}E_{pq}^2  = H_p(Tor_q^{A, II}(L_{•,•}^{(1)}, L_{•,•}^{(2)}))
  ^{(a')}E_{pq}^2 = ⊕_{q_1 + q_2 = q} Tor_p^A(H_{q_1}^I(L_{•,•}^{(1)}), H_{q_2}^I(L_{•,•}^{(2)}))
  ^{(b')}E_{pq}^2 = H_p(Tor_q^A(L_{•,•}^{(1)}, L_{•,•}^{(2)}))
  ^{(c)}E_{pq}^2  = ⊕_{q_1 + q_2 = q} Tor_p^A(H_{q_1}^{II}(L_{•,•}^{(1)}), H_{q_2}^{II}(L_{•,•}^{(2)}))
  ^{(d)}E_{pq}^2  = H_p(Tor_q^{A, I}(L_{•,•}^{(1)}, L_{•,•}^{(2)})),
```

where the notations conform to those of the general theory of hyperhomology. In what follows, we shall make these
initial terms more explicit.

**6.6.3. Spectral sequences (a) and (a').**

<!-- label: III.6.6.3 -->

We have seen in `(6.6.1)` that the homology module `H_n(L_{•,•}^{(i)})` of the bicomplex `L_{•,•}^{(i)}` was equal to
`H^{−n}(X^{(i)}, 𝒫_•^{(i)})`; so

```text
  ^{(a)}E_{pq}^2 = ⊕_{q_1 + q_2 = q} Tor_p^A(H^{−q_1}(X^{(1)}, 𝒫_•^{(1)}), H^{−q_2}(X^{(2)}, 𝒫_•^{(2)})).
```

By definition, the complex `H_n^I(L_{•,•}^{(i)})` has as term of degree `k` the homology module
`H_n(C^•(𝔘^{(i)}, 𝒫_k^{(i)}))`, that is, by definition, the cohomology module `H^{−n}(𝔘^{(i)}, 𝒫_k^{(i)})`; one knows
`(1.4.1)` that this module is canonically isomorphic to `H^{−n}(X^{(i)}, 𝒫_k^{(i)})`; so

```text
  ^{(a')}E_{pq}^2 = ⊕_{q_1 + q_2 = q} Tor_p^A(H^{−q_1}(X^{(1)}, 𝒫_•^{(1)}), H^{−q_2}(X^{(2)}, 𝒫_•^{(2)})).
```

**6.6.4. Spectral sequences (b) and (b').**

<!-- label: III.6.6.4 -->

By definition, `Tor_q^{A, II}(L_{•,•}^{(1)}, L_{•,•}^{(2)})` is a bicomplex whose term of degree `(h, k)` is the
`A`-module

```text
  Tor_q^A(C^{−h}(𝔘^{(1)}, 𝒫_•^{(1)}), C^{−k}(𝔘^{(2)}, 𝒫_•^{(2)})).
```

Let `Φ^{(i)}` be the index set of `𝔘^{(i)}`; by definition, the complex of modules `C^r(𝔘^{(i)}, 𝒫_•^{(i)})` (`r ≥ 0`)
is a direct sum of the complexes `Γ(U_ρ^{(i)}, 𝒫_•^{(i)})`, where `U_ρ^{(i)}` is the intersection of the `U_ξ^{(i)}` for
`ξ ∈ ρ`, and `ρ` ranges over `𝔓(Φ^{(i)})`; so the `A`-module

```text
  Tor_q^A(C^{−h}(𝔘^{(1)}, 𝒫_•^{(1)}), C^{−k}(𝔘^{(2)}, 𝒫_•^{(2)}))
```

is the direct sum of the `A`-modules `Tor_q^A(Γ(U_σ^{(1)}, 𝒫_•^{(1)}), Γ(U_τ^{(2)}, 𝒫_•^{(2)}))`, where `σ` (resp. `τ`)
ranges over the elements of `𝔓(Φ^{(1)})` (resp. `𝔓(Φ^{(2)})`) such that `Card(σ) = −(h+1)` (resp. `Card(τ) = −(k+1)`).
Since `X^{(1)}` and `X^{(2)}` are schemes, the `U_ρ^{(i)}` are affine, so by `(6.4.1.1)` one has

```text
  Tor_q^A(Γ(U_σ^{(1)}, 𝒫_•^{(1)}), Γ(U_τ^{(2)}, 𝒫_•^{(2)})) = Γ(U_σ^{(1)} ×_S U_τ^{(2)}, 𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)})).
```

<!-- original page 155 -->

One sees therefore that `^{(b)}E_{pq}^2` is the `(−p)`-th cohomology module of the complex `L^•(Φ^{(1)}, Φ^{(2)}; 𝒮)` of
*bi-alternating* cochains on `Φ^{(1)}` and `Φ^{(2)}` with values in the system of coefficients

```text
  𝒮 : (σ, τ) ↦ Γ(U_σ^{(1)} ×_S U_τ^{(2)}, 𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)}))
```

`(0_III, 11.8.4)`. One knows then `(0_III, 11.8.5 and 11.8.6)` that the cohomology of this complex is the same as that
of the complex `C^•(Φ^{(1)}, Φ^{(2)}; 𝒮)` of *all* cochains on `Φ^{(1)}` and `Φ^{(2)}` with values in `𝒮`, and also the
same as that of the complex `P^•(Φ^{(1)}, Φ^{(2)}; 𝒮)`, whose elements are linear combinations of the

```text
  λ(σ, τ) ∈ Γ(U_σ^{(1)} ×_S U_τ^{(2)}, 𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)}))
```

where `σ = (α_0, …, α_h)` and `τ = (β_0, …, β_h)` are sequences having the same number of elements. But one has then
`U_σ^{(1)} ×_S U_τ^{(2)} = (U_{α_0}^{(1)} ×_S U_{β_0}^{(2)}) ∩ ⋯ ∩ (U_{α_h}^{(1)} ×_S U_{β_h}^{(2)})` `(I, 3.2.7)`. If
one denotes by `𝔘` the cover of `Z = X^{(1)} ×_S X^{(2)}` by the affine open sets `U_α^{(1)} ×_S U_β^{(2)}`, one sees
finally, taking into account that `X^{(1)} ×_S X^{(2)}` is a *scheme*, that one has, by virtue of `(1.3.1)`,

```text
  ^{(b)}E_{pq}^2 = H^{−p}(X^{(1)} ×_S X^{(2)}, 𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)})).
```

In second place, `Tor_q^A(L_{•,•}^{(1)}, L_{•,•}^{(2)})` is a bicomplex whose term of degree `(h, k)` is the direct sum
of the `A`-modules

```text
  Tor_q^A(C^{−h_1}(𝔘^{(1)}, 𝒫_{k_1}^{(1)}), C^{−h_2}(𝔘^{(2)}, 𝒫_{k_2}^{(2)}))
```

such that `h_1 + h_2 = h` and `k_1 + k_2 = k`; making the modules `C^r(𝔘^{(i)}, 𝒫_j^{(i)})` explicit as above, one sees
again that this term is the direct sum of the `A`-modules

```text
  Γ(U_σ^{(1)} ×_S U_τ^{(2)}, 𝒯or_q^S(𝒫_{k_1}^{(1)}, 𝒫_{k_2}^{(2)}))
```

where `k_1 + k_2 = k`, and `σ` (resp. `τ`) ranges over the elements of `𝔓(Φ^{(1)})` (resp. `𝔓(Φ^{(2)})`) such that
`Card(σ) + Card(τ) = −h − 2`. The term `^{(b')}E_{pq}^2` that we are computing is the `(−p)`-th cohomology module of a
bicomplex `N^{••} = (N^{j,k})`, where the simple complex `N^{•,k}` is the complex of bi-alternating cochains on
`Φ^{(1)}` and `Φ^{(2)}`, with values in the system of coefficients

```text
  𝒮_k : (σ, τ) ↦ Γ(U_σ^{(1)} ×_S U_τ^{(2)}, ⊕_{k_1 + k_2 = k} 𝒯or_q^S(𝒫_{k_1}^{(1)}, 𝒫_{k_2}^{(2)})),
```

these systems of coefficients forming a complex `𝒮^•`, where the differential comes from that of the simple complex
associated to the bicomplex `𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)})`. One knows that the cohomology of `N^{••}` is the same as
that of the bicomplex `C^•(Φ^{(1)}, Φ^{(2)}; 𝒮^•)` `(0_III, 11.8.9)`, and also the same as that of the bicomplex
`P^•(Φ^{(1)}, Φ^{(2)}; 𝒮^•)`, whose elements of degree `(h, k)` are the linear combinations of

```text
  λ(σ, τ) ∈ Γ(U_σ^{(1)} ×_S U_τ^{(2)}, ⊕_{k_1 + k_2 = k} 𝒯or_q^S(𝒫_{k_1}^{(1)}, 𝒫_{k_2}^{(2)}))
```

`σ = (α_0, …, α_h)`, `τ = (β_0, …, β_h)` being sequences having the *same number of elements* `(0_III, 11.8.10)`. One
sees then as above that `^{(b')}E_{pq}^2` is the `(−p)`-th cohomology module of the bicomplex `C^•(𝔘, 𝒬^•)`, where `𝒬^•`
is the simple complex associated to the bicomplex `𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)})` of `𝒪_Z`-modules. With the conventions
made in `(6.6.1)`, one therefore has

```text
  ^{(b')}E_{pq}^2 = H^{−p}(X^{(1)} ×_S X^{(2)}, 𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)})).
```

<!-- original page 156 -->

**6.6.5. Spectral sequences (c) and (d).**

<!-- label: III.6.6.5 -->

By definition, the complex `H_n^{II}(L_{•,•}^{(i)})` has as term of degree `h` the `A`-module
`C^{−h}(𝔘^{(i)}, ℋ_n(𝒫_•^{(i)}))`, by virtue of the exactness of the functor `C^{−h}`. One has therefore, by definition
of the hypertor of two modules relative to two covers `(6.6.2)`,

```text
  ^{(c)}E_{pq}^2 = ⊕_{q_1 + q_2 = q} Tor_p^S(𝔘^{(1)}, 𝔘^{(2)}; ℋ_{q_1}(𝒫_•^{(1)}), ℋ_{q_2}(𝒫_•^{(2)})).
```

Finally, by definition, `Tor_q^{A, I}(L_{•,•}^{(1)}, L_{•,•}^{(2)})` is a bicomplex whose term of degree `(h, k)` is the
`A`-module `Tor_q^S(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_h^{(1)}, 𝒫_k^{(2)})`. One therefore has

```text
  ^{(d)}E_{pq}^2 = H_p(Tor_q^S(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})).
```

**6.6.6.**

<!-- label: III.6.6.6 -->

The theory of hyperhomology of functors of bicomplexes `(0_III, 11.7.3)` shows, as in `(6.3.4)`, that, for every
Cartan–Eilenberg flat resolution `M_{•,•,•}^{(i)}` of `L_{•,•}^{(i)}` (in the category of complexes of modules bounded
below) (`i = 1, 2`), one has canonical isomorphisms of bi-`∂`-functors

```text
  Tor_•^S(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})
        ⥲ H_•(M_{•,•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)})
        ⥲ H_•(M_{•,•,•}^{(1)} ⊗_A L_{•,•}^{(2)})
        ⥲ H_•(L_{•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)}).                                (6.6.6.1)
```

**6.6.7.**

<!-- label: III.6.6.7 -->

We shall now show that the global hypertor defined in `(6.6.2)`, and the corresponding six spectral sequences, do not
depend on the *finite* affine open covers `𝔘^{(i)}` that served to define them (up to canonical isomorphisms). For this
it will suffice to show that if `𝔙^{(i)}` are two other covers of the same nature, such that `𝔙^{(i)}` is *finer* than
`𝔘^{(i)}` for `i = 1, 2`, then one has canonical isomorphisms of spectral functors

```text
  ^{(t)}E(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ^{(t)}E(𝔙^{(1)}, 𝔙^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})
                                                                                (6.6.7, t)
```

where `t` is replaced by `a`, `b`, `a'`, `b'`, `c`, or `d`.

Now, one has for `i = 1, 2` homomorphisms of bicomplexes

```text
  C^•(𝔘^{(i)}, 𝒫_•^{(i)}) → C^•(𝔙^{(i)}, 𝒫_•^{(i)})
```

well defined up to homotopies `(G, II, 5.7.1)`; there already result canonically defined homomorphisms `(6.6.7, t)`
compatible with the boundary operators in the abutments `(0_III, 11.3.2)`. In addition, the computation of the `E_2`
terms of the spectral sequences `(a)`, `(b)`, `(a')`, `(b')` shows that for these spectral sequences the homomorphism
`(6.6.7, t)` is an isomorphism on the `E_2` terms; since these spectral sequences are biregular, one sees that
`(6.6.7, t)` is an isomorphism for these four spectral functors, hence an isomorphism of bi-`∂`-functors for their
common abutment `(0_III, 11.1.5)`.

In particular, for quasi-coherent `𝒪_{X^{(i)}}`-modules `ℱ^{(i)}` (`i = 1, 2`), the canonical homomorphism

```text
  Tor_•^S(𝔘^{(1)}, 𝔘^{(2)}; ℱ^{(1)}, ℱ^{(2)}) → Tor_•^S(𝔙^{(1)}, 𝔙^{(2)}; ℱ^{(1)}, ℱ^{(2)})
```

is bijective; given the computation of `(6.6.5)`, one sees that `(6.6.7, t)` is also an isomorphism on the `E_2` terms
for `t = c` and `t = d`. One concludes as above that `(6.6.7, t)` is also an isomorphism of spectral sequences for
`t = c` and `t = d`.

<!-- original page 157 -->

One may consider that the isomorphisms `(6.6.7, t)` define inductive systems of spectral functors on the filtered set of
pairs `(𝔘^{(1)}, 𝔘^{(2)})` of finite affine open covers of `X^{(1)}` and `X^{(2)}`. We shall denote by

```text
  ^{(t)}E(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})  or  ^{(t)}E^S(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})
```

the inductive limit of this system, and by `Tor_•^S(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})` the abutment of this
spectral functor, which we shall call the *global hypertor* of the two complexes `𝒫_•^{(1)}` and `𝒫_•^{(2)}`; if
`𝒫_•^{(1)}` and `𝒫_•^{(2)}` are reduced to their terms of degree `0`, `ℱ^{(1)}` and `ℱ^{(2)}`, we shall write

```text
  Tor_n^S(X^{(1)}, X^{(2)}; ℱ^{(1)}, ℱ^{(2)}),
```

and conformably to the general conventions, `Tor_q^S(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})` will therefore be the
bicomplex of `Tor_q^S(X^{(1)}, X^{(2)}; 𝒫_h^{(1)}, 𝒫_k^{(2)})`.

**6.6.8.**

<!-- label: III.6.6.8 -->

The hypotheses being those of `(6.6.1)`, consider now two `S`-morphisms `f_i : X^{(i)} → Y^{(i)}`, where
`Y^{(i)} = Spec(B_i)` is an affine `S`-scheme, `B_i` thus being an `A`-algebra (`i = 1, 2`); this defines therefore an
`A`-homomorphism `B_i → Γ(X^{(i)}, 𝒪_{X^{(i)}})` `(I, 2.2.4)`, and consequently each of the `L_{•,•}^{(i)}` defined in
`(6.6.2)` is a bicomplex of `B_i`-modules; one concludes that `L_{•,•}^{(1)} ⊗_A L_{•,•}^{(2)}` is a quadricomplex of
`(B_1 ⊗_A B_2)`-modules, and its six spectral hyperhomology functors may therefore be considered as taking their values
in the category of spectral sequences of `(B_1 ⊗_A B_2)`-modules. If one sets
`Y = Y^{(1)} ×_S Y^{(2)} = Spec(B_1 ⊗_A B_2)`, one may consider the quasi-coherent `𝒪_Y`-modules associated to these
modules `(I, 1.3.4)`; we shall denote by `^{(t)}ℰ(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})` (for `t = a`, `b`, `a'`, `b'`, `c`,
or `d`) the six spectral sequences `(^{(t)}E(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}))~` of `𝒪_Y`-modules, and
`𝒯or_•^S(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})` their common abutment `(Tor_•^S(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}))~`.
One will denote it `𝒯or_•^S(f_1, f_2; ℱ^{(1)}, ℱ^{(2)})` when `𝒫_•^{(i)}` is reduced to its term of degree `0`,
`ℱ^{(i)}` (`i = 1, 2`).

# §6 (continued). Local and global Tor functors; the Künneth formula

> _Translator's note._ This file continues §III.6 from the companion Part-A file. §6.1–§6.6 are there; §6.7–§6.9 are
> here. They will be concatenated for the final volume.

<!-- original page 25 -->

## 6.7. Global hypertor functors of complexes of quasi-coherent modules and Künneth spectral sequences: the general case.

**6.7.1.**

<!-- label: III.6.7.1 -->

We shall now generalize the definitions of `(6.6.8)` to the case where `S` is an arbitrary prescheme, `X^{(i)}`,
`Y^{(i)}` are `S`-preschemes, and `f_i : X^{(i)} → Y^{(i)}` are separated and quasi-compact morphisms. The task is then,
for every pair of complexes `𝒫_•^{(i)}` of `𝒪_{X^{(i)}}`-modules quasi-coherent, bounded below `(i = 1, 2)`, to define,
for every `n`, an `𝒪_Y`-module quasi-coherent `𝒯or^S_n(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})` together with `6` spectral
functors, which reduce to the definitions of `(6.6.8)` when `S`, `Y^{(1)}` and `Y^{(2)}` are affine (one sets
`Y = Y^{(1)} ×_S Y^{(2)}`).

Suppose first `S = Spec(A)` affine, but `Y^{(1)}` and `Y^{(2)}` arbitrary; let `W^{(i)}` be an affine open of `Y^{(i)}`;
`f_i^{-1}(W^{(i)})` is then a quasi-compact `S`-scheme, `W = W^{(1)} ×_S W^{(2)}` an affine open of `Y`; let
`f_i' : f_i^{-1}(W^{(i)}) → W^{(i)}` be the restriction of `f_i`, and `𝒫_•'^{(i)}` the restriction of `𝒫_•^{(i)}` to
`f_i^{-1}(W^{(i)})` `(i = 1, 2)`. We then have, by `(6.6.8)`, the spectral sequences
`^{(t)}𝓔(f_1', f_2'; 𝒫_•'^{(1)}, 𝒫_•'^{(2)})` of `(𝒪_Y | W)`-modules quasi-coherent, and it remains to verify that they
satisfy the gluing conditions `(0_I, 3.3.1)`. We are at once reduced to the case where `Y^{(i)} = Spec(B_i)` is affine
and where `W^{(i)} = D(g_i)`, with `g_i ∈ B_i`, so that `W = D(g_1 ⊗ g_2)`

<!-- original page 26 -->

in `Y = Spec(B_1 ⊗_A B_2)` `(II, 4.3.2.1)`; if `X'^{(i)} = f_i^{-1}(W^{(i)})`, the task is to establish a canonical
isomorphism of spectral functors

```text
  ^{(t)}E(X'^{(1)}, X'^{(2)}; 𝒫_•'^{(1)}, 𝒫_•'^{(2)})
        ⥲ ^{(t)}E(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⊗_B B_g                (6.7.1.1)
```

where one has set `B = B_1 ⊗_A B_2` and `g = g_1 ⊗ g_2`. To do this, start from finite affine open covers `𝔘^{(i)}` of
`X^{(i)}` `(i = 1, 2)`, and let `𝔘'^{(i)}` be the trace of `𝔘^{(i)}` on `X'^{(i)}`, which is still formed of affine
opens `(I, 5.5.10)`; more precisely, one has

```text
  C^•(𝔘'^{(i)}, 𝒫_•'^{(i)}) = C^•(𝔘^{(i)}, 𝒫_•^{(i)}) ⊗_{B_i} (B_i)_{g_i}.
```

If one sets `L_{•,•}^{(i)} = C^•(𝔘^{(i)}, 𝒫_•^{(i)})`, one therefore has
`L_{•,•}'^{(1)} ⊗_A L_{•,•}'^{(2)} = (L_{•,•}^{(1)} ⊗_{B_1} (B_1)_{g_1}) ⊗_A (L_{•,•}^{(2)} ⊗_{B_2} (B_2)_{g_2})`; since
one has `B_g = (B_1)_{g_1} ⊗_A (B_2)_{g_2}` up to a canonical isomorphism, one has, up to a canonical isomorphism,
`L_{•,•}'^{(1)} ⊗_A L_{•,•}'^{(2)} = (L_{•,•}^{(1)} ⊗_A L_{•,•}^{(2)}) ⊗_B B_g`. If `M_{•,•,•}^{(i)}` is a projective
Cartan–Eilenberg resolution of `L_{•,•}^{(i)}`, which one may suppose formed of `B_i`-modules, it follows from the fact
that `(B_i)_{g_i}` is flat over `B_i` that `M_{•,•,•}'^{(i)} = M_{•,•,•}^{(i)} ⊗_{B_i} (B_i)_{g_i}` is a projective
Cartan–Eilenberg resolution of the bicomplex `L_{•,•}'^{(i)}`; moreover, one has

```text
  M_{•,•,•}'^{(1)} ⊗_A M_{•,•,•}'^{(2)} = (M_{•,•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)}) ⊗_B B_g.
```

The desired isomorphism `(6.7.1.1)` then follows at once from the definitions of the hyperhomology of a bicomplex and
from the exactness of the functor `G ⊗_B B_g` in the `B`-module `G`.

**6.7.2.**

<!-- label: III.6.7.2 -->

Suppose now `S` arbitrary, and let `u_i : Y^{(i)} → S` be the structure morphisms `(i = 1, 2)`. Let `(S_α)` be an affine
open cover of `S`; set `Y_α^{(i)} = u_i^{-1}(S_α)`, `X_α^{(i)} = f_i^{-1}(Y_α^{(i)})`, and let
`f_{iα} : X_α^{(i)} → Y_α^{(i)}` be the restriction of `f_i`, which is a separated and quasi-compact morphism. The
`Y_α = Y_α^{(1)} ×_{S_α} Y_α^{(2)}` form an open cover of `Y`, and on each `Y_α` there are defined by `(6.7.1)` spectral
functors

```text
  ^{(t)}𝓔_α(f_{1α}, f_{2α}; 𝒫_•^{(1)} | X_α^{(1)}, 𝒫_•^{(2)} | X_α^{(2)});
```

it remains again to show that these functors satisfy the gluing conditions. One is at once reduced to the following
situation: `S = Spec(A)` is affine, `S' = D(h)`, with `h ∈ A`, and `u_i(Y^{(i)}) ⊂ S'`; one may further suppose
`Y^{(i)} = Spec(B_i)` affine; the task is to define canonical isomorphisms

```text
  ^{(t)}E^S(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ^{(t)}E^{S'}(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}).
                                                                                  (6.7.2.1)
```

Now, with the notations of `(6.6.2)`, the `L_{•,•}^{(i)}` are formed of `A_h`-modules, and one therefore has
`L_{•,•}^{(1)} ⊗_{A_h} L_{•,•}^{(2)} = L_{•,•}^{(1)} ⊗_A L_{•,•}^{(2)}` up to a canonical isomorphism; since one may
take a projective Cartan–Eilenberg resolution `M_{•,•,•}^{(i)}` of `L_{•,•}^{(i)}` formed of `A_h`-modules, this gives
at once the desired canonical isomorphism.

We have thus, in summary, proved the

**Theorem (6.7.3).**

<!-- label: III.6.7.3 -->

— *Let `S` be a prescheme, `f_i : X^{(i)} → Y^{(i)}` a separated and quasi-compact `S`-morphism of `S`-preschemes,
`𝒫_•^{(i)}` a complex of `𝒪_{X^{(i)}}`-modules quasi-coherent, bounded below `(i = 1, 2)`; one sets
`Y = Y^{(1)} ×_S Y^{(2)}`. There exists a bi-∂-functor `𝒯or^S_•(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})`*

<!-- original page 27 -->

*with values in the category of `𝒪_Y`-modules quasi-coherent, such that if `V^{(i)}` is an affine open of `Y^{(i)}`
`(i = 1, 2)` and `V = V^{(1)} ×_S V^{(2)}`, one has*

```text
  𝒯or^S_•(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)}) | V
      = (Tor^S_•(f_1^{-1}(V^{(1)}), f_2^{-1}(V^{(2)}); 𝒫_•^{(1)} | f_1^{-1}(V^{(1)}), 𝒫_•^{(2)} | f_2^{-1}(V^{(2)})))~.
```

*This bifunctor is the abutment of six biregular spectral functors*

```text
  ^{(t)}𝓔(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})                                  (t = a, b, a', b', c, d)
```

*whose `E_2` terms are given by*

```text
  (a)   ^{(a)}𝓔^2_{pq} = ⊕_{q_1 + q_2 = q} 𝒯or^S_p(ℋ^{-q_1}(f_1, 𝒫_•^{(1)}), ℋ^{-q_2}(f_2, 𝒫_•^{(2)}))

  (b)   ^{(b)}𝓔^2_{pq} = ℋ^{-p}(f_1 ×_S f_2, 𝒯or^S_q(𝒫_•^{(1)}, 𝒫_•^{(2)}))

  (a')  ^{(a')}𝓔^2_{pq} = ⊕_{q_1 + q_2 = q} 𝒯or^S_p(ℋ^{-q_1}(f_1, 𝒫_•^{(1)}), ℋ^{-q_2}(f_2, 𝒫_•^{(2)}))

  (b')  ^{(b')}𝓔^2_{pq} = ℋ^{-p}(f_1 ×_S f_2, 𝒯or^S_q(𝒫_•^{(1)}, 𝒫_•^{(2)}))

  (c)   ^{(c)}𝓔^2_{pq} = ⊕_{q_1 + q_2 = q} 𝒯or^S_p(f_1, f_2; ℋ_{q_1}(𝒫_•^{(1)}), ℋ_{q_2}(𝒫_•^{(2)}))

  (d)   ^{(d)}𝓔^2_{pq} = ℋ_p(𝒯or^S_q(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})).
```

*One says that the spectral sequences `(a)` and `(b)` are the* Künneth spectral sequences.

One will note that the spectral sequences `(a)` and `(a')` (resp. `(b)` and `(b')`) are *identical* when `𝒫_•^{(1)}` and
`𝒫_•^{(2)}` reduce to their terms of degree `0`; in this case, the sequences `(c)` and `(d)` are degenerate and are
therefore without interest.

**Remark (6.7.4).**

<!-- label: III.6.7.4 -->

The global hypertor that we have defined above include as particular cases both the hypercohomology modules defined in
`(6.2.1)` and the local hypertor defined in `(6.5.3)`. Let us show that one has, for every morphism `f : X → Y`
quasi-compact and separated and every complex `𝒫_•` of `𝒪_X`-modules quasi-coherent, bounded below, a canonical
isomorphism of ∂-functors in `𝒫_•`

```text
  𝒯or^Y_n(f, 1_Y; 𝒫_•, 𝒪_Y) ⥲ ℋ^{-n}(f, 𝒫_•)                  (for every n ∈ ℤ).        (6.7.4.1)
```

Indeed, the gluing methods of `(6.7.2)` reduce one at once to the case where `Y` is affine; one may then, by virtue of
`(6.2.2)`, compute the two members of `(6.7.4.1)` using one and the same finite cover `𝔘` of `Y` by affine opens, and
(for the first member) the cover of `Y` formed of `Y` itself; with the notations of `(6.6.2)`, the bicomplex
`L_{•,•}^{(2)}` is then reduced to its term of degrees `(0, 0)`, equal to `A`, and the conclusion follows from
`(0_III, 11.7.5)`. For a generalization of this result, see `(6.7.7)`; but one will note that when one replaces `𝒪_Y` by
an arbitrary quasi-coherent `𝒪_Y`-module `ℱ` in the first member of `(6.7.4.1)`, one no longer has in general an
isomorphism with `ℋ^{-n}(f, 𝒫_• ⊗_{𝒪_Y} ℱ)`, although, in the preceding computation, the bicomplex `L_{•,•}^{(1)} ⊗_A ℱ`
still identifies with the bicomplex `C^•(𝔘, 𝒫_• ⊗_{𝒪_Y} ℱ)`.

On the other hand, one has a canonical isomorphism of bi-∂-functors

```text
  𝒯or^S_•(1_{X^{(1)}}, 1_{X^{(2)}}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ 𝒯or^S_•(𝒫_•^{(1)}, 𝒫_•^{(2)}).             (6.7.4.2)
```

Indeed, one reduces again, by `(6.7.1)` and `(6.7.2)`, to the case where `S` and the `X^{(i)}` are affine; in computing
the first member of `(6.7.4.2)`, one may then take

<!-- original page 28 -->

as cover `𝔘^{(i)}` the family reduced to the single element `X^{(i)}`, so that, with the notations of `(6.6.2)`,
`L_{•,•}^{(i)}` reduces to `Γ(X^{(i)}, 𝒫_•^{(i)})` (regarded as a bicomplex whose terms of first degree `≠ 0` are zero),
and the equality of the two members of `(6.7.4.2)` follows from `(6.4.1.1)` and `(6.3.1)`.

**Proposition (6.7.5).**

<!-- label: III.6.7.5 -->

— *Let `u : 𝒫_•^{(1)} → 𝒬_•^{(1)}` be a homomorphism of complexes of `𝒪_{X^{(1)}}`-modules quasi-coherent, bounded
below, such that the homomorphism*

```text
  ℋ_•(u) : ℋ_•(𝒫_•^{(1)}) → ℋ_•(𝒬_•^{(1)})
```

*deduced from `u` is an isomorphism. Then the homomorphisms*

```text
  ^{(t)}𝓔(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)}) → ^{(t)}𝓔(f_1, f_2; 𝒬_•^{(1)}, 𝒫_•^{(2)})
```

*deduced from `u` are isomorphisms for `t = a`, `t = b` and `t = c`.*

The assertion concerning the spectral sequence `(c)` follows from the fact that this sequence is biregular and that the
homomorphism in question is an isomorphism on the `E_2` terms by hypothesis `(0_III, 11.1.5)`. This already shows that
`𝒯or^S_•(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)}) → 𝒯or^S_•(f_1, f_2; 𝒬_•^{(1)}, 𝒫_•^{(2)})` is an isomorphism. Applying the
relations `(6.7.4.1)` and `(6.7.4.2)` one sees first that the homomorphisms
`ℋ^{-n}(f_1, 𝒫_•^{(1)}) → ℋ^{-n}(f_1, 𝒬_•^{(1)})` and `𝒯or^S_•(𝒫_•^{(1)}, 𝒫_•^{(2)}) → 𝒯or^S_•(𝒬_•^{(1)}, 𝒫_•^{(2)})`
deduced from `u` are isomorphisms. The assertion concerning the sequences `(a)` and `(b)` then follows from the fact
that these sequences are biregular `(6.7.3)` and that the homomorphisms in question are bijective on the `E_2` terms
`(0_III, 11.1.5)`.

Note moreover that, if `u : 𝒫_•^{(1)} → 𝒬_•^{(1)}` is a homotopism, one deduces from it canonical isomorphisms
`^{(t)}𝓔(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ^{(t)}𝓔(f_1, f_2; 𝒬_•^{(1)}, 𝒫_•^{(2)})` for the six spectral sequences.
Indeed, if `S` and the `Y^{(i)}` are affine, one deduces from `u` a homotopism of bicomplexes
`C^•(𝔘^{(1)}, 𝒫_•^{(1)}) → C^•(𝔘^{(1)}, 𝒬_•^{(1)})`, and the proposition follows from the general theory of
hyperhomology `(0_III, 11.3.2)`; the passage to the general case is done by gluing, using the fact that, from a
homotopism of complexes, one deduces a homotopism of projective Cartan–Eilenberg resolutions of these complexes
`(M, XVII, 1.2)`.

**Proposition (6.7.6).**

<!-- label: III.6.7.6 -->

— *Suppose that the complex `𝒫_•^{(1)}` or the complex `𝒫_•^{(2)}` is formed of `S`-flat modules (both complexes being
bounded below). Then one has a canonical isomorphism of bi-∂-functors*

```text
  𝒯or^S_n(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ℋ^{-n}(f_1 ×_S f_2, 𝒫_•^{(1)} ⊗_S 𝒫_•^{(2)}).            (6.7.6.1)
```

Suppose first `S`, `Y^{(1)}` and `Y^{(2)}` affine, so that one is in the situation of `(6.6.2)`, whose notations we
keep. Suppose for instance that `𝒫_•^{(1)}` is formed of `S`-flat modules, and let us compute the hypertor using remark
`(6.6.6)`: it is therefore the homology of `L_{•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)}`, where `M_{•,•,•}^{(2)}` is a projective
Cartan–Eilenberg resolution of `L_{•,•}^{(2)}`, in the sense of `(0_III, 11.7.1)`. On the other hand, the modules
`L_{•,•}^{(1)}` are flat over `A` by virtue of hypothesis `(1.4.15.1)`; one then deduces from `(0_III, 11.7.5)` a
canonical isomorphism

```text
  Tor^S_•(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ℋ_•(L_{•,•}^{(1)} ⊗_A L_{•,•}^{(2)}).             (6.7.6.2)
```

On the other hand, one has a natural homomorphism of bicomplexes from `L_{•,•}^{(1)} ⊗_A L_{•,•}^{(2)}` into
`C^•(𝔘, 𝒬_•)`, where `𝔘` is the cover of `Z = X^{(1)} ×_S X^{(2)}` by the affine opens

<!-- original page 29 -->

`U_α^{(1)} ×_S U_β^{(2)}` and `𝒬_• = 𝒫_•^{(1)} ⊗_S 𝒫_•^{(2)}` (regarded as a simple complex with respect to total
degree); indeed, the definition of this homomorphism has in substance been given in the course of the computation of the
sequence `(b')` in `(6.6.4)`, for `q = 0`; it suffices simply (keeping the notations of `(6.6.4)`) to take into account
that on the one hand there is a natural homomorphism from the complex `N^{•k}` into the complex
`C^•(Φ^{(1)}, Φ^{(2)}; 𝒮_k)` `(0_III, 11.8.5)`, on the other hand a natural homomorphism from this latter complex into
the complex `P^•(Φ^{(1)}, Φ^{(2)}; 𝒮_k)` `(0_III, 11.8.6)`, and finally a natural homomorphism from this latter complex
of cochains into the subcomplex of alternating cochains `(0_III, 11.8.7)`. Moreover, the homomorphism of bicomplexes
thus defined gives an isomorphism in homology, as seen in `(6.6.4)`; one therefore has, by composing with `(6.7.6.2)`,
obtained an isomorphism

```text
  Tor^S_•(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ H^{-n}(𝔘, 𝒫_•^{(1)} ⊗_S 𝒫_•^{(2)}).               (6.7.6.3)
```

It must next be proved that the isomorphism thus defined does not depend on the chosen open covers (the second member of
`(6.7.6.3)` being canonically isomorphic to `H^{-n}(X^{(1)} ×_S X^{(2)}, 𝒫_•^{(1)} ⊗_S 𝒫_•^{(2)})` by `(6.2.2)`); this
is done using `(6.6.7)` by noting (with the notations of `(6.6.7)`) that one has a commutative diagram up to homotopisms

```text
  C^•(𝔘^{(1)}, 𝒫_•^{(1)}) ⊗_A C^•(𝔘^{(2)}, 𝒫_•^{(2)})  ──→  C^•(𝔘, 𝒬_•)

              │                                                  │
              │                                                  │
              ↓                                                  ↓

  C^•(𝔙^{(1)}, 𝒫_•^{(1)}) ⊗_A C^•(𝔙^{(2)}, 𝒫_•^{(2)})  ──→  C^•(𝔙, 𝒬_•)
```

where the horizontal arrows are the homomorphisms defined above. Finally, one passes to the general case by gluing,
which is done without difficulty as in `(6.7.1)` and `(6.7.2)`; we leave the details to the reader.

**Proposition (6.7.7).**

<!-- label: III.6.7.7 -->

— *Suppose that `𝒫_•^{(1)}` and `𝒫_•^{(2)}` are bounded below, and that all the modules `ℋ^{-n}(f_1, 𝒫_•^{(1)})` or all
the modules `ℋ^{-n}(f_2, 𝒫_•^{(2)})` are `S`-flat. Then one has a canonical isomorphism of bi-∂-functors (`n` running
through `ℤ`)*

```text
  𝒯or^S_n(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ⊕_{q_1 + q_2 = n} ℋ^{-q_1}(f_1, 𝒫_•^{(1)}) ⊗_S ℋ^{-q_2}(f_2, 𝒫_•^{(2)}).
                                                                                  (6.7.7.1)
```

Indeed, in view of `(6.5.8)`, the spectral sequence `(a)` of `(6.7.3)` is degenerate, and the proposition follows at
once from `(0_III, 11.1.6)`, this sequence being biregular `(6.7.3)`.

**Theorem (6.7.8).**

<!-- label: III.6.7.8 -->

— *Suppose that: 1° the complexes `𝒫_•^{(1)}` and `𝒫_•^{(2)}` are bounded below; 2° the complex `𝒫_•^{(1)}` or the
complex `𝒫_•^{(2)}` is formed of `S`-flat modules; 3° all the*

<!-- original page 30 -->

*modules `ℋ^{-n}(f_1, 𝒫_•^{(1)})` or all the modules `ℋ^{-n}(f_2, 𝒫_•^{(2)})` are `S`-flat. Then one has a canonical
isomorphism of bi-∂-functors (`n` running through `ℤ`)*

```text
  ℋ^{-n}(f_1 ×_S f_2, 𝒫_•^{(1)} ⊗_S 𝒫_•^{(2)})
       ⥲ ⊕_{n_1 + n_2 = n} ℋ^{-n_1}(f_1, 𝒫_•^{(1)}) ⊗_S ℋ^{-n_2}(f_2, 𝒫_•^{(2)})            (6.7.8.1)
```

*("*Künneth formula*").*

This follows from `(6.7.6)` and `(6.7.7)`.

When `S`, `Y^{(1)}` and `Y^{(2)}` are affine, the inverse of the isomorphism `(6.7.8.1)` is deduced (with the notations
of `(6.7.6)`) from the homomorphism of bicomplexes

```text
  C^•(𝔘^{(1)}, 𝒫_•^{(1)}) ⊗_A C^•(𝔘^{(2)}, 𝒫_•^{(2)}) → C^•(𝔘, 𝒬_•)
```

by the procedure defined in `(G, I, 2.7)`, as follows from `(G, I, 5.5)`.

**Proposition (6.7.9).**

<!-- label: III.6.7.9 -->

— *Suppose the following three conditions verified:*

*1° `S`, `Y^{(1)}` and `Y^{(2)}` are locally Noetherian, `f_1` and `f_2` are proper, `Y^{(1)}` or `Y^{(2)}` of finite
type over `S`.*

*2° `𝒫_•^{(1)}` and `𝒫_•^{(2)}` are bounded below.*

*3° For every `n ∈ ℤ`, `ℋ_n(𝒫_•^{(i)})` is a coherent module `(i = 1, 2)`.*

*Under these conditions, `𝒯or^S_n(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})` is a coherent `𝒪_Y`-module (with
`Y = Y^{(1)} ×_S Y^{(2)}`).*

It follows from `(6.5.13)` that the local hypertor `𝒯or^S_n(𝒫_•^{(1)}, 𝒫_•^{(2)})` are coherent `𝒪_X`-modules
(`X = X^{(1)} ×_S X^{(2)}` being locally Noetherian, since one of the `X^{(i)}` is by hypothesis of finite type over `S`
`(I, 6.3.4 and 6.3.8)`). Since `Y` is locally Noetherian and `f_1 ×_S f_2` is proper `(II, 5.4.2)`, it follows from
`(6.2.5)` that the terms `^{(b)}𝓔^2_{pq}` of `(6.7.3)` are coherent `𝒪_Y`-modules. Since all the spectral sequences of
`(6.7.3)` are biregular by virtue of hypothesis 2°, one concludes by `(0_III, 11.1.8)`.

**6.7.10.**

<!-- label: III.6.7.10 -->

Let now `Y'^{(i)}` be two `S`-preschemes `(i = 1, 2)`, `v_i : Y'^{(i)} → Y^{(i)}` two `S`-morphisms, `v : v_1 ×_S v_2`
their product, which is an `S`-morphism `Y' → Y`, where one sets `Y' = Y'^{(1)} ×_S Y'^{(2)}`. Consider on the other
hand, for `i = 1, 2`, an `S`-prescheme `X'^{(i)}`, and two `S`-morphisms `u_i : X'^{(i)} → X^{(i)}`,
`f_i' : X'^{(i)} → Y'^{(i)}`, so that the diagrams

```text
                       u_i
            X'^{(i)} ─────→ X^{(i)}

            f_i' │             │ f_i                                                      (6.7.10.1)
                 ↓             ↓

            Y'^{(i)} ─────→ Y^{(i)}
                       v_i
```

are commutative, the morphisms `f_i'` being *separated* and *quasi-compact*. One then has canonical
`𝒪_{Y'}`-homomorphisms of spectral functors

```text
  v^*(^{(t)}𝓔(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})) → ^{(t)}𝓔(f_1', f_2'; u_1^*(𝒫_•^{(1)}), u_2^*(𝒫_•^{(2)}))
                                                                                          (6.7.10.2)
```

for `t = a, a', b, b', c, d`. To define these, suppose first `S = Spec(A)`, `Y^{(i)} = Spec(B_i)`,
`Y'^{(i)} = Spec(B_i')` affine; the `X^{(i)}` and `X'^{(i)}` are then quasi-compact schemes. To compute the spectral
sequences `^{(t)}𝓔(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})`, we shall consider as in `(6.6.1)` finite covers `𝔘^{(i)}` by affine
opens of `X^{(i)}` `(i = 1, 2)`; to compute `^{(t)}𝓔(f_1', f_2'; u_1^*(𝒫_•^{(1)}), u_2^*(𝒫_•^{(2)}))`, we shall consider
finite covers `𝔘'^{(i)}`

<!-- original page 31 -->

of `X'^{(i)}` by affine opens, finer respectively than the covers `u_i^{-1}(𝔘^{(i)})` `(i = 1, 2)`. It is clear that the
bicomplex `C^•(𝔘^{(i)}, 𝒫_•^{(i)}) = L_{•,•}^{(i)}` can be regarded canonically as a sub-bicomplex of
`C^•(u_i^{-1}(𝔘^{(i)}), u_i^*(𝒫_•^{(i)}))` `(0_I, 4.4.3.2)`; moreover, by choosing a simplicial map `(G, II, 5.7)` of
`𝔘'^{(i)}` into `u_i^{-1}(𝔘^{(i)})`, one defines a homomorphism of bicomplexes
`C^•(u_i^{-1}(𝔘^{(i)}), u_i^*(𝒫_•^{(i)})) → C^•(𝔘'^{(i)}, u_i^*(𝒫_•^{(i)}))`, whence, by composition, a homomorphism of
bicomplexes `L_{•,•}^{(i)} → L_{•,•}'^{(i)} = C^•(𝔘'^{(i)}, u_i^*(𝒫_•^{(i)}))`. Moreover, this homomorphism is replaced
by a homotopic homomorphism when one changes simplicial map `(G, II, 5.7.1)`; one has thus a well-defined homomorphism
of spectral functors:

```text
  ^{(t)}𝓔(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) → ^{(t)}𝓔(𝔘'^{(1)}, 𝔘'^{(2)}; u_1^*(𝒫_•^{(1)}), u_2^*(𝒫_•^{(2)})).
                                                                                          (6.7.10.3)
```

One verifies at once that if `𝔙^{(i)}` is a finite affine cover of `X^{(i)}` finer than `𝔘^{(i)}`, `𝔙'^{(i)}` a finite
affine cover of `X'^{(i)}` finer than `u_i^{-1}(𝔙^{(i)})` and than `𝔙^{(i)}`, the diagram

```text
  C^•(𝔘^{(i)}, 𝒫_•^{(i)})  ─────→  C^•(𝔙^{(i)}, 𝒫_•^{(i)})

           │                                  │
           │                                  │
           ↓                                  ↓

  C^•(𝔘'^{(i)}, u_i^*(𝒫_•^{(i)})) ─→  C^•(𝔙'^{(i)}, u_i^*(𝒫_•^{(i)}))
```

is commutative, which implies that the homomorphism `(6.7.10.3)` does not depend essentially on the covers `𝔘^{(i)}` and
`𝔘'^{(i)}` considered. One has therefore in fact defined a homomorphism of `A`-modules

```text
  ^{(t)}E(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) → ^{(t)}E(X'^{(1)}, X'^{(2)}; u_1^*(𝒫_•^{(1)}), u_2^*(𝒫_•^{(2)})).
                                                                                          (6.7.10.4)
```

But it is clear by definition of the `u_i^*(𝒫_•^{(i)})` and by virtue of the commutativity of `(6.7.10.1)` that this
homomorphism is also a homomorphism of `(B_1 ⊗_A B_2)`-modules; since the second member of `(6.7.10.4)` is formed of
`(B_1' ⊗_A B_2')`-modules, one canonically deduces from `(6.7.10.4)` a homomorphism of `(B_1' ⊗_A B_2')`-modules

```text
  ^{(t)}E(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⊗_{B_1 ⊗_A B_2} (B_1' ⊗_A B_2')
       → ^{(t)}E(X'^{(1)}, X'^{(2)}; u_1^*(𝒫_•^{(1)}), u_2^*(𝒫_•^{(2)}))                   (6.7.10.5)
```

which, in view of `(I, 1.6.5)`, is none other than the desired homomorphism `(6.7.10.2)` in the particular case
considered.

It remains to pass to the general case by following the gluings of `(6.7.1)` and `(6.7.2)`; the second passage is
immediate; as for the first, one considers as in `(6.7.1)` elements `g_i ∈ B_i`, and their images `g_i' ∈ B_i'`, the
tensor product `g = g_1 ⊗ g_2` in `B = B_1 ⊗_A B_2` and its image `g' = g_1' ⊗ g_2'` in `B' = B_1' ⊗_A B_2'`, and
everything reduces to using

<!-- original page 32 -->

the canonical isomorphism `(M ⊗_B B')_{g'} ⥲ M_g ⊗_{B_g} B_{g'}'` `(0_I, 1.5.4)`; we leave the details to the reader.

**6.7.11.**

<!-- label: III.6.7.11 -->

The theory of global hypertor, developed above for two `S`-morphisms `X^{(i)} → Y^{(i)}` and two complexes `𝒫_•^{(i)}`
of modules quasi-coherent bounded below, extends at once to the following general case: one has a prescheme `S`, a
finite family of `S`-preschemes `Y^{(i)}` `(i ∈ I)`, a finite family of `S`-morphisms separated and quasi-compact
`f_i : X^{(i)} → Y^{(i)}`, and for each `i` a complex of `𝒪_{X^{(i)}}`-modules quasi-coherent `𝒫_•^{(i)}` bounded below.
If `Y` is the product of the `S`-preschemes `Y^{(i)}`, one then defines, for each integer `n ∈ ℤ`, an `𝒪_Y`-module
quasi-coherent `𝒯or^S_n((f_i)_{i ∈ I}; (𝒫_•^{(i)})_{i ∈ I})`, these modules forming a ∂-functor covariant in each of the
complexes `𝒫_•^{(i)}`; moreover, this functor is the common abutment of six spectral functors
`^{(t)}𝓔((f_i)_{i ∈ I}; (𝒫_•^{(i)})_{i ∈ I})`. We leave to the reader the task of repeating for this general case the
definitions and reasoning given above for `I = {1, 2}`. Let us simply note that when `I` reduces to a single element,
one recovers the hypercohomology `ℋ^•(f, 𝒫_•)` defined in `(6.2.7)` (as already observed in `(6.7.4)`). When `I` is the
interval `1 ≤ i ≤ m` of `ℕ`, we shall write

```text
  𝒯or^S_n(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})    for    𝒯or^S_n((f_i)_{i ∈ I}; (𝒫_•^{(i)})_{i ∈ I}).
```

**Proposition (6.7.12).**

<!-- label: III.6.7.12 -->

— *The notations being those of `(6.7.11)`, let `J` be a subset of `I` such that, for `i ∈ I − J`, one has
`X^{(i)} = Y^{(i)} = S`, `f_i` being reduced to the identity, and `𝒫_•^{(i)}` equal to the complex reduced to the term
of degree `0` equal to `𝒪_S`. There is then a canonical isomorphism of ∂-functors*

```text
  𝒯or^S_•((f_i)_{i ∈ I}; (𝒫_•^{(i)})_{i ∈ I}) ⥲ 𝒯or^S_•((f_j)_{j ∈ J}; (𝒫_•^{(j)})_{j ∈ J}).         (6.7.12.1)
```

One may restrict oneself to defining this isomorphism when `S` and the `Y^{(i)}` are affine, the gluing being done as
usual. For `i ∈ I − J`, one may take the cover `𝔘^{(i)}` formed of the single set `S`, and then
`L_{•,•}^{(i)} = C^•(𝔘^{(i)}, 𝒫_•^{(i)})` reduces to its only term of degrees `(0, 0)`, equal to `Γ(S, 𝒪_S) = A(S)`; the
isomorphism `(6.7.12.1)` is then evident.

**Remark (6.7.13).**

<!-- label: III.6.7.13 -->

The notations being those of `(6.7.3)`, consider the canonical `S`-isomorphism
`Y^{(1)} ×_S Y^{(2)} ⥲ Y^{(2)} ×_S Y^{(1)}` `(I, 3.3.5)`; then the image by this isomorphism of
`𝒯or^S_•(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})` is `𝒯or^S_•(f_2, f_1; 𝒫_•^{(2)}, 𝒫_•^{(1)})`; the question being local, one is
reduced to the case envisaged in `(6.6.2)`, and if one denotes by `M_{•,•,•}^{(i)}` a projective Cartan–Eilenberg
resolution of `L_{•,•}^{(i)}` `(i = 1, 2)`, the isomorphism considered transforms `M_{•,•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)}`
into `M_{•,•,•}^{(2)} ⊗_A M_{•,•,•}^{(1)}`, whence our assertion by considering the homology of the simple complexes
associated to these tricomplexes.

## 6.8. The associativity spectral sequences of the global hypertor.

**6.8.1.**

<!-- label: III.6.8.1 -->

The hypotheses and notations being those of `(6.7.11)` (and in particular the `𝒫_•^{(i)}` being supposed bounded below),
suppose given a partition `(I_j)_{j ∈ J}` of the index set `I`; we propose to give an "associativity" relation between
the hypertor `𝒯or^S_•((f_i)_{i ∈ I}; (𝒫_•^{(i)})_{i ∈ I})` and each of the "partial" hypertor

```text
  𝒯_{•, j} = 𝒯or^S_•((f_i)_{i ∈ I_j}; (𝒫_•^{(i)})_{i ∈ I_j}).
```

<!-- original page 33 -->

To simplify the notation, we shall restrict to the case where `I` is the interval `1 ≤ i ≤ m`, and where the partition
`(I_j)` is composed of the two intervals `{1, 2, …, r}` and `{r + 1, …, m}`.

**Proposition (6.8.2).**

<!-- label: III.6.8.2 -->

— *There exists a canonical biregular spectral functor (called the* "associativity spectral functor"*) denoted*

```text
  ^{(e)}𝓔(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})  (or simply  ^{(e)}𝓔(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}))
```

*whose abutment is `𝒯or^S_•(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})`, and whose `E_2` term is given by*

```text
  ^{(e)}𝓔^2_{pq} = ⊕_{q_1 + q_2 = q} 𝒯or^S_p(𝒯or^S_{q_1}(f_1, …, f_r; 𝒫_•^{(1)}, …, 𝒫_•^{(r)}),
                                            𝒯or^S_{q_2}(f_{r+1}, …, f_m; 𝒫_•^{(r+1)}, …, 𝒫_•^{(m)})).
```

In this statement, one has identified `Y` canonically with the product `Z^{(1)} ×_S Z^{(2)}`, where
`Z^{(1)} = Y^{(1)} ×_S Y^{(2)} ×_S ⋯ ×_S Y^{(r)}` and `Z^{(2)} = Y^{(r+1)} ×_S ⋯ ×_S Y^{(m)}`. We restrict ourselves to
the case where `S` and the `Y^{(i)}` are affine; one passes from this particular case to the general case by the methods
developed in `(6.7.1)` and `(6.7.2)`, and we leave the details of the reasoning (without difficulty) to the reader. We
shall therefore prove the

**Corollary (6.8.3).**

<!-- label: III.6.8.3 -->

— *Let `A` be a ring, `S = Spec(A)`, `X^{(i)}` `(1 ≤ i ≤ m)` be `S`-schemes quasi-compact and, for each `i`, let
`𝒫_•^{(i)}` be a complex of `𝒪_{X^{(i)}}`-modules quasi-coherent bounded below. There exists a canonical biregular
spectral functor having for abutment*

```text
  Tor^S_•(X^{(1)}, …, X^{(m)}; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})
```

*and whose `E_2` term is given by*

```text
  ^{(e)}E^2_{pq} = ⊕_{q_1 + q_2 = q} Tor^A_p(Tor^S_{q_1}(X^{(1)}, …, X^{(r)}; 𝒫_•^{(1)}, …, 𝒫_•^{(r)}),
                                            Tor^S_{q_2}(X^{(r+1)}, …, X^{(m)}; 𝒫_•^{(r+1)}, …, 𝒫_•^{(m)})).
```

According to the definition given in `(6.6.2)`, the computation of the hypertor in question is carried out by taking,
for each `i`, a finite affine open cover `𝔘^{(i)}` of `X^{(i)}`, by considering the bicomplexes
`L_{•,•}^{(i)} = C^•(𝔘^{(i)}, 𝒫_•^{(i)})`, a projective Cartan–Eilenberg resolution `M_{•,•,•}^{(i)}` of each of these
bicomplexes (in the sense of `(0_III, 11.7.1)`), the tensor product `M_{•,•,•} = ⊗_{i=1}^m M_{•,•,•}^{(i)}` of these
tricomplexes, and by taking the homology of `M_{•,•,•}`. Consider `M_{•,•,•}` as a simple complex `N_•`, tensor product
of the two simple complexes

```text
  N_•' = ⊗_{i=1}^r M_{•,•,•}^{(i)},               N_•'' = ⊗_{i=r+1}^m M_{•,•,•}^{(i)},
```

where `N_•'` and `N_•''` are graded by the sum of the total degrees of the `M_{•,•,•}^{(i)}`. Moreover, the `A`-modules
of the complexes `N_•'` and `N_•''` are *projective*, so it follows from `(6.5.9)` that one has
`H_•(M_{•,•,•}) = Tor^A_•(N_•', N_•'')`; the spectral sequence sought is then none other than the sequence `(6.3.2.2)`
applied to the complexes `N_•'` and `N_•''`, taking into account the interpretation of the homology modules of these
complexes which follows from what precedes (when one applies the remarks of the beginning to each of the partial
products `X^{(1)} ×_S ⋯ ×_S X^{(r)}` and `X^{(r+1)} ×_S ⋯ ×_S X^{(m)}`). Finally, the regularity properties follow from
`(6.3.2)` and from the fact that, the `𝒫_•^{(i)}` being bounded below, so are the `M_{•,•,•}^{(i)}`; consequently,
`N_•'` and `N_•''` are bounded below.

<!-- original page 34 -->

## 6.9. The base-change spectral sequences in the global hypertor.

**6.9.1.**

<!-- label: III.6.9.1 -->

The hypotheses and notations being still those of `(6.7.11)` (and in particular the `𝒫_•^{(i)}` being supposed bounded
below), consider a morphism `g : S' → S` of preschemes, and set `Y'^{(i)} = Y^{(i)}_{(S')}`, `X'^{(i)} = X^{(i)}_{(S')}`
and `𝒫_•'^{(i)} = 𝒫_•^{(i)} ⊗_{𝒪_S} 𝒪_{S'}`, `𝒫_•'^{(i)}` thus being a complex of `𝒪_{X'^{(i)}}`-modules quasi-coherent;
let `f_i' = (f_i)_{(S')} : X'^{(i)} → Y'^{(i)}`, which is a separated and quasi-compact morphism `(I, 5.5.1 and 6.6.4)`.
We propose to study the relations between the `𝒪_{Y'}`-modules quasi-coherent
`𝒯or^{S'}_n((f_i')_{i ∈ I}; (𝒫_•'^{(i)})_{i ∈ I})` and `𝒯or^S_n((f_i)_{i ∈ I}; (𝒫_•^{(i)})_{i ∈ I}) ⊗_{𝒪_S} 𝒪_{S'}`,
where `Y' = Y ×_S S' = Y_{(S')}`. A particularly simple case is the following one, which reduces to `(1.4.15)` when `I`
reduces to a single element and `𝒫_•` to a single module:

**Proposition (6.9.2).**

<!-- label: III.6.9.2 -->

— *If the morphism `g : S' → S` is flat, one has a canonical isomorphism of ∂-functors (in the `𝒫_•^{(i)}`):*

```text
  𝒯or^S_•((f_i)_{i ∈ I}; (𝒫_•^{(i)})_{i ∈ I}) ⊗_{𝒪_S} 𝒪_{S'} ⥲ 𝒯or^{S'}_•((f_i')_{i ∈ I}; (𝒫_•'^{(i)})_{i ∈ I}).
                                                                                          (6.9.2.1)
```

One may again restrict oneself to the case where `S`, `S'` and the `Y^{(i)}` are affine, the gluing being done following
the methods of `(6.7.1)` and `(6.7.2)`. Let `S = Spec(A)`, `S' = Spec(A')`, and take for each `i` an affine open cover
`𝔘^{(i)}` of `X^{(i)}`; if `u_i : X'^{(i)} → X^{(i)}` is the canonical projection, `u_i^{-1}(𝔘^{(i)})` is an affine open
cover of `X'^{(i)}` `(II, 1.5.5)`, which we shall denote by `𝔘'^{(i)}`; it is then clear that
`C^•(𝔘'^{(i)}, 𝒫_•'^{(i)}) = C^•(𝔘^{(i)}, 𝒫_•^{(i)}) ⊗_A A'`, and the existence of the isomorphism `(6.9.2.1)` is
immediate, since if `M_{•,•,•}^{(i)}` is a projective Cartan–Eilenberg resolution of
`L_{•,•}^{(i)} = C^•(𝔘^{(i)}, 𝒫_•^{(i)})` in the sense of `(0_III, 11.7.1)`, formed of `A`-modules,
`M_{•,•,•}^{(i)} ⊗_A A'` is a projective Cartan–Eilenberg resolution (in the same sense) of `L_{•,•}^{(i)} ⊗_A A'`
formed of `A'`-modules, by virtue of the hypothesis that `A'` is a flat `A`-module; this same hypothesis shows moreover
that `H_•(⊗_{i=1}^m (M_{•,•,•}^{(i)} ⊗_A A')) = H_•(⊗_{i=1}^m M_{•,•,•}^{(i)}) ⊗_A A'`.

One will note that when `I` is reduced to the single element `1`, the formula `(6.9.2.1)` follows directly from
`(6.7.7)`, applied by taking `Y_2 = X_2 = S'`, `f_2 = 1_{S'}`, and the complex `𝒫_•^{(2)}` reduced to its term of degree
`0`, equal to `𝒪_{S'}`; one knows then that the hypercohomology `ℋ^n(1_{S'}, 𝒪_{S'})` is zero for every `n ≠ 0` and
reduces to `𝒪_{S'}` for `n = 0` `(6.2.1)`.

In the general case, we shall introduce in place of `𝒪_{S'}` a complex `𝒬_•'` of `𝒪_{S'}`-modules quasi-coherent
*bounded below*, so that if, to simplify, one takes `I = {1, 2, …, m}`, one may consider the ∂-functor

```text
  𝒯or^S_•(f_1, …, f_m, 1_{S'}; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}, 𝒬_•').
```

**Proposition (6.9.3).**

<!-- label: III.6.9.3 -->

— *There exist three canonical biregular spectral functors denoted `^{(t)}𝓔(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}, 𝒬_•')`
(with `t = e`, `f` or `f'`) having for common abutment `𝒯or^S_•(f_1, …, f_m, 1_{S'}; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}, 𝒬_•')` and
whose `E_2` terms are respectively*

<!-- original page 35 -->

```text
  (e)   ^{(e)}𝓔^2_{pq} = ⊕_{q' + q'' = q} 𝒯or^S_p(𝒯or^S_{q'}(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}),
                                                  ℋ_{q''}(𝒬_•'))

  (f)   ^{(f)}𝓔^2_{pq} = ⊕_{q_1 + ⋯ + q_{m+1} = q} 𝒯or^{S'}_p(𝒯or^S_{q_1}(f_1, 1_{S'}; 𝒫_•^{(1)}, 𝒪_{S'}), …,
                                                              𝒯or^S_{q_m}(f_m, 1_{S'}; 𝒫_•^{(m)}, 𝒪_{S'}),
                                                              ℋ_{q_{m+1}}(𝒬_•'))

  (f')  ^{(f')}𝓔^2_{pq} = ⊕_{q_1 + ⋯ + q_m = q} 𝒯or^{S'}_p(f_1', …, f_m', 1_{S'}; 𝒯or^S_{q_1}(𝒫_•^{(1)}, 𝒪_{S'}), …,
                                                           𝒯or^S_{q_m}(𝒫_•^{(m)}, 𝒪_{S'}), 𝒬_•').
```

The sequence `(e)` is none other than the associativity sequence of `(6.8.2)` for `r = m`. To define the other two
spectral sequences, we shall again restrict to the case where `S`, `S'` and the `Y^{(i)}` are affine, the passage to the
general case being done by the methods of `(6.7.1)` and `(6.7.2)` and being left to the reader. We shall therefore prove
the

**Corollary (6.9.4).**

<!-- label: III.6.9.4 -->

— *Let `A` be a ring, `A'` an `A`-algebra, `S = Spec(A)`, `S' = Spec(A')`, `X^{(i)}` `(1 ≤ i ≤ m)` `S`-schemes
quasi-compact and for each `i`, let `X'^{(i)} = X^{(i)}_{(S')}`, which is a quasi-compact `S'`-scheme. For each `i`, let
`𝒫_•^{(i)}` be a complex of `𝒪_{X^{(i)}}`-modules quasi-coherent; let finally `Q_•'` be a complex of `A'`-modules, these
complexes being bounded below. There exist three biregular spectral functors in the `𝒫_•^{(i)}` and in `Q_•'`, having
for common abutment*

```text
  Tor^S_•(X^{(1)}, …, X^{(m)}, S'; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}, Q_•')
```

*and whose `E_2` terms are respectively*

```text
  (e)   ^{(e)}E^2_{pq} = ⊕_{q' + q'' = q} Tor^A_p(Tor^S_{q'}(X^{(1)}, …, X^{(m)}; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}),
                                                  H_{q''}(Q_•'))

  (f)   ^{(f)}E^2_{pq} = ⊕_{q_1 + ⋯ + q_{m+1} = q} Tor^{A'}_p(Tor^S_{q_1}(X^{(1)}, S'; 𝒫_•^{(1)}, 𝒪_{S'}), …,
                                                              Tor^S_{q_m}(X^{(m)}, S'; 𝒫_•^{(m)}, 𝒪_{S'}),
                                                              H_{q_{m+1}}(Q_•'))

  (f')  ^{(f')}E^2_{pq} = ⊕_{q_1 + ⋯ + q_m = q} Tor^{A'}_p(X'^{(1)}, …, X'^{(m)}, S';
                                                           𝒯or^S_{q_1}(𝒫_•^{(1)}, 𝒪_{S'}), …,
                                                           𝒯or^S_{q_m}(𝒫_•^{(m)}, 𝒪_{S'}), Q_•').
```

We shall not return to the first of these spectral functors, which has been treated in `(6.8.3)` and is included here
only for the record. To define the others, consider for each `i` a finite affine open cover `𝔘^{(i)}` of `X^{(i)}`, and,
if `u_i : X'^{(i)} → X^{(i)}` is the canonical projection, the corresponding finite affine open cover
`𝔘'^{(i)} = u_i^{-1}(𝔘^{(i)})`. By virtue of `(6.6.6)`,
`Tor^S_•(X^{(1)}, …, X^{(m)}, S'; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}, Q_•')` is obtained by taking for `1 ≤ i ≤ m` a projective
Cartan–Eilenberg resolution `M_{•,•,•}^{(i)}` of `L_{•,•}^{(i)} = C^•(𝔘^{(i)}, 𝒫_•^{(i)})` (in the sense of
`(0_III, 11.7.1)`), considering the tricomplex
`M_{•,•,•} = M_{•,•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)} ⊗ ⋯ ⊗_A M_{•,•,•}^{(m)} ⊗_A Q_•'` (where `Q_•'` is regarded as a
tricomplex whose two last degrees reduce to `0`), and taking its homology. If one sets
`M_{•,•,•}'^{(i)} = M_{•,•,•}^{(i)} ⊗_A A'`, one has (recalling that `Q_•'` is a complex of `A'`-modules)
`M_{•,•,•} = M_{•,•,•}'^{(1)} ⊗_{A'} M_{•,•,•}'^{(2)} ⊗ ⋯ ⊗_{A'} M_{•,•,•}'^{(m)} ⊗_{A'} Q_•'`. Now, consider each of
the complexes `M_{•,•,•}'^{(i)}` as a simple complex (with respect to its total degree) and note that this complex is
formed of `A'`-modules *projective*; it follows from `(6.3.7)` (extended to an arbitrary number of complexes) that
`H_•(M_{•,•,•})` is also equal to `Tor^{A'}_•(M_{•,•,•}'^{(1)}, …, M_{•,•,•}'^{(m)}, Q_•')`; it is therefore `(6.5.15)`
the abutment of a spectral sequence having the desired regularity properties (the three degrees of `M_{•,•,•}^{(i)}`
being bounded below when `𝒫_•^{(i)}` is bounded below) and whose `E_2` term is given by

```text
  E^2_{pq} = ⊕_{q_1 + ⋯ + q_{m+1} = q} Tor^{A'}_p(H_{q_1}(M_{•,•,•}'^{(1)}), …, H_{q_m}(M_{•,•,•}'^{(m)}),
                                                  H_{q_{m+1}}(Q_•')).
```

<!-- original page 36 -->

One has, moreover,
`H_{q_i}(M_{•,•,•}'^{(i)}) = H_{q_i}(M_{•,•,•}^{(i)} ⊗_A A') = Tor^S_{q_i}(X^{(i)}, S'; 𝒫_•^{(i)}, 𝒪_{S'})` by virtue of
the definition of the global hypertor, which gives the sequence `(f)` sought. One may on the other hand consider
`M_{•,•,•}'^{(i)}` as a bicomplex in which the first degree is the sum of the first and second degrees of the tricomplex
`M_{•,•,•}^{(i)}`, the second degree being the third degree of this tricomplex; since the modules forming the
`M_{•,•,•}'^{(i)}` are projective `A'`-modules, the general theory of hyperhomology shows that the homology of the
bicomplex `M_{•,•,•}'^{(1)} ⊗_{A'} M_{•,•,•}'^{(2)} ⊗ ⋯ ⊗_{A'} M_{•,•,•}'^{(m)} ⊗_{A'} Q_•'` is canonically isomorphic
to its hyperhomology `(0_III, 11.6.5)`; it is therefore the abutment of a spectral sequence with `E_2` term equal to

```text
  E^2_{pq} = ⊕_{q_1 + ⋯ + q_{m+1} = q} Tor^{A'}_p(H^{II}_{q_1}(M_{•,•,•}'^{(1)}), …,
                                                  H^{II}_{q_m}(M_{•,•,•}'^{(m)}), H^{II}_{q_{m+1}}(Q_•')).
```

Now, since the second degree of `Q_•'` reduces to `0`, one has `H^{II}_n(Q_•') = 0` for `n ≠ 0` and
`H^{II}_0(Q_•') = Q_•'`; the preceding formula is also written

```text
  E^2_{pq} = ⊕_{q_1 + ⋯ + q_m = q} Tor^{A'}_p(H^{II}_{q_1}(M_{•,•,•}'^{(1)}), …,
                                              H^{II}_{q_m}(M_{•,•,•}'^{(m)}), Q_•').
```

Moreover, one has
`H^{II}_{q_i}(M_{•,•,•}'^{(i)}) = H^{II}_{q_i}(M_{•,•,•}^{(i)} ⊗_A A') = Tor^A_{q_i}(L_{•,•}^{(i)}, A')` by virtue of
`(6.3.4)`; but `L_{•,•}^{(i)} = C^•(𝔘^{(i)}, 𝒫_•^{(i)})`, direct sum of the `Γ(V, 𝒫_•^{(i)})`, where `V` runs through
the (affine) intersections of `j + 1` sets of the cover `𝔘^{(i)}`; if `V' = u_i^{-1}(V)`, `V'` is affine in `X'^{(i)}`,
and it follows from `(6.4.1.1)` that one has

```text
  Γ(V', 𝒯or^S_{q_i}(𝒫_•^{(i)}, 𝒪_{S'})) = Tor^A_{q_i}(Γ(V, 𝒫_•^{(i)}), A')
```

whence for the bicomplex `H^{II}_{q_i}(M_{•,•,•}'^{(i)})` the expression

```text
  C^•(𝔘'^{(i)}, 𝒯or^S_{q_i}(𝒫_•^{(i)}, 𝒪_{S'}))
```

which gives finally the desired expression for the `E_2` term of the sequence `(f')`. The fact that this sequence is
biregular under the conditions indicated is verified as usual, taking into account that, if `𝒫_•^{(i)}` is bounded
below, all the degrees of `M_{•,•,•}^{(i)}` are bounded below.

**Remark (6.9.5).**

<!-- label: III.6.9.5 -->

One sees as in `(6.7.6)` that the replacement of the `𝒫_•^{(i)}` and of `𝒬_•'` by complexes which are respectively
*homotopic* to them does not change the sequences `(e)`, `(f)` and `(f')` up to canonical isomorphism. Moreover, for the
sequence `(f)`, homomorphisms `𝒫_•^{(i)} → ℛ_•^{(i)}`, `𝒬_•' → 𝒯_•'` of complexes which give isomorphisms in homology
`ℋ_•(𝒫_•^{(i)}) ⥲ ℋ_•(ℛ_•^{(i)})`, `ℋ_•(𝒬_•') ⥲ ℋ_•(𝒯_•')` yield an isomorphism of spectral sequences
`^{(f)}𝓔(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}, 𝒬_•') ⥲ ^{(f)}𝓔(f_1, …, f_m; ℛ_•^{(1)}, …, ℛ_•^{(m)}, 𝒯_•')`; the proof
is the same as for `(6.7.6)` taking into account the result of `(6.7.6)` and the regularity of the sequence `(f)`.

**Corollary (6.9.6).**

<!-- label: III.6.9.6 -->

— *Under the conditions of `(6.9.1)`, suppose that:*

*1° The complexes `𝒫_•^{(i)}` are formed of modules flat over `S`, and the `𝒪_Y`-modules*

```text
  𝒯or^S_n(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})
```

*are flat over `S`.*

*2° The `𝒫_•^{(i)}` and `𝒬_•'` are bounded below.*

<!-- original page 37 -->

*One has then, setting `𝒫_•'^{(i)} = 𝒫_•^{(i)} ⊗_{𝒪_S} 𝒪_{S'}`, canonical functorial isomorphisms*

```text
  𝒯or^{S'}_n(f_1', …, f_m', 1_{S'}; 𝒫_•'^{(1)}, …, 𝒫_•'^{(m)}, 𝒬_•')                       (6.9.6.1)
        ⥲ ⊕_{n' + n'' = n} 𝒯or^S_{n'}(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}) ⊗_{𝒪_S} ℋ_{n''}(𝒬_•').
```

*In particular, for `𝒬_•'` reduced to a single term `ℱ'` of degree `0`, one has canonical functorial isomorphisms*

```text
  𝒯or^{S'}_n(f_1', …, f_m', 1_{S'}; 𝒫_•'^{(1)}, …, 𝒫_•'^{(m)}, ℱ')                         (6.9.6.2)
        ⥲ 𝒯or^S_n(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}) ⊗_{𝒪_S} ℱ'
```

*and more particularly, for `ℱ' = 𝒪_{S'}`,*

```text
  𝒯or^{S'}_n(f_1', …, f_m'; 𝒫_•'^{(1)}, …, 𝒫_•'^{(m)})                                     (6.9.6.3)
        ⥲ 𝒯or^S_n(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}) ⊗_{𝒪_S} 𝒪_{S'}.
```

The flatness hypothesis on the modules composing the `𝒫_•^{(i)}` entails that the complexes
`𝒯or^S_{q_i}(𝒫_•^{(i)}, 𝒪_{S'})` are zero for `q_i ≠ 0` `(6.5.8)`. The sequence `(f')` is therefore degenerate;
hypothesis 2° entails moreover that it is biregular `(6.9.3)`, so the edge homomorphism

```text
  𝒯or^{S'}_n(f_1', …, f_m', 1_{S'}; 𝒫_•'^{(1)}, …, 𝒫_•'^{(m)}, 𝒬_•') → ^{(f')}𝓔^2_{n0}      (6.9.6.4)
        = 𝒯or^{S'}_n(f_1', …, f_m', 1_{S'}; 𝒫_•'^{(1)}, …, 𝒫_•'^{(m)}, 𝒬_•')
```

is bijective `(0_III, 11.1.6)`. The flatness hypothesis on the modules

```text
  𝒯or^S_n(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})
```

entails that `^{(e)}𝓔^2_{pq} = 0` for `p ≠ 0` `(6.5.8)`. The sequence `(e)` is therefore also degenerate, and since it
is biregular, the edge homomorphism

```text
  𝒯or^{S'}_n(f_1, …, f_m, 1_{S'}; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}, 𝒬_•') → ^{(e)}𝓔^2_{0n}          (6.9.6.5)
        = ⊕_{n' + n'' = n} 𝒯or^S_{n'}(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}) ⊗_{𝒪_S} ℋ_{n''}(𝒬_•')
```

is bijective `(0_III, 11.1.6)`; whence, by combining the two preceding isomorphisms, the isomorphism `(6.9.6.1)`. The
isomorphism `(6.9.6.2)` is deduced trivially, since one has then `ℋ_n(𝒬_•') = 0` if `n ≠ 0` and `ℋ_0(𝒬_•') = ℱ'`.
Finally, the case `ℱ' = 𝒪_{S'}` in `(6.9.6.2)` gives the isomorphism `(6.9.6.3)`, taking `(6.7.12)` into account.

**Corollary (6.9.7).**

<!-- label: III.6.9.7 -->

— *Under the conditions of `(6.9.1)`, suppose `S` and `S'` affine, and suppose given for each `i` an integer `d_i`
`(1 ≤ i ≤ m)`. There then exists an integer `N` depending only on `S`, the `X^{(i)}` and the `d_i`, having the following
property: for every integer `n_0`, one has canonical isomorphisms `(6.9.6.3)` for `n ≤ n_0` and for every system of
complexes `𝒫_•^{(i)}` verifying the following conditions: 1° `𝒫_k^{(i)} = 0` for `k < d_i`; 2° `𝒫_k^{(i)}` is flat over
`S` for `k < n_0 + N`; 3° `𝒯or^S_q(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})` is flat over `S` for `q < n_0 + N`.*

Suppose `𝒫_k^{(i)}` flat over `S` for `k < r`; then `𝒯or^S_{q_i}(𝒫_k^{(i)}, 𝒪_{S'}) = 0` for `k < r` and `q_i ≠ 0`; let
us compute

```text
  𝒯or^{S'}_p(f_1', …, f_m'; 𝒯or^S_{q_1}(𝒫_•^{(1)}, 𝒪_{S'}), …, 𝒯or^S_{q_m}(𝒫_•^{(m)}, 𝒪_{S'}))         (6.9.7.1)
```

<!-- original page 38 -->

by the method of `(6.6.2)`, with the help of the inverse image of a fixed affine cover `𝔘^{(i)}` of `X^{(i)}` `(i ≤ m)`
(independent of `S'` and of the `𝒫_•^{(i)}`); the terms `L_{•,•}^{(i)}` are zero for `j < −N_i` (depending only on
`𝔘^{(i)}`); if one of the `q_i` is non-zero, the simple complex whose homology of degree `p` is `(6.9.7.1)` has its
terms zero for all degrees `< r + Σ_{j ≠ i} d_j − Σ_{i=1}^m N_i`, hence `(6.9.7.1)` is zero for `p < r − N`, denoting by
`N` the largest of the numbers `Σ_{i=1}^m N_i − Σ_{j ≠ i} d_j`. One concludes from this that one has
`^{(f')}𝓔^2_{pq} = 0` for `q ≠ 0` and `p < r − N`; since on the other hand `^{(f')}𝓔^2_{pq} = 0` for `q < 0`, one sees
that the edge homomorphism `(6.9.6.4)` is bijective for `n < r − N` `(M, XV, 5.6)` (for `𝒬_•' = 𝒪_{S'}`). In the second
place, if `𝒯or^S_q(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})` is flat over `S` for `q < r`, one has `^{(e)}𝓔^2_{pq} = 0` for
`p ≠ 0` and `q < r`; on the other hand `^{(e)}𝓔^2_{pq} = 0` for `p < 0`, so the edge homomorphism `(6.9.6.5)` is
bijective for `n < r`, which completes the proof.

The most important case of `(6.9.3)` in the applications is that where `m = 1`, `𝒬_•'` being reduced to a single term
`ℱ'` of degree `0`; we shall state it again in this case in view of later references[^1]:

**Proposition (6.9.8).**

<!-- label: III.6.9.8 -->

— *Let `S` be a prescheme, `g : S' → S` a morphism, `f : X → Y` a separated and quasi-compact `S`-morphism of
`S`-preschemes, `𝒫_•` a complex of `𝒪_X`-modules quasi-coherent bounded below, `ℱ'` a quasi-coherent `𝒪_{S'}`-module.
There exist two biregular spectral functors in `𝒫_•` and `ℱ'`, with values in the category of `𝒪_{Y_{(S')}}`-modules
quasi-coherent, having the same abutment `𝒯or^S_•(f, 1_{S'}; 𝒫_•, ℱ')`, and whose `E_2` terms are*

```text
  ^{('e)}𝓔^2_{pq} = 𝒯or^S_p(ℋ^{-q}(f, 𝒫_•), ℱ')                                            (6.9.8.1)
  ^{(''e)}𝓔^2_{pq} = ℋ^{-p}(f', 𝒯or^S_q(𝒫_•, ℱ')),                                         (6.9.8.2)
```

*where `f' = f_{(S')} : X_{(S')} → Y_{(S')}`.*

The sequences in question can also be obtained, not starting from `(6.9.3)`, but from the sequences `(a)` and `(b')` of
`(6.7.3)` for `X^{(1)} = X`, `Y^{(1)} = Y`, `X^{(2)} = Y^{(2)} = S'`, `f_1 = f`, `f_2 = 1_{S'}`. When `S = S' = Y`, `Y`
being affine, one obtains two spectral sequences with `E_2` terms equal to

```text
  ^{('e)}𝓔^2_{pq} = 𝒯or^Y_p(ℋ^{-q}(f, 𝒫_•), ℱ)                                             (6.9.8.3)
  ^{(''e)}𝓔^2_{pq} = ℋ^{-p}(f, 𝒯or^Y_q(𝒫_•, ℱ))                                            (6.9.8.4)
```

abutting (by virtue of `(6.7.6)`) to the hypercohomology `ℋ^•(f, 𝒫_• ⊗_Y ℱ)` of the functor `f_*` with respect to the
complex `𝒫_• ⊗_Y ℱ` of `𝒪_X`-modules, for every `𝒪_Y`-module quasi-coherent and `Y`-flat `ℱ` (or for every `𝒪_Y`-module
quasi-coherent `ℱ` when `𝒫_•` is formed of `𝒪_X`-modules `Y`-flat), which are distinct from those of `(6.2.1)`.

**Corollary (6.9.9).**

<!-- label: III.6.9.9 -->

— *Under the conditions of `(6.9.8)`, suppose that the complex `𝒫_•` is bounded below, formed of modules flat over `S`,
and that the `𝒪_Y`-modules `ℋ^n(f, 𝒫_•)` are flat over `S`.*

<!-- original page 39 -->

*One has then canonical functorial isomorphisms*

```text
  𝒯or^{S'}_•(f', 1_{S'}; 𝒫_•', ℱ') ⥲ ℋ^•(f, 𝒫_•) ⊗_{𝒪_S} ℱ'                                (6.9.9.1)
```

*where `𝒫_•' = 𝒫_• ⊗_{𝒪_S} 𝒪_{S'}`; in particular, for `ℱ' = 𝒪_{S'}`, one has canonical functorial isomorphisms*

```text
  ℋ^•(f', 𝒫_•') ⥲ ℋ^•(f, 𝒫_•) ⊗_{𝒪_S} 𝒪_{S'}.                                              (6.9.9.2)
```

This is the particular case `m = 1` of `(6.9.6)`. More particularly:

**Corollary (6.9.10).**

<!-- label: III.6.9.10 -->

— *Let `S` be a prescheme, `f : X → Y` a separated and quasi-compact `S`-morphism of `S`-preschemes, `𝒫_•` a complex
bounded below, formed of `𝒪_X`-modules quasi-coherent, flat over `S`. Suppose moreover that the `𝒪_Y`-modules
`ℋ^n(f, 𝒫_•)` are flat over `S`. For every `s ∈ S`, denote by `X_s` and `Y_s` the fibres `X ⊗_S k(s)`, `Y ⊗_S k(s)`,
`f_s : X_s → Y_s` the morphism `f ×_S 1`, `𝒫_•^{(s)}` the complex `𝒫_• ⊗_S k(s)` of `𝒪_{X_s}`-modules. One has then
canonical functorial isomorphisms*

```text
  ℋ^•(f_s, 𝒫_•^{(s)}) ⥲ ℋ^•(f, 𝒫_•) ⊗_S k(s).                                              (6.9.10.1)
```

One thus has, under suitable flatness hypotheses, a case where the formation of the derived functors `R^n f_*(𝒫_•)`
"commutes with passage to fibres", which we shall recover by another method in §7.

*(To be continued.)*

# §6 (continued). Local and global Tor functors; the Künneth formula

> _Translator's note._ This file is the closing subsection of §III.6, translated as a separate piece for length. The
> opening (§6.1–§6.6) and middle (§6.7–§6.9) are in the companion Part-A and Part-B files. They will be concatenated for
> the final volume.

<!-- original page 39 -->

## 6.10. Local structure of certain cohomological functors.

**Proposition (6.10.1).**

<!-- label: III.6.10.1 -->

— *Let `S = Spec(A)` be an affine scheme, `Y^{(i)}` `(1 ≤ i ≤ n)` a finite family of affine `S`-schemes, flat over `S`;
for each `i`, let `f_i : X^{(i)} → Y^{(i)}` be a separated and quasi-compact `S`-morphism, and let `𝒫_•^{(i)}` be a
complex of `𝒪_{X^{(i)}}`-modules quasi-coherent, bounded below. Let `Y` be the product of the `S`-schemes `Y^{(i)}`.
There exists a complex `𝒦_•` of `𝒪_Y`-modules quasi-coherent and flat over `S`, having the following property: for every
affine `S`-scheme `S'` and every complex `ℱ_•'` of `𝒪_{S'}`-modules quasi-coherent, bounded below, there is an
isomorphism*

```text
  𝒯or^S_•(f_1, …, f_n, 1_{S'}; 𝒫_•^{(1)}, …, 𝒫_•^{(n)}, ℱ_•') ⥲ ℋ_•(𝒦_• ⊗_S ℱ_•')         (6.10.1.1)
```

*which is an isomorphism of `∂`-functors in `ℱ_•'`. Moreover, for every `S`-morphism `u : S'' → S'` of affine
`S`-schemes, the diagram*

```text
  𝒯or^S_•(f_1, …, f_n, 1_{S'}; 𝒫_•^{(1)}, …, 𝒫_•^{(n)}, ℱ_•')           ⥲   ℋ_•(𝒦_• ⊗_S ℱ_•')

                       │                                                              │           (6.10.1.2)
                       ↓                                                              ↓

  𝒯or^S_•(f_1, …, f_n, 1_{S''}; 𝒫_•^{(1)}, …, 𝒫_•^{(n)}, u^*(ℱ_•'))     ⥲   ℋ_•(𝒦_• ⊗_S u^*(ℱ_•'))
```

*(where the vertical arrows are the canonical `(𝒪_Y, 𝒪_S)`-morphisms defined in `(6.7.10)`) is commutative.*

**Proof.** We compute the hypertor by the method of `(6.6.2)`, taking remark `(6.6.6)` into account; with the notations
of `(6.6.2)`, each `L_{•,•}^{(i)}` is a bicomplex of `A_i`-modules, where we denote by `A_i` the ring of `Y^{(i)}`; it
therefore admits a projective Cartan–Eilenberg resolution `M_{•,•,•}^{(i)}` (in the sense of `(0_III, 11.7.1)`) formed
of `A_i`-modules, and by virtue of `(6.6.6)`, the first member of `(6.10.1.1)` is canonically isomorphic to
`H_•(M_{•,•,•} ⊗_A Q_•)`, where

```text
  M_{•,•,•} = M_{•,•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)} ⊗_A ⋯ ⊗_A M_{•,•,•}^{(n)}     and    Q_• = ℱ_•'.
```

Since, by hypothesis, the rings `A_i` are flat `A`-modules, the `M_{•,•,•}^{(i)}` are tricomplexes of flat `A`-modules
`(0_I, 6.2.1)`, and the same holds for `M_{•,•,•}`; moreover, if `B` is the ring of `Y`, tensor product of the `A_i`,
`M_{•,•,•}` is a tricomplex of `B`-modules; the complex `𝒦_• = (M_{•,•,•})^{~}` of `𝒪_Y`-modules (where `M_{•,•,•}` is

<!-- original page 40 -->

considered as a simple complex) therefore answers the question, as follows easily from `(6.7.10)`. ∎

**Corollary (6.10.2).**

<!-- label: III.6.10.2 -->

— *In the statement of `(6.10.1)`, one may suppose `𝒦_•` bounded below. When the `𝒫_•^{(i)}` are bounded above and the
`Y^{(i)}` of finite cohomological dimension, one may suppose `𝒦_•` bounded above.*

**Proof.** The first assertion follows from the fact that the three degrees of each of the `M_{•,•,•}^{(i)}` are bounded
below; on the other hand, if the rings `A_i` are of finite cohomological dimension, the third degree of each of the
`M_{•,•,•}^{(i)}` takes only finitely many values, and the same is true by construction of its first degree `(6.6.2)`;
since its second degree is bounded above provided that the degree of `𝒫_•^{(i)}` is bounded above `(6.6.2)`, the second
assertion follows at once. ∎

**Remarks (6.10.3).**

<!-- label: III.6.10.3 -->

— (i) With the notations of `(6.10.1)`, `ℋ_•(𝒦_• ⊗_S ℱ_•')` is isomorphic to `𝒯or_•(𝒦_•, ℱ_•')` since `𝒦_•` is formed of
`S`-flat `𝒪_Y`-modules `(6.5.9)`; it is therefore `(6.5.4)` the abutment of a regular spectral sequence with `E_2` term
given by

```text
  ^{(e)}𝓔^2_{pq} = ⊕_{q' + q'' = q} 𝒯or^S_p(ℋ_{q'}(𝒦_•), ℋ_{q''}(ℱ_•'))                       (6.10.3.1)
```

which is none other than the base-change spectral sequence `(e)` of `(6.9.3)`.

(ii) Let `𝒦_•'` be a second complex of `𝒪_Y`-modules quasi-coherent, flat over `S`, and let `g : 𝒦_• → 𝒦_•'` be a
homomorphism of complexes such that `ℋ_•(g) : ℋ_•(𝒦_•) → ℋ_•(𝒦_•')` is an isomorphism. Then, by virtue of `(6.3.3)` and
`(6.5.9)`, one deduces from `g` an isomorphism of `∂`-functors in `ℱ_•'`: `ℋ_•(𝒦_• ⊗_S ℱ_•') ⥲ ℋ_•(𝒦_•' ⊗_S ℱ_•')` such
that the diagram

```text
  ℋ_•(𝒦_• ⊗_S ℱ_•')           ⥲           ℋ_•(𝒦_•' ⊗_S ℱ_•')

           │                                       │

           ↓                                       ↓

  ℋ_•(𝒦_• ⊗_S u^*(ℱ_•'))      ⥲           ℋ_•(𝒦_•' ⊗_S u^*(ℱ_•'))
```

is commutative. This therefore proves that the complex `𝒦_•` is *not entirely determined* by the properties of
`(6.10.1)`.

<!-- original page 41 -->

(iii) In the proof of `(6.10.1)`, one may suppose the `M_{•,•,•}^{(i)}` formed of *free* `A_i`-modules (as follows
easily from the proof of `(0_III, 11.5.2.1)` "dualized"); the `M_{•,•,•}^{(i)} ⊗_A B` are then formed of free
`B`-modules, and since `M_{•,•,•}` is equal to their tensor product over `B`, one sees that one may further suppose in
`(6.10.1)` that `𝒦_•` is associated to a complex of *free* `B`-modules. Moreover, by virtue of `(M, XVII, 1.2)`, the
tricomplex `M_{•,•,•}` depends functorially on each of the bicomplexes `L_{•,•}^{(i)}` (hence on each of the
`𝒫_•^{(i)}`, once one fixes a finite cover of each of the `X^{(i)}`), the "morphisms" of tricomplexes being here
understood as the classes of homomorphisms for the homotopy relation; moreover, replacing a cover of `X^{(i)}` by a
finer cover gives rise for the `L_{•,•}^{(i)}` to homomorphisms defined precisely up to homotopy `(6.6.8)`, so one sees
finally that, with the preceding convention for morphisms, the tricomplex `M_{•,•,•}` is a *functor* in each of the
`𝒫_•^{(i)}`. We shall make this functorial dependence precise, and in particular the behaviour of `𝒦_•` with respect to
exact sequences `0 → 𝒫_•^{(i)} → 𝒬_•^{(i)} → ℛ_•^{(i)} → 0` of complexes, in the chapter devoted to a general algebra of
cohomological functors, mentioned in `(6.1.3)`.

**Scholium (6.10.4).**

<!-- label: III.6.10.4 -->

— The fact that `𝒦_•` is formed of `S`-flat `𝒪_Y`-modules implies easily that `ℋ_•(𝒦_• ⊗_S ℱ_•')` is a *homological
functor* in `ℱ_•'` (see the argument of `(7.7.1)`). It is this property which, as has been mentioned in `(6.1.1)`, is
the motivation for the introduction of hypertor. Indeed, set

```text
  X = X^{(1)} ×_S X^{(2)} ×_S ⋯ ×_S X^{(n)},   f = f_1 ×_S f_2 ×_S ⋯ ×_S f_n,
  𝒫_• = 𝒫_•^{(1)} ⊗_S 𝒫_•^{(2)} ⊗_S ⋯ ⊗_S 𝒫_•^{(n)},
  X' = X ×_S S',   Y' = Y ×_S S',   f' = f ×_S 1_{S'};
```

the base-change problems lead one to study the hypercohomology `ℋ_•(f', 𝒫_•' ⊗_S ℱ')` as a functor with respect to the
quasi-coherent `𝒪_{S'}`-module `ℱ'`, or equivalently the hypercohomology `ℋ_•(f, 𝒫_• ⊗_S ℱ)` as a functor in the
quasi-coherent `𝒪_S`-module `ℱ`. When the `𝒫_•^{(i)}` (hence also `𝒫_•`) are `S`-flat, it follows from what precedes and
from `(6.7.6)` that this functor is indeed a *cohomological functor* in `ℱ`; but this is no longer the case when one
drops the flatness hypothesis on the `𝒫_•^{(i)}`, and one can then no longer approach the study of `ℋ_•(f, 𝒫_• ⊗_S ℱ)`
by the usual methods of Homological Algebra.

We shall however have above all to use the case where `n = 1`, `Y = S`, and where `𝒫_•` is formed of `Y`-flat
`𝒪_X`-modules. We have in this case the

**Theorem (6.10.5).**

<!-- label: III.6.10.5 -->

— *Let `Y = Spec(A)` be a noetherian affine scheme, `f : X → Y` a proper morphism, `𝒫_•` a complex of `𝒪_X`-modules
coherent, flat over `Y`, bounded below. There then exists a complex `ℒ_•` of `𝒪_Y`-modules, bounded below, whose terms
`ℒ_i` are `𝒪_Y`-modules of the form `𝒪_Y^{n_i}`, and an isomorphism*

```text
  ℋ^•(f, 𝒫_• ⊗_Y 𝒬_•) ⥲ ℋ_•(ℒ_• ⊗_Y 𝒬_•)                                                   (6.10.5.1)
```

*of `∂`-functors in the complex `𝒬_•` of `𝒪_Y`-modules quasi-coherent, bounded below. Moreover, for every morphism
`u : Y' → Y`, setting*

```text
  X' = X_{(Y')},   f' = f_{(Y')},   𝒫_•' = 𝒫_• ⊗_Y 𝒪_{Y'},   ℒ_•' = u^*(ℒ_•)
```

<!-- original page 42 -->

*(which is a complex of `𝒪_{Y'}`-modules locally free of finite type), one has an isomorphism*

```text
  ℋ^•(f', 𝒫_•' ⊗_{Y'} 𝒬_•') ⥲ ℋ_•(ℒ_•' ⊗_{Y'} 𝒬_•')                                         (6.10.5.2)
```

*of `∂`-functors in the complex `𝒬_•'` of `𝒪_{Y'}`-modules quasi-coherent, bounded below, in such a way that the
diagram*

```text
  ℋ^•(f, 𝒫_• ⊗_Y 𝒬_•)              ⥲              ℋ_•(ℒ_• ⊗_Y 𝒬_•)

           │                                              │                                  (6.10.5.3)

           ↓                                              ↓

  ℋ^•(f', 𝒫_•' ⊗_{Y'} u^*(𝒬_•))    ⥲              ℋ_•(ℒ_•' ⊗_{Y'} u^*(𝒬_•))
```

*is commutative.*

**Proof.** The application of `(6.10.1)` gives first a complex `𝒦_•`, bounded below `(6.10.2)`, of quasi-coherent and
`Y`-flat `𝒪_Y`-modules `(6.10.3, (iii))` and an isomorphism

```text
  ℋ^•(f, 𝒫_• ⊗_Y 𝒬_•) ⥲ ℋ_•(𝒦_• ⊗_Y 𝒬_•)                                                   (6.10.5.4)
```

of `∂`-functors in `𝒬_•`, but *a priori* the terms of `𝒦_•` are not necessarily `𝒪_Y`-modules of finite type. But if one
applies `(6.10.5.4)` to the case where `𝒬_•` is a complex reduced to a single term `𝒪_Y`, one sees that `ℋ_•(𝒦_•)` is
isomorphic to `ℋ^•(f, 𝒫_•)`, and is consequently formed of *coherent* `𝒪_Y`-modules `(6.2.5)`. One knows then
`(0_III, 11.9.2)` that there exists a complex `ℒ_•`, bounded below, formed of `𝒪_Y`-modules associated to *free
`A`-modules of finite type*, and a homomorphism `ℒ_• → 𝒦_•`, such that the corresponding homomorphism for homology,
`ℋ_•(ℒ_•) → ℋ_•(𝒦_•)`, is bijective; whence the isomorphism `(6.10.5.1)`, by virtue of `(6.10.3, (ii))`. The other
assertions of `(6.10.5)` follow from `(6.10.1)` and `(6.10.3, (ii))` *when `Y'` is affine*; in the general case, it
suffices to verify that, when one considers a cover `(V_α)` of `Y'` by affine opens, and the corresponding isomorphism
`(6.10.5.2)` relative to each of the `V_α`, the restrictions to an affine open `W ⊂ V_α ∩ V_β` of the isomorphisms
corresponding to `V_α` and to `V_β` *coincide* with the isomorphism corresponding to `W`, which follows from the
commutativity of the diagram `(6.10.1.2)` applied to the canonical injections `W → V_α` and `W → V_β`. ∎

**Remark (6.10.6).**

<!-- label: III.6.10.6 -->

— In the following chapters, we shall apply `(6.10.5)` above all to the case where `𝒫_•` is reduced to a single coherent
`𝒪_X`-module `ℱ`, flat over `Y`. Since one then has `ℋ_n(ℒ_•) = ℋ^{-n}(f, ℱ) = R^{-n} f_*(ℱ)` `(6.2.1)`, one sees that
the `ℋ_n(ℒ_•)` are zero for `n > 0`; we shall see later `(7.7.12, (i))` that one may then suppose that `ℒ_•` has only
terms of degrees `≥ 0` (hence finitely many), provided that one replaces the hypothesis that the `ℒ_i` are associated to
free `A`-modules of finite type by the hypothesis that the `ℒ_i` are *locally free of finite type*.

The complex `ℒ_•` corresponding to such an `𝒪_X`-module `ℱ` does not appear to possess any

<!-- original page 43 -->

particular property, beyond the preceding restriction on the degrees. One may then ask whether, conversely, given a
complex `ℒ_•` formed of `𝒪_Y`-modules associated to projective `A`-modules of finite type, bounded below and whose terms
of degree `> 0` are zero, there exists a `Y`-scheme `X`, projective and flat over `Y`, and an `𝒪_X`-module `ℱ` locally
free, such that there is an isomorphism `ℋ^•(f, ℱ ⊗_Y 𝒬_•) ⥲ ℋ_•(ℒ_• ⊗_Y 𝒬_•)` functorial in `𝒬_•`. The interest of such
a result would be to reduce completely the cohomological theory of `Y`-flat coherent modules on proper `Y`-schemes to
the theory "up to homotopy" of complexes of projective `A`-modules of finite type on a noetherian ring `A`.

[^1]: The case treated in `(6.9.8)`, and in particular the spectral sequences `(6.9.8.3)` and `(6.9.8.4)`, had been
    pointed out to us in 1957 by J.-P. Serre.

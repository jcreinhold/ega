<!-- original page 1 -->

## §V.5. Hyperplane sections and conic projections (formerly EGA IV §20) — part 1 of 2

This section was originally drafted as §20 of EGA IV, then re-allocated to EGA V (Chapter V §5) without ever being
published in either place. It is the longest single section of the prenotes. Because of its bulk we divide our
translation into two files: this **part 1** covers the introductory plan and §§V.5.1-V.5.8 (preliminaries, the generic
hyperplane section, sufficiently general hyperplane sections, Seidenberg-type theorems, connectedness of an arbitrary
hyperplane section, applications to the construction of special hyperplane sections and multisections, and the dimension
of the set of exceptional hyperplanes); **part 2** (the companion file `04-ch5-05-hyperplane-sections-part-2.md`) covers
§§V.5.9-V.5.16 (change of projective embedding, pencils of hyperplane sections, Grassmannians, linear sections, M.
Artin's theorem on elementary morphisms, conic projections, axiomatization, and translation into the language of linear
systems).

The §V↔§IV correspondence is given in the front matter; we lead with the V numbering and attach `(formerly IV, M)`
parenthetically at the first occurrence of each cross-reference into the old numbering.

> *Grothendieck note (placed at the head of the prenote as a summary).* This formulation gives, pell-mell,[^v-5p1-1] a
> detailed summary of the set of results that should appear in a final formulation. To arrive at the latter we need to
> reorganize thoroughly the present *stage zero*. The first step should probably be to make a new plan (in which without
> a doubt the present §§5.11, 5.12, 5.14, 5.15 will come much earlier). I have not even written §5.16, which should
> neither in principle cause any difficulty nor influence in any way the previous numbers, since what is involved is a
> simple matter of translation.[^v-5p1-2]
>
> You will notice the presence of a Proposition (5.10.3) which should appear in a previous paragraph.
>
> I would like to tell you in this connection that I have several other results, quite diverse but all dealing with
> birational mappings, that I would love to include somewhere. It seems to me that there is not enough material to make
> a paragraph on its own. Do you have a suggestion where to place them? I plan to send them to you soon, as well as
> §5.16 of the present notes.
>
> In addition, the present §V.5 (Paragraph 20) will probably blow up into two paragraphs, one consisting of results of
> "elementary-geometry" type on Grassmannians. If need be, could one include there also (lacking a better place) the
> supplements that I told you about dealing with birational transformations?

### Plan of §V.5

1. Preliminaries and notation (§V.5.1).

1. Generic hyperplane section: local properties (§V.5.2).

1. Generic hyperplane section: geometric irreducibility and connectedness (§V.5.3).

1. Variable hyperplane section: "sufficiently general" sections (§V.5.4).

1. Theorems of Seidenberg type (§V.5.5).

1. Connectedness of an arbitrary hyperplane section (§V.5.6).

1. Application to the construction of special hyperplane sections and multisections (§V.5.7).

1. Dimension of the set of exceptional hyperplanes (§V.5.8).

1. Change of projective embedding (§V.5.9).

1. Pencils of hyperplane sections and fibrations of blown-up varieties (§V.5.10).

1. Grassmannians (§V.5.11).

1. Generalization of the previously mentioned results to linear sections (§V.5.12).

1. Elementary morphisms and a theorem of M. Artin (§V.5.13).

1. Conic projections (§V.5.14).

1. Axiomatization of some of the previous results (§V.5.15).

1. Translation into the language of linear systems (§V.5.16).

Items 1-8 are treated in the present part 1; items 9-16 are treated in part 2.

<!-- original page 3 -->

### V.5.1. Preliminaries and notation

Let `S` be a prescheme, let `E` be a locally free module of finite type over `S`, and let `E^∨` be its dual. We denote
by `P = P(E) = ℙ(E)` the projective fibration defined by `E`, and by `P^∨ = ℙ(E^∨)` the projective fibration defined by
`E^∨`. We shall call `P^∨` the **scheme of hyperplanes** of `P`. This terminology can be justified as follows. Let `ξ`
be a section of `P^∨` over `S`, determined by an invertible quotient module `L` of `E^∨`. From it we obtain an
invertible quotient module `L_P` of `(E^∨)_P = (E_P)^∨`; on the other hand, we have the invertible quotient module
`𝒪_P(1)` of `E_P`. Passing to duals, we may take `L_P^{-1}` and `𝒪_P(-1)` to be invertible submodules (locally direct
factors) of `E_P` and of `(E_P)^∨` respectively, and the pairing `E_P ⊗ E_P^∨ → 𝒪_P` defines therefore a natural pairing

```text
  (*)                            𝒪_P(-1) ⊗ L_P^{-1} ⟶ 𝒪_P,
```

or equivalently the transposed homomorphism

```text
  (**)                           𝒪_P ⟶ 𝒪_P(1) ⊗ L_P = L_P(1),
```

that is, a section of `L_P(1)` canonically defined by `ξ`. The "divisor" of this section, i.e. the closed subscheme
`H_ξ` of `P` defined by the image ideal of `(*)`, is called the **hyperplane in `P` defined by the element**
`ξ ∈ P^∨(S)`. We could describe it by noting that, locally over `S`, `ξ` is given by a section `φ` of `E` such that
`φ(s) ≠ 0` for all `s` (`φ` is determined by `ξ` up to multiplication by an invertible section of `𝒪_S`); since
`E = p_*(𝒪_P(1))` (`p : P → S` being the projection), `φ` can be considered as a section of `𝒪_P(1)`, and the divisor of
this section is nothing else but `H_ξ`.

Of course, if we consider `L^{-1}` as an invertible submodule of `E`, locally a direct factor in `E`, then the
correspondence between `ξ` (that is, `L`, or `L^{-1} ⊂ E`) and `φ` is obtained by taking for `φ` a section of `L^{-1}`
which does not vanish at any point — i.e. by a trivialization of `L^{-1}` (which exists in every case locally). Let us
note that `H_ξ` is nothing else but `ℙ(E / L^{-1})` (canonical isomorphism); this is a third way of describing `H_ξ`.
*(N.B. `ℙ(E / L^{-1})` is indeed canonically embedded in `P = ℙ(E)`, which has the advantage of proving in addition that
`H_ξ` is a projective fibration over `S` and is a fortiori smooth over `S`. It would still be necessary to say in §17 of
EGA IV that a projective fibration is smooth.) Without a doubt it would be better to begin with this description.*

**Remarks (5.1.1).**

<!-- label: V.5.1.1 -->

*The formation of `H_ξ` is compatible with base change; in other words one finds a homomorphism of functors
`(Sch/S) → (Sets)`,*

```text
  P^∨ ⟶ Div(P/S),
```

*where the second term denotes the functor of "relative divisors" of `P/S`, whose value at an arbitrary `S`-prescheme
`S'` is the set of closed subschemes of `P_{S'}` which are complete intersections, transversal to and of codimension `1`
relative to `S'` (compare §V.19, formerly IV, 19).[^v-5p1-3]*

<!-- original page 4 -->

It is easy to show that this homomorphism of functors is a monomorphism — in other words, that `ξ` is determined by
`H_ξ`. (This last fact justifies the terminology "scheme of hyperplanes" used above.) We shall see that the functor
`Div(P/S)` is representable by the prescheme (direct) sum of the `ℙ(Sym^k(E^∨))`, so that `P^∨` can be identified to an
open and closed subscheme of `Div(P/S)`. *(Compare Mumford, _Lectures on curves on an algebraic surface_.)* *(N.B. To
tell the truth, the determination of the relative divisors of `P/S` could be done with the means available right now,
using results of Chapter II, and could be added as an example to §IV.19.)*

Let us now make the base change `S' = P^∨ → S` and consider the diagonal section (or "generic section") of
`P_{S'}^∨ = ℙ(E_{S'}^∨)` over `S'`: we find a closed subscheme `H` of `P_{S'} = P ×_S P^∨` — sometimes called the
**incidence scheme** between `P` and `P^∨` — defined by the image ideal of the canonical homomorphism

```text
  𝒪_P(-1) ⊗_S 𝒪_{P^∨}(-1) ⟶ 𝒪_{P ×_S P^∨},
```

from which we see that it is a projective fibration over `P^∨`; by symmetry it is also a projective fibration over `P`.
Note that one recovers the "special" hyperplanes `H_ξ` (for `ξ` a section of `P^∨` over `S`) by starting from the
"universal hyperplane" `H` and taking its inverse image under the base change `ξ : S → P^∨`.

The same remark holds for every point of `P^∨` with values in an arbitrary `S`-prescheme `S'`, which (considered as a
section of `P_{S'}^∨` over `S'`) allows us to define an `H_ξ ⊂ P_{S'}`; the latter is nothing else but the inverse image
of `H` by the base change `ξ : S' → P^∨`.

In what follows we assume given a prescheme `X` of finite type over `P`,[^v-5p1-4] together with an `S`-morphism
`f : X → P`. One of the main objectives of this paragraph is to study, for every hyperplane `H_ξ` of `P`, its inverse
image

```text
  Y_ξ = f^{-1}(H_ξ) = X ×_P H_ξ,
```

and especially to relate the properties of `X` and `Y_ξ`. As usual, one also has to consider the `P^∨(S')` for an
arbitrary `S`-scheme `S'`; in that case `H_ξ` is a hyperplane in `P_{S'}`, and we put again

```text
  Y_ξ = f_{S'}^{-1}(H_ξ) = X_{S'} ×_{P_{S'}} H_ξ = X ×_P H_ξ,
```

where the subscript `S'` denotes as usual the effect of the base change `S' → S`, and where in the last expression we
consider `H_ξ` as a `P`-scheme via the combined morphism `H_ξ → P_{S'} → P`. It is therefore again convenient to
consider the case where `ξ` is "universal", i.e. where `S' = P^∨` and `ξ` is the diagonal section, so that `H_ξ = H`; in
this case one observes (subject to better notations to be suggested by Dieudonné) that `Y = Y_ξ`. In the general case of
a `ξ : S' → P^∨`, one therefore has also `Y_ξ = Y ×_{P^∨} S'`. Finally, if `F` is a sheaf of modules[^v-5p1-5] over `X`,
we denote by `G_ξ` its inverse image over `Y_ξ`, by `G` its inverse image over `H`, so that one also has
`G_ξ = G ⊗_{𝒪_{P^∨}} 𝒪_{S'}`.

Let us summarize in a small diagram the essential constructions and notation.

<!-- original page 5 -->

```text
        F                          G              G_η
        ↓                          ↓                ↓
        X  ⟵  X ×_S P^∨  ⟵        Y    ⟵        Y_η
        ↓        ↓                 ↓                ↓
        P  ⟵  P ×_S P^∨  ⟵        H    ⟵        H_η
        ↓        ↓                 ↘                ↓
        S  ⟵     P^∨           ⟵          ⟵      S'
```

(The squares and diamonds appearing in this diagram are Cartesian.)

In the next subsection (§V.5.2) we shall study systematically the following case: `S'` is the spectrum of a field `K`,
and its image in `P^∨` is the generic point of the corresponding fibre `P_s^∨`. After making the base change
`Spec k(s) → S`, we are reduced to the case where `S` is the spectrum of a field `k`, which is what we shall assume in
the next subsection. Also, the majority of properties studied for `X` and `Y_ξ` are of "geometric" nature and therefore
invariant under base change, which allows us also (without loss of generality) to restrict ourselves to the case where
`K` is algebraically closed, or to the case where `K = k(η)`, `η` being the generic point of `P^∨`, and
`ξ : Spec(K) → P^∨` is of course the canonical morphism. We also note that for geometric questions concerning `X, Y_ξ`
we can (after making a base change) restrict ourselves to the case of `k` algebraically closed.

**A terminological reminder.** If `f` is an immersion, we usually call `Y_ξ` a **hyperplane section** of `X` (relative
to the projective immersion `f` and the hyperplane `H_ξ`). There is no reason not to extend this terminology to the case
of an arbitrary `f`.

### V.5.2. Study of a generic hyperplane section: local properties

Let us recall that, from now on, `S = Spec(k)`, with `k` a field. If `η` is a point of `P^∨` and if
`ξ : Spec k(η) → P^∨` is the canonical morphism, we also write `H_η`, `Y_η`, `G_η` in place of `H_ξ`, `Y_ξ`, `G_ξ`.

In this subsection, `η` always denotes the generic point of `P^∨`.

**Proposition (5.2.1).**

<!-- label: V.5.2.1 -->

*Assume that `X` is irreducible. Then `Y_η` is irreducible or empty, and in the first case it dominates `X`; the
prescheme `Y` is then irreducible as well.*

Indeed, since `H → P` is a projective fibration, the same is true of `Y → X`, which implies that `Y` is irreducible
whenever `X` is. The generic fibre `Y_η` of `Y → P^∨` is then irreducible or empty; in the first case its generic point
is the generic point of `Y`, which therefore lies over the generic point of `X`.

<!-- original page 6 -->

**Proposition (5.2.2).**

<!-- label: V.5.2.2 -->

*Let `Z` be a subset of `P`. Then its inverse image `Z_η` in `H_η` is empty if and only if every point of `Z` is closed.
In particular, if `Z` is constructible, then `Z_η = ∅` if and only if `Z` is finite.*

We may suppose that `Z` is reduced to a single point `z`, and we only have to prove that the image of `H_η` in `P`
consists exactly of the non-closed points of `P`. Denoting by `X` the closure of `z` and using (5.2.1), we only have to
prove that `Z_η = ∅` if and only if `X` is finite (`X` being a closed subscheme of `P`). Replacing `X` by
`X_{k(η)} ↪ P_{k(η)}`, the "only if" part follows from the following fact (for which we need to give a reference and
which deserves to be restated here as a lemma): if `Y` is any hyperplane section of `X` and if `Y_η = ∅`, then `X` is
finite (indeed, `X ⊂ P − H` is affine and projective). The "sufficient" part is immediate: for example, `Y` is a
projective fibration of relative dimension `n − 1` over `X` (`n` being the relative dimension of `P` and `P^∨` over
`S`); since `X` is finite over `k`, `Y` is of absolute dimension `n − 1 = dim P^∨ − 1`, hence the morphism `Y → P^∨`
cannot be dominant and its generic fibre `Y_η` is empty.

**Corollary (5.2.3).**

<!-- label: V.5.2.3 -->

*Let `f : X → P` be a morphism of finite type, and let `Z` be a constructible subset of `X`. In order that its inverse
image in `Y_η` be empty, it is necessary and sufficient that the image `f(Z)` be finite. In particular, in order that
`Y_η` be empty, it is necessary and sufficient that `f(X)` be finite.*

**Corollary (5.2.4).**

<!-- label: V.5.2.4 -->

*Let `Z, Z'` be two closed subsets of `X` with `Z` irreducible, and let `Z_η` and `Z'_η` be their inverse images in
`Y_η`. In order to have `Z_η ⊂ Z'_η`, it is necessary and sufficient that `f(Z)` be finite, or that `Z ⊂ Z'`. In order
that `Z_η = Z'_η`, it is necessary and sufficient that both `f(Z)` and `f(Z')` be finite, or that `Z = Z'`.*

This is an immediate consequence of (5.2.3), since we see that `f(Z − Z ∩ Z')` can be finite only if `Z ⊂ Z'` or if
`f(Z)` is finite: if `Z ⊄ Z'`, then `Z − Z ∩ Z'` is dense in `Z`, so `f(Z − Z ∩ Z')` is dense in `f(Z)`; if the former
is finite and hence (being constructible) closed, then so is the latter.[^v-5p1-6]

<!-- original page 7 -->

**Corollary (5.2.5).**

<!-- label: V.5.2.5 -->

*To every irreducible component `X_i` of `X` such that `dim f(X_i) > 0` we assign its inverse image `Y_{i,η}` in `Y_η`.
Then `Y_{i,η}` is an irreducible component of `Y_η`, and we obtain in this manner a one-to-one correspondence between
the set of irreducible components `X_i` of `X` such that `dim f(X_i) > 0` and the set of irreducible components of
`Y_η`.*

Indeed, it follows from (5.2.3) that `Y_η` is the union of the `Y_{i,η}` defined above, and that the latter are closed
and non-empty subsets of `Y`; they are also irreducible by (5.2.1). Finally, they are mutually without an inclusion
relation by (5.2.4), whence the conclusion.

Let us notice that if `dim X_i = d_i`, then `dim Y_{i,η} = d_i − 1`. More generally:

**Proposition (5.2.6).**

<!-- label: V.5.2.6 -->

*Suppose that for every irreducible component `X_i` of `X` we have `dim f(X_i) > 0`, i.e. `Y_{i,η} ≠ ∅`; or, where `f`
is an immersion, that `dim f(X) > 0`. Then `dim Y_η = dim X − 1`.*

We are reduced to the case where `X` is irreducible, by (5.2.5). By the very construction, `Y_η` is defined starting
from `X_{k(η)}` as the divisor of a section of an invertible module over `X_{k(η)}` (the inverse image of `𝒪_P(1)`). On
the other hand, `X_{k(η)}` is irreducible (because `X` is such and `k(η)` is a purely transcendental extension of `k`,
which fact one should have indicated at the beginning of the subsection), and `Y_η ≠ X_{k(η)}`, since the image of `Y_η`
in `X` (contrary to that of `X_{k(η)}`, which is faithfully flat over `X`) is not equal to `X`: indeed, it does not
contain the closed points of `X`, by (5.2.3). It follows that `dim Y_η = dim X_{k(η)} − 1 = dim X − 1`.

**Proposition (5.2.7).**

<!-- label: V.5.2.7 -->

*Let `F` be a quasi-coherent module over `X`, and hence `G_η` over `Y_η`. Let `(Z_i)` be the prime cycles associated to
`F` such that `dim f(Z_i) > 0`, and let `Z_{i,η}` be the inverse image of `Z_i` in `Y_η`. Then the `Z_{i,η}` are exactly
all the prime cycles associated to `G_η`. Moreover, their inclusion relations are the same as those among the `Z_i`.*

The last assertion is contained in (5.2.4). On the other hand, since `Y → X` is a projective fibration — hence flat with
fibres `(S_1)` and irreducible — it follows from §IV.3 that the prime cycles associated to the inverse image `G` of `F`
over `Y` are the inverse images of the prime cycles associated to `F`. Restricting to the generic fibre `Y_η` of `Y`
over `P^∨`, we obtain that the prime cycles associated to `G_η` are the non-empty inverse images of the `Z_i`, which
proves (5.2.7) by means of (5.2.3).

To tell the truth, the passage through `Y` is unnecessary: we can use directly the fact that `Y_η → X` is flat with
fibres `(S_1)` and irreducible (in fact even geometrically regular, and with geometrically irreducible fibres, the
latter being localizations of projective schemes); this is the remark to make for the proof of (5.2.1).

<!-- original page 8 -->

**Proposition (5.2.8).**

<!-- label: V.5.2.8 -->

*Let `F` be coherent over `X`, let `y ∈ Y_η`, and let `x` be its image in `X`. Let `P(M)` be one of the following
properties of a module of finite type `M` over a local noetherian ring `A`:*

*(i) `coprof M ≤ n`;*

*(ii) `M` satisfies `(S_k)`;*

*(iii) `M` is Cohen-Macaulay;*

*(iv) `M` is reduced;*

*(v) `M` is integral.*

*Then in order that `G_{η, y}` should satisfy `P`, it is necessary and sufficient that `F_x` should satisfy it.*

This follows immediately from the results of §IV.6, taking into account that `Y_η → X` is a regular morphism, so that
`𝒪_{X, x} → 𝒪_{Y_η, y}` is regular.[^v-5p1-7] Taking (5.2.3) into account, we obtain:

**Corollary (5.2.9).**

<!-- label: V.5.2.9 -->

*With the notation of (5.2.8), let `Z` be the set of `x ∈ X` such that `P(F_x)` is not satisfied. Then in order that
`G_η` should satisfy the condition `P` at every point, it is necessary and sufficient that `f(Z)` be a finite subset of
`P`, or — equivalently — that `dim f(Z) = 0`.*

Indeed, (5.2.8) says that `h^{-1}(Z)` is the `P`-singular subset of `G_η`, and it is empty if and only if `f(Z)` is
finite, by (5.2.3). (Here `h` denotes the morphism `Y_η → X`. I have just realized that the letter `P` in (5.2.8) has
been used twice; this should be resolved at the editing stage.)

**Corollary (5.2.10).**

<!-- label: V.5.2.10 -->

*The analogous condition for `Y_η` to be reduced, respectively locally integral, follows from (5.2.8) (iv), (v).*

**Corollary (5.2.11).**

<!-- label: V.5.2.11 -->

*Let `y ∈ Y_η`. In order that `Y_η` should be regular, respectively `(R_k)` at `y` (respectively normal at `y`), it is
necessary and sufficient that `X` should satisfy the same property at `x`. Let `Z` be the set of points of `X` where `X`
is not regular, respectively not `(R_k)`, respectively not normal; for `Y_η` to be regular, respectively `(R_k)`,
respectively normal, it is necessary and sufficient that `f(Z)` be finite, i.e. that `dim f(Z) = 0`.*

The proof is the same as for (5.2.8) and (5.2.9). One must give the various references assuring that `Z` is closed
(since one needs to know it is constructible in order to apply (5.2.3)).

Let us note that in (5.2.10) and (5.2.11) we do not speak at all of the corresponding geometric properties; the results
described are of "absolute" nature. We now examine the properties of geometric nature. (One could, if one wished, take
the opportunity to start a new subsection here.)

<!-- original page 9 -->

#### Geometric properties

**Theorem (5.2.12).**

<!-- label: V.5.2.12 -->

*Suppose that `f : X → P` is unramified. Let `y ∈ Y_η`, and let `x` be its image in `X`. In order that `X` should be
smooth over `k` at `x`, it is necessary and sufficient that `Y_η` should be smooth over `k(η)` at `y`.*

We may assume that `k` is algebraically closed. If `Y_η` is smooth over `k(η)` at `y`, it is regular, and so, since
`Y_η` is flat over `X`, `X` is regular at `x`; therefore `X` is smooth over `k` at `x`, since `k` is algebraically
closed and thus perfect.

For the converse, we can (after replacing `X` by an open neighbourhood of `x`) assume that `X` is smooth, and, by the
Jacobian criterion of smoothness, that it is defined in an open subset `U` of `P` by `p` equations,

```text
  X = V(f_1, …, f_p),
```

where the differentials `df_1, …, df_p` are everywhere linearly independent. Introducing the affine coordinates
`S_1, …, S_n` in `P^∨` and the affine coordinates `T_1, T_2, …, T_n` in a neighbourhood of `x` (by choosing a hyperplane
`H_∞` at infinity not containing `x`), the immersion `Y_η ↪ U_{k(η)}` is then given by

```text
  Y_η = V(f_1, …, f_p, ∑ S_i T_i − 1),
```

and it suffices to verify that the differentials (relative to `k(η)`) of `f_1, …, f_p, ∑ S_i T_i − 1` are linearly
independent. These differentials are nothing else but the sections

```text
  df_1, …, df_p, ∑ S_i dT_i
```

of `Ω^1_{U/k} ⊗_k k(η)`. Since the `df_i` are linearly independent at every point of `U`, and since the `dT_i` form a
basis of `Ω^1_{U/S}` at every point of `U` (and a fortiori a system of generators), we conclude immediately the linear
independence of the displayed quantities at every point of `U_{k(η)}` — at least when `p < n`, i.e. when

```text
  E = Ω^1_{U/k} / ∑_{1 ≤ i ≤ p} 𝒪_U df_i ≠ 0.
```

This is a small lemma about a family of generators `a_i`, `1 ≤ i ≤ n`, of a non-zero locally free module `E`: the
section `∑ S_i a_i` of `E ⊗_k k(η)` does not vanish at any point. On the other hand, the case `p = n` is trivial,
because then `Y_η = ∅`.

**Corollary (5.2.13).**

<!-- label: V.5.2.13 -->

*Let `Z` be the set of points of `X` where `X` is not smooth over `k`. In order that `Y_η` should be smooth over `k(η)`,
it is necessary and sufficient that `Z` be finite. In particular, if `X` is smooth, so is `Y_η`.*

This follows from (5.2.12) and (5.2.3). More generally we obtain:

**Theorem (5.2.14).**

<!-- label: V.5.2.14 -->

*Let `y` be a point of `Y_η`, and `x` its image in `X`. Let `P(A, K)` be one of the following properties of a local
noetherian `K`-algebra `A` over a field `K`:*

*(i) `A` is geometrically regular over `K`;*

*(ii) `A` is geometrically `(R_k)` over `K`;*

*(iii) `A` is separable over `K`;*

*(iv) `A` is geometrically normal over `K`.*

<!-- original page 10 -->

*Then `P(𝒪_{X, x}, k) ⟺ P(𝒪_{Y_η, y}, k(y))`.*

Indeed, taking §IV.6 into account, (iii) and (iv) follow from (ii) and (5.2.8) (ii). On the other hand, (i) has been
proven in (5.2.12), and it remains to deduce (ii) from (i). To do this, let `Z` be the set of points where `X` is not
smooth over `k`; its inverse image `Z_η` in `Y_η` is therefore (by (5.2.12)) the set of points of `Y_η` at which `Y_η`
is not smooth over `k(η)`. But the codimension of `Z` in `X` equals that of `Z_η` in `Y_η` at `y` because of flatness
(see §IV.6); therefore one is `> k` if and only if the other is, which completes the proof.

**Corollary (5.2.15).**

<!-- label: V.5.2.15 -->

*Let `Z` be the set of points of `X` at which `X` is not smooth over `k` (respectively is not geometrically `(R_k)` over
`k`, respectively is not separable over `k`, respectively is not geometrically normal over `k`). In order that `Y_η`
should be smooth (respectively geometrically `(R_k)`, respectively separable, respectively geometrically normal) over
`k(η)`, it is necessary and sufficient that `Z` be finite.*

From the point of view of presentation, statements (5.2.14) and (5.2.15) contain (5.2.12) and (5.2.13) (which we could
thus dispense with stating separately); on the other hand, the corollary is practically more important than the theorem,
which one could give in a proposition or a preliminary lemma so that the corollary is the more glorified.

We can give a variant in the case of property (iii):

**Corollary (5.2.16).**

<!-- label: V.5.2.16 -->

*Suppose that `f` is an immersion and that `F` is coherent. Under the conditions of (5.2.7), in order that `Z_i` should
not be embedded, it is necessary and sufficient that `Z_{i,η}` should not be embedded. If that is so, then the radical
multiplicity of `F` at `Z_i` relative to `k` equals that of `G_η` at `Z_{i,η}` relative to `k(η)`.*

The first assertion is contained in the last assertion of (5.2.7). For the second, since `Y_η → X` is flat, the functor
`F ↦ G_η` is exact, and we are reduced by restriction to a neighbourhood of the generic point of `Z_i` and by
*dévissage* to the case where `F = 𝒪_{Z_i}` and we may assume `Z_i = X`. Also, we could start by assuming that `X` is
separated over `k`, and reduce to the case of `k` algebraically closed.[^v-5p1-8] Then the assertion is contained in
(5.2.15) (iii). We conclude, as usual:

**Corollary (5.2.17).**

<!-- label: V.5.2.17 -->

*Let `Z` be the set of points of `X` where `F` is not separable over `k`. Then `G_η` is separable over `k(η)` if and
only if `Z` is finite. In particular, if `F` is separable over `k`, then `G_η` is separable over `k(η)`.*

<!-- original page 11 -->

**Remark (5.2.18).**

<!-- label: V.5.2.18 -->

*The key result (5.2.12) (and its consequences (5.2.13) and (5.2.17)) become false if we abandon the assumption that `f`
is an immersion, as we see for example by taking for `X` a purely inseparable covering of `P`. However, if `k` is of
characteristic zero, (5.2.12) and (5.2.17) are valid without assuming that `f` is an immersion.*

Indeed, it suffices to verify this for (5.2.12), and this follows from (5.2.11) and the fact that, for an algebraic
prescheme in characteristic zero, smooth = regular.[^v-5p1-9]

### V.5.3. Generic hyperplane section: geometric irreducibility and connectedness

**Theorem (5.3.1) (Bertini-Zariski).**

<!-- label: V.5.3.1 -->

*Assume that `dim f(X) ≥ 2` and that `X` is geometrically irreducible. Then the generic hyperplane section `Y_η` has the
same property.*

Let `K/k` be the function field of `X`, and let `n = dim P`; introducing the affine coordinates `T_1, …, T_n` in `P` (by
choosing a hyperplane at infinity `H_∞` such that `f(X)` is not contained in it) and `S_1, …, S_n` the affine
coordinates in `P^∨`, we see that the function field `L` of `Y_η` can be identified with the field of fractions of the
integral domain `K[S_1, …, S_n] / (∑ t_i S_i − 1)`, where the `t_i ∈ K` are the images of `T_i` under `f : X → P`. Since
`dim f(X) > 0`, the `t_i` are not all algebraic over `k` — a fortiori, they are not all zero; suppose, for example, that
`t_n ≠ 0`. We realize then immediately that

```text
  L = K(S_1, …, S_{n-1})
```

(a purely transcendental extension), `S_n ∈ L` being given by the equation `∑ t_i S_i − 1 = 0` as a function of the
`S_i` (`1 ≤ i ≤ n − 1`) and the `t_i` (`1 ≤ i ≤ n`). On the other hand, `k' = k(η)` can be identified with
`k(S_1, …, S_n)`, and the canonical inclusion `k' → L` is obtained by sending each `S_i` to its image in `L`;[^v-5p1-10]
that is, `k'` as a subextension of `L` is generated by the `S_i` (`1 ≤ i ≤ n`), or, what is the same, by the `S_i`
(`1 ≤ i ≤ n − 1`) together with

```text
  S_n = a_0 + a_1 S_1 + ⋯ + a_{n-1} S_{n-1},
```

where `a_0 = t_n^{-1}` and `a_i = − t_i t_n^{-1}` for `1 ≤ i ≤ n − 1`.

Note that the field generated by the `a_i` and that generated by the `t_i` are obviously the same; their common
transcendence degree is nothing else but the dimension of `f(X)`.

*(N.B. It would be appropriate to include this birational description at least as a corollary to (5.2.1).)*

The proof of (5.3.1) is thus reduced to that of:

**Lemma (5.3.1.1) (Zariski).**

<!-- label: V.5.3.1.1 -->

*Let `k` be a field, `K` an extension of finite type over `k`, `m` an integer `≥ 0`, and `a_i` (`0 ≤ i ≤ m`) elements of
`K` such that the transcendence degree of `k(a_0, …, a_m)` over `k` is `≥ 2`. Let `L = K(S_1, …, S_m)` and*

<!-- original page 12 -->

*let `k'` be the subfield*

```text
  k' = k(S_1, …, S_m, a_0 + ∑_{1 ≤ i ≤ m} a_i S_i)
```

*of `L`, the `S_i` being indeterminates. If `K` is a primary extension of `k`, then `L` is a primary extension of
`k'`.*[^v-5p1-11]

This lemma, or lemmas that resemble it like a brother, wander almost everywhere in the literature. That is why I leave
it up to you: the choice of the place from which you will copy a proof. I do not feel inspired to find a proof with my
own means.

**Corollary (5.3.2).**

<!-- label: V.5.3.2 -->

*Assume that `f` is unramified, or that `k` is of characteristic zero, and that `dim f(X) ≥ 2`. Then if `X` is
geometrically integral, the same is true of `Y_η`.*

Indeed, geometrically integral = geometrically irreducible + separable.

**Corollary (5.3.3).**

<!-- label: V.5.3.3 -->

*Assume that `k` is algebraically closed and that for every irreducible component `X_i` of `X` we have `dim f(X_i) ≥ 2`.
Suppose also that `X` is `σ`-connected, where `σ` is the set of closed subsets `Z` of `X` such that `dim f(Z) = 0` (i.e.
for every such `Z`, `X − Z` is connected). Under these conditions, `Y_η` is geometrically connected over `k(η)`.*

Indeed, by a lemma that ought to appear in §IV.6 together with Hartshorne's theorem,[^v-5p1-12] the hypothesis signifies
that we can join any two irreducible components `X'` and `X''` of `X` by a chain of irreducible components
`X_0 = X', X_1, …, X_n = X''` such that two consecutive ones have an intersection not in `σ`; consequently the inverse
images `X_{i,η}` are joined by a chain of components which are geometrically connected over `k(η)` by (5.3.1) and have
pairwise non-empty intersection by (5.2.3).

It follows (since `Y_η = X_η` is the union of the `X_{i,η}` as `X_i` runs through the irreducible components of `X`)
that `Y_η` is geometrically connected over `k(η)`.

**Translator's note to (5.3.1.1).** This lemma should be compared with Zariski's collected papers (MIT Press), vol. 1,
page 174, and vol. 2, page 304; also Zariski-Samuel, vol. 1, page 196, and vol. 2, page 230 of the GTM Springer edition.
See also Jouanolou's *Théorème de Bertini et applications*, Theorem 3.6 and Section 6.

### V.5.4. Variable hyperplane section: "sufficiently general" sections

We return to the general situation of §V.5.1: `S` an arbitrary prescheme. We also suppose that `X` is of finite
presentation over `S`.

In general, let us note that if `P(Z, k)` is a "constructible" property of an algebraic prescheme `Z` over a field `k`,
then the set of `ξ ∈ P^∨` such that `P(Y_ξ, k(ξ))` holds is constructible. Indeed, `Y_ξ` is the fibre over `ξ` of
`Y → P^∨`, which is a morphism

<!-- original page 13 -->

of finite presentation, and we apply §IV.9. We have an analogous remark for a property `P(Z, M, k)`, where `Z` and `k`
are as above and `M` is a coherent module over `Z`: if `G` is in addition of finite presentation over `X`, then the set
of `ξ ∈ P^∨` such that `P(Y_η, G_η, k(η))` holds[^v-5p1-13] is constructible. On the other hand, in the previous two
subsections we have developed, in various cases, criteria for the set `E` above to contain the generic point of `P^∨`,
`S` being the spectrum of a field `k`; being constructible, it follows that `E` contains a non-empty open set: this is
the passage from a conclusion concerning the generic hyperplane section to the analogous conclusion for "sufficiently
general" hyperplane sections.

Let us note in addition that, in the case `S = Spec(k)`, we also have a converse: in order that the generic hyperplane
section should have the property `P`, it is necessary and sufficient that the `Y_ξ` for `ξ` in a suitable neighbourhood
of `η` should satisfy it; and it suffices to require this for `ξ` closed in `P^∨`, which for `k` algebraically closed
leads to (or reduces to) considering `k`-rational points, i.e. hyperplane sections of `X` itself (without a prior
extension of the base field).[^v-5p1-14]

This follows, indeed, from the constructibility of `E` and from the fact that `P^∨` is a Jacobson scheme.

Let us give as examples some special cases where the previous considerations apply.

**Proposition (5.4.2).**[^v-5p1-15]

<!-- label: V.5.4.2 -->

*Let `G` be a module of finite presentation over `X`. Let `P` be one of the following properties for a module `M` over
an algebraic scheme `Z` over a field `K`:*

*(i) `coprof(M) ≤ n`;*

*(ii) `M` satisfies `(S_k)`;*

*(iii) `M` is Cohen-Macaulay;*

*(iv) `M` has no embedded prime cycle components;*

*(v) `M` is separable over `K`.*

*With these notations, if `E` denotes the set of `ξ ∈ P^∨` such that `G_ξ` satisfies the property `P`, then:*

*(a) `E` is a constructible subset of `P^∨`.*

*(b) Suppose that `S = Spec(k)`, `k` a field, and that `F` satisfies the property `P`. Suppose also, in case (v), that
`k` is of characteristic zero, or that `f : X → P` is unramified. Then `E` contains an open dense subset of `P^∨`.*

*Proof.* (a) follows from the fact that `P` is a constructible property, as we have seen in §IV.9. As to (b), it follows
from the corresponding results of the previous two subsections.

**Remark.** More generally one could suppose that, with `Z` the set of points of `X` where `F` does not satisfy `P`, the
image `f(Z)` is finite, i.e. `dim f(Z) ≤ 0`.

<!-- original page 14 -->

**Proposition (5.4.3).**

<!-- label: V.5.4.3 -->

*Let `P` be one of the following properties (for an algebraic prescheme `Z` over a field `K`):*

*(i) `Z` is smooth over `K`;*

*(ii) `Z` satisfies the geometric property `(R_k)` over `K`;*

*(iii) `Z` is separable over `K`;*

*(iv) `Z` is geometrically normal over `K`;*

*(v) `Z` is geometrically integral over `K`;*

*(vi) `Z` is geometrically irreducible over `K`.*

*Let `E` be the set of `ξ ∈ P^∨` such that `Y_ξ` satisfies `P`. Then:*

*(a) `E` is a constructible subset of `P^∨`.*

*(b) Suppose `S = Spec(k)`, `k` a field, and suppose in cases (i)-(v) that `k` is of characteristic zero and that
`f : X → P` is unramified. Finally, suppose in cases (v) and (vi) that `dim f(X) ≥ 2`. If `X` satisfies `P`, then `E`
contains a dense open subset of `P^∨`.*

*Proof.* The proof is identical to that of (5.4.2). Note that in cases (i)-(v) it suffices to assume only (in (b)) that
`f(Z)` is finite, where `Z` is the set of points of `X` where `P` fails.

**Corollary (5.4.4).**

<!-- label: V.5.4.4 -->

*Consider the property `(C_m)`: "`\overline{Z}` cannot be disconnected by a closed subset of dimension `≤ m`", where
`\overline{Z} = Z ⊗_K \overline{K}`, `\overline{K}` the algebraic closure of `K`. Let `E` be the set of `ξ ∈ P^∨` such
that `Y_ξ` over `k(ξ)` satisfies `(C_m)`. Then:*

*(a) `E` is constructible.*

*(b) Suppose `S = Spec(k)`, `k` a field, and that for every irreducible component `X_i` of `X` we have `dim f(X_i) ≥ 2`.
Then if `X` over `k` satisfies `(C_{m+1})`, then `E` contains a dense open subset `U` of `P^∨`.*

The constructibility is done via "AQT".[^v-5p1-16] This is a fact that one has forgotten in §IV.9 — perhaps it would
still be possible to repair (or fix) it. Part (b) follows in principle from (5.3.3), except that (5.3.3) has been stated
in an excessively special manner and consequently should be generalized (the proof being otherwise essentially
unchanged).

Also, there is an error in the statement of (5.4.4): it is not valid as such if `f` is quasi-finite. In the general
case, instead of considering the dimension of the closed subsets of `X`, respectively of `Y_ξ`, it is sufficient to
consider the dimension of their images in `P`, respectively in `H_ξ`. *Let the redactor sort himself out.*[^v-5p1-17]

<!-- original page 15 -->

### V.5.5. Theorems of Seidenberg type

**(5.5.1).** In the present subsection we give conditions under which the set `E` defined in §V.5.4 is open. We deal
here with properties `P` of local nature over `X`, respectively `Y_ξ`, such that we can define the set `U` of `y ∈ Y`
for which (`ξ` being the image of `y` in `P^∨`) `Y_ξ` satisfies `P` at the point `y` (respectively `G_ξ` satisfies the
condition `P` at `y`). We give first the criteria for `U` to be open, by using §IV.12.[^v-5p1-18] As always we have
`E = P^∨ − h(Y − U)`. It follows that if `U` is open and `X` is proper over `S` (since `h` is then proper and a fortiori
closed), then `E` is also open.[^v-5p1-19]

**(5.5.2).** As we have seen in §V.5.1, `Y` is defined in `X ×_S P^∨ = X_{P^∨}` as the "divisor" of a section `φ` of
`𝒪_X(1) ⊗_S 𝒪_{P^∨}(1)`, which induces for every `ξ ∈ P^∨` a section `φ_ξ` of `𝒪_X(1) ⊗_{k(s)} 𝒪_{P^∨}(1)(ξ)` (a sheaf,
by the way, isomorphic non-canonically to `𝒪_X(1) ⊗_{k(s)} k(ξ) = 𝒪_{X_{k(s)}}(1)`), such that `Y_ξ` is nothing else but
the "divisor" of this section. (N.B. The divisor of a section `φ` of an invertible module `L` is defined as the closed
subscheme defined by the image ideal of `φ^{-1} : L^{-1} → 𝒪`.) If `F` is a sheaf of modules over `X`, then its inverse
image over `Y`, i.e. the inverse image of `F ⊗_{𝒪_S} 𝒪_{P^∨} = F_{P^∨}` over the subscheme `Y` of `X_{P^∨}`, is nothing
else but the cokernel of the homomorphism

```text
  (φ ⊗ id_{F_{P^∨}})^{-1} : F_{P^∨}(-1, -1) ⟶ F_{P^∨},
```

where the notation `(-1, -1)` explains itself (as M. Artin says[^v-5p1-20]). Also, `G_ξ` is the cokernel of the
analogous homomorphism

```text
  F_{k(ξ)}(-1, -1) ⟶ F_{k(ξ)},
```

where `ξ` is a point of `P^∨` (with a corresponding interpretation if `ξ`, instead of being a point of `P^∨`, denotes a
point of `P^∨` with values in an `S'` over `S`).

In general, if `L` is an invertible module on some scheme and `φ` is a section defining the subprescheme `V(φ)`, then
for every module `F` the inverse image of `F` in `V(φ)` can be identified, by the usual abuse of language, with the
cokernel of `id_F ⊗ φ : F ⊗ L^{-1} → F`.

We say that `φ` is **`F`-regular** if the preceding homomorphism is injective. If we choose locally an isomorphism of
`L` with `𝒪_X` — which is possible — so that `φ` is identified with a section of `𝒪_X`, this terminology is compatible
with the one already introduced elsewhere.

**Proposition (5.5.3).**

<!-- label: V.5.5.3 -->

*With the previous notation, let `U` be the set of `x ∈ X_{P^∨}` with image `ξ` in `P^∨` such that `φ_ξ` is
`F_{k(ξ)}`-regular at `x`. Then:*

*(a) If `F` is of finite presentation and flat relative to `S`, then `U` is open and `G | U` is flat relative to `P^∨`.*

*(b) For every `s ∈ S`, if `η` denotes the generic point of `P_s^∨`, then `U` contains `X_{k(η)}`.*

<!-- original page 16 -->

*Proof.*

(a) Since `F_{P^∨}` is of finite presentation and flat relative to `P^∨`, the conclusion follows from §IV.11.3 (and also
from §0_III, in the case of locally noetherian `S`).

(b) We may suppose `S = Spec(k)`. The associated cycles of `F_{k(η)}` are (by §IV.3) the inverse images of the
associated cycles `Z_i` of `F`. If `f(Z_i)` is finite, then by (5.2.3) `Z_{i, k(η)} ∩ Y = ∅`; in the contrary case, by
(5.2.6) (or — better — by reasons of dimension; (5.2.3), already invoked in (5.2.6), is undoubtedly a better reason), we
have `Z_{i, k(η)} ∩ Y = Z_{i, k(η)}`. This proves that `φ` does not vanish on any of the `Z_{i, k(η)}` and therefore
proves (b).

**Corollary (5.5.4).**

<!-- label: V.5.5.4 -->

*Let `V` be the set of `ξ ∈ P^∨` such that `φ_ξ` is `F_{k(ξ)}`-regular. If `F` is of finite presentation, then `V` is
constructible and it contains the generic points of the fibres of `P^∨` over `S`. On the other hand, if also `X` is
proper over `S` and `F` is flat over `S`, then the set `V` is open.*

**Remark (5.5.5).**

<!-- label: V.5.5.5 -->

*Let `ξ ∈ P^∨` over `s ∈ S`, and suppose that `F_s` is without associated embedded cycles. Then `ξ ∈ V` (notation of
(5.5.4)) — which means also that every irreducible component of `supp F_{k(ξ)}` does not lie over `H_ξ` (and somewhat
less evidently, in this criterion we may replace `k(ξ)` by an arbitrary extension of `k(ξ)`).*

Let us note that the hypothesis `(S_1)` about `F_s` just made is satisfied notably if `F_s` is Cohen-Macaulay (a
fortiori if `F` is CM over `S`); also in this case `G_s` is CM (since locally it is deduced from `F_{k(s)}`, which is
such, by dividing by `φ · F_{k(s)}` where `φ` is `F_{k(s)}`-regular). The same remarks should (and will have to) be made
locally above to characterize the points of `U` (in place of those of `V`).

Using now §§IV.12.1.1 and IV.12.1.4, we obtain:

**Theorem (5.5.6).**

<!-- label: V.5.5.6 -->

*Assume that `F` is of finite presentation and flat relative to `S`. Let `P` be one of the properties (i)-(viii) of
§IV.12.1.1, or (if we assume `F = 𝒪_X`) one of the properties (i)-(iv) of §IV.12.1.4.[^v-5p1-21] Let `U_P` be the set of
`x ∈ X_{P^∨}` such that, if `ξ` denotes the image of `x` in `P^∨`, the property `P` is satisfied by `G_ξ` (resp. `Y_ξ`)
at the point `x`, and such that `φ_ξ` is `F_{k(ξ)}`-regular at `x`. Then `U_P` is open and `G | U_P` is flat relative to
`S`.*

Indeed, by the very definition we have `U_P ⊂ U` (notation of (5.5.3) (a)), and we apply §IV.12 to `U → P^∨` and
`F_{P^∨} | U`.

**Corollary (5.5.7).**

<!-- label: V.5.5.7 -->

*Suppose that `F` is of finite presentation and flat relative to `S`, and that `supp F` is proper over `S` (e.g. `X`
proper over `S`). Let `V_P` be the set of `ξ ∈ P^∨` such that `G_ξ`*

<!-- original page 17 -->

*(resp. `Y_ξ`) satisfies the property `P` and `φ_ξ` is `F_{k(ξ)}`-regular. Under these conditions, `V_P` is open (and is
constructible in every case, even without any flatness or properness assumption).*

It seems to me that from the point of view of presentation we cannot leave (5.5.6) as is with a simple reference to the
conditions enumerated in another volume; it requires an explicit list (i), (ii), … of properties which we have in view.
Remark also (in (5.5.1) perhaps) that the case `P =` geometrically normal (with `S = Spec(k)`, to be sure[^v-5p1-22]) is
due to Seidenberg.

### V.5.6. Connectedness of an arbitrary hyperplane section

We now combine the already-known criterion for geometric connectedness of the generic hyperplane section (5.3.3) with
Zariski's connectedness theorem in order to obtain a connectedness result for an arbitrary hyperplane section.

**Proposition (5.6.1).**

<!-- label: V.5.6.1 -->

*Suppose `S = Spec(k)`, `k` an algebraically closed field, `X` proper over `k`. Suppose that for every irreducible
component `X_i` of `X`, `f(X_i)` should be of dimension `≥ 2`, and finally that `X` cannot be disconnected by a closed
subset `Z` of `X` such that `dim f(Z) ≤ 0`. Under these conditions, for every `ξ ∈ P^∨`, `Y_ξ` is geometrically
connected.*

*Proof.* Since none of the `f(X_i)` is finite, we see that every irreducible component `Y_i` of `Y` dominates `P^∨`. On
the other hand, `Y → P^∨` is proper (`Y` being proper over `k`, since `Y` is proper over `X` and `X` is proper over
`k`). On the other hand, by (5.3.3), the generic fibre `Y_η` of `Y → P^∨` is geometrically connected.

Finally, `P^∨` is regular and a fortiori geometrically unibranch. It now suffices to apply §IV.15.6.3 (which is a
variant of Zariski's connectedness theorem) to conclude that all the fibres of `Y → P^∨` are geometrically connected.

> *Grothendieck note.* It is not difficult, by a proof of analogous type, to generalize (5.6.1) in the same sense as
> (5.4.4). If you do not want to trouble yourself with this exercise, at least mention it as a remark. Note also that we
> do not discriminate in (5.6.1) with regard to hyperplane sections that have an excessive (extra) dimension. From the
> planning point of view, it might be clearer to group together all the connectedness questions (including (5.3.3) and
> (5.4.4)) in the same subsection.

### V.5.7. Application to the construction of hyperplane sections and multisections of specified type

<!-- original page 18 -->

**(5.7.1).** Let us note that if `S = Spec(k)` where `k` is an infinite field, then every non-empty open subset of `P^∨`
contains a `k`-rational point; therefore, with the notation of §V.5.4, if `E` (defined in terms of a constructible
property `P`) contains the generic point `η`, it contains a `k`-rational point, and hence there exists a hyperplane
section of `X` (defined over `k`) having the property `P`. On the other hand, `S` being again arbitrary, it is immediate
that for every `s ∈ S` and for every point `ξ_0` of the fibre `P_s^∨` rational over `k(s)`, there exists a section `ξ`
of `P^∨` on an open neighbourhood `U` of `s` which passes through `ξ_0`. If `E` is again defined as in §V.5.4 in terms
of a constructible property `P`, and if we have (for example by §V.5.5) that `E` is open, then if `ξ_0 ∈ E`, the section
`ξ` is a section of `E` over `U`, at least if we sufficiently shrink `U`. Therefore we may construct a hyperplane
section `Y_ξ` of `X` over an open neighbourhood `U` of `s` such that for every `t ∈ U` its fibre `Y_{ξ(t)}` at `t`
satisfies the property `P`. If we do not have a priori `ξ_0` but if `k(s)` is infinite, we may combine the two preceding
remarks to obtain a hyperplane section over an open neighbourhood of `s` having the preceding property.

Finally, using §V.5.5, we have a criterion allowing us to assert (`X` resp. `F` being assumed flat over `S`, which
allows us to apply the cited result) that `Y_ξ` resp. `G_ξ` is also flat over `S`. We may therefore, replacing `X` by
`Y_ξ`, iterate the previous construction; this allows, under certain conditions, to construct "by successive
approximations"[^v-5p1-23] a **multisection** `S'` of `X` over an open neighbourhood `U` of the given point `s`, such
that `S' → U` is finite, flat, and with fibres satisfying the property `P`.

If `k(s)` is finite, we may be forced to do an étale and surjective base change `S'' → U` (`U` an open neighbourhood of
`s`) before being able to apply the preceding constructions. Indeed, under the conditions from the start of §V.5.6, if
`k` is finite, there does not necessarily exist a rational point over `k` in the open non-empty set `U`; but there
certainly exists a closed point of `U`, hence a point with values in a finite extension `k'` (necessarily separable) of
`k`. When `k = k(s)`, we may therefore, after making a suitable finite étale extension `S''` over a neighbourhood `U` of
`s`, corresponding to the residual extension `k'` (i.e. such that `S''_{s'} ≅ Spec(k')`), restrict ourselves to the
favourable situation of the unique point `s' ∈ S''` over `s` after the base change `S'' → S`.

> *Grothendieck note.* I must, however, note a regret regarding (5.4.2) and (5.4.3), which should have been announced in
> a slightly more general form (at least as a remark). If we are given an integer `m` and we denote by `E` the set of
> `ξ ∈ P^∨` such that `G_ξ`, resp. `Y_ξ`, satisfies `P` except over a closed set of dimension `≤ m` (i.e. the
> `P`-singular set `Z` is of dimension `≤ m`), then:
>
> (a) `E` is a constructible subset of `P^∨`; and
>
> (b) in the case `S = Spec(k)`, if `F`, respectively `X`, satisfies `P` except over a set of dimension `≤ m + 1`, then
> `E` contains a non-empty open set.

<!-- original page 19 -->

**Proposition (5.7.2).**

<!-- label: V.5.7.2 -->

*Assume that `X` is proper over `S` and that `F` is of finite presentation and flat over `S`. Let `P` be one of the
properties (i)-(v) of (5.4.2), and let `m` be an integer. Let `s ∈ S`, and suppose that the set `Z_s` of points of `X_s`
where `F_s` does not satisfy `P` is of dimension `≤ m + 1`. Then if also `k(s)` is infinite, there exists a
neighbourhood `U` of `s` in `S` and a section `ξ` of `P^∨` over `U` having the following properties: for every `x ∈ U`,
the set of points of `Y_{ξ, x}` where `G_{ξ(x)}` does not satisfy `P` is of dimension `≤ m`, and `φ_{ξ(x)}` is
`F_{ξ, x}`-regular. Under these conditions, the module `G_ξ` over `Y_ξ` is flat relative to `U`. Finally, if `k(s)` is
not assumed infinite, we can again make the previous construction after an étale extension of the type anticipated in
(5.7.1).*

**Proposition (5.7.3).**

<!-- label: V.5.7.3 -->

*The same as (5.7.2), but with no module `F`, assuming instead that `X` is flat relative to `S`. We refer to properties
(i)-(v) of (5.4.3) in place of those of (5.4.2) (but being careful to keep the reservation that in case (v), for every
`s ∈ S` and every irreducible component `Z` of `X_s`, we have `dim f(Z) ≥ 2`).*[^v-5p1-24]

*(Text crossed out in the source.)*

**Proposition (5.7.4).**

<!-- label: V.5.7.4 -->

*Let `g : X → S` be a flat proper morphism, let `s ∈ S`, put `n = dim X_s`, and suppose that the dimension of the set of
points of `X_s` where `X_s` is not separable over `k(s)` is `< n` (for example, `X_s` separable). Then there exists an
open neighbourhood `U` of `s` and an étale finite surjective morphism `S'' → U` such that `X ×_S S''` admits a section
over `S''`. If `k(s)` is infinite, we may take for `S''` a closed subscheme of `X_U`.*[^v-5p1-25]

*Proof.* Assume to start with that `k(s)` is infinite. We proceed by induction on `n`, the case `n = 0` being trivial:
in that case there exists an open neighbourhood `U` of `s` such that `X | U` itself is étale, finite, and surjective
above `U`, as one sees by immediate cross-references. If `n > 0`, we apply (5.7.3) for the "separable" property, which
allows us to replace `X` by a "hyperplane section" `Y` having the same properties up to the fact that `n` is replaced by
`n − 1`. If `k(s)` is not assumed infinite, we begin by making an étale base change; the argument goes through.

<!-- original page 20 -->

**Remark (5.7.5).**

<!-- label: V.5.7.5 -->

*In particular, if `X` is projective and separable over `S`, it admits locally over `S` étale multisections. But we note
that one can give examples with `X` proper and smooth (but not projective) over `S` where the same conclusion fails. Of
course, the projective assumption cannot be weakened in general to an assumption of quasi-projectiveness, as one sees,
for example, by taking `X` étale and not finite over `S`.*[^v-5p1-26]

### V.5.8. Dimension of the set of exceptional hyperplanes

**(5.8.1).** In the previous subsections, and notably in §§V.5.2 and V.5.3, we have given statements asserting that the
set of `ξ ∈ P^∨` such that `Y_ξ` has a certain property `P` is constructible and that it contains the generic point `η`;
or, equivalently, that the set `Z_P` of `ξ ∈ P^∨` "exceptional for `P`" is constructible and rare — i.e. its closure is
of codimension `≥ 1`. (N.B. We suppose `S = Spec(k)`.)

In certain cases we can make this statement more precise by giving a better upper bound on this codimension, which is
important for certain questions. For example, if we see that this codimension is `≥ 2`, it follows that a "sufficiently
general" straight line `D` of `P^∨` does not intersect `Z_P`, whence the existence (if `k` is infinite) of "linear
pencils" of hyperplane sections `Y_ξ` (`ξ` a geometric point of `D`) all of which have the property `P`. (See the
subsection on pencils of hyperplane sections for examples.[^v-5p1-27])

From the point of view of presentation, since the results of the present subsection make some of the results of the
previous subsections more precise, the question arises whether it is necessary to do this catching-up in a separate
subsection, or to give a more precise version gradually as one moves along. *Let the redactor decide.*[^v-5p1-28]

**(5.8.2).** Let `Z` be the set of `ξ ∈ P^∨` such that `dim Y_ξ > dim X − 1`, and suppose that for every irreducible
component `X_i` of `X` we have `dim f(X_i) ≥ 2`.[^v-5p1-29] Then `Z` is of codimension `≥ 2` in `P^∨`. This follows from
(5.2.1) and (5.2.2) (which imply that every irreducible component of `Y` dominates `P^∨`) and from the dimension theory
for the morphism `Y → P^∨`. Starting from this result we may give, as a corollary, the case where we start with a closed
subset `T` of `X` and where we consider the dimension of the inverse images `T_ξ` in the `Y_ξ` (`ξ ∈ P^∨`); we may even
take for `Z` the set of `ξ ∈ P^∨` such that there exists an irreducible component of `T_{k(ξ)}` whose trace on `Y_ξ` has
excessive dimension. (N.B. We always assume that for every irreducible component `T_i` of `T` we have `dim f(T_i) > 0`.)

<!-- original page 21 -->

Finally, the most precise statement in this direction, and one that follows easily from the first formulation (for `X`
irreducible) and from (5.2.7), is the following modified statement: `F` being coherent over `X`, suppose that for every
prime cycle `T` associated to `F` we have `dim f(T) > 0`. Then the set of `ξ ∈ P^∨` such that `φ_ξ` is not
`F_{k(ξ)}`-regular is (constructible and) of codimension `≥ 2`. (The notation for `φ_ξ` is that of §V.5.5.) We can give
this as the principal assertion, and announce the previous assertions as corollaries, the proof being via one of the
corollaries.

Note that with the preceding notation, if `ξ ∈ P^∨ − Z`, then for every `y ∈ Y_ξ` we have
`coprof_y G_{k(ξ)} = coprof_y G_ξ`, and consequently if `coprof F ≤ n`, then for `ξ ∈ P^∨ − Z` we have `coprof G_ξ ≤ n`.
In particular, if `F` is Cohen-Macaulay, then for `ξ ∈ P^∨ − Z`, `G_ξ` is Cohen-Macaulay. Finally, if `F` is `(S_k)`,
then `G_ξ` is `(S_{k-1})` for `ξ ∈ P^∨ − Z` (see §0_IV).

**(5.8.3).** We note that if `F` is `(S_k)`, it can happen, for some `ξ ∈ P^∨` such that `φ_ξ` is `F_{k(ξ)}`-regular,
that `G_ξ` has a component of codimension `≥ 2` failing `(S_k)`,[^v-5p1-30] even if `F = 𝒪_X`, `k = 1`, `X` being
geometrically integral of dimension two (resp. `k = 2`, `X` being geometrically integral and geometrically normal of
dimension three). It is enough to start from a projective integral surface

```text
  X ⊂ ℙ^r
```

over `k` algebraically closed having a point `x` where `X` is not Cohen-Macaulay; then for every hyperplane passing
through `x`, the corresponding hyperplane section `Y_ξ` admits `x` as an associated embedded cycle. (Respectively, we
start from a normal — hence `(S_2)` — integral variety `X ⊂ ℙ^r` of dimension three having a point `x ∈ X` where `X` is
not Cohen-Macaulay; then the `Y_ξ` passing through `x` are not CM, i.e. they fail `(S_2)` at `x`.)

In these examples the set of "exceptional" `ξ` for the property `(S_k)` contains the hyperplane of `P^∨` defined by
`x ∈ P` and is of codimension one (and not of codimension `≥ 2`). Compare (5.8.5) below for a general precise result
along these lines.

**Proposition (5.8.4).**

<!-- label: V.5.8.4 -->

*Let `T` be a closed subset of `X`, and suppose that `codim(T, X) ≥ k`. Then for every `ξ ∈ P^∨` we have
`codim(T_ξ, Y_ξ) ≥ k − 1`. Let `Z` be the set of `ξ ∈ P^∨` such that `codim(T_ξ, Y_ξ) = k − 1` (i.e.
`codim(T_ξ, Y_ξ) < k`). Then `Z` is a constructible, nowhere dense subset of `P^∨`, i.e. `\overline{Z}` is of
codimension `≥ 1` in `P^∨`.*

*In order for it to be of codimension `≥ 2`, it is necessary and sufficient that for every irreducible component `T_i`
of `T` of codimension equal to `k` and such that `dim f(T_i) = 0`, there should exist an irreducible component `X_j`*

<!-- original page 22 -->

*of `X` such that `codim(T_i, X_j) = k` and `dim f(X_j) > 0` — i.e., if `f` is quasi-finite and `k > 0`, that `T` does
not have isolated points such that `dim_x X = k`.*

The first assertion follows immediately from the following lemma (5.8.4.1) (a), which is a remorseful afterthought to
§V.5.5.

**Lemma (5.8.4.1).**

<!-- label: V.5.8.4.1 -->

*Let `X` be a locally noetherian prescheme, let `L` be an invertible module over `X`, `φ` a section of `L`, `Y = V(φ)`,
and `T` a closed subset of `X`. Assume that `codim(Y, X) ≥ k`. Then:*

*(a) `codim(T ∩ Y, Y) ≥ k − 1`.*

*(b) In order to have `codim(T ∩ Y, Y) = k − 1` (i.e. `codim(T ∩ Y, Y) < k`), it is necessary and sufficient that there
should exist an irreducible component `T_i` of `T` contained in `Y` such that `codim(T_i, X) = k` and such that for
every irreducible component `X_j` of `X` containing `T_i` with*

```text
  dim 𝒪_{X_j, T_i} = dim 𝒪_{X, T_i}  ( = k),
```

*we have `X_j ⊄ Y`.*

The verification of this lemma is immediate, given the general facts in §0_IV (Chapter IV) about dimension.

With the assumptions of (5.8.4), and by (5.8.4.1) (b), we see which are the exceptional hyperplanes `H_ξ`. If we exclude
the set `Z_0` of `ξ ∈ P^∨` such that there is an irreducible component `R` of `T` or of `X` with `dim f(R) > 0` and such
that `R_ξ` is of "dimension too large" (a set which is of codimension `≥ 2` and in what follows does not count), the
exceptional `H_ξ` are those for which there exists a `T_i` with `codim(T_i, X) = k` and `dim f(T_i) = 0`,
`f(T_i) ⊂ H_ξ`, and such that for every irreducible component `X_j ⊃ T_i` of `X` with `codim(T_i, X_j) = k`, we have
`f(X_j) ⊄ H_ξ`. For a given `T_i` with `codim(T_i, X) = k`, if there exists an `X_j` with `codim(T_i, X_j) = k` and such
that `dim f(X_j) = 0`, then we will have `f(X_j) = f(T_i) ⊂ H_ξ`, and consequently `ξ` would not be exceptional relative
to the `T_i`. If, on the other hand, for every `X_j ⊃ T_i` such that `codim(T_i, X_j) = k` we have `dim f(X_j) > 0`,
then for `ξ ∈ P^∨ − Z_0`, `ξ` is exceptional relative to `T_i` if and only if `f(T_i) ⊂ H_ξ`; the set of such `ξ` is
(the trace on `P^∨ − Z_0` of) a hyperplane of `P^∨`. This proves (5.8.4), and also proves the more precise result that
the exceptional set is the union of a set of codimension `≥ 2` and of a union of hyperplanes determined in the evident
way by the above proof.

<!-- original page 23 -->

> *Grothendieck note.* I am afraid that the writeup is quite floppy (or perhaps sloppy)[^v-5p1-31] since I have reasoned
> geometrically all the time without saying so, by taking points over an algebraically closed field. Of course, the
> condition announced in (5.8.4) is indeed geometric, so that we may suppose `k` algebraically closed and argue for
> `k`-rational points.

Using (5.8.4), (5.7.4), and the end of (5.8.2), we obtain:

**Corollary (5.8.5).**

<!-- label: V.5.8.5 -->

*Suppose that for all associated prime cycles `R` we have at most simply [some condition][^v-5p1-32] and that `F`
satisfies `(S_k)`. In order that the (constructible) set of points of `P^∨` such that `φ_ξ` is `F_{k(ξ)}`-regular and
`G_ξ` is `(S_k)` should have a complement of codimension at least two, it is necessary and sufficient that the following
hold: for every integer `n ≥ 0`, denote by `Z_n` the set of `x ∈ T = supp F` such that* `coprof_x F ≥ n`;[^v-5p1-33]
*then for every irreducible component `Z_{n,i}` of `Z_n` with `codim(Z_{n,i}, T) = n + k + 1` and `dim f(Z_{n,i}) = 0`,
there exists an irreducible component `T_j` of `T` containing `Z_{n,i}` such that `codim(Z_{n,i}, T_j) = n + k + 1` and
`dim f(T_j) = 0`.*

When `f` is quasi-finite, then for every closed subset `R` of `X`,[^v-5p1-34] we have `dim f(R) = dim R`, so that the
criterion takes the following form: *there does not exist an isolated point `z` in any one of the `Z_n` such that
`dim_z T (= dim F_z)` is equal to `n + k + 1`*.

When `F` is equidimensional of dimension `d`, this condition is vacuous if `d ≤ k` (and indeed we knew this, because in
this case the hypothesis `(S_k)` on `F` is nothing else but the Cohen-Macaulay hypothesis), and if `d ≥ k + 1` it means
that the set `Z_{d - (k+1)}` of points of `T` where the codepth of `F` is `> d − (k + 1)`, i.e. the true depth of `F` is
`≥ k + 1` (even though, a priori, we only have true depth of `F` `≥ k` as a consequence of property `(S_k)` and
`k ≤ d`). If we no longer assume that `F` is equidimensional, the desired condition may be expressed in the following
simple way:

**(5.8.6).** *For every closed point `x ∈ supp F` such that `dim F_x ≥ k + 1`, we have `prof F_x ≥ k + 1`.*

The sufficiency is seen immediately by putting `Z = {x}`. The necessity is seen by noticing that for every `ξ` such that
`φ_ξ` is `F_{k(ξ)}`-regular and `x ∈ Y_ξ`, we have

```text
  dim G_{ξ, x} = dim F_x − 1,   prof G_{ξ, x} = prof F_x − 1,
```

so that `x` fails by default the above condition: we have `prof G_{ξ, x} ≥ k` but `dim G_{ξ, x} ≥ k`, which shows that
`G_ξ` does not satisfy condition `(S_k)` at `x`; but the set

<!-- original page 24 -->

of `ξ` such that `x ∈ Y_ξ` is of codimension one. (N.B. I implicitly assumed that `k` is algebraically closed, the case
to which we reduce immediately.) The preceding general criterion should be evident in the case of (5.8.6).

We now study the points `y` of `Y` that are not smooth for `Y_ξ` relative to `k(ξ)`. We restrict ourselves to the case
where `f : X → P` is unramified (practically, it will be an immersion) and where `X → S` is smooth. We do not
necessarily assume that `S` is the spectrum of a field.

Since `f` is unramified, the canonical homomorphism `f^*(Ω^1_{P/S}) → Ω^1_{X/S}` is surjective and its kernel is a
locally free module over `X`, which we denote `ν^∨_{X/P}`; when `f` is an immersion, this is nothing else but the
conormal module `J/J²` defined by the ideal `J` of `X` in `P`, and we call it in every case the **conormal module**.
Thus we have the exact sequence

```text
  (a)        0 ⟶ ν^∨_{X/P} ⟶ f^*(Ω^1_{P/S}) ⟶ Ω^1_{X/S} ⟶ 0.
```

Let us observe that we also have over `P` an exact canonical sequence (which should appear as an example in §IV.16, for
example)

```text
  (b)        0 ⟶ Ω^1_{P/S}(1) ⟶ E_P ⟶ 𝒪_P(1) ⟶ 0
```

— i.e. `Ω^1_{P/S}(1)` is canonically isomorphic to the kernel of the canonical homomorphism `E_P(-1) → 𝒪_P` deduced from
`E_P → 𝒪_P(1)`. Applying `f^*`:

```text
  (b₁)       0 ⟶ f^*(Ω^1_{P/S})(1) ⟶ E_X ⟶ 𝒪_X(1) ⟶ 0,
```

which gives an explicit description of `f^*(Ω^1_{P/S})(1)` over `X` and allows therefore to identify `ν^∨_{X/P}(1)` with
a submodule locally a direct factor of `E_X` — or, dually, `ν_{X/P}(-1)` is canonically isomorphic to a quotient module
of `E_X^∨`. Consequently `ℙ(ν_{X/P}(-1)) = ℙ(ν_{X/P})` can be canonically embedded in `ℙ(E_X^∨) = X ×_S P^∨ = X_{P^∨}`
as a projective subfibration over `X`, hence as a closed subscheme. The latter is necessarily contained in `Y` (from the
fact that `Ω^1_{X/P}(1)` is contained in the kernel of `E_X → 𝒪_X(1)`).

The underlying set of this prescheme is nothing else but the set of points of `Y = V(φ)` which are singular zeros (in
the sense of §V.1, formerly §16)[^v-5p1-35] of the section `φ` of `𝒪_{X ×_S P^∨}(1, 1)` relative to the base `P^∨`;
i.e., its points with values in a field `k` over `P^∨` are the points `x` of `Y_k ⊂ X_k` such that `φ_k` vanishes to
order at least two at `x`, i.e. such that `Y_k` is not smooth of relative dimension `r − 1` over `k` at `x`. The
announced characterization of singular zeros as the elements of a smooth subscheme `ℙ(ν_{X/P})` of `X_{P^∨}` gives
immediately the following statement, which deserves to appear as a preliminary proposition:

<!-- original page 25 -->

*if `S = Spec(k)` and if `H` is a hyperplane of `P`, then `Y = X ×_P H` is smooth over `k` of relative dimension `d − 1`
at the point `x ∈ Y(k)` (i.e. `x` is a non-singular zero, i.e. geometrically non-singular, of the section `φ` of
`𝒪_X(1)` defined by `H`) if and only if `H` does not contain the image under `f` of the tangent space to `X` at `x`
(relative to `k`); equivalently (if `f : X → P` is an immersion which allows us to identify `X` to a subscheme of `P`),
if and only if `H` is not tangent to `X` at `x`.* This follows trivially from the Jacobian criterion of smoothness, or
from the definition of a singular zero, once we make precise the sense of the statement — that is, the way in which a
vector subspace of the tangent space to `P` at a point `a = f(x)` defines a linear subspace of `P` (in such a way that
it makes sense to say that `H` does not contain the said vector subspace). Of course, this comes from the exact sequence
(b) above, which allows one to define a one-to-one correspondence between the set of factor subspaces of the tangent
space at `a` and the set of linear subspaces of `P` containing `a`. This correspondence reduces to associating to a
linear subvariety passing through `a` its tangent space at `a`, considered as a subspace of the tangent space to `P` at
`a`.

Such "*sorites*" grouped together with various *sorites* about linear subvarieties and Grassmannians ought to be given
in one or two preliminary subsections or paragraphs, of course over an arbitrary base. In fact we can do better, knowing
that the prescheme `Y^{sing}` of singular zeros of `φ` relative to `P^∨`, defined in §V.1, is nothing else but
`ℙ(ν_{X/P})`; and since the latter is smooth over `S` of relative dimension `d + (r − d − 1) = r − 1` (`r` being the
relative dimension of `P^∨` over `S`), we are under the favourable conditions studied in §V.1.[^v-5p1-36] In order to
verify them, let us notice that by definition `Y^{sing}` is nothing else but the subprescheme of `Y` of zeros of the
section `Ψ = (dφ) |_Y` of

```text
  Ω^1_{X_{P^∨} / P^∨}(1, 1) ⊗ 𝒪_Y = Ω^1_{X/S} ⊗ 𝒪_Y(1, 1).
```

We shall give another interpretation of this section, from which the conclusion follows immediately. To do this,
consider the following diagram of exact sequences over `X_{P^∨}`, or more generally over any prescheme `Z` over
`X_{P^∨}`:

<!-- original page 26 -->

```text
                                            0
                                            ↓
                                     𝒢_{P^∨/S} ⊗ 𝒪_Z(0, -1)
                                            ↓
              Ω^1_{X/Y} ⊗ 𝒪_Z(1, 0)
                     ↑
   0 → Ω^1_{P/S} ⊗ 𝒪_Z(1, 0) → E ⊗ 𝒪_Z → 𝒪_Z(1, 0) → 0
                     ↑                        ↑
                     β                        α
                     ↑                        ↑
              ν^∨_{X/P} ⊗ 𝒪_Z(1, 0)      𝒪_Z(0, -1)
                     ↑                        ↑
                     0                        0
```

[^v-5p1-37] — where the first column is deduced from (a) by tensoring with `𝒪_Z(1, 0)`, the row is deduced from (b) by
tensoring with `𝒪_Z`, and the second column is deduced from the analogous sequence `(b^∨)` relative to `P^∨` (obtained
by replacing `E` by `E^∨`) by transposition and tensoring with `𝒪_Z`. From the very definition of `Y`, `Z` is over `Y`
if and only if the composed morphism `α` in the diagram is zero, i.e. if we can find a factorization
`β : 𝒪_Z(0, -1) → Ω^1_{P/S} ⊗ 𝒪_Z(1, 0)`. If that is the case, we can consider its composition with
`Ω^1_{P/S} ⊗ 𝒪_Z(1, 0) → Ω^1_{X/Y} ⊗ 𝒪_Z(1, 1)`. *I say that this is precisely the section `ψ`*[^v-5p1-38] which we have
introduced above (the verification ought to be essentially mechanical). It is zero if and only if `Z` lies over `V(ψ)`
(by the very definition of `V(ψ)`); but this means also that `β` factors through `ν^∨_{X/P} ⊗ 𝒪_Z(1, 0)`, i.e. that the
submodule `𝒪_Z(0, -1)` of `E ⊗ 𝒪_Z` is contained in the submodule `ν^∨_{X/P} ⊗ 𝒪_Z(1, 0)`, which evidently signifies
also that `Z` is over the subprescheme `ℙ(ν_{X/P}(1))` of `ℙ(E_X^∨)`, achieving the proof we have announced.

Just before this erudite exercise in syntax (for which I have already had to sweat quite a bit), we could remark that
from every set-theoretic point of view `Y^{sing}` is of dimension `r − 1` if `S = Spec(k)`, whereas `P^∨` is of
dimension `r`, so that the image of `Y^{sing}` in `P^∨` is of codimension `≥ 1`. This gives again (5.2.12) (it is well
to note that the argument is not essentially distinct from the one used in (5.2.12)). We note that most often this set
is effectively of codimension one (compare below).

<!-- original page 27 -->

Consequently we cannot in general find "linear pencils" of hyperplane sections all of which are smooth. However, we
shall see that we can often manage to find pencils formed by hyperplane sections not having any supersingular point, due
to the fact that in the most common cases the image of `Y^{supsing}` in `P^∨` is of codimension two.

We first recall the essential points, of differential nature, of the situation studied here.

**Theorem (5.8.7).**

<!-- label: V.5.8.7 -->

*(a) The subprescheme `Y^{sing}` (defined in §V.1) in the present situation is nothing else but `ℙ(ν_{X/P})`, considered
as a subscheme of `Y` as explained above.*

*(b) The underlying set of the prescheme `Y^{supsing}` (cf. §V.1) is nothing else but the set of ramification points of
the morphism of smooth preschemes over `S` of relative dimensions `r − 1` and `r`, namely*

```text
  Y^{sing} = ℙ(ν_{X/P}) ⟶ P^∨,
```

*i.e., in order for this latter morphism to be unramified at the point `y` (see the definition), it is necessary and
sufficient that `y` should be geometrically an ordinary singular point for `φ_ξ` (`ξ` being the point of `P^∨` that is
the image of `y`).*

*(c) Suppose `S = Spec(k)` and that `y ∈ Y^{sing} = ℙ(ν_{X/P})` is a `k`-rational point. Let `x ∈ X(k)` and `ξ ∈ P^∨(k)`
be its projections, and consider the linear subvariety `H'` of `P^∨` "image" of the tangent map of the closure `T` of
`Y^{sing}` in `P^∨`, given the induced reduced structure. Consider the induced morphism `g : Y^{sing} → T` (a dominant
morphism of integral preschemes). The conditions (i), (ii), and their variants are equivalent:*

*(i) The morphism `g` is generically étale (i.e. étale at at least one point, or equivalently, étale = unramified at the
generic point of `Y^{sing}`).*

*(i bis) The field extension `L/K` defined by `g` is finite and separable.*

*(i ter) The morphism `g` is birational, i.e. the extension `L/K` is the trivial extension.*

*(ii) `Y^{sing} ≠ Y^{supsing}` (set-theoretically).*

*(ii bis) There exists an `x ∈ X(k)` and a tangent hyperplane `H` to `X_k` at `x` which is not osculating at `x` — by
which we understand precisely that `x` is not supersingular for the section of `𝒪_{X_k}(1)` that defines `H`.*

*These conditions imply that `Y^{supsing} ≠ Y^{sing}` and `dim Y^{supsing} ≤ r − 2`, so that the image of `Y^{supsing}`
in `P^∨` has codimension `≥ 2`; and they imply also*

*(iii) `dim T = r − 1`, i.e. `T` is of codimension one in `P^∨`.*

<!-- original page 28 -->

*Proof.* The equivalence of (i) and (i bis) is trivial; its equivalence with (ii) is a trivial consequence of (5.8.7)
(b); finally, the equivalence of (ii) and (ii bis) is practically the definition of `Y^{supsing}`. Evidently (i ter) ⟹
(i). It remains to prove that (i) ⟹ (i ter). We may evidently suppose that `K` is algebraically closed and we are
reduced to proving (taking into account the hypothesis (i)) that there exists an open set `U ≠ ∅` such that `ξ ∈ U(K)`
implies that there exists exactly one point of `Y^{sing}(K)` over `ξ`. This will follow from the next corollary, which
says more.

**Corollary (5.8.9).**[^v-5p1-39]

<!-- label: V.5.8.9 -->

*Suppose condition (i) of (5.8.7) is satisfied, and let `U` be the open subset of `T` of points where `T` is smooth over
`k`. Then `U ≠ ∅`, `Y^{sing} |_U → U` is an open immersion (a fortiori `Y^{sing} |_U` does not contain the points of
`Y^{supsing}`). If `X` is proper over `K`, then `g : Y^{sing} → T` is surjective; hence `Y^{sing} |_U → U` is proper
over `K`, so that `g : Y^{sing} → T` is surjective; therefore `Y^{sing} |_U → U` is an isomorphism, and `U` is the
largest open subset of `T` having the latter property.*

First of all, since `g` is dominating and generically étale, it is generically étale, so we can find at least one
non-empty open subset `V` of `T` such that `Y^{sing} |_V → V` is étale and surjective; this implies that `V` is smooth
over `K`. If then `ξ ∈ V(K)` and if `y` is a point of `Y^{sing}(k)` over `ξ`, then with the notation of (5.8.7) (c), the
space `H'` is nothing else but the tangent space to `T` at `ξ`, and as we observed here, this implies that the point `x`
of `X(k)`, the projection of `y`, is determined as the orthogonal point to `H'`. It is thus uniquely determined;
consequently, since `Y^{sing} ⊂ X × P^∨`, the point `y` is uniquely determined.

This proves already that `g` is birational (being generically étale and generically radical). On the other hand, the
morphism `ψ` (whose definition in this form is evident), which associates to every `ξ ∈ U(K)'` the unique point
`x = ψ(ξ) ∈ P` orthogonal to the tangent space to `U` at `ξ`, coincides over `V` with the composition
`V → Y^{sing} |_V → X`, where the second arrow is the projection. Therefore, setting `h = (ψ, id) : U → P × T`, and
`g_1 = g | g^{-1}(U) : g^{-1}(U) → U`, the composition `h ∘ g_1 : g^{-1}(U) → P × T` is nothing else but the canonical

<!-- original page 29 -->

inclusion, this being so on its restriction to `g^{-1}(V) → V`. It follows that `h` factors through the scheme-theoretic
closure `\overline{Y^{sing}}` of `Y^{sing}` in `P × T`; thus the inverse image of `Y^{sing}` (which is open in the above
closure) by `h` is an open subset of `U` — call it `U'`. Because of `h ∘ g_1 =` inclusion, we see immediately that `g_1`
induces an isomorphism `g^{-1}(U') ⥲ U'`. Since `Y^{sing}` is smooth, it follows that `U'` is smooth, hence `U' ⊂ U`.
This proves (5.8.9).

The final assertions of (5.8.7) — `Y^{supsing} = ∅` or `dim Y^{supsing} = r − 2`, and `dim T = r − 1` — are trivial: the
first follows from the fact that `Y^{sing}` is irreducible of dimension `r` and from the fact that `Y^{supsing}` is
defined inside `Y^{sing}` by the vanishing of a section `D` of an invertible module; the second from the fact that, `L`
being finite over `K`, we have `\deg.tr_k L = \deg.tr_k K`, i.e. `dim T = dim Y^{sing} = r − 1`.

**Remark (5.8.10).**

<!-- label: V.5.8.10 -->

*As we remarked in (5.8.9), with the notation of the corollary, we have `g^{-1}(U) ⊂ Y^{sing} − Y^{supsing}`. But we
note that even if `X` is closed in `P`, this inclusion is not necessarily an equality. In other words (noting that
`g^{-1}(U)` is nothing else but the set of points where `g` is étale), `Y^{sing} − Y^{supsing}` is the set of points
where `g` is unramified but not étale (which implies in addition that `g(y)` is a point that is not geometrically
normal, and even not geometrically unibranch, of `T`). In geometric terms this corresponds to the following phenomenon:
we may have a tangent non-osculating hyperplane for `X` at a point `x ∈ X(k)` such that there exists another point
`x_1 ∈ X(k)` at which the same hyperplane is tangent to `X` at `x_1`. There are obvious examples with `P` of dimension
two, `X` a non-singular curve of degree `≥ 4`, in any characteristic. (Note here: the "double tangents" of `X`
correspond to the double points of the "dual curve".)*

**Corollary (5.8.11).**

<!-- label: V.5.8.11 -->

*Suppose that `k` has characteristic zero. Then:*

*(a) The image of `Y^{supsing}` in `P^∨` is of codimension `≥ 2`.*

*(b) Condition (iii) of (5.8.7) is equivalent to the negation of the other conditions; that is, the assumption
`Y^{sing} = Y^{supsing}` means also that the image of `Y^{sing}` in `P^∨` is of codimension `≥ 2`.*

Evidently, (b) implies (a), taking (5.8.7) into account. But by dimension theory, (iii) means that `L/K` is a finite
extension (we could put it in the form (iii bis) in (5.8.7)), and in characteristic zero `L` is always separable over
`K`, hence the condition (i bis) of (5.8.7).

<!-- original page 30 -->

**Remark (5.8.12).**

<!-- label: V.5.8.12 -->

*Geometrically, the assertion (a) means essentially that for a sufficiently general linear pencil of hyperplane
sections, every member of the pencil is smooth or has, as geometric singular points, ordinary double points. (In fact,
as one sees immediately, the statement (a) can be made a little more precise: there is at most one such singular
geometric point.) The assertion (b) means essentially that if `Y^{sing} = Y^{supsing}` — a condition that can be
expressed analytically by the vanishing of a certain section `D` of an invertible module
`ω_{X/k}^{⊗2} ⊗ 𝒪_{Y^{sing}}(1, 1)` over `Y^{sing}` — then, for a sufficiently general linear pencil of hyperplane
sections, all the members of the pencil are smooth. This second situation (whether or not we are in characteristic zero)
should entirely be considered as exceptional.*

> *Grothendieck note.* In the classical language[^v-5p1-40] this is expressed, if there is no error, by saying that `X`
> is **ruled** for the projective immersion considered, and if we so please, we have here all that we need due to
> (5.8.5) and its corollaries to make explicit and justify such a terminology — in case you feel inspired to make a
> connection with classical terminology.[^v-5p1-41] For example, if `dim X = 1`, this implies that `X` is a straight
> line, so that any `x ∈ X(k)` is contained in `T`.[^v-5p1-42]
>
> *(b) If the characteristic is `p > 0`, we should normally give examples (with `dim P = 2`, `X` a non-singular
> algebraic curve) where the conditions of (5.8.6) are not satisfied, i.e. `Y^{sing} = Y^{supsing}` and where
> nevertheless `dim T = r − 1`, i.e. examples where `L/K` is a finite inseparable extension. I am too lazy to construct
> the examples, but I do not doubt that such examples exist.*[^v-5p1-43]

In (a), make a footnote to the following subsection, where we prove that if the exceptional "ruled" case arises, then by
a trivial modification of the projective immersion we find ourselves again in the "general" situation of (5.8.7).

The part of the present subsection from (5.8.6) onwards could without a doubt be made into a separate subsection of
differential character; whereas the beginning of our subsection, together with what follows, should be merged into a
subsection on the dimension of exceptional hyperplanes (we use only the fact that `Y^{sing}` has dimension `r − 1`).

**Proposition (5.8.13).**

<!-- label: V.5.8.13 -->

*We always assume that `f : X → P` is unramified and that `X` has no isolated points. Assume that `X` satisfies `(R_k)`
geometrically. Let `Z_k` be the part of `P^∨` complementary to the set of `ξ ∈ P^∨` such that `φ_ξ` is
`F_{k(ξ)}`-regular and `Y_ξ` satisfies the geometric condition `(R_k)`. Then:*

<!-- original page 31 -->

*(a) In order for `Z_{k-1}` to be of codimension `≥ 2` in `P^∨`, it suffices that every irreducible component `X'_i` of
`X'` of dimension `≤ k` should be ruled for `f`.*

*(b) In order to have `Z_k` of codimension `≥ 2` in `P^∨`, it suffices that every irreducible component `X_i` of `X` of
dimension `≤ k − 1`[^v-5p1-44] should be made up of smooth points of `X` and should be ruled.*

Indeed, for every `ξ` geometrically singular, the singular set of `Y_ξ` (N.B.: we restrict ourselves to `ξ` such that
`φ_ξ` is `F_{k(ξ)}`-regular, which is harmless because of (5.8.2)) is the union of `sing(Y'_ξ)` and of the inverse image
`T_ξ` of `T` in `Y_ξ`, so that the codimension of this singular set in `Y_ξ` is equal to the infimum of
`codim(sing(Y'_ξ), Y'_ξ)` and of `codim(T_ξ, Y_ξ)`. Let us restrict ourselves to `ξ` such that `sing(Y'_ξ)` is finite
(which is harmless: this leads to placing ourselves in the complement of a set of codimension `≥ 2`). The singular
geometric points of `Y'_ξ` are therefore isolated. The conclusion follows easily from this and from (5.8.4).

Combining (5.8.13), (5.8.5), and (5.8.6), we find in the usual manner:

**Corollary (5.8.14).**

<!-- label: V.5.8.14 -->

*Suppose that `f : X → P` is unramified and that `X` has no isolated points.[^v-5p1-45]*

*(a) Suppose `X` is separable over `k`. In order that the set of `ξ ∈ P^∨` such that `φ_ξ` is `F_{k(ξ)}`-regular and
`Y_ξ` is separable, should have a complement of codimension at least two, it is necessary and sufficient that every
irreducible component `X_i` of `X` of dimension one should be formed from smooth points of `X` and should be ruled
relative to `f`, and that for every closed point `x` of `X` such that `dim_x X ≥ 2` we have `prof_x X ≥ 2` (conditions
that are automatically satisfied if `X` is geometrically normal and if all of its irreducible components are of
dimension `≥ 2`).*

*(b) Suppose that `X` is geometrically normal. In order that the set of `ξ ∈ P^∨` such that `φ_ξ` is `F_{k(ξ)}`-regular
and `Y_ξ` is geometrically normal should have a complement of codimension at least two, it is necessary and sufficient
that every irreducible component `X_i` of `X` of dimension `≤ 2` should be formed of smooth points of `X` and should be
ruled relative to `f`, and that in addition for every closed point `x` of `X` such that `dim_x X ≥ 3` we have
`prof_x X ≥ 3`.*

**Remark (5.8.15).**

<!-- label: V.5.8.15 -->

*In (5.8.6), (5.8.13), and (5.8.14) we make for `X` the hypothesis `(S_k)` (respectively `(R_k)`, respectively
separable, respectively geometrically normal) that we wish to recover as a conclusion for the hyperplane sections,
except perhaps for `ξ` in an exceptional set of codimension at least two.*

<!-- original page 32 -->

This does not restrict the generality; to tell the truth, it would have been better to get rid of this preliminary
hypothesis, since we see immediately with the help of results of §IV.3.4 and §IV.5.12 that if `X` does not satisfy the
hypothesis in question, then (by §V.5.5) if there exists a closed point `x` where the hypothesis fails, then for every
`ξ` such that `φ_ξ` is `F_{k(ξ)}`-regular (a condition that only eliminates a set of codimension one)[^v-5p1-46] and
such that `x ∈ Y_ξ` (a condition that describes a set of exact codimension one), `Y_ξ` does not satisfy the said
hypothesis at `x`; the exceptional set `Z ⊂ P^∨` is of codimension one and not two. (I may have somewhat exaggerated the
case `(R_k)` where we still need some condition: `(S_1)` and perhaps equidimensionality.)

> *Grothendieck note (regret).* In (5.8.13) and (5.8.14) it suffices to suppose that `f : X → P` is unramified at the
> smooth points of `X`; for the sufficiency part it suffices only that they should be unramified over an open subset
> `X'` of `X` whose complement has codimension `≥ k + 1`.

**Proposition (5.8.16).**

<!-- label: V.5.8.16 -->

*Suppose `f : X → P` unramified on an open subset complementary to a set of codimension at least two, `X` geometrically
normal and of depth at least three at its closed points, and finally `X` geometrically integral and proper over `k`.
Then the set of `ξ ∈ P^∨` such that `Y_ξ` is geometrically normal and geometrically integral of dimension equal to
`dim X − 1` is constructible and has a complement of codimension at least two.*

Indeed, by (5.8.14) (b), such is the case for the property "`Y_ξ` is geometrically normal of dimension `dim X − 1`" (the
dimensional property expressing that `φ_ξ` is `F_{k(ξ)}`-regular). Therefore, by (5.6.1), all the `Y_ξ` are
geometrically connected. Since `Y_ξ` is geometrically normal, it is geometrically integral if and only if it is
geometrically connected, which gives the proof.

**Remarks (5.8.17).**

<!-- label: V.5.8.17 -->

*(a) The hypothesis of (5.8.16) implies that `dim X ≥ 3`. It is possible that, as soon as `X` is geometrically
irreducible and `dim f(X) ≥ 3` (without the hypothesis of normality and non-ramification), the set of `ξ` such that
`Y_ξ` is geometrically irreducible has a complement of codimension at least two. We can prove in every case that it does
not contain a hyperplane (see below).*

*(b) The conclusion of (5.8.16) is false if we leave out the assumption that `prof_x X ≥ 3` for `x` closed. For example,
it is false for a non-singular quadric `X` in `ℙ³`,[^v-5p1-47] whose hyperplane sections are reducible (in fact formed
by pairs of concurrent lines) and form therefore a two-dimensional family, hence of codimension one in `P^∨` (indeed the
dual of the quadric is a quadric in the dual space relative to the dual form).*

<!-- original page 33 -->

In the case of a non-singular surface in a projective space this situation should however be considered as exceptional,
[as we shall see] in the following subsection.

Let us suppose `X` integral and proper over `k` and `f` an immersion. Then it follows from (5.6.1), (5.8.7), and
(5.8.14) that if `Y^{sing} → P^∨` is not generically finite and inseparable, the set of `ξ ∈ P^∨` such that `Y_ξ` is
separable over `k(ξ)` with at most two irreducible components has a complement of codimension at least two.

We shall now examine more precisely the case of surfaces. (The case of curves does not arise, from the point of view of
irreducibility of hyperplane sections.)

> *Grothendieck note.* I noticed with fright that the quadric is not entitled to be called ruled in the sense in which I
> have been using the word "ruled". This is in disagreement with our forefathers,[^v-5p1-48] and it would be necessary
> to invent a more adequate word for the notion used here.

**Proposition (5.8.18).**

<!-- label: V.5.8.18 -->

*Suppose that `k` is algebraically closed, `X` is integral (respectively integral and normal) of dimension `≥ 2` and
proper over `k`. Let `T` be a closed finite subset of `X` such that `X − T` is smooth, and let `f | (X − T)` be
unramified. In order that the set of `ξ ∈ P^∨` such that `Y_ξ` is geometrically irreducible (respectively geometrically
integral) of dimension `d − 1` should have a complement of codimension `≥ 2`, it is necessary and sufficient that the
following conditions be satisfied:*

*(a) For every `x ∈ T`, there exists a hyperplane section `Y_ξ` (`ξ ∈ P^∨(k)`) passing through `x`, of dimension
`d − 1`, and which is irreducible.*

*(b) `X' = X − T` is "ruled" (sic) for `f`, or there exists a hyperplane section `Y_{ξ_0}` (`ξ_0 ∈ P^∨(k)`) of `X'`
which is of dimension `d − 1`, non-singular, and irreducible.[^v-5p1-49]*

Let us first assume that `X` is geometrically normal. We have already seen (by (5.8.14) (a)) that we can find a closed
subset `Z'` of `P^∨` of codimension `≥ 2` such that `ξ ∈ P^∨ − Z'` implies that `Y_ξ` is separable over `k(ξ)` and of
dimension `d − 1`. For such a `ξ`, it amounts to the same thing that `Y_ξ` should be geometrically irreducible or
geometrically integral, and the two problems[^v-5p1-50] considered in (5.8.18) are therefore equivalent. On the other
hand, by (5.5.6), the set `U` of `ξ ∈ P^∨` such that `Y_ξ` is geometrically integral of dimension `d − 1` (the dimension
hypothesis stating that `φ_ξ` is `F_{k(ξ)}`-regular) is open. We will exhibit a non-empty open subset `P^∨ − Z`
contained in `U`, taking for `Z` the union of `g(Y^{\prime,sing})` and of the hyperplanes `H_x` of `P^∨` defined by the
`f(x)`, `x ∈ T`. For `ξ ∈ P^∨ − Z`, `Y_ξ` is smooth of dimension `d − 1`, and since it is geometrically connected by
(5.6.1), it is geometrically integral. We have to express (prove) that every irreducible component of codimension one of
`Z` meets the open set `U`. But these irreducible components are the `H_x` (possibly repeated, but it is not essential)
and

<!-- original page 34 -->

also `g(Y^{\prime,sing})` when the latter is indeed of codimension one, i.e. `X'` "not ruled" for `f`. (N.B. We use the
irreducibility of `Y^{\prime,sing}`.) On the other hand, in order that this latter set should meet the open set `U`, it
is necessary and sufficient that `g(Y^{\prime,sing})` (which contains an open dense set) should meet `U`. This proves
(5.8.18) in this case. If we do not suppose that `X` is normal, we apply the previous result to the normalization of
`X`; the reasoning is immediate and I do not give the details here.

(N.B. In the geometrically integral case, (5.8.18) is contained in (5.8.16), more precisely, except in the case `d = 2`.
It is for the case of geometric irreducibility that it may be better not to require `d = 2` and not only `d ≥ 2`.)

It remains to make explicit the conditions (a) and (b) of (5.8.18). This leads us to examine in a general way the
following situation. Suppose that `X` is geometrically irreducible over `k`, and consider a linear subvariety `L` of `P`
(corresponding to the question of studying the hyperplane sections of `X` passing through a given point `x`, or tangent
to `X` at a given smooth point), formed therefore by the hyperplanes containing a linear subvariety `L_0` of `P`
(respectively a point, or the image of a tangent space to `X` at a smooth point, in the two cases considered). We ask
the question whether for the generic point of `L` (and hence for all points of a non-empty open subset of `L`), `Y` is
geometrically irreducible of dimension `dim X − 1`.

This is a variant of Bertini's theorem, which must appear in §V.5.3, and is treated by exactly the same method (or, if
one likes, reduces to it).[^v-5p1-51] The dimension question is settled simply by `f(X) ⊄ L_0`, i.e. by
`X' = f^{-1}(P − L_0)` being a dense open subset of `X`. Let `Q` be the projective space of hyperplanes passing through
`L_0`. (N.B. If `L_0` is defined by a vector subspace `F_0` of `E`, we have `Q = ℙ(F_0)`, and we consider the canonical
morphism (deduced from `F_0 → E`, cf. Chapter II)

```text
  u : P − L_0 ⟶ Q,
```

and we consider

```text
  g = u f' : f^{-1}(P − L_0) = X' ⟶ Q,
```

so that `L ≅ Q^∨` and the family of `X'_ξ` (`ξ ∈ L`) is nothing else than the family of hyperplane sections relative to
the morphism `g`. On the other hand, we see immediately that for every `ξ ∈ L`, "general" `X'` is dense in `X`, so that
`X'` is geometrically irreducible if and only if `X` is such. Granted this, the Bertini-Zariski theorem shows us that we
have the desired conclusion of irreducibility provided that `dim g(X') ≥ 2`. (To tell the truth, one could give a
converse to (5.3.1) as follows: if `X` is geometrically irreducible, `Y` is geometrically irreducible if and only if
either `dim f(X) ≥ 2`, or `dim f(X) = 1` and `f(X)` is contained in a straight line `D` defined over `k` and the generic
fibre of `X → D` is geometrically irreducible.) This also allows us, in the present version with `L`, to have a
necessary and sufficient condition for geometric irreducibility of `Y_ξ`, `ξ` generic in `L`.

From the cohomological[^v-5p1-52] point of view and in terms of field theory, we can express the condition in terms of
transcendence degree in the following fashion. We choose a "hyperplane at infinity" containing neither `L_0` nor `X`,
and we place ourselves in its complement, i.e. over a scheme of affine type essentially. We choose a basis of the space
of linear forms vanishing on `L_0`, say `T_1, …, T_p` (`p = codim(L_0, P)`), and we consider their inverse images
`t_1, …, t_p` in the field of fractions `K` of `X` (`X` assumed integral). At least one of the `t_i`, say `t_1`, is
`≠ 0`. Consider therefore `a_1 = t_2 / t_1, …, a_{p-1} = t_p / t_1`; then `dim g(X')` is nothing else but the
transcendence degree of `K(a_1, …, a_{p-1}) ⊂ K` over `k`. Therefore, if the transcendence degree is `≥ 2`, we are okay.
If it is one, then we must require that, over `\overline{k}`, `f(X)` be contained in a linear subvariety of `P`
containing `L_0` and of

<!-- original page 35 -->

dimension at most one, and that the generic fibre of `g : X' → g(X')` should be geometrically irreducible.

Suppose that `L_0` is of dimension `q`, so that the fibres of `u : P − L_0 → Q` are of dimension `q + 1`, and hence
those of `g` are of dimension `≤ q + 1`. Consequently we have `dim g(X') ≥ dim f(X) − (q + 1)`, so that the dimension
condition for `g(X')` is verified provided `dim f(X) ≥ q + 3`. If `q = 0`, we find the fact indicated in (5.8.17) (a).
Returning to the conditions of (5.8.18), we see that condition (a), relative to an `x ∈ T`, is satisfied provided that
`X` is not "conical at `x` relative to `f`" in an obvious sense.

> *Grothendieck note.* Maybe it will be better to introduce these latest Bertinisque developments in the next
> subsection, "Change of projective immersion".

______________________________________________________________________

[^v-5p1-1]: Translator's note: Blass renders this as "pêle mêle Fr". The French *pêle mêle* ("pell-mell", "jumbled
    together") is preserved here as "pell-mell" to keep Grothendieck's deliberately informal tone in his
    covering letter. The original Blass text retains the French.

[^v-5p1-2]: Translator's note: Blass adds a marginal "Ask AG if No. 16 has ever been written. [Tr]". The Vaiello unified
    edition records that §V.5.16 was never written; the present part 1 stops well before §V.5.9, so the question
    is deferred to part 2.

[^v-5p1-3]: Translator's note: Blass writes "compare Par. 19 [of EGA IV Tr.]" and adds a footnote that this "uses
    notation of new edition of EGA I [Tr.]". We render §V.19 (formerly EGA IV §19) which is the natural
    cross-reference in the renumbered scheme.

[^v-5p1-4]: Translator's note: Blass writes "of finite type over `P` [Tr]" with the marginal query "or over `S`, I am
    not sure [Tr]". The intended meaning is clearly "of finite type over `S`, with a structural morphism
    `f : X → P`"; the apparent ambiguity is between the structural morphism and the morphism through which `X`
    becomes a `P`-scheme, which is `f` itself. We adopt the natural reading.

[^v-5p1-5]: Translator's note: Blass adds the marginal query "Ask A.G. if module always means coherent or quasi-coherent
    sheaf of modules". In the standard EGA usage of the period, "module" without qualifier defaults to
    "quasi-coherent module"; we follow that convention here.

[^v-5p1-6]: Translator's note: Blass adds a marginal query "Ask Grothendieck: What is the meaning and role of underlined
    capital letters, in Section One for example". The underlined capitals in §V.5.1 (here normalized to upright
    capitals) appear in the source PDF as ordinary closure overlines indicating Zariski closure; we render them
    as `\overline{(\cdot)}` in displays and `Z̄` or "closure of `Z`" in prose.

[^v-5p1-7]: Translator's note: Blass adds the marginal query "Tr: clear up this reference. Is it EGAIV?" — yes, the
    reference is to EGA IV §6, which we render as "§IV.6".

[^v-5p1-8]: Translator's note: the source carries an editorial "incomprehensible" marker at this point. The reduction to
    `k` algebraically closed is the standard one (radical multiplicity at a prime cycle is preserved by the
    regular morphism `Y_η → X`, and the algebraic-closure base change is faithfully flat), and we render the
    sentence as the intended reduction.

[^v-5p1-9]: Translator's note: Blass adds the marginal remark "`X` unramified or `k` of characteristic zero". Either
    condition suffices: if `f` is unramified the proof in (5.2.12) goes through; if `k` is of characteristic
    zero, smooth = regular for algebraic preschemes.

[^v-5p1-10]: Translator's note: Blass writes "Si to Si [PB: check this!]" with the marginal "Probably `S_i` to `[S_i]`,
    equivalence class of `S_i` in `L` [Tr.]". We render this as the natural inclusion sending each affine
    coordinate `S_i` to its image in `L`.

[^v-5p1-11]: Translator's note: Blass adds the marginal "primary extension probably means that the smaller field is
    algebraically closed in the larger one (or quasi algebraically closed) [Tr]. Jouanolou Th. 3.6 [Tr]". This
    is correct: "primary" here means "regular" in the sense of Bourbaki, *Alg. comm.*: `k` is algebraically
    closed in `K`, or equivalently `K ⊗_k \overline{k}` is reduced and `K` is geometrically irreducible over
    `k`.

[^v-5p1-12]: Translator's note: Blass writes "in par. 6" with a marginal query; we render as §IV.6 since Hartshorne's
    connectedness theorem in the form Grothendieck uses appears in EGA IV §6 (more precisely §IV.15.6.3 in the
    published EGA IV, which is invoked again in (5.6.1) below).

[^v-5p1-13]: Translator's note: Blass writes "the previous two [Tr] sections" with a marginal query about the referent.
    Reading the source, the "previous two" are §§V.5.2 and V.5.3 — the local-properties and
    irreducibility-connectedness subsections we have just translated.

[^v-5p1-14]: Translator's note: Blass appends "(extension prealable Fr)". The French *extension préalable* ("prior
    extension") is a standard EGA expression for "a base change made before applying the construction"; we
    render as "prior extension of the base field".

[^v-5p1-15]: Translator's note: the source labels this Proposition 4.2 rather than 4.1; there is no 4.1 in the prenote
    (the introductory subsection numbered 4.1 is absorbed into the running text). We preserve the original
    numbering, since reordering would shift downstream references.

[^v-5p1-16]: Translator's note: Blass adds the marginal query "What is AQT? Ask AG.". The abbreviation appears nowhere
    else in the prenote; it is most plausibly "Artin-Quasi-finite Trick" or "abstract quotient technique",
    referring to a standard descent argument from §IV.9. We retain the marker since it has no settled
    expansion.

[^v-5p1-17]: Translator's note: Blass renders the Latin "Redactor demerdetur" — Grothendieck's own coinage, roughly "let
    the redactor extricate himself" — verbatim. We translate as "let the redactor sort himself out" and
    preserve the spirit of the original tag.

[^v-5p1-18]: Translator's note: Blass writes "paragraph 12" with the marginal "Locate that reference, most likely EGA IV
    [Tr], Yes [Tr].". We render as §IV.12, which is the openness-of-loci subsection in EGA IV the prenote
    points back to.

[^v-5p1-19]: Translator's note: Blass adds the marginal "Since `Y` is proper over `X` and `P^∨` is separated over `S`.
    (Marginal remark [Tr])". We incorporate this into the running argument.

[^v-5p1-20]: Translator's note: Blass writes "as Mike says" and adds a footnote "Mike Artin (I presume P.B.)". We render
    as "M. Artin".

[^v-5p1-21]: Translator's note: Blass adds the marginal "Ask AG about reference – probably EGA IV [Tr]. 12.1.4 does not
    check out [Tr].". §IV.12.1.4 is in fact the standard reference for openness of properties in flat families;
    the indexing in the published EGA IV is `(IV, 12.1.4)` and refers to the openness of the geometric
    properties listed in §IV.12.1.1.

[^v-5p1-22]: Translator's note: Blass writes "for sure" with the marginal "or to be sure [Tr]". The French residue *pour
    de bon* ("definitely", "for sure") is retired to "to be sure".

[^v-5p1-23]: Translator's note: Blass adds "(by successive approximations ???)" with a footnote "Translator's note: *de
    proche en proche* [Fr.]". The French *de proche en proche* ("step by step", "by successive approximations")
    is rendered as "by successive approximations" in scare quotes, since the construction is precisely the
    iterative one Grothendieck describes.

[^v-5p1-24]: Translator's note: Blass writes "in the case (v) that for every `s ∈ S` [illegible] irreducible component
    `Z` of `X_s` we have `dim f(Z) ≥ 2`. \[Nota Bene: For (v) compare 12.2.1 (x) and (xi) (we can then
    [illegible] in the other case 4.3 or 12.2.1 (x)\] (marginal remark largely illegible in preceding square
    brackets)". We follow the Vaiello reconciliation in restoring the intended hypothesis "in case (v), for
    every `s ∈ S` and every irreducible component `Z` of `X_s`, `dim f(Z) ≥ 2`".

[^v-5p1-25]: Translator's note: Blass adds the marginal "Unclear, ask AG.". The statement is clear in the Vaiello
    edition: when `k(s)` is infinite, the multisection `S'` may be realized inside `X_U` as a closed subscheme;
    in the finite-residue-field case one needs an étale extension first.

[^v-5p1-26]: Translator's note: Blass marks "by taking `X` étale non-finite over `S` …" with "Illegible". The intended
    example is the standard one: an étale cover that is not finite, e.g. an open immersion that is étale but
    not surjective, can fail to admit a multisection of the required type.

[^v-5p1-27]: Translator's note: Blass writes "(see Section No.29 for examples)" with the marginal "Section number
    omitted, ask A.G.". The reference is to the subsection on pencils of hyperplane sections (§V.5.10 in our
    numbering), treated in part 2.

[^v-5p1-28]: Translator's note: Blass renders the Latin "Redactor decidetur" (Grothendieck's coinage) with the footnote
    "Editor decide". We translate as "Let the redactor decide".

[^v-5p1-29]: Translator's note: Blass writes "we have `dim f(X_i) >`[illegible, is it two, ask A.G.]". The PDF resolves
    this as "`≥ 2`", which matches the rest of the proof; we drop the marker.

[^v-5p1-30]: Translator's note: Blass marks the property failing "(S_k)" with an "Illegible, ask A.G."; the context
    (irreducible component of codimension `≥ 2` of `G_ξ` failing the property `(S_k)` already enjoyed by `F`)
    makes the intended statement clear.

[^v-5p1-31]: Translator's note: Blass writes "is quite floppy (or perhaps sloppy) [Tr]". We preserve the
    Grothendieck-style self-deprecation as part of the prenote character.

[^v-5p1-32]: Translator's note: Blass marks the condition with "Illegible, ask A.G.". The Vaiello reconciliation
    restores it as "we have at most simple embedded components" (cf. EGA IV §IV.5.10 for the condition on
    associated prime cycles), but we preserve Blass's marker to flag the source ambiguity.

[^v-5p1-33]: Translator's note: Blass writes "the coprof_x [illegible]" — the natural reading (and the one consistent
    with §V.5.8 below) is `coprof_x F ≥ n`, i.e. that `x` lies in the level set of the codepth function.

[^v-5p1-34]: Translator's note: Blass writes "for every closed subset `R` of [illegible, ask A.G.]"; the referent in
    context is `X` (the ambient prescheme), as confirmed by the conclusion of the sentence.

[^v-5p1-35]: Translator's note: Blass writes "(par. 16)" with the marginal "See part II of these notes [Tr]". In our
    numbering, this is §V.1 (formerly EGA IV §16), the singular-and-supersingular-zeros subsection.

[^v-5p1-36]: Translator's note: Blass writes "No. 16 or paragraph 16" with the marginal "Ask AG about this reference –
    just later part of these notes". The reference is to §V.1 of these notes (the singular-zeros subsection),
    where the locally-free-module diagram is set up.

[^v-5p1-37]: Translator's note: Blass writes "\[Note to AG, the upper G is really an illegible letter `P^∨/S` what is
    this?\]". The intended object is the relative tangent sheaf `𝒢_{P^∨/S}` (kernel of the augmentation
    `𝒫^1_{P^∨/S} → 𝒪_{P^∨}`), in line with the §V.1 conventions; we render it `𝒢_{P^∨/S}`.

[^v-5p1-38]: Translator's note: Blass writes "section `ψ` [Blass: check if this letter is OK]"; the section is the
    differential `Ψ = (dφ) |_Y` introduced just above, with the lowercase variant used in the diagram
    verification. We follow Blass and write `ψ` here.

[^v-5p1-39]: Translator's note: Blass numbers this as Corollary 8.9, skipping 8.8 (the proof of (5.8.7) absorbs what
    would have been 8.8). We preserve the prenote numbering, so there is a gap between (5.8.7) and (5.8.9).

[^v-5p1-40]: Translator's note: Blass writes "[la taupe Fr]" — French *la taupe* literally "the mole", Grothendieck's
    slang for classical (pre-EGA) geometers (cf. *en termes de papa* in §V.1). We render as "the classical
    language".

[^v-5p1-41]: Translator's note: Blass writes "if you feel inspired to make connection with [la taupe Fr]". We restate as
    "make a connection with classical terminology".

[^v-5p1-42]: Translator's note: Blass writes "[illegible] `x ∈ X(k)` so `T` contains" with "illegible" markers; the
    natural reading is "any `x ∈ X(k)` is contained in `T`", since if `dim X = 1` the variety `X` itself is
    contained in its tangent variety.

[^v-5p1-43]: Translator's note: Blass adds a parenthetical "Do it Blass" — Grothendieck's working note to his
    translator. The examples in characteristic `p > 0` are the standard ones with a non-singular plane curve
    admitting strange tangent lines (cf. Hartshorne *Algebraic Geometry*, IV.3, Example 3.8.4).

[^v-5p1-44]: Translator's note: Blass writes "of dimension `≤ k − 1` (Ask A.G. illegible)". The dimensional bound
    `≤ k − 1` matches the Vaiello reconciliation and the geometric meaning of the statement; we drop the
    marker.

[^v-5p1-45]: Translator's note: Blass writes "[illegible] n.". The PDF does not resolve this marker; the sentence makes
    sense with the marker dropped, as it is clearly closing the preamble to (a) and (b).

[^v-5p1-46]: Translator's note: Blass writes "condition that only eliminate a set of codimension (illegible)"; the
    intended bound is "codimension `≥ 2`" — the regularity condition is generic — but we preserve the marker
    shape and write "codimension one" since the codimension-one set being eliminated is the trace of the
    non-regularity locus.

[^v-5p1-47]: Translator's note: Blass writes "for a non-singular quadric `X` in `P^3` [illegible]". The PDF resolves the
    marker as ordinary mathematical text continuing the example; we drop it.

[^v-5p1-48]: Translator's note: Blass writes "in disagreement with our fathers", the literal English for the French
    *avec nos pères* (our forefathers / our predecessors in the classical school). The variant *en termes de
    papa* recorded in §V.1 belongs to the same family of expressions.

[^v-5p1-49]: Translator's note: Blass writes "of dimension `d − 1` (non???) singular and irreducible.[^] \[illegible,
    ask A.G.\]". The PDF resolves the question mark — the section is non-singular and irreducible — and we drop
    the marker.

[^v-5p1-50]: Translator's note: Blass writes "the two problems [(respé et non respé) Fr. p. 50] (?)". The French *respé
    / non respé* are Grothendieck's shorthand for "respectively / not respectively", marking the parallel cases
    "geometrically irreducible" and "geometrically integral". We render as "the two problems" and let context
    carry the parallelism.

[^v-5p1-51]: Translator's note: Blass writes "which [j(devrait figurer) 51] must appear in No. 3, and is treated by
    exactly the same method, [(ou, si on veut, s'y ramène) Fr 51]". The French *qui devrait figurer / ou, si on
    veut, s'y ramène* glosses as "which must appear / or, if one prefers, reduces to it"; we render as a single
    clause.

[^v-5p1-52]: Translator's note: Blass writes "From the [(cunutesque?) Fr] point of view". The French marker is illegible
    in the PDF; the intended adjective is most plausibly *cohomologique* ("cohomological"), so we render
    "cohomological" while flagging the uncertainty.

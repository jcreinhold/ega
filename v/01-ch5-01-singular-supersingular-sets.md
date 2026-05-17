<!-- original page 1 -->

## §V.1. Singular and supersingular zeros of a function; differential criteria (formerly EGA IV §16)

This section was originally drafted as §16 of EGA IV, then re-allocated to EGA V (Chapter V §1) without ever being
published in either place. Grothendieck remarks at its head: *"This section will be used in §V.5 (formerly EGA IV §20)
on hyperplane sections, but its natural place seems to me to be here."*

The §V↔§IV correspondence is given in the front matter; we lead with the V numbering and attach `(formerly IV, M)`
parenthetically at the first occurrence of each cross-reference into the old numbering.

### V.1.1. The singular and supersingular zero of a section

**Definition (1.1).**

<!-- label: V.1.1 -->

*Let `X` be a regular prescheme, and `φ` a section of `𝒪_X`. A point `x ∈ X` is called a **singular zero** (or **root**)
of `φ` if `φ_x ∈ 𝔪_x²`. It is called a **supersingular zero** if it is a singular zero and if, in addition, the image of
`φ_x` in `𝔪_x² / 𝔪_x³ ≅ Sym²(𝔪_x / 𝔪_x²)` — interpreted as a quadratic form on the dual `t_x` of `𝔪_x / 𝔪_x²` over
`k(x)` — is degenerate. A singular zero that is not supersingular is sometimes called an **ordinary singular zero**.*

**Remark (1.2).**

<!-- label: V.1.2 -->

*If `x ∈ V(φ)`, then `x` is a non-singular zero of `φ` if and only if `φ_x ≠ 0` and `x` is a non-singular (that is,
regular) point of `V(φ)`, equivalently if and only if `x` is a regular point of `V(φ)` and `V(φ) ≠ X` in a neighbourhood
of `x`.*

**Definition (1.3).**

<!-- label: V.1.3 -->

*Let `X` be a smooth prescheme over a field `k`, `φ` a section of `𝒪_X`, and `x ∈ V(φ)`. We say that `x` is a
**geometrically singular** (resp. **geometrically supersingular**) zero of `φ` relative to `k` if for every extension
`k′/k` and every point `ξ` of `X` with values in `k′` localized at `x`, the corresponding point `x′` of `X_{k′}` is a
singular (resp. supersingular) zero of `φ_{k′}`.*

**Remarks (1.4).**

<!-- label: V.1.4 -->

*(a) From the criterion to be developed below it follows that in Definition (1.3) it suffices to test with a single
point with values in some `k′` — one can take `k′ = k(x)` or `\overline{k(x)}` and the canonical point with values in
this `k′`.*

*(b) From Remark (1.2) it follows that `x` is geometrically non-singular for `φ` if and only if `φ_x ≠ 0` and `V(φ)` is
smooth over `k` at `x`.*

*(c) Suppose given a prescheme `X` smooth over another prescheme `Y`, a section `φ` of `𝒪_X`, and an `x ∈ V(φ)`. We say
that `x` is a singular (resp. supersingular) zero **relative to `Y`** if it is a singular (resp. supersingular) zero
relative to `k(s)` over the fibre `X_s`, where `s` is the image of `x` in `Y`.*

*(d) Under the conditions of Definition (1.1), the singularity (resp. supersingularity) of an `x ∈ V(φ)` for `φ` is not
modified if one replaces `φ` by `φ′ = uφ` where `u` is a unit at `x`. It follows immediately that Definition (1.1), and
hence also Definition (1.3), extends in an obvious way to the case where `φ` is a section of an invertible module `L`
(in such a way as to recover the original definition when `L = 𝒪_X`).*

<!-- original page 2 -->

### V.1.5. Differential criteria; the zero set of `d⁰φ` and `d¹φ`

Let `X` be a prescheme smooth over another prescheme `Y`, and let `φ` be a section of `𝒪_X`. Then `φ` gives rise to a
section `d²_{X/Y} φ` of `𝒫^2_{X/Y}`, which reduces to a section `d¹_{X/Y} φ` of `𝒫^1_{X/Y}`, which itself reduces to the
section `d⁰φ = φ` of `𝒫^0_{X/Y} = 𝒪_X`.

**Proposition (1.5).**

<!-- label: V.1.5 -->

*The set of zeros of `d⁰φ` (resp. `d¹φ`) is equal to the set `V(φ)` of zeros of `φ` (resp. to the set `V(φ)_sing` of
zeros of `φ` singular relative to `S`).*

The first assertion is trivial. The second is just the Jacobian criterion, or — if one prefers — it follows from the
canonical isomorphism `𝔪_x / 𝔪_x² ≅ Ω^1_{X/k}(x)` valid when `x` is a rational point over `k` of a prescheme `X` over
`k`.

Note that `gr¹(𝒫^1_{X/Y}) ≅ Ω^1_{X/Y}`, so that the restriction `d¹φ |_{V(φ)}` can be interpreted as a section of
`Ω^1_{X/Y} ⊗ 𝒪_{V(φ)}`, which is precisely the restriction of `d_{X/Y} φ` to `V(φ)`. We can therefore consider the
prescheme of zeros of this section, which we denote `V(φ)_sing`, and whose underlying set is the set of zeros of `φ`
singular relative to `Y`, by Proposition (1.5).

*Aside.* If `ψ` is a section of a locally free module `E` of finite type over a prescheme `X`, one defines in an obvious
way the sub-prescheme of zeros of `ψ`, for example as defined by the image ideal of the map `E^∨ → 𝒪_X` given by the
transpose of `ψ`. When `E = 𝒪_X^n` and `ψ = (ψ_1, …, ψ_n)`, this ideal is just `∑ ψ_i 𝒪_X`, which defines
`V(ψ_1, …, ψ_n)`.

Now taking the restriction `d²φ |_{V(φ)_sing}` and noting that `gr²(𝒫^2_{X/Y}) ≅ Sym²(Ω^1_{X/Y})`, we obtain a canonical
section `M(φ)` of `Sym²(Ω^1_{X/Y}) ⊗ 𝒪_{V(φ)_sing}`. Taking points of `X` with values in fields, one sees immediately
that this section is precisely the one that determines the quadratic forms given in Definition (1.1) (in the case where
`X_k` is deduced from `X/S` by `Spec(k) → S`). One deduces a description of the set `V(φ)_{supsing}` in terms of this
section as follows: interpreting `M(φ)` as defining a homomorphism

```text
  M(φ)′ : 𝒢_{X/Y} ⊗_{𝒪_X} 𝒪_{V(φ)_sing} → Ω^1_{X/Y} ⊗_{𝒪_X} 𝒪_{V(φ)_sing},
```

take the set of points at which this homomorphism is not an isomorphism. This shows in particular that `V(φ)_{supsing}`
is a closed set. One can make the latter more precise by introducing

```text
  D(φ) = det M(φ) ∈ Γ(Ω^d_{X/Y})^{⊗ 2} ⊗ 𝒪_{V(φ)_sing}
```

and supposing that `X` has constant relative dimension `d` over `Y`. One may then use `V(φ)_{supsing}` to denote the
closed sub-prescheme of `V(φ)_sing` (and hence of `X`) defined by the vanishing of this section (now a section of an
invertible module), whose underlying set is the right one.

> *Grothendieck note.* It would be a good thing to summarize the above construction into a Proposition (1.6).[^v-1-1]

In the general case we cannot say anything more precise about `V(φ)_sing` and `V(φ)_{supsing}`. Let us examine a special
case that is interesting for certain applications.

<!-- original page 3 -->

### V.1.7. The supersingular set as a ramification locus

Assume that `Y` is also smooth over a prescheme `S`, with constant relative dimension `m` (to fix our ideas), and that
`V(φ)_sing`, which we denote `V′` for short — defined by the vanishing of the section `d¹` of the locally free module
`𝒫^1_{X/Y}` of rank `d + 1` — is smooth over `S` of relative dimension `(m + 1) − (d + 1) = m − 1`.

The notations `V(φ)_sing` and `V(φ)_{supsing}` are ambiguous in that the prescheme over which they are defined is left
implicit; we tacitly fix `Y`.[^v-1-2] Note that it follows from the assumptions that every singular zero of `φ` is
non-singular relative to `S`. In this situation one can write down the following diagram of locally free modules over
`V′`:

```text
                                            0
                                            ↑
                                  Ω^1_{X/Y} ⊗ 𝒪_{V′}
                                       ↗
                                  μ ↗
                                ↗
   0 → 𝒫^1_{X/Y} ⊗ 𝒪_{V′}  →  Ω^1_{X/S} ⊗ 𝒪_{V′}  →  Ω^1_{V′/S} → 0
              ↑                       ↑                  ↘
                                                       ↘ ν
              ↑                       ↑                  ↘
       𝒪_{V′}             →    Ω^1_{Y/S} ⊗ 𝒪_{V′}
              ↑                       ↑
   ω^{−2}_{X/Y} ⊗ 𝒪_{V′}             0
```

The columns come from the transitivity exact sequence for the smooth morphisms `X → Y` and `Y → S`, tensored with
`𝒪_{V′}` (this remains exact since all the modules involved are locally free). The horizontal line is a particular case
of an exact sequence obtained whenever, over `X/S`, we have a section `ψ` of a locally free module `F`, and take the
scheme of zeros `W`:

```text
  F^∨ ⊗ 𝒪_X → Ω^1_{X/S} ⊗ 𝒪_W → Ω^1_{W/S} → 0;
```

if `X/S` is smooth, the first homomorphism is injective exactly at the points where `W` is smooth over `X` with a "good"
relative dimension (here, everywhere). This exact sequence is an immediate consequence of the exact sequence

```text
  𝒥/𝒥² → Ω^1_{X/S} ⊗ 𝒪_W → Ω^1_{W/S} → 0
```

appearing in §V.1.5; the version we use here could be stated as its corollary.

The characterization of the set of points where the left-most arrow fails to be a monomorphism is contained in the
Jacobian criterion.

<!-- original page 4 -->

Note the canonical isomorphism `𝒫^1_{X/S} ≅ Ω^1_{X/S} ⊕ 𝒪_X`, whence `𝒫^1_{X/S} ⊗ 𝒪_{V′} ≅ 𝒢_{X/S} ⊕ 𝒪_X`.[^v-1-3] On
the other hand, one verifies that the composed homomorphism `μ` in the diagram above is zero on the factor `𝒪_{V′}`, and
on the factor `𝒢_{X/S} ⊗ 𝒪_{V′}` it reduces to the homomorphism `M(φ)′` deduced from the section `M(φ)` of
`Sym²(Ω^1_{X/S}) ⊗ 𝒪_{V′}` already mentioned. Thus at a point `x ∈ X`, `M(φ)` is non-degenerate — that is, `M(φ)′` is
surjective — if and only if `μ` is surjective at `x`, and we see from the diagram that this is also equivalent to saying
that `ν` is surjective at `x` (since both conditions assert that the canonical homomorphism from the sum of the two
cited submodules of `Ω^1_{X/S} ⊗ 𝒪_{V′}` into the latter is surjective at `x`).

We therefore find:

**Proposition (1.7).**

<!-- label: V.1.7 -->

*Under the preceding conditions (to be recalled), the underlying set of `V(φ)_{supsing}` is exactly the set of points of
`V(φ)_sing` at which the morphism `V(φ)_sing → Y` (of smooth preschemes over `S` of relative dimensions `m − 1` and `m`,
respectively) is ramified.*

In the old language[^v-1-4] — which should perhaps be added as a remark — a point `x ∈ V(φ)` is supersingular relative
to `Y` if and only if "it consists of at least two coinciding (infinitely near) singular points."

We must make Proposition (1.7) more precise from the point of view of an identity of sub-preschemes, not just of
subsets. Indeed, `V(φ)_{supsing}` has been defined as a closed sub-prescheme of `X`; on the other hand, we can equally
well define a natural closed sub-prescheme of `V′` whose underlying subset is the set of ramification points relative to
`Y`. Indeed, it suffices to express the set of points where a certain homomorphism of locally free modules
`Q = Ω^1_{Y/S} ⊗ 𝒪_{V′} → M = Ω^1_{V′/S}` fails to be surjective. If `q` and `r` are their respective ranks, this is
also the set of points where `Λ^q Q → Λ^r M` fails to be surjective, equivalently the zero set of the evident section of
`Hom(Λ^q Q, Λ^r M) ≅ (Λ^q Q)^∨ ⊗ Λ^r M`. We thus obtain a closed sub-prescheme of zeros of this section, which we call
`Ram(V′/Y)`.

*Claim.* `Ram(V′/Y) = V(φ)_{supsing}` (as closed sub-preschemes of `V′`).

This is a straightforward exercise on the diagram above, taking into account that `V(φ)_{supsing}` is defined by the
same procedure as the one made explicit for `Q → R` but in terms of the homomorphism
`𝒫 = 𝒫^1_{X/Y} ⊗ 𝒪_{V′} → S = Ω^1_{X/Y} ⊗ 𝒪_{V′}`, as follows from the description of `μ` given above. We are thus
reduced to the following general situation.

<!-- original page 5 -->

### V.1.8. A general lemma on locally free modules

We have on a ringed space `W` a locally free module `M` of rank `m`, and two locally free submodules `P` and `Q` of
respective ranks `p` and `q` with `p + q = m + 1`. Using the previous construction, applied to the morphisms
`P → M/Q = S` and `Q → M/P = R`, we find the sections

(a) of `P ⊗ det S ⊗ det P^{−1} = P ⊗ det M ⊗ det P^{−1} ⊗ det Q^{−1}`, and

(b) of `Q ⊗ det M ⊗ det P^{−1} ⊗ det Q^{−1}`,

which we may also view as homomorphisms of `L = det P ⊗ det Q ⊗ det M^{−1}` into `P` and into `Q`, respectively.

(For a locally free module `F` we denote by `det F` its highest exterior power; we use the fact that for a short exact
sequence

```text
  0 → F′ → F → F″ → 0
```

of locally free modules of finite rank we have a canonical isomorphism `det F = det F′ ⊗ det F″`.)

With these conventions, we have the commutativity of the diagram[^v-1-5]

> *Source-trace note: the Blass source file 01 ends mid-diagram on page 5; the diagram and the subsequent argument are
> visible in the source PDF  but were not captured by the Blass markdown transcription.
> We close §V.1 here with the construction already stated and refer the reader to the PDF for the final identification
> step that pins down `Ram(V′/Y) = V(φ)_{supsing}` as preschemes (rather than only as subsets).*

______________________________________________________________________

[^v-1-1]: Translator's note: in the source, this appears as Grothendieck's marginal aside ("It would be a good thing to
    summarize the above construction into a Proposition 6"). No Proposition (1.6) was ever written; we preserve
    the gap in numbering between (1.5) and (1.7) as in the prenote.

[^v-1-2]: Translator's note: Blass renders this with the parenthetical "(in the actual case it is assumed (sous entendu
    Fr) that it is `Y`)". The French *sous-entendu* ("understood", "tacitly assumed") survives in the Blass
    source; we modernize to "tacitly fix".

[^v-1-3]: Translator's note: Blass writes "(in the original the G is elongated)" at this point. The elongated `G` refers
    to the symbol Grothendieck uses for the tangent sheaf `𝒢_{X/S}` (kernel of the augmentation `𝒫^1 → 𝒪`); we
    render it `𝒢_{X/S}` throughout. Blass himself queries: "Is the elongated G the tangent sheaf? [Tr]". The
    answer is yes.

[^v-1-4]: Translator's note: Blass renders this as "in the language of the fathers (en termes de papa Fr)". The French
    *en termes de papa* ("in dad's terms") is Grothendieck's affectionate phrase for classical (pre-EGA)
    algebraic-geometry vocabulary; we render "in the old language".

[^v-1-5]: Translator's note: the Blass source ends here ("This being given, we have the commutativity of the diagram")
    with the diagram itself untranscribed; we end the section at the verbal claim and direct the reader to the
    source PDF for the remaining lines of the argument.

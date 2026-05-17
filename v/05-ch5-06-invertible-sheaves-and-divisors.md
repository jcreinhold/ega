<!-- original page 1 -->

## §V.6. Invertible sheaves and divisors relative to projective and multiprojective fibrations; linear systems of divisors (formerly EGA IV §21)

This section was originally drafted as §21 of EGA IV, then re-allocated to EGA V (Chapter V §6) without ever being
published in either place. We lead with the §V numbering and attach `(formerly IV, 21)` parenthetically at the first
occurrence of each cross-reference into the old numbering; subsequent in-section cross-references use V numbering alone.

The four subsections, following the prenote's own table of contents, are:

1. Invertible sheaves on projective and multiprojective fibrations.
1. Representability of `Div^L_{X/S}`: relative divisors on projective and multiprojective fibrations.
1. Linear systems of divisors and morphisms into projective fibrations.
1. Linear systems of divisors and invertible modules.

The results developed here, and in the following section, are already partly *global* in nature; they give complements
about projective schemes (`II`, `III`) and pure local results of the present Chapter V. One of the aims of the paragraph
is to develop the language of *linear systems of divisors*, which is connected on the one hand to the classification of
morphisms into a projective fibration, and on the other to the classification of invertible modules over a given
prescheme.

The "parameter schemes" really natural for the linear systems of divisors are the **Brauer-Severi schemes**, which
generalize projective fibrations and may be defined, for example, as those fibrations which become isomorphic to a
projective fibration after an étale surjective base extension. Since their study uses descent theory (taken up in
Chapter V[^v-6-1] of the original design), and since their classification is equivalent to the classification of torsors
under the projective group, we postpone the study of such schemes — and of their connection with the notion of linear
system — to Chapter VI.

From a technical point of view, the main result of the section is Theorem (1.1), which determines the Picard group of a
projective fibration in terms of that of the base, together with its immediate corollaries in subsections 1 and 2.

<!-- original page 2 -->

### V.6.1. Invertible sheaves on projective fibrations; automorphisms

> *Editorial note (Blass).* The bulk of this subsection was crossed out in the manuscript up to the point we shall
> indicate below; we restore it in full.

This subsection treats the determination of invertible sheaves on a projective fibration and its application to the
automorphisms of such a fibration.

**Theorem (1.1).**

<!-- label: V.6.1.1 -->

*Let `S` be a prescheme, `E` a locally free `𝒪_S`-module of finite rank `≥ 2` at every point, and `P = ℙ(E)` the
projective fibration that it defines, with structural morphism `f : P → S`. Then for every invertible module `L` over
`P` one can find a family `(S_n)_{n ∈ ℤ}` of disjoint open subsets of `S` covering `S`, indexed by `ℤ`, and an
invertible module `M` over `S`, such that the restriction of `L` to `f⁻¹(S_n)` is isomorphic to that of*

```text
  M ⊗ 𝒪_P(n) = f*(M)(n).
```

*Moreover, the family `(S_n)` is uniquely determined by these conditions, and `M` is then determined up to a unique
isomorphism.*

**Remark (1.2).**

<!-- label: V.6.1.2 -->

*If we drop the assumption on the rank of `E`, then `S` decomposes canonically into the sum-prescheme of three open
subsets `S^0`, `S^1`, `S^2` over which the rank of `E` is respectively `0`, `1`, and `≥ 2`. The determination of the
invertible modules over `P` reduces to that over `f⁻¹(S^i)` for `i = 0, 1, 2`. The case `i = 2` follows from (1.1); on
the other hand, `f⁻¹(S^1)` is `S^1`-isomorphic to `S^1`, so its Picard group is just `Pic(S^1)`; and finally `f⁻¹(S^0)`
is empty, so its Picard group is zero.*

**Corollary (1.3).**

<!-- label: V.6.1.3 -->

*Under the assumptions of (1.1), suppose moreover that `S` is connected and non-empty. Then every invertible module `L`
over `P` is isomorphic to a module of the form `f*(M)(n)`, where `n ∈ ℤ` and `M` is an invertible module over `S`.
Furthermore `n` is uniquely determined, and `M` is determined up to a unique isomorphism, by the data of `L`.*

Another way to formulate this corollary is the following. Consider the natural homomorphisms `Pic(S) → Pic(P)` (deduced
from `f : P → S`) and `ℤ → Pic(P)` (determined by the class `[𝒪_P(1)] ∈ Pic(P)`). We deduce a canonical homomorphism

```text
  (*)             Pic(S) × ℤ ⟶ Pic(P),
```

defined in any case, without any restrictive assumption on `S` or on `E`. This gives:

**Corollary (1.4).**

<!-- label: V.6.1.4 -->

*Under the conditions of (1.1), if `S ≠ ∅`, then the homomorphism `(*)` is injective; it is bijective if `S` is also
connected.*

If we drop the assumption that the rank of `E` is `≥ 2`, it follows from (1.2) and (1.4) that the homomorphism `(*)` is
still surjective when `S` is connected, but not necessarily injective: its kernel is isomorphic to `ℤ` if `E` is of rank
`1`, and to `Pic(S) × ℤ` if `E` is of rank zero.

#### Proof of (1.1).

We start from *uniqueness*. Suppose first `S = Spec(K)` is the spectrum of a field. Then `𝒪_P(n)` is not isomorphic to
`𝒪_P(m)` for `n ≠ m`; equivalently, `𝒪_P(m − n)` is not isomorphic to `𝒪_P` unless `m − n = 0`. Indeed, this follows
from the fact that `𝒪_P(1)` is ample and `dim P ≥ 1` (which uses `rank E ≥ 2`): we may suppose `d = m − n ≥ 0`; if
`d > 0`, then `𝒪_P(d)` would be ample, so it could be isomorphic to `𝒪_P` only if `P` were quasi-affine, hence finite
(since it is proper over `K`) — contradicting `dim P ≥ 1`. This already proves the uniqueness of the family `(S_n)`.

For the uniqueness of `M` up to a unique isomorphism, we are reduced to the case `S = S_n`. In this case the isomorphism

```text
  (**)            M ⥲ f_*(L(−n))
```

is uniquely determined by the isomorphism `L ⥲ f*(M)(n)`. Indeed, the latter defines an isomorphism `L(−n) ⥲ f*(M)`,
which yields an isomorphism of the right-hand side of `(**)` with `f_*(f*(M)) ≅ M ⊗ f_*(𝒪_P)`, and since
`f_*(𝒪_P) ⥲ 𝒪_S`, we deduce `(**)`.

We now prove *existence* of the `(S_n)` and `M`. By the uniqueness already shown the question is local over `S`, so we
are reduced to the following corollary:

<!-- original page 3 -->

**Corollary (1.5).**

<!-- label: V.6.1.5 -->

*Let `E` be locally free of finite rank over `S`, `P = ℙ(E)`, `L` an invertible module over `P`, and `s ∈ S`. Then there
exists an open neighbourhood `U` of `s` and an integer `n ∈ ℤ` such that `L | f⁻¹(U)` is isomorphic to
`𝒪_P(n) | f⁻¹(U)`.*

Of course, since the rank of `E` at `s` is `≥ 2`, the integer `n` is well defined.

Moreover, (1.5) is trivial when the rank of `E` at `s` is `≤ 1`. So we may assume that `E` is locally free of constant
rank `≥ 2`; the question being local, we may suppose `E = 𝒪_S^{r+1}` and hence `P = ℙ^r_S`.[^v-6-2] By the standard
brief procedure of (IV, §8), we are also reduced to the case where `S` is noetherian. We proceed in two steps:

**(a)** Suppose `S = Spec(K)` is the spectrum of a field. Then `L` is defined by a graded module of finite type `𝓛` over
the graded ring `K[t_0, …, t_r]`. The restriction `L'` of `L` to the punctured affine space `𝔼^{r+1}_K − \{0\}` is the
inverse image of `L` under the canonical projection morphism `q : 𝔼^{r+1}_K − \{0\} → ℙ^r_K`, and is therefore an
invertible module. Let `i : 𝔼^{r+1}_K − \{0\} ↪ 𝔼^{r+1}_K` be the canonical immersion. The affine ring `K[t_0, …, t_r]`
of `𝔼^{r+1}_K` is factorial; *a fortiori* its localization at the origin is factorial, and that ring has dimension
`≥ 2`. It follows that `i_*(L')` is an invertible module, corresponding to an invertible graded module `𝓜` over
`K[t_0, …, t_r]`.[^v-6-3] Moreover `𝓜 = Γ(𝔼^{r+1}_K − \{0\}, q*(𝓛))` is graded in a natural fashion, and the
homomorphism `𝓛 → 𝓜` is an isomorphism at every point of `𝔼^{r+1}_K` distinct from the origin.

Replacing `𝓛` by `𝓜`, we are reduced to the case of an invertible `𝓛`. Since `K[t_0, …, t_r]` is factorial, `𝓛` is then
free of rank one when we ignore its grading. A standard lemma — without doubt available in Bourbaki — implies that it is
also free of rank one as a graded module, which means that the associated `𝒪_P`-module is isomorphic to some `𝒪_P(n)`.
From the editorial point of view, it would be clumsy to begin by considering an `𝓛` of finite type; one should rather
begin by introducing directly `𝓛 = Γ(𝔼^{r+1}_K − \{0\}, q*(L))`, define the module `𝓛 = q_*(𝓛)`, and remark (by Chapter
II) that `𝓛` is a graded module that determines `L`; then one shows that `𝓛` is free of rank `1` as a graded module by
the indicated reasoning.

**(b)** *General case.* This is deduced from case (a) using `(III, 4.6.5)` together with the vanishing relation
`H^1(ℙ^r_K, 𝒪_{ℙ^r_K}) = 0` established in `(III, §2)`. q.e.d.

<!-- original page 4 -->

#### A variant of (1.4).

Let `ℤ(S)` denote the set of locally constant functions `S → ℤ`. We define an evident homomorphism `ℤ(S) → Pic(P)`: an
element `n ∈ ℤ(S)` corresponds to a partition `(S_n)_{n ∈ ℤ}` of `S` into disjoint open subsets (some possibly empty),
and to such a partition we associate the invertible module `𝒪_P(n)` whose restriction to `f⁻¹(S_n)` is `𝒪_P(n)`. We thus
obtain a variant

```text
  (* bis)          Pic(S) × ℤ(S) ⟶ Pic(P),
```

and a statement more general and more satisfactory than (1.4): under the conditions of (1.1), `(* bis)` is a bijection.
(Indeed, when `S ≠ ∅`, the canonical map `ℤ → ℤ(S)` sending `n` to the constant function of value `n` is injective; it
is bijective if and only if `S` is connected. So we recover (1.4) formally, and the statement above is the most general
form.)

We also remark — and this is a remark worth making — that in the language of the Picard scheme (which will be introduced
in [Chapter V.1.1](#)[^v-6-4]), the preceding statement reads simply: *under the conditions of (1.1), the canonical
homomorphism `ℤ_S → Pic_{P/S}` of constant group schemes `ℤ` over `S` into the relative Picard scheme, deduced from the
section of the latter defined by `𝒪_P(1)`, is an isomorphism.*

#### Morphisms between projective fibrations; degree.

Let `P` be a projective fibration over a field `K`. An invertible module `L` over `P` is said to be **of degree `n`** if
`L` is isomorphic to `𝒪_P(n)`; if `dim P ≥ 1`, this determines `n` in terms of `L`, but if `dim P ≤ 0` (`P` empty or
reduced to a point) then `L` is of degree `n` for every `n`. By (1.1) and (1.2), to say that `L` is of degree `n`
amounts to saying that the class of `L` in `Pic(P)` lies in the image of `Pic(S) × \{n\}` under the homomorphism `(*)`,
i.e. that `L` is isomorphic to a module of the form `f*(M)(n)` with `M` invertible over `S`. Moreover, if the fibres of
`P` are non-empty (`E` everywhere of rank `≥ 1`), then `M` is determined up to a unique isomorphism by `L`, again by
(1.1) and (1.2).

> *Grothendieck note.* I notice on this occasion that it would be proper to announce (1.1) without any hypothesis on the
> rank of `E`: every invertible `L` over `P` can be taken in the form indicated in that statement, and if the fibres of
> `P` are non-empty (i.e. the rank of `E` is `≥ 1`), then the partition of `S` is also uniquely determined by the choice
> of `L`. In that case Remark (1.2) is absorbed into the proof and disappears.

Let `P^1 = ℙ(E^1)` be a second projective fibration. The determination of `Pic(P)` allows us in principle to determine
the `S`-morphisms `g : P → P^1`: these are defined by an invertible module `L = g*(𝒪_{P^1}(1))` over `P` together with a
homomorphism `E^1 → f_*(L)` (such that the associated homomorphism `f*(E^1) → L` is surjective), modulo an isomorphism
of `L`. We say that `g : P → P^1` is *of degree `n`* if `L = g*(𝒪_{P^1}(1))` is of degree `n`. It is enough, evidently,
to determine the homomorphisms of degree `n` for each given `n`.

Note that if `g` is of degree `n` and `P` has fibres of dimension `≥ 1`, then necessarily `n ≥ 0` (since over a field
`K` with `dim P ≥ 1`, `𝒪_P(n)` is generated by its sections only when `n ≥ 0`). One could of course restrict to the case
where the fibres of `P` have dimension `≥ 1`, by proceeding as in (1.2). Since

```text
  f_*(f*(M)(n)) = M ⊗ f_*(𝒪_P(n)) = M ⊗ Sym^n(E),
```

the determination of `S`-morphisms `g : P → P^1` reduces to the determination, up to isomorphism, of pairs `(M, u)`,
where `M` is an invertible module over `S` and `u : E^1 → M ⊗ Sym^n(E)` is a homomorphism such that the corresponding
homomorphism `f*(E^1) → f*(M)(n)` is an epimorphism. The morphism `g` then determines a first global invariant over `S`,
namely the class `[M] ∈ Pic(S)`; with `M` fixed, the corresponding `g` correspond to a certain subset of the quotient
set `Hom(E^1, M ⊗ Sym^n(E)) / Γ(S, 𝒪_S)^×`, the passage to the quotient by `Γ(S, 𝒪_S)^×` corresponding to "module
isomorphism" in the description of `g : P → P^1` via invertible modules.

> *Nota bene.* The endomorphisms (resp. automorphisms) of an invertible `L` over a projective fibration `P` correspond
> to sections (resp. invertible sections) of `𝒪_P` over `P`, or — what amounts to the same — to sections (resp.
> invertible sections) of `𝒪_S ⥲ f_*(𝒪_P)` over `S`.

<!-- original page 5 -->

#### Special cases.

**(i) `n = 0`.** We take the homomorphisms `E^1 → M` that are surjective, i.e. everywhere non-zero, modulo isomorphism
of `M`. We find exactly the morphisms `g : P → P^1` of the form induced by a section `h` of `P^1` over `S` (namely those
determined by the invertible quotient `M` of `E^1`). Thus *the `S`-morphisms of degree `0` from `P` into `P^1` are the
constant morphisms relative to `S`.*

> *End of crossed-out portion (per the manuscript marker).*

**(ii) `n = 1`.** We take the homomorphisms `E^1 → E ⊗ M` that are surjective — as one verifies immediately. The
corresponding homomorphism `g : P → P^1` is then the composition

```text
  ℙ(E) ⥲ ℙ(E ⊗ M) ↪ ℙ(E^1),
```

where the first map is the canonical isomorphism described in Chapter II and the second is the canonical closed
immersion deduced from the epimorphism `E^1 → E ⊗ M`. We call the homomorphisms `P → P^1` of this form **linear**; the
morphisms `g : P → P^1` of degree `1` are then exactly the linear ones.

To finish, we determine the isomorphisms of `P` with `P^1`.

**Theorem (1.6).**

<!-- label: V.6.1.6 -->

*Let `S` be a prescheme, and let `P = ℙ(E)`, `P^1 = ℙ(E^1)` be two projective fibrations over `S` defined by `E`, `E^1`
locally free of finite type. Then every `S`-isomorphism `g : P → P^1` is definable as a composition*

```text
  ℙ(E) ⥲ ℙ(E ⊗ M) ⥲ ℙ(E^1),
```

*where `M` is an invertible module over `S`, the first map is the canonical isomorphism of Chapter II, and the second is
the isomorphism deduced from an isomorphism `u : E^1 ⥲ E ⊗ M`. Provided the fibres of `P` are non-empty (resp. of
dimension `≥ 1`), `M` (resp. the pair `(M, u)`) is determined up to a unique isomorphism by `g`.*

By the foregoing considerations we are reduced to showing that `g` is of degree one. This in turn reduces (by passing to
fibres) to the case where `S` is the spectrum of a field and (without loss of generality) `dim P ≥ 1`. But then `𝒪_P(1)`
is intrinsically characterized — independently of the way `P` is realized as a projective fibration — as the ample
generator of `Pic(P)` (between the two generators `𝒪_P(1)` and `𝒪_P(−1)`); consequently, if `g : P → P^1` is an
isomorphism, then `g*(𝒪_{P^1}(1))` is ample and is therefore isomorphic to `𝒪_P(1)`. We are done.

In a less elaborate local form, we may state:

**Corollary (1.7).**

<!-- label: V.6.1.7 -->

*Under the conditions of (1.6), every `S`-isomorphism `g : P → P^1` can be described, in a neighbourhood `U` of each
`s ∈ S`, by an isomorphism `u : E | U ⥲ E^1 | U`, the latter being well defined modulo multiplication by an element of
`Γ(U, 𝒪_U)^×`.*

In particular:

**Corollary (1.8).**

<!-- label: V.6.1.8 -->

*Let `S` be a prescheme, `P = ℙ(E)` a projective fibration over `S` defined by `E` locally free of finite type, and `u`
an automorphism of `P`. Then `u` is determined, in a neighbourhood `U` of every point `s ∈ S`, by an automorphism `ũ` of
`E | U`, the latter being well defined by `u` modulo multiplication by an element of `Γ(U, 𝒪_U)^×`.*

**Remark (1.9).**

<!-- label: V.6.1.9 -->

*From (1.8) one deduces easily that the group functor `Aut_S(P)` over `S` is representable by an affine `S`-prescheme of
finite presentation, which may also be interpreted as the quotient group-scheme of the linear group-scheme `GL(E)` by
its centre `𝔾_m`. This group-prescheme is called the **prescheme of projective groups**, or simply the **projective
group**, defined by `E`, and is denoted `PGL(E)`. If `E` is free, `E ≅ 𝒪_S^{r+1}`, then `PGL(E)` is just the
group-prescheme `PGL(r)_S` deduced by base change `S → Spec(ℤ)` from the analogous group-scheme `PGL(r)` over `Spec(ℤ)`,
called the **absolute projective group**.*

<!-- original page 6 -->

> *Grothendieck note.* End of Appendix 1. A marginal remark next to Remark (1.9) is partly illegible: the legible
> fragment refers to `ℙ(E ⊗ E^∨)` and the "open set defined by the non-vanishing of the determinant", presumably an
> embedded description of `PGL(E)` as the open subscheme of `ℙ(End(E))` cut out by `det ≠ 0`.[^v-6-5]

### V.6.2. Relative divisors and invertible sheaves on projective and multiprojective fibrations

**(2.1).** Let, as in V.6.1, `P = ℙ(E)`, with `E` locally free over `S` of rank `≥ 2` everywhere. We propose to
determine the set `Div^+(P/S)` of positive relative divisors over `P` with respect to `S`. Such a divisor is the same
data as an invertible module `L` over `P` together with a *transversally regular* section `φ` of `L`. By (1.1), ignoring
a possible partition of `S` if `S` is not connected, `L` is isomorphic to `M ⊗ 𝒪_P(n)` for some invertible `M` over `S`,
determined up to a unique isomorphism by `L`. Furthermore, by the canonical isomorphisms

```text
  (*)            f_*(L) ≅ M ⊗ f_*(𝒪_P(n)) ≅ M ⊗ Sym^n(E),
```

to give a section `φ` of `L` amounts to giving a section `ψ` of `M ⊗ Sym^n(E)`. Since the fibres of `P/S` are integral,
`φ` is transversally regular (i.e. regular on each fibre) if and only if `ψ(s) ≠ 0` for every `s ∈ S`; equivalently, the
homomorphism `M^∨ → Sym^n(E)` defined by `ψ` is "universally injective" (i.e. locally an isomorphism onto a direct
factor); equivalently again, its transpose `Sym^n(E)^∨ → M` is surjective.

We say that a relative divisor `D` over `P` is *of degree `n`* if `𝒪_P(D) = L` is of degree `n` in the sense of V.6.1.
Since `D ≥ 0`, this forces `n ≥ 0`: if we had `n < 0`, every section of `L` over fibres would vanish.[^v-6-6] By (1.1),
if `D` is a positive relative divisor over `P`, then there is a unique decomposition of `S` into a sum of disjoint open
subsets `(S_n)_{n ∈ ℕ}` such that for each `n`, `L | P/S_n` is of degree `n`. This reduces the determination of the set
of positive relative divisors to the determination, for given `n`, of those of degree `n`.[^v-6-7]

The foregoing reflections give:

**Proposition (2.2).**

<!-- label: V.6.2.2 -->

*Under the above hypotheses, there is a one-to-one correspondence between the set `Div^n(P/S)` of positive relative
divisors of degree `n` over `P` and the set of invertible quotient modules `M` of `Sym^n(E)^∨` (equivalently, of
invertible submodules of `Sym^n(E)` which are locally direct factors `M^∨`). If `D` and `M` correspond, then `𝒪_P(D)` is
canonically isomorphic to `M ⊗ 𝒪_P(n)`, and the canonical section `s_D` is identified, under this isomorphism, with the
section given by `(*)`.*

Note that this description is compatible with base change in `S`. Taking into account the interpretation of invertible
quotient modules of `Sym^n(E)^∨` as sections over `S` of `ℙ(Sym^n(E))`, we find:

**Corollary (2.3).**

<!-- label: V.6.2.3 -->

*The subfunctor `Div^n_{P/S}` of `Div^+_{P/S}` is canonically representable by `ℙ(Sym^n(E)^∨)`.*

Taking into account the reduction of V.6.2.1, it follows that:

**Corollary (2.4).**

<!-- label: V.6.2.4 -->

*The functor `Div^+_{P/S}` is canonically representable by the sum-prescheme of the `ℙ(Sym^n(E)^∨)` for
`n ∈ ℕ`.*[^v-6-8]

<!-- original page 7 -->

#### The multiprojective case.

**(2.5).** Now suppose we are given a finite family `(E_i)_{i ∈ I}` of locally free modules over `S`, with
`P_i = ℙ(E_i)` and `P = ∏_{i ∈ I, S} P_i` the *multiprojective fibration* over `S` defined by the `(E_i)`. For brevity
we write `𝒪_i(n)` for the inverse image to `P` of the invertible module `𝒪_{P_i}(n)` over `P_i`. For every system of
integers `n = (n_i)_{i ∈ I} ∈ ℤ^I`, we set

```text
  𝒪_P(n) = ⨂_{i ∈ I} 𝒪_i(n_i) = ⨂_{i ∈ I, 𝒪_S} 𝒪_{P_i}(n_i).
```

With this notation, (1.1) generalizes as follows:

**Proposition (2.6).**

<!-- label: V.6.2.6 -->

*Suppose that the `E_i` have rank `≥ 2` everywhere. Then for every invertible module `L` over the multiprojective
fibration `P`, there exists a decomposition of `S` into a sum of disjoint open subsets `(S_n)_{n ∈ ℤ^I}` and an
invertible module `M` over `S` such that*

```text
  L | P/S_n ≅ M ⊗ 𝒪_P(n) | P/S_n.
```

*Moreover, the `S_n` are uniquely determined, and `M` is determined up to a unique isomorphism.*

The proof consists of an immediate reduction to (1.1). Under the conditions of (2.6), we may therefore associate to
every invertible `L` over `P` a *multidegree* `n = (n_i)_{i ∈ I} ∈ ℤ(S)^I`, which characterizes `L` up to a unique
isomorphism provided `Pic(S) = 0`. The `n_i` (called the **partial degree of `L` with respect to the factor `P_i` of
index `i`**) admit the following interpretation: if for each `i` we choose a section `g_i` of `P_i` over `S` (such
sections exist locally over `S` in any case), the system defines, for each `i`, an `S`-morphism `g_i : P_i → P`; we then
have

```text
  n_i = deg g_i^*(L),
```

it being understood that in general `n_i` is not an integer but a locally constant function `S → ℤ`.

Proceeding as in V.6.1, we may deduce from (2.6) the determination of morphisms of one multiprojective fibration into
another, and in particular the determination of automorphisms of multiprojective fibrations. More interesting for us, in
view of (V, 5) on the resultant and discriminant of forms, will be the determination of positive relative divisors on a
multiprojective fibration.

**(2.7).** If `D` is a relative divisor over `P`, we define its *multidegree* as that of `𝒪_P(D)`. As above, the
determination of `Div^+(P/S)` reduces to that of `Div^n(P/S)` for given multidegree `n ∈ ℤ^I`. This gives an isomorphism
`L = 𝒪_P(D) ≅ M ⊗_{𝒪_S} 𝒪_P(n)`, and by (II, §2)

```text
  (**)           f_*(L) = M ⊗ f_*(𝒪_P(n)) = M ⊗ ⨂_i Sym^{n_i}(E_i).
```

Proceeding now as in (2.2), we find:

**Proposition (2.8).**

<!-- label: V.6.2.8 -->

*With the preceding notations, there is a one-to-one canonical correspondence between the set `Div^n(P/S)` of positive
relative divisors of multidegree `n` over `P` and the set of invertible quotient modules `M` of `(⨂_i Sym^{n_i}(E_i))^∨`
(equivalently, of invertible submodules locally direct factors `M^∨` of `⨂_i Sym^{n_i}(E_i)`). If `D` and `M`
correspond, then `𝒪_P(D)` is canonically isomorphic to `M ⊗ 𝒪_P(n)`, and `s_D` is identified under this isomorphism with
the section given by `(**)`.*

**Corollary (2.9).**

<!-- label: V.6.2.9 -->

*The subfunctor `Div^n_{P/S}` of `Div^+_{P/S}` corresponding to positive relative divisors of multidegree `n` is
canonically representable by the projective fibration `ℙ((⨂_i Sym^{n_i}(E_i))^∨)`. Consequently `Div^+_{P/S}` is
canonically representable by the sum-prescheme of the `ℙ((⨂_i Sym^{n_i}(E_i))^∨)` for `n ∈ ℕ^I`.*

<!-- original page 8 -->

#### Representability via a sheaf `Q` on the base.

**Remark (2.10).**

<!-- label: V.6.2.10 -->

*The simplicity of the determination of `Div^+_{P/S}` above stems from the simplicity of the structure of `Pic(P/S)` —
indeed from the "discrete" character of the Picard prescheme `Pic_{P/S}`. We can abstract from the foregoing reasoning
to a relative representability statement (relative to `Pic`).*

To make this precise, take a proper flat morphism `f : X → S` of finite presentation and an invertible module `L` over
`X`. We propose to determine the subset `Div^L(X/S)` of `Div^+(X/S)` formed by those positive relative divisors `D` such
that `𝒪_X(D)` is isomorphic to a module of the form `L ⊗_{𝒪_X} f*(M)` for some invertible module `M` over `S` (depending
on `D`). We assume that

```text
  (***)          𝒪_S ⥲ f_*(𝒪_X),
```

which implies that the above `M` is determined up to a unique isomorphism by `D`, namely

```text
  M = f_*(L^{−1} ⊗ 𝒪_X(D)).
```

To give `D` corresponding to a given `L` is then the same as to give a transversally regular section `φ` of `L ⊗ f*(M)`.
By `(III, §7)`, there exists a finitely presented module `Q` over `S` whose formation commutes with every base change,
together with an isomorphism of functors in the quasi-coherent module `G` over `S`,

```text
  f_*(L ⊗ G) ≅ Hom(Q, G).
```

(In `(III, §7)` one supposes `S` locally noetherian; this hypothesis is removed by the standard brief procedure, taking
into account the base-change commutation of `Q`.) In particular, to give `φ` is equivalent to giving a homomorphism
`Ψ : Q → M`. A necessary condition for `φ` to be transversally regular — sufficient if the fibres of `X` are integral —
is that `φ` should be `≠ 0` fibre by fibre. In terms of `Ψ`, this means that `Ψ` is surjective fibre by fibre, hence
that `Ψ` corresponds to a section of the projective fibration `ℙ(Q)` over `S`.

We obtain:

**Proposition (2.11).**

<!-- label: V.6.2.11 -->

*In the above notations, `Div^L(X/S)` is in canonical bijection with the set of sections of `ℙ(Q)` over `S` — given by
the quotient module `M` of `Q` — such that the section `φ` of `L ⊗ f*(M)` defined by `Ψ : Q → M` is transversally
regular.*

Suppose now that the hypothesis `(***)` continues to hold after every base change; equivalently, by `(III, §7)`, that

```text
  k(s) ⥲ H^0(X_s, 𝒪_{X_s})  for every s ∈ S.
```

Then (2.11) applies equally well to every `X_{S^1}/S^1` after an arbitrary base change `S^1 → S`. We obtain:

**Theorem (2.12).**

<!-- label: V.6.2.12 -->

*Let `f : X → S` be a proper morphism of finite presentation satisfying the above condition `(***)` universally, and let
`L` be an invertible module over `X`. Consider the subfunctor `Div^L_{X/S}` of `Div^+_{X/S}` defined above in terms of
`L`. There exists a finitely presented module `Q` over `S` such that this subfunctor is representable by a retrocompact
open sub-prescheme of the projective fibration `ℙ(Q)`. If, in addition, the fibres of `X/S` are geometrically integral,
then `Div^L_{X/S}` is representable by `ℙ(Q)` itself.*

The last assertion follows immediately from the construction above. For the general case we have already observed that
there is a monomorphism `Div^L_{X/S} → ℙ(Q)`, and we are reduced to showing that this is a retrocompact open immersion.
So we take a section of `ℙ(Q)` over `S` — i.e. an invertible quotient module `M` of `Q`, giving a section `φ` of
`L ⊗ f*(M)` non-vanishing on every fibre — and we must show that the subfunctor of the final functor `S' ↦ Sch_{/S}`
consisting of those `S' → S` for which `φ_{S'}` is transversally regular is representable by a retrocompact open subset
of `S`.

<!-- original page 9 -->

But this is now standard: representability by an open subset follows from the fact that `f` is proper and that
transverse regularity is an open condition (see `(IV, §11)`[^v-6-9]); retrocompactness follows immediately by reduction
to the noetherian case.

### V.6.3. Linear systems of divisors and morphisms into projective fibrations

#### Fixed points of a family of divisors.

**(3.1).** Let `D` be a family of positive divisors over `X/S` parametrized by `T`. A point `x ∈ X` is called a **fixed
point** of this family if `pr_1^{−1}(x) ⊂ D` set-theoretically, so that the set of non-fixed points is the complement of
`pr_1(X ×_S T − D)`. Consequently, if `T → S` is universally open (e.g. flat locally of finite presentation), the set of
fixed points is closed. We say that the family of divisors is **without fixed points** if the set `Z` of fixed points is
empty.

If `Z` is closed, then `X − Z` is the largest open subset of `X` such that the induced family of divisors of `(X − Z)/S`
parametrized by `T` is without fixed points. If the family `D` is without fixed points and `T` is flat and locally of
finite presentation over `S` with geometrically irreducible fibres satisfying `(S_1)`, then `D` is also a relative
divisor with respect to `X` (for `pr_1 : X ×_S T → X`). Indeed, `D` is defined locally at a point `z ∈ supp D` by one
equation `φ = 0`, and the equation `φ_x` induced on the fibre `T ⊗ k(x)` is non-nilpotent at `z` (otherwise,
`pr_1^{−1}(x) ∩ D = V(φ_x)` would contain a neighbourhood of `z` in `T ⊗ k(x)`, hence the whole of `T ⊗ k(x)` since this
fibre is irreducible — meaning `x` would be a fixed point, which it is not). Since `T ⊗ k(x)` is irreducible and
satisfies `(S_1)`, it follows that `φ_x` is `𝒪_{T ⊗ k(x)}`-regular at `z`. We obtain therefore a family of divisors of
`T/S` parametrized by `X`, i.e. a morphism

```text
  X ⟶ Div_{T/S}.
```

In the general case where the family of divisors of `X/S` may have fixed points, we obtain a family of divisors of `T/S`
parametrized by `X − Z`,[^v-6-10] i.e. a morphism `X − Z → Div_{T/S}`, by replacing `X` by `X − Z` in the preceding
construction. The argument shows in fact that `X − Z` is exactly the greatest open subset `U` of `X` such that
`D | U ×_S T` is a relative divisor of `U ×_S T` with respect to `U` — equivalently, such that its "symmetric image"
`ᵗD` is a family of divisors of `T/S` parametrized by `U/S`.

We remark that if `X` and `T` are both flat locally of finite presentation over `S`, with geometrically irreducible
fibres satisfying `(S_1)`, then the symmetry `D ↦ ᵗD` gives a one-to-one correspondence between families of divisors of
`X/S` parametrized by `T` without fixed points and families of divisors of `T/S` parametrized by `X` without fixed
points.

To remove the hypothesis on the fibres of `X/S` and `T/S`, it is convenient to replace "fixed points" by **fixed points
in the extended sense**: by such a fixed point of `D` we mean an `x ∈ X` such that `D` is not a relative divisor with
respect to `X` at all the points of `pr_1^{−1}(x)`. If `W` is the open subset of `X ×_S T` where `D` is a relative
divisor with respect to `X`, then the set of fixed points in the extended sense of `D` equals `pr_1(X ×_S T − W)`; since
`T → S` is proper, this is a closed subset `Z'` of `X`. In every case we obtain a family of divisors of `T/S`
parametrized by `X − Z'`. The assumption that the fibres of `T/S` are `(S_1)` and geometrically irreducible precisely
ensures that `Z = Z'` (fixed points in the strict sense coincide with fixed points in the extended sense).

<!-- original page 10 -->

*Geometric interpretation.* Suppose for simplicity that `S = Spec(k)`, with `k` algebraically closed (which is
permissible, after a base change, when `T/S` is flat and of finite presentation). To say that `x ∈ X(k)` is a fixed
point (resp. fixed point in the extended sense) means that `x ∈ supp D_t` for every `t ∈ T(k)` (resp. that there exists
a prime cycle `T'` associated to `T` such that `x ∈ supp D_t` for every `t ∈ T'(k)`).

*An omission.* The formation of the set `Z` of fixed points is compatible with base change in `S`; on the other hand,
`X − Z` (when open, e.g. for `T/S` flat locally of finite presentation) is universally schematically dense in `X`
relative to `S`. This last fact follows from `(IV, §11)`[^v-6-11] and from the fact that, for every `s ∈ S`, `Z_s`
contains no point of `X_s` associated to `𝒪_{X_s}` (the support of a divisor on `X_s` contains no such point).

#### Linear systems and morphisms into projective fibrations.

When `T` is a projective fibration `Q = ℙ(F)`, the functor `Div^+_{Q/S}` is representable by the sum-prescheme of the
`ℙ(Sym^n(F^∨))` (which we denote `ℙ(n)`); we find then a morphism

```text
  X − Z ⟶ ⨆_n ℙ(n).
```

We say that the family of divisors `D` is **of degree `n`** if the preceding morphism factors through `ℙ(n)`. If `X ≠ ∅`
(so `X − Z ≠ ∅`), the integer `n` is well defined by `D`. To define this notion of degree, we strictly need only the
canonical monomorphisms

```text
  ℙ(n) ⟶ Div_{P^∨/S}.
```

(Note. We set `P = ℙ(F^∨)`, so `Q = ℙ(F) = P^∨` with the notations of V.6.2.)

A **linear system of divisors over `X/S` parametrized by the projective fibration `Q = P^∨`** is a family of divisors
over `X/S` parametrized by `Q` which is of degree one, i.e. defining `f : X − Z → P`. To such a linear system, when the
fibres of `P^∨` are non-empty,[^v-6-12] is associated a *rational map* (better: a "pseudo-morphism relative to `S`")
`X ⤏ P`.

By the very construction, `D | (X − Z) ×_S P^∨` is the inverse image, under `f × id_{P^∨}`, of the canonical *incidence
divisor* `H` over `P ×_S P^∨`. Hence the knowledge of `f : X − Z → P` allows us to reconstruct, at least, the family of
divisors of `(X − Z)/S` induced by `D`. So if the family is without fixed points it is determined by the associated
morphism `f : X → P`. We obtain a one-to-one correspondence between linear systems without fixed points over `X/S`
parametrized by `P^∨` and morphisms `f : X → P` such that `(f × id)^{−1}(H)` is a relative divisor of `X ×_S P^∨` with
respect to `P^∨`. This condition can be checked fibre by fibre:

**Proposition (3.1).**

<!-- label: V.6.3.1 -->

*We have a one-to-one correspondence between linear systems without fixed points of divisors over `X/S` parametrized by
`P^∨` and morphisms `f : X → P` having the following property: for every `s ∈ S`, denoting by `\overline{k(s)}` an
algebraic closure of `k(s)`, and for every prime cycle `X'` associated to `X_{\overline{k(s)}}`, `f(X')` is not
contained in any hyperplane of `P_{\overline{k(s)}}`. (If `X` has geometrically integral fibres, this can be stated
simply by saying that `f(X_{\overline{k(s)}})` is not contained in any hyperplane of `P_{\overline{k(s)}}`.)*

In general (`Z ≠ ∅`) we can no longer assert that the knowledge of `f` determines the family of divisors. The most
trivial case is `P^∨ = S` of relative dimension zero: a linear system of divisors of `X/S` parametrized by `S` is just a
relative Cartier divisor `D` over `X` relative to `S`, the associated morphism is the projection `X − D → S`, and the
knowledge of this morphism (including its domain of definition) does not determine `D`.

To eliminate such unpleasant phenomena, we limit ourselves to linear systems **without fixed components**.

<!-- original page 11 -->

If `S = Spec(k)`, then given a family (not necessarily linear) of divisors of `X/S` parametrized by `T`, a **fixed
component** of the family is any irreducible component of codimension one of the set `Z` of fixed points; the family is
**without fixed components** if it has no fixed component, i.e. `codim(Z, X) ≥ 2`. This terminology extends immediately
to arbitrary `S` by considering fibres. The property of having no fixed component is stable under base change.

**Proposition (3.2).**

<!-- label: V.6.3.2 -->

*Suppose `X → S` is flat and locally of finite presentation, with fibres satisfying `(S_2)`. Let `D` be a linear system
of divisors without fixed components over `X/S` parametrized by `P^∨`. Then `D` is uniquely determined by the
corresponding morphism `f : X − Z → P` (`Z` = set of fixed points), and even by the equivalence class of `f` as a
pseudo-morphism relative to `S`; the set `X − Z` is the domain of definition of that class.*[^v-6-13]

We must prove that if `D'` is another linear system of divisors without fixed components parametrized by `P^∨`, defining
`f' : X − Z' → P`, and if `f` and `f'` agree on an open subset `U ⊂ (X − Z) ∩ (X − Z')` schematically dense relative to
`S`, then `D = D'`. Since `P` is separated over `S`, we may take `U = (X − Z) ∩ (X − Z') = X − Z''`, where
`Z'' = Z ∪ Z'`. Since `Z''` is of codimension `≥ 2` on each fibre and `X` has `(S_2)` fibres, for every `x ∈ Z''` the
fibre `X_s` has depth `≥ 2` at `x`. We may conclude (using flatness of `X` over `S`) that every divisor over `X` (not
necessarily transversal to the fibres) is determined by its restriction to `X − Z''`.

Let `𝒥` be the ideal sheaf defining `D`; it suffices to show that `𝒥 → i_*(𝒥 | X − Z'')` is an isomorphism (where
`i : X − Z'' ↪ X` is the canonical immersion), for then the homomorphism `𝒥 → 𝒪_X` is recovered by applying `i_*` to
`𝒥 | X − Z'' → 𝒪_X | X − Z''`. Since `𝒥` is invertible it is flat over `S`, and for `x ∈ Z''`, `prof_x 𝒥_{(s)} ≥ 2`. It
is therefore enough to prove:

**Lemma (3.3).**

<!-- label: V.6.3.3 -->

*Let `X → S` be of finite presentation, `𝓕` a module of finite presentation over `X`, flat relative to `S`, and `T` a
closed subset of `X`. Assume that for every `x ∈ X` over `s ∈ S` we have `prof_x 𝓕_s ≥ 1` (resp. `≥ 2`). Then the
canonical homomorphism `𝓕 → i_*(𝓕 | X − T)` is injective (resp. bijective), where `i : X − T ↪ X` is the canonical
immersion.*

Indeed, we may suppose `S` and `X` affine, and by the brief procedure reduce to `S` noetherian. Then the hypothesis
implies, by `(IV, §6)`, that `prof_x 𝓕 ≥ prof_x 𝓕_s` for every `x ∈ X` over `s ∈ S`, so `prof_x 𝓕 ≥ 1` (resp. `≥ 2`) for
`x ∈ T`. We conclude by `(IV, §5)`.[^v-6-14]

> *Grothendieck note.* For best results, this lemma ought to appear in `(IV, §11)` ("elimination of the noetherian
> hypothesis…"); compare `(IV, 11.3)`.[^v-6-15]

It finally remains to verify the last assertion of Proposition (3.2): that `X − Z` is exactly the domain of definition
of the rational map relative to `S` defined by `f`. Let `U ⊃ X − Z` be its domain of definition. By Proposition (3.1),
`U → P` is associated to a linear system of divisors `D''` over `U/S` parametrized by `P^∨`, and
`D'' | (X − Z) ×_S P^∨ = D | (X − Z) ×_S P^∨`. Applying the uniqueness result to `D''` and `D | U ×_S P^∨`, the two are
equal, so `D | U ×_S P^∨` has no fixed points: `Z ∩ U = ∅`, hence `U = X − Z`. q.e.d.

<!-- original page 12 -->

> *Grothendieck note.* I repent of having stated the proposition in a muddled form, half-way between the classical
> hypotheses and the natural ones, and without giving the converse.[^v-6-16] So I propose to announce instead:

**Proposition (3.4).**

<!-- label: V.6.3.4 -->

*Let `X → S` be flat locally of finite presentation, `Q = P^∨ = ℙ(E^∨)` a projective fibration over `S` defined by a
locally free module of finite type `F = E^∨`. Consider the set `Φ` of linear systems `D` of divisors over `X`
parametrized by `Q` such that the set `Z` of fixed points satisfies: `z ∈ Z ⟹ prof_z 𝒪_{X_s} ≥ 2` (where `s` is the
image of `z` in `S`). Consider also the set `𝔘` of pseudo-morphisms `f` relative to `S` of `X` into `P` such that the
domain of definition `U = U(f)` satisfies `z ∈ X − U ⟹ prof_z 𝒪_{X_s} ≥ 2`, and such that `f_U = f | U : U → P`
satisfies the non-degeneracy of (3.1). Consider the natural map `D ↦ f_D` of `Φ` into `𝔘`. Then:*

*(a) This map is injective, and for `D ∈ Φ` the set of fixed points `Z` is just the complement `X − U` of the domain of
definition of `f_D`.*

*(b) Let `f ∈ 𝔘`, and let `U` be an open subset over which `f` is defined and such that
`z ∈ X − U ⟹ prof_z 𝒪_{X_s, z} ≥ 2` (for instance `U = U(f)`). In order that `f` give rise to some `D ∈ Φ`, it is
necessary and sufficient that, setting `L_U = f_U^*(𝒪_P(1))` (with `f_U : U → P` the morphism induced by `f`), the
module `i_*(L_U)` over `X` is invertible (where `i : U ↪ X` is the canonical immersion).*

*If the fibres of `X` over `S` satisfy `(S_2)` — for instance if they are normal, or even just geometrically normal —
then the depth condition on a closed subset `Z` of `X` in the proposition means simply that for every `s ∈ S`, `Z_s` is
of codimension `≥ 2` in `X_s`; `Φ` is therefore exactly the set of linear systems without fixed components. Moreover, if
`S = Spec(k)` and `X` is normal, then for every rational map `f : X ⤏ P` the domain of definition `U(f)` satisfies
`codim(X − U(f), X) ≥ 2` (II.7), so `𝔘` is the set of all rational maps `X ⤏ P`.*

The proof of (a) has already been given. For (b), we note that the formation of `i_*(L_U)` commutes with every flat
extension `S' → S` (at least if `U → X` is quasi-compact, the case to which we reduce without difficulty), so the
condition in question is invariant under faithfully flat quasi-compact base change. Taking `S' = P^∨` and noting that
the hypothesis that `i'_*(L'_U)` is invertible does not change if we replace `L'_U` by `L'_U ⊗_{S'} M'` for any
invertible `M'` over `S'`, we have

```text
  i'_*(L'_U ⊗_{S'} M') ≅ i'_*(L'_U) ⊗_{S'} M'.
```

<!-- original page 13 -->

Taking `M' = 𝒪_{P^∨}(1)`, the condition becomes that `i'_*(N')` is invertible, where

```text
  N' = (f_U × id_{P^∨})^*(𝒪_{P ×_S P^∨}(1, 1)).
```

But `𝒪(1, 1)` is precisely the invertible module defined by the canonical (incidence) divisor `H` of `P ×_S P^∨`, so
that `N'` is the invertible module defined by `D' = (f_U × id_{P^∨})^{−1}(H)`. If `f` gives rise to a `D ∈ Φ`, then
`D' = D | U ×_S P^∨` and `N' = N | U ×_S P^∨`, where `N` is the invertible module over `X ×_S P^∨` defined by `D`. It
follows from Lemma (3.3), applied to `P ×_S P^∨ → P`, that `i_*(N') ≅ N`; hence `i'_*(N')` is invertible.

Conversely, if this condition is satisfied, we show that `f` gives rise to a `D ∈ Φ`, which evidently amounts to saying
that `D'` extends to a relative divisor of `X ×_S P^∨` with respect to `P^∨`. It suffices to show that it extends to a
divisor `D` over `X ×_S P^∨` (it will then automatically be a relative divisor with base `P^∨`, since `U` contains
elements associated to `𝒪_{X_s}` for every `s ∈ S`, and that property is stable under base change — in particular under
`S' = P^∨ → S`). But by Lemma (3.3) again, `D'` extends to a divisor `D` if and only if `D'` extends to an invertible
module, i.e. iff `i'_*(N')` is invertible. We have therefore the necessary and sufficient condition.

> *Grothendieck note.* The end of the proof should be edited to express the necessary and sufficient condition once only
> (rather than twice as I did), and to begin by isolating the following corollary of Lemma (3.3).

**Corollary (3.5).**

<!-- label: V.6.3.5 -->

*Suppose `g : X → S` is flat and locally of finite presentation. Let `T` be a closed subset of `X` such that
`x ∈ T ⟹ prof_x 𝒪_{X_s} ≥ 2` (where `s = g(x)`), and set `U = X − T`, `i : U ↪ X`. For every locally free module `L` of
finite type over `X`, let `L' = L | U`. Then:*

*(a) The functor `L ↦ L'` is fully faithful, and for every `L` the canonical homomorphism `L → i_*(L')` is an
isomorphism. For `L` to be of rank `n`, it is necessary and sufficient that `L'` should be.*

*(b) A locally free module `L'` over `U` is isomorphic to the restriction of a locally free module `L` over `X` if and
only if `i_*(L')` is locally free.*

*(c) Suppose `L'` is an invertible module associated to a divisor `D'` over `U`. Then the condition of (b) is also
necessary and sufficient in order that `D'` should be the restriction of a divisor `D` over `X` (which is then unique,
and equals the scheme-theoretic closure of `D'` in `X`). For `D` to be a relative divisor with respect to `S`, it is
necessary and sufficient that `D'` should be.*

We simply use the fact that every such `L` satisfies the hypothesis on `𝓕` in Lemma (3.3).

**Corollary (3.6).**

<!-- label: V.6.3.6 -->

*Suppose the local rings of `X` are factorial (for example, `X` regular). Then the map `Φ → 𝔘` of (3.4) is bijective. In
particular, if `X` is a regular prescheme locally of finite type over a field `k`, and `P` is a projective fibration
over `k`, then there is a one-to-one correspondence between the set `Φ` of linear systems of divisors without fixed
components over `X` parametrized by `P^∨`, and the set `𝔘` of rational maps `X ⤏ P` whose image (over `\overline{k}`)
does not factor through any hyperplane of `P_{\overline{k}}`.*

Indeed, since the local rings of `X` are factorial, every invertible module over `U` extends to an invertible module
over `X`, so the condition of (3.4)(b) is automatically satisfied. (By Auslander-Buchsbaum, a regular local ring is
factorial.)

<!-- original page 14 -->

### V.6.4. Linear systems of divisors and invertible modules

Using the results of V.6.1, we shall give a complete description of linear systems over `X` in terms of invertible
sheaves over `X`.

We may suppose that `P^∨ → S` is surjective; then so is `X ×_S P^∨ → P^∨`. According to the generalities of (V, 6.2)
above, to give a divisor `D` over `X ×_S P^∨` is to give an invertible module `N` over `X ×_S P^∨` together with a
regular section `φ` of `N`.[^v-6-17] The assumption that `D` is a linear system of divisors over `X` parametrized by
`P^∨` can be expressed by the two conditions

1. *(regularity fibre by fibre)* the sections `φ_t` (`t ∈ P^∨`) induced by `φ` on the fibres of `X ×_S P^∨` over `P^∨`
    are regular (which entails that `φ` is regular); and
1. *(degree 1)* the modules `N_x` (`x ∈ X`) induced by `N` on the fibres of `X ×_S P^∨` over `X` are of degree one.

By V.6.1, to give an `N` invertible over the projective fibration `X ×_S P^∨` over `X` satisfying condition 2 is
equivalent to giving an invertible module `L` over `X`; `N` is then determined as a function of `L` by

```text
  N = L ⊗_{𝒪_S} 𝒪_{P^∨}(1),
```

and `L` is determined in terms of `N` by

```text
  L ≅ pr_{1, *}(N(−1))
```

(where `(−1)` denotes tensoring with `𝒪_{P^∨}(−1)` over `𝒪_S`). To give `φ` is then to give a section of `L ⊗ 𝒪_P(1)`,
i.e. a section of

```text
  pr_{1, *}(L ⊗_{𝒪_X} 𝒪_{X ×_S P^∨}(1)) = L ⊗_{𝒪_S} pr_{1, *}(𝒪_{X ×_S P^∨}(1)).
```

By `(III, §2)`, `pr_{1, *}(𝒪_{X ×_S P^∨}(1)) = E^∨_X`, so that to give `φ` is equivalent to giving a morphism
`g*(E) → L` or, what is the same, a morphism `u : E → g_*(L)`, where `g : X → S` is the canonical projection.

It remains to express condition 1 in terms of `u`. Since the construction commutes with base change, it suffices to
express this condition fibre by fibre, taking into account that the points of `P` with values in an extension `k` of
`k(s)` correspond exactly to lines in `E(s) ⊗_{k(s)} k`. This condition is: *for every `t ∈ E(s)`, the corresponding
section `u(s)(t)` of `L_s` over `X_s` is regular*, and the analogous condition holds after every extension of the base
field. As usual, it suffices to test this over an algebraic closure of `k(s)`.

To summarize:

**Proposition (4.1).**

<!-- label: V.6.4.1 -->

*Let `g : X → S` be a flat morphism locally of finite presentation, `P = ℙ(E)` a projective fibration over `S` defined
by `E` locally free of finite type, everywhere `≠ 0` (so that `P` has non-empty fibres), and `P^∨ = ℙ(E^∨)`. Then there
is a bijection between the set of linear systems of divisors over `X/S` parametrized by `P^∨` and the set of pairs
`(L, u)` (up to isomorphism), where `L` is an invertible module over `X` and `u : E → g_*(L)` is a homomorphism such
that for every `s ∈ S` and every point `t` of `E(s) ⊗_{k(s)} \overline{k(s)}` (`\overline{k(s)}` an algebraic closure of
`k(s)`), the corresponding section `u(t)` of `L_s ⊗ \overline{k(s)}` over `X_s ⊗ \overline{k(s)}` is regular.*

<!-- original page 15 -->

If the fibres of `X` are geometrically integral, the condition on `u` simplifies: for every `s ∈ S`,
`u(s) : E(s) → H^0(X_s, L_s)` is injective. For convenience of reference, we recall the construction of the divisor `D`
in terms of `(L, u)`: it is the divisor of the evident section `φ` of `L ⊗_{𝒪_S} 𝒪_{P^∨}(1)` defined by `u`.

**Corollary (4.2).**

<!-- label: V.6.4.2 -->

*Assume `g : X → S` is proper, flat, and of finite presentation with geometrically integral fibres. Let `L` be an
invertible module over `X` and `P = ℙ(E)` a projective fibration over `S` as in (4.1). There exists a finitely presented
module `Q` over `S` and an isomorphism of functors of the quasi-coherent `𝒪_S`-module `F`:*

```text
  Hom(Q, F) ⥲ g_*(L ⊗_{𝒪_S} F).
```

*With this in hand, the linear systems of divisors on `X` parametrized by `P^∨` and associated to `L` in the sense of
(4.1) correspond bijectively to the surjective homomorphisms `Q → E^∨` modulo multiplication by a section of `𝒪_S^×`.*

The existence of `Q` reduces by the brief procedure to the case `S` noetherian, where it is `(III, 7.7.6)` (the
hypothesis on the fibres of `X` being unnecessary). Since `E` is locally free of finite type, to give a homomorphism
`E → g_*(L)` is the same as to give a section of `g_*(L) ⊗ E^∨`, i.e. a homomorphism `Q → E^∨`. It remains to express
the condition of (4.1) in this form. By hypothesis on the fibres of `X/S`, this reduces to fibre-by-fibre injectivity of

```text
  E(s) ⟶ H^0(X_s, L_s) ≅ Hom_{k(s)}(Q(s), k(s)),
```

i.e. surjectivity of `Q(s) → E^∨(s)`, which by Nakayama means surjectivity of `Q → E^∨`. The "modulo sections of
`𝒪_S^×`" becomes "modulo isomorphisms" in (4.1).

We may interpret (4.2) in another way using the fact that `ℙ(Q)` represents the subfunctor of `Div_{X/S}` defined by
`L`, by virtue of V.6.2. Consequently, a linear system parametrized by `P^∨` and associated to `L` is interpreted as a
morphism `P^∨ = ℙ(E) → ℙ(Q)`. The "linear" character of the family of divisors so defined is captured by saying that
this morphism is *linear*, i.e. is defined by a surjective morphism `Q → E^∨`. In this case `P^∨ → Div_{X/S}` is also a
monomorphism (since `P^∨ → ℙ(Q) → Div_{X/S}` is such); this is a more general fact, cf. the corollary below.

We agree that two linear families of divisors of `X/S` parametrized by projective fibrations `P^∨`, `(P^∨)'` are
**isomorphic** if they are transformed into each other by an `S`-isomorphism `P^∨ ⥲ (P^∨)'` (which is unique, by the
monomorphism property). We may then express (4.2) by saying that the set of classes (up to isomorphism) of linear
systems of divisors over `X` associated to `L` is in canonical bijection with the set `Grass(Q)(S)`, and this
correspondence is compatible with base change. The functor

```text
  S' ⟼ \{classes (mod isomorphism) of linear systems of divisors of X_{S'}/S' associated to L_{S'}\}
```

is therefore representable by the `S`-prescheme `Grass(Q)`.

> *Grothendieck note.* (Marginal remarks here are hard to read.)[^v-6-18]

We should also make explicit in (4.1) that `L | X − Z` is canonically isomorphic to `f*(𝒪_P(1))` (with the notations of
V.6.3). So for a `D ∈ Φ` in the sense of (3.4), `L | X − Z` is exactly the canonical and unique extension of
`f*(𝒪_P(1))` to an invertible sheaf over `X`.

<!-- original page 16 -->

#### Monomorphism into `Div_{X/S}`.

**Proposition (4.3).**

<!-- label: V.6.4.3 -->

*Let `D` be a linear system of divisors over `X/S` parametrized by `P^∨`, with `g : X → S` flat of finite presentation.*

*(a) Suppose `g` is of finite presentation, and that for every `s ∈ S`, denoting by `\overline{k(s)}` an algebraic
closure of `k(s)`, there exists a prime cycle `T` associated to `X_{\overline{k(s)}}` such that
`\overline{k(s)} ⥲ H^0(T, 𝒪_T)` (a condition automatically satisfied if `g` is proper and surjective). Then the morphism
`D : P^∨ → Div_{X/S}` is a monomorphism.*

*(b) Consider the map `u ↦ D ∘ u` from `Aut_S(P^∨)` into the set of families of divisors over `X/S` parametrized by
`P^∨`. If `g` is surjective, this map is injective; in particular, `D = D ∘ u` implies `u = id_{P^∨}`. More generally,
the morphism of functors `Aut_S(P^∨) → \{linear systems of divisors of X/S parametrized by P^∨\}` is a monomorphism.*

We note that under the hypotheses of (a), (b) is a trivial consequence of (a); on the other hand, (b) holds under less
restrictive assumptions than (a). The hypothesis in (a) is genuinely needed: for example, take `S = Spec(k)` and `X` an
open subset of `ℙ^1_k` not containing two distinct points `a, b ∈ ℙ^1_k(k)`; then `a` and `b` define the same divisor of
`X` (the zero divisor!) without being identical.

Suppose first that `S = Spec(k)` with `k` algebraically closed (a reduction we may make by descent). Let `T` be as in
(a), equipped with the induced reduced structure; we have a morphism

```text
  Div_{X/k} ⟶ Div_{T/k}
```

("induced divisor"), and it suffices to show that the composition `P^∨ → Div_{T/k}` is a monomorphism. The latter is
again a linear system of divisors, so we are reduced to the case `X = T`, hence to the case where `H^0(X, 𝒪_X) ⥲ 𝒪_S`.
Then for every `S'` over `k`,

```text
  g_{S', *}(𝒪_{X_{S'}}) ⥲ 𝒪_{S'}.
```

Now if `L` over `X` and `u : E → g_*(L)` are as in (4.1), and if two sections `φ`, `ψ` of `E_{S'}` everywhere non-zero
are such that `u(φ)` and `u(ψ)` have the same divisor as sections of `L_{S'}` over `X_{S'}`, then `u(ψ)` is deduced from
`u(φ)` by multiplication by an invertible section of `𝒪_{X_{S'}}`; from `(g_{S'})_*(𝒪_{X_{S'}}) ⥲ 𝒪_{S'}`, this
multiplier is an invertible section of `𝒪_{S'}`. So `ψ = c · φ` for `c ∈ 𝒪_{S'}^×`, meaning `φ` and `ψ` define the same
point of `P^∨` with values in `S'`. Since every point of `P^∨` with values in `S'` is defined locally over `S'` by a
section `φ` of `E_{S'}` not vanishing anywhere (cf. Chapter I), (a) follows.

To prove (b) we record:

**Lemma (4.4).**

<!-- label: V.6.4.4 -->

*Let `D` be a non-empty linear system of divisors over `X` locally of finite type over an algebraically closed field
`k`, parametrized by `P^∨ = ℙ(E)`, and let `f : X − Z → P` be the corresponding morphism (`Z` = base locus, i.e. set of
fixed points). If `r = rank_k E > 0`, there exist `r + 1` points `x_i` (`1 ≤ i ≤ r + 1`) of `X(k) − Z(k)` such that the
`f(x_i)` form a "projective base" of `P`: for every subset `J ⊂ [1, r + 1]` of cardinality `r`, the `f(x_j)` (`j ∈ J`)
are not contained in any hyperplane of `P`.*

We may suppose `Z = ∅`. Since (by (4.1)) `f(X)` is not contained in any hyperplane of `P`, we obtain at once the
existence of `r` points `x_i` (`1 ≤ i ≤ r`) such that the `f(x_i)` are projectively independent in `P`, i.e. defined by
linearly independent forms over `E`. It remains to find `x_{r+1} = x ∈ X(k)` such that `f(x)` lies in none of the `r`
hyperplanes `H_i` defined by the `(r − 1)`-tuples among the `f(x_j)`. Suppose the contrary; then by Jacobson-type
sorites,

```text
  f(X) ⊂ ⋃_i H_i,
```

<!-- original page 17 -->

so for some irreducible component `X_0 ⊂ X`, `f(X_0) ⊂ H_i` for some `i`, contradicting (3.1) (or (4.1)). q.e.d.

To prove (b), we may suppose `Z = ∅`. By (3.1) (or (4.1)), we are reduced to showing that an automorphism `u` of `P^∨`
is determined by the composition of its contragredient `u^∨` (on `P`) with `f : X → P`, and that the analogous statement
holds after every base change `S → Spec(k)` by an automorphism `u` of `P^∨_S`. But this follows immediately from Lemma
(4.4) and from the determination of automorphisms of `ℙ(E^∨) = ℙ(E)^∨` in V.6.1: the effect of an automorphism of a
projective fibration over `S` (relative to a locally free module of finite type) is determined by its effect on a
projective base in each fibre.

#### The general case: `S` arbitrary.

By base change over `S`, we are reduced in (a) to showing that any two sections of `P^∨` over `S` defining the same
divisor of `X` are identical, and in (b) to showing that any two automorphisms of `P^∨` for which `D ∘ u = D ∘ v` are
identical. We may suppose `S` affine; in (b), where we do not expressly suppose `g` of finite presentation but `g`
surjective, we reduce immediately (using that `g` is open) to the case where `X` is also affine, hence of finite
presentation over `S`. By the brief procedure we reduce to `S` noetherian.

For a noetherian base scheme `S` and a morphism of functors `h : F → G` over `S` (with `F`, `G : Sch_{/S} → Set`), there
are general criteria — to be made explicit in Chapter V — guaranteeing that if for every `s ∈ S` the morphism
`F_s → G_s` is a monomorphism, then `F → G` is a monomorphism, under suitable hypotheses on `F` and `G` (e.g. both
representable by preschemes of finite type over `S`; here only `F` is *a priori* representable). We summarize the
argument in the two cases of interest.

We have two sections `u, v` of a prescheme `F` of finite type over `S` (in (a), sections of `P^∨`; in (b), sections of
the projective group `PGL(E^∨)`); we want to show they are equal. It is enough to prove this after the base change

```text
  Spec(𝒪_{S, s} / 𝔪^{n+1}) ⟶ S,
```

which reduces to `S = Spec(A)` artinian local. Induction on the integer `n` such that `𝔪^{n+1} = 0` reduces us to the
case where `u` and `v` agree modulo `𝔪^n`. Then one is obtained from the other by an element `δ` of

```text
  Hom_k(u_0^*(Ω^1_{F_0/k}), V),
```

<!-- original page 18 -->

where `k = A/𝔪` is the residue field, `F_0 = F ⊗_A k` the reduced fibre, and `V = 𝔪^n = 𝔪^n / 𝔪^{n+1}`. It suffices to
show that `δ = 0` using the hypothesis `h(u) = h(v)`.

The general principle is: expressing that `h(u)` and `h(v)` coincide modulo `𝔪^n`, we see that their "difference" can be
written as an element `δ'` of `Hom_k(w_0^*(Ω^1_{G_0/k}), V)` where `w_0 = h_0(u_0) = h_0(v_0)` and `G_0 = G ×_A k`; this
element is exactly the one deduced from `δ` by composition with the natural homomorphism

```text
  h_0^* : w_0^*(Ω^1_{G_0/k}) ⟶ u_0^*(Ω^1_{F_0/k})
```

deduced from `h_0 : F_0 → G_0`. Since `h(u) = h(v)`, we have `δ' = 0`; the composition of `δ` with `h_0^*` is zero, so
if `h_0^*` is surjective, we conclude `δ = 0`. The fact that `h_0 : F_0 → G_0` is a monomorphism (which implies that the
induced map on points with values in the dual numbers over `k` is a monomorphism) gives the surjectivity of `h_0^*` (its
transpose is injective).

This reasoning is valid when `G` is representable, which is not strictly the case here. However, one can define a vector
bundle `𝒢_{w_0}` over `k` playing the role dual to `w_0^*(Ω^1_{G_0/k})`[^v-6-19] — the "tangent to `G_0` at `w_0`" — by
expressing the deviation of two points of `G` coinciding modulo `𝔪^n` as an element of `𝒢_{w_0} ⊗_k V`. This is
essentially straightforward, and is contained in the systematic developments of `(V, §26)`[^v-6-20] ("infinitesimal
extensions"), which we recall here.

- In case (a), `G` is the functor `Div_{X/S}`; `w_0` corresponds to a Cartier divisor `D_0` over `X_0 = X ⊗_A k`, and
    one must take

    ```text
      𝒢_{w_0} = H^0(D_0, 𝒩_{D_0/X_0}),
    ```

    where `𝒩` is the normal sheaf to `D_0` in `X_0`, isomorphic also to the sheaf induced on `D_0` by `𝒪_{X_0}(D_0)`.

- In case (b), we may suppose `D` has no fixed points and interpret the situation via morphisms into `P` (cf. (4.1));
    `G` becomes the functor `Hom_S(X, P)`, and

    ```text
      𝒢_{w_0} = Hom_{𝒪_{X_0}}(f_0^*(Ω^1_{P_0/k}), 𝒪_{P_0}).
    ```

In both cases we have a natural homomorphism

```text
  𝒢_{u_0} ⊗_k V ⟶ 𝒢_{w_0} ⊗_k V
```

(`𝒢_{u_0}` the dual of `u_0^*(Ω^1_{F_0/k})`) expressing the passage from `δ` to `δ'`; the injectivity follows from the
injectivity of `𝒢_{u_0} → 𝒢_{w_0}`, which comes from the fact that `h_0 : F_0 → G_0` is a monomorphism.

<!-- original page 19 -->

> *Grothendieck note.* In practice, writing out the last part of the proof without referring to the small calculations
> of `(V, §25)`[^v-6-21] does not seem possible (it being out of the question to redo them here in a particular case).
> We note that this does not give rise to a vicious circle: §25, and the present calculations, depend only on the
> rewrite of differential calculus from §16; and (4.3) will not be used again in Chapter V except perhaps in the two
> following numbers.[^v-6-22]

The interest of (4.3)(a) is to prove that, under the stated conditions, the parametrizing projective fibration can be
interpreted intrinsically: the notion of a *class of linear system* (up to isomorphism of parametrizing fibration) over
`X/S` becomes that of a subfunctor `P^∨` of `Div_{X/S}` satisfying certain properties — namely, representability by a
projective fibration, and the family of divisors defined by the canonical injection into `Div_{X/S}` being linear in the
sense of V.6.3. This is essentially the classical point of view: a linear system of divisors is a set of divisors
satisfying certain conditions; compare (4.5) below.

On the other hand, (4.3)(b) is equivalent to: *if `g` is surjective, then any isomorphism between two linear systems of
divisors over `X/S` parametrized by projective fibrations `P^∨`, `(P^∨)'` is induced by a unique `S`-isomorphism
`P^∨ ⥲ (P^∨)'` (compatible with `D`, `D'`).* So a class (up to isomorphism) of linear systems over `X/S` determines its
parametrizing projective fibration up to a unique isomorphism. Technically, this result will allow us — once we have the
descent theory of Chapter V (not yet written; the numbering is of only historical interest) — to perform faithfully flat
descent for linear systems of divisors, provided we are willing to allow as parametrizing fibrations the "twisted
projective fibrations" (i.e. the Brauer-Severi schemes), to be treated in a future section.

#### Vulgar description over a field.

Descending again to the earth — even lower — to explain in vulgar terms the notion of a linear system, we place
ourselves for simplicity over a field. (The statement holds essentially as such over an affine base.)

**Proposition (4.5).**

<!-- label: V.6.4.5 -->

*Let `X` be a prescheme of finite type over a field `k` such that*

```text
  k ⥲ H^0(X, 𝒪_X)
```

*is an isomorphism. To every linear system `D` of divisors over `X` parametrized by a projective fibration `P^∨` over
`k`, we associate the set `Ens(D)` of all the divisors of `X` of the form `D(t)`, `t ∈ P^∨(k)`.*

*(a) If `D'` is another linear system of divisors over `X` parametrized by `(P^∨)'`, then `D` and `D'` are isomorphic if
and only if `Ens(D) = Ens(D')`.*

*(b) Suppose `k` is algebraically closed, or `X` is geometrically integral. In order that a set `Δ` of positive Cartier
divisors over `X` should be of the form `Ens(D)`, it is necessary and sufficient that there exist a `k`-subspace `E` of
the vector space of meromorphic functions on `X` such that for every `φ ∈ E − \{0\}`, `φ` is regular (i.e. `div(φ)` is
defined), and `Δ` is the set of `div(φ)` for `φ ∈ E − \{0\}`.*

*(c) Let `E, E'` be two `k`-vector subspaces of the meromorphic functions on `X` satisfying the assumption of (b). Then
the sets of divisors `Δ`, `Δ'` defined by them are equal if and only if there exists a regular pseudo-function `φ` over
`X` such that*

```text
  E' = φ E.
```

*If `E ≠ \{0\}` (i.e. `Δ ≠ ∅`), such a `φ` is determined modulo multiplication by an element of `k^×`.*[^v-6-23]

<!-- original page 20 -->

The proof is an easy exercise using (4.1), and we dispense with writing it down unless protest is registered.

> *Grothendieck note.* It seems to me that (4.5) could profitably come before (4.3), being technically more trivial.
> Note also that if `X` is geometrically integral, the condition on `E` stated in (b) becomes void. The restriction at
> the beginning of (b) is attached to the fact that the condition announced may fail after passing to the algebraic
> closure of `k` (one can give easy examples in every characteristic, even with `k` separably closed in characteristic
> `p > 0`). For good measure one would announce (b) without supplementary conditions on `k` or `X` by announcing the
> condition on `E` and passing to the algebraic closure of `k` (noting that, if `X` is geometrically integral, this
> condition is void).

By abuse of language, a set `Δ` of divisors of the form `Ens(D)` is often called a **linear system of divisors on `X`**.

______________________________________________________________________

[^v-6-1]: Translator's note: Blass renders this as "(`[Tr]` of the original design)". Grothendieck means: the
    descent-theoretic Chapter V of the originally planned EGA, which was never written; today's reader should
    consult `(Bourbaki Sém. 236)`, `(SGA 1)`, and the descent material now scattered through `(SGA 3)` and
    `(SGA 4½)`.

[^v-6-2]: Translator's note: Blass renders this as "`E`, est dela frima `[Fr]`". The French *est de la frime* — slang
    for "is just for show" or "is window dressing" — is Grothendieck's marginal way of saying that the assumption
    of constant rank costs us nothing here, since the question is local. We modernize to "We may suppose…".

[^v-6-3]: Translator's note: Blass has `[illegible letter]` for the symbol naming the graded module produced by
    `i_*(L')`. The PDF shows this is `𝓜` (script M), which Grothendieck reuses on the next line; we write `𝓜`
    throughout.

[^v-6-4]: Translator's note: the reference is to a never-written section of the descent-theoretic Chapter V (originally
    planned); the modern locus is the relative Picard scheme `Pic_{X/S}` as constructed by
    `(Bourbaki Sém. 232/236)` or `(FGA)`. The present text is silent on its existence; we keep Grothendieck's
    forward reference verbatim.

[^v-6-5]: Translator's note: Blass writes "Marginal remark next to Remark 1.9 partly illegible `[illegible]` /
    `ℙ(E ⊗ E)` defined by the non-vanishing of the 'determinant'". The PDF (page 6) shows the marginal note ends
    with `ℙ(E ⊗ E^∨)`, not `ℙ(E ⊗ E)`; the correction is consistent with the modern description of `PGL(E)` as the
    open subscheme of `ℙ(End(E)) = ℙ(E ⊗ E^∨)` complementary to the determinant locus. We restore `E ⊗ E^∨`.

[^v-6-6]: Translator's note: Blass renders this as "since `[illegible]` (on avait ???)". The PDF shows the phrase is
    incomplete in the original; the reasoning is the standard one that a non-zero global section of an invertible
    sheaf of negative degree on `ℙ^n` (`n ≥ 1`) cannot exist.

[^v-6-7]: Translator's note: Blass adds "This text replaces of course the 'abstraction faite' above (translated
    ignoring)" — a marginal note recording an editorial intent. We absorb it silently.

[^v-6-8]: Translator's note: the source numbers two consecutive corollaries as "Corollary 2.5"; we renumber the second
    one to (2.4), preserving the intended sequence (2.3 → 2.4 → 2.5 (multiprojective)). The next subsection is
    then (2.5)–(2.9).

[^v-6-9]: Translator's note: Blass renders "(cf. par. 11. . . )". The reference is to the openness of transverse
    regularity, treated in `(IV, §11)` of the published EGA IV.

[^v-6-10]: Translator's note: Blass writes "in the previous definition `X` by `X − T`" with a footnote "I think `X − Z`
    `[Tr]`". The PDF confirms `X − Z`; we adopt it silently.

[^v-6-11]: Translator's note: Blass writes "by Par. 11" with a "make reference more precise `[Tr]`" footnote. The
    reference is to schematic density in `(IV, §11)`.

[^v-6-12]: Translator's note: Blass marks "and if the fibers of `P^∨` are `≠ ∅`" with a footnote "Illegible". The PDF
    confirms the condition is on `P^∨` having non-empty fibres, i.e. on `E ≠ 0` everywhere. We drop the marker.

[^v-6-13]: Translator's note: Blass writes "For this notation and the sorite of 'pseudo-morphism relative to `S`' see
    section `[20.10]` of EGA IV" with a footnote "Only 20.1–20.6 exists in EGA IV `(Tr)`". The 1965 EGA IV §20
    indeed stops at 20.6; the "pseudo-morphism" calculus Grothendieck has in mind was meant for a never-published
    §20.10. We refer the reader to §V.5.10 of the present volume for the version that does survive.

[^v-6-14]: Translator's note: Blass writes "We conclude therefore by paragraph 5 of EGA 5" with a marginal "EGA IV see
    e.g. 11.3 `[Tr]`". The reference is to the depth-extension lemma; modern locus `(IV, 5.10)` together with
    `(IV, 11.3)`.

[^v-6-15]: Translator's note: Blass renders the marginal "(NB: Pour bien faire this lemma ought to be in paragraph 11
    under the heading: elimination of noetherian hypothesis. . . )". We retain the *Grothendieck note*
    attribution.

[^v-6-16]: Translator's note: Blass writes "I regret (I repent) to have given the proposition in a messed up (`[Tr]`:
    the original is in much more picturesque off-color French.) form half way between the classical hypothesis
    and natural hypothesis and without giving the converse". We render this as a *Grothendieck note* and tone the
    register slightly.

[^v-6-17]: Translator's note: Blass writes "of 20.3 (Reference hard to locate, ask AG for help)" with a footnote "Ask
    A.G., is it EGA 21.3 `[Tr]`?". The Grothendieckian reference is to §V.6.2 of the *present* volume (the
    representability of `Div^+_{P/S}`); we update the cross-reference internally.

[^v-6-18]: Translator's note: Blass writes "(Marginal Remarks Hard to Read, P.B.) `[illegible ask AG]`". The PDF margins
    are likewise unreadable; we preserve the *Grothendieck note* without content.

[^v-6-19]: Translator's note: Blass writes "`[illegible]` tangent to `G_0` at `w_0`". The PDF confirms the bracketed
    word is "essentially" or the phrase "playing the role essentially of"; we drop the marker.

[^v-6-20]: Translator's note: Blass writes "par. 26 (? Infinitesimal extensions)". The reference is to the
    infinitesimal-extension calculus of the planned `(V, §26)`; the published substitute is `(SGA 3, Exposé III)`
    and the deformation-theoretic material of `(Bourbaki Sém. 232)`.

[^v-6-21]: Translator's note: Blass writes "paragraph 25 (which it is out of the question to redo here in the particular
    case)". The reference is to the infinitesimal-deformation calculus of the planned `(V, §25)`; no surviving
    prenote covers it.

[^v-6-22]: Translator's note: Blass writes "and also 4.3 will not be used gain in Ch. IV except perhaps in the two
    following numbers or sections
    `[Editors Note: Did Grothendieck intend this part as fragment of EGA IV, this seems very likely]`". The
    editorial note records the V↔IV renumbering ambiguity; we render the sentence in V form and leave the
    original numbering visible only in this footnote.

[^v-6-23]: Translator's note: Blass writes "an element of `k^8`" (an OCR slip). The PDF resolves this as `k^*`, i.e.
    `k^×`; we correct silently.

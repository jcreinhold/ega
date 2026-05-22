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

*Let $X$ be a regular prescheme, and $\phi$ a section of $\mathcal{O}_{X}$. A point $x \in X$ is called a **singular
zero** (or **root**) of $\phi$ if $\phi_{x} \in \mathfrak{m}^{2}_{x}$. It is called a **supersingular zero** if it is a
singular zero and if, in addition, the image of $\phi_{x}$ in $\mathfrak{m}^{2}_{x} / \mathfrak{m}^{3}_{x} \cong
Sym^{2}(\mathfrak{m}_{x} / \mathfrak{m}^{2}_{x})$ — interpreted as a quadratic form on the dual $t_{x}$ of
$\mathfrak{m}_{x} / \mathfrak{m}^{2}_{x}$ over $k(x)$ — is degenerate. A singular zero that is not supersingular is
sometimes called an **ordinary singular zero**.*

**Remark (1.2).**

<!-- label: V.1.2 -->

*If $x \in V(\phi)$, then $x$ is a non-singular zero of $\phi$ if and only if $\phi_{x} \neq 0$ and $x$ is a
non-singular (that is, regular) point of $V(\phi)$, equivalently if and only if $x$ is a regular point of $V(\phi)$ and
$V(\phi) \neq X$ in a neighbourhood of $x$.*

**Definition (1.3).**

<!-- label: V.1.3 -->

*Let $X$ be a smooth prescheme over a field $k$, $\phi$ a section of $\mathcal{O}_{X}$, and $x \in V(\phi)$. We say that
$x$ is a **geometrically singular** (resp. **geometrically supersingular**) zero of $\phi$ relative to $k$ if for every
extension $k'/k$ and every point $\xi$ of $X$ with values in $k'$ localized at $x$, the corresponding point $x'$ of
$X_{k'}$ is a singular (resp. supersingular) zero of $\phi_{k'}$.*

**Remarks (1.4).**

<!-- label: V.1.4 -->

*(a) From the criterion to be developed below it follows that in Definition (1.3) it suffices to test with a single
point with values in some $k'$ — one can take $k' = k(x)$ or $\overline{k(x)}$ and the canonical point with values in
this $k'$.*

*(b) From Remark (1.2) it follows that $x$ is geometrically non-singular for $\phi$ if and only if $\phi_{x} \neq 0$ and
$V(\phi)$ is smooth over $k$ at $x$.*

*(c) Suppose given a prescheme $X$ smooth over another prescheme $Y$, a section $\phi$ of $\mathcal{O}_{X}$, and an $x
\in V(\phi)$. We say that $x$ is a singular (resp. supersingular) zero **relative to $Y$** if it is a singular (resp.
supersingular) zero relative to $k(s)$ over the fibre $X_{s}$, where $s$ is the image of $x$ in $Y$.*

*(d) Under the conditions of Definition (1.1), the singularity (resp. supersingularity) of an $x \in V(\phi)$ for $\phi$
is not modified if one replaces $\phi$ by $\phi' = u\phi$ where $u$ is a unit at $x$. It follows immediately that
Definition (1.1), and hence also Definition (1.3), extends in an obvious way to the case where $\phi$ is a section of an
invertible module $L$ (in such a way as to recover the original definition when $L = \mathcal{O}_{X}$).*

<!-- original page 2 -->

### V.1.5. Differential criteria; the zero set of $d^{0}\phi$ and $d^{1}\phi$

Let $X$ be a prescheme smooth over another prescheme $Y$, and let $\phi$ be a section of $\mathcal{O}_{X}$. Then $\phi$
gives rise to a section $d^{2}_{X/Y} \phi$ of $\mathcal{P}^{2}_{X/Y}$, which reduces to a section $d^{1}_{X/Y} \phi$ of
$\mathcal{P}^{1}_{X/Y}$, which itself reduces to the section $d^{0}\phi = \phi$ of $\mathcal{P}^{0}_{X/Y} =
\mathcal{O}_{X}$.

**Proposition (1.5).**

<!-- label: V.1.5 -->

*The set of zeros of $d^{0}\phi$ (resp. $d^{1}\phi$) is equal to the set $V(\phi)$ of zeros of $\phi$ (resp. to the set
$V(\phi)_{sing}$ of zeros of $\phi$ singular relative to $S$).*

The first assertion is trivial. The second is just the Jacobian criterion, or — if one prefers — it follows from the
canonical isomorphism $\mathfrak{m}_{x} / \mathfrak{m}^{2}_{x} \cong \Omega^{1}_{X/k}(x)$ valid when $x$ is a rational
point over $k$ of a prescheme $X$ over $k$.

Note that $gr^{1}(\mathcal{P}^{1}_{X/Y}) \cong \Omega^{1}_{X/Y}$, so that the restriction $d^{1}\phi |_{V(\phi)}$ can be
interpreted as a section of $\Omega^{1}_{X/Y} \otimes \mathcal{O}_{V(\phi)}$, which is precisely the restriction of
$d_{X/Y} \phi$ to $V(\phi)$. We can therefore consider the prescheme of zeros of this section, which we denote
$V(\phi)_{sing}$, and whose underlying set is the set of zeros of $\phi$ singular relative to $Y$, by Proposition (1.5).

*Aside.* If $\psi$ is a section of a locally free module $E$ of finite type over a prescheme $X$, one defines in an
obvious way the sub-prescheme of zeros of $\psi$, for example as defined by the image ideal of the map $E^{\vee} \to
\mathcal{O}_{X}$ given by the transpose of $\psi$. When $E = \mathcal{O}^{n}_{X}$ and $\psi = (\psi_{1}, \cdots,
\psi_{n})$, this ideal is just $\sum \psi_{i} \mathcal{O}_{X}$, which defines $V(\psi_{1}, \cdots, \psi_{n})$.

Now taking the restriction $d^{2}\phi |_{V(\phi)_{sing}}$ and noting that $gr^{2}(\mathcal{P}^{2}_{X/Y}) \cong
Sym^{2}(\Omega^{1}_{X/Y})$, we obtain a canonical section $M(\phi)$ of $Sym^{2}(\Omega^{1}_{X/Y}) \otimes
\mathcal{O}_{V(\phi)_{sing}}$. Taking points of $X$ with values in fields, one sees immediately that this section is
precisely the one that determines the quadratic forms given in Definition (1.1) (in the case where $X_{k}$ is deduced
from $X/S$ by $\operatorname{Spec}(k) \to S$). One deduces a description of the set $V(\phi)_{supsing}$ in terms of this
section as follows: interpreting $M(\phi)$ as defining a homomorphism

```text
  M(φ)′ : 𝒢_{X/Y} ⊗_{𝒪_X} 𝒪_{V(φ)_sing} → Ω^1_{X/Y} ⊗_{𝒪_X} 𝒪_{V(φ)_sing},
```

take the set of points at which this homomorphism is not an isomorphism. This shows in particular that
$V(\phi)_{supsing}$ is a closed set. One can make the latter more precise by introducing

```text
  D(φ) = det M(φ) ∈ Γ(Ω^d_{X/Y})^{⊗ 2} ⊗ 𝒪_{V(φ)_sing}
```

and supposing that $X$ has constant relative dimension $d$ over $Y$. One may then use $V(\phi)_{supsing}$ to denote the
closed sub-prescheme of $V(\phi)_{sing}$ (and hence of $X$) defined by the vanishing of this section (now a section of
an invertible module), whose underlying set is the right one.

> *Grothendieck note.* It would be a good thing to summarize the above construction into a Proposition (1.6).[^v-1-1]

In the general case we cannot say anything more precise about $V(\phi)_{sing}$ and $V(\phi)_{supsing}$. Let us examine a
special case that is interesting for certain applications.

<!-- original page 3 -->

### V.1.7. The supersingular set as a ramification locus

Assume that $Y$ is also smooth over a prescheme $S$, with constant relative dimension $m$ (to fix our ideas), and that
$V(\phi)_{sing}$, which we denote $V'$ for short — defined by the vanishing of the section $d^{1}$ of the locally free
module $\mathcal{P}^{1}_{X/Y}$ of rank $d + 1$ — is smooth over $S$ of relative dimension $(m + 1) - (d + 1) = m - 1$.

The notations $V(\phi)_{sing}$ and $V(\phi)_{supsing}$ are ambiguous in that the prescheme over which they are defined
is left implicit; we tacitly fix $Y$.[^v-1-2] Note that it follows from the assumptions that every singular zero of
$\phi$ is non-singular relative to $S$. In this situation one can write down the following diagram of locally free
modules over $V'$:

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

The columns come from the transitivity exact sequence for the smooth morphisms $X \to Y$ and $Y \to S$, tensored with
$\mathcal{O}_{V'}$ (this remains exact since all the modules involved are locally free). The horizontal line is a
particular case of an exact sequence obtained whenever, over $X/S$, we have a section $\psi$ of a locally free module
$F$, and take the scheme of zeros $W$:

```text
  F^∨ ⊗ 𝒪_X → Ω^1_{X/S} ⊗ 𝒪_W → Ω^1_{W/S} → 0;
```

if $X/S$ is smooth, the first homomorphism is injective exactly at the points where $W$ is smooth over $X$ with a "good"
relative dimension (here, everywhere). This exact sequence is an immediate consequence of the exact sequence

```text
  𝒥/𝒥² → Ω^1_{X/S} ⊗ 𝒪_W → Ω^1_{W/S} → 0
```

appearing in §V.1.5; the version we use here could be stated as its corollary.

The characterization of the set of points where the left-most arrow fails to be a monomorphism is contained in the
Jacobian criterion.

<!-- original page 4 -->

Note the canonical isomorphism $\mathcal{P}^{1}_{X/S} \cong \Omega^{1}_{X/S} \oplus \mathcal{O}_{X}$, whence
$\mathcal{P}^{1}_{X/S} \otimes \mathcal{O}_{V'} \cong \mathcal{G}_{X/S} \oplus \mathcal{O}_{X}$.[^v-1-3] On the other
hand, one verifies that the composed homomorphism $\mu$ in the diagram above is zero on the factor $\mathcal{O}_{V'}$,
and on the factor $\mathcal{G}_{X/S} \otimes \mathcal{O}_{V'}$ it reduces to the homomorphism $M(\phi)'$ deduced from
the section $M(\phi)$ of $Sym^{2}(\Omega^{1}_{X/S}) \otimes \mathcal{O}_{V'}$ already mentioned. Thus at a point $x \in
X$, $M(\phi)$ is non-degenerate — that is, $M(\phi)'$ is surjective — if and only if $\mu$ is surjective at $x$, and we
see from the diagram that this is also equivalent to saying that $\nu$ is surjective at $x$ (since both conditions
assert that the canonical homomorphism from the sum of the two cited submodules of $\Omega^{1}_{X/S} \otimes
\mathcal{O}_{V'}$ into the latter is surjective at $x$).

We therefore find:

**Proposition (1.7).**

<!-- label: V.1.7 -->

*Under the preceding conditions (to be recalled), the underlying set of $V(\phi)_{supsing}$ is exactly the set of points
of $V(\phi)_{sing}$ at which the morphism $V(\phi)_{sing} \to Y$ (of smooth preschemes over $S$ of relative dimensions
$m - 1$ and $m$, respectively) is ramified.*

In the old language[^v-1-4] — which should perhaps be added as a remark — a point $x \in V(\phi)$ is supersingular
relative to $Y$ if and only if "it consists of at least two coinciding (infinitely near) singular points."

We must make Proposition (1.7) more precise from the point of view of an identity of sub-preschemes, not just of
subsets. Indeed, $V(\phi)_{supsing}$ has been defined as a closed sub-prescheme of $X$; on the other hand, we can
equally well define a natural closed sub-prescheme of $V'$ whose underlying subset is the set of ramification points
relative to $Y$. Indeed, it suffices to express the set of points where a certain homomorphism of locally free modules
$Q = \Omega^{1}_{Y/S} \otimes \mathcal{O}_{V'} \to M = \Omega^{1}_{V'/S}$ fails to be surjective. If $q$ and $r$ are
their respective ranks, this is also the set of points where $\Lambda^{q} Q \to \Lambda^{r} M$ fails to be surjective,
equivalently the zero set of the evident section of $\operatorname{Hom}(\Lambda^{q} Q, \Lambda^{r} M) \cong (\Lambda^{q}
Q)^{\vee} \otimes \Lambda^{r} M$. We thus obtain a closed sub-prescheme of zeros of this section, which we call
$Ram(V'/Y)$.

*Claim.* $Ram(V'/Y) = V(\phi)_{supsing}$ (as closed sub-preschemes of $V'$).

This is a straightforward exercise on the diagram above, taking into account that $V(\phi)_{supsing}$ is defined by the
same procedure as the one made explicit for $Q \to R$ but in terms of the homomorphism $\mathcal{P} =
\mathcal{P}^{1}_{X/Y} \otimes \mathcal{O}_{V'} \to S = \Omega^{1}_{X/Y} \otimes \mathcal{O}_{V'}$, as follows from the
description of $\mu$ given above. We are thus reduced to the following general situation.

<!-- original page 5 -->

### V.1.8. A general lemma on locally free modules

We have on a ringed space $W$ a locally free module $M$ of rank $m$, and two locally free submodules $P$ and $Q$ of
respective ranks $p$ and $q$ with $p + q = m + 1$. Using the previous construction, applied to the morphisms $P \to M/Q
= S$ and $Q \to M/P = R$, we find the sections

(a) of `P ⊗ det S ⊗ det P^{−1} = P ⊗ det M ⊗ det P^{−1} ⊗ det Q^{−1}`, and

(b) of `Q ⊗ det M ⊗ det P^{−1} ⊗ det Q^{−1}`,

which we may also view as homomorphisms of `L = det P ⊗ det Q ⊗ det M^{−1}` into $P$ and into $Q$, respectively.

(For a locally free module $F$ we denote by `det F` its highest exterior power; we use the fact that for a short exact
sequence

$$ 0 \to F' \to F \to F'' \to 0 $$

of locally free modules of finite rank we have a canonical isomorphism `det F = det F′ ⊗ det F″`.)

With these conventions, we have the commutativity of the diagram[^v-1-5]

> *Source-trace note: the Blass source file 01 ends mid-diagram on page 5; the diagram and the subsequent argument are
> visible in the source PDF but were not captured by the Blass markdown transcription. We close §V.1 here with the
> construction already stated and refer the reader to the PDF for the final identification step that pins down
> $Ram(V'/Y) = V(\phi)_{supsing}$ as preschemes (rather than only as subsets).*

______________________________________________________________________

[^v-1-1]: Translator's note: in the source, this appears as Grothendieck's marginal aside ("It would be a good thing to
    summarize the above construction into a Proposition 6"). No Proposition (1.6) was ever written; we preserve the gap
    in numbering between (1.5) and (1.7) as in the prenote.

[^v-1-2]: Translator's note: Blass renders this with the parenthetical "(in the actual case it is assumed (sous entendu
    Fr) that it is $Y$)". The French *sous-entendu* ("understood", "tacitly assumed") survives in the Blass source; we
    modernize to "tacitly fix".

[^v-1-3]: Translator's note: Blass writes "(in the original the G is elongated)" at this point. The elongated $G$ refers
    to the symbol Grothendieck uses for the tangent sheaf $\mathcal{G}_{X/S}$ (kernel of the augmentation
    $\mathcal{P}^{1} \to \mathcal{O}$); we render it $\mathcal{G}_{X/S}$ throughout. Blass himself queries: "Is the
    elongated G the tangent sheaf? [Tr]". The answer is yes.

[^v-1-4]: Translator's note: Blass renders this as "in the language of the fathers (en termes de papa Fr)". The French
    *en termes de papa* ("in dad's terms") is Grothendieck's affectionate phrase for classical (pre-EGA)
    algebraic-geometry vocabulary; we render "in the old language".

[^v-1-5]: Translator's note: the Blass source ends here ("This being given, we have the commutativity of the diagram")
    with the diagram itself untranscribed; we end the section at the verbal claim and direct the reader to the source
    PDF for the remaining lines of the argument.

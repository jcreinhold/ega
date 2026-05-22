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

Let $S$ be a prescheme, let $E$ be a locally free module of finite type over $S$, and let $E^{\vee}$ be its dual. We
denote by $P = P(E) = \mathbb{P}(E)$ the projective fibration defined by $E$, and by $P^{\vee} = \mathbb{P}(E^{\vee})$
the projective fibration defined by $E^{\vee}$. We shall call $P^{\vee}$ the **scheme of hyperplanes** of $P$. This
terminology can be justified as follows. Let $\xi$ be a section of $P^{\vee}$ over $S$, determined by an invertible
quotient module $L$ of $E^{\vee}$. From it we obtain an invertible quotient module `L_P` of $(E^{\vee})_{P} =
(E_{P})^{\vee}$; on the other hand, we have the invertible quotient module $\mathcal{O}_{P}(1)$ of `E_P`. Passing to
duals, we may take $L^{-1}_{P}$ and $\mathcal{O}_{P}(-1)$ to be invertible submodules (locally direct factors) of `E_P`
and of $(E_{P})^{\vee}$ respectively, and the pairing $E_{P} \otimes E^{\vee}_{P} \to \mathcal{O}_{P}$ defines therefore
a natural pairing

$$ (*) \mathcal{O}_{P}(-1) \otimes L^{-1}_{P} \longrightarrow \mathcal{O}_{P}, $$

or equivalently the transposed homomorphism

```text
  (**)                           𝒪_P ⟶ 𝒪_P(1) ⊗ L_P = L_P(1),
```

that is, a section of $L_{P}(1)$ canonically defined by $\xi$. The "divisor" of this section, i.e. the closed subscheme
$H_{\xi}$ of $P$ defined by the image ideal of `(*)`, is called the **hyperplane in $P$ defined by the element** $\xi
\in P^{\vee}(S)$. We could describe it by noting that, locally over $S$, $\xi$ is given by a section $\phi$ of $E$ such
that $\phi(s) \neq 0$ for all $s$ ($\phi$ is determined by $\xi$ up to multiplication by an invertible section of
$\mathcal{O}_{S}$); since $E = p_{*}(\mathcal{O}_{P}(1))$ ($p : P \to S$ being the projection), $\phi$ can be considered
as a section of $\mathcal{O}_{P}(1)$, and the divisor of this section is nothing else but $H_{\xi}$.

Of course, if we consider $L^{-1}$ as an invertible submodule of $E$, locally a direct factor in $E$, then the
correspondence between $\xi$ (that is, $L$, or $L^{-1} \subset E$) and $\phi$ is obtained by taking for $\phi$ a section
of $L^{-1}$ which does not vanish at any point — i.e. by a trivialization of $L^{-1}$ (which exists in every case
locally). Let us note that $H_{\xi}$ is nothing else but $\mathbb{P}(E / L^{-1})$ (canonical isomorphism); this is a
third way of describing $H_{\xi}$. *(N.B. $\mathbb{P}(E / L^{-1})$ is indeed canonically embedded in $P =
\mathbb{P}(E)$, which has the advantage of proving in addition that $H_{\xi}$ is a projective fibration over $S$ and is
a fortiori smooth over $S$. It would still be necessary to say in §17 of EGA IV that a projective fibration is smooth.)
Without a doubt it would be better to begin with this description.*

**Remarks (5.1.1).**

<!-- label: V.5.1.1 -->

*The formation of $H_{\xi}$ is compatible with base change; in other words one finds a homomorphism of functors $(Sch/S)
\to (Sets)$,*

$$ P^{\vee} \longrightarrow \operatorname{Div}(P/S), $$

*where the second term denotes the functor of "relative divisors" of $P/S$, whose value at an arbitrary $S$-prescheme
$S'$ is the set of closed subschemes of $P_{S'}$ which are complete intersections, transversal to and of codimension `1`
relative to $S'$ (compare §V.19, formerly IV, 19).[^v-5p1-3]*

<!-- original page 4 -->

It is easy to show that this homomorphism of functors is a monomorphism — in other words, that $\xi$ is determined by
$H_{\xi}$. (This last fact justifies the terminology "scheme of hyperplanes" used above.) We shall see that the functor
$\operatorname{Div}(P/S)$ is representable by the prescheme (direct) sum of the $\mathbb{P}(Sym^{k}(E^{\vee}))$, so that
$P^{\vee}$ can be identified to an open and closed subscheme of $\operatorname{Div}(P/S)$. *(Compare Mumford, _Lectures
on curves on an algebraic surface_.)* *(N.B. To tell the truth, the determination of the relative divisors of $P/S$
could be done with the means available right now, using results of Chapter II, and could be added as an example to
§IV.19.)*

Let us now make the base change $S' = P^{\vee} \to S$ and consider the diagonal section (or "generic section") of
$P^{\vee}_{S'} = \mathbb{P}(E^{\vee}_{S'})$ over $S'$: we find a closed subscheme $H$ of $P_{S'} = P \times_{S}
P^{\vee}$ — sometimes called the **incidence scheme** between $P$ and $P^{\vee}$ — defined by the image ideal of the
canonical homomorphism

```text
  𝒪_P(-1) ⊗_S 𝒪_{P^∨}(-1) ⟶ 𝒪_{P ×_S P^∨},
```

from which we see that it is a projective fibration over $P^{\vee}$; by symmetry it is also a projective fibration over
$P$. Note that one recovers the "special" hyperplanes $H_{\xi}$ (for $\xi$ a section of $P^{\vee}$ over $S$) by starting
from the "universal hyperplane" $H$ and taking its inverse image under the base change $\xi : S \to P^{\vee}$.

The same remark holds for every point of $P^{\vee}$ with values in an arbitrary $S$-prescheme $S'$, which (considered as
a section of $P^{\vee}_{S'}$ over $S'$) allows us to define an $H_{\xi} \subset P_{S'}$; the latter is nothing else but
the inverse image of $H$ by the base change $\xi : S' \to P^{\vee}$.

In what follows we assume given a prescheme $X$ of finite type over $P$,[^v-5p1-4] together with an $S$-morphism $f : X
\to P$. One of the main objectives of this paragraph is to study, for every hyperplane $H_{\xi}$ of $P$, its inverse
image

```text
  Y_ξ = f^{-1}(H_ξ) = X ×_P H_ξ,
```

and especially to relate the properties of $X$ and $Y_{\xi}$. As usual, one also has to consider the $P^{\vee}(S')$ for
an arbitrary $S$-scheme $S'$; in that case $H_{\xi}$ is a hyperplane in $P_{S'}$, and we put again

```text
  Y_ξ = f_{S'}^{-1}(H_ξ) = X_{S'} ×_{P_{S'}} H_ξ = X ×_P H_ξ,
```

where the subscript $S'$ denotes as usual the effect of the base change $S' \to S$, and where in the last expression we
consider $H_{\xi}$ as a $P$-scheme via the combined morphism $H_{\xi} \to P_{S'} \to P$. It is therefore again
convenient to consider the case where $\xi$ is "universal", i.e. where $S' = P^{\vee}$ and $\xi$ is the diagonal
section, so that $H_{\xi} = H$; in this case one observes (subject to better notations to be suggested by Dieudonné)
that $Y = Y_{\xi}$. In the general case of a $\xi : S' \to P^{\vee}$, one therefore has also $Y_{\xi} = Y
\times_{P^{\vee}} S'$. Finally, if $F$ is a sheaf of modules[^v-5p1-5] over $X$, we denote by $G_{\xi}$ its inverse
image over $Y_{\xi}$, by $G$ its inverse image over $H$, so that one also has $G_{\xi} = G
\otimes_{\mathcal{O}_{P^{\vee}}} \mathcal{O}_{S'}$.

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

In the next subsection (§V.5.2) we shall study systematically the following case: $S'$ is the spectrum of a field $K$,
and its image in $P^{\vee}$ is the generic point of the corresponding fibre $P^{\vee}_{s}$. After making the base change
$\operatorname{Spec} k(s) \to S$, we are reduced to the case where $S$ is the spectrum of a field $k$, which is what we
shall assume in the next subsection. Also, the majority of properties studied for $X$ and $Y_{\xi}$ are of "geometric"
nature and therefore invariant under base change, which allows us also (without loss of generality) to restrict
ourselves to the case where $K$ is algebraically closed, or to the case where $K = k(\eta)$, $\eta$ being the generic
point of $P^{\vee}$, and $\xi : \operatorname{Spec}(K) \to P^{\vee}$ is of course the canonical morphism. We also note
that for geometric questions concerning $X, Y_{\xi}$ we can (after making a base change) restrict ourselves to the case
of $k$ algebraically closed.

**A terminological reminder.** If $f$ is an immersion, we usually call $Y_{\xi}$ a **hyperplane section** of $X$
(relative to the projective immersion $f$ and the hyperplane $H_{\xi}$). There is no reason not to extend this
terminology to the case of an arbitrary $f$.

### V.5.2. Study of a generic hyperplane section: local properties

Let us recall that, from now on, $S = \operatorname{Spec}(k)$, with $k$ a field. If $\eta$ is a point of $P^{\vee}$ and
if $\xi : \operatorname{Spec} k(\eta) \to P^{\vee}$ is the canonical morphism, we also write $H_{\eta}$, $Y_{\eta}$,
$G_{\eta}$ in place of $H_{\xi}$, $Y_{\xi}$, $G_{\xi}$.

In this subsection, $\eta$ always denotes the generic point of $P^{\vee}$.

**Proposition (5.2.1).**

<!-- label: V.5.2.1 -->

*Assume that $X$ is irreducible. Then $Y_{\eta}$ is irreducible or empty, and in the first case it dominates $X$; the
prescheme $Y$ is then irreducible as well.*

Indeed, since $H \to P$ is a projective fibration, the same is true of $Y \to X$, which implies that $Y$ is irreducible
whenever $X$ is. The generic fibre $Y_{\eta}$ of $Y \to P^{\vee}$ is then irreducible or empty; in the first case its
generic point is the generic point of $Y$, which therefore lies over the generic point of $X$.

<!-- original page 6 -->

**Proposition (5.2.2).**

<!-- label: V.5.2.2 -->

*Let $Z$ be a subset of $P$. Then its inverse image $Z_{\eta}$ in $H_{\eta}$ is empty if and only if every point of $Z$
is closed. In particular, if $Z$ is constructible, then $Z_{\eta} = \emptyset$ if and only if $Z$ is finite.*

We may suppose that $Z$ is reduced to a single point $z$, and we only have to prove that the image of $H_{\eta}$ in $P$
consists exactly of the non-closed points of $P$. Denoting by $X$ the closure of $z$ and using (5.2.1), we only have to
prove that $Z_{\eta} = \emptyset$ if and only if $X$ is finite ($X$ being a closed subscheme of $P$). Replacing $X$ by
$X_{k(\eta)} \hookrightarrow P_{k(\eta)}$, the "only if" part follows from the following fact (for which we need to give
a reference and which deserves to be restated here as a lemma): if $Y$ is any hyperplane section of $X$ and if $Y_{\eta}
= \emptyset$, then $X$ is finite (indeed, $X \subset P - H$ is affine and projective). The "sufficient" part is
immediate: for example, $Y$ is a projective fibration of relative dimension $n - 1$ over $X$ ($n$ being the relative
dimension of $P$ and $P^{\vee}$ over $S$); since $X$ is finite over $k$, $Y$ is of absolute dimension $n - 1 = \dim
P^{\vee} - 1$, hence the morphism $Y \to P^{\vee}$ cannot be dominant and its generic fibre $Y_{\eta}$ is empty.

**Corollary (5.2.3).**

<!-- label: V.5.2.3 -->

*Let $f : X \to P$ be a morphism of finite type, and let $Z$ be a constructible subset of $X$. In order that its inverse
image in $Y_{\eta}$ be empty, it is necessary and sufficient that the image $f(Z)$ be finite. In particular, in order
that $Y_{\eta}$ be empty, it is necessary and sufficient that $f(X)$ be finite.*

**Corollary (5.2.4).**

<!-- label: V.5.2.4 -->

*Let `Z, Z'` be two closed subsets of $X$ with $Z$ irreducible, and let $Z_{\eta}$ and $Z'_{\eta}$ be their inverse
images in $Y_{\eta}$. In order to have $Z_{\eta} \subset Z'_{\eta}$, it is necessary and sufficient that $f(Z)$ be
finite, or that $Z \subset Z'$. In order that $Z_{\eta} = Z'_{\eta}$, it is necessary and sufficient that both $f(Z)$
and $f(Z')$ be finite, or that $Z = Z'$.*

This is an immediate consequence of (5.2.3), since we see that $f(Z - Z \cap Z')$ can be finite only if $Z \subset Z'$
or if $f(Z)$ is finite: if $Z \nsubset Z'$, then $Z - Z \cap Z'$ is dense in $Z$, so $f(Z - Z \cap Z')$ is dense in
$f(Z)$; if the former is finite and hence (being constructible) closed, then so is the latter.[^v-5p1-6]

<!-- original page 7 -->

**Corollary (5.2.5).**

<!-- label: V.5.2.5 -->

*To every irreducible component $X_{i}$ of $X$ such that $\dim f(X_{i}) > 0$ we assign its inverse image $Y_{i,\eta}$ in
$Y_{\eta}$. Then $Y_{i,\eta}$ is an irreducible component of $Y_{\eta}$, and we obtain in this manner a one-to-one
correspondence between the set of irreducible components $X_{i}$ of $X$ such that $\dim f(X_{i}) > 0$ and the set of
irreducible components of $Y_{\eta}$.*

Indeed, it follows from (5.2.3) that $Y_{\eta}$ is the union of the $Y_{i,\eta}$ defined above, and that the latter are
closed and non-empty subsets of $Y$; they are also irreducible by (5.2.1). Finally, they are mutually without an
inclusion relation by (5.2.4), whence the conclusion.

Let us notice that if $\dim X_{i} = d_{i}$, then $\dim Y_{i,\eta} = d_{i} - 1$. More generally:

**Proposition (5.2.6).**

<!-- label: V.5.2.6 -->

*Suppose that for every irreducible component $X_{i}$ of $X$ we have $\dim f(X_{i}) > 0$, i.e. $Y_{i,\eta} \neq
\emptyset$; or, where $f$ is an immersion, that $\dim f(X) > 0$. Then $\dim Y_{\eta} = \dim X - 1$.*

We are reduced to the case where $X$ is irreducible, by (5.2.5). By the very construction, $Y_{\eta}$ is defined
starting from $X_{k(\eta)}$ as the divisor of a section of an invertible module over $X_{k(\eta)}$ (the inverse image of
$\mathcal{O}_{P}(1)$). On the other hand, $X_{k(\eta)}$ is irreducible (because $X$ is such and $k(\eta)$ is a purely
transcendental extension of $k$, which fact one should have indicated at the beginning of the subsection), and $Y_{\eta}
\neq X_{k(\eta)}$, since the image of $Y_{\eta}$ in $X$ (contrary to that of $X_{k(\eta)}$, which is faithfully flat
over $X$) is not equal to $X$: indeed, it does not contain the closed points of $X$, by (5.2.3). It follows that
`dim Y_η = dim X_{k(η)} − 1 = dim X − 1`.

**Proposition (5.2.7).**

<!-- label: V.5.2.7 -->

*Let $F$ be a quasi-coherent module over $X$, and hence $G_{\eta}$ over $Y_{\eta}$. Let $(Z_{i})$ be the prime cycles
associated to $F$ such that $\dim f(Z_{i}) > 0$, and let $Z_{i,\eta}$ be the inverse image of $Z_{i}$ in $Y_{\eta}$.
Then the $Z_{i,\eta}$ are exactly all the prime cycles associated to $G_{\eta}$. Moreover, their inclusion relations are
the same as those among the $Z_{i}$.*

The last assertion is contained in (5.2.4). On the other hand, since $Y \to X$ is a projective fibration — hence flat
with fibres `(S_1)` and irreducible — it follows from §IV.3 that the prime cycles associated to the inverse image $G$ of
$F$ over $Y$ are the inverse images of the prime cycles associated to $F$. Restricting to the generic fibre $Y_{\eta}$
of $Y$ over $P^{\vee}$, we obtain that the prime cycles associated to $G_{\eta}$ are the non-empty inverse images of the
$Z_{i}$, which proves (5.2.7) by means of (5.2.3).

To tell the truth, the passage through $Y$ is unnecessary: we can use directly the fact that $Y_{\eta} \to X$ is flat
with fibres `(S_1)` and irreducible (in fact even geometrically regular, and with geometrically irreducible fibres, the
latter being localizations of projective schemes); this is the remark to make for the proof of (5.2.1).

<!-- original page 8 -->

**Proposition (5.2.8).**

<!-- label: V.5.2.8 -->

*Let $F$ be coherent over $X$, let $y \in Y_{\eta}$, and let $x$ be its image in $X$. Let $P(M)$ be one of the following
properties of a module of finite type $M$ over a local noetherian ring $A$:*

*(i) $coprof M \leq n$;*

*(ii) $M$ satisfies $(S_{k})$;*

*(iii) $M$ is Cohen-Macaulay;*

*(iv) $M$ is reduced;*

*(v) $M$ is integral.*

*Then in order that $G_{\eta, y}$ should satisfy $P$, it is necessary and sufficient that $F_{x}$ should satisfy it.*

This follows immediately from the results of §IV.6, taking into account that $Y_{\eta} \to X$ is a regular morphism, so
that $\mathcal{O}_{X, x} \to \mathcal{O}_{Y_{\eta}, y}$ is regular.[^v-5p1-7] Taking (5.2.3) into account, we obtain:

**Corollary (5.2.9).**

<!-- label: V.5.2.9 -->

*With the notation of (5.2.8), let $Z$ be the set of $x \in X$ such that $P(F_{x})$ is not satisfied. Then in order that
$G_{\eta}$ should satisfy the condition $P$ at every point, it is necessary and sufficient that $f(Z)$ be a finite
subset of $P$, or — equivalently — that $\dim f(Z) = 0$.*

Indeed, (5.2.8) says that $h^{-1}(Z)$ is the $P$-singular subset of $G_{\eta}$, and it is empty if and only if $f(Z)$ is
finite, by (5.2.3). (Here $h$ denotes the morphism $Y_{\eta} \to X$. I have just realized that the letter $P$ in (5.2.8)
has been used twice; this should be resolved at the editing stage.)

**Corollary (5.2.10).**

<!-- label: V.5.2.10 -->

*The analogous condition for $Y_{\eta}$ to be reduced, respectively locally integral, follows from (5.2.8) (iv), (v).*

**Corollary (5.2.11).**

<!-- label: V.5.2.11 -->

*Let $y \in Y_{\eta}$. In order that $Y_{\eta}$ should be regular, respectively $(R_{k})$ at $y$ (respectively normal at
$y$), it is necessary and sufficient that $X$ should satisfy the same property at $x$. Let $Z$ be the set of points of
$X$ where $X$ is not regular, respectively not $(R_{k})$, respectively not normal; for $Y_{\eta}$ to be regular,
respectively $(R_{k})$, respectively normal, it is necessary and sufficient that $f(Z)$ be finite, i.e. that $\dim f(Z)
= 0$.*

The proof is the same as for (5.2.8) and (5.2.9). One must give the various references assuring that $Z$ is closed
(since one needs to know it is constructible in order to apply (5.2.3)).

Let us note that in (5.2.10) and (5.2.11) we do not speak at all of the corresponding geometric properties; the results
described are of "absolute" nature. We now examine the properties of geometric nature. (One could, if one wished, take
the opportunity to start a new subsection here.)

<!-- original page 9 -->

#### Geometric properties

**Theorem (5.2.12).**

<!-- label: V.5.2.12 -->

*Suppose that $f : X \to P$ is unramified. Let $y \in Y_{\eta}$, and let $x$ be its image in $X$. In order that $X$
should be smooth over $k$ at $x$, it is necessary and sufficient that $Y_{\eta}$ should be smooth over $k(\eta)$ at
$y$.*

We may assume that $k$ is algebraically closed. If $Y_{\eta}$ is smooth over $k(\eta)$ at $y$, it is regular, and so,
since $Y_{\eta}$ is flat over $X$, $X$ is regular at $x$; therefore $X$ is smooth over $k$ at $x$, since $k$ is
algebraically closed and thus perfect.

For the converse, we can (after replacing $X$ by an open neighbourhood of $x$) assume that $X$ is smooth, and, by the
Jacobian criterion of smoothness, that it is defined in an open subset $U$ of $P$ by $p$ equations,

$$ X = V(f_{1}, \cdots, f_{p}), $$

where the differentials $df_{1}, \cdots, df_{p}$ are everywhere linearly independent. Introducing the affine coordinates
$S_{1}, \cdots, S_{n}$ in $P^{\vee}$ and the affine coordinates $T_{1}, T_{2}, \cdots, T_{n}$ in a neighbourhood of $x$
(by choosing a hyperplane $H_{\infty}$ at infinity not containing $x$), the immersion $Y_{\eta} \hookrightarrow
U_{k(\eta)}$ is then given by

```text
  Y_η = V(f_1, …, f_p, ∑ S_i T_i − 1),
```

and it suffices to verify that the differentials (relative to $k(\eta)$) of $f_{1}, \cdots, f_{p}, \sum S_{i} T_{i} - 1$
are linearly independent. These differentials are nothing else but the sections

```text
  df_1, …, df_p, ∑ S_i dT_i
```

of $\Omega^{1}_{U/k} \otimes_{k} k(\eta)$. Since the $df_{i}$ are linearly independent at every point of $U$, and since
the $dT_{i}$ form a basis of $\Omega^{1}_{U/S}$ at every point of $U$ (and a fortiori a system of generators), we
conclude immediately the linear independence of the displayed quantities at every point of $U_{k(\eta)}$ — at least when
$p < n$, i.e. when

```text
  E = Ω^1_{U/k} / ∑_{1 ≤ i ≤ p} 𝒪_U df_i ≠ 0.
```

This is a small lemma about a family of generators $a_{i}$, $1 \leq i \leq n$, of a non-zero locally free module $E$:
the section $\sum S_{i} a_{i}$ of $E \otimes_{k} k(\eta)$ does not vanish at any point. On the other hand, the case $p =
n$ is trivial, because then $Y_{\eta} = \emptyset$.

**Corollary (5.2.13).**

<!-- label: V.5.2.13 -->

*Let $Z$ be the set of points of $X$ where $X$ is not smooth over $k$. In order that $Y_{\eta}$ should be smooth over
$k(\eta)$, it is necessary and sufficient that $Z$ be finite. In particular, if $X$ is smooth, so is $Y_{\eta}$.*

This follows from (5.2.12) and (5.2.3). More generally we obtain:

**Theorem (5.2.14).**

<!-- label: V.5.2.14 -->

*Let $y$ be a point of $Y_{\eta}$, and $x$ its image in $X$. Let $P(A, K)$ be one of the following properties of a local
noetherian $K$-algebra $A$ over a field $K$:*

*(i) $A$ is geometrically regular over $K$;*

*(ii) $A$ is geometrically $(R_{k})$ over $K$;*

*(iii) $A$ is separable over $K$;*

*(iv) $A$ is geometrically normal over $K$.*

<!-- original page 10 -->

*Then $P(\mathcal{O}_{X, x}, k) \Longleftrightarrow P(\mathcal{O}_{Y_{\eta}, y}, k(y))$.*

Indeed, taking §IV.6 into account, (iii) and (iv) follow from (ii) and (5.2.8) (ii). On the other hand, (i) has been
proven in (5.2.12), and it remains to deduce (ii) from (i). To do this, let $Z$ be the set of points where $X$ is not
smooth over $k$; its inverse image $Z_{\eta}$ in $Y_{\eta}$ is therefore (by (5.2.12)) the set of points of $Y_{\eta}$
at which $Y_{\eta}$ is not smooth over $k(\eta)$. But the codimension of $Z$ in $X$ equals that of $Z_{\eta}$ in
$Y_{\eta}$ at $y$ because of flatness (see §IV.6); therefore one is $> k$ if and only if the other is, which completes
the proof.

**Corollary (5.2.15).**

<!-- label: V.5.2.15 -->

*Let $Z$ be the set of points of $X$ at which $X$ is not smooth over $k$ (respectively is not geometrically $(R_{k})$
over $k$, respectively is not separable over $k$, respectively is not geometrically normal over $k$). In order that
$Y_{\eta}$ should be smooth (respectively geometrically $(R_{k})$, respectively separable, respectively geometrically
normal) over $k(\eta)$, it is necessary and sufficient that $Z$ be finite.*

From the point of view of presentation, statements (5.2.14) and (5.2.15) contain (5.2.12) and (5.2.13) (which we could
thus dispense with stating separately); on the other hand, the corollary is practically more important than the theorem,
which one could give in a proposition or a preliminary lemma so that the corollary is the more glorified.

We can give a variant in the case of property (iii):

**Corollary (5.2.16).**

<!-- label: V.5.2.16 -->

*Suppose that $f$ is an immersion and that $F$ is coherent. Under the conditions of (5.2.7), in order that $Z_{i}$
should not be embedded, it is necessary and sufficient that $Z_{i,\eta}$ should not be embedded. If that is so, then the
radical multiplicity of $F$ at $Z_{i}$ relative to $k$ equals that of $G_{\eta}$ at $Z_{i,\eta}$ relative to $k(\eta)$.*

The first assertion is contained in the last assertion of (5.2.7). For the second, since $Y_{\eta} \to X$ is flat, the
functor $F \mapsto G_{\eta}$ is exact, and we are reduced by restriction to a neighbourhood of the generic point of
$Z_{i}$ and by *dévissage* to the case where $F = \mathcal{O}_{Z_{i}}$ and we may assume $Z_{i} = X$. Also, we could
start by assuming that $X$ is separated over $k$, and reduce to the case of $k$ algebraically closed.[^v-5p1-8] Then the
assertion is contained in (5.2.15) (iii). We conclude, as usual:

**Corollary (5.2.17).**

<!-- label: V.5.2.17 -->

*Let $Z$ be the set of points of $X$ where $F$ is not separable over $k$. Then $G_{\eta}$ is separable over $k(\eta)$ if
and only if $Z$ is finite. In particular, if $F$ is separable over $k$, then $G_{\eta}$ is separable over $k(\eta)$.*

<!-- original page 11 -->

**Remark (5.2.18).**

<!-- label: V.5.2.18 -->

*The key result (5.2.12) (and its consequences (5.2.13) and (5.2.17)) become false if we abandon the assumption that $f$
is an immersion, as we see for example by taking for $X$ a purely inseparable covering of $P$. However, if $k$ is of
characteristic zero, (5.2.12) and (5.2.17) are valid without assuming that $f$ is an immersion.*

Indeed, it suffices to verify this for (5.2.12), and this follows from (5.2.11) and the fact that, for an algebraic
prescheme in characteristic zero, smooth = regular.[^v-5p1-9]

### V.5.3. Generic hyperplane section: geometric irreducibility and connectedness

**Theorem (5.3.1) (Bertini-Zariski).**

<!-- label: V.5.3.1 -->

*Assume that $\dim f(X) \geq 2$ and that $X$ is geometrically irreducible. Then the generic hyperplane section
$Y_{\eta}$ has the same property.*

Let $K/k$ be the function field of $X$, and let $n = \dim P$; introducing the affine coordinates $T_{1}, \cdots, T_{n}$
in $P$ (by choosing a hyperplane at infinity $H_{\infty}$ such that $f(X)$ is not contained in it) and $S_{1}, \cdots,
S_{n}$ the affine coordinates in $P^{\vee}$, we see that the function field $L$ of $Y_{\eta}$ can be identified with the
field of fractions of the integral domain $K[S_{1}, \cdots, S_{n}] / (\sum t_{i} S_{i} - 1)$, where the $t_{i} \in K$
are the images of $T_{i}$ under $f : X \to P$. Since $\dim f(X) > 0$, the $t_{i}$ are not all algebraic over $k$ — a
fortiori, they are not all zero; suppose, for example, that $t_{n} \neq 0$. We realize then immediately that

$$ L = K(S_{1}, \cdots, S_{n-1}) $$

(a purely transcendental extension), $S_{n} \in L$ being given by the equation $\sum t_{i} S_{i} - 1 = 0$ as a function
of the $S_{i}$ ($1 \leq i \leq n - 1$) and the $t_{i}$ ($1 \leq i \leq n$). On the other hand, $k' = k(\eta)$ can be
identified with $k(S_{1}, \cdots, S_{n})$, and the canonical inclusion $k' \to L$ is obtained by sending each $S_{i}$ to
its image in $L$;[^v-5p1-10] that is, $k'$ as a subextension of $L$ is generated by the $S_{i}$ ($1 \leq i \leq n$), or,
what is the same, by the $S_{i}$ ($1 \leq i \leq n - 1$) together with

```text
  S_n = a_0 + a_1 S_1 + ⋯ + a_{n-1} S_{n-1},
```

where $a_{0} = t^{-1}_{n}$ and $a_{i} = - t_{i} t^{-1}_{n}$ for $1 \leq i \leq n - 1$.

Note that the field generated by the $a_{i}$ and that generated by the $t_{i}$ are obviously the same; their common
transcendence degree is nothing else but the dimension of $f(X)$.

*(N.B. It would be appropriate to include this birational description at least as a corollary to (5.2.1).)*

The proof of (5.3.1) is thus reduced to that of:

**Lemma (5.3.1.1) (Zariski).**

<!-- label: V.5.3.1.1 -->

*Let $k$ be a field, $K$ an extension of finite type over $k$, $m$ an integer $\geq 0$, and $a_{i}$ ($0 \leq i \leq m$)
elements of $K$ such that the transcendence degree of $k(a_{0}, \cdots, a_{m})$ over $k$ is $\geq 2$. Let $L = K(S_{1},
\cdots, S_{m})$ and*

<!-- original page 12 -->

*let $k'$ be the subfield*

```text
  k' = k(S_1, …, S_m, a_0 + ∑_{1 ≤ i ≤ m} a_i S_i)
```

*of $L$, the $S_{i}$ being indeterminates. If $K$ is a primary extension of $k$, then $L$ is a primary extension of
$k'$.*[^v-5p1-11]

This lemma, or lemmas that resemble it like a brother, wander almost everywhere in the literature. That is why I leave
it up to you: the choice of the place from which you will copy a proof. I do not feel inspired to find a proof with my
own means.

**Corollary (5.3.2).**

<!-- label: V.5.3.2 -->

*Assume that $f$ is unramified, or that $k$ is of characteristic zero, and that $\dim f(X) \geq 2$. Then if $X$ is
geometrically integral, the same is true of $Y_{\eta}$.*

Indeed, geometrically integral = geometrically irreducible + separable.

**Corollary (5.3.3).**

<!-- label: V.5.3.3 -->

*Assume that $k$ is algebraically closed and that for every irreducible component $X_{i}$ of $X$ we have $\dim f(X_{i})
\geq 2$. Suppose also that $X$ is $\sigma$-connected, where $\sigma$ is the set of closed subsets $Z$ of $X$ such that
$\dim f(Z) = 0$ (i.e. for every such $Z$, $X - Z$ is connected). Under these conditions, $Y_{\eta}$ is geometrically
connected over $k(\eta)$.*

Indeed, by a lemma that ought to appear in §IV.6 together with Hartshorne's theorem,[^v-5p1-12] the hypothesis signifies
that we can join any two irreducible components $X'$ and `X''` of $X$ by a chain of irreducible components $X_{0} = X',
X_{1}, \cdots, X_{n} = X''$ such that two consecutive ones have an intersection not in $\sigma$; consequently the
inverse images $X_{i,\eta}$ are joined by a chain of components which are geometrically connected over $k(\eta)$ by
(5.3.1) and have pairwise non-empty intersection by (5.2.3).

It follows (since $Y_{\eta} = X_{\eta}$ is the union of the $X_{i,\eta}$ as $X_{i}$ runs through the irreducible
components of $X$) that $Y_{\eta}$ is geometrically connected over $k(\eta)$.

**Translator's note to (5.3.1.1).** This lemma should be compared with Zariski's collected papers (MIT Press), vol. 1,
page 174, and vol. 2, page 304; also Zariski-Samuel, vol. 1, page 196, and vol. 2, page 230 of the GTM Springer edition.
See also Jouanolou's *Théorème de Bertini et applications*, Theorem 3.6 and Section 6.

### V.5.4. Variable hyperplane section: "sufficiently general" sections

We return to the general situation of §V.5.1: $S$ an arbitrary prescheme. We also suppose that $X$ is of finite
presentation over $S$.

In general, let us note that if $P(Z, k)$ is a "constructible" property of an algebraic prescheme $Z$ over a field $k$,
then the set of $\xi \in P^{\vee}$ such that $P(Y_{\xi}, k(\xi))$ holds is constructible. Indeed, $Y_{\xi}$ is the fibre
over $\xi$ of $Y \to P^{\vee}$, which is a morphism

<!-- original page 13 -->

of finite presentation, and we apply §IV.9. We have an analogous remark for a property $P(Z, M, k)$, where $Z$ and $k$
are as above and $M$ is a coherent module over $Z$: if $G$ is in addition of finite presentation over $X$, then the set
of $\xi \in P^{\vee}$ such that $P(Y_{\eta}, G_{\eta}, k(\eta))$ holds[^v-5p1-13] is constructible. On the other hand,
in the previous two subsections we have developed, in various cases, criteria for the set $E$ above to contain the
generic point of $P^{\vee}$, $S$ being the spectrum of a field $k$; being constructible, it follows that $E$ contains a
non-empty open set: this is the passage from a conclusion concerning the generic hyperplane section to the analogous
conclusion for "sufficiently general" hyperplane sections.

Let us note in addition that, in the case $S = \operatorname{Spec}(k)$, we also have a converse: in order that the
generic hyperplane section should have the property $P$, it is necessary and sufficient that the $Y_{\xi}$ for $\xi$ in
a suitable neighbourhood of $\eta$ should satisfy it; and it suffices to require this for $\xi$ closed in $P^{\vee}$,
which for $k$ algebraically closed leads to (or reduces to) considering $k$-rational points, i.e. hyperplane sections of
$X$ itself (without a prior extension of the base field).[^v-5p1-14]

This follows, indeed, from the constructibility of $E$ and from the fact that $P^{\vee}$ is a Jacobson scheme.

Let us give as examples some special cases where the previous considerations apply.

**Proposition (5.4.2).**[^v-5p1-15]

<!-- label: V.5.4.2 -->

*Let $G$ be a module of finite presentation over $X$. Let $P$ be one of the following properties for a module $M$ over
an algebraic scheme $Z$ over a field $K$:*

*(i) $coprof(M) \leq n$;*

*(ii) $M$ satisfies $(S_{k})$;*

*(iii) $M$ is Cohen-Macaulay;*

*(iv) $M$ has no embedded prime cycle components;*

*(v) $M$ is separable over $K$.*

*With these notations, if $E$ denotes the set of $\xi \in P^{\vee}$ such that $G_{\xi}$ satisfies the property $P$,
then:*

*(a) $E$ is a constructible subset of $P^{\vee}$.*

*(b) Suppose that $S = \operatorname{Spec}(k)$, $k$ a field, and that $F$ satisfies the property $P$. Suppose also, in
case (v), that $k$ is of characteristic zero, or that $f : X \to P$ is unramified. Then $E$ contains an open dense
subset of $P^{\vee}$.*

*Proof.* (a) follows from the fact that $P$ is a constructible property, as we have seen in §IV.9. As to (b), it follows
from the corresponding results of the previous two subsections.

**Remark.** More generally one could suppose that, with $Z$ the set of points of $X$ where $F$ does not satisfy $P$, the
image $f(Z)$ is finite, i.e. $\dim f(Z) \leq 0$.

<!-- original page 14 -->

**Proposition (5.4.3).**

<!-- label: V.5.4.3 -->

*Let $P$ be one of the following properties (for an algebraic prescheme $Z$ over a field $K$):*

*(i) $Z$ is smooth over $K$;*

*(ii) $Z$ satisfies the geometric property $(R_{k})$ over $K$;*

*(iii) $Z$ is separable over $K$;*

*(iv) $Z$ is geometrically normal over $K$;*

*(v) $Z$ is geometrically integral over $K$;*

*(vi) $Z$ is geometrically irreducible over $K$.*

*Let $E$ be the set of $\xi \in P^{\vee}$ such that $Y_{\xi}$ satisfies $P$. Then:*

*(a) $E$ is a constructible subset of $P^{\vee}$.*

*(b) Suppose $S = \operatorname{Spec}(k)$, $k$ a field, and suppose in cases (i)-(v) that $k$ is of characteristic zero
and that $f : X \to P$ is unramified. Finally, suppose in cases (v) and (vi) that $\dim f(X) \geq 2$. If $X$ satisfies
$P$, then $E$ contains a dense open subset of $P^{\vee}$.*

*Proof.* The proof is identical to that of (5.4.2). Note that in cases (i)-(v) it suffices to assume only (in (b)) that
$f(Z)$ is finite, where $Z$ is the set of points of $X$ where $P$ fails.

**Corollary (5.4.4).**

<!-- label: V.5.4.4 -->

*Consider the property $(C_{m})$: "$\overline{Z}$ cannot be disconnected by a closed subset of dimension $\leq m$",
where $\overline{Z} = Z \otimes_{K} \overline{K}$, $\overline{K}$ the algebraic closure of $K$. Let $E$ be the set of
$\xi \in P^{\vee}$ such that $Y_{\xi}$ over $k(\xi)$ satisfies $(C_{m})$. Then:*

*(a) $E$ is constructible.*

*(b) Suppose $S = \operatorname{Spec}(k)$, $k$ a field, and that for every irreducible component $X_{i}$ of $X$ we have
$\dim f(X_{i}) \geq 2$. Then if $X$ over $k$ satisfies $(C_{m+1})$, then $E$ contains a dense open subset $U$ of
$P^{\vee}$.*

The constructibility is done via "AQT".[^v-5p1-16] This is a fact that one has forgotten in §IV.9 — perhaps it would
still be possible to repair (or fix) it. Part (b) follows in principle from (5.3.3), except that (5.3.3) has been stated
in an excessively special manner and consequently should be generalized (the proof being otherwise essentially
unchanged).

Also, there is an error in the statement of (5.4.4): it is not valid as such if $f$ is quasi-finite. In the general
case, instead of considering the dimension of the closed subsets of $X$, respectively of $Y_{\xi}$, it is sufficient to
consider the dimension of their images in $P$, respectively in $H_{\xi}$. *Let the redactor sort himself
out.*[^v-5p1-17]

<!-- original page 15 -->

### V.5.5. Theorems of Seidenberg type

**(5.5.1).** In the present subsection we give conditions under which the set $E$ defined in §V.5.4 is open. We deal
here with properties $P$ of local nature over $X$, respectively $Y_{\xi}$, such that we can define the set $U$ of $y \in
Y$ for which ($\xi$ being the image of $y$ in $P^{\vee}$) $Y_{\xi}$ satisfies $P$ at the point $y$ (respectively
$G_{\xi}$ satisfies the condition $P$ at $y$). We give first the criteria for $U$ to be open, by using
§IV.12.[^v-5p1-18] As always we have $E = P^{\vee} - h(Y - U)$. It follows that if $U$ is open and $X$ is proper over
$S$ (since $h$ is then proper and a fortiori closed), then $E$ is also open.[^v-5p1-19]

**(5.5.2).** As we have seen in §V.5.1, $Y$ is defined in $X \times_{S} P^{\vee} = X_{P^{\vee}}$ as the "divisor" of a
section $\phi$ of $\mathcal{O}_{X}(1) \otimes_{S} \mathcal{O}_{P^{\vee}}(1)$, which induces for every $\xi \in P^{\vee}$
a section $\phi_{\xi}$ of $\mathcal{O}_{X}(1) \otimes_{k(s)} \mathcal{O}_{P^{\vee}}(1)(\xi)$ (a sheaf, by the way,
isomorphic non-canonically to $\mathcal{O}_{X}(1) \otimes_{k(s)} k(\xi) = \mathcal{O}_{X_{k(s)}}(1)$), such that
$Y_{\xi}$ is nothing else but the "divisor" of this section. (N.B. The divisor of a section $\phi$ of an invertible
module $L$ is defined as the closed subscheme defined by the image ideal of $\phi^{-1} : L^{-1} \to \mathcal{O}$.) If
$F$ is a sheaf of modules over $X$, then its inverse image over $Y$, i.e. the inverse image of $F
\otimes_{\mathcal{O}_{S}} \mathcal{O}_{P^{\vee}} = F_{P^{\vee}}$ over the subscheme $Y$ of $X_{P^{\vee}}$, is nothing
else but the cokernel of the homomorphism

```text
  (φ ⊗ id_{F_{P^∨}})^{-1} : F_{P^∨}(-1, -1) ⟶ F_{P^∨},
```

where the notation `(-1, -1)` explains itself (as M. Artin says[^v-5p1-20]). Also, $G_{\xi}$ is the cokernel of the
analogous homomorphism

$$ F_{k(\xi)}(-1, -1) \longrightarrow F_{k(\xi)}, $$

where $\xi$ is a point of $P^{\vee}$ (with a corresponding interpretation if $\xi$, instead of being a point of
$P^{\vee}$, denotes a point of $P^{\vee}$ with values in an $S'$ over $S$).

In general, if $L$ is an invertible module on some scheme and $\phi$ is a section defining the subprescheme $V(\phi)$,
then for every module $F$ the inverse image of $F$ in $V(\phi)$ can be identified, by the usual abuse of language, with
the cokernel of $id_{F} \otimes \phi : F \otimes L^{-1} \to F$.

We say that $\phi$ is **$F$-regular** if the preceding homomorphism is injective. If we choose locally an isomorphism of
$L$ with $\mathcal{O}_{X}$ — which is possible — so that $\phi$ is identified with a section of $\mathcal{O}_{X}$, this
terminology is compatible with the one already introduced elsewhere.

**Proposition (5.5.3).**

<!-- label: V.5.5.3 -->

*With the previous notation, let $U$ be the set of $x \in X_{P^{\vee}}$ with image $\xi$ in $P^{\vee}$ such that
$\phi_{\xi}$ is $F_{k(\xi)}$-regular at $x$. Then:*

*(a) If $F$ is of finite presentation and flat relative to $S$, then $U$ is open and $G | U$ is flat relative to
$P^{\vee}$.*

*(b) For every $s \in S$, if $\eta$ denotes the generic point of $P^{\vee}_{s}$, then $U$ contains $X_{k(\eta)}$.*

<!-- original page 16 -->

*Proof.*

(a) Since $F_{P^{\vee}}$ is of finite presentation and flat relative to $P^{\vee}$, the conclusion follows from §IV.11.3
(and also from §0_III, in the case of locally noetherian $S$).

(b) We may suppose $S = \operatorname{Spec}(k)$. The associated cycles of $F_{k(\eta)}$ are (by §IV.3) the inverse
images of the associated cycles $Z_{i}$ of $F$. If $f(Z_{i})$ is finite, then by (5.2.3) $Z_{i, k(\eta)} \cap Y =
\emptyset$; in the contrary case, by (5.2.6) (or — better — by reasons of dimension; (5.2.3), already invoked in
(5.2.6), is undoubtedly a better reason), we have $Z_{i, k(\eta)} \cap Y = Z_{i, k(\eta)}$. This proves that $\phi$ does
not vanish on any of the $Z_{i, k(\eta)}$ and therefore proves (b).

**Corollary (5.5.4).**

<!-- label: V.5.5.4 -->

*Let $V$ be the set of $\xi \in P^{\vee}$ such that $\phi_{\xi}$ is $F_{k(\xi)}$-regular. If $F$ is of finite
presentation, then $V$ is constructible and it contains the generic points of the fibres of $P^{\vee}$ over $S$. On the
other hand, if also $X$ is proper over $S$ and $F$ is flat over $S$, then the set $V$ is open.*

**Remark (5.5.5).**

<!-- label: V.5.5.5 -->

*Let $\xi \in P^{\vee}$ over $s \in S$, and suppose that $F_{s}$ is without associated embedded cycles. Then $\xi \in V$
(notation of (5.5.4)) — which means also that every irreducible component of $supp F_{k(\xi)}$ does not lie over
$H_{\xi}$ (and somewhat less evidently, in this criterion we may replace $k(\xi)$ by an arbitrary extension of
$k(\xi)$).*

Let us note that the hypothesis `(S_1)` about $F_{s}$ just made is satisfied notably if $F_{s}$ is Cohen-Macaulay (a
fortiori if $F$ is CM over $S$); also in this case $G_{s}$ is CM (since locally it is deduced from $F_{k(s)}$, which is
such, by dividing by $\phi \cdot F_{k(s)}$ where $\phi$ is $F_{k(s)}$-regular). The same remarks should (and will have
to) be made locally above to characterize the points of $U$ (in place of those of $V$).

Using now §§IV.12.1.1 and IV.12.1.4, we obtain:

**Theorem (5.5.6).**

<!-- label: V.5.5.6 -->

*Assume that $F$ is of finite presentation and flat relative to $S$. Let $P$ be one of the properties (i)-(viii) of
§IV.12.1.1, or (if we assume $F = \mathcal{O}_{X}$) one of the properties (i)-(iv) of §IV.12.1.4.[^v-5p1-21] Let `U_P`
be the set of $x \in X_{P^{\vee}}$ such that, if $\xi$ denotes the image of $x$ in $P^{\vee}$, the property $P$ is
satisfied by $G_{\xi}$ (resp. $Y_{\xi}$) at the point $x$, and such that $\phi_{\xi}$ is $F_{k(\xi)}$-regular at $x$.
Then `U_P` is open and $G | U_{P}$ is flat relative to $S$.*

Indeed, by the very definition we have $U_{P} \subset U$ (notation of (5.5.3) (a)), and we apply §IV.12 to $U \to
P^{\vee}$ and $F_{P^{\vee}} | U$.

**Corollary (5.5.7).**

<!-- label: V.5.5.7 -->

*Suppose that $F$ is of finite presentation and flat relative to $S$, and that `supp F` is proper over $S$ (e.g. $X$
proper over $S$). Let `V_P` be the set of $\xi \in P^{\vee}$ such that $G_{\xi}$*

<!-- original page 17 -->

*(resp. $Y_{\xi}$) satisfies the property $P$ and $\phi_{\xi}$ is $F_{k(\xi)}$-regular. Under these conditions, `V_P` is
open (and is constructible in every case, even without any flatness or properness assumption).*

It seems to me that from the point of view of presentation we cannot leave (5.5.6) as is with a simple reference to the
conditions enumerated in another volume; it requires an explicit list (i), (ii), … of properties which we have in view.
Remark also (in (5.5.1) perhaps) that the case $P =$ geometrically normal (with $S = \operatorname{Spec}(k)$, to be
sure[^v-5p1-22]) is due to Seidenberg.

### V.5.6. Connectedness of an arbitrary hyperplane section

We now combine the already-known criterion for geometric connectedness of the generic hyperplane section (5.3.3) with
Zariski's connectedness theorem in order to obtain a connectedness result for an arbitrary hyperplane section.

**Proposition (5.6.1).**

<!-- label: V.5.6.1 -->

*Suppose $S = \operatorname{Spec}(k)$, $k$ an algebraically closed field, $X$ proper over $k$. Suppose that for every
irreducible component $X_{i}$ of $X$, $f(X_{i})$ should be of dimension $\geq 2$, and finally that $X$ cannot be
disconnected by a closed subset $Z$ of $X$ such that $\dim f(Z) \leq 0$. Under these conditions, for every $\xi \in
P^{\vee}$, $Y_{\xi}$ is geometrically connected.*

*Proof.* Since none of the $f(X_{i})$ is finite, we see that every irreducible component $Y_{i}$ of $Y$ dominates
$P^{\vee}$. On the other hand, $Y \to P^{\vee}$ is proper ($Y$ being proper over $k$, since $Y$ is proper over $X$ and
$X$ is proper over $k$). On the other hand, by (5.3.3), the generic fibre $Y_{\eta}$ of $Y \to P^{\vee}$ is
geometrically connected.

Finally, $P^{\vee}$ is regular and a fortiori geometrically unibranch. It now suffices to apply §IV.15.6.3 (which is a
variant of Zariski's connectedness theorem) to conclude that all the fibres of $Y \to P^{\vee}$ are geometrically
connected.

> *Grothendieck note.* It is not difficult, by a proof of analogous type, to generalize (5.6.1) in the same sense as
> (5.4.4). If you do not want to trouble yourself with this exercise, at least mention it as a remark. Note also that we
> do not discriminate in (5.6.1) with regard to hyperplane sections that have an excessive (extra) dimension. From the
> planning point of view, it might be clearer to group together all the connectedness questions (including (5.3.3) and
> (5.4.4)) in the same subsection.

### V.5.7. Application to the construction of hyperplane sections and multisections of specified type

<!-- original page 18 -->

**(5.7.1).** Let us note that if $S = \operatorname{Spec}(k)$ where $k$ is an infinite field, then every non-empty open
subset of $P^{\vee}$ contains a $k$-rational point; therefore, with the notation of §V.5.4, if $E$ (defined in terms of
a constructible property $P$) contains the generic point $\eta$, it contains a $k$-rational point, and hence there
exists a hyperplane section of $X$ (defined over $k$) having the property $P$. On the other hand, $S$ being again
arbitrary, it is immediate that for every $s \in S$ and for every point $\xi_{0}$ of the fibre $P^{\vee}_{s}$ rational
over $k(s)$, there exists a section $\xi$ of $P^{\vee}$ on an open neighbourhood $U$ of $s$ which passes through
$\xi_{0}$. If $E$ is again defined as in §V.5.4 in terms of a constructible property $P$, and if we have (for example by
§V.5.5) that $E$ is open, then if $\xi_{0} \in E$, the section $\xi$ is a section of $E$ over $U$, at least if we
sufficiently shrink $U$. Therefore we may construct a hyperplane section $Y_{\xi}$ of $X$ over an open neighbourhood $U$
of $s$ such that for every $t \in U$ its fibre $Y_{\xi(t)}$ at $t$ satisfies the property $P$. If we do not have a
priori $\xi_{0}$ but if $k(s)$ is infinite, we may combine the two preceding remarks to obtain a hyperplane section over
an open neighbourhood of $s$ having the preceding property.

Finally, using §V.5.5, we have a criterion allowing us to assert ($X$ resp. $F$ being assumed flat over $S$, which
allows us to apply the cited result) that $Y_{\xi}$ resp. $G_{\xi}$ is also flat over $S$. We may therefore, replacing
$X$ by $Y_{\xi}$, iterate the previous construction; this allows, under certain conditions, to construct "by successive
approximations"[^v-5p1-23] a **multisection** $S'$ of $X$ over an open neighbourhood $U$ of the given point $s$, such
that $S' \to U$ is finite, flat, and with fibres satisfying the property $P$.

If $k(s)$ is finite, we may be forced to do an étale and surjective base change $S'' \to U$ ($U$ an open neighbourhood
of $s$) before being able to apply the preceding constructions. Indeed, under the conditions from the start of §V.5.6,
if $k$ is finite, there does not necessarily exist a rational point over $k$ in the open non-empty set $U$; but there
certainly exists a closed point of $U$, hence a point with values in a finite extension $k'$ (necessarily separable) of
$k$. When $k = k(s)$, we may therefore, after making a suitable finite étale extension `S''` over a neighbourhood $U$ of
$s$, corresponding to the residual extension $k'$ (i.e. such that $S''_{s'} \cong \operatorname{Spec}(k')$), restrict
ourselves to the favourable situation of the unique point $s' \in S''$ over $s$ after the base change $S'' \to S$.

> *Grothendieck note.* I must, however, note a regret regarding (5.4.2) and (5.4.3), which should have been announced in
> a slightly more general form (at least as a remark). If we are given an integer $m$ and we denote by $E$ the set of
> $\xi \in P^{\vee}$ such that $G_{\xi}$, resp. $Y_{\xi}$, satisfies $P$ except over a closed set of dimension $\leq m$
> (i.e. the $P$-singular set $Z$ is of dimension $\leq m$), then:
>
> (a) $E$ is a constructible subset of $P^{\vee}$; and
>
> (b) in the case $S = \operatorname{Spec}(k)$, if $F$, respectively $X$, satisfies $P$ except over a set of dimension
> $\leq m + 1$, then $E$ contains a non-empty open set.

<!-- original page 19 -->

**Proposition (5.7.2).**

<!-- label: V.5.7.2 -->

*Assume that $X$ is proper over $S$ and that $F$ is of finite presentation and flat over $S$. Let $P$ be one of the
properties (i)-(v) of (5.4.2), and let $m$ be an integer. Let $s \in S$, and suppose that the set $Z_{s}$ of points of
$X_{s}$ where $F_{s}$ does not satisfy $P$ is of dimension $\leq m + 1$. Then if also $k(s)$ is infinite, there exists a
neighbourhood $U$ of $s$ in $S$ and a section $\xi$ of $P^{\vee}$ over $U$ having the following properties: for every $x
\in U$, the set of points of $Y_{\xi, x}$ where $G_{\xi(x)}$ does not satisfy $P$ is of dimension $\leq m$, and
$\phi_{\xi(x)}$ is $F_{\xi, x}$-regular. Under these conditions, the module $G_{\xi}$ over $Y_{\xi}$ is flat relative to
$U$. Finally, if $k(s)$ is not assumed infinite, we can again make the previous construction after an étale extension of
the type anticipated in (5.7.1).*

**Proposition (5.7.3).**

<!-- label: V.5.7.3 -->

*The same as (5.7.2), but with no module $F$, assuming instead that $X$ is flat relative to $S$. We refer to properties
(i)-(v) of (5.4.3) in place of those of (5.4.2) (but being careful to keep the reservation that in case (v), for every
$s \in S$ and every irreducible component $Z$ of $X_{s}$, we have $\dim f(Z) \geq 2$).*[^v-5p1-24]

*(Text crossed out in the source.)*

**Proposition (5.7.4).**

<!-- label: V.5.7.4 -->

*Let $g : X \to S$ be a flat proper morphism, let $s \in S$, put $n = \dim X_{s}$, and suppose that the dimension of the
set of points of $X_{s}$ where $X_{s}$ is not separable over $k(s)$ is $< n$ (for example, $X_{s}$ separable). Then
there exists an open neighbourhood $U$ of $s$ and an étale finite surjective morphism $S'' \to U$ such that $X
\times_{S} S''$ admits a section over `S''`. If $k(s)$ is infinite, we may take for `S''` a closed subscheme of
`X_U`.*[^v-5p1-25]

*Proof.* Assume to start with that $k(s)$ is infinite. We proceed by induction on $n$, the case $n = 0$ being trivial:
in that case there exists an open neighbourhood $U$ of $s$ such that $X | U$ itself is étale, finite, and surjective
above $U$, as one sees by immediate cross-references. If $n > 0$, we apply (5.7.3) for the "separable" property, which
allows us to replace $X$ by a "hyperplane section" $Y$ having the same properties up to the fact that $n$ is replaced by
$n - 1$. If $k(s)$ is not assumed infinite, we begin by making an étale base change; the argument goes through.

<!-- original page 20 -->

**Remark (5.7.5).**

<!-- label: V.5.7.5 -->

*In particular, if $X$ is projective and separable over $S$, it admits locally over $S$ étale multisections. But we note
that one can give examples with $X$ proper and smooth (but not projective) over $S$ where the same conclusion fails. Of
course, the projective assumption cannot be weakened in general to an assumption of quasi-projectiveness, as one sees,
for example, by taking $X$ étale and not finite over $S$.*[^v-5p1-26]

### V.5.8. Dimension of the set of exceptional hyperplanes

**(5.8.1).** In the previous subsections, and notably in §§V.5.2 and V.5.3, we have given statements asserting that the
set of $\xi \in P^{\vee}$ such that $Y_{\xi}$ has a certain property $P$ is constructible and that it contains the
generic point $\eta$; or, equivalently, that the set `Z_P` of $\xi \in P^{\vee}$ "exceptional for $P$" is constructible
and rare — i.e. its closure is of codimension $\geq 1$. (N.B. We suppose $S = \operatorname{Spec}(k)$.)

In certain cases we can make this statement more precise by giving a better upper bound on this codimension, which is
important for certain questions. For example, if we see that this codimension is $\geq 2$, it follows that a
"sufficiently general" straight line $D$ of $P^{\vee}$ does not intersect `Z_P`, whence the existence (if $k$ is
infinite) of "linear pencils" of hyperplane sections $Y_{\xi}$ ($\xi$ a geometric point of $D$) all of which have the
property $P$. (See the subsection on pencils of hyperplane sections for examples.[^v-5p1-27])

From the point of view of presentation, since the results of the present subsection make some of the results of the
previous subsections more precise, the question arises whether it is necessary to do this catching-up in a separate
subsection, or to give a more precise version gradually as one moves along. *Let the redactor decide.*[^v-5p1-28]

**(5.8.2).** Let $Z$ be the set of $\xi \in P^{\vee}$ such that $\dim Y_{\xi} > \dim X - 1$, and suppose that for every
irreducible component $X_{i}$ of $X$ we have $\dim f(X_{i}) \geq 2$.[^v-5p1-29] Then $Z$ is of codimension $\geq 2$ in
$P^{\vee}$. This follows from (5.2.1) and (5.2.2) (which imply that every irreducible component of $Y$ dominates
$P^{\vee}$) and from the dimension theory for the morphism $Y \to P^{\vee}$. Starting from this result we may give, as a
corollary, the case where we start with a closed subset $T$ of $X$ and where we consider the dimension of the inverse
images $T_{\xi}$ in the $Y_{\xi}$ ($\xi \in P^{\vee}$); we may even take for $Z$ the set of $\xi \in P^{\vee}$ such that
there exists an irreducible component of $T_{k(\xi)}$ whose trace on $Y_{\xi}$ has excessive dimension. (N.B. We always
assume that for every irreducible component $T_{i}$ of $T$ we have $\dim f(T_{i}) > 0$.)

<!-- original page 21 -->

Finally, the most precise statement in this direction, and one that follows easily from the first formulation (for $X$
irreducible) and from (5.2.7), is the following modified statement: $F$ being coherent over $X$, suppose that for every
prime cycle $T$ associated to $F$ we have $\dim f(T) > 0$. Then the set of $\xi \in P^{\vee}$ such that $\phi_{\xi}$ is
not $F_{k(\xi)}$-regular is (constructible and) of codimension $\geq 2$. (The notation for $\phi_{\xi}$ is that of
§V.5.5.) We can give this as the principal assertion, and announce the previous assertions as corollaries, the proof
being via one of the corollaries.

Note that with the preceding notation, if $\xi \in P^{\vee} - Z$, then for every $y \in Y_{\xi}$ we have $coprof_{y}
G_{k(\xi)} = coprof_{y} G_{\xi}$, and consequently if $coprof F \leq n$, then for $\xi \in P^{\vee} - Z$ we have $coprof
G_{\xi} \leq n$. In particular, if $F$ is Cohen-Macaulay, then for $\xi \in P^{\vee} - Z$, $G_{\xi}$ is Cohen-Macaulay.
Finally, if $F$ is $(S_{k})$, then $G_{\xi}$ is $(S_{k-1})$ for $\xi \in P^{\vee} - Z$ (see §0_IV).

**(5.8.3).** We note that if $F$ is $(S_{k})$, it can happen, for some $\xi \in P^{\vee}$ such that $\phi_{\xi}$ is
$F_{k(\xi)}$-regular, that $G_{\xi}$ has a component of codimension $\geq 2$ failing $(S_{k})$,[^v-5p1-30] even if $F =
\mathcal{O}_{X}$, $k = 1$, $X$ being geometrically integral of dimension two (resp. $k = 2$, $X$ being geometrically
integral and geometrically normal of dimension three). It is enough to start from a projective integral surface

$$ X \subset \mathbb{P}^{r} $$

over $k$ algebraically closed having a point $x$ where $X$ is not Cohen-Macaulay; then for every hyperplane passing
through $x$, the corresponding hyperplane section $Y_{\xi}$ admits $x$ as an associated embedded cycle. (Respectively,
we start from a normal — hence `(S_2)` — integral variety $X \subset \mathbb{P}^{r}$ of dimension three having a point
$x \in X$ where $X$ is not Cohen-Macaulay; then the $Y_{\xi}$ passing through $x$ are not CM, i.e. they fail `(S_2)` at
$x$.)

In these examples the set of "exceptional" $\xi$ for the property $(S_{k})$ contains the hyperplane of $P^{\vee}$
defined by $x \in P$ and is of codimension one (and not of codimension $\geq 2$). Compare (5.8.5) below for a general
precise result along these lines.

**Proposition (5.8.4).**

<!-- label: V.5.8.4 -->

*Let $T$ be a closed subset of $X$, and suppose that $codim(T, X) \geq k$. Then for every $\xi \in P^{\vee}$ we have
$codim(T_{\xi}, Y_{\xi}) \geq k - 1$. Let $Z$ be the set of $\xi \in P^{\vee}$ such that $codim(T_{\xi}, Y_{\xi}) = k -
1$ (i.e. $codim(T_{\xi}, Y_{\xi}) < k$). Then $Z$ is a constructible, nowhere dense subset of $P^{\vee}$, i.e.
$\overline{Z}$ is of codimension $\geq 1$ in $P^{\vee}$.*

*In order for it to be of codimension $\geq 2$, it is necessary and sufficient that for every irreducible component
$T_{i}$ of $T$ of codimension equal to $k$ and such that $\dim f(T_{i}) = 0$, there should exist an irreducible
component $X_{j}$*

<!-- original page 22 -->

*of $X$ such that $codim(T_{i}, X_{j}) = k$ and $\dim f(X_{j}) > 0$ — i.e., if $f$ is quasi-finite and $k > 0$, that $T$
does not have isolated points such that $\dim_{x} X = k$.*

The first assertion follows immediately from the following lemma (5.8.4.1) (a), which is a remorseful afterthought to
§V.5.5.

**Lemma (5.8.4.1).**

<!-- label: V.5.8.4.1 -->

*Let $X$ be a locally noetherian prescheme, let $L$ be an invertible module over $X$, $\phi$ a section of $L$, $Y =
V(\phi)$, and $T$ a closed subset of $X$. Assume that $codim(Y, X) \geq k$. Then:*

*(a) $codim(T \cap Y, Y) \geq k - 1$.*

*(b) In order to have $codim(T \cap Y, Y) = k - 1$ (i.e. $codim(T \cap Y, Y) < k$), it is necessary and sufficient that
there should exist an irreducible component $T_{i}$ of $T$ contained in $Y$ such that $codim(T_{i}, X) = k$ and such
that for every irreducible component $X_{j}$ of $X$ containing $T_{i}$ with*

```text
  dim 𝒪_{X_j, T_i} = dim 𝒪_{X, T_i}  ( = k),
```

*we have $X_{j} \nsubset Y$.*

The verification of this lemma is immediate, given the general facts in §0_IV (Chapter IV) about dimension.

With the assumptions of (5.8.4), and by (5.8.4.1) (b), we see which are the exceptional hyperplanes $H_{\xi}$. If we
exclude the set `Z_0` of $\xi \in P^{\vee}$ such that there is an irreducible component $R$ of $T$ or of $X$ with $\dim
f(R) > 0$ and such that $R_{\xi}$ is of "dimension too large" (a set which is of codimension $\geq 2$ and in what
follows does not count), the exceptional $H_{\xi}$ are those for which there exists a $T_{i}$ with $codim(T_{i}, X) = k$
and $\dim f(T_{i}) = 0$, $f(T_{i}) \subset H_{\xi}$, and such that for every irreducible component $X_{j} \supset T_{i}$
of $X$ with $codim(T_{i}, X_{j}) = k$, we have $f(X_{j}) \nsubset H_{\xi}$. For a given $T_{i}$ with $codim(T_{i}, X) =
k$, if there exists an $X_{j}$ with $codim(T_{i}, X_{j}) = k$ and such that $\dim f(X_{j}) = 0$, then we will have
$f(X_{j}) = f(T_{i}) \subset H_{\xi}$, and consequently $\xi$ would not be exceptional relative to the $T_{i}$. If, on
the other hand, for every $X_{j} \supset T_{i}$ such that $codim(T_{i}, X_{j}) = k$ we have $\dim f(X_{j}) > 0$, then
for $\xi \in P^{\vee} - Z_{0}$, $\xi$ is exceptional relative to $T_{i}$ if and only if $f(T_{i}) \subset H_{\xi}$; the
set of such $\xi$ is (the trace on $P^{\vee} - Z_{0}$ of) a hyperplane of $P^{\vee}$. This proves (5.8.4), and also
proves the more precise result that the exceptional set is the union of a set of codimension $\geq 2$ and of a union of
hyperplanes determined in the evident way by the above proof.

<!-- original page 23 -->

> *Grothendieck note.* I am afraid that the writeup is quite floppy (or perhaps sloppy)[^v-5p1-31] since I have reasoned
> geometrically all the time without saying so, by taking points over an algebraically closed field. Of course, the
> condition announced in (5.8.4) is indeed geometric, so that we may suppose $k$ algebraically closed and argue for
> $k$-rational points.

Using (5.8.4), (5.7.4), and the end of (5.8.2), we obtain:

**Corollary (5.8.5).**

<!-- label: V.5.8.5 -->

*Suppose that for all associated prime cycles $R$ we have at most simply [some condition][^v-5p1-32] and that $F$
satisfies $(S_{k})$. In order that the (constructible) set of points of $P^{\vee}$ such that $\phi_{\xi}$ is
$F_{k(\xi)}$-regular and $G_{\xi}$ is $(S_{k})$ should have a complement of codimension at least two, it is necessary
and sufficient that the following hold: for every integer $n \geq 0$, denote by $Z_{n}$ the set of $x \in T = supp F$
such that* $coprof_{x} F \geq n$;[^v-5p1-33] *then for every irreducible component $Z_{n,i}$ of $Z_{n}$ with
$codim(Z_{n,i}, T) = n + k + 1$ and $\dim f(Z_{n,i}) = 0$, there exists an irreducible component $T_{j}$ of $T$
containing $Z_{n,i}$ such that $codim(Z_{n,i}, T_{j}) = n + k + 1$ and $\dim f(T_{j}) = 0$.*

When $f$ is quasi-finite, then for every closed subset $R$ of $X$,[^v-5p1-34] we have $\dim f(R) = \dim R$, so that the
criterion takes the following form: *there does not exist an isolated point $z$ in any one of the $Z_{n}$ such that
$\dim_{z} T (= \dim F_{z})$ is equal to $n + k + 1$*.

When $F$ is equidimensional of dimension $d$, this condition is vacuous if $d \leq k$ (and indeed we knew this, because
in this case the hypothesis $(S_{k})$ on $F$ is nothing else but the Cohen-Macaulay hypothesis), and if $d \geq k + 1$
it means that the set $Z_{d - (k+1)}$ of points of $T$ where the codepth of $F$ is $> d - (k + 1)$, i.e. the true depth
of $F$ is $\geq k + 1$ (even though, a priori, we only have true depth of $F$ $\geq k$ as a consequence of property
$(S_{k})$ and $k \leq d$). If we no longer assume that $F$ is equidimensional, the desired condition may be expressed in
the following simple way:

**(5.8.6).** *For every closed point $x \in supp F$ such that $\dim F_{x} \geq k + 1$, we have $prof F_{x} \geq k + 1$.*

The sufficiency is seen immediately by putting $Z = {x}$. The necessity is seen by noticing that for every $\xi$ such
that $\phi_{\xi}$ is $F_{k(\xi)}$-regular and $x \in Y_{\xi}$, we have

```text
  dim G_{ξ, x} = dim F_x − 1,   prof G_{ξ, x} = prof F_x − 1,
```

so that $x$ fails by default the above condition: we have $prof G_{\xi, x} \geq k$ but $\dim G_{\xi, x} \geq k$, which
shows that $G_{\xi}$ does not satisfy condition $(S_{k})$ at $x$; but the set

<!-- original page 24 -->

of $\xi$ such that $x \in Y_{\xi}$ is of codimension one. (N.B. I implicitly assumed that $k$ is algebraically closed,
the case to which we reduce immediately.) The preceding general criterion should be evident in the case of (5.8.6).

We now study the points $y$ of $Y$ that are not smooth for $Y_{\xi}$ relative to $k(\xi)$. We restrict ourselves to the
case where $f : X \to P$ is unramified (practically, it will be an immersion) and where $X \to S$ is smooth. We do not
necessarily assume that $S$ is the spectrum of a field.

Since $f$ is unramified, the canonical homomorphism $f^{*}(\Omega^{1}_{P/S}) \to \Omega^{1}_{X/S}$ is surjective and its
kernel is a locally free module over $X$, which we denote $\nu^{\vee}_{X/P}$; when $f$ is an immersion, this is nothing
else but the conormal module $J/J^{2}$ defined by the ideal $J$ of $X$ in $P$, and we call it in every case the
**conormal module**. Thus we have the exact sequence

```text
  (a)        0 ⟶ ν^∨_{X/P} ⟶ f^*(Ω^1_{P/S}) ⟶ Ω^1_{X/S} ⟶ 0.
```

Let us observe that we also have over $P$ an exact canonical sequence (which should appear as an example in §IV.16, for
example)

```text
  (b)        0 ⟶ Ω^1_{P/S}(1) ⟶ E_P ⟶ 𝒪_P(1) ⟶ 0
```

— i.e. $\Omega^{1}_{P/S}(1)$ is canonically isomorphic to the kernel of the canonical homomorphism $E_{P}(-1) \to
\mathcal{O}_{P}$ deduced from $E_{P} \to \mathcal{O}_{P}(1)$. Applying $f^{*}$:

```text
  (b₁)       0 ⟶ f^*(Ω^1_{P/S})(1) ⟶ E_X ⟶ 𝒪_X(1) ⟶ 0,
```

which gives an explicit description of $f^{*}(\Omega^{1}_{P/S})(1)$ over $X$ and allows therefore to identify
$\nu^{\vee}_{X/P}(1)$ with a submodule locally a direct factor of `E_X` — or, dually, $\nu_{X/P}(-1)$ is canonically
isomorphic to a quotient module of $E^{\vee}_{X}$. Consequently $\mathbb{P}(\nu_{X/P}(-1)) = \mathbb{P}(\nu_{X/P})$ can
be canonically embedded in $\mathbb{P}(E^{\vee}_{X}) = X \times_{S} P^{\vee} = X_{P^{\vee}}$ as a projective
subfibration over $X$, hence as a closed subscheme. The latter is necessarily contained in $Y$ (from the fact that
$\Omega^{1}_{X/P}(1)$ is contained in the kernel of $E_{X} \to \mathcal{O}_{X}(1)$).

The underlying set of this prescheme is nothing else but the set of points of $Y = V(\phi)$ which are singular zeros (in
the sense of §V.1, formerly §16)[^v-5p1-35] of the section $\phi$ of $\mathcal{O}_{X \times_{S} P^{\vee}}(1, 1)$
relative to the base $P^{\vee}$; i.e., its points with values in a field $k$ over $P^{\vee}$ are the points $x$ of
$Y_{k} \subset X_{k}$ such that $\phi_{k}$ vanishes to order at least two at $x$, i.e. such that $Y_{k}$ is not smooth
of relative dimension $r - 1$ over $k$ at $x$. The announced characterization of singular zeros as the elements of a
smooth subscheme $\mathbb{P}(\nu_{X/P})$ of $X_{P^{\vee}}$ gives immediately the following statement, which deserves to
appear as a preliminary proposition:

<!-- original page 25 -->

*if $S = \operatorname{Spec}(k)$ and if $H$ is a hyperplane of $P$, then $Y = X \times_{P} H$ is smooth over $k$ of
relative dimension $d - 1$ at the point $x \in Y(k)$ (i.e. $x$ is a non-singular zero, i.e. geometrically non-singular,
of the section $\phi$ of $\mathcal{O}_{X}(1)$ defined by $H$) if and only if $H$ does not contain the image under $f$ of
the tangent space to $X$ at $x$ (relative to $k$); equivalently (if $f : X \to P$ is an immersion which allows us to
identify $X$ to a subscheme of $P$), if and only if $H$ is not tangent to $X$ at $x$.* This follows trivially from the
Jacobian criterion of smoothness, or from the definition of a singular zero, once we make precise the sense of the
statement — that is, the way in which a vector subspace of the tangent space to $P$ at a point $a = f(x)$ defines a
linear subspace of $P$ (in such a way that it makes sense to say that $H$ does not contain the said vector subspace). Of
course, this comes from the exact sequence (b) above, which allows one to define a one-to-one correspondence between the
set of factor subspaces of the tangent space at $a$ and the set of linear subspaces of $P$ containing $a$. This
correspondence reduces to associating to a linear subvariety passing through $a$ its tangent space at $a$, considered as
a subspace of the tangent space to $P$ at $a$.

Such "*sorites*" grouped together with various *sorites* about linear subvarieties and Grassmannians ought to be given
in one or two preliminary subsections or paragraphs, of course over an arbitrary base. In fact we can do better, knowing
that the prescheme $Y^{sing}$ of singular zeros of $\phi$ relative to $P^{\vee}$, defined in §V.1, is nothing else but
$\mathbb{P}(\nu_{X/P})$; and since the latter is smooth over $S$ of relative dimension $d + (r - d - 1) = r - 1$ ($r$
being the relative dimension of $P^{\vee}$ over $S$), we are under the favourable conditions studied in §V.1.[^v-5p1-36]
In order to verify them, let us notice that by definition $Y^{sing}$ is nothing else but the subprescheme of $Y$ of
zeros of the section $\Psi = (d\phi) |_{Y}$ of

```text
  Ω^1_{X_{P^∨} / P^∨}(1, 1) ⊗ 𝒪_Y = Ω^1_{X/S} ⊗ 𝒪_Y(1, 1).
```

We shall give another interpretation of this section, from which the conclusion follows immediately. To do this,
consider the following diagram of exact sequences over $X_{P^{\vee}}$, or more generally over any prescheme $Z$ over
$X_{P^{\vee}}$:

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

[^v-5p1-37] — where the first column is deduced from (a) by tensoring with $\mathcal{O}_{Z}(1, 0)$, the row is deduced
from (b) by tensoring with $\mathcal{O}_{Z}$, and the second column is deduced from the analogous sequence $(b^{\vee})$
relative to $P^{\vee}$ (obtained by replacing $E$ by $E^{\vee}$) by transposition and tensoring with $\mathcal{O}_{Z}$.
From the very definition of $Y$, $Z$ is over $Y$ if and only if the composed morphism $\alpha$ in the diagram is zero,
i.e. if we can find a factorization $\beta : \mathcal{O}_{Z}(0, -1) \to \Omega^{1}_{P/S} \otimes \mathcal{O}_{Z}(1, 0)$.
If that is the case, we can consider its composition with $\Omega^{1}_{P/S} \otimes \mathcal{O}_{Z}(1, 0) \to
\Omega^{1}_{X/Y} \otimes \mathcal{O}_{Z}(1, 1)$. *I say that this is precisely the section $\psi$*[^v-5p1-38] which we
have introduced above (the verification ought to be essentially mechanical). It is zero if and only if $Z$ lies over
$V(\psi)$ (by the very definition of $V(\psi)$); but this means also that $\beta$ factors through $\nu^{\vee}_{X/P}
\otimes \mathcal{O}_{Z}(1, 0)$, i.e. that the submodule $\mathcal{O}_{Z}(0, -1)$ of $E \otimes \mathcal{O}_{Z}$ is
contained in the submodule $\nu^{\vee}_{X/P} \otimes \mathcal{O}_{Z}(1, 0)$, which evidently signifies also that $Z$ is
over the subprescheme $\mathbb{P}(\nu_{X/P}(1))$ of $\mathbb{P}(E^{\vee}_{X})$, achieving the proof we have announced.

Just before this erudite exercise in syntax (for which I have already had to sweat quite a bit), we could remark that
from every set-theoretic point of view $Y^{sing}$ is of dimension $r - 1$ if $S = \operatorname{Spec}(k)$, whereas
$P^{\vee}$ is of dimension $r$, so that the image of $Y^{sing}$ in $P^{\vee}$ is of codimension $\geq 1$. This gives
again (5.2.12) (it is well to note that the argument is not essentially distinct from the one used in (5.2.12)). We note
that most often this set is effectively of codimension one (compare below).

<!-- original page 27 -->

Consequently we cannot in general find "linear pencils" of hyperplane sections all of which are smooth. However, we
shall see that we can often manage to find pencils formed by hyperplane sections not having any supersingular point, due
to the fact that in the most common cases the image of $Y^{supsing}$ in $P^{\vee}$ is of codimension two.

We first recall the essential points, of differential nature, of the situation studied here.

**Theorem (5.8.7).**

<!-- label: V.5.8.7 -->

*(a) The subprescheme $Y^{sing}$ (defined in §V.1) in the present situation is nothing else but $\mathbb{P}(\nu_{X/P})$,
considered as a subscheme of $Y$ as explained above.*

*(b) The underlying set of the prescheme $Y^{supsing}$ (cf. §V.1) is nothing else but the set of ramification points of
the morphism of smooth preschemes over $S$ of relative dimensions $r - 1$ and $r$, namely*

$$ Y^{sing} = \mathbb{P}(\nu_{X/P}) \longrightarrow P^{\vee}, $$

*i.e., in order for this latter morphism to be unramified at the point $y$ (see the definition), it is necessary and
sufficient that $y$ should be geometrically an ordinary singular point for $\phi_{\xi}$ ($\xi$ being the point of
$P^{\vee}$ that is the image of $y$).*

*(c) Suppose $S = \operatorname{Spec}(k)$ and that $y \in Y^{sing} = \mathbb{P}(\nu_{X/P})$ is a $k$-rational point. Let
$x \in X(k)$ and $\xi \in P^{\vee}(k)$ be its projections, and consider the linear subvariety $H'$ of $P^{\vee}$ "image"
of the tangent map of the closure $T$ of $Y^{sing}$ in $P^{\vee}$, given the induced reduced structure. Consider the
induced morphism $g : Y^{sing} \to T$ (a dominant morphism of integral preschemes). The conditions (i), (ii), and their
variants are equivalent:*

*(i) The morphism $g$ is generically étale (i.e. étale at at least one point, or equivalently, étale = unramified at the
generic point of $Y^{sing}$).*

*(i bis) The field extension $L/K$ defined by $g$ is finite and separable.*

*(i ter) The morphism $g$ is birational, i.e. the extension $L/K$ is the trivial extension.*

*(ii) $Y^{sing} \neq Y^{supsing}$ (set-theoretically).*

*(ii bis) There exists an $x \in X(k)$ and a tangent hyperplane $H$ to $X_{k}$ at $x$ which is not osculating at $x$ —
by which we understand precisely that $x$ is not supersingular for the section of $\mathcal{O}_{X_{k}}(1)$ that defines
$H$.*

*These conditions imply that $Y^{supsing} \neq Y^{sing}$ and $\dim Y^{supsing} \leq r - 2$, so that the image of
$Y^{supsing}$ in $P^{\vee}$ has codimension $\geq 2$; and they imply also*

*(iii) $\dim T = r - 1$, i.e. $T$ is of codimension one in $P^{\vee}$.*

<!-- original page 28 -->

*Proof.* The equivalence of (i) and (i bis) is trivial; its equivalence with (ii) is a trivial consequence of (5.8.7)
(b); finally, the equivalence of (ii) and (ii bis) is practically the definition of $Y^{supsing}$. Evidently (i ter) ⟹
(i). It remains to prove that (i) ⟹ (i ter). We may evidently suppose that $K$ is algebraically closed and we are
reduced to proving (taking into account the hypothesis (i)) that there exists an open set $U \neq \emptyset$ such that
$\xi \in U(K)$ implies that there exists exactly one point of $Y^{sing}(K)$ over $\xi$. This will follow from the next
corollary, which says more.

**Corollary (5.8.9).**[^v-5p1-39]

<!-- label: V.5.8.9 -->

*Suppose condition (i) of (5.8.7) is satisfied, and let $U$ be the open subset of $T$ of points where $T$ is smooth over
$k$. Then $U \neq \emptyset$, $Y^{sing} |_{U} \to U$ is an open immersion (a fortiori $Y^{sing} |_{U}$ does not contain
the points of $Y^{supsing}$). If $X$ is proper over $K$, then $g : Y^{sing} \to T$ is surjective; hence $Y^{sing} |_{U}
\to U$ is proper over $K$, so that $g : Y^{sing} \to T$ is surjective; therefore $Y^{sing} |_{U} \to U$ is an
isomorphism, and $U$ is the largest open subset of $T$ having the latter property.*

First of all, since $g$ is dominating and generically étale, it is generically étale, so we can find at least one
non-empty open subset $V$ of $T$ such that $Y^{sing} |_{V} \to V$ is étale and surjective; this implies that $V$ is
smooth over $K$. If then $\xi \in V(K)$ and if $y$ is a point of $Y^{sing}(k)$ over $\xi$, then with the notation of
(5.8.7) (c), the space $H'$ is nothing else but the tangent space to $T$ at $\xi$, and as we observed here, this implies
that the point $x$ of $X(k)$, the projection of $y$, is determined as the orthogonal point to $H'$. It is thus uniquely
determined; consequently, since $Y^{sing} \subset X \times P^{\vee}$, the point $y$ is uniquely determined.

This proves already that $g$ is birational (being generically étale and generically radical). On the other hand, the
morphism $\psi$ (whose definition in this form is evident), which associates to every $\xi \in U(K)'$ the unique point
$x = \psi(\xi) \in P$ orthogonal to the tangent space to $U$ at $\xi$, coincides over $V$ with the composition $V \to
Y^{sing} |_{V} \to X$, where the second arrow is the projection. Therefore, setting $h = (\psi, id) : U \to P \times T$,
and $g_{1} = g | g^{-1}(U) : g^{-1}(U) \to U$, the composition $h \circ g_{1} : g^{-1}(U) \to P \times T$ is nothing
else but the canonical

<!-- original page 29 -->

inclusion, this being so on its restriction to $g^{-1}(V) \to V$. It follows that $h$ factors through the
scheme-theoretic closure $\overline{Y^{sing}}$ of $Y^{sing}$ in $P \times T$; thus the inverse image of $Y^{sing}$
(which is open in the above closure) by $h$ is an open subset of $U$ — call it $U'$. Because of $h \circ g_{1} =$
inclusion, we see immediately that $g_{1}$ induces an isomorphism $g^{-1}(U') \xrightarrow{\sim} U'$. Since $Y^{sing}$
is smooth, it follows that $U'$ is smooth, hence $U' \subset U$. This proves (5.8.9).

The final assertions of (5.8.7) — $Y^{supsing} = \emptyset$ or $\dim Y^{supsing} = r - 2$, and $\dim T = r - 1$ — are
trivial: the first follows from the fact that $Y^{sing}$ is irreducible of dimension $r$ and from the fact that
$Y^{supsing}$ is defined inside $Y^{sing}$ by the vanishing of a section $D$ of an invertible module; the second from
the fact that, $L$ being finite over $K$, we have $\deg.tr_{k} L = \deg.tr_{k} K$, i.e. `dim T = dim Y^{sing} = r − 1`.

**Remark (5.8.10).**

<!-- label: V.5.8.10 -->

*As we remarked in (5.8.9), with the notation of the corollary, we have $g^{-1}(U) \subset Y^{sing} - Y^{supsing}$. But
we note that even if $X$ is closed in $P$, this inclusion is not necessarily an equality. In other words (noting that
$g^{-1}(U)$ is nothing else but the set of points where $g$ is étale), $Y^{sing} - Y^{supsing}$ is the set of points
where $g$ is unramified but not étale (which implies in addition that $g(y)$ is a point that is not geometrically
normal, and even not geometrically unibranch, of $T$). In geometric terms this corresponds to the following phenomenon:
we may have a tangent non-osculating hyperplane for $X$ at a point $x \in X(k)$ such that there exists another point
$x_{1} \in X(k)$ at which the same hyperplane is tangent to $X$ at $x_{1}$. There are obvious examples with $P$ of
dimension two, $X$ a non-singular curve of degree $\geq 4$, in any characteristic. (Note here: the "double tangents" of
$X$ correspond to the double points of the "dual curve".)*

**Corollary (5.8.11).**

<!-- label: V.5.8.11 -->

*Suppose that $k$ has characteristic zero. Then:*

*(a) The image of $Y^{supsing}$ in $P^{\vee}$ is of codimension $\geq 2$.*

*(b) Condition (iii) of (5.8.7) is equivalent to the negation of the other conditions; that is, the assumption $Y^{sing}
= Y^{supsing}$ means also that the image of $Y^{sing}$ in $P^{\vee}$ is of codimension $\geq 2$.*

Evidently, (b) implies (a), taking (5.8.7) into account. But by dimension theory, (iii) means that $L/K$ is a finite
extension (we could put it in the form (iii bis) in (5.8.7)), and in characteristic zero $L$ is always separable over
$K$, hence the condition (i bis) of (5.8.7).

<!-- original page 30 -->

**Remark (5.8.12).**

<!-- label: V.5.8.12 -->

*Geometrically, the assertion (a) means essentially that for a sufficiently general linear pencil of hyperplane
sections, every member of the pencil is smooth or has, as geometric singular points, ordinary double points. (In fact,
as one sees immediately, the statement (a) can be made a little more precise: there is at most one such singular
geometric point.) The assertion (b) means essentially that if $Y^{sing} = Y^{supsing}$ — a condition that can be
expressed analytically by the vanishing of a certain section $D$ of an invertible module $\omega^{\otimes 2}_{X/k}
\otimes \mathcal{O}_{Y^{sing}}(1, 1)$ over $Y^{sing}$ — then, for a sufficiently general linear pencil of hyperplane
sections, all the members of the pencil are smooth. This second situation (whether or not we are in characteristic zero)
should entirely be considered as exceptional.*

> *Grothendieck note.* In the classical language[^v-5p1-40] this is expressed, if there is no error, by saying that $X$
> is **ruled** for the projective immersion considered, and if we so please, we have here all that we need due to
> (5.8.5) and its corollaries to make explicit and justify such a terminology — in case you feel inspired to make a
> connection with classical terminology.[^v-5p1-41] For example, if $\dim X = 1$, this implies that $X$ is a straight
> line, so that any $x \in X(k)$ is contained in $T$.[^v-5p1-42]
>
> *(b) If the characteristic is $p > 0$, we should normally give examples (with $\dim P = 2$, $X$ a non-singular
> algebraic curve) where the conditions of (5.8.6) are not satisfied, i.e. $Y^{sing} = Y^{supsing}$ and where
> nevertheless $\dim T = r - 1$, i.e. examples where $L/K$ is a finite inseparable extension. I am too lazy to construct
> the examples, but I do not doubt that such examples exist.*[^v-5p1-43]

In (a), make a footnote to the following subsection, where we prove that if the exceptional "ruled" case arises, then by
a trivial modification of the projective immersion we find ourselves again in the "general" situation of (5.8.7).

The part of the present subsection from (5.8.6) onwards could without a doubt be made into a separate subsection of
differential character; whereas the beginning of our subsection, together with what follows, should be merged into a
subsection on the dimension of exceptional hyperplanes (we use only the fact that $Y^{sing}$ has dimension $r - 1$).

**Proposition (5.8.13).**

<!-- label: V.5.8.13 -->

*We always assume that $f : X \to P$ is unramified and that $X$ has no isolated points. Assume that $X$ satisfies
$(R_{k})$ geometrically. Let $Z_{k}$ be the part of $P^{\vee}$ complementary to the set of $\xi \in P^{\vee}$ such that
$\phi_{\xi}$ is $F_{k(\xi)}$-regular and $Y_{\xi}$ satisfies the geometric condition $(R_{k})$. Then:*

<!-- original page 31 -->

*(a) In order for $Z_{k-1}$ to be of codimension $\geq 2$ in $P^{\vee}$, it suffices that every irreducible component
$X'_{i}$ of $X'$ of dimension $\leq k$ should be ruled for $f$.*

*(b) In order to have $Z_{k}$ of codimension $\geq 2$ in $P^{\vee}$, it suffices that every irreducible component
$X_{i}$ of $X$ of dimension $\leq k - 1$[^v-5p1-44] should be made up of smooth points of $X$ and should be ruled.*

Indeed, for every $\xi$ geometrically singular, the singular set of $Y_{\xi}$ (N.B.: we restrict ourselves to $\xi$ such
that $\phi_{\xi}$ is $F_{k(\xi)}$-regular, which is harmless because of (5.8.2)) is the union of $sing(Y'_{\xi})$ and of
the inverse image $T_{\xi}$ of $T$ in $Y_{\xi}$, so that the codimension of this singular set in $Y_{\xi}$ is equal to
the infimum of $codim(sing(Y'_{\xi}), Y'_{\xi})$ and of $codim(T_{\xi}, Y_{\xi})$. Let us restrict ourselves to $\xi$
such that $sing(Y'_{\xi})$ is finite (which is harmless: this leads to placing ourselves in the complement of a set of
codimension $\geq 2$). The singular geometric points of $Y'_{\xi}$ are therefore isolated. The conclusion follows easily
from this and from (5.8.4).

Combining (5.8.13), (5.8.5), and (5.8.6), we find in the usual manner:

**Corollary (5.8.14).**

<!-- label: V.5.8.14 -->

*Suppose that $f : X \to P$ is unramified and that $X$ has no isolated points.[^v-5p1-45]*

*(a) Suppose $X$ is separable over $k$. In order that the set of $\xi \in P^{\vee}$ such that $\phi_{\xi}$ is
$F_{k(\xi)}$-regular and $Y_{\xi}$ is separable, should have a complement of codimension at least two, it is necessary
and sufficient that every irreducible component $X_{i}$ of $X$ of dimension one should be formed from smooth points of
$X$ and should be ruled relative to $f$, and that for every closed point $x$ of $X$ such that $\dim_{x} X \geq 2$ we
have $prof_{x} X \geq 2$ (conditions that are automatically satisfied if $X$ is geometrically normal and if all of its
irreducible components are of dimension $\geq 2$).*

*(b) Suppose that $X$ is geometrically normal. In order that the set of $\xi \in P^{\vee}$ such that $\phi_{\xi}$ is
$F_{k(\xi)}$-regular and $Y_{\xi}$ is geometrically normal should have a complement of codimension at least two, it is
necessary and sufficient that every irreducible component $X_{i}$ of $X$ of dimension $\leq 2$ should be formed of
smooth points of $X$ and should be ruled relative to $f$, and that in addition for every closed point $x$ of $X$ such
that $\dim_{x} X \geq 3$ we have $prof_{x} X \geq 3$.*

**Remark (5.8.15).**

<!-- label: V.5.8.15 -->

*In (5.8.6), (5.8.13), and (5.8.14) we make for $X$ the hypothesis $(S_{k})$ (respectively $(R_{k})$, respectively
separable, respectively geometrically normal) that we wish to recover as a conclusion for the hyperplane sections,
except perhaps for $\xi$ in an exceptional set of codimension at least two.*

<!-- original page 32 -->

This does not restrict the generality; to tell the truth, it would have been better to get rid of this preliminary
hypothesis, since we see immediately with the help of results of §IV.3.4 and §IV.5.12 that if $X$ does not satisfy the
hypothesis in question, then (by §V.5.5) if there exists a closed point $x$ where the hypothesis fails, then for every
$\xi$ such that $\phi_{\xi}$ is $F_{k(\xi)}$-regular (a condition that only eliminates a set of codimension
one)[^v-5p1-46] and such that $x \in Y_{\xi}$ (a condition that describes a set of exact codimension one), $Y_{\xi}$
does not satisfy the said hypothesis at $x$; the exceptional set $Z \subset P^{\vee}$ is of codimension one and not two.
(I may have somewhat exaggerated the case $(R_{k})$ where we still need some condition: `(S_1)` and perhaps
equidimensionality.)

> *Grothendieck note (regret).* In (5.8.13) and (5.8.14) it suffices to suppose that $f : X \to P$ is unramified at the
> smooth points of $X$; for the sufficiency part it suffices only that they should be unramified over an open subset
> $X'$ of $X$ whose complement has codimension $\geq k + 1$.

**Proposition (5.8.16).**

<!-- label: V.5.8.16 -->

*Suppose $f : X \to P$ unramified on an open subset complementary to a set of codimension at least two, $X$
geometrically normal and of depth at least three at its closed points, and finally $X$ geometrically integral and proper
over $k$. Then the set of $\xi \in P^{\vee}$ such that $Y_{\xi}$ is geometrically normal and geometrically integral of
dimension equal to $\dim X - 1$ is constructible and has a complement of codimension at least two.*

Indeed, by (5.8.14) (b), such is the case for the property "$Y_{\xi}$ is geometrically normal of dimension $\dim X - 1$"
(the dimensional property expressing that $\phi_{\xi}$ is $F_{k(\xi)}$-regular). Therefore, by (5.6.1), all the
$Y_{\xi}$ are geometrically connected. Since $Y_{\xi}$ is geometrically normal, it is geometrically integral if and only
if it is geometrically connected, which gives the proof.

**Remarks (5.8.17).**

<!-- label: V.5.8.17 -->

*(a) The hypothesis of (5.8.16) implies that $\dim X \geq 3$. It is possible that, as soon as $X$ is geometrically
irreducible and $\dim f(X) \geq 3$ (without the hypothesis of normality and non-ramification), the set of $\xi$ such
that $Y_{\xi}$ is geometrically irreducible has a complement of codimension at least two. We can prove in every case
that it does not contain a hyperplane (see below).*

*(b) The conclusion of (5.8.16) is false if we leave out the assumption that $prof_{x} X \geq 3$ for $x$ closed. For
example, it is false for a non-singular quadric $X$ in $\mathbb{P}^{3}$,[^v-5p1-47] whose hyperplane sections are
reducible (in fact formed by pairs of concurrent lines) and form therefore a two-dimensional family, hence of
codimension one in $P^{\vee}$ (indeed the dual of the quadric is a quadric in the dual space relative to the dual
form).*

<!-- original page 33 -->

In the case of a non-singular surface in a projective space this situation should however be considered as exceptional,
[as we shall see] in the following subsection.

Let us suppose $X$ integral and proper over $k$ and $f$ an immersion. Then it follows from (5.6.1), (5.8.7), and
(5.8.14) that if $Y^{sing} \to P^{\vee}$ is not generically finite and inseparable, the set of $\xi \in P^{\vee}$ such
that $Y_{\xi}$ is separable over $k(\xi)$ with at most two irreducible components has a complement of codimension at
least two.

We shall now examine more precisely the case of surfaces. (The case of curves does not arise, from the point of view of
irreducibility of hyperplane sections.)

> *Grothendieck note.* I noticed with fright that the quadric is not entitled to be called ruled in the sense in which I
> have been using the word "ruled". This is in disagreement with our forefathers,[^v-5p1-48] and it would be necessary
> to invent a more adequate word for the notion used here.

**Proposition (5.8.18).**

<!-- label: V.5.8.18 -->

*Suppose that $k$ is algebraically closed, $X$ is integral (respectively integral and normal) of dimension $\geq 2$ and
proper over $k$. Let $T$ be a closed finite subset of $X$ such that $X - T$ is smooth, and let $f | (X - T)$ be
unramified. In order that the set of $\xi \in P^{\vee}$ such that $Y_{\xi}$ is geometrically irreducible (respectively
geometrically integral) of dimension $d - 1$ should have a complement of codimension $\geq 2$, it is necessary and
sufficient that the following conditions be satisfied:*

*(a) For every $x \in T$, there exists a hyperplane section $Y_{\xi}$ ($\xi \in P^{\vee}(k)$) passing through $x$, of
dimension $d - 1$, and which is irreducible.*

*(b) $X' = X - T$ is "ruled" (sic) for $f$, or there exists a hyperplane section $Y_{\xi_{0}}$ ($\xi_{0} \in
P^{\vee}(k)$) of $X'$ which is of dimension $d - 1$, non-singular, and irreducible.[^v-5p1-49]*

Let us first assume that $X$ is geometrically normal. We have already seen (by (5.8.14) (a)) that we can find a closed
subset $Z'$ of $P^{\vee}$ of codimension $\geq 2$ such that $\xi \in P^{\vee} - Z'$ implies that $Y_{\xi}$ is separable
over $k(\xi)$ and of dimension $d - 1$. For such a $\xi$, it amounts to the same thing that $Y_{\xi}$ should be
geometrically irreducible or geometrically integral, and the two problems[^v-5p1-50] considered in (5.8.18) are
therefore equivalent. On the other hand, by (5.5.6), the set $U$ of $\xi \in P^{\vee}$ such that $Y_{\xi}$ is
geometrically integral of dimension $d - 1$ (the dimension hypothesis stating that $\phi_{\xi}$ is $F_{k(\xi)}$-regular)
is open. We will exhibit a non-empty open subset $P^{\vee} - Z$ contained in $U$, taking for $Z$ the union of
$g(Y^{\prime,sing})$ and of the hyperplanes $H_{x}$ of $P^{\vee}$ defined by the $f(x)$, $x \in T$. For $\xi \in
P^{\vee} - Z$, $Y_{\xi}$ is smooth of dimension $d - 1$, and since it is geometrically connected by (5.6.1), it is
geometrically integral. We have to express (prove) that every irreducible component of codimension one of $Z$ meets the
open set $U$. But these irreducible components are the $H_{x}$ (possibly repeated, but it is not essential) and

<!-- original page 34 -->

also $g(Y^{\prime,sing})$ when the latter is indeed of codimension one, i.e. $X'$ "not ruled" for $f$. (N.B. We use the
irreducibility of $Y^{\prime,sing}$.) On the other hand, in order that this latter set should meet the open set $U$, it
is necessary and sufficient that $g(Y^{\prime,sing})$ (which contains an open dense set) should meet $U$. This proves
(5.8.18) in this case. If we do not suppose that $X$ is normal, we apply the previous result to the normalization of
$X$; the reasoning is immediate and I do not give the details here.

(N.B. In the geometrically integral case, (5.8.18) is contained in (5.8.16), more precisely, except in the case $d = 2$.
It is for the case of geometric irreducibility that it may be better not to require $d = 2$ and not only $d \geq 2$.)

It remains to make explicit the conditions (a) and (b) of (5.8.18). This leads us to examine in a general way the
following situation. Suppose that $X$ is geometrically irreducible over $k$, and consider a linear subvariety $L$ of $P$
(corresponding to the question of studying the hyperplane sections of $X$ passing through a given point $x$, or tangent
to $X$ at a given smooth point), formed therefore by the hyperplanes containing a linear subvariety `L_0` of $P$
(respectively a point, or the image of a tangent space to $X$ at a smooth point, in the two cases considered). We ask
the question whether for the generic point of $L$ (and hence for all points of a non-empty open subset of $L$), $Y$ is
geometrically irreducible of dimension $\dim X - 1$.

This is a variant of Bertini's theorem, which must appear in §V.5.3, and is treated by exactly the same method (or, if
one likes, reduces to it).[^v-5p1-51] The dimension question is settled simply by $f(X) \nsubset L_{0}$, i.e. by $X' =
f^{-1}(P - L_{0})$ being a dense open subset of $X$. Let $Q$ be the projective space of hyperplanes passing through
`L_0`. (N.B. If `L_0` is defined by a vector subspace `F_0` of $E$, we have $Q = \mathbb{P}(F_{0})$, and we consider the
canonical morphism (deduced from $F_{0} \to E$, cf. Chapter II)

```text
  u : P − L_0 ⟶ Q,
```

and we consider

```text
  g = u f' : f^{-1}(P − L_0) = X' ⟶ Q,
```

so that $L \cong Q^{\vee}$ and the family of $X'_{\xi}$ ($\xi \in L$) is nothing else than the family of hyperplane
sections relative to the morphism $g$. On the other hand, we see immediately that for every $\xi \in L$, "general" $X'$
is dense in $X$, so that $X'$ is geometrically irreducible if and only if $X$ is such. Granted this, the Bertini-Zariski
theorem shows us that we have the desired conclusion of irreducibility provided that $\dim g(X') \geq 2$. (To tell the
truth, one could give a converse to (5.3.1) as follows: if $X$ is geometrically irreducible, $Y$ is geometrically
irreducible if and only if either $\dim f(X) \geq 2$, or $\dim f(X) = 1$ and $f(X)$ is contained in a straight line $D$
defined over $k$ and the generic fibre of $X \to D$ is geometrically irreducible.) This also allows us, in the present
version with $L$, to have a necessary and sufficient condition for geometric irreducibility of $Y_{\xi}$, $\xi$ generic
in $L$.

From the cohomological[^v-5p1-52] point of view and in terms of field theory, we can express the condition in terms of
transcendence degree in the following fashion. We choose a "hyperplane at infinity" containing neither `L_0` nor $X$,
and we place ourselves in its complement, i.e. over a scheme of affine type essentially. We choose a basis of the space
of linear forms vanishing on `L_0`, say $T_{1}, \cdots, T_{p}$ ($p = codim(L_{0}, P)$), and we consider their inverse
images $t_{1}, \cdots, t_{p}$ in the field of fractions $K$ of $X$ ($X$ assumed integral). At least one of the $t_{i}$,
say $t_{1}$, is $\neq 0$. Consider therefore $a_{1} = t_{2} / t_{1}, \cdots, a_{p-1} = t_{p} / t_{1}$; then $\dim g(X')$
is nothing else but the transcendence degree of $K(a_{1}, \cdots, a_{p-1}) \subset K$ over $k$. Therefore, if the
transcendence degree is $\geq 2$, we are okay. If it is one, then we must require that, over $\overline{k}$, $f(X)$ be
contained in a linear subvariety of $P$ containing `L_0` and of

<!-- original page 35 -->

dimension at most one, and that the generic fibre of $g : X' \to g(X')$ should be geometrically irreducible.

Suppose that `L_0` is of dimension $q$, so that the fibres of $u : P - L_{0} \to Q$ are of dimension $q + 1$, and hence
those of $g$ are of dimension $\leq q + 1$. Consequently we have $\dim g(X') \geq \dim f(X) - (q + 1)$, so that the
dimension condition for $g(X')$ is verified provided $\dim f(X) \geq q + 3$. If $q = 0$, we find the fact indicated in
(5.8.17) (a). Returning to the conditions of (5.8.18), we see that condition (a), relative to an $x \in T$, is satisfied
provided that $X$ is not "conical at $x$ relative to $f$" in an obvious sense.

> *Grothendieck note.* Maybe it will be better to introduce these latest Bertinisque developments in the next
> subsection, "Change of projective immersion".

______________________________________________________________________

[^v-5p1-1]: Translator's note: Blass renders this as "pêle mêle Fr". The French *pêle mêle* ("pell-mell", "jumbled
    together") is preserved here as "pell-mell" to keep Grothendieck's deliberately informal tone in his covering
    letter. The original Blass text retains the French.

[^v-5p1-2]: Translator's note: Blass adds a marginal "Ask AG if No. 16 has ever been written. [Tr]". The Vaiello unified
    edition records that §V.5.16 was never written; the present part 1 stops well before §V.5.9, so the question is
    deferred to part 2.

[^v-5p1-3]: Translator's note: Blass writes "compare Par. 19 [of EGA IV Tr.]" and adds a footnote that this "uses
    notation of new edition of EGA I [Tr.]". We render §V.19 (formerly EGA IV §19) which is the natural cross-reference
    in the renumbered scheme.

[^v-5p1-4]: Translator's note: Blass writes "of finite type over $P$ [Tr]" with the marginal query "or over $S$, I am
    not sure [Tr]". The intended meaning is clearly "of finite type over $S$, with a structural morphism $f : X \to P$";
    the apparent ambiguity is between the structural morphism and the morphism through which $X$ becomes a $P$-scheme,
    which is $f$ itself. We adopt the natural reading.

[^v-5p1-5]: Translator's note: Blass adds the marginal query "Ask A.G. if module always means coherent or quasi-coherent
    sheaf of modules". In the standard EGA usage of the period, "module" without qualifier defaults to "quasi-coherent
    module"; we follow that convention here.

[^v-5p1-6]: Translator's note: Blass adds a marginal query "Ask Grothendieck: What is the meaning and role of underlined
    capital letters, in Section One for example". The underlined capitals in §V.5.1 (here normalized to upright
    capitals) appear in the source PDF as ordinary closure overlines indicating Zariski closure; we render them as
    $\overline{(\cdot)}$ in displays and $\bar{Z}$ or "closure of $Z$" in prose.

[^v-5p1-7]: Translator's note: Blass adds the marginal query "Tr: clear up this reference. Is it EGAIV?" — yes, the
    reference is to EGA IV §6, which we render as "§IV.6".

[^v-5p1-8]: Translator's note: the source carries an editorial "incomprehensible" marker at this point. The reduction to
    $k$ algebraically closed is the standard one (radical multiplicity at a prime cycle is preserved by the regular
    morphism $Y_{\eta} \to X$, and the algebraic-closure base change is faithfully flat), and we render the sentence as
    the intended reduction.

[^v-5p1-9]: Translator's note: Blass adds the marginal remark "$X$ unramified or $k$ of characteristic zero". Either
    condition suffices: if $f$ is unramified the proof in (5.2.12) goes through; if $k$ is of characteristic zero,
    smooth = regular for algebraic preschemes.

[^v-5p1-10]: Translator's note: Blass writes "Si to Si [PB: check this!]" with the marginal "Probably $S_{i}$ to
    $[S_{i}]$, equivalence class of $S_{i}$ in $L$ [Tr.]". We render this as the natural inclusion sending each affine
    coordinate $S_{i}$ to its image in $L$.

[^v-5p1-11]: Translator's note: Blass adds the marginal "primary extension probably means that the smaller field is
    algebraically closed in the larger one (or quasi algebraically closed) [Tr]. Jouanolou Th. 3.6 [Tr]". This is
    correct: "primary" here means "regular" in the sense of Bourbaki, *Alg. comm.*: $k$ is algebraically closed in $K$,
    or equivalently $K \otimes_{k} \overline{k}$ is reduced and $K$ is geometrically irreducible over $k$.

[^v-5p1-12]: Translator's note: Blass writes "in par. 6" with a marginal query; we render as §IV.6 since Hartshorne's
    connectedness theorem in the form Grothendieck uses appears in EGA IV §6 (more precisely §IV.15.6.3 in the published
    EGA IV, which is invoked again in (5.6.1) below).

[^v-5p1-13]: Translator's note: Blass writes "the previous two [Tr] sections" with a marginal query about the referent.
    Reading the source, the "previous two" are §§V.5.2 and V.5.3 — the local-properties and irreducibility-connectedness
    subsections we have just translated.

[^v-5p1-14]: Translator's note: Blass appends "(extension prealable Fr)". The French *extension préalable* ("prior
    extension") is a standard EGA expression for "a base change made before applying the construction"; we render as
    "prior extension of the base field".

[^v-5p1-15]: Translator's note: the source labels this Proposition 4.2 rather than 4.1; there is no 4.1 in the prenote
    (the introductory subsection numbered 4.1 is absorbed into the running text). We preserve the original numbering,
    since reordering would shift downstream references.

[^v-5p1-16]: Translator's note: Blass adds the marginal query "What is AQT? Ask AG.". The abbreviation appears nowhere
    else in the prenote; it is most plausibly "Artin-Quasi-finite Trick" or "abstract quotient technique", referring to
    a standard descent argument from §IV.9. We retain the marker since it has no settled expansion.

[^v-5p1-17]: Translator's note: Blass renders the Latin "Redactor demerdetur" — Grothendieck's own coinage, roughly "let
    the redactor extricate himself" — verbatim. We translate as "let the redactor sort himself out" and preserve the
    spirit of the original tag.

[^v-5p1-18]: Translator's note: Blass writes "paragraph 12" with the marginal "Locate that reference, most likely EGA IV
    [Tr], Yes [Tr].". We render as §IV.12, which is the openness-of-loci subsection in EGA IV the prenote points back
    to.

[^v-5p1-19]: Translator's note: Blass adds the marginal "Since $Y$ is proper over $X$ and $P^{\vee}$ is separated over
    $S$. (Marginal remark [Tr])". We incorporate this into the running argument.

[^v-5p1-20]: Translator's note: Blass writes "as Mike says" and adds a footnote "Mike Artin (I presume P.B.)". We render
    as "M. Artin".

[^v-5p1-21]: Translator's note: Blass adds the marginal "Ask AG about reference – probably EGA IV [Tr]. 12.1.4 does not
    check out [Tr].". §IV.12.1.4 is in fact the standard reference for openness of properties in flat families; the
    indexing in the published EGA IV is `(IV, 12.1.4)` and refers to the openness of the geometric properties listed in
    §IV.12.1.1.

[^v-5p1-22]: Translator's note: Blass writes "for sure" with the marginal "or to be sure [Tr]". The French residue *pour
    de bon* ("definitely", "for sure") is retired to "to be sure".

[^v-5p1-23]: Translator's note: Blass adds "(by successive approximations ???)" with a footnote "Translator's note: *de
    proche en proche* [Fr.]". The French *de proche en proche* ("step by step", "by successive approximations") is
    rendered as "by successive approximations" in scare quotes, since the construction is precisely the iterative one
    Grothendieck describes.

[^v-5p1-24]: Translator's note: Blass writes "in the case (v) that for every $s \in S$ [illegible] irreducible component
    $Z$ of $X_{s}$ we have $\dim f(Z) \geq 2$. \[Nota Bene: For (v) compare 12.2.1 (x) and (xi) (we can then
    [illegible] in the other case 4.3 or 12.2.1 (x)\] (marginal remark largely illegible in preceding square
    brackets)". We follow the Vaiello reconciliation in restoring the intended hypothesis "in case (v), for
    every $s \in S$ and every irreducible component $Z$ of $X_{s}$, $\dim f(Z) \geq 2$".

[^v-5p1-25]: Translator's note: Blass adds the marginal "Unclear, ask AG.". The statement is clear in the Vaiello
    edition: when $k(s)$ is infinite, the multisection $S'$ may be realized inside `X_U` as a closed subscheme; in the
    finite-residue-field case one needs an étale extension first.

[^v-5p1-26]: Translator's note: Blass marks "by taking $X$ étale non-finite over $S$ …" with "Illegible". The intended
    example is the standard one: an étale cover that is not finite, e.g. an open immersion that is étale but not
    surjective, can fail to admit a multisection of the required type.

[^v-5p1-27]: Translator's note: Blass writes "(see Section No.29 for examples)" with the marginal "Section number
    omitted, ask A.G.". The reference is to the subsection on pencils of hyperplane sections (§V.5.10 in our numbering),
    treated in part 2.

[^v-5p1-28]: Translator's note: Blass renders the Latin "Redactor decidetur" (Grothendieck's coinage) with the footnote
    "Editor decide". We translate as "Let the redactor decide".

[^v-5p1-29]: Translator's note: Blass writes "we have $\dim f(X_{i}) >$[illegible, is it two, ask A.G.]". The PDF
    resolves this as "$\geq 2$", which matches the rest of the proof; we drop the marker.

[^v-5p1-30]: Translator's note: Blass marks the property failing "(S_k)" with an "Illegible, ask A.G."; the context
    (irreducible component of codimension $\geq 2$ of $G_{\xi}$ failing the property $(S_{k})$ already enjoyed by $F$)
    makes the intended statement clear.

[^v-5p1-31]: Translator's note: Blass writes "is quite floppy (or perhaps sloppy) [Tr]". We preserve the
    Grothendieck-style self-deprecation as part of the prenote character.

[^v-5p1-32]: Translator's note: Blass marks the condition with "Illegible, ask A.G.". The Vaiello reconciliation
    restores it as "we have at most simple embedded components" (cf. EGA IV §IV.5.10 for the condition on associated
    prime cycles), but we preserve Blass's marker to flag the source ambiguity.

[^v-5p1-33]: Translator's note: Blass writes "the coprof_x [illegible]" — the natural reading (and the one consistent
    with §V.5.8 below) is $coprof_{x} F \geq n$, i.e. that $x$ lies in the level set of the codepth function.

[^v-5p1-34]: Translator's note: Blass writes "for every closed subset $R$ of [illegible, ask A.G.]"; the referent in
    context is $X$ (the ambient prescheme), as confirmed by the conclusion of the sentence.

[^v-5p1-35]: Translator's note: Blass writes "(par. 16)" with the marginal "See part II of these notes [Tr]". In our
    numbering, this is §V.1 (formerly EGA IV §16), the singular-and-supersingular-zeros subsection.

[^v-5p1-36]: Translator's note: Blass writes "No. 16 or paragraph 16" with the marginal "Ask AG about this reference –
    just later part of these notes". The reference is to §V.1 of these notes (the singular-zeros subsection), where the
    locally-free-module diagram is set up.

[^v-5p1-37]: Translator's note: Blass writes "\[Note to AG, the upper G is really an illegible letter `P^{\vee}/S` what is
    this?\]". The intended object is the relative tangent sheaf $\mathcal{G}_{P^{\vee}/S}$ (kernel of the augmentation
    $\mathcal{P}^{1}_{P^{\vee}/S} \to \mathcal{O}_{P^{\vee}}$), in line with the §V.1 conventions; we render it $\mathcal{G}_{P^{\vee}/S}$.

[^v-5p1-38]: Translator's note: Blass writes "section $\psi$ [Blass: check if this letter is OK]"; the section is the
    differential $\Psi = (d\phi) |_{Y}$ introduced just above, with the lowercase variant used in the diagram
    verification. We follow Blass and write $\psi$ here.

[^v-5p1-39]: Translator's note: Blass numbers this as Corollary 8.9, skipping 8.8 (the proof of (5.8.7) absorbs what
    would have been 8.8). We preserve the prenote numbering, so there is a gap between (5.8.7) and (5.8.9).

[^v-5p1-40]: Translator's note: Blass writes "[la taupe Fr]" — French *la taupe* literally "the mole", Grothendieck's
    slang for classical (pre-EGA) geometers (cf. *en termes de papa* in §V.1). We render as "the classical language".

[^v-5p1-41]: Translator's note: Blass writes "if you feel inspired to make connection with [la taupe Fr]". We restate as
    "make a connection with classical terminology".

[^v-5p1-42]: Translator's note: Blass writes "[illegible] $x \in X(k)$ so $T$ contains" with "illegible" markers; the
    natural reading is "any $x \in X(k)$ is contained in $T$", since if $\dim X = 1$ the variety $X$ itself is contained
    in its tangent variety.

[^v-5p1-43]: Translator's note: Blass adds a parenthetical "Do it Blass" — Grothendieck's working note to his
    translator. The examples in characteristic $p > 0$ are the standard ones with a non-singular plane curve admitting
    strange tangent lines (cf. Hartshorne *Algebraic Geometry*, IV.3, Example 3.8.4).

[^v-5p1-44]: Translator's note: Blass writes "of dimension $\leq k - 1$ (Ask A.G. illegible)". The dimensional bound
    $\leq k - 1$ matches the Vaiello reconciliation and the geometric meaning of the statement; we drop the marker.

[^v-5p1-45]: Translator's note: Blass writes "[illegible] n.". The PDF does not resolve this marker; the sentence makes
    sense with the marker dropped, as it is clearly closing the preamble to (a) and (b).

[^v-5p1-46]: Translator's note: Blass writes "condition that only eliminate a set of codimension (illegible)"; the
    intended bound is "codimension $\geq 2$" — the regularity condition is generic — but we preserve the marker shape
    and write "codimension one" since the codimension-one set being eliminated is the trace of the non-regularity locus.

[^v-5p1-47]: Translator's note: Blass writes "for a non-singular quadric $X$ in $P^{3}$ [illegible]". The PDF resolves
    the marker as ordinary mathematical text continuing the example; we drop it.

[^v-5p1-48]: Translator's note: Blass writes "in disagreement with our fathers", the literal English for the French
    *avec nos pères* (our forefathers / our predecessors in the classical school). The variant *en termes de papa*
    recorded in §V.1 belongs to the same family of expressions.

[^v-5p1-49]: Translator's note: Blass writes "of dimension $d - 1$ (non???) singular and irreducible.[^] \[illegible,
    ask A.G.\]". The PDF resolves the question mark — the section is non-singular and irreducible — and we drop the
    marker.

[^v-5p1-50]: Translator's note: Blass writes "the two problems [(respé et non respé) Fr. p. 50] (?)". The French *respé
    / non respé* are Grothendieck's shorthand for "respectively / not respectively", marking the parallel cases
    "geometrically irreducible" and "geometrically integral". We render as "the two problems" and let context carry the
    parallelism.

[^v-5p1-51]: Translator's note: Blass writes "which [j(devrait figurer) 51] must appear in No. 3, and is treated by
    exactly the same method, [(ou, si on veut, s'y ramène) Fr 51]". The French *qui devrait figurer / ou, si on veut,
    s'y ramène* glosses as "which must appear / or, if one prefers, reduces to it"; we render as a single clause.

[^v-5p1-52]: Translator's note: Blass writes "From the [(cunutesque?) Fr] point of view". The French marker is illegible
    in the PDF; the intended adjective is most plausibly *cohomologique* ("cohomological"), so we render "cohomological"
    while flagging the uncertainty.

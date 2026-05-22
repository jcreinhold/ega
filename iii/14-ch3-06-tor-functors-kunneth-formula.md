# §6. Local and global Tor functors; the Künneth formula

> _Translator's note._ This section is translated in two parts for length: §6.1–§6.6 here, §6.7–§6.9 in the companion
> file. They will be concatenated for the final volume.

<!-- original page 137 -->

## 6.1. Introduction.

**6.1.1.**

<!-- label: III.6.1.1 -->

Let $f : X \to Y$ be a morphism of preschemes and let $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-module. In the
study of the "higher direct images" $R^{n} f_{*}(\mathcal{F})$, one is led to consider the following general problem:
given a "base change" morphism $g : Y' \to Y$, we set $X' = X_{(Y')} = X \times_{Y} Y'$, $\mathcal{F}' = \mathcal{F}
\otimes_{\mathcal{O}_{Y}} \mathcal{O}_{Y'}$, $f' = f_{(Y')} : X' \to Y'$, and we propose to obtain information on the
higher direct images $R^{n} f'_{*}(\mathcal{F}')$ (assuming the $R^{n} f_{*}(\mathcal{F})$ known). One sees easily (cf.
for example `(7.7.2)`) that one is reduced to studying the variations of $R^{n} f_{*}(\mathcal{F}
\otimes_{\mathcal{O}_{Y}} \mathcal{G})$ for a variable quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{G}$, in other
words the functor $\mathcal{G} \mapsto R^{n} f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{G})$. If $\mathcal{F}$
is flat over $Y$, the functor $\mathcal{G} \mapsto \mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{G}$ is exact $(0_{I},
6.7.4)$, and consequently the composite functor $\mathcal{G} \mapsto R^{n} f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{Y}}
\mathcal{G})$ is again a cohomological functor. But this is no longer the case in general; in order to be able to apply
the cohomological methods, one is led to substitute for $\mathcal{G} \mapsto R^{n} f_{*}(\mathcal{F}
\otimes_{\mathcal{O}_{Y}} \mathcal{G})$ other functors which this time are *always* cohomological functors. These
functors, which generalize the "Tor" functors of module theory, are defined in n°s `6.3` to `6.7`; there are moreover
two such generalizations, one "local" and the other "global", related by spectral sequences that will be discussed in n°
`6.7`; as an application of these spectral sequences, one obtains in particular, under certain conditions, a "Künneth
formula" expressing $R^{n} (f_{1} \times f_{2})_{*}(\mathcal{F}_{1} \otimes_{Y} \mathcal{F}_{2})$ by means of the higher
direct images $R^{p} f_{1*}(\mathcal{F}_{1})$ and $R^{q} f_{2*}(\mathcal{F}_{2})$. Other spectral sequences `(6.8)`
generalize the associativity spectral sequences of the "Tor" functor of modules; finally, the base-change problem itself
leads to spectral sequences `(6.9)`.

**6.1.2.**

<!-- label: III.6.1.2 -->

In addition, one observes `(6.10)` that the cohomological functors $\mathcal{G} \mapsto \mathcal{T}_{i}(\mathcal{G})$ so
defined are locally (on $Y$) of the type $\mathcal{G} \mapsto \mathcal{H}_{i}(\mathcal{L}_{\bullet} \otimes_{Y}
\mathcal{G})$, where $\mathcal{L}_{\bullet}$ is a complex of locally free $\mathcal{O}_{Y}$-modules (defined up to
homotopy) and $\mathcal{H}_{\bullet}$ denotes homology. There is then an interest in forgetting the particular situation
that gave

<!-- original page 138 -->

rise to $\mathcal{T}_{i}$, and in studying in general the functors of the preceding form $\mathcal{G} \mapsto
\mathcal{H}_{i}(\mathcal{L}_{\bullet} \otimes_{Y} \mathcal{G})$ (where one moreover, if appropriate, makes finiteness
hypotheses on the $\mathcal{L}_{i}$ or the $\mathcal{H}_{i}(\mathcal{L}_{\bullet})$): this is the object of §7, whose
reading, for the essentials, is independent of §6. The most important properties of these functors concern the exactness
properties of a component $\mathcal{T}_{i}$ of $\mathcal{T}_{\bullet}$; we shall give various criteria allowing such
properties to be established; as an application, one will obtain conditions allowing one to assert (with the notations
of `(6.1.1)`) that the functor $\mathcal{G} \mapsto R^{n} f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{Y}} \mathcal{G})$ is
exact (which one will express by saying that $\mathcal{F}$ is *cohomologically flat over* $Y$ in dimension $n$). Another
important property for the components $\mathcal{T}_{i}$ of $\mathcal{T}_{\bullet}(\mathcal{G}) =
\mathcal{H}_{i}(\mathcal{L}_{\bullet} \otimes_{Y} \mathcal{G})$ is the *semi-continuity property* of the function $y
\mapsto \dim_{\kappa(y)}(\mathcal{T}_{i}(\kappa(y)))$; when $\mathcal{T}_{i}$ is exact, this property is replaced by a
*continuity property*, the converse being moreover true according to Grauert when $Y$ is reduced `(7.8.4)`.

**6.1.3.**

<!-- label: III.6.1.3 -->

In §§ 6 and 7, we have systematically made use of *hypercohomology*, taking everywhere as arguments *complexes* of
sheaves instead of sheaves, although the necessity of this point of view will appear only in later chapters. The
cohomological formalism developed on this occasion will moreover become more transparent in the chapter of this Treatise
that will be devoted to the elaboration of an algebra of cohomological functors of coherent sheaves, including the
duality formalism. But that will require developments which fall outside the framework of the present chapter.

**6.1.4.**

<!-- label: III.6.1.4 -->

To abbreviate, given two complexes $K^{\bullet}$, $K'^{\bullet}$ in an abelian category $\mathcal{C}$, we shall say that
a morphism of complexes $f : K^{\bullet} \to K'^{\bullet}$ is a *homotopism* if there exists a morphism $g :
K'^{\bullet} \to K^{\bullet}$ such that the composite morphisms $f \circ g$ and $g \circ f$ are both homotopic to the
identity (by abuse of language, when such a homotopism exists, one also says that $K^{\bullet}$ and $K'^{\bullet}$ are
*homotopic*). When one can define the hypercohomology of a covariant additive functor $T$ from $\mathcal{C}$ into an
abelian category $\mathcal{C}'$ with respect to a complex of $\mathcal{C}$ $(0_{III}, 11.4.3)$, it is immediate that a
homotopism $K^{\bullet} \to K'^{\bullet}$ of complexes of $\mathcal{C}$ canonically defines an isomorphism $R^{\bullet}
T(K^{\bullet}) \to R^{\bullet} T(K'^{\bullet})$ for hypercohomology (loc. cit.).

## 6.2. Hypercohomology of complexes of modules on a prescheme.

**6.2.1.**

<!-- label: III.6.2.1 -->

Let $X$ be a prescheme and $\mathcal{K}^{\bullet} = (\mathcal{K}^{i})_{i \in \mathbb{Z}}$ a complex of
$\mathcal{O}_{X}$-modules whose differential is of degree `+1`. Recall that for every morphism $f : X \to Y$ of
preschemes, one has defined $(0_{III}, 12.4.1)$ the $\mathcal{O}_{Y}$-modules of hypercohomology $\mathcal{H}^{n}(f,
\mathcal{K}^{\bullet})$ (also denoted $\mathcal{H}^{n}(\mathcal{K}^{\bullet})$ or $R^{n} f_{*}(\mathcal{K}^{\bullet})$)
for every $n \in \mathbb{Z}$; the hypercohomology $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet})$ is the abutment of
the two spectral functors $'\mathcal{E}(f, \mathcal{K}^{\bullet})$ and $''\mathcal{E}(f, \mathcal{K}^{\bullet})$, whose
`E_2` terms are given by

```text
  'E_2^{p,q} = ℋ^p(ℋ^q(f, 𝒦^•))                                                (6.2.1.1)
  ''E_2^{p,q} = ℋ^p(f, ℋ^q(𝒦^•)) = R^p f_*(ℋ^q(𝒦^•))                            (6.2.1.2)
```

<!-- original page 139 -->

where $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet})$ is the complex whose component of degree $i$ is
$\mathcal{H}^{i}(f, \mathcal{K}^{\bullet}) = R^{i} f_{*}(\mathcal{K}^{i})$ (loc. cit.). Recall also that when $Y$ is
reduced to a point, one denotes the corresponding hypercohomology by $H^{\bullet}(X, \mathcal{K}^{\bullet})$ (which is
formed of modules over $\Gamma(X, \mathcal{O}_{X})$ independent of the punctual prescheme $Y$ considered); when $Y = X$
and $f = 1_{X}$, one has $\mathcal{H}^{n}(f, \mathcal{K}^{\bullet}) = \mathcal{H}^{n}(\mathcal{K}^{\bullet})$
(cohomology of the complex $\mathcal{K}^{\bullet}$); when $\mathcal{K}^{i} = 0$ except for $i = i_{0}$, one has

```text
  ℋ^n(f, 𝒦^•) = R^{n − i_0} f_*(𝒦^{i_0}).
```

The spectral sequence $'\mathcal{E}(f, \mathcal{K}^{\bullet})$ is always regular; the two spectral sequences are
biregular when $\mathcal{K}^{\bullet}$ is bounded below $(0_{III}, 12.4.1)$. Every homotopism $h : \mathcal{K}^{\bullet}
\to \mathcal{K}'^{\bullet}$ of complexes of $\mathcal{O}_{X}$-modules `(6.1.4)` gives an isomorphism
$\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet}) \xrightarrow{\sim} \mathcal{H}^{\bullet}(f, \mathcal{K}'^{\bullet})$
for hypercohomology. The same holds when one assumes only that $\mathcal{H}^{\bullet}(h) :
\mathcal{H}^{\bullet}(\mathcal{K}^{\bullet}) \to \mathcal{H}^{\bullet}(\mathcal{K}'^{\bullet})$ is an isomorphism and
that $\mathcal{K}^{\bullet}$ and $\mathcal{K}'^{\bullet}$ are *bounded below*, as follows at once from $(0_{III},
11.1.5)$ applied to the spectral sequence `(6.2.1.2)` and to the analogous one for $\mathcal{K}'^{\bullet}$. Finally,
for every open cover $\mathfrak{U} = (U_{\alpha})$ of $X$, one has also defined $(0_{III}, 12.4.5)$ the hypercohomology
$H^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet})$ as the cohomology of the bicomplex $C^{\bullet}(\mathfrak{U},
\mathcal{K}^{\bullet})$ (whose component of bi-indices $(i, j)$ is by definition $C^{i}(\mathfrak{U},
\mathcal{K}^{j})$); the $H^{n}(\mathfrak{U}, \mathcal{K}^{\bullet})$ are again modules over $\Gamma(X,
\mathcal{O}_{X})$.

**Proposition (6.2.2).**

<!-- label: III.6.2.2 -->

*Let $X$ be a scheme and $\mathfrak{U} = (U_{\alpha})$ a cover of $X$ by affine open sets. For every complex
$\mathcal{K}^{\bullet}$ of quasi-coherent $\mathcal{O}_{X}$-modules, the hypercohomology modules $H^{\bullet}(X,
\mathcal{K}^{\bullet})$ and $H^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet})$ are canonically isomorphic.*

**Proof.** Indeed, every finite intersection $V$ of open sets of the cover $\mathfrak{U}$ is affine `(I, 5.5.6)`, so
$H^{q}(V, \mathcal{K}^{i}) = 0$ for every $i$ and every $q > 0$ `(1.3.1)`; the proposition is therefore a particular
case of $(0_{III}, 12.4.7)$.

**Proposition (6.2.3).**

<!-- label: III.6.2.3 -->

*Let $f : X \to Y$ be a quasi-compact and separated morphism of preschemes. For every complex $\mathcal{K}^{\bullet}$ of
quasi-coherent $\mathcal{O}_{X}$-modules, the $\mathcal{O}_{Y}$-modules $\mathcal{H}^{n}(f, \mathcal{K}^{\bullet})$ are
quasi-coherent.*

**Proof.** Since the $\mathcal{H}^{q}(f, \mathcal{K}^{i}) = R^{q} f_{*}(\mathcal{K}^{i})$ are quasi-coherent
$\mathcal{O}_{Y}$-modules `(1.4.10)`, the same holds for $'E^{p,q}_{2}$, which, by `(6.2.1.1)`, is a quotient of a
kernel of a homomorphism of quasi-coherent modules by an image of such a homomorphism `(I, 4.1.1)`. For the same reason,
all the $\mathcal{O}_{Y}$-modules $'E^{p,q}_{r}$, $B_{r}('E^{p,q}_{r})$, $Z_{r}('E^{p,q}_{r})$ of the first spectral
sequence are quasi-coherent. The regularity of the spectral sequence $'\mathcal{E}(f, \mathcal{K}^{\bullet})$ implies
that $Z_{\infty}('E^{p,q}_{2})$ is equal to one of the $Z_{k}('E^{p,q}_{2})$, hence is quasi-coherent, and the same
holds for $B_{\infty}('E^{p,q}_{2}) = \varinjlim B_{k}('E^{p,q}_{2})$ $(0_{III}, 11.2.4)$ and `(I, 4.1.1)`; the
$'E^{p,q}_{\infty}$ are therefore also quasi-coherent. The preceding spectral sequence being regular, the filtration of
the $F^{p}(\mathcal{H}^{n}(f, \mathcal{K}^{\bullet}))$ is discrete and exhaustive; in other words, the
$\mathcal{O}_{Y}$-module $\mathcal{H}^{n}(f, \mathcal{K}^{\bullet})$ is the union of an increasing sequence
$(\mathcal{G}_{k})_{k \geq 0}$ of $\mathcal{O}_{Y}$-modules such that $\mathcal{G}_{0} = 0$ and such that each
$\mathcal{G}_{k}/\mathcal{G}_{k-1}$ is equal to one of the $\mathcal{O}_{Y}$-modules $'E^{p,q}_{\infty}$, hence is
quasi-coherent. By induction on $k$, one deduces that the $\mathcal{G}_{k}$ are quasi-coherent `(I, 4.1.17)`, and since
$\mathcal{H}^{n}(f, \mathcal{K}^{\bullet}) = \varinjlim \mathcal{G}_{k}$, the proposition is proved `(I, 4.1.1)`.

<!-- original page 140 -->

**Corollary (6.2.4).**

<!-- label: III.6.2.4 -->

*Under the hypotheses of `(6.2.3)`, for every affine open $V$ of $Y$, the canonical homomorphism*

```text
  H^n(f⁻¹(V), 𝒦^•) → Γ(V, ℋ^n(f, 𝒦^•))                                          (6.2.4.1)
```

*is bijective for every $n \in \mathbb{Z}$.*

**Proof.** The proof is the same as that of `(1.4.11)`, using `(6.2.2)`, replacing $\mathcal{F}$ by
$\mathcal{K}^{\bullet}$, $\mathcal{K}^{\bullet}$ by $f_{*}(\mathcal{C}^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet}))$,
$\mathcal{H}^{\bullet}(\mathcal{K}^{\bullet})$ by $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet})$, and noting that the
latter is a quasi-coherent $\mathcal{O}_{Y}$-module by `(6.2.3)`.

**Proposition (6.2.5).**

<!-- label: III.6.2.5 -->

*Let $Y$ be a locally noetherian prescheme, $f : X \to Y$ a proper morphism, $\mathcal{K}^{\bullet}$ a complex of
$\mathcal{O}_{X}$-modules such that the $\mathcal{O}_{X}$-modules $\mathcal{H}^{q}(\mathcal{K}^{\bullet})$ are coherent.
Then the $\mathcal{O}_{Y}$-modules $\mathcal{H}^{n}(f, \mathcal{K}^{\bullet})$ are coherent.*

**Proof.** The question being local on $Y$, one may restrict to the case where $Y$ is noetherian and affine, and it is
therefore, by `(6.2.4)`, a matter of proving that the $H^{n}(X, \mathcal{K}^{\bullet})$ are $\Gamma(Y,
\mathcal{O}_{Y})$-modules of finite type. One has then $H^{\bullet}(X, \mathcal{K}^{\bullet}) =
H^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet})$ `(6.2.2)`, where one may assume that $\mathfrak{U}$ is *finite*, since
$X$ is quasi-compact. The cochains of each complex $C^{\bullet}(\mathfrak{U}, \mathcal{K}^{i})$ being *alternating* by
definition, there is an integer $r > 0$ such that $C^{i}(\mathfrak{U}, \mathcal{K}^{j}) = 0$ for $i < 0$ and $i > r$;
one concludes $(0_{III}, 11.3.3)$ that the two spectral sequences of the bicomplex $C^{\bullet}(\mathfrak{U},
\mathcal{K}^{\bullet})$ are biregular. Since the intersections of the sets of $\mathfrak{U}$ are affine open sets
`(I, 5.5.6)`, each functor $\mathcal{F} \mapsto C^{i}(\mathfrak{U}, \mathcal{F})$ is exact in the category of
quasi-coherent $\mathcal{O}_{X}$-modules; hence $H^{i}_{q}(C^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet})) =
C^{i}(\mathfrak{U}, \mathcal{H}^{q}(\mathcal{K}^{\bullet}))$, and the `E_2` terms of the second spectral sequence of
$C^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet})$ are given $(0_{III}, 11.3.2)$ by

```text
  ''E_2^{p,q} = H^p(C^•(𝔘, ℋ^q(𝒦^•))) = H^p(𝔘, ℋ^q(𝒦^•)) = H^p(X, ℋ^q(𝒦^•))
```

by `(1.4.1)`; since $f$ is proper, these are $\Gamma(Y, \mathcal{O}_{Y})$-modules of finite type `(3.2.1)`. The spectral
sequence $''\mathcal{E}(C^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet}))$ being biregular, one deduces that the
$H^{n}(X, \mathcal{K}^{\bullet})$ are $\Gamma(Y, \mathcal{O}_{Y})$-modules of finite type $(0_{III}, 11.1.8)$.

*A fortiori*, if $\mathcal{K}^{\bullet}$ is a complex of coherent $\mathcal{O}_{X}$-modules, the
$\mathcal{O}_{Y}$-modules $\mathcal{H}^{n}(f, \mathcal{K}^{\bullet})$ are coherent under the hypotheses of `(6.2.5)`
relative to $Y$ and $f$ $(0_{I}, 5.3.4)$.

**6.2.6.**

<!-- label: III.6.2.6 -->

The hypercohomology $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet})$ is a cohomological functor in the category of
complexes of $\mathcal{O}_{X}$-modules *bounded below* $(0_{III}, 12.4.4)$. It is a cohomological functor in the
category of all complexes of $\mathcal{O}_{X}$-modules when the morphism $f$ is quasi-compact and the space underlying
$X$ is locally noetherian: indeed, it then follows from `(G, II, 3.10.1)` that $f_{*}$ commutes with inductive limits
(the question being local on $Y$), and one may apply $(0_{III}, 11.5.2)$.

Finally, if $f$ is *separated*, $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet})$ is a cohomological functor in the
category of complexes of quasi-coherent $\mathcal{O}_{X}$-modules. This is immediate when $Y$ is affine, since $X$ is
then a scheme, and so, by virtue of the canonical isomorphism `(6.2.2)`, one is reduced to seeing that
$\mathcal{K}^{\bullet} \mapsto H^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet})$ is a cohomological functor in the
category of complexes of quasi-coherent $\mathcal{O}_{X}$-modules, which is immediate since the functor
$\mathcal{K}^{\bullet} \mapsto C^{\bullet}(\mathfrak{U}, \mathcal{K}^{\bullet})$ is exact in this category `(I, 1.3.7)`.
In the general case, for every affine open $V$

<!-- original page 141 -->

of $Y$, $f^{-1}(V)$ is a scheme, and to apply what precedes, it suffices to verify that for an exact sequence $0 \to
\mathcal{K}^{\bullet} \to \mathcal{K}'^{\bullet} \to \mathcal{K}''^{\bullet} \to 0$ of complexes of quasi-coherent
$\mathcal{O}_{X}$-modules, the homomorphism $\partial : \mathcal{H}^{n}(f, \mathcal{K}''^{\bullet})|V \to
\mathcal{H}^{n+1}(f, \mathcal{K}^{\bullet})|V$ does not depend on the affine open cover $\mathfrak{U}$ of $f^{-1}(V)$
used to define it. But this follows from the fact that, if $\mathfrak{U}'$ is an affine open cover finer than
$\mathfrak{U}$, the diagram

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

When one of the preceding conditions is satisfied and $\mathcal{K}^{\bullet} \to \mathcal{K}'^{\bullet}$ is a homotopism
`(6.1.4)`, the corresponding isomorphism $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet}) \xrightarrow{\sim}
\mathcal{H}^{\bullet}(f, \mathcal{K}'^{\bullet})$ is then an isomorphism of $\partial$-functors $(0_{III}, 11.4.4)$.

**6.2.7.**

<!-- label: III.6.2.7 -->

All the preceding applies naturally without change (apart from notation) to a complex $\mathcal{K}_{\bullet}$ of
quasi-coherent $\mathcal{O}_{X}$-modules whose differential is of degree $-1$; it suffices to consider the complex
$\mathcal{K}^{\bullet} = (\mathcal{K}^{i})$ where $\mathcal{K}^{i} = \mathcal{K}_{-i}$ for every $i \in \mathbb{Z}$.

## 6.3. Hypertor of two complexes of modules.

**6.3.1.**

<!-- label: III.6.3.1 -->

Let $A$ be a commutative ring and $P_{\bullet}$, $Q_{\bullet}$ two complexes of $A$-modules whose differentials are of
degree $-1$; let $L_{\bullet,\bullet}$ (resp. $M_{\bullet,\bullet}$) be a Cartan–Eilenberg projective resolution of
$P_{\bullet}$ (resp. $Q_{\bullet}$) $(0_{III}, 11.6.1)$; $L_{\bullet,\bullet} \otimes_{A} M_{\bullet,\bullet}$ is then
(for the sum of the first degrees and the sum of the second degrees) a bicomplex (with differentials of degree $-1$),
whose homology $H_{\bullet}(L_{\bullet,\bullet} \otimes_{A} M_{\bullet,\bullet})$ does not depend on the chosen
Cartan–Eilenberg resolutions $L_{\bullet,\bullet}$, $M_{\bullet,\bullet}$, and is by definition the *hyperhomology* of
the bifunctor $P_{\bullet} \otimes_{A} Q_{\bullet}$ in $P_{\bullet}$ and $Q_{\bullet}$ $(0_{III}, 11.6.5)$. We shall set
by definition

```text
  Tor_n^A(P_•, Q_•) = H_n(L_{•,•} ⊗_A M_{•,•})                                  (6.3.1.1)
```

<!-- original page 142 -->

and we shall say that this $A$-module is the *hypertor of index* $n$ of the two complexes $P_{\bullet}$, $Q_{\bullet}$.
One knows that in the category of complexes of $A$-modules *bounded below*, the $Tor^{A}_{n}(P_{\bullet}, Q_{\bullet})$
form a homological bifunctor in $P_{\bullet}$, $Q_{\bullet}$ $(0_{III}, 11.6.5)$. Moreover:

**Proposition (6.3.2).**

<!-- label: III.6.3.2 -->

*The bifunctor $Tor^{A}_{n}(P_{\bullet}, Q_{\bullet})$ is the common abutment of two spectral bifunctors
$'E(P_{\bullet}, Q_{\bullet})$, $''E(P_{\bullet}, Q_{\bullet})$, whose `E_2` terms are*

```text
  'E_{p,q}^2 = H_p(Tor_q^A(P_•, Q_•))                                           (6.3.2.1)
  ''E_{p,q}^2 = ⊕_{q'+q''=q} Tor_p^A(H_{q'}(P_•), H_{q''}(Q_•))                  (6.3.2.2)
```

*where, in `(6.3.2.1)`, $Tor^{A}_{q}(P_{\bullet}, Q_{\bullet})$ denotes the bicomplex formed by the $A$-modules
$Tor^{A}_{q}(P_{i}, Q_{j})$. The spectral sequence `(6.3.2.2)` is always regular; if $P_{\bullet}$ and $Q_{\bullet}$ are
bounded below, or if $A$ is of finite cohomological dimension, the two spectral sequences `(6.3.2.1)` and `(6.3.2.2)`
are biregular.*

**Proof.** This follows from $(0_{III}, 11.6.5)$, since when $A$ is of finite cohomological dimension $n$, every
$A$-module admits a projective resolution of length $n$ `(M, VI, 2.1)`.

**Corollary (6.3.3).**

<!-- label: III.6.3.3 -->

*Let $P'_{\bullet}$, $Q'_{\bullet}$ be two complexes of $A$-modules, $u : P_{\bullet} \to P'_{\bullet}$, $v :
Q_{\bullet} \to Q'_{\bullet}$ two homomorphisms of complexes. If the homomorphisms $H_{\bullet}(u) :
H_{\bullet}(P_{\bullet}) \to H_{\bullet}(P'_{\bullet})$, $H_{\bullet}(v) : H_{\bullet}(Q_{\bullet}) \to
H_{\bullet}(Q'_{\bullet})$ deduced respectively from $u$ and $v$ are bijective, then the homomorphism
$Tor^{A}_{\bullet}(P_{\bullet}, Q_{\bullet}) \to Tor^{A}_{\bullet}(P'_{\bullet}, Q'_{\bullet})$ deduced from $u$ and $v$
is bijective.*

**Proof.** Indeed, the homomorphism of spectral sequences $''E(P_{\bullet}, Q_{\bullet}) \to ''E(P'_{\bullet},
Q'_{\bullet})$ deduced from $u$ and $v$ is then an isomorphism on the `E_2` terms, and the conclusion follows from the
fact that these spectral sequences are regular by `(6.3.2)` $(0_{III}, 11.1.5)$.

**Proposition (6.3.4).**

<!-- label: III.6.3.4 -->

*Let $P_{\bullet}$, $Q_{\bullet}$ be two complexes of $A$-modules, bounded below. Let $L_{\bullet,\bullet}$ (resp.
$M_{\bullet,\bullet}$) be a bicomplex formed by flat $A$-modules such that for every $i$, $L_{i,\bullet}$ (resp.
$M_{i,\bullet}$) is a resolution of $P_{i}$ (resp. $Q_{i}$). Then one has canonical isomorphisms*

```text
  Tor_•^A(P_•, Q_•) ⥲ H_•(L_{•,•} ⊗_A Q_•) ⥲ H_•(P_• ⊗_A M_{•,•}) ⥲ H_•(L_{•,•} ⊗_A M_{•,•}).
                                                                                (6.3.4.1)
```

**Proof.** This follows from $(0_{III}, 11.6.5, (ii) and (iii))$ and from the definition of flat $A$-modules.

**Remarks (6.3.5).**

<!-- label: III.6.3.5 -->

*(i)* With the notations of `(6.3.1)`, the bicomplexes $L_{\bullet,\bullet} \otimes_{A} M_{\bullet,\bullet}$ and
$M_{\bullet,\bullet} \otimes_{A} L_{\bullet,\bullet}$ are canonically isomorphic, whence a canonical isomorphism
$Tor^{A}_{\bullet}(P_{\bullet}, Q_{\bullet}) \xrightarrow{\sim} Tor^{A}_{\bullet}(Q_{\bullet}, P_{\bullet})$.

*(ii)* If $F$ and $G$ are two $A$-modules, $P_{\bullet}$ and $Q_{\bullet}$ the complexes of $A$-modules reduced to $F$
and $G$ respectively in degree `0` and zero in the other degrees, then two projective resolutions $L_{\bullet}$,
$M_{\bullet}$ of $F$ and $G$ respectively may be considered as Cartan–Eilenberg resolutions of $P_{\bullet}$ and
$Q_{\bullet}$ by completing them by zeros. One has consequently in this case $Tor^{A}_{\bullet}(P_{\bullet},
Q_{\bullet}) \xrightarrow{\sim} Tor^{A}_{\bullet}(F, G)$.

**Proposition (6.3.6).**

<!-- label: III.6.3.6 -->

*Let $(P^{\lambda}_{\bullet})$, $(Q^{\mu}_{\bullet})$ be two filtered inductive systems of complexes of $A$-modules; one
has a canonical isomorphism*

```text
  lim_→  Tor_•^A(P_•^λ, Q_•^μ) ⥲ Tor_•^A(lim_→ P_•^λ, lim_→ Q_•^μ).             (6.3.6.1)
        λ,μ                              λ          μ
```

**Proof.** Set $P_{\bullet} = \varinjlim P^{\lambda}_{\bullet}$, $Q_{\bullet} = \varinjlim Q^{\mu}_{\bullet}$; by
functoriality, it is clear that the $Tor^{A}_{\bullet}(P^{\lambda}_{\bullet}, Q^{\mu}_{\bullet})$ form an inductive
system and that the applications $Tor^{A}_{\bullet}(P^{\lambda}_{\bullet}, Q^{\mu}_{\bullet}) \to
Tor^{A}_{\bullet}(P_{\bullet}, Q_{\bullet})$ deduced

<!-- original page 143 -->

from the canonical applications $P^{\lambda}_{\bullet} \to P_{\bullet}$, $Q^{\mu}_{\bullet} \to Q_{\bullet}$ form an
inductive system of homomorphisms, whence a canonical homomorphism `(6.3.6.1)`, and more generally a canonical
homomorphism $\varinjlim ''E(P^{\lambda}_{\bullet}, Q^{\mu}_{\bullet}) \to ''E(P_{\bullet}, Q_{\bullet})$ of which
`(6.3.6.1)` is the homomorphism of abutments. In addition, the spectral sequence $''E(P_{\bullet}, Q_{\bullet})$ is
regular `(6.3.2)`, and the same holds for the spectral sequence $\varinjlim ''E(P^{\lambda}_{\bullet},
Q^{\mu}_{\bullet})$, as follows from the definitions $(0_{III}, 11.1.7)$ and from the proof of $(0_{III}, 11.3.3)$; to
show that `(6.3.6.1)` is bijective, it therefore suffices $(0_{III}, 11.1.5)$ to prove that the homomorphism

```text
  lim_→ ''E(P_•^λ, Q_•^μ) → ''E(P_•, Q_•)                                       (6.3.6.2)
```

is bijective on the `E_2` terms. Since the functor $H_{\bullet}$ commutes with the inductive limit of complexes of
modules, one is finally reduced to proving that for two filtered inductive systems $(F^{\lambda})$, $(G^{\mu})$ of
$A$-modules, the canonical homomorphism

```text
  lim_→ (Tor_•^A(F^λ, G^μ)) → Tor_•^A(lim_→ F^λ, lim_→ G^μ)
       λ,μ                              λ          μ
```

is bijective. For that, consider for each $F^{\lambda}$ the *canonical free resolution*

```text
  L_•^λ : ⋯ → L_{i+1}^λ → L_i^λ → ⋯ → L_1^λ → L_0^λ → 0
```

where $L^{\lambda}_{0}$ is the $A$-module of formal linear combinations of elements of $F^{\lambda}$ and
$L^{\lambda}_{i+1}$ is the $A$-module of formal linear combinations of elements of $Ker(L^{\lambda}_{i} \to
L^{\lambda}_{i-1})$; one verifies immediately that the $L^{\lambda}_{\bullet}$ form an inductive system of complexes,
and if one sets $F = \varinjlim F^{\lambda}$, $L_{i} = \varinjlim L^{\lambda}_{i}$, the $L_{i}$ form a resolution
$L_{\bullet}$ of $F$, since the functor $\varinjlim$ is exact; in addition, the $L_{i}$, inductive limits of free
$A$-modules, are flat $(0_{I}, 6.1.2)$. One considers similarly for each $\mu$ the canonical free resolution
$M^{\mu}_{\bullet}$ of $G^{\mu}$, and $M_{\bullet} = \varinjlim M^{\mu}_{\bullet}$ is a flat resolution of $G =
\varinjlim G^{\mu}$. One then has `Tor_•^A(lim_→ F^λ, lim_→ G^μ) = H_•(L_• ⊗_A M_•)` by virtue of `(6.3.5)` and
`(6.3.4)`; but $H_{\bullet}(L_{\bullet} \otimes_{A} M_{\bullet}) = \varinjlim H_{\bullet}(L^{\lambda}_{\bullet}
\otimes_{A} M^{\mu}_{\bullet})$ since $H_{\bullet}$ commutes with inductive limits of complexes of modules; since
$H_{\bullet}(L^{\lambda}_{\bullet} \otimes_{A} M^{\mu}_{\bullet}) = Tor^{A}_{\bullet}(F^{\lambda}, G^{\mu})$, this
completes the proof.

When one assumes that there exists $i_{0}$ such that $P^{\lambda}_{i} = Q^{\mu}_{i} = 0$ for $i < i_{0}$ for all
$\lambda$ and $\mu$, one proves in the same way that the canonical homomorphism

```text
  lim_→ 'E(P_•^λ, Q_•^μ) → 'E(P_•, Q_•)                                         (6.3.6.3)
```

is bijective.

**Proposition (6.3.7).**

<!-- label: III.6.3.7 -->

*Assume $P_{\bullet}$ and $Q_{\bullet}$ bounded below. If the complex $P_{\bullet}$ is formed of flat $A$-modules, one
has a canonical $A$-isomorphism of $\partial$-functors in $Q_{\bullet}$*

```text
  Tor_•^A(P_•, Q_•) ⥲ H_•(P_• ⊗_A Q_•).                                         (6.3.7.1)
```

**Proof.** Indeed, the spectral sequence `(6.3.2.1)` is biregular and degenerate, and the existence of the isomorphism
`(6.3.7.1)` follows from $(0_{III}, 11.1.6)$. In addition, by computing the hypertor from a Cartan–Eilenberg projective
resolution of $P_{\bullet}$ `(6.3.4)`, one sees at once that the isomorphism so defined is an isomorphism of
$\partial$-functors in $Q_{\bullet}$.

<!-- original page 144 -->

**6.3.8.**

<!-- label: III.6.3.8 -->

Let $\rho : A \to A'$ be a homomorphism of rings. We propose to define an $A$-homomorphism of degree `0` functorial in
$P_{\bullet}$, $Q_{\bullet}$, canonically associated with $\rho$:

```text
  ρ_{P_•, Q_•} : Tor_•^A(P_•, Q_•) → Tor_•^{A'}(P_• ⊗_A A', Q_• ⊗_A A').        (6.3.8.1)
```

For this, consider a Cartan–Eilenberg *projective* resolution $L_{\bullet,\bullet}$ of $P_{\bullet}$; consider on the
other hand a Cartan–Eilenberg *projective* resolution $L'_{\bullet,\bullet}$ of $P_{\bullet} \otimes_{A} A'$. We shall
see that one can define an $A'$-homomorphism of complexes $L_{\bullet,\bullet} \otimes_{A} A' \to L'_{\bullet,\bullet}$,
determined up to homotopy. Indeed, the construction of $L_{\bullet,\bullet}$ is entirely determined when one is given
(arbitrarily), for each $i$, a projective resolution $(X^{B}_{ij})_{j \geq 0}$ of $B_{i}(P_{\bullet})$ and a projective
resolution $(X^{H}_{ij})_{j \geq 0}$ of $H_{i}(P_{\bullet})$, which are respectively equal to
$B^{I}_{i}(L_{\bullet,\bullet})$ and $H^{I}_{i}(L_{\bullet,\bullet})$; one deduces successively
$Z^{I}_{i}(L_{\bullet,\bullet}) = H^{I}_{i}(L_{\bullet,\bullet}) \oplus B^{I}_{i}(L_{\bullet,\bullet})$, then
$L_{i,\bullet} = Z^{I}_{i}(L_{\bullet,\bullet}) \oplus B^{I}_{i-1}(L_{\bullet,\bullet})$. That being so,
$X^{B}_{i,\bullet} \otimes_{A} A'$ is in general no longer a resolution of $B_{i}(P_{\bullet}) \otimes_{A} A'$, but it
is still a complex formed of *projective* $A'$-modules, and there is therefore an $A'$-homomorphism $X^{B}_{i,\bullet}
\otimes_{A} A' \to B^{I}_{i}(L'_{\bullet,\bullet})$ compatible with the augmentations, and determined up to homotopy
`(M, V, 1.1)`. One has similarly an $A'$-homomorphism $X^{H}_{i,\bullet} \otimes_{A} A' \to
H^{I}_{i}(L'_{\bullet,\bullet})$ determined up to homotopy, from which one deduces, by the construction recalled above,
an $A'$-homomorphism $L_{i,\bullet} \otimes_{A} A' \to L'_{i,\bullet}$ for every $i$; these homomorphisms (for $i \in
\mathbb{Z}$) are compatible with the differentials $L_{i,\bullet} \to L_{i-1,\bullet}$ and the analogous ones for
$L'_{i,\bullet}$, by virtue of the same construction, and they therefore constitute the desired $A'$-homomorphism
$L_{\bullet,\bullet} \otimes_{A} A' \to L'_{\bullet,\bullet}$.

To define `(6.3.8.1)`, it then suffices to consider similarly a Cartan–Eilenberg projective resolution
$M_{\bullet,\bullet}$ (resp. $M'_{\bullet,\bullet}$) of $Q_{\bullet}$ (resp. $Q_{\bullet} \otimes_{A} A'$), and an
$A'$-homomorphism $M_{\bullet,\bullet} \otimes_{A} A' \to M'_{\bullet,\bullet}$. From these homomorphisms one deduces an
$A'$-homomorphism $(L_{\bullet,\bullet} \otimes_{A} A') \otimes_{A'} (M_{\bullet,\bullet} \otimes_{A} A') \to
L'_{\bullet,\bullet} \otimes_{A'} M'_{\bullet,\bullet}$, then by composition an $A$-homomorphism of bicomplexes
$L_{\bullet,\bullet} \otimes_{A} M_{\bullet,\bullet} \to L'_{\bullet,\bullet} \otimes_{A'} M'_{\bullet,\bullet}$, and on
passing to homology one obtains `(6.3.8.1)`, which is well defined since it comes from a morphism of complexes defined
up to homotopy.

If $\rho' : A' \to A''$ is a second homomorphism of rings, and $\rho'' : A \to A''$ the composite homomorphism $\rho'
\circ \rho$, it is clear that $\rho''_{P_{\bullet}, Q_{\bullet}} = \rho'_{P'_{\bullet}, Q'_{\bullet}} \circ
\rho_{P_{\bullet}, Q_{\bullet}}$, where $P'_{\bullet} = P_{\bullet} \otimes_{A} A'$, $Q'_{\bullet} = Q_{\bullet}
\otimes_{A} A'$.

Note further that the morphism of bicomplexes $L_{\bullet,\bullet} \otimes_{A} M_{\bullet,\bullet} \to
L'_{\bullet,\bullet} \otimes_{A'} M'_{\bullet,\bullet}$ considered above defines functorial morphisms (in $P_{\bullet}$
and $Q_{\bullet}$) of spectral sequences

```text
  'E_{pq}^r(P_•, Q_•) → 'E_{pq}^r(P_• ⊗_A A', Q_• ⊗_A A')
  ''E_{pq}^r(P_•, Q_•) → ''E_{pq}^r(P_• ⊗_A A', Q_• ⊗_A A'),
```

independent of the Cartan–Eilenberg resolutions considered, and having also the preceding transitivity property.

**Proposition (6.3.9).**

<!-- label: III.6.3.9 -->

*Let $\rho : A \to A'$ be a homomorphism of rings such that $A'$ is a flat $A$-module. Then one has functorial canonical
isomorphisms*

```text
  Tor_•^{A'}(P_• ⊗_A A', Q_• ⊗_A A') ⥲ Tor_•^A(P_•, Q_•) ⊗_A A'                 (6.3.9.1)
  'E(P_• ⊗_A A', Q_• ⊗_A A') ⥲ 'E(P_•, Q_•) ⊗_A A'                              (6.3.9.2)
  ''E(P_• ⊗_A A', Q_• ⊗_A A') ⥲ ''E(P_•, Q_•) ⊗_A A'.
```

<!-- original page 145 -->

**Proof.** Indeed, given the exactness of the functor $M \otimes_{A} A'$ in $M$, $L_{\bullet,\bullet} \otimes_{A} A'$
and $M_{\bullet,\bullet} \otimes_{A} A'$ are then Cartan–Eilenberg projective resolutions of $P_{\bullet} \otimes_{A}
A'$ and $Q_{\bullet} \otimes_{A} A'$ respectively, whence the conclusion.

**6.3.10.**

<!-- label: III.6.3.10 -->

Let $\rho : A \to A'$ be a homomorphism of rings; for every complex $P'_{\bullet}$ of $A'$-modules,
$P'_{\bullet,[\rho]}$ is a complex of $A$-modules; moreover, the identity application $P'_{\bullet,[\rho]} \to
P'_{\bullet}$ can be considered as composed of the canonical applications

```text
  P'_{•,[ρ]} → P'_{•,[ρ]} ⊗_A A' →^μ P'_•,
```

where $\mu$ is the $A'$-homomorphism $\mu(x \otimes a') = a' x$. If $Q'_{\bullet}$ is a second complex of $A'$-modules,
one has therefore canonical functorial homomorphisms of degree `0`

```text
  Tor_•^A(P'_{•,[ρ]}, Q'_{•,[ρ]}) → Tor_•^{A'}(P'_{•,[ρ]} ⊗_A A', Q'_{•,[ρ]} ⊗_A A')
                                  → Tor_•^{A'}(P'_•, Q'_•)                      (6.3.10.1)
```

where the first arrow is the $A$-homomorphism defined in `(6.3.8)` and the second is deduced from the $A'$-homomorphisms
$P'_{\bullet,[\rho]} \otimes_{A} A' \to P'_{\bullet}$ and $Q'_{\bullet,[\rho]} \otimes_{A} A' \to Q'_{\bullet}$ by
functoriality. One has analogous homomorphisms for the spectral sequences of `(6.3.2)`, and obvious transitivity
properties, which we leave to the reader to state.

**Proposition (6.3.11).**

<!-- label: III.6.3.11 -->

*Let $\rho : A \to A'$ be a homomorphism of rings making $A'$ a flat $A$-module. For every complex $P'_{\bullet}$ of
$A'$-modules and every complex $Q_{\bullet}$ of $A$-modules bounded below, one has a functorial canonical isomorphism*

```text
  Tor_•^A(P'_{•,[ρ]}, Q_•) ⥲ Tor_•^{A'}(P'_•, Q_• ⊗_A A').                      (6.3.11.1)
```

**Proof.** Indeed, if $M_{\bullet,\bullet}$ is a Cartan–Eilenberg projective resolution of $Q_{\bullet}$,
$M_{\bullet,\bullet} \otimes_{A} A'$ is a Cartan–Eilenberg projective resolution of $Q_{\bullet} \otimes_{A} A'$, and
one has, up to a canonical isomorphism, $P'_{\bullet,[\rho]} \otimes_{A} M_{\bullet,\bullet} = P'_{\bullet} \otimes_{A'}
(M_{\bullet,\bullet} \otimes_{A} A')$; the conclusion follows from `(6.3.4)`.

**Remark (6.3.12).**

<!-- label: III.6.3.12 -->

Let $(A^{\lambda})$ be a filtered inductive system of rings, and let $(P^{\lambda}_{\bullet})$,
$(Q^{\lambda}_{\bullet})$ be two inductive systems of complexes of $(A^{\lambda})$-modules; one then has a canonical
isomorphism generalizing `(6.3.6.1)`

```text
  lim_→ Tor_•^{A^λ}(P_•^λ, Q_•^λ) ⥲ Tor_•^A(P_•, Q_•)                            (6.3.12.1)
```

where $A = \varinjlim A^{\lambda}$, $P_{\bullet} = \varinjlim P^{\lambda}_{\bullet}$, $Q_{\bullet} = \varinjlim
Q^{\lambda}_{\bullet}$. Once the homomorphisms

```text
  Tor_•^{A^λ}(P_•^λ, Q_•^λ) → Tor_•^{A^μ}(P_•^μ, Q_•^μ)
```

for $\lambda \leq \mu$ are defined, with the help of `(6.3.10)`, the proof is that of `(6.3.6)`.

**Proposition (6.3.13).**

<!-- label: III.6.3.13 -->

*Let $S$ be a multiplicative subset of $A$, $P_{\bullet}$ and $Q_{\bullet}$ two complexes of $A$-modules in which the
homotheties defined by the elements of $S$ are bijective, so that, if $A' = S^{-1} A$, $P_{\bullet}$ and $Q_{\bullet}$
are formed of $A'$-modules. Then one has a canonical isomorphism $Tor^{A}_{\bullet}(P_{\bullet}, Q_{\bullet})
\xrightarrow{\sim} Tor^{A'}_{\bullet}(P_{\bullet}, Q_{\bullet})$.*

**Proof.** Indeed, the hypothesis implies that the canonical homomorphisms $P_{\bullet} \to P_{\bullet} \otimes_{A} A'$,
$Q_{\bullet} \to Q_{\bullet} \otimes_{A} A'$ are bijective. On the other hand, the functoriality of the hypertor shows
that every $s \in S$ defines a bijective homothety in $Tor^{A}_{\bullet}(P_{\bullet}, Q_{\bullet})$, and consequently

```text
  Tor_•^A(P_•, Q_•) → Tor_•^A(P_•, Q_•) ⊗_A A'
```

<!-- original page 146 -->

is also a bijective homomorphism. Since $A'$ is a flat $A$-module, the conclusion follows from `(6.3.9)`, and one has
similarly canonical isomorphisms for the spectral sequences.

## 6.4. Local hypertor functors of complexes of quasi-coherent modules: case of affine schemes.

**6.4.1.**

<!-- label: III.6.4.1 -->

Let $S$ be an affine scheme with ring $A$, and $X$, $Y$ two affine $S$-schemes with rings $B$, $C$ respectively, so that
$B$ and $C$ are algebras over $A$. Every complex $\mathcal{P}_{\bullet}$ (resp. $\mathcal{Q}_{\bullet}$) of
quasi-coherent $\mathcal{O}_{X}$-modules (resp. $\mathcal{O}_{Y}$-modules) is of the form $\tilde{P}_{\bullet}$ (resp.
$\tilde{Q}_{\bullet}$), where $P_{\bullet}$ (resp. $Q_{\bullet}$) is a complex of $B$-modules (resp. $C$-modules)
`(I, 1.3.7 and 1.3.8)`. One may obviously consider $P_{\bullet}$ and $Q_{\bullet}$ as complexes of $A$-modules and form
the $Tor^{A}_{n}(P_{\bullet}, Q_{\bullet})$; furthermore, by virtue of the bifunctorial character of
$Tor^{A}_{n}(P_{\bullet}, Q_{\bullet})$, the $A$-algebras $B$ and $C$ operate on this $A$-module, and these operations
make it a $(B, C)$-bimodule, or, equivalently, a module over $B \otimes_{A} C = A(X \times_{S} Y)$. One has thereby
defined a quasi-coherent $\mathcal{O}_{X\times_{S} Y}$-module

```text
  𝒯or_n^{𝒪_S}(𝒫_•, 𝒬_•) = (Tor_n^A(P_•, Q_•))~                                   (6.4.1.1)
```

which is called the *local hypertor of index* $n$ of the complexes $\mathcal{P}_{\bullet}$ and $\mathcal{Q}_{\bullet}$,
and which is also denoted $\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$.

**Lemma (6.4.2).**

<!-- label: III.6.4.2 -->

*With the notations of `(6.4.1)`, suppose that the ring $A$ is of the form $R^{-1} A'$, where $A'$ is a ring and $R$ a
multiplicative subset of $A'$. Let $S' = \operatorname{Spec}(A')$, so that $X$ and $Y$ may be considered as
$S'$-preschemes and one has $X \times_{S'} Y = X \times_{S} Y$ `(I, 1.6.2 and 3.2.4)`. Then one has
$\mathcal{T}or^{S'}_{\bullet}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet}) =
\mathcal{T}or^{S}_{\bullet}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$.*

**Proof.** This follows from formula `(6.4.1.1)` and from `(6.3.13)`.

**6.4.3.**

<!-- label: III.6.4.3 -->

With the notations and hypotheses of `(6.4.1)`, let $\mathcal{F} = \tilde{F}$ be a quasi-coherent
$\mathcal{O}_{X}$-module, $\mathcal{G} = \tilde{G}$ a quasi-coherent $\mathcal{O}_{Y}$-module; considering $\mathcal{F}$
and $\mathcal{G}$ as complexes of modules, one will denote by $\mathcal{T}or^{S}_{n}(\mathcal{F}, \mathcal{G})$ or
$\mathcal{T}or^{\mathcal{O}_{S}}_{n}(\mathcal{F}, \mathcal{G})$ their hypertor of index $n$; it follows from
`(6.3.5, (ii))` that one has

```text
  𝒯or_n^{𝒪_S}(ℱ, 𝒢) = (Tor_n^A(F, G))~.                                          (6.4.3.1)
```

Returning now to the general case of two complexes of quasi-coherent modules $\mathcal{P}_{\bullet}$,
$\mathcal{Q}_{\bullet}$, formulas `(6.4.1.1)` and `(6.4.3.1)` show, taking into account Prop. `(6.3.2)`, that
$\mathcal{T}or^{S}_{\bullet}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ is the abutment of two spectral sequences
$'\mathcal{E}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$, $''\mathcal{E}(\mathcal{P}_{\bullet},
\mathcal{Q}_{\bullet})$, whose `E_2` terms are given by

```text
  'ℰ_{pq}^2 = ℋ_p(𝒯or_q^S(𝒫_•, 𝒬_•))                                            (6.4.3.2)
  ''ℰ_{pq}^2 = ⊕_{q'+q''=q} 𝒯or_p^S(ℋ_{q'}(𝒫_•), ℋ_{q''}(𝒬_•))                   (6.4.3.3)
```

where $\mathcal{T}or^{S}_{q}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ is the bicomplex of quasi-coherent
$\mathcal{O}_{X\times_{S} Y}$-modules $\mathcal{T}or^{S}_{q}(\mathcal{P}_{i}, \mathcal{Q}_{j})$.

**6.4.4.**

<!-- label: III.6.4.4 -->

Consider now two further affine schemes $X^{(1)} = \operatorname{Spec}(B^{(1)})$, $Y^{(1)} =
\operatorname{Spec}(C^{(1)})$, where $B^{(1)}$ and $C^{(1)}$ are $A$-algebras, and suppose given two

<!-- original page 147 -->

$S$-morphisms $u : X^{(1)} \to X$, $v : Y^{(1)} \to Y$, corresponding to $A$-homomorphisms $\phi : B \to B^{(1)}$,
$\psi : C \to C^{(1)}$. Consider the complexes $u^{*}(\mathcal{P}_{\bullet}) = (P_{\bullet} \otimes_{B} B^{(1)})~$ of
$\mathcal{O}_{X^{(1)}}$-modules, $v^{*}(\mathcal{Q}_{\bullet}) = (Q_{\bullet} \otimes_{C} C^{(1)})~$ of
$\mathcal{O}_{Y^{(1)}}$-modules. The canonical $A$-homomorphisms

```text
  P_• → P_• ⊗_B B^{(1)},   Q_• → Q_• ⊗_C C^{(1)}
```

give by functoriality an $A$-homomorphism

```text
  Tor_•^A(P_•, Q_•) → Tor_•^A(P_• ⊗_B B^{(1)}, Q_• ⊗_C C^{(1)});
```

moreover, again by functoriality, this homomorphism is in fact a homomorphism of $(B \otimes_{A} C)$-modules. From this
one concludes that one has thereby defined a $(u \times_{S} v)$-morphism

```text
  θ : 𝒯or_•^S(𝒫_•, 𝒬_•) → 𝒯or_•^S(u^*(𝒫_•), v^*(𝒬_•))                            (6.4.4.1)
```

and consequently, a homomorphism of $\mathcal{O}_{X^{(1)} \times_{S} Y^{(1)}}$-modules

```text
  θ^♯ : (u ×_S v)^*(𝒯or_•^S(𝒫_•, 𝒬_•)) → 𝒯or_•^S(u^*(𝒫_•), v^*(𝒬_•))             (6.4.4.2)
```

which is evidently a morphism of bi-$\partial$-functors in the categories of quasi-coherent modules bounded below.

The homomorphism `(6.4.4.2)` is not necessarily bijective; however:

**Lemma (6.4.5).**

<!-- label: III.6.4.5 -->

*With the notations of `(6.4.4)`, suppose that $u$ and $v$ are open immersions; then the homomorphism `(6.4.4.2)` is
bijective.*

**Proof.** Identify $X^{(1)}$ (resp. $Y^{(1)}$) with an open subset of $X$ (resp. $Y$); $X^{(1)}$ (resp. $Y^{(1)}$) is
then a union of open sets of the form $D(f)$ (resp. $D(g)$), where $f \in B$ (resp. $g \in C$), and the induced
preschemes $D(\phi(f))$ and $D(f)$ (resp. $D(\psi(g))$ and $D(g)$) are isomorphic. It will suffice to prove the lemma
when $X^{(1)}$ (resp. $Y^{(1)}$) is of the form $D(f)$ (resp. $D(g)$); indeed, if this point is established, and if one
returns to the general case, it suffices to prove that the restriction of $\theta^{\sharp}$ to each open set $D(f)
\times_{S} D(g)$ is an isomorphism; now, if $u_{1} : D(f) \to X^{(1)}$, $v_{1} : D(g) \to Y^{(1)}$ are the canonical
injections, the preceding restriction is none other than $(u_{1} \times_{S} v_{1})^{*}(\theta^{\sharp})$; but it is
immediate, by virtue of definitions `(6.4.4)` and $(0_{I}, 4.4.8)$, that on composing it with the canonical homomorphism

```text
  (u_1 ×_S v_1)^*(𝒯or_•^S(u^*(𝒫_•), v^*(𝒬_•))) → 𝒯or_•^S(u'^*(𝒫_•), v'^*(𝒬_•))   (6.4.5.1)
```

where $u' = u \circ u_{1}$ and $v' = v \circ v_{1}$, one obtains the canonical homomorphism

```text
  (u' ×_S v')^*(𝒯or_•^S(𝒫_•, 𝒬_•)) → 𝒯or_•^S(u'^*(𝒫_•), v'^*(𝒬_•))               (6.4.5.2)
```

and if one knows that `(6.4.5.1)` and `(6.4.5.2)` are isomorphisms, it will follow that the same holds for $(u_{1}
\times_{S} v_{1})^{*}(\theta^{\sharp})$.

Suppose then that $X^{(1)} = D(f)$ and $Y^{(1)} = D(g)$, so that $B^{(1)} = B_{f}$ and $C^{(1)} = C_{g}$;
$u^{*}(\mathcal{P}_{\bullet})$ (resp. $v^{*}(\mathcal{Q}_{\bullet})$) is then identified with $(P_{\bullet})~_{f}$
(resp. $(Q_{\bullet})~_{g}$); on the other hand, $X^{(1)} \times_{S} Y^{(1)}$ is identified with the open subscheme $D(f
\otimes g)$ of $X \times_{S} Y = \operatorname{Spec}(B \otimes_{A} C)$ `(II, 4.3.2.4)`; it is a matter of proving that
the homomorphism

```text
  (Tor_•^A(P_•, Q_•))_{f ⊗ g} → Tor_•^A((P_•)_f, (Q_•)_g)                       (6.4.5.3)
```

<!-- original page 148 -->

deduced by functoriality from the canonical homomorphisms $P_{\bullet} \to (P_{\bullet})_{f}$, $Q_{\bullet} \to
(Q_{\bullet})_{g}$, is bijective. Now $(0_{I}, 1.6.1)$, one may write $(P_{\bullet})_{f} = \varinjlim
P^{(n)}_{\bullet}$, where the $P^{(n)}_{\bullet}$ are all complexes of $B$-modules identical to $P_{\bullet}$, the
application $P^{(m)}_{\bullet} \to P^{(n)}_{\bullet}$ for $m \leq n$ being multiplication by $f^{n-m}$; one has an
analogous result for $Q_{\bullet}$ replacing $f$ by $g$; on the other hand, it is clear that the homomorphism

```text
  Tor_•^A(P_•^{(m)}, Q_•^{(m)}) → Tor_•^A(P_•^{(n)}, Q_•^{(n)})
```

corresponding to the homomorphisms $P^{(m)}_{\bullet} \to P^{(n)}_{\bullet}$ and $Q^{(m)}_{\bullet} \to
Q^{(n)}_{\bullet}$ is by definition multiplication by $(f \otimes g)^{n-m}$. The conclusion follows from $(0_{I},
1.6.1)$ applied to the first member of `(6.4.5.3)` and from `(6.3.6)`.

**6.4.6.**

<!-- label: III.6.4.6 -->

With the notations of `(6.4.4)`, one defines similarly canonical homomorphisms of spectral functors

```text
  (u ×_S v)^*('ℰ(𝒫_•, 𝒬_•)) → 'ℰ(u^*(𝒫_•), v^*(𝒬_•))                              (6.4.6.1)
  (u ×_S v)^*(''ℰ(𝒫_•, 𝒬_•)) → ''ℰ(u^*(𝒫_•), v^*(𝒬_•))
```

and the reasoning of `(6.4.5)` shows that when $u$ and $v$ are *open immersions*, the homomorphisms `(6.4.6.1)` are
bijective: indeed, taking into account `(6.3.6.2)` and `(6.3.6.3)`, it proves that it is an isomorphism on the `E_2`
terms, and `(6.4.5)` shows that it is an isomorphism on the abutments; one concludes therefore with the help of
$(0_{III}, 11.1.2)$ and $(0_{III}, 11.2.4)$.

## 6.5. Local hypertor functors of complexes of quasi-coherent modules: general case.

**6.5.1.**

<!-- label: III.6.5.1 -->

Consider now an arbitrary prescheme $S$ and two arbitrary $S$-preschemes $X$, $Y$; let $\mathcal{P}_{\bullet}$ (resp.
$\mathcal{Q}_{\bullet}$) be a complex of quasi-coherent $\mathcal{O}_{X}$-modules (resp. $\mathcal{O}_{Y}$-modules). Set
$Z = X \times_{S} Y$; we are going to define quasi-coherent $\mathcal{O}_{Z}$-modules
$\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$, called the *local hypertor* of
$\mathcal{P}_{\bullet}$ and $\mathcal{Q}_{\bullet}$, which reduce to those already defined in `(6.4)` when $S$, $X$, and
$Y$ are affine.

When $\mathcal{P}_{\bullet}$ and $\mathcal{Q}_{\bullet}$ reduce respectively to their terms of degree `0`, $\mathcal{F}$
and $\mathcal{G}$ (the others being zero), one will write $\mathcal{T}or^{S}_{n}(\mathcal{F}, \mathcal{G})$ instead of
$\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$.

**6.5.2.**

<!-- label: III.6.5.2 -->

Suppose first that $S$ is affine, and let $(X_{\lambda})$, $(Y_{\mu})$ be covers of $X$ and $Y$ respectively by affine
open sets; then the $Z_{\lambda \mu} = X_{\lambda} \times_{S} Y_{\mu}$ form an affine open cover of $Z$. Set
$\mathcal{P}_{\lambda,\bullet} = \mathcal{P}_{\bullet}|X_{\lambda}$, $\mathcal{Q}_{\mu,\bullet} =
\mathcal{Q}_{\bullet}|Y_{\mu}$; we have therefore for every pair $(\lambda, \mu)$ a quasi-coherent
$\mathcal{O}_{Z_{\lambda \mu}}$-module $\mathcal{F}_{\lambda \mu} = \mathcal{T}or^{S}_{n}(\mathcal{P}_{\lambda,\bullet},
\mathcal{Q}_{\mu,\bullet})$, and it must be shown that the $\mathcal{F}_{\lambda \mu}$ satisfy the gluing condition
$(0_{I}, 3.3.1)$. For this, it suffices to verify that for every affine open set $U \subset X_{\lambda} \cap
X_{\lambda'}$ (resp. $V \subset Y_{\mu} \cap Y_{\mu'}$), the restrictions of $\mathcal{F}_{\lambda \mu}$ and
$\mathcal{F}_{\lambda'\mu'}$ to $U \times_{S} V$ are canonically isomorphic; but this follows at once from the existence
of canonical isomorphisms of these restrictions onto $\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet}|U,
\mathcal{Q}_{\bullet}|V)$ `(6.4.5)`. Moreover, it follows at once from this definition and from `(6.4.5)` that the
$\mathcal{O}_{Z}$-module so defined does not depend (up to isomorphism) on the open covers $(X_{\lambda})$, $(Y_{\mu})$
considered;

<!-- original page 149 -->

we shall therefore denote it $\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$; it follows finally
from `(6.4.5)` that for *every* open subset $U$ (resp. $V$) of $X$ (resp. $Y$), the restriction of
$\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ to $U \times_{S} V$ is canonically isomorphic to
$\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet}|U, \mathcal{Q}_{\bullet}|V)$.

**6.5.3.**

<!-- label: III.6.5.3 -->

Passing now to the general case where $S$ is arbitrary, let $(S_{\alpha})$ be a cover of $S$ formed of affine open sets;
denote by $X_{\alpha}$ (resp. $Y_{\alpha}$) the inverse image of $S_{\alpha}$ in $X$ (resp. $Y$); it still must be
proved that the sheaves $\mathcal{T}or^{S_{\alpha}}_{n}(\mathcal{P}_{\bullet}|X_{\alpha},
\mathcal{Q}_{\bullet}|Y_{\alpha}) = \mathcal{G}_{\alpha}$ satisfy the gluing condition. It suffices to define, for every
affine open set $T$ contained in $S_{\alpha} \cap S_{\beta}$, canonical isomorphisms of the restrictions of
$\mathcal{G}_{\alpha}$ and $\mathcal{G}_{\beta}$ to $U \times_{S} V$ (where $U$ and $V$ denote the inverse images of $T$
in $X$ and $Y$ respectively) onto $\mathcal{T}or^{T}_{n}(\mathcal{P}_{\bullet}|U, \mathcal{Q}_{\bullet}|V)$; one may, in
addition, restrict to the case where $T$ is written as both $D(f_{\alpha})$ and $D(f_{\beta})$, $f_{\alpha}$ (resp.
$f_{\beta}$) being a section of $\mathcal{O}_{S}$ over $S_{\alpha}$ (resp. $S_{\beta}$); but then
$\mathcal{T}or^{T}_{n}(\mathcal{P}_{\bullet}|U, \mathcal{Q}_{\bullet}|V)$ is canonically isomorphic to
$\mathcal{T}or^{S_{\alpha}}_{n}(\mathcal{P}_{\bullet}|U, \mathcal{Q}_{\bullet}|V)$ on the one hand, and to
$\mathcal{T}or^{S_{\beta}}_{n}(\mathcal{P}_{\bullet}|U, \mathcal{Q}_{\bullet}|V)$ on the other, by virtue of `(6.4.2)`;
since one has just defined canonical isomorphisms of $\mathcal{G}_{\alpha}$ onto
$\mathcal{T}or^{S_{\alpha}}_{n}(\mathcal{P}_{\bullet}|U, \mathcal{Q}_{\bullet}|V)$ and of $\mathcal{G}_{\beta}$ onto
$\mathcal{T}or^{S_{\beta}}_{n}(\mathcal{P}_{\bullet}|U, \mathcal{Q}_{\bullet}|V)$ `(6.5.2)`, this completes the
definition of the $\mathcal{O}_{Z}$-module $\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$.
Moreover, for every open subset $U$ (resp. $V$) of $X$ (resp. $Y$), $\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet}|U,
\mathcal{Q}_{\bullet}|V)$ is canonically isomorphic to the restriction of $\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet},
\mathcal{Q}_{\bullet})$ to $U \times_{S} V$.

It is immediate that one has thereby defined (in the categories of complexes of quasi-coherent modules bounded below) a
bi-$\partial$-functor $\mathcal{T}or^{S}_{\bullet}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ with values in the
category of $\mathcal{O}_{Z}$-modules, for it is clear that the question is local on $X$, $Y$, and $S$, by virtue of
`(6.4.5)` and of the remark that `(6.4.4.2)` is a morphism of bi-$\partial$-functors. Note that if
$\mathcal{P}_{\bullet}$ and $\mathcal{Q}_{\bullet}$ are reduced respectively to their terms of degree `0`, $\mathcal{F}$
and $\mathcal{G}$, $\mathcal{T}or^{S}_{0}(\mathcal{F}, \mathcal{G})$ is none other, by virtue of `(6.4.1.1)`, than the
external tensor product $\mathcal{F} \otimes_{S} \mathcal{G}$ defined in `(I, 9.1.2)`; this follows indeed from
`(I, 9.1.3)`.

**6.5.4.**

<!-- label: III.6.5.4 -->

It follows from the preceding construction and from the remarks made in `(6.4.6)` that
$\mathcal{T}or^{S}_{\bullet}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ is the abutment of two spectral functors
$'\mathcal{E}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$, $''\mathcal{E}(\mathcal{P}_{\bullet},
\mathcal{Q}_{\bullet})$, with `E_2` terms equal to

```text
  'ℰ_{pq}^2 = ℋ_p(𝒯or_q^S(𝒫_•, 𝒬_•))                                            (6.5.4.1)
  ''ℰ_{pq}^2 = ⊕_{q'+q''=q} 𝒯or_p^S(ℋ_{q'}(𝒫_•), ℋ_{q''}(𝒬_•)).                  (6.5.4.2)
```

The spectral sequence `(6.5.4.2)` is always regular; the two spectral sequences are biregular if $\mathcal{P}_{\bullet}$
and $\mathcal{Q}_{\bullet}$ are bounded below. Another case where the two preceding sequences are biregular is the
following:

**6.5.5.**

<!-- label: III.6.5.5 -->

We shall say that on a topological space $T$ a sheaf of rings $\mathcal{A}$ is *of cohomological dimension $\leq n$* if,
for every $t \in T$, the ring $\mathcal{A}_{t}$ is of cohomological dimension $\leq n$; one then also says that the
*ringed space* $(T, \mathcal{A})$ is *of cohomological dimension $\leq n$*. One says that a sheaf of rings (resp. a
ringed space) is of *finite* cohomological dimension if there exists an integer $n$ such that it is of cohomological
dimension $\leq n$. Note that if the $\mathcal{A}_{t}$ are *noetherian (commutative) local* rings,

<!-- original page 150 -->

to say that they are of cohomological dimension $\leq n$ means that they are *regular* and of (Krull) dimension $\leq n$
$(0_{IV}, 17.3.1)$. With the terminology of dimension theory that we shall introduce in chap. IV, it is equivalent to
say that a locally noetherian prescheme $T$ is of cohomological dimension $\leq n$, or to say that it is *regular*
$(0_{I}, 4.1.4)$ and of dimension $\leq n$; this means that for every affine open $U$ of $T$, the ring $\Gamma(U,
\mathcal{O}_{T})$ is of cohomological dimension $\leq n$ $(0_{IV}, 17.2.6)$. That being so, this last remark, joined to
`(6.3.2)`, proves that *if $S$ is locally noetherian and of finite cohomological dimension, the spectral sequences
$'\mathcal{E}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ and $''\mathcal{E}(\mathcal{P}_{\bullet},
\mathcal{Q}_{\bullet})$ are biregular.*

It is clear that $\mathcal{T}or^{S}_{\bullet}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ is transformed into
$\mathcal{T}or^{S}_{\bullet}(\mathcal{Q}_{\bullet}, \mathcal{P}_{\bullet})$ (up to isomorphism) by the canonical
isomorphism of $X \times_{S} Y$ onto $Y \times_{S} X$.

**Proposition (6.5.6).**

<!-- label: III.6.5.6 -->

*Let $(\mathcal{P}_{\alpha,\bullet})$ be a filtered inductive system of complexes of quasi-coherent
$\mathcal{O}_{X}$-modules; then there exists a canonical isomorphism*

```text
  lim_→ (𝒯or_•^S(𝒫_{α,•}, 𝒬_•)) ⥲ 𝒯or_•^S(lim_→ 𝒫_{α,•}, 𝒬_•).                   (6.5.6.1)
```

**Proof.** The question being local on $S$, $X$, and $Y$, one may suppose $S$, $X$, $Y$ affine, and the proposition then
reduces to `(6.3.6)`.

**Remarks (6.5.7).**

<!-- label: III.6.5.7 -->

*(i)* Consider in particular the case where $S = X = Y$, $\mathcal{P}_{\bullet}$ and $\mathcal{Q}_{\bullet}$ being thus
two complexes of quasi-coherent $\mathcal{O}_{S}$-modules; then the $\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet},
\mathcal{Q}_{\bullet})$ are quasi-coherent $\mathcal{O}_{S}$-modules; moreover, for every point $z \in S$, it follows
from `(6.5.6)` that one has a canonical isomorphism

```text
  (𝒯or_n^S(𝒫_•, 𝒬_•))_z ⥲ Tor_n^{𝒪_z}((𝒫_•)_z, (𝒬_•)_z)                          (6.5.7.1)
```

since the question is local and one is reduced to the case of modules, by virtue of `(6.4.1.1)`.

*(ii)* One may generalize the definition of hypertor to the case of two complexes of $\mathcal{O}_{X}$-modules
$\mathcal{P}_{\bullet}$, $\mathcal{Q}_{\bullet}$ on the same ringed space $(X, \mathcal{O}_{X})$; for every open subset
$U$ of $X$, set indeed $A(U) = \Gamma(U, \mathcal{O}_{X})$, $P_{\bullet}(U) = \Gamma(U, \mathcal{P}_{\bullet})$,
$Q_{\bullet}(U) = \Gamma(U, \mathcal{Q}_{\bullet})$; the $A(U)$-modules $Tor^{A(U)}_{n}(P_{\bullet}(U), Q_{\bullet}(U))$
then form a *presheaf* on $X$, and one denotes by $\mathcal{T}or^{X}_{n}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$
the $\mathcal{O}_{X}$-module associated with this presheaf. When $X$ is a prescheme, it follows from `(6.3.12)` that
this $\mathcal{O}_{X}$-module is canonically isomorphic to the hypertor defined above. We shall not develop this
generalization further.

**Proposition (6.5.8).**

<!-- label: III.6.5.8 -->

*Let $X$, $Y$ be two $S$-preschemes, $\mathcal{F}$ (resp. $\mathcal{G}$) a quasi-coherent $\mathcal{O}_{X}$-module
(resp. $\mathcal{O}_{Y}$-module). If $\mathcal{F}$ or $\mathcal{G}$ is $S$-flat, one has
$\mathcal{T}or^{S}_{n}(\mathcal{F}, \mathcal{G}) = 0$ for $n \neq 0$.*

**Proof.** The question being local on $X$ and $Y$, one may suppose $X$, $Y$, $S$ affine, with respective rings $B$,
$C$, $A$, and $\mathcal{F} = \tilde{M}$, $\mathcal{G} = \tilde{N}$, $M$ (resp. $N$) being a $B$-module (resp.
$C$-module). Suppose for example that $\mathcal{F}$ is $S$-flat, which means that for every $s \in S$, $M_{s}$ is a flat
$A_{s}$-module $(0_{I}, 6.7.1)$; consequently $M$ is a flat $A$-module $(0_{I}, 6.3.3)$, and one knows that
$Tor^{A}_{n}(M, N) = 0$ for $n > 0$ and for every $C$-module $N$ $(0_{I}, 6.1.1)$, whence

<!-- original page 151 -->

the conclusion by `(6.4.1.1)`.

**Corollary (6.5.9).**

<!-- label: III.6.5.9 -->

*Let $X$, $Y$ be two $S$-preschemes, $\mathcal{P}_{\bullet}$ (resp. $\mathcal{Q}_{\bullet}$) a complex of quasi-coherent
$\mathcal{O}_{X}$-modules (resp. $\mathcal{O}_{Y}$-modules) bounded below. Suppose that all the $\mathcal{P}_{i}$ are
$S$-flat. Then there exists a canonical isomorphism of $\partial$-functors in $\mathcal{Q}_{\bullet}$*

```text
  𝒯or_•^S(𝒫_•, 𝒬_•) ⥲ ℋ_•(𝒫_• ⊗_S 𝒬_•).                                         (6.5.9.1)
```

**Proof.** This is none other than `(6.3.7)` when $S$, $X$, $Y$ are affine; one passes from there to the general case by
the reasoning of `(6.5.2)` and `(6.5.3)`.

**Corollary (6.5.10).**

<!-- label: III.6.5.10 -->

*Suppose that $X$ is flat over $S$ $(0_{I}, 6.7.1)$, that $\mathcal{P}_{\bullet}$ and $\mathcal{Q}_{\bullet}$ are
bounded below, and that all the $\mathcal{P}_{i}$ are locally free $\mathcal{O}_{X}$-modules (not necessarily of finite
type). Then the homomorphism `(6.5.9.1)` is bijective.*

**Proof.** Indeed, the hypothesis of `(6.5.9)` is satisfied, since flatness is a pointwise property on $X$ by definition
and every direct sum of flat modules is a flat module $(0_{I}, 6.1.2)$.

**Proposition (6.5.11).**

<!-- label: III.6.5.11 -->

*Let $X'$, $Y'$ be two $S$-preschemes, $f : X \to X'$, $g : Y \to Y'$ two affine $S$-morphisms. Let
$\mathcal{P}_{\bullet}$ (resp. $\mathcal{Q}_{\bullet}$) be a complex of quasi-coherent $\mathcal{O}_{X}$-modules (resp.
$\mathcal{O}_{Y}$-modules); one then has a functorial canonical isomorphism*

```text
  (f ×_S g)_*(𝒯or_•^S(𝒫_•, 𝒬_•)) ⥲ 𝒯or_•^S(f_*(𝒫_•), g_*(𝒬_•)).                  (6.5.11.1)
```

**Proof.** Since $f$ and $g$ are affine, $f_{*}(\mathcal{P}_{\bullet})$ and $g_{*}(\mathcal{Q}_{\bullet})$ are complexes
of quasi-coherent modules `(II, 1.2.6)`, and if one sets $Z' = X' \times_{S} Y'$, the two members of `(6.5.11.1)` are
quasi-coherent $\mathcal{O}_{Z'}$-modules `(6.5.1)`; one reduces easily to the case where $S$, $X'$, and $Y'$ are
affine; but then it is also the case for $X$ and $Y$ by hypothesis, and the verification follows at once from
`(6.4.1.1)` and `(I, 1.6.3)`.

**Remark (6.5.12).**

<!-- label: III.6.5.12 -->

Let $X'$, $Y'$ be two $S$-preschemes and suppose that $X'$ is $S$-flat; let $X$ be a closed subprescheme of $X'$, $i : X
\to X'$ the canonical injection, $\mathcal{P}_{\bullet}$ (resp. $\mathcal{Q}_{\bullet}$) a complex of
$\mathcal{O}_{X}$-modules (resp. $\mathcal{O}_{Y'}$-modules) quasi-coherent, bounded below. Let finally
$\mathcal{L}'_{\bullet,\bullet}$ be a resolution of $i_{*}(\mathcal{P}_{\bullet})$ formed of locally free
$\mathcal{O}_{X'}$-modules, such that every point of $X'$ has an affine open neighborhood $U$ for which
$\mathcal{L}'_{\bullet,\bullet}|U$ is a free resolution of $i_{*}(\mathcal{P}_{j})|U$ for every $j$. One then has a
canonical isomorphism

```text
  (i ×_S 1)_*(𝒯or_•^S(𝒫_•, 𝒬_•)) ⥲ ℋ_•(ℒ'_{•,•} ⊗_S 𝒬_•).                         (6.5.12.1)
```

**Proof.** If $S$, $X'$, $Y'$ are affine and if $\mathcal{L}'_{j,\bullet}$ is a free resolution of
$i_{*}(\mathcal{P}_{j})$ for every $j$, one is reduced, by virtue of `(6.5.11)`, to the case where $X' = X$ is $S$-flat,
and it suffices to apply `(6.3.4)`. In the general case, one defines the isomorphism `(6.5.12.1)` locally, and it
remains to verify that this definition does give a global isomorphism. For this, one must refer to the definition of the
first isomorphism `(6.3.4.1)`, which comes from an isomorphism of spectral sequences $(0_{III}, 11.6.5 and 11.5.3)$,
obtained itself from a morphism of bicomplexes $L_{\bullet,\bullet} \to L'_{\bullet,\bullet}$, where
$L_{\bullet,\bullet}$ is the given resolution of $P_{\bullet}$, $L'_{\bullet,\bullet}$ a projective resolution of
$P_{\bullet}$ in the category of complexes of $A$-modules bounded below

<!-- original page 152 -->

(cf. $(0_{III}, 11.5.2.2)$); our assertion follows from the fact that the isomorphism `(6.3.4.1)` does not depend on the
chosen projective resolution $L'_{\bullet,\bullet}$, by virtue of the existence of a homotopism between two such
resolutions `(M, V, 1.2)`.

**Proposition (6.5.13).**

<!-- label: III.6.5.13 -->

*Let $X$, $Y$ be two $S$-preschemes, and suppose verified one of the following conditions:*

*(i)* $X$ *and* $Z = X \times_{S} Y$ *are locally noetherian and* $X$ *is flat over* $S$.

*(ii)* $S$ *and* $X$ *are locally noetherian and* $Y$ *is of finite type over* $S$.

*Let $\mathcal{P}_{\bullet}$ (resp. $\mathcal{Q}_{\bullet}$) be a complex of quasi-coherent $\mathcal{O}_{X}$-modules
(resp. $\mathcal{O}_{Y}$-modules), bounded below. Suppose in addition that, for every $n$,
$\mathcal{H}_{n}(\mathcal{P}_{\bullet})$ (resp. $\mathcal{H}_{n}(\mathcal{Q}_{\bullet})$) is a $\mathcal{O}_{X}$-module
(resp. $\mathcal{O}_{Y}$-module) of finite type. Then the $\mathcal{T}or^{S}_{n}(\mathcal{P}_{\bullet},
\mathcal{Q}_{\bullet})$ are coherent $\mathcal{O}_{Z}$-modules.*

**Proof.** Since $\mathcal{P}_{\bullet}$ and $\mathcal{Q}_{\bullet}$ are bounded below, the spectral sequence
$''\mathcal{E}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ is biregular `(6.5.4)`, and by virtue of $(0_{III},
11.1.8)$, it suffices (since in the two cases (i), (ii), $Z$ is locally noetherian) to prove that the terms
$''\mathcal{E}^{2}_{pq}$ are coherent. The hypothesis on the $\mathcal{H}_{n}(\mathcal{P}_{\bullet})$ and
$\mathcal{H}_{n}(\mathcal{Q}_{\bullet})$ and the expression `(6.5.4.2)` of the $''\mathcal{E}^{2}_{pq}$ therefore show
that the proposition is equivalent to its particular case corresponding to $\mathcal{P}_{\bullet}$ and
$\mathcal{Q}_{\bullet}$ reduced to their terms of degree `0`, in other words to its

**Corollary (6.5.14).**

<!-- label: III.6.5.14 -->

*Suppose verified one of the conditions (i), (ii) of `(6.5.13)`, and let $\mathcal{F}$ (resp. $\mathcal{G}$) be a
quasi-coherent $\mathcal{O}_{X}$-module (resp. $\mathcal{O}_{Y}$-module) of finite type; then the
$\mathcal{T}or^{S}_{n}(\mathcal{F}, \mathcal{G})$ are coherent $\mathcal{O}_{Z}$-modules.*

**Proof.** The question being local on $X$ and $Y$, one may suppose $S$, $X$, $Y$ affine.

*(i)* Under the hypotheses of (i), $S$, $X$, and $Z$ are noetherian. There therefore exists a locally free resolution
$\mathcal{L}_{\bullet}$ of $\mathcal{F}$ formed of $\mathcal{O}_{X}$-modules of finite type `(I, 1.3.7)`; since $X$ is
flat over $S$, it follows from `(6.3.4)` that one has $\mathcal{T}or^{S}_{\bullet}(\mathcal{F}, \mathcal{G}) =
\mathcal{H}_{\bullet}(\mathcal{L}_{\bullet} \otimes_{S} \mathcal{G})$; now, the $\mathcal{L}_{i} \otimes_{S}
\mathcal{G}$ are quasi-coherent $\mathcal{O}_{Z}$-modules of finite type `(I, 9.1.1)`, hence coherent. One concludes
that $\mathcal{H}_{\bullet}(\mathcal{L}_{\bullet} \otimes_{S} \mathcal{G})$ is coherent $(0_{I}, 5.3.4)$.

*(ii)* Suppose now that the conditions (ii) are verified. Since the ring $A(Y)$ is a quotient of an $A(S)$-algebra of
polynomials in a finite number of indeterminates `(I, 6.3.3)`, $Y$ is a closed sub-$S$-prescheme of an affine
$S$-prescheme $Y'$, flat and of finite type over $S$; $Y'$ being noetherian `(I, 6.3.7)`, there exists a locally free
resolution $\mathcal{M}_{\bullet}$ of $j_{*}(\mathcal{G})$ by $\mathcal{O}_{Y'}$-modules of finite type ($j : Y \to Y'$
being the canonical injection); by virtue of `(6.5.12)`, $\mathcal{T}or^{S}_{\bullet}(\mathcal{F}, \mathcal{G})$ is the
inverse image, by $1 \times j$, of the $\mathcal{O}_{Z'}$-module $\mathcal{H}_{\bullet}(\mathcal{F} \otimes_{S}
\mathcal{M}_{\bullet})$ (where $Z' = X \times_{S} Y'$); one sees as in (i) that the $\mathcal{F} \otimes_{S}
\mathcal{M}_{i}$ are coherent $\mathcal{O}_{Z'}$-modules, and one again draws the conclusion from $(0_{I}, 5.3.4)$.

**6.5.15.**

<!-- label: III.6.5.15 -->

The theory developed above for two complexes $\mathcal{P}_{\bullet}$, $\mathcal{Q}_{\bullet}$ of quasi-coherent sheaves
on two $S$-preschemes $X$, $Y$ generalizes without difficulty to the case where one considers an arbitrary finite number
of $S$-preschemes $X^{(i)}$ ($1 \leq i \leq m$) and on each $X^{(i)}$ a complex $\mathcal{P}^{(i)}_{\bullet}$ of
quasi-coherent $\mathcal{O}_{X^{(i)}}$-modules; if $Z = X^{(1)} \times_{S} X^{(2)} \times_{S} \cdots \times_{S}
X^{(m)}$, one defines in this way a quasi-coherent $\mathcal{O}_{Z}$-module
$\mathcal{T}or^{S}_{q}(\mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet}, \cdots, \mathcal{P}^{(m)}_{\bullet})$.
We leave to the reader the task of developing the theory in this general case, and we restrict ourselves to writing, for
later reference, the `E_2` term of the second (regular) spectral sequence whose abutment is
$\mathcal{T}or^{S}_{\bullet}(\mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet}, \cdots,
\mathcal{P}^{(m)}_{\bullet})$:

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

Consider an affine scheme $S = \operatorname{Spec}(A)$ and two quasi-compact $S$-schemes $X^{(i)}$ ($i = 1, 2$); let
$\mathcal{P}^{(i)}_{\bullet}$ be a complex of quasi-coherent $\mathcal{O}_{X^{(i)}}$-modules, *bounded below*, whose
differential is of degree $-1$ ($i = 1, 2$). Consider on the other hand a *finite* cover $\mathfrak{U}^{(i)} =
(U^{(i)}_{\alpha})$ of $X^{(i)}$ by affine open sets; let $X = X^{(1)} \times_{S} X^{(2)}$, which is a quasi-compact
$S$-scheme `(I, 5.5.1 and 6.6.4)`, and let $\mathfrak{U} = \mathfrak{U}^{(1)} \times_{S} \mathfrak{U}^{(2)}$ be the
cover of $X$ formed of the affine open sets $U^{(1)}_{\alpha} \times_{S} U^{(2)}_{\beta}$. For every pair of integers $p
\leq 0$, $q \in \mathbb{Z}$, the group of $(-p)$-alternating cochains $C^{-p}(\mathfrak{U}^{(i)},
\mathcal{P}^{(i)}_{q})$ of the cover $\mathfrak{U}^{(i)}$ with coefficients in the sheaf $\mathcal{P}^{(i)}_{q}$
`(G, II, 5.1)` is an $A$-module; for $p > 0$, one will set $C^{p}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{q}) = 0$; one
has thereby defined a bicomplex $C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet})$ of $A$-modules, whose
*two* differentials are of degree $-1$. It follows from definitions $(0_{III}, 12.1.2)$ that the homology $A$-module
$H_{n}(C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet}))$ of this bicomplex (considered as usual as a simple
complex for the total degree) is none other than the *hypercohomology $A$-module* $H^{-n}(\mathfrak{U}^{(i)},
\mathcal{P}^{(i)\bullet})$, where $\mathcal{P}^{(i)\bullet}$ is the complex with differential of degree `+1` obtained by
taking $\mathcal{P}^{(i)}_{q}$ as the component of degree $q$; by abuse of notation, we shall write it
$H^{-n}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet})$. It then follows from `(6.2.2)` that this $A$-module is
canonically isomorphic to the hypercohomology $A$-module $H^{-n}(X^{(i)}, \mathcal{P}^{(i)\bullet})$, which we shall
similarly write $H^{-n}(X^{(i)}, \mathcal{P}^{(i)}_{\bullet})$; it therefore does not depend on the chosen finite cover
$\mathfrak{U}^{(i)}$.

**6.6.2.**

<!-- label: III.6.6.2 -->

We shall apply to the two bicomplexes of $A$-modules

```text
  L_{•,•}^{(i)} = C^•(𝔘^{(i)}, 𝒫_•^{(i)})                            (i = 1, 2)
```

and to the covariant bifunctor $L^{(1)}_{\bullet,\bullet} \otimes_{A} L^{(2)}_{\bullet,\bullet}$ in these two
bicomplexes, the general theory of hyperhomology of functors with respect to bicomplexes $(0_{III}, 11.7.4)$. Since the
cochains considered are *alternating* and the covers $\mathfrak{U}^{(i)}$ finite, one will note that the modules
$C^{-p}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{q})$ are $\neq 0$ only for a *finite* number (independent of $q$) of
values of $p$, and in particular the two degrees of each of the $L^{(i)}_{\bullet,\bullet}$ are *bounded below*. We
shall denote by $Tor^{A}_{n}(L^{(1)}_{\bullet,\bullet}, L^{(2)}_{\bullet,\bullet})$ or $Tor^{S}_{n}(\mathfrak{U}^{(1)},
\mathfrak{U}^{(2)}; \mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$ the $n$-th hyperhomology module of
$L^{(1)}_{\bullet,\bullet} \otimes_{A} L^{(2)}_{\bullet,\bullet}$, which we shall call the *hypertor of index $n$* of
$\mathcal{P}^{(1)}_{\bullet}$ and $\mathcal{P}^{(2)}_{\bullet}$, *relative to the covers* $\mathfrak{U}^{(1)}$ *and*
$\mathfrak{U}^{(2)}$. When $\mathcal{P}^{(1)}_{\bullet}$ and $\mathcal{P}^{(2)}_{\bullet}$ are reduced to their terms of
degree `0`, $\mathcal{F}^{(1)}$ and $\mathcal{F}^{(2)}$, one writes $Tor^{S}_{n}(\mathfrak{U}^{(1)}, \mathfrak{U}^{(2)};
\mathcal{F}^{(1)}, \mathcal{F}^{(2)})$ for their hypertor. One will denote by $\mathcal{T}or^{S}_{n}(\mathfrak{U}^{(1)},
\mathfrak{U}^{(2)}; \mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$, following the general conventions, the
*bicomplex* whose component of indices $(j, k)$ is $Tor^{S}_{n}(\mathfrak{U}^{(1)}, \mathfrak{U}^{(2)};
\mathcal{P}^{(1)}_{j}, \mathcal{P}^{(2)}_{k})$.

Since $L^{(i)}_{\bullet,\bullet}$ is an exact functor in $\mathcal{P}^{(i)}_{\bullet}$, since the intersections of the
sets

<!-- original page 154 -->

of $\mathfrak{U}^{(i)}$ are affine `(I, 5.5.6 and 1.3.11)`, $Tor^{S}_{n}(\mathfrak{U}^{(1)}, \mathfrak{U}^{(2)};
\mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$ is a covariant bi-$\partial$-functor in
$\mathcal{P}^{(1)}_{\bullet}$, $\mathcal{P}^{(2)}_{\bullet}$, with values in the category of $A$-modules $(0_{III},
11.7.3)$. Moreover, one knows $(0_{III}, 11.7.2)$ that this bifunctor is the common abutment of *six* biregular spectral
functors, which we shall denote by ${}^{(t)}E(\mathfrak{U}^{(1)}, \mathfrak{U}^{(2)}; \mathcal{P}^{(1)}_{\bullet},
\mathcal{P}^{(2)}_{\bullet})$ or ${}^{(t)}E(\mathfrak{U}^{(1)}, \mathfrak{U}^{(2)}; \mathcal{P}^{(1)}_{\bullet},
\mathcal{P}^{(2)}_{\bullet})$, where $t$ must be replaced by one of the letters $a$, $b$, $a'$, $b'$, $c$, $d$, and
whose `E_2` terms are the following:

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

We have seen in `(6.6.1)` that the homology module $H_{n}(L^{(i)}_{\bullet,\bullet})$ of the bicomplex
$L^{(i)}_{\bullet,\bullet}$ was equal to $H^{-n}(X^{(i)}, \mathcal{P}^{(i)}_{\bullet})$; so

```text
  ^{(a)}E_{pq}^2 = ⊕_{q_1 + q_2 = q} Tor_p^A(H^{−q_1}(X^{(1)}, 𝒫_•^{(1)}), H^{−q_2}(X^{(2)}, 𝒫_•^{(2)})).
```

By definition, the complex $H^{I}_{n}(L^{(i)}_{\bullet,\bullet})$ has as term of degree $k$ the homology module
$H_{n}(C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{k}))$, that is, by definition, the cohomology module
$H^{-n}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{k})$; one knows `(1.4.1)` that this module is canonically isomorphic to
$H^{-n}(X^{(i)}, \mathcal{P}^{(i)}_{k})$; so

```text
  ^{(a')}E_{pq}^2 = ⊕_{q_1 + q_2 = q} Tor_p^A(H^{−q_1}(X^{(1)}, 𝒫_•^{(1)}), H^{−q_2}(X^{(2)}, 𝒫_•^{(2)})).
```

**6.6.4. Spectral sequences (b) and (b').**

<!-- label: III.6.6.4 -->

By definition, $Tor^{A, II}_{q}(L^{(1)}_{\bullet,\bullet}, L^{(2)}_{\bullet,\bullet})$ is a bicomplex whose term of
degree $(h, k)$ is the $A$-module

```text
  Tor_q^A(C^{−h}(𝔘^{(1)}, 𝒫_•^{(1)}), C^{−k}(𝔘^{(2)}, 𝒫_•^{(2)})).
```

Let $\Phi^{(i)}$ be the index set of $\mathfrak{U}^{(i)}$; by definition, the complex of modules
$C^{r}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet})$ ($r \geq 0$) is a direct sum of the complexes
$\Gamma(U^{(i)}_{\rho}, \mathcal{P}^{(i)}_{\bullet})$, where $U^{(i)}_{\rho}$ is the intersection of the $U^{(i)}_{\xi}$
for $\xi \in \rho$, and $\rho$ ranges over $\mathfrak{P}(\Phi^{(i)})$; so the $A$-module

```text
  Tor_q^A(C^{−h}(𝔘^{(1)}, 𝒫_•^{(1)}), C^{−k}(𝔘^{(2)}, 𝒫_•^{(2)}))
```

is the direct sum of the $A$-modules $Tor^{A}_{q}(\Gamma(U^{(1)}_{\sigma}, \mathcal{P}^{(1)}_{\bullet}),
\Gamma(U^{(2)}_{\tau}, \mathcal{P}^{(2)}_{\bullet}))$, where $\sigma$ (resp. $\tau$) ranges over the elements of
$\mathfrak{P}(\Phi^{(1)})$ (resp. $\mathfrak{P}(\Phi^{(2)})$) such that $Card(\sigma) = -(h+1)$ (resp. $Card(\tau) =
-(k+1)$). Since $X^{(1)}$ and $X^{(2)}$ are schemes, the $U^{(i)}_{\rho}$ are affine, so by `(6.4.1.1)` one has

```text
  Tor_q^A(Γ(U_σ^{(1)}, 𝒫_•^{(1)}), Γ(U_τ^{(2)}, 𝒫_•^{(2)})) = Γ(U_σ^{(1)} ×_S U_τ^{(2)}, 𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)})).
```

<!-- original page 155 -->

One sees therefore that ${}^{(b)}E^{2}_{pq}$ is the $(-p)$-th cohomology module of the complex $L^{\bullet}(\Phi^{(1)},
\Phi^{(2)}; \mathcal{S})$ of *bi-alternating* cochains on $\Phi^{(1)}$ and $\Phi^{(2)}$ with values in the system of
coefficients

```text
  𝒮 : (σ, τ) ↦ Γ(U_σ^{(1)} ×_S U_τ^{(2)}, 𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)}))
```

$(0_{III}, 11.8.4)$. One knows then $(0_{III}, 11.8.5 and 11.8.6)$ that the cohomology of this complex is the same as
that of the complex $C^{\bullet}(\Phi^{(1)}, \Phi^{(2)}; \mathcal{S})$ of *all* cochains on $\Phi^{(1)}$ and
$\Phi^{(2)}$ with values in $\mathcal{S}$, and also the same as that of the complex $P^{\bullet}(\Phi^{(1)}, \Phi^{(2)};
\mathcal{S})$, whose elements are linear combinations of the

```text
  λ(σ, τ) ∈ Γ(U_σ^{(1)} ×_S U_τ^{(2)}, 𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)}))
```

where $\sigma = (\alpha_{0}, \cdots, \alpha_{h})$ and $\tau = (\beta_{0}, \cdots, \beta_{h})$ are sequences having the
same number of elements. But one has then $U^{(1)}_{\sigma} \times_{S} U^{(2)}_{\tau} = (U^{(1)}_{\alpha_{0}} \times_{S}
U^{(2)}_{\beta_{0}}) \cap \cdots \cap (U^{(1)}_{\alpha_{h}} \times_{S} U^{(2)}_{\beta_{h}})$ `(I, 3.2.7)`. If one
denotes by $\mathfrak{U}$ the cover of $Z = X^{(1)} \times_{S} X^{(2)}$ by the affine open sets $U^{(1)}_{\alpha}
\times_{S} U^{(2)}_{\beta}$, one sees finally, taking into account that $X^{(1)} \times_{S} X^{(2)}$ is a *scheme*, that
one has, by virtue of `(1.3.1)`,

```text
  ^{(b)}E_{pq}^2 = H^{−p}(X^{(1)} ×_S X^{(2)}, 𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)})).
```

In second place, $Tor^{A}_{q}(L^{(1)}_{\bullet,\bullet}, L^{(2)}_{\bullet,\bullet})$ is a bicomplex whose term of degree
$(h, k)$ is the direct sum of the $A$-modules

```text
  Tor_q^A(C^{−h_1}(𝔘^{(1)}, 𝒫_{k_1}^{(1)}), C^{−h_2}(𝔘^{(2)}, 𝒫_{k_2}^{(2)}))
```

such that $h_{1} + h_{2} = h$ and $k_{1} + k_{2} = k$; making the modules $C^{r}(\mathfrak{U}^{(i)},
\mathcal{P}^{(i)}_{j})$ explicit as above, one sees again that this term is the direct sum of the $A$-modules

```text
  Γ(U_σ^{(1)} ×_S U_τ^{(2)}, 𝒯or_q^S(𝒫_{k_1}^{(1)}, 𝒫_{k_2}^{(2)}))
```

where $k_{1} + k_{2} = k$, and $\sigma$ (resp. $\tau$) ranges over the elements of $\mathfrak{P}(\Phi^{(1)})$ (resp.
$\mathfrak{P}(\Phi^{(2)})$) such that $Card(\sigma) + Card(\tau) = -h - 2$. The term ${}^{(b')}E^{2}_{pq}$ that we are
computing is the $(-p)$-th cohomology module of a bicomplex $N^{\bullet\bullet} = (N^{j,k})$, where the simple complex
$N^{\bullet,k}$ is the complex of bi-alternating cochains on $\Phi^{(1)}$ and $\Phi^{(2)}$, with values in the system of
coefficients

```text
  𝒮_k : (σ, τ) ↦ Γ(U_σ^{(1)} ×_S U_τ^{(2)}, ⊕_{k_1 + k_2 = k} 𝒯or_q^S(𝒫_{k_1}^{(1)}, 𝒫_{k_2}^{(2)})),
```

these systems of coefficients forming a complex $\mathcal{S}^{\bullet}$, where the differential comes from that of the
simple complex associated to the bicomplex $\mathcal{T}or^{S}_{q}(\mathcal{P}^{(1)}_{\bullet},
\mathcal{P}^{(2)}_{\bullet})$. One knows that the cohomology of $N^{\bullet\bullet}$ is the same as that of the
bicomplex $C^{\bullet}(\Phi^{(1)}, \Phi^{(2)}; \mathcal{S}^{\bullet})$ $(0_{III}, 11.8.9)$, and also the same as that of
the bicomplex $P^{\bullet}(\Phi^{(1)}, \Phi^{(2)}; \mathcal{S}^{\bullet})$, whose elements of degree $(h, k)$ are the
linear combinations of

```text
  λ(σ, τ) ∈ Γ(U_σ^{(1)} ×_S U_τ^{(2)}, ⊕_{k_1 + k_2 = k} 𝒯or_q^S(𝒫_{k_1}^{(1)}, 𝒫_{k_2}^{(2)}))
```

$\sigma = (\alpha_{0}, \cdots, \alpha_{h})$, $\tau = (\beta_{0}, \cdots, \beta_{h})$ being sequences having the *same
number of elements* $(0_{III}, 11.8.10)$. One sees then as above that ${}^{(b')}E^{2}_{pq}$ is the $(-p)$-th cohomology
module of the bicomplex $C^{\bullet}(\mathfrak{U}, \mathcal{Q}^{\bullet})$, where $\mathcal{Q}^{\bullet}$ is the simple
complex associated to the bicomplex $\mathcal{T}or^{S}_{q}(\mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$ of
$\mathcal{O}_{Z}$-modules. With the conventions made in `(6.6.1)`, one therefore has

```text
  ^{(b')}E_{pq}^2 = H^{−p}(X^{(1)} ×_S X^{(2)}, 𝒯or_q^S(𝒫_•^{(1)}, 𝒫_•^{(2)})).
```

<!-- original page 156 -->

**6.6.5. Spectral sequences (c) and (d).**

<!-- label: III.6.6.5 -->

By definition, the complex $H^{II}_{n}(L^{(i)}_{\bullet,\bullet})$ has as term of degree $h$ the $A$-module
$C^{-h}(\mathfrak{U}^{(i)}, \mathcal{H}_{n}(\mathcal{P}^{(i)}_{\bullet}))$, by virtue of the exactness of the functor
$C^{-h}$. One has therefore, by definition of the hypertor of two modules relative to two covers `(6.6.2)`,

```text
  ^{(c)}E_{pq}^2 = ⊕_{q_1 + q_2 = q} Tor_p^S(𝔘^{(1)}, 𝔘^{(2)}; ℋ_{q_1}(𝒫_•^{(1)}), ℋ_{q_2}(𝒫_•^{(2)})).
```

Finally, by definition, $Tor^{A, I}_{q}(L^{(1)}_{\bullet,\bullet}, L^{(2)}_{\bullet,\bullet})$ is a bicomplex whose term
of degree $(h, k)$ is the $A$-module $Tor^{S}_{q}(\mathfrak{U}^{(1)}, \mathfrak{U}^{(2)}; \mathcal{P}^{(1)}_{h},
\mathcal{P}^{(2)}_{k})$. One therefore has

```text
  ^{(d)}E_{pq}^2 = H_p(Tor_q^S(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})).
```

**6.6.6.**

<!-- label: III.6.6.6 -->

The theory of hyperhomology of functors of bicomplexes $(0_{III}, 11.7.3)$ shows, as in `(6.3.4)`, that, for every
Cartan–Eilenberg flat resolution $M^{(i)}_{\bullet,\bullet,\bullet}$ of $L^{(i)}_{\bullet,\bullet}$ (in the category of
complexes of modules bounded below) ($i = 1, 2$), one has canonical isomorphisms of bi-$\partial$-functors

```text
  Tor_•^S(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})
        ⥲ H_•(M_{•,•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)})
        ⥲ H_•(M_{•,•,•}^{(1)} ⊗_A L_{•,•}^{(2)})
        ⥲ H_•(L_{•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)}).                                (6.6.6.1)
```

**6.6.7.**

<!-- label: III.6.6.7 -->

We shall now show that the global hypertor defined in `(6.6.2)`, and the corresponding six spectral sequences, do not
depend on the *finite* affine open covers $\mathfrak{U}^{(i)}$ that served to define them (up to canonical
isomorphisms). For this it will suffice to show that if $\mathfrak{V}^{(i)}$ are two other covers of the same nature,
such that $\mathfrak{V}^{(i)}$ is *finer* than $\mathfrak{U}^{(i)}$ for $i = 1, 2$, then one has canonical isomorphisms
of spectral functors

```text
  ^{(t)}E(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ^{(t)}E(𝔙^{(1)}, 𝔙^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})
                                                                                (6.6.7, t)
```

where $t$ is replaced by $a$, $b$, $a'$, $b'$, $c$, or $d$.

Now, one has for $i = 1, 2$ homomorphisms of bicomplexes

```text
  C^•(𝔘^{(i)}, 𝒫_•^{(i)}) → C^•(𝔙^{(i)}, 𝒫_•^{(i)})
```

well defined up to homotopies `(G, II, 5.7.1)`; there already result canonically defined homomorphisms `(6.6.7, t)`
compatible with the boundary operators in the abutments $(0_{III}, 11.3.2)$. In addition, the computation of the `E_2`
terms of the spectral sequences `(a)`, `(b)`, `(a')`, `(b')` shows that for these spectral sequences the homomorphism
`(6.6.7, t)` is an isomorphism on the `E_2` terms; since these spectral sequences are biregular, one sees that
`(6.6.7, t)` is an isomorphism for these four spectral functors, hence an isomorphism of bi-$\partial$-functors for
their common abutment $(0_{III}, 11.1.5)$.

In particular, for quasi-coherent $\mathcal{O}_{X^{(i)}}$-modules $\mathcal{F}^{(i)}$ ($i = 1, 2$), the canonical
homomorphism

```text
  Tor_•^S(𝔘^{(1)}, 𝔘^{(2)}; ℱ^{(1)}, ℱ^{(2)}) → Tor_•^S(𝔙^{(1)}, 𝔙^{(2)}; ℱ^{(1)}, ℱ^{(2)})
```

is bijective; given the computation of `(6.6.5)`, one sees that `(6.6.7, t)` is also an isomorphism on the `E_2` terms
for $t = c$ and $t = d$. One concludes as above that `(6.6.7, t)` is also an isomorphism of spectral sequences for $t =
c$ and $t = d$.

<!-- original page 157 -->

One may consider that the isomorphisms `(6.6.7, t)` define inductive systems of spectral functors on the filtered set of
pairs $(\mathfrak{U}^{(1)}, \mathfrak{U}^{(2)})$ of finite affine open covers of $X^{(1)}$ and $X^{(2)}$. We shall
denote by

```text
  ^{(t)}E(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})  or  ^{(t)}E^S(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})
```

the inductive limit of this system, and by $Tor^{S}_{\bullet}(X^{(1)}, X^{(2)}; \mathcal{P}^{(1)}_{\bullet},
\mathcal{P}^{(2)}_{\bullet})$ the abutment of this spectral functor, which we shall call the *global hypertor* of the
two complexes $\mathcal{P}^{(1)}_{\bullet}$ and $\mathcal{P}^{(2)}_{\bullet}$; if $\mathcal{P}^{(1)}_{\bullet}$ and
$\mathcal{P}^{(2)}_{\bullet}$ are reduced to their terms of degree `0`, $\mathcal{F}^{(1)}$ and $\mathcal{F}^{(2)}$, we
shall write

```text
  Tor_n^S(X^{(1)}, X^{(2)}; ℱ^{(1)}, ℱ^{(2)}),
```

and conformably to the general conventions, $Tor^{S}_{q}(X^{(1)}, X^{(2)}; \mathcal{P}^{(1)}_{\bullet},
\mathcal{P}^{(2)}_{\bullet})$ will therefore be the bicomplex of $Tor^{S}_{q}(X^{(1)}, X^{(2)}; \mathcal{P}^{(1)}_{h},
\mathcal{P}^{(2)}_{k})$.

**6.6.8.**

<!-- label: III.6.6.8 -->

The hypotheses being those of `(6.6.1)`, consider now two $S$-morphisms $f_{i} : X^{(i)} \to Y^{(i)}$, where $Y^{(i)} =
\operatorname{Spec}(B_{i})$ is an affine $S$-scheme, $B_{i}$ thus being an $A$-algebra ($i = 1, 2$); this defines
therefore an $A$-homomorphism $B_{i} \to \Gamma(X^{(i)}, \mathcal{O}_{X^{(i)}})$ `(I, 2.2.4)`, and consequently each of
the $L^{(i)}_{\bullet,\bullet}$ defined in `(6.6.2)` is a bicomplex of $B_{i}$-modules; one concludes that
$L^{(1)}_{\bullet,\bullet} \otimes_{A} L^{(2)}_{\bullet,\bullet}$ is a quadricomplex of $(B_{1} \otimes_{A}
B_{2})$-modules, and its six spectral hyperhomology functors may therefore be considered as taking their values in the
category of spectral sequences of $(B_{1} \otimes_{A} B_{2})$-modules. If one sets $Y = Y^{(1)} \times_{S} Y^{(2)} =
\operatorname{Spec}(B_{1} \otimes_{A} B_{2})$, one may consider the quasi-coherent $\mathcal{O}_{Y}$-modules associated
to these modules `(I, 1.3.4)`; we shall denote by ${}^{(t)}\mathcal{E}(f_{1}, f_{2}; \mathcal{P}^{(1)}_{\bullet},
\mathcal{P}^{(2)}_{\bullet})$ (for $t = a$, $b$, $a'$, $b'$, $c$, or $d$) the six spectral sequences
$({}^{(t)}E(X^{(1)}, X^{(2)}; \mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet}))~$ of $\mathcal{O}_{Y}$-modules,
and $\mathcal{T}or^{S}_{\bullet}(f_{1}, f_{2}; \mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$ their common
abutment $(Tor^{S}_{\bullet}(X^{(1)}, X^{(2)}; \mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet}))~$. One will
denote it $\mathcal{T}or^{S}_{\bullet}(f_{1}, f_{2}; \mathcal{F}^{(1)}, \mathcal{F}^{(2)})$ when
$\mathcal{P}^{(i)}_{\bullet}$ is reduced to its term of degree `0`, $\mathcal{F}^{(i)}$ ($i = 1, 2$).

# §6 (continued). Local and global Tor functors; the Künneth formula

> _Translator's note._ This file continues §III.6 from the companion Part-A file. §6.1–§6.6 are there; §6.7–§6.9 are
> here. They will be concatenated for the final volume.

<!-- original page 25 -->

## 6.7. Global hypertor functors of complexes of quasi-coherent modules and Künneth spectral sequences: the general case.

**6.7.1.**

<!-- label: III.6.7.1 -->

We shall now generalize the definitions of `(6.6.8)` to the case where $S$ is an arbitrary prescheme, $X^{(i)}$,
$Y^{(i)}$ are $S$-preschemes, and $f_{i} : X^{(i)} \to Y^{(i)}$ are separated and quasi-compact morphisms. The task is
then, for every pair of complexes $\mathcal{P}^{(i)}_{\bullet}$ of $\mathcal{O}_{X^{(i)}}$-modules quasi-coherent,
bounded below $(i = 1, 2)$, to define, for every $n$, an $\mathcal{O}_{Y}$-module quasi-coherent
$\mathcal{T}or^{S}_{n}(f_{1}, f_{2}; \mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$ together with `6`
spectral functors, which reduce to the definitions of `(6.6.8)` when $S$, $Y^{(1)}$ and $Y^{(2)}$ are affine (one sets
$Y = Y^{(1)} \times_{S} Y^{(2)}$).

Suppose first $S = \operatorname{Spec}(A)$ affine, but $Y^{(1)}$ and $Y^{(2)}$ arbitrary; let $W^{(i)}$ be an affine
open of $Y^{(i)}$; $f^{-1}_{i}(W^{(i)})$ is then a quasi-compact $S$-scheme, $W = W^{(1)} \times_{S} W^{(2)}$ an affine
open of $Y$; let $f_{i}' : f^{-1}_{i}(W^{(i)}) \to W^{(i)}$ be the restriction of $f_{i}$, and
$\mathcal{P}_{\bullet}'^{(i)}$ the restriction of $\mathcal{P}^{(i)}_{\bullet}$ to $f^{-1}_{i}(W^{(i)})$ $(i = 1, 2)$.
We then have, by `(6.6.8)`, the spectral sequences ${}^{(t)}\mathcal{E}(f_{1}', f_{2}'; \mathcal{P}_{\bullet}'^{(1)},
\mathcal{P}_{\bullet}'^{(2)})$ of $(\mathcal{O}_{Y} | W)$-modules quasi-coherent, and it remains to verify that they
satisfy the gluing conditions $(0_{I}, 3.3.1)$. We are at once reduced to the case where $Y^{(i)} =
\operatorname{Spec}(B_{i})$ is affine and where $W^{(i)} = D(g_{i})$, with $g_{i} \in B_{i}$, so that $W = D(g_{1}
\otimes g_{2})$

<!-- original page 26 -->

in $Y = \operatorname{Spec}(B_{1} \otimes_{A} B_{2})$ `(II, 4.3.2.1)`; if $X'^{(i)} = f^{-1}_{i}(W^{(i)})$, the task is
to establish a canonical isomorphism of spectral functors

```text
  ^{(t)}E(X'^{(1)}, X'^{(2)}; 𝒫_•'^{(1)}, 𝒫_•'^{(2)})
        ⥲ ^{(t)}E(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⊗_B B_g                (6.7.1.1)
```

where one has set $B = B_{1} \otimes_{A} B_{2}$ and $g = g_{1} \otimes g_{2}$. To do this, start from finite affine open
covers $\mathfrak{U}^{(i)}$ of $X^{(i)}$ $(i = 1, 2)$, and let $\mathfrak{U}'^{(i)}$ be the trace of
$\mathfrak{U}^{(i)}$ on $X'^{(i)}$, which is still formed of affine opens `(I, 5.5.10)`; more precisely, one has

```text
  C^•(𝔘'^{(i)}, 𝒫_•'^{(i)}) = C^•(𝔘^{(i)}, 𝒫_•^{(i)}) ⊗_{B_i} (B_i)_{g_i}.
```

If one sets $L^{(i)}_{\bullet,\bullet} = C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet})$, one therefore
has $L_{\bullet,\bullet}'^{(1)} \otimes_{A} L_{\bullet,\bullet}'^{(2)} = (L^{(1)}_{\bullet,\bullet} \otimes_{B_{1}}
(B_{1})_{g_{1}}) \otimes_{A} (L^{(2)}_{\bullet,\bullet} \otimes_{B_{2}} (B_{2})_{g_{2}})$; since one has $B_{g} =
(B_{1})_{g_{1}} \otimes_{A} (B_{2})_{g_{2}}$ up to a canonical isomorphism, one has, up to a canonical isomorphism,
$L_{\bullet,\bullet}'^{(1)} \otimes_{A} L_{\bullet,\bullet}'^{(2)} = (L^{(1)}_{\bullet,\bullet} \otimes_{A}
L^{(2)}_{\bullet,\bullet}) \otimes_{B} B_{g}$. If $M^{(i)}_{\bullet,\bullet,\bullet}$ is a projective Cartan–Eilenberg
resolution of $L^{(i)}_{\bullet,\bullet}$, which one may suppose formed of $B_{i}$-modules, it follows from the fact
that $(B_{i})_{g_{i}}$ is flat over $B_{i}$ that $M_{\bullet,\bullet,\bullet}'^{(i)} = M^{(i)}_{\bullet,\bullet,\bullet}
\otimes_{B_{i}} (B_{i})_{g_{i}}$ is a projective Cartan–Eilenberg resolution of the bicomplex
$L_{\bullet,\bullet}'^{(i)}$; moreover, one has

```text
  M_{•,•,•}'^{(1)} ⊗_A M_{•,•,•}'^{(2)} = (M_{•,•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)}) ⊗_B B_g.
```

The desired isomorphism `(6.7.1.1)` then follows at once from the definitions of the hyperhomology of a bicomplex and
from the exactness of the functor $G \otimes_{B} B_{g}$ in the $B$-module $G$.

**6.7.2.**

<!-- label: III.6.7.2 -->

Suppose now $S$ arbitrary, and let $u_{i} : Y^{(i)} \to S$ be the structure morphisms $(i = 1, 2)$. Let $(S_{\alpha})$
be an affine open cover of $S$; set $Y^{(i)}_{\alpha} = u^{-1}_{i}(S_{\alpha})$, $X^{(i)}_{\alpha} =
f^{-1}_{i}(Y^{(i)}_{\alpha})$, and let $f_{i\alpha} : X^{(i)}_{\alpha} \to Y^{(i)}_{\alpha}$ be the restriction of
$f_{i}$, which is a separated and quasi-compact morphism. The $Y_{\alpha} = Y^{(1)}_{\alpha} \times_{S_{\alpha}}
Y^{(2)}_{\alpha}$ form an open cover of $Y$, and on each $Y_{\alpha}$ there are defined by `(6.7.1)` spectral functors

```text
  ^{(t)}𝓔_α(f_{1α}, f_{2α}; 𝒫_•^{(1)} | X_α^{(1)}, 𝒫_•^{(2)} | X_α^{(2)});
```

it remains again to show that these functors satisfy the gluing conditions. One is at once reduced to the following
situation: $S = \operatorname{Spec}(A)$ is affine, $S' = D(h)$, with $h \in A$, and $u_{i}(Y^{(i)}) \subset S'$; one may
further suppose $Y^{(i)} = \operatorname{Spec}(B_{i})$ affine; the task is to define canonical isomorphisms

```text
  ^{(t)}E^S(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ^{(t)}E^{S'}(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}).
                                                                                  (6.7.2.1)
```

Now, with the notations of `(6.6.2)`, the $L^{(i)}_{\bullet,\bullet}$ are formed of $A_{h}$-modules, and one therefore
has $L^{(1)}_{\bullet,\bullet} \otimes_{A_{h}} L^{(2)}_{\bullet,\bullet} = L^{(1)}_{\bullet,\bullet} \otimes_{A}
L^{(2)}_{\bullet,\bullet}$ up to a canonical isomorphism; since one may take a projective Cartan–Eilenberg resolution
$M^{(i)}_{\bullet,\bullet,\bullet}$ of $L^{(i)}_{\bullet,\bullet}$ formed of $A_{h}$-modules, this gives at once the
desired canonical isomorphism.

We have thus, in summary, proved the

**Theorem (6.7.3).**

<!-- label: III.6.7.3 -->

— *Let $S$ be a prescheme, $f_{i} : X^{(i)} \to Y^{(i)}$ a separated and quasi-compact $S$-morphism of $S$-preschemes,
$\mathcal{P}^{(i)}_{\bullet}$ a complex of $\mathcal{O}_{X^{(i)}}$-modules quasi-coherent, bounded below $(i = 1, 2)$;
one sets $Y = Y^{(1)} \times_{S} Y^{(2)}$. There exists a bi-∂-functor $\mathcal{T}or^{S}_{\bullet}(f_{1}, f_{2};
\mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$*

<!-- original page 27 -->

*with values in the category of $\mathcal{O}_{Y}$-modules quasi-coherent, such that if $V^{(i)}$ is an affine open of
$Y^{(i)}$ $(i = 1, 2)$ and $V = V^{(1)} \times_{S} V^{(2)}$, one has*

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

One will note that the spectral sequences `(a)` and `(a')` (resp. `(b)` and `(b')`) are *identical* when
$\mathcal{P}^{(1)}_{\bullet}$ and $\mathcal{P}^{(2)}_{\bullet}$ reduce to their terms of degree `0`; in this case, the
sequences `(c)` and `(d)` are degenerate and are therefore without interest.

**Remark (6.7.4).**

<!-- label: III.6.7.4 -->

The global hypertor that we have defined above include as particular cases both the hypercohomology modules defined in
`(6.2.1)` and the local hypertor defined in `(6.5.3)`. Let us show that one has, for every morphism $f : X \to Y$
quasi-compact and separated and every complex $\mathcal{P}_{\bullet}$ of $\mathcal{O}_{X}$-modules quasi-coherent,
bounded below, a canonical isomorphism of ∂-functors in $\mathcal{P}_{\bullet}$

```text
  𝒯or^Y_n(f, 1_Y; 𝒫_•, 𝒪_Y) ⥲ ℋ^{-n}(f, 𝒫_•)                  (for every n ∈ ℤ).        (6.7.4.1)
```

Indeed, the gluing methods of `(6.7.2)` reduce one at once to the case where $Y$ is affine; one may then, by virtue of
`(6.2.2)`, compute the two members of `(6.7.4.1)` using one and the same finite cover $\mathfrak{U}$ of $Y$ by affine
opens, and (for the first member) the cover of $Y$ formed of $Y$ itself; with the notations of `(6.6.2)`, the bicomplex
$L^{(2)}_{\bullet,\bullet}$ is then reduced to its term of degrees `(0, 0)`, equal to $A$, and the conclusion follows
from $(0_{III}, 11.7.5)$. For a generalization of this result, see `(6.7.7)`; but one will note that when one replaces
$\mathcal{O}_{Y}$ by an arbitrary quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{F}$ in the first member of
`(6.7.4.1)`, one no longer has in general an isomorphism with $\mathcal{H}^{-n}(f, \mathcal{P}_{\bullet}
\otimes_{\mathcal{O}_{Y}} \mathcal{F})$, although, in the preceding computation, the bicomplex
$L^{(1)}_{\bullet,\bullet} \otimes_{A} \mathcal{F}$ still identifies with the bicomplex $C^{\bullet}(\mathfrak{U},
\mathcal{P}_{\bullet} \otimes_{\mathcal{O}_{Y}} \mathcal{F})$.

On the other hand, one has a canonical isomorphism of bi-∂-functors

```text
  𝒯or^S_•(1_{X^{(1)}}, 1_{X^{(2)}}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ 𝒯or^S_•(𝒫_•^{(1)}, 𝒫_•^{(2)}).             (6.7.4.2)
```

Indeed, one reduces again, by `(6.7.1)` and `(6.7.2)`, to the case where $S$ and the $X^{(i)}$ are affine; in computing
the first member of `(6.7.4.2)`, one may then take

<!-- original page 28 -->

as cover $\mathfrak{U}^{(i)}$ the family reduced to the single element $X^{(i)}$, so that, with the notations of
`(6.6.2)`, $L^{(i)}_{\bullet,\bullet}$ reduces to $\Gamma(X^{(i)}, \mathcal{P}^{(i)}_{\bullet})$ (regarded as a
bicomplex whose terms of first degree $\neq 0$ are zero), and the equality of the two members of `(6.7.4.2)` follows
from `(6.4.1.1)` and `(6.3.1)`.

**Proposition (6.7.5).**

<!-- label: III.6.7.5 -->

— *Let $u : \mathcal{P}^{(1)}_{\bullet} \to \mathcal{Q}^{(1)}_{\bullet}$ be a homomorphism of complexes of
$\mathcal{O}_{X^{(1)}}$-modules quasi-coherent, bounded below, such that the homomorphism*

$$ \mathcal{H}_{\bullet}(u) : \mathcal{H}_{\bullet}(\mathcal{P}^{(1)}_{\bullet}) \to
\mathcal{H}_{\bullet}(\mathcal{Q}^{(1)}_{\bullet}) $$

*deduced from $u$ is an isomorphism. Then the homomorphisms*

```text
  ^{(t)}𝓔(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)}) → ^{(t)}𝓔(f_1, f_2; 𝒬_•^{(1)}, 𝒫_•^{(2)})
```

*deduced from $u$ are isomorphisms for $t = a$, $t = b$ and $t = c$.*

The assertion concerning the spectral sequence `(c)` follows from the fact that this sequence is biregular and that the
homomorphism in question is an isomorphism on the `E_2` terms by hypothesis $(0_{III}, 11.1.5)$. This already shows that
$\mathcal{T}or^{S}_{\bullet}(f_{1}, f_{2}; \mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet}) \to
\mathcal{T}or^{S}_{\bullet}(f_{1}, f_{2}; \mathcal{Q}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$ is an isomorphism.
Applying the relations `(6.7.4.1)` and `(6.7.4.2)` one sees first that the homomorphisms $\mathcal{H}^{-n}(f_{1},
\mathcal{P}^{(1)}_{\bullet}) \to \mathcal{H}^{-n}(f_{1}, \mathcal{Q}^{(1)}_{\bullet})$ and
$\mathcal{T}or^{S}_{\bullet}(\mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet}) \to
\mathcal{T}or^{S}_{\bullet}(\mathcal{Q}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$ deduced from $u$ are
isomorphisms. The assertion concerning the sequences `(a)` and `(b)` then follows from the fact that these sequences are
biregular `(6.7.3)` and that the homomorphisms in question are bijective on the `E_2` terms $(0_{III}, 11.1.5)$.

Note moreover that, if $u : \mathcal{P}^{(1)}_{\bullet} \to \mathcal{Q}^{(1)}_{\bullet}$ is a homotopism, one deduces
from it canonical isomorphisms ${}^{(t)}\mathcal{E}(f_{1}, f_{2}; \mathcal{P}^{(1)}_{\bullet},
\mathcal{P}^{(2)}_{\bullet}) \xrightarrow{\sim} {}^{(t)}\mathcal{E}(f_{1}, f_{2}; \mathcal{Q}^{(1)}_{\bullet},
\mathcal{P}^{(2)}_{\bullet})$ for the six spectral sequences. Indeed, if $S$ and the $Y^{(i)}$ are affine, one deduces
from $u$ a homotopism of bicomplexes $C^{\bullet}(\mathfrak{U}^{(1)}, \mathcal{P}^{(1)}_{\bullet}) \to
C^{\bullet}(\mathfrak{U}^{(1)}, \mathcal{Q}^{(1)}_{\bullet})$, and the proposition follows from the general theory of
hyperhomology $(0_{III}, 11.3.2)$; the passage to the general case is done by gluing, using the fact that, from a
homotopism of complexes, one deduces a homotopism of projective Cartan–Eilenberg resolutions of these complexes
`(M, XVII, 1.2)`.

**Proposition (6.7.6).**

<!-- label: III.6.7.6 -->

— *Suppose that the complex $\mathcal{P}^{(1)}_{\bullet}$ or the complex $\mathcal{P}^{(2)}_{\bullet}$ is formed of
$S$-flat modules (both complexes being bounded below). Then one has a canonical isomorphism of bi-∂-functors*

```text
  𝒯or^S_n(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ℋ^{-n}(f_1 ×_S f_2, 𝒫_•^{(1)} ⊗_S 𝒫_•^{(2)}).            (6.7.6.1)
```

Suppose first $S$, $Y^{(1)}$ and $Y^{(2)}$ affine, so that one is in the situation of `(6.6.2)`, whose notations we
keep. Suppose for instance that $\mathcal{P}^{(1)}_{\bullet}$ is formed of $S$-flat modules, and let us compute the
hypertor using remark `(6.6.6)`: it is therefore the homology of $L^{(1)}_{\bullet,\bullet} \otimes_{A}
M^{(2)}_{\bullet,\bullet,\bullet}$, where $M^{(2)}_{\bullet,\bullet,\bullet}$ is a projective Cartan–Eilenberg
resolution of $L^{(2)}_{\bullet,\bullet}$, in the sense of $(0_{III}, 11.7.1)$. On the other hand, the modules
$L^{(1)}_{\bullet,\bullet}$ are flat over $A$ by virtue of hypothesis `(1.4.15.1)`; one then deduces from $(0_{III},
11.7.5)$ a canonical isomorphism

```text
  Tor^S_•(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ℋ_•(L_{•,•}^{(1)} ⊗_A L_{•,•}^{(2)}).             (6.7.6.2)
```

On the other hand, one has a natural homomorphism of bicomplexes from $L^{(1)}_{\bullet,\bullet} \otimes_{A}
L^{(2)}_{\bullet,\bullet}$ into $C^{\bullet}(\mathfrak{U}, \mathcal{Q}_{\bullet})$, where $\mathfrak{U}$ is the cover of
$Z = X^{(1)} \times_{S} X^{(2)}$ by the affine opens

<!-- original page 29 -->

$U^{(1)}_{\alpha} \times_{S} U^{(2)}_{\beta}$ and $\mathcal{Q}_{\bullet} = \mathcal{P}^{(1)}_{\bullet} \otimes_{S}
\mathcal{P}^{(2)}_{\bullet}$ (regarded as a simple complex with respect to total degree); indeed, the definition of this
homomorphism has in substance been given in the course of the computation of the sequence `(b')` in `(6.6.4)`, for $q =
0$; it suffices simply (keeping the notations of `(6.6.4)`) to take into account that on the one hand there is a natural
homomorphism from the complex $N^{\bullet k}$ into the complex $C^{\bullet}(\Phi^{(1)}, \Phi^{(2)}; \mathcal{S}_{k})$
$(0_{III}, 11.8.5)$, on the other hand a natural homomorphism from this latter complex into the complex
$P^{\bullet}(\Phi^{(1)}, \Phi^{(2)}; \mathcal{S}_{k})$ $(0_{III}, 11.8.6)$, and finally a natural homomorphism from this
latter complex of cochains into the subcomplex of alternating cochains $(0_{III}, 11.8.7)$. Moreover, the homomorphism
of bicomplexes thus defined gives an isomorphism in homology, as seen in `(6.6.4)`; one therefore has, by composing with
`(6.7.6.2)`, obtained an isomorphism

```text
  Tor^S_•(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ H^{-n}(𝔘, 𝒫_•^{(1)} ⊗_S 𝒫_•^{(2)}).               (6.7.6.3)
```

It must next be proved that the isomorphism thus defined does not depend on the chosen open covers (the second member of
`(6.7.6.3)` being canonically isomorphic to $H^{-n}(X^{(1)} \times_{S} X^{(2)}, \mathcal{P}^{(1)}_{\bullet} \otimes_{S}
\mathcal{P}^{(2)}_{\bullet})$ by `(6.2.2)`); this is done using `(6.6.7)` by noting (with the notations of `(6.6.7)`)
that one has a commutative diagram up to homotopisms

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

— *Suppose that $\mathcal{P}^{(1)}_{\bullet}$ and $\mathcal{P}^{(2)}_{\bullet}$ are bounded below, and that all the
modules $\mathcal{H}^{-n}(f_{1}, \mathcal{P}^{(1)}_{\bullet})$ or all the modules $\mathcal{H}^{-n}(f_{2},
\mathcal{P}^{(2)}_{\bullet})$ are $S$-flat. Then one has a canonical isomorphism of bi-∂-functors ($n$ running through
$\mathbb{Z}$)*

```text
  𝒯or^S_n(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⥲ ⊕_{q_1 + q_2 = n} ℋ^{-q_1}(f_1, 𝒫_•^{(1)}) ⊗_S ℋ^{-q_2}(f_2, 𝒫_•^{(2)}).
                                                                                  (6.7.7.1)
```

Indeed, in view of `(6.5.8)`, the spectral sequence `(a)` of `(6.7.3)` is degenerate, and the proposition follows at
once from $(0_{III}, 11.1.6)$, this sequence being biregular `(6.7.3)`.

**Theorem (6.7.8).**

<!-- label: III.6.7.8 -->

— *Suppose that: 1° the complexes $\mathcal{P}^{(1)}_{\bullet}$ and $\mathcal{P}^{(2)}_{\bullet}$ are bounded below; 2°
the complex $\mathcal{P}^{(1)}_{\bullet}$ or the complex $\mathcal{P}^{(2)}_{\bullet}$ is formed of $S$-flat modules; 3°
all the*

<!-- original page 30 -->

*modules $\mathcal{H}^{-n}(f_{1}, \mathcal{P}^{(1)}_{\bullet})$ or all the modules $\mathcal{H}^{-n}(f_{2},
\mathcal{P}^{(2)}_{\bullet})$ are $S$-flat. Then one has a canonical isomorphism of bi-∂-functors ($n$ running through
$\mathbb{Z}$)*

```text
  ℋ^{-n}(f_1 ×_S f_2, 𝒫_•^{(1)} ⊗_S 𝒫_•^{(2)})
       ⥲ ⊕_{n_1 + n_2 = n} ℋ^{-n_1}(f_1, 𝒫_•^{(1)}) ⊗_S ℋ^{-n_2}(f_2, 𝒫_•^{(2)})            (6.7.8.1)
```

*("*Künneth formula*").*

This follows from `(6.7.6)` and `(6.7.7)`.

When $S$, $Y^{(1)}$ and $Y^{(2)}$ are affine, the inverse of the isomorphism `(6.7.8.1)` is deduced (with the notations
of `(6.7.6)`) from the homomorphism of bicomplexes

```text
  C^•(𝔘^{(1)}, 𝒫_•^{(1)}) ⊗_A C^•(𝔘^{(2)}, 𝒫_•^{(2)}) → C^•(𝔘, 𝒬_•)
```

by the procedure defined in `(G, I, 2.7)`, as follows from `(G, I, 5.5)`.

**Proposition (6.7.9).**

<!-- label: III.6.7.9 -->

— *Suppose the following three conditions verified:*

*1° $S$, $Y^{(1)}$ and $Y^{(2)}$ are locally Noetherian, $f_{1}$ and $f_{2}$ are proper, $Y^{(1)}$ or $Y^{(2)}$ of
finite type over $S$.*

*2° $\mathcal{P}^{(1)}_{\bullet}$ and $\mathcal{P}^{(2)}_{\bullet}$ are bounded below.*

*3° For every $n \in \mathbb{Z}$, $\mathcal{H}_{n}(\mathcal{P}^{(i)}_{\bullet})$ is a coherent module $(i = 1, 2)$.*

*Under these conditions, $\mathcal{T}or^{S}_{n}(f_{1}, f_{2}; \mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$
is a coherent $\mathcal{O}_{Y}$-module (with $Y = Y^{(1)} \times_{S} Y^{(2)}$).*

It follows from `(6.5.13)` that the local hypertor $\mathcal{T}or^{S}_{n}(\mathcal{P}^{(1)}_{\bullet},
\mathcal{P}^{(2)}_{\bullet})$ are coherent $\mathcal{O}_{X}$-modules ($X = X^{(1)} \times_{S} X^{(2)}$ being locally
Noetherian, since one of the $X^{(i)}$ is by hypothesis of finite type over $S$ `(I, 6.3.4 and 6.3.8)`). Since $Y$ is
locally Noetherian and $f_{1} \times_{S} f_{2}$ is proper `(II, 5.4.2)`, it follows from `(6.2.5)` that the terms
${}^{(b)}\mathcal{E}^{2}_{pq}$ of `(6.7.3)` are coherent $\mathcal{O}_{Y}$-modules. Since all the spectral sequences of
`(6.7.3)` are biregular by virtue of hypothesis 2°, one concludes by $(0_{III}, 11.1.8)$.

**6.7.10.**

<!-- label: III.6.7.10 -->

Let now $Y'^{(i)}$ be two $S$-preschemes $(i = 1, 2)$, $v_{i} : Y'^{(i)} \to Y^{(i)}$ two $S$-morphisms, $v : v_{1}
\times_{S} v_{2}$ their product, which is an $S$-morphism $Y' \to Y$, where one sets $Y' = Y'^{(1)} \times_{S}
Y'^{(2)}$. Consider on the other hand, for $i = 1, 2$, an $S$-prescheme $X'^{(i)}$, and two $S$-morphisms $u_{i} :
X'^{(i)} \to X^{(i)}$, $f_{i}' : X'^{(i)} \to Y'^{(i)}$, so that the diagrams

```text
                       u_i
            X'^{(i)} ─────→ X^{(i)}

            f_i' │             │ f_i                                                      (6.7.10.1)
                 ↓             ↓

            Y'^{(i)} ─────→ Y^{(i)}
                       v_i
```

are commutative, the morphisms $f_{i}'$ being *separated* and *quasi-compact*. One then has canonical
$\mathcal{O}_{Y'}$-homomorphisms of spectral functors

```text
  v^*(^{(t)}𝓔(f_1, f_2; 𝒫_•^{(1)}, 𝒫_•^{(2)})) → ^{(t)}𝓔(f_1', f_2'; u_1^*(𝒫_•^{(1)}), u_2^*(𝒫_•^{(2)}))
                                                                                          (6.7.10.2)
```

for $t = a, a', b, b', c, d$. To define these, suppose first $S = \operatorname{Spec}(A)$, $Y^{(i)} =
\operatorname{Spec}(B_{i})$, $Y'^{(i)} = \operatorname{Spec}(B_{i}')$ affine; the $X^{(i)}$ and $X'^{(i)}$ are then
quasi-compact schemes. To compute the spectral sequences ${}^{(t)}\mathcal{E}(f_{1}, f_{2}; \mathcal{P}^{(1)}_{\bullet},
\mathcal{P}^{(2)}_{\bullet})$, we shall consider as in `(6.6.1)` finite covers $\mathfrak{U}^{(i)}$ by affine opens of
$X^{(i)}$ $(i = 1, 2)$; to compute ${}^{(t)}\mathcal{E}(f_{1}', f_{2}'; u^{*}_{1}(\mathcal{P}^{(1)}_{\bullet}),
u^{*}_{2}(\mathcal{P}^{(2)}_{\bullet}))$, we shall consider finite covers $\mathfrak{U}'^{(i)}$

<!-- original page 31 -->

of $X'^{(i)}$ by affine opens, finer respectively than the covers $u^{-1}_{i}(\mathfrak{U}^{(i)})$ $(i = 1, 2)$. It is
clear that the bicomplex $C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet}) = L^{(i)}_{\bullet,\bullet}$ can
be regarded canonically as a sub-bicomplex of $C^{\bullet}(u^{-1}_{i}(\mathfrak{U}^{(i)}),
u^{*}_{i}(\mathcal{P}^{(i)}_{\bullet}))$ $(0_{I}, 4.4.3.2)$; moreover, by choosing a simplicial map `(G, II, 5.7)` of
$\mathfrak{U}'^{(i)}$ into $u^{-1}_{i}(\mathfrak{U}^{(i)})$, one defines a homomorphism of bicomplexes
$C^{\bullet}(u^{-1}_{i}(\mathfrak{U}^{(i)}), u^{*}_{i}(\mathcal{P}^{(i)}_{\bullet})) \to
C^{\bullet}(\mathfrak{U}'^{(i)}, u^{*}_{i}(\mathcal{P}^{(i)}_{\bullet}))$, whence, by composition, a homomorphism of
bicomplexes $L^{(i)}_{\bullet,\bullet} \to L_{\bullet,\bullet}'^{(i)} = C^{\bullet}(\mathfrak{U}'^{(i)},
u^{*}_{i}(\mathcal{P}^{(i)}_{\bullet}))$. Moreover, this homomorphism is replaced by a homotopic homomorphism when one
changes simplicial map `(G, II, 5.7.1)`; one has thus a well-defined homomorphism of spectral functors:

```text
  ^{(t)}𝓔(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) → ^{(t)}𝓔(𝔘'^{(1)}, 𝔘'^{(2)}; u_1^*(𝒫_•^{(1)}), u_2^*(𝒫_•^{(2)})).
                                                                                          (6.7.10.3)
```

One verifies at once that if $\mathfrak{V}^{(i)}$ is a finite affine cover of $X^{(i)}$ finer than $\mathfrak{U}^{(i)}$,
$\mathfrak{V}'^{(i)}$ a finite affine cover of $X'^{(i)}$ finer than $u^{-1}_{i}(\mathfrak{V}^{(i)})$ and than
$\mathfrak{V}^{(i)}$, the diagram

```text
  C^•(𝔘^{(i)}, 𝒫_•^{(i)})  ─────→  C^•(𝔙^{(i)}, 𝒫_•^{(i)})

           │                                  │
           │                                  │
           ↓                                  ↓

  C^•(𝔘'^{(i)}, u_i^*(𝒫_•^{(i)})) ─→  C^•(𝔙'^{(i)}, u_i^*(𝒫_•^{(i)}))
```

is commutative, which implies that the homomorphism `(6.7.10.3)` does not depend essentially on the covers
$\mathfrak{U}^{(i)}$ and $\mathfrak{U}'^{(i)}$ considered. One has therefore in fact defined a homomorphism of
$A$-modules

```text
  ^{(t)}E(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) → ^{(t)}E(X'^{(1)}, X'^{(2)}; u_1^*(𝒫_•^{(1)}), u_2^*(𝒫_•^{(2)})).
                                                                                          (6.7.10.4)
```

But it is clear by definition of the $u^{*}_{i}(\mathcal{P}^{(i)}_{\bullet})$ and by virtue of the commutativity of
`(6.7.10.1)` that this homomorphism is also a homomorphism of $(B_{1} \otimes_{A} B_{2})$-modules; since the second
member of `(6.7.10.4)` is formed of $(B_{1}' \otimes_{A} B_{2}')$-modules, one canonically deduces from `(6.7.10.4)` a
homomorphism of $(B_{1}' \otimes_{A} B_{2}')$-modules

```text
  ^{(t)}E(X^{(1)}, X^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)}) ⊗_{B_1 ⊗_A B_2} (B_1' ⊗_A B_2')
       → ^{(t)}E(X'^{(1)}, X'^{(2)}; u_1^*(𝒫_•^{(1)}), u_2^*(𝒫_•^{(2)}))                   (6.7.10.5)
```

which, in view of `(I, 1.6.5)`, is none other than the desired homomorphism `(6.7.10.2)` in the particular case
considered.

It remains to pass to the general case by following the gluings of `(6.7.1)` and `(6.7.2)`; the second passage is
immediate; as for the first, one considers as in `(6.7.1)` elements $g_{i} \in B_{i}$, and their images $g_{i}' \in
B_{i}'$, the tensor product $g = g_{1} \otimes g_{2}$ in $B = B_{1} \otimes_{A} B_{2}$ and its image $g' = g_{1}'
\otimes g_{2}'$ in $B' = B_{1}' \otimes_{A} B_{2}'$, and everything reduces to using

<!-- original page 32 -->

the canonical isomorphism $(M \otimes_{B} B')_{g'} \xrightarrow{\sim} M_{g} \otimes_{B_{g}} B_{g'}'$ $(0_{I}, 1.5.4)$;
we leave the details to the reader.

**6.7.11.**

<!-- label: III.6.7.11 -->

The theory of global hypertor, developed above for two $S$-morphisms $X^{(i)} \to Y^{(i)}$ and two complexes
$\mathcal{P}^{(i)}_{\bullet}$ of modules quasi-coherent bounded below, extends at once to the following general case:
one has a prescheme $S$, a finite family of $S$-preschemes $Y^{(i)}$ $(i \in I)$, a finite family of $S$-morphisms
separated and quasi-compact $f_{i} : X^{(i)} \to Y^{(i)}$, and for each $i$ a complex of $\mathcal{O}_{X^{(i)}}$-modules
quasi-coherent $\mathcal{P}^{(i)}_{\bullet}$ bounded below. If $Y$ is the product of the $S$-preschemes $Y^{(i)}$, one
then defines, for each integer $n \in \mathbb{Z}$, an $\mathcal{O}_{Y}$-module quasi-coherent
$\mathcal{T}or^{S}_{n}((f_{i})_{i \in I}; (\mathcal{P}^{(i)}_{\bullet})_{i \in I})$, these modules forming a ∂-functor
covariant in each of the complexes $\mathcal{P}^{(i)}_{\bullet}$; moreover, this functor is the common abutment of six
spectral functors ${}^{(t)}\mathcal{E}((f_{i})_{i \in I}; (\mathcal{P}^{(i)}_{\bullet})_{i \in I})$. We leave to the
reader the task of repeating for this general case the definitions and reasoning given above for $I = {1, 2}$. Let us
simply note that when $I$ reduces to a single element, one recovers the hypercohomology $\mathcal{H}^{\bullet}(f,
\mathcal{P}_{\bullet})$ defined in `(6.2.7)` (as already observed in `(6.7.4)`). When $I$ is the interval $1 \leq i \leq
m$ of $\mathbb{N}$, we shall write

```text
  𝒯or^S_n(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})    for    𝒯or^S_n((f_i)_{i ∈ I}; (𝒫_•^{(i)})_{i ∈ I}).
```

**Proposition (6.7.12).**

<!-- label: III.6.7.12 -->

— *The notations being those of `(6.7.11)`, let $J$ be a subset of $I$ such that, for $i \in I - J$, one has $X^{(i)} =
Y^{(i)} = S$, $f_{i}$ being reduced to the identity, and $\mathcal{P}^{(i)}_{\bullet}$ equal to the complex reduced to
the term of degree `0` equal to $\mathcal{O}_{S}$. There is then a canonical isomorphism of ∂-functors*

```text
  𝒯or^S_•((f_i)_{i ∈ I}; (𝒫_•^{(i)})_{i ∈ I}) ⥲ 𝒯or^S_•((f_j)_{j ∈ J}; (𝒫_•^{(j)})_{j ∈ J}).         (6.7.12.1)
```

One may restrict oneself to defining this isomorphism when $S$ and the $Y^{(i)}$ are affine, the gluing being done as
usual. For $i \in I - J$, one may take the cover $\mathfrak{U}^{(i)}$ formed of the single set $S$, and then
$L^{(i)}_{\bullet,\bullet} = C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet})$ reduces to its only term of
degrees `(0, 0)`, equal to $\Gamma(S, \mathcal{O}_{S}) = A(S)$; the isomorphism `(6.7.12.1)` is then evident.

**Remark (6.7.13).**

<!-- label: III.6.7.13 -->

The notations being those of `(6.7.3)`, consider the canonical $S$-isomorphism $Y^{(1)} \times_{S} Y^{(2)}
\xrightarrow{\sim} Y^{(2)} \times_{S} Y^{(1)}$ `(I, 3.3.5)`; then the image by this isomorphism of
$\mathcal{T}or^{S}_{\bullet}(f_{1}, f_{2}; \mathcal{P}^{(1)}_{\bullet}, \mathcal{P}^{(2)}_{\bullet})$ is
$\mathcal{T}or^{S}_{\bullet}(f_{2}, f_{1}; \mathcal{P}^{(2)}_{\bullet}, \mathcal{P}^{(1)}_{\bullet})$; the question
being local, one is reduced to the case envisaged in `(6.6.2)`, and if one denotes by
$M^{(i)}_{\bullet,\bullet,\bullet}$ a projective Cartan–Eilenberg resolution of $L^{(i)}_{\bullet,\bullet}$ $(i = 1,
2)$, the isomorphism considered transforms $M^{(1)}_{\bullet,\bullet,\bullet} \otimes_{A}
M^{(2)}_{\bullet,\bullet,\bullet}$ into $M^{(2)}_{\bullet,\bullet,\bullet} \otimes_{A}
M^{(1)}_{\bullet,\bullet,\bullet}$, whence our assertion by considering the homology of the simple complexes associated
to these tricomplexes.

## 6.8. The associativity spectral sequences of the global hypertor.

**6.8.1.**

<!-- label: III.6.8.1 -->

The hypotheses and notations being those of `(6.7.11)` (and in particular the $\mathcal{P}^{(i)}_{\bullet}$ being
supposed bounded below), suppose given a partition $(I_{j})_{j \in J}$ of the index set $I$; we propose to give an
"associativity" relation between the hypertor $\mathcal{T}or^{S}_{\bullet}((f_{i})_{i \in I};
(\mathcal{P}^{(i)}_{\bullet})_{i \in I})$ and each of the "partial" hypertor

```text
  𝒯_{•, j} = 𝒯or^S_•((f_i)_{i ∈ I_j}; (𝒫_•^{(i)})_{i ∈ I_j}).
```

<!-- original page 33 -->

To simplify the notation, we shall restrict to the case where $I$ is the interval $1 \leq i \leq m$, and where the
partition $(I_{j})$ is composed of the two intervals ${1, 2, \cdots, r}$ and ${r + 1, \cdots, m}$.

**Proposition (6.8.2).**

<!-- label: III.6.8.2 -->

— *There exists a canonical biregular spectral functor (called the* "associativity spectral functor"*) denoted*

```text
  ^{(e)}𝓔(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})  (or simply  ^{(e)}𝓔(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}))
```

*whose abutment is $\mathcal{T}or^{S}_{\bullet}(f_{1}, \cdots, f_{m}; \mathcal{P}^{(1)}_{\bullet}, \cdots,
\mathcal{P}^{(m)}_{\bullet})$, and whose `E_2` term is given by*

```text
  ^{(e)}𝓔^2_{pq} = ⊕_{q_1 + q_2 = q} 𝒯or^S_p(𝒯or^S_{q_1}(f_1, …, f_r; 𝒫_•^{(1)}, …, 𝒫_•^{(r)}),
                                            𝒯or^S_{q_2}(f_{r+1}, …, f_m; 𝒫_•^{(r+1)}, …, 𝒫_•^{(m)})).
```

In this statement, one has identified $Y$ canonically with the product $Z^{(1)} \times_{S} Z^{(2)}$, where $Z^{(1)} =
Y^{(1)} \times_{S} Y^{(2)} \times_{S} \cdots \times_{S} Y^{(r)}$ and $Z^{(2)} = Y^{(r+1)} \times_{S} \cdots \times_{S}
Y^{(m)}$. We restrict ourselves to the case where $S$ and the $Y^{(i)}$ are affine; one passes from this particular case
to the general case by the methods developed in `(6.7.1)` and `(6.7.2)`, and we leave the details of the reasoning
(without difficulty) to the reader. We shall therefore prove the

**Corollary (6.8.3).**

<!-- label: III.6.8.3 -->

— *Let $A$ be a ring, $S = \operatorname{Spec}(A)$, $X^{(i)}$ $(1 \leq i \leq m)$ be $S$-schemes quasi-compact and, for
each $i$, let $\mathcal{P}^{(i)}_{\bullet}$ be a complex of $\mathcal{O}_{X^{(i)}}$-modules quasi-coherent bounded
below. There exists a canonical biregular spectral functor having for abutment*

```text
  Tor^S_•(X^{(1)}, …, X^{(m)}; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})
```

*and whose `E_2` term is given by*

```text
  ^{(e)}E^2_{pq} = ⊕_{q_1 + q_2 = q} Tor^A_p(Tor^S_{q_1}(X^{(1)}, …, X^{(r)}; 𝒫_•^{(1)}, …, 𝒫_•^{(r)}),
                                            Tor^S_{q_2}(X^{(r+1)}, …, X^{(m)}; 𝒫_•^{(r+1)}, …, 𝒫_•^{(m)})).
```

According to the definition given in `(6.6.2)`, the computation of the hypertor in question is carried out by taking,
for each $i$, a finite affine open cover $\mathfrak{U}^{(i)}$ of $X^{(i)}$, by considering the bicomplexes
$L^{(i)}_{\bullet,\bullet} = C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet})$, a projective
Cartan–Eilenberg resolution $M^{(i)}_{\bullet,\bullet,\bullet}$ of each of these bicomplexes (in the sense of $(0_{III},
11.7.1)$), the tensor product $M_{\bullet,\bullet,\bullet} = \otimes^{m}_{i=1} M^{(i)}_{\bullet,\bullet,\bullet}$ of
these tricomplexes, and by taking the homology of $M_{\bullet,\bullet,\bullet}$. Consider $M_{\bullet,\bullet,\bullet}$
as a simple complex $N_{\bullet}$, tensor product of the two simple complexes

```text
  N_•' = ⊗_{i=1}^r M_{•,•,•}^{(i)},               N_•'' = ⊗_{i=r+1}^m M_{•,•,•}^{(i)},
```

where $N_{\bullet}'$ and $N_{\bullet}''$ are graded by the sum of the total degrees of the
$M^{(i)}_{\bullet,\bullet,\bullet}$. Moreover, the $A$-modules of the complexes $N_{\bullet}'$ and $N_{\bullet}''$ are
*projective*, so it follows from `(6.5.9)` that one has $H_{\bullet}(M_{\bullet,\bullet,\bullet}) =
Tor^{A}_{\bullet}(N_{\bullet}', N_{\bullet}'')$; the spectral sequence sought is then none other than the sequence
`(6.3.2.2)` applied to the complexes $N_{\bullet}'$ and $N_{\bullet}''$, taking into account the interpretation of the
homology modules of these complexes which follows from what precedes (when one applies the remarks of the beginning to
each of the partial products $X^{(1)} \times_{S} \cdots \times_{S} X^{(r)}$ and $X^{(r+1)} \times_{S} \cdots \times_{S}
X^{(m)}$). Finally, the regularity properties follow from `(6.3.2)` and from the fact that, the
$\mathcal{P}^{(i)}_{\bullet}$ being bounded below, so are the $M^{(i)}_{\bullet,\bullet,\bullet}$; consequently,
$N_{\bullet}'$ and $N_{\bullet}''$ are bounded below.

<!-- original page 34 -->

## 6.9. The base-change spectral sequences in the global hypertor.

**6.9.1.**

<!-- label: III.6.9.1 -->

The hypotheses and notations being still those of `(6.7.11)` (and in particular the $\mathcal{P}^{(i)}_{\bullet}$ being
supposed bounded below), consider a morphism $g : S' \to S$ of preschemes, and set $Y'^{(i)} = Y^{(i)}_{(S')}$,
$X'^{(i)} = X^{(i)}_{(S')}$ and $\mathcal{P}_{\bullet}'^{(i)} = \mathcal{P}^{(i)}_{\bullet} \otimes_{\mathcal{O}_{S}}
\mathcal{O}_{S'}$, $\mathcal{P}_{\bullet}'^{(i)}$ thus being a complex of $\mathcal{O}_{X'^{(i)}}$-modules
quasi-coherent; let $f_{i}' = (f_{i})_{(S')} : X'^{(i)} \to Y'^{(i)}$, which is a separated and quasi-compact morphism
`(I, 5.5.1 and 6.6.4)`. We propose to study the relations between the $\mathcal{O}_{Y'}$-modules quasi-coherent
$\mathcal{T}or^{S'}_{n}((f_{i}')_{i \in I}; (\mathcal{P}_{\bullet}'^{(i)})_{i \in I})$ and
$\mathcal{T}or^{S}_{n}((f_{i})_{i \in I}; (\mathcal{P}^{(i)}_{\bullet})_{i \in I}) \otimes_{\mathcal{O}_{S}}
\mathcal{O}_{S'}$, where $Y' = Y \times_{S} S' = Y_{(S')}$. A particularly simple case is the following one, which
reduces to `(1.4.15)` when $I$ reduces to a single element and $\mathcal{P}_{\bullet}$ to a single module:

**Proposition (6.9.2).**

<!-- label: III.6.9.2 -->

— *If the morphism $g : S' \to S$ is flat, one has a canonical isomorphism of ∂-functors (in the
$\mathcal{P}^{(i)}_{\bullet}$):*

```text
  𝒯or^S_•((f_i)_{i ∈ I}; (𝒫_•^{(i)})_{i ∈ I}) ⊗_{𝒪_S} 𝒪_{S'} ⥲ 𝒯or^{S'}_•((f_i')_{i ∈ I}; (𝒫_•'^{(i)})_{i ∈ I}).
                                                                                          (6.9.2.1)
```

One may again restrict oneself to the case where $S$, $S'$ and the $Y^{(i)}$ are affine, the gluing being done following
the methods of `(6.7.1)` and `(6.7.2)`. Let $S = \operatorname{Spec}(A)$, $S' = \operatorname{Spec}(A')$, and take for
each $i$ an affine open cover $\mathfrak{U}^{(i)}$ of $X^{(i)}$; if $u_{i} : X'^{(i)} \to X^{(i)}$ is the canonical
projection, $u^{-1}_{i}(\mathfrak{U}^{(i)})$ is an affine open cover of $X'^{(i)}$ `(II, 1.5.5)`, which we shall denote
by $\mathfrak{U}'^{(i)}$; it is then clear that $C^{\bullet}(\mathfrak{U}'^{(i)}, \mathcal{P}_{\bullet}'^{(i)}) =
C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet}) \otimes_{A} A'$, and the existence of the isomorphism
`(6.9.2.1)` is immediate, since if $M^{(i)}_{\bullet,\bullet,\bullet}$ is a projective Cartan–Eilenberg resolution of
$L^{(i)}_{\bullet,\bullet} = C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet})$ in the sense of $(0_{III},
11.7.1)$, formed of $A$-modules, $M^{(i)}_{\bullet,\bullet,\bullet} \otimes_{A} A'$ is a projective Cartan–Eilenberg
resolution (in the same sense) of $L^{(i)}_{\bullet,\bullet} \otimes_{A} A'$ formed of $A'$-modules, by virtue of the
hypothesis that $A'$ is a flat $A$-module; this same hypothesis shows moreover that $H_{\bullet}(\otimes^{m}_{i=1}
(M^{(i)}_{\bullet,\bullet,\bullet} \otimes_{A} A')) = H_{\bullet}(\otimes^{m}_{i=1} M^{(i)}_{\bullet,\bullet,\bullet})
\otimes_{A} A'$.

One will note that when $I$ is reduced to the single element `1`, the formula `(6.9.2.1)` follows directly from
`(6.7.7)`, applied by taking $Y_{2} = X_{2} = S'$, $f_{2} = 1_{S'}$, and the complex $\mathcal{P}^{(2)}_{\bullet}$
reduced to its term of degree `0`, equal to $\mathcal{O}_{S'}$; one knows then that the hypercohomology
$\mathcal{H}^{n}(1_{S'}, \mathcal{O}_{S'})$ is zero for every $n \neq 0$ and reduces to $\mathcal{O}_{S'}$ for $n = 0$
`(6.2.1)`.

In the general case, we shall introduce in place of $\mathcal{O}_{S'}$ a complex $\mathcal{Q}_{\bullet}'$ of
$\mathcal{O}_{S'}$-modules quasi-coherent *bounded below*, so that if, to simplify, one takes $I = {1, 2, \cdots, m}$,
one may consider the ∂-functor

```text
  𝒯or^S_•(f_1, …, f_m, 1_{S'}; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}, 𝒬_•').
```

**Proposition (6.9.3).**

<!-- label: III.6.9.3 -->

— *There exist three canonical biregular spectral functors denoted ${}^{(t)}\mathcal{E}(f_{1}, \cdots, f_{m};
\mathcal{P}^{(1)}_{\bullet}, \cdots, \mathcal{P}^{(m)}_{\bullet}, \mathcal{Q}_{\bullet}')$ (with $t = e$, $f$ or $f'$)
having for common abutment $\mathcal{T}or^{S}_{\bullet}(f_{1}, \cdots, f_{m}, 1_{S'}; \mathcal{P}^{(1)}_{\bullet},
\cdots, \mathcal{P}^{(m)}_{\bullet}, \mathcal{Q}_{\bullet}')$ and whose `E_2` terms are respectively*

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

The sequence `(e)` is none other than the associativity sequence of `(6.8.2)` for $r = m$. To define the other two
spectral sequences, we shall again restrict to the case where $S$, $S'$ and the $Y^{(i)}$ are affine, the passage to the
general case being done by the methods of `(6.7.1)` and `(6.7.2)` and being left to the reader. We shall therefore prove
the

**Corollary (6.9.4).**

<!-- label: III.6.9.4 -->

— *Let $A$ be a ring, $A'$ an $A$-algebra, $S = \operatorname{Spec}(A)$, $S' = \operatorname{Spec}(A')$, $X^{(i)}$ $(1
\leq i \leq m)$ $S$-schemes quasi-compact and for each $i$, let $X'^{(i)} = X^{(i)}_{(S')}$, which is a quasi-compact
$S'$-scheme. For each $i$, let $\mathcal{P}^{(i)}_{\bullet}$ be a complex of $\mathcal{O}_{X^{(i)}}$-modules
quasi-coherent; let finally $Q_{\bullet}'$ be a complex of $A'$-modules, these complexes being bounded below. There
exist three biregular spectral functors in the $\mathcal{P}^{(i)}_{\bullet}$ and in $Q_{\bullet}'$, having for common
abutment*

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
only for the record. To define the others, consider for each $i$ a finite affine open cover $\mathfrak{U}^{(i)}$ of
$X^{(i)}$, and, if $u_{i} : X'^{(i)} \to X^{(i)}$ is the canonical projection, the corresponding finite affine open
cover $\mathfrak{U}'^{(i)} = u^{-1}_{i}(\mathfrak{U}^{(i)})$. By virtue of `(6.6.6)`, $Tor^{S}_{\bullet}(X^{(1)},
\cdots, X^{(m)}, S'; \mathcal{P}^{(1)}_{\bullet}, \cdots, \mathcal{P}^{(m)}_{\bullet}, Q_{\bullet}')$ is obtained by
taking for $1 \leq i \leq m$ a projective Cartan–Eilenberg resolution $M^{(i)}_{\bullet,\bullet,\bullet}$ of
$L^{(i)}_{\bullet,\bullet} = C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet})$ (in the sense of $(0_{III},
11.7.1)$), considering the tricomplex $M_{\bullet,\bullet,\bullet} = M^{(1)}_{\bullet,\bullet,\bullet} \otimes_{A}
M^{(2)}_{\bullet,\bullet,\bullet} \otimes \cdots \otimes_{A} M^{(m)}_{\bullet,\bullet,\bullet} \otimes_{A} Q_{\bullet}'$
(where $Q_{\bullet}'$ is regarded as a tricomplex whose two last degrees reduce to `0`), and taking its homology. If one
sets $M_{\bullet,\bullet,\bullet}'^{(i)} = M^{(i)}_{\bullet,\bullet,\bullet} \otimes_{A} A'$, one has (recalling that
$Q_{\bullet}'$ is a complex of $A'$-modules) $M_{\bullet,\bullet,\bullet} = M_{\bullet,\bullet,\bullet}'^{(1)}
\otimes_{A'} M_{\bullet,\bullet,\bullet}'^{(2)} \otimes \cdots \otimes_{A'} M_{\bullet,\bullet,\bullet}'^{(m)}
\otimes_{A'} Q_{\bullet}'$. Now, consider each of the complexes $M_{\bullet,\bullet,\bullet}'^{(i)}$ as a simple complex
(with respect to its total degree) and note that this complex is formed of $A'$-modules *projective*; it follows from
`(6.3.7)` (extended to an arbitrary number of complexes) that $H_{\bullet}(M_{\bullet,\bullet,\bullet})$ is also equal
to $Tor^{A'}_{\bullet}(M_{\bullet,\bullet,\bullet}'^{(1)}, \cdots, M_{\bullet,\bullet,\bullet}'^{(m)}, Q_{\bullet}')$;
it is therefore `(6.5.15)` the abutment of a spectral sequence having the desired regularity properties (the three
degrees of $M^{(i)}_{\bullet,\bullet,\bullet}$ being bounded below when $\mathcal{P}^{(i)}_{\bullet}$ is bounded below)
and whose `E_2` term is given by

```text
  E^2_{pq} = ⊕_{q_1 + ⋯ + q_{m+1} = q} Tor^{A'}_p(H_{q_1}(M_{•,•,•}'^{(1)}), …, H_{q_m}(M_{•,•,•}'^{(m)}),
                                                  H_{q_{m+1}}(Q_•')).
```

<!-- original page 36 -->

One has, moreover, $H_{q_{i}}(M_{\bullet,\bullet,\bullet}'^{(i)}) = H_{q_{i}}(M^{(i)}_{\bullet,\bullet,\bullet}
\otimes_{A} A') = Tor^{S}_{q_{i}}(X^{(i)}, S'; \mathcal{P}^{(i)}_{\bullet}, \mathcal{O}_{S'})$ by virtue of the
definition of the global hypertor, which gives the sequence `(f)` sought. One may on the other hand consider
$M_{\bullet,\bullet,\bullet}'^{(i)}$ as a bicomplex in which the first degree is the sum of the first and second degrees
of the tricomplex $M^{(i)}_{\bullet,\bullet,\bullet}$, the second degree being the third degree of this tricomplex;
since the modules forming the $M_{\bullet,\bullet,\bullet}'^{(i)}$ are projective $A'$-modules, the general theory of
hyperhomology shows that the homology of the bicomplex $M_{\bullet,\bullet,\bullet}'^{(1)} \otimes_{A'}
M_{\bullet,\bullet,\bullet}'^{(2)} \otimes \cdots \otimes_{A'} M_{\bullet,\bullet,\bullet}'^{(m)} \otimes_{A'}
Q_{\bullet}'$ is canonically isomorphic to its hyperhomology $(0_{III}, 11.6.5)$; it is therefore the abutment of a
spectral sequence with `E_2` term equal to

```text
  E^2_{pq} = ⊕_{q_1 + ⋯ + q_{m+1} = q} Tor^{A'}_p(H^{II}_{q_1}(M_{•,•,•}'^{(1)}), …,
                                                  H^{II}_{q_m}(M_{•,•,•}'^{(m)}), H^{II}_{q_{m+1}}(Q_•')).
```

Now, since the second degree of $Q_{\bullet}'$ reduces to `0`, one has $H^{II}_{n}(Q_{\bullet}') = 0$ for $n \neq 0$ and
$H^{II}_{0}(Q_{\bullet}') = Q_{\bullet}'$; the preceding formula is also written

```text
  E^2_{pq} = ⊕_{q_1 + ⋯ + q_m = q} Tor^{A'}_p(H^{II}_{q_1}(M_{•,•,•}'^{(1)}), …,
                                              H^{II}_{q_m}(M_{•,•,•}'^{(m)}), Q_•').
```

Moreover, one has $H^{II}_{q_{i}}(M_{\bullet,\bullet,\bullet}'^{(i)}) = H^{II}_{q_{i}}(M^{(i)}_{\bullet,\bullet,\bullet}
\otimes_{A} A') = Tor^{A}_{q_{i}}(L^{(i)}_{\bullet,\bullet}, A')$ by virtue of `(6.3.4)`; but $L^{(i)}_{\bullet,\bullet}
= C^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)}_{\bullet})$, direct sum of the $\Gamma(V,
\mathcal{P}^{(i)}_{\bullet})$, where $V$ runs through the (affine) intersections of $j + 1$ sets of the cover
$\mathfrak{U}^{(i)}$; if $V' = u^{-1}_{i}(V)$, $V'$ is affine in $X'^{(i)}$, and it follows from `(6.4.1.1)` that one
has

```text
  Γ(V', 𝒯or^S_{q_i}(𝒫_•^{(i)}, 𝒪_{S'})) = Tor^A_{q_i}(Γ(V, 𝒫_•^{(i)}), A')
```

whence for the bicomplex $H^{II}_{q_{i}}(M_{\bullet,\bullet,\bullet}'^{(i)})$ the expression

$$ C^{\bullet}(\mathfrak{U}'^{(i)}, \mathcal{T}or^{S}_{q_{i}}(\mathcal{P}^{(i)}_{\bullet}, \mathcal{O}_{S'})) $$

which gives finally the desired expression for the `E_2` term of the sequence `(f')`. The fact that this sequence is
biregular under the conditions indicated is verified as usual, taking into account that, if
$\mathcal{P}^{(i)}_{\bullet}$ is bounded below, all the degrees of $M^{(i)}_{\bullet,\bullet,\bullet}$ are bounded
below.

**Remark (6.9.5).**

<!-- label: III.6.9.5 -->

One sees as in `(6.7.6)` that the replacement of the $\mathcal{P}^{(i)}_{\bullet}$ and of $\mathcal{Q}_{\bullet}'$ by
complexes which are respectively *homotopic* to them does not change the sequences `(e)`, `(f)` and `(f')` up to
canonical isomorphism. Moreover, for the sequence `(f)`, homomorphisms $\mathcal{P}^{(i)}_{\bullet} \to
\mathcal{R}^{(i)}_{\bullet}$, $\mathcal{Q}_{\bullet}' \to \mathcal{T}_{\bullet}'$ of complexes which give isomorphisms
in homology $\mathcal{H}_{\bullet}(\mathcal{P}^{(i)}_{\bullet}) \xrightarrow{\sim}
\mathcal{H}_{\bullet}(\mathcal{R}^{(i)}_{\bullet})$, $\mathcal{H}_{\bullet}(\mathcal{Q}_{\bullet}') \xrightarrow{\sim}
\mathcal{H}_{\bullet}(\mathcal{T}_{\bullet}')$ yield an isomorphism of spectral sequences ${}^{(f)}\mathcal{E}(f_{1},
\cdots, f_{m}; \mathcal{P}^{(1)}_{\bullet}, \cdots, \mathcal{P}^{(m)}_{\bullet}, \mathcal{Q}_{\bullet}')
\xrightarrow{\sim} {}^{(f)}\mathcal{E}(f_{1}, \cdots, f_{m}; \mathcal{R}^{(1)}_{\bullet}, \cdots,
\mathcal{R}^{(m)}_{\bullet}, \mathcal{T}_{\bullet}')$; the proof is the same as for `(6.7.6)` taking into account the
result of `(6.7.6)` and the regularity of the sequence `(f)`.

**Corollary (6.9.6).**

<!-- label: III.6.9.6 -->

— *Under the conditions of `(6.9.1)`, suppose that:*

*1° The complexes $\mathcal{P}^{(i)}_{\bullet}$ are formed of modules flat over $S$, and the $\mathcal{O}_{Y}$-modules*

```text
  𝒯or^S_n(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})
```

*are flat over $S$.*

*2° The $\mathcal{P}^{(i)}_{\bullet}$ and $\mathcal{Q}_{\bullet}'$ are bounded below.*

<!-- original page 37 -->

*One has then, setting $\mathcal{P}_{\bullet}'^{(i)} = \mathcal{P}^{(i)}_{\bullet} \otimes_{\mathcal{O}_{S}}
\mathcal{O}_{S'}$, canonical functorial isomorphisms*

```text
  𝒯or^{S'}_n(f_1', …, f_m', 1_{S'}; 𝒫_•'^{(1)}, …, 𝒫_•'^{(m)}, 𝒬_•')                       (6.9.6.1)
        ⥲ ⊕_{n' + n'' = n} 𝒯or^S_{n'}(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}) ⊗_{𝒪_S} ℋ_{n''}(𝒬_•').
```

*In particular, for $\mathcal{Q}_{\bullet}'$ reduced to a single term $\mathcal{F}'$ of degree `0`, one has canonical
functorial isomorphisms*

```text
  𝒯or^{S'}_n(f_1', …, f_m', 1_{S'}; 𝒫_•'^{(1)}, …, 𝒫_•'^{(m)}, ℱ')                         (6.9.6.2)
        ⥲ 𝒯or^S_n(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}) ⊗_{𝒪_S} ℱ'
```

*and more particularly, for $\mathcal{F}' = \mathcal{O}_{S'}$,*

```text
  𝒯or^{S'}_n(f_1', …, f_m'; 𝒫_•'^{(1)}, …, 𝒫_•'^{(m)})                                     (6.9.6.3)
        ⥲ 𝒯or^S_n(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}) ⊗_{𝒪_S} 𝒪_{S'}.
```

The flatness hypothesis on the modules composing the $\mathcal{P}^{(i)}_{\bullet}$ entails that the complexes
$\mathcal{T}or^{S}_{q_{i}}(\mathcal{P}^{(i)}_{\bullet}, \mathcal{O}_{S'})$ are zero for $q_{i} \neq 0$ `(6.5.8)`. The
sequence `(f')` is therefore degenerate; hypothesis 2° entails moreover that it is biregular `(6.9.3)`, so the edge
homomorphism

```text
  𝒯or^{S'}_n(f_1', …, f_m', 1_{S'}; 𝒫_•'^{(1)}, …, 𝒫_•'^{(m)}, 𝒬_•') → ^{(f')}𝓔^2_{n0}      (6.9.6.4)
        = 𝒯or^{S'}_n(f_1', …, f_m', 1_{S'}; 𝒫_•'^{(1)}, …, 𝒫_•'^{(m)}, 𝒬_•')
```

is bijective $(0_{III}, 11.1.6)$. The flatness hypothesis on the modules

```text
  𝒯or^S_n(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)})
```

entails that ${}^{(e)}\mathcal{E}^{2}_{pq} = 0$ for $p \neq 0$ `(6.5.8)`. The sequence `(e)` is therefore also
degenerate, and since it is biregular, the edge homomorphism

```text
  𝒯or^{S'}_n(f_1, …, f_m, 1_{S'}; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}, 𝒬_•') → ^{(e)}𝓔^2_{0n}          (6.9.6.5)
        = ⊕_{n' + n'' = n} 𝒯or^S_{n'}(f_1, …, f_m; 𝒫_•^{(1)}, …, 𝒫_•^{(m)}) ⊗_{𝒪_S} ℋ_{n''}(𝒬_•')
```

is bijective $(0_{III}, 11.1.6)$; whence, by combining the two preceding isomorphisms, the isomorphism `(6.9.6.1)`. The
isomorphism `(6.9.6.2)` is deduced trivially, since one has then $\mathcal{H}_{n}(\mathcal{Q}_{\bullet}') = 0$ if $n
\neq 0$ and $\mathcal{H}_{0}(\mathcal{Q}_{\bullet}') = \mathcal{F}'$. Finally, the case $\mathcal{F}' =
\mathcal{O}_{S'}$ in `(6.9.6.2)` gives the isomorphism `(6.9.6.3)`, taking `(6.7.12)` into account.

**Corollary (6.9.7).**

<!-- label: III.6.9.7 -->

— *Under the conditions of `(6.9.1)`, suppose $S$ and $S'$ affine, and suppose given for each $i$ an integer $d_{i}$ $(1
\leq i \leq m)$. There then exists an integer $N$ depending only on $S$, the $X^{(i)}$ and the $d_{i}$, having the
following property: for every integer $n_{0}$, one has canonical isomorphisms `(6.9.6.3)` for $n \leq n_{0}$ and for
every system of complexes $\mathcal{P}^{(i)}_{\bullet}$ verifying the following conditions: 1° $\mathcal{P}^{(i)}_{k} =
0$ for $k < d_{i}$; 2° $\mathcal{P}^{(i)}_{k}$ is flat over $S$ for $k < n_{0} + N$; 3° $\mathcal{T}or^{S}_{q}(f_{1},
\cdots, f_{m}; \mathcal{P}^{(1)}_{\bullet}, \cdots, \mathcal{P}^{(m)}_{\bullet})$ is flat over $S$ for $q < n_{0} + N$.*

Suppose $\mathcal{P}^{(i)}_{k}$ flat over $S$ for $k < r$; then $\mathcal{T}or^{S}_{q_{i}}(\mathcal{P}^{(i)}_{k},
\mathcal{O}_{S'}) = 0$ for $k < r$ and $q_{i} \neq 0$; let us compute

```text
  𝒯or^{S'}_p(f_1', …, f_m'; 𝒯or^S_{q_1}(𝒫_•^{(1)}, 𝒪_{S'}), …, 𝒯or^S_{q_m}(𝒫_•^{(m)}, 𝒪_{S'}))         (6.9.7.1)
```

<!-- original page 38 -->

by the method of `(6.6.2)`, with the help of the inverse image of a fixed affine cover $\mathfrak{U}^{(i)}$ of $X^{(i)}$
$(i \leq m)$ (independent of $S'$ and of the $\mathcal{P}^{(i)}_{\bullet}$); the terms $L^{(i)}_{\bullet,\bullet}$ are
zero for $j < -N_{i}$ (depending only on $\mathfrak{U}^{(i)}$); if one of the $q_{i}$ is non-zero, the simple complex
whose homology of degree $p$ is `(6.9.7.1)` has its terms zero for all degrees $< r + \Sigma_{j \neq i} d_{j} -
\Sigma^{m}_{i=1} N_{i}$, hence `(6.9.7.1)` is zero for $p < r - N$, denoting by $N$ the largest of the numbers
$\Sigma^{m}_{i=1} N_{i} - \Sigma_{j \neq i} d_{j}$. One concludes from this that one has ${}^{(f')}\mathcal{E}^{2}_{pq}
= 0$ for $q \neq 0$ and $p < r - N$; since on the other hand ${}^{(f')}\mathcal{E}^{2}_{pq} = 0$ for $q < 0$, one sees
that the edge homomorphism `(6.9.6.4)` is bijective for $n < r - N$ `(M, XV, 5.6)` (for $\mathcal{Q}_{\bullet}' =
\mathcal{O}_{S'}$). In the second place, if $\mathcal{T}or^{S}_{q}(f_{1}, \cdots, f_{m}; \mathcal{P}^{(1)}_{\bullet},
\cdots, \mathcal{P}^{(m)}_{\bullet})$ is flat over $S$ for $q < r$, one has ${}^{(e)}\mathcal{E}^{2}_{pq} = 0$ for $p
\neq 0$ and $q < r$; on the other hand ${}^{(e)}\mathcal{E}^{2}_{pq} = 0$ for $p < 0$, so the edge homomorphism
`(6.9.6.5)` is bijective for $n < r$, which completes the proof.

The most important case of `(6.9.3)` in the applications is that where $m = 1$, $\mathcal{Q}_{\bullet}'$ being reduced
to a single term $\mathcal{F}'$ of degree `0`; we shall state it again in this case in view of later references[^1]:

**Proposition (6.9.8).**

<!-- label: III.6.9.8 -->

— *Let $S$ be a prescheme, $g : S' \to S$ a morphism, $f : X \to Y$ a separated and quasi-compact $S$-morphism of
$S$-preschemes, $\mathcal{P}_{\bullet}$ a complex of $\mathcal{O}_{X}$-modules quasi-coherent bounded below,
$\mathcal{F}'$ a quasi-coherent $\mathcal{O}_{S'}$-module. There exist two biregular spectral functors in
$\mathcal{P}_{\bullet}$ and $\mathcal{F}'$, with values in the category of $\mathcal{O}_{Y_{(S')}}$-modules
quasi-coherent, having the same abutment $\mathcal{T}or^{S}_{\bullet}(f, 1_{S'}; \mathcal{P}_{\bullet}, \mathcal{F}')$,
and whose `E_2` terms are*

```text
  ^{('e)}𝓔^2_{pq} = 𝒯or^S_p(ℋ^{-q}(f, 𝒫_•), ℱ')                                            (6.9.8.1)
  ^{(''e)}𝓔^2_{pq} = ℋ^{-p}(f', 𝒯or^S_q(𝒫_•, ℱ')),                                         (6.9.8.2)
```

*where $f' = f_{(S')} : X_{(S')} \to Y_{(S')}$.*

The sequences in question can also be obtained, not starting from `(6.9.3)`, but from the sequences `(a)` and `(b')` of
`(6.7.3)` for $X^{(1)} = X$, $Y^{(1)} = Y$, $X^{(2)} = Y^{(2)} = S'$, $f_{1} = f$, $f_{2} = 1_{S'}$. When $S = S' = Y$,
$Y$ being affine, one obtains two spectral sequences with `E_2` terms equal to

```text
  ^{('e)}𝓔^2_{pq} = 𝒯or^Y_p(ℋ^{-q}(f, 𝒫_•), ℱ)                                             (6.9.8.3)
  ^{(''e)}𝓔^2_{pq} = ℋ^{-p}(f, 𝒯or^Y_q(𝒫_•, ℱ))                                            (6.9.8.4)
```

abutting (by virtue of `(6.7.6)`) to the hypercohomology $\mathcal{H}^{\bullet}(f, \mathcal{P}_{\bullet} \otimes_{Y}
\mathcal{F})$ of the functor $f_{*}$ with respect to the complex $\mathcal{P}_{\bullet} \otimes_{Y} \mathcal{F}$ of
$\mathcal{O}_{X}$-modules, for every $\mathcal{O}_{Y}$-module quasi-coherent and $Y$-flat $\mathcal{F}$ (or for every
$\mathcal{O}_{Y}$-module quasi-coherent $\mathcal{F}$ when $\mathcal{P}_{\bullet}$ is formed of
$\mathcal{O}_{X}$-modules $Y$-flat), which are distinct from those of `(6.2.1)`.

**Corollary (6.9.9).**

<!-- label: III.6.9.9 -->

— *Under the conditions of `(6.9.8)`, suppose that the complex $\mathcal{P}_{\bullet}$ is bounded below, formed of
modules flat over $S$, and that the $\mathcal{O}_{Y}$-modules $\mathcal{H}^{n}(f, \mathcal{P}_{\bullet})$ are flat over
$S$.*

<!-- original page 39 -->

*One has then canonical functorial isomorphisms*

```text
  𝒯or^{S'}_•(f', 1_{S'}; 𝒫_•', ℱ') ⥲ ℋ^•(f, 𝒫_•) ⊗_{𝒪_S} ℱ'                                (6.9.9.1)
```

*where $\mathcal{P}_{\bullet}' = \mathcal{P}_{\bullet} \otimes_{\mathcal{O}_{S}} \mathcal{O}_{S'}$; in particular, for
$\mathcal{F}' = \mathcal{O}_{S'}$, one has canonical functorial isomorphisms*

```text
  ℋ^•(f', 𝒫_•') ⥲ ℋ^•(f, 𝒫_•) ⊗_{𝒪_S} 𝒪_{S'}.                                              (6.9.9.2)
```

This is the particular case $m = 1$ of `(6.9.6)`. More particularly:

**Corollary (6.9.10).**

<!-- label: III.6.9.10 -->

— *Let $S$ be a prescheme, $f : X \to Y$ a separated and quasi-compact $S$-morphism of $S$-preschemes,
$\mathcal{P}_{\bullet}$ a complex bounded below, formed of $\mathcal{O}_{X}$-modules quasi-coherent, flat over $S$.
Suppose moreover that the $\mathcal{O}_{Y}$-modules $\mathcal{H}^{n}(f, \mathcal{P}_{\bullet})$ are flat over $S$. For
every $s \in S$, denote by $X_{s}$ and $Y_{s}$ the fibres $X \otimes_{S} k(s)$, $Y \otimes_{S} k(s)$, $f_{s} : X_{s} \to
Y_{s}$ the morphism $f \times_{S} 1$, $\mathcal{P}^{(s)}_{\bullet}$ the complex $\mathcal{P}_{\bullet} \otimes_{S} k(s)$
of $\mathcal{O}_{X_{s}}$-modules. One has then canonical functorial isomorphisms*

```text
  ℋ^•(f_s, 𝒫_•^{(s)}) ⥲ ℋ^•(f, 𝒫_•) ⊗_S k(s).                                              (6.9.10.1)
```

One thus has, under suitable flatness hypotheses, a case where the formation of the derived functors $R^{n}
f_{*}(\mathcal{P}_{\bullet})$ "commutes with passage to fibres", which we shall recover by another method in §7.

*(To be continued.)*

# §6 (continued). Local and global Tor functors; the Künneth formula

> _Translator's note._ This file is the closing subsection of §III.6, translated as a separate piece for length. The
> opening (§6.1–§6.6) and middle (§6.7–§6.9) are in the companion Part-A and Part-B files. They will be concatenated for
> the final volume.

<!-- original page 39 -->

## 6.10. Local structure of certain cohomological functors.

**Proposition (6.10.1).**

<!-- label: III.6.10.1 -->

— *Let $S = \operatorname{Spec}(A)$ be an affine scheme, $Y^{(i)}$ $(1 \leq i \leq n)$ a finite family of affine
$S$-schemes, flat over $S$; for each $i$, let $f_{i} : X^{(i)} \to Y^{(i)}$ be a separated and quasi-compact
$S$-morphism, and let $\mathcal{P}^{(i)}_{\bullet}$ be a complex of $\mathcal{O}_{X^{(i)}}$-modules quasi-coherent,
bounded below. Let $Y$ be the product of the $S$-schemes $Y^{(i)}$. There exists a complex $\mathcal{K}_{\bullet}$ of
$\mathcal{O}_{Y}$-modules quasi-coherent and flat over $S$, having the following property: for every affine $S$-scheme
$S'$ and every complex $\mathcal{F}_{\bullet}'$ of $\mathcal{O}_{S'}$-modules quasi-coherent, bounded below, there is an
isomorphism*

```text
  𝒯or^S_•(f_1, …, f_n, 1_{S'}; 𝒫_•^{(1)}, …, 𝒫_•^{(n)}, ℱ_•') ⥲ ℋ_•(𝒦_• ⊗_S ℱ_•')         (6.10.1.1)
```

*which is an isomorphism of $\partial$-functors in $\mathcal{F}_{\bullet}'$. Moreover, for every $S$-morphism $u : S''
\to S'$ of affine $S$-schemes, the diagram*

```text
  𝒯or^S_•(f_1, …, f_n, 1_{S'}; 𝒫_•^{(1)}, …, 𝒫_•^{(n)}, ℱ_•')           ⥲   ℋ_•(𝒦_• ⊗_S ℱ_•')

                       │                                                              │           (6.10.1.2)
                       ↓                                                              ↓

  𝒯or^S_•(f_1, …, f_n, 1_{S''}; 𝒫_•^{(1)}, …, 𝒫_•^{(n)}, u^*(ℱ_•'))     ⥲   ℋ_•(𝒦_• ⊗_S u^*(ℱ_•'))
```

*(where the vertical arrows are the canonical $(\mathcal{O}_{Y}, \mathcal{O}_{S})$-morphisms defined in `(6.7.10)`) is
commutative.*

**Proof.** We compute the hypertor by the method of `(6.6.2)`, taking remark `(6.6.6)` into account; with the notations
of `(6.6.2)`, each $L^{(i)}_{\bullet,\bullet}$ is a bicomplex of $A_{i}$-modules, where we denote by $A_{i}$ the ring of
$Y^{(i)}$; it therefore admits a projective Cartan–Eilenberg resolution $M^{(i)}_{\bullet,\bullet,\bullet}$ (in the
sense of $(0_{III}, 11.7.1)$) formed of $A_{i}$-modules, and by virtue of `(6.6.6)`, the first member of `(6.10.1.1)` is
canonically isomorphic to $H_{\bullet}(M_{\bullet,\bullet,\bullet} \otimes_{A} Q_{\bullet})$, where

```text
  M_{•,•,•} = M_{•,•,•}^{(1)} ⊗_A M_{•,•,•}^{(2)} ⊗_A ⋯ ⊗_A M_{•,•,•}^{(n)}     and    Q_• = ℱ_•'.
```

Since, by hypothesis, the rings $A_{i}$ are flat $A$-modules, the $M^{(i)}_{\bullet,\bullet,\bullet}$ are tricomplexes
of flat $A$-modules $(0_{I}, 6.2.1)$, and the same holds for $M_{\bullet,\bullet,\bullet}$; moreover, if $B$ is the ring
of $Y$, tensor product of the $A_{i}$, $M_{\bullet,\bullet,\bullet}$ is a tricomplex of $B$-modules; the complex
$\mathcal{K}_{\bullet} = (M_{\bullet,\bullet,\bullet})^{~}$ of $\mathcal{O}_{Y}$-modules (where
$M_{\bullet,\bullet,\bullet}$ is

<!-- original page 40 -->

considered as a simple complex) therefore answers the question, as follows easily from `(6.7.10)`. ∎

**Corollary (6.10.2).**

<!-- label: III.6.10.2 -->

— *In the statement of `(6.10.1)`, one may suppose $\mathcal{K}_{\bullet}$ bounded below. When the
$\mathcal{P}^{(i)}_{\bullet}$ are bounded above and the $Y^{(i)}$ of finite cohomological dimension, one may suppose
$\mathcal{K}_{\bullet}$ bounded above.*

**Proof.** The first assertion follows from the fact that the three degrees of each of the
$M^{(i)}_{\bullet,\bullet,\bullet}$ are bounded below; on the other hand, if the rings $A_{i}$ are of finite
cohomological dimension, the third degree of each of the $M^{(i)}_{\bullet,\bullet,\bullet}$ takes only finitely many
values, and the same is true by construction of its first degree `(6.6.2)`; since its second degree is bounded above
provided that the degree of $\mathcal{P}^{(i)}_{\bullet}$ is bounded above `(6.6.2)`, the second assertion follows at
once. ∎

**Remarks (6.10.3).**

<!-- label: III.6.10.3 -->

— (i) With the notations of `(6.10.1)`, $\mathcal{H}_{\bullet}(\mathcal{K}_{\bullet} \otimes_{S}
\mathcal{F}_{\bullet}')$ is isomorphic to $\mathcal{T}or_{\bullet}(\mathcal{K}_{\bullet}, \mathcal{F}_{\bullet}')$ since
$\mathcal{K}_{\bullet}$ is formed of $S$-flat $\mathcal{O}_{Y}$-modules `(6.5.9)`; it is therefore `(6.5.4)` the
abutment of a regular spectral sequence with `E_2` term given by

```text
  ^{(e)}𝓔^2_{pq} = ⊕_{q' + q'' = q} 𝒯or^S_p(ℋ_{q'}(𝒦_•), ℋ_{q''}(ℱ_•'))                       (6.10.3.1)
```

which is none other than the base-change spectral sequence `(e)` of `(6.9.3)`.

(ii) Let $\mathcal{K}_{\bullet}'$ be a second complex of $\mathcal{O}_{Y}$-modules quasi-coherent, flat over $S$, and
let $g : \mathcal{K}_{\bullet} \to \mathcal{K}_{\bullet}'$ be a homomorphism of complexes such that
$\mathcal{H}_{\bullet}(g) : \mathcal{H}_{\bullet}(\mathcal{K}_{\bullet}) \to
\mathcal{H}_{\bullet}(\mathcal{K}_{\bullet}')$ is an isomorphism. Then, by virtue of `(6.3.3)` and `(6.5.9)`, one
deduces from $g$ an isomorphism of $\partial$-functors in $\mathcal{F}_{\bullet}'$:
$\mathcal{H}_{\bullet}(\mathcal{K}_{\bullet} \otimes_{S} \mathcal{F}_{\bullet}') \xrightarrow{\sim}
\mathcal{H}_{\bullet}(\mathcal{K}_{\bullet}' \otimes_{S} \mathcal{F}_{\bullet}')$ such that the diagram

```text
  ℋ_•(𝒦_• ⊗_S ℱ_•')           ⥲           ℋ_•(𝒦_•' ⊗_S ℱ_•')

           │                                       │

           ↓                                       ↓

  ℋ_•(𝒦_• ⊗_S u^*(ℱ_•'))      ⥲           ℋ_•(𝒦_•' ⊗_S u^*(ℱ_•'))
```

is commutative. This therefore proves that the complex $\mathcal{K}_{\bullet}$ is *not entirely determined* by the
properties of `(6.10.1)`.

<!-- original page 41 -->

(iii) In the proof of `(6.10.1)`, one may suppose the $M^{(i)}_{\bullet,\bullet,\bullet}$ formed of *free*
$A_{i}$-modules (as follows easily from the proof of $(0_{III}, 11.5.2.1)$ "dualized"); the
$M^{(i)}_{\bullet,\bullet,\bullet} \otimes_{A} B$ are then formed of free $B$-modules, and since
$M_{\bullet,\bullet,\bullet}$ is equal to their tensor product over $B$, one sees that one may further suppose in
`(6.10.1)` that $\mathcal{K}_{\bullet}$ is associated to a complex of *free* $B$-modules. Moreover, by virtue of
`(M, XVII, 1.2)`, the tricomplex $M_{\bullet,\bullet,\bullet}$ depends functorially on each of the bicomplexes
$L^{(i)}_{\bullet,\bullet}$ (hence on each of the $\mathcal{P}^{(i)}_{\bullet}$, once one fixes a finite cover of each
of the $X^{(i)}$), the "morphisms" of tricomplexes being here understood as the classes of homomorphisms for the
homotopy relation; moreover, replacing a cover of $X^{(i)}$ by a finer cover gives rise for the
$L^{(i)}_{\bullet,\bullet}$ to homomorphisms defined precisely up to homotopy `(6.6.8)`, so one sees finally that, with
the preceding convention for morphisms, the tricomplex $M_{\bullet,\bullet,\bullet}$ is a *functor* in each of the
$\mathcal{P}^{(i)}_{\bullet}$. We shall make this functorial dependence precise, and in particular the behaviour of
$\mathcal{K}_{\bullet}$ with respect to exact sequences $0 \to \mathcal{P}^{(i)}_{\bullet} \to
\mathcal{Q}^{(i)}_{\bullet} \to \mathcal{R}^{(i)}_{\bullet} \to 0$ of complexes, in the chapter devoted to a general
algebra of cohomological functors, mentioned in `(6.1.3)`.

**Scholium (6.10.4).**

<!-- label: III.6.10.4 -->

— The fact that $\mathcal{K}_{\bullet}$ is formed of $S$-flat $\mathcal{O}_{Y}$-modules implies easily that
$\mathcal{H}_{\bullet}(\mathcal{K}_{\bullet} \otimes_{S} \mathcal{F}_{\bullet}')$ is a *homological functor* in
$\mathcal{F}_{\bullet}'$ (see the argument of `(7.7.1)`). It is this property which, as has been mentioned in `(6.1.1)`,
is the motivation for the introduction of hypertor. Indeed, set

```text
  X = X^{(1)} ×_S X^{(2)} ×_S ⋯ ×_S X^{(n)},   f = f_1 ×_S f_2 ×_S ⋯ ×_S f_n,
  𝒫_• = 𝒫_•^{(1)} ⊗_S 𝒫_•^{(2)} ⊗_S ⋯ ⊗_S 𝒫_•^{(n)},
  X' = X ×_S S',   Y' = Y ×_S S',   f' = f ×_S 1_{S'};
```

the base-change problems lead one to study the hypercohomology $\mathcal{H}_{\bullet}(f', \mathcal{P}_{\bullet}'
\otimes_{S} \mathcal{F}')$ as a functor with respect to the quasi-coherent $\mathcal{O}_{S'}$-module $\mathcal{F}'$, or
equivalently the hypercohomology $\mathcal{H}_{\bullet}(f, \mathcal{P}_{\bullet} \otimes_{S} \mathcal{F})$ as a functor
in the quasi-coherent $\mathcal{O}_{S}$-module $\mathcal{F}$. When the $\mathcal{P}^{(i)}_{\bullet}$ (hence also
$\mathcal{P}_{\bullet}$) are $S$-flat, it follows from what precedes and from `(6.7.6)` that this functor is indeed a
*cohomological functor* in $\mathcal{F}$; but this is no longer the case when one drops the flatness hypothesis on the
$\mathcal{P}^{(i)}_{\bullet}$, and one can then no longer approach the study of $\mathcal{H}_{\bullet}(f,
\mathcal{P}_{\bullet} \otimes_{S} \mathcal{F})$ by the usual methods of Homological Algebra.

We shall however have above all to use the case where $n = 1$, $Y = S$, and where $\mathcal{P}_{\bullet}$ is formed of
$Y$-flat $\mathcal{O}_{X}$-modules. We have in this case the

**Theorem (6.10.5).**

<!-- label: III.6.10.5 -->

— *Let $Y = \operatorname{Spec}(A)$ be a noetherian affine scheme, $f : X \to Y$ a proper morphism,
$\mathcal{P}_{\bullet}$ a complex of $\mathcal{O}_{X}$-modules coherent, flat over $Y$, bounded below. There then exists
a complex $\mathcal{L}_{\bullet}$ of $\mathcal{O}_{Y}$-modules, bounded below, whose terms $\mathcal{L}_{i}$ are
$\mathcal{O}_{Y}$-modules of the form $\mathcal{O}^{n_{i}}_{Y}$, and an isomorphism*

```text
  ℋ^•(f, 𝒫_• ⊗_Y 𝒬_•) ⥲ ℋ_•(ℒ_• ⊗_Y 𝒬_•)                                                   (6.10.5.1)
```

*of $\partial$-functors in the complex $\mathcal{Q}_{\bullet}$ of $\mathcal{O}_{Y}$-modules quasi-coherent, bounded
below. Moreover, for every morphism $u : Y' \to Y$, setting*

```text
  X' = X_{(Y')},   f' = f_{(Y')},   𝒫_•' = 𝒫_• ⊗_Y 𝒪_{Y'},   ℒ_•' = u^*(ℒ_•)
```

<!-- original page 42 -->

*(which is a complex of $\mathcal{O}_{Y'}$-modules locally free of finite type), one has an isomorphism*

```text
  ℋ^•(f', 𝒫_•' ⊗_{Y'} 𝒬_•') ⥲ ℋ_•(ℒ_•' ⊗_{Y'} 𝒬_•')                                         (6.10.5.2)
```

*of $\partial$-functors in the complex $\mathcal{Q}_{\bullet}'$ of $\mathcal{O}_{Y'}$-modules quasi-coherent, bounded
below, in such a way that the diagram*

```text
  ℋ^•(f, 𝒫_• ⊗_Y 𝒬_•)              ⥲              ℋ_•(ℒ_• ⊗_Y 𝒬_•)

           │                                              │                                  (6.10.5.3)

           ↓                                              ↓

  ℋ^•(f', 𝒫_•' ⊗_{Y'} u^*(𝒬_•))    ⥲              ℋ_•(ℒ_•' ⊗_{Y'} u^*(𝒬_•))
```

*is commutative.*

**Proof.** The application of `(6.10.1)` gives first a complex $\mathcal{K}_{\bullet}$, bounded below `(6.10.2)`, of
quasi-coherent and $Y$-flat $\mathcal{O}_{Y}$-modules `(6.10.3, (iii))` and an isomorphism

```text
  ℋ^•(f, 𝒫_• ⊗_Y 𝒬_•) ⥲ ℋ_•(𝒦_• ⊗_Y 𝒬_•)                                                   (6.10.5.4)
```

of $\partial$-functors in $\mathcal{Q}_{\bullet}$, but *a priori* the terms of $\mathcal{K}_{\bullet}$ are not
necessarily $\mathcal{O}_{Y}$-modules of finite type. But if one applies `(6.10.5.4)` to the case where
$\mathcal{Q}_{\bullet}$ is a complex reduced to a single term $\mathcal{O}_{Y}$, one sees that
$\mathcal{H}_{\bullet}(\mathcal{K}_{\bullet})$ is isomorphic to $\mathcal{H}^{\bullet}(f, \mathcal{P}_{\bullet})$, and
is consequently formed of *coherent* $\mathcal{O}_{Y}$-modules `(6.2.5)`. One knows then $(0_{III}, 11.9.2)$ that there
exists a complex $\mathcal{L}_{\bullet}$, bounded below, formed of $\mathcal{O}_{Y}$-modules associated to *free
$A$-modules of finite type*, and a homomorphism $\mathcal{L}_{\bullet} \to \mathcal{K}_{\bullet}$, such that the
corresponding homomorphism for homology, $\mathcal{H}_{\bullet}(\mathcal{L}_{\bullet}) \to
\mathcal{H}_{\bullet}(\mathcal{K}_{\bullet})$, is bijective; whence the isomorphism `(6.10.5.1)`, by virtue of
`(6.10.3, (ii))`. The other assertions of `(6.10.5)` follow from `(6.10.1)` and `(6.10.3, (ii))` *when $Y'$ is affine*;
in the general case, it suffices to verify that, when one considers a cover $(V_{\alpha})$ of $Y'$ by affine opens, and
the corresponding isomorphism `(6.10.5.2)` relative to each of the $V_{\alpha}$, the restrictions to an affine open $W
\subset V_{\alpha} \cap V_{\beta}$ of the isomorphisms corresponding to $V_{\alpha}$ and to $V_{\beta}$ *coincide* with
the isomorphism corresponding to $W$, which follows from the commutativity of the diagram `(6.10.1.2)` applied to the
canonical injections $W \to V_{\alpha}$ and $W \to V_{\beta}$. ∎

**Remark (6.10.6).**

<!-- label: III.6.10.6 -->

— In the following chapters, we shall apply `(6.10.5)` above all to the case where $\mathcal{P}_{\bullet}$ is reduced to
a single coherent $\mathcal{O}_{X}$-module $\mathcal{F}$, flat over $Y$. Since one then has
$\mathcal{H}_{n}(\mathcal{L}_{\bullet}) = \mathcal{H}^{-n}(f, \mathcal{F}) = R^{-n} f_{*}(\mathcal{F})$ `(6.2.1)`, one
sees that the $\mathcal{H}_{n}(\mathcal{L}_{\bullet})$ are zero for $n > 0$; we shall see later `(7.7.12, (i))` that one
may then suppose that $\mathcal{L}_{\bullet}$ has only terms of degrees $\geq 0$ (hence finitely many), provided that
one replaces the hypothesis that the $\mathcal{L}_{i}$ are associated to free $A$-modules of finite type by the
hypothesis that the $\mathcal{L}_{i}$ are *locally free of finite type*.

The complex $\mathcal{L}_{\bullet}$ corresponding to such an $\mathcal{O}_{X}$-module $\mathcal{F}$ does not appear to
possess any

<!-- original page 43 -->

particular property, beyond the preceding restriction on the degrees. One may then ask whether, conversely, given a
complex $\mathcal{L}_{\bullet}$ formed of $\mathcal{O}_{Y}$-modules associated to projective $A$-modules of finite type,
bounded below and whose terms of degree `> 0` are zero, there exists a $Y$-scheme $X$, projective and flat over $Y$, and
an $\mathcal{O}_{X}$-module $\mathcal{F}$ locally free, such that there is an isomorphism $\mathcal{H}^{\bullet}(f,
\mathcal{F} \otimes_{Y} \mathcal{Q}_{\bullet}) \xrightarrow{\sim} \mathcal{H}_{\bullet}(\mathcal{L}_{\bullet}
\otimes_{Y} \mathcal{Q}_{\bullet})$ functorial in $\mathcal{Q}_{\bullet}$. The interest of such a result would be to
reduce completely the cohomological theory of $Y$-flat coherent modules on proper $Y$-schemes to the theory "up to
homotopy" of complexes of projective $A$-modules of finite type on a noetherian ring $A$.

[^1]: The case treated in `(6.9.8)`, and in particular the spectral sequences `(6.9.8.3)` and `(6.9.8.4)`, had been
    pointed out to us in 1957 by J.-P. Serre.

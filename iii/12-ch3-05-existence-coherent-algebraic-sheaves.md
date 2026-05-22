# §5. An existence theorem for coherent algebraic sheaves

<!-- original page 149 -->

## 5.1. Statement of the theorem

**(5.1.1)**

<!-- label: III.5.1.1 -->

Let $A$ be an *adic Noetherian* ring, $\mathfrak{J}$ an ideal of definition of $A$, so that $A$ is separated and
complete for the $\mathfrak{J}$-adic topology. If $Y = \operatorname{Spec}(A)$, the affine formal scheme $Spf(A)$ is
identified with the completion `Ŷ` of $Y$ along the closed subset $Y' = V(\mathfrak{J})$ `(I, 10.10.1)`. Let $X$ be a
(usual) $Y$-prescheme of finite type, $f : X \to Y$ the structure morphism; we shall denote by $\mathfrak{X}$ the
completion of $X$ along the closed subset $X' = f^{-1}(Y')$, or equivalently the `Ŷ`-formal prescheme $X \times_{Y}
\hat{Y}$; by $\hat{f} : \mathfrak{X} \to \hat{Y}$ the extension of $f$ to the completions; finally, for every coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$, we shall denote by $\hat{\mathcal{F}}$ its completion $\mathcal{F}_{/X'}$, which
is a coherent $\mathcal{O}_{\mathfrak{X}}$-module.

**Proposition (5.1.2).**

<!-- label: III.5.1.2 -->

*The hypotheses and notation being those of (5.1.1), let $\mathcal{F}$ be a coherent $\mathcal{O}_{X}$-module whose
support is proper over $Y$ `(II, 5.4.10)`. The canonical homomorphisms (4.1.4)*

```text
  ρ_i : H^i(X, ℱ) → H^i(𝔛, 𝓕̂)
```

*are then isomorphisms.*

**Proof.** Since $H^{i}(X, \mathcal{F})$ is an $A$-module of finite type (3.2.4), hence identical to its Hausdorff
completion for the $\mathfrak{J}$-preadic topology $(0_{I}, 7.3.6)$, the proposition is only a particular case of
(4.1.10).

Recall that the canonical isomorphisms $\rho_{i}$ commute with the coboundaries for every exact sequence $0 \to
\mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ of coherent $\mathcal{O}_{X}$-modules (`(0, 12.1.6)` and
`(I, 10.8.9)`).

**Corollary (5.1.3).**

<!-- label: III.5.1.3 -->

*Let $\mathcal{F}$, $\mathcal{G}$ be two coherent $\mathcal{O}_{X}$-modules such that the intersection of their supports
is proper over $Y$. Then the canonical homomorphism*

```text
  Hom_{𝒪_X}(ℱ, 𝒢) → Hom_{𝒪_𝔛}(𝓕̂, 𝓖̂)                                          (5.1.3.1)
```

*which associates to every homomorphism $u : \mathcal{F} \to \mathcal{G}$ its completion $\hat{u} : \hat{\mathcal{F}}
\to \hat{\mathcal{G}}$, is an isomorphism. Moreover, when the morphism $f$ is closed, in order that `û` be injective
(resp. surjective) it is necessary and sufficient that $u$ be so.*

**Proof.** The first assertion is a particular case of (4.5.3), again due to the fact that the first member of (5.1.3.1)
is an $A$-module of finite type, hence identical to its Hausdorff completion. To prove the second, note by virtue of
`(I, 10.8.14)` that `û` is injective (resp. surjective) if and only if there exists a neighbourhood of $X'$ in which $u$
is injective (resp. surjective).

<!-- original page 150 -->

The conclusion therefore follows from the following lemma:

**Lemma (5.1.3.1).**

<!-- label: III.5.1.3.1 -->

*Under the hypotheses of (5.1.1), if one assumes in addition that the morphism $f$ is closed, then every neighbourhood
of $X'$ in $X$ is identical to $X$.*

**Proof.** First, we may reduce to the case where $f(X) = Y$. Indeed, by hypothesis, $f(X)$ is a closed subset $Z$ of
$Y$; we may in addition replace $f$ by $f_{red}$ `(I, 6.3.4)`, and suppose consequently $X$ and $Y$ reduced; we may then
replace $Y$ by the reduced closed subprescheme of $Y$ with $Z$ as underlying space `(I, 5.2.2)`, since every ideal of
$A$ is closed, and every quotient ring of $A$ is therefore adic and Noetherian. One then has $f(X') = Y'$; if $V$ is an
open neighbourhood of $X'$ in $X$, $f(X - V)$ is closed in $Y$ by hypothesis, and does not meet $Y'$; but this is
impossible unless $X - V$ is empty, since $\mathfrak{J}$ is contained in the radical of $A$ `(I, 1.1.15` and
`0_I, 7.1.10)`, whence the conclusion.

When one restricts to coherent $\mathcal{O}_{X}$-modules whose support is proper over $Y$, (5.1.3) can be stated, in the
language of categories, by saying that the functor $\mathcal{F} \mapsto \hat{\mathcal{F}}$ is *fully faithful* from the
category of $\mathcal{O}_{X}$-modules of the preceding type into the category of coherent
$\mathcal{O}_{\mathfrak{X}}$-modules, and consequently establishes an *equivalence* of the first of these categories
with a *full* subcategory of the second `(0, 8.1.6)`. The existence theorem will prove that when $X$ is proper over $Y$,
this subcategory is in fact the category of *all* coherent $\mathcal{O}_{\mathfrak{X}}$-modules. More precisely:

**Theorem (5.1.4).**

<!-- label: III.5.1.4 -->

*Let $A$ be an adic Noetherian ring, $Y = \operatorname{Spec}(A)$, $\mathfrak{J}$ an ideal of definition of $A$, $Y' =
V(\mathfrak{J})$, $f : X \to Y$ a separated morphism of finite type, $X' = f^{-1}(Y')$. Let $\hat{Y} = Y_{/Y'} =
Spf(A)$, $\mathfrak{X} = X_{/X'}$ be the completions of $Y$ and $X$ along $Y'$ and $X'$, $\hat{f} : \mathfrak{X} \to
\hat{Y}$ the extension of $f$ to the completions; then the functor $\mathcal{F} \mapsto \hat{\mathcal{F}} =
\mathcal{F}_{/X'}$ is an equivalence of the category of coherent $\mathcal{O}_{X}$-modules of support proper over
$\operatorname{Spec}(A)$ with the category of coherent $\mathcal{O}_{\mathfrak{X}}$-modules of support proper over
$Spf(A)$.*

In other words, taking (5.1.3) into account:

**Corollary (5.1.5).**

<!-- label: III.5.1.5 -->

*For an $\mathcal{O}_{\mathfrak{X}}$-module to be isomorphic to the completion of an $\mathcal{O}_{X}$-module which is
coherent and of support proper over $\operatorname{Spec}(A)$, it is necessary and sufficient that it be coherent and of
support proper over $Spf(A)$.*

The most important case is the:

**Corollary (5.1.6).**

<!-- label: III.5.1.6 -->

*Suppose $X$ proper over $Y = \operatorname{Spec}(A)$. Then the functor $\mathcal{F} \mapsto \hat{\mathcal{F}}$ is an
equivalence of the category of coherent $\mathcal{O}_{X}$-modules and of the category of coherent
$\mathcal{O}_{\mathfrak{X}}$-modules.*

**Scholium (5.1.7).**

<!-- label: III.5.1.7 -->

If one takes into account the characterization of coherent sheaves on formal preschemes `(I, 10.11.3)`, one sees that
under the conditions of (5.1.1), the data of a coherent $\mathcal{O}_{\mathfrak{X}}$-module of support proper over
$\operatorname{Spec}(A)$ is equivalent (on setting $Y_{n} = \operatorname{Spec}(A/\mathfrak{J}^{n+1})$ and $X_{n} = X
\times_{Y} Y_{n}$) to the data of a projective system of coherent $\mathcal{O}_{X_{n}}$-modules $(\mathcal{F}_{n})$ such
that for $m \leq n$ one has $\mathcal{F}_{m} = \mathcal{F}_{n} \otimes_{\mathcal{O}_{Y_{n}}} \mathcal{O}_{Y_{m}}$ (or
equivalently $\mathcal{F}_{m} = \mathcal{F}_{n} / \mathfrak{J}^{m+1} \mathcal{F}_{n}$) and that the support of
$\mathcal{F}_{0}$ is a part of `X_0` proper over `Y_0`. By means of `(I, 10.11.4)`, one likewise interprets
homomorphisms of coherent $\mathcal{O}_{\mathfrak{X}}$-modules as homomorphisms of projective systems of coherent
$\mathcal{O}_{X_{n}}$-modules.

<!-- original page 151 -->

In all known cases of application, $A$ is in fact an *adic local Noetherian* ring, so the $Y_{n}$ are spectra of
*artinian local rings*, and the results of this section and the preceding ones reduce in large measure algebraic
geometry over an adic local Noetherian ring to algebraic geometry over artinian local rings.

**Corollary (5.1.8).**

<!-- label: III.5.1.8 -->

*Under the conditions of (5.1.4), the map $Z \mapsto \hat{Z} = Z_{/(Z \cap X')}$ is a bijection of the set of closed
subpreschemes $Z$ of $X$, proper over $Y$, onto the set of closed formal subpreschemes of $\mathfrak{X}$, proper over
`Ŷ`.*

**Proof.** Indeed, a closed formal subprescheme of $\mathfrak{X}$ is of the form $(\mathfrak{T},
(\mathcal{O}_{\mathfrak{X}}/\mathcal{A}) | \mathfrak{T})$, where $\mathcal{A}$ is a coherent Ideal of
$\mathcal{O}_{\mathfrak{X}}$ `(I, 10.14.2)`; if $\mathfrak{T}$ is proper over `Ŷ`, it follows from (5.1.4) that
$\mathcal{O}_{\mathfrak{X}} / \mathcal{A}$ is isomorphic to an $\mathcal{O}_{\mathfrak{X}}$-module of the form
$\hat{\mathcal{F}}$, where $\mathcal{F}$ is a coherent $\mathcal{O}_{X}$-module of support proper over $Y$; in addition,
it follows from (5.1.3) that the canonical homomorphism $\mathcal{O}_{\mathfrak{X}} \to
\mathcal{O}_{\mathfrak{X}}/\mathcal{A}$ is of the form `û`, where $u : \mathcal{O}_{X} \to \mathcal{F}$ is a
*surjective* homomorphism of $\mathcal{O}_{X}$-modules. Hence $\mathcal{F}$ is of the form $\mathcal{O}_{X} /
\mathcal{N}$, where $\mathcal{N}$ is a coherent Ideal of $\mathcal{O}_{X}$, and $\mathcal{A} = \hat{\mathcal{N}}$
`(I, 10.8.8)`, whence the conclusion `(I, 10.14.7)`.

## 5.2. Proof of the existence theorem: projective and quasi-projective cases

**(5.2.1)**

<!-- label: III.5.2.1 -->

Under the conditions of (5.1.4), we shall say *provisionally* that a coherent $\mathcal{O}_{\mathfrak{X}}$-module is
*algebraizable* if it is isomorphic to a completion $\hat{\mathcal{F}}$ of a coherent $\mathcal{O}_{X}$-module
$\mathcal{F}$ of support proper over $Y$.

**Lemma (5.2.2).**

<!-- label: III.5.2.2 -->

*Let $\mathcal{F}'$, $\mathcal{G}'$ be two algebraizable $\mathcal{O}_{\mathfrak{X}}$-modules. For every homomorphism
$u : \mathcal{F}' \to \mathcal{G}'$, $Ker(u)$, $Im(u)$ and $Coker(u)$ are algebraizable.*

**Proof.** Indeed, if $\mathcal{F}' = \hat{\mathcal{F}}$, $\mathcal{G}' = \hat{\mathcal{G}}$, where $\mathcal{F}$ and
$\mathcal{G}$ are coherent $\mathcal{O}_{X}$-modules of supports proper over $Y$, one has $u = \hat{v}$, where $v :
\mathcal{F} \to \mathcal{G}$ is a homomorphism (5.1.3). By virtue of the exactness of the functor $\mathcal{F} \mapsto
\hat{\mathcal{F}}$, $Ker(u)$ is isomorphic to $\hat{Ker(v)}$, and since the support of $Ker(v)$ is contained in that of
$\mathcal{F}$, one sees that $Ker(u)$ is algebraizable; analogous proof for $Im(u)$ and $Coker(u)$.

**Proposition (5.2.3).**

<!-- label: III.5.2.3 -->

*Let $A$ be an adic Noetherian ring, $\mathfrak{J}$ an ideal of definition of $A$, $\mathfrak{Y} = Spf(A)$, $f :
\mathfrak{X} \to \mathfrak{Y}$ a proper morphism of formal preschemes. Set $Y_{k} =
\operatorname{Spec}(A/\mathfrak{J}^{k+1})$, $X_{k} = \mathfrak{X} \times_{\mathfrak{Y}} Y_{k}$, and for every
$\mathcal{O}_{\mathfrak{X}}$-module $\mathcal{F}$, $\mathcal{F}_{k} = \mathcal{F} \otimes_{\mathcal{O}_{\mathfrak{X}}}
\mathcal{O}_{X_{k}} = \mathcal{F} / \mathfrak{J}^{k+1} \mathcal{F}$. Let $\mathcal{L}$ be an invertible
$\mathcal{O}_{\mathfrak{X}}$-module, and suppose that $\mathcal{L}_{0} = \mathcal{L}/\mathfrak{J}\mathcal{L}$ is an
ample $\mathcal{O}_{X_{0}}$-module; for every $\mathcal{O}_{\mathfrak{X}}$-module $\mathcal{F}$ and every integer $n$,
set $\mathcal{F}(n) = \mathcal{F} \otimes \mathcal{L}^{\otimes n}$. Then, for every coherent
$\mathcal{O}_{\mathfrak{X}}$-module $\mathcal{F}$, there exists an integer $n_{0}$ such that, for every $n \geq n_{0}$,
the following properties hold:*

*(i) The canonical homomorphism $H^{0}(\mathfrak{X}, \mathcal{F}(n)) \to H^{0}(\mathfrak{X}, \mathcal{F}_{k}(n))$ is
surjective for every $k \geq 0$.*

*(ii) One has $H^{q}(\mathfrak{X}, \mathcal{F}(n)) = 0$ for every $q > 0$.*

**Proof.** We know that the underlying spaces of $\mathfrak{X}$ and `X_0` are the same; the sheaves $\mathcal{M}_{k} =
\mathfrak{J}^{k} \mathcal{F} / \mathfrak{J}^{k+1} \mathcal{F}$, being annihilated by $\mathfrak{J}$, may be considered
as coherent $\mathcal{O}_{X_{0}}$-modules $(0_{I}, 5.3.10)$; in addition, if one sets $\mathcal{M}_{k}(n) =
\mathcal{M}_{k} \otimes_{\mathcal{O}_{X_{0}}} \mathcal{L}^{\otimes n}_{0}$, one sees at once that $\mathcal{M}_{k}(n) =
\mathfrak{J}^{k} \mathcal{F}(n) / \mathfrak{J}^{k+1} \mathcal{F}(n)$. Note that, since $\mathcal{L}_{0}$ is ample for
$f_{0} : X_{0} \to Y_{0}$, and

<!-- original page 152 -->

$f_{0}$ is proper, we conclude that $f_{0}$ is *projective* `(II, 5.5.4)`. Let $\mathcal{S} = \oplus_{k \geq 0}
\mathfrak{J}^{k} / \mathfrak{J}^{k+1}$ be the graded $A$-algebra associated to the $\mathfrak{J}$-adic filtration of
$A$, which is of finite type since $A$ is Noetherian; if one sets $\mathcal{S}' = f^{*}_{0}(\tilde{\mathcal{S}})$,
$\mathcal{S}'$ is a quasi-coherent $\mathcal{O}_{X_{0}}$-algebra of finite type, and $\mathcal{M} = \oplus_{k \geq 0}
\mathcal{M}_{k}$ a graded quasi-coherent $\mathcal{S}'$-module of finite type (since $\mathcal{F}_{0}$ is coherent and
generates the $\mathcal{S}'$-module $\mathcal{M}$). We are therefore in the conditions of application of theorem (2.4.1,
(ii)), and we conclude that there exists $n_{0}$ such that, for $n \geq n_{0}$ and for every $k$, one has

```text
  H^q(X_0, ℳ_k(n)) = 0           for every q > 0.                              (5.2.3.1)
```

One therefore also has $H^{q}(\mathfrak{X}, \mathcal{M}_{k}(n)) = 0$ for $q > 0$ and $n \geq n_{0}$,
$\mathcal{M}_{k}(n)$ being this time considered as $\mathcal{O}_{\mathfrak{X}}$-module. Applying the exact cohomology
sequence to

```text
  0 → 𝔍^h 𝓕(n) / 𝔍^{k+1} 𝓕(n) → 𝔍^h 𝓕(n) / 𝔍^k 𝓕(n) →
                                              𝔍^k 𝓕(n) / 𝔍^{k+1} 𝓕(n) → 0,
```

one deduces first that for $0 \leq h < k$, $n \geq n_{0}$ and $q > 0$, one has, by induction on $k - h$,

```text
  H^q(𝔛, 𝔍^h 𝓕(n) / 𝔍^k 𝓕(n)) = 0                                              (5.2.3.2)
```

and in particular for $h = 0$,

```text
  H^q(𝔛, 𝓕_k(n)) = 0           for n ≥ n_0, k ≥ 0 and q > 0.                   (5.2.3.3)
```

Another portion of the exact cohomology sequence, for $h = 0$, gives the exact sequence

```text
  H^0(𝔛, 𝓕_{k+1}(n)) → H^0(𝔛, 𝓕_k(n)) → H^1(𝔛, 𝔍^k 𝓕(n) / 𝔍^{k+1} 𝓕(n)) = 0,   (5.2.3.4)
```

whence one deduces that for $h \leq k$, the canonical map

```text
  H^0(𝔛, 𝓕_{k+1}(n)) → H^0(𝔛, 𝓕_h(n))                                          (5.2.3.5)
```

is surjective. For every $q$, the projective system $(H^{q}(\mathfrak{X}, \mathcal{F}_{k}(n)))_{k \geq 0}$ therefore
satisfies condition `(ML)` for $n \geq n_{0}$. Moreover, every formal affine open $U$ of $\mathfrak{X}$ is also an
affine open in each of the $X_{k}$ `(I, 10.5.2)`, hence one has $H^{q}(U, \mathcal{F}_{k}(n)) = 0$ for every $q > 0$
(1.3.1), and $H^{0}(U, \mathcal{F}_{k+1}(n)) \to H^{0}(U, \mathcal{F}_{k}(n))$ is surjective for $h \leq k$
`(I, 1.3.9)`. The conditions of application of $(0_{III}, 13.3.1)$ are consequently fulfilled, and we conclude that, for
$n \geq n_{0}$:

1° For every $q > 0$, $H^{q}(\mathfrak{X}, \mathcal{F}(n)) \to \varprojlim H^{q}(\mathfrak{X}, \mathcal{F}_{k}(n))$ is
bijective, hence, by virtue of (5.2.3.3), $H^{q}(\mathfrak{X}, \mathcal{F}(n)) = 0$.

2° The homomorphism $H^{0}(\mathfrak{X}, \mathcal{F}(n)) \to \varprojlim H^{0}(\mathfrak{X}, \mathcal{F}_{k}(n))$ is
bijective; moreover, since the homomorphisms (5.2.3.5) are surjective, so is each of the homomorphisms

```text
  lim_← H^0(𝔛, 𝓕_k(n)) → H^0(𝔛, 𝓕_h(n)),
```

which completes the proof.

**Corollary (5.2.4).**

<!-- label: III.5.2.4 -->

*The hypotheses being those of (5.2.3), for every coherent $\mathcal{O}_{\mathfrak{X}}$-module $\mathcal{F}$, there
exists an integer $N$ such that for $n \geq N$, $\mathcal{F}(n)$ is generated by its sections above*

<!-- original page 153 -->

*$\mathfrak{X}$; in other words, $\mathcal{F}$ is isomorphic to the quotient of an $\mathcal{O}_{\mathfrak{X}}$-module
of the form $(\mathcal{L}^{\otimes(-n)})^{h}$.*

**Proof.** Since `X_0` is Noetherian, it follows from the hypothesis on $\mathcal{L}_{0}$ and from `(II, 4.5.5)` that
there exists $n_{0}$ such that, for $n \geq n_{0}$, $\mathcal{F}_{0}(n)$ is generated by its sections above `X_0`;
moreover, one may suppose $n_{0}$ chosen large enough that the homomorphism $\Gamma(\mathfrak{X}, \mathcal{F}(n)) \to
\Gamma(X_{0}, \mathcal{F}_{0}(n))$ is surjective for $n \geq n_{0}$ (5.2.3). There thus exists a finite number of
sections $s_{i} \in \Gamma(\mathfrak{X}, \mathcal{F}(n))$ whose images in $\Gamma(X_{0}, \mathcal{F}_{0}(n))$ generate
$\mathcal{F}_{0}(n)$ $(0_{I}, 5.2.3)$. Since $\mathfrak{J}$ is contained in the maximal ideal of the local ring at every
point of $\mathfrak{X}$, it follows from Nakayama's lemma, applied to these local rings, that the $s_{i}$ generate
$\mathcal{F}(n)$ $(0_{I}, 5.1.1)$.

**(5.2.5) Proof of the existence theorem: projective case.**

<!-- label: III.5.2.5 -->

The notation being that of (5.1.4), suppose $f$ *projective*, so that there exists an ample $\mathcal{O}_{X}$-module
$\mathcal{L}$ `(I, 5.5.4)`. By definition, $X_{n} = X \times_{Y} Y_{n}$ is equal to the closed subprescheme $X_{n}
\times_{Y} Y_{n} = f^{-1}(Y_{n})$ of $X$; if $\mathcal{L}'$ is the completion $\mathcal{L} \otimes_{\mathcal{O}_{X}}
\mathcal{O}_{\mathfrak{X}}$ of $\mathcal{L}$, one has $\mathcal{L}'_{0} = \mathcal{L} / \mathfrak{J}\mathcal{L}$,
considered as $\mathcal{O}_{X_{0}}$-module; one knows that $\mathcal{L}'_{0}$ is ample `(II, 4.6.13, (i bis))`. One may
therefore apply to $\mathcal{L}'$ and to every coherent $\mathcal{O}_{\mathfrak{X}}$-module $\mathcal{F}$ Corollary
(5.2.4); one sees thus that $\mathcal{F}$ is isomorphic to a quotient of $\mathcal{G} =
(\mathcal{L}'^{\otimes(-n)})^{k}$ for suitable integers $n > 0$ and $k > 0$. Now, it is clear that $\mathcal{G}$ is the
completion of $(\mathcal{L}^{\otimes(-n)})^{k}$ `(I, 10.8.10)`, and is therefore algebraizable. Next consider the
canonical surjective homomorphism $u : \mathcal{G} \to \mathcal{F}$, and let $\mathcal{H} = Ker(u)$, which is a coherent
$\mathcal{O}_{\mathfrak{X}}$-module $(0_{I}, 5.3.4)$. One sees in the same way that there exists an algebraizable
$\mathcal{O}_{\mathfrak{X}}$-module $\mathcal{K}$ and a homomorphism $v : \mathcal{K} \to \mathcal{G}$ such that
$\mathcal{H} = Im(v)$. One then has $\mathcal{F} = Coker(v)$, and $\mathcal{F}$ is algebraizable by virtue of (5.2.2).

**(5.2.6) Proof of the existence theorem: quasi-projective case.**

<!-- label: III.5.2.6 -->

The notation being still that of (5.1.4), suppose now that $f$ is *quasi-projective*. Then there exists a projective
morphism $g : Z \to Y$ such that $X$ is identified with the $Y$-prescheme induced on an open subset of $Z$
`(II, 5.3.2)`; if one sets $Z' = g^{-1}(Y')$, one has $X' = X \cap Z'$. Consequently, the completion $\mathfrak{X} =
X_{/X'}$ is identified with the formal prescheme induced by the completion $\mathfrak{J} = Z_{/Z'}$ on the open subset
$X \cap Z'$ of $\mathfrak{J}$ `(I, 10.8.5)`. Let $\mathcal{F}$ be a coherent $\mathcal{O}_{\mathfrak{X}}$-module whose
support $T'$ is proper over `Ŷ`; this means by definition that there exists a closed subprescheme of $X'$, having $T'
\subset X'$ as underlying space, such that the restriction $T' \to Y'$ of $f$ is proper; it follows that $T'$ is proper
over $Y$, hence *closed* in $Z'$ `(II, 5.4.10)`. It follows that $\mathcal{F}$ is the sheaf induced on $\mathfrak{X}$ by
the $\mathcal{O}_{\mathfrak{J}}$-module $\mathcal{F}'$ obtained by glueing of $\mathcal{F}$ (defined on the open subset
$\mathfrak{X}$ of $\mathfrak{J}$) and the sheaf `0` on the open subset $\mathfrak{J} - T'$ of $\mathfrak{J}$, these two
sheaves coinciding on the intersection open subset $\mathfrak{X} - T'$. It is clear that $\mathcal{F}'$ is coherent; by
virtue of (5.2.5), there exists a coherent $\mathcal{O}_{Z}$-module $\mathcal{G}$ such that $\mathcal{F}' =
\hat{\mathcal{G}}$; let $T$ be the support of $\mathcal{G}$, so that $T' = T \cap Z'$ `(I, 10.8.12)`. If $h$ is the
restriction of $g$ to the reduced closed subprescheme of $Z$ having $T$ as underlying space, one then has $T' =
h^{-1}(Y') = T \cap g^{-1}(Y')$, and consequently $X \cap T$ is an open subset of $T$ containing $T'$.

<!-- original page 154 -->

Since $h$ is proper `(II, 5.4.2)`, hence closed, it follows from (5.1.3.1) that $X \cap T = T$; in other words $T
\subset X$, and since $T$ is closed in $Z$, $T$ is proper over $Y$. If $\mathcal{F}$ is the sheaf induced on $X$ by
$\mathcal{G}$, its completion $\hat{\mathcal{F}}$ is induced on $\mathfrak{X}$ by $\hat{\mathcal{G}}$ `(I, 10.8.4)`,
hence is equal to $\mathcal{F}'$, which completes the proof.

## 5.3. Proof of the existence theorem: general case

**Lemma (5.3.1).**

<!-- label: III.5.3.1 -->

*Under the conditions of (5.1.4), if $0 \to \mathcal{H} \to \mathcal{F} \to \mathcal{G} \to 0$ is an exact sequence of
coherent $\mathcal{O}_{\mathfrak{X}}$-modules such that $\mathcal{G}$ and $\mathcal{H}$ are algebraizable, then
$\mathcal{F}$ is algebraizable.*

**Proof.** Indeed, suppose $\mathcal{G} = \hat{\mathcal{B}}$, $\mathcal{H} = \hat{\mathcal{C}}$, where $\mathcal{B}$ and
$\mathcal{C}$ are coherent $\mathcal{O}_{X}$-modules with supports proper over $Y$; $\mathcal{F}$ canonically defines an
element of the $A$-module $Ext^{1}_{\mathcal{O}_{\mathfrak{X}}}(\mathfrak{X}; \hat{\mathcal{B}}, \hat{\mathcal{C}})$
`(0, 12.3.2)`, and the hypotheses imply that this $A$-module is canonically isomorphic to $Ext^{1}_{\mathcal{O}_{X}}(X;
\mathcal{B}, \mathcal{C})$ (4.5.2); there thus exists an exact sequence $0 \to \mathcal{C} \to \mathcal{A} \to
\mathcal{B} \to 0$ of coherent $\mathcal{O}_{X}$-modules such that the canonical image of the element of
$Ext^{1}_{\mathcal{O}_{X}}(X; \mathcal{B}, \mathcal{C})$ corresponding to $\mathcal{A}$ is the element of
$Ext^{1}_{\mathcal{O}_{\mathfrak{X}}}(\mathfrak{X}; \hat{\mathcal{B}}, \hat{\mathcal{C}})$ corresponding to
$\mathcal{F}$. But by definition (taking `(I, 10.8.8, (ii))` into account), this means that $\mathcal{F}$ is isomorphic
to $\hat{\mathcal{A}}$, whence the lemma, since $Supp(\mathcal{A})$ is contained in the union of $Supp(\mathcal{B})$ and
$Supp(\mathcal{C})$, hence is proper over $Y$.

**Corollary (5.3.2).**

<!-- label: III.5.3.2 -->

*Under the conditions of (5.1.1), let $u : \mathcal{F} \to \mathcal{G}$ be a homomorphism of coherent
$\mathcal{O}_{\mathfrak{X}}$-modules; if $\mathcal{G}$, $Ker(u)$ and $Coker(u)$ are algebraizable, then so is
$\mathcal{F}$.*

**Proof.** The lemma (5.2.2) applied to the homomorphism $\mathcal{G} \to Coker(u)$ shows indeed that $Im(u)$ is
algebraizable, and it then suffices to apply lemma (5.3.1) to the exact sequence $0 \to Ker(u) \to \mathcal{F} \to Im(u)
\to 0$.

**Lemma (5.3.3).**

<!-- label: III.5.3.3 -->

*Under the conditions of (5.1.1), let $h : Z \to Y$ be a morphism of finite type, $\mathfrak{z} = Z_{/Z'}$ the
completion of $Z$ along $Z' = h^{-1}(Y')$, $g : Z \to X$ a proper $Y$-morphism, $\hat{g} : \mathfrak{z} \to
\mathfrak{X}$ its extension to the completions. For every algebraizable $\mathcal{O}_{\mathfrak{z}}$-module
$\mathcal{F}'$, $\hat{g}_{*}(\mathcal{F}')$ is an algebraizable $\mathcal{O}_{\mathfrak{X}}$-module.*

**Proof.** Indeed, if $\mathcal{F}$ is a coherent $\mathcal{O}_{Z}$-module such that $\mathcal{F}' = \hat{\mathcal{F}}$,
it follows from the first comparison theorem (4.1.5) that $\hat{g}_{*}(\mathcal{F}')$ is isomorphic to the completion of
$g_{*}(\mathcal{F})$.

**Lemma (5.3.4).**

<!-- label: III.5.3.4 -->

*Let $X$ be a (usual) Noetherian scheme, $X'$ a closed subset of $X$, $f : Z \to X$ a proper morphism, $Z' =
f^{-1}(X')$, $\mathfrak{X} = X_{/X'}$, $\mathfrak{z} = Z_{/Z'}$, $\hat{f} : \mathfrak{z} \to \mathfrak{X}$ the extension
of $f$ to the completions. Let $\mathcal{M}$ be a coherent Ideal of $\mathcal{O}_{X}$ such that, if $U = X -
Supp(\mathcal{O}_{X} / \mathcal{M})$, the restriction $f^{-1}(U) \to U$ of $f$ is an isomorphism. Then, for every
coherent $\mathcal{O}_{\mathfrak{X}}$-module $\mathcal{F}$, there exists an integer $n > 0$ such that the kernel and
cokernel of the canonical homomorphism $\rho_{\mathcal{F}} : \mathcal{F} \to \hat{f}_{*}(\hat{f}^{*}(\mathcal{F}))$
$(0_{I}, 4.4.3)$ are annihilated by $\hat{\mathcal{M}}^{n}$.*

**Proof.** We may restrict to the case where $X = \operatorname{Spec}(B)$, $B$ a Noetherian ring, hence $X' =
V(\mathfrak{K})$, where $\mathfrak{K}$ is an ideal of $B$. We are going to see that one may reduce to the case where $B$
is an *adic Noetherian* ring and $\mathfrak{K}$ an ideal of definition of $B$. Indeed, let `B_1` be the Hausdorff
completion of $B$ for the $\mathfrak{K}$-preadic topology; if $\mathfrak{K}_{1} = \mathfrak{K} B_{1}$, `B_1` is
therefore an

<!-- original page 155 -->

adic Noetherian ring of which $\mathfrak{K}_{1}$ is an ideal of definition. Set $X_{1} = \operatorname{Spec}(B_{1})$ and
let $h : X_{1} \to X$ be the morphism corresponding to the canonical homomorphism $B \to B_{1}$; if $X'_{1} =
h^{-1}(X')$, one then has $X'_{1} = V(\mathfrak{K}_{1})$. Set finally $Z_{1} = Z \times_{X} X_{1} = Z_{(X_{1})}$, $f_{1}
= f_{(X_{1})} : Z_{1} \to X_{1}$, which is a proper morphism `(II, 5.4.2)`, and denote by $\mathfrak{X}_{1}$ the
completion of `X_1` along $X'_{1}$, by $\mathfrak{z}_{1} = Z_{1} \times_{X} \mathfrak{X}_{1}$ the completion of `Z_1`
along $Z'_{1} = f^{-1}_{1}(X'_{1})$, by $\hat{f}_{1}$ the extension of $f_{1}$ to the completions. It is immediate that
the extension $\hat{h} : \mathfrak{X}_{1} \to \mathfrak{X}$ of $h$ to the completions is an isomorphism, corresponding
to the identity map of `B_1` `(I, 10.9.1)`; one concludes that the corresponding homomorphism $\mathfrak{z}_{1} \to
\mathfrak{z}$ is also an isomorphism, these isomorphisms identifying $\hat{f}_{1}$ and $\hat{f}$. Finally,
$\mathcal{M}_{1} = h^{*}(\mathcal{M})$ is a coherent Ideal of $\mathcal{O}_{X_{1}}$ and $Supp(\mathcal{O}_{X_{1}} /
\mathcal{M}_{1}) = h^{-1}(Supp(\mathcal{O}_{X} / \mathcal{M}))$ `(I, 9.1.13)`, hence, if $U_{1} = X_{1} -
Supp(\mathcal{O}_{X_{1}} / \mathcal{M}_{1})$, one has $U_{1} = h^{-1}(U)$, whence it follows at once that the
restriction $f^{-1}_{1}(U_{1}) \to U_{1}$ of $f_{1}$ is an isomorphism `(I, 3.2.7)`; in addition, the completions
$\hat{\mathcal{M}}$ and $\hat{\mathcal{M}}_{1}$ are identified by `ĥ` `(I, 10.9.5)`. All hypotheses of (5.3.4) are
therefore fulfilled by `X_1`, $X'_{1}$, $f_{1}$ and $\mathcal{M}_{1}$, and one may therefore from now on suppose $B$
adic Noetherian and $\mathfrak{K}$ an ideal of definition of $B$. One then has $\mathfrak{X} = Spf(B)$, and $\mathcal{F}
= N^{\Delta}$, where $N$ is a $B$-module of finite type, whence $\mathcal{F} = \hat{\mathcal{G}}$, where $\mathcal{G}$
is the coherent $\mathcal{O}_{X}$-module `Ñ` `(I, 10.10.5)`, and consequently $\hat{f}^{*}(\mathcal{F}) =
\hat{f^{*}(\mathcal{G})}$ `(I, 10.9.5)`. In addition, by virtue of the first comparison theorem (4.1.5),
$\hat{f}_{*}(\hat{f^{*}(\mathcal{G})})$ is canonically identified with $\hat{f_{*}(f^{*}(\mathcal{G}))}$, and the
canonical homomorphism $\rho_{\mathcal{F}}$ is none other than $\hat{\rho}_{\mathcal{G}}$ by virtue of (5.1.3). Now, the
kernel $\mathcal{P}$ and the cokernel $\mathcal{Q}$ of $\rho_{\mathcal{G}} : \mathcal{G} \to f_{*}(f^{*}(\mathcal{G}))$
are coherent $\mathcal{O}_{X}$-modules, and by hypothesis their restrictions to $U$ are obviously zero. There thus
exists an integer $n > 0$ such that $\mathcal{M}^{n} \mathcal{P} = \mathcal{M}^{n} \mathcal{Q} = 0$ `(I, 9.3.4)`; one
concludes that $\hat{\mathcal{M}}^{n} \hat{\mathcal{P}} = \hat{\mathcal{M}}^{n} \hat{\mathcal{Q}} = 0$ `(I, 10.8.8` and
`10.8.10)`.

**5.3.5. End of the proof of the existence theorem.**

<!-- label: III.5.3.5 -->

The hypotheses being those of (5.1.4), we shall use the principle of Noetherian induction $(0_{I}, 2.2.2)$, supposing
therefore the theorem true for every closed subprescheme $T$ of $X$ whose underlying space is distinct from $X$ (the
completion $\mathfrak{T}$ being of course the completion of $T$ along $T \cap X'$). We may suppose $X$ non-empty. Since
$f$ is separated and of finite type, we may apply Chow's lemma `(II, 5.6.1)`: there thus exists a $Y$-scheme $Z$ and a
$Y$-morphism $g : Z \to X$ such that the structure morphism $h : Z \to Y$ is quasi-projective, the morphism $g$
projective and surjective, and in addition a non-empty open subset $U$ of $X$ such that the restriction $g^{-1}(U) \to
U$ is an isomorphism. Let $\mathcal{M}$ be a coherent Ideal of $\mathcal{O}_{X}$ defining a closed subprescheme of
underlying space $X - U$ `(I, 5.2.2)`, and let $\mathcal{F}$ be a coherent $\mathcal{O}_{\mathfrak{X}}$-module whose
support $E$ is proper over $Y$; denote by $\mathfrak{z}$ the completion of $Z$ along $h^{-1}(Y')$, by $\hat{g} :
\mathfrak{z} \to \mathfrak{X}$ the extension of $g$ to the completions. Then $\hat{g}^{*}(\mathcal{F})$ is a coherent
$\mathcal{O}_{\mathfrak{z}}$-module whose support is contained in $g^{-1}(E)$ and is consequently proper over $Y$, since
$g$ is projective, hence proper `(II, 5.4.6)`. Since $h$ is quasi-projective, $\hat{g}^{*}(\mathcal{F})$ is
algebraizable by virtue of (5.2.6). We conclude

<!-- original page 156 -->

that $\hat{g}_{*}(\hat{g}^{*}(\mathcal{F}))$ is an algebraizable $\mathcal{O}_{\mathfrak{X}}$-module (5.3.3) since $g$
is proper. We may now apply to $\mathcal{M}$ and to $g$ the result of (5.3.4): the kernel $\mathcal{P}$ and the cokernel
$\mathcal{Q}$ of the homomorphism $\rho_{\mathcal{F}} : \mathcal{F} \to \hat{g}_{*}(\hat{g}^{*}(\mathcal{F}))$ are
annihilated by a power $\hat{\mathcal{M}}^{n}$; let $T$ be the closed subprescheme of $X$ defined by $\mathcal{M}^{n}$,
having $X - U$ as underlying space, $j : T \to X$ the canonical injection, so that the extension to the completions
$\hat{j} : \mathfrak{T} \to \mathfrak{X}$ is the canonical injection `(I, 10.14.7)`. One may therefore write
$\mathcal{P} = \hat{j}_{*}(\hat{j}^{*}(\mathcal{P}))$ and $\mathcal{Q} = \hat{j}_{*}(\hat{j}^{*}(\mathcal{Q}))$, and
since $U$ is non-empty, it follows from the induction hypothesis that $\hat{j}^{*}(\mathcal{P})$ and
$\hat{j}^{*}(\mathcal{Q})$ are algebraizable $\mathcal{O}_{\mathfrak{T}}$-modules; by virtue of (5.3.3), $\mathcal{P}$
and $\mathcal{Q}$ are algebraizable, and one may then apply (5.3.2), which finally proves that $\mathcal{F}$ is
algebraizable. Q.E.D.

## 5.4. Application: comparison of morphisms of usual schemes and of morphisms of formal schemes. Algebraizable formal schemes

**Theorem (5.4.1).**

<!-- label: III.5.4.1 -->

*Let $A$ be an adic Noetherian ring, $\mathfrak{J}$ an ideal of definition of $A$, $S = \operatorname{Spec}(A)$, $S' =
V(\mathfrak{J})$. Let $u : X \to S$ be a proper morphism, $v : Y \to S$ a separated morphism of finite type, and let
`Ŝ`, $\mathfrak{X}$, $\mathfrak{Y}$ be the completions of $S$, $X$, $Y$ along $S'$, $u^{-1}(S')$, $v^{-1}(S')$
respectively. If, for every $S$-morphism $f : X \to Y$, $\hat{f} : \mathfrak{X} \to \mathfrak{Y}$ is the extension of
$f$ to the completions, the map $f \mapsto \hat{f}$ is a bijection*

```text
  Hom_S(X, Y) ⥲ Hom_Ŝ(𝔛, 𝔜).
```

**Proof.** Let us first show that $f \mapsto \hat{f}$ is *injective*. Suppose indeed that two $S$-morphisms $f$, $g$
from $X$ to $Y$ are such that $\hat{f} = \hat{g}$. One then knows `(I, 10.9.4)` that there exists an open neighbourhood
$V$ of $X' = u^{-1}(S')$ in which $f$ and $g$ coincide. Now, since $u$ is a closed map, one has $V = X$ (5.1.3.1),
whence $f = g$.

Let us now prove that $f \mapsto \hat{f}$ is *surjective*, and let $h$ therefore be an `Ŝ`-morphism $\mathfrak{X} \to
\mathfrak{Y}$. Let $Z = X \times_{S} Y$, and denote by $p : Z \to X$ and $q : Z \to Y$ the canonical projections; $Z$ is
of finite type over $S$ `(I, 6.3.4)`, hence Noetherian; denote by $\mathfrak{z}$ its completion along $Z' =
p^{-1}(u^{-1}(S'))$; one knows that $\mathfrak{z}$ is canonically identified with $\mathfrak{X} \times_{\hat{S}}
\mathfrak{Y}$, the projections $\mathfrak{z} \to \mathfrak{X}$ and $\mathfrak{z} \to \mathfrak{Y}$ being identified with
the extensions $\hat{p}$ and $\hat{q}$ `(I, 10.9.7)`. Since $Y$ is separated over $S$, $\mathfrak{Y}$ is separated over
`Ŝ` `(I, 10.15.7)`, hence the graph morphism $\Gamma_{h} = (1_{\mathfrak{X}}, h) : \mathfrak{X} \to \mathfrak{z}$ is a
closed immersion `(I, 10.15.4)`. Let $\mathfrak{T}$ be the closed formal subprescheme of $\mathfrak{z}$ associated to
this immersion, and $j : \mathfrak{T} \to \mathfrak{z}$ the canonical injection, so that $\Gamma_{h} = j \circ w$, where
$w : \mathfrak{X} \to \mathfrak{T}$ is an isomorphism `(I, 10.14.3)` whose inverse isomorphism is $\hat{p} \circ j$; in
addition, $\mathfrak{T}$ is obviously proper over `Ŝ`, since $\mathfrak{X}$ is; one concludes (5.1.8) that there exists
a closed subprescheme $T$ of $Z$ such that $\mathfrak{T} = \hat{T} = T_{/(T \cap Z')}$, and that $j = \hat{i}$, where
$i$ is the canonical injection $T \to Z$ `(I, 10.14.7)`. Then $p \circ i : T \to X$ is an isomorphism, since it is so
for $\hat{p \circ i} = \hat{p} \circ \hat{i}$ by hypothesis, and it suffices to apply

<!-- original page 157 -->

(4.6.8), noting as above that $S$ is the only neighbourhood of $S'$ in $S$. Let $g : X \to T$ be the inverse isomorphism
of $p \circ i$, and set $f = q \circ i \circ g$, which is a morphism $X \to Y$ whose graph is by definition $\Gamma_{f}
= i \circ g$. Since `ĝ` is the inverse isomorphism of $\hat{p \circ i} = w$, one has $\hat{\Gamma_{f}} = \hat{i} \circ
\hat{g} = j \circ w = \Gamma_{h}$. But one knows that $\hat{\Gamma_{f}} = \Gamma_{\hat{f}}$ `(I, 10.9.8)`, whence
finally $h = \hat{f}$, which completes the proof.

One may therefore say, in the language of categories, that the functor $X \mapsto \mathfrak{X}$ is *fully faithful*
`(0, 8.1.6)` from the category of proper schemes over $\operatorname{Spec}(A)$ into the category of proper formal
schemes over $Spf(A)$, for every adic Noetherian ring $A$; it consequently establishes an *equivalence* between the
first of these categories and a subcategory of the second; the objects of the latter will be called *algebraizable
formal schemes*. For such a scheme $\mathfrak{X}$, there exists a usual scheme $X$, proper over
$\operatorname{Spec}(A)$, determined up to unique isomorphism, such that $\mathfrak{X}$ is isomorphic to $\hat{X}$.

**Scholium (5.4.2).**

<!-- label: III.5.4.2 -->

With the notation of (5.4.1), set $S_{n} = \operatorname{Spec}(A/\mathfrak{J}^{n+1})$, $X_{n} = X \times_{S} S_{n}$,
$Y_{n} = Y \times_{S} S_{n}$. It follows from (5.4.1) and from `(I, 10.12.3)` that to give an $S$-morphism $f : X \to Y$
is equivalent to giving an $(S_{n})$-adic inductive system `(I, 10.12.2)` of $S_{n}$-morphisms $f_{n} : X_{n} \to
Y_{n}$.

**Remark (5.4.3).**

<!-- label: III.5.4.3 -->

Contrary to what the existence theorem (5.1.6) might suggest, there exist formal schemes proper over $Spf(A)$ that are
*not* algebraizable (just as there exist compact analytic spaces that do not come from complex algebraic varieties). We
shall later encounter such schemes in "moduli theory", which deals precisely (when the base field is $\mathbb{C}$) with
the infinitesimal variations of the complex structure of a complete algebraic variety, and it is known that such
variations may give rise to analytic varieties that are not algebraic.

**Proposition (5.4.4).**

<!-- label: III.5.4.4 -->

*Let $A$ be an adic Noetherian ring, $\mathfrak{S} = Spf(A)$, $g : \mathfrak{X} \to \mathfrak{S}$, $h : \mathfrak{Y} \to
\mathfrak{S}$ two proper morphisms of formal schemes, $f : \mathfrak{X} \to \mathfrak{Y}$ an $\mathfrak{S}$-morphism. If
$f$ is finite and if $\mathfrak{Y}$ is algebraizable, then $\mathfrak{X}$ is algebraizable.*

**Proof.** Note that the hypotheses on $g$ and $h$ already entail that $f$ is proper (3.4.1), and for $f$ to be finite,
it suffices that for every $y \in \mathfrak{Y}$, the fibre $f^{-1}(y)$ is finite (4.8.11). The hypothesis entails that
$\mathcal{B} = f_{*}(\mathcal{O}_{\mathfrak{X}})$ is a coherent $\mathcal{O}_{\mathfrak{Y}}$-Algebra (4.8.6), hence it
follows from the existence theorem that, if $\mathfrak{Y} = \hat{Y}$ and $h = \hat{w}$, where $w : Y \to
\operatorname{Spec}(A)$ is a proper morphism of usual schemes, there exists a coherent $\mathcal{O}_{Y}$-Algebra
$\mathcal{C}$ such that $\mathcal{B} = \hat{\mathcal{C}}$. Let $X = \operatorname{Spec}(\mathcal{C})$, and $u : X \to Y$
the structure morphism; it then follows at once from the definition of $\mathfrak{X}$ from $\mathcal{B}$ (4.8.7) that
$\mathfrak{X}$ is canonically isomorphic to $\hat{X}$ and that $f$ is identified with `û` (it suffices to see this for
the case where $Y$ is affine).

Note that (5.1.8) is a particular case of (5.4.4).

**Theorem (5.4.5).**

<!-- label: III.5.4.5 -->

*Let $A$ be an adic Noetherian ring, $\mathfrak{J}$ an ideal of definition of $A$, $S = \operatorname{Spec}(A)$,
$\mathfrak{S} = \hat{S} = Spf(A)$, $f : \mathfrak{X} \to \mathfrak{S}$ a proper morphism of formal schemes. Set $S_{k} =
\operatorname{Spec}(A/\mathfrak{J}^{k+1})$, $X_{k} = \mathfrak{X} \times_{\mathfrak{S}} S_{k}$, and for every
$\mathcal{O}_{\mathfrak{X}}$-module $\mathcal{F}$, $\mathcal{F}_{k} = \mathcal{F} \otimes_{\mathcal{O}_{\mathfrak{X}}}
\mathcal{O}_{X_{k}} = \mathcal{F} / \mathfrak{J}^{k+1} \mathcal{F}$.*

<!-- original page 158 -->

*Let $\mathcal{L}$ be an invertible $\mathcal{O}_{\mathfrak{X}}$-module, and suppose that $\mathcal{L}_{0} = \mathcal{L}
/ \mathfrak{J}\mathcal{L}$ is an ample $\mathcal{O}_{X_{0}}$-module. Then $\mathfrak{X}$ is algebraizable, and if $X$ is
a proper $S$-scheme such that $\mathfrak{X}$ is isomorphic to $\hat{X}$, there exists an ample $\mathcal{O}_{X}$-module
$\mathcal{M}$ such that $\mathcal{L}$ is isomorphic to $\hat{\mathcal{M}}$ (which implies that $X$ is projective over
$S$).*

**Proof.** Let us apply (5.2.3) to $\mathcal{F} = \mathcal{O}_{\mathfrak{X}}$: there thus exists an integer $n_{0}$ such
that for $n \geq n_{0}$, the canonical homomorphism $\Gamma(\mathfrak{X}, \mathcal{L}^{\otimes n}) \to \Gamma(X_{0},
\mathcal{L}^{\otimes n}_{0})$ is surjective. One may suppose $n \geq n_{0}$ chosen large enough that
$\mathcal{L}^{\otimes n}_{0}$ is *very ample* for `S_0` `(II, 4.5.10)`. Since the morphism $f_{0} : X_{0} \to S_{0}$ is
proper, $\Gamma(X_{0}, \mathcal{L}^{\otimes n}_{0})$ is an $A$-module of finite type (3.2.1), hence there exists a
sub-$A$-module of finite type $E$ of $\Gamma(\mathfrak{X}, \mathcal{L}^{\otimes n})$ whose image in $\Gamma(X_{0},
\mathcal{L}^{\otimes n}_{0})$ is this latter module in its entirety. This being so, for every $k \geq 0$, consider the
homomorphism $u_{k} : E / \mathfrak{J}^{k+1} E \to \Gamma(X_{k}, \mathcal{L}^{\otimes n}_{k})$ deduced from the
canonical injection $E \to \Gamma(\mathfrak{X}, \mathcal{L}^{\otimes n})$. Note that $(f_{k})_{*}(\mathcal{L}^{\otimes
n}_{k})$ is quasi-coherent, and since $\Gamma(S_{k}, (f_{k})_{*}(\mathcal{L}^{\otimes n}_{k})) = \Gamma(X_{k},
\mathcal{L}^{\otimes n}_{k})$, $u_{k}$ defines a homomorphism $\tilde{u}_{k} : (E / \mathfrak{J}^{k+1} E)^{\sim} \to
(f_{k})_{*}(\mathcal{L}^{\otimes n}_{k})$, and consequently also a homomorphism $\tilde{u}^{\sharp}_{k} : f^{*}_{k}((E /
\mathfrak{J}^{k+1} E)^{\sim}) \to \mathcal{L}^{\otimes n}_{k}$. Moreover, if one sets $\mathcal{G}_{k} = f^{*}_{k}((E /
\mathfrak{J}^{k+1} E)^{\sim})$, one has $\mathcal{G}_{k} = \mathcal{G}_{0} / \mathfrak{J}^{k} \mathcal{G}_{0}$
`(I, 9.1.5)`, hence $\tilde{u}^{\sharp}_{k} : \mathcal{G}_{k} / \mathfrak{J}^{k} \mathcal{G}_{k} \to
\mathcal{L}^{\otimes n}_{k} / \mathfrak{J}^{k} \mathcal{L}^{\otimes n}_{k}$ is deduced from $\tilde{u}^{\sharp}_{0}$ by
passage to quotients. Now, by definition of $E$, $\tilde{u}^{\sharp}_{0}$ is none other than the canonical homomorphism
$\sigma : f^{*}_{0}((f_{0})_{*}(\mathcal{L}^{\otimes n}_{0})) \to \mathcal{L}^{\otimes n}_{0}$, and the hypothesis that
$\mathcal{L}^{\otimes n}_{0}$ is very ample entails that $\tilde{u}^{\sharp}_{0}$ is *surjective* `(II, 4.4.3)`; one
then deduces from Nakayama's lemma that each of the $\tilde{u}^{\sharp}_{k}$ is also surjective. Each of the
$\tilde{u}^{\sharp}_{k}$ therefore defines `(II, 4.2.2)` an $S_{k}$-morphism $g_{k} : X_{k} \to P_{k} = \mathbf{P}(E /
\mathfrak{J}^{k+1} E)$, and since $P_{h} = P_{k} \times_{S_{k}} S_{h}$ for $h \leq k$ by virtue of `(II, 4.1.3)`,
$(g_{k})$ is an $(S_{k})$-adic inductive system `(I, 10.12.2)` by virtue of the relations between the
$\tilde{u}^{\sharp}_{k}$ and of `(II, 4.2.10)`. The $g_{k}$ therefore define an $\mathfrak{S}$-morphism of formal
schemes $g : \mathfrak{X} \to \mathfrak{P}$, where $\mathfrak{P}$ is the inductive limit of the system $(P_{k})$, or
equivalently the completion $\hat{P}$, where $P = \mathbf{P}(E)$. In addition, the hypothesis that $\mathcal{L}^{\otimes
n}_{0}$ is very ample entails that $g_{0}$ is a closed immersion `(II, 4.4.3)`; one concludes that $g$ is a closed
immersion of formal schemes (4.8.10), hence $\mathfrak{X}$ is algebraizable (5.1.8). The fact that $\mathcal{L}$ is
isomorphic to the completion $\hat{\mathcal{M}}$ of an invertible $\mathcal{O}_{X}$-module then follows from the
existence theorem (5.1.6). In addition, $\mathcal{L}^{\otimes n}$ is then the completion of $\mathcal{M}^{\otimes n}$
`(I, 10.8.10)`, and the homomorphisms $\tilde{u}^{\sharp}_{k}$ define a well-determined homomorphism $\hat{v} :
f^{*}(\tilde{E}) \to \hat{\mathcal{M}}^{\otimes n}$ (5.1.7); moreover, since $\hat{v}$ is surjective, so is $v$
`(I, 10.11.5)`, hence so is $u$ (5.1.3); in addition, the morphism $r : X \to P$ defined by $v$ `(II, 4.2.2)` has as
extension to the completions $g$, and since $g$ is a closed immersion, so is $r$, by (5.1.8) and (5.4.1); one concludes
that $\mathcal{M}^{\otimes n}$ is very ample `(II, 4.4.6)` and $\mathcal{M}$ is ample `(II, 4.5.10)`.

**Remark (5.4.6).**

<!-- label: III.5.4.6 -->

Let $A$ be an adic Noetherian ring, $\mathfrak{S} = Spf(A)$, $f : \mathfrak{X} \to \mathfrak{S}$ a proper morphism of
formal schemes. Let $\mathcal{N}$ be the coherent Ideal of $\mathcal{O}_{\mathfrak{X}}$ such that for every formal
affine open $U$ of $\mathfrak{X}$, $\Gamma(U, \mathcal{N})$ is the nilradical of $\Gamma(U,
\mathcal{O}_{\mathfrak{X}})$; the existence of this Ideal follows easily from `(I, 10.10.2)` and from the fact that
every ring homomorphism $B \to C$ sends the nilradical of $B$ into that of $C$. Let $\mathfrak{X}'$ be the closed formal
subscheme of $\mathfrak{X}$ defined by $\mathcal{N}$ `(I, 10.14.2)`; it would be interesting to know whether, when
$\mathfrak{X}'$ is algebraizable, $\mathfrak{X}$ itself is algebraizable. One would no doubt arrive at a solution to
this problem if one knew how to classify (for example by means of invariants of

<!-- original page 159 -->

cohomological nature) the *extensions* of a structure sheaf $\mathcal{O}_{\mathfrak{X}}$ (for a usual prescheme or a
formal prescheme) by an Ideal of square zero, in other words the $\mathcal{O}_{\mathfrak{X}}$-Algebras $\mathcal{A}$
such that $\mathcal{O}_{\mathfrak{X}}$ is isomorphic to $\mathcal{A} / \mathcal{J}$, where $\mathcal{J}$ is an Ideal of
square zero of $\mathcal{A}$.

## 5.5. A decomposition of certain schemes

**Proposition (5.5.1).**

<!-- label: III.5.5.1 -->

*Let $A$ be an adic Noetherian ring, $\mathfrak{J}$ an ideal of definition of $A$, $Y = \operatorname{Spec}(A)$. Let
$f : X \to Y$ be a separated morphism of finite type; set $Y_{0} = \operatorname{Spec}(A/\mathfrak{J})$,
$X_{0} = X \times_{Y} Y_{0} = f^{-1}(Y_{0})$. Let `Z_0` be an open part of `X_0`, proper over `Y_0`; then there exists
in $X$ an open and closed part $Z$, proper over $Y$ and such that $Z \cap X_{0} = Z_{0}$.*

**Proof.** By hypothesis, there is an open subset $T$ of $X$ such that $T \cap X_{0} = Z_{0}$; let $\mathfrak{T}$ be the
completion along `Z_0` of the scheme induced by $X$ on the open subset $T$; the support of $\mathcal{O}_{\mathfrak{T}}$
being `Z_0`, which is proper over `Y_0`, $\mathfrak{T}$ is proper over $\hat{Y} = Spf(A)$ (3.4.1). It follows from
(5.1.8) that there exists a closed subscheme $Z$ of $T$ proper over $Y$ such that, if $i : Z \to T$ is the canonical
injection, $\hat{i} : \hat{\mathcal{Z}} \to \mathfrak{T}$ is an isomorphism ($\hat{\mathcal{Z}}$ being the completion of
$Z$ along `Z_0`). One concludes (4.6.8) that there exists in $T$ an open neighbourhood $V$ of `Z_0` such that the
restriction $i^{-1}(V) \to V$ of $i$ is an isomorphism. But $i^{-1}(V)$ is a neighbourhood of `Z_0` in $Z$, hence is
necessarily identical to $Z$ (5.1.3.1). One concludes that $Z$ is open in $T$, hence in $X$, which completes the proof.

**Corollary (5.5.2).**

<!-- label: III.5.5.2 -->

*If `X_0` is proper over `Y_0`, $X$ is the union of two disjoint open parts $Z$ and $Z'$ such that $Z$ is proper over
$Y$ and contains `X_0`; in addition, every closed part $P$ of $X$, proper over $Y$, is contained in $Z$.*

**Proof.** The last assertion follows from the fact that $P \cap Z'$, being closed in $P$, is proper over $Y$; if $P
\cap Z'$ were not empty, $f(P \cap Z')$ would be closed non-empty in $Y$, hence would meet `Y_0` (5.1.3.1), which
contradicts the definition of $Z$.

*(To be continued.)*

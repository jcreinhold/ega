# §1. Affine morphisms

Most of the results in this section are the "global" counterparts of those in Chapter I, §1; they are therefore not
essentially new and merely provide a convenient language for the sequel.

## 1.1. $S$-preschemes and $\mathcal{O}_{S}$-algebras

**(1.1.1)**

<!-- label: II.1.1.1 -->

Let $S$ be a prescheme, $X$ an $S$-prescheme, and $f : X \to S$ its structure morphism. We know `(0, 4.2.4)` that the
direct image $f_{*}(\mathcal{O}_{X})$ is an $\mathcal{O}_{S}$-algebra, which we

<!-- original page 6 -->

denote by $\mathcal{A}(X)$ when no confusion is likely. If $U$ is an open subset of $S$, then

$$ \mathcal{A}(f^{-1}(U)) = \mathcal{A}(X)|U. $$

Likewise, for every $\mathcal{O}_{X}$-module $\mathcal{F}$ (resp. every $\mathcal{O}_{X}$-algebra $\mathcal{B}$), we
write $\mathcal{A}(\mathcal{F})$ (resp. $\mathcal{A}(\mathcal{B})$) for the direct image $f_{*}(\mathcal{F})$ (resp.
$f_{*}(\mathcal{B})$), which is an $\mathcal{A}(X)$-module (resp. $\mathcal{A}(X)$-algebra), and not just an
$\mathcal{O}_{S}$-module (resp. $\mathcal{O}_{S}$-algebra).

**(1.1.2)**

<!-- label: II.1.1.2 -->

Let $Y$ be a second $S$-prescheme, $g : Y \to S$ its structure morphism, and $h : X \to Y$ an $S$-morphism, giving the
commutative diagram

```text
        h
   X ─────→ Y                                                            (1.1.2.1)
    \      /
   f \    / g
      ↘  ↙
       S
```

By definition $h = (\psi, \theta)$, where $\theta : \mathcal{O}_{Y} \to h_{*}(\mathcal{O}_{X}) =
\psi_{*}(\mathcal{O}_{X})$ is a homomorphism of sheaves of rings; we therefore obtain `(0, 4.2.2)` a homomorphism of
$\mathcal{O}_{S}$-algebras $g_{*}(\theta) : g_{*}(\mathcal{O}_{Y}) \to g_{*}(h_{*}(\mathcal{O}_{X})) =
f_{*}(\mathcal{O}_{X})$, in other words a homomorphism of $\mathcal{O}_{S}$-algebras $\mathcal{A}(Y) \to
\mathcal{A}(X)$, which we also denote by $\mathcal{A}(h)$. If $h' : Y \to Z$ is a second $S$-morphism, it is immediate
that $\mathcal{A}(h' \circ h) = \mathcal{A}(h) \circ \mathcal{A}(h')$. We have thus defined a _contravariant functor_
$\mathcal{A}(X)$ on the category of $S$-preschemes, with values in the category of $\mathcal{O}_{S}$-algebras.

Now let $\mathcal{F}$ be an $\mathcal{O}_{X}$-module, $\mathcal{G}$ an $\mathcal{O}_{Y}$-module, and $u : \mathcal{G}
\to \mathcal{F}$ an $h$-morphism — that is `(0, 4.4.1)`, a homomorphism of $\mathcal{O}_{Y}$-modules $\mathcal{G} \to
h_{*}(\mathcal{F})$. Then $g_{*}(u) : g_{*}(\mathcal{G}) \to g_{*}(h_{*}(\mathcal{F})) = f_{*}(\mathcal{F})$ is a
homomorphism $\mathcal{A}(\mathcal{G}) \to \mathcal{A}(\mathcal{F})$ of $\mathcal{O}_{S}$-modules, which we denote by
$\mathcal{A}(u)$; furthermore, the pair $(\mathcal{A}(h), \mathcal{A}(u))$ is a _di-homomorphism_ from the
$\mathcal{A}(Y)$-module $\mathcal{A}(\mathcal{G})$ to the $\mathcal{A}(X)$-module $\mathcal{A}(\mathcal{F})$.

**(1.1.3)**

<!-- label: II.1.1.3 -->

If we fix the prescheme $S$, the pairs $(X, \mathcal{F})$ with $X$ an $S$-prescheme and $\mathcal{F}$ an
$\mathcal{O}_{X}$-module form a _category_: a _morphism_ $(X, \mathcal{F}) \to (Y, \mathcal{G})$ is by definition a pair
$(h, u)$ with $h : X \to Y$ an $S$-morphism and $u : \mathcal{G} \to \mathcal{F}$ an $h$-morphism. We may then say that
$(\mathcal{A}(X), \mathcal{A}(\mathcal{F}))$ is a _contravariant functor_ with values in the category whose objects are
pairs consisting of an $\mathcal{O}_{S}$-algebra and a module over that algebra, and whose morphisms are
di-homomorphisms.

## 1.2. Affine preschemes over a prescheme

**Definition.**

<!-- label: II.1.2.1 -->

Let $X$ be an $S$-prescheme and $f : X \to S$ its structure morphism. We say that $X$ is _affine over_ $S$ if there
exists a covering $(S_{\alpha})$ of $S$ by affine opens such that for every $\alpha$, the prescheme induced by $X$ on
$f^{-1}(S_{\alpha})$ is affine.

**Example.**

<!-- label: II.1.2.2 -->

Every closed subprescheme of $S$ is an $S$-prescheme affine over $S$ (`I, 4.2.3` and `4.2.4`).

**Remark.**

<!-- label: II.1.2.3 -->

A prescheme $X$ affine over $S$ need not itself be an affine scheme, as the example $X = S$ from (1.2.2) shows. On the
other hand, if an affine scheme $X$ is an $S$-prescheme, $X$ is not necessarily affine over $S$ (see (1.3.3) below).
Recall

<!-- original page 7 -->

however that if $S$ is a _scheme_, then every $S$-prescheme that is an affine scheme is affine over $S$ (`I, 5.5.10`).

**Proposition.**

<!-- label: II.1.2.4 -->

Every $S$-prescheme affine over $S$ is separated over $S$ (in other words, it is an $S$-scheme).

**Proof.** This follows immediately from `(I, 5.5.5)` and `(I, 5.5.8)`.

**Proposition.**

<!-- label: II.1.2.5 -->

Let $X$ be an $S$-scheme affine over $S$ and $f : X \to S$ its structure morphism. For every open $U \subset S$,
$f^{-1}(U)$ is affine over $U$.

**Proof.** By Definition (1.2.1), we reduce to the case where $S = \operatorname{Spec}(A)$ and $X =
\operatorname{Spec}(B)$ are affine, with $f = ({}^{a}\phi, \tilde{\phi})$ and $\phi : A \to B$ a homomorphism. Since the
$D(g)$ for $g \in A$ form a basis of $S$, we reduce to $U = D(g)$; but $f^{-1}(U) = D(\phi(g))$ `(I, 1.2.2.2)`, which
gives the proposition.

**Proposition.**

<!-- label: II.1.2.6 -->

Let $X$ be an $S$-scheme affine over $S$ and $f : X \to S$ its structure morphism. For every quasi-coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$, $f_{*}(\mathcal{F})$ is a quasi-coherent $\mathcal{O}_{S}$-module.

**Proof.** Given (1.2.4), this follows from `(I, 9.2.2 a)`.

In particular, the $\mathcal{O}_{S}$-algebra $\mathcal{A}(X) = f_{*}(\mathcal{O}_{X})$ is _quasi-coherent_.

**Proposition.**

<!-- label: II.1.2.7 -->

Let $X$ be an $S$-scheme affine over $S$. For every $S$-prescheme $Y$, the map $h \mapsto \mathcal{A}(h)$ from
$\operatorname{Hom}_{S}(Y, X)$ to $\operatorname{Hom}(\mathcal{A}(X), \mathcal{A}(Y))$ (1.1.2) is bijective.

**Proof.** Let $f : X \to S$ and $g : Y \to S$ be the structure morphisms.

First, suppose $S = \operatorname{Spec}(A)$ and $X = \operatorname{Spec}(B)$ are affine. We must show that every
homomorphism $\omega : f_{*}(\mathcal{O}_{X}) \to g_{*}(\mathcal{O}_{Y})$ of $\mathcal{O}_{S}$-algebras arises from a
unique $S$-morphism $h : Y \to X$ via $\mathcal{A}(h) = \omega$. By definition, for every open $U \subset S$, $\omega$
defines a homomorphism

```text
  ω_U = Γ(U, ω) : Γ(f⁻¹(U), 𝒪_X) → Γ(g⁻¹(U), 𝒪_Y)
```

of $\Gamma(U, \mathcal{O}_{S})$-algebras. In particular, taking $U = S$, we obtain a homomorphism $\phi : \Gamma(X,
\mathcal{O}_{X}) \to \Gamma(Y, \mathcal{O}_{Y})$ of $\Gamma(S, \mathcal{O}_{S})$-algebras, to which corresponds a
well-defined $S$-morphism $h : Y \to X$ since $X$ is affine `(I, 2.2.4)`. It remains to prove $\mathcal{A}(h) = \omega$,
that is: for every open $U$ in a basis of $S$, $\omega_{U}$ coincides with the algebra homomorphism $\phi_{U}$
corresponding to the restriction $g^{-1}(U) \to f^{-1}(U)$ of $h$. We may take $U = D(\lambda)$ with $\lambda \in S$;
then if $f = ({}^{a}\rho, \tilde{\rho})$ with $\rho : A \to B$ a ring homomorphism, $f^{-1}(U) = D(\mu)$ for $\mu =
\rho(\lambda)$, and $\Gamma(f^{-1}(U), \mathcal{O}_{X})$ is the ring of fractions $B_{\mu}$. The diagram

```text
   B ──────φ─────→ Γ(Y, 𝒪_Y)
   │                  │
   ↓                  ↓
   B_μ ────φ_U───→ Γ(g⁻¹(U), 𝒪_Y)
```

commutes, and so does the analogous diagram with $\phi_{U}$ replaced by $\omega_{U}$; the equality $\phi_{U} =
\omega_{U}$ then follows from the universal property of rings of fractions `(0, 1.2.4)`.

For the general case, let $(S_{\alpha})$ be a covering of $S$ by affine opens

<!-- original page 8 -->

such that the $f^{-1}(S_{\alpha})$ are affine. Every homomorphism $\omega : \mathcal{A}(X) \to \mathcal{A}(Y)$ of
$\mathcal{O}_{S}$-algebras restricts to a family of homomorphisms

$$ \omega_{\alpha} : \mathcal{A}(f^{-1}(S_{\alpha})) \to \mathcal{A}(g^{-1}(S_{\alpha})) $$

of $\mathcal{O}_{S_{\alpha}}$-algebras, hence to a family of $S_{\alpha}$-morphisms $h_{\alpha} : g^{-1}(S_{\alpha}) \to
f^{-1}(S_{\alpha})$ by the affine case above. We need only check that on every affine open $U$ in a basis of $S_{\alpha}
\cap S_{\beta}$, the restrictions of $h_{\alpha}$ and $h_{\beta}$ to $g^{-1}(U)$ agree, which is evident since both
correspond to the restriction $\mathcal{A}(X)|U \to \mathcal{A}(Y)|U$ of $\omega$.

**Corollary.**

<!-- label: II.1.2.8 -->

Let $X$, $Y$ be two $S$-schemes affine over $S$. An $S$-morphism $h : Y \to X$ is an isomorphism if and only if
$\mathcal{A}(h) : \mathcal{A}(X) \to \mathcal{A}(Y)$ is one.

**Proof.** Immediate from (1.2.7) and the functoriality of $\mathcal{A}(X)$.

## 1.3. Affine prescheme over $S$ associated to an $\mathcal{O}_{S}$-algebra

**Proposition.**

<!-- label: II.1.3.1 -->

Let $S$ be a prescheme. For every quasi-coherent $\mathcal{O}_{S}$-algebra $\mathcal{B}$, there exists a prescheme $X$
affine over $S$, defined up to unique $S$-isomorphism, such that $\mathcal{A}(X) = \mathcal{B}$.

**Proof.** Uniqueness follows from (1.2.8); we prove existence. For every affine open $U \subset S$, set $X_{U} =
\operatorname{Spec}(\Gamma(U, \mathcal{B}))$; since $\Gamma(U, \mathcal{B})$ is a $\Gamma(U, \mathcal{O}_{S})$-algebra,
`X_U` is an $S$-prescheme `(I, 1.6.1)`. As $\mathcal{B}$ is quasi-coherent, the $\mathcal{O}_{S}$-algebra
$\mathcal{A}(X_{U})$ is canonically identified with $\mathcal{B}|U$ (`I, 1.3.7`, `1.3.13`, `1.6.3`). For a second affine
open $V \subset S$, let $X_{U,V}$ be the prescheme induced by `X_U` on $f^{-1}_{U}(U \cap V)$, where $f_{U} : X_{U} \to
S$ is the structure morphism; then $X_{U,V}$ and $X_{V,U}$ are affine over $U \cap V$ (1.2.5), and by definition
$\mathcal{A}(X_{U,V})$ and $\mathcal{A}(X_{V,U})$ both identify canonically with $\mathcal{B}|(U \cap V)$. Hence (1.2.8)
there is a canonical $S$-isomorphism $\theta_{U,V} : X_{V,U} \to X_{U,V}$; furthermore, if $W$ is a third affine open of
$S$ and $\theta'_{U,V}$, $\theta'_{V,W}$, $\theta'_{U,W}$ are the restrictions to the inverse images of $U \cap V \cap
W$, then $\theta'_{U,V} \circ \theta'_{V,W} = \theta'_{U,W}$. Consequently there exists a prescheme $X$, a covering
`(T_U)` of $X$ by affine opens, and for each $U$ an isomorphism $\phi_{U} : X_{U} \to T_{U}$ such that $\phi_{U}$
carries $f^{-1}_{U}(U \cap V)$ onto $T_{U} \cap T_{V}$ with $\theta_{U,V} = \phi^{-1}_{U} \circ \phi_{V}$ `(I, 2.3.1)`.
The morphism $g_{U} = f_{U} \circ \phi^{-1}_{U}$ makes `T_U` an $S$-prescheme, and $g_{U}$, $g_{V}$ coincide on $T_{U}
\cap T_{V}$, so $X$ is an $S$-prescheme. It is then clear by construction that $X$ is affine over $S$ and that
$\mathcal{A}(T_{U}) = \mathcal{B}|U$, whence $\mathcal{A}(X) = \mathcal{B}$.

We say that the $S$-scheme $X$ so defined is _associated to the $\mathcal{O}_{S}$-algebra_ $\mathcal{B}$, or is the
_spectrum of $\mathcal{B}$_, and we denote it by $\operatorname{Spec}(\mathcal{B})$.

**Corollary.**

<!-- label: II.1.3.2 -->

Let $X$ be a prescheme affine over $S$ and $f : X \to S$ the structure morphism. For every affine open $U \subset S$,
the prescheme induced on $f^{-1}(U)$ is the affine scheme with ring $\Gamma(U, \mathcal{A}(X))$.

<!-- original page 9 -->

**Proof.** Since by (1.2.6) and (1.3.1) we may take $X$ to be associated to an $\mathcal{O}_{S}$-algebra, the corollary
follows from the construction of $X$ in (1.3.1).

**Example.**

<!-- label: II.1.3.3 -->

Let $S$ be the affine plane over a field $K$ with the origin doubled `(I, 5.5.11)`; with the notation of `(I, 5.5.11)`,
$S$ is the union of two affine opens `Y_1`, `Y_2`. If $f$ is the open immersion $Y_{1} \to S$, then $f^{-1}(Y_{2}) =
Y_{1} \cap Y_{2}$ is not an affine open in `Y_1` (_loc. cit._), giving an example of an affine scheme that is not affine
over $S$.

**Corollary.**

<!-- label: II.1.3.4 -->

Let $S$ be an affine scheme. An $S$-prescheme $X$ is affine over $S$ if and only if $X$ is an affine scheme.

**Corollary.**

<!-- label: II.1.3.5 -->

Let $X$ be a prescheme affine over a prescheme $S$, and let $Y$ be an $X$-prescheme. Then $Y$ is affine over $S$ if and
only if $Y$ is affine over $X$.

**Proof.** We reduce immediately to the case where $S$ is an affine scheme, and then, by (1.3.4), so is $X$; the two
conditions both say that $Y$ is an affine scheme (1.3.4).

**(1.3.6)**

<!-- label: II.1.3.6 -->

Let $X$ be a prescheme affine over $S$. To give a prescheme $Y$ affine _over_ $X$ is, by Corollary (1.3.5), the same as
to give a prescheme $Y$ affine _over_ $S$ together with an $S$-morphism $g : Y \to X$; in other words ((1.3.1) and
(1.2.7)), it is the same as to give a quasi-coherent $\mathcal{O}_{S}$-algebra $\mathcal{B}$ together with a
homomorphism $\mathcal{A}(X) \to \mathcal{B}$ of $\mathcal{O}_{S}$-algebras (which may be viewed as defining on
$\mathcal{B}$ an $\mathcal{A}(X)$-algebra structure). If $f : X \to S$ is the structure morphism, then $\mathcal{B} =
f_{*}(g_{*}(\mathcal{O}_{Y}))$.

**Corollary.**

<!-- label: II.1.3.7 -->

Let $X$ be a prescheme affine over $S$. Then $X$ is of finite type over $S$ if and only if the quasi-coherent
$\mathcal{O}_{S}$-algebra $\mathcal{A}(X)$ is of finite type `(I, 9.6.2)`.

**Proof.** By definition `(I, 9.6.2)` we reduce to the case where $S$ is affine; then $X$ is affine `(1.3.4)`, and if $S
= \operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$, then $\mathcal{A}(X)$ is the $\mathcal{O}_{S}$-algebra
$\tilde{B}$. Since $\Gamma(S, \tilde{B}) = B$, the corollary follows from `(I, 9.6.2)` and `(I, 6.3.3)`.

**Corollary.**

<!-- label: II.1.3.8 -->

Let $X$ be a prescheme affine over $S$. Then $X$ is reduced if and only if the quasi-coherent $\mathcal{O}_{S}$-algebra
$\mathcal{A}(X)$ is reduced `(0, 4.1.4)`.

**Proof.** The question is local on $S$; by Corollary (1.3.2), the assertion follows from `(I, 5.1.1)` and `(I, 5.1.4)`.

## 1.4. Quasi-coherent sheaves on an affine prescheme over $S$

**Proposition.**

<!-- label: II.1.4.1 -->

Let $X$ be a prescheme affine over $S$, $Y$ an $S$-prescheme, and $\mathcal{F}$ (resp. $\mathcal{G}$) a quasi-coherent
$\mathcal{O}_{X}$-module (resp. $\mathcal{O}_{Y}$-module). Then the map $(h, u) \mapsto (\mathcal{A}(h),
\mathcal{A}(u))$ from the set of morphisms $(Y, \mathcal{G}) \to (X, \mathcal{F})$ to the set of di-homomorphisms
$(\mathcal{A}(X), \mathcal{A}(\mathcal{F})) \to (\mathcal{A}(Y), \mathcal{A}(\mathcal{G}))$ ((1.1.2) and (1.1.3)) is
bijective.

**Proof.** The proof follows exactly the same lines as that of (1.2.7), using `(I, 2.2.5)` and `(I, 2.2.4)`; details are
left to the reader.

**Corollary.**

<!-- label: II.1.4.2 -->

If, in addition to the hypotheses of (1.4.1), $Y$ is also affine over $S$, then $(h, u)$ is an isomorphism if and only
if $(\mathcal{A}(h), \mathcal{A}(u))$ is a di-isomorphism.

**Proposition.**

<!-- label: II.1.4.3 -->

<!-- original page 10 -->

For every pair $(\mathcal{B}, \mathcal{M})$ consisting of a quasi-coherent $\mathcal{O}_{S}$-algebra $\mathcal{B}$ and a
quasi-coherent $\mathcal{B}$-module $\mathcal{M}$ (viewed as an $\mathcal{O}_{S}$-module or as a $\mathcal{B}$-module —
these are equivalent `(I, 9.6.1)`), there exists a pair $(X, \mathcal{F})$ consisting of a prescheme $X$ affine over $S$
and a quasi-coherent $\mathcal{O}_{X}$-module $\mathcal{F}$ such that $\mathcal{A}(X) = \mathcal{B}$ and
$\mathcal{A}(\mathcal{F}) = \mathcal{M}$; this pair is determined up to unique isomorphism.

**Proof.** Uniqueness follows from (1.4.1) and (1.4.2); existence is proved as in (1.3.1), and we again leave details to
the reader.

We denote by $\tilde{\mathcal{M}}$ the $\mathcal{O}_{X}$-module $\mathcal{F}$ so obtained, and call it _associated_ to
the quasi-coherent $\mathcal{B}$-module $\mathcal{M}$. For every affine open $U \subset S$, $\mathcal{F}|p^{-1}(U)$
(where $p$ is the structure morphism $X \to S$) is canonically isomorphic to $\tilde{\Gamma(U, \mathcal{M})}$.

**Corollary.**

<!-- label: II.1.4.4 -->

On the category of quasi-coherent $\mathcal{B}$-modules, $\tilde{\mathcal{M}}$ is a covariant additive exact functor in
$\mathcal{M}$ that commutes with direct limits and direct sums.

**Proof.** We reduce immediately to the case where $S$ is affine; the corollary then follows from `(I, 1.3.5)`,
`(I, 1.3.9)`, and `(I, 1.3.11)`.

**Corollary.**

<!-- label: II.1.4.5 -->

Under the hypotheses of (1.4.3), $\tilde{\mathcal{M}}$ is an $\mathcal{O}_{X}$-module of finite type if and only if
$\mathcal{M}$ is a $\mathcal{B}$-module of finite type.

**Proof.** We reduce to $S = \operatorname{Spec}(A)$ affine. Then $\mathcal{B} = \tilde{B}$, where $B$ is an $A$-algebra
of finite type `(I, 9.6.2)`, and $\mathcal{M} = \tilde{M}$, where $M$ is a $B$-module `(I, 1.3.13)`. On the prescheme
$X$, $\mathcal{O}_{X}$ is associated to $B$ and $\tilde{\mathcal{M}}$ to the $B$-module $M$; so $\tilde{\mathcal{M}}$ is
of finite type iff $M$ is of finite type `(I, 1.3.13)`, whence the claim.

**Proposition.**

<!-- label: II.1.4.6 -->

Let $Y$ be a prescheme affine over $S$, and let $X$, $X'$ be two preschemes affine over $Y$ (hence also over $S$ by
(1.3.5)). Set $\mathcal{B} = \mathcal{A}(Y)$, $\mathcal{A} = \mathcal{A}(X)$, $\mathcal{A}' = \mathcal{A}(X')$. Then $X
\times_{Y} X'$ is affine over $Y$ (and hence also over $S$), and $\mathcal{A}(X \times_{Y} X')$ is canonically
identified with $\mathcal{A} \otimes_{\mathcal{B}} \mathcal{A}'$.

**Proof.** By `(I, 9.6.1)`, $\mathcal{A} \otimes_{\mathcal{B}} \mathcal{A}'$ is a quasi-coherent $\mathcal{B}$-algebra,
and thus also a quasi-coherent $\mathcal{O}_{S}$-algebra `(I, 9.6.1)`. Let $Z$ be the spectrum of $\mathcal{A}
\otimes_{\mathcal{B}} \mathcal{A}'$ (1.3.1). The canonical $\mathcal{B}$-homomorphisms $\mathcal{A} \to \mathcal{A}
\otimes_{\mathcal{B}} \mathcal{A}'$ and $\mathcal{A}' \to \mathcal{A} \otimes_{\mathcal{B}} \mathcal{A}'$ correspond by
(1.2.7) to $Y$-morphisms $p : Z \to X$ and $p' : Z \to X'$. To see that `(Z, p, p')` is a product $X \times_{Y} X'$, we
may reduce to the case where $S$ is an affine scheme with ring $C$ `(I, 3.2.6.4)`. Then $Y$, $X$, $X'$ are affine
schemes (1.3.4) with rings $B$, $A$, $A'$ which are $C$-algebras such that $\mathcal{B} = \tilde{B}$, $\mathcal{A} =
\tilde{A}$, $\mathcal{A}' = \tilde{A}'$. Then `(I, 1.3.13)` gives $\mathcal{A} \otimes_{\mathcal{B}} \mathcal{A}' =
\tilde{A \otimes_{B} A'}$, so the ring of $Z$ is $A \otimes_{B} A'$ and the morphisms $p$, $p'$ correspond to the
canonical homomorphisms $A \to A \otimes_{B} A'$ and $A' \to A \otimes_{B} A'$. The proposition follows from
`(I, 3.2.2)`.

**Corollary.**

<!-- label: II.1.4.7 -->

Let $\mathcal{F}$ (resp. $\mathcal{F}'$) be a quasi-coherent $\mathcal{O}_{X}$-module (resp. $\mathcal{O}_{X'}$-module).
Then $\mathcal{A}(\mathcal{F} \otimes_{Y} \mathcal{F}')$ is canonically identified with $\mathcal{A}(\mathcal{F})
\otimes_{\mathcal{A}(Y)} \mathcal{A}(\mathcal{F}')$.

**Proof.** We know `(I, 9.1.2)` that $\mathcal{F} \otimes_{Y} \mathcal{F}'$ is quasi-coherent on $X \times_{Y} X'$. Let
$g : Y \to S$, $f : X \to Y$, $f' : X' \to Y$ be the structure morphisms, so that the structure morphism

<!-- original page 11 -->

$h : Z \to S$ equals $g \circ f \circ p = g \circ f' \circ p'$. We define a canonical homomorphism

```text
  𝒜(ℱ) ⊗_{𝒜(Y)} 𝒜(ℱ') → 𝒜(ℱ ⊗_Y ℱ')
```

as follows: for every open $U \subset S$, the canonical homomorphisms $\Gamma(f^{-1}(g^{-1}(U)), \mathcal{F}) \to
\Gamma(h^{-1}(U), p*(\mathcal{F}))$ and $\Gamma(f'^{-1}(g^{-1}(U)), \mathcal{F}') \to \Gamma(h^{-1}(U),
p'*(\mathcal{F}'))$ `(0, 4.4.3)` give a canonical homomorphism

```text
  Γ(f⁻¹(g⁻¹(U)), ℱ) ⊗_{Γ(g⁻¹(U), 𝒪_Y)} Γ(f'⁻¹(g⁻¹(U)), ℱ')
    → Γ(h⁻¹(U), p*(ℱ)) ⊗_{Γ(h⁻¹(U), 𝒪_Z)} Γ(h⁻¹(U), p'*(ℱ')).
```

To see this is an isomorphism of $\mathcal{A}(Z)$-modules, we reduce to the affine case: $S$ (and hence $X$, $X'$, $Y$,
$X \times_{Y} X'$) affine, and (with the notation of (1.4.6)) $\mathcal{F} = \tilde{M}$, $\mathcal{F}' = \tilde{M}'$
with $M$ an $A$-module and $M'$ an $A'$-module. Then $\mathcal{F} \otimes_{Y} \mathcal{F}'$ identifies with the sheaf on
$X \times_{Y} X'$ associated to the $(A \otimes_{B} A')$-module $M \otimes_{B} M'$ `(I, 9.1.3)`, and the corollary
follows from the canonical identification of $\mathcal{O}_{S}$-modules $\tilde{M \otimes_{B} M'}$ and $\tilde{M}
\otimes_{\tilde{B}} \tilde{M}'$ (where $M$, $M'$, $B$ are viewed as $C$-modules) (`I, 1.3.13` and `1.6.3`).

Applying (1.4.7) in the special case $X = Y$, $\mathcal{F}' = \mathcal{O}_{X'}$, we see that the $\mathcal{A}'$-module
$\mathcal{A}(f'*(\mathcal{F}))$ identifies with $\mathcal{A}(\mathcal{F}) \otimes_{\mathcal{B}} \mathcal{A}'$.

**(1.4.8)**

<!-- label: II.1.4.8 -->

In particular, when $X = X' = Y$ (with $X$ affine over $S$), for any two quasi-coherent $\mathcal{O}_{X}$-modules
$\mathcal{F}$, $\mathcal{G}$,

```text
  𝒜(ℱ ⊗_{𝒪_X} 𝒢) = 𝒜(ℱ) ⊗_{𝒜(X)} 𝒜(𝒢)                                    (1.4.8.1)
```

up to canonical functorial isomorphism. If furthermore $\mathcal{F}$ admits a finite presentation, then `(I, 1.6.3)` and
`(I, 1.3.12)` give

```text
  𝒜(𝓗𝓸𝓶_X(ℱ, 𝒢)) = 𝓗𝓸𝓶_{𝒜(X)}(𝒜(ℱ), 𝒜(𝒢))                                  (1.4.8.2)
```

up to canonical isomorphism.

**Remark.**

<!-- label: II.1.4.9 -->

If $X$, $X'$ are two preschemes affine over $S$, then the disjoint sum $X \sqcup X'$ is also affine over $S$, since the
sum of two affine schemes is affine.

**Proposition.**

<!-- label: II.1.4.10 -->

Let $S$ be a prescheme, $\mathcal{B}$ a quasi-coherent $\mathcal{O}_{S}$-algebra, and $X =
\operatorname{Spec}(\mathcal{B})$. For every quasi-coherent sheaf of ideals $\mathcal{J}$ of $\mathcal{B}$,
$\tilde{\mathcal{J}}$ is a quasi-coherent sheaf of ideals of $\mathcal{O}_{X}$, and the closed subprescheme $Y$ of $X$
it defines is canonically isomorphic to $\operatorname{Spec}(\mathcal{B}/\mathcal{J})$.

**Proof.** By `(I, 4.2.3)`, $Y$ is affine over $S$; by (1.3.1) we reduce to $S$ affine, and the assertion is then
`(I, 4.1.2)`.

The conclusion of (1.4.10) can be restated: if $h : \mathcal{B} \to \mathcal{B}'$ is a _surjective_ homomorphism of
quasi-coherent $\mathcal{O}_{S}$-algebras, then `Spec(h) : Spec(ℬ') → Spec(ℬ)` is a _closed immersion_.

**Proposition.**

<!-- label: II.1.4.11 -->

<!-- original page 12 -->

Let $S$ be a prescheme, $\mathcal{B}$ a quasi-coherent $\mathcal{O}_{S}$-algebra, and $X =
\operatorname{Spec}(\mathcal{B})$. For every quasi-coherent sheaf of ideals $\mathcal{K}$ of $\mathcal{O}_{S}$ (denoting
by $f : X \to S$ the structure morphism), $f*(\mathcal{K})\mathcal{O}_{X} = \tilde{\mathcal{KB}}$ up to canonical
isomorphism.

**Proof.** The question is local on $S$, so we reduce to $S = \operatorname{Spec}(A)$ affine, where the assertion is
just `(I, 1.6.9)`.

## 1.5. Change of base prescheme

**Proposition.**

<!-- label: II.1.5.1 -->

Let $X$ be a prescheme affine over $S$. For every base change $g : S' \to S$, $X' = X_{(S')} = X \times_{S} S'$ is
affine over $S'$.

**Proof.** If $f' : X' \to S'$ is the projection, it suffices to prove that $f'^{-1}(U')$ is an affine open for every
affine open $U' \subset S'$ such that $g(U')$ is contained in an affine open $U \subset S$ (1.2.1). We may thus assume
$S$ and $S'$ are affine; it then suffices to show $X'$ is affine (1.3.4). But then $X$ is affine, and if $A$, $A'$, $B$
are the rings of $S$, $S'$, $X$, then $X'$ is the affine scheme with ring $A' \otimes_{A} B$ `(I, 3.2.2)`.

**Corollary.**

<!-- label: II.1.5.2 -->

Under the hypotheses of (1.5.1), let $f : X \to S$ be the structure morphism and $f' : X' \to S'$, $g' : X' \to X$ the
projections, so that the diagram

```text
   X ←─g'── X'
   │        │
 f │        │ f'
   ↓        ↓
   S ←──g── S'
```

is commutative. For every quasi-coherent $\mathcal{O}_{X}$-module $\mathcal{F}$, there is a canonical isomorphism of
$\mathcal{O}_{S'}$-modules

$$ u : g*(f_{*}(\mathcal{F})) \xrightarrow{\sim} f'_{*}(g'*(\mathcal{F})). (1.5.2.1) $$

In particular, there is a canonical isomorphism from $\mathcal{A}(X')$ to $g*(\mathcal{A}(X))$.

**Proof.** To define $u$, it suffices to define a homomorphism

```text
  v : f_*(ℱ) → g_*(f'_*(g'*(ℱ))) = f_*(g'_*(g'*(ℱ)))
```

and set $u = v\sharp$ `(0, 4.4.3)`. Take $v = f_{*}(\rho)$ with $\rho : \mathcal{F} \to g'_{*}(g'*(\mathcal{F}))$ the
canonical homomorphism `(0, 4.4.3)`. To prove that $u$ is an isomorphism, we may assume $S$, $S'$ (hence $X$, $X'$) are
affine. With the notation of (1.5.1), $\mathcal{F} = \tilde{M}$ for a $B$-module $M$, and one checks that both
$g*(f_{*}(\mathcal{F}))$ and $f'_{*}(g'*(\mathcal{F}))$ equal the $\mathcal{O}_{S'}$-module associated to the
$A'$-module $A' \otimes_{A} M$ (with $M$ viewed as an $A$-module), and that $u$ corresponds to the identity (`I, 1.6.3`,
`1.6.5`, `1.6.7`).

**Remark.**

<!-- label: II.1.5.3 -->

One should _not_ expect (1.5.2) to remain valid when $X$ is no longer affine over $S$ — not even when $S' =
\operatorname{Spec}(\kappa(s))$ for $s \in S$ with $S' \to S$ the canonical morphism `(I, 2.4.5)`, in which case $X'$ is
just the _fibre_ $f^{-1}(s)$ `(I, 3.6.2)`. In other words, when $X$ is not affine over $S$, the operation

<!-- original page 13 -->

"direct image of quasi-coherent sheaves" does not commute with the operation "passage to fibres". We will see however in
Chapter III `(III, 4.2.4)` a result in this direction, of an "asymptotic" character, valid for _coherent_ sheaves on $X$
when $f$ is proper (5.4) and $S$ is Noetherian.

**Corollary.**

<!-- label: II.1.5.4 -->

For every prescheme $X$ affine over $S$ and every $s \in S$, the fibre $f^{-1}(s)$ (where $f : X \to S$ is the structure
morphism) is an affine scheme.

**Proof.** Apply (1.5.1) with $S' = \operatorname{Spec}(\kappa(s))$ and use (1.3.4).

**Corollary.**

<!-- label: II.1.5.5 -->

Let $X$ be an $S$-prescheme and $S'$ a prescheme affine over $S$. Then $X' = X_{(S')}$ is a prescheme affine over $X$.
Furthermore, if $f : X \to S$ is the structure morphism, there is a canonical isomorphism of $\mathcal{O}_{X}$-algebras
$\mathcal{A}(X') \xrightarrow{\sim} f*(\mathcal{A}(S'))$, and for every quasi-coherent $\mathcal{A}(S')$-module
$\mathcal{M}$ a canonical di-isomorphism $f*(\mathcal{M}) \xrightarrow{\sim} \mathcal{A}(f'*(\tilde{\mathcal{M}}))$,
where $f' = f_{(S')} : X' \to S'$ is the structure morphism.

**Proof.** Swap the roles of $X$ and $S'$ in (1.5.1) and (1.5.2).

**(1.5.6)**

<!-- label: II.1.5.6 -->

Now let $S$, $S'$ be two preschemes, $q : S' \to S$ a morphism, $\mathcal{B}$ (resp. $\mathcal{B}'$) a quasi-coherent
$\mathcal{O}_{S}$-algebra (resp. $\mathcal{O}_{S'}$-algebra), and $u : \mathcal{B} \to \mathcal{B}'$ a $q$-morphism —
that is, a homomorphism $\mathcal{B} \to q_{*}(\mathcal{B}')$ of $\mathcal{O}_{S}$-algebras. If $X =
\operatorname{Spec}(\mathcal{B})$ and $X' = \operatorname{Spec}(\mathcal{B}')$, we obtain canonically a morphism

```text
  v = Spec(u) : X' → X
```

such that the diagram

```text
   X' ──v──→ X
   │         │                                                            (1.5.6.1)
   ↓         ↓
   S' ──q──→ S
```

commutes (the vertical arrows being the structure morphisms). Indeed, the datum of $u$ is equivalent to that of a
homomorphism $u\sharp : q*(\mathcal{B}) \to \mathcal{B}'$ of quasi-coherent $\mathcal{O}_{S'}$-algebras `(0, 4.4.3)`,
which canonically defines an $S'$-morphism

$$ w : \operatorname{Spec}(\mathcal{B}') \to \operatorname{Spec}(q*(\mathcal{B})) $$

with $\mathcal{A}(w) = u\sharp$ (1.2.7). On the other hand, (1.5.2) gives a canonical identification
$\operatorname{Spec}(q*(\mathcal{B})) \cong X \times_{S} S'$, and $v$ is the composition $X' \xrightarrow{w} X
\times_{S} S' \xrightarrow{pr_{1}} X$; the commutativity of (1.5.6.1) follows from the definitions. Let $U$ (resp. $U'$)
be an affine open of $S$ (resp. $S'$) with $q(U') \subset U$, with rings $A = \Gamma(U, \mathcal{O}_{S})$, $A' =
\Gamma(U', \mathcal{O}_{S'})$, and $B = \Gamma(U, \mathcal{B})$, $B' = \Gamma(U', \mathcal{B}')$. The restriction of $u$
to a $(q|U')$-morphism $\mathcal{B}|U \to \mathcal{B}'|U'$ corresponds to a di-homomorphism of algebras $B \to B'$; if
$V$, $V'$ are the inverse images of $U$, $U'$ in $X$, $X'$ under the structure morphisms, the morphism $V' \to V$ (the
restriction of $v$) corresponds `(I, 1.7.3)` to this di-homomorphism.

**(1.5.7)**

<!-- label: II.1.5.7 -->

Under the same hypotheses as (1.5.6), let $\mathcal{M}$ be a quasi-coherent $\mathcal{B}$-module. There is then a
canonical isomorphism of $\mathcal{O}_{X'}$-modules

```text
  v*(ℳ̃) ⥲ (q*(ℳ) ⊗_{q*(ℬ)} ℬ')̃.                                          (1.5.7.1)
```

<!-- original page 14 -->

Indeed, the canonical isomorphism (1.5.2.1) gives a canonical identification of $pr_{1}*(\tilde{\mathcal{M}})$ with the
sheaf on $\operatorname{Spec}(q*(\mathcal{B}))$ associated to the $q*(\mathcal{B})$-module $q*(\mathcal{M})$, and one
applies (1.4.7).

## 1.6. Affine morphisms

**(1.6.1)**

<!-- label: II.1.6.1 -->

We say that a morphism $f : X \to Y$ of preschemes is _affine_ if it makes $X$ an affine prescheme over $Y$. The
properties of preschemes affine over another translate as follows in this language:

**Proposition.**

<!-- label: II.1.6.2 -->

1. A closed immersion is affine.
1. The composition of two affine morphisms is affine.
1. If $f : X \to Y$ is an affine $S$-morphism, then $f_{(S')} : X_{(S')} \to Y_{(S')}$ is affine for every base change
   $S' \to S$.
1. If $f : X \to Y$ and $f' : X' \to Y'$ are two affine $S$-morphisms, then $f \times_{S} f' : X \times_{S} X' \to Y
   \times_{S} Y'$ is affine.
1. If $f : X \to Y$ and $g : Y \to Z$ are two morphisms such that $g \circ f$ is affine and $g$ is separated, then $f$
   is affine.
1. If $f$ is affine, so is $f_{red}$.

**Proof.** By `(I, 5.5.12)`, it suffices to prove (i), (ii), (iii). But (i) is just Example (1.2.2), (ii) is just
Corollary (1.3.5), and (iii) follows from (1.5.1) since $X_{(S')}$ identifies with $X \times_{Y} Y_{(S')}$
`(I, 3.3.11)`.

**Corollary.**

<!-- label: II.1.6.3 -->

If $X$ is an affine scheme and $Y$ is a scheme, then every morphism $f : X \to Y$ is affine.

**Proposition.**

<!-- label: II.1.6.4 -->

Let $Y$ be a locally Noetherian prescheme and $f : X \to Y$ a morphism of finite type. Then $f$ is affine if and only if
$f_{red}$ is.

**Proof.** By (1.6.2)(vi), it suffices to prove sufficiency. We may suppose $Y$ affine and Noetherian, and must show $X$
is affine; then $Y_{red}$ is affine, so by hypothesis $X_{red}$ is affine. Since $X$ is Noetherian, the conclusion
follows from `(I, 6.1.7)`.

## 1.7. Vector bundle associated to a sheaf of modules

**(1.7.1)**

<!-- label: II.1.7.1 -->

Let $A$ be a ring and $E$ an $A$-module. Recall that the _symmetric algebra_ on $E$, denoted $\mathbb{S}(E)$ (or
$\mathbb{S}_{A}(E)$), is the quotient of the tensor algebra $\mathbb{T}(E)$ by the two-sided ideal generated by $x
\otimes y - y \otimes x$ for $x, y \in E$. The algebra $\mathbb{S}(E)$ is characterized by the following universal
property: if $\sigma : E \to \mathbb{S}(E)$ is the canonical map (obtained by composing $E \to \mathbb{T}(E)$ with
$\mathbb{T}(E) \to \mathbb{S}(E)$), then every $A$-linear map $E \to B$ with $B$ a _commutative_ $A$-algebra factors
uniquely as $E \xrightarrow{\sigma} \mathbb{S}(E) \xrightarrow{g} B$, where $g$ is an $A$-homomorphism _of algebras_.
From this characterization, for two $A$-modules $E$, $F$,

```text
  𝕊(E ⊕ F) = 𝕊(E) ⊗ 𝕊(F)
```

<!-- original page 15 -->

up to canonical isomorphism. Furthermore, $\mathbb{S}(E)$ is a covariant functor in $E$ from $A$-modules to commutative
$A$-algebras, and if $E = \varinjlim E_{\lambda}$, then $\mathbb{S}(E) = \varinjlim \mathbb{S}(E_{\lambda})$ up to
canonical isomorphism. By abuse of notation, a product $\sigma(x_{1})\sigma(x_{2}) \cdots \sigma(x_{n})$ with $x_{i} \in
E$ is often written $x_{1} x_{2} \cdots x_{n}$ when no confusion can arise. The algebra $\mathbb{S}(E)$ is _graded_,
with $\mathbb{S}_{n}(E)$ the set of linear combinations of products of $n$ elements of $E$ ($n \geq 0$); $\mathbb{S}(A)$
is canonically isomorphic to the polynomial algebra `A[T]` in one indeterminate, and $\mathbb{S}(A^{n})$ to $A[T_{1},
\cdots, T_{n}]$.

**(1.7.2)**

<!-- label: II.1.7.2 -->

Let $\phi : A \to B$ be a ring homomorphism. If $F$ is a $B$-module, the canonical map $F \to \mathbb{S}(F)$ gives a
canonical map $F_{[\phi]} \to \mathbb{S}(F)_{[\phi]}$, which factors as $F_{[\phi]} \to \mathbb{S}(F_{[\phi]}) \to
\mathbb{S}(F)_{[\phi]}$; the canonical homomorphism $\mathbb{S}(F_{[\phi]}) \to \mathbb{S}(F)_{[\phi]}$ is surjective
but not in general bijective. If $E$ is an $A$-module, every di-homomorphism $E \to F$ (that is, every $A$-homomorphism
$E \to F_{[\phi]}$) yields canonically an $A$-homomorphism of algebras $\mathbb{S}(E) \to \mathbb{S}(F_{[\phi]}) \to
\mathbb{S}(F)_{[\phi]}$, i.e. a di-homomorphism of algebras $\mathbb{S}(E) \to \mathbb{S}(F)$.

With the same notation, for every $A$-module $E$, $\mathbb{S}(E \otimes_{A} B)$ is canonically isomorphic to
$\mathbb{S}(E) \otimes_{A} B$; this follows immediately from the universal property of $\mathbb{S}(E)$ (1.7.1).

**(1.7.3)**

<!-- label: II.1.7.3 -->

Let $R$ be a multiplicative subset of $A$. Applying (1.7.2) with $B = R^{-1}A$ and recalling that $R^{-1}E = E
\otimes_{A} R^{-1}A$, we get $\mathbb{S}(R^{-1}E) = R^{-1}\mathbb{S}(E)$ up to canonical isomorphism. If $R' \supset R$
is a second multiplicative subset, the diagram

```text
   R⁻¹E ─────→ R'⁻¹E
     │           │
     ↓           ↓
   𝕊(R⁻¹E) → 𝕊(R'⁻¹E)
```

commutes.

**(1.7.4)**

<!-- label: II.1.7.4 -->

Now let $(S, \mathcal{A})$ be a ringed space and $\mathcal{E}$ an $\mathcal{A}$-module on $S$. Associating to every open
$U \subset S$ the $\Gamma(U, \mathcal{A})$-module $\mathbb{S}(\Gamma(U, \mathcal{E}))$ defines (by the functoriality of
$\mathbb{S}(E)$ (1.7.2)) a presheaf of algebras; we call the associated sheaf, denoted $\mathbb{S}(\mathcal{E})$ or
$\mathbb{S}_{\mathcal{A}}(\mathcal{E})$, the _symmetric $\mathcal{A}$-algebra on the $\mathcal{A}$-module
$\mathcal{E}$_. By (1.7.1) $\mathbb{S}(\mathcal{E})$ is the solution of a universal problem: every homomorphism of
$\mathcal{A}$-modules $\mathcal{E} \to \mathcal{B}$ with $\mathcal{B}$ an $\mathcal{A}$-algebra factors uniquely as
$\mathcal{E} \to \mathbb{S}(\mathcal{E}) \to \mathcal{B}$, the second arrow being a homomorphism of
$\mathcal{A}$-algebras. There is thus a bijective correspondence between homomorphisms $\mathcal{E} \to \mathcal{B}$ of
$\mathcal{A}$-modules and homomorphisms $\mathbb{S}(\mathcal{E}) \to \mathcal{B}$ of $\mathcal{A}$-algebras. In
particular, every homomorphism $u : \mathcal{E} \to \mathcal{F}$ of $\mathcal{A}$-modules defines a homomorphism
$\mathbb{S}(u) : \mathbb{S}(\mathcal{E}) \to \mathbb{S}(\mathcal{F})$ of $\mathcal{A}$-algebras, and
$\mathbb{S}(\mathcal{E})$ is a covariant functor in $\mathcal{E}$.

<!-- original page 16 -->

By (1.7.2) and the commutation of $\mathbb{S}$ with direct limits, $(\mathbb{S}(\mathcal{E}))_{s} =
\mathbb{S}(\mathcal{E}_{s})$ for every $s \in S$. For two $\mathcal{A}$-modules $\mathcal{E}$, $\mathcal{F}$,
$\mathbb{S}(\mathcal{E} \oplus \mathcal{F})$ identifies canonically with $\mathbb{S}(\mathcal{E}) \otimes_{\mathcal{A}}
\mathbb{S}(\mathcal{F})$, as one sees on presheaves.

We also note that $\mathbb{S}(\mathcal{E})$ is a graded $\mathcal{A}$-algebra — the infinite direct sum of the
$\mathbb{S}_{n}(\mathcal{E})$, where $\mathbb{S}_{n}(\mathcal{E})$ is the sheaf associated to the presheaf $U \mapsto
\mathbb{S}_{n}(\Gamma(U, \mathcal{E}))$. In particular $\mathbb{S}_{\mathcal{A}}(\mathcal{A})$ identifies with
$\mathcal{A}[T] = \mathcal{A} \otimes_{\mathbb{Z}} \mathbb{Z}[T]$ ($T$ an indeterminate, $\mathbb{Z}$ viewed as a
constant sheaf).

**(1.7.5)**

<!-- label: II.1.7.5 -->

Let $(T, \mathcal{B})$ be a second ringed space and $f : (S, \mathcal{A}) \to (T, \mathcal{B})$ a morphism. For
$\mathcal{F}$ a $\mathcal{B}$-module, $\mathbb{S}(f*(\mathcal{F}))$ identifies canonically with
$f*(\mathbb{S}(\mathcal{F}))$: with $f = (\psi, \theta)$ and by definition `(0, 4.3.1)`,

```text
  𝕊(f*(ℱ)) = 𝕊(ψ*(ℱ) ⊗_{ψ*(ℬ)} 𝒜) = 𝕊(ψ*(ℱ)) ⊗_{ψ*(ℬ)} 𝒜
```

by (1.7.2). For every open $U \subset S$ and every section $h$ of $\mathbb{S}(\psi*(\mathcal{F}))$ over $U$, $h$ agrees
in a neighbourhood $V$ of every $s \in U$ with an element of $\mathbb{S}(\Gamma(V, \psi*(\mathcal{F})))$; unfolding the
definition of $\psi*(\mathcal{F})$ `(0, 3.7.1)` and using that every element of $\mathbb{S}(E)$ is a linear combination
of finitely many products of elements of $E$, one finds a neighbourhood $W$ of $\psi(s)$ in $T$, a section $h'$ of
$\mathbb{S}(\mathcal{F})$ over $W$, and a neighbourhood $V' \subset V \cap \psi^{-1}(W)$ of $s$ such that $h$ agrees
with $t \mapsto h'(\psi(t))$ on $V'$; whence the assertion.

**Proposition.**

<!-- label: II.1.7.6 -->

Let $A$ be a ring, $S = \operatorname{Spec}(A)$ its prime spectrum, and $\mathcal{E} = \tilde{M}$ the
$\mathcal{O}_{S}$-module associated to an $A$-module $M$. Then the $\mathcal{O}_{S}$-algebra $\mathbb{S}(\mathcal{E})$
is associated to the $A$-algebra $\mathbb{S}(M)$.

**Proof.** For every $f \in A$, $\mathbb{S}(M_{f}) = (\mathbb{S}(M))_{f}$ (1.7.3), so the proposition follows from
`(I, 1.3.4)`.

**Corollary.**

<!-- label: II.1.7.7 -->

If $S$ is a prescheme and $\mathcal{E}$ a quasi-coherent $\mathcal{O}_{S}$-module, then the $\mathcal{O}_{S}$-algebra
$\mathbb{S}(\mathcal{E})$ is quasi-coherent. If furthermore $\mathcal{E}$ is of finite type, then each
$\mathbb{S}_{n}(\mathcal{E})$ is an $\mathcal{O}_{S}$-module of finite type.

**Proof.** The first assertion is immediate from (1.7.6) and `(I, 1.4.1)`. The second follows because for an $A$-module
$E$ of finite type, $\mathbb{S}_{n}(E)$ is also of finite type; apply `(I, 1.3.13)`.

**Definition.**

<!-- label: II.1.7.8 -->

Let $\mathcal{E}$ be a quasi-coherent $\mathcal{O}_{S}$-module. We call the _vector bundle over $S$ defined by
$\mathcal{E}$_, denoted $\mathbb{V}(\mathcal{E})$, the spectrum (1.3.1) of the quasi-coherent $\mathcal{O}_{S}$-algebra
$\mathbb{S}(\mathcal{E})$.

By (1.2.7), for every $S$-prescheme $X$ there is a canonical bijective correspondence between the $S$-morphisms $X \to
\mathbb{V}(\mathcal{E})$ and the homomorphisms $\mathbb{S}(\mathcal{E}) \to \mathcal{A}(X)$ of
$\mathcal{O}_{S}$-algebras, hence also between these $S$-morphisms and the homomorphisms $\mathcal{E} \to \mathcal{A}(X)
= f_{*}(\mathcal{O}_{X})$ of $\mathcal{O}_{S}$-modules (where $f$ is the structure morphism $X \to S$). In particular:

**(1.7.9)**

<!-- label: II.1.7.9 -->

Take $X$ to be the subprescheme induced by $S$ on an _open_ $U \subset S$. Then the $S$-morphisms $U \to
\mathbb{V}(\mathcal{E})$ are just the $U$-sections `(I, 2.5.5)` of the $U$-prescheme induced by
$\mathbb{V}(\mathcal{E})$ on $p^{-1}(U)$ (with $p : \mathbb{V}(\mathcal{E}) \to S$ the structure morphism). By the
above, these $U$-sections correspond bijectively to homomorphisms of $\mathcal{O}_{S}$-modules $\mathcal{E} \to
j_{*}(\mathcal{O}_{S}|U)$ (with $j : U \to S$ the canonical injection), or

<!-- original page 17 -->

equivalently `(0, 4.4.3)` to $(\mathcal{O}_{S}|U)$-homomorphisms $j*(\mathcal{E}) = \mathcal{E}|U \to
\mathcal{O}_{S}|U$. It is immediate that restriction to an open $U' \subset U$ of an $S$-morphism $U \to
\mathbb{V}(\mathcal{E})$ corresponds to the restriction to $U'$ of the corresponding homomorphism $\mathcal{E}|U \to
\mathcal{O}_{S}|U$. We conclude that _the sheaf of germs of $S$-sections_ of $\mathbb{V}(\mathcal{E})$ is canonically
identified with the _dual_ $\check{\mathcal{E}}$ of $\mathcal{E}$.

In particular, taking $X = U = S$, the _zero_ homomorphism $\mathcal{E} \to \mathcal{O}_{S}$ corresponds to a canonical
$S$-section of $\mathbb{V}(\mathcal{E})$, called the _zero $S$-section_ (cf. (8.3.3)).

**(1.7.10)**

<!-- label: II.1.7.10 -->

Now take $X$ to be the spectrum ${\xi}$ of a field $K$; the structure morphism $f : X \to S$ corresponds to a
monomorphism $\kappa(s) \to K$ with $s = f(\xi)$ `(I, 2.4.6)`. The $S$-morphisms ${\xi} \to \mathbb{V}(\mathcal{E})$ are
then just the _geometric points of $\mathbb{V}(\mathcal{E})$ with values in the extension $K$ of $\kappa(s)$_
`(I, 3.4.5)`, points localized over $p^{-1}(s)$. The set of these points — which we call the _rational geometric fibre
over $K$_ of $\mathbb{V}(\mathcal{E})$ over $s$ — identifies, by (1.7.8), with
$\operatorname{Hom}_{\mathcal{O}_{S}}(\mathcal{E}, f_{*}(\mathcal{O}_{X}))$, or equivalently `(0, 4.4.3)` with
$\operatorname{Hom}_{\mathcal{O}_{X}}(f*(\mathcal{E}), \mathcal{O}_{X} = K)$. By definition `(0, 4.3.1)`
$f*(\mathcal{E}) = \mathcal{E}_{s} \otimes_{\mathcal{O}_{s}} K = \mathcal{E}^{s} \otimes_{\kappa(s)} K$ with
$\mathcal{E}^{s} = \mathcal{E}_{s}/\mathfrak{m}_{s} \mathcal{E}_{s}$; so the rational geometric fibre of
$\mathbb{V}(\mathcal{E})$ over $s$ with values in $K$ identifies with the _dual_ of the $K$-vector space
$\mathcal{E}^{s} \otimes_{\kappa(s)} K$. If $\mathcal{E}^{s}$ or $K$ is finite-dimensional over $\kappa(s)$, this dual
identifies further with $\check{\mathcal{E}^{s}} \otimes_{\kappa(s)} K$, where $\check{\mathcal{E}^{s}}$ denotes the
dual of the $\kappa(s)$-vector space $\mathcal{E}^{s}$.

**Proposition.**

<!-- label: II.1.7.11 -->

1. $\mathbb{V}(\mathcal{E})$ is a contravariant functor in $\mathcal{E}$ from quasi-coherent $\mathcal{O}_{S}$-modules
   to affine $S$-schemes.
1. If $\mathcal{E}$ is an $\mathcal{O}_{S}$-module of finite type, then $\mathbb{V}(\mathcal{E})$ is of finite type over
   $S$.
1. If $\mathcal{E}$ and $\mathcal{F}$ are two quasi-coherent $\mathcal{O}_{S}$-modules, then $\mathbb{V}(\mathcal{E}
   \oplus \mathcal{F})$ identifies canonically with $\mathbb{V}(\mathcal{E}) \times_{S} \mathbb{V}(\mathcal{F})$.
1. For a morphism $g : S' \to S$ and any quasi-coherent $\mathcal{O}_{S}$-module $\mathcal{E}$,
   $\mathbb{V}(g*(\mathcal{E}))$ identifies canonically with $\mathbb{V}(\mathcal{E})_{(S')} = \mathbb{V}(\mathcal{E})
   \times_{S} S'$.
1. A surjective homomorphism $\mathcal{E} \to \mathcal{F}$ of quasi-coherent $\mathcal{O}_{S}$-modules corresponds to a
   closed immersion $\mathbb{V}(\mathcal{F}) \to \mathbb{V}(\mathcal{E})$.

**Proof.** (i) is immediate from (1.2.7), given that every homomorphism $\mathcal{E} \to \mathcal{F}$ of
$\mathcal{O}_{S}$-modules canonically defines a homomorphism $\mathbb{S}(\mathcal{E}) \to \mathbb{S}(\mathcal{F})$ of
$\mathcal{O}_{S}$-algebras. (ii) follows immediately from `(I, 6.3.1)` and the fact that for an $A$-module $E$ of finite
type, $\mathbb{S}(E)$ is an $A$-algebra of finite type. For (iii), start from the canonical isomorphism
$\mathbb{S}(\mathcal{E} \oplus \mathcal{F}) \xrightarrow{\sim} \mathbb{S}(\mathcal{E}) \otimes_{\mathcal{O}_{S}}
\mathbb{S}(\mathcal{F})$ (1.7.4) and apply (1.4.6). Similarly, for (iv), start from $\mathbb{S}(g*(\mathcal{E}))
\xrightarrow{\sim} g*(\mathbb{S}(\mathcal{E}))$ (1.7.5) and apply (1.5.2). Finally, for (v), surjectivity of
$\mathcal{E} \to \mathcal{F}$ implies surjectivity of the corresponding homomorphism $\mathbb{S}(\mathcal{E}) \to
\mathbb{S}(\mathcal{F})$ of $\mathcal{O}_{S}$-algebras, and the conclusion follows from (1.4.10).

**(1.7.12)**

<!-- label: II.1.7.12 -->

Taking $\mathcal{E} = \mathcal{O}_{S}$ in particular, the prescheme $\mathbb{V}(\mathcal{O}_{S})$ is the affine
$S$-scheme which is the spectrum of the $\mathcal{O}_{S}$-algebra $\mathbb{S}(\mathcal{O}_{S})$, and the latter
identifies with the $\mathcal{O}_{S}$-algebra $\mathcal{O}_{S}[T] = \mathcal{O}_{S} \otimes_{\mathbb{Z}} \mathbb{Z}[T]$

<!-- original page 18 -->

($T$ an indeterminate). This is evident when $S = \operatorname{Spec}(\mathbb{Z})$, by (1.7.6), and the general case
follows by considering the structure morphism $S \to \operatorname{Spec}(\mathbb{Z})$ and using (1.7.11)(iv). We
therefore write $\mathbb{V}(\mathcal{O}_{S}) = S[T]$, and we have

```text
  S[T] = S ⊗_ℤ ℤ[T].                                                      (1.7.12.1)
```

The identification of the sheaf of germs of $S$-sections of `S[T]` with $\mathcal{O}_{S}$, already seen in
`(I, 3.3.15)`, reappears here in a more general context, as a special case of (1.7.9).

**(1.7.13)**

<!-- label: II.1.7.13 -->

For every $S$-prescheme $X$, we have seen (1.7.8) that $\operatorname{Hom}_{S}(X, S[T])$ is canonically identified with
$\operatorname{Hom}_{\mathcal{O}_{S}}(\mathcal{O}_{S}, \mathcal{A}(X))$, which is canonically isomorphic to $\Gamma(S,
\mathcal{A}(X))$ and so carries a ring structure. To every $S$-morphism $h : X \to Y$ corresponds a morphism
$\Gamma(\mathcal{A}(h)) : \Gamma(S, \mathcal{A}(Y)) \to \Gamma(S, \mathcal{A}(X))$ for these ring structures (1.1.2).
Equipped with this ring structure, $\operatorname{Hom}_{S}(X, S[T])$ becomes a _contravariant functor_ in $X$ from the
category of $S$-preschemes to rings. On the other hand, $\operatorname{Hom}_{S}(X, \mathbb{V}(\mathcal{E}))$ identifies
likewise with $\operatorname{Hom}_{\mathcal{O}_{S}}(\mathcal{E}, \mathcal{A}(X))$ (with $\mathcal{A}(X)$ viewed as an
_$\mathcal{O}_{S}$-module_); it is therefore canonically endowed with a module structure over the ring
$\operatorname{Hom}_{S}(X, S[T])$, and the pair

```text
  (Hom_S(X, S[T]), Hom_S(X, 𝕍(ℰ)))
```

is a contravariant functor in $X$ with values in the category whose objects are pairs $(A, M)$ with $A$ a ring and $M$
an $A$-module, the morphisms being di-homomorphisms.

We interpret this by saying that `S[T]` is an _$S$-scheme of rings_ and that $\mathbb{V}(\mathcal{E})$ is an _$S$-scheme
of modules_ over the $S$-scheme of rings `S[T]` (cf. Chapter 0, §8).

**(1.7.14)**

<!-- label: II.1.7.14 -->

We shall see that the $S$-scheme-of-modules structure on $\mathbb{V}(\mathcal{E})$ reconstructs $\mathcal{E}$ up to
unique isomorphism: we show that $\mathcal{E}$ is canonically isomorphic to an $\mathcal{O}_{S}$-submodule of
$\mathbb{S}(\mathcal{E}) = \mathcal{A}(\mathbb{V}(\mathcal{E}))$ defined by means of that structure. Indeed (1.7.4), the
set $\operatorname{Hom}_{\mathcal{O}_{S}}(\mathbb{S}(\mathcal{E}), \mathcal{A}(X))$ of homomorphisms of
_$\mathcal{O}_{S}$-algebras_ identifies canonically with $\operatorname{Hom}_{\mathcal{O}_{S}}(\mathcal{E},
\mathcal{A}(X))$, the set of homomorphisms of _$\mathcal{O}_{S}$-modules_: if $h$, $h'$ are two elements of the latter
set, $s_{i}$ ($1 \leq i \leq n$) sections of $\mathcal{E}$ over an open $U \subset S$, and $t$ a section of
$\mathcal{A}(X)$ over $U$, then by definition

```text
  (h + h')(s_1 s_2 ⋯ s_n) = ∏_{i=1}^n (h(s_i) + h'(s_i))
```

and

```text
  (t · h)(s_1 s_2 ⋯ s_n) = tⁿ ∏_{i=1}^n h(s_i).
```

Given this, if $z$ is a section of $\mathbb{S}(\mathcal{E})$ over $U$, then $h \mapsto h(z)$ is a map from
$\operatorname{Hom}_{S}(X, \mathbb{V}(\mathcal{E})) = \operatorname{Hom}_{\mathcal{O}_{S}}(\mathbb{S}(\mathcal{E}),
\mathcal{A}(X))$ to $\Gamma(U, \mathcal{A}(X))$. We will

<!-- original page 19 -->

show that $\mathcal{E}$ is identified with the $\mathcal{O}_{S}$-submodule of $\mathbb{S}(\mathcal{E})$ such that, _for
every open $U \subset S$, every section $z$ of this submodule over $U$, and every $S$-prescheme $X$, the map $h \mapsto
h(z)$ from $\operatorname{Hom}_{\mathcal{O}_{S}|U}(\mathbb{S}(\mathcal{E})|U, \mathcal{A}(X)|U)$ to $\Gamma(U,
\mathcal{A}(X))$ is a homomorphism of $\Gamma(U, \mathcal{A}(X))$-modules_.

It is immediate that $\mathcal{E}$ has this property; for the converse, we reduce to proving that when $S =
\operatorname{Spec}(A)$ and $\mathcal{E} = \tilde{M}$, a section $z$ of $\mathbb{S}(\mathcal{E})$ over $S$ (for $U = S$)
satisfying the stated property must be a section of $\mathcal{E}$. Write $z = \sum^{\infty}_{n=0} z_{n}$ with $z_{n} \in
\mathbb{S}_{n}(M)$; we must show $z_{n} = 0$ for $n \neq 1$. Set $B = \mathbb{S}(M)$ and take $X =
\operatorname{Spec}(B[T])$ for an indeterminate $T$. Then $\operatorname{Hom}_{\mathcal{O}_{S}}(\mathbb{S}(\mathcal{E}),
\mathcal{A}(X))$ identifies with the set of ring homomorphisms $h : B \to B[T]$ `(I, 1.3.13)`, and by the calculation
above $(T \cdot h)(z) = \sum^{\infty}_{n=0} T^{n} h(z_{n})$; the hypothesis on $z$ gives $\sum^{\infty}_{n=0} T^{n}
h(z_{n}) = T \cdot \sum^{\infty}_{n=0} h(z_{n})$ for every $h$. Taking $h$ to be the canonical injection yields
$\sum^{\infty}_{n=0} T^{n} z_{n} = T \cdot \sum^{\infty}_{n=0} z_{n}$, which forces $z_{n} = 0$ for $n \neq 1$.

**Proposition.**

<!-- label: II.1.7.15 -->

Let $Y$ be a prescheme whose underlying space is Noetherian, or a quasi-compact scheme. Every affine $Y$-scheme $X$ of
finite type over $Y$ is $Y$-isomorphic to a closed $Y$-subscheme of a $Y$-scheme of the form $\mathbb{V}(\mathcal{E})$,
where $\mathcal{E}$ is a quasi-coherent $\mathcal{O}_{Y}$-module of finite type.

**Proof.** The quasi-coherent $\mathcal{O}_{Y}$-algebra $\mathcal{A}(X)$ is of finite type (1.3.7). The hypotheses imply
$\mathcal{A}(X)$ is generated by a quasi-coherent $\mathcal{O}_{Y}$-submodule $\mathcal{E}$ of finite type `(I, 9.6.5)`;
by definition, the canonical homomorphism $\mathbb{S}(\mathcal{E}) \to \mathcal{A}(X)$ extending the injection
$\mathcal{E} \to \mathcal{A}(X)$ is _surjective_. The conclusion follows from (1.4.10).

# §4. Projective bundles. Ample sheaves

## 4.1. Definition of projective bundles

**Definition.**

<!-- label: II.4.1.1 -->

Let $Y$ be a prescheme, $\mathcal{E}$ a quasi-coherent $\mathcal{O}_{Y}$-module, and
$\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E})$ the symmetric $\mathcal{O}_{Y}$-algebra of $\mathcal{E}$ (1.7.4), which is
quasi-coherent (1.7.7). We call the _projective bundle over $Y$ defined by $\mathcal{E}$_, and denote by
$\mathbb{P}(\mathcal{E})$, the $Y$-scheme $P = \operatorname{Proj}(\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}))$. The
$\mathcal{O}_{P}$-module $\mathcal{O}_{P}(1)$ is called the _tautological sheaf on $P$_.

> _Translator's note._ EGA's 1961 term `faisceau fondamental` (literally "fundamental sheaf") is the modern
> _tautological line bundle_, or _Serre line bundle_, $\mathcal{O}_{\mathbb{P}(\mathcal{E})}(1)$. We render it as
> "tautological sheaf" throughout §4; the term is recorded in the ledger under §4.1.1.

When $Y$ is affine of ring $A$, we have $\mathcal{E} = \tilde{E}$ for some $A$-module $E$, and we then write
$\mathbb{P}(E)$ in place of $\mathbb{P}(\tilde{E})$.

When we take $\mathcal{E} = \mathcal{O}^{n}_{Y}$, we write $\mathbb{P}^{n-1}_{Y}$ in place of $\mathbb{P}(\mathcal{E})$;
if in addition $Y$ is affine of ring $A$, we also write $\mathbb{P}^{n-1}_{A}$ in place of $\mathbb{P}^{n-1}_{Y}$. Since
$\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{O}_{Y})$ is canonically identified with $\mathcal{O}_{Y}[T]$ (1.7.4),
$\mathbb{P}^{0}_{Y}$ is canonically identified with $Y$ (3.1.7); the example (2.4.3) is then nothing but
$\mathbb{P}^{1}_{K}$.

**(4.1.2)**

<!-- label: II.4.1.2 -->

Let $\mathcal{E}$, $\mathcal{F}$ be two quasi-coherent $\mathcal{O}_{Y}$-modules and $u : \mathcal{E} \to \mathcal{F}$
an $\mathcal{O}_{Y}$-homomorphism; there is canonically associated to it a homomorphism $\mathbb{S}(u) :
\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}) \to \mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{F})$ of graded
$\mathcal{O}_{Y}$-algebras (1.7.4). If $u$ is _surjective_, then so is $\mathbb{S}(u)$, and therefore (3.6.2, (i))
$\operatorname{Proj}(\mathbb{S}(u))$ is a _closed immersion_ $\mathbb{P}(\mathcal{F}) \to \mathbb{P}(\mathcal{E})$,
which we denote by $\mathbb{P}(u)$. We may therefore say that $\mathbb{P}(\mathcal{E})$ is a _contravariant functor_ in
$\mathcal{E}$, provided we restrict the morphisms of quasi-coherent $\mathcal{O}_{Y}$-modules to the surjective
homomorphisms.

Still supposing $u$ surjective and setting $P = \mathbb{P}(\mathcal{E})$, $Q = \mathbb{P}(\mathcal{F})$, and $j =
\mathbb{P}(u)$, we have, up to isomorphism,

```text
  j*(𝒪_P(n)) = 𝒪_Q(n)            for all n ∈ ℤ,                            (4.1.2.1)
```

as follows from (3.6.3).

**(4.1.3)**

<!-- label: II.4.1.3 -->

Now let $\psi : Y' \to Y$ be a morphism and set $\mathcal{E}' = \psi*(\mathcal{E})$; we then have
$\mathbb{S}_{\mathcal{O}_{Y'}}(\mathcal{E}') = \psi*(\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}))$ (1.7.5); hence (3.5.3),

```text
  ℙ(ψ*(𝓔)) = ℙ(𝓔) ×_Y Y'                                                   (4.1.3.1)
```

up to canonical isomorphism. Furthermore, we evidently have

$$ \psi*((\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}))(n)) = (\mathbb{S}_{\mathcal{O}_{Y'}}(\mathcal{E}'))(n) $$

for all $n \in \mathbb{Z}$; setting $P = \mathbb{P}(\mathcal{E})$ and $P' = \mathbb{P}(\mathcal{E}')$, we therefore have
(3.5.4), up to isomorphism,

```text
  𝒪_{P'}(n) = 𝒪_P(n) ⊗_Y 𝒪_{Y'}    for all n ∈ ℤ.                          (4.1.3.2)
```

<!-- original page 72 -->

**Proposition.**

<!-- label: II.4.1.4 -->

Let $\mathcal{L}$ be an invertible $\mathcal{O}_{Y}$-module. For every quasi-coherent $\mathcal{O}_{Y}$-module
$\mathcal{E}$, there exists a canonical $Y$-isomorphism $i_{\mathcal{L}} : \mathbb{P}(\mathcal{E}) \xrightarrow{\sim}
\mathbb{P}(\mathcal{E} \otimes \mathcal{L})$; furthermore, setting $P = \mathbb{P}(\mathcal{E})$ and $Q =
\mathbb{P}(\mathcal{E} \otimes \mathcal{L})$, $i_{\mathcal{L}}*(\mathcal{O}_{Q}(n))$ is canonically isomorphic to
$\mathcal{O}_{P}(n) \otimes_{Y} \mathcal{L}^{\otimes n}$ for all $n \in \mathbb{Z}$.

**Proof.** Note first that if $A$ is a ring, $E$ an $A$-module, and $L$ a _free monogenic_ $A$-module, one canonically
defines a homomorphism of $A$-modules

```text
  𝕊_n(E ⊗ L) → 𝕊_n(E) ⊗ L^{⊗n}
```

by sending $(x_{1} \otimes y_{1}) \cdots (x_{n} \otimes y_{n})$ to

```text
  (x_1 x_2 ⋯ x_n) ⊗ (y_1 ⊗ y_2 ⊗ ⋯ ⊗ y_n)         (x_i ∈ E, y_i ∈ L, for 1 ≤ i ≤ n).
```

One verifies immediately (by reducing to the case $L = A$) that this homomorphism is in fact an isomorphism. We conclude
a canonical isomorphism of graded $A$-algebras $\mathbb{S}_{A}(E \otimes L) \xrightarrow{\sim} \oplus_{n\geq 0}
\mathbb{S}_{n}(E) \otimes L^{\otimes n}$. Returning to the situation of (4.1.4), the preceding remarks allow us to
define a canonical isomorphism of graded $\mathcal{O}_{Y}$-algebras

```text
  𝕊_{𝒪_Y}(𝓔 ⊗_{𝒪_Y} ℒ) ⥲ ⊕_{n≥0} 𝕊_n(𝓔) ⊗_{𝒪_Y} ℒ^{⊗n}                    (4.1.4.1)
```

by defining this isomorphism as one of presheaves and using (1.7.4), `(I, 1.3.9)`, and `(I, 1.3.12)`. The proposition
then follows from (3.1.8, (iii)) and (3.2.10).

**(4.1.5)**

<!-- label: II.4.1.5 -->

With the hypotheses of (4.1.1), set $P = \mathbb{P}(\mathcal{E})$ and denote by $p$ the structure morphism $P \to Y$.
Since by definition $\mathcal{E} = (\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}))_{1}$, we have a canonical homomorphism
$\alpha_{1} : \mathcal{E} \to p_{*}(\mathcal{O}_{P}(1))$ (3.3.2.2), and therefore also `(0, 4.4.3)` a canonical
homomorphism

$$ \alpha_{1}\sharp : p*(\mathcal{E}) \to \mathcal{O}_{P}(1). (4.1.5.1) $$

**Proposition.**

<!-- label: II.4.1.6 -->

The canonical homomorphism (4.1.5.1) is surjective.

**Proof.** We saw in (3.3.2) that $\alpha_{1}\sharp$ corresponds functorially to the canonical homomorphism $\mathcal{E}
\otimes_{\mathcal{O}_{Y}} \mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}) \to (\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}))(1)$;
since by definition $\mathcal{E}$ generates $\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E})$, this homomorphism is
surjective, whence the conclusion by (3.2.4).

## 4.2. Morphisms from a prescheme to a projective bundle

**(4.2.1)**

<!-- label: II.4.2.1 -->

Keeping the notation of (4.1.5), let $X$ be a $Y$-prescheme, $q : X \to Y$ its structure morphism, and $r : X \to P$ a
$Y$-_morphism_, so that we have the commutative diagram

```text
         r
   P ←─────── X
    \       /
   p \     / q
      ↘   ↙
        Y
```

<!-- original page 73 -->

Since the functor $r*$ is right exact `(0, 4.3.1)`, from the surjective homomorphism (4.1.5.1) we obtain a surjective
homomorphism

$$ r*(\alpha_{1}\sharp) : r*(p*(\mathcal{E})) \to r*(\mathcal{O}_{P}(1)). $$

But $r*(p*(\mathcal{E})) = q*(\mathcal{E})$, and $r*(\mathcal{O}_{P}(1))$ is locally isomorphic to $r*(\mathcal{O}_{P})
= \mathcal{O}_{X}$, in other words an _invertible_ sheaf $\mathcal{L}_{r}$ on $\mathcal{O}_{X}$. We have thus defined,
starting from $r$, a canonical surjective $\mathcal{O}_{X}$-homomorphism

$$ \phi_{r} : q*(\mathcal{E}) \to \mathcal{L}_{r}. (4.2.1.1) $$

When $Y = \operatorname{Spec}(A)$ is affine and $\mathcal{E} = \tilde{E}$, this homomorphism may be made more explicit
as follows: given $f \in E$, it follows from (2.6.3) that

$$ r^{-1}(D_{+}(f)) = X_{\phi_{r}\flat(f)}. (4.2.1.2) $$

Let $V$ be an affine open of $X$ contained in $r^{-1}(D_{+}(f))$, and let $B$ be its ring, an $A$-algebra; set $S =
\mathbb{S}_{A}(E)$. The restriction of $r$ to $V$ corresponds to an $A$-homomorphism $\omega : S_{(f)} \to B$; we have
$q*(\mathcal{E})|V = (E \otimes_{A} B)~$ and $\mathcal{L}_{r}|V = \tilde{L}_{r}$, where $L_{r} = (S(1))_{(f)}
\otimes_{S_{(f)}} B_{[\omega]}$ `(I, 1.6.5)`. The restriction of $\phi_{r}$ to $q*(\mathcal{E})|V$ corresponds to the
$B$-homomorphism $u : E \otimes_{A} B \to L_{r}$ sending $x \otimes 1$ to $(x/1) \otimes f = (f/1) \otimes \omega(x/f)$.
The canonical extension of $\phi_{r}$ to a homomorphism of $\mathcal{O}_{X}$-algebras

```text
  ψ_r : q*(𝕊(𝓔)) = 𝕊(q*(𝓔)) → 𝕊(ℒ_r) = ⊕_{n≥0} ℒ_r^{⊗n}
```

is thus such that the restriction of $\psi_{r}$ to $q*(\mathbb{S}_{n}(\mathcal{E}))|V$ corresponds to the homomorphism
$\mathbb{S}_{n}(E \otimes_{A} B) = \mathbb{S}_{n}(E) \otimes_{A} B \to L^{\otimes n}_{r}$ sending $s \otimes 1$ to
$(f/1)^{\otimes n} \otimes \omega(s/f^{n})$.

**(4.2.2)**

<!-- label: II.4.2.2 -->

Conversely, suppose given a morphism $q : X \to Y$, an invertible $\mathcal{O}_{X}$-module $\mathcal{L}$, and a
quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{E}$; to a homomorphism $\phi : q*(\mathcal{E}) \to \mathcal{L}$ there
canonically corresponds a homomorphism of quasi-coherent $\mathcal{O}_{X}$-algebras

```text
  ψ : 𝕊(q*(𝓔)) = q*(𝕊(𝓔)) → ⊕_{n≥0} ℒ^{⊗n}
```

and therefore (3.7.1) a $Y$-morphism $r_{\mathcal{L},\psi} : G(\psi) \to \operatorname{Proj}(\mathbb{S}(\mathcal{E})) =
\mathbb{P}(\mathcal{E})$, which we denote $r_{\mathcal{L},\phi}$. If $\phi$ is surjective, then so is $\psi$, and
therefore (3.7.4) $r_{\mathcal{L},\phi}$ is _everywhere defined_. Moreover, with the notation of (4.2.1) and (4.2.2):

**Proposition.**

<!-- label: II.4.2.3 -->

Given a morphism $q : X \to Y$ and a quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{E}$, the maps $r \mapsto
(\mathcal{L}_{r}, \phi_{r})$ and $(\mathcal{L}, \phi) \mapsto r_{\mathcal{L},\phi}$ put into bijective correspondence
the set of $Y$-morphisms $r : X \to \mathbb{P}(\mathcal{E})$ and the set of equivalence classes of pairs $(\mathcal{L},
\phi)$ consisting of an invertible $\mathcal{O}_{X}$-module $\mathcal{L}$ and a surjective homomorphism $\phi :
q*(\mathcal{E}) \to \mathcal{L}$, two pairs $(\mathcal{L}, \phi)$ and $(\mathcal{L}', \phi')$ being equivalent if there
exists an $\mathcal{O}_{X}$-isomorphism $\tau : \mathcal{L} \xrightarrow{\sim} \mathcal{L}'$ such that $\phi' = \tau
\circ \phi$.

**Proof.** Start first from a $Y$-morphism $r : X \to \mathbb{P}(\mathcal{E})$, form $\mathcal{L}_{r}$ and $\phi_{r}$
(4.2.1), and set $r' = r_{\mathcal{L}_{r}, \phi_{r}}$; it follows at once from (4.2.1) and (3.7.2) that the morphisms
$r$ and $r'$ are identical (taking as generator of $\mathcal{L}_{r}$ the element $(f/1) \otimes 1$ in order to define
the homomorphisms $v_{n}$ of (3.7.2)). Conversely, start from a pair $(\mathcal{L}, \phi)$ and form

<!-- original page 74 -->

$r'' = r_{\mathcal{L},\phi}$, then $\mathcal{L}_{r''}$ and $\phi_{r''}$; we show there is a canonical isomorphism
$\tau : \mathcal{L}_{r''} \xrightarrow{\sim} \mathcal{L}$ such that $\phi = \tau \circ \phi_{r''}$. To define it we may
place ourselves in the case $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$ affine, and (with the notation of
(4.2.1) and (3.7.2)) assign to each element $(x/1) \otimes 1$ of $L_{r''}$ (with $x \in E$) the element $v_{1}(x) c$ of
$L$. One verifies at once that $\tau$ does not depend on the chosen generator $c$ of $L$; since $v_{1}$ is surjective by
hypothesis, to prove $\tau$ is an isomorphism it suffices to show that if $x/1 = 0$ in $(S(1))_{(f)}$, then
$v_{1}(x)/1 = 0$ in $B_{g}$; but the first relation says that $f^{n} x = 0$ in $\mathbb{S}_{n+1}(E)$ for some $n$,
whence $v_{n+1}(f^{n} x) = g^{n} v_{1}(x) = 0$ in $B$, whence the conclusion. Finally, it is immediate that for two
equivalent pairs $(\mathcal{L}, \phi)$ and $(\mathcal{L}', \phi')$ we have
$r_{\mathcal{L},\phi} = r_{\mathcal{L}',\phi'}$.

In particular, for $X = Y$:

**Theorem.**

<!-- label: II.4.2.4 -->

The set of $Y$-sections of $\mathbb{P}(\mathcal{E})$ is in canonical bijective correspondence with the set of
quasi-coherent sub-$\mathcal{O}_{Y}$-modules $\mathcal{F}$ of $\mathcal{E}$ such that $\mathcal{E}/\mathcal{F}$ is
invertible.

Note that this property corresponds to the classical definition of "projective space" as the set of hyperplanes of a
vector space (the classical case corresponds to $Y = \operatorname{Spec}(K)$, $K$ a field, and $\mathcal{E} =
\tilde{E}$, $E$ a finite-dimensional $K$-vector space; the $\mathcal{F}$ with the property stated in (4.2.4) then
correspond to the hyperplanes of $E$, and we know on the other hand that the $Y$-sections of $\mathbb{P}(\mathcal{E})$
are then the $K$-rational points of $\mathbb{P}(\mathcal{E})$ `(I, 3.4.5)`).

**Remark.**

<!-- label: II.4.2.5 -->

Since there is a canonical bijective correspondence between $Y$-morphisms from $X$ to $P$ and their graph morphisms, the
$X$-sections of $P \times_{Y} X$ `(I, 3.3.14)`, we see that conversely (4.2.3) can be deduced from (4.2.4). Denote by
$Hyp_{Y}(X, \mathcal{E})$ the set of quasi-coherent sub-$\mathcal{O}_{X}$-modules $\mathcal{F}$ of
$\mathcal{E} \otimes_{Y} \mathcal{O}_{X} = q*(\mathcal{E})$ such that $q*(\mathcal{E})/\mathcal{F}$ is an invertible
$\mathcal{O}_{X}$-module. If $g : X' \to X$ is a $Y$-morphism, the right-exactness of $g*$ gives
$g*(q*(\mathcal{E})/\mathcal{F}) = g*(q*(\mathcal{E}))/g*(\mathcal{F})$, so the latter sheaf is invertible, and
therefore $Hyp_{Y}(X, \mathcal{E})$ is a _contravariant functor_ on the category of $Y$-preschemes. The theorem (4.2.4)
may then be interpreted as defining a _canonical isomorphism_ of functors
$\operatorname{Hom}_{Y}(X, \mathbb{P}(\mathcal{E}))$ and $Hyp_{Y}(X, \mathcal{E})$, contravariant in the variable $X$
over the category of $Y$-preschemes. This also gives a characterization of the projective bundle
$P = \mathbb{P}(\mathcal{E})$ by the following _universal property_, closer to geometric intuition than the
constructions of §§2 and 3: for every morphism $q : X \to Y$ and every invertible $\mathcal{O}_{X}$-module $\mathcal{L}$
that is a quotient of $\mathcal{E} \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{X}$, there exists a unique $Y$-morphism
$r : X \to P$ such that $\mathcal{L} = r*(\mathcal{O}_{P}(1))$.

We shall see later how, in the same way, one may define, among other things, the "Grassmannian" schemes.

**Corollary.**

<!-- label: II.4.2.6 -->

Suppose every invertible $\mathcal{O}_{Y}$-module is trivial `(I, 2.4.8)`. Let $V$ be the group
$\operatorname{Hom}_{\mathcal{O}_{Y}}(\mathcal{E}, \mathcal{O}_{Y})$, regarded as a module over the ring $A = \Gamma(Y,
\mathcal{O}_{Y})$, and let $V*$ be the subset of $V$ formed by the surjective homomorphisms. Then the set of
$Y$-sections of $\mathbb{P}(\mathcal{E})$ is canonically identified with $V*/A*$, where $A*$ is the group of units of
$A$.

<!-- original page 75 -->

In particular:

1. Corollary (4.2.6) applies whenever $Y$ is a _local scheme_ `(I, 2.4.8)`. Let $Y$ be an arbitrary prescheme, $y$ a
   point of $Y$, and $Y' = \operatorname{Spec}(\kappa(y))$; the fibre $p^{-1}(y)$ of $\mathbb{P}(\mathcal{E})$ is, by
   (4.1.3.1), identified with $\mathbb{P}(\mathcal{E}^{y})$, where $\mathcal{E}^{y} = \mathcal{E}_{y}
   \otimes_{\mathcal{O}_{y}} \kappa(y) = \mathcal{E}_{y} / \mathfrak{m}_{y} \mathcal{E}_{y}$ is regarded as a vector
   space over $\kappa(y)$. More generally, if $K$ is an extension of $\kappa(y)$, then $p^{-1}(y) \otimes_{\kappa(y)} K$
   is identified with $\mathbb{P}(\mathcal{E}^{y} \otimes_{\kappa(y)} K)$. Corollary (4.2.6) therefore shows that the
   set of geometric points of $\mathbb{P}(\mathcal{E})$ with values in the extension $K$ of $\kappa(y)$ `(I, 3.4.5)`,
   which one may also call the _rational geometric fibre over $K$ of $\mathbb{P}(\mathcal{E})$ over the point $y$_, is
   identified with the _projective space_ associated to the _dual_ of the $K$-vector space $\mathcal{E}^{y}
   \otimes_{\kappa(y)} K$.
1. Suppose $Y$ is affine of ring $A$, and that every invertible $\mathcal{O}_{Y}$-module is trivial; take in addition
   $\mathcal{E} = \mathcal{O}^{n}_{Y}$. Then in (4.2.6), $V$ is identified with $A^{n}$ `(I, 1.3.8)`, and $V*$ with the
   set of systems $(f_{i})_{1\leq i\leq n}$ of elements of $A$ generating the ideal $A$; two such systems define the
   same $Y$-section of $\mathbb{P}^{n-1}_{Y} = \mathbb{P}^{n-1}_{A}$ — in other words, the same _point of
   $\mathbb{P}^{n-1}_{A}$ with values in $A$_ — if and only if one is obtained from the other by multiplication by an
   invertible element of $A$.

These properties justify the terminology "projective bundle" for $\mathbb{P}(\mathcal{E})$. Note that the definition of
"projective space" so obtained is in fact _dual_ to the classical definition; this is forced upon us by the need to
define $\mathbb{P}(\mathcal{E})$ for an _arbitrary_ quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{E}$, not
necessarily locally free.

**Remark.**

<!-- label: II.4.2.7 -->

We shall see in Chapter V that, if $Y$ is locally Noetherian and connected and $\mathcal{E}$ is locally free, then,
setting $P = \mathbb{P}(\mathcal{E})$, every invertible $\mathcal{O}_{P}$-module $\mathcal{L}$ is isomorphic to one of
the form $\mathcal{L}' \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{P}(m)$, where $\mathcal{L}'$ is an invertible
$\mathcal{O}_{Y}$-module, well-determined up to isomorphism, and $m$ is a well-determined integer. In other words,
$H^{1}(P, \mathcal{O}_{P}*)$ is isomorphic to $\mathbb{Z} \times H^{1}(Y, \mathcal{O}_{Y}*)$ `(0, 5.4.7)`. We shall also
see `(III, 2.1.14, taking (0, 5.4.10) into account)` that $p_{*}(\mathcal{L}^{\otimes m}) = 0$ for $m < 0$ and
$p_{*}(\mathcal{L}^{\otimes m})$ is isomorphic to $\mathcal{L}' \otimes_{\mathcal{O}_{Y}}
(\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}))_{m}$ for $m \geq 0$. If $\mathcal{F}$ is a quasi-coherent
$\mathcal{O}_{Y}$-module, every $Y$-morphism $\mathbb{P}(\mathcal{F}) \to \mathbb{P}(\mathcal{E})$ is therefore
determined by the data of an invertible $\mathcal{O}_{Y}$-module $\mathcal{L}'$, an integer $m \geq 0$, and an
$\mathcal{O}_{Y}$-homomorphism $\psi : \mathcal{F} \to \mathcal{L}' \otimes_{\mathcal{O}_{Y}}
(\mathbb{S}_{\mathcal{O}_{Y}}(\mathcal{E}))_{m}$ such that the corresponding homomorphism $\psi\sharp$ of
$\mathcal{O}_{\mathbb{P}(\mathcal{F})}$-modules is surjective. We shall also see that if the $Y$-morphism in question is
an isomorphism, then $m = 1$ and $\mathcal{F}$ is isomorphic to $\mathcal{E} \otimes_{\mathcal{O}_{Y}} \mathcal{L}'$
(the converse of (4.1.4)). This will let us determine the sheaf of germs of automorphisms of $\mathbb{P}(\mathcal{E})$
as the quotient of the sheaf of groups $\operatorname{Aut}(\mathcal{E})$ (which is locally isomorphic to $GL(n,
\mathcal{O}_{Y})$ if $\mathcal{E}$ is of rank $n$) by $\mathcal{O}_{Y}*$.

**(4.2.8)**

<!-- label: II.4.2.8 -->

Keeping the notation of (4.2.1), let $u : X' \to X$ be a morphism; if the $Y$-morphism $r : X \to P$ corresponds to the
homomorphism $\phi : q*(\mathcal{E}) \to \mathcal{L}$, then the $Y$-morphism $r \circ u$ corresponds to $u*(\phi) :
u*(q*(\mathcal{E})) \to u*(\mathcal{L})$, as follows immediately from the definitions.

**(4.2.9)**

<!-- label: II.4.2.9 -->

Let $\mathcal{E}$, $\mathcal{F}$ be two quasi-coherent $\mathcal{O}_{Y}$-modules, $v : \mathcal{E} \to \mathcal{F}$ a
surjective homomorphism, and $j = \mathbb{P}(v)$ the corresponding closed immersion $\mathbb{P}(\mathcal{F}) \to
\mathbb{P}(\mathcal{E})$ (4.1.2). If the $Y$-morphism $r : X \to \mathbb{P}(\mathcal{F})$ corresponds to the
homomorphism $\phi : q*(\mathcal{F}) \to \mathcal{L}$, then the

<!-- original page 76 -->

$Y$-morphism $j \circ r$ corresponds to $q*(\mathcal{E}) \xrightarrow{q*(v)} q*(\mathcal{F}) \xrightarrow{\phi}
\mathcal{L}$; this again follows from the definition given in (4.2.1).

**(4.2.10)**

<!-- label: II.4.2.10 -->

Let $\psi : Y' \to Y$ be a morphism, and set $\mathcal{E}' = \psi*(\mathcal{E})$. If the $Y$-morphism $r : X \to P$
corresponds to the homomorphism $\phi : q*(\mathcal{E}) \to \mathcal{L}$, then the $Y'$-morphism

```text
  r_{(Y')} : X_{(Y')} → P' = ℙ(𝓔')
```

corresponds to $\phi_{(Y')} : q_{(Y')}*(\mathcal{E}') = q*(\mathcal{E}) \otimes_{Y} \mathcal{O}_{Y'} \to \mathcal{L}
\otimes_{Y} \mathcal{O}_{Y'}$. Indeed, by (4.1.3.1) we have the commutative diagram

```text
   Y' ←─── P' = P_{(Y')} ←─── X_{(Y')}
   │           │                │
   │           │ u              │ v
   ↓           ↓                ↓
   Y  ←─── P            ←─── X
              p              r
```

By (4.1.3.2),

```text
  (r_{(Y')})*(𝒪_{P'}(1)) = (r_{(Y')})*(u*(𝒪_P(1))) = v*(r*(𝒪_P(1)))
                         = v*(ℒ) = ℒ ⊗_Y 𝒪_{Y'};
```

on the other hand, $u*(\alpha_{1}\sharp)$ is precisely the canonical homomorphism $\alpha_{1}\sharp :
(p_{(Y')})*(\mathcal{E}') \to \mathcal{O}_{P'}(1)$, as one sees by making the canonical homomorphisms $\alpha_{1}\sharp$
for $P$ and $P'$ explicit as in (4.1.6). Whence our assertion.

## 4.3. The Segre morphism

**(4.3.1)**

<!-- label: II.4.3.1 -->

Let $Y$ be a prescheme and $\mathcal{E}$, $\mathcal{F}$ two quasi-coherent $\mathcal{O}_{Y}$-modules; set $P_{1} =
\mathbb{P}(\mathcal{E})$, $P_{2} = \mathbb{P}(\mathcal{F})$, and let $p_{1} : P_{1} \to Y$, $p_{2} : P_{2} \to Y$ be the
structure morphisms. Let $Q = P_{1} \times_{Y} P_{2}$, and let $q_{1} : Q \to P_{1}$, $q_{2} : Q \to P_{2}$ be the
canonical projections; the $\mathcal{O}_{Q}$-module $\mathcal{L} = \mathcal{O}_{P_{1}}(1) \otimes_{Y}
\mathcal{O}_{P_{2}}(1) = q_{1}*(\mathcal{O}_{P_{1}}(1)) \otimes_{\mathcal{O}_{Q}} q_{2}*(\mathcal{O}_{P_{2}}(1))$ is
invertible, as the tensor product of two invertible $\mathcal{O}_{Q}$-modules `(0, 5.4.4)`. On the other hand, if $r =
p_{1} \circ q_{1} = p_{2} \circ q_{2}$ is the structure morphism $Q \to Y$, then $r*(\mathcal{E}
\otimes_{\mathcal{O}_{Y}} \mathcal{F}) = q_{1}*(p_{1}*(\mathcal{E})) \otimes_{\mathcal{O}_{Q}}
q_{2}*(p_{2}*(\mathcal{F}))$ `(0, 4.3.3)`. The canonical surjective homomorphisms (4.1.5.1) $p_{1}*(\mathcal{E}) \to
\mathcal{O}_{P_{1}}(1)$ and $p_{2}*(\mathcal{F}) \to \mathcal{O}_{P_{2}}(1)$ therefore yield, by tensor product, a
canonical homomorphism

```text
  s : r*(𝓔 ⊗_{𝒪_Y} 𝓕) → ℒ                                                   (4.3.1.1)
```

which is evidently surjective; from this we obtain (4.2.2) a canonical morphism, called the _Segre morphism_:

```text
  ς : ℙ(𝓔) ×_Y ℙ(𝓕) → ℙ(𝓔 ⊗_{𝒪_Y} 𝓕).                                       (4.3.1.2)
```

Let us make $\varsigma$ explicit when $Y = \operatorname{Spec}(A)$ is affine, $\mathcal{E} = \tilde{E}$, $\mathcal{F} =
\tilde{F}$, with $E$, $F$ two $A$-modules, so that $\mathcal{E} \otimes_{\mathcal{O}_{Y}} \mathcal{F} = (E \otimes_{A}
F)~$ `(I, 1.3.12)`; set $R = \mathbb{S}_{A}(E)$, $S = \mathbb{S}_{A}(F)$, $T = \mathbb{S}_{A}(E \otimes_{A} F)$. Let $f
\in E$, $g \in F$, and consider the affine open

```text
  D₊(f) ×_Y D₊(g) = Spec(B)
```

<!-- original page 77 -->

of $Q$, where $B = R_{(f)} \otimes_{A} S_{(g)}$; the restriction of $\mathcal{L}$ to this affine open is $\tilde{L}$,
where

```text
  L = (R(1))_{(f)} ⊗_A (S(1))_{(g)},
```

and the element $c = (f/1) \otimes (g/1)$ is a generator of $L$, regarded as a free $B$-module (2.5.7). The homomorphism
(4.3.1.1) corresponds to the homomorphism

```text
  (x ⊗ y) ⊗ b ↦ b ((x/1) ⊗ (y/1))
```

from $(E \otimes_{A} F) \otimes_{A} B$ to $L$. With the notation of (3.7.2) we therefore have $v_{1}(x \otimes y) =
(x/f) \otimes (y/g)$; the restriction of $\varsigma$ to $D_{+}(f) \times_{Y} D_{+}(g)$ is a morphism of this affine
scheme to $D_{+}(f \otimes g)$, corresponding to the ring homomorphism $\omega : T_{(f\otimes g)} \to R_{(f)}
\otimes_{A} S_{(g)}$ defined by

```text
  ω((x ⊗ y)/(f ⊗ g)) = (x/f) ⊗ (y/g)                                       (4.3.1.3)
```

for $x \in E$ and $y \in F$.

**(4.3.2)**

<!-- label: II.4.3.2 -->

It follows from (4.2.3) that we have a canonical isomorphism

```text
  τ : ς*(𝒪_P(1)) ⥲ 𝒪_{P_1}(1) ⊗_Y 𝒪_{P_2}(1)                              (4.3.2.1)
```

where we have set $P = \mathbb{P}(\mathcal{E} \otimes_{\mathcal{O}_{Y}} \mathcal{F})$. We show that, for $x \in
\Gamma(Y, \mathcal{E})$ and $y \in \Gamma(Y, \mathcal{F})$,

```text
  τ(α_1(x ⊗ y)) = α_1(x) ⊗ α_1(y).                                         (4.3.2.2)
```

Indeed, we reduce to the case $Y$ affine, and we then have, with the notation of (4.3.1) and (2.6.2), $\alpha^{f\otimes
g}_{1}(x \otimes y) = (x \otimes y)/1$ in $(T(1))_{(f\otimes g)}$, $\alpha^{f}_{1}(x) = x/1$ in $(R(1))_{(f)}$, and
$\alpha^{g}_{1}(y) = y/1$ in $(S(1))_{(g)}$. The definition of $\tau$ given in (4.2.3) and the computation of $v_{1}$
done in (4.3.1) prove (4.3.2.2) at once. From this we derive

```text
  ς⁻¹(P_{x⊗y}) = (P_1)_x ×_Y (P_2)_y                                        (4.3.2.3)
```

with the notation of (3.1.4). Indeed, taking (3.3.3) into account, the formula (4.3.2.2) reduces (returning to the
affine case via `(I, 3.2.7)` and `(I, 3.2.3)`) to proving the following lemma:

**Lemma.**

<!-- label: II.4.3.2.4 -->

Let $B$, $B'$ be two $A$-algebras, and set $Y = \operatorname{Spec}(A)$, $Z = \operatorname{Spec}(B)$, $Z' =
\operatorname{Spec}(B')$. For any $t \in B$ and $t' \in B'$, we have $D(t \otimes t') = D(t) \times_{Y} D(t')$.

**Proof.** If $p : Z \times_{Y} Z' \to Z$ and $p' : Z \times_{Y} Z' \to Z'$ are the canonical projections, it follows
from `(I, 1.2.2.2)` that $p^{-1}(D(t)) = D(t \otimes 1)$ and $p'^{-1}(D(t')) = D(1 \otimes t')$; the conclusion follows
from `(I, 3.2.7)` and `(I, 1.1.9.1)`, since $(t \otimes 1)(1 \otimes t') = t \otimes t'$.

**Proposition.**

<!-- label: II.4.3.3 -->

The Segre morphism is a closed immersion.

**Proof.** The question being local on $Y$, we reduce to the case where $Y$ is affine. With the notation of (4.3.1) and
(4.3.2), the $D_{+}(f \otimes g)$ form a basis for the topology of $P$, since the $f \otimes g$ generate $T$ when $f$
ranges over $E$ and $g$ over $F$. On the other hand, by (4.3.2.3), $\varsigma^{-1}(D_{+}(f \otimes g)) = D_{+}(f)
\times_{Y} D_{+}(g)$. It thus suffices `(I, 4.2.4)` to prove that the restriction of $\varsigma$ to $D_{+}(f) \times_{Y}
D_{+}(g)$ is a closed immersion into $D_{+}(f \otimes g)$. But, with the same notation, formula (4.3.1.3) shows that
$\omega$ is surjective, which completes the proof.

**(4.3.4)**

<!-- label: II.4.3.4 -->

The Segre morphism is functorial in $\mathcal{E}$ and $\mathcal{F}$, when one restricts the

<!-- original page 78 -->

homomorphisms of quasi-coherent $\mathcal{O}_{Y}$-modules to surjective homomorphisms. Indeed, we must show that if
$\mathcal{E} \to \mathcal{E}'$ is a surjective $\mathcal{O}_{Y}$-homomorphism, then the diagram

```text
                       j × 1
   ℙ(𝓔') × ℙ(𝓕) ─────────────→ ℙ(𝓔) × ℙ(𝓕)

         │                          │
       ς │                          │ ς
         ↓                          ↓

   ℙ(𝓔' ⊗ 𝓕) ────────────────→ ℙ(𝓔 ⊗ 𝓕)
```

commutes, $j$ denoting the canonical closed immersion $\mathbb{P}(\mathcal{E}') \to \mathbb{P}(\mathcal{E})$. Set
$P_{1}' = \mathbb{P}(\mathcal{E}')$ and keep the other notation of (4.3.1); $j \times 1$ is a closed immersion
`(I, 4.3.1)`, and up to isomorphism

$$ (j \times 1)*(\mathcal{O}_{P_{1}}(1) \otimes \mathcal{O}_{P_{2}}(1)) = j*(\mathcal{O}_{P_{1}}(1)) \otimes
\mathcal{O}_{P_{2}}(1) = \mathcal{O}_{P_{1}'}(1) \otimes \mathcal{O}_{P_{2}}(1) $$

by (4.1.2.1) and `(I, 9.1.5)`; our assertion therefore follows from (4.2.8) and (4.2.9).

**(4.3.5)**

<!-- label: II.4.3.5 -->

With the notation of (4.3.1), let $\psi : Y' \to Y$ be a morphism, and set $\mathcal{E}' = \psi*(\mathcal{E})$,
$\mathcal{F}' = \psi*(\mathcal{F})$. Then the Segre morphism $\mathbb{P}(\mathcal{E}') \times \mathbb{P}(\mathcal{F}')
\to \mathbb{P}(\mathcal{E}' \otimes \mathcal{F}')$ is identified with $\varsigma_{(Y')}$. Indeed, keeping the notation
of (4.3.1), set in addition $P_{1}' = \mathbb{P}(\mathcal{E}')$, $P_{2}' = \mathbb{P}(\mathcal{F}')$; we know (4.1.3.1)
that $P_{i}'$ is identified with $(P_{i})_{(Y')}$ ($i = 1, 2$), so the structure morphism $P_{1}' \times P_{2}' \to Y'$
is identified with $r_{(Y')}$. On the other hand, $\mathcal{E}' \otimes \mathcal{F}'$ is identified with
$\psi*(\mathcal{E} \otimes \mathcal{F})$, so $\mathbb{P}(\mathcal{E}' \otimes \mathcal{F}')$ is identified with
$(\mathbb{P}(\mathcal{E} \otimes \mathcal{F}))_{(Y')}$ (4.1.3.1). Finally, $\mathcal{O}_{P_{1}'}(1) \otimes_{Y'}
\mathcal{O}_{P_{2}'}(1) = \mathcal{L}'$ is identified with $\mathcal{L} \otimes_{Y} \mathcal{O}_{Y'}$, by (4.1.3.2) and
`(I, 9.1.11)`. The canonical homomorphism $(r_{(Y')})*(\mathcal{E}' \otimes \mathcal{F}') \to \mathcal{L}'$ is then
identified with $s_{(Y')}$, and our assertion follows from (4.2.10).

**Remark.**

<!-- label: II.4.3.6 -->

The prescheme given by the disjoint sum of $\mathbb{P}(\mathcal{E})$ and $\mathbb{P}(\mathcal{F})$ is likewise
canonically isomorphic to a _closed subprescheme of $\mathbb{P}(\mathcal{E} \oplus \mathcal{F})$_. Indeed, the
surjective homomorphisms $\mathcal{E} \oplus \mathcal{F} \to \mathcal{E}$ and $\mathcal{E} \oplus \mathcal{F} \to
\mathcal{F}$ correspond to closed immersions $\mathbb{P}(\mathcal{E}) \to \mathbb{P}(\mathcal{E} \oplus \mathcal{F})$
and $\mathbb{P}(\mathcal{F}) \to \mathbb{P}(\mathcal{E} \oplus \mathcal{F})$; everything comes down to showing that the
underlying spaces of the closed subpreschemes of $\mathbb{P}(\mathcal{E} \oplus \mathcal{F})$ so obtained have no point
in common. The question being local on $Y$, we may adopt the notation of (4.3.1); now $\mathbb{S}_{n}(E)$ and
$\mathbb{S}_{n}(F)$ are identified with submodules of $\mathbb{S}_{n}(E \oplus F)$ whose intersection reduces to `0`;
and if $\mathfrak{p}$ is a graded prime ideal of $\mathbb{S}(E)$ such that $\mathfrak{p} \cap \mathbb{S}_{n}(E) \neq
\mathbb{S}_{n}(E)$ for every $n \geq 0$, then it corresponds in $\mathbb{S}(E \oplus F)$ to a graded prime ideal whose
trace on $\mathbb{S}_{n}(E)$ is $\mathfrak{p} \cap \mathbb{S}_{n}(E)$, but which _contains_ $\mathbb{S}_{+}(F)$, as one
sees at once. Hence two points of $\operatorname{Proj}(\mathbb{S}(E))$ and $\operatorname{Proj}(\mathbb{S}(F))$
respectively cannot have the same image in $\operatorname{Proj}(\mathbb{S}(E \oplus F))$.

## 4.4. Immersions into projective bundles. Very ample sheaves

**Proposition.**

<!-- label: II.4.4.1 -->

Let $Y$ be a quasi-compact scheme or a prescheme whose underlying space is Noetherian, $q : X \to Y$ a morphism _of
finite type_, and $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module.

1. Let $\mathcal{S}$ be a quasi-coherent graded $\mathcal{O}_{Y}$-algebra with positive degrees, and $\psi :
   q*(\mathcal{S}) \to \oplus_{n\geq 0} \mathcal{L}^{\otimes n}$ a homomorphism of graded algebras. For
   $r_{\mathcal{L},\psi}$ to be everywhere defined and an immersion, it is necessary

<!-- original page 79 -->

```
and sufficient that there exist an integer `n ≥ 0` and a quasi-coherent
sub-`𝒪_Y`-module `𝓔` of `𝒮_n` _of finite type_ such that the
homomorphism
`φ' = ψ_n ∘ q*(j) : q*(𝓔) → ℒ^{⊗n} = ℒ'`
(with `j` the injection `𝓔 → 𝒮_n`) is surjective and the morphism
`r_{ℒ',φ'} : X → ℙ(𝓔)` is an immersion.
```

1. Let $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{Y}$-module, and $\phi : q*(\mathcal{F}) \to \mathcal{L}$ a
   surjective homomorphism. For the morphism $r_{\mathcal{L},\phi}$ to be an immersion $X \to \mathbb{P}(\mathcal{F})$,
   it is necessary and sufficient that there exist a quasi-coherent sub-$\mathcal{O}_{Y}$-module $\mathcal{E}$ of
   $\mathcal{F}$ _of finite type_ such that the homomorphism $\phi' = \phi \circ q*(j) : q*(\mathcal{E}) \to
   \mathcal{L}$ (with $j : \mathcal{E} \to \mathcal{F}$ the canonical injection) is surjective and
   $r_{\mathcal{L},\phi'} : X \to \mathbb{P}(\mathcal{E})$ is an immersion.

**Proof.**

(i) The fact that $r_{\mathcal{L},\psi}$ is everywhere defined and an immersion is equivalent, by (3.8.5), to the
existence of an $n \geq 0$ and an $\mathcal{E}$ such that, if $\mathcal{S}'$ is the sub-algebra of $\mathcal{S}$
generated by $\mathcal{E}$, the homomorphism $q*(\mathcal{E}) \to \mathcal{L}^{\otimes n}$ is surjective and
$r_{\mathcal{L},\psi'} : X \to \operatorname{Proj}(\mathcal{S}')$ is everywhere defined and an immersion. We have on the
other hand a canonical surjective homomorphism $\mathbb{S}(\mathcal{E}) \to \mathcal{S}'$, to which corresponds a closed
immersion $\operatorname{Proj}(\mathcal{S}') \to \mathbb{P}(\mathcal{E})$ (3.6.2); whence the conclusion.

(ii) Since $\mathcal{F}$ is the direct limit of its quasi-coherent submodules of finite type $\mathcal{E}_{\lambda}$
`(I, 9.4.9)`, $\mathbb{S}(\mathcal{F})$ is the direct limit of the $\mathbb{S}(\mathcal{E}_{\lambda})$; the conclusion
follows from (3.8.4), upon observing that in the proof of (3.8.4) one may take all the $n_{i}$ equal to `1`: indeed
(assuming $Y$ affine), if $r = r_{\mathcal{L},\phi}$ is an immersion, then $r(X)$ is a quasi-compact subspace of
$\mathbb{P}(\mathcal{F})$ that may be covered by finitely many open subsets of $\mathbb{P}(\mathcal{F})$ of the form
$D_{+}(f)$ with $f \in F$, such that $D_{+}(f) \cap r(X)$ is closed.

**Definition.**

<!-- label: II.4.4.2 -->

Let $Y$ be a prescheme, $q : X \to Y$ a morphism. We say that an invertible $\mathcal{O}_{X}$-module $\mathcal{L}$ is
_very ample for $q$_ (or _very ample for $Y$_, or simply _very ample_ if no confusion results) if there exists a
quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{E}$ and a $Y$-immersion $i$ of $X$ into $P = \mathbb{P}(\mathcal{E})$
such that $\mathcal{L}$ is isomorphic to $i*(\mathcal{O}_{P}(1))$.

It is equivalent (4.2.3) to say that there exists a quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{E}$ and a
surjective homomorphism $\phi : q*(\mathcal{E}) \to \mathcal{L}$ such that $r_{\mathcal{L},\phi} : X \to
\mathbb{P}(\mathcal{E})$ is an _immersion_.

Note that the existence of a very-ample-for-$Y$ $\mathcal{O}_{X}$-module implies that $q$ is _separated_ ((3.1.3) and
`(I, 5.5.1, (i) and (ii))`).

**Corollary.**

<!-- label: II.4.4.3 -->

Suppose there exists a quasi-coherent graded $\mathcal{O}_{Y}$-algebra $\mathcal{S}$ generated by $\mathcal{S}_{1}$ and
a $Y$-immersion $i : X \to P = \operatorname{Proj}(\mathcal{S})$ such that $\mathcal{L}$ is isomorphic to
$i*(\mathcal{O}_{P}(1))$; then $\mathcal{L}$ is very ample relative to $q$.

**Proof.** If $\mathcal{F} = \mathcal{S}_{1}$, the canonical homomorphism $\mathbb{S}(\mathcal{F}) \to \mathcal{S}$ is
surjective; composing the corresponding closed immersion $\operatorname{Proj}(\mathcal{S}) \to \mathbb{P}(\mathcal{F})$
(3.6.2) with the immersion $i$, we obtain an immersion $j : X \to \mathbb{P}(\mathcal{F}) = P'$ such that $\mathcal{L}$
is isomorphic to $j*(\mathcal{O}_{P'}(1))$ (3.6.3).

**Proposition.**

<!-- label: II.4.4.4 -->

Let $q : X \to Y$ be a quasi-compact morphism, and $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module. The following
properties are equivalent:

a) $\mathcal{L}$ is very ample relative to $q$. b) $q_{*}(\mathcal{L})$ is quasi-coherent, the canonical homomorphism
$\sigma : q*(q_{*}(\mathcal{L})) \to \mathcal{L}$ is surjective, and the morphism $r_{\mathcal{L},\sigma} : X \to
\mathbb{P}(q_{*}(\mathcal{L}))$ is an immersion.

**Proof.** Since $q$ is quasi-compact, we know $q_{*}(\mathcal{L})$ is quasi-coherent when $q$ is separated
`(I, 9.2.2)`.

<!-- original page 80 -->

We know (3.4.7) that the existence of a surjective homomorphism $\phi : q*(\mathcal{E}) \to \mathcal{L}$ (with
$\mathcal{E}$ a quasi-coherent $\mathcal{O}_{Y}$-module) implies that $\sigma$ is surjective; moreover, to the
factorization $q*(\mathcal{E}) \to q*(q_{*}(\mathcal{L})) \xrightarrow{\sigma} \mathcal{L}$ of $\phi$ corresponds
canonically a factorization

```text
  q*(𝕊(𝓔)) → q*(𝕊(q_*(ℒ))) → ⊕_{n≥0} ℒ^{⊗n}
```

so (3.8.3) the hypothesis that $r_{\mathcal{L},\phi}$ is an immersion implies that so is $j = r_{\mathcal{L},\sigma}$;
moreover (4.2.4), $\mathcal{L}$ is isomorphic to $j*(\mathcal{O}_{P'}(1))$ with $P' = \mathbb{P}(q_{*}(\mathcal{L}))$.
Thus (a) and (b) are equivalent.

**Corollary.**

<!-- label: II.4.4.5 -->

Suppose $q$ is quasi-compact. For $\mathcal{L}$ to be very ample relative to $Y$, it is necessary and sufficient that
there exist an open cover $(U_{\alpha})$ of $Y$ such that $\mathcal{L} | q^{-1}(U_{\alpha})$ is very ample relative to
$U_{\alpha}$ for every $\alpha$.

**Proof.** Indeed, condition (b) of (4.4.4) is local on $Y$.

**Proposition.**

<!-- label: II.4.4.6 -->

Let $Y$ be a quasi-compact scheme or a prescheme whose underlying space is Noetherian, $q : X \to Y$ a morphism _of
finite type_, and $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module. Then conditions (a) and (b) of (4.4.4) are
equivalent to the following:

a') There exists a quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{E}$ _of finite type_ and a surjective homomorphism
$\phi : q*(\mathcal{E}) \to \mathcal{L}$ such that $r_{\mathcal{L},\phi}$ is an immersion. b') There exists a coherent
sub-$\mathcal{O}_{Y}$-module $\mathcal{E}$ of $q_{*}(\mathcal{L})$ _of finite type_ with the properties stated in (a').

**Proof.** It is clear that (a') or (b') implies (a); on the other hand, (a) implies (a') by (4.4.1), and similarly (b)
implies (b').

**Corollary.**

<!-- label: II.4.4.7 -->

Suppose $Y$ is a quasi-compact scheme or a Noetherian prescheme. If $\mathcal{L}$ is very ample for $q$, then there
exists a quasi-coherent graded $\mathcal{O}_{Y}$-algebra $\mathcal{S}$ such that $\mathcal{S}_{1}$ is of finite type and
generates $\mathcal{S}$, and a dominant open $Y$-immersion $i : X \to P = \operatorname{Proj}(\mathcal{S})$ such that
$\mathcal{L}$ is isomorphic to $i*(\mathcal{O}_{P}(1))$.

**Proof.** Condition (b') of (4.4.6) is satisfied; the structure morphism $p : \mathbb{P}(\mathcal{E}) = P' \to Y$ is
then separated and of finite type (3.1.3), so $P'$ is a quasi-compact scheme (resp. a Noetherian prescheme) if $Y$ is
one. Let $Z$ be the closure `(I, 9.5.11)` of the subprescheme $X'$ of $P'$ associated to the immersion $j =
r_{\mathcal{L},\phi}$ of $X$ into $P'$; it is clear that $j$ factors as the canonical injection $Z \to P'$ followed by a
dominant open immersion $i : X \to Z$. But $Z$ is identified with a prescheme $\operatorname{Proj}(\mathcal{S})$, where
$\mathcal{S}$ is a graded $\mathcal{O}_{Y}$-algebra quotient of $\mathbb{S}(\mathcal{E})$ by a quasi-coherent graded
sheaf of ideals (3.6.2); it is clear that $\mathcal{S}_{1}$ is of finite type and generates $\mathcal{S}$. Moreover,
$\mathcal{O}_{Z}(1)$ is the inverse image of $\mathcal{O}_{P'}(1)$ under the canonical injection (3.6.3), so
$\mathcal{L} = i*(\mathcal{O}_{Z}(1))$.

**Proposition.**

<!-- label: II.4.4.8 -->

Let $q : X \to Y$ be a morphism, $\mathcal{L}$ a very-ample-relative-to-$q$ $\mathcal{O}_{X}$-module, and $\mathcal{L}'$
an invertible $\mathcal{O}_{X}$-module such that there exist a quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{E}'$
and a surjective homomorphism $q*(\mathcal{E}') \to \mathcal{L}'$. Then $\mathcal{L} \otimes_{\mathcal{O}_{X}}
\mathcal{L}'$ is very ample relative to $q$.

**Proof.** The hypothesis implies the existence of a $Y$-morphism $r' : X \to P' = \mathbb{P}(\mathcal{E}')$ such that
$\mathcal{L}' = r'*(\mathcal{O}_{P'}(1))$ (4.2.1). By hypothesis there is also a quasi-coherent $\mathcal{O}_{Y}$-module
$\mathcal{E}$ and a

<!-- original page 81 -->

$Y$-immersion $r : X \to P = \mathbb{P}(\mathcal{E})$ such that $\mathcal{L} = r*(\mathcal{O}_{P}(1))$. Set $Q =
\mathbb{P}(\mathcal{E} \otimes \mathcal{E}')$ and consider the Segre morphism $\varsigma : P \times_{Y} P' \to Q$
(4.3.1). Since $r$ is an immersion, so is $(r, r')_{Y} : X \to P \times_{Y} P'$ `(I, 5.3.14)`; but $\varsigma$ is an
immersion (4.3.3), so $r'' : X \xrightarrow{(r,r')} P \times_{Y} P' \xrightarrow{\varsigma} Q$ is too. On the other hand
(4.3.2.1), $\varsigma*(\mathcal{O}_{Q}(1))$ is isomorphic to $\mathcal{O}_{P}(1) \otimes_{Y} \mathcal{O}_{P'}(1)$, so
`(I, 9.1.4)` $r''*(\mathcal{O}_{Q}(1))$ is isomorphic to $\mathcal{L} \otimes \mathcal{L}'$, which proves the
proposition.

**Corollary.**

<!-- label: II.4.4.9 -->

Let $q : X \to Y$ be a morphism.

1. Let $\mathcal{L}$ be an invertible $\mathcal{O}_{X}$-module and $\mathcal{K}$ an invertible $\mathcal{O}_{Y}$-module.
   For $\mathcal{L}$ to be very ample relative to $q$, it is necessary and sufficient that $\mathcal{L} \otimes
   q*(\mathcal{K})$ be so.
1. If $\mathcal{L}$ and $\mathcal{L}'$ are two $\mathcal{O}_{X}$-modules very ample relative to $q$, then so is
   $\mathcal{L} \otimes \mathcal{L}'$; in particular, $\mathcal{L}^{\otimes n}$ is very ample relative to $q$ for every
   $n > 0$.

**Proof.** (ii) is an immediate consequence of (4.4.8), as is the necessity of (i); on the other hand, if $\mathcal{L}
\otimes q*(\mathcal{K})$ is very ample, so is $(\mathcal{L} \otimes q*(\mathcal{K})) \otimes q*(\mathcal{K}^{-1})$ by
the above, and this latter $\mathcal{O}_{X}$-module is isomorphic to $\mathcal{L}$ `(0, 5.4.3 and 5.4.5)`.

**Proposition.**

<!-- label: II.4.4.10 -->

1. For every prescheme $Y$, every invertible $\mathcal{O}_{Y}$-module $\mathcal{L}$ is very ample relative to the
   identity morphism `1_Y`.
1. (i bis) Let $f : X \to Y$ be a morphism and $j : X' \to X$ an immersion. If $\mathcal{L}$ is an
   $\mathcal{O}_{X}$-module very ample relative to $f$, then $j*(\mathcal{L})$ is very ample relative to $f \circ j$.
1. Let $Z$ be a quasi-compact prescheme, $f : X \to Y$ a morphism of finite type, $g : Y \to Z$ a quasi-compact
   morphism, $\mathcal{L}$ an $\mathcal{O}_{X}$-module very ample relative to $f$, and $\mathcal{K}$ an
   $\mathcal{O}_{Y}$-module very ample relative to $g$. Then there exists an integer $n_{0} > 0$ such that $\mathcal{L}
   \otimes f*(\mathcal{K}^{\otimes n})$ is very ample relative to $g \circ f$ for all $n \geq n_{0}$.
1. Let $f : X \to Y$ and $g : Y' \to Y$ be morphisms, and set $X' = X_{(Y')}$. If $\mathcal{L}$ is an
   $\mathcal{O}_{X}$-module very ample relative to $f$, then $\mathcal{L}' = \mathcal{L} \otimes_{Y} \mathcal{O}_{Y'}$
   is an $\mathcal{O}_{X'}$-module very ample relative to $f_{(Y')}$.
1. Let $f_{i} : X_{i} \to Y_{i}$ ($i = 1, 2$) be two $S$-morphisms. If $\mathcal{L}_{i}$ is an
   $\mathcal{O}_{X_{i}}$-module very ample relative to $f_{i}$ ($i = 1, 2$), then $\mathcal{L}_{1} \otimes_{S}
   \mathcal{L}_{2}$ is very ample relative to $f_{1} \times_{S} f_{2}$.
1. Let $f : X \to Y$ and $g : Y \to Z$ be morphisms. If an $\mathcal{O}_{X}$-module $\mathcal{L}$ is very ample relative
   to $g \circ f$, then $\mathcal{L}$ is very ample relative to $f$.
1. Let $f : X \to Y$ be a morphism, and $j$ the canonical injection $X_{red} \to X$. If $\mathcal{L}$ is an
   $\mathcal{O}_{X}$-module very ample relative to $f$, then $j*(\mathcal{L})$ is very ample relative to $f_{red}$.

**Proof.** Property (i bis) follows immediately from Definition (4.4.2), and it is immediate that (vi) follows formally
from (i bis) and (v) by an argument modeled on `(I, 5.5.12)`, which we leave to the reader. To prove (v), consider, as
in `(I, 5.5.12)`, the factorization $X \xrightarrow{\Gamma_{f}} X \times_{Z} Y \xrightarrow{p_{2}} Y$, noting that
$p_{2} = (g \circ f) \times 1_{Y}$. It follows from the hypothesis and from (i) and (iv) that $\mathcal{L}
\otimes_{\mathcal{O}_{Z}} \mathcal{O}_{Y}$ is very ample for $p_{2}$; on the other hand, $\mathcal{L} =
\Gamma_{f}*(\mathcal{L} \otimes_{\mathcal{O}_{Z}} \mathcal{O}_{Y})$ `(I, 9.1.4)`, and $\Gamma_{f}$ is an immersion
`(I, 5.3.11)`; we may therefore apply (i bis).

<!-- original page 82 -->

To prove (i), we apply Definition (4.4.2) with $\mathcal{E} = \mathcal{L}$, noting that then $\mathbb{P}(\mathcal{E})$
is identified with $Y$ (4.1.4).

Let us prove (iii). There exists a quasi-coherent $\mathcal{O}_{Y}$-module $\mathcal{E}$ and a $Y$-immersion $i : X \to
\mathbb{P}(\mathcal{E}) = P$ such that $\mathcal{L} = i*(\mathcal{O}_{P}(1))$; setting $\mathcal{E}' = g*(\mathcal{E})$,
$\mathcal{E}'$ is a quasi-coherent $\mathcal{O}_{Y'}$-module, and $P' = \mathbb{P}(\mathcal{E}') = P_{(Y')}$ (4.1.3.1);
$i_{(Y')}$ is an immersion of $X_{(Y')}$ into $P'$ `(I, 4.3.2)`, and $\mathcal{L}'$ is isomorphic to
$(i_{(Y')})*(\mathcal{O}_{P'}(1))$ (4.2.10).

To prove (iv), note that by hypothesis there is a $Y_{i}$-immersion $r_{i} : X_{i} \to P_{i} =
\mathbb{P}(\mathcal{E}_{i})$, where $\mathcal{E}_{i}$ is a quasi-coherent $\mathcal{O}_{Y_{i}}$-module, and
$\mathcal{L}_{i} = r_{i}*(\mathcal{O}_{P_{i}}(1))$ ($i = 1, 2$); $r_{1} \times_{S} r_{2}$ is an $S$-immersion of $X_{1}
\times_{S} X_{2}$ into $P_{1} \times_{S} P_{2}$ `(I, 4.3.1)`, and the inverse image of $\mathcal{O}_{P_{1}}(1)
\otimes_{S} \mathcal{O}_{P_{2}}(1)$ under this immersion is $\mathcal{L}_{1} \otimes_{S} \mathcal{L}_{2}$. Set $T =
Y_{1} \times_{S} Y_{2}$, and let $p_{1}$, $p_{2}$ be the projections of $T$ to `Y_1`, `Y_2` respectively. Setting
$P_{i}' = \mathbb{P}(p_{i}*(\mathcal{E}_{i}))$ ($i = 1, 2$), we have by (4.1.3.1) $P_{i}' = P_{i} \times_{Y_{i}} T$,
whence

```text
  P_1' ×_T P_2' = (P_1 ×_{Y_1} T) ×_T (P_2 ×_{Y_2} T)
                = P_1 ×_{Y_1} (T ×_{Y_2} P_2)
                = P_1 ×_{Y_1} (Y_1 ×_S P_2)
                = P_1 ×_S P_2
```

up to canonical isomorphism. Similarly, $\mathcal{O}_{P_{i}'}(1) = \mathcal{O}_{P_{i}}(1) \otimes_{Y_{i}}
\mathcal{O}_{T}$ (4.1.3.2), and an analogous computation (based notably on `(I, 9.1.9.1 and 9.1.2)`) shows that, in the
above identification, $\mathcal{O}_{P_{1}'}(1) \otimes_{T} \mathcal{O}_{P_{2}'}(1)$ is identified with
$\mathcal{O}_{P_{1}}(1) \otimes_{S} \mathcal{O}_{P_{2}}(1)$. We may thus regard $r_{1} \times_{S} r_{2}$ as a
$T$-immersion of $X_{1} \times_{S} X_{2}$ into $P_{1}' \times_{T} P_{2}'$, the inverse image of $\mathcal{O}_{P_{1}'}(1)
\otimes_{T} \mathcal{O}_{P_{2}'}(1)$ being $\mathcal{L}_{1} \otimes_{S} \mathcal{L}_{2}$. We finish the argument as in
(4.4.8) using the Segre morphism.

It remains to prove (ii). We may first restrict to the case where $Z$ is an affine scheme, since in general there is a
finite cover $(U_{i})$ of $Z$ by affine opens; if the proposition is proved for $\mathcal{K} | g^{-1}(U_{i})$,
$\mathcal{L} | f^{-1}(g^{-1}(U_{i}))$, and an integer $n_{i}$, it suffices to take $n_{0}$ the largest of the $n_{i}$ to
obtain the result for $\mathcal{K}$ and $\mathcal{L}$ (4.4.5). The hypothesis implies that $f$ and $g$ are separated, so
$X$ and $Y$ are quasi-compact schemes.

There is an immersion $r : X \to P = \mathbb{P}(\mathcal{E})$, where $\mathcal{E}$ is a quasi-coherent
$\mathcal{O}_{Y}$-module of finite type, and $\mathcal{L} = r*(\mathcal{O}_{P}(1))$, by (4.4.6). We shall see that there
exists an $\mathcal{O}_{P}$-module $\mathcal{M}$ very ample relative to the composed morphism $P \xrightarrow{h} Y
\xrightarrow{g} Z$ such that $\mathcal{O}_{P}(1)$ is isomorphic to $\mathcal{M} \otimes_{Y} \mathcal{K}^{\otimes(-m)}$
for some integer $m$. For $n \geq m + 1$, $\mathcal{O}_{P}(1) \otimes_{Y} \mathcal{K}^{\otimes n}$ will thus be very
ample for $Z$ by hypothesis and (iv) applied to the morphisms $h : P \to Y$ and `1_Y`; since $r$ is an immersion and
$\mathcal{L} \otimes f*(\mathcal{K}^{\otimes n}) = r*(\mathcal{O}_{P}(1) \otimes_{Y} \mathcal{K}^{\otimes n})$, the
conclusion will follow from (i bis). To prove our claim about $\mathcal{O}_{P}(1)$, we use the following lemma:

**Lemma.**

<!-- label: II.4.4.10.1 -->

Let $Z$ be a quasi-compact scheme or a prescheme whose underlying space is Noetherian, $g : Y \to Z$ a quasi-compact
morphism, $\mathcal{K}$ an invertible $\mathcal{O}_{Y}$-module very ample for $g$, and $\mathcal{E}$ a quasi-coherent
$\mathcal{O}_{Y}$-module of finite type. Then there exists an integer $m_{0}$ such that, for every $m \geq m_{0}$,
$\mathcal{E}$ is isomorphic to a quotient of an $\mathcal{O}_{Y}$-module of the form $g*(\mathcal{F}) \otimes
\mathcal{K}^{\otimes(-m)}$, where $\mathcal{F}$ is a quasi-coherent $\mathcal{O}_{Z}$-module of finite type (depending
on $m$).

This lemma will be proved in (4.5.10.1); the reader may verify that (4.4.10) is not used anywhere in §4.5.

<!-- original page 83 -->

This lemma being granted, there is a closed immersion $j_{1}$ of $P$ into

$$ P_{1} = \mathbb{P}(g*(\mathcal{F}) \otimes \mathcal{K}^{\otimes(-m)}) $$

such that $\mathcal{O}_{P}(1)$ is isomorphic to $j_{1}*(\mathcal{O}_{P_{1}}(1))$ (4.1.2). On the other hand, there is an
isomorphism from `P_1` to $P_{2} = \mathbb{P}(g*(\mathcal{F}))$, identifying $\mathcal{O}_{P_{2}}(1) \otimes_{Y}
\mathcal{K}^{\otimes(-m)}$ with $\mathcal{O}_{P_{1}}(1)$ (4.1.4); we therefore have a closed immersion $j_{2} : P \to
P_{2}$ such that $\mathcal{O}_{P}(1)$ is isomorphic to $j_{2}*(\mathcal{O}_{P_{2}}(1)) \otimes_{Y}
\mathcal{K}^{\otimes(-m)}$. Finally, `P_2` is identified with $P_{3} \times_{Z} Y$, where $P_{3} =
\mathbb{P}(\mathcal{F})$, and $\mathcal{O}_{P_{2}}(1)$ with $\mathcal{O}_{P_{3}}(1) \otimes_{Z} \mathcal{O}_{Y}$
(4.1.3). By definition, $\mathcal{O}_{P_{3}}(1)$ is very ample for $Z$; since so is $\mathcal{K}$, we conclude from (iv)
that $\mathcal{O}_{P_{2}}(1) \otimes_{Y} \mathcal{K}$ is very ample for $Z$; so is $\mathcal{M} =
j_{2}*(\mathcal{O}_{P_{2}}(1) \otimes_{Y} \mathcal{K})$ by (i bis), and $\mathcal{O}_{P}(1)$ is isomorphic to
$\mathcal{M} \otimes_{Y} \mathcal{K}^{\otimes(-m-1)}$, which completes the proof.

**Proposition.**

<!-- label: II.4.4.11 -->

Let $f : X \to Y$ and $f' : X' \to Y$ be two morphisms, `X''` the sum prescheme $X \sqcup X'$, and $f'' : X'' \to Y$ the
morphism that agrees with $f$ (resp. $f'$) on $X$ (resp. $X'$). Let $\mathcal{L}$ (resp. $\mathcal{L}'$) be an
invertible $\mathcal{O}_{X}$-module (resp. $\mathcal{O}_{X'}$-module), and let $\mathcal{L}''$ be the invertible
$\mathcal{O}_{X''}$-module that agrees with $\mathcal{L}$ on $X$ and with $\mathcal{L}'$ on $X'$. For $\mathcal{L}''$ to
be very ample relative to `f''`, it is necessary and sufficient that $\mathcal{L}$ be very ample relative to $f$ and
$\mathcal{L}'$ very ample relative to $f'$.

**Proof.** We reduce at once to $Y$ affine. If $\mathcal{L}''$ is very ample, then so are $\mathcal{L}$ and
$\mathcal{L}'$ by (4.4.10, (i bis)). Conversely, if $\mathcal{L}$ and $\mathcal{L}'$ are very ample, it follows at once
from Definition (4.4.2) and from (4.3.6) that $\mathcal{L}''$ is very ample.

## 4.5. Ample sheaves

**(4.5.1)**

<!-- label: II.4.5.1 -->

Given a prescheme $X$ and an invertible $\mathcal{O}_{X}$-module $\mathcal{L}$, we set, for every
$\mathcal{O}_{X}$-module $\mathcal{F}$ (when no confusion over $\mathcal{L}$ is possible),
$\mathcal{F}(n) = \mathcal{F} \otimes_{\mathcal{O}_{X}} \mathcal{L}^{\otimes n}$ ($n \in \mathbb{Z}$); we also set
$S = \oplus_{n\geq 0} \Gamma(X, \mathcal{L}^{\otimes n})$ (a graded subring of the ring $\Gamma_{\bullet}(\mathcal{L})$
defined in `(0, 5.4.6)`). Regarding $X$ as a $\mathbb{Z}$-prescheme with $p : X \to \operatorname{Spec}(\mathbb{Z})$ the
structure morphism, there is a bijective correspondence between the homomorphisms
$p*(\tilde{S}) \to \oplus_{n\geq 0} \mathcal{L}^{\otimes n}$ of graded $\mathcal{O}_{X}$-algebras and the endomorphisms
of the graded ring $S$ `(I, 2.2.5)`; the homomorphism
$\epsilon : p*(\tilde{S}) \to \oplus_{n\geq 0} \mathcal{L}^{\otimes n}$ corresponding in this way to the identity
automorphism of $S$ is called _canonical_. It corresponds (3.7.1) to a morphism $G(\epsilon) \to \operatorname{Proj}(S)$
which is also called _canonical_.

**Theorem.**

<!-- label: II.4.5.2 -->

Let $X$ be a quasi-compact scheme or a prescheme whose underlying space is Noetherian, $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-module, and $S$ the graded ring $\oplus_{n\geq 0} \Gamma(X, \mathcal{L}^{\otimes n})$. The following
conditions are equivalent:

a) When $f$ ranges over the set of homogeneous elements of $S_{+}$, the $X_{f}$ form a basis for the topology of $X$.
a') When $f$ ranges over the set of homogeneous elements of $S_{+}$, the $X_{f}$ that are affine form a cover of $X$. b)
The canonical morphism $G(\epsilon) \to \operatorname{Proj}(S)$ (4.5.1) is everywhere defined and is a dominant open
immersion.

<!-- original page 84 -->

b') The canonical morphism $G(\epsilon) \to \operatorname{Proj}(S)$ is everywhere defined and is a homeomorphism of the
underlying space of $X$ onto a subspace of $\operatorname{Proj}(S)$. c) For every quasi-coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$, denoting by $\mathcal{F}_{n}$ the sub-$\mathcal{O}_{X}$-module of
$\mathcal{F}(n)$ generated by the sections of $\mathcal{F}(n)$ over $X$, $\mathcal{F}$ is the sum of the
sub-$\mathcal{O}_{X}$-modules $\mathcal{F}_{n}(-n)$ for the integers $n > 0$. c') Property (c) holds for every
quasi-coherent sheaf of ideals of $\mathcal{O}_{X}$.

Furthermore, if $(f_{\alpha})$ is a family of homogeneous elements of $S_{+}$ such that the $X_{f_{\alpha}}$ are affine,
then the restriction to $\bigcup_{\alpha} X_{f_{\alpha}}$ of the canonical morphism $X \to \operatorname{Proj}(S)$ is an
isomorphism of $\bigcup_{\alpha} X_{f_{\alpha}}$ onto $\bigcup_{\alpha} (\operatorname{Proj}(S))_{f_{\alpha}}$.

**Proof.** It is clear that (b) implies (b'), and (b') implies (a) by formula (3.7.3.1) (taking into account that
$\epsilon\flat$ is the identity). Condition (a) implies (a'): every $x \in X$ has an affine neighbourhood $U$ such that
$\mathcal{L} | U$ is isomorphic to $\mathcal{O}_{X} | U$; if $f \in \Gamma(X, \mathcal{L}^{\otimes n})$ satisfies $x \in
X_{f} \subset U$, then $X_{f}$ is also the set of $x' \in U$ with $(f | U)(x') \neq 0$, and is therefore an affine open
`(I, 1.3.6)`. To show that (a') implies (b), it suffices to prove the last assertion of the statement, and to verify in
addition that, if $X = \bigcup X_{f_{\alpha}}$, condition (iv) of (3.8.2) is satisfied. This last point follows at once
from `(I, 9.3.1, (i))`. As for the last assertion of (4.5.2), since $X_{f_{\alpha}}$ is the inverse image of
$(\operatorname{Proj}(S))_{f_{\alpha}}$ under $G(\epsilon) \to \operatorname{Proj}(S)$, it suffices to apply
`(I, 9.3.2)`. Hence (a), (a'), (b), (b') are equivalent.

To show that (a') implies (c), note that if $X_{f}$ is affine (with $f \in S_{k}$), then $\mathcal{F} | X_{f}$ is
generated by its sections over $X_{f}$ `(I, 1.3.9)`; on the other hand `(I, 9.3.1, (ii))`, such a section $s$ is of the
form $(t | X_{f}) \otimes (f | X_{f})^{-m}$, where $t \in \Gamma(X, \mathcal{F}(km))$; by definition $t$ is also a
section of $\mathcal{F}_{km}$, so $s$ is indeed a section of $\mathcal{F}_{km}(-km)$ over $X_{f}$, which proves (c). It
is clear that (c) implies (c'), and it remains to show that (c') implies (a). Let $U$ be an open neighbourhood of $x \in
X$, and $\mathcal{J}$ a quasi-coherent sheaf of ideals of $\mathcal{O}_{X}$ defining a closed subprescheme of $X$ with
$X - U$ as underlying space `(I, 5.2.1)`. Hypothesis (c') implies that there exists an integer $n > 0$ and a section $f$
of $\mathcal{J}(n)$ over $X$ such that $f(x) \neq 0$. But evidently $f \in S_{n}$, and $x \in X_{f} \subset U$, which
proves (a).

When $X$ is a prescheme whose underlying space is Noetherian, the equivalent conditions of (4.5.2) imply that $X$ is a
_scheme_, since it is isomorphic to a subprescheme of the scheme $S = \operatorname{Proj}(A)$ by (4.5.2, b).

**Definition.**

<!-- label: II.4.5.3 -->

We say that an invertible $\mathcal{O}_{X}$-module $\mathcal{L}$ is _ample_ if $X$ is a quasi-compact scheme and the
equivalent conditions of (4.5.2) are satisfied.

It follows evidently from criterion (4.5.2, a) that, if $\mathcal{L}$ is an ample $\mathcal{O}_{X}$-module, then for
every open $U$ of $X$, $\mathcal{L} | U$ is an ample $(\mathcal{O}_{X} | U)$-module.

It also follows from the proof of (4.5.2) that the _affine_ $X_{f}$ already form a basis for the topology of $X$.
Moreover:

**Corollary.**

<!-- label: II.4.5.4 -->

Let $\mathcal{L}$ be an ample $\mathcal{O}_{X}$-module. For every finite subspace $Z$ of $X$ and every neighbourhood $U$
of $Z$, there exists an integer $n$ and an $f \in \Gamma(X, \mathcal{L}^{\otimes n})$ such that $X_{f}$ is an affine
neighbourhood of $Z$ contained in $U$.

<!-- original page 85 -->

**Proof.** By (4.5.2, b), it suffices to show that for every finite part $Z'$ of $\operatorname{Proj}(S)$ and every open
neighbourhood $U$ of $Z'$, there exists a homogeneous element $f \in S_{+}$ such that $Z \subset
(\operatorname{Proj}(S))_{f} \subset U$ (2.4.1). By definition the closed set $Y$, complement of $U$ in
$\operatorname{Proj}(S)$, is of the form $V_{+}(\mathfrak{J})$, where $\mathfrak{J}$ is a graded ideal of $S$ not
containing $S_{+}$ (2.3.2); on the other hand, the points of $Z'$ are by definition graded prime ideals
$\mathfrak{p}_{i}$ of $S_{+}$ not containing $\mathfrak{J}$ (2.3.1). There thus exists an element $f \in \mathfrak{J}$
not belonging to any of the $\mathfrak{p}_{i}$ (Bourbaki, _Alg. comm._, chap. II, §1, no. 1, prop. 2), and since the
$\mathfrak{p}_{i}$ are graded, the argument _loc. cit._ shows that one may even take $f$ to be homogeneous; this element
answers the question.

**Proposition.**

<!-- label: II.4.5.5 -->

Suppose $X$ is a quasi-compact scheme or a prescheme whose underlying space is Noetherian. Then conditions (a) to (c')
of (4.5.2) are also equivalent to the following:

d) For every quasi-coherent $\mathcal{O}_{X}$-module $\mathcal{F}$ of finite type, there exists an integer $n_{0}$ such
that, for every $n \geq n_{0}$, $\mathcal{F}(n)$ is generated by its sections over $X$. d') For every quasi-coherent
$\mathcal{O}_{X}$-module $\mathcal{F}$ of finite type, there exist integers $n > 0$ and $k > 0$ such that $\mathcal{F}$
is isomorphic to a quotient of the $\mathcal{O}_{X}$-module $\mathcal{L}^{\otimes(-n)} \otimes \mathcal{O}^{k}_{X}$.
d'') Property (d') holds for every quasi-coherent sheaf of ideals of $\mathcal{O}_{X}$ of finite type.

**Proof.** Since $X$ is quasi-compact, if a quasi-coherent $\mathcal{O}_{X}$-module $\mathcal{F}$ of finite type is such
that $\mathcal{F}(n)$ (which is of finite type) is generated by its sections over $X$, then $\mathcal{F}(n)$ is
generated by a finite number of these sections `(0, 5.2.3)`; so (d) implies (d'), and it is clear that (d') implies
(d''). Since every quasi-coherent $\mathcal{O}_{X}$-module $\mathcal{G}$ is the direct limit of its
sub-$\mathcal{O}_{X}$-modules of finite type `(I, 9.4.9)`, to verify condition (c') of (4.5.2), it suffices to do so for
a quasi-coherent sheaf of ideals of $\mathcal{O}_{X}$ of finite type, so (d'') implies (c'). It remains to see that if
$\mathcal{L}$ is ample, property (d) holds. Consider a finite cover of $X$ by $X_{f_{i}}$ ($f_{i} \in S_{n_{i}}$) which
we may assume affine; replacing the $f_{i}$ by suitable powers (which does not change the $X_{f_{i}}$), we may suppose
all the $n_{i}$ equal to a single integer $m$. The sheaf $\mathcal{F} | X_{f_{i}}$, of finite type by hypothesis, is
generated by a finite number of sections $h_{ij}$ over $X_{f_{i}}$ `(I, 1.3.13)`; so there is an integer $k_{0}$ such
that the section $h_{ij} \otimes f^{\otimes k_{0}}_{i}$ extends to a section of $\mathcal{F}(k_{0} m)$ over $X$ for
every pair $(i, j)$ `(I, 9.3.1)`. _A fortiori_ the $h_{ij} \otimes f^{\otimes k}_{i}$ extend to sections of
$\mathcal{F}(km)$ over $X$ for every $k \geq k_{0}$, and for these values of $k$, $\mathcal{F}(km)$ is generated by its
sections over $X$. For every $p$ with $0 < p < m$, $\mathcal{F}(p)$ is also of finite type, so there is an integer
$k_{p}$ such that $\mathcal{F}(p)(km) = \mathcal{F}(p + km)$ is generated by its sections over $X$ for $k \geq k_{p}$.
Taking $n_{0}$ larger than all the $k_{p} m$, we conclude that $\mathcal{F}(n)$ is generated by its sections over $X$
for every $n \geq n_{0}$, since such an $n$ writes $n = km + p$ with $k \geq k_{p}$ and $0 \leq p < m$.

**Proposition.**

<!-- label: II.4.5.6 -->

Let $X$ be a quasi-compact scheme and $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module.

1. Let $n > 0$ be an integer. For $\mathcal{L}$ to be ample, it is necessary and sufficient that $\mathcal{L}^{\otimes
   n}$ be ample.
1. Let $\mathcal{L}'$ be an invertible $\mathcal{O}_{X}$-module such that for every $x \in X$ there exists an integer
   $n > 0$

<!-- original page 86 -->

```
and a section `s'` of `ℒ'^{⊗n}` over `X` such that `s'(x) ≠ 0`. Then
if `ℒ` is ample, so is `ℒ ⊗ ℒ'`.
```

**Proof.** Property (i) is an evident consequence of criterion (a) of (4.5.2), since $X_{f^{\otimes n}} = X_{f}$. On the
other hand, if $\mathcal{L}$ is ample, then for every $x \in X$ and every neighbourhood $U$ of $x$ there is $m > 0$ and
$f \in \Gamma(X, \mathcal{L}^{\otimes m})$ such that $x \in X_{f} \subset U$ (4.5.2, a); if $f' \in \Gamma(X,
\mathcal{L}'^{\otimes n})$ satisfies $f'(x) \neq 0$, then $s(x) \neq 0$ for $s = f^{\otimes n} \otimes f'^{\otimes m}
\in \Gamma(X, (\mathcal{L} \otimes \mathcal{L}')^{\otimes mn})$, so $x \in X_{s} \subset X_{f} \subset U$, which proves
that $\mathcal{L} \otimes \mathcal{L}'$ is ample (4.5.2, a).

**Corollary.**

<!-- label: II.4.5.7 -->

The tensor product of two ample $\mathcal{O}_{X}$-modules is ample.

**Corollary.**

<!-- label: II.4.5.8 -->

Let $\mathcal{L}$ be an ample $\mathcal{O}_{X}$-module and $\mathcal{L}'$ an invertible $\mathcal{O}_{X}$-module. Then
there exists an integer $n_{0} > 0$ such that $\mathcal{L}^{\otimes n} \otimes \mathcal{L}'$ is ample and generated by
its sections over $X$ for $n \geq n_{0}$.

**Proof.** By (4.5.5) there is an integer $m_{0}$ such that $\mathcal{L}^{\otimes m} \otimes \mathcal{L}'$ is generated
by its sections over $X$ for $m \geq m_{0}$; by (4.5.6) we may then take $n_{0} = m_{0} + 1$.

**Remark.**

<!-- label: II.4.5.9 -->

Let $P = H^{1}(X, \mathcal{O}_{X}*)$ be the group of classes of invertible $\mathcal{O}_{X}$-modules `(0, 5.4.7)`, and
let $P^{+}$ be the part of $P$ formed by the classes of ample sheaves. Suppose $P^{+}$ is non-empty. Then it follows
from (4.5.7) and (4.5.8) that

```text
  P⁺ + P⁺ ⊂ P⁺    and    P⁺ − P⁺ = P,
```

in other words, $P^{+} \cup {0}$ is the set of positive elements in $P$ for a _preorder_ structure on $P$ compatible
with its group structure, which is even _archimedean_ by (4.5.8). For this reason one sometimes says "positive sheaf"
instead of ample sheaf, and "negative sheaf" for the inverse of such a sheaf (terminology that we shall not follow).

**Proposition.**

<!-- label: II.4.5.10 -->

Let $Y$ be an affine scheme, $q : X \to Y$ a quasi-compact separated morphism, and $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-module.

1. If $\mathcal{L}$ is very ample relative to $q$, then $\mathcal{L}$ is ample.
1. Suppose in addition that the morphism $q$ is _of finite type_. Then, for $\mathcal{L}$ to be ample, it is necessary
   and sufficient that it possess one of the following equivalent properties: e) There exists $n_{0} > 0$ such that for
   every integer $n \geq n_{0}$, $\mathcal{L}^{\otimes n}$ is very ample relative to $q$. e') There exists $n > 0$ such
   that $\mathcal{L}^{\otimes n}$ is very ample relative to $q$.

**Proof.** The first claim follows from Definition (4.4.2) of a very ample $\mathcal{O}_{X}$-module: if $A$ is the ring
of $Y$, there exists an $A$-module $E$ and a surjective homomorphism

```text
  ψ : q*((𝕊(E))~) → ⊕_{n≥0} ℒ^{⊗n}
```

such that $i = r_{\mathcal{L},\psi}$ is an everywhere-defined immersion $X \to P = \mathbb{P}(\tilde{E})$ and
$\mathcal{L} = i*(\mathcal{O}_{P}(1))$; since the $D_{+}(f)$ for $f$ homogeneous in $(\mathbb{S}(E))_{+}$ form a basis
of the topology of $P$, and $i^{-1}(D_{+}(f)) = X_{\psi\flat(f)}$ by (3.7.3.1), we see that condition (a) of (4.5.2) is
satisfied, so $\mathcal{L}$ is ample.

Now we prove that if $q$ is of finite type and $\mathcal{L}$ is ample, then $\mathcal{L}$ satisfies (e). First, it
follows from criterion (b) of (4.5.2) and from (4.4.1, (i)) that there exists

<!-- original page 86 -->

an integer $k_{0} > 0$ such that $\mathcal{L}^{\otimes k_{0}}$ is very ample relative to $q$. Also by (4.5.5) there is
an integer $m_{0}$ such that for $m \geq m_{0}$, $\mathcal{L}^{\otimes m}$ is generated by its sections over $X$. Set
$n_{0} = k_{0} + m_{0}$; if $n \geq n_{0}$, write $n = k_{0} + m$ with $m \geq m_{0}$, whence $\mathcal{L}^{\otimes n} =
\mathcal{L}^{\otimes k_{0}} \otimes \mathcal{L}^{\otimes m}$. Since $\mathcal{L}^{\otimes m}$ is generated by its
sections over $X$, it follows from (4.4.8) and (3.4.7) that $\mathcal{L}^{\otimes n}$ is very ample relative to $q$.
Finally, it is clear that (e) implies (e'), and (e') implies that $\mathcal{L}$ is ample by (i) and (4.5.6, (i)).

**(4.5.10.1)** _Proof of Lemma (4.4.10.1)._

<!-- label: II.4.5.10.1 -->

Set $\mathcal{E}(n) = \mathcal{E} \otimes \mathcal{K}^{\otimes n}$; since $g$ is separated (4.4.2), the argument of
(3.4.8) applies and reduces matters to showing that the canonical homomorphism $g*(g_{*}(\mathcal{E}(n))) \to
\mathcal{E}(n)$ is surjective for $n$ large enough. Furthermore, since $Z$ is quasi-compact, the argument of (3.4.6)
reduces the proposition to the case where $Z$ is affine. But $\mathcal{K}$ is then ample by (4.5.10, (i)), and the
conclusion follows from (4.5.5, d').

**Corollary.**

<!-- label: II.4.5.11 -->

Let $Y$ be an affine scheme, $q : X \to Y$ a separated morphism of finite type, $\mathcal{L}$ an ample
$\mathcal{O}_{X}$-module, and $\mathcal{L}'$ an invertible $\mathcal{O}_{X}$-module. There exists an integer $n_{0}$
such that for $n \geq n_{0}$, $\mathcal{L}^{\otimes n} \otimes \mathcal{L}'$ is very ample relative to $q$.

**Proof.** There is an $m_{0}$ such that for $m \geq m_{0}$, $\mathcal{L}^{\otimes m} \otimes \mathcal{L}'$ is generated
by its sections over $X$ (4.5.8); on the other hand there is a $k_{0}$ such that $\mathcal{L}^{\otimes k}$ is very ample
relative to $q$ for $k \geq k_{0}$. Therefore $\mathcal{L}^{\otimes(k + m_{0})} \otimes \mathcal{L}'$ is very ample for
$k \geq k_{0}$ ((4.4.8) and (3.4.7)).

**Remark.**

<!-- label: II.4.5.12 -->

It is not known whether the hypothesis that an $\mathcal{O}_{X}$-module $\mathcal{L}$ is such that $\mathcal{L}^{\otimes
n}$ is very ample (relative to $q$) implies the same conclusion for $\mathcal{L}^{\otimes(n+1)}$.

**Proposition.**

<!-- label: II.4.5.13 -->

Let $X$ be a quasi-compact prescheme, $Z$ a closed subprescheme of $X$ defined by a _nilpotent_ quasi-coherent sheaf
$\mathcal{J}$ of ideals of $\mathcal{O}_{X}$, and $j$ the canonical injection $Z \to X$. For an invertible
$\mathcal{O}_{X}$-module $\mathcal{L}$ to be ample, it is necessary and sufficient that $\mathcal{L}' = j*(\mathcal{L})$
be an ample $\mathcal{O}_{Z}$-module.

**Proof.** _The condition is necessary._ Indeed, for every section $f$ of $\mathcal{L}^{\otimes n}$ over $X$, let $f'$
be its canonical image $f \otimes 1$, a section of $\mathcal{L}'^{\otimes n} = \mathcal{L}^{\otimes n}
\otimes_{\mathcal{O}_{X}} (\mathcal{O}_{X}/\mathcal{J})$ over the space $Z$ (which is identical to $X$); it is clear
that $X_{f} = Z_{f'}$, so criterion (a) of (4.5.2) shows that $\mathcal{L}'$ is ample.

To see that the condition is _sufficient_, note first that we may reduce to the case $\mathcal{J}^{2} = 0$ by
considering the (finite) sequence of preschemes $X_{k} = (X, \mathcal{O}_{X} / \mathcal{J}^{k+1})$, each a closed
subprescheme of the next defined by a sheaf of ideals of square zero. Moreover, $X$ is a scheme, since $X_{red}$ is by
hypothesis (4.5.3 and `(I, 5.5.1)`). Criterion (a) of (4.5.2) shows that it suffices to prove the

**Lemma.**

<!-- label: II.4.5.13.1 -->

Under the hypotheses of (4.5.13), suppose in addition that $\mathcal{J}$ is of square zero; $\mathcal{L}$ being an
invertible $\mathcal{O}_{X}$-module, let $g$ be a section of $\mathcal{L}'^{\otimes n}$ over $Z$ such that $Z_{g}$ is
affine. Then there exists an integer $m > 0$ such that $g^{\otimes m}$ is the canonical image of a section $f$ of
$\mathcal{L}^{\otimes nm}$ over $X$.

**Proof.** We have the exact sequence of $\mathcal{O}_{X}$-modules

```text
  0 → 𝒥(n) → 𝒪_X(n) = ℒ^{⊗n} → 𝒪_Z(n) = ℒ'^{⊗n} → 0
```

<!-- original page 88 -->

since $\mathcal{F}(n)$ is an exact functor in $\mathcal{F}$; whence the cohomology exact sequence

```text
  0 → Γ(X, 𝒥(n)) → Γ(X, ℒ^{⊗n}) → Γ(X, ℒ'^{⊗n}) ─∂→ H¹(X, 𝒥(n))
```

which associates to $g$ in particular an element $\partial g \in H^{1}(X, \mathcal{J}(n))$.

Note that since $\mathcal{J}^{2} = 0$, $\mathcal{J}$ may be regarded as a quasi-coherent $\mathcal{O}_{Z}$-module, and
for every $k$ we have $\mathcal{L}'^{\otimes k} \otimes_{\mathcal{O}_{Z}} \mathcal{J}(n) = \mathcal{J}(n + k)$; for
every section $s \in \Gamma(X, \mathcal{L}'^{\otimes k})$, tensor multiplication by $s$ is a homomorphism
$\mathcal{J}(n) \to \mathcal{J}(n + k)$ of $\mathcal{O}_{Z}$-modules, which therefore yields a homomorphism $H^{1}(X,
\mathcal{J}(n)) \to H^{1}(X, \mathcal{J}(n + k))$ of cohomology groups.

We shall see that

$$ g^{\otimes m} \otimes \partial g = 0 (4.5.13.2) $$

for $m > 0$ large enough. Indeed, $Z_{g}$ is an affine open of $Z$, so $H^{1}(Z_{g}, \mathcal{J}(n)) = 0$ when
$\mathcal{J}(n)$ is viewed as an $\mathcal{O}_{Z}$-module `(I, 5.1.9.2)`. In particular, if $g' = g | Z_{g}$, and
considering its image under the map
$\partial : \Gamma(Z_{g}, \mathcal{L}'^{\otimes n}) \to H^{1}(Z_{g}, \mathcal{J}(n))$, we have $\partial g' = 0$. To
make this relation explicit, observe that in dimension 1 the cohomology of a sheaf of abelian groups coincides with its
Čech cohomology (G, II, 5.9); to compute $\partial g$, we must thus consider a fine enough open cover $(U_{\alpha})$ of
$X$, which we may take _finite_ and made of affine opens, take for each $\alpha$ a section
$g_{\alpha} \in \Gamma(U_{\alpha}, \mathcal{L}^{\otimes n})$ whose canonical image in
$\Gamma(U_{\alpha}, \mathcal{L}'^{\otimes n})$ is $g | U_{\alpha}$, and consider the cocycle class of
$(g_{\alpha|\beta} - g_{\beta|\alpha})$, with $g_{\alpha|\beta}$ the restriction of $g_{\alpha}$ to
$U_{\alpha} \cap U_{\beta}$ (this cocycle taking values in $\mathcal{J}(n)$). One may further suppose that $\partial g'$
is computed in the same way using the cover formed by the $U_{\alpha} \cap Z_{g}$ and the restrictions
$g_{\alpha} | (U_{\alpha} \cap Z_{g})$ (replacing $(U_{\alpha})$ by a finer cover if needed); the relation
$\partial g' = 0$ then means there exists for each $\alpha$ a section
$h_{\alpha} \in \Gamma(U_{\alpha} \cap Z_{g}, \mathcal{J}(n))$ such that
$(g_{\alpha|\beta} - g_{\beta|\alpha}) | (U_{\alpha} \cap U_{\beta} \cap Z_{g}) = h_{\alpha|\beta} - h_{\beta|\alpha}$,
with $h_{\alpha|\beta}$ the restriction of $h_{\alpha}$ to $U_{\alpha} \cap U_{\beta} \cap Z_{g}$ (G, II, 5.11). Then
there exists an integer $m > 0$ such that $g^{\otimes m} \otimes h_{\alpha}$ is the restriction to
$U_{\alpha} \cap Z_{g}$ of a section $t_{\alpha} \in \Gamma(U_{\alpha}, \mathcal{J}(n + nm))$ for every $\alpha$
`(I, 9.3.1)`; hence $g^{\otimes m} \otimes (g_{\alpha|\beta} - g_{\beta|\alpha}) = t_{\alpha|\beta} - t_{\beta|\alpha}$
for every pair of indices, which proves (4.5.13.2).

Note further that if $s \in \Gamma(X, \mathcal{O}_{Z}(p))$, $t \in \Gamma(X, \mathcal{O}_{Z}(q))$, then in the group
$H^{1}(X, \mathcal{J}(p + q))$

```text
  ∂(s ⊗ t) = (∂s) ⊗ t + s ⊗ (∂t).                                          (4.5.13.3)
```

Indeed, to compute both sides we may again consider an open cover $(U_{\alpha})$ of $X$, and for each $\alpha$ a section
$s_{\alpha} \in \Gamma(U_{\alpha}, \mathcal{O}_{X}(p))$ (resp. $t_{\alpha} \in \Gamma(U_{\alpha}, \mathcal{O}_{X}(q))$)
whose canonical image in $\Gamma(U_{\alpha}, \mathcal{O}_{Z}(p))$ (resp. $\Gamma(U_{\alpha}, \mathcal{O}_{Z}(q))$) is $s
| U_{\alpha}$ (resp. $t | U_{\alpha}$); the relation (4.5.13.3) then follows from

```text
  (s_{α|β} ⊗ t_{α|β}) − (s_{β|α} ⊗ t_{β|α})
    = (s_{α|β} − s_{β|α}) ⊗ t_{α|β} + s_{β|α} ⊗ (t_{α|β} − t_{β|α})
```

with the same notation. By induction on $k$ we therefore have

```text
  ∂(g^{⊗k}) = (k g^{⊗(k−1)}) ⊗ (∂g)                                        (4.5.13.4)
```

<!-- original page 89 -->

and we conclude from (4.5.13.2) and (4.5.13.4) that $\partial(g^{\otimes(m+1)}) = 0$; hence $g^{\otimes(m+1)}$ is the
canonical image of a section $f$ of $\mathcal{L}^{\otimes n(m+1)}$ over $X$, which completes the proof of (4.5.13).

**Corollary.**

<!-- label: II.4.5.14 -->

Let $X$ be a Noetherian scheme, and $j$ the canonical injection $X_{red} \to X$. For an invertible
$\mathcal{O}_{X}$-module $\mathcal{L}$ to be ample, it is necessary and sufficient that $j*(\mathcal{L})$ be an ample
$\mathcal{O}_{X_{red}}$-module.

**Proof.** This follows from `(I, 6.1.6)`.

## 4.6. Relatively ample sheaves

**Definition.**

<!-- label: II.4.6.1 -->

Let $f : X \to Y$ be a quasi-compact morphism, and $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module. We say that
$\mathcal{L}$ is _ample relative to $f$_, or _relative to $Y$_, or _$f$-ample_, or _$Y$-ample_ (or even simply _ample_,
if no confusion arises with the notion defined in (4.5.3)) if there exists an affine open cover $(U_{\alpha})$ of $Y$
such that, setting $X_{\alpha} = f^{-1}(U_{\alpha})$, $\mathcal{L} | X_{\alpha}$ is an ample
$\mathcal{O}_{X_{\alpha}}$-module for every $\alpha$.

The existence of an $f$-ample $\mathcal{O}_{X}$-module implies that $f$ is necessarily _separated_ ((4.5.3) and
`(I, 5.5.5)`).

**Proposition.**

<!-- label: II.4.6.2 -->

Let $f : X \to Y$ be a quasi-compact morphism, and $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module. If
$\mathcal{L}$ is very ample relative to $f$, then it is ample relative to $f$.

**Proof.** This follows from the local (on $Y$) character of the notion of very ample sheaf (4.4.5), from Definition
(4.6.1), and from criterion (4.5.10, (i)).

**Proposition.**

<!-- label: II.4.6.3 -->

Let $f : X \to Y$ be a quasi-compact morphism, $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module, and let
$\mathcal{S}$ be the graded $\mathcal{O}_{Y}$-algebra $\oplus_{n\geq 0} f_{*}(\mathcal{L}^{\otimes n})$. The following
conditions are equivalent:

a) $\mathcal{L}$ is $f$-ample. b) $\mathcal{S}$ is quasi-coherent and the canonical homomorphism $\sigma :
f*(\mathcal{S}) \to \oplus_{n\geq 0} \mathcal{L}^{\otimes n}$ `(0, 4.4.3)` is such that the $Y$-morphism
$r_{\mathcal{L},\sigma} : G(\sigma) \to \operatorname{Proj}(\mathcal{S}) = P$ is everywhere defined and is a dominant
open immersion. b') The morphism $f$ is separated, the $Y$-morphism $r_{\mathcal{L},\sigma}$ is everywhere defined and
is a homeomorphism of the underlying space of $X$ onto a subspace of $\operatorname{Proj}(\mathcal{S})$.

Furthermore, when these hold, for every $n \in \mathbb{Z}$ the canonical homomorphism

$$ r_{\mathcal{L},\sigma}*(\mathcal{O}_{P}(n)) \to \mathcal{L}^{\otimes n} (4.6.3.1) $$

defined in (3.7.9.1) is an isomorphism.

Finally, for every quasi-coherent $\mathcal{O}_{X}$-module $\mathcal{F}$, setting $\mathcal{M} = \oplus_{n\geq 0}
f_{*}(\mathcal{F} \otimes \mathcal{L}^{\otimes n})$, the canonical homomorphism

$$ r_{\mathcal{L},\sigma}*(\tilde{\mathcal{M}}) \to \mathcal{F} (4.6.3.2) $$

defined in (3.7.9.2) is an isomorphism.

**Proof.** We have noted that (a) implies $f$ is separated, so $\mathcal{S}$ is quasi-coherent `(I, 9.2.2, a)`. Since
$r_{\mathcal{L},\sigma}$ being an everywhere defined immersion is of local character on $Y$, to prove (a) implies (b) we
may suppose $Y$ affine and $\mathcal{L}$ ample;

<!-- original page 89 -->

the assertion then follows from (4.5.2, b). It is clear that (b) implies (b'); finally, to prove (b') implies (a), it
suffices to consider an affine open cover of $Y$ by $U_{\alpha}$ and to apply criterion (4.5.2, b') to each sheaf
$\mathcal{L} | f^{-1}(U_{\alpha})$.

For the last two assertions, we use the fact that $\sigma\flat$ here is the identity, and the explicit description of
the homomorphisms (3.7.9.1) and (3.7.9.2); it follows at once that (4.6.3.1) is an isomorphism. As for (4.6.3.2), we may
reduce to $Y$ affine, hence $\mathcal{L}$ ample; it is clear that (4.6.3.2) is injective, and criterion (4.5.2, c) shows
it is surjective, whence the conclusion.

**Corollary.**

<!-- label: II.4.6.4 -->

Let $(U_{\alpha})$ be an open cover of $Y$. For $\mathcal{L}$ to be ample relative to $Y$, it is necessary and
sufficient that $\mathcal{L} | f^{-1}(U_{\alpha})$ be ample relative to $U_{\alpha}$ for every $\alpha$.

**Proof.** Condition (b) is indeed local on $Y$.

**Corollary.**

<!-- label: II.4.6.5 -->

Let $\mathcal{K}$ be an invertible $\mathcal{O}_{Y}$-module. For $\mathcal{L}$ to be $Y$-ample, it is necessary and
sufficient that $\mathcal{L} \otimes f*(\mathcal{K})$ be so.

**Proof.** This is an evident consequence of (4.6.4), taking the $U_{\alpha}$ such that $\mathcal{K} | U_{\alpha}$ is
isomorphic to $\mathcal{O}_{Y} | U_{\alpha}$ for every $\alpha$.

**Corollary.**

<!-- label: II.4.6.6 -->

Suppose $Y$ affine; for $\mathcal{L}$ to be $Y$-ample it is necessary and sufficient that $\mathcal{L}$ be ample.

**Proof.** This is an immediate consequence of Definition (4.6.1) and of the criteria (4.6.3, b) and (4.5.2, b), since
here $\operatorname{Proj}(\mathcal{S}) = \operatorname{Proj}(\Gamma(Y, \mathcal{S}))$ by definition.

**Corollary.**

<!-- label: II.4.6.7 -->

Let $f : X \to Y$ be a quasi-compact morphism. Suppose there exist a quasi-coherent $\mathcal{O}_{Y}$-module
$\mathcal{E}$ and a $Y$-morphism $g : X \to P = \mathbb{P}(\mathcal{E})$ that is a homeomorphism of the underlying space
of $X$ onto a subspace of $P$; then $\mathcal{L} = g*(\mathcal{O}_{P}(1))$ is $Y$-ample.

**Proof.** We may suppose $Y$ affine; the corollary then follows from criterion (4.5.2, a), from formula (3.7.3.1), and
from (4.2.3).

**Proposition.**

<!-- label: II.4.6.8 -->

Let $X$ be a quasi-compact scheme or a prescheme whose underlying space is Noetherian, and $f : X \to Y$ a quasi-compact
separated morphism. For an invertible $\mathcal{O}_{X}$-module $\mathcal{L}$ to be $f$-ample, it is necessary and
sufficient that one of the following equivalent conditions hold:

c) For every quasi-coherent $\mathcal{O}_{X}$-module $\mathcal{F}$ of finite type, there exists an integer $n_{0} > 0$
such that for every $n \geq n_{0}$, the canonical homomorphism $\sigma : f*(f_{*}(\mathcal{F} \otimes
\mathcal{L}^{\otimes n})) \to \mathcal{F} \otimes \mathcal{L}^{\otimes n}$ is surjective. c') For every quasi-coherent
sheaf $\mathcal{J}$ of ideals of $\mathcal{O}_{X}$ of finite type, there exists an integer $n > 0$ such that the
canonical homomorphism $\sigma : f*(f_{*}(\mathcal{J} \otimes \mathcal{L}^{\otimes n})) \to \mathcal{J} \otimes
\mathcal{L}^{\otimes n}$ is surjective.

**Proof.** Since $X$ is quasi-compact, so is $f(X)$, so there exists a finite cover $(U_{i})$ of $f(X)$ by affine opens
of $Y$. To prove (c) when $\mathcal{L}$ is $f$-ample, we may replace $Y$ by the $U_{i}$ and $X$ by the $f^{-1}(U_{i})$:
if we obtain for each $i$ an integer $n_{i}$ such that (c) holds (for $U_{i}$, $f^{-1}(U_{i})$, and $\mathcal{L} |
f^{-1}(U_{i})$) for every $n \geq n_{i}$, it suffices to take $n_{0}$ the largest of the $n_{i}$ to obtain (c) for $Y$,
$X$, $\mathcal{L}$. But when $Y$ is affine, condition (c) follows from (4.5.5, d) taking (4.6.6) into account. It is
trivial that (c) implies (c'). Finally, to prove that (c') implies that $\mathcal{L}$ is $f$-ample, we may again
restrict to $Y$ affine: indeed, every quasi-coherent sheaf $\mathcal{J}_{i}$ of ideals of $\mathcal{O}_{X} |
f^{-1}(U_{i})$ of finite type is the restriction of a coherent sheaf of ideals of $\mathcal{O}_{X}$ of finite type
`(I, 9.4.7)`, and hypothesis (c') implies

<!-- original page 91 -->

that $\mathcal{J}_{i} \otimes (\mathcal{L}^{\otimes n} | f^{-1}(U_{i}))$ is generated by its sections (taking
`(I, 9.2.2)` and (3.4.7) into account); it then suffices to apply criterion (4.5.5, d'').

**Proposition.**

<!-- label: II.4.6.9 -->

Let $f : X \to Y$ be a quasi-compact morphism, $\mathcal{L}$ an invertible $\mathcal{O}_{X}$-module.

1. Let $n > 0$ be an integer. For $\mathcal{L}$ to be $f$-ample, it is necessary and sufficient that
   $\mathcal{L}^{\otimes n}$ be $f$-ample.
1. Let $\mathcal{L}'$ be an invertible $\mathcal{O}_{X}$-module, and suppose there exists an integer $n > 0$ such that
   the canonical homomorphism $\sigma : f*(f_{*}(\mathcal{L}'^{\otimes n})) \to \mathcal{L}'^{\otimes n}$ is surjective.
   Then, if $\mathcal{L}$ is $f$-ample, so is $\mathcal{L} \otimes \mathcal{L}'$.

**Proof.** We reduce immediately to the case $Y$ affine, and the proposition is then an immediate consequence of
(4.5.6).

**Corollary.**

<!-- label: II.4.6.10 -->

The tensor product of two $f$-ample $\mathcal{O}_{X}$-modules is $f$-ample.

**Proposition.**

<!-- label: II.4.6.11 -->

Let $Y$ be a quasi-compact prescheme, $f : X \to Y$ a morphism of finite type, and $\mathcal{L}$ an invertible
$\mathcal{O}_{X}$-module. For $\mathcal{L}$ to be $f$-ample, it is necessary and sufficient that it possess one of the
following equivalent properties:

d) There exists $n_{0} > 0$ such that for every integer $n \geq n_{0}$, $\mathcal{L}^{\otimes n}$ is very ample relative
to $f$. d') There exists $n > 0$ such that $\mathcal{L}^{\otimes n}$ is very ample relative to $f$.

**Proof.** If $\mathcal{L}$ is ample relative to $f$, there is a finite cover $(U_{i})$ of $Y$ by affine opens such that
the $\mathcal{L} | f^{-1}(U_{i})$ are ample. We then conclude (4.5.10) that there exists an integer $n_{0}$ such that
$\mathcal{L}^{\otimes n} | f^{-1}(U_{i})$ is very ample relative to $f^{-1}(U_{i}) \to U_{i}$ for every $n \geq n_{0}$
and every $i$, so $\mathcal{L}^{\otimes n}$ is very ample relative to $f$ (4.4.5). Conversely, (d') already implies
$\mathcal{L}^{\otimes n}$ is $f$-ample (4.6.2), so the same holds for $\mathcal{L}$ (4.6.9, (i)).

**Corollary.**

<!-- label: II.4.6.12 -->

Let $Y$ be a quasi-compact prescheme, $f : X \to Y$ a morphism of finite type, and $\mathcal{L}$, $\mathcal{L}'$ two
invertible $\mathcal{O}_{X}$-modules. If $\mathcal{L}$ is $f$-ample, there exists an $n_{0}$ such that
$\mathcal{L}^{\otimes n} \otimes \mathcal{L}'$ is very ample relative to $f$ for every $n \geq n_{0}$.

**Proof.** One argues as in (4.6.11) using a finite affine open cover of $Y$ and (4.5.11).

**Proposition.**

<!-- label: II.4.6.13 -->

1. For every prescheme $Y$, every invertible $\mathcal{O}_{Y}$-module $\mathcal{L}$ is ample relative to the identity
   morphism `1_Y`.
1. (i bis) Let $f : X \to Y$ be a quasi-compact morphism, and $j : X' \to X$ a quasi-compact morphism that is a
   homeomorphism of the underlying space of $X'$ onto a subspace of $X$. If $\mathcal{L}$ is an $\mathcal{O}_{X}$-module
   ample relative to $f$, then $j*(\mathcal{L})$ is ample relative to $f \circ j$.
1. Let $Z$ be a quasi-compact prescheme, $f : X \to Y$ and $g : Y \to Z$ quasi-compact morphisms, $\mathcal{L}$ an
   $\mathcal{O}_{X}$-module ample relative to $f$, and $\mathcal{K}$ an $\mathcal{O}_{Y}$-module ample relative to $g$.
   Then there exists an integer $n_{0} > 0$ such that $\mathcal{L} \otimes f*(\mathcal{K}^{\otimes n})$ is ample
   relative to $g \circ f$ for every $n \geq n_{0}$.
1. Let $f : X \to Y$ be a quasi-compact morphism, $g : Y' \to Y$ a morphism, and set $X' = X_{(Y')}$. If $\mathcal{L}$
   is an $\mathcal{O}_{X}$-module ample relative to $f$, then $\mathcal{L}' = \mathcal{L} \otimes_{Y} \mathcal{O}_{Y'}$
   is an $\mathcal{O}_{X'}$-module ample relative to $f_{(Y')}$.
1. Let $f_{i} : X_{i} \to Y_{i}$ ($i = 1, 2$) be two quasi-compact $S$-morphisms. If $\mathcal{L}_{i}$ is an
   $\mathcal{O}_{X_{i}}$-module ample relative to $f_{i}$ ($i = 1, 2$), then $\mathcal{L}_{1} \otimes_{S}
   \mathcal{L}_{2}$ is ample relative to $f_{1} \times_{S} f_{2}$.
1. Let $f : X \to Y$ and $g : Y \to Z$ be morphisms with $g \circ f$ quasi-compact. If an

<!-- original page 92 -->

```
`𝒪_X`-module `ℒ` is ample relative to `g ∘ f`, and if `g` is
separated or the underlying space of `X` is locally Noetherian, then
`ℒ` is ample relative to `f`.
```

1. Let $f : X \to Y$ be a quasi-compact morphism, and $j$ the canonical injection $X_{red} \to X$. If $\mathcal{L}$ is
   an $\mathcal{O}_{X}$-module ample relative to $f$, then $j*(\mathcal{L})$ is ample relative to $f_{red}$.

**Proof.** Note first that (v) and (vi) follow from (i), (i bis), and (iv) by the same argument as in (4.4.10), using
(4.6.4) in place of (4.4.5); we leave the details to the reader. Assertion (i) is trivially a consequence of (4.4.10,
(i)) and (4.6.2). To prove (i bis), (iii) and (iv) we use the following lemma:

**Lemma.**

<!-- label: II.4.6.13.1 -->

1. Let $u : Z \to S$ be a morphism, $\mathcal{L}$ an invertible $\mathcal{O}_{S}$-module, $s$ a section of $\mathcal{L}$
   over $S$, and $s'$ the section of $u*(\mathcal{L}) = \mathcal{L}'$ over $Z$ canonically corresponding to it. Then
   $Z_{s'} = u^{-1}(S_{s})$.
1. Let $Z$, $Z'$ be two $S$-preschemes, $p$, $p'$ the projections of $T = Z \times_{S} Z'$, $\mathcal{L}$ (resp.
   $\mathcal{L}'$) an invertible $\mathcal{O}_{Z}$-module (resp. $\mathcal{O}_{Z'}$-module), $t$ (resp. $t'$) a section
   of $\mathcal{L}$ (resp. $\mathcal{L}'$) over $Z$ (resp. $Z'$), and $s$ (resp. $s'$) the section of $p*(\mathcal{L})$
   (resp. $p'*(\mathcal{L}')$) over $Z \times_{S} Z'$ corresponding to it. Then $T_{s \otimes s'} = Z_{t} \times_{S}
   Z'_{t'}$.

**Proof.** The definitions show that we may reduce to the case where all preschemes considered are affine. Furthermore,
in (i), we may assume $\mathcal{L} = \mathcal{O}_{S}$; assertion (i) then follows at once from `(I, 1.2.2.2)`.
Similarly, in (ii) we may restrict to $\mathcal{L} = \mathcal{O}_{Z}$, $\mathcal{L}' = \mathcal{O}_{Z'}$, and the
assertion then reduces to Lemma (4.3.2.4).

We now prove (i bis). We may suppose $Y$ affine (4.6.4), hence $\mathcal{L}$ ample (4.6.6); when $s$ ranges over the
union of the $\Gamma(X, \mathcal{L}^{\otimes n})$ ($n > 0$), the $X_{s}$ form a basis for the topology of $X$ (4.5.2,
a), so by hypothesis the $j^{-1}(X_{s})$ form a basis for the topology of $X'$. By Lemma (4.6.13.1, (i)) and (4.5.2, a),
$j*(\mathcal{L})$ is ample.

Now we prove (iii). We may again suppose $Y$, $Y'$ affine (4.6.4), whence the projection $h : X' \to X$ is affine
(1.5.5). Since $\mathcal{L}$ is ample (4.6.6), as $s$ ranges over the sections of the $\mathcal{L}^{\otimes n}$ ($n >
0$) over $X$ such that $X_{s}$ is affine, the $X_{s}$ cover $X$ (4.5.2, a'), so the $h^{-1}(X_{s})$ are affine (1.2.5)
and cover $X'$; it follows again from Lemma (4.6.13.1, (i)) and (4.5.2, a') that $\mathcal{L}'$ is ample, the morphism
$f_{(Y')}$ being quasi-compact `(I, 6.6.4, (iii))`.

To prove (iv), note first that $f_{1} \times_{S} f_{2}$ is quasi-compact `(I, 6.6.4, (iv))`. We may further suppose $S$,
`Y_1`, `Y_2` affine ((4.6.4) and `(I, 3.2.7)`), hence $\mathcal{L}_{i}$ ample ($i = 1, 2$) (4.6.6). The opens
$(X_{1})_{s_{1}} \times_{S} (X_{2})_{s_{2}}$ form a cover of $X_{1} \times_{S} X_{2}$ as $s_{i}$ ranges over the
sections of $\mathcal{L}^{\otimes n_{i}}_{i}$ such that $(X_{i})_{s_{i}}$ is affine (4.5.2, a'). Replacing $s_{1}$ and
$s_{2}$ by suitable powers (which does not change the $(X_{i})_{s_{i}}$), we may always suppose $n_{1} = n_{2}$. We
deduce from (4.6.13.1, (ii)) and (4.5.2, a') that $\mathcal{L}_{1} \otimes_{S} \mathcal{L}_{2}$ is ample, whence the
assertion, since $Y_{1} \times_{S} Y_{2}$ is affine (4.6.6).

It remains to prove (ii). By the same argument as in (4.4.10), but using (4.6.4) here, we may restrict to the case $Z$
affine. Since $\mathcal{K}$ is then ample, and $Y$ quasi-compact, there are finitely many sections $s_{i} \in \Gamma(Y,
\mathcal{K}^{\otimes k_{i}})$ such that the $Y_{s_{i}}$

<!-- original page 93 -->

are _affine_ and cover $Y$ (4.5.2, a'); replacing the $s_{i}$ by suitable powers, we may further suppose all the $k_{i}$
equal to a single integer $k$. Let $s_{i}'$ be the sections of $f*(\mathcal{K}^{\otimes k})$ over $X$ canonically
corresponding to the $s_{i}$, so that the $X_{s_{i}'} = f^{-1}(Y_{s_{i}})$ (4.6.13.1, (i)) cover $X$. Since $\mathcal{L}
| X_{s_{i}'}$ is ample (4.6.4 and 4.6.6), there exist for each $i$ finitely many sections $t_{ij} \in \Gamma(X,
\mathcal{L}^{\otimes n_{ij}})$ such that the $X_{t_{ij}}$ are affine, contained in $X_{s_{i}'}$, and cover $X_{s_{i}'}$
(4.5.2, a'); we may further suppose all the $n_{ij}$ equal to a single integer $n$. With this, $X$ is separated and
quasi-compact, so there exists an integer $m > 0$ and, for every $(i, j)$, a section

```text
  u_{ij} ∈ Γ(X, ℒ^{⊗n} ⊗_X f*(𝒦^{⊗mk}))
```

such that $t_{ij} \otimes s_{i}'^{\otimes m}$ is the restriction to $X_{s_{i}'}$ of $u_{ij}$ `(I, 9.3.1)`; moreover
$X_{u_{ij}} = X_{t_{ij}}$, so the $X_{u_{ij}}$ are affine and cover $X$. We may also suppose $m$ is of the form `nr`;
setting $n_{0} = rk$, we see (4.5.2, a') that $\mathcal{L} \otimes_{\mathcal{O}_{X}} f*(\mathcal{K}^{\otimes n_{0}})$ is
ample. Furthermore, there exists $h_{0} > 0$ such that $\mathcal{K}^{\otimes h}$ is generated by its sections over $Y$
for every $h \geq h_{0}$ (4.5.5); _a fortiori_ $f*(\mathcal{K}^{\otimes h})$ is generated by its sections over $X$ for
$h \geq h_{0}$, by the definition of inverse images `(0, 3.7.1 and 4.4.1)`. We conclude that $\mathcal{L} \otimes
f*(\mathcal{K}^{\otimes(n_{0} + h)})$ is ample for every $h \geq h_{0}$ (4.5.6), which completes the proof.

**Remark.**

<!-- label: II.4.6.14 -->

Under the conditions of (ii), one should refrain from believing that $\mathcal{L} \otimes f*(\mathcal{K})$ is ample for
$g \circ f$: indeed, since $\mathcal{L} \otimes f*(\mathcal{K}^{-1})$ is also ample for $f$ (4.6.5), one would conclude
that $\mathcal{L}$ is ample for $g \circ f$; taking in particular $g$ to be the identity morphism, _every_ invertible
$\mathcal{O}_{X}$-module would be ample for $f$, which is not the case in general (see (5.1.6), (5.3.4, (i)), and
(5.3.1)).

**Proposition.**

<!-- label: II.4.6.15 -->

Let $f : X \to Y$ be a quasi-compact morphism, $\mathcal{J}$ a quasi-coherent locally nilpotent sheaf of ideals of
$\mathcal{O}_{X}$, $Z$ the closed subprescheme of $X$ defined by $\mathcal{J}$, and $j : Z \to X$ the canonical
injection. For an invertible $\mathcal{O}_{X}$-module $\mathcal{L}$ to be ample for $f$, it is necessary and sufficient
that $j*(\mathcal{L})$ be ample for $f \circ j$.

**Proof.** The question being local on $Y$ (4.6.4), we may suppose $Y$ affine; since $X$ is then quasi-compact, we may
suppose $\mathcal{J}$ nilpotent. Taking (4.6.6) into account, the proposition is then nothing but (4.5.13).

**Corollary.**

<!-- label: II.4.6.16 -->

Let $X$ be a locally Noetherian prescheme, $f : X \to Y$ a quasi-compact morphism. For an invertible
$\mathcal{O}_{X}$-module $\mathcal{L}$ to be ample for $f$, it is necessary and sufficient that its inverse image
$\mathcal{L}'$ under the canonical injection $X_{red} \to X$ be ample for $f_{red}$.

**Proof.** We have already seen that the condition is necessary (4.6.13, (vi)); conversely, if it is satisfied, we may
restrict, to prove that $\mathcal{L}$ is ample for $f$, to the case $Y$ affine (4.6.4); then $Y_{red}$ is also affine,
so $\mathcal{L}'$ is ample (4.6.6), and so is $\mathcal{L}$ by (4.5.13), since $X$ is then Noetherian and $X_{red}$ a
closed subprescheme of $X$ defined by a quasi-coherent nilpotent sheaf of ideals `(I, 6.1.6)`.

**Proposition.**

<!-- label: II.4.6.17 -->

With the notation and hypotheses of (4.4.11), for $\mathcal{L}''$ to be ample relative to `f''`, it is necessary and
sufficient that $\mathcal{L}$ be ample relative to $f$ and $\mathcal{L}'$ ample relative to $f'$.

<!-- original page 94 -->

**Proof.** The necessity of the condition follows from (4.6.13, (i bis)). To see that the condition is sufficient, we
may restrict to $Y$ affine, and then the fact that $\mathcal{L}''$ is ample follows from criterion (4.5.2, a) applied to
$\mathcal{L}$, $\mathcal{L}'$, and $\mathcal{L}''$, observing that a section of $\mathcal{L}$ over $X$ extends (by `0`)
to a section of $\mathcal{L}''$ over `X''`.

**Proposition.**

<!-- label: II.4.6.18 -->

Let $Y$ be a quasi-compact prescheme, $\mathcal{S}$ a quasi-coherent graded $\mathcal{O}_{Y}$-algebra of finite type, $X
= \operatorname{Proj}(\mathcal{S})$, and $f : X \to Y$ the structure morphism. Then $f$ is of finite type, and there
exists an integer $d > 0$ such that $\mathcal{O}_{X}(d)$ is invertible and $f$-ample.

**Proof.** By (3.1.10), there exists an integer $d > 0$ such that $\mathcal{S}^{(d)}$ is generated by $\mathcal{S}_{d}$.
Under the canonical isomorphism between $X$ and $X^{(d)} = \operatorname{Proj}(\mathcal{S}^{(d)})$, $\mathcal{O}_{X}(d)$
is identified with $\mathcal{O}_{X^{(d)}}(1)$ (3.2.9, (ii)). We see that we are reduced to the case where $\mathcal{S}$
is generated by $\mathcal{S}_{1}$; the proposition then follows from (4.4.3) and (4.6.2) (taking into account that $f$
is a morphism of finite type (3.4.1)).

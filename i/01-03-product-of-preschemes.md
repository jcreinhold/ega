# §3. Product of Preschemes

<!-- label: I.3 -->

## 3.1. Sums of preschemes

<!-- label: I.3.1 -->

**(3.1.1)** Let $(X_{\alpha})$ be an arbitrary family of preschemes, and let $X$ be a topological space that is the sum
of the underlying spaces $X_{\alpha}$; thus $X$ is the union of pairwise disjoint open subspaces $X'_{\alpha}$, and for
each $\alpha$ there is a homeomorphism $\varphi_{\alpha} : X_{\alpha} \to X'_{\alpha}$. If each $X'_{\alpha}$ is
equipped with the sheaf $(\varphi_{\alpha})_{*}(\mathcal{O}_{X_{\alpha}})$, it is clear that $X$ becomes a prescheme,
called the _sum_ of the family $(X_{\alpha})$ and written $\coprod_{\alpha} X_{\alpha}$. If $Y$ is a prescheme, the map
$f \mapsto (f \circ \varphi_{\alpha})$ is a bijection of $\operatorname{Hom}(X, Y)$ onto the product set $\prod_{\alpha}
\operatorname{Hom}(X_{\alpha}, Y)$. In particular, if the $X_{\alpha}$ are $S$-preschemes with structure morphisms
$\psi_{\alpha}$, then $X$ is an $S$-prescheme for the unique morphism $\psi : X \to S$ such that $\psi \circ
\varphi_{\alpha} = \psi_{\alpha}$ for every $\alpha$; that is, $X$ is the coproduct in the category of $S$-preschemes.
The sum of two preschemes $X$, $Y$ is written $X \amalg Y$. It is immediate that if $X = \operatorname{Spec}(A)$ and $Y
= \operatorname{Spec}(B)$, then $X \amalg Y$ is canonically identified with $\operatorname{Spec}(A \times B)$.

## 3.2. Products of preschemes

<!-- label: I.3.2 -->

**Definition (3.2.1).** Given two $S$-preschemes $X$, $Y$, a triple $(Z, p_{1}, p_{2})$ formed of an $S$-prescheme $Z$
and two $S$-morphisms $p_{1} : Z \to X$, $p_{2} : Z \to Y$ is called a _product of the $S$-preschemes $X$ and $Y$_ if,
for every $S$-prescheme $T$, the map $f \mapsto (p_{1} \circ f, p_{2} \circ f)$ is a bijection of the set of
$S$-morphisms $T \to Z$ onto the set of pairs formed of an $S$-morphism $T \to X$ and an $S$-morphism $T \to Y$; in
other words, a bijection

$$ \operatorname{Hom}_{S}(T, Z) \xrightarrow{\sim} \operatorname{Hom}_{S}(T, X) \times \operatorname{Hom}_{S}(T, Y). $$

This is thus the general notion of the product of two objects of a category (T, I, 1.1) applied to the category of
$S$-preschemes; in particular, a product of two $S$-preschemes is unique up to a unique $S$-isomorphism. Because of this
uniqueness, one usually denotes a product of two $S$-preschemes $X$, $Y$ by $X \times_{S} Y$ (or simply $X \times Y$
when no confusion can arise), the projections $p_{1}$, $p_{2}$ — called the _canonical projections_ of $X \times_{S} Y$
onto $X$ and $Y$ respectively — being suppressed from the notation. If $g : T \to X$, $h : T \to Y$ are two
$S$-morphisms, we write $(g, h)_{S}$, or simply $(g, h)$, for the $S$-morphism $f : T \to X \times_{S} Y$ such that
$p_{1} \circ f = g$, $p_{2} \circ f = h$. If $X'$, $Y'$ are two $S$-preschemes with canonical projections $p'_{1}$,
$p'_{2}$ of $X' \times_{S} Y'$ (assumed to exist), and $u : X' \to X$, $v : Y' \to Y$ are $S$-morphisms, we write $u
\times_{S} v$ (or simply $u \times v$) for the $S$-morphism $(u \circ p'_{1}, v \circ p'_{2})_{S}$ of $X' \times_{S} Y'$
into $X \times_{S} Y$.

When $S$ is an affine scheme with ring $A$, one often replaces $S$ by $A$ in the preceding notation.

**Proposition (3.2.2).** Let $X$, $Y$, $S$ be three affine schemes, with respective rings $B$, $C$, $A$. Let $Z =
\operatorname{Spec}(B \otimes_{A} C)$, and let $p_{1}$, $p_{2}$ be the $S$-morphisms corresponding (2.2.4) to the
canonical $A$-homomorphisms $u : b \mapsto b \otimes 1$ and $v : c \mapsto 1 \otimes c$ of $B$ and $C$ into $B
\otimes_{A} C$. Then $(Z, p_{1}, p_{2})$ is a product of $X$ and $Y$.

**Proof.** By (2.2.4), everything reduces to checking that, by associating to each $A$-homomorphism $f : B \otimes_{A} C
\to L$ (where $L$ is an $A$-algebra) the pair $(f \circ u, f \circ v)$, one defines a bijection
$\operatorname{Hom}_{A}(B \otimes_{A} C, L) \xrightarrow{\sim} \operatorname{Hom}_{A}(B, L) \times
\operatorname{Hom}_{A}(C, L)$[^I-3-1]; this is immediate from the definitions and the relation $b \otimes c = (b \otimes
1)(1 \otimes c)$.

**Corollary (3.2.3).** Let $T$ be an affine scheme with ring $D$, and let $\xi = ({}^{a}\rho, \ldots)$ (resp. $\zeta =
({}^{a}\sigma, \ldots)$) be an $S$-morphism $T \to X$ (resp. $T \to Y$), where $\rho$ (resp. $\sigma$) is an
$A$-homomorphism of $B$ (resp. $C$) into $D$. Then $(\xi, \zeta)_{S} = {}^{a}\tau$, where $\tau : B \otimes_{A} C \to D$
is the homomorphism such that $\tau(b \otimes c) = \rho(b)\sigma(c)$.

**Proposition (3.2.4).** Let $f : S' \to S$ be a monomorphism of preschemes (T, I, 1.1), and let $X$, $Y$ be two
$S'$-preschemes, regarded also as $S$-preschemes by means of $f$. Then every product of the $S$-preschemes $X$, $Y$ is a
product of the $S'$-preschemes $X$, $Y$, and conversely.

**Proof.** Let $\varphi : X \to S'$, $\psi : Y \to S'$ be the structure morphisms. If $T$ is an $S$-prescheme and $u : T
\to X$, $v : T \to Y$ are two $S$-morphisms, then by definition $f \circ \varphi \circ u = f \circ \psi \circ v =
\theta$, the structure morphism of $T$; the hypothesis on $f$ gives $\varphi \circ u = \psi \circ v = \theta'$, and one
sees that $T$ may be regarded as an $S'$-prescheme with structure morphism $\theta'$, and $u$, $v$ as $S'$-morphisms.
The conclusion follows at once, taking (3.2.1) into account.

**Corollary (3.2.5).** Let $X$, $Y$ be two $S$-preschemes with structure morphisms $\varphi : X \to S$, $\psi : Y \to
S$, and let $S'$ be an open subset of $S$ such that $\varphi(X) \subset S'$, $\psi(Y) \subset S'$. Then every product of
the $S$-preschemes $X$, $Y$ is also a product of the $S'$-preschemes $X$, $Y$, and conversely.

**Proof.** It suffices to apply (3.2.4) to the canonical injection $S' \to S$.

**Theorem (3.2.6).** Given two $S$-preschemes $X$, $Y$, a product $X \times_{S} Y$ exists.

We proceed in several steps.

**Lemma (3.2.6.1).** Let $(Z, p, q)$ be a product of $X$ and $Y$, and let $U$, $V$ be open subsets of $X$, $Y$
respectively. If $W = p^{-1}(U) \cap q^{-1}(V)$, then the triple formed of $W$ and the restrictions of $p$ and $q$ to
$W$ (regarded as morphisms $W \to U$, $W \to V$) is a product of $U$ and $V$.

**Proof.** If $T$ is an $S$-prescheme, the $S$-morphisms $T \to W$ may be identified with the $S$-morphisms $T \to Z$
whose image lies in $W$. If $g : T \to U$, $h : T \to V$ are two $S$-morphisms, they may be regarded as $S$-morphisms of
$T$ into $X$ and $Y$ respectively, so by hypothesis there is a unique $S$-morphism $f : T \to Z$ with $g = p \circ f$,
$h = q \circ f$. Since $p(f(T)) \subset U$ and $q(f(T)) \subset V$, we have $f(T) \subset p^{-1}(U) \cap q^{-1}(V) = W$,
whence the assertion.

**Lemma (3.2.6.2).** Let $Z$ be an $S$-prescheme, $p : Z \to X$, $q : Z \to Y$ two $S$-morphisms, $(U_{\alpha})$ an open
cover of $X$, and $(V_{\lambda})$ an open cover of $Y$. Suppose that for every pair $(\alpha, \lambda)$ the
$S$-prescheme $W_{\alpha\lambda} = p^{-1}(U_{\alpha}) \cap q^{-1}(V_{\lambda})$, with the restrictions of $p$ and $q$,
constitutes a product of $U_{\alpha}$ and $V_{\lambda}$. Then $(Z, p, q)$ is a product of $X$ and $Y$.

**Proof.** We first show that if $f_{1}$, $f_{2}$ are two $S$-morphisms $T \to Z$, then $p \circ f_{1} = p \circ f_{2}$
and $q \circ f_{1} = q \circ f_{2}$ imply $f_{1} = f_{2}$. Indeed, $Z$ is the union of the $W_{\alpha\lambda}$, so the
$f_{1}^{-1}(W_{\alpha\lambda})$ form an open cover of $T$, as do the $f_{2}^{-1}(W_{\alpha\lambda})$; moreover
$f_{1}^{-1}(W_{\alpha\lambda}) = f_{2}^{-1}(W_{\alpha\lambda})$ by the hypotheses, so it suffices to see that the
restrictions of $f_{1}$ and $f_{2}$ to this open set agree for each pair of indices. But these restrictions may be
regarded as $S$-morphisms into $W_{\alpha\lambda}$, so the assertion follows from the hypotheses and (3.2.1). Now
suppose given two $S$-morphisms $g : T \to X$, $h : T \to Y$. Set $T_{\alpha\lambda} = g^{-1}(U_{\alpha}) \cap
h^{-1}(V_{\lambda})$; the $T_{\alpha\lambda}$ form an open cover of $T$. By hypothesis there is an $S$-morphism
$f_{\alpha\lambda}$ such that $p \circ f_{\alpha\lambda}$ and $q \circ f_{\alpha\lambda}$ are the restrictions of $g$
and $h$ to $T_{\alpha\lambda}$. The restrictions of $f_{\alpha\lambda}$ and $f_{\beta\mu}$ to $T_{\alpha\lambda} \cap
T_{\beta\mu}$ coincide: their images lie in $W_{\alpha\lambda} \cap W_{\beta\mu}$, and since by (3.2.6.1) this open set
is a product of $U_{\alpha} \cap U_{\beta}$ and $V_{\lambda} \cap V_{\mu}$, the equality of $p \circ f_{\alpha\lambda}$
with $p \circ f_{\beta\mu}$ and of $q \circ f_{\alpha\lambda}$ with $q \circ f_{\beta\mu}$ there forces the two
restrictions to agree. The $f_{\alpha\lambda}$ therefore glue to an $S$-morphism $f : T \to Z$ with $g = p \circ f$, $h
= q \circ f$, which proves (3.2.6.2).

**(3.2.6.3)** Let $(U_{\alpha})$ be an open cover of $X$ and $(V_{\lambda})$ an open cover of $Y$, and suppose that for
every pair $(\alpha, \lambda)$ a product of $U_{\alpha}$ and $V_{\lambda}$ exists. Then a product of $X$ and $Y$ exists.

**Proof.** Applying (3.2.6.1) to the open sets $U_{\alpha} \cap U_{\beta}$ and $V_{\lambda} \cap V_{\mu}$, one sees that
a product of the induced $S$-preschemes exists; the uniqueness of the product yields canonical gluing isomorphisms
$f_{ij}$ between the overlaps (writing $i = (\alpha, \lambda)$, $j = (\beta, \mu)$) satisfying the cocycle condition
$f_{ik} = f_{jk} \circ f_{ij}$, by (3.2.6.1) applied to triple intersections. By the gluing of preschemes (2.3.1) there
is a prescheme $Z$, an open cover $(Z_{i})$, and isomorphisms $g_{i}$ of the induced prescheme $Z_{i}$ onto $U_{\alpha}
\times_{S} V_{\lambda}$ with $f_{ij} = g_{i} \circ g_{j}^{-1}$ and $g_{i}(Z_{i} \cap Z_{j}) = W_{ij}$. The projections
and structure morphisms of the $U_{\alpha} \times_{S} V_{\lambda}$ glue to morphisms $p : Z \to X$, $q : Z \to Y$,
$\theta : Z \to S$ coinciding with $p_{i} \circ g_{i}$, $q_{i} \circ g_{i}$, $\theta_{i} \circ g_{i}$ on each $Z_{i}$;
this makes $Z$ an $S$-prescheme. One checks (using (3.2.6.1) and uniqueness of products) that $p^{-1}(U_{\alpha}) \cap
q^{-1}(V_{\lambda}) = Z_{i}$, so by (3.2.6.2) $(Z, p, q)$ is a product of $X$ and $Y$.

**(3.2.6.4)** Let $\varphi : X \to S$, $\psi : Y \to S$ be the structure morphisms of $X$ and $Y$, let $(S_{i})$ be an
open cover of $S$, and set $X_{i} = \varphi^{-1}(S_{i})$, $Y_{i} = \psi^{-1}(S_{i})$. If each product $X_{i} \times_{S}
Y_{i}$ exists, then $X \times_{S} Y$ exists.

**Proof.** By (3.2.6.3) it suffices to prove that the products $X_{i} \times_{S} Y_{j}$ exist for all $i$, $j$. Set
$X_{ij} = X_{i} \cap X_{j} = \varphi^{-1}(S_{i} \cap S_{j})$, $Y_{ij} = Y_{i} \cap Y_{j} = \psi^{-1}(S_{i} \cap S_{j})$;
by (3.2.6.1) the product $Z_{ij} = X_{ij} \times_{S} Y_{ij}$ exists. If $T$ is an $S$-prescheme and $g : T \to X_{i}$, $h
: T \to Y_{j}$ are $S$-morphisms, then necessarily $\varphi(g(T)) = \psi(h(T)) \subset S_{i} \cap S_{j}$ by the
definition of an $S$-morphism, so $g(T) \subset X_{ij}$ and $h(T) \subset Y_{ij}$; it is then immediate that $Z_{ij}$ is
a product of $X_{i}$ and $Y_{j}$.

**(3.2.6.5)** We can now complete the proof of (3.2.6). If $S$ is an affine scheme, there are covers $(U_{\alpha})$,
$(V_{\lambda})$ of $X$ and $Y$ by affine opens; since $U_{\alpha} \times_{S} V_{\lambda}$ exists by (3.2.2), so does $X
\times_{S} Y$ by (3.2.6.3). If $S$ is an arbitrary prescheme, take a cover $(S_{i})$ of $S$ by affine opens; with $X_{i}
= \varphi^{-1}(S_{i})$, $Y_{i} = \psi^{-1}(S_{i})$, the products $X_{i} \times_{S_{i}} Y_{i}$ exist by the foregoing,
and then $X_{i} \times_{S} Y_{i}$ exists too by (3.2.5), so $X \times_{S} Y$ exists by (3.2.6.4). $\square$

**Corollary (3.2.7).** Let $Z = X \times_{S} Y$ be the product of two $S$-preschemes, $p$, $q$ its projections, and
$\varphi$ (resp. $\psi$) the structure morphism of $X$ (resp. $Y$). Let $S'$ be an open subset of $S$, and $U$ (resp.
$V$) an open subset of $X$ (resp. $Y$) contained in $\varphi^{-1}(S')$ (resp. $\psi^{-1}(S')$). Then the product $U
\times_{S'} V$ is canonically identified with the prescheme induced by $Z$ on $p^{-1}(U) \cap q^{-1}(V)$ (regarded as an
$S'$-prescheme). Moreover, if $f : T \to X$, $g : T \to Y$ are $S$-morphisms with $f(T) \subset U$, $g(T) \subset V$,
then the $S'$-morphism $(f, g)_{S'}$ is identified with the restriction of $(f, g)_{S}$. This follows from (3.2.5) and
(3.2.6.1).

**(3.2.8)** Let $(X_{\alpha})$, $(Y_{\lambda})$ be two families of $S$-preschemes, and $X$ (resp. $Y$) the sum of the
family $(X_{\alpha})$ (resp. $(Y_{\lambda})$) (3.1). Then $X \times_{S} Y$ is identified with the sum of the family
$(X_{\alpha} \times_{S} Y_{\lambda})$; this follows at once from (3.2.6.3).

## 3.3. Formal properties of the product; change of base prescheme

<!-- label: I.3.3 -->

**(3.3.1)** The reader will note that all the properties stated in this section, except (3.3.13) and (3.3.15), hold
without change in any category, whenever the products that occur in the statements exist (for it is clear that the
notions of $S$-object and $S$-morphism can be defined exactly as in (2.5) for any object $S$ of the category).

**(3.3.2)** First, $X \times_{S} Y$ is a covariant bifunctor in $X$ and $Y$ on the category of $S$-preschemes: it
suffices to remark that the diagram

$$
\begin{array}{ccc}
X \times_{S} Y & \to & X' \times_{S} Y \to X'' \times_{S} Y \\
\downarrow & & \downarrow \\
X & \to & X' \to X''
\end{array}
$$

is commutative.

**Proposition (3.3.3).** For every $S$-prescheme $X$, the first (resp. second) projection of $X \times_{S} S$ (resp. $S
\times_{S} X$) is a functorial isomorphism of $X \times_{S} S$ (resp. $S \times_{S} X$) onto $X$, whose inverse is
$(1_{X}, \varphi)_{S}$ (resp. $(\varphi, 1_{X})_{S}$), where $\varphi$ denotes the structure morphism $X \to S$. One may
therefore write, up to a canonical isomorphism, $$ X \times_{S} S = S \times_{S} X = X. $$

**Proof.** It suffices to prove that the triple $(X, 1_{X}, \varphi)$ is a product of $X$ and $S$. If $T$ is an
$S$-prescheme, the only $S$-morphism of $T$ into $S$ is necessarily the structure morphism $\theta : T \to S$. If $f$ is
an $S$-morphism of $T$ into $X$, then necessarily $\theta = \varphi \circ f$, whence the assertion.

**Corollary (3.3.4).** Let $X$, $Y$ be two $S$-preschemes with structure morphisms $\varphi : X \to S$, $\psi : Y \to
S$. If one identifies $X$ with $X \times_{S} S$ and $Y$ with $S \times_{S} Y$, the projections $X \times_{S} Y \to X$
and $X \times_{S} Y \to Y$ are identified with $1_{X} \times_{S} \psi$ and $\varphi \times_{S} 1_{Y}$ respectively. (The
verification is immediate and left to the reader.)

**(3.3.5)** One may define, in the same way as in (3.2), the product of any finite number $n$ of $S$-preschemes; the
existence of these products follows from (3.2.6) by induction on $n$, on remarking that $(X_{1} \times_{S} \cdots
\times_{S} X_{n-1}) \times_{S} X_{n}$ satisfies the definition of the product. Uniqueness of the product entails, as in
any category, its commutativity and associativity properties. For example, if $p_{1}$, $p_{2}$, $p_{3}$ denote the
projections of $X_{1} \times_{S} X_{2} \times_{S} X_{3}$, and one identifies this prescheme with $(X_{1} \times_{S}
X_{2}) \times_{S} X_{3}$, then the projection onto $X_{1} \times_{S} X_{2}$ is identified with $(p_{1}, p_{2})_{S}$.

**(3.3.6)** Let $S$, $S'$ be two preschemes and $\varphi : S' \to S$ a morphism, making $S'$ an $S$-prescheme. For every
$S$-prescheme $X$, consider the product $X \times_{S} S'$, and let $p$ and $\pi'$ be its projections onto $X$ and $S'$
respectively. Equipped with $\pi'$, this product is an $S'$-prescheme; regarded as such, it is denoted $X_{(S')}$ or
$X_{(\varphi)}$, and one says it is the prescheme _obtained by extension of the base prescheme from $S$ to $S'$, by
means of $\varphi$_, or the _inverse image of $X$ by $\varphi$_. Note that if $\pi$ is the structure morphism of $X$ and
$\theta$ the structure morphism of $X \times_{S} S'$ regarded as an $S$-prescheme, the corresponding square is
commutative.

**(3.3.7)** With the notation of (3.3.6), for every $S$-morphism $f : X \to Y$ one writes $f_{(S')}$ for the
$S'$-morphism $f \times_{S} 1 : X_{(S')} \to Y_{(S')}$, and one says $f_{(S')}$ is the _inverse image of the morphism
$f$ by $\varphi$_. Thus $X_{(S')}$ is a covariant functor in $X$, from the category of $S$-preschemes to that of
$S'$-preschemes.

**(3.3.8)** The prescheme $X_{(S')}$ may also be regarded as the solution of a universal mapping problem: every
$S'$-prescheme $T$ is also an $S$-prescheme by means of $\varphi$; every $S$-morphism $g : T \to X$ then factors
uniquely as $g = p \circ f$, where $f$ is an $S'$-morphism $T \to X_{(S')}$, as follows from the definition of the
product applied to the $S$-morphisms $f$ and $\theta : T \to S'$ (the structure morphism of $T$).

**Proposition (3.3.9)** _(transitivity of extension of the base prescheme)._ Let $S''$ be a prescheme and $\varphi' :
S'' \to S'$ a morphism. For every $S$-prescheme $X$, there is a canonical functorial isomorphism of the $S''$-prescheme
$(X_{(S')})_{(S'')}$ onto the $S''$-prescheme $X_{(S'')}$.

**Proof.** Let $T$ be an $S''$-prescheme with structure morphism $\zeta$, and $g$ an $S$-morphism of $T$ into $X$ ($T$
being regarded as an $S$-prescheme with structure morphism $\varphi \circ \varphi' \circ \zeta$). Since $T$ is also an
$S'$-prescheme with structure morphism $\varphi' \circ \zeta$, one may write $g = p \circ g'$, where $g'$ is an
$S'$-morphism $T \to X_{(S')}$, then $g' = p' \circ g''$, where $g''$ is an $S''$-morphism $T \to (X_{(S')})_{(S'')}$.
The proposition follows from the uniqueness of the solution of a universal mapping problem.

This result is also expressed by writing the equality (up to canonical isomorphism) $(X_{(S')})_{(S'')} = X_{(S'')}$, or
again $$ (X \times_{S} S') \times_{S'} S'' = X \times_{S} S''. \tag{3.3.9.1} $$ The functorial character of the
isomorphism is expressed by the transitivity formula for inverse images of morphisms $$ (f_{(S')})_{(S'')} = f_{(S'')}
\tag{3.3.9.2} $$ for every $S$-morphism $f : X \to Y$.

**Corollary (3.3.10).** If $X$ and $Y$ are two $S$-preschemes, there is a canonical functorial isomorphism of the
$S'$-prescheme $X_{(S')} \times_{S'} Y_{(S')}$ onto the $S'$-prescheme $(X \times_{S} Y)_{(S')}$.

**Proof.** Up to canonical isomorphisms, $$ (X \times_{S} S') \times_{S'} (Y \times_{S} S') = X \times_{S} (Y \times_{S}
S') = (X \times_{S} Y) \times_{S} S' $$ by (3.3.9.1) and the associativity of products of $S$-preschemes. The functorial
character is expressed by $$ (u_{(S')}, v_{(S')})_{S'} = ((u, v)_{S})_{(S')} \tag{3.3.10.1} $$ for every pair of
$S$-morphisms $u : T \to X$, $v : T \to Y$. In other words, the inverse-image functor $X \mapsto X_{(S')}$ commutes with
the formation of products; it also commutes with the formation of sums (3.2.8).

**Corollary (3.3.11).** Let $Y$ be an $S$-prescheme and $f : X \to Y$ a morphism making $X$ a $Y$-prescheme (and hence
also an $S$-prescheme). Then $X_{(S')}$ is identified with the product $X \times_{Y} Y_{(S')}$, the projection $X
\times_{Y} Y_{(S')} \to Y_{(S')}$ being identified with $f_{(S')}$.

**Proof.** Let $\psi : Y \to S$ be the structure morphism of $Y$. Since $Y_{(S')}$ is identified with $S'_{(\ldots)}$
and $X_{(S')}$ with the corresponding base change, the assertion follows from (3.3.9) and (3.3.4) via the commutative
diagram relating the morphisms $f$, $\psi$, and $\varphi$.

**(3.3.12)** Let $f : X \to X'$, $g : Y \to Y'$ be two $S$-morphisms that are monomorphisms of preschemes (T, I, 1.1);
then $f \times_{S} g$ is a monomorphism. Indeed, if $p$, $q$ are the projections of $X \times_{S} Y$, $p'$, $q'$ those
of $X' \times_{S} Y'$, and $u$, $v$ two $S$-morphisms $T \to X \times_{S} Y$, the relation $(f \times_{S} g) \circ u =
(f \times_{S} g) \circ v$ gives $p' \circ (f \times_{S} g) \circ u = p' \circ (f \times_{S} g) \circ v$, i.e. $f \circ p
\circ u = f \circ p \circ v$, and since $f$ is a monomorphism, $p \circ u = p \circ v$; likewise $q \circ u = q \circ
v$, whence $u = v$. It follows that for every extension $S' \to S$ of the base prescheme, $f_{(S')} : X_{(S')} \to
X'_{(S')}$ is a monomorphism.

**(3.3.13)** Let $S$, $S'$ be two affine schemes with respective rings $A$, $A'$; a morphism $S' \to S$ thus corresponds
to a ring homomorphism $A \to A'$. If $X$ is an $S$-prescheme, one also writes $X_{(A')}$ or $X \otimes_{A} A'$ for the
$S'$-prescheme $X_{(S')}$; when $X$ is itself affine with ring $B$, $X_{(A')}$ is affine with ring $B_{(A')} = B
\otimes_{A} A'$, obtained by extension to $A'$ of the ring of scalars of the $A$-algebra $B$.

**(3.3.14)** With the notation of (3.3.6), for every $S$-morphism $f : S' \to X$, $f' = (f, 1_{S'})_{S}$ is an
$S$-morphism $S' \to X' = X_{(S')}$ such that $p \circ f' = f$ and $\pi' \circ f' = 1_{S'}$ — in other words, an
_$S'$-section of $X'$_; and conversely, if $f'$ is such an $S'$-section, then $f = p \circ f'$ is an $S$-morphism $S'
\to X$. One thus defines a canonical bijection $$ \operatorname{Hom}_{S}(S', X) \xrightarrow{\sim}
\operatorname{Hom}_{S'}(S', X'). $$ One says $f'$ is the _graph morphism_ of $f$, denoted $\Gamma_{f}$.

**(3.3.15)** Given a prescheme $X$, which may always be regarded as a $\mathbf{Z}$-prescheme, it follows in particular
from (3.3.14) that the $X$-sections of $X \otimes_{\mathbf{Z}} \mathbf{Z}[T]$ (where $T$ is an indeterminate) correspond
bijectively to the morphisms $\mathbf{Z}[T] \to X$. We show these $X$-sections also correspond bijectively to the
sections of the structure sheaf $\mathcal{O}_{X}$ over $X$. Let $(U_{\alpha})$ be a cover of $X$ by affine opens; let $u
: X \to X \otimes_{\mathbf{Z}} \mathbf{Z}[T]$ be an $X$-morphism and $u_{\alpha}$ its restriction to $U_{\alpha}$. If
$A_{\alpha}$ is the ring of the affine scheme $U_{\alpha}$, then $U_{\alpha} \otimes_{\mathbf{Z}} \mathbf{Z}[T]$ is
affine with ring $A_{\alpha}[T]$ (3.2.2), and $u_{\alpha}$ corresponds canonically to an $A_{\alpha}$-homomorphism
$A_{\alpha}[T] \to A_{\alpha}$ (1.7.3). Such a homomorphism is completely determined by the image $s_{\alpha} \in
A_{\alpha} = \Gamma(U_{\alpha}, \mathcal{O}_{X})$ of $T$; the compatibility of $u_{\alpha}$ and $u_{\beta}$ on overlaps
shows the $s_{\alpha}$ are the restrictions of a section $s$ of $\mathcal{O}_{X}$ over $X$, and conversely. This result
will be generalized in (II, 1.7.12).

## 3.4. Points of a prescheme with values in a prescheme; geometric points

<!-- label: I.3.4 -->

**(3.4.1)** Let $X$ be a prescheme. For every prescheme $T$, one writes $X(T)$ for the set $\operatorname{Hom}(T, X)$ of
morphisms $T \to X$, and the elements of this set are called _points of $X$ with values in $T$_. Associating to each
morphism $f : T \to T'$ the map $u' \mapsto u' \circ f$ of $X(T')$ into $X(T)$, one sees that, for fixed $X$, $X(T)$ is
a contravariant functor in $T$ from preschemes to sets. Moreover, every morphism $g : X \to Y$ defines a functorial
homomorphism $X(T) \to Y(T)$, sending $u \in X(T)$ to $g \circ u$.

**(3.4.2)** Given three sets $P$, $Q$, $R$ and two maps $\varphi : P \to R$, $\psi : Q \to R$, the _fiber product of $P$
and $Q$ over $R$_ (relative to $\varphi$ and $\psi$) is the subset of $P \times Q$ formed of the pairs $(p, q)$ with
$\varphi(p) = \psi(q)$; it is written $P \times_{R} Q$. Definition (3.2.1) of the product of $S$-preschemes may be
reinterpreted, with the notation of (3.4.1), by the formula $$ (X \times_{S} Y)(T) = X(T) \times_{S(T)} Y(T),
\tag{3.4.2.1} $$ the maps $X(T) \to S(T)$ and $Y(T) \to S(T)$ corresponding to the structure morphisms $X \to S$ and $Y
\to S$.

**(3.4.3)** If one fixes a prescheme $S$ and considers only $S$-preschemes and $S$-morphisms, one writes $X(T)_{S}$ for
the set $\operatorname{Hom}_{S}(T, X)$ of $S$-morphisms $T \to X$ (suppressing the index $S$ when no confusion is
possible); the elements of $X(T)_{S}$ are the _$S$-points_ of the $S$-prescheme $X$ with values in $T$. In particular,
an $S$-section of $X$ is nothing but a point of $X$ with values in $S$. Formula (3.4.2.1) then reads $$ (X \times_{S}
Y)(T)_{S} = X(T)_{S} \times Y(T)_{S}; \tag{3.4.3.1} $$ more generally, if $Z$ is an $S$-prescheme and $X$, $Y$, $T$ are
$Z$-preschemes (hence ipso facto $S$-preschemes), $$ (X \times_{Z} Y)(T)_{S} = X(T)_{S} \times_{Z(T)_{S}} Y(T)_{S}.
\tag{3.4.3.2} $$ To prove that a triple $(W, r, s)$ is a product of $X$ and $Y$ over $Z$, it suffices to verify that for
every $S$-prescheme $T$, the corresponding diagram makes $W(T)_{S}$ the fiber product of $X(T)_{S}$ and $Y(T)_{S}$ over
$Z(T)_{S}$.

**(3.4.4)** When $T$ (resp. $S$) is an affine scheme with ring $B$ (resp. $A$), one replaces $T$ (resp. $S$) by $B$
(resp. $A$) in the preceding notation, and speaks of _points of $X$ with values in the ring $B$_, or of _points of the
$A$-prescheme $X$ with values in the $A$-algebra $B$_, for the elements of $X(B)$ and $X(B)_{A}$ respectively. Note that
$X(B)$ and $X(B)_{A}$ are now covariant functors in $B$. One likewise writes $X(T)_{A}$ for the set of points of the
$A$-prescheme $X$ with values in the $A$-prescheme $T$.

**(3.4.5)** Consider the case where $T = \operatorname{Spec}(A)$ with $A$ a local ring; the elements of $X(A)$ then
correspond bijectively to the local homomorphisms $\mathcal{O}_{x} \to A$ for $x \in X$ (2.4.4), and one says the point
$x$ is the _locality_ of the corresponding point of $X$ with values in $A$. More particularly, one calls _geometric
points_ of a prescheme $X$ the points of $X$ with values in a field $K$: giving such a point amounts to giving its
locality $x$ in the underlying space of $X$ together with an extension $K$ of $\kappa(x)$. $K$ is called the _value
field_ of the geometric point, which is said to be _localized at $x$_. One thus defines a map $X(K) \to X$ sending a
geometric point to its locality. If $S' = \operatorname{Spec}(K)$ is an $S$-prescheme (i.e. $K$ is regarded as an
extension of a residue field $\kappa(s)$, $s \in S$) and $X$ is an $S$-prescheme, an element of $X(K)_{S}$ — a
_geometric point of $X$ above $s$ with values in $K$_ — consists of a $\kappa(s)$-monomorphism of a residue field
$\kappa(x)$ into $K$, where $x$ is a point of $X$ above $s$. In particular, if $S = \operatorname{Spec}(K) = \{\xi\}$,
the geometric points of $X$ with values in $K$ are identified with the points $x \in X$ such that $\kappa(x) = K$; these
are called the points of the $K$-prescheme $X$ _rational over $K$_.

**Lemma (3.4.6).** Let $X_{i}$ ($1 \le i \le n$) be $S$-preschemes, $s$ a point of $S$, and $x_{i}$ a point of $X_{i}$
above $s$. Then there exist an extension $K$ of $\kappa(s)$ and a geometric point of the product $Y = X_{1} \times_{S}
\cdots \times_{S} X_{n}$, with values in $K$, whose projections are localized at the $x_{i}$.

**Proof.** There exist $\kappa(s)$-monomorphisms $\kappa(x_{i}) \to K$ into a common extension $K$ of $\kappa(s)$
(Bourbaki, _Alg._, ch. V, §4, prop. 2). The composites $\kappa(s) \to \kappa(x_{i}) \to K$ are all the same, so the
morphisms $\operatorname{Spec}(K) \to X_{i}$ are $S$-morphisms and define a unique morphism $\operatorname{Spec}(K) \to
Y$. The corresponding point $y$ clearly projects to $x_{i}$ in each $X_{i}$.

**Proposition (3.4.7).** Let $X_{i}$ ($1 \le i \le n$) be $S$-preschemes, and for each $i$ let $x_{i}$ be a point of
$X_{i}$. For there to exist a point $y$ of $Y = X_{1} \times_{S} \cdots \times_{S} X_{n}$ whose $i$-th projection is
$x_{i}$ for $1 \le i \le n$, it is necessary and sufficient that the $x_{i}$ lie above a common point $s$ of $S$.

**Proof.** The condition is clearly necessary; Lemma (3.4.6) shows it is sufficient. In other words, writing $(X)$ for
the underlying set of $X$, there is a canonical surjective map $(X \times_{S} Y) \to (X) \times_{(S)} (Y)$; this map is
_not_ injective in general — there may be several distinct points of $X \times_{S} Y$ with the same projections $x \in
X$, $y \in Y$, as one already sees when $S$, $X$, $Y$ are prime spectra of fields $k$, $K$, $K'$, since $K \otimes_{k}
K'$ generally has several distinct prime ideals (cf. 3.4.9).

**Corollary (3.4.8).** Let $f : X \to Y$ be an $S$-morphism, $f_{(S')} : X_{(S')} \to Y_{(S')}$ the $S'$-morphism
deduced from $f$ by an extension $S' \to S$ of the base prescheme. Let $p$ (resp. $q$) be the projection $X_{(S')} \to
X$ (resp. $Y_{(S')} \to Y$); then for every subset $M$ of $X$, $$ f_{(S')}^{-1}(q^{-1}(M)) = p^{-1}(f^{-1}(M)). $$

**Proof.** By (3.3.11), $X_{(S')}$ is identified with the product $X \times_{Y} Y_{(S')}$ via the commutative square. By
(3.4.7), the relation $q(y') = f(x)$ for $x \in M$, $y' \in Y_{(S')}$ is equivalent to the existence of $x' \in
X_{(S')}$ with $p(x') = x$ and $f_{(S')}(x') = y'$, whence the corollary.

**Proposition (3.4.9).** Let $X$, $Y$ be two $S$-preschemes, $x$ a point of $X$ and $y$ a point of $Y$, above the same
point $s \in S$. The set of points of $X \times_{S} Y$ with projections $x$ and $y$ is in canonical bijection with the
set of _types of composite extensions_ of $\kappa(x)$ and $\kappa(y)$, regarded as extensions of $\kappa(s)$ (Bourbaki,
_Alg._, ch. VIII, §8, prop. 2).

**Proof.** Let $p$ (resp. $q$) be the projection of $X \times_{S} Y$ onto $X$ (resp. $Y$), and let $E = p^{-1}(x) \cap
q^{-1}(y)$. The morphisms $\operatorname{Spec}(\kappa(x)) \to S$ and $\operatorname{Spec}(\kappa(y)) \to S$ factor
through $\operatorname{Spec}(\kappa(s)) \to S$; since the latter is a monomorphism (2.4.7), (3.2.4) gives $$ P =
\operatorname{Spec}(\kappa(x)) \times_{S} \operatorname{Spec}(\kappa(y)) = \operatorname{Spec}(\kappa(x)
\otimes_{\kappa(s)} \kappa(y)). $$ We define mutually inverse maps $\alpha : P_{0} \to E$, $\beta : E \to P_{0}$
($P_{0}$ the underlying set of $P$). With $i : \operatorname{Spec}(\kappa(x)) \to X$, $j :
\operatorname{Spec}(\kappa(y)) \to Y$ the canonical morphisms (2.4.5), $\alpha$ is the map of underlying spaces
corresponding to $i \times_{S} j$. Conversely, every $z \in E$ defines two $\kappa(s)$-monomorphisms $\kappa(x) \to
\kappa(z)$, $\kappa(y) \to \kappa(z)$, hence a $\kappa(s)$-monomorphism $\kappa(x) \otimes_{\kappa(s)} \kappa(y) \to
\kappa(z)$ and a morphism $\operatorname{Spec}(\kappa(z)) \to P$; $\beta(z)$ is the image of $z$ under it. That $\alpha
\circ \beta$ and $\beta \circ \alpha$ are the identity follows from (2.4.5) and (3.2.1). Finally, $P_{0}$ is in
bijection with the set of types of composite extensions of $\kappa(x)$ and $\kappa(y)$ (Bourbaki, _Alg._, ch. VIII, §8,
prop. 1).

## 3.5. Surjections and injections

<!-- label: I.3.5 -->

**(3.5.1)** Consider in general a property $\mathrm{P}$ of morphisms of preschemes, and the two statements:

(i) If $f : X \to X'$, $g : Y \to Y'$ are two $S$-morphisms with property $\mathrm{P}$, then $f \times_{S} g$ has
property $\mathrm{P}$.

(ii) If $f : X \to Y$ is an $S$-morphism with property $\mathrm{P}$, then every $S'$-morphism $f_{(S')} : X_{(S')} \to
Y_{(S')}$ deduced from $f$ by extension of the base prescheme has property $\mathrm{P}$.

Since $f_{(S')} = f \times_{S} 1_{S'}$, one sees that if the identity $1_{X}$ has property $\mathrm{P}$ for every
prescheme $X$, then (i) implies (ii); and since $f \times_{S} g$ is the composite $X \times_{S} Y \xrightarrow{f \times
1} X' \times_{S} Y \xrightarrow{1 \times g} X' \times_{S} Y'$, if property $\mathrm{P}$ is stable under composition then
(ii) implies (i).

**Proposition (3.5.2).** (i) If $f : X \to X'$, $g : Y \to Y'$ are surjective $S$-morphisms, then $f \times_{S} g$ is
surjective. (ii) If $f : X \to Y$ is a surjective $S$-morphism, then $f_{(S')}$ is surjective for every extension $S'$
of the base prescheme.

**Proof.** Since a composite of surjections is a surjection, it suffices by (3.5.1) to prove (ii); this follows at once
from (3.4.8) applied to $M = X$.

**Proposition (3.5.3).** For a morphism $f : X \to Y$ to be surjective, it is necessary and sufficient that for every
field $K$ and every morphism $\operatorname{Spec}(K) \to Y$, there exist an extension $K'$ of $K$ and a morphism
$\operatorname{Spec}(K') \to X$ making the diagram
$$
\begin{array}{ccc}
X & \leftarrow & \operatorname{Spec}(K') \\
\downarrow & & \downarrow \\
Y & \leftarrow & \operatorname{Spec}(K)
\end{array}
$$
commute.

**Proof.** The condition is sufficient: for any $y \in Y$, apply it to a morphism $\operatorname{Spec}(K) \to Y$
corresponding to a monomorphism $\kappa(y) \to K$ (2.4.6). Conversely, suppose $f$ surjective, and let $y \in Y$ be the
image of the unique point of $\operatorname{Spec}(K)$; there is $x \in X$ with $f(x) = y$. Consider the corresponding
monomorphism $\kappa(y) \to \kappa(x)$ (2.2.1); take $K'$ an extension of $\kappa(y)$ admitting
$\kappa(y)$-monomorphisms of $\kappa(x)$ and of $K$ (Bourbaki, _Alg._, ch. V, §4, prop. 2); the morphism
$\operatorname{Spec}(K') \to X$ corresponding to $\kappa(x) \to K'$ answers the question. In the language of (3.4.5):
every geometric point of $Y$ with values in $K$ comes from a geometric point of $X$ with values in an extension of $K$.

**Definition (3.5.4).** A morphism of preschemes $f : X \to Y$ is called _universally injective_, or a _radicial
morphism_, if for every field $K$ the corresponding map $X(K) \to Y(K)$ is injective.

It follows at once from the definitions that every monomorphism of preschemes (T, 1.1) is radicial.

**(3.5.5)** For a morphism $f : X \to Y$ to be radicial, it suffices that the condition of (3.5.4) hold for every
algebraically closed field. Indeed, if $K$ is arbitrary and $K'$ an algebraically closed extension of $K$, the square
relating $X(K) \to Y(K)$ and $X(K') \to Y(K')$ is commutative, and since $X(K) \to X(K')$ is injective and (by
hypothesis) $X(K') \to Y(K')$ is injective, $X(K) \to Y(K)$ is necessarily injective.

**Proposition (3.5.6).** Let $f : X \to Y$, $g : Y \to Z$ be two morphisms of preschemes. (i) If $f$ and $g$ are
radicial, so is $g \circ f$. (ii) Conversely, if $g \circ f$ is radicial, so is $f$.

**Proof.** By (3.5.4), the proposition reduces to the corresponding (evident) assertions for the maps $X(K) \to Y(K) \to
Z(K)$.

**Proposition (3.5.7).** (i) If the $S$-morphisms $f : X \to X'$, $g : Y \to Y'$ are radicial, so is $f \times_{S} g$.
(ii) If the $S$-morphism $f : X \to Y$ is radicial, so is $f_{(S')} : X_{(S')} \to Y_{(S')}$ for every extension $S' \to
S$ of the base prescheme.

**Proof.** By (3.5.1) it suffices to prove (i). By (3.4.2.1), $(X \times_{S} Y)(K) = X(K) \times_{S(K)} Y(K)$ and $(X'
\times_{S} Y')(K) = X'(K) \times_{S(K)} Y'(K)$; the map corresponding to $f \times_{S} g$ is then $(u, v) \mapsto (f
\circ u, g \circ v)$, and the proposition follows.

**Proposition (3.5.8).** For a morphism $f = (\psi, \theta) : X \to Y$ to be radicial, it is necessary and sufficient
that $\psi$ be injective and that, for every $x \in X$, the monomorphism $\theta^{x} : \kappa(\psi(x)) \to \kappa(x)$
make $\kappa(x)$ a _radicial (purely inseparable) extension_ of $\kappa(\psi(x))$.

**Proof.** Suppose $f$ radicial. First, $\psi(x_{1}) = \psi(x_{2}) = y$ forces $x_{1} = x_{2}$: there is a field $K$,
extension of $\kappa(y)$, with $\kappa(y)$-monomorphisms $\kappa(x_{1}) \to K$, $\kappa(x_{2}) \to K$ (Bourbaki, _Alg._,
ch. V, §4, prop. 2); the corresponding morphisms $u_{1}, u_{2} : \operatorname{Spec}(K) \to X$ satisfy $f \circ u_{1} =
f \circ u_{2}$, hence $u_{1} = u_{2}$, so $x_{1} = x_{2}$. Next, regarding $\kappa(x)$ as an extension of
$\kappa(\psi(x))$ via $\theta^{x}$: if it were not radicial, there would be two distinct $\kappa(\psi(x))$-monomorphisms
of $\kappa(x)$ into an algebraically closed extension $K$, and the two corresponding morphisms $\operatorname{Spec}(K)
\to X$ would violate the hypothesis. Conversely, by (2.4.6), the stated conditions are immediately sufficient for $f$ to
be radicial.

**Corollary (3.5.9).** If $A$ is a ring and $S$ a multiplicative subset of $A$, the canonical morphism
$\operatorname{Spec}(S^{-1}A) \to \operatorname{Spec}(A)$ is radicial.

**Proof.** This morphism is a monomorphism (1.6.2).

**Corollary (3.5.10).** Let $f : X \to Y$ be a radicial morphism, $g : Y' \to Y$ a morphism, and $X' = X_{(Y')} = X
\times_{Y} Y'$. Then the radicial morphism $f_{(Y')}$ (3.5.7(ii)) is a bijection of the underlying space $X'$ onto
$g^{-1}(f(X))$; moreover, for every field $K$, the set $X'(K)$ is identified with the subset of $Y'(K)$ that is the
inverse image, under $Y'(K) \to Y(K)$ (corresponding to $g$), of the subset $X(K)$ of $Y(K)$.

**Proof.** The first assertion follows from (3.5.8) and (3.4.8); the second from the commutativity of the square
relating $X'(K) \to Y'(K)$ and $X(K) \to Y(K)$.

**Remark (3.5.11).** We say a morphism $f = (\psi, \theta)$ of preschemes is _injective_ if the map $\psi$ is injective.
For a morphism $f = (\psi, \theta) : X \to Y$ to be radicial, it is necessary and sufficient that for every morphism $Y'
\to Y$ the morphism $f_{(Y')} : X_{(Y')} \to Y'$ be injective (which justifies the terminology _universally injective_).
The condition is necessary by (3.5.7(ii)) and (3.5.8). Conversely, it implies first that $\psi$ is injective; and if for
some $x \in X$ the monomorphism $\theta^{x} : \kappa(\psi(x)) \to \kappa(x)$ were not radicial, there would be an
extension $K$ of $\kappa(\psi(x))$ and two distinct morphisms $\operatorname{Spec}(K) \to X$ over the same morphism
$\operatorname{Spec}(K) \to Y$ (3.5.8); setting $Y' = \operatorname{Spec}(K)$, there would be two distinct $Y'$-sections
of $X_{(Y')}$ (3.3.14), contradicting the injectivity of $f_{(Y')}$.

## 3.6. Fibers

<!-- label: I.3.6 -->

**Proposition (3.6.1).** Let $f : X \to Y$ be a morphism, $y$ a point of $Y$, and $\mathfrak{a}_{y}$ an ideal of
definition of $\mathcal{O}_{y}$ for the $\mathfrak{m}_{y}$-preadic topology. The projection $p : X \times_{Y}
\operatorname{Spec}(\mathcal{O}_{y}/\mathfrak{a}_{y}) \to X$ is a homeomorphism of the underlying space of $X \times_{Y}
\operatorname{Spec}(\mathcal{O}_{y}/\mathfrak{a}_{y})$ onto the fiber $f^{-1}(y)$, equipped with the topology induced
from that of $X$.

**Proof.** Since $\operatorname{Spec}(\mathcal{O}_{y}/\mathfrak{a}_{y}) \to Y$ is radicial (3.5.4 and 2.4.7) and
$\operatorname{Spec}(\mathcal{O}_{y}/\mathfrak{a}_{y})$ is reduced to a single point — the ideal
$\mathfrak{m}_{y}/\mathfrak{a}_{y}$ being nilpotent by hypothesis (1.1.12) — we already know (3.5.10 and 3.3.4) that $p$
identifies, _as a set_, the underlying space with $f^{-1}(y)$; it remains to prove $p$ is a homeomorphism. By (3.2.7)
the question is local on $X$ and $Y$, so we may assume $X = \operatorname{Spec}(B)$, $Y = \operatorname{Spec}(A)$, with
$B$ an $A$-algebra. Then $p$ corresponds to the homomorphism $1 \otimes \varphi : B \to B \otimes_{A} A'$, where $A' =
\mathcal{O}_{y}/\mathfrak{a}_{y}$ and $\varphi : A \to A'$ is canonical. Every element of $B \otimes_{A} A'$ may be
written $(\sum b_{i} \otimes 1)(1 \otimes \varphi(s)^{-1})$ with $s \notin \mathfrak{j}_{y}$, and prop. (1.2.4) applies.

**(3.6.2)** Throughout the rest of this Treatise, when we consider a fiber $f^{-1}(y)$ of a morphism as equipped with a
structure of $\kappa(y)$-prescheme, we always mean the prescheme obtained by transporting the structure of $X \times_{Y}
\operatorname{Spec}(\kappa(y))$ by the projection into $X$. We also write this product $X \otimes_{Y} \kappa(y)$ or $X
\otimes_{\mathcal{O}_{y}} \kappa(y)$; more generally, for an $\mathcal{O}_{y}$-algebra $B$, we write $X \otimes_{Y} B$
or $X \otimes_{\mathcal{O}_{y}} B$ for the product $X \times_{Y} \operatorname{Spec}(B)$. With this convention, it
follows from (3.5.10) that the points of $X$ with values in an extension $K$ of $\kappa(y)$ are identified with the
points of $f^{-1}(y)$ with values in $K$.

**(3.6.3)** Let $f : X \to Y$, $g : Y \to Z$ be two morphisms, $h = g \circ f$ their composite; for $z \in Z$, the fiber
$h^{-1}(z)$ is a prescheme isomorphic to $$ X \times_{Z} \operatorname{Spec}(\kappa(z)) = (X \times_{Y} Y) \times_{Z}
\operatorname{Spec}(\kappa(z)) = X \times_{Y} g^{-1}(z). $$ In particular, if $U$ is an open subset of $X$, the
prescheme induced on $U \cap f^{-1}(y)$ by the prescheme $f^{-1}(y)$ is isomorphic to $f_{U}^{-1}(y)$ ($f_{U}$ being the
restriction of $f$ to $U$).

**Proposition (3.6.4)** _(transitivity of fibers)._ Let $f : X \to Y$, $g : Y' \to Y$ be two morphisms; set $X' = X
\times_{Y} Y' = X_{(Y')}$ and $f' = f_{(Y')} : X' \to Y'$. For every $y' \in Y'$, setting $y = g(y')$, the prescheme
$f'^{-1}(y')$ is isomorphic to $f^{-1}(y) \otimes_{\kappa(y)} \kappa(y')$.

**Proof.** This amounts to remarking that the two preschemes $(X \times_{Y} \operatorname{Spec}(\kappa(y)))
\otimes_{\kappa(y)} \kappa(y')$ and $(X \times_{Y} Y') \times_{Y'} \operatorname{Spec}(\kappa(y'))$ are both canonically
isomorphic to $X \times_{Y} \operatorname{Spec}(\kappa(y'))$ by (3.3.9.1). In particular, if $V$ is an open neighborhood
of $y$ in $Y$ and $f_{V}$ denotes the restriction of $f$ to the prescheme induced on $f^{-1}(V)$, the preschemes
$f^{-1}(y)$ and $f_{V}^{-1}(y)$ are canonically identified.

**Proposition (3.6.5).** Let $f : X \to Y$ be a morphism, $y$ a point of $Y$, $Z = \operatorname{Spec}(\mathcal{O}_{y})$
the local prescheme, and $p = (\psi, \theta)$ the projection $X \times_{Y} Z \to X$. Then $p$ is a homeomorphism of the
underlying space of $X \times_{Y} Z$ onto the subspace $f^{-1}(Z)$ of $X$ (when the underlying space of $Z$ is
identified with a subspace of $Y$, cf. (2.4.2)), and for every $t \in X \times_{Y} Z$, setting $x = \psi(t)$,
$\theta_{t}^{\sharp}$ is an isomorphism of $\mathcal{O}_{x}$ onto $\mathcal{O}_{t}$.

**Proof.** Since $Z$ (identified with a subspace of $Y$) is contained in every affine open containing $y$ (2.4.2), we
may, as in (3.6.1), reduce to the case $X = \operatorname{Spec}(A)$, $Y = \operatorname{Spec}(B)$ affine schemes, $A$ a
$B$-algebra. Then $X \times_{Y} Z$ is the prime spectrum of $A \otimes_{B} \mathcal{O}_{y}$, and this ring is
canonically identified with $S^{-1}A$, where $S$ is the image of $B \setminus \mathfrak{j}_{y}$ in $A$ (0, 1.5.2); since
$p$ then corresponds to the canonical homomorphism $A \to S^{-1}A$, the proposition follows from (1.6.2).

## 3.7. Application: reduction of a prescheme mod $\mathfrak{J}$[^I-3-2]

<!-- label: I.3.7 -->

**(3.7.1)** Let $A$ be a ring, $X$ an $A$-prescheme, and $\mathfrak{J}$ an ideal of $A$; then $X_{0} = X \otimes_{A}
(A/\mathfrak{J})$ is an $(A/\mathfrak{J})$-prescheme, sometimes said to be _deduced from $X$ by reduction mod
$\mathfrak{J}$_.

**(3.7.2)** This terminology is used above all when $A$ is a local ring and $\mathfrak{J}$ its maximal ideal, so that
$X_{0}$ is a prescheme over the residue field $k = A/\mathfrak{J}$ of $A$. When moreover $A$ is integral with field of
fractions $K$, one may also consider the $K$-prescheme $X' = X \otimes_{A} K$. By an abuse of language we shall not use,
it was customary until now to say that $X_{0}$ is deduced from $X'$ by reduction mod $\mathfrak{J}$. In the cases where
this language was used, $A$ was a local ring of dimension $1$ (most often a discrete valuation ring), and it was
understood (more or less explicitly) that the given $K$-prescheme $X'$ was a closed subprescheme of a $K$-prescheme $P'$
(in fact a projective space of type $\mathbf{P}^{n}$, cf. II, 4.1.1), itself of the form $P' = P \otimes_{A} K$, where
$P$ is a given $A$-prescheme. In our language, the definition of $X_{0}$ from $X'$ is formulated as follows.

Consider the affine scheme $Y = \operatorname{Spec}(A)$, consisting of two points: the unique closed point $\mathfrak{y}
= \mathfrak{J}$ and the generic point $(0)$, the set $U$ reduced to the generic point being an open $U =
\operatorname{Spec}(K)$ in $Y$. If $X$ is an $A$-prescheme (i.e. a $Y$-prescheme), $X \otimes_{A} K = X'$ is nothing but
the prescheme induced by $X$ on $\psi^{-1}(U)$, where $\psi : X \to Y$ is the structure morphism. In particular, if
$\varphi : P \to Y$ is the structure morphism, a closed subprescheme $X'$ of $P' = \varphi^{-1}(U)$ is a (locally
closed) subprescheme of $P$. If $P$ is noetherian (for instance if $A$ is noetherian and $P$ of finite type over $A$),
there is a smallest closed subprescheme $\bar{X} = X$ of $P$ majorizing $X'$ (9.5.10), and $X'$ is the prescheme induced
by $X$ on the open $\varphi^{-1}(U) \cap X$, hence isomorphic to $X \otimes_{A} K$ (9.5.10). The immersion of $X'$ into
$P' = P \otimes_{A} K$ thus canonically lets us regard $X'$ as of the form $X' = X \otimes_{A} K$, where $X$ is an
$A$-prescheme. One may then consider the prescheme reduced mod $\mathfrak{J}$, $X_{0} = X \otimes_{A} k$, which is none
other than the fiber $\psi^{-1}(\mathfrak{y})$ of the closed point. Until now, for lack of adequate terminology, the
$A$-prescheme $X$ was not introduced explicitly. It should be noted, however, that all the assertions usually made about
the "prescheme reduced mod $\mathfrak{J}$" $X_{0}$ must be regarded as consequences of more complete assertions
concerning $X$ itself, and can be formulated and understood satisfactorily only by interpreting them in this way. It
seems, moreover, that the hypotheses made always amount to hypotheses on $X$ itself (independently of a prior immersion
of $X'$ into some $\mathbf{P}^{n}$), which permits more intrinsic statements.

**(3.7.3)** Let us finally point out a very particular fact, which has no doubt contributed to delaying the conceptual
clarification of the situation considered here: if $A$ is a discrete valuation ring and $X$ is proper over $A$ (which is
in fact the case if $X$ is a closed subprescheme of a $\mathbf{P}^{n}$, cf. II, 5.5.4), then the points of $X$ with
values in $A$ and the points of $X'$ with values in $K$ are in bijective correspondence (II, 7.3.8). This is why one has
often believed one was proving results about $X'$, whereas in reality one was proving statements about $X$, which remain
valid (in this form) when the base local ring is no longer assumed to be of dimension $1$.

[^I-3-1]: The notation $\operatorname{Hom}_{A}$ here denotes the set of homomorphisms of $A$-algebras.

[^I-3-2]: This subsection, which uses notions and results from later in Chapter I and from Chapter II, will not be used
in the sequel, and is intended only for readers familiar with classical algebraic geometry.

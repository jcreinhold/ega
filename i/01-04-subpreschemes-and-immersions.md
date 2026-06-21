# §4. Subpreschemes and Immersion Morphisms

<!-- label: I.4 -->

## 4.1. Subpreschemes

<!-- label: I.4.1 -->

**(4.1.1)** Since the notion of quasi-coherent sheaf (0, 5.1.3) is local, a quasi-coherent $\mathcal{O}_{X}$-Module
$\mathcal{F}$ on a prescheme $X$ may be defined by the condition that, for every affine open $V$ of $X$, $\mathcal{F}|V$
is isomorphic to the sheaf associated to a $\Gamma(V, \mathcal{O}_{X})$-module (1.4.1). On a prescheme $X$ the structure
sheaf $\mathcal{O}_{X}$ is quasi-coherent, and kernels, cokernels, and images of homomorphisms of quasi-coherent
$\mathcal{O}_{X}$-Modules, as well as inductive limits and direct sums of quasi-coherent $\mathcal{O}_{X}$-Modules, are
quasi-coherent (1.3.7 and 1.3.9).

**Proposition (4.1.2).** Let $X$ be a prescheme and $\mathcal{J}$ a quasi-coherent sheaf of ideals in $\mathcal{O}_{X}$.
The support $Y$ of the sheaf $\mathcal{O}_{X}/\mathcal{J}$ is closed, and if $\mathcal{O}_{Y}$ denotes the restriction
of $\mathcal{O}_{X}/\mathcal{J}$ to $Y$, then $(Y, \mathcal{O}_{Y})$ is a prescheme.

**Proof.** By (2.1.3) it suffices to treat the case where $X = \operatorname{Spec}(A)$ is affine, and to show that there
$Y$ is closed in $X$ and is an affine scheme. Indeed, $\mathcal{O}_{X} = \tilde{A}$ and $\mathcal{J} =
\tilde{\mathfrak{J}}$, where $\mathfrak{J}$ is an ideal of $A$ (1.4.1); then $Y = V(\mathfrak{J})$ and is identified
with the prime spectrum of $B = A/\mathfrak{J}$ (1.1.11). Moreover, if $\varphi : A \to B = A/\mathfrak{J}$ is the
canonical homomorphism, the direct image $\varphi_{*}(\tilde{B})$ is canonically identified with the sheaf
$\widetilde{A/\mathfrak{J}} = \mathcal{O}_{Y}$ (1.6.3 and 1.3.9), which completes the proof.

We say $(Y, \mathcal{O}_{Y})$ is the _subprescheme of $(X, \mathcal{O}_{X})$ defined by the sheaf of ideals
$\mathcal{J}$_; it is a special case of the general notion of subprescheme.

**Definition (4.1.3).** A ringed space $(Y, \mathcal{O}_{Y})$ is a _subprescheme_ of a prescheme $(X, \mathcal{O}_{X})$
if: 1° $Y$ is a locally closed subspace of $X$; 2° if $U$ denotes the largest open of $X$ containing $Y$ such that $Y$
is closed in $U$ (i.e. the complement in $X$ of the frontier of $Y$ relative to $Y$), then $(Y, \mathcal{O}_{Y})$ is a
subprescheme of $(U, \mathcal{O}_{X}|U)$ defined by a quasi-coherent sheaf of ideals of $\mathcal{O}_{X}|U$. The
subprescheme $(Y, \mathcal{O}_{Y})$ is called _closed_ if $Y$ is closed in $X$ (in which case $U = X$).

It follows at once from this definition and (4.1.2) that the closed subpreschemes of $X$ are in canonical bijective
correspondence with the quasi-coherent sheaves of ideals $\mathcal{J}$ of $\mathcal{O}_{X}$: if two such sheaves
$\mathcal{J}$, $\mathcal{J}'$ have the same (closed) support $Y$ and the restrictions of $\mathcal{O}_{X}/\mathcal{J}$
and $\mathcal{O}_{X}/\mathcal{J}'$ to $Y$ agree, then $\mathcal{J}' = \mathcal{J}$.

**(4.1.4)** Let $(Y, \mathcal{O}_{Y})$ be a subprescheme of $X$, $U$ the largest open of $X$ containing $Y$ in which $Y$
is closed, and $V$ an open of $X$ contained in $U$; then $V \cap Y$ is closed in $V$. If moreover $Y$ is defined by the
quasi-coherent sheaf of ideals $\mathcal{J}$ of $\mathcal{O}_{X}|U$, then $\mathcal{J}|V$ is a quasi-coherent sheaf of
ideals of $\mathcal{O}_{X}|V$, and the prescheme induced by $Y$ on $Y \cap V$ is the closed subprescheme of $V$ defined
by $\mathcal{J}|V$. Conversely:

**Proposition (4.1.5).** Let $(Y, \mathcal{O}_{Y})$ be a ringed space such that $Y$ is a subspace of $X$ and there is a
cover $(V_{\alpha})$ of $Y$ by opens of $X$ such that, for each $\alpha$, $Y \cap V_{\alpha}$ is closed in $V_{\alpha}$
and the ringed space $(Y \cap V_{\alpha}, \mathcal{O}_{Y}|(Y \cap V_{\alpha}))$ is a closed subprescheme of the
prescheme induced on $V_{\alpha}$ by $X$. Then $(Y, \mathcal{O}_{Y})$ is a subprescheme of $X$.

**Proof.** The hypothesis implies $Y$ is locally closed in $X$ and the largest open $U$ containing $Y$ in which $Y$ is
closed contains all the $V_{\alpha}$; we may thus reduce to $U = X$ and $Y$ closed in $X$. Define a quasi-coherent sheaf
of ideals $\mathcal{J}$ of $\mathcal{O}_{X}$ by taking for $\mathcal{J}|V_{\alpha}$ the sheaf of ideals of
$\mathcal{O}_{X}|V_{\alpha}$ defining the closed subprescheme $(Y \cap V_{\alpha}, \mathcal{O}_{Y}|(Y \cap
V_{\alpha}))$, and $\mathcal{J}|W = \mathcal{O}_{X}|W$ for every open $W$ of $X$ not meeting $Y$. By (4.1.3) and (4.1.4)
there is a unique sheaf of ideals $\mathcal{J}$ satisfying these conditions, and it defines the closed subprescheme $(Y,
\mathcal{O}_{Y})$. In particular, the prescheme induced by $X$ on an open of $X$ is a subprescheme of $X$.

**Proposition (4.1.6).** A subprescheme (resp. closed subprescheme) of a subprescheme (resp. closed subprescheme) of $X$
is canonically identified with a subprescheme (resp. closed subprescheme) of $X$.

**Proof.** A locally closed subset of a locally closed subspace of $X$ is a locally closed subspace of $X$, so by
(4.1.5) the question is local and we may assume $X$ affine; the proposition then follows from the canonical
identification of $A/\mathfrak{J}'$ with $(A/\mathfrak{J})/(\mathfrak{J}'/\mathfrak{J})$ when $\mathfrak{J} \subset
\mathfrak{J}'$ are two ideals of a ring $A$. We shall always make this identification in the sequel.

**(4.1.7)** Let $Y$ be a subprescheme of a prescheme $X$, and $\psi : Y \to X$ the canonical injection of underlying
spaces; the inverse image $\psi^{*}(\mathcal{O}_{X})$ is the restriction $\mathcal{O}_{X}|Y$ (0, 3.7.1). For each $y \in
Y$, let $\omega_{y}$ be the canonical homomorphism $(\mathcal{O}_{X})_{y} \to (\mathcal{O}_{Y})_{y}$; these are the
stalk restrictions of a surjective homomorphism $\omega : \mathcal{O}_{X}|Y \to \mathcal{O}_{Y}$ of sheaves of rings (it
suffices to check locally, assuming $X$ affine and $Y$ closed: if $\mathcal{J}$ defines $Y$, the $\omega_{y}$ are the
stalk restrictions of $\mathcal{O}_{X} \to (\mathcal{O}_{X}/\mathcal{J})|Y$). We have thus defined a monomorphism of
ringed spaces (0, 4.1.1) $j = (\psi, \omega)$, which is evidently a morphism $Y \to X$ of preschemes (2.2.1), the
_canonical injection morphism_. If $f : X \to Z$ is a morphism, we call the composite $Y \to X \to Z$ the _restriction
of $f$ to the subprescheme $Y$_.

**(4.1.8)** In accordance with the general definitions (T, I, 1.1), we say that a morphism of preschemes $f : Z \to X$
is _dominated_ by the injection morphism $j : Y \to X$ of a subprescheme $Y$ of $X$ if $f$ factors as $Z \xrightarrow{g}
Y \xrightarrow{j} X$, where $g$ is a morphism of preschemes; $g$ is necessarily unique since $j$ is a monomorphism.

**Proposition (4.1.9).** For a morphism $f : Z \to X$ to be dominated by an injection morphism $j : Y \to X$, it is
necessary and sufficient that $f(Z) \subset Y$ and that, for every $z \in Z$, setting $y = f(z)$, the homomorphism
$(\mathcal{O}_{X})_{y} \to \mathcal{O}_{z}$ corresponding to $f$ factor through $(\mathcal{O}_{X})_{y} \to
(\mathcal{O}_{Y})_{y} \to \mathcal{O}_{z}$ (equivalently, that the kernel of $(\mathcal{O}_{X})_{y} \to \mathcal{O}_{z}$
contain that of $(\mathcal{O}_{X})_{y} \to (\mathcal{O}_{Y})_{y}$).

**Proof.** The conditions are clearly necessary. To see they are sufficient, we may reduce to the case where $Y$ is a
closed subprescheme of $X$, replacing $X$ if necessary by an open $U$ in which $Y$ is closed (4.1.3); $Y$ is then
defined by a quasi-coherent sheaf $\mathcal{J}$ of ideals of $\mathcal{O}_{X}$. Write $f = (\psi, \theta)$, and let
$\mathcal{N}$ be the kernel sheaf of $\theta : \psi^{*}(\mathcal{O}_{X}) \to \mathcal{O}_{Z}$; by the properties of the
functor $\psi^{*}$ (0, 3.7.2), the hypothesis gives $\psi^{*}(\mathcal{J}) \subset \mathcal{N}$. Hence $\theta$ factors
as $\psi^{*}(\mathcal{O}_{X}) \to \psi^{*}(\mathcal{O}_{X}/\mathcal{J}) \to \mathcal{O}_{Z}$, the first arrow being
canonical. Letting $\psi'$ be the continuous map $Z \to Y$ coinciding with $\psi$, one has $\psi'^{*}(\mathcal{O}_{Y})$
on the left, and the second arrow $\omega$ is a local homomorphism, so $g = (\psi', \omega)$ is a morphism $Z \to Y$ of
preschemes (2.2.1) with $f = j \circ g$, whence the proposition.

**Corollary (4.1.10).** For an injection morphism $Z \to X$ to be dominated by the injection morphism $Y \to X$, it is
necessary and sufficient that $Z$ be a subprescheme of $Y$.

We then write $Z \le Y$, and this is an order relation on the set of subpreschemes of $X$.

## 4.2. Immersion morphisms

<!-- label: I.4.2 -->

**Definition (4.2.1).** A morphism $f : Y \to X$ is called an _immersion_ (resp. _closed immersion_, resp. _open
immersion_) if it factors as $Y \xrightarrow{g} Z \xrightarrow{j} X$, where $g$ is an isomorphism, $Z$ a subprescheme of
$X$ (resp. a closed subprescheme, resp. a prescheme induced on an open), and $j$ the injection morphism.

The subprescheme $Z$ and the isomorphism $g$ are then uniquely determined: if $Z'$ is a second subprescheme with
injection $j'$ and $g'$ an isomorphism $Y \to Z'$ with $j \circ g = j' \circ g'$, then $j' = j \circ g \circ g'^{-1}$,
whence $Z' \le Z$ (4.1.10), and likewise $Z \le Z'$, so $Z' = Z$; since $j$ is a monomorphism, $g' = g$. One calls $f =
j \circ g$ the _canonical factorization_ of the immersion $f$, and $Z$, $g$ the subprescheme and isomorphism
_associated_ to $f$. An immersion is a monomorphism of preschemes (4.1.7) and a fortiori a radicial morphism (3.5.4).

**Proposition (4.2.2).** _a)_ For a morphism $f = (\psi, \theta) : Y \to X$ to be an open immersion, it is necessary and
sufficient that $\psi$ be a homeomorphism of $Y$ onto an open subset of $X$, and that for every $y \in Y$ the
homomorphism $\theta_{y}^{\sharp} : (\mathcal{O}_{X})_{\psi(y)} \to \mathcal{O}_{y}$ be bijective. _b)_ For $f = (\psi,
\theta) : Y \to X$ to be an immersion (resp. a closed immersion), it is necessary and sufficient that $\psi$ be a
homeomorphism of $Y$ onto a locally closed (resp. closed) subset of $X$, and that for every $y \in Y$ the homomorphism
$\theta_{y}^{\sharp}$ be surjective.

**Proof.** _a)_ The conditions are clearly necessary. Conversely, if they hold, $\theta$ is an isomorphism of
$\mathcal{O}_{Y}$ onto $\psi^{*}(\mathcal{O}_{X})$, and $\psi^{*}(\mathcal{O}_{X})$ is the sheaf obtained by transport
of structure from $\mathcal{O}_{X}|\psi(Y)$ via $\psi^{-1}$, whence the conclusion.

_b)_ The conditions being clearly necessary, we prove sufficiency. First suppose $X$ affine and $Z = \psi(Y)$ closed in
$X$. By (0, 3.4.6), $\psi_{*}(\mathcal{O}_{Y})$ has support $Z$, and its restriction $\mathcal{O}'_{Z}$ to $Z$ recovers
$(Y, \mathcal{O}_{Y})$ by transport of structure via $\psi$. We show $\psi_{*}(\mathcal{O}_{Y})$ is a quasi-coherent
$\mathcal{O}_{X}$-Module. For $x \notin Z$ it vanishes near $x$; for $x = \psi(y) \in Z$, take an affine open
neighborhood $V$ of $y$ in $Y$; then $\psi(V)$ is the trace on $Z$ of an open $U$ of $X$, and the restriction of
$\psi_{*}(\mathcal{O}_{Y})$ to $U$ agrees with that of the direct image $(\psi_{V})_{*}(\mathcal{O}_{Y}|V)$. The
restriction of $(\psi, \theta)$ to $(V, \mathcal{O}_{Y}|V)$ is of the form $({}^{a}\varphi, \tilde{\varphi})$, where
$\varphi : A = \Gamma(X, \mathcal{O}_{X}) \to \Gamma(V, \mathcal{O}_{Y})$ is a homomorphism (1.7.3), so
$(\psi_{V})_{*}(\mathcal{O}_{Y}|V)$ is quasi-coherent (1.6.3), proving the claim by the local nature of quasi-coherence.
Since $\psi$ is a homeomorphism, (0, 3.4.5) gives that $\theta_{y}^{\sharp}$ is identified with a stalk of the canonical
map $\mathcal{O}_{X} \to \psi_{*}(\mathcal{O}_{Y})$ via isomorphisms, so the surjectivity of $\theta_{y}^{\sharp}$ gives
that of this map. As $\psi_{*}(\mathcal{O}_{Y})$ has support $Z$, the canonical homomorphism of $\mathcal{O}_{X} =
\tilde{A}$ onto the quasi-coherent Module $\psi_{*}(\mathcal{O}_{Y})$ is surjective; hence there is a unique isomorphism
$\omega$ of a quotient $\widetilde{A/\mathfrak{J}}$ ($\mathfrak{J}$ an ideal of $A$) onto $\psi_{*}(\mathcal{O}_{Y})$
inducing $\theta$ (1.3.8). With $\mathcal{O}'_{Z}$ the restriction of $\widetilde{A/\mathfrak{J}}$ to $Z$, $(Z,
\mathcal{O}'_{Z})$ is a subprescheme of $X$, and $f$ factors as the canonical injection of this subprescheme and the
isomorphism $(\psi_{0}, \omega_{0})$. For the general case, take an affine open $U$ of $X$ with $U \cap \psi(Y)$ closed
and nonempty; restricting $f$ to $\psi^{-1}(U)$ reduces to the first case, giving a closed immersion $\psi^{-1}(U) \to
U$ with canonical factorization $j_{U} \circ g_{U}$. For a second affine open $V \subset U$, uniqueness of the canonical
factorization (4.2.1) forces compatibility on overlaps, so by (4.1.5) there is a subprescheme $Z$ of $X$ with underlying
space $\psi(Y)$, and the $g_{U}$ glue to an isomorphism $g : Y \to Z$ with $f = j \circ g$.

**Corollary (4.2.3).** Let $X$ be an affine scheme. For a morphism $f = (\psi, \theta) : Y \to X$ to be a closed
immersion, it is necessary and sufficient that $Y$ be an affine scheme and the homomorphism $\Gamma(\theta) :
\Gamma(\mathcal{O}_{X}) \to \Gamma(\mathcal{O}_{Y})$ be surjective.

**Corollary (4.2.4).** _a)_ Let $f : Y \to X$ be a morphism and $(V_{\lambda})$ a cover of $f(Y)$ by opens of $X$. For
$f$ to be an immersion (resp. an open immersion), it is necessary and sufficient that its restriction to each induced
prescheme $f^{-1}(V_{\lambda})$ be an immersion (resp. an open immersion) into $V_{\lambda}$. _b)_ Let $f : Y \to X$ be
a morphism and $(V_{\lambda})$ an open cover of $X$. For $f$ to be a closed immersion, it is necessary and sufficient
that its restriction to each $f^{-1}(V_{\lambda})$ be a closed immersion into $V_{\lambda}$.

**Proof.** Write $f = (\psi, \theta)$; in case _a)_, $\theta_{y}^{\sharp}$ is surjective (resp. bijective) for all $y$,
and in case _b)_ surjective for all $y$, so it suffices to check the topological condition on $\psi$. Now $\psi$ is
injective and carries neighborhoods to neighborhoods within $\psi(Y)$; in case _a)_, $\psi(Y) \cap V_{\lambda}$ is
locally closed (resp. open) in $V_{\lambda}$, so $\psi(Y)$ is locally closed (resp. open) in $\bigcup V_{\lambda}$, a
fortiori in $X$; in case _b)_, $\psi(Y) \cap V_{\lambda}$ is closed in $V_{\lambda}$, so $\psi(Y)$ is closed in $X =
\bigcup V_{\lambda}$.

**Proposition (4.2.5).** The composite of two immersions (resp. two open immersions, two closed immersions) is an
immersion (resp. an open immersion, a closed immersion). This follows trivially from (4.1.6).

## 4.3. Products of immersions

<!-- label: I.4.3 -->

**Proposition (4.3.1).** Let $\alpha : X' \to X$, $\beta : Y' \to Y$ be two $S$-morphisms. If $\alpha$ and $\beta$ are
immersions (resp. open immersions, resp. closed immersions), then $\alpha \times_{S} \beta : X' \times_{S} Y' \to X
\times_{S} Y$ is an immersion (resp. open, resp. closed). Moreover, if $\alpha$ (resp. $\beta$) identifies $X'$ (resp.
$Y'$) with a subprescheme $X''$ (resp. $Y''$) of $X$ (resp. $Y$), then $\alpha \times_{S} \beta$ identifies the
underlying space of $X' \times_{S} Y'$ with the subspace $p^{-1}(X'') \cap q^{-1}(Y'')$ of $X \times_{S} Y$, where $p$,
$q$ are the projections.

**Proof.** By (4.2.1) we may assume $X'$, $Y'$ are subpreschemes and $\alpha$, $\beta$ injection morphisms. The
proposition is already known for subpreschemes induced on opens (3.2.7); since every subprescheme is a closed
subprescheme of a prescheme induced on an open (4.1.3), we reduce to $X'$, $Y'$ closed subpreschemes. We may assume $S$
affine: covering $S$ by affine opens $S_{\mu}$ and using (3.2.5), (3.2.6.4), (3.2.7), and (4.2.4), the general case
follows from the affine one. Likewise we may assume $X$, $Y$ affine: covering by affine opens and using (3.2.7), the
relation $p'^{-1}(X'_{i}) \cap q'^{-1}(Y'_{j}) = \gamma^{-1}(U_{i} \times_{S} V_{j})$ (where $\gamma = \alpha \times_{S}
\beta$) reduces to the affine case. So assume $X$, $Y$, $S$ affine with rings $B$, $C$, $A$; then $B$, $C$ are
$A$-algebras, $X'$, $Y'$ affine with quotient rings $B'$, $C'$, and $\alpha = ({}^{a}\rho, \ldots)$, $\beta =
({}^{a}\sigma, \ldots)$ with $\rho : B \to B'$, $\sigma : C \to C'$ the canonical surjections (1.7.3). Now $X \times_{S}
Y$ (resp. $X' \times_{S} Y'$) is affine with ring $B \otimes_{A} C$ (resp. $B' \otimes_{A} C'$), and $\alpha \times_{S}
\beta = ({}^{a}\tau, \ldots)$ with $\tau = \rho \otimes \sigma : B \otimes_{A} C \to B' \otimes_{A} C'$ (3.2.2, 3.2.3);
since $\tau$ is surjective, $\alpha \times_{S} \beta$ is a (closed) immersion. If $\mathfrak{b}$ (resp. $\mathfrak{c}$)
is the kernel of $\rho$ (resp. $\sigma$), the kernel of $\tau$ is $u(\mathfrak{b}) + v(\mathfrak{c})$ ($u : b \mapsto b
\otimes 1$, $v : c \mapsto 1 \otimes c$); this corresponds in $\operatorname{Spec}(B \otimes_{A} C)$ to the closed set
$p^{-1}(X') \cap q^{-1}(Y')$, completing the proof.

**Corollary (4.3.2).** If $f : X \to Y$ is an immersion (resp. open, resp. closed immersion) and an $S$-morphism, then
$f_{(S')}$ is an immersion (resp. open, resp. closed immersion) for every extension $S' \to S$ of the base prescheme.

## 4.4. Inverse image of a subprescheme

<!-- label: I.4.4 -->

**Proposition (4.4.1).** Let $f : X \to Y$ be a morphism, $Y'$ a subprescheme (resp. closed subprescheme, resp.
prescheme induced on an open) of $Y$, and $j : Y' \to Y$ the injection morphism. Then the projection $p : X \times_{Y}
Y' \to X$ is an immersion (resp. closed, resp. open); the associated subprescheme of $X$ has underlying space
$f^{-1}(Y')$, and if $j'$ is its injection morphism, a morphism $h : Z \to X$ is such that $f \circ h$ is dominated by
$j$ if and only if $h$ is dominated by $j'$.

**Proof.** Since $p = 1_{X} \times_{Y} j$ (3.3.4), the first assertion follows from (4.3.1); the second is a special
case of (3.5.10) (exchanging the roles of $X$ and $Y'$). Finally, if $f \circ h = j \circ h'$ with $h' : Z \to Y'$, the
definition of the product gives $h = p \circ u$ for a morphism $u : Z \to X \times_{Y} Y'$, whence the last assertion.

We say the subprescheme of $X$ so defined is the _inverse image of the subprescheme $Y'$ of $Y$ by $f$_, consistent with
the terminology of (3.3.6). When $f^{-1}(Y') = X$, $f$ factors as $X \to Y' \to Y$. When $y$ is a closed point of $Y$
and $Y' = \operatorname{Spec}(\kappa(y))$ the smallest closed subprescheme with $\{y\}$ as underlying space (4.1.9), the
closed subprescheme $f^{-1}(Y')$ is canonically isomorphic to the fiber $f^{-1}(y)$ of (3.6.2), with which it is
identified.

**Corollary (4.4.2).** Let $f : X \to Y$, $g : Y \to Z$ be two morphisms, $h = g \circ f$. For every subprescheme $Z'$
of $Z$, the subpreschemes $f^{-1}(g^{-1}(Z'))$ and $h^{-1}(Z')$ of $X$ are identical. This follows from the canonical
isomorphism $X \times_{Y} (Y \times_{Z} Z') \cong X \times_{Z} Z'$ (3.3.9.1).

**Corollary (4.4.3).** Let $X'$, $X''$ be two subpreschemes of $X$ with injections $j' : X' \to X$, $j'' : X'' \to X$.
Then $j'^{-1}(X'')$ and $j''^{-1}(X')$ both equal the infimum $\inf(X', X'')$ for the order relation between
subpreschemes, and are canonically isomorphic to $X' \times_{X} X''$. This follows from (4.4.1) and (4.1.10).

**Corollary (4.4.4).** Let $f : X \to Y$ be a morphism and $Y'$, $Y''$ two subpreschemes of $Y$; then $f^{-1}(\inf(Y',
Y'')) = \inf(f^{-1}(Y'), f^{-1}(Y''))$. This follows from the canonical isomorphism between $(X \times_{Y} Y')
\times_{X} (X \times_{Y} Y'')$ and $X \times_{Y} (Y' \times_{Y} Y'')$ (3.3.9.1).

**Proposition (4.4.5).** Let $f : X \to Y$ be a morphism and $Y'$ a closed subprescheme of $Y$ defined by a
quasi-coherent sheaf $\mathcal{J}$ of ideals of $\mathcal{O}_{Y}$ (4.1.3). Then the closed subprescheme $f^{-1}(Y')$ of
$X$ is defined by the quasi-coherent sheaf of ideals $f^{*}(\mathcal{J})\mathcal{O}_{X}$ of $\mathcal{O}_{X}$.

**Proof.** The question is local on $X$ and $Y$; it suffices to remark that if $B$ is an $A$-algebra and $\mathfrak{J}$
an ideal of $A$, then $B \otimes_{A} (A/\mathfrak{J}) = B/\mathfrak{J}B$, and to apply (1.6.9).

**Corollary (4.4.6).** Let $X'$ be a closed subprescheme of $X$ defined by a quasi-coherent sheaf of ideals
$\mathcal{J}$ of $\mathcal{O}_{X}$, and $i : X' \to X$ the injection. For the restriction $f \circ i$ of $f$ to $X'$ to
be dominated by the injection $j : Y' \to Y$ (i.e. to factor as $j \circ g$ with $g : X' \to Y'$), it is necessary and
sufficient that $f^{*}(\mathcal{J}')\mathcal{O}_{X} \subset \mathcal{J}$, where $\mathcal{J}'$ is the ideal sheaf of
$Y'$. It suffices to apply (4.4.1) to $i$, taking (4.4.5) into account.

## 4.5. Local immersions and local isomorphisms

<!-- label: I.4.5 -->

**Definition (4.5.1).** Let $f : X \to Y$ be a morphism of preschemes. We say $f$ is a _local immersion at a point $x
\in X$_ if there exist an open neighborhood $U$ of $x$ in $X$ and an open neighborhood $V$ of $f(x)$ in $Y$ such that
the restriction of $f$ to the induced prescheme $U$ is a closed immersion of $U$ into the induced prescheme $V$. We say
$f$ is a _local immersion_ if it is so at every point of $X$.

**Definition (4.5.2).** We say a morphism $f : X \to Y$ is a _local isomorphism at a point $x \in X$_ if there exists an
open neighborhood $U$ of $x$ in $X$ such that the restriction of $f$ to the induced prescheme $U$ is an open immersion
of $U$ into $Y$. We say $f$ is a _local isomorphism_ if it is so at every point of $X$.

**(4.5.3)** An immersion (resp. a closed immersion) $f : X \to Y$ may thus be characterized as a local immersion such
that $f$ is a homeomorphism of the underlying space of $X$ onto a subset (resp. a closed subset) of $Y$. An open
immersion $f$ may be characterized as an injective local isomorphism.

**Proposition (4.5.4).** Let $X$ be an irreducible prescheme and $f : X \to Y$ an injective dominant morphism. If $f$ is
a local immersion, then $f$ is an immersion and $f(X)$ is open in $Y$.

**Proof.** Let $x \in X$, and let $U$, $V$ be open neighborhoods of $x$ and $f(x)$ such that $f|U$ is a closed immersion
into $V$. Since $U$ is dense in $X$, $f(U)$ is dense in $Y$ by hypothesis, so $f(U) = V$ and $f$ is a homeomorphism of
$U$ onto $V$; injectivity of $f$ gives $f^{-1}(V) = U$, whence the proposition.

**Proposition (4.5.5).** (i) The composite of two local immersions (resp. two local isomorphisms) is a local immersion
(resp. a local isomorphism). (ii) Let $f : X \to X'$, $g : Y \to Y'$ be two $S$-morphisms. If $f$ and $g$ are local
immersions (resp. local isomorphisms), so is $f \times_{S} g$. (iii) If an $S$-morphism $f$ is a local immersion (resp.
a local isomorphism), so is $f_{(S')}$ for every extension $S' \to S$ of the base prescheme.

**Proof.** By (3.5.1) it suffices to prove (i) and (ii). (i) follows at once from the transitivity of closed (resp.
open) immersions (4.2.4) and the fact that if $f$ is a homeomorphism of $X$ onto a closed subset of $Y$, then for every
open $U \subset X$, $f(U)$ is open in $f(X)$, hence $f(U) = V \cap f(X)$ for some open $V$ of $Y$, so $f(U)$ is closed
in $V$. For (ii), let $p$, $q$ be the projections of $X \times_{S} Y$ and $p'$, $q'$ those of $X' \times_{S} Y'$. There
are open neighborhoods $U$, $U'$, $V$, $V'$ of $x = p(\xi)$, $x' = p'(\xi')$, $y = q(\xi)$, $y' = q'(\xi')$ such that
the restrictions of $f$ and $g$ to $U$ and $V$ are closed (resp. open) immersions into $U'$ and $V'$. Since the
underlying spaces of $U \times_{S} V$ and $U' \times_{S} V'$ are identified with the open neighborhoods $p^{-1}(U) \cap
q^{-1}(V)$ and $p'^{-1}(U') \cap q'^{-1}(V')$ (3.2.7), the proposition follows from (4.3.1).

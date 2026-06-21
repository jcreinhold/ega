# §10. Formal Schemes

<!-- label: I.10 -->

## 10.1. Formal affine schemes

<!-- label: I.10.1 -->

**(10.1.1)** Let $A$ be an admissible topological ring (0, 7.1.2); for every ideal of definition $\mathfrak{J}$ of $A$,
$\operatorname{Spec}(A/\mathfrak{J})$ is identified with the closed subspace $V(\mathfrak{J})$ of
$\operatorname{Spec}(A)$ (1.1.11), the set of open prime ideals of $A$; this topological space does not depend on the
ideal of definition $\mathfrak{J}$ considered; let us denote it by $\mathfrak{X}$. Let $(\mathfrak{J}_{\lambda})$ be a
fundamental system of neighborhoods of $0$ in $A$, formed of ideals of definition, and for each $\lambda$, let
$\mathcal{O}_{\lambda}$ be the structure sheaf of $\operatorname{Spec}(A/\mathfrak{J}_{\lambda})$; this sheaf is induced
on $\mathfrak{X}$ by $\widetilde{A/\mathfrak{J}_{\lambda}}$ (which is zero off $\mathfrak{X}$). For $\mathfrak{J}_{\mu}
\subset \mathfrak{J}_{\lambda}$, the canonical homomorphism $A/\mathfrak{J}_{\mu} \to A/\mathfrak{J}_{\lambda}$
therefore defines a homomorphism $u_{\lambda\mu} : \mathcal{O}_{\mu} \to \mathcal{O}_{\lambda}$ of sheaves of rings
(1.6.1), and $(\mathcal{O}_{\lambda})$ is a projective system of sheaves of rings for these homomorphisms. Since the
topology of $\mathfrak{X}$ admits a base formed of quasi-compact opens, one may associate to each
$\mathcal{O}_{\lambda}$ a sheaf of pseudo-discrete topological rings (0, 3.8.1) which has $\mathcal{O}_{\lambda}$ as its
underlying sheaf of rings (without topology), and which we shall again denote by $\mathcal{O}_{\lambda}$; and the
$\mathcal{O}_{\lambda}$ again form a projective system of sheaves of topological rings (0, 3.8.2). We shall designate by
$\mathcal{O}_{\mathfrak{X}}$ the sheaf of topological rings on $\mathfrak{X}$, the projective limit of the system
$(\mathcal{O}_{\lambda})$; for every quasi-compact open $U$ of $\mathfrak{X}$, $\Gamma(U, \mathcal{O}_{\mathfrak{X}})$
is therefore the topological ring projective limit of the system of discrete rings $\Gamma(U, \mathcal{O}_{\lambda})$
(0, 3.2.6).

**Definition (10.1.2).** Given an admissible topological ring $A$, one calls _formal spectrum_ of $A$, and denotes by
$\operatorname{Spf}(A)$, the closed subspace $\mathfrak{X}$ of $\operatorname{Spec}(A)$ formed of the open prime ideals
of $A$. One says that a topologically ringed space is a _formal affine scheme_ if it is isomorphic to a formal spectrum
$\operatorname{Spf}(A) = \mathfrak{X}$ equipped with the sheaf of topological rings $\mathcal{O}_{\mathfrak{X}}$,
projective limit of the sheaves of pseudo-discrete rings $(\widetilde{A/\mathfrak{J}_{\lambda}})|\mathfrak{X}$, where
$\mathfrak{J}_{\lambda}$ runs through the filtered set of ideals of definition of $A$.

When we speak of a formal spectrum $\mathfrak{X} = \operatorname{Spf}(A)$ as a formal affine scheme, it will always be a
question of the topologically ringed space $(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$ where
$\mathcal{O}_{\mathfrak{X}}$ is defined as above.

One will note that every affine scheme $X = \operatorname{Spec}(A)$ may be considered as a formal affine scheme in one
and only one way, by considering $A$ as a discrete topological ring: the topological rings $\Gamma(U, \mathcal{O}_{X})$
are then discrete when $U$ is quasi-compact (but not in general when $U$ is an arbitrary open of $X$).

**Proposition (10.1.3).** If $\mathfrak{X} = \operatorname{Spf}(A)$, where $A$ is an admissible ring, then
$\Gamma(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$ is topologically isomorphic to $A$.

**Proof.** Indeed, since $\mathfrak{X}$ is closed in $\operatorname{Spec}(A)$, it is quasi-compact, and consequently
$\Gamma(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$ is topologically isomorphic to the projective limit of the discrete
rings $\Gamma(\mathfrak{X}, \mathcal{O}_{\lambda})$; but $\Gamma(\mathfrak{X}, \mathcal{O}_{\lambda})$ is isomorphic to
$A/\mathfrak{J}_{\lambda}$ (1.3.7); since $A$ is separated and complete, it is topologically isomorphic to $\varprojlim
A/\mathfrak{J}_{\lambda}$ (0, 7.2.1), whence the proposition.

**Proposition (10.1.4).** Let $A$ be an admissible ring, $\mathfrak{X} = \operatorname{Spf}(A)$, and for every $f \in
A$, let $\mathfrak{D}(f) = D(f) \cap \mathfrak{X}$; the topologically ringed space $(\mathfrak{D}(f),
\mathcal{O}_{\mathfrak{X}}|\mathfrak{D}(f))$ is isomorphic to the formal affine spectrum $\operatorname{Spf}(A_{\{f\}})$
(0, 7.6.15).

**Proof.** For every ideal of definition $\mathfrak{J}$ of $A$, the discrete ring
$\widetilde{A_{\{f\}}/\mathfrak{J}_{\{f\}}}$ is identified canonically with $A_{f}/\mathfrak{J}_{f}$ (0, 7.6.9); hence
(1.2.5 and 1.2.6) the topological space $\operatorname{Spf}(A_{\{f\}})$ is identified canonically with
$\mathfrak{D}(f)$. Moreover, for every quasi-compact open $U$ of $\mathfrak{X}$ contained in $\mathfrak{D}(f)$,
$\Gamma(U, \mathcal{O}_{\mathfrak{X}})$ is identified with the module of sections of the structure sheaf of
$\operatorname{Spec}(A_{f}/\mathfrak{J}_{f})$ over $U$ (1.3.6); hence, if one sets $\mathfrak{Y} =
\operatorname{Spf}(A_{\{f\}})$, then $\Gamma(U, \mathcal{O}_{\mathfrak{X}})$ is identified with the module of sections
$\Gamma(U, \mathcal{O}_{\mathfrak{Y}})$, which proves the proposition.

**(10.1.5)** As a sheaf of rings without topology, the structure sheaf $\mathcal{O}_{\mathfrak{X}}$ of
$\operatorname{Spf}(A)$ admits, for every $x \in \mathfrak{X}$, a stalk which, by virtue of (10.1.4), is identified with
the inductive limit $\varinjlim A_{\{f\}}$ for $f \notin x$. Consequently (0, 7.6.17 and 7.6.18):

**Proposition (10.1.6).** For every $x \in \mathfrak{X} = \operatorname{Spf}(A)$, the stalk $\mathcal{O}_{x}$ is a local
ring whose residue field is isomorphic to $\kappa(x) = A_{x}/\mathfrak{j}_{x}A_{x}$. If in addition $A$ is adic and
Noetherian, $\mathcal{O}_{x}$ is a Noetherian ring.

Since $\kappa(x)$ is not reduced to $0$, one concludes from this result that the support of the sheaf of rings
$\mathcal{O}_{\mathfrak{X}}$ is equal to $\mathfrak{X}$.

## 10.2. Morphisms of formal affine schemes

<!-- label: I.10.2 -->

**(10.2.1)** Let $A$, $B$ be two admissible rings, and let $\varphi : B \to A$ be a continuous homomorphism. The
continuous map ${}^{a}\varphi : \operatorname{Spec}(A) \to \operatorname{Spec}(B)$ (1.2.1) then sends $\mathfrak{X} =
\operatorname{Spf}(A)$ into $\mathfrak{Y} = \operatorname{Spf}(B)$, for the inverse image under $\varphi$ of an open
prime ideal of $A$ is an open prime ideal of $B$. On the other hand, for every $g \in B$, $\varphi$ defines a continuous
homomorphism $\Gamma(\mathfrak{D}(g), \mathcal{O}_{\mathfrak{Y}}) \to \Gamma(\mathfrak{D}(\varphi(g)),
\mathcal{O}_{\mathfrak{X}})$ by virtue of (10.1.4), (10.1.3), and (0, 7.6.7); since these homomorphisms satisfy the
conditions of compatibility for the restrictions corresponding to the passage from $g$ to a multiple of $g$, and since
$\mathfrak{D}(\varphi(g)) = {}^{a}\varphi^{-1}(\mathfrak{D}(g))$, they define a continuous homomorphism of sheaves of
topological rings $\theta : \mathcal{O}_{\mathfrak{Y}} \to \psi_{*}(\mathcal{O}_{\mathfrak{X}})$ (0, 3.2.5), which we
shall again denote by $\widetilde{\varphi}$; one has thus obtained a morphism $({}^{a}\varphi, \widetilde{\varphi})$ of
topologically ringed spaces $\mathfrak{X} \to \mathfrak{Y}$. One will note that, as a homomorphism of sheaves of rings
without topology, $\widetilde{\varphi}$ defines a homomorphism $\widetilde{\varphi}_{x}^{\sharp} :
\mathcal{O}_{{}^{a}\varphi(x)} \to \mathcal{O}_{x}$ on the stalks, for every $x \in \mathfrak{X}$.

**Proposition (10.2.2).** Let $A$, $B$ be two admissible topological rings, and let $\mathfrak{X} =
\operatorname{Spf}(A)$, $\mathfrak{Y} = \operatorname{Spf}(B)$. For a morphism $u = (\psi, \theta) : \mathfrak{X} \to
\mathfrak{Y}$ of topologically ringed spaces to be of the form $({}^{a}\varphi, \widetilde{\varphi})$, where $\varphi$
is a continuous ring homomorphism $B \to A$, it is necessary and sufficient that for every $x \in \mathfrak{X}$,
$\theta_{x}^{\sharp}$ be a local homomorphism $\mathcal{O}_{\psi(x)} \to \mathcal{O}_{x}$.

**Proof.** The condition is necessary: indeed, let $\mathfrak{p} = \mathfrak{j}_{x} \in \operatorname{Spf}(A)$, and let
$\mathfrak{q} = \varphi^{-1}(\mathfrak{p})$; if $g \notin \mathfrak{q}$, one has $\varphi(g) \notin \mathfrak{p}$, and
it is immediate that the homomorphism $B_{\mathfrak{q}} \to A_{\mathfrak{p}}$ deduced from $\varphi$ (0, 7.6.7)
transforms $\mathfrak{q}B_{\mathfrak{q}}$ into a part of $\mathfrak{p}A_{\mathfrak{p}}$; passing to the inductive limit,
one sees therefore (taking account of (10.1.5) and of (0, 7.6.17)) that $\widetilde{\varphi}_{x}^{\sharp}$ is a local
homomorphism.

Conversely, let $(\psi, \theta)$ be a morphism verifying the condition of the statement; by virtue of (10.1.3), $\theta$
defines a continuous ring homomorphism
$$ \varphi = \Gamma(\theta) : B = \Gamma(\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}}) \to \Gamma(\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}) = A. $$
By virtue of the hypothesis on $\theta$, for the section $\varphi(g)$ of $\mathcal{O}_{\mathfrak{X}}$ over $\mathfrak{X}$
to have an invertible germ at the point $x$, it is necessary and sufficient that $g$ have an invertible germ at the point
$\psi(x)$. But by virtue of (0, 7.6.17), the sections of $\mathcal{O}_{\mathfrak{X}}$ (resp. $\mathcal{O}_{\mathfrak{Y}}$)
over $\mathfrak{X}$ (resp. $\mathfrak{Y}$) whose germ is not invertible at the point $x$ (resp. $\psi(x)$) are exactly the
elements of $\mathfrak{j}_{x}$ (resp. $\mathfrak{j}_{\psi(x)}$); the preceding remark thus shows that $\psi = {}^{a}\varphi$.
Finally, for every $g \in B$, the diagram
$$ \begin{array}{ccc} B = \Gamma(\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}}) & \longrightarrow & \Gamma(\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}) = A \\ \downarrow & & \downarrow \\ B_{\{g\}} = \Gamma(\mathfrak{D}(g),
\mathcal{O}_{\mathfrak{Y}}) & \longrightarrow & \Gamma(\mathfrak{D}(\varphi(g)), \mathcal{O}_{\mathfrak{X}}) =
A_{\{\varphi(g)\}} \end{array} $$
is commutative; by the universal property of the complete rings of fractions (0, 7.6.6), $\theta_{g}$ is equal to
$\widetilde{\varphi}_{g}$ for every $g \in B$, hence (0, 3.2.5) one has $\theta = \widetilde{\varphi}$.

We shall say that a morphism $(\psi, \theta)$ of topologically ringed spaces verifying the condition of (10.2.2) is a
_morphism of formal affine schemes_. One may say that the functors $\operatorname{Spf}(A)$ in $A$ and
$\Gamma(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$ in $\mathfrak{X}$ define an equivalence between the category of
admissible rings and the dual category of the category of formal affine schemes (T, I, 1.2).

**(10.2.3)** As a particular case of (10.2.2), let us note that, for $f \in A$, the canonical injection of the formal
affine scheme induced by $\mathfrak{X}$ on $\mathfrak{D}(f)$ corresponds to the canonical continuous homomorphism $A \to
A_{\{f\}}$. Under the hypotheses of (10.2.2), let $h$ be an element of $B$ and $g$ an element of $A$, a multiple of
$\varphi(h)$; one then has $\psi(\mathfrak{D}(g)) \subset \mathfrak{D}(h)$; the restriction of $u$ to $\mathfrak{D}(g)$,
considered as a morphism of $\mathfrak{D}(g)$ into $\mathfrak{D}(h)$, is the unique morphism $v$ making commutative the
diagram
$$ \begin{array}{ccc} \mathfrak{D}(g) & \xrightarrow{v} & \mathfrak{D}(h) \\ \downarrow & & \downarrow \\ \mathfrak{X} &
\xrightarrow{u} & \mathfrak{Y} \end{array} $$
This morphism corresponds to the unique continuous homomorphism $\varphi' : B_{\{h\}} \to A_{\{g\}}$ (0, 7.6.7) making
commutative the diagram
$$ \begin{array}{ccc} A & \xleftarrow{\varphi} & B \\ \downarrow & & \downarrow \\ A_{\{g\}} & \xleftarrow{\varphi'} &
B_{\{h\}} \end{array} $$

## 10.3. Ideals of definition of a formal affine scheme

<!-- label: I.10.3 -->

**(10.3.1)** Let $A$ be an admissible ring, $\mathfrak{J}$ an open ideal of $A$, $\mathfrak{X}$ the formal affine scheme
$\operatorname{Spf}(A)$. Let $(\mathfrak{J}_{\lambda})$ be the set of ideals of definition of $A$ contained in
$\mathfrak{J}$; then $\widetilde{\mathfrak{J}/\mathfrak{J}_{\lambda}}$ is a sheaf of ideals of
$\widetilde{A/\mathfrak{J}_{\lambda}}$. Let us designate by $\mathfrak{J}^{\Delta}$ the projective limit of the sheaves
induced on $\mathfrak{X}$ by $\widetilde{\mathfrak{J}/\mathfrak{J}_{\lambda}}$, which is identified with a sheaf of
ideals of $\mathcal{O}_{\mathfrak{X}}$ (0, 3.2.6). For every $f \in A$, $\Gamma(\mathfrak{D}(f), \mathfrak{J}^{\Delta})$
is the projective limit of $\mathfrak{J}_{f}/(\mathfrak{J}_{\lambda})_{f}$, in other words is identified with the open
ideal $\mathfrak{J}_{\{f\}}$ of the ring $A_{\{f\}}$ (0, 7.6.9), and in particular $\Gamma(\mathfrak{X},
\mathfrak{J}^{\Delta}) = \mathfrak{J}$; one concludes (the $\mathfrak{D}(f)$ forming a base for the topology of
$\mathfrak{X}$) that one has

$$ \mathfrak{J}_{\{f\}} = (\mathfrak{J}^{\Delta})_{\{f\}} \tag{10.3.1.1} $$

**(10.3.2)** With the notations of (10.3.1), for every $f \in A$, the canonical map of $A_{\{f\}} =
\Gamma(\mathfrak{D}(f), \mathcal{O}_{\mathfrak{X}})$ into $\Gamma(\mathfrak{D}(f), \widetilde{(A/\mathfrak{J})_{f}}) =
A_{f}/\mathfrak{J}_{f}$ is surjective and has for kernel $\Gamma(\mathfrak{D}(f), \mathfrak{J}^{\Delta}) =
\mathfrak{J}_{\{f\}}$ (0, 7.6.9); these maps therefore define a continuous surjective homomorphism, said to be
_canonical_, of the sheaf of topological rings $\mathcal{O}_{\mathfrak{X}}$ onto the sheaf of discrete rings
$(\widetilde{A/\mathfrak{J}})|\mathfrak{X}$ whose kernel is $\mathfrak{J}^{\Delta}$; this homomorphism is moreover none
other than $\widetilde{\varphi}$ (10.2.1), where $\varphi$ is the continuous homomorphism $A \to A/\mathfrak{J}$; the
morphism $(\psi, \theta) : \operatorname{Spec}(A/\mathfrak{J}) \to \mathfrak{X}$ of formal affine schemes (where $\psi$
is moreover the identity homeomorphism of $\mathfrak{X}$ onto itself) is again said to be _canonical_. One therefore
has, by what precedes, a canonical isomorphism

$$ \mathcal{O}_{\mathfrak{X}}/\mathfrak{J}^{\Delta} \cong (\widetilde{A/\mathfrak{J}})|\mathfrak{X} \tag{10.3.2.1} $$

It is clear (by virtue of $\Gamma(\mathfrak{X}, \mathfrak{J}^{\Delta}) = \mathfrak{J}$) that the map $\mathfrak{J} \to
\mathfrak{J}^{\Delta}$ is strictly increasing; by what precedes, for $\mathfrak{J} \subset \mathfrak{J}'$, the sheaf
$\mathfrak{J}^{\Delta}/\mathfrak{J}'^{\Delta}$ is canonically isomorphic to $\widetilde{\mathfrak{J}/\mathfrak{J}'} =
(\mathfrak{J}/\mathfrak{J}')^{\sim}$.

**(10.3.3)** The hypotheses and notations still being those of (10.3.1), we shall say that a sheaf of ideals
$\mathcal{I}$ of $\mathcal{O}_{\mathfrak{X}}$ is a _sheaf of ideals of definition_ of $\mathfrak{X}$ (or an _Ideal of
definition_ of $\mathfrak{X}$) if, for every $x \in \mathfrak{X}$, there exists an open neighborhood of $x$ of the form
$\mathfrak{D}(f)$, where $f \in A$, such that $\mathcal{I}|\mathfrak{D}(f)$ is of the form $\mathfrak{g}^{\Delta}$,
where $\mathfrak{g}$ is an ideal of definition of $A_{\{f\}}$.

**Proposition (10.3.4).** For every $f \in A$, every Ideal of definition of $\mathfrak{X}$ induces an Ideal of
definition of $\mathfrak{D}(f)$.

**Proof.** This results from (10.3.1.1).

**Proposition (10.3.5).** If $A$ is an admissible ring, every Ideal of definition of $\mathfrak{X} =
\operatorname{Spf}(A)$ is of the form $\mathfrak{J}^{\Delta}$, where $\mathfrak{J}$ is an ideal of definition of $A$,
uniquely determined.

**Proof.** Indeed, let $\mathcal{I}$ be an Ideal of definition of $\mathfrak{X}$; by hypothesis, and since
$\mathfrak{X}$ is quasi-compact, there is a finite number of elements $f_{i} \in A$ such that the $\mathfrak{D}(f_{i})$
cover $\mathfrak{X}$ and that $\mathcal{I}|\mathfrak{D}(f_{i}) = \mathfrak{g}_{i}^{\Delta}$, where $\mathfrak{g}_{i}$ is
an ideal of definition of $A_{\{f_{i}\}}$. For each $i$, there exists therefore an open ideal $\mathfrak{K}_{i}$ of $A$
such that $(\mathfrak{K}_{i})_{\{f_{i}\}} = \mathfrak{g}_{i}$ (0, 7.6.9); let $\mathfrak{J}_{1}$ be an ideal of
definition of $A$ contained in all the $\mathfrak{K}_{i}$. The canonical image of
$\mathcal{I}/\mathfrak{J}_{1}^{\Delta}$ in the structure sheaf $(\widetilde{A/\mathfrak{J}_{1}})$ of
$\operatorname{Spec}(A/\mathfrak{J}_{1})$ (10.3.2) is then such that its restriction to $\mathfrak{D}(f_{i})$ is equal
to that of $(\widetilde{\mathfrak{K}_{i}/\mathfrak{J}_{1}})$; one concludes that this canonical image is a
quasi-coherent sheaf on $\operatorname{Spec}(A/\mathfrak{J}_{1})$, hence of the form
$(\widetilde{\mathfrak{J}/\mathfrak{J}_{1}})$, where $\mathfrak{J}$ is an ideal of $A$ containing $\mathfrak{J}_{1}$
(1.4.1), whence $\mathcal{I} = \mathfrak{J}^{\Delta}$ (10.3.2); moreover, since for each $i$ there exists an integer
$n_{i}$ such that $\mathfrak{g}_{i}^{n_{i}} \subset (\mathfrak{J}_{1})_{\{f_{i}\}}$, one will have, denoting by $n$ the
largest of the $n_{i}$, $(\mathfrak{J}/\mathfrak{J}_{1})^{n}|\mathfrak{D}(f_{i}) = 0$, and consequently (10.3.2)
$((\mathfrak{J}/\mathfrak{J}_{1})^{n})^{\Delta} = 0$, whence finally $(\mathfrak{J}/\mathfrak{J}_{1})^{n} = 0$ (1.3.13),
which proves that $\mathfrak{J}$ is an ideal of definition of $A$ (0, 7.1.4).

**Proposition (10.3.6).** Let $A$ be an adic ring, $\mathfrak{J}$ an ideal of definition of $A$ such that
$\mathfrak{J}/\mathfrak{J}^{2}$ is an $(A/\mathfrak{J})$-module of finite type. For every integer $n > 0$, one then has
$(\mathfrak{J}^{\Delta})^{n} = (\mathfrak{J}^{n})^{\Delta}$.

**Proof.** Indeed, for every $f \in A$, one has (since $\mathfrak{J}^{n}$ is an open ideal) $$
((\mathfrak{J}^{\Delta})^{n})_{\{f\}} = ((\mathfrak{J}^{\Delta})_{\{f\}})^{n} = (\mathfrak{J}_{\{f\}})^{n} =
(\mathfrak{J}^{n})_{\{f\}} = ((\mathfrak{J}^{n})^{\Delta})_{\{f\}} $$ by virtue of (10.3.1.1) and of (0, 7.6.12). Since
$(\mathfrak{J}^{\Delta})^{n}$ is associated to the presheaf $U \to (\Gamma(U, \mathfrak{J}^{\Delta}))^{n}$ (0, 4.1.6),
the corollary results from this, since the $\mathfrak{D}(f)$ form a base for the topology of $\mathfrak{X}$.

**(10.3.7)** One says that a family $(\mathcal{I}_{\lambda})$ of Ideals of definition of $\mathfrak{X}$ is a
_fundamental system of Ideals of definition_ if every Ideal of definition of $\mathfrak{X}$ contains one of the
$\mathcal{I}_{\lambda}$; since $\mathcal{I}_{\lambda} = \mathfrak{J}_{\lambda}^{\Delta}$, it amounts to the same to say
that the $\mathfrak{J}_{\lambda}$ form a fundamental system of neighborhoods of $0$ in $A$. Let $(f_{\alpha})$ be a
family of elements of $A$ such that the $\mathfrak{D}(f_{\alpha})$ cover $\mathfrak{X}$. If $(\mathcal{I}_{\lambda})$ is
a filtered decreasing family of ideals of $\mathcal{O}_{\mathfrak{X}}$ such that for every $\alpha$, the family
$(\mathcal{I}_{\lambda}|\mathfrak{D}(f_{\alpha}))$ is a fundamental system of Ideals of definition of
$\mathfrak{D}(f_{\alpha})$, then $(\mathcal{I}_{\lambda})$ is a fundamental system of Ideals of definition of
$\mathfrak{X}$.

**Proof.** Indeed, for every Ideal of definition $\mathcal{I}$ of $\mathfrak{X}$, there is a finite covering of
$\mathfrak{X}$ by sets $\mathfrak{D}(f_{i})$ such that, for each $i$, $\mathcal{I}|\mathfrak{D}(f_{i})$ is an Ideal of
definition of $\mathfrak{D}(f_{i})$ contained in $\mathcal{I}_{\lambda}|\mathfrak{D}(f_{i})$. If $\mu$ is an index such
that $\mathcal{I}_{\mu} \subset \mathcal{I}_{\lambda_{i}}$ for all $i$, it results from (10.3.3) that
$\mathcal{I}_{\mu}$ is an Ideal of definition of $\mathfrak{X}$, evidently contained in $\mathcal{I}$, whence our
assertion.

## 10.4. Formal preschemes and morphisms of formal preschemes

<!-- label: I.10.4 -->

**(10.4.1)** Given a topologically ringed space $X$, one says that an open $U \subset X$ is a _formal affine open_
(resp. an _adic formal affine open_, resp. a _Noetherian formal affine open_) if the topologically ringed space induced
by $X$ on $U$ is a formal affine scheme (resp. such a scheme whose ring is adic, resp. adic and Noetherian).

**Definition (10.4.2).** One calls _formal prescheme_ a topologically ringed space $\mathfrak{X}$ every point of which
admits a formal affine open neighborhood. One says that the formal prescheme $\mathfrak{X}$ is _adic_ (resp. _locally
Noetherian_) if every point of $\mathfrak{X}$ admits an adic (resp. Noetherian) formal affine open neighborhood. One
says that $\mathfrak{X}$ is _Noetherian_ if it is locally Noetherian and if its underlying space is quasi-compact (hence
Noetherian).

**Proposition (10.4.3).** If $\mathfrak{X}$ is a formal prescheme (resp. locally Noetherian), the formal affine opens
(resp. Noetherian affine opens) form a base for the topology of $\mathfrak{X}$.

**Proof.** This results from (10.4.2) and (10.1.4), taking account of the fact that if $A$ is an adic Noetherian ring,
so is $A_{\{f\}}$ for every $f \in A$ (0, 7.6.11).

**Corollary (10.4.4).** If $\mathfrak{X}$ is a formal prescheme (resp. a locally Noetherian formal prescheme, resp.
Noetherian), the topologically ringed space induced on every open of $\mathfrak{X}$ is again a formal prescheme (resp. a
locally Noetherian formal prescheme, resp. Noetherian).

**Definition (10.4.5).** Given two formal preschemes $\mathfrak{X}$, $\mathfrak{Y}$, one calls _morphism (of formal
preschemes)_ of $\mathfrak{X}$ into $\mathfrak{Y}$ every morphism $(\psi, \theta)$ of topologically ringed spaces such
that, for every $x \in \mathfrak{X}$, $\theta_{x}^{\sharp}$ is a local homomorphism $\mathcal{O}_{\psi(x)} \to
\mathcal{O}_{x}$.

It is immediate that the composite of two morphisms of formal preschemes is again such a morphism; the formal preschemes
therefore form a category, and one will denote by $\operatorname{Hom}(\mathfrak{X}, \mathfrak{Y})$ the set of morphisms
of a formal prescheme $\mathfrak{X}$ into a formal prescheme $\mathfrak{Y}$.

If $U$ is an open part of $\mathfrak{X}$, the canonical injection into $\mathfrak{X}$ of the formal prescheme induced by
$\mathfrak{X}$ on $U$ is a morphism of formal preschemes (and even a monomorphism of topologically ringed spaces (0,
4.1.1)).

**Proposition (10.4.6).** Let $\mathfrak{X}$ be a formal prescheme, $\mathfrak{G} = \operatorname{Spf}(A)$ a formal
affine scheme. There exists a canonical one-to-one correspondence between the morphisms of the formal prescheme
$\mathfrak{X}$ into the formal prescheme $\mathfrak{G}$ and the continuous homomorphisms of the ring $A$ into the
topological ring $\Gamma(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$.

**Proof.** The demonstration is the same as that of (2.2.4), replacing "homomorphism" by "continuous homomorphism",
"affine open" by "formal affine open", and using (10.2.2) instead of (1.7.3); we leave the details to the reader.

**(10.4.7)** Given a formal prescheme $\mathfrak{G}$, one says that the datum of a formal prescheme $\mathfrak{X}$ and
of a morphism $\varphi : \mathfrak{X} \to \mathfrak{G}$ defines a _formal prescheme $\mathfrak{X}$ over $\mathfrak{G}$_,
or a _$\mathfrak{G}$-formal prescheme_, $\varphi$ being called the _structure morphism_ of the $\mathfrak{G}$-prescheme
$\mathfrak{X}$. If $\mathfrak{G} = \operatorname{Spf}(A)$, where $A$ is an admissible ring, one also says that the
$\mathfrak{G}$-formal prescheme $\mathfrak{X}$ is an _$A$-formal prescheme_ or a _formal prescheme over $A$_. An
arbitrary formal prescheme may always be considered as a formal prescheme over $\mathbf{Z}$ (equipped with the discrete
topology).

If $\mathfrak{X}$, $\mathfrak{Y}$ are two $\mathfrak{G}$-formal preschemes, one says that a morphism $u : \mathfrak{X} \to
\mathfrak{Y}$ is a _$\mathfrak{G}$-morphism_ if the diagram
$$ \begin{array}{ccc} \mathfrak{X} & \xrightarrow{u} & \mathfrak{Y} \\ & \searrow \quad \swarrow & \\ & \mathfrak{G} &
\end{array} $$
(where the oblique arrows are the structure morphisms) is commutative. With this definition, the
$\mathfrak{G}$-formal preschemes (for fixed $\mathfrak{G}$) form a category. One designates by
$\operatorname{Hom}_{\mathfrak{G}}(\mathfrak{X}, \mathfrak{Y})$ the set of $\mathfrak{G}$-morphisms of the
$\mathfrak{G}$-formal prescheme $\mathfrak{X}$ into the $\mathfrak{G}$-formal prescheme $\mathfrak{Y}$. When $\mathfrak{G}
= \operatorname{Spf}(A)$, one also says $A$-morphism instead of $\mathfrak{G}$-morphism.

**(10.4.8)** Since every affine scheme may be considered as a formal affine scheme (10.1.2), every (ordinary) prescheme
may be considered as a formal prescheme. It moreover results from (10.4.5) that for ordinary preschemes, the morphisms
(resp. $\mathfrak{G}$-morphisms) of formal preschemes coincide with the morphisms (resp. $S$-morphisms) defined in §2.

## 10.5. Ideals of definition of formal preschemes

<!-- label: I.10.5 -->

**(10.5.1)** Let $\mathfrak{X}$ be a formal prescheme; one says that an $\mathcal{O}_{\mathfrak{X}}$-Ideal $\mathcal{I}$
is a _sheaf of ideals of definition_ (or an _Ideal of definition_) of $\mathfrak{X}$ if every $x \in \mathfrak{X}$
possesses a formal affine open neighborhood $U$ such that $\mathcal{I}|U$ is an Ideal of definition of the formal affine
scheme induced by $\mathfrak{X}$ on $U$ (10.3.3); by virtue of (10.3.1.1) and (10.4.3), for every open $V \subset
\mathfrak{X}$, $\mathcal{I}|V$ is then an Ideal of definition of the formal prescheme induced by $\mathfrak{X}$ on $V$.

One says that a family $(\mathcal{I}_{\lambda})$ of Ideals of definition of $\mathfrak{X}$ is a _fundamental system of
Ideals of definition_ if there exists a covering $(U_{\alpha})$ of $\mathfrak{X}$ by formal affine opens such that, for
every $\alpha$, the family of $\mathcal{I}_{\lambda}|U_{\alpha}$ is a fundamental system of Ideals of definition
(10.3.6) of the formal affine scheme induced by $\mathfrak{X}$ on $U_{\alpha}$. It results from the final remark of
(10.3.7) that when $\mathfrak{X}$ is a formal affine scheme, this definition coincides with the definition given in
(10.3.7). For every open $V$ of $\mathfrak{X}$, the restrictions $\mathcal{I}_{\lambda}|V$ then form a fundamental
system of Ideals of definition of the formal prescheme induced on $V$, by virtue of (10.3.1.1). If $\mathfrak{X}$ is a
locally Noetherian formal prescheme, and $\mathcal{I}$ an Ideal of definition of $\mathfrak{X}$, it results from
(10.3.6) that the powers $\mathcal{I}^{n}$ form a fundamental system of Ideals of definition of $\mathfrak{X}$.

**(10.5.2)** Let $\mathfrak{X}$ be a formal prescheme, $\mathcal{I}$ an Ideal of definition of $\mathfrak{X}$. Then the
ringed space $(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{I})$ is an (ordinary) prescheme, which is affine (resp.
locally Noetherian, resp. Noetherian) when $\mathfrak{X}$ is a formal affine scheme (resp. a locally Noetherian formal
prescheme, resp. Noetherian); one is indeed at once reduced to the affine case, and then the proposition has already
been demonstrated in (10.3.2). Moreover, if $\theta : \mathcal{O}_{\mathfrak{X}} \to
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}$ is the canonical homomorphism, $u = (1_{\mathfrak{X}}, \theta)$ is a morphism
(said to be _canonical_) of formal preschemes $(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{I}) \to (\mathfrak{X},
\mathcal{O}_{\mathfrak{X}})$, for here again, this has been seen in the affine case (10.3.2), to which one reduces at
once.

**Proposition (10.5.3).** Let $\mathfrak{X}$ be a formal prescheme, $(\mathcal{I}_{\lambda})$ a fundamental system of
Ideals of definition of $\mathfrak{X}$. Then the sheaf of topological rings $\mathcal{O}_{\mathfrak{X}}$ is the
projective limit of the sheaves of pseudo-discrete rings (0, 3.8.1) $\mathcal{O}_{\mathfrak{X}}/\mathcal{I}_{\lambda}$.

**Proof.** Since the topology of $\mathfrak{X}$ admits a base of quasi-compact formal affine opens (10.4.3), one is
reduced to the affine case, where the proposition is a consequence of (10.3.5), (10.3.2), and of the definition
(10.1.1).

It is not certain that every formal prescheme admits Ideals of definition. However:

**Proposition (10.5.4).** Let $\mathfrak{X}$ be a locally Noetherian formal prescheme. There exists a largest Ideal of
definition $\mathcal{T}$ of $\mathfrak{X}$; it is the only Ideal of definition $\mathcal{I}$ such that the prescheme
$(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{I})$ is reduced. If $\mathcal{I}$ is an Ideal of definition of
$\mathfrak{X}$, $\mathcal{T}$ is the inverse image under $\mathcal{O}_{\mathfrak{X}} \to
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}$ of the Nilradical of $\mathcal{O}_{\mathfrak{X}}/\mathcal{I}$.

**Proof.** Suppose first that $\mathfrak{X} = \operatorname{Spf}(A)$, where $A$ is an adic Noetherian ring. The
existence and properties of $\mathcal{T}$ result immediately from (10.3.4) and (5.1.1), taking account of the existence
and properties of the largest ideal of definition of $A$ (0, 7.1.6 and 7.1.7).

To prove the existence and properties of $\mathcal{T}$ in the general case, it suffices to show that if $U \supset V$
are two Noetherian formal affine opens of $\mathfrak{X}$, the largest Ideal of definition $\mathcal{T}_{U}$ of $U$
induces the largest Ideal of definition $\mathcal{T}_{V}$ of $V$; but since $(V,
(\mathcal{O}_{\mathfrak{X}}|V)/(\mathcal{T}_{U}|V))$ is reduced, this results from what precedes.

One designates by $\mathfrak{X}_{\mathrm{red}}$ the (ordinary) reduced prescheme $(\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}/\mathcal{T})$.

**Corollary (10.5.5).** Let $\mathfrak{X}$ be a locally Noetherian formal prescheme, $\mathcal{T}$ the largest Ideal of
definition of $\mathfrak{X}$; for every open $V$ of $\mathfrak{X}$, $\mathcal{T}|V$ is the largest Ideal of definition
of the formal prescheme induced by $\mathfrak{X}$ on $V$.

**Proposition (10.5.6).** Let $\mathfrak{X}$, $\mathfrak{Y}$ be two formal preschemes, $\mathcal{I}$ (resp.
$\mathcal{J}$) an Ideal of definition of $\mathfrak{X}$ (resp. $\mathfrak{Y}$), $f : \mathfrak{X} \to \mathfrak{Y}$ a
morphism of formal preschemes.

(i) If $f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{I}$, there exists a unique morphism $f' :
(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{I}) \to (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}}/\mathcal{J})$ of
ordinary preschemes making commutative the diagram

$$ \begin{array}{ccc} (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}) & \xrightarrow{f} & (\mathfrak{Y},
\mathcal{O}_{\mathfrak{Y}}) \\ \uparrow & & \uparrow \\ (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{I}) &
\xrightarrow{f'} & (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}}/\mathcal{J}) \end{array} \tag{10.5.6.1} $$

where the vertical arrows are the canonical morphisms.

(ii) Suppose that $\mathfrak{X} = \operatorname{Spf}(A)$, $\mathfrak{Y} = \operatorname{Spf}(B)$ are formal affine
schemes, $\mathcal{I} = \mathfrak{J}^{\Delta}$, $\mathcal{J} = \mathfrak{K}^{\Delta}$, where $\mathfrak{J}$ (resp.
$\mathfrak{K}$) is an ideal of definition of $A$ (resp. $B$), and $f = ({}^{a}\varphi, \widetilde{\varphi})$, where
$\varphi : B \to A$ is a continuous homomorphism; for $f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} \subset
\mathcal{I}$, it is necessary and sufficient that $\varphi(\mathfrak{K}) \subset \mathfrak{J}$, and $f'$ is then the
morphism $({}^{a}\varphi', \widetilde{\varphi'})$, where $\varphi' : B/\mathfrak{K} \to A/\mathfrak{J}$ is the
homomorphism deduced from $\varphi$ by passage to the quotients.

**Proof.** (i) If $f = (\psi, \theta)$, the hypothesis entails that the image under $\theta^{*} : \psi^{*}(\mathcal{J})
\to \mathcal{O}_{\mathfrak{X}}$ of the sheaf of ideals $\psi^{*}(\mathcal{J})$ of $\psi^{*}(\mathcal{O}_{\mathfrak{Y}})$
is contained in $\mathcal{I}$ (0, 4.3.5). By passage to the quotients, one therefore deduces from $\theta^{\sharp}$ a
homomorphism of sheaves of rings $$ \omega : \psi^{*}(\mathcal{O}_{\mathfrak{Y}}/\mathcal{J}) =
\psi^{*}(\mathcal{O}_{\mathfrak{Y}})/\psi^{*}(\mathcal{J}) \to \mathcal{O}_{\mathfrak{X}}/\mathcal{I}; $$ moreover,
since for every $x \in \mathfrak{X}$, $\theta_{x}^{\sharp}$ is a local homomorphism, so is $\omega_{x}$. The morphism of
ringed spaces $(\psi, \omega)$ is therefore (2.2.1) the unique morphism $f'$ of ringed spaces answering the question.

(ii) The canonical functorial correspondence between morphisms of formal affine preschemes and continuous homomorphisms
of rings (10.2.2) shows that in the case considered, the relation $f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} \subset
\mathcal{I}$ entails that one has $f' = ({}^{a}\varphi', \widetilde{\varphi'})$, where $\varphi' : B/\mathfrak{K} \to
A/\mathfrak{J}$ is the unique homomorphism making commutative the diagram

$$ \begin{array}{ccc} B & \xrightarrow{\varphi} & A \\ \downarrow & & \downarrow \\ B/\mathfrak{K} & \xrightarrow{\varphi'}
& A/\mathfrak{J} \end{array} \tag{10.5.6.2} $$

The existence of $\varphi'$ therefore implies that $\varphi(\mathfrak{K}) \subset \mathfrak{J}$. Conversely, if this
condition is verified, then, denoting by $\varphi'$ the unique homomorphism making commutative the diagram (10.5.6.2)
and setting $f' = ({}^{a}\varphi', \widetilde{\varphi'})$, it is clear that the diagram (10.5.6.1) is commutative; the
consideration of the homomorphisms $\psi^{*}(\mathcal{J}) \to \mathcal{I}$ and
$\psi^{*}(\mathcal{O}_{\mathfrak{Y}}/\mathcal{J}) \to \mathcal{O}_{\mathfrak{X}}/\mathcal{I}$ corresponding to $f$ and
$f'$ respectively then shows that this entails the relation $f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} \subset
\mathcal{I}$.

It is clear that the correspondence $f \to f'$ defined above is functorial.

## 10.6. Formal preschemes as inductive limits of preschemes

<!-- label: I.10.6 -->

**(10.6.1)** Let $\mathfrak{X}$ be a formal prescheme, $(\mathcal{I}_{\lambda})$ a fundamental system of Ideals of
definition of $\mathfrak{X}$; for each $\lambda$, let $f_{\lambda}$ be the canonical morphism $(\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}_{\lambda}) \to \mathfrak{X}$ (10.5.2); for $\mathcal{I}_{\mu} \subset
\mathcal{I}_{\lambda}$, the canonical homomorphism $\mathcal{O}_{\mathfrak{X}}/\mathcal{I}_{\mu} \to
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}_{\lambda}$ defines a canonical morphism $f_{\lambda\mu} : (\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}_{\lambda}) \to (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{I}_{\mu})$ of
(ordinary) preschemes such that one has $f_{\lambda} = f_{\mu} \circ f_{\lambda\mu}$. The preschemes $X_{\lambda} =
(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{I}_{\lambda})$ and the morphisms $f_{\lambda\mu}$ therefore
constitute (by virtue of (10.4.8)) an inductive system in the category of formal preschemes.

**Proposition (10.6.2).** With the notations of (10.6.1), the formal prescheme $\mathfrak{X}$ and the morphisms
$f_{\lambda}$ constitute an inductive limit (T, I, 1.8) of the system $(X_{\lambda}, f_{\lambda\mu})$ in the category of
formal preschemes.

**Proof.** Let $\mathfrak{Y}$ be a formal prescheme, and for each index $\lambda$, let $$ g_{\lambda} = (\psi_{\lambda},
\theta_{\lambda}) : X_{\lambda} \to \mathfrak{Y} $$ be a morphism such that one has $g_{\lambda} = g_{\mu} \circ
f_{\lambda\mu}$ for $\mathcal{I}_{\mu} \subset \mathcal{I}_{\lambda}$. This last condition and the definition of the
$X_{\lambda}$ entail first that all the $\psi_{\lambda}$ are identical to one and the same continuous map $\psi :
\mathfrak{X} \to \mathfrak{Y}$ of the underlying spaces; moreover, the homomorphisms $\theta_{\lambda}^{\sharp} :
\psi^{*}(\mathcal{O}_{\mathfrak{Y}}) \to \mathcal{O}_{X_{\lambda}} = \mathcal{O}_{\mathfrak{X}}/\mathcal{I}_{\lambda}$
form a projective system of homomorphisms of sheaves of rings. By passage to the projective limit, one therefore deduces
a homomorphism $\omega : \psi^{*}(\mathcal{O}_{\mathfrak{Y}}) \to \varprojlim
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}_{\lambda} = \mathcal{O}_{\mathfrak{X}}$, and it is clear that the morphism $g =
(\psi, \omega)$ of ringed spaces is the only one making commutative the diagrams

$$ \begin{array}{ccc} X_{\lambda} & \xrightarrow{g_{\lambda}} & \mathfrak{Y} \\ \downarrow & \nearrow & \\ \mathfrak{X} &
& \end{array} \tag{10.6.2.1} $$

It remains therefore to prove that $g$ is a morphism of formal preschemes; the question being local on $\mathfrak{X}$
and $\mathfrak{Y}$, one may suppose $\mathfrak{X} = \operatorname{Spf}(A)$, $\mathfrak{Y} = \operatorname{Spf}(B)$, $A$
and $B$ being admissible rings, with $\mathcal{I}_{\lambda} = \mathfrak{J}_{\lambda}^{\Delta}$, where
$(\mathfrak{J}_{\lambda})$ is a fundamental system of ideals of definition of $A$ (10.3.5); since $A = \varprojlim
A/\mathfrak{J}_{\lambda}$, the existence of a morphism of formal affine schemes $g$ making commutative the diagrams
(10.6.2.1) results then from the one-to-one correspondence (10.2.2) between morphisms of formal affine schemes and
continuous homomorphisms of rings, and from the definition of the projective limit. But the uniqueness of $g$ as a
morphism of ringed spaces shows that it coincides with the morphism denoted the same way at the beginning of the
demonstration.

The following proposition establishes, under certain supplementary conditions, the existence of the inductive limit of a
given inductive system of (ordinary) preschemes in the category of formal preschemes:

**Proposition (10.6.3).** Let $X$ be a topological space, $(\mathcal{O}_{i}, u_{ij})$ a projective system of sheaves of
rings on $X$, having $\mathbf{N}$ for index set. Let $\mathcal{J}_{i}$ be the kernel of $u_{i0} : \mathcal{O}_{i} \to
\mathcal{O}_{0}$. Suppose that:

a) the ringed space $(X, \mathcal{O}_{0})$ is a prescheme $X_{0}$.

b) for every $x \in X$ and every $i$, there exists an open neighborhood $U_{i}$ of $x$ in $X$ such that the restriction
$\mathcal{J}_{i}|U_{i}$ is nilpotent.

c) the homomorphisms $u_{ij}$ are surjective.

Let $\mathcal{O}_{\infty}$ be the sheaf of topological rings projective limit of the sheaves of pseudo-discrete rings
$\mathcal{O}_{i}$, and let $u_{\infty i} : \mathcal{O}_{\infty} \to \mathcal{O}_{i}$ be the canonical homomorphism. Then
the topologically ringed space $(X, \mathcal{O}_{\infty})$ is a formal prescheme; the homomorphisms $u_{\infty i}$ are
surjective; their kernels $\mathcal{J}_{\infty i}$ form a fundamental system of Ideals of definition of $\mathfrak{X}$,
and $\mathcal{J}_{\infty i}$ is the projective limit of the sheaves of ideals $\mathcal{J}_{ji}$.

**Proof.** Let us first note that on each stalk, $u_{ij}$ is a surjective homomorphism and a fortiori a local
homomorphism; hence $v_{ij} = (1_{X}, u_{ij})$ is a morphism of preschemes $X_{i} \to X_{j}$ ($i \geq j$) (2.2.1).
Suppose first that each $X_{i}$ is an affine scheme with ring $A_{i}$. There exists a ring homomorphism $\varphi_{ij} :
A_{j} \to A_{i}$ such that $u_{ij} = \widetilde{\varphi_{ij}}$ (1.7.3); consequently (1.6.3), the sheaf
$\mathcal{O}_{i}$ is a quasi-coherent $\mathcal{O}_{j}$-Module on $X_{j}$ (for the external law defined by $u_{ij}$),
associated to $A_{i}$ considered as an $A_{j}$-module by means of $\varphi_{ij}$. For every $f \in A_{j}$, let $f' =
\varphi_{ij}(f)$; by hypothesis, the opens $D(f)$ and $D(f')$ are identical in $X$, and the homomorphism of
$\Gamma(D(f), \mathcal{O}_{j}) = (A_{j})_{f}$ into $\Gamma(D(f), \mathcal{O}_{i}) = (A_{i})_{f'}$ corresponding to
$u_{ij}$ is none other than $(\varphi_{ij})_{f}$ (1.6.1). But when one considers $A_{i}$ as an $A_{j}$-module,
$(A_{i})_{f'}$ is the $(A_{j})_{f}$-module $(A_{i})_{f}$, hence one also has $u_{ij} = \widetilde{\varphi_{ij}}$ when
$\varphi_{ij}$ is this time considered as a homomorphism of $A_{j}$-modules. Then, since $u_{ij}$ is surjective, one
concludes that $\varphi_{ij}$ is also (1.3.9), and if $\mathfrak{J}_{ij}$ is the kernel of $\varphi_{ij}$, the kernel of
$u_{ij}$ is a quasi-coherent $\mathcal{O}_{j}$-Module equal to $\widetilde{\mathfrak{J}_{ij}}$. In particular, one has
$\mathcal{J}_{i} = \widetilde{\mathfrak{J}_{i}}$, where $\mathfrak{J}_{i}$ is the kernel of $\varphi_{i0} : A_{i} \to
A_{0}$. Hypothesis b) entails that $\mathcal{J}_{i}$ is nilpotent: indeed, since $X$ is quasi-compact, one may cover $X$
by a finite number of opens $V_{k}$ such that $(\mathcal{J}_{i}|V_{k})^{n_{k}} = 0$, and taking for $n$ the largest of
the $n_{k}$, one has $\mathcal{J}_{i}^{n} = 0$. One concludes that $\mathfrak{J}_{i}$ is nilpotent (1.3.13). Then the
ring $A = \varprojlim A_{i}$ is admissible (0, 7.2.2), the canonical homomorphism $\varphi_{i} : A \to A_{i}$ is
surjective and its kernel $\mathfrak{J}_{\infty i}$ is equal to the projective limit of the $\mathfrak{J}_{ki}$ for $k
\geq i$; the $\mathfrak{J}_{\infty i}$ form a fundamental system of neighborhoods of $0$ in $A$. The assertions of
(10.6.3) result in this case from (10.1.1) and (10.3.2), $(X, \mathcal{O}_{\infty})$ being none other than
$\operatorname{Spf}(A)$.

Still in this same particular case, let us note that if $f = (f_{i})$ is an element of the projective limit $A =
\varprojlim A_{i}$, all the opens $D(f_{i})$ (affine open in $X_{i}$) are identified with the open $\mathfrak{D}(f)$ of
$\mathfrak{X}$, the prescheme induced by $X_{i}$ on $\mathfrak{D}(f)$ being thus identified with the affine scheme
$\operatorname{Spec}((A_{i})_{f})$.

In the general case, let us remark first that for every quasi-compact open $U$ of $X$, each of the $\mathcal{J}_{i}|U$
is nilpotent, as the reasoning made above shows. We shall see that for every $x \in X$, there is an open neighborhood
$U$ of $x$ in $X$ which is an affine open for all the $X_{i}$. Indeed, take $U$ affine open for $X_{0}$, and observe
that $\mathcal{O}_{x_{i}} = \mathcal{O}_{x_{0}}/\mathcal{J}_{i}$. Since $\mathcal{J}_{i}|U$ is nilpotent, by virtue of
what precedes, $U$ is affine open also for each $X_{i}$ by virtue of (5.1.9). This being so, for every $U$ satisfying
the preceding conditions, the study of the affine case made above shows that $(U, \mathcal{O}_{\infty}|U)$ is a formal
prescheme of which the $\mathcal{J}_{\infty i}|U$ form a fundamental system of ideals of definition and
$\mathcal{O}_{\infty}|U$ is the projective limit of the $\mathcal{O}_{i}|U$; whence the conclusion.

**Corollary (10.6.4).** Suppose that for $i \geq j$, the kernel of $u_{ij}$ is $\mathcal{J}_{i}^{j+1}$ and that
$\mathcal{J}_{1}/\mathcal{J}_{1}^{2}$ is of finite type over $\mathcal{O}_{0} = \mathcal{O}_{1}/\mathcal{J}_{1}$. Then
$\mathfrak{X}$ is an adic formal prescheme, and if $\mathcal{J}_{\infty}^{(n)}$ is the kernel of $\mathcal{O}_{\infty}
\to \mathcal{O}_{n}$, one has $\mathcal{J}_{\infty}^{(n)} = \mathcal{J}_{\infty}^{n+1}$ and
$\mathcal{J}_{\infty}/\mathcal{J}_{\infty}^{2}$ is isomorphic to $\mathcal{J}_{1}$. If in addition $X_{0}$ is locally
Noetherian (resp. Noetherian), $\mathfrak{X}$ is locally Noetherian (resp. Noetherian).

**Proof.** Since the spaces underlying $\mathfrak{X}$ and $X_{0}$ are the same, the question is local and one may
suppose all the $X_{i}$ affine; taking account of the relations $\mathcal{J}_{i} = \widetilde{\mathfrak{J}_{i}}$ (with
the notations of (10.6.3)), one is at once reduced to the corresponding assertions of (0, 7.2.7 and 7.2.8), noting that
$\mathfrak{J}_{1}/\mathfrak{J}_{1}^{2}$ is then an $A_{0}$-module of finite type (1.3.9).

In particular, every locally Noetherian formal prescheme $\mathfrak{X}$ is the inductive limit of a sequence $(X_{n})$
of (ordinary) locally Noetherian preschemes verifying the conditions of (10.6.3) and (10.6.4): it suffices to consider
an Ideal of definition $\mathcal{I}$ of $\mathfrak{X}$ (10.5.4) and to take $X_{n} = (\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}^{n+1})$ ((10.5.1) and (10.6.2)).

**Corollary (10.6.5).** Let $A$ be an admissible ring. For the formal affine scheme $\mathfrak{X} =
\operatorname{Spf}(A)$ to be Noetherian, it is necessary and sufficient that $A$ be adic and Noetherian.

**Proof.** The condition is evidently sufficient. Conversely, suppose that $\mathfrak{X}$ is Noetherian, and let
$\mathfrak{J}$ be an ideal of definition of $A$, $\mathcal{I} = \mathfrak{J}^{\Delta}$ the corresponding Ideal of
definition of $\mathfrak{X}$. The (ordinary) preschemes $X_{n} = (\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}^{n+1})$ are then affine and Noetherian, hence the rings $A_{n} =
A/\mathfrak{J}^{n+1}$ are Noetherian (6.1.3), whence one concludes that $\mathfrak{J}/\mathfrak{J}^{2}$ is an
$(A/\mathfrak{J})$-module of finite type. Since the $\mathcal{I}^{n}$ form a fundamental system of Ideals of definition
of $\mathfrak{X}$ (10.5.1), one has $\mathcal{O}_{\mathfrak{X}} = \varprojlim
(\mathcal{O}_{\mathfrak{X}}/\mathcal{I}^{n})$ (10.5.3); one concludes (10.1.3) that $A$ is topologically isomorphic to
$\varprojlim A/\mathfrak{J}^{n}$, hence is adic and Noetherian (0, 7.2.8).

**Remark (10.6.6).** With the notations of (10.6.3), let $\mathcal{F}_{i}$ be an $\mathcal{O}_{i}$-Module, and suppose
given, for $i \geq j$, a $v_{ij}$-morphism $\theta_{ij} : \mathcal{F}_{i} \to \mathcal{F}_{j}$, so that $\theta_{jk}
\circ \theta_{ij} = \theta_{ik}$ for $i \geq j \geq k$. Since the continuous map underlying $v_{ij}$ is the identity,
$\theta_{ij}$ is a homomorphism of sheaves of abelian groups on the space $X$; moreover, if $\mathcal{F}$ is the
projective limit of the projective system $(\mathcal{F}_{i})$ of sheaves of abelian groups, the fact that the
$\theta_{ij}$ are $v_{ij}$-morphisms permits one to define on $\mathcal{F}$ a structure of $\mathcal{O}_{\infty}$-Module
by passage to the projective limit; equipped with this structure, we shall say that $\mathcal{F}$ is the _projective
limit_ (for the $\theta_{ij}$) of the system of $\mathcal{O}_{i}$-Modules $(\mathcal{F}_{i})$. In the particular case
where $v_{ij}^{*}(\mathcal{F}_{j}) = \mathcal{F}_{i}$ and where $\theta_{ij}$ is the identity, we shall say for brevity
that $\mathcal{F}$ is the projective limit of a system $(\mathcal{F}_{i})$ such that $v_{ij}^{*}(\mathcal{F}_{j}) =
\mathcal{F}_{i}$ for $j \leq i$ (without mentioning the $\theta_{ij}$).

**(10.6.7)** Let $\mathfrak{X}$, $\mathfrak{Y}$ be two formal preschemes, $\mathcal{I}$ (resp. $\mathcal{J}$) an Ideal
of definition of $\mathfrak{X}$ (resp. $\mathfrak{Y}$), $f : \mathfrak{X} \to \mathfrak{Y}$ a morphism such that
$f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{I}$. One then has, for every integer $n > 0$,
$f^{*}(\mathcal{J}^{n+1})\mathcal{O}_{\mathfrak{X}} = (f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}})^{n+1} \subset
\mathcal{I}^{n+1}$; one may therefore (10.5.6) deduce from $f$ a morphism of (ordinary) preschemes $f_{n} : X_{n} \to
Y_{n}$, on setting $X_{n} = (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{I}^{n+1})$, $Y_{n} = (\mathfrak{Y},
\mathcal{O}_{\mathfrak{Y}}/\mathcal{J}^{n+1})$, and it results at once from the definitions that the diagrams

$$ \begin{array}{ccc} X_{n} & \xrightarrow{f_{n}} & Y_{n} \\ \uparrow & & \uparrow \\ X_{m} & \xrightarrow{f_{m}} & Y_{m}
\end{array} \tag{10.6.7.1} $$

are commutative for $m \leq n$; in other words, $(f_{n})$ is an inductive system of morphisms.

**(10.6.8)** Conversely, let $(X_{n})$ (resp. $(Y_{n})$) be an inductive system of (ordinary) preschemes satisfying the
conditions b) and c) of (10.6.3), and let $\mathfrak{X}$ (resp. $\mathfrak{Y}$) be its inductive limit. By definition of
inductive limits, every sequence $(f_{n})$ of morphisms $X_{n} \to Y_{n}$ forming an inductive system admits an
inductive limit $f : \mathfrak{X} \to \mathfrak{Y}$, which is the unique morphism of formal preschemes making
commutative the diagrams

$$ \begin{array}{ccc} X_{n} & \xrightarrow{f_{n}} & Y_{n} \\ \downarrow & & \downarrow \\ \mathfrak{X} & \xrightarrow{f}
& \mathfrak{Y} \end{array} $$

**Proposition (10.6.9).** Let $\mathfrak{X}$, $\mathfrak{Y}$ be two locally Noetherian formal preschemes, $\mathcal{I}$
(resp. $\mathcal{J}$) an Ideal of definition of $\mathfrak{X}$ (resp. $\mathfrak{Y}$); the map $f \to (f_{n})$ defined
in (10.6.7) is a bijection of the set of morphisms $f : \mathfrak{X} \to \mathfrak{Y}$ such that
$f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{I}$ onto the set of sequences $(f_{n})$ of morphisms
making commutative the diagrams (10.6.7.1).

**Proof.** If $f$ is the inductive limit of such a sequence, it must be shown that
$f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{I}$. The question being local on $\mathfrak{X}$ and
$\mathfrak{Y}$, one may restrict oneself to the case where $\mathfrak{X} = \operatorname{Spf}(A)$, $\mathfrak{Y} =
\operatorname{Spf}(B)$ are affine, $A$ and $B$ being adic Noetherian, $\mathcal{I} = \mathfrak{J}^{\Delta}$,
$\mathcal{J} = \mathfrak{K}^{\Delta}$, where $\mathfrak{J}$ (resp. $\mathfrak{K}$) is an ideal of definition of $A$
(resp. $B$). One then has $X_{n} = \operatorname{Spec}(A_{n})$, $Y_{n} = \operatorname{Spec}(B_{n})$, with $A_{n} =
A/\mathfrak{J}^{n+1}$ and $B_{n} = B/\mathfrak{K}^{n+1}$, by virtue of (10.3.6) and (10.3.2); $f_{n} =
({}^{a}\varphi_{n}, \widetilde{\varphi_{n}})$, where the homomorphisms $\varphi_{n} : B_{n} \to A_{n}$ form a projective
system, hence $f = ({}^{a}\varphi, \widetilde{\varphi})$, where $\varphi = \varprojlim \varphi_{n}$. The commutativity
of the diagram (10.6.7.1) for $m = 0$ then gives the condition $\varphi_{n}(\mathfrak{K}/\mathfrak{K}^{n+1}) \subset
\mathfrak{J}/\mathfrak{J}^{n+1}$ for every $n$, hence, passing to the projective limit, $\varphi(\mathfrak{K}) \subset
\mathfrak{J}$, and this entails $f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{I}$ (10.5.6, (ii)).

**Corollary (10.6.10).** Let $\mathfrak{X}$, $\mathfrak{Y}$ be two locally Noetherian formal preschemes, $\mathcal{T}$
the largest Ideal of definition of $\mathfrak{X}$ (10.5.4).

(i) For every Ideal of definition $\mathcal{J}$ of $\mathfrak{Y}$ and every morphism $f : \mathfrak{X} \to
\mathfrak{Y}$, one has $f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{T}$.

(ii) There is a canonical one-to-one correspondence between $\operatorname{Hom}(\mathfrak{X}, \mathfrak{Y})$ and the set
of sequences $(f_{n})$ of morphisms making commutative the diagrams (10.6.7.1), where $X_{n} = (\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}/\mathcal{T}^{n+1})$, $Y_{n} = (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}}/\mathcal{J}^{n+1})$.

**Proof.** (ii) results at once from (i) and (10.6.9). To demonstrate (i), one may restrict oneself to the case where
$\mathfrak{X} = \operatorname{Spf}(A)$, $\mathfrak{Y} = \operatorname{Spf}(B)$, $A$ and $B$ being Noetherian,
$\mathcal{T} = \mathfrak{T}^{\Delta}$, $\mathcal{J} = \mathfrak{K}^{\Delta}$, where $\mathfrak{T}$ is the largest ideal
of definition of $A$ and $\mathfrak{K}$ an ideal of definition of $B$. Let $f = ({}^{a}\varphi, \widetilde{\varphi})$,
where $\varphi : B \to A$ is a continuous homomorphism; since the elements of $\mathfrak{K}$ are topologically nilpotent
(0, 7.1.4, (ii)), so are those of $\varphi(\mathfrak{K})$, hence $\varphi(\mathfrak{K}) \subset \mathfrak{T}$ since
$\mathfrak{T}$ is the set of topologically nilpotent elements of $A$ (0, 7.1.6); whence the conclusion by virtue of
(10.5.6, (ii)).

**Corollary (10.6.11).** Let $\mathfrak{S}$, $\mathfrak{X}$, $\mathfrak{Y}$ be three locally Noetherian formal
preschemes, $f : \mathfrak{X} \to \mathfrak{S}$, $g : \mathfrak{Y} \to \mathfrak{S}$ morphisms making $\mathfrak{X}$ and
$\mathfrak{Y}$ into $\mathfrak{S}$-formal preschemes. Let $\mathcal{L}$ (resp. $\mathcal{I}$, $\mathcal{J}$) be an Ideal
of definition of $\mathfrak{S}$ (resp. $\mathfrak{X}$, $\mathfrak{Y}$), and suppose that
$f^{*}(\mathcal{L})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{I}$, $g^{*}(\mathcal{L})\mathcal{O}_{\mathfrak{Y}}
\subset \mathcal{J}$; set $S_{n} = (\mathfrak{S}, \mathcal{O}_{\mathfrak{S}}/\mathcal{L}^{n+1})$, $X_{n} =
(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{I}^{n+1})$, $Y_{n} = (\mathfrak{Y},
\mathcal{O}_{\mathfrak{Y}}/\mathcal{J}^{n+1})$. There is then a canonical one-to-one correspondence between
$\operatorname{Hom}_{\mathfrak{S}}(\mathfrak{X}, \mathfrak{Y})$ and the set of sequences $(u_{n})$ of $S_{n}$-morphisms
$u_{n} : X_{n} \to Y_{n}$ making commutative the diagrams (10.6.7.1).

**Proof.** For every $\mathfrak{S}$-morphism $u : \mathfrak{X} \to \mathfrak{Y}$, one has by definition $f = g \circ u$,
hence $$ u^{*}(g^{*}(\mathcal{L}))\mathcal{O}_{\mathfrak{X}} =
u^{*}(g^{*}(\mathcal{L})\mathcal{O}_{\mathfrak{Y}})\mathcal{O}_{\mathfrak{X}} =
f^{*}(\mathcal{L})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{I} $$ the corollary thus follows from (10.6.9).

One will note that, for $m \leq n$, the datum of a morphism $f_{m} : X_{m} \to Y_{m}$ determines one and only one
morphism $f_{n} : X_{n} \to Y_{n}$ making commutative the diagram (10.6.7.1), as one sees at once by reducing to the
affine case; one has thus defined a map $\rho_{nm} : \operatorname{Hom}_{S_{m}}(X_{m}, Y_{m}) \to
\operatorname{Hom}_{S_{n}}(X_{n}, Y_{n})$ and the $\operatorname{Hom}_{S_{n}}(X_{n}, Y_{n})$ form for the $\rho_{nm}$ a
projective system of sets; (10.6.11) may be stated again by saying that there exists a canonical bijection $$
\operatorname{Hom}_{\mathfrak{S}}(\mathfrak{X}, \mathfrak{Y}) \cong \varprojlim_{n} \operatorname{Hom}_{S_{n}}(X_{n},
Y_{n}). $$

## 10.7. Product of formal preschemes

<!-- label: I.10.7 -->

**(10.7.1)** Let $\mathfrak{S}$ be a formal prescheme; the $\mathfrak{S}$-formal preschemes forming a category, one may
define the notion of product of $\mathfrak{S}$-formal preschemes.

**Proposition (10.7.2).** Let $\mathfrak{X} = \operatorname{Spf}(B)$, $\mathfrak{Y} = \operatorname{Spf}(C)$ be two
formal affine schemes over a formal affine scheme $\mathfrak{S} = \operatorname{Spf}(A)$. Let $\mathfrak{Z} =
\operatorname{Spf}(B \widehat{\otimes}_{A} C)$, $p_{1}$, $p_{2}$ the $\mathfrak{S}$-morphisms corresponding (10.2.2) to
the canonical (continuous) $A$-homomorphisms $b$ and $c$ of $B$ and $C$ into $B \widehat{\otimes}_{A} C$; then
$(\mathfrak{Z}, p_{1}, p_{2})$ is a product of the $\mathfrak{S}$-formal affine schemes $\mathfrak{X}$ and
$\mathfrak{Y}$.

**Proof.** By virtue of (10.4.6), everything reduces to verifying that if, to every continuous $A$-homomorphism $\varphi
: B \widehat{\otimes}_{A} C \to D$, where $D$ is an admissible ring which is a topological $A$-algebra, one associates the
pair $(\varphi \circ b, \varphi \circ c)$, one defines a bijection
$$ \operatorname{Hom}_{A}(B \widehat{\otimes}_{A} C, D) \cong \operatorname{Hom}_{A}(B, D) \times \operatorname{Hom}_{A}(C,
D) $$
which is none other than the universal property of the completed tensor product (0, 7.7.6).

**Proposition (10.7.3).** Given two $\mathfrak{S}$-formal preschemes $\mathfrak{X}$, $\mathfrak{Y}$, the product
$\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y}$ exists.

**Proof.** The demonstration is identical to that of (3.2.6), replacing therein the affine schemes (resp. the affine
opens) by the formal affine schemes (resp. the formal affine opens), and the prop. (3.2.2) by (10.7.2).

All the formal properties of the product of preschemes (3.2.7 and 3.2.8, 3.3.1 to 3.3.12) are valid without any
modification for the product of formal preschemes.

**(10.7.4)** Let $\mathfrak{S}$, $\mathfrak{X}$, $\mathfrak{Y}$ be three formal preschemes and let $f : \mathfrak{X} \to
\mathfrak{S}$, $g : \mathfrak{Y} \to \mathfrak{S}$ be two morphisms. Suppose that there exist in $\mathfrak{S}$,
$\mathfrak{X}$, $\mathfrak{Y}$ respectively three fundamental systems of Ideals of definition $(\mathcal{L}_{\lambda})$,
$(\mathcal{I}_{\lambda})$, $(\mathcal{J}_{\lambda})$ respectively, having the same index set $I$, such that
$f^{*}(\mathcal{L}_{\lambda})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{I}_{\lambda}$ and
$g^{*}(\mathcal{L}_{\lambda})\mathcal{O}_{\mathfrak{Y}} \subset \mathcal{J}_{\lambda}$ for every $\lambda$. Set
$S_{\lambda} = (\mathfrak{S}, \mathcal{O}_{\mathfrak{S}}/\mathcal{L}_{\lambda})$, $X_{\lambda} = (\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}_{\lambda})$, $Y_{\lambda} = (\mathfrak{Y},
\mathcal{O}_{\mathfrak{Y}}/\mathcal{J}_{\lambda})$; for $\mathcal{L}_{\mu} \subset \mathcal{L}_{\lambda}$,
$\mathcal{I}_{\mu} \subset \mathcal{I}_{\lambda}$, $\mathcal{J}_{\mu} \subset \mathcal{J}_{\lambda}$, note that
$S_{\mu}$ (resp. $X_{\mu}$, $Y_{\mu}$) is a closed subprescheme of $S_{\lambda}$ (resp. $X_{\lambda}$, $Y_{\lambda}$)
having the same underlying space (10.6.1). Since $S_{\mu} \to S_{\lambda}$ is a monomorphism of preschemes, one sees
first that the products $X_{\mu} \times_{S_{\mu}} Y_{\mu}$ and $X_{\mu} \times_{S_{\lambda}} Y_{\mu}$ are identical
(3.2.4), then that $X_{\mu} \times_{S_{\mu}} Y_{\mu}$ is identified with a closed subprescheme of $X_{\lambda}
\times_{S_{\lambda}} Y_{\lambda}$ having the same underlying space (4.3.1). This being so, the product $\mathfrak{X}
\times_{\mathfrak{S}} \mathfrak{Y}$ is the inductive limit of the ordinary preschemes $X_{\lambda} \times_{S_{\lambda}}
Y_{\lambda}$: indeed, one sees as in (10.6.2) that one may reduce to the case where $\mathfrak{S}$, $\mathfrak{X}$, and
$\mathfrak{Y}$ are formal affine schemes. Taking account of (10.5.6, (ii)) and of the hypothesis on the fundamental
systems of Ideals of definition of $\mathfrak{S}$, $\mathfrak{X}$, and $\mathfrak{Y}$, one sees at once that our
assertion results from the definition of the completed tensor product of two algebras (0, 7.7.1).

Moreover, let $\mathfrak{Z}$ be an $\mathfrak{S}$-formal prescheme, $(\mathcal{K}_{\lambda})$ a fundamental system of
Ideals of definition of $\mathfrak{Z}$ having $I$ as index set, $u : \mathfrak{Z} \to \mathfrak{X}$, $v : \mathfrak{Z}
\to \mathfrak{Y}$ two $\mathfrak{S}$-morphisms such that $u^{*}(\mathcal{I}_{\lambda})\mathcal{O}_{\mathfrak{Z}} \subset
\mathcal{K}_{\lambda}$ and $v^{*}(\mathcal{J}_{\lambda})\mathcal{O}_{\mathfrak{Z}} \subset \mathcal{K}_{\lambda}$. If
one sets $Z_{\lambda} = (\mathfrak{Z}, \mathcal{O}_{\mathfrak{Z}}/\mathcal{K}_{\lambda})$, and if $u_{\lambda} :
Z_{\lambda} \to X_{\lambda}$ and $v_{\lambda} : Z_{\lambda} \to Y_{\lambda}$ are the $S_{\lambda}$-morphisms
corresponding to $u$ and $v$ (10.5.6), one verifies at once that $(u, v)_{\mathfrak{S}}$ is the inductive limit of the
$S_{\lambda}$-morphisms $(u_{\lambda}, v_{\lambda})_{S_{\lambda}}$.

The considerations of this number apply in particular when $\mathfrak{S}$, $\mathfrak{X}$, and $\mathfrak{Y}$ are
locally Noetherian, taking as fundamental systems of Ideals of definition the systems formed of the powers of an Ideal
of definition (10.5.1). But one will note that $\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y}$ is not necessarily
locally Noetherian (see however (10.13.5)).

## 10.8. Formal completion of a prescheme along a closed part

<!-- label: I.10.8 -->

**(10.8.1)** Let $X$ be a locally Noetherian (ordinary) prescheme, $X'$ a closed part of the space underlying $X$;
designate by $\Phi$ the set of coherent sheaves of ideals $\mathcal{I}$ in $\mathcal{O}_{X}$ such that the support of
$\mathcal{O}_{X}/\mathcal{I}$ is $X'$. The set $\Phi$ is not empty (5.2.1, 4.1.4, and 6.1.1); we shall order it by the
relation $\supset$.

**Lemma (10.8.2).** The ordered set $\Phi$ is filtered; if $X$ is Noetherian, then for every $\mathcal{I} \in \Phi$, the
set of powers $\mathcal{I}^{n}$ ($n > 0$) is cofinal with $\Phi$.

**Proof.** Indeed, if $\mathcal{I}_{1}$ and $\mathcal{I}_{2}$ belong to $\Phi$, and if one sets $\mathcal{I} =
\mathcal{I}_{1}\mathcal{I}_{2}$, $\mathcal{I}$ is coherent since $\mathcal{O}_{X}$ is coherent (6.1.1 and 0, 5.3.4), and
one has $\mathcal{I}_{x} = (\mathcal{I}_{1})_{x}(\mathcal{I}_{2})_{x}$ for every $x \in X$, hence $\mathcal{I}_{x} =
\mathcal{O}_{x}$ for $x \notin X'$ and $\mathcal{I}_{x} \neq \mathcal{O}_{x}$ for $x \in X'$, which proves that
$\mathcal{I} \in \Phi$. On the other hand, if $X$ is Noetherian, and if $\mathcal{I}_{1}$ and $\mathcal{I}$ belong to
$\Phi$, there exists an integer $n > 0$ such that $\mathcal{I}^{n} \subset \mathcal{I}_{1}$ (9.3.4), which signifies
that $\mathcal{I}^{n} \subset \mathcal{I}_{1}$.

**(10.8.3)** Let now $\mathcal{F}$ be a coherent $\mathcal{O}_{X}$-Module; for every $\mathcal{I} \in \Phi$,
$\mathcal{F} \otimes_{\mathcal{O}_{X}} (\mathcal{O}_{X}/\mathcal{I})$ is a coherent $\mathcal{O}_{X}$-Module (9.1.1), of
support contained in $X'$, and which we shall most often identify with its restriction to $X'$. When $\mathcal{I}$ runs
through $\Phi$, these sheaves form a projective system of sheaves of abelian groups.

**Definition (10.8.4).** Given a closed part $X'$ of a locally Noetherian prescheme $X$ and a coherent
$\mathcal{O}_{X}$-Module $\mathcal{F}$, one calls _completion of $\mathcal{F}$ along $X'$_ and designates by
$\mathcal{F}_{/X'}$ or by $\widehat{\mathcal{F}}$ (when no confusion is possible) the restriction to $X'$ of the sheaf
$\varprojlim (\mathcal{F} \otimes_{\mathcal{O}_{X}} (\mathcal{O}_{X}/\mathcal{I}))$; one says that its sections over
$X'$ are the _formal sections of $\mathcal{F}$ along $X'$_.

It is immediate that for every open $U \subset X$, one has $(\mathcal{F}|U)_{/(U \cap X')} = (\mathcal{F}_{/X'})|(U \cap
X')$.

By passage to the projective limit, it is clear that $(\mathcal{O}_{X})_{/X'}$ is a sheaf of rings, and that
$\mathcal{F}_{/X'}$ may be considered as an $(\mathcal{O}_{X})_{/X'}$-Module. Moreover, since there exists a base for
the topology of $X'$ formed of quasi-compact opens, one may consider $(\mathcal{O}_{X})_{/X'}$ (resp.
$\mathcal{F}_{/X'}$) as a sheaf of topological rings (resp. of topological groups) projective limit of the sheaves of
pseudo-discrete rings (resp. groups) $\mathcal{O}_{X}/\mathcal{I}$ (resp. $\mathcal{F} \otimes_{\mathcal{O}_{X}}
(\mathcal{O}_{X}/\mathcal{I}) = \mathcal{F}/\mathcal{I}\mathcal{F}$); by passage to the projective limit,
$\mathcal{F}_{/X'}$ then becomes a topological $(\mathcal{O}_{X})_{/X'}$-Module (0, 3.8.1 and 3.8.2); let us recall that
for every quasi-compact open $U \subset X$, $\Gamma(U \cap X', (\mathcal{O}_{X})_{/X'})$ (resp. $\Gamma(U \cap X',
\mathcal{F}_{/X'})$) is then the projective limit of the discrete rings (resp. groups) $\Gamma(U,
\mathcal{O}_{X}/\mathcal{I})$ (resp. $\Gamma(U, \mathcal{F}/\mathcal{I}\mathcal{F})$).

If now $u : \mathcal{F} \to \mathcal{G}$ is a homomorphism of $\mathcal{O}_{X}$-Modules, one deduces from it canonically
homomorphisms $u_{\mathcal{I}} : \mathcal{F} \otimes_{\mathcal{O}_{X}} (\mathcal{O}_{X}/\mathcal{I}) \to \mathcal{G}
\otimes_{\mathcal{O}_{X}} (\mathcal{O}_{X}/\mathcal{I})$ for every $\mathcal{I} \in \Phi$, and these homomorphisms form
a projective system. By passage to the projective limit and restriction to $X'$, they therefore give a continuous
$(\mathcal{O}_{X})_{/X'}$-homomorphism $\mathcal{F}_{/X'} \to \mathcal{G}_{/X'}$, denoted $u|X'$ or $\widehat{u}$ and
called the _completion of the homomorphism $u$ along $X'$_. It is clear that if $v : \mathcal{G} \to \mathcal{H}$ is a
second homomorphism of $\mathcal{O}_{X}$-Modules, one has $(v \circ u)_{/X'} = v_{/X'} \circ u_{/X'}$, hence $u \to
u_{/X'}$ is a covariant additive functor in $\mathcal{F}$, from the category of coherent $\mathcal{O}_{X}$-Modules, with
values in the category of topological $(\mathcal{O}_{X})_{/X'}$-Modules.

**Proposition (10.8.5).** The support of $(\mathcal{O}_{X})_{/X'}$ is $X'$; the topologically ringed space $(X',
(\mathcal{O}_{X})_{/X'})$ is a locally Noetherian formal prescheme, and if $\mathcal{I} \in \Phi$, $\mathcal{I}_{/X'}$
is an Ideal of definition of this formal prescheme. If $X = \operatorname{Spec}(A)$ is an affine scheme with Noetherian
ring, $\mathcal{I} = \widetilde{\mathfrak{J}}$ where $\mathfrak{J}$ is an ideal of $A$, and $X' = V(\mathfrak{J})$, then
$(X', (\mathcal{O}_{X})_{/X'})$ is canonically identified with $\operatorname{Spf}(\widehat{A})$, where $\widehat{A}$ is
the separated completion of $A$ for the $\mathfrak{J}$-preadic topology.

**Proof.** One may evidently restrict oneself to proving the last assertion. One knows (0, 7.3.3) that the separated
completion $\widehat{\mathfrak{J}}$ of $\mathfrak{J}$ for the $\mathfrak{J}$-preadic topology is identified with the
ideal $\mathfrak{J}\widehat{A}$ of $\widehat{A}$, and that $\widehat{A}$ is a $\widehat{\mathfrak{J}}$-adic Noetherian
ring such that $\widehat{A}/\widehat{\mathfrak{J}}^{n} = A/\mathfrak{J}^{n}$ (0, 7.2.6). This last relation shows that
the open prime ideals of $\widehat{A}$ are the ideals $\mathfrak{P} = \mathfrak{p}\widehat{A}$, where $\mathfrak{p}$ is
a prime ideal of $A$ containing $\mathfrak{J}$, and that one has $\mathfrak{P} \cap A = \mathfrak{p}$, whence
$\operatorname{Spf}(\widehat{A}) = X'$. Since $\mathcal{O}_{X}/\mathcal{I}^{n} = \widetilde{(A/\mathfrak{J}^{n})}$, the
proposition follows at once from the definitions.

One says that the formal prescheme thus defined is the _completion of $X$ along $X'$_ and one denotes it by
$\widehat{X}_{/X'}$ or $\widehat{X}$ if no confusion is to be feared. When one takes $X' = X$, one may take $\mathcal{I}
= 0$, and one therefore has $\widehat{X}_{/X} = X$.

It is clear that if $U$ is a subprescheme induced on an open of $X$, $\widehat{U}_{/(U \cap X')}$ is canonically
identified with the formal subprescheme induced by $\widehat{X}_{/X'}$ on the open $U \cap X'$ of $X'$.

**Corollary (10.8.6).** The (ordinary) prescheme $X'_{\mathrm{red}}$ is the unique reduced subprescheme of $X$ having
$X'$ for underlying space (5.2.1). For $\widehat{X}$ to be Noetherian, it is necessary and sufficient that
$X'_{\mathrm{red}}$ be, and it is sufficient that $X$ be.

**Proof.** The determination of $\widehat{X}_{\mathrm{red}}$ being local (10.5.4), one may again suppose that $X$ is an
affine scheme with Noetherian ring; with the notations of (10.8.5), the ideal $\mathfrak{T}$ of topologically nilpotent
elements of $\widehat{A}$ is the inverse image under the canonical map $\widehat{A} \to
\widehat{A}/\widehat{\mathfrak{J}} = A/\mathfrak{J}$ of the nilradical of $A/\mathfrak{J}$ (0, 7.1.3), hence
$\widehat{A}/\mathfrak{T}$ is isomorphic to the quotient of $A/\mathfrak{J}$ by its nilradical. The first assertion
therefore results from (10.5.4) and (5.1.1). If $\widehat{X}$ is Noetherian, its underlying space $X'$ is also, hence
the $X_{n} = \operatorname{Spec}(\mathcal{O}_{X}/\mathcal{I}^{n})$ are Noetherian (6.1.2) and so is $\widehat{X}$
(10.6.4); the converse is immediate, by virtue of (6.1.2).

**(10.8.7)** The canonical homomorphisms $\mathcal{O}_{X} \to \mathcal{O}_{X}/\mathcal{I}$ (for $\mathcal{I} \in \Phi$)
form a projective system and therefore give, by passage to the projective limit, a homomorphism of sheaves of rings
$\theta : \mathcal{O}_{X} \to \psi_{*}((\mathcal{O}_{X})_{/X'})$, denoting by $\psi$ the canonical injection $X' \to X$ of
the underlying spaces. We shall designate by $i$ (or $i_{X}$) the morphism (said to be _canonical_)
$$ (\psi, \theta) : \widehat{X}_{/X'} \to X $$
of ringed spaces.

By tensorization, for every coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, the canonical homomorphisms
$\mathcal{O}_{X} \to \mathcal{O}_{X}/\mathcal{I}$ give homomorphisms $\mathcal{F} \to \mathcal{F}
\otimes_{\mathcal{O}_{X}} (\mathcal{O}_{X}/\mathcal{I})$ of $\mathcal{O}_{X}$-Modules which again form a projective
system, and therefore give, by passage to the projective limit, a canonical functorial homomorphism $\gamma :
\mathcal{F} \to \mathcal{F}_{/X'}$ of $\mathcal{O}_{X}$-Modules.

**Proposition (10.8.8).** (i) The functor $\mathcal{F}_{/X'}$ (in $\mathcal{F}$) is exact.

(ii) The functorial homomorphism $\widehat{\gamma} : i^{*}(\mathcal{F}) \to \mathcal{F}_{/X'}$ of
$(\mathcal{O}_{X})_{/X'}$-Modules is an isomorphism.

**Proof.** (i) It suffices to prove that if $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ is an exact
sequence of coherent $\mathcal{O}_{X}$-Modules, and $U$ an affine open of $X$, with Noetherian ring $A$, the sequence $$
0 \to \Gamma(U \cap X', \mathcal{F}'_{/X'}) \to \Gamma(U \cap X', \mathcal{F}_{/X'}) \to \Gamma(U \cap X',
\mathcal{F}''_{/X'}) \to 0 $$ is exact. One then has $\mathcal{F}|U = \widetilde{M}$, $\mathcal{F}'|U = \widetilde{M'}$,
$\mathcal{F}''|U = \widetilde{M''}$, where $M$, $M'$, $M''$ are three $A$-modules of finite type such that the sequence
$0 \to M' \to M \to M'' \to 0$ is exact (1.5.1 and 1.3.11); let $\mathcal{I} \in \Phi$ and let $\mathfrak{J}$ be an
ideal of $A$ such that $\mathcal{I}|U = \widetilde{\mathfrak{J}}$. One then has $$ \Gamma(U \cap X', \mathcal{F}
\otimes_{\mathcal{O}_{X}} (\mathcal{O}_{X}/\mathcal{I}^{n})) = M \otimes_{A}(A/\mathfrak{J}^{n}) $$ (1.3.12); hence, by
definition of the projective limit, one has $$ \Gamma(U \cap X', \mathcal{F}_{/X'}) = \varprojlim_{n} (M
\otimes_{A}(A/\mathfrak{J}^{n})) = \widehat{M} $$ the separated completion of $M$ for the $\mathfrak{J}$-preadic
topology, and likewise $$ \Gamma(U \cap X', \mathcal{F}'_{/X'}) = \widehat{M'}, \quad \Gamma(U \cap X',
\mathcal{F}''_{/X'}) = \widehat{M''} $$ our assertion then results from the fact that when $A$ is Noetherian, the
functor $\widehat{M}$ in $M$ is exact on the category of $A$-modules of finite type (0, 7.3.3).

(ii) The question being local, one may suppose that one has an exact sequence $\mathcal{O}_{X}^{q} \to \mathcal{O}_{X}^{p}
\to \mathcal{F} \to 0$ (0, 5.3.2); since $\widehat{\gamma}$ is functorial, and the functors $i^{*}(\mathcal{F})$ and
$\mathcal{F}_{/X'}$ are right exact (by (i) and (0, 4.3.1)), one has the commutative diagram
$$ \begin{array}{ccc} i^{*}(\mathcal{O}_{X}^{q}) \to i^{*}(\mathcal{O}_{X}^{p}) \to i^{*}(\mathcal{F}) \to 0 \\ \quad
\downarrow \widehat{\gamma} \qquad \downarrow \widehat{\gamma} \qquad \downarrow \widehat{\gamma} \\ (\mathcal{O}_{X}^{q})_{/X'}
\to (\mathcal{O}_{X}^{p})_{/X'} \to \mathcal{F}_{/X'} \to 0 \end{array} \tag{10.8.8.1} $$
whose lines are exact. Moreover, the two functors $i^{*}(\mathcal{F})$ and $\mathcal{F}_{/X'}$ commute with finite direct
sums (0, 3.2.6 and 4.3.2) and one is therefore reduced to demonstrating our assertion for $\mathcal{F} = \mathcal{O}_{X}$.
One then has $i^{*}(\mathcal{O}_{X}) = (\mathcal{O}_{X})_{/X'} = (\mathcal{O}_{X})_{/X'}$ (0, 4.3.4), and
$\widehat{\gamma}$ is a homomorphism of $(\mathcal{O}_{X})_{/X'}$-Modules; it therefore suffices to verify that
$\widehat{\gamma}$ transforms the unit section of $\mathcal{O}_{X}$ over an open of $X'$ into itself, which is immediate
and therefore shows that in this case $\widehat{\gamma}$ is the identity.

**Corollary (10.8.9).** The morphism of ringed spaces $i : \widehat{X}_{/X'} \to X$ is flat.

**Proof.** This indeed results from (0, 6.7.3) and from (10.8.8, (i)).

**Corollary (10.8.10).** If $\mathcal{F}$ and $\mathcal{G}$ are coherent $\mathcal{O}_{X}$-Modules, there exist
canonical functorial isomorphisms (in $\mathcal{F}$ and $\mathcal{G}$)

$$ (\mathcal{F}_{/X'}) \otimes_{(\mathcal{O}_{X})_{/X'}} (\mathcal{G}_{/X'}) \cong (\mathcal{F}
\otimes_{\mathcal{O}_{X}} \mathcal{G})_{/X'} \tag{10.8.10.1} $$

$$ (\mathcal{H}om_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G}))_{/X'} \cong
\mathcal{H}om_{(\mathcal{O}_{X})_{/X'}}(\mathcal{F}_{/X'}, \mathcal{G}_{/X'}) \tag{10.8.10.2} $$

**Proof.** This results from the canonical identification of $i^{*}(\mathcal{F})$ and of $\mathcal{F}_{/X'}$; the
existence of the first isomorphism is then a result valid for all morphisms of ringed spaces (0, 4.3.3.1) and that of
the second a result valid for all flat morphisms (0, 6.7.6), hence follows from (10.8.9).

**Proposition (10.8.11).** For every coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, the kernel of the canonical
homomorphism $\Gamma(X, \mathcal{F}) \to \Gamma(X', \mathcal{F}_{/X'})$ deduced from $\mathcal{F} \to \mathcal{F}_{/X'}$
is formed of the sections null in a neighborhood of $X'$.

**Proof.** It results from the definition of $\mathcal{F}_{/X'}$ that the canonical image of such a section is null.
Conversely, if $s \in \Gamma(X, \mathcal{F})$ has a null image in $\Gamma(X', \mathcal{F}_{/X'})$, it suffices to see
that every $x \in X'$ admits a neighborhood in $X$ in which $s$ is null, and one may therefore reduce to the case where
$X = \operatorname{Spec}(A)$ is affine, $A$ Noetherian, $X' = V(\mathfrak{J})$, where $\mathfrak{J}$ is an ideal of $A$,
and $\mathcal{F} = \widetilde{M}$, where $M$ is an $A$-module of finite type. Then $\Gamma(X', \mathcal{F}_{/X'})$ is
the separated completion $\widehat{M}$ of $M$ for the $\mathfrak{J}$-preadic topology, and the homomorphism $\Gamma(X,
\mathcal{F}) \to \Gamma(X', \mathcal{F}_{/X'})$ is the canonical homomorphism $M \to \widehat{M}$. One knows (0, 7.3.7)
that the kernel of this homomorphism is the set of $s \in M$ annihilated by an element of $1 + \mathfrak{J}$. One
therefore has $(1 + f)s = 0$ for an $f \in \mathfrak{J}$; for every $x \in X'$ one deduces $(1 + f_{x})s_{x} = 0$, and
since $1 + f_{x}$ is invertible in $\mathcal{O}_{x}$ ($f_{x} \in \mathfrak{j}_{x}$ being contained in the maximal ideal
of $\mathcal{O}_{x}$), one has $s_{x} = 0$, which demonstrates the proposition.

**Corollary (10.8.12).** The support of $\mathcal{F}_{/X'}$ is equal to $\operatorname{Supp}(\mathcal{F}) \cap X'$.

**Proof.** It is clear that $\mathcal{F}_{/X'}$ is an $(\mathcal{O}_{X})_{/X'}$-Module of finite type (10.8.8, (ii)) and
(0, 5.2.4), hence its support is closed (0, 5.2.2) and evidently contained in $\operatorname{Supp}(\mathcal{F}) \cap
X'$. To show that it is equal to this last set, one is at once reduced to proving that the relation $\Gamma(X',
\mathcal{F}_{/X'}) = 0$ entails $\operatorname{Supp}(\mathcal{F}) \cap X' = \emptyset$; now this results from (10.8.11)
and from (1.4.1).

**Corollary (10.8.13).** Let $u : \mathcal{F} \to \mathcal{G}$ be a homomorphism of coherent $\mathcal{O}_{X}$-Modules.
For $u_{/X'} : \mathcal{F}_{/X'} \to \mathcal{G}_{/X'}$ to be null, it is necessary and sufficient that $u$ be null in a
neighborhood of $X'$.

**Proof.** Indeed, by (10.8.8, (ii)), $u_{/X'}$ is identified with $i^{*}(u)$, hence if one considers $u$ as a section
over $X$ of the sheaf $\mathcal{H} = \mathcal{H}om_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})$, $u_{/X'}$ is the
section of $i^{*}(\mathcal{H}) = \mathcal{H}_{/X'}$ over $X'$ which corresponds to it canonically ((10.8.10.2) and (0,
4.4.6)). It therefore suffices to apply (10.8.11) to the coherent $\mathcal{O}_{X}$-Module $\mathcal{H}$.

**Corollary (10.8.14).** Let $u : \mathcal{F} \to \mathcal{G}$ be a homomorphism of coherent $\mathcal{O}_{X}$-Modules.
For $u_{/X'}$ to be a monomorphism (resp. an epimorphism), it is necessary and sufficient that $u$ be a monomorphism
(resp. an epimorphism) in a neighborhood of $X'$.

**Proof.** Let $\mathcal{Q}$ and $\mathcal{R}$ be the cokernel and the kernel of $u$, so that one has the exact sequence
$0 \to \mathcal{R} \to \mathcal{F} \to \mathcal{G} \to \mathcal{Q} \to 0$, whence (10.8.8, (i)) the exact sequence $$ 0
\to \mathcal{R}_{/X'} \xrightarrow{v_{/X'}} \mathcal{F}_{/X'} \xrightarrow{u_{/X'}} \mathcal{G}_{/X'}
\xrightarrow{w_{/X'}} \mathcal{Q}_{/X'} \to 0. $$ If $u_{/X'}$ is a monomorphism (resp. an epimorphism), one has
$v_{/X'} = 0$ (resp. $w_{/X'} = 0$), hence there is a neighborhood of $X'$ in which $v = 0$ (resp. $w = 0$) by virtue of
(10.8.13).

## 10.9. Extension of a morphism to the completions

<!-- label: I.10.9 -->

**(10.9.1)** Let $X$, $Y$ be two locally Noetherian (ordinary) preschemes, $f : X \to Y$ a morphism, $X'$ (resp. $Y'$) a
closed part of the underlying space $X$ (resp. $Y$), such that $f(X') \subset Y'$. Let $\mathcal{I}$ (resp.
$\mathcal{J}$) be a sheaf of ideals of $\mathcal{O}_{X}$ (resp. $\mathcal{O}_{Y}$) such that the support of
$\mathcal{O}_{X}/\mathcal{I}$ (resp. $\mathcal{O}_{Y}/\mathcal{J}$) is $X'$ (resp. $Y'$) and that
$f^{*}(\mathcal{J})\mathcal{O}_{X} \subset \mathcal{I}$; one will note that there always exist such sheaves of ideals,
for one may for example take for $\mathcal{I}$ the largest sheaf of ideals of $\mathcal{O}_{X}$ defining a subprescheme
of $X$ having $X'$ for underlying space (5.2.1), and the hypothesis $f(X') \subset Y'$ then entails
$f^{*}(\mathcal{J})\mathcal{O}_{X} \subset \mathcal{I}$ (5.2.4). One therefore has, for every integer $n > 0$,
$f^{*}(\mathcal{J}^{n})\mathcal{O}_{X} \subset \mathcal{I}^{n}$ (0, 4.3.5); consequently (4.4.6), if one sets $X_{n} =
(X', \mathcal{O}_{X}/\mathcal{I}^{n+1})$, $Y_{n} = (Y', \mathcal{O}_{Y}/\mathcal{J}^{n+1})$, one deduces from $f$ a
morphism $f_{n} : X_{n} \to Y_{n}$, and it is immediate that the $f_{n}$ form an inductive system. We shall designate
its inductive limit (10.6.8) by $\widehat{f} : \widehat{X}_{/X'} \to \widehat{Y}_{/Y'}$, and we shall say (by abuse of
language) that $\widehat{f}$ is the _extension of $f$ to the completions of $X$ and $Y$ along $X'$ and $Y'$_. It is
immediate to verify that this morphism does not depend on the choice of the sheaves of ideals $\mathcal{I}$,
$\mathcal{J}$ verifying the conditions above. It suffices indeed to see it when $X$ and $Y$ are affine Noetherian
schemes with rings $A$, $B$; then $\mathcal{I} = \widetilde{\mathfrak{J}}$, $\mathcal{J} = \widetilde{\mathfrak{K}}$,
where $\mathfrak{J}$ (resp. $\mathfrak{K}$) is an ideal of $A$ (resp. $B$), $f$ corresponds to a ring homomorphism
$\varphi : B \to A$ such that $\varphi(\mathfrak{K}) \subset \mathfrak{J}$ (4.4.6 and 1.7.4); $\widehat{f}$ is then the
morphism which corresponds (10.2.2) to the continuous homomorphism $\widehat{\varphi} : \widehat{B} \to \widehat{A}$,
where $\widehat{A}$ (resp. $\widehat{B}$) is the separated completion of $A$ (resp. $B$) for the $\mathfrak{J}$-preadic
(resp. $\mathfrak{K}$-preadic) topology (10.6.8); and one knows that if one replaces $\mathcal{I}$ by another sheaf of
ideals $\mathcal{I}' = \widetilde{\mathfrak{J}'}$ such that the support of $\mathcal{O}_{X}/\mathcal{I}'$ is again $X'$,
the $\mathfrak{J}$-preadic and $\mathfrak{J}'$-preadic topologies on $\widehat{A}$ are the same (10.8.2).

One will note that, by this definition, the continuous map $X' \to Y'$ of the spaces underlying $\widehat{X}_{/X'}$ and
$\widehat{Y}_{/Y'}$ which corresponds to $\widehat{f}$ is none other than the restriction to $X'$ of $f$.

**(10.9.2)** It results at once from the preceding definition that the diagram of morphisms of ringed spaces
$$ \begin{array}{ccc} \widehat{X}_{/X'} & \xrightarrow{\widehat{f}} & \widehat{Y}_{/Y'} \\ \downarrow i_{X} & &
\downarrow i_{Y} \\ X & \xrightarrow{f} & Y \end{array} $$
is commutative, the vertical arrows being the canonical morphisms (10.8.7).

**(10.9.3)** Let $Z$ be a third prescheme, $g : Y \to Z$ a morphism, $Z'$ a closed part of $Z$ such that $g(Y') \subset
Z'$. If $\widehat{g}$ designates the completion along $Y'$ and $Z'$ of the morphism $g$, it results at once from
(10.9.1) that one has $\widehat{(g \circ f)} = \widehat{g} \circ \widehat{f}$.

**Proposition (10.9.4).** Let $X$, $Y$ be two locally Noetherian $S$-preschemes, $Y$ being of finite type over $S$. Let
$f$, $g$ be two $S$-morphisms of $X$ into $Y$ such that $f(X') \subset Y'$, $g(X') \subset Y'$. For $\widehat{f} =
\widehat{g}$, it is necessary and sufficient that $f$ and $g$ coincide in a neighborhood of $X'$.

**Proof.** The condition is evidently sufficient (without hypothesis of finiteness on $Y$). To see that it is necessary,
let us remark first that the hypothesis $\widehat{f} = \widehat{g}$ implies $f(x) = g(x)$ for every $x \in X'$. On the
other hand, the question being local, one may suppose that $X$ and $Y$ are respective affine open neighborhoods of $x$
and of $y = f(x) = g(x)$, with Noetherian rings, that $S$ is affine, and that $\Gamma(Y, \mathcal{O}_{Y})$ is a
$\Gamma(S, \mathcal{O}_{S})$-algebra of finite type (6.3.3). Then $f$ and $g$ correspond to two $\Gamma(S,
\mathcal{O}_{S})$-homomorphisms $\rho$, $\sigma$ of $\Gamma(Y, \mathcal{O}_{Y})$ into $\Gamma(X, \mathcal{O}_{X})$
(1.7.3), and by hypothesis, the extensions by continuity of these homomorphisms to the separated completion of
$\Gamma(Y, \mathcal{O}_{Y})$ are the same. One concludes from (10.8.11) that for every section $s \in \Gamma(Y,
\mathcal{O}_{Y})$, the sections $\rho(s)$ and $\sigma(s)$ coincide in a neighborhood of $X'$ (depending on $s$); since
$\Gamma(Y, \mathcal{O}_{Y})$ is an algebra of finite type over $\Gamma(S, \mathcal{O}_{S})$, one deduces at once that
there exists a neighborhood $V$ of $X'$ such that $\rho(s)$ and $\sigma(s)$ coincide in $V$ for every section $s \in
\Gamma(Y, \mathcal{O}_{Y})$. If $h \in \Gamma(Y, \mathcal{O}_{Y})$ is such that $D(h)$ is a neighborhood of $x$
contained in $V$, one concludes from what precedes and from (1.4.1, d)) that $f$ and $g$ coincide in $D(h)$.

**Proposition (10.9.5).** Under the hypotheses of (10.9.1), for every coherent $\mathcal{O}_{Y}$-Module $\mathcal{G}$,
there exists a canonical functorial isomorphism of $(\mathcal{O}_{X})_{/X'}$-Modules $$ (f^{*}(\mathcal{G}))_{/X'} \cong
\widehat{f}^{*}(\mathcal{G}_{/Y'}). $$

**Proof.** If one identifies canonically $(f^{*}(\mathcal{G}))_{/X'}$ with $i_{X}^{*}(f^{*}(\mathcal{G}))$ and
$\widehat{f}^{*}(\mathcal{G}_{/Y'})$ with $\widehat{f}^{*}(i_{Y}^{*}(\mathcal{G}))$ (10.8.8), the proposition results at
once from the commutativity of the diagram of (10.9.2).

**(10.9.6)** Let now $\mathcal{F}$ be a coherent $\mathcal{O}_{X}$-Module, $\mathcal{G}$ a coherent
$\mathcal{O}_{Y}$-Module. If $u : \mathcal{G} \to \mathcal{F}$ is an $f$-morphism of $\mathcal{G}$ into $\mathcal{F}$,
there corresponds to it an $\mathcal{O}_{X}$-homomorphism $u^{\flat} : f^{*}(\mathcal{G}) \to \mathcal{F}$, hence by
completion a continuous $(\mathcal{O}_{X})_{/X'}$-homomorphism $(u^{\flat})_{/X'} : (f^{*}(\mathcal{G}))_{/X'} \to
\mathcal{F}_{/X'}$; and by virtue of (10.9.5) there exists one and only one $\widehat{f}$-morphism $v :
\mathcal{G}_{/Y'} \to \mathcal{F}_{/X'}$ such that $v^{\flat} = (u^{\flat})_{/X'}$. If one considers the triples
$(\mathcal{F}, X, X')$ ($\mathcal{F}$ being a coherent $\mathcal{O}_{X}$-Module and $X'$ a closed part of $X$) as a
category, the morphisms $(\mathcal{F}, X, X') \to (\mathcal{G}, Y, Y')$ consisting of a morphism of preschemes $f : X
\to Y$ such that $f(X') \subset Y'$ and of an $f$-morphism $u : \mathcal{G} \to \mathcal{F}$, one may therefore say that
$(\widehat{X}_{/X'}, \mathcal{F}_{/X'})$ is a functor in $(\mathcal{F}, X, X')$, taking its values in the category of
pairs $(\mathfrak{Z}, \mathcal{H})$ formed of a locally Noetherian formal prescheme $\mathfrak{Z}$ and of an
$\mathcal{O}_{\mathfrak{Z}}$-Module $\mathcal{H}$, the morphisms of this last category consisting of the pairs formed of
a morphism $g$ of formal preschemes and of a $g$-morphism.

**Proposition (10.9.7).** Let $S$, $X$, $Y$ be three locally Noetherian preschemes, $g : X \to S$, $h : Y \to S$ two
morphisms, $S'$ a closed part of $S$, $X'$ (resp. $Y'$) a closed part of $X$ (resp. $Y$) such that $g(X') \subset S'$
(resp. $h(Y') \subset S'$); let $Z = X \times_{S} Y$; suppose $Z$ locally Noetherian, and let $Z' = p^{-1}(X') \cap
q^{-1}(Y')$, where $p$ and $q$ are the projections of $X \times_{S} Y$. Under these conditions, the completion
$\widehat{Z}_{/Z'}$ is identified with the product of the $\widehat{S}_{/S'}$-formal preschemes $(\widehat{X}_{/X'})
\times_{\widehat{S}_{/S'}} (\widehat{Y}_{/Y'})$, the structure morphisms being identified with $\widehat{g}$ and
$\widehat{h}$, and the projections with $\widehat{p}$ and $\widehat{q}$.

**Proof.** It is immediate that the question is local for $S$, $X$, and $Y$, and one is therefore reduced to the case
where $S = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$, $Y = \operatorname{Spec}(C)$, $S' = V(\mathfrak{J})$,
$X' = V(\mathfrak{K})$, $Y' = V(\mathfrak{L})$, where $\mathfrak{J}$, $\mathfrak{K}$, $\mathfrak{L}$ are three ideals
such that $\varphi(\mathfrak{J}) \subset \mathfrak{K}$ and $\psi(\mathfrak{J}) \subset \mathfrak{L}$, denoting by
$\varphi$ and $\psi$ the homomorphisms $A \to B$ and $A \to C$ which correspond to $g$ and $h$. Then one knows that $Z =
\operatorname{Spec}(B \otimes_{A} C)$ and that $Z' = V(\mathfrak{M})$, where $\mathfrak{M}$ is the ideal
$\operatorname{Im}(\mathfrak{K} \otimes_{A} C) + \operatorname{Im}(B \otimes_{A} \mathfrak{L})$. The conclusion results
(10.7.2) from the fact that the completed tensor product $\widehat{B} \widehat{\otimes}_{\widehat{A}} \widehat{C}$
(where $\widehat{A}$, $\widehat{B}$, $\widehat{C}$ are respectively the separated completions of $A$, $B$, $C$ for the
$\mathfrak{J}$-, $\mathfrak{K}$-, and $\mathfrak{L}$-preadic topologies) is the separated completion of the tensor
product $B \otimes_{A} C$ for the $\mathfrak{M}$-preadic topology (0, 7.7.2).

One will note moreover that if $T$ is a locally Noetherian $S$-prescheme, $u : T \to X$, $v : T \to Y$ two
$S$-morphisms, $T'$ a closed part of $T$ such that $u(T') \subset X'$, $v(T') \subset Y'$, then the extension to the
completions $\widehat{((u, v)_{S})}$ is identified with $(\widehat{u}, \widehat{v})_{\widehat{S}}$.

**Corollary (10.9.8).** Let $X$, $Y$ be two locally Noetherian $S$-preschemes such that $X \times_{S} Y$ is locally
Noetherian; let $S'$ be a closed part of $S$, $X'$ (resp. $Y'$) a closed part of $X$ (resp. $Y$) whose image in $S$ is
contained in $S'$. For every $S$-morphism $f : X \to Y$ such that $f(X') \subset Y'$, the graph morphism
$\Gamma_{\widehat{f}}$ is identified with the extension $\widehat{\Gamma_{f}}$ of the graph morphism of $f$.

**Corollary (10.9.9).** Let $X$, $Y$ be two locally Noetherian preschemes, $f : X \to Y$ a morphism, $Y'$ a closed part
of $Y$, $X' = f^{-1}(Y')$. Then the formal prescheme $\widehat{X}_{/X'}$ is identified, by the commutative diagram $$
\begin{array}{ccc} X & \xleftarrow{i_{X}} & \widehat{X}_{/X'} \\ \downarrow f & & \downarrow \widehat{f} \\ Y &
\xleftarrow{i_{Y}} & \widehat{Y}_{/Y'} \end{array} $$ with the product $X \times_{Y} (\widehat{Y}_{/Y'})$ of formal
preschemes.

**Proof.** It suffices to apply (10.9.7) replacing $S$ and $S'$ by $Y$, $X$ and $X'$ by $X$.

**Remark (10.9.10).** If $X$ is the sum $X_{1} \amalg X_{2}$ (3.1), $X'$ the union $X'_{1} \cup X'_{2}$, where $X'_{i}$
is a closed part of $X_{i}$ ($i = 1, 2$), one sees at once that one has $\widehat{X}_{/X'} = \widehat{X_{1}}_{/X'_{1}}
\amalg \widehat{X_{2}}_{/X'_{2}}$.

## 10.10. Application to coherent sheaves on formal affine schemes

<!-- label: I.10.10 -->

**(10.10.1)** Throughout this paragraph, $A$ will designate an adic Noetherian ring, $\mathfrak{J}$ an ideal of
definition of $A$. Let $X = \operatorname{Spec}(A)$, $\mathfrak{X} = \operatorname{Spf}(A)$, which is identified with
the closed part $V(\mathfrak{J})$ of $X$ (10.1.2). Moreover, the definition (10.1.2) and the definition (10.8.4) show
that the formal affine scheme $\mathfrak{X}$ is identical to the completion $\widehat{X}_{/\mathfrak{X}}$ of the affine
scheme $X$ along the closed part $\mathfrak{X}$ of its underlying space. To every coherent $\mathcal{O}_{X}$-Module
$\mathcal{F}$ there corresponds therefore an $\mathcal{O}_{\mathfrak{X}}$-Module of finite type
$\mathcal{F}_{/\mathfrak{X}}$ which is moreover a sheaf of topological modules on the sheaf of topological rings
$\mathcal{O}_{\mathfrak{X}}$. But every coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ is of the form $\widetilde{M}$,
where $M$ is an $A$-module of finite type (1.5.1); we shall set $(\widetilde{M})_{/\mathfrak{X}} = M^{\Delta}$.
Moreover, if $u : M \to N$ is an $A$-homomorphism of $A$-modules of finite type, there corresponds to it a homomorphism
$\widetilde{u} : \widetilde{M} \to \widetilde{N}$, and consequently also a continuous homomorphism
$(\widetilde{u})_{/\mathfrak{X}} : (\widetilde{M})_{/\mathfrak{X}} \to (\widetilde{N})_{/\mathfrak{X}}$, which we shall
denote $u^{\Delta}$. It is immediate that $(v \circ u)^{\Delta} = v^{\Delta} \circ u^{\Delta}$; one has thus defined a
covariant additive functor $M^{\Delta}$ from the category of $A$-modules of finite type into that of
$\mathcal{O}_{\mathfrak{X}}$-Modules of finite type. When $A$ is a discrete ring, one has $M^{\Delta} = \widetilde{M}$.

**Proposition (10.10.2).** (i) $M^{\Delta}$ is an exact functor in $M$, and there exists a canonical functorial
isomorphism of $A$-modules $\Gamma(\mathfrak{X}, M^{\Delta}) \cong M$.

(ii) If $M$ and $N$ are two $A$-modules of finite type, there exist canonical functorial isomorphisms

$$ (M \otimes_{A} N)^{\Delta} \cong M^{\Delta} \otimes_{\mathcal{O}_{\mathfrak{X}}} N^{\Delta} \tag{10.10.2.1} $$

$$ (\operatorname{Hom}_{A}(M, N))^{\Delta} \cong \mathcal{H}om_{\mathcal{O}_{\mathfrak{X}}}(M^{\Delta}, N^{\Delta})
\tag{10.10.2.2} $$

(iii) The map $u \to u^{\Delta}$ is a functorial isomorphism

$$ \operatorname{Hom}_{A}(M, N) \cong \operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(M^{\Delta}, N^{\Delta})
\tag{10.10.2.3} $$

**Proof.** The exactness of $M^{\Delta}$ results from the exactness of the functors $\widetilde{M}$ (1.3.5) and
$\mathcal{F}_{/X'}$ (10.8.8). By definition, $\Gamma(\mathfrak{X}, M^{\Delta})$ is the separated completion of the
$A$-module $\Gamma(X, \widetilde{M}) = M$ for the $\mathfrak{J}$-preadic topology; but since $A$ is complete and $M$ of
finite type, one knows (0, 7.3.6) that $M$ is separated and complete, which finishes proving (i). The isomorphism
(10.10.2.1) (resp. (10.10.2.2)) comes from the composition of the isomorphisms (1.3.12, (i)) and (10.8.10.1) (resp.
(1.3.12, (ii)) and (10.8.10.2)). Finally, since $\operatorname{Hom}_{A}(M, N)$ is an $A$-module of finite type, one may
apply (i) to it, which identifies $\Gamma(\mathfrak{X}, (\operatorname{Hom}_{A}(M, N))^{\Delta})$ with
$\operatorname{Hom}_{A}(M, N)$, and use (10.10.2.2), which proves that the homomorphism (10.10.2.3) is an isomorphism.

One deduces from (10.10.2) a whole series of consequences analogous to those deduced from (1.3.7) and (1.3.12), which we
leave to the reader the care of formulating.

Let us note that the property of exactness of $M^{\Delta}$, applied to the exact sequence $0 \to \mathfrak{J} \to A \to
A/\mathfrak{J} \to 0$, shows that the sheaf of ideals of $\mathcal{O}_{\mathfrak{X}}$ designated here by
$\mathfrak{J}^{\Delta}$ coincides with the one which had been denoted in the same way in (10.3.1), by virtue of
(10.3.2).

**Proposition (10.10.3).** Under the hypotheses of (10.10.1), $\mathcal{O}_{\mathfrak{X}}$ is a coherent sheaf of rings.

**Proof.** If $f \in A$, one knows that $A_{\{f\}}$ is an adic Noetherian ring (0, 7.6.11) and since the question is
local, one is reduced (10.1.4) to proving that the kernel of a homomorphism $v : \mathcal{O}_{\mathfrak{X}}^{p} \to
\mathcal{O}_{\mathfrak{X}}$ is an $\mathcal{O}_{\mathfrak{X}}$-Module of finite type. One then has $v = u^{\Delta}$,
where $u$ is an $A$-homomorphism $A^{p} \to A$ (10.10.2); since $A$ is Noetherian, the kernel of $u$ is of finite type,
in other words one has a homomorphism $A^{q} \to A^{p}$ such that the sequence $A^{q} \to A^{p} \to A$ is exact. One
concludes (10.10.2) that the sequence $\mathcal{O}_{\mathfrak{X}}^{q} \to \mathcal{O}_{\mathfrak{X}}^{p} \to
\mathcal{O}_{\mathfrak{X}}$ is exact, which proves that the kernel of $v$ is of finite type.

**(10.10.4)** With the preceding notations, set $A_{n} = A/\mathfrak{J}^{n+1}$, and let $X_{n}$ be the affine scheme
$\operatorname{Spec}(A_{n}) = (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{I}^{n+1})$, $\mathcal{I} =
\mathfrak{J}^{\Delta}$ being the sheaf of ideals of definition of $\mathcal{O}_{\mathfrak{X}}$ corresponding to the
ideal $\mathfrak{J}$. Let $u_{nm}$ be the morphism of preschemes $X_{m} \to X_{n}$ corresponding to the canonical
homomorphism $A_{n} \to A_{m}$ for $m \geq n$; the formal scheme $\mathfrak{X}$ is the inductive limit of the $X_{n}$
for the $u_{nm}$ (10.6.3).

**Proposition (10.10.5).** Under the hypotheses of (10.10.1), let $\mathcal{F}$ be an
$\mathcal{O}_{\mathfrak{X}}$-Module. The following conditions are equivalent:

a) $\mathcal{F}$ is a coherent $\mathcal{O}_{\mathfrak{X}}$-Module.

b) $\mathcal{F}$ is isomorphic to the projective limit (10.6.6) of a sequence $(\mathcal{F}_{n})$ of coherent
$\mathcal{O}_{X_{n}}$-Modules such that $u_{nm}^{*}(\mathcal{F}_{n}) = \mathcal{F}_{m}$.

c) There exists an $A$-module of finite type $M$ (determined up to canonical isomorphism by (10.10.2, (i))) such that
$\mathcal{F}$ is isomorphic to $M^{\Delta}$.

**Proof.** Let us first show that b) implies c). One has $\mathcal{F}_{n} = \widetilde{M_{n}}$, where $M_{n}$ is an
$A_{n}$-module of finite type, and the hypothesis entails that $M_{m} = M_{n} \otimes_{A_{n}} A_{m}$ for $m \geq n$
(1.6.5); the $M_{n}$ therefore form a projective system for the canonical $A_{n}$-homomorphisms $M_{m} \to M_{n}$ ($m
\geq n$), and it results at once from the definition of the $A_{n}$ that this projective system verifies the conditions
of (0, 7.2.9); its projective limit $M$ is consequently an $A$-module of finite type such that $M_{n} = M \otimes_{A}
A_{n}$ for every $n$. One deduces that $\mathcal{F}_{n}$ is induced on $X_{n}$ by $\widetilde{M}
\otimes_{\mathcal{O}_{X}} (\mathcal{O}_{X}/\mathcal{I}^{n+1})$, hence $\mathcal{F} = M^{\Delta}$ by definition (10.8.4).

Conversely, c) entails b); indeed, if $u_{n}$ is the immersion morphism $X_{n} \to X$, $u_{n}^{*}(\widetilde{M}) = (M
\otimes_{A} A_{n})^{\sim}$ is induced on $X_{n}$ by $\widetilde{M} \otimes_{\mathcal{O}_{X}}
(\mathcal{O}_{X}/\mathcal{I}^{n+1})$, and $M^{\Delta} = \varprojlim u_{n}^{*}(\widetilde{M})$ by definition (10.8.4);
since $u_{nm} = u_{n} \circ u_{m}$ for $m \geq n$, the $\mathcal{F}_{n} = u_{n}^{*}(\widetilde{M})$ verify the
conditions of b), whence our assertion.

Let us now show that c) implies a): indeed, one has by definition $\mathcal{F} = M^{\Delta}$; $M$ being the cokernel of
a homomorphism $A^{q} \to A^{p}$, it results from (10.10.2) that $M^{\Delta}$ is the cokernel of a homomorphism
$\mathcal{O}_{\mathfrak{X}}^{q} \to \mathcal{O}_{\mathfrak{X}}^{p}$, and since the sheaf of rings
$\mathcal{O}_{\mathfrak{X}}$ is coherent (10.10.3), so is $M^{\Delta}$ (0, 5.3.4).

Finally, a) entails b). Considered as an $\mathcal{O}_{\mathfrak{X}}$-Module, one has $\mathcal{O}_{X_{n}} =
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}^{n+1} = (A_{n})^{\Delta}$; $\mathcal{F}_{n} = \mathcal{F}
\otimes_{\mathcal{O}_{\mathfrak{X}}} \mathcal{O}_{X_{n}}$ is a coherent $\mathcal{O}_{X_{n}}$-Module (0, 5.3.5), and
since it is also an $\mathcal{O}_{\mathfrak{X}}$-Module and $\mathcal{I}^{n+1}$ is coherent, one concludes that
$\mathcal{F}_{n}$ is a coherent $\mathcal{O}_{\mathfrak{X}}$-Module (0, 5.3.10), and it is immediate that
$u_{nm}^{*}(\mathcal{F}_{n}) = \mathcal{F}_{m}$ for $m \geq n$ (recalling that the continuous map $X_{m} \to X_{n}$ of
the underlying spaces is the identity of $\mathfrak{X}$). The sheaf $\mathcal{F}' = \varprojlim \mathcal{F}_{n}$ is
therefore a coherent $\mathcal{O}_{\mathfrak{X}}$-Module, since one has seen that b) entails a). The canonical
homomorphisms $\mathcal{F} \to \mathcal{F}_{n}$ form a projective system, which by passage to the limit gives a
canonical homomorphism $w : \mathcal{F} \to \mathcal{F}'$, and everything reduces to demonstrating that $w$ is
bijective. The question now being local, one may restrict oneself to the case where $\mathcal{F}$ is the cokernel of a
homomorphism $\mathcal{O}_{\mathfrak{X}}^{q} \to \mathcal{O}_{\mathfrak{X}}^{p}$; this homomorphism being of the form
$v^{\Delta}$, where $v$ is a homomorphism $A^{q} \to A^{p}$ (10.10.2), $\mathcal{F}$ is isomorphic to $M^{\Delta}$,
where $M = \operatorname{Coker} v$ (10.10.2). One then has, by virtue of (10.10.2), $\mathcal{F}_{n} = M^{\Delta}
\otimes_{A} A_{n} = (M \otimes_{A} A_{n})^{\Delta}$, and since the $\mathfrak{J}$-adic topology on $M \otimes_{A} A_{n}$
is discrete, one has $(M \otimes_{A} A_{n})^{\Delta} = (M \otimes_{A} A_{n})^{\sim}$ (as $\mathcal{O}_{X_{n}}$-Module);
one has seen above that $M^{\Delta} = \varprojlim \mathcal{F}_{n}$ and $w$ is therefore indeed in this case the
identity. Q.E.D.

**Corollary (10.10.6).** If $\mathcal{F}$ verifies condition b) of (10.10.5), the projective system $(\mathcal{F}_{n})$
is isomorphic to the system of the $\mathcal{F} \otimes_{\mathcal{O}_{\mathfrak{X}}} \mathcal{O}_{X_{n}}$.

**(10.10.7)** Let now $A$, $B$ be two adic Noetherian rings, $\varphi : B \to A$ a continuous homomorphism; one will
designate by $\mathfrak{J}$ (resp. $\mathfrak{K}$) an ideal of definition of $A$ (resp. $B$), such that
$\varphi(\mathfrak{K}) \subset \mathfrak{J}$, and one will set $X = \operatorname{Spec}(A)$, $Y =
\operatorname{Spec}(B)$, $\mathfrak{X} = \operatorname{Spf}(A)$, $\mathfrak{Y} = \operatorname{Spf}(B)$. Let $f : X \to
Y$ be the morphism of preschemes corresponding to $\varphi$ (1.6.1), $\widehat{f} : \mathfrak{X} \to \mathfrak{Y}$ its
extension to the completions (10.9.1), which is also the morphism of formal preschemes corresponding to $\varphi$
(10.2.2).

**Proposition (10.10.8).** For every $B$-module $N$ of finite type, there exists a canonical functorial isomorphism of
$\mathcal{O}_{\mathfrak{X}}$-Modules $$ \widehat{f}^{*}(N^{\Delta}) \cong (N \otimes_{B} A)^{\Delta}. $$

**Proof.** Indeed, denoting by $i_{X} : \mathfrak{X} \to X$ and $i_{Y} : \mathfrak{Y} \to Y$ the canonical morphisms,
one has (10.8.8), up to canonical functorial isomorphisms, $N^{\Delta} = i_{Y}^{*}(\widetilde{N})$ and $$ (N \otimes_{B}
A)^{\Delta} = i_{X}^{*}((N \otimes_{B} A)^{\sim}) = i_{X}^{*}(f^{*}(\widetilde{N})) $$ (1.6.5); the proposition
therefore results from the commutativity of the diagram (10.9.2).

**Corollary (10.10.9).** For every ideal $\mathfrak{b}$ of $B$, one has $\widehat{f}^{*}(\mathfrak{b}^{\Delta})
\mathcal{O}_{\mathfrak{X}} = (\mathfrak{b}A)^{\Delta}$.

**Proof.** Indeed, let $j$ be the canonical injection $\mathfrak{b} \to B$, to which corresponds the canonical injection
$j^{\Delta} : \mathfrak{b}^{\Delta} \to \mathcal{O}_{\mathfrak{Y}}$ of sheaves of $\mathcal{O}_{\mathfrak{Y}}$-Modules;
by definition, $\widehat{f}^{*}(\mathfrak{b}^{\Delta})\mathcal{O}_{\mathfrak{X}}$ is the image of the homomorphism
$\widehat{f}^{*}(j^{\Delta}) : \widehat{f}^{*}(\mathfrak{b}^{\Delta}) \to \mathcal{O}_{\mathfrak{X}} =
\widehat{f}^{*}(\mathcal{O}_{\mathfrak{Y}})$; but this homomorphism is identified with $(j \otimes 1)^{\Delta} :
(\mathfrak{b} \otimes_{B} A)^{\Delta} \to (B \otimes_{B} A)^{\Delta}$ by (10.10.8). Since the image of $j \otimes 1$ is
the ideal $\mathfrak{b}A$ of $A$, the image of $(j \otimes 1)^{\Delta}$ is therefore $(\mathfrak{b}A)^{\Delta}$ by
virtue of (10.10.2), whence the conclusion.

## 10.11. Coherent sheaves on formal preschemes

<!-- label: I.10.11 -->

**Proposition (10.11.1).** If $\mathfrak{X}$ is a locally Noetherian formal prescheme, the sheaf of rings
$\mathcal{O}_{\mathfrak{X}}$ is coherent and every sheaf of ideals of definition of $\mathfrak{X}$ is coherent.

**Proof.** The question being local, one is reduced to the case of a Noetherian formal affine scheme, and the
proposition therefore results from (10.10.3) and (10.10.5).

**(10.11.2)** Let $\mathfrak{X}$ be a locally Noetherian formal prescheme, $\mathcal{I}$ a sheaf of ideals of definition
of $\mathfrak{X}$, $X_{n}$ the (ordinary) locally Noetherian prescheme $(\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}^{n+1})$, so that $\mathfrak{X}$ is the inductive limit of the sequence $(X_{n})$
for the canonical morphisms $u_{nm} : X_{m} \to X_{n}$ (10.6.3). With these notations:

**Theorem (10.11.3).** For an $\mathcal{O}_{\mathfrak{X}}$-Module $\mathcal{F}$ to be coherent, it is necessary and
sufficient that it be isomorphic to a projective limit of a sequence $(\mathcal{F}_{n})$, where $\mathcal{F}_{n}$ is a
coherent $\mathcal{O}_{X_{n}}$-Module such that $u_{nm}^{*}(\mathcal{F}_{n}) = \mathcal{F}_{m}$ for $m \geq n$ (10.6.6).
The projective system $(\mathcal{F}_{n})$ is then isomorphic to the system of the $u_{n}^{*}(\mathcal{F}) = \mathcal{F}
\otimes_{\mathcal{O}_{\mathfrak{X}}} \mathcal{O}_{X_{n}}$, $u_{n}$ being the canonical morphism $X_{n} \to
\mathfrak{X}$.

**Proof.** The question being local, one is reduced to the case where $\mathfrak{X}$ is a Noetherian formal affine
scheme, and the theorem is then a consequence of (10.10.5) and (10.10.6).

One may therefore say that the datum of a coherent $\mathcal{O}_{\mathfrak{X}}$-Module is equivalent to that of a
projective system $(\mathcal{F}_{n})$ of coherent $\mathcal{O}_{X_{n}}$-Modules such that $u_{nm}^{*}(\mathcal{F}_{n}) =
\mathcal{F}_{m}$ for $m \geq n$.

**Corollary (10.11.4).** If $\mathcal{F}$ and $\mathcal{G}$ are two coherent $\mathcal{O}_{\mathfrak{X}}$-Modules, one
may (with the notations of (10.11.3)) define a canonical functorial isomorphism

$$ \operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G}) \cong \varprojlim_{n}
\operatorname{Hom}_{\mathcal{O}_{X_{n}}}(\mathcal{F}_{n}, \mathcal{G}_{n}) \tag{10.11.4.1} $$

**Proof.** The projective limit of the second member is to be understood for the maps $\theta_{n} \to
u_{nm}^{*}(\theta_{n})$ ($m \geq n$) of $\operatorname{Hom}_{\mathcal{O}_{X_{n}}}(\mathcal{F}_{n}, \mathcal{G}_{n})$
into $\operatorname{Hom}_{\mathcal{O}_{X_{m}}}(\mathcal{F}_{m}, \mathcal{G}_{m})$. The homomorphism (10.11.4.1) makes
correspond to an element $\theta \in \operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G})$ the
sequence $(u_{n}^{*}(\theta))$; one sees at once that one defines a homomorphism inverse to the preceding by making
correspond to the projective system $(\theta_{n}) \in \varprojlim
\operatorname{Hom}_{\mathcal{O}_{X_{n}}}(\mathcal{F}_{n}, \mathcal{G}_{n})$ its projective limit in
$\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G})$, taking account of (10.11.3).

**Corollary (10.11.5).** For a homomorphism $\theta : \mathcal{F} \to \mathcal{G}$ to be surjective, it is necessary and
sufficient that the corresponding homomorphism $\theta_{0} = u_{0}^{*}(\theta) : \mathcal{F}_{0} \to \mathcal{G}_{0}$
be.

**Proof.** The question being local, one is reduced to the case where $\mathfrak{X} = \operatorname{Spf}(A)$, $A$ being
adic Noetherian, $\mathcal{F} = M^{\Delta}$, $\mathcal{G} = N^{\Delta}$ and $\theta = u^{\Delta}$, where $M$ and $N$ are
$A$-modules of finite type and $u$ a homomorphism $M \to N$; one then has moreover $\theta_{0} = \widetilde{u_{0}}$,
where $u_{0}$ is the homomorphism $u \otimes 1 : M \otimes_{A} A/\mathfrak{J} \to N \otimes_{A} A/\mathfrak{J}$; the
conclusion results from the fact that $\theta$ and $u$ (resp. $\theta_{0}$ and $u_{0}$) are simultaneously surjective
(1.3.9 and 10.10.2) and from the fact that $u$ and $u_{0}$ are simultaneously surjective (0, 7.1.14).

**(10.11.6)** The th. (10.11.3) shows that one may consider every coherent $\mathcal{O}_{\mathfrak{X}}$-Module
$\mathcal{F}$ as a topological $\mathcal{O}_{\mathfrak{X}}$-Module, by considering it as the projective limit of the
sheaves of pseudo-discrete groups $\mathcal{F}_{n}$ (0, 3.8.1). It then results from (10.11.4) that every homomorphism $u
: \mathcal{F} \to \mathcal{G}$ of coherent $\mathcal{O}_{\mathfrak{X}}$-Modules is automatically continuous (0, 3.8.2).
Moreover, if $\mathcal{F}'$ is a coherent sub-$\mathcal{O}_{\mathfrak{X}}$-Module of a coherent
$\mathcal{O}_{\mathfrak{X}}$-Module $\mathcal{F}$, then for every open $U \subset \mathfrak{X}$, $\Gamma(U, \mathcal{F}')$
is a closed subgroup of the topological group $\Gamma(U, \mathcal{F})$, for the functor $\Gamma$ being left exact,
$\Gamma(U, \mathcal{F}')$ is the kernel of the homomorphism $\Gamma(U, \mathcal{F}) \to \Gamma(U,
\mathcal{F}/\mathcal{F}')$, which is continuous by what precedes, since $\mathcal{F}/\mathcal{F}'$ is coherent (0,
5.3.4); our assertion results from the fact that $\Gamma(U, \mathcal{F}/\mathcal{F}')$ is a separated topological group.

**Proposition (10.11.7).** Let $\mathcal{F}$ and $\mathcal{G}$ be two coherent $\mathcal{O}_{\mathfrak{X}}$-Modules. One
may define (with the notations of (10.11.3)) canonical functorial isomorphisms of topological
$\mathcal{O}_{\mathfrak{X}}$-Modules (10.11.6)

$$ \mathcal{F} \otimes_{\mathcal{O}_{\mathfrak{X}}} \mathcal{G} \cong \varprojlim_{n} (\mathcal{F}_{n}
\otimes_{\mathcal{O}_{X_{n}}} \mathcal{G}_{n}) \tag{10.11.7.1} $$

$$ \mathcal{H}om_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G}) \cong \varprojlim_{n}
\mathcal{H}om_{\mathcal{O}_{X_{n}}}(\mathcal{F}_{n}, \mathcal{G}_{n}) \tag{10.11.7.2} $$

**Proof.** The existence of the isomorphism (10.11.7.1) results from the formula $$ \mathcal{F}_{n}
\otimes_{\mathcal{O}_{X_{n}}} \mathcal{G}_{n} = (\mathcal{F} \otimes_{\mathcal{O}_{\mathfrak{X}}} \mathcal{O}_{X_{n}})
\otimes_{\mathcal{O}_{X_{n}}} (\mathcal{G} \otimes_{\mathcal{O}_{\mathfrak{X}}} \mathcal{O}_{X_{n}}) = (\mathcal{F}
\otimes_{\mathcal{O}_{\mathfrak{X}}} \mathcal{G}) \otimes_{\mathcal{O}_{\mathfrak{X}}} \mathcal{O}_{X_{n}} $$ and from
(10.11.3). The isomorphism (10.11.7.2), where the two members are considered as sheaves of modules without topology,
results from the definition of the sections of $\mathcal{H}om_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G})$
and $\mathcal{H}om_{\mathcal{O}_{X_{n}}}(\mathcal{F}_{n}, \mathcal{G}_{n})$ and from the existence of the isomorphism
(10.11.4.1), applied to the prescheme induced on an arbitrary Noetherian formal affine open of $\mathfrak{X}$. It
remains to prove that the isomorphism (10.11.7.2) is bicontinuous over a quasi-compact set, and one is therefore reduced
to the case where $\mathfrak{X} = \operatorname{Spf}(A)$, $A$ being adic Noetherian, whence (10.10.5) $\mathcal{F} =
M^{\Delta}$, $\mathcal{G} = N^{\Delta}$, $M$, $N$ being $A$-modules of finite type; taking account of (10.10.2.1),
(10.10.2.3), and (1.3.12, (ii)), one is reduced to showing that the canonical isomorphism $\operatorname{Hom}_{A}(M, N)
\cong \varprojlim_{n} \operatorname{Hom}_{A_{n}}(M_{n}, N_{n})$ (with $M_{n} = M \otimes_{A} A_{n}$, $N_{n} = N
\otimes_{A} A_{n}$) is continuous, which was proved in (0, 7.8.2).

**(10.11.8)** Since $\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G})$ is the group of sections
of the sheaf of topological groups $\mathcal{H}om_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G})$, it is
equipped with a group topology. If $\mathfrak{X}$ is Noetherian, it results from (10.11.7.2) that a fundamental system
of neighborhoods of $0$ in this group is obtained by taking the subgroups
$\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{I}^{n}\mathcal{G})$ ($n$ arbitrary).

**Proposition (10.11.9).** Let $\mathfrak{X}$ be a Noetherian formal prescheme, $\mathcal{F}$ and $\mathcal{G}$ two
coherent $\mathcal{O}_{\mathfrak{X}}$-Modules. In the topological group
$\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G})$ the surjective (resp. injective, bijective)
homomorphisms form an open part.

**Proof.** By virtue of (10.11.5), the set of surjective homomorphisms in
$\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G})$ is the inverse image, under the continuous
map $\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G}) \to
\operatorname{Hom}_{\mathcal{O}_{X_{0}}}(\mathcal{F}_{0}, \mathcal{G}_{0})$, of a part of the discrete group
$\operatorname{Hom}_{\mathcal{O}_{X_{0}}}(\mathcal{F}_{0}, \mathcal{G}_{0})$, whence the first assertion. To demonstrate
the second, let us cover $\mathfrak{X}$ by a finite number of Noetherian formal affine opens $U_{i}$. For $\theta \in
\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G})$ to be injective, it is necessary and
sufficient that all its images under the (continuous) restriction maps
$\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G}) \to
\operatorname{Hom}_{\mathcal{O}_{U_{i}}}(\mathcal{F}|U_{i}, \mathcal{G}|U_{i})$ be; one is therefore reduced to the
affine case, and then this has already been proved in (0, 7.8.3).

## 10.12. Adic morphisms of formal preschemes

<!-- label: I.10.12 -->

**(10.12.1)** Let $\mathfrak{X}$, $\mathfrak{G}$ be two locally Noetherian formal preschemes; we shall say that a
morphism $f : \mathfrak{X} \to \mathfrak{G}$ is _adic_ if there exists an Ideal of definition $\mathcal{I}$ of
$\mathfrak{G}$ such that $\mathcal{J} = f^{*}(\mathcal{I})\mathcal{O}_{\mathfrak{X}}$ is an Ideal of definition of
$\mathfrak{X}$; one also says then that $\mathfrak{X}$ is an _adic $\mathfrak{G}$-prescheme_ (for $f$). When this is so,
for every Ideal of definition $\mathcal{I}_{1}$ of $\mathfrak{G}$, $\mathcal{J}_{1} =
f^{*}(\mathcal{I}_{1})\mathcal{O}_{\mathfrak{X}}$ is an Ideal of definition of $\mathfrak{X}$. Indeed, the question
being local, one may suppose $\mathfrak{X}$ and $\mathfrak{G}$ affine Noetherian; there exists therefore an integer $n$
such that $\mathcal{I}^{n} \subset \mathcal{I}_{1}$ and $\mathcal{I}_{1}^{n} \subset \mathcal{I}$ (10.3.6 and 0, 7.1.4),
whence $\mathcal{J}^{n} \subset \mathcal{J}_{1}$ and $\mathcal{J}_{1}^{n} \subset \mathcal{J}$. The first of these
relations proves that $\mathcal{J}_{1} = \mathfrak{g}_{1}^{\Delta}$, where $\mathfrak{g}_{1}$ is an open ideal of $A =
\Gamma(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$, and the second proves that $\mathfrak{g}_{1}$ is an ideal of
definition of $A$ (0, 7.1.4), whence our assertion.

It results at once from what precedes that if $\mathfrak{X}$ and $\mathfrak{Y}$ are two adic $\mathfrak{G}$-preschemes,
every $\mathfrak{G}$-morphism $u : \mathfrak{X} \to \mathfrak{Y}$ is adic: indeed, if $f : \mathfrak{X} \to
\mathfrak{G}$, $g : \mathfrak{Y} \to \mathfrak{G}$ are the structure morphisms, and $\mathcal{I}$ an Ideal of definition
of $\mathfrak{G}$, one has $f = g \circ u$, hence
$u^{*}(g^{*}(\mathcal{I})\mathcal{O}_{\mathfrak{Y}})\mathcal{O}_{\mathfrak{X}} =
f^{*}(\mathcal{I})\mathcal{O}_{\mathfrak{X}}$ is an Ideal of definition of $\mathfrak{X}$, and by hypothesis
$g^{*}(\mathcal{I})\mathcal{O}_{\mathfrak{Y}}$ is an Ideal of definition of $\mathfrak{Y}$.

**(10.12.2)** In what follows, we shall suppose fixed a locally Noetherian formal prescheme $\mathfrak{G}$ and an Ideal
of definition $\mathcal{I}$ of $\mathfrak{G}$; we shall set $S_{n} = (\mathfrak{G}, \mathcal{O}_{\mathfrak{G}}/\mathcal{I}^{n+1})$.
The adic (locally Noetherian) $\mathfrak{G}$-preschemes evidently form a category. We shall say that an inductive system
$(X_{n})$ of (ordinary) locally Noetherian $S_{n}$-preschemes is an _adic $(S_{n})$-inductive system_ if the structure
morphisms $f_{n} : X_{n} \to S_{n}$ are such that, for $m \geq n$, the diagrams
$$ \begin{array}{ccc} X_{n} & \xleftarrow{} & X_{m} \\ \downarrow f_{n} & & \downarrow f_{m} \\ S_{n} & \xleftarrow{} &
S_{m} \end{array} \tag{10.12.2.1} $$
are commutative and identify $X_{m}$ with the product $X_{n} \times_{S_{n}} S_{m} = (X_{n})_{(S_{m})}$. The adic inductive
systems form a category: it suffices indeed to define a morphism $(X_{n}) \to (Y_{n})$ of such systems as an inductive
system of $S_{n}$-morphisms $u_{n} : X_{n} \to Y_{n}$ such that $u_{m}$ is identified with $(u_{n})_{(S_{m})}$ for $m \geq
n$. This being so:

**Theorem (10.12.3).** There is a canonical equivalence between the category of adic $\mathfrak{G}$-preschemes and the
category of adic $(S_{n})$-inductive systems.

**Proof.** The equivalence in question is obtained in the following way: if $\mathfrak{X}$ is an adic
$\mathfrak{G}$-prescheme, $f : \mathfrak{X} \to \mathfrak{G}$ the structure morphism, $\mathcal{J} =
f^{*}(\mathcal{I})\mathcal{O}_{\mathfrak{X}}$ is an Ideal of definition of $\mathfrak{X}$ and one makes correspond to
$\mathfrak{X}$ the inductive system of the $X_{n} = (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}}/\mathcal{J}^{n+1})$, the
structure morphism $f_{n} : X_{n} \to S_{n}$ corresponding to $f$ (10.5.6). Let us first show that $(X_{n})$ is an adic
inductive system: if $f = (\psi, \theta)$, one has $\psi^{*}(\mathcal{I})\mathcal{O}_{\mathfrak{X}} = \mathcal{J}$,
hence $\psi^{*}(\mathcal{I}^{n+1})\mathcal{O}_{\mathfrak{X}} = \mathcal{J}^{n+1}$ for every $n$, and (by the exactness
of the functor $\psi^{*}$) $\mathcal{J}^{m+1}/\mathcal{J}^{n+1} =
\psi^{*}(\mathcal{I}^{m+1}/\mathcal{I}^{n+1})(\mathcal{O}_{\mathfrak{X}}/\mathcal{J}^{n+1})$ for $m \geq n$; our
conclusion therefore results from (4.4.5). It is immediate moreover to verify that to a $\mathfrak{G}$-morphism $u :
\mathfrak{X} \to \mathfrak{Y}$ of adic $\mathfrak{G}$-preschemes there corresponds (with evident notations) an inductive
system of $S_{n}$-morphisms $u_{n} : X_{n} \to Y_{n}$ such that $u_{m}$ is identified with $(u_{n})_{(S_{m})}$ for $m
\geq n$.

The fact that one has indeed thus defined an equivalence will result from the following more precise proposition:

**Proposition (10.12.3.1).** Let $(X_{n})$ be an inductive system of $S_{n}$-preschemes; suppose that the structure
morphisms $f_{n} : X_{n} \to S_{n}$ are such that the diagrams (10.12.2.1) are commutative and identify $X_{m}$ with
$X_{n} \times_{S_{n}} S_{m}$ for $m \geq n$. Then the inductive system $(X_{n})$ verifies the conditions b) and c) of
(10.6.3); let $\mathfrak{X}$ be its inductive limit, $f : \mathfrak{X} \to \mathfrak{G}$ the morphism inductive limit of
the inductive system $(f_{n})$. Then, if $X_{0}$ is locally Noetherian, $\mathfrak{X}$ is locally Noetherian and $f$ is
an adic morphism.

**Proof.** Since the sheaf of ideals of $\mathcal{O}_{S_{m}}$ which defines the subprescheme $S_{n}$ of $S_{m}$ is
nilpotent, so is, by virtue of (4.4.5), the sheaf of ideals of $\mathcal{O}_{X_{m}}$ defining the subprescheme $X_{n}$
of $X_{m}$, hence the conditions of (10.6.3) are indeed verified. The question is consequently local on $\mathfrak{X}$
and $\mathfrak{G}$ and one may suppose that $\mathfrak{G} = \operatorname{Spf}(A)$, $\mathcal{I} =
\mathfrak{J}^{\Delta}$, $A$ being a $\mathfrak{J}$-adic Noetherian ring, and $X_{n} = \operatorname{Spec}(B_{n})$; if
$A_{n} = A/\mathfrak{J}^{n+1}$, the hypothesis entails that $B_{0}$ is Noetherian and that if one sets $S_{n} =
S/\mathfrak{J}^{n+1}$, $B_{m} = B_{n} \otimes_{A_{n}} A_{m}$. The kernel of $B_{n} \to B_{0}$ is therefore $\mathfrak{R}
= \mathfrak{J}B_{n}$ and the kernel of $B_{m} \to B_{n}$ is $\mathfrak{R}^{n+1}$ for $m \geq n$; moreover, since $A_{n}$
is Noetherian, $\mathfrak{R}$ is of finite type over $A_{n}$, hence $\mathfrak{R}/\mathfrak{R}^{2}$ is of finite type
over $B_{n}$, and a fortiori over $B_{0} = B_{n}/\mathfrak{R}$; the fact that $\mathfrak{X}$ is Noetherian then results
from (10.6.4); if $B = \varprojlim B_{n}$ one has $\mathfrak{X} = \operatorname{Spf}(B)$, and if $\mathfrak{n}$ is the
kernel of $B \to B_{0}$, $B_{n} = B/\mathfrak{n}^{n+1}$. If $\rho_{n} : A/\mathfrak{J}^{n+1} \to B/\mathfrak{n}^{n+1}$
is the homomorphism corresponding to $f_{n}$, one therefore has $\mathfrak{n}^{n+1}/\mathfrak{n}^{n+2} =
\rho_{n}(\mathfrak{J}^{n+1}/\mathfrak{J}^{n+2})$; as the homomorphism $\rho : A \to B$ corresponding to $f$ is equal to
$\varprojlim \rho_{n}$, the ideal $\mathfrak{J}B$ of $B$ is dense in $\mathfrak{n}$, and since every ideal of $B$ is
closed (0, 7.3.5), one has $\mathfrak{n} = \mathfrak{J}B$. If $\mathcal{J} = \mathfrak{n}^{\Delta}$, the relation
$f^{*}(\mathcal{I})\mathcal{O}_{\mathfrak{X}} = \mathcal{J}$ then results from (10.10.9) and finishes the demonstration.

**(10.12.3.2)** The preceding equivalence furnishes, for two adic $\mathfrak{G}$-preschemes $\mathfrak{X}$,
$\mathfrak{Y}$, a canonical bijection $$ \operatorname{Hom}_{\mathfrak{G}}(\mathfrak{X}, \mathfrak{Y}) \cong
\varprojlim_{n} \operatorname{Hom}_{S_{n}}(X_{n}, Y_{n}) $$ the projective limit being relative to the maps $u_{n} \to
(u_{n})_{(S_{m})}$ for $m \geq n$.

## 10.13. Morphisms of finite type

<!-- label: I.10.13 -->

**Proposition (10.13.1).** Let $\mathfrak{Y}$ be a locally Noetherian formal prescheme, $\mathcal{J}$ an Ideal of
definition of $\mathfrak{Y}$, $f : \mathfrak{X} \to \mathfrak{Y}$ a morphism of formal preschemes. The following
conditions are equivalent:

a) $\mathfrak{X}$ is locally Noetherian, $f$ is an adic morphism (10.12.1) and if one sets $\mathcal{I} =
f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}}$, the morphism $f_{0} : (\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}/\mathcal{I}) \to (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}}/\mathcal{J})$ deduced from $f$ is
of finite type.

b) $\mathfrak{X}$ is locally Noetherian, and is the inductive limit of an adic $(Y_{n})$-inductive system $(X_{n})$ such
that the morphism $X_{0} \to Y_{0}$ is of finite type.

c) Every point of $\mathfrak{Y}$ possesses a Noetherian formal affine open neighborhood $V$ having the following
property:

(Q) $f^{-1}(V)$ is the union of a finite family of Noetherian formal affine opens $U_{i}$ such that the adic Noetherian
ring $\Gamma(U_{i}, \mathcal{O}_{\mathfrak{X}})$ is topologically isomorphic to the quotient of an algebra of restricted
formal power series (0, 7.5.1) over $\Gamma(V, \mathcal{O}_{\mathfrak{Y}})$, by an ideal (necessarily closed).

**Proof.** It is immediate that a) entails b) by virtue of (10.12.3). To show that b) entails c), one may, since the
question is local on $\mathfrak{Y}$, suppose that $\mathfrak{Y} = \operatorname{Spf}(B)$, where $B$ is adic Noetherian;
let $\mathcal{J} = \mathfrak{K}^{\Delta}$, $\mathfrak{K}$ being an ideal of definition of $B$. Since by hypothesis
$X_{0}$ is of finite type over $Y_{0}$, $X_{0}$ is the finite union of affine opens $U_{i}$ such that the ring $A_{i0}$
of the affine scheme induced by $X_{0}$ on $U_{i}$ is an algebra of finite type over the ring $B/\mathfrak{K}$ of
$Y_{0}$ (6.3.2). By virtue of (5.1.9), $U_{i}$ is also an affine open in each of the Noetherian preschemes $X_{n}$, and
if $A_{in}$ is the ring of the affine scheme induced by $X_{n}$ on $U_{i}$, hypothesis b) entails that for $m \geq n$,
$A_{in}$ is isomorphic to $A_{im}/\mathfrak{K}^{n+1}A_{im}$. Consequently, the formal prescheme induced on $U_{i}$ by
$\mathfrak{X}$ is isomorphic to $\operatorname{Spf}(A_{i})$, where $A_{i} = \varprojlim_{n} A_{in}$ (10.6.4); $A_{i}$ is
a $\mathfrak{K}A_{i}$-adic ring, and $A_{i}/\mathfrak{K}A_{i}$, isomorphic to $A_{i0}$, is an algebra of finite type
over $B/\mathfrak{K}$. One concludes (0, 7.5.5) that $A_{i}$ is topologically isomorphic to a quotient of an algebra of
restricted formal power series over $B$ (by a necessarily closed ideal, since such an algebra is Noetherian (0, 7.5.4)).

To demonstrate that c) entails a), one may limit oneself to the case where $\mathfrak{Y} = \operatorname{Spf}(A)$ is
also affine, $A$ being an adic Noetherian ring, isomorphic to the quotient of an algebra of restricted formal power
series over $B$ by a closed ideal. Then (0, 7.5.5), $A/\mathfrak{K}A$ is an algebra of finite type over
$B/\mathfrak{K}$, and $\mathfrak{K}A = \mathfrak{J}$ is an ideal of definition of $A$, hence, by virtue of (10.10.9),
the conditions of a) are satisfied.

One will note that if the conditions of prop. (10.13.1) are fulfilled, property a) is valid for every Ideal of
definition $\mathcal{J}$ of $\mathfrak{Y}$ (by virtue of c)), and consequently, in property b), all the $f_{n}$ are
morphisms of finite type.

**Corollary (10.13.2).** If the conditions of (10.13.1) are verified, every Noetherian formal affine open $V$ of
$\mathfrak{Y}$ possesses property (Q), and if $\mathfrak{Y}$ is Noetherian, so is $\mathfrak{X}$.

**Proof.** This results at once from (10.13.1) and from (6.3.2).

**Definition (10.13.3).** When the equivalent properties a), b), c) of (10.13.1) are verified, one says that the
morphism $f$ is _of finite type_, or that $\mathfrak{X}$ is a _$\mathfrak{Y}$-formal prescheme of finite type_, or a
_formal prescheme of finite type over $\mathfrak{Y}$_.

**Corollary (10.13.4).** Let $\mathfrak{X} = \operatorname{Spf}(A)$, $\mathfrak{Y} = \operatorname{Spf}(B)$ be two
Noetherian formal affine schemes; for $\mathfrak{X}$ to be of finite type over $\mathfrak{Y}$, it is necessary and
sufficient that the adic Noetherian ring $A$ be isomorphic to the quotient of an algebra of restricted formal power
series over $B$ by a closed ideal.

**Proof.** Indeed, with the notations of (10.13.1), if $\mathfrak{X}$ is of finite type over $\mathfrak{Y}$,
$A/\mathfrak{K}A$ is then a $(B/\mathfrak{K})$-algebra of finite type by virtue of (6.3.3) and $\mathfrak{K}A$ is an
ideal of definition of $A$ (10.10.9). One therefore concludes by (0, 7.5.5).

**Proposition (10.13.5).** (i) The composite of two morphisms of formal preschemes which are of finite type is of finite
type.

(ii) Let $\mathfrak{X}$, $\mathfrak{G}$, $\mathfrak{G}'$ be three locally Noetherian (resp. Noetherian) formal
preschemes, $f : \mathfrak{X} \to \mathfrak{G}$, $g : \mathfrak{G}' \to \mathfrak{G}$ two morphisms. If $f$ is of finite
type, $\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{G}'$ is locally Noetherian (resp. Noetherian) and is of finite type
over $\mathfrak{G}'$.

(iii) Let $\mathfrak{G}$ be a locally Noetherian formal prescheme, $\mathfrak{X}'$, $\mathfrak{Y}'$ two locally
Noetherian $\mathfrak{G}$-formal preschemes such that $\mathfrak{X}' \times_{\mathfrak{G}} \mathfrak{Y}'$ is locally
Noetherian. If $\mathfrak{X}$, $\mathfrak{Y}$ are locally Noetherian $\mathfrak{G}$-formal preschemes, $f : \mathfrak{X}
\to \mathfrak{X}'$, $g : \mathfrak{Y} \to \mathfrak{Y}'$ two $\mathfrak{G}$-morphisms of finite type, $\mathfrak{X}
\times_{\mathfrak{G}} \mathfrak{Y}$ is locally Noetherian and $f \times_{\mathfrak{G}} g$ is a $\mathfrak{G}$-morphism
of finite type.

**Proof.** (iii) is deduced from (i) and (ii) by the formal reasoning of (3.5.1) and it therefore suffices to prove (i)
and (ii).

Let $\mathfrak{X}$, $\mathfrak{Y}$, $\mathfrak{Z}$ be three locally Noetherian formal preschemes, $f : \mathfrak{X} \to
\mathfrak{Y}$, $g : \mathfrak{Y} \to \mathfrak{Z}$ two morphisms of finite type. If $\mathcal{L}$ is an Ideal of
definition of $\mathfrak{Z}$, $\mathcal{J} = g^{*}(\mathcal{L})\mathcal{O}_{\mathfrak{Y}}$ is one for $\mathfrak{Y}$ and
$\mathcal{I} = f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}}$ is one for $\mathfrak{X}$. Set $X_{0} = (\mathfrak{X},
\mathcal{O}_{\mathfrak{X}}/\mathcal{I})$, $Y_{0} = (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}}/\mathcal{J})$, $Z_{0} =
(\mathfrak{Z}, \mathcal{O}_{\mathfrak{Z}}/\mathcal{L})$ and let $f_{0} : X_{0} \to Y_{0}$, $g_{0} : Y_{0} \to Z_{0}$ be
the morphisms corresponding to $f$ and $g$. Since by hypothesis $f_{0}$ and $g_{0}$ are of finite type, so is $g_{0}
\circ f_{0}$ (6.3.4) which corresponds to $g \circ f$; hence $g \circ f$ is of finite type by (10.13.1).

Under the conditions of (ii), $\mathfrak{G}$ (resp. $\mathfrak{X}$, $\mathfrak{G}'$) is the inductive limit of a
sequence $(S_{n})$ (resp. $(X_{n})$, $(S'_{n})$) of locally Noetherian preschemes and one may suppose (10.13.1) that
$X_{m} = X_{n} \times_{S_{n}} S_{m}$ for $m \geq n$. The formal prescheme $\mathfrak{X} \times_{\mathfrak{G}}
\mathfrak{G}'$ is then the inductive limit of the preschemes $X_{n} \times_{S_{n}} S'_{n}$ (10.7.4), and one has $$
X_{n} \times_{S_{n}} S'_{n} = (X_{n} \times_{S_{n}} S_{n}) \times_{S_{n}} S'_{n} = (X_{n} \times_{S_{n}} S'_{n})
\times_{S'_{n}} S'_{n}. $$ Moreover, $X_{0} \times_{S_{0}} S'_{0}$ is locally Noetherian since $X_{0}$ is of finite type
over $S_{0}$ (6.3.8). One concludes first (10.12.3.1) that $\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{G}'$ is locally
Noetherian; moreover, since $X_{0} \times_{S_{0}} S'_{0}$ is of finite type over $S'_{0}$ (6.3.8), it results from
(10.12.3.1) and from (10.13.1) that $\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{G}'$ is of finite type over
$\mathfrak{G}'$, which finishes proving (ii) (the assertion relative to the Noetherian preschemes being an immediate
consequence of (6.3.8)).

**Corollary (10.13.6).** Under the hypotheses of (10.9.9), if $f$ is a morphism of finite type, so is its extension
$\widehat{f}$ to the completions.

## 10.14. Closed subpreschemes of formal preschemes

<!-- label: I.10.14 -->

**Proposition (10.14.1).** Let $\mathfrak{X}$ be a locally Noetherian formal prescheme, $\mathcal{J}$ a coherent sheaf
of ideals of $\mathcal{O}_{\mathfrak{X}}$. If $\mathfrak{Y}$ is the (closed) support of
$\mathcal{O}_{\mathfrak{X}}/\mathcal{J}$, the topologically ringed space $(\mathfrak{Y},
(\mathcal{O}_{\mathfrak{X}}/\mathcal{J})|\mathfrak{Y})$ is a locally Noetherian formal prescheme, which is Noetherian if
$\mathfrak{X}$ is.

**Proof.** Let us note that $\mathcal{O}_{\mathfrak{X}}/\mathcal{J}$ is coherent by virtue of (10.10.3) and (0, 5.3.4),
hence its support $\mathfrak{Y}$ is closed (0, 5.2.2). Let $\mathcal{I}$ be an Ideal of definition of $\mathfrak{X}$, and
let $\mathcal{R}_{n} = (\mathcal{J} + \mathcal{I}^{n+1})/\mathcal{I}^{n+1}$; the sheaf of rings
$\mathcal{O}_{\mathfrak{X}}/\mathcal{J}$ is the projective limit of the sheaves $\mathcal{O}_{\mathfrak{X}}/(\mathcal{J} +
\mathcal{I}^{n+1}) = (\mathcal{O}_{\mathfrak{X}}/\mathcal{J}) \otimes_{\mathcal{O}_{\mathfrak{X}}} (\mathcal{O}_{\mathfrak{X}}/\mathcal{I}^{n+1})$
(10.11.3), which all have $\mathfrak{Y}$ for support. The sheaf $(\mathcal{J} + \mathcal{I}^{n+1})/\mathcal{I}^{n+1}$ is a
coherent $\mathcal{O}_{\mathfrak{X}}$-Module, since $\mathcal{I}^{n+1}$ is coherent, hence $(\mathcal{J} +
\mathcal{I}^{n+1})/\mathcal{I}^{n+1}$ is also a coherent $(\mathcal{O}_{\mathfrak{X}}/\mathcal{I}^{n+1})$-Module (0,
5.3.10); if $Y_{n}$ is the closed subprescheme of $X_{n}$ defined by this sheaf of ideals, it is immediate that
$(\mathfrak{Y}, (\mathcal{O}_{\mathfrak{X}}/\mathcal{J})|\mathfrak{Y})$ is the formal prescheme inductive limit of the
$Y_{n}$, and since the conditions of (10.6.4) are satisfied, this proves that this formal prescheme is locally
Noetherian, and Noetherian if $\mathfrak{X}$ is (since then $Y_{0}$ is by virtue of (6.1.4)).

**Definition (10.14.2).** One calls _closed subprescheme_ of a formal prescheme $\mathfrak{X}$ every formal prescheme
$(\mathfrak{Y}, (\mathcal{O}_{\mathfrak{X}}/\mathcal{J})|\mathfrak{Y})$ where $\mathcal{J}$ is a coherent
$\mathcal{O}_{\mathfrak{X}}$-Module; one says that this prescheme is the closed subprescheme defined by $\mathcal{J}$.

It is clear that the correspondence thus defined between coherent $\mathcal{O}_{\mathfrak{X}}$-Modules and closed
subpreschemes of $\mathfrak{X}$ is one-to-one.

The morphism of topologically ringed spaces $j = (\psi, \theta) : \mathfrak{Y} \to \mathfrak{X}$, where $\psi$ is the
injection $\mathfrak{Y} \to \mathfrak{X}$ and $\theta$ the canonical homomorphism $\mathcal{O}_{\mathfrak{X}} \to
\mathcal{O}_{\mathfrak{X}}/\mathcal{J}$, is evidently (10.4.5) a morphism of formal preschemes, which one calls the
_canonical injection_ of $\mathfrak{Y}$ into $\mathfrak{X}$. One will note that if $\mathfrak{X} =
\operatorname{Spf}(A)$, where $A$ is adic Noetherian, one has $\mathcal{J} = \mathfrak{a}^{\Delta}$, where
$\mathfrak{a}$ is an ideal of $A$ (10.10.5), and it results at once from what precedes that one then has $\mathfrak{Y} =
\operatorname{Spf}(A/\mathfrak{a})$ up to an isomorphism, and that $j$ corresponds (10.2.2) to the canonical
homomorphism $A \to A/\mathfrak{a}$.

One says that a morphism $f : \mathfrak{Z} \to \mathfrak{X}$ of locally Noetherian formal preschemes is a _closed
immersion_ if it factors as $\mathfrak{Z} \xrightarrow{g} \mathfrak{Y} \xrightarrow{j} \mathfrak{X}$, where $g$ is an
isomorphism of $\mathfrak{Z}$ onto a closed subprescheme $\mathfrak{Y}$ of $\mathfrak{X}$ and $j$ the canonical
injection. Since $j$ is a monomorphism of ringed spaces, $g$ and $\mathfrak{Y}$ are necessarily unique.

**Proposition (10.14.3).** A closed immersion is a morphism of finite type.

**Proof.** One reduces at once to the case where $\mathfrak{X}$ is a formal affine scheme $\operatorname{Spf}(A)$ and
$\mathfrak{Y} = \operatorname{Spf}(A/\mathfrak{a})$; the proposition results from (10.13.1, c)).

**Lemma (10.14.4).** Let $f : \mathfrak{Y} \to \mathfrak{X}$ be a morphism of locally Noetherian formal preschemes, and
let $(U_{\alpha})$ be a covering of $f(\mathfrak{Y})$ by Noetherian formal affine opens of $\mathfrak{X}$, such that the
$f^{-1}(U_{\alpha})$ are Noetherian formal affine opens of $\mathfrak{Y}$. For $f$ to be a closed immersion, it is
necessary and sufficient that $f(\mathfrak{Y})$ be a closed part of $\mathfrak{X}$ and that, for every $\alpha$, the
restriction of $f$ to $f^{-1}(U_{\alpha})$ correspond (10.4.6) to a surjective homomorphism $\Gamma(U_{\alpha},
\mathcal{O}_{\mathfrak{X}}) \to \Gamma(f^{-1}(U_{\alpha}), \mathcal{O}_{\mathfrak{Y}})$.

**Proof.** The conditions are evidently necessary. Conversely, if they are fulfilled, and if one designates by
$\mathfrak{a}_{\alpha}$ the kernel of $\Gamma(U_{\alpha}, \mathcal{O}_{\mathfrak{X}}) \to \Gamma(f^{-1}(U_{\alpha}),
\mathcal{O}_{\mathfrak{Y}})$, one defines a coherent sheaf of ideals $\mathcal{J}$ of $\mathcal{O}_{\mathfrak{X}}$ by
taking $\mathcal{J}|U_{\alpha} = \mathfrak{a}_{\alpha}^{\Delta}$, and by taking $\mathcal{J}$ null in the complement of
the union of the $U_{\alpha}$. Indeed, since $f(\mathfrak{Y})$ is closed and the support of
$\mathfrak{a}_{\alpha}^{\Delta}$ is $U_{\alpha} \cap f(\mathfrak{Y})$, everything reduces to verifying that
$\mathfrak{a}_{\alpha}^{\Delta}$ and $\mathfrak{a}_{\beta}^{\Delta}$ induce the same sheaf on a Noetherian formal affine
open $V \subset U_{\alpha} \cap U_{\beta}$. Now, the restriction of $f$ to $f^{-1}(U_{\alpha})$ being a closed immersion
of this formal prescheme into $U_{\alpha}$, $f^{-1}(V)$ is a Noetherian formal affine open in $f^{-1}(U_{\alpha})$ and
the restriction of $f$ to $f^{-1}(V)$ is a closed immersion; if $\mathfrak{b}$ is the kernel of the surjective
homomorphism $\Gamma(V, \mathcal{O}_{\mathfrak{X}}) \to \Gamma(f^{-1}(V), \mathcal{O}_{\mathfrak{Y}})$ corresponding to
this restriction, it is immediate (10.10.2) that $\mathfrak{a}_{\alpha}^{\Delta}$ induces $\mathfrak{b}^{\Delta}$ on
$V$. The sheaf of ideals $\mathcal{J}$ being thus defined, it is then clear that $f = g \circ j$, where $j :
\mathfrak{Z} \to \mathfrak{X}$ is the canonical injection of the closed subprescheme $\mathfrak{Z}$ of $\mathfrak{X}$
defined by $\mathcal{J}$, and $g$ an isomorphism of $\mathfrak{Y}$ onto $\mathfrak{Z}$.

**Proposition (10.14.5).** (i) If $f : \mathfrak{Z} \to \mathfrak{Y}$, $g : \mathfrak{Y} \to \mathfrak{X}$ are closed
immersions of locally Noetherian formal preschemes, $g \circ f$ is a closed immersion.

(ii) Let $\mathfrak{X}$, $\mathfrak{Y}$, $\mathfrak{Z}$ be three locally Noetherian formal preschemes, $f : \mathfrak{X}
\to \mathfrak{Z}$ a closed immersion, $g : \mathfrak{Y} \to \mathfrak{Z}$ a morphism. Then the morphism $\mathfrak{X}
\times_{\mathfrak{Z}} \mathfrak{Y} \to \mathfrak{Y}$ is a closed immersion.

(iii) Let $\mathfrak{G}$ be a locally Noetherian formal prescheme, $\mathfrak{X}'$, $\mathfrak{Y}'$ two
$\mathfrak{G}$-formal preschemes locally Noetherian such that $\mathfrak{X}' \times_{\mathfrak{G}} \mathfrak{Y}'$ is
locally Noetherian. If $\mathfrak{X}$, $\mathfrak{Y}$ are locally Noetherian $\mathfrak{G}$-formal preschemes, $f :
\mathfrak{X} \to \mathfrak{X}'$, $g : \mathfrak{Y} \to \mathfrak{Y}'$ two $\mathfrak{G}$-morphisms which are closed
immersions, then $f \times_{\mathfrak{G}} g$ is a closed immersion.

**Proof.** By virtue of (3.5.1), it again suffices to prove (i) and (ii).

To demonstrate (i), one may suppose that $\mathfrak{Y}$ (resp. $\mathfrak{Z}$) is a closed subprescheme of
$\mathfrak{X}$ (resp. $\mathfrak{Y}$) defined by a coherent sheaf $\mathcal{J}$ (resp. $\mathcal{K}$) of ideals of
$\mathcal{O}_{\mathfrak{X}}$ (resp. $\mathcal{O}_{\mathfrak{Y}}$); if $\psi$ is the injection $\mathfrak{Y} \to
\mathfrak{X}$ of the underlying spaces, $\psi_{*}(\mathcal{K})$ is a coherent sheaf of ideals of
$\psi_{*}(\mathcal{O}_{\mathfrak{Y}}) = \mathcal{O}_{\mathfrak{X}}/\mathcal{J}$ (0, 5.3.12), hence also a coherent
$\mathcal{O}_{\mathfrak{X}}$-Module (0, 5.3.10); the kernel $\mathcal{K}_{1}$ of $\mathcal{O}_{\mathfrak{X}} \to
(\mathcal{O}_{\mathfrak{X}}/\mathcal{J})/\psi_{*}(\mathcal{K})$ is therefore a coherent sheaf of ideals of
$\mathcal{O}_{\mathfrak{X}}$ (0, 5.3.4), and $\mathcal{O}_{\mathfrak{X}}/\mathcal{K}_{1}$ is isomorphic to
$\psi_{*}(\mathcal{O}_{\mathfrak{Y}}/\mathcal{K})$, which proves that $\mathfrak{Z}$ is isomorphic to a closed
subprescheme of $\mathfrak{X}$.

To demonstrate (ii), it is immediate that one may limit oneself to the case where $\mathfrak{Z} =
\operatorname{Spf}(A)$, $\mathfrak{X} = \operatorname{Spf}(B)$, $\mathfrak{Y} = \operatorname{Spf}(C)$, $A$ being a
$\mathfrak{J}$-adic Noetherian ring, $B = A/\mathfrak{a}$, where $\mathfrak{a}$ is an ideal of $A$, $C$ an adic and
Noetherian topological $A$-algebra. Everything reduces to proving that the homomorphism $C \to C \widehat{\otimes}_{A}
(A/\mathfrak{a})$ is surjective: now, $A/\mathfrak{a}$ is an $A$-module of finite type, and its topology is the
$\mathfrak{J}$-adic topology; it then results from (0, 7.7.8) that $C \widehat{\otimes}_{A} (A/\mathfrak{a})$ is
identified with $C \otimes_{A} (A/\mathfrak{a}) = C/\mathfrak{a}C$, whence our assertion.

**Corollary (10.14.6).** Under the hypotheses of (10.14.5, (ii)), let $p : \mathfrak{X} \times_{\mathfrak{Z}} \mathfrak{Y}
\to \mathfrak{X}$, $q : \mathfrak{X} \times_{\mathfrak{Z}} \mathfrak{Y} \to \mathfrak{Y}$ be the projections, so that the
diagram
$$ \begin{array}{ccc} \mathfrak{X} & \xleftarrow{p} & \mathfrak{X} \times_{\mathfrak{Z}} \mathfrak{Y} \\ \downarrow f & &
\downarrow q \\ \mathfrak{Z} & \xleftarrow{g} & \mathfrak{Y} \end{array} $$
is commutative. For every coherent $\mathcal{O}_{\mathfrak{X}}$-Module $\mathcal{F}$, one then has a canonical
isomorphism of $\mathcal{O}_{\mathfrak{Y}}$-Modules

$$ u : g^{*}(f_{*}(\mathcal{F})) \cong q_{*}(p^{*}(\mathcal{F})). \tag{10.14.6.1} $$

**Proof.** To define a homomorphism $g^{*}(f_{*}(\mathcal{F})) \to q_{*}(p^{*}(\mathcal{F}))$, one knows that it amounts
to the same to define a homomorphism $f_{*}(\mathcal{F}) \to g_{*}(q_{*}(p^{*}(\mathcal{F}))) =
f_{*}(p_{*}(p^{*}(\mathcal{F})))$ (0, 4.4.3): we shall take $u = f_{*}(\rho)$, where $\rho$ is the canonical
homomorphism $\mathcal{F} \to p_{*}(p^{*}(\mathcal{F}))$ (0, 4.4.3). To see that $u$ is an isomorphism, one reduces at
once to the case where $\mathfrak{Z}$, $\mathfrak{X}$, $\mathfrak{Y}$ are formal spectra of adic Noetherian rings $A$,
$B$, $C$, with the conditions seen above in (10.14.5, (ii)); one then has $f_{*}(\mathcal{F}) = M^{\Delta}$, where $M$
is an $(A/\mathfrak{a})$-module of finite type (10.10.5), and the two members of (10.14.6.1) are identified
respectively, by virtue of (10.10.8), with $(C \otimes_{A} M)^{\Delta}$ and $((C/\mathfrak{a}C) \otimes_{A/\mathfrak{a}}
M)^{\Delta}$, whence the corollary, since $(C/\mathfrak{a}C) \otimes_{A/\mathfrak{a}} M = (C \otimes_{A}
(A/\mathfrak{a})) \otimes_{A/\mathfrak{a}} M$ is canonically identified with $C \otimes_{A} M$.

**Corollary (10.14.7).** Let $X$ be a locally Noetherian ordinary prescheme, $Y$ a closed subprescheme of $X$, $j$ the
canonical injection $Y \to X$, $X'$ a closed part of $X$ and $Y' = Y \cap X'$; then $\widehat{j} : \widehat{Y}_{/Y'} \to
\widehat{X}_{/X'}$ is a closed immersion, and for every coherent $\mathcal{O}_{Y}$-Module $\mathcal{F}$, one has $$
\widehat{j}_{*}(\mathcal{F}_{/Y'}) = (j_{*}(\mathcal{F}))_{/X'}. $$

**Proof.** Since $Y' = j^{-1}(X')$, it suffices to use (10.9.9) and to apply (10.14.5) and (10.14.6).

## 10.15. Separated formal preschemes

<!-- label: I.10.15 -->

**Definition (10.15.1).** Let $\mathfrak{G}$ be a formal prescheme, $\mathfrak{X}$ a $\mathfrak{G}$-formal prescheme, $f
: \mathfrak{X} \to \mathfrak{G}$ the structure morphism. One calls _diagonal morphism_ $\Delta_{f} : \mathfrak{X} \to
\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{X}$ (also denoted $\Delta_{\mathfrak{X}}$) the morphism $(1_{\mathfrak{X}},
1_{\mathfrak{X}})_{\mathfrak{G}}$. One says that $\mathfrak{X}$ is _separated over $\mathfrak{G}$_, or a _$\mathfrak{G}$-formal
scheme_, or that $f$ is a _separated morphism_, if the image under $\Delta_{f}$ of the underlying space $\mathfrak{X}$ is
a closed part of the space underlying $\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{X}$. One says that a formal prescheme
$\mathfrak{X}$ is _separated_, or is a _formal scheme_, if it is separated over $\mathbf{Z}$.

**Proposition (10.15.2).** Suppose that the formal preschemes $\mathfrak{G}$, $\mathfrak{X}$ are respectively inductive
limits of sequences $(S_{n})$, $(X_{n})$ of ordinary preschemes, and that the morphism $f : \mathfrak{X} \to
\mathfrak{G}$ is the inductive limit of a sequence of morphisms $f_{n} : X_{n} \to S_{n}$. For $f$ to be separated, it
is necessary and sufficient that the morphism $f_{0} : X_{0} \to S_{0}$ be.

**Proof.** Indeed, $\Delta_{f}$ is then the inductive limit of the sequence of morphisms $\Delta_{X_{n}/S_{n}}$
(10.7.4), and the image under $\Delta_{\mathfrak{X}/\mathfrak{G}}$ of the underlying space $\mathfrak{X}$ (resp. the
underlying space $\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{X}$) is identical to the image under
$\Delta_{X_{0}/S_{0}}$ of the underlying space $X_{0}$ (resp. to the underlying space $X_{0} \times_{S_{0}} X_{0}$);
whence the conclusion.

**Proposition (10.15.3).** Suppose in what follows that all the formal preschemes (resp. morphisms of formal preschemes)
considered are inductive limits of sequences of ordinary preschemes (resp. of morphisms of ordinary preschemes).

(i) The composite of two separated morphisms is separated.

(ii) If $f : \mathfrak{X} \to \mathfrak{X}'$, $g : \mathfrak{Y} \to \mathfrak{Y}'$ are two separated
$\mathfrak{G}$-morphisms, $f \times_{\mathfrak{G}} g$ is separated.

(iii) If $f : \mathfrak{X} \to \mathfrak{Y}$ is a separated $\mathfrak{G}$-morphism, the $\mathfrak{G}'$-morphism
$f_{(\mathfrak{G}')}$ is separated for every extension $\mathfrak{G}' \to \mathfrak{G}$ of the formal base prescheme.

(iv) If the composite $g \circ f$ of two morphisms is separated, $f$ is separated.

(One understands in this statement that if one and the same formal prescheme $\mathfrak{Z}$ intervenes several times in
one and the same proposition, one considers it as the inductive limit of the same sequence $(Z_{n})$ of ordinary
preschemes everywhere it figures, and the morphisms of $\mathfrak{Z}$ into a formal prescheme (resp. of a formal
prescheme into $\mathfrak{Z}$) as inductive limits of morphisms of the $Z_{n}$ into ordinary preschemes (resp. of
ordinary preschemes into the $Z_{n}$).)

**Proof.** With the notations of (10.15.2), one has indeed $(g \circ f)_{0} = g_{0} \circ f_{0}$, and $(f
\times_{\mathfrak{G}} g)_{0} = f_{0} \times_{\mathfrak{G}_{0}} g_{0}$, and the assertions of (10.15.3) are then
immediate consequences of (10.15.2) and of the corresponding assertions of (5.5.1) for ordinary preschemes.

We leave to the reader the care of stating, for the same kind of formal preschemes and of morphisms as in (10.15.3), the
propositions corresponding to (5.5.5), (5.5.9), and (5.5.10) (replacing therein "affine open" by "formal affine open
verifying condition b) of (10.6.3)").

An analogous reasoning also shows that every Noetherian formal affine scheme is separated, which justifies the
terminology.

**Proposition (10.15.4).** Let $\mathfrak{G}$ be a locally Noetherian formal prescheme, $\mathfrak{X}$, $\mathfrak{Y}$
two locally Noetherian $\mathfrak{G}$-formal preschemes, such that $\mathfrak{X}$ or $\mathfrak{Y}$ is of finite type
over $\mathfrak{G}$ (so that $\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{Y}$ is locally Noetherian) and that
$\mathfrak{Y}$ is separated over $\mathfrak{G}$. Let $f : \mathfrak{X} \to \mathfrak{Y}$ be a $\mathfrak{G}$-morphism;
then the graph morphism $\Gamma_{f} = (1_{\mathfrak{X}}, f)_{\mathfrak{G}} : \mathfrak{X} \to \mathfrak{X}
\times_{\mathfrak{G}} \mathfrak{Y}$ is a closed immersion.

**Proof.** One may suppose that $\mathfrak{G}$ is the inductive limit of a sequence $(S_{n})$ of locally Noetherian
preschemes, $\mathfrak{X}$ (resp. $\mathfrak{Y}$) the inductive limit of a sequence $(X_{n})$ (resp. $(Y_{n})$) of
$S_{n}$-preschemes, $f$ the inductive limit of a sequence of $S_{n}$-morphisms $f_{n} : X_{n} \to Y_{n}$; then
$\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{Y}$ is the inductive limit of the sequence $(X_{n} \times_{S_{n}} Y_{n})$
and $\Gamma_{f}$ of the sequence $(\Gamma_{f_{n}})$ (10.7.4); by hypothesis, $Y_{0}$ is separated over $S_{0}$
(10.15.2), hence the space $\Gamma_{f_{0}}(X_{0})$ is a closed subspace of $X_{0} \times_{S_{0}} Y_{0}$; since the
underlying spaces of $\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{Y}$ (resp. $\Gamma_{f}(\mathfrak{X})$) and $X_{0}
\times_{S_{0}} Y_{0}$ (resp. $\Gamma_{f_{0}}(X_{0})$) are the same, one sees already that $\Gamma_{f}(\mathfrak{X})$ is
a closed subspace of $\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{Y}$. Let us now remark that when $(U, V)$ runs
through the set of pairs formed of a Noetherian formal affine open $U$ (resp. $V$) of $\mathfrak{X}$ (resp.
$\mathfrak{Y}$) such that $f(U) \subset V$, the opens $U \times_{\mathfrak{G}} V$ form a covering of
$\Gamma_{f}(\mathfrak{X})$ in $\mathfrak{X} \times_{\mathfrak{G}} \mathfrak{Y}$, and if $f_{U} : U \to V$ is the
restriction of $f$ to $U$, $\Gamma_{f_{U}} : U \to U \times_{\mathfrak{G}} V$ is the restriction of $\Gamma_{f}$ to $U$.
If we show that $\Gamma_{f_{U}}$ is a closed immersion, it will be so also for $\Gamma_{f}$ (10.14.4); in other words,
one is reduced to the case where $\mathfrak{G} = \operatorname{Spf}(A)$, $\mathfrak{X} = \operatorname{Spf}(B)$,
$\mathfrak{Y} = \operatorname{Spf}(C)$ are affine ($A$, $B$, $C$ adic Noetherian), $f$ corresponding to a continuous
$A$-homomorphism $\varphi : C \to B$; $\Gamma_{f}$ then corresponds to the unique continuous homomorphism $\omega : B
\widehat{\otimes}_{A} C \to B$ which, composed with the canonical homomorphisms $B \to B \widehat{\otimes}_{A} C$ and $C
\to B \widehat{\otimes}_{A} C$, gives respectively the identity and $\varphi$. Now, it is clear that $\omega$ is
surjective, whence our assertion.

**Corollary (10.15.5).** Let $\mathfrak{G}$ be a locally Noetherian formal prescheme, $\mathfrak{X}$ a
$\mathfrak{G}$-prescheme of finite type; for $\mathfrak{X}$ to be separated over $\mathfrak{G}$, it is necessary and
sufficient that the diagonal morphism $\mathfrak{X} \to \mathfrak{X} \times_{\mathfrak{G}} \mathfrak{X}$ be a closed
immersion.

**Proposition (10.15.6).** A closed immersion $j : \mathfrak{Y} \to \mathfrak{X}$ of locally Noetherian formal
preschemes is a separated morphism.

**Proof.** With the notations of (10.14.2), $j_{0} : Y_{0} \to X_{0}$ is a closed immersion, hence a separated morphism,
and it suffices to apply (10.15.2).

**Proposition (10.15.7).** Let $X$ be a locally Noetherian (ordinary) prescheme, $X'$ a closed part of $X$ and
$\widehat{X} = \widehat{X}_{/X'}$. For $\widehat{X}$ to be separated, it is necessary and sufficient that
$X'_{\mathrm{red}}$ be, and it is sufficient that $X$ be.

**Proof.** Indeed, with the notations of (10.8.5), for $\widehat{X}$ to be separated, it is necessary and sufficient
that $X_{0}$ be (10.15.2), and since $\widehat{X}_{\mathrm{red}} = (X_{0})_{\mathrm{red}}$, it is equivalent to say that
$X'_{\mathrm{red}}$ is (5.5.1, (vi)).

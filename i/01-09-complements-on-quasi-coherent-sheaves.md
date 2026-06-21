# §9. Complements on Quasi-coherent Sheaves

<!-- label: I.9 -->

## 9.1. Tensor product of quasi-coherent sheaves

<!-- label: I.9.1 -->

**Proposition (9.1.1).** Let $X$ be a prescheme (resp. a locally Noetherian prescheme). Let $\mathcal{F}$ and
$\mathcal{G}$ be two quasi-coherent (resp. coherent) $\mathcal{O}_{X}$-Modules; then $\mathcal{F}
\otimes_{\mathcal{O}_{X}} \mathcal{G}$ is quasi-coherent (resp. coherent), and of finite type if $\mathcal{F}$ and
$\mathcal{G}$ are of finite type. If $\mathcal{F}$ admits a finite presentation and if $\mathcal{G}$ is quasi-coherent
(resp. coherent), then $\mathcal{H}om_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})$ is quasi-coherent (resp. coherent).

**Proof.** The question being local, one may suppose $X$ affine (resp. affine Noetherian); moreover, if $\mathcal{F}$ is
coherent, one may suppose that it is the cokernel of a homomorphism $\mathcal{O}_{X}^{m} \to \mathcal{O}_{X}^{n}$. The
assertions concerning quasi-coherent sheaves then follow from (1.3.12) and (1.3.9); the assertions concerning coherent
sheaves follow from (1.5.1) and from the fact that, if $M$ and $N$ are modules of finite type over a Noetherian ring
$A$, then $M \otimes_{A} N$ and $\operatorname{Hom}_{A}(M, N)$ are $A$-modules of finite type.

**Definition (9.1.2).** Let $X$, $Y$ be two $S$-preschemes, $p$, $q$ the projections of $X \times_{S} Y$, and
$\mathcal{F}$ (resp. $\mathcal{G}$) a quasi-coherent $\mathcal{O}_{X}$-Module (resp. $\mathcal{O}_{Y}$-Module). One
calls _tensor product of $\mathcal{F}$ and $\mathcal{G}$ over $\mathcal{O}_{S}$_ (or over $S$), and one denotes by
$\mathcal{F} \otimes_{\mathcal{O}_{S}} \mathcal{G}$ (or $\mathcal{F} \otimes_{S} \mathcal{G}$), the tensor product
$p^{*}(\mathcal{F}) \otimes_{\mathcal{O}_{X \times_{S} Y}} q^{*}(\mathcal{G})$ on the prescheme $X \times_{S} Y$.

If $X_{i}$ ($1 \leqslant i \leqslant n$) are $S$-preschemes and $\mathcal{F}_{i}$ a quasi-coherent
$\mathcal{O}_{X_{i}}$-Module ($1 \leqslant i \leqslant n$), one defines in the same way the tensor product
$\mathcal{F}_{1} \otimes_{S} \mathcal{F}_{2} \otimes_{S} \dots \otimes_{S} \mathcal{F}_{n}$ on the prescheme $Z = X_{1}
\times_{S} X_{2} \times_{S} \dots \times_{S} X_{n}$; it is a quasi-coherent $\mathcal{O}_{Z}$-Module by virtue of
(9.1.1) and (0, 5.1.4); it is coherent if the $\mathcal{F}_{i}$ are and if $Z$ is locally Noetherian, by virtue of
(9.1.1), (0, 5.3.11), and (6.1.1).

It will be noted that if one takes $X = Y = S$, the definition (9.1.2) gives back the tensor product of
$\mathcal{O}_{S}$-Modules. Moreover, since $q^{*}(\mathcal{O}_{Y}) = \mathcal{O}_{X \times_{S} Y}$ (0, 4.3.4), the
product $\mathcal{F} \otimes_{S} \mathcal{O}_{Y}$ is canonically identified with $p^{*}(\mathcal{F})$, and likewise
$\mathcal{O}_{X} \otimes_{S} \mathcal{G}$ is canonically identified with $q^{*}(\mathcal{G})$. More particularly, if one
takes $Y = S$ and one denotes by $f$ the structural morphism $X \to Y$, one has $\mathcal{O}_{X} \otimes_{Y} \mathcal{G}
= f^{*}(\mathcal{G})$: the ordinary tensor product and the inverse image thus appear as particular cases of the general
tensor product.

The definition (9.1.2) entails immediately that, for $X$ and $Y$ fixed, $\mathcal{F} \otimes_{S} \mathcal{G}$ is a
covariant additive bifunctor, right exact in $\mathcal{F}$ and $\mathcal{G}$.

**Proposition (9.1.3).** Let $S$, $X$, $Y$ be three affine schemes of rings $A$, $B$, $C$ respectively, $B$ and $C$
being $A$-algebras. Let $M$ (resp. $N$) be a $B$-module (resp. $C$-module), and $\mathcal{F} = \widetilde{M}$ (resp.
$\mathcal{G} = \widetilde{N}$) the associated quasi-coherent sheaf; then $\mathcal{F} \otimes_{S} \mathcal{G}$ is
canonically isomorphic to the sheaf associated to the $(B \otimes_{A} C)$-module $M \otimes_{A} N$.

**Proof.** Indeed, by virtue of (1.6.5), $\mathcal{F} \otimes_{S} \mathcal{G}$ is canonically isomorphic to the sheaf
associated to the $(B \otimes_{A} C)$-module $$ (M \otimes_{B} (B \otimes_{A} C)) \otimes_{B \otimes_{A} C} ((B
\otimes_{A} C) \otimes_{C} N) $$ and, by reason of the canonical isomorphisms between tensor products, this last is
isomorphic to $M \otimes_{B} (B \otimes_{A} C) \otimes_{C} N = (M \otimes_{B} B) \otimes_{A} (C \otimes_{C} N) = M
\otimes_{A} N$.

**Proposition (9.1.4).** Let $f : T \to X$, $g : T \to Y$ be two $S$-morphisms, and $\mathcal{F}$ (resp. $\mathcal{G}$)
a quasi-coherent $\mathcal{O}_{X}$-Module (resp. $\mathcal{O}_{Y}$-Module). One then has $(f, g)_{S}^{*}(\mathcal{F}
\otimes_{S} \mathcal{G}) = f^{*}(\mathcal{F}) \otimes_{\mathcal{O}_{T}} g^{*}(\mathcal{G})$.

**Proof.** If $p$, $q$ are the projections of $X \times_{S} Y$, the formula results in fact from the relations $(f,
g)_{S}^{*} \circ p^{*} = f^{*}$ and $(f, g)_{S}^{*} \circ q^{*} = g^{*}$ (0, 3.5.5), and from the fact that an inverse
image of a tensor product of algebraic sheaves is the tensor product of their inverse images (0, 4.3.3).

**Corollary (9.1.5).** Let $f : X \to X'$, $g : Y \to Y'$ be two $S$-morphisms, and $\mathcal{F}'$ (resp.
$\mathcal{G}'$) a quasi-coherent $\mathcal{O}_{X'}$-Module (resp. $\mathcal{O}_{Y'}$-Module). One then has $$ (f
\times_{S} g)^{*}(\mathcal{F}' \otimes_{S} \mathcal{G}') = f^{*}(\mathcal{F}') \otimes_{S} g^{*}(\mathcal{G}'). $$

**Proof.** This results from (9.1.4) and from the fact that $f \times_{S} g = (f \circ p, g \circ q)_{S}$, $p$ and $q$
being the projections of $X \times_{S} Y$.

**Corollary (9.1.6).** Let $X$, $Y$, $Z$ be three $S$-preschemes, and $\mathcal{F}$ (resp. $\mathcal{G}$, $\mathcal{H}$)
a quasi-coherent $\mathcal{O}_{X}$-Module (resp. $\mathcal{O}_{Y}$-Module, $\mathcal{O}_{Z}$-Module); the sheaf
$\mathcal{F} \otimes_{S} \mathcal{G} \otimes_{S} \mathcal{H}$ is the inverse image of $(\mathcal{F} \otimes_{S}
\mathcal{G}) \otimes_{S} \mathcal{H}$ under the canonical isomorphism of $X \times_{S} Y \times_{S} Z$ onto $(X
\times_{S} Y) \times_{S} Z$.

**Proof.** Indeed, this isomorphism is written $(p_{1}, p_{2})_{S} \times_{S} p_{3}$, denoting by $p_{1}$, $p_{2}$,
$p_{3}$ the projections of $X \times_{S} Y \times_{S} Z$.

Likewise, the inverse image of $\mathcal{G} \otimes_{S} \mathcal{F}$ under the canonical isomorphism of $X \times_{S} Y$
onto $Y \times_{S} X$ is $\mathcal{F} \otimes_{S} \mathcal{G}$.

**Corollary (9.1.7).** If $X$ is an $S$-prescheme, every quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ is the
inverse image of $\mathcal{F} \otimes_{S} \mathcal{O}_{S}$ under the canonical isomorphism of $X$ onto $X \times_{S} S$
(3.3.3).

**Proof.** Indeed, this isomorphism is $(1_{X}, \varphi)_{S}$, where $\varphi$ is the structural morphism $X \to S$, and
the corollary results from (9.1.4) and from the fact that $\varphi^{*}(\mathcal{O}_{S}) = \mathcal{O}_{X}$.

**(9.1.8)** Let $X$ be an $S$-prescheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{X}$-Module, and $\varphi : S' \to
S$ a morphism; one denotes by $\mathcal{F}_{(\varphi)}$ or $\mathcal{F}_{(S')}$ the quasi-coherent sheaf $\mathcal{F}
\otimes_{S} \mathcal{O}_{S'}$ on $X \times_{S} S' = X_{(\varphi)} = X_{(S')}$; thus $\mathcal{F}_{(S')} =
p^{*}(\mathcal{F})$, where $p$ is the projection $X_{(S')} \to X$.

**Proposition (9.1.9).** Let $\varphi' : S'' \to S'$ be a morphism. For every quasi-coherent $\mathcal{O}_{X}$-Module
$\mathcal{F}$ on the $S$-prescheme $X$, $(\mathcal{F}_{(\varphi)})_{(\varphi')}$ is the inverse image of
$\mathcal{F}_{(\varphi \circ \varphi')}$ under the canonical isomorphism $(X_{(\varphi)})_{(\varphi')}
\xrightarrow{\sim} X_{(\varphi \circ \varphi')}$ (3.3.9).

**Proof.** This results at once from the definitions and from (3.3.9), and is also written $$ (9.1.9.1) \qquad
(\mathcal{F} \otimes_{S} \mathcal{O}_{S'}) \otimes_{S'} \mathcal{O}_{S''} = \mathcal{F} \otimes_{S} \mathcal{O}_{S''}.
$$

**Proposition (9.1.10).** Let $Y$ be an $S$-prescheme, $f : X \to Y$ an $S$-morphism. For every quasi-coherent
$\mathcal{O}_{Y}$-Module $\mathcal{G}$ and every morphism $S' \to S$, one has $(f_{(S')})^{*}(\mathcal{G}_{(S')}) =
(f^{*}(\mathcal{G}))_{(S')}$.

**Proof.** This results at once from the commutativity of the diagram
$$
\begin{array}{ccc}
X_{(S')} & \xrightarrow{\ f_{(S')}\ } & Y_{(S')} \\
\downarrow & & \downarrow \\
X & \xrightarrow{\ \ f\ \ } & Y
\end{array}
$$

**Corollary (9.1.11).** Let $X$, $Y$ be two $S$-preschemes, and $\mathcal{F}$ (resp. $\mathcal{G}$) a quasi-coherent
$\mathcal{O}_{X}$-Module (resp. $\mathcal{O}_{Y}$-Module). The inverse image of the sheaf $\mathcal{F}_{(S')}
\otimes_{S'} \mathcal{G}_{(S')}$ under the canonical isomorphism $(X \times_{S} Y)_{(S')} \xrightarrow{\sim} (X_{(S')})
\times_{S'} (Y_{(S')})$ (3.3.10) is equal to $(\mathcal{F} \otimes_{S} \mathcal{G})_{(S')}$.

**Proof.** If $p$, $q$ are the projections of $X \times_{S} Y$, the isomorphism in question is none other than
$(p_{(S')}, q_{(S')})_{S'}$; the corollary results from the propositions (9.1.4) and (9.1.10).

**Proposition (9.1.12).** With the notations of (9.1.2), let $z$ be a point of $X \times_{S} Y$, $x = p(z)$, $y = q(z)$;
the stalk $(\mathcal{F} \otimes_{S} \mathcal{G})_{z}$ is isomorphic to $(\mathcal{F}_{x} \otimes_{\mathcal{O}_{x}}
\mathcal{O}_{z}) \otimes_{\mathcal{O}_{z}} (\mathcal{G}_{y} \otimes_{\mathcal{O}_{y}} \mathcal{O}_{z}) = \mathcal{F}_{x}
\otimes_{\mathcal{O}_{x}} \mathcal{O}_{z} \otimes_{\mathcal{O}_{y}} \mathcal{G}_{y}$.

**Proof.** Since one may reduce to the affine case, the proposition results from the formula (1.6.5.1).

**Corollary (9.1.13).** If $\mathcal{F}$ and $\mathcal{G}$ are of finite type, one has $$
\operatorname{Supp}(\mathcal{F} \otimes_{S} \mathcal{G}) = p^{-1}(\operatorname{Supp}(\mathcal{F})) \cap
q^{-1}(\operatorname{Supp}(\mathcal{G})). $$

**Proof.** Since $p^{*}(\mathcal{F})$ and $q^{*}(\mathcal{G})$ are of finite type over $\mathcal{O}_{X \times_{S} Y}$,
one is reduced, by (9.1.12) and (0, 1.7.5), to the particular case where $\mathcal{G} = \mathcal{O}_{Y}$, that is, to
proving the formula $$ (9.1.13.1) \qquad \operatorname{Supp}(p^{*}(\mathcal{F})) =
p^{-1}(\operatorname{Supp}(\mathcal{F})). $$ The same reasoning as in (0, 1.7.5) reduces this to verifying that one has,
for every $z \in X \times_{S} Y$, $\mathcal{O}_{z}/\mathfrak{m}_{x}\mathcal{O}_{z} \neq 0$ (with $x = p(z)$), which
follows from the fact that the homomorphism $\mathcal{O}_{x} \to \mathcal{O}_{z}$ is local by hypothesis.

We leave to the reader the task of extending to a product of an arbitrary number of factors the results proved in this
number for two factors.

## 9.2. Direct image of a quasi-coherent sheaf

<!-- label: I.9.2 -->

**Proposition (9.2.1).** Let $f : X \to Y$ be a morphism of preschemes. Suppose that there exists a covering
$(Y_{\alpha})$ of $Y$ by affine opens having the following property: each of the $f^{-1}(Y_{\alpha})$ admits a finite
covering $(X_{\alpha i})$ by affine opens contained in $f^{-1}(Y_{\alpha})$, such that each of the intersections
$X_{\alpha i} \cap X_{\alpha j}$ is itself a finite union of affine opens. Under these conditions, for every
quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$, $f_{*}(\mathcal{F})$ is a quasi-coherent
$\mathcal{O}_{Y}$-Module.

**Proof.** The question being local on $Y$, one may suppose $Y$ equal to one of the $Y_{\alpha}$, and thus suppress the
indices $\alpha$.

a) Suppose first that the $X_{i} \cap X_{j}$ are themselves affine opens. Put $\mathcal{F}_{i} = \mathcal{F}|X_{i}$,
$\mathcal{F}_{ij} = \mathcal{F}|(X_{i} \cap X_{j})$, and let $\mathcal{F}'_{i}$ and $\mathcal{F}'_{ij}$ be the images of
$\mathcal{F}_{i}$ and $\mathcal{F}_{ij}$ respectively under the restrictions of $f$ to $X_{i}$ and $X_{i} \cap X_{j}$;
one knows that the $\mathcal{F}'_{i}$ and $\mathcal{F}'_{ij}$ are quasi-coherent (1.6.3). Put $\mathcal{G} =
\bigoplus_{i} \mathcal{F}'_{i}$, $\mathcal{H} = \bigoplus_{i,j} \mathcal{F}'_{ij}$; $\mathcal{G}$ and $\mathcal{H}$ are
quasi-coherent $\mathcal{O}_{Y}$-Modules; we are going to define a homomorphism $u : \mathcal{G} \to \mathcal{H}$ such
that $f_{*}(\mathcal{F})$ is the kernel of $u$; it will result that $f_{*}(\mathcal{F})$ is quasi-coherent (1.3.9). It
suffices to define $u$ as a homomorphism of presheaves; taking account of the definitions of $\mathcal{G}$ and
$\mathcal{H}$, it therefore suffices, for every open set $W \subset Y$, to define a homomorphism $$ u_{W} :
\bigoplus_{i} \Gamma(f^{-1}(W) \cap X_{i}, \mathcal{F}) \to \bigoplus_{i,j} \Gamma(f^{-1}(W) \cap X_{i} \cap X_{j},
\mathcal{F}) $$ so as to satisfy the usual compatibility conditions as $W$ varies. If, for every section $s_{i} \in
\Gamma(f^{-1}(W) \cap X_{i}, \mathcal{F})$, one denotes by $s_{i|j}$ its restriction to $f^{-1}(W) \cap X_{i} \cap
X_{j}$, one will put $$ u_{W}((s_{i})) = (s_{i|j} - s_{j|i}) $$ and the compatibility conditions are evidently
fulfilled. To prove that the kernel $\mathcal{R}$ of $u$ is $f_{*}(\mathcal{F})$, let us define a homomorphism of
$f_{*}(\mathcal{F})$ into $\mathcal{R}$ by making correspond to every section $s \in \Gamma(f^{-1}(W), \mathcal{F})$ the
family $(s_{i})$, where $s_{i}$ is the restriction of $s$ to $f^{-1}(W) \cap X_{i}$; the axioms $(F1)$ and $(F2)$ of
sheaves (G, II, 1.1) entail that this homomorphism is bijective, which completes the demonstration in this case.

b) In the general case, the same reasoning applies once one has established that the $\mathcal{F}_{ij}$ are
quasi-coherent. Now, by hypothesis, $X_{i} \cap X_{j}$ is a finite union of affine opens $X_{ijk}$; and since the
$X_{ijk}$ are affine opens in a scheme, the intersection of any two of them is again an affine open (5.5.6). One is thus
reduced to the first case, and (9.2.1) is therefore proved.

**Corollary (9.2.2).** The conclusion of (9.2.1) holds in each of the following cases:

a) $f$ is separated and quasi-compact.

b) $f$ is separated and of finite type.

c) $f$ is quasi-compact and the space underlying $X$ is locally Noetherian.

**Proof.** In case a), the $X_{i} \cap X_{j}$ are affine (5.5.6). Case b) is a particular case of a) (6.6.3). Finally,
in case c), one may reduce to the case where $Y$ is affine and the space underlying $X$ is Noetherian; then $X$ admits a
finite affine open covering $(X_{i})$, and the $X_{i} \cap X_{j}$, being quasi-compact, are finite unions of affine
opens (2.1.3).

## 9.3. Extension of sections of quasi-coherent sheaves

<!-- label: I.9.3 -->

**Theorem (9.3.1).** Let $X$ be a prescheme whose underlying space is Noetherian, or a scheme whose underlying space is
quasi-compact. Let $\mathcal{L}$ be an invertible $\mathcal{O}_{X}$-Module (0, 5.4.1), $f$ a section of $\mathcal{L}$
over $X$, $X_{f}$ the open set of those $x \in X$ where $f(x) \neq 0$ (0, 5.5.1), and $\mathcal{F}$ a quasi-coherent
$\mathcal{O}_{X}$-Module.

(i) If $s \in \Gamma(X, \mathcal{F})$ is such that $s|X_{f} = 0$, there exists an integer $n > 0$ such that $s \otimes
f^{\otimes n} = 0$.

(ii) For every section $s \in \Gamma(X_{f}, \mathcal{F})$, there exists an integer $n > 0$ such that $s \otimes
f^{\otimes n}$ extends to a section of $\mathcal{F} \otimes \mathcal{L}^{\otimes n}$ over $X$.

**Proof.** (i) Since the space underlying $X$ is quasi-compact, hence a finite union of affine opens $U_{i}$ such that
$\mathcal{L}|U_{i}$ is isomorphic to $\mathcal{O}_{X}|U_{i}$, one is reduced to the case where $X$ is affine and
$\mathcal{L} = \mathcal{O}_{X}$. In this case, $f$ is identified with an element of $A(X)$ and one has $X_{f} = D(f)$;
$s$ is identified with an element of an $A(X)$-module $M$, and $s|X_{f}$ with the corresponding element of $M_{f}$, and
the result is trivial, taking account of the definition of a module of fractions.

(ii) Again $X$ is a finite union of affine opens $U_{i}$ ($1 \leqslant i \leqslant r$) such that $\mathcal{L}|U_{i} \cong \mathcal{O}_{X}|U_{i}$, and for each $i$, $(s \otimes f^{\otimes n})|(U_{i} \cap X_{f})$ is identified, by the preceding isomorphism, with $(f|(U_{i} \cap X_{f}))^{n}(s|(U_{i} \cap X_{f}))$. One then knows (1.4.1) that there exists an integer $n > 0$ such that for each $i$, $(s \otimes f^{\otimes n})|(U_{i} \cap X_{f})$ extends to a section $s_{i}$ of $\mathcal{F} \otimes \mathcal{L}^{\otimes n}$ over $U_{i}$. Let $s_{i|j}$ be the restriction of $s_{i}$ to $U_{i} \cap U_{j}$; one has by definition $s_{i|j} - s_{j|i} = 0$ in $X_{f} \cap U_{i} \cap U_{j}$. Now, if $X$ is a Noetherian space, $U_{i} \cap U_{j}$ is quasi-compact; if $X$ is a scheme, $U_{i} \cap U_{j}$ is an affine open (5.5.6), hence again quasi-compact. By virtue of (i), there thus exists an integer $m$ (independent of $i$ and $j$) such that $(s_{i|j} - s_{j|i}) \otimes f^{\otimes m} = 0$. One concludes at once that there exists a section $s'$ of $\mathcal{F} \otimes \mathcal{L}^{\otimes (n+m)}$ over $X$, inducing $s_{i} \otimes f^{\otimes m}$ over each $U_{i}$, and inducing consequently $s \otimes f^{\otimes (n+m)}$ over $X_{f}$.

The corollaries that follow give an interpretation of the theorem (9.3.1) in a more algebraic language:

**Corollary (9.3.2).** The hypotheses being those of (9.3.1), consider the graded ring $A_{*} = \Gamma_{*}(\mathcal{L})$
and the graded $A_{*}$-module $M_{*} = \Gamma_{*}(\mathcal{L}, \mathcal{F})$ (0, 5.4.6). If $f \in A_{n}$, where $n \in
\mathbf{Z}$, then one has a canonical isomorphism $\Gamma(X_{f}, \mathcal{F}) \xrightarrow{\sim} ((M_{*})_{f})_{0}$ (the
subgroup of the module of fractions $(M_{*})_{f}$ formed of the elements of degree $0$).

**Corollary (9.3.3).** Suppose the hypotheses of (9.3.1) verified, and suppose in addition that $\mathcal{L} =
\mathcal{O}_{X}$. Then if one puts $A = \Gamma(X, \mathcal{O}_{X})$, $M = \Gamma(X, \mathcal{F})$, the $A_{f}$-module
$\Gamma(X_{f}, \mathcal{F})$ is canonically isomorphic to $M_{f}$.

**Proposition (9.3.4).** Let $X$ be a Noetherian prescheme, $\mathcal{F}$ a coherent $\mathcal{O}_{X}$-Module, and
$\mathcal{J}$ a coherent sheaf of ideals in $\mathcal{O}_{X}$, such that the support of $\mathcal{F}$ is contained in
that of $\mathcal{O}_{X}/\mathcal{J}$. Then there exists an integer $n > 0$ such that $\mathcal{J}^{n}\mathcal{F} = 0$.

**Proof.** Since $X$ is a finite union of affine opens whose rings are Noetherian, one may suppose $X$ affine with
Noetherian ring $A$; then $\mathcal{F} = \widetilde{M}$, where $M = \Gamma(X, \mathcal{F})$ is an $A$-module of finite
type, and $\mathcal{J} = \widetilde{\mathfrak{J}}$, where $\mathfrak{J} = \Gamma(X, \mathcal{J})$ is an ideal of $A$
(1.4.1 and 1.5.1). Since $A$ is Noetherian, $\mathfrak{J}$ admits a finite system of generators $f_{i}$ ($1 \leqslant i
\leqslant m$). By hypothesis, every section of $\mathcal{F}$ over $X$ is null in each of the $D(f_{i})$; if $s_{j}$ ($1
\leqslant j \leqslant q$) are sections of $\mathcal{F}$ generating $M$, there thus exists an integer $h$ independent of
$i$ and $j$ such that $f_{i}^{h} s_{j} = 0$ (1.4.1), hence $f_{i}^{h} s = 0$ for every $s \in M$. One concludes that if
$n = mh$, one has $\mathfrak{J}^{n}M = 0$, and consequently the corresponding $\mathcal{O}_{X}$-Module
$\mathcal{J}^{n}\mathcal{F} = (\mathfrak{J}^{n}M)^{\sim}$ (1.3.13) is null.

**Corollary (9.3.5).** Under the hypotheses of (9.3.4), there exists a closed subprescheme $Y$ of $X$, whose underlying
space is the support of $\mathcal{O}_{X}/\mathcal{J}$, and such that, if $j : Y \to X$ is the canonical injection, one
has $\mathcal{F} = j_{*}(j^{*}(\mathcal{F}))$.

**Proof.** Let us first remark that the supports of $\mathcal{O}_{X}/\mathcal{J}$ and of
$\mathcal{O}_{X}/\mathcal{J}^{n}$ are the same, for if $\mathcal{J}_{x} = \mathcal{O}_{x}$, one also has
$\mathcal{J}_{x}^{n} = \mathcal{O}_{x}$, and one has on the other hand $\mathcal{J}_{x}^{n} \subset \mathcal{J}_{x}$ for
every $x \in X$. One may therefore, by virtue of (9.3.4), suppose that $\mathcal{J}\mathcal{F} = 0$; one then takes for
$Y$ the closed subprescheme of $X$ defined by $\mathcal{J}$, and since $\mathcal{F}$ is then an
$(\mathcal{O}_{X}/\mathcal{J})$-Module, the conclusion is immediate.

## 9.4. Extension of quasi-coherent sheaves

<!-- label: I.9.4 -->

**(9.4.1)** Let $X$ be a topological space, $\mathcal{F}$ a sheaf of sets (resp. of groups, of rings) on $X$, $U$ an
open part of $X$, $\psi : U \to X$ the canonical injection, and $\mathcal{G}$ a subsheaf of $\mathcal{F}|U =
\psi^{*}(\mathcal{F})$. Since $\psi_{*}$ is left exact, $\psi_{*}(\mathcal{G})$ is a subsheaf of
$\psi_{*}(\psi^{*}(\mathcal{F}))$; if one considers the canonical homomorphism $\rho : \mathcal{F} \to
\psi_{*}(\psi^{*}(\mathcal{F}))$ (0, 3.5.3), we shall denote by $\overline{\mathcal{G}}$ the subsheaf
$\rho^{-1}(\psi_{*}(\mathcal{G}))$ of $\mathcal{F}$. It results immediately from the definitions that for every open $V$
of $X$, $\Gamma(V, \overline{\mathcal{G}})$ is formed of the sections $s \in \Gamma(V, \mathcal{F})$ whose restriction
to $V \cap U$ is a section of $\mathcal{G}$ over $V \cap U$. One thus has $\overline{\mathcal{G}}|U =
\psi^{*}(\overline{\mathcal{G}}) = \mathcal{G}$, and $\overline{\mathcal{G}}$ is the largest subsheaf of $\mathcal{F}$
inducing $\mathcal{G}$ on $U$; we shall say that $\overline{\mathcal{G}}$ is the _canonical extension of the subsheaf
$\mathcal{G}$ of $\mathcal{F}|U$ to a subsheaf of $\mathcal{F}$_.

**Proposition (9.4.2).** Let $X$ be a prescheme, $U$ an open part of $X$ such that the canonical injection $j : U \to X$
is a quasi-compact morphism (which will be verified for every $U$ if the underlying space $X$ is locally Noetherian
(6.6.4, (i))). Then:

(i) For every quasi-coherent $(\mathcal{O}_{X}|U)$-Module $\mathcal{F}$, $j_{*}(\mathcal{F})$ is a quasi-coherent
$\mathcal{O}_{X}$-Module and one has $(j_{*}(\mathcal{F}))|U = j^{*}(j_{*}(\mathcal{F})) = \mathcal{F}$.

(ii) For every quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ and every quasi-coherent
sub-$(\mathcal{O}_{X}|U)$-Module $\mathcal{G}$, the canonical extension $\overline{\mathcal{G}}$ of $\mathcal{G}$
(9.4.1) is a quasi-coherent sub-$\mathcal{O}_{X}$-Module of $\mathcal{F}$.

**Proof.** If $j = (\psi, \theta)$ ($\psi$ being the injection $U \to X$ of the underlying spaces), one has by
definition $j_{*}(\mathcal{F}) = \psi_{*}(\mathcal{F})$ for every $(\mathcal{O}_{X}|U)$-Module $\mathcal{F}$, and
moreover $j^{*}(\mathcal{H}) = \psi^{*}(\mathcal{H}) = \mathcal{H}|U$ for every $\mathcal{O}_{X}$-Module $\mathcal{H}$,
by reason of the definition of a prescheme induced on an open. (i) is therefore a particular case of (9.2.2, a)); for
the same reason, $j_{*}(j^{*}(\mathcal{F}))$ is quasi-coherent, and since $\overline{\mathcal{G}}$ is the inverse image
of $j_{*}(\mathcal{G})$ under the homomorphism $\rho : \mathcal{F} \to j_{*}(j^{*}(\mathcal{F}))$, (ii) results from
(4.1.1).

It will be noted that the hypothesis that the morphism $j : U \to X$ is quasi-compact is also verified when the open $U$
is quasi-compact and $X$ a scheme: indeed, $U$ is then a finite union of affine opens $U_{i}$, and for every affine open
$V$ of $X$, $V \cap U_{i}$ is an affine open (5.5.6), hence quasi-compact.

**Corollary (9.4.3).** Let $X$ be a prescheme, $U$ a quasi-compact open of $X$ such that the injection morphism $j : U
\to X$ is quasi-compact. Suppose in addition that every quasi-coherent $\mathcal{O}_{X}$-Module is the inductive limit
of its quasi-coherent sub-$\mathcal{O}_{X}$-Modules of finite type (which holds when $X$ is an affine scheme). Let then
$\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-Module and $\mathcal{G}$ a quasi-coherent
sub-$(\mathcal{O}_{X}|U)$-Module of finite type of $\mathcal{F}|U$. There then exists a quasi-coherent
sub-$\mathcal{O}_{X}$-Module of finite type $\mathcal{G}'$ of $\mathcal{F}$ such that $\mathcal{G}'|U = \mathcal{G}$.

**Proof.** Indeed, one has $\mathcal{F}|U = \overline{\mathcal{F}}|U$, and $\overline{\mathcal{F}}$ is quasi-coherent by
(9.4.2), hence the inductive limit of its quasi-coherent sub-$\mathcal{O}_{X}$-Modules of finite type
$\mathcal{H}_{\lambda}$. Consequently $\mathcal{G}$ is the inductive limit of the $\mathcal{H}_{\lambda}|U$, hence equal
to one of the $\mathcal{H}_{\lambda}|U$ since it is of finite type (0, 5.2.3).

**Remark (9.4.4).** Suppose that for every affine open $U \subset X$ the injection morphism $U \to X$ is quasi-compact.
Then if the conclusion of (9.4.3) holds for every affine open $U$ and every quasi-coherent
sub-$(\mathcal{O}_{X}|U)$-Module of finite type $\mathcal{G}$ of $\mathcal{F}|U$, it results that $\mathcal{F}$ is the
inductive limit of its quasi-coherent sub-$\mathcal{O}_{X}$-Modules of finite type. Indeed, for every affine open $U
\subset X$, one has $\mathcal{F}|U = \widetilde{M}$, where $M$ is an $A(U)$-module, and since the latter is the
inductive limit of its submodules of finite type, $\mathcal{F}|U$ is the inductive limit of its quasi-coherent
sub-$(\mathcal{O}_{X}|U)$-Modules of finite type (1.3.9). Now, by hypothesis, each of these sub-Modules is induced on
$U$ by a quasi-coherent sub-$\mathcal{O}_{X}$-Module of finite type $\mathcal{G}_{\lambda, U}$ of $\mathcal{F}$. The
finite sums of the $\mathcal{G}_{\lambda, U}$ are again quasi-coherent $\mathcal{O}_{X}$-Modules of finite type, for the
question is local and the case where $X$ is affine has been treated in (1.3.10); it is clear then that $\mathcal{F}$ is
the inductive limit of these finite sums, whence our assertion.

**Corollary (9.4.5).** Under the hypotheses of (9.4.3), for every quasi-coherent $(\mathcal{O}_{X}|U)$-Module of finite
type $\mathcal{G}$, there exists a quasi-coherent $\mathcal{O}_{X}$-Module of finite type $\mathcal{G}'$ such that
$\mathcal{G}'|U = \mathcal{G}$.

**Proof.** Since $\mathcal{F} = j_{*}(\mathcal{G})$ is quasi-coherent (9.4.2) and $\mathcal{F}|U = \mathcal{G}$, it
suffices to apply (9.4.3) to $\mathcal{F}$.

**Lemma (9.4.6).** Let $X$ be a prescheme, $L$ a well-ordered set, $(V_{\lambda})_{\lambda \in L}$ a covering of $X$ by
affine opens, $U$ an open of $X$; for every $\lambda \in L$, put $W_{\lambda} = \bigcup_{\mu < \lambda} V_{\mu}$.
Suppose that: $1°$ For every $\lambda \in L$, $V_{\lambda} \cap W_{\lambda}$ is quasi-compact; $2°$ The immersion
morphism $U \to X$ is quasi-compact. Then, for every quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ and every
quasi-coherent sub-$(\mathcal{O}_{X}|U)$-Module of finite type $\mathcal{G}$ of $\mathcal{F}|U$, there exists a
quasi-coherent sub-$\mathcal{O}_{X}$-Module of finite type $\mathcal{G}'$ of $\mathcal{F}$ such that $\mathcal{G}'|U =
\mathcal{G}$.

**Proof.** Put $U_{\lambda} = U \cup W_{\lambda}$; one is going to define by transfinite recursion a family
$(\mathcal{G}'_{\lambda})$, where $\mathcal{G}'_{\lambda}$ is a quasi-coherent
sub-$(\mathcal{O}_{X}|U_{\lambda})$-Module of finite type of $\mathcal{F}|U_{\lambda}$, such that
$\mathcal{G}'_{\lambda}|U_{\mu} = \mathcal{G}'_{\mu}$ for $\mu < \lambda$ and $\mathcal{G}'_{\lambda}|U = \mathcal{G}$.
The unique sub-$\mathcal{O}_{X}$-Module $\mathcal{G}'$ of $\mathcal{F}$ such that $\mathcal{G}'|U_{\lambda} =
\mathcal{G}'_{\lambda}$ for every $\lambda \in L$ (0, 3.3.1) will answer the question. Suppose then the
$\mathcal{G}'_{\mu}$ defined and having the preceding properties for $\mu < \lambda$; if $\lambda$ has no predecessor,
one will take for $\mathcal{G}'_{\lambda}$ the unique sub-$(\mathcal{O}_{X}|U_{\lambda})$-Module of
$\mathcal{F}|U_{\lambda}$ such that $\mathcal{G}'_{\lambda}|U_{\mu} = \mathcal{G}'_{\mu}$ for every $\mu < \lambda$,
which is licit since the $U_{\mu}$ with $\mu < \lambda$ then form a covering of $U_{\lambda}$. If on the contrary
$\lambda = \mu + 1$, one has $U_{\lambda} = U_{\mu} \cup V_{\mu}$, and it will suffice to define a quasi-coherent
sub-$(\mathcal{O}_{X}|V_{\mu})$-Module of finite type $\mathcal{G}''_{\mu}$ of $\mathcal{F}|V_{\mu}$ such that $$
\mathcal{G}''_{\mu}|(U_{\mu} \cap V_{\mu}) = \mathcal{G}'_{\mu}|(U_{\mu} \cap V_{\mu}); $$ one will then take for
$\mathcal{G}'_{\lambda}$ the sub-$(\mathcal{O}_{X}|U_{\lambda})$-Module of $\mathcal{F}|U_{\lambda}$ such that
$\mathcal{G}'_{\lambda}|U_{\mu} = \mathcal{G}'_{\mu}$ and $\mathcal{G}'_{\lambda}|V_{\mu} = \mathcal{G}''_{\mu}$ (0,
3.3.1). Now, since $V_{\mu}$ is affine, the existence of $\mathcal{G}''_{\mu}$ is assured by (9.4.3) as soon as one has
proved that $U_{\mu} \cap V_{\mu}$ is quasi-compact; but $U_{\mu} \cap V_{\mu}$ is the union of $U \cap V_{\mu}$ and
$W_{\mu} \cap V_{\mu}$, which are both quasi-compact by virtue of the hypothesis.

**Theorem (9.4.7).** Let $X$ be a prescheme, $U$ an open of $X$. Suppose one of the following conditions verified:

a) The space underlying $X$ is locally Noetherian.

b) $X$ is a quasi-compact scheme and $U$ a quasi-compact open.

For every quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ and every quasi-coherent
sub-$(\mathcal{O}_{X}|U)$-Module of finite type $\mathcal{G}$ of $\mathcal{F}|U$, there then exists a quasi-coherent
sub-$\mathcal{O}_{X}$-Module of finite type $\mathcal{G}'$ of $\mathcal{F}$ such that $\mathcal{G}'|U = \mathcal{G}$.

**Proof.** Let $(V_{\lambda})_{\lambda \in L}$ be a covering of $X$ by affine opens, $L$ being supposed finite in case
b); $L$ being endowed with a structure of well-ordered set, it suffices to verify that the conditions of the lemma
(9.4.6) are satisfied. This is evident in hypothesis a), the spaces $V_{\lambda}$ being Noetherian. In hypothesis b),
the $V_{\lambda} \cap V_{\mu}$ are affine (5.5.6), hence quasi-compact, and since $L$ is finite, $V_{\lambda} \cap
W_{\lambda}$ is quasi-compact. Whence the theorem.

**Corollary (9.4.8).** Under the hypotheses of (9.4.7), for every quasi-coherent $(\mathcal{O}_{X}|U)$-Module of finite
type $\mathcal{G}$, there exists a quasi-coherent $\mathcal{O}_{X}$-Module of finite type $\mathcal{G}'$ such that
$\mathcal{G}'|U = \mathcal{G}$.

**Proof.** It suffices to apply (9.4.7) to $\mathcal{F} = j_{*}(\mathcal{G})$, which is quasi-coherent (9.4.2) and such
that $\mathcal{F}|U = \mathcal{G}$.

**Corollary (9.4.9).** Let $X$ be a prescheme whose underlying space is locally Noetherian, or a quasi-compact scheme.
Then every quasi-coherent $\mathcal{O}_{X}$-Module is the inductive limit of its quasi-coherent
sub-$\mathcal{O}_{X}$-Modules of finite type.

**Proof.** This results from (9.4.7) and from the remark (9.4.4).

**Corollary (9.4.10).** Under the hypotheses of (9.4.9), if a quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{F}$ is
such that every quasi-coherent sub-$\mathcal{O}_{X}$-Module of finite type of $\mathcal{F}$ is generated by its sections
over $X$, then $\mathcal{F}$ is generated by its sections over $X$.

**Proof.** Indeed, let $U$ be an affine open neighborhood of a point $x \in X$, and let $s$ be a section of
$\mathcal{F}$ over $U$; the sub-$\mathcal{O}_{X}$-Module $\mathcal{G}$ of $\mathcal{F}|U$ generated by $s$ is
quasi-coherent and of finite type, hence there exists a quasi-coherent sub-$\mathcal{O}_{X}$-Module of finite type
$\mathcal{G}'$ of $\mathcal{F}$ such that $\mathcal{G}'|U = \mathcal{G}$ (9.4.7). By hypothesis, there are therefore a
finite number of sections $t_{i}$ of $\mathcal{G}'$ over $X$ and sections $a_{i}$ of $\mathcal{O}_{X}$ over a
neighborhood $V \subset U$ of $x$ such that $s|V = \sum_{i} a_{i} \cdot (t_{i}|V)$, which proves the corollary.

## 9.5. Closed image of a prescheme; closure of a subprescheme

<!-- label: I.9.5 -->

**Proposition (9.5.1).** Let $f : X \to Y$ be a morphism of preschemes such that $f_{*}(\mathcal{O}_{X})$ is a quasi-coherent $\mathcal{O}_{Y}$-Module (which holds if $f$ is quasi-compact and if moreover $f$ is separated or $X$ locally Noetherian (9.2.2)). Then there exists a smallest subprescheme $Y'$ of $Y$ such that the canonical injection $j : Y' \to Y$ majorizes $f$ (or, what amounts to the same (4.4.1), such that the subprescheme $f^{-1}(Y')$ of $X$ is identical to $X$).

More precisely:

**Corollary (9.5.2).** Under the conditions of (9.5.1), let $f = (\psi, \theta)$ and let $\mathcal{J}$ be the
(quasi-coherent) kernel of the homomorphism $\theta : \mathcal{O}_{Y} \to f_{*}(\mathcal{O}_{X})$. Then the closed
subprescheme $Y'$ of $Y$ defined by $\mathcal{J}$ verifies the conditions of (9.5.1).

**Proof.** Since the functor $\psi^{*}$ is exact, the canonical factorization $\theta : \mathcal{O}_{Y} \to \mathcal{O}_{Y}/\mathcal{J} \xrightarrow{\theta'} \psi_{*}(\mathcal{O}_{X})$ gives (0, 3.5.4.3) a factorization $\theta^{\sharp} : \psi^{*}(\mathcal{O}_{Y}) \to \psi^{*}(\mathcal{O}_{Y})/\psi^{*}(\mathcal{J}) \xrightarrow{\theta'^{\sharp}} \mathcal{O}_{X}$; as for every $x \in X$, $\theta_{x}^{\sharp}$ is a local homomorphism, the same is true of $\theta_{x}'^{\sharp}$; if one denotes by $\psi_{0}$ the continuous map $\psi$ considered as a map of $X$ into $X'$, by $\theta_{0}$ the restriction $\theta'|X' : (\mathcal{O}_{Y}/\mathcal{J})|X' \to \psi_{*}(\mathcal{O}_{X})|X' = (\psi_{0})_{*}(\mathcal{O}_{X})$, one sees thus that $f_{0} = (\psi_{0}, \theta_{0})$ is a morphism of preschemes $X \to X'$ (2.2.1) such that $f = j \circ f_{0}$. If now $X''$ is a second closed subprescheme of $Y$, defined by a quasi-coherent sheaf of ideals $\mathcal{J}'$ of $\mathcal{O}_{Y}$ and such that the injection $j' : X'' \to Y$ majorizes $f$, one must first have $X'' \supset \psi(X)$, hence $X' \subset X''$ since $X''$ is closed. Moreover, for every $y \in X''$, $\theta$ must factor as $\mathcal{O}_{y} \to \mathcal{O}_{y}/\mathcal{J}'_{y} \to (\psi_{*}(\mathcal{O}_{X}))_{y}$, which by definition entails $\mathcal{J}'_{y} \subset \mathcal{J}_{y}$, and consequently $X'$ is a closed subprescheme of $X''$ (4.1.10).

**Definition (9.5.3).** When there exists a smallest closed subprescheme $Y'$ of $Y$ such that the canonical injection
$j : Y' \to Y$ majorizes $f$, one says that $Y'$ is the _closed image prescheme of $X$ under the morphism $f$_.

**Proposition (9.5.4).** If $f_{*}(\mathcal{O}_{X})$ is a quasi-coherent $\mathcal{O}_{Y}$-Module, the space underlying
the closed image of $X$ under $f$ is the closure $\overline{f(X)}$ in $Y$.

**Proof.** Since the support of $f_{*}(\mathcal{O}_{X})$ is contained in $\overline{f(X)}$, one has (with the notations
of (9.5.2)) $\mathcal{J}_{y} = \mathcal{O}_{y}$ for $y \notin \overline{f(X)}$, hence the support of
$\mathcal{O}_{Y}/\mathcal{J}$ is contained in $\overline{f(X)}$. Moreover, this support is closed and contains $f(X)$:
indeed, if $y \in f(X)$, the unit element of the ring $(\psi_{*}(\mathcal{O}_{X}))_{y}$ is not null, being the germ at
$y$ of the section $$ 1 \in \Gamma(X, \mathcal{O}_{X}) = \Gamma(Y, \psi_{*}(\mathcal{O}_{X})); $$ since it is the image
under $\theta$ of the unit element of $\mathcal{O}_{y}$, the latter does not belong to $\mathcal{J}_{y}$, hence
$\mathcal{O}_{y}/\mathcal{J}_{y} \neq 0$; this completes the demonstration.

**Proposition (9.5.5)** (transitivity of closed images). Let $f : X \to Y$ and $g : Y \to Z$ be two morphisms of
preschemes; suppose that the closed image $Y'$ of $X$ under $f$ exists, and that, if $g'$ is the restriction of $g$ to
$Y'$, the closed image $Z'$ of $Y'$ under $g'$ exists. Then the closed image of $X$ under $g \circ f$ exists and is
equal to $Z'$.

**Proof.** It suffices (9.5.1) to show that $Z'$ is the smallest closed subprescheme $Z_{1}$ of $Z$ such that the closed
subprescheme $(g \circ f)^{-1}(Z_{1})$ of $X$ (equal to $f^{-1}(g^{-1}(Z_{1}))$ by (4.4.2)) is equal to $X$; it amounts
to the same to say that $Z'$ is the smallest closed subprescheme of $Z$ such that $f$ is majorized by the injection
$g^{-1}(Z_{1}) \to Y$ (4.4.1). Now, by virtue of the existence of the closed image $Y'$, every $Z_{1}$ having this
property is such that $g^{-1}(Z_{1})$ majorizes $Y'$, which is equivalent to saying that $j'^{-1}(g^{-1}(Z_{1})) =
g'^{-1}(Z_{1}) = Y'$, denoting by $j'$ the injection $Y' \to Y$. By definition of $Z'$, one concludes well that $Z'$ is
the smallest closed subprescheme of $Z$ verifying the preceding condition.

**Corollary (9.5.6).** Let $f : X \to Y$ be an $S$-morphism such that $Y$ is the closed image of $X$ under $f$. Let $Z$
be an $S$-scheme; if two $S$-morphisms $g_{1}$, $g_{2}$ of $Y$ into $Z$ are such that $g_{1} \circ f = g_{2} \circ f$,
then $g_{1} = g_{2}$.

**Proof.** Let $h = (g_{1}, g_{2})_{S} : Y \to Z \times_{S} Z$; since the diagonal $T = \Delta_{Z}(Z)$ is a closed
subprescheme of $Z \times_{S} Z$, $Y' = h^{-1}(T)$ is a closed subprescheme of $Y$ (4.4.1). Put $u = g_{1} \circ f =
g_{2} \circ f$; one then has by definition of the product $h' = h \circ f = (u, u)_{S}$, hence $h \circ f = \Delta_{Z}
\circ u$; since $\Delta_{Z}^{-1}(T) = Z$, one has $h'^{-1}(T) = u^{-1}(Z) = X$, hence $f^{-1}(Y') = X$. One concludes
(4.4.1) that the canonical injection $Y' \to Y$ majorizes $f$, hence $Y' = Y$ by hypothesis; consequently (4.4.1), $h$
factors as $\Delta_{Z} \circ v$, where $v$ is a morphism $Y \to Z$, which entails $g_{1} = g_{2} = v$.

**Remark (9.5.7).** If $X$ and $Y$ are $S$-schemes, the proposition (9.5.6) signifies that when $Y$ is the closed image
of $X$ under $f$, $f$ is an epimorphism in the category of $S$-schemes (T, 1.1). We shall prove in chap. V that,
conversely, if the closed image $Y'$ of $X$ under $f$ exists and if $f$ is an epimorphism of $S$-schemes, then one
necessarily has $Y' = Y$.

**Proposition (9.5.8).** Suppose the hypotheses of (9.5.1) verified, and let $Y'$ be the closed image of $X$ under $f$.
For every open $V$ of $Y$, let $f_{V} : f^{-1}(V) \to V$ be the restriction of $f$; then the closed image of $f^{-1}(V)$
under $f_{V}$ in $V$ exists and is equal to the prescheme induced by $Y'$ on the open $V \cap Y'$ of $Y'$ (in other
words, to the subprescheme $\inf(V, Y')$ of $Y$ (4.4.3)).

**Proof.** Put $X' = f^{-1}(V)$; since the direct image of $\mathcal{O}_{X'}$ under $f_{V}$ is none other than the
restriction of $f_{*}(\mathcal{O}_{X})$ to $V$, it is clear that the kernel $\mathcal{J}'$ of the homomorphism
$\mathcal{O}_{V} \to (f_{V})_{*}(\mathcal{O}_{X'})$ is the restriction of $\mathcal{J}$ to $V$, whence at once the
proposition.

It will be noted that this result is interpreted by saying that the formation of the closed image commutes with an
extension $Y_{1} \to Y$ of the base prescheme that is an open immersion. We shall see in chap. IV that the same holds
for an extension $Y_{1} \to Y$ that is a flat morphism, provided that $f$ is separated and quasi-compact.

**Proposition (9.5.9).** Let $f : X \to Y$ be a morphism such that the closed image $Y'$ of $X$ under $f$ exists.

(i) If $X$ is reduced, so is $Y'$.

(ii) If one supposes the hypotheses of (9.5.1) verified and if $X$ is irreducible (resp. integral), so is $Y'$.

**Proof.** By hypothesis, the morphism $f$ factors as $X \xrightarrow{g} Y' \xrightarrow{j} Y$, where $j$ is the
canonical injection. Since $X$ is reduced, $g$ factors as $X \xrightarrow{h} Y'_{\mathrm{red}} \xrightarrow{j'} Y'$,
where $j'$ is the canonical injection (5.2.2), and it then results from the definition of $Y'$ that $Y'_{\mathrm{red}} =
Y'$. If moreover the conditions of (9.5.1) are fulfilled, it results from (9.5.4) that $f(X)$ is dense in $Y'$; if $X$
is irreducible, so therefore is $Y'$ (0, 2.1.5). The assertion relative to integral preschemes results from the
conjunction of the two others.

**Proposition (9.5.10).** Let $Y$ be a subprescheme of a prescheme $X$, such that the canonical injection $i : Y \to X$
is a quasi-compact morphism. There then exists a smallest closed subprescheme $\overline{Y}$ of $X$ majorizing $Y$; its
underlying space is the closure of that of $Y$; the latter is open in its closure, and the prescheme $Y$ is induced on
this open by $\overline{Y}$.

**Proof.** It suffices to apply (9.5.1) to the injection $j$, which is separated (5.5.1) and quasi-compact by
hypothesis; (9.5.1) thus proves the existence of $\overline{Y}$ and (9.5.4) shows that its underlying space is the
closure of $Y$ in $X$; since $Y$ is locally closed in $X$, it is open in $\overline{Y}$, and the last assertion comes
from (9.5.8) applied to an open $V$ of $X$ such that $Y$ is closed in $V$.

With these notations, if the injection $V \to X$ is quasi-compact, and if $\mathcal{J}$ is the quasi-coherent sheaf of
ideals of $\mathcal{O}_{X}|V$ defining the closed subprescheme $Y$ of $V$, it results from (9.5.1) that the
quasi-coherent sheaf of ideals of $\mathcal{O}_{X}$ defining $\overline{Y}$ is the canonical extension (9.4.1)
$\overline{\mathcal{J}}$ of $\mathcal{J}$, for it is evidently the largest quasi-coherent subsheaf of ideals of
$\mathcal{O}_{X}$ inducing $\mathcal{J}$ on $V$.

**Corollary (9.5.11).** Under the hypotheses of (9.5.10), every section of $\mathcal{O}_{\overline{Y}}$ over an open $V$
of $\overline{Y}$ that is null in $V \cap Y$ is null.

**Proof.** By virtue of (9.5.8), one may reduce to the case where $V = \overline{Y}$. If one takes account of the fact
that the sections of $\mathcal{O}_{\overline{Y}}$ over $\overline{Y}$ correspond canonically to the
$\overline{Y}$-sections of $\overline{Y} \otimes_{\mathbf{Z}} \mathbf{Z}[T]$ (3.3.15) and of the fact that the latter is
separated over $\overline{Y}$, the corollary appears as a particular case of (9.5.6).

When there exists a smallest closed subprescheme $\overline{Y}$ of $X$ majorizing a subprescheme $Y$ of $X$, one says
that $Y'$ is the _closure of $Y$ in $X$_, when no confusion results.

## 9.6. Quasi-coherent sheaves of algebras; change of the structure sheaf

<!-- label: I.9.6 -->

**Proposition (9.6.1).** Let $X$ be a prescheme, $\mathcal{B}$ a quasi-coherent $\mathcal{O}_{X}$-Algebra (0, 5.1.3).
For a $\mathcal{B}$-Module $\mathcal{F}$ to be quasi-coherent (on the ringed space $(X, \mathcal{B})$), it is necessary
and sufficient that $\mathcal{F}$ be a quasi-coherent $\mathcal{O}_{X}$-Module.

**Proof.** Since the question is local, one may suppose $X$ affine with ring $A$, and then $\mathcal{B} =
\widetilde{B}$, where $B$ is an $A$-algebra (1.4.3). If $\mathcal{F}$ is quasi-coherent on the ringed space $(X,
\mathcal{B})$, one may also suppose that $\mathcal{F}$ is the cokernel of a $\mathcal{B}$-homomorphism
$\mathcal{B}^{(I)} \to \mathcal{B}^{(J)}$; since this homomorphism is also an $\mathcal{O}_{X}$-homomorphism of
$\mathcal{O}_{X}$-Modules, and since $\mathcal{B}^{(I)}$ and $\mathcal{B}^{(J)}$ are quasi-coherent
$\mathcal{O}_{X}$-Modules (1.3.9, (ii)), $\mathcal{F}$ is also a quasi-coherent $\mathcal{O}_{X}$-Module (1.3.9, (i)).

Inversely, if $\mathcal{F}$ is a quasi-coherent $\mathcal{O}_{X}$-Module, one has $\mathcal{F} = \widetilde{M}$, where
$M$ is a $B$-module (1.4.3); $M$ is isomorphic to a cokernel of a $B$-homomorphism $B^{(I)} \to B^{(J)}$, hence
$\mathcal{F}$ is a $\mathcal{B}$-Module isomorphic to the cokernel of the corresponding homomorphism $\mathcal{B}^{(I)}
\to \mathcal{B}^{(J)}$ (1.3.13), which completes the demonstration.

In particular, if $\mathcal{F}$ and $\mathcal{G}$ are two quasi-coherent $\mathcal{B}$-Modules, $\mathcal{F}
\otimes_{\mathcal{B}} \mathcal{G}$ is a quasi-coherent $\mathcal{B}$-Module; the same is true of
$\mathcal{H}om_{\mathcal{B}}(\mathcal{F}, \mathcal{G})$ when one supposes in addition that $\mathcal{F}$ admits a finite
presentation (1.3.13).

**(9.6.2)** Given a prescheme $X$, we shall say that a quasi-coherent $\mathcal{O}_{X}$-Algebra $\mathcal{B}$ is of
_finite type_ if for every $x \in X$, there exists an affine open neighborhood $U$ of $x$ such that $\Gamma(U,
\mathcal{B}) = B$ is an algebra of finite type over $\Gamma(U, \mathcal{O}_{X}) = A$. One then has $\mathcal{B}|U =
\widetilde{B}$, and for every $f \in A$, the $(\mathcal{O}_{X}|D(f))$-Algebra induced $\mathcal{B}|D(f)$ is of finite
type, for it is isomorphic to $(B_{f})^{\sim}$, and $B_{f} = B \otimes_{A} A_{f}$ is evidently an algebra of finite type
over $A_{f}$. Since the $D(f)$ form a base of the topology of $U$, one concludes that if $\mathcal{B}$ is a
quasi-coherent $\mathcal{O}_{X}$-Algebra of finite type, then for every open $V$ of $X$, $\mathcal{B}|V$ is a
quasi-coherent $(\mathcal{O}_{X}|V)$-Algebra of finite type.

**Proposition (9.6.3).** Let $X$ be a locally Noetherian prescheme. Then every quasi-coherent $\mathcal{O}_{X}$-Algebra
of finite type $\mathcal{B}$ is a coherent sheaf of rings (0, 5.3.7).

**Proof.** One may again limit oneself to the case where $X$ is an affine scheme with Noetherian ring $A$, and where
$\mathcal{B} = \widetilde{B}$, $B$ being an $A$-algebra of finite type; $B$ is then a Noetherian ring. This being so, it
is necessary to prove that the kernel $\mathcal{N}$ of a $\mathcal{B}$-homomorphism $\mathcal{B}^{m} \to \mathcal{B}$ is
a $\mathcal{B}$-Module of finite type; now, it is isomorphic (as a $\mathcal{B}$-Module) to $\widetilde{N}$, where $N$
is the kernel of the corresponding homomorphism of $B$-modules $B^{m} \to B$ (1.3.13). Since $B$ is Noetherian, the
submodule $N$ of $B^{m}$ is a $B$-module of finite type, hence there exists a homomorphism $B^{p} \to B^{m}$ of image
$N$; the sequence $B^{p} \to B^{m} \to B$ being exact, the same is true of the corresponding sequence $\mathcal{B}^{p}
\to \mathcal{B}^{m} \to \mathcal{B}$ (1.3.5), and since $\mathcal{N}$ is the image of $\mathcal{B}^{p} \to
\mathcal{B}^{m}$ (1.3.9, (i)), the proposition is proved.

**Corollary (9.6.4).** Under the hypotheses of (9.6.3), for a $\mathcal{B}$-Module $\mathcal{F}$ to be coherent, it is
necessary and sufficient that it be a quasi-coherent $\mathcal{O}_{X}$-Module and a $\mathcal{B}$-Module of finite type.
If this is so, and if $\mathcal{G}$ is a sub-$\mathcal{B}$-Module or a quotient $\mathcal{B}$-Module of $\mathcal{F}$,
then for $\mathcal{G}$ to be a coherent $\mathcal{B}$-Module, it is necessary and sufficient that $\mathcal{G}$ be a
quasi-coherent $\mathcal{O}_{X}$-Module.

**Proof.** Taking account of (9.6.1), the conditions on $\mathcal{F}$ are evidently necessary; let us show that they are
sufficient. One may limit oneself to the case where $X$ is affine with Noetherian ring $A$, $\mathcal{B} =
\widetilde{B}$, where $B$ is an $A$-algebra of finite type, $\mathcal{F} = \widetilde{M}$, where $M$ is a $B$-module,
and where there exists a surjective $\mathcal{B}$-homomorphism $\mathcal{B}^{m} \to \mathcal{F} \to 0$. One then has a
corresponding exact sequence $B^{m} \to M \to 0$, hence $M$ is a $B$-module of finite type; moreover, the kernel $P$ of
the homomorphism $B^{m} \to M$ is then a $B$-module of finite type, since $B$ is Noetherian. One concludes (1.3.13) that
$\mathcal{F}$ is the cokernel of a $\mathcal{B}$-homomorphism $\mathcal{B}^{p} \to \mathcal{B}^{m}$ and is therefore
coherent since $\mathcal{B}$ is a coherent sheaf of rings (0, 5.3.4). The same reasoning shows that a quasi-coherent
sub-$\mathcal{B}$-Module (resp. a quotient $\mathcal{B}$-Module) of $\mathcal{F}$ is of finite type, whence the second
part of the corollary.

**Proposition (9.6.5).** Let $X$ be a quasi-compact scheme or a prescheme whose underlying space is Noetherian. For
every quasi-coherent $\mathcal{O}_{X}$-Algebra of finite type $\mathcal{B}$, there exists a quasi-coherent
sub-$\mathcal{O}_{X}$-Module of finite type $\mathcal{E}$ of $\mathcal{B}$ such that $\mathcal{E}$ generates (0, 4.1.4)
the $\mathcal{O}_{X}$-Algebra $\mathcal{B}$.

**Proof.** Indeed, there exists by hypothesis a finite covering $(U_{i})$ of $X$ formed of affine opens such that
$\Gamma(U_{i}, \mathcal{B}) = B_{i}$ is an algebra of finite type over $\Gamma(U_{i}, \mathcal{O}_{X}) = A_{i}$; let
$E_{i}$ be a sub-$A_{i}$-module of finite type of $B_{i}$ generating the $A_{i}$-algebra $B_{i}$; by virtue of (9.4.7),
there exists a sub-$\mathcal{O}_{X}$-Module $\mathcal{E}_{i}$ of $\mathcal{B}$, quasi-coherent and of finite type, such
that $\mathcal{E}_{i}|U_{i} = \widetilde{E}_{i}$. It is clear that the sum $\mathcal{E}$ of the $\mathcal{E}_{i}$
answers the question.

**Proposition (9.6.6).** Let $X$ be a prescheme whose underlying space is locally Noetherian, or a quasi-compact scheme.
Then every quasi-coherent $\mathcal{O}_{X}$-Algebra $\mathcal{B}$ is the inductive limit of its quasi-coherent
sub-$\mathcal{O}_{X}$-Algebras of finite type.

**Proof.** Indeed, it results from (9.4.9) that $\mathcal{B}$ is the inductive limit (as an $\mathcal{O}_{X}$-Module) of
its quasi-coherent sub-$\mathcal{O}_{X}$-Modules of finite type; these last generate quasi-coherent
sub-$\mathcal{O}_{X}$-Algebras of finite type of $\mathcal{B}$ (1.3.14), of which $\mathcal{B}$ is a fortiori the
inductive limit.

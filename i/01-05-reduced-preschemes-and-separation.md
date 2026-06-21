# §5. Reduced Preschemes; Separation Condition

<!-- label: I.5 -->

## 5.1. Reduced preschemes

<!-- label: I.5.1 -->

**Proposition (5.1.1).** Let $(X, \mathcal{O}_{X})$ be a prescheme and $\mathcal{B}$ a quasi-coherent
$\mathcal{O}_{X}$-Algebra. There exists one and only one quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{N}$ whose
stalk $\mathcal{N}_{x}$ at every $x \in X$ is the nilradical of the ring $\mathcal{B}_{x}$. When $X$ is affine, and
consequently $\mathcal{B} = \tilde{B}$, where $B$ is an algebra over $A(X)$, one has $\mathcal{N} =
\tilde{\mathfrak{R}}$, where $\mathfrak{R}$ is the nilradical of $B$.

**Proof.** The question being local, we are reduced to proving the last assertion. We know that $\tilde{\mathfrak{R}}$
is a quasi-coherent $\mathcal{O}_{X}$-Module (1.4.1) and that its stalk at the point $x \in X$ is the ideal
$\mathfrak{R}_{x}$ of the ring of fractions $B_{x}$; everything comes down to proving that the nilradical of $B_{x}$ is
contained in $\mathfrak{R}_{x}$, the opposite inclusion being evident. Now let $z/s$ be an element of the nilradical of
$B_{x}$, with $z \in B$, $s \notin \mathfrak{j}_{x}$; by hypothesis, there exists an integer $k$ such that $(z/s)^{k} =
0$, which means that there exists $t \notin \mathfrak{j}_{x}$ such that $tz^{k} = 0$. We conclude that $(tz)^{k} = 0$,
and consequently $z/s = (tz)/(ts)$ belongs to $\mathfrak{R}_{x}$.

We shall say that the quasi-coherent $\mathcal{O}_{X}$-Module $\mathcal{N}$ thus defined is the _Nilradical of the
$\mathcal{O}_{X}$-Algebra $\mathcal{B}$_; we shall denote in particular by $\mathcal{N}_{X}$ the nilradical of
$\mathcal{O}_{X}$.

**Corollary (5.1.2).** Let $X$ be a prescheme; the closed subprescheme of $X$ defined by the sheaf of ideals
$\mathcal{N}_{X}$ is the only reduced subprescheme (0, 4.1.4) of $X$ having $X$ as underlying space; it is also the
smallest subprescheme of $X$ having $X$ as underlying space.

**Proof.** Since the structure sheaf of the closed subprescheme $Y$ defined by $\mathcal{N}_{X}$ is
$\mathcal{O}_{X}/\mathcal{N}_{X}$, it is immediate that $Y$ is reduced and has $X$ as underlying space, since
$\mathcal{N}_{x} \neq \mathcal{O}_{x}$ for every $x \in X$. To prove the other assertions, remark that a subprescheme
$Z$ of $X$ having $X$ as underlying space is defined by a sheaf of ideals $\mathcal{J}$ (4.1.3) such that
$\mathcal{J}_{x} \neq \mathcal{O}_{x}$ for every $x \in X$. We may restrict ourselves to the case where $X$ is affine,
say $X = \operatorname{Spec}(A)$ and $\mathcal{J} = \tilde{\mathfrak{J}}$, where $\mathfrak{J}$ is an ideal of $A$;
then, for every $x \in X$, one has $\mathfrak{J}_{x} \neq \mathfrak{j}_{x}$, so $\mathfrak{J}$ is contained in all the
prime ideals of $A$, that is, in their intersection $\mathfrak{R}$, the nilradical of $A$. This proves that $Y$ is the
smallest subprescheme of $X$ having $X$ as underlying space (4.1.9); moreover, if $Z$ is distinct from $Y$, one
necessarily has $\mathcal{J}_{x} \neq \mathcal{N}_{x}$ for at least one $x \in X$, and consequently (5.1.1) $Z$ is not
reduced.

**Definition (5.1.3).** The _reduced prescheme associated with a prescheme $X$_, denoted $X_{\mathrm{red}}$, is the
unique reduced subprescheme of $X$ having $X$ as underlying space.

To say that a prescheme $X$ is reduced thus means that $X = X_{\mathrm{red}}$.

**Proposition (5.1.4).** For the prime spectrum of a ring $A$ to be a reduced (resp. integral) prescheme (2.1.7), it is
necessary and sufficient that $A$ be a reduced (resp. integral) ring.

**Proof.** Indeed, it follows at once from (5.1.1) that the condition $\mathcal{N} = (0)$ is necessary and sufficient
for $X = \operatorname{Spec}(A)$ to be reduced; the assertion concerning integral rings is then a consequence of
(1.1.13).

Since every ring of fractions $\neq \{0\}$ of an integral ring is integral, it follows from (5.1.4) that for every
locally integral prescheme $X$, $\mathcal{O}_{x}$ is an integral ring for every $x \in X$. The converse is true when the
underlying space of $X$ is locally Noetherian: indeed, $X$ is then reduced, and if $U$ is an affine open of $X$ which is
a Noetherian space, $U$ has only a finite number of irreducible components, so its ring $A$ has only a finite number of
minimal prime ideals (1.1.14). If two of these components $U_{i}$ had a common point $x$, $\mathcal{O}_{x}$ would have
at least two distinct minimal prime ideals, and so would not be integral; the $U_{i}$ are consequently pairwise disjoint
opens, and each of them is therefore integral.

**(5.1.5)** Let $f = (\psi, \theta) : X \to Y$ be a morphism of preschemes; the homomorphism $\theta_{x}^{\sharp} :
\mathcal{O}_{\psi(x)} \to \mathcal{O}_{x}$ sends every nilpotent element of $\mathcal{O}_{\psi(x)}$ to a nilpotent element
of $\mathcal{O}_{x}$; by passage to the quotients, one therefore deduces from $\theta^{\sharp}$ a homomorphism
$$ \omega : \psi^{*}(\mathcal{O}_{Y}/\mathcal{N}_{Y}) \to \mathcal{O}_{X}/\mathcal{N}_{X}. $$
It is clear that for every $x \in X$, $\omega_{x} : \mathcal{O}_{\psi(x)}/\mathcal{N}_{\psi(x)} \to
\mathcal{O}_{x}/\mathcal{N}_{x}$ is a local homomorphism, so $(\psi, \omega)$ is a morphism of preschemes
$X_{\mathrm{red}} \to Y_{\mathrm{red}}$, which we shall denote $f_{\mathrm{red}}$ and call the _reduced morphism
associated with $f$_. It is immediate that for two morphisms $f : X \to Y$, $g : Y \to Z$, one has $(g \circ
f)_{\mathrm{red}} = g_{\mathrm{red}} \circ f_{\mathrm{red}}$, so one has defined $X_{\mathrm{red}}$ as a covariant
functor in $X$.

The preceding definition shows that the diagram
$$
\begin{array}{ccc}
X_{\mathrm{red}} & \xrightarrow{f_{\mathrm{red}}} & Y_{\mathrm{red}} \\
\downarrow & & \downarrow \\
X & \xrightarrow{f} & Y
\end{array}
$$
is commutative, the vertical arrows being the injection morphisms; in other words, $X_{\mathrm{red}} \to X$ is a
functorial morphism. One will note in particular that if $X$ is reduced, every morphism $f : X \to Y$ factors as $X
\xrightarrow{f_{\mathrm{red}}} Y_{\mathrm{red}} \to Y$; in other words, $f$ is dominated by the injection morphism
$Y_{\mathrm{red}} \to Y$.

**Proposition (5.1.6).** Let $f : X \to Y$ be a morphism; if $f$ is surjective (resp. radicial, an immersion, a closed
immersion, an open immersion, a local immersion, a local isomorphism), then so is $f_{\mathrm{red}}$. Conversely, if
$f_{\mathrm{red}}$ is surjective (resp. radicial), then so is $f$.

**Proof.** The proposition is trivial if $f$ is surjective; if $f$ is radicial, it follows from the fact that for every
$x \in X$, the field $\kappa(x)$ is the same for the preschemes $X$ and $X_{\mathrm{red}}$ (3.5.8). Finally, if $f =
(\psi, \theta)$ is an immersion, a closed immersion, or a local immersion (resp. an open immersion, or a local
isomorphism), the proposition follows from the fact that if $\theta^{\sharp}$ is surjective (resp. bijective), then so
is the homomorphism obtained by passing to the quotients by the nilradicals of $\mathcal{O}_{\psi(x)}$ and
$\mathcal{O}_{x}$ (5.1.2 and 4.2.2) (cf. (5.5.12)).

**Proposition (5.1.7).** If $X$, $Y$ are two $S$-preschemes, the preschemes $X_{\mathrm{red}} \times_{S_{\mathrm{red}}}
Y_{\mathrm{red}}$ and $X_{\mathrm{red}} \times_{S} Y_{\mathrm{red}}$ are identical, and are canonically identified with
a subprescheme of $X \times_{S} Y$ having the same underlying space as this product.

**Proof.** The canonical identification of $X_{\mathrm{red}} \times_{S} Y_{\mathrm{red}}$ with a subprescheme of $X
\times_{S} Y$ having the same underlying space follows from (4.3.1). On the other hand, if $\varphi$ and $\psi$ are the
structure morphisms $X_{\mathrm{red}} \to S$, $Y_{\mathrm{red}} \to S$, they factor through $S_{\mathrm{red}}$ (5.1.5),
and since $S_{\mathrm{red}} \to S$ is a monomorphism, the first assertion follows from (3.2.4).

**Corollary (5.1.8).** The preschemes $(X \times_{S} Y)_{\mathrm{red}}$ and $(X_{\mathrm{red}} \times_{S_{\mathrm{red}}}
Y_{\mathrm{red}})_{\mathrm{red}}$ are canonically identified.

**Proof.** This follows from (5.1.2) and (5.1.7).

One will note that if $X$ and $Y$ are reduced preschemes, the same is not necessarily true of $X \times_{S} Y$, for the
tensor product of two reduced algebras may have nilpotent elements.

**Proposition (5.1.9).** Let $X$ be a prescheme, $\mathcal{J}$ a quasi-coherent sheaf of ideals of $\mathcal{O}_{X}$
such that $\mathcal{J}^{n} = 0$ for an integer $n > 0$. Let $X_{0}$ be the closed subprescheme $(X,
\mathcal{O}_{X}/\mathcal{J})$ of $X$; for $X$ to be an affine scheme, it is necessary and sufficient that $X_{0}$ be
one.

**Proof.** The condition being evidently necessary, let us prove that it is sufficient. If we set $X_{k} = (X,
\mathcal{O}_{X}/\mathcal{J}^{k+1})$, everything comes down to proving by induction on $k$ that the $X_{k}$ are affine, so
we are reduced to the case where $\mathcal{J}^{2} = 0$. Set
$$ A = \Gamma(X, \mathcal{O}_{X}), \qquad A_{0} = \Gamma(X_{0}, \mathcal{O}_{X_{0}}) = \Gamma(X, \mathcal{O}_{X}/\mathcal{J}). $$
From the canonical homomorphism $\mathcal{O}_{X} \to \mathcal{O}_{X}/\mathcal{J}$ one deduces a homomorphism of rings
$\varphi : A \to A_{0}$. We shall see below that $\varphi$ is surjective, so that the sequence
$$ \text{(5.1.9.1)} \qquad 0 \to \Gamma(X, \mathcal{J}) \to \Gamma(X, \mathcal{O}_{X}) \to \Gamma(X, \mathcal{O}_{X}/\mathcal{J}) \to 0 $$
is exact. Suppose this point established, and let us show that it entails the proposition. Note that $\mathfrak{R} =
\Gamma(X, \mathcal{J})$ is an ideal of square zero in $A$, and is thus a module over $A_{0} = A/\mathfrak{R}$. By
hypothesis, one has $X_{0} = \operatorname{Spec}(A_{0})$, and since the underlying topological spaces $X_{0}$ and $X$ are
identical, $\mathfrak{R} = \Gamma(X_{0}, \mathcal{J})$; moreover, since $\mathcal{J}^{2} = 0$, $\mathcal{J}$ is a
quasi-coherent $(\mathcal{O}_{X}/\mathcal{J})$-Module, so one has $\mathcal{J} = \tilde{\mathfrak{R}}$ and $\mathcal{J}_{x}
= \mathfrak{R}_{x}$ for every $x \in X_{0}$ (1.4.1). This being so, let $X' = \operatorname{Spec}(A)$, and consider the
morphism $f = (\psi, \theta) : X \to X'$ of preschemes corresponding to the identity map $A \to \Gamma(X, \mathcal{O}_{X})$
(2.2.4). For every affine open $V$ in $X$, the diagram
$$
\begin{array}{ccc}
A & \to & \Gamma(V, \mathcal{O}_{X}|V) \\
\downarrow & & \downarrow \\
A_{0} = A/\mathfrak{R} & \to & \Gamma(V, \mathcal{O}_{X_{0}}|V)
\end{array}
$$
is commutative, whence one concludes that the diagram
$$
\begin{array}{ccc}
X' & \xleftarrow{j} & X \\
\uparrow{\scriptstyle j'} & & \uparrow{\scriptstyle j} \\
X_{0} & \xleftarrow{f_{0}} & X_{0}
\end{array}
$$
is commutative, $X_{0}$ being the closed subprescheme of $X'$ defined by the quasi-coherent sheaf of ideals
$\tilde{\mathfrak{R}}$, and $j$, $j'$ the canonical injection morphisms. But since $X_{0}$ is affine, $f_{0}$ is an
isomorphism, and since the underlying continuous maps of $j$ and $j'$ are the identity maps, one sees first of all that
$\psi : X \to X'$ is a homeomorphism. Moreover, the relation $\mathfrak{R}_{x} = \mathcal{J}_{x}$ shows that the
restriction of $\theta^{\sharp} : \psi^{*}(\mathcal{O}_{X'}) \to \mathcal{O}_{X}$ is an isomorphism of
$\psi^{*}(\tilde{\mathfrak{R}})$ onto $\mathcal{J}$; on the other hand, by passage to the quotients, $\theta^{\sharp}$
gives an isomorphism $\psi^{*}(\mathcal{O}_{X'}/\tilde{\mathfrak{R}}) \to \mathcal{O}_{X}/\mathcal{J}$, since $f_{0}$ is
an isomorphism; one concludes at once from the five lemma (M, I, 1.1) that $\theta^{\sharp}$ is itself an isomorphism, so
that $f$ is an isomorphism, and consequently that $X$ is affine.

Everything thus comes down to proving the exactness of (5.1.9.1), which will follow from $\mathrm{H}^{1}(X, \mathcal{J})
= 0$. Now $\mathrm{H}^{1}(X, \mathcal{J}) = \mathrm{H}^{1}(X_{0}, \mathcal{J})$, and we have seen that $\mathcal{J}$ is
a quasi-coherent $\mathcal{O}_{X_{0}}$-Module. Our assertion will therefore follow from the

**Lemma (5.1.9.2).** If $Y$ is an affine scheme and $\mathcal{F}$ a quasi-coherent $\mathcal{O}_{Y}$-Module, one has
$\mathrm{H}^{1}(Y, \mathcal{F}) = 0$.

This lemma will be proved in chap. III, §1, as a consequence of the more general theorem that $\mathrm{H}^{i}(Y,
\mathcal{F}) = 0$ for every $i > 0$. To give an independent proof of it, observe that $\mathrm{H}^{1}(Y, \mathcal{F})$
is identified with the module $\operatorname{Ext}^{1}_{\mathcal{O}_{Y}}(Y; \mathcal{O}_{Y}, \mathcal{F})$ of classes of
extensions of the $\mathcal{O}_{Y}$-Module $\mathcal{O}_{Y}$ by the $\mathcal{O}_{Y}$-Module $\mathcal{F}$ (T, 4.2.3);
everything thus comes down to proving that such an extension $\mathcal{G}$ is trivial. Now, for every $y \in Y$, there
is a neighborhood $V$ of $y$ in $Y$ such that $\mathcal{G}|V$ is isomorphic to $\mathcal{F}|V \oplus \mathcal{O}_{Y}|V$
(0, 5.4.9); one concludes that $\mathcal{G}$ is a quasi-coherent $\mathcal{O}_{Y}$-Module. If $A$ is the ring of $Y$,
one therefore has $\mathcal{F} = \tilde{M}$, $\mathcal{G} = \tilde{N}$, where $M$ and $N$ are $A$-modules, and by
hypothesis $N$ is an extension of the $A$-module $A$ by the $A$-module $M$ (1.3.11). Since this extension is necessarily
trivial, the lemma is proved, and consequently also (5.1.9).

**Corollary (5.1.10).** Let $X$ be a prescheme such that $\mathcal{N}_{X}$ is nilpotent. For $X$ to be an affine scheme,
it is necessary and sufficient that $X_{\mathrm{red}}$ be one.

## 5.2. Existence of a subprescheme with a given underlying space

<!-- label: I.5.2 -->

**Proposition (5.2.1).** For every locally closed subspace $Y$ of the underlying space of a prescheme $X$, there exists
one and only one reduced subprescheme of $X$ having $Y$ as underlying space.

**Proof.** The uniqueness following from (5.1.2), it remains to prove the existence of the subprescheme in question.

If $X$ is affine with ring $A$, and $Y$ closed in $X$, the proposition is immediate: $\mathfrak{j}(Y)$ is the largest
ideal $\mathfrak{a} \subset A$ such that $V(\mathfrak{a}) = Y$, and it is equal to its radical (1.1.4 (i)), so
$A/\mathfrak{j}(Y)$ is a reduced ring.

In the general case, for every affine open $U \subset X$ such that $U \cap Y$ is closed in $U$, consider the closed
subprescheme $Y_{U}$ of $U$ defined by the sheaf of ideals associated with the ideal $\mathfrak{j}(U \cap Y)$ of $A(U)$,
which is reduced. Let us show that, if $V$ is an affine open of $X$ contained in $U$, $Y_{V}$ is induced by $Y_{U}$ on
$V \cap Y$; now this induced prescheme is a closed subprescheme of $V$ which is reduced and has $V \cap Y$ as underlying
space; the uniqueness of $Y_{V}$ thus entails our assertion.

**Proposition (5.2.2).** Let $X$ be a reduced prescheme, $f : X \to Y$ a morphism, $Z$ a closed subprescheme of $Y$ such
that $f(X) \subset Z$; then $f$ factors as $X \xrightarrow{g} Z \xrightarrow{j} Y$, where $j$ is the injection morphism.

**Proof.** It follows from the hypothesis that the closed subprescheme $f^{-1}(Z)$ of $X$ has the whole of $X$ as
underlying space (4.4.1); since $X$ is reduced, this closed subprescheme coincides with $X$ (5.1.2), and the proposition
thus follows from (4.4.1).

**Corollary (5.2.3).** Let $X$ be a reduced subprescheme of a prescheme $Y$; if $Z$ is the reduced closed subprescheme
of $Y$ having $\bar{X}$ as underlying space, $X$ is a subprescheme induced on an open of $Z$.

**Proof.** There is indeed an open $U$ of $Y$ such that $X = U \cap \bar{X}$; since $X$ is a reduced subprescheme of $Z$
by virtue of (5.2.2), the subprescheme $X$ is induced by $Z$ on the open subspace $X$ by virtue of the uniqueness
(5.2.1).

**Corollary (5.2.4).** Let $f : X \to Y$ be a morphism, $X'$ (resp. $Y'$) a closed subprescheme of $X$ (resp. $Y$)
defined by a quasi-coherent sheaf of ideals $\mathcal{J}$ (resp. $\mathcal{K}$) of $\mathcal{O}_{X}$ (resp.
$\mathcal{O}_{Y}$). Suppose that $X'$ is reduced and that $f(X') \subset Y'$. Then one has
$f^{*}(\mathcal{K})\mathcal{O}_{X} \subset \mathcal{J}$.

**Proof.** Since the restriction of $f$ to $X'$ factors as $X' \to Y' \to Y$ by (5.2.2), it suffices to apply (4.4.6).

## 5.3. Diagonal; graph of a morphism

<!-- label: I.5.3 -->

**(5.3.1)** Let $X$ be an $S$-prescheme; the _diagonal morphism of $X$ into $X \times_{S} X$_, denoted $\Delta_{X/S}$,
or $\Delta_{X}$, or even $\Delta$ if no confusion is possible, is the $S$-morphism $(1_{X}, 1_{X})_{S}$; in other words,
the unique $S$-morphism $\Delta_{X}$ such that $$ \text{(5.3.1.1)} \qquad p_{1} \circ \Delta_{X} = p_{2} \circ
\Delta_{X} = 1_{X}, $$ $p_{1}$, $p_{2}$ denoting the projections of $X \times_{S} X$ (def. (3.2.1)). If $f : T \to X$,
$g : T \to Y$ are two $S$-morphisms, one verifies at once that $$ \text{(5.3.1.2)} \qquad (f, g)_{S} = (f \times_{S} g)
\circ \Delta_{T/S}. $$

The reader will observe that the preceding definition and the results stated in nos. (5.3.1) to (5.3.8) are valid in any
category, provided that the products appearing in them exist in this category.

**Proposition (5.3.2).** Let $X$, $Y$ be two $S$-preschemes; if one canonically identifies the product $(X \times Y)
\times (X \times Y)$ with $(X \times X) \times (Y \times Y)$, the morphism $\Delta_{X \times Y}$ is identified with
$\Delta_{X} \times \Delta_{Y}$.

**Proof.** Indeed, if $p_{1}$, $q_{1}$ are the first projections $X \times X \to X$, $Y \times Y \to Y$, the first
projection $(X \times Y) \times (X \times Y) \to X \times Y$ is identified with $p_{1} \times q_{1}$, and one has $$
(p_{1} \times q_{1}) \circ (\Delta_{X} \times \Delta_{Y}) = (p_{1} \circ \Delta_{X}) \times (q_{1} \circ \Delta_{Y}) =
1_{X \times Y}; $$ the same reasoning applies for the second projections.

**Corollary (5.3.4).** For every extension $S' \to S$ of the base prescheme, $\Delta_{X_{(S')}}$ is canonically
identified with $(\Delta_{X})_{(S')}$.

**Proof.** It suffices to remark that $(X \times_{S} X)_{(S')}$ is canonically identified with $X_{(S')} \times_{S'}
X_{(S')}$ (3.3.10).

**Proposition (5.3.5).** Let $X$, $Y$ be two $S$-preschemes, $\varphi : S \to T$ a morphism, making of every $S$-prescheme
a $T$-prescheme. Let $f : X \to S$, $g : Y \to S$ be the structure morphisms, $p$, $q$ the projections of $X \times_{S}
Y$, $\pi = f \circ p = g \circ q$ the structure morphism $X \times_{S} Y \to S$. Then the diagram
$$
\text{(5.3.5.1)} \qquad
\begin{array}{ccc}
X \times_{S} Y & \xrightarrow{(p, q)_{T}} & X \times_{T} Y \\
{\scriptstyle \pi}\downarrow & & \downarrow{\scriptstyle f \times_{T} g} \\
S & \xrightarrow{\Delta_{S/T}} & S \times_{T} S
\end{array}
$$
is commutative, and identifies $X \times_{S} Y$ with the product of the $(S \times_{T} S)$-preschemes $S$ and $X
\times_{T} Y$, the projections being identified with $\pi$ and $(p, q)_{T}$.

**Proof.** By virtue of (3.4.3), one is reduced to proving the corresponding proposition in the category of sets, by
replacing $X$, $Y$, $S$ with $X(Z)_{T}$, $Y(Z)_{T}$, $S(Z)_{T}$, $Z$ being an arbitrary $T$-prescheme. But for the
category of sets, the verification is immediate and left to the reader.

**Corollary (5.3.6).** The morphism $(p, q)_{T}$ is identified (setting $P = S \times_{T} S$) with $1_{X \times_{T} Y}
\times_{P} \Delta_{S}$.

**Proof.** This follows from (5.3.5) and (3.3.4).

**Corollary (5.3.7).** If $f : X \to Y$ is an $S$-morphism, the diagram
$$
\begin{array}{ccc}
X & \xrightarrow{(1_{X}, f)_{S}} & X \times_{S} Y \\
{\scriptstyle f}\downarrow & & \downarrow{\scriptstyle f \times_{S} 1_{Y}} \\
Y & \xrightarrow{\Delta_{Y}} & Y \times_{S} Y
\end{array}
$$
is commutative, and identifies $X$ with the product of the $(Y \times_{S} Y)$-preschemes $Y$ and $X \times_{S} Y$.

**Proof.** It suffices to apply (5.3.5), replacing $S$ by $Y$ and $T$ by $S$, and remarking that $X \times_{Y} Y = X$
(3.3.3).

**Proposition (5.3.8).** For $f : X \to Y$ to be a monomorphism of preschemes, it is necessary and sufficient that
$\Delta_{X/Y}$ be an isomorphism of $X$ onto $X \times_{Y} X$.

**Proof.** Indeed, to say that $f$ is a monomorphism means that for every $Y$-prescheme $Z$, the corresponding map $f' :
X(Z)_{Y} \to Y(Z)_{Y}$ is an injection, and since $Y(Z)_{Y}$ is reduced to a single element, this means that the same is
true of $X(Z)_{Y}$. But this is also expressed by saying that $X(Z)_{Y} \times X(Z)_{Y}$ is canonically isomorphic to
$X(Z)_{Y}$, and the first of these sets being $(X \times_{Y} X)(Z)_{Y}$ (3.4.3.1), this means that $\Delta_{X/Y}$ is an
isomorphism.

**Proposition (5.3.9).** The diagonal morphism $\Delta_{X}$ is an immersion of $X$ into $X \times_{S} X$.

**Proof.** Indeed, since the continuous maps $p_{1}$ and $\Delta_{X}$ of the underlying spaces are such that $p_{1}
\circ \Delta_{X}$ is the identity, $\Delta_{X}$ is a homeomorphism of $X$ onto $\Delta_{X}(X)$. Likewise, the composite
homomorphism $\mathcal{O}_{X} \to \mathcal{O}_{\Delta_{X}(x)} \to \mathcal{O}_{x}$ of the homomorphisms corresponding to
$p_{1}$ and to $\Delta_{X}$ being the identity, the homomorphism corresponding to $\Delta_{X}$ is surjective; the
proposition thus follows from (4.2.2).

One says that the subprescheme of $X \times_{S} X$ associated with the immersion $\Delta_{X}$ (4.2.1) is the _diagonal
of $X \times_{S} X$_.

**Corollary (5.3.10).** Under the hypotheses of (5.3.5), $(p, q)_{T}$ is an immersion.

**Proof.** This follows from (5.3.6) and (4.3.1).

One says (under the hypotheses of (5.3.5)) that $(p, q)_{T}$ is the _canonical immersion of $X \times_{S} Y$ into $X
\times_{T} Y$_.

**Corollary (5.3.11).** Let $X$, $Y$ be two $S$-preschemes, $f : X \to Y$ an $S$-morphism; then the graph morphism
$\Gamma_{f} = (1_{X}, f)_{S}$ of $f$ (3.3.14) is an immersion of $X$ into $X \times_{S} Y$.

**Proof.** This is the particular case of cor. (5.3.10) where one replaces $S$ by $Y$ and $T$ by $S$ (cf. (5.3.7)).

The subprescheme of $X \times_{S} Y$ associated with the immersion $\Gamma_{f}$ (4.2.1) is called the _graph of the
morphism $f$_; the subpreschemes of $X \times_{S} Y$ which are graphs of morphisms $X \to Y$ are characterized by the
fact that the restriction to such a subprescheme $G$ of the projection $p_{1} : X \times_{S} Y \to X$ is an isomorphism
$g$ of $G$ onto $X$: $G$ is then the graph of the morphism $p_{2} \circ g^{-1}$, where $p_{2}$ is the projection $X
\times_{S} Y \to Y$.

When one takes in particular $X = S$, the $S$-morphisms $S \to Y$, which are none other than the $S$-sections of $Y$
(2.5.5), are equal to their graph morphisms; the subpreschemes of $Y$ which are graphs of $S$-sections (in other words,
those which are isomorphic to $S$ by the restriction of the structure morphism $Y \to S$) are still called the _images_
of these sections, or, by abuse of language, the _$S$-sections of $Y$_.

**Corollary (5.3.12).** The hypotheses and notations being those of (5.3.11), for every morphism $g : S' \to S$, let
$f'$ be the inverse image of $f$ by $g$ (3.3.7); then $\Gamma_{f'}$ is the inverse image of $\Gamma_{f}$ by $g$.

**Proof.** This is a particular case of formula (3.3.10.1).

**Corollary (5.3.13).** Let $f : X \to Y$, $g : Y \to Z$ be two morphisms; if $g \circ f$ is an immersion (resp. a local
immersion), then so is $f$.

**Proof.** Indeed, $f$ factors as $X \xrightarrow{\Gamma_{f}} X \times_{Z} Y \xrightarrow{p_{2}} Y$. On the other hand,
$p_{2}$ is identified with $(g \circ f) \times_{Z} 1_{Y}$ (3.3.4); if $g \circ f$ is an immersion (resp. a local
immersion), then so is $p_{2}$ (4.3.1 and 4.5.5), and since $\Gamma_{f}$ is an immersion (5.3.11), one concludes by
(4.2.4) (resp. (4.5.5)).

**Corollary (5.3.14).** Let $j : X \to Y$, $g : X \to Z$ be two $S$-morphisms. If $j$ is an immersion (resp. a local
immersion), then so is $(j, g)_{S}$.

**Proof.** Indeed, if $p : Y \times_{S} Z \to Y$ is the first projection, one has $j = p \circ (j, g)_{S}$, and it
suffices to apply (5.3.13).

**Proposition (5.3.15).** If $f : X \to Y$ is an $S$-morphism, the diagram
$$
\text{(5.3.15.1)} \qquad
\begin{array}{ccc}
X & \xrightarrow{\Delta_{X}} & X \times_{S} X \\
{\scriptstyle f}\downarrow & & \downarrow{\scriptstyle f \times_{S} f} \\
Y & \xrightarrow{\Delta_{Y}} & Y \times_{S} Y
\end{array}
$$
is commutative (in other words $\Delta_{X}$ is a functorial morphism in the category of preschemes).

**Proof.** The verification is immediate and left to the reader.

**Corollary (5.3.16).** If $X$ is a subprescheme of $Y$, the diagonal $\Delta_{X}(X)$ is identified with a subprescheme
of $\Delta_{Y}(Y)$, whose underlying space is identified with $$ \Delta_{Y}(Y) \cap p_{1}^{-1}(X) = \Delta_{Y}(Y) \cap
p_{2}^{-1}(X) $$ ($p_{1}$, $p_{2}$ projections of $Y \times_{S} Y$).

**Proof.** Apply (5.3.15) to the injection morphism $f : X \to Y$; one knows then that $f \times_{S} f$ is an immersion,
identifying the underlying space of $X \times_{S} X$ with the subspace $p_{1}^{-1}(X) \cap p_{2}^{-1}(X)$ of $Y
\times_{S} Y$ (4.3.1); moreover, if $z \in \Delta_{Y}(Y) \cap p_{1}^{-1}(X)$, one has $z = \Delta_{Y}(y)$ and $y =
p_{1}(z) \in X$, so $y = f(y)$, and $z = \Delta_{Y}(f(y))$ belongs to $\Delta_{X}(X)$ by virtue of the commutativity of
the diagram (5.3.15.1).

**Corollary (5.3.17).** Let $f_{1} : Y \to X$, $f_{2} : Y \to X$ be two $S$-morphisms, $y$ a point of $Y$ such that
$f_{1}(y) = f_{2}(y) = x$ and such that the homomorphisms $\kappa(x) \to \kappa(y)$ corresponding to $f_{1}$ and $f_{2}$
are identical. Then, if $f = (f_{1}, f_{2})_{S}$, the point $f(y)$ belongs to the diagonal $\Delta_{X/S}(X)$.

**Proof.** The two homomorphisms $\kappa(x) \to \kappa(y)$ corresponding to $f_{i}$ ($i = 1, 2$) define two $S$-morphisms
$g_{i} : \operatorname{Spec}(\kappa(y)) \to \operatorname{Spec}(\kappa(x))$ such that the diagrams
$$
\begin{array}{ccc}
\operatorname{Spec}(\kappa(y)) & \xrightarrow{g_{i}} & \operatorname{Spec}(\kappa(x)) \\
\downarrow & & \downarrow \\
Y & \xrightarrow{f_{i}} & X
\end{array}
$$
are commutative. The diagram
$$
\begin{array}{ccc}
\operatorname{Spec}(\kappa(y)) & \xrightarrow{(g_{1}, g_{2})_{S}} & \operatorname{Spec}(\kappa(x)) \times_{S} \operatorname{Spec}(\kappa(x)) \\
\downarrow & & \downarrow \\
Y & \xrightarrow{(f_{1}, f_{2})_{S}} & X \times_{S} X
\end{array}
$$
is therefore also commutative. Now it follows from the equality $g_{1} = g_{2}$ that the image under $(g_{1}, g_{2})_{S}$
of the unique point of $\operatorname{Spec}(\kappa(y))$ belongs to the diagonal of $\operatorname{Spec}(\kappa(x))
\times_{S} \operatorname{Spec}(\kappa(x))$; the conclusion thus follows from (5.3.15).

## 5.4. Separated morphisms and separated preschemes

<!-- label: I.5.4 -->

**Definition (5.4.1).** One says that a morphism of preschemes $f : X \to Y$ is _separated_ if the diagonal morphism $X
\to X \times_{Y} X$ is a closed immersion; one also says then that $X$ is a _prescheme separated over $Y$_, or a
_$Y$-scheme_. One says that a prescheme $X$ is _separated_ if it is separated over $\operatorname{Spec}(\mathbb{Z})$;
one also says then that $X$ is a _scheme_ (cf. (5.5.7)).

By virtue of (5.3.9), for $X$ to be separated over $Y$, it is necessary and sufficient that $\Delta_{X}(X)$ be a closed
subspace of the underlying space of $X \times_{Y} X$.

**Proposition (5.4.2).** Let $S \to T$ be a separated morphism. If $X$ and $Y$ are two $S$-preschemes, the canonical
immersion $X \times_{S} Y \to X \times_{T} Y$ (5.3.10) is closed.

**Proof.** Indeed, referring to the diagram (5.3.5.1), one sees that $(p, q)_{T}$ can be considered as obtained from
$\Delta_{S/T}$ by the extension $f \times_{T} g : X \times_{T} Y \to S \times_{T} S$ of the base prescheme $S \times_{T}
S$; the proposition then follows from (4.3.2).

**Corollary (5.4.3).** Let $Y$ be an $S$-scheme, $f : X \to Y$ an $S$-morphism. Then the graph morphism $\Gamma_{f} : X
\to X \times_{S} Y$ (5.3.11) is a closed immersion.

**Proof.** This is the particular case of (5.4.2) where one replaces $S$ by $Y$ and $T$ by $S$.

**Corollary (5.4.4).** Let $f : X \to Y$, $g : Y \to Z$ be two morphisms, $g$ being separated. If $g \circ f$ is a
closed immersion, then so is $f$.

**Proof.** The proof from (5.4.3) is the same as that of (5.3.13) from (5.3.11).

**Corollary (5.4.5).** Let $Z$ be an $S$-scheme, $j : X \to Y$, $g : X \to Z$ two $S$-morphisms. If $j$ is a closed
immersion, then so is $(j, g)_{S} : X \to Y \times_{S} Z$.

**Proof.** The proof from (5.4.4) is the same as that of (5.3.14) from (5.3.13).

**Corollary (5.4.6).** If $X$ is an $S$-scheme, every $S$-section of $X$ (2.5.5) is a closed immersion.

**Proof.** If $\varphi : X \to S$ is the structure morphism, $\psi : S \to X$ an $S$-section of $X$, it suffices to
apply (5.4.5) to $\varphi \circ \psi = 1_{S}$.

**Corollary (5.4.7).** Let $S$ be an integral prescheme, $s$ its generic point, $X$ an $S$-scheme. If two $S$-sections
$f$, $g$ of $X$ are such that $f(s) = g(s)$, then $f = g$.

**Proof.** Indeed, if $x = f(s) = g(s)$, the homomorphisms $\kappa(x) \to \kappa(s)$ corresponding to $f$ and $g$ are
necessarily identical. If $h = (f, g)_{S}$, one deduces (5.3.17) that $h(s)$ belongs to the diagonal $Z =
\Delta_{X}(X)$; but since $S = \overline{\{s\}}$ and $Z$ is closed by hypothesis, one has $h(S) \subset Z$. It then
follows from (5.2.2) that $h$ factors as $S \to Z \to X \times_{S} X$, and one concludes that $f = g$ by definition of
the diagonal.

**Remark (5.4.8).** If one supposes conversely that the conclusion of (5.4.3) is verified when $f = 1_{Y}$, one
concludes that $Y$ is separated over $S$; likewise, if one supposes that the conclusion of (5.4.5) applies to the two
morphisms $Y \to Y \times_{S} Y \to Y$, one deduces that $\Delta_{Y}$ is a closed immersion, so that $Y$ is separated
over $Z$; finally, the validity of the conclusion of (5.4.6) for the $Y$-section $\Delta_{Y}$ of the $Y$-prescheme $Y
\times_{S} Y \to Y$ implies that $Y$ is separated over $S$.

## 5.5. Separation criteria

<!-- label: I.5.5 -->

**Proposition (5.5.1).** (i) Every monomorphism of preschemes (and in particular every immersion) is a separated
morphism.

(ii) The composite of two separated morphisms is separated.

(iii) If $f : X \to X'$, $g : Y \to Y'$ are two separated $S$-morphisms, $f \times_{S} g$ is separated.

(iv) If $f : X \to Y$ is a separated $S$-morphism, the $S'$-morphism $f_{(S')}$ is separated for every extension $S' \to
S$ of the base prescheme.

(v) If the composite $g \circ f$ of two morphisms is separated, $f$ is separated.

(vi) For a morphism $f$ to be separated, it is necessary and sufficient that $f_{\mathrm{red}}$ (5.1.5) be so.

**Proof.** (i) follows at once from (5.3.8). If $f : X \to Y$, $g : Y \to Z$ are two morphisms, the diagram
$$
\text{(5.5.1.1)} \qquad
\begin{array}{ccc}
X & \xrightarrow{\Delta_{X/Z}} & X \times_{Z} X \\
{\scriptstyle \Delta_{X/Y}}\searrow & & \nearrow{\scriptstyle j} \\
& X \times_{Y} X &
\end{array}
$$
where $j$ denotes the canonical immersion (5.3.10), is commutative, as one verifies at once. If $f$ and $g$ are
separated, $\Delta_{X/Y}$ is a closed immersion by definition, and $j$ is a closed immersion by virtue of (5.4.2), so
$\Delta_{X/Z}$ is a closed immersion by (4.2.4), which proves (ii). Given (i) and (ii), (iii) and (iv) are equivalent
(3.5.1), and it suffices to prove (iv). Now $X_{(S')} \times_{Y_{(S')}} X_{(S')}$ is canonically identified with $(X
\times_{Y} X) \times_{Y} Y_{(S')}$ by virtue of (3.3.11) and (3.3.9.1), and one verifies at once that the diagonal
morphism $\Delta_{X_{(S')}}$ is then identified with $\Delta_{X} \times_{Y} 1_{Y_{(S')}}$; the proposition thus follows
from (4.3.1).

To establish (v), consider, as in (5.3.13), the factorization $X \xrightarrow{\Gamma_{f}} X \times_{Z} Y
\xrightarrow{p_{2}} Y$ of $f$, remarking that $p_{2} = (g \circ f) \times_{Z} 1_{Y}$; the hypothesis that $g \circ f$ is
separated entails that $p_{2}$ is separated by (iii) and (i), and since $\Gamma_{f}$ is an immersion, $\Gamma_{f}$ is
separated by (i), so $f$ is separated by (ii). Finally, to prove (vi), recall that the preschemes $X_{\mathrm{red}}
\times_{Y_{\mathrm{red}}} X_{\mathrm{red}}$ and $X_{\mathrm{red}} \times_{Y} X_{\mathrm{red}}$ are canonically identified
(5.1.7); if one denotes by $j$ the injection $X_{\mathrm{red}} \to X$, the diagram
$$
\begin{array}{ccc}
X_{\mathrm{red}} & \xrightarrow{\Delta_{X_{\mathrm{red}}}} & X_{\mathrm{red}} \times_{Y} X_{\mathrm{red}} \\
{\scriptstyle j}\downarrow & & \downarrow{\scriptstyle j \times_{Y} j} \\
X & \xrightarrow{\Delta_{X}} & X \times_{Y} X
\end{array}
$$
is commutative (5.3.15), and the proposition follows from the fact that the vertical arrows are homeomorphisms of the
underlying spaces (4.3.1).

**Corollary (5.5.2).** If $f : X \to Y$ is separated, the restriction of $f$ to every subprescheme of $X$ is separated.

**Proof.** This follows from (5.5.1, (i) and (ii)).

**Corollary (5.5.3).** If $X$, $Y$ are two $S$-preschemes such that $Y$ is separated over $S$, $X \times_{S} Y$ is
separated over $X$.

**Proof.** This is a particular case of (5.5.1, (iv)).

**Proposition (5.5.4).** Let $X$ be a prescheme, and suppose that its underlying space is the union of a finite family
of closed parts $X_{k}$ ($1 \le k \le n$); for each $k$ one considers the reduced subprescheme of $X$ having $X_{k}$ as
underlying space (5.2.1) and one denotes it again by $X_{k}$. Let $f : X \to Y$ be a morphism, and for each $k$, let
$Y_{k}$ be a closed part of $Y$ such that $f(X_{k}) \subset Y_{k}$; one denotes again by $Y_{k}$ the reduced
subprescheme of $Y$ having $Y_{k}$ as underlying space, so that the restriction $X_{k} \to Y$ of $f$ to $X_{k}$ factors
as $X_{k} \xrightarrow{f_{k}} Y_{k} \to Y$ (5.2.2). For $f$ to be separated, it is necessary and sufficient that the
$f_{k}$ be so.

**Proof.** The necessity follows from (5.5.1, (i), (ii) and (v)). Conversely, if the condition of the statement is
satisfied, each of the restrictions $X_{k} \to Y$ of $f$ is separated (5.5.1, (i) and (ii)); if $p_{1}$, $p_{2}$ are the
projections of $X \times_{Y} X$, the subspace $\Delta_{X_{k}}(X_{k})$ is identified with the subspace $\Delta_{X}(X)
\cap p_{1}^{-1}(X_{k})$ of the underlying space of $X \times_{Y} X$ (5.3.16); these subspaces being closed in $X
\times_{Y} X$, the same is true of their union $\Delta_{X}(X)$.

Suppose in particular that the $X_{k}$ are the irreducible components of $X$; one may then suppose that the $Y_{k}$ are
irreducible components of $Y$ (0, 2.1.5); prop. (5.5.4) thus reduces in this case the notion of separation to the case
of integral preschemes (2.1.7).

**Proposition (5.5.5).** Let $(Y_{\lambda})$ be an open cover of a prescheme $Y$; for a morphism $f : X \to Y$ to be
separated, it is necessary and sufficient that each of its restrictions $f^{-1}(Y_{\lambda}) \to Y_{\lambda}$ be
separated.

**Proof.** If we set $X_{\lambda} = f^{-1}(Y_{\lambda})$, everything comes down, taking account of (4.2.4, b)) and of
the identity of the products $X_{\lambda} \times_{Y} X_{\lambda}$ and $X_{\lambda} \times_{Y_{\lambda}} X_{\lambda}$
(3.2.5), to proving that the $X_{\lambda} \times_{Y} X_{\lambda}$ form a cover of $X \times_{Y} X$. Now if one sets
$Y_{\lambda\mu} = Y_{\lambda} \cap Y_{\mu}$ and $X_{\lambda\mu} = X_{\lambda} \cap X_{\mu} = f^{-1}(Y_{\lambda\mu})$,
$X_{\lambda} \times_{Y} X_{\mu}$ is identified with the product $X_{\lambda\mu} \times_{Y_{\lambda\mu}} X_{\lambda\mu}$
(3.2.6.4), so also with $X_{\lambda\mu} \times_{Y} X_{\lambda\mu}$ (3.2.5), and finally with an open of $X_{\lambda}
\times_{Y} X_{\lambda}$, which establishes our assertion (3.2.7).

Prop. (5.5.4) allows, by taking a cover of $Y$ by affine opens, to reduce the study of separated morphisms to that of
separated morphisms with values in affine schemes.

**Proposition (5.5.6).** Let $Y$ be an affine scheme, $X$ a prescheme, $(U_{\alpha})$ a cover of $X$ by affine opens.
For a morphism $f : X \to Y$ to be separated, it is necessary and sufficient that, for every pair of indices $(\alpha,
\beta)$, $U_{\alpha} \cap U_{\beta}$ be an affine open, and that the ring $\Gamma(U_{\alpha} \cap U_{\beta},
\mathcal{O}_{X})$ be generated by the union of the canonical images of the rings $\Gamma(U_{\alpha}, \mathcal{O}_{X})$
and $\Gamma(U_{\beta}, \mathcal{O}_{X})$.

**Proof.** The $U_{\alpha} \times_{Y} U_{\beta}$ form an open cover of $X \times_{Y} X$ (3.2.7); denoting by $p$ and $q$
the projections of $X \times_{Y} X$, one has $$ \Delta_{X}^{-1}(U_{\alpha} \times_{Y} U_{\beta}) =
\Delta_{X}^{-1}(p^{-1}(U_{\alpha}) \cap q^{-1}(U_{\beta})) = \Delta_{X}^{-1}(p^{-1}(U_{\alpha})) \cap
\Delta_{X}^{-1}(q^{-1}(U_{\beta})) = U_{\alpha} \cap U_{\beta}; $$ everything thus comes down to expressing that the
restriction of $\Delta_{X}$ to $U_{\alpha} \cap U_{\beta}$ is a closed immersion into $U_{\alpha} \times_{Y} U_{\beta}$.
Now this restriction is none other than $(j_{\alpha}, j_{\beta})_{Y}$, denoting by $j_{\alpha}$ (resp. $j_{\beta}$) the
injection morphism of $U_{\alpha} \cap U_{\beta}$ into $U_{\alpha}$ (resp. $U_{\beta}$), as follows from the
definitions. Since $U_{\alpha} \times_{Y} U_{\beta}$ is an affine scheme whose ring is canonically isomorphic to
$\Gamma(U_{\alpha}, \mathcal{O}_{X}) \otimes_{\Gamma(Y, \mathcal{O}_{Y})} \Gamma(U_{\beta}, \mathcal{O}_{X})$ (3.2.2),
one sees that $U_{\alpha} \cap U_{\beta}$ must be an affine scheme and that the map $h_{\alpha} \otimes h_{\beta}
\mapsto h_{\alpha} h_{\beta}$ of the ring $A(U_{\alpha} \times_{Y} U_{\beta})$ into $\Gamma(U_{\alpha} \cap U_{\beta},
\mathcal{O}_{X})$ must be surjective (4.2.3), which completes the proof.

**Corollary (5.5.7).** An affine scheme is separated (and is consequently a scheme, which justifies the terminology of
(5.4.1)).

**Corollary (5.5.8).** Let $Y$ be an affine scheme; for $f : X \to Y$ to be a separated morphism, it is necessary and
sufficient that $X$ be separated (in other words, that $X$ be a scheme).

**Proof.** One observes indeed that the criterion of (5.5.6) does not depend on $f$.

**Corollary (5.5.9).** For a morphism $f : X \to Y$ to be separated, it is necessary that for every open $U$ on which
$Y$ induces a separated prescheme, the induced prescheme $f^{-1}(U)$ be separated, and it suffices that this be so for
every affine open $U \subset Y$.

**Proof.** The necessity of the condition follows from (5.5.4) and (5.5.1 (ii)); the sufficiency follows from (5.5.4)
and (5.5.8), taking account of the existence of affine open covers of $Y$.

In particular, if $X$ and $Y$ are affine schemes, every morphism $X \to Y$ is separated.

**Proposition (5.5.10).** Let $Y$ be a scheme, $f : X \to Y$ a morphism. For every affine open $U$ of $X$ and every
affine open $V$ of $Y$, $U \cap f^{-1}(V)$ is affine.

**Proof.** Let $p_{1}$, $p_{2}$ be the projections of $X \times_{Z} Y$; the subspace $U \cap f^{-1}(V)$ is the image
under $p_{1}$ of $\Gamma_{f}(X) \cap p_{1}^{-1}(U) \cap p_{2}^{-1}(V)$. Now $p_{1}^{-1}(U) \cap p_{2}^{-1}(V)$ is
identified with the underlying space of the prescheme $U \times_{Z} V$ (3.2.7), and is consequently an affine scheme
(3.2.2); since $\Gamma_{f}(X)$ is closed in $X \times_{Z} Y$ (5.4.3), $\Gamma_{f}(X) \cap p_{1}^{-1}(U) \cap
p_{2}^{-1}(V)$ is closed in $U \times_{Z} V$, and consequently the prescheme induced by the subprescheme of $X
\times_{Z} Y$ associated with $\Gamma_{f}$ (4.2.1), on the open part $\Gamma_{f}(X) \cap p_{1}^{-1}(U) \cap
p_{2}^{-1}(V)$ of its underlying space, is a closed subprescheme of an affine scheme, hence an affine scheme (4.2.3).
The proposition then follows from the fact that $\Gamma_{f}$ is an immersion.

**Examples (5.5.11).** The prescheme of example (2.3.2) (“projective line over a field $K$”) is separated, for, with the
cover $(X_{1}, X_{2})$ of $X$ by affine opens, $X_{1} \cap X_{2} = U_{12}$ is affine and $\Gamma(U_{12},
\mathcal{O}_{X})$, the ring of rational fractions of the form $f(s)/s^{m}$ with $f \in K[s]$, is generated by $K[s]$ and
by $1/s$, so the conditions of (5.5.6) are verified.

With the same choice of $X_{1}$, $X_{2}$, $U_{12}$ and $U_{21}$ as in example (2.3.2), let us take this time for
$u_{12}$ the isomorphism which to $f(s)$ assigns $f(t)$; one obtains this time by gluing an integral non-separated
prescheme $X$, for the first condition of (5.5.6) is verified, but not the second. It is immediate here that $\Gamma(X,
\mathcal{O}_{X}) \to \Gamma(X_{1}, \mathcal{O}_{X}) = K[s]$ is an isomorphism; the inverse isomorphism defines a
morphism $f : X \to \operatorname{Spec}(K[s])$ which is surjective, and for every $y \in \operatorname{Spec}(K[s])$ such
that $\mathfrak{j}_{y} \neq (0)$, $f^{-1}(y)$ is reduced to a point, but for $\mathfrak{j}_{y} = (0)$, $f^{-1}(y)$
consists of two distinct points (one says that $X$ is the “affine line over $K$, where the point $0$ is doubled”).

One can also give examples where none of the two conditions of (5.5.6) is verified. Let us first remark that in the
prime spectrum $Y$ of the polynomial ring $A = K[s, t]$ in two indeterminates over a field $K$, the open $U$, union of
$D(s)$ and $D(t)$, is not an affine open. Indeed, if $z$ is a section of $\mathcal{O}_{Y}$ over $U$, there exist two
integers $m \ge 0$, $n \ge 0$ such that $s^{m} z$ and $t^{n} z$ are the restrictions to $U$ of polynomials in $s$ and
$t$ (1.4.1), which is evidently possible only if the section $z$ extends to a section over the whole of $Y$, identified
with a polynomial in $s$ and $t$. If $U$ were an affine open, the injection morphism $U \to Y$ would then be an
isomorphism (1.7.3), which is absurd since $U \neq Y$.

This being so, let us take two affine schemes $Y_{1}$, $Y_{2}$, prime spectra of the rings $A_{1} = K[s_{1}, t_{1}]$,
$A_{2} = K[s_{2}, t_{2}]$; let us take $U_{12} = D(s_{1}) \cup D(t_{1})$, $U_{21} = D(s_{2}) \cup D(t_{2})$, and for
$u_{12}$ the restriction to $U_{21}$ of the isomorphism $Y_{2} \to Y_{1}$ corresponding to the isomorphism of rings
which to $f(s_{1}, t_{1})$ assigns $f(s_{2}, t_{2})$; one thus has an example where none of the conditions of (5.5.6) is
satisfied (the integral prescheme thus obtained is called the “affine plane over $K$, where the point $0$ is doubled”).

**Remark (5.5.12).** Given a property $P$ of morphisms of preschemes, consider the following propositions:

(i) Every closed immersion possesses the property $P$.

(ii) The composite of two morphisms possessing the property $P$ possesses the property $P$.

(iii) If $f : X \to X'$, $g : Y \to Y'$ are two $S$-morphisms possessing the property $P$, $f \times_{S} g$ possesses
the property $P$.

(iv) If $f : X \to Y$ is an $S$-morphism possessing the property $P$, every $S'$-morphism $f_{(S')}$ obtained by an
extension $S' \to S$ of the base prescheme possesses the property $P$.

(v) If the composite $g \circ f$ of two morphisms $f : X \to Y$, $g : Y \to Z$ possesses the property $P$, and if $g$ is
separated, $f$ possesses the property $P$.

(vi) If a morphism $f : X \to Y$ possesses the property $P$, then so does $f_{\mathrm{red}}$ (5.1.5).

Under these conditions, if one supposes (i) and (ii) verified, (iii) and (iv) are equivalent, and (v) and (vi) are
consequences of (i), (ii) and (iii).

The first assertion has already been proved (3.5.1). Consider the factorization (5.3.13) of $f$ into $X
\xrightarrow{\Gamma_{f}} X \times_{Z} Y \xrightarrow{p_{2}} Y$; the relation $p_{2} = (g \circ f) \times_{Z} 1_{Y}$
shows that if $g \circ f$ possesses the property $P$, then so does $p_{2}$ by virtue of (iii); if $g$ is separated,
$\Gamma_{f}$ is a closed immersion (5.4.3), and so possesses the property $P$ too by (i); finally, by virtue of (ii),
$f$ possesses the property $P$.

Finally, consider the commutative diagram
$$
\begin{array}{ccc}
X_{\mathrm{red}} & \xrightarrow{f_{\mathrm{red}}} & Y_{\mathrm{red}} \\
\downarrow & & \downarrow \\
X & \xrightarrow{f} & Y
\end{array}
$$
where the vertical arrows are closed immersions (5.1.5), so possess the property $P$ by (i). The hypothesis that $f$
possesses the property $P$ therefore entails by (ii) that $X_{\mathrm{red}} \xrightarrow{f_{\mathrm{red}}}
Y_{\mathrm{red}} \to Y$ possesses the property $P$; finally, since a closed immersion is separated (5.5.1 (i)),
$f_{\mathrm{red}}$ possesses the property $P$ by virtue of (v).

One will note that if one considers the propositions:

(i') Every immersion possesses the property $P$.

(v') If $g \circ f$ possesses the property $P$, then so does $f$;

then the reasoning made above shows that (v') is a consequence of (i'), (ii) and (iii).

**(5.5.13)** One will note that (v) and (vi) are still consequences of (i), (iii) and

(ii') If $j : X \to Y$ is a closed immersion and $g : Y \to Z$ a morphism possessing the property $P$, then $g \circ j$
possesses the property $P$.

Likewise, (v') is a consequence of (i'), (iii) and

(ii'') If $j : X \to Y$ is an immersion and $g : Y \to Z$ a morphism possessing the property $P$, then $g \circ j$
possesses the property $P$.

This follows indeed at once from the reasonings of (5.5.12).

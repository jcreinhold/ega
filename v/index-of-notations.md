# Index of notations — EGA V

Source-ordered, with §V section subheadings. Reused notations from EGA I-IV (e.g. $\mathcal{O}_{X}$, $\Omega^{1}_{X/S}$,
$\operatorname{Pic}(X)$, `Sym`, $\Lambda$, $\mathbb{P}$, `Proj`, `Spec`, $\to$, $\mapsto$, $\otimes$, $\cong$) are not
re-listed here; see $docs/books/ega/iv/index-of-notations.md$.

Note on overloads: the symbol $\mathcal{G}$ denotes the **tangent sheaf** $\mathcal{G}_{X/Y}$ in §V.1 and §V.5.8 (kernel
of the augmentation $\mathcal{P}^{1}_{X/Y} \to \mathcal{O}_{X}$), but is repurposed in §V.6.4.3 as the abstract "tangent
vector space $\mathcal{G}_{w_{0}}$" of a functor at a chosen point; the same glyph carries two distinct meanings.
Similarly the symbol $\mathcal{P}$ denotes the **sheaf of principal parts** $\mathcal{P}^{n}_{X/Y}$ in §V.1 and a
generic **projective fibration** in §V.5.15; context distinguishes. The notation $(S_{n})$ denotes both Serre's depth
condition (§V.5.2.8) and a $\mathbb{Z}$-indexed open partition of the base (§V.6.1.1); we attach the subscript range
$(S_{n})_{n \in \mathbb{Z}}$ when ambiguity could arise.

## §V.1. Singular and supersingular zeros

- $\mathfrak{m}_{x}$, $\mathfrak{m}^{2}_{x}$, $\mathfrak{m}_{x} / \mathfrak{m}^{2}_{x}$ — maximal ideal of
  $\mathcal{O}_{X,x}$, its square, and the Zariski cotangent space. `(V, 1.1)`
- $t_{x}$ — dual of $\mathfrak{m}_{x} / \mathfrak{m}^{2}_{x}$ over $k(x)$ (Zariski tangent space). `(V, 1.1)`
- $Sym^{2}(\mathfrak{m}_{x} / \mathfrak{m}^{2}_{x})$ — module of quadratic forms on $t_{x}$. `(V, 1.1)`
- $V(\phi)$ — zero set / subscheme of zeros of a section $\phi$. `(V, 1.1)`, `(V, 1.5)`
- $V(\phi)_{sing}$ — singular zeros of $\phi$ (relative to $Y$). `(V, 1.5)`
- $V(\phi)_{supsing}$ — supersingular zeros of $\phi$ (relative to $Y$). `(V, 1.5)`
- $\phi_{k'}$, $X_{k'}$ — base change of $\phi$ and of $X$ along $k \to k'$. `(V, 1.3)`
- $d^{0}\phi = \phi$ — order-`0` principal-parts truncation. `(V, 1.5)`
- $d^{1}_{X/Y} \phi$ — order-`1` truncation. `(V, 1.5)`
- $d^{2}_{X/Y} \phi$ — order-`2` truncation. `(V, 1.5)`
- $d_{X/Y} \phi$ — universal differential of $\phi$ (restriction of $d^{1}\phi$ to $V(\phi)$). `(V, 1.5)`
- $\mathcal{P}^{n}_{X/Y}$ — sheaf of principal parts of order $n$ (cf. $(0_{IV}, 20.4.14)$). `(V, 1.5)`
- $gr^{1}(\mathcal{P}^{1}_{X/Y}) \cong \Omega^{1}_{X/Y}$ — first graded piece. `(V, 1.5)`
- $gr^{2}(\mathcal{P}^{2}_{X/Y}) \cong Sym^{2}(\Omega^{1}_{X/Y})$ — second graded piece. `(V, 1.5)`
- $M(\phi)$ — canonical section of $Sym^{2}(\Omega^{1}_{X/Y}) \otimes \mathcal{O}_{V(\phi)_{sing}}$; quadratic form on
  the cotangent space. `(V, 1.5)`
- $M(\phi)'$ — homomorphism $\mathcal{G}_{X/Y} \otimes \mathcal{O}_{V(\phi)_{sing}} \to \Omega^{1}_{X/Y} \otimes
  \mathcal{O}_{V(\phi)_{sing}}$ deduced from $M(\phi)$. `(V, 1.5)`
- $D(\phi) = det M(\phi)$ — discriminant of $M(\phi)$; section of $\Gamma(\Omega^{d}_{X/Y})^{\otimes 2} \otimes
  \mathcal{O}_{V(\phi)_{sing}}$. `(V, 1.5)`
- $\mathcal{G}_{X/Y}$ — tangent sheaf; kernel of $\mathcal{P}^{1}_{X/Y} \to \mathcal{O}_{X}$. `(V, 1.5)`, footnote
  $[{}^{v}-1-3]$
- $V' = V(\phi)_{sing}$ — abbreviation in §V.1.7. `(V, 1.7)`
- $\mu$, $\nu$ — composed homomorphisms in the §V.1.7 diagram. `(V, 1.7)`
- $Ram(V'/Y)$ — ramification subprescheme of $V'$ relative to $Y$. `(V, 1.7)`
- `det F` — highest exterior power of a locally free module $F$ of finite rank. `(V, 1.8)`
- $\Lambda^{q} Q$, $\Lambda^{r} M$ — exterior powers used to detect non-surjectivity loci. `(V, 1.7)`
- `L = det P ⊗ det Q ⊗ det M^{−1}` — line bundle in the §V.1.8 lemma. `(V, 1.8)`

## §V.2.15-§V.2.16. Smooth forms; smooth quadratic forms

- $\mathbb{P}(E)$, $P = \mathbb{P}(E)$ — projective fibration. `(V, 2.15.1)`
- $\mathcal{O}_{P}(n)$ — Serre twist on $P$. `(V, 2.15.1)`
- $Sym^{n}(E)$ — $n$-th symmetric power. `(V, 2.15.1)`
- $V(\phi) \subset P$ — subscheme of zeros of an $n$-form. `(V, 2.15.1)`
- $\mathcal{J}$, $\mathcal{O}_{X}/\mathcal{J}$ — ideal and quotient sheaf in an augmentation. `(V, 2.15.2)`
- $\mathcal{N}_{X/Y} = \mathcal{J}/\mathcal{J}^{2}$ — conormal module of $Y = V(\mathcal{J})$ in $X$. `(V, 2.15.2)`
- $\Psi : Sym_{\mathcal{O}_{Y}}(\mathcal{N}) \to gr_{\mathcal{J}}(\mathcal{O}_{X})$ — canonical surjection on the
  associated graded ring. `(V, 2.15.2)`
- $\mathcal{K} = \ker(\Psi_{n})$ — kernel in degree $n$ (invertible submodule of
  $Sym^{n}_{\mathcal{O}_{Y}}(\mathcal{N})$). `(V, 2.15.2)`
- $r(A)$ — radical / maximal ideal of a local ring. `(V, 2.15.2)`
- $d^{n} \phi$ — order-$n$ principal part of $\phi$. `(V, 2.15.7)`
- $I$ — augmentation ideal of $\mathcal{P}^{n}_{X'/k} \otimes k(x)$. `(V, 2.15.7)`
- $Q \in Sym^{2}(E)$ — quadratic form. `(V, 2.16.1)`
- $B$ — symmetric bilinear form on $E^{\vee}$ associated to $Q$. `(V, 2.16.1)`
- $d(Q) \in \Gamma(det(E)^{\otimes 2})$ — ordinary discriminant. `(V, 2.16.1)`
- $N \subset E^{\vee}$ — "kernel" of the alternating bilinear form in characteristic 2. `(V, 2.16.2)`
- $Q_{n}$, $Q_{2m}$, $Q_{2m+1}$ — standard quadratic forms in $n$, `2m`, $2m+1$ variables. `(V, 2.16.4)`
- $\tilde{d}(Q)$ — corrected (adjusted) discriminant of $Q$. `(V, 2.16.6)`, `(V, 2.16.7)`
- $\mathbb{V}(\cdot)$ — vector-bundle functor associated to a locally free sheaf. `(V, 2.16.3)`, `(V, 2.16.11)`
- $Isom((E_{0}, Q_{0}), (E, Q))$ — functor of isometries. `(V, 2.16.11)`
- $Isom(E_{0}, E)$ — functor of isomorphisms of locally free modules. `(V, 2.16.11)`
- $\mathcal{Q}(E) = \mathbb{V}(Sym^{2}(E))$ — affine bundle of quadratic forms. `(V, 2.16.11)`
- $\mathcal{Q}(E)* = \mathcal{Q}(E)_{\tilde{d}}$ — open subset of smooth (i.e. $\tilde{d}$-invertible) quadratic forms.
  `(V, 2.16.11)`
- $O(n)$ — absolute orthogonal group (stabilizer of $Q_{n}$ in $\operatorname{Aut}(\mathbb{Z}^{n})$). `(V, 2.16.12)`
- $O(Q)$ — orthogonal group scheme relative to $Q$. `(V, 2.16.12)`
- $SO(n)$ — special orthogonal subgroup. `(V, 2.16.14)`
- $\mu_{2,S}$ — group scheme of square roots of unity over $S$. `(V, 2.16.14)`

## §V.5.1. Hyperplane sections — preliminaries and notation

- $P = \mathbb{P}(E)$ — projective fibration. `(V, 5.1)`
- $P^{\vee} = \mathbb{P}(E^{\vee})$ — scheme of hyperplanes (dual projective fibration). `(V, 5.1)`
- $L$, `L_P`, $L^{-1}_{P}$ — invertible quotient / submodule used to define a hyperplane. `(V, 5.1)`
- $H_{\xi}$ — hyperplane in $P$ defined by $\xi \in P^{\vee}(S)$. `(V, 5.1)`
- $H$ — universal / incidence hyperplane in $P \times_{S} P^{\vee}$. `(V, 5.1)`
- $\operatorname{Div}(P/S)$ — functor of relative divisors of $P/S$. `(V, 5.1.1)`
- $f : X \to P$ — projective immersion / unramified morphism. `(V, 5.1)`
- $Y_{\xi} = f^{-1}(H_{\xi})$ — hyperplane section associated to $\xi$. `(V, 5.1)`
- $Y = X \times_{P} H$ — total hyperplane section over $P^{\vee}$. `(V, 5.1)`
- $F$, $G_{\xi}$, $G$ — sheaf on $X$ and its inverse images on $Y_{\xi}$, $Y$. `(V, 5.1)`

## §V.5.2-§V.5.3. Generic hyperplane section

- $\eta$ — generic point of $P^{\vee}$. `(V, 5.2)`
- $H_{\eta}$, $Y_{\eta}$, $G_{\eta}$ — hyperplane, hyperplane section, sheaf at $\eta$. `(V, 5.2)`
- $Z_{\eta}$ — inverse image of $Z \subset P$ in $H_{\eta}$. `(V, 5.2.2)`
- $Y_{i,\eta}$ — irreducible component of $Y_{\eta}$. `(V, 5.2.5)`
- $coprof_{y} G$ — codepth of $G$ at $y$. `(V, 5.2.8)`
- $(S_{k})$, $(R_{k})$ — Serre's depth and regularity conditions. `(V, 5.2.8)`, `(V, 5.2.11)`
- $K$, $L$ — function fields of $X$ and $Y_{\eta}$. `(V, 5.3.1)`
- $S_{1}, \cdots, S_{n}$ — affine coordinates in $P^{\vee}$. `(V, 5.3.1)`
- $T_{1}, \cdots, T_{n}$ — affine coordinates in $P$. `(V, 5.3.1)`
- $t_{i} \in K$ — image of $T_{i}$ under $f : X \to P$. `(V, 5.3.1)`
- $(C_{m})$ — non-disconnect-by-codimension-$m$ property. `(V, 5.4.4)`

## §V.5.4-§V.5.5. Variable hyperplane sections; Seidenberg-type theorems

- $E$ — set of $\xi \in P^{\vee}$ such that $Y_{\xi}$ has a given property. `(V, 5.4)`
- `Z_P` — set of $\xi \in P^{\vee}$ exceptional for property $P$. `(V, 5.8.1)`
- $\phi_{\xi}$ — section of $\mathcal{O}_{X}(1) \otimes \mathcal{O}_{P^{\vee}}(1)(\xi)$ defining $Y_{\xi}$. `(V, 5.5.2)`
- $U$, `U_P`, $V$, `V_P` — flatness / $P$-regularity loci on $Y$ or on $P^{\vee}$. `(V, 5.5.3)`-`(V, 5.5.7)`

## §V.5.6-§V.5.8. Connectedness, multisections, dimension of the exceptional set

- $S' \to U$ — étale extension. `(V, 5.7.1)`
- $S'$ — multisection of $X$ over $U$. `(V, 5.7.1)`
- $Z_{k}$ — exceptional set for the geometric condition $(R_{k})$. `(V, 5.8.13)`
- $Z_{n}$ — set where $coprof_{x} F \geq n$. `(V, 5.8.5)`
- $Z_{0}$ — set of $\xi$ with an irreducible component of "dimension too large". `(V, 5.8.4)`
- $T_{i}$, $Z_{n,i}$ — irreducible components used in `(5.8.4)`-`(5.8.5)`. `(V, 5.8.4)`, `(V, 5.8.5)`
- $\nu^{\vee}_{X/P}$, $\nu_{X/P}$ — conormal and normal modules of $f : X \to P$. `(V, 5.8.6)`
- `E_P` — tautological bundle on $P$. `(V, 5.8.6)`
- $\psi = (d\phi)|_{Y}$ — restriction of the differential to $Y$. `(V, 5.8.6)`
- $Y^{sing}$, $Y^{supsing}$ — singular / supersingular zero loci on $Y$. `(V, 5.8.6)`, `(V, 5.8.7)`
- $T$ — closure of $Y^{sing}$ in $P^{\vee}$ (reduced induced structure). `(V, 5.8.7)`
- $H'$ — image of the tangent map in $P^{\vee}$. `(V, 5.8.7)`
- $g : Y^{sing} \to T$ — dominant morphism. `(V, 5.8.7)`
- $Y^{\prime, sing}$ — singular locus of $Y' = X - T$. `(V, 5.8.18)`
- $H_{x}$ — hyperplane in $P^{\vee}$ defined by $x \in P$. `(V, 5.8.18)`
- $D$ — section of $\omega^{\otimes 2}_{X/k} \otimes \mathcal{O}_{Y^{sing}}(1, 1)$ whose vanishing is $Y^{supsing}$.
  `(V, 5.8.12)`

## §V.5.9. Change of projective embedding

- $\mathbb{P}^{(n)} = \mathbb{P}(Sym^{n}(\mathcal{E}))$ — $n$-fold Veronese projective fibration. `(V, 5.9.1)`
- $u_{n} : \mathbb{P} \to \mathbb{P}^{(n)}$ — Veronese immersion. `(V, 5.9.1)`
- $f_{n} = u_{n} \circ f$ — composed unramified morphism. `(V, 5.9.2)`
- $Y^{(n)}_{\xi}$ — hyperplane section of $X$ relative to $f_{n}$. `(V, 5.9.3)`

## §V.5.10. Pencils of hyperplane sections

- `Y_L` — linear pencil of hyperplane sections defined by $L \subset P^{\vee}$. `(V, 5.10.1)`
- $L_{0}$ — polar codimension-`2` linear subvariety of $\mathbb{P}$ corresponding to $L$. `(V, 5.10.2)`
- $T = X \times_{\mathbb{P}} L_{0}$ — centre of the blow-up associated to a pencil. `(V, 5.10.2)`
- $F_{X}(-1) \to \mathcal{O}_{X}$ — regular homomorphism associated to a pencil. `(V, 5.10.2)`
- $\widetilde{X}$ — blow-up of $X$ with centre $T$. `(V, 5.10.2)`, `(V, 5.10.3)`
- $\mathcal{G}$, $\mathcal{J}$, $\mathcal{K}$, $\mathcal{H}$ — auxiliary modules / ideals in §V.5.10.3. `(V, 5.10.3)`
- $p = \mathbb{P}(\mathcal{G})$, $p_{C}$ — projective fibration / conic projection. `(V, 5.10.3)`
- $I_{k'} = \operatorname{Spec} k'[t]/(t^{2})$ — first-order infinitesimal "double point". `(V, 5.10.4)`

## §V.5.11-§V.5.12. Grassmannians; linear sections

- $Grass_{n}(\mathcal{E})$ — Grassmannian of rank-$n$ locally free quotients of $\mathcal{E}$. `(V, 5.11)`
- $Grass(\mathcal{E})$ — disjoint sum over all ranks. `(V, 5.11)`
- $Grass_{n}(s)$ — subfunctor associated to a decomposition `(s)` of $\mathcal{E}$. `(V, 5.11)`
- $Grass^{n}(\mathbb{P}) = Grass_{n+1}(\mathcal{E})$ — Grassmannian of dimension-$n$ linear subvarieties of
  $\mathbb{P}$. `(V, 5.12)`
- `Grass_n(ℙ) = Grass^{n−1}(ℙ^∨) = Grass_n(ℰ^∨)` — Grassmannian of codimension-$n$ linear subvarieties. `(V, 5.12)`
- $Gr_{m} = Grass_{m}(\mathbb{P})$ — abbreviation in §V.5.12. `(V, 5.12)`
- $F$ — canonical quotient on $Grass_{m}$. `(V, 5.12)`
- $H^{(m)}$ — incidence prescheme for codimension-$m$ linear sections. `(V, 5.12)`
- $Y^{(m)} = X \times_{\mathbb{P}} H^{(m)}$; $X^{(m)}$ (Grothendieck's preferred notation) — linear-section total space.
  `(V, 5.12)`
- $\phi_{m}$, $\phi^{(m)}$ — sections defining the linear-section divisor. `(V, 5.12)`
- $X^{(m)}_{sing} = V_{1}$, `V_0`, `V_2`, $V''$, $V' - V''$ — filtration of the linear-section family. `(V, 5.12)`
- $V^{(k)}$ — subscheme of $X^{(m)}$ cut out by $\dim T_{x} \cap L \geq n - m + k$. `(V, 5.12)`
- $L_{\xi}$ — linear subvariety of codimension $m$ indexed by $\xi \in Gr_{m}$. `(V, 5.12)`

## §V.5.14. Conic projections

- $C = \mathbb{P}(F)$ — centre of conic projection. `(V, 5.14)`
- $Q(C)$ — projective space of codimension-$m$ linear subvarieties of $\mathbb{P}$ containing $C$. `(V, 5.14)`
- $p_{C} : \mathbb{P} - C \to \mathbb{P}(G)$ — algebraic conic projection (cf. EGA II). `(V, 5.14)`
- $p^{X}_{C} = p_{C} \circ f$ — conic projection of $X$ with centre $C$. `(V, 5.14)`
- $\widetilde{X}(C)$, $\widetilde{F}(C)$ — extended conic projection space and sheaf. `(V, 5.14)`
- $C_{\eta}$ — $C$ over the generic point of $Grass_{m+1}$. `(V, 5.14)`
- $Y_{\eta}$ — scheme-theoretic image of $X_{k(\eta)}$ under $p_{C_{\eta}}$. `(V, 5.14.5)`

## §V.5.15. Axiomatization

- $\mathcal{P}$, $\tilde{\mathcal{P}}$, $G$ — abstract incidence data ($\mathcal{P}$ a projective fibration, $G$ a
  Grassmannian-type prescheme, $\tilde{\mathcal{P}}$ the incidence prescheme). `(V, 5.15)`
- $\tilde{X} = X \times_{\mathcal{P}} \tilde{\mathcal{P}}$ — abstract analogue of the total hyperplane section.
  `(V, 5.15)`
- $N$, $m$ — relative dimensions of $G/S$ and of $\tilde{\mathcal{P}} \to \mathcal{P}$. `(V, 5.15)`
- $\tilde{Z}$ — inverse image of $Z$ in $\tilde{X}$. `(V, 5.15)`
- $E(x, V)$ — set of $\xi$ with bad incidence at $(x, V)$. `(V, 5.15)`

## §V.6.1. Invertible sheaves on projective fibrations

- $P = \mathbb{P}(E)$, $f : P \to S$ — projective fibration with structural morphism. `(V, 6.1.1)`
- $(S_{n})_{n \in \mathbb{Z}}$ — open decomposition of $S$ indexed by integers. `(V, 6.1.1)`
- $M \otimes \mathcal{O}_{P}(n) = f^{*}(M)(n)$ — twist of an invertible module on a projective fibration. `(V, 6.1.1)`
- $\operatorname{Pic}(S)$, $\operatorname{Pic}(P)$ — Picard groups. `(V, 6.1.3)`, `(V, 6.1.4)`
- `(*)` — canonical homomorphism $\operatorname{Pic}(S) \times \mathbb{Z} \to \operatorname{Pic}(P)$. `(V, 6.1.3)`
- $\mathbb{Z}(S)$ — locally constant functions $S \to \mathbb{Z}$. `(V, 6.1.4)`
- $(* bis)$ — extension $\operatorname{Pic}(S) \times \mathbb{Z}(S) \to \operatorname{Pic}(P)$. `(V, 6.1.4)`
- $\operatorname{Pic}_{P/S}$ — relative Picard scheme (forward reference). `(V, 6.1.4)`
- $\operatorname{Aut}_{S}(P)$ — automorphism group functor of $P$ over $S$. `(V, 6.1.9)`
- $PGL(E)$, $PGL(r)$, $PGL(r)_{S}$ — projective group schemes. `(V, 6.1.9)`
- $GL(E)$, $\mathbb{G}_{m}$ — linear group scheme and its centre. `(V, 6.1.9)`

## §V.6.2. Relative divisors

- $\operatorname{Div}^{+}(P/S)$ — set of positive relative divisors of $P/S$. `(V, 6.2.1)`
- $\operatorname{Div}^{n}(P/S)$ — degree-$n$ part. `(V, 6.2.2)`
- $\operatorname{Div}^{n}_{P/S}$ — subfunctor representing $\operatorname{Div}^{n}$. `(V, 6.2.3)`
- $\operatorname{Div}^{+}_{P/S}$ — full divisor functor. `(V, 6.2.4)`
- $\mathcal{O}_{i}(n)$ — pullback of $\mathcal{O}_{P_{i}}(n)$ to a multiprojective fibration. `(V, 6.2.5)`
- $\mathcal{O}_{P}(n)$ — multidegree-$n$ twist on a multiprojective fibration. `(V, 6.2.5)`
- $Sym^{n}(E)$, $Sym^{n_{i}}(E_{i})$ — symmetric powers. `(V, 6.2.2)`, `(V, 6.2.8)`
- $Q$ — finitely presented module on $S$ representing pushforwards (cf. `(III, §7)`). `(V, 6.2.10)`, `(V, 6.2.12)`
- $\operatorname{Div}^{L}_{X/S}$ — subfunctor parametrizing divisors with $\mathcal{O}_{X}(D) \cong L \otimes f^{*} M$.
  `(V, 6.2.10)`

## §V.6.3. Linear systems and morphisms

- $Z$ — set of fixed points of a family of divisors. `(V, 6.3.1)`
- $Z'$ — set of fixed points in the extended sense. `(V, 6.3.1)`
- $D$ — family of positive divisors. `(V, 6.3.1)`
- `ᵗD` — symmetric image of $D$. `(V, 6.3.1)`
- $\operatorname{Div}_{T/S}$ — divisor functor. `(V, 6.3.1)`
- $Q = \mathbb{P}(F) = P^{\vee}$ — parametrizing projective fibration. `(V, 6.3)`
- $\mathbb{P}(n) = \mathbb{P}(Sym^{n}(F^{\vee}))$ — degree-$n$ divisor space. `(V, 6.3)`
- $f : X - Z \to P$ — morphism associated to a linear system. `(V, 6.3)`, `(V, 6.3.1)`
- $H$ — canonical incidence divisor on $P \times_{S} P^{\vee}$. `(V, 6.3.1)`
- $\Phi$, $\mathfrak{U}$ — sets of linear systems / pseudo-morphisms. `(V, 6.3.4)`
- $U(f)$ — domain of definition of a pseudo-morphism. `(V, 6.3.4)`
- $L_{U} = f^{*}_{U}(\mathcal{O}_{P}(1))$, $i_{*}(L_{U})$ — invertible-module construction. `(V, 6.3.4)`

## §V.6.4. Linear systems and invertible modules

- $N$ — invertible module on $X \times_{S} P^{\vee}$ corresponding to a divisor $D$. `(V, 6.4)`
- $u : E \to g_{*}(L)$ — datum classifying a linear system. `(V, 6.4.1)`
- $Q$, $Q \to E^{\vee}$ — module representing $g_{*}(L \otimes \cdot)$ and surjection determining a linear system.
  `(V, 6.4.2)`
- $Grass(Q)$ — Grassmannian representing classes of linear systems associated to $L$. `(V, 6.4.2)`
- $\operatorname{Aut}_{S}(P^{\vee})$, $\operatorname{Aut}_{S}(\mathbb{P}(E^{\vee}))$ — automorphism group functor.
  `(V, 6.4.3)`
- $Ens(D)$, $\Delta$ — set of divisors arising from a linear system. `(V, 6.4.5)`
- $\mathcal{G}_{w_{0}}$ — abstract "tangent vector space" of a functor at $w_{0}$ (re-use of the §V.1 glyph; cf. note
  above). `(V, 6.4.3)`
- $\mathcal{N}_{D_{0}/X_{0}}$ — normal sheaf of `D_0` in `X_0`. `(V, 6.4.3)`
- $div(\phi)$ — divisor of a meromorphic function $\phi$. `(V, 6.4.5)`
- $E$ (in §V.6.4.5) — $k$-subspace of meromorphic functions defining a linear system. `(V, 6.4.5)`

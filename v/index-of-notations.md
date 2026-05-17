# Index of notations — EGA V

Source-ordered, with §V section subheadings. Reused notations from EGA I-IV (e.g. `𝒪_X`, `Ω^1_{X/S}`, `Pic(X)`, `Sym`,
`Λ`, `ℙ`, `Proj`, `Spec`, `→`, `↦`, `⊗`, `≅`) are not re-listed here; see `docs/books/ega/iv/index-of-notations.md`.

Note on overloads: the symbol `𝒢` denotes the **tangent sheaf** `𝒢_{X/Y}` in §V.1 and §V.5.8 (kernel of the augmentation
`𝒫^1_{X/Y} → 𝒪_X`), but is repurposed in §V.6.4.3 as the abstract "tangent vector space `𝒢_{w_0}`" of a functor at a
chosen point; the same glyph carries two distinct meanings. Similarly the symbol `𝒫` denotes the **sheaf of principal
parts** `𝒫^n_{X/Y}` in §V.1 and a generic **projective fibration** in §V.5.15; context distinguishes. The notation
`(S_n)` denotes both Serre's depth condition (§V.5.2.8) and a `ℤ`-indexed open partition of the base (§V.6.1.1); we
attach the subscript range `(S_n)_{n ∈ ℤ}` when ambiguity could arise.

## §V.1. Singular and supersingular zeros

- `𝔪_x`, `𝔪_x²`, `𝔪_x / 𝔪_x²` — maximal ideal of `𝒪_{X,x}`, its square, and the Zariski cotangent space. `(V, 1.1)`
- `t_x` — dual of `𝔪_x / 𝔪_x²` over `k(x)` (Zariski tangent space). `(V, 1.1)`
- `Sym²(𝔪_x / 𝔪_x²)` — module of quadratic forms on `t_x`. `(V, 1.1)`
- `V(φ)` — zero set / subscheme of zeros of a section `φ`. `(V, 1.1)`, `(V, 1.5)`
- `V(φ)_sing` — singular zeros of `φ` (relative to `Y`). `(V, 1.5)`
- `V(φ)_{supsing}` — supersingular zeros of `φ` (relative to `Y`). `(V, 1.5)`
- `φ_{k′}`, `X_{k′}` — base change of `φ` and of `X` along `k → k′`. `(V, 1.3)`
- `d⁰φ = φ` — order-`0` principal-parts truncation. `(V, 1.5)`
- `d¹_{X/Y} φ` — order-`1` truncation. `(V, 1.5)`
- `d²_{X/Y} φ` — order-`2` truncation. `(V, 1.5)`
- `d_{X/Y} φ` — universal differential of `φ` (restriction of `d¹φ` to `V(φ)`). `(V, 1.5)`
- `𝒫^n_{X/Y}` — sheaf of principal parts of order `n` (cf. `(0_IV, 20.4.14)`). `(V, 1.5)`
- `gr¹(𝒫^1_{X/Y}) ≅ Ω^1_{X/Y}` — first graded piece. `(V, 1.5)`
- `gr²(𝒫^2_{X/Y}) ≅ Sym²(Ω^1_{X/Y})` — second graded piece. `(V, 1.5)`
- `M(φ)` — canonical section of `Sym²(Ω^1_{X/Y}) ⊗ 𝒪_{V(φ)_sing}`; quadratic form on the cotangent space. `(V, 1.5)`
- `M(φ)′` — homomorphism `𝒢_{X/Y} ⊗ 𝒪_{V(φ)_sing} → Ω^1_{X/Y} ⊗ 𝒪_{V(φ)_sing}` deduced from `M(φ)`. `(V, 1.5)`
- `D(φ) = det M(φ)` — discriminant of `M(φ)`; section of `Γ(Ω^d_{X/Y})^{⊗ 2} ⊗ 𝒪_{V(φ)_sing}`. `(V, 1.5)`
- `𝒢_{X/Y}` — tangent sheaf; kernel of `𝒫^1_{X/Y} → 𝒪_X`. `(V, 1.5)`, footnote `[^v-1-3]`
- `V′ = V(φ)_sing` — abbreviation in §V.1.7. `(V, 1.7)`
- `μ`, `ν` — composed homomorphisms in the §V.1.7 diagram. `(V, 1.7)`
- `Ram(V′/Y)` — ramification subprescheme of `V′` relative to `Y`. `(V, 1.7)`
- `det F` — highest exterior power of a locally free module `F` of finite rank. `(V, 1.8)`
- `Λ^q Q`, `Λ^r M` — exterior powers used to detect non-surjectivity loci. `(V, 1.7)`
- `L = det P ⊗ det Q ⊗ det M^{−1}` — line bundle in the §V.1.8 lemma. `(V, 1.8)`

## §V.2.15-§V.2.16. Smooth forms; smooth quadratic forms

- `ℙ(E)`, `P = ℙ(E)` — projective fibration. `(V, 2.15.1)`
- `𝒪_P(n)` — Serre twist on `P`. `(V, 2.15.1)`
- `Sym^n(E)` — `n`-th symmetric power. `(V, 2.15.1)`
- `V(φ) ⊂ P` — subscheme of zeros of an `n`-form. `(V, 2.15.1)`
- `𝒥`, `𝒪_X/𝒥` — ideal and quotient sheaf in an augmentation. `(V, 2.15.2)`
- `𝒩_{X/Y} = 𝒥/𝒥²` — conormal module of `Y = V(𝒥)` in `X`. `(V, 2.15.2)`
- `Ψ : Sym_{𝒪_Y}(𝒩) → gr_𝒥(𝒪_X)` — canonical surjection on the associated graded ring. `(V, 2.15.2)`
- `𝒦 = ker(Ψ_n)` — kernel in degree `n` (invertible submodule of `Sym^n_{𝒪_Y}(𝒩)`). `(V, 2.15.2)`
- `r(A)` — radical / maximal ideal of a local ring. `(V, 2.15.2)`
- `d^n φ` — order-`n` principal part of `φ`. `(V, 2.15.7)`
- `I` — augmentation ideal of `𝒫^n_{X′/k} ⊗ k(x)`. `(V, 2.15.7)`
- `Q ∈ Sym²(E)` — quadratic form. `(V, 2.16.1)`
- `B` — symmetric bilinear form on `E^∨` associated to `Q`. `(V, 2.16.1)`
- `d(Q) ∈ Γ(det(E)^{⊗ 2})` — ordinary discriminant. `(V, 2.16.1)`
- `N ⊂ E^∨` — "kernel" of the alternating bilinear form in characteristic 2. `(V, 2.16.2)`
- `Q_n`, `Q_{2m}`, `Q_{2m+1}` — standard quadratic forms in `n`, `2m`, `2m+1` variables. `(V, 2.16.4)`
- `d̃(Q)` — corrected (adjusted) discriminant of `Q`. `(V, 2.16.6)`, `(V, 2.16.7)`
- `𝕍(·)` — vector-bundle functor associated to a locally free sheaf. `(V, 2.16.3)`, `(V, 2.16.11)`
- `Isom((E₀, Q₀), (E, Q))` — functor of isometries. `(V, 2.16.11)`
- `Isom(E₀, E)` — functor of isomorphisms of locally free modules. `(V, 2.16.11)`
- `𝒬(E) = 𝕍(Sym²(E))` — affine bundle of quadratic forms. `(V, 2.16.11)`
- `𝒬(E)* = 𝒬(E)_{d̃}` — open subset of smooth (i.e. `d̃`-invertible) quadratic forms. `(V, 2.16.11)`
- `O(n)` — absolute orthogonal group (stabilizer of `Q_n` in `Aut(ℤ^n)`). `(V, 2.16.12)`
- `O(Q)` — orthogonal group scheme relative to `Q`. `(V, 2.16.12)`
- `SO(n)` — special orthogonal subgroup. `(V, 2.16.14)`
- `μ_{2,S}` — group scheme of square roots of unity over `S`. `(V, 2.16.14)`

## §V.5.1. Hyperplane sections — preliminaries and notation

- `P = ℙ(E)` — projective fibration. `(V, 5.1)`
- `P^∨ = ℙ(E^∨)` — scheme of hyperplanes (dual projective fibration). `(V, 5.1)`
- `L`, `L_P`, `L_P^{−1}` — invertible quotient / submodule used to define a hyperplane. `(V, 5.1)`
- `H_ξ` — hyperplane in `P` defined by `ξ ∈ P^∨(S)`. `(V, 5.1)`
- `H` — universal / incidence hyperplane in `P ×_S P^∨`. `(V, 5.1)`
- `Div(P/S)` — functor of relative divisors of `P/S`. `(V, 5.1.1)`
- `f : X → P` — projective immersion / unramified morphism. `(V, 5.1)`
- `Y_ξ = f^{−1}(H_ξ)` — hyperplane section associated to `ξ`. `(V, 5.1)`
- `Y = X ×_P H` — total hyperplane section over `P^∨`. `(V, 5.1)`
- `F`, `G_ξ`, `G` — sheaf on `X` and its inverse images on `Y_ξ`, `Y`. `(V, 5.1)`

## §V.5.2-§V.5.3. Generic hyperplane section

- `η` — generic point of `P^∨`. `(V, 5.2)`
- `H_η`, `Y_η`, `G_η` — hyperplane, hyperplane section, sheaf at `η`. `(V, 5.2)`
- `Z_η` — inverse image of `Z ⊂ P` in `H_η`. `(V, 5.2.2)`
- `Y_{i,η}` — irreducible component of `Y_η`. `(V, 5.2.5)`
- `coprof_y G` — codepth of `G` at `y`. `(V, 5.2.8)`
- `(S_k)`, `(R_k)` — Serre's depth and regularity conditions. `(V, 5.2.8)`, `(V, 5.2.11)`
- `K`, `L` — function fields of `X` and `Y_η`. `(V, 5.3.1)`
- `S_1, …, S_n` — affine coordinates in `P^∨`. `(V, 5.3.1)`
- `T_1, …, T_n` — affine coordinates in `P`. `(V, 5.3.1)`
- `t_i ∈ K` — image of `T_i` under `f : X → P`. `(V, 5.3.1)`
- `(C_m)` — non-disconnect-by-codimension-`m` property. `(V, 5.4.4)`

## §V.5.4-§V.5.5. Variable hyperplane sections; Seidenberg-type theorems

- `E` — set of `ξ ∈ P^∨` such that `Y_ξ` has a given property. `(V, 5.4)`
- `Z_P` — set of `ξ ∈ P^∨` exceptional for property `P`. `(V, 5.8.1)`
- `φ_ξ` — section of `𝒪_X(1) ⊗ 𝒪_{P^∨}(1)(ξ)` defining `Y_ξ`. `(V, 5.5.2)`
- `U`, `U_P`, `V`, `V_P` — flatness / `P`-regularity loci on `Y` or on `P^∨`. `(V, 5.5.3)`-`(V, 5.5.7)`

## §V.5.6-§V.5.8. Connectedness, multisections, dimension of the exceptional set

- `S′ → U` — étale extension. `(V, 5.7.1)`
- `S′` — multisection of `X` over `U`. `(V, 5.7.1)`
- `Z_k` — exceptional set for the geometric condition `(R_k)`. `(V, 5.8.13)`
- `Z_n` — set where `coprof_x F ≥ n`. `(V, 5.8.5)`
- `Z₀` — set of `ξ` with an irreducible component of "dimension too large". `(V, 5.8.4)`
- `T_i`, `Z_{n,i}` — irreducible components used in `(5.8.4)`-`(5.8.5)`. `(V, 5.8.4)`, `(V, 5.8.5)`
- `ν^∨_{X/P}`, `ν_{X/P}` — conormal and normal modules of `f : X → P`. `(V, 5.8.6)`
- `E_P` — tautological bundle on `P`. `(V, 5.8.6)`
- `ψ = (dφ)|_Y` — restriction of the differential to `Y`. `(V, 5.8.6)`
- `Y^{sing}`, `Y^{supsing}` — singular / supersingular zero loci on `Y`. `(V, 5.8.6)`, `(V, 5.8.7)`
- `T` — closure of `Y^{sing}` in `P^∨` (reduced induced structure). `(V, 5.8.7)`
- `H′` — image of the tangent map in `P^∨`. `(V, 5.8.7)`
- `g : Y^{sing} → T` — dominant morphism. `(V, 5.8.7)`
- `Y^{\prime, sing}` — singular locus of `Y′ = X − T`. `(V, 5.8.18)`
- `H_x` — hyperplane in `P^∨` defined by `x ∈ P`. `(V, 5.8.18)`
- `D` — section of `ω_{X/k}^{⊗ 2} ⊗ 𝒪_{Y^{sing}}(1, 1)` whose vanishing is `Y^{supsing}`. `(V, 5.8.12)`

## §V.5.9. Change of projective embedding

- `ℙ^{(n)} = ℙ(Sym^n(ℰ))` — `n`-fold Veronese projective fibration. `(V, 5.9.1)`
- `u_n : ℙ → ℙ^{(n)}` — Veronese immersion. `(V, 5.9.1)`
- `f_n = u_n ∘ f` — composed unramified morphism. `(V, 5.9.2)`
- `Y_ξ^{(n)}` — hyperplane section of `X` relative to `f_n`. `(V, 5.9.3)`

## §V.5.10. Pencils of hyperplane sections

- `Y_L` — linear pencil of hyperplane sections defined by `L ⊂ P^∨`. `(V, 5.10.1)`
- `L₀` — polar codimension-`2` linear subvariety of `ℙ` corresponding to `L`. `(V, 5.10.2)`
- `T = X ×_ℙ L₀` — centre of the blow-up associated to a pencil. `(V, 5.10.2)`
- `F_X(−1) → 𝒪_X` — regular homomorphism associated to a pencil. `(V, 5.10.2)`
- `\widetilde{X}` — blow-up of `X` with centre `T`. `(V, 5.10.2)`, `(V, 5.10.3)`
- `𝒢`, `𝒥`, `𝒦`, `ℋ` — auxiliary modules / ideals in §V.5.10.3. `(V, 5.10.3)`
- `p = ℙ(𝒢)`, `p_C` — projective fibration / conic projection. `(V, 5.10.3)`
- `I_{k′} = Spec k′[t]/(t²)` — first-order infinitesimal "double point". `(V, 5.10.4)`

## §V.5.11-§V.5.12. Grassmannians; linear sections

- `Grass_n(ℰ)` — Grassmannian of rank-`n` locally free quotients of `ℰ`. `(V, 5.11)`
- `Grass(ℰ)` — disjoint sum over all ranks. `(V, 5.11)`
- `Grass_n(s)` — subfunctor associated to a decomposition `(s)` of `ℰ`. `(V, 5.11)`
- `Grass^n(ℙ) = Grass_{n+1}(ℰ)` — Grassmannian of dimension-`n` linear subvarieties of `ℙ`. `(V, 5.12)`
- `Grass_n(ℙ) = Grass^{n−1}(ℙ^∨) = Grass_n(ℰ^∨)` — Grassmannian of codimension-`n` linear subvarieties. `(V, 5.12)`
- `Gr_m = Grass_m(ℙ)` — abbreviation in §V.5.12. `(V, 5.12)`
- `F` — canonical quotient on `Grass_m`. `(V, 5.12)`
- `H^{(m)}` — incidence prescheme for codimension-`m` linear sections. `(V, 5.12)`
- `Y^{(m)} = X ×_ℙ H^{(m)}`; `X^{(m)}` (Grothendieck's preferred notation) — linear-section total space. `(V, 5.12)`
- `φ_m`, `φ^{(m)}` — sections defining the linear-section divisor. `(V, 5.12)`
- `X^{(m)}_sing = V_1`, `V_0`, `V_2`, `V″`, `V′ − V″` — filtration of the linear-section family. `(V, 5.12)`
- `V^{(k)}` — subscheme of `X^{(m)}` cut out by `dim T_x ∩ L ≥ n − m + k`. `(V, 5.12)`
- `L_ξ` — linear subvariety of codimension `m` indexed by `ξ ∈ Gr_m`. `(V, 5.12)`

## §V.5.14. Conic projections

- `C = ℙ(F)` — centre of conic projection. `(V, 5.14)`
- `Q(C)` — projective space of codimension-`m` linear subvarieties of `ℙ` containing `C`. `(V, 5.14)`
- `p_C : ℙ − C → ℙ(G)` — algebraic conic projection (cf. EGA II). `(V, 5.14)`
- `p_C^X = p_C ∘ f` — conic projection of `X` with centre `C`. `(V, 5.14)`
- `\widetilde{X}(C)`, `\widetilde{F}(C)` — extended conic projection space and sheaf. `(V, 5.14)`
- `C_η` — `C` over the generic point of `Grass_{m+1}`. `(V, 5.14)`
- `Y_η` — scheme-theoretic image of `X_{k(η)}` under `p_{C_η}`. `(V, 5.14.5)`

## §V.5.15. Axiomatization

- `𝒫`, `𝒫̃`, `G` — abstract incidence data (`𝒫` a projective fibration, `G` a Grassmannian-type prescheme, `𝒫̃` the
    incidence prescheme). `(V, 5.15)`
- `X̃ = X ×_𝒫 𝒫̃` — abstract analogue of the total hyperplane section. `(V, 5.15)`
- `N`, `m` — relative dimensions of `G/S` and of `𝒫̃ → 𝒫`. `(V, 5.15)`
- `Z̃` — inverse image of `Z` in `X̃`. `(V, 5.15)`
- `E(x, V)` — set of `ξ` with bad incidence at `(x, V)`. `(V, 5.15)`

## §V.6.1. Invertible sheaves on projective fibrations

- `P = ℙ(E)`, `f : P → S` — projective fibration with structural morphism. `(V, 6.1.1)`
- `(S_n)_{n ∈ ℤ}` — open decomposition of `S` indexed by integers. `(V, 6.1.1)`
- `M ⊗ 𝒪_P(n) = f^*(M)(n)` — twist of an invertible module on a projective fibration. `(V, 6.1.1)`
- `Pic(S)`, `Pic(P)` — Picard groups. `(V, 6.1.3)`, `(V, 6.1.4)`
- `(*)` — canonical homomorphism `Pic(S) × ℤ → Pic(P)`. `(V, 6.1.3)`
- `ℤ(S)` — locally constant functions `S → ℤ`. `(V, 6.1.4)`
- `(* bis)` — extension `Pic(S) × ℤ(S) → Pic(P)`. `(V, 6.1.4)`
- `Pic_{P/S}` — relative Picard scheme (forward reference). `(V, 6.1.4)`
- `Aut_S(P)` — automorphism group functor of `P` over `S`. `(V, 6.1.9)`
- `PGL(E)`, `PGL(r)`, `PGL(r)_S` — projective group schemes. `(V, 6.1.9)`
- `GL(E)`, `𝔾_m` — linear group scheme and its centre. `(V, 6.1.9)`

## §V.6.2. Relative divisors

- `Div^+(P/S)` — set of positive relative divisors of `P/S`. `(V, 6.2.1)`
- `Div^n(P/S)` — degree-`n` part. `(V, 6.2.2)`
- `Div^n_{P/S}` — subfunctor representing `Div^n`. `(V, 6.2.3)`
- `Div^+_{P/S}` — full divisor functor. `(V, 6.2.4)`
- `𝒪_i(n)` — pullback of `𝒪_{P_i}(n)` to a multiprojective fibration. `(V, 6.2.5)`
- `𝒪_P(n)` — multidegree-`n` twist on a multiprojective fibration. `(V, 6.2.5)`
- `Sym^n(E)`, `Sym^{n_i}(E_i)` — symmetric powers. `(V, 6.2.2)`, `(V, 6.2.8)`
- `Q` — finitely presented module on `S` representing pushforwards (cf. `(III, §7)`). `(V, 6.2.10)`, `(V, 6.2.12)`
- `Div^L_{X/S}` — subfunctor parametrizing divisors with `𝒪_X(D) ≅ L ⊗ f^* M`. `(V, 6.2.10)`

## §V.6.3. Linear systems and morphisms

- `Z` — set of fixed points of a family of divisors. `(V, 6.3.1)`
- `Z′` — set of fixed points in the extended sense. `(V, 6.3.1)`
- `D` — family of positive divisors. `(V, 6.3.1)`
- `ᵗD` — symmetric image of `D`. `(V, 6.3.1)`
- `Div_{T/S}` — divisor functor. `(V, 6.3.1)`
- `Q = ℙ(F) = P^∨` — parametrizing projective fibration. `(V, 6.3)`
- `ℙ(n) = ℙ(Sym^n(F^∨))` — degree-`n` divisor space. `(V, 6.3)`
- `f : X − Z → P` — morphism associated to a linear system. `(V, 6.3)`, `(V, 6.3.1)`
- `H` — canonical incidence divisor on `P ×_S P^∨`. `(V, 6.3.1)`
- `Φ`, `𝔘` — sets of linear systems / pseudo-morphisms. `(V, 6.3.4)`
- `U(f)` — domain of definition of a pseudo-morphism. `(V, 6.3.4)`
- `L_U = f_U^*(𝒪_P(1))`, `i_*(L_U)` — invertible-module construction. `(V, 6.3.4)`

## §V.6.4. Linear systems and invertible modules

- `N` — invertible module on `X ×_S P^∨` corresponding to a divisor `D`. `(V, 6.4)`
- `u : E → g_*(L)` — datum classifying a linear system. `(V, 6.4.1)`
- `Q`, `Q → E^∨` — module representing `g_*(L ⊗ ·)` and surjection determining a linear system. `(V, 6.4.2)`
- `Grass(Q)` — Grassmannian representing classes of linear systems associated to `L`. `(V, 6.4.2)`
- `Aut_S(P^∨)`, `Aut_S(ℙ(E^∨))` — automorphism group functor. `(V, 6.4.3)`
- `Ens(D)`, `Δ` — set of divisors arising from a linear system. `(V, 6.4.5)`
- `𝒢_{w_0}` — abstract "tangent vector space" of a functor at `w_0` (re-use of the §V.1 glyph; cf. note above).
    `(V, 6.4.3)`
- `𝒩_{D_0/X_0}` — normal sheaf of `D_0` in `X_0`. `(V, 6.4.3)`
- `div(φ)` — divisor of a meromorphic function `φ`. `(V, 6.4.5)`
- `E` (in §V.6.4.5) — `k`-subspace of meromorphic functions defining a linear system. `(V, 6.4.5)`

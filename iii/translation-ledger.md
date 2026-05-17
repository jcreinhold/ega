# Translation ledger — EGA III

Running French↔English term ledger for the EGA III translation. Seeded from `zz-index-terminologique-part-1.md`,
`zz-index-terminologique-part-2.md`, `zz-index-notations-part-1.md`, and `zz-index-notations-part-2.md`. Extends the EGA
II ledger at `docs/books/ega/ii/translation-ledger.md`.

## Terms inherited from EGA II

The EGA II ledger transfers unchanged: `préschéma` → prescheme, `schéma` → scheme, `morphisme structural` → structure
morphism, `morphisme affine`, `morphisme propre`, `morphisme projectif`, `morphisme entier`, `morphisme fini`,
`morphisme quasi-fini`, `universellement fermé`, `séparé`, `très ample`, `(TF)` / `(TN)` conditions, `éclatement` →
blow-up, `cône projetant` → projecting cone, `fermeture projective` → projective closure, `homogénéisation` →
homogenization, etc.

## EGA III additions

### Chapter 0_III preliminaries

| French                                                         | English                                                         | First appearance      | Note                                                                                                       |
| -------------------------------------------------------------- | --------------------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------- |
| aboutissement d'une suite spectrale                            | abutment of a spectral sequence                                 | 0_III.11.1.1          | EGA's "aboutissement"; modern "abutment" or "limit".                                                       |
| application quasi-compacte                                     | quasi-compact map                                               | 0_III.9.1.1           | Continuous `f : X → Y` such that `f⁻¹(U)` is quasi-compact for every quasi-compact open `U`.               |
| augmentation d'une résolution                                  | augmentation of a resolution                                    | 0_III.11.4.1          |                                                                                                            |
| bicomplexe                                                     | bicomplex                                                       | 0_III.11.2.1          |                                                                                                            |
| caractéristique d'Euler–Poincaré (d'un complexe)               | Euler–Poincaré characteristic (of a complex)                    | 0_III.11.10.1         |                                                                                                            |
| cochaîne bi-alternée                                           | bi-alternating cochain                                          | 0_III.11.8.4          |                                                                                                            |
| complexe défini par un bicomplexe                              | complex defined by a bicomplex                                  | 0_III.11.3.1          |                                                                                                            |
| condition (ML)                                                 | condition (ML)                                                  | 0_III.13.1.2          | Mittag–Leffler condition; preserve EGA's `(ML)` form.                                                      |
| constructible (partie, ensemble)                               | constructible (subset, set)                                     | 0_III.9.1.2           |                                                                                                            |
| constructible (fonction)                                       | constructible (function)                                        | 0_III.9.3.1           |                                                                                                            |
| cup-produit                                                    | cup product                                                     | 0_III.12.1.2          |                                                                                                            |
| dihomomorphisme                                                | di-homomorphism                                                 | 0_III.8.2.1           |                                                                                                            |
| edge-homomorphisme (d'une suite spectrale)                     | edge homomorphism (of a spectral sequence)                      | 0_III.12.1.7          | EGA writes "edge-homomorphisme" in English (hyphen kept in source; we drop it).                            |
| extension de degré fini (d'un corps)                           | extension of finite degree (of a field)                         | 0_III.10.3.2          |                                                                                                            |
| extension plate d'anneaux locaux                               | flat extension of local rings                                   | 0_III.10.3.1          | Local homomorphism `A → B` of Noetherian local rings making `B` a flat `A`-module.                         |
| `f`-plat (sur)                                                 | `f`-flat (over)                                                 | 0_III.10.2.4          | When `M` is `A`-flat via `f : A → B`.                                                                      |
| Ens (catégorie)                                                | `Set` (category)                                                | 0_III.8.1.1           | We render EGA's bold-face **Ens** as upright `Set` in backticks.                                           |
| extension (d'un `𝒪_X`-Module par un `𝒪_X`-Module)              | extension (of an `𝒪_X`-module by an `𝒪_X`-module)               | 0_III.12.3.2          | Group of equivalence classes identified with `Ext^1`.                                                      |
| faisceau image directe supérieure `R^q f_*(ℱ)`                 | higher direct image sheaf `R^q f_*(ℱ)`                          | 0_III.12.2.1          |                                                                                                            |
| `f`-morphisme (de Modules)                                     | `f`-morphism (of modules)                                       | 0_III.12.1.3          | A morphism `ℱ → ℱ'` over a morphism `f` of ringed spaces (cf. `(0_I, 4.4.1)`).                             |
| foncteur image directe                                         | direct image functor                                            | 0_III.12.2.1          | `f_* : C(X) → C(Y)`.                                                                                       |
| hypercohomologie d'un recouvrement                             | hypercohomology of a cover                                      | 0_III.12.4.5          | `H^•(𝔘, 𝒦^•)` for a complex `𝒦^•` of `𝒪_X`-modules.                                                        |
| morphisme d'espaces annelés                                    | morphism of ringed spaces                                       | 0_III.12.1.3          |                                                                                                            |
| idéalement séparé (module)                                     | ideally separated (module)                                      | 0_III.10.2.1          | An `A`-module `M` such that `𝔞 ⊗_A M` is separated for the `𝔍`-preadic topology for every ideal `𝔞`.       |
| critère local de platitude                                     | local criterion of flatness                                     | 0_III.10.2.1          | The criteria a)/b)/c)/d) relating flatness of `M` to flatness of the quotients `M/𝔍^n M`.                  |
| homothétie (`f_M : x ↦ fx`)                                    | homothety (`f_M : x ↦ fx`)                                      | 0_III.10.2.7          | EGA's term for the multiplication-by-`f` endomorphism.                                                     |
| homomorphisme local d'anneaux locaux                           | local homomorphism of local rings                               | 0_III.10.2.4          | Sends the maximal ideal into the maximal ideal.                                                            |
| domination (d'anneau local par anneau de valuation)            | domination (of a local ring by a valuation ring)                | 0_III.10.2.8          | `B` dominates `A` if `A ⊂ B` and the maximal ideal of `B` contracts to that of `A`.                        |
| séparé complété (d'un module pour une topologie)               | Hausdorff completion (of a module for a topology)               | 0_III.10.2.3          | "Séparé complété" = take the Hausdorff quotient and then complete; standard English: Hausdorff completion. |
| `gr(A)`, `gr(M)` (anneau, module gradué associé)               | `gr(A)`, `gr(M)` (associated graded ring, module)               | 0_III.10.1.1          | `gr(A) = ⊕_{p≥0} 𝔍^p/𝔍^{p+1}` for `A` filtered by `𝔍`.                                                     |
| topologie `𝔍`-préadique                                        | `𝔍`-preadic topology                                            | 0_III.10.2.1          | Topology defined by the powers of an ideal `𝔍`; "preadic" preserved (EGA's term).                          |
| suite spectrale de Leray (d'un foncteur composé)               | Leray spectral sequence (of a composite functor)                | 0_III.12.2.4          | `E_2^{p,q} = R^p g_*(R^q f_*(ℱ)) ⟹ R^{p+q}(g ∘ f)_*(ℱ)`.                                                   |
| suite spectrale de Leray (d'un recouvrement)                   | Leray spectral sequence (of a cover)                            | 0_III.12.4.6          | Hypercohomology version: `E_2^{p,q} = H^p(𝔘, ℎ^q(𝒦^•))`.                                                   |
| essentiellement constant (système projectif)                   | essentially constant (projective system)                        | 0_III.13.4.2          |                                                                                                            |
| filtration co-discrète, co-séparée, etc.                       | co-discrete, co-separated, etc. filtration                      | 0_III.11.1.3          | Render the full list: discrète, exhaustive, finie, séparée → discrete, exhaustive, finite, separated.      |
| final (objet) d'une catégorie                                  | final object of a category                                      | 0_III.8.1.10          |                                                                                                            |
| foncteur covariant canonique                                   | canonical covariant functor                                     | 0_III.8.1.2           | `𝒞 → Hom(𝒞°, Set)`.                                                                                        |
| foncteur contravariant (covariant)                             | contravariant (covariant) functor                               | 0_III.8.1.1           |                                                                                                            |
| générisation (d'un point)                                      | generization (of a point)                                       | 0_III.9.3.4           | Cited from `(0_I, 2.1.2)`; `x'` is a generization of `x` iff `x ∈ {x'}̄`.                                   |
| homomorphisme de structures algébriques sur catégories         | homomorphism of algebraic structures on categories              | 0_III.8.2.1           |                                                                                                            |
| hypercohomologie (d'un foncteur, d'un bifoncteur)              | hypercohomology (of a functor, of a bifunctor)                  | 0_III.11.4.3 / 11.4.6 |                                                                                                            |
| hyperhomologie                                                 | hyperhomology                                                   | 0_III.11.6.2          | Symmetric vocabulary to hypercohomology.                                                                   |
| limite projective (inductive)                                  | projective (inductive) limit                                    | 0_III.8.1.9 / 8.1.11  |                                                                                                            |
| localement constructible                                       | locally constructible                                           | 0_III.9.1.11          |                                                                                                            |
| loi de composition externe (interne)                           | external (internal) composition law                             | 0_III.8.2.1           |                                                                                                            |
| morphisme de suites spectrales                                 | morphism of spectral sequences                                  | 0_III.11.1.2          |                                                                                                            |
| morphisme fonctoriel                                           | functorial morphism                                             | 0_III.8.1.2           | I.e. a morphism in `Hom(𝒞°, Set)`; modern: natural transformation.                                         |
| `C`-objet en groupes, `C`-groupe, `C`-anneau, `C`-module       | `C`-object in groups, `C`-group, `C`-ring, `C`-module           | 0_III.8.2.3           |                                                                                                            |
| objet des bords, des cobords, des cycles, des cocycles         | object of boundaries, coboundaries, cycles, cocycles            | 0_III.11.2.1          |                                                                                                            |
| objet des images universelles                                  | object of universal images                                      | 0_III.13.1.1          |                                                                                                            |
| objet gradué associé à un système projectif satisfaisant (ML)  | graded object associated to a projective system satisfying (ML) | 0_III.13.4.2          |                                                                                                            |
| objet gradué limité inférieurement (supérieurement)            | graded object bounded below (above)                             | 0_III.11.2.1          |                                                                                                            |
| pleine (sous-catégorie)                                        | full (subcategory)                                              | 0_III.8.1.5           |                                                                                                            |
| pleinement fidèle (foncteur)                                   | fully faithful (functor)                                        | 0_III.8.1.5           |                                                                                                            |
| représentable (foncteur)                                       | representable (functor)                                         | 0_III.8.1.8           |                                                                                                            |
| résolution cohomologique                                       | cohomological resolution                                        | 0_III.11.4            |                                                                                                            |
| résolution droite / gauche                                     | right resolution / left resolution                              | 0_III.11.4            |                                                                                                            |
| résolution homologique                                         | homological resolution                                          | 0_III.11.4            |                                                                                                            |
| résolution injective / projective / libre / plate              | injective / projective / free / flat resolution                 | 0_III.11.4            |                                                                                                            |
| résolution de Cartan–Eilenberg (droite, injective)             | Cartan–Eilenberg resolution (right, injective)                  | 0_III.11.4.2          |                                                                                                            |
| résolution de Cartan–Eilenberg (gauche, projective)            | Cartan–Eilenberg resolution (left, projective)                  | 0_III.11.6.1          |                                                                                                            |
| rétrocompact (ensemble)                                        | retrocompact (set)                                              | 0_III.9.1.1           | A set whose intersection with every quasi-compact open is quasi-compact.                                   |
| semi-continue supérieurement (fonction)                        | upper semi-continuous (function)                                | 0_III.9.3.4           | EGA's "semi-continue supérieurement"; standard English form.                                               |
| sous-catégorie (pleine)                                        | (full) subcategory                                              | 0_III.8.1.5           |                                                                                                            |
| strict (système projectif)                                     | strict (projective system)                                      | 0_III.13.4.2          |                                                                                                            |
| système projectif                                              | projective system                                               | 0_III.8.1.9           |                                                                                                            |
| suite spectrale dans une catégorie abélienne                   | spectral sequence in an abelian category                        | 0_III.11.1.1          |                                                                                                            |
| suite spectrale dégénérée                                      | degenerate spectral sequence                                    | 0_III.11.1.6          |                                                                                                            |
| suite spectrale faiblement convergente                         | weakly convergent spectral sequence                             | 0_III.11.1.3          |                                                                                                            |
| suite spectrale régulière, corégulière, birégulière            | regular, coregular, biregular spectral sequence                 | 0_III.11.1.3          |                                                                                                            |
| suite spectrale d'un foncteur (relativement à un objet filtré) | spectral sequence of a functor (relative to a filtered object)  | 0_III.13.6.4          |                                                                                                            |
| suites spectrales d'un bicomplexe                              | spectral sequences of a bicomplex                               | 0_III.11.3.2          |                                                                                                            |
| suites spectrales d'hypercohomologie                           | hypercohomology spectral sequences                              | 0_III.11.4.3          |                                                                                                            |
| suites spectrales d'hyperhomologie                             | hyperhomology spectral sequences                                | 0_III.11.6.2          |                                                                                                            |
| système de coefficients                                        | system of coefficients                                          | 0_III.11.8.4          |                                                                                                            |
| complexe de chaînes `C_•(A)`, `L_•(A) = C_•(A)/D_•(A)`         | chain complex `C_•(A)`, `L_•(A) = C_•(A)/D_•(A)`                | 0_III.11.8.1          | `D_•(A)` = degenerate chains.                                                                              |
| complexe de cochaînes `C^•(A, B; 𝒮)`, `L^•(A, B; 𝒮)`           | cochain complex `C^•(A, B; 𝒮)`, `L^•(A, B; 𝒮)`                  | 0_III.11.8.4          | `L^•` is the bi-alternating sub-complex.                                                                   |
| edge-homomorphisme d'un bicomplexe                             | edge homomorphism of a bicomplex                                | 0_III.11.3.4          | `'E_2^{p,0} → H^p(K^{•,•})` from `Z_{II}^0(K^{•,•}) → K^{•,•}`.                                            |
| chaîne dégénérée                                               | degenerate chain                                                | 0_III.11.8.1          |                                                                                                            |
| complexe scindé                                                | split complex                                                   | 0_III.11.4.2          | A simple complex `L^{•,j}` where each `0 → Z → L → B → 0` is split.                                        |
| morphismes homotopes d'ordre `≤ k`                             | morphisms homotopic of order `≤ k`                              | 0_III.11.2.3          | After Cartan–Eilenberg `(M, XV, 3.1)`.                                                                     |
| résolution finie / de longueur `≤ n`                           | finite resolution / resolution of length `≤ n`                  | 0_III.11.4.1          |                                                                                                            |
| filtration régulière (d'un complexe)                           | regular filtration (of a complex)                               | 0_III.11.2.4          | `H^n(F^p(K^•)) = 0` for `p > u(n)`.                                                                        |
| théorème d'Eilenberg–Zilber                                    | Eilenberg–Zilber theorem                                        | 0_III.11.8.6          | Cited as `(G, I, 3.10.2)`.                                                                                 |
| formule de Künneth (pour `C_•(A) ⊗ C_•(B)`)                    | Künneth formula (for `C_•(A) ⊗ C_•(B)`)                         | 0_III.11.8.3          | Cited as `(G, I, 5.5.2)`.                                                                                  |
| `∞`-présentation finie (d'un module)                           | finite `∞`-presentation (of a module)                           | 0_III.11.9.3          | Forward reference to chap. IV.                                                                             |
| `𝒮`-`C`-module filtré, `gr^•(𝒮)`-`C`-module gradué             | `𝒮`-`C`-module filtered, `gr^•(𝒮)`-`C`-module graded            | 0_III.13.6.6          | Match the EGA convention attaching the species to the ambient structure.                                   |
| `gr^•(𝒮)`-`C`-module bigradué                                  | `gr^•(𝒮)`-`C`-module bigraded                                   | 0_III.13.6.6          |                                                                                                            |
| limité inférieurement (système projectif)                      | bounded below (projective system)                               | 0_III.13.4.1          | `A_k = 0` for `k < k_0`; matches "limité inférieurement" usage in `(0_III, 11.2.1)`.                       |
| condition (ML')                                                | condition (ML')                                                 | 0_III.13.2.4          | Topological variant: `f_{αγ}(A_γ)` dense in `f_{αβ}(A_β)` for `γ ≥ β`.                                     |
| filtration `𝔍`-bonne, `J`-bonne                                | `𝔍`-good filtration, `J`-good filtration                        | 0_III.13.7.7          | `𝔍 F^p(M) ⊂ F^{p+1}(M)` with equality for `p` large enough.                                                |
| sous-objet (sous-ensemble) des « images universelles »         | subobject (subset) of "universal images"                        | 0_III.13.1.1          | Quotes preserved from EGA.                                                                                 |
| objet gradué associé à un système projectif strict             | graded object associated to a strict projective system          | 0_III.13.4.2          | Notation `gr^•(𝐀)`.                                                                                        |
| `lim^{(i)}_←` (foncteurs dérivés droits de `lim_←`)            | `lim^{(i)}_←` (right-derived functors of `lim_←`)               | 0_III.13.2.4          | Introduced by allusion in EGA, cited via Roos `[28]`.                                                      |
| anneau `𝔍`-adique noethérien                                   | noetherian `𝔍`-adic ring                                        | 0_III.13.7.7          | EGA III §III.3, §III.4 context; matches `(0_I, 7.6)`.                                                      |

### Chapter III, Part 1

| French                                             | English                                          | First appearance | Note                                                                                        |
| -------------------------------------------------- | ------------------------------------------------ | ---------------- | ------------------------------------------------------------------------------------------- |
| algébrisable (`𝒪_X`-Module)                        | algebraizable (`𝒪_X`-module)                     | III.5.2.1        | EGA's "algébrisable"; "comes from an algebraic-coherent sheaf along the formal completion". |
| algébrisable (schéma formel)                       | algebraizable (formal scheme)                    | III.5.4.2        |                                                                                             |
| analytiquement intègre (anneau)                    | analytically integral (ring)                     | III.4.3.6        | Local ring whose completion is integral.                                                    |
| complexe de l'algèbre extérieure (Koszul)          | exterior algebra (Koszul) complex                | III.1.1.1        | EGA writes "complexe de l'algèbre extérieure"; matches modern "Koszul complex".             |
| exact (sous-ensemble) dans une catégorie abélienne | exact (subset) in an abelian category            | III.3.1.1        |                                                                                             |
| factorisation de Stein                             | Stein factorization                              | III.4.3.3        |                                                                                             |
| fini (morphisme de préschémas formels)             | finite (morphism of formal preschemes)           | III.4.8.2        |                                                                                             |
| fini (préschéma formel) au-dessus de `𝔇`, `𝔇`-fini | finite (formal prescheme) over `𝔇`, `𝔇`-finite   | III.4.8.2        |                                                                                             |
| genre arithmétique                                 | arithmetic genus                                 | III.2.5.1        | Of `X` over Artinian local `A`: `χ_A(𝒪_X)`.                                                 |
| géométriquement connexe (fibre)                    | geometrically connected (fiber)                  | III.4.3.4        |                                                                                             |
| nombre géométrique de composantes connexes (fibre) | geometric number of connected components (fiber) | III.4.3.4        |                                                                                             |
| partie propre (sur `𝔇`) d'un préschéma formel      | proper part (over `𝔇`) of a formal prescheme     | III.3.4.1        |                                                                                             |
| polynôme de Hilbert                                | Hilbert polynomial                               | III.2.5.3        | `P ∈ ℚ[T]` with `χ_A(ℱ(n)) = P(n)` for every `n ∈ ℤ`.                                       |
| propre (morphisme de préschémas formels)           | proper (morphism of formal preschemes)           | III.3.4.1        |                                                                                             |
| théorème de finitude                               | finiteness theorem                               | III.3.2.1        |                                                                                             |
| lemme de dévissage                                 | dévissage lemma                                  | III.3.1          | "Dévissage" kept in French per house style; the §III.3.1 lemma is (3.1.2).                  |
| lemme de Chow                                      | Chow's lemma                                     | III.3.2.1        | First applied in EGA III at (3.2.1); statement is `(II, 5.6.2)`.                            |
| schéma algébrique propre (sur un corps)            | proper algebraic scheme (over a field)           | III.3.2.3        |                                                                                             |
| `𝔍`-bonne (filtration)                             | `𝔍`-good (filtration)                            | III.3.4.4        | Matches `(0_III, 13.7.7)`.                                                                  |
| isomorphisme topologique                           | topological isomorphism                          | III.3.4.3        | Continuous bijective homomorphism with continuous inverse.                                  |
| théorème fondamental (des morphismes projectifs)   | fundamental theorem (of projective morphisms)    | III.2.2.1        | Serre's theorem: coherence of `R^q f_*(ℱ)`, vanishing/generation for `ℱ(n)`, `n ≫ 0`.       |
| théorème fondamental (des morphismes propres)      | fundamental theorem (of proper morphisms)        | III.4.1.1        | First comparison theorem between algebraic and formal theories; (4.1.5).                    |
| théorème de connexion (de Zariski)                 | connection theorem (of Zariski)                  | III.4.3.1        | Stein factorization existence; non-emptiness/connectedness of fibres of `f'`.               |
| « main theorem » de Zariski                        | "main theorem" of Zariski                        | III.4.4.3        | EGA keeps the English phrase, in quotes; we preserve it.                                    |
| premier théorème de comparaison                    | first comparison theorem                         | III.4.1.6        | Algebraic vs. formal theories; commutation of `R^n f_*` with completion.                    |
| critère d'amplitude                                | ampleness criterion                              | III.4.7.1        | If `ℒ ∣ X_y` is ample, then `ℒ` is ample on `f^{-1}(U)` for a neighbourhood `U` of `y`.     |
| caractéristique d'Euler–Poincaré (d'un faisceau)   | Euler–Poincaré characteristic (of a sheaf)       | III.2.5.1        | `χ_A(ℱ) = Σ (−1)^i long H^i(X, ℱ)` for `ℱ` coherent on `X` projective over Artinian `A`.    |
| conducteur de `ℬ` sur `𝒜`                          | conductor of `ℬ` over `𝒜`                        | III.2.6.2.4      | Largest quasi-coherent sub-`𝒜`-module of `𝒜` annihilating `ℬ/𝒜`.                            |
| accouplement par cup-produit                       | cup-product pairing                              | III.2.1.16       | `R^r f_*(𝒪_X(n)) × R^0 f_*(ω(−n)) → R^r f_*(ω)` defining Serre duality on `ℙ(ℰ)`.           |
| unibranche (anneau, point)                         | unibranch (ring, point)                          | III.4.3.6        |                                                                                             |
| universellement ouvert (morphisme)                 | universally open (morphism)                      | III.4.3.9        |                                                                                             |

### Chapter III, Part 2

| French                                                          | English                                                     | First appearance | Note                                                    |
| --------------------------------------------------------------- | ----------------------------------------------------------- | ---------------- | ------------------------------------------------------- |
| caractéristique d'Euler–Poincaré d'un complexe de modules       | Euler–Poincaré characteristic of a complex of modules       | III.7.9.5        |                                                         |
| cohomologiquement plat (en un point, sur `Y`, en dimension `p`) | cohomologically flat (at a point, on `Y`, in dimension `p`) | III.7.8.1        |                                                         |
| complexes homotopes                                             | homotopic complexes                                         | III.6.1.4        |                                                         |
| espace annelé de dimension cohomologique `≤ n`                  | ringed space of cohomological dimension `≤ n`               | III.6.5.5        |                                                         |
| extension des scalaires (dans un foncteur covariant additif)    | extension of scalars (in a covariant additive functor)      | III.7.1.3        |                                                         |
| faisceau d'anneaux de dimension cohomologique `≤ n`             | sheaf of rings of cohomological dimension `≤ n`             | III.6.5.5        |                                                         |
| formule de Künneth                                              | Künneth formula                                             | III.6.7.8        |                                                         |
| homologiquement plat (en un point, sur `Y`, en dim. `p`)        | homologically flat (at a point, on `Y`, in dim. `p`)        | III.7.8.1        |                                                         |
| homotopisme                                                     | homotopism                                                  | III.6.1.4        | A morphism of complexes that is a homotopy equivalence. |
| hypertor (de deux complexes de `A`-modules)                     | hypertor (of two complexes of `A`-modules)                  | III.6.3.1        |                                                         |
| hypertor local (de deux complexes de modules)                   | local hypertor (of two complexes of modules)                | III.6.4.1        |                                                         |
| hypertor global (de deux complexes de modules)                  | global hypertor (of two complexes of modules)               | III.6.6.2        |                                                         |
| hypertor relatif à deux recouvrements                           | hypertor relative to two covers                             | III.6.6.2        | `Tor_n^S(𝔘^{(1)}, 𝔘^{(2)}; 𝒫_•^{(1)}, 𝒫_•^{(2)})`.      |
| hypercohomologie d'un recouvrement (notation `H^{−n}`)          | hypercohomology of a cover (negative-degree convention)     | III.6.6.1        | Used when the differential is of degree `−1`.           |
| produit tensoriel externe `ℱ ⊗_S 𝒢`                             | external tensor product `ℱ ⊗_S 𝒢`                           | III.6.5.3        | Reduces to `𝒯or_0^S(ℱ, 𝒢)`; cf. `(I, 9.1.2)`.           |
| dimension cohomologique finie (faisceau, espace annelé)         | finite cohomological dimension (sheaf, ringed space)        | III.6.5.5        |                                                         |
| recouvrement plus fin                                           | finer cover                                                 | III.6.6.7        | EGA's "plus fin"; standard English.                     |
| résolution projective de Cartan–Eilenberg                       | Cartan–Eilenberg projective resolution                      | III.6.3.1        | Already listed for 0_III.11.6.1; first §III.6 use.      |
| polynôme de Hilbert relatif à un complexe de modules            | Hilbert polynomial relative to a complex of modules         | III.7.9.12       |                                                         |
| suites spectrales de Künneth                                    | Künneth spectral sequences                                  | III.6.7.3        |                                                         |
| `Ab`, `Ab_A` (catégories de modules)                            | `Ab`, `Ab_A` (categories of modules)                        | III.7.1.1        | `Ab_A` = left `A`-modules; `Ab` = `Z`-modules.          |
| foncteur covariant additif `A`-linéaire                         | covariant additive `A`-linear functor                       | III.7.1.2        |                                                         |
| `T_{(B)}`, `T^{(B)}`, `T ⊗_A B` (extension des scalaires)       | `T_{(B)}`, `T^{(B)}`, `T ⊗_A B` (extension of scalars)      | III.7.1.3        | Three EGA notations for the base-changed functor.       |
| `T_𝔭` (localisation d'un foncteur)                              | `T_𝔭` (localization of a functor)                           | III.7.1.4        | `T_𝔭 = T_{(A_𝔭)}` when `𝔭` is a prime ideal of `A`.     |
| homomorphisme canonique `t_M : T(A_s) ⊗_A M → T(M)`             | canonical homomorphism `t_M : T(A_s) ⊗_A M → T(M)`          | III.7.2.2        | Comparison map for an additive functor.                 |
| foncteur homologique de modules                                 | homological functor of modules                              | III.7.3.1        | Cf. `(T, II, 2.1)`.                                     |
| `d_p(x) = rang_{κ(x)} T_p(κ(x))`                                | `d_p(x) = rang_{κ(x)} T_p(κ(x))`                            | III.7.6.6        | Fibrewise rank function on `Spec(A)`.                   |
| propriété d'échange                                             | exchange property                                           | III.7.7.5        | Bijectivity of `𝒯_p(𝒪_Y) ⊗_{𝒪_Y} ℳ → 𝒯_p(ℳ)`.           |
| propriété de semi-continuité                                    | semi-continuity property                                    | III.7.7.5        | Upper semi-continuity of `y ↦ rang_{κ(y)} T_p(κ(y))`.   |
| revêtement étale                                                | étale cover                                                 | III.7.8.10       | Forward reference to chap. IV.                          |
| `EP(f, 𝒫_•; y)`, `EP(Y, 𝒫_•; y)`, `EP(𝒫_•; y)`                  | `EP(f, 𝒫_•; y)`, `EP(Y, 𝒫_•; y)`, `EP(𝒫_•; y)`              | III.7.9.5        | Euler–Poincaré characteristic at a point.               |
| `PH(f, 𝒫_•; y)`, `PH(𝒫_•; y)` (polynôme de Hilbert)             | `PH(f, 𝒫_•; y)`, `PH(𝒫_•; y)` (Hilbert polynomial)          | III.7.9.11       |                                                         |
| critère d'exactitude de Grauert                                 | Grauert exactness criterion                                 | III.7.6.9        | The semi-continuity / continuity dichotomy.             |

## Translator's policy notes

- "Préschéma formel" → "formal prescheme" throughout. EGA III §III.3–§III.4 develop proper morphisms of formal
    preschemes anticipating the full Chapter I §10 treatment.
- "Système projectif satisfaisant `(ML)`" stays as "projective system satisfying `(ML)`" rather than "inverse system" —
    match EGA's vocabulary.
- "Koszul complex" is the modern name for what EGA calls `complexe de l'algèbre   extérieure K•(f)`. We render the EGA
    name with a translator's note at first use in §III.1.1.1 and use "Koszul" elsewhere only when no ambiguity is
    risked.
- "Caractéristique d'Euler–Poincaré" stays as Euler–Poincaré characteristic (not "Euler characteristic" alone — EGA's
    nomenclature is settled).
- "Suites spectrales de changement de base" → base-change spectral sequences (EGA III §III.6.9). Distinct from the
    base-change spectral sequences for `Tor` and `Ext` in `(0_III, 12.5)`.
- "Suites spectrales d'associativité" → associativity spectral sequences (EGA III §III.6.8); the corresponding spectral
    *functor* is called "associativity spectral functor" (foncteur spectral d'associativité).
- "Foncteur spectral" rendered as "spectral functor" (not "spectral sequence functor"); EGA's term is the family of
    spectral sequences attached to a parameter (the `𝒫_•^{(i)}` here).
- For §III.6.7: EGA writes `ℋ^{-n}(f, 𝒫_•)` for hypercohomology in *negative-degree* convention (matching `R^n f_*` via
    `n ↦ −n`). We preserve this sign convention literally; the hypertor abutment `𝒯or^S_n` is indexed by `n`, and the
    `(b)`-type sequence relates it to `ℋ^{-p}(f_1 ×_S f_2, −)`.
- "Edge-homomorphisme" → edge homomorphism (no hyphen in English); cf. ledger entry at `0_III.12.1.7`.

### Part B of §III.6 (subsections 6.7–6.9)

Source file: `13-c3-s06-foncteurs-tor-formule-kunneth.md`, lines 922–1613. Output file:
`14-ch3-06-tor-functors-kunneth-formula.md` (§§6.7–6.9 portion of the concatenated file). PDF pages: EGA-III-2 pp.
25–39.

Subsection coverage:

- §6.7 (lines 922–1257): global hypertor of complexes of quasi-coherent modules; Künneth formula (6.7.8); the six
    spectral sequences `(a), (a'), (b), (b'), (c), (d)` of (6.7.3); finite-index extension (6.7.11); functoriality under
    change of `S`-preschemes (6.7.10).
- §6.8 (lines 1258–1324): associativity spectral functor `^{(e)}𝓔` of (6.8.2); affine corollary (6.8.3).
- §6.9 (lines 1325–1613): base-change spectral sequences `^{(e)}𝓔, ^{(f)}𝓔, ^{(f')}𝓔` of (6.9.3); flat-`g` reduction
    (6.9.2); degenerate-case isomorphisms (6.9.6); uniform `N`-bound (6.9.7); `m = 1` restatement (6.9.8); fibrewise
    commutation (6.9.10).

### Part C of §III.6 (subsection 6.10)

Source file: `13-c3-s06-foncteurs-tor-formule-kunneth.md`, lines 1615–end. Output file:
`14-ch3-06-tor-functors-kunneth-formula.md` (§6.10 portion of the concatenated file). PDF pages: EGA-III-2 pp. 39–43.

Subsection coverage:

- §6.10 (lines 1615–end): local structure of certain cohomological functors. Proposition (6.10.1) establishes the
    existence of a quasi-coherent `S`-flat complex `𝒦_•` on `Y` with `𝒯or^S_• ⥲ ℋ_•(𝒦_• ⊗_S ℱ_•')` and the
    base-change-functorial diagram (6.10.1.2). Corollary (6.10.2) gives boundedness improvements. Remarks (6.10.3)
    record the spectral sequence (e), the homotopy non-uniqueness of `𝒦_•`, and the free / finite-cover refinement.
    Scholium (6.10.4) explains why hypertor is the right tool when flatness fails. Theorem (6.10.5) is the noetherian
    proper-morphism specialization (`n = 1`, `Y = S`, `𝒫_•` `Y`-flat coherent): the complex `ℒ_•` may be taken
    associated to free `A`-modules of finite type. Remark (6.10.6) records the single-coherent-sheaf case and asks the
    converse question about realizing a given complex of projectives.

### Translator's policy notes — Part C

- `𝒦_•` and `ℒ_•`: EGA uses cursive script-K and script-L for the two complexes appearing in (6.10.1) and (6.10.5). We
    render them as `𝒦_•` and `ℒ_•` respectively, matching the script-X conventions established in Parts A and B.
- `ℋ_•(𝒦_• ⊗_S ℱ_•')` denotes the homology sheaves of the chain complex of `𝒪_Y`-modules `𝒦_• ⊗_S ℱ_•'`, taken termwise.
    This is *not* a hypercohomology of a functor; it is the homology of a complex of sheaves. The locked cohomology
    notation `ℋ^•(f, …)` (hyperderived-functor of `f_*`) is reserved for the LHS of `(6.10.5.1)`, matching Part B's
    sign-convention discussion at the bottom of the policy notes.
- `(6.10.3.1)` interprets the spectral sequence `(e)` of `(6.9.3)` in the present flat-`𝒦_•` setting. EGA writes the
    `E_2` term using a hyperhomology-of-`ℱ_•'` slot; when `ℱ_•'` is concentrated in degree `0` this collapses to
    `𝒯or^S_p(ℋ_q(𝒦_•), ℱ')`. We keep the general form `⊕_{q' + q'' = q} 𝒯or^S_p(ℋ_{q'}(𝒦_•), ℋ_{q''}(ℱ_•'))`.
- `(0, 11.5.2.1) "dualized"`: EGA's literal "« dualisée »". We preserve the quoted hint as in the source.

# Translation conventions — EGA III

These conventions are locked after the §III.1 calibration pass. They **inherit** the EGA II conventions at
`docs/books/ega/ii/conventions.md` verbatim; only the EGA-III-specific additions for cohomology, derived functors,
spectral sequences, and the running Chapter 0_III preliminaries are recorded here.

## 1. Inherited from EGA II

Terminology table (§1), math glyphs and Unicode policy (§2), block labels (§3), numbered displays and cross-references
(§4), pagination comments (§5), proof idioms (§6), source-trace footer format (§7), translator-note guidance (§8), and
modality preservation (§9) all transfer unchanged. Re-read those sections in `docs/books/ega/ii/conventions.md` before
extending the ledger or making a stylistic choice here.

## 2. Cross-volume citations specific to EGA III

EGA III uses the running Chapter 0 (suite) — call it Chapter 0_III — and cites the preliminaries of EGA I as plain
"Chapter 0". To keep the two distinguishable in print we write them differently:

- `(0_III, 10.3.1)` cites a paragraph in `03-ch0-10-complements-flat-modules.md` (Chap 0_III §10).
- `(0, 4.2.4)` cites Chapter 0 in EGA I.
- `(I, 4.2.3)`, `(II, 5.5.4)` cite EGA I, EGA II respectively.
- `(III, 2.3.8)` cites EGA III itself; later volumes use this form.

EGA III also routinely cites four external classics, which we render literally:

| Source key in EGA III | Work                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------- |
| `(M, …)`              | H. Cartan and S. Eilenberg, *Homological Algebra* (Princeton, 1956).                  |
| `(G, …)`              | R. Godement, *Topologie algébrique et théorie des faisceaux* (Hermann, 1958).         |
| `(T, …)`              | A. Grothendieck, *Sur quelques points d'algèbre homologique* (Tôhoku Math. J., 1957). |
| `(FAC, …)`            | J.-P. Serre, *Faisceaux algébriques cohérents* (Annals of Math., 1955).               |

Where the source spells these out (e.g. "Cartan–Eilenberg, *loc. cit.*"), we keep the spelling and add the bracketed key
in the bibliography.

## 3. Complex and cohomology notation

EGA III routinely manipulates chain and cochain complexes, bicomplexes, total complexes, derived and hyper-derived
functors. We fix the following Unicode rendering; display long expressions in fenced ```` ```text ```` blocks as in EGA
II.

- Complexes: `K•` and `K_•` (lower-degree boundary) for chain complexes, `K•` and `K^•` (upper-degree boundary) for
    cochain complexes. EGA's `K^•` and `K_•` are rendered with explicit `^•` / `_•` whenever the context could confuse
    them.
- Bicomplexes: `K^{p,q}`, `K_{p,q}`.
- Total complex: `s(K)` (EGA's preferred notation; matches Cartan–Eilenberg); occasionally `Tot(K)` when the source uses
    that.
- Cocycles, coboundaries, cohomology: `Z^i(K)`, `B^i(K)`, `H^i(K)`, with matching lower-indexed `Z_i`, `B_i`, `H_i` for
    chain complexes.
- Cohomology of a sheaf or module: `H^i(X, ℱ)`, `H^i(𝔘, ℱ)` (open cover), `H^i(U, ℱ)` (open set).
- Derived functors: `R^i F`, `R F` (right-derived; covariant), `L_i F`, `LF` (left).
- Hyper-derived: `R^• T(K^•)`, `L_• T(K_•)` for hypercohomology and hyperhomology of a complex; `R^• T(K^•, K'^•)`,
    `L_• T(K_•, K'_•)` for bifunctors.
- Higher direct images: `R^i f_* ℱ`, `R f_* ℱ`.
- Tor and Ext: `Tor_i(A, B)`, `Tor_i^A(M, N)`, `Ext^i(A, B)`, `Ext^i_A(M, N)`.
- Hypertor: `𝒯or_i(K_•, K'_•)`, `Tor_i(M_•, N_•)`, with subscripts as in the source.
- Filtration: `F^•`, `F_•`, `gr^•`, `gr_•`. Graded object associated to a filtration: `gr(K)`.

## 4. Spectral sequences

EGA III's central objects. We render every spectral sequence in the canonical "page, indices, abutment" form:

````
```text
  E_2^{p,q} = H^p(Y, R^q f_* ℱ) ⟹ H^{p+q}(X, ℱ).
````

````

- The page index is the subscript: `E_r^{p,q}` (cohomological) or `E^r_{p,q}` (homological).
- The differential is `d_r : E_r^{p,q} → E_r^{p+r, q-r+1}`.
- Abutment uses `⟹` ("abuts to" / "converges to" — both English forms occur in EGA; we render either by `⟹` when the
  source uses `⟹` or the equivalent French "aboutit à"; we keep "abuts to" in prose since it's the canonical English
  form).
- For filtered complexes we name the filtration: `F^p H^n` is the `p`th piece of the filtration on `H^n` induced by the
  filtration on the complex.
- Convergence properties: `weakly convergent`, `regular`, `coregular`, `biregular`, `degenerate` — match
  `(0_III, 11.1.3)` and `(0_III, 11.1.6)`.

## 5. Cech cohomology

- `C^•(𝔘, ℱ)` for the Čech cochain complex of `ℱ` with respect to the cover `𝔘`.
- `Ȟ^•(X, ℱ)` (with caron) when EGA distinguishes Čech from derived cohomology; otherwise `H^•(𝔘, ℱ)` for the Čech
  cohomology of the cover `𝔘`.
- We never silently identify Čech and derived cohomology; preserve EGA's bookkeeping.

## 6. Modules and sheaves

- `𝒪_X`-module: `𝒪_X`-module (lowercase per EGA II convention; the type comes from the prefix).
- Quasi-coherent / coherent: as in EGA II.
- A module on a topological space `X` whose support is at most `n`-dimensional: EGA writes `dim ≤ n`; render as
  `cohomological dimension ≤ n` when EGA does, and `dim_X ℱ ≤ n` for support otherwise.
- Filtered, graded, bigraded `𝒮`–C-module, `gr^•(𝒮)`-C-module: render `S`-`C`-module filtré, etc., in the form
  `𝒮`-`𝒞`-module filtered, `gr^•(𝒮)`-`𝒞`-module graded — following the EGA convention of attaching the module species
  to the ambient structure.

## 7. The Mittag–Leffler condition

EGA III §0_III.13 introduces condition `(ML)` for projective systems. We keep the EGA abbreviation. Related vocabulary:

| French                                     | English                                   |
| ------------------------------------------ | ----------------------------------------- |
| condition `(ML)`                           | condition (ML) / Mittag–Leffler condition |
| système projectif strict                   | strict projective system                  |
| système projectif essentiellement constant | essentially constant projective system    |
| objet des images universelles              | object of universal images                |

## 8. Formal preschemes (forward references)

EGA III §III.3 and §III.4 use formal preschemes (`préschémas formels`) and properness relative to a formal base,
anticipating EGA I, ch. I §10 (formal preschemes) and forthcoming material. Render:

- `préschéma formel` → formal prescheme.
- `fini sur 𝔇`, `𝔇-fini` → finite over `𝔇`, `𝔇`-finite.
- `propre sur 𝔇` → proper over `𝔇`.
- Stein factorization, geometric fiber, geometric number of connected components: standard English terms.

## 9. Spectral-sequence-specific terminology

| French                                 | English                             |
| -------------------------------------- | ----------------------------------- |
| aboutissement                          | abutment                            |
| bicomplexe                             | bicomplex                           |
| caractéristique d'Euler–Poincaré       | Euler–Poincaré characteristic       |
| co-séparé, co-discrète                 | co-separated, co-discrete           |
| cohomologiquement plat                 | cohomologically flat                |
| complexe défini par un bicomplexe      | complex defined by a bicomplex      |
| cup-produit                            | cup product                         |
| cochaîne bi-alternée                   | bi-alternating cochain              |
| filtration co-discrète                 | co-discrete filtration              |
| hypercohomologie                       | hypercohomology                     |
| hyperhomologie                         | hyperhomology                       |
| polynôme de Hilbert                    | Hilbert polynomial                  |
| résolution de Cartan–Eilenberg         | Cartan–Eilenberg resolution         |
| résolution cohomologique               | cohomological resolution            |
| résolution droite / gauche             | right resolution / left resolution  |
| résolution injective / projective      | injective / projective resolution   |
| résolution libre / plate               | free / flat resolution              |
| résolution homologique                 | homological resolution              |
| suite spectrale                        | spectral sequence                   |
| suite spectrale dégénérée              | degenerate spectral sequence        |
| suite spectrale faiblement convergente | weakly convergent spectral sequence |
| suite spectrale régulière              | regular spectral sequence           |
| système de coefficients                | system of coefficients              |

## 10. EGA-III-specific terminology

These extend the EGA II terminology table; they first appear in the §III.1 calibration and the Chap 0_III preliminaries.

| French                                             | English                                        |
| -------------------------------------------------- | ---------------------------------------------- |
| algébrisable (`𝒪_X`-Module)                        | algebraizable (`𝒪_X`-module)                   |
| algébrisable (schéma formel)                       | algebraizable (formal scheme)                  |
| analytiquement intègre                             | analytically integral                          |
| application quasi-compacte                         | quasi-compact map                              |
| augmentation d'une résolution                      | augmentation of a resolution                   |
| complexe de l'algèbre extérieure                   | exterior algebra complex                       |
| complexe de Koszul                                 | Koszul complex                                 |
| condition (TF), condition (TN)                     | condition (TF), condition (TN)                 |
| constructible (partie, ensemble)                   | constructible (subset, set)                    |
| constructible (fonction)                           | constructible (function)                       |
| dihomomorphisme                                    | di-homomorphism                                |
| exact (sous-ensemble) dans une catégorie abélienne | exact (subset) in an abelian category          |
| factorisation de Stein                             | Stein factorization                            |
| filtration                                         | filtration                                     |
| fini (morphisme de préschémas formels)             | finite (morphism of formal preschemes)         |
| foncteur représentable                             | representable functor                          |
| foncteur covariant canonique `C → Hom(C°, Ens)`    | canonical covariant functor `C → Hom(C°, Set)` |
| genre arithmétique                                 | arithmetic genus                               |
| géométriquement connexe                            | geometrically connected                        |
| localement constructible                           | locally constructible                          |
| loi de composition externe / interne               | external / internal composition law            |
| morphisme de suites spectrales                     | morphism of spectral sequences                 |
| nombre géométrique de composantes connexes         | geometric number of connected components       |
| `C`-objet en groupes                               | `C`-object in groups                           |
| `C`-groupe, `C`-anneau, `C`-module                 | `C`-group, `C`-ring, `C`-module                |
| objet final d'une catégorie                        | final object of a category                     |
| partie propre (sur 𝔇)                              | proper part (over `𝔇`)                         |
| pleine (sous-catégorie)                            | full (subcategory)                             |
| pleinement fidèle (foncteur)                       | fully faithful (functor)                       |
| polynôme de Hilbert                                | Hilbert polynomial                             |
| propre (morphisme de préschémas formels)           | proper (morphism of formal preschemes)         |
| représentable (foncteur)                           | representable (functor)                        |
| rétrocompact                                       | retrocompact                                   |
| unibranche (anneau, point)                         | unibranch (ring, point)                        |
| universellement ouvert                             | universally open                               |

## 11. Two-part packaging

The 1961 first part and the 1963 second part are translated in one repository tree. We keep:

- two front-matter files, one per part (`00-front-matter-part-1.md`, `13-front-matter-part-2.md`),
- one merged terminology index, alphabetized,
- one merged notation index, source-ordered with subheadings for Chap 0_III, Chap III Part 1, and Chap III Part 2,
- one merged bibliography.

The merged back matter is the reader's surface. Each translated file's `<!-- source: … -->` footer still points to its
original Part 1 or Part 2 OCR file.

## 12. Source-trace footer

Each translated section ends with:

```html

````

When no LaTeX cross-reference exists (e.g. for §III.6 and §III.7), the `cross-ref:` line is omitted.

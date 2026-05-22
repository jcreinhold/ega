# Translation conventions — EGA IV

These conventions are locked after the §IV.1 calibration pass. They **inherit** the EGA III conventions at
$docs/books/ega/iii/conventions.md$ verbatim (which in turn inherit EGA II); only the EGA-IV-specific additions for
commutative algebra, formal smoothness, derivations and differentials, Jacobson preschemes, étale morphisms, regular
immersions, meromorphic functions, and divisors are recorded here.

## 1. Inherited from EGA III

The full EGA III conventions transfer unchanged: the terminology table, math glyphs and Unicode policy, block label
format (`<!-- label: IV.N.M.K -->`), numbered display blocks in fenced ```` ```text ```` blocks, page-break comments
(`<!-- original page N -->`), source-trace footer format, translator-note guidance, modality preservation, cohomology
and spectral-sequence rendering, Čech cohomology bookkeeping, condition (ML) terminology, formal-prescheme vocabulary,
and the citation forms for $(I, \cdots)$, $(II, \cdots)$, $(III, \cdots)$, $(0, \cdots)$, $(0_{III}, \cdots)$, $(M,
\cdots)$, $(G, \cdots)$, $(T, \cdots)$, $(FAC, \cdots)$. Re-read those sections in $docs/books/ega/iii/conventions.md$
before extending the ledger or making a stylistic choice here.

**Block labels.** English: $**Proposition (1.1.4).**$, $**Definition (1.2.1).**$, $**Corollary (1.2.3).**$, $**Theorem
(1.8.4) (Chevalley).**$, $**Lemma (3.2.1).**$, $**Remark (1.6.4).**$, $**Scholium (2.3.3).**$. Never French
("Définition", "Corollaire", etc.). Each labeled block is followed by a blank line, the `<!-- label: IV.N.M.K -->`
comment, another blank line, then the italicized body.

**Proofs.** EGA IV follows the inline-prose convention: a proof begins immediately after the labeled italic body, in
ordinary (non-italic) prose, *without* an explicit $**Proof.**$ marker. (This is a deliberate divergence from EGA III's
explicit-marker convention; it matches the typographical style of the printed EGA IV, where short proofs are not always
marked "Démonstration." in the source.) Long, multi-step proofs may use sub-paragraph markers like "Step 1.", "(a)", or
"(i)" inline; do not insert a $**Proof.**$ header retroactively.

## 2. Cross-volume citations specific to EGA IV

EGA IV continues the running Chapter 0 from EGA III at §14 — call it Chapter 0_IV — and is cited by later volumes (and
within itself) as Chapter IV. To keep the two distinguishable in print we write them differently:

- $(0_{IV}, 19.3.5)$ cites a paragraph in `06-ch0-19-formally-smooth-algebras.md` (Chap 0_IV §19).
- `(IV, 17.6.2)` cites EGA IV itself (used by later EGA volumes and by cross-section references inside EGA IV).
- $(0_{III}, 13.4.2)$ cites Chap 0_III in EGA III.
- `(III, 2.3.8)`, `(II, 5.5.4)`, `(I, 4.2.3)`, `(0, 4.2.4)` cite EGA III, EGA II, EGA I, and Chapter 0 of EGA I,
  respectively.

EGA IV cites several external classics. We extend the EGA III table:

| Source key in EGA IV                    | Work                                                                                  |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| $(M, \cdots)$                           | H. Cartan and S. Eilenberg, _Homological Algebra_ (Princeton, 1956).                  |
| $(G, \cdots)$                           | R. Godement, _Topologie algébrique et théorie des faisceaux_ (Hermann, 1958).         |
| $(T, \cdots)$                           | A. Grothendieck, _Sur quelques points d'algèbre homologique_ (Tôhoku Math. J., 1957). |
| $(FAC, \cdots)$                         | J.-P. Serre, _Faisceaux algébriques cohérents_ (Annals of Math., 1955).               |
| `(Bourbaki, Alg. comm., …)`             | N. Bourbaki, _Éléments de mathématique : Algèbre commutative_ (Hermann, 1961-1965).   |
| $(Bourbaki, Alg., \cdots)$              | N. Bourbaki, _Éléments de mathématique : Algèbre_ (Hermann, 1942-).                   |
| $(Bourbaki, Top. g\acute{e}n., \cdots)$ | N. Bourbaki, _Éléments de mathématique : Topologie générale_ (Hermann, 1940-).        |

Bourbaki citations are rendered in the EGA form `(Bourbaki, Alg. comm., chap. II, §3, n° 4)` or shorter
`(Bourbaki, Alg. comm., II, §3, n° 4)` when that matches the source. Page numbers are kept when present;
chapter/section/n° structure is preserved verbatim. Where EGA spells out the title (e.g. "Bourbaki, _Algèbre
commutative_, chap. II, §3, n° 4"), we keep the spelling and add the bracketed key in the bibliography.

The Nagata text *Local Rings* (Interscience, 1962) is cited as $(Nagata, \cdots)$ with chapter and section number.
Zariski- Samuel *Commutative Algebra* (Van Nostrand, 1958-1960) is cited as $(Zariski-Samuel, \cdots)$ with volume,
chapter, section.

## 3. Differential and formal-smoothness notation

EGA IV §§0_IV.19-22 and §§IV.16-18 work systematically with derivations, differentials, and the family of formal-
smoothness conditions. We fix the following Unicode rendering; display long expressions in fenced ```` ```text ````
blocks.

- Module of relative differentials (rings): $\Omega_{B/A}$. EGA writes $\Omega^{1}_{B/A}$; we render as $\Omega_{B/A}$
  when no higher differentials are in play and as $\Omega^{1}_{B/A}$ when the source needs the index for disambiguation.
- Higher exterior powers: $\Omega^{p}_{B/A} = \Lambda^{p} \Omega_{B/A}$.
- Module of relative differentials (schemes): $\Omega^{1}_{X/Y}$ (or $\Omega_{X/Y}$ when no index is needed); locally on
  $\operatorname{Spec}(B) \to \operatorname{Spec}(A)$ this is $\Omega^{1}_{B/A}$ glued.
- Universal derivation: $d : B \to \Omega_{B/A}$, $d_{B/A}$ when the source/target needs naming.
- Derivation modules: $\operatorname{Der}_{A}(B, M)$, $\operatorname{Der}(B, M)$ (when $A$ is understood); EGA's
  $T_{B/A}(M)$ notation is preserved when used.
- Frobenius: $F : A \to A$, $a \mapsto a^{p}$ (characteristic $p > 0$).
- $p$-basis: a family $(b_{i})$ whose images in $A/A^{p}$ form a basis (EGA's "$p$-base"). We render $p$-base →
  "$p$-basis".
- Imperfection module: $\Upsilon_{B/A}$ (EGA's "module d'imperfection"; pronounce "upsilon" or render literally).
- Differential criteria for smoothness, étaleness, unramifiedness: EGA's `(D_I)`, $(D_{II})$, $(D_{III})$ letter-pair
  labels are preserved literally.

## 4. Formal smoothness / étaleness / unramifiedness

EGA IV §0_IV.19 and §IV.17 introduce the family of "formally $P$" properties ($P \in {smooth, \acute{e}tale,
unramified}$). We fix the terminology as follows:

| French                   | English               | Note                                                     |
| ------------------------ | --------------------- | -------------------------------------------------------- |
| formellement lisse       | formally smooth       | For a topology; usually $J$-adic or discrete             |
| formellement étale       | formally étale        |                                                          |
| formellement non ramifié | formally unramified   |                                                          |
| lisse                    | smooth                | Locally of finite presentation + formally smooth         |
| étale                    | étale                 | Smooth + unramified, equivalently …                      |
| non ramifié              | unramified            | Locally of finite presentation + Ω^1 = 0                 |
| différentiellement lisse | differentially smooth | EGA IV §16; weaker than smooth in non-Noetherian setting |

Where EGA writes "formellement lisse pour la topologie $\mathcal{J}$-préadique", we render "formally smooth for the
$\mathcal{J}$-preadic topology". The qualifier ("for the discrete topology", "for the $J$-adic topology", etc.) is kept;
do not silently drop it. EGA's stylistic device of inserting the topology as a parenthetical adverb is preserved when it
occurs.

## 5. Dimension, depth, regularity

EGA IV §§0_IV.14-17 fix the combinatorial-dimension and depth machinery. We fix:

- Combinatorial / Krull dimension of a topological space: $\dim(X)$.
- Local dimension at a point: $\dim_{x}(X)$.
- Codimension of $Y$ in $X$ at a point $y$: $codim_{y}(Y, X)$.
- Depth (`profondeur`): $prof(M)$, $prof_{\mathfrak{m}}(M)$. We render the EGA symbol `prof` rather than English `depth`
  because the symbol is the entry in the notation index; the term "depth" appears in English running prose.
- Regular system of parameters: $(t_{1}, \cdots, t_{n})$ with $(t_{1}, \cdots, t_{n})\cdot A = \mathfrak{m}$ and $n =
  \dim(A)$.
- Cohen-Macaulay: EGA's "anneau de Cohen-Macaulay" → "Cohen-Macaulay ring"; the abbreviation `(CM)` is preserved where
  used.
- Regular: EGA's "régulier" → "regular".
- $M$-regular sequence ($suite M-r\acute{e}guli\grave{e}re$): a sequence $(f_{1}, \cdots, f_{n})$ such that each $f_{i}$
  is a non-zero-divisor on $M / (f_{1}, \cdots, f_{i-1})M$.
- $\mathcal{F}$-regular sequence ($suite \mathcal{F}-r\acute{e}guli\grave{e}re$): the sheaf-of-modules version; rendered
  with the script $\mathcal{F}$.

## 6. Jacobson preschemes and constructibility (§§IV.9-10)

- Jacobson prescheme: EGA's "préschéma de Jacobson"; we render literally and capitalize "Jacobson" throughout.
- Jacobson condition: `(J)`, parenthesized as in EGA.
- Very dense subset: EGA's "partie très dense"; we render literally.
- Constructible function/set: inherited from $(0_{III}, 9.1.x)$ rendering.

## 7. Étale morphisms, henselian rings (§§IV.17-18)

- Étale morphism: as above. The EGA family-of-properties is rendered exactly: étale, étale at a point, locally étale, …
- Henselian local ring: EGA's "anneau local hensélien" → "Henselian local ring" (capitalize Hensel).
- Strict Henselization: EGA's "hensélisation stricte" → "strict Henselization".
- Hensel's lemma: EGA's "lemme de Hensel" → "Hensel's lemma".
- Étale cover (revêtement étale): "étale cover" (EGA III ledger; reinforced here).

## 8. Regular immersions, divisors (§§IV.19, IV.21)

- Regular immersion of codimension $n$: EGA's "immersion régulière"; we render literally. Definition at $(0_{IV},
  15.x)$.
- Transversally regular immersion: EGA's "immersion transversalement régulière"; locked at §IV.19.1.
- Sheaf of meromorphic functions: $\mathcal{M}_{X}$, $\mathcal{M}^{\times}_{X}$. (Distinct from $\mathcal{M}_{X}$, which
  EGA uses for ideal sheaves; check context.)
- Cartier divisor: EGA's "diviseur de Cartier"; locked at §IV.21.1.
- Weil divisor: EGA's "diviseur de Weil"; locked at §IV.21.6.
- Picard group: $\operatorname{Pic}(X)$.
- Locally principal divisor / locally factorial scheme: render literally.

## 9. Excellent rings (§IV.7)

EGA IV §IV.7 introduces "excellent rings" with a long list of formal properties. The term is preserved verbatim:
"excellent ring", "anneau excellent". Sub-properties:

- Japanese ring / Nagata ring: EGA's "anneau japonais"; we render literally (matches §0_IV.23). EGA's vocabulary is
  older than Nagata's "pseudo-geometric ring" / Matsumura's "Nagata ring"; we keep "Japanese ring" with a one-line
  translator's note at first appearance.
- Universally Japanese: EGA's "universellement japonais"; locked at §0_IV.23.1.
- (G)-ring, (G)-property: EGA's `(G)` for "Grothendieck"; preserved literally in `(IV, 7.x)`.

## 10. EGA-IV-specific terminology

These extend the EGA III terminology tables; they first appear in the §IV.1 calibration and the Chap 0_IV preliminaries.
Locked piecewise as each section lands. The current table is in [translation-ledger.md](translation-ledger.md).

## 11. Four-part packaging

The 1964 first part, 1965 second part, 1966 third part, and 1967 fourth part are translated in one repository tree. We
keep:

- four front-matter files, one per part (`00-front-matter-part-1.md`, `13-front-matter-part-2.md`,
  `20-front-matter-part-3.md`, `28-front-matter-part-4.md`),
- one merged terminology index, alphabetized, with chapter prefix where ambiguous (`0_IV` vs `IV`),
- one merged notation index, source-ordered with subheadings for Chap 0 (continued) and Chap IV Parts 1-4,
- one merged bibliography.

The merged back matter is the reader's surface. Each translated file's $<!-- source: \cdots -->$ footer still points to
its original Part 1, 2, 3, or 4 OCR file.

## 12. §IV.11

EGA IV Part 3 (1966) prints §§8, 9, 10, 11, 12, 13, 14, 15 — including §11. The 1964 sommaire announced §11 as
"Topological properties of flat morphisms of finite presentation; local criteria of flatness" with the footnote that the
order and content of §§11-21 are tentative; the published §11 followed that announcement. (Older secondary literature
occasionally treats §11 as unpublished; this is incorrect.) The §11 file lives at
`23a-ch4-11-flatness-loci-and-descent.md` in the translation tree, ordered between §10 and §12. Subsequent
flatness-descent developments that build on §11 include Raynaud-Gruson, _Critères de platitude et de projectivité_
(Inventiones math. 13, 1971), and the étale-cohomology projects of SGA 4½.

## 13. Source-trace footer

Each translated section ends with:

```html

```

When no LaTeX cross-reference exists, the $cross-ref:$ line is omitted. The PDF entry is narrowed to the relevant part
(e.g. `EGA-IV-1.pdf` for Part 1 sections).

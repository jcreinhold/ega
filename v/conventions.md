# Translation conventions — EGA V

These conventions are locked after the §V.1 calibration pass. They **inherit** the EGA IV conventions at
`docs/books/ega/iv/conventions.md` verbatim (which in turn inherit EGA II and EGA III); only the EGA-V-specific
additions for *prenote character*, V↔IV renumbering, and the differences in source pathology (digital-LaTeX OCR rather
than scan OCR; English-source rather than French-source) are recorded here.

## 1. Inherited from EGA IV

The full EGA IV conventions transfer unchanged: the terminology table, math glyphs and Unicode policy, block label
format (`<!-- label: V.N.M.K -->`), numbered display blocks in fenced ```` ```text ```` blocks, page-break comments
(`<!-- original page N -->`), source-trace footer format, translator-note guidance, modality preservation, cohomology
and spectral-sequence rendering, differential and formal-smoothness notation, regular-immersion and divisor vocabulary,
and the citation forms for `(I, …)`, `(II, …)`, `(III, …)`, `(IV, …)`, `(0_III, …)`, `(0_IV, …)`, `(M, …)`, `(G, …)`,
`(T, …)`, `(FAC, …)`, `(Bourbaki, Alg. comm., …)`, `(Nagata, …)`, `(Zariski-Samuel, …)`. Re-read those sections in
`docs/books/ega/iv/conventions.md` before extending the ledger or making a stylistic choice here.

**Block labels.** English: `**Proposition (1.1).**`, `**Definition (1.3).**`, `**Corollary (1.4).**`,
`**Theorem (5.3.2).**`, `**Lemma (5.3.4).**`, `**Remark (1.2).**`, `**Scholium (5.8).**`. Never French. Each labeled
block is followed by a blank line, the `<!-- label: V.N.M.K -->` comment, another blank line, then the italicized body.

**Proofs.** EGA V inherits EGA IV's inline-prose convention: a proof begins immediately after the labeled italic body,
in ordinary (non-italic) prose, *without* an explicit `**Proof.**` marker. Long multi-step proofs may use sub-paragraph
markers like "Step 1.", "(a)", or "(i)" inline; do not insert a `**Proof.**` header retroactively.

## 2. EGA V citation form

EGA V is the never-published fifth volume; we cite it as Chapter V. The §V.N.M.K decimal numbering is used throughout.

- `(V, 5.3.2)` cites EGA V itself.
- `(formerly IV, 20.3.2)` is attached parenthetically **only at the first occurrence in each section** where a §V
    passage was originally drafted under the EGA IV numbering. After the first occurrence in a given file, the
    parenthetical is dropped; subsequent in-section cross-references use V numbering alone.
- `(IV, 17.6.2)`, `(0_IV, 19.3.5)`, etc. cite the published EGA IV and earlier volumes as in the EGA IV conventions.
- `(Mumford, …)` cites D. Mumford, _Lectures on curves on an algebraic surface_ (Princeton, 1966). Used in §V.5 and
    §V.6.
- `(Bourbaki Sém. N)` cites Séminaire Bourbaki exposé number `N`. EGA V references Sém. 232, 236, and 261 in particular.

## 3. V↔IV renumbering map

Grothendieck's prenotes were drafted under the EGA IV numbering and renumbered into EGA V only after EGA IV's Part 1
appeared in 1964. The mapping from prenote section to EGA V section is:

| EGA V (this edition) | Originally drafted as | Topic                                                   |
| -------------------- | --------------------- | ------------------------------------------------------- |
| §V.1                 | EGA IV §16            | Singular and supersingular zeros; differential criteria |
| §§V.2.15, V.2.16     | EGA IV §§17.15, 17.16 | Jacobian and regularity supplements                     |
| §V.5                 | EGA IV §20            | Hyperplane sections and conic projections               |
| §V.6                 | EGA IV §21            | Invertible sheaves; divisors; linear systems            |

The section opening of each translated file states this correspondence inline. Inside-the-section cross-references to
"old §N" are normalized to `(formerly IV, N)` at first occurrence and to plain `(V, M)` afterwards.

## 4. Prenote character

The Blass & Blass source preserves Grothendieck's *prenote* style: marginal author-to-self comments, occasional
structural sketches, "would be better as Proposition" remarks, and untrimmed French residue (parentheticals tagged
`Fr`). We preserve this character; we do not silently smooth it into clean EGA-style exposition.

### Grothendieck marginal notes

Render Grothendieck's author-to-self comments as italicized translator-marked inserts. For short inline asides ("It
would be a good thing to summarize the above construction into a Proposition 6"):

```markdown
… defined by the vanishing of this section, whose underlying set is the right one.
*Grothendieck note: it would be a good thing to summarize the above construction into a Proposition 6.*
```

For longer asides (a sentence or more set off in the source), use an italicized blockquote:

```markdown
> *Grothendieck note.* In the language of the fathers (which we should give as a remark) a point …
```

The marker `*Grothendieck note*` distinguishes these from the surrounding mathematical prose. Never merge them silently;
that is the prenote character the reader needs.

### `[Tr.]` translator queries

Blass occasionally inserts `[Tr]` or `[Tr.]` queries (typically uncertainties about a French phrase, an ambiguous
notation, or a notational guess). Render these as numbered footnotes at the section foot, with key `[^v-N-k]` where `N`
is the §V section number and `k` is a per-section running index. The footnote body begins "Translator's note:".

```markdown
… the elongated `G` is the tangent sheaf.[^v-1-1]

[^v-1-1]: Translator's note (Blass): is the elongated `G` the tangent sheaf?
```

When the `[Tr]` query is mathematically substantive (e.g. Blass asks whether a symbol is `G` or `𝒢`), retain it in a
footnote even if we settle the question in the body. When the query is purely typographic and has a clear answer from
the PDF, resolve silently.

### `[illegible]` markers

Each `[illegible]` instance: read the source PDF; if the symbol/word is recoverable, drop the marker silently in the
body. If not, render as `[illegible]` inline and add a translator footnote describing the surrounding context. For
example:

```markdown
… homomorphism `M(φ)′` [illegible][^v-1-2] deduced from the section …

[^v-1-2]: Translator's note: the prenote source shows an indistinct mark following `M(φ)′`; possibly a prime, possibly
a tilde. The PDF does not resolve it. We follow the Vaiello edition in dropping the mark.
```

### French residue

The Blass translation leaves French interjections at points where the prenotes' bilingual working notes surface:
`en termes de papa Fr`, `sous-entendu Fr`, `pêle mêle Fr`, `confondus Fr`. These are retired into idiomatic English:

- `en termes de papa Fr` → "in the old language" (translator footnote at first occurrence quoting the original).
- `sous-entendu Fr` → "tacitly assumed", "understood".
- `pêle mêle Fr` → "pell-mell", "jumbled together", or restructure the sentence.
- `confondus Fr` → "coinciding".

When the French carries information the English alone cannot (a Bourbaki-style aside, a deliberate stylistic choice),
preserve the French in a translator footnote with the literal English gloss.

## 5. Math notation locked to EGA IV

All math notation inherits EGA IV. The Blass files render OCR fragments in non-standard forms (e.g. `Ω1X/k`, `mX /m2X`,
`d2X/Y φ`, `PX/Y2`); these are normalized:

| Blass OCR form      | Normalized rendering                | Notes                                                                                                    |
| ------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `Ω1X/k`             | `Ω^1_{X/k}`                         | Subscripts via underscores; superscripts via `^`.                                                        |
| `mX /m2X`           | `𝔪_X / 𝔪_X²`                        | Fraktur for local maximal ideals; Unicode `²`.                                                           |
| `m2X /m3X`          | `𝔪_X² / 𝔪_X³`                       |                                                                                                          |
| `Sym(mX /m2X )`     | `Sym(𝔪_X / 𝔪_X²)`                   |                                                                                                          |
| `Sym2 (Ω1X/Y )`     | `Sym²(Ω^1_{X/Y})`                   |                                                                                                          |
| `OX`, `OY`          | `𝒪_X`, `𝒪_Y`                        | Script 𝒪.                                                                                                |
| `d2X/Y φ`           | `d²_{X/Y} φ`                        |                                                                                                          |
| `PX/Y2`             | `𝒫^2_{X/Y}`                         | Script 𝒫 for principal parts (cf. EGA IV §0_IV.20).                                                      |
| `d0φ`, `d1φ`, `d2φ` | `d⁰φ`, `d¹φ`, `d²φ`                 | Unicode superscripts.                                                                                    |
| `V (φ)sing`         | `V(φ)_sing`                         |                                                                                                          |
| `V (φ)sup sing`     | `V(φ)_{sup sing}`                   | Or `V(φ)_supsing` for compactness; both acceptable.                                                      |
| `Λ1`, `Λ`           | `Λ¹`, `Λ`                           | Use Unicode superscripts; reserve `^` for arbitrary exponents.                                           |
| `det`, `Sym`        | `det`, `Sym`                        | Unaltered.                                                                                               |
| `≃ (≈)`             | `≅`                                 | Blass uses both `≃` and `≈` inconsistently; standardize to `≅` for isomorphism.                          |
| `→`, `↦`            | `→`, `↦`                            | Unaltered.                                                                                               |
| `i.e.`              | "that is", "i.e."                   | Modernize when verbose; preserve as `i.e.` in technical asides.                                          |
| `e.g.`              | "for example", "e.g."               | Modernize when verbose.                                                                                  |
| `(K)`, `(Tr)`       | Strip from prose; footnote if `Tr`. | The `(K)`-style "key" markings in the Blass margins are editorial; they are not part of the mathematics. |

For the OCR's `Λr R` and similar Greek-Roman ambiguities, consult the PDF; in our experience the PDF resolves them as
`Λ^r M` (capital lambda with rank `r` of the module `M`).

## 6. Source-trace footer

Each translated section ends with:

```html

```

The reconciliation line is included whenever the Vaiello unified file was consulted to resolve `[illegible]` markers or
ambiguities. The PDF entry is narrowed to the relevant fragment (e.g. `EGA-V-1-2.pdf` for §§V.1 and V.2.15-16,
`EGA-V-5.pdf` for §V.5, `EGA-V-6.pdf` for §V.6).

## 7. Prescheme / scheme reconciliation

Inherit the EGA II-IV convention: `préschéma` → "prescheme", `schéma` → "scheme". The Blass translation is inconsistent
("prescheme" in some passages, "scheme" in others). We normalize: when the prenote semantically uses the 1961-1967 sense
(separated/quasi-compact-versus-not distinction not yet collapsed), render "prescheme"; when the prenote uses "scheme"
in a sense that survives into post-1970s terminology, render "scheme". The default for these prenotes — which were
drafted in the 1962-1966 window — is "prescheme".

## 8. EGA-V-specific terminology

The Blass translation introduces no new French↔English terminology; the source is already English. The translation
ledger at [translation-ledger.md](translation-ledger.md) records the Blass→idiomatic-English term map (mostly
disambiguations and modernizations), and a few additional terms specific to the §V.5 hyperplane-sections theory and the
§V.6 invertible-sheaves theory.

## 9. Six-file layout

EGA V is presented as a single tree with five numbered section files plus six metadata files:

- `00-front-matter.md` — title page, publication-history note, V↔IV mapping, sommaire.
- `01-ch5-01-singular-supersingular-sets.md`, `02-ch5-02-jacobian-supplements.md`,
    `03-ch5-05-hyperplane-sections-part-1.md`, `04-ch5-05-hyperplane-sections-part-2.md`,
    `05-ch5-06-invertible-sheaves-and-divisors.md` — five numbered section files.
- One alphabetized terminology index, one source-ordered notation index, one bibliography.

Each translated file's `<!-- source: … -->` footer points back to the Blass piecemeal source.

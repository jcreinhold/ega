# EGA I: The Language of Schemes

_Éléments de Géométrie Algébrique_ by A. Grothendieck, written in collaboration with J. Dieudonné. Chapter I: _The
Language of Schemes_.

Originally published as _Publications mathématiques de l'IHÉS_, tome 4 (1960), pp. 5–228.

## About this translation

This is an idiomatic English translation in Markdown with Unicode mathematics. The French source is at ; the original
scanned text is at . A LaTeX hand-translation by the EGA community lives at ; passages have been cross-referenced
against it but the prose here has been revised for English mathematical idiom while preserving Grothendieck's
architectural voice.

The translation preserves EGA's historical terminology (notably `prescheme` for what current authors usually call a
scheme, and `scheme` for what current authors call a separated scheme). On its first occurrence in each section, a
flagged term is rendered with a bracketed modern gloss — for example, `prescheme [modern: scheme]` — and subsequent
occurrences in the same section use the historical term alone. See [glossary.md](glossary.md) for the full ledger.

EGA's decimal numbering is preserved exactly: `(N.M.K)` for items in the current chapter, `(0, N.M.K)` for
cross-references to Chapter 0, `(I, N.M.K)` for cross-references to Chapter I. Original page transitions are marked
inline as HTML comments (`<!-- original page n -->`).

## Contents

- [Front matter (title, dedication, Introduction)](00-front-matter.md)
- [Chapter 0 — Preliminaries](00-00-chapter-preliminaries.md)
    - [§1. Rings of fractions](00-01-rings-of-fractions.md)
    - [§2. Irreducible spaces. Noetherian spaces](00-02-irreducible-and-noetherian-spaces.md)
    - [§3. Complements on sheaves](00-03-complements-on-sheaves.md)
    - [§4. Ringed spaces](00-04-ringed-spaces.md)
    - [§5. Quasi-coherent sheaves and coherent sheaves](00-05-quasi-coherent-and-coherent-sheaves.md)
    - [§6. Flatness](00-06-flatness.md)
    - [§7. Adic rings](00-07-adic-rings.md)
- [Chapter I — The Language of Schemes](01-00-chapter-language-of-schemes.md)
    - [§1. Affine schemes](01-01-affine-schemes.md)
    - [§2. Preschemes and morphisms of preschemes](01-02-preschemes-and-morphisms.md)
    - [§3. Product of preschemes](01-03-product-of-preschemes.md)
    - [§4. Subpreschemes and immersion morphisms](01-04-subpreschemes-and-immersions.md)
    - [§5. Reduced preschemes; separation condition](01-05-reduced-preschemes-and-separation.md)
    - [§6. Finiteness conditions](01-06-finiteness-conditions.md)
    - [§7. Rational maps](01-07-rational-maps.md)
    - [§8. Chevalley schemes](01-08-chevalley-schemes.md)
    - [§9. Complements on quasi-coherent sheaves](01-09-complements-on-quasi-coherent-sheaves.md)
    - [§10. Formal schemes](01-10-formal-schemes.md)
- [Bibliography](bibliography.md)
- [Index of notation](index-notation.md)
- [Terminological index](index-terminology.md)
- [Glossary and translation ledger](glossary.md)

## Reference convention

Inside this volume, an item labelled `(N.M.K)` is the K-th item in subsection M of paragraph N. For a reference to
Chapter 0 from inside Chapter I (or vice versa), the chapter prefix is written: `(0, 1.2.4)` or `(I, 5.3.1)`. References
to later volumes (EGA II, III, ...) follow the same scheme: `(II, 6.2.3)`, etc. Bibliographic citations are by bracketed
number, e.g. `[14]`, with the bibliography at the end.

## Status

| File                                           | Source state       | Translation state                                    |
| ---------------------------------------------- | ------------------ | ---------------------------------------------------- |
| 00-front-matter.md                             | clean Unicode      | drafted (full prose)                                 |
| 00-00-chapter-preliminaries.md                 | clean (index only) | drafted (full)                                       |
| 00-01-rings-of-fractions.md                    | clean Unicode      | drafted (full)                                       |
| 00-02-irreducible-and-noetherian-spaces.md     | clean Unicode      | drafted (full)                                       |
| 00-03-complements-on-sheaves.md                | clean Unicode      | drafted (full)                                       |
| 00-04-ringed-spaces.md                         | clean Unicode      | drafted (full)                                       |
| 00-05-quasi-coherent-and-coherent-sheaves.md   | clean Unicode      | drafted (full)                                       |
| 00-06-flatness.md                              | clean Unicode      | drafted (full)                                       |
| 00-07-adic-rings.md                            | OCR + LaTeX + PDF  | drafted (compact, full coverage)                     |
| 01-00-chapter-language-of-schemes.md           | OCR (index)        | drafted (full)                                       |
| 01-01-affine-schemes.md                        | OCR + LaTeX + PDF  | drafted (compact, full coverage; proofs sketched)    |
| 01-02-preschemes-and-morphisms.md              | OCR + LaTeX + PDF  | drafted (compact, full coverage; proofs sketched)    |
| 01-03-product-of-preschemes.md                 | OCR + LaTeX + PDF  | skeleton (definitions + statements; proofs deferred) |
| 01-04-subpreschemes-and-immersions.md          | OCR + LaTeX + PDF  | skeleton                                             |
| 01-05-reduced-preschemes-and-separation.md     | OCR + LaTeX + PDF  | skeleton                                             |
| 01-06-finiteness-conditions.md                 | OCR + LaTeX + PDF  | skeleton                                             |
| 01-07-rational-maps.md                         | OCR + LaTeX + PDF  | skeleton                                             |
| 01-08-chevalley-schemes.md                     | OCR + LaTeX + PDF  | skeleton                                             |
| 01-09-complements-on-quasi-coherent-sheaves.md | OCR + LaTeX + PDF  | skeleton                                             |
| 01-10-formal-schemes.md                        | OCR + LaTeX + PDF  | skeleton                                             |
| bibliography.md                                | OCR                | drafted (full)                                       |
| index-notation.md                              | OCR                | drafted (full)                                       |
| index-terminology.md                           | OCR                | drafted (full)                                       |

"Drafted (full)" marks files giving the complete prose of EGA. "Drafted (compact, full coverage)" marks files that
preserve every numbered statement and definition but compress proofs to sketches. "Skeleton" marks files capturing
subsection structure, definitions, and statements of theorems and propositions, with full proofs deferred to a follow-up
pass. All files are first passes and have not yet been audited end-to-end.

Chapter 0 §1–§6 derive from clean Unicode hand-transcriptions of the source PDF. Chapter 0 §7, Chapter I, the
bibliography, and the indices are translated against the OCR-corrupted French source, cross-referenced against the
community LaTeX translation and the source PDF. Math fidelity in the skeleton sections has been preserved by
cross-referencing the LaTeX; the prose is original and idiomatic English.

## Next steps

For a follow-up session, the recommended order of work is:

1. Audit Chapter 0 §1–§6 against the source PDF for any subtle terminological drift.
1. Expand Chapter I §3 (Products of preschemes), §4 (Subpreschemes and immersions), and §5 (Reduced preschemes and
    separation) from skeleton to full coverage; these are foundational.
1. Expand Chapter I §6 (Finiteness conditions) and §9 (Complements on quasi-coherent sheaves) — used heavily in later
    EGA volumes.
1. Expand Chapter I §7, §8, and §10 — less central, can wait.
1. Add a Chapter 0 §7 prose audit; the current draft is compact and could be expanded with full proofs.

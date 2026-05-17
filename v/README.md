# EGA V — Elementary procedures for the construction of schemes (unpublished)

English markdown edition of the surviving fragments of

> A. Grothendieck, _Éléments de géométrie algébrique : V. Procédés élémentaires de construction de schémas_,
> never published. The text survives only as Grothendieck's handwritten *prenotes* — draft notes intended for later
> expansion. Piotr Blass and Joseph Blass produced an English translation; this edition is a polished, formatted
> re-presentation of that translation.

## Status

EGA V was announced in 1964 alongside EGA IV Part 1 but never reached print. The surviving prenotes cover four
fragments of the planned volume:

- §V.1 (formerly EGA IV §16) — singular and supersingular zeros of a function; differential criteria,
- §V.2.15 and §V.2.16 (formerly EGA IV §§17.15-17.16) — Jacobian and regularity supplements,
- §V.5 (formerly EGA IV §20) — hyperplane sections and conic projections,
- §V.6 (formerly EGA IV §21) — invertible sheaves, divisors, and linear systems relative to projective fibrations.

The renumbering reflects the post-1964 reorganization that moved material from EGA IV to a planned EGA V. The prenotes
were drafted under the original EGA IV numbering and reference it throughout; we lead with the V numbering and attach
`(formerly IV, M)` parenthetically at the first occurrence in each section.

## Source

The Blass & Blass translations sit at , distributed as

- `01-section-1-and-2-supplements.md` — §V.1 + §§V.2.15-2.16 (237 lines),
- `02-section-5-hyperplane-sections.md` — §V.5 (2,563 lines),
- `03-section-6-invertible-sheaves-divisors.md` — §V.6 (975 lines),
- `04-vaiello-unified-translation.md` — Vaiello unified edition (4,625 lines; consulted only for reconciliation).

Source PDFs live at , , , and
. Unlike EGA I-IV, these PDFs are digital-LaTeX output rather than scans of
typeset journal pages, so the math symbols are largely intact in the OCR; Unicode subscripts/superscripts and arrows
shifted in places.

The Vaiello unified edition reorganizes broadly the same prenotes into a single running text. We treat the piecemeal
files (01-03) as canonical and consult the Vaiello file only when the piecemeal source is illegible, ambiguous, or
missing context.

## Contents

- [Front matter (publication-history note, prenote attribution, V↔IV mapping)](00-front-matter.md)
- [§V.1. Singular and supersingular zeros of a function; differential criteria (formerly EGA IV §16)](01-ch5-01-singular-supersingular-sets.md)
- [§V.2 supplements (§§2.15-2.16): Jacobian and regularity (formerly EGA IV §§17.15-17.16)](02-ch5-02-jacobian-supplements.md)
- [§V.5 part 1: Hyperplane sections and conic projections (§§5.1-5.8) (formerly EGA IV §20)](03-ch5-05-hyperplane-sections-part-1.md)
- [§V.5 part 2: Hyperplane sections and conic projections (§§5.9-5.16)](04-ch5-05-hyperplane-sections-part-2.md)
- [§V.6. Invertible sheaves and divisors; linear systems (formerly EGA IV §21)](05-ch5-06-invertible-sheaves-and-divisors.md)

### Back matter

- [Bibliography](bibliography.md)
- [Index of notations](index-of-notations.md)
- [Index of terminology](index-of-terminology.md)

## House style

See [conventions.md](conventions.md) for the locked translation conventions (block labels, Unicode, page-break and
label HTML comments, source-trace footers, Grothendieck marginal-note rendering, V↔IV cross-reference style). The EGA V
conventions inherit `docs/books/ega/iv/conventions.md` verbatim and add the prenote-specific extensions. See
[translation-ledger.md](translation-ledger.md) for the running Blass→idiomatic-English term map (extending the EGA IV
ledger; minor in scope since most vocabulary inherits).

## Citation form

Within EGA V, decimal labels `(V, N.M.K)` cite the local volume. Cross-volume references appear as in EGA:

- `(V, 5.3.2)` cites EGA V itself.
- `(formerly IV, 20.3.2)` is attached parenthetically at the first occurrence in each section where a §V passage was
    originally drafted under EGA IV numbering. After that first occurrence, the parenthetical is dropped.
- `(IV, 17.6.2)` cites the published EGA IV.
- `(III, 2.3.8)`, `(II, 5.5.4)`, `(I, 4.2.3)` cite earlier volumes.
- `(0_IV, 19.3.5)`, `(0_III, 13.4.2)` cite the running Chapter 0 in EGA IV and EGA III respectively.
- `(M, …)`, `(G, …)`, `(T, …)`, `(FAC, …)`, `(Bourbaki, Alg. comm., …)` — external classics, inherited from EGA IV.
- `(Mumford, …)` — D. Mumford, _Lectures on curves on an algebraic surface_ (Princeton, 1966), cited in §V.5 and §V.6.

## Prenote character

The Blass translations preserve Grothendieck's *prenote* style: marginal author-to-self comments, structural sketches,
and occasional "this would be better as a Proposition" remarks. We render these as italicized translator-marked
inserts — either inline `*Grothendieck note: …*` or, for longer asides, as

> *Grothendieck note.* … (italicized blockquote)

and never silently merge them into the surrounding prose. Substantive `[Tr.]` queries from Blass are rendered as
numbered footnotes at the section foot. `[illegible]` markers are resolved against the source PDF where possible; where
the PDF is genuinely unreadable we keep the marker and add a translator footnote naming what surrounds it.

## A note on EGA V's other planned sections

The 1964 sommaire of EGA IV Part 1 announced EGA V as covering elementary procedures for the construction of schemes,
descent techniques, the method of the generic fibre, and algebraic and formal schemes. Of those planned chapters only
the four fragments above survive as prenotes. The relevant published substitutes are:

- Bourbaki Séminaire 232 (Grothendieck, _Techniques de construction en géométrie analytique_), Sém. 236 (_Techniques
    de descente_), and Sém. 261 (_Techniques de construction de schémas_) develop the descent and generic-fibre
    material that EGA V would have covered.
- Mumford, _Lectures on curves on an algebraic surface_, covers the projective and Picard-scheme material related to
    §V.5 and §V.6.
- Raynaud-Gruson, _Critères de platitude et de projectivité_ (Inv. math. 13, 1971), continues the flatness/descent
    program started in EGA IV §11.

None of these are translated here.

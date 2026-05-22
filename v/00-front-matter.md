# Éléments de géométrie algébrique

## V. Elementary procedures for the construction of schemes (unpublished — prenotes)

A. Grothendieck — prenotes for an unpublished fifth volume of EGA. Translated and edited by Piotr Blass and Joseph
Blass; polished and formatted here in continuity with the EGA I-IV translations at $docs/books/ega/{i,ii,iii,iv}/$.

The intended fifth volume was announced in 1964 alongside EGA IV Part 1 under the title *Procédés élémentaires de
construction de schémas* (elementary procedures for the construction of schemes), with descent techniques, the method of
the generic fibre, and algebraic and formal schemes. It was never published. What survives are Grothendieck's
handwritten *prenotes* — draft notes intended for later expansion — covering four fragments of the planned volume.

## Source attribution

The Blass & Blass English translations sit at

- `01-section-1-and-2-supplements.md` (237 lines) — §V.1 + §§V.2.15-2.16 prenotes.
- `02-section-5-hyperplane-sections.md` (2,563 lines) — §V.5 prenotes.
- `03-section-6-invertible-sheaves-divisors.md` (975 lines) — §V.6 prenotes.
- `04-vaiello-unified-translation.md` (4,625 lines) — Vaiello unified edition; reconciliation reference only.

Source PDFs (digital-LaTeX, not scans):

- — §V.1 and §§V.2.15-2.16.
- — §V.5.
- — §V.6.
- — Vaiello unified edition.

Unlike EGA I-IV, the PDFs are digital LaTeX output rather than scans of typeset journal pages, so OCR pathology is
limited to shifted Unicode subscripts/superscripts and the occasional ambiguous glyph. Math symbols are largely intact;
prose is in English.

## V↔IV mapping

Grothendieck's prenotes were drafted under the EGA IV numbering and renumbered to EGA V only after EGA IV's Part 1
appeared in 1964. The §V↔§IV correspondence is:

| EGA V (this edition) | Originally drafted as | Topic                                                   |
| -------------------- | --------------------- | ------------------------------------------------------- |
| §V.1                 | EGA IV §16            | Singular and supersingular zeros; differential criteria |
| §§V.2.15, V.2.16     | EGA IV §§17.15, 17.16 | Jacobian and regularity supplements                     |
| §V.5                 | EGA IV §20            | Hyperplane sections and conic projections               |
| §V.6                 | EGA IV §21            | Invertible sheaves; divisors; linear systems            |

We lead with the V numbering and attach `(formerly IV, M)` parenthetically at the first occurrence in each translated
file; after that first occurrence, the parenthetical is dropped.

## Sommaire (the four published prenote fragments)

- **§V.1.** Singular and supersingular zeros of a function; differential criteria.
- **§§V.2.15, V.2.16.** Jacobian and regularity supplements.
- **§V.5.** Hyperplane sections and conic projections (Bertini-Zariski theorem, connectedness, generic sections,
  grassmannians, linear-system formulation).
- **§V.6.** Invertible sheaves and divisors relative to projective fibrations; linear systems.

The 1964 sommaire announced further sections — descent techniques, method of the generic fibre, algebraic and formal
schemes — but no prenotes for those sections survive. The relevant published substitutes are Grothendieck's Séminaire
Bourbaki exposés 232 (analytic construction techniques), 236 (descent techniques), and 261 (scheme construction),
together with Mumford's *Lectures on curves on an algebraic surface* and the post-EGA-IV flatness/descent literature
(Raynaud-Gruson 1971; SGA 4½). None of those is translated here.

## House style

These prenotes are polished into idiomatic English mathematical prose in continuity with EGA I-IV. The Blass & Blass
translation is the canonical source; we retire French residue, fix grammar, modernize archaic phrasings where the
mathematics is unchanged, normalize OCR'd math glyphs to Unicode, and preserve Grothendieck's marginal author-to-self
comments as italicized translator-marked inserts ($*Grothendieck note: \cdots*$ or $> *Grothendieck note.* \cdots$).
Translator queries from Blass become numbered footnotes at the section foot. `[illegible]` markers are resolved against
the source PDFs where possible; where the PDF is genuinely unreadable we keep the marker and add a translator footnote
naming the surrounding context.

See [conventions.md](conventions.md) for the full locked house style and [translation-ledger.md](translation-ledger.md)
for the running Blass→idiomatic-English term map.

## Citation form within this edition

- `(V, N.M.K)` cites EGA V itself (this edition).
- `(formerly IV, M)` parenthetical at first occurrence in each file, then dropped.
- $(IV, \cdots)$, $(III, \cdots)$, $(II, \cdots)$, $(I, \cdots)$, $(0_{IV}, \cdots)$, $(0_{III}, \cdots)$ cite the
  published earlier volumes.
- $(M, \cdots)$, $(G, \cdots)$, $(T, \cdots)$, $(FAC, \cdots)$, `(Bourbaki, Alg. comm., …)`, $(Nagata, \cdots)$,
  $(Zariski-Samuel, \cdots)$ are inherited classical citations (see EGA IV conventions).
- $(Mumford, \cdots)$ cites D. Mumford, _Lectures on curves on an algebraic surface_ (Princeton, 1966).
- $(Bourbaki S\acute{e}m. 232/236/261)$ cites Grothendieck's Séminaire Bourbaki exposés.

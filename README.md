# EGA — English translation

An idiomatic, LLM-generated English translation (Markdown, Unicode mathematics) of Grothendieck and Dieudonné's
*Éléments de Géométrie Algébrique* (*Publications mathématiques de l'IHÉS*, 1960–1967).

## Volumes

- [`i/`](i) — Chapter I: The Language of Schemes
- [`ii/`](ii) — Chapter II: Elementary Global Study of Some Classes of Morphisms
- [`iii/`](iii) — Chapter III: Cohomological Study of Coherent Sheaves
- [`iv/`](iv) — Chapter IV: Local Study of Schemes and of Schemes Morphisms
- [`v/`](v) — Chapter V (unpublished; reconstructed material)

Each volume directory has its own `README.md` with status, contents, and translation notes.

## Translation principles

- Preserve EGA's historical terminology (notably `prescheme` / `scheme`); inline the modern gloss on first occurrence
  per section, and keep a per-volume `glossary.md` ledger.
- Preserve EGA's decimal numbering exactly: `(N.M.K)` within a chapter, `(0, N.M.K)` for Chapter 0 references,
  `(I, N.M.K)` for cross-chapter references.
- Mark original page transitions inline as HTML comments (`<!-- original page n -->`).
- Revise prose for English mathematical idiom while preserving Grothendieck's architectural voice.

## Source

The French source text was drawn from the Grothendieck Circle's archive of Grothendieck's published writings:
<https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/pubtexts.php>.

## Related projects

- [ryankeleti/ega](https://github.com/ryankeleti/ega) — a community LaTeX English translation of EGA. EGA I and II are
  complete; EGA III and IV are partial. Cross-referenced here for technical accuracy.
- [The Stacks Project](https://stacks.math.columbia.edu/) — an open-source modernized reference covering much of the
  same material in contemporary scheme-theoretic language, with permanently linkable tags.

## License and citation

The translation is © 2026 Jacob Reinhold and licensed under
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/); see
[LICENSE](LICENSE). The underlying French text remains © the original authors and publishers.

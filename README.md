# EGA — English translation

An idiomatic English translation, in Markdown with Unicode mathematics, of Grothendieck and Dieudonné's *Éléments de
Géométrie Algébrique* (originally published in *Publications mathématiques de l'IHÉS*, 1960–1967).

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

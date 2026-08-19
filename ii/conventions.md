# Translation conventions — EGA II

These conventions are locked. Changes after §1 require a deliberate update here, the translation ledger, and a sweep of
already-translated sections.

## 1. Terminology

| French                                            | English                                                                                   |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| préschéma                                         | prescheme (preserve EGA's 1961 distinction)                                               |
| schéma                                            | scheme                                                                                    |
| morphisme structural                              | structure morphism                                                                        |
| ouvert (n.)                                       | open set                                                                                  |
| ouvert affine                                     | affine open                                                                               |
| Module (capitalized)                              | module (lowercase; type — $\mathcal{O}_{X}$-module vs $A$-module — comes from the prefix) |
| Algèbre (capitalized)                             | algebra (lowercase; same as above)                                                        |
| Idéal (capitalized)                               | sheaf of ideals (when on a scheme); ideal (in a ring)                                     |
| anneau gradué                                     | graded ring                                                                               |
| module gradué                                     | graded module                                                                             |
| Algèbre graduée                                   | graded algebra                                                                            |
| quasi-cohérent                                    | quasi-coherent                                                                            |
| cohérent                                          | coherent                                                                                  |
| inversible                                        | invertible                                                                                |
| type fini                                         | of finite type                                                                            |
| présentation finie                                | of finite presentation                                                                    |
| spectre premier homogène                          | homogeneous prime spectrum                                                                |
| spectre homogène                                  | homogeneous spectrum                                                                      |
| fibré projectif                                   | projective bundle                                                                         |
| fibré vectoriel                                   | vector bundle                                                                             |
| faisceau ample, très ample                        | ample sheaf, very ample sheaf                                                             |
| morphisme affine                                  | affine morphism                                                                           |
| morphisme quasi-affine                            | quasi-affine morphism                                                                     |
| morphisme propre                                  | proper morphism                                                                           |
| morphisme projectif                               | projective morphism                                                                       |
| morphisme quasi-projectif                         | quasi-projective morphism                                                                 |
| morphisme entier                                  | integral morphism                                                                         |
| morphisme fini                                    | finite morphism                                                                           |
| morphisme quasi-fini                              | quasi-finite morphism                                                                     |
| morphisme propre                                  | proper morphism                                                                           |
| universellement fermé                             | universally closed                                                                        |
| séparé                                            | separated                                                                                 |
| anneau de valuation                               | valuation ring                                                                            |
| critère valuatif                                  | valuative criterion                                                                       |
| éclatement, préschéma éclaté                      | blow-up, blow-up prescheme                                                                |
| cône affine, cône projectif                       | affine cone, projective cone                                                              |
| cône projetant                                    | projecting cone                                                                           |
| fermeture projective                              | projective closure                                                                        |
| Idéal fractionnaire                               | fractional ideal sheaf                                                                    |
| fonctions rationnelles, faisceau $\mathcal{R}(Y)$ | rational functions, sheaf $\mathcal{R}(Y)$                                                |
| birationnel                                       | birational                                                                                |
| domination                                        | domination                                                                                |
| dominant (morphisme)                              | dominant                                                                                  |
| di-homomorphisme                                  | di-homomorphism                                                                           |
| anneau local                                      | local ring                                                                                |
| corps résiduel                                    | residue field, written $\kappa(x)$ (matching SGA I)                                       |
| (T.F.), (T.N.) conditions                         | (TF), (TN) conditions                                                                     |

## 2. Mathematical glyphs

All mathematics is written in LaTeX and rendered with KaTeX: inline math in `$...$`, displayed math in `$$...$$`. Do not
use raw Unicode mathematical symbols (script/Fraktur/Greek letters, arrows, relations, operators) in running text —
write the LaTeX command instead.

- Structure sheaves and standard sheaves: $\mathcal{O}_{X}$, $\mathcal{O}_{Y}$, $\mathcal{O}_{S}$, $\mathcal{O}_{X}(1)$,
  $\mathcal{O}(n)$, $\mathcal{M}$, $\mathcal{F}$, $\mathcal{G}$, $\mathcal{S}$, $\mathcal{A}$, $\mathcal{B}$,
  $\mathcal{I}$, $\mathcal{I}_{n}$, $\mathcal{R}$, $\mathcal{J}$, $\mathcal{N}$.

- Ideals in rings: $\mathfrak{m}$, $\mathfrak{n}$, $\mathfrak{p}$, $\mathfrak{q}$, $\mathfrak{a}$, $\mathfrak{b}$,
  $\mathfrak{d}$, $\mathfrak{J}$ for ideal-sheaf locals.

- Maps: $\to$, $\mapsto$, $\hookrightarrow$, $\twoheadrightarrow$, $\cong$, $\simeq$, $\subset$, $\subseteq$, $\supset$,
  $\supseteq$, $\in$, $\ni$.

- Operators: $\otimes$, $\oplus$, $\prod$, $\coprod$, $\cap$, $\cup$, $\bigcap$, $\bigcup$, $\perp$.

- Functors: write $\operatorname{Hom}$, $\operatorname{Spec}$, $\operatorname{Proj}$, $\Gamma$, $\operatorname{Sym}$,
  $\det$, $\operatorname{Pic}$, $\operatorname{End}$, $\operatorname{Aut}$ — use `\operatorname{...}` so they render
  upright.

- Specs: $\operatorname{Spec}(A)$, $\operatorname{Proj}(S)$, $\operatorname{Spec}(\mathcal{S})$ for the relative Spec,
  $\operatorname{Proj}(\mathcal{S})$ similarly.

- Greek letters as LaTeX commands: $\phi$, $\psi$, $\rho$, $\sigma$, $\tau$, $\theta$, $\omega$, $\Delta$, $\Gamma$,
  $\Omega$, $\Sigma$.

- Display equations: a `$$...$$` block, e.g.

    $$
    \Delta_{X/Y} : X \to X \times_{Y} X
    $$

## 3. Block labels

Use bold-label, blank line, HTML label comment, blank line, body:

```markdown
**Proposition.**

<!-- label: II.1.2.4 -->

Every `S`-prescheme that is affine over `S` is separated over `S` (in other words, it is
an `S`-scheme).
```

Available labels: **Theorem.**, **Proposition.**, **Lemma.**, **Corollary.**, **Definition.**, **Example.**,
**Remark.**, **Notation.**, **Reminder.**. The HTML label uses the form `II.N.M.K` (volume prefix `II`, then EGA's
decimal address).

Proofs follow immediately as a **Proof.** paragraph; no **Proof.** HTML label needed unless the proof is itself a
numbered display.

## 4. Numbered displays and cross-references

EGA's parenthesized identifiers `(1.1.2.1)` are kept exactly. When the original prose writes "Setting (8.1.1.4)", we
render

$$ \mathcal{S} = \oplus_{n\geq 0} \mathcal{I}_{n}. (8.1.1.4) $$

with the tag right-aligned in plain text (no special markup; the right-alignment is informational only). Inline
citations stay literal: `(I, 4.2.3)`, `(0, 4.2.4)`, `(III, 2.3.8)`, and within the chapter just `(1.2.4)` or `(5.5.10)`.

## 5. Pagination

`<!-- original page N -->` at every page boundary in the IHÉS print (pages 5–222). The break should appear at the prose
break, not mid-sentence; if a sentence straddles a page, place the comment after the period of the sentence containing
the break, and note the page change in the comment if useful.

## 6. Proof idioms (French → English)

- `Soient X, Y …` $\to$ "Let $X$, $Y$ …"
- `On a` $\to$ "We have"
- `Posons` $\to$ "Set"
- `Démontrons` $\to$ "We show"
- `Montrons` $\to$ "We show"
- `Il suffit de` $\to$ "It suffices to"
- `Cela résulte aussitôt de …` $\to$ "This follows immediately from …"
- `Cela résulte de …` $\to$ "This follows from …"
- `D'après …` $\to$ "By …"
- `En vertu de …` $\to$ "By virtue of …" or "By …" depending on register
- `Compte tenu de …` $\to$ "Taking … into account"
- `Réciproquement` $\to$ "Conversely"
- `On notera que` $\to$ "Note that"
- `On dit que` $\to$ "We say that" (in definitions); "One says that" only when the source is being deliberately
  impersonal in a way that matters
- `Il est immédiat que` $\to$ "It is immediate that"
- `Tout revient à …` $\to$ "It comes down to …"
- `D'autre part` $\to$ "On the other hand"
- `En particulier` $\to$ "In particular"

Keep long Grothendieck sentences long when the chain of dependencies is doing mathematical work. Split only when an
English reader genuinely loses the antecedent.

## 7. Source-trace footer

Each translated section ends with:

```html

```

## 8. Translator notes

A short `> _Translator's note._ …` quoted block, used only when:

- A 1961 term differs from current usage and a reader could misread the math.
- The OCR was unsalvageable and a small reconstruction was needed.
- The existing LaTeX cross-reference disagrees with the French and a choice had to be made.

Do not silently modernize. Do not interpolate exposition.

## 9. Modality

Preserve modal weight:

- `il semble` $\to$ "it seems"
- `on s'attend à ce que` $\to$ "one expects that"
- `conjecturalement` $\to$ "conjecturally"
- `vraisemblablement` $\to$ "presumably"
- `manifestement` $\to$ "manifestly"
- `évidemment` $\to$ "obviously"
- `clairement` $\to$ "clearly"

Do not collapse these into a single English register.

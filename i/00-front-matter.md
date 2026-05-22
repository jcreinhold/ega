# Éléments de géométrie algébrique

## I. The Language of Schemes

**by A. GROTHENDIECK** _written in collaboration with J. DIEUDONNÉ_

Institut des Hautes Études Scientifiques 1960

_Publications mathématiques de l'I.H.É.S._, tome 4 (1960), pp. 5–228.

______________________________________________________________________

## Introduction

<!-- label: I.introduction -->

_To Oscar Zariski and André Weil._

<!-- original page 5 -->

This memoir, and the many others intended to follow it, are meant to form a treatise on the foundations of algebraic
geometry. They do not, in principle, presuppose any particular knowledge of the subject; indeed, it has turned out that
such knowledge — despite its obvious advantages — can sometimes (through the overly exclusive habit of the birational
viewpoint it implies) hinder a reader who wants to become familiar with the viewpoint and the techniques presented here.
On the other hand, we assume that the reader has a good knowledge of the following subjects:

_a)_ _Commutative algebra_, as set out for instance in the forthcoming volumes of the _Éléments_ of N. Bourbaki (and,
until those volumes appear, in Samuel–Zariski [13] and Samuel [11], [12]).

_b)_ _Homological algebra_, for which we refer to Cartan–Eilenberg [2] (cited as (M)) and Godement [4] (cited as (G)),
as well as A. Grothendieck's recent article [6] (cited as (T)).

_c)_ _Sheaf theory_, where our principal references will be (G) and (T); this theory supplies the indispensable language
for interpreting the essential notions of commutative algebra in "geometric" terms and for "globalizing" them.

_d)_ Finally, the reader will find it useful to have some familiarity with the _functorial language_, which will be
constantly employed throughout this treatise, and for which he or she may consult (M), (G), and especially (T); the
principles of this language and the main results of the general theory of functors will be expounded in more detail in a
work now in preparation by the authors of this treatise.

______________________________________________________________________

It is not the place, in this Introduction, to offer a more or less summary description of the "scheme" viewpoint in
algebraic geometry, nor the long list of reasons that have made its adoption necessary — in particular, the systematic
acceptance of nilpotent elements in the local rings of the "varieties" we shall consider (a step that necessarily pushes
the notion of rational map into the background, in favor of the notion of regular map, or "morphism"). The present
treatise aims precisely to develop the language of "schemes" systematically and, we hope, to demonstrate its necessity.
While it would be easy to do so,

<!-- original page 6 -->

we shall not attempt here to give an "intuitive" introduction to the notions developed in Chapter I. The reader who
wants a preliminary glimpse of the material of this treatise may consult the lecture given by A. Grothendieck at the
International Congress of Mathematicians in Edinburgh in 1958 [7], and the exposé [8] by the same author. The work [14]
(cited as (FAC)) of J.-P. Serre may also be regarded as an intermediate exposition between the classical viewpoint and
the scheme-theoretic viewpoint in algebraic geometry; for that reason, reading it can be excellent preparation for
reading our _Éléments_.

______________________________________________________________________

For the reader's information, we give below the general plan envisaged for this treatise, subject to later modification,
particularly as regards the last chapters:

- **Chapter I.** — The language of schemes.
- **— II.** — Elementary global study of certain classes of morphisms.
- **— III.** — Cohomology of coherent algebraic sheaves. Applications.
- **— IV.** — Local study of morphisms.
- **— V.** — Elementary procedures for constructing schemes.
- **— VI.** — Descent techniques. General method of constructing schemes.
- **— VII.** — Group schemes; principal fiber bundles.
- **— VIII.** — Differential study of fiber bundles.
- **— IX.** — The fundamental group.
- **— X.** — Residues and duality.
- **— XI.** — Intersection theories, Chern classes, the Riemann–Roch theorem.
- **— XII.** — Abelian schemes and Picard schemes.
- **— XIII.** — Weil cohomology.

In principle, every chapter is regarded as open, and additional paragraphs may always be added later; such paragraphs
will appear as separate fascicles, to reduce the inconveniences of the mode of publication adopted. When such a
paragraph is foreseen or in preparation at the time a chapter is published, it will be mentioned in that chapter's table
of contents, even if, owing to priorities, its actual publication is to be appreciably later. For the reader's
convenience, we have collected in a "Chapter 0" various complements from commutative algebra, homological algebra, and
sheaf theory used in the course of this treatise — results that are more or less well known, but for which we have not
been able to give convenient references. We recommend that the reader refer to Chapter 0 only in the course of reading
the treatise proper, and only insofar as the results we cite are not sufficiently familiar to him. In this way, we
think, reading this treatise may serve a beginner as a good route to becoming familiar with commutative algebra and
homological algebra, whose study, when not accompanied by tangible applications, is judged tedious, even depressing, by
a fair number of people.

______________________________________________________________________

It is beyond our competence to give in this Introduction even a summary historical sketch of the notions and results
expounded. The text will contain only those references judged particularly useful for understanding it, and we shall
indicate the origin of only the most important results. Formally at least, the subjects treated in this new work are
rather new, which explains the sparseness of references to the Fathers of algebraic geometry of the nineteenth and early
twentieth centuries, whose work we know only by hearsay. It is nevertheless fitting to say a few words here about the
works that have most directly influenced the authors and contributed to the development of the scheme-theoretic
viewpoint. The fundamental work (FAC) of J.-P. Serre must be cited first of all: it has served as an introduction to
algebraic geometry for more than one young convert (one of the authors of the present treatise included), put off by the
dryness of A. Weil's classical _Foundations_ [18]. There, for the first time, it is shown that the "Zariski topology" of
an "abstract" algebraic variety is perfectly suited to applying certain techniques of algebraic topology and, in
particular, gives rise to a cohomology theory. Moreover, the definition of an algebraic variety given there is the one
that lends itself most naturally to the extension of that notion which we develop here.[^intro-1] Serre had already
noticed himself that the cohomology theory of affine algebraic varieties carries over without difficulty if one replaces
affine algebras over a field by arbitrary commutative rings. Chapters I and II of this treatise, and the first two
paragraphs of Chapter III, may therefore be regarded, in essentials, as easy transpositions of the principal results of
(FAC) and of a subsequent article by the same author [15] to this broader framework. We have also drawn considerable
profit from the _Séminaire de Géométrie algébrique_ of C. Chevalley [1]; in particular, the systematic use of
"constructible sets", introduced by him, has proved very useful in scheme theory (cf. Chapter IV). From him we have also
borrowed the study of morphisms from the standpoint of dimension (Chapter IV), which carries over to the
scheme-theoretic framework with no significant change. It is worth noting, moreover, that the notion of "scheme of local
rings", introduced by Chevalley, naturally lends itself to an extension of algebraic geometry (although without the full
flexibility and generality we intend to give it here); on the relation between this notion and our theory, see Chapter
I, §8. Such an extension has been developed by M. Nagata in a series of memoirs [9] containing many special results on
algebraic geometry over Dedekind rings.[^intro-2]

______________________________________________________________________

Finally, it goes without saying that a book on algebraic geometry, and especially one on its foundations, is necessarily
influenced — if only by way of intermediaries — by mathematicians such as O. Zariski and A. Weil. In particular,
Zariski's _Theory of holomorphic functions_ [20], suitably made more flexible by cohomological methods and completed by
an existence theorem (Chapter III, §§4 and 5), is — together with the descent technique exposed in Chapter VI — one of
the principal tools used in this treatise, and seems to us one of the most powerful at our disposal in algebraic
geometry.

The general technique in which it fits may be sketched as follows (a typical example will be given in Chapter IX, in the
study of the fundamental group). One has a proper morphism (Chapter II) $f : X \to Y$ from one algebraic variety to
another (more generally, from one scheme to another) that one wishes to study in a neighborhood of a point $y \in Y$,
with a view to solving a problem $P$ relating to a neighborhood of $y$. One proceeds in successive steps:

1° One may assume that $Y$ is affine, so that $X$ becomes a scheme defined over the affine ring $A$ of $Y$, and one may
even replace $A$ by the local ring of $y$. This reduction is always easy in practice (Chapter V) and reduces us to the
case where $A$ is a _local_ ring.

2° One studies the problem under consideration when $A$ is a local _Artinian_ ring. For the problem to retain a meaning
when $A$ is not assumed to be an integral domain, it is sometimes necessary to reformulate $P$; this reformulation often
yields a better understanding of the problem, which is "infinitesimal" in nature at this stage.

3° The theory of formal schemes (Chapter III, §§3, 4, and 5) allows one to pass from the case of an Artinian ring to
that of a _complete local ring_.

4° Finally, if $A$ is an arbitrary local ring, consideration of "multiform sections" over suitable schemes over $X$,
approximating a given "formal" section (Chapter IV), will often allow one to pass from a result known for the scheme
obtained from $X$ by extension of scalars to the completion of $A$, to an analogous result for a suitably simple finite
extension (for example, an unramified one) of $A$.

This sketch shows the importance of the systematic study of schemes defined over an Artinian ring $A$. Serre's viewpoint
in his formulation of local class field theory, and the recent work of Greenberg, suggest that such a study might be
undertaken by attaching functorially to such a scheme $X$ a scheme $X'$ over the residue field $k$ of $A$ (assumed
perfect) of dimension equal (in favorable cases) to $n \cdot \dim X$, where $n$ is the length of $A$.

As for the influence of A. Weil, let it suffice to say that one of the principal motivations behind the writing of this
treatise has been the need to develop the apparatus necessary to formulate, with all the desired generality, the
definition of "Weil cohomology", and to undertake the proof[^intro-3] of all the formal properties needed to establish
his famous conjectures in Diophantine geometry [19]; this motivation stands alongside the desire to find the natural
framework for the customary notions and methods of algebraic geometry, and to give the authors the occasion to
understand those notions and techniques.

______________________________________________________________________

To conclude, we believe it useful to warn the reader that, just like the authors themselves, he will doubtless have some
difficulty before becoming accustomed to the language of schemes and convincing himself that the usual constructions
suggested by geometric intuition can be transcribed, essentially in only one reasonable way, into this language. As in
many parts of modern mathematics, the initial intuition appears to drift further and further from the language
appropriate to express it with the precision and generality required. Here, the psychological difficulty lies in the
need to carry over, to the objects of a category already rather different from the category of sets (namely, the
category of preschemes, or the category of preschemes over a given prescheme), notions familiar for sets: Cartesian
products, group laws, ring laws, module laws, fiber bundles, principal homogeneous fiber bundles, and so on. It will
doubtless be hard for the mathematician of the future to escape this new effort of abstraction — perhaps, all told, a
fairly small one compared with that made by our fathers as they were becoming familiar with set theory.

______________________________________________________________________

References will be given following the decimal system; for instance, in `III, 4.9.3`, the numeral `III` indicates the
chapter, the `4` the paragraph, and the `9.3` the item within the paragraph. _Within the same chapter_, the chapter
prefix is omitted.

[^intro-1]: As J.-P. Serre has pointed out to us, the idea of defining the structure of a variety by giving a sheaf of
    rings is due to H. Cartan, who took it as the starting point of his theory of analytic spaces. Of course, just as in
    algebraic geometry, it would be important, in "analytic geometry", to admit nilpotent elements in the local rings of
    analytic spaces. This extension of the definition of H. Cartan and J.-P. Serre has recently been taken up by H.
    Grauert [5], and there is reason to hope that a systematic exposition of analytic geometry in this general setting
    will soon appear. It is also clear that the notions and techniques developed in this treatise retain their meaning
    in analytic geometry, although one must expect more considerable technical difficulties in that theory. One can
    foresee that algebraic geometry, by the simplicity of its methods, may serve as a kind of formal model for future
    developments in the theory of analytic spaces.

[^intro-2]: Among works close in spirit to our viewpoint in algebraic geometry, let us mention the important work of E.
    Kähler [22] and a recent Note of Chow and Igusa [3], which take up, within the Nagata–Chevalley framework, certain
    results of (FAC) and also give a Künneth formula.

[^intro-3]: To avoid any misunderstanding, we point out that this task has barely been undertaken at the time this
    Introduction is being written, and so has not yet led to a proof of the Weil conjectures.

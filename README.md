# intro-to-linguistics

Demos illustrating concepts for my Introduction to Linguistics course.

##mu.py and mu.puzzle.py##
An algorithm for generating theorems of the MIU-system described by Douglas Hofstadter in *Gödel, Escher, Bach*.  Originally, mu.py was developed for UGS303, Minds & Machines at UT Austin.  Neither @chbrown nor I can remember which of us created it.  But mu.puzzle.py I wrote later for Intro to Linguistics, using simple string matching instead of regular expressions, for purposes of comparison.  The latter allows the user to set an upper limit on the number of theorems generated.  The original mu.py is non-terminating.  These are useful for discussion of formal languages, string rewriting systems, algorithms, and decideability.  

##temporal-reference-engine.py##
A random temporal expression generator.  

##toy-morphophonology.py##
A toy grammar illustrating the concepts of lexical items as sound-meaning pairs and morphemes as functions.  Particular lexical items evoke discussion of context-dependent phonological changes in morphemes ('house', 'start') or of suppletion ('meet').

Phonological forms are given in broad IPA transcription.  Logical forms are just represented with glosses (e.g. '-PST' for the logical form contributed by past tense morphology) -- at the point in the semester when I introduce this demo, students have no background in formal semantics.

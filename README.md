# intro-to-linguistics

Demos illustrating concepts for my Introduction to Linguistics course.

## mu.py and mu.puzzle.py ##

Scripts for generating theorems of the MIU-system described by Douglas Hofstadter in *Gödel, Escher, Bach*.  Originally, mu.py was developed for UGS303, Minds & Machines at UT Austin.  Neither @chbrown nor I can remember which of us created it.  But mu.puzzle.py I wrote later for Intro to Linguistics, using simple string matching in the first two rewrite rules, instead of regular expressions, for purposes of comparison.  Also, mu.puzzle.py allows the user to set an upper bound on the number of theorems generated, while the original mu.py is non-terminating.  These are useful for discussion of formal languages, string rewriting systems, algorithms, and decideability.

### Usage of mu.py ###

`python mu.py`

Theorems will be generated until there is no additional memory or until the script is killed (`ctrl+c`).

### Usage of mu.puzzle.py###

Open Python interpreter from terminal and read in script and execute the puzzle solver function with various upper bounds.
```
execfile('<path/to/mu.puzzle.py>')
MU_Puzzle_Solver(10)
MU_Puzzle_Solver(100)
MU_Puzzle_Solver(1000) # etc.
```

## temporal-reference-engine.py ##
A random temporal expression generator.  

### Usage ###

From the interpreter:
```
execfile('<path/to/temporal-reference-engine.py')

Time() # etc.
```

## toy-morphophonology.py ##

A toy grammar illustrating the concepts of lexical items as sound-meaning pairs and morphemes as functions.  Particular lexical items evoke discussion of context-dependent phonological changes in morphemes ('house', 'start') or of suppletion ('meet').  Also good for discussion of selectional/type restrictions imposed by functions.

Phonological forms are given in broad IPA transcription.  Logical forms are just represented with glosses (e.g. '-PST' for the logical form contributed by past tense morphology) -- at the point in the semester when I introduce this demo, students have no background in formal semantics.

### Usage ###

Read file into interpreter, and try out the functions on various vocabulary items.
```
PL(boy)
PST(boy)
PST(believe)
PST(meet)
CMPR(house)
CMPR(short)
```

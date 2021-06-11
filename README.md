This is an n-gram which requires training text to be manually entered. Future work could involve using machine learning to train and gain probabilities from a 
very large amount of text.

Simply run the .py file. The first prompt requires a sentence that will be used to "train" the model. For example, a sentence such as: 
Toilet paper has two possible orientations when the roll is parallel to both the wall and the floor: The toilet paper may hang over (in front of) or under (behind) the roll.

The sentence should be one long line and can't have any line breaks inside it, as this will skip other inputs the program needs.

The second prompt is the phrase or sentence(s) that the probability should be determined for. Case does not matter. If multiple sentences are added, it is important that
a period is present where appropriate in-between the sentences.

The third prompt requires either True (or true), if a sentence was entered, or False (or false), if a phrase was entered. 

The fourth prompt requires an integer n-value. This will determine how large the grams generated will be.

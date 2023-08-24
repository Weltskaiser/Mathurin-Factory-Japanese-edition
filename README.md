# Mathurin Factory - Japanese edition: a Japanese vocabulary learning game

## What is this?
`Mathurin Factory - Japanese edition` transforms your journey of learning a new language's vocabulary into a ludic and progression-showing game. Train yourself on specific words categories and get evaluated on it. Relax on a dark screen, no ads or distraction. Can you get a perfect score on each category?

## How to use it?
### Gather data
Pick a complete vocabulary list you want to master up and match it to the following format: a CSV file `vocabulary.csv`, containing four columns:
- Katakana
- Kanji
- English translation
- Romaji transcription
<!--(Hello)-->
Ensure there is a header row (the program will skip it). There can be blank rows.<br>
Now put level delimiters. Delimiters will be useful for the program to understand which rows belong to which category. Categories a recursives, e.g. the word `にんげん,人間,human,ningen` belongs to the category `People`, that itself belongs to the category `Nouns`. A category can contain an undefined number of sub-categories. To delimit categories, you only have to introduce them by inserting a row that only contains one column, which is the level delimiter followed by two random characters (they will be skipped) and then the category name. So you first have to decide how many category levels you want and what will be you delimiters.
Here is an example of a valid CSV file, where we chose to have two category levels, delimited by the characters `=` and `-`:
```csv
Kana,Kanji,English,Romaji
== Nouns
-- People
にんげん,人間,human,ningen
じんるい,人類,humanity,jinrui
-- Body
あし,足、脚,foot/leg,ashi
かかと,踵,heel,kakato
すね,脛,shin,sune
== Adjectives
-- Feelings
うれしい,嬉しい,happy,ureshii
== Verbs
-- To do
する,,to do,suru
-- Existence
いる,,to exist [for animate objects],iru
-- Movement
いく,行く,to go,iku
くる,来る,to come,kuru
```
Now, pick a TTF font file (make sure it supports every one of your language's characters) up.
Finally, get your JSON score file if you have one already (e.g. you try improving your score on another device for example).
Place these three (or two) files in this directory.

### Setup the program
Modify `jp.sh`: replace the arguments by the values you chose:
- Indicate the paths to your CSV, TTF and JSON file. The last one will be generated if the file does not exist
- The second argument (after the path to your CSV) is the string containing the delimiters: if you chose `=` and `-` like in our example above, you have to write `=-`. Beware of the order: the first one is the top-level category.

### Run it
Execute `jp.sh` from a shell and the game starts!

## How to play?
### Select your category
The program prompts you to select a top-level category, then a next category into the one you chose, and so on. Press only Enter if you want to train on the whole category you've already selected.

### Train yourself
Then the game window displays. Everything is controlled by the keyboards, here are the keybinds:
- `Enter`: show the next word
- `Backspace`: show/hide the kana
- `Left Shift`: show/hide the kanji (why?)
- `Right Shift`: show/hide the english translation
- `Right Arrow`: show/hide the romaji transcription
- `Down Arrow`: show/hide both the english translation and the romaji transcription
- `Left Arrow`: show/hide all three the kana, the english translation and the romaji transcription
- `Keypad 4`: start the evaluation mode
- `Keypad 5`: state you got it wrong
- `Keypad 6`: state you got it correct
- `Left Control`: exit the program (even in evaluation mode)
<!--(Hello)-->
Scroll through your category and try to memorize the vocabulary! At first with every information, then try to remove the english translation and guess the translation using the kanji and/or kana. When you think you're good, try to hide the romaji, then the kana.

### The evaluation system
`Mathurin Factory - Japanese edition` proposes you to evaluate yourself. All you need is to start the evaluation mode. From now on, for every word you get, you will have to indicate if you guessed the word correctly or not, then you will be able to scroll to the next word. When you're done with all of the words, your score is displayed and it will replace the previous best score in the JSON score file if you made it better! That's all, you can close the program and launch it anew the try the other categories.

## The science behind it
[Warning: very based content here]
The true value of `Mathurin Factory - Japanese edition` is the main key that will enable you to master your new language in a ridiculously tiny amount of time! We said "understand" and not "master", here we explain the choice.<br>
The best way to learn a language is to mimic babies: they listen to the language (from their parents or the school), then understand it, and then alongside their learning they learn how to speak. We can follow their progress by listening to them, and we notice that they start with words amongst the most basic vocabulary, usually nouns and verbs. Then they learn how to articulate the vocabulary to form basic sentences, and we see that they learn grammar/conjugations/etc. by experience.<br>
That is exactly what we want to do: **learn vocabulary**, then **intuitively understand how to use** it in a sentence by listening to natives. **The grammar/conjugations/etc. should intuitively come to your mind, you don't need to learn it**. Most of kids don't know about every one of their language's specifications, they just know how to speak it. That's why they often have troubles writing certain sentences using the correct spelling/grammar/conjugation/etc. This is the proof that you don't need to learn them to be able to understand or speak the language. Even adults are far from mastering the whole of their language - and that's absolutely okay.<br>
So go on, **learn your 1000 most common words, listen to natives or read sentences**, and you will see you will incorporate the essence of the language and start to understand the way it functions. At first, you will only recognize basic words but you will understand neither their order in the sentence nor the words articulating them, but after a while it will become logical.<br>
You will note that this method essentially lets you understand the language, but it will neither allow you to write the language properly, nor be able to hold a conversation with a native. That's absolutely true. When your brain is only trained to understand A from B, it will not put much effort to let you easily find B from A. Especially about kanjis: you may recogniwe them, but good luck to write it correctly and not write "alligator" where you wanted to write "pendulum" (I didn't check the spelling, chances are they are completely different, of course that was an example).<br>
But let's be honest: in most cases, you won't have the opportunity or use to express yourself in a new language. You may wonder to travel or speak/write to natives, but you may just want to read/watch content in Japanese on Internet, which is by far the most accessible usage you can do. And even if you want to communicate with people in Japanese: **nobody will blame you for your grammar**. You could have the worst grammar ever, even only tell a sequences of words, like "I - food - please": **your interlocutor will still understand you**. Only French people will try to deeply correct you, haha. More seriously, if the person you're speaking to is quite intelligent, they will encourage you and maybe give you the right sentence, but not try to impregnate you with the subleties of the language using grammar explanations, because you won't be able to remember, as if you wanted to teach the conditional past tense to a 5 year old child. Let the learner the time that is needed to master enough of the language to understand these fine elements.<br>
You've come so far? You could have learned a bunch of vocabulary meanwhile, go practice and have fun!

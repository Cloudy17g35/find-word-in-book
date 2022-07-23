Simple REST API.

Performs GET operation books/?book_name={book_name}&word={word}

API makes call to site gutenberg.org and takes
book text (possible books are in location: find_word_in_book/config.json)


For now possible books are:

* Moby Dick (Herman Melville)
* Idiot (Fyodor Dostoevsky)
* Sun Also Rises (Ernest Hemingway)


API looks for a requested word in whole book text (word length must be at least 2 and word cannot be a stopword, list of stopwords can be find here: https://gist.github.com/sebleier/554280)

returns number of word occurences in the book and the lines where word occured

Exaple calls and results:

book: moby dick
word: mouse
books/?book_name=moby%20dick&word=mouse

result:
```
{"occurences":3,"lines":["locked; and not a mouse to be heard; and it’s been just so silent ever","the wondrous whale was but a species of magnified mouse, or at least","now shook the slight cedar as a mildly cruel cat her mouse. With"]}
```





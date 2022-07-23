# Simple REST API.

Performs GET operation books/?book_name={book_name}&word={word}

API makes call to site gutenberg.org and takes
book text (possible books are in location: find_word_in_book/config.json)


for now possible books are:

* Moby Dick (Herman Melville)
* Idiot (Fyodor Dostoevsky)
* Sun Also Rises (Ernest Hemingway)


API looks for a requested word in whole book text (word length must be at least 2 and word cannot be a stopword, list of stopwords can be find here: https://gist.github.com/sebleier/554280)

returns number of word occurences in the book and the lines where word occured

Exaple calls and results:

**book_name:** moby dick

**word:** mouse

```
books/?book_name=moby dick&word=mouse
```

result:
```
{
    "occurences": 3,
    "lines": [
        "locked; and not a mouse to be heard; and it’s been just so silent ever",
        "the wondrous whale was but a species of magnified mouse, or at least",
        "now shook the slight cedar as a mildly cruel cat her mouse. With"
    ]
}
```


**book_name:** sun also rises

**word:** evening

```
/books?book_name=sun also rises&word=evening
```

result:
```
{
    "occurences": 12,
    "lines": [
        "_apéritif_ and watch the evening crowd on the Boulevard.",
        "pairs, looking for the evening meal. I watched a good-looking girl walk",
        "“And have you had a lovely evening?”",
        "Monday evening he turned up at the flat. I heard his taxi stop and went",
        "sporting evening.”",
        "June evening.",
        "same evening about seven o’clock I stopped in at the Select to see",
        "couldn’t stick it, so I left. Later on in the evening I found the box in",
        "sleeveless evening dress. She looked quite beautiful. Mike acted as",
        "In the evening was the paseo. For an hour after dinner every one, all",
        "We watched the beginning of the evening of the last night of the fiesta.",
        "their nurses before the season opened. In the evening there would be"
    ]
}
```

**book_name:** idiot

**word:** guillotine

```
/books?book_name=idiot&word=guillotine
```

result:
```
{
    "occurences": 2,
    "lines": [
        "the purpose of avoiding pain, this guillotine I mean; but a thought",
        "criminal, one minute before the fall of the guillotine, while the"
    ]
}
```


In order to run the code using Docker:

```
docker build -t find-word-in-book .
```

```
docker run -p 80:80 find-word-in-book
```

api will work on http://0.0.0.0/books

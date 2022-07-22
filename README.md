API endpoint is word,API returns the number of  word occurences in total
in book and the lines where word occured

For instance:

Foo bar
hello world
brown fox
bar foo

for word = bar
should return:
 {
	"occurences": 2,
	"lines": ["foo bar", "bar foo"]
}

looking for a word that is considered a problem will be treated as a bad request, list of stopwords: https://gist.github.com/sebleier/554280

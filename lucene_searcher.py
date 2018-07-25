import lucene
from java.nio.file import Paths
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher, BooleanClause, BooleanQuery, TermQuery
from org.apache.lucene.index import DirectoryReader, Term

input_q = input()
lucene.initVM()
index_path = Paths.get('./lucene.index')
question_field = 'question'
answer_field = 'answer'

directory = SimpleFSDirectory(index_path)
searcher = IndexSearcher(DirectoryReader.open(directory))

qtq = TermQuery(Term(question_field, input_q))
query_builder = BooleanQuery.Builder()
query = query_builder\
    .add(BooleanClause(qtq, BooleanClause.Occur.SHOULD))\
    .build()
top_n = 5
scoreDocs = searcher.search(query, top_n).scoreDocs
print('found nums: ', len(scoreDocs))
for scoreDoc in scoreDocs:
    doc = searcher.doc(scoreDoc.doc)
    print('Best Math: ', doc.get(question_field))
    print('Answer: ', doc.get(answer_field))
    print('---------------------\n')

import lucene
from java.nio.file import Paths
from org.apache.lucene.index import IndexWriterConfig, IndexWriter, FieldInfo, IndexOptions
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.analysis.standard import StandardAnalyzer
from xlrd import open_workbook

wb = open_workbook('./QA-samples.xlsx')
sheet0 = wb.sheet_by_index(0)
sheet1 = wb.sheet_by_index(1)

print('initializing Lucene VM')
lucene.initVM()
print('lucene version ', lucene.VERSION)

index_path = Paths.get('./lucene.index')
question_field = 'question'
answer_field = 'answer'

index_store = SimpleFSDirectory(index_path)
analyzer = StandardAnalyzer()
config = IndexWriterConfig(analyzer)
config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
writer = IndexWriter(index_store, config)

TokenizeFields = True

# Question field type

qft = FieldType()
# qft.setIndexed(True)  # todo
qft.setStored(True)
qft.setTokenized(TokenizeFields)
qft.setIndexOptions(IndexOptions.DOCS_AND_FREQS)

# Answer field type
aft = FieldType()
# aft.setIndexed(False)  # todo
aft.setStored(True)
for row in range(1, sheet1.nrows):
    doc = Document()
    row_q = str(sheet1.cell(row, 0).value)
    row_a = str(sheet0.cell(row, 1).value)
    doc.add(Field(question_field, row_q, qft))
    doc.add(Field(answer_field, row_a, aft))
    writer.addDocument(doc)
writer.commit()
writer.close()

# Usage: python test_es.py accounts.json
from os import name
import sys, json, logging, pytest, logstash
from logging import StreamHandler
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk

host = '10.60.61.10'
filename = "accounts.json"
yield_ok = True  # if set to False will skip successful documents in the output
chunk_size = 10000
errors_before_interrupt = 5
refresh_index_after_insert = False
max_insert_retries = 3
index_name = 'my_index'

# you can use RFC-1738 to specify the url
es = Elasticsearch(['http://elastic:muneer@10.60.61.10:9200'])

print("Testing Elasticsearch Create/Search/Bulk Operations")

def esOperations(index_name="test-index"):
    doc = {
        'author': 'muneer',
        'text': 'Testing Elasticsearch Create and Search Operations.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="index_name", id=1, body=doc)
    res = es.get(index="index_name", id=1)
    es.indices.refresh(index="index_name")
    res = es.search(index="index_name")
    print("Got %d Hits:" % res['hits']['total']['value'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

# res = es.search(index="test-index")
# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

def data_generator(index_name):
    f = open(filename)
    for line in f:
        yield {**json.loads(line), **{
            "_index": index_name,
        }}

def bulkImport():
    errors_count = 0
    ## Performance Testing (BUlk Import of Data Set)
    for ok, result in streaming_bulk(es, data_generator(index_name), chunk_size=chunk_size, refresh=refresh_index_after_insert,
                                    max_retries=max_insert_retries, yield_ok=yield_ok):
        if ok is not True:
            logging.error('Failed to import data')
            logging.error(str(result))
            errors_count += 1

            if errors_count == errors_before_interrupt:
                logging.fatal('Too many import errors, exiting with error code')
                exit(1)

# Integration Testing
test = logging.getLogger('python-logstash-logger')
test.setLevel(logging.INFO)
test.addHandler(logstash.TCPLogstashHandler(host, 5044, version=1))
test.addHandler(StreamHandler())

def integration():
    try:
        test.error('python-logstash: test logstash error message.')
        test.info('python-logstash: test logstash info message.')
        test.warning('python-logstash: test logstash warning message.')

        # add extra field to logstash message
        extra = {
            'test_string': 'python3 version: ' + repr(sys.version_info),
            'test_boolean': True,
            'test_dict': {'a': 1, 'b': 'c'},
            'test_float': 1.23,
            'test_integer': 123,
            'test_list': [1, 2, '3'],
        }
        test.info('python-logstash: test extra fields', extra=extra)
    except:
        print("Error")

esOperations()
bulkImport()
integration()
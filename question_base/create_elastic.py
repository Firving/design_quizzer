from elasticsearch import Elasticsearch
import numpy as np
from datetime import datetime
es = Elasticsearch('http://localhost:9200')
import json
import time
import copy
import csv
import re

# try:
#     print('try to create an index')
#     es.indices.create(index='question_pool_all', ignore=400)
#     print('Create the index succesffuly.')
# except:
#     print('error')
es.indices.delete(index='question_pool_all', ignore=[400, 404])
print('Recreating the index.')
es.indices.create(index='question_pool_all', ignore=400)
print('Do not rebuild the dataset, it takes hours.')

start_time = time.time()
count = 1
# '../question_pool_0821.json'
with open('../question_pool_0825.json', 'rb') as f:
    items = json.load(f)
    items_length = len(items)
    for item in items:
        # print(item)
        # for question in item['questions']:
        #     # if 'other_options_wiki' in question.keys():
        #     store_item = copy.deepcopy(item)
        #     # print(question)
        #     store_item['questions'] = ''
        #     store_item['question_id:'] = question['question_id:']
        #     store_item['raw_critique'] = question['raw_critique']
        #     store_item['select_design_concept'] = question['select_design_concept']
        #     store_item['mention_ui_elements'] = question['mention_ui_elements']
        #     store_item['question'] = question['question']
        #     store_item['right_answer'] = question['right_answer']
        #     store_item['explanation'] = question['explanation']
        #     # store_item['other_options'] = question['other_options']
        #     # store_item['other_options_wiki'] = question['other_options_wiki']
        #
        #     # new structure 20220820
        #     store_item['answer_cluster'] = question['select_design_concept']['cluster']
        #     store_item['answer_pos_tag'] = question['select_design_concept']['pos_tag']
        #     store_item['other_option_1'] = question['other_options'][0]
        #     store_item['other_option_2'] = question['other_options'][1]
        #


        es.index(index='question_pool_all', body=item)
        count += 1
        if count % 100 == 0:
            print('Insert {}/{} palettes: take {}s'.format(count, items_length, round(time.time() - start_time, 2)))
            print(item['ui_elements'])
        # if count == 401:
        #     break

print('It takes {} seconds to write {} questions.'.format(time.time() - start_time, count))
import json
import wikipedia
import wikipediaapi
import random

with open('./pool2(feedback_request_post_comments).json', 'r') as f:
    items = json.load(f)

store_data = []
count = 0
for item in items:
    if "questions" in item.keys():
        for i in range(len(item['questions'])):
            select_design_concept = item['questions'][i]['select_design_concept']
            print(select_design_concept['name'])
            search_result = wikipedia.search(select_design_concept['name'])
            if len(search_result) == 0:
                continue
            keyword = search_result[0]
            wiki_wiki = wikipediaapi.Wikipedia('en')
            page_py = wiki_wiki.page(keyword)
            if page_py.exists():  # It takes time to do so, so we need to prepare the hint for each option in advance
                one_sentence_summary = page_py.summary.split('.')[0] + '.'
                # print(keyword)
                # print(one_sentence_summary)
                if 'may refer to' in one_sentence_summary:
                    one_sentence_summary = 'It may refer to many wiki pages. Click the link to check.'
                    # print(one_sentence_summary)
                    # if len(one_sentence_summary.split('\n')) > 1:
                    #     if one_sentence_summary.split('\n')[1] != '':
                    #         keyword = one_sentence_summary.split('\n')[1].split(',')[0]
                    #     elif len(one_sentence_summary.split('\n')) > 2:
                    #         keyword = one_sentence_summary.split('\n')[2].split(',')[0]
                    #     page_py = wiki_wiki.page(keyword)
                    #     one_sentence_summary = page_py.summary.split('.')[0] + '.'
                    #     if 'may refer to' in one_sentence_summary:
                    #         one_sentence_summary = page_py.sections[0].text.split('\n')[0]
                    # else:
                    #     # print(page_py.sections)
                    #     # print(page_py.sections[0].text)
                    #     keyword = page_py.sections[0].text.split('\n')[1].split(',')[0]
                    #     page_py = wiki_wiki.page(keyword)
                    #     one_sentence_summary = page_py.summary.split('.')[0] + '.'
                    #     if 'may refer to' in one_sentence_summary:
                    #         one_sentence_summary = page_py.sections[0].text.split('\n')[0]

                # if hasattr(page_py, 'fullurl'):
                try:
                    item['questions'][i]['select_design_concept']['wiki_title'] = keyword
                    item['questions'][i]['select_design_concept']['wiki_url'] = page_py.fullurl
                    item['questions'][i]['select_design_concept']['wiki_summary'] = one_sentence_summary
                except:
                    pass
            else:
                print('page not exist')
                print(keyword)
                continue
            item['questions'][i]['other_options_wiki'] = []
            for j in range(2):
                option = item['questions'][i]['other_options'][j]
                search_result = wikipedia.search(option)
                if len(search_result) == 0:
                    continue
                keyword = search_result[0]
                wiki_wiki = wikipediaapi.Wikipedia('en')
                page_py = wiki_wiki.page(keyword)
                # print(page_py.summary)
                # print(page_py.sections)
                if page_py.exists():  # It takes time to do so, so we need to prepare the hint for each option in advance
                    one_sentence_summary = page_py.summary.split('.')[0] + '.'
                    # print(keyword)
                    # print(one_sentence_summary)
                    if 'may refer to' in one_sentence_summary:
                        one_sentence_summary = 'It may refer to many wiki pages. Click the link to check.'
                        # print(one_sentence_summary)
                        # if len(one_sentence_summary.split('\n')) > 1:
                        #     if one_sentence_summary.split('\n')[1] != '':
                        #         keyword = one_sentence_summary.split('\n')[1].split(',')[0]
                        #     elif len(one_sentence_summary.split('\n')) > 2:
                        #         keyword = one_sentence_summary.split('\n')[2].split(',')[0]
                        #     page_py = wiki_wiki.page(keyword)
                        #     one_sentence_summary = page_py.summary.split('.')[0] + '.'
                        #     if 'may refer to' in one_sentence_summary:
                        #         one_sentence_summary = page_py.sections[0].text.split('\n')[0]
                        # else:
                        #     # print(page_py.sections)
                        #     # print(page_py.sections[0].text)
                        #     keyword = page_py.sections[0].text.split('\n')[1].split(',')[0]
                        #     page_py = wiki_wiki.page(keyword)
                        #     one_sentence_summary = page_py.summary.split('.')[0] + '.'
                        #     if 'may refer to' in one_sentence_summary:
                        #         one_sentence_summary = page_py.sections[0].text.split('\n')[0]
                    # if hasattr(page_py, 'fullurl'):
                    try:
                        item['questions'][i]['other_options_wiki'].append({
                            "name": option,
                            "wiki_title": keyword,
                            'wiki_url': page_py.fullurl,
                            'wiki_summary': one_sentence_summary
                        })
                    except:
                        pass
        store_data.append(item)
        count+=1
        print(count)

with open('./data_all_2.json', 'w') as f:
    json_string = json.dumps(store_data)
    f.write(json_string)
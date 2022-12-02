import transformers 
from transformers import AutoTokenizer
from transformers import pipeline
import os
import datetime
import json

article_dir_path = '/persistent/articles'
sum_dir_path = '/persistent/summaries'

def load_model():
    hub_model_id = "devansh71/news-sum-dev-ai5"
    summarizer = pipeline("summarization", model=hub_model_id)
    return summarizer

def predict(text,model):
    summary = model(text)
    sum_text = summary[0]['summary_text']
    return sum_text

def load_data(article_dir_path): 
    text= {}
    headings= {}
    
    for i,file in enumerate(os.listdir(article_dir_path)):
        file_path  = os.path.join(article_dir_path,file)
        f = open(file_path,'r')
        json_file = json.load(f)
        f.close()
        headings[file]=list(json_file.keys())
        text[file]=list(json_file.values())
    return text,headings
    
def load_data_sum(file_path):
    for i,file in enumerate(os.listdir(file_path)):
        file_path  = os.path.join(file_path,file)
        f = open(file_path,'r')
        json_file = json.load(f)
        f.close()
    return json_file
        
def get_prediction():
    today = datetime.date.today()
    today=str(today).replace('-','_')
    article_path = os.path.join(article_dir_path,today)
    sum_path = os.path.join(sum_dir_path,today)
    
    if os.path.exists(sum_path):
        # summaries already exists
        summary_dict=load_data_sum(sum_path)
    else:
        # also store to storage
        os.makedirs(sum_path)
        articles,heds=load_data(article_path)

        model = load_model()
        summaries = {}
        summary_dict={}
        for idx,text in articles.items():
            category = idx.split('.')[0]
            summaries[category]=[]
            for i,arts in enumerate(text):
                summaries[category].append(predict(arts,model))
            temp_dict={}
            for i in range(len(summaries[category])):
                temp_dict[heds[idx][i]]=summaries[category][i]
            summary_dict[category] = temp_dict

        file_name ='news.json'
        file_path = os.path.join(sum_path,file_name)
        with open(file_path,'w') as f:
            json.dump(summary_dict,f,indent=4)

    return summary_dict

if __name__== '__main__':
    sum = get_prediction()
    print(sum)
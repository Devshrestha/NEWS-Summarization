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
        headings[i]=list(json_file.keys())[0]
        text[i]=list(json_file.values())[0]
    return text,headings
    
        
def get_prediction():
    today = datetime.date.today()
    today=str(today).replace('-','_')
    article_path = os.path.join(article_dir_path,today)
    sum_path = os.path.join(sum_dir_path,today)
    
    if os.path.exists(sum_path):
        # summaries already exists
        summaries,heds=load_data(sum_path)
    else:
        # also store to storage
        os.makedirs(sum_path)
        articles,heds=load_data(article_path)
        model = load_model()
        summaries = {}
        for idx,text in articles.items():
            summaries[idx]=predict(text,model)

            summary_dict = {heds[idx][0]:summaries[idx]}
            file_name =f'news{idx}.json'
            file_path = os.path.join(sum_path,file_name)
            with open(file_path,'w') as f:
                json.dump(summary_dict,f,indent=4)
    
    return summaries,heds

if __name__== '__main__':
    sum = get_prediction()
    print(sum)
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.predict import get_prediction

# Setup FastAPI app
app = FastAPI(
    title="API Server",
    description="API Server",
    version="v1"
)

# Enable CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
# @app.get("/")
# async def get_index():
#     return {
#         "message": "Home mising webpage"
#     }

@app.get("/")
async def get_summaries():
    final=[]
    summary_dict=get_prediction()
    for keys in summary_dict.keys():
        for k,v in summary_dict[keys].items():
            final.append({'hed':k,'sum':v})
 
    return final

@app.get("/inter")
async def get_summaries_international():
    final=[]
    v=get_prediction()
    for k,v in v['internat'].items():
        final.append({'hed':k,'sum':v})
    return final
    
@app.get("/national")
async def get_summaries_national():
    final=[]
    summary_dict=get_prediction()
    for k,v in summary_dict['nat'].items():
        final.append({'hed':k,'sum':v})
    return final

@app.get("/sport")
async def get_summaries_sports():
    final=[]
    summary_dict=get_prediction()
    for k,v in summary_dict['sports'].items():
        final.append({'hed':k,'sum':v})
    return final

@app.get("/tech")
async def get_summaries_tech():
    final=[]
    summary_dict=get_prediction()
    for k,v in summary_dict['tech'].items():
        final.append({'hed':k,'sum':v})
    return final
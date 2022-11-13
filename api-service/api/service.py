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
@app.get("/")
async def get_index():
    return {
        "message": "Home mising webpage"
    }

@app.get("/home")
async def get_summaries():
    final={}
    sum,hed=get_prediction()

    for i in hed.keys():
        final[hed[i]] = sum[i]
    
    return final
        
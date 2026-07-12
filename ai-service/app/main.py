from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import hashlib
app=FastAPI(title='Clinical Evidence AI Service')
class SearchRequest(BaseModel):
    question:str
    protocolId:str
    sources:list[Literal['pubmed','maude','internal']]
@app.get('/health')
def health():
    return {'status':'ok','service':'evidence-ai'}
@app.post('/search')
def search(req:SearchRequest):
    query='("influenza"[Title/Abstract]) AND (molecular OR NAAT) AND (sensitivity OR agreement)'
    records=[{'source':'PubMed','id':'38910211','title':'Analytical and clinical performance of a multiplex respiratory assay','decision':'pending-human-screening','evidenceLevel':'candidate'},{'source':'MAUDE','id':'2026-4412','title':'False-negative complaint trend','decision':'signal-review','evidenceLevel':'surveillance'}]
    return {'protocolId':req.protocolId,'searchStrategy':query,'queryHash':hashlib.sha256(query.encode()).hexdigest(),'records':records,'controls':['Human screening required','Copyright and source terms apply','No autonomous clinical conclusion']}

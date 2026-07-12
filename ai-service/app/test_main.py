from app.main import search,SearchRequest
def test_search_has_hash():
    result=search(SearchRequest(question='clinical performance influenza',protocolId='P-1',sources=['pubmed']))
    assert len(result['queryHash'])==64
def test_human_control():
    result=search(SearchRequest(question='test evidence',protocolId='P-1',sources=['pubmed']))
    assert 'Human screening required' in result['controls']

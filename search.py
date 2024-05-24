def search_by_criteria(index, criteria, value):
    return index.get(criteria, {}).get(value, [])

def recommend(index, search_params, start=0, limit=5):
    if not search_params:
        return []

    criteria, value = next(iter(search_params.items()))
    results = search_by_criteria(index, criteria, value)
    
    for criteria, value in search_params.items():
        results = [item for item in results if item in search_by_criteria(index, criteria, value)]
    
    return results[start:start+limit] 
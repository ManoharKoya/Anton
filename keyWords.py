from monkeylearn import MonkeyLearn

ml = MonkeyLearn('4c542abbabebda0cea399c23cad345a05ffde48f')

def get_key_words(txt):
    data = [txt]
    model_id = 'ex_YCya9nrn'
    result = ml.extractors.extract(model_id, data)
    lst = []
    for i in result.body :
        for j in i["extractions"]:
            lst.append(j["parsed_value"])
    return lst
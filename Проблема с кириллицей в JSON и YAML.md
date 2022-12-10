    
-- *JSON* --\
with open(file_buy, selector, encoding='utf-8') as f:\
===> json.dump(buy, f, **ensure_ascii=False**)

-- *YAML* --\
with open(file_buy2, selector, encoding='utf-8') as f:\
===> yaml.dump(buy, f, **allow_unicode=True**)
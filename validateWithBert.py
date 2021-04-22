import torch
import numpy as np
from torch import nn
from transformers import AutoConfig, AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('FPTAI/vibert-base-cased', do_lower_case=False)
model = AutoModel.from_pretrained('FPTAI/vibert-base-cased')


def validate(s1, s2):
    list_s2 = s2.split()

    if len(list_s2) < 3:
        err_code = 1
        err_txt = 'Câu quá ngắn, vui lòng thử lại.'
        return err_code, err_txt

    encoding1 = tokenizer(s1, max_length=128, truncation=True, padding='max_length', return_token_type_ids=False)
    encoding2 = tokenizer(s2, max_length=128, truncation=True, padding='max_length', return_token_type_ids=False)

    encoding1['input_ids'] = torch.from_numpy(np.array([encoding1['input_ids']]))
    encoding1['attention_mask'] = torch.from_numpy(np.array([encoding1['attention_mask']]))

    encoding2['input_ids'] = torch.from_numpy(np.array([encoding2['input_ids']]))
    encoding2['attention_mask'] = torch.from_numpy(np.array([encoding2['attention_mask']]))

    embed1 = model(encoding1['input_ids'], encoding1['attention_mask'])[0][:, 0]
    embed2 = model(encoding2['input_ids'], encoding2['attention_mask'])[0][:, 0]

    score = nn.functional.cosine_similarity(embed1, embed2).tolist()[0]
    err_code = 0
    return err_code, score

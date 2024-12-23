import transformers
import torch
from huggingface_hub import login
import os
import json
import pandas as pd
import time
os.environ['HF_HOME'] = '/clwork/zhidong/llama/cache'

def generate_simplified(pipeline, prompt):
    messages = [
        {"role": "system", "content": "You are a doctor who can explain everything easliy to the patient"},
        {"role": "user", 
        "content": 
        f"""
    Objective: Simplify the provided text by:
    1. Rephrasing complex sentences for clarity.
    2. Replacing or defining rarely-used terms.

    Guidelines:
    - For sentences that seem complex, rephrase them in simpler terms.
    - If you encounter unfamiliar or rare words, either replace them with a commonly known synonym or provide a concise definition.

    Note: In the training samples, complex sentences are flagged with `<rephrase>` and rare terms with `<rare>`. However, these tokens won't appear in testing samples. You'll need to recognize and address such complexities independently.

    Examples:

    1.
    Original:
    Furthermore, the circumference of thighs was measured to assess the <rare>postoperative swelling<rare>.
    A total of 444 hypertensive patients, aged between 27 to 65 years, without any recent hypertensive treatment, were included.
    <rephrase>The tongue often obstructs the upper respiratory tract, especially in comatose patients or those with cardiopulmonary arrest.<rephrase>

    Simplified:
    Additionally, we measured thigh sizes to check for swelling after surgery.
    444 patients, aged 27-65 with high blood pressure and no recent treatment, were studied.
    The tongue can block breathing, mostly seen in unconscious people or those who've had a sudden heart stoppage.

    Your task: Apply these guidelines to simplify the provided texts.

    Now simplify the following sentence:
    Original: 
    {prompt}

    Simplified:
    """},
    ]

    outputs = pipeline(
        messages,
        max_new_tokens=512,
    )

    return outputs[0]["generated_text"][-1]['content'].replace("\n", "").replace("\r", "")

import re

def extract_simplified_sentence_or_return_original(text):
    # Use regex to find the sentence that follows the phrases indicating simplification
    match = re.search(r"simplified sentence would be:\s*\"(.*?)\"|even simpler terms:\s*\"(.*?)\"", text)

    # If a match is found, return the simplified sentence
    if match:
        return match.group(1) if match.group(1) else match.group(2)

    # If no match is found, return the original text
    return text

def postprocesing(data):
  data['generated']=data['generated'].apply(lambda x: x.replace("Here's a simplified version:",""))
  data['generated']=data['generated'].apply(lambda x: x.replace("Here's a simplified version of the sentence:\"",""))
  data['generated']=data['generated'].apply(lambda x: x.replace("Here's a simplified version of the sentence:",""))
  data['generated']=data['generated'].apply(lambda x: x.replace("Here's a simplified version:",""))
  data['generated']=data['generated'].apply(lambda x: x.replace("Simplified:",""))
  data['generated']=data['generated'].apply(lambda x: x.replace("**Simplified**:",""))
  data['generated']=data['generated'].apply(lambda x: x.replace("Here's a simplified version of the given sentence:",""))
  data['generated']=data['generated'].apply(lambda x: x.replace("Here's the simplified version of the sentence:",""))
  data['generated']=data['generated'].apply(lambda x: x.replace("Here's the simplified version:",""))
  data['generated']=data['generated'].apply(lambda x: x.replace("\"",""))
  data['generated']=data['generated'].apply(lambda x: extract_simplified_sentence_or_return_original(x))
  return data
 

if __name__ == "__main__":
    
    accesstoken = "/clwork/zhidong/llama/token.txt"
    with open(accesstoken,'r', encoding='utf-8') as f:
        token = f.read()
        login(token=token, add_to_git_credential=True)

    # filename = "/clwork/zhidong/llama/data/plaba.tsv"
    filename = "/clwork/zhidong/llama/data/plabatest.tsv"

    plaba = pd.read_csv(filename,index_col=None,sep='\t')

    model_id = "meta-llama/Meta-Llama-3.1-70B-instruct"

    pipeline = transformers.pipeline(
        "text-generation",
        model=model_id,
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto",
        # device=0,
        batch_size=256,
    )
    print('----------generating----------')
    start = time.time() 

    print(len(plaba["sentence"]))
    
    result = [generate_simplified(pipeline, text) for text in plaba['sentence']]
    end = time.time() 
    time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
    print(time_diff)

    plaba['generated'] = result
    plaba.to_csv("/clwork/zhidong/llama/data/plaba_generated_70b_instruct_testdata.tsv",sep="\t",encoding="utf-8",index=None)
    plaba = postprocesing(plaba)
    plaba.to_csv("/clwork/zhidong/llama/data/plaba_generated_70b_instruct_testdata_postprocessed.tsv",sep="\t",encoding="utf-8",index=None)


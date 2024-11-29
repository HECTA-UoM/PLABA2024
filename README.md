# PLABA2024 from Manchester (United, MMU+UoM) NLP
PLABA 2024 system report with shared fined models RoBERTa-Base and prompts for LLMs

# Task 1 - Term Replacement
- Task 1 will not require complete adaptation. Rather, your system will identify difficult terms, decide how to handle them, and provide replacements.
  - Task 1A - Identifying non-consumer terms: Given an abstract, return a list of exact strings from the text, each representing a concept a consumer would not understand.
  - Task 1B - Classifying replacement: For each identified non-consumer term, determine whether the term could be (non-exclusively):
  - Task 1C - Generation: Provide text for each positive label from 1B (except "omitted" label).


# Task 2 - Complete Abstract Adaptation
- Task 2 is to end-to-end adapt biomedical abstracts for the general public using plain language. Given a set of abstracts (the source), your system will provide output for each sentence of the source

# Please cite our work if you use the materiels shared here, the fine-tuning scirpt, prompts, saved models, etc.

@misc{ling2024beemancplabatracktac2024,
      title={BeeManc at the PLABA Track of TAC-2024: RoBERTa for task 1 and LLaMA3.1 and GPT-4o for task 2}, 
      author={Zhidong Ling and Zihao Li and Pablo Romeo and Lifeng Han and Goran Nenadic},
      year={2024},
      eprint={2411.07381},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={ https://arxiv.org/abs/2411.07381 }, 
}

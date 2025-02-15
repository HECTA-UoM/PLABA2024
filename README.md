# PLABA2024 from Manchester (United, MMU+UoM) NLP
PLABA 2024 system report with shared fined models RoBERTa-Base and prompts for LLMs

# Task 1 - Term Replacement
- Task 1 will not require complete adaptation. Rather, your system will identify difficult terms, decide how to handle them, and provide replacements.
  - Task 1A - Identifying non-consumer terms: Given an abstract, return a list of exact strings from the text, each representing a concept a consumer would not understand.
  - Task 1B - Classifying replacement: For each identified non-consumer term, determine whether the term could be (non-exclusively):
  - Task 1C - Generation: Provide text for each positive label from 1B (except "omitted" label).


# Task 2 - Complete Abstract Adaptation
- Task 2 is to end-to-end adapt biomedical abstracts for the general public using plain language. Given a set of abstracts (the source), your system will provide output for each sentence of the source

# Abstract
This report is the system description of the \textsc{MaLei} team (\textbf{Manchester} and \textbf{Leiden}) for shared task Plain Language Adaptation of Biomedical Abstracts (PLABA) 2024 (we had an earlier name BeeManc following last year). 
This report contains two sections corresponding to the two sub-tasks in PLABA-2024. 
In task one, we applied fine-tuned ReBERTa-Base models to identify and classify the difficult terms, jargon and acronyms in the biomedical abstracts and reported the F1 score. 
Due to time constraints, we didn't finish the replacement task. 
In task two, we leveraged Llamma3.1-70B-Instruct and GPT-4o with the one-shot prompts to complete the abstract adaptation and reported the scores in BLEU, SARI, BERTScore, LENS, and SALSA.
From the official Evaluation from PLABA-2024 on Task 1A and 1B, our \textbf{much smaller fine-tuned RoBERTa-Base} model ranked 3rd and 2nd respectively on the two sub-tasks, and the \textbf{1st on averaged F1 scores across the two tasks} from 9 evaluated systems. Our LLaMA-3.1-70B-instructed model achieved the \textbf{highest Completeness} score for Task-2.
We share our source codes, fine-tuned models, and related resources at https://github.com/HECTA-UoM/PLABA2024


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

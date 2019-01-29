1) Training model (encoder-decoder):

- Downloading the training UMBC data at page (because the data is very large, up to 15GB, we cannot include them in the submission): https://ebiquity.umbc.edu/resource/html/id/351/UMBC-webbase-corpus. Pleasing using the option that contains both words and their POS taggings. Then run dataset_tokenizer.py to extract and tokensize the words and POS taggings.

- Using preprocess_dataset.py to turn these raw data into TFRecords files for words and POS seperately. Put words TFRecords files in folder "/UMBC corpus TFRecords/TFRecords_words". Put words TFRecords files in folder "/UMBC corpus TFRecords/TFRecords_POSs".

- Downloading the Glove embeddings (1.5GB) at https://nlp.stanford.edu/projects/glove/. Please use the 6B-300d version for our model. Put them at "/src/dictionaries/Glove"

- Running train.py for training. For our results, we have trained the model for 7 hours.
  


2) Evaluating model (encoder only):

Because what we have trained is an encoder, we will evaluate it by using them for sentence embeddings for 4 downstream tasks. For each task we will train a model on top of this encoder and evaluate the performance of this model. 
Please consult here if having any trouble regarding running the evaluation step: https://github.com/facebookresearch/SentEval.
Each of these training + testing task takses about 1 hour. So please be patient.

a) CR:
- Download data at: https://nlp.stanford.edu/~sidaw/home/projects:nbsvm
- Put the data in "evaluations/CR"
- Running training/testing code:
  + Open evaluate.py, changing the code at line 54 and 55 to "CR" and "evaluations/CR"
  + Modify the code at line 52 to 1 (0 is for original model, 1 is our proposed model)
  + Run evaluate.py


b) TREC:
- Download data at: http://cogcomp.org/Data/QA/QC/
- Put the data in "evaluations/TREC"
- Running training/testing code:
  + Open evaluate.py, changing the code at line 54 and 55 to "TREC" and "evaluations/TREC"
  + Modify the code at line 52 to 1 (0 is for original model, 1 is our proposed model)
  + Run evaluate.py

c) SICK:
- Download data at: http://clic.cimec.unitn.it/composes/sick.html
- Put the data in "evaluations/SICK"
- Running training/testing code:
  + Open evaluate.py, changing the code at line 54 and 55 to "SICK" and "evaluations/SICK"
  + Modify the code at line 52 to 1 (0 is for original model, 1 is our proposed model)
  + Run evaluate.py

d) MSRP:
- Download data at: https://www.microsoft.com/en-us/download/details.aspx?id=52398&from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fdownloads%2F607d14d9-20cd-47e3-85bc-a2f65cd28042%2Fdefault.aspx
- Put the data in "evaluations/MSRP"
- Running training/testing code:
  + Open evaluate.py, changing the code at line 54 and 55 to "MSRP" and "evaluations/MSRP"
  + Modify the code at line 52 to 1 (0 is for original model, 1 is our proposed model)
  + Run evaluate.py

* Caveat: If you don't run train.py, you still need to download Glove embeddings as instructed in (1) in order to run the evaluation step.




  
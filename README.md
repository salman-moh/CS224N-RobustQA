# Question Answering NLP Task:
### Gaining More from Less Data in out-of-domain Question Answering Models


We propose text augmentation techniques for Question Answering task in NLP that
involves using synonyms with stochasticity on out-of-domain datasets (DuoRC
and RACE and RelationExtraction) that are set to be 400 times smaller than the
in-domain datasets (SQuAD, NewsQA, NaturalQuestions). We address ways to
improve extraction of generalized information from out-of-domain or less available
datasets from large pre-trained models like BERT or its variation DistilBERT which
is used here with also being able to benefit from producing QA applications across
domains. It is found that augmenting less available QA datasets in ways described,
indicate improvement in generalization, but not all augmentations strategies are
equally good. We find that these augmentations are helpful in achieving better
performance on out-of-domain data.


![Image-paragraph-Salman](https://user-images.githubusercontent.com/31631107/140655800-c367f76e-7b6a-470a-a7a6-5dbb22d61c8a.jpg)


## Starter code for robustqa track
- Download datasets from [here](https://drive.google.com/file/d/1Fv2d30hY-2niU7t61ktnMsi_HUXS6-Qx/view?usp=sharing)
- Setup environment with `conda env create -f environment.yml`
- Train a baseline MTL system with `python train.py --do-train --eval-every 2000 --run-name baseline`
- Evaluate the system on test set with `python train.py --do-eval --sub-file mtl_submission.csv --save-dir save/baseline-01`
- Upload the csv file in `save/baseline-01` to the test leaderboard. For the validation leaderboard, run `python train.py --do-eval --sub-file mtl_submission_val.csv --save-dir save/baseline-01 --eval-dir datasets/oodomain_val`

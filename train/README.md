# README

This repo contains final project by Group 22.

## File Directory

### Main Items
- Fake-News-Detection-Final.pdf
    - this is the final report in pdf format
- Fake-News-Detector.pdf
    - this is the presentation in pdf format
- Fake-News-Detector.pptx
    - this is the presentation in powerpoint format
- FakeNewsDetection_Finalproject.ipynb
    - this is the jupyter notebook containing the code

### Related Files
In order for the notebook to run completely, the following three files are included. However, we have uncommented parts of the code in the jupyter notebook to avoid retraining the models. As a result, it is possible to run the code without model training with additional pickle files. This is described in further detail in the next section.

- train.json
- us_politicians.csv
- related_articles

### Pickle Files
Since this is a lengthy notebook, running from start to finish often crashes the kernel. As a result, we have decided to load and save pickle files at the start and end of every section, respectively, as a means of saving the progress. By doing so, each section in this report are independent of the rest given that the correct input pickle files are available. This enables us to run/test specific sections, without running the entire code from the beginning.

To conduct individual section testing, you may find all available pickle files at the following link.

Link: https://utoronto-my.sharepoint.com/:f:/g/personal/aaronhao_tan_utoronto_ca/EtY5W9Vr3MZBvWjEihYwY7kBRG02wRoLYzyISJD2qd3T9g?e=CNNDeQ

### Prerequisite Files
This code involves the training of four different classification models as well as a Doc2Vec model which takes a total of 8+ hours. In addition, the processing of the text data for feature exploration and engineering takes an additional 2 hours (on a 32 core machine). As a result, certain parts of this code are commented out to avoid a lengthy run time. The fully trained models and complete dataframes are instead loaded in to this notebook as pickle files. Therefore, to successfully run this file, the following files must exist in the same directory. It is worth noting that even with these files loaded, we skip all training code; because the notebook will still take roughly 3 hours to run from beginning to end.

- Model Files
    - Doc2Vec Model:
        - 30epoch_150vec.model
        - 30epoch_150vec.model.wv.vectors.npy
        - 30epoch_150vec.model.trainables.syn1neg.npy
        - 30epoch_150vec.model.docvecs.vectors_docs.npy
    - Classification mModel:
        - best_model_dtc.pkl
        - best_model_knn.pkl
        - best_model_svm.pkl
        - best_model.logistic.pkl
- Dataframe Files
    - article_sentences_ind.pkl

# Automatic Language Detection of textual documents
The goal of this project is to create a simple **language detection ML model** using known **NLP** techniques. The project was written entirely in **Python**. The data used is a labeled set of sentences in 22 languages.
Detailed description and thorough analysis can be found in *FinalReport.pdf*. The project contains:
1. Basic *Explratory Data Analysis* - comparing statistical text feature among different languages
2. Preprocessing
  1. Data cleaning - lowercasing the entire dataset, punctuation removal was also considered
  2. Feature engineering - features used: *unigram token frequency* for different vocabulary sizes, sentence to character ratio, average word length and an a priori predicted probability of the sentence belonging to each language using the utf-8
codes for prediction. Additional features were considered, such as bigram and trigram tokenization, commas ratio, periods ratio and special symbols ratio.
  4. Normalization
3. Model training - the following classification models were used: *Naive Bayes* as baseline, *XGBoost* and *SVC*. The models were compared using confusion matrices and F1-score.
4. Result analysis - includes PCA analysis and vocabulary coverage analysis for different sizes of vocabulary and both character and word tokenization

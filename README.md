# Data Science Project Template

_A reproducible data science project template inspired from [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/)._


### Template can be downloaded using command:
``` bash
    wget https://github.com/ibuda/ds-project-template
```

or by cloning it:

``` bash
    git clone https://github.com/ibuda/ds-project-template
```


### The template directory structure
------------

The directory structure of the template is as follows: 

```
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── predictions    <- The results of your model predictions.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── build_features.py  <- script to build feature set.
├── make_dataset.py    <- script to generate final, canonical data set for training.
├── predict_model.py   <- script to generate predictions on test dataset.
│── train_model.py     <- script to train model on train dataset.

```
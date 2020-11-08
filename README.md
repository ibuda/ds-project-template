# Data Science Project Template

_A reproducible data science project template inspired from [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/)._


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

# How to create project environment with Conda

1. Create environment, substitute <env_name> with your desired environment name: `conda create -n <env_name>`
2. Activate it: `conda activate <env_name>`
3. In case you will need jupyter lab with it:  
    a. Install ipykernel to be used with jupyterlab:  
	`conda install ipykernel`  
    c. Configure python kernel, substitute <kernel_name> with your desired kernel name. It will appear in jupyter lab available kernels list:  
	`ipython kernel install --user --name=<kernel_name>`  
    b. Install jupyter lab:  
	`conda install jupyterlab`  

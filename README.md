scikit-physlearn
----------------

**scikit-physlearn** is a Python package for single-target and multi-target regression. 
It is designed to amalgamate regressors in
[scikit-learn](https://scikit-learn.org/),
[LightGBM](https://lightgbm.readthedocs.io/en/latest/index.html),
[XGBoost](https://xgboost.readthedocs.io/en/latest/),
[CatBoost](https://catboost.ai/),
and [Mlxtend](http://rasbt.github.io/mlxtend/)
with a unified ```Regressor``` object that follows the scikit-learn API with data representations in pandas.
Moreover, it offers the ability to boost these regressors with a modified initialization,
as described in the paper: *Boosting on the shoulders of giants in quantum device calibration*.

The repository was started by Alex Wozniakowski during his graduate studies at Nanyang Technological University.

Reference Paper
----------------
If you use this code, please consider adding the corresponding citation:
```
@article{wozniakowski2020boosting,
  title={Boosting on the shoulders of giants in quantum device calibration},
  author={Wozniakowski, Alex and Thompson, Jayne and Gu, Mile and Binder, Felix},
  journal={arXiv preprint arXiv:2005.06194},
  year={2020}
}

```

Below is the directory structure for ```paper_results```:
```
examples
|
|
|___paper_results
    |   improved_main_body.py
    |   main_body.py
    |   supplementary.py
```

The results in ```main_body.py``` use a
[StackingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html)
for each single-target subtask, and the pseudo-residuals are the negative gradient of the squared error loss function.
The results in ```improved_main_body.py``` use a
[Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) regressor for the third single-target subtask,
and for each single-target subtask the pseudo-residuals are the negative gradient of the Huber loss function.
The results in ```supplementary.py``` use an
[MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html)
for each single-target subtask, and the regressor uses the raw control voltage features as input.

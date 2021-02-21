from utils.propertieshelper import load_properties
import os
import pickle
import json
from sklearn.model_selection import train_test_split, GridSearchCV


class TrainPredict:

    def __init__(self, config_path, model_name):
        model_props = load_properties(config_path, model_name)
        self.target = model_props['target']
        self.test_size = float(model_props['test_size'])
        self.model_output_filepath = model_props['model_output_filepath']
        self.model_result_filepath = model_props['model_result_filepath']
        self.features_filename = model_props['features_filename']

    def data_preparation(self):
        return df

    def feature_engineering(self, df):
        return df

    def feature_selection(self, df):
        return X, y, feature_names

    def train_test_split(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=42)
        return X_train, X_test, y_train, y_test

    def grid_search_train(self, X, y, estimator, param):
        param_grid = {
            "rf": {
                "n_estimators": [80],
                "bootstrap": ['True'],
                "criterion": ['mse'],
                "max_features": ['auto', 'sqrt'],
                "min_samples_leaf": [50]
            }
        }
        print(param_grid[param])
        X_train, X_test, y_train, y_test = self.train_test_split(X, y)
        grid_search = GridSearchCV(estimator, param_grid[param], cv=5, n_jobs=-1)
        grid_search.fit(X_train, y_train)
        model = grid_search.best_estimator_
        predictions = model.predict(X_test)
        return model, predictions, y_test

    def save_model(self, model, model_name):
        full_path = os.path.join(self.model_output_filepath, model_name)
        pickle.dump(model, open(full_path, 'wb'))

    def save_output(self, y_pred_test, y_test, output_name):
        results = {"y_pred_test": y_pred_test.tolist(),
                   "y_test": y_test.tolist()}
        with open(os.path.join(self.model_result_filepath, output_name), 'w') as ofile:
            json.dump(results, ofile)

    def post_processing(self):
        return

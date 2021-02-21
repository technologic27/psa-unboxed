from utils.propertieshelper import load_properties
import pandas as pd
import numpy as np


class Features:

    def __init__(self, config_path, model_name):
        model_props = load_properties(config_path, model_name)
        self.categorical_features = model_props['categorical_features']
from typing import Any, Optional
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sn
import yaml


class Analysis():
	def __init__(self, analysis_config:str):
		CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']

 		# add analysis config to list of paths to load
		paths_to_load = CONFIG_PATHS + [analysis_config]

		# initialize an empty dictionary to hold the final configuration
		config = {}

		for path in paths_to_load:
			with open(path, 'r') as f:
				this_config = yaml.safe_load(f)
			config.update(this_config)

		self.config = config

	def load_data(self):
		self.config['data_path']
		pass
	
	def compute_analysis(self):
		pass

	def plot_data(self, save_path:Optional[str] = None) -> matplotlib.Figure:
		pass

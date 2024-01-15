import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
from typing import List, Optional

class Analysis:
    def __init__(self, analysis_config: str):
        self.config = {
            'analysis_config': analysis_config,
            **self.load_config('configs/system_config.yml'),
            **self.load_config('configs/user_config.yml'),
        }

    def load_config(self, path: str) -> dict:
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def load_data(self):
        self.config['repos'] = self.get_top_starred_repos()

    def compute_analysis(self):
        repos = self.config.get('repos', [])
        if not repos:
            raise Exception("No data to analyze. Load data first.")
        lang_stars = {}
        for repo in repos:
            lang = repo["name"].split('/')[0]
            lang_stars.setdefault(lang, []).append(repo["stars"])
        self.analyze_language_stars(lang_stars)

    def analyze_language_stars(self, lang_stars):
        languages, stars_per_language = zip(*lang_stars.items())

        # Box plot
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=languages, y=stars_per_language)
        self.set_plot_labels("Comparison of Stars Across Programming Languages")
        plt.show()

        # Alternatively, use a bar plot
        plt.figure(figsize=(10, 6))
        sns.barplot(x=languages, y=[sum(stars) / len(stars) for stars in stars_per_language])
        self.set_plot_labels("Comparison of Average Stars Across Programming Languages")
        plt.show()

    def set_plot_labels(self, title):
        plt.xlabel("Programming Language")
        plt.ylabel("Number of Stars")
        plt.title(title)
        plt.xticks(rotation=45)

    def plot_data(self, save_path: Optional[str] = None) -> plt.Figure:
        repos = self.config.get('repos', [])
        if not repos:
            raise Exception("No data to plot. Load data first.")
        self.plot_histogram(repos)
        self.bar_plot(repos)

    def get_top_starred_repos(self) -> List[dict]:
        url = "https://api.github.com/search/repositories?q=stars:%3E1&sort=stars"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error retrieving data from GitHub API: {response.status_code}")
        return [{"name": item["full_name"], "stars": item["stargazers_count"]} for item in json.loads(response.text)["items"]]

    def plot_histogram(self, repos: List[dict]):
        stars = [repo["stars"] for repo in repos]
        sns.histplot(stars, bins=20)
        self.set_plot_labels("Histogram of the number of stars for the top 20 most starred Repos")
        plt.show()

    def bar_plot(self, repos: List[dict]):
        stars = [repo["stars"] for repo in repos]
        names = [repo["name"].split('/')[1] for repo in repos]
        plt.barh(names, stars)
        self.set_plot_labels("Bar plot of the top most starred Repos in Github")
        plt.show()


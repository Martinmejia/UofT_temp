This repository contains a Python class, Analysis, that performs analysis on the top-starred GitHub repositories based on their programming languages.

1. Overview
    The Analysis class is designed to load GitHub repositories data, compute analysis, and plot visualizations. It utilizes the GitHub API to retrieve information about top-starred repositories.

  1.1 Getting Started
    1.1.1. Clone the repository:

      bash
      Copy code
      git clone https://github.com/your-username/analysis-repo.git

    1.1.2. Install the required dependencies:

      bash
      Copy code
      pip install requests matplotlib seaborn pyyaml

    1.1.3. Ensure you have a valid GitHub API token. You can create one following the instructions here:
    https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

    1.1.4. Create two configuration files:

        - configs/system_config.yml: Contains system-level configurations.
        - configs/user_config.yml: Contains user-specific configurations, including the GitHub API token.
        
        Example system_config.yml:

          yaml
          Copy code
          github_api_url: https://api.github.com

        Example user_config.yml:

          yaml
          Copy code
          github_api_token: YOUR_GITHUB_API_TOKEN

2. Usage

Example usage of the Analysis class:

  from Analysis import Analysis

  # Create an instance of Analysis with the path to user_config.yml
  analysis = Analysis(analysis_config='configs/user_config.yml')

  # Load data from GitHub API
  analysis.load_data()

  # Compute and analyze the data
  analysis.compute_analysis()

  # Plot data
  analysis.plot_data()

3. Methods

  __init__(self, analysis_config: str) -> None
  Initializes the Analysis class with the path to the user configuration file.

  load_config(self, path: str) -> dict
  Loads configuration data from a YAML file.

  load_data(self) -> None
  Retrieves and loads top-starred repositories data from the GitHub API.

  compute_analysis(self) -> None
  Computes analysis on the loaded data, such as box plots and bar plots.

  plot_data(self, save_path: Optional[str] = None) -> plt.Figure
  Plots histogram and bar plots of the top-starred repositories.

  get_top_starred_repos(self) -> List[dict]
  Retrieves the top-starred repositories from the GitHub API.

  plot_histogram(self, repos: List[dict]) -> None
  Plots a histogram of the number of stars for the top 20 most-starred repositories.

  bar_plot(self, repos: List[dict]) -> None
  Plots a bar plot of the top most-starred repositories on GitHub.

4. License
  This project is licensed under the MIT License - see the LICENSE file for details.
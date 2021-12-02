# Conda

1. Create a virtual environment
   * `conda create --name my_env_name python=3.8` or whatever Python version you may need.
2. List available envs (2 different ways
   * `conda env list`
   * `conda info --envs`
3. Activate virtual env
   * `conda activate my_env_name`
4. Deactivate current environment
   * `conda deactivate`
5. If pip doesn't work with a fresh conda install:
   * `conda install pip`
6. Install project dependencies (listed in requirements.txt file)
   * `conda install --file requirements.txt`
   * `pip install -r requirements.txt`
7. Delete an old environment
   * `conda remove --name my_env_name --all`
   * `conda env remove -n my_env_name`
8. Update conda
   * `conda update conda`
9. Update all packages in the current environment
   * `conda update --all`
10. Update all packages in another env
    * `conda update -n my_env_name --all`
11. List installed packages in current environment
    * `conda list`
12. Add conda-forge channel
    * `conda config --add channels conda-forge`
13. Check conda channels
    * `conda config --show channels`
14. Remove conda-forge channel
    * `conda config --remove channels conda-forge`
15. Create an environment file from your current environment.
    * `conda env export --from-history > environment.yml`
16. Create a new environment and install dependencies listed in YML file.
    * `conda env create -f environment.yml`

# DS3K

This README attempts to explain the structure of our DS3000 project.

## `data`
- Contains both raw and processed data used in our project.
- The subdirectories with group member names are their individual data records from Spotify.
- The subdirectory `group` includes the final processed data used to train our models.
  - You can see most of its creation in the `transformation` directory.
## `eda`
- Contains initial exploration of data, as well as some early steps of data conglomeration, transformation, and visualization
- Much of the data included in these files was not used in final model training, as we originally featurized our entire streaming history
## `transformation`
- Contains code that was used to prepare the master table of our streaming libraries and create the train/test split.
- Data is transformed (encoded / scaled) in these notebooks, then saved to `data/`
## `classification_models`
- Contains notebooks where each of our model implementations were created
- Additionally includes model comparison visualizations.
## Upper level files
- `api-setup.py` - used to get API keys from a file ignored by git
- `requirements.txt` - some of the libraries used in our analysis
  - Probably isn't up to date!
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python [conda env:mne]
#     language: python
#     name: conda-env-mne-py
# ---

# %%
# import dependencies
import ipywidgets
import bokeh
from bokeh.io import output_notebook, push_notebook

output_notebook()
# %% [markdown]
# #### This is a demonstration of a simple browser for eegs in the eeg.h5/eeghdf format

# %%

import eegvis.nb_eegview as nb_eegview
import eeghdf

# %%
# use full browser width
nb_eegview.setNotebookWidth100()
# %%
# load your eeg file (use one that comes with the eeg-hdfstorage package)
hf = eeghdf.Eeghdf("../../eeg-hdfstorage/data/absence_epilepsy.eeghdf")

# %%
browser = nb_eegview.EeghdfBrowser(hf)

# %%
browser.show()

# %% [markdown]
# Note, this depends on ipywidgets and bokeh interactions. Depending on the version of ipywidgets and the installation state, this may not work in jupyterlab. For instance, it was not initially working for me in jupyter lab version 1.0.2. However, after doing:
# ```
# $ jupyter labextension install @jupyter-widgets/jupyterlab-manager
# $ jupyter labextension install jupyterlab_bokeh
# ```
# It worked fine in jupyter lab for me.
#

# %%
bokeh.__version__

# %%
ipywidgets.__version__

# %%
import scipy
scipy.__version__

# %%

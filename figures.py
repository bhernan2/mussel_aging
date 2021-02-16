import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

rename_melt =  pd.read_csv("agers_melt.csv")

def aging_boxplot():
    fig = px.box(rename_melt, 
            x="variable", 
            y="value", 
            color="variable",
            boxmode="overlay", 
            points='all')

    return fig


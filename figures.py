import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

rename_melt =  pd.read_csv("agers_melt.csv")
df_rename = pd.read_csv("zebra_mussels/burrow_scatter.csv")
df_types = pd.read_csv("zebra_mussels/burrow_boxplot.csv")
def aging_boxplot():
        fig = px.box(rename_melt, 
            x="variable", 
            y="value", 
            color="variable",
            boxmode="overlay",
        #     title='<i>L. teres</i>',
            labels = {'variable': 'Agers', 'value':'Age'},
            points='all',
            color_discrete_sequence=["#601A4A", "#EE442F", "#63ACBE"],
            )
        fig.update_layout(height=700, width=900,)
        return fig

def zebra_burrow_scatter():
        fig = make_subplots(rows=3, cols=4,subplot_titles=("T1", "T2", "T3", "T4", "T5", "T6", "T7","T8","T9", "T10", "T11", "T12"))

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T1"], mode='markers'),
              row=1, col=1)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T2"], mode='markers'),
              row=1, col=2)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T3"], mode='markers'),
              row=1, col=3)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T4"], mode='markers'),
              row=1, col=4)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T5"], mode='markers'),
              row=2, col=1)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T6"], mode='markers'),
              row=2, col=2)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T7"], mode='markers'),
              row=2, col=3)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T8"], mode='markers'),
              row=2, col=4)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T9"], mode='markers'),
              row=3, col=1)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T10"], mode='markers'),
              row=3, col=2)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T11"], mode='markers'),
              row=3, col=3)

        fig.add_trace(go.Scatter(x=df_rename["Day"], y=df_rename["T12"], mode='markers'),
              row=3, col=4)

        #just to save
        fig.update_layout(height=500, width=500,
                #   title_text="Counts of mussels burrowed ~90% by tanks across days",
                  showlegend=False)
        return fig
def zebra_burrow_boxplot():
        fig = px.box(df_types, 
            x="type", 
            y="value", 
            color="type",
            boxmode="overlay",
        #     title='Boxplots of control and treatment (zebra mussels present & zebra mussels attached) tanks. <br>The ends of the box represent the lower and upper quartiles, while the median (second <br>quartile) is marked by a line inside the box.<br><br>',
            labels = {'type': 'Type', 'value':'Count'},
            points='all',
            color_discrete_sequence=["#601A4A", "#EE442F", "#63ACBE"],
            )
        fig.update_layout(height=500, 
                          width=500,
                        )
        return fig


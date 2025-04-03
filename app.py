import io
import json

import matplotlib
import numpy as np
import pandas as pd
import plotly
from flask import Flask, render_template, send_file, jsonify
from matplotlib import pyplot as plt
import plotly.graph_objects as go
from matplotlib.pyplot import title
from plotly.graph_objs import Figure
from plotly.subplots import make_subplots

matplotlib.use('Agg')

app = Flask(__name__)


def read_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=2)
    df.columns = df.columns.str.strip()
    return df


@app.route('/plot')
def create_plot():
    try:
        df = read_data(r"data/NIHMS1635539-supplement-1635539_Sup_tab_4.xlsx", "S4B limma results")

        if 'logFC' not in df.columns or 'adj.P.Val' not in df.columns or 'EntrezGeneSymbol' not in df.columns:
            return "Used columns are not found", 500

        plot: Figure = go.Figure()

        plot.add_trace(go.Scatter(x=df["logFC"], y=-np.log10(df["adj.P.Val"]), mode='markers', marker=dict(color=-np.log10(df['adj.P.Val']), colorscale='Plotly3', size=9, opacity=0.8), text=df['EntrezGeneSymbol'], customdata=df['EntrezGeneSymbol'], hoverinfo='text', name='Volcano Plot'))

        plot.update_layout(title="Volcano Plot", xaxis_title="Logarithmic Fold Change (logFC)", yaxis_title="Adjusted P Value", clickmode='event+select')

        plot_json = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template("index.html", plot_json=plot_json)

    except Exception as e:
        return str(e), 500



@app.route('/boxplot/<gene_id>', methods=['GET'])
def boxplot(gene_id):
    df = read_data(r"data/NIHMS1635539-supplement-1635539_Sup_tab_4.xlsx", "S4A values")

    gene_df = df[df['EntrezGeneSymbol'] == gene_id]

    young_dons = [col for col in gene_df.columns if 'YD' in col]
    old_dons = [col for col in gene_df.columns if 'OD' in col]

    young_dons_data = gene_df[young_dons].values.flatten()
    old_dons_data = gene_df[old_dons].values.flatten()

    plot = make_subplots(rows=1, cols=1)

    plot.add_trace(go.Box(y = young_dons_data, name = "Young Donors", boxmean='sd', marker = dict(color = 'pink'), jitter = 0.3, pointpos= -1.8), row=1, col=1)
    plot.add_trace(go.Box(y = old_dons_data, name = "Old Donors", boxmean='sd', marker = dict(color = 'purple'), jitter = 0.3, pointpos= -1.8), row=1, col=1)

    plot.update_layout(title=f"Protein Concentration Comparison for Gene {gene_id}", xaxis_title="Donor Age", yaxis_title = "Protein concentration", showlegend= True)

    return plot.to_json()

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

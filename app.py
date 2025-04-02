import io

import matplotlib
import numpy as np
import pandas as pd
from flask import Flask, render_template, send_file
from matplotlib import pyplot as plt

matplotlib.use('Agg')

app = Flask(__name__)

def read_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=2)
    df.columns = df.columns.str.strip()
    return df

@app.route('/plot')
def create_plot():
    df = read_data(r"data/NIHMS1635539-supplement-1635539_Sup_tab_4.xlsx", "S4B limma results")
    plt.figure(figsize=(20,12))
    plt.scatter(df['logFC'], -np.log10(df['adj.P.Val']), c = -np.log10(df['adj.P.Val']), cmap='gist_rainbow', alpha=0.7)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    return send_file(buffer, mimetype='image/png')
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


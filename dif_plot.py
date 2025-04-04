try:
    df = read_data(r"data/NIHMS1635539-supplement-1635539_Sup_tab_4.xlsx", "S4B limma results")
    print("DataFrame Loaded:", df.columns)  # Verify column names

    # Check if necessary columns exist
    if 'logFC' not in df.columns or 'adj.P.Val' not in df.columns or 'EntrezGeneSymbol' not in df.columns:
        return "Required columns are missing in the sheet!", 500

    # Create the plot
    plot = go.Figure()
    plot.add_trace(go.Scatter(
        x=df['logFC'],
        y=-np.log10(df['adj.P.Val']),
        mode='markers',
        marker=dict(
            color=-np.log10(df['adj.P.Val']),
            colorscale='Viridis',
            size=10,
            opacity=0.7
        ),
        text=df['EntrezGeneSymbol'],
        hoverinfo='text',
        name="Volcano Plot"
    ))

    plot.update_layout(
        title="Volcano Plot",
        xaxis_title="Log Fold Change (logFC)",
        yaxis_title="-log10(Adjusted P Value)",
        clickmode='event+select'
    )

    # Serialize plot to JSON
    plot_json = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)
    print("Generated plot_json:", plot_json)  # Check JSON output

    return render_template('index.html', plot_json=plot_json)

except Exception as e:
    print("Error encountered:", str(e))
    return f"Error: {str(e)}", 500
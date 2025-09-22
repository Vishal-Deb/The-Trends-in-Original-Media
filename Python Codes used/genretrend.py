import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Load CSVs ---
df_counts = pd.read_csv("origin_genre_counts.csv")   # columns: origin, genre, count
df_trends = pd.read_csv("genre_year_trends.csv")     # columns: year, origin, genre, count

# --- 1. Genre Comparison by Origin (Percentage Bar Chart) ---
# Calculate percentages
df_counts["total"] = df_counts.groupby("origin")["count"].transform("sum")
df_counts["percentage"] = (df_counts["count"] / df_counts["total"]) * 100

# Create a dropdown menu for genre selection
genres = df_counts["genre"].unique()

fig1 = go.Figure()

# Add traces for each genre (initially hidden except the first one)
for i, g in enumerate(genres):
    subset = df_counts[df_counts["genre"] == g]
    fig1.add_trace(go.Bar(
        x=subset["origin"],
        y=subset["percentage"],
        name=g,
        visible=(i == 0)  # only show first by default
    ))

# Dropdown menu
buttons = []
for i, g in enumerate(genres):
    visible = [False] * len(genres)
    visible[i] = True
    buttons.append(dict(
        label=g,
        method="update",
        args=[{"visible": visible},
              {"title": f"Percentage of '{g}' by Origin"}]
    ))

fig1.update_layout(
    updatemenus=[dict(
        active=0,
        buttons=buttons,
        x=1.2,
        y=1.1
    )],
    title=f"Percentage of '{genres[0]}' by Origin",
    xaxis_title="Origin",
    yaxis_title="Percentage (%)",
    showlegend=False
)

fig1.write_html("genre_comparison_by_origin.html")
print("Saved: genre_comparison_by_origin.html")

# --- 2. Genre Trends by Year for Each Origin (Stacked Column Chart) ---
df_trends["total"] = df_trends.groupby(["year", "origin"])["count"].transform("sum")
df_trends["percentage"] = (df_trends["count"] / df_trends["total"]) * 100

genres2 = df_trends["genre"].unique()
origins = df_trends["origin"].unique()

fig2 = go.Figure()

# Add traces for each genre × origin, only first genre visible
for i, g in enumerate(genres2):
    subset = df_trends[df_trends["genre"] == g]
    for origin in origins:
        sub2 = subset[subset["origin"] == origin]
        fig2.add_trace(go.Bar(
            x=sub2["year"],
            y=sub2["percentage"],
            name=origin,
            visible=(i == 0)
        ))

# Dropdown for genres
buttons2 = []
for i, g in enumerate(genres2):
    visible = [False] * (len(genres2) * len(origins))
    start = i * len(origins)
    end = start + len(origins)
    for j in range(start, end):
        visible[j] = True
    buttons2.append(dict(
        label=g,
        method="update",
        args=[{"visible": visible},
              {"title": f"Yearly Trends of '{g}' by Origin"}]
    ))

fig2.update_layout(
    barmode="stack",
    updatemenus=[dict(
        active=0,
        buttons=buttons2,
        x=1.2,
        y=1.1
    )],
    title=f"Yearly Trends of '{genres2[0]}' by Origin",
    xaxis_title="Year",
    yaxis_title="Percentage (%)"
)

fig2.write_html("genre_trends_by_year.html")
print("Saved: genre_trends_by_year.html")
import pandas as pd
import plotly.graph_objects as go

# --- Load the CSV ---
df = pd.read_csv("genre_origin_year_metrics.csv", encoding="utf-8-sig")
df.columns = df.columns.str.strip()  # clean up headers just in case

# ======================================================
# Preprocess
# ======================================================
# For bar charts, we collapse over years
df_grouped = df.groupby(["Origin", "Genre"], as_index=False).agg({
    "Avg_Rating": "mean",
    "Avg_Votes": "sum",
    "Weighted_Rating": "mean"
})

# Calculate % of votes within each origin
df_grouped["Total_Votes"] = df_grouped.groupby("Origin")["Avg_Votes"].transform("sum")
df_grouped["Votes_Percentage"] = (df_grouped["Avg_Votes"] / df_grouped["Total_Votes"]) * 100

genres = df_grouped["Genre"].unique()
origins = df_grouped["Origin"].unique()

# ======================================================
# 1. Avg Rating by Origin (dropdown for Genre)
# ======================================================
fig1 = go.Figure()
for i, g in enumerate(genres):
    subset = df_grouped[df_grouped["Genre"] == g]
    fig1.add_trace(go.Bar(
        x=subset["Origin"],
        y=subset["Avg_Rating"],
        name=g,
        visible=(i == 0)
    ))

buttons1 = []
for i, g in enumerate(genres):
    visible = [False] * len(genres)
    visible[i] = True
    buttons1.append(dict(
        label=g,
        method="update",
        args=[{"visible": visible},
              {"title": f"Average Rating by Origin — Genre: {g}"}]
    ))

fig1.update_layout(
    updatemenus=[dict(active=0, buttons=buttons1, x=1.2, y=1.1)],
    title=f"Average Rating by Origin — Genre: {genres[0]}",
    xaxis_title="Origin",
    yaxis_title="Average Rating",
    showlegend=False
)
fig1.write_html("avg_rating_by_origin.html")

# ======================================================
# 2. Avg Votes % by Origin (dropdown for Genre)
# ======================================================
fig2 = go.Figure()
for i, g in enumerate(genres):
    subset = df_grouped[df_grouped["Genre"] == g]
    fig2.add_trace(go.Bar(
        x=subset["Origin"],
        y=subset["Votes_Percentage"],
        name=g,
        visible=(i == 0)
    ))

buttons2 = []
for i, g in enumerate(genres):
    visible = [False] * len(genres)
    visible[i] = True
    buttons2.append(dict(
        label=g,
        method="update",
        args=[{"visible": visible},
              {"title": f"Votes % by Origin — Genre: {g}"}]
    ))

fig2.update_layout(
    updatemenus=[dict(active=0, buttons=buttons2, x=1.2, y=1.1)],
    title=f"Votes % by Origin — Genre: {genres[0]}",
    xaxis_title="Origin",
    yaxis_title="Votes Percentage (%)",
    showlegend=False
)
fig2.write_html("votes_percentage_by_origin.html")

# ======================================================
# 3. Weighted Rating by Origin (dropdown for Genre)
# ======================================================
fig3 = go.Figure()
for i, g in enumerate(genres):
    subset = df_grouped[df_grouped["Genre"] == g]
    fig3.add_trace(go.Bar(
        x=subset["Origin"],
        y=subset["Weighted_Rating"],
        name=g,
        visible=(i == 0)
    ))

buttons3 = []
for i, g in enumerate(genres):
    visible = [False] * len(genres)
    visible[i] = True
    buttons3.append(dict(
        label=g,
        method="update",
        args=[{"visible": visible},
              {"title": f"Weighted Rating by Origin — Genre: {g}"}]
    ))

fig3.update_layout(
    updatemenus=[dict(active=0, buttons=buttons3, x=1.2, y=1.1)],
    title=f"Weighted Rating by Origin — Genre: {genres[0]}",
    xaxis_title="Origin",
    yaxis_title="Weighted Rating",
    showlegend=False
)
fig3.write_html("weighted_rating_by_origin.html")

# ======================================================
# 4. Weighted Rating Trends Over Years (dropdown for Genre, Origins as lines)
# ======================================================
fig4 = go.Figure()

for i, g in enumerate(genres):
    subset = df[df["Genre"] == g].groupby(["Year", "Origin"], as_index=False)["Weighted_Rating"].mean()
    subset = subset.sort_values("Year")  # make sure years go forward
    for origin in origins:
        sub2 = subset[subset["Origin"] == origin]
        fig4.add_trace(go.Scatter(
            x=sub2["Year"],
            y=sub2["Weighted_Rating"],
            mode="lines+markers",
            name=origin,
            visible=(i == 0)
        ))

buttons4 = []
for i, g in enumerate(genres):
    visible = [False] * (len(genres) * len(origins))
    start = i * len(origins)
    end = start + len(origins)
    for j in range(start, end):
        visible[j] = True
    buttons4.append(dict(
        label=g,
        method="update",
        args=[{"visible": visible},
              {"title": f"Weighted Rating Trends Over Years — Genre: {g}"}]
    ))

fig4.update_layout(
    updatemenus=[dict(active=0, buttons=buttons4, x=1.2, y=1.1)],
    title=f"Weighted Rating Trends Over Years — Genre: {genres[0]}",
    xaxis_title="Year",
    yaxis_title="Weighted Rating"
)

fig4.write_html("weighted_rating_trends.html")

print("All plots generated successfully!")



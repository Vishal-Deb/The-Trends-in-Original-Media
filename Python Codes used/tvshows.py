import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("tvshows_combined.csv", encoding="utf-8-sig")
df.columns = df.columns.str.strip()

# ===============================
# Weighted Rating Calculation
# ===============================
m = 1000  # minimum votes
C = df["rating"].mean()

df["Weighted_Rating"] = (df["votes"] / (df["votes"] + m)) * df["rating"] + (m / (df["votes"] + m)) * C

# Prepare unique lists
genres = df["genre"].dropna().unique()
statuses = df["status"].dropna().unique()
origins = df["origin"].unique()

# ===============================
# 1. Bar Chart: Average Rating
# ===============================
fig1 = go.Figure()

for g in genres:
    for s in statuses:
        subset = df[(df["genre"] == g) & (df["status"] == s)]
        grouped = subset.groupby("origin", as_index=False)["rating"].mean()
        fig1.add_trace(go.Bar(
            x=grouped["origin"],
            y=grouped["rating"],
            name=f"{g} | {s}",
            visible=False
        ))

# Dropdown menu logic
buttons1 = []
trace_count = 0
for g in genres:
    for s in statuses:
        visible = [False] * (len(genres) * len(statuses))
        visible[trace_count] = True
        buttons1.append(dict(
            label=f"{g} | {s}",
            method="update",
            args=[{"visible": visible},
                  {"title": f"Average Rating by Origin — {g}, {s}"}]
        ))
        trace_count += 1

fig1.update_layout(
    updatemenus=[dict(active=0, buttons=buttons1, x=1.2, y=1.1)],
    title="Average Rating by Origin",
    xaxis_title="Origin",
    yaxis_title="Average Rating",
    showlegend=False
)
fig1.data[0].visible = True
fig1.write_html("avg_rating_bar.html")

# ===============================
# 2. Bar Chart: Weighted Rating
# ===============================
fig2 = go.Figure()

for g in genres:
    for s in statuses:
        subset = df[(df["genre"] == g) & (df["status"] == s)]
        grouped = subset.groupby("origin", as_index=False)["Weighted_Rating"].mean()
        fig2.add_trace(go.Bar(
            x=grouped["origin"],
            y=grouped["Weighted_Rating"],
            name=f"{g} | {s}",
            visible=False
        ))

buttons2 = []
trace_count = 0
for g in genres:
    for s in statuses:
        visible = [False] * (len(genres) * len(statuses))
        visible[trace_count] = True
        buttons2.append(dict(
            label=f"{g} | {s}",
            method="update",
            args=[{"visible": visible},
                  {"title": f"Weighted Rating by Origin — {g}, {s}"}]
        ))
        trace_count += 1

fig2.update_layout(
    updatemenus=[dict(active=0, buttons=buttons2, x=1.2, y=1.1)],
    title="Weighted Rating by Origin",
    xaxis_title="Origin",
    yaxis_title="Weighted Rating",
    showlegend=False
)
fig2.data[0].visible = True
fig2.write_html("weighted_rating_bar.html")

# ===============================
# Clustered Column Chart: Likelihood of Cancelled/Concluded by Rating Range
# ===============================
bins = [0, 6, 7, 8, 9, 10]
labels = ["<6", "6-7", "7-8", "8-9", "9-10"]
df["Rating_Range"] = pd.cut(df["rating"], bins=bins, labels=labels, include_lowest=True)

# Make Rating_Range categorical with all labels
df["Rating_Range"] = df["Rating_Range"].cat.set_categories(labels)

fig5 = go.Figure()

for g in genres:
    for s in statuses:
        subset = df[(df["genre"] == g) & (df["status"] == s)]
        
        # Total shows per Origin and Rating Range
        total_per_bin = df[df["genre"] == g].groupby(["origin", "Rating_Range"])["imdb_id"].count().rename("Total_Shows").reset_index()
        # Shows with given status per Origin and Rating Range
        status_per_bin = subset.groupby(["origin", "Rating_Range"])["imdb_id"].count().rename("Status_Shows").reset_index()
        
        # Merge and calculate percentage
        merged = total_per_bin.merge(status_per_bin, on=["origin", "Rating_Range"], how="left")
        merged["Status_Shows"] = merged["Status_Shows"].fillna(0)  # only fill numeric
        merged["Percentage"] = (merged["Status_Shows"] / merged["Total_Shows"]) * 100
        
        for origin in origins:
            sub2 = merged[merged["origin"] == origin]
            fig5.add_trace(go.Bar(
                x=sub2["Rating_Range"],
                y=sub2["Percentage"],
                name=origin,
                visible=False
            ))

# Dropdown buttons for Genre + Status
buttons5 = []
trace_count = 0
for g in genres:
    for s in statuses:
        visible = [False] * (len(genres) * len(statuses) * len(origins))
        start = trace_count
        end = trace_count + len(origins)
        for j in range(start, end):
            visible[j] = True
        buttons5.append(dict(
            label=f"{g} | {s}",
            method="update",
            args=[{"visible": visible},
                  {"title": f"Percentage of Shows ({s}) by Rating Range — Genre: {g}"}]
        ))
        trace_count += len(origins)

fig5.update_layout(
    updatemenus=[dict(active=0, buttons=buttons5, x=1.2, y=1.1)],
    barmode="group",
    title="Percentage of Shows by Rating Range and Origin",
    xaxis_title="Rating Range",
    yaxis_title="Percentage of Shows (%)"
)
fig5.data[0].visible = True

fig5.write_html("status_percentage_by_rating.html")
print("✅ Clustered column chart saved: status_percentage_by_rating.html")

import pandas as pd
import plotly.graph_objects as go

# Load CSV
df = pd.read_csv(r"C:\Users\visha\OneDrive\Desktop\Project\origin_type_counts.csv")

# Get unique types and origins
types = df['type'].unique()
origins = df['origin'].unique()

# -----------------------------
# 1. Dropdown by type (show counts across origins)
# -----------------------------
fig_type = go.Figure()

for t in types:
    data = df[df['type'] == t]
    fig_type.add_trace(go.Pie(
        labels=data['origin'],
        values=data['count'],
        name=t,
        visible=(t == types[0])  # show first type initially
    ))

buttons_type = [
    dict(
        label=t,
        method="update",
        args=[{"visible": [trace.name == t for trace in fig_type.data]},
              {"title": f"Content Counts Across Origins for Type: {t}"}]
    )
    for t in types
]

fig_type.update_layout(
    updatemenus=[dict(active=0, buttons=buttons_type, x=0.1, y=1.2)],
    title=f"Content Counts Across Origins for Type: {types[0]}"
)

fig_type.write_html(r"C:\Users\visha\OneDrive\Desktop\Project\pie_by_type.html")
print("Dropdown pie chart by type saved as pie_by_type.html")

# -----------------------------
# 2. Dropdown by origin (show type breakdown within origin)
# -----------------------------
fig_origin = go.Figure()

for o in origins:
    data = df[df['origin'] == o]
    fig_origin.add_trace(go.Pie(
        labels=data['type'],
        values=data['count'],
        name=o,
        visible=(o == origins[0])  # show first origin initially
    ))

buttons_origin = [
    dict(
        label=o,
        method="update",
        args=[{"visible": [trace.name == o for trace in fig_origin.data]},
              {"title": f"Type Breakdown for Origin: {o}"}]
    )
    for o in origins
]

fig_origin.update_layout(
    updatemenus=[dict(active=0, buttons=buttons_origin, x=0.1, y=1.2)],
    title=f"Type Breakdown for Origin: {origins[0]}"
)

fig_origin.write_html(r"C:\Users\visha\OneDrive\Desktop\Project\pie_by_origin.html")
print("Dropdown pie chart by origin saved as pie_by_origin.html")

# -----------------------------
# 3. Total content by origin (simple pie)
# -----------------------------
origin_totals = df.groupby("origin", as_index=False)["count"].sum()

fig_total = go.Figure(go.Pie(
    labels=origin_totals['origin'],
    values=origin_totals['count'],
    title="Total Content by Origin"
))

fig_total.write_html(r"C:\Users\visha\OneDrive\Desktop\Project\pie_total_origin.html")
print("Total content pie chart saved as pie_total_origin.html")


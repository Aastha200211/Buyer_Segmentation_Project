import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Buyer Segmentation Dashboard",
    page_icon="🏠",
    layout="wide"
)

# ---------------- BACKGROUND IMAGE ----------------

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg = get_base64("background.png")

page_bg = f"""
<style>

/* ---------------- BACKGROUND ---------------- */

.stApp {{
    background-image: url("data:image/png;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* ---------------- HEADER ---------------- */

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

/* ---------------- SIDEBAR ---------------- */

[data-testid="stSidebar"] {{
    background: rgba(40,40,40,0.92);
}}

/* Sidebar Heading & Labels */

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p {{
    color: white !important;
    font-weight: bold;
}}

/* ---------------- SELECT BOX ---------------- */

/* White select box */

.stSelectbox div[data-baseweb="select"] > div {{
    background-color: white !important;
    color: black !important;
    border-radius: 8px;
}}

/* Selected text (Australia, India, etc.) */

.stSelectbox div[data-baseweb="select"] span {{
    color: black !important;
}}

/* Search text while typing */

.stSelectbox input {{
    color: black !important;
}}

/* Dropdown menu */

div[role="listbox"] {{
    background: white !important;
}}

/* Dropdown options */

div[role="option"] {{
    color: black !important;
    background: white !important;
}}

/* Hover effect */

div[role="option"]:hover {{
    background: #EAEAEA !important;
}}

/* ---------------- KPI CARDS ---------------- */

div[data-testid="metric-container"] {{
    background: rgba(255,255,255,0.90);
    padding:15px;
    border-radius:15px;
    box-shadow:2px 2px 12px rgba(0,0,0,0.30);
}}

/* ---------------- HEADINGS ---------------- */

h1,h2,h3,h4,h5 {{
    color:black;
}}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------

df = pd.read_csv("buyer_segmentation_final.csv")

# ---------------- TITLE ----------------

st.title("🏠 Machine Learning Based Buyer Segmentation")
st.markdown("### Investment Profiling for Real Estate Market Intelligence")


# ---------------- SIDEBAR ----------------

st.sidebar.title("Filters")

country = st.sidebar.selectbox(
    "Country",
    ["All"] + sorted(df["country"].unique())
)

region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(df["region"].unique())
)

client = st.sidebar.selectbox(
    "Client Type",
    ["All"] + sorted(df["client_type"].unique())
)

# ---------------- FILTER ----------------

filtered_df = df.copy()

if country != "All":
    filtered_df = filtered_df[filtered_df["country"] == country]

if region != "All":filtered_df = filtered_df[filtered_df["region"] == region]

if client != "All":filtered_df = filtered_df[filtered_df["client_type"] == client]

display_df = filtered_df.copy()

display_df["sale_price"] = display_df["sale_price"].apply(
    lambda x: f"₹{x:,.0f}"
)
# ---------------- KPIs ----------------

st.subheader("Dashboard Overview")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Total Buyers",
    len(filtered_df)
)

c2.metric(
    "Countries",
    filtered_df["country"].nunique()
)

c3.metric(
    "Regions",
    filtered_df["region"].nunique()
)

c4.metric(
    "Buyer Segments",
    filtered_df["Buyer_Segment"].nunique()
)

# ---------------- CHARTS ----------------

left,right = st.columns(2)

with left:

    st.subheader("Buyer Segments")

    fig,ax=plt.subplots(figsize=(7,5))

    filtered_df["Buyer_Segment"].value_counts().plot(
        kind="bar",
        color="steelblue",
        ax=ax
    )

    plt.xticks(rotation=20)

    st.pyplot(fig)

with right:

    st.subheader("Average Sale Price")

    fig,ax=plt.subplots(figsize=(7,5))

    filtered_df.groupby("Buyer_Segment")["sale_price"].mean().plot(
        kind="bar",
        color="green",
        ax=ax
    )

    plt.xticks(rotation=20)

    st.pyplot(fig)

# ---------------- SECOND ROW ----------------

left,right = st.columns(2)

with left:

    st.subheader("Average Buyer Age")

    fig,ax=plt.subplots(figsize=(7,5))

    filtered_df.groupby("Buyer_Segment")["Age"].mean().plot(
        kind="bar",
        color="orange",
        ax=ax
    )

    plt.xticks(rotation=20)

    st.pyplot(fig)

with right:

    st.subheader("Satisfaction Score")

    fig,ax=plt.subplots(figsize=(7,5))

    sns.boxplot(
        data=filtered_df,
        x="Buyer_Segment",
        y="satisfaction_score",
        ax=ax
    )

    plt.xticks(rotation=20)

    st.pyplot(fig)

# ---------------- SCATTER ----------------

st.subheader("Buyer Analysis")

fig,ax=plt.subplots(figsize=(10,6))

sns.scatterplot(
    data=filtered_df,
    x="Age",
    y="sale_price",
    hue="Buyer_Segment",
    s=80,
    ax=ax
)

st.pyplot(fig)

# ---------------- TABLE ----------------

st.subheader("Buyer Details")

st.dataframe(display_df)

# ---------------- DOWNLOAD BUTTON ----------------

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="Buyer_Segmentation.csv",
    mime="text/csv"
)

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""
### Developed using

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Machine Learning (K-Means Clustering)
""")
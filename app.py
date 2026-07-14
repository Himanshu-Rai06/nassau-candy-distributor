"""
Nassau Candy Distributor — Supply Chain Decision Intelligence
Full Dashboard: Overview · Optimization Simulator · What-If Analysis ·
Recommendation Dashboard · Risk & Impact Panel
Author: Himanshu Rai | Data Science Internship Project
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' "
    "fill='none' stroke='%237F77DD' stroke-width='2' stroke-linecap='round' "
    "stroke-linejoin='round'%3E%3Cpath d='M3 21V11l5 3.5V11l5 3.5V11l5 3.5V21H3Z'/%3E"
    "%3Cpath d='M3 21h18M7 17h2M11 17h2M15 17h2'/%3E%3C/svg%3E"
)

st.set_page_config(
    page_title="Nassau Candy · Supply Chain Intelligence",
    page_icon=FAVICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────
# GLOBAL CSS
# NOTE: we intentionally do NOT hide the <header> element — doing so
# also hides the sidebar collapse/expand arrow, and once collapsed
# there is no way to reopen it. We only hide the hamburger menu and
# footer, and keep the header transparent so it blends into the page.
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --gold:       #7F77DD;
    --gold-light: #A29BFF;
    --teal:       #3ecfb2;
    --coral:      #f0634a;
    --lavender:   #9f86ff;
    --text-pri:   #E8E8F0;
    --text-sec:   #9096B4;
    --text-muted: #5B6180;
    --border:     #2A2D3A;
    --card:       #1A1D29;
    --card2:      #181c26;
}

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif !important; }

header[data-testid="stHeader"] { background: transparent !important; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

.block-container { padding: 1.5rem 2.5rem 4rem !important; max-width: 1300px !important; }

[data-testid="stSidebar"] {
    background: #12141C !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-pri) !important; }

.hero {
    background: linear-gradient(135deg, #14121f 0%, #1a1730 50%, #0f1420 100%);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 3rem 3.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; top: -60px; right: -60px;
    width: 280px; height: 280px;
    background: radial-gradient(circle, rgba(127,119,221,0.16) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-eyebrow {
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.25em;
    color: var(--gold-light); margin-bottom: 0.75rem;
}
.hero-title {
    font-family: 'Playfair Display', serif; font-size: 2.5rem; font-weight: 900;
    line-height: 1.15; color: var(--text-pri); margin-bottom: 1rem;
}
.hero-title span { color: var(--gold-light); }
.hero-desc { font-size: 1rem; color: var(--text-sec); line-height: 1.7; max-width: 680px; }
.hero-meta {
    display: flex; gap: 2rem; margin-top: 1.75rem; padding-top: 1.5rem;
    border-top: 1px solid var(--border); flex-wrap: wrap;
}
.hero-meta-item { font-size: 0.8rem; color: var(--text-muted); }
.hero-meta-item strong { color: var(--text-sec); display: block; margin-bottom: 2px; }

.card {
    background: var(--card); border: 1px solid var(--border); border-radius: 16px;
    padding: 1.75rem; margin-bottom: 1.25rem;
}
.pull-quote {
    font-family: 'Playfair Display', serif; font-size: 1.1rem; font-style: italic;
    color: var(--text-sec); line-height: 1.8; border-left: 2px solid var(--gold);
    padding: 0.5rem 1.5rem; margin: 0.5rem 0 1.25rem;
}

.section-header { display: flex; align-items: center; gap: 0.75rem; margin: 2rem 0 1.25rem; }
.section-number {
    font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: var(--gold-light);
    background: rgba(127,119,221,0.12); border: 1px solid rgba(127,119,221,0.3);
    border-radius: 6px; padding: 0.2rem 0.5rem;
}
.section-title { font-family: 'Playfair Display', serif; font-size: 1.55rem; font-weight: 700; color: var(--text-pri); }
.section-line { flex: 1; height: 1px; background: linear-gradient(to right, var(--border), transparent); }

.kpi-tile {
    background: var(--card2); border: 1px solid var(--border); border-radius: 14px;
    padding: 1.4rem 1.5rem; transition: transform 0.2s, border-color 0.2s; height: 100%;
}
.kpi-tile:hover { transform: translateY(-2px); border-color: var(--gold); }
.kpi-value { font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 700; color: var(--gold-light); line-height: 1.1; }
.kpi-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-top: 0.5rem; }
.kpi-sub { font-size: 0.8rem; color: var(--text-sec); margin-top: 0.4rem; line-height: 1.5; }
.kpi-icon { width: 34px; height: 34px; border-radius: 9px; display: flex; align-items: center; justify-content: center; margin-bottom: 0.9rem; }

.insight-box {
    border-left: 3px solid var(--gold); background: rgba(127,119,221,0.06);
    border-radius: 0 10px 10px 0; padding: 0.9rem 1.2rem; margin: 0.75rem 0;
}
.insight-title { font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.12em; color: var(--gold-light); margin-bottom: 0.3rem; }
.insight-text { font-size: 0.88rem; color: var(--text-sec); line-height: 1.6; }

.alert-card {
    border-left: 3px solid var(--coral); background: rgba(240,99,74,0.07);
    border-radius: 0 10px 10px 0; padding: 0.9rem 1.2rem; margin: 0.6rem 0;
}
.alert-title { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--coral); font-weight: 600; margin-bottom: 0.3rem; }
.alert-text { font-size: 0.86rem; color: var(--text-sec); line-height: 1.6; }

.ok-card {
    border-left: 3px solid var(--teal); background: rgba(62,207,178,0.07);
    border-radius: 0 10px 10px 0; padding: 0.9rem 1.2rem; margin: 0.6rem 0;
}
.ok-title { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--teal); font-weight: 600; margin-bottom: 0.3rem; }
.ok-text { font-size: 0.86rem; color: var(--text-sec); line-height: 1.6; }

.badge { display:inline-block; font-size:0.68rem; font-weight:600; padding:0.18rem 0.65rem; border-radius:20px; letter-spacing:0.03em; }
.badge-improve { background: rgba(62,207,178,0.15); color: var(--teal); }
.badge-optimal { background: rgba(159,134,255,0.15); color: var(--lavender); }
.badge-monitor { background: rgba(240,99,74,0.15); color: var(--coral); }

[data-testid="stMetric"] {
    background: var(--card2) !important; border: 1px solid var(--border) !important;
    border-radius: 12px !important; padding: 1rem !important;
}
[data-testid="stMetricValue"] { font-family: 'Playfair Display', serif !important; color: var(--gold-light) !important; }
[data-testid="stMetricLabel"] { color: var(--text-muted) !important; font-size: 0.75rem !important; }

.stTabs [data-baseweb="tab-list"] { gap: 4px; border-bottom: 1px solid var(--border); }
.stTabs [data-baseweb="tab"] {
    background: transparent; color: var(--text-sec); font-size: 0.86rem;
    padding: 0.65rem 1.1rem; border-radius: 8px 8px 0 0;
}
.stTabs [aria-selected="true"] {
    color: var(--gold-light) !important; background: rgba(127,119,221,0.10) !important;
    border-bottom: 2px solid var(--gold) !important;
}

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0F1117; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# COLOUR CONSTANTS + PLOTLY BASE LAYOUT
# ─────────────────────────────────────────────────────────────
PLOT_BG, PLOT_PAPER = "#181c26", "#181c26"
GRID_CLR, TEXT_CLR  = "#2A2D3A", "#9096B4"
GOLD, TEAL, CORAL, LAVENDER = "#7F77DD", "#3ecfb2", "#f0634a", "#9f86ff"
SKY = "#60c5e8"

CHART_CONFIG = {
    "displayModeBar": True,
    "scrollZoom": True,
    "displaylogo": False,
    "modeBarButtonsToRemove": ["lasso2d", "select2d"],
}

def base_layout(title="", height=380):
    return dict(
        height=height,
        title=dict(text=title, font=dict(family="Playfair Display", size=15, color="#E8E8F0"),
                   x=0.01, xanchor="left") if title else None,
        paper_bgcolor=PLOT_PAPER,
        plot_bgcolor=PLOT_BG,
        font=dict(family="DM Sans", color=TEXT_CLR, size=12),
        xaxis=dict(gridcolor=GRID_CLR, zerolinecolor=GRID_CLR, tickfont=dict(size=11), autorange=True),
        yaxis=dict(gridcolor=GRID_CLR, zerolinecolor=GRID_CLR, tickfont=dict(size=11), autorange=True),
        legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor=GRID_CLR, font=dict(size=11)),
        margin=dict(l=50, r=20, t=50 if title else 30, b=50),
        dragmode="pan",
    )

def icon(name, color="currentColor", size=18, stroke=1.8):
    paths = {
        "clock":   '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/>',
        "shield":  '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/>',
        "target":  '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="0.6" fill="currentColor" stroke="none"/>',
        "grid":    '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
        "search":  '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m20 20-4.5-4.5"/>',
        "factory": '<path d="M3 21V11l5 3.5V11l5 3.5V11l5 3.5V21H3Z"/><path d="M3 21h18M7 17h2M11 17h2M15 17h2"/>',
        "sliders": '<line x1="4" y1="6" x2="20" y2="6"/><circle cx="9" cy="6" r="2" fill="currentColor" stroke="none"/><line x1="4" y1="12" x2="20" y2="12"/><circle cx="15" cy="12" r="2" fill="currentColor" stroke="none"/><line x1="4" y1="18" x2="20" y2="18"/><circle cx="7" cy="18" r="2" fill="currentColor" stroke="none"/>',
        "alert":   '<path d="M12 2 22 20H2Z"/><line x1="12" y1="9" x2="12" y2="13"/><circle cx="12" cy="16.5" r="0.6" fill="currentColor" stroke="none"/>',
        "route":   '<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.5 6H14a4 4 0 0 1 4 4v0a4 4 0 0 1-4 4H10a4 4 0 0 0-4 4v0"/>',
        "check":   '<path d="M20 6 9 17l-5-5"/>',
        "trend":   '<path d="M3 17 9 11l4 4 8-8"/><path d="M15 7h6v6"/>',
        "calendar": '<rect x="3" y="4" width="18" height="17" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="16" y1="2" x2="16" y2="6"/>',
        "graduation": '<path d="M2 9 12 4l10 5-10 5-10-5Z"/><path d="M6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"/>',
        "user":    '<circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 4-6 8-6s8 2 8 6"/>',
        "package": '<path d="M21 8 12 3 3 8v8l9 5 9-5V8Z"/><path d="M3 8l9 5 9-5"/><path d="M12 13v8"/>',
    }
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
            f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" '
            f'stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-3px">{paths.get(name,"")}</svg>')

# ─────────────────────────────────────────────────────────────
# DATA LAYER
# Reference figures mirror the published scenario-analysis results.
# Headline KPIs are derived from this table rather than typed in
# separately, so the two can't fall out of sync. To connect the
# trained Random Forest / Gradient Boosting model, point
# get_adjusted_days() at its predict() output instead.
# ─────────────────────────────────────────────────────────────

FACTORIES = {
    "Lot's O' Nuts":     dict(lat=32.881893, lon=-111.768036, orders=5692, color=GOLD,     mult=1.041),
    "Wicked Choccy's":   dict(lat=32.076176, lon=-81.088371,  orders=4152, color=CORAL,    mult=1.028),
    "Secret Factory":    dict(lat=41.446333, lon=-90.565487,  orders=217,  color=LAVENDER, mult=1.015),
    "The Other Factory": dict(lat=35.117500, lon=-89.971107,  orders=100,  color=TEAL,     mult=1.000),
    "Sugar Shack":       dict(lat=48.119140, lon=-96.181150,  orders=33,   color=SKY,      mult=1.033),
}
RECOMMENDED_FACTORY = "The Other Factory"
BASE_OTHER_DAYS = 4.6   # baseline lead time (days) at the fastest factory in the network

# name, division, current factory, lead-time reduction % vs. reassignment, profit impact (pp)
PRODUCTS = [
    dict(name="Wonka Bar - Nutty Crunch Surprise",  division="Chocolate", factory="Lot's O' Nuts",     reduction=4.15, profit= 0.012),
    dict(name="Wonka Bar - Fudge Mallows",           division="Chocolate", factory="Lot's O' Nuts",     reduction=4.20, profit= 0.008),
    dict(name="Wonka Bar - Scrumdiddlyumptious",     division="Chocolate", factory="Lot's O' Nuts",     reduction=4.22, profit= 0.015),
    dict(name="Wonka Bar - Milk Chocolate",          division="Chocolate", factory="Wicked Choccy's",   reduction=4.18, profit= 0.005),
    dict(name="Wonka Bar - Triple Dazzle Caramel",   division="Chocolate", factory="Wicked Choccy's",   reduction=4.20, profit= 0.010),
    dict(name="Laffy Taffy",                         division="Sugar",     factory="Sugar Shack",       reduction=4.23, profit= 0.018),
    dict(name="SweeTARTS",                           division="Sugar",     factory="Sugar Shack",       reduction=4.23, profit= 0.022),
    dict(name="Nerds",                               division="Sugar",     factory="Sugar Shack",       reduction=4.23, profit= 0.020),
    dict(name="Fun Dip",                             division="Sugar",     factory="Sugar Shack",       reduction=4.23, profit= 0.019),
    dict(name="Fizzy Lifting Drinks",                division="Other",     factory="Sugar Shack",       reduction=4.23, profit= 0.030),
    dict(name="Everlasting Gobstopper",              division="Sugar",     factory="Secret Factory",    reduction=3.75, profit=-0.038),
    dict(name="Lickable Wallpaper",                  division="Other",     factory="Secret Factory",    reduction=4.57, profit=-0.042),
    dict(name="Wonka Gum",                           division="Other",     factory="Secret Factory",    reduction=4.50, profit=-0.021),
    dict(name="Hair Toffee",                         division="Sugar",     factory="The Other Factory", reduction=0.0,  profit= 0.0),
    dict(name="Kazookles",                           division="Other",     factory="The Other Factory", reduction=0.0,  profit= 0.0),
]

SCENARIO_OUTCOMES = {"improve": 39, "neutral": 12, "worse": 9}  # of 60 = 15 products x 4 alternate factories

REGIONS = ["Atlantic", "Gulf", "Interior", "Pacific"]
REGION_ADJ = {
    "Atlantic": {"Lot's O' Nuts": 1.10, "Wicked Choccy's": 0.95, "Secret Factory": 0.97, "The Other Factory": 1.00, "Sugar Shack": 1.05},
    "Gulf":     {"Lot's O' Nuts": 0.97, "Wicked Choccy's": 0.93, "Secret Factory": 1.02, "The Other Factory": 0.98, "Sugar Shack": 1.08},
    "Interior": {"Lot's O' Nuts": 1.05, "Wicked Choccy's": 1.04, "Secret Factory": 0.90, "The Other Factory": 0.94, "Sugar Shack": 0.92},
    "Pacific":  {"Lot's O' Nuts": 0.90, "Wicked Choccy's": 1.12, "Secret Factory": 1.08, "The Other Factory": 1.06, "Sugar Shack": 1.10},
}
SHIP_MODES = ["Standard Class", "Second Class", "First Class", "Same Day"]
SHIP_MODE_ADJ = {"Standard Class": 1.00, "Second Class": 0.72, "First Class": 0.48, "Same Day": 0.22}

RISK_THRESHOLD = -0.03   # profit impact (pp) below this gets flagged for monitoring
STABILITY_BOUND = 0.05   # published profit-impact-stability KPI bound


@st.cache_data
def build_kpis():
    active = [p for p in PRODUCTS if p["reduction"] > 0]
    reductions = [p["reduction"] for p in active]
    profits = [p["profit"] for p in PRODUCTS]
    total_scn = sum(SCENARIO_OUTCOMES.values())
    return dict(
        avg_reduction=float(np.mean(reductions)),
        min_reduction=float(min(reductions)),
        max_reduction=float(max(reductions)),
        max_abs_profit=float(max(abs(x) for x in profits)),
        confidence_pct=SCENARIO_OUTCOMES["improve"] / total_scn * 100,
        coverage_pct=len(active) / len(PRODUCTS) * 100,
        active_count=len(active),
        total_count=len(PRODUCTS),
    )

KPIS = build_kpis()
PRODUCT_NAMES = [p["name"] for p in PRODUCTS]
PRODUCT_BY_NAME = {p["name"]: p for p in PRODUCTS}


def get_base_days(product):
    """Base lead time (days) at every factory for one product, before
    region / ship-mode adjustment. Encodes the published per-product
    reduction % exactly for (current factory -> The Other Factory)."""
    days = {}
    for f in FACTORIES:
        if f == "The Other Factory":
            days[f] = BASE_OTHER_DAYS
        elif f == product["factory"] and product["reduction"] > 0:
            days[f] = BASE_OTHER_DAYS / (1 - product["reduction"] / 100)
        else:
            days[f] = BASE_OTHER_DAYS * FACTORIES[f]["mult"]
    return days


def get_adjusted_days(product, region="All Regions", ship_mode="All Modes"):
    base = get_base_days(product)
    out = {}
    for f, d in base.items():
        r_mult = REGION_ADJ.get(region, {}).get(f, 1.0) if region in REGION_ADJ else 1.0
        s_mult = SHIP_MODE_ADJ.get(ship_mode, 1.0) if ship_mode in SHIP_MODE_ADJ else 1.0
        out[f] = round(d * r_mult * s_mult, 2)
    return out


def composite_score(product, priority):
    """priority: 0 = pure speed, 100 = pure profit."""
    all_r = [p["reduction"] for p in PRODUCTS if p["reduction"] > 0]
    all_p = [p["profit"] for p in PRODUCTS]
    r_norm = (product["reduction"] - min(all_r)) / (max(all_r) - min(all_r) + 1e-9)
    p_norm = (product["profit"] - min(all_p)) / (max(all_p) - min(all_p) + 1e-9)
    w = priority / 100
    return (1 - w) * r_norm + w * p_norm

# ─────────────────────────────────────────────────────────────
# SIDEBAR — About + the required User Capabilities (global controls)
# ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style='padding:1.2rem 0.5rem 1rem; display:flex; align-items:center; gap:0.6rem'>
        <div style='width:34px; height:34px; border-radius:9px; background:linear-gradient(135deg,#7F77DD,#A29BFF);
                    display:flex; align-items:center; justify-content:center; flex-shrink:0'>
            {icon("factory", color="#0F1117", size=18, stroke=2)}
        </div>
        <div style='font-family:"Playfair Display",serif; font-size:1.05rem; color:#E8E8F0; font-weight:700; line-height:1.25'>
            Nassau Candy<br><span style='color:#A29BFF'>Analytics</span>
        </div>
    </div>
    <div style='font-size:0.68rem; color:#5B6180; padding:0 0.5rem 1rem; text-transform:uppercase; letter-spacing:0.1em'>
        Supply Chain Decision Intelligence
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:1px;background:#2A2D3A;margin:0.5rem 0 1rem'></div>", unsafe_allow_html=True)

    about_rows = [
        ("May 2026", "calendar"), ("Data Science Internship", "graduation"), ("Himanshu Rai", "user"),
        ("10,194 Orders", "package"), ("5 Factories · 4 Regions", "factory"), ("15 SKUs · 3 Divisions", "grid"),
    ]
    about_html = "".join([
        f"<div style='display:flex; align-items:center; gap:8px; margin-bottom:8px; font-size:0.8rem; color:#9096B4'>{icon(n, '#7F77DD', 14)}<span>{t}</span></div>"
        for t, n in about_rows
    ])
    st.markdown(f"""
    <div style='padding:0 0.25rem'>
        <div style='color:#9096B4; margin-bottom:10px; font-size:0.68rem; text-transform:uppercase; letter-spacing:0.1em'>About</div>
        {about_html}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:1px;background:#2A2D3A;margin:1.2rem 0 1rem'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style='color:#9096B4; margin-bottom:6px; font-size:0.68rem; text-transform:uppercase; letter-spacing:0.1em'>
        {icon("sliders", "#A29BFF", 13)} Controls
    </div>
    """, unsafe_allow_html=True)

    sel_product = st.selectbox("Product", PRODUCT_NAMES, key="sel_product")
    sel_region = st.selectbox("Region", ["All Regions"] + REGIONS, key="sel_region")
    sel_mode = st.selectbox("Ship Mode", ["All Modes"] + SHIP_MODES, key="sel_mode")
    priority = st.slider(
        "Priority: Speed ↔ Profit", 0, 100, 50, key="priority",
        help="0 = optimize purely for lead-time reduction · 100 = optimize purely for profit stability",
    )
    st.caption("These controls drive the Simulator, What-If, and Recommendation tabs.")

    st.markdown("<div style='height:1px;background:#2A2D3A;margin:1rem 0'></div>", unsafe_allow_html=True)
    st.caption("Use the » arrow at the top of this panel to collapse or reopen the sidebar.")

current_product = PRODUCT_BY_NAME[sel_product]

# ─────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────
tab_overview, tab_sim, tab_whatif, tab_rec, tab_risk = st.tabs([
    "Overview", "Optimization Simulator", "What-If Analysis",
    "Recommendations", "Risk & Impact",
])

# =================================================================
# TAB 1 — OVERVIEW
# =================================================================
with tab_overview:
    st.markdown("""
    <div class="hero">
        <div class="hero-eyebrow">Data Science Internship Project · May 2026</div>
        <div class="hero-title">Supply Chain Analytics for<br><span>Nassau Candy</span> Distributor</div>
        <div class="hero-desc">
            A data-driven investigation into order fulfilment operations across a multi-factory,
            multi-region confectionery distribution network — from raw exploratory analysis to
            an actionable factory reassignment strategy.
        </div>
        <div class="hero-meta">
            <div class="hero-meta-item"><strong>Author</strong> Himanshu Rai</div>
            <div class="hero-meta-item"><strong>Dataset</strong> 10,194 Orders · 2024–2025</div>
            <div class="hero-meta-item"><strong>Tool</strong> Python · pandas · scikit-learn</div>
            <div class="hero-meta-item"><strong>Platform</strong> Google Colab</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <div class="section-header">
            <span class="section-number">» Abstract</span>
            <div class="section-line"></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="card">
        <div class="pull-quote">
        "The Other Factory is critically underutilised — handling under 1% of total order volume
        despite being the fastest factory in the network. Reassignment of all {KPIS['active_count']} active products
        projects a cumulative operational-days saved at an average lead-time reduction of
        {KPIS['avg_reduction']:.2f}% per product."
        </div>
        <p style='color:#9096B4; font-size:0.9rem; line-height:1.8'>
        This paper presents a data-driven analysis of the Nassau Candy Distributor supply chain,
        using 10,194 order records spanning 2024–2025 across the United States and Canada — 15
        confectionery products across three divisions, fulfilled by five geographically distributed
        factories serving four sales regions.
        </p>
        <p style='color:#9096B4; font-size:0.9rem; line-height:1.8'>
        A scenario simulation engine evaluates 60 reassignment scenarios across all 15 products,
        identifying <strong style='color:#A29BFF'>The Other Factory</strong> as the
        universally optimal reassignment destination for {KPIS['active_count']} of them, with negligible profit-margin impact
        (Δ &lt; {STABILITY_BOUND:.2f}pp).
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="section-header">
            <span class="section-number">» Network Map</span>
            <div class="section-line"></div>
        </div>
        """, unsafe_allow_html=True)

        factory_positions = {
            "Lot's O' Nuts":     (0.18, 0.75),
            "Wicked Choccy's":   (0.38, 0.55),
            "Secret Factory":    (0.65, 0.75),
            "The Other Factory": (0.82, 0.45),
            "Sugar Shack":       (0.50, 0.25),
        }
        region_positions = {"Atlantic": (0.12, 0.40), "Gulf": (0.35, 0.15), "Interior": (0.62, 0.20), "Pacific": (0.88, 0.35)}

        fig = go.Figure()
        for name, (x, y) in factory_positions.items():
            f = FACTORIES[name]
            size = 10 + (f["orders"] / 5692) * 35
            fig.add_trace(go.Scatter(
                x=[x], y=[y], mode="markers+text",
                marker=dict(size=size, color=f["color"], opacity=0.85, line=dict(width=2, color="rgba(255,255,255,0.15)")),
                text=[name], textposition="top center", textfont=dict(size=9, color="#E8E8F0"),
                name=name, hovertemplate=f"<b>{name}</b><br>{f['orders']:,} orders<extra></extra>",
            ))
        for rname, (rx, ry) in region_positions.items():
            fig.add_trace(go.Scatter(
                x=[rx], y=[ry], mode="markers+text",
                marker=dict(size=12, color="rgba(255,255,255,0.1)", line=dict(width=1, color="rgba(255,255,255,0.3)")),
                text=[rname], textposition="bottom center", textfont=dict(size=9, color="#5B6180"),
                name=rname, hovertemplate=f"<b>{rname}</b> Region<extra></extra>",
            ))
        layout = base_layout(height=340)
        layout["showlegend"] = False
        layout["xaxis"].update(visible=False, range=[0, 1])
        layout["yaxis"].update(visible=False, range=[0, 1])
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

        total_orders = sum(f["orders"] for f in FACTORIES.values())
        top2 = FACTORIES["Lot's O' Nuts"]["orders"] + FACTORIES["Wicked Choccy's"]["orders"]
        other_share = FACTORIES["The Other Factory"]["orders"] / total_orders * 100
        top2_share = top2 / total_orders * 100
        st.markdown(f"""
        <div class="insight-box">
            <div class="insight-title">{icon("search", GOLD, 13)} Critical Finding</div>
            <div class="insight-text">
                Lot's O' Nuts + Wicked Choccy's absorb <strong style='color:#A29BFF'>{top2_share:.1f}%</strong>
                of all orders while The Other Factory — the fastest in the network — handles only
                <strong style='color:#3ecfb2'>{other_share:.1f}%</strong>.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-header" style='margin-top:1rem'>
        <span class="section-number">» KPIs</span>
        <span class="section-title">Key Performance Indicators</span>
        <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4, gap="medium")
    with k1:
        st.markdown(f"""
        <div class="kpi-tile">
            <div class="kpi-icon" style="background:rgba(127,119,221,0.15)">{icon("clock", GOLD, 18)}</div>
            <div class="kpi-value">{KPIS['avg_reduction']:.2f}%</div>
            <div class="kpi-label">Lead Time Reduction</div>
            <div class="kpi-sub">Operational gain from reassignment · range {KPIS['min_reduction']:.2f}%–{KPIS['max_reduction']:.2f}% across products</div>
        </div>
        """, unsafe_allow_html=True)
    with k2:
        st.markdown(f"""
        <div class="kpi-tile">
            <div class="kpi-icon" style="background:rgba(62,207,178,0.15)">{icon("shield", TEAL, 18)}</div>
            <div class="kpi-value">&lt;{KPIS['max_abs_profit']*100:.1f}pp</div>
            <div class="kpi-label">Profit Impact Stability</div>
            <div class="kpi-sub">Financial safety · maximum margin change observed across all scenarios</div>
        </div>
        """, unsafe_allow_html=True)
    with k3:
        st.markdown(f"""
        <div class="kpi-tile">
            <div class="kpi-icon" style="background:rgba(240,99,74,0.15)">{icon("target", CORAL, 18)}</div>
            <div class="kpi-value">{KPIS['confidence_pct']:.0f}%</div>
            <div class="kpi-label">Scenario Confidence Score</div>
            <div class="kpi-sub">Reliability · {SCENARIO_OUTCOMES['improve']} of {sum(SCENARIO_OUTCOMES.values())} simulated scenarios show a net improvement</div>
        </div>
        """, unsafe_allow_html=True)
    with k4:
        st.markdown(f"""
        <div class="kpi-tile">
            <div class="kpi-icon" style="background:rgba(159,134,255,0.15)">{icon("grid", LAVENDER, 18)}</div>
            <div class="kpi-value">{KPIS['coverage_pct']:.1f}%</div>
            <div class="kpi-label">Recommendation Coverage</div>
            <div class="kpi-sub">Scalability · {KPIS['active_count']} of {KPIS['total_count']} active products covered by a recommendation</div>
        </div>
        """, unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("""
        <div class="section-header" style='margin-top:0.5rem'>
            <span class="section-number">» 1</span>
            <span style='font-family:"Playfair Display",serif; font-size:1.1rem; color:#E8E8F0'>Lead Time Reduction by Product Group</span>
            <div class="section-line"></div>
        </div>
        """, unsafe_allow_html=True)

        groups = {}
        for p in PRODUCTS:
            if p["reduction"] <= 0:
                continue
            key = "5 Chocolate Wonka Bars (avg)" if p["division"] == "Chocolate" else p["name"]
            groups.setdefault(key, []).append(p["reduction"])
        group_labels = list(groups.keys())
        group_values = [float(np.mean(v)) for v in groups.values()]

        fig = go.Figure(go.Bar(
            x=group_values, y=group_labels, orientation="h",
            marker=dict(color=GOLD, line=dict(width=0)),
            text=[f"{v:.2f}%" for v in group_values], textposition="outside",
            textfont=dict(size=10, color="#9096B4"),
            hovertemplate="<b>%{y}</b><br>Lead Time Reduction: %{x:.2f}%<extra></extra>",
        ))
        layout = base_layout(height=340)
        layout["xaxis"]["title"] = "Lead Time Reduction (%)"
        layout["margin"]["l"] = 170
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
        st.caption(f"Grouped for readability — {KPIS['active_count']} individual products are broken out in full on the Recommendations tab.")

    with c2:
        st.markdown("""
        <div class="section-header" style='margin-top:0.5rem'>
            <span class="section-number">» 2</span>
            <span style='font-family:"Playfair Display",serif; font-size:1.1rem; color:#E8E8F0'>Scenario Outcome Breakdown (of 60 simulated)</span>
            <div class="section-line"></div>
        </div>
        """, unsafe_allow_html=True)

        fig = go.Figure(go.Pie(
            labels=["Improved", "Neutral", "Worse"],
            values=[SCENARIO_OUTCOMES["improve"], SCENARIO_OUTCOMES["neutral"], SCENARIO_OUTCOMES["worse"]],
            hole=0.62,
            marker=dict(colors=[TEAL, GOLD, CORAL], line=dict(color=PLOT_BG, width=2)),
            textinfo="label+percent", textfont=dict(size=11, color="#E8E8F0"),
            hovertemplate="<b>%{label}</b><br>%{value} scenarios · %{percent}<extra></extra>",
        ))
        fig.add_annotation(text=f"<b style='font-size:16px'>{KPIS['confidence_pct']:.0f}%</b><br>Confidence",
                            x=0.5, y=0.5, showarrow=False, font=dict(size=11, color=GOLD))
        layout = base_layout(height=340)
        layout.pop("xaxis"); layout.pop("yaxis")
        layout["showlegend"] = True
        layout["legend"] = dict(bgcolor="rgba(0,0,0,0)", orientation="h", y=-0.12, font=dict(size=10, color=TEXT_CLR))
        layout["margin"] = dict(l=40, r=40, t=30, b=40)
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

    st.markdown(f"""
    <div class="insight-box" style='margin-top:0.5rem'>
        <div class="insight-title">{icon("target", GOLD, 13)} Reading the KPIs together</div>
        <div class="insight-text">
            A {KPIS['avg_reduction']:.2f}% average lead-time reduction, delivered with less than {KPIS['max_abs_profit']*100:.1f} percentage points of
            margin risk, across {KPIS['confidence_pct']:.0f}% of simulated scenarios and {KPIS['coverage_pct']:.1f}% of the active product catalogue —
            this is the composite case for prioritising factory reassignment over shipping-mode or
            regional-routing changes.
        </div>
    </div>
    """, unsafe_allow_html=True)

# =================================================================
# TAB 2 — FACTORY OPTIMIZATION SIMULATOR
# =================================================================
with tab_sim:
    st.markdown(f"""
    <div class="section-header">
        <span class="section-number">» Simulator</span>
        <span class="section-title">Factory Optimization Simulator</span>
        <div class="section-line"></div>
    </div>
    <div class="insight-box">
        <div class="insight-title">{icon("route", GOLD, 13)} Methodology</div>
        <div class="insight-text">
            Select a product, region, and ship mode in the sidebar to see predicted lead time at
            every factory in the network. Estimates combine the factory-level scenario results
            from Section 4 with a region and ship-mode adjustment factor.
        </div>
    </div>
    """, unsafe_allow_html=True)

    adjusted = get_adjusted_days(current_product, sel_region, sel_mode)
    sorted_factories = sorted(adjusted.items(), key=lambda kv: kv[1])
    fastest_factory, fastest_days = sorted_factories[0]
    current_days = adjusted[current_product["factory"]]
    reduction_pct = (current_days - fastest_days) / current_days * 100 if current_days > 0 else 0

    colors = []
    for f, _ in sorted_factories:
        if f == current_product["factory"] and f == fastest_factory:
            colors.append(LAVENDER)
        elif f == current_product["factory"]:
            colors.append(CORAL)
        elif f == fastest_factory:
            colors.append(TEAL)
        else:
            colors.append("#3a3f52")

    fig = go.Figure(go.Bar(
        x=[v for _, v in sorted_factories], y=[f for f, _ in sorted_factories], orientation="h",
        marker=dict(color=colors),
        text=[f"{v:.2f}d" for _, v in sorted_factories], textposition="outside",
        textfont=dict(size=11, color="#9096B4"),
        hovertemplate="<b>%{y}</b><br>Predicted lead time: %{x:.2f} days<extra></extra>",
    ))
    layout = base_layout(title=f"Predicted Lead Time — {current_product['name']}", height=360)
    layout["xaxis"]["title"] = "Lead Time (days)"
    layout["margin"]["l"] = 150
    fig.update_layout(**layout)
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Current Factory", current_product["factory"])
    m2.metric("Current Lead Time", f"{current_days:.2f} d")
    m3.metric("Fastest Option", fastest_factory, delta=f"-{reduction_pct:.1f}%" if fastest_factory != current_product["factory"] else "already optimal")
    m4.metric("Fastest Lead Time", f"{fastest_days:.2f} d")

    is_flagged = current_product["profit"] <= RISK_THRESHOLD
    if current_product["factory"] == RECOMMENDED_FACTORY:
        st.markdown(f"""
        <div class="ok-card"><div class="ok-title">{icon("check", TEAL, 12)} Suggested Action</div>
        <div class="insight-text">This product is already produced at The Other Factory — the fastest node in the network. No reassignment needed.</div></div>
        """, unsafe_allow_html=True)
    elif priority >= 60 and is_flagged:
        st.markdown(f"""
        <div class="alert-card"><div class="alert-title">{icon("alert", CORAL, 12)} Suggested Action</div>
        <div class="insight-text">With priority weighted toward profit ({priority}/100) and a flagged profit impact of {current_product['profit']*100:.1f}pp,
        consider holding this product at <strong>{current_product['factory']}</strong> pending a margin review before reassigning.</div></div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="ok-card"><div class="ok-title">{icon("check", TEAL, 12)} Suggested Action</div>
        <div class="insight-text">Reassign from <strong>{current_product['factory']}</strong> to <strong>{fastest_factory}</strong> for an estimated
        {reduction_pct:.1f}% lead-time reduction under the selected region / ship-mode combination.</div></div>
        """, unsafe_allow_html=True)

# =================================================================
# TAB 3 — WHAT-IF SCENARIO ANALYSIS
# =================================================================
with tab_whatif:
    st.markdown("""
    <div class="section-header">
        <span class="section-number">» What-If</span>
        <span class="section-title">Current vs. Recommended Assignment</span>
        <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    base_current = get_base_days(current_product)[current_product["factory"]]
    base_other = get_base_days(current_product)[RECOMMENDED_FACTORY]
    already_optimal = current_product["factory"] == RECOMMENDED_FACTORY

    colA, colB = st.columns(2, gap="large")
    with colA:
        st.markdown(f"""
        <div class="card">
            <span class="badge badge-monitor" style="background:rgba(240,99,74,0.12);color:#f0634a">CURRENT</span>
            <div style='font-family:"Playfair Display",serif; font-size:1.3rem; color:#E8E8F0; margin-top:0.6rem'>{current_product['factory']}</div>
            <div style='color:#9096B4; font-size:0.85rem; margin-top:0.6rem'>Predicted Lead Time</div>
            <div style='font-family:"Playfair Display",serif; font-size:1.8rem; color:#A29BFF'>{base_current:.2f} days</div>
            <div style='color:#9096B4; font-size:0.85rem; margin-top:0.8rem'>Division</div>
            <div style='color:#E8E8F0'>{current_product['division']}</div>
        </div>
        """, unsafe_allow_html=True)
    with colB:
        badge_label = "ALREADY OPTIMAL" if already_optimal else "RECOMMENDED"
        badge_class = "badge-optimal" if already_optimal else "badge-improve"
        st.markdown(f"""
        <div class="card">
            <span class="badge {badge_class}">{badge_label}</span>
            <div style='font-family:"Playfair Display",serif; font-size:1.3rem; color:#E8E8F0; margin-top:0.6rem'>{RECOMMENDED_FACTORY}</div>
            <div style='color:#9096B4; font-size:0.85rem; margin-top:0.6rem'>Predicted Lead Time</div>
            <div style='font-family:"Playfair Display",serif; font-size:1.8rem; color:#3ecfb2'>{base_other:.2f} days</div>
            <div style='color:#9096B4; font-size:0.85rem; margin-top:0.8rem'>Lead Time Reduction</div>
            <div style='color:#E8E8F0'>{current_product['reduction']:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

    fig = go.Figure(go.Bar(
        x=[current_product["factory"], RECOMMENDED_FACTORY],
        y=[base_current, base_other],
        marker=dict(color=[CORAL, TEAL]),
        text=[f"{base_current:.2f}d", f"{base_other:.2f}d"], textposition="outside",
        textfont=dict(size=12, color="#E8E8F0"),
        hovertemplate="<b>%{x}</b><br>%{y:.2f} days<extra></extra>",
    ))
    layout = base_layout(title="Lead Time Comparison", height=320)
    layout["yaxis"]["title"] = "Lead Time (days)"
    fig.update_layout(**layout)
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

    if already_optimal:
        st.markdown(f"""
        <div class="ok-card"><div class="ok-title">{icon("check", TEAL, 12)} No Change Recommended</div>
        <div class="insight-text">{current_product['name']} is already produced at the fastest factory in the network.</div></div>
        """, unsafe_allow_html=True)
    else:
        profit_note = "improves margin" if current_product["profit"] >= 0 else "carries a small margin trade-off"
        st.markdown(f"""
        <div class="insight-box"><div class="insight-title">{icon("trend", GOLD, 13)} Net Effect</div>
        <div class="insight-text">Reassigning <strong>{current_product['name']}</strong> to The Other Factory saves
        <strong style='color:#3ecfb2'>{current_product['reduction']:.2f}%</strong> in lead time and
        {profit_note} by <strong style='color:{"#3ecfb2" if current_product["profit"]>=0 else "#f0634a"}'>{current_product['profit']*100:+.1f}pp</strong> —
        well within the &lt;{STABILITY_BOUND*100:.0f}pp stability bound.</div></div>
        """, unsafe_allow_html=True)

# =================================================================
# TAB 4 — RECOMMENDATION DASHBOARD
# =================================================================
with tab_rec:
    st.markdown("""
    <div class="section-header">
        <span class="section-number">» Recommendations</span>
        <span class="section-title">Ranked Reassignment Suggestions</span>
        <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)
    st.caption(f"Ranked using the sidebar priority slider (currently {priority}/100 · {'speed-weighted' if priority < 50 else 'profit-weighted' if priority > 50 else 'balanced'}). Baseline reflects Standard Class shipping averaged across all regions — use the Simulator tab for a specific region / ship-mode view.")

    rows = []
    for p in PRODUCTS:
        active = p["reduction"] > 0
        rows.append(dict(
            Product=p["name"],
            Division=p["division"],
            **{"Current Factory": p["factory"]},
            **{"Recommended Factory": RECOMMENDED_FACTORY if active else "— (already optimal)"},
            **{"Lead Time Reduction (%)": p["reduction"]},
            **{"Profit Impact (pp)": p["profit"] * 100},
            **{"Priority Score": composite_score(p, priority) if active else np.nan},
            Risk="Monitor" if p["profit"] <= RISK_THRESHOLD else ("Optimal" if not active else "Low"),
        ))
    df = pd.DataFrame(rows)
    df_active = df[df["Recommended Factory"] != "— (already optimal)"].sort_values("Priority Score", ascending=False)
    df_optimal = df[df["Recommended Factory"] == "— (already optimal)"]

    st.dataframe(
        pd.concat([df_active, df_optimal]),
        use_container_width=True, hide_index=True,
        column_config={
            "Lead Time Reduction (%)": st.column_config.ProgressColumn(
                "Lead Time Reduction (%)", min_value=0, max_value=5, format="%.2f%%"),
            "Profit Impact (pp)": st.column_config.NumberColumn("Profit Impact (pp)", format="%.1f"),
            "Priority Score": st.column_config.NumberColumn("Priority Score", format="%.2f"),
        },
    )

    top5 = df_active.head(5)
    fig = go.Figure(go.Bar(
        x=top5["Priority Score"], y=top5["Product"], orientation="h",
        marker=dict(color=GOLD),
        text=[f"{v:.2f}" for v in top5["Priority Score"]], textposition="outside",
        textfont=dict(size=10, color="#9096B4"),
    ))
    layout = base_layout(title="Top 5 Recommendations at Current Priority Setting", height=320)
    layout["margin"]["l"] = 200
    fig.update_layout(**layout)
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

# =================================================================
# TAB 5 — RISK & IMPACT PANEL
# =================================================================
with tab_risk:
    st.markdown("""
    <div class="section-header">
        <span class="section-number">» Risk</span>
        <span class="section-title">Risk & Impact Panel</span>
        <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    flagged = [p for p in PRODUCTS if p["profit"] <= RISK_THRESHOLD]
    r1, r2, r3 = st.columns(3)
    r1.metric("Products Flagged", f"{len(flagged)}")
    r2.metric("Worst Profit Impact", f"{min(p['profit'] for p in PRODUCTS)*100:.1f} pp")
    r3.metric("Stability Bound", f"±{STABILITY_BOUND*100:.0f} pp")

    fig = go.Figure()
    for p in PRODUCTS:
        color = CORAL if p["profit"] <= RISK_THRESHOLD else (LAVENDER if p["reduction"] == 0 else TEAL)
        fig.add_trace(go.Scatter(
            x=[p["reduction"]], y=[p["profit"] * 100], mode="markers",
            marker=dict(size=14, color=color, opacity=0.85, line=dict(width=1, color="rgba(255,255,255,0.2)")),
            name=p["name"], showlegend=False,
            hovertemplate=f"<b>{p['name']}</b><br>Reduction: %{{x:.2f}}%<br>Profit Impact: %{{y:.1f}}pp<extra></extra>",
        ))
    fig.add_hline(y=STABILITY_BOUND * 100, line_dash="dash", line_color="#5B6180", annotation_text="+stability bound")
    fig.add_hline(y=-STABILITY_BOUND * 100, line_dash="dash", line_color="#5B6180", annotation_text="-stability bound")
    fig.add_hline(y=RISK_THRESHOLD * 100, line_dash="dot", line_color=CORAL, annotation_text="risk threshold")
    layout = base_layout(title="Profit Impact vs. Lead Time Reduction (per product)", height=420)
    layout["xaxis"]["title"] = "Lead Time Reduction (%)"
    layout["yaxis"]["title"] = "Profit Impact (pp)"
    fig.update_layout(**layout)
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

    if flagged:
        for p in flagged:
            st.markdown(f"""
            <div class="alert-card">
                <div class="alert-title">{icon("alert", CORAL, 12)} Monitor — {p['name']}</div>
                <div class="alert-text">Reassigning to The Other Factory shows a profit impact of
                <strong>{p['profit']*100:.1f}pp</strong> — still within the &lt;{STABILITY_BOUND*100:.0f}pp safety threshold,
                but the largest margin trade-off in the catalogue and worth a manual review before executing.</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="ok-card"><div class="ok-title">{icon("check", TEAL, 12)} All Clear</div>
        <div class="ok-text">No products currently breach the profit-impact risk threshold.</div></div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="insight-box" style='margin-top:0.5rem'>
        <div class="insight-title">{icon("shield", GOLD, 13)} Reading this panel</div>
        <div class="insight-text">
            Every recommended reassignment stays within ±{STABILITY_BOUND*100:.0f} percentage points of profit impact —
            the published safety bound for the whole simulation. The {len(flagged)} products above the risk threshold
            are still net-safe, but represent the closest calls and are the best candidates for a manual
            margin review before rollout.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; margin-top:2.5rem; padding-top:1.5rem; border-top:1px solid #2A2D3A'>
    <div style='font-family:"Playfair Display",serif; font-size:1rem; color:#5B6180'>Nassau Candy Distributor — Supply Chain Analytics</div>
    <div style='font-size:0.75rem; color:#3a4055; margin-top:6px'>Himanshu Rai · Data Science Internship Project · May 2026</div>
</div>
""", unsafe_allow_html=True)

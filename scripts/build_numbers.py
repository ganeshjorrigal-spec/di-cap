"""Build data/numbers.csv and data/ratios.md from reported figures (Rs crore).
Every reported figure carries its source. Calculated figures carry their formula."""
import csv, os
D = "Dabur"; M = "Marico"
SRC_D26 = ("NSE integrated filing, consolidated audited results FY26 (7 May 2026)", "https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_156029_07052026173844_iXBRL_WEB.html")
SRC_D25 = ("NSE integrated filing, consolidated audited results FY25 (7 May 2025)", "https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_89680_07052025230450_iXBRL_WEB.html")
SRC_D24 = ("Dabur Annual Report FY24, consolidated financial statements", "https://www.dabur.com/digital-annual-report/reports/dabur-consolidated-financials.pdf")
SRC_M = ("Marico consolidated audited results FY26 with FY25 comparatives (exchange filing copy)", "https://files.tijorifinance.com/india/company/3891/2419/FR-Mar26.pdf")
SRC_MIP = ("Marico Q4 FY26 investor presentation", "https://files.tijorifinance.com/india/company/3891/2420/IP-Apr26.pdf")
SRC_SCR = ("Screener.in consolidated (aggregated; website figure)", "https://www.screener.in/")

R = {}  # (co, year, key) -> value
rows = []
def rep(co, yr, key, val, src, loc):
    R[(co, yr, key)] = val
    rows.append([co, key, round(val, 2), "Rs cr", yr, src[0] + " | " + src[1], loc, "As reported", "Reported"])

# ---------- Dabur (lakh / 100 = crore) ----------
d26 = dict(rev=1319257, oi=59977, mat=560274, pur=130331, chinv=-8228, emp=137564, fin=14540, da=46893,
           oth=254132, adv=88806, pbt_pre=243728, exc=-1505, pbt=242223, tax=55174, np=186869, np_own=189503, np_nci=-2634,
           ta=1747991, eq_own=1141952, nci=38323, eq_tot=1180275, tl=567716, nca=859395, ca=888596,
           inv=232163, rec=71541, pay=295434, cash=19937, bank=36270, ci=459547, nci_inv=433116,
           b_cur=104672, b_nc=1596, lease_nc=18118, lease_cur=4346, ppe=283992, goodwill=40511, intang=65007,
           cfo=257862, cfi=-128522, cff=-123573, taxpaid=39879, capex=42014, div=141896, intpaid=14046,
           cf_rec=17668, cf_pay=12787, cf_inv=-2151, cf_oca=-935, cf_ofa=-749, cf_ocl=-532, cf_intinc=-36622, cf_fv=-12870,
           tr_buy=743820, tr_sell=625311, seg_cc=1086407, seg_food=201555, seg_ret=10656, seg_oth=16748)
d25 = dict(rev=1256309, oi=55010, mat=526368, pur=132828, chinv=-5710, emp=129123, fin=16350, da=44560,
           oth=242066, adv=86464, pbt_pre=225734, exc=0, pbt=225734, tax=51747, np=174042, np_own=176763, np_nci=-2721,
           ta=1623228, eq_own=1080069, nci=40957, eq_tot=1121026, tl=502202, nca=969982, ca=653246,
           inv=230011, rec=88850, pay=282534, cash=18427, bank=39374, ci=208755, nci_inv=537243,
           b_cur=42609, b_nc=30403, ppe=279988, goodwill=40509, intang=74122,
           cfo=198675, cfi=-44911, cff=-140534, taxpaid=40454, capex=56954, div=97478, intpaid=16477,
           cf_rec=1222, cf_pay=40718, cf_inv=-35314, cf_oca=-20886, cf_ofa=146, cf_ocl=3243, cf_intinc=-40816, cf_fv=-2815,
           tr_buy=618840, tr_sell=587912, seg_cc=1016010, seg_food=210061, seg_ret=11547, seg_oth=15029)
for yr, d, src, loc in (("FY26", d26, SRC_D26, "Consolidated P&L / statement of assets and liabilities / cash flow / segment note, year ended 31 Mar 2026"),
                        ("FY25", d25, SRC_D25, "Consolidated P&L / statement of assets and liabilities / cash flow / segment note, year ended 31 Mar 2025")):
    for k, v in d.items():
        rep(D, yr, k, v / 100.0, src, loc)
d24 = dict(rev=12404.01, oi=482.41, mat=5186.90, pur=1211.11, chinv=48.95, emp=1239.56, fin=124.18, da=399.21,
           pbt_pre=2358.74, exc=0, pbt=2358.74, tax=547.43, np=1811.31, np_own=1842.68, np_nci=-31.37,
           ta=15122.68, eq_own=177.20 + 9689.10, nci=436.78, eq_tot=10303.08, inv=1946.97, rec=898.72, pay=2421.71,
           cash=247.60, bank=418.76, ci=1666.60, nci_inv=5258.76, b_cur=622.10, b_nc=535.97, lease_cur=36.75, lease_nc=170.27,
           cfo=2013.47, cfi=-971.74, cff=-1161.18, taxpaid=493.92, capex=563.86, div=965.76, intpaid=106.68,
           cf_rec=-55.34, cf_pay=216.57, cf_inv=77.24, cf_oca=-203.77, cf_ofa=-4.92, cf_intinc=-393.10, cf_fv=-39.45)
d23 = dict(rev=11529.89, oi=445.39, fin=78.24, pbt=2218.68, np=1701.33, np_own=1707.15, cfo=1488.43)
for k, v in d24.items():
    rep(D, "FY24", k, v, SRC_D24, "Consolidated balance sheet, P&L and cash flow, FY24 column")
for k, v in d23.items():
    rep(D, "FY23", k, v, SRC_D24, "Consolidated P&L and cash flow, FY23 comparative column")
for yr, rev, op, oi, fin, da, pbt in (("FY22", 10889, 2252, 308, 39, 253, 2269),):
    pass
# ---------- Marico (Rs crore) ----------
m26 = dict(rev=13611, oi=204, mat=6197, pur=1565, chinv=-203, emp=916, fin=53, da=202, adv=1300, oth_ex_adv=1508,
           pbt=2277, tax=464, np=1813, np_own=1762, np_nci=51,
           ta=10075, eq_own=4210, nci=284, eq_tot=4494, tl=5581, nca=4215, ca=5860,
           inv=1611, rec=1304, pay=146 + 1488, cash=404, bank=89, ci=1948, nci_inv=135, b_cur=355, b_nc=0,
           lease_cur=75, lease_nc=127, goodwill=1036, intang=1498, ppe=832, ocfl=1585, oncfl=947,
           cfo=2084, cfi=-722, cff=-1279, taxpaid=565, capex=319, acq=452, acq_nci=221, div=908, div_nci=81,
           cf_inv=-352, cf_rec=-2, cf_pay=282, cf_ofl=362, wc_total=253)
m25 = dict(rev=10831, oi=208, mat=4572, pur=960, chinv=-144, emp=831, fin=53, da=178, adv=1128, oth_ex_adv=1345,
           pbt=2116, tax=458, np=1658, np_own=1629, np_nci=29,
           ta=8332, eq_own=3975, nci=291, eq_tot=4266, tl=4066, nca=3255, ca=5077,
           inv=1235, rec=1271, pay=89 + 1217, cash=321, bank=456, ci=1375, nci_inv=215, b_cur=379, b_nc=0,
           lease_cur=51, lease_nc=124, goodwill=857, intang=946, ppe=710, ocfl=288, oncfl=1211,
           cfo=1363, cfi=-621, cff=-649, taxpaid=484, capex=161, acq=0, acq_nci=70, div=453, div_nci=47,
           cf_inv=101, cf_rec=-205, cf_pay=-218, cf_ofl=4, wc_total=-293)
for yr, d in (("FY26", m26), ("FY25", m25)):
    for k, v in d.items():
        rep(M, yr, k, float(v), SRC_M, f"Consolidated P&L / balance sheet / cash flow, {yr} column")
# Screener 5-year series for trends (both)
scr = {D: {"FY22": (10889, 2252, 308, 39, 253, 2269, 1742, 1802), "FY23": (11530, 2162, 445, 78, 311, 2219, 1701, 1488)},
       M: {"FY22": (9512, 1681, 98, 39, 139, 1601, 1255, 1016), "FY23": (9764, 1810, 144, 56, 155, 1743, 1322, 1419), "FY24": (9653, 2026, 142, 73, 158, 1937, 1502, 1387)}}
for co, ys in scr.items():
    for yr, t in ys.items():
        for k, v in zip(("scr_sales", "scr_ebitda", "scr_oi", "scr_fin", "scr_da", "scr_pbt", "scr_np", "scr_cfo"), t):
            R[(co, yr, k)] = float(v)
            rows.append([co, k, v, "Rs cr", yr, SRC_SCR[0] + " | " + SRC_SCR[1], "Consolidated annual P&L and cash flow tables", "Website aggregate", "Reported (website)"])

# ---------- Calculations ----------
def g(co, yr, k): return R[(co, yr, k)]
calc = []
def c(co, yr, key, val, defn, unit="ratio"):
    R[(co, yr, key)] = val
    calc.append([co, key, round(val, 4) if unit != "Rs cr" else round(val, 2), unit, yr, "Calculated from reported rows", "data/numbers.csv", defn, "Calculated"])

for co, yrs in ((D, ("FY24", "FY25", "FY26")), (M, ("FY25", "FY26"))):
    for y in yrs:
        rev = g(co, y, "rev")
        cogs = g(co, y, "mat") + g(co, y, "pur") + g(co, y, "chinv")
        c(co, y, "cogs_built", cogs, "Materials consumed + purchases of stock-in-trade + change in inventories", "Rs cr")
        c(co, y, "gross_margin", (rev - cogs) / rev, "(Revenue from operations - built COGS) / revenue")
        pbt_pre = g(co, y, "pbt_pre") if (co, y, "pbt_pre") in R else g(co, y, "pbt")
        ebit = pbt_pre - g(co, y, "oi") + g(co, y, "fin")
        c(co, y, "ebit_operating", ebit, "PBT before exceptional items - other income + finance costs", "Rs cr")
        c(co, y, "operating_margin", ebit / rev, "Operating EBIT / revenue from operations")
        c(co, y, "net_margin", g(co, y, "np_own") / rev, "Profit attributable to owners / revenue from operations")
        c(co, y, "roe", g(co, y, "np_own") / g(co, y, "eq_own"), "Profit attributable to owners / closing equity attributable to owners")
        at = rev / g(co, y, "ta"); em = g(co, y, "ta") / g(co, y, "eq_own")
        c(co, y, "asset_turnover", at, "Revenue / closing total assets")
        c(co, y, "equity_multiplier", em, "Closing total assets / closing owners' equity")
        c(co, y, "dupont_product", (g(co, y, "np_own") / rev) * at * em, "Net margin x asset turnover x equity multiplier (must equal ROE)")
        borrow = g(co, y, "b_cur") + g(co, y, "b_nc")
        c(co, y, "borrowings", borrow, "Current + non-current borrowings (excludes lease liabilities)", "Rs cr")
        c(co, y, "debt_to_equity", borrow / g(co, y, "eq_own"), "Borrowings / closing owners' equity")
        treas = g(co, y, "cash") + g(co, y, "bank") + g(co, y, "ci") + g(co, y, "nci_inv")
        c(co, y, "cash_and_investments", treas, "Cash + other bank balances + current investments + non-current investments", "Rs cr")
        c(co, y, "net_debt", borrow - treas, "Borrowings - cash and investments (negative = net cash)", "Rs cr")
        ce = g(co, y, "eq_tot") + borrow
        c(co, y, "capital_employed", ce, "Total equity (incl. NCI) + borrowings", "Rs cr")
        c(co, y, "roce", (g(co, y, "pbt") + g(co, y, "fin")) / ce, "(PBT + finance costs) / capital employed")
        c(co, y, "roce_operating_ex_treasury", ebit / (ce - treas), "Operating EBIT / (capital employed - cash and investments)")
        c(co, y, "interest_cover", ebit / g(co, y, "fin"), "Operating EBIT / finance costs")
        c(co, y, "other_income_share_pbt", g(co, y, "oi") / g(co, y, "pbt"), "Other income / PBT")
        rd = g(co, y, "rec") / rev * 365; idays = g(co, y, "inv") / cogs * 365; pd = g(co, y, "pay") / cogs * 365
        c(co, y, "receivable_days", rd, "Closing trade receivables / revenue x 365", "days")
        c(co, y, "inventory_days", idays, "Closing inventories / built COGS x 365", "days")
        c(co, y, "payable_days", pd, "Closing trade payables / built COGS x 365", "days")
        c(co, y, "ccc", rd + idays - pd, "Receivable days + inventory days - payable days", "days")
        c(co, y, "cfo_minus_pat", g(co, y, "cfo") - g(co, y, "np"), "Cash from operations - group profit for the year (incl. NCI)", "Rs cr")
        c(co, y, "cfo_to_pat", g(co, y, "cfo") / g(co, y, "np"), "Cash from operations / group profit for the year")
        if (co, y, "adv") in R: c(co, y, "ad_to_sales", g(co, y, "adv") / rev, "Advertisement / revenue")
        c(co, y, "employee_to_sales", g(co, y, "emp") / rev, "Employee benefits / revenue")
        c(co, y, "da_to_sales", g(co, y, "da") / rev, "Depreciation and amortisation / revenue")
# Dabur FY23 operating margin and 5-yr trend from Screener for FY22 (both) and Marico FY22-24
c(D, "FY23", "operating_margin", (g(D, "FY23", "pbt") - g(D, "FY23", "oi") + g(D, "FY23", "fin")) / g(D, "FY23", "rev"), "(PBT - other income + finance costs) / revenue")
for co, ys in ((D, ("FY22",)), (M, ("FY22", "FY23", "FY24"))):
    for y in ys:
        c(co, y, "operating_margin", (g(co, y, "scr_pbt") - g(co, y, "scr_oi") + g(co, y, "scr_fin")) / g(co, y, "scr_sales"), "(PBT - other income + finance costs) / sales, Screener aggregates")
# CCC change decomposition
for co, a, b in ((D, "FY25", "FY26"), (M, "FY25", "FY26"), (D, "FY24", "FY25")):
    dr = g(co, b, "receivable_days") - g(co, a, "receivable_days"); di = g(co, b, "inventory_days") - g(co, a, "inventory_days"); dp = g(co, b, "payable_days") - g(co, a, "payable_days")
    c(co, f"{a}->{b}", "ccc_change_check", (dr + di - dp) - (g(co, b, "ccc") - g(co, a, "ccc")), f"(dRec {dr:.2f} + dInv {di:.2f} - dPay {dp:.2f}) - dCCC; must be 0", "days")
# Revenue CAGR FY22-26
c(D, "FY22-FY26", "revenue_cagr", (g(D, "FY26", "rev") / g(D, "FY22", "scr_sales")) ** 0.25 - 1, "(FY26 revenue / FY22 sales)^(1/4) - 1")
c(M, "FY22-FY26", "revenue_cagr", (g(M, "FY26", "rev") / g(M, "FY22", "scr_sales")) ** 0.25 - 1, "(FY26 revenue / FY22 sales)^(1/4) - 1")
# 3-yr cash conversion Dabur, 2-yr Marico
c(D, "FY24-FY26", "cfo_to_pat_cum", sum(g(D, y, "cfo") for y in ("FY24", "FY25", "FY26")) / sum(g(D, y, "np") for y in ("FY24", "FY25", "FY26")), "Sum CFO / sum group profit, 3 years")
c(M, "FY25-FY26", "cfo_to_pat_cum", sum(g(M, y, "cfo") for y in ("FY25", "FY26")) / sum(g(M, y, "np") for y in ("FY25", "FY26")), "Sum CFO / sum group profit, 2 years")
# Tie checks
checks = []
for co, ys in ((D, ("FY25", "FY26")), (M, ("FY25", "FY26"))):
    for y in ys:
        checks.append((co, y, "BS: assets = equity + liabilities", g(co, y, "ta") - (g(co, y, "eq_tot") + g(co, y, "tl"))))
        checks.append((co, y, "BS: assets = NCA + CA", g(co, y, "ta") - (g(co, y, "nca") + g(co, y, "ca"))))
        checks.append((co, y, "Equity: owners + NCI = total", g(co, y, "eq_tot") - (g(co, y, "eq_own") + g(co, y, "nci"))))
        checks.append((co, y, "P&L: owners + NCI = profit", g(co, y, "np") - (g(co, y, "np_own") + g(co, y, "np_nci"))))
checks.append((D, "FY24", "Equity: owners + NCI = total", g(D, "FY24", "eq_tot") - (g(D, "FY24", "eq_own") + g(D, "FY24", "nci"))))
checks.append((D, "FY24", "P&L: owners + NCI = profit", g(D, "FY24", "np") - (g(D, "FY24", "np_own") + g(D, "FY24", "np_nci"))))
for co, y in ((D, "FY24"), (D, "FY25"), (D, "FY26"), (M, "FY25"), (M, "FY26")):
    checks.append((co, y, "DuPont product - ROE", g(co, y, "dupont_product") - g(co, y, "roe")))
    checks.append((co, y, "CF: CFO+CFI+CFF (net change before FX)", g(co, y, "cfo") + g(co, y, "cfi") + g(co, y, "cff")))

os.makedirs("data", exist_ok=True)
with open("data/numbers.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company", "figure", "value", "unit", "year", "source", "location", "definition", "type"])
    w.writerows(rows); w.writerows(calc)
with open("data/checks.md", "w") as f:
    f.write("# Tie checks (auto-generated by scripts/build_numbers.py)\n\n| Company | Year | Check | Difference |\n|---|---|---|---|\n")
    for co, y, n, v in checks: f.write(f"| {co} | {y} | {n} | {v:.4f} |\n")
# Ratio summary
keys = ["rev", "gross_margin", "operating_margin", "net_margin", "roe", "asset_turnover", "equity_multiplier", "dupont_product", "roce", "roce_operating_ex_treasury",
        "debt_to_equity", "net_debt", "interest_cover", "other_income_share_pbt", "receivable_days", "inventory_days", "payable_days", "ccc", "np", "cfo", "cfo_minus_pat", "cfo_to_pat",
        "ad_to_sales", "employee_to_sales", "da_to_sales", "cash_and_investments"]
with open("data/ratios.md", "w") as f:
    f.write("# Ratio summary (auto-generated; definitions in data/numbers.csv)\n\n| Metric | Dabur FY24 | Dabur FY25 | Dabur FY26 | Marico FY25 | Marico FY26 |\n|---|---|---|---|---|---|\n")
    for k in keys:
        vals = []
        for co, y in ((D, "FY24"), (D, "FY25"), (D, "FY26"), (M, "FY25"), (M, "FY26")):
            v = R.get((co, y, k))
            if v is None: vals.append("n/a")
            elif k in ("receivable_days", "inventory_days", "payable_days", "ccc", "interest_cover"): vals.append(f"{v:,.1f}")
            elif abs(v) < 5 and k not in ("rev", "np", "cfo"): vals.append(f"{v*100:.1f}%" if k not in ("asset_turnover", "equity_multiplier", "debt_to_equity", "cfo_to_pat") else f"{v:.2f}")
            else: vals.append(f"{v:,.1f}")
        f.write(f"| {k} | " + " | ".join(vals) + " |\n")
    f.write("\n## Trends\n\n| Metric | FY22 | FY23 | FY24 | FY25 | FY26 |\n|---|---|---|---|---|---|\n")
    for co in (D, M):
        f.write(f"| {co} operating margin | " + " | ".join(f"{R[(co,y,'operating_margin')]*100:.1f}%" if (co, y, "operating_margin") in R else "n/a" for y in ("FY22", "FY23", "FY24", "FY25", "FY26")) + " |\n")
    f.write(f"\nRevenue CAGR FY22-26: Dabur {R[(D,'FY22-FY26','revenue_cagr')]*100:.1f}%, Marico {R[(M,'FY22-FY26','revenue_cagr')]*100:.1f}%\n")
    f.write(f"Cash conversion: Dabur 3-yr CFO/PAT {R[(D,'FY24-FY26','cfo_to_pat_cum')]*100:.1f}%; Marico 2-yr {R[(M,'FY25-FY26','cfo_to_pat_cum')]*100:.1f}%\n")
    for k in [(D,'FY25->FY26'),(M,'FY25->FY26'),(D,'FY24->FY25')]:
        f.write(f"CCC change check {k[0]} {k[1]}: {R[(k[0],k[1],'ccc_change_check')]:.4f}\n")
print(open("data/checks.md").read()); print(open("data/ratios.md").read())

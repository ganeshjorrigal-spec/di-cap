import csv
rows=list(csv.DictReader(open("data/numbers.csv")))
idx={(r["company"],r["year"],r["figure"]):r for r in rows}
short={"NSE integrated filing, consolidated audited results FY26 (7 May 2026)":"[S1] Dabur FY26 audited results",
 "NSE integrated filing, consolidated audited results FY25 (7 May 2025)":"[S2] Dabur FY25 audited results",
 "Dabur Annual Report FY24, consolidated financial statements":"[S3] Dabur Annual Report FY24",
 "Marico consolidated audited results FY26 with FY25 comparatives (exchange filing copy)":"[S4] Marico FY26 audited results",
 "Marico Q4 FY26 investor presentation":"[S5] Marico Q4 FY26 presentation",
 "Dabur Q4 FY26 investor presentation":"[S6] Dabur Q4 FY26 presentation",
 "Screener.in consolidated (aggregated; website figure)":"[S7] Screener.in (website)"}
names={"rev":"Revenue from operations","np":"Profit for the year (group)","np_own":"Profit attributable to owners","cfo":"Cash from operations",
"eq_own":"Equity attributable to owners","ta":"Total assets","eq_tot":"Total equity","borrowings":"Borrowings","fin":"Finance costs","oi":"Other income","pbt":"Profit before tax",
"pbt_pre":"Profit before exceptional items and tax","da":"Depreciation and amortisation","emp":"Employee benefits expense","adv":"Advertisement","oth":"Other expenses",
"mat":"Cost of materials consumed","pur":"Purchases of stock-in-trade","chinv":"Change in inventories","rec":"Trade receivables","inv":"Inventories","pay":"Trade payables",
"cash":"Cash and cash equivalents","bank":"Other bank balances","ci":"Current investments","nci_inv":"Non-current investments","b_cur":"Current borrowings","b_nc":"Non-current borrowings",
"lease_cur":"Lease liabilities, current","lease_nc":"Lease liabilities, non-current","div":"Dividends paid","capex":"Purchase of property, plant and equipment",
"cf_pay":"Cash flow: change in trade payables","cf_rec":"Cash flow: change in trade receivables","cf_inv":"Cash flow: change in inventories","cf_intinc":"Cash flow: interest income adjustment",
"taxpaid":"Income taxes paid","tax":"Tax expense","tr_buy":"Purchase of other long-term assets (investments)","tr_sell":"Sale of other long-term assets (investments)",
"seg_cc":"Segment revenue: Consumer Care","seg_food":"Segment revenue: Food","seg_ret":"Segment revenue: Retail","seg_oth":"Segment revenue: Other",
"ocfl":"Other current financial liabilities","cf_ofl":"Cash flow: change in other financial liabilities","wc_total":"Cash flow: total working capital change","ppe":"Property, plant and equipment",
"cogs_built":"COGS (built)","gross_margin":"Gross margin","ebit_operating":"Operating profit (EBIT)","operating_margin":"Operating margin","net_margin":"Net margin","roe":"ROE",
"asset_turnover":"Asset turnover","equity_multiplier":"Assets ÷ owners' equity","roce":"ROCE","roce_operating_ex_treasury":"Operating ROCE excluding cash and investments",
"debt_to_equity":"Borrowings ÷ owners' equity","debt_incl_leases_to_equity":"(Borrowings + leases) ÷ owners' equity","net_cash":"Net cash","cash_and_investments":"Cash and investments",
"capital_employed":"Capital employed","interest_cover":"Interest cover","other_income_share_pbt":"Other income ÷ PBT","receivable_days":"Receivable days","inventory_days":"Inventory days",
"payable_days":"Payable days","ccc":"Cash conversion cycle","cfo_minus_pat":"Cash from operations − profit","cfo_to_pat":"Cash from operations ÷ profit","ad_to_sales":"Advertisement ÷ revenue",
"employee_to_sales":"Employee cost ÷ revenue","da_to_sales":"Depreciation ÷ revenue","revenue_cagr":"Revenue growth per year","cfo_to_pat_cum":"Cumulative cash from operations ÷ profit",
"international_revenue_q4":"International revenue, Q4","dividend_declared":"Dividend declared for the year","parachute_share_india_pct":"Parachute coconut oil, % of India revenue",
"vaho_share_india_pct":"Value-added hair oils, % of India revenue","saffola_oils_share_india_pct":"Saffola edible oils, % of India revenue","india_volume_growth_pct":"India volume growth",
"india_revenue_growth_pct":"India revenue growth","international_ccg_pct":"International constant-currency growth","material_cost_pct_rev":"Material cost, % of revenue","bangladesh_share_intl_pct":"Bangladesh, % of international revenue",
"scr_sales":"Sales (website aggregate)","scr_pbt":"PBT (website aggregate)","scr_oi":"Other income (website aggregate)","scr_fin":"Interest (website aggregate)"}
want=[]
def calc_src(co,y):
    if co=="Marico": return "[S4]" if y in ("FY25","FY26") else "[S4], [S7]"
    return {"FY24":"[S3]","FY25":"[S2]","FY26":"[S1]","FY23":"[S3]"}.get(y, "[S1], [S2], [S3], [S7]")
D,M="Dabur","Marico"
DA={"FY24":("rev","np","np_own","cfo","eq_own","ta","borrowings","fin","oi","pbt","da","cf_pay","cf_rec","capex","div","operating_margin","net_margin","roe","asset_turnover","equity_multiplier","roce","gross_margin","employee_to_sales","cfo_minus_pat"),
 "FY25":("rev","np","np_own","cfo","eq_own","ta","borrowings","rec","inv","pay","cogs_built","cf_pay","cf_rec","capex","div","seg_cc","seg_food","operating_margin","net_margin","roe","roce","gross_margin","receivable_days","inventory_days","payable_days","ccc","cfo_minus_pat","tr_buy","tr_sell"),
 "FY26":("rev","np","np_own","cfo","eq_own","eq_tot","ta","borrowings","b_cur","fin","oi","pbt","pbt_pre","da","emp","adv","oth","cogs_built","rec","inv","pay","cash","bank","ci","nci_inv","lease_cur","lease_nc","cf_pay","cf_rec","cf_intinc","taxpaid","tax","capex","div","tr_buy","tr_sell","seg_cc","seg_food","seg_ret","seg_oth","gross_margin","ebit_operating","operating_margin","net_margin","roe","asset_turnover","equity_multiplier","roce","roce_operating_ex_treasury","capital_employed","cash_and_investments","net_cash","debt_to_equity","debt_incl_leases_to_equity","interest_cover","other_income_share_pbt","ad_to_sales","employee_to_sales","da_to_sales","receivable_days","inventory_days","payable_days","ccc","cfo_minus_pat")}
for y,ks in DA.items():
    for k in ks: want.append((D,y,k))
MA={"FY25":("rev","np","np_own","cfo","eq_own","ta","rec","inv","pay","cogs_built","cf_rec","cf_pay","wc_total","ocfl","ebit_operating","gross_margin","operating_margin","net_margin","roe","asset_turnover","equity_multiplier","roce","receivable_days","inventory_days","payable_days","ccc","cfo_minus_pat","cfo_to_pat","material_cost_pct_rev"),
 "FY26":("rev","np","np_own","cfo","eq_own","eq_tot","ta","borrowings","fin","oi","pbt","emp","adv","da","rec","inv","pay","cogs_built","cash","bank","ci","nci_inv","lease_cur","lease_nc","ocfl","cf_pay","cf_ofl","ebit_operating","gross_margin","operating_margin","net_margin","roe","asset_turnover","equity_multiplier","roce","roce_operating_ex_treasury","cash_and_investments","net_cash","debt_to_equity","debt_incl_leases_to_equity","interest_cover","other_income_share_pbt","ad_to_sales","employee_to_sales","da_to_sales","receivable_days","inventory_days","payable_days","ccc","cfo_minus_pat","material_cost_pct_rev")}
for y,ks in MA.items():
    for k in ks: want.append((M,y,k))
want+= [(D,"FY22","scr_sales"),(D,"FY22","scr_pbt"),(D,"FY22","scr_oi"),(D,"FY22","scr_fin"),(D,"FY22","operating_margin"),(D,"FY23","rev"),(D,"FY23","oi"),(D,"FY23","fin"),(D,"FY23","pbt"),(D,"FY23","operating_margin"),
 (M,"FY22","scr_sales"),(M,"FY22","operating_margin"),(M,"FY23","operating_margin"),(M,"FY24","operating_margin"),
 (D,"FY22-FY26","revenue_cagr"),(M,"FY22-FY26","revenue_cagr"),(D,"FY24-FY26","cfo_to_pat_cum"),(M,"FY25-FY26","cfo_to_pat_cum"),
 (D,"Q4 FY26","international_revenue_q4"),(D,"FY26","dividend_declared")]+[(M,"FY26",k) for k in ("parachute_share_india_pct","vaho_share_india_pct","saffola_oils_share_india_pct","india_volume_growth_pct","india_revenue_growth_pct","international_ccg_pct","bangladesh_share_intl_pct")]
pct={"gross_margin","operating_margin","net_margin","roe","roce","roce_operating_ex_treasury","other_income_share_pbt","ad_to_sales","employee_to_sales","da_to_sales","revenue_cagr","cfo_to_pat_cum","cfo_to_pat"}
def fmt(k,v,u):
    v=float(v)
    if k in pct: return f"{v*100:.1f}%"
    if "pct" in k: return f"{v:.1f}%"
    if u=="days": return (f"−{abs(v):.2f} days" if v<0 else f"{v:.2f} days")
    if k in ("asset_turnover","equity_multiplier","debt_to_equity","debt_incl_leases_to_equity"): return f"{v:.4f}"
    if k=="interest_cover": return f"{v:.1f}x"
    return (f"−₹{abs(v):,.2f} cr" if v<0 else f"₹{v:,.2f} cr")
out=["| Company | Figure | Value | Year | Source and location | Definition or calculation | Type |","|---|---|---|---|---|---|---|"]
missing=[]
for co,y,k in want:
    r=idx.get((co,y,k))
    if not r: missing.append((co,y,k)); continue
    if k=="ccc":
        rd,idd,pd=[round(float(idx[(co,y,x)]["value"]),2) for x in ("receivable_days","inventory_days","payable_days")]
        r=dict(r); r["value"]=str(round(rd+idd-pd,2)); r["definition"]="Receivable days + inventory days - payable days (sum of the rounded components)"
    src=r["source"].split(" | ")[0]; s=short.get(src,src)
    stmt=("consolidated balance sheet" if k in ("eq_own","eq_tot","ta","rec","inv","pay","cash","bank","ci","nci_inv","b_cur","b_nc","lease_cur","lease_nc","ocfl","borrowings") else
          "consolidated cash flow statement" if k in ("cfo","cf_pay","cf_rec","cf_inv","cf_intinc","taxpaid","capex","div","tr_buy","tr_sell","cf_ofl","wc_total") else
          "segment note" if k.startswith("seg_") else
          "consolidated P&L")
    loc= (s + ", " + (r["location"] if "presentation" in s.lower() or "Screener" in s else stmt)) if r["type"].startswith("Reported") else (calc_src(co,y) + ", calculated from the statement lines named in the definition")
    t="Reported" if r["type"]=="Reported" else ("Reported (website)" if "website" in r["type"] else "Calculated")
    out.append(f"| {co} | {names.get(k,k)} | {fmt(k,r['value'],r['unit'])} | {y} | {loc} | {"As reported" if r["type"].startswith("Reported") else r["definition"]} | {t} |")
src_list="\n".join(f"- {v}: {k} ({next((r['source'].split(' | ')[1] for r in rows if r['source'].startswith(k)),'')})" for k,v in short.items())
open("drafts/numbers-table.md","w").write("# Numbers table\n\nAll figures consolidated, ₹ crore unless stated. Reported = taken from a statement; Calculated = my arithmetic on reported figures; Reported (website) = Screener.in aggregate, used only for FY22 and FY23 trend points.\n\n"+"\n".join(out)+"\n\n## Sources\n\n"+src_list+"\n")
print(len(out)-2,"rows; missing:",missing)

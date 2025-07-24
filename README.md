# Hamilton Transit Project (Python+Power-BI)

Data-driven urban mobility project that bridges the gap between sustainability, tourism, and transport planning. This project explores optimal bus routing and environmental efficiency to connect tourists—without cars—to Hamilton’s waterfalls.

---

## Project Overview

Hamilton boasts over 100 waterfalls and cascades, but lack of car-free accessibility limits tourism potential. This project builds on data from Hamilton's Transportation Master Plan and Tourism Strategy to:
- Cluster top-rated waterfalls to design routes
- Estimate seasonal tourist demand
- Optimize bus deployment using a linear programming model that minimizes CO₂ emissions

---

## Project Highlights

- **Data Cleaning**: Manually refined data in Excel to focus on 21 waterfalls with public access and strong visitor feedback.
- **Clustering Analysis**: Grouped waterfalls using DBSCAN for route creation.
- **Demand Forecasting**: Based on seasonal, weekday/weekend data from Stats Canada and local tourism databases.
- **Optimization Modeling**: Used linear programming to propose bus schedules that reduce emissions while meeting demand.
- **Environmental Impact Assessment**: Aligned with Canada’s Net-Zero by 2050 goals.

---

## Data Cleaning Process

Raw data included 103 waterfalls. Through manual cleaning in Excel:
- Filtered out inaccessible or poorly reviewed locations
- Standardized names, coordinates, and cluster inputs
- Prioritized 21 key destinations for meaningful analysis

---

## Repository Structure

| Folder | Contents |
|--------|----------|
| `/Dashboard/` | Power BI report file `.pbix` |
| `/Data/` | Raw and cleaned datasets (Excel format) used in the project |
| `/Reports/` | Dashboard and Project PDF reports |
| `/Images/` | Screenshots of dashboard visuals |
| `/Codes/` | Python code for clustering and LP modeling |

---

## Technologies & Tools

- Python (Pandas, NumPy, Scikit-learn)
- Excel (manual data cleaning)
- Google Maps API
- Linear Programming with PyCharm
- DBSCAN clustering
- Stats Canada & Open Hamilton datasets

---

## Key Outcomes

| Metric                  | Value                 |
|------------------------|-----------------------|
| Annual CO₂ Emissions   | 350.79 kg               |
| Bus Types Considered   | Nova Bus 40-ft, 60-ft |
| Routes Proposed        | 3                     |
| Optimized Trip Patterns| Seasonal & Demand-based|

---

## Strategic Insights

- Larger articulated buses are preferred when demand is high, reducing emissions per passenger.
- Route 2 has the highest demand across all seasons and days.
- Winter season trips are reduced to prevent service overuse during low season.
- Fall season shows the most balanced use of both bus types.

---

## Recommendations

- Add visitor demographics to tailor services digitally
- Implement dynamic pricing strategies during low-demand days
- Expand to include vehicle maintenance and fuel economics
- Incorporate electric/hybrid buses in future models

---

## Contact
Name: Maria Agualimpia  
Email Address: mariaagualimpia24@gmail.com  
LinkedIn: (https://www.linkedin.com/in/maria-agualimpia-11a535129/)

---

## References

This project incorporates official data from:
- [Open Hamilton](https://open.hamilton.ca)
- [Tourism Hamilton](https://tourismhamilton.com/hamilton-waterfalls-guide/)
- [Canada’s Net-Zero by 2050 Plan](https://www.canada.ca/en/services/environment/weather/climatechange/climate-plan/net-zero-emissions-2050.html)
- [Statistics Canada](https://www.statcan.gc.ca)



# Telco Churn TCI  
**Turning Telco Data Into a Retention Engine 🚀**  
*Built like a real AI product — not a classroom task.*

Churn isn’t a “classification exercise” — it’s a **business survival problem**.  
Telcos bleed revenue when customers leave, and most models stop at “accuracy on a notebook”.  
I didn’t build this for grades. **I built it to *ship* like an AI retention product.**

This project takes raw telco data → transforms it → trains an ML model → deploys it as an app people can actually use to make decisions.  
One person, full stack of the pipeline, end-to-end.

---

## 🚩 The Problem 

Telcos lose **millions** because they don’t know *who’s about to churn* until it’s too late.  
Retention teams guess. Discounts fly randomly. Zero targeting. Zero personalization.

**Goal:** Build an AI-driven product that predicts churn early + helps teams **act**, not just “see a probability”.

---

## 💡 What This AI Product Does

This isn’t “just a model”. It’s a **mini retention AI product**, with:

| Layer | What I Built | Why It Matters |
|-------|----------------|----------------|
| **Data Pipeline** | Cleaned, validated, transformed telco data | Real-world-ish data quality (messy in, clean out) |
| **EDA Insights** | Found behavioral patterns behind churn | Gives business context, not just math |
| **Feature Engineering** | Smart features (tenure buckets, service bundles, contract risk, etc.) | Improves model impact & explainability |
| **ML Model** | Trained + tuned churn classifier | Provides accurate early-warning signals |
| **App Layer** | Streamlit predictive app | Makes non-technical users ACT on the output |

---

## ⚙️ Tech Stack

- **Python**, Pandas, NumPy, Scikit-Learn  
- EDA + Visualization: Matplotlib, Seaborn  
- App: **Streamlit**  
- Deployment-Ready: Dockerfile + requirements.txt  
- Structure: `/notebooks`, `/app`, `/scripts`, `/data`, `/assets`

---

## 📊 Key Results (R2 = Results-First)

> The model isn’t chasing fancy metrics — it delivers **decision-value**.

- ✅ Predicts churn **before** it happens so retention teams can step in  
- ✅ Clean insights that show **why** customers churn (not just who)  
- ✅ Lightweight enough to deploy & integrate into real workflows  
- ✅ Clear “recommendation layer” for **actionable retention steps**

---

## 🧠 How It Works (High-Level)

1. **Raw data → cleaned dataset**  
2. **EDA reveals churn patterns** (contract type, tenure, payment method are killers)  
3. **Feature engineering boosts signal**  
4. **Model trained + evaluated**  
5. **Streamlit app enables prediction & what-to-do next**

---

## 🎯 Why This Project Belongs in My Portfolio

Because it’s not a toy.

I scoped this like a product someone could *use* inside a telco team.  
Full lifecycle. Clear value. Deployment mindset.  
If it’s not usable, it’s not AI — it’s homework.  
This one is **usable**.

---

## 🚀 Try the App

> When deployed: A link will go here.

- Upload customer data or input manually  
- Get churn probability + reasons + recommended actions  
- Designed for **CX, Retention, and Data teams**  

---

## 🗂️ Project Structure
```
📦 telco-churn-tci
 ┣ 📜 README.md
 ┣ 📜 CV_bullets.txt
 ┣ 📜 Dockerfile
 ┣ 📜 requirements.txt
 ┣ 📜 LICENSE
 ┣ 📜 .gitignore
 ┣ 📂 data
 ┃ ┣ 📂 raw
 ┃ ┗ 📜 telco_secret.csv
 ┣ 📂 notebooks
 ┃ ┣ 01_eda.ipynb
 ┃ ┣ 02_feature_engineering.ipynb
 ┃ ┗ 03_modeling.ipynb
 ┣ 📂 app
 ┃ ┗ streamlit_app.py
 ┣ 📂 scripts
 ┃ ┗ generate_synthetic_telco.py
 ┣ 📂 assets
 ┃ ┗ logo.png
 ┗ 📜 run.sh
```

---

## 📈 Future Enhancements

Planned upgrades — because AI products evolve:

- Add **SHAP-based explainability**
- Add retention **recommendation engine** per persona
- Deploy to **HuggingFace / Streamlit Cloud / Docker**
- Add monitoring for drift & model performance

---

## 🧑‍💻 About Me

I’m building AI products that **solve real problems**, not just hit metrics.  
Curious, hands-on, and I ship.

---

## License
This project is licensed under the MIT License.

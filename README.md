# AtmoSync - Micro-Climate Arbitrage Analytics

## 📌 Project Overview
AtmoSync is a Data Analytics project designed to monitor micro-climate conditions during commodity transportation and identify potential spoilage risks.

## 🎯 Problem Statement
Traditional supply chain monitoring systems often fail to detect hyperlocal temperature and humidity changes during transportation. These changes can affect commodity quality and lead to financial losses.

## 🚀 Objectives
- Monitor temperature, humidity, and vibration.
- Analyze commodity spoilage risks.
- Identify micro-climate changes.
- Generate actionable business insights.
- Recommend suitable alternative markets.

---

## 🏗️ System Architecture

```text
[Source Data / Sensors] ──▶ [Apache Kafka] ──▶ [Snowflake (RAW_IOT_TELEMETRY)] ──▶ [dbt Staging & Tests] ──▶ [Apache Superset BI]
```

1. **Ingestion Layer (`Apache Kafka`):** Streams real-time container micro-climate telemetry (`TIMESTAMP`, `CONTAINER_ID`, `COMMODITY`, `TEMPERATURE_C`, `HUMIDITY_PERCENT`, `VIBRATION_G`, `STATUS`).
2. **Data Warehouse (`Snowflake`):** Stores raw incoming telemetry events in `SNOWFLAKE_LEARNING_DB.PUBLIC.RAW_IOT_TELEMETRY`.
3. **Transformation & Quality (`dbt`):** Transforms raw telemetry via 4 staging models and validates data integrity using automated schema tests (`dbt/`).
4. **Visualization Layer (`Apache Superset`):** Powers the live **AtmoSync Overview Dashboard** tracking event throughput, temperature vs. humidity drift, and spoilage risk status breakdown (`superset/`).

---

## 📁 Repository Structure

- **`data/`** — Spoilage risk parameters and reference datasets
- **`dbt/`** — dbt project configuration, 4 staging models, and schema tests
- **`sql/`** — Snowflake DDL & telemetry setup queries
- **`superset/`** — Apache Superset dashboard configurations & exports
- **`atmosync_analysis.ipynb`** — Exploratory & micro-climate analysis notebook
- **`README.md`** — Project overview, architecture, and documentation
---

## 📋 Review & Progress Notes
- Week 1 and Week 2 progress write-ups submitted on the Infotact portal (`ITS/DA/1751`).
- Tracking live ingestion (`RAW_IOT_TELEMETRY`), `dbt` validation, and Superset dashboard readiness for review.

# AtmoSync - Micro-Climate Arbitrage Analytics

## ðŸ“Œ Project Overview

AtmoSync is a Data Analytics project designed to monitor micro-climate conditions during commodity transportation and identify potential spoilage risks.

## ðŸŽ¯ Problem Statement

Traditional supply chain monitoring systems often fail to detect hyperlocal temperature and humidity changes during transportation. These changes can affect commodity quality and lead to financial losses.

## ðŸš€ Objectives

- Monitor temperature, humidity, and vibration.
- Analyze commodity spoilage risks.
- Identify micro-climate changes.
- Generate actionable business insights.
- Recommend suitable alternative markets.

---

## ðŸ—ï¸ System Architecture

```text
[Source Data / Sensors] â†’ [Apache Kafka] â†’ [Snowflake] â†’ [dbt Transformation & Tests] â†’ [Apache Superset BI]
```

1. **Ingestion Layer (Apache Kafka):** Collects real-time container micro-climate telemetry, including timestamp, container ID, commodity, temperature, humidity, vibration, and status.

2. **Data Warehouse (Snowflake):** Stores raw incoming telemetry events in `SNOWFLAKE_LEARNING_DB.PUBLIC.RAW_IOT_TELEMETRY`.

3. **Transformation & Quality (dbt):** Uses four staging models to clean and transform Products, Components, Resale Market, and Warranty datasets. Seven schema tests have successfully passed.

4. **Visualization Layer (Apache Superset):** Provides the AtmoSync Overview Dashboard for monitoring telemetry events, temperature, humidity, and spoilage risk indicators.

---

## ðŸ“‚ Repository Structure

- **`data/`** â€” Sample datasets and reference parameters.
- **`dbt/`** â€” dbt project configuration, four staging models, and schema tests.
- **`sql/`** â€” Snowflake DDL and SQL analysis queries.
- **`superset/`** â€” Dashboard configurations and exports.
- **`atmosync_analysis.ipynb`** â€” Exploratory data analysis notebook.
- **`README.md`** â€” Project overview, architecture, and documentation.

---

## ðŸ“‹ Review & Progress Notes

1. **Portal Submissions:** Week 1 and Week 2 internship write-ups have been submitted.

2. **Snowflake Setup:** The `RAW_IOT_TELEMETRY` table and its schema have been created and verified.

3. **Data Transformation:** Four dbt staging models have been developed for Products, Components, Resale Market, and Warranty datasets.

4. **Data Quality:** Seven dbt schema tests have successfully passed with zero errors.

5. **GitHub Contribution:** The dbt project configuration, staging models, and schema tests have been pushed to the team's repository.

6. **Live Pipeline Status:** Kafka producer/consumer ingestion is pending execution by the technical team. Live telemetry data validation will be performed after the data is loaded into Snowflake.

7. **Next Steps:** Verify live telemetry records, execute relevant dbt models and tests, and coordinate with the team for end-to-end pipeline validation.

---

## ðŸ› ï¸ Technologies Used

- Python
- SQL
- Snowflake
- dbt
- Apache Kafka
- Apache Superset
- GitHub
---
**Project:** AtmoSync - Micro-Climate Arbitrage Analytics
**Focus Area:** Data Analytics and Data Quality Validation

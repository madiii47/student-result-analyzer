# Student Result Analyzer

A console-based data analytics application written in Python using Object-Oriented Programming (OOP) design patterns. The application automates academic grade parsing, tracks student data profiles via dynamic class attributes, implements runtime loop input validation, and compiles detailed class performance summaries.

---

## Technical Architecture and OOP Principles

* **Data Encapsulation:** Student profiles are managed by a centralized `Student` class layer, grouping state variables (`name`, `marks`, `total`, `percentage`) and computation behaviors under a single organizational blueprint.
* **Algorithmic Validation:** Features a safe multi-tiered validation loop that parses array splits, forcing users to submit a precise subject count matches to avoid system calculation errors or array index mismatches.
* **Dynamic Metric Aggregation:** Computes individual metrics like specific grading brackets (`A+` down to `Fail`) alongside macro-level statistics including multi-object accumulation and overall class average performance percentages.

---

## Project Structure

* `Student` Class: Models individual instances, mapping grade criteria ranges dynamically via internal class methods.
* `main()` Controller Function: Handles runtime state initialization, command-line data extraction, looping parameters, and outputs a formatted reporting table grid.

---

## How to Setup and Run

1. **Clone the Project:** Copy the source repository files to your local workstation.
2. **Environment Verification:** Ensure you have Python 3.x installed on your computer. Verify by typing this in your terminal:
   ```bash
   python --version
3. **Execute the Script:** Launch the application from your console interface:
   python main.py

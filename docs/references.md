# References and Resources

## Repositories
1. [pandas_dq GitHub Repo](https://github.com/AutoViML/pandas_dq): A library for identifying and resolving data quality issues in a single line of code.
2. [Awesome ML Data Quality Papers](https://github.com/SJTU-DMTai/awesome-ml-data-quality-papers): A curated list of papers focusing on ML data quality management.

## Datasets
1. [Airbnb Open Dataset](https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata)
2. Data Dictionary: Attached in `data/raw/Airbnb_Open_Data_Dictionary.xlsx`.

## Papers and Talks
- **Theodoros Rekatsinas's Lecture (Stanford MLSys Seminar):**
  - [Lecture: ](https://www.youtube.com/live/_2upFBZsMN4?si=gPN2RWeQZ7BeHhX1).
  - [Website: ](https://sliu583.gitbook.io/blog/specific-work/seminar-and-talk/mlsys/episode-18).

# Summary of "Software 2.0 for Data Quality" by Theodoros Rekatsinas

## Overview
Theodoros Rekatsinas’s talk on "Software 2.0 for Data Quality" outlines how machine learning can be used to automate various data quality tasks, including error detection, data cleaning, and imputation. Key systems like HoloClean and Pickett demonstrate the application of ML-based methods for structured data.

## Key Concepts
1. **Data Quality Challenges**:
   - Dealing with missing values, errors, and outliers.
   - The importance of structured context (e.g., functional dependencies).

2. **HoloClean**:
   - An ML-driven system for probabilistic error detection and cleaning.
   - Leverages self-supervised learning to model dependencies between features.

3. **Pickett**:
   - Focuses on validating ML pipelines by filtering noisy data before training.
   - Employs transformers for schema-level attention to detect errors.

4. **Applications**:
   - Automating cleaning for tabular data.
   - Extending ML pipelines to be robust to noisy or adversarial data.

## Important Takeaways
- Probabilistic models can learn both how clean data looks and how errors occur.
- ML-based systems outperform traditional rule-based cleaning methods, especially in scalability and adaptability.

## Relevance to Our Project
This lecture provides inspiration and methodology for:
- Using transformers for tabular data validation.
- Exploring unsupervised learning methods for error detection.
- Automating data cleaning tasks for structured datasets like Airbnb.

Slides are available in `docs/slides/rekatsinas_lecture.pdf`.

- **Draft Paper:**
  - Find the draft paper in `docs/paper/draft.pdf`.
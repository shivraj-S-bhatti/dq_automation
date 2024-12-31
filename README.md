# **DQ Automation**

**Testing out SOTA for DQ**

## **Overview**
This repository explores state-of-the-art (SOTA) techniques for **Data Quality (DQ)** automation using machine learning and advanced data profiling techniques. The project aims to streamline the data cleaning and validation processes and provide actionable insights for improved data handling.

## **Features**
- Data profiling and exploratory analysis
- Automated data validation and quality checks
- Integration of **LLM-based** agents for advanced recommendations
- Experimentation with public datasets like Airbnb Open Data

## **Repository Structure**
```
dq_automation/
│
├── data/
│   ├── raw/                 # Raw input data files (e.g., Airbnb dataset)
│   ├── processed/           # Cleaned and processed data outputs
│
├── docs/
│   ├── paper/               # Draft research papers and notes
│   ├── slides/              # Related presentation slides
│   └── references.md        # List of reference links and citations
│
├── notebooks/               # Jupyter notebooks for experiments and analysis
│
├── src/
│   ├── main.py              # Main project logic
│   ├── profiling.py         # Data profiling scripts
│   ├── utils.py             # Utility functions
│   └── validation.py        # Validation checks
│
├── tests/
│   └── test_validation.py   # Unit tests for validation scripts
│
├── .gitattributes           # Git LFS configuration
├── .gitignore               # Ignored files and folders
├── LICENSE                  # Project license
├── README.md                # Project overview
└── requirements.txt         # Python dependencies
```

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/shivraj-S-bhatti/dq_automation.git
   cd dq_automation
   ```

2. Set up a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## **Usage**
1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Run the main script:
   ```bash
   python src/main.py
   ```

3. Launch Jupyter notebooks for exploratory analysis:
   ```bash
   jupyter notebook notebooks/exploratory.ipynb
   ```

## **Datasets**
The project leverages the **Airbnb Open Data** for testing profiling and validation methodologies. [Link to Data Dictionary](https://docs.google.com/spreadsheets/d/1b_dvmyhb_kAJhUmv81rAxl4KcXn0Pymz)

## **References**
- Thodoros's lecture slides on Data Quality (included in `docs/slides`).
- State-of-the-art machine learning papers for Data Quality (`docs/paper`).
- Repositories for ML-based Data Quality tools.

## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request with your updates.

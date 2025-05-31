

 🚀 Startup Funding Analysis Dashboard


A comprehensive data-driven Streamlit web application that analyzes startup funding trends in India using a cleaned dataset. This dashboard provides insights into funding rounds, sectors, cities, investor behavior, and startup-specific analytics.


 📊 Features


- 📅 Time-Series Analysis (MoM/YoY)

- 💼 Sector-wise Investment Distribution

- 🏙️ City-wise and Round-wise Funding Trends

- 🏆 Top Funded Startups by Year

- 👨‍💼 Investor Portfolio Explorer

- 🏢 Startup-Specific Funding Analysis

- 📈 Interactive and dynamic visualizations using Matplotlib

- 🧠 Smart data parsing and correction for date anomalies


 🗂️ Dataset


The app uses a cleaned version of a startup funding dataset. Sample columns include:

- `date`

- `startup`

- `vertical`

- `subvertical`

- `city`

- `round`

- `amount`

- `investor`


Ensure your CSV file is named `startup_cleaned.csv` and located in the root directory of the project.


 📦 Installation


1. Clone the repository

   ```bash

   git clone https://github.com/your-username/startup-funding-analysis.git

   cd startup-funding-analysis

````


2. Install dependencies


   ```bash

   pip install -r requirements.txt

   ```


3. Run the app


   ```bash

   streamlit run app.py

   ```


 🧾 Requirements


Ensure the following Python packages are installed:


 `streamlit`

 `pandas`

 `matplotlib`

 `fonttools` (used internally)


Install all using:


```bash

pip install streamlit pandas matplotlib fonttools

```


 📁 Project Structure


```

.

├── app.py                    Main Streamlit application

├── startup_cleaned.csv       Cleaned dataset

├── requirements.txt          Python dependencies

└── README.md                 Project documentation

```

 ✨ Future Enhancements


 Add Plotly or Altair charts for better interactivity

 Allow filtering by multiple investors or cities

 Include CSV download/export options

 Add NLP-based search for startups and investors


 🤝 Contributing


Pull requests are welcome! For significant changes, please open an issue first to discuss your proposed changes.


 📝 License


This project is licensed under the [MIT License](LICENSE).


 👨‍💻 Developed By


Ronit Rajput – ICT Engineer

Feel free to connect on https://www.linkedin.com/in/ronit-rajput-973602278 or reach out via email.

# 🏠 Rental Property Data Analysis Dashboard

A comprehensive data science project featuring interactive analysis of rental property data with both Jupyter notebooks and a Streamlit web application.

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)

## 📊 Project Overview

This project provides a complete data science environment for analyzing rental property data, featuring:
- **Interactive Jupyter Notebooks** with filtering capabilities
- **Streamlit Web Dashboard** for real-time data exploration
- **Comprehensive Data Analysis** with statistical insights
- **Interactive Visualizations** using Plotly and Matplotlib

## 🏗️ Project Structure

```
data_science_project/
├── README.md                    # This file
├── requirements.txt             # Python package dependencies
├── streamlit_app.py            # Streamlit web application
├── data_science_workbook.ipynb # Interactive Jupyter notebook
├── practice_dataset.csv        # Sample rental property dataset
├── create_dataset.py           # Dataset generation script
└── .gitignore                  # Git ignore file
```

## 📈 Dataset Description

The practice dataset contains **12 rental properties** with the following features:
- **`last name`**: Property owner names
- **`unit sf`**: Unit square footage (50-200 sq ft, divisible by 10)
- **`rental rate`**: Monthly rental rates ($50-$250)
- **Correlation**: Larger units tend to have higher rental rates

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rental-property-analysis.git
cd rental-property-analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run streamlit_app.py
```

### 4. Launch Jupyter Notebook (Optional)
```bash
jupyter notebook
```

## 🎯 Features

### Streamlit Dashboard
- **Interactive Filtering**: Real-time data filtering by unit size and rental rate
- **Dynamic Visualizations**: Plotly charts that update with filter changes
- **Statistical Analysis**: Comprehensive metrics and correlation analysis
- **Data Export**: Download filtered datasets as CSV files
- **Responsive Design**: Works on desktop and mobile devices

### Jupyter Notebook
- **Interactive Widgets**: Slider controls for data filtering
- **Preset Filters**: Quick access to common filter combinations
- **Advanced Analysis**: Statistical analysis and data manipulation
- **Visualization Suite**: Multiple chart types and correlation analysis

## 📊 Key Metrics & Analysis

- **Correlation Analysis**: Relationship between unit size and rental rates
- **Market Segmentation**: Small, medium, and large unit categories
- **Value Analysis**: Rate per square foot calculations
- **Statistical Insights**: Mean, median, standard deviation, and range analysis

## 🚀 Deployment

### Streamlit Cloud Deployment
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click!

### Local Development
```bash
# Install development dependencies
pip install -r requirements.txt

# Run the app locally
streamlit run streamlit_app.py

# Run with auto-reload for development
streamlit run streamlit_app.py --server.runOnSave true
```

## 🎨 Customization

### Adding New Data
1. Update `practice_dataset.csv` with your data
2. Modify column names in `streamlit_app.py` if needed
3. Adjust filter ranges in the sidebar

### Styling
- Customize colors in the CSS section of `streamlit_app.py`
- Modify chart themes in the Plotly configurations
- Update the page configuration for different layouts

## 📚 Learning Objectives

This project demonstrates:
- **Data Loading & Preprocessing**: CSV file handling and data cleaning
- **Interactive Dashboards**: Streamlit app development
- **Data Visualization**: Plotly, Matplotlib, and Seaborn
- **Statistical Analysis**: Correlation, regression, and descriptive statistics
- **Web Deployment**: Streamlit Cloud deployment
- **Version Control**: Git and GitHub best practices

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Data visualization powered by [Plotly](https://plotly.com/)
- Data analysis with [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/)

## 📞 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/rental-property-analysis](https://github.com/yourusername/rental-property-analysis)


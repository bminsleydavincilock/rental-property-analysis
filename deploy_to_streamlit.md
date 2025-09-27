# Deploy to Streamlit Cloud

## Prerequisites
- GitHub repository with your code
- Streamlit Cloud account (free)

## Steps to Deploy

### 1. Push to GitHub
Make sure all your files are committed and pushed to GitHub:
```bash
git add .
git commit -m "Add Supabase integration and data upload scripts"
git push origin main
```

### 2. Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `data_science_project`
5. Main file path: `streamlit_app.py`
6. Branch: `main`

### 3. Environment Variables (if needed)
If you need to set environment variables in Streamlit Cloud:
1. Go to your app settings
2. Add secrets in the "Secrets" section
3. Your current setup uses config.py, so no secrets needed

### 4. App Configuration
- **App URL**: Will be provided by Streamlit Cloud
- **Auto-redeploy**: Enabled (redeploys on git push)
- **Python version**: 3.9+ (automatically detected)

## What's Working
✅ **Supabase Integration**: App loads data from Supabase table  
✅ **Data Processing**: All calculations and visualizations work  
✅ **Fallback**: Falls back to CSV if Supabase fails  
✅ **Interactive Features**: Filters, charts, and analysis tools  

## Test Your Deployment
1. Visit your Streamlit Cloud URL
2. Verify data loads from Supabase (should show "Data loaded from Supabase database")
3. Test all interactive features
4. Check that visualizations display correctly

## Files Included
- `streamlit_app.py` - Main Streamlit application
- `database.py` - Supabase data loading module
- `config.py` - Configuration with Supabase credentials
- `practice_dataset.csv` - Fallback data file
- `requirements.txt` - Python dependencies
- Upload scripts for data management

Your app is ready to deploy! 🚀

"""
Streamlit Data Science Dashboard
Interactive analysis of rental property data
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from database import load_data

# Page configuration
st.set_page_config(
    page_title="Rental Property Data Analysis",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .filter-section {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Data loading is now handled by the database module

def main():
    # Header
    st.markdown('<h1 class="main-header">🏠 Rental Property Data Analysis Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data from Supabase (with CSV fallback)
    df = load_data()
    if df is None:
        return
    
    # Sidebar filters
    st.sidebar.markdown("## 🔍 Filter Options")
    
    # Unit size filter
    st.sidebar.markdown("### Unit Size (sq ft)")
    min_size, max_size = st.sidebar.slider(
        "Size Range",
        min_value=int(df['unitsf'].min()),
        max_value=int(df['unitsf'].max()),
        value=(int(df['unitsf'].min()), int(df['unitsf'].max())),
        step=10
    )
    
    # Rental rate filter
    st.sidebar.markdown("### Rental Rate ($)")
    min_rate, max_rate = st.sidebar.slider(
        "Rate Range",
        min_value=float(df['rentalrate'].min()),
        max_value=float(df['rentalrate'].max()),
        value=(float(df['rentalrate'].min()), float(df['rentalrate'].max())),
        step=5.0
    )
    
    # Apply filters
    filtered_df = df[
        (df['unitsf'] >= min_size) & 
        (df['unitsf'] <= max_size) &
        (df['rentalrate'] >= min_rate) & 
        (df['rentalrate'] <= max_rate)
    ].copy()
    
    # Main content
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Units", len(filtered_df))
    
    with col2:
        avg_size = filtered_df['unitsf'].mean()
        st.metric("Avg Unit Size", f"{avg_size:.0f} sq ft")
    
    with col3:
        avg_rate = filtered_df['rentalrate'].mean()
        st.metric("Avg Rental Rate", f"${avg_rate:.2f}")
    
    with col4:
        avg_rate_per_sf = filtered_df['rate_per_sf'].mean()
        st.metric("Avg Rate/sq ft", f"${avg_rate_per_sf:.2f}")
    
    # Tabs for different analyses
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Data Overview", "📈 Visualizations", "🔍 Detailed Analysis", "📋 Raw Data"])
    
    with tab1:
        st.markdown("## Dataset Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Basic Statistics")
            st.dataframe(filtered_df.describe(), use_container_width=True)
        
        with col2:
            st.markdown("### Data Summary")
            st.write(f"**Dataset Shape:** {filtered_df.shape}")
            st.write(f"**Columns:** {', '.join(filtered_df.columns)}")
            st.write(f"**Missing Values:** {filtered_df.isnull().sum().sum()}")
            
            if len(filtered_df) > 1:
                correlation = filtered_df['unitsf'].corr(filtered_df['rentalrate'])
                st.write(f"**Correlation (Size vs Rate):** {correlation:.3f}")
    
    with tab2:
        st.markdown("## Interactive Visualizations")
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Unit Size vs Rental Rate', 'Rental Rate Distribution', 
                          'Unit Size Distribution', 'Rate per Sq Ft by Unit'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Scatter plot
        fig.add_trace(
            go.Scatter(
                x=filtered_df['unitsf'],
                y=filtered_df['rentalrate'],
                mode='markers',
                marker=dict(size=10, color='blue', opacity=0.7),
                text=filtered_df['lastname'],
                hovertemplate='<b>%{text}</b><br>Size: %{x} sq ft<br>Rate: $%{y}<extra></extra>',
                name='Units'
            ),
            row=1, col=1
        )
        
        # Add trend line
        if len(filtered_df) > 1:
            z = np.polyfit(filtered_df['unitsf'], filtered_df['rentalrate'], 1)
            p = np.poly1d(z)
            x_trend = np.linspace(filtered_df['unitsf'].min(), filtered_df['unitsf'].max(), 100)
            fig.add_trace(
                go.Scatter(
                    x=x_trend,
                    y=p(x_trend),
                    mode='lines',
                    line=dict(color='red', dash='dash'),
                    name='Trend Line'
                ),
                row=1, col=1
            )
        
        # Histogram - Rental Rate
        fig.add_trace(
            go.Histogram(
                x=filtered_df['rentalrate'],
                nbinsx=min(10, len(filtered_df)),
                marker_color='green',
                opacity=0.7,
                name='Rental Rate'
            ),
            row=1, col=2
        )
        
        # Histogram - Unit Size
        fig.add_trace(
            go.Histogram(
                x=filtered_df['unitsf'],
                nbinsx=min(10, len(filtered_df)),
                marker_color='orange',
                opacity=0.7,
                name='Unit Size'
            ),
            row=2, col=1
        )
        
        # Bar chart - Rate per sq ft
        fig.add_trace(
            go.Bar(
                x=filtered_df['lastname'],
                y=filtered_df['rate_per_sf'],
                marker_color='purple',
                opacity=0.7,
                name='Rate per Sq Ft'
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            height=800,
            showlegend=False,
            title_text="Property Analysis Dashboard"
        )
        
        fig.update_xaxes(title_text="Unit Size (sq ft)", row=1, col=1)
        fig.update_yaxes(title_text="Rental Rate ($)", row=1, col=1)
        fig.update_xaxes(title_text="Rental Rate ($)", row=1, col=2)
        fig.update_yaxes(title_text="Frequency", row=1, col=2)
        fig.update_xaxes(title_text="Unit Size (sq ft)", row=2, col=1)
        fig.update_yaxes(title_text="Frequency", row=2, col=1)
        fig.update_xaxes(title_text="Unit", row=2, col=2)
        fig.update_yaxes(title_text="Rate per Sq Ft ($)", row=2, col=2)
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("## Detailed Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Size Category Analysis")
            size_analysis = filtered_df.groupby('size_category').agg({
                'rentalrate': ['count', 'mean', 'std'],
                'rate_per_sf': 'mean'
            }).round(2)
            size_analysis.columns = ['Count', 'Avg Rate', 'Std Rate', 'Avg Rate/SqFt']
            st.dataframe(size_analysis, use_container_width=True)
        
        with col2:
            st.markdown("### Top/Bottom Units")
            
            # Most expensive
            most_expensive = filtered_df.loc[filtered_df['rentalrate'].idxmax()]
            st.markdown("**Most Expensive Unit:**")
            st.write(f"👤 {most_expensive['lastname']}")
            st.write(f"📏 {most_expensive['unitsf']} sq ft")
            st.write(f"💰 ${most_expensive['rentalrate']}")
            
            # Least expensive
            least_expensive = filtered_df.loc[filtered_df['rentalrate'].idxmin()]
            st.markdown("**Least Expensive Unit:**")
            st.write(f"👤 {least_expensive['lastname']}")
            st.write(f"📏 {least_expensive['unitsf']} sq ft")
            st.write(f"💰 ${least_expensive['rentalrate']}")
        
        # Best value analysis
        st.markdown("### Best Value Analysis")
        best_value = filtered_df.nsmallest(3, 'rate_per_sf')[['lastname', 'unitsf', 'rentalrate', 'rate_per_sf']]
        st.dataframe(best_value, use_container_width=True)
    
    with tab4:
        st.markdown("## Raw Data")
        
        # Display options
        col1, col2, col3 = st.columns(3)
        with col1:
            show_all = st.checkbox("Show all columns", value=True)
        with col2:
            sort_by = st.selectbox("Sort by", ['rentalrate', 'unitsf', 'rate_per_sf', 'lastname'])
        with col3:
            ascending = st.checkbox("Ascending order", value=False)
        
        # Prepare data for display
        display_df = filtered_df.copy()
        if not show_all:
            display_df = display_df[['lastname', 'unitsf', 'rentalrate', 'rate_per_sf']]
        
        display_df = display_df.sort_values(sort_by, ascending=ascending)
        
        st.dataframe(display_df, use_container_width=True)
        
        # Download button
        csv = display_df.to_csv(index=False)
        st.download_button(
            label="📥 Download filtered data as CSV",
            data=csv,
            file_name=f"filtered_rental_data_{len(filtered_df)}_units.csv",
            mime="text/csv"
        )
    
    # Footer
    st.markdown("---")
    st.markdown("### 🎯 Filter Summary")
    st.write(f"Showing **{len(filtered_df)}** of **{len(df)}** units")
    st.write(f"Size range: {min_size} - {max_size} sq ft")
    st.write(f"Rate range: ${min_rate:.2f} - ${max_rate:.2f}")

if __name__ == "__main__":
    main()

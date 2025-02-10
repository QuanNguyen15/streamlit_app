import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

# Cấu hình trang: full-width
st.set_page_config(page_title="Interactive Dashboard", layout="wide")

# Bọc toàn bộ nội dung trong một container (giống thẻ <div>)
with st.container():
    # Tiêu đề chính của Dashboard
    st.title("Interactive Dashboard với Streamlit")
    
    # ----------------------------
    # Các bộ lọc tương tác
    # ----------------------------
    st.sidebar.header("Bộ lọc dữ liệu")
    
    # Bộ lọc Category (cho phép chọn một category hoặc 'All')
    categories_sample = ['A', 'B', 'C', 'D']
    category_options = ['All'] + sorted(categories_sample)
    selected_category = st.sidebar.selectbox("Chọn Category", category_options, index=0)
    
    # Bộ lọc khoảng thời gian: chọn ngày bắt đầu và kết thúc
    # Xác định khoảng ngày mặc định dựa trên dữ liệu mẫu
    default_start = pd.to_datetime('2023-01-01')
    default_end = pd.to_datetime('2023-04-10')
    start_date, end_date = st.sidebar.date_input(
        "Chọn khoảng thời gian",
        value=[default_start, default_end],
        min_value=default_start,
        max_value=default_end
    )
    
    # ----------------------------
    # Tạo dữ liệu mẫu
    # ----------------------------
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=100, freq='D')
    sales = np.random.randint(100, 1000, size=100)
    profit = np.random.randint(10, 100, size=100)
    categories = np.random.choice(categories_sample, size=100)
    
    df = pd.DataFrame({
        "Date": dates,
        "Sales": sales,
        "Profit": profit,
        "Category": categories
    })
    
    # ----------------------------
    # Lọc dữ liệu theo bộ lọc
    # ----------------------------
    # Lọc theo khoảng thời gian
    df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]
    # Lọc theo Category (nếu không chọn 'All')
    if selected_category != 'All':
        df = df[df["Category"] == selected_category]
    
    # Kiểm tra dữ liệu sau khi lọc
    if df.empty:
        st.warning("Không có dữ liệu cho lựa chọn của bạn. Vui lòng thay đổi các bộ lọc.")
    else:
        # ----------------------------
        # Tạo các biểu đồ tương tác
        # ----------------------------
        
        # 1. Line Chart: Doanh số theo thời gian
        fig_line = px.line(df, x="Date", y="Sales", title="Doanh số theo thời gian")
        
        # 2. Bar Chart: Lợi nhuận trung bình theo Category
        avg_profit = df.groupby("Category")["Profit"].mean().reset_index()
        fig_bar = px.bar(avg_profit, x="Category", y="Profit", title="Lợi nhuận trung bình theo Category")
        
        # 3. Scatter Plot: Mối quan hệ giữa Sales và Profit
        fig_scatter = px.scatter(df, x="Sales", y="Profit", color="Category", title="Sales vs Profit")
        
        # 4. Histogram: Phân bố của Sales
        fig_hist = px.histogram(df, x="Sales", nbins=20, title="Phân bố của Sales")
        
        # 5. Pie Chart: Phân bố số lượng theo Category
        cat_count = df['Category'].value_counts().reset_index()
        cat_count.columns = ['Category', 'Count']
        fig_pie = px.pie(cat_count, names='Category', values='Count', title="Phân bố Category")
        
        # 6. Altair Area Chart: Doanh số theo thời gian (biểu đồ vùng)
        chart_altair = alt.Chart(df).mark_area(color='lightblue').encode(
            x=alt.X('Date:T', title="Ngày"),
            y=alt.Y('Sales:Q', title="Doanh số")
        ).properties(title="Altair Area Chart: Doanh số theo thời gian")
        
        # ----------------------------
        # Sắp xếp giao diện dạng lưới (grid layout)
        # ----------------------------
        st.markdown("## Row 1: Biểu đồ đường & Biểu đồ cột")
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig_line, use_container_width=True)
        with col2:
            st.plotly_chart(fig_bar, use_container_width=True)
        
        st.markdown("## Row 2: Biểu đồ phân tán & Histogram")
        col3, col4 = st.columns(2)
        with col3:
            st.plotly_chart(fig_scatter, use_container_width=True)
        with col4:
            st.plotly_chart(fig_hist, use_container_width=True)
        
        st.markdown("## Row 3: Pie Chart & Altair Area Chart")
        col5, col6 = st.columns(2)
        with col5:
            st.plotly_chart(fig_pie, use_container_width=True)
        with col6:
            st.altair_chart(chart_altair, use_container_width=True)

import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="Well Shop", layout="wide")

# Path to the image in the 'image' folder
image_path = os.path.join(os.getcwd(), "image/1.jpeg")

# Custom CSS styles
st.markdown(f"""
    <style>
        html, body, [class*="st-emotion-cache"] {{
            font-family: 'Arial', sans-serif;
            background-color: #f7f7f7;
        }}

        .title {{
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }}

        .banner {{
            width: 100%;
            height: 250px;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 3px 5px 15px rgba(0, 0, 0, 0.2);
            overflow: hidden;
            position: relative;
            margin-bottom: 40px;
        }}

        .banner img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 20px;
            opacity: 0.85;
        }}

        .banner-text {{
            position: absolute;
            font-size: 32px;
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
        }}

        .subtitle {{
            font-size: 26px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            color: #444;
        }}

        .product-box {{
            width: 100%;
            border-radius: 15px;
            box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.1);
            padding: 15px;
            text-align: center;
            background: white;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-bottom: 20px;
        }}

        .product-box img {{
            width: 100%;
            height: 160px;
            object-fit: cover;
            border-radius: 10px;
        }}

        .product-box:hover {{
            transform: scale(1.05);
            box-shadow: 4px 6px 12px rgba(0, 0, 0, 0.2);
        }}

        .product-name {{
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
        }}

        .product-price {{
            font-size: 14px;
            color: #E44D26;
            font-weight: bold;
        }}
    </style>
""", unsafe_allow_html=True)

# Store title
st.markdown("<div class='title'>Well Shop</div>", unsafe_allow_html=True)

# Promotional banner
st.markdown(f"""
    <div class='banner'>
        <img src='{image_path}' alt='Promotion'>
        <div class='banner-text'>🔥 Special Promotion - Limited Time! 🔥</div>
    </div>
""", unsafe_allow_html=True)

# Product section title
st.markdown("<div class='subtitle'>Our Products</div>", unsafe_allow_html=True)

# Product list
products = [
    {"name": "Nike Sneakers", "price": "$120", "image": image_path},
    {"name": "Luxury Watch", "price": "$250", "image": image_path},
    {"name": "Leather Bag", "price": "$180", "image": image_path},
    {"name": "Wireless Headphones", "price": "$90", "image": image_path},
    {"name": "Stylish Sunglasses", "price": "$60", "image": image_path},
    {"name": "Gaming Laptop", "price": "$1500", "image": image_path},
    {"name": "Smartphone", "price": "$799", "image": image_path},
    {"name": "Digital Camera", "price": "$550", "image": image_path},
    {"name": "Gaming Console", "price": "$499", "image": image_path},
    {"name": "Mechanical Keyboard", "price": "$120", "image": image_path},
    {"name": "Wireless Mouse", "price": "$40", "image": image_path},
    {"name": "4K Monitor", "price": "$350", "image": image_path},
    {"name": "Luxury Perfume", "price": "$75", "image": image_path},
    {"name": "Premium Coffee Beans", "price": "$25", "image": image_path},
    {"name": "Portable Speaker", "price": "$99", "image": image_path},
    {"name": "Mountain Bike", "price": "$800", "image": image_path},
]

# Display products in a 4x4 grid
rows = 4
cols = 4
index = 0

for _ in range(rows):
    col_group = st.columns(cols)
    for col in col_group:
        if index < len(products):
            product = products[index]
            with col:
                st.markdown(f"""
                    <div class='product-box'>
                        <img src='{product["image"]}' alt='{product["name"]}'>
                        <div class='product-name'>{product["name"]}</div>
                        <div class='product-price'>{product["price"]}</div>
                    </div>
                """, unsafe_allow_html=True)
            index += 1

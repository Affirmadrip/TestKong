import streamlit as st
import os

# Set the page configuration and title
st.set_page_config(page_title="Well Shop", layout="wide")

# Construct the path to the image file
image_path = os.path.join("image", "1.png")

# Check if the image file exists
if not os.path.exists(image_path):
    st.error(f"Image not found: {image_path}")
else:
    # CSS styles for the page
    st.markdown("""
        <style>
            html, body, [class*="st-emotion-cache"] {
                font-family: 'Arial', sans-serif;
                background-color: #f7f7f7;
            }
            .title {
                font-size: 40px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 30px;
                color: #333;
            }
            .banner {
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
            }
            .banner img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                border-radius: 20px;
                opacity: 0.85;
            }
            .banner-text {
                position: absolute;
                font-size: 32px;
                font-weight: bold;
                color: white;
                text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
            }
            .subtitle {
                font-size: 26px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
                color: #444;
            }
            .product-box {
                width: 100%;
                border-radius: 15px;
                box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.1);
                padding: 15px;
                text-align: center;
                background: white;
                transition: transform 0.2s, box-shadow 0.2s;
                margin-bottom: 20px;
            }
            .product-box img {
                width: 100%;
                height: 160px;
                object-fit: cover;
                border-radius: 10px;
            }
            .product-box:hover {
                transform: scale(1.05);
                box-shadow: 4px 6px 12px rgba(0, 0, 0, 0.2);
            }
            .product-name {
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            .product-price {
                font-size: 14px;
                color: #E44D26;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # Display the shop title
    st.markdown("<div class='title'>Well Shop</div>", unsafe_allow_html=True)

    # Display the promotional banner
    st.markdown("""
        <div class='banner'>
            <img src='data:image/png;base64,{image_path}' alt='Promotion'>
            <div class='banner-text'>🔥 Special Promotion - Limited Time! 🔥</div>
        </div>
    """, unsafe_allow_html=True)

    # Display the product section title
    st.markdown("<div class='subtitle'>Our Products</div>", unsafe_allow_html=True)

    # Define a list of products
    products = [
        {"name": "Nike Sneakers", "price": "$120"},
        {"name": "Luxury Watch", "price": "$250"},
        {"name": "Leather Bag", "price": "$180"},
        {"name": "Wireless Headphones", "price": "$90"},
        {"name": "Stylish Sunglasses", "price": "$60"},
        {"name": "Gaming Laptop", "price": "$1500"},
        {"name": "Smartphone", "price": "$799"},
        {"name": "Digital Camera", "price": "$550"},
        {"name": "Gaming Console", "price": "$499"},
        {"name": "Mechanical Keyboard", "price": "$120"},
        {"name": "Wireless Mouse", "price": "$40"},
        {"name": "4K Monitor", "price": "$350"},
        {"name": "Luxury Perfume", "price": "$75"},
        {"name": "Premium Coffee Beans", "price": "$25"},
        {"name": "Portable Speaker", "price": "$99"},
        {"name": "Mountain Bike", "price": "$800"},
    ]

    # Display the products in a grid
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
                            <img src='data:image/png;base64,{image_path}' alt='{product["name"]}'>
                            <div class='product-name'>{product["name"]}</div>
                            <div class='product-price'>{product["price"]}</div>
                        </div>
                    """, unsafe_allow_html=True)
                index += 1

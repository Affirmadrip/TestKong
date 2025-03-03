import streamlit as st

# ตั้งค่าหน้าหลัก
st.set_page_config(page_title="Well Shop", layout="wide")

# URL หรือ path ของภาพโปรโมชั่น
promo_image = "data:image/jpeg;base64,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"

# สไตล์ CSS ที่ปรับปรุงใหม่
st.markdown(f"""
    <style>
        html, body, [class*="st-emotion-cache"] {{
            font-family: 'Arial', sans-serif;
            background-color: #f7f7f7;
        }}

        /* ชื่อร้าน */
        .title {{
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }}

        /* แบนเนอร์ */
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

        /* รูปภาพโปรโมชั่น */
        .banner img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 20px;
            opacity: 0.85;
        }}

        /* ข้อความบนแบนเนอร์ */
        .banner-text {{
            position: absolute;
            font-size: 32px;
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
        }}

        /* หัวข้อสินค้า */
        .subtitle {{
            font-size: 26px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            color: #444;
        }}

        /* กล่องสินค้า */
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

        /* ชื่อสินค้า */
        .product-name {{
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
        }}

        /* ราคาสินค้า */
        .product-price {{
            font-size: 14px;
            color: #E44D26;
            font-weight: bold;
        }}
    </style>
""", unsafe_allow_html=True)

# ชื่อร้าน
st.markdown("<div class='title'>Well Shop</div>", unsafe_allow_html=True)

# แบนเนอร์ พร้อมภาพโปรโมชั่น
st.markdown(f"""
    <div class='banner'>
        <img src='{promo_image}' alt='Promotion'>
        <div class='banner-text'>🔥 Special Promotion - Limited Time! 🔥</div>
    </div>
""", unsafe_allow_html=True)

# หัวข้อสินค้า
st.markdown("<div class='subtitle'>Our Products</div>", unsafe_allow_html=True)

# รายการสินค้า
image_path = "image/1.jpeg"  # Use the same image for all products

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


# แสดงสินค้าเป็นตาราง 4×4 พร้อมเพิ่มระยะห่าง
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


import streamlit as st
import requests
import json

# Page setting
st.set_page_config(
    page_title="ImmoEliza House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# API URL
api_url = "https://immoeliza-api-cloris-f-chen.onrender.com/predict"

# Page information
st.title("🏠 ImmoEliza House Price Predictor")
st.markdown("### AI-Powered Belgian Real Estate Price Prediction")

# Sidebar information
st.sidebar.markdown("## 📋 API Information")
st.sidebar.markdown("**API Endpoint:** '/Predict'")
st.sidebar.markdown("**Method:** POST")
st.sidebar.markdown("**Response:** JSON with price prediction")
st.sidebar.markdown("-----")
st.sidebar.markdown("**Team Project:** Indivadual branch 'Cloris_F_Chen_Deployment'")
st.sidebar.markdown("**Developer:**Cloris F. Chen")

# Area of main content. Two columns
col1,col2 = st.columns([1,1])

with col1:
    st.markdown("## 🏡 Property Details")

    # Required fields
    st.markdown("### Required Fields")
    area = st.number_input("Living Area(m²)",min_value=1, value= 120,step=1)
    property_type = st.selectbox("Property Type",["HOUSE","APARTMENT","OTHERS"])
    bedrooms = st.number_input("Number of Bedrooms",min_value=0,value=3,step=1)
    zip_code = st.number_input("ZIP Code",min_value=1000,max_value=9999,value=1000,step=1)

    # Optional fields
    st.markdown("### Optional Fields (Improve Accuracy)")

    col1_1,col1_2 = st.columns(2)

    with col1_1:
        garden = st.checkbox("Has Garden")
        swimming_pool = st.checkbox("Has Swimming Pool")
        terrace = st.checkbox("Has Terrace")

    with col1_2:
        parking = st.checkbox("Has Parking")
        lift = st.checkbox("Has Lift")

    building_state = st.selectbox(
        "Building State",
        ["None", "NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO BE DONE UP", "TO REBUILD"]
    )

    epc_score = st.selectbox(
        "EPC Score", 
        ["None", "A++", "A+", "A", "B", "C", "D", "E", "F", "G"]
    )

with col2:
    st.markdown("## 🎯 Prediction Results")

    # Prediction button
    if st.button("🔮 Predict Price", type="primary",use_container_width=True) :
        # Create request data
        data = {
                "data":{
                    "area":area,
                    "property-type":property_type,
                    "bedrooms-number":bedrooms,
                    "zip-code":zip_code
                    }
            }

        # Add optional fields
        if garden:
            data["data"]["garden"] = garden
        if swimming_pool:
            data["data"]["swimming-pool"] = swimming_pool
        if terrace:
            data["data"]["terrace"] = terrace
        if parking:
            data["data"]["parking"] = parking
        if lift:
            data["data"]["lift"] = lift
        if building_state != "None":
            data["data"]["building-state"] = building_state
        if epc_score != "None":
            data["data"]["epc-score"] = epc_score

        # Show request data
        st.markdown("### 📤 Request Data")
        st.json(data)

        # Send request
        try:
            with st.spinner("🔄 Predicting price...") :
                response = requests.post(api_url, json=data, timeout=30)
            if response.status_code == 200 :
                result = response.json()
                if result.get("prediction") is not None:
                    # Successfully predict
                    price = result["prediction"]
                    st.success(f"✅ Prediction Successful!")
                    st.markdown("### 💰 Predicted Price")
                    st.markdown(f"# €{price:,.2f}")

                    # Show response
                    st.markdown("### 📥 API Response")
                    st.json(result)

                    # Price analysis
                    st.markdown("### 📊 Price Analysis")
                    col2_1, col2_2, col2_3 = st.columns(3)
                        
                    with col2_1:
                        st.metric("Price per m²", f"€{price/area:,.0f}")
                    
                    with col2_2:
                        if bedrooms > 0:
                            st.metric("Price per Bedroom", f"€{price/bedrooms:,.0f}")
                        else:
                            st.metric("Price per Bedroom", "N/A")
                        
                    with col2_3:
                        # Predict from region
                        if 1000 <= zip_code <= 1299:
                            region = "Brussels"
                            avg_price = 400000
                        elif zip_code >= 9000:
                            region = "Ghent area"
                            avg_price = 350000
                        else:
                            region = "Other regions"
                            avg_price = 300000
                        
                        comparison = "Above" if price > avg_price else "Below"
                        st.metric(f"vs {region} avg", f"{comparison} average")

                else:
                    st.error("❌ Prediction failed")
                    st.json(result)
            else:
                st.error(f"❌ API Error: {response.status_code}")
                try:
                    error_data = response.json()
                    st.json(error_data)
                except:
                    st.text(response.text)
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection Error: {str(e)}")
            st.info("💡 The API might be starting up. Please wait 30-60 seconds and try again.")
    else:
        # Show imformation if no click
        st.info("👆 Click the 'Predict Price' button to get a house price prediction!")
        st.markdown("### 📋 Instructions")
        st.markdown("1. Fill in the required fields above")
        st.markdown("2. Optionally, add more details for better accuracy")
        st.markdown("3. Click 'Predict Price' to get your result")
        st.markdown("4. View the prediction and analysis below")

# Bottom Information 
st.markdown("---")
st.markdown("### 📚 API Documentation")
st.markdown("For complete API documentation and testing, visit:")
st.markdown("🔗 [Interactive API Docs](https://immoeliza-api-cloris-f-chen.onrender.com/docs)")
# ImmoEliza House Price Predictor - Interactive Demo

## 🎯 Overview

This is an interactive web interface for the **ImmoEliza House Price Prediction API**, built with Streamlit. It provides a user-friendly way to test the machine learning API without requiring any coding knowledge.

## 🔗 Related Projects

- **Main API Repository**: [ImmoEliza_API_Cloris_F_Chen](https://github.com/Cloris-la/ImmoEliza_API_Cloris_F_Chen)
- **Live API**: https://immoeliza-api-cloris-f-chen.onrender.com
- **API Documentation**: https://immoeliza-api-cloris-f-chen.onrender.com/docs

## 🚀 Live Demo

**🌐 [Try the Interactive Demo](https://immoelizaapiclorisfchendemo-tektqwghdn2s458cdxgaxe.streamlit.app/)**

## 📋 Features

### ✅ **User-Friendly Interface**
- Interactive form with all required and optional fields
- Real-time input validation
- Clear field descriptions and examples

### ✅ **Real-Time API Integration**
- Calls the live ImmoEliza API
- Displays request and response data
- Shows detailed error messages

### ✅ **Price Analysis**
- Predicted house price in EUR
- Price per square meter calculation
- Price per bedroom analysis

### ✅ **Professional Presentation**
- Clean, modern interface
- Responsive design
- Real-time loading indicators

## 🏠 How to Use

### 1. **Required Fields**
Fill in the mandatory information:
- **Living Area**: Property size in square meters
- **Property Type**: HOUSE, APARTMENT, or OTHERS
- **Bedrooms**: Number of bedrooms
- **ZIP Code**: Belgian postal code (1000-9999)

### 2. **Optional Fields** (Improve Accuracy)
Add additional details for better predictions:
- Garden, Swimming Pool, Terrace
- Parking, Elevator
- Building State, EPC Score

### 3. **Get Prediction**
- Click "Predict Price" button
- View the predicted price and analysis
- See the API request/response data

## 🛠️ Technical Details

### **Built With**
- **Streamlit** - Web interface framework
- **Requests** - API communication
- **Python 3.10+** - Programming language

### **API Integration**
- **Endpoint**: `https://immoeliza-api-cloris-f-chen.onrender.com/predict`
- **Method**: POST
- **Format**: JSON
- **Response**: Price prediction with status code

### **Features**
- Error handling for API failures
- Loading states and user feedback
- Input validation and formatting
- Responsive layout design

## 🚀 Local Development

### **Prerequisites**
- Python 3.10 or higher
- pip package manager

### **Installation**
```bash
# Clone the repository
git clone https://github.com/Cloris-la/ImmoEliza_API_Cloris_F_Chen_Demo.git
cd immoeliza-streamlit-demo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run streamlit_app.py
```

### **Access**
- **Local URL**: http://localhost:8501
- **Network URL**: http://your-ip:8501

## 📦 Deployment

### **Streamlit Cloud**
1. Push code to GitHub repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select repository and main file (`streamlit_app.py`)
5. Deploy automatically

### **Requirements**
The app will automatically install:
- `streamlit`
- `requests`

## 🎨 Interface Preview

The interface includes:
- **Input Form**: Easy-to-use property details form
- **Prediction Results**: Clear price display with analysis
- **API Response**: Technical details for developers
- **Documentation Link**: Access to full API documentation

## 📖 API Documentation

For complete API documentation and technical details, visit:
- **Interactive Docs**: https://immoeliza-api-cloris-f-chen.onrender.com/docs
- **API Repository**: [ImmoEliza_API_Cloris_F_Chen](https://github.com/Cloris-la/ImmoEliza_API_Cloris_F_Chen)

## 🤝 Team Project Context

This project is part of a three-person team collaboration. Each team member developed their own API requirements and build their streamlit app. [main repository](https://github.com/Cloris-la/challenge-api-deployment). This current streamlit app is developed in the Cloris_F_Chen_Deployment branch as my individual contribution to the team project. This Streamlit app demonstrates:
- **API Integration**: How to consume the machine learning API
- **User Experience**: Making ML predictions accessible to non-technical users
- **Professional Presentation**: Creating polished demos for stakeholders

## 🔧 Configuration

### **API Settings**
- **Base URL**: `https://immoeliza-api-cloris-f-chen.onrender.com`
- **Timeout**: 30 seconds
- **Retry Logic**: Automatic error handling

### **UI Settings**
- **Theme**: Streamlit default
- **Layout**: Wide mode
- **Page Icon**: 🏠
- **Page Title**: ImmoEliza House Price Predictor

## 📝 Usage Examples

### **Basic Prediction**
```json
{
  "data": {
    "area": 120,
    "property-type": "HOUSE",
    "bedrooms-number": 3,
    "zip-code": 1000
  }
}
```

### **Detailed Prediction**
```json
{
  "data": {
    "area": 150,
    "property-type": "APARTMENT",
    "bedrooms-number": 2,
    "zip-code": 2000,
    "garden": true,
    "terrace": true,
    "building-state": "GOOD",
    "epc-score": "B"
  }
}
```

## 🐛 Troubleshooting

### **Common Issues**

1. **API Connection Error**
   - Check if API is running
   - Verify URL is correct
   - Wait for cold start (30-60 seconds)

2. **Prediction Failed**
   - Ensure all required fields are filled
   - Check ZIP code format (1000-9999)
   - Verify property type spelling

3. **Slow Response**
   - API may be starting up (first request)
   - Free tier has cold start delays
   - Wait and try again

## 📊 Performance

- **Response Time**: 1-3 seconds (after warm-up)
- **Cold Start**: 30-60 seconds (first request)
- **Availability**: 24/7 (subject to Render free tier limits)

## 🔮 Future Enhancements

- [ ] Add data visualization charts
- [ ] Include property photos upload
- [ ] Add batch prediction capability
- [ ] Implement user authentication
- [ ] Add prediction history

## 👨‍💻 Developer

**Cloris F. Chen**  
- **API Repository**: [ImmoEliza_API_Cloris_F_Chen](https://github.com/Cloris-la/ImmoEliza_API_Cloris_F_Chen)
- **Demo Repository**: [ImmoEliza Streamlit Demo](https://github.com/Cloris-la/ImmoEliza_API_Cloris_F_Chen_Demo)

## 📄 License

This project is part of an educational assignment and team collaboration.

---

**Built with : using Streamlit and the ImmoEliza API**
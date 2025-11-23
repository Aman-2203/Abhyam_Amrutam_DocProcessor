# Abhayam Amrutam Services (AAS)

A Flask-based document processing platform that provides AI-powered proofreading, translation, and OCR services with integrated payment processing and user authentication.

## Features

### Document Processing Modes
- **Mode 1: Proofreading** - AI-powered grammar and spelling correction using Google Gemini
- **Mode 2: Translation** - Multi-language translation with support for Sanskrit and other languages
- **Mode 3: OCR** - Extract text from scanned PDFs and images using Google Vision API

### Key Capabilities
- **OTP-based Authentication** - Secure email-based login system
- **Razorpay Payment Integration** - Per-page pricing with secure payment processing
- **Free Trial System** - 3 free pages per tool for new users
- **Email Delivery** - Processed documents sent directly to user's email
- **Parallel Processing** - Multi-threaded document processing for faster results


## Prerequisites

- Python 3.8 or higher
- MongoDB database
- Google Gemini API key
- Google Vision API key
- Razorpay account (for payments)
- Gmail account with App Password (for OTP emails)

## Installation



### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the root directory with the following variables:

```env
# Google AI API Keys
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_VISION_API_KEY=your_vision_api_key_here

# Email Configuration (for OTP)
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password_here

# MongoDB Configuration
MONGODB_URI=your_mongodb_connection_string
MONGO_DB=your_database_name

# Razorpay Credentials
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret
```

```

## Running the Application
python app.py
```

The application will be available at `http://localhost:8080`


## Project Structure

```
AAS_CLONE/
├── app.py                  # Main Flask application
├── auth.py                 # Authentication and OTP handling
├── config.py               # Configuration and constants
├── db_config.py            # MongoDB connection setup
├── document_handler.py     # Document processing orchestration
├── payment_handler.py      # Razorpay payment integration
├── processors.py           # AI processing classes (Proofreading, Translation, OCR)
├── utils.py                # Utility functions for document manipulation
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in git)
├── templates/              # HTML templates
│   ├── index.html         # Main processing interface
│   ├── login.html         # Login page
│   ├── feature.html       # Features page
│   ├── pricing.html       # Pricing information
│   └── contactus.html     # Contact page
├── static/                 # Static assets (CSS, JS, images)
├── uploads/                # Temporary file uploads
└── outputs/                # Processed documents
```




## API Endpoints

### Authentication
- `GET /login` - Login page
- `POST /send-otp` - Send OTP to email
- `POST /verify-otp` - Verify OTP and create session
- `GET /logout` - Logout user

### Document Processing
- `GET /mode/<mode_num>` - Processing interface for specific mode
- `POST /process` - Upload and process document
- `GET /progress/<job_id>` - Get processing progress
- `GET /download/<filename>` - Download processed file
- `POST /send-document/<job_id>` - Email processed document

### Payment
- `POST /create-payment` - Create Razorpay order
- `POST /verify-payment` - Verify payment signature

### Pages
- `GET /` - Home page
- `GET /feature` - Features page
- `GET /pricing` - Pricing page
- `GET /contactus` - Contact page


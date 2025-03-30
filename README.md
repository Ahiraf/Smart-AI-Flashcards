###### Smart AI Flashcards #####

### 📌 Overview

Smart AI Flashcards is a project that automatically generates flashcards using AI. It processes PDFs, extracts key terms and meanings, and creates visually appealing flashcards with images which are helpful for students to learn something in a short period of time!

### 🚀 Features

***🤖 AI-Powered Extraction:*** Uses Google's Gemini AI to extract key terms and definitions from PDFs.

***🖼️ Image-Based Flashcards:*** Converts extracted data into beautifully designed images.

***📝 Custom Prompts:*** Allows users to define their own AI prompts for better term extraction.

***🔒 Secure API Handling:*** Keeps API keys safe by using environment variables.

### 🔧 Installation & Setup

***1️⃣ Clone the Repository***

git clone https://github.com/yourusername/Smart-AI-Flashcards.git
cd Smart-AI-Flashcards

***2️⃣ Create a Virtual Environment (Optional but Recommended)***

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

***3️⃣ Install Dependencies***

pip install -r requirements.txt

***4️⃣ Set Up API Key***

Store your GEMINI_API_KEY securely:

export GEMINI_API_KEY='your_api_key_here'  # macOS/Linux
set GEMINI_API_KEY='your_api_key_here'  # Windows

Alternatively, add it to your .bashrc or .zshrc file for persistent access.

### 📜 Usage

***1️⃣ Place Your PDF***

Save your study material as a PDF in the /data folder.

***2️⃣ Run the Script***

python Code.py

<img width="1272" alt="Screenshot 2025-03-28 at 4 39 48 PM" src="https://github.com/user-attachments/assets/e74cd4b8-5cd4-41f5-88b3-6710d25fb95d" />

<img width="1272" alt="Screenshot 2025-03-28 at 4 40 34 PM" src="https://github.com/user-attachments/assets/e9ec52b4-ad07-4914-ae63-0150f7ce18a4" />


## This will generate flashcards inside the /output folder,like the followings :

![Statistics](https://github.com/user-attachments/assets/5fdd14bf-49ae-439d-8bc8-092eefcda278)

![Cumulative Frequency curve or Ogive](https://github.com/user-attachments/assets/8cbf41cb-be96-4955-bc1e-4ac261b3e700)

![Kurtosis](https://github.com/user-attachments/assets/a6303597-7b17-444d-a2ce-73818bb171cc)


***📂 Project Structure***

Smart-AI-Flashcards/
├── data/            # Folder for PDFs
├── Output/          # Generated flashcards (images)
├── Code.py          # Main script to process PDF and create flashcards
├── create_image.py  # Script to generate images
├── requirements.txt # Dependencies
├── .gitignore       # Ignores sensitive files
├── README.md        # This file

🛠️ Technologies Used

=> Python 🐍
=> Google Gemini AI 🤖
=> Pillow (PIL) 🎨
=> Textwrap 📝

### 📬 Contributions & Feedback

Feel free to open issues, contribute, or suggest improvements! 😊


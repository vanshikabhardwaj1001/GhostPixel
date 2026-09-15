# 👻 GhostPixel

**GhostPixel** is a Python-based image steganography tool designed to securely hide secret messages inside images and retrieve them when needed.

The project combines **image steganography, cryptography, image analysis, and a command-line interface** into one lightweight cybersecurity tool.

> **GhostPixel: Hide the message. Leave the image looking normal.**

---

## 📌 Overview

Steganography is the practice of hiding information inside another medium so that the existence of the hidden information is difficult to notice.

GhostPixel uses images as the carrier medium. A secret message can be embedded into an image and later extracted using the decoder.

The project also provides functionality for detecting potential hidden data and inspecting image properties.

### 🔐 Main workflow

```text
                  ┌──────────────────┐
                  │     GhostPixel   │
                  └────────┬─────────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
          Encoding      Decoding      Detection
             │             │             │
             ▼             ▼             ▼
          Image +       Hidden         Analyze
          Message       Message        Image
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                     Image Analysis
```

---

# ✨ Features

GhostPixel currently provides the following features:

### 1. 🔒 Encode Secret Message

Hide a secret text message inside an image.

```text
Image + Secret Message
        ↓
   GhostPixel
        ↓
Image containing hidden data
```

The resulting image can be saved as a new output file.

---

### 2. 🔓 Decode Secret Message

Extract a previously hidden message from a steganographic image.

```text
Steganographic Image
        ↓
   GhostPixel
        ↓
   Hidden Message
```

---

### 3. 🕵️ Detect Hidden Data

Analyze an image for indicators that may suggest the presence of hidden information.

This feature is intended as an educational detection mechanism and should not be considered a guaranteed forensic steganalysis solution.

---

### 4. 🖼️ Image Information

Display useful information about an image, such as:

* Image format
* Image dimensions
* Image mode
* Image size
* Other available image properties

---

### 5. 📖 Help / About

Provides information about GhostPixel, its functionality, and how to use the available options.

---

### 6. 🚪 Exit

Safely exits the application.

---

# 🖥️ Application Menu

When GhostPixel starts, users are presented with:

```text
========================================
            GHOSTPIXEL 👻
       IMAGE STEGANOGRAPHY TOOL
========================================

1. Encode secret message
2. Decode secret message
3. Detect hidden data
4. Image information
5. Help/About
6. Exit
```

---

# 🛠️ Technologies Used

GhostPixel is built using:

| Technology   | Purpose                                     |
| ------------ | ------------------------------------------- |
| Python       | Core programming language                   |
| Pillow       | Image processing and manipulation           |
| Cryptography | Message protection/encryption functionality |
| CLI          | User interaction                            |

---

# 📂 Project Structure

```text
GhostPixel/
│
├── ghostpixel.py       # Main application and menu
├── encoder.py          # Message encoding functionality
├── decoder.py          # Message decoding functionality
├── crypto.py           # Cryptographic functionality
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── LICENSE             # MIT License
├── .gitignore          # Git ignored files
│
├── screenshots/        # Project screenshots
│
└── output/             # Generated output images
```

---

# ⚙️ Installation

## Prerequisites

Before running GhostPixel, make sure you have:

* Python 3.x
* pip
* Git (optional, for development/version control)

Check your Python installation:

```bash
python --version
```

Check pip:

```bash
pip --version
```

---

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/GhostPixel.git
```

Move into the project directory:

```bash
cd GhostPixel
```

Replace `YOUR-USERNAME` with your GitHub username.

---

## 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Start GhostPixel using:

```bash
python ghostpixel.py
```

The application will display the main menu.

---

## 🔒 Encoding a Message

Select:

```text
1. Encode secret message
```

The program will ask for the required image and message information.

Example:

```text
Enter input image path:
Enter secret message:
Enter output image path:
```

GhostPixel then creates an output image containing the hidden message.

---

## 🔓 Decoding a Message

Select:

```text
2. Decode secret message
```

Provide the image containing the hidden data.

GhostPixel will attempt to extract the embedded message.

---

## 🕵️ Detecting Hidden Data

Select:

```text
3. Detect hidden data
```

Provide the image you want to analyze.

GhostPixel will perform its implemented checks and report whether hidden data may be present.

> Detection results should be treated as indicators rather than definitive proof of steganography.

---

## 🖼️ Viewing Image Information

Select:

```text
4. Image information
```

Provide the image path.

GhostPixel displays available image metadata and properties.

---

# 🔐 Security Concept

GhostPixel demonstrates an important cybersecurity concept:

**Data can be hidden without visibly changing the carrier medium in an obvious way.**

Traditional encryption attempts to make the contents of a message unreadable.

Steganography attempts to make the existence of the message less obvious.

These concepts can also be combined:

```text
             Secret Message
                   │
                   ▼
             Cryptography
                   │
                   ▼
          Encrypted Message
                   │
                   ▼
            Steganography
                   │
                   ▼
              Image File
```

This layered approach demonstrates how cryptographic protection and information hiding can complement each other.

---

# 🧠 How Image Steganography Works

A common image steganography technique is **Least Significant Bit (LSB) steganography**.

Digital images contain pixel values.

For example:

```text
Pixel value:

10110110
```

The least significant bit is:

```text
1011011[0]
        ↑
       LSB
```

Changing this bit produces:

```text
10110111
```

The visual difference is generally extremely small.

By modifying selected least significant bits across many pixels, binary message data can be embedded into an image.

Conceptually:

```text
Secret Message
      ↓
Convert to Binary
      ↓
10110100 01101000 ...
      ↓
Modify Image Pixel Bits
      ↓
Steganographic Image
```

The exact implementation used by GhostPixel is defined by the project's encoder and decoder modules.

---

# 🔍 Detection Concept

Steganography can leave statistical or structural indicators in an image.

Detection techniques may examine things such as:

* Pixel distributions
* Image properties
* Unusual modifications
* Embedded markers
* File structure
* Statistical anomalies

GhostPixel's detection functionality is primarily designed for **educational and demonstration purposes**.

It should not be considered a complete professional steganalysis framework.

---

# 🧪 Example Use Case

Imagine Alice wants to send Bob a secret message.

Instead of sending:

```text
Meet me at 8 PM.
```

directly, Alice can use GhostPixel to embed the message inside an ordinary image.

```text
                Alice
                  │
                  ▼
          Secret Message
                  │
                  ▼
             GhostPixel
                  │
                  ▼
          Normal-looking Image
                  │
                  ▼
                Bob
                  │
                  ▼
             GhostPixel
                  │
                  ▼
          Extracted Message
```

The image can then be transferred like a normal image file.

---

# 📸 Screenshots

Screenshots demonstrating GhostPixel's functionality can be added here.

### Main Menu

```text
Add screenshot here
```

### Encoding

```text
Add screenshot here
```

### Decoding

```text
Add screenshot here
```

### Detection

```text
Add screenshot here
```

### Image Information

```text
Add screenshot here
```

---

# 🚀 Future Improvements

Possible future versions of GhostPixel could include:

* [ ] GUI interface
* [ ] Drag-and-drop image support
* [ ] Password-protected encoding
* [ ] Stronger encryption integration
* [ ] Support for additional image formats
* [ ] Batch encoding and decoding
* [ ] Advanced steganalysis
* [ ] Statistical LSB analysis
* [ ] Image comparison tools
* [ ] File hiding support
* [ ] Better error handling
* [ ] Logging and audit functionality
* [ ] Unit tests
* [ ] Automated testing
* [ ] Cross-platform executable release
* [ ] Docker support

---

# 🎯 Learning Objectives

This project demonstrates practical concepts related to:

* Python programming
* Cybersecurity
* Information hiding
* Image processing
* Cryptography
* Binary data
* File handling
* Command-line applications
* Security analysis

---

# ⚠️ Disclaimer

GhostPixel is intended for **educational, research, and authorized security testing purposes**.

Do not use this software to conceal, transfer, or extract information without proper authorization.

The developer is not responsible for misuse of this software.

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve GhostPixel:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Test the changes.
5. Commit your changes.

```bash
git commit -m "Add new feature"
```

6. Push the branch.

```bash
git push origin feature/new-feature
```

7. Open a Pull Request.

---

# 📜 License

GhostPixel is released under the **MIT License**.

See the `LICENSE` file for more information.

---

# 👩‍💻 Author

**Vanshika**

Cybersecurity student interested in:

* Defensive Security
* SOC Operations
* Network Security
* Cybersecurity Tools
* Security Monitoring
* Ethical Hacking

---

# ⭐ Support

If you find GhostPixel useful for learning or experimentation, consider giving the repository a ⭐ on GitHub.

---

## 👻 GhostPixel

**Hide information. Analyze images. Explore cybersecurity.**

```text
██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
██║  ███╗███████║██║   ██║███████╗   ██║
██║   ██║██╔══██║██║   ██║╚════██║   ██║
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝

        IMAGE STEGANOGRAPHY TOOL
```


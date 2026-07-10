
# 🖼️ VisionCanvas-OpenCV

An interactive **OpenCV + Streamlit** application for real-time image processing. Upload any image and instantly visualize multiple computer vision operations with adjustable parameters through a simple web interface.

---

## ✨ Features

* 📤 Upload images (PNG, JPG, JPEG, BMP, WEBP)
* 🎨 Original Image Preview
* ⚫ Grayscale Conversion
* 🌫 Gaussian Blur
* 🎯 Otsu Automatic Thresholding
* ✂️ Canny Edge Detection
* 🌑 Negative Image Transformation
* 📏 Adjustable Image Resize
* 🎛 Interactive Sidebar Controls
* 📥 Download Processed Output
* 🖥 Grid View & Separate View Modes
* ⚡ Fast and Responsive Interface

---

## 🛠 Technologies Used

* Python
* OpenCV
* Streamlit
* NumPy

---

## 📂 Project Structure

```
VisionCanvas-OpenCV/
│
├── app.py
├── requirements.txt
├── README.md
└── images/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/MUBARAK-53/VisionCanvas-OpenCV.git
```

Move into the project directory

```bash
cd VisionCanvas-OpenCV
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
opencv-python
numpy
```

or install manually

```bash
pip install streamlit opencv-python numpy
```

---

## 🎛 Available Controls

| Control              | Purpose                        |
| -------------------- | ------------------------------ |
| Resize Width         | Resize uploaded image width    |
| Resize Height        | Resize uploaded image height   |
| Gaussian Kernel      | Blur intensity                 |
| Canny Low Threshold  | Lower edge detection threshold |
| Canny High Threshold | Upper edge detection threshold |
| Display Mode         | Grid or Separate View          |

---

## 🖼 Image Processing Operations

### Original

Displays the uploaded image.

### Grayscale

Converts the RGB image into a single-channel grayscale image.

### Gaussian Blur

Smooths the image to reduce noise before edge detection.

### Otsu Threshold

Automatically determines the optimal threshold value for binary segmentation.

### Canny Edge Detection

Highlights object boundaries using gradient-based edge detection.

### Negative Image

Creates the photographic negative by inverting pixel intensities.

---

## 📥 Output

The application generates a combined image containing all processed outputs.

Users can download the generated result as a PNG image with a single click.

---

## 💡 Future Improvements

* Histogram Equalization
* Adaptive Thresholding
* Morphological Operations
* Contour Detection
* Face Detection
* Object Detection
* Image Segmentation
* Color Space Conversion
* Background Removal
* Live Webcam Processing

---

## 🎯 Applications

* Computer Vision Learning
* Digital Image Processing
* Academic Projects
* OpenCV Practice
* Image Analysis
* Edge Detection Demonstrations
* Image Enhancement

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Mubarak Naikwade**

B.Tech Computer Science Engineering

Passionate about Computer Vision, OpenCV, Machine Learning, and AI Applications.

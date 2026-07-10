import cv2 as cv
import numpy as np
import streamlit as st

st.set_page_config(page_title="OpenCV Image Processor", page_icon="🖼️", layout="wide")

st.title("OpenCV Multi-Image Processor")
st.write("Upload an image to generate Original, Grayscale, Gaussian Blur, Otsu Threshold, Canny Edge, and Negative outputs.")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg", "bmp", "webp"])

resize_width = st.sidebar.slider("Resize width", 100, 800, 300, 10)
resize_height = st.sidebar.slider("Resize height", 100, 800, 300, 10)
blur_kernel = st.sidebar.select_slider("Gaussian blur kernel", options=[3, 5, 7, 9], value=5)
canny_low = st.sidebar.slider("Canny low threshold", 0, 255, 50)
canny_high = st.sidebar.slider("Canny high threshold", 0, 255, 150)
view_mode = st.sidebar.radio("Display mode", ["Grid view", "Separate view"], index=0)


def bgr_to_rgb(img):
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)


def label_image(img, text):
    out = img.copy()
    cv.putText(out, text, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return out


def to_bgr(gray_img):
    return cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR)


def encode_png(image_bgr):
    ok, buffer = cv.imencode('.png', image_bgr)
    return buffer.tobytes() if ok else None


if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)

    if img is None:
        st.error("Image not found or unsupported file format.")
    else:
        img = cv.resize(img, (resize_width, resize_height))
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (blur_kernel, blur_kernel), 0)
        _, thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        edge = cv.Canny(blur, canny_low, canny_high)
        negative = 255 - gray

        original_l = label_image(img, "Original")
        gray_l = label_image(to_bgr(gray), "Grayscale")
        blur_l = label_image(to_bgr(blur), "Gaussian Blur")
        thresh_l = label_image(to_bgr(thresh), "Otsu Threshold")
        edge_l = label_image(to_bgr(edge), "Canny Edge")
        negative_l = label_image(to_bgr(negative), "Negative")

        gap = np.ones((resize_height, 10, 3), dtype=np.uint8) * 255
        first_row = np.hstack((original_l, gap, gray_l, gap, blur_l))
        second_row = np.hstack((thresh_l, gap, edge_l, gap, negative_l))
        multi = np.vstack((first_row, second_row))

        if view_mode == "Grid view":
            st.subheader("Combined Grid")
            st.image(bgr_to_rgb(multi), use_container_width=True)
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(bgr_to_rgb(original_l), caption="Original", use_container_width=True)
                st.image(bgr_to_rgb(thresh_l), caption="Otsu Threshold", use_container_width=True)
            with col2:
                st.image(bgr_to_rgb(gray_l), caption="Grayscale", use_container_width=True)
                st.image(bgr_to_rgb(edge_l), caption="Canny Edge", use_container_width=True)
            with col3:
                st.image(bgr_to_rgb(blur_l), caption="Gaussian Blur", use_container_width=True)
                st.image(bgr_to_rgb(negative_l), caption="Negative", use_container_width=True)

        grid_bytes = encode_png(multi)
        if grid_bytes:
            st.download_button("Download output image", data=grid_bytes, file_name="multi_output.png", mime="image/png")

        st.subheader("Processed arrays")
        st.code(
            f"Original shape: {img.shape}\n"
            f"Gray shape: {gray.shape}\n"
            f"Threshold used: Otsu automatic\n"
            f"Canny thresholds: {canny_low}, {canny_high}",
            language="text"
        )
else:
    st.info("Upload an image file to start processing.")

st.markdown("""
### Run locally
```bash
pip install streamlit opencv-python numpy
streamlit run app.py
```
""")
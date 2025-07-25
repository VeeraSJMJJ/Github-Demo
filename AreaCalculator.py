import streamlit as st
import math

st.set_page_config(page_title="📐 Geometry Master", layout="centered")
st.title("📐 Geometry Master – Area, Perimeter & Surface Area")
st.markdown("Choose a shape, view diagram, and calculate area & perimeter/surface area.")

# --- Shape selection ---
shape = st.selectbox("Select a shape:", [
    "Circle", "Rectangle", "Triangle",
    "Sphere (3D)", "Cylinder (3D)"
])

# --- Diagrams ---
shape_images = {
    "Circle": "https://upload.wikimedia.org/wikipedia/commons/3/34/Circle_-_black_simple.svg",
    "Rectangle": "https://upload.wikimedia.org/wikipedia/commons/5/55/Rectangle_example.svg",
    "Triangle": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Triangle-equilateral.svg",
    "Sphere (3D)": "https://upload.wikimedia.org/wikipedia/commons/1/15/Sphere.svg",
    "Cylinder (3D)": "https://upload.wikimedia.org/wikipedia/commons/4/42/Cylinder_geometry.svg"
}

st.image(shape_images[shape], caption=f"{shape} diagram", use_container_width=True)

# --- Calculation functions ---
def area_circle(r): return math.pi * r**2
def perimeter_circle(r): return 2 * math.pi * r

def area_rectangle(l, w): return l * w
def perimeter_rectangle(l, w): return 2 * (l + w)

def area_triangle(b, h): return 0.5 * b * h
def perimeter_triangle(a, b, c): return a + b + c

def surface_area_sphere(r): return 4 * math.pi * r**2
def volume_sphere(r): return (4/3) * math.pi * r**3

def surface_area_cylinder(r, h): return 2 * math.pi * r * (r + h)
def volume_cylinder(r, h): return math.pi * r**2 * h

# --- Inputs & Outputs ---
if shape == "Circle":
    r = st.number_input("Radius (r)", min_value=0.0, step=0.1)
    if r > 0:
        st.success(f"🟠 Area = πr² = {area_circle(r):.2f}")
        st.info(f"🟣 Perimeter = 2πr = {perimeter_circle(r):.2f}")

elif shape == "Rectangle":
    l = st.number_input("Length (l)", min_value=0.0)
    w = st.number_input("Width (w)", min_value=0.0)
    if l > 0 and w > 0:
        st.success(f"🟠 Area = l × w = {area_rectangle(l, w):.2f}")
        st.info(f"🟣 Perimeter = 2(l + w) = {perimeter_rectangle(l, w):.2f}")

elif shape == "Triangle":
    b = st.number_input("Base (b)", min_value=0.0)
    h = st.number_input("Height (h)", min_value=0.0)
    a = st.number_input("Side a", min_value=0.0)
    c = st.number_input("Side c", min_value=0.0)
    if b > 0 and h > 0:
        st.success(f"🟠 Area = ½ × b × h = {area_triangle(b, h):.2f}")
    if a > 0 and b > 0 and c > 0:
        st.info(f"🟣 Perimeter = a + b + c = {perimeter_triangle(a, b, c):.2f}")

elif shape == "Sphere (3D)":
    r = st.number_input("Radius (r)", min_value=0.0)
    if r > 0:
        st.success(f"🟠 Surface Area = 4πr² = {surface_area_sphere(r):.2f}")
        st.info(f"🔵 Volume = 4⁄3 πr³ = {volume_sphere(r):.2f}")

elif shape == "Cylinder (3D)":
    r = st.number_input("Radius (r)", min_value=0.0)
    h = st.number_input("Height (h)", min_value=0.0)
    if r > 0 and h > 0:
        st.success(f"🟠 Surface Area = 2πr(r + h) = {surface_area_cylinder(r, h):.2f}")
        st.info(f"🔵 Volume = πr²h = {volume_cylinder(r, h):.2f}")

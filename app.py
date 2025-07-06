import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import io

# Streamlit Setup
st.set_page_config(page_title="Mathematischer Ausdrucks-Viewer", layout="centered")
st.title("🔢 Mathematische Ausdrücke grafisch darstellen")

# Info & Beispiele
with st.expander("ℹ️ Beispiele für gültige Eingaben"):
    st.markdown("""
    **Allgemeine Ausdrücke:**
    - `sqrt(x)` → \( \sqrt{x} \)
    - `x**2 + 2*x + 1` → \( x^2 + 2x + 1 \)
    - `log(x), ln(x), exp(x)`

    **Ableitungen & Integrale:**
    - `diff(sin(x), x)` → \( \frac{d}{dx} \sin(x) \)
    - `Integral(x**2, x)` → \( \int x^2 \, dx \)

    **Summen & Produkte:**
    - `Sum(1/n, (n, 1, 10))` → \( \sum_{n=1}^{10} \frac{1}{n} \)
    - `Product(n, (n, 1, 5))` → \( \prod_{n=1}^{5} n \)

    **Gleichungen & Gleichungssysteme:**
    - `Eq(x**2, 1)` → \( x^2 = 1 \)
    - `Matrix([[a, b], [b, c]])` → 2x2-Matrix

    **Vektor, Matrix, Determinante:**
    - `det(Matrix([[a, b], [b, c]]))` → \( \det \begin{bmatrix} a & b \\ b & c \end{bmatrix} \)
    """)

# Eingabe
user_input = st.text_area("🧮 Gib deinen mathematischen Ausdruck ein:", value="(a - λ)*(c - λ) - b**2")

# Fehleranfällige Symbole korrigieren
user_input = user_input.replace("^", "**").replace("ln", "log")

# Definiere Symbole (auch griechische)
a, b, c, d, e, f, g, h, x, y, z, t, n = sp.symbols("a b c d e f g h x y z t n")
θ, φ, α, β, γ, δ, λ = sp.symbols("θ φ α β γ δ λ")

# Symbolische Auswertung
if user_input.strip():
    try:
        expr = sp.sympify(user_input)
        simplified = sp.simplify(expr)

        st.subheader("📘 Darstellung:")
        st.latex(sp.latex(expr))

        st.subheader("📉 Vereinfachte Form:")
        st.latex(sp.latex(simplified))

        # Formel als PNG generieren
        fig, ax = plt.subplots(figsize=(0.01, 0.01))
        ax.axis("off")
        tex = f"${sp.latex(expr)}$"
        fig.text(0.5, 0.5, tex, fontsize=20, ha='center', va='center')

        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0.3, dpi=300)
        buf.seek(0)

        st.subheader("🖼️ Vorschau als Bild:")
        st.image(buf)

        st.download_button("⬇️ Formel als PNG herunterladen", data=buf, file_name="formel.png", mime="image/png")

    except Exception as e:
        st.error(f"❌ Fehler beim Verarbeiten des Ausdrucks:\n\n{e}")

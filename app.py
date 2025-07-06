import streamlit as st
import sympy as sp

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

# Eingabefeld
user_input = st.text_area("🧮 Gib deinen mathematischen Ausdruck ein:", value="(a - λ)*(c - λ) - b**2")

# Fehleranfällige Symbole korrigieren
user_input = user_input.replace("^", "**").replace("ln", "log")

# Definiere erlaubte Symbole (inkl. griechisch)
a, b, c, d, e, f, g, h, x, y, z, t, n = sp.symbols("a b c d e f g h x y z t n")
θ, φ, α, β, γ, δ, λ = sp.symbols("θ φ α β γ δ λ")

# Symbolische Verarbeitung
if user_input.strip():
    try:
        expr = sp.sympify(user_input)
        simplified = sp.simplify(expr)

        # Anzeige
        st.subheader("📘 Darstellung:")
        if isinstance(expr, sp.Equality):
            st.latex(sp.latex(expr.lhs) + " = " + sp.latex(expr.rhs))
        else:
            st.latex(sp.latex(expr))

        # Vereinfachte Darstellung (optional)
        st.subheader("📉 Vereinfachter Ausdruck:")
        st.latex(sp.latex(simplified))

        # LaTeX-Download
        st.download_button("⬇️ LaTeX-Datei herunterladen", data=sp.latex(expr), file_name="formel.tex")

    except Exception as e:
        st.error(f"❌ Fehler beim Verarbeiten des Ausdrucks:\n\n{e}")

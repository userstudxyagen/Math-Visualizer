import streamlit as st
import sympy as sp
from sympy.abc import a, b, c, d, e, f, g, h, x, y, z, t, θ, φ, α, β, γ, δ, λ, n

# Streamlit Setup
st.set_page_config(page_title="🧮 Mathematischer Ausdrucks-Viewer", layout="centered")
st.title("🧠 Mathematische Ausdrücke grafisch darstellen")

# Eingabe
st.markdown("Gib unten einen beliebigen mathematischen Ausdruck ein – z. B.:")
st.code("sqrt(x), (a - λ)*(c - λ) - b**2, Integral(x**2, x), Eq(x**2, 1), Matrix([[a, b], [b, c]])")

user_input = st.text_area("📝 Ausdruck eingeben:", "(a - λ)*(c - λ) - b**2")

# Voreinstellungen für Symbolersetzung (optional)
user_input = user_input.replace("^", "**").replace("ln", "log")

# Symbolische Verarbeitung
if user_input.strip():
    try:
        expr = sp.sympify(user_input)

        # Optional: Vereinfachungen anwenden
        col1, col2, col3 = st.columns(3)
        if col1.checkbox("🔄 Vereinfachen (simplify)", value=True):
            expr = sp.simplify(expr)
        if col2.checkbox("🎯 Trigonometrisch vereinfachen (trigsimp)"):
            expr = sp.trigsimp(expr)
        if col3.checkbox("📦 Ausmultiplizieren (expand)"):
            expr = sp.expand(expr)

        # Darstellung
        st.subheader("📘 Darstellung des Ausdrucks:")
        if isinstance(expr, sp.Equality):
            st.latex(sp.latex(expr.lhs) + " = " + sp.latex(expr.rhs))
        else:
            st.latex(sp.latex(expr))

        # Download als .tex
        st.download_button("⬇️ LaTeX-Code herunterladen", data=sp.latex(expr), file_name="formel.tex")

    except Exception as e:
        st.error(f"❌ Fehler beim Verarbeiten des Ausdrucks:\n{e}")

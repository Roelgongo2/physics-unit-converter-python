# physics-unit-converter-python
Phase 0 / Unit U001: Motion and Electronics Unit Converter with Dimensional Validation Checks.

# Motion & Electronics Unit Converter & Validator
### Polymath OS — Curriculum Phase 0 | Unit U001

A comprehensive engineering calculator built in Python that executes unified motion and electronics evaluations. This project serves as evidence of completion for the **Phase 0 / Unit U001 (Algebraic Fluency and Equations)** competency milestone, demonstrating formula engineering, data-type management, and boundary-condition checking.

## ⚛️ Engineering Formulas Implemented

### 🏃 Mechanics & Motion
* **Velocity (v):** \(v = \frac{d}{t}\) (Meters per Second)
* **Acceleration (a):** \(a = \frac{\Delta v}{t}\) (Meters per Second Squared)
* **Force (F):** F = m ⋅ a (Newton)
* **Pressure (P):** \(P = \frac{F}{A}\) (Pascal)
* **Momentum (p):** p = m ⋅ v (Kilogram-Meter per Second)

### ⚡ Electronics & Electromagnetism
* **Charge (Q):** Q = I ⋅ t (Coulomb)
* **Voltage (V):** \(V = \frac{W}{Q}\) (Volt)
* **Resistance (R):** \(R = \frac{V}{I}\) (Ohm)
* **Capacitance (C):** \(C = \frac{Q}{V}\) (Farad)
* **Magnetic Field (B):** \(B = \frac{F}{I \cdot L}\) (Tesla)

---

## 🔍 Dimensional & Logical Validation Checks
To enforce physical accuracy and avoid computational exceptions (such as `ZeroDivisionError`), the pipeline runs structural safety checks before compiling calculations:
1. **Time Check:** Time must be strictly greater than 0 seconds (t > 0) to compute rates.
2. **Mass Check:** Mass must be a non-negative scalar (m ≥ 0) to comply with classical mechanics.
3. **Geometric Check:** Scalar length/distance entries must be non-negative (l ≥ 0).
4. **Electronic Protection:** Internal guards prevent divisions by zero if an electrical network drops below measurable charge, voltage, or current states.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your local environment.

### Execution
Clone this repository or download `main.py`, navigate to the project directory via your terminal, and run:
```bash
python main.py
```

### Example Log Output
```text
--- Motion & Electronics Unit Converter & Validator ---
Enter a length value in meters: 10
Enter a mass value in kilograms: 5
Enter a time value in seconds: 2
Enter an electric current value in Amperes: 3
...

🔍 RUNNING DIMENSIONAL HOMOGENEITY & SAFETY CHECKS...
✅ DIMENSIONAL CHECKS PASSED. OUTPUTTING CONVERSIONS:

  [Motion] Velocity: 5.0000 m/s
  [Motion] Acceleration: 2.5000 m/s^2
  [Motion] Force (Newton): 12.5000 N
  [Electronics] Voltage (Volt): 4.1667 V
  [Electronics] Resistance (Ohm): 1.3889 Ω
```

---
## 📑 Curriculum Context
* **Class:** 01 — Mathematics & Quantitative Foundations
* **Category:** Algebra, functions & geometry
* **Subcategory:** Algebraic fluency and equations (U001)
* **Core Prerequisite Outcome:** Independent engineering script development with operational design error tracking.

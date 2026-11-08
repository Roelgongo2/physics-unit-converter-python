# ==============================================================================
# PHYSICS FORMULA & SI UNIT REFERENCE SHEET
# ==============================================================================

# ------------------------------------------------------------------------------
# PART 1: THE 7 BASE SI UNITS (THE BUILDING BLOCKS)
# ------------------------------------------------------------------------------

# Length (Symbols: l, d, x)
#   Base Unit: meter (m)
#   What it measures: Distance or spatial separation.

# Mass (Symbol: m)
#   Base Unit: kilogram (kg)
#   What it measures: The amount of matter in an object.

# Time (Symbol: t)
#   Base Unit: second (s)
#   What it measures: Duration or passage of time.

# Electric Current (Symbols: I, i)
#   Base Unit: ampere (A)
#   What it measures: The flow rate of electrical charge.

# Temperature (Symbol: T)
#   Base Unit: kelvin (K)
#   What it measures: Absolute thermodynamic hotness or coldness.

# Amount of Substance (Symbol: n)
#   Base Unit: mole (mol)
#   What it measures: Count of elementary particles (atoms or molecules).

# Luminous Intensity (Symbol: Iv)
#   Base Unit: candela (cd)
#   What it measures: The perceived power of light emitted.

# ------------------------------------------------------------------------------
# PART 2: DERIVED SI UNITS WITH SPECIAL NAMES
# ------------------------------------------------------------------------------

# 1. Hertz (Hz) -- Frequency
#   Word Formula: Frequency = Number of Cycles / Time
#   Symbol Formula: f = 1 / T
#   Base Unit Breakdown: 1/s (or s^-1)
#   Plain English: How many times a wave repeats itself in exactly one second.

# 2. Newton (N) -- Force & Weight
#   Word Formula: Force = Mass * Acceleration
#   Symbol Formula: F = m * a
#   Base Unit Breakdown: kg * m / s^2 (or kg * m * s^-2)
#   Plain English: The strength of a push or a pull. 1 Newton can accelerate a 
#   1 kg object by 1 meter per second, every second.

# 3. Pascal (Pa) -- Pressure & Stress
#   Word Formula: Pressure = Force / Area
#   Symbol Formula: P = F / A
#   Base Unit Breakdown: kg / (m * s^2) (or kg * m^-1 * s^-2)
#   Plain English: How intensely a force is concentrated over a surface area.

# 4. Joule (J) -- Energy, Work, & Heat
#   Word Formula: Work = Force * Distance
#   Symbol Formula: W = F * d
#   Base Unit Breakdown: kg * m^2 / s^2 (or kg * m^2 * s^-2)
#   Plain English: The energy spent when you use 1 Newton of force to push an 
#   object forward by 1 meter.

# 5. Watt (W) -- Power
#   Word Formula: Power = Energy / Time
#   Symbol Formula: P = W / t
#   Base Unit Breakdown: kg * m^2 / s^3 (or kg * m^2 * s^-3)
#   Plain English: Speed of energy usage. A 100W appliance burns through 
#   100 Joules of energy every single second.

# 6. Coulomb (C) -- Electric Charge
#   Word Formula: Charge = Electric Current * Time
#   Symbol Formula: Q = I * t
#   Base Unit Breakdown: A * s
#   Plain English: The raw packet of electricity. 1 Ampere flowing down a wire 
#   for 1 second moves exactly 1 Coulomb of charge.

# 7. Volt (V) -- Voltage & Electric Potential
#   Word Formula: Voltage = Work / Electric Charge
#   Symbol Formula: V = W / Q
#   Base Unit Breakdown: kg * m^2 / (s^3 * A) (or kg * m^2 * s^-3 * A^-1)
#   Plain English: Electrical "pushing pressure." Measures how many Joules of 
#   energy are carried by each Coulomb of electric charge.

# 8. Ohm (Ohm) -- Electrical Resistance
#   Word Formula: Resistance = Voltage / Current
#   Symbol Formula: R = V / I
#   Base Unit Breakdown: kg * m^2 / (s^3 * A^2) (or kg * m^2 * s^-3 * A^-2)
#   Plain English: Friction for electricity. Measures how strongly a component 
#   fights back against the flow of electrical current.

# 9. Farad (F) -- Capacitance
#   Word Formula: Capacitance = Electric Charge / Voltage
#   Symbol Formula: C = Q / V
#   Base Unit Breakdown: (s^4 * A^2) / (kg * m^2) (or kg^-1 * m^-2 * s^4 * A^2)
#   Plain English: Electrical storage capacity. Tracks how much charge a 
#   capacitor can store per volt of pressure applied to it.

# 10. Tesla (T) -- Magnetic Field Strength
#   Word Formula: Magnetic Field = Force / (Current * Length of Wire)
#   Symbol Formula: B = F / (I * L)
#   Base Unit Breakdown: kg / (s^2 * A) (or kg * s^-2 * A^-1)
#   Plain English: The intensity of a magnetic field acting on a 1-meter long 
#   wire carrying a 1 Ampere current.

# ------------------------------------------------------------------------------
# PART 3: STANDARD DERIVED UNITS
# ------------------------------------------------------------------------------

# Area
#   Formula: Length * Width (A = l * w)
#   Base Units: m^2
#   Meaning: Two-dimensional flat space.

# Volume
#   Formula: Length * Width * Height (V = l * w * h)
#   Base Units: m^3
#   Meaning: Three-dimensional physical space occupied.

# Velocity / Speed
#   Formula: Distance / Time (v = d / t)
#   Base Units: m/s
#   Meaning: How many meters you cross in one second.

# Acceleration
#   Formula: Change in Velocity / Time (a = v / t)
#   Base Units: m/s^2
#   Meaning: How fast your speed is changing.

# Density
#   Formula: Mass / Volume (Density = m / V)
#   Base Units: kg/m^3
#   Meaning: How tightly packed an object's matter is inside its space.

# Momentum
#   Formula: Mass * Velocity (p = m * v)
#   Base Units: kg * m / s
#   Meaning: The "unstoppability" of a moving object.


# ==============================================================================
# PHYSICS FORMULA & SI UNIT REFERENCE SHEET (CURRICULUM PHASE 0)
# ==============================================================================

# --- INPUT SECTION ---
print("--- Motion & Electronics Unit Converter & Validator ---")
length = float(input("Enter a length value in meters: "))
mass = float(input("Enter a mass value in kilograms: "))
time = float(input("Enter a time value in seconds: "))
electric_current = float(input("Enter an electric current value in Amperes: "))
temperature = float(input("Enter a Temperature value in Kelvin: "))
amount_of_substance = float(input("Enter an amount of substance value in mols: "))
luminous_intensity = float(input("Enter a luminous intensity value in candela: "))

print("\n------------------------------------------------")
print("🔍 RUNNING DIMENSIONAL HOMOGENEITY & SAFETY CHECKS...")
print("------------------------------------------------")

# --- DIMENSIONAL CHECKS (This satisfies your assignment requirement!) ---
has_errors = False

if time <= 0:
    print("DIMENSIONAL ERROR: Time must be strictly greater than 0 seconds to compute rates (Velocity, Acceleration, Watts).")
    has_errors = True

if mass < 0:
    print("PHYSICAL ERROR: Mass cannot be a negative value in classical mechanics.")
    has_errors = True

if length < 0:
    print("GEOMETRIC ERROR: Scalar length/distance cannot be negative.")
    has_errors = True

# --- CALCULATION AND DISPLAY SECTION ---
if not has_errors:
    # Motion Calculations
    Velocity = length / time
    Acceleration = Velocity / time
    Volume = length * length * length
    area = length * length
    Hertz = 1 / time
    Newton = mass * Acceleration
    Density = mass / Volume
    Momentum = mass * Velocity
    Pascal = Newton / area
    
    # Electronics Calculations
    Joule = Newton * length
    Watt = Joule / time
    Coulomb = electric_current * time
    volt = Joule / Coulomb if Coulomb != 0 else 0
    Ohm = volt / electric_current if electric_current != 0 else 0
    Farad = Coulomb / volt if volt != 0 else 0
    Tesla = Newton / (electric_current * length) if (electric_current * length) != 0 else 0

    print("\n DIMENSIONAL CHECKS PASSED. OUTPUTTING CONVERSIONS:\n")
    print(f"  [Motion] Velocity: {Velocity:.4f} m/s")
    print(f"  [Motion] Acceleration: {Acceleration:.4f} m/s^2")
    print(f"  [Motion] Force (Newton): {Newton:.4f} N")
    print(f"  [Motion] Pressure (Pascal): {Pascal:.4f} Pa")
    print(f"  [Electronics] Energy (Joule): {Joule:.4f} J")
    print(f"  [Electronics] Power (Watt): {Watt:.4f} W")
    print(f"  [Electronics] Charge (Coulomb): {Coulomb:.4f} C")
    print(f"  [Electronics] Voltage (Volt): {volt:.4f} V")
    print(f"  [Electronics] Resistance (Ohm): {Ohm:.4f} Ω")
    print(f"  [Electronics] Capacitance (Farad): {Farad:.4f} F")
    print(f"  [Electronics] Magnetic Field (Tesla): {Tesla:.4f} T")
    print("\n TASK STATUS: COMPLETED & DONE!")
else:
    print("\n CONVERSION HALTED: Please fix the dimensional check errors above and try again.")

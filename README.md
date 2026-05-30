# Learning Python

![alt text](971.jpg)

Here I am going to share my notes and the small projects I will make through this journey.

# UIU PHYSICS COMPLETE FORMULA CHEATSHEET

---

## SECTION 1: MECHANICS — KINEMATICS

### Basic Quantities
$$v = \frac{\Delta x}{\Delta t} \quad \text{(velocity)}$$

$$a = \frac{\Delta v}{\Delta t} \quad \text{(acceleration)}$$

### Equations of Motion (Constant Acceleration)

$$v = u + at$$

$$s = ut + \frac{1}{2}at^2$$

$$v^2 = u^2 + 2as$$

$$s = \frac{u+v}{2} \cdot t$$

### Free Fall
$$g = 9.8 \text{ m/s}^2 \approx 10 \text{ m/s}^2$$

**Upward motion:**
$$v^2 = u^2 - 2gh$$
$$v = 0 \text{ at maximum height}$$
$$h_{max} = \frac{u^2}{2g}$$

**Downward from rest:**
$$v^2 = 2gh$$
$$h = \frac{1}{2}gt^2$$

### Projectile Motion
$$x = v_0 \cos\theta \cdot t \quad \text{(horizontal)}$$

$$y = v_0 \sin\theta \cdot t - \frac{1}{2}gt^2 \quad \text{(vertical)}$$

$$\text{Range} = \frac{v_0^2 \sin(2\theta)}{g}$$

$$h_{max} = \frac{(v_0 \sin\theta)^2}{2g}$$

$$\text{Time of flight} = \frac{2v_0 \sin\theta}{g}$$

---

## SECTION 2: NEWTON'S LAWS & FORCES

### Newton's Laws

**First Law:** $F_{net} = 0 \Rightarrow$ constant velocity (equilibrium)

**Second Law:**
$$F_{net} = ma$$

**Third Law:** $F_{action} = -F_{reaction}$

### Common Forces

**Weight:**
$$W = mg$$

**Friction (Kinetic):**
$$f_k = \mu_k N$$

**Friction (Static):**
$$f_s \leq \mu_s N$$

**Normal Force:** $N$ perpendicular to surface

**Tension:** Force along rope/string

### Inclined Plane
**Component along plane:** $mg\sin\theta$

**Component perpendicular:** $mg\cos\theta$

**Normal force:** $N = mg\cos\theta$

**Friction:** $f = \mu N = \mu mg\cos\theta$

---

## SECTION 3: MOMENTUM & COLLISIONS

### Linear Momentum
$$p = mv$$

$$\text{Units: kg·m/s}$$

### Conservation of Momentum
$$\sum p_{before} = \sum p_{after}$$

**No external forces:**
$$m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'$$

### Gun-Bullet Back Velocity
**Initially at rest (initial momentum = 0):**
$$m_{gun} \cdot v_{gun} + m_{bullet} \cdot v_{bullet} = 0$$

$$v_{gun} = -\frac{m_{bullet}}{m_{gun}} \cdot v_{bullet}$$

**Example:** 8 kg gun, 0.1 kg bullet at 70 m/s:
$$v_{gun} = -\frac{0.1}{8} \times 70 = -0.875 \text{ m/s}$$

### Impulse
$$J = F \cdot \Delta t = \Delta p$$

$$F \cdot \Delta t = m \Delta v$$

### Types of Collisions

**Elastic:** $KE$ conserved, momentum conserved

**Perfectly Inelastic:** Objects stick, momentum conserved only

**Partially Inelastic:** Some KE lost, momentum conserved

---

## SECTION 4: WORK, ENERGY & POWER

### Work
$$W = F \cdot d \cdot \cos\theta$$

$$W = 0 \text{ if } F \perp d$$

**Work by friction:** $W = -\mu mg \cdot d$ (negative, opposes motion)

### Kinetic Energy
$$KE = \frac{1}{2}mv^2$$

### Potential Energy (Gravitational)
$$PE_g = mgh$$

### Potential Energy (Elastic/Spring)
$$PE_{spring} = \frac{1}{2}kx^2$$

**Hooke's Law:** $F = -kx$

### Work-Energy Theorem
$$W_{net} = \Delta KE = KE_f - KE_i$$

### Conservation of Mechanical Energy
$$KE + PE = \text{constant}$$

$$\frac{1}{2}mv_i^2 + mgh_i = \frac{1}{2}mv_f^2 + mgh_f$$

### Power
$$P = \frac{W}{t} = F \cdot v$$

$$\text{Units: Watts (W) = J/s}$$

**Crane lifting:** $P = mgv$

$$\text{Example: } P = 330 \times 10 \times 0.15 = 495 \text{ W}$$

---

## SECTION 5: ROTATIONAL MOTION

### Angular Quantities
$$\theta = \text{angular displacement (radians)}$$

$$\omega = \frac{\theta}{t} \quad \text{(angular velocity, rad/s)}$$

$$\omega = 2\pi f = \frac{2\pi}{T}$$

$$\alpha = \frac{\Delta\omega}{\Delta t} \quad \text{(angular acceleration)}$$

### Relation to Linear Quantities
$$v = \omega r$$

$$a_{tangential} = \alpha r$$

### Moment of Inertia
**Point mass:** $I = mr^2$

**Solid sphere:** $I = \frac{2}{5}mr^2$

**Solid cylinder:** $I = \frac{1}{2}mr^2$

**Hollow sphere:** $I = \frac{2}{3}mr^2$

### Torque
$$\tau = r \times F = rF\sin\theta$$

$$\tau = I\alpha$$

### Angular Momentum
$$L = I\omega = mr^2\omega$$

$$L = mvr \quad \text{(for circular motion)}$$

### Conservation of Angular Momentum
$$L_{initial} = L_{final}$$

$$I_1\omega_1 = I_2\omega_2$$

**Example:** 980 g sphere, r = 20 cm, ω = 4 rad/s:
$$L = 0.98 \times (0.2)^2 \times 4 = 0.1568 \text{ kg·m}^2\text{/s}$$

---

## SECTION 6: CIRCULAR MOTION

### Uniform Circular Motion
**Centripetal acceleration:**
$$a_c = \frac{v^2}{r} = \omega^2 r$$

**Centripetal force:**
$$F_c = \frac{mv^2}{r} = m\omega^2 r$$

**Period:**
$$T = \frac{2\pi r}{v} = \frac{2\pi}{\omega}$$

**Frequency:**
$$f = \frac{1}{T}$$

$$\omega = 2\pi f$$

---

## SECTION 7: SIMPLE HARMONIC MOTION (SHM)

### Defining Equation
**Restoring force:**
$$F = -kx$$

**Displacement:**
$$x(t) = A\cos(\omega t + \phi)$$

**Velocity:**
$$v(t) = -A\omega\sin(\omega t + \phi)$$

**Acceleration:**
$$a(t) = -A\omega^2\cos(\omega t + \phi) = -\omega^2 x$$

### Key Parameters
**Amplitude:** $A$ (maximum displacement)

**Angular frequency:**
$$\omega = \sqrt{\frac{k}{m}} = 2\pi f$$

**Period:**
$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}$$

**Frequency:**
$$f = \frac{1}{T}$$

### Finding Amplitude from Max Acceleration
$$a_{max} = \omega^2 A$$

$$A = \frac{a_{max}}{\omega^2}$$

**Example:** $a_{max} = 9$ m/s², $k = 16$ N/m, $m = 4$ kg:
$$\omega = \sqrt{\frac{16}{4}} = 2 \text{ rad/s}$$
$$A = \frac{9}{4} = 2.25 \text{ m}$$

### Energy in SHM
**Total Energy:**
$$E = \frac{1}{2}kA^2 = \frac{1}{2}m\omega^2A^2$$

**Kinetic Energy:**
$$KE = \frac{1}{2}m\omega^2(A^2 - x^2)$$

**Potential Energy:**
$$PE = \frac{1}{2}m\omega^2x^2$$

**Maximum velocity:**
$$v_{max} = A\omega$$

### Spring-Mass System
$$T = 2\pi\sqrt{\frac{m}{k}}$$

### Simple Pendulum
$$T = 2\pi\sqrt{\frac{L}{g}}$$

$$T \text{ independent of mass}$$

---

## SECTION 8: WAVES

### Wave Properties
**Amplitude:** $A$ (maximum displacement)

**Wavelength:** $\lambda$ (distance for one complete oscillation)

**Frequency:** $f$ (oscillations per second, Hz)

**Period:** $T = \frac{1}{f}$

**Wave speed:**
$$v = f\lambda$$

**Angular frequency:**
$$\omega = 2\pi f$$

**Wave number:**
$$k = \frac{2\pi}{\lambda}$$

### Progressive Wave Equation
$$y = A\sin(kx - \omega t) \quad \text{[+x direction]}$$

$$y = A\sin(\omega t - kx) \quad \text{[same]}$$

### Particle Velocity in Wave
$$v_y = \frac{\partial y}{\partial t} = -A\omega\cos(kx - \omega t)$$

**At specific time $t = t_0$:**
$$v_y(t_0) = -A\omega\cos(kx - \omega t_0)$$

### Reading Wavelength from Equation
**From:** $y = A\sin\left(\frac{2\pi x}{\lambda} - \omega t\right)$

**Read directly:** $\lambda$ from coefficient

**If:** $y = A\sin(\pi x - \omega t)$, then $k = \pi = \frac{2\pi}{\lambda}$, so $\lambda = 2$

### Phase Difference & Path Difference
**Phase difference:**
$$\Delta\phi = \frac{2\pi}{\lambda} \Delta x$$

**Path difference from phase difference:**
$$\Delta x = \frac{\lambda}{2\pi} \Delta\phi$$

**Example:** $\Delta\phi = 3\pi$:
$$\Delta x = \frac{\lambda}{2\pi} \times 3\pi = \frac{3\lambda}{2}$$

### Standing Waves
**Nodes:** Zero amplitude

**Antinodes:** Maximum amplitude

**Harmonics:** $f_n = nf_1$ where $n = 1, 2, 3, ...$

### Sound Waves
**Speed of sound:** $v \approx 340$ m/s (in air at 15°C)

### Doppler Effect
$$f' = f \times \frac{v \pm v_{observer}}{v \mp v_{source}}$$

**Observer approaching source:** $+$ in numerator

**Source approaching observer:** $-$ in denominator

**Receding:** opposite signs

### Electromagnetic Waves
**Speed in vacuum:**
$$c = 3 \times 10^8 \text{ m/s}$$

$$c = f\lambda$$

**E and B relationship:**
$$E = cB$$

**Example:** $f = 20$ MHz, $E = 3$ V/m:
$$B = \frac{E}{c} = \frac{3}{3\times 10^8} = 10^{-8} \text{ T}$$

**FM Radio period:** $T = \frac{1}{f}$

Example: 100 MHz: $T = 10^{-8}$ s = 10 ns

---

## SECTION 9: THERMODYNAMICS

### Temperature Conversions
$$K = °C + 273$$

$$°C = \frac{5}{9}(°F - 32)$$

$$°F = \frac{9}{5}°C + 32$$

### Heat & Calorimetry

**Heat for temperature change:**
$$Q = mc\Delta T$$

$c$ = specific heat capacity (J/kg·K)

**Heat for phase change:**
$$Q = mL$$

$L$ = latent heat (J/kg)

### Laws of Thermodynamics

**Zeroth Law:** Objects reach thermal equilibrium

**First Law:**
$$\Delta U = Q - W$$

$Q$ = heat added, $W$ = work done by system

**Second Law:** Entropy of isolated system always increases

$$dS \geq 0$$

### Heat Engines

**Efficiency:**
$$\eta = \frac{W}{Q_H} = 1 - \frac{Q_C}{Q_H}$$

**Carnot Engine (Maximum Efficiency):**
$$\eta_{Carnot} = 1 - \frac{T_C}{T_H}$$

**Between ice (273 K) and boiling water (373 K):**
$$\eta = 1 - \frac{273}{373} = 0.268 = 26.8\%$$

### Entropy

**Entropy change (isothermal):**
$$\Delta S = \frac{Q}{T}$$

**Phase change:**
$$\Delta S = \frac{mL}{T}$$

**Water → steam at 100°C = 373 K, 4 kg:**
$$\Delta S = \frac{4 \times 373 \times 10^6}{373} = 4 \times 10^6 \text{ J/K}$$

**Always positive for irreversible processes**

---

## SECTION 10: KINETIC THEORY OF GASES

### Ideal Gas Law
$$PV = nRT$$

$$PV = Nk_BT$$

**Gas constant:** $R = 8.314$ J/(mol·K)

**Boltzmann constant:** $k_B = 1.38 \times 10^{-23}$ J/K

### Average Kinetic Energy
$$\overline{KE} = \frac{3}{2}k_BT$$

**At T = 10 K:**
$$\overline{KE} = \frac{3}{2}(1.38 \times 10^{-23})(10) = 2.07 \times 10^{-22} \text{ J}$$

**Convert to eV:** $\div 1.6 \times 10^{-19}$

### Gas Laws

**Boyle's Law (constant T):**
$$PV = \text{constant}$$

**Charles' Law (constant P):**
$$\frac{V}{T} = \text{constant}$$

**Gay-Lussac's Law (constant V):**
$$\frac{P}{T} = \text{constant}$$

**Combined:**
$$\frac{PV}{T} = \text{constant}$$

---

## SECTION 11: STATIC ELECTRICITY (ELECTROSTATICS)

### Electric Charge

**Quantization:**
$$q = ne$$

$e = 1.6 \times 10^{-19}$ C (elementary charge)

**Conservation:** Total charge constant in isolated system

### Coulomb's Law

$$F = k\frac{q_1q_2}{r^2}$$

$$k = 9 \times 10^9 \text{ N·m}^2\text{/C}^2$$

**Direction:** Attractive if opposite charges, repulsive if same

### Electric Field

$$E = \frac{F}{q} = k\frac{Q}{r^2}$$

**Field lines:** Away from $+$ charge, toward $-$ charge

**Superposition:** $\vec{E}_{total} = \sum \vec{E}_i$

### Gauss's Law

$$\Phi = \frac{Q_{enclosed}}{\epsilon_0}$$

$$\epsilon_0 = 8.85 \times 10^{-12} \text{ F/m}$$

**Flux:** $\Phi = EA\cos\theta$ (Wb = T·m²)

### Electric Potential

$$V = k\frac{Q}{r} \quad \text{(point charge)}$$

$$V = \frac{U}{q}$$

**Relationship:**
$$E = -\frac{dV}{dx}$$

**Equipotential surfaces:** Perpendicular to field lines

### Electric Potential Energy

$$U = qV$$

$$U = k\frac{q_1q_2}{r}$$

---

## SECTION 12: CAPACITORS

### Basic Definition

$$C = \frac{Q}{V}$$

**Units:** Farad (F) = C/V

### Parallel Plate Capacitor

$$C = \epsilon_0 \frac{A}{d}$$

$A$ = plate area, $d$ = separation

### Capacitor Combinations

**Series:**
$$\frac{1}{C_T} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + ...$$

**Parallel:**
$$C_T = C_1 + C_2 + C_3 + ...$$

### Energy Stored in Capacitor

$$U = \frac{1}{2}CV^2$$

$$U = \frac{Q^2}{2C}$$

$$U = \frac{1}{2}QV$$

**Example:** $C = 5\mu F$, $V = 5$ V:
$$U = \frac{1}{2}(5 \times 10^{-6})(25) = 62.5 \times 10^{-6} \text{ J} = 62.5 \text{ μJ}$$

### Equivalent Capacitance Problems

**Example:** $C_1 = 100\mu F$, $C_2 = 200\mu F$, $C_3 = 300\mu F$ in series:

$$\frac{1}{C_T} = \frac{1}{100} + \frac{1}{200} + \frac{1}{300}$$

$$\frac{1}{C_T} = \frac{6+3+2}{600} = \frac{11}{600}$$

$$C_T = 54.5 \text{ μF}$$

---

## SECTION 13: CURRENT ELECTRICITY

### Basic Quantities

**Current:**
$$I = \frac{Q}{t}$$

**Units:** Amperes (A) = C/s

**Conventional current:** Flow of positive charge

### Resistance & Ohm's Law

$$V = IR$$

**Resistivity:**
$$R = \rho\frac{L}{A}$$

$\rho$ = resistivity, $L$ = length, $A$ = cross-sectional area

### Power & Energy

$$P = VI$$

$$P = I^2R$$

$$P = \frac{V^2}{R}$$

**Energy:**
$$W = Pt = QV$$

**Example:** 220 V, 18 W bulb:
$$I = \frac{P}{V} = \frac{18}{220} = 81.8 \text{ mA}$$

**Example:** 8 mC charge through 12 V:
$$W = QV = (8 \times 10^{-3})(12) = 0.096 \text{ J} = 96 \text{ mJ}$$

### Current from Power Rating

$$I = \frac{P}{V}$$

### Resistor Combinations

**Series:**
$$R_T = R_1 + R_2 + R_3 + ...$$

**Parallel:**
$$\frac{1}{R_T} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + ...$$

**Example:** Two 6Ω in parallel, then series with 6Ω:
$$R_p = \frac{1}{\frac{1}{6}+\frac{1}{6}} = 3\Omega$$
$$R_T = 3 + 6 = 9\Omega$$

### EMF & Internal Resistance

**Circuit equation:**
$$\mathcal{E} = I(R + r)$$

**Terminal voltage:**
$$V = \mathcal{E} - Ir$$

**Solving for I:**
$$I = \frac{\mathcal{E}}{R + r}$$

**Example:** $\mathcal{E} = 3$ V, $r = 0.5\Omega$, $R = 90\Omega$:
$$I = \frac{3}{90 + 0.5} = \frac{3}{90.5} \approx 33.1 \text{ mA}$$

**Finding internal resistance:**
$$r = \frac{\mathcal{E}}{I} - R$$

$$r = \frac{\mathcal{E} - V}{I}$$

### Kirchhoff's Laws

**Kirchhoff's Current Law (KCL):**
$$\sum I_{in} = \sum I_{out}$$

**Kirchhoff's Voltage Law (KVL):**
$$\sum V = 0 \quad \text{(around closed loop)}$$

---

## SECTION 14: MAGNETISM

### Magnetic Field

**Units:** Tesla (T) = kg/(A·s²)

**Field lines:** Closed loops, N to S outside magnet

### Lorentz Force

**On moving charge:**
$$\vec{F} = q\vec{v} \times \vec{B}$$

$$F = qvB\sin\theta$$

**Direction:** Right-hand rule

**On current-carrying wire:**
$$F = BIL\sin\theta$$

$L$ = length of wire

### Magnetic Field from Wire

$$B = \frac{\mu_0 I}{2\pi r}$$

$$\mu_0 = 4\pi \times 10^{-7} \text{ T·m/A}$$

**Direction:** Right-hand rule (thumb = current, fingers = field)

### Ampere's Law

$$\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{enclosed}$$

**For solenoid:**
$$B = \mu_0 nI$$

$n$ = turns per unit length

### Magnetic Flux

$$\Phi = BA\cos\theta$$

**Units:** Weber (Wb) = T·m²

---

## SECTION 15: ELECTROMAGNETIC INDUCTION

### Faraday's Law

$$\mathcal{E} = -\frac{d\Phi}{dt}$$

$$\mathcal{E} = -\frac{d(BA\cos\theta)}{dt}$$

### Lenz's Law

**Induced current opposes the change in flux**

**Direction:** Determine using right-hand rule

### Transformer Equation

$$\frac{V_1}{V_2} = \frac{N_1}{N_2} = \frac{I_2}{I_1}$$

$N$ = number of turns

---

## SECTION 16: ELECTROMAGNETIC WAVES

### Maxwell's Equations (Conceptual)

1. Changing $\vec{E}$ field creates $\vec{B}$ field
2. Changing $\vec{B}$ field creates $\vec{E}$ field
3. Creates self-propagating wave

### EM Wave Properties

**Transverse wave:** $\vec{E} \perp \vec{B} \perp$ direction

**Speed in vacuum:**
$$c = 3 \times 10^8 \text{ m/s}$$

$$c = f\lambda$$

**Electric & magnetic field relationship:**
$$E = cB$$

**Energy transport:** Proportional to $E^2$ or $B^2$

### Example Problem

**FM radio:** $f = 20$ MHz, $E = 3$ V/m

$$B = \frac{E}{c} = \frac{3}{3 \times 10^8} = 10^{-8} \text{ T}$$

**Period:** $T = \frac{1}{f} = \frac{1}{20 \times 10^6} = 50$ ns

### EM Spectrum

$$\text{Radio} \to \text{Microwave} \to \text{IR} \to \text{Visible} \to \text{UV} \to \text{X-ray} \to \text{Gamma}$$

All travel at $c = 3 \times 10^8$ m/s

---

## SECTION 17: MODERN PHYSICS — PHOTOELECTRIC EFFECT

### Photon Energy

$$E = hf$$

$$E = \frac{hc}{\lambda}$$

$$h = 6.63 \times 10^{-34} \text{ J·s}$$

$$c = 3 \times 10^8 \text{ m/s}$$

### Einstein's Photoelectric Equation

$$hf = \Phi + KE_{max}$$

$\Phi$ = work function (J or eV)

$$KE_{max} = hf - \Phi$$

### Work Function & Threshold Wavelength

$$\Phi = hf_0 = \frac{hc}{\lambda_0}$$

$$\lambda_0 = \frac{hc}{\Phi}$$

**For incident light < $\lambda_0$:** No photoelectric effect

### Example Problem

**Sodium work function:** $\Phi = 3$ eV

$$\lambda_0 = \frac{hc}{\Phi} = \frac{(6.63 \times 10^{-34})(3 \times 10^8)}{(3)(1.6 \times 10^{-19})} = 4.14 \times 10^{-7} \text{ m} = 414 \text{ nm}$$

**λ = 663 nm on sodium:**
$$E = \frac{hc}{\lambda} = \frac{(6.63 \times 10^{-34})(3 \times 10^8)}{663 \times 10^{-9}} = 3 \times 10^{-19} \text{ J}$$

$$E = \frac{3 \times 10^{-19}}{1.6 \times 10^{-19}} = 1.88 \text{ eV}$$

### Photon Momentum

$$p = \frac{h}{\lambda}$$

---

## SECTION 18: MODERN PHYSICS — BOHR MODEL

### Energy Levels

$$E_n = -\frac{13.6}{n^2} \text{ eV}$$

$$n = 1, 2, 3, ...$$

**Ground state:** $E_1 = -13.6$ eV

**n = 2:** $E_2 = -3.4$ eV

**n = 3:** $E_3 = -1.51$ eV

### Electron Transitions

**Energy absorbed/emitted:**
$$\Delta E = E_{final} - E_{initial} = hf$$

$$hf = E_1 - E_2 = -13.6 - (-3.4) = -10.2 \text{ eV}$$

**Frequency:**
$$f = \frac{\Delta E}{h}$$

### De Broglie Wavelength

$$\lambda = \frac{h}{p} = \frac{h}{mv}$$

---

## SECTION 19: MODERN PHYSICS — QUANTUM

### Heisenberg Uncertainty Principle

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

$$\hbar = \frac{h}{2\pi} = 1.055 \times 10^{-34} \text{ J·s}$$

---

## SECTION 20: NUCLEAR PHYSICS

### Atomic Structure

**Mass number:** $A = Z + N$

$Z$ = protons, $N$ = neutrons

**Isotopes:** Same $Z$, different $N$

### Radioactive Decay

**Alpha (α) decay:**
$$^A_Z X \to ^{A-4}_{Z-2}Y + ^4_2He$$

**Beta (β) decay:**
$$^A_Z X \to ^A_{Z+1}Y + e^- + \bar{\nu}_e$$

**Gamma (γ) decay:**
$$^A_Z X^* \to ^A_Z X + \gamma$$

### Decay Law

$$N = N_0 e^{-\lambda t}$$

$\lambda$ = decay constant (s⁻¹)

### Half-Life

$$t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda}$$

**After n half-lives:**
$$N = \frac{N_0}{2^n}$$

**Example:** $\lambda = 0.693$ s⁻¹:
$$t_{1/2} = \frac{0.693}{0.693} = 1 \text{ s}$$

---

## SECTION 21: SEMICONDUCTORS & ELECTRONICS

### Boolean Algebra

**NOT operation:**
$$\overline{0} = 1, \quad \overline{1} = 0$$

**AND operation (·):**
$$0 \cdot 0 = 0, \quad 0 \cdot 1 = 0, \quad 1 \cdot 1 = 1$$

**OR operation (+):**
$$0 + 0 = 0, \quad 0 + 1 = 1, \quad 1 + 1 = 1$$

**De Morgan's Laws:**
$$\overline{AB} = \bar{A} + \bar{B}$$

$$\overline{A + B} = \bar{A} \cdot \bar{B}$$

### Logic Gates

**Fundamental Gates:**
- **AND:** Output 1 only if both inputs 1
- **OR:** Output 1 if any input 1
- **NOT:** Inverts input

**Universal Gates:**
- **NAND:** $\overline{AB}$ (can build any gate)
- **NOR:** $\overline{A+B}$ (can build any gate)

**XOR:** Output 1 when inputs different
$$A \oplus B = A\bar{B} + \bar{A}B$$

### Number System Conversions

**Decimal to Binary:** Repeated division by 2

**Decimal to Hexadecimal:** Repeated division by 16

**Example:** $9_{10} \to ?_{16}$

$9 < 16$, so $9_{10} = 9_{16}$

**Example:** $255_{10} \to ?_{16}$

$255 \div 16 = 15$ remainder $15$

$15_{16} = F_{16}$, so $255_{10} = FF_{16}$

**Hex digits:** 0-9, A(10), B(11), C(12), D(13), E(14), F(15)

---

## CONSTANTS & USEFUL VALUES

$$g = 9.8 \text{ m/s}^2 \approx 10 \text{ m/s}^2$$

$$k = 9 \times 10^9 \text{ N·m}^2\text{/C}^2$$

$$\epsilon_0 = 8.85 \times 10^{-12} \text{ F/m}$$

$$\mu_0 = 4\pi \times 10^{-7} \text{ T·m/A}$$

$$h = 6.63 \times 10^{-34} \text{ J·s}$$

$$\hbar = 1.055 \times 10^{-34} \text{ J·s}$$

$$e = 1.6 \times 10^{-19} \text{ C}$$

$$c = 3 \times 10^8 \text{ m/s}$$

$$k_B = 1.38 \times 10^{-23} \text{ J/K}$$

$$R = 8.314 \text{ J/(mol·K)}$$

---

## QUICK LOOKUP BY EXAM QUESTION

| Question | Topic | Key Formula |
|----------|-------|-------------|
| Q16 (Momentum) | Gun-bullet | $m_1v_1 + m_2v_2 = 0$ |
| Q17 (Angular momentum) | Rotational | $L = mr^2\omega$ |
| Q18,19,25,26 (SHM/Waves) | SHM | $x = A\cos(\omega t)$ |
| Q20 (Entropy) | Thermodynamics | $\Delta S = Q/T$ |
| Q21 (Kinetic energy of gas) | Kinetic theory | $\overline{KE} = \frac{3}{2}k_BT$ |
| Q22-28,33,35,45 (Circuits) | Electricity | $V = IR$, $P = VI$ |
| Q30,41 (Photoelectric) | Modern physics | $hf = \Phi + KE_{max}$ |
| Q31 (Wave phase) | Waves | $\Delta\phi = \frac{2\pi}{\lambda}\Delta x$ |
| Q32,34 (Capacitors) | Static electricity | $C = Q/V$, $U = \frac{1}{2}CV^2$ |
| Q40 (EM waves) | EM | $E = cB$ |
| Q42 (Half-life) | Nuclear | $t_{1/2} = 0.693/\lambda$ |
| Q43 (Entropy phase) | Thermodynamics | $\Delta S = mL/T$ |
| Q44 (Logic gates) | Electronics | Truth tables |

---

## TIPS FOR USING THIS CHEATSHEET

✅ **During Study:** Reference formulas while solving practice problems

✅ **Before Exam:** Make sure you can derive or understand where each formula comes from

✅ **During Exam:** Use as quick reference, write down key formulas immediately after reading questions

✅ **Check Units:** Always verify your answer has correct units

✅ **Key Concepts to Memorize:**
- $v = u + at$
- $F = ma$
- $W = Fd$
- $P = VI$
- $c = f\lambda$
- $hf = \Phi + KE_{max}$
- Kirchhoff's laws
- SHM equations
- Capacitor formulas

---

**Total Formulas Covered:** 200+ equations  
**All topics from UIU Physics admission exam**  
**Last updated:** 2 weeks before exam

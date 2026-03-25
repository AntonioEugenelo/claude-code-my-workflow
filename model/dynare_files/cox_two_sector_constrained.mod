// =========================================================================
// Cox et al. (2025) + Eugenelo Constrained Fiscal Policy
// Two-sector model with zero-budget constraint (gbar = 0, rho = 0)
//
// Eugenelo Section 5: aggregate government good provision is exogenous.
// The planner reallocates spending across sectors but cannot change the
// aggregate basket. With gbar=0 and rho=0, this means:
//   omega_g1 * g1 + omega_g2 * g2 = 0
//
// Structural equations: Cox et al. baseline (kappa=0, sigma=1)
// Policy rules: Eugenelo constrained optimal fiscal + monetary
// =========================================================================

var ytilde1 ytilde2 pi1 pi2 ftilde1 ftilde2
    p1 p2 pc pi_agg ytilde_agg ftilde_agg
    i_nom a1 a2
    g1 g2 y1 y2;

varexo eps1 eps2;

parameters beta phi chi theta rho_a rho_g
           omegac1 omegac2 omegag1 omegag2
           alpha1 alpha2
           mu1 mu2 chi1 chi2 chistar1 chistar2 chistar
           lambda1 lambda2
           // Eugenelo constrained policy helper coefficients
           Dk_num1 Dk_num2 Dk_den1 Dk_den2 D1 D2
           R12
           coeff_y1 coeff_pi1
           coeff_y_den2 coeff_pi_den2
           Rscale1
           // Monetary policy coefficients
           mp_lhs1 mp_lhs2
           mp_rhs_g1 mp_rhs_g2
           mp_rhs_y1 mp_rhs_y2;

// =========================================================================
// CALIBRATION (same as baseline)
// =========================================================================
beta    = 0.997;
phi     = 4;
chi     = 0.185;
theta   = 6;            // *** NOT IN COX ET AL. ***
rho_a   = 0.85;
rho_g   = 0;            // CES parameter for government basket (0 = Cobb-Douglas)

// Asymmetric weights: government demand tilted toward sticky sector
// (consistent with U.S. data per Cox et al. 2024)
omegac1 = 0.6; omegac2 = 0.4;
omegag1 = 0.3; omegag2 = 0.7;
alpha1  = 0.25; alpha2  = 0.75;

// Derived structural parameters
mu1      = (1-chi)*omegac1 + chi*omegag1;
mu2      = (1-chi)*omegac2 + chi*omegag2;
chi1     = chi*omegag1/mu1;
chi2     = chi*omegag2/mu2;
chistar1 = chi1/(1-chi1);
chistar2 = chi2/(1-chi2);
chistar  = chi/(1-chi);
lambda1  = (1-alpha1)*(1-beta*alpha1)/alpha1;
lambda2  = (1-alpha2)*(1-beta*alpha2)/alpha2;

// =========================================================================
// EUGENELO CONSTRAINED POLICY COEFFICIENTS
// (Appendix E, with rho=0, residual sector i=2)
// =========================================================================
// NOTE: In the Eugenelo paper, \phi and \varphi both denote the inverse
// Frisch elasticity. This is a LaTeX inconsistency, not separate parameters.

// Per-sector terms (Eugenelo notation)
// Numerator:   1 + lambda_k*(1+phi)
// Denominator: 1 + lambda_k*(1+phi*(1-chi_k))
Dk_num1 = 1 + lambda1*(1+phi);
Dk_num2 = 1 + lambda2*(1+phi);
Dk_den1 = 1 + lambda1*(1+phi*(1-chi1));
Dk_den2 = 1 + lambda2*(1+phi*(1-chi2));
D1      = Dk_num1/Dk_den1;
D2      = Dk_num2/Dk_den2;

// NOTE: The original Eugenelo formula had a spurious (1-chi_k)/(1-chi_i)
// factor (R12). The corrected derivation eliminates it.
// R12 is kept at 1 (no cross-chi ratio in the corrected formula).
R12     = 1;

// Coefficients on own sector variables (y_k, pi_k)
coeff_y1  = phi/Dk_num1;
coeff_pi1 = theta*phi*(1-chi1)/Dk_num1;

// Coefficients on residual sector variables (y_i, pi_i) — using Dk_den
coeff_y_den2  = phi/Dk_den2;
coeff_pi_den2 = theta*phi*(1-chi2)/Dk_den2;

// Scale factor for residual-sector terms: R12/D1
Rscale1 = R12/D1;

// Monetary policy coefficients (Eugenelo eq in policy_two.tex lines 50-53)
// LHS: mu_k * theta*(1-chi_k) * (1+phi*(1-chi_k)) / Dk_den_k
mp_lhs1 = mu1*theta*(1-chi1)*(1+phi*(1-chi1))/Dk_den1;
mp_lhs2 = mu2*theta*(1-chi2)*(1+phi*(1-chi2))/Dk_den2;

// RHS: mu_k * chi_k / Dk_den_k  (coefficient on g_k)
mp_rhs_g1 = mu1*chi1/Dk_den1;
mp_rhs_g2 = mu2*chi2/Dk_den2;

// RHS: mu_k * (1-chi_k)*(1+phi+chistar_k) / Dk_den_k  (coefficient on y_k)
mp_rhs_y1 = mu1*(1-chi1)*(1+phi+chistar1)/Dk_den1;
mp_rhs_y2 = mu2*(1-chi2)*(1+phi+chistar2)/Dk_den2;

// =========================================================================
// MODEL EQUATIONS
// =========================================================================
model(linear);

// ===== STRUCTURAL EQUATIONS (same as baseline) =====

// [1-2] Sectoral Phillips Curves (Cox et al. eq 2.23)
pi1 = beta*pi1(+1) + lambda1*(1+phi)*ytilde1 - lambda1*chistar1*ftilde1;
pi2 = beta*pi2(+1) + lambda2*(1+phi)*ytilde2 - lambda2*chistar2*ftilde2;

// [3] Demand relation, sector 1 (Cox et al. eq 2.24)
ytilde1 - ytilde_agg = chistar1*ftilde1 - chistar*ftilde_agg
    - (p1 - pc)
    - a1 + mu1*a1 + mu2*a2
    + chistar*((mu1-omegag1)*a1 + (mu2-omegag2)*a2);

// [4-5] Price-inflation identities
p1 = p1(-1) + pi1;
p2 = p2(-1) + pi2;

// [6-9] Aggregation
pc         = omegac1*p1 + omegac2*p2;
pi_agg     = omegac1*pi1 + omegac2*pi2;
ytilde_agg = mu1*ytilde1 + mu2*ytilde2;
ftilde_agg = omegag1*(ftilde1+ytilde1) + omegag2*(ftilde2+ytilde2) - ytilde_agg;

// [10] IS curve (backs out interest rate, eq 2.22)
ytilde1 = ytilde1(+1) - (i_nom - pi1(+1) - (a1(+1)-a1))
          - chistar1*(ftilde1(+1)-ftilde1);

// [11-12] Shock processes
a1 = rho_a*a1(-1) + eps1;
a2 = rho_a*a2(-1) + eps2;

// ===== VARIABLE LINKS (level deviations <-> gaps) =====

// [13-14] Government spending GAP (Eugenelo notation: g_k = ftilde_k + ytilde_k)
// This is the deviation of g_k from efficient level (g_bar_k = a_k),
// NOT the level deviation from steady state.
g1 = ftilde1 + ytilde1;
g2 = ftilde2 + ytilde2;

// [15-16] Output GAP (Eugenelo notation: y_k = ytilde_k)
y1 = ytilde1;
y2 = ytilde2;

// ===== CONSTRAINED OPTIMAL POLICY (Eugenelo Section 5) =====

// [17] Zero-budget constraint (rho=0 => Cobb-Douglas basket)
// gbar_t = sum omega_gk g_kt = 0
omegag1*g1 + omegag2*g2 = 0;

// [18] Eugenelo optimal fiscal rule for sector 1, residual = sector 2
// (Appendix E derivation, policy_two.tex lines 14-23, with rho=0)
//
// g_1 = R12*(D2/D1)*g_2
//      - coeff_y1*y_1 - coeff_pi1*pi_1
//      + Rscale1*(coeff_y_den2*y_2 + coeff_pi_den2*pi_2)
//
g1 = R12*(D2/D1)*g2
     - coeff_y1*y1 - coeff_pi1*pi1
     + Rscale1*(coeff_y_den2*y2 + coeff_pi_den2*pi2);

// [19] Eugenelo optimal monetary policy (policy_two.tex lines 50-53)
//
// sum_k mp_lhs_k * pi_k = sum_k (mp_rhs_g_k * g_k - mp_rhs_y_k * y_k)
//
mp_lhs1*pi1 + mp_lhs2*pi2
    = mp_rhs_g1*g1 + mp_rhs_g2*g2
      - mp_rhs_y1*y1 - mp_rhs_y2*y2;

end;

// =========================================================================
// SHOCKS & SOLUTION
// =========================================================================
shocks;
var eps1 = 1;
var eps2 = 1;
end;

steady;
check;

stoch_simul(order=1, irf=40, nograph);

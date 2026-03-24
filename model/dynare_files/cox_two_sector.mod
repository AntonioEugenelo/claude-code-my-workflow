// =========================================================================
// Cox et al. (2025) — Two-Sector Model
// "Optimal Monetary and Fiscal Policies in Disaggregated Economies"
// NBER WP 32914
//
// All variables are log-deviations from the efficient steady state.
// Equation references: (X.Y) refers to Cox et al. equation numbering.
// =========================================================================

// ----- Endogenous variables -----
var ytilde1     ${\tilde{y}_{1,t}}$   (long_name='Output gap sector 1')
    ytilde2     ${\tilde{y}_{2,t}}$   (long_name='Output gap sector 2')
    pi1         ${\pi_{1,t}}$         (long_name='Inflation sector 1')
    pi2         ${\pi_{2,t}}$         (long_name='Inflation sector 2')
    ftilde1     ${\tilde{f}_{1,t}}$   (long_name='Fiscal gap sector 1')
    ftilde2     ${\tilde{f}_{2,t}}$   (long_name='Fiscal gap sector 2')
    p1          ${p_{1,t}}$           (long_name='Price level sector 1')
    p2          ${p_{2,t}}$           (long_name='Price level sector 2')
    pc          ${p_{c,t}}$           (long_name='Consumer price index')
    pi_agg      ${\pi_t}$             (long_name='Aggregate inflation')
    ytilde_agg  ${\tilde{y}_t}$       (long_name='Aggregate output gap')
    ftilde_agg  ${\tilde{f}_t}$       (long_name='Aggregate fiscal gap')
    i_nom       ${i_t}$               (long_name='Nominal interest rate (dev from SS)')
    a1          ${a_{1,t}}$           (long_name='Productivity sector 1')
    a2          ${a_{2,t}}$           (long_name='Productivity sector 2')
;

// ----- Exogenous shocks -----
varexo eps1     ${\varepsilon_{1,t}}$ (long_name='Productivity shock sector 1')
       eps2     ${\varepsilon_{2,t}}$ (long_name='Productivity shock sector 2')
;

// ----- Parameters -----
parameters
    // Structural (from Cox et al. Section 5.1, p.24)
    beta        ${\beta}$
    phi         ${\varphi}$
    chi         ${\chi}$
    theta       ${\theta}$
    rho_a       ${\rho_a}$
    // Sector weights
    omegac1     ${\omega_{c,1}}$
    omegac2     ${\omega_{c,2}}$
    omegag1     ${\omega_{g,1}}$
    omegag2     ${\omega_{g,2}}$
    // Calvo parameters
    alpha1      ${\alpha_1}$
    alpha2      ${\alpha_2}$
    // Derived (computed in calibration block)
    mu1         ${\mu_1}$
    mu2         ${\mu_2}$
    chi1        ${\chi_1}$
    chi2        ${\chi_2}$
    chistar1    ${\chi_1^*}$
    chistar2    ${\chi_2^*}$
    chistar     ${\chi^*}$
    lambda1     ${\lambda_1}$
    lambda2     ${\lambda_2}$
;

// =========================================================================
// CALIBRATION
// =========================================================================

// --- Directly calibrated (Cox et al. Section 5.1) ---
beta    = 0.997;        // Monthly discount factor
phi     = 4;            // Inverse-Frisch elasticity (Chetty et al. 2011)
chi     = 0.185;        // Government demand / GDP (Cox et al. 2024 "Big G")
rho_a   = 0.85;         // Productivity shock persistence

// MISSING DATA: theta is NOT stated in Cox et al. calibration section.
// Standard values: 6 (Gali 2008), 11 (Woodford 2003).
// Eugenelo extension paper uses theta = 6 in worked examples.
// Using theta = 6 as baseline; sensitivity analysis recommended.
theta   = 6;            // *** NOT IN COX ET AL. — ASSUMED ***

// --- Sector weights (symmetric 2-sector baseline) ---
// For the theoretical 2-sector analysis, Cox et al. use symmetric weights.
// The asymmetric U.S. calibration (121 sectors) is in Section 5.
omegac1 = 0.5;
omegac2 = 0.5;          // = 1 - omegac1
omegag1 = 0.5;
omegag2 = 0.5;          // = 1 - omegag1

// --- Calvo parameters (asymmetric price stickiness) ---
// Cox et al. do not specify 2-sector values; these come from BLS PPI
// micro data for the 121-sector calibration (Pasten et al. 2020/2024).
// MISSING DATA: exact sector-level alpha_k from restricted BLS data.
// Using illustrative values: sector 1 = flexible, sector 2 = sticky.
alpha1  = 0.25;         // *** ILLUSTRATIVE — needs BLS data for U.S. ***
alpha2  = 0.75;         // *** ILLUSTRATIVE — needs BLS data for U.S. ***

// --- Derived parameters (Cox et al. Section 2.2, eqs 2.16-2.19) ---
mu1     = (1-chi)*omegac1 + chi*omegag1;       // Sector 1 output share
mu2     = (1-chi)*omegac2 + chi*omegag2;       // Sector 2 output share
chi1    = chi*omegag1/mu1;                      // Gov't share of sector 1 output
chi2    = chi*omegag2/mu2;                      // Gov't share of sector 2 output
chistar1 = chi1/(1-chi1);                       // chi_1^*
chistar2 = chi2/(1-chi2);                       // chi_2^*
chistar  = chi/(1-chi);                         // chi^*
lambda1 = (1-alpha1)*(1-beta*alpha1)/alpha1;    // Phillips curve slope sector 1
lambda2 = (1-alpha2)*(1-beta*alpha2)/alpha2;    // Phillips curve slope sector 2

// =========================================================================
// MODEL EQUATIONS
// =========================================================================
model(linear);

// ----- STRUCTURAL EQUATIONS -----

// [1-2] Sectoral Phillips Curves (eq 2.23)
// pi_kt = beta * E pi_{k,t+1} + lambda_k * (1+phi) * ytilde_kt - lambda_k * chi*_k * ftilde_kt
pi1 = beta * pi1(+1) + lambda1*(1+phi)*ytilde1 - lambda1*chistar1*ftilde1;
pi2 = beta * pi2(+1) + lambda2*(1+phi)*ytilde2 - lambda2*chistar2*ftilde2;

// [3] Demand relation, sector 1 (eq 2.24)
// ytilde_k - ytilde = chi*_k ftilde_k - chi* ftilde - (p_k - p_c)
//                     - (a_k - a) + chi* sum_j (mu_j - omega_{g,j}) a_j
// where a = mu1*a1 + mu2*a2
ytilde1 - ytilde_agg = chistar1*ftilde1 - chistar*ftilde_agg
    - (p1 - pc)
    - a1 + mu1*a1 + mu2*a2
    + chistar*((mu1 - omegag1)*a1 + (mu2 - omegag2)*a2);

// [4-5] Price-inflation identities (eq 2.25)
p1 = p1(-1) + pi1;
p2 = p2(-1) + pi2;

// [6] Aggregate consumer price index (eq 2.26)
pc = omegac1*p1 + omegac2*p2;

// [7] Aggregate inflation (eq 2.27)
pi_agg = omegac1*pi1 + omegac2*pi2;

// [8] Aggregate output gap (eq 2.29)
ytilde_agg = mu1*ytilde1 + mu2*ytilde2;

// [9] Aggregate fiscal gap (eq 2.28)
ftilde_agg = omegag1*(ftilde1 + ytilde1) + omegag2*(ftilde2 + ytilde2) - ytilde_agg;

// ----- OPTIMAL POLICY RULES -----

// [10-11] Optimal sectoral fiscal policy (eq 3.32)
// ftilde*_kt = -[(1+phi)(1+lambda_k) / (1+(1+phi)lambda_k)] ytilde*_kt
//              -[theta(1-chi_k)phi   / (1+(1+phi)lambda_k)] pi*_kt
ftilde1 = -((1+phi)*(1+lambda1))/(1+(1+phi)*lambda1) * ytilde1
          - (theta*(1-chi1)*phi)/(1+(1+phi)*lambda1) * pi1;

ftilde2 = -((1+phi)*(1+lambda2))/(1+(1+phi)*lambda2) * ytilde2
          - (theta*(1-chi2)*phi)/(1+(1+phi)*lambda2) * pi2;

// [12] Optimal monetary policy (eq 3.33)
// theta * sum_k [(1-chi_k)mu_k / (1+lambda_k(1+phi))] pi_kt
//    = -sum_k [mu_k / (1+lambda_k(1+phi))] ytilde_kt
theta * ( (1-chi1)*mu1/(1+lambda1*(1+phi)) * pi1
        + (1-chi2)*mu2/(1+lambda2*(1+phi)) * pi2 )
    = -( mu1/(1+lambda1*(1+phi)) * ytilde1
       + mu2/(1+lambda2*(1+phi)) * ytilde2 );

// ----- INTEREST RATE -----

// [13] Sectoral IS curve, sector 1 — backs out i_nom (eq 2.22)
// ytilde_kt = E ytilde_{k,t+1} - (i_t - E pi_{k,t+1} - rbar_kt) - chi*_k E Delta ftilde_{k,t+1}
// where rbar_kt = E Delta a_{k,t+1} = a_k(+1) - a_k
ytilde1 = ytilde1(+1) - (i_nom - pi1(+1) - (a1(+1) - a1))
          - chistar1*(ftilde1(+1) - ftilde1);

// ----- SHOCK PROCESSES -----

// [14-15] AR(1) sectoral productivity
// MISSING DATA: Cox et al. set rho_a = 0.85 but do not specify sigma^2_a.
// Table 3 reports "variance multipliers" (var(X)/var(eps)), so normalising
// var(eps) = 1 gives variance multipliers directly.
a1 = rho_a * a1(-1) + eps1;
a2 = rho_a * a2(-1) + eps2;

end;

// =========================================================================
// SHOCK SPECIFICATION
// =========================================================================
shocks;
// Normalised to unit variance. Cox et al. Table 3 reports variance
// multipliers, so var(X) from simulation = variance multiplier directly.
// Shocks are independent across sectors (Cox et al. assumption).
var eps1 = 1;
var eps2 = 1;
end;

// =========================================================================
// SOLUTION & OUTPUT
// =========================================================================
steady;
check;

// IRFs to 40 periods (= 40 months under Cox et al. monthly calibration)
stoch_simul(order=1, irf=40, nograph);

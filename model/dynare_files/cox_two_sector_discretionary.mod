// =========================================================================
// Cox et al. (2025) — Discretionary (Time-Consistent) Optimal Policy
// with Budget Constraint (gbar=0, rho=0)
//
// Uses Dynare's discretionary_policy to find the SAME time-consistent
// solution that Cox et al. and Eugenelo derive analytically.
// Compare to cox_two_sector_constrained.mod (Eugenelo rules).
// =========================================================================

var ytilde1 ytilde2 pi1 pi2 ftilde1 ftilde2
    p1 p2 pc pi_agg ytilde_agg ftilde_agg
    i_nom a1 a2
    g1 g2 y1 y2;

varexo eps1 eps2;

parameters beta phi chi theta rho_a
           omegac1 omegac2 omegag1 omegag2
           alpha1 alpha2
           mu1 mu2 chi1 chi2 chistar1 chistar2 chistar
           lambda1 lambda2;

beta    = 0.997;
phi     = 4;
chi     = 0.185;
theta   = 6;
rho_a   = 0.85;

omegac1 = 0.6; omegac2 = 0.4;
omegag1 = 0.3; omegag2 = 0.7;
alpha1  = 0.25; alpha2  = 0.75;

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
// PLANNER OBJECTIVE: Cox et al. eq 3.31 (period loss, quadratic)
// =========================================================================
planner_objective
    - 0.5*mu1*(theta*(1-chi1)/lambda1*pi1*pi1
               + (1+phi)*ytilde1*ytilde1
               + chistar1*ftilde1*ftilde1)
    - 0.5*mu2*(theta*(1-chi2)/lambda2*pi2*pi2
               + (1+phi)*ytilde2*ytilde2
               + chistar2*ftilde2*ftilde2);

// =========================================================================
// STRUCTURAL MODEL (no policy rules)
// i_nom removed from var list — it's an instrument
// g1 is the other instrument (g2 determined by budget constraint)
// =========================================================================
model(linear);

// [1-2] Sectoral Phillips Curves
pi1 = beta*pi1(+1) + lambda1*(1+phi)*ytilde1 - lambda1*chistar1*ftilde1;
pi2 = beta*pi2(+1) + lambda2*(1+phi)*ytilde2 - lambda2*chistar2*ftilde2;

// [3] Demand relation, sector 1
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

// [10] IS curve (structural, links i_nom to allocation)
ytilde1 = ytilde1(+1) - (i_nom - pi1(+1) - (a1(+1)-a1))
          - chistar1*(ftilde1(+1)-ftilde1);

// [11-12] Shocks
a1 = rho_a*a1(-1) + eps1;
a2 = rho_a*a2(-1) + eps2;

// [12-13] Government spending gaps (g_k = ftilde_k + ytilde_k)
g1 = ftilde1 + ytilde1;
g2 = ftilde2 + ytilde2;

// [14-15] Output gaps (y_k = ytilde_k)
y1 = ytilde1;
y2 = ytilde2;

// [16] Zero-budget constraint
omegag1*g1 + omegag2*g2 = 0;

end;

shocks;
var eps1 = 1;
var eps2 = 1;
end;

// =========================================================================
// DISCRETIONARY (TIME-CONSISTENT) OPTIMAL POLICY
// This is what Cox et al. and Eugenelo solve analytically.
// =========================================================================
discretionary_policy(instruments=(i_nom, g1), irf=40, nograph);

%% verify_constrained_focs.m
%  Manual re-derivation of the constrained optimal fiscal rule for K=2
%  Compares: (1) Eugenelo analytical formulas, (2) direct FOC solution,
%            (3) Dynare discretionary_policy
%
%  The constrained problem (Cox et al. + budget constraint):
%    min  sum_k mu_k [theta(1-chi_k)/lambda_k * pi_k^2
%                     + (1+phi)*ytilde_k^2 + chistar_k*ftilde_k^2] / 2
%    s.t. Phillips curves, demand relation, price identities,
%         aggregation, and budget constraint.
%
%  Period-by-period optimization: take E[pi_{k,t+1}] as given.
%  This is the Cox et al. / Eugenelo approach.

clear; clc;

%% Parameters (asymmetric weights where constraint binds)
beta    = 0.997;
phi     = 4;        % inverse Frisch (= varphi in Eugenelo notation)
chi     = 0.185;
theta   = 6;

omegac1 = 0.6; omegac2 = 0.4;
omegag1 = 0.3; omegag2 = 0.7;
alpha1  = 0.25; alpha2  = 0.75;

% Derived
mu1      = (1-chi)*omegac1 + chi*omegag1;
mu2      = (1-chi)*omegac2 + chi*omegag2;
chi1     = chi*omegag1/mu1;
chi2     = chi*omegag2/mu2;
chistar1 = chi1/(1-chi1);
chistar2 = chi2/(1-chi2);
chistar  = chi/(1-chi);
lambda1  = (1-alpha1)*(1-beta*alpha1)/alpha1;
lambda2  = (1-alpha2)*(1-beta*alpha2)/alpha2;

fprintf('=== Parameters ===\n');
fprintf('mu1=%.4f, mu2=%.4f\n', mu1, mu2);
fprintf('chi1=%.4f, chi2=%.4f\n', chi1, chi2);
fprintf('chistar1=%.4f, chistar2=%.4f\n', chistar1, chistar2);
fprintf('lambda1=%.4f, lambda2=%.4f\n', lambda1, lambda2);

%% =====================================================================
%  PART 1: Direct FOC solution (period-by-period, Cox et al. style)
%  =====================================================================
%
%  The planner chooses {ytilde_k, pi_k, ftilde_k, p_k, p_c, ytilde, ftilde}
%  to minimize the loss, taking E[pi_{k,t+1}] and p_{k,t-1} as given.
%
%  Following Cox et al. Appendix C, the key FOC system is:
%
%  From FOC(pi_k) + FOC(p_k):
%    theta(1-chi_k)/lambda_k * pi_k + phi^pi_k + phi^y_k - (1-chi_k)*v_y = 0
%    => phi^pi_k = -theta(1-chi_k)/lambda_k * pi_k - phi^y_k + (1-chi_k)*v_y
%
%  From FOC(ytilde_k):
%    (1+phi)*ytilde_k - chi*_k*ftilde_k
%    - phi^y_k*(1+chi*_k)
%    + phi^pi_k*lambda_k*(1+phi) + phi^pi_k*lambda_k*chi*_k
%    + v_y = 0
%
%  From FOC(ftilde_k) (constrained, k ~= residual):
%    chi*_k*(ftilde_k - chi_k/(1-chi_i) * ftilde_i * (omegag_k/omegag_i)^rho)
%    + phi^y_k*chi*_k - phi^y_i*chi_k/(1-chi_i)*(omegag_k/omegag_i)^rho
%    - phi^pi_k*lambda_k*chi*_k + phi^pi_i*lambda_i*chi_k/(1-chi_i)*(omegag_k/omegag_i)^rho
%    - chi_k*v_y*(1 - (omegag_k/omegag_i)^rho) = 0
%
%  With rho=0, (omegag_k/omegag_i)^rho = 1, so the v_y term vanishes.
%
%  Additionally, from aggregation FOCs:
%    v_p = (1-chi)*v_y
%    v_g = -chi*v_y
%
%  And the budget constraint: omegag1*(ftilde1+ytilde1) + omegag2*(ftilde2+ytilde2) = 0

%% Solve the condensed FOC system symbolically
%  Following Eugenelo Appendix E, eqs (5a)-(5d):
%
%  (5a) "pi_foc": -theta/lambda_k * pi_k + phi^pi_k/(1-chi_k) + phi^y_k/(1-chi_k) - v_y = 0
%  (5b) "y_foc":  (1+phi+chi*_k)*(ytilde_k + phi^pi_k*lambda_k) - chi*_k*g_k
%                  - phi^y_k/(1-chi_k) + v_y = 0
%  (5c) "g_foc" (rho=0):
%        1/(1-chi_k)*(ftilde_k + theta/lambda_k*pi_k) - 1/(1-chi_i)*(ftilde_i + theta/lambda_i*pi_i)
%        - (1+lambda_k)/(1-chi_k)*phi^pi_k + (1+lambda_i)/(1-chi_i)*phi^pi_i = 0
%  (5d) v_p = -v_g*(1-chi)/chi = v_y*(1-chi)
%
%  From (5a) and (5b), eliminate phi^y_k to get phi^pi_k:
%  (eq:phi_pi in appendix):
%    phi^pi_k = (1-chi_k)/(1+lambda_k+phi*lambda_k*(1-chi_k))
%               * (chi*_k*g_k - ytilde_k*(1+phi+chi*_k) + theta/lambda_k*pi_k)
%
%  Note: g_k = ftilde_k + ytilde_k, so:
%    chi*_k*g_k - ytilde_k*(1+phi+chi*_k) = chi*_k*ftilde_k - ytilde_k*(1+phi)

% Define notation: for sector k, let
%   Dk = 1 + lambda_k + phi*lambda_k*(1-chi_k)  (denominator in phi^pi_k)
Dk = @(lam,chik) 1 + lam + phi*lam*(1-chik);
D1 = Dk(lambda1, chi1);
D2 = Dk(lambda2, chi2);

fprintf('\nD1 = %.6f, D2 = %.6f\n', D1, D2);

%% Now substitute phi^pi_k into the g_foc (5c) for k=1, i=2 (residual):
%
%  1/(1-chi1)*(ftilde1 + theta/lambda1*pi1)
%  - 1/(1-chi2)*(ftilde2 + theta/lambda2*pi2)
%  - (1+lambda1) * [chi*1*ftilde1 - ytilde1*(1+phi) + theta/lambda1*pi1] / D1
%  + (1+lambda2) * [chi*2*ftilde2 - ytilde2*(1+phi) + theta/lambda2*pi2] / D2
%  = 0
%
%  Collect terms in ftilde1, ytilde1, pi1, ftilde2, ytilde2, pi2:

% Coefficient on ftilde1:
%   1/(1-chi1) - (1+lambda1)*chistar1/D1
c_f1 = 1/(1-chi1) - (1+lambda1)*chistar1/D1;

% Coefficient on ytilde1:
%   (1+lambda1)*(1+phi)/D1
c_y1 = (1+lambda1)*(1+phi)/D1;

% Coefficient on pi1:
%   theta/lambda1 * [1/(1-chi1) - (1+lambda1)/D1]
c_pi1 = theta/lambda1 * (1/(1-chi1) - (1+lambda1)/D1);

% Coefficient on ftilde2:
%   -1/(1-chi2) + (1+lambda2)*chistar2/D2
c_f2 = -1/(1-chi2) + (1+lambda2)*chistar2/D2;

% Coefficient on ytilde2:
%   -(1+lambda2)*(1+phi)/D2
c_y2 = -(1+lambda2)*(1+phi)/D2;

% Coefficient on pi2:
%   theta/lambda2 * [-1/(1-chi2) + (1+lambda2)/D2]
c_pi2 = theta/lambda2 * (-1/(1-chi2) + (1+lambda2)/D2);

fprintf('\n=== GOC coefficients (g_foc equation) ===\n');
fprintf('c_f1=%.6f, c_y1=%.6f, c_pi1=%.6f\n', c_f1, c_y1, c_pi1);
fprintf('c_f2=%.6f, c_y2=%.6f, c_pi2=%.6f\n', c_f2, c_y2, c_pi2);

%% The g_foc gives us: c_f1*f1 + c_y1*y1 + c_pi1*pi1 + c_f2*f2 + c_y2*y2 + c_pi2*pi2 = 0
%
%  Using g_k = f_k + y_k, rewrite:
%    c_f1*(g1-y1) + c_y1*y1 + c_pi1*pi1 + c_f2*(g2-y2) + c_y2*y2 + c_pi2*pi2 = 0
%    c_f1*g1 + (c_y1-c_f1)*y1 + c_pi1*pi1 + c_f2*g2 + (c_y2-c_f2)*y2 + c_pi2*pi2 = 0
%
%  Combined with budget constraint: omegag1*g1 + omegag2*g2 = 0 => g2 = -omegag1/omegag2*g1
%
%  Substitute g2:
%    c_f1*g1 + c_f2*(-omegag1/omegag2)*g1 + (c_y1-c_f1)*y1 + c_pi1*pi1
%    + (c_y2-c_f2)*y2 + c_pi2*pi2 = 0
%
%  Solve for g1:
coeff_g1 = c_f1 - c_f2*omegag1/omegag2;
g1_y1  = -(c_y1-c_f1) / coeff_g1;
g1_pi1 = -c_pi1 / coeff_g1;
g1_y2  = -(c_y2-c_f2) / coeff_g1;
g1_pi2 = -c_pi2 / coeff_g1;

fprintf('\n=== DIRECT FOC: g1 = a*y1 + b*pi1 + c*y2 + d*pi2 ===\n');
fprintf('  g1 = %.6f*y1 + %.6f*pi1 + %.6f*y2 + %.6f*pi2\n', ...
    g1_y1, g1_pi1, g1_y2, g1_pi2);

%% =====================================================================
%  PART 2: Eugenelo formula (from policy_two.tex, rho=0)
%  =====================================================================
%  g1 = R12*(D2_ratio/D1_ratio)*g2
%       - phi*y1/(1+lambda1*(1+phi))
%       - theta*phi*(1-chi1)*pi1/(1+lambda1*(1+phi))
%       + R12/D1_ratio * [phi*y2/D2 + theta*phi*(1-chi2)*pi2/D2]
%
%  where D_ratio_k = (1+lambda_k*(1+phi)) / (1+lambda_k+phi*lambda_k*(1-chi_k))
%        R12 = (1-chi1)/(1-chi2)

Dk_num = @(lam) 1 + lam*(1+phi);
Dk_den = @(lam,chik) 1 + lam*(1+phi*(1-chik));  % = D_k
D_ratio = @(lam,chik) Dk_num(lam)/Dk_den(lam,chik);

R12 = (1-chi1)/(1-chi2);
D1r = D_ratio(lambda1, chi1);
D2r = D_ratio(lambda2, chi2);

% Eugenelo formula coefficients for g1 = ... (with g2 = -omegag1/omegag2*g1)
eug_g2_coeff = R12 * D2r / D1r;
eug_y1  = -phi / Dk_num(lambda1);
eug_pi1 = -theta*phi*(1-chi1) / Dk_num(lambda1);
eug_y2  = R12/D1r * phi / Dk_den(lambda2,chi2);
eug_pi2 = R12/D1r * theta*phi*(1-chi2) / Dk_den(lambda2,chi2);

% Substitute g2 = -(omegag1/omegag2)*g1:
%   g1 = eug_g2_coeff * (-(omegag1/omegag2)*g1) + eug_y1*y1 + ...
%   g1*(1 + eug_g2_coeff*omegag1/omegag2) = eug_y1*y1 + ...
denom = 1 + eug_g2_coeff*omegag1/omegag2;
eug_g1_y1  = eug_y1 / denom;
eug_g1_pi1 = eug_pi1 / denom;
eug_g1_y2  = eug_y2 / denom;
eug_g1_pi2 = eug_pi2 / denom;

fprintf('\n=== EUGENELO FORMULA: g1 = a*y1 + b*pi1 + c*y2 + d*pi2 ===\n');
fprintf('  g1 = %.6f*y1 + %.6f*pi1 + %.6f*y2 + %.6f*pi2\n', ...
    eug_g1_y1, eug_g1_pi1, eug_g1_y2, eug_g1_pi2);

%% =====================================================================
%  PART 3: Compare
%  =====================================================================
fprintf('\n=== COMPARISON ===\n');
fprintf('%15s %12s %12s %12s\n', 'Coefficient', 'Direct FOC', 'Eugenelo', 'Match?');
pairs = {'y1', g1_y1, eug_g1_y1; 'pi1', g1_pi1, eug_g1_pi1; ...
         'y2', g1_y2, eug_g1_y2; 'pi2', g1_pi2, eug_g1_pi2};
for j = 1:size(pairs,1)
    match = abs(pairs{j,2}-pairs{j,3}) < 1e-10;
    if match, ms = 'YES'; else, ms = 'NO'; end
    fprintf('%15s %12.6f %12.6f %12s\n', pairs{j,1}, pairs{j,2}, pairs{j,3}, ms);
end

%% =====================================================================
%  PART 4: Monetary policy FOC
%  =====================================================================
%  From Eugenelo policy_two.tex lines 50-53:
%  sum_k mu_k * theta*(1-chi_k)/lambda_k * (lambda_k+phi*lambda_k*(1-chi_k))/D_k * pi_k
%  = sum_k mu_k * [chi_k*g_k/D_k - y_k*(1-chi_k)*(1+phi+chistar_k)/D_k]
%
%  From Cox et al. Appendix C, the monetary policy condition comes from
%  combining the FOCs and eliminating multipliers.
%  Under the constrained problem, the monetary FOC should be the same
%  aggregation condition.

fprintf('\n=== MONETARY POLICY ===\n');
fprintf('Eugenelo MP condition involves g_k on the RHS (cannot simplify to\n');
fprintf('pure output target as in unconstrained case).\n');
fprintf('Both models should satisfy this condition in equilibrium.\n');

%% =====================================================================
%  PART 5: Diagnose Dynare discretionary_policy discrepancy
%  =====================================================================
fprintf('\n=== DIAGNOSIS ===\n');
fprintf('If Direct FOC matches Eugenelo: formulas are correctly derived.\n');
fprintf('Dynare discretionary_policy solves the Markov-perfect equilibrium,\n');
fprintf('which includes an additional value-function channel:\n');
fprintf('  phi^p_k(MP) = phi^p_k(static) + beta * dV/dp_k\n');
fprintf('The dV/dp_k term captures how current p_k affects future welfare\n');
fprintf('through the demand relation (relative price dispersion).\n');
fprintf('This is absent in the Cox et al. / Eugenelo static approach.\n');

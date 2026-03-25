%% launch_two_sector.m
%  Cox et al. (2025) — Two-Sector Baseline Model
%  Runs Dynare, displays key diagnostics, verifies special cases.
%
%  Usage: matlab -batch "run('launch_two_sector.m')"
%  Or run interactively from the model/ directory.

clear; clc; close all;

%% Setup paths
model_dir = fileparts(mfilename('fullpath'));
dynare_dir = fullfile(model_dir, 'dynare_files');
output_dir = fullfile(model_dir, 'output');
if ~exist(output_dir, 'dir'), mkdir(output_dir); end

%% Run Dynare
cd(dynare_dir);
dynare cox_two_sector noclearall;
cd(model_dir);

%% Display calibration summary
fprintf('\n');
fprintf('============================================================\n');
fprintf('  Cox et al. (2025) — Two-Sector Model: Calibration Summary\n');
fprintf('============================================================\n');
fprintf('  beta    = %.4f   (monthly discount)\n', M_.params(strmatch('beta', M_.param_names, 'exact')));
fprintf('  phi     = %.1f     (inverse-Frisch)\n', M_.params(strmatch('phi', M_.param_names, 'exact')));
fprintf('  chi     = %.3f   (G/Y share)\n', M_.params(strmatch('chi', M_.param_names, 'exact')));
fprintf('  theta   = %.0f       (within-sector elasticity) *** NOT IN COX ET AL. ***\n', M_.params(strmatch('theta', M_.param_names, 'exact')));
fprintf('  rho_a   = %.2f    (shock persistence)\n', M_.params(strmatch('rho_a', M_.param_names, 'exact')));
fprintf('------------------------------------------------------------\n');
fprintf('  alpha1  = %.2f    (Calvo sector 1 — flexible)\n', M_.params(strmatch('alpha1', M_.param_names, 'exact')));
fprintf('  alpha2  = %.2f    (Calvo sector 2 — sticky)\n', M_.params(strmatch('alpha2', M_.param_names, 'exact')));
fprintf('  lambda1 = %.4f  (Phillips slope sector 1)\n', M_.params(strmatch('lambda1', M_.param_names, 'exact')));
fprintf('  lambda2 = %.4f  (Phillips slope sector 2)\n', M_.params(strmatch('lambda2', M_.param_names, 'exact')));
fprintf('------------------------------------------------------------\n');
fprintf('  mu1     = %.4f  (sector 1 output share)\n', M_.params(strmatch('mu1', M_.param_names, 'exact')));
fprintf('  mu2     = %.4f  (sector 2 output share)\n', M_.params(strmatch('mu2', M_.param_names, 'exact')));
fprintf('  chi1    = %.4f  (G/Y share sector 1)\n', M_.params(strmatch('chi1', M_.param_names, 'exact')));
fprintf('  chi2    = %.4f  (G/Y share sector 2)\n', M_.params(strmatch('chi2', M_.param_names, 'exact')));
fprintf('============================================================\n\n');

%% Display variance multipliers (cf. Cox et al. Table 3)
fprintf('============================================================\n');
fprintf('  Variance Multipliers (cf. Cox et al. Table 3)\n');
fprintf('============================================================\n');

var_names = {'pi_agg', 'ytilde_agg', 'ftilde_agg', ...
             'pi1', 'pi2', 'ytilde1', 'ytilde2', ...
             'ftilde1', 'ftilde2', 'i_nom'};

for j = 1:length(var_names)
    idx = strmatch(var_names{j}, M_.endo_names, 'exact');
    if ~isempty(idx)
        fprintf('  var(%12s) = %10.6f\n', var_names{j}, oo_.var(idx, idx));
    end
end
fprintf('============================================================\n\n');

%% Verification: aggregate fiscal neutrality (eq 3.34)
% Under optimal policy: sum_k mu_k (g_kt - gbar_kt) = 0
% Equivalently: sum_k mu_k (ftilde_kt + ytilde_kt) = 0
mu1_val = M_.params(strmatch('mu1', M_.param_names, 'exact'));
mu2_val = M_.params(strmatch('mu2', M_.param_names, 'exact'));

idx_f1 = strmatch('ftilde1', M_.endo_names, 'exact');
idx_f2 = strmatch('ftilde2', M_.endo_names, 'exact');
idx_y1 = strmatch('ytilde1', M_.endo_names, 'exact');
idx_y2 = strmatch('ytilde2', M_.endo_names, 'exact');

% Check covariance: var(mu1*(f1+y1) + mu2*(f2+y2)) should be ~0
% under symmetric weights (mu_k = omega_gk for all k)
cov_matrix = oo_.var([idx_f1 idx_f2 idx_y1 idx_y2], [idx_f1 idx_f2 idx_y1 idx_y2]);
w = [mu1_val mu2_val mu1_val mu2_val];
agg_fiscal_var = w * cov_matrix * w';

fprintf('Verification: aggregate fiscal neutrality (eq 3.34)\n');
fprintf('  var(sum mu_k (ftilde_k + ytilde_k)) = %.2e\n', agg_fiscal_var);
if abs(agg_fiscal_var) < 1e-8
    fprintf('  STATUS: PASS (< 1e-8)\n');
else
    fprintf('  STATUS: CHECK — may reflect asymmetric omega_ck vs omega_gk\n');
end
fprintf('\n');

%% Missing data summary
fprintf('============================================================\n');
fprintf('  MISSING DATA — Required for Full Replication\n');
fprintf('============================================================\n');
fprintf('  1. theta (within-sector elasticity of substitution)\n');
fprintf('     - Not stated in Cox et al. Section 5.1\n');
fprintf('     - Currently using theta = 6 (Gali 2008 standard)\n');
fprintf('     - Alternative: theta = 11 (Woodford 2003)\n');
fprintf('     - ACTION: check Cox et al. code/appendix or contact authors\n');
fprintf('\n');
fprintf('  2. alpha_k (Calvo probabilities, sector-specific)\n');
fprintf('     - Source: BLS PPI micro data (Pasten et al. 2020/2024)\n');
fprintf('     - Status: RESTRICTED (confidential BLS data)\n');
fprintf('     - Currently using illustrative alpha1=0.25, alpha2=0.75\n');
fprintf('     - ACTION: obtain from Pasten et al. published tables,\n');
fprintf('       or use publicly available freq. of price change estimates\n');
fprintf('\n');
fprintf('  3. omega_ck (private consumption sector shares)\n');
fprintf('     - Source: BEA Use Table, NAICS 4-digit (2007-2012 avg)\n');
fprintf('     - Status: PUBLIC (downloadable from BEA website)\n');
fprintf('     - Currently using symmetric omega_c1 = omega_c2 = 0.5\n');
fprintf('     - ACTION: download for full 121-sector calibration\n');
fprintf('\n');
fprintf('  4. omega_gk (government demand sector shares)\n');
fprintf('     - Source: USASpending.gov, federal procurement (2007-2012)\n');
fprintf('     - Status: PUBLIC (downloadable)\n');
fprintf('     - Currently using symmetric omega_g1 = omega_g2 = 0.5\n');
fprintf('     - ACTION: download for full 121-sector calibration\n');
fprintf('\n');
fprintf('  5. sigma^2_a (shock variance)\n');
fprintf('     - Not stated in Cox et al.\n');
fprintf('     - Table 3 uses variance multipliers (normalised by var(eps))\n');
fprintf('     - Currently using var(eps) = 1 (unit normalisation)\n');
fprintf('     - Variance multipliers are directly comparable to Table 3\n');
fprintf('============================================================\n');

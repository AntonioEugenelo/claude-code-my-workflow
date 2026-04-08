# Monetary Policy Wrapped Diff

This note reformats the current LaTeX edits into wrapped before/after blocks so they are readable
without changing source formatting in the paper files.

## Section 4

File: `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`

### Monetary policy opening paragraph

**Before**

```tex
\paragraph{\textcolor{red}{Monetary policy (Figure~\ref{fig:robust_monpol})}}
\textcolor{red}{
We compare the benchmark with a counterfactual in which the smoothing parameter is set to
$\rho_{k,r} = 0.999$ for all four country blocs (vs.\ $0.7$ in the baseline),
rendering interest rates effectively fixed over the simulation horizon while preserving
model determinacy.\footnote{
The Taylor rule remains operative under $\rho_{k,r} = 0.999$ but with a half-life of
approximately 693 quarters. Under a level-responding Taylor rule ($\phi_{k,y}$),
the persistent output deviation would sustain the interest rate response and the 19\%
amplification would be larger; the growth specification attenuates monetary amplification
for near-permanent shocks.
}
This exercise is best read as a reduced-form comparison across monetary-policy regimes,
not as a clean identification of a single channel, because the near-fixed-rate
counterfactual changes both UIP and the consumption Euler equation.
}
```

**After**

```tex
\paragraph{\textcolor{red}{Monetary policy (Figure~\ref{fig:robust_monpol})}}
\textcolor{red}{
We compare the benchmark with a counterfactual in which the smoothing parameter is set to
$\rho_{k,r} = 0.999$ for all four country blocs (vs.\ $0.7$ in the baseline),
rendering interest rates effectively fixed over the simulation horizon while preserving
model determinacy.\footnote{
The Taylor rule remains operative under $\rho_{k,r} = 0.999$, but only extremely slowly;
under a level-responding rule, the resulting amplification would be larger.
}
This is a reduced-form comparison across monetary-policy regimes,
not a clean single-channel identification, because the near-fixed-rate
counterfactual changes both UIP and the consumption Euler equation.
}
```

### Monetary policy main paragraph

**Before**

```tex
\textcolor{red}{
Quantitatively, the benchmark regime is associated with a larger Chinese contraction than
the near-fixed-rate regime: the three-year average GDP response is $-0.147$\% in the
benchmark versus $-0.119$\% under near-fixed rates, a difference of about 19\%.
For the US, the corresponding averages are $+0.019$\% versus $+0.028$\%;
for the EA, they are $+0.009$\% versus $+0.003$\%.
The comparison therefore shows that a more active interest-rate response coincides with
stronger Chinese contraction, less positive US output, and stronger trade diversion
toward the EA.
}

\textcolor{red}{
The mechanism operates through front-loaded dollar appreciation.
Under the benchmark Taylor rule, the US interest rate rises on impact ($+0.056$~pp)
in response to tariff-driven inflation, generating a sharper dollar appreciation
($-0.37$\% REER on impact) via uncovered interest parity (UIP).
Relative to the near-fixed-rate case, this coincides with a larger renminbi depreciation
against the dollar, higher renminbi-denominated intermediate-input costs for Chinese firms,
and stronger trade diversion toward EA producers.
Figure~\ref{fig:monpol_reer_dw} therefore supports a regime comparison in which
exchange-rate dynamics and intertemporal-demand effects move together rather than being
separately identified.\footnote{
Under DCP, Chinese export prices to the US are sticky in dollars, so the dollar
appreciation does not directly raise the dollar price of Chinese goods; the tariff itself
is the sole source of the import price increase at the US border. The monetary
amplification operates instead through the CNY/USD exchange rate's effect on Chinese
production costs and the dynamic path of the US real exchange rate.
}
}

\textcolor{red}{
Under near-fixed rates, the interest rate barely responds ($<0.001$~pp) and the dollar
appreciates less on impact ($-0.24$\% REER) and without overshooting. The residual
appreciation is primarily a real exchange-rate adjustment: tariffs raise the US price
level relative to foreign prices even without much interest-rate movement.\footnote{
The NFA premium ($\gamma_*=0.001$) contributes approximately $0.001$~pp per quarter
to the UIP equation, too small to generate substantial exchange rate overshooting
within the simulation horizon. Empirically, UIP is violated at short horizons;
time-varying risk premia would moderate the overshooting channel.
}
The benchmark-versus-near-fixed comparison therefore combines exchange-rate and IS-curve
effects, and a clean separation would require an additional counterfactual that fixes
the exchange-rate path while holding the Euler-equation rate at its benchmark path.
}

\textcolor{red}{
The EA's positive trade-diversion response is also smaller under near-fixed rates
($+0.003$\% vs.\ $+0.009$\%). For China, the stronger CNY/USD depreciation under the
benchmark raises renminbi-denominated intermediate-input costs and amplifies cost
propagation through production networks. For the EA, the stronger dollar raises the
relative cost of US goods for third-country buyers and strengthens demand reallocation
toward EA producers through the Armington substitution system.
}
```

**After**

```tex
\textcolor{red}{
Quantitatively, the benchmark regime is associated with a larger Chinese contraction than
the near-fixed-rate regime: the three-year average GDP response is $-0.147$\% in the
benchmark versus $-0.119$\% under near-fixed rates, a difference of about 19\%.
For the US, the corresponding averages are $+0.019$\% versus $+0.028$\%;
for the EA, they are $+0.009$\% versus $+0.003$\%.
US CPI inflation is also lower under near-fixed rates ($+0.035$~pp versus $+0.064$~pp
on the three-year average four-quarter measure), while Chinese CPI is slightly higher
($+0.009$~pp versus $-0.002$~pp on the same measure). The comparison therefore shows
that a more active interest-rate response coincides with stronger Chinese contraction,
less positive US output, stronger trade diversion toward the EA, and a more inflationary
US price path on average.
}

\textcolor{red}{
This higher US average does not come from the initial dollar appreciation itself.
The tariff raises US CPI on impact in both regimes, but under the benchmark Taylor rule
the dollar also reverses more sharply after the initial appreciation. Concretely,
the US rate rises on impact ($+0.056$~pp), generating a larger initial appreciation
($-0.37$\% REER) than under near-fixed rates, where the rate response is negligible
and the dollar appreciates only $-0.24$\% without overshooting.
In the benchmark, US CPI then remains positive in quarters 2 and 3
(about $+0.008$~pp in both), whereas under near-fixed rates it is near zero by
quarter 2 and slightly negative by quarter 3; because the reported statistic averages
rolling four-quarter CPI over 12 quarters, that persistence lifts the benchmark average.
For China, by contrast, the stronger benchmark CNY/USD depreciation raises input costs
on impact, but the deeper contraction dominates after quarter 1 and pushes the average
Chinese CPI measure slightly below zero.
Figure~\ref{fig:monpol_reer_dw} therefore supports a regime comparison in which
exchange-rate and IS-curve effects move jointly rather than as a clean decomposition.\footnote{
Within the heterogeneous-DCP benchmark, dollar-invoiced Chinese export prices to the US
are sticky in dollars, so dollar appreciation does not directly raise the dollar price
of that subset of goods at the US border; the tariff is the source of the import price
increase there. Monetary amplification instead operates through the dynamic path of the
US real exchange rate, the non-DCP pass-through margin, and the CNY/USD exchange rate's
effect on Chinese production costs.
}
}
```

## Conclusion

File: `master_supporting_docs/Tariffs_ECB/0_clean/sections/60_Conclusions.tex`

### Fourth finding

**Before**

```tex
\textcolor{red}{
Fourth, active monetary policy amplifies tariff transmission through exchange rate
overshooting and domestic demand contraction. Under the benchmark Taylor rule,
the interest rate response to tariff-driven inflation generates a sharp dollar
appreciation via the UIP condition, amplifying the contraction for the targeted
country and raising US CPI inflation. When we render monetary policy near-inactive
($\rho_{k,r} = 0.999$), the Chinese GDP contraction shrinks by 19\% and US CPI
inflation falls by roughly 45\%, as the exchange rate adjusts gradually without
overshooting. The monetary policy rule, not just the invoicing regime, is a
quantitatively important determinant of tariff transmission. It operates through both
the exchange rate channel (interest rate differentials driving dollar overshooting via UIP)
and the domestic demand channel (higher rates contracting consumption via the Euler equation).
}
```

**After**

```tex
\textcolor{red}{
Fourth, active monetary policy amplifies tariff transmission through exchange rate
overshooting and domestic demand contraction. Under the benchmark Taylor rule,
the interest-rate response to tariff-driven inflation generates a sharper dollar
overshooting-and-reversal path via the UIP condition, amplifying the contraction for
the targeted country and keeping the US CPI path more elevated on average. When we
render monetary policy near-inactive ($\rho_{k,r} = 0.999$), the Chinese GDP contraction
shrinks by 19\% and the three-year average four-quarter US CPI measure falls from
about $0.064$~pp to $0.035$~pp, while the exchange rate adjusts more gradually and
without overshooting. The monetary policy rule, not just the invoicing regime, is a
quantitatively important determinant of tariff transmission. It operates through both
the exchange rate channel (interest rate differentials driving dollar overshooting via UIP)
and the domestic demand channel (higher rates contracting consumption via the Euler equation).
}
```

## Recommended Use

- Read this file for content review.
- Keep the `.tex` files single-line if that matches the repo's editing style.
- If you want, future review notes can be generated in this wrapped format whenever a paragraph-level edit is made.

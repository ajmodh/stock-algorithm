import adx_algo
values_input= [[
30.20,
30.28,
30.45,
29.35,
29.35,
29.29,
28.83,
28.73,
28.67,
28.85,
28.64,
27.68,
27.21,
26.87,
27.41,
26.94,
26.52,
26.52,
27.09,
27.69,
28.45,
28.53,
28.67,
29.01,
29.87,
29.80,
29.75,
30.65,
30.60,
30.76,
31.17,
30.89,
30.04,
30.66,
30.60,
31.97,
32.10,
32.03,
31.63,
31.85,
32.71,
32.76,
32.58,
32.13,
33.12,
33.19,
32.52,
32.44,
33.22,
32.83,
33.62,
33.75,
33.60,
34.08,
34.58,
34.22,
34.77,
34.74,
35.01,
34.94,
34.42,
34.40,
34.16,
33.34,
33.39,
33.51,
33.96,
34.42,
34.72,
33.94,
33.66,
34.51,
34.87,
34.75,
35.17,
36.16,
36.45,
36.03,
36.45,
36.74,
36.61,
36.83,
36.84,
36.89,
36.38,
35.99,
35.86,
35.88,
35.73,
36.07,
35.60,
34.98,
35.58,
36.07,
36.21,
36.46,
36.44,
36.54
],
[
29.41,
29.32,
29.96,
28.74,
28.56,
28.41,
28.08,
27.43,
27.66,
27.83,
27.40,
27.09,
26.18,
26.13,
26.63,
26.13,
25.43,
25.35,
25.88,
26.96,
27.14,
28.01,
27.88,
27.99,
28.76,
29.14,
28.71,
28.93,
30.03,
29.39,
30.14,
30.43,
29.35,
29.99,
29.52,
30.94,
31.54,
31.36,
30.92,
31.20,
32.13,
32.23,
31.97,
31.56,
32.21,
32.63,
31.76,
31.78,
32.09,
32.19,
32.76,
33.04,
33.05,
33.33,
33.73,
33.70,
34.20,
34.31,
34.14,
33.57,
33.57,
33.37,
33.21,
32.66,
32.77,
32.92,
33.08,
33.64,
33.86,
33.00,
33.01,
32.87,
34.11,
33.89,
34.44,
35.28,
35.78,
35.60,
36.00,
36.08,
35.79,
36.33,
35.96,
36.41,
35.87,
35.25,
35.19,
35.12,
35.24,
35.62,
34.74,
34.49,
35.00,
35.00,
35.76,
35.83,
35.82,
36.10],
[
29.87,
30.24,
30.10,
28.90,
28.92,
28.48,
28.56,
27.56,
28.47,
28.28,
27.49,
27.23,
26.35,
26.33,
27.03,
26.22,
26.01,
25.46,
27.03,
27.45,
28.36,
28.43,
27.95,
29.01,
29.38,
29.36,
28.91,
30.61,
30.05,
30.19,
31.12,
30.54,
29.78,
30.04,
30.49,
31.47,
32.05,
31.97,
31.13,
31.66,
32.64,
32.59,
32.19,
32.10,
32.93,
33.00,
31.94,
32.39,
32.49,
32.80,
33.38,
33.42,
33.17,
33.63,
33.96,
34.05,
34.73,
34.70,
34.71,
33.89,
33.91,
34.03,
33.62,
32.72,
33.08,
33.06,
33.92,
34.08,
33.96,
33.34,
33.23,
34.47,
34.23,
34.63,
35.05,
36.05,
36.10,
35.99,
36.40,
36.44,
36.33,
36.61,
36.48,
36.48,
36.31,
35.57,
35.22,
35.56,
35.49,
35.87,
34.80,
34.72,
35.30,
36.00,
36.08,
36.16,
36.09,
36.11
]]


print adx_algo.adx_resul(values_input, 14)
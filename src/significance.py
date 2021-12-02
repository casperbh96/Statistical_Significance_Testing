import numpy as np
from scipy import stats
from scipy.stats import levene, f_oneway

def gaussian_test(col, values):
    stat1, p1 = stats.shapiro(values)
    stat2, p2 = stats.normaltest(values)

    print(f"Gaussian: {col}\n\t{p1:5f} (Shapiro-Wilk)\n\t{p2:5f} (D'Agostino's)")


def correlation_test(df):
    pearson = df.corr(method=lambda x, y: stats.pearsonr(x, y)[1])
    spearman = df.corr(method=lambda x, y: stats.spearmanr(x, y)[1])

    pearson = pearson.round(4)
    spearman = spearman.round(4)

    return pearson, spearman

def boldness_test(bold1, bold2, bold3):
    rng = np.random.RandomState(42)
    a_ton_of_text_boldness = rng.uniform(low=0.7, high=2.5, size=200)

    variance_check = [[bold1, bold2], [bold2, bold3]]

    for check in variance_check:
        stat1, p1 = levene(a_ton_of_text_boldness, check, center='mean')
        stat2, p2 = f_oneway(a_ton_of_text_boldness, check)

        print(f'{p1:5f}')
        print(f'{p2:5f}')
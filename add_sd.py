mean = X.groupby(['nucleotide_position', 'percentile']).mean()['obs/exp']
SD = X.groupby(['nucleotide_position', 'percentile']).std()['obs/exp']

ax = sns.tsplot(data=X, time='nucleotide_position', unit = "sample_number", 
           condition='percentile', value='obs/exp', ci="sd")

for percentil in set(X['percentile']):
    ax.errorbar(range(0, len(mean.loc[:, percentil])),
                list(mean.loc[:, percentil]),
                yerr=list(SD.loc[:, percentil]),
                fmt='-o') 

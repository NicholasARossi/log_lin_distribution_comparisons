import pandas as pd
import matplotlib.pyplot as plt
import random
import matplotlib.cm as cm
import numpy.random as rnd
import numpy as np
# plt.style.use('rossidata')


if __name__ == "__main__":
    plt.close('all')
    fig, ax = plt.subplots(1, 2, figsize=(8, 3))
    # Random gaussian data.
    Ntotal = 7322
    n_bins = 30
    # data = np.random.randn(Ntotal)*10000

    data = np.random.gamma(2, 2, size=Ntotal) * 10000

    # data=np.random.uniform(10**1,10**6, size=10**7)
    # data=pd.read_csv('data2.csv')
    # data=data['pop'].values
    data += abs(min(data)) + 1
    data += 10
    # This is  the colormap I'd like to use.
    cm = plt.cm.get_cmap('RdYlBu_r')
    bins = np.linspace(min(data), max(data), n_bins)

    col = np.linspace(0, 1, n_bins)

    n, bins, patches = ax[0].hist(data, bins=bins)

    # scale values to interval [0,1]

    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c ** .4))

    ax[0].scatter(data[::10000],
                  -0.0000025 * np.ones(len(data[::10000])) + 0.0000005 * np.random.randn(len(data[::10000])),
                  facecolor='#00ccbc', s=3, alpha=0.25)

    bins = np.logspace(np.log10(min(data)), np.log10(max(data)), n_bins)

    n, bins, patches = ax[1].hist(data, bins=bins)
    col = np.linspace(0, 1, n_bins)
    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c ** 1.5))

    ax[1].set_xscale('log')

    ax[0].set_title('Linear Bins/ Linear Scale')
    ax[1].set_title('Log Bins/ Log Scale')
    ax[0].scatter(data, -100 * np.ones(len(data)) + 20 * np.random.randn(len(data)), s=3, alpha=0.25)

    # ax[1].scatter(data[::10000],-0.0000025*np.ones(len(data[::10000]))+0.0000005*np.random.randn(len(data[::10000])),s=3,alpha=0.25)


    # ax[1].scatter(data[::10000],-50*np.ones(len(data[::10000]))+10*np.random.randn(len(data[::10000])),s=3,alpha=0.25)
    ax[1].scatter(data, -100 * np.ones(len(data)) + 20 * np.random.randn(len(data)), facecolor='#00ccbc', s=3,
                  alpha=0.25)

    for l in range(2):
        ax[l].set_ylabel('Counts')
        ax[l].set_xlabel('Values')
        ax[l].set_ylim([-200, 1250])
    # ax[l].set_ylim([-10**5.5,10**6.35])
    fig.savefig('figures/test_hist.pdf', dpi=300)

    plt.close('all')
    fig, ax = plt.subplots(1, 2, figsize=(8, 3))
    # Random gaussian data.
    Ntotal = 1000000
    n_bins = 30
    # data = np.random.randn(Ntotal)*10000

    # data = np.random.gamma(2,2, size=10**7)*10000

    lower_lim = 10 ** 3
    upper_lim = 10 ** 7
    # bins=np.linspace(10**3,10**7,30)

    data = pd.read_csv('data.csv')

    A = data['pop'].values

    # This is  the colormap I'd like to use.
    cm = plt.cm.get_cmap('RdYlBu_r')
    bins = np.linspace(lower_lim, upper_lim, n_bins)

    col = np.linspace(0, 1, n_bins)

    n, bins, patches = ax[0].hist(A[~np.isnan(A)], bins=bins)
    results = A[~np.isnan(A)]
    # scale values to interval [0,1]

    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c))

    ax[0].scatter(results, -50 * np.ones(len(results)) + 10 * np.random.randn(len(results)), s=3, alpha=0.25)

    bins = np.logspace(np.log10(lower_lim), np.log10(upper_lim), n_bins)

    n, bins, patches = ax[1].hist(A[~np.isnan(A)], bins=bins)
    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c))
    ax[1].scatter(results, -50 * np.ones(len(results)) + 10 * np.random.randn(len(results)), s=3, alpha=0.25)

    ax[1].set_xscale('log')

    ax[0].set_title('Linear Bins/ Linear Scale')
    ax[1].set_title('Log Bins/ Log Scale')

    for l in range(2):
        ax[l].set_ylabel('Counts')
        ax[l].set_xlabel('Global City/ Town Sizes')
        ax[l].set_ylim([-100, 600])
    fig.savefig('figures/data_hist.pdf', dpi=300)


    # fig
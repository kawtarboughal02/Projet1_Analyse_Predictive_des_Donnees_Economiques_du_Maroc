import matplotlib.pyplot as plt
import seaborn as sns


def plot_time_series(df):
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    axes[0].plot(df.index, df['pib'], color='#1f77b4', marker='o')
    axes[0].set_title('Évolution du PIB du Maroc')
    axes[0].set_ylabel('PIB')
    axes[0].grid(True)

    axes[1].plot(df.index, df['inflation_pct'], color='#d62728', marker='o')
    axes[1].set_title('Évolution de l’inflation au Maroc')
    axes[1].set_ylabel('Inflation (%)')
    axes[1].grid(True)

    axes[2].plot(df.index, df['chomage_pct'], color='#2ca02c', marker='o')
    axes[2].set_title('Évolution du chômage au Maroc')
    axes[2].set_ylabel('Chômage (%)')
    axes[2].set_xlabel('Année')
    axes[2].grid(True)

    plt.tight_layout()
    return fig


def plot_correlation(correlation):
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Corrélation entre les indicateurs économiques')
    plt.tight_layout()
    return plt.gcf()

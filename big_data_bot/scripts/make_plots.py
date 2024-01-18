import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})


def make_single_plot(df, city, goods, marker):
    df = df[(df['subcategoryName'] == goods) & (df['city'] == city)]

    if marker == 'discount':
        figure = sns.lineplot(
            x="DT",
            y="avg_price_discount_new",
            data=df,
            label=f'{goods}'
        ).get_figure()

        rotation = 50
        for i, ax in enumerate(figure.axes):
            ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)

        plt.xlabel('Дата')
        plt.ylabel('Cредняя цена')
        plt.title(f'Средняя цена на {goods} в {city}')

        figure.savefig('data/outputs/single_plot.png')

    elif marker == 'regular':
        figure = sns.lineplot(
            x="DT",
            y="avg_price_regular_new",
            data=df,
            label=f'{goods}'
        ).get_figure()

        rotation = 50
        for i, ax in enumerate(figure.axes):
            ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)

        plt.xlabel('Дата')
        plt.ylabel('Cредняя цена')
        plt.title(f'Средняя цена на {goods} в {city}')

        figure.savefig('data/outputs/single_plot.png')


def make_multi_plot(df, goods, marker):

    df_mos = df[(df['subcategoryName'] == goods) & (df['city'] == 'Moscow')]
    df_kaz = df[(df['subcategoryName'] == goods) & (df['city'] == 'Kazan')]
    df_kras = df[(df['subcategoryName'] == goods) & (df['city'] == 'Krasnodar')]
    df_tum = df[(df['subcategoryName'] == goods) & (df['city'] == 'Tumen')]
    df_ekat = df[(df['subcategoryName'] == goods) & (df['city'] == 'Ekaterinburg')]
    df_piter = df[(df['subcategoryName'] == goods) & (df['city'] == 'St.Petersburg')]

    if marker == 'discount':
        fig, ax = plt.subplots(
            2, 3,
            figsize=(12, 6)
        )

        sns.lineplot(
            x="DT",
            y="avg_price_discount_new",
            data=df_mos,
            label='Moscow',
            ax=ax[0][0]
        )
        ax[0][0].tick_params(labelrotation=50)
        ax[0][0].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в Moscow')

        sns.lineplot(
            x="DT",
            y="avg_price_discount_new",
            data=df_kaz,
            label='Kazan',
            ax=ax[0][1]
        )
        ax[0][1].tick_params(labelrotation=50)
        ax[0][1].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в Kazan')

        sns.lineplot(
            x="DT",
            y="avg_price_discount_new",
            data=df_kras,
            label='Krasnodar',
            ax=ax[0][2]
        )
        ax[0][2].tick_params(labelrotation=50)
        ax[0][2].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в Krasnodar')

        sns.lineplot(
            x="DT",
            y="avg_price_discount_new",
            data=df_tum,
            label='Tumen',
            ax=ax[1][0]
        )
        ax[1][0].tick_params(labelrotation=50)
        ax[1][0].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в Tumen')

        sns.lineplot(
            x="DT",
            y="avg_price_discount_new",
            data=df_ekat,
            label='Ekaterinburg',
            ax=ax[1][1]
        )
        ax[1][1].tick_params(labelrotation=50)
        ax[1][1].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в Ekaterinburg')

        sns.lineplot(
            x="DT",
            y="avg_price_discount_new",
            data=df_piter,
            label='St.Petersburg',
            ax=ax[1][2]
        )
        ax[1][2].tick_params(labelrotation=50)
        ax[1][2].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в St.Petersburg')

        fig.savefig('data/outputs/multi_plot.png')

    elif marker == 'regular':
        fig, ax = plt.subplots(
            2, 3,
            figsize=(12, 6)
        )

        sns.lineplot(
            x="DT",
            y="avg_price_regular_new",
            data=df_mos,
            label='Moscow',
            ax=ax[0][0]
        )
        ax[0][0].tick_params(labelrotation=50)
        ax[0][0].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в Moscow')

        sns.lineplot(
            x="DT",
            y="avg_price_regular_new",
            data=df_kaz,
            label='Kazan',
            ax=ax[0][1]
        )
        ax[0][1].tick_params(labelrotation=50)
        ax[0][1].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в Kazan')

        sns.lineplot(
            x="DT",
            y="avg_price_regular_new",
            data=df_kras,
            label='Krasnodar',
            ax=ax[0][2]
        )
        ax[0][2].tick_params(labelrotation=50)
        ax[0][2].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в Krasnodar')

        sns.lineplot(
            x="DT",
            y="avg_price_regular_new",
            data=df_tum,
            label='Tumen',
            ax=ax[1][0]
        )
        ax[1][0].tick_params(labelrotation=50)
        ax[1][0].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в Tumen')

        sns.lineplot(
            x="DT",
            y="avg_price_regular_new",
            data=df_ekat,
            label='Ekaterinburg',
            ax=ax[1][1]
        )
        ax[1][1].tick_params(labelrotation=50)
        ax[1][1].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в Ekaterinburg')

        sns.lineplot(
            x="DT",
            y="avg_price_regular_new",
            data=df_piter,
            label='St.Petersburg',
            ax=ax[1][2]
        )
        ax[1][2].tick_params(labelrotation=50)
        ax[1][2].set(xlabel='Дата',
                     ylabel='Средняя цена',
                     title=f'Средняя цена в St.Petersburg')

        fig.savefig('data/outputs/multi_plot.png')

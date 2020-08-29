import pandas as pd
import data_clean as data
import scraper_toDB

pickle_name = 'top_posts.pkl'


def main():

    df = scraper_toDB.to_df()
    df['lemmatized_text'] = df['context'].apply(data.text_normalization)
    df.to_pickle('./pickled_df/%s' % pickle_name)


if __name__ == '__main__':
    main()

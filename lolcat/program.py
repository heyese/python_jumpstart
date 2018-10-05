import cats


def main():
    # Print header
    header('Cat Factory App')

    # Prep directory for cat pictures
    cat_dir = cats.prep_directory('pics')

    # Download cat pictures
    cats.download_pics(8, cat_dir)

    # Display cat pictures
    cats.display_pics(cat_dir)

def header(app_name):
    print('{0:-<{w}}\n{1:^{w}}\n{0:-<{w}}'.format('', app_name, w=2 * len(app_name)))


if __name__ == '__main__':
    main()

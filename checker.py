from glob import glob
from sys import argv

def main(main_file="articles.txt", codes_file="table_price_codes.txt", categorys_file="table_category_prices.txt"):
    """
    1
    It will compare photo's articles in the folder and in the list
    and print out missed names
    
    2
    Generate prices for the table by the category and codes map files
    """
    # get photos set
    articles_photo_list = map(lambda x: x[:7], glob('*.jpg'))
    photo_set = set(articles_photo_list)
   
    # get table set
    table_set = None
    articles_table_list = None
    with open(main_file, 'r') as main_f:
        articles_table_list = map(lambda x: x[:-1], main_f.readlines())
        table_set = set(articles_table_list)
    
    # compare sets and print out results
    missed_photo = sorted(table_set - photo_set)
    missed_table = sorted(photo_set - table_set)
    print 'Missed in photos:', missed_photo, len(photo_set)
    print 'Missed in table:', missed_table, len(table_set)
    # print 'Missed ALL:', table_set ^ photo_set
     
    # calculate prices   
    categorys = None
    codes = None
    
    with open(categorys_file, 'r') as f:
        categorys = dict(map(lambda x: tuple(x[:-1].split()), f.readlines()))
    
    # print categorys
    
    with open(codes_file, 'r') as f:
        codes = dict(map(lambda x: (x[:-1].split()[0], categorys.get(x[:-1].split()[1], '0')), f.readlines()))
        
    # print codes
    
    prices = map(lambda x: codes.get(x, '0'), articles_table_list)
    
    with open("checker_maped_prices.txt", 'w') as f:
        f.write('Prices:\n')
        for price in prices:
            f.write(price + '\n')
    
    with open("checker_codes_prices.txt", 'w') as f:
        f.write('Article, price:\n')
        for key in sorted(codes.keys()):
            f.write(key + '\t' + codes[key] + '\n')
    
    
    with open("checker_report.txt", 'w') as f:
        f.write('Missed in photos:\n')
        for article in missed_photo:
            f.write(article + '\n')
        f.write('\n')
        
        f.write('Missed in table:\n')
        for article in missed_table:
            f.write(article + '\n')
        f.write('\n')
        
        # f.write('All photo articles:\n')
        # for article in sorted(photo_set):
        #     f.write(article + '\n')
        # f.write('\n')
    
if __name__ == "__main__":
    main(*argv[1:])
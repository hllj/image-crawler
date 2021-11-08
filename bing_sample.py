from icrawler.builtin import BingImageCrawler
import imghdr
from glob import glob

import os
import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
                    description='Process crawl images from google'
                )
    parser.add_argument('--max_num', type=int,
                        help='Maximum number images crawl')
    parser.add_argument('--keyword', type=str, help='Keyword for searching',
                        required=True)
    parser.add_argument('--root_dir', type=str, help='Image folder to save',
                        default='download')
    args = parser.parse_args()
    if os.path.exists(args.root_dir) is False:
        os.makedirs(args.root_dir)
    bing_crawler = BingImageCrawler(
                        storage={'root_dir': args.root_dir},
                        feeder_threads=8,
                        parser_threads=8,
                        downloader_threads=16
                    )
    bing_crawler.crawl(
                            keyword=args.keyword, max_num=args.max_num,
                            file_idx_offset='auto'
                        )

    # change extension if need
    list_file = glob(f'{args.root_dir}/*')

    for file in list_file:
        old_ext = file.split('.')[1]
        name = file.split('.')[0]
        new_ext = imghdr.what(file)
        if old_ext != new_ext and new_ext is not None:
            new_file = f"{name}.{new_ext}"
            os.rename(file, new_file)
            print(f"Change file name! {new_file}")
        

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

    bing_crawler = BingImageCrawler(
                        storage={'root_dir': args.root_dir},
                        feeder_threads=8,
                        parser_threads=8,
                        downloader_threads=16
                    )
    bing_crawler.crawl(keyword=args.keyword, max_num=args.max_num)

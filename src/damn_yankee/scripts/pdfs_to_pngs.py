import argparse
import os
import sys
from damn_yankee.clean.pdf_to_png import PdfToPng
from damn_yankee.logger import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(
        description="Process data from a specified directory."
    )
    parser.add_argument(
        "--data-dir",
        required=True,
        help="Path to the data directory"
    )

    args = parser.parse_args()

    data_dir = args.data_dir

    if not os.path.isdir(data_dir):
        logger.error(f"Error: '{data_dir}' is not a valid directory.")
        sys.exit(1)

    logger.info(f"Data directory provided: {data_dir}")
    for _data_dir in os.listdir(data_dir):
        if _data_dir in {"2004-03-01-2004-06-30", "2004-08-13-2004-12-31"}:
            print("already processed, continuing...")
            continue
        
        full_dir = os.path.join(data_dir, _data_dir)
        if os.path.isdir(full_dir):
            PdfToPng(data_dir=full_dir, dry_run=False).write_images_from_pdf()

if __name__ == "__main__":
    main()

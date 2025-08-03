import os
from typing import List
from pdf2image import convert_from_path
from PIL import Image
from damn_yankee.logger import setup_logger
from dataclasses import dataclass

logger = setup_logger()

DPI = 300


class PdfToPng:
    def __init__(self, data_dir: str=None, dry_run: bool=False):
        self.dry_run = dry_run
        if data_dir is None:
            try:
                data_dir = os.environ['DATA_DIR']
            except KeyError:
                logger.error(f"DATA_DIR environment must be set to run {__file__}")
                raise

        logger.info(f"Setting data_dir to: {data_dir}")
        self.data_dir = data_dir
        self.img_data_dir = os.path.join(data_dir, "imgs")        
        logger.info(f"Setting img_data_dir to: {self.img_data_dir}")

        if not os.path.exists(self.img_data_dir):
            logger.info(f"{self.img_data_dir} does not exist, creating it")
            os.makedirs(self.img_data_dir)

    def pdf_to_images(self, pdf_file: str) -> List[Image.Image]:
        pdf_path = os.path.join(self.data_dir, pdf_file)
        logger.info(f"Starting PDF to PNG conversion for '{pdf_path}'")

        if not os.path.exists(pdf_path):
            logger.error(f"PDF file '{pdf_path}' does not exist.")

        try:
            if not self.dry_run:
                images = convert_from_path(pdf_path, dpi=DPI)
            else:
                images = []

            logger.info(f"Converted PDF into {len(images)} image(s)")
            return images
        except Exception as e:
            logger.exception(f"Failed to convert PDF: {e}")
    
    def write_images(self, images: List[Image.Image], pdf_file: str) -> None:
        for i, image in enumerate(images):
            file_name = pdf_file.replace(".pdf", "")
            page_num = i + 1
            output_path = os.path.join(self.img_data_dir, f"{file_name}_page_{page_num}.png")
            try:
                if not self.dry_run:
                    image.save(output_path, "PNG")
                logger.info(f"Saved page {page_num} to '{output_path}'")
            except Exception as e:
                logger.error(f"Failed to save page {page_num}: {e}")

    def write_images_from_pdf(self) -> None:
        for pdf_file in os.listdir(self.data_dir):
            if not pdf_file.endswith(".pdf"):
                continue
            
            images = self.pdf_to_images(pdf_file)
            self.write_images(images, pdf_file)
    
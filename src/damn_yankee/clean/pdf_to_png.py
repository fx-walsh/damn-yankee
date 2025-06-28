import os
import logging
from pdf2image import convert_from_path

DPI = 300

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("pdf_to_png.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

try:
    data_dir = os.environ['DATA_DIR']
except KeyError:
    logger.error(f"DATA_DIR environment must be set to run {__file__}")
    raise

logger.info(f"Reading input pdfs from {data_dir}")

clean_data_dir = os.path.join(data_dir, "clean")

logger.info(f"Writing png images to {clean_data_dir}")

if not os.path.exists(clean_data_dir):
    logger.info(f"{clean_data_dir} does not exist, creating it")
    os.makedirs(clean_data_dir)

for pdf_file in os.listdir(data_dir):
    pdf_path = os.path.join(data_dir, pdf_file)
    logger.info(f"Starting PDF to PNG conversion for '{pdf_path}'")

    if not os.path.exists(pdf_path):
        logger.error(f"PDF file '{pdf_path}' does not exist.")

    try:
        images = convert_from_path(pdf_path, dpi=DPI)
        logger.info(f"Converted PDF into {len(images)} image(s)")
    except Exception as e:
        logger.exception(f"Failed to convert PDF: {e}")

    output_paths = []
    for i, image in enumerate(images):
        page_num = i + 1
        output_path = os.path.join(clean_data_dir, f"{pdf_file}_page_{page_num}.png")
        try:
            image.save(output_path, "PNG")
            output_paths.append(output_path)
            logger.info(f"Saved page {page_num} to '{output_path}'")
        except Exception as e:
            logger.error(f"Failed to save page {page_num}: {e}")
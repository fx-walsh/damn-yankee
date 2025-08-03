import logging
import os
import time

def setup_logger():
    # Get the name of the calling script
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    log_filename = f"logs/{script_name}-{time.time()}.log"

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(script_name)

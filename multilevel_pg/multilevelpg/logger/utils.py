import datetime
# from malib.logger import logger
# from malib.logger import CsvOutput
# from malib.logger import StdOutput
# from malib.logger import TensorBoardOutput
# from malib.logger import TextOutput
from multilevel_pg.multilevelpg.logger import logger, CsvOutput, StdOutput, TensorBoardOutput, TextOutput

def set_logger(log_prefix):
    current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = "log/{}/{}/".format(log_prefix, current_time)
    text_log_file = "{}debug.log".format(log_dir)
    tabular_log_file = "{}progress.csv".format(log_dir)
    logger.add_output(TextOutput(text_log_file))
    logger.add_output(CsvOutput(tabular_log_file))
    logger.add_output(TensorBoardOutput(log_dir))
    logger.add_output(StdOutput())
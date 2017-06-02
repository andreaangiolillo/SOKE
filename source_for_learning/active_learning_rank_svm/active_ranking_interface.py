
class ActiveRankingInterface(object):

    def __init__(self, ra_model):
        """
        :param ra_model: RankSvmInterface
        :return:
        """
        self.ra_model = ra_model

    def get_rank_and_active(self, tr_data_x, tr_data_y, rank_data, max_to_rank = 10, max_best_scored=10):
        raise NotImplementedError("Should have implemented this")

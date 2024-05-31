from .rec_metric import RecMetric


class RecGTCMetric(object):

    def __init__(self,
                 main_indicator='acc',
                 is_filter=False,
                 ignore_space=True,
                 stream=False,
                 **kwargs):
        self.main_indicator = main_indicator
        self.is_filter = is_filter
        self.ignore_space = ignore_space
        self.eps = 1e-5
        self.gtc_metric = RecMetric(main_indicator=main_indicator,
                                    is_filter=is_filter,
                                    ignore_space=ignore_space,
                                    stream=stream)
        self.ctc_metric = RecMetric(main_indicator=main_indicator,
                                    is_filter=is_filter,
                                    ignore_space=ignore_space,
                                    stream=stream)

    def __call__(self, pred_label, *args, **kwargs):

        ctc_metric = self.ctc_metric(pred_label[1])
        gtc_metric = self.gtc_metric(pred_label[0])
        ctc_metric['gtc_acc'] = gtc_metric['acc']
        ctc_metric['gtc_norm_edit_dis'] = gtc_metric['norm_edit_dis']
        return ctc_metric

    def get_metric(self):
        """
        return metrics {
                 'acc': 0,
                 'norm_edit_dis': 0,
            }
        """
        ctc_metric = self.ctc_metric.get_metric()
        gtc_metric = self.gtc_metric.get_metric()
        ctc_metric['gtc_acc'] = gtc_metric['acc']
        ctc_metric['gtc_norm_edit_dis'] = gtc_metric['norm_edit_dis']
        return ctc_metric

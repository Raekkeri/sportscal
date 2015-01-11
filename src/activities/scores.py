BASE_SCORE = 1

class BaseScore(object):
    def get_score(self, activity):
        return BASE_SCORE


class SingleAttrBasedScore(BaseScore):
    """Abstract"""
    def get_score(self, activity):
        score = super(SingleAttrBasedScore, self).get_score(activity)
        _type = activity.type
        multiplier = float(getattr(_type, self.multpl_attr))
        return (score *
                multiplier *
                self.attr_to_unit(self.get_attr(activity)))

    def attr_to_unit(self, attr):
        return attr / float(self.reference_value)

    def get_attr(self, activity):
        return getattr(activity, self.attr)


class DistanceBasedScore(SingleAttrBasedScore):
    attr = 'distance'
    multpl_attr = 'distance_multiplier'
    reference_value = 1000 # 1 km


class DurationBasedScore(SingleAttrBasedScore):
    attr = 'duration'
    multpl_attr = 'duration_multiplier'
    reference_value = 600 # a 10 minutes

    def get_attr(self, activity):
        return activity.get_duration()


AVAILABLE_SCORES = dict((cls.__name__, cls()) for cls in [
    DistanceBasedScore, DurationBasedScore, BaseScore])

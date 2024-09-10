class CompetitionImageUrl:

    def __init__(self, competition_image_url: str):
        self.__competition_image_url = competition_image_url

    @property
    def value(self):
        return self.__competition_image_url

    @staticmethod
    def from_string(competition_image_url: str):
        return CompetitionImageUrl(competition_image_url)

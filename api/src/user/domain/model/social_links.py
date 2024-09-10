class SocialLinks:
    def __init__(self, email: str, x: str, instagram: str, other: str):
        self.__email: str = email
        self.__x: str = x
        self.__instagram: str = instagram
        self.__other: str = other

    @property
    def email(self):
        return self.__email

    @property
    def x(self):
        return self.__x

    @property
    def instagram(self):
        return self.__instagram

    @property
    def other(self):
        return self.__other

    def to_dict(self):
        return {
            "email": self.email,
            "x": self.x,
            "instagram": self.instagram,
            "other": self.other,
        }

    @staticmethod
    def from_dict(social_links: dict):
        return SocialLinks(
            social_links.get("email", ""),
            social_links.get("x", ""),
            social_links.get("instagram", ""),
            social_links.get("other", ""),
        )

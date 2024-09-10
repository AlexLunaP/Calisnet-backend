from faker import Faker

from ..social_links import SocialLinks

fake = Faker()


class TestSocialLinks:
    def test_constructor(self):
        email = fake.email()
        x = fake.url()
        instagram = fake.url()
        other = fake.url()

        social_links = SocialLinks(email, x, instagram, other)

        assert social_links.email == email
        assert social_links.x == x
        assert social_links.instagram == instagram
        assert social_links.other == other

    def test_to_dict(self):
        email = fake.email()
        x = fake.url()
        instagram = fake.url()
        other = fake.url()

        social_links = SocialLinks(email, x, instagram, other)

        data = social_links.to_dict()

        assert data["email"] == email
        assert data["x"] == x
        assert data["instagram"] == instagram
        assert data["other"] == other

    def test_from_dict(self):
        email = fake.email()
        x = fake.url()
        instagram = fake.url()
        other = fake.url()

        data = {
            "email": email,
            "x": x,
            "instagram": instagram,
            "other": other,
        }

        new_social_links = SocialLinks.from_dict(data)

        assert new_social_links.email == email
        assert new_social_links.x == x
        assert new_social_links.instagram == instagram
        assert new_social_links.other == other

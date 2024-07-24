from rest_framework import serializers
from main.app.models import UserProfile, ProfileFeedItem


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile
        fields = ["id", "email", "name", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"},
            },
        }

    def create(self, validated_data):
        """Create and return a new user"""

        user = UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    user_profile = serializers.StringRelatedField()

    class Meta:
        model = ProfileFeedItem
        fields = "__all__"
        extra_kwargs = {
            "user_profile": {
                "read_only": True,
            },
        }

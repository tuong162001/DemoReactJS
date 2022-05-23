from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Course, Lesson, Tag, Comment, User, Action, Rating,LessonView


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, course):
        request = self.context['request']
        name = course.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name

        return request.build_absolute_uri(path)

    class Meta:
        model = Course
        fields = ["id", "subject", "image", "created_date", "category"]


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class UserSerializer(ModelSerializer):
    avatar = SerializerMethodField()

    def get_avatar(self, user):
        request = self.context['request']
        name = user.avatar.name
        if user.avatar:
            if name.startswith("static/"):
                path = '/%s' % name
            else:
                path = '/static/%s' % name

            return request.build_absolute_uri(path)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "avatar",
                  "username", "password", "email", "date_joined"]
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }



class CommentSerializer(ModelSerializer):
    creator = SerializerMethodField()

    def get_creator(self, comment):
        return UserSerializer(comment.creator, context={"request": self.context.get('request')}).data


    class Meta:
        model = Comment
        fields = ["id", "content", "created_date", "update_date","creator"]

class LessonSerializer(ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, lesson):
        request = self.context['request']
        name = lesson.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name

        return request.build_absolute_uri(path)

    class Meta:
        model = Lesson
        fields = ["id", "subject", "image", "created_date", "update_date", "course"]

class LessonDetailSerializer(LessonSerializer):
    tags = TagSerializer(many=True)
    rate = SerializerMethodField()

    def get_rate(self, lesson):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            r = lesson.rating_set.filter(creator=request.user).first()
            if r:
                return r.rate

        return -1


    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ["content", "tags", "rate"]

class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "type",  "created_date"]

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rate",  "created_date"]

class LessonViewSerializer(ModelSerializer):
    class Meta:
        model = LessonView
        fields = ["id", "views", "lesson"]
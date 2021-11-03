from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'password', 'user_name')

    def create(self):
        if(User.objects.filter(user_id = self.validated_data['user_id']).count() == 0):
            new_user = User(user_id = self.validated_data['user_id'], 
                user_name = self.validated_data['user_name'], 
                password = self.validated_data['password'],
                status = False)
            new_user.save()
            return True
        else:
            return False




class PostSerializer(serializers.ModelSerializer):
    publisher = UserSerializer(read_only=True)
    # publisher = serializers.CharField(source='publisher.user_id')
    # exp_id = serializers.IntegerField(source='experien?ce.exp_id')

    class Meta:
        model = Post
        fields = ('post_id','publisher', 'title', 'content', 'published_time','exp_id')
    
    # def to_representation(self, instance):
    #     self.fields['publisher'] =  UserSerializer(read_only=True)
    #     return super(PostSerializer, self).to_representation(instance)

    # def create(self, validated_data):
    #     new_post = Post(
    #         publisher = self.validated_data['publisher'], 
    #         title = self.validated_data['title'],
    #         content = self.validated_data['content'],
    #         published_time = self.validated_data['published_time'],
    #         exp_id = self.validated_data['ex'],
    #     )
    #     new_post.save()
    #     return True
        

       


#!/usr/bin/env python
"""
Script to export existing data for deployment
This ensures all users, profiles, and posts are preserved
"""
import os
import sys
import django
import json

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Profile, Post, LikePost, FollowersCount

def export_data():
    print("Exporting existing data...")
    
    # Export users
    users_data = []
    for user in User.objects.all():
        users_data.append({
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'is_active': user.is_active,
            'date_joined': user.date_joined.isoformat(),
        })
    
    # Export profiles
    profiles_data = []
    for profile in Profile.objects.all():
        profiles_data.append({
            'user_username': profile.user.username,
            'id_user': profile.id_user,
            'bio': profile.bio,
            'location': profile.location,
            'profileimg': str(profile.profileimg),
        })
    
    # Export posts
    posts_data = []
    for post in Post.objects.all():
        posts_data.append({
            'id': str(post.id),
            'user': post.user,
            'image': str(post.image),
            'caption': post.caption,
            'created_at': post.created_at.isoformat(),
            'no_of_likes': post.no_of_likes,
        })
    
    # Export likes
    likes_data = []
    for like in LikePost.objects.all():
        likes_data.append({
            'post_id': like.post_id,
            'username': like.username,
        })
    
    # Export followers
    followers_data = []
    for follower in FollowersCount.objects.all():
        followers_data.append({
            'follower': follower.follower,
            'user': follower.user,
        })
    
    # Save to JSON file
    data = {
        'users': users_data,
        'profiles': profiles_data,
        'posts': posts_data,
        'likes': likes_data,
        'followers': followers_data,
    }
    
    with open('exported_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Exported {len(users_data)} users")
    print(f"✅ Exported {len(profiles_data)} profiles")
    print(f"✅ Exported {len(posts_data)} posts")
    print(f"✅ Exported {len(likes_data)} likes")
    print(f"✅ Exported {len(followers_data)} followers")
    print("📁 Data saved to exported_data.json")

if __name__ == '__main__':
    export_data()

import pandas as pd
import numpy as np
import requests
import json
import pandas as pd
import numpy as np
import praw
import datetime as dt
import requests


#import both and drop unneeded cols
reals = pd.read_csv('./data/real_posts.csv')
reals.drop(['Unnamed: 0', 'approved_at_utc', 'approved_by', 'archived', 'author',
       'author_flair_background_color',
       'author_flair_css_class', 'author_flair_richtext',
       'author_flair_template_id', 'author_flair_text',
       'author_flair_text_color', 'author_flair_type', 'author_fullname',
       'banned_at_utc', 'banned_by', 'can_gild', 'can_mod_post', 'category',
       'clicked', 'content_categories', 'contest_mode', 'created',
       'created_utc', 'distinguished', 'domain', 'downs', 'edited', 'gilded',
       'hidden', 'hide_score', 'id', 'is_crosspostable', 'is_meta',
       'is_original_content', 'is_reddit_media_domain', 'is_self', 'is_video',
       'likes', 'link_flair_background_color', 'link_flair_css_class',
       'link_flair_richtext', 'link_flair_template_id', 'link_flair_text',
       'link_flair_text_color', 'link_flair_type', 'locked', 'media',
       'media_embed', 'media_only', 'mod_note', 'mod_reason_by',
       'mod_reason_title', 'mod_reports', 'name', 'no_follow', 'num_comments',
       'num_crossposts', 'num_reports', 'over_18', 'parent_whitelist_status',
       'permalink', 'pinned', 'pwls', 'quarantine', 'removal_reason',
       'report_reasons', 'saved', 'score', 'secure_media',
       'secure_media_embed', 'selftext', 'selftext_html', 'send_replies',
       'spoiler', 'stickied', 'subreddit_id',
       'subreddit_name_prefixed', 'subreddit_subscribers', 'subreddit_type',
       'suggested_sort', 'thumbnail', 'ups', 'url', 'user_reports',
       'view_count', 'visited', 'whitelist_status', 'wls'],
          inplace = True, axis = 1)

reals.drop_duplicates(inplace = True)

fakes = pd.read_csv('./data/fake_posts.csv')
fakes.drop(['thumbnail_height', 'thumbnail_width', 'ups', 'url',
            'user_reports', 'view_count', 'visited', 'whitelist_status', 'wls',
            'Unnamed: 0', 'approved_at_utc', 'approved_by', 'archived', 'author',
            'author_flair_background_color', 'author_flair_css_class',
            'author_flair_richtext', 'author_flair_template_id',
            'author_flair_text', 'author_flair_text_color', 'author_flair_type', 'author_fullname',
            'banned_at_utc', 'banned_by', 'body_html', 'can_gild',
            'can_mod_post', 'category', 'clicked', 'collapsed', 'collapsed_reason',
            'content_categories', 'contest_mode', 'controversiality', 'created',
            'created_utc', 'distinguished', 'domain', 'downs', 'edited', 'gilded',
            'hidden', 'hide_score', 'id', 'is_crosspostable', 'is_meta',
            'is_original_content', 'is_reddit_media_domain', 'is_self',
            'is_submitter', 'is_video', 'likes', 'link_author',
            'link_flair_background_color', 'link_flair_css_class',
            'link_flair_richtext', 'link_flair_template_id', 'link_flair_text',
            'link_flair_text_color', 'link_flair_type', 'link_id', 'link_permalink',
            'link_title', 'link_url', 'locked', 'media', 'media_embed',
            'media_only', 'mod_note', 'mod_reason_by', 'mod_reason_title',
            'mod_reports', 'name', 'no_follow', 'num_comments', 'num_crossposts',
            'num_reports', 'over_18', 'parent_id', 'parent_whitelist_status',
            'permalink', 'pinned', 'pwls', 'quarantine',
            'removal_reason', 'replies', 'report_reasons', 'saved', 'score',
            'score_hidden', 'secure_media', 'secure_media_embed', 'selftext',
            'selftext_html', 'send_replies', 'spoiler', 'stickied',
            'subreddit_id', 'subreddit_name_prefixed', 'subreddit_subscribers',
            'subreddit_type', 'suggested_sort', 'thumbnail'],
             axis = 1, inplace = True)


# fill nulls, combine cols
# no nulls in reals

fakes.fillna("", inplace = True)
# Combine title and body text to get full sample
fakes['text'] = fakes['body'] + fakes['title']
fakes.drop(['body', 'title'], inplace = True, axis =1)
fakes.drop_duplicates(inplace = True)

#report numbers
print("Dim of real posts:", reals.shape)
print("Dim of fake posts:", fakes.shape)

data = pd.concat([reals,fakes], axis = 0, sort = True)
data.drop(['author_cakeday', 'post_hint', 'preview', 'previous_visits'],
            inplace = True, axis =1)
data.fillna("", inplace = True)
data['data'] = data['text'] + data['title']
data.drop(['text', 'title'], inplace = True, axis =1)
print(data.shape)

data.to_csv('./data/data_cleaned.csv')

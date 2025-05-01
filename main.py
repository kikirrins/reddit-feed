import os
import praw
from reddit import search_ticker_mentions

# Init reddit
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),#my client id
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),  #your client secret
    user_agent=os.getenv('REDDIT_USER_AGENT'))     # your reddit password

# Search for posts containing ticker
q = 'title:$NVDA'

# Search for ticker mentions
posts = search_ticker_mentions(reddit, q)
print("Posts found: ", len(posts))

sorted_posts = sorted(posts, key=lambda x: x['score'], reverse=True)

# Print results
for post in sorted_posts[:3]:  # Show top 3 posts
    print(f"\nSubreddit: r/{post['subreddit']}")
    print(f"Title: {post['title']}")
    print(f"Content: {post['content'][:200]}..." if len(post['content']) > 200 else f"Content: {post['content']}")
    print(f"Score: {post['score']}")
    print(f"Comments: {post['num_comments']}")
    print(f"URL: {post['url']}")
    print(f"Posted: {post['created_utc']}")
    
    # Print comments
    if post['comments']:
        print("\nTop comments:")
        for i, comment in enumerate(post['comments'][:3], 1):  # Show top 3 comments
            print(f"  {i}. {comment['author']} ({comment['score']} points):")
            print(f"     {comment['body'][:100]}..." if len(comment['body']) > 100 else f"     {comment['body']}")
    
    print("-" * 80)


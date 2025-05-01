from datetime import datetime, timedelta

def search_ticker_mentions(
    reddit,
    search_query,
    subreddits=['wallstreetbets', 'stocks', 'investing'],
    time_filter='week',
    limit=100
):
    """
    Search for ticker mentions across specified subreddits

    Args:
        reddit: Reddit API instance
        subreddits: List of subreddit names to search
        time_filter: Time filter for search (hour, day, week, month, year, all)
        limit: Maximum number of posts to retrieve per subreddit
    """
    ticker_posts = []

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        try:
            search_results = subreddit.search(
                search_query,
                time_filter=time_filter,
                limit=limit
            )
            for submission in search_results:
                # Get post content directly
                content = submission.selftext
                
                # Get comments
                comments_data = []
                try:
                    submission.comment_sort = 'top'
                    submission.comments.replace_more(limit=0)
                    
                    for comment in list(submission.comments)[:10]:  # Limit to 10 comments
                        comment_data = {
                            'id': comment.id,
                            'author': str(comment.author) if comment.author else '[deleted]',
                            'body': comment.body,
                            'score': comment.score,
                            'created_utc': datetime.fromtimestamp(comment.created_utc),
                            'is_submitter': comment.is_submitter
                        }
                        comments_data.append(comment_data)
                except Exception as e:
                    print(f"Error fetching comments for {submission.id}: {str(e)}")
                
                post_data = {
                    'title': submission.title,
                    'subreddit': subreddit_name,
                    'url': f'https://reddit.com{submission.permalink}',
                    'score': submission.score,
                    'created_utc': datetime.fromtimestamp(submission.created_utc),
                    'author': str(submission.author),
                    'num_comments': submission.num_comments,
                    'content': content,
                    'comments': comments_data
                }
                ticker_posts.append(post_data)

        except Exception as e:
            print(f"Error searching {subreddit_name}: {str(e)}")
            continue

    return ticker_posts

def get_post_comments(reddit, submission_id, limit=None, sort='top'):
    """
    Retrieves all comments from a Reddit post.

    Args:
        reddit: Reddit API instance
        submission_id: The ID of the submission (post) to fetch comments from
        limit: Maximum number of top-level comments to fetch (None for all)
        sort: Sort order for comments ('top', 'new', 'controversial', 'old', 'qa')

    Returns:
        A list of dictionaries containing comment data
    """
    try:
        submission = reddit.submission(id=submission_id)
        submission.comment_sort = sort
        submission.comments.replace_more(limit=0)  # Replace MoreComments objects to get all comments
        
        comments_data = []
        
        for comment in submission.comments.list():
            comment_data = {
                'id': comment.id,
                'author': str(comment.author) if comment.author else '[deleted]',
                'body': comment.body,
                'score': comment.score,
                'created_utc': datetime.fromtimestamp(comment.created_utc),
                'is_submitter': comment.is_submitter,
                'parent_id': comment.parent_id
            }
            comments_data.append(comment_data)
            
            # Limit top-level comments if specified
            if limit and len(comments_data) >= limit:
                break
                
        return comments_data
        
    except Exception as e:
        print(f"Error fetching comments for post {submission_id}: {str(e)}")
        return []
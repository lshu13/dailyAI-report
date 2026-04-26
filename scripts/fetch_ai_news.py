import requests
import json
from datetime import datetime

def fetch_ai_news():
    """
    Fetch top 3 most important AI development news from a public API.
    Uses NewsAPI.org (free tier) - you'll need to add your API key to GitHub Secrets.
    """
    
    # For production, use: API_KEY from environment variable
    # api_key = os.environ.get('NEWS_API_KEY')
    
    # Alternative: Use Hacker News API (no auth required)
    try:
        # Fetch top stories from Hacker News
        response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
        top_story_ids = response.json()[:30]  # Get top 30, we'll filter for AI
        
        ai_news = []
        keywords = ['ai', 'artificial intelligence', 'machine learning', 'llm', 'neural', 'gpt', 'transformer']
        
        for story_id in top_story_ids:
            story_url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
            story = requests.get(story_url).json()
            
            title = story.get('title', '').lower()
            
            # Check if story is AI-related
            if any(keyword in title for keyword in keywords):
                ai_news.append({
                    'title': story.get('title'),
                    'url': story.get('url'),
                    'score': story.get('score', 0),
                    'time': story.get('time'),
                    'source': 'Hacker News'
                })
            
            if len(ai_news) >= 3:
                break
        
        return sorted(ai_news, key=lambda x: x['score'], reverse=True)[:3]
    
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

def generate_email_html(news_items):
    """Generate HTML email body from news items"""
    
    html = """
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; color: #333; }
            .container { max-width: 600px; margin: 0 auto; padding: 20px; }
            .header { background-color: #0066cc; color: white; padding: 20px; border-radius: 5px; }
            .news-item { margin: 20px 0; padding: 15px; border-left: 4px solid #0066cc; background-color: #f9f9f9; }
            .news-title { font-size: 18px; font-weight: bold; margin-bottom: 10px; }
            .news-link { color: #0066cc; text-decoration: none; }
            .news-link:hover { text-decoration: underline; }
            .footer { margin-top: 30px; font-size: 12px; color: #999; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Daily AI Development News</h1>
                <p>Top 3 Most Important Stories - """ + datetime.now().strftime("%B %d, %Y") + """</p>
            </div>
    """
    
    for i, item in enumerate(news_items, 1):
        html += f"""
            <div class="news-item">
                <div class="news-title">#{i} - {item['title']}</div>
                <p><strong>Source:</strong> {item.get('source', 'Unknown')}</p>
                <p><strong>Relevance Score:</strong> {item.get('score', 0)}</p>
                <p><a href="{item.get('url', '#')}" class="news-link" target="_blank">Read More →</a></p>
            </div>
        """
    
    html += """
            <div class="footer">
                <p>This is an automated daily report. Customize your preferences in the GitHub repository settings.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html

if __name__ == '__main__':
    news_items = fetch_ai_news()
    
    if news_items:
        email_html = generate_email_html(news_items)
        with open('email_body.html', 'w') as f:
            f.write(email_html)
        print(f"Successfully fetched {len(news_items)} AI news items")
        print(json.dumps(news_items, indent=2))
    else:
        print("No AI news found")

# Setup Guide: Physical AI Textbook Backend

## Prerequisites

- Python 3.11+
- Git

## 1. Neon Postgres Setup

1. Go to [neon.tech](https://neon.tech) and create account
2. Create new project
3. Copy connection string:
   ```
   postgresql://user:password@ep-xxx.region.aws.neon.tech/neondb?sslmode=require
   ```

## 2. Qdrant Cloud Setup

1. Go to [cloud.qdrant.io](https://cloud.qdrant.io) and create account
2. Create new cluster (Free tier available)
3. Copy:
   - Cluster URL: `https://xxx.aws.cloud.qdrant.io:6333`
   - API Key (from API Keys tab)

## 3. OpenAI API Setup

1. Go to [platform.openai.com](https://platform.openai.com)
2. Create API key
3. Copy key (starts with `sk-`)

## 4. Environment Configuration

```bash
cd backend
cp .env.example .env
```

Edit `.env`:
```env
DATABASE_URL=postgresql://user:password@ep-xxx.region.aws.neon.tech/neondb?sslmode=require
QDRANT_HOST=https://xxx.aws.cloud.qdrant.io:6333
QDRANT_API_KEY=your_qdrant_api_key
OPENAI_API_KEY=sk-your_openai_key
BETTER_AUTH_SECRET=your_random_secret
BETTER_AUTH_URL=http://localhost:8000
```

## 5. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

## 6. Initialize Services

```bash
# Setup Qdrant collection
python -m scripts.setup_qdrant --verify

# Index textbook content
python -m scripts.index_content
```

## 7. Start Server

```bash
python run.py
```

Server runs at `http://localhost:8000`

## 8. Verification

### Test Health
```bash
curl http://localhost:8000/health
```

### Test Chatbot
```bash
curl -X POST http://localhost:8000/api/chatbot/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is physical AI?"}'
```

### API Docs
- Swagger: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Common Issues

**Qdrant connection failed:**
- Check URL includes `https://` and port `:6333`
- Verify API key is correct

**Database error:**
- Check connection string format
- Ensure `?sslmode=require` at end

**OpenAI rate limit:**
- Check usage at platform.openai.com
- Reduce batch size: `--batch-size 25`

## Cost Estimates

**Free Tier:**
- Neon: Free (0.5 GB)
- Qdrant: Free (1 GB)
- OpenAI: ~$0.50-2.00/day

**Production:**
- Neon: ~$19/month
- Qdrant: ~$25/month
- OpenAI: ~$20-50/month

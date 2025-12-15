# Better-Auth Patterns

## Overview

This skill provides patterns and best practices for integrating Better-Auth (better-auth.com) into the Physical AI & Humanoid Robotics Textbook project for authentication and authorization.

## What is Better-Auth?

Better-Auth is a modern, self-hosted authentication framework that provides:
- Email/Password authentication
- Social logins (Google, GitHub, etc.)
- Session management
- JWT tokens
- Rate limiting
- Two-factor authentication (2FA)
- Magic link authentication

## Installation & Setup

### Backend (FastAPI)

```bash
# Install better-auth Python client
pip install better-auth-python
```

```python
# backend/app/auth.py
from better_auth import BetterAuth
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Initialize Better-Auth
auth = BetterAuth(
    secret=os.getenv("BETTER_AUTH_SECRET"),
    database_url=os.getenv("DATABASE_URL"),
    api_url=os.getenv("BETTER_AUTH_API_URL", "http://localhost:3001")
)

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Dependency to get current authenticated user"""
    try:
        token = credentials.credentials
        user = await auth.verify_token(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
```

### Frontend (React/Docusaurus)

```bash
# Install better-auth client
npm install @better-auth/react
```

```tsx
// frontend/src/auth/AuthProvider.tsx
import { BetterAuthProvider, useBetterAuth } from '@better-auth/react';

export function AuthProvider({ children }) {
  return (
    <BetterAuthProvider
      apiUrl={process.env.REACT_APP_BETTER_AUTH_URL}
      onSessionChange={(session) => {
        console.log('Session changed:', session);
      }}
    >
      {children}
    </BetterAuthProvider>
  );
}
```

## Authentication Patterns

### Pattern 1: Email/Password Signup

```python
#backend/app/routes/auth.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    name: str

@router.post("/signup")
async def signup(data: SignupRequest):
    """Register new user"""
    try:
        user = await auth.signup(
            email=data.email,
            password=data.password,
            name=data.name
        )
        return {
            "user": user,
            "message": "Signup successful. Please check your email for verification."
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

```tsx
// Frontend component
import { useBetterAuth } from '@better-auth/react';

export function SignupForm() {
  const { signup } = useBetterAuth();
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    
    try {
      await signup({
        email: formData.get('email'),
        password: formData.get('password'),
        name: formData.get('name')
      });
      // Redirect to verification page
    } catch (error) {
      console.error('Signup failed:', error);
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input name="name" type="text" placeholder="Full Name" required />
      <input name="email" type="email" placeholder="Email" required />
      <input name="password" type="password" placeholder="Password" required />
      <button type="submit">Sign Up</button>
    </form>
  );
}
```

### Pattern 2: Email/Password Login

```python
# backend/app/routes/auth.py
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/login")
async def login(data: LoginRequest):
    """Authenticate user"""
    try:
        session = await auth.login(
            email=data.email,
            password=data.password
        )
        return {
            "token": session.token,
            "user": session.user,
            "expiresAt": session.expires_at
        }
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
```

```tsx
// Frontend component
export function LoginForm() {
  const { login } = useBetterAuth();
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    
    try {
      const session = await login({
        email: formData.get('email'),
        password: formData.get('password')
      });
      // Store token and redirect
      localStorage.setItem('auth_token', session.token);
      window.location.href = '/dashboard';
    } catch (error) {
      console.error('Login failed:', error);
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input name="email" type="email" placeholder="Email" required />
      <input name="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  );
}
```

### Pattern 3: Social Login (Google)

```python
# backend/app/routes/auth.py
@router.get("/oauth/google")
async def google_oauth():
    """Initialize Google OAuth flow"""
    auth_url = await auth.get_oauth_url(
        provider="google",
        redirect_uri=os.getenv("GOOGLE_REDIRECT_URI")
    )
    return {"url": auth_url}

@router.get("/oauth/google/callback")
async def google_callback(code: str):
    """Handle Google OAuth callback"""
    try:
        session = await auth.oauth_callback(
            provider="google",
            code=code
        )
        return session
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

```tsx
// Frontend component
export function GoogleLoginButton() {
  const handleGoogleLogin = async () => {
    const response = await fetch('/api/auth/oauth/google');
    const { url } = await response.json();
    window.location.href = url;
  };
  
  return (
    <button onClick={handleGoogleLogin} className="btn-google">
      <GoogleIcon /> Continue with Google
    </button>
  );
}
```

## Session Management

### Verify Session Middleware

```python
# backend/app/middleware/auth.py
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Skip auth for public routes
        if request.url.path in ["/api/auth/login", "/api/auth/signup"]:
            return await call_next(request)
        
        # Get token from header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing auth token")
        
        token = auth_header.split(" ")[1]
        
        try:
            user = await auth.verify_token(token)
            request.state.user = user
            return await call_next(request)
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid token")
```

### Frontend Session Hook

```tsx
// frontend/src/hooks/useSession.ts
import { useBetterAuth } from '@better-auth/react';

export function useSession() {
  const { session, loading, error } = useBetterAuth();
  
  return {
    user: session?.user,
    isAuthenticated: !!session,
    isLoading: loading,
    error
  };
}

// Usage in component
export function ProtectedComponent() {
  const { user, isAuthenticated, isLoading } = useSession();
  
  if (isLoading) return <div>Loading...</div>;
  if (!isAuthenticated) return <div>Please login</div>;
  
  return <div>Welcome, {user.name}!</div>;
}
```

## Route Protection

### Backend Protected Routes

```python
# backend/app/routes/protected.py
from fastapi import APIRouter, Depends
from app.auth import get_current_user

router = APIRouter(prefix="/api/user", tags=["User"])

@router.get("/profile")
async def get_profile(user = Depends(get_current_user)):
    """Get current user profile"""
    return user

@router.patch("/profile")
async def update_profile(
    data: dict,
    user = Depends(get_current_user)
):
    """Update user profile"""
    # Update logic here
    return {"message": "Profile updated"}
```

### Frontend Route Protection

```tsx
// frontend/src/components/ProtectedRoute.tsx
import { Navigate } from 'react-router-dom';
import { useSession } from '../hooks/useSession';

export function ProtectedRoute({ children }) {
  const { isAuthenticated, isLoading } = useSession();
  
  if (isLoading) {
    return <div className="loading">Verifying session...</div>;
  }
  
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }
  
  return children;
}

// Usage in routing
<Route 
  path="/dashboard" 
  element={
    <ProtectedRoute>
      <Dashboard />
    </ProtectedRoute>
  } 
/>
```

## Personalization Integration

### User Preferences Storage

```python
# backend/app/models/user_profile.py
from sqlalchemy import Column, String, Integer, JSON, ForeignKey
from app.database import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), unique=True)
    background = Column(String)  # "beginner", "intermediate", "advanced"
    interests = Column(JSON)  # List of topics
    preferences = Column(JSON)  # UI preferences, etc.
```

```python
# backend/app/routes/personalization.py
@router.post("/personalize")
async def update_personalization(
    data: dict,
    user = Depends(get_current_user)
):
    """Update user personalization settings"""
    profile = await UserProfile.get_or_create(user_id=user.id)
    profile.background = data.get("background")
    profile.interests = data.get("interests")
    await profile.save()
    return {"message": "Preferences saved"}
```

### Frontend Personalization

```tsx
// frontend/src/contexts/PersonalizationContext.tsx
export function PersonalizationProvider({ children }) {
  const { user } = useSession();
  const [preferences, setPreferences] = useState(null);
  
  useEffect(() => {
    if (user) {
      fetchPreferences();
    }
  }, [user]);
  
  const fetchPreferences = async () => {
    const response = await fetch('/api/user/preferences', {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
      }
    });
    const data = await response.json();
    setPreferences(data);
  };
  
  return (
    <PersonalizationContext.Provider value={{ preferences, setPreferences }}>
      {children}
    </PersonalizationContext.Provider>
  );
}
```

## Best Practices

### Security

1. **Use Environment Variables** - Never hardcode secrets
2. **HTTPS Only** - Enforce SSL in production
3. **Rate Limiting** - Prevent brute force attacks
4. **Password Strength** - Enforce strong password requirements
5. **Token Expiration** - Set reasonable expiration times
6. **Refresh Tokens** - Implement token refreshing

### Error Handling

```python
# Consistent error responses
class AuthError(Exception):
    def __init__(self, message: str, code: str):
        self.message = message
        self.code = code

@app.exception_handler(AuthError)
async def auth_error_handler(request, exc):
    return JSONResponse(
        status_code=401,
        content={
            "error": exc.code,
            "message": exc.message
        }
    )
```

### Session Storage

```typescript
// Store sessions securely
class SessionStorage {
  private static TOKEN_KEY = 'auth_token';
  
  static setToken(token: string) {
    // Use httpOnly cookies in production
    localStorage.setItem(this.TOKEN_KEY, token);
  }
  
  static getToken(): string | null {
    return localStorage.getItem(this.TOKEN_KEY);
  }
  
  static clearToken() {
    localStorage.removeItem(this.TOKEN_KEY);
  }
}
```

## Environment Variables

```bash
# backend/.env
BETTER_AUTH_SECRET=your-secret-key-here
BETTER_AUTH_API_URL=http://localhost:3001
DATABASE_URL=postgresql://user:pass@localhost/db
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8000/api/auth/oauth/google/callback
```

```bash
# frontend/.env
REACT_APP_BETTER_AUTH_URL=http://localhost:8000/api/auth
REACT_APP_API_URL=http://localhost:8000
```

## Testing Authentication

```python
# backend/tests/test_auth.py
import pytest
from fastapi.testclient import TestClient

def test_signup(client: TestClient):
    response = client.post("/api/auth/signup", json={
        "email": "test@example.com",
        "password": "SecurePass123!",
        "name": "Test User"
    })
    assert response.status_code == 200
    assert "user" in response.json()

def test_login(client: TestClient):
    response = client.post("/api/auth/login", json={
        "email": "test@example.com",
        "password": "SecurePass123!"
    })
    assert response.status_code == 200
    assert "token" in response.json()
```

---

**Version:** 1.0  
**Last Updated:** 2025-12-12  
**Compatibility:** Better-Auth v2.x, FastAPI, React

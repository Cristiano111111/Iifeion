import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useLocation, Navigate, useNavigate } from 'react-router-dom';
import { 
  Home, 
  DollarSign, 
  Activity, 
  Droplets, 
  Moon, 
  Calendar,
  Target,
  Settings as SettingsIcon,
  TrendingUp,
  Clock,
  StickyNote,
  Heart,
  Trophy,
  Sparkles,
  Pencil,
  Check,
  X
} from 'lucide-react';
import Dashboard from './components/Dashboard';
import Budget from './components/Budget';
import Fitness from './components/Fitness';
import WaterTracker from './components/WaterTracker';
import SleepTracker from './components/SleepTracker';
import Goals from './components/Goals';
import Habits from './components/Habits';
import Settings from './components/Settings';
import Login from './components/Login';
import Pomodoro from './components/Pomodoro';
import QuickNotes from './components/QuickNotes';
import MoodTracker from './components/MoodTracker';
import Achievements from './components/Achievements';
import Tasks from './components/tasks';
import './App.css';
import { getXPData } from './components/xpUtils';

// Add Google Fonts import for Orbitron at the top of the file (injected into the document head)
if (!document.getElementById('orbitron-font')) {
  const link = document.createElement('link');
  link.id = 'orbitron-font';
  link.rel = 'stylesheet';
  link.href = 'https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap';
  document.head.appendChild(link);
}

function Navigation({ onLogout, user }) {
  const location = useLocation();
  const profilePic = user && user.profilePic ? user.profilePic : '';
  // XP bar logic
  const { xp, level } = getXPData(user);
  console.log('NAV DEBUG user:', user, 'xp:', xp, 'level:', level);
  const maxLevel = 20;
  const xpPerLevel = 100;
  const xpProgress = Math.min(100, (xp / xpPerLevel) * 100);
  const navItems = [
    { profilePic: true },
    { path: '/', icon: Home, label: 'Dashboard' },
    { path: '/budget', icon: DollarSign, label: 'Budget' },
    { path: '/fitness', icon: Activity, label: 'Fitness' },
    { path: '/water', icon: Droplets, label: 'Water' },
    { path: '/sleep', icon: Moon, label: 'Sleep' },
    { path: '/goals', icon: Target, label: 'Goals' },
    { path: '/habits', icon: TrendingUp, label: 'Habits' },
    { path: '/pomodoro', icon: Clock, label: 'Work Timer' },
    { path: '/notes', icon: StickyNote, label: 'Notes' },
    { path: '/mood', icon: Heart, label: 'Mood' },
    { path: '/achievements', icon: Trophy, label: 'Achievements' },
  ];
  // Remove app name editing state and logic
  return (
    <nav className="navigation">
      <div className="nav-header" style={{ textAlign: 'left', paddingLeft: '16px' }}>
        <h2 style={{
          margin: 0,
          fontWeight: 700,
          fontSize: 28,
          letterSpacing: '0.08em',
          fontFamily: 'Orbitron, Montserrat, Poppins, Arial, sans-serif',
          background: 'linear-gradient(90deg, #4FC3F7 0%, #1976D2 100%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          textShadow: '0 2px 16px #23272f',
          textTransform: 'uppercase',
        }}>lifeion</h2>
      </div>
      {/* XP bar always at the top */}
      <div className="xp-bar-nav" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', margin: '18px 0 18px 0', minHeight: 110 }}>
        <img
          src={profilePic || 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" viewBox="0 0 56 56"><circle cx="28" cy="28" r="28" fill="%23e0e7ef"/><circle cx="28" cy="22" r="10" fill="%23bfc7d5"/><ellipse cx="28" cy="44" rx="16" ry="8" fill="%23bfc7d5"/></svg>'}
          alt="Profile"
          style={{
            width: 56,
            height: 56,
            borderRadius: '50%',
            objectFit: 'cover',
            border: '2px solid #ccc',
            marginBottom: 8,
          }}
        />
        <div
          className="xp-level-box"
          style={{
            width: '100%',
            textAlign: 'center',
            marginTop: profilePic ? 2 : 0,
            marginBottom: profilePic ? 0 : 12,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <div
            className="xp-level-label"
            style={{
              fontWeight: 700,
              fontSize: 13,
              color: '#ffd93d',
              letterSpacing: '0.04em',
              marginBottom: 2,
            }}
          >
            Level {level} / {maxLevel}
          </div>
          <div
            className="xp-bar-bg"
            style={{
              width: '80%',
              height: 8,
              background: 'rgba(102,126,234,0.13)',
              borderRadius: 8,
              margin: '0 auto',
              position: 'relative',
              overflow: 'hidden',
            }}
          >
            <div
              className="xp-bar-fill"
              style={{
                width: `${xpProgress}%`,
                height: '100%',
                background: 'linear-gradient(90deg, #ffd93d 0%, #667eea 100%)',
                borderRadius: 8,
                transition: 'width 0.5s cubic-bezier(0.4,0,0.2,1)',
              }}
            ></div>
          </div>
          <div
            className="xp-label"
            style={{ fontSize: 11, color: '#bfc7d5', marginTop: 2 }}
          >
            {level < maxLevel ? `${xp} / ${xpPerLevel} XP` : 'MAX LEVEL'}
          </div>
        </div>
      </div>
      <div className="nav-items">
        {navItems.filter(item => !item.profilePic).map((item, idx) => {
          const Icon = item.icon;
          const isActive = location.pathname === item.path;
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`nav-item ${isActive ? 'active' : ''}`}
            >
              <Icon size={20} />
              <span>{item.label}</span>
            </Link>
          );
        })}
      </div>
    </nav>
  );
}

function TopRightSettings() {
  const navigate = useNavigate();
  return (
    <button
      className="settings-btn settings-bubble"
      style={{ 
        position: 'absolute', 
        top: 20, 
        right: 24, 
        background: 'rgba(255, 255, 255, 0.1)', 
        border: '1px solid rgba(255, 255, 255, 0.2)', 
        borderRadius: '50%',
        width: '48px',
        height: '48px',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        backdropFilter: 'blur(10px)',
        boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
        transition: 'all 0.3s ease'
      }}
      onClick={() => navigate('/settings')}
      title="Settings"
    >
      <SettingsIcon size={24} />
    </button>
  );
}

function App() {
  const currentUser = localStorage.getItem('currentUser') || '';
  const userKey = currentUser ? `user_${currentUser}` : '';
  const userData = userKey ? JSON.parse(localStorage.getItem(userKey) || '{}') : {};
  
  const [user, setUser] = useState(currentUser);
  const [darkMode, setDarkMode] = useState(!!userData.darkMode);

  useEffect(() => {
    if (user) {
      const userKey = `user_${user}`;
      const userData = JSON.parse(localStorage.getItem(userKey) || '{}');
      setDarkMode(!!userData.darkMode);
    }
  }, [user]);

  useEffect(() => {
    if (user) {
      const userKey = `user_${user}`;
      const userData = JSON.parse(localStorage.getItem(userKey) || '{}');
      userData.darkMode = darkMode;
      localStorage.setItem(userKey, JSON.stringify(userData));
    }
  }, [darkMode, user]);

  const handleLogin = (username) => {
    setUser(username);
    localStorage.setItem('currentUser', username);
    window.location.href = '/';
  };

  const handleLogout = () => {
    setUser('');
    localStorage.removeItem('currentUser');
    setDarkMode(false);
  };

  const handleToggleDarkMode = () => setDarkMode(!darkMode);

  if (!user) {
    return <Login onLogin={handleLogin} darkMode={false} />;
  }

  const userObj = JSON.parse(localStorage.getItem(`user_${user}`) || '{}');

  return (
    <Router>
      <div className={`app${darkMode ? ' dark-mode' : ''}`} style={{ position: 'relative' }}>
        <Navigation onLogout={handleLogout} user={userObj} />
        <TopRightSettings />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard user={user} />} />
            <Route path="/budget" element={<Budget user={user} />} />
            <Route path="/fitness" element={<Fitness user={user} />} />
            <Route path="/water" element={<WaterTracker user={user} />} />
            <Route path="/sleep" element={<SleepTracker user={user} />} />
            <Route path="/goals" element={<Goals user={userObj} />} />
            <Route path="/habits" element={<Habits user={userObj} />} />
            <Route path="/pomodoro" element={<Pomodoro user={user} />} />
            <Route path="/notes" element={<QuickNotes user={user} />} />
            <Route path="/mood" element={<MoodTracker user={user} />} />
            <Route path="/achievements" element={<Achievements user={user} />} />
            <Route path="/tasks" element={<Tasks user={userObj} />} />
            <Route path="/settings" element={<Settings onToggleDarkMode={handleToggleDarkMode} darkMode={darkMode} user={user} onLogout={handleLogout} userEmail={userObj?.email || ''} />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App; 
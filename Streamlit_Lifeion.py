<!DOCTYPE html>
<!-- saved from url=(0022)http://localhost:3000/ -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <link rel="icon" href="http://localhost:3000/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#000000">
    <meta name="description" content="lifeion - Your comprehensive life management app">
    <title>lifeion</title>
    <link href="./lifeion_files/css2" rel="stylesheet">
  <script defer="" src="./lifeion_files/bundle.js.download"></script><style>* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  color: #333;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
}

.btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s ease;
  font-size: 14px;
}

.btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  background: #f8f9fa;
  color: #333;
  border: 1px solid #e9ecef;
}

.btn-secondary:hover {
  background: #e9ecef;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.input {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-size: 14px;
  transition: border-color 0.2s ease;
}

.input:focus {
  outline: none;
  border-color: #667eea;
}

.grid {
  display: grid;
  gap: 20px;
}

.grid-2 {
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}

.grid-3 {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

.flex {
  display: flex;
  align-items: center;
}

.flex-between {
  justify-content: space-between;
}

.flex-center {
  justify-content: center;
}

.text-center {
  text-align: center;
}

.mb-4 {
  margin-bottom: 16px;
}

.mb-2 {
  margin-bottom: 8px;
}

.mt-4 {
  margin-top: 16px;
}

.text-lg {
  font-size: 18px;
  font-weight: 600;
}

.text-xl {
  font-size: 24px;
  font-weight: 700;
}

.text-gray {
  color: #6c757d;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: #e9ecef;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  transition: width 0.3s ease;
}

@media (max-width: 768px) {
  .container {
    padding: 16px;
  }
  
  .card {
    padding: 16px;
  }
  
  .grid-2,
  .grid-3 {
    grid-template-columns: 1fr;
  }
} 
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL3NyYy9pbmRleC5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7RUFDRSxTQUFTO0VBQ1QsVUFBVTtFQUNWLHNCQUFzQjtBQUN4Qjs7QUFFQTtFQUNFOztjQUVZO0VBQ1osbUNBQW1DO0VBQ25DLGtDQUFrQztFQUNsQyw2REFBNkQ7RUFDN0QsaUJBQWlCO0VBQ2pCLFdBQVc7QUFDYjs7QUFFQTtFQUNFO2FBQ1c7QUFDYjs7QUFFQTtFQUNFLGlCQUFpQjtFQUNqQixjQUFjO0VBQ2QsYUFBYTtBQUNmOztBQUVBO0VBQ0UsaUJBQWlCO0VBQ2pCLG1CQUFtQjtFQUNuQixhQUFhO0VBQ2IsMENBQTBDO0VBQzFDLG1CQUFtQjtFQUNuQixxREFBcUQ7QUFDdkQ7O0FBRUE7RUFDRSwyQkFBMkI7RUFDM0IsMkNBQTJDO0FBQzdDOztBQUVBO0VBQ0UsNkRBQTZEO0VBQzdELFlBQVk7RUFDWixZQUFZO0VBQ1osa0JBQWtCO0VBQ2xCLGtCQUFrQjtFQUNsQixlQUFlO0VBQ2YsZ0JBQWdCO0VBQ2hCLHlCQUF5QjtFQUN6QixlQUFlO0FBQ2pCOztBQUVBO0VBQ0UsMkJBQTJCO0VBQzNCLCtDQUErQztBQUNqRDs7QUFFQTtFQUNFLG1CQUFtQjtFQUNuQixXQUFXO0VBQ1gseUJBQXlCO0FBQzNCOztBQUVBO0VBQ0UsbUJBQW1CO0VBQ25CLHlDQUF5QztBQUMzQzs7QUFFQTtFQUNFLFdBQVc7RUFDWCxrQkFBa0I7RUFDbEIseUJBQXlCO0VBQ3pCLGtCQUFrQjtFQUNsQixlQUFlO0VBQ2Ysa0NBQWtDO0FBQ3BDOztBQUVBO0VBQ0UsYUFBYTtFQUNiLHFCQUFxQjtBQUN2Qjs7QUFFQTtFQUNFLGFBQWE7RUFDYixTQUFTO0FBQ1g7O0FBRUE7RUFDRSwyREFBMkQ7QUFDN0Q7O0FBRUE7RUFDRSwyREFBMkQ7QUFDN0Q7O0FBRUE7RUFDRSxhQUFhO0VBQ2IsbUJBQW1CO0FBQ3JCOztBQUVBO0VBQ0UsOEJBQThCO0FBQ2hDOztBQUVBO0VBQ0UsdUJBQXVCO0FBQ3pCOztBQUVBO0VBQ0Usa0JBQWtCO0FBQ3BCOztBQUVBO0VBQ0UsbUJBQW1CO0FBQ3JCOztBQUVBO0VBQ0Usa0JBQWtCO0FBQ3BCOztBQUVBO0VBQ0UsZ0JBQWdCO0FBQ2xCOztBQUVBO0VBQ0UsZUFBZTtFQUNmLGdCQUFnQjtBQUNsQjs7QUFFQTtFQUNFLGVBQWU7RUFDZixnQkFBZ0I7QUFDbEI7O0FBRUE7RUFDRSxjQUFjO0FBQ2hCOztBQUVBO0VBQ0UsV0FBVztFQUNYLFdBQVc7RUFDWCxtQkFBbUI7RUFDbkIsa0JBQWtCO0VBQ2xCLGdCQUFnQjtBQUNsQjs7QUFFQTtFQUNFLFlBQVk7RUFDWiw0REFBNEQ7RUFDNUQsMkJBQTJCO0FBQzdCOztBQUVBO0VBQ0U7SUFDRSxhQUFhO0VBQ2Y7O0VBRUE7SUFDRSxhQUFhO0VBQ2Y7O0VBRUE7O0lBRUUsMEJBQTBCO0VBQzVCO0FBQ0YiLCJzb3VyY2VzQ29udGVudCI6WyIqIHtcclxuICBtYXJnaW46IDA7XHJcbiAgcGFkZGluZzogMDtcclxuICBib3gtc2l6aW5nOiBib3JkZXItYm94O1xyXG59XHJcblxyXG5ib2R5IHtcclxuICBmb250LWZhbWlseTogJ0ludGVyJywgLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAnU2Vnb2UgVUknLCAnUm9ib3RvJywgJ094eWdlbicsXHJcbiAgICAnVWJ1bnR1JywgJ0NhbnRhcmVsbCcsICdGaXJhIFNhbnMnLCAnRHJvaWQgU2FucycsICdIZWx2ZXRpY2EgTmV1ZScsXHJcbiAgICBzYW5zLXNlcmlmO1xyXG4gIC13ZWJraXQtZm9udC1zbW9vdGhpbmc6IGFudGlhbGlhc2VkO1xyXG4gIC1tb3otb3N4LWZvbnQtc21vb3RoaW5nOiBncmF5c2NhbGU7XHJcbiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgIzY2N2VlYSAwJSwgIzc2NGJhMiAxMDAlKTtcclxuICBtaW4taGVpZ2h0OiAxMDB2aDtcclxuICBjb2xvcjogIzMzMztcclxufVxyXG5cclxuY29kZSB7XHJcbiAgZm9udC1mYW1pbHk6IHNvdXJjZS1jb2RlLXBybywgTWVubG8sIE1vbmFjbywgQ29uc29sYXMsICdDb3VyaWVyIE5ldycsXHJcbiAgICBtb25vc3BhY2U7XHJcbn1cclxuXHJcbi5jb250YWluZXIge1xyXG4gIG1heC13aWR0aDogMTIwMHB4O1xyXG4gIG1hcmdpbjogMCBhdXRvO1xyXG4gIHBhZGRpbmc6IDIwcHg7XHJcbn1cclxuXHJcbi5jYXJkIHtcclxuICBiYWNrZ3JvdW5kOiB3aGl0ZTtcclxuICBib3JkZXItcmFkaXVzOiAxNnB4O1xyXG4gIHBhZGRpbmc6IDI0cHg7XHJcbiAgYm94LXNoYWRvdzogMCAxMHB4IDI1cHggcmdiYSgwLCAwLCAwLCAwLjEpO1xyXG4gIG1hcmdpbi1ib3R0b206IDIwcHg7XHJcbiAgdHJhbnNpdGlvbjogdHJhbnNmb3JtIDAuMnMgZWFzZSwgYm94LXNoYWRvdyAwLjJzIGVhc2U7XHJcbn1cclxuXHJcbi5jYXJkOmhvdmVyIHtcclxuICB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoLTJweCk7XHJcbiAgYm94LXNoYWRvdzogMCAxNXB4IDM1cHggcmdiYSgwLCAwLCAwLCAwLjE1KTtcclxufVxyXG5cclxuLmJ0biB7XHJcbiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgIzY2N2VlYSAwJSwgIzc2NGJhMiAxMDAlKTtcclxuICBjb2xvcjogd2hpdGU7XHJcbiAgYm9yZGVyOiBub25lO1xyXG4gIHBhZGRpbmc6IDEycHggMjRweDtcclxuICBib3JkZXItcmFkaXVzOiA4cHg7XHJcbiAgY3Vyc29yOiBwb2ludGVyO1xyXG4gIGZvbnQtd2VpZ2h0OiA1MDA7XHJcbiAgdHJhbnNpdGlvbjogYWxsIDAuMnMgZWFzZTtcclxuICBmb250LXNpemU6IDE0cHg7XHJcbn1cclxuXHJcbi5idG46aG92ZXIge1xyXG4gIHRyYW5zZm9ybTogdHJhbnNsYXRlWSgtMXB4KTtcclxuICBib3gtc2hhZG93OiAwIDVweCAxNXB4IHJnYmEoMTAyLCAxMjYsIDIzNCwgMC40KTtcclxufVxyXG5cclxuLmJ0bi1zZWNvbmRhcnkge1xyXG4gIGJhY2tncm91bmQ6ICNmOGY5ZmE7XHJcbiAgY29sb3I6ICMzMzM7XHJcbiAgYm9yZGVyOiAxcHggc29saWQgI2U5ZWNlZjtcclxufVxyXG5cclxuLmJ0bi1zZWNvbmRhcnk6aG92ZXIge1xyXG4gIGJhY2tncm91bmQ6ICNlOWVjZWY7XHJcbiAgYm94LXNoYWRvdzogMCA1cHggMTVweCByZ2JhKDAsIDAsIDAsIDAuMSk7XHJcbn1cclxuXHJcbi5pbnB1dCB7XHJcbiAgd2lkdGg6IDEwMCU7XHJcbiAgcGFkZGluZzogMTJweCAxNnB4O1xyXG4gIGJvcmRlcjogMnB4IHNvbGlkICNlOWVjZWY7XHJcbiAgYm9yZGVyLXJhZGl1czogOHB4O1xyXG4gIGZvbnQtc2l6ZTogMTRweDtcclxuICB0cmFuc2l0aW9uOiBib3JkZXItY29sb3IgMC4ycyBlYXNlO1xyXG59XHJcblxyXG4uaW5wdXQ6Zm9jdXMge1xyXG4gIG91dGxpbmU6IG5vbmU7XHJcbiAgYm9yZGVyLWNvbG9yOiAjNjY3ZWVhO1xyXG59XHJcblxyXG4uZ3JpZCB7XHJcbiAgZGlzcGxheTogZ3JpZDtcclxuICBnYXA6IDIwcHg7XHJcbn1cclxuXHJcbi5ncmlkLTIge1xyXG4gIGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KGF1dG8tZml0LCBtaW5tYXgoMzAwcHgsIDFmcikpO1xyXG59XHJcblxyXG4uZ3JpZC0zIHtcclxuICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IHJlcGVhdChhdXRvLWZpdCwgbWlubWF4KDI1MHB4LCAxZnIpKTtcclxufVxyXG5cclxuLmZsZXgge1xyXG4gIGRpc3BsYXk6IGZsZXg7XHJcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcclxufVxyXG5cclxuLmZsZXgtYmV0d2VlbiB7XHJcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xyXG59XHJcblxyXG4uZmxleC1jZW50ZXIge1xyXG4gIGp1c3RpZnktY29udGVudDogY2VudGVyO1xyXG59XHJcblxyXG4udGV4dC1jZW50ZXIge1xyXG4gIHRleHQtYWxpZ246IGNlbnRlcjtcclxufVxyXG5cclxuLm1iLTQge1xyXG4gIG1hcmdpbi1ib3R0b206IDE2cHg7XHJcbn1cclxuXHJcbi5tYi0yIHtcclxuICBtYXJnaW4tYm90dG9tOiA4cHg7XHJcbn1cclxuXHJcbi5tdC00IHtcclxuICBtYXJnaW4tdG9wOiAxNnB4O1xyXG59XHJcblxyXG4udGV4dC1sZyB7XHJcbiAgZm9udC1zaXplOiAxOHB4O1xyXG4gIGZvbnQtd2VpZ2h0OiA2MDA7XHJcbn1cclxuXHJcbi50ZXh0LXhsIHtcclxuICBmb250LXNpemU6IDI0cHg7XHJcbiAgZm9udC13ZWlnaHQ6IDcwMDtcclxufVxyXG5cclxuLnRleHQtZ3JheSB7XHJcbiAgY29sb3I6ICM2Yzc1N2Q7XHJcbn1cclxuXHJcbi5wcm9ncmVzcy1iYXIge1xyXG4gIHdpZHRoOiAxMDAlO1xyXG4gIGhlaWdodDogOHB4O1xyXG4gIGJhY2tncm91bmQ6ICNlOWVjZWY7XHJcbiAgYm9yZGVyLXJhZGl1czogNHB4O1xyXG4gIG92ZXJmbG93OiBoaWRkZW47XHJcbn1cclxuXHJcbi5wcm9ncmVzcy1maWxsIHtcclxuICBoZWlnaHQ6IDEwMCU7XHJcbiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDkwZGVnLCAjNjY3ZWVhIDAlLCAjNzY0YmEyIDEwMCUpO1xyXG4gIHRyYW5zaXRpb246IHdpZHRoIDAuM3MgZWFzZTtcclxufVxyXG5cclxuQG1lZGlhIChtYXgtd2lkdGg6IDc2OHB4KSB7XHJcbiAgLmNvbnRhaW5lciB7XHJcbiAgICBwYWRkaW5nOiAxNnB4O1xyXG4gIH1cclxuICBcclxuICAuY2FyZCB7XHJcbiAgICBwYWRkaW5nOiAxNnB4O1xyXG4gIH1cclxuICBcclxuICAuZ3JpZC0yLFxyXG4gIC5ncmlkLTMge1xyXG4gICAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxZnI7XHJcbiAgfVxyXG59ICdLCJzb3VyY2VSb290IjoiIn0= */</style><style>.app {
  display: flex;
  min-height: 100vh;
}

/* --- Modern Sidebar --- */
.navigation {
  width: 220px;
  min-width: 220px;
  background: rgba(40, 44, 52, 0.85);
  backdrop-filter: blur(16px) saturate(1.2);
  box-shadow: 0 8px 32px rgba(40, 44, 52, 0.18), 2px 0 24px rgba(102, 126, 234, 0.08);
  border-radius: 24px;
  padding: 32px 0 24px 0;
  position: fixed;
  height: 92vh;
  top: 4vh;
  left: 24px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  z-index: 10;
  border: 1.5px solid rgba(102, 126, 234, 0.08);
  box-sizing: border-box;
  overflow-x: hidden;
}

.nav-header {
  padding: 0 32px 28px;
  border-bottom: 1.5px solid rgba(102, 126, 234, 0.08);
  margin-bottom: 28px;
}

.nav-header h2 {
  color: #fff;
  font-size: 22px;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-shadow: 0 2px 8px rgba(102, 126, 234, 0.12);
}

.nav-items {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 14px 32px 14px 24px;
  color: #bfc7d5;
  text-decoration: none;
  font-weight: 600;
  font-size: 16px;
  border-radius: 12px;
  position: relative;
  transition: all 0.18s cubic-bezier(0.4,0,0.2,1);
  cursor: pointer;
  overflow: hidden;
}

.nav-item svg {
  width: 26px;
  height: 26px;
  opacity: 0.92;
  filter: drop-shadow(0 1px 4px rgba(102,126,234,0.08));
}

.nav-item:hover {
  background: rgba(102, 126, 234, 0.10);
  color: #fff;
  transform: scale(1.045);
  box-shadow: 0 2px 12px rgba(102,126,234,0.08);
}

.nav-item.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  border-radius: 12px;
  margin-right: 0;
  box-shadow: 0 4px 24px rgba(102,126,234,0.18);
}

.nav-item.active::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  bottom: 8px;
  width: 6px;
  border-radius: 6px;
  background: linear-gradient(180deg, #ffd93d 0%, #667eea 100%);
  box-shadow: 0 0 12px 2px #ffd93d66;
}

.profile-pic-tab {
  margin-bottom: 18px !important;
  margin-left: 0 !important;
  padding-left: 24px !important;
  padding-right: 24px !important;
  padding-top: 8px !important;
  padding-bottom: 8px !important;
  background: rgba(255,255,255,0.07);
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(102,126,234,0.10);
  border: 1.5px solid rgba(102,126,234,0.10);
  display: flex;
  align-items: center;
  justify-content: flex-start;
}
.profile-pic-tab img {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  object-fit: cover;
  border: 2.5px solid #667eea;
  box-shadow: 0 2px 12px rgba(102,126,234,0.10);
}

/* XP/Level System Styles */
.xp-level-box {
  margin-top: 4px;
  margin-bottom: 2px;
  width: 100%;
  text-align: center;
}
.xp-level-label {
  font-weight: 700;
  font-size: 13px;
  color: #ffd93d;
  letter-spacing: 0.04em;
  margin-bottom: 2px;
}
.xp-bar-bg {
  width: 80%;
  height: 8px;
  background: rgba(102,126,234,0.13);
  border-radius: 8px;
  margin: 0 auto;
  position: relative;
  overflow: hidden;
}
.xp-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #ffd93d 0%, #667eea 100%);
  border-radius: 8px;
  transition: width 0.5s cubic-bezier(0.4,0,0.2,1);
}
.xp-label {
  font-size: 11px;
  color: #bfc7d5;
  margin-top: 2px;
}
.app.dark-mode .xp-bar-bg {
  background: rgba(255,255,255,0.08);
}
.app.dark-mode .xp-label {
  color: #ffd93d;
}

/* --- Dark Mode Sidebar --- */
.app.dark-mode .navigation {
  background: rgba(35, 39, 43, 0.92);
  box-shadow: 0 8px 32px rgba(40, 44, 52, 0.28), 2px 0 24px rgba(102, 126, 234, 0.12);
  border: 1.5px solid rgba(102, 126, 234, 0.13);
}
.app.dark-mode .nav-header h2 {
  color: #ffd93d;
  text-shadow: 0 2px 8px #23272b;
}
.app.dark-mode .nav-item {
  color: #bfc7d5;
}
.app.dark-mode .nav-item.active {
  background: linear-gradient(135deg, #23272b 0%, #667eea 100%);
  color: #ffd93d;
  box-shadow: 0 4px 24px #23272b99;
}
.app.dark-mode .nav-item.active::before {
  background: linear-gradient(180deg, #ffd93d 0%, #667eea 100%);
  box-shadow: 0 0 12px 2px #ffd93d99;
}
.app.dark-mode .profile-pic-tab {
  background: rgba(255,255,255,0.04);
  border: 1.5px solid #23272b;
}
.app.dark-mode .profile-pic-tab img {
  border: 2.5px solid #ffd93d;
}

/* --- Responsive Sidebar --- */
@media (max-width: 900px) {
  .navigation {
    width: 64px;
    min-width: 64px;
    padding: 16px 0 16px 0;
    border-radius: 16px;
    left: 8px;
  }
  .nav-header {
    padding: 0 8px 12px;
    margin-bottom: 12px;
  }
  .nav-header h2 {
    font-size: 0;
  }
  .nav-items {
    gap: 2px;
  }
  .nav-item {
    padding: 10px 10px 10px 10px;
    gap: 0;
    justify-content: center;
    font-size: 0;
  }
  .nav-item span {
    display: none;
  }
  .profile-pic-tab {
    padding-left: 4px !important;
    padding-right: 4px !important;
    padding-top: 4px !important;
    padding-bottom: 4px !important;
    margin-bottom: 8px !important;
  }
  .profile-pic-tab img {
    width: 40px;
    height: 40px;
  }
}

/* --- End Modern Sidebar --- */

.main-content {
  flex: 1 1;
  margin-left: 280px;
  padding: 24px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

.app.dark-mode {
  background: #181a1b;
}
.app.dark-mode .main-content {
  background: #181a1b;
  color: #f1f1f1;
}
.app.dark-mode .card {
  background: #23272b;
  color: #f1f1f1;
  box-shadow: 0 4px 24px rgba(0,0,0,0.7);
}
.app.dark-mode .btn {
  background: linear-gradient(135deg, #23272b 0%, #181a1b 100%);
  color: #fff;
}
.app.dark-mode .input {
  background: #23272b;
  color: #fff;
  border-color: #444;
}
.app.dark-mode .text-gray {
  color: #aaa;
}
.app.dark-mode .navigation {
  background: #23272b;
  box-shadow: 2px 0 10px rgba(0,0,0,0.7);
}
.app.dark-mode .nav-header h2 {
  color: #f1f1f1;
}
.app.dark-mode .nav-item {
  color: #aaa;
}
.app.dark-mode .nav-item.active {
  background: linear-gradient(135deg, #333 0%, #23272b 100%);
  color: #fff;
}

/* Switch for dark mode */
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 22px;
}
.switch input { display: none; }
.slider {
  position: absolute;
  cursor: pointer;
  top: 0; left: 0; right: 0; bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 22px;
}
.slider:before {
  position: absolute;
  content: "";
  height: 16px;
  width: 16px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}
input:checked + .slider {
  background-color: #667eea;
}
input:checked + .slider:before {
  transform: translateX(18px);
}

.settings-btn {
  position: absolute;
  top: 24px;
  right: 32px;
  background: #fff;
  border: 2px solid #667eea;
  border-radius: 50%;
  padding: 10px;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.15);
  transition: background 0.2s, border-color 0.2s, box-shadow 0.2s;
  z-index: 100;
}
.settings-btn:hover {
  background: #667eea;
  border-color: #764ba2;
  box-shadow: 0 4px 16px rgba(102, 126, 234, 0.25);
}
.settings-btn svg {
  color: #667eea;
  width: 32px;
  height: 32px;
  transition: color 0.2s;
}
.settings-btn:hover svg {
  color: #fff;
}
.app.dark-mode .settings-btn {
  background: #23272b;
  border: 2px solid #667eea;
  box-shadow: 0 0 0 6px rgba(102,126,234,0.25), 0 0 24px 8px #667eea44;
}
.app.dark-mode .settings-btn:hover {
  background: #667eea;
  border-color: #fff;
  box-shadow: 0 0 0 8px #667eea88, 0 0 32px 12px #667eea66;
}
.app.dark-mode .settings-btn svg {
  color: #fff;
}

.settings-btn.settings-bubble {
  position: absolute;
  top: 20px;
  right: 24px;
  background: #fff;
  border: 2px solid #667eea;
  border-radius: 50%;
  padding: 6px;
  box-shadow: 0 0 0 7px rgba(102,126,234,0.18), 0 0 24px 10px #667eea33;
  transition: background 0.2s, border-color 0.2s, box-shadow 0.2s;
  z-index: 100;
}
.settings-btn.settings-bubble:hover {
  background: #667eea;
  border-color: #764ba2;
  box-shadow: 0 0 0 12px #667eea44, 0 0 32px 14px #667eea77;
}
.settings-btn.settings-bubble svg {
  color: #222;
  width: 22px;
  height: 22px;
  transition: color 0.2s;
}
.settings-btn.settings-bubble:hover svg {
  color: #fff;
}
.app.dark-mode .settings-btn.settings-bubble {
  background: #23272b;
  border: 2px solid #667eea;
  box-shadow: 0 0 0 10px rgba(102,126,234,0.28), 0 0 32px 12px #667eea55;
}
.app.dark-mode .settings-btn.settings-bubble:hover {
  background: #667eea;
  border-color: #fff;
  box-shadow: 0 0 0 16px #667eea77, 0 0 48px 20px #667eea99;
}
.app.dark-mode .settings-btn.settings-bubble svg {
  color: #fff;
}

/* Grid layouts for new components */
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.grid-5 {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0.5rem;
}

/* Mood tracker styles */
.mood-option {
  transition: transform 0.2s ease;
}

.mood-option:hover {
  transform: scale(1.05);
}

/* Pomodoro timer styles */
.pomodoro-circle {
  transition: stroke-dashoffset 1s linear;
}

/* Quick notes styles */
.note-card {
  transition: all 0.3s ease;
}

.note-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .grid-3 {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .grid-5 {
    grid-template-columns: repeat(3, 1fr);
  }

  .settings-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .widget-controls {
    padding: 12px 16px;
  }

  .widget-title {
    font-size: 14px;
    margin: 0 12px;
  }

  .customize-btn {
    padding: 10px 16px;
    font-size: 13px;
  }

  .empty-state {
    padding: 60px 20px;
  }

  .empty-title {
    font-size: 20px;
  }

  .empty-description {
    font-size: 14px;
  }
}

@media (max-width: 480px) {
  .grid-3 {
    grid-template-columns: 1fr;
  }
  
  .grid-5 {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Animation for progress bars */
@keyframes progress {
  from { width: 0%; }
  to { width: var(--progress); }
}

.progress-bar {
  animation: progress 1s ease-out;
}

/* Hover effects for interactive elements */
.interactive:hover {
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Dark mode specific styles */
.dark-mode .mood-option {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.2);
}

.dark-mode .note-card {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.1);
}

/* Dashboard Widget Styles */
.widget-container {
  background: transparent;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: none;
  border: none;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.widget-container.customizing {
  background: white;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.widget-container:hover {
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  transform: translateY(-4px);
}

.widget-container.dragging {
  opacity: 0.7;
  transform: rotate(1deg) scale(1.02);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
  z-index: 1000;
}

.widget-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 0;
  position: relative;
}

.widget-controls {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  color: white;
}

.drag-handle {
  display: flex;
  align-items: center;
  cursor: grab;
  padding: 4px;
  border-radius: 6px;
  transition: all 0.2s ease;
  opacity: 0.7;
}

.drag-handle:hover {
  opacity: 1;
  background: rgba(255, 255, 255, 0.1);
}

.drag-handle:active {
  cursor: grabbing;
}

.grip-icon {
  color: rgba(255, 255, 255, 0.9);
  transition: color 0.2s ease;
}

.drag-handle:hover .grip-icon {
  color: white;
}

.widget-title {
  font-weight: 600;
  font-size: 16px;
  letter-spacing: 0.025em;
  flex: 1 1;
  text-align: center;
  margin: 0 16px;
}

.widget-actions {
  display: flex;
  align-items: center;
}

.hide-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border: none;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: rgba(255, 255, 255, 0.8);
  cursor: pointer;
  transition: all 0.2s ease;
  backdrop-filter: blur(10px);
}

.hide-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  transform: scale(1.05);
}

.widget-content {
  background: white;
  padding: 0;
}

/* Drag and Drop Visual Feedback */
.widget-container[draggable="true"] {
  cursor: grab;
}

.widget-container[draggable="true"]:active {
  cursor: grabbing;
}

.widgets-container {
  min-height: 200px;
}

/* Settings Panel Styles */
.settings-panel {
  background: white;
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(0, 0, 0, 0.05);
  overflow: hidden;
}

.settings-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: white;
}

.settings-title {
  font-size: 20px;
  font-weight: 600;
  margin: 0;
  letter-spacing: 0.025em;
}

.close-settings-btn {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: white;
  width: 32px;
  height: 32px;
  border-radius: 8px;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.2s ease;
  backdrop-filter: blur(10px);
}

.close-settings-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

.settings-content {
  padding: 24px;
}

.settings-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  margin-bottom: 24px;
}

.section-title {
  font-size: 16px;
  font-weight: 600;
  color: #333;
  margin-bottom: 16px;
  letter-spacing: 0.025em;
}

.widget-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.widget-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px;
  background: #f8f9fa;
  border-radius: 12px;
  border: 1px solid rgba(0, 0, 0, 0.05);
  transition: all 0.2s ease;
}

.widget-item:hover {
  background: #f1f3f4;
  transform: translateY(-1px);
}

.widget-name {
  font-weight: 500;
  color: #333;
}

.visibility-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
  font-weight: 500;
}

.visibility-toggle.active {
  background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
  color: white;
  box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
}

.visibility-toggle.inactive {
  background: linear-gradient(135deg, #6c757d 0%, #5a6268 100%);
  color: white;
  box-shadow: 0 2px 8px rgba(108, 117, 125, 0.3);
}

.visibility-toggle:hover {
  transform: scale(1.05);
}

.instructions-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.instruction-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 16px;
  background: #f8f9fa;
  border-radius: 12px;
  border: 1px solid rgba(0, 0, 0, 0.05);
  transition: all 0.2s ease;
}

.instruction-item:hover {
  background: #f1f3f4;
  transform: translateY(-1px);
}

.instruction-icon {
  font-size: 24px;
  flex-shrink: 0;
}

.instruction-content h4 {
  font-weight: 600;
  color: #333;
  margin: 0 0 4px 0;
  font-size: 14px;
}

.instruction-content p {
  color: #666;
  margin: 0;
  font-size: 13px;
  line-height: 1.4;
}

.settings-actions {
  display: flex;
  justify-content: center;
  padding-top: 16px;
  border-top: 1px solid rgba(0, 0, 0, 0.05);
}

.reset-btn {
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 12px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(255, 107, 107, 0.3);
}

.reset-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(255, 107, 107, 0.4);
}

/* Customize Button */
.customize-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 12px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  letter-spacing: 0.025em;
}

.customize-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(102, 126, 234, 0.4);
}

.customize-btn.active {
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
  box-shadow: 0 4px 16px rgba(255, 107, 107, 0.3);
}

.customize-btn.active:hover {
  box-shadow: 0 6px 24px rgba(255, 107, 107, 0.4);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 80px 24px;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  border-radius: 20px;
  border: 2px dashed rgba(102, 126, 234, 0.2);
}

.empty-icon {
  color: #667eea;
  margin-bottom: 24px;
  opacity: 0.7;
}

.empty-title {
  font-size: 24px;
  font-weight: 600;
  color: #333;
  margin-bottom: 12px;
  letter-spacing: 0.025em;
}

.empty-description {
  color: #666;
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 32px;
  max-width: 400px;
  margin-left: auto;
  margin-right: auto;
}

.empty-action-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 16px 32px;
  border-radius: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-size: 16px;
  letter-spacing: 0.025em;
}

.empty-action-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 32px rgba(102, 126, 234, 0.4);
}

/* Dark Mode Widget Styles */
.app.dark-mode .widget-container {
  background: transparent;
  box-shadow: none;
  border: none;
}

.app.dark-mode .widget-container.customizing {
  background: #23272b;
  box-shadow: 0 4px 20px rgba(0,0,0,0.25);
  border: 1px solid #333;
}

.app.dark-mode .widget-header {
  background: linear-gradient(135deg, #2c3034 0%, #23272b 100%);
  border-bottom: 1px solid #444;
}

.app.dark-mode .widget-header:hover {
  background: linear-gradient(135deg, #23272b 0%, #1e2124 100%);
}

.app.dark-mode .widget-content {
  background: #23272b;
  color: #f1f1f1;
}

.app.dark-mode .settings-panel {
  background: linear-gradient(135deg, #2c3034 0%, #23272b 100%);
  border: 1px solid #444;
}

.app.dark-mode .widget-toggle.active {
  background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
}

.app.dark-mode .widget-toggle.inactive {
  background: linear-gradient(135deg, #6c757d 0%, #5a6268 100%);
} 

.customize-row {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 32px;
} 

.drag-handle, .hide-btn {
  display: none;
}

.widget-container.customizing .drag-handle,
.widget-container.customizing .hide-btn {
  display: flex;
} 

/* Hide scrollbars in sidebar and main content */
.navigation, .main-content, .container {
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE 10+ */
}
.navigation::-webkit-scrollbar,
.main-content::-webkit-scrollbar,
.container::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera */
} 

/* Confetti Overlay Styles */
.confetti-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  width: 100vw; height: 100vh;
  z-index: 9999;
  pointer-events: none;
  background: transparent;
  animation: confetti-fadeout 2s forwards;
}
@keyframes confetti-fadeout {
  0% { opacity: 1; }
  80% { opacity: 1; }
  100% { opacity: 0; }
}
.confetti-piece {
  position: absolute;
  border-radius: 4px;
  opacity: 0.85;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  animation: confetti-fall 1.5s cubic-bezier(0.4,0,0.2,1) forwards;
}
@keyframes confetti-fall {
  0% { transform: translateY(0) scale(1) rotate(var(--angle,0deg)); opacity: 1; }
  80% { opacity: 1; }
  100% { transform: translateY(60vh) scale(0.8) rotate(var(--angle,0deg)); opacity: 0; }
} 
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL3NyYy9BcHAuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBO0VBQ0UsYUFBYTtFQUNiLGlCQUFpQjtBQUNuQjs7QUFFQSwyQkFBMkI7QUFDM0I7RUFDRSxZQUFZO0VBQ1osZ0JBQWdCO0VBQ2hCLGtDQUFrQztFQUNsQyx5Q0FBeUM7RUFDekMsbUZBQW1GO0VBQ25GLG1CQUFtQjtFQUNuQixzQkFBc0I7RUFDdEIsZUFBZTtFQUNmLFlBQVk7RUFDWixRQUFRO0VBQ1IsVUFBVTtFQUNWLGdCQUFnQjtFQUNoQixhQUFhO0VBQ2Isc0JBQXNCO0VBQ3RCLFdBQVc7RUFDWCw2Q0FBNkM7RUFDN0Msc0JBQXNCO0VBQ3RCLGtCQUFrQjtBQUNwQjs7QUFFQTtFQUNFLG9CQUFvQjtFQUNwQixvREFBb0Q7RUFDcEQsbUJBQW1CO0FBQ3JCOztBQUVBO0VBQ0UsV0FBVztFQUNYLGVBQWU7RUFDZixnQkFBZ0I7RUFDaEIsc0JBQXNCO0VBQ3RCLGdEQUFnRDtBQUNsRDs7QUFFQTtFQUNFLGFBQWE7RUFDYixzQkFBc0I7RUFDdEIsUUFBUTtBQUNWOztBQUVBO0VBQ0UsYUFBYTtFQUNiLG1CQUFtQjtFQUNuQixTQUFTO0VBQ1QsNEJBQTRCO0VBQzVCLGNBQWM7RUFDZCxxQkFBcUI7RUFDckIsZ0JBQWdCO0VBQ2hCLGVBQWU7RUFDZixtQkFBbUI7RUFDbkIsa0JBQWtCO0VBQ2xCLCtDQUErQztFQUMvQyxlQUFlO0VBQ2YsZ0JBQWdCO0FBQ2xCOztBQUVBO0VBQ0UsV0FBVztFQUNYLFlBQVk7RUFDWixhQUFhO0VBQ2IscURBQXFEO0FBQ3ZEOztBQUVBO0VBQ0UscUNBQXFDO0VBQ3JDLFdBQVc7RUFDWCx1QkFBdUI7RUFDdkIsNkNBQTZDO0FBQy9DOztBQUVBO0VBQ0UsNkRBQTZEO0VBQzdELFdBQVc7RUFDWCxtQkFBbUI7RUFDbkIsZUFBZTtFQUNmLDZDQUE2QztBQUMvQzs7QUFFQTtFQUNFLFdBQVc7RUFDWCxrQkFBa0I7RUFDbEIsT0FBTztFQUNQ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QzdELHNCQUFzQjtBQUN4Qjs7QUFFQTtFQUNFLDZEQUE2RDtBQUMvRDs7QUFFQTtFQUNFLDZEQUE2RDtBQUMvRDs7QUFFQTtFQUNFLGFBQWE7RUFDYix1QkFBdUI7RUFDdkIsbUJBQW1CO0VBQ25CLG1CQUFtQjtBQUNyQjs7QUFFQTtFQUNFLGFBQWE7QUFDZjs7QUFFQTs7RUFFRSxhQUFhO0FBQ2Y7O0FBRUEsZ0RBQWdEO0FBQ2hEO0VBQ0UscUJBQXFCLEVBQUUsWUFBWTtFQUNuQyx3QkFBd0IsRUFBRSxXQUFXO0FBQ3ZDO0FBQ0E7OztFQUdFLGFBQWEsRUFBRSwwQkFBMEI7QUFDM0M7O0FBRUEsNEJBQTRCO0FBQzVCO0VBQ0UsZUFBZTtFQUNmLE1BQU0sRUFBRSxPQUFPLEVBQUUsUUFBUSxFQUFFLFNBQVM7RUFDcEMsWUFBWSxFQUFFLGFBQWE7RUFDM0IsYUFBYTtFQUNiLG9CQUFvQjtFQUNwQix1QkFBdUI7RUFDdkIsdUNBQXVDO0FBQ3pDO0FBQ0E7RUFDRSxLQUFLLFVBQVUsRUFBRTtFQUNqQixNQUFNLFVBQVUsRUFBRTtFQUNsQixPQUFPLFVBQVUsRUFBRTtBQUNyQjtBQUNBO0VBQ0Usa0JBQWtCO0VBQ2xCLGtCQUFrQjtFQUNsQixhQUFhO0VBQ2Isc0NBQXNDO0VBQ3RDLGdFQUFnRTtBQUNsRTtBQUNBO0VBQ0UsS0FBSywyREFBMkQsRUFBRSxVQUFVLEVBQUU7RUFDOUUsTUFBTSxVQUFVLEVBQUU7RUFDbEIsT0FBTyxnRUFBZ0UsRUFBRSxVQUFVLEVBQUU7QUFDdkYiLCJzb3VyY2VzQ29udGVudCI6WyIuYXBwIHtcclxuICBkaXNwbGF5OiBmbGV4O1xyXG4gIG1pbi1oZWlnaHQ6IDEwMHZoO1xyXG59XHJcblxyXG4vKiAtLS0gTW9kZXJuIFNpZGViYXIgLS0tICovXHJcbi5uYXZpZ2F0aW9uIHtcclxuICB3aWR0aDogMjIwcHg7XHJcbiAgbWluLXdpZHRoOiAyMjBweDtcclxuICBiYWNrZ3JvdW5kOiByZ2JhKDQwLCA0NCwgNTIsIDAuODUpO1xyXG4gIGJhY2tkcm9wLWZpbHRlcjogYmx1cigxNnB4KSBzYXR1cmF0ZSgxLjIpO1xyXG4gIGJveC1zaGFkb3c6IDAgOHB4IDMycHggcmdiYSg0MCwgNDQsIDUyLCAwLjE4KSwgMnB4IDAgMjRweCByZ2JhKDEwMiwgMTI2LCAyMzQsIDAuMDgpO1xyXG4gIGJvcmRlci1yYWRpdXM6IDI0cHg7XHJcbiAgcGFkZGluZzogMzJweCAwIDI0cHggMDtcclxuICBwb3NpdGlvbjogZml4ZWQ7XHJcbiAgaGVpZ2h0OiA5MnZoO1xyXG4gIHRvcDogNHZoO1xyXG4gIGxlZnQ6IDI0cHg7XHJcbiAgb3ZlcmZsb3cteTogYXV0bztcclxuICBkaXNwbGF5OiBmbGV4O1xyXG4gIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XHJcbiAgei1pbmRleDogMTA7XHJcbiAgYm9yZGVyOiAxLjVweCBzb2xpZCByZ2JhKDEwMiwgMTI2LCAyMzQsIDAuMDgpO1xyXG4gIGJveC1zaXppbmc6IGJvcmRlci1ib3g7XHJcbiAgb3ZlcmZsb3cteDogaGlkZGVuO1xyXG59XHJcblxyXG4ubmF2LWhlYWRlciB7XHJcbiAgcGFkZGluZzogMCAzMnB4IDI4cHg7XHJcbiAgYm9yZGVyLWJvdHRvbTogMS41cHggc29saWQgcmdiYSgxMDIsIDEyNiwgMjM0LCAwLjA4KTtcclxuICBtYXJnaW4tYm90dG9tOiAyOHB4O1xyXG59XHJcblxyXG4ubmF2LWhlYWRlciBoMiB7XHJcbiAgY29sb3I6ICNmZmY7XHJcbiAgZm9udC1zaXplOiAyMnB4O1xyXG4gIGZvbnQtd2VpZ2h0OiA4MDA7XHJcbiAgbGV0dGVyLXNwYWNpbmc6IDAuMDRlbTtcclxuICB0ZXh0LXNoYWRvdzogMCAycHggOHB4IHJnYmEoMTAyLCAxMjYsIDIzNCwgMC4xMik7XHJcbn1cclxuXHJcbi5uYXYtaXRlbXMge1xyXG4gIGRpc3BsYXk6IGZsZXg7XHJcbiAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcclxuICBnYXA6IDhweDtcclxufVxyXG5cclxuLm5hdi1pdGVtIHtcclxuICBkaXNwbGF5OiBmbGV4O1xyXG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XHJcbiAgZ2FwOiAxOHB4O1xyXG4gIHBhZGRpbmc6IDE0cHggMzJweCAxNHB4IDI0cHg7XHJcbiAgY29sb3I6ICNiZmM3ZDU7XHJcbiAgdGV4dC1kZWNvcmF0aW9uOiBub25lO1xyXG4gIGZvbnQtd2VpZ2h0OiA2MDA7XHJcbiAgZm9udC1zaXplOiAxNnB4O1xyXG4gIGJvcmRlci1yYWRpdXM6IDEycHg7XHJcbiAgcG9zaXRpb246IHJlbGF0aXZlO1xyXG4gIHRyYW5zaXRpb246IGFsbCAwLjE4cyBjdWJpYy1iZXppZXIoMC40LDAsMC4yLDEpO1xyXG4gIGN1cnNvcjogcG9pbnRlcjtcclxuICBvdmVyZmxvdzogaGlkZGVuO1xyXG59XHJcblxyXG4ubmF2LWl0ZW0gc3ZnIHtcclxuICB3aWR0aDogMjZweDtcclxuICBoZWlnaHQ6IDI2cHg7XHJcbiAgb3BhY2l0eTogMC45MjtcclxuICBmaWx0ZXI6IGRyb3Atc2hhZG93KDAgMXB4IDRweCByZ2JhKDEwMiwxMjYsMjM0LDAuMDgpKTtcclxufVxyXG5cclxuLm5hdi1pdGVtOmhvdmVyIHtcclxuICBiYWNrZ3JvdW5kOiByZ2JhKDEwMiwgMTI2LCAyMzQsIDAuMTApO1xyXG4gIGNvbG9yOiAjZmZmO1xyXG4gIHRyYW5zZm9ybTogc2NhbGUoMS4wNDUpO1xyXG4gIGJveC1zaGFkb3c6IDAgMnB4IDEycHggcmdiYSgxMDIsMTI2LDIzNCwwLjA4KTtcclxufVxyXG5cclxuLm5hdi1pdGVtLmFjdGl2ZSB7XHJcbiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgIzY2N2VlYSAwJSwgIzc2NGJhMiAxMDAlKTtcclxuICBjb2xvcjogI2ZmZjtcclxuICBib3JkZXItcmFkaXVzOiAxMnB4O1xyXG4gIG1hcmdpbi1yaWdodDogMDtcclxuICBib3gtc2hhZG93OiAwIDRweCAyNHB4IHJnYmEoMTAyLDEyNiwyMzQsMC4xOCk7XHJcbn1cclxuXHJcbi5uYXYtaXRlbS5hY3RpdmU6OmJlZm9yZSB7XHJcbiAgY29udGVudDogJyc7XHJcbiAgcG9zaXRpb246IGFic29sdXRlO1xyXG4gIGxlZnQ6IDA7XHJcbiAgdG9wOiA4cHg7XHJcbiAgYm90dG9tOiA4cHg7XHJcbiAgd2lkdGg6IDZweDtcclxuICBib3JkZXItcmFkaXVzOiA2cHg7XHJcbiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDE4MGRlZywgI2ZmZDkzZCAwJSwgIzY2N2VlYSAxMDAlKTtcclxuICBib3gtc2hhZG93OiAwIDAgMTJweCAycHggI2ZmZDkzZDY2O1xyXG59XHJcblxyXG4ucHJvZmlsZS1waWMtdGFiIHtcclxuICBtYXJnaW4tYm90dG9tOiAxOHB4ICFpbXBvcnRhbnQ7XHJcbiAgbWFyZ2luLWxlZnQ6IDAgIWltcG9ydGFudDtcclxuICBwYWRkaW5nLWxlZnQ6IDI0cHggIWltcG9ydGFudDtcclxuICBwYWRkaW5nLXJpZ2h0OiAyNHB4ICFpbXBvcnRhbnQ7XHJcbiAgcGFkZGluZy10b3A6IDhweCAhaW1wb3J0YW50O1xyXG4gIHBhZGRpbmctYm90dG9tOiA4cHggIWltcG9ydGFudDtcclxuICBiYWNrZ3JvdW5kOiByZ2JhKDI1NSwyNTUsMjU1LDAuMDcpO1xyXG4gIGJvcmRlci1yYWRpdXM6IDE2cHg7XHJcbiAgYm94LXNoYWRvdzogMCAycHggMTJweCByZ2JhKDEwMiwxMjYsMjM0LDAuMTApO1xyXG4gIGJvcmRlcjogMS41cHggc29saWQgcmdiYSgxMDIsMTI2LDIzNCwwLjEwKTtcclxuICBkaXNwbGF5OiBmbGV4O1xyXG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XHJcbiAganVzdGlmeS1jb250ZW50OiBmbGV4LXN0YXJ0O1xyXG59XHJcbi5wcm9maWxlLXBpYy10YWIgaW1nIHtcclxuICB3aWR0aDogNTZweDtcclxuICBoZWlnaHQ6IDU2cHg7XHJcbiAgYm9yZGVyLXJhZGl1czogNTAlO1xyXG4gIG9iamVjdC1maXQ6IGNvdmVyO1xyXG4gIGJvcmRlcjogMi41cHggc29saWQgIzY2N2VlYTtcclxuICBib3gtc2hhZG93OiAwIDJweCAxMnB4IHJnYmEoMTAyLDEyNiwyMzQsMC4xMCk7XHJcbn1cclxuXHJcbi8qIFhQL0xldmVsIFN5c3RlbSBTdHlsZXMgKi9cclxuLnhwLWxldmVsLWJveCB7XHJcbiAgbWFyZ2luLXRvcDogNHB4O1xyXG4gIG1hcmdpbi1ib3R0b206IDJweDtcclxuICB3aWR0aDogMTAwJTtcclxuICB0ZXh0LWFsaWduOiBjZW50ZXI7XHJcbn1cclxuLnhwLWxldmVsLWxhYmVsIHtcclxuICBmb250LXdlaWdodDogNzAwO1xyXG4gIGZvbnQtc2l6ZTogMTNweDtcclxuICBjb2xvcjogI2ZmZDkzZDtcclxuICBsZXR0ZXItc3BhY2luZzogMC4wNGVtO1xyXG4gIG1hcmdpbi1ib3R0b206IDJweDtcclxufVxyXG4ueHAtYmFyLWJnIHtcclxuICB3aWR0aDogODAlO1xyXG4gIGhlaWdodDogOHB4O1xyXG4gIGJhY2tncm91bmQ6IHJnYmEoMTAyLDEyNiwyMzQsMC4xMyk7XHJcbiAgYm9yZGVyLXJhZGl1czogOHB4O1xyXG4gIG1hcmdpbjogMCBhdXRvO1xyXG4gIHBvc2l0aW9uOiByZWxhdGl2ZTtcclxuICBvdmVyZmxvdzogaGlkZGVuO1xyXG59XHJcbi54cC1iYXItZmlsbCB7XHJcbiAgaGVpZ2h0OiAxMDAlO1xyXG4gIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCg5MGRlZywgI2ZmZDkzZCAwJSwgIzY2N2VlYSAxMDAlKTtcclxuICBib3JkZXItcmFkaXVzOiA4cHg7XHJcbiAgdHJhbnNpdGlvbjogd2lkdGggMC41cyBjdWJpYy1iZXppZXIoMC40LDAsMC4yLDEpO1xyXG59XHJcbi54cC1sYWJlbCB7XHJcbiAgZm9udC1zaXplOiAxMXB4O1xyXG4gIGNvbG9yOiAjYmZjN2Q1O1xyXG4gIG1hcmdpbi10b3A6IDJweDtcclxufVxyXG4uYXBwLmRhcmstbW9kZSAueHAtYmFyLWJnIHtcclxuICBiYWNrZ3JvdW5kOiByZ2JhKDI1NSwyNTUsMjU1LDAuMDgpO1xyXG59XHJcbi5hcHAuZGFyay1tb2RlIC54cC1sYWJlbCB7XHJcbiAgY29sb3I6ICNmZmQ5M2Q7XHJcbn1cclxuXHJcbi8qIC0tLSBEYXJrIE1vZGUgU2lkZWJhciAtLS0gKi9cclxuLmFwcC5kYXJrLW1vZGUgLm5hdmlnYXRpb24ge1xyXG4gIGJhY2tncm91bmQ6IHJnYmEoMzUsIDM5LCA0MywgMC45Mik7XHJcbiAgYm94LXNoYWRvdzogMCA4cHggMzJweCByZ2JhKDQwLCA0NCwgNTIsIDAuMjgpLCAycHggMCAyNHB4IHJnYmEoMTAyLCAxMjYsIDIzNCwgMC4xMik7XHJcbiAgYm9yZGVyOiAxLjVweCBzb2xpZCByZ2JhKDEwMiwgMTI2LCAyMzQsIDAuMTMpO1xyXG59XHJcbi5hcHAuZGFyay1tb2RlIC5uYXYtaGVhZGVyIGgyIHtcclxuICBjb2xvcjogI2ZmZDkzZDtcclxuICB0ZXh0LXNoYWRvdzogMCAycHggOHB4ICMyMzI3MmI7XHJcbn1cclxuLmFwcC5kYXJrLW1vZGUgLm5hdi1pdGVtIHtcclxuICBjb2xvcjogI2JmYzdkNTtcclxufVxyXG4uYXBwLmRhcmstbW9kZSAubmF2LWl0ZW0uYWN0aXZlIHtcclxuICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCAjMjMyNzJiIDAlLCAjNjY3ZWVhIDEwMCUpO1xyXG4gIGNvbG9yOiAjZmZkOTNkO1xyXG4gIGJveC1zaGFkb3c6IDAgNHB4IDI0cHggIzIzMjcyYjk5O1xyXG59XHJcbi5hcHAuZGFyay1tb2RlIC5uYXYtaXRlbS5hY3RpdmU6OmJlZm9yZSB7XHJcbiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDE4MGRlZywgI2ZmZDkzZCAwJSwgIzY2N2VlYSAxMDAlKTtcclxuICBib3gtc2hhZG93OiAwIDAgMTJweCAycHggI2ZmZDkzZDk5O1xyXG59XHJcbi5hcHAuZGFyay1tb2RlIC5wcm9maWxlLXBpYy10YWIge1xyXG4gIGJhY2tncm91bmQ6IHJnYmEoMjU1LDI1NSwyNTUsMC4wNCk7XHJcbiAgYm9yZGVyOiAxLjVweCBzb2xpZCAjMjMyNzJiO1xyXG59XHJcbi5hcHAuZGFyay1tb2RlIC5wcm9maWxlLXBpYy10YWIgaW1nIHtcclxuICBib3JkZXI6IDIuNXB4IHNvbGlkICNmZmQ5M2Q7XHJcbn1cclxuXHJcbi8qIC0tLSBSZXNwb25zaXZlIFNpZGViYXIgLS0tICovXHJcbkBtZWRpYSAobWF4LXdpZHRoOiA5MDBweCkge1xyXG4gIC5uYXZpZ2F0aW9uIHtcclxuICAgIHdpZHRoOiA2NHB4O1xyXG4gICAgbWluLXdpZHRoOiA2NHB4O1xyXG4gICAgcGFkZGluZzogMTZweCAwIDE2cHggMDtcclxuICAgIGJvcmRlci1yYWRpdXM6IDE2cHg7XHJcbiAgICBsZWZ0OiA4cHg7XHJcbiAgfVxyXG4gIC5uYXYtaGVhZGVyIHtcclxuICAgIHBhZGRpbmc6IDAgOHB4IDEycHg7XHJcbiAgICBtYXJnaW4tYm90dG9tOiAxMnB4O1xyXG4gIH1cclxuICAubmF2LWhlYWRlciBoMiB7XHJcbiAgICBmb250LXNpemU6IDA7XHJcbiAgfVxyXG4gIC5uYXYtaXRlbXMge1xyXG4gICAgZ2FwOiAycHg7XHJcbiAgfVxyXG4gIC5uYXYtaXRlbSB7XHJcbiAgICBwYWRkaW5nOiAxMHB4IDEwcHggMTBweCAxMHB4O1xyXG4gICAgZ2FwOiAwO1xyXG4gICAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7XHJcbiAgICBmb250LXNpemU6IDA7XHJcbiAgfVxyXG4gIC5uYXYtaXRlbSBzcGFuIHtcclxuICAgIGRpc3BsYXk6IG5vbmU7XHJcbiAgfVxyXG4gIC5wcm9maWxlLXBpYy10YWIge1xyXG4gICAgcGFkZGluZy1sZWZ0OiA0cHggIWltcG9ydGFudDtcclxuICAgIHBhZGRpbmctcmlnaHQ6IDRweCAhaW1wb3J0YW50O1xyXG4gICAgcGFkZGluZy10b3A6IDRweCAhaW1wb3J0YW50O1xyXG4gICAgcGFkZGluZy1ib3R0b206IDRweCAhaW1wb3J0YW50O1xyXG4gICAgbWFyZ2luLWJvdHRvbTogOHB4ICFpbXBvcnRhbnQ7XHJcbiAgfVxyXG4gIC5wcm9maWxlLXBpYy10YWIgaW1nIHtcclxuICAgIHdpZHRoOiA0MHB4O1xyXG4gICAgaGVpZ2h0OiA0MHB4O1xyXG4gIH1cclxufVxyXG5cclxuLyogLS0tIEVuZCBNb2Rlcm4gU2lkZWJhciAtLS0gKi9cclxuXHJcbi5tYWluLWNvbnRlbnQge1xyXG4gIGZsZXg6IDE7XHJcbiAgbWFyZ2luLWxlZnQ6IDI4MHB4O1xyXG4gIHBhZGRpbmc6IDI0cHg7XHJcbiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgIzY2N2VlYSAwJSwgIzc2NGJhMiAxMDAlKTtcclxuICBtaW4taGVpZ2h0OiAxMDB2aDtcclxufVxyXG5cclxuLmFwcC5kYXJrLW1vZGUge1xyXG4gIGJhY2tncm91bmQ6ICMxODFhMWI7XHJcbn1cclxuLmFwcC5kYXJrLW1vZGUgLm1haW4tY29udGVudCB7XHJcbiAgYmFja2dyb3VuZDogIzE4MWExYjtcclxuICBjb2xvcjogI2YxZjFmMTtcclxufVxyXG4uYXBwLmRhcmstbW9kZSAuY2FyZCB7XHJcbiAgYmFja2dyb3VuZDogIzIzMjcyYjtcclxuICBjb2xvcjogI2YxZjFmMTtcclxuICBib3gtc2hhZG93OiAwIDRweCAyNHB4IHJnYmEoMCwwLDAsMC43KTtcclxufVxyXG4uYXBwLmRhcmstbW9kZSAuYnRuIHtcclxuICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCAjMjMyNzJiIDAlLCAjMTgxYTFiIDEwMCUpO1xyXG4gIGNvbG9yOiAjZmZmO1xyXG59XHJcbi5hcHAuZGFyay1tb2RlIC5pbnB1dCB7XHJcbiAgYmFja2dyb3VuZDogIzIzMjcyYjtcclxuICBjb2xvcjogI2ZmZjtcclxuICBib3JkZXItY29sb3I6ICM0NDQ7XHJcbn1cclxuLmFwcC5kYXJrLW1vZGUgLnRleHQtZ3JheSB7XHJcbiAgY29sb3I6ICNhYWE7XHJcbn1cclxuLmFwcC5kYXJrLW1vZGUgLm5hdmlnYXRpb24ge1xyXG4gIGJhY2tncm91bmQ6ICMyMzI3MmI7XHJcbiAgYm94LXNoYWRvdzogMnB4IDAgMTBweCByZ2JhKDAsMCwwLDAuNyk7XHJcbn1cclxuLmFwcC5kYXJrLW1vZGUgLm5hdi1oZWFkZXIgaDIge1xyXG4gIGNvbG9yOiAjZjFmMWYxO1xyXG59XHJcbi5hcHAuZGFyay1tb2RlIC5uYXYtaXRlbSB7XHJcbiAgY29sb3I6ICNhYWE7XHJcbn1cclxuLmFwcC5kYXJrLW1vZGUgLm5hdi1pdGVtLmFjdGl2ZSB7XHJcbiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgIzMzMyAwJSwgIzIzMjcyYiAxMDAlKTtcclxuICBjb2xvcjogI2ZmZjtcclxufVxyXG5cclxuLyogU3dpdGNoIGZvciBkYXJrIG1vZGUgKi9cclxuLnN3aXRjaCB7XHJcbiAgcG9zaXRpb246IHJlbGF0aXZlO1xyXG4gIGRpc3BsYXk6IGlubGluZS1ibG9jaztcclxuICB3aWR0aDogNDBweDtcclxuICBoZWlnaHQ6IDIycHg7XHJcbn1cclxuLnN3aXRjaCBpbnB1dCB7IGRpc3BsYXk6IG5vbmU7IH1cclxuLnNsaWRlciB7XHJcbiAgcG9zaXRpb246IGFic29sdXRlO1xyXG4gIGN1cnNvcjogcG9pbnRlcjtcclxuICB0b3A6IDA7IGxlZnQ6IDA7IHJpZ2h0OiAwOyBib3R0b206IDA7XHJcbiAgYmFja2dyb3VuZC1jb2xvcjogI2NjYztcclxuICB0cmFuc2l0aW9uOiAuNHM7XHJcbiAgYm9yZGVyLXJhZGl1czogMjJweDtcclxufVxyXG4uc2xpZGVyOmJlZm9yZSB7XHJcbiAgcG9zaXRpb246IGFic29sdXRlO1xyXG4gIGNvbnRlbnQ6IFwiXCI7XHJcbiAgaGVpZ2h0OiAxNnB4O1xyXG4gIHdpZHRoOiAxNnB4O1xyXG4gIGxlZnQ6IDNweDtcclxuICBib3R0b206IDNweDtcclxuICBiYWNrZ3JvdW5kLWNvbG9yOiB3aGl0ZTtcclxuICB0cmFuc2l0aW9uOiAuNHM7XHJcbiAgYm9yZGVyLXJhZGl1czogNTAlO1xyXG59XHJcbmlucHV0OmNoZWNrZWQgKyAuc2xpZGVyIHtcclxuICBiYWNrZ3JvdW5kLWNvbG9yOiAjNjY3ZWVhO1xyXG59XHJcbmlucHV0OmNoZWNrZWQgKyAuc2xpZGVyOmJlZm9yZSB7XHJcbiAgdHJhbnNmb3JtOiB0cmFuc2xhdGVYKDE4cHgpO1xyXG59XHJcblxyXG4uc2V0dGluZ3MtYnRuIHtcclxuICBwb3NpdGlvbjogYWJzb2x1dGU7XHJcbiAgdG9wOiAyNHB4O1xyXG4gIHJpZ2h0OiAzMnB4O1xyXG4gIGJhY2tncm91bmQ6ICNmZmY7XHJcbiAgYm9yZGVyOiAycHggc29saWQgIzY2N2VlYTtcclxuICBib3JkZXItcmFkaXVzOiA1MCU7XHJcbiAgcGFkZGluZzogMTBweDtcclxuICBib3gtc2hhZG93OiAwIDJweCA4cHggcmdiYSgxMDIsIDEyNiwgMjM0LCAwLjE1KTtcclxuICB0cmFuc2l0aW9uOiBiYWNrZ3JvdW5kIDAuMnMsIGJvcmRlci1jb2xvciAwLjJzLCBib3gtc2hhZG93IDAuMnM7XHJcbiAgei1pbmRleDogMTAwO1xyXG59XHJcbi5zZXR0aW5ncy1idG46aG92ZXIge1xyXG4gIGJhY2tncm91bmQ6ICM2NjdlZWE7XHJcbiAgYm9yZGVyLWNvbG9yOiAjNzY0YmEyO1xyXG4gIGJveC1zaGFkb3c6IDAgNHB4IDE2cHggcmdiYSgxMDIsIDEyNiwgMjM0LCAwLjI1KTtcclxufVxyXG4uc2V0dGluZ3MtYnRuIHN2ZyB7XHJcbiAgY29sb3I6ICM2NjdlZWE7XHJcbiAgd2lkdGg6IDMycHg7XHJcbiAgaGVpZ2h0OiAzMnB4O1xyXG4gIHRyYW5zaXRpb246IGNvbG9yIDAuMnM7XHJcbn1cclxuLnNldHRpbmdzLWJ0bjpob3ZlciBzdmcge1xyXG4gIGNvbG9yOiAjZmZmO1xyXG59XHJcbi5hcHAuZGFyay1tb2RlIC5zZXR0aW5ncy1idG4ge1xyXG4gIGJhY2tncm91bmQ6ICMyMzI3MmI7XHJcbiAgYm9yZGVyOiAycHggc29saWQgIzY2N2VlYTtcclxuICBib3gtc2hhZG93OiAwIDAgMCA2cHggcmdiYSgxMDIsMTI2LDIzNCwwLjI1KSwgMCAwIDI0cHggOHB4ICM2NjdlZWE0NDtcclxufVxyXG4uYXBwLmRhcmstbW9kZSAuc2V0dGluZ3MtYnRuOmhvdmVyIHtcclxuICBiYWNrZ3JvdW5kOiAjNjY3ZWVhO1xyXG4gIGJvcmRlci1jb2xvcjogI2ZmZjtcclxuICBib3gtc2hhZG93OiAwIDAgMCA4cHggIzY2N2VlYTg4LCAwIDAgMzJweCAxMnB4ICM2NjdlZWE2NjtcclxufVxyXG4uYXBwLmRhcmstbW9kZSAuc2V0dGluZ3MtYnRuIHN2ZyB7XHJcbiAgY29sb3I6ICNmZmY7XHJcbn1cclxuXHJcbi5zZXR0aW5ncy1idG4uc2V0dGluZ3MtYnViYmxlIHtcclxuICBwb3NpdGlvbjogYWJzb2x1dGU7XHJcbiAgdG9wOiAyMHB4O1xyXG4gIHJpZ2h0OiAyNHB4O1xyXG4gIGJhY2tncm91bmQ6ICNmZmY7XHJcbiAgYm9yZGVyOiAycHggc29saWQgIzY2N2VlYTtcclxuICBib3JkZXItcmFkaXVzOiA1MCU7XHJcbiAgcGFkZGluZzogNnB4O1xyXG4gIGJveC1zaGFkb3c6IDAgMCAwIDdweCByZ2JhKDEwMiwxMjYsMjM0LDAuMTgpLCAwIDAgMjRweCAxMHB4ICM2NjdlZWEzMztcclxuICB0cmFuc2l0aW9uOiBiYWNrZ3JvdW5kIDAuMnMsIGJvcmRlci1jb2xvciAwLjJzLCBib3gtc2hhZG93IDAuMnM7XHJcbiAgei1pbmRleDogMTAwO1xyXG59XHJcbi5zZXR0aW5ncy1idG4uc2V0dGluZ3MtYnViYmxlOmhvdmVyIHtcclxuICBiYWNrZ3JvdW5kOiAjNjY3ZWVhO1xyXG4gIGJvcmRlci1jb2xvcjogIzc2NGJhMjtcclxuICBib3gtc2hhZG93OiAwIDAgMCAxMnB4ICM2NjdlZWE0NCwgMCAwIDMycHggMTRweCAjNjY3ZWVhNzc7XHJcbn1cclxuLnNldHRpbmdzLWJ0bi5zZXR0aW5ncy1idWJibGUgc3ZnIHtcclxuICBjb2xvcjogIzIyMjtcclxuICB3aWR0aDogMjJweDtcclxuICBoZWlnaHQ6IDIycHg7XHJcbiAgdHJhbnNpdGlvbjogY29sb3IgMC4ycztcclxufVxyXG4uc2V0dGluZ3MtYnRuLnNldHRpbmdzLWJ1YmJsZTpob3ZlciBzdmcge1xyXG4gIGNvbG9yOiAjZmZmO1xyXG59XHJcbi5hcHAuZGFyay1tb2RlIC5zZXR0aW5ncy1idG4uc2V0dGluZ3MtYnViYmxlIHtcclxuICBiYWNrZ3JvdW5kOiAjMjMyNzJiO1xyXG4gIGJvcmRlcjogMnB4IHNvbGlkICM2NjdlZWE7XHJcbiAgYm94LXNoYWRvdzogMCAwIDAgMTBweCByZ2JhKDEwMiwxMjYsMjM0LDAuMjgpLCAwIDAgMzJweCAxMnB4ICM2NjdlZWE1NTtcclxufVxyXG4uYXBwLmRhcmstbW9kZSAuc2V0dGluZ3MtYnRuLnNldHRpbmdzLWJ1YmJsZTpob3ZlciB7XHJcbiAgYmFja2dyb3VuZDogIzY2N2VlYTtcclxuICBib3JkZXItY29sb3I6ICNmZmY7XHJcbiAgYm94LXNoYWRvdzogMCAwIDAgMTZweCAjNjY3ZWVhNzcsIDAgMCA0OHB4IDIwcHggIzY2N2VlYTk5O1xyXG59XHJcbi5hcHAuZGFyay1tb2RlIC5zZXR0aW5ncy1idG4uc2V0dGluZ3MtYnViYmxlIHN2ZyB7XHJcbiAgY29sb3I6ICNmZmY7XHJcbn1cclxuXHJcbi8qIEdyaWQgbGF5b3V0cyBmb3IgbmV3IGNvbXBvbmVudHMgKi9cclxuLmdyaWQtMyB7XHJcbiAgZGlzcGxheTogZ3JpZDtcclxuICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IHJlcGVhdCgzLCAxZnIpO1xyXG4gIGdhcDogMXJlbTtcclxufVxyXG5cclxuLmdyaWQtNSB7XHJcbiAgZGlzcGxheTogZ3JpZDtcclxuICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IHJlcGVhdCg1LCAxZnIpO1xyXG4gIGdhcDogMC41cmVtO1xyXG59XHJcblxyXG4vKiBNb29kIHRyYWNrZXIgc3R5bGVzICovXHJcbi5tb29kLW9wdGlvbiB7XHJcbiAgdHJhbnNpdGlvbjogdHJhbnNmb3JtIDAuMnMgZWFzZTtcclxufVxyXG5cclxuLm1vb2Qtb3B0aW9uOmhvdmVyIHtcclxuICB0cmFuc2Zvcm06IHNjYWxlKDEuMDUpO1xyXG59XHJcblxyXG4vKiBQb21vZG9ybyB0aW1lciBzdHlsZXMgKi9cclxuLnBvbW9kb3JvLWNpcmNsZSB7XHJcbiAgdHJhbnNpdGlvbjogc3Ryb2tlLWRhc2hvZmZzZXQgMXMgbGluZWFyO1xyXG59XHJcblxyXG4vKiBRdWljayBub3RlcyBzdHlsZXMgKi9cclxuLm5vdGUtY2FyZCB7XHJcbiAgdHJhbnNpdGlvbjogYWxsIDAuM3MgZWFzZTtcclxufVxyXG5cclxuLm5vdGUtY2FyZDpob3ZlciB7XHJcbiAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKC0ycHgpO1xyXG4gIGJveC1zaGFkb3c6IDAgNHB4IDEycHggcmdiYSgwLCAwLCAwLCAwLjE1KTtcclxufVxyXG5cclxuLyogUmVzcG9uc2l2ZSBhZGp1c3RtZW50cyAqL1xyXG5AbWVkaWEgKG1heC13aWR0aDogNzY4cHgpIHtcclxuICAuZ3JpZC0zIHtcclxuICAgIGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KDIsIDFmcik7XHJcbiAgfVxyXG4gIFxyXG4gIC5ncmlkLTUge1xyXG4gICAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiByZXBlYXQoMywgMWZyKTtcclxuICB9XHJcblxyXG4gIC5zZXR0aW5ncy1ncmlkIHtcclxuICAgIGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyO1xyXG4gICAgZ2FwOiAyNHB4O1xyXG4gIH1cclxuXHJcbiAgLndpZGdldC1jb250cm9scyB7XHJcbiAgICBwYWRkaW5nOiAxMnB4IDE2cHg7XHJcbiAgfVxyXG5cclxuICAud2lkZ2V0LXRpdGxlIHtcclxuICAgIGZvbnQtc2l6ZTogMTRweDtcclxuICAgIG1hcmdpbjogMCAxMnB4O1xyXG4gIH1cclxuXHJcbiAgLmN1c3RvbWl6ZS1idG4ge1xyXG4gICAgcGFkZGluZzogMTBweCAxNnB4O1xyXG4gICAgZm9udC1zaXplOiAxM3B4O1xyXG4gIH1cclxuXHJcbiAgLmVtcHR5LXN0YXRlIHtcclxuICAgIHBhZGRpbmc6IDYwcHggMjBweDtcclxuICB9XHJcblxyXG4gIC5lbXB0eS10aXRsZSB7XHJcbiAgICBmb250LXNpemU6IDIwcHg7XHJcbiAgfVxyXG5cclxuICAuZW1wdHktZGVzY3JpcHRpb24ge1xyXG4gICAgZm9udC1zaXplOiAxNHB4O1xyXG4gIH1cclxufVxyXG5cclxuQG1lZGlhIChtYXgtd2lkdGg6IDQ4MHB4KSB7XHJcbiAgLmdyaWQtMyB7XHJcbiAgICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IDFmcjtcclxuICB9XHJcbiAgXHJcbiAgLmdyaWQtNSB7XHJcbiAgICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IHJlcGVhdCgyLCAxZnIpO1xyXG4gIH1cclxufVxyXG5cclxuLyogQW5pbWF0aW9uIGZvciBwcm9ncmVzcyBiYXJzICovXHJcbkBrZXlmcmFtZXMgcHJvZ3Jlc3Mge1xyXG4gIGZyb20geyB3aWR0aDogMCU7IH1cclxuICB0byB7IHdpZHRoOiB2YXIoLS1wcm9ncmVzcyk7IH1cclxufVxyXG5cclxuLnByb2dyZXNzLWJhciB7XHJcbiAgYW5pbWF0aW9uOiBwcm9ncmVzcyAxcyBlYXNlLW91dDtcclxufVxyXG5cclxuLyogSG92ZXIgZWZmZWN0cyBmb3IgaW50ZXJhY3RpdmUgZWxlbWVudHMgKi9cclxuLmludGVyYWN0aXZlOmhvdmVyIHtcclxuICB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoLTFweCk7XHJcbiAgYm94LXNoYWRvdzogMCAycHggOHB4IHJnYmEoMCwgMCwgMCwgMC4xKTtcclxufVxyXG5cclxuLyogRGFyayBtb2RlIHNwZWNpZmljIHN0eWxlcyAqL1xyXG4uZGFyay1tb2RlIC5tb29kLW9wdGlvbiB7XHJcbiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjEpO1xyXG4gIGJvcmRlci1jb2xvcjogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjIpO1xyXG59XHJcblxyXG4uZGFyay1tb2RlIC5ub3RlLWNhcmQge1xyXG4gIGJhY2tncm91bmQ6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4wNSk7XHJcbiAgYm9yZGVyLWNvbG9yOiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMSk7XHJcbn1cclxuXHJcbi8qIERhc2hib2FyZCBXaWRnZXQgU3R5bGVzICovXHJcbi53aWRnZXQtY29udGFpbmVyIHtcclxuICBiYWNrZ3JvdW5kOiB0cmFuc3BhcmVudDtcclxuICBib3JkZXItcmFkaXVzOiAxNnB4O1xyXG4gIG92ZXJmbG93OiBoaWRkZW47XHJcbiAgYm94LXNoYWRvdzogbm9uZTtcclxuICBib3JkZXI6IG5vbmU7XHJcbiAgdHJhbnNpdGlvbjogYWxsIDAuM3MgY3ViaWMtYmV6aWVyKDAuNCwgMCwgMC4yLCAxKTtcclxufVxyXG5cclxuLndpZGdldC1jb250YWluZXIuY3VzdG9taXppbmcge1xyXG4gIGJhY2tncm91bmQ6IHdoaXRlO1xyXG4gIGJveC1zaGFkb3c6IDAgNHB4IDIwcHggcmdiYSgwLCAwLCAwLCAwLjA4KTtcclxuICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDAsIDAsIDAsIDAuMDUpO1xyXG59XHJcblxyXG4ud2lkZ2V0LWNvbnRhaW5lcjpob3ZlciB7XHJcbiAgYm94LXNoYWRvdzogMCA4cHggMzJweCByZ2JhKDAsIDAsIDAsIDAuMTIpO1xyXG4gIHRyYW5zZm9ybTogdHJhbnNsYXRlWSgtNHB4KTtcclxufVxyXG5cclxuLndpZGdldC1jb250YWluZXIuZHJhZ2dpbmcge1xyXG4gIG9wYWNpdHk6IDAuNztcclxuICB0cmFuc2Zvcm06IHJvdGF0ZSgxZGVnKSBzY2FsZSgxLjAyKTtcclxuICBib3gtc2hhZG93OiAwIDEycHggNDBweCByZ2JhKDAsIDAsIDAsIDAuMTUpO1xyXG4gIHotaW5kZXg6IDEwMDA7XHJcbn1cclxuXHJcbi53aWRnZXQtaGVhZGVyIHtcclxuICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCAjNjY3ZWVhIDAlLCAjNzY0YmEyIDEwMCUpO1xyXG4gIHBhZGRpbmc6IDA7XHJcbiAgcG9zaXRpb246IHJlbGF0aXZlO1xyXG59XHJcblxyXG4ud2lkZ2V0LWNvbnRyb2xzIHtcclxuICBkaXNwbGF5OiBmbGV4O1xyXG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XHJcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xyXG4gIHBhZGRpbmc6IDE2cHggMjBweDtcclxuICBjb2xvcjogd2hpdGU7XHJcbn1cclxuXHJcbi5kcmFnLWhhbmRsZSB7XHJcbiAgZGlzcGxheTogZmxleDtcclxuICBhbGlnbi1pdGVtczogY2VudGVyO1xyXG4gIGN1cnNvcjogZ3JhYjtcclxuICBwYWRkaW5nOiA0cHg7XHJcbiAgYm9yZGVyLXJhZGl1czogNnB4O1xyXG4gIHRyYW5zaXRpb246IGFsbCAwLjJzIGVhc2U7XHJcbiAgb3BhY2l0eTogMC43O1xyXG59XHJcblxyXG4uZHJhZy1oYW5kbGU6aG92ZXIge1xyXG4gIG9wYWNpdHk6IDE7XHJcbiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjEpO1xyXG59XHJcblxyXG4uZHJhZy1oYW5kbGU6YWN0aXZlIHtcclxuICBjdXJzb3I6IGdyYWJiaW5nO1xyXG59XHJcblxyXG4uZ3JpcC1pY29uIHtcclxuICBjb2xvcjogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjkpO1xyXG4gIHRyYW5zaXRpb246IGNvbG9yIDAuMnMgZWFzZTtcclxufVxyXG5cclxuLmRyYWctaGFuZGxlOmhvdmVyIC5ncmlwLWljb24ge1xyXG4gIGNvbG9yOiB3aGl0ZTtcclxufVxyXG5cclxuLndpZGdldC10aXRsZSB7XHJcbiAgZm9udC13ZWlnaHQ6IDYwMDtcclxuICBmb250LXNpemU6IDE2cHg7XHJcbiAgbGV0dGVyLXNwYWNpbmc6IDAuMDI1ZW07XHJcbiAgZmxleDogMTtcclxuICB0ZXh0LWFsaWduOiBjZW50ZXI7XHJcbiAgbWFyZ2luOiAwIDE2cHg7XHJcbn1cclxuXHJcbi53aWRnZXQtYWN0aW9ucyB7XHJcbiAgZGlzcGxheTogZmxleDtcclxuICBhbGlnbi1pdGVtczogY2VudGVyO1xyXG59XHJcblxyXG4uaGlkZS1idG4ge1xyXG4gIGRpc3BsYXk6IGZsZXg7XHJcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcclxuICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjtcclxuICB3aWR0aDogMzJweDtcclxuICBoZWlnaHQ6IDMycHg7XHJcbiAgYm9yZGVyOiBub25lO1xyXG4gIGJhY2tncm91bmQ6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4xKTtcclxuICBib3JkZXItcmFkaXVzOiA4cHg7XHJcbiAgY29sb3I6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC44KTtcclxuICBjdXJzb3I6IHBvaW50ZXI7XHJcbiAgdHJhbnNpdGlvbjogYWxsIDAuMnMgZWFzZTtcclxuICBiYWNrZHJvcC1maWx0ZXI6IGJsdXIoMTBweCk7XHJcbn1cclxuXHJcbi5oaWRlLWJ0bjpob3ZlciB7XHJcbiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjIpO1xyXG4gIGNvbG9yOiB3aGl0ZTtcclxuICB0cmFuc2Zvcm06IHNjYWxlKDEuMDUpO1xyXG59XHJcblxyXG4ud2lkZ2V0LWNvbnRlbnQge1xyXG4gIGJhY2tncm91bmQ6IHdoaXRlO1xyXG4gIHBhZGRpbmc6IDA7XHJcbn1cclxuXHJcbi8qIERyYWcgYW5kIERyb3AgVmlzdWFsIEZlZWRiYWNrICovXHJcbi53aWRnZXQtY29udGFpbmVyW2RyYWdnYWJsZT1cInRydWVcIl0ge1xyXG4gIGN1cnNvcjogZ3JhYjtcclxufVxyXG5cclxuLndpZGdldC1jb250YWluZXJbZHJhZ2dhYmxlPVwidHJ1ZVwiXTphY3RpdmUge1xyXG4gIGN1cnNvcjogZ3JhYmJpbmc7XHJcbn1cclxuXHJcbi53aWRnZXRzLWNvbnRhaW5lciB7XHJcbiAgbWluLWhlaWdodDogMjAwcHg7XHJcbn1cclxuXHJcbi8qIFNldHRpbmdzIFBhbmVsIFN0eWxlcyAqL1xyXG4uc2V0dGluZ3MtcGFuZWwge1xyXG4gIGJhY2tncm91bmQ6IHdoaXRlO1xyXG4gIGJvcmRlci1yYWRpdXM6IDIwcHg7XHJcbiAgYm94LXNoYWRvdzogMCA4cHggMzJweCByZ2JhKDAsIDAsIDAsIDAuMSk7XHJcbiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSgwLCAwLCAwLCAwLjA1KTtcclxuICBvdmVyZmxvdzogaGlkZGVuO1xyXG59XHJcblxyXG4uc2V0dGluZ3MtaGVhZGVyIHtcclxuICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCAjNjY3ZWVhIDAlLCAjNzY0YmEyIDEwMCUpO1xyXG4gIHBhZGRpbmc6IDIwcHggMjRweDtcclxuICBkaXNwbGF5OiBmbGV4O1xyXG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XHJcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xyXG4gIGNvbG9yOiB3aGl0ZTtcclxufVxyXG5cclxuLnNldHRpbmdzLXRpdGxlIHtcclxuICBmb250LXNpemU6IDIwcHg7XHJcbiAgZm9udC13ZWlnaHQ6IDYwMDtcclxuICBtYXJnaW46IDA7XHJcbiAgbGV0dGVyLXNwYWNpbmc6IDAuMDI1ZW07XHJcbn1cclxuXHJcbi5jbG9zZS1zZXR0aW5ncy1idG4ge1xyXG4gIGJhY2tncm91bmQ6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4xKTtcclxuICBib3JkZXI6IG5vbmU7XHJcbiAgY29sb3I6IHdoaXRlO1xyXG4gIHdpZHRoOiAzMnB4O1xyXG4gIGhlaWdodDogMzJweDtcclxuICBib3JkZXItcmFkaXVzOiA4cHg7XHJcbiAgZm9udC1zaXplOiAxOHB4O1xyXG4gIGN1cnNvcjogcG9pbnRlcjtcclxuICB0cmFuc2l0aW9uOiBhbGwgMC4ycyBlYXNlO1xyXG4gIGJhY2tkcm9wLWZpbHRlcjogYmx1cigxMHB4KTtcclxufVxyXG5cclxuLmNsb3NlLXNldHRpbmdzLWJ0bjpob3ZlciB7XHJcbiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjIpO1xyXG4gIHRyYW5zZm9ybTogc2NhbGUoMS4wNSk7XHJcbn1cclxuXHJcbi5zZXR0aW5ncy1jb250ZW50IHtcclxuICBwYWRkaW5nOiAyNHB4O1xyXG59XHJcblxyXG4uc2V0dGluZ3MtZ3JpZCB7XHJcbiAgZGlzcGxheTogZ3JpZDtcclxuICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IDFmciAxZnI7XHJcbiAgZ2FwOiAzMnB4O1xyXG4gIG1hcmdpbi1ib3R0b206IDI0cHg7XHJcbn1cclxuXHJcbi5zZWN0aW9uLXRpdGxlIHtcclxuICBmb250LXNpemU6IDE2cHg7XHJcbiAgZm9udC13ZWlnaHQ6IDYwMDtcclxuICBjb2xvcjogIzMzMztcclxuICBtYXJnaW4tYm90dG9tOiAxNnB4O1xyXG4gIGxldHRlci1zcGFjaW5nOiAwLjAyNWVtO1xyXG59XHJcblxyXG4ud2lkZ2V0LWxpc3Qge1xyXG4gIGRpc3BsYXk6IGZsZXg7XHJcbiAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcclxuICBnYXA6IDEycHg7XHJcbn1cclxuXHJcbi53aWRnZXQtaXRlbSB7XHJcbiAgZGlzcGxheTogZmxleDtcclxuICBhbGlnbi1pdGVtczogY2VudGVyO1xyXG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcclxuICBwYWRkaW5nOiAxNnB4O1xyXG4gIGJhY2tncm91bmQ6ICNmOGY5ZmE7XHJcbiAgYm9yZGVyLXJhZGl1czogMTJweDtcclxuICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDAsIDAsIDAsIDAuMDUpO1xyXG4gIHRyYW5zaXRpb246IGFsbCAwLjJzIGVhc2U7XHJcbn1cclxuXHJcbi53aWRnZXQtaXRlbTpob3ZlciB7XHJcbiAgYmFja2dyb3VuZDogI2YxZjNmNDtcclxuICB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoLTFweCk7XHJcbn1cclxuXHJcbi53aWRnZXQtbmFtZSB7XHJcbiAgZm9udC13ZWlnaHQ6IDUwMDtcclxuICBjb2xvcjogIzMzMztcclxufVxyXG5cclxuLnZpc2liaWxpdHktdG9nZ2xlIHtcclxuICBkaXNwbGF5OiBmbGV4O1xyXG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XHJcbiAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7XHJcbiAgd2lkdGg6IDM2cHg7XHJcbiAgaGVpZ2h0OiAzNnB4O1xyXG4gIGJvcmRlcjogbm9uZTtcclxuICBib3JkZXItcmFkaXVzOiAxMHB4O1xyXG4gIGN1cnNvcjogcG9pbnRlcjtcclxuICB0cmFuc2l0aW9uOiBhbGwgMC4ycyBlYXNlO1xyXG4gIGZvbnQtd2VpZ2h0OiA1MDA7XHJcbn1cclxuXHJcbi52aXNpYmlsaXR5LXRvZ2dsZS5hY3RpdmUge1xyXG4gIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxMzVkZWcsICM0Q0FGNTAgMCUsICM0NWEwNDkgMTAwJSk7XHJcbiAgY29sb3I6IHdoaXRlO1xyXG4gIGJveC1zaGFkb3c6IDAgMnB4IDhweCByZ2JhKDc2LCAxNzUsIDgwLCAwLjMpO1xyXG59XHJcblxyXG4udmlzaWJpbGl0eS10b2dnbGUuaW5hY3RpdmUge1xyXG4gIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxMzVkZWcsICM2Yzc1N2QgMCUsICM1YTYyNjggMTAwJSk7XHJcbiAgY29sb3I6IHdoaXRlO1xyXG4gIGJveC1zaGFkb3c6IDAgMnB4IDhweCByZ2JhKDEwOCwgMTE3LCAxMjUsIDAuMyk7XHJcbn1cclxuXHJcbi52aXNpYmlsaXR5LXRvZ2dsZTpob3ZlciB7XHJcbiAgdHJhbnNmb3JtOiBzY2FsZSgxLjA1KTtcclxufVxyXG5cclxuLmluc3RydWN0aW9ucy1saXN0IHtcclxuICBkaXNwbGF5OiBmbGV4O1xyXG4gIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XHJcbiAgZ2FwOiAxNnB4O1xyXG59XHJcblxyXG4uaW5zdHJ1Y3Rpb24taXRlbSB7XHJcbiAgZGlzcGxheTogZmxleDtcclxuICBhbGlnbi1pdGVtczogZmxleC1zdGFydDtcclxuICBnYXA6IDE2cHg7XHJcbiAgcGFkZGluZzogMTZweDtcclxuICBiYWNrZ3JvdW5kOiAjZjhmOWZhO1xyXG4gIGJvcmRlci1yYWRpdXM6IDEycHg7XHJcbiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSgwLCAwLCAwLCAwLjA1KTtcclxuICB0cmFuc2l0aW9uOiBhbGwgMC4ycyBlYXNlO1xyXG59XHJcblxyXG4uaW5zdHJ1Y3Rpb24taXRlbTpob3ZlciB7XHJcbiAgYmFja2dyb3VuZDogI2YxZjNmNDtcclxuICB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoLTFweCk7XHJcbn1cclxuXHJcbi5pbnN0cnVjdGlvbi1pY29uIHtcclxuICBmb250LXNpemU6IDI0cHg7XHJcbiAgZmxleC1zaHJpbms6IDA7XHJcbn1cclxuXHJcbi5pbnN0cnVjdGlvbi1jb250ZW50IGg0IHtcclxuICBmb250LXdlaWdodDogNjAwO1xyXG4gIGNvbG9yOiAjMzMzO1xyXG4gIG1hcmdpbjogMCAwIDRweCAwO1xyXG4gIGZvbnQtc2l6ZTogMTRweDtcclxufVxyXG5cclxuLmluc3RydWN0aW9uLWNvbnRlbnQgcCB7XHJcbiAgY29sb3I6ICM2NjY7XHJcbiAgbWFyZ2luOiAwO1xyXG4gIGZvbnQtc2l6ZTogMTNweDtcclxuICBsaW5lLWhlaWdodDogMS40O1xyXG59XHJcblxyXG4uc2V0dGluZ3MtYWN0aW9ucyB7XHJcbiAgZGlzcGxheTogZmxleDtcclxuICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjtcclxuICBwYWRkaW5nLXRvcDogMTZweDtcclxuICBib3JkZXItdG9wOiAxcHggc29saWQgcmdiYSgwLCAwLCAwLCAwLjA1KTtcclxufVxyXG5cclxuLnJlc2V0LWJ0biB7XHJcbiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgI2ZmNmI2YiAwJSwgI2VlNWE1MiAxMDAlKTtcclxuICBjb2xvcjogd2hpdGU7XHJcbiAgYm9yZGVyOiBub25lO1xyXG4gIHBhZGRpbmc6IDEycHggMjRweDtcclxuICBib3JkZXItcmFkaXVzOiAxMnB4O1xyXG4gIGZvbnQtd2VpZ2h0OiA1MDA7XHJcbiAgY3Vyc29yOiBwb2ludGVyO1xyXG4gIHRyYW5zaXRpb246IGFsbCAwLjJzIGVhc2U7XHJcbiAgYm94LXNoYWRvdzogMCAycHggOHB4IHJnYmEoMjU1LCAxMDcsIDEwNywgMC4zKTtcclxufVxyXG5cclxuLnJlc2V0LWJ0bjpob3ZlciB7XHJcbiAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKC0ycHgpO1xyXG4gIGJveC1zaGFkb3c6IDAgNHB4IDE2cHggcmdiYSgyNTUsIDEwNywgMTA3LCAwLjQpO1xyXG59XHJcblxyXG4vKiBDdXN0b21pemUgQnV0dG9uICovXHJcbi5jdXN0b21pemUtYnRuIHtcclxuICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCAjNjY3ZWVhIDAlLCAjNzY0YmEyIDEwMCUpO1xyXG4gIGNvbG9yOiB3aGl0ZTtcclxuICBib3JkZXI6IG5vbmU7XHJcbiAgcGFkZGluZzogMTJweCAyMHB4O1xyXG4gIGJvcmRlci1yYWRpdXM6IDEycHg7XHJcbiAgZm9udC13ZWlnaHQ6IDUwMDtcclxuICBjdXJzb3I6IHBvaW50ZXI7XHJcbiAgdHJhbnNpdGlvbjogYWxsIDAuM3MgZWFzZTtcclxuICBib3gtc2hhZG93OiAwIDRweCAxNnB4IHJnYmEoMTAyLCAxMjYsIDIzNCwgMC4zKTtcclxuICBkaXNwbGF5OiBmbGV4O1xyXG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XHJcbiAgZ2FwOiA4cHg7XHJcbiAgZm9udC1zaXplOiAxNHB4O1xyXG4gIGxldHRlci1zcGFjaW5nOiAwLjAyNWVtO1xyXG59XHJcblxyXG4uY3VzdG9taXplLWJ0bjpob3ZlciB7XHJcbiAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKC0ycHgpO1xyXG4gIGJveC1zaGFkb3c6IDAgNnB4IDI0cHggcmdiYSgxMDIsIDEyNiwgMjM0LCAwLjQpO1xyXG59XHJcblxyXG4uY3VzdG9taXplLWJ0bi5hY3RpdmUge1xyXG4gIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxMzVkZWcsICNmZjZiNmIgMCUsICNlZTVhNTIgMTAwJSk7XHJcbiAgYm94LXNoYWRvdzogMCA0cHggMTZweCByZ2JhKDI1NSwgMTA3LCAxMDcsIDAuMyk7XHJcbn1cclxuXHJcbi5jdXN0b21pemUtYnRuLmFjdGl2ZTpob3ZlciB7XHJcbiAgYm94LXNoYWRvdzogMCA2cHggMjRweCByZ2JhKDI1NSwgMTA3LCAxMDcsIDAuNCk7XHJcbn1cclxuXHJcbi8qIEVtcHR5IFN0YXRlICovXHJcbi5lbXB0eS1zdGF0ZSB7XHJcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xyXG4gIHBhZGRpbmc6IDgwcHggMjRweDtcclxuICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCAjZjhmOWZhIDAlLCAjZTllY2VmIDEwMCUpO1xyXG4gIGJvcmRlci1yYWRpdXM6IDIwcHg7XHJcbiAgYm9yZGVyOiAycHggZGFzaGVkIHJnYmEoMTAyLCAxMjYsIDIzNCwgMC4yKTtcclxufVxyXG5cclxuLmVtcHR5LWljb24ge1xyXG4gIGNvbG9yOiAjNjY3ZWVhO1xyXG4gIG1hcmdpbi1ib3R0b206IDI0cHg7XHJcbiAgb3BhY2l0eTogMC43O1xyXG59XHJcblxyXG4uZW1wdHktdGl0bGUge1xyXG4gIGZvbnQtc2l6ZTogMjRweDtcclxuICBmb250LXdlaWdodDogNjAwO1xyXG4gIGNvbG9yOiAjMzMzO1xyXG4gIG1hcmdpbi1ib3R0b206IDEycHg7XHJcbiAgbGV0dGVyLXNwYWNpbmc6IDAuMDI1ZW07XHJcbn1cclxuXHJcbi5lbXB0eS1kZXNjcmlwdGlvbiB7XHJcbiAgY29sb3I6ICM2NjY7XHJcbiAgZm9udC1zaXplOiAxNnB4O1xyXG4gIGxpbmUtaGVpZ2h0OiAxLjU7XHJcbiAgbWFyZ2luLWJvdHRvbTogMzJweDtcclxuICBtYXgtd2lkdGg6IDQwMHB4O1xyXG4gIG1hcmdpbi1sZWZ0OiBhdXRvO1xyXG4gIG1hcmdpbi1yaWdodDogYXV0bztcclxufVxyXG5cclxuLmVtcHR5LWFjdGlvbi1idG4ge1xyXG4gIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxMzVkZWcsICM2NjdlZWEgMCUsICM3NjRiYTIgMTAwJSk7XHJcbiAgY29sb3I6IHdoaXRlO1xyXG4gIGJvcmRlcjogbm9uZTtcclxuICBwYWRkaW5nOiAxNnB4IDMycHg7XHJcbiAgYm9yZGVyLXJhZGl1czogMTZweDtcclxuICBmb250LXdlaWdodDogNjAwO1xyXG4gIGN1cnNvcjogcG9pbnRlcjtcclxuICB0cmFuc2l0aW9uOiBhbGwgMC4zcyBlYXNlO1xyXG4gIGJveC1zaGFkb3c6IDAgNHB4IDE2cHggcmdiYSgxMDIsIDEyNiwgMjM0LCAwLjMpO1xyXG4gIGRpc3BsYXk6IGlubGluZS1mbGV4O1xyXG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XHJcbiAgZ2FwOiAxMnB4O1xyXG4gIGZvbnQtc2l6ZTogMTZweDtcclxuICBsZXR0ZXItc3BhY2luZzogMC4wMjVlbTtcclxufVxyXG5cclxuLmVtcHR5LWFjdGlvbi1idG46aG92ZXIge1xyXG4gIHRyYW5zZm9ybTogdHJhbnNsYXRlWSgtM3B4KTtcclxuICBib3gtc2hhZG93OiAwIDhweCAzMnB4IHJnYmEoMTAyLCAxMjYsIDIzNCwgMC40KTtcclxufVxyXG5cclxuLyogRGFyayBNb2RlIFdpZGdldCBTdHlsZXMgKi9cclxuLmFwcC5kYXJrLW1vZGUgLndpZGdldC1jb250YWluZXIge1xyXG4gIGJhY2tncm91bmQ6IHRyYW5zcGFyZW50O1xyXG4gIGJveC1zaGFkb3c6IG5vbmU7XHJcbiAgYm9yZGVyOiBub25lO1xyXG59XHJcblxyXG4uYXBwLmRhcmstbW9kZSAud2lkZ2V0LWNvbnRhaW5lci5jdXN0b21pemluZyB7XHJcbiAgYmFja2dyb3VuZDogIzIzMjcyYjtcclxuICBib3gtc2hhZG93OiAwIDRweCAyMHB4IHJnYmEoMCwwLDAsMC4yNSk7XHJcbiAgYm9yZGVyOiAxcHggc29saWQgIzMzMztcclxufVxyXG5cclxuLmFwcC5kYXJrLW1vZGUgLndpZGdldC1oZWFkZXIge1xyXG4gIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxMzVkZWcsICMyYzMwMzQgMCUsICMyMzI3MmIgMTAwJSk7XHJcbiAgYm9yZGVyLWJvdHRvbTogMXB4IHNvbGlkICM0NDQ7XHJcbn1cclxuXHJcbi5hcHAuZGFyay1tb2RlIC53aWRnZXQtaGVhZGVyOmhvdmVyIHtcclxuICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCAjMjMyNzJiIDAlLCAjMWUyMTI0IDEwMCUpO1xyXG59XHJcblxyXG4uYXBwLmRhcmstbW9kZSAud2lkZ2V0LWNvbnRlbnQge1xyXG4gIGJhY2tncm91bmQ6ICMyMzI3MmI7XHJcbiAgY29sb3I6ICNmMWYxZjE7XHJcbn1cclxuXHJcbi5hcHAuZGFyay1tb2RlIC5zZXR0aW5ncy1wYW5lbCB7XHJcbiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgIzJjMzAzNCAwJSwgIzIzMjcyYiAxMDAlKTtcclxuICBib3JkZXI6IDFweCBzb2xpZCAjNDQ0O1xyXG59XHJcblxyXG4uYXBwLmRhcmstbW9kZSAud2lkZ2V0LXRvZ2dsZS5hY3RpdmUge1xyXG4gIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxMzVkZWcsICM0Q0FGNTAgMCUsICM0NWEwNDkgMTAwJSk7XHJcbn1cclxuXHJcbi5hcHAuZGFyay1tb2RlIC53aWRnZXQtdG9nZ2xlLmluYWN0aXZlIHtcclxuICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCAjNmM3NTdkIDAlLCAjNWE2MjY4IDEwMCUpO1xyXG59IFxyXG5cclxuLmN1c3RvbWl6ZS1yb3cge1xyXG4gIGRpc3BsYXk6IGZsZXg7XHJcbiAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7XHJcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcclxuICBtYXJnaW4tYm90dG9tOiAzMnB4O1xyXG59IFxyXG5cclxuLmRyYWctaGFuZGxlLCAuaGlkZS1idG4ge1xyXG4gIGRpc3BsYXk6IG5vbmU7XHJcbn1cclxuXHJcbi53aWRnZXQtY29udGFpbmVyLmN1c3RvbWl6aW5nIC5kcmFnLWhhbmRsZSxcclxuLndpZGdldC1jb250YWluZXIuY3VzdG9taXppbmcgLmhpZGUtYnRuIHtcclxuICBkaXNwbGF5OiBmbGV4O1xyXG59IFxyXG5cclxuLyogSGlkZSBzY3JvbGxiYXJzIGluIHNpZGViYXIgYW5kIG1haW4gY29udGVudCAqL1xyXG4ubmF2aWdhdGlvbiwgLm1haW4tY29udGVudCwgLmNvbnRhaW5lciB7XHJcbiAgc2Nyb2xsYmFyLXdpZHRoOiBub25lOyAvKiBGaXJlZm94ICovXHJcbiAgLW1zLW92ZXJmbG93LXN0eWxlOiBub25lOyAvKiBJRSAxMCsgKi9cclxufVxyXG4ubmF2aWdhdGlvbjo6LXdlYmtpdC1zY3JvbGxiYXIsXHJcbi5tYWluLWNvbnRlbnQ6Oi13ZWJraXQtc2Nyb2xsYmFyLFxyXG4uY29udGFpbmVyOjotd2Via2l0LXNjcm9sbGJhciB7XHJcbiAgZGlzcGxheTogbm9uZTsgLyogQ2hyb21lLCBTYWZhcmksIE9wZXJhICovXHJcbn0gXHJcblxyXG4vKiBDb25mZXR0aSBPdmVybGF5IFN0eWxlcyAqL1xyXG4uY29uZmV0dGktb3ZlcmxheSB7XHJcbiAgcG9zaXRpb246IGZpeGVkO1xyXG4gIHRvcDogMDsgbGVmdDogMDsgcmlnaHQ6IDA7IGJvdHRvbTogMDtcclxuICB3aWR0aDogMTAwdnc7IGhlaWdodDogMTAwdmg7XHJcbiAgei1pbmRleDogOTk5OTtcclxuICBwb2ludGVyLWV2ZW50czogbm9uZTtcclxuICBiYWNrZ3JvdW5kOiB0cmFuc3BhcmVudDtcclxuICBhbmltYXRpb246IGNvbmZldHRpLWZhZGVvdXQgMnMgZm9yd2FyZHM7XHJcbn1cclxuQGtleWZyYW1lcyBjb25mZXR0aS1mYWRlb3V0IHtcclxuICAwJSB7IG9wYWNpdHk6IDE7IH1cclxuICA4MCUgeyBvcGFjaXR5OiAxOyB9XHJcbiAgMTAwJSB7IG9wYWNpdHk6IDA7IH1cclxufVxyXG4uY29uZmV0dGktcGllY2Uge1xyXG4gIHBvc2l0aW9uOiBhYnNvbHV0ZTtcclxuICBib3JkZXItcmFkaXVzOiA0cHg7XHJcbiAgb3BhY2l0eTogMC44NTtcclxuICBib3gtc2hhZG93OiAwIDJweCA4cHggcmdiYSgwLDAsMCwwLjA4KTtcclxuICBhbmltYXRpb246IGNvbmZldHRpLWZhbGwgMS41cyBjdWJpYy1iZXppZXIoMC40LDAsMC4yLDEpIGZvcndhcmRzO1xyXG59XHJcbkBrZXlmcmFtZXMgY29uZmV0dGktZmFsbCB7XHJcbiAgMCUgeyB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoMCkgc2NhbGUoMSkgcm90YXRlKHZhcigtLWFuZ2xlLDBkZWcpKTsgb3BhY2l0eTogMTsgfVxyXG4gIDgwJSB7IG9wYWNpdHk6IDE7IH1cclxuICAxMDAlIHsgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKDYwdmgpIHNjYWxlKDAuOCkgcm90YXRlKHZhcigtLWFuZ2xlLDBkZWcpKTsgb3BhY2l0eTogMDsgfVxyXG59ICJdLCJzb3VyY2VSb290IjoiIn0= */</style><link id="orbitron-font" rel="stylesheet" href="./lifeion_files/css2(1)"></head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"><div class="app dark-mode" style="position: relative;"><nav class="navigation"><div class="nav-header" style="text-align: left; padding-left: 16px;"><h2 style="margin: 0px; font-weight: 700; font-size: 28px; letter-spacing: 0.08em; font-family: Orbitron, Montserrat, Poppins, Arial, sans-serif; background: linear-gradient(90deg, rgb(79, 195, 247) 0%, rgb(25, 118, 210) 100%) text; -webkit-text-fill-color: transparent; text-shadow: rgb(35, 39, 47) 0px 2px 16px; text-transform: uppercase;">lifeion</h2></div><div class="nav-items"><div class="nav-item profile-pic-tab" style="justify-content: flex-start; cursor: default; pointer-events: none; margin-bottom: 8px; margin-left: -16px; flex-direction: column; align-items: center;"><img src="data:image/jpeg;base64,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" alt="Profile" style="width: 56px; height: 56px; border-radius: 50%; object-fit: cover; border: 2px solid rgb(204, 204, 204); margin-bottom: 8px;"><div class="xp-level-box" style="width: 100%; text-align: center; margin-top: 2px;"><div class="xp-level-label" style="font-weight: 700; font-size: 13px; color: rgb(255, 217, 61); letter-spacing: 0.04em; margin-bottom: 2px;">Level 3 / 20</div><div class="xp-bar-bg" style="width: 80%; height: 8px; background: rgba(102, 126, 234, 0.13); border-radius: 8px; margin: 0px auto; position: relative; overflow: hidden;"><div class="xp-bar-fill" style="width: 60%; height: 100%; background: linear-gradient(90deg, rgb(255, 217, 61) 0%, rgb(102, 126, 234) 100%); border-radius: 8px; transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);"></div></div><div class="xp-label" style="font-size: 11px; color: rgb(191, 199, 213); margin-top: 2px;">60 / 100 XP</div></div></div><a class="nav-item active" href="http://localhost:3000/"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-home"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg><span>Dashboard</span></a><a class="nav-item " href="http://localhost:3000/budget"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-dollar-sign"><line x1="12" x2="12" y1="2" y2="22"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg><span>Budget</span></a><a class="nav-item " href="http://localhost:3000/fitness"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-activity"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg><span>Fitness</span></a><a class="nav-item " href="http://localhost:3000/water"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-droplets"><path d="M7 16.3c2.2 0 4-1.83 4-4.05 0-1.16-.57-2.26-1.71-3.19S7.29 6.75 7 5.3c-.29 1.45-1.14 2.84-2.29 3.76S3 11.1 3 12.25c0 2.22 1.8 4.05 4 4.05z"></path><path d="M12.56 6.6A10.97 10.97 0 0 0 14 3.02c.5 2.5 2 4.9 4 6.5s3 3.5 3 5.5a6.98 6.98 0 0 1-11.91 4.97"></path></svg><span>Water</span></a><a class="nav-item " href="http://localhost:3000/sleep"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-moon"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"></path></svg><span>Sleep</span></a><a class="nav-item " href="http://localhost:3000/goals"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-target"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg><span>Goals</span></a><a class="nav-item " href="http://localhost:3000/habits"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-trending-up"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"></polyline><polyline points="16 7 22 7 22 13"></polyline></svg><span>Habits</span></a><a class="nav-item " href="http://localhost:3000/pomodoro"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-clock"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg><span>Work Timer</span></a><a class="nav-item " href="http://localhost:3000/notes"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-sticky-note"><path d="M15.5 3H5a2 2 0 0 0-2 2v14c0 1.1.9 2 2 2h14a2 2 0 0 0 2-2V8.5L15.5 3Z"></path><path d="M15 3v6h6"></path></svg><span>Notes</span></a><a class="nav-item " href="http://localhost:3000/mood"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-heart"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></svg><span>Mood</span></a><a class="nav-item " href="http://localhost:3000/achievements"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-trophy"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path></svg><span>Achievements</span></a></div></nav><button class="settings-btn settings-bubble" title="Settings" style="position: absolute; top: 20px; right: 24px; background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 50%; width: 48px; height: 48px; cursor: pointer; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(10px); box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 12px; transition: 0.3s;"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-settings"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"></path><circle cx="12" cy="12" r="3"></circle></svg></button><main class="main-content"><div class="container"><div class="card"><div class="flex flex-between mb-2"><h1 class="text-xl">Dashboard</h1><span class="text-gray">Wednesday, July 9th</span></div><div class="customize-row mb-6"><button class="customize-btn " title="Customize Dashboard"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-settings"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"></path><circle cx="12" cy="12" r="3"></circle></svg>Customize</button></div><div class="widgets-container"><div class="widget-container mb-6" draggable="false" style="opacity: 1; cursor: default; transform: none; background: transparent; box-shadow: none; border: none;"><div class="widget-header"><div class="widget-controls"><div class="widget-title">Quick Stats</div><div class="widget-actions"></div></div></div><div class="widget-content"><div class="grid grid-3 mb-4"><div class="card" style="background: linear-gradient(135deg, rgb(102, 126, 234) 0%, rgb(118, 75, 162) 100%); color: white;"><div class="flex flex-between"><div><p class="text-gray" style="color: rgba(255, 255, 255, 0.8);">Budget</p><h3 class="text-lg">$0</h3><p style="font-size: 12px; opacity: 0.8;">of $2000</p></div><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-dollar-sign"><line x1="12" x2="12" y1="2" y2="22"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div><div class="progress-bar mt-4" style="background: rgba(255, 255, 255, 0.2);"><div class="progress-fill" style="width: 0%; background: white;"></div></div></div><div class="card" style="background: linear-gradient(135deg, rgb(76, 175, 80) 0%, rgb(69, 160, 73) 100%); color: white;"><div class="flex flex-between"><div><p class="text-gray" style="color: rgba(255, 255, 255, 0.8);">Water</p><h3 class="text-lg">0L</h3><p style="font-size: 12px; opacity: 0.8;">of 8L</p></div><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-droplets"><path d="M7 16.3c2.2 0 4-1.83 4-4.05 0-1.16-.57-2.26-1.71-3.19S7.29 6.75 7 5.3c-.29 1.45-1.14 2.84-2.29 3.76S3 11.1 3 12.25c0 2.22 1.8 4.05 4 4.05z"></path><path d="M12.56 6.6A10.97 10.97 0 0 0 14 3.02c.5 2.5 2 4.9 4 6.5s3 3.5 3 5.5a6.98 6.98 0 0 1-11.91 4.97"></path></svg></div><div class="progress-bar mt-4" style="background: rgba(255, 255, 255, 0.2);"><div class="progress-fill" style="width: 0%; background: white;"></div></div></div><div class="card" style="background: linear-gradient(135deg, rgb(255, 152, 0) 0%, rgb(245, 124, 0) 100%); color: white;"><div class="flex flex-between"><div><p class="text-gray" style="color: rgba(255, 255, 255, 0.8);">Fitness</p><h3 class="text-lg">0</h3><p style="font-size: 12px; opacity: 0.8;">of 10,000</p></div><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-activity"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg></div><div class="progress-bar mt-4" style="background: rgba(255, 255, 255, 0.2);"><div class="progress-fill" style="width: 0%; background: white;"></div></div></div></div></div></div><div class="widget-container mb-6" draggable="false" style="opacity: 1; cursor: default; transform: none; background: transparent; box-shadow: none; border: none;"><div class="widget-header"><div class="widget-controls"><div class="widget-title">Quick Actions</div><div class="widget-actions"></div></div></div><div class="widget-content"><div class="card"><h2 class="text-lg mb-4">Quick Actions</h2><div class="grid grid-2"><button class="btn" title="Quickly add a new expense to your budget" style="background: rgb(102, 126, 234);"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-plus"><path d="M5 12h14"></path><path d="M12 5v14"></path></svg>Add Expense</button><button class="btn" title="Quickly log 0.5L of water intake" style="background: rgb(76, 175, 80);"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-droplets"><path d="M7 16.3c2.2 0 4-1.83 4-4.05 0-1.16-.57-2.26-1.71-3.19S7.29 6.75 7 5.3c-.29 1.45-1.14 2.84-2.29 3.76S3 11.1 3 12.25c0 2.22 1.8 4.05 4 4.05z"></path><path d="M12.56 6.6A10.97 10.97 0 0 0 14 3.02c.5 2.5 2 4.9 4 6.5s3 3.5 3 5.5a6.98 6.98 0 0 1-11.91 4.97"></path></svg>Log Water</button><button class="btn" title="Log a new workout session" style="background: rgb(255, 152, 0);"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-activity"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>Log Workout</button><button class="btn" title="Log your sleep duration and quality" style="background: rgb(156, 39, 176);"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-moon"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"></path></svg>Log Sleep</button></div></div></div></div><div class="widget-container mb-6" draggable="false" style="opacity: 1; cursor: default; transform: none; background: transparent; box-shadow: none; border: none;"><div class="widget-header"><div class="widget-controls"><div class="widget-title">Goals Summary</div><div class="widget-actions"></div></div></div><div class="widget-content"><div class="card"><h2 class="text-lg mb-4">Goals Summary</h2><div class="grid grid-3 mb-4"><div class="text-center p-3 bg-blue-50 rounded-lg"><h3 class="text-lg font-bold text-blue-600">0</h3><p class="text-sm text-gray-600">Active Goals</p></div><div class="text-center p-3 bg-green-50 rounded-lg"><h3 class="text-lg font-bold text-green-600">0</h3><p class="text-sm text-gray-600">Completed</p></div><div class="text-center p-3 bg-orange-50 rounded-lg"><h3 class="text-lg font-bold text-orange-600">0.0%</h3><p class="text-sm text-gray-600">Overall Progress</p></div></div><p class="text-gray text-center">No active goals</p></div></div></div><div class="widget-container mb-6" draggable="false" style="opacity: 1; cursor: default; transform: none; background: transparent; box-shadow: none; border: none;"><div class="widget-header"><div class="widget-controls"><div class="widget-title">Weekly Overview</div><div class="widget-actions"></div></div></div><div class="widget-content"><div class="card"><h2 class="text-lg mb-4">Weekly Overview</h2><div class="recharts-responsive-container" style="width: 100%; height: 300px; min-width: 0px;"><div class="recharts-wrapper" style="position: relative; cursor: default; width: 100%; height: 100%; max-height: 300px; max-width: 1057px;"><svg class="recharts-surface" width="1057" height="300" viewBox="0 0 1057 300" style="width: 100%; height: 100%;"><title></title><desc></desc><defs><clippath id="recharts32-clip"><rect x="65" y="5" height="260" width="987"></rect></clippath></defs><g class="recharts-cartesian-grid"><g class="recharts-cartesian-grid-horizontal"><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="65" y1="265" x2="1052" y2="265"></line><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="65" y1="200" x2="1052" y2="200"></line><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="65" y1="135" x2="1052" y2="135"></line><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="65" y1="70" x2="1052" y2="70"></line><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="65" y1="5" x2="1052" y2="5"></line></g><g class="recharts-cartesian-grid-vertical"><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="65" y1="5" x2="65" y2="265"></line><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="229.5" y1="5" x2="229.5" y2="265"></line><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="394" y1="5" x2="394" y2="265"></line><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="558.5" y1="5" x2="558.5" y2="265"></line><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="723" y1="5" x2="723" y2="265"></line><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="887.5" y1="5" x2="887.5" y2="265"></line><line stroke-dasharray="3 3" stroke="#ccc" fill="none" x="65" y="5" width="987" height="260" x1="1052" y1="5" x2="1052" y2="265"></line></g></g><g class="recharts-layer recharts-cartesian-axis recharts-xAxis xAxis"><line orientation="bottom" width="987" height="30" x="65" y="265" class="recharts-cartesian-axis-line" stroke="#666" fill="none" x1="65" y1="265" x2="1052" y2="265"></line><g class="recharts-cartesian-axis-ticks"><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="bottom" width="987" height="30" x="65" y="265" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="65" y1="271" x2="65" y2="265"></line><text orientation="bottom" width="987" height="30" stroke="none" x="65" y="273" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="middle" fill="#666"><tspan x="65" dy="0.71em">Mon</tspan></text></g><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="bottom" width="987" height="30" x="65" y="265" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="229.5" y1="271" x2="229.5" y2="265"></line><text orientation="bottom" width="987" height="30" stroke="none" x="229.5" y="273" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="middle" fill="#666"><tspan x="229.5" dy="0.71em">Tue</tspan></text></g><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="bottom" width="987" height="30" x="65" y="265" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="394" y1="271" x2="394" y2="265"></line><text orientation="bottom" width="987" height="30" stroke="none" x="394" y="273" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="middle" fill="#666"><tspan x="394" dy="0.71em">Wed</tspan></text></g><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="bottom" width="987" height="30" x="65" y="265" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="558.5" y1="271" x2="558.5" y2="265"></line><text orientation="bottom" width="987" height="30" stroke="none" x="558.5" y="273" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="middle" fill="#666"><tspan x="558.5" dy="0.71em">Thu</tspan></text></g><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="bottom" width="987" height="30" x="65" y="265" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="723" y1="271" x2="723" y2="265"></line><text orientation="bottom" width="987" height="30" stroke="none" x="723" y="273" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="middle" fill="#666"><tspan x="723" dy="0.71em">Fri</tspan></text></g><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="bottom" width="987" height="30" x="65" y="265" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="887.5" y1="271" x2="887.5" y2="265"></line><text orientation="bottom" width="987" height="30" stroke="none" x="887.5" y="273" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="middle" fill="#666"><tspan x="887.5" dy="0.71em">Sat</tspan></text></g><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="bottom" width="987" height="30" x="65" y="265" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="1052" y1="271" x2="1052" y2="265"></line><text orientation="bottom" width="987" height="30" stroke="none" x="1042.40625" y="273" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="middle" fill="#666"><tspan x="1042.40625" dy="0.71em">Sun</tspan></text></g></g></g><g class="recharts-layer recharts-cartesian-axis recharts-yAxis yAxis"><line orientation="left" width="60" height="260" x="5" y="5" class="recharts-cartesian-axis-line" stroke="#666" fill="none" x1="65" y1="5" x2="65" y2="265"></line><g class="recharts-cartesian-axis-ticks"><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="left" width="60" height="260" x="5" y="5" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="59" y1="265" x2="65" y2="265"></line><text orientation="left" width="60" height="260" stroke="none" x="57" y="265" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="end" fill="#666"><tspan x="57" dy="0.355em">0</tspan></text></g><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="left" width="60" height="260" x="5" y="5" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="59" y1="200" x2="65" y2="200"></line><text orientation="left" width="60" height="260" stroke="none" x="57" y="200" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="end" fill="#666"><tspan x="57" dy="0.355em">3000</tspan></text></g><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="left" width="60" height="260" x="5" y="5" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="59" y1="135" x2="65" y2="135"></line><text orientation="left" width="60" height="260" stroke="none" x="57" y="135" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="end" fill="#666"><tspan x="57" dy="0.355em">6000</tspan></text></g><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="left" width="60" height="260" x="5" y="5" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="59" y1="70" x2="65" y2="70"></line><text orientation="left" width="60" height="260" stroke="none" x="57" y="70" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="end" fill="#666"><tspan x="57" dy="0.355em">9000</tspan></text></g><g class="recharts-layer recharts-cartesian-axis-tick"><line orientation="left" width="60" height="260" x="5" y="5" class="recharts-cartesian-axis-tick-line" stroke="#666" fill="none" x1="59" y1="5" x2="65" y2="5"></line><text orientation="left" width="60" height="260" stroke="none" x="57" y="9.600000381469727" class="recharts-text recharts-cartesian-axis-tick-value" text-anchor="end" fill="#666"><tspan x="57" dy="0.355em">12000</tspan></text></g></g></g><g class="recharts-layer recharts-line"><path stroke="#FF9800" stroke-width="2" fill="none" width="987" height="260" class="recharts-curve recharts-line-curve" stroke-dasharray="1033.0069580078125px 0px" d="M65,80.833C119.833,73.25,174.667,65.667,229.5,65.667C284.333,65.667,339.167,96,394,96C448.833,96,503.667,37.5,558.5,37.5C613.333,37.5,668.167,72.167,723,72.167C777.833,72.167,832.667,5,887.5,5C942.333,5,997.167,32.083,1052,59.167"></path><g class="recharts-layer"></g><g class="recharts-layer recharts-line-dots"><circle r="3" stroke="#FF9800" stroke-width="2" fill="#fff" width="987" height="260" cx="65" cy="80.83333333333333" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#FF9800" stroke-width="2" fill="#fff" width="987" height="260" cx="229.5" cy="65.66666666666666" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#FF9800" stroke-width="2" fill="#fff" width="987" height="260" cx="394" cy="96" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#FF9800" stroke-width="2" fill="#fff" width="987" height="260" cx="558.5" cy="37.5" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#FF9800" stroke-width="2" fill="#fff" width="987" height="260" cx="723" cy="72.16666666666666" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#FF9800" stroke-width="2" fill="#fff" width="987" height="260" cx="887.5" cy="5" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#FF9800" stroke-width="2" fill="#fff" width="987" height="260" cx="1052" cy="59.16666666666668" class="recharts-dot recharts-line-dot"></circle></g></g><g class="recharts-layer recharts-line"><path stroke="#4CAF50" stroke-width="2" fill="none" width="987" height="260" class="recharts-curve recharts-line-curve" stroke-dasharray="987px 0px" d="M65,264.848C119.833,264.838,174.667,264.827,229.5,264.827C284.333,264.827,339.167,264.87,394,264.87C448.833,264.87,503.667,264.805,558.5,264.805C613.333,264.805,668.167,264.819,723,264.827C777.833,264.834,832.667,264.848,887.5,264.848C942.333,264.848,997.167,264.838,1052,264.827"></path><g class="recharts-layer"></g><g class="recharts-layer recharts-line-dots"><circle r="3" stroke="#4CAF50" stroke-width="2" fill="#fff" width="987" height="260" cx="65" cy="264.84833333333336" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#4CAF50" stroke-width="2" fill="#fff" width="987" height="260" cx="229.5" cy="264.82666666666665" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#4CAF50" stroke-width="2" fill="#fff" width="987" height="260" cx="394" cy="264.87" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#4CAF50" stroke-width="2" fill="#fff" width="987" height="260" cx="558.5" cy="264.805" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#4CAF50" stroke-width="2" fill="#fff" width="987" height="260" cx="723" cy="264.82666666666665" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#4CAF50" stroke-width="2" fill="#fff" width="987" height="260" cx="887.5" cy="264.84833333333336" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#4CAF50" stroke-width="2" fill="#fff" width="987" height="260" cx="1052" cy="264.82666666666665" class="recharts-dot recharts-line-dot"></circle></g></g><g class="recharts-layer recharts-line"><path stroke="#9C27B0" stroke-width="2" fill="none" width="987" height="260" class="recharts-curve recharts-line-curve" stroke-dasharray="987px 0px" d="M65,264.838C119.833,264.832,174.667,264.827,229.5,264.827C284.333,264.827,339.167,264.848,394,264.848C448.833,264.848,503.667,264.816,558.5,264.816C613.333,264.816,668.167,264.838,723,264.838C777.833,264.838,832.667,264.805,887.5,264.805C942.333,264.805,997.167,264.816,1052,264.827"></path><g class="recharts-layer"></g><g class="recharts-layer recharts-line-dots"><circle r="3" stroke="#9C27B0" stroke-width="2" fill="#fff" width="987" height="260" cx="65" cy="264.83750000000003" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#9C27B0" stroke-width="2" fill="#fff" width="987" height="260" cx="229.5" cy="264.82666666666665" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#9C27B0" stroke-width="2" fill="#fff" width="987" height="260" cx="394" cy="264.84833333333336" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#9C27B0" stroke-width="2" fill="#fff" width="987" height="260" cx="558.5" cy="264.81583333333333" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#9C27B0" stroke-width="2" fill="#fff" width="987" height="260" cx="723" cy="264.83750000000003" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#9C27B0" stroke-width="2" fill="#fff" width="987" height="260" cx="887.5" cy="264.805" class="recharts-dot recharts-line-dot"></circle><circle r="3" stroke="#9C27B0" stroke-width="2" fill="#fff" width="987" height="260" cx="1052" cy="264.82666666666665" class="recharts-dot recharts-line-dot"></circle></g></g></svg><div tabindex="-1" class="recharts-tooltip-wrapper recharts-tooltip-wrapper-right recharts-tooltip-wrapper-bottom" style="visibility: hidden; pointer-events: none; position: absolute; top: 0px; left: 0px; transform: translate(65px, 10px);"><div class="recharts-default-tooltip" style="margin: 0px; padding: 10px; background-color: rgb(255, 255, 255); border: 1px solid rgb(204, 204, 204); white-space: nowrap;"><p class="recharts-tooltip-label" style="margin: 0px;"></p></div></div></div></div></div></div></div><div class="widget-container mb-6" draggable="false" style="opacity: 1; cursor: default; transform: none; background: transparent; box-shadow: none; border: none;"><div class="widget-header"><div class="widget-controls"><div class="widget-title">Recent Activities</div><div class="widget-actions"></div></div></div><div class="widget-content"><div class="card"><h2 class="text-lg mb-4">Recent Activities</h2><p class="text-gray text-center">No recent activities</p></div></div></div></div></div></div></main></div></div>
  
 <span id="recharts_measurement_span" aria-hidden="true" style="position: absolute; top: -20000px; left: 0px; padding: 0px; margin: 0px; border: none; white-space: pre; font-size: 16px; letter-spacing: normal;">6</span></body></html>